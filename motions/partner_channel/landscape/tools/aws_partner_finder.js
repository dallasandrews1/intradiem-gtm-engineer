const puppeteer = require('puppeteer-core');
(async () => {
  const browser = await puppeteer.launch({executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', headless: false, args: ['--no-sandbox', '--window-size=1400,2600']});
  const page = await browser.newPage();
  await page.setUserAgent('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36');
  const url = 'https://partners.amazonaws.com/search/partners?facets=Product%20%3A%20Amazon%20Connect%7CProduct%20%3A%20Amazon%20Connect%20%3A%20Omni-Channel%20Customer%20Experience%7CProduct%20%3A%20Amazon%20Connect%20%3A%20Agent%20Empowerment%20and%20Productivity%7CProduct%20%3A%20Amazon%20Connect%20%3A%20Analytics%2C%20Dashboards%20%26%20Reporting%7CProduct%20%3A%20Amazon%20Connect%20%3A%20Self-Service%20Configuration%20and%20Management';
  await page.goto(url, {waitUntil: 'networkidle0', timeout: 120000});
  await new Promise(r => setTimeout(r, 8000));
  // Location facet block
  const loc = await page.evaluate(() => {
    const t = document.body.innerText; const i = t.indexOf('Location'); return t.slice(i, i + 400);
  });
  console.error('LOCATION BLOCK: ' + loc.replace(/\n/g, ' / '));
  // try opening the location type select and choosing "Headquarters" then a region
  const opts = await page.evaluate(() => {
    const sel = [...document.querySelectorAll('select')].map(s => [...s.options].map(o => o.textContent.trim()).join(' | '));
    const btns = [...document.querySelectorAll('button')].filter(b => /location/i.test(b.textContent)).map(b => b.textContent.trim().slice(0, 60));
    return {sel, btns};
  });
  console.error('SELECTS: ' + JSON.stringify(opts).slice(0, 600));
  const all = [];
  for (let p = 0; p < 30; p++) {
    const cards = await page.evaluate(() => {
      const t = document.body.innerText;
      const out = [];
      const re = /Contact Partner\n([^\n]+)\n\n([^\n]+)\n/g; let m;
      while ((m = re.exec(t))) out.push({name: m[1].trim(), blurb: m[2].trim().slice(0, 300)});
      const c = (t.match(/(\d+)-(\d+) of (\d+) results/) || [])[0];
      return {out, c};
    });
    all.push(...cards.out);
    const next = await page.evaluate(() => {
      const b = document.querySelector('li[data-testid="pagination-right-arrow"] button');
      if (b && !b.disabled) { b.click(); return true; } return false;
    });
    if (p === 0) console.error('page1 ' + cards.c + ' cards ' + cards.out.length);
    if (!next) break;
    await new Promise(r => setTimeout(r, 3500));
  }
  const seen = new Map(); for (const c of all) seen.set(c.name, c);
  console.log(JSON.stringify([...seen.values()], null, 1));
  await browser.close();
})().catch(e => { console.error('ERR ' + e.message); process.exit(1); });
