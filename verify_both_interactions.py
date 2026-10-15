import urllib.request
import json
import asyncio
import websockets
import subprocess
import time
import base64

subprocess.run(['pkill', '-9', '-f', 'chrome_verify_both'], stderr=subprocess.DEVNULL)
time.sleep(0.5)

proc = subprocess.Popen([
    '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    '--headless=new',
    '--remote-debugging-port=9292',
    '--user-data-dir=/tmp/chrome_verify_both_' + str(int(time.time())),
    '--incognito',
    '--disable-cache',
    '--disable-gpu',
    '--window-size=1280,900',
    'https://eatgopty.com/menu-del-dia/'
])

async def verify():
    page = None
    for _ in range(30):
        try:
            data = json.loads(urllib.request.urlopen('http://127.0.0.1:9292/json').read())
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
        # Wait for page scripts and loop items to render
        await asyncio.sleep(4.5)

        # 1. Verify Card Buttons state in DOM
        js_inspect = """
        (function() {
            var btns = Array.from(document.querySelectorAll('.woosq-btn, a.elementor-button')).filter(function(b) {
                return b.innerText && b.innerText.includes('Agregar al Pedido');
            });
            var fab = document.querySelector('.eatgo-fab-cart');
            return JSON.stringify({
                foundButtons: btns.length,
                firstButtonDataId: btns.length ? btns[0].getAttribute('data-id') : null,
                firstButtonClasses: btns.length ? btns[0].className : null,
                firstButtonHref: btns.length ? btns[0].getAttribute('href') : null,
                fabExists: !!fab,
                fabDisplay: fab ? window.getComputedStyle(fab).display : 'none'
            });
        })()
        """
        await ws.send(json.dumps({'id': 1, 'method': 'Runtime.evaluate', 'params': {'expression': js_inspect, 'returnByValue': True}}))
        while True:
            msg = json.loads(await ws.recv())
            if msg.get('id') == 1:
                res = msg['result']['result']['value']
                print('DOM STATE:', json.dumps(json.loads(res), indent=2))
                break

        # 2. Click the first Card Button ("+ Agregar al Pedido")
        js_click_card = """
        (function() {
            var btn = Array.from(document.querySelectorAll('.woosq-btn, a.elementor-button')).find(function(b) {
                return b.innerText && b.innerText.includes('Agregar al Pedido');
            });
            if (btn) {
                btn.click();
                return 'Clicked button for product ' + btn.getAttribute('data-id');
            }
            return 'No button found';
        })()
        """
        await ws.send(json.dumps({'id': 2, 'method': 'Runtime.evaluate', 'params': {'expression': js_click_card, 'returnByValue': True}}))
        while True:
            msg = json.loads(await ws.recv())
            if msg.get('id') == 2:
                print('CLICK CARD RESULT:', msg['result']['result']['value'])
                break

        # Wait for WPC Quick View modal to open and load product details
        await asyncio.sleep(2.5)

        # Check if modal opened
        js_check_modal = """
        (function() {
            var popup = document.querySelector('#woosq-popup');
            var title = popup ? popup.querySelector('.product_title, h1, h2') : null;
            return JSON.stringify({
                popupExists: !!popup,
                popupClass: popup ? popup.className : null,
                popupDisplay: popup ? window.getComputedStyle(popup).display : 'none',
                productTitleInModal: title ? title.innerText.trim() : null
            });
        })()
        """
        await ws.send(json.dumps({'id': 3, 'method': 'Runtime.evaluate', 'params': {'expression': js_check_modal, 'returnByValue': True}}))
        while True:
            msg = json.loads(await ws.recv())
            if msg.get('id') == 3:
                res = msg['result']['result']['value']
                print('MODAL VERIFICATION:', json.dumps(json.loads(res), indent=2))
                break

        # Take screenshot of open modal
        await ws.send(json.dumps({'id': 4, 'method': 'Page.captureScreenshot'}))
        while True:
            msg = json.loads(await ws.recv())
            if msg.get('id') == 4 and 'result' in msg:
                img_data = base64.b64decode(msg['result']['data'])
                with open('evidence_modal_product_opened.png', 'wb') as f:
                    f.write(img_data)
                print('SAVED: evidence_modal_product_opened.png (bytes:', len(img_data), ')')
                break

        # 3. Close modal and click FAB button to test Side-Drawer
        js_click_fab = """
        (function() {
            var closeBtn = document.querySelector('.woosq-close');
            if (closeBtn) closeBtn.click();
            
            var fab = document.querySelector('.eatgo-fab-cart');
            if (fab) {
                fab.click();
                return 'Clicked FAB';
            }
            return 'FAB not found';
        })()
        """
        await ws.send(json.dumps({'id': 5, 'method': 'Runtime.evaluate', 'params': {'expression': js_click_fab, 'returnByValue': True}}))
        while True:
            msg = json.loads(await ws.recv())
            if msg.get('id') == 5:
                print('CLICK FAB RESULT:', msg['result']['result']['value'])
                break

        await asyncio.sleep(2.0)

        # Check Side Drawer
        js_check_drawer = """
        (function() {
            var drawer = document.querySelector('.elementor-menu-cart__container');
            var header = document.querySelector('.eg-comanda-header');
            return JSON.stringify({
                drawerOpen: drawer ? drawer.classList.contains('elementor-menu-cart--shown') : false,
                headerExists: !!header,
                headerTitle: header ? header.querySelector('.eg-header-title').innerText : null
            });
        })()
        """
        await ws.send(json.dumps({'id': 6, 'method': 'Runtime.evaluate', 'params': {'expression': js_check_drawer, 'returnByValue': True}}))
        while True:
            msg = json.loads(await ws.recv())
            if msg.get('id') == 6:
                res = msg['result']['result']['value']
                print('SIDE DRAWER VERIFICATION:', json.dumps(json.loads(res), indent=2))
                break

        # Take screenshot of open drawer with FAB
        await ws.send(json.dumps({'id': 7, 'method': 'Page.captureScreenshot'}))
        while True:
            msg = json.loads(await ws.recv())
            if msg.get('id') == 7 and 'result' in msg:
                img_data = base64.b64decode(msg['result']['data'])
                with open('evidence_side_drawer_opened.png', 'wb') as f:
                    f.write(img_data)
                print('SAVED: evidence_side_drawer_opened.png (bytes:', len(img_data), ')')
                break

try:
    asyncio.run(verify())
finally:
    proc.terminate()
