import urllib.request
import json
import asyncio
import websockets
import subprocess
import time
import base64

subprocess.run(['pkill', '-9', '-f', 'chrome_click_verify'], stderr=subprocess.DEVNULL)
time.sleep(0.5)

proc = subprocess.Popen([
    '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    '--headless=new',
    '--remote-debugging-port=9298',
    '--user-data-dir=/tmp/chrome_click_verify',
    '--disable-gpu',
    '--window-size=1280,900',
    'https://eatgopty.com/menu-del-dia/'
])

async def verify():
    page = None
    for _ in range(30):
        try:
            data = json.loads(urllib.request.urlopen('http://127.0.0.1:9298/json').read())
            pages = [t for t in data if t.get('type') == 'page']
            if pages:
                page = pages[0]
                break
        except Exception:
            await asyncio.sleep(0.3)
            
    if not page:
        print('Page not found!')
        return

    ws_url = page['webSocketDebuggerUrl']
    print('Connected to DevTools:', ws_url)
    async with websockets.connect(ws_url, max_size=None) as ws:
        # Wait for page scripts to settle
        await asyncio.sleep(4.0)

        # 1. Inspect buttons and fab state
        js_inspect = """
        (function() {
            var fab = document.querySelector('.eatgo-fab-cart');
            var cardBtns = Array.from(document.querySelectorAll('a.elementor-button, .woosq-btn')).filter(function(b) {
                return b.innerText.includes('Agregar al Pedido');
            });
            return JSON.stringify({
                fabExists: !!fab,
                fabVisible: fab ? window.getComputedStyle(fab).display : 'none',
                fabText: fab ? fab.innerText.replace(/\\s+/g, ' ').trim() : '',
                totalCardBtns: cardBtns.length,
                firstCardDataId: cardBtns.length ? cardBtns[0].getAttribute('data-id') : null,
                firstCardClasses: cardBtns.length ? cardBtns[0].className : null,
                firstCardHref: cardBtns.length ? cardBtns[0].getAttribute('href') : null
            });
        })()
        """
        await ws.send(json.dumps({'id': 1, 'method': 'Runtime.evaluate', 'params': {'expression': js_inspect, 'returnByValue': True}}))
        while True:
            msg = json.loads(await ws.recv())
            if msg.get('id') == 1:
                res = msg['result']['result']['value']
                print('DOM INSPECTION RESULT:', json.dumps(json.loads(res), indent=2))
                break

        # 2. Test click on Card button ("+ Agregar al Pedido") and see if WPC modal opens
        js_click_card = """
        (function() {
            var btn = document.querySelector('.woosq-btn, a.elementor-button');
            if (btn) {
                btn.click();
                return 'Clicked card button';
            }
            return 'No button found';
        })()
        """
        await ws.send(json.dumps({'id': 2, 'method': 'Runtime.evaluate', 'params': {'expression': js_click_card, 'returnByValue': True}}))
        while True:
            msg = json.loads(await ws.recv())
            if msg.get('id') == 2:
                print('Card Click Result:', msg['result']['result']['value'])
                break

        await asyncio.sleep(2.0)

        # Check if modal opened
        js_check_modal = """
        (function() {
            var popup = document.querySelector('#woosq-popup, .woosq-popup');
            return JSON.stringify({
                popupExists: !!popup,
                popupClasses: popup ? popup.className : null,
                popupVisible: popup ? window.getComputedStyle(popup).display : 'none'
            });
        })()
        """
        await ws.send(json.dumps({'id': 3, 'method': 'Runtime.evaluate', 'params': {'expression': js_check_modal, 'returnByValue': True}}))
        while True:
            msg = json.loads(await ws.recv())
            if msg.get('id') == 3:
                res = msg['result']['result']['value']
                print('MODAL STATUS AFTER CLICK:', json.dumps(json.loads(res), indent=2))
                break

        # 3. Test click on FAB and check side drawer
        js_click_fab = """
        (function() {
            // Close modal if open first
            var closeBtn = document.querySelector('.woosq-close');
            if (closeBtn) closeBtn.click();
            
            var fab = document.querySelector('.eatgo-fab-cart');
            if (fab) {
                fab.click();
                return 'Clicked FAB';
            }
            return 'No FAB found';
        })()
        """
        await ws.send(json.dumps({'id': 4, 'method': 'Runtime.evaluate', 'params': {'expression': js_click_fab, 'returnByValue': True}}))
        while True:
            msg = json.loads(await ws.recv())
            if msg.get('id') == 4:
                print('FAB Click Result:', msg['result']['result']['value'])
                break

        await asyncio.sleep(1.5)

        # Check if Side Drawer is opened
        js_check_drawer = """
        (function() {
            var container = document.querySelector('.elementor-menu-cart__container');
            return JSON.stringify({
                drawerExists: !!container,
                hasShownClass: container ? container.classList.contains('elementor-menu-cart--shown') : false,
                ariaHidden: container ? container.getAttribute('aria-hidden') : null,
                comandaHeaderExists: !!document.querySelector('.eg-comanda-header'),
                comandaTitle: document.querySelector('.eg-header-title') ? document.querySelector('.eg-header-title').innerText : null
            });
        })()
        """
        await ws.send(json.dumps({'id': 5, 'method': 'Runtime.evaluate', 'params': {'expression': js_check_drawer, 'returnByValue': True}}))
        while True:
            msg = json.loads(await ws.recv())
            if msg.get('id') == 5:
                res = msg['result']['result']['value']
                print('SIDE DRAWER STATUS AFTER FAB CLICK:', json.dumps(json.loads(res), indent=2))
                break

        # Capture visual evidence of opened side drawer
        await ws.send(json.dumps({'id': 6, 'method': 'Page.captureScreenshot'}))
        while True:
            msg = json.loads(await ws.recv())
            if msg.get('id') == 6 and 'result' in msg:
                img_bytes = base64.b64decode(msg['result']['data'])
                with open('fab_drawer_live_evidence.png', 'wb') as f:
                    f.write(img_bytes)
                print('SUCCESS! WROTE fab_drawer_live_evidence.png, bytes:', len(img_bytes))
                break

try:
    asyncio.run(verify())
finally:
    proc.terminate()
