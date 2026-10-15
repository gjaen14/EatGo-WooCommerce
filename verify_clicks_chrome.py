import urllib.request
import json
import asyncio
import websockets
import subprocess
import time
import base64

subprocess.run(['pkill', '-9', '-f', 'chrome_verify_clicks'], stderr=subprocess.DEVNULL)
time.sleep(0.5)

proc = subprocess.Popen([
    '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    '--headless=new',
    '--remote-debugging-port=9295',
    '--user-data-dir=/tmp/chrome_verify_clicks',
    '--window-size=1280,900',
    '--disable-gpu',
    'https://eatgopty.com/menu-del-dia/'
])

async def verify():
    await asyncio.sleep(5.0)
    data = json.loads(urllib.request.urlopen('http://127.0.0.1:9295/json').read())
    page = [t for t in data if t.get('type') == 'page'][0]
    
    async with websockets.connect(page['webSocketDebuggerUrl'], max_size=None) as ws:
        async def evaluate(expr):
            req_id = int(time.time() * 1000) % 1000000
            await ws.send(json.dumps({'id': req_id, 'method': 'Runtime.evaluate', 'params': {'expression': expr, 'returnByValue': True}}))
            while True:
                msg = json.loads(await ws.recv())
                if msg.get('id') == req_id:
                    return msg.get('result', {}).get('result', {}).get('value')

        async def capture_screenshot(filename):
            req_id = int(time.time() * 1000) % 1000000
            await ws.send(json.dumps({'id': req_id, 'method': 'Page.captureScreenshot', 'params': {'format': 'png'}}))
            while True:
                msg = json.loads(await ws.recv())
                if msg.get('id') == req_id:
                    img_data = base64.b64decode(msg['result']['data'])
                    with open(filename, 'wb') as f:
                        f.write(img_data)
                    print(f"Screenshot saved to {filename}")
                    break

        # 1. Check Card Buttons Status
        btn_status = await evaluate("""
        (function() {
            var items = [];
            document.querySelectorAll('.e-loop-item').forEach(function(item) {
                var btn = item.querySelector('.elementor-element-w14btna a, a.woosq-btn, a.elementor-button');
                items.push({
                    cardClass: item.className,
                    btnText: btn ? btn.innerText.trim() : null,
                    btnClass: btn ? btn.className : null,
                    btnDataId: btn ? btn.getAttribute('data-id') : null,
                    btnHref: btn ? btn.getAttribute('href') : null
                });
            });
            var fab = document.querySelector('.eatgo-fab-cart');
            return {
                buttons: items.slice(0, 3),
                fabExists: !!fab,
                fabTotal: fab ? fab.innerText.trim() : null,
                fabVisible: fab ? window.getComputedStyle(fab).display !== 'none' : false
            };
        })()
        """)
        print("BUTTON STATUS:", json.dumps(btn_status, indent=2))

        # 2. Click on the first "+ Agregar al Pedido" button
        click_card = await evaluate("""
        (function() {
            var btn = document.querySelector('.elementor-element-w14btna a, a.woosq-btn');
            if (btn) {
                btn.click();
                return { clicked: true, pid: btn.getAttribute('data-id') };
            }
            return { clicked: false };
        })()
        """)
        print("CLICK CARD RESULT:", click_card)

        # Wait for modal to open
        await asyncio.sleep(2.5)

        modal_status = await evaluate("""
        (function() {
            var hasOpenClass = document.body.classList.contains('woosq-open');
            var popup = document.querySelector('.woosq-popup, .woosq-sidebar, #woosq-popup');
            var popupVisible = popup ? window.getComputedStyle(popup).display !== 'none' : false;
            return {
                bodyOpenClass: hasOpenClass,
                popupFound: !!popup,
                popupVisible: popupVisible
            };
        })()
        """)
        print("MODAL STATUS AFTER CLICK:", json.dumps(modal_status, indent=2))
        await capture_screenshot("screenshot_card_modal.png")

        # Close modal if open
        await evaluate("""
        (function() {
            var closeBtn = document.querySelector('.woosq-close, .woosq-overlay');
            if (closeBtn) closeBtn.click();
            document.body.classList.remove('woosq-open');
        })()
        """)
        await asyncio.sleep(1.0)

        # 3. Click on FAB Cart (.eatgo-fab-cart)
        click_fab = await evaluate("""
        (function() {
            var fab = document.querySelector('.eatgo-fab-cart');
            if (fab) {
                fab.click();
                return { clicked: true };
            }
            return { clicked: false };
        })()
        """)
        print("CLICK FAB RESULT:", click_fab)

        await asyncio.sleep(1.5)

        drawer_status = await evaluate("""
        (function() {
            var container = document.querySelector('.elementor-menu-cart__container');
            var isShown = container ? container.classList.contains('elementor-menu-cart--shown') : false;
            var ariaHidden = container ? container.getAttribute('aria-hidden') : null;
            var comandaHeader = document.querySelector('.eg-comanda-header');
            return {
                containerFound: !!container,
                isShown: isShown,
                ariaHidden: ariaHidden,
                comandaHeaderFound: !!comandaHeader
            };
        })()
        """)
        print("SIDE DRAWER STATUS AFTER FAB CLICK:", json.dumps(drawer_status, indent=2))
        await capture_screenshot("screenshot_fab_drawer.png")

try:
    asyncio.run(verify())
finally:
    proc.terminate()
