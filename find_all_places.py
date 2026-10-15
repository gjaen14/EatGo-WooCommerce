
import urllib.request, json, base64

auth = 'Basic SmFlbkRldjo0bjNGS3kyNlNrQnB3ZThHUEJ6ZGJxRXo='
req = urllib.request.Request('https://eatgopty.com/wp-json/wp/v2/pages/58', headers={'Authorization': auth})
with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode('utf-8'))

for k, v in data.items():
    if isinstance(v, str) and 'w_sync_cards_exact' in v:
        print('Found in key:', k)
    elif isinstance(v, dict):
        for subk, subv in v.items():
            if isinstance(subv, str) and 'w_sync_cards_exact' in subv:
                print(f'Found in {k}.{subk}')
