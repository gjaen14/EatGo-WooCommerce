import subprocess
import time
import json
import urllib.request
import asyncio
import base64
import websockets

async def capture():
    proc = subprocess.Popen([
        '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
        '--headless=new',
        '--remote-debugging-port=9227',
        '--user-data-dir=/tmp/chrome_p9227',
        '--disable-gpu',
        '--window-size=1280,1100',
        'about:blank'
    ])
    try:
        targets = None
        for i in range(25):
            await asyncio.sleep(0.4)
            try:
                targets = json.loads(urllib.request.urlopen('http://localhost:9227/json').read())
                pages = [t for t in targets if t.get('type') == 'page']
                if pages:
                    targets = pages
                    break
            except Exception:
                pass
        
        if not targets:
            raise Exception("No page targets found")

        ws_url = targets[0]['webSocketDebuggerUrl']
        print('Connecting to page ws:', ws_url)
        
        async with websockets.connect(ws_url) as ws:
            print('Navigating to https://eatgopty.com/donde-comer-y-retirar/ ...')
            await ws.send(json.dumps({'id': 1, 'method': 'Page.navigate', 'params': {'url': 'https://eatgopty.com/donde-comer-y-retirar/'}}))
            await asyncio.sleep(5.0)

            # 1. Capture Top (Corporativo + Tarjetas)
            print('1. Capturing Top screenshot...')
            await ws.send(json.dumps({'id': 2, 'method': 'Runtime.evaluate', 'params': {'expression': 'window.scrollTo(0, 0)'}}))
            await asyncio.sleep(0.5)
            await ws.send(json.dumps({'id': 3, 'method': 'Page.captureScreenshot'}))
            while True:
                msg = json.loads(await ws.recv())
                if msg.get('id') == 3 and 'result' in msg and 'data' in msg['result']:
                    img_data = base64.b64decode(msg['result']['data'])
                    with open('evidence_donde_comer_top.png', 'wb') as f:
                        f.write(img_data)
                    print('Saved evidence_donde_comer_top.png')
                    break

            # 2. Scroll to and capture Tarjetas
            print('2. Capturing Cards screenshot...')
            scroll_cards = '''
            (function() {
                var el = document.querySelector('[data-id="maincon"]') || document.querySelector('.elementor-element-maincon');
                if (el) el.scrollIntoView({ behavior: 'instant', block: 'center' });
            })()
            '''
            await ws.send(json.dumps({'id': 4, 'method': 'Runtime.evaluate', 'params': {'expression': scroll_cards}}))
            await asyncio.sleep(0.8)
            await ws.send(json.dumps({'id': 5, 'method': 'Page.captureScreenshot'}))
            while True:
                msg = json.loads(await ws.recv())
                if msg.get('id') == 5 and 'result' in msg and 'data' in msg['result']:
                    img_data = base64.b64decode(msg['result']['data'])
                    with open('evidence_donde_comer_cards.png', 'wb') as f:
                        f.write(img_data)
                    print('Saved evidence_donde_comer_cards.png')
                    break

            # 3. Scroll to and capture Turnos y Pagos
            print('3. Capturing Turnos y Pagos screenshot...')
            scroll_turnos = '''
            (function() {
                var el = document.querySelector('[data-id="turnosp"]') || document.querySelector('.elementor-element-turnosp');
                if (el) el.scrollIntoView({ behavior: 'instant', block: 'center' });
            })()
            '''
            await ws.send(json.dumps({'id': 6, 'method': 'Runtime.evaluate', 'params': {'expression': scroll_turnos}}))
            await asyncio.sleep(0.8)
            await ws.send(json.dumps({'id': 7, 'method': 'Page.captureScreenshot'}))
            while True:
                msg = json.loads(await ws.recv())
                if msg.get('id') == 7 and 'result' in msg and 'data' in msg['result']:
                    img_data = base64.b64decode(msg['result']['data'])
                    with open('evidence_donde_comer_turnos.png', 'wb') as f:
                        f.write(img_data)
                    print('Saved evidence_donde_comer_turnos.png')
                    break

            # 4. Scroll to and capture Footer
            print('4. Capturing Footer screenshot...')
            scroll_footer = '''
            (function() {
                var el = document.querySelector('footer');
                if (el) el.scrollIntoView({ behavior: 'instant', block: 'end' });
            })()
            '''
            await ws.send(json.dumps({'id': 8, 'method': 'Runtime.evaluate', 'params': {'expression': scroll_footer}}))
            await asyncio.sleep(0.8)
            await ws.send(json.dumps({'id': 9, 'method': 'Page.captureScreenshot'}))
            while True:
                msg = json.loads(await ws.recv())
                if msg.get('id') == 9 and 'result' in msg and 'data' in msg['result']:
                    img_data = base64.b64decode(msg['result']['data'])
                    with open('evidence_footer_corporate.png', 'wb') as f:
                        f.write(img_data)
                    print('Saved evidence_footer_corporate.png')
                    break

    finally:
        proc.terminate()

asyncio.run(capture())
