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

for el in data[2]['elements']:
    if el.get('id') == 'c01vmod':
        html = el.get('settings', {}).get('html', '')
        
        # Remove the outer misplaced block
        outer_block = """  // Delegación idéntica a Menú Semanal (Post 564) para WPC Quick View modal
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
  });"""
        
        if outer_block in html:
            html = html.replace(outer_block, '')
            print("Removed misplaced outer block")

        # Now insert the click delegation INSIDE jQuery(document).ready(function($) { ... })
        correct_inner_delegation = """
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
});"""

        # Replace closing of jQuery ready
        if '});' in html and correct_inner_delegation not in html:
            # find last occurrence of });
            last_idx = html.rfind('});')
            if last_idx != -1:
                html = html[:last_idx] + correct_inner_delegation + html[last_idx+3:]
                print("Inserted click delegation INSIDE jQuery ready function")

        el['settings']['html'] = html
        break

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
