const { chromium } = require('playwright');
const path = require('path');

async function renderCards() {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  
  const htmlPath = path.join(__dirname, 'index.html');
  await page.goto(`file://${htmlPath}`, { waitUntil: 'networkidle' });
  
  // Wait for fonts to load
  await page.waitForTimeout(2000);
  
  // Card IDs to render
  const cards = [
    { id: 'cn-card-01', name: 'cn-cover' },
    { id: 'cn-card-02', name: 'cn-collapse-inevitable' },
    { id: 'cn-card-03', name: 'cn-tech-boom' },
    { id: 'cn-card-04', name: 'cn-flat-societies' },
    { id: 'en-card-01', name: 'en-cover' },
    { id: 'en-card-02', name: 'en-collapse-inevitable' },
    { id: 'en-card-03', name: 'en-tech-boom' },
    { id: 'en-card-04', name: 'en-flat-societies' },
  ];
  
  const outputDir = path.join(__dirname, 'output');
  const fs = require('fs');
  if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir, { recursive: true });
  }
  
  for (const card of cards) {
    const element = await page.$(`#${card.id}`);
    if (element) {
      await element.screenshot({
        path: path.join(outputDir, `${card.name}.png`),
        type: 'png',
      });
      console.log(`Rendered: ${card.name}.png`);
    }
  }
  
  await browser.close();
  console.log('All cards rendered successfully!');
}

renderCards().catch(console.error);