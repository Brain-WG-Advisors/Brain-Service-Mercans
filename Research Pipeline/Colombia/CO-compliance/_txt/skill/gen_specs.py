# -*- coding: utf-8 -*-
import io, os, glob, datetime
import openpyxl

OUT = "08-skill/co-compliance/references/04-reports-spec.md"
SPECDIR = "04-reports-spec"

ORDER = [
    "CO-DIAN-001-NominaElectronica-Spec.xlsx",
    "CO-DIAN-002-Formulario350-Spec.xlsx",
    "CO-PILA-003-AportesSeguridadSocial-Spec.xlsx",
    "CO-DIAN-004-Formulario220-Spec.xlsx",
    "CO-DIAN-005-Formato2276-Spec.xlsx",
    "CO-CESANTIAS-006-ConsignacionAnual-Spec.xlsx",
]


def cl(v):
    if v is None:
        return ""
    if isinstance(v, (datetime.datetime, datetime.date)):
        return v.isoformat()[:10]
    s = str(v)
    return s.replace("|", "\\|").replace("\r", " ").replace("\n", "<br>").strip()


def raw(v):
    if v is None:
        return ""
    if isinstance(v, (datetime.datetime, datetime.date)):
        return v.isoformat()[:10]
    return str(v).replace("\r", "").rstrip()


def row_vals(r):
    """Return (escaped-for-table, raw-for-code-fence) value lists."""
    v = [raw(c.value) for c in r]
    while v and v[-1].strip() == "":
        v.pop()
    return v


def render_sheet(ws, W):
    blocks = []   # ('table', [rows]) or ('text', [lines])
    cur = None
    for r in ws.iter_rows(min_row=1, max_row=ws.max_row):
        v = row_vals(r)
        if not any(x for x in v):
            # a blank row breaks a paragraph but never breaks a table
            if cur is not None and cur[0] == "text" and cur[1] and cur[1][-1] != [""]:
                cur[1].append([""])
            continue
        kind = "table" if len([x for x in v if x]) >= 2 else "text"
        if cur is None or cur[0] != kind:
            cur = (kind, [])
            blocks.append(cur)
        cur[1].append(v)

    for kind, rows in blocks:
        if kind == "text":
            # free text / XML / fixed-width records: fenced so layout survives verbatim
            while rows and rows[-1] == [""]:
                rows.pop()
            W("")
            W("```")
            for v in rows:
                W(v[0] if v else "")
            W("```")
            W("")
        else:
            ncol = max(len(v) for v in rows)
            rows = [[cl(x) for x in v] + [""] * (ncol - len(v)) for v in rows]
            W("")
            if ncol == 2 and len(rows) >= 3:
                W("| Item | Value |")
                W("|---|---|")
                body = rows
            else:
                W("| " + " | ".join(rows[0]) + " |")
                W("|" + "---|" * ncol)
                body = rows[1:]
            for v in body:
                W("| " + " | ".join(v) + " |")
            W("")


L = []
W = L.append

