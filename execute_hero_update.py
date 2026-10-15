import urllib.request, json, base64

auth = base64.b64encode(b'JaenDev:4n3FKy26SkBpwe8GPBzdbqEz').decode('utf-8')

# 1. Fetch current page 58
req = urllib.request.Request('https://eatgopty.com/wp-json/wp/v2/pages/58?context=edit', headers={'Authorization': f'Basic {auth}'})
with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode('utf-8'))
    meta = data.get('meta', {})
    el_data = json.loads(meta.get('_elementor_data', '[]'))

# 2. Build the Hero elements
badge_widget = {
    "id": "h01badg",
    "elType": "widget",
    "widgetType": "heading",
    "settings": {
        "title": "<span class=\"badge-live-red\">Desayunos, almuerzos y comida rápida</span>",
        "header_size": "div",
        "_css_classes": "badge-live-red-widget",
        "margin": {
            "unit": "px",
            "top": "0",
            "right": "0",
            "bottom": "16",
            "left": "0",
            "isLinked": False
        },
        "margin_mobile": {
            "unit": "px",
            "top": "0",
            "right": "0",
            "bottom": "14",
            "left": "0",
            "isLinked": False
        }
    },
    "elements": []
}

title_h1_widget = {
    "id": "h01titl",
    "elType": "widget",
    "widgetType": "heading",
    "settings": {
        "title": "Descubre nuestros paquetes corporativos y pedidos especiales",
        "header_size": "h1",
        "title_color": "#FFFFFF",
        "typography_typography": "custom",
        "typography_font_family": "Open Sans",
        "typography_font_size": {
            "unit": "px",
            "size": 42,
            "sizes": []
        },
        "typography_font_size_mobile": {
            "unit": "px",
            "size": 25,
            "sizes": []
        },
        "typography_font_weight": "900",
        "typography_line_height": {
            "unit": "em",
            "size": 1.15,
            "sizes": []
        },
        "typography_letter_spacing": {
            "unit": "px",
            "size": -0.5,
            "sizes": []
        },
        "width": {
            "unit": "%",
            "size": 100,
            "sizes": []
        },
        "max_width": {
            "unit": "px",
            "size": 680,
            "sizes": []
        },
        "max_width_mobile": {
            "unit": "%",
            "size": 100,
            "sizes": []
        },
        "margin": {
            "unit": "px",
            "top": "0",
            "right": "0",
            "bottom": "24",
            "left": "0",
            "isLinked": False
        },
        "margin_mobile": {
            "unit": "px",
            "top": "0",
            "right": "0",
            "bottom": "20",
            "left": "0",
            "isLinked": False
        },
        "text_shadow_text_shadow_type": "yes",
        "text_shadow_text_shadow": {
            "horizontal": 0,
            "vertical": 2,
            "blur": 8,
            "color": "rgba(0, 0, 0, 0.5)"
        }
    },
    "elements": []
}

buttons_container = {
    "id": "h01btns",
    "elType": "container",
    "settings": {
        "content_width": "full",
        "flex_direction": "row",
        "flex_direction_mobile": "column",
        "flex_justify_content": "flex-start",
        "flex_align_items": "center",
        "flex_align_items_mobile": "stretch",
        "flex_gap": {
            "unit": "px",
            "size": 16,
            "sizes": []
        },
        "flex_gap_mobile": {
            "unit": "px",
            "size": 12,
            "sizes": []
        },
        "margin": {
            "unit": "px",
            "top": "0",
            "right": "0",
            "bottom": "0",
            "left": "0",
            "isLinked": False
        }
    },
    "elements": [
        {
            "id": "h01btn1",
            "elType": "widget",
            "widgetType": "button",
            "settings": {
                "text": "Cotiza aquí",
                "align": "left",
                "align_mobile": "justify",
                "link": {
                    "url": "https://wa.me/50762345678?text=Hola%20Eat%26Go,%20quiero%20cotizar%20paquetes%20corporativos%20y%20pedidos%20especiales",
                    "is_external": "true",
                    "nofollow": "",
                    "custom_attributes": ""
                },
                "selected_icon": {
                    "value": "fas fa-paper-plane",
                    "library": "fa-solid"
                },
                "icon_align": "right",
                "icon_indent": {
                    "unit": "px",
                    "size": 8,
                    "sizes": []
                },
                "typography_typography": "custom",
                "typography_font_family": "Open Sans",
                "typography_font_size": {
                    "unit": "px",
                    "size": 15,
                    "sizes": []
                },
                "typography_font_weight": "800",
                "button_text_color": "#FFFFFF",
                "background_color": "#C81C20",
                "hover_color": "#FFFFFF",
                "button_background_hover_color": "#A81518",
                "border_radius": {
                    "unit": "px",
                    "top": "50",
                    "right": "50",
                    "bottom": "50",
                    "left": "50",
                    "isLinked": True
                },
                "button_padding": {
                    "unit": "px",
                    "top": "14",
                    "right": "32",
                    "bottom": "14",
                    "left": "32",
                    "isLinked": False
                },
                "button_padding_mobile": {
                    "unit": "px",
                    "top": "13",
                    "right": "24",
                    "bottom": "13",
                    "left": "24",
                    "isLinked": False
                },
                "button_box_shadow_box_shadow_type": "yes",
                "button_box_shadow_box_shadow": {
                    "horizontal": 0,
                    "vertical": 4,
                    "blur": 16,
                    "spread": 0,
                    "color": "rgba(200, 28, 32, 0.45)"
                }
            },
            "elements": []
        },
        {
            "id": "h01btn2",
            "elType": "widget",
            "widgetType": "button",
            "settings": {
                "text": "Ver menú",
                "align": "left",
                "align_mobile": "justify",
                "link": {
                    "url": "/menu-del-dia/",
                    "is_external": "",
                    "nofollow": "",
                    "custom_attributes": ""
                },
                "typography_typography": "custom",
                "typography_font_family": "Open Sans",
                "typography_font_size": {
                    "unit": "px",
                    "size": 15,
                    "sizes": []
                },
                "typography_font_weight": "700",
                "button_text_color": "#FFFFFF",
                "background_color": "transparent",
                "hover_color": "#FFFFFF",
                "button_background_hover_color": "rgba(255, 255, 255, 0.12)",
                "border_border": "solid",
                "border_width": {
                    "unit": "px",
                    "top": "1.5",
                    "right": "1.5",
                    "bottom": "1.5",
                    "left": "1.5",
                    "isLinked": True
                },
                "border_color": "rgba(255, 255, 255, 0.6)",
                "border_hover_color": "#FFFFFF",
                "border_radius": {
                    "unit": "px",
                    "top": "50",
                    "right": "50",
                    "bottom": "50",
                    "left": "50",
                    "isLinked": True
                },
                "button_padding": {
                    "unit": "px",
                    "top": "14",
                    "right": "28",
                    "bottom": "14",
                    "left": "28",
                    "isLinked": False
                },
                "button_padding_mobile": {
                    "unit": "px",
                    "top": "13",
                    "right": "24",
                    "bottom": "13",
                    "left": "24",
                    "isLinked": False
                }
            },
            "elements": []
        }
    ]
}

