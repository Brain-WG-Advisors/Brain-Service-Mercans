# -*- coding: utf-8 -*-
"""Conferencia celula a celula base x v1.2 + validacao do pacote.
python -I compare_v12.py <base.xlsx> <v12.xlsx> <changes.json> <log.md>"""
import sys, json, zipfile, re, hashlib
import xml.etree.ElementTree as ET
import openpyxl
from openpyxl.utils import range_boundaries

BASE, NEW, CH, LOG = sys.argv[1:5]
HL = "FFDDEBF7"
changes = json.load(open(CH, encoding="utf-8"))
expected = {(s, r): t for s, r, t in changes}
out, fails = [], []

def P(x=""):
    out.append(x)

P("# Conferência célula a célula: TW Payslip Specification base (export 2026-10-27) × v1.2")
P("")
P(f"- Base: `{BASE}` md5 {hashlib.md5(open(BASE,'rb').read()).hexdigest()}")
P(f"- v1.2: `{NEW}` md5 {hashlib.md5(open(NEW,'rb').read()).hexdigest()}")
P("")

# 1. pacote: partes iguais byte a byte, XML bem formado
zb, zn = zipfile.ZipFile(BASE), zipfile.ZipFile(NEW)
nb, nn = set(zb.namelist()), set(zn.namelist())
P("## 1. Pacote (zip)")
P(f"- Partes só na v1.2: {sorted(nn-nb)}; só na base: {sorted(nb-nn)}")
same = [n for n in nb & nn if zb.read(n) == zn.read(n)]
diff = sorted(n for n in nb & nn if zb.read(n) != zn.read(n))
P(f"- Partes idênticas byte a byte: {len(same)}; alteradas: {diff}")
allowed = {"xl/worksheets/sheet1.xml", "xl/worksheets/sheet2.xml", "xl/styles.xml", "xl/workbook.xml", "xl/_rels/workbook.xml.rels", "[Content_Types].xml"}
if set(diff) - allowed or (nn - nb) != {"xl/worksheets/sheet4.xml"} or (nb - nn):
    fails.append("partes alteradas fora do esperado")
bad = []
for n in zn.namelist():
    if n.endswith(".xml") or n.endswith(".rels") or n.endswith(".vml"):
        try:
            ET.fromstring(zn.read(n))
        except ET.ParseError as e:
            if not n.endswith(".vml"):
                bad.append(f"{n}: {e}")
P(f"- XML bem formado: {'todos' if not bad else bad}")
if bad: fails.append("xml mal formado")
# integridade de referencias
ct = zn.read("[Content_Types].xml").decode()
rels = zn.read("xl/_rels/workbook.xml.rels").decode()
wbx = zn.read("xl/workbook.xml").decode()
for rid, tgt in re.findall(r'Id="(rId\d+)"[^>]*Target="([^"]+)"', rels):
    if "xl/" + tgt not in nn: fails.append(f"rel {rid} -> {tgt} inexistente")
for rid in re.findall(r'r:id="(rId\d+)"', wbx):
    if f'Id="{rid}"' not in rels: fails.append(f"workbook {rid} sem rel")
if '/xl/worksheets/sheet4.xml' not in ct: fails.append("sheet4 sem content type")
st = zn.read("xl/styles.xml").decode()
nx = len(re.findall(r'<xf ', re.search(r'<cellXfs[^>]*>(.*?)</cellXfs>', st, re.S).group(1)))
cnt = int(re.search(r'<cellXfs count="(\d+)"', st).group(1))
nf = len(re.findall(r'<fill>', re.search(r'<fills[^>]*>(.*?)</fills>', st, re.S).group(1)))
fcnt = int(re.search(r'<fills count="(\d+)"', st).group(1))
P(f"- styles: cellXfs {nx}/{cnt}, fills {nf}/{fcnt}")
if nx != cnt or nf != fcnt: fails.append("contagem de styles")
maxs = max(int(x) for p in nn if p.startswith("xl/worksheets/sheet") for x in re.findall(r' s="(\d+)"', zn.read(p).decode()))
P(f"- maior índice de estilo usado: {maxs} (< {cnt})")
if maxs >= cnt: fails.append("estilo fora do intervalo")
# merges: sem sobreposicao
sp = zn.read("xl/worksheets/sheet2.xml").decode()
mc = re.findall(r'<mergeCell ref="([A-Z0-9:]+)"/>', sp)
cells = {}
for m in mc:
    c1, r1, c2, r2 = range_boundaries(m)
    for r in range(r1, r2 + 1):
        for c in range(c1, c2 + 1):
            if (r, c) in cells: fails.append(f"merge sobreposto {m} x {cells[(r,c)]}")
            cells[(r, c)] = m
