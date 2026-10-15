import subprocess
import time
import json
import urllib.request
import asyncio
import base64
import websockets
import os

async def capture():
    # Kill any existing chrome instances on 9226
    proc = subprocess.Popen([
        '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
        '--headless=new',
        '--remote-debugging-port=9226',
        '--user-data-dir=/tmp/chrome_desayuno_profile',
        '--disable-gpu',
        '--window-size=1280,1000',
        'about:blank'
    ])
    try:
        targets = None
        for _ in range(15):
            try:
                targets = json.loads(urllib.request.urlopen('http://localhost:9226/json').read())
                break
            except Exception:
                await asyncio.sleep(0.5)
        if not targets:
            raise RuntimeError("Chrome failed to start")
        ws_url = targets[0]['webSocketDebuggerUrl']
        
        async with websockets.connect(ws_url, max_size=50*1024*1024) as ws:
            # 1. Navigate to home
            await ws.send(json.dumps({'id': 1, 'method': 'Page.navigate', 'params': {'url': 'https://eatgopty.com/'}}))
            await asyncio.sleep(4.0)

            # 2. Scroll to Desayunos section and trigger click on first button
            click_js = '''
            (function() {
                var btn = document.querySelector('.elementor-element-w_btn_314 a') || document.querySelector('.elementor-element-w_btn_314');
                if (btn) {
                    btn.scrollIntoView({ behavior: 'instant', block: 'center' });
                    // Trigger click via jQuery to ensure all handlers run
                    if (window.jQuery) {
                        window.jQuery(btn).trigger('click');
                    } else {
                        btn.click();
                    }
                    return "clicked";
                }
                return "not found";
            })()
            '''
            await ws.send(json.dumps({'id': 2, 'method': 'Runtime.evaluate', 'params': {'expression': click_js}}))
            await asyncio.sleep(4.0)

            # 3. Screenshot
            await ws.send(json.dumps({'id': 3, 'method': 'Page.captureScreenshot', 'params': {'format': 'png'}}))
            
            while True:
                msg = json.loads(await ws.recv())
                if msg.get('id') == 3:
                    img_data = base64.b64decode(msg['result']['data'])
                    out = 'desayunos_modal_verified.png'
                    with open(out, 'wb') as f:
                        f.write(img_data)
                    print(f'Saved {out} successfully! Size: {len(img_data)}')
                    break
    finally:
        proc.terminate()

asyncio.run(capture())
