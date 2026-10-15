import urllib.request
import json
import base64

username = 'JaenDev'
password = '4n3FKy26SkBpwe8GPBzdbqEz'
auth = 'Basic ' + base64.b64encode(f'{username}:{password}'.encode()).decode()

with open('snippet_5_engine.php') as f:
    php_code = f.read()

# Strip <?php from start if present
if php_code.startswith('<?php'):
    php_code = php_code[5:].strip()

payload = {
    'name': 'EatGo Weekly Rotation Query Engine',
    'desc': 'Motor de rotacion semanal de menu y hooks de consulta para Loop Grids en Elementor.',
    'code': php_code,
    'scope': 'global',
    'active': 1,
    'priority': 1
}

req = urllib.request.Request(
    'https://eatgopty.com/wp-json/code-snippets/v1/snippets/5',
    headers={
        'Authorization': auth,
        'Content-Type': 'application/json'
    },
    data=json.dumps(payload).encode('utf-8')
)

with urllib.request.urlopen(req) as resp:
    data = json.load(resp)
    print('Snippet 5 updated successfully! Active:', data.get('active'))
