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
        '--remote-debugging-port=9288',
        '--user-data-dir=/tmp/chrome_p9288',
        '--disable-gpu',
        '--window-size=1280,1050',
        'about:blank'
    ])
    try:
        await asyncio.sleep(1.5)
        raw = urllib.request.urlopen('http://localhost:9288/json').read()
        targets = json.loads(raw)
        pages = [t for t in targets if t.get('type') == 'page']
        ws_url = pages[0]['webSocketDebuggerUrl']
        
        async with websockets.connect(ws_url, max_size=50*1024*1024) as ws:
            print("Navigating to https://eatgopty.com/ ...")
            await ws.send(json.dumps({'id': 1, 'method': 'Page.navigate', 'params': {'url': 'https://eatgopty.com/'}}))
            await asyncio.sleep(6.0)

            click_js = '''
            (function() {
                var btn = document.querySelector('.elementor-element-w_btn_314 a') || document.querySelector('.elementor-element-w_btn_314');
                if (btn) {
                    btn.scrollIntoView({ behavior: 'instant', block: 'center' });
                    btn.click();
                    return "clicked";
                }
                return "not found";
            })()
            '''
            print("Clicking button...")
            await ws.send(json.dumps({'id': 2, 'method': 'Runtime.evaluate', 'params': {'expression': click_js}}))
            await asyncio.sleep(4.0)

            print("Taking screenshot...")
            await ws.send(json.dumps({'id': 3, 'method': 'Page.captureScreenshot'}))
            resp = json.loads(await ws.recv())
            while resp.get('id') != 3:
                resp = json.loads(await ws.recv())
            
            img_data = base64.b64decode(resp['result']['data'])
            with open('desayuno_modal_verified.png', 'wb') as f:
                f.write(img_data)
            
            with open('/Users/jaendev/.gemini/antigravity/brain/535e662b-3f91-4b37-9e72-7036af9c6a38/desayuno_modal_verified.png', 'wb') as f:
                f.write(img_data)
            print('Saved desayuno_modal_verified.png successfully! Size:', len(img_data))
    finally:
        proc.terminate()

asyncio.run(capture())
