import subprocess
import time
import json
import urllib.request
import asyncio
import base64
import websockets

subprocess.run(['pkill', '-9', '-f', 'chrome_test_profile'], stderr=subprocess.DEVNULL)
time.sleep(1)

async def capture():
    proc = subprocess.Popen([
        '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
        '--headless=new',
        '--remote-debugging-port=9222',
        '--user-data-dir=/tmp/chrome_test_profile',
        '--disable-gpu',
        '--window-size=1280,1400',
        'about:blank'
    ])
    try:
        targets = None
        for _ in range(30):
            try:
                targets = json.loads(urllib.request.urlopen('http://127.0.0.1:9222/json').read())
                if targets:
                    break
            except Exception:
                await asyncio.sleep(0.5)
        
        if not targets:
            raise Exception("DevTools port never opened")
        
        ws_url = targets[0]['webSocketDebuggerUrl']
        
        async with websockets.connect(ws_url, max_size=50*1024*1024) as ws:
            # 1. Navigate
            await ws.send(json.dumps({'id': 1, 'method': 'Page.navigate', 'params': {'url': 'https://eatgopty.com/menu-del-dia/'}}))
            await asyncio.sleep(5.0)

            # 2. Screenshot
            await ws.send(json.dumps({'id': 3, 'method': 'Page.captureScreenshot'}))
            resp = json.loads(await ws.recv())
            while resp.get('id') != 3:
                resp = json.loads(await ws.recv())
            
            img_data = base64.b64decode(resp['result']['data'])
            with open('/Applications/XAMPP/xamppfiles/htdocs/Eat&Go_Woocomerce/fab_cart_evidence.png', 'wb') as f:
                f.write(img_data)
            print('SUCCESS_SAVED_EVIDENCE:', len(img_data))
    finally:
        proc.terminate()

asyncio.run(capture())
