# Colombia (CO) — QA Cross-Check Report

**Artifact set:** CO-compliance v2.4 · scope_manifest v1.0 · fiscal year 2026
**Reviewed:** 2026-09-07
**Reviewer:** Mercans Compliance Regulations Team — QA cross-check (stage 07)
**Currency:** COP · **SMMLV 2026:** 1,750,905 · **UVT 2026:** 52,374

---

## 1. Executive Summary

**Overall score: 94 / 100 — PASS WITH PATCHES**

| Verdict | **NEEDS PATCHES** |
|---|---|
| CRITICAL issues | **0** |
| MAJOR issues | **3** |
| MINOR issues | **12** |

The Colombia pack is one of the stronger builds in the pipeline. Every structural gate passes:
all 300 Global WTC baseline codes are present and *individually re-configured for Colombia*
(not template-copied), the 4-bucket DD↔spec reconciliation is **100%**, all six in-scope report
specs are format-compliant to the Spain 9-sheet standard, and the WTC Form Reference Guide's 65
cross-references resolve to real spec files, sheets and in-range rows with **zero broken pointers**.

Two substantive verifications were performed rather than assumed:

- **The income-tax withholding on the payslip re-derives exactly.** Gross 19,200,000 − employee
  contributions 1,728,000 = 17,472,000; less the ET art. 206 num. 10 exempt 25% capped at
  790 UVT ÷ 12 = 3,447,955 → base 14,024,045 = 267.76732 UVT; ET art. 383 band 150–360 UVT →
  0.28 × (267.76732 − 150) + 10 = 42.97485 UVT × 52,374 = **2,250,765**, the exact figure shown.
  The 40% / 1,340-UVT art. 388 caps were correctly tested and not binding.
- **The 1 July 2026 rest-day premium step and the 15 July 2026 hourly-divisor change are both
  fully encoded** in the WTC formula column with dual-dated values (80%→90%, 220→210), including
  the compounded rest-day overtime codes (HEDDF 205%→215%, HENDF 255%→265%, HRNDF 115%→125%).
  This is the single most material Colombian 2026 change and it is not simplified anywhere.

**No stale fiscal parameters were found.** Every occurrence of 1,423,500 (2025 SMMLV) and 49,799
(2025 UVT) in the pack is an explicit historical comparison, not a live value.

All three MAJOR findings are documentation/wiring defects in the **payslip generator** and one
**stale cross-reference in the CCG**. None affects a calculation. All are cheap to patch.

---

## 2. Per-Check Alignment Scores

| # | Check | Score | Result |
|---|---|---|---|
| 1 | CCG Modules 3–9 ↔ WTC | **67 of 67 matched (100%); 65 of 67 exact treatment (97%)** | PASS |
| 2 | CCG Module 2 ↔ DD | **43 of 44 in-scope field items (98%)** | PASS |
| 3 | CCG Module 10 ↔ Report Specs | **6 of 6 in-scope reports (100%)**; 1 descoped | PASS (MAJOR doc defect) |
| 4 | DD ↔ Report Specs (4-bucket) | **94 of 94 DD-bucket fields (100%)** | PASS |
| 5 | Global WTC coverage | **300 of 300 (100%)**, 0 excluded | PASS |
| 6 | Scope discipline | **PASS**, 1 MINOR | PASS |
| 7 | Report Spec format compliance | **6 of 6 fully compliant** | PASS |
| 8 | v2.4 standards | **4 of 5 artifacts clean**; payslip has placeholders | PASS WITH PATCHES |
| 9 | v2.4 NEW — composite key / inter-field | **C13 partial · C16 100% · C17 PASS · C20 PASS** | PASS WITH PATCHES |

---

### Check 1 — CCG ↔ WTC alignment: 67 of 67 matched (100%)

Every wage-type head named in CCG Modules 3–9 resolves to a WTC row, and the tax / social-security
treatment matches column-for-column.

| CCG source | Heads | In WTC | Exact treatment match |
|---|---|---|---|
| Module 4.6 pay-component reference table | 34 | 34 | 32 |
| Module 5 contributions (8 funds, EE + ER legs) | 8 | 8 | 8 |
| Module 7 post-tax deduction list | 11 | 11 | 11 |
| Module 9 termination heads (A1–A7, B1–B7; B8 correctly out of payroll) | 14 | 14 | 14 |
| **Total** | **67** | **67** | **65** |

Spot-verified treatment matches (CCG legend CB / PL / BB / VB / TX vs WTC columns Q–U / T / W / X / N):

- **Transport allowance** (`CO-AUX-TRANSPORTE`) — CB No, PL No, **BB Yes**, VB No, TX Yes. The
  counter-intuitive Colombian line is right in both artifacts.
- **Night premium** (`CO-RECARGO-NOCTURNO`) VB **Yes** vs **day/night overtime** (`CO-HED`, `CO-HEN`)
  VB **No** — the CST art. 192 distinction is preserved, not flattened.
- **All-inclusive salary** (`CO-SALARIO-INTEGRAL`) — benefit base **No** (absorbed), vacation base
  **Yes** (full 100%), 70% IBC/levy factor carried in the formula column.
- **Service bonus** (`CO-PRIMA-SERVICIOS`) — CB No, PL No, tax code `CO-TX-03` (separate art. 385
  Procedure-1 table read). Correctly *not* treated as an ordinary monthly earning.
- **Sickness cascade** — days 1–2 employer (`CO-INCAP-EG-EMPLEADOR`, PL **Yes**) vs day 3+ EPS
  (`CO-INCAP-EG-EPS`, PL **No**, CB Yes) is split into distinct codes, as the CCG requires.

**Quality gates inside the WTC:** 0 blank cells across the 11 subjection columns for all 402 rows;
246 `Yes/No` conditional entries, **all 246** carrying a substantive column-D justification (v2.5 C3
guard); all 10 tax codes defined in the legend with a Colombian authority citation (C9).

The 2 non-exact rows are a **CCG-side** simplification, not a WTC error — see MINOR-04.

---

### Check 2 — CCG ↔ DD alignment: 43 of 44 (98%)

