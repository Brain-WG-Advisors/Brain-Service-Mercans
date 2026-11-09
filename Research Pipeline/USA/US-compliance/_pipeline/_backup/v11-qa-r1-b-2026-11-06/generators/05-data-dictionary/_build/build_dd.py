# -*- coding: utf-8 -*-
"""Build the US Data Dictionary (stage 4) from the CZ template, the DD facts and the approved Report Specs.

Re-runnable: python build_dd.py   ->  05-data-dictionary/US-DD-001-v1.0.xlsx
                                      05-data-dictionary/_build/checks/rspec_dd_recon.csv
                                      _pipeline/DD-bindings.csv
The generator is the only source of the workbook: a correction goes into dd_defs.py, dd_rules.py or this file.
"""
import copy
import csv
import datetime as dt
import os
import re
import sys

from openpyxl import load_workbook
from openpyxl.styles import Alignment, Font, PatternFill

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import dd_common as D  # noqa: E402
import dd_defs as DEF  # noqa: E402
import dd_recon as RC  # noqa: E402
import dd_rules as RU  # noqa: E402

BLUE = "FFD9E1F2"
WHITE = "FFFFFFFF"
FONT = "Times New Roman"

ID_COLS = dict(country=1, name=3, label=5, desc=6, dtype=7, pre=8, ftype=9, fmt=10, om=11, notes=22)     # A..V
CF_COLS = dict(country=2, name=4, label=6, desc=7, dtype=8, pre=9, ftype=10, fmt=11, om=12, notes=23)     # B..W
ID_LAST, CF_LAST = 22, 23
COUNTRY_NAME = D.COUNTRY

TOOLTIP_FACT_ROLE = {}


def g(text):
    return D.clean(text)


def fill(color):
    return PatternFill("solid", fgColor=color)


def style_data_cell(c, color, wrap=True):
    c.fill = fill(color)
    c.font = Font(name=FONT, size=9)
    c.alignment = Alignment(vertical="top", wrap_text=wrap)


def clear_sheet(ws, first_row, last_col):
    """Remove every value below the header of a template sheet (rows of the precedent country)."""
    for row in ws.iter_rows(min_row=first_row, max_row=ws.max_row, max_col=max(last_col, ws.max_column)):
        for c in row:
            c.value = None
            c.fill = PatternFill(fill_type=None)
            c.font = Font(name=FONT, size=9)
            c.alignment = Alignment()
            c.border = copy.copy(ws["A1"].border)
    for r in list(ws.row_dimensions):
        if r >= first_row:
            ws.row_dimensions[r].height = None


def notes_for(e, usage):
    """Additional Notes cell: level, group, tagged sources with effective period, derived values, consumers, notes."""
    parts = [f"{e['lvl']}.", f"Group: {e['grp']}."]
    D.at(f"{'ID Information' if e['sheet'] == 'ID' else 'Country Fields'} / {e['name']} / Additional Notes")
    if e["facts"]:
        parts.append("Sources: " + "; ".join(D.src(k) for k in e["facts"]) + ".")
    if e["derived"]:
        parts.append("Derived values that are not stored here (computed by the report from the dates and inputs of this "
                     "dictionary): " + "; ".join(D.src(k) for k in e["derived"]) + ".")
    parts.append(RC.used_by_text(e["id"], usage))
    if e.get("fmt_from"):
        parts.append("Format notation (N numeric, AN alphanumeric, length in brackets) as in column J of the Report Specification.")
    if e["note"]:
        parts.append(e["note"])
    return g(" ".join(parts))


def fmt_text(e):
    f = RC.element_format(e)
    return g(f)


def cell_values(e, usage):
    label = e["label"] or e["name"]
    return dict(country=COUNTRY_NAME, name=g(e["name"]), label=g(label), desc=g(e["desc"]), dtype=e["dt"],
                pre=g(e["pre"]), ftype=e["ftype"], fmt=fmt_text(e), om=g(e["om"]), notes=notes_for(e, usage))


def write_row(ws, r, cols, vals, color, last_col, orange):
    for ci in range(1, last_col + 1):
        c = ws.cell(r, ci)
        style_data_cell(c, color)
    for k, ci in cols.items():
        v = vals.get(k)
        if v not in (None, ""):
            ws.cell(r, ci).value = v


