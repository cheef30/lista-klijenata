import json,sys
q=json.load(open('waq.json')); r=json.load(open('wa_res.json'))
for a in sys.argv[1:]:
    st=a
    x=q.pop(0); r[x['n']]=st; print(x['n'],'->',st)
json.dump(q,open('waq.json','w'),ensure_ascii=False); json.dump(r,open('wa_res.json','w'),ensure_ascii=False,indent=1)
print(len(q),'left; today POSLATO count:', sum(1 for v in r.values() if v=='POSLATO'))
for x in q[:3]: print(x['n']); print(x['url'])
