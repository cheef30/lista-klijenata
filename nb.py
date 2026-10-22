import json,sys
q=json.load(open('waq.json')); k=int(sys.argv[1]) if len(sys.argv)>1 else 2
T=322845267
JS="const N='%s';const d=[...document.querySelectorAll('[role=\"dialog\"]')].map(x=>x.innerText.slice(0,60));const m=document.querySelector('#main');let r;if(!m){r={st:d.length?'nema WA':'nije ucitano',d}}else{const hdr=(m.querySelector('header')||{}).innerText||'';const box=(m.querySelector('footer [contenteditable=\"true\"]')||{}).innerText||'';if(!hdr.replace(/\\D/g,'').includes(N)){r={st:'drugi chat / kontakt',hdr:hdr.slice(0,40),d}}else if(!box.includes('Stefan')){r={st:'nema teksta',hdr}}else{m.querySelector('footer button[aria-label=\"Send\"]').click();await new Promise(z=>setTimeout(z,3000));const b2=(m.querySelector('footer [contenteditable=\"true\"]')||{}).innerText.trim();const ok=m.innerText.slice(-900).includes('Stefan')&&b2==='';r={st:ok?'POSLATO':'proveri',hdr:hdr.slice(0,30)}}}JSON.stringify(r)"
a=[]
for x in q[:k]:
    ph=x['url'].split('phone=')[1].split('&')[0][3:]
    a+= [{"name":"navigate","input":{"tabId":T,"url":x['url']}}]+[{"name":"computer","input":{"tabId":T,"action":"wait","duration":10}}]*2+[{"name":"computer","input":{"tabId":T,"action":"wait","duration":8}},{"name":"javascript_tool","input":{"tabId":T,"action":"javascript_exec","text":JS%ph}}]
print(' + '.join(x['n'] for x in q[:k]))
print(json.dumps(a,ensure_ascii=False))
