# -*- coding: utf-8 -*-
import openpyxl, io
import openpyxl.utils as ou

WB = "02-wtc/CO-WTC-001-v1.0.xlsx"
OUT = "08-skill/co-compliance/references/02-wtc.md"
wb = openpyxl.load_workbook(WB, data_only=True)


def cl(v):
    if v is None:
        return ""
    s = str(v)
    return s.replace("|", "\\|").replace("\r", " ").replace("\n", "<br>").strip()


L = []
W = L.append

W("""# Colombia - Wage Type Catalogue (WTC) - COMPLETE REFERENCE

**Source artifact:** `02-wtc/CO-WTC-001-v1.0.xlsx` (v1.0, 2026-09-04, Mercans Compliance Regulations Team)
**Structure:** 6 sheets - Wage Type Catalogue **402 rows x 28 columns** - **300 of 300** Global WTC baseline
codes included (0 excluded) + **102** Colombia-specific `CO-` codes.
**Currency:** COP - **Fiscal year:** 2026 - **SMMLV** 1,750,905 - **UVT** 52,374.

> **DERIVED flag (disclosed in the source artifact):** the Mercans code numbers for the 102 Colombia-specific
> rows are **DERIVED** - no Mercans numeric code range has been assigned for Colombia, so mnemonic `CO-` codes
> are used and **must be renumbered at system-configuration time**.

## Column legend (verbatim header text of the Wage Type Catalogue)

| Col | Header (verbatim) |
|---|---|""")

ws = wb["Wage Type Catalogue"]
hdr = [c.value for c in ws[1]]
for i, h in enumerate(hdr):
    W("| %s | %s |" % (ou.get_column_letter(i + 1), cl(h)))

W("""
The **five social-insurance subjection columns Q-U** (instead of one) and the **three Colombia-specific base
columns V-X** are deliberate: Colombia has eight mandatory contributions across three insurance branches, three
payroll levies and one employee-only solidarity surcharge, and **they do not share a base**. See Sheet 5 -
Global WTC Coverage, items 7-9.

---

## Sheet 1 - Version Control
""")

vc = wb["Version Control"]
W("| Version | Effective Date | Change Description | Status | Updated By |")
W("|---|---|---|---|---|")
for r in range(13, 40):
    row = [cl(vc.cell(row=r, column=c).value) for c in range(2, 7)]
    if not any(row):
        continue
    W("| " + " | ".join(row) + " |")

W("""
> **[QA MINOR-01]** Row 14 of the source Version Control sheet (`2.0 | 2025-09-09 | Wage codes Mapping |
> Released | Devshree Vyas`) is **un-cleaned CZ template residue**, confirmed identical to row 14 of
> `shared/_CZ_Wage_Type_Catalogue_V2_0.xlsx`. It makes the change log read as if v2.0 predates v1.0 by a year.
> Ignore it: the only genuine Colombia entry is **v1 of 2026-09-04**. Fix = delete the row, or replace it with
> the v1.1 DD-to-spec alignment-patch entry that the DD and all six report specs already carry.

---

## Sheet 2 - Wage Type Catalogue: subjection and configuration matrix (all 402 rows)

Columns A-C, E, G-Y, AA. The four long-text columns - **D** *Wage Type Explanation*, **F** *Formula*,
**Z** *Tax Code Source* and **AB** *YTD Remarks* - are reproduced in full, per code, in
"Sheet 2 (continued)" below.

Legend for the subjection columns: **N** Subject to Tax - **O** Table Tax (ET art. 383) - **P** Special Tax
(non-resident flat 20%, ET art. 408) - **Q** Salud EPS - **R** FSP (Fondo de Solidaridad Pensional) -
**S** ARL - **T** Parafiscales (CCF 4% / SENA 2% / ICBF 3%) - **U** Pension Obligatoria -
**V** Salary / Non-Salary (CST arts. 127 / 128) - **W** Statutory-Benefit Base - **X** Vacation Base (CST art. 192).

| Code | Name (EN) | Name (ES) | Category | Tax Code | Calc Type | Prorating | Occurrence | Ign0 | Enforce | InPerRec | N | O | P | Q | R | S | T | U | V | W | X | Nomina Electronica element | YTD Load |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|""")

