---
name: elementor-weekly-menu-engine
description: Arquitectura técnica y motor de rotación semanal de menú en WooCommerce y Elementor Loop Grids para Eat&Go. Garantiza control nativo en Elementor, filtrado dinámico por semana activa, cambio de día instantáneo sin recarga (0-reload), regla de domingo y anti-lazyloading.
---

# Elementor Weekly Menu Engine - Eat&Go Architecture

Este skill define la arquitectura maestra para la gestión, rotación semanal y visualización interactiva del **Menú Semanal** (`/menu-semanal/`, Post 564) en WordPress/WooCommerce y Elementor Pro.

---

## 1. PRINCIPIO DE ARQUITECTURA LIMPIA (ANTI-SOBREINGENIERÍA)

### ⛔ PROHIBICIONES ESTRICTAS EN BACKEND / PHP:
1. **JAMÁS forzar `posts_per_page` en el hook PHP:**
   - La cantidad de platos a mostrar (ej. 3, 6, 12 o todos) la gobierna el usuario o diseñador directamente desde la barra lateral de configuración del widget `loop-grid` en Elementor.
   - Forzar `posts_per_page` en PHP secuestra el widget e impide crear cuadrículas de 2 filas (6 platos) cuando la cocina publica sopas o platos adicionales.
2. **JAMÁS forzar `orderby` u `order` en el hook PHP:**
   - Elementor Pro incluye controles nativos para ordenar por Fecha, Menú Order, Título o Aleatorio. PHP no debe sobreescribir esta decisión visual.
3. **Rol Exclusivo del Hook PHP:**
   - El hook `elementor/query/{query_id}` tiene un único propósito: **filtrar por la taxonomía dinámica `product_cat` de acuerdo con la semana activa del calendario.**

---

## 2. ESQUEMA DE CATEGORÍAS EN WOOCOMMERCE

La rotación de cocina opera con slugs fijos combinados por día y número de semana:

| Día | Slug Semana 1 | Slug Semana 2 | Fallback General |
| :--- | :--- | :--- | :--- |
| **Lunes** | `lunes-1` *(Sopas & Caldos)* | `lunes-2` *(Sancocho / Menestras)* | `lunes` |
| **Martes** | `martes-1` *(Mondongo / Guisados)* | `martes-2` *(Carne Entomatada)* | `martes` |
| **Miércoles** | `miercoles-1` *(Paila Criolla / Asados)* | `miercoles-2` *(Lechona / Cerdo)* | `miercoles` |
| **Jueves** | `jueves-1` *(Costillas / Pastas)* | `jueves-2` *(Ahumados / Aves)* | `jueves` |
| **Viernes** | `viernes-1` *(Mariscos / Pescado Frito)* | `viernes-2` *(Arroz con Mariscos)* | `viernes` |
| **Sábado** | `sabado-1` *(Paila Familiar)* | `sabado-2` *(Fiesta Criolla)* | `semana-{$semana}` / `semana-1` |

### Resolución con Operador `IN`:
Para evitar que platos multi-categorizados (como sopas o platos presentes en varias semanas) queden excluidos, el hook debe consultar con `operator: IN`:
```php
$terms_to_query = [$category_slug];
if (strpos($category_slug, '-1') !== false || $category_slug === $dia) {
    $terms_to_query = array_unique([$category_slug, "{$dia}-1", $dia]);
}
```

---

## 3. MOTOR PHP Y HOOKS DE ELEMENTOR (`eatgo-weekly-rotation-engine.php`)

Ubicación: `wp-content/mu-plugins/eatgo-weekly-rotation-engine.php` (o Code Snippet global de prioridad 1).

