# Colombia - QA Cross-Check, Known Limitations and Open Items - COMPLETE REFERENCE

**Sources reproduced in full below:**
- `07-qa-crosscheck/CO-QA-REPORT.md` - the stage-07 QA cross-check (2026-09-07)
- `scope_manifest.json` - the 14 numbered known gaps `CO-GAP-01`...`CO-GAP-14` and the 10 items resolved in
  this pass
- `07-qa-crosscheck/CO-ALIGNMENT-PATCH.md` - the mandatory DD-to-spec alignment patch (v1.1, 2026-09-07)
- `07-qa-crosscheck/handover_status.md` - the pre-submission audit gate verdict

**Headline verdict: 94 / 100 - PASS WITH PATCHES (`NEEDS PATCHES`) - 0 CRITICAL - 3 MAJOR - 12 MINOR.**
The compliance *content* is dev-ready; the three MAJORs are wiring and cross-reference defects in two files
(the payslip generator and CCG Module 10), not calculation errors.

---

## Quick index of open items by artifact

| Artifact | Open items |
|---|---|
| **Payslip** (`06-payslip.md`) | **MAJOR-01** `XXXXX` wage-type placeholders (36 cells) - **MAJOR-02** no CUNE / QR / generation date / payment date / prefix+consecutive - MINOR-05 vacation base includes bundled overtime - MINOR-06 no navy header / green net-pay fill - `Unit Rate Details` account codes are illustrative placeholders `[VERIFY WITH RA]` |
| **CCG** (`01-ccg.md`) | **MAJOR-03** Module 10 scope note cites a non-existent `CO-RPT-007` spec and `CO-SIR-001...007` register; CO-RPT-007 row not marked out of scope - MINOR-04 Module 4.6 table contradicts its own 40%-clamp narrative on two rows |
| **WTC** (`02-wtc.md`) | MINOR-01 CZ template residue in Version Control row 14 - MINOR-09 `CO-TX-08` defined but assigned to zero rows (by design - column-P overlay) - 4 substantive OPEN ITEMS (sick-pay rate, incapacity floor, high-risk pension rate, monthly apportionment of annual UVT caps) |
| **DD** (`05-data-dictionary.md`) | MINOR-03 four document-type codes the manifest declares out of scope (`11`, `CD`, `SC`, `PT`) - MINOR-11 active-pensioner flag has no discrete field (carried by `Worker Sub-Type = 01`) - option-mapper count 35 in the file vs 30 in the QA report `[VERIFY WITH RA]` |
| **Report specs** (`04-reports-spec.md`) | MINOR-02 PILA composite key not labelled - MINOR-07 five Sheet-4 column labels vary from the standard - MINOR-08 Version-Control column order - MINOR-10 column L carries no WTC code for amount fields - MINOR-12 F350 uses 4 of 5 row colours (legitimate) - **all 563 Sheet-4 rows carry `Query to RA` = *Pending RA review*** |
| **SIR** (`03-sir.md`) | 2 open questions in the landscape (below) - per-tenant secrets (`SoftwareID`, PIN, ONAC X.509) are issued at habilitacion and cannot pre-exist a client engagement |

## The four substantive OPEN ITEMS carried in the WTC (engine defaults, all configurable)

| # | Item | Position | Mercans default |
|---|---|---|---|
| 1 | **Rate for the employer's first two days of general-illness incapacity.** Decreto 2943 de 2013 art. 1 (compiled at Decreto 780 de 2016 art. 3.2.1.10) allocates days 1-2 to the employer but **does not state the rate**. CST art. 227 sets the *auxilio* at two thirds for the first 90 days; market practice applies 66.67% on that basis, a minority pays 100%. | `CO-INCAP-EG-EMPLEADOR` | **66.67%**, configurable |
| 2 | **Minimum-wage floor on incapacity payments.** Where 66.67% of salary falls below one SMMLV (1,750,905), market practice and settled administrative doctrine top the payment up to one minimum wage. The primary regulatory source was **not retrieved**. | incapacity cascade | **apply the floor**, configurable |
| 3 | **Additional employer pension contribution for Decreto Ley 2090 de 2003 high-risk activities.** The Resolucion 2388 rate table implies +10 pp employer-borne (26% total vs 16% standard); the 2026 rate and base are **not confirmed from a primary regulatory source** (`CO-GAP-02`). | `AltoRiesgoPension` | read from the Res. 2388 table; **DERIVED** |
| 4 | **Monthly apportionment of the ANNUAL 790-UVT and 1,340-UVT tax caps.** Both caps are stated annually while withholding is monthly. No regulation prescribes the apportionment expressly. | ET arts. 206 num. 10, 388 | **one twelfth** - 65.8333 UVT (3,447,955) and 111.6667 UVT (5,848,430), configurable |

---

# Part A - CO-QA-REPORT.md (verbatim, in full)


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


---

# Part B - Known gaps and resolved items (`scope_manifest.json` v1.0, verbatim)

Every gap below is a **disclosed limitation**, not a silent omission. Treat each as a live
`[VERIFY WITH RA]` item.

## B.1 The 14 numbered known gaps


### CO-GAP-01 - PILA Registro Tipo 2 (per-contributor settlement record) byte-exact field positions

- **status:** Field names and purposes captured from Resolucion MSPS 2388 de 2016 Anexo Tecnico 2; the complete field-by-field position/length table was NOT extracted this pass. Archivo Tipo 1 (34 fields, 567 positions) and Archivo Tipo 2 Registro Tipo 1 (22 fields, 359 positions) ARE byte-exact.
- **action:** Extract the Registro Tipo 2 table from the primary source and from the chosen operador de informacion's technical guide before any productive PILA layout is configured.

### CO-GAP-02 - AltoRiesgoPension additional employer pension contribution rate and base for 2026

- **status:** Decreto Ley 2090 de 2003 establishes the high-risk activities and the nomina electronica XML carries a required AltoRiesgoPension flag. The Resolucion 2388 de 2016 rate table shows a TOTAL pension rate of 26% for a high-risk contributor against the standard 16%, implying an additional 10 points borne by the employer, but the 2026 confirmation and the precise base were not obtained from a primary regulatory source.
- **action:** Verify against the current implementing decree before configuring any high-risk employee.

### CO-GAP-03 - Rate for the employer's first two days of general-illness incapacity

- **status:** Decreto 2943 de 2013 art. 1 (compiled at Decreto 780 de 2016 art. 3.2.1.10) allocates days 1-2 to the employer but does not state the rate. CST art. 227 sets the auxilio at two thirds for the first 90 days. Mercans default: 66.67%, configurable.
- **action:** Configurable per client; document the client's election.

### CO-GAP-04 - Minimum-wage floor on incapacity payments

- **status:** Market practice and settled administrative doctrine top incapacity payments up to one minimum wage where 66.67% of salary falls below it. The primary regulatory source was not retrieved this pass. Mercans default: apply the floor, configurable.
- **action:** Verify the primary source; keep configurable.

### CO-GAP-05 - Monthly apportionment of the 790-UVT and 1,340-UVT ANNUAL caps

- **status:** Both caps are stated annually while withholding is monthly. Market practice, which Mercans follows, apportions at one twelfth per month (65.8333 and 111.6667 UVT). No regulation prescribes the apportionment expressly.
- **action:** Configurable; document the client's election.

### CO-GAP-06 - No nomina electronica document-type code for the PPT (Permiso por Proteccion Temporal)

- **status:** The PPT was created by Decreto 216 de 2021, one month AFTER the Anexo Tecnico v1.0 of 11 February 2021, and is now held by the large majority of regularised Venezuelan migrants. Code 47 (PEP) is its legally superseded predecessor and the only available proxy. The annex is still at version 1.0.
- **action:** Use code 47 as the proxy and flag to the client; monitor for an annex update.

### CO-GAP-07 - XSD type constraints that conflict with real-world data

- **status:** Trabajador/@NumeroDocumento is typed xsd:integer, so a passport or foreign ID containing letters cannot be schema-valid (document types 21, 41, 42, 50). Trabajador/@SegundoApellido is use=required, yet many Colombians and virtually all foreign nationals have only one surname. No official workaround is published for either.
- **action:** Emit a placeholder for the second surname; escalate the alphanumeric document-number case to DIAN per client.

### CO-GAP-08 - 2026 minimum-wage decree is subject to a pending annulment action on the merits

- **status:** Decreto 1469 de 2025 (COP 1,750,905, +23%) was provisionally suspended by the Consejo de Estado on 12 February 2026 in proceeding 11001-03-25-000-2026-00004-00; the Government complied with Decreto 0159 de 19 February 2026 re-fixing the identical amount transitorily; on 9 July 2026 the Consejo de Estado REVOKED the suspension, so Decreto 1469 de 2025 recovered full force and is the operative instrument. The amount COP 1,750,905 has never been in dispute. The merits action remains pending.
- **action:** Cite Decreto 1469 de 2025 as operative; re-verify before any 2027 cut-over.

### CO-GAP-09 - Legal weight of MinTrabajo Circular Externa 101 de 22-09-2025 (the 220 -> 210 hourly divisor)

- **status:** The divisor table was read VERBATIM from the primary circular PDF this pass (page 10): 15 Jul 2023 = 235, 15 Jul 2024 = 230, 15 Jul 2025 = 220, 15 Jul 2026 = 210. The sourcing concern from earlier passes is CLOSED. The remaining caveat is that a ministerial circular is administrative doctrine, not statute, and the divisor is judicially untested.
- **action:** Configure 220/210 with the 15 July 2026 cut-over; monitor for judicial challenge.

### CO-GAP-10 - Formulario 350 prescribed form image (Resolucion DIAN 000031 de 2024 annex)

- **status:** The deadline table, the rounding rule (ET art. 577) and the natural-person / legal-person split ARE verified. The field-by-field form layout was not retrieved.
- **action:** Retrieve the annex before configuring a productive Form 350 layout.

### CO-GAP-11 - Law 2381 of 2024 pension reform - 2027 change control, NOT a 2026 configuration item

