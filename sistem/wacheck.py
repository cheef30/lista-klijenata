import json,sys
T=json.load(open('/home/claude/leads/sistem/tabs.json'))['wa']
js="const m=document.querySelector('#main');const d=[...document.querySelectorAll('[role=dialog]')].map(x=>x.innerText.slice(0,30));m?'WA '+(m.querySelector('header')||{}).innerText.slice(0,22)+' rows='+(m.querySelector('[role=application]')||m).querySelectorAll('[role=row]').length:'NO '+d"
a=[]
for n in sys.argv[1:]:
  n=n.lstrip('0')
  a+=[{"name":"navigate","input":{"tabId":T,"url":"https://web.whatsapp.com/send?phone=381"+n}},{"name":"computer","input":{"tabId":T,"action":"wait","duration":10}},{"name":"computer","input":{"tabId":T,"action":"wait","duration":3}},{"name":"javascript_tool","input":{"tabId":T,"action":"javascript_exec","text":js}}]
print(json.dumps(a))
