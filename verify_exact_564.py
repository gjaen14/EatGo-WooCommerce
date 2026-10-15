import urllib.request
import json
import asyncio
import websockets
import subprocess
import time
import base64

subprocess.run(["pkill", "-9", "-f", "chrome_test_exact_564"], stderr=subprocess.DEVNULL)
time.sleep(0.5)

proc = subprocess.Popen([
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless=new",
    "--remote-debugging-port=9281",
    "--user-data-dir=/tmp/chrome_test_exact_564",
    "--window-size=1280,1000",
    "--disable-gpu",
    "https://eatgopty.com/"
])

async def test():
    await asyncio.sleep(4.0)
    data = json.loads(urllib.request.urlopen("http://127.0.0.1:9281/json").read())
    page = [t for t in data if t.get("type") == "page"][0]
    
    async with websockets.connect(page["webSocketDebuggerUrl"], max_size=None) as ws:
        async def evaluate(expr):
            req_id = int(time.time() * 1000) % 1000000
            await ws.send(json.dumps({"id": req_id, "method": "Runtime.evaluate", "params": {"expression": expr, "returnByValue": True}}))
            while True:
                msg = json.loads(await ws.recv())
                if msg.get("id") == req_id:
                    return msg.get("result", {}).get("result", {}).get("value")

        async def capture(filename):
            req_id = int(time.time() * 1000) % 1000000
            await ws.send(json.dumps({"id": req_id, "method": "Page.captureScreenshot", "params": {"format": "png"}}))
            while True:
                msg = json.loads(await ws.recv())
                if msg.get("id") == req_id:
                    img_data = base64.b64decode(msg["result"]["data"])
                    with open(filename, "wb") as f:
                        f.write(img_data)
                    print("Screenshot saved to", filename)
                    break

        await asyncio.sleep(2.0)

        # 1. Inspect button status before click
        before = await evaluate("""
        (function() {
            var btn = document.querySelector(".elementor-element-9d0e1f8 a");
            var wrap = document.querySelector(".elementor-element-9d0e1f8");
            return {
                btnText: btn ? btn.innerText.trim() : null,
                btnClass: btn ? btn.className : null,
                wrapClass: wrap ? wrap.className : null,
                btnHref: btn ? btn.getAttribute("href") : null,
                btnDataId: btn ? btn.getAttribute("data-id") : null,
                hasWoosqBtn: btn ? btn.classList.contains("woosq-btn") : false,
                hasAjaxAdd: btn ? btn.classList.contains("ajax_add_to_cart") : false
            };
        })()
        """)
        print("BEFORE CLICK:", json.dumps(before, indent=2))

        # 2. Click the button "+ Agregar al Pedido" on Home
        click_res = await evaluate("""
        (function() {
            var btn = document.querySelector(".elementor-element-9d0e1f8 a");
            if (btn) {
                btn.click();
                return { clicked: true, dataId: btn.getAttribute("data-id") };
            }
            return { clicked: false };
        })()
        """)
        print("CLICK RESULT:", json.dumps(click_res, indent=2))

        await asyncio.sleep(2.5)

        # 3. Check for WPC Quick View modal and View cart suppression
        after = await evaluate("""
        (function() {
            var popup = document.querySelector("#woosq-popup, .woosq-popup, .mfp-wrap");
            var hasBodyOpen = document.body.classList.contains("woosq-open");
            var addedToCart = document.querySelectorAll(".added_to_cart, a.wc-forward");
            var visibleCount = 0;
            addedToCart.forEach(function(el) {
                var s = window.getComputedStyle(el);
                if (s.display !== "none" && s.visibility !== "hidden") visibleCount++;
            });
            return {
                popupFound: !!popup,
                popupVisible: popup ? (window.getComputedStyle(popup).display !== "none") : false,
                popupClasses: popup ? popup.className : null,
                bodyHasWoosqOpen: hasBodyOpen,
                addedToCartTotal: addedToCart.length,
                addedToCartVisible: visibleCount
            };
        })()
        """)
        print("AFTER CLICK:", json.dumps(after, indent=2))

        # 4. Capture screenshot showing modal open (exact same modal as Post 564)
        await capture("screenshot_home_exact_564_modal.png")

try:
    asyncio.run(test())
finally:
    proc.terminate()