- **status:** Law 2381 de 2024 replaces the Ley 100 de 1993 two-regime pension architecture with a pillar system. Its own art. 94 set entry into force at 1 July 2025, but Constitutional Court Auto 841 of 18 June 2025 SUSPENDED that entry into force (sparing only arts. 12 and 76) and ordered the Camara de Representantes to re-run the fourth plenary debate. Judgment C-264 of 25 August 2026 (case D-15989) then upheld art. 94 on the understanding that the validated provisions take effect 1 APRIL 2027, upheld over 80 articles against the procedural challenge, and returned nine provisions to the Camara for a cured debate: art. 11 inciso 4, art. 14, art. 19 literal k, art. 23 paragrafo transitorio, art. 36, art. 63 inciso 2, art. 84 num. 5, art. 92 inciso 1 and art. 93. CONSEQUENCE: every 2026 pay period runs on Ley 100 de 1993 as amended by Ley 797 de 2003. No part of Law 2381 is live for 2026 and none is configured. Documented in CCG Module 5.1 (newest-law check) with the full FY2026-vs-2027 comparison.
- **action:** Treat as a 1 April 2027 change-control item, not a 2026 gap. Before the cut-over: (a) re-read art. 19 literal k after the cured Camara debate, since the 2.3-minimum-wage routing between the prima media and individual-savings components sits in a returned provision; (b) re-cut the solidarity-fund deduction from the current 1.0% + 0.2%-1.0% two-account bands to the single five-band 1.5%/1.8%/2.5%/2.8%/3.0% scale of art. 20 nums. 1-5; (c) add a per-employee transition flag for the art. 75 grandfathering at 750 weeks (women) / 900 weeks (men). The 16% total, the 12%/4% split (expressed by art. 20 as 75%/25% of the total) and the 25-minimum-wage ceiling are UNCHANGED, so those need no rework.

### CO-GAP-12 - Whether every licensed operador de informacion accepts the same 258-position cesantias record

- **status:** The layout is published by Simple S.A. and the channel is confirmed independently by ACH Colombia (SOI), but SOI publishes its own column layout only inside the upload screen, behind an authenticated session. Aportes en Linea, Asopagos, Enlace Operativo and MiPlanilla were not verified. The Fondo Nacional del Ahorro's employer instructivo, which as a state entity would be the one genuinely official schema for this filing, is no longer retrievable - its published URL (fna.gov.co/empleadores/.../INSTRUCTIVO ARCHIVO PLANO ENTIDADES PRIVADAS.pdf) returns 404 after the FNA site redesign. Also unstated in the source: the code page and the line terminator.
- **action:** Confirm the layout against one real accepted filing per client operator before a productive run; retry the FNA instructivo through the redesigned site.

### CO-GAP-13 - The 8.33% monthly advance deposit of cesantias is not yet operable

- **status:** Ley 2466 de 2025 art. 64 par. 1 is IN FORCE and permits it, but routes it through PILA and instructs MinSalud to regulate. As at 4 September 2026 the implementing decree is still a MinTrabajo DRAFT (proyecto amending Decreto 1072 de 2015 arts. 2.2.1.3.1, 2.2.1.3.4, 2.2.1.3.5 and 2.2.1.3.13, held at 00-official-sources/pdfs/proyecto_decreto_cesantias_2026.pdf). That draft would give MinSalud six months from its entry into force to adjust PILA, and then the fondos and operadores a FURTHER six months to build; no PILA tipo de cotizacion for cesantias exists yet. The annual planilla therefore remains the only lawful route. The draft also confirms two rules that survive regardless: the definitive annual consolidation on the average-of-the-year base, and mora running from 15 February.
- **action:** Build the fields but keep the feature switched OFF (Spec fields MA01-MA05, all flagged DRAFT). Monitor for the enacted decree AND the MinSalud PILA resolution; when both land, add a contribution type to the CO-PILA-003 Spec.

### CO-GAP-14 - Ley 2466 de 2025 art. 15 announces two paragraphs but enacts three

- **status:** The enacting formula of art. 15 reads 'adicionese ... los paragrafos 2 y 3 del articulo 57 del Codigo Sustantivo del Trabajo', yet the published text prints a Paragrafo 4 - the one making proven direct payment of cesantias discharging. Verified against the local Ley_2466_de_2025.pdf. The substance is not in doubt and the CCG citation (CST art. 57 par. 4, added by Ley 2466 de 2025 art. 15) matches the printed text, but the internal inconsistency should be expected to be raised.
- **action:** Cite CST art. 57 par. 4 as added by Ley 2466 de 2025 art. 15 and note the drafting discrepancy where challenged. No engine impact.

## B.2 Items RESOLVED in this pass (10)


1. Q-3 / D-4 RESOLVED: the conflict between the nomina electronica Anexo Tecnico section 5.5.5 (which hard-codes the pre-reform dominical percentages 100/75/150/110) and the Ley 2466 de 2025 schedule of 80%/90%/100% is settled by DIAN CONCEPTO 013840 (int. 1568) of 1 October 2025: the annex percentage 'debe leerse en consonancia con la normatividad vigente para cada caso especifico', and the coexistence of differentiated percentages within one month 'no constituye obstaculo alguno' to generation, transmission or validation. The engine reports the REAL statutory percentage.

2. Q-5 RESOLVED: apprentices are fully specified. Ley 2466 de 2025 art. 21 (substituting CST art. 81) makes the apprenticeship a SPECIAL FIXED-TERM LABOUR CONTRACT governed by the Labour Code, max 3 years. Apoyo de sostenimiento: dual training 75% SMMLV year 1 and 100% year 2; traditional training 75% in the lectiva phase and 100% in the practical phase; university students never below 100%. Classroom phase: health and occupational risk only, fully employer-paid, as a dependiente. Practical or dual phase: full integral social security plus ALL prestaciones, auxilios and other labour-contract rights. Decreto 0223 de 5 March 2026 art. 2.2.6.3.3.4 par. 2: the IBC must in every case be at least 1 SMMLV. Art. 2.2.6.3.3.6 par. 1: parafiscales are payable in the practical/dual phase, with the ET art. 114-1 exoneration applicable.

3. Q-10 SUBSTANTIALLY CLOSED: the PILA file structure is now sourced from Resolucion MSPS 2388 de 2016 Anexo Tecnico 2 - Archivo Tipo 1 (34 fields, 567 positions) and Archivo Tipo 2 Registro Tipo 1 (22 fields, 359 positions) byte-exact, the full planilla-type list (E, Y, A, I, S, M, N, T, F, J, X, U, K, H, O, Q, B, D, Z) and the novedad mnemonics (ING, RET, TDE/TAE, TDP/TAP, VSP/VST, SLN, IGE, LMA, VAC-LR, IRL, AVP, VCT) VERIFIED from a primary source rather than practitioner knowledge. Only Registro Tipo 2 positions remain open - see CO-GAP-01.

4. Q-19 SOURCING CLOSED: the 220 -> 210 divisor table was read verbatim from the primary MinTrabajo Circular Externa 101 de 2025 PDF, not from a compilation mirror.

5. Q-24 RESOLVED: Ley 2381 de 2024 (pension reform) is NOT in force for any part of fiscal year 2026. The Corte Constitucional, by SENTENCIA C-264 DE 2026 delivered 25 August 2026, declared the great majority of the law exequible on procedural grounds and returned nine points to the Camara de Representantes; it declared art. 94 exequible on the understanding that the upheld provisions ENTER INTO FORCE ON 1 APRIL 2027. The Ley 100 de 1993 architecture (16% total pension, 12%/4% split, Fondo de Solidaridad Pensional, 25-SMMLV ceiling, RPM/RAIS election) governs the whole of 2026.

6. NEW FINDING, corrects earlier Colombia material: NON-RESIDENT employees are withheld at the FLAT 20% of ET art. 408, not under the ET art. 383 progressive table, until they acquire tax residence under ET art. 10. DIAN CONCEPTO 011108 of 29 June 2026 (published 3 July 2026), confirming Concepto 1789 int. 14595 of 2025, expressly rejected applying art. 383 from the start of the employment relationship in anticipation of future residence: status is determined 'al momento de cada pago'. Where a non-resident performs the service entirely outside Colombia the income is foreign-source and NO withholding applies (DIAN Oficio 28380 de 2019).

7. NEW FINDING: Ley 2466 de 2025 art. 64 ('regimen simple laboral') adds two paragraphs to Ley 50 de 1990 art. 99 permitting (a) monthly advance deposit of 8.33% of the base to the fondo de cesantias, and (b) written agreement to pay the 1% cesantias interest MONTHLY. Both are configurable engine options that smooth the January and February cash-flow spikes.

8. DEFECT FOUND IN OFFICIAL GUIDANCE: MinTrabajo Circular Externa 101 de 2025 section 5.1 states 'trabajo suplementario en Domingo y festivos con un recargo del 75% (Art. 179 CST)' - the PRE-REFORM figure - contradicting its own section 4, which correctly sets out the 80% / 90% / 100% phase-in. The section 4 schedule, which tracks the statutory text of CST art. 179 as substituted by Ley 2466 de 2025 art. 14, governs. The 75% reference is a residual error and must NOT be configured.

9. CO-CESANTIAS-006 LAYOUT SOURCING CLOSED: scope_manifest previously recorded the annual cesantias deposit as having no published schema ('each fondo publishes its own layout'). It does have one. The Simple S.A. 'Manual Cesantias' (licensed operador de informacion), section 3.2, publishes a byte-exact fixed-width layout of 20 campos in 258 positions with Inicial-Final positions, lengths, types and validations, and section 3.1 publishes the parallel XLS 97-2003 layout of 16 columns A-P; both carry the five-value fondo code table (02 Proteccion, 03 Porvenir, 10 Colfondos, 15 FNA, 19 Skandia) and the document-type table. The positions are arithmetically consistent (2+5+2+16+20+20+20+20+2+3+4+9+4+9+50+2+3+7+50+10 = 258). The CHANNEL is independently confirmed by the ACH Colombia (SOI) instructivo DDS-DES-INS-008 v2. Both PDFs are now in 00-official-sources/pdfs/ and extracted to _txt/. Spec accuracy 88%, against the previous DERIVED assumption.

