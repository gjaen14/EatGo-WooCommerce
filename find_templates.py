
import urllib.request, json, base64

auth = base64.b64encode(b'JaenDev:4n3FKy26SkBpwe8GPBzdbqEz').decode('utf-8')
# Find where custom-css or custom_css is stored in wp_postmeta via search
req = urllib.request.Request('https://eatgopty.com/wp-json/wp/v2/pages/58?context=edit', headers={'Authorization': f'Basic {auth}'})
with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode('utf-8'))
    meta = data.get('meta', {})
    for k, v in meta.items():
        if isinstance(v, str) and 'MÁS VENDIDO' in v:
            print('FOUND MÁS VENDIDO IN META:', k)
        elif isinstance(v, dict):
            for sk, sv in v.items():
                if isinstance(sv, str) and 'MÁS VENDIDO' in sv:
                    print(f'FOUND MÁS VENDIDO IN META: {k}.{sk}')
