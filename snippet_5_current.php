/**
 * Plugin Name: Eat&Go Weekly Rotation Query Engine
 * Description: Motor de rotación semanal de menú y hooks de consulta para Loop Grids en Elementor.
 * Version: 2.6.0
 * Author: Eat&Go Criollo Express
 */
if (!defined('ABSPATH')) exit;

// 1. ESCRIBIR ARCHIVO MU-PLUGIN EN wp-content/mu-plugins/eatgo-weekly-rotation-engine.php
if (defined('WPMU_PLUGIN_DIR')) {
    $mu_dir = WPMU_PLUGIN_DIR;
    $mu_file = $mu_dir . '/eatgo-weekly-rotation-engine.php';
    if (!is_dir($mu_dir)) {
        wp_mkdir_p($mu_dir);
    }
    $full_code = '<?php' . PHP_EOL .
    '/**' . PHP_EOL .
    ' * Plugin Name: Eat&Go Weekly Rotation Query Engine' . PHP_EOL .
    ' * Description: Motor de rotacion semanal de menu y hooks de consulta para Loop Grids en Elementor.' . PHP_EOL .
    ' * Version: 3.0.0' . PHP_EOL .
    ' * Author: Eat&Go Criollo Express' . PHP_EOL .
    ' */' . PHP_EOL .
    'if (!defined(\'ABSPATH\')) exit;' . PHP_EOL . PHP_EOL;
    @file_put_contents($mu_file, $full_code);
}

// 2. REGISTRAR AJUSTE EN AJUSTES -> GENERAL
add_action('init', function() {
    register_setting('general', 'eatgo_semana_activa', [
        'type' => 'string',
        'sanitize_callback' => 'sanitize_text_field',
        'default' => 'auto',
        'show_in_rest' => true
    ]);
});

add_action('admin_init', function() {
    add_settings_section(
        'eatgo_weekly_settings_section',
        '🍽️ Eat&Go: Configuración de Menú Semanal',
        function() {
            echo '<p>Controla la rotación automática de menú según el calendario o fuerza una semana específica para la cocina.</p>';
        },
        'general'
    );

    add_settings_field(
        'eatgo_semana_activa',
        'Semana Activa del Menú',
        function() {
            $val = get_option('eatgo_semana_activa', 'auto');
            $auto_val = (intval(date('W')) % 2 !== 0) ? '1' : '2';
            ?>
            <select name="eatgo_semana_activa" id="eatgo_semana_activa">
                <option value="auto" <?php selected($val, 'auto'); ?>>Automática por Calendario (Actualmente Semana <?php echo $auto_val; ?>)</option>
                <option value="1" <?php selected($val, '1'); ?>>Forzar Semana 1 (lunes-1, martes-1, etc.)</option>
                <option value="2" <?php selected($val, '2'); ?>>Forzar Semana 2 (lunes-2, martes-2, etc.)</option>
                <option value="3" <?php selected($val, '3'); ?>>Forzar Semana 3 (lunes-semana-3 / lunes-3)</option>
                <option value="4" <?php selected($val, '4'); ?>>Forzar Semana 4 (lunes-semana-4 / lunes-4)</option>
            </select>
            <p class="description">Semana actual del año: <?php echo date('W'); ?>. Permite forzar de la Semana 1 a la 4 o usar ?semana=[1-4] por URL.</p>
            <?php
        },
        'general',
        'eatgo_weekly_settings_section'
    );
});

// 3. FUNCIÓN HELPER PARA OBTENER LA SEMANA ACTIVA
if (!function_exists('eatgo_get_active_week')) {
    function eatgo_get_active_week() {
        // 1. Soporte para parámetro URL (?semana=1, 2, 3, 4)
        if (!empty($_GET['semana'])) {
            $url_sem = sanitize_key($_GET['semana']);
            if (in_array($url_sem, ['1', '2', '3', '4'], true)) {
                return $url_sem;
            }
        }
        
        // 2. Opción forzada en ajustes de WordPress
        $option = get_option('eatgo_semana_activa', 'auto');
        if (in_array($option, ['1', '2', '3', '4'], true)) {
            return $option;
        }
        
        // 3. Cálculo de calendario con Zona Horaria de Panamá (GMT-5)
        try {
            $tz = new DateTimeZone('America/Panama');
            $now = new DateTime('now', $tz);
            $week_num = intval($now->format('W'));
        } catch (Exception $e) {
            $week_num = intval(date('W'));
        }
        
        return ($week_num % 2 !== 0) ? '1' : '2';
    }
}
if (!function_exists('eatgo_get_active_week_number')) {
    function eatgo_get_active_week_number() {
        return eatgo_get_active_week();
    }
}

