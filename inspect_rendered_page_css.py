import urllib.request
import re

url = "https://eatgopty.com/menu-semanal/"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, timeout=15) as resp:
    html = resp.read().decode('utf-8')

print("Page HTML size:", len(html))

# Look for elementor post CSS link
css_links = re.findall(r'<link[^>]*href="([^"]*uploads/elementor/css/[^"]*)"', html)
print("Elementor CSS files:", css_links)

# Let's inspect the first 10 elementor-element divs in body
elements = re.findall(r'<div class="([^"]*elementor-element[^"]*)"', html)
for el in elements[:10]:
    print("Element:", el)

