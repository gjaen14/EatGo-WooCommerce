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
        '--user-data-dir=/tmp/chrome_test_desayunos_exact',
        '--disable-gpu',
        '--window-size=1280,1100',
        'about:blank'
    ])
    try:
        for _ in range(15):
            try:
                targets = json.loads(urllib.request.urlopen('http://localhost:9288/json').read())
                break
            except Exception:
                await asyncio.sleep(0.5)
        targets = json.loads(urllib.request.urlopen('http://localhost:9288/json').read())
        pages = [t for t in targets if t.get('type') == 'page']
        ws_url = pages[0]['webSocketDebuggerUrl']
        
        async with websockets.connect(ws_url, max_size=50*1024*1024) as ws:
            # 1. Navigate
            await ws.send(json.dumps({'id': 1, 'method': 'Page.navigate', 'params': {'url': 'https://eatgopty.com/'}}))
            await asyncio.sleep(5.0)

            # 2. Click on Desayuno button
            click_js = '''
            (function() {
                var p = document.querySelector(".elementor-element-w_btn_314 a") || document.querySelector(".elementor-element-w_btn_314");
                console.log("BUTTON FOUND:", p);
                if (p) {
                    p.scrollIntoView({ behavior: 'instant', block: 'center' });
                    p.click();
                }
            })()
            '''
            await ws.send(json.dumps({'id': 2, 'method': 'Runtime.evaluate', 'params': {'expression': click_js}}))
            await asyncio.sleep(4.0)

            # 2.5 Inspect what is in DOM
            dom_js = """
            (function() {
                var popup = document.querySelector('.woosq-popup');
                var mfp = document.querySelector('.mfp-content');
                var title = document.querySelector('.woosq-product .product_title') || document.querySelector('.product_title');
                return {
                    hasPopup: !!popup,
                    popupClass: popup ? popup.className : null,
                    hasMfp: !!mfp,
                    hasTitle: !!title,
                    titleText: title ? title.innerText : null
                };
            })()
            """
            await ws.send(json.dumps({'id': 10, 'method': 'Runtime.evaluate', 'params': {'expression': dom_js, 'returnByValue': True}}))
            r = json.loads(await ws.recv())
            while r.get('id') != 10:
                r = json.loads(await ws.recv())
            print('DOM INSPECT:', json.dumps(r.get('result', {}).get('result', {}).get('value'), indent=2))

            # 3. Screenshot
            await ws.send(json.dumps({'id': 3, 'method': 'Page.captureScreenshot'}))
            resp = json.loads(await ws.recv())
            while resp.get('id') != 3:
                resp = json.loads(await ws.recv())
            
            img_data = base64.b64decode(resp['result']['data'])
            save_path = '/Users/jaendev/.gemini/antigravity/brain/535e662b-3f91-4b37-9e72-7036af9c6a38/desayuno_modal_verified.png'
            with open(save_path, 'wb') as f:
                f.write(img_data)
            print(f'Saved {save_path} successfully!')
    finally:
        proc.terminate()

asyncio.run(capture())
