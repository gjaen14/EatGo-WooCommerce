import urllib.request
import json
import base64

auth_str = "JaenDev:4n3FKy26SkBpwe8GPBzdbqEz"
auth_header = "Basic " + base64.b64encode(auth_str.encode()).decode()

req = urllib.request.Request(
    "https://eatgopty.com/wp-json/wp/v2/pages/564?context=edit",
    headers={"Authorization": auth_header}
)

with urllib.request.urlopen(req, timeout=15) as r:
    data = json.loads(r.read().decode())
    print("Meta keys:", list(data.get("meta", {}).keys()))
    print("Template:", data.get("template"))

