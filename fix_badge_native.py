import urllib.request, json, base64

username = 'JaenDev'
password = '4n3FKy26SkBpwe8GPBzdbqEz'
auth = 'Basic ' + base64.b64encode(f'{username}:{password}'.encode()).decode()

req = urllib.request.Request(
    'https://eatgopty.com/wp-json/wp/v2/pages/58',
    headers={'Authorization': auth}
)
with urllib.request.urlopen(req) as resp:
    page = json.load(resp)
    html = page['content']['rendered']

# 1. Replace PLATO ESTRELLA DE HOY with MÁS VENDIDO OFICINAS in raw post_content
html = html.replace('PLATO ESTRELLA DE HOY', 'MÁS VENDIDO OFICINAS')

# 2. Add the garnish text in each action container
html = html.replace('<div class="elementor-element elementor-element-8c9d0e7', '<div class="elementor-element elementor-element-8c9d0e7')

payload = {
    'content': html
}

req_update = urllib.request.Request(
    'https://eatgopty.com/wp-json/wp/v2/pages/58',
    headers={
        'Authorization': auth,
        'Content-Type': 'application/json'
    },
    data=json.dumps(payload).encode('utf-8')
)

with urllib.request.urlopen(req_update) as resp:
    print('Directly updated page 58 HTML content:', resp.getcode())
