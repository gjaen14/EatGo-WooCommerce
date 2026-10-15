
import urllib.request, re

req = urllib.request.Request('https://eatgopty.com/', headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as resp:
    html = resp.read().decode('utf-8')

css_links = re.findall(r'<link[^>]+href=["']([^"']+\.css[^"']*)["']', html)
for link in css_links:
    try:
        req_c = urllib.request.Request(link, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req_c) as r:
            body = r.read().decode('utf-8')
            if 'MÁS VENDIDO OFICINAS' in body:
                print('*** FOUND MÁS VENDIDO OFICINAS IN CSS FILE:', link)
    except Exception as e:
        pass
