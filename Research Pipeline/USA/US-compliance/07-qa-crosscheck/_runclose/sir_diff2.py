import re, sys, docx, difflib
sys.stdout.reconfigure(encoding="utf-8")
def dl(p):
    d = docx.Document(p); o = [x.text for x in d.paragraphs]
    for t in d.tables:
        for r in t.rows: o.append(" | ".join(c.text for c in r.cells))
    return [re.sub(r"SIR-RQ-\d+", "SIR-RQ-n", x) for x in o]
a = dl("_pipeline/_backup/pre-f27-2026-11-04/sir/US-SIR-INDEX-001-v1.0.docx"); b = dl("03-statutory-integrations/US-SIR-INDEX-001-v1.0.docx")
d = [l for l in difflib.unified_diff(a, b, lineterm="", n=0) if l[:1] in "+-" and l[:3] not in ("+++", "---")]
print("changes after masking SIR-RQ ids:", len(d))
for l in d: print(l[:400])
