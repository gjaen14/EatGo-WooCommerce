const { spawn } = require('child_process');
const http = require('http');
const fs = require('fs');
const path = require('path');
const WebSocket = require('ws');

async function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

function getJson(url) {
    return new Promise((resolve, reject) => {
        http.get(url, (res) => {
            let data = '';
            res.on('data', chunk => data += chunk);
            res.on('end', () => {
                try {
                    resolve(JSON.parse(data));
                } catch (e) {
                    reject(e);
                }
            });
        }).on('error', reject);
    });
}

async function main() {
    const port = 9240;
    console.log('Spawning Chrome on port', port);
    const chrome = spawn('/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', [
        '--headless=new',
        `--remote-debugging-port=${port}`,
        '--user-data-dir=/tmp/chrome_node_9240',
        '--disable-gpu',
        '--window-size=1280,1050',
        'https://eatgopty.com/'
    ]);

    try {
        let wsUrl = null;
        for (let i = 0; i < 30; i++) {
            await sleep(500);
            try {
                const targets = await getJson(`http://127.0.0.1:${port}/json`);
                const page = targets.find(t => t.type === 'page' && (t.url.includes('eatgo') || t.url.includes('http')));
                if (page && page.webSocketDebuggerUrl) {
                    wsUrl = page.webSocketDebuggerUrl;
                    break;
                }
            } catch (err) {}
        }

        if (!wsUrl) {
            throw new Error('Could not find Chrome page target');
        }

        console.log('Connected to target:', wsUrl);
        const ws = new WebSocket(wsUrl, { maxPayload: 100 * 1024 * 1024 });

        await new Promise((resolve, reject) => {
            ws.on('open', resolve);
            ws.on('error', reject);
        });

        let nextId = 1;
        function send(method, params = {}) {
            return new Promise((resolve, reject) => {
                const id = nextId++;
                const timer = setTimeout(() => {
                    reject(new Error(`Timeout waiting for response to ${method}`));
                }, 30000);

                function onMsg(data) {
                    try {
                        const parsed = JSON.parse(data.toString());
                        if (parsed.id === id) {
                            clearTimeout(timer);
                            ws.off('message', onMsg);
                            if (parsed.error) reject(parsed.error);
                            else resolve(parsed.result);
                        }
                    } catch (e) {}
                }

                ws.on('message', onMsg);
                ws.send(JSON.stringify({ id, method, params }));
            });
        }

        console.log('Waiting 7s for full page load...');
        await sleep(7000);

        console.log('Triggering click / woosq on breakfast button...');
        const clickResult = await send('Runtime.evaluate', {
            expression: `
            new Promise((resolve) => {
                var btn = document.querySelector(".elementor-element-w_btn_314 a") || document.querySelector(".elementor-element-w_btn_314");
                if (btn) {
                    btn.scrollIntoView({ behavior: "instant", block: "center" });
                    var pid = btn.getAttribute("data-id") || 578;
                    // Trigger click asynchronously
                    setTimeout(() => {
                        if (typeof woosq_open === "function") {
                            woosq_open(pid);
                        } else {
                            btn.click();
                        }
                    }, 50);
                    resolve({ status: "invoked", pid: pid, text: btn.innerText.trim() });
                } else {
                    resolve({ status: "not_found" });
                }
            })
            `,
            awaitPromise: true,
            returnByValue: true
        });
        console.log('Trigger result:', clickResult.result ? clickResult.result.value : clickResult);

        console.log('Waiting for modal to appear and open...');
        const modalRes = await send('Runtime.evaluate', {
            expression: `
            new Promise((resolve) => {
                var start = Date.now();
                var timer = setInterval(function() {
                    var popup = document.querySelector(".woosq-popup");
                    var title = document.querySelector(".woosq-product .product_title, .woosq-popup h1, .woosq-popup .product_title");
                    var price = document.querySelector(".woosq-product .price");
                    if (popup && title) {
                        clearInterval(timer);
                        resolve({
                            isOpen: true,
                            title: title.innerText.trim(),
                            price: price ? price.innerText.trim() : ""
                        });
                    } else if (Date.now() - start > 10000) {
                        clearInterval(timer);
                        resolve({ isOpen: false });
                    }
                }, 300);
            })
            `,
            awaitPromise: true,
            returnByValue: true
        });
        console.log('Modal status:', modalRes.result ? modalRes.result.value : modalRes);

        // Allow images & styles in modal to stabilize
        await sleep(2000);

        console.log('Capturing screenshot...');
        const screenshotRes = await send('Page.captureScreenshot', { format: 'png' });
        const buf = Buffer.from(screenshotRes.data, 'base64');

        const outPath = path.resolve(__dirname, 'desayuno_modal_verified.png');
        fs.writeFileSync(outPath, buf);
        console.log('Saved to:', outPath, 'Bytes:', buf.length);

        const artifactPath = '/Users/jaendev/.gemini/antigravity/brain/535e662b-3f91-4b37-9e72-7036af9c6a38/desayuno_modal_verified.png';
        fs.writeFileSync(artifactPath, buf);
        console.log('Saved to artifact:', artifactPath);

        ws.close();
    } finally {
        chrome.kill();
    }
}

main().catch(err => {
    console.error('Fatal error:', err);
    process.exit(1);
});
