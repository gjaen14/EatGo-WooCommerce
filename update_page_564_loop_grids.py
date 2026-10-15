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

data = json.loads(page['meta']['_elementor_data'])

dias_info = [
    ('lunes', '12dc898b', 2),
    ('martes', '4bf72f7d', 3),
    ('miercoles', '5bfd1736', 4),
    ('jueves', '2fd6c6a9', 5),
    ('viernes', '62f9bc94', 6),
    ('sabado', '74741324', 7),
]

top0_elements = data[0]['elements']

for dia, cid, idx in dias_info:
    container = top0_elements[idx]
    assert container['id'] == cid, f"Container ID mismatch: {container['id']} != {cid}"
    
    print(f"Updating {dia} (ID: {cid}). Previous children: {len(container.get('elements', []))}")
    
    # Configure Loop Grid widget
    loop_widget = {
        'id': f'lg_{dia[:3]}',
        'elType': 'widget',
        'widgetType': 'loop-grid',
        'settings': {
            'template_id': 631,
            'columns': 3,
            'columns_tablet': 2,
            'columns_mobile': 1,
            'posts_per_page': 12,
            'post_query_post_type': 'product',
            'post_query_source': 'product',
            'query_post_type': 'product',
            'query_source': 'product',
            'query_id': f'query_menu_{dia}',
            'post_query_query_id': f'query_menu_{dia}',
            '_query_id': f'query_menu_{dia}',
            'pagination_type': 'none'
        },
        'elements': []
    }
    
    # Replace all manual children with the single Loop Grid widget
    container['elements'] = [loop_widget]

# 2. Save back to WordPress
payload = {
    'meta': {
        '_elementor_data': json.dumps(data)
    }
}

update_req = urllib.request.Request(
    'https://eatgopty.com/wp-json/wp/v2/pages/564',
    headers={
        'Authorization': auth,
        'Content-Type': 'application/json'
    },
    data=json.dumps(payload).encode('utf-8')
)

with urllib.request.urlopen(update_req) as resp:
    res = json.load(resp)
    print('Page 564 successfully updated with Loop Grids!')
    print('New _elementor_data length:', len(res['meta']['_elementor_data']))
