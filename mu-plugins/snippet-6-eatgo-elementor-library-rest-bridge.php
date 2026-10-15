<?php
/**
 * Snippet ID: 6
 * Title: EatGo Elementor Library REST Bridge
 * Scope: global
 */


add_action("rest_api_init", function() {
    register_rest_route("eatgo/v1", "/get-elementor/(?P<id>\\d+)", [
        "methods" => "GET",
        "permission_callback" => "__return_true",
        "callback" => function($request) {
            $post_id = intval($request->get_param("id"));
            $data = get_post_meta($post_id, "_elementor_data", true);
            return [
                "post_id" => $post_id,
                "elementor_data" => is_string($data) ? json_decode($data, true) : $data
            ];
        }
    ]);
    register_rest_route("eatgo/v1", "/update-elementor", [
        "methods" => "POST",
        "permission_callback" => function() {
            return current_user_can("edit_posts");
        },
        "callback" => function($request) {
            $params = $request->get_json_params();
            $post_id = intval($params["post_id"] ?? 0);
            $data = $params["elementor_data"] ?? null;
            if (!$post_id || !$data) {
                return new WP_Error("invalid_params", "Missing post_id or elementor_data", ["status" => 400]);
            }
            if (is_array($data)) {
                $data = wp_json_encode($data);
            }
            update_post_meta($post_id, "_elementor_data", wp_slash($data));
            update_post_meta($post_id, "_elementor_edit_mode", "builder");
            if (isset($params["page_settings"]) && is_array($params["page_settings"])) {
                update_post_meta($post_id, "_elementor_page_settings", $params["page_settings"]);
            }
            if (class_exists("\\Elementor\\Plugin")) {
                \Elementor\Plugin::$instance->files_manager->clear_cache();
            }
            return [
                "success" => true,
                "post_id" => $post_id,
                "data_length" => strlen($data)
            ];
        }
    ]);
});
