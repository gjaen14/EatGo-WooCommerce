import urllib.request, json, base64

username = 'JaenDev'
password = '4n3FKy26SkBpwe8GPBzdbqEz'
auth = 'Basic ' + base64.b64encode(f'{username}:{password}'.encode()).decode()

# 1. Fetch current Page 58
req = urllib.request.Request(
    'https://eatgopty.com/wp-json/wp/v2/pages/58?context=edit',
    headers={'Authorization': auth}
)
with urllib.request.urlopen(req) as resp:
    page = json.load(resp)

data = json.loads(page['meta']['_elementor_data'])

# Helper to find widget
def find_and_update(items):
    for it in items:
        if isinstance(it, dict):
            if it.get('id') == '3a9e80b':
                s = it.setdefault('settings', {})
                print("Found 3a9e80b! Previous query settings:")
                print("query_id:", s.get('query_id'), "product_taxonomy_posts_ids:", s.get('product_taxonomy_posts_ids'))
                
                # Assign unique query ID
                s['query_id'] = 'query_home_platos_hoy'
                s['post_query_query_id'] = 'query_home_platos_hoy'
                s['product_query_query_id'] = 'query_home_platos_hoy'
                s['_query_id'] = 'query_home_platos_hoy'
                
                # Make sure query source is product
                s['post_query_post_type'] = 'product'
                s['post_query_source'] = 'product'
                s['query_post_type'] = 'product'
                s['query_source'] = 'product'
                
                # Clear manual inclusion of all semana-1 dishes (term 21)
                s['product_taxonomy_query_filter_by'] = ''
                s['product_taxonomy_posts_ids'] = []
                
                # Ensure template 190 is preserved
                s['template_id'] = '190'
                print("Updated 3a9e80b with query_home_platos_hoy!")
                
            if it.get('id') == 'c01loop':
                s = it.setdefault('settings', {})
                print("Found c01loop! Updating query_id as well...")
                s['query_id'] = 'query_home_platos_hoy'
                s['post_query_query_id'] = 'query_home_platos_hoy'
                s['product_query_query_id'] = 'query_home_platos_hoy'
                s['_query_id'] = 'query_home_platos_hoy'
                s['post_query_post_type'] = 'product'
                s['post_query_source'] = 'product'
                s['query_post_type'] = 'product'
                s['query_source'] = 'product'
                
            if 'elements' in it:
                find_and_update(it['elements'])

find_and_update(data)

# 2. Save back to Page 58
payload = {
    'meta': {
        '_elementor_data': json.dumps(data)
    }
}

update_req = urllib.request.Request(
    'https://eatgopty.com/wp-json/wp/v2/pages/58',
    headers={'Authorization': auth, 'Content-Type': 'application/json'},
    data=json.dumps(payload).encode('utf-8')
)

with urllib.request.urlopen(update_req) as resp:
    res = json.load(resp)
    print("Page 58 successfully updated! Length:", len(res['meta']['_elementor_data']))
