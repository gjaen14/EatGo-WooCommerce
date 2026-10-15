with open('snippet_477_perfect.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Ensure .elementor-widget-woocommerce-menu-cart is toggled when opening & closing drawer
old_drawer_open = """      $('.elementor-menu-cart__container').addClass('elementor-menu-cart--shown').attr('aria-hidden', 'false');"""
new_drawer_open = """      $('.elementor-widget-woocommerce-menu-cart').addClass('elementor-menu-cart--shown');
      $('.elementor-menu-cart__container').addClass('elementor-menu-cart--shown').attr('aria-hidden', 'false');"""

if old_drawer_open in content:
    content = content.replace(old_drawer_open, new_drawer_open)
    print("Updated drawer open with widget selector")

old_drawer_close = """    $('.elementor-menu-cart__container').removeClass('elementor-menu-cart--shown').attr('aria-hidden', 'true');"""
new_drawer_close = """    $('.elementor-widget-woocommerce-menu-cart, .elementor-menu-cart__container').removeClass('elementor-menu-cart--shown').attr('aria-hidden', 'true');"""

if old_drawer_close in content:
    content = content.replace(old_drawer_close, new_drawer_close)
    print("Updated drawer close with widget selector")

# 2. Ensure syncCardQuickViewButtons targets cards accurately
old_sync = """  function syncCardQuickViewButtons() {
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
  }"""

new_sync = """  function syncCardQuickViewButtons() {
    $('.e-loop-item.product, .e-loop-item[class*="post-"], .e-loop-item[class*="e-loop-item-"]').each(function() {
      var $card = $(this);
      var match = ($card.attr('class') || '').match(/\\bpost-(\\d+)\\b/);
      if (!match) {
        match = ($card.attr('class') || '').match(/\\be-loop-item-(\\d+)\\b/);
      }
      if (match && match[1]) {
        var pid = match[1];
        var $btn = $card.find('.elementor-element-w14btna a, a.woosq-btn, a.elementor-button:has(.elementor-button-text:contains("Agregar"))');
        $btn.addClass('woosq-btn').attr('data-id', pid).attr('href', '#');
      }
    });
  }"""

if old_sync in content:
    content = content.replace(old_sync, new_sync)
    print("Updated syncCardQuickViewButtons targeting")

with open('snippet_477_perfect.txt', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated snippet_477_perfect.txt successfully")
