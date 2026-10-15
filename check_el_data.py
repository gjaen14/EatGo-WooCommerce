
import urllib.request, json

auth = 'Basic SmFlbkRldjo0bjNGS3kyNlNrQnB3ZThHUEJ6ZGJxRXo='
req = urllib.request.Request('https://eatgopty.com/wp-json/wp/v2/pages/58?context=edit', headers={'Authorization': auth})
with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode('utf-8'))

meta = data.get('meta', {})
print('meta keys:', list(meta.keys()))
for k, v in meta.items():
    print(k, type(v))
    if isinstance(v, str) and 'w_sync' in v:
        print('FOUND IN META:', k)