// 4. ELEMENTOR QUERY HOOKS PARA LOOP GRIDS (query_menu_lunes, query_menu_martes, etc.)
$dias_semana = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado'];

foreach ($dias_semana as $dia) {
    add_action("elementor/query/query_menu_{$dia}", function($query) use ($dia) {
        $semana = eatgo_get_active_week();
        $category_slug = "{$dia}-{$semana}";

        $term = get_term_by('slug', $category_slug, 'product_cat');
        if (!$term || $term->count == 0) {
            $alt_slug = "{$dia}-semana-{$semana}";
            $alt_term = get_term_by('slug', $alt_slug, 'product_cat');
            if ($alt_term && $alt_term->count > 0) {
                $category_slug = $alt_slug;
            } else {
                $fallback_term = get_term_by('slug', "{$dia}-1", 'product_cat');
                if ($fallback_term && $fallback_term->count > 0) {
                    $category_slug = "{$dia}-1";
                } else {
                    $dia_term = get_term_by('slug', $dia, 'product_cat');
                    if ($dia_term && $dia_term->count > 0) {
                        $category_slug = $dia;
                    } else {
                        $category_slug = "semana-{$semana}";
                        $sem_term = get_term_by('slug', $category_slug, 'product_cat');
                        if (!$sem_term || $sem_term->count == 0) {
                            $category_slug = 'semana-1';
                        }
                    }
                }
            }
        }

        if (!empty($_GET['semana'])) {
            $terms_to_query = [$category_slug];
        } else {
            $terms_to_query = [$category_slug];
            if (strpos($category_slug, '-1') !== false || $category_slug === $dia) {
                $terms_to_query = array_unique([$category_slug, "{$dia}-1", $dia]);
            }
        }

        $query->set('post_type', 'product');
        $query->set('post_status', 'publish');

        $tax_query = (array) $query->get('tax_query');
        $tax_query[] = [
            'taxonomy' => 'product_cat',
            'field'    => 'slug',
            'terms'    => $terms_to_query,
            'operator' => 'IN',
        ];

        $query->set('tax_query', $tax_query);
    });
}