CCG Module 2 correctly summarises fields by group and defers field-level detail to CO-DD-001
(explicit scope note in the module body). DD carries **17 ID Information** + **98 Country Fields**
= **115 field rows**.

| CCG Module 2 group | In-scope items | In DD |
|---|---|---|
| Identity | 6 | 6 |
| Contact and location | 4 | 4 |
| Employment | 7 (period start/end and time worked are CALC) | 7 |
| Remuneration structure | 2 (3 amounts excluded by scope rule) | 2 |
| Working time | 5 | 5 |
| Social-security profile | 9 | 8 |
| Withholding profile | 4 (7 declared amounts excluded by scope rule) | 4 |
| Payment | 5 | 5 |
| Accumulators | 0 (all CALC) | n/a |
| **Total** | **44** | **43** |

The single gap: CCG Module 2 lists an **active-pensioner flag** as a distinct social-security profile
field; the DD carries it only implicitly through `Worker Sub-Type` = `01`. The WTC does define a
first-class `CO-FLAG-PENSIONADO-ACTIVO`. Functionally covered, so scored as a match-with-nuance
rather than a defect — see MINOR-11.

Amount-bearing items (contractual monthly salary, salary-in-kind valuation, housing-loan interest,
prepaid health premiums, voluntary pension/AFC contributions, third-party meal payments) are
**correctly absent** from the DD under the v2.4 rule that no amounts enter the Data Dictionary.

**Option mappers:** 30 mappers documented, every one carrying a `Referenced by <field> (Mandatory=…)`
reverse-reference back to the consuming DD field — the C16 bidirectional requirement, satisfied
in full.

---

### Check 3 — CCG ↔ Report Specs: 6 of 6 in-scope (100%)

| CCG ID | Report | Spec file | Status |
|---|---|---|---|
| CO-RPT-001 | Electronic Payroll Support Document (nómina electrónica) | `CO-DIAN-001-NominaElectronica-Spec.xlsx` | ✓ |
| CO-RPT-002 | Form 350 — monthly withholding return | `CO-DIAN-002-Formulario350-Spec.xlsx` | ✓ |
| CO-RPT-003 | PILA — integrated contribution return | `CO-PILA-003-AportesSeguridadSocial-Spec.xlsx` | ✓ |
| CO-RPT-004 | Form 220 — annual income/withholding certificate | `CO-DIAN-004-Formulario220-Spec.xlsx` | ✓ |
| CO-RPT-005 | Format 2276 v4 — information return | `CO-DIAN-005-Formato2276-Spec.xlsx` | ✓ |
| CO-RPT-006 | Severance-savings annual deposit | `CO-CESANTIAS-006-ConsignacionAnual-Spec.xlsx` | ✓ |
| CO-RPT-007 | Disability-hiring contract report (MinTrabajo) | — | **Descoped** (HR-scope) |

CO-RPT-007 is properly descoped in `scope_manifest.json` with a descoping reason, client impact
(*"Refer to HRMS team"*) and `product_mapping_required: false`, alongside two further HR-scope
filings (SENA apprentice quota, RUAF-ND) and four not-payroll filings. Scope discipline is intact.

**However**, CCG Module 10's own scope note still directs the dev team to *"the Colombia Report
Specifications **CO-RPT-001 to CO-RPT-007** and the Statutory Integrations Register **CO-SIR-001 to
CO-SIR-007**"*. Neither a CO-RPT-007 spec nor any `CO-SIR-00n` register entry exists. See **MAJOR-03**.

---

### Check 4 — DD ↔ Report Specs, 4-bucket method: 94 of 94 (100%)

**563 spec field rows** across the six Sheet-4 specifications, classified by the `System Mapping`
token in column L:

| Bucket | Rows | Distinct tokens | Must be in DD? | Found in DD |
|---|---|---|---|---|
| **DD** — `Employee.*`, `Company.*`, `Contract.*` | 160 | **94** | **Yes** | **94 (100%)** |
| **CALC** — `Payroll.*`, `SUM(Payroll…)`, casilla/numeral arithmetic, cross-field derivations | 249 | — | No | correctly excluded |
| **SYS** — `Mercans.*`, `System.*`, `PayPeriod.*`, `Constant*`, `(system total)`, structural mirrors | 136 | — | No | correctly excluded |
| **TX/out-of-payroll** — `(employee declaration)`, `(client tax function)`, `(client accounts payable)` | 18 | — | No | correctly excluded |
| **Total** | **563** | | | |

**Score: 94 of 94 DD-bucket fields found in DD = 100% alignment.**

The 18 out-of-payroll rows (F220 casillas 61–73 other-income declarations and asset/debt statements,
F350 legal-person and self-withholding blocks, 2276 VAT limbs) all carry `Payroll Field = N` **and**
`Relevant for Payroll = N`, so they are correctly outside the DD bucket rather than silently omitted.

Per the check instruction, **no penalty** was applied for TX / CALC / SYS fields being absent
from the DD.

Reverse direction: 22 of the 115 DD fields carry no `Spec ref:` (Date of Birth, Gender, Nationality,
weekly hours, days per week, obligatory rest day, 36-hour shift flag, work modality, withholding
procedure, pension regime, severance regime, multi-employer flag, and 10 others). Each is a
CCG-Module-2-sourced calculation or configuration input that no *filing* carries — legitimately
DD-only, not orphaned.

The v1.1 **DD↔SPEC ALIGNMENT PATCH** is recorded in the change log of the DD and all six specs
(2026-09-07), covering option mappers, field naming and reverse references.

---

### Check 5 — Global WTC coverage audit

| Item | Value |
|---|---|
| Baseline file | `shared/Global_WTC_V1_0.xlsx` |
| Global codes in the baseline | **300** |
| **Global codes included in the Colombia WTC** | **300 (100.0%)** |
| **Global codes excluded** | **0** |
| Colombia-specific additions (`CO-` prefixed) | **102** |
| Total Wage Type Catalogue rows | **402** |

Verified programmatically after normalising the baseline's float-formatted codes: the intersection
is 300, the set difference is empty in both directions for the numeric range, and the WTC carries no
invented numeric codes outside the baseline.

