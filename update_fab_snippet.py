import urllib.request
import json
import base64

username = 'JaenDev'
password = '4n3FKy26SkBpwe8GPBzdbqEz'
auth = 'Basic ' + base64.b64encode(f'{username}:{password}'.encode()).decode()

with open('snippet_477_current.txt', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Añadir CSS para ocultar el toggle superior y posicionar/animar el FAB Cart
fab_css = """
/* Ocultar el botón toggle rígido superior del Header */
.elementor-menu-cart__toggle {
  display: none !important;
}

/* Asegurar que el Side Drawer quede siempre por encima del FAB */
.elementor-menu-cart__container {
  z-index: 999999 !important;
}

/* ========================================================
   EAT&GO: BOTÓN FLOTANTE INFERIOR DERECHO (FAB CART)
   ======================================================== */
.eatgo-fab-cart {
  position: fixed !important;
  bottom: 24px !important;
  right: 24px !important;
  z-index: 99998 !important;
  background-color: #c81c20 !important;
  color: #FFFFFF !important;
  border-radius: 50px !important;
  padding: 10px 18px !important;
  display: flex !important;
  align-items: center !important;
  gap: 8px !important;
  box-shadow: 0 8px 24px rgba(200, 28, 32, 0.45) !important;
  cursor: pointer !important;
  text-decoration: none !important;
  transition: background-color 0.2s ease, transform 0.2s ease, box-shadow 0.2s ease !important;
  animation: fab-radar-pulse 2s infinite !important;
  user-select: none !important;
  font-family: 'Open Sans', -apple-system, BlinkMacSystemFont, sans-serif !important;
}

.eatgo-fab-cart:hover {
  background-color: #a81518 !important;
  transform: translateY(-2px) !important;
  color: #FFFFFF !important;
  text-decoration: none !important;
}

.eatgo-fab-cart:active {
  transform: scale(0.97) !important;
}

.eatgo-fab-cart .eatgo-fab-icon {
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  line-height: 1 !important;
}

.eatgo-fab-cart .eatgo-fab-icon svg {
  display: block !important;
  width: 18px !important;
  height: 18px !important;
}

.eatgo-fab-cart .eatgo-fab-badge {
  background-color: #FFFFFF !important;
  color: #18181B !important;
  font-family: 'Open Sans', sans-serif !important;
  font-size: 12px !important;
  font-weight: 800 !important;
  min-width: 22px !important;
  height: 22px !important;
  border-radius: 50px !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  padding: 0 5px !important;
  line-height: 1 !important;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.15) !important;
}

.eatgo-fab-cart .eatgo-fab-total {
  color: #FFFFFF !important;
  font-family: 'Open Sans', sans-serif !important;
  font-size: 14px !important;
  font-weight: 700 !important;
  letter-spacing: 0.2px !important;
  line-height: 1 !important;
  white-space: nowrap !important;
}

@keyframes fab-radar-pulse {
  0% {
    box-shadow: 0 0 0 0 rgba(200, 28, 32, 0.7), 0 8px 24px rgba(200, 28, 32, 0.4);
  }
  70% {
    box-shadow: 0 0 0 14px rgba(200, 28, 32, 0), 0 8px 24px rgba(200, 28, 32, 0.4);
  }
  100% {
    box-shadow: 0 0 0 0 rgba(200, 28, 32, 0), 0 8px 24px rgba(200, 28, 32, 0.4);
  }
}
"""

# Insertar CSS antes de </style>
if '</style>' in code:
    code = code.replace('</style>', fab_css + '\n</style>', 1)
else:
    print('Error: </style> not found')

# 2. Insertar JS para FAB
fab_js = """
  // ========================================================
  // BOTÓN FLOTANTE INFERIOR DERECHO (FAB - EAT&GO)
  // ========================================================
  function renderEatGoFabCart() {
    var $fab = $('.eatgo-fab-cart');
    if (!$fab.length) {
      var fabHtml = [
        '<a href="#comanda" class="eatgo-fab-cart" role="button" aria-label="Ver Comanda y Carrito">',
          '<span class="eatgo-fab-icon">',
            '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round">',
              '<path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"></path>',
              '<line x1="3" y1="6" x2="21" y2="6"></line>',
              '<path d="M16 10a4 4 0 0 1-8 0"></path>',
            '</svg>',
          '</span>',
          '<span class="eatgo-fab-badge">0</span>',
          '<span class="eatgo-fab-total">$0.00</span>',
        '</a>'
      ].join('');
      $('body').append(fabHtml);
      $fab = $('.eatgo-fab-cart');
    }

    var cart = (typeof getCartData === 'function') ? getCartData() : { count: 0, subtotal: 0 };
    var count = cart.count;
    var totalStr = '$' + (cart.subtotal || 0).toFixed(2);

    if (count === 0) {
      var elemQty = parseInt($('.elementor-button-icon-qty').attr('data-counter') || $('.elementor-button-icon-qty').text() || '0', 10);
      var elemAmount = $('.elementor-button-text .woocommerce-Price-amount').first().text().trim();
      if (elemQty > 0) {
        count = elemQty;
      }
      if (elemAmount) {
        totalStr = elemAmount;
      }
    }

    var $badge = $fab.find('.eatgo-fab-badge');
    var $total = $fab.find('.eatgo-fab-total');

    if ($badge.text() !== String(count)) {
      $badge.text(count);
    }
    if ($total.text() !== totalStr) {
      $total.text(totalStr);
    }
  }

  // Click en FAB para abrir Side Drawer
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
  });
"""

# Insertar fab_js antes de // EVENTOS INTERACTIVOS
target_marker = '  // EVENTOS INTERACTIVOS'
if target_marker in code:
    code = code.replace(target_marker, fab_js + '\n' + target_marker, 1)
else:
    print('Warning: EVENTOS INTERACTIVOS not found, inserting before </script>')
    code = code.replace('</script>', fab_js + '\n</script>', 1)

# Asegurar que renderEatGoFabCart se llame al final de renderComandaDigital
if '    renderEatGoFabCart();' not in code:
    marker_mode = "$comandaBody.find('.eg-inp-oficina').attr('placeholder', 'Ej: Piso 14, Of. 1402').prop('disabled', false).css('opacity', '1');\n    }"
    if marker_mode in code:
        code = code.replace(marker_mode, marker_mode + '\n    renderEatGoFabCart();', 1)
    else:
        print('Warning: marker_mode not found')

# Asegurar llamadas en document.ready y eventos
if 'renderEatGoFabCart();' in code:
    code = code.replace('renderComandaDigital();\n  });', 'renderComandaDigital();\n    renderEatGoFabCart();\n  });', 1)
    code = code.replace('setTimeout(renderComandaDigital, 40);', 'setTimeout(function() { renderComandaDigital(); renderEatGoFabCart(); }, 40);', 1)
    code = code.replace('var observer = new MutationObserver(function() {\n    renderComandaDigital();\n  });', 'var observer = new MutationObserver(function() {\n    renderComandaDigital();\n    renderEatGoFabCart();\n  });', 1)

with open('snippet_477_updated_with_fab.txt', 'w', encoding='utf-8') as f:
    f.write(code)

print('Updated length:', len(code))

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

req = urllib.request.Request(
    'https://eatgopty.com/wp-json/wp/v2/elementor_snippet/477',
    headers={
        'Authorization': auth,
        'Content-Type': 'application/json'
    },
    data=json.dumps(payload).encode('utf-8')
)

try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        print('Updated snippet HTTP:', resp.getcode())
        data = json.load(resp)
        print('Snippet ID:', data.get('id'), 'Status:', data.get('status'))
except urllib.error.HTTPError as e:
    print('HTTPError:', e.code, e.read().decode('utf-8'))
except Exception as e:
    print('Exception:', e)
