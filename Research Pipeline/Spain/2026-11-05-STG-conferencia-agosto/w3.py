import sys, json
sys.stdout.reconfigure(encoding='utf-8')
w=json.load(open('wtc.json',encoding='utf-8'))
g=json.load(open('g2n.json',encoding='utf-8'))
codes=[str(h).split(' - ')[0] for h in g['hdr'] if h]
for c in codes:
    if c.startswith('52') or c[0] in '6' and c not in ('64440','64992','64993','64994','64996','64997','64998','64999','63952','63953','63956','63957'): continue
    v=w['rows'].get(c)
    if not v: continue
    print('=====',c,v[1],'|',v[4],'|',v[6])
    print('  EXPL:',(v[3] or '')[:500])
    print('  F:',(v[5] or '')[:900])
