import docx, difflib, sys, os, hashlib
sys.stdout.reconfigure(encoding="utf-8")
BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
def lines(p):
    d = docx.Document(p); out = [x.text for x in d.paragraphs]
    for t in d.tables:
        for r in t.rows:
            out.append(" | ".join(c.text for c in r.cells))
    return out
a = os.path.join(BASE, "_pipeline", "_backup", "pre-m13-2026-11-04", "US-CCG-001-v1.0.docx")
b = os.path.join(BASE, "01-ccg", "US-CCG-001-v1.0.docx")
print("before", hashlib.md5(open(a,"rb").read()).hexdigest(), "after", hashlib.md5(open(b,"rb").read()).hexdigest())
diff = [l for l in difflib.unified_diff(lines(a), lines(b), lineterm="", n=0) if l[:1] in "+-" and not l.startswith(("+++", "---"))]
print("changed lines", len(diff))
for l in diff: print(l[:330])