**Coverage is genuine, not nominal.** Spot-checks confirm each global row was re-configured against
Colombian law rather than carried over:

- `62520` *Transportation allowance* → CB **No** / PL **No** / BB **Yes**, mapped to
  nómina electrónica `AuxilioTransporte (NIE071)`, with the CST art. 128 / Ley 21 de 1982 art. 17
  reasoning in column D.
- `62901` *Supplemental basic (13th/14th month)* → tax code `CO-TX-03`, CB No, PL No, quoting
  CST art. 307 verbatim (*"La prima anual no es salario…"*).
- `23640` *Pension contributions (employer)* → notes that the 12% is **never** relieved by the
  ET art. 114-1 exoneration and rounds **up** to the next multiple of 100 (PILA rule).
- `62990` *Stock options and grants* → taxable at exercise/vesting on the spread; IBC `Yes/No`
  against the 40% clamp.
- `21100`–`21190` deduction-mechanism series → `CO-NA`, every subjection column `NA`, with the
  CST art. 149 written-order and minimum-wage-floor constraint stated on each row.

**Colombia-specific expansion rationale (documented on the Global WTC Coverage sheet):** five
social-security subjection columns (Q–U) instead of one, because Colombia's eight mandatory
contributions across three insurance branches, three payroll levies and one employee-only
solidarity surcharge **do not share a base**; plus three Colombia-specific base columns (the hard
CST art. 127/128 salary flag demanded at *element level* by the paired `S`/`NS` XML element names,
the statutory-benefit base, and the CST art. 192 vacation base).

**Tax code legend (C9):** 10 codes `CO-TX-01` … `CO-TX-10` plus `CO-NA`, each with a meaning and an
official Colombian source. Assignment distribution: `CO-TX-01` 249, `CO-NA` 109, `CO-TX-06` 17,
`CO-TX-02` 9, `CO-TX-10` 8, `CO-TX-07` 5, `CO-TX-03` 2, `CO-TX-04`/`CO-TX-05`/`CO-TX-09` 1 each.
`CO-TX-08` (non-resident flat 20%) has **zero** assignments — see MINOR-09.

---

### Check 6 — Scope discipline

| Rule | Result |
|---|---|
| No calculated amounts in DD | **PASS** — zero amount-bearing fields; zero occurrences of SMMLV / UVT / ceiling values anywhere in the DD |
| No Base Salary in DD | **PASS** — contractual monthly salary, salary-in-kind valuation and all declared relief amounts are absent by design |
| No identification data in WTC | **PASS** — the 28 WTC columns are wage-type attributes only; the 8 `CO-FLAG-*` rows are calculation switches, not identifiers |
| No full field specs in CCG Module 2 | **PASS** — group-level summary table plus an explicit *"the authoritative, field-level list … is in CO-DD-001"* note. The document-format and combo-value tables are template-mandated question answers, not field specs |
| No full field specs in CCG Module 10 | **PASS** — explicit *"does not reproduce field-level specification content"* scope note |

One MINOR deviation: the DD's `Employee Document Type` mapper carries code **11** (Registro civil de
nacimiento) and its PILA/cesantías counterpart carries **CD**, **SC** and **PT**, none of which
appear in the manifest's `option_mapper_scope.personal_id_type` list of 10 in-scope codes — whose
`_comment` states *"Out-of-scope codes must be excluded from ALL artifacts."* See MINOR-03.

---

### Check 7 — Report Spec format compliance (per report)

| Spec | 9 sheets, exact order | Sheet 4: 21 cols A–U | Header FF4472C4 / white / bold | Row colours | Scope Summary green/red | Population Rules |
|---|---|---|---|---|---|---|
| CO-DIAN-001 Nómina Electrónica | ✓ | ✓ (225 rows) | ✓ 21/21 | amber 151 · blue 43 · grey 19 · red 5 · green 4 | ✓ 29 / 12 | ✓ 34 rows |
| CO-DIAN-002 Formulario 350 | ✓ | ✓ (69 rows) | ✓ 21/21 | amber 26 · blue 20 · red 13 · grey 7 | ✓ 23 / 16 | ✓ 28 rows |
| CO-PILA-003 PILA | ✓ | ✓ (170 rows) | ✓ 21/21 | amber 117 · blue 24 · grey 14 · red 9 · green 3 | ✓ 28 / 13 | ✓ 29 rows |
| CO-DIAN-004 Formulario 220 | ✓ | ✓ (75 rows) | ✓ 21/21 | amber 47 · red 12 · grey 7 · blue 6 | ✓ 28 / 12 | ✓ 28 rows |
| CO-DIAN-005 Formato 2276 | ✓ | ✓ (50 rows) | ✓ 21/21 | amber 32 · grey 7 · red 4 · blue 3 · green 1 | ✓ 28 / 13 | ✓ 30 rows |
| CO-CESANTIAS-006 Consignación | ✓ | ✓ (52 rows) | ✓ 21/21 | amber 19 · blue 15 · grey 6 · green 5 · red 4 | ✓ 25 / 19 | ✓ 20 rows |

- Sheet order is `Version Control · Report Matrix · Payroll Scope Summary · <Report> Spec ·
  File Structure · Field Options · Population Rules · Example Analysis · Sample File` in all six.
- Sheet 4 headers sit on row 2 (title row 1, spacer row 3), all 21 cells `FF4472C4` with
  `FFFFFFFF` bold font — 126 of 126 header cells compliant.
- Payroll Scope Summary uses `FFC6EFCE` green YES / `FFFFC7CE` red NO throughout, with the
  `FF1F4E78` dark-blue header row.
- Version Control change-log header row uses `FF4BACC6` teal per the standard.
- **Source status is honest per spec:** PILA is marked *PRIMARY, BYTE-EXACT* with field counts and
  position totals arithmetically verified (A1 = 34/567, A2R1 = 22/359, A2R2 = 97/686); Formato 2276
  is marked *DERIVED for the XML layout* because the técnicas annex is not held locally. No spec
  overclaims its sourcing.

