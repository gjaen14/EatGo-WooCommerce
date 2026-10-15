import json
import urllib.request
import base64

# --- 1. PREPARAR PÁGINA 751 ---
with open('remote_page_751_data.json', 'r', encoding='utf-8') as f:
    page_data = json.load(f)

# Card Retiro (antes crigh01) y Card Presencial (antes cleft01)
maincon = page_data[0]
card_presencial = maincon['elements'][0]  # cleft01
card_retiro = maincon['elements'][1]      # crigh01

# Actualizar Card Retiro (ahora a la izquierda)
# crbdt01: "RETIRO SIN FILAS"
card_retiro['elements'][0]['elements'][1]['elements'][0]['settings']['title'] = "RETIRO SIN FILAS"
# crtxt01: "Listo a tu hora elegida"
card_retiro['elements'][0]['elements'][1]['elements'][1]['settings']['title'] = "Listo a tu hora elegida"
# crh201: "RETIRA TU PEDIDO SIN FILAS"
card_retiro['elements'][0]['elements'][2]['settings']['title'] = "RETIRA TU PEDIDO SIN FILAS"
# crp01: Parrafo
card_retiro['elements'][0]['elements'][3]['settings']['editor'] = '<p style="margin:0;">¿Quieres que tu despacho sea rápido y sin filas? Realiza tu pedido desde nuestra web y al llegar la tendremos lista para su retiro bajo el nombre registrado.</p>'
# crbtn01: Boton "Pedido sin filas"
card_retiro['elements'][1]['settings']['text'] = "🛒 Pedido sin filas"
card_retiro['elements'][1]['settings']['link'] = {'url': '/menu-semanal/', 'is_external': False, 'nofollow': False}

# Actualizar Card Presencial (ahora a la derecha)
# clbdt01: "OPCIÓN PRESENCIAL"
card_presencial['elements'][0]['elements'][1]['elements'][0]['settings']['title'] = "OPCIÓN PRESENCIAL"
# cltxt01: "10-20 minutos"
card_presencial['elements'][0]['elements'][1]['elements'][1]['settings']['title'] = "10-20 minutos"
# clh201: "VISÍTANOS EN NUESTRO FOOD TRUCK"
card_presencial['elements'][0]['elements'][2]['settings']['title'] = "VISÍTANOS EN NUESTRO FOOD TRUCK"
# clbtn01: Boton "Cómo llegar"
card_presencial['elements'][1]['settings']['text'] = "🧭 Cómo llegar"
card_presencial['elements'][1]['settings']['link'] = {'url': 'https://maps.google.com/?q=Calle+50+Obarrio+Panama', 'is_external': True, 'nofollow': False}

# Invertir las tarjetas: Retiro a la izquierda (index 0), Presencial a la derecha (index 1)
maincon['elements'] = [card_retiro, card_presencial]

# --- ACTUALIZAR BLOQUE TURNOS Y PAGOS (turnosp) ---
turnosp = page_data[1]
coltur0 = turnosp['elements'][0]
colpag0 = turnosp['elements'][1]

# Columna Turnos:
coltur0['elements'][0]['settings']['title'] = "HORARIO DE ATENCIÓN"
coltur0['elements'][1]['settings']['title'] = "Turnos de Servicio Diario"
coltur0['elements'][2]['settings']['editor'] = '<p style="margin:0;">Cocinamos en dos tandas cada día para asegurar sabor y frescura</p>'

# Caja Mañana
cajman0 = coltur0['elements'][3]['elements'][0]
cajman0['elements'][0]['settings']['title'] = "TURNO MAÑANA"
cajman0['elements'][1]['settings']['title'] = "Desayuno panameño"
cajman0['elements'][2]['settings']['title'] = "6:30 AM – 11:00 AM"

# Caja Mediodía
cajmed0 = coltur0['elements'][3]['elements'][1]
cajmed0['elements'][0]['settings']['title'] = "TURNO MEDIODÍA"
cajmed0['elements'][1]['settings']['title'] = "Almuerzo criollo"
cajmed0['elements'][2]['settings']['title'] = "11:30 AM – 3:00 PM"

