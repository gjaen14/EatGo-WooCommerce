import urllib.request
import json
import asyncio
import websockets
import subprocess
import time
import base64

subprocess.run(['pkill', '-9', '-f', 'chrome_drawer_capture'], stderr=subprocess.DEVNULL)
time.sleep(0.5)

proc = subprocess.Popen([
    '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    '--headless=new',
    '--remote-debugging-port=9291',
    '--user-data-dir=/tmp/chrome_drawer_capture_' + str(int(time.time())),
    '--incognito',
    '--disable-cache',
    '--disable-gpu',
    '--window-size=1280,900',
    'https://eatgopty.com/menu-del-dia/'
])

async def capture_drawer():
    page = None
    for _ in range(30):
        try:
            data = json.loads(urllib.request.urlopen('http://127.0.0.1:9291/json').read())
            pages = [t for t in data if t.get('type') == 'page']
            if pages:
                page = pages[0]
                break
        except Exception:
            await asyncio.sleep(0.3)
            
    if not page:
        return

    ws_url = page['webSocketDebuggerUrl']
    async with websockets.connect(ws_url, max_size=None) as ws:
        await asyncio.sleep(4.0)

        # Directly click FAB
        js_fab = """
        (function() {
            var fab = document.querySelector('.eatgo-fab-cart');
            if (fab) {
                fab.click();
                return 'Clicked FAB';
            }
            return 'No FAB';
        })()
        """
        await ws.send(json.dumps({'id': 1, 'method': 'Runtime.evaluate', 'params': {'expression': js_fab, 'returnByValue': True}}))
        while True:
            msg = json.loads(await ws.recv())
            if msg.get('id') == 1:
                print('FAB CLICK:', msg['result']['result']['value'])
                break

        await asyncio.sleep(2.0)

        await ws.send(json.dumps({'id': 2, 'method': 'Page.captureScreenshot'}))
        while True:
            msg = json.loads(await ws.recv())
            if msg.get('id') == 2 and 'result' in msg:
                img_data = base64.b64decode(msg['result']['data'])
                with open('fab_drawer_open_clean.png', 'wb') as f:
                    f.write(img_data)
                print('SAVED: fab_drawer_open_clean.png')
                break

try:
    asyncio.run(capture_drawer())
finally:
    proc.terminate()
