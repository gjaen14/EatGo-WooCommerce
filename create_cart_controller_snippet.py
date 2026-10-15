import urllib.request
import json
import base64

auth = 'Basic ' + base64.b64encode(b'JaenDev:4n3FKy26SkBpwe8GPBzdbqEz').decode()

php_code = """
add_action('wp_ajax_eatgo_cart_update_qty', 'eatgo_cart_update_qty_handler');
add_action('wp_ajax_nopriv_eatgo_cart_update_qty', 'eatgo_cart_update_qty_handler');
function eatgo_cart_update_qty_handler() {
    $cart_item_key = sanitize_text_field($_POST['cart_item_key'] ?? '');
    $qty = intval($_POST['quantity'] ?? 0);
    if ($cart_item_key && function_exists('WC') && WC()->cart) {
        if ($qty <= 0) {
            WC()->cart->remove_cart_item($cart_item_key);
        } else {
            WC()->cart->set_quantity($cart_item_key, $qty, true);
        }
        WC_AJAX::get_refreshed_fragments();
    }
    wp_die();
}

add_action('wp_ajax_eatgo_cart_clear', 'eatgo_cart_clear_handler');
add_action('wp_ajax_nopriv_eatgo_cart_clear', 'eatgo_cart_clear_handler');
function eatgo_cart_clear_handler() {
    if (function_exists('WC') && WC()->cart) {
        WC()->cart->empty_cart();
        WC_AJAX::get_refreshed_fragments();
    }
    wp_die();
}
"""

payload = {
    'name': 'EatGo Comanda Digital Cart Controller',
    'desc': 'Endpoints AJAX para actualizar cantidad y vaciar carrito en la Comanda Digital.',
    'code': php_code.strip(),
    'scope': 'global',
    'active': True,
    'priority': 5
}

req = urllib.request.Request(
    'https://eatgopty.com/wp-json/code-snippets/v1/snippets',
    headers={'Authorization': auth, 'Content-Type': 'application/json'},
    data=json.dumps(payload).encode('utf-8')
)

try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        print('Created snippet HTTP:', resp.getcode())
        data = json.load(resp)
        print('Snippet ID:', data.get('id'), 'Active:', data.get('active'))
except Exception as e:
    print('Error:', e)
