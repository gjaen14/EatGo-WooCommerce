import subprocess
import time
import json
import urllib.request
import asyncio
import base64
import websockets
import os

OUT_PATH1 = '/Applications/XAMPP/xamppfiles/htdocs/Eat&Go_Woocomerce/fix_verification.png'
OUT_PATH2 = '/Users/jaendev/.gemini/antigravity/brain/1a37f2fd-eda6-4b22-aa59-5653119632b5/fix_verification.png'

async def verify():
    subprocess.run(['pkill', '-9', '-f', 'chrome_verify_fix'], stderr=subprocess.DEVNULL)
    time.sleep(0.4)

    proc = subprocess.Popen([
        '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
        '--headless=new',
        '--remote-debugging-port=9233',
        '--user-data-dir=/tmp/chrome_verify_fix',
        '--disable-gpu',
        '--window-size=1280,1000',
        'about:blank'
    ])
    try:
        targets = None
        for i in range(25):
            await asyncio.sleep(0.2)
            try:
                raw = json.loads(urllib.request.urlopen('http://localhost:9233/json').read())
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
            start_nav = time.time()
            await ws.send(json.dumps({'id': 1, 'method': 'Page.navigate', 'params': {'url': 'https://eatgopty.com/'}}))
            while True:
                msg = json.loads(await ws.recv())
                if msg.get('id') == 1:
                    print('Page navigation ack received:', msg, flush=True)
                    break
            
            # Wait 4 seconds and check main thread responsiveness
            await asyncio.sleep(4.0)
            
            # Send evaluate ping - if main thread is blocked, this will time out
            print('Testing main thread responsiveness with simple evaluation...', flush=True)
            ping_start = time.time()
            await ws.send(json.dumps({
                'id': 2,
                'method': 'Runtime.evaluate',
                'params': {'expression': '({ readyState: document.readyState, fabExists: !!document.querySelector(".eatgo-fab-cart"), title: document.title })', 'returnByValue': True}
            }))
            
            eval_done = False
            while True:
                msg = json.loads(await ws.recv())
                if msg.get('id') == 2:
                    ping_duration = time.time() - ping_start
                    result_val = msg.get('result', {}).get('result', {}).get('value')
                    print(f'MAIN THREAD RESPONSIVE! Ping answered in {ping_duration:.3f}s: {json.dumps(result_val)}', flush=True)
                    eval_done = True
                    break
            
            # Capture screenshot
            print('Capturing verification screenshot...', flush=True)
            await ws.send(json.dumps({'id': 3, 'method': 'Page.captureScreenshot'}))
            while True:
                msg = json.loads(await ws.recv())
                if msg.get('id') == 3:
                    if 'result' in msg and 'data' in msg['result']:
                        img_data = base64.b64decode(msg['result']['data'])
                        for out_path in [OUT_PATH1, OUT_PATH2]:
                            with open(out_path, 'wb') as f:
                                f.write(img_data)
                                f.flush()
                                os.fsync(f.fileno())
                            print('SAVED SCREENSHOT:', out_path, 'bytes:', len(img_data), flush=True)
                    break
    finally:
        proc.terminate()

if __name__ == '__main__':
    asyncio.run(verify())
