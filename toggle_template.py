import urllib.request, json, base64

username = 'JaenDev'
password = '4n3FKy26SkBpwe8GPBzdbqEz'
auth = 'Basic ' + base64.b64encode(f'{username}:{password}'.encode()).decode()

# Fetch page 58
req = urllib.request.Request(
    'https://eatgopty.com/wp-json/wp/v2/pages/58?context=edit',
    headers={'Authorization': auth}
)
with urllib.request.urlopen(req) as resp:
    page = json.load(resp)

data = json.loads(page['meta']['_elementor_data'])

# Find widget 3a9e80b
def set_template(items, tid):
    for it in items:
        if it.get('id') == '3a9e80b':
            it['settings']['template_id'] = str(tid)
        if 'elements' in it:
            set_template(it['elements'], tid)

# 1. Set to 314
set_template(data, 314)
payload1 = {'meta': {'_elementor_data': json.dumps(data)}}
req1 = urllib.request.Request('https://eatgopty.com/wp-json/wp/v2/pages/58', headers={'Authorization': auth, 'Content-Type': 'application/json'}, data=json.dumps(payload1).encode('utf-8'))
urllib.request.urlopen(req1)

# 2. Set back to 190
set_template(data, 190)
payload2 = {'meta': {'_elementor_data': json.dumps(data)}}
req2 = urllib.request.Request('https://eatgopty.com/wp-json/wp/v2/pages/58', headers={'Authorization': auth, 'Content-Type': 'application/json'}, data=json.dumps(payload2).encode('utf-8'))
urllib.request.urlopen(req2)

print('Toggled template to reload 190!')
