import urllib.request
import json
import base64

username = 'JaenDev'
password = '4n3FKy26SkBpwe8GPBzdbqEz'
auth = 'Basic ' + base64.b64encode(f'{username}:{password}'.encode()).decode()

with open('current_menu_data.json') as f:
    menu_data = json.load(f)

menu_json_str = json.dumps(menu_data)

script_content = f"""<style>
/* ========================================================
   EAT&GO: DISEÑO VISUAL OFICIAL (100% PRESERVADO)
   ======================================================== */

/* Píldoras de los Días */
.elementor-element-440f623b p,
.btn-dia-tab,
[class*="dia-tab"] {{
  cursor: pointer !important;
  transition: all 0.2s ease !important;
  border-radius: 50px !important;
  user-select: none !important;
}}

/* Ocultar badge de caja 75°C en todas las tarjetas */
[data-interaction-id*="bbox-"],
div[data-interaction-id="7a466aab"],
div[data-interaction-id="217a4710"],
div[data-interaction-id="25a756bf"],
div[data-interaction-id="12719368"],
div[data-interaction-id="44071ae2"],
div[data-interaction-id="250580c3"],
div[data-interaction-id="3fa9579f"],
div[data-interaction-id="a87b821"],
div[data-interaction-id="30d8f2ff"],
div[data-interaction-id="5a1b375c"],
div[data-interaction-id="6c6b207b"],
div[data-interaction-id="6baa9db1"],
div[data-interaction-id="45f48e79"],
div[data-interaction-id="2eae153b"],
div[data-interaction-id="5d978d53"],
.elementor-element-c06bgbtm {{
  display: none !important;
}}

/* Botón + Agregar al Pedido (Fiel a la captura oficial) */
.woosq-btn,
.elementor-button.woosq-btn,
p a:has(img[alt="bag"]),
[data-id="1193b42"] [class*="e-con"] [class*="e-con"] > p:last-child a,
[class*="btn-plato-"] a {{
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  width: 100% !important;
  height: 48px !important;
  background-color: #F59E0B !important;
  color: #000000 !important; /* TEXTO NEGRO OFICIAL */
  font-family: 'Open Sans', sans-serif !important;
  font-size: 14px !important;
  font-weight: 800 !important;
  text-decoration: none !important;
  border-radius: 50px !important; /* PÍLDORA 50PX */
  border: none !important;
  cursor: pointer !important;
  transition: all 0.2s ease !important;
  box-shadow: 0 4px 12px rgba(245, 158, 11, 0.28) !important;
  gap: 8px !important;
  box-sizing: border-box !important;
}}

.woosq-btn:hover,
.elementor-button.woosq-btn:hover,
.woosq-btn:hover, a[data-id]:hover {{
  background-color: #D97706 !important;
  color: #000000 !important;
  transform: translateY(-1px) !important;
  box-shadow: 0 6px 16px rgba(245, 158, 11, 0.38) !important;
}}

/* Icono bag.svg en el botón */
.woosq-btn img,
.woosq-btn svg,
a:contains("Agregar al Pedido") img {{
  width: 20px !important;
  height: 20px !important;
  stroke: #000000 !important;
  fill: none !important;
  display: inline-block !important;
  vertical-align: middle !important;
}}

/* Badge PLATO ESTRELLA (Superior Izquierda) */
[data-interaction-id*="bcat-plato-"],
[data-id="1193b42"] div:has(> img) > p:first-of-type {{
  position: absolute !important;
  top: 12px !important;
  left: 12px !important;
  display: inline-block !important;
  background: #18181B !important;
  color: #FACC15 !important;
  font-family: 'Open Sans', sans-serif !important;
  font-size: 10px !important;
  font-weight: 800 !important;
  letter-spacing: 0.5px !important;
  padding: 4px 10px !important;
  border-radius: 50px !important;
  text-transform: uppercase !important;
  margin: 0 !important;
  z-index: 5 !important;
}}

/* Badge PRECIO (Superior Derecha) */
[data-interaction-id*="bpr-plato-"],
[data-id="1193b42"] div:has(> img) > p:last-of-type {{
  position: absolute !important;
  top: 12px !important;
  right: 12px !important;
  display: inline-block !important;
  background: #FFFFFF !important;
  color: #18181B !important;
  font-family: 'Open Sans', sans-serif !important;
  font-size: 13px !important;
  font-weight: 800 !important;
  padding: 4px 12px !important;
  border-radius: 50px !important;
  box-shadow: 0 2px 4px rgba(0,0,0,0.12) !important;
  margin: 0 !important;
  z-index: 5 !important;
}}

/* Selector de Acompañamiento */
[data-interaction-id*="sbox-plato-"] span,
[data-id="1193b42"] span:contains("Arroz") {{
  display: flex !important;
  align-items: center !important;
  justify-content: space-between !important;
  background: #FFFFFF !important;
  border: 1px solid #E5E7EB !important;
  border-radius: 12px !important;
  padding: 9px 12px !important;
  font-family: 'Open Sans', sans-serif !important;
  font-size: 12px !important;
  font-weight: 600 !important;
  color: #18181B !important;
}}
</style>

<script>
jQuery(function($) {{
  if (!$('body').hasClass('page-id-564') && window.location.pathname.indexOf('menu-semanal') === -1) {{
    return;
  }}

  // 1. Datos iniciales sincronizados de WooCommerce
  var menuData = {menu_json_str};

  var diasInfo = {{
    'lunes': {{ nombre: 'LUNES', badge: '🥣 Día de Caldos Reconfortantes', sub: 'Arranca la semana laboral con energía criolla y guisos reconfortantes de olla honda.' }},
    'martes': {{ nombre: 'MARTES', badge: '🥘 Tradición y Estofados Campesinos', sub: 'Platos tradicionales guisados a fuego lento con el sazón del interior.' }},
    'miercoles': {{ nombre: 'MIÉRCOLES', badge: '🔥 Paila Criolla & Asados', sub: 'Mitad de semana con carnes al horno, lechona y cortes jugosos.' }},
    'jueves': {{ nombre: 'JUEVES', badge: '🍗 Costillas, Aves & Sabor Ahumado', sub: 'Especialidades ahumadas y pastas criollas con salsas espesas.' }},
    'viernes': {{ nombre: 'VIERNES', badge: '🐟 Mariscos & Sabor Caribeño', sub: 'Cierra la semana con pescado frito, mariscos y arroz con coco.' }},
    'sabado': {{ nombre: 'SÁBADO', badge: '👨‍👩‍👧‍👦 Paila Familiar & Fiestas Criollas', sub: 'Porciones familiares para compartir el fin de semana.' }}
  }};

  var diasSemana = ['domingo', 'lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado'];
  var fechaHoy = new Date();
  var diaNum = fechaHoy.getDay(); // 0 es Domingo, 1 es Lunes...

  // REGLA DE DOMINGO: Si hoy es domingo (cocina cerrada), activar LUNES por defecto para pedidos anticipados
  var diaActivo = (diaNum === 0) ? 'lunes' : diasSemana[diaNum];

  var pillMap = {{
    '302c53b1': 'lunes',
    '1366f201': 'martes',
    'db09404': 'miercoles',
    '10dfeecc': 'jueves',
    '258724b8': 'viernes',
    '38fd654a': 'sabado'
  }};

  var bagSvgHtml = '<img src="https://eatgopty.com/wp-content/uploads/2026/09/bag.svg" width="20" height="20" alt="bag" style="vertical-align: middle; stroke: #000000; fill: none; margin-right: 8px; display: inline-block;">';

  // 2. Función para poblar tarjetas con datos de platos
  function poblarGrillaPlatos(gridElement, platos) {{
    if (!platos || !platos.length) return;
    var $cards = gridElement.children();
    platos.slice(0, 3).forEach(function(p, idx) {{
      var $card = $cards.eq(idx);
      if (!$card.length) return;

      var $cover = $card.children().eq(0);
      var $body = $card.children().eq(1);

      // Imagen
      if (p.image_url) {{
        $cover.find('img').first().attr('src', p.image_url).removeAttr('srcset');
      }}

      // Badge PLATO ESTRELLA
      $cover.find('p').first().text('PLATO ESTRELLA');

      // Badge PRECIO
      if (p.price) {{
        $cover.find('p').eq(1).text(p.price);
      }}

      // Título
      if (p.name) {{
        $body.find('h4, h3').first().text(p.name);
      }}

      // Descripción
      if (p.description) {{
        $body.find('p').first().text(p.description);
      }}

      // Botón + Agregar al Pedido con icono y data-id
      var $btn = $body.find('a').last();
      $btn.addClass('woosq-btn')
          .attr('data-id', p.id || '420')
          .html(bagSvgHtml + '+ Agregar al Pedido');
    }});
  }}

  function actualizarTodasLasGrillas(data) {{
    if (!data || !data.dias) return;
    var semNum = data.semana_activa || '1';
    var $counter = $('.banner-dia-counter, [data-interaction-id="4a66aef8"], .banner-counter').first();
    if ($counter.length) {{
      $counter.text('🗓️ Semana ' + semNum + ' del Mes • 3 especialidades preparadas hoy');
    }}

    var gridMapping = {{
      'lunes': $('[data-interaction-id="69a6b14f"], .elementor-element-69a6b14f, [configuration-id="grid-lunes"]'),
      'martes': $('[data-interaction-id="5c59ff09"], .elementor-element-5c59ff09, [configuration-id="grid-martes"]'),
      'miercoles': $('[data-interaction-id="777795ed"], .elementor-element-777795ed, [configuration-id="grid-miercoles"]'),
      'jueves': $('[data-interaction-id="777c2879"], .elementor-element-777c2879, [configuration-id="grid-jueves"]'),
      'viernes': $('[data-interaction-id="5b7538c7"], .elementor-element-5b7538c7, [configuration-id="grid-viernes"]'),
      'sabado': $('[data-interaction-id="7ed1d723"], .elementor-element-7ed1d723, [configuration-id="grid-sabado"]')
    }};

    for (var d in data.dias) {{
      if (gridMapping[d] && data.dias[d].platos) {{
        poblarGrillaPlatos(gridMapping[d], data.dias[d].platos);
      }}
    }}
  }}

  // 3. Aplicar datos iniciales inmediatamente
  actualizarTodasLasGrillas(menuData);

  // 4. Función para cambiar de día (CERO RECARGA)
  function seleccionarDia(diaSlug) {{
    if (!diasInfo[diaSlug]) diaSlug = 'lunes';

    // A. Píldoras
    $('.btn-dia-tab, [class*="dia-tab"]').each(function() {{
      var target = $(this).attr('data-dia') || $(this).text().toLowerCase();
      if (target.indexOf(diaSlug) !== -1) {{
        $(this).addClass('is-active').css({{
          'background-color': '#F59E0B',
          'border-color': '#F59E0B',
          'color': '#18181B',
          'font-weight': '800'
        }});
      }} else {{
        $(this).removeClass('is-active').css({{
          'background-color': '#FFFFFF',
          'border': '1px solid #E5E7EB',
          'color': '#18181B',
          'font-weight': '600'
        }});
      }}
    }});

    for (var pid in pillMap) {{
      var $p = $('[data-interaction-id="' + pid + '"]');
      if (pillMap[pid] === diaSlug) {{
        $p.addClass('is-active').css({{
          'background-color': '#F59E0B',
          'border-color': '#F59E0B',
          'color': '#18181B',
          'font-weight': '800',
          'box-shadow': '0 2px 8px rgba(245,158,11,0.3)',
          'cursor': 'pointer'
        }});
        $p.find('*').css({{
          'color': '#18181B',
          'font-weight': '800'
        }});
      }} else {{
        $p.removeClass('is-active').css({{
          'background-color': '#FFFFFF',
          'border': '1px solid #E5E7EB',
          'color': '#18181B',
          'font-weight': '600',
          'box-shadow': 'none',
          'cursor': 'pointer'
        }});
        $p.find('*').css({{
          'color': '#18181B',
          'font-weight': '600'
        }});
      }}
    }}

    // B. Banner
    var info = diasInfo[diaSlug];
    var $title = $('.banner-dia-title, [data-interaction-id="7a072b70"] h3, [data-interaction-id="7a072b70"], .elementor-heading-title:contains("MENÚ DEL")').first();
    $title.text('MENÚ DEL ' + info.nombre);

    var $badge = $('.banner-dia-badge, [data-interaction-id="6ff39463"]').first();
    $badge.text(info.badge);

    var $sub = $('.banner-dia-sub, [data-interaction-id="4b3186ef"]').first();
    $sub.text(info.sub);

    // C. Grillas
    var gridMap = {{
      'lunes': $('[data-interaction-id="69a6b14f"], .elementor-element-69a6b14f, [configuration-id="grid-lunes"]'),
      'martes': $('[data-interaction-id="5c59ff09"], .elementor-element-5c59ff09, [configuration-id="grid-martes"]'),
      'miercoles': $('[data-interaction-id="777795ed"], .elementor-element-777795ed, [configuration-id="grid-miercoles"]'),
      'jueves': $('[data-interaction-id="777c2879"], .elementor-element-777c2879, [configuration-id="grid-jueves"]'),
      'viernes': $('[data-interaction-id="5b7538c7"], .elementor-element-5b7538c7, [configuration-id="grid-viernes"]'),
      'sabado': $('[data-interaction-id="7ed1d723"], .elementor-element-7ed1d723, [configuration-id="grid-sabado"]')
    }};

    for (var s in gridMap) {{
      if (s === diaSlug) {{
        gridMap[s].css('display', 'flex').hide().fadeIn(180);
      }} else {{
        gridMap[s].hide().css('display', 'none');
      }}
    }}
  }}

  // Ejecutar selección inicial (LUNES por regla de Domingo)
  seleccionarDia(diaActivo);

  // 5. Escuchar clics en los días (Cero recarga)
  $(document).on('click', '.btn-dia-tab, [class*="dia-tab"], .elementor-element-440f623b p, [data-interaction-id="302c53b1"], [data-interaction-id="1366f201"], [data-interaction-id="db09404"], [data-interaction-id="10dfeecc"], [data-interaction-id="258724b8"], [data-interaction-id="38fd654a"], a:contains("LUNES"), a:contains("MARTES"), a:contains("MIÉRCOLES"), a:contains("JUEVES"), a:contains("VIERNES"), a:contains("SÁBADO")', function(e) {{
    e.preventDefault();
    var iid = $(this).attr('data-interaction-id');
    if (iid && pillMap[iid]) {{
      seleccionarDia(pillMap[iid]);
      return;
    }}
    var txt = $(this).text().toLowerCase();
    for (var slug in diasInfo) {{
      if (txt.indexOf(slug) !== -1) {{
        seleccionarDia(slug);
        break;
      }}
    }}
  }});

  // 6. Conectar modales nativos QuickView (+ Agregar al Pedido)
  $(document).on('click', '.woosq-btn, a:contains("Agregar al Pedido")', function(e) {{
    e.preventDefault();
    e.stopPropagation();
    var pid = $(this).attr('data-id') || $(this).attr('data-product_id');
    if (pid && typeof woosq_open === 'function') {{
      woosq_open(pid);
    }}
  }});

  // 7. Sincronización en segundo plano con la API de WordPress
  $.ajax({{
    url: '/wp-json/eatgo/v1/menu-semanal',
    method: 'GET',
    dataType: 'json',
    success: function(res) {{
      if (res && res.dias) {{
        actualizarTodasLasGrillas(res);
      }}
    }}
  }});
}});
</script>"""

payload = {
    'title': 'EatGo Menú Semanal Motor Interactivo Dinámico',
    'status': 'publish',
    'meta': {
        '_elementor_code': script_content,
        '_elementor_location': 'elementor_body_end',
        '_elementor_priority': 1,
        '_elementor_conditions': ['include/general']
    }
}

req = urllib.request.Request(
    'https://eatgopty.com/wp-json/wp/v2/elementor_snippet/660',
    headers={
        'Authorization': auth,
        'Content-Type': 'application/json'
    },
    data=json.dumps(payload).encode('utf-8')
)

with urllib.request.urlopen(req) as resp:
    data = json.load(resp)
    print('Snippet 660 updated successfully with zero-reload dynamic engine! Status:', data.get('status'))