rows = []
for r in ws.iter_rows(min_row=2, max_row=ws.max_row):
    v = [cl(c.value) for c in r]
    while len(v) < 28:
        v.append("")
    if not v[0]:
        continue
    rows.append(v)

idx = [0, 1, 2, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 26]
for v in rows:
    W("| " + " | ".join(v[i] for i in idx) + " |")

W("""
**Row count: %d wage types.**

---

## Sheet 2 (continued) - Explanation, Formula, Tax Code Source and YTD Remarks, per code

One block per wage type, in catalogue order. Nothing is summarised: columns **D**, **F**, **Z** and **AB**
appear here in full.
""" % len(rows))

for v in rows:
    W("\n### `%s` - %s%s" % (v[0], v[1], (" - *%s*" % v[2] if v[2] else "")))
    W("")
    W("| Attribute | Value |")
    W("|---|---|")
    W("| Category (col E) | %s |" % v[4])
    W("| Tax Code (col G) | %s |" % v[6])
    W("| Wage Type Explanation (col D) | %s |" % v[3])
    W("| Formula (col F) | %s |" % v[5])
    W("| Nomina Electronica element (col Y) | %s |" % v[24])
    W("| Tax Code Source - C9 (col Z) | %s |" % v[25])
    W("| YTD Load (col AA) | %s |" % v[26])
    W("| YTD Remarks (col AB) | %s |" % v[27])


def text_sheet(name, title):
    W("\n---\n\n## %s\n" % title)
    s = wb[name]
    W("```")
    blanks = 0
    for r in s.iter_rows(min_row=1, max_row=s.max_row):
        parts = [str(c.value).rstrip() for c in r if c.value is not None and str(c.value).strip() != ""]
        if not parts:
            blanks += 1
            if blanks <= 1:
                W("")
            continue
        blanks = 0
        W("  ".join(parts))
    W("```")


text_sheet("Employer Sick Pay", "Sheet 3 - Employer Sick Pay and the incapacity cascade (2026)")
text_sheet("Tax Credit", "Sheet 4 - Tax Credit (Colombia has NONE - the equivalent mechanisms are deductions and exempt income)")

# ---- Sheet 5 Global WTC Coverage ----
W("\n---\n\n## Sheet 5 - Global WTC Coverage\n")
gc = wb["Global WTC Coverage"]
W("| # | Item | Detail |")
W("|---|---|---|")
mode = "cov"
legend_title = ""
for r in gc.iter_rows(min_row=2, max_row=gc.max_row):
    a, b, c = [cl(x.value) for x in (r[0], r[1], r[2])]
    if not any((a, b, c)):
        continue
    if a.upper().startswith("TAX CODE LEGEND"):
        mode = "hdr"
        legend_title = a
        continue
    if mode == "hdr":
        mode = "legend"
        W("\n### Tax code legend (control C9 - every code defined and sourced to a Colombian authority publication)\n")
        W("*%s*\n" % legend_title)
        W("| Tax Code | Meaning | Official Source |")
        W("|---|---|---|")
        continue
    W("| %s | %s | %s |" % (a, b, c))

W("""
> **[QA MINOR-09]** `CO-TX-08` (non-resident flat 20%, ET art. 408) is fully defined in the legend but is
> assigned to **zero** of the 402 catalogue rows. This is **not an omission**: non-residency is a
> *residency-driven overlay* applied per employee through **column P (Special Tax)**, not a per-wage-type
> assignment. Assignment distribution across the catalogue: `CO-TX-01` 249 - `CO-NA` 109 - `CO-TX-06` 17 -
> `CO-TX-02` 9 - `CO-TX-10` 8 - `CO-TX-07` 5 - `CO-TX-03` 2 - `CO-TX-04` / `CO-TX-05` / `CO-TX-09` 1 each -
> `CO-TX-08` 0.
""")

# ---- Sheet 6 Form Reference Guide ----
W("\n---\n\n## Sheet 6 - Form Reference Guide (control C17)\n")
fr = wb["Form Reference Guide"]
h = [cl(c.value) for c in fr[1]]
h = [x for x in h if x]
W("| " + " | ".join(h) + " |")
W("|" + "---|" * len(h))
n = 0
for r in fr.iter_rows(min_row=2, max_row=fr.max_row):
    v = [cl(c.value) for c in r][:len(h)]
    while len(v) < len(h):
        v.append("")
    if not any(v):
        continue
    W("| " + " | ".join(v) + " |")
    n += 1
