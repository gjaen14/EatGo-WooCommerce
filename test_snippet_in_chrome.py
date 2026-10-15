import urllib.request
import json
import asyncio
import websockets
import subprocess
import time

subprocess.run(['pkill', '-9', '-f', 'chrome_test_snippet'], stderr=subprocess.DEVNULL)
time.sleep(0.5)

proc = subprocess.Popen([
    '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    '--headless=new',
    '--remote-debugging-port=9294',
    '--user-data-dir=/tmp/chrome_test_snippet',
    '--disable-gpu',
    'https://eatgopty.com/menu-del-dia/'
])

async def test():
    await asyncio.sleep(4.0)
    data = json.loads(urllib.request.urlopen('http://127.0.0.1:9294/json').read())
    page = [t for t in data if t.get('type') == 'page'][0]
    async with websockets.connect(page['webSocketDebuggerUrl'], max_size=None) as ws:
        js = """
        (function() {
            var snippetInHtml = document.body.innerHTML.includes('syncCardQuickViewButtons');
            return {
                snippetInHtml: snippetInHtml,
                fnExists: typeof syncCardQuickViewButtons,
                loopItemsCount: document.querySelectorAll('.e-loop-item').length
            };
        })()
        """
        await ws.send(json.dumps({'id': 1, 'method': 'Runtime.evaluate', 'params': {'expression': js, 'returnByValue': True}}))
        while True:
            msg = json.loads(await ws.recv())
            if msg.get('id') == 1:
                print('TEST RESULT:', msg['result']['result']['value'])
                break

try:
    asyncio.run(test())
finally:
    proc.terminate()
