
import urllib.request, json, base64

auth = base64.b64encode(b'JaenDev:4n3FKy26SkBpwe8GPBzdbqEz').decode('utf-8')
req = urllib.request.Request('https://eatgopty.com/wp-json/wp/v2/pages/58?context=edit', headers={'Authorization': f'Basic {auth}'})
with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode('utf-8'))
    meta = data.get('meta', {})
    page_settings = meta.get('_elementor_page_settings', {})
    print('Type of page_settings:', type(page_settings))
    if isinstance(page_settings, dict):
        print('Keys in page_settings:', list(page_settings.keys()))
        custom_css = page_settings.get('custom_css', '')
        print('Length of custom_css in page_settings:', len(custom_css))