### Código Oficial del Motor de Consulta:
```php
<?php
/**
 * Plugin Name: Eat&Go Weekly Rotation Query Engine
 * Description: Motor de rotación semanal de menú y hooks de consulta para Loop Grids en Elementor.
 * Version: 3.0.0
 * Author: Eat&Go Criollo Express
 */
if (!defined('ABSPATH')) exit;

// 1. OBTENER SEMANA ACTIVA (Automática o Forzada por Ajuste)
if (!function_exists('eatgo_get_active_week')) {
    function eatgo_get_active_week() {
        $option = get_option('eatgo_semana_activa', 'auto');
        if ($option === '1' || $option === '2') {
            return $option;
        }
        // Semanas impares del año = Semana 1; Semanas pares = Semana 2
        return (intval(date('W')) % 2 !== 0) ? '1' : '2';
    }
}

// 2. REGISTRAR SELECTOR EN AJUSTES -> GENERAL
add_action('init', function() {
    register_setting('general', 'eatgo_semana_activa', [
        'type' => 'string',
        'sanitize_callback' => 'sanitize_text_field',
        'default' => 'auto',
        'show_in_rest' => true
    ]);
});

add_action('admin_init', function() {
    add_settings_section(
        'eatgo_weekly_settings_section',
        '🍽️ Eat&Go: Configuración de Menú Semanal',
        function() {
            echo '<p>Controla la rotación automática según el calendario o fuerza una semana fija para la cocina.</p>';
        },
        'general'
    );

    add_settings_field(
        'eatgo_semana_activa',
        'Semana Activa del Menú',
        function() {
            $val = get_option('eatgo_semana_activa', 'auto');
            $auto_val = (intval(date('W')) % 2 !== 0) ? '1' : '2';
            ?>
            <select name="eatgo_semana_activa" id="eatgo_semana_activa">
                <option value="auto" <?php selected($val, 'auto'); ?>>Automática por Calendario (Actualmente Semana <?php echo $auto_val; ?>)</option>
                <option value="1" <?php selected($val, '1'); ?>>Forzar Semana 1 (lunes-1, martes-1, etc.)</option>
                <option value="2" <?php selected($val, '2'); ?>>Forzar Semana 2 (lunes-2, martes-2, etc.)</option>
            </select>
            <p class="description">Semana actual del año: <?php echo date('W'); ?>.</p>
            <?php
        },
        'general',
        'eatgo_weekly_settings_section'
    );
});

// 3. HOOKS DE CONSULTA PARA LOOP GRIDS (query_menu_lunes, query_menu_martes, etc.)
$dias_semana = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado'];

foreach ($dias_semana as $dia) {
    add_action("elementor/query/query_menu_{$dia}", function($query) use ($dia) {
        $semana = eatgo_get_active_week();
        $category_slug = "{$dia}-{$semana}";

        // Fallbacks automáticos si la categoría aún no tiene productos cargados
        $term = get_term_by('slug', $category_slug, 'product_cat');
        if (!$term || $term->count == 0) {
            $fallback_term = get_term_by('slug', "{$dia}-1", 'product_cat');
            if ($fallback_term && $fallback_term->count > 0) {
                $category_slug = "{$dia}-1";
            } else {
                $dia_term = get_term_by('slug', $dia, 'product_cat');
                if ($dia_term && $dia_term->count > 0) {
                    $category_slug = $dia;
                } else {
                    $category_slug = "semana-{$semana}";
                    $sem_term = get_term_by('slug', $category_slug, 'product_cat');
                    if (!$sem_term || $sem_term->count == 0) {
                        $category_slug = 'semana-1';
                    }
                }
            }
        }

        $terms_to_query = [$category_slug];
        if (strpos($category_slug, '-1') !== false || $category_slug === $dia) {
            $terms_to_query = array_unique([$category_slug, "{$dia}-1", $dia]);
        }

        // Configuración mínima esencial (CERO sobreescritura de paginación u orden)
        $query->set('post_type', 'product');
        $query->set('post_status', 'publish');

        $tax_query = (array) $query->get('tax_query');
        $tax_query[] = [
            'taxonomy' => 'product_cat',
            'field'    => 'slug',
            'terms'    => $terms_to_query,
            'operator' => 'IN',
        ];

        $query->set('tax_query', $tax_query);
    });
}
```

---

## 4. INTEGRACIÓN CON WIDGET LOOP GRID (ELEMENTOR)

