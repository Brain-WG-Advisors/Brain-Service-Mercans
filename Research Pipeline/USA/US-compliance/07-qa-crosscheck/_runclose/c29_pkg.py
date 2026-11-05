# C29 residual-marker lint (v2.12 HARD patterns) over every deliverable incl. design .md and the skill.
import re, glob, os, sys, json, docx
from openpyxl import load_workbook
sys.stdout.reconfigure(encoding="utf-8")
BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
SK = os.path.join(BASE, "..", "skills-build", "payroll-compliance-united-states")
HARD_CS = [r'\bTODO\b', r'\bTBD\b', r'\bFIXME\b', r'\bVERIFY\s+No\b', r'RESEARCH-GAP', r'\?\?\?']
HARD_CI = [r'\[\s*placeholder\s*\]', r'\[\s*CHECK\s*\]', r'\[\s*\?\s*\]', r'to be confirmed', r'to be verified', r'lorem ipsum']
hits = []
def scan(t, loc):
    if not t: return
    t = str(t)
    for p in HARD_CS:
        if re.search(p, t): hits.append((loc, p, t[:120]))
    for p in HARD_CI:
        if re.search(p, t, re.I): hits.append((loc, p, t[:120]))
n = 0
for p in glob.glob(os.path.join(BASE, "0[13]-*", "*.docx")):
    d = docx.Document(p); n += 1
    for i, x in enumerate(d.paragraphs): scan(x.text, f"{os.path.basename(p)} p{i}")
    for ti, t in enumerate(d.tables):
        for ri, r in enumerate(t.rows):
            for c in r.cells: scan(c.text, f"{os.path.basename(p)} t{ti} r{ri}")
for p in glob.glob(os.path.join(BASE, "0[2456]-*", "*.xlsx")):
    wb = load_workbook(p, read_only=True); n += 1
    for ws in wb.worksheets:
        for row in ws.iter_rows():
            for c in row:
                if isinstance(c.value, str): scan(c.value, f"{os.path.basename(p)}!{ws.title}!{c.coordinate}")
for p in glob.glob(os.path.join(BASE, "09-design", "*.md")) + [os.path.join(BASE, "scope_manifest.json")] + glob.glob(os.path.join(SK, "**", "*.md"), recursive=True):
    if "_build" in p: continue
    n += 1
    for i, l in enumerate(open(p, encoding="utf-8").read().splitlines()): scan(l, f"{os.path.relpath(p, BASE)}:{i+1}")
print("files", n, "hits", len(hits))
for h in hits[:30]: print(h)
json.dump(hits, open(os.path.join(os.path.dirname(__file__), "out", "c29_pkg.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
