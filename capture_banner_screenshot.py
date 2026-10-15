import subprocess
import json
import urllib.request
import asyncio
import base64
import websockets

async def capture():
    proc = subprocess.Popen([
        '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
        '--headless=new',
        '--remote-debugging-port=9227',
        '--user-data-dir=/tmp/chrome_banner_profile',
        '--disable-gpu',
        '--window-size=1280,900',
        'about:blank'
    ])
    try:
        await asyncio.sleep(2.0)
        targets = json.loads(urllib.request.urlopen('http://localhost:9227/json').read())
        ws_url = targets[0]['webSocketDebuggerUrl']
        
        async with websockets.connect(ws_url, max_size=None) as ws:
            # 1. Navigate to home
            await ws.send(json.dumps({'id': 1, 'method': 'Page.navigate', 'params': {'url': 'https://eatgopty.com/'}}))
            await asyncio.sleep(4.0)

            # Scroll to banner
            scroll_js = '''
            (function() {
                var el = document.querySelector('[data-id="429a0b0f"]') || document.querySelector('.elementor-element-429a0b0f');
                if (el) {
                    el.scrollIntoView({ behavior: 'instant', block: 'center' });
                }
            })()
            '''
            await ws.send(json.dumps({'id': 2, 'method': 'Runtime.evaluate', 'params': {'expression': scroll_js}}))
            await asyncio.sleep(1.0)

            # 2. Desktop Screenshot
            await ws.send(json.dumps({'id': 3, 'method': 'Page.captureScreenshot'}))
            resp = json.loads(await ws.recv())
            while resp.get('id') != 3:
                resp = json.loads(await ws.recv())
            
            img_data = base64.b64decode(resp['result']['data'])
            with open('banner_desktop_verified.png', 'wb') as f:
                f.write(img_data)
            print('Saved banner_desktop_verified.png successfully!')

            # 3. Mobile
            await ws.send(json.dumps({
                'id': 4,
                'method': 'Emulation.setDeviceMetricsOverride',
                'params': {
                    'width': 390,
                    'height': 844,
                    'deviceScaleFactor': 2,
                    'mobile': True
                }
            }))
            await asyncio.sleep(1.0)

            await ws.send(json.dumps({'id': 5, 'method': 'Runtime.evaluate', 'params': {'expression': scroll_js}}))
            await asyncio.sleep(0.5)

            await ws.send(json.dumps({'id': 6, 'method': 'Page.captureScreenshot'}))
            resp = json.loads(await ws.recv())
            while resp.get('id') != 6:
                resp = json.loads(await ws.recv())
            
            img_mobile = base64.b64decode(resp['result']['data'])
            with open('banner_mobile_verified.png', 'wb') as f:
                f.write(img_mobile)
            print('Saved banner_mobile_verified.png successfully!')

    finally:
        proc.terminate()

asyncio.run(capture())
