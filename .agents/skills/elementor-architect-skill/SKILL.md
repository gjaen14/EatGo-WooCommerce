---
name: elementor-architect-skill
description: Reglas estrictas y arquitectura de diseño para generar estructuras nativas de Elementor 3.x+ y Flexbox Containers mediante MCP o JSON.
---

# Elementor Senior Architecture & Forensic Design Skill

## 1. DIRECTRICES DE MOTOR (ENGINE RULES)
- **Cero Secciones Legadas:** PROHIBIDO generar `"elType": "section"` o `"elType": "column"`. Toda la maquetación debe realizarse usando **Flexbox Containers** (`"elType": "container"`).
- **Generación de IDs:** Cada contenedor y widget DEBE tener un ID único pseudo-aleatorio de exactamente 7 caracteres alfanuméricos en minúsculas (Ejemplo: `id: "3e4f1a2"`). Prohibido duplicar IDs.
- **Tipos de Elementos (elType):**
  - Contenedor (Padre o Hijo): `"elType": "container"`
  - Componente visual: `"elType": "widget"`, acompañado obligatoriamente de `"widgetType": "[nombre_del_widget]"` (ej. `"heading"`, `"image"`, `"text-editor"`, `"button"`, `"icon-box"`).

## 2. REGLAS DE SINTAXIS PARA SETTINGS (ESTRICTO)
- **Unidades y Espaciados:** Los paddings, margins y gaps NUNCA deben ser strings simples (`"20px"`). Deben usar el formato de objeto de Elementor:
```json
"padding": { "unit": "px", "top": "16", "right": "24", "bottom": "16", "left": "24", "isLinked": false },
"flex_gap": { "unit": "px", "size": 16 }
```
- **Limpieza de Widgets con Contenido por Defecto:** En widgets como `icon-box` o `image-box`, es OBLIGATORIO definir `"description_text": ""` para prevenir que Elementor inyecte párrafos de relleno ("Lorem Ipsum").
- **Responsividad:** Para elementos en fila (`row`), declara siempre el comportamiento móvil si se requiere apilar: `"flex_direction_mobile": "column"`.

## 3. ESQUEMA DE DATOS Y JERARQUÍA
Todo bloque inyectado debe respetar este estándar:
```json
{
  "id": "a1b2c3d",
  "elType": "container",
  "settings": {
    "content_width": "boxed",
    "boxed_width": { "unit": "px", "size": 1300 },
    "flex_direction": "row",
    "flex_justify_content": "space-between",
    "flex_align_items": "center",
    "flex_gap": { "unit": "px", "size": 16 }
  },
  "elements": [
    // Widgets directos o sub-contenedores
  ]
}
```

## 4. PROTOCOLO DE EJECUCIÓN MCP
- Si el MCP permite actualizar `post_meta`: inyecta la estructura en la clave `_elementor_data` serializada en JSON y marca `_elementor_edit_mode = "builder"`.
- Si el MCP es visual: crea los contenedores respetando el orden jerárquico (Padre -> Contenedor flex -> Widgets).