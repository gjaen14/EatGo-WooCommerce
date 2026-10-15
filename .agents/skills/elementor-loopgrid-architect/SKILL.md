---
name: elementor-loopgrid-architect
description: Directrices maestras de diseño y arquitectura técnica para Loop Grids y plantillas de tarjetas de productos en Elementor (Eat&Go). Protege la funcionalidad de WooCommerce, WPC Quick View y soluciona definitivamente el problema de imágenes de tarjetas en gris por lazy loading.
---

# Elementor Loop Grid & Product Cards Architecture - Eat&Go

Este documento es de cumplimiento **OBLIGATORIO** cada vez que se realice mantenimiento, diseño, estilización o modificación en cualquier Loop Grid o plantilla de tarjeta (`loop-item`) de Elementor en Eat&Go.

---

## 1. PRINCIPIO FUNDAMENTAL: SEPARACIÓN DE DISEÑO Y FUNCIONALIDAD

Está **TERMINANTEMENTE PROHIBIDO** alterar, eliminar o renombrar los elementos y atributos funcionales de las tarjetas al realizar ajustes estéticos:

1. **Clases del Botón de Compra / Modal por Tipo de Tarjeta:**
   - **Plantilla Menú Semanal (Loop Item 631):** Utiliza la clase `woosq-btn` para abrir el modal WPC Quick View / Personalización del plato. Enlace `#` y sin popups de Elementor vinculados.
   - **Plantilla Carrusel con Video (Loop Item 781 - Home):** Utiliza compra instantánea DIRECTA mediante WooCommerce AJAX nativo con las clases estándar `ajax_add_to_cart add_to_cart_button product_type_simple`. NUNCA asignar `woosq-btn` a esta plantilla para no saturar con popups redundantes.
   - **Resolución Dinámica de Producto (Bulletproof Resolver en Snippet 110):**
     * PROHIBIDO vincular selectores genéricos de Elementor como `.elementor-element-9d0e1f8` al manejador de clics de `woosq_open()`.
     * Si un botón tiene clase `ajax_add_to_cart`, WPC Quick View NO debe interceptar el clic, de lo contrario activará el backdrop oscurecido (`.mfp-bg`) sin abrir el modal o rompiendo la compra instantánea.
2. **Scripts y Eventos de WooCommerce:**
   - No envolver el botón de agregar en contenedores con `pointer-events: none` ni interceptar sus eventos de clic con handlers JS que cancelen el bubbling sin disparar la acción nativa de WooCommerce.
3. **Botón Secundario (WhatsApp):**
   - Enlace `https://wa.me/50762345678` con target externo, respetando el texto y padding.

---

## 2. EL PROBLEMA DE LA TARJETA EN GRIS (ROOT CAUSE)

En Elementor, las imágenes de fondo dinámicas en contenedores Loop Item suelen aparecer con un fondo gris plano o transparentes debido a dos causas críticas:

### Causa A: El Lazy Loading de Elementor
Elementor inyecta en el `<head>` del sitio:
```css
.e-con.e-parent:nth-of-type(n+4):not(.e-lazyloaded):not(.e-no-lazyload),
.e-con.e-parent:nth-of-type(n+4):not(.e-lazyloaded):not(.e-no-lazyload) * {
    background-image: none !important;
}
```
Si el contenedor de la tarjeta no recibe la clase `.e-lazyloaded` o `.e-no-lazyload`, Elementor borra el `background-image` en tiempo de renderizado con `none !important`.

### Causa B: Entidades HTML en el Bloque `<style>`
Cuando el editor de Elementor o WordPress procesa el `custom_css`, las comillas dobles `url("...")` a menudo se escapan como `url(&quot;...&quot;)`.
> **Regla de Oro:** En CSS dentro de `<style>`, los navegadores NO decodifican entidades HTML. Por lo tanto, `url(&quot;...&quot;)` se considera una URL corrupta. **Las URLs en CSS deben ser SIEMPRE limpias y sin comillas:** `url(https://eatgopty.com/...)`.

---

## 3. SOLUCIÓN DEFINITIVA ANTI-FONDO GRIS (OVERRIDE CSS)

Para garantizar que la imagen de fondo siempre cargue al 100% de calidad y en tamaño `cover`, se debe aplicar la siguiente regla con alta especificidad:

```css
/* Anular Lazy Loading y garantizar renderizado de imagen en Loop Item */
html body .e-con.e-parent:not(.e-lazyloaded) div.elementor-element.elementor-element-<ID_CONTENEDOR>,
html body div.elementor-element.elementor-element-<ID_CONTENEDOR> {
  background-size: cover !important;
  background-position: center center !important;
  background-repeat: no-repeat !important;
  background-image: inherit; /* o url directa sin comillas */
}
```

---

## 4. GUÍA DE ESTILOS POR PLANTILLA

