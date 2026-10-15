import urllib.request, json, base64

auth = base64.b64encode(b'JaenDev:4n3FKy26SkBpwe8GPBzdbqEz').decode('utf-8')

# 1. Update Snippet 854 with the new utility classes
req_snip = urllib.request.Request(
    'https://eatgopty.com/wp-json/wp/v2/elementor_snippet/854?context=edit',
    headers={'Authorization': f'Basic {auth}'}
)
with urllib.request.urlopen(req_snip) as resp:
    snip_data = json.loads(resp.read().decode('utf-8'))

css_code = snip_data.get('meta', {}).get('_elementor_code', '')

# Append our utility classes if not already present
new_classes_css = """
/* 4. CLASE UTILITARIA PARA RESPLANDOR DE TARJETAS (BADGE-GLOW-RED) */
.badge-glow-red {
  animation: badge-glow-red 1.6s infinite ease-in-out !important;
}

/* 5. BOTON RADAR TITILANTE EAT&GO (PULSE & GLOW) */
.btn-pulse-red,
.badge-live-btn,
.elementor-element-1d852e0f a,
.elementor-element-1d852e0f button {
  animation: pulse-button-radar 1.6s infinite ease-in-out !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
}

@keyframes pulse-button-radar {
  0%, 100% {
    transform: scale(1);
    box-shadow: 0 0 0 0 rgba(200, 28, 32, 0.7);
  }
  50% {
    transform: scale(1.08);
    box-shadow: 0 0 14px 4px rgba(220, 38, 38, 0.6), 0 0 0 8px rgba(220, 38, 38, 0);
  }
}
"""

if '.btn-pulse-red' not in css_code:
    # insert before closing </style>
    if '</style>' in css_code:
        updated_css = css_code.replace('</style>', new_classes_css + '\n</style>')
    else:
        updated_css = css_code + new_classes_css

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
else:
    print('Snippet 854 already contains .btn-pulse-red')

# 2. Update Page 58 Elementor Data
req_page = urllib.request.Request(
    'https://eatgopty.com/wp-json/wp/v2/pages/58?context=edit',
    headers={'Authorization': f'Basic {auth}'}
)
with urllib.request.urlopen(req_page) as resp:
    page_data = json.loads(resp.read().decode('utf-8'))
    el_data = json.loads(page_data['meta']['_elementor_data'])

# Locate Index 1 (Banner: 429a0b0f -> 5b4c19)
banner_container = el_data[1]['elements'][0]
print('Found banner container:', banner_container.get('id'))

# Add badge-glow-red to classes
cur_classes = banner_container.get('settings', {}).get('classes', {}).get('value', [])
if 'badge-glow-red' not in cur_classes:
    cur_classes.append('badge-glow-red')
banner_container['settings']['classes']['value'] = cur_classes

# Locate button (Child 1: 1d852e0f)
btn_node = banner_container['elements'][1]
print('Found button:', btn_node.get('id'), btn_node.get('widgetType'))
btn_classes = btn_node.get('settings', {}).get('classes', {}).get('value', [])
if 'btn-pulse-red' not in btn_classes:
    btn_classes.append('btn-pulse-red')
btn_node['settings']['classes']['value'] = btn_classes

# Save Page 58
payload_page = json.dumps({
    'meta': {
        '_elementor_data': json.dumps(el_data),
        '_elementor_edit_mode': 'builder'
    }
}).encode('utf-8')

req_page_up = urllib.request.Request(
    'https://eatgopty.com/wp-json/wp/v2/pages/58',
    data=payload_page,
    headers={
        'Authorization': f'Basic {auth}',
        'Content-Type': 'application/json'
    },
    method='POST'
)
with urllib.request.urlopen(req_page_up) as resp:
    print('Page 58 updated successfully! Status:', resp.status)

# 3. Clear Elementor cache
del_req = urllib.request.Request(
    'https://eatgopty.com/wp-json/elementor/v1/cache',
    headers={'Authorization': f'Basic {auth}'},
    method='DELETE'
)
with urllib.request.urlopen(del_req) as resp:
    print('Elementor cache cleared!')
