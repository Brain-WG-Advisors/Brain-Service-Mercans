# md5 of every deliverable vs its md5_final (run-close, compliance-qa-auditor)
import hashlib, json, os, glob, sys
BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
SK = os.path.abspath(os.path.join(BASE, "..", "skills-build", "payroll-compliance-united-states"))
def md5(p): return hashlib.md5(open(p, "rb").read()).hexdigest()
res = {}
for art, f in [("WTC","02-wtc"),("SIR","03-statutory-integrations"),("RSPEC","04-reports-spec"),("DD","05-data-dictionary"),("PSL","06-payslip"),("DESIGN","09-design")]:
    lst = os.path.join(BASE, f, "_build", "checks", "md5_final.txt")
    ok, bad, missing = 0, [], []
    for ln in open(lst, encoding="utf-8").read().splitlines():
        ln = ln.strip()
        if not ln or ln.startswith("#"): continue
        h, p = ln.split(None, 1); p = p.lstrip("*").strip()
        q = os.path.join(BASE, p) if os.path.exists(os.path.join(BASE, p)) else os.path.join(BASE, f, p)
        if not os.path.exists(q): missing.append(p); continue
        (ok := ok + 1) if md5(q) == h else bad.append((p, h, md5(q)))
    res[art] = {"listed_ok": ok, "mismatch": bad, "missing": missing}
d = os.path.join(BASE, "01-ccg", "US-CCG-001-v1.0.docx"); res["CCG"] = {"current": md5(d)}
ok, bad, missing = 0, [], []
for ln in open(os.path.join(BASE, "_pipeline", "SKILL-md5.txt"), encoding="utf-8").read().splitlines():
    if not ln.strip(): continue
    h, p = ln.split(None, 1); q = os.path.join(SK, p.lstrip("*").strip())
    if not os.path.exists(q): missing.append(p); continue
    (ok := ok + 1) if md5(q) == h else bad.append((p, h, md5(q)))
res["SKILL"] = {"listed_ok": ok, "mismatch": bad, "missing": missing}
res["SCOPE"] = {"current": md5(os.path.join(BASE, "scope_manifest.json"))}
res["deliverables"] = {os.path.relpath(p, BASE).replace("\\","/"): md5(p) for p in
    glob.glob(os.path.join(BASE,"01-ccg","*.docx"))+glob.glob(os.path.join(BASE,"02-wtc","*.xlsx"))+glob.glob(os.path.join(BASE,"03-statutory-integrations","*.docx"))
    +glob.glob(os.path.join(BASE,"03-statutory-integrations","*.json"))+glob.glob(os.path.join(BASE,"04-reports-spec","*.xlsx"))+glob.glob(os.path.join(BASE,"05-data-dictionary","*.xlsx"))
    +glob.glob(os.path.join(BASE,"06-payslip","*.xlsx"))+glob.glob(os.path.join(BASE,"09-design","*.md"))+[os.path.join(BASE,"scope_manifest.json")]}
json.dump(res, open(os.path.join(os.path.dirname(__file__), "out", "md5.json"), "w"), indent=1)
for k, v in res.items():
    if k != "deliverables": print(k, {a: (len(b) if isinstance(b, list) else b) for a, b in v.items()})
