import urllib.request
import json
import asyncio
import websockets
import subprocess
import time
import base64

subprocess.run(['pkill', '-9', '-f', 'chrome_test_modal'], stderr=subprocess.DEVNULL)
time.sleep(0.5)

proc = subprocess.Popen([
    '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    '--headless=new',
    '--remote-debugging-port=9296',
    '--user-data-dir=/tmp/chrome_test_modal',
    '--window-size=1280,900',
    '--disable-gpu',
    'https://eatgopty.com/menu-del-dia/'
])

async def test():
    await asyncio.sleep(4.0)
    data = json.loads(urllib.request.urlopen('http://127.0.0.1:9296/json').read())
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

        # Check woosq_open
        res = await evaluate("""
        (function() {
            if (typeof woosq_open === 'function') {
                woosq_open(446);
                return { opened: true };
            }
            return { opened: false, reason: 'woosq_open not defined' };
        })()
        """)
        print("OPEN RESULT:", res)

        await asyncio.sleep(3.0)

        # Check modal content
        modal_info = await evaluate("""
        (function() {
            var mfp = document.querySelector('.mfp-content, .woosq-popup, #woosq-popup');
            return {
                mfpFound: !!mfp,
                html: mfp ? mfp.innerHTML.substring(0, 300) : null
            };
        })()
        """)
        print("MODAL INFO:", modal_info)
        await capture_screenshot("screenshot_modal_446.png")

        # Now test opening side cart with both classes
        cart_res = await evaluate("""
        (function() {
            $('.elementor-widget-woocommerce-menu-cart').addClass('elementor-menu-cart--shown');
            $('.elementor-menu-cart__container').addClass('elementor-menu-cart--shown').attr('aria-hidden', 'false');
            if (typeof renderComandaDigital === 'function') renderComandaDigital();
            var main = document.querySelector('.elementor-menu-cart__main');
            return {
                mainFound: !!main,
                mainTransform: main ? window.getComputedStyle(main).transform : null,
                mainOpacity: main ? window.getComputedStyle(main).opacity : null
            };
        })()
        """)
        print("CART RES:", cart_res)
        await asyncio.sleep(1.0)
        await capture_screenshot("screenshot_side_cart_open.png")

try:
    asyncio.run(test())
finally:
    proc.terminate()
