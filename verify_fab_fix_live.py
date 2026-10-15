import urllib.request
import json
import asyncio
import websockets
import subprocess
import time
import base64
import os

subprocess.run(['pkill', '-9', '-f', 'chrome_verify_fab'], stderr=subprocess.DEVNULL)
time.sleep(0.5)

proc = subprocess.Popen([
    '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    '--headless=new',
    '--remote-debugging-port=9295',
    '--user-data-dir=/tmp/chrome_verify_fab',
    '--window-size=430,932',  # Modern mobile viewport (iPhone 14/15 Pro)
    '--disable-gpu',
    'https://eatgopty.com/menu-semanal/'
])

async def verify():
    for _ in range(30):
        try:
            data = json.loads(urllib.request.urlopen('http://127.0.0.1:9295/json').read())
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
                    img_data = base64.b64decode(msg.get('result', {}).get('data'))
                    with open(filename, 'wb') as f:
                        f.write(img_data)
                    return filename

        print("Waiting for page load...")
        await asyncio.sleep(6.0)

        # 1. Clear cart first to start clean
        clear_res = await evaluate('''
        new Promise((resolve) => {
            var $ = window.jQuery;
            $.ajax({
                url: '/wp-admin/admin-ajax.php',
                type: 'POST',
                data: { action: 'eatgo_cart_clear' },
                success: function() {
                    $(document.body).trigger('wc_fragment_refresh');
                    setTimeout(() => resolve('CART_CLEARED'), 1000);
                },
                error: function() { resolve('CLEAR_ERROR'); }
            });
        })
        ''')
        print("Clear Cart Result:", clear_res)
        await asyncio.sleep(2.0)

        # 2. Add 1 dish (e.g. Costilla $5.75)
        # Find product card and its add button or trigger add via AJAX
        add_res = await evaluate('''
        new Promise((resolve) => {
            var $ = window.jQuery;
            // Find first available product
            var $firstCard = $('.e-loop-item.product, .e-loop-item[class*="post-"]').first();
            var match = ($firstCard.attr('class') || '').match(/(?:post-|e-loop-item-)(\\d+)/);
            var pid = match ? match[1] : null;

            if (!pid) {
                // Fallback to Costilla pid if known or search
                var $btn = $('a[data-product_id]').first();
                if ($btn.length) pid = $btn.attr('data-product_id');
            }

            if (!pid) {
                resolve({ error: 'No product ID found' });
                return;
            }

            $.ajax({
                url: '/?wc-ajax=add_to_cart',
                type: 'POST',
                data: { product_id: pid, quantity: 1 },
                success: function(resp) {
                    $(document.body).trigger('wc_fragment_refresh');
                    $(document.body).trigger('added_to_cart', [resp.fragments, resp.cart_hash]);
                    setTimeout(() => {
                        resolve({
                            success: true,
                            productId: pid,
                            fabBadge: $('.eatgo-fab-cart .eatgo-fab-badge').text(),
                            fabTotal: $('.eatgo-fab-cart .eatgo-fab-total').text(),
                            fabVisible: $('.eatgo-fab-cart').is(':visible')
                        });
                    }, 1500);
                },
                error: function(err) {
                    resolve({ error: 'Failed to add to cart' });
                }
            });
        })
        ''')
        print("Add To Cart Result:", json.dumps(add_res, indent=2))
        await asyncio.sleep(2.0)

        # 3. Click the FAB button (.eatgo-fab-cart)
        click_res = await evaluate('''
        (function() {
            var $ = window.jQuery;
            var $fab = $('.eatgo-fab-cart');
            $fab.trigger('click');
            return {
                fabExists: $fab.length > 0,
                fabHref: $fab.attr('href'),
                fabClasses: $fab.attr('class'),
                drawerShown: $('.elementor-menu-cart__container').hasClass('elementor-menu-cart--shown')
            };
        })()
        ''')
        print("FAB Click Result:", json.dumps(click_res, indent=2))
        await asyncio.sleep(3.0)

        # 4. Check drawer state & quantities
        drawer_data = await evaluate('''
        (function() {
            var $ = window.jQuery;
            var headerCount = $('.eg-header-count').text().trim();
            var cardQty = $('.eg-qty-selector .eg-qty-val').first().text().trim();
            var cardPrice = $('.eg-card-price').first().text().trim();
            var foodCount = $('.eg-val-alimentos').text().trim();
            var totalPay = $('.eg-resumen-total-val').text().trim();
            var fabBadge = $('.eatgo-fab-badge').text().trim();
            var fabTotal = $('.eatgo-fab-total').text().trim();

            return {
                headerCount: headerCount,
                cardQty: cardQty,
                cardPrice: cardPrice,
                foodCount: foodCount,
                totalPay: totalPay,
                fabBadge: fabBadge,
                fabTotal: fabTotal
            };
        })()
        ''')
        print("DRAWER DATA AFTER FAB CLICK:", json.dumps(drawer_data, indent=2))

        # 5. Capture screenshot
        artifact_dir = '/Users/jaendev/.gemini/antigravity/brain/f578ed85-e95e-4496-9473-5f6b492a38ae'
        os.makedirs(artifact_dir, exist_ok=True)
        screenshot_path = os.path.join(artifact_dir, 'fab_click_drawer_verified.png')
        await capture_screenshot(screenshot_path)
        print("Screenshot saved to:", screenshot_path)

try:
    asyncio.run(verify())
finally:
    proc.terminate()
