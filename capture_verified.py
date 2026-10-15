import subprocess
import time
import json
import urllib.request
import asyncio
import base64
import websockets
import os

subprocess.run(['pkill', '-9', '-f', 'Google Chrome'], stderr=subprocess.DEVNULL)
time.sleep(1)

proc = subprocess.Popen([
    '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    '--headless=new',
    '--remote-debugging-port=9222',
    '--user-data-dir=/tmp/chrome_p9222',
    '--disable-gpu',
    '--window-size=1440,1050',
    'about:blank'
])

async def run():
    await asyncio.sleep(2)
    targets = json.loads(urllib.request.urlopen('http://localhost:9222/json').read())
    ws_url = targets[0]['webSocketDebuggerUrl']
    async with websockets.connect(ws_url, max_size=50*1024*1024) as ws:
        # Navigate to Menu del dia
        await ws.send(json.dumps({'id': 1, 'method': 'Page.navigate', 'params': {'url': 'https://eatgopty.com/menu-del-dia/'}}))
        
        # Wait for page to load
        await asyncio.sleep(5)
        
        # Check FAB status in DOM
        check_js = '''
        (function() {
            var fab = document.querySelector(".eatgo-fab-cart");
            return {
                fabExists: !!fab,
                fabText: fab ? fab.innerText.trim() : null,
                fabZIndex: fab ? window.getComputedStyle(fab).zIndex : null,
                fabPosition: fab ? window.getComputedStyle(fab).position : null,
                headerToggleDisplay: document.querySelector(".elementor-menu-cart__toggle") ? window.getComputedStyle(document.querySelector(".elementor-menu-cart__toggle")).display : "none"
            };
        })()
        '''
        await ws.send(json.dumps({'id': 2, 'method': 'Runtime.evaluate', 'params': {'expression': check_js, 'returnByValue': True}}))
        
        while True:
            msg = json.loads(await ws.recv())
            if msg.get('id') == 2 and 'result' in msg:
                print("EVAL RESULT:", json.dumps(msg.get('result', {}).get('value', {})))
                break
        
        # Request screenshot
        await ws.send(json.dumps({'id': 3, 'method': 'Page.captureScreenshot'}))
        while True:
            resp = json.loads(await ws.recv())
            if resp.get('id') == 3 and 'result' in resp:
                data = base64.b64decode(resp['result']['data'])
                out_path = '/Applications/XAMPP/xamppfiles/htdocs/Eat&Go_Woocomerce/fab_verified.png'
                with open(out_path, 'wb') as f:
                    f.write(data)
                    f.flush()
                    os.fsync(f.fileno())
                print('SAVED_SUCCESSFULLY:', out_path, 'size:', len(data))
                break

try:
    asyncio.run(run())
finally:
    proc.terminate()
