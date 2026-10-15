import subprocess
import time
import json
import urllib.request
import asyncio
import base64
import websockets

async def capture():
    subprocess.run(['pkill', '-f', 'remote-debugging-port=9223'], capture_output=True)
    await asyncio.sleep(1.0)
    proc = subprocess.Popen([
        '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
        '--headless=new',
        '--remote-debugging-port=9223',
        '--user-data-dir=/tmp/chrome_home_profile',
        '--disable-gpu',
        '--window-size=1280,1000',
        'about:blank'
    ])
    try:
        await asyncio.sleep(2.0)
        targets = json.loads(urllib.request.urlopen('http://localhost:9223/json').read())
        ws_url = targets[0]['webSocketDebuggerUrl']
        
        async with websockets.connect(ws_url) as ws:
            # 1. Navigate to home
            await ws.send(json.dumps({'id': 1, 'method': 'Page.navigate', 'params': {'url': 'https://eatgopty.com/'}}))
            await asyncio.sleep(3.5)

            # 2. Scroll to section desayunos and click
            scroll_js = '''
            (function() {
                var btn = document.querySelector(".elementor-element-w_btn_314 a") || document.querySelector(".elementor-element-w_btn_314");
                if (btn) {
                    btn.scrollIntoView({ behavior: 'instant', block: 'center' });
                    btn.click();
                    return "clicked";
                }
                return "not found";
            })()
            '''
            await ws.send(json.dumps({'id': 2, 'method': 'Runtime.evaluate', 'params': {'expression': scroll_js}}))
            await asyncio.sleep(4.0)

            # 3. Screenshot
            await ws.send(json.dumps({'id': 3, 'method': 'Page.captureScreenshot'}))
            resp = json.loads(await ws.recv())
            while resp.get('id') != 3:
                resp = json.loads(await ws.recv())
            
            print('RESP keys:', list(resp.keys()))
            if 'error' in resp:
                print('Error capturing screenshot:', resp['error'])
            else:
                img_data = base64.b64decode(resp['result']['data'])
                with open('desayuno_modal_verified.png', 'wb') as f:
                    f.write(img_data)
                print('Saved desayuno_modal_verified.png successfully!')
    finally:
        proc.terminate()

asyncio.run(capture())
