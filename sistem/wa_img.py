"""Pravi browser_batch JSON za slanje slike+teksta (caption) jednoj firmi.
python3 wa_img.py prep <ime>   -> batch: screenshot slike + otvori chat + uhvati Photos input
python3 wa_img.py send <ime>   -> batch: nalepi caption, proveri, posalji, proveri
"""
import json, sys, re, unicodedata, os
import os
T = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "tabs.json")))
WA, IMG = T["wa"], T["img"]
import subprocess
SHA = subprocess.run(["git","-C",os.path.dirname(os.path.abspath(__file__)),"rev-parse","HEAD"],capture_output=True,text=True).stdout.strip() or "main"
REPO_RAW = f"https://raw.githubusercontent.com/cheef30/lista-klijenata/{SHA}/mockups/"
def slug(s):
    s = unicodedata.normalize("NFKD", s.replace("đ","dj").replace("Đ","Dj")).encode("ascii","ignore").decode()
    return re.sub(r"[^a-z0-9]+","-",s.lower()).strip("-")
leads = {x["n"]: x for x in json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "danas.json")))}
mode, name = sys.argv[1], sys.argv[2]
L = leads[name]
num = re.sub(r"\D","",L["tel"]).lstrip("0")
if mode in ("prep","prepwa"):
    js = ("const m=document.querySelector('#main');const d=[...document.querySelectorAll('[role=dialog]')].map(x=>x.innerText.slice(0,50));"
          "let out;if(!m){out='NEMA WA '+d}else{const hdr=(m.querySelector('header')||{}).innerText||'';const pane=m.querySelector('[role=application]')||m;const n=pane.querySelectorAll('[role=row]').length;"
          f"const dg=hdr.replace(/\\D/g,'');if(dg.length>5&&!dg.includes('{num}')){{out='DRUGI CHAT '+hdr}}else if(n>1){{out='VEC IMA PORUKA rows='+n}}else{{"
          "m.querySelector('footer button[aria-label=\"Attach\"]').click();await new Promise(r=>setTimeout(r,1500));"
          "window.__orig=window.__orig||HTMLInputElement.prototype.click;window.__pin=null;HTMLInputElement.prototype.click=function(){if(this.type==='file'){window.__pin=this;if(!this.isConnected){this.style.display='none';document.body.appendChild(this);}return;}return window.__orig.call(this)};"
          "const it=[...document.querySelectorAll('[role=menuitem]')].find(x=>/Photos/.test(x.innerText));it&&it.click();await new Promise(r=>setTimeout(r,800));HTMLInputElement.prototype.click=window.__orig;"
          "const ins=[...document.querySelectorAll('input[type=file]')];out='SPREMNO rows='+n+' pin_index='+ins.indexOf(window.__pin)+' od '+ins.length}}out")
    a = ([] if mode=="prepwa" else [{"name":"navigate","input":{"tabId":IMG,"url":REPO_RAW+slug(name)+".jpg"}},
         {"name":"computer","input":{"tabId":IMG,"action":"wait","duration":2}},
         {"name":"computer","input":{"tabId":IMG,"action":"screenshot"}}]) + [{"name":"navigate","input":{"tabId":WA,"url":"https://web.whatsapp.com/send?phone=381"+num}},
         {"name":"computer","input":{"tabId":WA,"action":"wait","duration":10}},
         {"name":"computer","input":{"tabId":WA,"action":"wait","duration":4}},
         {"name":"javascript_tool","input":{"tabId":WA,"action":"javascript_exec","text":js}},{"name":"find","input":{"tabId":WA,"query":"file input elements (type=file)"}}]
else:
    msg = json.dumps(L["msg"], ensure_ascii=False)
    key = L.get("ck") or L["domain"]  # ck: tekst koji sigurno postoji u poruci
    js = (f"const msg={msg};let out;const hdr=document.querySelector('#main header').innerText;"
          f"const dg=hdr.replace(/\\D/g,'');if(dg.length>5&&!dg.includes('{num}')){{out='DRUGI CHAT'}}else{{"
          "let cap=null;for(let i=0;i<6&&!cap;i++){cap=[...document.querySelectorAll('[contenteditable=true]')].find(e=>!e.closest('#main footer'));if(!cap)await new Promise(r=>setTimeout(r,700));}"
          "if(!cap){out='NEMA CAPTION POLJA'}else{cap.focus();const dt=new DataTransfer();dt.setData('text/plain',msg);cap.dispatchEvent(new ClipboardEvent('paste',{clipboardData:dt,bubbles:true,cancelable:true}));await new Promise(r=>setTimeout(r,900));"
          f"if(!cap.innerText.includes('{key}')){{out='CAPTION NIJE UPISAN'}}else{{const b=[...document.querySelectorAll('[aria-label^=\"Send \"]')].find(e=>/selected/.test(e.getAttribute('aria-label')));b.click();await new Promise(r=>setTimeout(r,6000));"
          f"const t=document.querySelector('#main').innerText;out=t.includes('{key}')?'POSLATO':'PROVERI'}}}}}}out")
    a = [{"name":"javascript_tool","input":{"tabId":WA,"action":"javascript_exec","text":js}}]
print(json.dumps(a, ensure_ascii=False))
