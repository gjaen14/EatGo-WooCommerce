import json

with open("template_631_data.json") as f:
    elements = json.load(f)

# Build a standalone HTML mock with the exact markup and CSS of template 631
bag_svg = '<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#000000" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align:middle;margin-right:8px;"><path d="M3.4 5.467a2 2 0 0 0-.4 1.2V20a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6.667a2 2 0 0 0-.4-1.2l-2-2.667A2 2 0 0 0 17 2H7a2 2 0 0 0-1.6.8z"></path><path d="M3 6h18"></path><path d="M16 10a4 4 0 0 1-8 0"></path></svg>'
send_svg = '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#10B981" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align:middle;margin-right:8px;"><line x1="22" y1="2" x2="11" y2="13"></line><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon></svg>'

html = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Eat&Go - Card 631 Preview</title>
<link href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600;700;800&display=swap" rel="stylesheet">
<style>
  body {{
    background: #F1F5F9;
    font-family: 'Open Sans', sans-serif;
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    margin: 0;
    padding: 40px;
    box-sizing: border-box;
  }}

  .card-container {{
    width: 380px;
    background: #FFFFFF;
    border-radius: 24px;
    border: 1px solid #E5E7EB;
    box-shadow: 0 4px 20px rgba(0,0,0,0.06);
    overflow: hidden;
    transition: transform 0.25s ease, box-shadow 0.25s ease;
  }}

  .card-container:hover {{
    transform: translateY(-4px);
    box-shadow: 0 14px 32px rgba(0,0,0,0.12);
  }}

  .card-header {{
    position: relative;
    height: 240px;
    background-image: url('https://eatgopty.com/wp-content/uploads/2026/09/Diseno-sin-titulo-6.png');
    background-size: cover;
    background-position: center;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 14px 16px;
    box-sizing: border-box;
  }}

  .header-top {{
    display: flex;
    justify-content: space-between;
    align-items: center;
  }}

  .badge-star {{
    background: #18181B;
    color: #FACC15;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 0.5px;
    padding: 6px 12px;
    border-radius: 50px;
    text-transform: uppercase;
  }}

  .badge-price {{
    background: #FFFFFF;
    color: #18181B;
    font-size: 14px;
    font-weight: 800;
    padding: 5px 14px;
    border-radius: 50px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.15);
  }}

  .header-bottom {{
    display: flex;
    justify-content: flex-end;
  }}

  .badge-box {{
    background: rgba(24, 24, 27, 0.85);
    backdrop-filter: blur(6px);
    -webkit-backdrop-filter: blur(6px);
    color: #FFFFFF;
    font-size: 11.5px;
    font-weight: 700;
    padding: 6px 12px;
    border-radius: 8px;
    display: inline-flex;
    align-items: center;
    gap: 6px;
  }}

  .card-body {{
    padding: 20px 22px 24px;
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    gap: 12px;
  }}

  .card-title {{
    font-size: 18px;
    font-weight: 800;
    color: #18181B;
    margin: 0;
    line-height: 1.3;
  }}

  .card-desc {{
    font-size: 12.5px;
    color: #6B7280;
    margin: 0;
    line-height: 1.5;
  }}

  .divider {{
    height: 1px;
    background: #F3F4F6;
    margin: 4px 0;
  }}

  .option-label {{
    font-size: 11.5px;
    font-weight: 700;
    color: #374151;
    margin: 0;
  }}

  .option-box {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: #FFFFFF;
    border: 1px solid #E5E7EB;
    border-radius: 12px;
    padding: 10px 14px;
    font-size: 12.5px;
    font-weight: 600;
    color: #18181B;
    cursor: pointer;
  }}

  .btn-primary {{
    background: #F59E0B;
    color: #000000;
    font-size: 14px;
    font-weight: 800;
    border: none;
    border-radius: 50px;
    padding: 13px 20px;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    box-shadow: 0 4px 14px rgba(245, 158, 11, 0.38);
    transition: all 0.2s ease;
    text-decoration: none;
    margin-top: 4px;
  }}

  .btn-primary:hover {{
    background: #D97706;
    transform: translateY(-1px);
    box-shadow: 0 6px 18px rgba(245, 158, 11, 0.48);
  }}

  .btn-secondary {{
    background: #F4F4F5;
    color: #18181B;
    font-size: 12.5px;
    font-weight: 700;
    border: 1px solid #E5E7EB;
    border-radius: 50px;
    padding: 11px 18px;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    text-decoration: none;
    transition: background 0.2s ease;
  }}

  .btn-secondary:hover {{
    background: #E4E4E7;
  }}
</style>
</head>
<body>

<div class="card-container">
  <div class="card-header">
    <div class="header-top">
      <div class="badge-star">PLATO ESTRELLA</div>
      <div class="badge-price">$6.50</div>
    </div>
    <div class="header-bottom">
      <div class="badge-box">📦 Ver en Caja 75°C</div>
    </div>
  </div>
  <div class="card-body">
    <h3 class="card-title">Sancocho Tradicional de Gallina de Patio</h3>
    <p class="card-desc">El rey indiscutible de Panamá: caldo espeso con ñame baboso, gallina suave y abundante culantro fresco cosechado.</p>
    <div class="divider"></div>
    <p class="option-label">Acompañamiento a tu gusto:</p>
    <div class="option-box">
      <span>Arroz Blanco Criollo</span>
      <span style="color:#9CA3AF;font-size:12px;">⌵</span>
    </div>
    <a href="#" class="btn-primary woosq-btn" data-id="631">
      {bag_svg} + Agregar al Pedido
    </a>
    <a href="https://wa.me/50762345678" target="_blank" class="btn-secondary">
      {send_svg} Planificar para este día por WhatsApp
    </a>
  </div>
</div>

</body>
</html>
"""

with open("card_631_preview.html", "w") as f:
    f.write(html)
print("Saved card_631_preview.html")
