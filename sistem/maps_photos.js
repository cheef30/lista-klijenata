const a=[...document.querySelectorAll('a.hfpxzc')].find(x=>x.getAttribute('aria-label').toLowerCase().includes(KEY))||document.querySelector('a.hfpxzc');if(a){a.click();await new Promise(r=>setTimeout(r,4000));}
const tab=[...document.querySelectorAll('button[role=tab]')].find(x=>/Слике|Photos|Fotografije/.test(x.innerText));if(tab){tab.click();await new Promise(r=>setTimeout(r,3500));}
const sc=[...document.querySelectorAll('[role=main] div')].find(d=>d.scrollHeight>d.clientHeight+200);if(sc){for(let i=0;i<3;i++){sc.scrollBy(0,2000);await new Promise(r=>setTimeout(r,1200));}}
const urls=new Set();document.querySelectorAll('[role=main] [style*="googleusercontent"], [role=main] img').forEach(e=>{let u=e.tagName==='IMG'?e.src:(e.getAttribute('style').match(/url\("?([^")]+)/)||[])[1];if(u&&/googleusercontent\.com\/(p|gps)/.test(u))urls.add(u.split('=')[0]);});
localStorage.setItem('ph_'+KEY,JSON.stringify([...urls]));KEY+': '+urls.size