// 4.1 ELEMENTOR QUERY HOOK PARA /menu-del-dia/ (menu_del_dia_auto)
add_action('elementor/query/menu_del_dia_auto', function($query) {
    // 1. Detección de Semana Activa (con soporte ?semana=1, 2, 3, 4)
    $semana = eatgo_get_active_week();
    if (!empty($_GET['semana'])) {
        $sem_req = sanitize_key($_GET['semana']);
        if (in_array($sem_req, ['1', '2', '3', '4'], true)) {
            $semana = $sem_req;
        }
    }

    $dias_validos = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado'];

    // 2. Detectar Override de Día por URL (?dia=[nombre_dia])
    $dia_target = '';
    if (!empty($_GET['dia'])) {
        $raw_dia = sanitize_text_field(wp_unslash($_GET['dia']));
        $raw_dia = strtolower(trim($raw_dia));
        $accents = ['á' => 'a', 'é' => 'e', 'í' => 'i', 'ó' => 'o', 'ú' => 'u'];
        $clean_dia = strtr($raw_dia, $accents);
        if (in_array($clean_dia, $dias_validos, true)) {
            $dia_target = $clean_dia;
        }
    }

    // 3. Detección de Día por Defecto (con Zona Horaria de Panamá y Regla de Domingo)
    if (empty($dia_target)) {
        try {
            $tz = new DateTimeZone('America/Panama');
            $now = new DateTime('now', $tz);
            $day_of_week = intval($now->format('w')); // 0=Domingo, 1=Lunes... 6=Sábado
        } catch (Exception $e) {
            $day_of_week = intval(function_exists('wp_date') ? wp_date('w') : date('w'));
        }

        // REGLA DE DOMINGO: Si es domingo (0), resolver platos del LUNES para pedidos anticipados
        if ($day_of_week === 0) {
            $dia_target = 'lunes';
        } else {
            $map_dias = [
                1 => 'lunes',
                2 => 'martes',
                3 => 'miercoles',
                4 => 'jueves',
                5 => 'viernes',
                6 => 'sabado'
            ];
            $dia_target = isset($map_dias[$day_of_week]) ? $map_dias[$day_of_week] : 'lunes';
        }
    }

    // 4. Filtrado en WooCommerce por categoría (semana + día)
    $category_slug = "{$dia_target}-{$semana}";

    $term = get_term_by('slug', $category_slug, 'product_cat');
    if (!$term || $term->count == 0) {
        $alt_slug = "{$dia_target}-semana-{$semana}";
        $alt_term = get_term_by('slug', $alt_slug, 'product_cat');
        if ($alt_term && $alt_term->count > 0) {
            $category_slug = $alt_slug;
        } else {
            $fallback_term = get_term_by('slug', "{$dia_target}-1", 'product_cat');
            if ($fallback_term && $fallback_term->count > 0) {
                $category_slug = "{$dia_target}-1";
            } else {
                $dia_term = get_term_by('slug', $dia_target, 'product_cat');
                if ($dia_term && $dia_term->count > 0) {
                    $category_slug = $dia_target;
                } else {
                    $category_slug = "semana-{$semana}";
                    $sem_term = get_term_by('slug', $category_slug, 'product_cat');
                    if (!$sem_term || $sem_term->count == 0) {
                        $category_slug = 'semana-1';
                    }
                }
            }
        }
    }

    // Si el usuario especificó ?semana= en la URL, respetar estrictamente esa semana
    if (!empty($_GET['semana'])) {
        $terms_to_query = [$category_slug];
    } else {
        $terms_to_query = [$category_slug];
        if (strpos($category_slug, '-1') !== false || $category_slug === $dia_target) {
            $terms_to_query = array_unique([$category_slug, "{$dia_target}-1", $dia_target]);
        }
    }

    $query->set('post_type', 'product');
    $query->set('post_status', 'publish');

    $tax_query = (array) $query->get('tax_query');
    $tax_query[] = [
        'taxonomy' => 'product_cat',
        'field'    => 'slug',
        'terms'    => $terms_to_query,
        'operator' => 'IN',
    ];

    $query->set('tax_query', $tax_query);
});

// 5. ENDPOINTS REST
add_action('rest_api_init', function() {
    register_rest_route('eatgo/v1', '/menu-semanal', [
        'methods' => 'GET',
        'callback' => 'eatgo_rest_get_menu_semanal',
        'permission_callback' => '__return_true'
    ]);

    // Sincronizar y compilar HTML de Elementor en post_content
    register_rest_route('eatgo/v1', '/compile-page-564', [
        'methods' => ['POST', 'GET'],
        'callback' => function() {
            if (!class_exists('\Elementor\Plugin')) {
                return rest_ensure_response(['error' => 'no_elementor']);
            }
            $post_id = !empty($_GET['id']) ? intval($_GET['id']) : 564;
            
            // Render fresh builder content
            $builder_html = \Elementor\Plugin::$instance->frontend->get_builder_content_for_display($post_id, true);
            
            // Save to post_content in database
            global $wpdb;
            $wpdb->update(
                $wpdb->posts,
                ['post_content' => $builder_html],
                ['ID' => $post_id]
            );

            // Clear Elementor CSS cache
            if (class_exists('\Elementor\Core\Files\CSS\Post')) {
                $css_file = \Elementor\Core\Files\CSS\Post::create($post_id);
                $css_file->update();
            }
            \Elementor\Plugin::$instance->files_manager->clear_cache();

            return rest_ensure_response([
                'success' => true,
                'content_length' => strlen($builder_html),
                'has_loop_grid' => strpos($builder_html, 'elementor-widget-loop-grid') !== false,
                'has_5c' => strpos($builder_html, '5c1c1deb') !== false
            ]);
        },
        'permission_callback' => '__return_true'
    ]);
});

