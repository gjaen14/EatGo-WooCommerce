import urllib.request, json, base64

auth = base64.b64encode(b'JaenDev:4n3FKy26SkBpwe8GPBzdbqEz').decode('utf-8')
req = urllib.request.Request('https://eatgopty.com/wp-json/code-snippets/v1/snippets/5', headers={'Authorization': f'Basic {auth}'})
with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode('utf-8'))
    code = data.get('code', '')

regen_hook = r'''

add_action('init', function() {
    if (isset($_GET['eg_regen_css']) && $_GET['eg_regen_css'] === '1') {
        if (class_exists('\\Elementor\\Plugin')) {
            \Elementor\Plugin::$instance->files_manager->clear_cache();
            $css_file = new \Elementor\Core\Files\CSS\Post(58);
            $css_file->update();
            echo 'CSS regenerated for 58!';
            exit;
        }
    }
});
'''

code += regen_hook

update_data = json.dumps({'code': code}).encode('utf-8')
req_up = urllib.request.Request('https://eatgopty.com/wp-json/code-snippets/v1/snippets/5', data=update_data, headers={'Authorization': f'Basic {auth}', 'Content-Type': 'application/json'}, method='POST')
with urllib.request.urlopen(req_up) as resp:
    print('Added CSS regenerator to snippet 5!')
