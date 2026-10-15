import json
import urllib.request
import base64

auth = base64.b64encode(b'JaenDev:4n3FKy26SkBpwe8GPBzdbqEz').decode('utf-8')

# 1. Restore Snippet 660
with open('snippet_660_pre_surgery_backup.json', 'r', encoding='utf-8') as f:
    backup_660 = json.load(f)

payload_660 = json.dumps({
    'title': backup_660.get('title', {}).get('rendered', 'EatGo Menú Semanal Motor Interactivo Dinámico'),
    'status': 'publish',
    'meta': {
        '_elementor_code': backup_660['meta']['_elementor_code'],
        '_elementor_location': backup_660['meta'].get('_elementor_location', 'elementor_body_end'),
        '_elementor_priority': backup_660['meta'].get('_elementor_priority', 1)
    }
}).encode('utf-8')

req_660 = urllib.request.Request(
    'https://eatgopty.com/wp-json/wp/v2/elementor_snippet/660',
    data=payload_660,
    headers={
        'Authorization': f'Basic {auth}',
        'Content-Type': 'application/json'
    },
    method='POST'
)

with urllib.request.urlopen(req_660) as resp:
    res_660 = json.load(resp)
    print("Snippet 660 restored successfully! Status:", res_660.get('status'))

# 2. Restore Page 564
with open('page_564_pre_surgery_backup.json', 'r', encoding='utf-8') as f:
    backup_564 = json.load(f)

payload_564 = json.dumps({
    'meta': {
        '_elementor_data': backup_564['meta']['_elementor_data'],
        '_elementor_page_settings': backup_564['meta'].get('_elementor_page_settings', {}),
        '_elementor_edit_mode': backup_564['meta'].get('_elementor_edit_mode', 'builder')
    }
}).encode('utf-8')

req_564 = urllib.request.Request(
    'https://eatgopty.com/wp-json/wp/v2/pages/564',
    data=payload_564,
    headers={
        'Authorization': f'Basic {auth}',
        'Content-Type': 'application/json'
    },
    method='POST'
)

with urllib.request.urlopen(req_564) as resp:
    res_564 = json.load(resp)
    print("Page 564 restored successfully! Status:", res_564.get('status'))