if (!function_exists('eatgo_rest_get_menu_semanal')) {
    function eatgo_rest_get_menu_semanal() {
        $semana = eatgo_get_active_week();
        $dias = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado'];
        $menu = [
            'semana_activa' => $semana,
            'modo' => get_option('eatgo_semana_activa', 'auto'),
            'dias' => []
        ];

        foreach ($dias as $dia) {
            $category_slug = "{$dia}-{$semana}";
            
            $args = [
                'status' => 'publish',
                'limit' => 12,
                'category' => [$category_slug],
                'orderby' => 'menu_order title',
                'order' => 'ASC'
            ];

            $products = function_exists('wc_get_products') ? wc_get_products($args) : [];
            
            if (empty($products)) {
                $fallback_args = [
                    'status' => 'publish',
                    'limit' => 12,
                    'category' => ["{$dia}-1", $dia],
                    'orderby' => 'menu_order title',
                    'order' => 'ASC'
                ];
                $products = function_exists('wc_get_products') ? wc_get_products($fallback_args) : [];
            }

            if (empty($products)) {
                $fallback_gen = [
                    'status' => 'publish',
                    'limit' => 12,
                    'category' => ["semana-{$semana}", 'semana-1'],
                    'orderby' => 'date',
                    'order' => 'DESC'
                ];
                $products = function_exists('wc_get_products') ? wc_get_products($fallback_gen) : [];
            }

            $dia_platos = [];
            foreach ($products as $p) {
                $image_id = $p->get_image_id();
                $image_url = $image_id ? wp_get_attachment_image_url($image_id, 'full') : '';
                
                $dia_platos[] = [
                    'id' => $p->get_id(),
                    'name' => $p->get_name(),
                    'price' => '$' . number_format((float)$p->get_price(), 2, '.', ''),
                    'description' => wp_strip_all_tags($p->get_short_description() ?: $p->get_description() ?: 'Delicioso plato tradicional panameño preparado al momento.'),
                    'image_url' => $image_url,
                    'tag' => 'PLATO ESTRELLA'
                ];
            }

            $menu['dias'][$dia] = [
                'slug' => $category_slug,
                'platos' => $dia_platos
            ];
        }

        return rest_ensure_response($menu);
    }
}

// 6. CAMPO DE VIDEO NATIVO PARA PRODUCTOS EN WOOCOMMERCE
add_action('woocommerce_product_options_general_product_data', function() {
    echo '<div class="options_group">';
    woocommerce_wp_text_input([
        'id'          => '_eatgo_video_url',
        'label'       => 'URL del Video del Plato (YouTube/MP4)',
        'placeholder' => 'https://www.youtube.com/watch?v=...',
        'description' => 'Ingresa el enlace del video de preparacion o presentacion del plato para mostrar en el modal.',
        'desc_tip'    => true,
    ]);
    echo '</div>';
});

add_action('woocommerce_process_product_meta', function($post_id) {
    if (isset($_POST['_eatgo_video_url'])) {
        update_post_meta($post_id, '_eatgo_video_url', esc_url_raw($_POST['_eatgo_video_url']));
    }
});

// Exponer en REST API de productos
add_action('rest_api_init', function() {
    register_rest_field('product', 'eatgo_video_url', [
        'get_callback' => function($product_arr) {
            return get_post_meta($product_arr['id'], '_eatgo_video_url', true) ?: '';
        },
        'update_callback' => function($value, $product_obj) {
            return update_post_meta($product_obj->ID, '_eatgo_video_url', esc_url_raw($value));
        },
        'schema' => [
            'type'        => 'string',
            'description' => 'URL del video del producto.',
        ],
    ]);
});
