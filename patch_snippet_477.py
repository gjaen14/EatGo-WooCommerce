import urllib.request
import json
import base64

username = 'JaenDev'
password = '4n3FKy26SkBpwe8GPBzdbqEz'
auth = 'Basic ' + base64.b64encode(f'{username}:{password}'.encode()).decode()

with open('snippet_477_live.txt', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Add CSS suppression
suppression_css = """
/* ========================================================
   SUPRESIÓN ESTRICTA: VIEW CART RESIDUAL WOOCOMMERCE (HOME & GLOBAL)
   ======================================================== */
.page-id-58 .added_to_cart,
.page-id-58 a.wc-forward,
.added_to_cart,
a.wc-forward {
  display: none !important;
  visibility: hidden !important;
  opacity: 0 !important;
  pointer-events: none !important;
  height: 0 !important;
  width: 0 !important;
  margin: 0 !important;
  padding: 0 !important;
  line-height: 0 !important;
}
"""

if '<style>' in code:
    code = code.replace('<style>', '<style>' + suppression_css, 1)
    print("Added suppression CSS to <style>")
else:
    print("Warning: <style> not found")

# 2. Update syncCardQuickViewButtons
old_sync_find = "$card.find('.elementor-element-w14btna a, a.woosq-btn, a.elementor-button:has(.elementor-button-text:contains(\"Agregar\"))')"
new_sync_find = "$card.find('.elementor-element-w14btna a, .elementor-element-9d0e1f8 a, a.woosq-btn, a.elementor-button:has(.elementor-button-text:contains(\"Agregar\"))')"

if old_sync_find in code:
    code = code.replace(old_sync_find, new_sync_find)
    print("Updated syncCardQuickViewButtons with 9d0e1f8")
else:
    print("Warning: old_sync_find not found")

# 3. Update click handler
old_click = "$('.woosq-btn, .woosq-btn *, .elementor-element-w14btna a, .elementor-element-w14btna a *, a.elementor-button:has(.elementor-button-text:contains(\"Agregar\")), .elementor-button-text:contains(\"Agregar\")'"
new_click = "$('.woosq-btn, .woosq-btn *, .elementor-element-w14btna a, .elementor-element-w14btna a *, .elementor-element-9d0e1f8 a, .elementor-element-9d0e1f8 a *, a.elementor-button:has(.elementor-button-text:contains(\"Agregar\")), .elementor-button-text:contains(\"Agregar\")'"

if old_click in code:
    code = code.replace(old_click, new_click)
    print("Updated click delegation with 9d0e1f8")
else:
    print("Warning: old_click not found")

# Save updated snippet
with open('snippet_477_updated.txt', 'w', encoding='utf-8') as f:
    f.write(code)

payload = {
    'title': 'EatGo Comanda Digital WhatsApp Drawer',
    'status': 'publish',
    'meta': {
        '_elementor_code': code.strip(),
        '_elementor_location': 'elementor_body_end',
        '_elementor_priority': 1,
        '_elementor_conditions': ['include/general']
    }
}

req = urllib.request.Request(
    'https://eatgopty.com/wp-json/wp/v2/elementor_snippet/477',
    headers={
        'Authorization': auth,
        'Content-Type': 'application/json'
    },
    data=json.dumps(payload).encode('utf-8')
)

with urllib.request.urlopen(req, timeout=15) as resp:
    print('Updated snippet 477 HTTP:', resp.getcode())
