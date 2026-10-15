# Regla de Arquitectura y Negocio: Menú del Día (`/menu-del-dia/`)

## 1. Contexto e Identificadores del Sistema
- **URL Canónica:** `https://eatgopty.com/menu-del-dia/`
- **Post ID en WordPress:** `724`
- **Tipo de Post:** `page`
- **Plantilla de Página:** `elementor_header_footer`
- **Query ID en Elementor Loop Grid:** `menu_del_dia_auto`
- **Snippet Backend (Code Snippets Pro):** Snippet ID `5` (respaldo local en `snippet_5_engine.php`)
- **JSON de Respaldo Elementor:** `pagina_menu_del_dia.json` (en la raíz del proyecto local)

---

## 2. Regla de Aislamiento Estricto (PROHIBICIONES)
Al trabajar, ajustar o iterar sobre la página `/menu-del-dia/`:
1. **PROHIBIDO modificar el Post ID 58** (Página de Inicio / Home).
2. **PROHIBIDO modificar el Post ID 564** (Página Menú Semanal).
3. **PROHIBIDO alterar directamente la Plantilla Loop Item 631** (`loop-item-plato-menu`), ya que es compartida con otras vistas.
4. Toda lógica visual específica de la página debe residir dentro del JSON/configuración de la página 724 o el Query Hook de Elementor.

---

## 3. Lógica del Motor Backend (Snippet ID 5)
La consulta de productos es interceptada a través del hook nativo de Elementor:
`add_action('elementor/query/menu_del_dia_auto', 'eatgo_filter_menu_del_dia_auto');`

### 3.1. Detección de Tiempo y Zona Horaria
- Toda resolución temporal DEBE realizarse con zona horaria estricta: `America/Panama` (`new DateTime('now', new DateTimeZone('America/Panama'))`).
- Prohibido usar `date()` directo del servidor sin forzar la zona horaria de Panamá.

### 3.2. Regla de Negocio del Domingo
- Si el día actual es **Domingo** (cocina cerrada), la consulta DEBE resolver automáticamente al **Lunes** siguiente para permitir la preventa y pedidos anticipados de oficina.

### 3.3. Detección de Semana Activa
- **Opción de WordPress:** Consulta primero `get_option('eatgo_semana_activa')`.
- **Cálculo de Calendario:** Si no está configurada, calcula el ciclo de 2 semanas:
  - Semana impar del año (`date('W') % 2 !== 0`) ➔ Semana `1`.
  - Semana par del año (`date('W') % 2 === 0`) ➔ Semana `2`.

### 3.4. Matriz de Sobrescritura por Parámetros URL (`$_GET`)
El motor debe permitir navegación directa o forzada para soporte y testing:
1. `?dia=[lunes|martes|miercoles|jueves|viernes]`
   - Si se especifica, fuerza la consulta al día solicitado.
   - Mantiene la semana activa por defecto si `&semana=` no se pasa.
2. `?semana=[1|2|3|4]`
   - Si se especifica, fuerza la semana solicitada (ej. `&semana=1` muestra platos de semana 1).
3. **Mapeo de Categoría WooCommerce (`product_cat`):**
   - El slug de categoría objetivo se construye estrictamente como: `[dia]-[semana]` (ej. `lunes-1`, `lunes-2`, `martes-1`, etc.).

---

## 4. Gobernanza Visual y Frontend (Elementor)
Siguiendo las directrices de `elementor-native-governance` y `elementor-loopgrid-architect`:
1. **Controles Nativos:**
   - La disposición de columnas del Loop Grid debe usar 1 columna en móvil (`columns_mobile: "1"`) y 3 en desktop (`columns: 3`).
   - Prohibido secuestrar estilos o layouts con `!important` en CSS externo.
2. **Soporte Anti-Lazyload de Elementor:**
   - Para evitar que los contenedores de imagen de la plantilla 631 queden en gris (`.elementor-element-c02covr`), la página 724 incluye un mapa de imágenes precargadas de los platos con clases `.e-lazyloaded .e-no-lazyload` y fallback asíncrono a `/wp-json/eatgo/v1/menu-semanal`.
3. **Interacciones WooCommerce:**
   - Se debe mantener la integración con WPC Quick View delegando el evento click en botones `.woosq-btn` invocando `woosq_open(productId)`.
   - La barra inferior flotante de comanda (`.elementor-element-m11stkc`) debe permanecer fija en la parte inferior para accesibilidad rápida del pedido en móviles y desktop.

---

## 5. Protocolo de Re-sincronización y Recuperación
Si la página sufriera alguna desconfiguración o alteración externa:
1. **Restaurar Snippet:** Enviar el código de `snippet_5_engine.php` a la REST API de Code Snippets (`POST https://eatgopty.com/wp-json/code-snippets/v1/snippets/5`).
2. **Restaurar Estructura Elementor:** Actualizar el Post ID 724 (`_elementor_data`) con el contenido de `pagina_menu_del_dia.json`.
3. **Limpieza de Caché:** Ejecutar `wp_cache_clear` vía MCP para invalidar cualquier caché de transients o páginas estáticas.
