import urllib.request
import json
import base64

username = 'JaenDev'
password = '4n3FKy26SkBpwe8GPBzdbqEz'
auth = 'Basic ' + base64.b64encode(f'{username}:{password}'.encode()).decode()

# 1. Fetch current 781
req = urllib.request.Request(
    'https://eatgopty.com/wp-json/wp/v2/elementor_library/781?context=edit',
    headers={'Authorization': auth}
)
with urllib.request.urlopen(req) as resp:
    post = json.load(resp)

data = json.loads(post['meta']['_elementor_data'])

# 2. Update widget 9d0e1f8
def update_button(elements):
    for el in elements:
        if el.get('id') == '9d0e1f8':
            st = el.get('settings', {})
            st['text'] = '+ Agregar al Pedido'
            st['link'] = {
                'url': '#',
                'is_external': False,
                'nofollow': False
            }
            st['_css_classes'] = 'woosq-btn'
            st.pop('custom_attributes', None)
            st['button_text_color'] = '#FFFFFF'
            st['background_color'] = '#C81C20'
            st['typography_typography'] = 'custom'
            st['typography_font_family'] = 'Open Sans'
            st['typography_font_weight'] = '800'
            st['typography_font_size'] = {'unit': 'px', 'size': 14}
            st['border_radius'] = {'unit': 'px', 'top': '50', 'right': '50', 'bottom': '50', 'left': '50', 'isLinked': True}
            st['text_padding'] = {'unit': 'px', 'top': '10', 'right': '16', 'bottom': '10', 'left': '14', 'isLinked': False}
            st['align'] = 'right'
            st['selected_icon'] = {
                'value': {
                    'id': 638,
                    'url': 'https://eatgopty.com/wp-content/uploads/2026/09/bag.svg'
                },
                'library': 'svg'
            }
            st['icon_align'] = 'left'
            st['icon_indent'] = {'unit': 'px', 'size': 8}
            st['box_shadow_box_shadow_type'] = 'yes'
            st['box_shadow_box_shadow'] = {
                'horizontal': 0,
                'vertical': 4,
                'blur': 12,
                'spread': 0,
                'color': 'rgba(245, 158, 11, 0.35)'
            }
            print('Successfully updated settings for widget 9d0e1f8!')
            return True
        if 'elements' in el:
            if update_button(el['elements']):
                return True
    return False

if not update_button(data):
    raise Exception("Widget 9d0e1f8 not found in template 781!")

payload = {
    'status': 'publish',
    'meta': {
        '_elementor_data': json.dumps(data)
    }
}

req_update = urllib.request.Request(
    'https://eatgopty.com/wp-json/wp/v2/elementor_library/781',
    headers={
        'Authorization': auth,
        'Content-Type': 'application/json'
    },
    data=json.dumps(payload).encode('utf-8')
)

with urllib.request.urlopen(req_update) as resp:
    print('Updated Template 781 HTTP status:', resp.getcode())
    res = json.load(resp)
    print('Template 781 successfully updated!')
