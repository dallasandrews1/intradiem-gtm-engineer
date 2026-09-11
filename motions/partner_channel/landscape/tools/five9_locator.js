const puppeteer = require('puppeteer-core');
const DEEP = `function deepAll(root, out) { out = out || []; for (const el of root.querySelectorAll('*')) { out.push(el); if (el.shadowRoot) deepAll(el.shadowRoot, out); } return out; }`;
(async () => {
  const browser = await puppeteer.launch({executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', headless: 'new', args: ['--no-sandbox']});
  const page = await browser.newPage();
  await page.setViewport({width: 1400, height: 2200});
  await page.goto('https://www.five9.com/partner-locator', {waitUntil: 'networkidle2', timeout: 120000});
  await new Promise(r => setTimeout(r, 8000));
  const grab = () => page.evaluate((DEEP) => {
    eval(DEEP);
    const all = deepAll(document);
    const leaf = e => e.children.length === 0 ? (e.textContent || '').trim() : '';
    const tiles = [];
    for (const n of all.filter(e => leaf(e) === 'Contact Us')) {
      let c = n;
      for (let k = 0; k < 10 && c.parentElement; k++) { c = c.parentElement; if ((c.textContent || '').length > 80 && (c.textContent||'').includes('|') === false && (c.innerText||'').split('\n').length >= 4) break; }
      tiles.push((c.innerText || '').replace(/\s*\n\s*/g, ' | ').replace(/\s+/g, ' ').trim());
    }
    const cnt = all.map(leaf).find(t => /^\d+\s*\/\s*\d+$/.test(t)) || (document.body.innerText.match(/(\d+)\s*\/\s*(\d+)/) || [])[0] || '?';
    return {tiles: tiles.filter(t => t.length > 40 && !/Get Support/.test(t)), cnt};
  }, DEEP);
  const clickNext = () => page.evaluate((DEEP) => {
    eval(DEEP);
    const cands = deepAll(document).filter(e => /^Next$/.test((e.textContent || '').trim()));
    const b = cands.find(e => /BUTTON|A|SPAN|DIV|LI/.test(e.tagName));
    if (b) { b.click(); return b.tagName + ' ' + (b.className || ''); } return null;
  }, DEEP);
  const seen = new Map();
  let prevKey = '', pages = 0, sameCount = 0;
  for (let i = 0; i < 260; i++) {
    const d = await grab();
    const key = d.tiles.map(t => t.slice(0, 30)).join('#');
    if (i === 0) console.error('first: cnt=' + d.cnt + ' tiles=' + d.tiles.length + ' :: ' + (d.tiles[0] || '').slice(0, 200));
    if (key && key !== prevKey) { for (const t of d.tiles) seen.set(t.slice(0, 90), t); pages++; sameCount = 0; prevKey = key; }
    else { sameCount++; if (sameCount > 4) { console.error('stuck at page ' + pages + ' cnt=' + d.cnt); break; } }
    const c = await clickNext();
    if (!c) { console.error('no Next'); break; }
    await new Promise(r => setTimeout(r, sameCount ? 3000 : 1600));
    if (i % 25 === 0) console.error('iter ' + i + ' pages ' + pages + ' tiles ' + seen.size + ' cnt=' + d.cnt + ' next=' + c);
  }
  console.log(JSON.stringify([...seen.values()], null, 1));
  await browser.close();
})().catch(e => { console.error('ERR ' + e.message); process.exit(1); });
