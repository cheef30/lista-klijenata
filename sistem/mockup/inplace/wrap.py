"""Pravi kompozit (desktop + telefon) od jedne HTML stranice, za ubacivanje u tab na domenu klijenta.
python3 wrap.py drinska.html drinskabajkaapartmani.rs > drinska.js"""
import sys, html, json
page = open(sys.argv[1], encoding="utf-8").read()
domain = sys.argv[2]
sd = html.escape(page, quote=True)
W = f'''<!doctype html><html><head><meta charset="utf-8"><style>
html,body{{margin:0;height:100%;background:#C9C6BE;overflow:hidden;font-family:system-ui,sans-serif}}
.stage{{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;gap:56px}}
.win{{width:950px;height:664px;border-radius:12px;overflow:hidden;background:#F7F7F5;box-shadow:0 30px 60px -28px rgba(40,40,40,.55)}}
.bar{{height:30px;display:flex;align-items:center;gap:7px;padding:0 12px}}
.bar i{{width:10px;height:10px;border-radius:50%;display:block}}
.bar span{{margin-left:40px;flex:1;max-width:620px;height:18px;border-radius:6px;background:#E7E6E2;font-size:11px;color:#4A5258;display:flex;align-items:center;padding-left:12px}}
.vp{{width:950px;height:634px;overflow:hidden}}
.vp iframe{{width:1440px;height:961px;border:0;transform:scale(.66);transform-origin:0 0}}
.ph{{width:300px;height:640px;border-radius:40px;background:#1E262B;padding:10px;box-shadow:0 30px 60px -26px rgba(30,30,30,.6)}}
.ph div{{width:280px;height:620px;border-radius:31px;overflow:hidden}}
.ph iframe{{width:390px;height:864px;border:0;transform:scale(.718);transform-origin:0 0}}
</style></head><body><div class="stage">
<div class="win"><div class="bar"><i style="background:#E26A5A"></i><i style="background:#E8B84A"></i><i style="background:#6BBF6A"></i><span>{domain}</span></div><div class="vp"><iframe srcdoc="{sd}"></iframe></div></div>
<div class="ph"><div><iframe srcdoc="{sd}"></iframe></div></div>
</div></body></html>'''
print("document.open();document.write(" + json.dumps(W, ensure_ascii=False) + ");document.close();'ok'")
