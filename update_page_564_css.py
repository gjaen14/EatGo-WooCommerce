import urllib.request
import json
import base64

username = 'JaenDev'
password = '4n3FKy26SkBpwe8GPBzdbqEz'
auth = 'Basic ' + base64.b64encode(f'{username}:{password}'.encode()).decode()

# 1. Fetch current Page 564
req = urllib.request.Request(
    'https://eatgopty.com/wp-json/wp/v2/pages/564?context=edit',
    headers={'Authorization': auth}
)
with urllib.request.urlopen(req) as resp:
    page = json.load(resp)

ps = page.get('meta', {}).get('_elementor_page_settings', {})
if isinstance(ps, str):
    ps = json.loads(ps)

current_css = ps.get('custom_css', '')

additional_rules = """
/* Reglas CSS Oficiales de Productos para Loop Grid Nativo (0 manipulación JS) */
html body .e-loop-item-707 div.elementor-element.elementor-element-c02covr {
  background-image: url("https://eatgopty.com/wp-content/uploads/2026/09/Diseno-sin-titulo-17.png") !important;
}
html body .e-loop-item-656 div.elementor-element.elementor-element-c02covr {
  background-image: url("https://eatgopty.com/wp-content/uploads/2026/09/Albondigas-con-pasta.png") !important;
}
html body .e-loop-item-651 div.elementor-element.elementor-element-c02covr {
  background-image: url("https://eatgopty.com/wp-content/uploads/2026/09/arroz-con-chuleta.png") !important;
}
html body .e-loop-item-657 div.elementor-element.elementor-element-c02covr {
  background-image: url("https://eatgopty.com/wp-content/uploads/2026/09/rabito.png") !important;
}
html body .e-loop-item-690 div.elementor-element.elementor-element-c02covr {
  background-image: url("https://eatgopty.com/wp-content/uploads/2026/09/Diseno-sin-titulo-15.png") !important;
}
html body .e-loop-item-685 div.elementor-element.elementor-element-c02covr {
  background-image: url("https://eatgopty.com/wp-content/uploads/2026/09/Diseno-sin-titulo-13.png") !important;
}
html body .e-loop-item-688 div.elementor-element.elementor-element-c02covr {
  background-image: url("https://eatgopty.com/wp-content/uploads/2026/09/Diseno-sin-titulo-14.png") !important;
}
html body .e-loop-item-683 div.elementor-element.elementor-element-c02covr {
  background-image: url("https://eatgopty.com/wp-content/uploads/2026/09/Diseno-sin-titulo-8.png") !important;
}
html body .e-loop-item-670 div.elementor-element.elementor-element-c02covr {
  background-image: url("https://eatgopty.com/wp-content/uploads/2026/09/Diseno-sin-titulo-10.png") !important;
}
html body .e-loop-item-676 div.elementor-element.elementor-element-c02covr {
  background-image: url("https://eatgopty.com/wp-content/uploads/2026/09/Diseno-sin-titulo-11.png") !important;
}
html body .e-loop-item-669 div.elementor-element.elementor-element-c02covr {
  background-image: url("https://eatgopty.com/wp-content/uploads/2026/09/Diseno-sin-titulo-7.png") !important;
}
html body .e-loop-item-699 div.elementor-element.elementor-element-c02covr {
  background-image: url("https://eatgopty.com/wp-content/uploads/2026/09/Diseno-sin-titulo-16.png") !important;
}
html body .e-loop-item-668 div.elementor-element.elementor-element-c02covr {
  background-image: url("https://eatgopty.com/wp-content/uploads/2026/09/Diseno-sin-titulo-8.png") !important;
}
html body .e-loop-item-664 div.elementor-element.elementor-element-c02covr {
  background-image: url("https://eatgopty.com/wp-content/uploads/2026/09/Diseno-sin-titulo-8.png") !important;
}
html body .e-loop-item-666 div.elementor-element.elementor-element-c02covr {
  background-image: url("https://eatgopty.com/wp-content/uploads/2026/09/Diseno-sin-titulo-9.png") !important;
}
html body .e-loop-item-662 div.elementor-element.elementor-element-c02covr {
  background-image: url("https://eatgopty.com/wp-content/uploads/2026/09/Diseno-sin-titulo-7.png") !important;
}
"""

for item in ['e-loop-item-707', 'e-loop-item-656', 'e-loop-item-690']:
    if item in current_css:
        print(f'{item} already present, skipping append')
        break
else:
    current_css = current_css + "\n" + additional_rules
    ps['custom_css'] = current_css
    payload = {
        'meta': {
            '_elementor_page_settings': ps
        }
    }
    req_update = urllib.request.Request(
        'https://eatgopty.com/wp-json/wp/v2/pages/564',
        headers={
            'Authorization': auth,
            'Content-Type': 'application/json'
        },
        data=json.dumps(payload).encode('utf-8')
    )
    with urllib.request.urlopen(req_update) as resp:
        res = json.load(resp)
        print('Page 564 custom_css updated successfully!')

