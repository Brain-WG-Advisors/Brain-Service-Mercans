# -*- coding: utf-8 -*-
"""Regex lint of the printed fact notes: round / history / retrieval wording must not appear in any deliverable.
usage: python note_vocab_lint.py   (BASE = US-compliance); exit 1 on a hit."""
import glob, os, re, sys
import docx
from openpyxl import load_workbook
BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
RX = re.compile(r"\bR\d 20\d\d|effective_from|local copy|script shell|journal|orchestrator|agent 2|triage|precheck|(?:returned|HTTP)[^.]{0,40}\bbytes\b", re.I)
hits = []
def scan(label, text):
    text = re.sub(r"\[\[(?:FACT|GAP):[^\]]*\]\]", " ", text or "")   # key names inside tags are not prose
    m = RX.search(text)
    if m:
        hits.append((label, m.group(0), text[max(0, m.start() - 40):m.end() + 40].replace("\n", " ")))
for p in (glob.glob(os.path.join(BASE, "01-ccg", "*.docx")) + glob.glob(os.path.join(BASE, "03-statutory-integrations", "*.docx"))):
    d = docx.Document(p)
    for i, para in enumerate(d.paragraphs): scan(f"{os.path.basename(p)} para {i+1}", para.text)
    for ti, t in enumerate(d.tables):
        for ri, r in enumerate(t.rows):
            for c in r.cells: scan(f"{os.path.basename(p)} table {ti+1} r{ri+1}", c.text)
for p in glob.glob(os.path.join(BASE, "0[2459]-*", "*.xlsx")) + glob.glob(os.path.join(BASE, "04-reports-spec", "*.xlsx")):
    wb = load_workbook(p, read_only=True, data_only=True)
    for ws in wb.worksheets:
        for row in ws.iter_rows():
            for c in row:
                if isinstance(c.value, str): scan(f"{os.path.basename(p)}!{ws.title}!{c.coordinate}", c.value)
for p in glob.glob(os.path.join(BASE, "09-design", "*.md")):
    for i, ln in enumerate(open(p, encoding="utf-8").read().splitlines()): scan(f"{os.path.basename(p)} line {i+1}", ln)
print("note vocabulary hits:", len(hits))
for h in hits[:30]: print(h)
sys.exit(1 if hits else 0)
