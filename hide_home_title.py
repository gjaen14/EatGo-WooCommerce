
import urllib.request, json, base64

auth = base64.b64encode(b'JaenDev:4n3FKy26SkBpwe8GPBzdbqEz').decode('utf-8')
req = urllib.request.Request('https://eatgopty.com/wp-json/wp/v2/pages/58?context=edit', headers={'Authorization': f'Basic {auth}'})
with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode('utf-8'))
    meta = data.get('meta', {})
    page_settings = meta.get('_elementor_page_settings', {})

# Hide page title natively in Elementor
page_settings['hide_title'] = 'yes'

update_payload = json.dumps({
    'meta': {
        '_elementor_page_settings': page_settings
    }
}).encode('utf-8')

req_up = urllib.request.Request('https://eatgopty.com/wp-json/wp/v2/pages/58', data=update_payload, headers={'Authorization': f'Basic {auth}', 'Content-Type': 'application/json'}, method='POST')
with urllib.request.urlopen(req_up) as resp:
    print('Set hide_title to yes in _elementor_page_settings!')
