import urllib.request
import json
import asyncio
import websockets
import subprocess
import time
import base64

subprocess.run(['pkill', '-9', '-f', 'chrome_menu_verify'], stderr=subprocess.DEVNULL)
time.sleep(0.5)

chrome_port = 9340
proc = subprocess.Popen([
    '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    '--headless=new',
    f'--remote-debugging-port={chrome_port}',
    '--user-data-dir=/tmp/chrome_menu_verify_proof',
    '--window-size=1280,1024',
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

            # Extract card info for Lunes
            res = await send('Runtime.evaluate', {
                'expression': '''
                (function() {
                    var cards = Array.from(document.querySelectorAll('.elementor-element-lg_lun .e-loop-item, [data-id="lg_lun"] .e-loop-item, [data-interaction-id="12dc898b"] .e-loop-item'));
                    return cards.map(c => {
                        var title = c.querySelector('h3, h4')?.innerText || '';
                        var price = c.querySelector('[data-interaction-id*="bpr-"]')?.innerText || '';
                        var covr = c.querySelector('.elementor-element-c02covr, [data-id="c02covr"]');
                        var bg = covr ? window.getComputedStyle(covr).backgroundImage : '';
                        var cls = Array.from(c.classList).filter(x => x.startsWith('post-'))[0] || '';
                        return { title, price, bg, cls };
                    });
                })()
                ''',
                'returnByValue': True
            })
            
            cards = res.get('result', {}).get('value', [])
            print("\n=== VERIFICACIÓN DOM LUNES ===")
            for c in cards:
                print(f"[{c['cls']}] {c['title']} | {c['price']} | {c['bg']}")

            # Scroll into menu section
            await send('Runtime.evaluate', {
                'expression': '''
                var el = document.querySelector('[data-interaction-id="60277592"], [data-interaction-id="12dc898b"], .elementor-element-lg_lun');
                if (el) el.scrollIntoView({ behavior: 'instant', block: 'start' });
                '''
            })
            await asyncio.sleep(1)

            # Capture screenshot
            ss = await send('Page.captureScreenshot', {'format': 'png'})
            img_data = base64.b64decode(ss['data'])
            with open('verification_menu_semanal_clean.png', 'wb') as f:
                f.write(img_data)
            print("\nScreenshot saved to verification_menu_semanal_clean.png")

            # Check Menu del Dia
            print("\nChecking Menu del Dia (Post 724)...")
            await send('Page.navigate', {'url': f'https://eatgopty.com/menu-del-dia/?cb={cb}'})
            await asyncio.sleep(4)

            res_dia = await send('Runtime.evaluate', {
                'expression': '''
                (function() {
                    var cards = Array.from(document.querySelectorAll('.e-loop-item'));
                    return cards.slice(0, 3).map(c => {
                        var title = c.querySelector('h3, h4')?.innerText || '';
                        var covr = c.querySelector('.elementor-element-c02covr, [data-id="c02covr"]');
                        var bg = covr ? window.getComputedStyle(covr).backgroundImage : '';
                        var cls = Array.from(c.classList).filter(x => x.startsWith('post-'))[0] || '';
                        return { title, bg, cls };
                    });
                })()
                ''',
                'returnByValue': True
            })
            cards_dia = res_dia.get('result', {}).get('value', [])
            print("=== VERIFICACIÓN POST 724 (MENÚ DEL DÍA) ===")
            for c in cards_dia:
                print(f"[{c['cls']}] {c['title']} | {c['bg']}")

    finally:
        proc.kill()

asyncio.run(run())
