exec(open('base.py',encoding='utf-8').read())
e=[x for x in E if x['id']=='1016737'][0]
print({k:v for k,v in e.items() if not (k.startswith('52') or k.startswith('58')) and v not in (0,0.0,'')})
import json
g=json.load(open('g2n.json',encoding='utf-8'))
for r in g['rows']:
    if str(r[0])=='1016737': print([ (g['hdr'][i],v) for i,v in enumerate(r) if i<45 and v not in (None,0,0.0,'')][4:])
