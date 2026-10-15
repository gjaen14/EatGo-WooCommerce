import json
import urllib.request
import base64

auth_str = "JaenDev:4n3FKy26SkBpwe8GPBzdbqEz"
auth_header = "Basic " + base64.b64encode(auth_str.encode()).decode()

# 1. Desplegar Página 751
with open('updated_page_751.json', 'r', encoding='utf-8') as f:
    page_content = json.load(f)

payload_page = {
    'template': 'elementor_header_footer',
    'meta': {
        '_elementor_edit_mode': 'builder',
        '_elementor_template_type': 'wp-page',
        '_elementor_data': json.dumps(page_content)
    }
}

req_page = urllib.request.Request(
    'https://eatgopty.com/wp-json/wp/v2/pages/751',
    headers={'Authorization': auth_header, 'Content-Type': 'application/json'},
    data=json.dumps(payload_page).encode('utf-8'),
    method='POST'
)
with urllib.request.urlopen(req_page, timeout=30) as resp:
    res_p = json.loads(resp.read().decode('utf-8'))
    print("1. Página 751 actualizada en WordPress con éxito! Status:", res_p.get('status'))

# 2. Desplegar Footer 932
with open('updated_footer_932.json', 'r', encoding='utf-8') as f:
    footer_content = json.load(f)

payload_footer = {
    'meta': {
        '_elementor_edit_mode': 'builder',
        '_elementor_template_type': 'footer',
        '_elementor_data': json.dumps(footer_content)
    }
}

req_footer = urllib.request.Request(
    'https://eatgopty.com/wp-json/wp/v2/elementor_library/932',
    headers={'Authorization': auth_header, 'Content-Type': 'application/json'},
    data=json.dumps(payload_footer).encode('utf-8'),
    method='POST'
)
with urllib.request.urlopen(req_footer, timeout=30) as resp:
    res_f = json.loads(resp.read().decode('utf-8'))
    print("2. Footer 932 actualizado en WordPress con éxito! Status:", res_f.get('status'))

# 3. Limpiar Elementor Cache
try:
    del_req = urllib.request.Request(
        'https://eatgopty.com/wp-json/elementor/v1/cache',
        headers={'Authorization': auth_header},
        method='DELETE'
    )
    with urllib.request.urlopen(del_req, timeout=15) as resp:
        print("3. Elementor cache endpoint ejecutado!")
except Exception as e:
    print("3. Elementor cache endpoint notice:", e)

