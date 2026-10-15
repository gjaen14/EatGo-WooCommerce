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
        '--remote-debugging-port=9299',
        '--user-data-dir=/tmp/chrome_hero_profile9299',
        '--disable-gpu',
        '--window-size=1280,1050',
        'about:blank'
    ])
    try:
        await asyncio.sleep(2.0)
        targets = json.loads(urllib.request.urlopen('http://localhost:9299/json').read())
        pages = [t for t in targets if t.get('type') == 'page']
        ws_url = pages[0]['webSocketDebuggerUrl']
        
        async with websockets.connect(ws_url) as ws:
            # 1. Navigate to home
            await ws.send(json.dumps({'id': 1, 'method': 'Page.navigate', 'params': {'url': 'https://eatgopty.com/'}}))
            await asyncio.sleep(4.0)

            # Scroll and click Desayuno button
            click_js = '''
            var btn = document.querySelector(".elementor-element-w_btn_314 a") || document.querySelector(".elementor-element-w_btn_314");
            if (btn) {
                btn.scrollIntoView({ behavior: "instant", block: "center" });
                btn.click();
            }
            '''
            await ws.send(json.dumps({'id': 2, 'method': 'Runtime.evaluate', 'params': {'expression': click_js}}))
            await asyncio.sleep(4.0)

            # 2. Modal Screenshot
            await ws.send(json.dumps({'id': 3, 'method': 'Page.captureScreenshot'}))
            resp = json.loads(await ws.recv())
            while resp.get('id') != 3:
                resp = json.loads(await ws.recv())
            
            img_data = base64.b64decode(resp['result']['data'])
            with open('desayuno_modal_verified.png', 'wb') as f:
                f.write(img_data)
            print('Saved desayuno_modal_verified.png successfully!')
    finally:
        proc.terminate()

asyncio.run(capture())
