import urllib.request
import json
import asyncio
import websockets
import subprocess
import time
import base64
import os

subprocess.run(['pkill', '-9', '-f', 'chrome_menu_verify'], stderr=subprocess.DEVNULL)
time.sleep(0.5)

chrome_port = 9310
proc = subprocess.Popen([
    '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    '--headless=new',
    f'--remote-debugging-port={chrome_port}',
    '--user-data-dir=/tmp/chrome_menu_verify',
    '--window-size=1280,900',
    '--disable-gpu',
    'about:blank'
])

async def run():
    try:
        data = None
        for _ in range(30):
            try:
                data = json.loads(urllib.request.urlopen(f'http://127.0.0.1:{chrome_port}/json').read())
                if data:
                    break
            except Exception:
                await asyncio.sleep(0.3)

        if not data:
            print("Failed to connect to Chrome remote debugging port.")
            return

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
            cb = int(time.time())
            url = f'https://eatgopty.com/menu-semanal/?cb={cb}'
            print(f"Navigating to {url}...")
            await send('Page.navigate', {'url': url})
            await asyncio.sleep(5)

            # Check DOM state and inline styles
            eval_res = await send('Runtime.evaluate', {
                'expression': """
                (function() {
                    var pills = Array.from(document.querySelectorAll('[data-interaction-id="675a0b2b"], [data-interaction-id="407669ce"], [data-interaction-id="2c494cb1"], [data-interaction-id="60e274d"], [data-interaction-id="4fdd1a46"], [data-interaction-id="da15a65"], .btn-dia-tab, [class*="dia-tab"]'));
                    
                    var results = pills.map(function(p) {
                        var cs = window.getComputedStyle(p);
                        return {
                            text: p.innerText.trim(),
                            className: p.className,
                            hasInlineStyle: p.hasAttribute('style'),
                            inlineStyle: p.getAttribute('style') || '',
                            bgColor: cs.backgroundColor,
                            color: cs.color,
                            border: cs.border
                        };
                    });

                    // Check title
                    var titleEl = document.querySelector('[data-interaction-id="346b2401"], .banner-dia-title, [data-interaction-id="7a072b70"] h3');
                    var titleText = titleEl ? titleEl.innerText.trim() : 'N/A';
                    
                    // Check grids visible
                    var grids = Array.from(document.querySelectorAll('[data-interaction-id="12dc898b"], [data-interaction-id="4bf72f7d"], [data-interaction-id="5bfd1736"], [data-interaction-id="2fd6c6a9"], [data-interaction-id="62f9bc94"], [data-interaction-id="74741324"]'));
                    var visibleGrids = grids.map(function(g) {
                        return {
                            id: g.getAttribute('data-interaction-id'),
                            display: window.getComputedStyle(g).display
                        };
                    });

                    // Check cart and whatsapp
                    var cartBtn = document.querySelector('.elementor-menu-cart__toggle, .woosq-btn, a[href*="cart"], .eatgo-fab');
                    var waBtn = document.querySelector('a[href*="wa.me"], a[href*="whatsapp"]');

                    return {
                        pills: results,
                        title: titleText,
                        visibleGrids: visibleGrids,
                        hasCart: !!cartBtn,
                        hasWA: !!waBtn
                    };
                })()
                """,
                'returnByValue': True
            })

            data_eval = eval_res.get('result', {}).get('value', {})
            print("Evaluation Result:", json.dumps(data_eval, indent=2, ensure_ascii=False))

            # Take screenshot before click
            ss1 = await send('Page.captureScreenshot', {'format': 'png'})
            with open('verification_menu_semanal_initial.png', 'wb') as f:
                f.write(base64.b64decode(ss1['data']))
            print("Captured verification_menu_semanal_initial.png")

            # Click on MARTES to verify interactive day change
            click_res = await send('Runtime.evaluate', {
                'expression': """
                (function() {
                    var martesBtn = document.querySelector('[data-interaction-id="407669ce"], [data-dia="martes"]') || 
                                    Array.from(document.querySelectorAll('.btn-dia-tab, [class*="dia-tab"]')).find(el => el.innerText.toUpperCase().includes('MARTES'));
                    if (martesBtn) {
                        martesBtn.click();
                        return "Clicked Martes successfully";
                    }
                    return "Martes button not found";
                })()
                """,
                'returnByValue': True
            })
            print("Martes Click:", click_res.get('result', {}).get('value'))
            await asyncio.sleep(2)

            # Check state after clicking Martes
            eval_after = await send('Runtime.evaluate', {
                'expression': """
                (function() {
                    var titleEl = document.querySelector('[data-interaction-id="346b2401"], .banner-dia-title, [data-interaction-id="7a072b70"] h3');
                    return {
                        title: titleEl ? titleEl.innerText.trim() : 'N/A',
                        martesActive: document.querySelector('[data-interaction-id="407669ce"]') ? document.querySelector('[data-interaction-id="407669ce"]').classList.contains('is-active') : false
                    };
                })()
                """,
                'returnByValue': True
            })
            print("After Martes Click:", json.dumps(eval_after.get('result', {}).get('value', {}), indent=2))

            # Screenshot after click
            ss2 = await send('Page.captureScreenshot', {'format': 'png'})
            with open('verification_menu_semanal_martes.png', 'wb') as f:
                f.write(base64.b64decode(ss2['data']))
            print("Captured verification_menu_semanal_martes.png")

    finally:
        proc.terminate()
        subprocess.run(['pkill', '-9', '-f', 'chrome_menu_verify'], stderr=subprocess.DEVNULL)

asyncio.run(run())
