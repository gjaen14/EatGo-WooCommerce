
import urllib.request, json

auth = 'Basic SmFlbkRldjo0bjNGS3kyNlNrQnB3ZThHUEJ6ZGJxRXo='
req = urllib.request.Request('https://eatgopty.com/wp-json/wp/v2/pages/58', headers={'Authorization': auth})
with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode('utf-8'))

rendered = data.get('content', {}).get('rendered', '')
pos = rendered.find('w_sync_cards_exact')
print('=== EXACT 300 CHARS BEFORE w_sync_cards_exact ===')
print(repr(rendered[max(0, pos-300):pos]))
print('=== EXACT 300 CHARS AFTER w_sync_cards_exact ===')
print(repr(rendered[pos:pos+300]))