10. CO-CESANTIAS-006 TRANSPORT-ALLOWANCE DEFECT IDENTIFIED IN THE CHANNEL ITSELF: the operator's auto-calculator uses 'Salario basico * (dias trabajados / 360)' and its campo 12 is named 'salario basico', whereas CST art. 253 requires the auxilio de transporte in the base and Ley 2466 de 2025 art. 64 par. 1 says so expressly for the monthly advance. For a 2026 minimum-wage employee the portal computes COP 1,750,905 against a statutory COP 2,000,000 - a COP 249,095 short deposit per employee, penalised as non-deposit at one day's salary per day of delay, uncapped. The engine must always write its own figure into campo 14. Documented at Spec field T14 and on Sheets 5, 7, 8 and 9.

## B.3 Known failure patterns checked (control C20)

- F1
- F2
- F3
- F4
- F5
- F6
- F7
- F8
- F9
- F10
- F11
- F12
- F13
- F14
- F15
- F16
- F17
- F18
- F19
- F20
- F21
- F22

### Failure-pattern notes

- **F18_stale_law**: PREVENTED. Newest applicable law used as primary source throughout: Ley 2466 de 2025 (labour reform, sanctioned 25 June 2025) for working time, night window, overtime limits, rest-day premium, contract types, apprenticeship, prescription and cesantias mechanics; Decreto 0223 de 5 March 2026 for the apprenticeship regulation; Decreto 1469 de 2025 for the 2026 minimum wage; Decreto 1470 de 2025 for the transport allowance; Resolucion DIAN 000238 de 2025 for the tax unit; MinTrabajo Circular 101 de 2025 for the hourly divisor; DIAN Conceptos 013840 de 2025 and 011108 de 2026 for the two live doctrinal points. SUPERSEDED REFERENCES EXPLICITLY FLAGGED: the legacy 240 hourly divisor (obsolete); the pre-reform 21:00 night boundary (superseded 25 Dec 2025); the pre-reform 75% dominical premium (superseded 1 Jul 2025); CST art. 162 literal b) (repealed by Ley 2466/2025 art. 70); the nomina electronica Anexo Tecnico 5.5.5 legacy percentages (read per DIAN Concepto 013840/2025); Decreto 0159 de 2026 (spent after the Consejo de Estado revoked the suspension on 9 July 2026).
- **F19_hr_scope**: PREVENTED. Three HR-scope filings descoped with reasons and client impact: the MinTrabajo disability-hiring contract report and quota, the SENA apprentice quota and its monetisation, and RUAF-ND vital-events notifications. All require headcount census, qualification, occupational or certification data sourced outside payroll.
- **F20_wtc_tax_codes**: Colombia has no country-specific tax-code legend of the Egypt type. The taxability dimensions the WTC must carry are enumerated in wage_type_categories.special_rules: salary/non-salary, IBC, payroll-levy base, statutory-benefit base, vacation base and taxable. Every wage type must carry a HARD salary/non-salary flag, because the nomina electronica XML separates them at element level with paired S/NS element names.
- **F21_filing_mechanics**: RESEARCHED AND DOCUMENTED. Colombian wage taxes and contributions file as SEPARATE submissions to SEPARATE authorities through THREE DIFFERENT CHANNEL POSTURES - not as one consolidated grid: (a) the nomina electronica is genuine MACHINE-TO-MACHINE (SOAP 1.2, XAdES-EPES, synchronous ApplicationResponse); (b) Formulario 350, Formulario 220 and the informacion exogena are PORTAL ROUND-TRIPS with DIAN; (c) PILA is a PORTAL ROUND-TRIP THROUGH A LICENSED PRIVATE OPERADOR DE INFORMACION - the employer never reaches the government directly for social security. The annual filings (Formulario 220, Formato 2276) and the annual cesantias deposit are SEPARATE employer obligations, NOT derived from the monthly filings. Colombia imposes NO employer year-end tax reconciliation and NO annual social-security reconciliation.
- **F22_pdf_size**: Source PDF folder for this build is 77 MB across 22 files, held in a SINGLE subfolder (00-official-sources/pdfs). Two files exceed 5 MB and are scanned (Decreto 0223 de 2026 at 17 MB and Resolucion DIAN 000227 de 2025 at 15 MB); both were extracted page-selectively with pdfplumber rather than loaded whole.

## B.4 Integration-landscape open questions

- Whether any licensed PILA operador besides ARUS/SuAporte offers a contractual API, and what the ARUS 'APIS PILA' catalogue actually contains - the developer portal renders no public content. Closeable only with an operator commercial contact, and only worth doing once the client's operator is fixed.
- Whether DIAN publishes a standalone XSD for Formato 2276 v4 in the reporting-year prevalidador release, or whether the prevalidador remains the only validator. Affects 04-reports-spec fidelity, not the integration verdict.


---

# Part C - DD-to-Report-Specs alignment patch v1.1 (verbatim, in full)


# Colombia — DD ↔ REPORT SPECS ALIGNMENT PATCH

**Country:** Colombia (CO) · **Stage:** alignment patch (mandatory pre-audit step)
**Date:** 2026-09-07 · **Result:** all six checks aligned — **0 open mismatches**

## Files patched

| File | v1.0 → | Rebuilt from source |
|---|---|---|
| `05-data-dictionary/CO-DD-001-v1.0.xlsx` | v1.1 | `build_co_dd.py` + `co_dd_data_{employee,employer,employment,mappers}.py` |
| `04-reports-spec/CO-DIAN-001-NominaElectronica-Spec.xlsx` | v1.1 | `co_r1_nomina_electronica.py` / `co_r1_sheets.py` |
| `04-reports-spec/CO-DIAN-002-Formulario350-Spec.xlsx` | v1.1 | `co_r2_formulario350.py` / `co_r2_sheets.py` |
| `04-reports-spec/CO-PILA-003-AportesSeguridadSocial-Spec.xlsx` | v1.1 | `co_r3_pila.py` / `co_r3_sheets.py` |
| `04-reports-spec/CO-DIAN-004-Formulario220-Spec.xlsx` | v1.1 | `co_r4_formulario220.py` / `co_r4_sheets.py` |
| `04-reports-spec/CO-DIAN-005-Formato2276-Spec.xlsx` | v1.1 | `co_r5_formato2276.py` / `co_r5_sheets.py` |
| `04-reports-spec/CO-CESANTIAS-006-ConsignacionAnual-Spec.xlsx` | v1.1 | `co_r6_cesantias.py` / `co_r6_sheets.py` |

Every fix is applied **in the generator source**, never to the `.xlsx` by hand, so
a rebuild reproduces the aligned state exactly. Version Control sheets on all
seven files carry the v1.1 change-log entry.

## Authority order used to resolve every divergence

official government form / anexo técnico / XSD **>** CCG **>** web research.

Primary sources: DIAN Anexo Técnico Nómina Electrónica V1.0 (Res. DIAN 000013 de
2021) tables 5.1.1–5.5.8; PILA Anexo Técnico 2 (Res. MSPS 2388 de 2016, AT2
versión 09 of 16-09-2019); Formulario 350 (Res. DIAN 000031 de 2024); Formulario
220 + instructivo; Res. DIAN 000227 de 23-09-2025 (Formato 2276 v4); published
severance-savings (cesantías) XLS/PCSS layouts; Res. DIAN 000238 de 15-12-2025
(UVT 2026 = COP 52,374); Decreto 1469 de 2025 (SMMLV 2026 = COP 1,750,905).

---

## CHECK 1 — Option mapper code alignment (F1 prevention)

| Check | Field / Mapper | Issue Found | Fix Applied | File Patched |
|---|---|---|---|---|
| 1 | `Worker Type` code 40 | DD carried code 40 "Beneficiario UPC adicional". Anexo table 5.5.3 admits exactly sixteen codes (01 02 04 12 18 19 21 22 23 30 31 47 51 54 56 58); 40 is a PILA-only *tipo cotizante* for a health-coverage beneficiary, not an employee, and the mapper drives `Employee.Worker_Type_Code` → NIE041, a table-5.5.3 code. | Code 40 removed; recorded in the mapper's excluded-code list with the reason. | `co_dd_data_mappers.py` |
| 1 | `Employee Document Type` code 47 | Abbreviation read `PE`. Anexo table 5.2.1 prints **PEP**. `PE` is the PILA/SOI two-letter code — a different catalogue. | Abbreviation → `PEP`; the PILA two-letter equivalent moved to the Constraint/Notes and given its own mapper (below). | `co_dd_data_mappers.py` |
| 1 | `Worker Sub-Type` | Hard rule did not match the PILA anexo statutory list, and the dual catalogue was undocumented — DIAN table 5.5.4 admits only `00`/`01`, whereas PILA T2R2-006 runs 0–12 as a **single digit**. | Hard rule aligned to the PILA list (1, 2, 3, 4, 5, 6, 9, 12), the in-scope subset named separately, and the code-width trap recorded explicitly. | `co_dd_data_mappers.py` |
| 1 | **NEW** `Employee Document Type (PILA / Cesantías)` | `CD` and `SC` were named as valid in the numeric mapper's constraint (b) but had no row anywhere, so PILA T2R2-003 / T2R2-074 and CO-CESANTIAS-006 T03 had no complete code table. | New mapper carrying AT2 v09 campo 3 verbatim — CC CE TI PA CD SC RC PE — plus `PT`, scoped "cesantías XLS layout ONLY" (absent from the PILA fixed-width list, no DIAN numeric equivalent, CO-GAP-06). | `co_dd_data_mappers.py` |
| 1 | `Principal Contributor Document Type` (PILA T2R2-074) | **Wrong mapper attached.** The field pointed at `Employer Document Type` while its own Pre-Defined Format and notes both said it takes the PILA two-letter **contributor** catalogue. The two lists differ in exactly two places — the employer list carries `NI` and lacks `RC` — so the wrong mapper admitted a corporate NIT as a principal contributor's document type and rejected a *registro civil*, precisely the beneficiary case the field exists for. Spec T2R2-074 points at the same Sheet 6 table as T2R2-003. | Field re-pointed to `Employee Document Type (PILA / Cesantías)`; the employer mapper's own note, which had claimed T2R2-074 as a second referrer, corrected to say so and to name the two-code difference. | `co_dd_data_employment.py`, `co_dd_data_mappers.py` |
| 1 | `Tipo de trabajador` code 21 | Spec Sheet 6 abbreviation `EST-P` vs DD `EST-PG`. | Spec aligned to the DD abbreviation. | `co_r1_sheets.py` |
| 1 | `Clase de aportante` code D | Spec Sheet 6 abbreviation `LEY 1429` (with a space) vs DD `LEY1429`. | Spec aligned to the DD abbreviation. | `co_r3_sheets.py` |
| 1 / 4 | `PARENTESCO` (F220 casilla 82) | Spec Sheet 6 table did not carry the DD `Dependant Relationship` codes. | Code table rewritten to the DD codes (ET art. 387 dependant classes). | `co_r4_sheets.py` |

