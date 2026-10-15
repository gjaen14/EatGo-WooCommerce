import urllib.request
import json
import base64

# Read snippet_477_fixed.txt
with open('snippet_477_fixed.txt', 'r', encoding='utf-8') as f:
    code = f.read()

# Target observer code to remove
observer_block = """  // Observador de mutaciones del DOM para re-renderizado reactivo
  var observer = new MutationObserver(function() {
    renderComandaDigital();
    renderEatGoFabCart();
  });

  var target = document.body;
  if (target) {
    observer.observe(target, { childList: true, subtree: true });
  }"""

if observer_block in code:
    code = code.replace(observer_block, "  // MutationObserver removido para evitar bucle infinito y congelamiento del navegador")
    print("SUCCESS: MutationObserver block found and removed!")
else:
    print("WARNING: Exact observer block not found, searching with regex or substrings...")
    # fallback substring replacement
    import re
    code = re.sub(
        r'// Observador de mutaciones del DOM.*?'
        r'observer\.observe\(target,\s*\{\s*childList:\s*true,\s*subtree:\s*true\s*\}\);\s*\}',
        '// MutationObserver removido para evitar bucle infinito',
        code,
        flags=re.DOTALL
    )

# Save cleaned code
with open('snippet_477_clean.txt', 'w', encoding='utf-8') as f:
    f.write(code)

print("Cleaned code size:", len(code))

# Deploy to WordPress REST API
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
        print('Updated snippet 477 HTTP:', resp.getcode())
        data = json.load(resp)
        print('Snippet ID:', data.get('id'), 'Status:', data.get('status'))
except Exception as e:
    print('Deploy error:', e)
