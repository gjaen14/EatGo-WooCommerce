import json
import urllib.request

structure = {
  'version': '0.4',
  'title': 'Dónde Comer y Retirar - Eat&Go',
  'type': 'page',
  'content': [
    {
      'id': 'maincon',
      'elType': 'container',
      'settings': {
        'content_width': 'boxed',
        'boxed_width': {'unit': 'px', 'size': 1280},
        'flex_direction': 'row',
        'flex_justify_content': 'center',
        'flex_align_items': 'stretch',
        'flex_gap': {'unit': 'px', 'size': 32},
        'flex_direction_mobile': 'column',
        'flex_gap_mobile': {'unit': 'px', 'size': 24},
        'padding': {'unit': 'px', 'top': '60', 'right': '20', 'bottom': '60', 'left': '20', 'isLinked': False},
        'padding_mobile': {'unit': 'px', 'top': '40', 'right': '16', 'bottom': '40', 'left': '16', 'isLinked': False}
      },
      'elements': [
        # TARJETA IZQUIERDA
        {
          'id': 'cleft01',
          'elType': 'container',
          'settings': {
            'content_width': 'full',
            'width': {'unit': '%', 'size': 50},
            'width_mobile': {'unit': '%', 'size': 100},
            'flex_direction': 'column',
            'flex_justify_content': 'space-between',
            'padding': {'unit': 'px', 'top': '40', 'right': '36', 'bottom': '40', 'left': '36', 'isLinked': False},
            'padding_mobile': {'unit': 'px', 'top': '32', 'right': '20', 'bottom': '32', 'left': '20', 'isLinked': False},
            'background_background': 'classic',
            'background_color': '#FFFFFF',
            'border_border': 'solid',
            'border_width': {'unit': 'px', 'top': '1', 'right': '1', 'bottom': '1', 'left': '1', 'isLinked': True},
            'border_color': '#E5E7EB',
            'border_radius': {'unit': 'px', 'top': '28', 'right': '28', 'bottom': '28', 'left': '28', 'isLinked': True},
            'box_shadow_box_shadow_type': 'yes',
            'box_shadow_box_shadow': {'horizontal': 0, 'vertical': 10, 'blur': 30, 'spread': 0, 'color': 'rgba(0,0,0,0.04)'}
          },
          'elements': [
            # BLOQUE SUPERIOR
            {
              'id': 'cltop01',
              'elType': 'container',
              'settings': {
                'content_width': 'full',
                'flex_direction': 'column',
                'flex_align_items': 'flex-start'
              },
              'elements': [
                # Icono Tenedor/Cuchillo
                {
                  'id': 'clicn01',
                  'elType': 'container',
                  'settings': {
                    'content_width': 'full',
                    'width': {'unit': 'px', 'size': 48},
                    'custom_width': {'unit': 'px', 'size': 48},
                    'min_height': {'unit': 'px', 'size': 48},
                    'height': {'unit': 'px', 'size': 48},
                    'flex_shrink': 0,
                    'background_background': 'classic',
                    'background_color': '#FFFBEB',
                    'border_radius': {'unit': 'px', 'top': '14', 'right': '14', 'bottom': '14', 'left': '14', 'isLinked': True},
                    'flex_direction': 'row',
                    'flex_justify_content': 'center',
                    'flex_align_items': 'center',
                    'padding': {'unit': 'px', 'top': '0', 'right': '0', 'bottom': '0', 'left': '0', 'isLinked': True}
                  },
                  'elements': [
                    {
                      'id': 'clicw01',
                      'elType': 'widget',
                      'widgetType': 'icon',
                      'settings': {
                        'selected_icon': {'value': 'fas fa-utensils', 'library': 'fa-solid'},
                        'primary_color': '#D97706',
                        'size': {'unit': 'px', 'size': 22}
                      }
                    }
                  ]
                },
                # Fila de Badges
                {
                  'id': 'clrow01',
                  'elType': 'container',
                  'settings': {
                    'content_width': 'full',
                    'flex_direction': 'row',
                    'flex_align_items': 'center',
                    'flex_gap': {'unit': 'px', 'size': 10},
                    'margin': {'unit': 'px', 'top': '16', 'right': '0', 'bottom': '12', 'left': '0', 'isLinked': False}
                  },
                  'elements': [
                    {
                      'id': 'clbdg01',
                      'elType': 'container',
                      'settings': {
                        'background_background': 'classic',
                        'background_color': '#FEF3C7',
                        'border_radius': {'unit': 'px', 'top': '50', 'right': '50', 'bottom': '50', 'left': '50', 'isLinked': True},
                        'padding': {'unit': 'px', 'top': '4', 'right': '12', 'bottom': '4', 'left': '12', 'isLinked': False}
                      },
                      'elements': [
                        {
                          'id': 'clbdt01',
                          'elType': 'widget',
                          'widgetType': 'heading',
                          'settings': {
                            'title': 'OPCIÓN PRESENCIAL',
                            'header_size': 'span',
                            'title_color': '#92400E',
                            'typography_typography': 'custom',
                            'typography_font_family': 'Open Sans',
                            'typography_font_size': {'unit': 'px', 'size': 11},
                            'typography_font_weight': '700',
                            'typography_letter_spacing': {'unit': 'px', 'size': 0.5}
                          }
                        }
                      ]
                    },
                    {
                      'id': 'cltxt01',
                      'elType': 'widget',
                      'widgetType': 'heading',
                      'settings': {
                        'title': 'Salón Climatizado',
                        'header_size': 'span',
                        'title_color': '#6B7280',
                        'typography_typography': 'custom',
                        'typography_font_family': 'Open Sans',
                        'typography_font_size': {'unit': 'px', 'size': 13},
                        'typography_font_weight': '500'
                      }
                    }
                  ]
                },
                # H2
                {
                  'id': 'clh201',
                  'elType': 'widget',
                  'widgetType': 'heading',
                  'settings': {
                    'title': 'Visítanos en Nuestro Comedor',
                    'header_size': 'h2',
                    'title_color': '#18181B',
                    'typography_typography': 'custom',
                    'typography_font_family': 'Open Sans',
                    'typography_font_size': {'unit': 'px', 'size': 28},
                    'typography_font_weight': '900',
                    'typography_line_height': {'unit': 'em', 'size': 1.2},
                    'margin': {'unit': 'px', 'top': '0', 'right': '0', 'bottom': '12', 'left': '0', 'isLinked': False}
                  }
                },
                # Párrafo
                {
                  'id': 'clp01',
                  'elType': 'widget',
                  'widgetType': 'text-editor',
                  'settings': {
                    'editor': '<p style=\"margin:0;\">Un espacio moderno, limpio y con aire acondicionado diseñado para que los colaboradores y ejecutivos de la Zona Bancaria almuercen cómodamente paila criolla servida al momento.</p>',
                    'text_color': '#4B5563',
                    'typography_typography': 'custom',
                    'typography_font_family': 'Open Sans',
                    'typography_font_size': {'unit': 'px', 'size': 14},
                    'typography_line_height': {'unit': 'em', 'size': 1.6},
                    'margin': {'unit': 'px', 'top': '0', 'right': '0', 'bottom': '24', 'left': '0', 'isLinked': False}
                  }
                },
                # Checklist icon-list
                {
                  'id': 'cllst01',
                  'elType': 'widget',
                  'widgetType': 'icon-list',
                  'settings': {
                    'icon_align': 'left',
                    'space_between': {'unit': 'px', 'size': 12},
                    'icon_color': '#10B981',
                    'icon_size': {'unit': 'px', 'size': 16},
                    'text_color': '#374151',
                    'typography_typography': 'custom',
                    'typography_font_family': 'Open Sans',
                    'typography_font_size': {'unit': 'px', 'size': 13.5},
                    'typography_line_height': {'unit': 'em', 'size': 1.5},
                    'icon_list': [
                      {
                        'text': '<b>Horario de Almuerzos:</b> Lunes a Viernes 11:30 AM a 3:30 PM',
                        'selected_icon': {'value': 'fas fa-check-circle', 'library': 'fa-solid'}
                      },
                      {
                        'text': '<b>Horario de Desayunos:</b> Lunes a Sábado 6:30 AM a 11:00 AM',
                        'selected_icon': {'value': 'fas fa-check-circle', 'library': 'fa-solid'}
                      },
                      {
                        'text': '<b>Mesas individuales y grupales</b> con servicio rápido de paila.',
                        'selected_icon': {'value': 'fas fa-check-circle', 'library': 'fa-solid'}
                      },
                      {
                        'text': '<b>Wi-Fi gratuito</b> y tomas de corriente en barra para laptop.',
                        'selected_icon': {'value': 'fas fa-check-circle', 'library': 'fa-solid'}
                      }
                    ]
                  }
                }
              ]
            },
            # BLOQUE INFERIOR (Botón Maps)
            {
              'id': 'clbtn01',
              'elType': 'widget',
              'widgetType': 'button',
              'settings': {
                'text': '🧭 Cómo Llegar al Comedor (Google Maps)',
                'link': {'url': 'https://maps.google.com/?q=Calle+50+Obarrio+Panama', 'is_external': True, 'nofollow': False},
                'button_type': 'default',
                'align': 'justify',
                'background_color': '#18181B',
                'button_text_color': '#FFFFFF',
                'button_background_hover_color': '#27272A',
                'hover_color': '#FFFFFF',
                'typography_typography': 'custom',
                'typography_font_family': 'Open Sans',
                'typography_font_size': {'unit': 'px', 'size': 14},
                'typography_font_weight': '700',
                'border_radius': {'unit': 'px', 'top': '14', 'right': '14', 'bottom': '14', 'left': '14', 'isLinked': True},
                'padding': {'unit': 'px', 'top': '15', 'right': '24', 'bottom': '15', 'left': '24', 'isLinked': False},
                'margin': {'unit': 'px', 'top': '32', 'right': '0', 'bottom': '0', 'left': '0', 'isLinked': False}
              }
            }
          ]
        },
        # TARJETA DERECHA
        {
          'id': 'crigh01',
          'elType': 'container',
          'settings': {
            'content_width': 'full',
            'width': {'unit': '%', 'size': 50},
            'width_mobile': {'unit': '%', 'size': 100},
            'flex_direction': 'column',
            'flex_justify_content': 'space-between',
            'padding': {'unit': 'px', 'top': '40', 'right': '36', 'bottom': '40', 'left': '36', 'isLinked': False},
            'padding_mobile': {'unit': 'px', 'top': '32', 'right': '20', 'bottom': '32', 'left': '20', 'isLinked': False},
            'background_background': 'classic',
            'background_color': '#FFFFFF',
            'border_border': 'solid',
            'border_width': {'unit': 'px', 'top': '2', 'right': '2', 'bottom': '2', 'left': '2', 'isLinked': True},
            'border_color': '#FDE68A',
            'border_radius': {'unit': 'px', 'top': '28', 'right': '28', 'bottom': '28', 'left': '28', 'isLinked': True},
            'box_shadow_box_shadow_type': 'yes',
            'box_shadow_box_shadow': {'horizontal': 0, 'vertical': 10, 'blur': 30, 'spread': 0, 'color': 'rgba(0,0,0,0.04)'}
          },
          'elements': [
            # BLOQUE SUPERIOR
            {
              'id': 'crtop01',
              'elType': 'container',
              'settings': {
                'content_width': 'full',
                'flex_direction': 'column',
                'flex_align_items': 'flex-start'
              },
              'elements': [
                # Icono Paquete/Caja
                {
                  'id': 'cricn01',
                  'elType': 'container',
                  'settings': {
                    'content_width': 'full',
                    'width': {'unit': 'px', 'size': 48},
                    'custom_width': {'unit': 'px', 'size': 48},
                    'min_height': {'unit': 'px', 'size': 48},
                    'height': {'unit': 'px', 'size': 48},
                    'flex_shrink': 0,
                    'background_background': 'classic',
                    'background_color': '#ECFDF5',
                    'border_radius': {'unit': 'px', 'top': '14', 'right': '14', 'bottom': '14', 'left': '14', 'isLinked': True},
                    'flex_direction': 'row',
                    'flex_justify_content': 'center',
                    'flex_align_items': 'center',
                    'padding': {'unit': 'px', 'top': '0', 'right': '0', 'bottom': '0', 'left': '0', 'isLinked': True}
                  },
                  'elements': [
                    {
                      'id': 'cricw01',
                      'elType': 'widget',
                      'widgetType': 'icon',
                      'settings': {
                        'selected_icon': {'value': 'fas fa-box-open', 'library': 'fa-solid'},
                        'primary_color': '#059669',
                        'size': {'unit': 'px', 'size': 22}
                      }
                    }
                  ]
                },
                # Fila de Badges
                {
                  'id': 'crrow01',
                  'elType': 'container',
                  'settings': {
                    'content_width': 'full',
                    'flex_direction': 'row',
                    'flex_align_items': 'center',
                    'flex_gap': {'unit': 'px', 'size': 10},
                    'margin': {'unit': 'px', 'top': '16', 'right': '0', 'bottom': '12', 'left': '0', 'isLinked': False}
                  },
                  'elements': [
                    {
                      'id': 'crbdg01',
                      'elType': 'container',
                      'settings': {
                        'background_background': 'classic',
                        'background_color': '#D1FAE5',
                        'border_radius': {'unit': 'px', 'top': '50', 'right': '50', 'bottom': '50', 'left': '50', 'isLinked': True},
                        'padding': {'unit': 'px', 'top': '4', 'right': '12', 'bottom': '4', 'left': '12', 'isLinked': False}
                      },
                      'elements': [
                        {
                          'id': 'crbdt01',
                          'elType': 'widget',
                          'widgetType': 'heading',
                          'settings': {
                            'title': 'RETIRO EXPRESS',
                            'header_size': 'span',
                            'title_color': '#065F46',
                            'typography_typography': 'custom',
                            'typography_font_family': 'Open Sans',
                            'typography_font_size': {'unit': 'px', 'size': 11},
                            'typography_font_weight': '700',
                            'typography_letter_spacing': {'unit': 'px', 'size': 0.5}
                          }
                        }
                      ]
                    },
                    {
                      'id': 'crtxt01',
                      'elType': 'widget',
                      'widgetType': 'heading',
                      'settings': {
                        'title': 'Listo en 10-15 min',
                        'header_size': 'span',
                        'title_color': '#6B7280',
                        'typography_typography': 'custom',
                        'typography_font_family': 'Open Sans',
                        'typography_font_size': {'unit': 'px', 'size': 13},
                        'typography_font_weight': '500'
                      }
                    }
                  ]
                },
                # H2
                {
                  'id': 'crh201',
                  'elType': 'widget',
                  'widgetType': 'heading',
                  'settings': {
                    'title': 'Mostrador Pick & Go (Cero Filas)',
                    'header_size': 'h2',
                    'title_color': '#18181B',
                    'typography_typography': 'custom',
                    'typography_font_family': 'Open Sans',
                    'typography_font_size': {'unit': 'px', 'size': 28},
                    'typography_font_weight': '900',
                    'typography_line_height': {'unit': 'em', 'size': 1.2},
                    'margin': {'unit': 'px', 'top': '0', 'right': '0', 'bottom': '12', 'left': '0', 'isLinked': False}
                  }
                },
                # Párrafo
                {
                  'id': 'crp01',
                  'elType': 'widget',
                  'widgetType': 'text-editor',
                  'settings': {
                    'editor': '<p style=\"margin:0;\">¿Poco tiempo de almuerzo? Pide desde tu celular antes de bajar del piso de tu oficina. Cuando llegues, tu comanda estará empacada y rotulada con tu nombre en el mostrador rápido.</p>',
                    'text_color': '#4B5563',
                    'typography_typography': 'custom',
                    'typography_font_family': 'Open Sans',
                    'typography_font_size': {'unit': 'px', 'size': 14},
                    'typography_line_height': {'unit': 'em', 'size': 1.6},
                    'margin': {'unit': 'px', 'top': '0', 'right': '0', 'bottom': '24', 'left': '0', 'isLinked': False}
                  }
                },
                # Contenedor de Pasos
                {
                  'id': 'crstp00',
                  'elType': 'container',
                  'settings': {
                    'content_width': 'full',
                    'flex_direction': 'column',
                    'flex_gap': {'unit': 'px', 'size': 10}
                  },
                  'elements': [
                    # Paso 1
                    {
                      'id': 'crstp01',
                      'elType': 'container',
                      'settings': {
                        'content_width': 'full',
                        'flex_direction': 'row',
                        'flex_align_items': 'center',
                        'flex_gap': {'unit': 'px', 'size': 14},
                        'background_background': 'classic',
                        'background_color': '#FFFFFF',
                        'border_border': 'solid',
                        'border_width': {'unit': 'px', 'top': '1', 'right': '1', 'bottom': '1', 'left': '1', 'isLinked': True},
                        'border_color': '#E5E7EB',
                        'border_radius': {'unit': 'px', 'top': '14', 'right': '14', 'bottom': '14', 'left': '14', 'isLinked': True},
                        'padding': {'unit': 'px', 'top': '12', 'right': '16', 'bottom': '12', 'left': '16', 'isLinked': False}
                      },
                      'elements': [
                        {
                          'id': 'crcir01',
                          'elType': 'container',
                          'settings': {
                            'content_width': 'full',
                            'width': {'unit': 'px', 'size': 30},
                            'custom_width': {'unit': 'px', 'size': 30},
                            'min_height': {'unit': 'px', 'size': 30},
                            'height': {'unit': 'px', 'size': 30},
                            'flex_shrink': 0,
                            'border_radius': {'unit': 'px', 'top': '50', 'right': '50', 'bottom': '50', 'left': '50', 'isLinked': True},
                            'background_background': 'classic',
                            'background_color': '#F59E0B',
                            'flex_direction': 'row',
                            'flex_justify_content': 'center',
                            'flex_align_items': 'center',
                            'padding': {'unit': 'px', 'top': '0', 'right': '0', 'bottom': '0', 'left': '0', 'isLinked': True}
                          },
                          'elements': [
                            {
                              'id': 'crnum01',
                              'elType': 'widget',
                              'widgetType': 'heading',
                              'settings': {
                                'title': '1',
                                'header_size': 'span',
                                'title_color': '#FFFFFF',
                                'typography_typography': 'custom',
                                'typography_font_family': 'Open Sans',
                                'typography_font_size': {'unit': 'px', 'size': 14},
                                'typography_font_weight': '800',
                                'align': 'center'
                              }
                            }
                          ]
                        },
                        {
                          'id': 'crtxt11',
                          'elType': 'widget',
                          'widgetType': 'text-editor',
                          'settings': {
                            'editor': '<p style=\"margin:0;\"><b>Pides por la Web o WhatsApp:</b> Indicas retiro Pick &amp; Go y tu nombre.</p>',
                            'text_color': '#374151',
                            'typography_typography': 'custom',
                            'typography_font_family': 'Open Sans',
                            'typography_font_size': {'unit': 'px', 'size': 13},
                            'typography_line_height': {'unit': 'em', 'size': 1.4}
                          }
                        }
                      ]
                    },
                    # Paso 2
                    {
                      'id': 'crstp02',
                      'elType': 'container',
                      'settings': {
                        'content_width': 'full',
                        'flex_direction': 'row',
                        'flex_align_items': 'center',
                        'flex_gap': {'unit': 'px', 'size': 14},
                        'background_background': 'classic',
                        'background_color': '#FFFFFF',
                        'border_border': 'solid',
                        'border_width': {'unit': 'px', 'top': '1', 'right': '1', 'bottom': '1', 'left': '1', 'isLinked': True},
                        'border_color': '#E5E7EB',
                        'border_radius': {'unit': 'px', 'top': '14', 'right': '14', 'bottom': '14', 'left': '14', 'isLinked': True},
                        'padding': {'unit': 'px', 'top': '12', 'right': '16', 'bottom': '12', 'left': '16', 'isLinked': False}
                      },
                      'elements': [
                        {
                          'id': 'crcir02',
                          'elType': 'container',
                          'settings': {
                            'content_width': 'full',
                            'width': {'unit': 'px', 'size': 30},
                            'custom_width': {'unit': 'px', 'size': 30},
                            'min_height': {'unit': 'px', 'size': 30},
                            'height': {'unit': 'px', 'size': 30},
                            'flex_shrink': 0,
                            'border_radius': {'unit': 'px', 'top': '50', 'right': '50', 'bottom': '50', 'left': '50', 'isLinked': True},
                            'background_background': 'classic',
                            'background_color': '#F59E0B',
                            'flex_direction': 'row',
                            'flex_justify_content': 'center',
                            'flex_align_items': 'center',
                            'padding': {'unit': 'px', 'top': '0', 'right': '0', 'bottom': '0', 'left': '0', 'isLinked': True}
                          },
                          'elements': [
                            {
                              'id': 'crnum02',
                              'elType': 'widget',
                              'widgetType': 'heading',
                              'settings': {
                                'title': '2',
                                'header_size': 'span',
                                'title_color': '#FFFFFF',
                                'typography_typography': 'custom',
                                'typography_font_family': 'Open Sans',
                                'typography_font_size': {'unit': 'px', 'size': 14},
                                'typography_font_weight': '800',
                                'align': 'center'
                              }
                            }
                          ]
                        },
                        {
                          'id': 'crtxt12',
                          'elType': 'widget',
                          'widgetType': 'text-editor',
                          'settings': {
                            'editor': '<p style=\"margin:0;\"><b>Empacamos a 75°C:</b> En bolsa térmica sellada para mantener el calor.</p>',
                            'text_color': '#374151',
                            'typography_typography': 'custom',
                            'typography_font_family': 'Open Sans',
                            'typography_font_size': {'unit': 'px', 'size': 13},
                            'typography_line_height': {'unit': 'em', 'size': 1.4}
                          }
                        }
                      ]
                    },
                    # Paso 3
                    {
                      'id': 'crstp03',
                      'elType': 'container',
                      'settings': {
                        'content_width': 'full',
                        'flex_direction': 'row',
                        'flex_align_items': 'center',
                        'flex_gap': {'unit': 'px', 'size': 14},
                        'background_background': 'classic',
                        'background_color': '#FFFFFF',
                        'border_border': 'solid',
                        'border_width': {'unit': 'px', 'top': '1', 'right': '1', 'bottom': '1', 'left': '1', 'isLinked': True},
                        'border_color': '#E5E7EB',
                        'border_radius': {'unit': 'px', 'top': '14', 'right': '14', 'bottom': '14', 'left': '14', 'isLinked': True},
                        'padding': {'unit': 'px', 'top': '12', 'right': '16', 'bottom': '12', 'left': '16', 'isLinked': False}
                      },
                      'elements': [
                        {
                          'id': 'crcir03',
                          'elType': 'container',
                          'settings': {
                            'content_width': 'full',
                            'width': {'unit': 'px', 'size': 30},
                            'custom_width': {'unit': 'px', 'size': 30},
                            'min_height': {'unit': 'px', 'size': 30},
                            'height': {'unit': 'px', 'size': 30},
                            'flex_shrink': 0,
                            'border_radius': {'unit': 'px', 'top': '50', 'right': '50', 'bottom': '50', 'left': '50', 'isLinked': True},
                            'background_background': 'classic',
                            'background_color': '#F59E0B',
                            'flex_direction': 'row',
                            'flex_justify_content': 'center',
                            'flex_align_items': 'center',
                            'padding': {'unit': 'px', 'top': '0', 'right': '0', 'bottom': '0', 'left': '0', 'isLinked': True}
                          },
                          'elements': [
                            {
                              'id': 'crnum03',
                              'elType': 'widget',
                              'widgetType': 'heading',
                              'settings': {
                                'title': '3',
                                'header_size': 'span',
                                'title_color': '#FFFFFF',
                                'typography_typography': 'custom',
                                'typography_font_family': 'Open Sans',
                                'typography_font_size': {'unit': 'px', 'size': 14},
                                'typography_font_weight': '800',
                                'align': 'center'
                              }
                            }
                          ]
                        },
                        {
                          'id': 'crtxt13',
                          'elType': 'widget',
                          'widgetType': 'text-editor',
                          'settings': {
                            'editor': '<p style=\"margin:0;\"><b>Llegas y retiras:</b> Muestras tu confirmación, tomas tu paquete y listo.</p>',
                            'text_color': '#374151',
                            'typography_typography': 'custom',
                            'typography_font_family': 'Open Sans',
                            'typography_font_size': {'unit': 'px', 'size': 13},
                            'typography_line_height': {'unit': 'em', 'size': 1.4}
                          }
                        }
                      ]
                    }
                  ]
                }
              ]
            },
            # BLOQUE INFERIOR (Botón WhatsApp)
            {
              'id': 'crbtn01',
              'elType': 'widget',
              'widgetType': 'button',
              'settings': {
                'text': '✈️ Pedir para Retiro Inmediato por WhatsApp',
                'link': {'url': 'https://wa.me/50762345678?text=Hola%20Eat%26Go,%20quiero%20hacer%20un%20pedido%20Pick%20%26%20Go%20para%20retirar', 'is_external': True, 'nofollow': False},
                'button_type': 'default',
                'align': 'justify',
                'background_color': '#059669',
                'button_text_color': '#FFFFFF',
                'button_background_hover_color': '#047857',
                'hover_color': '#FFFFFF',
                'typography_typography': 'custom',
                'typography_font_family': 'Open Sans',
                'typography_font_size': {'unit': 'px', 'size': 14},
                'typography_font_weight': '800',
                'border_radius': {'unit': 'px', 'top': '14', 'right': '14', 'bottom': '14', 'left': '14', 'isLinked': True},
                'padding': {'unit': 'px', 'top': '15', 'right': '24', 'bottom': '15', 'left': '24', 'isLinked': False},
                'margin': {'unit': 'px', 'top': '32', 'right': '0', 'bottom': '0', 'left': '0', 'isLinked': False}
              }
            }
          ]
        }
      ]
    }
  ]
}

