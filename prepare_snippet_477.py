import json

with open('snippet_477_current_downloaded.txt', 'r', encoding='utf-8') as f:
    current = f.read()

# 1. Update CSS to keep header toggle clickable while off-screen / invisible
old_css_toggle = """.elementor-menu-cart__toggle,
#elementor-menu-cart__toggle_button,
.elementor-menu-cart__toggle_button {
  display: none !important;
}"""

new_css_toggle = """.elementor-menu-cart__toggle,
#elementor-menu-cart__toggle_button,
.elementor-menu-cart__toggle_button {
  position: absolute !important;
  opacity: 0 !important;
  pointer-events: none !important;
  width: 1px !important;
  height: 1px !important;
  clip: rect(0, 0, 0, 0) !important;
}"""

if old_css_toggle in current:
    current = current.replace(old_css_toggle, new_css_toggle)
    print("Replaced toggle CSS successfully")
else:
    print("Warning: old_css_toggle not found exactly")

# 2. Update FAB click handler
old_fab_click = """  // Click en FAB para abrir Side Drawer (Robusto multi-selector & fallbacks)
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

new_fab_click = """  // Click en FAB para abrir Side Drawer (Robusto multi-selector & fallbacks)
  $(document).on('click', '.eatgo-fab-cart, .eatgo-fab-cart *', function(e) {
    e.preventDefault();
    if ($('.woofc-cart-toggle').length) {
      $('.woofc-cart-toggle').trigger('click');
    } else if (typeof xoo_wsc_cart !== 'undefined') {
      xoo_wsc_cart.open();
    } else if ($('.elementor-menu-cart__toggle, #elementor-menu-cart__toggle_button').length) {
      var $toggle = $('#elementor-menu-cart__toggle_button');
      if ($toggle.length && $toggle[0]) {
        $toggle[0].click();
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

if old_fab_click in current:
    current = current.replace(old_fab_click, new_fab_click)
    print("Replaced FAB click handler successfully")
else:
    print("Warning: old_fab_click not found exactly")

# 3. Update syncCardQuickViewButtons & card click handler
old_quickview_sync = """  // ========================================================
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
  });"""

new_quickview_sync = """  // ========================================================
  // TAREA 1: VINCULACIÓN MODAL DE PRODUCTO (WPC QUICK VIEW)
  // ========================================================
  function syncCardQuickViewButtons() {
    $('.e-loop-item, [class*="post-"]').each(function() {
      var $item = $(this);
      var match = ($item.attr('class') || '').match(/(?:post-|e-loop-item-)(\\d+)/);
      if (match && match[1]) {
        var pid = match[1];
        var $btn = $item.find('.elementor-element-w14btna a, a.elementor-button:has(.elementor-button-text:contains("Agregar al Pedido"))');
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

  // Delegación de clic robusta para tarjetas de productos (Modal WPC Quick View)
  $(document).on('click', '.woosq-btn, .woosq-btn *, .elementor-element-w14btna a, .elementor-element-w14btna a *, a.elementor-button:has(.elementor-button-text:contains("Agregar")), .elementor-button-text:contains("Agregar")', function(e) {
    e.preventDefault();
    var $el = $(this);
    var $btn = $el.closest('a');
    var pid = $btn.attr('data-id');
    if (!pid || isNaN(pid)) {
      var $card = $el.closest('.e-loop-item, [class*="post-"]');
      var match = ($card.attr('class') || '').match(/(?:post-|e-loop-item-)(\\d+)/);
      if (match && match[1]) pid = match[1];
    }
    if (pid && !isNaN(pid)) {
      $btn.attr('data-id', pid).addClass('woosq-btn').attr('href', '#');
      if (typeof woosq_open === 'function') {
        woosq_open(pid);
      } else {
        $(document.body).trigger('woosq_open', [pid]);
      }
    }
  });"""

if old_quickview_sync in current:
    current = current.replace(old_quickview_sync, new_quickview_sync)
    print("Replaced quickview sync and handler successfully")
else:
    print("Warning: old_quickview_sync not found exactly")

with open('snippet_477_perfect.txt', 'w', encoding='utf-8') as f:
    f.write(current)
print("Saved snippet_477_perfect.txt, length:", len(current))
