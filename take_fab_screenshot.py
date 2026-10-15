import subprocess
import time
import json
import urllib.request
import asyncio
import base64
import websockets
import os

ARTIFACT_DIR = '/Users/jaendev/.gemini/antigravity/brain/f180faf7-7a71-484e-b640-c77ee658b798'
os.makedirs(ARTIFACT_DIR, exist_ok=True)

async def capture():
    proc = subprocess.Popen([
        '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
        '--headless=new',
        '--remote-debugging-port=9224',
        '--user-data-dir=/tmp/chrome_test_profile_fab_art',
        '--disable-gpu',
        '--window-size=1440,1050',
        'about:blank'
    ])
    try:
        await asyncio.sleep(2)
        targets = json.loads(urllib.request.urlopen('http://localhost:9224/json').read())
        ws_url = targets[0]['webSocketDebuggerUrl']
        
        async with websockets.connect(ws_url) as ws:
            # 1. Enable Runtime and Page
            await ws.send(json.dumps({'id': 1, 'method': 'Page.enable'}))
            await ws.send(json.dumps({'id': 2, 'method': 'Runtime.enable'}))

            # 2. Navigate to menu-del-dia
            await ws.send(json.dumps({'id': 3, 'method': 'Page.navigate', 'params': {'url': 'https://eatgopty.com/menu-del-dia/'}}))
            await asyncio.sleep(5)

            # Check DOM state
            check_js = '''
            (function() {
                var fab = document.querySelector('.eatgo-fab-cart');
                var headerToggle = document.querySelector('.elementor-menu-cart__toggle');
                var headerToggleComputed = headerToggle ? window.getComputedStyle(headerToggle).display : 'null';
                var fabComputed = fab ? window.getComputedStyle(fab) : null;
                
                return {
                    hasFab: !!fab,
                    fabText: fab ? fab.innerText.trim() : null,
                    headerToggleDisplay: headerToggleComputed,
                    fabPosition: fabComputed ? {
                        position: fabComputed.position,
                        bottom: fabComputed.bottom,
                        right: fabComputed.right,
                        zIndex: fabComputed.zIndex,
                        backgroundColor: fabComputed.backgroundColor,
                        animation: fabComputed.animation
                    } : null
                };
            })()
            '''
            await ws.send(json.dumps({
                'id': 4,
                'method': 'Runtime.evaluate',
                'params': {'expression': check_js, 'returnByValue': True}
            }))
            
            while True:
                msg = json.loads(await ws.recv())
                if msg.get('id') == 4:
                    print('DOM Check Result:', json.dumps(msg.get('result', {}).get('value', {}), indent=2))
                    break

            # 3. Capture initial screenshot
            await ws.send(json.dumps({'id': 5, 'method': 'Page.captureScreenshot', 'params': {'format': 'png'}}))
            while True:
                msg = json.loads(await ws.recv())
                if msg.get('id') == 5:
                    out_path = os.path.join(ARTIFACT_DIR, 'fab_cart_initial.png')
                    with open(out_path, 'wb') as f:
                        f.write(base64.b64decode(msg['result']['data']))
                    print('Saved initial screenshot to:', out_path)
                    break

            # 4. Add product to cart via WooCommerce and re-evaluate
            add_item_js = '''
            (function() {
                return new Promise((resolve) => {
                    jQuery.post('/?wc-ajax=add_to_cart', { product_id: 97, quantity: 2 }, function(data) {
                        jQuery(document.body).trigger('added_to_cart', [data.fragments, data.cart_hash]);
                        jQuery(document.body).trigger('wc_fragments_refreshed');
                        setTimeout(() => resolve(true), 800);
                    });
                });
            })()
            '''
            await ws.send(json.dumps({
                'id': 6,
                'method': 'Runtime.evaluate',
                'params': {'expression': add_item_js, 'awaitPromise': True, 'returnByValue': True}
            }))
            while True:
                msg = json.loads(await ws.recv())
                if msg.get('id') == 6:
                    print('Added product 97 x 2 to cart')
                    break

            await asyncio.sleep(1.5)

            # Check FAB text after adding product
            await ws.send(json.dumps({
                'id': 7,
                'method': 'Runtime.evaluate',
                'params': {
                    'expression': 'document.querySelector(".eatgo-fab-cart") ? document.querySelector(".eatgo-fab-cart").innerText.trim() : "no fab"',
                    'returnByValue': True
                }
            }))
            while True:
                msg = json.loads(await ws.recv())
                if msg.get('id') == 7:
                    print('FAB Text after adding items:', msg.get('result', {}).get('value'))
                    break

            # 5. Capture screenshot with items in FAB
            await ws.send(json.dumps({'id': 8, 'method': 'Page.captureScreenshot', 'params': {'format': 'png'}}))
            while True:
                msg = json.loads(await ws.recv())
                if msg.get('id') == 8:
                    out_path = os.path.join(ARTIFACT_DIR, 'fab_cart_with_items.png')
                    with open(out_path, 'wb') as f:
                        f.write(base64.b64decode(msg['result']['data']))
                    print('Saved screenshot with items to:', out_path)
                    break

            # 6. Click FAB to verify side drawer opens
            click_fab_js = '''
            (function() {
                var fab = document.querySelector('.eatgo-fab-cart');
                if (fab) fab.click();
            })()
            '''
            await ws.send(json.dumps({
                'id': 9,
                'method': 'Runtime.evaluate',
                'params': {'expression': click_fab_js, 'returnByValue': True}
            }))
            await asyncio.sleep(1.5)

            # 7. Capture screenshot of drawer open
            await ws.send(json.dumps({'id': 10, 'method': 'Page.captureScreenshot', 'params': {'format': 'png'}}))
            while True:
                msg = json.loads(await ws.recv())
                if msg.get('id') == 10:
                    out_path = os.path.join(ARTIFACT_DIR, 'fab_cart_drawer_opened.png')
                    with open(out_path, 'wb') as f:
                        f.write(base64.b64decode(msg['result']['data']))
                    print('Saved drawer screenshot to:', out_path)
                    break

    finally:
        proc.terminate()

if __name__ == '__main__':
    asyncio.run(capture())
