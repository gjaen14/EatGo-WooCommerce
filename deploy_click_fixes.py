import urllib.request
import json
import base64

# 1. Fetch current snippet 477 directly from WordPress
username = 'JaenDev'
password = '4n3FKy26SkBpwe8GPBzdbqEz'
auth = 'Basic ' + base64.b64encode(f'{username}:{password}'.encode()).decode()

req = urllib.request.Request(
    'https://eatgopty.com/wp-json/wp/v2/elementor_snippet/477',
    headers={'Authorization': auth}
)
with urllib.request.urlopen(req) as resp:
    data = json.load(resp)
    code = data.get('meta', {}).get('_elementor_code', '')

with open('snippet_477_before_clicks_fix.txt', 'w', encoding='utf-8') as f:
    f.write(code)

print('Current code fetched, length:', len(code))

# 2. Update TAREA 2: FAB Click listener
old_fab_click = """  // Click en FAB para abrir Side Drawer
  $(document).on('click', '.eatgo-fab-cart', function(e) {
    e.preventDefault();
    var $toggle = $('#elementor-menu-cart__toggle_button');
    if ($toggle.length) {
      $toggle.trigger('click');
    }
    $('.elementor-menu-cart__container').addClass('elementor-menu-cart--shown').attr('aria-hidden', 'false');
    if (typeof renderComandaDigital === 'function') {
      renderComandaDigital();
    }
  });"""

new_fab_click = """  // Click en FAB para abrir Side Drawer (Robusto multi-selector & fallbacks)
  $(document).on('click', '.eatgo-fab-cart, .eatgo-fab-cart *', function(e) {
    e.preventDefault();
    if ($('.woofc-cart-toggle').length) {
      $('.woofc-cart-toggle').trigger('click');
    } else if (typeof xoo_wsc_cart !== 'undefined') {
      xoo_wsc_cart.open();
    } else if ($('#elementor-menu-cart__toggle_button, .elementor-menu-cart__toggle').length) {
      var $toggle = $('#elementor-menu-cart__toggle_button');
      if ($toggle.length) {
        $toggle.trigger('click');
      } else {
        $('.elementor-menu-cart__toggle').first().trigger('click');
      }
      $('.elementor-menu-cart__container').addClass('elementor-menu-cart--shown').attr('aria-hidden', 'false');
      if (typeof renderComandaDigital === 'function') {
        renderComandaDigital();
      }
    } else if (window.elementorProFrontend && elementorProFrontend.modules && elementorProFrontend.modules.popup) {
      elementorProFrontend.modules.popup.showPopup({ id: 326 });
    }
  });"""

if old_fab_click in code:
    code = code.replace(old_fab_click, new_fab_click, 1)
    print("Replaced FAB click handler successfully")
else:
    # Try finding $(document).on('click', '.eatgo-fab-cart'
    target = "$(document).on('click', '.eatgo-fab-cart'"
    idx = code.find(target)
    if idx != -1:
        end_idx = code.find("});", idx) + 3
        code = code[:idx] + new_fab_click + code[end_idx:]
        print("Replaced FAB click handler by position successfully")
    else:
        print("Warning: FAB click target not found")

# 3. Update TAREA 1: Card button "+ Agregar al Pedido" opens Quick View modal
card_sync_and_click = """
  // ========================================================
  // TAREA 1: VINCULACIÓN MODAL DE PRODUCTO (WPC QUICK VIEW)
  // ========================================================
  function syncCardQuickViewButtons() {
    $('.e-loop-item, [class*="post-"]').each(function() {
      var $item = $(this);
      var match = ($item.attr('class') || '').match(/post-(\\d+)/);
      if (match && match[1]) {
        var pid = match[1];
        var $btn = $item.find('a.elementor-button, .woosq-btn');
        $btn.each(function() {
          var $b = $(this);
          if (!$b.hasClass('woosq-btn')) {
            $b.addClass('woosq-btn');
          }
          if ($b.attr('data-id') !== pid) {
            $b.attr('data-id', pid);
          }
          if ($b.attr('href') !== '#') {
            $b.attr('href', '#');
          }
        });
      }
    });
  }

  // Delegación de clic robusta para tarjetas de productos
  $(document).on('click', '.woosq-btn, .woosq-btn *, a.elementor-button:has(.elementor-button-text:contains("Agregar al Pedido")), .elementor-button-text:contains("Agregar al Pedido")', function(e) {
    e.preventDefault();
    var $el = $(this);
    var $btn = $el.closest('a.elementor-button, .woosq-btn');
    var pid = $btn.attr('data-id');
    if (!pid || isNaN(pid)) {
      var $loopItem = $el.closest('[class*="post-"], .e-loop-item');
      var match = ($loopItem.attr('class') || '').match(/post-(\\d+)/);
      if (match && match[1]) pid = match[1];
    }
    if (pid) {
      $btn.attr('data-id', pid).addClass('woosq-btn').attr('href', '#');
      if (typeof woosq_open === 'function') {
        woosq_open(pid);
      }
    }
  });
"""

# Insert card_sync_and_click right after new_fab_click
if new_fab_click in code:
    code = code.replace(new_fab_click, new_fab_click + '\n' + card_sync_and_click, 1)
    print("Inserted card_sync_and_click after FAB click handler")
else:
    print("Warning: new_fab_click not in code")

# Ensure syncCardQuickViewButtons is called in document.ready and MutationObserver
target_ready = "renderEatGoFabCart();\n    renderComandaDigital();"
if target_ready in code:
    code = code.replace(target_ready, target_ready + "\n    syncCardQuickViewButtons();", 1)
    print("Added syncCardQuickViewButtons() to document.ready")

target_observer = "renderComandaDigital();\n    renderEatGoFabCart();\n  });"
if target_observer in code:
    code = code.replace(target_observer, "renderComandaDigital();\n    renderEatGoFabCart();\n    syncCardQuickViewButtons();\n  });", 1)
    print("Added syncCardQuickViewButtons() to MutationObserver")

# Also immediate execution before IIFE close
target_iife = "  // Invocacion inmediata de FAB Cart\n  renderEatGoFabCart();"
if target_iife in code:
    code = code.replace(target_iife, target_iife + "\n  syncCardQuickViewButtons();", 1)
    print("Added immediate syncCardQuickViewButtons() before IIFE close")

# 4. Save and deploy snippet 477 to WordPress
with open('snippet_477_clicks_fixed.txt', 'w', encoding='utf-8') as f:
    f.write(code)

payload = {
    'title': 'EatGo Comanda Digital WhatsApp Drawer & FAB Cart',
    'status': 'publish',
    'meta': {
        '_elementor_code': code.strip(),
        '_elementor_location': 'elementor_body_end',
        '_elementor_priority': 1,
        '_elementor_conditions': ['include/general']
    }
}

req_update = urllib.request.Request(
    'https://eatgopty.com/wp-json/wp/v2/elementor_snippet/477',
    headers={
        'Authorization': auth,
        'Content-Type': 'application/json'
    },
    data=json.dumps(payload).encode('utf-8')
)

try:
    with urllib.request.urlopen(req_update, timeout=15) as resp:
        print('Updated snippet HTTP:', resp.getcode())
        data = json.load(resp)
        print('Snippet ID:', data.get('id'), 'Status:', data.get('status'))
except Exception as e:
    print('Deploy error:', e)
