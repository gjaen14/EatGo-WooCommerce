import urllib.request

for fname in ['local-564-frontend-desktop.css?ver=6ab87105de14a', 'base-desktop.css?ver=6ab8695d39d3f']:
    url = f"https://eatgopty.com/wp-content/uploads/elementor/css/{fname}"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=15) as resp:
            content = resp.read().decode('utf-8')
            print(f"=== {fname} (length {len(content)}) ===")
            print(content[:800])
    except Exception as e:
        print(f"Error {fname}: {e}")

