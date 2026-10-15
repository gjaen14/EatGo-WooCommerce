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

find_files = """
    register_rest_route('eatgo/v1', '/find-files', [
        'methods' => 'GET',
        'callback' => function() {
            $uploads = wp_upload_dir();
            $base = $uploads['basedir'];
            $cmd = "grep -rn '5c1c1deb' " . escapeshellarg($base);
            $output = @shell_exec($cmd);
            return rest_ensure_response([
                'uploads_grep' => $output ? substr($output, 0, 1000) : 'none',
                'basedir' => $base
            ]);
        },
        'permission_callback' => '__return_true'
    ]);
"""

if '/find-files' not in code:
    code = code.replace("register_rest_route('eatgo/v1', '/search-element'", find_files + "\n    register_rest_route('eatgo/v1', '/search-element'")
    snippet['code'] = code
    snippet['active'] = True

    update_req = urllib.request.Request(
        'https://eatgopty.com/wp-json/code-snippets/v1/snippets/5',
        headers={'Authorization': auth, 'Content-Type': 'application/json'},
        data=json.dumps(snippet).encode('utf-8')
    )
    with urllib.request.urlopen(update_req) as resp:
        print('Updated snippet 5 with find-files')

req_files = urllib.request.Request('https://eatgopty.com/wp-json/eatgo/v1/find-files')
with urllib.request.urlopen(req_files) as resp:
    print('Find-files result:', json.dumps(json.load(resp), indent=2))
