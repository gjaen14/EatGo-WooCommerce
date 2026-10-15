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
        '--remote-debugging-port=9222',
        '--user-data-dir=/tmp/chrome_test_profile',
        '--disable-gpu',
        '--window-size=1280,1400',
        'about:blank'
    ])
    try:
        await asyncio.sleep(1.5)
        targets = json.loads(urllib.request.urlopen('http://localhost:9222/json').read())
        ws_url = targets[0]['webSocketDebuggerUrl']
        
        async with websockets.connect(ws_url) as ws:
            # 1. Navigate
            await ws.send(json.dumps({'id': 1, 'method': 'Page.navigate', 'params': {'url': 'https://eatgopty.com/menu-semanal/'}}))
            await asyncio.sleep(3.5)

            # 2. Click on Martes
            click_js = '''
            (function() {
                var p = document.querySelector('[data-id="407669ce"], [data-interaction-id="407669ce"]') ||
                        Array.from(document.querySelectorAll("p")).find(el => el.textContent.includes("MARTES"));
                if (p) p.click();
            })()
            '''
            await ws.send(json.dumps({'id': 2, 'method': 'Runtime.evaluate', 'params': {'expression': click_js}}))
            await asyncio.sleep(0.8)

            # 3. Screenshot
            await ws.send(json.dumps({'id': 3, 'method': 'Page.captureScreenshot'}))
            resp = json.loads(await ws.recv())
            # Receive until id 3
            while resp.get('id') != 3:
                resp = json.loads(await ws.recv())
            
            img_data = base64.b64decode(resp['result']['data'])
            with open('menu_martes_interactive.png', 'wb') as f:
                f.write(img_data)
            print('Saved menu_martes_interactive.png successfully!')
    finally:
        proc.terminate()

asyncio.run(capture())
