import urllib.request
import re

url = "https://eatgopty.com/menu-semanal/"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, timeout=15) as resp:
    html = resp.read().decode('utf-8')

# Search for inline style tags with elementor or custom css
style_tags = re.findall(r'<style[^>]*>(.*?)</style>', html, re.DOTALL)
print("Total style tags:", len(style_tags))
for idx, st in enumerate(style_tags):
    if "676ea28c" in st or "card-plato" in st or "flex" in st or "elementor-element" in st:
        print(f"--- Style tag {idx} (len {len(st)}) ---")
        print(st[:500])
        print("...\n")