# ------------------------------------------------------------------------------------------- build ---
def build(out_dir=None, sidecars=True):
    recs, usage = RC.compute(DEF.ELEMENTS)
    for e in DEF.ELEMENTS:
        e["_notes"] = None
    wb = load_workbook(D.TEMPLATE)
    # precedent leftovers: the table objects of the precedent country's ranges (stale over the new content) and the
    # review comments written on its data cells; the generic version-control guidance comments (B12:E12) stay
    for name in ("ID Information", "Country Fields", "Country Option Mappers"):
        for t in list(wb[name].tables):
            del wb[name].tables[t]
        for row in wb[name].iter_rows():
            for c in row:
                c.comment = None
    wb["Version Control"]["A1"].comment = None
    for dv in wb["Version Control"].data_validations.dataValidation:
        if "Released" in str(dv.formula1):
            dv.formula1 = '"In Progress,Under Review,Approved,Released,Issued,For QA,Superseded"'

    # ---- Version Control: one row (package version, issue date, "Issued") -------------------------
    ws = wb["Version Control"]
    ws["B9"].value = f"{COUNTRY_NAME} | {D.DD_REF}"
    rows = D.C.changelog_rows("DD", D.STATUS)
    if rows:   # v1.1: previous version row + this version with what changed, why and the source
        for r, (ver, eff, desc, st) in zip((13, 14), rows):
            ws[f"B{r}"].value = float(ver)
            ws[f"C{r}"].value = __import__("datetime").datetime.strptime(eff, "%Y-%m-%d")
            ws[f"D{r}"].value = ("Data Dictionary of the United States payroll package" if r == 13 else desc)
            ws[f"E{r}"].value = st
            ws[f"F{r}"].value = D.AUTHOR
    else:
        ws["B13"].value = float(D.PKG)
        ws["C13"].value = D.ISSUE
        ws["D13"].value = "Data Dictionary of the United States payroll package"
        ws["E13"].value = D.STATUS
        ws["F13"].value = D.AUTHOR
        for col in "BCDEF":
            ws[f"{col}14"].value = None

    # ---- Introduction: keep the table of contents, evaluate the numbering formulas -----------------
    ws = wb["Introduction"]
    for i, r in enumerate(range(11, 17), start=1):
        ws.cell(r, 2).value = float(i)

    # ---- ID Information ----------------------------------------------------------------------------
    ws = wb["ID Information"]
    hdr13 = {c.column: (c.value, copy.copy(c.fill), copy.copy(c.font), copy.copy(c.alignment)) for c in ws[13]}
    sec12 = copy.copy(ws["A12"].font)
    clear_sheet(ws, 5, ID_LAST)
    ee_ids = [e for e in DEF.ELEMENTS if e["sheet"] == "ID" and e["lvl"] == DEF.EE]
    er_ids = [e for e in DEF.ELEMENTS if e["sheet"] == "ID" and e["lvl"] == DEF.ER]
    r = 5
    n_id = 0
    for i, e in enumerate(ee_ids):
        write_row(ws, r, ID_COLS, cell_values(e, usage), BLUE if i % 2 == 0 else WHITE, ID_LAST, None)
        r += 1
        n_id += 1
    r += 1
    ws.cell(r, 1).value = "Country-Specific Legal Entity Fields"
    ws.cell(r, 1).font = sec12
    r += 1
    for ci, (v, f, fo, al) in hdr13.items():
        if ci <= ID_LAST:
            c = ws.cell(r, ci)
            c.value, c.fill, c.font, c.alignment = v, f, fo, al
    r += 1
    for i, e in enumerate(er_ids):
        write_row(ws, r, ID_COLS, cell_values(e, usage), BLUE if i % 2 == 0 else WHITE, ID_LAST, None)
        r += 1
        n_id += 1
    id_last_row = r - 1
    ws.auto_filter.ref = f"A4:V{id_last_row}"

    # ---- Country Fields -------------------------------------------------------------------------------
    ws = wb["Country Fields"]
    clear_sheet(ws, 5, 24)
    cf = [e for e in DEF.ELEMENTS if e["sheet"] == "CF"]
    r = 5
    for i, e in enumerate(cf):
        write_row(ws, r, CF_COLS, cell_values(e, usage), BLUE if i % 2 == 0 else WHITE, CF_LAST, None)
        r += 1
    cf_last_row = r - 1

    # ---- Country Option Mappers --------------------------------------------------------------------------
    ws = wb["Country Option Mappers"]
    hdr = {c.column: (c.value, copy.copy(c.fill), copy.copy(c.font), copy.copy(c.alignment)) for c in ws[4]}
    clear_sheet(ws, 5, 6)
    r = 5
    first = True
    mapper_row = {}
    used_mappers = {e["om"] for e in DEF.ELEMENTS if e["om"]}
    names = {m["name"] for m in RU.MAPPERS}
    missing = sorted(used_mappers - names)
    if missing:
        raise SystemExit(f"option mappers referenced but not defined: {missing}")
    unused = sorted(names - used_mappers)
    if unused:
        raise SystemExit(f"option mappers defined but not referenced: {unused}")
    for m in RU.MAPPERS:
        if not first:
            r += 1
            for ci, (v, f, fo, al) in hdr.items():
                if 2 <= ci <= 6:
                    c = ws.cell(r, ci)
                    c.value, c.fill, c.font, c.alignment = v, f, fo, al
            r += 1
        first = False
        mapper_row[m["name"]] = r
        D.at(f"Country Option Mappers / {m['name']}")
        for i, row in enumerate(m["rows"]):
            code, abbr, local, eng = row
            if m["kind"] == "w4":
                key = local                       # per-State fact key
                f = D.fact(key)
                local_txt = D.tag(key)
                eng = f"{D.STATE_NAMES[code]}: [{f['register_id']}] ({D.eff(key)})"
            else:
                local_txt = local
                if i == 0 and m["keys"]:
                    eng = (eng + (" " if eng.endswith(".") else ". ") if eng else "") + "Sources: " + \
                        "; ".join(D.src(k) for k in m["keys"]) + "."
                    if m["note"]:
                        eng += " " + m["note"]
                elif i == 0 and m["note"]:
                    eng = (eng + (" " if eng.endswith(".") else ". ") if eng else "") + m["note"]
            color = "FFD9E2F3"
            for ci in range(2, 7):
                c = ws.cell(r, ci)
                c.fill = fill(color)
                c.font = Font(name=FONT, size=9)
                c.alignment = Alignment(vertical="top", wrap_text=True)
            if i == 0:
                ws.cell(r, 2).value = g(m["name"])
            ws.cell(r, 3).value = g(code)
            ws.cell(r, 4).value = g(abbr)
            ws.cell(r, 5).value = g(local_txt)
            ws.cell(r, 6).value = g(eng)
            r += 1
    om_last_row = r - 1

    # ---- widths for the wrapped text columns (template widths kept elsewhere) ----------------------------------
    wsid, wscf = wb["ID Information"], wb["Country Fields"]
    for ws_, widths in ((wsid, {"F": 48, "H": 36, "J": 24, "K": 26, "V": 70}),
                        (wscf, {"G": 48, "I": 36, "K": 24, "L": 26, "W": 70, "D": 34, "F": 24})):
        for col, w in widths.items():
            ws_.column_dimensions[col].width = w
    wb["Country Option Mappers"].column_dimensions["E"].width = 44
    wb["Country Option Mappers"].column_dimensions["F"].width = 70

    out = os.path.join(out_dir or D.OUT, D.FILENAME)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    wb.save(out)

    # ---- sidecars -------------------------------------------------------------------------------------------------
    if sidecars:
        os.makedirs(D.CHECKS, exist_ok=True)
        RC.write_csv(recs, os.path.join(D.CHECKS, "rspec_dd_recon.csv"))
        RC.write_usage_csv(DEF.ELEMENTS, usage, os.path.join(D.CHECKS, "dd_element_usage.csv"))
        write_bindings()
        write_overlay(recs)
    return dict(out=out, id_rows=n_id, cf_rows=len(cf), id_last=id_last_row, cf_last=cf_last_row, om_last=om_last_row,
                recs=recs, usage=usage, mapper_row=mapper_row)


