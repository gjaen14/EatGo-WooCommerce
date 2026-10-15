import urllib.request
import json
import base64

username = 'JaenDev'
password = '4n3FKy26SkBpwe8GPBzdbqEz'
auth = 'Basic ' + base64.b64encode(f'{username}:{password}'.encode()).decode()

req = urllib.request.Request(
    'https://eatgopty.com/wp-json/wp/v2/pages/58?context=edit',
    headers={'Authorization': auth}
)
with urllib.request.urlopen(req) as resp:
    p = json.load(resp)

data = json.loads(p['meta']['_elementor_data'])

found = False
for top in data:
    def process_el(el):
        global found
        if el.get('id') == 'c01vmod':
            found = True
            html = el.get('settings', {}).get('html', '')
            
            # 1. Add suppression CSS if not present
            suppression_css = """
.page-id-58 .added_to_cart,
.page-id-58 a.wc-forward,
.added_to_cart,
a.wc-forward {
  display: none !important;
  visibility: hidden !important;
  opacity: 0 !important;
  pointer-events: none !important;
  height: 0 !important;
  width: 0 !important;
  margin: 0 !important;
  padding: 0 !important;
  line-height: 0 !important;
}
"""
            if '.added_to_cart' not in html:
                html = html.replace('</style>', suppression_css + '\n</style>', 1)
                print('Added suppression CSS to c01vmod')

            # 2. Replace sync logic for button 9d0e1f8
            old_sync = """      if (pid) {
        var $btn = $card.find(".elementor-element-9d0e1f8 a.elementor-button, .elementor-element-9d0e1f8 .elementor-button");
        $btn.attr("data-product_id", pid).attr("data-quantity", "1").attr("href", "?add-to-cart=" + pid);
        $btn.addClass("ajax_add_to_cart add_to_cart_button product_type_simple");
      }"""

            new_sync = """      if (pid) {
        var $btn = $card.find(".elementor-element-9d0e1f8 a.elementor-button, .elementor-element-9d0e1f8 .elementor-button, a.elementor-button:has(.elementor-button-text:contains(\\"Agregar\\"))");
        $btn.removeClass("ajax_add_to_cart add_to_cart_button product_type_simple")
            .addClass("woosq-btn")
            .attr("data-id", pid)
            .attr("href", "#")
            .removeAttr("data-product_id")
            .removeAttr("data-quantity");
      }"""

            if old_sync in html:
                html = html.replace(old_sync, new_sync)
                print('Replaced button sync logic in c01vmod')
            else:
                print('Warning: old_sync not found exactly in c01vmod')

            el['settings']['html'] = html
            return

        for child in el.get('elements', []):
            process_el(child)

    process_el(top)

if not found:
    raise Exception("c01vmod not found in Post 58!")

payload = {
    'meta': {
        '_elementor_data': json.dumps(data)
    }
}

req_update = urllib.request.Request(
    'https://eatgopty.com/wp-json/wp/v2/pages/58',
    headers={
        'Authorization': auth,
        'Content-Type': 'application/json'
    },
    data=json.dumps(payload).encode('utf-8')
)

with urllib.request.urlopen(req_update) as resp:
    print('Updated Post 58 HTTP:', resp.getcode())
