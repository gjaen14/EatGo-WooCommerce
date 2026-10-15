import urllib.request
import json
import asyncio
import websockets
import subprocess
import time
import base64

subprocess.run(['pkill', '-9', '-f', 'chrome_test_home'], stderr=subprocess.DEVNULL)
time.sleep(0.5)

proc = subprocess.Popen([
    '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    '--headless=new',
    '--remote-debugging-port=9297',
    '--user-data-dir=/tmp/chrome_test_home',
    '--window-size=1280,1000',
    '--disable-gpu',
    'https://eatgopty.com/'
])

async def test():
    await asyncio.sleep(5.0)
    data = json.loads(urllib.request.urlopen('http://127.0.0.1:9297/json').read())
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

        # 1. Scroll to the Menu del Dia / carousel section
        scroll_info = await evaluate("""
        (function() {
            var section = document.querySelector('.elementor-element-c01comp, .elementor-element-9d0e1f8, [data-elementor-type="loop-item"]');
            if (section) {
                section.scrollIntoView({ behavior: 'instant', block: 'center' });
                return { found: true, top: section.getBoundingClientRect().top };
            }
            return { found: false };
        })()
        """)
        print("SCROLL INFO:", scroll_info)
        await asyncio.sleep(1.5)

        # 2. Inspect buttons in Home
        btn_info = await evaluate("""
        (function() {
            var btns = Array.from(document.querySelectorAll('.elementor-element-9d0e1f8 a, .e-loop-item .woosq-btn, a:has(.elementor-button-text:contains("Agregar al Pedido"))'));
            var addedToCart = Array.from(document.querySelectorAll('.added_to_cart, a.wc-forward'));
            var visibleAddedToCart = addedToCart.filter(function(el) {
                var style = window.getComputedStyle(el);
                return style.display !== 'none' && style.visibility !== 'hidden' && style.opacity !== '0';
            });
            return {
                buttonCount: btns.length,
                firstButtonText: btns[0] ? btns[0].innerText.trim() : null,
                firstButtonClasses: btns[0] ? btns[0].className : null,
                firstButtonDataId: btns[0] ? btns[0].getAttribute('data-id') : null,
                firstButtonHref: btns[0] ? btns[0].getAttribute('href') : null,
                totalAddedToCartInDom: addedToCart.length,
                visibleAddedToCartCount: visibleAddedToCart.length
            };
        })()
        """)
        print("BUTTON INFO:", btn_info)

        # Capture home card state before click
        await capture_screenshot("screenshot_home_cards_clean.png")

        # 3. Simulate click on the first button
        click_res = await evaluate("""
        (function() {
            var btn = document.querySelector('.elementor-element-9d0e1f8 a, .e-loop-item .woosq-btn');
            if (btn) {
                btn.click();
                return { clicked: true, dataId: btn.getAttribute('data-id') };
            }
            return { clicked: false };
        })()
        """)
        print("CLICK RESULT:", click_res)
        await asyncio.sleep(3.0)

        # 4. Check if modal opened and if view cart is visible
        after_click_info = await evaluate("""
        (function() {
            var mfp = document.querySelector('.mfp-content, .woosq-popup, #woosq-popup');
            var addedToCart = Array.from(document.querySelectorAll('.added_to_cart, a.wc-forward'));
            var visibleAddedToCart = addedToCart.filter(function(el) {
                var style = window.getComputedStyle(el);
                return style.display !== 'none' && style.visibility !== 'hidden' && style.opacity !== '0';
            });
            return {
                modalFound: !!mfp,
                modalVisible: mfp ? (window.getComputedStyle(mfp).display !== 'none') : false,
                totalAddedToCartInDom: addedToCart.length,
                visibleAddedToCartCount: visibleAddedToCart.length
            };
        })()
        """)
        print("AFTER CLICK INFO:", after_click_info)

        # Capture screenshot with modal open (proving successful sync and 0 view cart)
        await capture_screenshot("screenshot_home_click_modal.png")

try:
    asyncio.run(test())
finally:
    proc.terminate()
