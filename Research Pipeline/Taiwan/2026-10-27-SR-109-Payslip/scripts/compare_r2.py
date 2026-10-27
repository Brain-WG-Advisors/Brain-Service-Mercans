# -*- coding: utf-8 -*-
"""Rodada 2: diff celula a celula v1.2 rodada 1 x v1.2 rodada 2.
python -I compare_r2.py <r1.xlsx> <r2.xlsx> <log.md>"""
import sys, hashlib, openpyxl
R1, R2, LOG = sys.argv[1:4]
ALLOWED = {("Spec", c) for c in "Q6 Q15 Q51 T22 T37 U14 H16 Q20 T47 T49".split()} | \
          {("Report Matrix", c) for c in "B17 A22 B22 A23 B23".split()} | \
          {("Version Control", c) for c in "B13 C13 D13 E13 F13 B14 C14 D14 F14 B15 C15 D15 E15 F15".split()}
HL = "FFDDEBF7"
def fill(c): return c.fill.fgColor.rgb if c.fill is not None and c.fill.fill_type == "solid" else None
a, b = openpyxl.load_workbook(R1), openpyxl.load_workbook(R2)
out = ["# Rodada 2: diff célula a célula (v1.2 rodada 1 × v1.2 rodada 2)", "",
       f"- r1 md5 {hashlib.md5(open(R1,'rb').read()).hexdigest()} · r2 md5 {hashlib.md5(open(R2,'rb').read()).hexdigest()}", "",
       "| Aba | Célula | Antes (r1) | Depois (r2) | Fill r2 | Status |", "|---|---|---|---|---|---|"]
fails = []; n = {}
assert a.sheetnames == b.sheetnames
for s in b.sheetnames:
    w0, w1 = a[s], b[s]
    for r in range(1, max(w0.max_row, w1.max_row) + 1):
        for c in range(1, max(w0.max_column, w1.max_column) + 1):
            x, y = w0.cell(r, c), w1.cell(r, c)
            if x.value == y.value and fill(x) == fill(y): continue
            ok = (s, y.coordinate) in ALLOWED and (fill(y) == HL or y.value is None)
            if not ok: fails.append(f"{s}!{y.coordinate}")
            n[s] = n.get(s, 0) + 1
            cut = lambda v: ("" if v is None else str(v)).replace("|", "/")[:160]
            out.append(f"| {s} | {y.coordinate} | {cut(x.value)} | {cut(y.value)} | {fill(y)} | {'ok' if ok else 'FORA DO ESCOPO'} |")
out += ["", f"- Células por aba: {n}; total {sum(n.values())}", "- **Nenhuma diferença fora do escopo da rodada 2.**" if not fails else "- FALHAS: " + ", ".join(fails)]
open(LOG, "w", encoding="utf-8").write("\n".join(out) + "\n")
print(n, fails)