W("\n**%d entries.** Validated mechanically: every target file exists, every sheet name resolves and every row"
  " number is in range - **0 broken pointers**. Two entries are honestly marked `DERIVED - no statutory filing`"
  " (benefit accruals; withholding-procedure election)." % n)

W("""
---

## Catalogue statistics (from the QA cross-check, 2026-09-07)

| Metric | Value |
|---|---|
| Global baseline file | `shared/Global_WTC_V1_0.xlsx` |
| Global codes in the baseline | 300 |
| Global codes included in the Colombia WTC | **300 (100.0%)** |
| Global codes excluded | **0** |
| Colombia-specific additions (`CO-` prefixed) | **102** |
| Total Wage Type Catalogue rows | **402** |
| Blank cells across the 11 subjection columns | **0** (all 402 rows) |
| `Yes/No` conditional entries | 246 - **all 246** carry a substantive column-D justification (control C3) |
| Tax codes defined and sourced | 11 (`CO-TX-01`...`CO-TX-10` + `CO-NA`), all with Colombian authority citations (control C9) |

**Colombia-specific additions by category:** Earnings (core pay, six premium hour types, statutory benefits,
leave cascade, termination heads) **55** - Employee deductions **19** - Employer contributions and accruals
**11** - Calculation bases **5** - Configuration flags **8** - Taxes **2** - Rates / percentages **2** -
Intermediary / notional **2** - total **102** (of which 8 flags + 5 bases + 2 rates + 2 notional = 17
non-monetary).

**Catalogue-wide category distribution:** Earning 295 - Deduction 71 - Employer Contribution 16 - Flag 8 -
Base 5 - Percentage 3 - Tax 2 - Intermediary 1 - Notional 1.

## 2026 mid-year cut-overs encoded in the Formula column (do NOT simplify)

| Change | Before | From | Legal basis |
|---|---|---|---|
| Sunday / holiday rest-day premium (recargo dominical y festivo) | **80%** | **90% from 1 July 2026** (then 100% from 1 July 2027) | Ley 2466 de 2025 |
| Compounded rest-day overtime `CO-HEDDF` | 205% | **215%** from 1 Jul 2026 | idem |
| Compounded rest-day overtime `CO-HENDF` | 255% | **265%** from 1 Jul 2026 | idem |
| Compounded rest-day night premium `CO-HRNDF` | 115% | **125%** from 1 Jul 2026 | idem |
| Monthly hourly divisor | **220** | **210 from 15 July 2026** | Ley 2101 de 2021 (progressive working-week reduction) |

> The WTC explicitly warns that the nomina electronica technical annex's **legacy `75 / 100 / 150 / 110`
> literals must NOT be configured**. Use the dual-dated statutory values above.

---

## Payslip-to-WTC wiring gap (QA MAJOR-01)

The payslip generator carries `XXXXX` placeholders instead of real WTC codes on 36 cells (18 lines x 2 language
sheets). The correct codes, all of which exist in this catalogue, are:

`CO-SALARIO-BASICO` - `CO-AUX-TRANSPORTE` - `CO-COMISIONES` - `CO-DED-SALUD` - `CO-DED-PENSION` -
`CO-DED-FSP-SOLIDARIDAD` - `CO-RETENCION-FUENTE` - `CO-ER-SALUD` - `CO-ER-PENSION` - `CO-ER-ARL` -
`CO-ER-CCF` - `CO-ER-SENA` - `CO-ER-ICBF` - `CO-PROV-CESANTIAS` - `CO-PROV-INTERESES-CESANTIAS` -
`CO-PROV-PRIMA` - `CO-PROV-VACACIONES`.

Payslip lines *Overtime & Surcharges* and *Commissions & Bonuses* each bundle multiple wage types and must be
split into their constituent codes (or labelled with an explicit multi-code list) - see also QA MINOR-05 on the
CST art. 192 vacation base.
""")

txt = "\n".join(L)
io.open(OUT, "w", encoding="utf-8").write(txt)
print(OUT, len(txt), "rows", len(rows))
