import json, urllib.request, base64

# SVG bag icon content from Media ID 638
bag_svg = '<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#000000" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align:middle;margin-right:8px;"><path d="M3.4 5.467a2 2 0 0 0-.4 1.2V20a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6.667a2 2 0 0 0-.4-1.2l-2-2.667A2 2 0 0 0 17 2H7a2 2 0 0 0-1.6.8z"></path><path d="M3 6h18"></path><path d="M16 10a4 4 0 0 1-8 0"></path></svg>'

# Read base JSON
with open("template_631_data.json") as f:
    elements = json.load(f)

# Find w14btna (button) and w15btnw (whatsapp button) in elements tree
def update_button_elements(items):
    for item in items:
        if item.get("id") == "w14btna":
            # Update button text with SVG
            item["settings"]["text"] = f'{bag_svg}+ Agregar al Pedido'
            item["settings"]["background_color"] = "#F59E0B"
            item["settings"]["button_text_color"] = "#000000"
            item["settings"]["typography_font_weight"] = "800"
            item["settings"]["typography_font_size"] = {"unit": "px", "size": 14}
            item["settings"]["border_radius"] = {"unit": "px", "top": "50", "right": "50", "bottom": "50", "left": "50", "isLinked": True}
            item["settings"]["box_shadow_box_shadow_type"] = "yes"
            item["settings"]["box_shadow_box_shadow"] = {"horizontal": 0, "vertical": 4, "blur": 12, "spread": 0, "color": "rgba(245, 158, 11, 0.35)"}
        elif item.get("id") == "w15btnw":
            # WhatsApp button with green paperplane icon
            send_svg = '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#10B981" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align:middle;margin-right:8px;"><line x1="22" y1="2" x2="11" y2="13"></line><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon></svg>'
            item["settings"]["text"] = f'{send_svg}Planificar para este día por WhatsApp'
            item["settings"]["background_color"] = "#F4F4F5"
            item["settings"]["button_text_color"] = "#18181B"
            item["settings"]["border_border"] = "solid"
            item["settings"]["border_width"] = {"unit": "px", "top": "1", "right": "1", "bottom": "1", "left": "1", "isLinked": True}
            item["settings"]["border_color"] = "#E5E7EB"
            item["settings"]["border_radius"] = {"unit": "px", "top": "50", "right": "50", "bottom": "50", "left": "50", "isLinked": True}
            item["settings"]["typography_font_weight"] = "700"
            item["settings"]["typography_font_size"] = {"unit": "px", "size": 12.5}
        
        if "elements" in item:
            update_button_elements(item["elements"])

update_button_elements(elements)

# Save updated JSON
with open("template_631_data.json", "w") as f:
    json.dump(elements, f)

