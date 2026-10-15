import json

elements = [
  {
    "id": "c01root",
    "elType": "container",
    "settings": {
      "content_width": "full",
      "flex_direction": "column",
      "background_background": "classic",
      "background_color": "#FFFFFF",
      "border_border": "solid",
      "border_width": {
        "unit": "px",
        "top": "1",
        "right": "1",
        "bottom": "1",
        "left": "1",
        "isLinked": True
      },
      "border_color": "#E5E7EB",
      "border_radius": {
        "unit": "px",
        "top": "24",
        "right": "24",
        "bottom": "24",
        "left": "24",
        "isLinked": True
      },
      "overflow": "hidden",
      "padding": {
        "unit": "px",
        "top": "0",
        "right": "0",
        "bottom": "0",
        "left": "0",
        "isLinked": True
      },
      "box_shadow_box_shadow_type": "yes",
      "box_shadow_box_shadow": {
        "horizontal": 0,
        "vertical": 4,
        "blur": 16,
        "spread": 0,
        "color": "rgba(0,0,0,0.05)"
      }
    },
    "elements": [
      {
        "id": "c02covr",
        "elType": "container",
        "settings": {
          "content_width": "full",
          "min_height": {
            "unit": "px",
            "size": 220
          },
          "flex_direction": "column",
          "flex_justify_content": "space-between",
          "padding": {
            "unit": "px",
            "top": "12",
            "right": "12",
            "bottom": "12",
            "left": "12",
            "isLinked": True
          },
          "background_background": "classic",
          "background_image": {
            "url": "",
            "id": "",
            "__dynamic__": {
              "url": '[elementor-tag id="eg_bg_feat_img" name="post-featured-image" settings="%7B%7D"]'
            }
          },
          "background_position": "center center",
          "background_size": "cover",
          "background_repeat": "no-repeat"
        },
        "elements": [
          {
            "id": "c03bgtop",
            "elType": "container",
            "settings": {
              "content_width": "full",
              "flex_direction": "row",
              "flex_justify_content": "space-between",
              "flex_align_items": "center",
              "width": {
                "unit": "%",
                "size": 100
              }
            },
            "elements": [
              {
                "id": "w04bstar",
                "elType": "widget",
                "widgetType": "text-editor",
                "settings": {
                  "editor": '<div style="display:inline-block;background:#18181B;color:#FACC15;font-family:\'Open Sans\',sans-serif;font-size:10px;font-weight:800;letter-spacing:0.5px;padding:4px 10px;border-radius:50px;text-transform:uppercase;">PLATO ESTRELLA</div>'
                }
              },
              {
                "id": "w05bpric",
                "elType": "widget",
                "widgetType": "heading",
                "settings": {
                  "title": "$6.50",
                  "__dynamic__": {
                    "title": '[elementor-tag id="eg_dyn_price" name="woocommerce-product-price-tag" settings="%7B%22before%22%3A%22%22%7D"]'
                  },
                  "header_size": "div",
                  "title_color": "#18181B",
                  "typography_typography": "custom",
                  "typography_font_family": "Open Sans",
                  "typography_font_size": {
                    "unit": "px",
                    "size": 13
                  },
                  "typography_font_weight": "800",
                  "_background_background": "classic",
                  "_background_color": "#FFFFFF",
                  "_border_radius": {
                    "unit": "px",
                    "top": "50",
                    "right": "50",
                    "bottom": "50",
                    "left": "50",
                    "isLinked": True
                  },
                  "_padding": {
                    "unit": "px",
                    "top": "4",
                    "right": "12",
                    "bottom": "4",
                    "left": "12",
                    "isLinked": False
                  },
                  "_box_shadow_box_shadow_type": "yes",
                  "_box_shadow_box_shadow": {
                    "horizontal": 0,
                    "vertical": 2,
                    "blur": 4,
                    "spread": 0,
                    "color": "rgba(0,0,0,0.12)"
                  }
                }
              }
            ]
          },
          {
            "id": "c06bgbtm",
            "elType": "container",
            "settings": {
              "content_width": "full",
              "flex_direction": "row",
              "flex_justify_content": "flex-end",
              "flex_align_items": "center",
              "width": {
                "unit": "%",
                "size": 100
              }
            },
            "elements": [
              {
                "id": "w07bbox",
                "elType": "widget",
                "widgetType": "text-editor",
                "settings": {
                  "editor": '<div style="display:inline-flex;align-items:center;gap:4px;background:rgba(24,24,27,0.85);backdrop-filter:blur(4px);color:#FFFFFF;font-family:\'Open Sans\',sans-serif;font-size:11px;font-weight:700;padding:4px 8px;border-radius:6px;">📦 Ver en Caja 75°C</div>'
                }
              }
            ]
          }
        ]
      },
      {
        "id": "c08body",
        "elType": "container",
        "settings": {
          "content_width": "full",
          "flex_direction": "column",
          "padding": {
            "unit": "px",
            "top": "18",
            "right": "18",
            "bottom": "18",
            "left": "18",
            "isLinked": True
          },
          "flex_gap": {
            "unit": "px",
            "size": 10
          }
        },
        "elements": [
          {
            "id": "w09titl",
            "elType": "widget",
            "widgetType": "heading",
            "settings": {
              "title": "Sancocho Tradicional de Gallina de Patio",
              "__dynamic__": {
                "title": '[elementor-tag id="eg_dyn_title" name="post-title" settings="%7B%22fallback%22%3A%22Nombre del Plato%22%7D"]'
              },
              "header_size": "h3",
              "title_color": "#18181B",
              "typography_typography": "custom",
              "typography_font_family": "Open Sans",
              "typography_font_size": {
                "unit": "px",
                "size": 17
              },
              "typography_font_weight": "800",
              "typography_line_height": {
                "unit": "em",
                "size": 1.25
              }
            }
          },
          {
            "id": "w10desc",
            "elType": "widget",
            "widgetType": "text-editor",
            "settings": {
              "editor": "El rey indiscutible de Panamá: caldo espeso con ñame baboso, gallina suave y abundante culantro fresco cosechado.",
              "__dynamic__": {
                "editor": '[elementor-tag id="eg_dyn_desc" name="post-excerpt" settings="%7B%22fallback%22%3A%22Delicioso plato tradicional panameño preparado al momento.%22%7D"]'
              },
              "text_color": "#6B7280",
              "typography_typography": "custom",
              "typography_font_family": "Open Sans",
              "typography_font_size": {
                "unit": "px",
                "size": 12
              },
              "typography_line_height": {
                "unit": "em",
                "size": 1.45
              }
            }
          },
          {
            "id": "w11divd",
            "elType": "widget",
            "widgetType": "divider",
            "settings": {
              "color": "#F3F4F6",
              "weight": {
                "unit": "px",
                "size": 1
              },
              "gap": {
                "unit": "px",
                "size": 2
              }
            }
          },
          {
            "id": "w12lbls",
            "elType": "widget",
            "widgetType": "heading",
            "settings": {
              "title": "Acompañamiento a tu gusto:",
              "header_size": "div",
              "title_color": "#374151",
              "typography_typography": "custom",
              "typography_font_family": "Open Sans",
              "typography_font_size": {
                "unit": "px",
                "size": 11
              },
              "typography_font_weight": "700"
            }
          },
          {
            "id": "w13boxs",
            "elType": "widget",
            "widgetType": "text-editor",
            "settings": {
              "editor": '<div style="display:flex;align-items:center;justify-content:space-between;background:#FFFFFF;border:1px solid #E5E7EB;border-radius:12px;padding:9px 12px;font-family:\'Open Sans\',sans-serif;font-size:12px;font-weight:600;color:#18181B;"><span>Arroz Blanco Criollo</span><span style="color:#9CA3AF;font-size:12px;">⌵</span></div>'
            }
          },
          {
            "id": "w14btna",
            "elType": "widget",
            "widgetType": "button",
            "settings": {
              "text": "🛍️ + Agregar al Pedido",
              "link": {
                "url": "#",
                "is_external": False,
                "nofollow": False,
                "custom_attributes": 'data-id|[elementor-tag id="eg_pid" name="post-id"]'
              },
              "align": "justify",
              "button_text_color": "#000000",
              "background_color": "#F59E0B",
              "border_radius": {
                "unit": "px",
                "top": "50",
                "right": "50",
                "bottom": "50",
                "left": "50",
                "isLinked": True
              },
              "typography_typography": "custom",
              "typography_font_family": "Open Sans",
              "typography_font_weight": "800",
              "typography_font_size": {
                "unit": "px",
                "size": 14
              },
              "text_padding": {
                "unit": "px",
                "top": "12",
                "right": "20",
                "bottom": "12",
                "left": "20",
                "isLinked": False
              },
              "_css_classes": "woosq-btn",
              "custom_attributes": 'data-id|[elementor-tag id="eg_pid" name="post-id"]'
            }
          },
          {
            "id": "w15btnw",
            "elType": "widget",
            "widgetType": "button",
            "settings": {
              "text": "✈️ Planificar para este día por WhatsApp",
              "link": {
                "url": "https://wa.me/50762345678",
                "is_external": True,
                "nofollow": False
              },
              "align": "justify",
              "button_text_color": "#18181B",
              "background_color": "#F4F4F5",
              "border_border": "solid",
              "border_width": {
                "unit": "px",
                "top": "1",
                "right": "1",
                "bottom": "1",
                "left": "1",
                "isLinked": True
              },
              "border_color": "#E5E7EB",
              "border_radius": {
                "unit": "px",
                "top": "50",
                "right": "50",
                "bottom": "50",
                "left": "50",
                "isLinked": True
              },
              "typography_typography": "custom",
              "typography_font_family": "Open Sans",
              "typography_font_weight": "700",
              "typography_font_size": {
                "unit": "px",
                "size": 12.5
              },
              "text_padding": {
                "unit": "px",
                "top": "10",
                "right": "16",
                "bottom": "10",
                "left": "16",
                "isLinked": False
              }
            }
          }
        ]
      }
    ]
  }
]

with open("template_631_data.json", "w") as f:
    json.dump(elements, f)

print("Generated template_631_data.json with", len(elements), "root elements.")
