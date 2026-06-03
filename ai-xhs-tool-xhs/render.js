const puppeteer = require('puppeteer-core');
const path = require('path');
const fs = require('fs');

async function renderPage(pageNum, outputPath) {
  const browser = await puppeteer.launch({
    executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    headless: 'new',
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });

  const page = await browser.newPage();
  await page.setViewport({ width: 1080, height: 1440, deviceScaleFactor: 1 });

  const htmlPath = path.resolve(__dirname, 'index.html');
  await page.goto(`file://${htmlPath}`, { waitUntil: 'networkidle0' });

  await new Promise(r => setTimeout(r, 1500));

  const posterId = `xhs-0${pageNum}`;
  
  // Method: find the element, get its bounding box, scroll to it, then screenshot
  const element = await page.$(`#${posterId}`);
  if (!element) {
    console.error(`Element #${posterId} not found!`);
    await browser.close();
    return;
  }

  const boundingBox = await element.boundingBox();
  if (!boundingBox) {
    console.error(`BoundingBox for #${posterId} is null!`);
    await browser.close();
    return;
  }

  console.log(`Page ${pageNum}: boundingBox=${JSON.stringify(boundingBox)}`);

  // Scroll the element into view
  await element.scrollIntoView();
  await new Promise(r => setTimeout(r, 500));

  // Screenshot the element directly
  await element.screenshot({
    path: outputPath,
    type: 'png'
  });

  await browser.close();
  console.log(`Rendered page ${pageNum} -> ${outputPath}`);
}

async function main() {
  const outputDir = path.resolve(__dirname, 'output');
  if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir, { recursive: true });
  }

  for (let i = 1; i <= 8; i++) {
    await renderPage(i, path.join(outputDir, `page${i}.png`));
  }

  console.log('All 8 pages rendered successfully!');
}

main().catch(console.error);