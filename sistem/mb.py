import json,sys,urllib.parse
js=open('/home/claude/leads/sistem/maps_extract.js').read().strip()
tab=int(sys.argv[1]); qs=sys.argv[2:]
a=[]
for q in qs:
  a+= [{"name":"navigate","input":{"tabId":tab,"url":"https://www.google.com/maps/search/"+urllib.parse.quote_plus(q)+"?hl=sr"}},{"name":"computer","input":{"tabId":tab,"action":"wait","duration":5}},{"name":"javascript_tool","input":{"tabId":tab,"action":"javascript_exec","text":"await "+js}}]
print(json.dumps(a,ensure_ascii=False))