# Columna Pagos:
colpag0['elements'][1]['settings']['title'] = "MÉTODOS DE PAGO"
colpag0['elements'][2]['settings']['editor'] = '<p style="margin:0;">Aceptamos los siguientes métodos de pago, tanto para retiro o delivery:</p>'
# Las 4 tarjetas de pago permanecen 100% intactas

# --- CREAR SECCIÓN CORPORATIVO Y EVENTOS (TOP DE PÁGINA) ---
form_html = """
<div class="eatgo-corp-form-wrap" style="font-family:'Open Sans', sans-serif;">
  <form id="eatgoCorpForm" onsubmit="event.preventDefault(); window.sendCorpWhatsApp();" style="display:flex; flex-direction:column; gap:18px;">
    <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(260px, 1fr)); gap:16px;">
      <div>
        <label style="display:block; font-size:13px; font-weight:700; color:#374151; margin-bottom:6px;">Nombre de Contacto *</label>
        <input type="text" id="corp_nombre" required placeholder="Ej. Juan Pérez" style="width:100%; box-sizing:border-box; padding:12px 14px; border:1.5px solid #E5E7EB; border-radius:12px; font-size:14px; background:#F9FAFB; color:#18181B; outline:none; transition:border-color 0.2s;" onfocus="this.style.borderColor='#059669'" onblur="this.style.borderColor='#E5E7EB'" />
      </div>
      <div>
        <label style="display:block; font-size:13px; font-weight:700; color:#374151; margin-bottom:6px;">Empresa / Organización *</label>
        <input type="text" id="corp_empresa" required placeholder="Ej. Banco General / Consultora" style="width:100%; box-sizing:border-box; padding:12px 14px; border:1.5px solid #E5E7EB; border-radius:12px; font-size:14px; background:#F9FAFB; color:#18181B; outline:none; transition:border-color 0.2s;" onfocus="this.style.borderColor='#059669'" onblur="this.style.borderColor='#E5E7EB'" />
      </div>
      <div>
        <label style="display:block; font-size:13px; font-weight:700; color:#374151; margin-bottom:6px;">Teléfono / WhatsApp *</label>
        <input type="tel" id="corp_telefono" required placeholder="Ej. +507 6234-5678" style="width:100%; box-sizing:border-box; padding:12px 14px; border:1.5px solid #E5E7EB; border-radius:12px; font-size:14px; background:#F9FAFB; color:#18181B; outline:none; transition:border-color 0.2s;" onfocus="this.style.borderColor='#059669'" onblur="this.style.borderColor='#E5E7EB'" />
      </div>
      <div>
        <label style="display:block; font-size:13px; font-weight:700; color:#374151; margin-bottom:6px;">Cantidad de Personas *</label>
        <input type="number" id="corp_personas" required min="5" placeholder="Ej. 25" style="width:100%; box-sizing:border-box; padding:12px 14px; border:1.5px solid #E5E7EB; border-radius:12px; font-size:14px; background:#F9FAFB; color:#18181B; outline:none; transition:border-color 0.2s;" onfocus="this.style.borderColor='#059669'" onblur="this.style.borderColor='#E5E7EB'" />
      </div>
      <div style="grid-column: 1 / -1;">
        <label style="display:block; font-size:13px; font-weight:700; color:#374151; margin-bottom:6px;">Fecha del Evento *</label>
        <input type="date" id="corp_fecha" required style="width:100%; box-sizing:border-box; padding:12px 14px; border:1.5px solid #E5E7EB; border-radius:12px; font-size:14px; background:#F9FAFB; color:#18181B; outline:none; transition:border-color 0.2s;" onfocus="this.style.borderColor='#059669'" onblur="this.style.borderColor='#E5E7EB'" />
      </div>
    </div>
    <div style="display:flex; flex-wrap:wrap; gap:12px; margin-top:8px;">
      <button type="submit" style="flex:1; min-width:220px; background:#059669; color:#FFFFFF; border:none; padding:15px 24px; border-radius:12px; font-size:14px; font-weight:800; cursor:pointer; display:flex; align-items:center; justify-content:center; gap:8px; box-shadow:0 4px 14px rgba(5,150,105,0.25); transition:background 0.2s;" onmouseover="this.style.background='#047857'" onmouseout="this.style.background='#059669'">
        <span>📲</span> Solicitar Cotización por WhatsApp
      </button>
      <button type="button" onclick="window.sendCorpEmail();" style="flex:1; min-width:200px; background:#18181B; color:#FFFFFF; border:none; padding:15px 24px; border-radius:12px; font-size:14px; font-weight:700; cursor:pointer; display:flex; align-items:center; justify-content:center; gap:8px; transition:background 0.2s;" onmouseover="this.style.background='#27272A'" onmouseout="this.style.background='#18181B'">
        <span>✉️</span> Enviar por Correo
      </button>
    </div>
  </form>
</div>
<script>
window.sendCorpWhatsApp = function() {
  var nom = document.getElementById('corp_nombre').value.trim();
  var emp = document.getElementById('corp_empresa').value.trim();
  var tel = document.getElementById('corp_telefono').value.trim();
  var per = document.getElementById('corp_personas').value.trim();
  var fec = document.getElementById('corp_fecha').value.trim();
  if(!nom || !emp || !tel || !per || !fec) {
    alert('Por favor completa todos los campos para enviarte la cotización.');
    return;
  }
  var msg = "*SOLICITUD DE COTIZACIÓN CORPORATIVA / EVENTOS - EAT & GO* 🏢\\n" +
            "---------------------------------------------\\n" +
            "👤 *Nombre:* " + nom + "\\n" +
            "🏢 *Empresa:* " + emp + "\\n" +
            "📞 *Teléfono:* " + tel + "\\n" +
            "👥 *Cantidad de personas:* " + per + "\\n" +
            "📅 *Fecha del evento:* " + fec + "\\n" +
            "---------------------------------------------\\n" +
            "Solicito propuesta formal y menú para nuestro evento.";
  var url = "https://wa.me/50762345678?text=" + encodeURIComponent(msg);
  window.open(url, '_blank');
};
window.sendCorpEmail = function() {
  var nom = document.getElementById('corp_nombre').value.trim();
  var emp = document.getElementById('corp_empresa').value.trim();
  var tel = document.getElementById('corp_telefono').value.trim();
  var per = document.getElementById('corp_personas').value.trim();
  var fec = document.getElementById('corp_fecha').value.trim();
  var subject = encodeURIComponent("Cotización Corporativa - " + (emp || nom || "Empresa"));
  var body = encodeURIComponent("Estimado equipo de Eat & Go,\n\nSolicito cotización para evento corporativo:\n\n- Nombre: " + nom + "\n- Empresa: " + emp + "\n- Teléfono: " + tel + "\n- Personas: " + per + "\n- Fecha del Evento: " + fec + "\n\nQuedo a la espera de su propuesta.");
  window.location.href = "mailto:ventas@eatgopty.com?subject=" + subject + "&body=" + body;
};
</script>
"""

