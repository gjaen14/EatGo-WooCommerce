import urllib.request, json, base64

username = 'JaenDev'
password = '4n3FKy26SkBpwe8GPBzdbqEz'
auth = 'Basic ' + base64.b64encode(f'{username}:{password}'.encode()).decode()

req = urllib.request.Request(
    'https://eatgopty.com/wp-json/wp/v2/elementor_library/190?context=edit',
    headers={'Authorization': auth}
)
with urllib.request.urlopen(req) as resp:
    post = json.load(resp)

data = json.loads(post['meta']['_elementor_data'])

# Recursive search for 3d4e5f2 and replace editor text
def replace_badge(items):
    for it in items:
        if it.get('id') == '3d4e5f2':
            it['settings']['editor'] = '<p><span class="eg-badge-tag">MÁS VENDIDO OFICINAS</span></p>'
        if 'elements' in it:
            replace_badge(it['elements'])

replace_badge(data)

payload = {
    'status': 'publish',
    'meta': {
        '_elementor_data': json.dumps(data)
    }
}

req_update = urllib.request.Request(
    'https://eatgopty.com/wp-json/wp/v2/elementor_library/190',
    headers={
        'Authorization': auth,
        'Content-Type': 'application/json'
    },
    data=json.dumps(payload).encode('utf-8')
)

with urllib.request.urlopen(req_update) as resp:
    print('Updated Template 190 badge text:', resp.getcode())
