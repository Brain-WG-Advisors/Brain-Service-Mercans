# Local C46 emulation on the annex markdown (the real check scans the assembled DOCX).
import sys, os, glob, json, re, collections
sys.path.insert(0, os.path.expanduser("~/mercans-pipeline/shared/consistency-checks"))
import consistency_checks as cc
BASE = sys.argv[1]; JURS = sys.argv[2].split(",")
facts_last, facts_all = {}, collections.defaultdict(set)
for fp in glob.glob(os.path.join(BASE, "_research", "*-facts.json")):
    for f in json.load(open(fp, encoding="utf-8")).get("facts", []):
        facts_last[f["key"]] = f.get("value"); facts_all[f["key"]].add(json.dumps(f.get("value")))
forms = {}
for k, v in facts_last.items():
    for n, pct in cc.distinctive_forms(k, v):
        forms.setdefault((round(n, 6), pct), set()).add(k)
tot = collections.Counter()
for j in JURS:
    p = os.path.join(BASE, "01-ccg", "annexes", f"annex_{j}.md")
    mism, multi, unb, notkey = [], [], [], []
    for i, t in enumerate(open(p, encoding="utf-8").read().splitlines(), 1):
        for m in cc.TAG.finditer(t):
            k, v = m.group(1), m.group(2)
            if k not in facts_last: notkey.append((i, k)); continue
            a, b = cc._num(v), cc._num(facts_last[k])
            same = (abs(a-b) < 1e-9) if (a is not None and b is not None) else (str(v).strip() == str(facts_last[k]).strip())
            if not same:
                # does it equal another period's value of the same key?
                ok = any((cc._num(json.loads(x)) is not None and a is not None and abs(cc._num(json.loads(x))-a) < 1e-9) or str(json.loads(x)).strip()==v.strip() for x in facts_all[k])
                (multi if ok else mism).append((i, k, v))
        bare = cc.TAG.sub(" ", t)
        for m in cc.NUM_IN_TEXT.finditer(bare):
            n = cc._num(m.group(1))
            if n is None: continue
            ks = forms.get((round(n, 6), bool(m.group(2))))
            if ks: unb.append((i, m.group(0).strip(), sorted(ks)[:3]))
    tot.update(mism=len(mism), multi=len(multi), unbound=len(unb), notkey=len(notkey), tags=len(cc.TAG.findall(open(p, encoding='utf-8').read())))
    print(f"== {j}: tags-ok-but-other-period {len(multi)}, MISMATCH {mism}, NOT-A-KEY {notkey}")
    for u in unb: print("   unbound", u)
print(dict(tot))
