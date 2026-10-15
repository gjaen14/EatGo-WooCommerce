import urllib.request, json, base64

username = 'JaenDev'
password = '4n3FKy26SkBpwe8GPBzdbqEz'
auth = 'Basic ' + base64.b64encode(f'{username}:{password}'.encode()).decode()

req = urllib.request.Request(
    'https://eatgopty.com/wp-json/wp/v2/pages/58?context=edit',
    headers={'Authorization': auth}
)
with urllib.request.urlopen(req) as resp:
    page = json.load(resp)

with open('all_product_bg_rules.css') as f:
    bg_rules = f.read()

final_css = f"""/* ========================================================
   Eat&Go Home Loop Cards - 100% Identical to Target Captura 1
   ======================================================== */

/* Root Card Container */
html body .elementor-190 div.elementor-element.elementor-element-1e4962ce,
html body div.elementor-element.elementor-element-1e4962ce {{
  background-size: cover !important;
  background-position: center center !important;
  background-repeat: no-repeat !important;
  position: relative !important;
  overflow: hidden !important;
  border-radius: 28px !important;
}}

/* Gradient Overlay: food image brightly visible, dark at bottom */
html body .elementor-190 div.elementor-element.elementor-element-1e4962ce::before,
html body div.elementor-element.elementor-element-1e4962ce::before {{
  content: '' !important;
  position: absolute !important;
  top: 0 !important;
  left: 0 !important;
  right: 0 !important;
  bottom: 0 !important;
  opacity: 1 !important;
  background: linear-gradient(180deg, rgba(0,0,0,0.05) 0%, rgba(0,0,0,0.25) 40%, rgba(0,0,0,0.92) 80%) !important;
  z-index: 1 !important;
  pointer-events: none !important;
}}

html body .elementor-190 div.elementor-element.elementor-element-1e4962ce > *,
html body div.elementor-element.elementor-element-1e4962ce > * {{
  position: relative !important;
  z-index: 2 !important;
}}

/* Product Specific Backgrounds */
{bg_rules}

/* Badge Top Left - MÁS VENDIDO OFICINAS */
.elementor-element-3d4e5f2 {{
  background-color: rgba(24, 24, 27, 0.85) !important;
  border: 1px solid rgba(234, 179, 8, 0.5) !important;
  border-radius: 50px !important;
  padding: 6px 16px !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
}}

.elementor-element-3d4e5f2 p,
.elementor-element-3d4e5f2 span,
.elementor-element-3d4e5f2 .eg-badge-tag {{
  color: #FACC15 !important;
  font-family: 'Open Sans', sans-serif !important;
  font-size: 11px !important;
  font-weight: 800 !important;
  letter-spacing: 0.5px !important;
  text-transform: uppercase !important;
  margin: 0 !important;
  padding: 0 !important;
}}

/* Price Top Right - Pill #FF5500 */
.elementor-element-4e5f6a3,
.elementor-190 .elementor-element-4e5f6a3 {{
  background-color: #FF5500 !important;
  border-radius: 50px !important;
  padding: 6px 16px !important;
  min-width: 68px !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  box-shadow: 0 2px 8px rgba(255, 85, 0, 0.3) !important;
  white-space: nowrap !important;
}}

.elementor-element-4e5f6a3 .elementor-heading-title {{
  color: #FFFFFF !important;
  font-family: 'Open Sans', sans-serif !important;
  font-size: 14px !important;
  font-weight: 800 !important;
  margin: 0 !important;
  white-space: nowrap !important;
}}

/* Dish Title & Description */
.elementor-element-6a7b8c5 .elementor-heading-title {{
  color: #FFFFFF !important;
  font-family: 'Open Sans', sans-serif !important;
  font-size: 26px !important;
  font-weight: 800 !important;
  line-height: 1.15 !important;
  text-shadow: 0 2px 4px rgba(0,0,0,0.6) !important;
}}

.elementor-element-7b8c9d6 {{
  color: #D4D4D8 !important;
  font-family: 'Open Sans', sans-serif !important;
  font-size: 13px !important;
  line-height: 1.45 !important;
  text-shadow: 0 1px 3px rgba(0,0,0,0.7) !important;
}}

/* Bottom Action Row - Horizontal flex (Garnish Left, Button Right) */
.elementor-element-8c9d0e7 {{
  display: flex !important;
  flex-direction: row !important;
  justify-content: space-between !important;
  align-items: center !important;
  width: 100% !important;
  margin-top: 14px !important;
  padding-top: 14px !important;
  border-top: 1px solid rgba(255, 255, 255, 0.12) !important;
}}

.elementor-element-8c9d0e7::before {{
  content: 'Incluye guarnición criolla' !important;
  font-family: 'Open Sans', sans-serif !important;
  font-size: 13px !important;
  font-weight: 500 !important;
  color: #A1A1AA !important;
  display: inline-block !important;
  margin-right: auto !important;
  line-height: 1.2 !important;
}}

.elementor-element-8c9d0e7 .elementor-element-9d0e1f8 {{
  margin-left: auto !important;
}}

/* Action Button - Orange Pill with Bag SVG */
.elementor-element-9d0e1f8 a.elementor-button,
.elementor-element-9d0e1f8 .elementor-button {{
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  background-color: #FF5500 !important;
  color: #FFFFFF !important;
  border-radius: 50px !important;
  padding: 8px 18px !important;
  box-shadow: 0 4px 14px rgba(255, 85, 0, 0.35) !important;
  transition: all 0.2s ease !important;
  border: none !important;
}}

.elementor-element-9d0e1f8 a.elementor-button:hover,
.elementor-element-9d0e1f8 .elementor-button:hover {{
  background-color: #E04B00 !important;
  transform: translateY(-2px) !important;
  box-shadow: 0 6px 18px rgba(255, 85, 0, 0.45) !important;
}}

.elementor-element-9d0e1f8 .elementor-button-icon {{
  display: none !important;
}}

.elementor-element-9d0e1f8 .elementor-button-text {{
  font-size: 0 !important;
  line-height: 0 !important;
  color: transparent !important;
  display: inline-flex !important;
  align-items: center !important;
}}

.elementor-element-9d0e1f8 .elementor-button-text::before {{
  content: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="%23FFFFFF" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M3.4 5.467a2 2 0 0 0-.4 1.2V20a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6.667a2 2 0 0 0-.4-1.2l-2-2.667A2 2 0 0 0 17 2H7a2 2 0 0 0-1.6.8z"/><path d="M3 6h18"/><path d="M16 10a4 4 0 0 1-8 0"/></svg>') !important;
  display: inline-block !important;
  margin-right: 8px !important;
  vertical-align: middle !important;
}}

.elementor-element-9d0e1f8 .elementor-button-text::after {{
  content: 'Agregar' !important;
  font-family: 'Open Sans', sans-serif !important;
  font-size: 14px !important;
  line-height: 1 !important;
  font-weight: 800 !important;
  color: #FFFFFF !important;
  display: inline-block !important;
}}
"""

page_settings = page['meta'].get('_elementor_page_settings', {})
page_settings['custom_css'] = final_css

payload = {
    'meta': {
        '_elementor_page_settings': page_settings
    }
}

req_update = urllib.request.Request(
    'https://eatgopty.com/wp-json/wp/v2/pages/58',
    headers={
        'Authorization': auth,
        'Content-Type': 'application/json'
    },
    data=json.dumps(payload).encode('utf-8')
)

with urllib.request.urlopen(req_update) as resp:
    print('Updated clean CSS to Page 58! Status:', resp.getcode())
