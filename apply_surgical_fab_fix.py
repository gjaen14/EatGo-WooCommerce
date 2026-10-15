import urllib.request
import json
import base64

auth = base64.b64encode(b'JaenDev:4n3FKy26SkBpwe8GPBzdbqEz').decode('utf-8')
headers = {
    'Authorization': f'Basic {auth}',
    'Content-Type': 'application/json'
}

# 1. Fetch live snippet 477
req = urllib.request.Request('https://eatgopty.com/wp-json/wp/v2/elementor_snippet/477?context=edit', headers=headers)
with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode('utf-8'))
    content = data.get('meta', {}).get('_elementor_code', '')

# Backup current before modifying
with open('snippet_477_backup_before_fab_fix.txt', 'w', encoding='utf-8') as f:
    f.write(content)
print(f"Backed up live snippet 477 ({len(content)} chars).")

# 1. Update FAB markup to javascript:void(0);
old_markup = '<a href="#comanda" class="eatgo-fab-cart" role="button" aria-label="Ver Resumen de Pedido">'
new_markup = '<a href="javascript:void(0);" class="eatgo-fab-cart" role="button" aria-label="Ver Resumen de Pedido">'
if old_markup in content:
    content = content.replace(old_markup, new_markup)
    print("Replaced FAB markup to href='javascript:void(0);'.")
else:
    print("WARNING: old_markup not found.")

# 2. Add sanitization in renderEatGoFabCart
target_render = "$fab = $('.eatgo-fab-cart');\n    }\n\n    var cart = (typeof getCartData"
sanitization_code = """$fab = $('.eatgo-fab-cart');
    }

    // Sanitización activa contra atributos y clases nativas de compra de WooCommerce
    $fab.attr('href', 'javascript:void(0);')
        .removeAttr('data-product_id data-product-id data-quantity')
        .removeClass('ajax_add_to_cart add_to_cart_button product_type_simple');

    var cart = (typeof getCartData"""

if target_render in content:
    content = content.replace(target_render, sanitization_code)
    print("Added sanitization in renderEatGoFabCart.")
else:
    print("WARNING: target_render not found.")

# 3. Stop immediate propagation and isolate click event
old_click = """  $(document).on('click', '.eatgo-fab-cart, .eatgo-fab-cart *', function(e) {
    e.preventDefault();
    openSideComandaDrawer();
  });"""

new_click = """  $(document).on('click', '.eatgo-fab-cart, .eatgo-fab-cart *', function(e) {
    e.preventDefault();
    e.stopPropagation();
    e.stopImmediatePropagation();
    openSideComandaDrawer();
    return false;
  });"""

if old_click in content:
    content = content.replace(old_click, new_click)
    print("Updated FAB click event to preventDefault + stopPropagation + stopImmediatePropagation.")
else:
    print("WARNING: old_click not found.")

# 4. Synchronize data-qty attribute on existing cards
old_sync = """        if (matchingItem) {
          $item.find('.eg-qty-val').text(matchingItem.qty);
          $item.find('.eg-card-price').text('$' + matchingItem.total.toFixed(2));
        }"""

new_sync = """        if (!matchingItem && $item.find('.eg-card-title').length) {
          var itemTitle = $item.find('.eg-card-title').text().trim();
          matchingItem = cart.items.find(function(it) { return it.name === itemTitle; });
        }
        if (matchingItem) {
          $item.find('.eg-qty-val').text(matchingItem.qty);
          $item.find('.eg-qty-selector').attr('data-qty', matchingItem.qty);
          $item.find('.eg-card-price').text('$' + matchingItem.total.toFixed(2));
        }"""

if old_sync in content:
    content = content.replace(old_sync, new_sync)
    print("Updated card quantity synchronization.")
else:
    print("WARNING: old_sync not found.")

# 5. Push update to WordPress GoDaddy
payload = json.dumps({
    'meta': {
        '_elementor_code': content
    }
}).encode('utf-8')

update_req = urllib.request.Request(
    'https://eatgopty.com/wp-json/wp/v2/elementor_snippet/477',
    data=payload,
    headers=headers,
    method='POST'
)

with urllib.request.urlopen(update_req) as resp:
    result = json.loads(resp.read().decode('utf-8'))
    print("Successfully updated Snippet 477! Status:", resp.status)
