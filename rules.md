---
name: project-master-rules
description: Reglas maestras permanentes y gobernanza obligatoria para el proyecto Eat&Go.
---

# 🏛️ REGLAS MAESTRAS DE ARQUITECTURA Y EJECUCIÓN (EAT&GO)

Este documento rige el 100% de las acciones del agente. Antes de procesar cualquier tarea, el agente DEBE cargar e incorporar en su memoria los siguientes 5 skills especializados:

## 1. LOS 5 SKILLS OBLIGATORIOS (CORE STACK)
1. `elementor-architect-skill`: Estructura estricta de Flexbox Containers 3.x+, cero secciones/columnas legadas, IDs de 7 caracteres.
2. `elementor-migration`: Traducción precisa de tokens de React a Elementor (Open Sans, paleta oficial, regla `icon-box`).
3. `elementor-loopgrid-architect`: Especialista en Loop Grids, plantillas `loop-item`, Query IDs y consultas dinámicas de WooCommerce.
4. `elementor-native-governance`: Prioridad absoluta a controles nativos de Elementor. Prohibición de secuestrar estilos con `!important` y snippets limitados estrictamente a lógica de negocio.
5. `elementor-weekly-menu-engine`: Motor de rotación semanal, aislamiento de query hooks (`query_menu_{dia}`), interfaz con 0-recarga de pestañas y renderizado nativo por CSS de imágenes en el Menú Semanal (Post 564).

## 2. POLÍTICA DE SEGURIDAD Y CERO REGRESIONES (INNEGOCIABLE)
- **Prohibido Sobrescribir Clases Existentes:** Las clases funcionales activas (`woosq-btn`, `eatgo-sticky-cart-bar`, `btn-trigger-side-cart`, etc.) están congeladas y en producción. Cualquier nuevo estilo debe ser estrictamente aditivo (nuevas clases con prefijo único).
- **Preservación de Flujos Aprobados:** Nunca modifiques el Header (677), el Side-Drawer de WhatsApp, el Loop de Desayunos o el Menú del Día a menos que se indique explícitamente en la orden.
- **Autonomía con Criterio:** Si una tarea pide estilizar un elemento, no toques el backend. Si pide lógica, no toques el CSS.

## 3. MAPA DE REGLAS POR FUNCIONALIDAD (LECTURA OBLIGATORIA)
- **Menú Semanal (`/menu-semanal/` - Post ID 564):**
  * Regla de Negocio & Aislamiento: [.agents/rules/menu_semanal_rules.md](file://.agents/rules/menu_semanal_rules.md)
  * Skill de Arquitectura Oficial: [.agents/skills/elementor-weekly-menu-engine/SKILL.md](file://.agents/skills/elementor-weekly-menu-engine/SKILL.md)
  * Motores: Snippet 5 (Query Hooks PHP), Snippet 660 (Píldoras 0-recarga, regla domingo) y renderizado nativo por CSS para fotos de platos.
- **Menú del Día (`/menu-del-dia/` - Post ID 724):**
  * Regla de Negocio & Aislamiento: [.agents/rules/menu_del_dia_rules.md](file://.agents/rules/menu_del_dia_rules.md)
  * Motor: Query Hook `menu_del_dia_auto` (Snippet ID 5 en WordPress).
- **Entorno Remoto WordPress (GoDaddy):**
  * Regla de Conexión: [.agents/rules/wordpress_remote.md](file://.agents/rules/wordpress_remote.md)
  * Interacción 100% mediante herramientas MCP (`elementor-my-blog` y `wordpress-mcp`). Cero WordPress local.