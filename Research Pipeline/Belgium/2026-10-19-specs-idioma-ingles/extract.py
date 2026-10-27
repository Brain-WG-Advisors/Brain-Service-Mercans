import glob,os,re,json
from openpyxl import load_workbook
import sys; sys.path.insert(0,'.'); from langdefs import *
FR2=FR|set("à été être où après avant chaque lorsqu autre autres cas même ainsi peut doivent concerné concernée cadre ayant dont auprès fixant correspondant relative relatif mesure période travailleurs données numéro".split())
def score(v):
    w=re.findall(r"[a-zàâçéèêëîïôûùüÿœ]+",v.lower())
    return sum(x in FR2 for x in w), sum(x in EN for x in w)
cells=[];uniq={}
for f in sorted(glob.glob('be19/BE-NSSO-00[1-4]*.xlsx')+glob.glob('be19/BE-FEDRIS*.xlsx')):
    wb=load_workbook(f,read_only=True); core=[s for s in wb.sheetnames if s.endswith('Spec')][0]
    for i,r in enumerate(wb[core].iter_rows(values_only=True),start=1):
        if i==1: continue
        for col in "GM":
            v=r[ord(col)-65] if ord(col)-65<len(r) else None
            if not isinstance(v,str) or not v.strip() or v.startswith("═"): continue
            fr,en=score(v)
            cells.append(dict(file=os.path.basename(f),cell=f"{col}{i}",text=v,fr=fr,en=en))
json.dump(cells,open('mg_cells.json','w',encoding='utf-8'),ensure_ascii=False,indent=0)
import collections
c=collections.Counter((x['file'][:14],x['cell'][0],'FR' if x['fr']>0 else 'none') for x in cells)
for k in sorted(c): print(k,c[k])
u=set(x['text'] for x in cells if x['fr']>0); print('unique FR-ish texts',len(u), 'chars',sum(len(t) for t in u))