Only F350 uses 4 of the 5 row colours (no fixed/constant rows exist in an aggregate return) —
see MINOR-12.

---

### Check 8 — v2.4 standards

| Artifact | Standard | Result |
|---|---|---|
| **CCG** | 13 official modules, exact titles, template Q&A H3 format | **PASS.** 14 H1 (Version Control + Modules 1–13) with exact standard titles; 38 H2 sub-sections; 160 H3, of which **108** are template question / deliverable headings — a 1:1 match to the 108 items in `shared/CCG_TEMPLATE_QUESTIONS.md` (95 verbatim, 13 paraphrased deliverables). 248 tables. |
| **DD** | CZ V2.0 format, blue columns only | **PASS.** All 8 CZ V2.0 sheets present in template order. Header fills match the template cell-for-cell (10 blue `FF4472C4` + 12 orange `FFFF9900`); `Country Fields` correctly starts at column B as the CZ template does. Orange system columns (Ordinal, Internal Code, Parent/Sub Group, Default Value, MSS/ESS permissions) are **left blank** — blue-columns-only rule respected. No Czech residue in Introduction or Instructions. |
| **WTC** | CZ V2.0 + Global WTC baseline + Form Reference Guide | **PASS.** 6 sheets: Version Control, Wage Type Catalogue (402 × 28), Employer Sick Pay (49 populated rows, the full incapacity cascade), Tax Credit (90 rows — correctly states Colombia has **no** tax credit and documents the three deduction/exempt-income classes instead), Global WTC Coverage (16 items + the tax-code legend), **Form Reference Guide (65 entries)**. |
| **Report Specs** | Spain 9-sheet, 21-column Sheet 4 | **PASS** — 6 of 6, see Check 7. |
| **Payslip** | 8-sheet Mercans standard, navy/grey palette, green net-pay | **PASS WITH PATCHES.** 8 sheets in the reference order; grey palette (`FFDCDCDC` / `FFA9A9A9` / `FFF5F5F5`) matches `REFERENCE_Payslip_Spain.xlsx` exactly. Wage-type codes are `XXXXX` placeholders (MAJOR-01); no navy header accent and no green net-pay fill (MINOR-06); CUNE / QR / generation date absent (MAJOR-02). |

**Payslip arithmetic — independently re-derived and correct:**

| Line | Formula | Value |
|---|---|---|
| Total earnings | 18,000,000 + 500,000 + 700,000 + 0 | 19,200,000 |
| Health 4% / Pension 4% / FSP 1% | on IBC 19,200,000 (below the 25-SMMLV cap 43,772,625; above the 4-SMMLV FSP trigger 7,003,620) | 768,000 / 768,000 / 192,000 |
| Retención en la fuente | ET arts. 383/388, re-derived above | 2,250,765 |
| **Net pay** (`I8` → `H34`) | `SUM(H21:J24) − SUM(H28:J31)` | **15,221,235** |
| YTD gross / EE contributions / tax / net (7 months) | 19,200,000 × 7 / 1,728,000 × 7 / 2,250,765 × 7 / difference | 134,400,000 / 12,096,000 / 15,755,355 / **106,548,645** ✓ |

YTD net ÷ 7 = 15,221,235 — exactly the monthly net, so the YTD block and the monthly block are
mutually consistent. Employer block (8.5 / 12 / 0.522 / 4 / 2 / 3 %) and provisions
(8.33 + 1 + 8.33 + 4.17 = **21.83%**) agree with the WTC's stated 21.8333% total. The
**cesantías / prima provisions correctly include** the transport-allowance line (H21:H24) while the
**vacation provision correctly excludes** it (H21:H23) — the CST art. 192 vs art. 253 distinction is
implemented, not glossed.

The Spanish sheet `Colombia (ES)` is fully translated (the six residual English-token matches are
Spanish–English cognates: *Pension*, *Base*, *Total*). This satisfies Resolution DIAN 000013 art. 26,
which makes Spanish mandatory and another language additive.

---

### Check 9 — v2.4 NEW: composite key / inter-field constraints

| Control | Result |
|---|---|
| **C13** — composite-key fields documented in Sheet 4 column M | **PARTIAL (4 of 6).** Cesantías 9 annotations, Nómina Electrónica 7, Formato 2276 5, Formulario 220 1. **PILA 0** and **F350 0**. F350 is correctly N/A (aggregate return, no per-employee key). PILA documents `T2R2-004` as a *"Join key to NIE045 / F220 casilla 25 / 2276 numeral 2"* but never labels the `T2R2-003 + T2R2-004` type+number pair as a composite key — see MINOR-02. |
| **C16** — conditional fields bidirectionally documented | **PASS — 100%.** 297 spec rows carry `Mandatory = C`; **all 297** have a populated `Conditional Reason` (column G). 53 DD fields are `CM`; **all 53** have a populated `Pre-Condition for Conditional Mandatory`. Additionally all 30 DD option mappers carry a `Referenced by …` reverse-reference. Zero omissions in either direction. |
| **C17** — Form Reference Guide present in WTC | **PASS.** 65 entries mapping wage-type category → spec file → sheet → row → notes. Validated mechanically: **0 broken pointers** — every target file exists, every sheet name resolves, every row number is in range. Two entries are honestly marked `DERIVED — no statutory filing` (benefit accruals; withholding-procedure election). |
| **C20** — scope decision audit trail complete | **PASS.** `scope_manifest.json` carries 13 in-scope / 11 out-of-scope employment types with a 300-word rationale and an inbound data contract; 6 in-scope filings each with legal basis, deadline, channel and rationale; 7 descoped filings each with `descoping_reason` + `client_impact` + `product_mapping_required`; 5 option-mapper scope lists; 14 numbered known gaps (`CO-GAP-01`…`CO-GAP-14`); 10 resolved items; 22 failure patterns checked with notes on F18–F22. |

---

## 3. Issues List

### MAJOR

**MAJOR-01 — Payslip wage-type codes are `XXXXX` placeholders; the payslip is not wired to the WTC**
*File:* `06-payslip/CO_Compliance_Payslip_Generator.xlsx`, sheets `Colombia (EN)` and `Colombia (ES)`,
rows 21–24, 28–31, 38–43, 48–51 (18 lines × 2 sheets = 36 cells).

