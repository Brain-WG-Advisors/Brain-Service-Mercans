# -*- coding: utf-8 -*-
import io, datetime
import openpyxl

WB = "05-data-dictionary/CO-DD-001-v1.0.xlsx"
OUT = "08-skill/co-compliance/references/05-data-dictionary.md"
wb = openpyxl.load_workbook(WB, data_only=True)


def raw(v):
    if v is None:
        return ""
    if isinstance(v, (datetime.datetime, datetime.date)):
        return v.isoformat()[:10]
    return str(v).replace("\r", "").rstrip()


def cl(s):
    return s.replace("|", "\\|").replace("\n", "<br>").strip()


def render_sheet(ws, W):
    blocks = []
    cur = None
    for r in ws.iter_rows(min_row=1, max_row=ws.max_row):
        v = [raw(c.value) for c in r]
        while v and v[-1].strip() == "":
            v.pop()
        if not any(x.strip() for x in v):
            if cur is not None and cur[0] == "text" and cur[1] and cur[1][-1] != [""]:
                cur[1].append([""])
            continue
        kind = "table" if len([x for x in v if x.strip()]) >= 2 else "text"
        if cur is None or cur[0] != kind:
            cur = (kind, [])
            blocks.append(cur)
        cur[1].append(v)

    for kind, rows in blocks:
        if kind == "text":
            while rows and rows[-1] == [""]:
                rows.pop()
            W("")
            for v in rows:
                line = next((x for x in v if x.strip()), "")
                W(("**%s**" % line) if line else "")
            W("")
        else:
            ncol = max(len(v) for v in rows)
            rows = [v + [""] * (ncol - len(v)) for v in rows]
            keep = [i for i in range(ncol) if any(r[i].strip() for r in rows)]
            rows = [[cl(r[i]) for i in keep] for r in rows]
            n = len(keep)
            W("")
            if n == 2 and len(rows) >= 3:
                W("| Item | Value |")
                W("|---|---|")
                body = rows
            else:
                W("| " + " | ".join(rows[0]) + " |")
                W("|" + "---|" * n)
                body = rows[1:]
            for v in body:
                W("| " + " | ".join(v) + " |")
            W("")


L = []
W = L.append

