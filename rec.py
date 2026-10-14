import json,sys
q=json.load(open('waq.json')); r=json.load(open('wa_res.json'))
retry=[]
for a in sys.argv[1:]:
    st='POSLATO 14.10.' if a=='POSLATO' else a
    x=q.pop(0)
    if a=='RETRY': retry.append(x); print(x['n'],'-> retry'); continue
    r[x['n']]=st; print(x['n'],'->',st)
q[0:0]=retry
json.dump(q,open('waq.json','w'),ensure_ascii=False); json.dump(r,open('wa_res.json','w'),ensure_ascii=False,indent=1)
print(len(q),'left; today POSLATO count:', sum(1 for v in r.values() if v=='POSLATO 14.10.'))
for x in q[:3]: print(x['n']); print(x['url'])
