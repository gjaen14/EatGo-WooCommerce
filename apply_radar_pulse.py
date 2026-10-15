import urllib.request, json, base64

auth = base64.b64encode(b'JaenDev:4n3FKy26SkBpwe8GPBzdbqEz').decode('utf-8')

# 1. Update Snippet 854
req_snip = urllib.request.Request(
    'https://eatgopty.com/wp-json/wp/v2/elementor_snippet/854?context=edit',
    headers={'Authorization': f'Basic {auth}'}
)
with urllib.request.urlopen(req_snip) as resp:
    snip_data = json.loads(resp.read().decode('utf-8'))

css_code = snip_data.get('meta', {}).get('_elementor_code', '')

# Clean up any previous section 5 if present
if '/* 5. BOTON RADAR TITILANTE EAT&GO' in css_code:
    css_code = css_code[:css_code.find('/* 5. BOTON RADAR TITILANTE EAT&GO')]
    if '</style>' not in css_code:
        css_code += '</style>'

radar_css = """
/* ========================================================
   EAT&GO: RADAR PULSE PASTEL PARA BOTON CIRCULAR (BANNER ALMUERZO)
   Aislamiento exclusivo: solo data-interaction-id="1d852e0f"
   ======================================================== */
[data-interaction-id="1d852e0f"],
a[data-interaction-id="1d852e0f"],
.elementor-element-429a0b0f a[data-interaction-id="1d852e0f"] {
  background-color: #FFFFFF !important;
  color: #B91C1C !important;
  border-radius: 50% !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  text-decoration: none !important;
  box-sizing: border-box !important;
  animation: radar-pulse-pastel-pink 1.8s infinite cubic-bezier(0.25, 1, 0.5, 1) !important;
  transition: transform 0.2s ease, box-shadow 0.2s ease !important;
}

[data-interaction-id="1d852e0f"]:hover,
a[data-interaction-id="1d852e0f"]:hover {
  transform: scale(1.08) !important;
}

@keyframes radar-pulse-pastel-pink {
  0% {
    box-shadow: 0 0 0 0 rgba(252, 165, 165, 0.9); /* Rosado pastel suave #FCA5A5 */
  }
  50% {
    box-shadow: 0 0 0 8px rgba(252, 165, 165, 0.5), 0 0 16px 3px rgba(254, 202, 202, 0.35);
  }
  100% {
    box-shadow: 0 0 0 16px rgba(252, 165, 165, 0);
  }
}
</style>
"""

updated_css = css_code.replace('</style>', radar_css)

payload_snip = json.dumps({
    'meta': {
        '_elementor_code': updated_css
    }
}).encode('utf-8')

req_snip_up = urllib.request.Request(
    'https://eatgopty.com/wp-json/wp/v2/elementor_snippet/854',
    data=payload_snip,
    headers={
        'Authorization': f'Basic {auth}',
        'Content-Type': 'application/json'
    },
    method='POST'
)
with urllib.request.urlopen(req_snip_up) as resp:
    print('Snippet 854 updated successfully! Status:', resp.status)

# 2. Clear Elementor cache
del_req = urllib.request.Request(
    'https://eatgopty.com/wp-json/elementor/v1/cache',
    headers={'Authorization': f'Basic {auth}'},
    method='DELETE'
)
with urllib.request.urlopen(del_req) as resp:
    print('Elementor cache cleared!')
