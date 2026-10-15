import subprocess
import time
import json
import urllib.request
import asyncio
import base64
import websockets

async def capture():
    proc = subprocess.Popen([
        '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
        '--headless=new',
        '--remote-debugging-port=9444',
        '--user-data-dir=/tmp/chrome_test_profile_cart_9444',
        '--disable-gpu',
        '--window-size=1440,1050',
        'about:blank'
    ])
    try:
        ws_url = None
        for _ in range(12):
            try:
                targets = json.loads(urllib.request.urlopen('http://localhost:9444/json').read())
                ws_url = targets[0]['webSocketDebuggerUrl']
                break
            except Exception:
                await asyncio.sleep(0.5)
        
        if not ws_url:
            print('Could not connect to Chrome on port 9444')
            return

        async with websockets.connect(ws_url) as ws:
            # 1. Navigate to Menu Semanal
            await ws.send(json.dumps({'id': 1, 'method': 'Page.navigate', 'params': {'url': 'https://eatgopty.com/menu-semanal/'}}))
            await asyncio.sleep(4.0)

            # 2. Add an item and open the Comanda Drawer
            open_script = '''
            (function() {
                // Add item to cart via WooCommerce AJAX
                if (typeof jQuery !== 'undefined') {
                    jQuery.post('/?wc-ajax=add_to_cart', { product_id: 97, quantity: 1 }, function(data) {
                        jQuery(document.body).trigger('added_to_cart', [data.fragments, data.cart_hash]);
                        jQuery(document.body).trigger('wc_fragments_refreshed');
                    });
                }
                
                setTimeout(function() {
                    // Open drawer
                    var btn = document.querySelector('.elementor-menu-cart__toggle_button, #elementor-menu-cart__toggle_button');
                    if (btn) btn.click();
                    
                    var container = document.querySelector('.elementor-menu-cart__container');
                    if (container) {
                        container.classList.add('elementor-menu-cart--shown');
                        container.setAttribute('aria-hidden', 'false');
                    }
                    
                    // Demo inputs
                    setTimeout(function() {
                        var inpNombre = document.querySelector('.eg-inp-nombre');
                        if (inpNombre) {
                            inpNombre.value = 'Carlos Mendoza';
                            inpNombre.dispatchEvent(new Event('input', { bubbles: true }));
                        }
                        var inpTel = document.querySelector('.eg-inp-tel');
                        if (inpTel) {
                            inpTel.value = '6234-5678';
                            inpTel.dispatchEvent(new Event('input', { bubbles: true }));
                        }
                        var inpEdificio = document.querySelector('.eg-inp-edificio');
                        if (inpEdificio) {
                            inpEdificio.value = 'Torre Global Bank';
                            inpEdificio.dispatchEvent(new Event('input', { bubbles: true }));
                        }
                        var inpOficina = document.querySelector('.eg-inp-oficina');
                        if (inpOficina) {
                            inpOficina.value = 'Piso 14, Of. 1402';
                            inpOficina.dispatchEvent(new Event('input', { bubbles: true }));
                        }
                    }, 400);
                }, 1000);
            })()
            '''
            await ws.send(json.dumps({'id': 2, 'method': 'Runtime.evaluate', 'params': {'expression': open_script}}))
            await asyncio.sleep(3.5)

            # 3. Screenshot
            await ws.send(json.dumps({'id': 3, 'method': 'Page.captureScreenshot'}))
            
            resp = json.loads(await ws.recv())
            while resp.get('id') != 3:
                resp = json.loads(await ws.recv())
            
            img_data = base64.b64decode(resp['result']['data'])
            artifact_path = '/Users/jaendev/.gemini/antigravity/brain/634b1f07-6953-4def-898c-6e4df20cdf3f/comanda_digital_drawer_live.png'
            with open(artifact_path, 'wb') as f:
                f.write(img_data)
            with open('comanda_digital_drawer_live.png', 'wb') as f:
                f.write(img_data)
            print(f'Saved screenshot to {artifact_path}')
    finally:
        proc.terminate()

asyncio.run(capture())
