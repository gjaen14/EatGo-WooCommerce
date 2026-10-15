import subprocess
import json
import urllib.request
import asyncio
import base64
import websockets

subprocess.run(['pkill', '-9', '-f', 'chrome_fab_proof'], stderr=subprocess.DEVNULL)

async def capture():
    proc = subprocess.Popen([
        '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
        '--headless=new',
        '--remote-debugging-port=9228',
        '--user-data-dir=/tmp/chrome_fab_proof',
        '--disable-gpu',
        '--window-size=1280,900',
        'about:blank'
    ])
    try:
        await asyncio.sleep(2.0)
        targets = None
        for _ in range(30):
            try:
                raw = json.loads(urllib.request.urlopen('http://127.0.0.1:9228/json').read())
                pages = [t for t in raw if t.get('type') == 'page']
                if pages:
                    targets = pages
                    break
            except Exception:
                await asyncio.sleep(0.3)
        
        ws_url = targets[0]['webSocketDebuggerUrl']
        
        async with websockets.connect(ws_url, max_size=None) as ws:
            # 1. Navigate to home
            await ws.send(json.dumps({'id': 1, 'method': 'Page.navigate', 'params': {'url': 'https://eatgopty.com/'}}))
            await asyncio.sleep(4.5)

            # 2. Desktop Screenshot
            await ws.send(json.dumps({'id': 2, 'method': 'Page.captureScreenshot'}))
            resp = json.loads(await ws.recv())
            while resp.get('id') != 2:
                resp = json.loads(await ws.recv())
            
            img_data = base64.b64decode(resp['result']['data'])
            with open('fab_cart_desktop.png', 'wb') as f:
                f.write(img_data)
            print('Saved fab_cart_desktop.png successfully!')

            # 3. Mobile Emulation
            await ws.send(json.dumps({
                'id': 3,
                'method': 'Emulation.setDeviceMetricsOverride',
                'params': {
                    'width': 390,
                    'height': 844,
                    'deviceScaleFactor': 2,
                    'mobile': True
                }
            }))
            await asyncio.sleep(1.0)

            await ws.send(json.dumps({'id': 4, 'method': 'Page.captureScreenshot'}))
            resp = json.loads(await ws.recv())
            while resp.get('id') != 4:
                resp = json.loads(await ws.recv())
            
            img_mobile = base64.b64decode(resp['result']['data'])
            with open('fab_cart_mobile.png', 'wb') as f:
                f.write(img_mobile)
            print('Saved fab_cart_mobile.png successfully!')

    finally:
        proc.terminate()

asyncio.run(capture())
