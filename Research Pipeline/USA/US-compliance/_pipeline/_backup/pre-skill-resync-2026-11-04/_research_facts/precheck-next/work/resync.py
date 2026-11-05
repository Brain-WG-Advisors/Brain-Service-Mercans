import json,glob,os,collections
R='../..'
ref={}  # (key,eff)->fact  from CCG then RSPEC
for fn in sorted(glob.glob(R+'/CCG-*-facts.json'))+[R+'/RSPEC-facts.json']:
    d=json.load(open(fn,encoding='utf-8'))
    for f in d.get('facts',[]): ref[(f['key'],f.get('effective_from'))]=(os.path.basename(fn),f)
refk=collections.defaultdict(list)
for (k,e),v in ref.items(): refk[k].append(e)
out=[]
for fn in ['DD-8_sheets','WTC-global_baseline','WTC-country_specific','SIR','PSL']:
    d=json.load(open(R+'/%s-facts.json'%fn,encoding='utf-8'))
    for f in d['facts']:
        k=f['key']
        if k not in refk: continue
        r=ref.get((k,f.get('effective_from')))
        if not r: out.append((fn,k,'DATE-NOT-IN-REF',f.get('effective_from'),refk[k]));continue
        rf=r[1]
        for fld in ('value','effective_to','register_id'):
            if f.get(fld)!=rf.get(fld): out.append((fn,k,fld,f.get(fld),rf.get(fld),r[0]))
json.dump(out,open('resync.json','w'),ensure_ascii=False,indent=1)
print(len(out),collections.Counter((o[0],o[2]) for o in out))
for o in out[:40]: print(str(o)[:260])