Every line item reads `XXXXX - Basic Salary (Salario Basico)`, `XXXXX - Aporte a Pension - Empleado`,
and so on. The WTC contains 402 fully-configured codes including exact matches for all 18 lines
(`CO-SALARIO-BASICO`, `CO-DED-SALUD`, `CO-DED-PENSION`, `CO-DED-FSP-SOLIDARIDAD`,
`CO-RETENCION-FUENTE`, `CO-ER-SALUD`, `CO-ER-PENSION`, `CO-ER-ARL`, `CO-ER-CCF`, `CO-ER-SENA`,
`CO-ER-ICBF`, `CO-PROV-CESANTIAS`, `CO-PROV-INTERESES-CESANTIAS`, `CO-PROV-PRIMA`,
`CO-PROV-VACACIONES`).

*Impact:* the dev team cannot trace a payslip line back to a wage type, and the payslip↔WTC
alignment gate cannot be evidenced.

**Fix:** substitute the real WTC code into column A on both language sheets. Note that lines 22
(`Overtime & Surcharges`) and 23 (`Commissions & Bonuses`) each bundle multiple wage types — either
split them into their constituent codes or label them with an explicit multi-code list.

---

**MAJOR-02 — Payslip omits CUNE, generation date, payment date, document prefix/consecutive and the QR code, all of which CCG Module 10.3 lists as mandatory content**
*File:* `06-payslip/CO_Compliance_Payslip_Generator.xlsx` (whole workbook)

CCG Module 10.3 correctly establishes that Colombia has **no statutory payslip-content article**
(grep-tested across the consolidated CST for all seven Spanish terms, zero hits) and that the
operative itemisation rule is **Resolution DIAN 000013 of 2021 art. 5**, whose 13 mandatory items
apply to any graphical representation issued under art. 24. Grepping the entire payslip workbook
for `CUNE`, `QR`, `prefij`, `consecutiv`, `Fecha de generación` and `Generation date` returns
**zero hits** in all 8 sheets.

Mapped against art. 5:

| art. 5 item | Present |
|---|---|
| 1 Employer name + NIT | ✓ rows 7, 9 |
| 2 Employee name + document number | ✓ rows 12, 16 |
| 3 Document identification — consecutive number preceded by the authorised prefix | ✗ (only a static `REF-CO-2026` footer) |
| 4 Generation date | ✗ |
| 5 Payment or credit date | ✗ |
| 6 Accrued values, itemised | ✓ rows 21–25 |
| 7 Deducted values, itemised | ✓ rows 28–32 |
| 8 Total difference | ✓ row 34 |
| 9 Payment or credit period | Partial (`Tax Month` / `Days in Month`, no explicit period start/end) |
| 10 Payment method and medium | Partial (banking block, no payment-method code) |
| 11 Country, department, municipality of origin | Partial (free-text employer address) |
| 13 **CUNE** | ✗ |
| Technical Annex §13.1 QR code ≥ 2 cm on every page | ✗ |

*Impact:* if a client issues the graphical representation, the document as templated does not carry
the art. 5 content that art. 24 requires — and the CUNE + QR are precisely what make the paper
document traceable to the validated XML.

**Fix:** add a header block for `Prefijo + Consecutivo`, `Fecha de generación`, `Fecha de pago`,
`Período de pago (desde/hasta)`, `Forma y medio de pago`, `País / Departamento / Municipio de
origen`, a `CUNE` field, and a placeholder image anchor sized ≥ 2 cm × 2 cm for the QR. Reference
the DD fields that already exist for these (`Electronic Payroll Document Prefix`,
`Place of Work Country/Department/Municipality Code`, `Payment Form`, `Payment Method`).

---

**MAJOR-03 — CCG Module 10 scope note points the dev team to a CO-RPT-007 spec and a CO-SIR-001…007 register, neither of which exists**
*File:* `01-ccg/modules/m10_reporting.md` lines 5–8 (and the corresponding block in
`CO-CCG-001-v1.0.docx`, Module 10 preamble)

The note reads: *"For layouts, code tables, validation rules, XML paths and field-by-field detail,
see the Colombia Report Specifications **CO-RPT-001 to CO-RPT-007** and the Statutory Integrations
Register **CO-SIR-001 to CO-SIR-007**."*

Both ranges are wrong:

- **CO-RPT-007** (the MinTrabajo disability-hiring contract report) is deliberately **descoped** in
  `scope_manifest.json` as HR-scope, so no spec was built and none should be. Module 10's own
  summary table nevertheless lists CO-RPT-007 as a live obligation with **no out-of-scope marker**.
- **CO-SIR-001…007 do not exist in any form.** The register is `CO-SIR-INDEX-001-v1.0.docx`, an
  authority index over **4 authorities** (1 integrable, 3 manual), with a single runbook at
  `03-statutory-integrations/DIAN-NE/` organised as **7 phases** `P1`…`P7`. A grep of the SIR index
  for `CO-SIR-\d+` returns zero matches. The "007" appears to be a mis-transcription of the
  7-phase runbook structure.

*Impact:* a developer following the scope note will hunt for two non-existent artifact families and
will treat a descoped HR filing as in-scope. This is the highest-friction defect in the pack for
the receiving team.

**Fix:** amend the scope note to *"see the Colombia Report Specifications CO-RPT-001 to CO-RPT-006
and the Statutory Integration Register CO-SIR-INDEX-001 with the DIAN-NE configuration runbook
(phases P1–P7)"*, and add an explicit `OUT OF SCOPE — HR-scope, see scope_manifest` marker to the
CO-RPT-007 row of the Module 10.1 table.

---

### MINOR

