<?php
/**
 * Snippet ID: 7
 * Title: EatGo Comanda Digital Cart Controller
 * Scope: global
 */

add_action('wp_ajax_eatgo_cart_update_qty', 'eatgo_cart_update_qty_handler');
add_action('wp_ajax_nopriv_eatgo_cart_update_qty', 'eatgo_cart_update_qty_handler');
function eatgo_cart_update_qty_handler() {
    $cart_item_key = sanitize_text_field($_POST['cart_item_key'] ?? '');
    $qty = intval($_POST['quantity'] ?? 0);
    if ($cart_item_key && function_exists('WC') && WC()->cart) {
        if ($qty <= 0) {
            WC()->cart->remove_cart_item($cart_item_key);
        } else {
            WC()->cart->set_quantity($cart_item_key, $qty, true);
        }
        WC_AJAX::get_refreshed_fragments();
    }
    wp_die();
}

add_action('wp_ajax_eatgo_cart_clear', 'eatgo_cart_clear_handler');
add_action('wp_ajax_nopriv_eatgo_cart_clear', 'eatgo_cart_clear_handler');
function eatgo_cart_clear_handler() {
    if (function_exists('WC') && WC()->cart) {
        WC()->cart->empty_cart();
        WC_AJAX::get_refreshed_fragments();
    }
    wp_die();
}

// ==========================================
// EAT&GO: PANEL ADMINISTRABLE DE PEDIDOS & WHATSAPP
// ==========================================
add_action('admin_menu', function() {
    add_menu_page(
        'Eat&Go Pedidos',
        'Eat&Go Pedidos',
        'manage_options',
        'eatgo-pedidos-settings',
        'eatgo_render_pedidos_settings_page',
        'dashicons-cart',
        56
    );
});

add_action('admin_init', function() {
    register_setting('eatgo_pedidos_group', 'eatgo_whatsapp_phone');
    register_setting('eatgo_pedidos_group', 'eatgo_whatsapp_formatted');
    register_setting('eatgo_pedidos_group', 'eatgo_delivery_cost');
    register_setting('eatgo_pedidos_group', 'eatgo_dispatch_hours');
    register_setting('eatgo_pedidos_group', 'eatgo_time_retiro');
    register_setting('eatgo_pedidos_group', 'eatgo_time_delivery');
    
    if (get_option('eatgo_whatsapp_phone') === false || get_option('eatgo_whatsapp_phone') === '') {
        update_option('eatgo_whatsapp_phone', '50769906424');
    }
    if (get_option('eatgo_whatsapp_formatted') === false || get_option('eatgo_whatsapp_formatted') === '') {
        update_option('eatgo_whatsapp_formatted', '+507 6990-6424');
    }
    if (get_option('eatgo_delivery_cost') === false || get_option('eatgo_delivery_cost') === '') {
        update_option('eatgo_delivery_cost', '2.50');
    }
    if (get_option('eatgo_dispatch_hours') === false || get_option('eatgo_dispatch_hours') === '') {
        update_option('eatgo_dispatch_hours', 'Se despacha de 11:30am a 3:30pm');
    }
    if (get_option('eatgo_time_retiro') === false || get_option('eatgo_time_retiro') === '') {
        update_option('eatgo_time_retiro', '10-15 minutos');
    }
    if (get_option('eatgo_time_delivery') === false || get_option('eatgo_time_delivery') === '') {
        update_option('eatgo_time_delivery', '20-35 min');
    }
});

