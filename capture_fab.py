import subprocess
import time
import json
import urllib.request
import asyncio
import base64
import websockets
import os

OUTPUT_FILE = '/Applications/XAMPP/xamppfiles/htdocs/Eat&Go_Woocomerce/fab_cart_live_verified.png'

async def capture():
    # Kill any dangling Chrome instances
    subprocess.run(['pkill', '-f', 'chrome_test_fab'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(1)

    proc = subprocess.Popen([
        '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
        '--headless=new',
        '--remote-debugging-port=9225',
        '--user-data-dir=/tmp/chrome_test_fab',
        '--disable-gpu',
        '--window-size=1440,1050',
        'about:blank'
    ])
    try:
        await asyncio.sleep(2)
        targets = json.loads(urllib.request.urlopen('http://localhost:9225/json').read())
        ws_url = targets[0]['webSocketDebuggerUrl']
        
        async with websockets.connect(ws_url, max_size=50*1024*1024) as ws:
            # 1. Navigate to Menu del dia
            await ws.send(json.dumps({'id': 1, 'method': 'Page.navigate', 'params': {'url': 'https://eatgopty.com/menu-del-dia/'}}))
            await asyncio.sleep(4)

            # 2. Add an item to cart via AJAX so the FAB shows 1 dish and price
            add_item_js = '''
            (function() {
                if (typeof jQuery !== "undefined") {
                    jQuery.post("/?wc-ajax=add_to_cart", { product_id: 97, quantity: 1 }, function(data) {
                        jQuery(document.body).trigger("added_to_cart", [data.fragments, data.cart_hash]);
                        jQuery(document.body).trigger("wc_fragments_refreshed");
                    });
                }
            })()
            '''
            await ws.send(json.dumps({'id': 2, 'method': 'Runtime.evaluate', 'params': {'expression': add_item_js}}))
            await asyncio.sleep(2)

            # 3. Capture screenshot
            await ws.send(json.dumps({'id': 3, 'method': 'Page.captureScreenshot'}))
            
            while True:
                resp = json.loads(await ws.recv())
                if resp.get('id') == 3:
                    img_data = base64.b64decode(resp['result']['data'])
                    with open(OUTPUT_FILE, 'wb') as f:
                        f.write(img_data)
                    print('Screenshot saved successfully:', OUTPUT_FILE, 'Bytes:', len(img_data))
                    break
    finally:
        proc.terminate()

if __name__ == '__main__':
    asyncio.run(capture())
