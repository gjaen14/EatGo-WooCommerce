import subprocess
import time
import json
import urllib.request
import asyncio
import base64
import websockets
import os

OUT_PATH1 = '/Applications/XAMPP/xamppfiles/htdocs/Eat&Go_Woocomerce/fix_desayunos_scroll.png'
OUT_PATH2 = '/Users/jaendev/.gemini/antigravity/brain/1a37f2fd-eda6-4b22-aa59-5653119632b5/fix_desayunos_scroll.png'

async def verify():
    subprocess.run(['pkill', '-9', '-f', 'chrome_verify_scroll'], stderr=subprocess.DEVNULL)
    time.sleep(0.4)

    proc = subprocess.Popen([
        '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
        '--headless=new',
        '--remote-debugging-port=9234',
        '--user-data-dir=/tmp/chrome_verify_scroll',
        '--disable-gpu',
        '--window-size=1280,1000',
        'about:blank'
    ])
    try:
        targets = None
        for i in range(25):
            await asyncio.sleep(0.2)
            try:
                raw = json.loads(urllib.request.urlopen('http://localhost:9234/json').read())
                pages = [t for t in raw if t.get('type') == 'page']
                if pages:
                    targets = pages
                    break
            except Exception:
                pass
        
        ws_url = targets[0]['webSocketDebuggerUrl']
        
        async with websockets.connect(ws_url, max_size=50*1024*1024) as ws:
            await ws.send(json.dumps({'id': 1, 'method': 'Page.navigate', 'params': {'url': 'https://eatgopty.com/'}}))
            while True:
                msg = json.loads(await ws.recv())
                if msg.get('id') == 1:
                    break
            
            await asyncio.sleep(3.5)
            
            # Scroll to desayunos section smoothly
            scroll_js = '''
            (function() {
                var el = document.querySelector('.elementor-element-w_btn_314') || document.querySelector('.elementor-element-2dff3627');
                if (el) {
                    el.scrollIntoView({ behavior: 'instant', block: 'center' });
                    return { scrolled: true };
                }
                window.scrollTo(0, 1500);
                return { scrolled: false, fallback: true };
            })()
            '''
            await ws.send(json.dumps({'id': 2, 'method': 'Runtime.evaluate', 'params': {'expression': scroll_js, 'returnByValue': True}}))
            while True:
                msg = json.loads(await ws.recv())
                if msg.get('id') == 2:
                    print('Scroll eval:', msg.get('result', {}).get('result', {}).get('value'))
                    break
            
            await asyncio.sleep(1.5)
            
            # Capture screenshot
            await ws.send(json.dumps({'id': 3, 'method': 'Page.captureScreenshot'}))
            while True:
                msg = json.loads(await ws.recv())
                if msg.get('id') == 3:
                    img_data = base64.b64decode(msg['result']['data'])
                    for out_path in [OUT_PATH1, OUT_PATH2]:
                        with open(out_path, 'wb') as f:
                            f.write(img_data)
                            f.flush()
                            os.fsync(f.fileno())
                        print('SAVED SCROLL SCREENSHOT:', out_path)
                    break
    finally:
        proc.terminate()

if __name__ == '__main__':
    asyncio.run(verify())
