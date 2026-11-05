# Text diff of every deliverable vs a backup folder (docx paragraphs+cells; xlsx cells; md lines).
import sys, os, glob, hashlib, difflib, docx
from openpyxl import load_workbook
sys.stdout.reconfigure(encoding="utf-8")
BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
BK = os.path.join(BASE, "_pipeline", "_backup", sys.argv[1])
md5 = lambda p: hashlib.md5(open(p, "rb").read()).hexdigest()
def dl(p):
    d = docx.Document(p); o = [x.text for x in d.paragraphs]
    for t in d.tables:
        for r in t.rows: o.append(" | ".join(c.text for c in r.cells))
    return o
def xl(p):
    wb = load_workbook(p, read_only=True); o = {}
    for ws in wb.worksheets:
        for row in ws.iter_rows():
            for c in row:
                if c.value is not None: o[f"{ws.title}!{c.coordinate}"] = str(c.value)
    return o
cur = {"ccg": "01-ccg", "sir": "03-statutory-integrations", "rspec": "04-reports-spec", "dd": "05-data-dictionary", "wtc": "02-wtc", "design": "09-design"}
for k, d in cur.items():
    for b in glob.glob(os.path.join(BK, k, "*.*")):
        c = os.path.join(BASE, d, os.path.basename(b))
        if not os.path.exists(c): print("MISSING", c); continue
        if md5(b) == md5(c): continue
        if b.endswith(".docx"):
            diff = [l for l in difflib.unified_diff(dl(b), dl(c), lineterm="", n=0) if l[:1] in "+-" and l[:3] not in ("+++", "---")]
        elif b.endswith(".xlsx"):
            A, B = xl(b), xl(c)
            diff = [f"{x}: {A.get(x,'')[:150]!r} -> {B.get(x,'')[:150]!r}" for x in sorted(set(A) | set(B)) if A.get(x) != B.get(x)]
        else:
            diff = [l for l in difflib.unified_diff(open(b, encoding="utf-8").read().splitlines(), open(c, encoding="utf-8").read().splitlines(), lineterm="", n=0) if l[:1] in "+-" and l[:3] not in ("+++", "---")]
        print(f"== {k}/{os.path.basename(b)}: {len(diff)} changes")
        for l in diff[:40]: print("   ", l[:300])
