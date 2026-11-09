"""Run the pipeline's own C46 logic over the annex markdown files (deliverables() only reads DOCX/XLSX,
so this applies the same functions to the module markdown that will be assembled into the DOCX)."""
import sys, os, glob, json, re
sys.path.insert(0, os.path.expanduser("~/mercans-pipeline/shared/consistency-checks"))
import consistency_checks as CC
BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
facts = {}
multi = {}
for fp in glob.glob(os.path.join(BASE, "_research", "*-facts.json")):
    for f in json.load(open(fp, encoding="utf-8")).get("facts", []):
        facts[f["key"]] = f.get("value")
        multi.setdefault(f["key"], set()).add(json.dumps(f.get("value")))
forms = {}
for k, v in facts.items():
    for n, pct in CC.distinctive_forms(k, v):
        forms.setdefault((round(n, 6), pct), set()).add(k)
allvals = {}
for fp in glob.glob(os.path.join(BASE, "_research", "*-facts.json")):
    for f in json.load(open(fp, encoding="utf-8")).get("facts", []):
        allvals.setdefault(f["key"], []).append(f.get("value"))
units = sys.argv[1:] or ["FED", "MULTI", "AK", "AL", "AR", "AZ", "CA", "CO", "CT"]
tot_tags = tot_unb = tot_bad = tot_badmulti = 0
for u in units:
    p = os.path.join(BASE, "01-ccg", "annexes", f"annex_{u}.md")
    tags = unbound = bad = badm = 0
    for i, t in enumerate(open(p, encoding="utf-8").read().splitlines(), 1):
        for m in CC.TAG.finditer(t):
            tags += 1
            k, v = m.group(1), m.group(2)
            if k not in facts:
                bad += 1; print(u, i, "UNKNOWN KEY", k); continue
            a = CC._num(v)
            ok_any = any((CC._num(x) is not None and a is not None and abs(a - CC._num(x)) < 1e-9) or str(x).strip() == v.strip()
                         or str(x).replace("]", ")").replace("[", "(").strip() == v.strip() for x in allvals[k])
            if not ok_any:
                bad += 1; print(u, i, "VALUE MISMATCH", k, v[:60])
            else:
                b = CC._num(facts[k])
                same = (abs(a - b) < 1e-9) if (a is not None and b is not None) else (str(v).strip() == str(facts[k]).strip())
                if not same:
                    badm += 1
        bare = CC.TAG.sub(" ", t)
        for m in CC.NUM_IN_TEXT.finditer(bare):
            n = CC._num(m.group(1))
            if n is None:
                continue
            ks = forms.get((round(n, 6), bool(m.group(2))))
            if ks:
                unbound += 1
                print(u, i, "UNBOUND", m.group(0).strip(), sorted(ks)[:3], "::", bare[max(0, m.start()-60):m.end()+20].replace("\n", " "))
    print(f"== {u}: tags {tags}, unbound {unbound}, mismatch {bad}, multi-value-key tags C46 would misread {badm}")
    tot_tags += tags; tot_unb += unbound; tot_bad += bad; tot_badmulti += badm
print(f"TOTAL tags {tot_tags} unbound {tot_unb} mismatch {tot_bad} multi-value {tot_badmulti}")
