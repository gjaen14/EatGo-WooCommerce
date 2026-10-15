import json, urllib.request, base64

url_get = "https://eatgopty.com/wp-json/wp/v2/pages/564?context=edit"
username = "JaenDev"
password = "4n3FKy26SkBpwe8GPBzdbqEz"
auth_header = "Basic " + base64.b64encode(f"{username}:{password}".encode()).decode()

req = urllib.request.Request(url_get, headers={"Authorization": auth_header})
with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode())

elementor_data = json.loads(data["meta"]["_elementor_data"])

updated = 0
def update_loop_grids(elements):
    global updated
    for el in elements:
        if el.get("widgetType") == "loop-grid":
            old_tpl = el.get("settings", {}).get("template_id")
            print(f"Found loop-grid {el.get('id')}, template_id: {old_tpl} -> updating to 631")
            el.setdefault("settings", {})["template_id"] = "631"
            updated += 1
        if "elements" in el:
            update_loop_grids(el["elements"])

update_loop_grids(elementor_data)
print(f"Total loop-grids updated: {updated}")

url_post = "https://eatgopty.com/wp-json/wp/v2/pages/564"
payload = {
    "meta": {
        "_elementor_data": json.dumps(elementor_data)
    }
}

req_post = urllib.request.Request(url_post, data=json.dumps(payload).encode("utf-8"), headers={
    "Content-Type": "application/json",
    "Authorization": auth_header
})

with urllib.request.urlopen(req_post) as resp_post:
    print("Update status:", resp_post.getcode())
    print("Page 564 successfully updated with template 631!")
