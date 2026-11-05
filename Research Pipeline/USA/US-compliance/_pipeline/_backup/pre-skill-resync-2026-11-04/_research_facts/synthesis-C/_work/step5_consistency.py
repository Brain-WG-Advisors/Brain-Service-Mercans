import json,glob,collections,sys,os
by=collections.defaultdict(lambda: collections.defaultdict(set))
for f in sorted(glob.glob(os.path.join(sys.argv[1],'*-facts.json'))):
    d=json.load(open(f,encoding='utf-8'))
    for x in d['facts']:
        v=x['value']; v=round(v,6) if isinstance(v,float) else v
        by[x['key']][os.path.basename(f)].add((x['effective_from'],x.get('effective_to'),json.dumps(v),x['register_id']))
div=[]
for k,files in by.items():
    if len(files)<2: continue
    sig={fn:frozenset((a,b,c) for a,b,c,_ in s) for fn,s in files.items()}
    if len(set(sig.values()))>1: div.append((k,{fn:sorted(s) for fn,s in files.items()}))
print('keys in >1 file:',sum(1 for f in by.values() if len(f)>1),'divergent:',len(div))
for k,v in div:
    print('##',k)
    for fn,s in v.items(): print('   ',fn,s)
