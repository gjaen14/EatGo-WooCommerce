
# Fetch the actual compiled CSS of Elementor on Home page
import urllib.request, re

req = urllib.request.Request('https://eatgopty.com/', headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as resp:
    html = resp.read().decode('utf-8')

# Find all CSS file links
css_links = re.findall(r'<link[^>]+href=["']([^"']+\.css[^"']*)["']', html)
print('Total css files:', len(css_links))
for link in css_links:
    if 'post-58' in link or 'post-190' in link or 'custom' in link or 'elementor' in link:
        print('Checking link:', link)
        try:
            req_css = urllib.request.Request(link, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req_css) as resp_css:
                css_body = resp_css.read().decode('utf-8')
                if 'MÁS VENDIDO' in css_body or '3d4e5f2' in css_body:
                    print(f'*** FOUND 3d4e5f2 in {link}! ***')
                    for line in css_body.split('
'):
                        if '3d4e5f2' in line or 'MÁS VENDIDO' in line or 'content:' in line:
                            print(' ', line[:120])
        except Exception as e:
            print('Error reading link:', e)
