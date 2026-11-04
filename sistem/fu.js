(async()=>{const m=document.querySelector('#main');let out;if(!m){out='NEMA CHAT'}else{const hdr=(m.querySelector('header')||{}).innerText||'';const dg=hdr.replace(/\D/g,'');
if(dg.length>5&&!dg.includes(window.NUM)){out='DRUGI '+hdr.slice(0,30)}else{
const W=m.getBoundingClientRect();let mi=0,mo=0;
[...m.querySelectorAll('[role=row]')].filter(r=>r.querySelector('[data-id]')).forEach(r=>{const p=r.querySelector('[data-pre-plain-text]');const pt=p?p.getAttribute('data-pre-plain-text'):'';
const b=[...r.querySelectorAll('div')].find(d=>{const q=d.getBoundingClientRect();return q.width>60&&q.width<W.width*0.8});let dir='';
if(b){const q=b.getBoundingClientRect();const L=q.left-W.left,Rr=W.right-q.right;dir=Rr<L-50?'o':(L<Rr-50?'i':'')}
if(/\] Stefan:/.test(pt)||(!pt&&dir==='o'))mo++;else if(pt||dir==='i')mi++;});
if(mi>0){out='ODGOVORIO in='+mi+' :: '+m.innerText.slice(-250).replace(/\n+/g,' / ')}
else if(mo<1||mo>2||m.innerText.includes('proverim')){out='PRESKOCI out='+mo}
else if(window.DRY){out='OK ZA SLANJE out='+mo}
else{const box=m.querySelector('footer [contenteditable=true]');box.focus();const dt=new DataTransfer();dt.setData('text/plain',window.MSG);
box.dispatchEvent(new ClipboardEvent('paste',{clipboardData:dt,bubbles:true,cancelable:true}));await new Promise(r=>setTimeout(r,700));
const b=m.querySelector('footer button[aria-label="Send"]');if(!b){out='NEMA SEND'}else{b.click();await new Promise(r=>setTimeout(r,2500));out=m.innerText.includes('samo da proverim')?'POSLATO':'PROVERI'}}}}return out})()