seccion_corporativa = {
  "id": "corpeve",
  "elType": "container",
  "settings": {
    "_element_id": "corporativo-eventos",
    "content_width": "boxed",
    "boxed_width": {"unit": "px", "size": 1280},
    "flex_direction": "column",
    "flex_align_items": "stretch",
    "flex_gap": {"unit": "px", "size": 24},
    "padding": {"unit": "px", "top": "40", "right": "40", "bottom": "40", "left": "40", "isLinked": False},
    "padding_mobile": {"unit": "px", "top": "28", "right": "20", "bottom": "28", "left": "20", "isLinked": False},
    "margin": {"unit": "px", "top": "40", "right": "auto", "bottom": "0", "left": "auto", "isLinked": False},
    "background_background": "classic",
    "background_color": "#FFFFFF",
    "border_border": "solid",
    "border_width": {"unit": "px", "top": "1", "right": "1", "bottom": "1", "left": "1", "isLinked": True},
    "border_color": "#E5E7EB",
    "border_radius": {"unit": "px", "top": "28", "right": "28", "bottom": "28", "left": "28", "isLinked": True},
    "box_shadow_box_shadow_type": "yes",
    "box_shadow_box_shadow": {"horizontal": 0, "vertical": 10, "blur": 30, "spread": 0, "color": "rgba(0,0,0,0.04)"}
  },
  "elements": [
    {
      "id": "corphdr",
      "elType": "container",
      "settings": {
        "content_width": "full",
        "flex_direction": "column",
        "flex_align_items": "flex-start",
        "flex_gap": {"unit": "px", "size": 10}
      },
      "elements": [
        {
          "id": "corpbdg",
          "elType": "container",
          "settings": {
            "background_background": "classic",
            "background_color": "#FEF3C7",
            "border_radius": {"unit": "px", "top": "50", "right": "50", "bottom": "50", "left": "50", "isLinked": True},
            "padding": {"unit": "px", "top": "4", "right": "14", "bottom": "4", "left": "14", "isLinked": False}
          },
          "elements": [
            {
              "id": "corpbtx",
              "elType": "widget",
              "widgetType": "heading",
              "settings": {
                "title": "🏢 PEDIDOS CORPORATIVOS Y EVENTOS",
                "header_size": "span",
                "title_color": "#92400E",
                "typography_typography": "custom",
                "typography_font_family": "Open Sans",
                "typography_font_size": {"unit": "px", "size": 11},
                "typography_font_weight": "700",
                "typography_letter_spacing": {"unit": "px", "size": 0.5}
              }
            }
          ]
        },
        {
          "id": "corptit",
          "elType": "widget",
          "widgetType": "heading",
          "settings": {
            "title": "Pedidos Corporativos y Eventos",
            "header_size": "h2",
            "title_color": "#18181B",
            "typography_typography": "custom",
            "typography_font_family": "Open Sans",
            "typography_font_size": {"unit": "px", "size": 28},
            "typography_font_weight": "900",
            "typography_line_height": {"unit": "em", "size": 1.2},
            "margin": {"unit": "px", "top": "4", "right": "0", "bottom": "4", "left": "0", "isLinked": False}
          }
        },
        {
          "id": "corpsub",
          "elType": "widget",
          "widgetType": "text-editor",
          "settings": {
            "editor": "<p style=\"margin:0;\">¿Tienes una reunión de equipo, almuerzo de oficina o evento corporativo en Panamá? Completa tus datos a continuación para coordinar tu cotización a la medida con despacho puntual y factura fiscal con RUC (DGI).</p>",
            "text_color": "#4B5563",
            "typography_typography": "custom",
            "typography_font_family": "Open Sans",
            "typography_font_size": {"unit": "px", "size": 14},
            "typography_line_height": {"unit": "em", "size": 1.6}
          }
        }
      ]
    },
    {
      "id": "corpfrm",
      "elType": "widget",
      "widgetType": "html",
      "settings": {
        "html": form_html
      }
    }
  ]
}

