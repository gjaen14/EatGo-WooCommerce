import urllib.request
import json
import base64

username = 'JaenDev'
password = '4n3FKy26SkBpwe8GPBzdbqEz'
auth = 'Basic ' + base64.b64encode(f'{username}:{password}'.encode()).decode()

script_content = """<style>
/* ========================================================
   EAT&GO: DISEÑO VISUAL OFICIAL (100% PRESERVADO)
   Loop Grid Nativo + Template 631
   ======================================================== */

/* Píldoras de los Días */
.elementor-element-38d9444c p,
.btn-dia-tab,
[class*="dia-tab"] {
  cursor: pointer !important;
  transition: all 0.2s ease !important;
  border-radius: 50px !important;
  user-select: none !important;
}

/* Anti-lazyload para imágenes de Template 631 */
.elementor-element-c02covr,
[data-id="c02covr"],
.e-loop-item [data-id="c02covr"],
.elementor-element-c01root [data-id="c02covr"] {
  background-size: cover !important;
  background-position: center center !important;
  background-repeat: no-repeat !important;
  opacity: 1 !important;
  min-height: 220px !important;
  border-radius: 24px 24px 0 0 !important;
}

/* Ocultar badge de caja 75°C y botón secundario WhatsApp */
.elementor-element-c06bgbtm,
[data-id="c06bgbtm"],
.elementor-element-w15btnw,
[data-id="w15btnw"],
div[data-interaction-id="7a466aab"],
div[data-interaction-id="217a4710"],
div[data-interaction-id="25a756bf"] {
  display: none !important;
}

/* Banner superior */
[data-id="60277592"] {
  background-color: #FEFCE8 !important;
  border: 1px solid #FEF08A !important;
  border-radius: 16px !important;
  padding: 16px 24px !important;
}
[data-interaction-id="3b175772"] {
  background-color: #FEF3C7 !important;
  color: #92400E !important;
  font-size: 12px !important;
  font-weight: 700 !important;
  padding: 4px 10px !important;
  border-radius: 8px !important;
  display: inline-block !important;
  margin: 0 !important;
}
[data-interaction-id="5e2b25c1"] {
  background: transparent !important;
  color: #71717A !important;
  font-size: 14px !important;
  font-weight: 400 !important;
  text-transform: none !important;
  margin: 0 !important;
  border-radius: 0 !important;
  padding: 0 !important;
}

/* Botón Agregar al Pedido */
.page-id-564 .elementor-element-w14btna .elementor-button,
.page-id-564 .elementor-element-w14btna a,
.page-id-564 .elementor-element-c01root .woosq-btn,
.elementor-631 .woosq-btn {
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  width: 100% !important;
  height: 48px !important;
  background-color: #F59E0B !important;
  color: #000000 !important;
  font-family: 'Open Sans', sans-serif !important;
  font-size: 14px !important;
  font-weight: 800 !important;
  text-decoration: none !important;
  border-radius: 50px !important;
  border: none !important;
  cursor: pointer !important;
  transition: all 0.2s ease !important;
  box-shadow: 0 4px 12px rgba(245, 158, 11, 0.28) !important;
  gap: 8px !important;
  box-sizing: border-box !important;
}

.page-id-564 .elementor-element-w14btna .elementor-button:hover,
.page-id-564 .elementor-element-w14btna a:hover,
.page-id-564 .elementor-element-c01root .woosq-btn:hover,
.elementor-631 .woosq-btn:hover {
  background-color: #D97706 !important;
  color: #000000 !important;
  transform: translateY(-1px) !important;
  box-shadow: 0 6px 16px rgba(245, 158, 11, 0.38) !important;
}

/* Icono bag.svg en el botón */
.page-id-564 .elementor-element-w14btna img,
.page-id-564 .elementor-element-c01root .woosq-btn img,
.page-id-564 .elementor-element-c01root .woosq-btn svg,
.elementor-631 .woosq-btn img,
.elementor-631 .woosq-btn svg {
  width: 20px !important;
  height: 20px !important;
  stroke: #000000 !important;
  fill: none !important;
  display: inline-block !important;
  vertical-align: middle !important;
}

/* Asegurar que las tarjetas de Template 631 tengan esquinas redondeadas y sombra */
.elementor-element-c01root,
[data-id="c01root"],
.e-loop-item {
  border-radius: 24px !important;
  overflow: hidden !important;
  background: #FFFFFF !important;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.06) !important;
  border: 1px solid #F4F4F5 !important;
}

.eg-garnish-label {
  font-family: 'Open Sans', -apple-system, BlinkMacSystemFont, sans-serif !important;
  font-size: 13px !important;
  font-weight: 500 !important;
  color: #D4D4D8 !important;
  line-height: 1.2 !important;
  display: inline-block !important;
  white-space: nowrap !important;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.8) !important;
}

.elementor-element-8c9d0e7 {
  border-top: 1px solid rgba(255, 255, 255, 0.15) !important;
  padding-top: 14px !important;
  margin-top: 14px !important;
}

</style>

<script>
jQuery(function($) {

  
