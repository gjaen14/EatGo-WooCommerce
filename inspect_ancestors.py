import urllib.request
import re

url = "https://eatgopty.com/menu-semanal/"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, timeout=15) as resp:
    html = resp.read().decode('utf-8')

idx = html.find("elementor-element-676ea28c")
# Print 1500 chars before this element to see the parent HTML tags
print("HTML BEFORE 676ea28c:\n", html[max(0, idx-1500):idx])

