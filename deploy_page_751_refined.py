import json
import urllib.request
import base64

auth_str = "JaenDev:4n3FKy26SkBpwe8GPBzdbqEz"
auth_header = "Basic " + base64.b64encode(auth_str.encode()).decode()

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
    print("Página 751 actualizada en WordPress! Status:", res_p.get('status'))

try:
    del_req = urllib.request.Request(
        'https://eatgopty.com/wp-json/elementor/v1/cache',
        headers={'Authorization': auth_header},
        method='DELETE'
    )
    with urllib.request.urlopen(del_req, timeout=15) as resp:
        print("Elementor cache endpoint ejecutado!")
except Exception as e:
    print("Elementor cache endpoint notice:", e)