Para cada contenedor de día (`grid-lunes`, `grid-martes`, etc.):
1. **Widget:** `loop-grid` nativo de Elementor.
2. **Template ID:** `631` (`Eat&Go – Card Menú Semanal`).
3. **Query Settings del Widget:**
   - Source: `product` / `Productos de WooCommerce`.
   - Query ID: `query_menu_{dia}` (ej. `query_menu_lunes`, `query_menu_martes`...).
   - Columns: `3` (Desktop) y `1` (Móvil).
   - Items por página: `6` o `12` para acomodar 2 o más filas de 3 platos cuando hay sopas y especiales.

---

## 5. FRONTEND INTERACTIVO (0-RECARGA DE PÁGINA)

El script de frontend (`elementor_snippet 660` o equivalente) gestiona el cambio instantáneo de días:

1. **Regla de Domingo:**
   - Si `new Date().getDay() === 0` (domingo con cocina cerrada), activar **LUNES** por defecto para captar pedidos anticipados.
2. **Switching Instantáneo de Grillas:**
   - Cada contenedor de día (`[data-id="12dc898b"]`, etc.) se mapea en un objeto `gridMap`.
   - Al hacer clic en cualquier píldora de día:
     - Se actualiza la clase `.is-active` y estilos visuales de la píldora.
     - Se actualiza el título y badge del banner (`MENÚ DEL LUNES`, etc.).
     - Se ocultan las otras grillas y se muestra con `.fadeIn(180)` la grilla seleccionada.
     - Se cuenta dinámicamente la cantidad de `.e-loop-item` visibles y se actualiza el subtítulo: `🗓️ Semana X del Mes • N especialidades preparadas hoy`.
3. **WPC Quick View (`.woosq-btn`):**
   - Extraer el ID de WooCommerce con Regex `post-(\d+)` del contenedor `.e-loop-item` o clase de producto.
   - Disparar `woosq_open(pid)`.
4. **⛔ PROHIBICIÓN ESTRICTA DE MANIPULACIÓN JS DE IMÁGENES:**
   - **Prohibido** usar diccionarios de imágenes (`knownImages`) o sobreescribir el DOM de las tarjetas por índice numérico (`renderPlatosDia` o `$cards.eq(idx)`).
   - Manipular el DOM con arrays por índice desalinea y cruza los títulos y fotos respecto a WooCommerce.
   - Toda imagen de cabecera (`c02covr`) debe ser gobernada exclusivamente de forma **nativa por CSS** asociado a la clase de producto `.post-{ID}` o `.e-loop-item-{ID}`:
     ```css
     .page-id-564 .post-154 [data-id="c02covr"] {
       background-image: url("https://eatgopty.com/.../Costilla-BBQ_EatGo2.png") !important;
     }
     ```
5. **Anti-Fondo Gris (Layout CSS Override):**
   ```css
   .elementor-element-c02covr,
   [data-id="c02covr"],
   .e-loop-item [data-id="c02covr"] {
     background-size: cover !important;
     background-position: center center !important;
     background-repeat: no-repeat !important;
     opacity: 1 !important;
     min-height: 220px !important;
   }
   ```

---

## 6. CHECKLIST DE VERIFICACIÓN PARA NUEVAS IMPLEMENTACIONES

- [ ] ¿El hook PHP en `query_menu_{dia}` carece por completo de `posts_per_page`, `orderby` y `order`?
- [ ] ¿El widget Loop Grid en Elementor tiene asignado el `Query ID` correspondiente (`query_menu_lunes`, etc.)?
- [ ] ¿El límite de ítems en Elementor permite visualizar todas las especialidades del día (incluyendo sopas y platos secundarios)?
- [ ] ¿El script de frontend respeta la **prohibición absoluta** de manipular fotos o títulos por JS?
- [ ] ¿Cada plato en `https://eatgopty.com/menu-semanal/` coincide exactamente con su foto real de WooCommerce (Costilla con Costilla, Sopa con Sopa)?
- [ ] ¿El botón de compra contiene el icono SVG `bag.svg` y abre el modal de Quick View sin recargar la página?
- [ ] ¿Se ejecutó `wp_cache_clear` tras actualizar el backend o Snippets?
