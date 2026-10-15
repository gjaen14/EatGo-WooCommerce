import urllib.request
import json
import asyncio
import websockets
import subprocess
import time
import base64

subprocess.run(['pkill', '-9', '-f', 'chrome_live_verify'], stderr=subprocess.DEVNULL)
time.sleep(0.5)

proc = subprocess.Popen([
    '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    '--headless=new',
    '--remote-debugging-port=9300',
    '--user-data-dir=/tmp/chrome_live_verify',
    '--window-size=1280,450',
    '--disable-gpu',
    'about:blank'
])

async def run():
    for _ in range(25):
        try:
            data = json.loads(urllib.request.urlopen('http://127.0.0.1:9300/json').read())
            break
        except Exception:
            await asyncio.sleep(0.3)
            
    page = [t for t in data if t.get('type') == 'page'][0]
    async with websockets.connect(page['webSocketDebuggerUrl'], max_size=None) as ws:
        async def send(method, params=None):
            req_id = int(time.time() * 1000) % 1000000
            await ws.send(json.dumps({'id': req_id, 'method': method, 'params': params or {}}))
            while True:
                msg = json.loads(await ws.recv())
                if msg.get('id') == req_id:
                    return msg.get('result', {})

        await send('Page.enable')
        # Navigate with cache bust
        await send('Page.navigate', {'url': f'https://eatgopty.com/?cb={int(time.time())}'})
        await asyncio.sleep(5)

        # 1. Capture HOME active
        res1 = await send('Page.captureScreenshot', {'format': 'png'})
        with open('live_menu_home_active.png', 'wb') as f:
            f.write(base64.b64decode(res1['data']))
        print("Captured live_menu_home_active.png")

        # 2. Get coordinates of PEDIDOS
        res_rect = await send('Runtime.evaluate', {
            'expression': """
            (function() {
                var el = document.querySelector('li.menu-item-753 a, .eatgo-nav-pills a:last-child');
                if (!el) {
                    var links = Array.from(document.querySelectorAll('.elementor-nav-menu--main a'));
                    el = links[links.length - 1];
                }
                var rect = el.getBoundingClientRect();
                return { x: rect.x + rect.width / 2, y: rect.y + rect.height / 2, text: el.innerText };
            })()
            """,
            'returnByValue': True
        })
        pt = res_rect.get('result', {}).get('value')
        print('Hover target:', pt)

        if pt and 'x' in pt:
            await send('Input.dispatchMouseEvent', {
                'type': 'mouseMoved',
                'x': pt['x'],
                'y': pt['y']
            })
            await asyncio.sleep(1)

        # 3. Capture hover on PEDIDOS
        res2 = await send('Page.captureScreenshot', {'format': 'png'})
        with open('live_menu_hover_pedidos.png', 'wb') as f:
            f.write(base64.b64decode(res2['data']))
        print("Captured live_menu_hover_pedidos.png")

        # 4. Check computed styles
        styles = await send('Runtime.evaluate', {
            'expression': """
            (function() {
                var home = document.querySelector('a.elementor-item-active');
                var cs = window.getComputedStyle(home);
                var csBefore = window.getComputedStyle(home, '::before');
                return {
                    homeText: home ? home.innerText : null,
                    borderRadius: cs.borderRadius,
                    beforeRadius: csBefore.borderRadius,
                    beforeBg: csBefore.backgroundColor
                };
            })()
            """,
            'returnByValue': True
        })
        print('Live computed styles:', json.dumps(styles.get('result', {}).get('value'), indent=2))

asyncio.run(run())
proc.kill()
