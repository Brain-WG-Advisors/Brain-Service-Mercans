# -*- coding: utf-8 -*-
"""Conferencia v2.1 x v2.2 celula a celula + validacao XML.
Uso: python -I compare_v21_v22.py <v2.1.xlsx> <v2.2.xlsx> <changes_manifest.json> <log.txt>
Lista TODAS as diferencas (valor, formula, preenchimento) e confere cada uma contra o
manifesto de mudancas C1..C11. Qualquer diferenca fora do manifesto = FALHA.
"""
import json, re, sys, zipfile
import xml.dom.minidom
from collections import Counter
import openpyxl

A, B, MAN, LOG = sys.argv[1:5]
out = []
p = out.append
man = json.load(open(MAN, encoding="utf-8"))
exp = {(c["sheet"], c["cell"]): c for c in man["changes"]}
fails = 0

# 1) XML bem-formado em todas as partes + partes inalteradas identicas
za, zb = zipfile.ZipFile(A), zipfile.ZipFile(B)
p("== 1. Partes do pacote ==")
for n in zb.namelist():
    data = zb.read(n)
    if n.endswith(".xml") or n.endswith(".rels"):
        try: xml.dom.minidom.parseString(data)
        except Exception as e:
            fails += 1; p("XML INVALIDO: %s %s" % (n, e))
    if n in za.namelist():
        p("%-40s %s" % (n, "identica" if za.read(n) == data else "ALTERADA"))
    else:
        p("%-40s NOVA" % n)
missing = set(za.namelist()) - set(zb.namelist())
if missing: fails += 1; p("PARTES PERDIDAS: %s" % missing)
p("zip testzip: %s" % zb.testzip())

# 2) celula a celula (valores com formula crua + cor de preenchimento)
wa = openpyxl.load_workbook(A); wbk = openpyxl.load_workbook(B)
def fill(c):
    f = c.fill
    return f.fgColor.rgb if f is not None and f.fill_type == "solid" else None
p("\n== 2. Abas ==")
p("v2.1: %s" % wa.sheetnames); p("v2.2: %s" % wbk.sheetnames)
diffs = []
for name in wbk.sheetnames:
    sb = wbk[name]; sa = wa[name] if name in wa.sheetnames else None
    cells = set()
    for ws in (sa, sb):
        if ws is None: continue
        for row in ws.iter_rows():
            for c in row:
                if c.value is not None or fill(c) is not None: cells.add(c.coordinate)
    for ref in cells:
        va = sa[ref].value if sa else None; vb = sb[ref].value
        fa = fill(sa[ref]) if sa else None; fb = fill(sb[ref])
        if va != vb or fa != fb:
            diffs.append((name, ref, va, vb, fa, fb))
diffs.sort(key=lambda d: (wbk.sheetnames.index(d[0]), openpyxl.utils.cell.coordinate_to_tuple(d[1])))

p("\n== 3. Todas as diferencas (aba | celula | mudanca | antes -> depois | preenchimento) ==")
seen = set(); per_sheet = Counter(); per_change = Counter()
for name, ref, va, vb, fa, fb in diffs:
    key = (name, ref); m = exp.get(key)
    if m is None:
        fails += 1; tag = "FORA DO MANIFESTO"
    else:
        tag = m["change"]; seen.add(key)
        if (m["new"] or None) != (vb or None):
            fails += 1; tag += " [VALOR DIFERE DO MANIFESTO]"
    if vb not in (None, "") and fb != "FFDDEBF7":
        fails += 1; tag += " [SEM DESTAQUE AZUL]"
    per_sheet[name] += 1; per_change[tag.split(" ")[0]] += 1
    p("%s | %s | %s\n   ANTES : %r\n   DEPOIS: %r\n   fill  : %s -> %s" % (name, ref, tag, va, vb, fa, fb))
for key in exp:
    if key not in seen:
        fails += 1; p("MANIFESTO SEM DIFERENCA: %s" % (key,))

p("\n== 4. Contagem ==")
for k, v in per_sheet.items(): p("aba %-22s %d celulas" % (k, v))
for k, v in sorted(per_change.items()): p("mudanca %-10s %d celulas" % (k, v))
p("total de celulas diferentes: %d" % len(diffs))

# 5) varreduras de conteudo
p("\n== 5. Varreduras ==")
bad = ["Employer.Denomination", "Employer.RegisteredAddress", "Employer.CNASPayingCentre",
       "Employee.SocialSecurityNumber", "Payroll.ContributoryBase", "Working Hours"]
for name in wbk.sheetnames:
    for row in wbk[name].iter_rows():
        for c in row:
            v = c.value
            if isinstance(v, str):
                if v.startswith("="):
                    fails += 1; p("FORMULA/'=' em %s!%s: %r" % (name, c.coordinate, v[:60]))
                for b in bad:
                    if b in v and "never 'Working Hours'" not in v and "never \"Working Hours\"" not in v:
                        p("ATENCAO: '%s' em %s!%s" % (b, name, c.coordinate))
                if re.search(r"31 January|2% per month|2%/month", v):
                    p("NOTA: '31 January'/'2%%' em %s!%s (%s)" % (name, c.coordinate, "historico Change Log - mantido" if name == "Change Log vs Pipeline" else "VERIFICAR"))
# dados pessoais: nenhuma celula da aba Henkel pode ter 12 digitos (nº segurado)
for row in wbk["Henkel Configuration"].iter_rows():
    for c in row:
        if isinstance(c.value, str) and re.search(r"\b\d{12}\b", c.value):
            fails += 1; p("POSSIVEL Nº DE SEGURADO em Henkel!%s" % c.coordinate)
p("\nRESULTADO: %s (%d falhas)" % ("OK" if fails == 0 else "FALHA", fails))
open(LOG, "w", encoding="utf-8").write("\n".join(out) + "\n")
print("\n".join(out[-40:]))
