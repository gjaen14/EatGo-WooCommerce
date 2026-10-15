---
name: elementor-migration
description: Migra páginas TSX del proyecto Eat&Go React a plantillas JSON de Elementor para WordPress. Usa esta skill cuando el usuario pida migrar, convertir o actualizar cualquier página (.tsx) al formato Elementor, crear plantillas JSON de Elementor, o actualizar páginas en WordPress.
---

# 🚀 Skill: Migración TSX → Elementor (Eat&Go)

## Contexto del Proyecto
**Eat&Go** es un food truck digital. El objetivo es migrar cada página o componente de React TSX a una plantilla Elementor JSON importable en WordPress.

- **Origen:** App React (Vite + TSX) en `src/pages/` y `src/components/`.
- **Destino:** WordPress + Elementor Flexbox Containers (`https://eatgopty.com/`).

---

## Proceso de Migración (Paso a Paso)

1. **LEER el TSX fuente y `src/data.ts`** para identificar secciones visuales y datos dinámicos.
2. **MAPEAR componentes React a Flexbox Containers de Elementor:**
   - Todo layout horizontal (`flex-row`) → Container con `"flex_direction": "row"`.
   - Todo layout vertical (`flex-col`) → Container con `"flex_direction": "column"`.
   - Espaciados (`gap-4`) → `"flex_gap": { "size": 16, "unit": "px" }`.
   - Alineación → `"flex_align_items": "center"` y `"flex_justify_content": "space-between"`.
3. **Cargar la Plantilla Base:** Consultar `resources/template-base.json` para mantener la estructura estándar.
4. **Aplicar Design System Oficial de Marca (eat&go):**
   - **Primary (Rojo Marca):** `#C81C20` (CTAs, botones primarios).
   - **Secondary (Amarillo):** `#FFCF00` (Acentos y destacados).
   - **Tertiary (Oscuro):** `#18181B` (Fondos oscuros, textos principales).
   - **Neutral (Fondo claro):** `#F4F4F5` o `#FFFFFF`.
   - **Bordes / Separadores:** `#E4E4E7`.
   - **Tipografía Oficial:** `"Open Sans", sans-serif` (Títulos 700 bold, Párrafos 400 regular). *(NO USAR "Outfit")*.
   - **Border Radius:** Cards (`20px`), Botones (`50px` pill o `10px`).
5. **Manejo de Imágenes:** Usar placeholders `[IMG_COMIDA_URL]`, `[IMG_LOGO_URL]`, etc.
6. **Hardcodear Datos Estáticos:** Transformar los `.map()` de React a elementos estáticos repetidos en el JSON.
7. **Generar el Archivo Final:** Guardar como `{pagina}_elementor.json` en la raíz del proyecto.

---

## ⚠️ Reglas Críticas de Generación JSON (BLOQUEO ANTI-ERRORES)

1. **PROHIBIDO USAR `section` O `column`:** 
   - Elementor moderno utiliza Flexbox Containers. Está terminantemente prohibido generar `"elType": "section"` o `"elType": "column"`.
   - Cada bloque contenedor DEBE ser `"elType": "container"`.
   - Para anchos, NO uses `_column_size`. Usa `"width": { "unit": "%", "size": 25 }` o permite que el Flexbox distribuya el espacio con `"flex_justify_content": "space-between"`.

2. **REGLA PARA WIDGETS `icon-box`:**
   - Si usas el widget `icon-box`, es OBLIGATORIO definir `"description_text": ""` (cadena vacía). Si omites este campo, Elementor inyectará automáticamente un párrafo con "Lorem Ipsum" que destruye el diseño.

3. **ANIDACIÓN LIMPIA (No crear "divception"):**
   - No anides contenedores innecesarios. Un contenedor padre en fila (`row`) puede contener directamente los 4 elementos de contacto uno al lado del otro usando `flex_gap`.

4. **INTEGRIDAD DE ARCHIVO:**
   - No subir HTML plano vía REST API; generar siempre el archivo `.json` listo para importar en WP Admin -> Plantillas -> Importar.

---

## Checklist de Trabajo

- [ ] Verificar que TODO contenedor tenga `"elType": "container"` (cero secciones/columnas).
- [ ] Verificar que la tipografía sea `"Open Sans"` y el color principal sea `#C81C20`.
- [ ] Si hay `icon-box`, confirmar que `"description_text": ""` esté presente.
- [ ] Validar que el JSON cierre todas sus llaves y corchetes correctamente.