**Verified equal, no change needed** — all 36 DD mappers were cross-read against
every Sheet 6 section, not a sample. Reconciled exactly: Employee / Employer /
Legal-Representative / Dependant Document Type, Pay Frequency, Contract Type,
Payment Method, Payment Form, Class of Contributor, Occupational Risk Class,
Employer Status Action Type, Form of Presentation, PILA Filing Modality, PILA
Planilla Type, Employer Person Type, Employer Legal Nature, Contributor Type,
Formato 2276 Informant Type, Yes/No Indicator, Dependant Relationship,
Severance-Savings Fund, Treaty Status, Withholding Procedure.

Two apparent divergences were confirmed **correct as they stand**:

- `Worker Sub-Type` — DD holds 00/01/03/04/05/06/09 (two-digit, nómina
  electrónica convention) against PILA's single-digit 0–12. The DD is a
  documented in-scope subset: 02, 10 and 11/12 are independientes / taxi
  populations outside private-sector employment. The dual catalogue and the
  code-width trap are stated in the mapper note.
- `PILA Novedad (Change Event) Type` — DD splits 18 atomic codes where spec
  Sheet 6 groups rows (`TDE / TAE`, `TDP / TAP`, `VAC-LR`, `Correcciones A/C`).
  Same semantic content on both sides; both document the three-value VAC/LR
  flag and the two correction limbs.

## CHECK 2 — Field classification accuracy (F3 prevention)

| Check | Field / Mapper | Issue Found | Fix Applied | File Patched |
|---|---|---|---|---|
| 2 | `Contract.Contractual_Salary` → NIE062, T2R2-040, T12 | Flagged Payroll Field = **Y** in the specs, but it is an **amount**. The pipeline rule is explicit: basic/base salary amounts belong to the Wage Type Catalogue, not the Data Dictionary. The DD build already excluded it, so the two builds were out of lock-step. | The three spec rows now read **N**, and the mapping is removed from `_DD_MASTER_MAPPINGS`. The DD carries no such field, so the deviation is resolved at source rather than annotated. | `co_r1_nomina_electronica.py`, `co_r3_pila.py`, `co_r6_cesantias.py`, `build_co_specs.py` |
| 2 | calculated amounts under an `Employee.` prefix | Several computed amounts carried a master-data System Mapping namespace, which made column E unreadable as a classification. | Retagged to the `Payroll.` namespace so column E and the namespace agree on every one of the 563 fields. | `co_r1_nomina_electronica.py`, `co_r3_pila.py` |

Final state, swept over all 563 fields: **0** rows where E=N but the mapping is
`Employee.` / `Company.` / `Contract.`; **0** rows where E=Y but the mapping is
`Payroll.` / `SUM` / `COUNT` / `System.` / `Mercans.` / `PayPeriod.` /
`Constant`; **0** rows where E=Y on an Amount / Count / Rate value type. Column E
distribution 160 Y / 403 N. Every Payroll-Field=Y mapping resolves to a DD row.

## CHECK 3 — Mandatory / conditional flags and C16 bidirectionality (F13 prevention)

Mandatory distribution: 246 Y · 297 C · 20 N. **Every one of the 297 C fields
carries a conditional reason**, and none is a stub (shortest is 25+ characters).

| Check | Field / Mapper | Issue Found | Fix Applied | File Patched |
|---|---|---|---|---|
| 3 | 82 DD field notes | `Spec ref` citations were stale or incomplete — a systematic off-by-N drift across the NIE, A1 and T2R blocks. Examples: Hire Date cited `NIE057`, which does not exist (the anexo field is `NIE002` FechaIngreso); the whole PILA employer block `A1-011`–`A1-017` was displaced by one; Place of Work Municipality cited `NIE053`, which is the work *address* (municipality is `NIE052`). | All 82 citations re-derived from the System Mapping join; each now names the artefact, the field ID and the Mandatory flag per artefact. | `co_dd_data_employee.py`, `co_dd_data_employer.py`, `co_dd_data_employment.py` |
| 3 | DD notes citing artefacts in prose | Five notes named artefacts in prose with no field ID at all — "all four DIAN artefacts" (Employer NIT DV), "all four per-employee artefacts" (Employee Second Surname), "(CO-DIAN-001)" with no ID (Employer Municipality Code). | Rewritten to explicit per-artefact field IDs. | `co_dd_data_employer.py`, `co_dd_data_employee.py` |
| 3 | mapper notes | Same defect class inside the Option Mapper notes: `NIE055`→NIE041, `NIE056`→NIE042, `NIE059`→NIE061, `NIE060`→NIE029, `A1-001`→A1-002/T2R1-005, `A1-017`→A1-020, `A1-032`→A1-030/T2R1-021, cesantías `T02`→T09. | Corrected. | `co_dd_data_mappers.py` |
| 3 | **45 spec fields — C16 in the spec-internal direction** | The v2.4 C16 rule is symmetric: *if A's condition mentions B, then B's notes must mention A*. It had been enforced only in the direction **DD note → spec field ID**; the spec-internal direction was never tested. Sweeping all 563 fields for Mandatory=C rows whose conditional reason names another field on the same artefact — and accepting an ID **range** (`NIE206-NIE209`, `T2R2-036 to T2R2-039`) as a valid reverse reference — left 45 B-side fields with no reverse reference at all: **18 on CO-DIAN-001**, **27 on CO-PILA-003**. | Reverse references installed for all 45, as a keyed post-assembly `_apply_c16` pass so each sentence travels with its row and survives a rebuild. A conditional B-side field takes the sentence in its **Conditional Reason (col G)**; an unconditional one takes it in its **Explanation (col M)**, so a Mandatory=Y row never acquires a conditional reason. | `co_r1_nomina_electronica.py`, `co_r3_pila.py` |

The 45, by artefact:

- **CO-DIAN-001 (18)** — NIAE214, NIE003, NIE004, NIE005, NIE011, NIE030,
  NIE041, NIE061, NIE065, NIE066, NIE118, NIE146, NIE160, NIE168, NIE170,
  NIE187, NIE188, NIE189.
- **CO-PILA-003 (27)** — A1-007, A1-019, A1-024, A1-033, T2R1-008, T2R1-011,
  T2R1-012, T2R1-019, T2R2-003, T2R2-005, T2R2-006, T2R2-008, T2R2-009,
  T2R2-031, T2R2-033, T2R2-036, T2R2-039, T2R2-042, T2R2-043, T2R2-045,
  T2R2-046, T2R2-048, T2R2-049, T2R2-066, T2R2-068, T2R2-080, T2R2-097.

Substantive examples, not boilerplate: NIE118 (service bonus, salary) now
records that it pairs with NIE119 and that *the salary and non-salary portions
must never be summed into one*; T2R2-036/039 (day counts) now record that the
whole novedad block T2R2-015–T2R2-030 drives them, so a novedad reported without
a matching movement in the day counters is a reconciliation error; T2R2-005
(contributor type) now names each field its code gates — T2R2-009/010 blank for
type 40, T2R2-056/074 only for type 40, T2R2-096 only for part-time type 51,
T2R2-031 blank only where the type is not obliged to contribute to pension.

Final state: **350 conditional cross-reference pairs, 0 unreciprocated.**

## CHECK 4 — Option value completeness (F14 prevention)

| Check | Field / Mapper | Issue Found | Fix Applied | File Patched |
|---|---|---|---|---|
| 4 | PILA T2R2-003 → "Tipo documento cotizante" | Column O pointed at a Sheet 6 section that **did not exist**. This is the employee document type on the social-security channel and a Payroll Field = Y master-data field, so an absent code table is a hard gap. | Section built from AT2 v09 Registro Tipo 2 campo 3 verbatim: eight values with their DIAN numeric equivalents, the PA/CD alphanumeric rule, the PE 15-digit SOI rule, and the CD/SC "no DIAN equivalent" note. | `co_r3_sheets.py` |
| 4 | PILA A1-034 → "Ley 1429 de 2010" | Column O pointed at a non-existent section. | Section built (S/N election, Decreto 1074 de 2015 art. 2.2.2.42.1, plus the hard rule that A1-034=S with A1-007≠D is rejected by the operador). | `co_r3_sheets.py` |
| 4 | Formato 2276 document type (numerals 2 and 34) | Code table was a bare placeholder row. | Completed with the 11 DIAN numeric codes. | `co_r5_sheets.py` |
| 4 | geographic section (NIE) | Column O referenced "Países / Departamentos / Municipios", which did not resolve to the section header. | Section renamed so all three references resolve. | `co_r1_sheets.py` |
| 4 | overtime / surcharge type (NIE) | "Overtime / surcharge type" did not resolve. | Section renamed (table 5.5.5). | `co_r1_sheets.py` |
| 4 | PILA T2R1-002, cesantías E09 | Column O text did not match the "MODALIDAD DE LA PLANILLA" and "RESPUESTA A LA VALIDACION ASOFONDOS" headers. | References aligned to the headers. | `co_r3_sheets.py`, `co_r6_sheets.py` |

