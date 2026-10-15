import subprocess, time, json, urllib.request, asyncio, websockets, base64, os

async def main():
    chrome_port = 9277
    profile_dir = f'/tmp/chrome_p{chrome_port}'
    subprocess.run(['rm', '-rf', profile_dir], capture_output=True)
    subprocess.run(['pkill', '-f', f'remote-debugging-port={chrome_port}'], capture_output=True)
    time.sleep(0.5)

    proc = subprocess.Popen([
        '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
        '--headless=new',
        f'--remote-debugging-port={chrome_port}',
        f'--user-data-dir={profile_dir}',
        '--disable-gpu',
        '--window-size=1280,1100',
        'https://eatgopty.com/'
    ])
    try:
        ws_url = None
        for _ in range(30):
            time.sleep(0.5)
            try:
                tabs = json.loads(urllib.request.urlopen(f'http://localhost:{chrome_port}/json').read())
                pages = [t for t in tabs if t.get('type') == 'page' and 'eatgo' in t.get('url', '')]
                if pages:
                    ws_url = pages[0]['webSocketDebuggerUrl']
                    break
            except Exception:
                pass
        
        if not ws_url:
            print('Could not find page WS URL!')
            return

        print('Connected to page WS:', ws_url, flush=True)
        async with websockets.connect(ws_url, max_size=50*1024*1024) as ws:
            # Wait for DOM and Elementor scripts to finish initializing
            print('Waiting 6s for page initialization...', flush=True)
            await asyncio.sleep(6)

            # Trigger click on first desayuno button
            trigger_js = '''
            (function() {
                var btn = document.querySelector(".elementor-element-w_btn_314 a");
                if (btn) {
                    btn.scrollIntoView({ behavior: 'instant', block: 'center' });
                    btn.click();
                    return "clicked";
                }
                return "not found";
            })()
            '''
            cmd_id = 101
            await ws.send(json.dumps({'id': cmd_id, 'method': 'Runtime.evaluate', 'params': {'expression': trigger_js, 'returnByValue': True}}))
            while True:
                msg = json.loads(await ws.recv())
                if msg.get('id') == cmd_id:
                    print('Click result:', msg.get('result', {}).get('result', {}).get('value'), flush=True)
                    break

            # Wait 4s for modal animation and content loading
            print('Waiting 4s for modal...', flush=True)
            await asyncio.sleep(4)

            # Check modal content
            check_js = '''
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
            cmd_id = 102
            await ws.send(json.dumps({'id': cmd_id, 'method': 'Runtime.evaluate', 'params': {'expression': check_js, 'returnByValue': True}}))
            while True:
                msg = json.loads(await ws.recv())
                if msg.get('id') == cmd_id:
                    print('Modal status:', msg.get('result', {}).get('result', {}).get('value'), flush=True)
                    break

            # Capture screenshot
            print('Capturing screenshot...', flush=True)
            cmd_id = 103
            await ws.send(json.dumps({'id': cmd_id, 'method': 'Page.captureScreenshot', 'params': {'format': 'png'}}))
            while True:
                msg = json.loads(await ws.recv())
                if msg.get('id') == cmd_id:
                    img_data = base64.b64decode(msg['result']['data'])
                    out_path = '/Applications/XAMPP/xamppfiles/htdocs/Eat&Go_Woocomerce/desayuno_modal_verified.png'
                    with open(out_path, 'wb') as f:
                        f.write(img_data)
                    artifact_path = '/Users/jaendev/.gemini/antigravity/brain/535e662b-3f91-4b37-9e72-7036af9c6a38/desayuno_modal_verified.png'
                    with open(artifact_path, 'wb') as f:
                        f.write(img_data)
                    print(f'Successfully wrote {out_path} and {artifact_path} ({len(img_data)} bytes)', flush=True)
                    break
    finally:
        proc.terminate()

asyncio.run(main())
