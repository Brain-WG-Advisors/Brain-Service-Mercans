import re,json
L=open('anexo.txt',encoding='utf-8').read().split('\n')
# table 1 region: from first NIE001 line (1213) to before 'NIAE' region
start=1213
end=[i for i,l in enumerate(L) if l.strip().startswith('NIAE001')][0]
junk=re.compile(r'Resoluci|Formule|www\.dian|Carrera 8|Código postal|\(11 FEB|Dirección de Gest|^Anexo Técnico|^Página|=====PAGE|^ID\s*$|^ns\s*$|^Campo\s*$|^Descripción\s*$|^T\s*$|^F Tam|^Padre\s*$|^Oc\s*$|^Observaciones\s*$|^V\s*$|^Xpath\s*$')
blocks={}; cur=None
for l in L[start-1:end]:
    s=l.strip()
    if re.fullmatch(r'NIE\d{3}',s):
        cur=s; blocks[cur]=[]; continue
    if cur and s and not junk.search(s): blocks[cur].append(s)
rec={}
for k,v in blocks.items():
    txt=' | '.join(v)
    oc=re.search(r'\b([01])-(\d+|N)\b',txt)
    # type line: 'A A 11' or 'E N'
    m=re.search(r'(?:^|\| )([AE]) ([A-Z])\s*(\d+(?:-\d+)?)?(?: \||$)',txt)
    xp=re.search(r'(/Nomina\S*(?: \| \S+)*)',txt)
    xp=''
    for j,ln in enumerate(v):
        if ln.startswith('1.0') :
            rest=ln[3:].strip(); parts=[rest] if rest else []
            for ln2 in v[j+1:]:
                if ' ' in ln2 or not (ln2.startswith('/') or parts): break
                parts.append(ln2)
            xp=''.join(parts); break
    rec[k]=dict(xp=xp,lines=v,name=v[0] if v else '',T=m.group(1) if m else None,F=m.group(2) if m else None,tam=m.group(3) if m else None,oc=oc.group(0) if oc else None,txt=txt)
json.dump(rec,open('anexo_nie.json','w',encoding='utf-8'),ensure_ascii=False,indent=0)
print(len(rec))
for k in sorted(rec)[:12]: print(k,{x:rec[k][x] for x in ('name','T','F','tam','oc')})
