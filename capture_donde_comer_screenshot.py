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
        '--remote-debugging-port=9226',
        '--user-data-dir=/tmp/chrome_p9226',
        '--disable-gpu',
        '--window-size=1280,1000',
        'about:blank'
    ])
    try:
        targets = None
        for i in range(20):
            await asyncio.sleep(0.5)
            try:
                targets = json.loads(urllib.request.urlopen('http://localhost:9226/json').read())
                pages = [t for t in targets if t.get('type') == 'page']
                if pages:
                    targets = pages
                    break
            except Exception:
                pass
        
        if not targets:
            raise Exception("No page targets found")

        ws_url = targets[0]['webSocketDebuggerUrl']
        print('Connecting to page ws:', ws_url)
        
        async with websockets.connect(ws_url) as ws:
            print('Navigating to https://eatgopty.com/donde-comer-y-retirar/ ...')
            await ws.send(json.dumps({'id': 1, 'method': 'Page.navigate', 'params': {'url': 'https://eatgopty.com/donde-comer-y-retirar/'}}))
            await asyncio.sleep(4.0)

            # Scroll into view of .elementor-element-turnosp
            scroll_js = '''
            (function() {
                var el = document.querySelector('.elementor-element-turnosp') || document.querySelector('[data-id="turnosp"]');
                if (el) {
                    el.scrollIntoView({ behavior: 'instant', block: 'center' });
                }
            })()
            '''
            await ws.send(json.dumps({'id': 2, 'method': 'Runtime.evaluate', 'params': {'expression': scroll_js}}))
            await asyncio.sleep(1.0)

            print('Capturing screenshot...')
            await ws.send(json.dumps({'id': 3, 'method': 'Page.captureScreenshot'}))
            while True:
                msg = json.loads(await ws.recv())
                if msg.get('id') == 3 and 'result' in msg and 'data' in msg['result']:
                    img_data = base64.b64decode(msg['result']['data'])
                    with open('turnos_pagos_verified.png', 'wb') as f:
                        f.write(img_data)
                    print('Saved turnos_pagos_verified.png, size:', len(img_data))
                    break
    finally:
        proc.terminate()

asyncio.run(capture())
