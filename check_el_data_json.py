
import urllib.request, json

auth = 'Basic SmFlbkRldjo0bjNGS3kyNlNrQnB3ZThHUEJ6ZGJxRXo='
req = urllib.request.Request('https://eatgopty.com/wp-json/wp/v2/pages/58?context=edit', headers={'Authorization': auth})
with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode('utf-8'))

raw = data.get('content', {}).get('raw', '')
print('Length of raw:', len(raw))
print('Has 7b0a2a6c in raw?', '7b0a2a6c' in raw)
print('Has 2852bda3 in raw?', '2852bda3' in raw)
