
const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({ headless: 'new', args: ['--no-sandbox', '--disable-gpu'] });
  const page = await browser.newPage();
  await page.setViewport({ width: 1280, height: 1400 });
  await page.goto('https://eatgopty.com/menu-semanal/', { waitUntil: 'networkidle2' });
  
  // Click on Martes
  await page.evaluate(() => {
    const martesPill = document.querySelector('[data-id="407669ce"], [data-interaction-id="407669ce"]') || 
                       Array.from(document.querySelectorAll('p, a')).find(el => el.textContent.includes('MARTES'));
    if (martesPill) martesPill.click();
  });
  
  await new Promise(r => setTimeout(r, 600));
  await page.screenshot({ path: 'menu_martes_verified.png' });
  await browser.close();
  console.log('Martes screenshot saved!');
})();
