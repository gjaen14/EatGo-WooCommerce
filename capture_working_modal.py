import subprocess, time, json, urllib.request, asyncio, websockets, base64

async def test():
    subprocess.run(['pkill', '-f', 'remote-debugging-port=9255'], capture_output=True)
    await asyncio.sleep(1)

    proc = subprocess.Popen([
        '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
        '--headless=new',
        '--remote-debugging-port=9255',
        '--user-data-dir=/tmp/test9255',
        '--disable-gpu',
        '--window-size=1280,1000',
        'about:blank'
    ])
    try:
        data = None
        for _ in range(25):
            try:
                data = json.loads(urllib.request.urlopen('http://localhost:9255/json').read())
                if [t for t in data if t.get('type') == 'page']:
                    break
            except Exception:
                await asyncio.sleep(0.5)
        pages = [t for t in data if t.get('type') == 'page']
        if not pages:
            print('No page target found!')
            return
        ws_url = pages[0]['webSocketDebuggerUrl']
        print('Target page found:', pages[0]['url'], ws_url, flush=True)

        async with websockets.connect(ws_url, max_size=50*1024*1024) as ws:
            await ws.send(json.dumps({'id': 1, 'method': 'Page.enable'}))
            await ws.send(json.dumps({'id': 2, 'method': 'Runtime.enable'}))
            
            # Send navigate
            print('Navigating to https://eatgopty.com/ ...', flush=True)
            await ws.send(json.dumps({'id': 3, 'method': 'Page.navigate', 'params': {'url': 'https://eatgopty.com/'}}))
            
            # Wait 7s for full page load
            await asyncio.sleep(7)

            # Click button
            click_code = '''
            (function() {
                var btn = document.querySelector(".elementor-element-w_btn_314 a") || document.querySelector(".elementor-element-w_btn_314");
                if (btn) {
                    btn.scrollIntoView({ behavior: 'instant', block: 'center' });
                    btn.click();
                    return 'clicked ' + btn.getAttribute('data-id');
                }
                return 'not found';
            })()
            '''
            await ws.send(json.dumps({'id': 4, 'method': 'Runtime.evaluate', 'params': {'expression': click_code, 'returnByValue': True}}))
            while True:
                msg = json.loads(await ws.recv())
                if msg.get('id') == 4:
                    print('Click evaluate:', msg.get('result', {}).get('result', {}).get('value'), flush=True)
                    break
            
            # Wait 3.5s for modal to render
            await asyncio.sleep(3.5)

            # Check modal
            check_modal = '''
            (function() {
                var popup = document.querySelector(".woosq-popup");
                var title = document.querySelector(".woosq-product .product_title, .woosq-popup .product_title");
                var price = document.querySelector(".woosq-product .price");
                return {
                    isOpen: !!popup,
                    title: title ? title.innerText.trim() : null,
                    price: price ? price.innerText.trim() : null
                };
            })()
            '''
            await ws.send(json.dumps({'id': 5, 'method': 'Runtime.evaluate', 'params': {'expression': check_modal, 'returnByValue': True}}))
            while True:
                msg = json.loads(await ws.recv())
                if msg.get('id') == 5:
                    print('Modal check:', msg.get('result', {}).get('result', {}).get('value'), flush=True)
                    break

            # Capture screenshot
            print('Requesting screenshot...', flush=True)
            await ws.send(json.dumps({'id': 6, 'method': 'Page.captureScreenshot'}))
            while True:
                msg = json.loads(await ws.recv())
                if msg.get('id') == 6:
                    img_data = base64.b64decode(msg['result']['data'])
                    out_path = 'modal_desayuno_live.png'
                    with open(out_path, 'wb') as f:
                        f.write(img_data)
                    print(f'WROTE {out_path}, size: {len(img_data)}', flush=True)
                    break
    finally:
        proc.terminate()

asyncio.run(test())
