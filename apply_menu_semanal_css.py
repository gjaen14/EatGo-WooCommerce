import json, urllib.request, base64

with open("menu_semanal_css.txt") as f:
    css_content = f.read()

# Add anti-lazyload override and default image for products without featured media
extra_rules = """
/* Anti-Lazyload Override for c02covr */
html body .e-con.e-parent:not(.e-lazyloaded) div.elementor-element.elementor-element-c02covr,
html body div.elementor-element.elementor-element-c02covr {
  background-size: cover !important;
  background-position: center center !important;
  background-repeat: no-repeat !important;
  min-height: 220px !important;
  height: 220px !important;
}

/* Fallback image for items without image like 648 (Macarrones) */
html body .e-loop-item-648 div.elementor-element.elementor-element-c02covr {
  background-image: url("https://eatgopty.com/wp-content/uploads/2026/09/Diseno-sin-titulo-6.png") !important;
}
"""

final_css = extra_rules + "\n" + css_content

url_564 = "https://eatgopty.com/wp-json/wp/v2/pages/564"
username = "JaenDev"
password = "4n3FKy26SkBpwe8GPBzdbqEz"
auth_header = "Basic " + base64.b64encode(f"{username}:{password}".encode()).decode()

payload = {
    "meta": {
        "_elementor_page_settings": {
            "custom_css": final_css
        }
    }
}

req_564 = urllib.request.Request(url_564, data=json.dumps(payload).encode("utf-8"), headers={
    "Content-Type": "application/json",
    "Authorization": auth_header
})

with urllib.request.urlopen(req_564) as response:
    print("Page 564 updated:", response.getcode())

url_631 = "https://eatgopty.com/wp-json/wp/v2/elementor_library/631"
req_631 = urllib.request.Request(url_631, data=json.dumps(payload).encode("utf-8"), headers={
    "Content-Type": "application/json",
    "Authorization": auth_header
})

with urllib.request.urlopen(req_631) as response:
    print("Template 631 updated:", response.getcode())