def write_overlay(recs):
    """Column L of the Report Spec rows that cite this dictionary, written with the exact DD Field Names (C27, F25).
    Read by the Report Spec generator (us_book.write); keyed by spec id and field position."""
    import json
    full = {(r["spec"], r["row"]): r["mapping"] for r in D.spec_rows()}
    out = {}
    for r in recs:
        key = f"{r['spec']}|{r['fid']}"
        if (r["spec"], r["fid"]) in RU.L_OVERRIDE:
            out[key] = RU.L_OVERRIDE[(r["spec"], r["fid"])]
            continue
        if r["status"] != "MAPPED":
            continue
        text = f"{D.DD_REF}: {r['dd_elements']}"
        orig = full[(r["spec"], r["row"])]
        _, _, rest = orig.partition(";")
        rest = rest.strip()
        if (r["spec"], r["fid"]) in RU.HOURS_MIXED:
            text += "; " + RU.HOURS_NOTE
        elif re.match(r"(payroll result|rate table)", rest):
            text += "; " + rest
        out[key] = text
    for k in RU.L_OVERRIDE:
        out.setdefault(f"{k[0]}|{k[1]}", RU.L_OVERRIDE[k])
    path = os.path.join(D.SPECS, "_build", "dd_l_overlay.json")
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(dict(sorted(out.items())), fh, indent=1, ensure_ascii=False)


def write_bindings():
    path = os.path.join(D.BASE, "_pipeline", "DD-bindings.csv")
    with open(path, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["location", "key", "register_id", "effective_from", "facts_file"])
        for key, locs in sorted(D.USED.items()):
            k = key.split("@")[0]
            f = D.fact(k)
            for loc in sorted(locs):
                w.writerow([loc, k, f["register_id"], f.get("effective_from"), f["_file"]])


if __name__ == "__main__":
    out_dir = sys.argv[sys.argv.index("--out") + 1] if "--out" in sys.argv else None
    res = build(out_dir, sidecars=out_dir is None)
    from collections import Counter
    c = Counter(r["status"] for r in res["recs"])
    print("written", res["out"])
    print("ID Information data rows:", res["id_rows"], "| Country Fields data rows:", res["cf_rows"],
          "| elements:", res["id_rows"] + res["cf_rows"], "| mapper last row:", res["om_last"])
    print("recon:", dict(c))
