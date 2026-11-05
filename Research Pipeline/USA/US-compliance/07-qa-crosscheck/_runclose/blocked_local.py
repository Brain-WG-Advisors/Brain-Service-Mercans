import csv, os, re, sys, glob
sys.stdout.reconfigure(encoding="utf-8")
BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
want = {"US-FEDB5-401": "192,300", "US-COB5-003": "0.44", "US-CAS5-005": "last four", "US-INS5-009": "2.95", "US-MAS5-012": "0.46",
        "US-FLS5-003": "7,000", "US-NCS5-011": "3.99", "US-KYS5-009": "3.5", "US-UTS5-001": "4.45", "US-MIPIT-001": "4.25",
        "US-COS5-012": "4.4", "US-FIL-002": "42-007", "US-TXP52-008": "C-42", "US-ORS5-015": "other state"}
rows = {r["id"]: r for r in csv.DictReader(open(os.path.join(BASE, "00-official-sources", "legal-basis-register.csv"), encoding="utf-8"))}
print(list(next(iter(rows.values())).keys())[:30])
for rid, tok in want.items():
    r = rows.get(rid, {})
    lf = r.get("local_file") or r.get("local_copy") or ""
    hit = "no local file"
    for cand in [p for p in re.split(r"[;|]", lf) if p.strip()]:
        p = os.path.join(BASE, cand.strip()) if not os.path.isabs(cand.strip()) else cand.strip()
        if os.path.exists(p):
            try:
                if p.lower().endswith(".pdf"):
                    from pypdf import PdfReader
                    t = " ".join((pg.extract_text() or "") for pg in PdfReader(p).pages[:40])
                else:
                    t = open(p, encoding="utf-8", errors="ignore").read()
                t = re.sub(r"\s+", " ", t)
                hit = ("FOUND" if tok.lower() in t.lower() else "not found") + f" in {os.path.basename(p)}"
            except Exception as e:
                hit = f"read error {e}"
            break
        else:
            hit = f"missing {cand.strip()[:80]}"
    print(rid, tok, "|", r.get("verified_on"), "|", hit)
