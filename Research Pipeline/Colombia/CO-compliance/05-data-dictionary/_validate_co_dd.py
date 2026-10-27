# -*- coding: utf-8 -*-
"""
_validate_co_dd.py - mechanical gate for CO-DD-001-v1.0.xlsx.

Run: python _validate_co_dd.py
"""
import glob
import os
import re
import sys

from openpyxl import load_workbook

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from make_classification import classify  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
DD = os.path.join(HERE, "CO-DD-001-v1.0.xlsx")
TPL = os.path.join(HERE, "..", "..", "shared", "CZ_Data_Dictionary_V2_0.xlsx")
SPECS = os.path.join(HERE, "..", "04-reports-spec")

ID_ORANGE = [2, 4] + list(range(12, 22))
CF_ORANGE = [3, 5] + list(range(13, 23))
EXTERNAL_MAPPERS = {"ISO 3166-1 (see the 'Country Codes - ISO 3166-1' sheet)"}

results = []


def check(name, ok, detail=""):
    results.append((name, ok, detail))


def main():
    wb = load_workbook(DD)
    tpl = load_workbook(TPL)

    check("C1  sheet order and count match the CZ V2.0 template",
          wb.sheetnames == tpl.sheetnames, str(wb.sheetnames))

    same = all(
        [[c.value for c in r] for r in wb[s].iter_rows(min_row=1, max_row=60)]
        == [[c.value for c in r] for r in tpl[s].iter_rows(min_row=1, max_row=60)]
        for s in ("Currency Codes - ISO 4217", "Country Codes - ISO 3166-1"))
    check("C2  ISO 4217 and ISO 3166-1 reference sheets preserved verbatim", same)

    check("C3  country name propagated, Czechia removed",
          wb["Version Control"]["B9"].value == "Colombia"
          and not any("Czechia" in str(c.value)
                      for s in ("Instructions", "Introduction")
                      for r in wb[s].iter_rows() for c in r if c.value))

    # orange columns empty on data rows
    leaks = []
    for sheet, orange, namecol in (("ID Information", ID_ORANGE, 3),
                                   ("Country Fields", CF_ORANGE, 4)):
        ws = wb[sheet]
        hdr = {r for r in range(1, ws.max_row + 1) if ws.cell(r, namecol).value == "Field Name"}
        for r in range(1, ws.max_row + 1):
            if r in hdr:
                continue
            for c in orange:
                if ws.cell(r, c).value not in (None, ""):
                    leaks.append((sheet, r, c))
    check("C4  ORANGE (dev-team) columns left empty on every data row", not leaks, str(leaks[:5]))

    # blue mandatory columns populated
    blanks = []
    for sheet, namecol, cols in (("ID Information", 3, (1, 3, 6, 7, 9, 10, 22)),
                                 ("Country Fields", 4, (2, 4, 6, 7, 8, 10, 11, 23))):
        ws = wb[sheet]
        for r in range(1, ws.max_row + 1):
            v = ws.cell(r, namecol).value
            if not v or v == "Field Name":
                continue
            for c in cols:
                if ws.cell(r, c).value in (None, ""):
                    blanks.append((sheet, r, c, v))
    check("C5  required BLUE columns populated on every field row", not blanks, str(blanks[:5]))

    # data types restricted
    bad = []
    for sheet, namecol, dtcol, ftcol in (("ID Information", 3, 7, 9),
                                         ("Country Fields", 4, 8, 10)):
        ws = wb[sheet]
        for r in range(1, ws.max_row + 1):
            v = ws.cell(r, namecol).value
            if not v or v == "Field Name":
                continue
            if ws.cell(r, dtcol).value not in ("M", "CM", "O"):
                bad.append((sheet, r, "datatype", ws.cell(r, dtcol).value))
            if ws.cell(r, ftcol).value not in ("Text", "Number", "Date", "Integer",
                                               "Decimal", "Counter"):
                bad.append((sheet, r, "fieldtype", ws.cell(r, ftcol).value))
    check("C6  Data Type in {M,CM,O} and Field Type in the six permitted values",
          not bad, str(bad[:5]))

    # CM rows have a pre-condition
    nopre = []
    for sheet, namecol, dtcol, precol in (("ID Information", 3, 7, 8),
                                          ("Country Fields", 4, 8, 9)):
        ws = wb[sheet]
        for r in range(1, ws.max_row + 1):
            if ws.cell(r, dtcol).value == "CM" and not ws.cell(r, precol).value:
                nopre.append((sheet, r, ws.cell(r, namecol).value))
    check("C7  every Conditional-Mandatory field carries a pre-condition", not nopre, str(nopre))

    # mapper integrity
    ws = wb["Country Option Mappers"]
    defined, incomplete, noconstraint = set(), [], []
    for r in range(4, ws.max_row + 1):
        a, code = ws.cell(r, 2).value, ws.cell(r, 3).value
        if a == "Option Mapper Description":
            continue
        if a:
            defined.add(a)
            if not ws.cell(r, 7).value:
                noconstraint.append(a)
        if code is not None:
            if any(ws.cell(r, c).value in (None, "") for c in (3, 4, 5, 6)):
                incomplete.append((r, code))
    check("C8  every option-mapper code has code, abbreviation, local name and English description",
          not incomplete, str(incomplete[:5]))
    check("C9  every option-mapper block carries a Constraint / Notes entry (v2.4 C14)",
          not noconstraint, str(noconstraint))

    unresolved = []
    for sheet, col in (("ID Information", 11), ("Country Fields", 12)):
        w = wb[sheet]
        for r in range(1, w.max_row + 1):
            v = w.cell(r, col).value
            if v and v != "Option Mapper" and v not in defined and v not in EXTERNAL_MAPPERS:
                unresolved.append((sheet, r, v))
    check("C10 every Option Mapper reference resolves to a defined mapper",
          not unresolved, str(unresolved))

    orphans = sorted(defined - {w.cell(r, col).value
                                for sheet, col in (("ID Information", 11), ("Country Fields", 12))
                                for w in [wb[sheet]] for r in range(1, w.max_row + 1)})
    # Social Security Subsystem and PILA Novedad are reference mappers by design
    orphans = [o for o in orphans
               if o not in ("Social Security Subsystem", "PILA Novedad (Change Event) Type")]
    check("C11 no orphan mappers (every mapper is referenced, bar the two documented "
          "reference-only mappers)", not orphans, str(orphans))

    # scope: no amounts / parameters as field names
    banned = re.compile(r"\b(gross|net pay|taxable income|base salary|basic salary|contractual "
                        r"salary|ceiling|threshold|minimum wage|UVT|SMMLV|rate of)\b", re.I)
    leak = []
    for sheet, col in (("ID Information", 3), ("Country Fields", 4)):
        w = wb[sheet]
        for r in range(1, w.max_row + 1):
            v = w.cell(r, col).value
            if isinstance(v, str) and banned.search(v):
                leak.append((sheet, r, v))
    check("C12 no calculated amount, rate, ceiling or parameter carried as a DD field", not leak,
          str(leak))

    # traceability: every DD-bucket spec mapping cited somewhere in the notes
    mapnames = set()
    for f in sorted(glob.glob(os.path.join(SPECS, "CO-*-Spec.xlsx"))):
        sw = load_workbook(f, data_only=True)
        for s in [x for x in sw.sheetnames if "Spec" in x]:
            w = sw[s]
            hdr = None
            for r in range(1, 8):
                if w.cell(r, 1).value == "Field Name (EN)":
                    hdr = r
                    break
            if hdr is None:
                continue
            for r in range(hdr + 1, w.max_row + 1):
                sm = (w.cell(r, 12).value or "").strip()
                if sm and classify(sm) == "DD":
                    for part in re.split(r"\s*\+\s*", sm.split("(")[0]):
                        if "." in part:
                            mapnames.add(part.strip())
    blob = "\n".join(str(wb[s].cell(r, c).value)
                     for s, c in (("ID Information", 22), ("Country Fields", 23))
                     for r in range(1, wb[s].max_row + 1)
                     if wb[s].cell(r, c).value)
    untraced = sorted(m for m in mapnames if m not in blob)
    check("C13 every DD-bucket spec mapping is traceable to a DD field", not untraced,
          str(untraced))

    width = max(len(n) for n, _, _ in results)
    fails = 0
    for n, ok, d in results:
        print("%-*s  %s%s" % (width, n, "PASS" if ok else "FAIL", "" if ok else "  " + d))
        fails += 0 if ok else 1
    print("\n%d checks, %d failures" % (len(results), fails))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
