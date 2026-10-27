# -*- coding: utf-8 -*-
"""Conferência da v1.2 contra a base, célula a célula e parte a parte.
Uso: python -I compare_v12.py <base.xlsx> <v1.2.xlsx> <log.md>
Falha (exit 1) se qualquer diferença estiver fora da lista EDITS."""
import datetime, os, re, sys, zipfile, xml.etree.ElementTree as ET
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from edits_v12 import EDITS, SHEET_NAME
import openpyxl, warnings
warnings.filterwarnings("ignore")

base, new, logp = sys.argv[1:4]
L, fails = [], []
def log(s=""): L.append(s)
def fail(s): fails.append(s); log("**FALHA** " + s)

expected = {(SHEET_NAME[p], c): (k, v) for p, c, k, v, _ in EDITS}
assert len(expected) == len(EDITS), "célula repetida na lista"

# ---- 1. partes do zip ----
za, zb = zipfile.ZipFile(base), zipfile.ZipFile(new)
na, nb = [i.filename for i in za.infolist()], [i.filename for i in zb.infolist()]
log("## 1. Partes do pacote")
if na != nb: fail("lista/ordem de partes diferente")
modified = {"xl/styles.xml", "xl/worksheets/sheet1.xml", "xl/worksheets/sheet2.xml", "xl/worksheets/sheet3.xml"}
for n in na:
    same = za.read(n) == zb.read(n)
    if n in modified:
        log("- `%s`: alterada (esperado)" % n)
    elif not same:
        fail("parte %s mudou sem estar na lista" % n)
log("- %d partes; %d idênticas byte a byte; %d alteradas (só as 4 esperadas)" % (
    len(na), sum(za.read(n) == zb.read(n) for n in na), sum(za.read(n) != zb.read(n) for n in na)))

# ---- 2. XML: tirando as células editadas, o resto é idêntico ----
log("\n## 2. XML das folhas sem as células editadas")
for p in sorted({p for p, *_ in EDITS}):
    xa, xb = za.read(p).decode("utf-8"), zb.read(p).decode("utf-8")
    for _p, c, *_ in [e for e in EDITS if e[0] == p]:
        pat = r'<c r="%s"[^>]*?(?:/>|>.*?</c>)' % c
        xa = re.sub(pat, "<CELL %s/>" % c, xa, count=1, flags=re.S)
        xb = re.sub(pat, "<CELL %s/>" % c, xb, count=1, flags=re.S)
    if xa == xb: log("- `%s`: idêntico fora das %d células editadas" % (p, sum(1 for e in EDITS if e[0] == p)))
    else: fail("%s difere fora das células editadas" % p)
sa, sb = za.read("xl/styles.xml").decode(), zb.read("xl/styles.xml").decode()
fa = re.search(r'<fills count="\d+">(.*?)</fills>', sa, re.S).group(1)
fb = re.search(r'<fills count="\d+">(.*?)</fills>', sb, re.S).group(1)
xa_ = re.search(r'<cellXfs count="\d+">(.*?)</cellXfs>', sa, re.S).group(1)
xb_ = re.search(r'<cellXfs count="\d+">(.*?)</cellXfs>', sb, re.S).group(1)
ok_st = fb.startswith(fa) and xb_.startswith(xa_) and "DDEBF7" in fb[len(fa):]
rest_a = re.sub(r'<fills.*?</fills>|<cellXfs.*?</cellXfs>', "", sa, flags=re.S)
rest_b = re.sub(r'<fills.*?</fills>|<cellXfs.*?</cellXfs>', "", sb, flags=re.S)
if ok_st and rest_a == rest_b: log("- `xl/styles.xml`: só acrescentou 1 fill (FFDDEBF7) e os xf clonados no fim; resto idêntico")
else: fail("styles.xml com mudança fora do acréscimo")

# ---- 3. XML bem formado ----
log("\n## 3. XML bem formado")
for n in nb:
    if n.endswith(".xml") or n.endswith(".rels"):
        try: ET.fromstring(zb.read(n))
        except ET.ParseError as e: fail("XML inválido %s: %s" % (n, e))
log("- todas as partes .xml/.rels da v1.2 passam no parser")

