# Regla de Arquitectura y Negocio: Menú Semanal (`/menu-semanal/`)

## 1. Contexto e Identificadores del Sistema
- **URL Canónica:** `https://eatgopty.com/menu-semanal/`
- **Post ID en WordPress:** `564`
- **Tipo de Post:** `page`
- **Plantilla de Página:** `elementor_header_footer`
- **Plantilla Loop Item:** Post ID `631` (`loop-item-plato-menu`)
- **Query IDs Backend:** `query_menu_lunes`, `query_menu_martes`, `query_menu_miercoles`, `query_menu_jueves`, `query_menu_viernes`, `query_menu_sabado`
- **Motor PHP Backend:** Code Snippet ID `5` (`EatGo Weekly Rotation Query Engine`, respaldo en `snippet_5_engine.php`)
- **Motor JS Frontend Interactivo:** Elementor Custom Code ID `660` (`EatGo Menú Semanal Motor Interactivo Dinámico`)
- **REST API Endpoint de Menú Semanal:** `/wp-json/eatgo/v1/menu-semanal`

---

## 2. Regla de Aislamiento Estricto (PROHIBICIONES)
Al trabajar, ajustar o iterar sobre el Menú Semanal:
1. **PROHIBIDO modificar el Post ID 58** (Home / Inicio) ni alterar el Post ID 724 (Menú del Día).
2. **PROHIBIDO forzar `posts_per_page` o `orderby` en el hook PHP:**
   - La cantidad de platos a mostrar la gobierna el diseñador desde el widget `loop-grid` de Elementor (ej. 3, 4, 6 o 12).
   - Forzar `posts_per_page` en PHP secuestra el widget e impide mostrar filas completas cuando la cocina añade platos.
3. **PROHIBIDO alterar la estructura base de la Plantilla 631** sin verificar su impacto en Home (58), Menú del Día (724) y Menú Semanal (564).

---

## 3. Lógica del Motor Backend (Snippet ID 5)
El backend intercepta las consultas de cada grilla con hooks dedicados:
`elementor/query/query_menu_{dia}` (donde `{dia}` es `lunes`, `martes`, etc.).

### 3.1. Detección de Semana Activa
- **Opción de WordPress:** `get_option('eatgo_semana_activa')`. Permite fijar `1` o `2` desde Ajustes Generales.
- **Cálculo Automático por Calendario:**
  - Si está en `auto`, evalúa `(intval(date('W')) % 2 !== 0) ? '1' : '2'`.
  - Zona horaria de cálculo: `America/Panama`.

### 3.2. Taxonomía de Categorías WooCommerce (`product_cat`)
- Slugs por día y semana: `lunes-1`, `lunes-2`, `martes-1`, `martes-2`, etc.
- Consulta con operador `IN` y fallbacks ordenados:
  1. `{$dia}-{$semana}`
  2. Fallback a `{$dia}-1`
  3. Fallback a categoría base `{$dia}`
  4. Fallback a `semana-{$semana}`

---

## 4. Motor Interactivo Frontend (Snippet 660 - 0 Recarga)
El script de frontend garantiza la experiencia de usuario tipo app móvil sin refrescar la página:

### 4.1. Guardia de Seguridad
- Se ejecuta **única y exclusivamente** si la página tiene la clase `.page-id-564` o la ruta contiene `/menu-semanal/`.

### 4.2. Activación Automática por Día y Regla de Domingo
- Detecta el día actual con `new Date().getDay()`.
- **Regla de Domingo:** Si hoy es domingo (`getDay() === 0`), activa automáticamente **LUNES** por defecto para captar pedidos anticipados.
- Si hoy es cualquier otro día, activa el día correspondiente (ej. Martes activa `martes`).

### 4.3. Píldoras de Días y Grillas Sincronizadas
- Cada píldora activa la grilla correspondiente ocultando las demás mediante `.hide()` y `.fadeIn(180)`.
- Actualiza en caliente el título del banner (`MENÚ DEL ...`), el badge del día y el contador de platos disponibles.
- Mapeo de selectores soportados:
  - Lunes: `lg_lun` / `[data-interaction-id="12dc898b"]` (píldora `675a0b2b`).
  - Martes: `lg_mar` / `[data-interaction-id="4bf72f7d"]` (píldora `407669ce`).
  - Miércoles: `lg_mie` / `[data-interaction-id="5bfd1736"]` (píldora `2c494cb1`).
  - Jueves: `lg_jue` / `[data-interaction-id="2fd6c6a9"]` (píldora `60e274d`).
  - Viernes: `lg_vie` / `[data-interaction-id="62f9bc94"]` (píldora `4fdd1a46`).
  - Sábado: `lg_sab` / `[data-interaction-id="74741324"]` (píldora `da15a65`).

### 4.4. Solución Anti-Lazyload y Renderizado de Imágenes por CSS Nativo
- La plantilla Loop 631 renderiza la imagen como `background-image` en el contenedor `.elementor-element-c02covr` (o `[data-id="c02covr"]`).
- **PROHIBIDO TERMINANTEMENTE:** Manipular o inyectar imágenes mediante scripts de JavaScript (`knownImages`, `renderPlatosDia` o `$cards.eq(idx)`), ya que desincronizan las fotos reales de los productos respecto a WooCommerce.
- **Estándar Oficial:** Las imágenes son gobernadas de forma nativa por reglas CSS por post ID (`.page-id-564 .post-{ID} [data-id="c02covr"]`) configuradas en el bloque `<style>` del Snippet 660 y `custom_css` de la página 564.

### 4.5. Integración con WPC Quick View
- Delegación de eventos en `.woosq-btn` para abrir el modal nativo mediante `woosq_open(productId)` extrayendo el ID con Regex `post-(\d+)`.

---

## 5. Protocolo de Recuperación Rápida
Si el menú semanal pierde interactividad o imágenes:
1. Verificar que el Snippet 660 en `elementor_snippet` esté activo, contenga las reglas CSS de producto en `<style>` y **NO** intente manipular imágenes por JS.
2. Verificar que el Snippet 5 en Code Snippets mantenga los hooks `elementor/query/query_menu_*`.
3. Purgar caché con `wp_cache_clear`.
