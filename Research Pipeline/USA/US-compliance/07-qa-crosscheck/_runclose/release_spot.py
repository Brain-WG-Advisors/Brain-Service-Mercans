import sys, re, docx, difflib, collections
from openpyxl import load_workbook
sys.stdout.reconfigure(encoding="utf-8")
TAG = re.compile(r"\[\[FACT:[^=\]]+=([^\]]*)\]\]")
def norm(s): return re.sub(r"\s+", " ", TAG.sub(r"\1", s or "")).strip()
def xl(p):
    wb = load_workbook(p, read_only=True); return {f"{ws.title}!{c.coordinate}": str(c.value) for ws in wb.worksheets for r in ws.iter_rows() for c in r if c.value is not None}
def dc(p):
    d = docx.Document(p); return [x.text for x in d.paragraphs] + [" | ".join(c.text for c in r.cells) for t in d.tables for r in t.rows]
for src, rel in [("02-wtc/US-WTC-001-v1.0.xlsx", None), ("04-reports-spec/US-UI-001-StateUIWageReports-Spec.xlsx", None), ("03-statutory-integrations/US-SIR-INDEX-001-v1.0.docx", None)]:
    rel = "10-release/" + src
    if src.endswith(".xlsx"):
        A, B = xl(src), xl(rel)
        diff = [(k, norm(A.get(k)), B.get(k)) for k in sorted(set(A) | set(B)) if norm(A.get(k, "")) != (B.get(k) or "").strip()]
        kinds = collections.Counter(k.split("!")[0] for k, *_ in diff)
        print("==", src, "cells", len(A), "->", len(B), "| differing after tag-normalise:", len(diff), dict(kinds.most_common(5)))
        for k, a, b in diff[:6]: print("   ", k, "|", a[:110], "->", (b or "")[:110])
    else:
        a = [norm(x) for x in dc(src)]; b = [re.sub(r"\s+", " ", x).strip() for x in dc(rel)]
        d = [l for l in difflib.unified_diff(a, b, lineterm="", n=0) if l[:1] in "+-" and l[:3] not in ("+++", "---")]
        print("==", src, "lines", len(a), "->", len(b), "| differing after tag-normalise:", len(d))
        for l in d[:8]: print("   ", l[:200])