**MINOR-01 — WTC Version Control carries un-cleaned CZ template residue**
`02-wtc/CO-WTC-001-v1.0.xlsx`, `Version Control` row 14: `2.0 | 2025-09-09 | Wage codes Mapping |
Released | Devshree Vyas`. Confirmed identical to row 14 of `shared/_CZ_Wage_Type_Catalogue_V2_0.xlsx`.
Row 13 was correctly overwritten with the Colombia entry (`1 | 2026-09-04 | … | Mercans Compliance`),
so the change log now reads v2.0 as *predating* v1.0 by a year. The DD's Version Control is clean,
which confirms this is a WTC-specific miss rather than a systemic template issue.
**Fix:** delete row 14, or replace it with the genuine v1.1 alignment-patch entry that the DD and all
six specs already carry.

**MINOR-02 — PILA spec does not label the contributor document type + number pair as a composite key (C13)**
`CO-PILA-003-…-Spec.xlsx`, `PILA Spec` rows 65–66 (`T2R2-003`, `T2R2-004`). Column M calls
`T2R2-004` a *"Join key"* but never states that type + number **together** form the record key —
even though `CO-CESANTIAS-006` annotates the identical pair as `COMPOSITE FIELD` at row 4.
**Fix:** add `COMPOSITE KEY: T2R2-003 + T2R2-004 …` to column M of both rows, matching the Cesantías
wording. (F350 needs no change — an aggregate return has no per-employee key.)

**MINOR-03 — DD document-type mappers carry codes the manifest declares out of scope**
`05-data-dictionary/CO-DD-001-v1.0.xlsx`, `Country Option Mappers` rows 5 (code `11`, Registro civil)
and 22/23/26 (`CD` Carné diplomático, `SC` Salvoconducto, `PT` PPT). The manifest's
`option_mapper_scope.personal_id_type` lists 10 in-scope codes excluding `11`, and its `_comment`
states out-of-scope codes must be excluded from **all** artifacts. In mitigation, the DD annotates
each (`"Under-7s; never an employee"`, `"CESANTIAS XLS LAYOUT ONLY"`) rather than presenting them as
usable, and `CD`/`SC`/`PT` are genuinely in the published PILA and cesantías catalogues.
**Fix:** either add these four to the manifest's in-scope list as *reference-only catalogue values*,
or add a `REFERENCE ONLY — NOT IN SCOPE` prefix to their DD constraint notes. The manifest and DD
must agree either way.

**MINOR-04 — CCG Module 4.6 table contradicts its own 40%-clamp narrative for two rows**
`01-ccg/modules/m04_compensation.md` line 814 table: *Occasional gratuity* and *Employer-paid prepaid
health premium* both show **CB = No** flat. But the same module (lines 330, 345, 766–776) states that
Law 1393 of 2010 art. 30 forces **any** non-salary payment above 40% of total remuneration back into
the contribution base, and the *Extra-statutory bonus* row in the same table correctly says
*"Only above the 40% clamp"*. The WTC is the more accurate artifact here: `CO-GRATIF-OCASIONAL` and
`CO-MEDICINA-PREPAGADA-ER` both carry `Yes/No` on columns Q/R/S/U with the clamp reasoning in
column D. **This is a CCG-side simplification, not a CCG↔WTC conflict.**
**Fix:** change both rows' CB cell to `Only above the 40% clamp` for consistency with the WTC and
with Module 4.6's own narrative.

**MINOR-05 — Payslip vacation provision base includes the bundled overtime line**
`Colombia (EN)`/`(ES)` cell `H51`: `=ROUND(SUM($H$21:$H$23)*0.0417,0)`. Row 22 is
`Overtime & Surcharges (Horas Extra y Recargos)`. Per CST art. 192 — and per WTC column X, which sets
`CO-HED`/`CO-HEN`/`CO-RECARGO-DOMINICAL` to vacation base **No** while `CO-RECARGO-NOCTURNO` is
**Yes** — overtime and rest-day work must be excluded from the vacation base while the night premium
is included. The bundled demo line makes the two inseparable.
**Fix:** split row 22 into an overtime line (excluded from H51) and a premium line (included), so the
vacation base honours art. 192.

**MINOR-06 — Payslip lacks the navy header accent and green net-pay fill**
The `Colombia (EN)`/`(ES)` sheets use only the grey family (`FFDCDCDC`, `FFA9A9A9`, `FFF5F5F5`).
This **matches `shared/REFERENCE_Payslip_Spain.xlsx` exactly**, which itself has no navy and no green,
so the build faithfully mirrors the reference. The v2.4 check nonetheless calls for a navy/grey
palette with a green net-pay highlight.
**Fix (cosmetic):** apply `FF1F4E78` navy to the section header rows (19, 27, 36, 46, 54, 58, 65, 71)
and `FFC6EFCE` green to `A34:H34`. Consider raising the same change against the shared Spain
reference so the standard and the reference stop disagreeing.

**MINOR-07 — Sheet 4 column headers deviate in wording from the standard on 5 of 21 columns**
All six specs use `Record Type` (std. `Record Type / Section`), `Position (in file)` (std.
`Position (Start-End)`), `Length` (std. `Field Length`), `Explanation` (std. `Field Explanation`) and
`Frequency` (std. `Reporting Frequency`). Semantics, order and count are correct; only the labels
differ. Consistent across all six, so harmless in practice.
**Fix:** align the five labels to `shared/report-spec-template/REPORT_SPEC_STANDARD_FORMAT.md`, or
record the Colombia wording as an accepted variant.

**MINOR-08 — Spec Version Control change-log column order differs from the template**
All six specs use `Version | Effective Date | Status | Change Description | Updated By`; the template
(`ES-M296-001`) uses `Version | Effective Date | Change Description | Status | Updated By`. Teal
`FF4BACC6` header fill is correct.
**Fix:** swap columns C and D, or accept as a variant.

**MINOR-09 — Tax code `CO-TX-08` is defined in the legend but assigned to zero wage types**
`02-wtc/CO-WTC-001-v1.0.xlsx`, `Global WTC Coverage` row 28 defines `CO-TX-08` (non-resident flat 20%
on gross, ET art. 408) with a full citation chain including DIAN Concepto 011108 of 29 June 2026.
No row in the 402-row catalogue carries it — non-residency is instead handled as a per-employee
overlay through column P (*Special Tax*).
**Fix:** add a note to the legend entry stating that `CO-TX-08` is a residency-driven overlay applied
via column P rather than a per-wage-type assignment, so a reader does not read the zero count as an
omission.

