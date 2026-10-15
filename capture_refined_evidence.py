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
        '--remote-debugging-port=9229',
        '--user-data-dir=/tmp/chrome_p9229',
        '--disable-gpu',
        '--window-size=1280,1050',
        'about:blank'
    ])
    try:
        targets = None
        for i in range(25):
            await asyncio.sleep(0.4)
            try:
                targets = json.loads(urllib.request.urlopen('http://localhost:9229/json').read())
                pages = [t for t in targets if t.get('type') == 'page']
                if pages:
                    targets = pages
                    break
            except Exception:
                pass
        
        ws_url = targets[0]['webSocketDebuggerUrl']
        async with websockets.connect(ws_url) as ws:
            print('Navigating to https://eatgopty.com/donde-comer-y-retirar/ ...')
            await ws.send(json.dumps({'id': 1, 'method': 'Page.navigate', 'params': {'url': 'https://eatgopty.com/donde-comer-y-retirar/'}}))
            await asyncio.sleep(5.0)

            # Scroll to top
            await ws.send(json.dumps({'id': 2, 'method': 'Runtime.evaluate', 'params': {'expression': 'window.scrollTo(0, 0)'}}))
            await asyncio.sleep(0.5)

            # Capture screenshot
            print('Capturing refined top screenshot...')
            await ws.send(json.dumps({'id': 3, 'method': 'Page.captureScreenshot'}))
            while True:
                msg = json.loads(await ws.recv())
                if msg.get('id') == 3 and 'result' in msg and 'data' in msg['result']:
                    img_data = base64.b64decode(msg['result']['data'])
                    with open('evidence_refined_corporate_section.png', 'wb') as f:
                        f.write(img_data)
                    print('Saved evidence_refined_corporate_section.png')
                    break
    finally:
        proc.terminate()

asyncio.run(capture())
