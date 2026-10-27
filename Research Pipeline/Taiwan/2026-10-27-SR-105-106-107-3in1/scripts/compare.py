"""Cell-by-cell comparison base x v1.1 + zip-part integrity.
Usage: compare.py <base.xlsx> <new.xlsx> <edits.json> <out.md>
Exit 1 if any difference is outside the declared edit list, or a changed cell lacks the FFDDEBF7 fill,
or an untouched zip part changed."""
import json
import sys
import zipfile
import warnings

import openpyxl

warnings.filterwarnings("ignore")
BLUE = "FFDDEBF7"


def show(v):
    if v is None:
        return "(vazio)"
    s = str(v).replace("\n", " / ").replace("|", "¦")
    return s


def main(base, new, edits_json, out):
    ed = json.load(open(edits_json, encoding="utf-8"))
    declared = {(e["sheet"], e["cell"]) for e in ed["edits"]}
    removed_sheets = {e["sheet"] for e in ed["edits"] if e["cell"] == "*"}
    wa = openpyxl.load_workbook(base)
    wb = openpyxl.load_workbook(new)
    diffs, problems, noop = [], [], []
    for ws in wa.worksheets:
        if ws.title not in wb.sheetnames:
            diffs.append((ws.title, "*", "aba existente", "ABA REMOVIDA", ""))
            if ws.title not in removed_sheets:
                problems.append("aba removida sem declaração: " + ws.title)
            continue
        wn = wb[ws.title]
        coords = set()
        for w in (ws, wn):
            for row in w.iter_rows():
                for c in row:
                    if c.value is not None:
                        coords.add(c.coordinate)
        for co in coords:
            a, n = ws[co].value, wn[co].value
            if a != n:
                fill = wn[co].fill.fgColor.rgb if wn[co].fill and wn[co].fill.fgColor is not None else None
                diffs.append((ws.title, co, a, n, fill))
                if (ws.title, co) not in declared:
                    problems.append("DIFERENÇA FORA DA LISTA: %s!%s" % (ws.title, co))
                if fill != BLUE:
                    problems.append("célula alterada sem azul: %s!%s (%s)" % (ws.title, co, fill))
    for wsn in wb.sheetnames:
        if wsn not in wa.sheetnames:
            problems.append("aba nova inesperada: " + wsn)
    dset = {(d[0], d[1]) for d in diffs}
    for s, c in sorted(declared):
        if c != "*" and (s, c) not in dset:
            noop.append("%s!%s" % (s, c))
    # blue cells must all be declared
    for wsn in wb.sheetnames:
        for row in wb[wsn].iter_rows():
            for c in row:
                f = c.fill.fgColor.rgb if c.fill and c.fill.fgColor is not None else None
                if f == BLUE and (wsn, c.coordinate) not in declared:
                    if not (wsn in wa.sheetnames and wa[wsn][c.coordinate].fill.fgColor.rgb == BLUE):
                        problems.append("azul em célula não declarada: %s!%s" % (wsn, c.coordinate))
    # zip parts
    za, zb = zipfile.ZipFile(base), zipfile.ZipFile(new)
    na, nb = za.namelist(), zb.namelist()
    mod = set(ed["modified_parts"]); rem = set(ed["removed_parts"])
    parts_same, parts_mod = 0, []
    for p in na:
        if p in rem:
            if p in nb:
                problems.append("parte removida ainda presente: " + p)
            continue
        if p not in nb:
            problems.append("parte sumiu: " + p)
            continue
        same = za.read(p) == zb.read(p)
        if p in mod:
            parts_mod.append(p + (" (igual)" if same else ""))
        elif same:
            parts_same += 1
        else:
            problems.append("parte não declarada mudou: " + p)
    extra = [p for p in nb if p not in na]
    if extra:
        problems.append("partes novas: %s" % extra)

    with open(out, "w", encoding="utf-8") as f:
        f.write("# Comparação célula a célula\n\n- Base: `%s`\n- Nova: `%s`\n\n" % (base, new))
        f.write("- Células com diferença: **%d** (declaradas: %d; sem efeito: %d)\n" % (
            len([d for d in diffs if d[1] != "*"]), len([d for d in declared if d[1] != "*"]), len(noop)))
        f.write("- Abas removidas: %s\n" % (", ".join(d[0] for d in diffs if d[1] == "*") or "nenhuma"))
        f.write("- Partes do zip idênticas (bytes descomprimidos): %d; alteradas (declaradas): %s; removidas: %s\n"
                % (parts_same, ", ".join(parts_mod), ", ".join(sorted(rem)) or "nenhuma"))
        f.write("- Problemas: **%d**\n\n" % len(problems))
        for p in problems:
            f.write("  - ⚠️ %s\n" % p)
        if noop:
            f.write("\nEdições sem efeito (valor já era igual): %s\n" % ", ".join(noop))
        f.write("\n| # | Aba | Célula | Antes | Depois | Preenchimento |\n|---|---|---|---|---|---|\n")
        def key(d):
            import re
            m = re.match(r"([A-Z]+)(\d+)", d[1]) if d[1] != "*" else None
            return (d[0], int(m.group(2)) if m else 0, m.group(1) if m else "")
        for i, d in enumerate(sorted(diffs, key=key), 1):
            f.write("| %d | %s | %s | %s | %s | %s |\n" % (i, d[0], d[1], show(d[2]), show(d[3]), d[4] or ""))
    print("diffs=%d problems=%d noop=%d parts_same=%d" % (len(diffs), len(problems), len(noop), parts_same))
    for p in problems:
        print("  PROBLEM:", p)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:5]))
