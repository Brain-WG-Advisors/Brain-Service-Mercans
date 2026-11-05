import json,glob,re,os,sys
sys.stdout.reconfigure(encoding="utf-8")
want=re.compile(sys.argv[1],re.I)
seen=set()
for p in sorted(glob.glob('_research/*-facts.json')):
    a=os.path.basename(p).split('-')[0]
    for f in json.load(open(p,encoding='utf-8'))['facts']:
        k=f['key']
        if not want.search(k): continue
        if (k,str(f.get('value')),f.get('effective_from')) in seen: continue
        seen.add((k,str(f.get('value')),f.get('effective_from')))
        print(a,'|',k,'|',str(f.get('value'))[:90],'|',f.get('effective_from'),'|',f.get('register_id'),'|',f.get('url'))
