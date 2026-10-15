import subprocess
import time
import json
import urllib.request
import asyncio
import base64
import websockets
import os
import sys

async def main():
    print('Starting Chrome...', flush=True)
    proc = subprocess.Popen([
        '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
        '--headless=new',
        '--remote-debugging-port=9228',
        '--user-data-dir=/tmp/chrome_p9228',
        '--disable-gpu',
        '--window-size=1280,1000',
        'about:blank'
    ])
    try:
        targets = None
        for i in range(25):
            try:
                targets = json.loads(urllib.request.urlopen('http://localhost:9228/json').read())
                print('Connected to Chrome!', flush=True)
                break
            except Exception:
                await asyncio.sleep(0.5)
        
        if not targets:
            print('Failed to reach Chrome port 9228', flush=True)
            return

        ws_url = targets[0]['webSocketDebuggerUrl']
        print('Connecting ws:', ws_url, flush=True)
        
        async with websockets.connect(ws_url, max_size=50*1024*1024) as ws:
            async def send_eval(expr, await_promise=False):
                cmd_id = int(time.time() * 1000) % 1000000
                payload = {
                    'id': cmd_id,
                    'method': 'Runtime.evaluate',
                    'params': {
                        'expression': expr,
                        'returnByValue': True,
                        'awaitPromise': await_promise
                    }
                }
                await ws.send(json.dumps(payload))
                while True:
                    msg = json.loads(await ws.recv())
                    if msg.get('id') == cmd_id:
                        return msg.get('result', {}).get('result', {}).get('value')

            print('1. Navigating to https://eatgopty.com/ ...', flush=True)
            await ws.send(json.dumps({'id': 1, 'method': 'Page.navigate', 'params': {'url': 'https://eatgopty.com/'}}))
            while True:
                msg = json.loads(await ws.recv())
                if msg.get('id') == 1:
                    break

            print('2. Waiting for Desayunos section and button...', flush=True)
            wait_and_click_js = '''
            new Promise((resolve) => {
                var start = Date.now();
                var timer = setInterval(function() {
                    var btn = document.querySelector(".elementor-element-w_btn_314 a") || document.querySelector(".elementor-element-w_btn_314");
                    if (btn) {
                        clearInterval(timer);
                        btn.scrollIntoView({ behavior: "instant", block: "center" });
                        var pid = btn.getAttribute("data-id") || 578;
                        if (typeof woosq_open === "function") {
                            woosq_open(pid);
                            resolve({ status: "woosq_open", pid: pid, btnText: btn.innerText });
                        } else {
                            btn.click();
                            resolve({ status: "clicked", pid: pid, btnText: btn.innerText });
                        }
                    } else if (Date.now() - start > 20000) {
                        clearInterval(timer);
                        resolve({ status: "timeout" });
                    }
                }, 400);
            })
            '''
            click_res = await send_eval(wait_and_click_js, await_promise=True)
            print('Click result:', click_res, flush=True)

            print('3. Waiting for Quick View modal popup...', flush=True)
            wait_modal_js = '''
            new Promise((resolve) => {
                var start = Date.now();
                var timer = setInterval(function() {
                    var popup = document.querySelector(".woosq-popup");
                    var title = document.querySelector(".woosq-product .product_title, .woosq-popup h1, .woosq-popup .product_title");
                    var price = document.querySelector(".woosq-product .price");
                    if (popup && title) {
                        clearInterval(timer);
                        resolve({
                            isOpen: true,
                            title: title.innerText.trim(),
                            price: price ? price.innerText.trim() : ""
                        });
                    } else if (Date.now() - start > 10000) {
                        clearInterval(timer);
                        resolve({ isOpen: false });
                    }
                }, 300);
            })
            '''
            modal_res = await send_eval(wait_modal_js, await_promise=True)
            print('Modal result:', modal_res, flush=True)

            # Wait another 1s for images to render
            await asyncio.sleep(1.5)

            print('4. Capturing screenshot...', flush=True)
            ss_id = 9999
            await ws.send(json.dumps({'id': ss_id, 'method': 'Page.captureScreenshot'}))
            while True:
                msg = json.loads(await ws.recv())
                if msg.get('id') == ss_id:
                    data = base64.b64decode(msg['result']['data'])
                    base_dir = os.path.dirname(os.path.abspath(__file__))
                    out_path1 = os.path.join(base_dir, 'desayuno_modal_verified.png')
                    out_path2 = '/Users/jaendev/.gemini/antigravity/brain/535e662b-3f91-4b37-9e72-7036af9c6a38/desayuno_modal_verified.png'
                    for p in [out_path1, out_path2]:
                        with open(p, 'wb') as f:
                            f.write(data)
                        print(f'WROTE FILE: {p} (size={os.path.getsize(p)})', flush=True)
                    break
    finally:
        print('Terminating Chrome...', flush=True)
        proc.terminate()

asyncio.run(main())
