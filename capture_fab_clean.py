import subprocess
import time
import json
import urllib.request
import asyncio
import base64
import websockets
import os

subprocess.run(['pkill', '-9', '-f', 'chrome_fab_profile'], stderr=subprocess.DEVNULL)
time.sleep(1)

OUT_PATH = '/Users/jaendev/.gemini/antigravity/brain/f180faf7-7a71-484e-b640-c77ee658b798/fab_cart_verified.png'
os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)

async def capture():
    proc = subprocess.Popen([
        '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
        '--headless=new',
        '--remote-debugging-port=9223',
        '--user-data-dir=/tmp/chrome_fab_profile',
        '--disable-gpu',
        '--window-size=1280,1000',
        'about:blank'
    ])
    try:
        await asyncio.sleep(2.5)
        targets = json.loads(urllib.request.urlopen('http://localhost:9223/json').read())
        ws_url = targets[0]['webSocketDebuggerUrl']
        
        async with websockets.connect(ws_url) as ws:
            # 1. Navigate to menu del dia
            await ws.send(json.dumps({'id': 1, 'method': 'Page.navigate', 'params': {'url': 'https://eatgopty.com/menu-del-dia/'}}))
            await asyncio.sleep(4.5)

            # 2. Screenshot
            await ws.send(json.dumps({'id': 3, 'method': 'Page.captureScreenshot'}))
            resp = json.loads(await ws.recv())
            while resp.get('id') != 3:
                resp = json.loads(await ws.recv())
            
            img_data = base64.b64decode(resp['result']['data'])
            with open(OUT_PATH, 'wb') as f:
                f.write(img_data)
                f.flush()
                os.fsync(f.fileno())
            print('Saved to OUT_PATH successfully! Bytes:', len(img_data), 'Exists:', os.path.exists(OUT_PATH))
    finally:
        proc.terminate()

asyncio.run(capture())
