import csv, os, re, sys, json, glob
sys.stdout.reconfigure(encoding="utf-8")
BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
reg = {r["id"]: r for r in csv.DictReader(open(os.path.join(BASE, "00-official-sources", "legal-basis-register.csv"), encoding="utf-8"))}
facts = {}
for p in glob.glob(os.path.join(BASE, "_research", "CCG-*-facts.json")):
    for f in json.load(open(p, encoding="utf-8"))["facts"]:
        facts.setdefault(f["key"], f)
checks = {"practice.ga.rate_change_2026": ["4.99", "5.19", "0.125", "3.99"],
          "practice.sc.withholding_rates_2026": ["1.99", "6%"],
          "practice.ne.use_circular_en_tables": ["2.26", "4.60", "4.55"],
          "practice.oh.flat_rate_vs_tables": ["2.99", "3.4", "2.75"],
          "practice.ct.tables_vs_rules": ["withholding tables"],
          "ma.pfml.rate.selection_basis": ["January 1"]}
def text(path):
    if path.lower().endswith(".pdf"):
        from pypdf import PdfReader
        return " ".join((pg.extract_text() or "") for pg in PdfReader(path).pages)
    return open(path, encoding="utf-8", errors="ignore").read()
for k, toks in checks.items():
    f = facts.get(k, {})
    ids = [f.get("register_id")] + list(f.get("_also") or f.get("also_register_ids") or [])
    print(k, ids, "| value:", str(f.get("value"))[:200])
    for rid in [i for i in ids if i]:
        r = reg.get(rid, {}); lf = (r.get("local_file") or "").split(";")[0].strip()
        p = os.path.join(BASE, lf) if lf else ""
        if p and os.path.exists(p):
            t = re.sub(r"\s+", " ", text(p))
            print("  ", rid, os.path.basename(p), {x: (x in t) for x in toks})
        else:
            print("  ", rid, "no local file", lf[:80])
