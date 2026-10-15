---
name: elementor-native-governance
description: Regla estricta de arquitectura que prioriza el uso de controles nativos de Elementor para diseño visual y limita los snippets de código EXCLUSIVAMENTE a lógica de negocio y hooks de comportamiento. Prohíbe el secuestro de estilos mediante CSS externo.
---

# 🏛️ Elementor Native-First & Design Governance Policy

Este skill establece la jerarquía estricta entre la interfaz visual de Elementor y el código personalizado (Snippets PHP/JS/CSS).

## 1. LA REGLA DE ORO: SEPARACIÓN DE RESPONSABILIDADES
- **DISEÑO VISUAL (100% Nativo en Elementor):** Todo lo que sea colores, tamaños de fuente, tipografías, paddings, márgenes, sombras y border-radius DEBE configurarse exclusivamente a través de los paneles de control de Elementor. 
- **LÓGICA Y COMPORTAMIENTO (Snippets):** Los snippets de PHP, JavaScript o archivos mu-plugins se limitan ÚNICAMENTE a cálculos de servidor, consultas (Queries de WooCommerce), llamadas AJAX, y eventos de clic.

## 2. PROHIBICIÓN DE SECUESTRO VISUAL (ANTI-OVERRIDE)
- **Clases de Acción vs. Clases de Estilo:**
  * Clases como `woosq-btn`, `btn-trigger-side-cart`, `btn-open-modal` son **Action Hooks (Disparadores de Comportamiento)**.
  * **ESTÁ ESTRICTAMENTE PROHIBIDO** declarar propiedades de diseño (`background`, `color`, `padding`, `border-radius`, `font-size`) asociadas a estas clases de comportamiento con `!important`.
  * *Razón:* Al meter estilos en una clase funcional, se inhabilita el editor visual de Elementor, impidiendo que el usuario pueda cambiar el diseño de sus botones desde la interfaz.
- Si una clase funcional necesita ser asignada a un botón de Elementor, el botón DEBE conservar el 100% de la personalización visual definida en el editor.

## 3. POLÍTICA DE "SNIPPET COMO ÚLTIMO RECURSO"
Antes de escribir cualquier línea de código o script en WordPress:
1. El agente debe verificar si la necesidad se resuelve mediante:
   - Controles nativos de Elementor Pro (Theme Builder, Display Conditions, Dynamic Tags).
   - Ajustes nativos de WooCommerce (Categorías, Atributos, Productos Variables).
   - Funcionalidades del plugin activo (ej. WPClever settings).
2. Solo se autoriza un snippet PHP o JS si la funcionalidad requerida es inexistente de forma nativa (ej. el cálculo rotativo de Semana 1 vs 2, o el soporte para forzar días por URL `?dia=martes`).

## 4. CHECKLIST OBLIGATORIO DE CUMPLIMIENTO
Antes de reportar una tarea como completada, el agente debe validar:
- [ ] ¿El usuario puede cambiar el color de este botón o el tamaño del texto desde el panel de Elementor sin que mi código lo bloquee? (Debe ser SÍ).
- [ ] ¿El snippet PHP solo filtra datos y no altera la cantidad de tarjetas ni el diseño? (Debe ser SÍ).
- [ ] ¿Las clases de plugins (ej. `woosq-btn`) conservan intacto el diseño asignado en Elementor? (Debe ser SÍ).