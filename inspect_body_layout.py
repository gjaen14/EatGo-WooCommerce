import urllib.request
import re

css_url = "https://eatgopty.com/wp-content/uploads/elementor/css/base-desktop.css?ver=6ab8695d39d3f"
content = urllib.request.urlopen(css_url).read().decode('utf-8')
print("e-flexbox-base rules:")
for r in content.split('}'):
    if 'e-flexbox-base' in r or 'elementor-564' in r:
        print(" ->", r.strip())

