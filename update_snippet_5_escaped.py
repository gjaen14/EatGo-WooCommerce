import urllib.request, json, base64

auth = base64.b64encode(b'JaenDev:4n3FKy26SkBpwe8GPBzdbqEz').decode('utf-8')
req = urllib.request.Request('https://eatgopty.com/wp-json/code-snippets/v1/snippets/5', headers={'Authorization': f'Basic {auth}'})
with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode('utf-8'))
    code = data.get('code', '')

idx = code.find("add_action('wp_head'")
if idx != -1:
    code = code[:idx].strip()

# Notice: In Python, raw string r''' ''' protects backslashes and quotes
hook_code = r'''

add_action('wp_head', function() {
    $css = '<style id="eatgo-cards-modal-final-fix">' .
           '.woosq-product .product_title, .woosq-product h1.product_title, .woosq-product h1.entry-title, .woosq-popup .product_title, .woosq-popup h1 { display: block !important; visibility: visible !important; opacity: 1 !important; font-family: "Open Sans", sans-serif !important; font-weight: 800 !important; font-size: 22px !important; color: #18181B !important; line-height: 1.25 !important; margin-bottom: 8px !important; }' .
           '.elementor-element-3d4e5f2::before, .elementor-element-3d4e5f2::after, .elementor-element-3d4e5f2 .eg-badge-tag::before, .elementor-element-3d4e5f2 .eg-badge-tag::after { display: none !important; content: none !important; }' .
           '.elementor-element-3d4e5f2 { background-color: rgba(24, 24, 27, 0.85) !important; border: 1px solid rgba(234, 179, 8, 0.5) !important; border-radius: 50px !important; padding: 6px 14px !important; display: inline-flex !important; align-items: center !important; justify-content: center !important; }' .
           '.elementor-element-3d4e5f2 p, .elementor-element-3d4e5f2 .eg-badge-tag { margin: 0 !important; padding: 0 !important; font-family: "Open Sans", sans-serif !important; font-size: 11px !important; font-weight: 800 !important; letter-spacing: 0.5px !important; color: #FACC15 !important; line-height: 1 !important; text-transform: uppercase !important; display: inline-block !important; }' .
           '.elementor-element-8c9d0e7 .eg-garnish-label, .elementor-element-8c9d0e7::before, .elementor-element-8c9d0e7::after { display: none !important; content: none !important; }' .
           '.elementor-element-w_garnish_text { font-family: "Open Sans", sans-serif !important; font-size: 13px !important; font-weight: 500 !important; color: #D4D4D8 !important; display: inline-block !important; margin-right: auto !important; line-height: 1.2 !important; white-space: nowrap !important; text-shadow: 0 1px 2px rgba(0, 0, 0, 0.8) !important; }' .
           '.elementor-element-9d0e1f8 a.elementor-button, .elementor-element-9d0e1f8 .elementor-button { display: inline-flex !important; align-items: center !important; justify-content: center !important; background-color: #FF5500 !important; color: #FFFFFF !important; border-radius: 50px !important; padding: 8px 18px !important; box-shadow: 0 4px 14px rgba(255, 85, 0, 0.35) !important; transition: all 0.2s ease !important; }' .
           '.elementor-element-9d0e1f8 a.elementor-button:hover, .elementor-element-9d0e1f8 .elementor-button:hover { background-color: #E04B00 !important; transform: translateY(-2px) !important; box-shadow: 0 6px 18px rgba(255, 85, 0, 0.45) !important; }' .
           '</style>';

    $js = '<script>' .
          'jQuery(function($) {' .
          '  function sanitizeEatGoCards() {' .
          '    $(".elementor-element-8c9d0e7 .eg-garnish-label").remove();' .
          '    $(".elementor-element-3d4e5f2").each(function() {' .
          '      var spans = $(this).find("span");' .
          '      if (spans.length > 1) { spans.slice(1).remove(); }' .
          '    });' .
          '  }' .
          '  sanitizeEatGoCards();' .
          '  setInterval(sanitizeEatGoCards, 60);' .
          '});' .
          '</script>';

    echo $css . "\n" . $js;
}, 1);
'''

code += hook_code

update_data = json.dumps({'code': code}).encode('utf-8')
req_up = urllib.request.Request('https://eatgopty.com/wp-json/code-snippets/v1/snippets/5', data=update_data, headers={'Authorization': f'Basic {auth}', 'Content-Type': 'application/json'}, method='POST')
with urllib.request.urlopen(req_up) as resp:
    print('Snippet 5 updated successfully with robust PHP variables!')

req_act = urllib.request.Request('https://eatgopty.com/wp-json/code-snippets/v1/snippets/5/activate', headers={'Authorization': f'Basic {auth}', 'Content-Type': 'application/json'}, method='POST')
with urllib.request.urlopen(req_act) as resp:
    print('Snippet 5 activated successfully! Status:', resp.status)
