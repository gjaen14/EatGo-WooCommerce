# Directrices del Proyecto Eat&Go

> ⚠️ **MANDATORIO PARA CUALQUIER AGENTE (LEER ANTES DE TRABAJAR):**
> Antes de realizar cualquier acción, análisis o modificación en este repositorio, el agente **DEBE leer obligatoriamente todos los archivos de reglas en `.agents/rules/`** y respetar estrictamente los límites de aislamiento por funcionalidad. Prohibido ejecutar cambios sin consultar la regla correspondiente a la página o motor involucrado.

---

## 1. Conexión Exclusiva vía MCP con WordPress y Elementor
1. **Conexión 100% por MCP**: Toda la conexión, lectura, creación, edición y administración de WordPress y Elementor se realiza **directa y exclusivamente mediante las herramientas MCP** (`elementor-my-blog` y `wordpress-mcp`).
2. **WordPress está en la nube (GoDaddy)**: El sitio está alojado en `https://eatgopty.com/`. NO existe WordPress local (no hay archivos PHP, carpetas `wp-content`, ni base de datos local).
3. **El entorno local es solo React**: Todo el código en esta máquina pertenece únicamente al frontend React (Vite + TypeScript).
4. **Prohibido buscar archivos de WordPress en el equipo**: Jamás usar `find`, `grep` u otros comandos locales para buscar archivos del core de WordPress o plugins; toda interacción remota se canaliza a través de las herramientas MCP.

---

## 2. Reglas Específicas por Funcionalidad

### A. Menú Semanal (`/menu-semanal/` - Post ID 564)
- **Regla Oficial:** [.agents/rules/menu_semanal_rules.md](file://.agents/rules/menu_semanal_rules.md) (Lectura obligatoria).
- **Skill Especializada:** [.agents/skills/elementor-weekly-menu-engine/SKILL.md](file://.agents/skills/elementor-weekly-menu-engine/SKILL.md).
- **Backend:** Snippet ID 5 (`query_menu_lunes` ... `query_menu_sabado`) en `America/Panama`.
- **Frontend Interactivo:** Elementor Custom Code Snippet ID 660 (cambio de día instantáneo con 0-recarga, regla de domingo, cero manipulación JS de imágenes).
- **Aislamiento:** Prohibido tocar Post 58 (Home), Post 724 (Menú del Día) o forzar `posts_per_page` en PHP.

### B. Menú del Día (`/menu-del-dia/` - Post ID 724)
- **Regla Oficial:** [.agents/rules/menu_del_dia_rules.md](file://.agents/rules/menu_del_dia_rules.md) (Lectura obligatoria).
- **Aislamiento:** Prohibido tocar Post 58 (Home), Post 564 (Menú Semanal) o Template Loop 631.
- **Backend:** Query Hook `menu_del_dia_auto` (Snippet ID 5 en WordPress, respaldo en `snippet_5_engine.php`).
- **Parámetros & Resolución:** Zona `America/Panama`, regla de domingo, soporta `?dia=` y `?semana=`.
- **Respaldo:** `pagina_menu_del_dia.json`.