inner_hero_container = {
    "id": "c00hero",
    "elType": "container",
    "settings": {
        "content_width": "boxed",
        "boxed_width": {
            "unit": "px",
            "size": 1320
        },
        "flex_direction": "column",
        "flex_justify_content": "center",
        "flex_align_items": "flex-start",
        "flex_gap": {
            "unit": "px",
            "size": 0
        },
        "padding": {
            "unit": "px",
            "top": "80",
            "right": "32",
            "bottom": "80",
            "left": "32",
            "isLinked": False
        },
        "padding_mobile": {
            "unit": "px",
            "top": "48",
            "right": "20",
            "bottom": "48",
            "left": "20",
            "isLinked": False
        },
        "custom_css": "@media (max-width: 767px) { selector .elementor-element-h01titl { max-width: 330px !important; width: 100% !important; } selector .elementor-element-h01titl .elementor-heading-title { word-break: normal !important; overflow-wrap: normal !important; hyphens: none !important; -webkit-hyphens: none !important; } selector .elementor-element-h01btns { width: 100% !important; } selector .elementor-element-h01btns .elementor-button { width: 100% !important; justify-content: center !important; } }"
    },
    "elements": [
        badge_widget,
        title_h1_widget,
        buttons_container
    ]
}

hero_container_settings = {
    "content_width": "full",
    "min_height": {
        "unit": "vh",
        "size": 75,
        "sizes": []
    },
    "min_height_tablet": {
        "unit": "vh",
        "size": "",
        "sizes": []
    },
    "min_height_mobile": {
        "unit": "vh",
        "size": 75,
        "sizes": []
    },
    "background_background": "video",
    "background_video_link": "https://eatgopty.com/wp-content/uploads/2026/10/header-menu.mp4",
    "background_overlay_background": "gradient",
    "background_overlay_color": "#000000",
    "background_overlay_color_stop": {
        "unit": "%",
        "size": 20,
        "sizes": []
    },
    "background_overlay_color_b": "rgba(0, 0, 0, 0)",
    "background_overlay_color_b_stop": {
        "unit": "%",
        "size": 85,
        "sizes": []
    },
    "background_overlay_gradient_type": "linear",
    "background_overlay_gradient_angle": {
        "unit": "deg",
        "size": 90,
        "sizes": []
    },
    "background_overlay_opacity": {
        "unit": "px",
        "size": 0.85,
        "sizes": []
    },
    "flex_direction": "column",
    "flex_justify_content": "center",
    "flex_align_items": "center",
    "padding": {
        "unit": "px",
        "top": "0",
        "right": "0",
        "bottom": "0",
        "left": "0",
        "isLinked": True
    }
}

# Attach to el_data[0]['elements'][0] (which is container 94b251e)
hero_node = el_data[0]['elements'][0]
hero_node['settings'] = hero_container_settings
hero_node['elements'] = [inner_hero_container]

# Save updated JSON
updated_elementor_data = json.dumps(el_data)

payload = json.dumps({
    'meta': {
        '_elementor_data': updated_elementor_data,
        '_elementor_edit_mode': 'builder'
    }
}).encode('utf-8')

req_up = urllib.request.Request(
    'https://eatgopty.com/wp-json/wp/v2/pages/58',
    data=payload,
    headers={
        'Authorization': f'Basic {auth}',
        'Content-Type': 'application/json'
    },
    method='POST'
)

with urllib.request.urlopen(req_up) as resp:
    res = json.loads(resp.read().decode('utf-8'))
    print("Page 58 successfully updated! Status:", resp.status)
