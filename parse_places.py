import json,sys,re,glob,os
seen=set()
for l in open('new_leads.tsv'): seen.add(re.sub(r'\D','',l.split('\t')[3])[-8:])
old=json.load(open('data.json'))
for x in old: seen.add(re.sub(r'\D','',x['tel'])[-8:])
out=[]
for f in sys.argv[1:]:
    t=open(f).read()
    try: d=json.loads(t)
    except Exception:
        d=json.loads(t[t.index('{'):t.rindex('}')+1])
    for p in d.get('places',[]):
        ph=p.get('phone_number') or ''
        dig=re.sub(r'\D','',ph)
        if not dig.startswith('3816'): continue
        k=dig[-8:]
        if k in seen: continue
        seen.add(k)
        revs=[r for r in p.get('reviews',[]) if len(r)>25][:1]
        print(f"{p['name']} | {p['address'].split(',')[-2].strip()[:22] if ',' in p['address'] else p['address'][:22]} | {p.get('types',[''])[0]} | 0{dig[3:5]} {dig[5:]} | {p.get('rating')} ({p.get('rating_count')}) || " + ' ## '.join(r[:110].replace('\n',' ') for r in revs))