W("""# Colombia - Statutory Report Specifications - COMPLETE REFERENCE

**Source artifacts:** the six in-scope specifications in `04-reports-spec/`, each built to the Spain 9-sheet
standard with a 21-column (A-U) Sheet 4 field list.
**Jurisdiction:** Colombia (CO) - **Currency:** COP - **Fiscal year:** 2026
**Totals:** 6 specs - 54 sheets - **563 Sheet-4 field rows** (Nomina Electronica 225 - PILA 170 - Formulario 220
75 - Formulario 350 69 - Cesantias 52 - Formato 2276 50).

## The six in-scope filings

| CCG ID | Filing ID (scope_manifest) | Report | Authority | Frequency | Deadline | Channel | Spec file |
|---|---|---|---|---|---|---|---|
| CO-RPT-001 | CO-DIAN-NE-MONTHLY-001 | Electronic Payroll Support Document (*documento soporte de pago de nomina electronica*) | DIAN | Monthly | Within the first **10 days** of the following month | **MACHINE-TO-MACHINE** SOAP 1.2 (the only M2M channel in Colombia) | `CO-DIAN-001-NominaElectronica-Spec.xlsx` |
| CO-RPT-002 | CO-DIAN-F350-MONTHLY-002 | Form 350 - monthly withholding return (*declaracion de retenciones en la fuente*) | DIAN | Monthly | **7th to 16th business day** of the following month, by the last digit of the NIT | Portal round-trip (Muisca), IFE-signed | `CO-DIAN-002-Formulario350-Spec.xlsx` |
| CO-RPT-003 | CO-PILA-MONTHLY-003 | PILA - integrated social-security and payroll-levy return | Ministerio de Salud y Proteccion Social, via a licensed *operador de informacion* | Monthly | **2nd to 16th business day** of the following month, by the last two digits of the NIT | Portal round-trip / fixed-width flat file to an operator | `CO-PILA-003-AportesSeguridadSocial-Spec.xlsx` |
| CO-RPT-004 | CO-DIAN-F220-ANNUAL-004 | Form 220 - annual income and withholding certificate to each employee | DIAN (issued to the employee) | Annual | **Last business day of March** | Issued to the employee (no filing) | `CO-DIAN-004-Formulario220-Spec.xlsx` |
| CO-RPT-005 | CO-DIAN-EXO2276-ANNUAL-005 | Formato 2276 v4 - third-party information return on work and pension income | DIAN | Annual | **May-June**, by NIT | Portal upload of XML prepared in the *prevalidador* | `CO-DIAN-005-Formato2276-Spec.xlsx` |
| CO-RPT-006 | CO-CESANTIAS-DEPOSIT-ANNUAL-006 | Severance-savings annual deposit allocation | *Fondos de Cesantias* (Porvenir, Proteccion, Colfondos, Skandia, FNA), via an *operador de informacion* | Annual | **By 14 February** following the 31 December liquidation (for accrual year 2026: **Friday 12 February 2027**) | Portal round-trip / file upload to an operator | `CO-CESANTIAS-006-ConsignacionAnual-Spec.xlsx` |

**CO-RPT-007** (MinTrabajo disability-hiring contract report) is **descoped** as HR-scope in
`scope_manifest.json` - no spec exists and none should. See QA MAJOR-03 in `07-qa-report.md`.

## Sheet-4 21-column layout (A-U), identical in all six specs

| Col | Header (as used in the Colombia specs) | Standard label (variance noted in QA MINOR-07) |
|---|---|---|
| A | Field Name (EN) | same |
| B | Field Name (Local ES) | same |
| C | **Record Type** | `Record Type / Section` |
| D | Field Position | same |
| E | Payroll Field (Y/N) | same |
| F | Mandatory (Y/N/C) | same |
| G | Conditional Reason | same |
| H | **Position (in file)** | `Position (Start-End)` |
| I | **Length** | `Field Length` |
| J | Format | same |
| K | Example | same |
| L | System Mapping | same |
| M | **Explanation** | `Field Explanation` |
| N | Relevant for Payroll (Y/N) | same |
| O | Option Values | same |
| P | Rounding | same |
| Q | Negative (Y/N) | same |
| R | Value Type | same |
| S | **Frequency** | `Reporting Frequency` |
| T | Query to RA | same |
| U | RA Comments | same |

**System Mapping buckets (4-bucket DD reconciliation, 563 rows):** `DD` (`Employee.*`, `Company.*`,
`Contract.*`) 160 rows / 94 distinct tokens - all 94 present in the Data Dictionary (**100%**) -
`CALC` (`Payroll.*`, `SUM(Payroll...)`, casilla / numeral arithmetic) 249 - `SYS` (`Mercans.*`, `System.*`,
`PayPeriod.*`, `Constant*`, `(system total)`) 136 - `TX / out-of-payroll` (`(employee declaration)`,
`(client tax function)`, `(client accounts payable)`) 18.

> **[QA MINOR-10]** Column L carries no WTC code for amount-bearing fields (it uses `Payroll.*` tokens). The
> WTC-to-spec direction is covered by the WTC's 65-entry Form Reference Guide, but the spec-to-WTC direction is
> not: a developer mapping `NIE071` has no WTC code in front of them. Suggested fix:
> `Payroll.Transport_Allowance [WTC: CO-AUX-TRANSPORTE / 62520]`.

> **[QA MINOR-07 / MINOR-08]** Five of the 21 Sheet-4 column labels and the Version-Control change-log column
> order differ in wording from `shared/report-spec-template/REPORT_SPEC_STANDARD_FORMAT.md`. Semantics, order
> and count are correct and the deviation is consistent across all six specs.

> **[QA MINOR-02]** The PILA spec does not label `T2R2-003` + `T2R2-004` (contributor document type + number)
> as a **composite key** in column M, even though `CO-CESANTIAS-006` annotates the identical pair as
> `COMPOSITE FIELD` at row 4. Column M calls `T2R2-004` a *"Join key to NIE045 / F220 casilla 25 / 2276
> numeral 2"* only. Treat type + number **together** as the record key. (Formulario 350 needs no composite key -
> it is an aggregate return with no per-employee record.)

**Source-status honesty (per spec, as declared in Sheet 1 / Sheet 5):** PILA is `PRIMARY, BYTE-EXACT` with
field counts and position totals arithmetically verified (Archivo Tipo 1 = 34 fields / 567 positions;
Archivo Tipo 2 registro 1 = 22 / 359; registro 2 = 97 / 686). Formato 2276 is marked **DERIVED** for the XML
layout because the DIAN *especificaciones tecnicas* annex is not held locally. No spec overclaims its sourcing.

---
""")

for i, fn in enumerate(ORDER, start=1):
    p = os.path.join(SPECDIR, fn)
    wb = openpyxl.load_workbook(p, data_only=True)
    W("\n\n---\n\n# Spec %d of 6 - `%s`\n" % (i, fn))
    W("**Sheets (9, in standard order):** " + " - ".join("`%s`" % s for s in wb.sheetnames) + "\n")
    for si, ws in enumerate(wb.worksheets, start=1):
        W("\n## %s - Sheet %d: %s\n" % (fn.replace("-Spec.xlsx", ""), si, ws.title))
        render_sheet(ws, W)

txt = "\n".join(L)
io.open(OUT, "w", encoding="utf-8").write(txt)
print(OUT, len(txt))