P(f"- mergeCells Spec: {len(mc)} (contagem declarada {re.search(r'<mergeCells count=.(\d+)', sp).group(1)}), sem sobreposição: {'sim' if not any('merge' in f for f in fails) else 'NÃO'}")
P("")

# 2. celula a celula
wb0 = openpyxl.load_workbook(BASE)
wb1 = openpyxl.load_workbook(NEW)
P("## 2. Célula a célula (valor e preenchimento)")
P(f"- Abas base: {wb0.sheetnames}; abas v1.2: {wb1.sheetnames}")
def fill(c):
    return c.fill.fgColor.rgb if c.fill is not None and c.fill.fill_type == "solid" else None
rows = []
count = {}
for name in wb1.sheetnames:
    w1 = wb1[name]
    w0 = wb0[name] if name in wb0.sheetnames else None
    maxr = max(w1.max_row, w0.max_row if w0 else 0)
    maxc = max(w1.max_column, w0.max_column if w0 else 0)
    for r in range(1, maxr + 1):
        for c in range(1, maxc + 1):
            c1 = w1.cell(r, c)
            v0 = w0.cell(r, c).value if w0 else None
            f0 = fill(w0.cell(r, c)) if w0 else None
            v1, f1 = c1.value, fill(c1)
            ref = c1.coordinate
            if v0 == v1 and f0 == f1:
                if (name, ref) in expected:
                    fails.append(f"{name}!{ref} esperado alterar e não mudou")
                continue
            exp = (name, ref) in expected
            okv = exp and (expected[(name, ref)] or None) == v1
            okf = f1 == HL
            status = "ok" if (exp and okv and okf) else "FORA DO ESCOPO" if not exp else "ERRO"
            if status != "ok": fails.append(f"{name}!{ref} {status} v0={v0!r} v1={v1!r} f0={f0} f1={f1}")
            count[name] = count.get(name, 0) + 1
            rows.append((name, ref, v0, v1, f1, status))
for (s, r), t in expected.items():
    if not any(x[0] == s and x[1] == r for x in rows):
        if t:  # celula vazia nova sem valor nao aparece como diferenca de valor
            fails.append(f"{s}!{r} esperado e não encontrado")
P(f"- Células diferentes por aba: {count}")
P(f"- Total: {len(rows)}; esperadas pelo script: {len(expected)}")
P("")
P("| Aba | Célula | Antes | Depois | Fill | Status |")
P("|---|---|---|---|---|---|")
def cut(v):
    s = "" if v is None else str(v).replace("|", "/").replace("\n", " ")
    return s if len(s) <= 140 else s[:137] + "..."
for name, ref, v0, v1, f1, stt in rows:
    P(f"| {name} | {ref} | {cut(v0)} | {cut(v1)} | {f1} | {stt} |")
P("")
P("## 3. Resultado")
P("- **Nenhuma diferença fora do escopo; pacote válido.**" if not fails else "- FALHAS:\n" + "\n".join("  - " + f for f in fails))
open(LOG, "w", encoding="utf-8").write("\n".join(out) + "\n")
print("fails:", len(fails)); print("\n".join(fails[:30])); print(count)
