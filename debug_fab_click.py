import urllib.request
import json
import asyncio
import websockets
import subprocess
import time

subprocess.run(['pkill', '-9', '-f', 'chrome_debug_fab'], stderr=subprocess.DEVNULL)
time.sleep(0.5)

proc = subprocess.Popen([
    '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    '--headless=new',
    '--remote-debugging-port=9292',
    '--user-data-dir=/tmp/chrome_debug_fab',
    '--disable-gpu',
    'https://eatgopty.com/menu-del-dia/'
])

async def test():
    for _ in range(25):
        try:
            data = json.loads(urllib.request.urlopen('http://127.0.0.1:9292/json').read())
            break
        except Exception:
            await asyncio.sleep(0.5)
            
    page = [t for t in data if t.get('type') == 'page'][0]
    async with websockets.connect(page['webSocketDebuggerUrl'], max_size=None) as ws:
        async def evaluate(expr):
            req_id = int(time.time() * 1000) % 1000000
            await ws.send(json.dumps({'id': req_id, 'method': 'Runtime.evaluate', 'params': {'expression': expr, 'returnByValue': True}}))
            while True:
                msg = json.loads(await ws.recv())
                if msg.get('id') == req_id:
                    return msg.get('result', {}).get('result', {}).get('value')

        await asyncio.sleep(4.0)

        # Trigger jQuery click on .eatgo-fab-cart
        res = await evaluate("""
        (function() {
            var $ = window.jQuery;
            var $fab = $('.eatgo-fab-cart');
            $fab.trigger('click');
            var widget = $('.elementor-widget-woocommerce-menu-cart');
            var container = $('.elementor-menu-cart__container');
            var main = $('.elementor-menu-cart__main');
            return JSON.stringify({
                fabFound: $fab.length,
                widgetHasClass: widget.hasClass('elementor-menu-cart--shown'),
                containerHasClass: container.hasClass('elementor-menu-cart--shown'),
                containerScale: container.css('transform'),
                mainTransform: main.css('transform'),
                mainOpacity: main.css('opacity')
            });
        })()
        """)
        print("DEBUG RESULT:", json.dumps(res, indent=2))

try:
    asyncio.run(test())
finally:
    proc.terminate()
