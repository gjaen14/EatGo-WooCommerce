import json, urllib.request, base64

with open("template_631_data.json") as f:
    elementor_data = f.read()

custom_css = """
/* Hover Micro-interactions */
.elementor-631 .elementor-element-c01root:hover {
  transform: translateY(-4px);
  transition: transform 0.25s ease, box-shadow 0.25s ease;
  box-shadow: 0 12px 24px rgba(0,0,0,0.08) !important;
}

/* Primary Button Styling */
.elementor-631 .elementor-element-w14btna a {
  background-color: #F59E0B !important;
  color: #000000 !important;
  font-family: 'Open Sans', sans-serif !important;
  font-weight: 800 !important;
  letter-spacing: -0.2px !important;
  transition: all 0.2s ease !important;
  box-shadow: 0 4px 12px rgba(245, 158, 11, 0.28) !important;
}

.elementor-631 .elementor-element-w14btna a:hover {
  background-color: #D97706 !important;
  color: #000000 !important;
  transform: translateY(-1px) !important;
  box-shadow: 0 6px 16px rgba(245, 158, 11, 0.38) !important;
}

/* Secondary Button Hover */
.elementor-631 .elementor-element-w15btnw a:hover {
  background-color: #E4E4E7 !important;
  color: #18181B !important;
}
"""

page_settings = {
    "custom_css": custom_css
}

url = "https://eatgopty.com/wp-json/wp/v2/elementor_library/631"
username = "JaenDev"
password = "4n3FKy26SkBpwe8GPBzdbqEz"
auth_header = "Basic " + base64.b64encode(f"{username}:{password}".encode()).decode()

payload = {
    "status": "publish",
    "meta": {
        "_elementor_edit_mode": "builder",
        "_elementor_template_type": "loop-item",
        "_elementor_data": elementor_data,
        "_elementor_page_settings": page_settings
    }
}

req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers={
    "Content-Type": "application/json",
    "Authorization": auth_header
})

try:
    with urllib.request.urlopen(req) as response:
        print("Status code:", response.getcode())
        resp_data = json.loads(response.read().decode())
        print("Updated Post ID:", resp_data.get("id"))
        print("Title:", resp_data.get("title", {}).get("rendered"))
except urllib.error.HTTPError as e:
    print("HTTP Error:", e.code)
    print("Error body:", e.read().decode()[:500])
except Exception as e:
    print("Error:", str(e))