**MINOR-10 — Spec Sheet 4 column L carries no WTC code for amount-bearing fields**
`System Mapping` uses `Payroll.*` tokens (`Payroll.Transport_Allowance`, `Payroll.Prima_Amount`,
`Payroll.Commission`, `Payroll.Income_Tax_Withheld`, …). The WTC→spec direction is fully covered by
the 65-entry Form Reference Guide, but the spec→WTC direction is not: a developer mapping
`NIE071` has no WTC code in front of them.
**Fix:** append the WTC code to column L for amount fields, e.g.
`Payroll.Transport_Allowance [WTC: CO-AUX-TRANSPORTE / 62520]`.

**MINOR-11 — Active-pensioner flag has no discrete DD field**
CCG Module 2 lists it as a social-security profile field and the WTC defines
`CO-FLAG-PENSIONADO-ACTIVO`, but the DD carries it only through `Worker Sub-Type = 01`. The manifest's
`inbound_data_contract` also names it explicitly among the per-employee inputs the engine must
receive. Functionally covered; formally under-specified.
**Fix:** either add an `Active Pensioner Flag` row to `Country Fields`, or add a note to
`Worker Sub-Type` confirming it is the sole carrier of the flag.

**MINOR-12 — F350 Sheet 4 uses 4 of the 5 standard row colours**
No `FFC6EFCE` green (fixed/constant) rows, because Formulario 350 is an aggregate return with no
constant-valued fields. Expected and harmless.
**Fix:** none required; noted for completeness so the colour-count check is not read as a miss.

---

## 4. Global WTC Coverage Summary

| Metric | Value |
|---|---|
| Baseline | `shared/Global_WTC_V1_0.xlsx` (300 codes) |
| **Included in the Colombia WTC** | **300** |
| **Excluded** | **0** |
| **Coverage** | **100.0%** |
| Colombia-specific additions | 102 (`CO-` prefixed) |
| Catalogue total | 402 rows × 28 columns |

**Exclusion reasons:** none — no global code was dropped. Every one was re-configured against
CO-CCG-001 Modules 3–10, the six report specs, and the primary law held in
`00-official-sources/pdfs/` (CST Decreto 2663 de 1950, Ley 100 de 1993, Ley 797 de 2003,
Ley 1393 de 2010, Ley 21 de 1982, Ley 2466 de 2025, ET Decreto-Ley 624 de 1989, Decreto 0223 de 2026).

**Colombia-specific additions, by category:**

| Category | Count |
|---|---|
| Earnings (core pay, six premium hour types, statutory benefits, leave cascade, termination heads) | 55 |
| Employee deductions | 19 |
| Employer contributions and accruals | 11 |
| Calculation bases | 5 |
| Configuration flags | 8 |
| Taxes | 2 |
| Rates / percentages | 2 |
| Intermediary / notional | 2 |
| **Total** | **102** (of which 8 flags + 5 bases + 2 rates + 2 notional = 17 non-monetary) |

Catalogue-wide category distribution: Earning 295 · Deduction 71 · Employer Contribution 16 ·
Flag 8 · Base 5 · Percentage 3 · Tax 2 · Intermediary 1 · Notional 1.

**Egypt F20 guard:** satisfied. Commission is a first-class wage type (`CO-COMISIONES`) with its own
nómina electrónica element `Comision (NIE155)`, and the global commission-bearing codes are
configured rather than dropped. Every tax code in the catalogue is defined in the legend with an
official Colombian source.

**Documented DERIVED flag:** the Mercans code numbers for the 102 Colombia-specific rows are DERIVED —
no numeric Mercans range has been assigned for Colombia, so mnemonic `CO-` codes are used and must be
renumbered at system-configuration time. This is disclosed on the Global WTC Coverage sheet rather
than presented as final.

---

## 5. v2.4 Compliance Summary

| Requirement | Status |
|---|---|
| CCG — 13 official modules, exact titles | ✅ 14 H1 (Version Control + Modules 1–13) |
| CCG — template Q&A format (H3 headings) | ✅ 108 of 108 template questions/deliverables as H3 |
| CCG — no field-level specs in Modules 2 and 10 | ✅ explicit scope notes in both |
| DD — CZ V2.0 format | ✅ all 8 sheets, template order, header fills cell-exact |
| DD — blue columns only | ✅ 12 orange system columns left blank |
| DD — no amounts, no Base Salary | ✅ zero amount fields; zero fiscal parameters |
| WTC — CZ V2.0 structure | ✅ 6 sheets (Employer Sick Pay + Tax Credit both populated with Colombia content) |
| WTC — Global WTC baseline | ✅ 300/300, 0 excluded, all re-configured |
| WTC — Form Reference Guide sheet | ✅ 65 entries, 0 broken pointers |
| WTC — no identification data | ✅ wage-type attributes only |
| Report Specs — Spain 9-sheet format | ✅ 6/6, exact sheet names and order |
| Report Specs — 21-column Sheet 4 A–U | ✅ 6/6, 126/126 header cells `FF4472C4`/white/bold |
| Report Specs — row colour coding | ✅ 6/6 (F350 uses 4 of 5, legitimately) |
| Report Specs — Payroll Scope Summary green/red | ✅ 6/6 |
| Report Specs — Population Rules completed | ✅ 6/6 (20–34 rules each) |
| Payslip — 8-sheet Mercans standard | ✅ 8 sheets, reference order |
| Payslip — navy/grey palette | ⚠️ grey only (matches Spain reference) — MINOR-06 |
| Payslip — green net-pay | ⚠️ absent — MINOR-06 |
| Payslip — WTC codes wired | ❌ `XXXXX` placeholders — MAJOR-01 |
| **C13** — composite keys in Sheet 4 column M | ⚠️ 4 of 6 (F350 N/A; PILA gap) — MINOR-02 |
| **C16** — conditional fields bidirectional | ✅ 297/297 spec + 53/53 DD + 30/30 mappers |
| **C17** — Form Reference Guide in WTC | ✅ present and pointer-validated |
| **C20** — scope decision audit trail | ✅ complete (13/11 employment types, 6/7 filings, 14 gaps, 22 failure patterns) |
| **C2** — newest-law check | ✅ Ley 2381 de 2024 correctly excluded (Sentencia C-264 de 2026, 25 Aug 2026; art. 94 entry-into-force) |
| **C3** — Yes/No entries justified | ✅ 246/246 with column-D reasoning |
| **C9** — every tax code defined and sourced | ✅ 11 codes, all with Colombian authority citations |
| **C19** — no invented field codes | ✅ NIE/NIAE, A1/T2R1/T2R2, casilla and numeral prefixes all pattern-verified against primary sources |

