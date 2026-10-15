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

inspect_code = """
    register_rest_route('eatgo/v1', '/inspect-doc-elements', [
        'methods' => 'GET',
        'callback' => function() {
            if (!class_exists('\\Elementor\\Plugin')) {
                return rest_ensure_response(['error' => 'no elementor']);
            }
            $doc = \\Elementor\\Plugin::$instance->documents->get(564);
            if (!$doc) {
                return rest_ensure_response(['error' => 'no doc']);
            }
            $data = $doc->get_elements_data();
            
            // Look at container 2 (Lunes)
            $top0 = $data[0]['elements'] ?? [];
            $c_lunes = $top0[2] ?? [];
            
            return rest_ensure_response([
                'doc_class' => get_class($doc),
                'top0_children_count' => count($top0),
                'lunes_id' => $c_lunes['id'] ?? null,
                'lunes_children' => $c_lunes['elements'] ?? []
            ]);
        },
        'permission_callback' => '__return_true'
    ]);
"""

if '/inspect-doc-elements' not in code:
    code = code.replace("register_rest_route('eatgo/v1', '/search-element'", inspect_code + "\n    register_rest_route('eatgo/v1', '/search-element'")
    snippet['code'] = code
    snippet['active'] = True

    update_req = urllib.request.Request(
        'https://eatgopty.com/wp-json/code-snippets/v1/snippets/5',
        headers={'Authorization': auth, 'Content-Type': 'application/json'},
        data=json.dumps(snippet).encode('utf-8')
    )
    with urllib.request.urlopen(update_req) as resp:
        print('Updated snippet 5 with inspect-doc-elements')

req_inspect = urllib.request.Request('https://eatgopty.com/wp-json/eatgo/v1/inspect-doc-elements')
with urllib.request.urlopen(req_inspect) as resp:
    data = json.load(resp)
    print('Inspect doc elements result:', json.dumps(data, indent=2))