# 1. Save local file
with open('pagina_donde_comer.json', 'w', encoding='utf-8') as f:
    json.dump(structure, f, indent=2, ensure_ascii=False)
print('1. Saved pagina_donde_comer.json')

# 2. Update WordPress Page 751
auth = 'Basic SmFlbkRldjo0bjNGS3kyNlNrQnB3ZThHUEJ6ZGJxRXo='
payload = {
    'template': 'elementor_header_footer',
    'meta': {
        '_elementor_edit_mode': 'builder',
        '_elementor_template_type': 'wp-page',
        '_elementor_data': json.dumps(structure['content'])
    }
}
req = urllib.request.Request('https://eatgopty.com/wp-json/wp/v2/pages/751',
    headers={'Authorization': auth, 'Content-Type': 'application/json'},
    data=json.dumps(payload).encode('utf-8'),
    method='POST'
)
with urllib.request.urlopen(req) as resp:
    res = json.loads(resp.read().decode('utf-8'))
print('2. Updated WordPress Page 751!')

# 3. Clear Elementor cache
del_req = urllib.request.Request('https://eatgopty.com/wp-json/elementor/v1/cache',
    headers={'Authorization': auth},
    method='DELETE'
)
with urllib.request.urlopen(del_req) as resp:
    print('3. Elementor cache cleared!')