---

## 6. Notable Strengths

Recorded because they are unusual and worth carrying to other countries:

1. **The 2026 mid-year cut-overs are dual-dated, not simplified.** The rest-day premium
   (80% → 90% on 1 Jul 2026 → 100% on 1 Jul 2027) and the hourly divisor (220 → 210 on 15 Jul 2026)
   are encoded with both values and both dates in every affected WTC formula, including the three
   compounded rest-day overtime codes, and the WTC explicitly warns that the nómina electrónica
   annex's legacy `75/100/150/110` literals **must not** be configured.
2. **The minimum-wage litigation is handled correctly.** Decreto 1469 de 2025 (COP 1,750,905) was
   provisionally suspended by the Council of State on 12 Feb 2026 and re-fixed by Decreto 0159 de
   2026. The CCG traces the sequence and concludes — correctly — that the *amount* was continuously
   in force from 1 Jan 2026 and was never in doubt. Every artifact uses 1,750,905 consistently.
3. **The one-calibre discipline.** Minimum wage governs social security and labour thresholds; UVT
   governs every tax threshold. The Tax Credit sheet states the rule explicitly and no artifact
   mixes them.
4. **Honest integration posture.** The SIR verdict states plainly that Colombia is a
   *one-integration* country — 1 of 4 authorities and 1 of 6 filings are machine-to-machine — and
   scores the ARUS/SuAporte "APIS PILA" commercial offering as `integration = false` after fetching
   the developer portal and finding no catalogue, endpoints, OpenAPI or WSDL. The DIAN M2M channel
   was verified live (both WSDLs HTTP 200, `SendNominaSync` declared, Caja de Herramientas ZIP
   downloaded with the XSD v1.0.6 set).
5. **Defects in official sources are recorded rather than propagated.** The pack documents the
   MinTrabajo Circular 101 de 2025 §5.1 rest-day-premium error, the ARL class-IV rate defect in
   Decreto 1607, the `Trabajador/@NumeroDocumento` `xsd:integer` typing that no passport can satisfy,
   the required-`SegundoApellido` attribute that most foreign nationals cannot populate, the missing
   PPT document-type code (`CO-GAP-06`), the Ley 2466 art. 15 two-paragraphs-announced /
   three-enacted discrepancy, and the cesantías operator's own transport-allowance calculator bug.

---

## 7. Readiness Verdict

### **NEEDS PATCHES**

**Score 94/100 · 0 CRITICAL · 3 MAJOR · 12 MINOR**

The compliance content is dev-ready. Every calculation this review re-derived independently came out
exact, all five structural alignment gates pass at 97–100%, and the two hardest Colombian 2026
questions — the mid-year premium/divisor steps and the suspended minimum-wage decree — are answered
correctly and consistently across all seven artifacts.

The three MAJOR findings are wiring and cross-reference defects, not compliance errors, and are
confined to two files:

| Priority | Fix | File | Effort |
|---|---|---|---|
| 1 | Replace 36 `XXXXX` placeholders with real WTC codes (MAJOR-01) | payslip generator | ~1 h |
| 2 | Add the art. 5 header block, CUNE field and QR anchor (MAJOR-02) | payslip generator | ~2 h |
| 3 | Correct the `CO-RPT-001…007` / `CO-SIR-001…007` scope note and mark CO-RPT-007 out of scope (MAJOR-03) | `m10_reporting.md` + CCG docx rebuild | ~30 min |
| 4 | Delete the CZ template residue row (MINOR-01), label the PILA composite key (MINOR-02), reconcile the document-type mapper scope (MINOR-03), fix the two CCG 4.6 clamp rows (MINOR-04), split the bundled overtime line (MINOR-05) | WTC, PILA spec, DD, CCG, payslip | ~2 h |

**Recommendation:** apply MAJOR-01 through MAJOR-03 and MINOR-01 through MINOR-05, then re-run this
cross-check. On that basis the pack moves to **READY FOR DEV TEAM**. MINOR-06 through MINOR-12 are
cosmetic or standard-alignment items that can ship as-is with the deviations recorded; MINOR-06 in
particular should be raised against the shared Spain payslip reference rather than fixed only in
Colombia, since the reference itself does not meet the navy/green criterion.

---

*Artifacts reviewed: `01-ccg/CO-CCG-001-v1.0.docx` (14 H1 / 38 H2 / 160 H3 / 248 tables) and its 13
module sources · `02-wtc/CO-WTC-001-v1.0.xlsx` (6 sheets, 402 × 28) ·
`03-statutory-integrations/CO-SIR-INDEX-001-v1.0.docx` + `integration-landscape.json` + the DIAN-NE
runbook (P1–P7) · `04-reports-spec/` (6 specs × 9 sheets, 563 Sheet-4 field rows) ·
`05-data-dictionary/CO-DD-001-v1.0.xlsx` (8 sheets, 115 fields, 30 mappers) ·
`06-payslip/CO_Compliance_Payslip_Generator.xlsx` (8 sheets) · `scope_manifest.json` (v1.0) ·
`shared/Global_WTC_V1_0.xlsx` (300 codes) · `shared/CZ_Data_Dictionary_V2_0.xlsx` ·
`shared/_CZ_Wage_Type_Catalogue_V2_0.xlsx` · `shared/REFERENCE_Payslip_Spain.xlsx` ·
`shared/report-spec-template/` · `shared/CCG_TEMPLATE_QUESTIONS.md`.*
