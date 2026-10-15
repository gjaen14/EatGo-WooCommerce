import json

refined_corp_html = """
<div class="eatgo-corp-grid" style="font-family:'Open Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
  <style>
    .eatgo-corp-grid {
      display: grid;
      grid-template-columns: 4.8fr 7.2fr;
      gap: 36px;
      align-items: flex-start;
      width: 100%;
    }
    @media (max-width: 991px) {
      .eatgo-corp-grid {
        grid-template-columns: 1fr;
        gap: 28px;
      }
    }
    .eatgo-channel-card {
      display: flex;
      align-items: center;
      gap: 14px;
      padding: 16px 20px;
      background: #FFFFFF !important;
      border: 1px solid #E5E7EB;
      border-radius: 16px;
      text-decoration: none !important;
      transition: all 0.2s ease;
      box-shadow: 0 1px 3px rgba(0,0,0,0.03);
      cursor: pointer;
    }
    .eatgo-channel-card:hover {
      border-color: #F59E0B;
      transform: translateY(-1px);
      box-shadow: 0 6px 16px rgba(0,0,0,0.06);
    }
    .eatgo-channel-card.channel-whatsapp:hover {
      border-color: #10B981;
    }
    .eatgo-form-card {
      background: #FFFFFF;
      border: 1px solid #E5E7EB;
      border-radius: 28px;
      padding: 36px 36px 32px;
      box-shadow: 0 8px 24px rgba(0,0,0,0.04);
    }
    @media (max-width: 640px) {
      .eatgo-form-card {
        padding: 24px 20px;
        border-radius: 20px;
      }
    }
    .eatgo-input-field {
      width: 100%;
      box-sizing: border-box;
      padding: 11px 14px;
      background: #FAFAFA;
      border: 1.5px solid #E5E7EB;
      border-radius: 12px;
      font-size: 13.5px;
      font-family: inherit;
      color: #18181B;
      outline: none;
      transition: border-color 0.2s, background 0.2s;
    }
    .eatgo-input-field:focus {
      background: #FFFFFF;
      border-color: #F59E0B;
    }
    .eatgo-form-label {
      display: block;
      font-size: 12px;
      font-weight: 700;
      color: #374151;
      margin-bottom: 6px;
    }
    .eatgo-btn-primary {
      width: 100%;
      padding: 14px 20px;
      background: #F59E0B;
      color: #18181B;
      border: none;
      border-radius: 12px;
      font-size: 14px;
      font-weight: 900;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      transition: all 0.2s ease;
      box-shadow: 0 4px 14px rgba(245,158,11,0.25);
    }
    .eatgo-btn-primary:hover {
      background: #D97706;
      color: #FFFFFF;
      transform: translateY(-1px);
    }
  </style>

  <!-- COLUMNA IZQUIERDA: Canales de Atención Directa -->
  <div style="display:flex; flex-direction:column; gap:16px;">
    <div>
      <h3 style="margin:0 0 10px 0; font-size:24px; font-weight:900; color:#18181B; letter-spacing:-0.3px;">
        Canales de Atención Directa
      </h3>
      <p style="margin:0; font-size:13px; color:#4B5563; line-height:1.6;">
        Respondemos de inmediato para confirmación de pedidos, dudas sobre platos de la paila o reservas de almuerzos corporativos.
      </p>
    </div>

    <div style="display:flex; flex-direction:column; gap:12px; margin-top:6px;">
      <!-- WhatsApp (usa api.whatsapp.com para no ser afectado por jQuery wa.me) -->
      <a href="https://api.whatsapp.com/send?phone=50762345678&text=Hola%20Eat%26Go,%20deseo%20hacer%20una%20consulta%20directa" target="_blank" rel="noopener noreferrer" class="eatgo-channel-card channel-whatsapp">
        <div style="width:42px; height:42px; border-radius:12px; background:#ECFDF5; color:#059669; display:flex; align-items:center; justify-content:center; flex-shrink:0;">
          <svg style="width:20px; height:20px; fill:currentColor;" viewBox="0 0 24 24"><path d="M2.01 21L23 12 2.01 3 2 10l15 2-15 2z"/></svg>
        </div>
        <div style="display:flex; flex-direction:column; gap:2px;">
          <span style="font-size:13px; font-weight:700; color:#18181B;">WhatsApp Pedidos Express</span>
          <span style="font-size:12px; color:#6B7280;">+507 6234-5678 (Respuesta &lt; 2 min)</span>
        </div>
      </a>

      <!-- Teléfono Fijo -->
      <a href="tel:+5072645000" class="eatgo-channel-card">
        <div style="width:42px; height:42px; border-radius:12px; background:#FEF3C7; color:#D97706; display:flex; align-items:center; justify-content:center; flex-shrink:0;">
          <svg style="width:20px; height:20px; fill:currentColor;" viewBox="0 0 24 24"><path d="M20.01 15.38c-1.23 0-2.42-.2-3.53-.56a.977.977 0 00-1.01.24l-2.2 2.2a15.053 15.053 0 01-6.59-6.59l2.2-2.21a.96.96 0 00.25-1.01A11.36 11.36 0 018.57 3.9c0-.55-.45-1-1-1H4c-.55 0-1 .45-1 1 0 9.39 7.61 17 17 17 .55 0 1-.45 1-1v-3.52c0-.55-.45-1-.99-1z"/></svg>
        </div>
        <div style="display:flex; flex-direction:column; gap:2px;">
          <span style="font-size:13px; font-weight:700; color:#18181B;">Teléfono Fijo de Cocina</span>
          <span style="font-size:12px; color:#6B7280;">+507 264-5000 (Mostrador Local)</span>
        </div>
      </a>

      <!-- Correo -->
      <a href="mailto:pedidos@eatandgopa.com" class="eatgo-channel-card">
        <div style="width:42px; height:42px; border-radius:12px; background:#F3F4F6; color:#374151; display:flex; align-items:center; justify-content:center; flex-shrink:0;">
          <svg style="width:20px; height:20px; fill:currentColor;" viewBox="0 0 24 24"><path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg>
        </div>
        <div style="display:flex; flex-direction:column; gap:2px;">
          <span style="font-size:13px; font-weight:700; color:#18181B;">Correo Corporativo</span>
          <span style="font-size:12px; color:#6B7280;">pedidos@eatandgopa.com</span>
        </div>
      </a>
    </div>
  </div>

  <!-- COLUMNA DERECHA: Tarjeta de Formulario -->
  <div class="eatgo-form-card">
    <div style="display:flex; align-items:center; gap:8px; font-size:11px; font-weight:900; text-transform:uppercase; letter-spacing:1px; color:#92400E; margin-bottom:6px;">
      <svg style="width:14px; height:14px; fill:currentColor;" viewBox="0 0 24 24"><path d="M20 2H4c-1.1 0-1.99.9-1.99 2L2 22l4-4h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2z"/></svg>
      <span>ENVÍANOS UN MENSAJE</span>
    </div>
    
    <h3 style="margin:0 0 6px 0; font-size:24px; font-weight:900; color:#18181B; letter-spacing:-0.3px; line-height:1.25;">
      ¿Tienes alguna consulta o requerimiento especial?
    </h3>
    <p style="margin:0 0 22px 0; font-size:13px; color:#6B7280; line-height:1.5;">
      Escríbenos y te contactamos por WhatsApp o llamada en minutos con tu cotización formal.
    </p>

    <form id="eatgoRefinedForm" onsubmit="event.preventDefault(); window.sendRefinedWhatsApp();" style="display:flex; flex-direction:column; gap:16px;">
      <!-- Fila 1: Nombre y Teléfono -->
      <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(220px, 1fr)); gap:14px;">
        <div>
          <label class="eatgo-form-label">Nombre Completo *</label>
          <input type="text" id="ref_nombre" required placeholder="Ej: Carlos Moreno" class="eatgo-input-field" />
        </div>
        <div>
          <label class="eatgo-form-label">Teléfono / WhatsApp *</label>
          <input type="tel" id="ref_telefono" required placeholder="Ej: +507 6123-4567" class="eatgo-input-field" />
        </div>
      </div>

      <!-- Fila 2: Empresa y Personas -->
      <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(220px, 1fr)); gap:14px;">
        <div>
          <label class="eatgo-form-label">Empresa / Organización *</label>
          <input type="text" id="ref_empresa" required placeholder="Ej: Banco General / Particular" class="eatgo-input-field" />
        </div>
        <div>
          <label class="eatgo-form-label">Cantidad de Personas *</label>
          <input type="number" id="ref_personas" required min="1" placeholder="Ej: 25 personas" class="eatgo-input-field" />
        </div>
      </div>

      <!-- Fila 3: Fecha del Evento y Motivo -->
      <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(220px, 1fr)); gap:14px;">
        <div>
          <label class="eatgo-form-label">Fecha Tentativa del Evento *</label>
          <input type="date" id="ref_fecha" required class="eatgo-input-field" />
        </div>
        <div>
          <label class="eatgo-form-label">Motivo de Consulta</label>
          <select id="ref_motivo" class="eatgo-input-field" style="cursor:pointer;">
            <option value="empresa">Almuerzo de Empresa / Factura Fiscal</option>
            <option value="catering">Catering para Evento Especial</option>
            <option value="retiro">Retiro Pick & Go en Local</option>
            <option value="comedor">Visitar el Comedor Presencial</option>
            <option value="otro">Otra Consulta Personalizada</option>
          </select>
        </div>
      </div>

      <!-- Fila 4: Mensaje o Pedido Detallado -->
      <div>
        <label class="eatgo-form-label">Mensaje o Pedido Detallado</label>
        <textarea id="ref_mensaje" rows="3" placeholder="Indícanos platos de interés, número de personas o cualquier instrucción..." class="eatgo-input-field" style="resize:vertical;"></textarea>
      </div>

      <!-- Botón de Envío -->
      <div style="margin-top:4px;">
        <button type="submit" class="eatgo-btn-primary">
          <svg style="width:16px; height:16px; fill:currentColor;" viewBox="0 0 24 24"><path d="M2.01 21L23 12 2.01 3 2 10l15 2-15 2z"/></svg>
          <span>Enviar Consulta Directa por WhatsApp</span>
        </button>
      </div>
    </form>
  </div>
</div>

<script>
window.sendRefinedWhatsApp = function() {
  var nom = document.getElementById('ref_nombre').value.trim();
  var tel = document.getElementById('ref_telefono').value.trim();
  var emp = document.getElementById('ref_empresa').value.trim();
  var per = document.getElementById('ref_personas').value.trim();
  var fec = document.getElementById('ref_fecha').value.trim();
  var motSel = document.getElementById('ref_motivo');
  var mot = motSel ? motSel.options[motSel.selectedIndex].text : 'Consulta';
  var men = document.getElementById('ref_mensaje').value.trim();

  if(!nom || !tel || !emp || !per || !fec) {
    alert('Por favor completa los campos requeridos (*).');
    return;
  }

  var msg = "*CONSULTA CORPORATIVA / EVENTOS - EAT & GO* 🏢\\n" +
            "---------------------------------------------\\n" +
            "👤 *Nombre:* " + nom + "\\n" +
            "📞 *Teléfono:* " + tel + "\\n" +
            "🏛️ *Empresa:* " + emp + "\\n" +
            "👥 *Cantidad de personas:* " + per + "\\n" +
            "📅 *Fecha:* " + fec + "\\n" +
            "📋 *Motivo:* " + mot + "\\n";
  if(men) {
    msg += "📝 *Detalles:* " + men + "\\n";
  }
  msg += "---------------------------------------------\\n" +
         "Solicito propuesta formal y disponibilidad.";

  var url = "https://api.whatsapp.com/send?phone=50762345678&text=" + encodeURIComponent(msg);
  window.open(url, '_blank');
};
</script>
"""

with open('updated_page_751.json', 'r', encoding='utf-8') as f:
    page_data = json.load(f)

corp_sec = page_data[0]
corp_sec['settings'] = {
    "_element_id": "corporativo-eventos",
    "content_width": "boxed",
    "boxed_width": {"unit": "px", "size": 1280},
    "flex_direction": "column",
    "padding": {"unit": "px", "top": "50", "right": "20", "bottom": "10", "left": "20", "isLinked": False},
    "padding_mobile": {"unit": "px", "top": "36", "right": "16", "bottom": "10", "left": "16", "isLinked": False},
    "margin": {"unit": "px", "top": "0", "right": "auto", "bottom": "0", "left": "auto", "isLinked": False}
}

corp_sec['elements'] = [
    {
        "id": "corpfrm",
        "elType": "widget",
        "widgetType": "html",
        "settings": {
            "html": refined_corp_html
        }
    }
]

with open('updated_page_751.json', 'w', encoding='utf-8') as f:
    json.dump(page_data, f, indent=2, ensure_ascii=False)

print("updated_page_751.json listo con api.whatsapp.com!")
