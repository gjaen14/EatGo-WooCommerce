import subprocess
import time
import json
import urllib.request
import asyncio
import base64
import websockets
import os

async def capture():
    # Make sure port 9222 is free
    subprocess.run(['pkill', '-f', 'chrome_test_desayunos'], capture_output=True)
    time.sleep(1)

    proc = subprocess.Popen([
        '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
        '--headless=new',
        '--remote-debugging-port=9240',
        '--user-data-dir=/tmp/chrome_test_desayunos',
        '--disable-gpu',
        '--window-size=1280,1100',
        'about:blank'
    ])
    try:
        targets = None
        for _ in range(20):
            try:
                targets = json.loads(urllib.request.urlopen('http://localhost:9240/json').read())
                break
            except Exception:
                await asyncio.sleep(0.5)
        
        ws_url = targets[0]['webSocketDebuggerUrl']
        
        async with websockets.connect(ws_url, max_size=50*1024*1024) as ws:
            # 0. Enable domains
            await ws.send(json.dumps({'id': 10, 'method': 'Page.enable'}))
            await ws.send(json.dumps({'id': 11, 'method': 'Runtime.enable'}))
            await asyncio.sleep(0.5)

            # 1. Navigate
            print('Navigating...', flush=True)
            await ws.send(json.dumps({'id': 1, 'method': 'Page.navigate', 'params': {'url': 'https://eatgopty.com/'}}))
            await asyncio.sleep(6.0)

            # 2. Click on the Desayuno button (+ Agregar a Comanda)
            print('Clicking + Agregar a Comanda...', flush=True)
            click_js = '''
            (function() {
                var btn = document.querySelector(".elementor-element-w_btn_314 a") || document.querySelector(".elementor-element-w_btn_314");
                if (btn) {
                    btn.scrollIntoView({ behavior: "instant", block: "center" });
                    btn.click();
                    return "clicked";
                }
                return "btn not found";
            })()
            '''
            await ws.send(json.dumps({'id': 2, 'method': 'Runtime.evaluate', 'params': {'expression': click_js}}))
            await asyncio.sleep(4.0)

            # 3. Screenshot
            print('Capturing screenshot...', flush=True)
            await ws.send(json.dumps({'id': 3, 'method': 'Page.captureScreenshot'}))
            while True:
                raw = await ws.recv()
                resp = json.loads(raw)
                if resp.get('id') == 3:
                    img_data = base64.b64decode(resp['result']['data'])
                    out_file = '/Applications/XAMPP/xamppfiles/htdocs/Eat&Go_Woocomerce/desayunos_modal_live.png'
                    with open(out_file, 'wb') as f:
                        f.write(img_data)
                    print(f'Saved {out_file} successfully! Size: {len(img_data)}', flush=True)
                    break
    finally:
        proc.terminate()

asyncio.run(capture())
