// Run from repo root with a local server at HOME_QA_URL (default :8769).
// Set PLAYWRIGHT_MODULE to the installed Playwright module if scratch deps differ.
import { createRequire } from 'node:module';
import { readFileSync, writeFileSync } from 'node:fs';
import { execFileSync } from 'node:child_process';
import { resolve } from 'node:path';
import assert from 'node:assert/strict';
const require=createRequire(import.meta.url);
const {webkit,chromium}=require(process.env.PLAYWRIGHT_MODULE || './.scratch/gate/probes/ux/node_modules/playwright');
const out=resolve('qa/priority-growth-2026-10-07');
process.env.TMPDIR=resolve(out,'.scratch');
const url=process.env.HOME_QA_URL || 'http://127.0.0.1:8769/';
const before=execFileSync('git',['show','21cd40942dc64d2a48498a4d8ff4caa4c0e4d661:index.html'],{encoding:'utf8'});
const after=readFileSync('index.html','utf8');
for(const pattern of [/<style>([\s\S]*?)<\/style>/,/<!-- analytics -->[\s\S]*?<!-- \/analytics -->/]) assert.equal(before.match(pattern)[0],after.match(pattern)[0]);
const links=s=>[...s.matchAll(/href="([^"]+)"/g)].map(m=>m[1]).sort();
assert.deepEqual(links(before),links(after));
assert(after.includes('Haveo is an iPhone and iPad app for networking event prep.'));
assert(after.includes('<time data-page-updated datetime="2026-10-07">'));
assert(/<loc>https:\/\/haveo.app\/<\/loc>\s*<lastmod>2026-10-07<\/lastmod>/.test(readFileSync('sitemap.xml','utf8')));
const results=[];
for(const [name,engine] of [['webkit',webkit],['chromium',chromium]]){
 const browser=await engine.launch();
 try{
 for(const [width,height] of [[375,667],[390,844],[390,600],[1280,800]]){
  console.log('checking',name,width,height);
  const context=await browser.newContext({viewport:{width,height},deviceScaleFactor:1,hasTouch:true,isMobile:width<680});
  // Exercise the human-only listener while all collection is blocked.
  await context.addInitScript(()=>{const ua=navigator.userAgent.replace('Headless','');Object.defineProperty(navigator,'webdriver',{get:()=>false});Object.defineProperty(navigator,'userAgent',{get:()=>ua})});
  await context.route(/https:\/\/[^/]*(google-analytics|googletagmanager)\.com\//,r=>r.abort());
  // Synthetic click destination is intercepted; curl checks the real listing separately.
  await context.route('https://apps.apple.com/**',r=>r.fulfill({status:200,body:'Synthetic handoff destination.'}));
  const page=await context.newPage();page.setDefaultTimeout(10000);
  const errors=[];page.on('pageerror',e=>errors.push(String(e)));
  assert.equal((await page.goto(url)).status(),200);await page.evaluate(()=>document.fonts.ready);
  const primary=page.locator('.home-hero .btn-appstore');const box=await primary.boundingBox();
  assert(box.y+box.height<=height);assert(box.height>=44);
  assert.equal(await page.locator('.home-hero .btn').count(),1);
  assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));
  for(const link of await page.locator('.secondary-actions a').all()) assert((await link.boundingBox()).height>=44);
  assert(await page.locator('.hero-char img').evaluate(el=>el.complete&&el.naturalWidth>0));
  const screenshot=`after-${name}-${width}x${height}.png`;await page.screenshot({path:resolve(out,screenshot)});
  // macOS WebKit handles apps.apple.com outside the page (control example.com opens
  // normally). Record trusted input without invoking the OS; native iPhone handoff
  // stays pending. Chromium additionally checks the real anchor's popup URL.
  if(name==='webkit') await page.evaluate(()=>document.addEventListener('click',e=>{const a=e.target.closest('a[href*="apps.apple.com"]');if(a){window.qaHandoff={url:a.href,trusted:e.isTrusted};e.preventDefault()}},true));
  let destination;
  if(name==='chromium'){
   const popupPromise=page.waitForEvent('popup');await primary.locator('svg').tap();
   const popup=await popupPromise;await popup.waitForLoadState();destination=popup.url();await popup.close();
  }else{
   await primary.locator('svg').tap();const handoff=await page.evaluate(()=>window.qaHandoff);assert(handoff.trusted);destination=handoff.url;
  }
  const dest=new URL(destination);assert.equal(dest.host,'apps.apple.com');assert.equal(dest.pathname,'/app/haveo/id6774740212');assert.equal(dest.searchParams.get('ct'),'site-hero');
  const events=await page.evaluate(()=>Array.from(dataLayer).filter(x=>x[0]==='event'&&x[1]==='app_store_click').map(x=>x[2]));
  assert.deepEqual(events,[{placement:'site-hero',page_path:'/'}]);
  await page.getByRole('link',{name:'Share feedback',exact:true}).tap();await page.waitForFunction(()=>location.hash==='#feedback');
  await page.locator('#feedback .feedback').scrollIntoViewIfNeeded();assert(await page.getByRole('link',{name:'Send us feedback',exact:true}).isVisible());
  await page.goto(url);await page.evaluate(()=>document.fonts.ready);await page.keyboard.press(name==='webkit'?'Alt+Tab':'Tab');
  assert(await primary.evaluate(el=>el===document.activeElement));assert.notEqual(await primary.evaluate(el=>getComputedStyle(el).outlineStyle),'none');
  if(name==='webkit'){
   await page.evaluate(()=>document.addEventListener('click',e=>{const a=e.target.closest('a[href*="apps.apple.com"]');if(a){window.qaKeyboard=e.isTrusted;e.preventDefault()}},true));
   await page.keyboard.press('Enter');assert(await page.evaluate(()=>window.qaKeyboard));
  }else{const keyboardPopup=page.waitForEvent('popup');await page.keyboard.press('Enter');await(await keyboardPopup).close()}
  assert.deepEqual(errors,[]);
  results.push({browser:name,viewport:[width,height],button_rect:box,screenshot,handoff_url:destination,navigation:name==='chromium'?'popup URL verified':'trusted input verified; native App Store handoff pending',keyboard:'pass',feedback:'pass',synthetic_event:events[0],analytics_delivery:'blocked',overflow:false});await context.close();
 }
 let context=await browser.newContext({viewport:{width:375,height:667},javaScriptEnabled:false});let page=await context.newPage();await page.goto(url);
 assert(await page.locator('.home-hero .btn-appstore').isVisible());assert(await page.locator('.home-hero .sub').isVisible());await context.close();
 context=await browser.newContext({viewport:{width:375,height:667},reducedMotion:'reduce'});page=await context.newPage();await page.goto(url);await page.evaluate(()=>document.fonts.ready);
 assert.equal(await page.locator('.hero-char').evaluate(el=>getComputedStyle(el).animationName),'none');
 const primary=page.locator('.home-hero .btn-appstore');await primary.hover();await page.mouse.down();assert.equal(await primary.evaluate(el=>getComputedStyle(el).transform),'none');
 await page.mouse.move(0,0);await page.mouse.up();await page.screenshot({path:resolve(out,`reduced-motion-${name}.png`)});await context.close();
 }finally{await browser.close()}
}
writeFileSync(resolve(out,'verification.json'),JSON.stringify({checks:results,no_js:['webkit','chromium'],reduced_motion:['webkit','chromium'],raw_html:'pass',shared_css_analytics_and_links:'unchanged'},null,2)+'\n');
console.log(`PASS: ${results.length} browser/viewport cases; touch, keyboard, synthetic attribution, no-JS and reduced motion. WebKit native App Store handoff remains pending.`);
