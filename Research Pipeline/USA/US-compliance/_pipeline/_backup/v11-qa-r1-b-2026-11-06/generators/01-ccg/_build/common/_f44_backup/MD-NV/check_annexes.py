# -*- coding: utf-8 -*-
"""Self-check of annexes MD..NV: tags vs facts (any period), C46-style unbound scan
against all facts files, C29 residual markers, C47 rework words. Run with python -I."""
import glob, json, os, re, sys, collections
BASE = sys.argv[1]
JURS = "MD ME MI MN MO MS MT NC ND NE NH NJ NM NV".split()
sys.path.insert(0, os.path.expanduser("~/mercans-pipeline/shared/consistency-checks"))
sys.path.insert(0, os.path.expanduser("~/mercans-pipeline/shared/release"))
import consistency_checks as cc  # noqa
import release_crosscheck as rc  # noqa

vals = collections.defaultdict(list)
last = {}
for fp in glob.glob(os.path.join(BASE, "_research", "*-facts.json")):
    for f in json.load(open(fp, encoding="utf-8")).get("facts", []):
        vals[f["key"]].append(f.get("value"))
        last[f["key"]] = f.get("value")
forms = {}
for k, v in last.items():
    for n, pct in cc.distinctive_forms(k, v):
        forms.setdefault((round(n, 6), pct), set()).add(k)
pats, legit, external = rc.build_patterns("1.0", {})
C29 = re.compile(r"\[placeholder\]|\bTODO\b|\bTBD\b|\bFIXME\b|\bXXX\b|\[CHECK\]|\[\?\]|VERIFY No\.|to be confirmed|to be verified", re.I)
tot = collections.Counter()
for j in JURS:
    p = os.path.join(BASE, "01-ccg", "annexes", f"annex_{j}.md")
    t = open(p, encoding="utf-8").read()
    bad, single, unb, c29, rw = [], [], [], [], []
    for ln, line in enumerate(t.split("\n"), 1):
        for m in cc.TAG.finditer(line):
            k, v = m.group(1), m.group(2)
            if k not in vals:
                bad.append((ln, k, "missing key"))
                continue
            ok = any((cc._num(v) is not None and cc._num(x) is not None and abs(cc._num(v) - cc._num(x)) < 1e-9)
                     or str(v).strip() == ("True" if x is True else "False" if x is False else str(x)).strip()
                     for x in vals[k])
            if not ok:
                bad.append((ln, k, v))
            a, b = cc._num(v), cc._num(last[k])
            same = (abs(a - b) < 1e-9) if (a is not None and b is not None) else (str(v).strip() == str(last[k]).strip())
            if ok and not same:
                single.append((ln, k, v, last[k]))
        bare = cc.TAG.sub(" ", line)
        for m in cc.NUM_IN_TEXT.finditer(bare):
            n = cc._num(m.group(1))
            if n is None:
                continue
            ks = forms.get((round(n, 6), bool(m.group(2))))
            if ks:
                unb.append((ln, m.group(0).strip(), sorted(ks)[:2]))
        if C29.search(line):
            c29.append(ln)
        clean = cc.TAG.sub(" ", line).replace("RESEARCH-GAP", "")
        for name, rx in pats.items():
            if name.startswith("finding ids"):
                continue
            for m in rx.finditer(clean):
                if not legit.search(clean):
                    rw.append((ln, name, m.group(0)))
    tot["bad"] += len(bad); tot["single"] += len(single); tot["unbound"] += len(unb); tot["c29"] += len(c29); tot["rework"] += len(rw)
    tot["tags"] += len(cc.TAG.findall(t)); tot["gaps"] += t.count("RESEARCH-GAP")
    print(f"{j}: tags {len(cc.TAG.findall(t))} bad {len(bad)} multi-period {len(single)} unbound {len(unb)} C29 {len(c29)} rework {len(rw)} gaps {t.count('RESEARCH-GAP')}")
    for x in bad + unb + rw:
        print("   ", x)
    if "-v" in sys.argv:
        for x in single:
            print("    multi-period", x)
print(dict(tot))