# CSS for Template 631
custom_css = """/* Template 631 - Pixel Perfect Design Matching Reference */
.elementor-631 div.elementor-element.elementor-element-c01root {
  background-color: #FFFFFF !important;
  border-radius: 24px !important;
  border: 1px solid #E5E7EB !important;
  box-shadow: 0 4px 16px rgba(0,0,0,0.06) !important;
  overflow: hidden !important;
  transition: transform 0.25s ease, box-shadow 0.25s ease !important;
}

.elementor-631 div.elementor-element.elementor-element-c01root:hover {
  transform: translateY(-4px) !important;
  box-shadow: 0 12px 28px rgba(0,0,0,0.12) !important;
}

/* Header container: Clean Crisp Photography without overlay/blur */
.elementor-631 div.elementor-element.elementor-element-c02covr {
  min-height: 220px !important;
  height: 220px !important;
  background-size: cover !important;
  background-position: center center !important;
  background-repeat: no-repeat !important;
  border-top-left-radius: 24px !important;
  border-top-right-radius: 24px !important;
  position: relative !important;
  overflow: hidden !important;
}

.elementor-631 div.elementor-element.elementor-element-c02covr::before {
  display: none !important;
  content: none !important;
  opacity: 0 !important;
  background: none !important;
}

/* Badge PLATO ESTRELLA */
.elementor-631 div.elementor-element.elementor-element-w04bstar div {
  background: #18181B !important;
  color: #FACC15 !important;
  font-family: 'Open Sans', sans-serif !important;
  font-size: 10px !important;
  font-weight: 800 !important;
  letter-spacing: 0.5px !important;
  padding: 5px 12px !important;
  border-radius: 50px !important;
  text-transform: uppercase !important;
  display: inline-block !important;
}

/* Badge Precio */
.elementor-631 div.elementor-element.elementor-element-w05bpric .elementor-heading-title {
  background: #FFFFFF !important;
  color: #18181B !important;
  font-family: 'Open Sans', sans-serif !important;
  font-size: 13px !important;
  font-weight: 800 !important;
  padding: 4px 12px !important;
  border-radius: 50px !important;
  box-shadow: 0 2px 6px rgba(0,0,0,0.15) !important;
  display: inline-block !important;
}

/* Badge Ver en Caja */
.elementor-631 div.elementor-element.elementor-element-w07bbox div {
  background: rgba(24,24,27,0.85) !important;
  backdrop-filter: blur(4px) !important;
  -webkit-backdrop-filter: blur(4px) !important;
  color: #FFFFFF !important;
  font-family: 'Open Sans', sans-serif !important;
  font-size: 11px !important;
  font-weight: 700 !important;
  padding: 5px 10px !important;
  border-radius: 8px !important;
  display: inline-flex !important;
  align-items: center !important;
}

/* Title Styling */
.elementor-631 div.elementor-element.elementor-element-w09titl .elementor-heading-title {
  color: #18181B !important;
  font-family: 'Open Sans', sans-serif !important;
  font-size: 17px !important;
  font-weight: 800 !important;
  line-height: 1.25 !important;
}

/* Description Styling */
.elementor-631 div.elementor-element.elementor-element-w10desc {
  color: #6B7280 !important;
  font-family: 'Open Sans', sans-serif !important;
  font-size: 12px !important;
  line-height: 1.45 !important;
}

/* Primary Button Styling */
.elementor-631 div.elementor-element.elementor-element-w14btna a.elementor-button {
  background-color: #F59E0B !important;
  color: #000000 !important;
  font-family: 'Open Sans', sans-serif !important;
  font-weight: 800 !important;
  font-size: 14px !important;
  border-radius: 50px !important;
  padding: 12px 20px !important;
  box-shadow: 0 4px 14px rgba(245, 158, 11, 0.35) !important;
  transition: all 0.2s ease !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
}

.elementor-631 div.elementor-element.elementor-element-w14btna a.elementor-button:hover {
  background-color: #D97706 !important;
  transform: translateY(-1px) !important;
  box-shadow: 0 6px 18px rgba(245, 158, 11, 0.45) !important;
}

/* Secondary Button Styling */
.elementor-631 div.elementor-element.elementor-element-w15btnw a.elementor-button {
  background-color: #F4F4F5 !important;
  color: #18181B !important;
  border: 1px solid #E5E7EB !important;
  font-family: 'Open Sans', sans-serif !important;
  font-weight: 700 !important;
  font-size: 12.5px !important;
  border-radius: 50px !important;
  padding: 10px 16px !important;
  transition: all 0.2s ease !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
}

.elementor-631 div.elementor-element.elementor-element-w15btnw a.elementor-button:hover {
  background-color: #E4E4E7 !important;
}
"""

# Update WordPress Elementor Library 631
url = "https://eatgopty.com/wp-json/wp/v2/elementor_library/631"
username = "JaenDev"
password = "4n3FKy26SkBpwe8GPBzdbqEz"
auth_header = "Basic " + base64.b64encode(f"{username}:{password}".encode()).decode()

payload = {
    "status": "publish",
    "meta": {
        "_elementor_edit_mode": "builder",
        "_elementor_template_type": "loop-item",
        "_elementor_data": json.dumps(elements),
        "_elementor_page_settings": {
            "custom_css": custom_css
        }
    }
}

req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers={
    "Content-Type": "application/json",
    "Authorization": auth_header
})

try:
    with urllib.request.urlopen(req) as resp:
        print("Updated template 631 successfully, status:", resp.getcode())
except Exception as e:
    print("Error updating template 631:", e)
