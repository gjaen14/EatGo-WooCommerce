import json, urllib.request, base64

# Read menu_semanal_css.txt and remove double quotes inside url(...)
with open("menu_semanal_css.txt") as f:
    css_content = f.read()

# Replace url("...") with url(...)
import re
clean_css = re.sub(r'url\("([^"]+)"\)', r'url(\1)', css_content)

extra_rules = """
/* Anti-Lazyload Override for c02covr */
html body .e-con.e-parent:not(.e-lazyloaded) div.elementor-element.elementor-element-c02covr,
html body div.elementor-element.elementor-element-c02covr {
  background-size: cover !important;
  background-position: center center !important;
  background-repeat: no-repeat !important;
  min-height: 220px !important;
  height: 220px !important;
  width: 100% !important;
}

/* Fallback image for items without image like 648 (Macarrones) */
html body .e-loop-item-648 div.elementor-element.elementor-element-c02covr {
  background-image: url(https://eatgopty.com/wp-content/uploads/2026/09/Diseno-sin-titulo-6.png) !important;
}
"""

final_clean_css = extra_rules + "\n" + clean_css

username = "JaenDev"
password = "4n3FKy26SkBpwe8GPBzdbqEz"
auth_header = "Basic " + base64.b64encode(f"{username}:{password}".encode()).decode()

payload = {
    "meta": {
        "_elementor_page_settings": {
            "custom_css": final_clean_css
        }
    }
}

for post_id, endpoint in [(564, "pages"), (631, "elementor_library")]:
    url = f"https://eatgopty.com/wp-json/wp/v2/{endpoint}/{post_id}"
    req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers={
        "Content-Type": "application/json",
        "Authorization": auth_header
    })
    try:
        with urllib.request.urlopen(req) as resp:
            print(f"Updated {endpoint} {post_id}:", resp.getcode())
    except Exception as e:
        print(f"Error {endpoint} {post_id}:", e)