function eatgo_render_pedidos_settings_page() {
    if (!current_user_can('manage_options')) return;
    ?>
    <div class="wrap" style="max-width: 820px;">
        <h1 style="display:flex; align-items:center; gap:12px; font-weight:800; color:#18181B; margin-bottom: 24px;">
            <span style="background:#c81c20; color:#fff; padding:6px 14px; border-radius:8px; font-size:18px;">Eat&Go</span>
            Ajustes de Pedidos y WhatsApp
        </h1>
        
        <?php if (isset($_GET['settings-updated']) && $_GET['settings-updated']) : ?>
            <div class="notice notice-success is-dismissible" style="border-left-color: #10B981;">
                <p><strong>✅ Configuración de pedidos actualizada y activa en todo el sitio.</strong></p>
            </div>
        <?php endif; ?>

        <div style="background:#fff; border-radius:12px; border:1px solid #E5E7EB; box-shadow:0 4px 12px rgba(0,0,0,0.05); padding:24px;">
            <form method="post" action="options.php">
                <?php settings_fields('eatgo_pedidos_group'); ?>
                
                <h2 style="font-size:16px; font-weight:700; color:#18181B; border-bottom:2px solid #F3F4F6; padding-bottom:8px; margin-top:0;">
                    📱 Contacto y Despacho WhatsApp
                </h2>
                <table class="form-table" role="presentation" style="margin-top:0;">
                    <tr>
                        <th scope="row"><label for="eatgo_whatsapp_phone">Número Canónico (WhatsApp)</label></th>
                        <td>
                            <input name="eatgo_whatsapp_phone" type="text" id="eatgo_whatsapp_phone" value="<?php echo esc_attr(get_option('eatgo_whatsapp_phone', '50769906424')); ?>" class="regular-text" style="font-size:15px; font-weight:600;" required />
                            <p class="description">Número con código de país sin símbolos (+, - ni espacios). Ej: <code>50769906424</code></p>
                        </td>
                    </tr>
                    <tr>
                        <th scope="row"><label for="eatgo_whatsapp_formatted">Formato Visual</label></th>
                        <td>
                            <input name="eatgo_whatsapp_formatted" type="text" id="eatgo_whatsapp_formatted" value="<?php echo esc_attr(get_option('eatgo_whatsapp_formatted', '+507 6990-6424')); ?>" class="regular-text" />
                            <p class="description">Texto mostrado en header y footer. Ej: <code>+507 6990-6424</code></p>
                        </td>
                    </tr>
                </table>

                <h2 style="font-size:16px; font-weight:700; color:#18181B; border-bottom:2px solid #F3F4F6; padding-bottom:8px; margin-top:24px;">
                    🛵 Tarifas y Horarios de Entrega
                </h2>
                <table class="form-table" role="presentation" style="margin-top:0;">
                    <tr>
                        <th scope="row"><label for="eatgo_delivery_cost">Costo de Delivery ($)</label></th>
                        <td>
                            <input name="eatgo_delivery_cost" type="number" step="0.01" min="0" id="eatgo_delivery_cost" value="<?php echo esc_attr(get_option('eatgo_delivery_cost', '2.50')); ?>" class="small-text" style="font-size:15px; font-weight:600;" required />
                            <p class="description">Tarifa aplicada cuando el cliente selecciona "Delivery". Ej: <code>2.50</code></p>
                        </td>
                    </tr>
                    <tr>
                        <th scope="row"><label for="eatgo_dispatch_hours">Horario de Despacho (Ayuda)</label></th>
                        <td>
                            <input name="eatgo_dispatch_hours" type="text" id="eatgo_dispatch_hours" value="<?php echo esc_attr(get_option('eatgo_dispatch_hours', 'Se despacha de 11:30am a 3:30pm')); ?>" class="large-text" />
                            <p class="description">Texto gris de ayuda debajo del campo de hora en el cajón de pedido.</p>
                        </td>
                    </tr>
                    <tr>
                        <th scope="row"><label for="eatgo_time_retiro">Tiempo Estimado (Retiro)</label></th>
                        <td>
                            <input name="eatgo_time_retiro" type="text" id="eatgo_time_retiro" value="<?php echo esc_attr(get_option('eatgo_time_retiro', '10-15 minutos')); ?>" class="regular-text" />
                            <p class="description">Ej: <code>10-15 minutos</code></p>
                        </td>
                    </tr>
                    <tr>
                        <th scope="row"><label for="eatgo_time_delivery">Tiempo Estimado (Delivery)</label></th>
                        <td>
                            <input name="eatgo_time_delivery" type="text" id="eatgo_time_delivery" value="<?php echo esc_attr(get_option('eatgo_time_delivery', '20-35 min')); ?>" class="regular-text" />
                            <p class="description">Ej: <code>20-35 min</code></p>
                        </td>
                    </tr>
                </table>

                <?php submit_button('Guardar Ajustes de Pedidos', 'primary', 'submit', true, ['style' => 'background:#c81c20; border-color:#c81c20; font-size:14px; padding:6px 20px; font-weight:700;']); ?>
            </form>
        </div>
    </div>
    <?php
}

// Inyección Frontend en wp_head
add_action('wp_head', function() {
    $phone = get_option('eatgo_whatsapp_phone', '50769906424');
    if (empty($phone)) $phone = '50769906424';
    $clean_phone = preg_replace('/[^0-9]/', '', $phone);
    $formatted = get_option('eatgo_whatsapp_formatted', '+507 6990-6424');
    $val = get_option('eatgo_delivery_cost');
    $delivery_cost = ($val !== false && is_numeric($val) && floatval($val) > 0) ? floatval($val) : 2.50;
    $dispatch_hours = get_option('eatgo_dispatch_hours', 'Se despacha de 11:30am a 3:30pm');
    $time_retiro = get_option('eatgo_time_retiro', '10-15 minutos');
    $time_delivery = get_option('eatgo_time_delivery', '20-35 min');

    $config = [
        'whatsappPhone' => $clean_phone,
        'whatsappUrl' => 'https://wa.me/' . $clean_phone,
        'whatsappFormatted' => $formatted,
        'deliveryCost' => $delivery_cost,
        'dispatchHours' => $dispatch_hours,
        'timeRetiro' => $time_retiro,
        'timeDelivery' => $time_delivery,
    ];
    echo '<script id="eatgo-config-vars">window.EatGoConfig = ' . json_encode($config) . ';</script>' . "
";
}, 5);
