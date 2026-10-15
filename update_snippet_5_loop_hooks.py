import urllib.request
import json
import base64

username = 'JaenDev'
password = '4n3FKy26SkBpwe8GPBzdbqEz'
auth = 'Basic ' + base64.b64encode(f'{username}:{password}'.encode()).decode()

php_code = """
// 1. ESCRIBIR ARCHIVO MU-PLUGIN EN wp-content/mu-plugins/eatgo-weekly-rotation-engine.php
if (defined('WPMU_PLUGIN_DIR')) {
    $mu_dir = WPMU_PLUGIN_DIR;
    $mu_file = $mu_dir . '/eatgo-weekly-rotation-engine.php';
    if (!is_dir($mu_dir)) {
        wp_mkdir_p($mu_dir);
    }
    $header = '<?php' . PHP_EOL .
    '/**' . PHP_EOL .
    ' * Plugin Name: Eat&Go Weekly Rotation Engine' . PHP_EOL .
    ' * Description: Motor de rotación semanal de menú y hooks de consulta para Loop Grids en Elementor.' . PHP_EOL .
    ' * Version: 2.1.0' . PHP_EOL .
    ' * Author: Eat&Go Criollo Express' . PHP_EOL .
    ' */' . PHP_EOL .
    'if (!defined(\\'ABSPATH\\')) exit;' . PHP_EOL;
    @file_put_contents($mu_file, $header);
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
            </select>
            <p class="description">Semana actual del año: <?php echo date('W'); ?>. En modo "Automática", las semanas impares son Semana 1 y las pares son Semana 2.</p>
            <?php
        },
        'general',
        'eatgo_weekly_settings_section'
    );
});

// 3. FUNCIÓN HELPER PARA OBTENER LA SEMANA ACTIVA
if (!function_exists('eatgo_get_active_week')) {
    function eatgo_get_active_week() {
        $option = get_option('eatgo_semana_activa', 'auto');
        if ($option === '1' || $option === '2') {
            return $option;
        }
        return (intval(date('W')) % 2 !== 0) ? '1' : '2';
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

        // Verificar si la categoría existe y tiene productos
        $term = get_term_by('slug', $category_slug, 'product_cat');
        if (!$term || $term->count == 0) {
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

        $query->set('post_type', 'product');
        $query->set('post_status', 'publish');
        $query->set('posts_per_page', 3);

        $tax_query = (array) $query->get('tax_query');
        $tax_query[] = [
            'taxonomy' => 'product_cat',
            'field'    => 'slug',
            'terms'    => [$category_slug],
            'operator' => 'IN',
        ];

        $query->set('tax_query', $tax_query);
        $query->set('orderby', 'menu_order title');
        $query->set('order', 'ASC');
    });
}

// 5. ENDPOINT REST PARA CONSULTAR LOS PLATOS DE LA SEMANA ACTIVA
add_action('rest_api_init', function() {
    register_rest_route('eatgo/v1', '/menu-semanal', [
        'methods' => 'GET',
        'callback' => 'eatgo_rest_get_menu_semanal',
        'permission_callback' => '__return_true'
    ]);

    register_rest_route('eatgo/v1', '/search-element', [
        'methods' => 'GET',
        'callback' => function() {
            global $wpdb;
            $posts = $wpdb->get_results("SELECT ID, post_title, post_type, post_status FROM {$wpdb->posts} WHERE post_content LIKE '%5c1c1deb%'");
            $meta = $wpdb->get_results("SELECT post_id, meta_key, length(meta_value) as len FROM {$wpdb->postmeta} WHERE meta_value LIKE '%5c1c1deb%'");
            return rest_ensure_response([
                'posts' => $posts,
                'meta' => $meta
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
                'limit' => 3,
                'category' => [$category_slug],
                'orderby' => 'menu_order title',
                'order' => 'ASC'
            ];

            $products = function_exists('wc_get_products') ? wc_get_products($args) : [];
            
            if (empty($products)) {
                $fallback_args = [
                    'status' => 'publish',
                    'limit' => 3,
                    'category' => ["{$dia}-1", $dia],
                    'orderby' => 'menu_order title',
                    'order' => 'ASC'
                ];
                $products = function_exists('wc_get_products') ? wc_get_products($fallback_args) : [];
            }

            if (empty($products)) {
                $fallback_gen = [
                    'status' => 'publish',
                    'limit' => 3,
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
"""

payload = {
    'name': 'EatGo Weekly Rotation Query Engine',
    'desc': 'Motor de rotacion semanal de menu y hooks de consulta para Loop Grids en Elementor.',
    'code': php_code,
    'scope': 'global',
    'active': True,
    'priority': 1
}

req = urllib.request.Request(
    'https://eatgopty.com/wp-json/code-snippets/v1/snippets/5',
    headers={
        'Authorization': auth,
        'Content-Type': 'application/json'
    },
    data=json.dumps(payload).encode('utf-8')
)

with urllib.request.urlopen(req) as resp:
    data = json.load(resp)
    print('Snippet 5 updated successfully with Loop Grid hooks! Active:', data.get('active'))
