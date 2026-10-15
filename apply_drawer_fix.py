with open('snippet_477_perfect.txt', 'r', encoding='utf-8') as f:
    css_js = f.read()

# 1. Update the toggle CSS to standard screen-reader hide without pointer-events: none
old_toggle_css = """.elementor-menu-cart__toggle,
#elementor-menu-cart__toggle_button,
.elementor-menu-cart__toggle_button {
  position: absolute !important;
  opacity: 0 !important;
  pointer-events: none !important;
  width: 1px !important;
  height: 1px !important;
  clip: rect(0, 0, 0, 0) !important;
}"""

new_toggle_css = """.elementor-menu-cart__toggle,
#elementor-menu-cart__toggle_button,
.elementor-menu-cart__toggle_button {
  position: absolute !important;
  opacity: 0 !important;
  width: 1px !important;
  height: 1px !important;
  margin: -1px !important;
  padding: 0 !important;
  border: 0 !important;
  clip: rect(0, 0, 0, 0) !important;
  overflow: hidden !important;
}

/* Forzar despliegue garantizado del Side-Drawer cuando está activo */
.elementor-menu-cart--shown .elementor-menu-cart__container,
.elementor-widget-woocommerce-menu-cart.elementor-menu-cart--shown .elementor-menu-cart__container {
  transform: scale(1) !important;
  background-color: rgba(0, 0, 0, 0.45) !important;
  opacity: 1 !important;
  pointer-events: auto !important;
}

.elementor-menu-cart--shown .elementor-menu-cart__main,
.elementor-widget-woocommerce-menu-cart.elementor-menu-cart--shown .elementor-menu-cart__main {
  transform: translateX(0) !important;
  opacity: 1 !important;
  pointer-events: auto !important;
}"""

if old_toggle_css in css_js:
    css_js = css_js.replace(old_toggle_css, new_toggle_css)
    print("Updated toggle CSS and added robust shown styles")
else:
    print("Warning: old_toggle_css not found")

# 2. Update FAB click handler and close handler
old_fab_block = """  // Click en FAB para abrir Side Drawer (Robusto multi-selector & fallbacks)
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
      $('.elementor-widget-woocommerce-menu-cart').addClass('elementor-menu-cart--shown');
      $('.elementor-menu-cart__container').addClass('elementor-menu-cart--shown').attr('aria-hidden', 'false');
      if (typeof renderComandaDigital === 'function') {
        renderComandaDigital();
      }
    } else if (window.elementorProFrontend && elementorProFrontend.modules && elementorProFrontend.modules.popup) {
      elementorProFrontend.modules.popup.showPopup({ id: 326 });
    }
  });"""

new_fab_block = """  // Función universal para desplegar el Side Drawer de la comanda
  function openSideComandaDrawer() {
    if ($('.woofc-cart-toggle').length) {
      $('.woofc-cart-toggle').trigger('click');
    } else if (typeof xoo_wsc_cart !== 'undefined') {
      xoo_wsc_cart.open();
    } else if ($('.elementor-menu-cart__toggle, #elementor-menu-cart__toggle_button').length) {
      $('.elementor-menu-cart__toggle, #elementor-menu-cart__toggle_button').first().trigger('click');
      $('.elementor-widget-woocommerce-menu-cart, .elementor-menu-cart__container').addClass('elementor-menu-cart--shown').attr('aria-hidden', 'false');
      if (typeof renderComandaDigital === 'function') {
        renderComandaDigital();
      }
    } else if (window.elementorProFrontend && elementorProFrontend.modules && elementorProFrontend.modules.popup) {
      elementorProFrontend.modules.popup.showPopup({ id: 326 });
    }
  }

  // Click en FAB para abrir Side Drawer
  $(document).on('click', '.eatgo-fab-cart, .eatgo-fab-cart *', function(e) {
    e.preventDefault();
    openSideComandaDrawer();
  });"""

if old_fab_block in css_js:
    css_js = css_js.replace(old_fab_block, new_fab_block)
    print("Updated FAB click handler")
else:
    print("Warning: old_fab_block not found")

with open('snippet_477_perfect.txt', 'w', encoding='utf-8') as f:
    f.write(css_js)
print("Finished updating snippet_477_perfect.txt")
