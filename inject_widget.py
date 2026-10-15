import json, urllib.request, base64

with open('home_page_58_data.json') as f:
    data = json.load(f)

script_html = """<script>
jQuery(function($) {
  function syncHomeCards() {
    $('.elementor-element-3d4e5f2').each(function() {
      $(this).find('p, span').text('MÁS VENDIDO OFICINAS');
    });
    $('.elementor-element-8c9d0e7').each(function() {
      var $row = $(this);
      $row.contents().filter(function() {
        return this.nodeType === 3;
      }).remove();
      if (!$row.find('.eg-garnish-label').length) {
        $row.prepend('<span class="eg-garnish-label" style="font-family:\'Open Sans\',sans-serif;font-size:13px;font-weight:500;color:#A1A1AA;line-height:1.2;display:inline-block;">Incluye guarnición criolla</span>');
      }
    });
  }
  syncHomeCards();
  setInterval(syncHomeCards, 300);
});
</script>"""

widget = {
    'id': 'w_sync_cards_exact',
    'elType': 'widget',
    'widgetType': 'html',
    'settings': {
        'html': script_html
    },
    'elements': []
}

data[0]['elements'].append(widget)

username = 'JaenDev'
password = '4n3FKy26SkBpwe8GPBzdbqEz'
auth = 'Basic ' + base64.b64encode(f'{username}:{password}'.encode()).decode()

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
    res = json.load(resp)
    print('Clean injected HTML widget into Page 58! Status:', resp.getcode())
