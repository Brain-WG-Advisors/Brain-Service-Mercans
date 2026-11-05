# -*- coding: utf-8 -*-
"""Tag-sync check: every [[FACT:key=value]] of every deliverable equals a current value of that key (any period entry).
usage: python tag_sync_check.py [--json out.json]   (run from anywhere; BASE = parent of _pipeline)
Exit 1 when a tag text matches no current fact value (stale wording) or names an unknown key."""
import glob, json, os, re, sys
import docx
from openpyxl import load_workbook
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TAG = re.compile(r"\[\[FACT:([A-Za-z0-9_.]+)=([^\]]*)\]\]")
FACTS = {}
for p in glob.glob(os.path.join(BASE, "_research", "*-facts.json")):
    for f in json.load(open(p, encoding="utf-8"))["facts"]:
        FACTS.setdefault(f["key"], []).append(f.get("value"))
def norm(v):
    s = re.sub(r"\s+", " ", str(v)).strip()
    t = s.replace(",", "")
    try:
        return ("n", round(float(t), 9))
    except ValueError:
        return ("s", s)
ART = {"CCG": [os.path.join(BASE, "01-ccg", "*.docx")], "SIR": [os.path.join(BASE, "03-statutory-integrations", "*.docx")],
       "RSPEC": [os.path.join(BASE, "04-reports-spec", "*.xlsx")], "DD": [os.path.join(BASE, "05-data-dictionary", "*.xlsx")],
       "WTC": [os.path.join(BASE, "02-wtc", "*.xlsx")], "PSL": [os.path.join(BASE, "06-payslip", "*.xlsx")],
       "DESIGN": [os.path.join(BASE, "09-design", "*.md")]}
def texts(path):
    if path.endswith(".md"):
        for i, ln in enumerate(open(path, encoding="utf-8").read().splitlines()):
            yield f"line {i+1}", ln
    elif path.endswith(".docx"):
        d = docx.Document(path)
        for i, p in enumerate(d.paragraphs):
            yield f"para {i+1}", p.text
        for ti, t in enumerate(d.tables):
            for ri, r in enumerate(t.rows):
                seen = set()
                for ci, c in enumerate(r.cells):
                    if id(c._tc) not in seen:
                        seen.add(id(c._tc)); yield f"table {ti+1} r{ri+1}c{ci+1}", c.text
    else:
        wb = load_workbook(path, read_only=True, data_only=False)
        for ws in wb.worksheets:
            for row in ws.iter_rows():
                for c in row:
                    if isinstance(c.value, str):
                        yield f"{ws.title}!{c.coordinate}", c.value
res, bad = {}, []
for art, pats in ART.items():
    n = 0; b = []
    for pat in pats:
        for path in sorted(glob.glob(pat)):
            for loc, t in texts(path):
                for m in TAG.finditer(t):
                    n += 1
                    k, v = m.group(1), m.group(2)
                    if k not in FACTS:
                        b.append((os.path.basename(path), loc, k, "unknown key", v[:70])); continue
                    if norm(v) not in {norm(x) for x in FACTS[k]}:
                        b.append((os.path.basename(path), loc, k, "stale", v[:70]))
    res[art] = {"tags": n, "stale_or_unknown": len(b), "keys": sorted({x[2] for x in b})[:40]}
    bad += [(art,) + x for x in b]
print(json.dumps(res, indent=1))
for x in bad[:60]: print(x)
if "--json" in sys.argv:
    json.dump({"summary": res, "details": bad}, open(sys.argv[sys.argv.index("--json") + 1], "w", encoding="utf-8"), indent=1, ensure_ascii=False)
sys.exit(1 if bad else 0)