# Insertar sección corporativa al inicio
updated_page_data = [seccion_corporativa, maincon, turnosp]

# Guardar localmente
with open('updated_page_751.json', 'w', encoding='utf-8') as f:
    json.dump(updated_page_data, f, indent=2, ensure_ascii=False)
print("1. Guardado updated_page_751.json con éxito!")

# --- 2. PREPARAR FOOTER 932 ---
with open('footer_932_data.json', 'r', encoding='utf-8') as f:
    footer_data = json.load(f)

# Buscar y actualizar el nodo de enlaces corporativos en footer_data
def update_footer_node(node):
    if isinstance(node, dict):
        if node.get('id') == '1a3d344b' or ('paragraph' in node.get('settings', {}) and 'Cotiza' in str(node.get('settings', {}))):
            p_val = node['settings']['paragraph']
            if isinstance(p_val, dict) and 'value' in p_val:
                p_val['value'] = '<a target="_self" href="/donde-comer-y-retirar/#corporativo-eventos">Catering Corporativo / Eventos</a><br><a target="_self" href="/donde-comer-y-retirar/#corporativo-eventos">Cotiza aquí</a><br><a target="_self" href="/donde-comer-y-retirar/#contactos">Contáctanos</a>'
                print("2. Nodo de footer 1a3d344b actualizado!")
        for v in node.values():
            update_footer_node(v)
    elif isinstance(node, list):
        for item in node:
            update_footer_node(item)

update_footer_node(footer_data)

with open('updated_footer_932.json', 'w', encoding='utf-8') as f:
    json.dump(footer_data, f, indent=2, ensure_ascii=False)
print("3. Guardado updated_footer_932.json con éxito!")

