import subprocess
import time
import json
import urllib.request
import asyncio
import base64
import websockets
import os

subprocess.run(['pkill', '-9', '-f', 'chrome_final_proof'], stderr=subprocess.DEVNULL)
time.sleep(1)

OUT_FILE = '/Users/jaendev/.gemini/antigravity/brain/f180faf7-7a71-484e-b640-c77ee658b798/fab_cart_menu_del_dia.png'

async def capture():
    proc = subprocess.Popen([
        '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
        '--headless=new',
        '--remote-debugging-port=9229',
        '--user-data-dir=/tmp/chrome_final_proof',
        '--disable-gpu',
        '--window-size=1280,950',
        'about:blank'
    ])
    try:
        targets = None
        for i in range(30):
            await asyncio.sleep(0.3)
            try:
                raw = json.loads(urllib.request.urlopen('http://localhost:9229/json').read())
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
            # Enable page
            await ws.send(json.dumps({'id': 1, 'method': 'Page.enable'}))
            
            # Navigate
            await ws.send(json.dumps({'id': 2, 'method': 'Page.navigate', 'params': {'url': 'https://eatgopty.com/menu-del-dia/'}}))
            await asyncio.sleep(5.0)

            # Capture screenshot
            await ws.send(json.dumps({'id': 3, 'method': 'Page.captureScreenshot'}))
            
            while True:
                msg = json.loads(await ws.recv())
                if msg.get('id') == 3 and 'result' in msg and 'data' in msg['result']:
                    data = base64.b64decode(msg['result']['data'])
                    with open(OUT_FILE, 'wb') as f:
                        f.write(data)
                        f.flush()
                        os.fsync(f.fileno())
                    print('CAPTURED_SUCCESSFULLY:', OUT_FILE, 'Bytes:', len(data))
                    break
            
            await asyncio.sleep(0.5)
    finally:
        proc.terminate()

if __name__ == '__main__':
    asyncio.run(capture())
