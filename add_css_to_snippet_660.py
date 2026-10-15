import urllib.request
import json
import base64

username = 'JaenDev'
password = '4n3FKy26SkBpwe8GPBzdbqEz'
auth = 'Basic ' + base64.b64encode(f'{username}:{password}'.encode()).decode()

req = urllib.request.Request(
    'https://eatgopty.com/wp-json/wp/v2/elementor_snippet/660',
    headers={'Authorization': auth}
)
with urllib.request.urlopen(req) as resp:
    data = json.load(resp)

code = data.get('meta', {}).get('_elementor_code', '')

css_extra = """
/* Reglas de Imágenes CSS Oficiales para Loop Items de Elementor */
.page-id-564 .post-707 [data-id="c02covr"],
.page-id-564 .e-loop-item-707 [data-id="c02covr"] {
  background-image: url("https://eatgopty.com/wp-content/uploads/2026/09/Diseno-sin-titulo-17.png") !important;
}
.page-id-564 .post-656 [data-id="c02covr"],
.page-id-564 .e-loop-item-656 [data-id="c02covr"] {
  background-image: url("https://eatgopty.com/wp-content/uploads/2026/09/Albondigas-con-pasta.png") !important;
}
.page-id-564 .post-651 [data-id="c02covr"],
.page-id-564 .e-loop-item-651 [data-id="c02covr"] {
  background-image: url("https://eatgopty.com/wp-content/uploads/2026/09/arroz-con-chuleta.png") !important;
}
.page-id-564 .post-657 [data-id="c02covr"],
.page-id-564 .e-loop-item-657 [data-id="c02covr"] {
  background-image: url("https://eatgopty.com/wp-content/uploads/2026/09/rabito.png") !important;
}
.page-id-564 .post-690 [data-id="c02covr"],
.page-id-564 .e-loop-item-690 [data-id="c02covr"] {
  background-image: url("https://eatgopty.com/wp-content/uploads/2026/09/Diseno-sin-titulo-15.png") !important;
}
.page-id-564 .post-685 [data-id="c02covr"],
.page-id-564 .e-loop-item-685 [data-id="c02covr"] {
  background-image: url("https://eatgopty.com/wp-content/uploads/2026/09/Diseno-sin-titulo-13.png") !important;
}
.page-id-564 .post-688 [data-id="c02covr"],
.page-id-564 .e-loop-item-688 [data-id="c02covr"] {
  background-image: url("https://eatgopty.com/wp-content/uploads/2026/09/Diseno-sin-titulo-14.png") !important;
}
.page-id-564 .post-683 [data-id="c02covr"],
.page-id-564 .e-loop-item-683 [data-id="c02covr"] {
  background-image: url("https://eatgopty.com/wp-content/uploads/2026/09/Diseno-sin-titulo-8.png") !important;
}
.page-id-564 .post-670 [data-id="c02covr"],
.page-id-564 .e-loop-item-670 [data-id="c02covr"] {
  background-image: url("https://eatgopty.com/wp-content/uploads/2026/09/Diseno-sin-titulo-10.png") !important;
}
.page-id-564 .post-676 [data-id="c02covr"],
.page-id-564 .e-loop-item-676 [data-id="c02covr"] {
  background-image: url("https://eatgopty.com/wp-content/uploads/2026/09/Diseno-sin-titulo-11.png") !important;
}
.page-id-564 .post-669 [data-id="c02covr"],
.page-id-564 .e-loop-item-669 [data-id="c02covr"] {
  background-image: url("https://eatgopty.com/wp-content/uploads/2026/09/Diseno-sin-titulo-7.png") !important;
}
.page-id-564 .post-699 [data-id="c02covr"],
.page-id-564 .e-loop-item-699 [data-id="c02covr"] {
  background-image: url("https://eatgopty.com/wp-content/uploads/2026/09/Diseno-sin-titulo-16.png") !important;
}
.page-id-564 .post-668 [data-id="c02covr"],
.page-id-564 .e-loop-item-668 [data-id="c02covr"] {
  background-image: url("https://eatgopty.com/wp-content/uploads/2026/09/Diseno-sin-titulo-8.png") !important;
}
.page-id-564 .post-664 [data-id="c02covr"],
.page-id-564 .e-loop-item-664 [data-id="c02covr"] {
  background-image: url("https://eatgopty.com/wp-content/uploads/2026/09/Diseno-sin-titulo-8.png") !important;
}
.page-id-564 .post-666 [data-id="c02covr"],
.page-id-564 .e-loop-item-666 [data-id="c02covr"] {
  background-image: url("https://eatgopty.com/wp-content/uploads/2026/09/Diseno-sin-titulo-9.png") !important;
}
.page-id-564 .post-662 [data-id="c02covr"],
.page-id-564 .e-loop-item-662 [data-id="c02covr"] {
  background-image: url("https://eatgopty.com/wp-content/uploads/2026/09/Diseno-sin-titulo-7.png") !important;
}
"""

if '</style>' in code:
    code = code.replace('</style>', css_extra + '\n</style>')

payload = {
    'meta': {
        '_elementor_code': code
    }
}

req_update = urllib.request.Request(
    'https://eatgopty.com/wp-json/wp/v2/elementor_snippet/660',
    headers={
        'Authorization': auth,
        'Content-Type': 'application/json'
    },
    data=json.dumps(payload).encode('utf-8')
)

with urllib.request.urlopen(req_update) as resp:
    res = json.load(resp)
    print('Snippet 660 CSS enhanced successfully!')