# ---- 4. célula a célula (valor + estilo) ----
log("\n## 4. Célula a célula (valor, preenchimento, fonte, borda, alinhamento, formato)")
wa, wb_ = openpyxl.load_workbook(base), openpyxl.load_workbook(new)
if wa.sheetnames != wb_.sheetnames: fail("abas diferentes")
def sty(c):
    f = c.fill
    return (f.fill_type, f.fgColor.rgb if f.fgColor is not None else None, c.font.name, c.font.sz, c.font.b,
            repr(c.border), repr(c.alignment), c.number_format)
diffs = {}
for ws in wa.worksheets:
    w2 = wb_[ws.title]
    R, C = max(ws.max_row, w2.max_row), max(ws.max_column, w2.max_column)
    n_cells = 0
    for r in range(1, R + 1):
        for c in range(1, C + 1):
            a, b = ws.cell(r, c), w2.cell(r, c)
            n_cells += 1
            if a.value != b.value or sty(a) != sty(b):
                diffs[(ws.title, a.coordinate)] = (a, b)
    log("- `%s`: %d células comparadas" % (ws.title, n_cells))
unexpected = sorted(set(diffs) - set(expected))
missing = sorted(set(expected) - set(diffs))
for k in unexpected: fail("diferença fora da lista: %s!%s" % k)
for k in missing: fail("edição não aplicada: %s!%s" % k)
for k, (kind, val) in expected.items():
    if k not in diffs: continue
    a, b = diffs[k]
    want = val
    if kind == "date": want = datetime.datetime(val.year, val.month, val.day)
    if b.value != want: fail("%s!%s valor %r != %r" % (k[0], k[1], b.value, want))
    if b.fill.fgColor.rgb != "FFDDEBF7" or b.fill.fill_type != "solid": fail("%s!%s sem azul" % k)
    sa_, sb_ = sty(a), sty(b)
    if sa_[2:] != sb_[2:]: fail("%s!%s fonte/borda/alinhamento/formato mudou" % k)
b23 = [d for d in diffs if d == ("Report Matrix", "B23")]
if b23:
    a, b = diffs[("Report Matrix", "B23")]
    if not b.value.startswith(a.value.replace("ASCII or BIG5", "ASCII and BIG5")): fail("B23 não preserva o texto antigo")
    else: log("- Report Matrix!B23: itens 1, 2 e 4 preservados; item 3 "or" → "and" (rodada 2); itens 5 e 6 acrescentados")
t1 = [(ws.cell(r, 1).value) for ws in [wa["Testing"]] for r in range(1, 15)]
t2 = [(ws.cell(r, 1).value) for ws in [wb_["Testing"]] for r in range(1, 15)]
log("- aba Testing intocada: %s" % ("sim" if t1 == t2 and za.read("xl/worksheets/sheet4.xml") == zb.read("xl/worksheets/sheet4.xml") else "NÃO"))

log("\n## 5. Diferenças encontradas (todas devem estar na lista)")
log("| Aba | Célula | Antes | Depois |\n|---|---|---|---|")
def short(v):
    s = "" if v is None else str(v)
    s = s.replace("\n", " / ").replace("|", "\\|")
    return s if len(s) <= 160 else s[:157] + "..."
for k in sorted(diffs, key=lambda k: (wa.sheetnames.index(k[0]), k[1][0], int(re.sub(r"\D", "", k[1])))):
    a, b = diffs[k]
    log("| %s | %s | %s | %s |" % (k[0], k[1], short(a.value), short(b.value)))
per = {}
for k in diffs: per[k[0]] = per.get(k[0], 0) + 1
log("\nPor aba: " + ", ".join("%s = %d" % (s, per.get(s, 0)) for s in wa.sheetnames))
log("Total de células diferentes: %d | esperadas: %d | fora da lista: %d | não aplicadas: %d" % (
    len(diffs), len(expected), len(unexpected), len(missing)))
log("\n**Resultado: %s**" % ("PASS (nenhuma diferença fora do escopo)" if not fails else "FAIL (%d)" % len(fails)))
hdr = "# Log de comparação célula a célula: SR-108 SNHI v1.1 → v1.2\n\nBase: `%s`\nNova: `%s`\nGerado: %s\n\n" % (
    base, os.path.basename(new), datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
open(logp, "w", encoding="utf-8").write(hdr + "\n".join(L) + "\n")
print("PASS" if not fails else "FAIL", len(diffs), per)
sys.exit(1 if fails else 0)
