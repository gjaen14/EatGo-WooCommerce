
import urllib.request, json, base64

auth = 'Basic SmFlbkRldjo0bjNGS3kyNlNrQnB3ZThHUEJ6ZGJxRXo='
req = urllib.request.Request('https://eatgopty.com/wp-json/wp/v2/pages/58', headers={'Authorization': auth, 'Content-Type': 'application/json'}, data=json.dumps({'content': ''}).encode('utf-8'), method='POST')
with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode('utf-8'))
    print('Reset raw content to empty, status:', resp.status)
