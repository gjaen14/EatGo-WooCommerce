import subprocess
import time
import json
import urllib.request
import asyncio
import base64
import websockets
import os

# Matar instancias previas
subprocess.run(['pkill', '-9', '-f', 'Google Chrome'], stderr=subprocess.DEVNULL)
time.sleep(1)

proc = subprocess.Popen([
    '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    '--headless=new',
    '--remote-debugging-port=9222',
    '--user-data-dir=/tmp/chrome_clean_profile_comanda',
    '--disable-gpu',
    '--window-size=1440,1050',
    'about:blank'
])

async def run():
    ws_url = None
    for attempt in range(15):
        try:
            targets = json.loads(urllib.request.urlopen('http://localhost:9222/json').read())
            pages = [t for t in targets if t.get('type') == 'page']
            if pages:
                ws_url = pages[0]['webSocketDebuggerUrl']
                print(f"Connected to page target: {pages[0].get('url')} - {ws_url}")
                break
        except Exception:
            pass
        await asyncio.sleep(0.5)

    if not ws_url:
        print("Error: Could not locate Chrome page target.")
        return

    async with websockets.connect(ws_url, max_size=50*1024*1024) as ws:
        # 1. Enable Page
        await ws.send(json.dumps({'id': 1, 'method': 'Page.enable'}))
        
        # 2. Navigate
        await ws.send(json.dumps({'id': 2, 'method': 'Page.navigate', 'params': {'url': 'https://eatgopty.com/menu-semanal/'}}))
        await asyncio.sleep(4.0)

        # 3. Simulate adding item and opening drawer
        setup_js = '''
        (function() {
            // Agregar plato al carrito vía WooCommerce AJAX
            if (typeof jQuery !== 'undefined') {
                jQuery.post('/?wc-ajax=add_to_cart', { product_id: 97, quantity: 1 }, function(data) {
                    jQuery(document.body).trigger('added_to_cart', [data.fragments, data.cart_hash]);
                    jQuery(document.body).trigger('wc_fragments_refreshed');
                });
            }
            
            setTimeout(function() {
                // Abrir el drawer de Elementor
                var container = document.querySelector('.elementor-menu-cart__container');
                if (container) {
                    container.classList.add('elementor-menu-cart--shown');
                    container.setAttribute('aria-hidden', 'false');
                }
                
                // Llenar campos de despacho de muestra
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
                }, 500);
            }, 1000);
        })()
        '''
        await ws.send(json.dumps({'id': 3, 'method': 'Runtime.evaluate', 'params': {'expression': setup_js}}))
        await asyncio.sleep(2.5)

        # 4. Check DOM state
        inspect_js = '''
        (function() {
            var header = document.querySelector('.eg-comanda-header');
            var cards = document.querySelectorAll('.eg-custom-card');
            var body = document.querySelector('.eg-comanda-body');
            var total = document.querySelector('.eg-resumen-total-val');
            var waBtn = document.querySelector('.eg-btn-whatsapp');
            return {
                hasHeader: !!header,
                headerTitle: header ? header.querySelector('.eg-header-title').innerText : null,
                cardCount: cards.length,
                hasBody: !!body,
                totalVal: total ? total.innerText : null,
                waHref: waBtn ? waBtn.getAttribute('href') : null
            };
        })()
        '''
        await ws.send(json.dumps({'id': 4, 'method': 'Runtime.evaluate', 'params': {'expression': inspect_js, 'returnByValue': True}}))
        
        while True:
            msg = json.loads(await ws.recv())
            if msg.get('id') == 4:
                print("DOM STATE INSPECTION:", json.dumps(msg.get('result', {}).get('result', {}).get('value', {}), indent=2))
                break

        # 5. Capture Screenshot
        await ws.send(json.dumps({'id': 5, 'method': 'Page.captureScreenshot'}))
        while True:
            resp = json.loads(await ws.recv())
            if resp.get('id') == 5:
                data = base64.b64decode(resp['result']['data'])
                art_dir = '/Users/jaendev/.gemini/antigravity/brain/634b1f07-6953-4def-898c-6e4df20cdf3f'
                art_path = os.path.join(art_dir, 'comanda_digital_drawer_verified.png')
                local_path = '/Applications/XAMPP/xamppfiles/htdocs/Eat&Go_Woocomerce/comanda_digital_drawer_verified.png'
                
                with open(art_path, 'wb') as f:
                    f.write(data)
                with open(local_path, 'wb') as f:
                    f.write(data)
                    f.flush()
                    os.fsync(f.fileno())
                print('SAVED_SUCCESSFULLY:', art_path, 'size:', len(data))
                break

try:
    asyncio.run(run())
finally:
    proc.terminate()
