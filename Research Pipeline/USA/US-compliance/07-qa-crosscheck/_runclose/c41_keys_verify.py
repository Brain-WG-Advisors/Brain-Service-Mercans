import csv, os, re, sys
sys.stdout.reconfigure(encoding="utf-8")
reg = {r["id"]: r for r in csv.DictReader(open("00-official-sources/legal-basis-register.csv", encoding="utf-8"))}
def text(p):
    if p.lower().endswith(".pdf"):
        from pypdf import PdfReader
        return " ".join((pg.extract_text() or "") for pg in PdfReader(p).pages)
    return open(p, encoding="utf-8", errors="ignore").read()
checks = {"US-FEDS6-009": ["1.2", "4.5", "California", "Virgin Islands"], "US-MEP52-002": ["941ME"], "US-NJR3-004": ["M-5008-R", "6/26"],
          "US-DCP51-014": ["D-2848"], "US-TXP52-008": ["C-42"], "US-FEDS5-031": ["February 2, 2026", "February 10"]}
for rid, toks in checks.items():
    r = reg[rid]; lf = [x.strip() for x in r["local_file"].split(";") if x.strip()]
    found = {}
    for p in lf:
        if os.path.exists(p):
            t = re.sub(r"\s+", " ", text(p)); found = {k: (k in t) for k in toks}; break
    print(rid, r["status"], r["effective_from"], found or ("no local file " + r["local_file"][:60]))
