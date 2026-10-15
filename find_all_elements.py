import urllib.request
import json
import base64

username = 'JaenDev'
password = '4n3FKy26SkBpwe8GPBzdbqEz'
auth = 'Basic ' + base64.b64encode(f'{username}:{password}'.encode()).decode()

req = urllib.request.Request(
    'https://eatgopty.com/wp-json/code-snippets/v1/snippets/5',
    headers={'Authorization': auth}
)
with urllib.request.urlopen(req) as resp:
    snippet = json.load(resp)

code = snippet['code']

# Search across tables
find_code = """
    register_rest_route('eatgo/v1', '/find-all', [
        'methods' => 'GET',
        'callback' => function() {
            global $wpdb;
            $res = [];
            
            $opts = $wpdb->get_results("SELECT option_name, length(option_value) as len FROM {$wpdb->options} WHERE option_value LIKE '%5c1c1deb%'");
            $res['options'] = $opts;

            $posts = $wpdb->get_results("SELECT ID, post_title, post_type FROM {$wpdb->posts} WHERE post_content LIKE '%5c1c1deb%'");
            $res['posts'] = $posts;

            $meta = $wpdb->get_results("SELECT post_id, meta_key FROM {$wpdb->postmeta} WHERE meta_value LIKE '%5c1c1deb%'");
            $res['meta'] = $meta;

            return rest_ensure_response($res);
        },
        'permission_callback' => '__return_true'
    ]);
"""

if '/find-all' not in code:
    code = code.replace("register_rest_route('eatgo/v1', '/search-element'", find_code + "\n    register_rest_route('eatgo/v1', '/search-element'")
    snippet['code'] = code
    snippet['active'] = True

    update_req = urllib.request.Request(
        'https://eatgopty.com/wp-json/code-snippets/v1/snippets/5',
        headers={'Authorization': auth, 'Content-Type': 'application/json'},
        data=json.dumps(snippet).encode('utf-8')
    )
    with urllib.request.urlopen(update_req) as resp:
        print('Updated snippet 5 with find-all')

# Call find-all
req_find = urllib.request.Request('https://eatgopty.com/wp-json/eatgo/v1/find-all')
with urllib.request.urlopen(req_find) as resp:
    data = json.load(resp)
    print('Find-all results:', json.dumps(data, indent=2))
