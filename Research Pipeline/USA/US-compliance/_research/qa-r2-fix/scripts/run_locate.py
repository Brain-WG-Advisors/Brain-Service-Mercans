import sys, json; sys.path.insert(0, '.')
from lib import *; from locate import *
fields, R = load_reg(); byid = {r['id']: r for r in R}
s = json.load(open('_research/qa-r2-fix/scan.json', encoding='utf-8'))
TIER = {'A.1': 0, 'A.2': 1, 'A.3': 2}
res = {}
for k, L in s.items():
    jp = 'US-' + k.split('.')[0].upper()
    for e in L:
        v = e['value']; row = byid.get(e['rid'], {})
        own = locate(k, v, files_of(row))
        best = None
        if not (own and own['score'] >= 1):
            for r in R:
                if not r['id'].startswith(jp) or r['id'] == e['rid'] or r['status'] not in ('active', 'partial'): continue
                if r['tier'] not in TIER: continue
                L2 = locate(k, v, files_of(r))
                if L2 and L2['score'] >= 1:
                    cand = (L2['score'], -TIER[r['tier']], r['id'], L2)
                    if best is None or cand[:2] > best[:2]: best = cand
        res.setdefault(k, []).append({**{x: e[x] for x in ('file', 'idx', 'value', 'eff', 'rid', 'miscited', 'reason')}, 'own_loc': own, 'new': best and {'id': best[2], **best[3]}})
json.dump(res, open('_research/qa-r2-fix/locate.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
import collections
c = collections.Counter()
for k, L in res.items():
    for e in L:
        st = 'own_ctx' if e['own_loc'] and e['own_loc']['score'] >= 1 else ('repoint' if e['new'] else ('own_noctx' if e['own_loc'] else 'none'))
        c[(e['miscited'], st)] += 1
print(c)