Final state: **563 of 563** non-empty column-O values resolve — every one of the
138 `-> Sheet 6:` pointers lands on a real section, and no code-table section is
left as a bare placeholder.

## CHECK 5 — Composite key documentation (F12 prevention)

| Check | Field / Mapper | Issue Found | Fix Applied | File Patched |
|---|---|---|---|---|
| 5 | F220 casilla 4 (certificate number) | Length > 8 with a concatenated example (`2026-000417`) and no Composite Key Structure. DIAN prescribes **no** structure here — the instructivo says the number is "asignado por la persona natural o jurídica que expide la certificación", i.e. the employer assigns it — so the series is Mercans-designed and had to be fixed and documented to be auditable. | Composite Key Structure documented: positions 1–4 = accrual year AAAA from `PayPeriod.Fiscal_Year` (the year earned, **not** the year of issue); position 5 = literal hyphen; positions 6–11 = six-digit zero-filled consecutive from `Mercans.Certificate_Sequence`, restarting each accrual year, unique per employer per year. **Persistence:** assigned once and never reused, including after a reissue — a corrected certificate takes the next consecutive and cites the superseded number, because ET art. 378 makes the employee's copy the evidential document and two certificates may not share a number. | `co_r4_formulario220.py` |

Verified already documented, no change needed: NIE012 (document number =
prefix + consecutive), NIE020, NIE024 (CUNE SHA-384), Formato 2276 N02 and N34,
cesantías E01 (employer document type + number) and T04.

Two candidates were examined and correctly need **no** composite documentation:
F350 casilla 4 is DIAN-assigned and opaque (the form prints *"Espacio reservado
para la DIAN"*, and DIAN publishes no breakdown — the contrast with F220 casilla
4 is recorded on both rows), and NIE025 is the fixed literal `CUNE-SHA384`, not
a key.

## CHECK 6 — Code prefix verification (F14 prevention)

| Check | Field / Mapper | Issue Found | Fix Applied | File Patched |
|---|---|---|---|---|
| 6 | `R()` builder | No mechanism existed to state a prefix pattern in column J; patterns lived only in Sheet 6 notes, which is not where a developer reads the format. | `R()` gained `fmt_extra`, appending the pattern to column J. | `co_r3_pila.py` |
| 6 | PILA administradora codes — T2R1-014, T2R2-031, T2R2-032, T2R2-033, T2R2-034, T2R2-035 | Column J stated only `A(6)`. | Pattern `^(ARL\|EPS\|EOC\|AFP\|CCF\|FSP)[0-9]{3}$` stated in column J — three alphabetic positions naming the subsystem, three numeric naming the administradora; verified against the PILA anexo, which names FSP001, MIN001 and MIN002 in running prose. | `co_r3_pila.py` |
| 6 | **PILA T2R2-077 (ARL of the member)** | **Missed by the first pass.** Carries example `ARL001` yet column J stated only `A(6)`, while all six sibling administradora fields stated the pattern. Found by sweeping every field whose example is a letter-prefixed code rather than checking a hardcoded list. | Same prefix pattern added. | `co_r3_pila.py` |
| 6 | **DD administradora fields (7)** | Employer ARL, Employee ARL, EPS, EPS Transfer, AFP, AFP Transfer and CCF stated only `A(6) - administradoras catalogue` in Pre-Defined Format while the specs stated the full six-position pattern — the two documents describing the same format differently. | The pattern is now carried on **both** sides. The severance-savings fund code is deliberately left at `N(2)`, being a different published catalogue. | `co_dd_data_employment.py`, `co_dd_data_employer.py` |
| 6 | F350 casilla 983 (professional card) | No pattern. | `^[0-9]{1,6}-T$` stated, with the note that the `-T` suffix is part of the identifier and must not be stripped, because the Junta Central de Contadores quotes the card with it. | `co_r2_formulario350.py` |
| 6 | NIE010 / NIE012 | Numbering prefix and document number had no stated pattern. | Prefix pattern stated in column J; NIE012's pattern stated alongside its composite key. | `co_r1_nomina_electronica.py` |

Final state: every prefixed administradora example states its pattern in column
J; **0** examples violate the regex their own column J states; the DD states the
same pattern on all 7 administradora fields.

---

## Verification

Two verifiers, both re-run against the rebuilt workbooks:

| Verifier | Coverage | Result |
|---|---|---|
| `_txt/align/verify_alignment.py` | Checks 1–6, 22 assertions | **0 failed** |
| `_txt/align/verify_c16_prefix.py` | C16 spec-internal direction over all 563 fields; full prefix sweep incl. the DD side | **0 failed** |
| `05-data-dictionary/_validate_co_dd.py` | DD structural conformance C1–C13 | **13 checks, 0 failures** |
| `_audit_v24_mechanical.py` (`CL_AUDIT_CODE=CO`) | mechanical v2.4 gate | 14 PASS · 2 MANUAL · 2 FAIL |

`verify_c16_prefix.py` was written for this stage because the first pass's
verifier hardcoded its Check 5 and Check 6 field lists and tested C16 in one
direction only — which is how T2R2-077 and the 45 unreciprocated pairs survived
it. The new verifier sweeps instead of sampling.

The two mechanical-audit FAILs are **C21 and C26**, both looking for the
placeholder sheet names `Unknown (EN)` / `Unknown (XX)` in
`XX_Compliance_Payslip_Generator.xlsx`. They concern `06-payslip`, are outside
this stage, and are the same known false positive recorded on TN / OM / CI. The
harness must be invoked with `CL_AUDIT_CODE=CO`; without it, `CODE` defaults to
`XX` and all path-based checks report the CCG and `scope_manifest.json` as
missing.

## Accepted by design — recorded rather than changed

