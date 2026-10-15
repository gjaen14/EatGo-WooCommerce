import subprocess
import time
import json
import urllib.request
import asyncio
import base64
import websockets

async def capture():
    port = 9226
    proc = subprocess.Popen([
        '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
        '--headless=new',
        f'--remote-debugging-port={port}',
        '--user-data-dir=/tmp/chrome_p9226',
        '--disable-gpu',
        '--window-size=1280,1000',
        'about:blank'
    ])
    try:
        targets = None
        for i in range(20):
            await asyncio.sleep(0.5)
            try:
                targets = json.loads(urllib.request.urlopen(f'http://localhost:{port}/json').read())
                pages = [t for t in targets if t.get('type') == 'page']
                if pages:
                    targets = pages
                    break
            except Exception:
                pass
        
        if not targets:
            raise Exception("No page targets found")

        ws_url = targets[0]['webSocketDebuggerUrl']
        print('Connecting to page ws:', ws_url)
        
        async with websockets.connect(ws_url, max_size=50*1024*1024) as ws:
            print('Navigating to https://eatgopty.com/ ...')
            await ws.send(json.dumps({'id': 1, 'method': 'Page.navigate', 'params': {'url': 'https://eatgopty.com/'}}))
            await asyncio.sleep(6.0)

            # Click breakfast button
            click_js = '''
            (function() {
                var btn = document.querySelector('.elementor-element-w_btn_314 a') || document.querySelector('.elementor-element-w_btn_314');
                if (btn) {
                    btn.scrollIntoView({ behavior: 'instant', block: 'center' });
                    btn.click();
                } else if (typeof woosq_open === 'function') {
                    woosq_open(578);
                }
            })()
            '''
            print('Clicking breakfast button...')
            await ws.send(json.dumps({'id': 2, 'method': 'Runtime.evaluate', 'params': {'expression': click_js}}))
            await asyncio.sleep(4.0)

            print('Capturing screenshot...')
            await ws.send(json.dumps({'id': 10, 'method': 'Page.captureScreenshot'}))
            while True:
                msg = json.loads(await ws.recv())
                if msg.get('id') == 10 and 'result' in msg and 'data' in msg['result']:
                    img_data = base64.b64decode(msg['result']['data'])
                    out_path = '/Applications/XAMPP/xamppfiles/htdocs/Eat&Go_Woocomerce/desayuno_modal_verified.png'
                    with open(out_path, 'wb') as f:
                        f.write(img_data)
                    print('Saved to', out_path, 'size:', len(img_data))
                    
                    artifact_path = '/Users/jaendev/.gemini/antigravity/brain/535e662b-3f91-4b37-9e72-7036af9c6a38/desayuno_modal_verified.png'
                    with open(artifact_path, 'wb') as f:
                        f.write(img_data)
                    print('Saved to artifact:', artifact_path)
                    break
    finally:
        proc.terminate()

if __name__ == '__main__':
    asyncio.run(capture())
