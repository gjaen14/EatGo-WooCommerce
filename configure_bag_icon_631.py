import json, urllib.request, base64

with open("template_631_data.json") as f:
    elements = json.load(f)

def configure_icons(items):
    for item in items:
        if item.get("id") == "w14btna":
            item["settings"]["text"] = "+ Agregar al Pedido"
            item["settings"]["selected_icon"] = {
                "value": {
                    "id": 638,
                    "url": "https://eatgopty.com/wp-content/uploads/2026/09/bag.svg"
                },
                "library": "svg"
            }
            item["settings"]["icon_align"] = "left"
            item["settings"]["icon_indent"] = {"unit": "px", "size": 8}
        if "elements" in item:
            configure_icons(item["elements"])

configure_icons(elements)

with open("template_631_data.json", "w") as f:
    json.dump(elements, f)

url = "https://eatgopty.com/wp-json/wp/v2/elementor_library/631"
username = "JaenDev"
password = "4n3FKy26SkBpwe8GPBzdbqEz"
auth_header = "Basic " + base64.b64encode(f"{username}:{password}".encode()).decode()

payload = {
    "status": "publish",
    "meta": {
        "_elementor_data": json.dumps(elements)
    }
}

req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers={
    "Content-Type": "application/json",
    "Authorization": auth_header
})

with urllib.request.urlopen(req) as resp:
    print("Updated 631 with native selected_icon:", resp.getcode())
