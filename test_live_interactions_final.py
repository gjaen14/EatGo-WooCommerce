import urllib.request
import json
import asyncio
import websockets
import subprocess
import time
import base64

subprocess.run(['pkill', '-9', '-f', 'chrome_final_verify'], stderr=subprocess.DEVNULL)
time.sleep(0.5)

proc = subprocess.Popen([
    '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    '--headless=new',
    '--remote-debugging-port=9293',
    '--user-data-dir=/tmp/chrome_final_verify',
    '--window-size=1280,900',
    '--disable-gpu',
    'https://eatgopty.com/menu-del-dia/'
])

async def run_test():
    for _ in range(25):
        try:
            data = json.loads(urllib.request.urlopen('http://127.0.0.1:9293/json').read())
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

        await asyncio.sleep(4.5)

        # 1. Inspect first card button
        btn_info = await evaluate("""
        (function() {
            var firstCard = document.querySelector('.e-loop-item.product, .e-loop-item[class*="post-"]');
            var btn = firstCard ? firstCard.querySelector('.elementor-element-w14btna a, a.woosq-btn, a.elementor-button') : null;
            return {
                cardClass: firstCard ? firstCard.className : null,
                btnExists: !!btn,
                btnText: btn ? btn.innerText.trim() : null,
                btnClass: btn ? btn.className : null,
                btnDataId: btn ? btn.getAttribute('data-id') : null,
                btnHref: btn ? btn.getAttribute('href') : null
            };
        })()
        """)
        print("FIRST BUTTON INFO:", json.dumps(btn_info, indent=2))

        # 2. Click the card button
        click_card = await evaluate("""
        (function() {
            var btn = document.querySelector('.e-loop-item.product .elementor-element-w14btna a, .e-loop-item a.woosq-btn, .elementor-element-w14btna a');
            if (btn) {
                btn.click();
                return { clicked: true, dataId: btn.getAttribute('data-id') };
            }
            return { clicked: false };
        })()
        """)
        print("CLICKED CARD:", click_card)

        await asyncio.sleep(3.0)

        modal_info = await evaluate("""
        (function() {
            var popup = document.querySelector('.mfp-content, .woosq-popup, #woosq-popup, .woosq-product');
            return {
                popupFound: !!popup,
                classes: popup ? popup.className : null,
                title: popup ? (popup.querySelector('.product_title, h1, h2') ? popup.querySelector('.product_title, h1, h2').innerText : 'no title') : null
            };
        })()
        """)
        print("MODAL STATUS:", json.dumps(modal_info, indent=2))
        await capture_screenshot("evidencia_modal_plato.png")

        # 3. Close the modal
        await evaluate("""
        (function() {
            var closeBtn = document.querySelector('.mfp-close, .woosq-close, button.mfp-close');
            if (closeBtn) closeBtn.click();
            if (window.jQuery && jQuery.magnificPopup) jQuery.magnificPopup.close();
            document.body.classList.remove('woosq-open');
        })()
        """)
        await asyncio.sleep(1.5)

        # 4. Click the FAB Cart (.eatgo-fab-cart)
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
        print("CLICKED FAB:", click_fab)

        await asyncio.sleep(2.0)

        drawer_info = await evaluate("""
        (function() {
            var widget = document.querySelector('.elementor-widget-woocommerce-menu-cart');
            var container = document.querySelector('.elementor-menu-cart__container');
            var main = document.querySelector('.elementor-menu-cart__main');
            var header = document.querySelector('.eg-comanda-header');
            return {
                widgetShown: widget ? widget.classList.contains('elementor-menu-cart--shown') : false,
                containerShown: container ? container.classList.contains('elementor-menu-cart--shown') : false,
                mainVisible: main ? (window.getComputedStyle(main).opacity !== '0') : false,
                comandaHeaderFound: !!header
            };
        })()
        """)
        print("DRAWER STATUS:", json.dumps(drawer_info, indent=2))
        await capture_screenshot("evidencia_side_drawer.png")

try:
    asyncio.run(run_test())
finally:
    proc.terminate()
