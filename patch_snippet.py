import urllib.request
import json
import base64

with open('snippet_477_before_refinement.txt', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. CSS fix
old_css = """.elementor-menu-cart__toggle {
  display: none !important;
}"""

new_css = """.elementor-menu-cart__toggle,
#elementor-menu-cart__toggle_button,
.elementor-menu-cart__toggle_button {
  display: none !important;
}"""

if old_css in code:
    code = code.replace(old_css, new_css, 1)
    print('CSS rule replaced successfully')
else:
    print('Warning: old_css not found')

# 2. Add renderEatGoFabCart() at start of renderComandaDigital
target_func = "function renderComandaDigital() {"
idx = code.find(target_func)
if idx != -1:
    # insert renderEatGoFabCart(); right after function renderComandaDigital() {\n
    insert_pos = idx + len(target_func)
    code = code[:insert_pos] + "\n    renderEatGoFabCart();" + code[insert_pos:]
    print("Inserted renderEatGoFabCart() at start of renderComandaDigital")
else:
    print("Warning: renderComandaDigital not found")

# 3. Add renderEatGoFabCart() in document.ready and immediately
target_ready = "$(document).ready(function() {"
idx2 = code.find(target_ready)
if idx2 != -1:
    insert_pos2 = idx2 + len(target_ready)
    code = code[:insert_pos2] + "\n    renderEatGoFabCart();" + code[insert_pos2:]
    print("Inserted renderEatGoFabCart() in $(document).ready")
else:
    print("Warning: $(document).ready not found")

# Also call it immediately before closing IIFE
target_iife = "})(jQuery);"
idx3 = code.find(target_iife)
if idx3 != -1:
    code = code[:idx3] + "  // Invocacion inmediata de FAB Cart\n  renderEatGoFabCart();\n\n" + code[idx3:]
    print("Inserted immediate renderEatGoFabCart() invocation before IIFE close")
else:
    print("Warning: IIFE close not found")

with open('snippet_477_fixed.txt', 'w', encoding='utf-8') as f:
    f.write(code)

print("Snippet fixed length:", len(code))

# Deploy to WordPress via REST API
username = 'JaenDev'
password = '4n3FKy26SkBpwe8GPBzdbqEz'
auth = 'Basic ' + base64.b64encode(f'{username}:{password}'.encode()).decode()

payload = {
    'title': 'EatGo Comanda Digital WhatsApp Drawer & FAB Cart',
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

try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        print('Updated snippet HTTP:', resp.getcode())
        data = json.load(resp)
        print('Snippet ID:', data.get('id'), 'Status:', data.get('status'))
except Exception as e:
    print('Deploy error:', e)
