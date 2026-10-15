import urllib.request
import json
import base64
import re

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
            
            # 1. Ensure CSS suppression
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

            # 2. Replace the button sync block
            # Pattern matching the old block
            old_pattern = r'if\s*\(\s*pid\s*\)\s*\{\s*var\s+\$btn\s*=\s*\$card\.find\([^\)]+\);[\s\S]*?\$btn\.addClass\([^\)]+\);\s*\}'
            
            new_block = """if (pid) {
        var $wrap = $card.find(".elementor-element-9d0e1f8");
        $wrap.removeClass("ajax_add_to_cart add_to_cart_button product_type_simple");
        var $btn = $card.find(".elementor-element-9d0e1f8 a.elementor-button, .elementor-element-9d0e1f8 .elementor-button, a.elementor-button:has(.elementor-button-text:contains(\\"Agregar\\"))");
        $btn.removeClass("ajax_add_to_cart add_to_cart_button product_type_simple")
            .addClass("woosq-btn")
            .attr("data-id", pid)
            .attr("href", "#")
            .removeAttr("data-product_id")
            .removeAttr("data-quantity");
      }"""

            if re.search(old_pattern, html):
                html = re.sub(old_pattern, new_block, html, count=1)
                print('Successfully replaced button sync block with regex')
            else:
                print('Warning: old_pattern did not match, checking manual match')
                target = '$btn.addClass("ajax_add_to_cart add_to_cart_button product_type_simple");'
                if target in html:
                    print('Target substring found!')

            # 3. Add explicit click delegation for woosq_open on the Home card buttons
            click_code = """
  // Delegación idéntica a Menú Semanal (Post 564) para WPC Quick View modal
  $(document).on("click", ".elementor-element-9d0e1f8 a, .elementor-element-9d0e1f8 .elementor-button, .elementor-781 .woosq-btn", function(e) {
    e.preventDefault();
    e.stopPropagation();
    if (typeof e.stopImmediatePropagation === "function") e.stopImmediatePropagation();
    var $b = $(this).closest("a");
    var pid = $b.attr("data-id");
    if (!pid) {
      var $card = $(this).closest(".e-loop-item, [class*='post-']");
      var match = ($card.attr("class") || "").match(/(?:post-|e-loop-item-)(\\d+)/);
      if (match && match[1]) pid = match[1];
    }
    if (pid) {
      if (typeof woosq_open === "function") {
        woosq_open(pid);
      } else {
        $(document.body).trigger("woosq_open", [pid]);
      }
    }
  });
"""
            if 'Delegación idéntica a Menú Semanal' not in html:
                # Insert before </script>
                html = html.replace('</script>', click_code + '\n</script>', 1)
                print('Added woosq_open click handler to c01vmod')

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
