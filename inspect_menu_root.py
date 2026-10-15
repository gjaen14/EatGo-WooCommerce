import urllib.request
import re

url = "https://eatgopty.com/menu-semanal/"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, timeout=15) as resp:
    html = resp.read().decode('utf-8')

# Find elementor-element-676ea28c
idx = html.find("elementor-element-676ea28c")
print("Found 676ea28c at:", idx)
if idx != -1:
    print(html[idx:idx+250])

# Find the class list of elementor-element-676ea28c
m = re.search(r'<div class="([^"]*elementor-element-676ea28c[^"]*)"', html)
if m:
    classes = m.group(1).split()
    print("Classes on 676ea28c:", classes)
    
    # Let's inspect CSS for each class
    css_url = "https://eatgopty.com/wp-content/uploads/elementor/css/local-564-frontend-desktop.css?ver=6ab87105de14a"
    css_content = urllib.request.urlopen(css_url).read().decode('utf-8')
    for c in classes:
        for rule in css_content.split('}'):
            if c in rule:
                print(f"Rule for .{c} -> {rule.strip()}")

