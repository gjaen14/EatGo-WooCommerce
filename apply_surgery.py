import json
import urllib.request
import base64

auth = base64.b64encode(b'JaenDev:4n3FKy26SkBpwe8GPBzdbqEz').decode('utf-8')

# 1. Snippet 660 surgery
with open('snippet_660_pre_surgery_backup.json', 'r', encoding='utf-8') as f:
    data_660 = json.load(f)

code_660 = data_660['meta']['_elementor_code']

target_660 = """      if (target.indexOf(diaSlug) !== -1) {
        $(this).addClass('is-active').css({
          'background-color': '#F59E0B',
          'border-color': '#F59E0B',
          'color': '#18181B',
          'font-weight': '800',
          'box-shadow': '0 2px 8px rgba(245,158,11,0.3)',
          'cursor': 'pointer'
        });
        $(this).find('*').css({ 'color': '#18181B', 'font-weight': '800' });
      } else {
        $(this).removeClass('is-active').css({
          'background-color': '#FFFFFF',
          'border': '1px solid #E5E7EB',
          'color': '#18181B',
          'font-weight': '600',
          'box-shadow': 'none',
          'cursor': 'pointer'
        });
        $(this).find('*').css({ 'color': '#18181B', 'font-weight': '600' });
      }"""

replacement_660 = """      if (target.indexOf(diaSlug) !== -1) {
        $(this).addClass('is-active');
      } else {
        $(this).removeClass('is-active');
      }"""

assert target_660 in code_660, "Target not found in snippet 660!"
new_code_660 = code_660.replace(target_660, replacement_660, 1)

payload_660 = json.dumps({
    'meta': {
        '_elementor_code': new_code_660
    }
}).encode('utf-8')

req_660 = urllib.request.Request(
    'https://eatgopty.com/wp-json/wp/v2/elementor_snippet/660',
    data=payload_660,
    headers={
        'Authorization': f'Basic {auth}',
        'Content-Type': 'application/json'
    },
    method='POST'
)

with urllib.request.urlopen(req_660) as resp:
    res = json.load(resp)
    print("Snippet 660 updated successfully! ID:", res.get('id'))

# 2. Page 564 element 307dd20b surgery
with open('page_564_pre_surgery_backup.json', 'r', encoding='utf-8') as f:
    data_564 = json.load(f)

edata_str = data_564['meta']['_elementor_data']
edata = json.loads(edata_str)

def clean_widget_307dd20b(elements):
    modified = False
    for el in elements:
        if el.get('id') == '307dd20b':
            val = el.get('settings', {}).get('paragraph', {}).get('value', '')
            target_pill_css = """    // 1. Píldoras
    $('[configuration-id^="pill-"]').each(function() {
      var cfg = $(this).attr('configuration-id');
      if (cfg === 'pill-' + dia) {
        $(this).css({
          'background-color': '#F59E0B',
          'border-color': '#F59E0B',
          'box-shadow': '0 2px 6px rgba(245,158,11,0.25)'
        });
      } else {
        $(this).css({
          'background-color': '#FFFFFF',
          'border-color': '#E5E7EB',
          'box-shadow': 'none'
        });
      }
    });"""

            replacement_pill_css = """    // 1. Píldoras
    $('[configuration-id^="pill-"]').each(function() {
      var cfg = $(this).attr('configuration-id');
      if (cfg === 'pill-' + dia) {
        $(this).addClass('is-active');
      } else {
        $(this).removeClass('is-active');
      }
    });"""
            if target_pill_css in val:
                new_val = val.replace(target_pill_css, replacement_pill_css, 1)
                el['settings']['paragraph']['value'] = new_val
                print("Element 307dd20b cleaned of inline css!")
                modified = True
        if 'elements' in el:
            if clean_widget_307dd20b(el['elements']):
                modified = True
    return modified

mod = clean_widget_307dd20b(edata)
if mod:
    new_edata_str = json.dumps(edata, ensure_ascii=False)
    payload_564 = json.dumps({
        'meta': {
            '_elementor_data': new_edata_str
        }
    }).encode('utf-8')
    req_564 = urllib.request.Request(
        'https://eatgopty.com/wp-json/wp/v2/pages/564',
        data=payload_564,
        headers={
            'Authorization': f'Basic {auth}',
            'Content-Type': 'application/json'
        },
        method='POST'
    )
    with urllib.request.urlopen(req_564) as resp:
        res = json.load(resp)
        print("Page 564 element 307dd20b updated successfully! ID:", res.get('id'))
else:
    print("Element 307dd20b target was not found or already clean.")