### A. Plantilla Loop Destacados (Post 190 - Home Page)
- **Concepto:** Tarjeta inmersiva de fondo completo (Full Card Background).
- **Capa 0 (Fondo):** Imagen del producto cubriendo el 100% del contenedor raíz (`1e4962ce`).
- **Capa 1 (Overlay):** Gradiente vertical inmersivo para legibilidad:
  `linear-gradient(180deg, rgba(0,0,0,0.1) 0%, rgba(0,0,0,0.5) 45%, rgba(0,0,0,0.95) 75%)`
- **Capa 2 (Contenido):**
  - Título en blanco puro `#FFFFFF`, font-weight 800, text-shadow sutil.
  - Fila inferior con `"Incluye guarnición criolla"` (`#E4E4E7`, 13px) a la izquierda y botón naranja `+ Agregar` a la derecha.

### B. Plantilla Menú Semanal (Post 631)
- **Concepto:** Tarjeta moderna dividida en Header fotográfico y Body blanco limpio.
- **Header (`c02covr`):**
  - Altura fija de 220px, esquinas superiores redondeadas (24px).
  - **SIN DIFUMINADO:** La foto de la comida debe ser 100% nítida, iluminada y clara (`background: none !important; opacity: 1 !important;`).
  - Badge `"PLATO ESTRELLA"`: Fondo `#18181B`, texto amarillo `#FACC15`, border-radius `50px`.
  - Badge Precio: Píldora blanca `#FFFFFF`, texto oscuro `#18181B` negrita 800, sombra suave.
  - Badge `"📦 Ver en Caja 75°C"`: Fondo `#18181B` con 85% opacidad, texto blanco.
- **Body (`c08body`):**
  - Fondo blanco `#FFFFFF`, padding uniforme (18px).
  - Título oscuro `#18181B` (17px, font-weight 800).
  - Selector de Acompañamiento: Caja blanca con borde `#E5E7EB`, esquinas redondeadas 12px, texto `"Arroz Blanco Criollo"` y chevron `⌵`.
  - Botón Principal `+ Agregar al Pedido`:
    - Fondo naranja `#F59E0B` o `#FF5500`.
    - **Icono obligatorio:** SVG `bag` (Media ID 638) integrado limpiamente antes del texto.
    - Clases: `woosq-btn` y atributos `data-id`.
  - Botón Secundario `Planificar para este día por WhatsApp`:
    - Fondo gris claro `#F4F4F5`, borde `#E5E7EB`, texto `#18181B`.

### C. Plantilla Carrusel con Video (Post 781 - Home Page)
- **Concepto:** Tarjeta inmersiva con micro-video y compra instantánea directa.
- **Botón Play NATIVO (`eg_play_icon`):**
  - Widget nativo `icon` (stacked, circle, size 14px + padding 10px = 34px total).
  - Fondo circular oscuro semitransparente (`rgba(24, 24, 27, 0.7)`), icono blanco (`#FFFFFF`).
  - Posicionamiento absoluto nativo en la esquina superior de la foto.
  - Lógica condicional: Oculto si el plato no tiene `_eatgo_video_url`. Al hacer clic abre el modal vertical de video.
- **Botón de Compra Directo (`9d0e1f8`):**
  - Texto: `"+ Agregar al Pedido"`.
  - Clases obligatorias: `ajax_add_to_cart add_to_cart_button product_type_simple`.
  - Enlace: `?add-to-cart=[id]`.
  - NUNCA incluir `woosq-btn` para permitir la compra AJAX nativa instantánea sin modales redundantes.
- **Modal Vertical de Video (`c01vmod`):**
  - Estilo App vertical (ancho máx 440px, esquinas redondeadas 24px, fondo oscuro `#18181B`).
  - Video superior 16:9, Título (20px bold blanco), Precio (18px bold) y Botón amarillo destacado (`#ffcf00`, texto `#18181B`, border-radius 14px).
  - Cero textos distractores o garantías redundantes: solo los 4 elementos esenciales.

---

## 5. CHECKLIST DE VERIFICACIÓN ANTES DE DAR POR TERMINADA UNA TAREA
- [ ] ¿El botón de compra de Loop Item 631 conserva `woosq-btn` y abre Quick View?
- [ ] ¿El botón de compra de Loop Item 781 conserva `ajax_add_to_cart` y añade directamente al carrito?
- [ ] ¿El botón de Play en Loop Item 781 se oculta si el plato no tiene video asignado?
- [ ] ¿El modal de video vertical muestra exclusivamente: Video, Título, Precio y Botón Amarillo?
- [ ] ¿Las URLs de imágenes en `custom_css` carecen de comillas dobles (sin `&quot;`)?
- [ ] ¿Se verificó visualmente y se purgaron las cachés de Elementor y WordPress tras el guardado?