1. **Twelve `Mandatory=Y` rows on CO-CESANTIAS-006 (T03, T04, T05, T07, T09,
   T10, T11, T12, T13, T14, IN01, IN02) carry text in column G.** These are deliberate
   C16 back-references ("T04 back-references this field", "see E09, which
   back-references this field") placed there by the first pass. The 45 reverse
   references added in this pass use column M for unconditional rows instead, to
   avoid putting a conditional reason on a non-conditional field. Two
   conventions therefore coexist in the pack. Left as-is: the mechanical audit's
   C12 checks header depth, not per-row column-G emptiness, and rewriting
   deliberate prior-pass text carries more risk than the cosmetic gain. Worth
   settling one way in a future revision of the standard.
2. **`Social Security Subsystem` and `PILA Novedad (Change Event) Type` remain
   reference-only mappers**, unreferenced by any DD field's Option Mapper column
   by design — they document transactional per-payrun values that gate
   master-data conditionality. `_validate_co_dd.py` C11 exempts exactly these
   two. The contributor document-type mapper is **no longer** in that category:
   it is now properly owned by `Principal Contributor Document Type`.
3. **`PT` (Permiso por Protección Temporal)** stays scoped "cesantías XLS layout
   ONLY" in the contributor mapper. It is absent from the PILA fixed-width list
   of AT2 v09 and has no DIAN numeric equivalent — carried as **CO-GAP-06**, not
   silently normalised to `PE`/47.

## Tooling written for this stage

Under `_txt/align/`:

`patch_lib.py` (adjacent-string-literal rewriter) · `patch_dd_notes.py`,
`patch_dd_notes2.py`, `patch_dd_notes3.py` (82 + 5 DD note citations) ·
`patch_dd_mappers.py` (Check 1) · `patch_specs.py`, `patch_specs2.py`
(Checks 1, 2, 4, 5, 6) · `patch_c16_reverse.py` (45 C16 reverse references) ·
`patch_versions.py` (change-log rows) · `verify_alignment.py`,
`verify_c16_prefix.py` (verification) · pre-patch source snapshots in
`_txt/align/backup/`.


---

# Part D - Pre-submission audit gate / handover status (verbatim, in full)


# Pre-Submission Audit — Colombia v2.4

**Overall verdict:** READY_FOR_HANDOVER

**Date:** 7 September 2026
**Auditor:** Pre-Submission Audit Gate (content review)
**Country code:** CO · **Currency:** COP · **Local language:** ES · **Fiscal year:** 2026

---

## Mechanical audit raw result

| Run | Command | PASS | MANUAL | FAIL | Overall |
|---|---|---|---|---|---|
| Original (`logs/audit_v24_mechanical.json`) | `python _audit_v24_mechanical.py` | 12 | 3 | 3 | **BLOCKED** |
| Re-check (`logs/audit_v24_recheck.json`) | same, after fixes | **16** | **2** | **0** | **READY_FOR_HANDOVER** |

The three original FAILs (C12, C20, C29) were all investigated at the artifact level and all three
proved to be **matcher defects in the shared audit harness, not artifact defects**. Two of them
(C12 = F25, C20 = F24) are already-logged shared-harness bugs now reproduced on a sixth country.
The third (C29) is a new regression of the previously-fixed Spanish-`todo` defect. One of the three
MANUALs (C33) was likewise a matcher defect, but investigating it surfaced **one genuine content
defect in the CCG**, which was fixed.

> **Interpreter / environment note.** The audit must be run with `python` (has `python-docx` 1.2.0 +
> `openpyxl`), not `python3`, and requires the country environment to be injected:
> ```
> CL_AUDIT_CODE=CO CL_AUDIT_COUNTRY=Colombia CL_AUDIT_LOCAL_LANG_SHORT=ES \
> CL_AUDIT_CURRENCY=COP python _audit_v24_mechanical.py
> ```
> Run bare, `CODE` defaults to `XX` and every artifact check reports "missing" — a false BLOCKED.
> This is the same interpreter mismatch logged on BH/OM/TN/CI.

---

## Artifacts produced

| Artifact | File | Size |
|---|---|---|
| CCG | `01-ccg/CO-CCG-001-v1.0.docx` | 279 KB |
| CCG source modules | `01-ccg/modules/m01…m13*.md` | 13 files, 442 KB |
| WTC | `02-wtc/CO-WTC-001-v1.0.xlsx` | 300 KB |
| SIR index | `03-statutory-integrations/CO-SIR-INDEX-001-v1.0.docx` | 40 KB |
| Integration landscape | `03-statutory-integrations/integration-landscape.json` | 35 KB |
| Integration runbook | `03-statutory-integrations/DIAN-NE/` (P1–P7 + interlinkages + effort estimates) | 10 files, 86 KB |
| Report Specs | `04-reports-spec/` | 6 files, 425 KB |
| DD | `05-data-dictionary/CO-DD-001-v1.0.xlsx` | 551 KB |
| DD classification | `05-data-dictionary/CO-DD-001-classification.md` | 31 KB |
| Payslip | `06-payslip/CO_Compliance_Payslip_Generator.xlsx` | 492 KB |
| QA cross-check | `07-qa-crosscheck/` (alignment patch, payslip verification, scope validation) | 3 files, 60 KB |

### Report spec inventory (6 in-scope filings, all specced)

| Filing ID | Spec file | Rows |
|---|---|---|
| CO-DIAN-NE-MONTHLY-001 | `CO-DIAN-001-NominaElectronica-Spec.xlsx` | 225 |
| CO-DIAN-F350-MONTHLY-002 | `CO-DIAN-002-Formulario350-Spec.xlsx` | 69 |
| CO-PILA-MONTHLY-003 | `CO-PILA-003-AportesSeguridadSocial-Spec.xlsx` | 170 |
| CO-DIAN-F220-ANNUAL-004 | `CO-DIAN-004-Formulario220-Spec.xlsx` | 75 |
| CO-DIAN-EXO2276-ANNUAL-005 | `CO-DIAN-005-Formato2276-Spec.xlsx` | 50 |
| CO-CESANTIAS-DEPOSIT-ANNUAL-006 | `CO-CESANTIAS-006-ConsignacionAnual-Spec.xlsx` | 52 |

7 further filings are descoped in `scope_manifest.json`, each with a written reason
(MinTrabajo disability report, SENA apprentice quota, RUAF novedades — all HR-scope; PILA planillas
T/F and I/Y — out-of-scope employment types; ICA withholding — not a payroll filing; Form 110 —
employee obligation, not employer).

### Integration coverage

Exactly one authority is a genuine machine-to-machine channel, so exactly one 7-phase runbook exists.
This is by design, not a gap:

| Authority | Channel | Integration | Runbook | Filings carried |
|---|---|---|---|---|
| DIAN-NE | SOAP 1.2 web service (`SendNominaSync`) | **Yes (M2M)** | `DIAN-NE/` P1–P7 | 001 |
| DIAN-MUISCA | Portal round-trip | No | n/a | 002, 004, 005 |
| PILA-OI | Licensed intermediary portal / file upload | No | n/a | 003 |
| FONDOS-CESANTIAS | Licensed intermediary portal / file upload | No | n/a | 006 |

The M2M verdict was verified live on 4 September 2026, not inferred: both the production
(`vpfe.dian.gov.co`) and habilitación (`vpfe-hab.dian.gov.co`) WSDLs returned HTTP 200 unauthenticated
and both declare `wsdl:operation name="SendNominaSync"`.

---

## Audit results (C1–C33)

| Check | Original | Final | Detail (final) |
|---|---|---|---|
| C1 — CCG structural completeness | PASS | PASS | 13 modules |
| C8 — Open-item resolution (CCG) | PASS | PASS | No open-item markers |
| C11 — CCG question coverage | PASS | PASS | 96/96 (100%) |
| C12 — Spec column schema depth | **FAIL** | **PASS** | All 6 specs adequate — 13/16 keywords each, 21 columns |
| C20 — Scope decision audit trail | **FAIL** | **PASS** | 6 in-scope all specced, 7 descoped with reasons |
| C21 — Payslip 8-sheet structure | PASS | PASS | All 8 sheets present |
| C22 — Payslip spec depth | PASS | PASS | All sections, 62 rows |
| C23 — XML/XSD justification | PASS | PASS | No unsupported XML in specs |
| C24 — Portal/institution labels | PASS | PASS | Consistent |
| C25 — Sample-file fabrication guard | MANUAL | MANUAL | Dispositioned below — verified genuine |
| C26 — Payslip formula + currency hygiene | PASS | PASS | 8-sheet + currency format OK |
| C27 — System Mapping → DD traceability | MANUAL | MANUAL | 476 → 230, all derived/structural; dispositioned below |
| C28 — Zero-minor-unit currency rule | PASS | PASS | COP has a minor unit — rule N/A |
| C29 — Residual-marker lint (all artifacts) | **FAIL** | **PASS** | No residual markers |
| C30 — Source-tier flag | PASS | PASS | No tier-3 aggregator sources |
| C31 — Resident / non-resident treatment | PASS | PASS | Both present |
| C32 — Cross-artifact fact consistency | PASS | PASS | No `[[FACT:]]` tags (country pre-dates tagging) |
| C33 — CCG English-only prose | MANUAL | **PASS** | English-only; 1 genuine defect found and fixed |

---

## False positives identified

### C12 override — merged title banner on row 1 (known bug **F25**, 6th country)

C12 reported `6/6 specs have thin schema` with 0–1/16 keywords. Manual inspection: every spec's
Field Specification sheet carries a **merged single-cell title banner on row 1** and the real column
headers on **row 2**. `check_c12` read only `next(spec_sheet.iter_rows(max_row=1))`, so it scanned the
banner and matched nothing.

Evidence — `CO-PILA-003-AportesSeguridadSocial-Spec.xlsx`, sheet `PILA Spec`, dimensions `A1:U170`:

- **Row 1** (1 cell): `"Integrated Contribution Settlement Return (PILA) — social security and payroll levies - Planilla Integrada de Liquidacion de Aportes (PILA)"`
- **Row 2** (21 cells): `Field Name (EN)` · `Field Name (Local ES)` · `Record Type` · `Field Position` ·
  `Payroll Field (Y/N)` · `Mandatory (Y/N/C)` · `Conditional Reason` · `Position (in file)` · `Length` ·
  `Format` · `Example` · `System Mapping` · `Explanation` · `Relevant for Payroll (Y/N)` · `Option Values` ·
  `Rounding` · `Negative (Y/N)` · `Value Type` · `Frequency` · `Query to RA` · `RA Comments`

Row 2 scores **13/16** keywords against the standard schema — above the 12 threshold — for all six
specs. The 3 unmatched keywords are labelling differences, not missing columns: the specs use
`Query to RA` / `RA Comments` instead of `Error Code` / `Error Message`, and `Option Values` instead of
`Code Table`. The 21-column standard schema is fully present. This is exactly the defect logged as
F25 on Oman and reproduced on TN, CI and CG.

### C20 override — spec-traceability matcher (known bug **F24**, 6th country)

C20 reported all six in-scope filings as `In-scope without spec`. All six specs exist and pass C12.
`check_c20` tested `filing_id.lower().replace(' ','')` as a substring of a spec filename with `_` and
`-` stripped — it strips separators from the filename but **not** from the filing ID, so a dashed
semantic ID can never match a dash-stripped filename, and the word order is transposed besides
(`NE-MONTHLY-001` vs `001-NominaElectronica`).

`scope_manifest.json` already carries an explicit `spec_file` link on every in-scope filing, and all
six resolve on disk (verified):

```
CO-DIAN-NE-MONTHLY-001          -> CO-DIAN-001-NominaElectronica-Spec.xlsx        exists=True
CO-DIAN-F350-MONTHLY-002        -> CO-DIAN-002-Formulario350-Spec.xlsx            exists=True
CO-PILA-MONTHLY-003             -> CO-PILA-003-AportesSeguridadSocial-Spec.xlsx   exists=True
CO-DIAN-F220-ANNUAL-004         -> CO-DIAN-004-Formulario220-Spec.xlsx            exists=True
CO-DIAN-EXO2276-ANNUAL-005      -> CO-DIAN-005-Formato2276-Spec.xlsx              exists=True
CO-CESANTIAS-DEPOSIT-ANNUAL-006 -> CO-CESANTIAS-006-ConsignacionAnual-Spec.xlsx   exists=True
```

All 7 out-of-scope filings carry a `descoping_reason`. Pure naming-convention false negative.

### C29 override — the Spanish word *todo*, not an English TODO marker

C29 reported `CO-WTC-001-v1.0.xlsx[Wage Type Catalogue]: \bTODO\b`. Manual inspection: **29 cells,
every one of them the ordinary Spanish word `todo`/`Todo`** inside quoted statutory text. Exact case
forms found: `todo` ×27, `Todo` ×2 — **zero** uppercase `TODO`. `check_c29` matches with
`re.IGNORECASE`, so the Spanish word is unavoidably caught.

The six distinct contexts, all quoted statute:

| Occurrences | Context | Source |
|---|---|---|
| 24 | *"…debe valorarse expresamente en **todo** contrato de trabajo"* | Labour Code art. 129 (salary in kind) |
| 1 | *"…en reemplazo del auxilio de transporte. En **todo** caso, los teletrabajadores…"* | Law 1221 of 2008 (telework) |
| 1 | *"…el salario en especie debe valorarse expresamente en **todo** contrato de trabajo."* | Labour Code art. 129 |
| 1 | *"**Todo** empleador que habitualmente ocupe uno (1) o …"* | Law 11 of 1984 art. 7 |
| 1 | *"…provides that 'en **todo** caso la base de cotizacion debe ser…'"* | Decree 1072 of 2015 art. 2.2.6.3.3.4 par. 2 |
| 1 | *"**Todo** empleador que se afilie por primera vez al S…"* | occupational-risk affiliation |

This is the same defect the harness docstring says was already fixed for C8 ("C8 uses word-boundary
regex (no false positive on Spanish 'todo' etc.)") — C29, added later in v2.8, reintroduced it by
adding `re.IGNORECASE`. It is the Chile v2.4 precedent recurring.

### C33 override — mathematical and typographic symbols misread as non-Latin script

C33 flagged 158 CCG passages as "possible local-language passage". Every flagged sample was a fully
English sentence. Root cause: the detector excludes only a hand-written list of punctuation, so any
symbol outside that list is treated as foreign script. Character-level analysis of all
**7,292 CCG prose strings** shows the 170 flagged strings are triggered by exactly nine characters,
**all of them mathematical or typographic**:

| Char | Codepoint | Name | Hits |
|---|---|---|---|
| → | U+2192 | RIGHTWARDS ARROW | 87 |
| − | U+2212 | MINUS SIGN | 33 |
| § | U+00A7 | SECTION SIGN | 31 |
| ≤ | U+2264 | LESS-THAN OR EQUAL TO | 29 |
| · | U+00B7 | MIDDLE DOT | 27 |
| ≥ | U+2265 | GREATER-THAN OR EQUAL TO | 19 |
| ± | U+00B1 | PLUS-MINUS SIGN | 3 |
| Σ | U+03A3 | GREEK CAPITAL LETTER SIGMA | 1 |
| ≈ | U+2248 | ALMOST EQUAL TO | 1 |

Not one is a letter in any language. They appear in legitimate English prose such as
`"NIT 902025831 → DV 4"`, `"the Technical Annex §1.1.1.1"`, `"round half to even, with a ±2.00 tolerance"`,
and the NIT check-digit formula `S = Σ (digit_i × W_i)`.

**Independently confirmed no leakage exists.** C33's own curated Spanish function-word branch never
runs on these strings (the code `continue`s after a non-Latin hit), so it was executed separately over
all 7,292 strings: **0 hits**. A second, much broader scan with ~90 Spanish function and payroll words
returned 16 candidates, all of which are English sentences caught on English/Spanish cognates
("social", "pension", "literal") or on retained terms of art. Spot-checks confirm the B10 citation form
is followed — *"the integrated contribution return (Planilla Integrada de Liquidación de Aportes, PILA)"*,
*"the statutory service bonus (prima de servicios)"*, *"Unpaid leave (licencia no remunerada)"*.

**No translation was required.** Per the audit instruction, a hit that is only a proper noun or an
already-parenthesised citation is recorded as an override, not "translated". One genuine exception was
found and is recorded under Real fixes below.

### C25 disposition — sample file verified genuine, not fabricated

C25 flagged `CO-DIAN-001-NominaElectronica-Spec.xlsx` because its `Sample File` sheet contains XML
while `00-official-sources/sample-files/` is empty. The check only looks in that one directory; the
official DIAN Technical Annex **is** on disk at
`00-official-sources/pdfs/AnexoTecnico-NominaElectronica-V1.0.pdf` (extracted to `_txt/ne_anexo.txt`,
557,807 characters). Verified against it:

- The sheet **self-declares its provenance in a "PROVENANCE NOTE — READ FIRST" block**, stating that
  the SOAP envelopes are quoted verbatim from Anexo Técnico v1.0 §9.5 and §9.7.2, that the XML instance
  is *constructed* from the annex's own XPath inventory, that **DIAN publishes no sample instance**, and
  that it is therefore *"a faithful reconstruction of the documented structure — NOT an official DIAN
  sample"*, to be validated against XSD v1.0.6 in habilitación before use.
- The SOAP terms all occur in the annex text: `SendNominaSync` ×13, `wcf.dian.colombia` ×7,
  `IWcfDianCustomerServices` ×2, `contentFile` ×4, `soap-envelope` ×5, `ApplicationResponse` ×40.
- **All 29 distinct XML element names in the constructed instance are traceable to the annex.** A
  first pass matched 28/29; the lone miss, `LugarGeneracionXML`, is present as NIE013 but was split
  across lines by the PDF's column layout (`LugarGeneracionXM` / `L`), with the XPath
  `/NominaIndividual/LugarGeneracionXML` intact in the annex.

Nothing is fabricated, and the artifact does not overclaim. **MANUAL retained** — this is the check
working as designed (a human confirms), and the disposition is now recorded.

### C27 disposition — dotted identifiers vs prose DD field names

C27 flagged 476 System Mapping values as needing a DD link. Column L **is** `System Mapping`, so the
check reads the right column, but it compares by substring: it requires a whole DD cell string (>4
chars) to appear inside the mapping text. DD fields are named in prose (`Employee Document Type`,
`Employer NIT`) while mappings are dotted identifiers (`Employee.Document_Type`, `Company.NIT`), so the
test can essentially never succeed. Two further contributors: `min_row=2` reads the banner-offset
header row itself as data (6 of the 476 were the literal header cell `"System Mapping"`), and the
`DERIVED` classifier does not recognise the canonical system namespaces.

Under an alphanumeric-only normalisation, **459 of the 465 non-header values (98%) resolve to a DD
field**. After the C27 fix (below), the count falls 476 → **230**, and every remaining item is
genuinely derived or structural:

| Count | Namespace | Example | Class |
|---|---|---|---|
| 158 | `Payroll.*` | `Payroll.Overtime_Detail`, `Payroll.Meal_Excess_41UVT` | payroll-engine result, not DD master data |
| 69 | `Mercans.*` | `Mercans.Cesantias_Accrual_Year`, `Mercans.Payment_Channel_Config` | pipeline configuration |
| 3 | arithmetic / n-a | `NIE187 - NIE188 (+/- NIE186)`, `T2R2-047 + T2R2-048 + T2R2-049`, `(not an input)` | cross-field computation |

The 261 distinct identifiers are coherent payroll concepts, not placeholders — `Income_Tax_Withheld`,
`Health_Employee_Contribution`, `Prestaciones_Sociales`, `Cesantias_Paid_To_Employee`,
`NonResident_Withholding`. **MANUAL retained** by choice: extending `DERIVED` to auto-accept the
`Payroll.*` namespace would let a genuinely unmapped payroll field pass silently in a future country.
A human confirming the class is the correct outcome here.

---

## Real fixes applied

### 1. CCG — B10 violation: bare Spanish noun in English prose (found via C33)

Investigating C33 surfaced one genuine defect the mechanical check could not have flagged (it was
masked by the symbol false positives). Module 8, the sickness-incapacity open item, used the bare
Spanish common noun *auxilio* standing alone in an English sentence, with no English wording and no
first-use introduction — a real breach of control B10. It was the **first** use of that term in
document order; the later *"auxilio de cesantía"* (a different benefit) is correctly introduced.

- **Was:** "…Labour Code art. 227 sets the *auxilio* at two thirds for the first 90 days…"
- **Now:** "…Labour Code art. 227 sets the cash sickness benefit (*auxilio monetario*) at two thirds for the first 90 days…"

English wording first, statutory term in parentheses on first use, existing italic run formatting
preserved. Verified verbatim against the source PDF on disk
(`00-official-sources/pdfs/Decreto_2663_de_1950.pdf`), CST art. 227:

> "ARTICULO 227. VALOR DE AUXILIO. En caso de incapacidad comprobada para desempeñar sus labores,
> ocasionada por enfermedad no profesional, el trabajador tiene derecho a que el {empleador} le pague
> un **auxilio monetario** hasta por ciento ochenta (180) días, así: las dos terceras (2/3) partes del
> salario durante los primeros noventa (90) días y la mitad del salario por el tiempo restante."

This also independently confirms the CCG's substantive claim (two thirds for the first 90 days). No
rate, base, ceiling or legal citation changed.

### 2. CCG — Version Control entry for the language pass

Added row **1.0 rev B** (7 September 2026) to the Version Control table, recording the C33 language
pass, the 158-passage false-positive finding, and the one genuine B10 correction — consistent with how
rev A logged the earlier compliance pass.

### 3. Audit harness — four matcher fixes (`_audit_v24_mechanical.py`, v2.9)

Following the TN/CI/CG precedent, the false positives were fixed **in the harness**, not merely
overridden, so the next country does not re-hit them. Backup at `_audit_v24_mechanical.py.bak`;
patch script `_patch_audit_v29.py`. All changes compile clean.

| Check | Fix |
|---|---|
| **C12** (F25) | Scan the first 3 rows for the header, skipping any row with fewer than 2 non-empty cells (a merged title banner); keep the best keyword match instead of assuming row 1. |
| **C20** (F24) | Prefer the explicit `spec_file` link when the manifest carries one, and report it only if the declared file is genuinely absent from disk. Fall back to fuzzy matching only when absent, now stripping separators from **both** sides. |
| **C29** | An open-item marker is an ALL-CAPS convention. `TODO` is now matched **case-sensitively**; markers that cannot collide with a natural-language word (`TBD`, `FIXME`, `VERIFY No`, `[placeholder]`, `[CHECK]`, `[?]`) keep `IGNORECASE`. A real marker written `Todo:` is still caught by an explicit pattern, so detection strength is preserved. |
| **C33** | Replaced the punctuation-blocklist regex with a Unicode **general-category** test: only a character in category `L*` (a letter) outside the Latin blocks counts as script leakage. Symbols, punctuation, marks and digits can never trigger it. A short whitelist covers Greek letters used as mathematical notation (Σ, Π, Δ, μ, σ, …). |
| **C27** | Compare on an alphanumeric-only normalisation so `Payroll.Basic_Salary` matches `Basic Salary`; skip the banner-offset header row; treat `PayPeriod.*`, `System.*` and `Constant` as the structural class. (This implements the C27 widening already recommended in the CG v2.4 log entry.) |

**Regression-tested, not just applied.** The new C33 detector was run against known-positive and
known-negative cases: all nine CO symbol cases now read clean, while Bulgarian Cyrillic, Arabic,
Japanese and Greek prose are **still flagged**, and Latin-accented terms (`Liquidación de Aportes`,
`São Paulo`, `Köln`, `Ångström`) correctly read clean. Detection strength is preserved in every case.

---

## Remaining issues

**None blocking.** No FAIL remains and nothing was left unfixed.

Two MANUALs are retained deliberately, both dispositioned with evidence above — C25 (sample file
verified genuine against the official annex; the check is doing its job by asking a human) and C27
(230 derived/structural mappings; auto-accepting the `Payroll.*` namespace would weaken the check for
future countries).

Two open questions are carried forward from the SIR stage. Neither affects the handover verdict and
both are recorded in `integration-landscape.json`:

1. Whether any licensed PILA *operador de información* besides ARUS/SuAporte offers a contractual API.
   The ARUS "APIS PILA" developer portal renders no public content; closeable only with an operator
   contract. Does not change the verdict — PILA is a portal round-trip either way.
2. Whether DIAN publishes a standalone XSD for Formato 2276 v4, or whether the *prevalidador* remains
   the only validator. Affects `04-reports-spec` fidelity for filing 005, not the integration verdict.

Stage `08-skill/` is empty — the claude.ai compliance skill has not been built for Colombia. That is a
separate pipeline stage and is outside this gate's scope; flagging it only so it is not mistaken for
a missing handover artifact.

---

## Sign-off recommendation

**READY_FOR_HANDOVER.**

All 18 mechanical checks pass or are dispositioned: 16 PASS, 2 MANUAL with written evidence, 0 FAIL.
Every artifact in the v2.4 set is present and structurally complete — CCG (13 modules, 96/96 question
coverage), WTC, DD, 6 report specs covering all 6 in-scope filings, SIR index with a 7-phase runbook
for the one genuine M2M channel, and the 8-sheet payslip generator.

Three of the four original blocking/manual signals were harness defects and are now fixed in the
harness rather than papered over. The one genuine content defect found (a bare Spanish noun breaching
control B10) was corrected against the primary source and logged in the CCG's own version control.

---

## Next steps

1. Open the artifacts and review — particularly `CO-CCG-001-v1.0.docx` Module 8 (the corrected
   sickness-incapacity passage) and the Version Control table entry 1.0 rev B.
2. Manual confirmations to close the two retained MANUALs at review:
   - **C25** — confirm the DIAN NE sample XML is accepted as a documented reconstruction. It must be
     validated against XSD v1.0.6 in the DIAN habilitación environment before production use, as the
     sheet's own provenance note instructs.
   - **C27** — confirm the `Payroll.*` and `Mercans.*` namespaces are the accepted pipeline-side
     convention for engine results and configuration.
3. Two CCG open items remain flagged in-document for the dev team (both carry a Mercans configurable
   default and are already carried in the QA report, so neither blocks): the employer's rate for the
   first two days of incapacity (default 66.67%), and the minimum-wage floor on incapacity payments
   (primary regulatory source not retrieved this pass).
4. **If READY:** share with the dev team.
5. **Port the v2.9 harness fixes to `shared/`.** C12, C20, C27, C29 and C33 were fixed in the CO copy
   of `_audit_v24_mechanical.py`. F24 and F25 have now recurred on six consecutive countries
   (BH, OM, TN, CI, CG, CO) — the fixes should be promoted to the shared harness so country seven does
   not repeat this investigation.
6. Failure log updated — see `shared/country_failure_log.md`: F24/F25 reproduction recorded for CO,
   and **F27** (C29 `todo` regression) and **F28** (C33 symbol misread) added.


---

# Part E - Accuracy notes: what was independently re-derived, and what is DERIVED

## Verified by recomputation (exact, no rounding tolerance)

| Item | Result |
|---|---|
| Payslip income-tax withholding (ET arts. 383 / 388 / 206 num. 10) | **2,250,765 COP - exact.** Gross 19,200,000 - contributions 1,728,000 = 17,472,000; less 25% exempt capped at 790 UVT / 12 = 3,447,955 -> base 14,024,045 = 267.76732 UVT; band 150-360 UVT -> 0.28 x (267.76732 - 150) + 10 = 42.97485 UVT x 52,374. The 40% / 1,340-UVT art. 388 caps were tested and are not binding. |
| Payslip net pay | **15,221,235 COP** (`SUM(H21:J24) - SUM(H28:J31)`) |
| YTD block (7 months) | 134,400,000 / 12,096,000 / 15,755,355 / **106,548,645**; YTD net / 7 = the monthly net exactly |
| Employer block + provisions | 8.5 / 12 / 0.522 / 4 / 2 / 3 % and 8.33 + 1 + 8.33 + 4.17 = **21.83%**, agreeing with the WTC's 21.8333% |
| PILA record lengths | Archivo Tipo 1 **34 fields / 567 positions**; Archivo Tipo 2 Registro Tipo 1 **22 / 359**; Registro Tipo 2 **97 / 686** - arithmetically verified |
| Global WTC coverage | **300 of 300**, set difference empty in both directions |
| Form Reference Guide pointers | **65 of 65** resolve to a real file, sheet and in-range row - 0 broken |
| Fiscal parameters | SMMLV **1,750,905** (Decreto 1469 de 2025 art. 1) and UVT **52,374** (Res. DIAN 000238 de 15-12-2025 art. 1) verified in the source PDFs. **No stale parameters**: every occurrence of 1,423,500 (2025 SMMLV) or 49,799 (2025 UVT) is an explicit historical comparison. |

## Declared DERIVED (must be reconciled at configuration time)

| Item | Why |
|---|---|
| The Mercans code numbers of the 102 Colombia-specific WTC rows | No Mercans numeric code range has been assigned for Colombia; mnemonic `CO-` codes are used and **must be renumbered**. |
| Auxilio de transporte 2026 = **249,095** | Carried from the CCG because Decreto 1470 de 2025 is not held in `00-official-sources`. |
| The additional high-risk pension rate | Read from the Resolucion 2388 rate table (26% total vs 16% standard, implying +10 pp employer-borne), **not** from the implementing decree - `CO-GAP-02`. |
| Formato 2276 v4 XML layout | Marked **DERIVED** in the spec because the DIAN *especificaciones tecnicas* annex is not held locally. |
| The 7-phase `P1`-`P7` DIAN-NE runbook decomposition | The canonical `shared/si-runbook` module is not installed in this checkout; the phase boundaries are reconstructed from the stage-6 contract. Content maps across cleanly; file names may need renaming. |
| `Unit Rate Details` account codes on the payslip generator | Sheet is headed *"illustrative placeholder account codes; align to actual CO-WTC once available"*. |

## Defects found in OFFICIAL sources and recorded rather than propagated

| Source | Defect |
|---|---|
| MinTrabajo Circular Externa 101 de 2025, section 5.1 | States the Sunday/holiday supplementary-work premium as *"75% (Art. 179 CST)"* - the **pre-reform** figure - contradicting its own section 4, which correctly sets out the 80% / 90% / 100% phase-in. |
| Nomina electronica Anexo Tecnico v1.0, section 5.5.5 | Hard-codes the pre-reform rest-day percentages **75 / 100 / 150 / 110**. Settled by **DIAN Concepto 013840 (int. 1568) of 1 October 2025**: the statutory Ley 2466 de 2025 percentages govern; the annex literals **must not be configured**. |
| Decreto 1607 de 2002 | ARL class-IV rate defect. |
| Nomina electronica XSD | `Trabajador/@NumeroDocumento` typed `xsd:integer`, so no passport or alphanumeric foreign ID can be schema-valid (document types 21, 41, 42, 50); `Trabajador/@SegundoApellido` is `use=required`, yet many Colombians and virtually all foreign nationals have only one surname. No official workaround published - `CO-GAP-07`. |
| Nomina electronica document-type catalogue | **No code for the PPT** (*Permiso por Proteccion Temporal*, Decreto 216 de 2021), created one month after the annex and now held by the large majority of regularised Venezuelan migrants. Code 47 (PEP) is its legally superseded predecessor and the only proxy - `CO-GAP-06`. |
| Ley 2466 de 2025 art. 15 | The enacting formula announces *"los paragrafos 2 y 3"* but the published text prints a **Paragrafo 4** - `CO-GAP-14`. |
| Cesantias operator (Simple S.A.) auto-calculator | Uses `salario basico * (dias trabajados / 360)` and names campo 12 *"salario basico"*, whereas **CST art. 253 requires the auxilio de transporte in the base**. The operator's own calculator is wrong. |

## Time-sensitive parameters - reverify before each cycle

| Parameter | 2026 value | Watch |
|---|---|---|
| SMMLV | **1,750,905** COP/month | Decreto 1469 de 2025 was provisionally suspended (Consejo de Estado, 12 Feb 2026), re-fixed at the identical amount by Decreto 0159 de 2026, and the suspension was revoked on 9 July 2026. The **amount** was continuously in force from 1 Jan 2026 and was never in doubt - but an **annulment action on the merits is still pending** (`CO-GAP-08`). |
| Auxilio de transporte | **249,095** COP/month | Decreto 1470 de 2025 art. 1 - DERIVED, decree not held locally |
| UVT | **52,374** COP | Res. DIAN 000238 de 15-12-2025 art. 1 (uprating certified at 5.17%, from 49,799) |
| IBC ceiling / FSP trigger | 25 SMMLV = **43,772,625** / 4 SMMLV = **7,003,620** | move with the SMMLV |
| Rest-day premium | 80% -> **90% on 1 Jul 2026** -> 100% on 1 Jul 2027 | Ley 2466 de 2025 |
| Hourly divisor | 220 -> **210 on 15 Jul 2026** | Ley 2101 de 2021 + MinTrabajo Circular 101 de 2025 (the circular's legal weight is `CO-GAP-09`) |
| Pension architecture | **Ley 100 de 1993 as amended by Ley 797 de 2003** governs all of 2026 | Ley 2381 de 2024 is NOT in force for any 2026 period: art. 94 entry into force was suspended by Auto 841 de 2025 and, per **Sentencia C-264 de 25 August 2026**, the upheld provisions take effect **1 April 2027** (`CO-GAP-11`) |
| Cesantias 8.33% monthly advance deposit | permitted by Ley 2466 de 2025 art. 64 par. 1 but **not yet operable** | the implementing decree was still a MinTrabajo draft as at 4 September 2026 (`CO-GAP-13`) |
