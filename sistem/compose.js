// Compose primera u google.com tabu. Postavi SHA, SLUG, KEY, PICK, DOM pre pokretanja.
const SHA='__SHA__',SLUG='__SLUG__',KEY='__KEY__',PICK=__PICK__,DOM='__DOM__';
const ph=JSON.parse(localStorage.getItem('ph_'+KEY)||'[]');
if(ph.length<5){'MALO SLIKA '+ph.length}else{
const R='https://raw.githubusercontent.com/cheef30/lista-klijenata/'+SHA+'/sistem/mockup/real/';
let p=await (await fetch(R+'pages/'+SLUG+'.html')).text();
PICK.forEach((k,i)=>{p=p.split('{{I'+i+'}}').join(ph[k]+'=w1600');});
let w=await (await fetch(R+'wrap.html')).text();
const esc=p.replace(/&/g,'&amp;').replace(/"/g,'&quot;');
w=w.split('{{DOMAIN}}').join(DOM).split('{{SD}}').join(esc);
document.open();document.write(w);document.close();
await new Promise(r=>setTimeout(r,3500));
document.getElementById('st').style.transform='translate(-50%,-50%) scale('+Math.min(innerWidth/1420,innerHeight/740)+')';
'OK '+ph.length+' slika'}
