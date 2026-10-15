import subprocess
import time
import json
import urllib.request
import asyncio
import base64
import websockets
import os

OUT_PATH1 = '/Applications/XAMPP/xamppfiles/htdocs/Eat&Go_Woocomerce/desayuno_modal_verified.png'
OUT_PATH2 = '/Users/jaendev/.gemini/antigravity/brain/535e662b-3f91-4b37-9e72-7036af9c6a38/desayuno_modal_verified.png'

async def capture():
    # Kill any lingering instances
    subprocess.run(['pkill', '-9', '-f', 'chrome_p9229'], stderr=subprocess.DEVNULL)
    time.sleep(0.5)

    proc = subprocess.Popen([
        '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
        '--headless=new',
        '--remote-debugging-port=9229',
        '--user-data-dir=/tmp/chrome_p9229',
        '--disable-gpu',
        '--window-size=1280,1000',
        'about:blank'
    ])
    try:
        targets = None
        for i in range(25):
            await asyncio.sleep(0.2)
            try:
                raw = json.loads(urllib.request.urlopen('http://localhost:9229/json').read())
                pages = [t for t in raw if t.get('type') == 'page']
                if pages:
                    targets = pages
                    break
            except Exception:
                pass
        
        if not targets:
            raise Exception("No page targets found")

        ws_url = targets[0]['webSocketDebuggerUrl']
        print('Connected to ws:', ws_url, flush=True)
        
        async with websockets.connect(ws_url, max_size=50*1024*1024) as ws:
            print('Navigating to https://eatgopty.com/ ...', flush=True)
            await ws.send(json.dumps({'id': 1, 'method': 'Page.navigate', 'params': {'url': 'https://eatgopty.com/'}}))
            while True:
                msg = json.loads(await ws.recv())
                if msg.get('id') == 1:
                    print('Page navigation initiated:', msg, flush=True)
                    break
            
            print('Waiting 6s for page to load scripts and Elementor...', flush=True)
            await asyncio.sleep(6.0)
            
            # Step 1: Wait and find/click breakfast button
            click_js = '''
            (function() {
                var btn = document.querySelector('.elementor-element-w_btn_314 a') || document.querySelector('.elementor-element-w_btn_314');
                if (btn) {
                    btn.scrollIntoView({ behavior: 'instant', block: 'center' });
                    var pid = btn.getAttribute('data-id') || 578;
                    if (typeof woosq_open === 'function') {
                        woosq_open(pid);
                    } else {
                        btn.click();
                    }
                    return { clicked: true, text: btn.innerText.trim(), pid: pid };
                }
                return { clicked: false };
            })()
            '''
            
            btn_clicked = False
            for step in range(20):
                await asyncio.sleep(0.5)
                req_id = 100 + step
                await ws.send(json.dumps({'id': req_id, 'method': 'Runtime.evaluate', 'params': {'expression': click_js, 'returnByValue': True}}))
                while True:
                    msg = json.loads(await ws.recv())
                    if msg.get('id') == req_id:
                        res_obj = msg.get('result', {}).get('result', {})
                        val = res_obj.get('value') or {}
                        if isinstance(val, dict) and val.get('clicked'):
                            print('BUTTON CLICKED SUCCESSFULLY:', json.dumps(val), flush=True)
                            btn_clicked = True
                        break
                if btn_clicked:
                    break

            if not btn_clicked:
                print('WARNING: Button not clicked during poll', flush=True)

            # Step 2: Poll for modal popup
            modal_js = '''
            (function() {
                var popup = document.querySelector('.woosq-popup') || document.querySelector('#woosq-popup');
                var title = document.querySelector('.woosq-product .product_title, .woosq-popup .product_title');
                var price = document.querySelector('.woosq-product .price');
                if (popup) {
                    return {
                        found: true,
                        title: title ? title.innerText.trim() : null,
                        price: price ? price.innerText.trim() : null
                    };
                }
                return { found: false };
            })()
            '''
            
            modal_opened = False
            for step in range(25):
                await asyncio.sleep(0.4)
                req_id = 200 + step
                await ws.send(json.dumps({'id': req_id, 'method': 'Runtime.evaluate', 'params': {'expression': modal_js, 'returnByValue': True}}))
                while True:
                    msg = json.loads(await ws.recv())
                    if msg.get('id') == req_id:
                        res_obj = msg.get('result', {}).get('result', {})
                        val = res_obj.get('value') or {}
                        if isinstance(val, dict) and val.get('found'):
                            print('MODAL DETECTED OPEN:', json.dumps(val), flush=True)
                            modal_opened = True
                        break
                if modal_opened:
                    break

            # Brief pause for image and animations to render
            await asyncio.sleep(2.0)

            # Step 3: Capture screenshot
            print('Capturing screenshot...', flush=True)
            await ws.send(json.dumps({'id': 3, 'method': 'Page.captureScreenshot'}))
            while True:
                msg = json.loads(await ws.recv())
                if msg.get('id') == 3:
                    if 'error' in msg:
                        print('Screenshot error:', msg['error'], flush=True)
                        break
                    if 'result' in msg and 'data' in msg['result']:
                        img_data = base64.b64decode(msg['result']['data'])
                        for out_path in [OUT_PATH1, OUT_PATH2]:
                            with open(out_path, 'wb') as f:
                                f.write(img_data)
                                f.flush()
                                os.fsync(f.fileno())
                            print('FILE_SAVED_COMPLETELY:', out_path, 'bytes:', len(img_data), flush=True)
                        break
    finally:
        proc.terminate()

if __name__ == '__main__':
    asyncio.run(capture())
