// Pokreni na Google Maps strani pretrage, sa: const KEY='deo imena malim slovima';
// Otvori karticu firme, klikne "Прикажи слике", sačuva linkove fotografija u localStorage 'ph_'+KEY.
const a=[...document.querySelectorAll('a.hfpxzc')].find(x=>x.getAttribute('aria-label').toLowerCase().includes(KEY))||document.querySelector('a.hfpxzc');if(a){a.click();await new Promise(r=>setTimeout(r,4000));}
const btn=[...document.querySelectorAll('button')].find(x=>/Прикажи слике|See photos|Prikaži slike/.test(x.getAttribute('aria-label')||x.innerText));if(btn){btn.click();await new Promise(r=>setTimeout(r,4000));}
const urls=new Set();document.querySelectorAll('[style*="googleusercontent"], img').forEach(e=>{let u=e.tagName==='IMG'?e.src:((e.getAttribute('style')||'').match(/url\("?([^")]+)/)||[])[1];if(u&&/googleusercontent\.com\/(p\/|gps-cs)/.test(u))urls.add(u.split('=')[0]);});
localStorage.setItem('ph_'+KEY,JSON.stringify([...urls]));KEY+': '+urls.size