W("""# Colombia - Data Dictionary (DD) - COMPLETE REFERENCE

**Source artifact:** `05-data-dictionary/CO-DD-001-v1.0.xlsx` (v1.0 of 2026-09-04, patched to **v1.1** on
2026-09-07 by the DD-to-Spec alignment patch)
**Format:** Mercans CZ V2.0 Data Dictionary template - all 8 sheets in template order.
**Jurisdiction:** Colombia (CO) - **Currency:** COP - **Fiscal year:** 2026

## Contents and totals

| Sheet | Content | Rows |
|---|---|---|
| 1. Version Control | change log (v1 initial + v1.1 alignment patch) | 2 entries |
| 2. Introduction | template introduction and table of contents | - |
| 3. Instructions | column-by-column instructions (template, verbatim) | 15 items |
| 4. ID Information | Colombia identification fields - employee + legal entity | **17 fields** |
| 5. Country Fields | Colombia country-specific data fields | **98 fields** |
| 6. Country Option Mappers | code tables consumed by the fields above | **35 mappers** (counted in the v1.0/v1.1 file) |
| 7. Currency Codes - ISO 4217 | template reference list (`DO NOT TOUCH`) | ISO 4217 |
| 8. Country Codes - ISO 3166-1 | template reference list (`DO NOT TOUCH`) | ISO 3166-1 alpha-2 |

**Field total: 115** (17 ID Information + 98 Country Fields), of which **53 M** (Mandatory) ·
**53 CM** (Conditional Mandatory) · **9 O** (Optional).

> **Count note [VERIFY WITH RA]:** the stage-07 QA report states *"30 option mappers"* and
> *"all 30 carrying a `Referenced by ...` reverse-reference"*. Counted directly in the delivered workbook there
> are **35** mappers: **32** carry an explicit `Referenced by <field> (Mandatory=...)` reverse-reference, and
> **3** are documented reference/generic mappers instead — `Social Security Subsystem` and
> `PILA Novedad (Change Event) Type` (*"Reference mapper for ..."*) and `Yes/No Indicator` (*"Generic two-value
> indicator referenced by every S/N master-data flag in this dictionary"*). The C16 intent is met in all 35
> cases; only the QA report's count is stale.

## Scope rules observed (verified by the QA cross-check, all PASS)

- **No amounts in the Data Dictionary.** Contractual monthly salary, salary-in-kind valuation, housing-loan
  interest, prepaid-health premiums, voluntary pension / AFC contributions and third-party meal payments are
  **deliberately absent**. Zero occurrences of SMMLV, UVT or any ceiling value anywhere in the DD.
- **No Base Salary field.**
- **Blue columns only.** The 12 orange system columns (`Ordinal`, `Internal Code`, `Parent Field Group` and its
  ordinal / internal code, `Sub Group` and its ordinal / internal code, `Default Value`, `MSS Field Permissions`,
  `ESS Field Permissions`) are intentionally **left blank** - they are populated at system-configuration time,
  not by compliance. Their headers are shown below with empty cells.
- **`Country Fields` starts at column B**, exactly as the CZ V2.0 template does.
- No Czech residue in Introduction or Instructions.

## Mandatoriness and traceability

- **53 fields are `CM` (Conditional Mandatory)** and **all 53** carry a populated
  `Pre-Condition for Conditional Mandatory` - control **C16**, 100%.
- **All 35 option mappers** are bidirectionally documented - 32 with an explicit
  `Referenced by <field> (Mandatory=...)` reverse-reference back to the consuming DD field, 3 as declared
  reference/generic mappers - the C16 bidirectional requirement, satisfied in full.
- **94 of 94** `DD`-bucket field tokens from the six report specs (`Employee.*`, `Company.*`, `Contract.*`,
  160 spec rows) are present here - **100%** 4-bucket reconciliation.
- 22 of the 115 DD fields carry **no** `Spec ref:` (Date of Birth, Gender, Nationality, weekly hours, days per
  week, obligatory rest day, 36-hour shift flag, work modality, withholding procedure, pension regime,
  severance regime, multi-employer flag and 10 others). Each is a CCG-Module-2-sourced calculation or
  configuration input that no *filing* carries - legitimately DD-only, not orphaned.

## Open QA items on this artifact

> **[QA MINOR-03]** `Country Option Mappers` rows 5 (code `11`, *Registro civil de nacimiento*) and 22 / 23 / 26
> (`CD` *Carne diplomatico*, `SC` *Salvoconducto*, `PT` *Permiso por Proteccion Temporal*) carry codes that
> `scope_manifest.json` -> `option_mapper_scope.personal_id_type` declares **out of scope** (its `_comment`
> states out-of-scope codes must be excluded from **all** artifacts). In mitigation the DD annotates each one
> (*"Under-7s; never an employee"*, *"CESANTIAS XLS LAYOUT ONLY"*) rather than presenting it as usable, and
> `CD` / `SC` / `PT` are genuinely in the published PILA and cesantias catalogues. **Read these four as
> REFERENCE ONLY - NOT IN SCOPE** until the manifest and the DD are reconciled.

> **[QA MINOR-11]** The **active-pensioner flag** has no discrete DD field. CCG Module 2 lists it as a
> social-security profile field and the WTC defines `CO-FLAG-PENSIONADO-ACTIVO`, but the DD carries it only
> through **`Worker Sub-Type` = `01`**, which is therefore its sole carrier. The manifest's
> `inbound_data_contract` also names it explicitly among the per-employee inputs the engine must receive.
> Functionally covered; formally under-specified.

**Colombia has NO separate social-security number.** The identity-document type + document number pair is the
key on every statutory artefact - see `Employee Document Type` / `Employee Document Number` and the PILA
`T2R2-003 + T2R2-004` composite key. **Colombia does not use IBAN** for domestic accounts.

---
""")

TITLES = {
    "Version Control": "Sheet 1 - Version Control",
    "Introduction": "Sheet 2 - Introduction",
    "Instructions": "Sheet 3 - Instructions (template, verbatim)",
    "ID Information": "Sheet 4 - ID Information (17 fields: employee + legal entity)",
    "Country Fields": "Sheet 5 - Country Fields (98 Colombia-specific fields)",
    "Country Option Mappers": "Sheet 6 - Country Option Mappers (30 mappers)",
    "Currency Codes - ISO 4217": "Sheet 7 - Currency Codes, ISO 4217 (template reference, DO NOT TOUCH)",
    "Country Codes - ISO 3166-1": "Sheet 8 - Country Codes, ISO 3166-1 alpha-2 (template reference, DO NOT TOUCH)",
}

for ws in wb.worksheets:
    W("\n\n---\n\n## %s\n" % TITLES.get(ws.title, ws.title))
    render_sheet(ws, W)

txt = "\n".join(L)
io.open(OUT, "w", encoding="utf-8").write(txt)
print(OUT, len(txt))
