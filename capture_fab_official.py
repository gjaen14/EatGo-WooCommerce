import subprocess
import time
import json
import urllib.request
import asyncio
import base64
import websockets
import os

OUT_PATH = '/Applications/XAMPP/xamppfiles/htdocs/Eat&Go_Woocomerce/fab_verified_live.png'

async def capture():
    # Kill any lingering instances
    subprocess.run(['pkill', '-9', '-f', 'chrome_p9227'], stderr=subprocess.DEVNULL)
    time.sleep(0.5)

    proc = subprocess.Popen([
        '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
        '--headless=new',
        '--remote-debugging-port=9227',
        '--user-data-dir=/tmp/chrome_p9227',
        '--disable-gpu',
        '--window-size=1280,1000',
        'about:blank'
    ])
    try:
        targets = None
        for i in range(20):
            await asyncio.sleep(0.2)
            try:
                raw = json.loads(urllib.request.urlopen('http://localhost:9227/json').read())
                pages = [t for t in raw if t.get('type') == 'page']
                if pages:
                    targets = pages
                    break
            except Exception:
                pass
        
        if not targets:
            raise Exception("No page targets found")

        ws_url = targets[0]['webSocketDebuggerUrl']
        
        async with websockets.connect(ws_url, max_size=50*1024*1024) as ws:
            await ws.send(json.dumps({'id': 1, 'method': 'Page.navigate', 'params': {'url': 'https://eatgopty.com/menu-del-dia/'}}))
            
            # Poll for FAB element in DOM
            check_js = '''
            (function() {
                var fab = document.querySelector('.eatgo-fab-cart');
                return fab ? {
                    found: true,
                    text: fab.innerText.trim(),
                    display: window.getComputedStyle(fab).display,
                    position: window.getComputedStyle(fab).position,
                    zIndex: window.getComputedStyle(fab).zIndex
                } : { found: false };
            })()
            '''
            
            fab_found = False
            for step in range(12):
                await asyncio.sleep(0.5)
                req_id = 100 + step
                await ws.send(json.dumps({'id': req_id, 'method': 'Runtime.evaluate', 'params': {'expression': check_js, 'returnByValue': True}}))
                while True:
                    msg = json.loads(await ws.recv())
                    if msg.get('id') == req_id and 'result' in msg and 'value' in msg['result']:
                        val = msg['result']['value']
                        if val.get('found'):
                            print('FAB FOUND IN DOM:', json.dumps(val))
                            fab_found = True
                        break
                if fab_found:
                    break
            
            # Brief pause for styles/animation render
            await asyncio.sleep(1.0)

            # Capture screenshot
            await ws.send(json.dumps({'id': 3, 'method': 'Page.captureScreenshot'}))
            while True:
                msg = json.loads(await ws.recv())
                if msg.get('id') == 3 and 'result' in msg and 'data' in msg['result']:
                    img_data = base64.b64decode(msg['result']['data'])
                    with open(OUT_PATH, 'wb') as f:
                        f.write(img_data)
                        f.flush()
                        os.fsync(f.fileno())
                    print('FILE_SAVED_COMPLETELY:', OUT_PATH, 'bytes:', len(img_data))
                    break
    finally:
        proc.terminate()

if __name__ == '__main__':
    asyncio.run(capture())
