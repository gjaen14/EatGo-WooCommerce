import urllib.request
import json
import base64

# Leer el código generado
with open('snippet_660_live_extracted.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# Dividir style y script
style_part, _ = content.split('<script>', 1)

css_addition = """
/* Estado Inactivo / Bloqueado para platos de dias que no corresponden a hoy */
.page-id-564 .elementor-element-w14btna.is-disabled-day a.elementor-button,
.page-id-564 .elementor-element-w14btna a.elementor-button.is-disabled-day,
.page-id-564 .is-disabled-day .elementor-element-w14btna a.elementor-button,
.page-id-564 .woosq-btn.is-disabled-day,
.page-id-564 .is-disabled-day .woosq-btn {
  pointer-events: none !important;
  cursor: not-allowed !important;
  opacity: 0.45 !important;
  filter: grayscale(0.6) !important;
  background-color: #E4E4E7 !important;
  color: #71717A !important;
  box-shadow: none !important;
  transform: none !important;
}
.page-id-564 .elementor-element-w14btna.is-disabled-day a.elementor-button:hover,
.page-id-564 .elementor-element-w14btna.is-disabled-day a.elementor-button:focus {
  background-color: #E4E4E7 !important;
  color: #71717A !original !important;
}
.page-id-564 .elementor-element-w14btna.is-disabled-day svg,
.page-id-564 a.elementor-button.is-disabled-day svg {
  opacity: 0.5 !important;
  stroke: #71717A !important;
  fill: #71717A !important;
}
"""

new_style = style_part.rstrip() + css_addition + "\n</style>\n"

new_script = """<script>
jQuery(function($) {
  // Asegurar que solo se ejecute en la página de Menú Semanal
  if (!$('body').hasClass('page-id-564') && window.location.pathname.indexOf('menu-semanal') === -1) {
    return;
  }

  // 1. Diccionario de días e información de cabecera
  var diasInfo = {
    'lunes': { nombre: 'LUNES', badge: '🍲 Día de Caldos Reconfortantes', sub: 'Arranca la semana laboral con energía criolla y guisos reconfortantes de olla honda.' },
    'martes': { nombre: 'MARTES', badge: '🥘 Día de Guisados y Tradición', sub: 'Pailas encendidas con el clásico mondongo panameño y carnes en salsa.' },
    'miercoles': { nombre: 'MIÉRCOLES', badge: '🍖 Especiales de Mitad de Semana', sub: 'El ombligo de la semana se saborea con puerco criollo y costilla suave.' },
    'jueves': { nombre: 'JUEVES', badge: '🍝 Día Criollo & Aves al Callejón', sub: 'Pastas tradicionales con albóndigas y porotos criollos que rinden homenaje a la casa.' },
    'viernes': { nombre: 'VIERNES', badge: '🐟 Mariscos Frescos & Fin de Semana', sub: 'Cierre de oficina como se debe: corvina, mariscos y salsas caribeñas.' },
    'sabado': { nombre: 'SÁBADO', badge: '👨‍👩‍👧‍👦 Paila Familiar de Fin de Semana', sub: 'Bandejas y platos abundantes para compartir en familia o con amigos.' }
  };

  var diasSemana = ['domingo', 'lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado'];

  // Obtener fecha actual en zona horaria America/Panama
  function getPanamaDayInfo() {
    try {
      var dStr = new Date().toLocaleString('en-US', { timeZone: 'America/Panama' });
      var dPanama = new Date(dStr);
      var dNum = dPanama.getDay();
      return { num: dNum, slug: diasSemana[dNum] };
    } catch(e) {
      var dLocal = new Date();
      var dNum = dLocal.getDay();
      return { num: dNum, slug: diasSemana[dNum] };
    }
  }

  var hoyInfo = getPanamaDayInfo();
  var diaHoyNum = hoyInfo.num;       // 0 = Domingo, 1 = Lunes, etc.
  var diaHoySlug = hoyInfo.slug;     // 'domingo', 'lunes', etc.
  var esDomingo = (diaHoyNum === 0);

  // 1.1. Detección de parámetro en URL (?dia=miercoles, ?dia=viernes, etc.)
  function getUrlDiaParam() {
    try {
      var urlParam = '';
      if (window.URLSearchParams) {
        var params = new URLSearchParams(window.location.search);
        urlParam = params.get('dia');
      } else {
        var m = window.location.search.match(/[?&]dia=([^&]+)/);
        if (m) urlParam = decodeURIComponent(m[1]);
      }
      if (urlParam) {
        urlParam = urlParam.toLowerCase().trim();
        var mapDia = {
          'lun': 'lunes', 'lunes': 'lunes',
          'mar': 'martes', 'martes': 'martes',
          'mie': 'miercoles', 'mié': 'miercoles', 'miercoles': 'miercoles', 'miércoles': 'miercoles',
          'jue': 'jueves', 'jueves': 'jueves',
          'vie': 'viernes', 'viernes': 'viernes',
          'sab': 'sabado', 'sáb': 'sabado', 'sabado': 'sabado', 'sábado': 'sabado'
        };
        if (mapDia[urlParam]) return mapDia[urlParam];
      }
    } catch(e) {}
    return null;
  }

  var diaParamUrl = getUrlDiaParam();

  // REGLA DE DOMINGO: Si hoy es domingo (cocina cerrada), activar LUNES por defecto en pantalla
  var diaActivo = diaParamUrl ? diaParamUrl : (esDomingo ? 'lunes' : diaHoySlug);

  var pillMap = {
    '675a0b2b': 'lunes',
    '407669ce': 'martes',
    '2c494cb1': 'miercoles',
    '60e274d': 'jueves',
    '4fdd1a46': 'viernes',
    'da15a65': 'sabado',
    '302c53b1': 'lunes',
    '1366f201': 'martes',
    'db09404': 'miercoles',
    '10dfeecc': 'jueves',
    '258724b8': 'viernes',
    '38fd654a': 'sabado'
  };

  var gridMap = {
    'lunes': $('[data-interaction-id="12dc898b"], [data-interaction-id="69a6b14f"], .elementor-element-lg_lun, [data-id="lg_lun"]'),
    'martes': $('[data-interaction-id="4bf72f7d"], [data-interaction-id="5c59ff09"], .elementor-element-lg_mar, [data-id="lg_mar"]'),
    'miercoles': $('[data-interaction-id="5bfd1736"], [data-interaction-id="777795ed"], .elementor-element-lg_mie, [data-id="lg_mie"]'),
    'jueves': $('[data-interaction-id="2fd6c6a9"], [data-interaction-id="777c2879"], .elementor-element-lg_jue, [data-id="lg_jue"]'),
    'viernes': $('[data-interaction-id="62f9bc94"], [data-interaction-id="5b7538c7"], .elementor-element-lg_vie, [data-id="lg_vie"]'),
    'sabado': $('[data-interaction-id="74741324"], [data-interaction-id="7ed1d723"], .elementor-element-lg_sab, [data-id="lg_sab"]')
  };

  // 2. Consultar info de semana activa únicamente para actualizar el banner
  $.ajax({
    url: '/wp-json/eatgo/v1/menu-semanal',
    method: 'GET',
    dataType: 'json',
    success: function(res) {
      if (res && res.dias) {
        var semNum = res.semana_activa || '1';
        var $counter = $('[data-interaction-id="60fcda6e"], .banner-dia-counter, [data-interaction-id="4a66aef8"]').first();
        if ($counter.length) {
          var countPlatos = (res.dias[diaActivo] && res.dias[diaActivo].platos) ? res.dias[diaActivo].platos.length : 3;
          $counter.text('🗓️ Semana ' + semNum + ' del Mes • ' + countPlatos + ' especialidades preparadas hoy');
        }
      }
    }
  });

  // 3. Control Operativo de Botones (+ Agregar al Pedido) por Día
  function actualizarBotonesPorDia(diaSlug) {
    var esDiaComprable = (!esDomingo && diaSlug === diaHoySlug);
    var diaTexto = diasInfo[diaSlug] ? diasInfo[diaSlug].nombre : diaSlug.toUpperCase();
    var $activeGrid = gridMap[diaSlug];

    if (!$activeGrid || !$activeGrid.length) return;

    $activeGrid.find('.woosq-btn, .elementor-element-w14btna').each(function() {
      var $btnContainer = $(this);
      var $btnLink = $btnContainer.is('a') ? $btnContainer : $btnContainer.find('a');
      var $btnText = $btnContainer.find('.elementor-button-text');

      if (esDiaComprable) {
        // Habilitar compras de HOY
        $btnContainer.removeClass('is-disabled-day').css('pointer-events', 'auto');
        $btnLink.removeClass('is-disabled-day').css('pointer-events', 'auto');
        if ($btnText.length) {
          $btnText.text('+ Agregar al Pedido');
        }
      } else {
        // Deshabilitar compras de otros días o si es domingo
        $btnContainer.addClass('is-disabled-day').css('pointer-events', 'none');
        $btnLink.addClass('is-disabled-day').css('pointer-events', 'none');
        if ($btnText.length) {
          $btnText.text('Disponible el ' + diaTexto.charAt(0) + diaTexto.slice(1).toLowerCase());
        }
      }
    });
  }

  // 4. Función para activar un día visualmente (CERO RECARGA)
  function seleccionarDia(diaSlug) {
    if (!diasInfo[diaSlug]) diaSlug = 'lunes';
    diaActivo = diaSlug;

    // A. Actualizar estado visual de las píldoras
    $('[data-interaction-id="675a0b2b"], [data-interaction-id="407669ce"], [data-interaction-id="2c494cb1"], [data-interaction-id="60e274d"], [data-interaction-id="4fdd1a46"], [data-interaction-id="da15a65"], .btn-dia-tab, [class*="dia-tab"]').each(function() {
      var iid = $(this).attr('data-interaction-id');
      var target = (iid && pillMap[iid]) ? pillMap[iid] : ($(this).attr('data-dia') || $(this).text().toLowerCase());
      if (target.indexOf(diaSlug) !== -1) {
        $(this).addClass('is-active').css({
          'background-color': '#F59E0B',
          'border-color': '#F59E0B',
          'color': '#18181B',
          'font-weight': '800',
          'box-shadow': '0 2px 8px rgba(245,158,11,0.3)',
          'cursor': 'pointer'
        });
        $(this).find('*').css({ 'color': '#18181B', 'font-weight': '800' });
      } else {
        $(this).removeClass('is-active').css({
          'background-color': '#FFFFFF',
          'border': '1px solid #E5E7EB',
          'color': '#18181B',
          'font-weight': '600',
          'box-shadow': 'none',
          'cursor': 'pointer'
        });
        $(this).find('*').css({ 'color': '#18181B', 'font-weight': '600' });
      }
    });

    // B. Actualizar textos del banner
    var info = diasInfo[diaSlug];
    var $title = $('[data-interaction-id="346b2401"], .banner-dia-title, [data-interaction-id="7a072b70"] h3, .elementor-heading-title:contains("MENÚ DEL")').first();
    if ($title.length) $title.text('MENÚ DEL ' + info.nombre);

    var $badge = $('[data-interaction-id="3b175772"], .banner-dia-badge, [data-interaction-id="6ff39463"]').first();
    if ($badge.length) $badge.text(info.badge);

    var $sub = $('[data-interaction-id="5e2b25c1"], .banner-dia-sub, [data-interaction-id="4b3186ef"]').first();
    if ($sub.length) $sub.text(info.sub);

    // C. Mostrar los platos de ese día y ocultar los demás
    for (var s in gridMap) {
      if (s === diaSlug) {
        gridMap[s].css('display', 'flex').hide().fadeIn(180);
      } else {
        gridMap[s].hide().css('display', 'none');
      }
    }

    // D. Aplicar control operativo en los botones del día seleccionado
    actualizarBotonesPorDia(diaSlug);
  }

  // Ejecutar selección inicial automática
  seleccionarDia(diaActivo);

  // 5. Escuchar clics en las píldoras de los días (Cero recarga)
  $(document).on('click', '[data-interaction-id="675a0b2b"], [data-interaction-id="407669ce"], [data-interaction-id="2c494cb1"], [data-interaction-id="60e274d"], [data-interaction-id="4fdd1a46"], [data-interaction-id="da15a65"], .btn-dia-tab, [class*="dia-tab"], a:contains("LUNES"), a:contains("MARTES"), a:contains("MIÉRCOLES"), a:contains("JUEVES"), a:contains("VIERNES"), a:contains("SÁBADO")', function(e) {
    e.preventDefault();
    var iid = $(this).attr('data-interaction-id');
    if (iid && pillMap[iid]) {
      seleccionarDia(pillMap[iid]);
      return;
    }
    var txt = $(this).text().toLowerCase();
    for (var slug in diasInfo) {
      if (txt.indexOf(slug) !== -1) {
        seleccionarDia(slug);
        break;
      }
    }
  });

  // 6. Conectar modales nativos QuickView (+ Agregar al Pedido) con guardia de seguridad
  $(document).on('click', '.woosq-btn, .elementor-element-w14btna a', function(e) {
    // Si la tarjeta o botón está en estado inactivo por día no correspondiente, bloquear estrictamente
    if ($(this).hasClass('is-disabled-day') || $(this).closest('.is-disabled-day').length || $(this).closest('.elementor-element-w14btna').hasClass('is-disabled-day')) {
      e.preventDefault();
      e.stopPropagation();
      e.stopImmediatePropagation();
      return false;
    }

    // Guardia de seguridad: verificar si el día activo en pantalla es HOY
    if (esDomingo || diaActivo !== diaHoySlug) {
      e.preventDefault();
      e.stopPropagation();
      e.stopImmediatePropagation();
      return false;
    }

    e.preventDefault();
    e.stopPropagation();
    var pid = $(this).attr('data-id') || $(this).attr('data-product_id');
    if (!pid || pid.indexOf('elementor-tag') !== -1) {
      var postClass = $(this).closest('[class*="post-"]').attr('class') || '';
      var match = postClass.match(/post-(\\d+)/);
      if (match && match[1]) pid = match[1];
    }
    if (pid && typeof woosq_open === 'function') {
      woosq_open(pid);
    }
  });
});
</script>"""

full_code = new_style + new_script

# Guardar en archivo local
with open('snippet_660_final_payload.txt', 'w', encoding='utf-8') as out:
    out.write(full_code)

print("Generated code length:", len(full_code))

# Actualizar en WordPress
username = 'JaenDev'
password = '4n3FKy26SkBpwe8GPBzdbqEz'
auth = 'Basic ' + base64.b64encode(f'{username}:{password}'.encode()).decode()

payload = json.dumps({
    'meta': {
        '_elementor_code': full_code
    }
}).encode('utf-8')

req = urllib.request.Request(
    'https://eatgopty.com/wp-json/wp/v2/elementor_snippet/660',
    data=payload,
    headers={
        'Authorization': auth,
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0'
    },
    method='POST'
)

try:
    with urllib.request.urlopen(req) as resp:
        res = json.loads(resp.read().decode('utf-8'))
        print('Updated snippet 660 successfully! Status:', resp.status)
        print('Modified:', res.get('modified'))
except Exception as e:
    print('Error deploying snippet 660:', e)
