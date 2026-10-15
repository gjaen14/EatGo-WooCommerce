import urllib.request
import json
import base64

auth = 'Basic SmFlbkRldjo0bjNGS3kyNlNrQnB3ZThHUEJ6ZGJxRXo='

# 1. Fetch current Header 677
req = urllib.request.Request(
    'https://eatgopty.com/wp-json/wp/v2/elementor_library/677?context=edit',
    headers={'Authorization': auth}
)
with urllib.request.urlopen(req) as resp:
    post_data = json.loads(resp.read().decode('utf-8'))

meta = post_data.get('meta', {})
el_data = json.loads(meta.get('_elementor_data', '[]'))
page_settings = meta.get('_elementor_page_settings', {})

# 2. Surgically modify widget 665ecca1 in _elementor_data
widget_found = False

def update_nav_widget(elements):
    global widget_found
    for el in elements:
        if el.get('id') == '665ecca1':
            widget_found = True
            settings = el.setdefault('settings', {})
            # Add dedicated encapsulation class
            settings['_css_classes'] = 'eatgo-nav-pills'
            # Add surgical custom CSS directly to this widget
            settings['custom_css'] = (
                "selector .elementor-nav-menu--main .elementor-item,\n"
                "selector .elementor-nav-menu--main:not(.e--pointer-framed) .elementor-item:before,\n"
                "selector .elementor-nav-menu--main:not(.e--pointer-framed) .elementor-item:after,\n"
                "selector .elementor-nav-menu--main:not(.e--pointer-framed) .elementor-item.elementor-item-active:before,\n"
                "selector .elementor-nav-menu--main:not(.e--pointer-framed) .elementor-item.elementor-item-active:after,\n"
                ".eatgo-nav-pills .elementor-nav-menu--main .elementor-item,\n"
                ".eatgo-nav-pills .elementor-nav-menu--main:not(.e--pointer-framed) .elementor-item:before,\n"
                ".eatgo-nav-pills .elementor-nav-menu--main:not(.e--pointer-framed) .elementor-item:after,\n"
                ".eatgo-nav-pills .elementor-nav-menu--main:not(.e--pointer-framed) .elementor-item.elementor-item-active:before,\n"
                ".eatgo-nav-pills .elementor-nav-menu--main:not(.e--pointer-framed) .elementor-item.elementor-item-active:after {\n"
                "  border-radius: 50px !important;\n"
                "}\n"
            )
            print("Updated widget 665ecca1 settings with eatgo-nav-pills and custom_css.")
        if 'elements' in el:
            update_nav_widget(el['elements'])

update_nav_widget(el_data)
if not widget_found:
    raise Exception("Widget 665ecca1 not found in Header 677!")

# 3. Also update page_settings['custom_css'] for Rule 1 to ensure pill border-radius
current_custom_css = page_settings.get('custom_css', '')
old_rule_1 = """/* 1. Eliminar pseudo-elementos residuales de punteros */
.elementor-677 .elementor-widget-nav-menu .elementor-nav-menu .elementor-item:before,
.elementor-677 .elementor-widget-nav-menu .elementor-nav-menu .elementor-item:after,
.elementor-677 .elementor-widget-nav-menu .elementor-item:before,
.elementor-677 .elementor-widget-nav-menu .elementor-item:after {
  display: none;
  content: none;
}"""

new_rule_1 = """/* 1. Menú Principal: Diseño Píldora para Enlaces, Hover y Puntero de Fondo */
.eatgo-nav-pills .elementor-nav-menu--main .elementor-item,
.eatgo-nav-pills .elementor-nav-menu--main:not(.e--pointer-framed) .elementor-item:before,
.eatgo-nav-pills .elementor-nav-menu--main:not(.e--pointer-framed) .elementor-item:after,
.eatgo-nav-pills .elementor-nav-menu--main:not(.e--pointer-framed) .elementor-item.elementor-item-active:before,
.eatgo-nav-pills .elementor-nav-menu--main:not(.e--pointer-framed) .elementor-item.elementor-item-active:after,
.elementor-677 .elementor-element-665ecca1 .elementor-nav-menu--main .elementor-item,
.elementor-677 .elementor-element-665ecca1 .elementor-nav-menu--main:not(.e--pointer-framed) .elementor-item:before,
.elementor-677 .elementor-element-665ecca1 .elementor-nav-menu--main:not(.e--pointer-framed) .elementor-item:after,
.elementor-677 .elementor-element-665ecca1 .elementor-nav-menu--main:not(.e--pointer-framed) .elementor-item.elementor-item-active:before,
.elementor-677 .elementor-element-665ecca1 .elementor-nav-menu--main:not(.e--pointer-framed) .elementor-item.elementor-item-active:after {
  border-radius: 50px !important;
}"""

if old_rule_1 in current_custom_css:
    page_settings['custom_css'] = current_custom_css.replace(old_rule_1, new_rule_1, 1)
    print("Replaced Rule 1 in page_settings['custom_css']")
else:
    # Prepend new_rule_1
    page_settings['custom_css'] = new_rule_1 + "\n\n" + current_custom_css
    print("Prepended Rule 1 to page_settings['custom_css']")

# 4. Save to WordPress REST API
payload = {
    'meta': {
        '_elementor_data': json.dumps(el_data),
        '_elementor_page_settings': page_settings
    }
}

req_update = urllib.request.Request(
    'https://eatgopty.com/wp-json/wp/v2/elementor_library/677',
    headers={
        'Authorization': auth,
        'Content-Type': 'application/json'
    },
    data=json.dumps(payload).encode('utf-8')
)

with urllib.request.urlopen(req_update) as resp:
    print('Header 677 updated successfully! HTTP Code:', resp.getcode())

# 5. Flush Elementor Cache
try:
    del_req = urllib.request.Request(
        'https://eatgopty.com/wp-json/elementor/v1/cache',
        headers={'Authorization': auth},
        method='DELETE'
    )
    with urllib.request.urlopen(del_req) as resp:
        print('Elementor cache cleared! HTTP Code:', resp.getcode())
except Exception as e:
    print('Elementor cache clear notice:', e)
