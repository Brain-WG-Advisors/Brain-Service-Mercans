import json,re,collections
c=json.load(open('mg_cells.json',encoding='utf-8'))
EXTRA={"Voie publique.","Code permettant d'identifier un pays.","Code permettant de distinguer un apprenti.","Exprimée en jours calendriers."}
PFX="Restated at its corrected value for the original quarter. "
targets=[];units=collections.OrderedDict()
for x in c:
    t=x['text']; pre=''
    if t.startswith(PFX): pre=PFX; body=t[len(PFX):]
    else: body=t
    if x['fr']>0 or body in EXTRA:
        if body.startswith('NOT FOUND'): continue
        x['prefix']=pre; x['body']=body; targets.append(x); units.setdefault(body,None)
json.dump(targets,open('targets.json','w',encoding='utf-8'),ensure_ascii=False,indent=0)
U=list(units)
print(len(targets),'cells',len(U),'units',sum(map(len,U)),'chars')
cnt=collections.Counter((x['file'][:14],x['cell'][0]) for x in targets); print(sorted(cnt.items()))
# check other english prefixes: units starting with English
for u in U:
    if re.match(r"^[A-Z][a-z]+ [a-z]+ (the|a|is|of)\b",u): print('ENPFX?',u[:120])
n=4; k=(len(U)+n-1)//n
for i in range(n): json.dump({str(j):U[j] for j in range(i*k,min(len(U),(i+1)*k))},open(f'batch{i+1}.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
