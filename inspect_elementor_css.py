import urllib.request
import re

url = "https://eatgopty.com/menu-semanal/"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, timeout=15) as resp:
    html = resp.read().decode('utf-8')

# Search for any css files or elementor styles
links = re.findall(r'<link[^>]*rel=[\'"]stylesheet[\'"][^>]*href=[\'"]([^\'"]+)[\'"]', html)
print(f"Total stylesheets: {len(links)}")
for l in links:
    if 'elementor' in l:
        print("Elementor CSS link:", l)

