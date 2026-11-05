import sys, json; sys.path.insert(0, '.')
from lib import *
fields, R = load_reg(); byid = {r['id']: r for r in R}
rev = json.load(open('_qa/CCG-review-r2.json', encoding='utf-8'))
mk = rev['findings'][29]['_mis_cited_keys']
unv = rev['numeric_verification']['unverified_keys']; reasons = rev['numeric_verification']['_numeric_unverified_reasons']
target = set(mk) | set(reasons)
TIER = {'A.1': 0, 'A.2': 1, 'A.3': 2}
out = {}
for fn in facts_files():
    d = json.load(open(fn, encoding='utf-8'))
    for i, f in enumerate(d.get('facts', [])):
        if f['key'] not in target: continue
        v = f['value']; rid = f.get('register_id'); row = byid.get(rid, {})
        own = any(find(v, text_of(p)) for p in files_of(row))
        cands = []
        if not own and isinstance(v, (int, float)) and not isinstance(v, bool):
            jp = 'US-' + f['key'].split('.')[0].upper()
            for r in R:
                if not r['id'].startswith(jp) or r['id'] == rid: continue
                for p in files_of(r):
                    h = find(v, text_of(p))
                    if h:
                        t = text_of(p); pos = h[0][0]
                        cands.append({'id': r['id'], 'tier': r['tier'], 'status': r['status'], 'n': len(h), 'page': page_at(t, pos), 'snip': snippet(t, pos, 70), 'file': p, 'inst': r['instrument_name'][:80]})
                        break
            cands.sort(key=lambda c: (c['status'] != 'active', TIER.get(c['tier'], 9), -c['n']))
        out.setdefault(f['key'], []).append({'file': fn, 'idx': i, 'value': v, 'eff': f.get('effective_from'), 'rid': rid, 'rid_has_file': bool(files_of(row)), 'own': own, 'reason': reasons.get(f['key']), 'miscited': f['key'] in mk, 'cands': cands[:4]})
json.dump(out, open('../scan.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
import collections
c = collections.Counter()
for k, L in out.items():
    for e in L:
        c[(e['miscited'], e['own'], bool(e['cands']), e['rid_has_file'])] += 1
print(c); print(len(out), 'of', len(target))
