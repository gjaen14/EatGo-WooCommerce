import urllib.request, json, base64

auth = 'Basic ' + base64.b64encode(b'JaenDev:4n3FKy26SkBpwe8GPBzdbqEz').decode()

with open('snippet_5_backup_before_query.php', 'r', encoding='utf-8') as f:
    code = f.read()

target = "add_action('elementor/query/menu_del_dia_auto', function($query) {"
assert target in code, 'menu_del_dia_auto not found in snippet 5'

hook_code = """

// 4.2 ELEMENTOR QUERY HOOK PARA HOME - PLATOS DESTACADOS (query_home_platos_hoy)
add_action('elementor/query/query_home_platos_hoy', function($query) {
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

    $tax_query = [
        [
            'taxonomy' => 'product_cat',
            'field'    => 'slug',
            'terms'    => $terms_to_query,
            'operator' => 'IN',
        ]
    ];

    $query->set('tax_query', $tax_query);
});
"""

idx_start = code.find(target)
idx_end = code.find("});", idx_start) + 3

new_code = code[:idx_end] + hook_code + code[idx_end:]

with open('snippet_5_engine.php', 'w', encoding='utf-8') as f:
    f.write(new_code)

print('Updated snippet_5_engine.php locally. Now uploading to Code Snippets API...')

update_data = json.dumps({'code': new_code}).encode('utf-8')
req_up = urllib.request.Request(
    'https://eatgopty.com/wp-json/code-snippets/v1/snippets/5',
    data=update_data,
    headers={'Authorization': auth, 'Content-Type': 'application/json'},
    method='POST'
)

with urllib.request.urlopen(req_up) as resp:
    res = json.loads(resp.read().decode('utf-8'))
    print(f"Snippet 5 updated successfully in WordPress! ID: {res.get('id')}, Active: {res.get('active')}")
