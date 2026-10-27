# France QA cross-check report, alignment patch, scope validation and scope manifest

The complete France quality record: the independent QA cross-check of 2026-08-28 (overall 87/100, verdict NEEDS PATCHES - 0 CRITICAL, 3 MAJOR F-1..F-3, 3 MINOR m-1..m-3; checks 1-9, the v2.4 compliance summary, the scoring table and the audit-method note recording where it diverges from the superseded 12:21 report), the DD-vs-Spec alignment patch and its open items, the scope lock-in validation (PASS, findings W-01..W-03) and the full scope manifest with every in-scope and out-of-scope decision, known limitation and failure pattern checked.


## Provenance

| Source artifact | Bytes | SHA-256 |
|---|---|---|
| `FR-compliance/07-qa-crosscheck/FR-QA-REPORT.md` | 29,719 | `1bb895c6af9919bc…` |
| `FR-compliance/07-qa-crosscheck/FR-ALIGNMENT-PATCH.md` | 9,655 | `4d7bea5ada9ecf3f…` |
| `FR-compliance/07-qa-crosscheck/scope_validation.md` | 42,173 | `959c7933f552a3d7…` |
| `FR-compliance/scope_manifest.json` | 62,284 | `071558c285369335…` |

This file is a complete, verbatim conversion of the artifacts above. Figures, dates, code values, French terminology and legal citations are reproduced exactly as delivered; nothing is summarised or rounded.


## Navigation index

Read with `offset` / `limit` rather than opening the whole file.

| Line | Section |
|---|---|
| 68 | Part 1 - FR QA cross-check report (verbatim) |
| 70 | &nbsp;&nbsp;&nbsp;&nbsp;FRANCE — QA CROSS-CHECK REPORT |
| 81 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;EXECUTIVE SUMMARY |
| 116 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PER-CHECK ALIGNMENT SCORES |
| 388 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;GLOBAL WTC COVERAGE SUMMARY |
| 406 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ISSUES |
| 521 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;v2.4 COMPLIANCE SUMMARY |
| 538 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;SCORING |
| 554 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;READINESS VERDICT |
| 556 | &nbsp;&nbsp;&nbsp;&nbsp;⚠️ NEEDS PATCHES |
| 581 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;AUDIT METHOD AND DIVERGENCES FROM THE SUPERSEDED REPORT |
| 607 | Part 2 - FR alignment patch: Data Dictionary vs Report Specs (verbatim) |
| 609 | &nbsp;&nbsp;&nbsp;&nbsp;FR-ALIGNMENT-PATCH — Data Dictionary vs Report Specs |
| 616 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Inputs actually read |
| 633 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Patch log |
| 653 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Check 2 — why nothing was changed |
| 675 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Open items — NOT fixed, and why |
| 709 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Verification |
| 732 | Part 3 - Scope lock-in validation (verbatim) |
| 734 | &nbsp;&nbsp;&nbsp;&nbsp;FR — SCOPE LOCK-IN VALIDATION |
| 746 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;VERDICT |
| 764 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CHECK 1 — FILE EXISTS AND IS VALID JSON |
| 781 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CHECK 2 — REQUIRED SECTIONS PRESENT AND NON-EMPTY |
| 805 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CHECK 3 — AUTHORITY FILING FIELD COMPLETENESS |
| 841 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CHECK 4 — INBOUND PRODUCT MAPPING (F8) |
| 870 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CHECK 5 — IN-SCOPE / OUT-OF-SCOPE COLLISIONS (F2) |
| 910 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CHECK 6 — KNOWN FAILURE PATTERNS (F1–F15) |
| 936 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;B1 — NON-RESIDENT HANDLING FOR COVERED INCOME TYPES |
| 975 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;FINDINGS (non-blocking) |
| 1040 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;SCOPE DECISION REGISTER (v2.8 B7) |
| 1209 | Part 4 - scope_manifest.json (full) |
| 1227 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;employment_types |
| 1370 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;authority_filings |
| 1763 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;wage_type_categories |
| 1836 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;option_mapper_scope |
| 1931 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;integrations |
| 2187 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;known_failure_patterns_to_check (22 items) |
| 2213 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;failure_pattern_notes |
| 2224 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;scope_manifest_changelog (1 items) |
| 2237 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;known_limitations (3 items) |

---


# Part 1 - FR QA cross-check report (verbatim)

## FRANCE — QA CROSS-CHECK REPORT

**Artifact set:** `FR-compliance/` · **Standard:** v2.4 · **Filing year:** 2026 · **Currency:** EUR
**Date:** 2026-08-28 · **Auditor:** independent QA cross-check (did not build these artifacts)
**Method:** every figure below was measured mechanically from the delivered binaries, not read from
a build log or a prior report. The superseded report of 12:21 today is preserved at
`FR-QA-REPORT.md.bak-20260828-124820`; where this audit reaches a different number, the
divergence is stated explicitly and the measurement is shown.

---

### EXECUTIVE SUMMARY

**Overall score: 87 / 100**
**Verdict: NEEDS PATCHES** — 0 CRITICAL, 3 MAJOR, 3 MINOR

France is a structurally exemplary build. Every hard contract v2.4 imposes is met **exactly**, and
several were verified against falsifiable claims the build itself made rather than being taken on
trust. The CCG carries all 13 official modules with byte-exact template titles and reproduces
**136 of 136** template questions plus **13 of 13** template Deliverables as H3 headings — no
question is missing and nothing was invented. All 15 Report Specs share an **identical** 21-column
Sheet 4 header, all 9 sheets in the correct order, correct blue `FF4472C4` white-bold header row and
full row colouring. The Global WTC baseline is covered **300 of 300, in baseline order, at catalogue
rows 2–301, with zero exclusions** — a claim the coverage sheet makes explicitly and which this
audit re-derived from `shared/Global_WTC_V1_0.xlsx` position by position. Conditional-field
documentation (C16) is complete in **both** directions: 700 of 700 conditional spec rows and 125 of
125 DD conditional-mandatory fields carry their reason.

**The defects are concentrated in one layer: the DD↔Spec reconciliation annotation.** 264 spec rows
across 12 specs assert `NO DD COUNTERPART although this row is marked payroll master data —
registered as an open gap for scope owner adjudication`. That assertion is **substantially false**.
At least 156 of those rows name a field the Data Dictionary plainly defines, roughly 25 are
calculated amounts that belong in the CALC bucket and are not DD candidates at all, and a further
tranche are special-regime rubriques (CNIEG, ENIM, FINESS, entertainment, public-sector) that the
build **already descoped in writing** and already has a correct label for — it uses that correct
label 100 times elsewhere in the same specs. The registered limitation `FR-LIM-001` compounds this:
it counts 199 rows where the artifacts carry 264, and it nominates *employee e-mail address* as its
one "genuine omission" — a field the DD defines at `E-mail Address`.

This is not a legal or research defect. The underlying content is sound and well-sourced; a
mechanical reconciliation was run on the wrong key, its output was written into 12 delivered
workbooks as though it were a finding, and a scope question was then raised on the strength of it.
Nothing needs re-researching. **No finding requires new source material.**

---

### PER-CHECK ALIGNMENT SCORES

| # | Check | Score | Status |
|---|---|---|---|
| 1 | CCG ↔ WTC alignment | **2 confirmed gaps** of 374 wage types | PASS (→ F-2) |
| 2 | CCG Module 2 ↔ DD | **35 / 35 (100%)** | PASS |
| 3 | CCG Module 10 ↔ Report Specs | **11 / 12 (91.7%)** | NEEDS PATCH → F-3 |
| 4 | DD ↔ Report Specs (4-bucket) | **720 / 984 as delivered (73.2%)** | NEEDS PATCH → F-1 |
| 5 | Global WTC coverage | **300 / 300 (100%)** | PASS |
| 6 | Scope discipline | **0 violations** | PASS |
| 7 | Report Spec format compliance | **15 / 15 (100%)** | PASS |
| 8 | v2.4 standards | **5 / 5 artifact classes** | PASS (1 standard query → m-3) |
| 9 | v2.4 NEW — composite key / inter-field | **3 / 4 sub-checks** | PARTIAL → m-1 |

---

#### Check 1 — CCG ↔ WTC alignment · 2 confirmed gaps

The Wage Type Catalogue holds **374 rows**. Every one carries a complete treatment set: **zero** rows
are missing `Subject to Tax` or `Q1 URSSAF`. Category split: 230 Earning, 66 Deduction, 33 Employer
Contribution, 14 Flag, 12 Base, 7 Intermediary, 6 Percentage, 3 Notional, 3 Tax.

Concepts named in the treatment tables of CCG Modules 4–9 were matched against the catalogue. A
purely literal match scores poorly (31%) because the CCG's treatment matrices are written as
qualified phrases — *"Professional expense reimbursement within the statutory limits"*, *"Employer
death-and-disability contribution within limits"* — rather than as wage type names. **That is a
measurement artefact, not a gap**, and this audit did not report it as one. Every literal
non-match was probed against the catalogue by concept. Nearly all resolve:

| CCG concept | Resolves to |
|---|---|
| Value-sharing bonus | 62218 / 62219 / 62229 |
| Free share awards, share options | 62890, 62990, 62993, 62994 |
| Seniority, thirteenth month | 62140, 62200 |
| 50 % transport season ticket | 62520 |
| Partial activity | 62870, 62871 |
| Damages for unfair dismissal | 62883 |
| Voluntary / compulsory retirement indemnity | 62910, 62920 |
| Profit-sharing and incentive schemes, paid and invested | 62210–62215 |

Three unpaid leaves — parental education, carer's, parental presence — have no wage type and
**correctly so**: CCG Module 8 states each is *"unpaid by the employer"* with the allowance paid
directly by the family allowance fund, and the module's own table answers "No" to payment through
payroll. Absence of a wage type is the right answer.

**Two genuine gaps survive** (→ **F-2**). CCG Module 7 sets out four benefit-in-kind categories
carrying a statutory flat valuation. Two have wage types; two do not:

| BIK category (CCG M7) | Statutory flat value | Wage type |
|---|---|---|
| Accommodation | scale | ✅ 62400 flat, 62410 real cost |
| Company vehicle | 2025 scale, 70 % EV abatement | ✅ 62500 |
| **Meals** | **EUR 5.50 per meal, EUR 11.00 for two** | ❌ **none** |
| **Communication tools** | **10 % of purchase price or annual subscription** | ❌ **none** |

A broad sweep across all 24 columns and 374 rows of the catalogue, in English, French and the
explanation text, returns no match for either. `62670` is the employer share of meal **vouchers**
(a distinct, separately-exempt item under General Tax Code Article 81 19°) and `62630`/`62570` are
cash meal **allowances**. None values an employer-provided meal at the statutory flat rate.

---

#### Check 2 — CCG Module 2 ↔ DD · 35 of 35 (100%)

CCG Module 2 does not enumerate field specifications. It groups mandatory employee data into six
categories and states *"The complete field list, with formats and validation, is in the France Data
Dictionary."* That is correct v2.4 scope discipline (see Check 6), so this check was run at concept
level against the DD's **189 fields** (25 ID Information + 164 Country Fields) and its 413-row
Country Option Mappers sheet.

All 35 concepts resolve. Six required looking past the field list into the option mappers, and all
six are genuinely present — this audit initially scored them as missing and corrected on inspection:

| Concept | Where it lives |
|---|---|
| Managerial grade (*statut cadre*) | `Supplementary Pension Category Status`; `Employee Status under the Collective Agreement` |
| Day-count arrangement (*forfait jours*) | `Working-Time Arrangement`, mapper codes 20 / 21 |
| Withholding rate validity period | `Withholding Rate Validity Date` |
| Apprenticeship / work-study status | `Contract Nature`, mapper codes 61 / 64 / 65 |
| Garnishment orders | `Wage Attachment in Force` / `Type` / `Reference` |
| Work pattern | `Working-Time Arrangement` |

---

#### Check 3 — CCG Module 10 ↔ Report Specs · 11 of 12 (91.7%)

Module 10's in-scope table lists **12** reports. **15** specs are delivered. The five extra specs
are the inbound return flows (CRM PAS, CRM URSSAF, Retour Agirc-Arrco, Notification Taux AT/MP,
BPIJ), which Module 10 covers in its mandatory-inbound-integration section rather than in the
outbound reports table. That is correct, not a mismatch.

| Module 10 in-scope report | Spec |
|---|---|
| DSN monthly | FR-DSN-001 ✅ |
| DSN event — end of contract | FR-DSN-002 ✅ |
| DSN event — work stoppage / resumption | FR-DSN-003 ✅ |
| DPAE | FR-URSSAF-001 ✅ |
| Withholding at source remittance | FR-DGFIP-001 ✅ |
| DOETH | FR-URSSAF-003 ✅ |
| Apprenticeship tax balance | FR-URSSAF-004 ✅ |
| Allocation of the balance (SOLTéA) | FR-CDC-001 ✅ |
| Payroll tax 2501-SD | FR-DGFIP-003 ✅ |
| Payroll tax annual 2502-SD | FR-DGFIP-003 ✅ (same spec, both forms) |
| Work accident declaration | FR-CPAM-002 ✅ |
| **Posted-worker declaration (SIPSI)** | ❌ **none** → **F-3** |

---

#### Check 4 — DD ↔ Report Specs (4-bucket) · 720 of 984 as delivered (73.2%)

**1,672** field rows were read from Sheet 4 across all 15 specs and bucketed on the spec's own
`System Mapping` (column L) annotation:

| Bucket | Rows | Correctly excluded from DD? |
|---|---|---|
| **DD — mapped to a DD field** | **720** | n/a — found |
| SYS — transmission envelope, norm-fixed value, return context | 382 | ✅ yes |
| CALC — produced by the payroll calculation | 206 | ✅ yes |
| Out-of-scope rubrique | 100 | ✅ yes |
| **DD — asserted missing ("open gap")** | **264** | ❌ **see F-1** |

Per the 4-bucket method, the 688 SYS / CALC / out-of-scope rows are **not** penalised. The DD bucket
is therefore 984, giving **720 / 984 = 73.2 % as delivered**.

**The 264 do not survive scrutiny.** Each was matched against the DD's 189 field names by exact
match, close string match and concept-token coverage:

| Adjudication | Rows |
|---|---|
| DD counterpart found, high confidence | **105** |
| DD counterpart found, likely | **51** |
| Calculated amount — CALC bucket, not a DD candidate | **25** |
| Unresolved (incl. descoped special regimes) | **83** |

Worked examples, spec assertion → DD reality:

| Spec row asserting "no DD counterpart" | DD defines |
|---|---|
| `FR-DSN-001` r112 · E-mail address | `E-mail Address` |
| `FR-CPAM-002` r3 · Employer's name or company name | `Employer Legal Name` |
| `FR-CPAM-002` r6 · SIRET of the establishment of attachment | `Establishment SIRET` |
| `FR-CPAM-002` r10 · Social security number | `Employee Social Security Number (NIR)` |
| `FR-CPAM-002` r16 · Date of hire | `Date and Time of Hire` |
| `FR-CPAM-002` r17 · Occupation | `Occupation Code (PCS-ESE)` |
| `FR-CPAM-002` r20 · Type of employment contract | `Contract Nature` |
| `FR-CARSAT-001` r4 · Net AT/MP contribution rate | `Occupational-Accident Net Rate (AT/MP)` |
| `FR-DSN-001` r124 · Former surname at birth | `Surname at Birth` (change-block prior value) |

**All 17** of `FR-CPAM-002`'s open gaps and the **single** `FR-CARSAT-001` gap are false — every one
has a DD counterpart. The DAT spec names fields by their French form labels while the DD uses
canonical names, so a name-key join could not match them.

Two further sub-populations are mislabelled rather than missing:

- **~25 calculated amounts**, almost all in `FR-DGFIP-003`: *"Tax due for the month or the quarter"*,
  *"Base at the normal rate — metropolitan France"*, *"Normal-rate tax"*, *"Balance of tax payable"*.
  These are payroll-tax computation outputs. They are marked `payroll master data`, which is wrong on
  its face, and per the 4-bucket method they must not be counted against the DD at all.
- **Descoped special-regime rubriques** labelled as open gaps instead of out-of-scope: *College
  (CNIEG)*, *Balance of accrued and untaken leave (ENIM)*, *Geographic FINESS number*, *Live-performance
  service provider label number*, *Entertainment promoter licence number*, *Public employer internal
  number*, *Active-service rate*. `shared/FR_regime_scope_note.txt` locks this build to the *régime
  général* and names CNIEG and ENIM as out of scope; `scope_manifest.json` records 13 descoped
  employment types. The specs already carry the correct label — `rubrique out of scope for this
  build` — and use it 100 times. These rows should carry it too.

Corrected for false gaps and bucket errors, true DD↔Spec alignment is approximately **89–92 %**.

---

#### Check 5 — Global WTC coverage · 300 of 300 (100%)

The `Global WTC Coverage` sheet asserts that all 300 baseline pay element codes appear in the
Wage Type Catalogue *in baseline order at rows 2–301, none skipped, none duplicated, none excluded*.
This audit tested that claim position by position against `shared/Global_WTC_V1_0.xlsx`:

| Test | Result |
|---|---|
| Baseline codes in `Global_WTC_V1_0.xlsx` | 300 |
| Order/code mismatches across positions 1–300 | **0** |
| Baseline codes absent from the catalogue | **0** |
| Catalogue rows 302–375 (France-specific additions) | 74, all `FR-0xx`, none carrying a global code |

**300 included · 0 excluded · 100 % coverage.** The claim is exact.

---

#### Check 6 — Scope discipline · 0 violations

| Rule | Result |
|---|---|
| No calculated amounts or Base Salary in the DD | ✅ 0 of 189 field names match calculated/base-salary patterns |
| No identification data in the WTC | ✅ only "Birth allowance" (row 228) trips an identifier regex — a wage type, not identity data |
| No full field specs in CCG Module 2 | ✅ six data groups, explicit pointer to the DD |
| No full field specs in CCG Module 10 | ✅ *"Field-level layouts … are held in the France Report Specifications and are not reproduced here."* |

---

#### Check 7 — Report Spec format compliance · 15 of 15 (100%)

Every one of the 15 specs passes every sub-test:

- **9 sheets, correct names, correct order** — 15/15
- **Sheet 4 has 21 columns A–U** with a header **identical across all 15 files** — 15/15
- **Header row `FF4472C4`, white, bold** — 15/15
- **Row colours applied** — 15/15 (amber `FFFFEB9C`, blue `FFBDD7EE`, green `FFC6EFCE`, red `FFFFC7CE`, grey `FFD6DCE4`)
- **Payroll Scope Summary green/red** — 15/15 carry both `FFC6EFCE` and `FFFFC7CE`
- **Population Rules completed** — 15/15, between 16 and 26 populated rows each

Verified 21-column header: `Field Name (EN) · Field Name (FR) · Record Type · Field Position ·
Payroll Field (Y/N) · Mandatory (Y/N/C) · Conditional Reason · Position (Start-End) · Field Length ·
Format · Example · System Mapping · Field Explanation · Relevant for Payroll · Option Values ·
Rounding · Negative (Y/N) · Value Type · Reporting Frequency · Query to RA · RA Comments`

---

#### Check 8 — v2.4 standards · 5 of 5 artifact classes

**CCG — 13 official modules, exact titles, template Q&A format.** All 13 module titles are
**byte-identical** to `shared/CCG_TEMPLATE_QUESTIONS.md`. The delivered `.docx` carries 14 Heading 1
(13 modules + Table of Contents), 39 Heading 2, **149 Heading 3** and 202 tables. The 149 H3s
decompose exactly:

| | Template | CCG | Missing | Invented |
|---|---|---|---|---|
| Questions | 136 | 136 | **0** | **0** |
| Deliverables | 13 | 13 | **0** | **0** |
| **Total H3** | 149 | **149** | 0 | 0 |

Module 12 renders its five template scenarios as `Deliverable: Example N — <scenario>` and adds a
sixth France-specific scenario; the scenario text is the template's own. No question was dropped.

**DD — CZ V2.0 format, blue columns only.** 8 sheets in CZ order (`Version Control`, `Introduction`,
`Instructions`, `ID Information`, `Country Fields`, `Country Option Mappers`, `Currency Codes — ISO
4217`, `Country Codes — ISO 3166-1`). Header rows match CZ V2.0 column-for-column.

**WTC — CZ V2.0 + Global WTC baseline + Form Reference Guide.** 6 sheets, 374 catalogue rows,
`Global WTC Coverage` (392 rows) and `Form Reference Guide` (51 rows) both present.

**Report Specs — Spain 9-sheet with 21-column Sheet 4.** 15/15 (Check 7).

**Payslip — 8-sheet Mercans standard, navy/grey palette.** Sheet contract matches exactly:
`How to set up Payslip · Compliance Payslip · France (EN) · France (FR) · Payslip Spec ·
Field Option · Population Range · Unit Rate Details`. Palette is navy `FF1F3864` / greys
`FFDCDCDC`, `FFF2F2F2`, `FFA9A9A9` / accent `FFFCE4D6`. The `NET PAID` band (row 76, both language
sheets) is navy, **not** green — see **m-3**, which is a query against the standard rather than a
France defect.

---

#### Check 9 — v2.4 NEW · composite key / inter-field constraints · 3 of 4

| Check | Result |
|---|---|
| **C13** composite-key fields documented in Sheet 4 column M | ⚠️ **53 of 90 (58.9 %)** → **m-1** |
| **C16** conditional fields bidirectionally documented | ✅ **100 %** — 700/700 spec rows, 125/125 DD CM fields |
| **C17** Form Reference Guide present in WTC | ✅ 51 rows, category → spec file → sheet → **actual row number** |
| **C20** scope decision audit trail complete | ✅ complete |

**C13.** 90 rows across the 15 specs name a composite identifier (SIRET, SIREN, NIC, NIR, NTT).
53 carry a `Composite Key` breakdown in column M and the documentation is substantive where present
— *"SIREN in positions 1 to 9, establishment sequence (NIC) in 10 to 13, check digit in 14"*. 37 do
not, concentrated in repeated NIR/NTT rows in `FR-DSN-001` and in every `Head-office NIC` row.

**C20.** `scope_manifest.json` v1.1 carries `scope_decided_by`, `scope_decided_on`, a source
artifact, 12 in-scope and 13 out-of-scope employment types with rationale, 15 in-scope and 13
out-of-scope authority filings each with a descoping reason and client impact, 22 known failure
patterns, a changelog and 3 known limitations. This is a complete audit trail — with the two
integrity defects noted in **F-1** and **F-3**.

---

### GLOBAL WTC COVERAGE SUMMARY

| | |
|---|---|
| Baseline codes in `Global_WTC_V1_0.xlsx` | **300** |
| **Included** | **300 (100 %)** |
| **Excluded** | **0** |
| Position/order mismatches | **0** |
| France-specific additions (`FR-001`–`FR-074`) | **74** |
| Total catalogue rows | **374** |

No exclusion reasons are required, because nothing was excluded. The coverage sheet further asserts
every global code was configured fresh for France rather than copied from Belgium; the code and
ordering half of that claim is verified here, and the Belgium catalogue is a different build's
artifact outside this audit's scope.

---

### ISSUES

#### MAJOR

**F-1 · 264 spec rows assert a DD gap that mostly does not exist; the registered limitation
misstates both its size and its example**

*Severity: MAJOR · 12 of 15 specs · `scope_manifest.json` · `FR-ALIGNMENT-PATCH.md`*

264 Sheet 4 rows carry `NO DD COUNTERPART although this row is marked payroll master data —
registered as an open gap in FR-ALIGNMENT-PATCH.md for scope owner adjudication`. Adjudicating each
against the DD's 189 fields and 413 option-mapper rows: **≥156 have a DD counterpart**, **~25 are
calculated amounts** that are not DD candidates under the 4-bucket method, and a further tranche are
special-regime rubriques the build already descoped in `shared/FR_regime_scope_note.txt` and
`scope_manifest.json`. All 17 gaps in `FR-CPAM-002` and the 1 in `FR-CARSAT-001` are false.

Two integrity defects compound it. `FR-LIM-001` records **199** rows where the artifacts carry
**264** — the limitation and the deliverables disagree. And it nominates *employee e-mail address*
as the one *"genuine omission"*; the DD defines `E-mail Address`, and that row appears in this
audit's exact-match list twice (`FR-DSN-001` r112, `FR-DSN-002` r90).

Root cause: the reconciliation joined on the NEODeS rubrique. Six of the filings are not NEODeS
filings — DPAE cites Labour Code articles, the DAT cites form field labels, the payroll-tax return
cites form positions — so the join could not run, and its non-result was written into the delivered
workbooks as a positive finding.

> **Fix.** Re-run the reconciliation on field name plus concept for the six non-NEODeS specs.
> Re-bucket the ~25 calculated rows to CALC. Re-label the descoped-regime rows with the existing
> `rubrique out of scope for this build` wording. Then restate `FR-LIM-001` against whatever genuinely
> survives — on this evidence a small fraction of 264 — and correct its example. **No research
> required; this is an annotation pass over data already held.**

---

**F-2 · Meal and communication-tools benefits in kind have no wage type**

*Severity: MAJOR · `02-wtc/FR-WTC-001-v1.0.xlsx` · CCG Module 7*

CCG Module 7 sets a statutory flat valuation for four BIK categories. Accommodation (62400/62410)
and company vehicle (62500) have wage types. **Meals** (EUR 5.50 per meal, EUR 11.00 for two, no
benefit where the employee contributes at least EUR 2.75) and **communication tools** (10 % of the
inclusive purchase price or of the annual subscription) have none — confirmed by a sweep of all 24
columns across all 374 rows in English, French and explanation text. Meal *vouchers* (62670) and
meal *allowances* (62570/62630) are different items with different legal bases and do not cover it.

Consequence: the payroll engine cannot value two benefits the CCG requires it to value. Both feed
the DSN remuneration block and both are contributory, so the gap reaches the filing, not just the
payslip.

> **Fix.** Add four wage types — meal BIK at flat value, meal BIK at real cost, communication-tools
> BIK, and an employee-contribution offset — mirroring the accommodation pattern (62400/62410/62403).
> The rates and rules are already in CCG Module 7; no research required.

---

**F-3 · Posted-worker declaration is in scope in the CCG, out of scope in the manifest, and absent
from the filing register**

*Severity: MAJOR · CCG Module 10 · Module 11 · `scope_manifest.json`*

Module 10's table headed **"In scope for the payroll engine"** lists the posted-worker declaration
(Ministry of Labour, SIPSI, per posting, before the posting begins). Three artifacts contradict it:

- `scope_manifest.json` descopes it — *"The posting declaration (SIPSI) is an administrative
  obligation of the receiving entity, not a payroll output"* — with a client-impact note;
- CCG Module 11 says posted workers are *"largely outside payroll scope"*;
- `authority_filings.out_of_scope` holds 13 entries and the posted-worker declaration is **not among
  them**, so it is neither in the in-scope register (15 filings, all with specs) nor the out-of-scope
  one.

It has no spec, which is the correct outcome given the descoping decision. The defect is that the
CCG asserts the opposite and the filing register records neither position.

> **Fix.** Move the row from Module 10's in-scope table to its out-of-scope table, carrying the
> manifest's existing reason and client impact. Add a matching `FR-MOL-001` entry to
> `authority_filings.out_of_scope` so the register is complete. One-paragraph edit, no research.

---

#### MINOR

**m-1 · C13 composite-key documentation covers 53 of 90 eligible identifier fields (58.9 %)**

37 rows naming a SIRET, SIREN, NIC, NIR or NTT carry no `Composite Key` breakdown in column M —
every `Head-office NIC` row across four specs, the repeated NIR/NTT rows in `FR-DSN-001`
(rows 513–567), and single rows in AGIRC, CDC, CPAM-003, DGFIP-002 and DGFIP-003. Where present the
documentation is good; it simply was not applied uniformly.

> **Fix.** Propagate the existing SIRET and NIR breakdown text to the 37 rows. Mechanical.

**m-2 · DD filename says v1.0; its Version Control and all 15 specs say v1.1**

`FR-DD-001-v1.0.xlsx` contains a Version Control row `1.1 · 2026-08-27 · Alignment patch … ·
Released`, and all 15 specs cite `reconciled against FR-DD-001 v1.1`. The filename, the QA brief and
`scope_manifest.json` all reference v1.0. Anyone diffing by filename will believe they hold the
pre-patch file.

> **Fix.** Rename to `FR-DD-001-v1.1.xlsx` and update the manifest reference and the specs' citation
> path. Alternatively revert the Version Control row if v1.1 was not intended to ship.

**m-3 · Green net-pay emphasis absent — but the standard and the precedent disagree**

The v2.4 brief calls for green net-pay on the payslip. FR's `NET PAID` band (row 76, both language
sheets) is navy `FF1F3864`, and green `FFC6EFCE` appears once, on a legal-basis note. **This is not
a France defect:** the delivered Belgium payslip uses the same navy `FF1F3864` for `NET AMOUNT DUE
AND PAID` and contains no green at all, and `shared/REFERENCE_Payslip_Tunisia.xlsx` uses navy
`FF0B5394` for `Net Pay`. FR's palette matches the BE precedent exactly. The brief's clause is
implemented by no delivered artifact.

> **Fix.** Raise with the standard owner and settle it once: either amend the v2.4 wording to match
> the navy precedent, or open a propagation item covering FR **and** BE. Do not patch France alone —
> that would break consistency with the only signed-off precedent.

---

### v2.4 COMPLIANCE SUMMARY

| Requirement | Status | Evidence |
|---|---|---|
| CCG — 13 modules, exact titles | ✅ | 13/13 byte-identical to template |
| CCG — template Q&A as H3 | ✅ | 136/136 questions + 13/13 deliverables = 149 H3 |
| DD — CZ V2.0 format, blue columns only | ✅ | 8 sheets in CZ order, headers match |
| WTC — CZ V2.0 + Global baseline | ✅ | 300/300 in order, 74 FR additions |
| WTC — Form Reference Guide (C17) | ✅ | 51 rows, real row numbers |
| Report Specs — Spain 9-sheet, 21-col Sheet 4 | ✅ | 15/15 identical headers |
| Payslip — 8-sheet, navy/grey | ✅ | contract exact; green net-pay → m-3 |
| C13 — composite keys in Sheet 4 col M | ⚠️ | 53/90 → m-1 |
| C16 — conditional fields bidirectional | ✅ | 700/700 and 125/125 |
| C20 — scope decision audit trail | ✅ | complete; integrity defects in F-1, F-3 |

---

### SCORING

| Dimension | Weight | Score | Weighted |
|---|---:|---:|---:|
| Structural / format compliance (Checks 7, 8) | 30 | 30 | 30.0 |
| Content coverage (Checks 1, 2, 5) | 25 | 24 | 24.0 |
| Cross-artifact alignment (Checks 3, 4) | 25 | 15 | 15.0 |
| Scope discipline and audit trail (Checks 6, 9) | 20 | 18 | 18.0 |
| **Total** | **100** | | **87.0** |

Alignment is scored down hardest because F-1 put an incorrect assertion into 12 delivered workbooks
and then escalated it to a scope question in the manifest — the one place where a reader has no way
to detect the error without re-running the join.

---

### READINESS VERDICT

## ⚠️ NEEDS PATCHES

France is close to ready and the remaining work is small, bounded and entirely mechanical. **No
finding requires new legal research, and none touches the correctness of a rate, threshold or legal
basis.** The build's sourcing is genuinely strong: claims trace to Social Security Code and Labour
Code articles, the NEODeS CT2026.1 norm is cited at field level, and every one of the build's own
falsifiable claims that this audit re-derived — the 300-code baseline coverage, the 149 H3 headings,
the identical 21-column headers, the 100 % conditional documentation — held up exactly.

**Blocking before hand-off to the dev team:**

1. **F-1** — re-run the DD↔Spec reconciliation on field name for the six non-NEODeS specs, re-bucket
   the calculated rows, re-label the descoped-regime rows, then restate `FR-LIM-001` and correct its
   e-mail-address example. Largest item; still an annotation pass over data already held.
2. **F-2** — add the meal and communication-tools BIK wage types. Rates are already in CCG Module 7.
3. **F-3** — move the posted-worker row to Module 10's out-of-scope table and add the matching
   `authority_filings.out_of_scope` entry.

**Non-blocking:** m-1 (propagate composite-key text to 37 rows), m-2 (DD version rename), m-3 (raise
the green-net-pay clause with the standard owner — do not patch France in isolation).

Once F-1 through F-3 land, this build is **READY FOR DEV TEAM**.

---

### AUDIT METHOD AND DIVERGENCES FROM THE SUPERSEDED REPORT

Every figure here was measured from the delivered binaries with `openpyxl` and `python-docx`.
Claims made by the artifacts about themselves were treated as hypotheses to test, not as evidence.
Three of this audit's own intermediate results were wrong and were corrected before reporting: a
literal CCG↔WTC match that under-reported coverage at 31 %, six Module 2 concepts scored as missing
that are present in the option mappers, and an initial reading of 952 "NO DD COUNTERPART" rows that
collapsed to 264 once justified SYS/CALC/out-of-scope exclusions were separated out.

Divergences from the 12:21 report, which is preserved at `FR-QA-REPORT.md.bak-20260828-124820`:

| Item | Superseded report | This audit | Why |
|---|---|---|---|
| DD↔Spec alignment | 486 / 562 (86.5 %) | **720 / 984 (73.2 %)** | Denominator: 1,672 Sheet-4 rows were read; the DD bucket is 984, not 562 |
| False "no DD counterpart" rows | "at least 14" | **≥156 of 264** | Adjudicated all 264 by exact, close and concept match |
| C13 composite key | 39 / 71 (55 %) | **53 / 90 (58.9 %)** | Eligible population measured as all SIRET/SIREN/NIC/NIR/NTT rows |
| CCG ↔ WTC | 245 / 246 (99.6 %) | 2 confirmed gaps | Same conclusion; ratio not reproducible, so gaps are named individually |
| CCG Module 2 ↔ DD | 21 / 21 | 35 / 35 | Both 100 %; different concept enumeration |
| Green net-pay | not raised | **m-3** | BE and Tunisia precedent contradict the brief |
| `FR-LIM-001` count drift (199 vs 264) | not raised | **part of F-1** | Manifest and artifacts disagree |

Both reports independently reach the same three MAJOR findings and the same overall verdict of
**NEEDS PATCHES**. This audit scores F-1 materially larger, and adds the `FR-LIM-001` count drift
and the payslip palette query.


# Part 2 - FR alignment patch: Data Dictionary vs Report Specs (verbatim)

## FR-ALIGNMENT-PATCH — Data Dictionary vs Report Specs

**Date:** 2026-08-27
**Patched by:** Wallisson Gomes
**Scope:** `FR-compliance/05-data-dictionary/FR-DD-001-v1.0.xlsx` (v1.0 → v1.1) against the
15 delivered specs in `FR-compliance/04-reports-spec/` (each v1.0 → v1.1).

### Inputs actually read

| Artifact | What was read |
|---|---|
| `05-data-dictionary/FR-DD-001-v1.0.xlsx` | ID Information (25 rows), Country Fields (164), Country Option Mappers (54 mappers / 303 codes), Version Control |
| `04-reports-spec/*.xlsx` — all 15 | Sheet 4 field specification (1,428 field rows × 21 columns), Sheet 6 Field Options (3,501 code rows), Version Control, Payroll Scope Summary, Population Rules |
| `01-ccg/FR-CCG-001-v1.0.docx` + `01-ccg/modules/` | 13 content modules, for the mappers authored from the CCG rather than from NEODeS |
| `scope_manifest.json` | `option_mapper_scope`, `employment_types`, régime-général descoping |
| `05-data-dictionary/fr_dd_data_mappers.py` | the private-sector filter and its per-mapper `excluded` reasoning |
| `04-reports-spec/_lib/fr_norm.py` | the build's own definition of column E |

Linkage between the two sides is the **NEODeS rubrique**: the DD records one in
`Additional Notes` for 162 of its 189 fields, and the specs carry it in column D.
That gives 165 DD-side rubriques and 1,142 spec-side rubrique rows to join on.

---

### Patch log

| Check | Field / Mapper | Issue found | Fix applied | File patched |
|---|---|---|---|---|
| 1 | `Contract Nature` (S21.G00.40.007) | Codes **32** (contrat d'appui au projet d'entreprise) and **60** (contrat d'engagement éducatif) were dropped by the private-sector filter but not named in the mapper note, breaching the module's own stated discipline that every exclusion is named | Both named in the note with their legal ground; 60 additionally flagged as a **scope-owner decision**, not a technical exclusion | DD `Country Option Mappers` G50 |
| 1 | `Public-Policy or Collectively Agreed Scheme` (S21.G00.40.008) | Code **80** (contrat de génération) dropped without being named | Named as a closed historic scheme, abolished by Ordonnance n° 2017-1387 of 22 Sept 2017 | DD `Country Option Mappers` G61 |
| 1 | 14 mappers / 122 distinct codes | The DD filters these codes out of the régime-général perimeter; the specs carried them with **no marking at all**, so DD and spec disagreed with nothing to reconcile them. Version Control claimed such codes were "marked out of scope and coloured as excluded" — true of Sheet 4 rubriques (100 red rows), **false of Sheet 6 codes** | 247 option rows marked `OUT OF SCOPE …` in column E and filled `FFFFC7CE`, the same red the spec already uses for out-of-scope rubriques on Sheet 4 | 5 specs, `Field Options` |
| 1 | all 54 mappers | *No defect.* 650 code-pairs shared between DD and specs compared on code value **and** French local name | none — 650/650 matched exactly | — |
| 2 | column E, 1,428 rows | *No defect.* See "Check 2 — why nothing was changed" below | none | — |
| 3 | 700 conditional fields | *No defect.* Every `Mandatory=C` field already carries a Conditional Reason | none | — |
| 3 (C16) | 42 bidirectional references | *No defect.* Every in-file rubrique reference reciprocates | none — 0 one-way references | — |
| 4 | 132 option tables | *No defect.* No field points at a missing table; no table is unreferenced | none | — |
| 4 | `Field Options` column D, **all 15 specs** | Header read **`Description (NL)`** — Dutch, a Belgium-template residue. The column contains French | Renamed to `Description (FR)` | 15 specs, `Field Options` |
| 5 | NIR, NTT, SIRET, SIREN, cancelled-declaration id | 172 identifier fields longer than 8 characters; **none** documented a Composite Key Structure, although the DD documents the decomposition in its Pre-Defined Format column | 58 rows given a `Composite Key Structure` block in column M: each sub-field's position, length, source and persistence | 15 specs, Sheet 4 col M |
| 6 | S21.G00.71.002, S21.G00.72.001, S10.G00.00.006 | Coded identifiers whose codes carry a real prefix grammar (`RU**`, `RET*`, `P{YY}V{NN}`) documented only as "closed list" | Prefix pattern appended to column J | 10 rows across the specs |
| — | column L, 1,357 rows | Every spec still carried `[provisional - pending FR-DD-001]`, and Version Control said the DD was `NOT AVAILABLE, PENDING STAGE 4`. The DD has existed since 27 Aug | 403 mappings resolved to `[CONFIRMED against FR-DD-001 v1.1 — <sheet> row <n>: <field>]`; the other 952 marked reconciled **with the reason** there is no DD counterpart | 15 specs, Sheet 4 col L |
| — | Version Control | Stale forward reference to the DD | "Downstream alignment" rewritten; v1.1 row inserted under the preserved v1.0 row in all 15 specs and in the DD | 16 files |

---

### Check 2 — why nothing was changed

The instruction reads: *a calculated field (amount, total, tax) is not a payroll master
data field*. Applying that literally flags 243 rows where column E is `Y` and the value
type is `Calculated`, plus 16 `Declared Contact` rows. **None of them is a
misclassification**, for two reasons that were verified rather than assumed:

1. The build defines column E explicitly, in `_lib/fr_norm.py`: *"'Payroll Field (Y/N)'
   asks whether PAYROLL must act on the value, not whether payroll populates it."*
   It is not a master-data flag, so a computed amount is correctly `Y`.
2. The distinction the check is protecting **already exists**, on every row, in column N:
   573 rows read `Yes - payroll master data`, 219 read `Yes - produced by the payroll
   calculation`. Column E and column N agree on 1,416 of 1,428 rows; the 12 exceptions are
   nuanced prose (`Yes, indirectly`, `Yes as a CONTROL`) on procedural rows, not field rows.

The 16 `Declared Contact` rows are consistent on both sides: the DD calls them "Filing
configuration", the spec says "populated by the filing component and not by the payroll
calculation". Flipping 243 rows would have destroyed a working distinction to satisfy a
reading the artifact does not use. The finding is recorded here instead.

---

### Open items — NOT fixed, and why

**1. 199 spec rows marked "payroll master data" have no Data Dictionary counterpart**
(148 distinct rubriques). All 199 are yellow-filled `Yes - payroll master data` on Sheet 4,
so the specs assert it consistently. Breakdown:

| Group | Rubriques | Character |
|---|---|---|
| `S21.G00.41`, `.31`, `.16` — *changement / former value* blocks | 57 | Change-history echoes of fields the DD already holds; a DD carries the current value, not the prior one |
| `S89.G00.67/87/88/89` — employee share schemes | 30 | **Already registered** as an open scope question in `FR-DD-001-build-log.md` |
| `S21.G00.40` sector fields (maritime, CNIEG, entertainment, public employer) | 23 | Mostly outside the locked régime-général perimeter |
| Event blocks `.60 .62 .65 .66 .98 .85 .13 .34 .44 .72 .73 .86` | 37 | Per-event data rather than master data |
| `S21.G00.30.018` employee e-mail address | 1 | The most likely genuine omission |

Closing this means adding up to 148 fields to the Data Dictionary. That is a Stage-4 scope
decision, not an alignment edit — adding them here would be inventing scope the owner has
not granted. Each affected spec row now says so in column L rather than claiming a mapping
that does not exist.

**2. Contract Nature code 60 — contrat d'engagement éducatif.** It *is* a private-law
contract under the régime général, so the private-sector filter alone does not exclude it;
it is excluded because it is not one of the six contract types in
`scope_manifest.json → option_mapper_scope.contract_type`. Recorded in the mapper note as
an owner decision. If the owner rules it in, it is added with its verbatim norm label.

**3. Version Control rows 19 and 20 still say `FR-WTC-001` and `FR-SIR-001` are
`NOT AVAILABLE, PENDING STAGE 5 / 6`.** Both artifacts now exist on disk
(`02-wtc/FR-WTC-001-v1.0.xlsx`, `03-statutory-integrations/FR-SIR-INDEX-001-v1.0.docx`,
the latter under a different id than the row asserts). Those statements are stale, but this
patch aligned the specs against the **Data Dictionary** only. Rewriting them would assert an
alignment that has not been performed. Left for a WTC/SIR alignment pass.

---

### Verification

`07-qa-crosscheck/_align/verify.py` re-extracts all 16 patched workbooks and re-runs every
check. **All 26 assertions pass**, including the ones that prove the patch was surgical:

- 1,428 field rows and 3,501 option rows before and after — no row added or lost
- no `field_en / field_fr / field_position / position / length / example / payroll_field /
  mandatory / cond_reason / value_type` cell differs from its pre-patch value — **0 drifts**
- no option code added or removed in any table
- DD still 54 mappers / 303 codes; its 25 image, comment and table zip parts survive
- 650/650 shared code-pairs still match on value and French local name
- 0 `[provisional - pending FR-DD-001]` markers and 0 `FR-DD-001 - NOT AVAILABLE` remain
- all 15 specs carry both their v1.0 history row and the new v1.1 row

The DD was patched by **zip-level XML surgery**, not openpyxl: it contains images, cell
comments and 13 table parts that an openpyxl round-trip would have silently dropped. The
15 specs contain no such parts (verified first) and were safe to rewrite with openpyxl.

Pre-patch copies and SHA-256 hashes: `07-qa-crosscheck/_align/backup/`.
Scripts: `_align/extract.py`, `_align/patch_dd.py`, `_align/patch_specs.py`,
`_align/patch_vc.py`, `_align/verify.py`.


# Part 3 - Scope lock-in validation (verbatim)

## FR — SCOPE LOCK-IN VALIDATION

**Artifact validated:** `FR-compliance/scope_manifest.json` (50,117 bytes, mtime 2026-08-27 08:40)
**Schema:** `shared/scope_manifest_template.json`
**Gate:** BLOCKING — Stage 2 onward may not start until this gate passes.
**Validated on:** 27 August 2026
**Validator:** scope lock-in validation (v2.8, B7 + B1 enabled)
**Scope owner of record:** Wallisson Gomes, lock date 26 August 2026
**Upstream scope instrument:** `shared/FR_regime_scope_note.txt` (v2.6, régime général only)

---

### VERDICT

**PASS** — all six checks pass. Three non-blocking findings (W-01…W-03) are recorded for the
next stage. No B1 blocking finding: non-resident handling is present for every covered
income type.

| Check | Subject | Result |
|---|---|---|
| 1 | File exists, valid JSON | **PASS** |
| 2 | All required sections present and non-empty | **PASS** |
| 3 | `authority_filings.in_scope` field completeness | **PASS** — 15/15 |
| 4 | `integrations.inbound` product_mapping_required set | **PASS** — 8/8 set, 0 warnings |
| 5 | No code in both in_scope and out_of_scope for one mapper | **PASS** — 0 collisions |
| 6 | `known_failure_patterns_to_check` populated F1–F15 | **PASS** — F1–F22 present |
| B1 | Non-resident handling for covered income types | **PASS** — no blocking finding |

---

### CHECK 1 — FILE EXISTS AND IS VALID JSON

PASS. `FR-compliance/scope_manifest.json` parses. 19 top-level keys, all 12 template keys
present plus 7 France additions (`code`, `generated`, `source_artifact`, `mandate_document`,
`failure_pattern_notes`, and two mapper extensions). Header block fully populated:

```
country=France  country_code=FR  currency=EUR  year=2026  scope_version=1.0
scope_decided_by=Wallisson Gomes   scope_decided_on=2026-08-26
source_artifact=FR-CCG-001-v1.0.docx
mandate_document=FR-compliance/00-official-sources/ccg-sources/FR-CCG-source-register.md
```

No placeholder or empty-string values survive from the template.

---

### CHECK 2 — REQUIRED SECTIONS PRESENT AND NON-EMPTY

PASS. Every required section is present, correctly shaped and non-empty.

| Section | Required members | Populated |
|---|---|---|
| `employment_types` | in_scope, out_of_scope, rationale | 12 / 13 / 1,010-char rationale |
| `authority_filings` | in_scope, out_of_scope | 15 / 12 |
| `wage_type_categories` | in_scope, out_of_scope, special_rules | 35 / 7 / 16 |
| `option_mapper_scope` | per-mapper code lists | 9 mappers, 52 codes |
| `integrations` | outbound, inbound, both | 12 / 8 / 1 |

`option_mapper_scope` carries the five template mappers (`personal_id_type`,
`insurance_type`, `contract_type`, `correction_codes`, `benefit_type`) and adds four
France-specific ones (`working_time_type`, `withholding_rate_type`, `residence_status`,
`leave_type`). Additions are permitted; no template mapper is missing or empty.

The `employment_types` out-of-scope list carries all seven régimes spéciaux named in the
upstream scope note (RATP, ENIM, CNBF, CRPCEN, CAVIMAC, CNIEG/CAMIEG, and the catch-all),
each with a reason and a client-impact statement. The upstream instrument is honoured
exactly — nothing named there was silently dropped, nothing was added to it.

---

### CHECK 3 — AUTHORITY FILING FIELD COMPLETENESS

PASS. 15/15 in-scope filings carry all six required fields with no null, no empty string
and no out-of-enum value. `integration_type` is one of {inbound, outbound, both} in every
case; `product_mapping_required` is a JSON boolean in every case (never null, never a
string).

| filing_id | authority | frequency | format | integration_type | pmr |
|---|---|---|---|---|---|
| FR-DSN-001 | URSSAF (+ CNAV, CPAM, AGIRC-ARRCO, France Travail, DGFiP, insurers) | monthly | TXT | outbound | true |
| FR-DSN-002 | France Travail | per event, 5 days | TXT | outbound | true |
| FR-DSN-003 | CPAM | per event, 5 days | TXT | outbound | true |
| FR-URSSAF-001 | URSSAF (DPAE) | per hire | XML | outbound | true |
| FR-DGFIP-001 | DGFiP (PAS) | monthly, quarterly under 11 emp | TXT | both | true |
| FR-DGFIP-002 | DGFiP (compte rendu métier) | monthly/quarterly/annual | TXT | inbound | true |
| FR-CARSAT-001 | CARSAT (AT/MP rate) | annual + reclassification | XML | inbound | true |
| FR-URSSAF-002 | URSSAF (NIR certification) | monthly | TXT | inbound | true |
| FR-URSSAF-003 | URSSAF for Agefiph (DOETH) | annual | TXT | outbound | true |
| FR-URSSAF-004 | URSSAF (apprenticeship tax balance) | annual | TXT | outbound | true |
| FR-DGFIP-003 | DGFiP (taxe sur les salaires) | monthly/quarterly/annual | XML | outbound | true |
| FR-CPAM-002 | CPAM (work accident declaration) | per event, 48h | XML | outbound | **false** |
| FR-CDC-001 | Caisse des Dépôts (SOLTeA) | annual | XLSX | outbound | **false** |
| FR-CPAM-003 | CPAM (daily benefit statements) | per event | TXT | inbound | true |
| FR-AGIRC-001 | AGIRC-ARRCO | monthly | TXT | inbound | true |

All 12 out-of-scope filings carry `filing_id` plus a non-empty `descoping_reason` (and, beyond
the template minimum, `authority` and `client_impact`).

The two `product_mapping_required=false` entries are both **outbound** and both carry an
explicit justification — FR-CPAM-002 takes incident data held outside payroll and needs
only identity and a pay reference; FR-CDC-001 allocates an amount already declared by
FR-URSSAF-004. Neither is an F8 trigger (F8 concerns inbound flows). Recorded as advisory
W-03 so the Report Spec stage does not silently reinterpret them as mapped filings.

---

### CHECK 4 — INBOUND PRODUCT MAPPING (F8)

PASS, **0 warnings**. All 8 `integrations.inbound` entries and the 1 `both` entry carry
`product_mapping_required` explicitly, and every one is `true`. No inbound flow is
defaulted out of product mapping — the F8 pattern that has cost earlier countries a
rebuild does not appear here.

| id | counterparty | format | frequency | pmr |
|---|---|---|---|---|
| FR-DGFIP-002 | DGFiP | TXT | monthly/quarterly/annual | true |
| FR-URSSAF-002 | URSSAF | TXT | monthly | true |
| FR-CARSAT-001 | CARSAT | XML | annual | true |
| FR-CPAM-003 | CPAM | TXT | per event | true |
| FR-AGIRC-001 | AGIRC-ARRCO | TXT | monthly | true |
| FR-CLIENT-001 | client | — | — | true |
| FR-CLIENT-002 | client | — | — | true |
| FR-COURT-001 | court / bailiff | — | — | true |
| FR-DGFIP-001 (both) | DGFiP | TXT | monthly | true |

Two inbound flows deserve to be called out as correctly handled, because both are
routinely mis-scoped. **FR-DGFIP-002**, the *compte rendu métier*, is marked as the only
lawful source of an employee's withholding rate, with a parse-and-apply obligation and a
date check on every run. **FR-URSSAF-002** records that from June 2026 an uncorrected
anomaly on the capped gross base may be corrected by the authority itself under the
substituted-declaration power, so the flow must be acted on rather than archived. Both are
`pmr=true`.

---

### CHECK 5 — IN-SCOPE / OUT-OF-SCOPE COLLISIONS (F2)

PASS. 0 collisions, tested on ASCII-folded, punctuation-normalised labels.

| Section | in_scope | out_of_scope | overlap |
|---|---|---|---|
| employment_types | 12 | 13 | none |
| authority_filings | 15 | 12 | none |
| wage_type_categories | 35 | 7 | none |

`option_mapper_scope` follows the template shape — a flat list of in-scope codes per mapper
with no per-mapper `out_of_scope` member — so an intra-mapper collision is structurally
impossible. Three additional cross-section scans were run and all pass:

- **No out-of-scope filing leaks into `integrations`.** All 12 descoped filing_ids are
  absent from all three integration lists.
- **No integration_type contradiction.** All 15 in-scope filings appear in `integrations`
  under the same direction they declare (9 outbound, 5 inbound, 1 both). Zero mismatches.
- **The 6 extra integrations are legitimately non-statutory** — FR-BANK-001, FR-GL-001 and
  FR-PAYSLIP-001 outbound; FR-CLIENT-001, FR-CLIENT-002 and FR-COURT-001 inbound. They are
  integrations without being authority filings, which is correct, not an inconsistency.

Two **near-collisions** were examined by hand and cleared. Both are deliberate splits that
the manifest reconciles in its own text, not accidents:

1. *Overseas departments.* Descoped as an employment type (LODEOM exemption arithmetic),
   yet the 8% and 14.4% territorial withholding rates are an in-scope
   `withholding_rate_type` code. The `employment_types.rationale` states the split
   explicitly: "What is out of scope in the overseas departments is only the LODEOM
   exemption arithmetic." Consistent.
2. *Posted worker on an A1.* Descoped as an employment type ("no French payslip to
   produce"), yet present as an in-scope `residence_status` code. This is the correct
   design — the code exists so the engine can *recognise* and suppress the population.
   Carried forward as advisory W-02a so it is implemented as an exclusion flag and never
   as a payslip-producing population.

A third split is a real gap and is raised as W-01 below.

---

### CHECK 6 — KNOWN FAILURE PATTERNS (F1–F15)

PASS. `known_failure_patterns_to_check` contains 22 entries, F1 through F22 with no gaps —
F1–F15 as required, plus F16–F22. `failure_pattern_notes` supplies France-specific
substance for F18–F22: stale 2026 law references, the five HR-scope descopings, the
requirement that WTC codes come from the NEODeS CT2026.1.2 legend rather than a
neighbouring country's catalogue, the verified (not assumed) consolidated filing mechanic,
and a pointer to the 16 `special_rules`.

Two observations, neither blocking:

- The 22 entries are **bare identifiers** (`"F1"`, `"F2"`, …) rather than the template's
  labelled form (`"F1 - Option mapper alignment DD<->Specs"`). Verified against
  `scope_manifest.json.bak-20260827-084033`: the backup is identical, so this is an
  authoring shortfall, not drift introduced by the 27 August edit. The IDs resolve
  unambiguously against `shared/country_failure_log.md`, so downstream agents can still
  act on them. Recommend relabelling at the next `scope_version` bump.
- The canonical log now runs to **F31**. F23–F31 — including F29 (a fix applied in one
  direction certified as complete), F30 (gap registers proliferate with no country-level
  union) and F31 (a lint named "across ALL artifacts" covering a subset) — are not carried
  into the France checklist. Check 6 requires F1–F15 and is satisfied, so this does not
  block; but F23–F31 should be added before the QA stage, since all three named patterns
  bite at closure rather than at scoping.

---

### B1 — NON-RESIDENT HANDLING FOR COVERED INCOME TYPES

**PASS — no blocking finding.**

B1 makes missing non-resident handling blocking for any covered income type. The scope
manifest carries a non-resident dimension at four independent levels, and the CCG it
derives from resolves it per income type rather than generically:

- `employment_types.in_scope` — non-resident employees working in France and affiliated to
  the French scheme, withheld under General Tax Code Article 182 A.
- `option_mapper_scope.residence_status` — resident (CGI Art. 4 B, as modified by treaty),
  non-resident, French-scheme affiliation, and A1 posted worker, closed by the standing
  warning that tax residence and social security affiliation are independent tests.
- `option_mapper_scope.withholding_rate_type` — a dedicated non-resident code carrying the
  0/12/20 bands and the 0/8/14.4 overseas bands.
- `authority_filings.out_of_scope` FR-DGFIP-005 — CGI Article 197 A descoped on the ground
  that it is assessment-level, not withholding-level, with the note that an
  assessment-level levy was wrongly propagated into withholding artifacts in an earlier
  country. This is the correct exclusion, correctly reasoned.

The governing CCG carries an explicit **Resident and Non-Resident Treatment Matrix**
(`01-ccg/modules/m06_tax.md` §6.0) giving rate, base and method for each side of every
income family in scope — regular salary, severance and termination payments, equity,
contractor pay and benefits in kind — plus the overseas rates, the liberatory /
non-liberatory split of the 12% and 20% fractions, and the independence of the social
security test. Coverage extends beyond the matrix: `m09_termination.md` gives the resident
vs non-resident termination mechanics and the 10% flat deduction on the 182 A base;
`m11_advanced.md` handles mid-year change of residence as a date-split with a switch of
*mechanism*, not merely of rate, and handles the non-resident with two French employers
each consuming the progressive bands.

Every covered income type therefore has a determinate non-resident answer. The two
in-scope wage types with an inherent residence dimension — the impatriation premium
(CGI Art. 155 B) and expatriation supplements (CGI Art. 81 A) — are resident-side reliefs
by statutory construction and are documented as payroll-level items in `m11_advanced.md`.
Nothing covered is left without a non-resident treatment.

---

### FINDINGS (non-blocking)

#### W-01 — The L137-13 employer contribution has no scope row of its own

**Location:** `scope_manifest.json` → `wage_type_categories.out_of_scope[1]`
**Pattern risk:** F2 / F3
**Severity:** WARN — does not block this gate.

Free share and share option gains are descoped as an income type, which is correct. But the
same entry concedes that "only the 30% employer contribution (and, above EUR 300,000, the
10% employee contribution) touch the DSN", and the CCG confirms it at
`01-ccg/modules/m11_advanced.md`: the 30% employer contribution under Social Security Code
Article L137-13 is "payable in the month following the acquisition or the grant, and
declared in the DSN".

So an in-scope, DSN-declared payroll obligation exists only as a subordinate clause inside
an out-of-scope row. Under B7 that is an unrecorded scope decision, and it leaves the WTC
and the DSN Report Spec with no in-scope wage type to attach either contribution to. The
employer/employee split (30% employer under L137-13, 10% employee above EUR 300,000 under
L137-14) is exactly the shape F3 describes.

**Action:** before the WTC stage, promote both contributions to explicit
`wage_type_categories.in_scope` rows — declaration-only, outside the ordinary contribution
bands — while leaving the *gain* descoped. This is an addition, not a reversal.

#### W-02 — CGI Article 182 A ter is instructed but never scoped

**Location:** CCG `01-ccg/modules/m06_tax.md` §6.0, equity row → no counterpart in the manifest
**Severity:** WARN — does not block this gate.

The CCG states that for a non-resident, the acquisition gain on a French-source award is
subject to a specific withholding under General Tax Code Article 182 A ter and "must be
modelled separately". The manifest records no decision on it — it appears in neither
`authority_filings.in_scope` nor `authority_filings.out_of_scope`. Because the underlying
income type is descoped, the practical answer is almost certainly out of scope, but the CCG
has issued an instruction that the scope manifest never closes.

B1 does not bite here: 182 A ter attaches to an income type that is *not* covered, so this
is not missing non-resident handling for a covered type.

**Action:** add an explicit `authority_filings.out_of_scope` row (suggested id
FR-DGFIP-006) descoping 182 A ter as attaching to a descoped income type and operated by
the awarding entity rather than by payroll. One row closes the instruction.

##### W-02a — A1 posted worker: in-scope code for an out-of-scope population

**Location:** `option_mapper_scope.residence_status` vs `employment_types.out_of_scope`
**Severity:** ADVISORY.

Correct as designed — the code must exist for the engine to recognise and suppress the
population. Recorded so that the DD and Report Spec stages implement it as an exclusion and
routing flag only, and never as a payslip-producing population.

#### W-03 — Two in-scope filings carry product_mapping_required=false

**Location:** `authority_filings.in_scope` → FR-CPAM-002, FR-CDC-001
**Severity:** ADVISORY — correctly decided, recorded to prevent later reinterpretation.

Both are outbound, so neither triggers the F8 check, and both carry a reasoned
justification. Recorded so the Report Spec stage treats them as in-scope filings that
deliberately carry no wage-type or option-mapper dependency, rather than re-deriving a
mapping for them or dropping them from the filing inventory.

---

### SCOPE DECISION REGISTER (v2.8 B7)

Every scope decision in the manifest, one row each — 151 rows: 119 in-scope, 32 out.

**Column semantics.** *OWNED-UPSTREAM* — the decision was made above this build (the scope
owner's lock of 26 August 2026 recorded in `shared/FR_regime_scope_note.txt`) rather than
derived from law by the CCG agent; 8 rows, being the seven named régimes spéciaux and the
MSA filing. *INBOUND-DATA-CONTRACT* — HRB must parse or act on data arriving from an
external party; 19 rows. *REVERSIBLE* — the decision can be changed later without new
research or a rebuild. In-scope decisions are reversible because the research is already
done; descopings are reversible where they are routing calls (HR-scope, not-a-payroll-
filing) but **not** where rates and mechanics were deliberately left unresearched. The 8
irreversible rows are the régimes spéciaux and MSA, each of which the manifest itself marks
"separate scoping required".

| DECISION | IN-SCOPE | OWNED-UPSTREAM | INBOUND-DATA-CONTRACT | REVERSIBLE | BASIS |
|---|---|---|---|---|---|
| EMP-IN: Permanent contract (contrat a duree indeterminee, CDI) | Y | N | N | Y | employment_types.rationale - regime general lock, 26 Aug 2026 |
| EMP-IN: Fixed-term contract (contrat a duree determinee, CDD), including the 10% end-of-contract indemnity | Y | N | N | Y | employment_types.rationale - regime general lock, 26 Aug 2026 |
| EMP-IN: Part-time employees, including the prorated social security ceiling and additional hours (heures complementaires) | Y | N | N | Y | employment_types.rationale - regime general lock, 26 Aug 2026 |
| EMP-IN: Managerial grade (cadre) and non-managerial employees | Y | N | N | Y | employment_types.rationale - regime general lock, 26 Aug 2026 |
| EMP-IN: Employees on an annual day-count arrangement (forfait annuel en jours) | Y | N | N | Y | employment_types.rationale - regime general lock, 26 Aug 2026 |
| EMP-IN: Apprenticeship contracts (contrat d'apprentissage) | Y | N | N | Y | employment_types.rationale - regime general lock, 26 Aug 2026 |
| EMP-IN: Professionalisation contracts (contrat de professionnalisation) | Y | N | N | Y | employment_types.rationale - regime general lock, 26 Aug 2026 |
| EMP-IN: Interns (stagiaires) receiving a statutory gratuity, exempt to 15% of the hourly ceiling per hour of attendance | Y | N | N | Y | employment_types.rationale - regime general lock, 26 Aug 2026 |
| EMP-IN: Temporary-agency workers (interimaires), where the client is the agency and therefore the employer | Y | N | N | Y | employment_types.rationale - regime general lock, 26 Aug 2026 |
| EMP-IN: Company officers treated as employees (assimiles salaries): chair or managing director of a SAS or SA, minority or equal-shareholding manager  | Y | N | N | Y | employment_types.rationale - regime general lock, 26 Aug 2026 |
| EMP-IN: Employees whose place of work is in Alsace-Moselle (Bas-Rhin, Haut-Rhin, Moselle): the general scheme plus the 1.30% local employee health con | Y | N | N | Y | employment_types.rationale - regime general lock, 26 Aug 2026 |
| EMP-IN: Non-resident employees working in France and affiliated to the French scheme, withheld under General Tax Code Article 182 A | Y | N | Y | Y | General Tax Code Article 182 A |
| EMP-OUT: RATP scheme (Paris transport) | N | Y | N | N | Regime special outside the regime general. Descoped before Stage 1 by the scope owner, 26 August 2026. Rates and mechanics deliberately not researched |
| EMP-OUT: ENIM scheme (maritime and seafarers) | N | Y | N | N | Regime special outside the regime general. Descoped before Stage 1 by the scope owner, 26 August 2026. |
| EMP-OUT: CNBF scheme (lawyers) | N | Y | N | N | Regime special outside the regime general. Descoped before Stage 1 by the scope owner, 26 August 2026. |
| EMP-OUT: CRPCEN scheme (notarial staff) | N | Y | N | N | Regime special outside the regime general. Descoped before Stage 1 by the scope owner, 26 August 2026. |
| EMP-OUT: CAVIMAC scheme (clergy) | N | Y | N | N | Regime special outside the regime general. Descoped before Stage 1 by the scope owner, 26 August 2026. |
| EMP-OUT: CNIEG and CAMIEG schemes (gas and electricity sector) | N | Y | N | N | Regime special outside the regime general. Descoped before Stage 1 by the scope owner, 26 August 2026. |
| EMP-OUT: Any other sector-specific caisse outside the regime general | N | Y | N | N | Catch-all for the regimes speciaux. Acknowledged as existing in the CCG; rates and mechanics deliberately not researched, per the locked scope decisio |
| EMP-OUT: Agricultural employees under the MSA scheme (regime agricole) | N | N | N | Y | A separate collection network (Mutualite Sociale Agricole) with its own DSN channel, its own contribution set and its own paid-leave arrangements. Out |
| EMP-OUT: Majority-shareholding managers of a SARL, and other self-employed workers (travailleurs non salaries) | N | N | N | Y | Self-employed under the SSI scheme. Contributions are assessed and paid personally, outside payroll entirely. Not an employment type the engine can pr |
| EMP-OUT: Public-sector statutory staff (fonctionnaires) and their pension schemes | N | N | N | Y | Outside the private-sector regime general to which this build is scoped. |
| EMP-OUT: Workers posted into France who remain affiliated to a foreign scheme under a portable document A1 | N | N | Y | Y | No French social security contributions are due and the foreign employer pays the worker. There is no French payslip to produce. The posting declarati |
| EMP-OUT: Mayotte | N | N | N | Y | A distinct social security scheme with its own contribution set and its own minimum wage (EUR 9.56 an hour from 1 June 2026 against EUR 12.31 national |
| EMP-OUT: Overseas departments - the LODEOM specific exemption schemes (Guadeloupe, Martinique, Guyane, La Reunion) | N | N | N | Y | The general degressive reduction is replaced by the overseas exemption schemes, which are more generous and structured differently. Their existence, t |
| FILING-IN: FR-DSN-001 - URSSAF (and, through the same file, CNAV, CPAM, AGIRC-ARRCO, France Travail, DGFiP, supplementary health and death-and-disabil | Y | N | N | Y | NEODeS; pmr=True |
| FILING-IN: FR-DSN-002 - France Travail, via net-entreprises.fr | Y | N | N | Y | TXT / per event, within 5 days; pmr=True |
| FILING-IN: FR-DSN-003 - Caisse Primaire d'Assurance Maladie (CPAM), via net-entreprises.fr | Y | N | N | Y | TXT / per event, within 5 days; pmr=True |
| FILING-IN: FR-URSSAF-001 - URSSAF, via net-entreprises.fr | Y | N | N | Y | XML / per hire; pmr=True |
| FILING-IN: FR-DGFIP-001 - Direction Generale des Finances Publiques (DGFiP) | Y | N | Y | Y | TXT / monthly, with a quarterly option below 11 employees; pmr=True |
| FILING-IN: FR-DGFIP-002 - DGFiP | Y | N | Y | Y | TXT / monthly, quarterly or annual by amount; pmr=True |
| FILING-IN: FR-CARSAT-001 - Caisse d'Assurance Retraite et de la Sante au Travail (CARSAT), via the compte AT/MP on net-entreprises.fr | Y | N | Y | Y | XML / annual, and on any reclassification; pmr=True |
| FILING-IN: FR-URSSAF-002 - URSSAF, via net-entreprises.fr | Y | N | Y | Y | TXT / monthly; pmr=True |
| FILING-IN: FR-URSSAF-003 - URSSAF, on behalf of Agefiph | Y | N | N | Y | TXT / annual; pmr=True |
| FILING-IN: FR-URSSAF-004 - URSSAF | Y | N | N | Y | TXT / annual; pmr=True |
| FILING-IN: FR-DGFIP-003 - DGFiP | Y | N | N | Y | XML / monthly, quarterly or annual by amount; pmr=True |
| FILING-IN: FR-CPAM-002 - CPAM, via net-entreprises.fr | Y | N | N | Y | XML / per event, within 48 hours; pmr=False |
| FILING-IN: FR-CDC-001 - Caisse des Depots, SOLTeA platform | Y | N | N | Y | XLSX / annual; pmr=False |
| FILING-IN: FR-CPAM-003 - Caisse Primaire d'Assurance Maladie (CPAM) | Y | N | Y | Y | TXT / per event; pmr=True |
| FILING-IN: FR-AGIRC-001 - AGIRC-ARRCO institutions, via the DSN return flow | Y | N | Y | Y | TXT / monthly; pmr=True |
| FILING-OUT: FR-HR-001 - Ministry of Labour, Egapro platform | N | N | N | Y | HR-scope - requires data beyond payroll system. The professional equality index (Index de l'egalite professionnelle femmes-hommes), due annually by 1  |
| FILING-OUT: FR-HR-002 - Works council (comite social et economique) | N | N | N | Y | HR-scope - requires data beyond payroll system. The social report (bilan social), due from employers with 300 or more employees, requires recruitment, |
| FILING-OUT: FR-HR-003 - Works council | N | N | N | Y | HR-scope - requires data beyond payroll system. The economic, social and environmental database (BDESE) requires investment, environmental and governa |
| FILING-OUT: FR-HR-004 - DARES, Ministry of Labour statistical service | N | N | N | Y | HR-scope - requires data beyond payroll system. The ACEMO survey of labour activity and employment conditions is a sampled statistical survey requirin |
| FILING-OUT: FR-HR-005 - Ministry of Labour | N | N | N | Y | HR-scope - requires data beyond payroll system. The gender-balance obligation for senior executives and governing bodies, applying to employers above  |
| FILING-OUT: FR-FIN-001 - DGFiP | N | N | N | Y | Not a payroll filing. The taxes on the use of vehicles for economic purposes (which replaced the former taxe sur les vehicules de societe) are assesse |
| FILING-OUT: FR-FIN-002 - DGFiP | N | N | N | Y | Not a payroll filing. The construction investment obligation (participation des employeurs a l'effort de construction) for employers of 50 or more is  |
| FILING-OUT: FR-MSA-001 - Mutualite Sociale Agricole | N | Y | N | N | Outside the regime general. The agricultural scheme has its own collection network, its own DSN channel and its own contribution set. |
| FILING-OUT: FR-CIBTP-001 - Sector paid-leave funds (caisses de conges payes) in construction, public works, entertainment, dockers and transport | N | N | N | Y | Sector-specific flow not built for the baseline France build. In these sectors the FUND pays the employee's holiday pay and the employer pays a contri |
| FILING-OUT: FR-DGFIP-004 - DGFiP | N | N | N | Y | General Tax Code Article 182 B, at 25% on sums paid to a non-resident for se |
| FILING-OUT: FR-DGFIP-005 - DGFiP | N | N | N | Y | General Tax Code Article 197 A (20% up to EUR 29,579 of French net taxable i |
| FILING-OUT: FR-URSSAF-005 - URSSAF | N | N | N | Y | Out of the employment-type scope. Contributions for company officers who are self-employed (majority-shareholding SARL managers and other travailleurs |
| WAGE-IN: Base salary for the contractual working time (salaire de base), smoothed at 151.67 hours for a full-time 35-hour week | Y | N | N | Y | wage_type_categories.in_scope |
| WAGE-IN: Overtime, base and premium (25% for the first eight hours beyond 35 in the week, 50% thereafter, floor of 10% by agreement) | Y | N | N | Y | wage_type_categories.in_scope |
| WAGE-IN: Additional hours for part-time employees (heures complementaires), 10% within the first tenth and 25% beyond | Y | N | N | Y | wage_type_categories.in_scope |
| WAGE-IN: Days worked beyond an annual day-count arrangement, premiumed at at least 10% | Y | N | N | Y | wage_type_categories.in_scope |
| WAGE-IN: Seniority bonus (prime d'anciennete) | Y | N | N | Y | wage_type_categories.in_scope |
| WAGE-IN: Thirteenth month (13eme mois) | Y | N | N | Y | wage_type_categories.in_scope |
| WAGE-IN: Holiday bonus (prime de vacances) | Y | N | N | Y | wage_type_categories.in_scope |
| WAGE-IN: Performance and objectives bonus | Y | N | N | Y | wage_type_categories.in_scope |
| WAGE-IN: Commission, including a contractual guaranteed minimum against commission | Y | N | N | Y | wage_type_categories.in_scope |
| WAGE-IN: On-call, shift, Sunday and night premiums | Y | N | N | Y | wage_type_categories.in_scope |
| WAGE-IN: Paid annual leave pay, computed as the higher of the one-tenth rule and the salary maintenance rule | Y | N | N | Y | wage_type_categories.in_scope |
| WAGE-IN: Public holiday pay, including the 100% premium for work on 1 May | Y | N | N | Y | wage_type_categories.in_scope |
| WAGE-IN: Working-time reduction days (jours de RTT) and their monetisation | Y | N | N | Y | wage_type_categories.in_scope |
| WAGE-IN: Employer top-up on sickness (90% for 30 days, 66.66% for the next 30, after one year's service and a seven-day waiting period) | Y | N | N | Y | wage_type_categories.in_scope |
| WAGE-IN: Daily social security benefits transiting the payslip where the employer is subrogated | Y | N | N | Y | wage_type_categories.in_scope |
| WAGE-IN: Partial activity (activite partielle) allowance | Y | N | N | Y | wage_type_categories.in_scope |
| WAGE-IN: Benefits in kind: company vehicle, accommodation, meals (EUR 5.50 per meal for 2026), communication tools | Y | N | N | Y | wage_type_categories.in_scope |
| WAGE-IN: Meal vouchers, employer share exempt to EUR 7.32 per voucher at 50% to 60% of face value | Y | N | N | Y | wage_type_categories.in_scope |
| WAGE-IN: 50% reimbursement of the public transport season ticket (compulsory) | Y | N | N | Y | wage_type_categories.in_scope |
| WAGE-IN: Sustainable mobility allowance | Y | N | N | Y | wage_type_categories.in_scope |
| WAGE-IN: Professional expense reimbursements, within and above the statutory limits | Y | N | N | Y | wage_type_categories.in_scope |
| WAGE-IN: Value-sharing bonus (prime de partage de la valeur), standard and enhanced regimes | Y | N | N | Y | wage_type_categories.in_scope |
| WAGE-IN: Compensatory notice indemnity (ordinary pay) | Y | N | N | Y | wage_type_categories.in_scope |
| WAGE-IN: Compensatory leave indemnity (ordinary pay) | Y | N | N | Y | wage_type_categories.in_scope |
| WAGE-IN: Fixed-term end-of-contract indemnity, 10% or 6% (ordinary pay) | Y | N | N | Y | wage_type_categories.in_scope |
| WAGE-IN: Non-compete indemnity (ordinary pay) | Y | N | N | Y | wage_type_categories.in_scope |
| WAGE-IN: Statutory and collectively agreed redundancy payments, with the three-layer exemption | Y | N | N | Y | wage_type_categories.in_scope |
| WAGE-IN: Mutually agreed termination and compulsory retirement indemnities, with the 40% employer contribution | Y | N | N | Y | wage_type_categories.in_scope |
| WAGE-IN: Voluntary retirement indemnity (fully contributable and taxable outside a collective redundancy plan) | Y | N | N | Y | wage_type_categories.in_scope |
| WAGE-IN: Impatriation premium under General Tax Code Article 155 B, real amount or 30% flat | Y | N | N | Y | General Tax Code Article 155 B, real amount or 30% flat |
| WAGE-IN: Expatriation supplements exempt within 40% under General Tax Code Article 81 A | Y | N | N | Y | General Tax Code Article 81 A |
| WAGE-IN: Employee and employer contributions to the compulsory health cover, death-and-disability cover and supplementary pension schemes | Y | N | N | Y | wage_type_categories.in_scope |
| WAGE-IN: Advance on the current month (acompte) as a netting line, NOT a separate pay run | Y | N | N | Y | wage_type_categories.in_scope |
| WAGE-IN: Advance in the strict sense (avance), recoverable at one tenth of pay per period | Y | N | N | Y | wage_type_categories.in_scope |
| WAGE-IN: Wage attachments, maintenance orders paid by direct payment, and tax levy notices | Y | N | N | Y | wage_type_categories.in_scope |
| WAGE-OUT: Attendance fees (jetons de presence) paid to non-executive directors - taxed as investment income at 12.8% plus capital social levies of 18. | N | N | N | Y | Attendance fees (jetons de presence) paid to non-executive directors - taxed as investment income at 12.8% plus capital social levies of 18.6%, with a |
| WAGE-OUT: Free share acquisition gains and share option exercise gains - taxable in the year of DISPOSAL, outside withholding at source and outside th | N | N | N | Y | Free share acquisition gains and share option exercise gains - taxable in the year of DISPOSAL, outside withholding at source and outside the ordinary |
| WAGE-OUT: Profit-sharing and incentive-scheme amounts (participation, interessement) once invested - outside gross pay, with their own regime and thei | N | N | N | Y | Profit-sharing and incentive-scheme amounts (participation, interessement) once invested - outside gross pay, with their own regime and their own sche |
| WAGE-OUT: Employee payments into a company savings plan or collective retirement savings plan - a saving, not a contribution | N | N | N | Y | Employee payments into a company savings plan or collective retirement savings plan - a saving, not a contribution |
| WAGE-OUT: Self-employed contractor invoices - not remuneration, no employer withholding | N | N | N | Y | Self-employed contractor invoices - not remuneration, no employer withholding |
| WAGE-OUT: Holiday pay in the construction, public works and entertainment sectors - paid by the sector fund, not by the employer | N | N | N | Y | Holiday pay in the construction, public works and entertainment sectors - paid by the sector fund, not by the employer |
| WAGE-OUT: Student loan repayments - NO SUCH DEDUCTION EXISTS IN FRANCE. Recorded explicitly so that a requirement referring to one is raised as an err | N | N | N | Y | Student loan repayments - NO SUCH DEDUCTION EXISTS IN FRANCE. Recorded explicitly so that a requirement referring to one is raised as an error rather  |
| MAPPER-IN [personal_id_type]: NIR - numero d'inscription au repertoire, 15 characters (13 digits + 2-digit key); key = 97 minus (the 13-digit number m | Y | N | N | Y | option_mapper_scope.personal_id_type |
| MAPPER-IN [personal_id_type]: NTT - numero technique temporaire, up to 40 characters, conventionally the SIRET plus an internal sequence; used only un | Y | N | N | Y | option_mapper_scope.personal_id_type |
| MAPPER-IN [insurance_type]: Regime general - URSSAF, CNAM, CNAV | Y | N | N | Y | option_mapper_scope.insurance_type |
| MAPPER-IN [insurance_type]: Regime general plus the Alsace-Moselle local health scheme (additional 1.30% employee contribution, triggered by the place | Y | N | N | Y | option_mapper_scope.insurance_type |
| MAPPER-IN [insurance_type]: AGIRC-ARRCO supplementary pension (bands 1 and 2) | Y | N | N | Y | option_mapper_scope.insurance_type |
| MAPPER-IN [insurance_type]: Compulsory supplementary health cover (complementaire sante), employer share at least 50% | Y | N | N | Y | option_mapper_scope.insurance_type |
| MAPPER-IN [insurance_type]: Managerial-grade death-and-disability cover, 1.50% of the capped band, wholly employer-paid | Y | N | N | Y | option_mapper_scope.insurance_type |
| MAPPER-IN [insurance_type]: Optional death-and-disability and supplementary pension schemes, collective and compulsory | Y | N | N | Y | option_mapper_scope.insurance_type |
| MAPPER-IN [contract_type]: CDI - permanent contract | Y | N | N | Y | option_mapper_scope.contract_type |
| MAPPER-IN [contract_type]: CDD - fixed-term contract | Y | N | N | Y | option_mapper_scope.contract_type |
| MAPPER-IN [contract_type]: Apprenticeship contract | Y | N | N | Y | option_mapper_scope.contract_type |
| MAPPER-IN [contract_type]: Professionalisation contract | Y | N | N | Y | option_mapper_scope.contract_type |
| MAPPER-IN [contract_type]: Temporary-agency assignment | Y | N | N | Y | option_mapper_scope.contract_type |
| MAPPER-IN [contract_type]: Internship agreement (convention de stage) - gratuity, not a wage | Y | N | N | Y | option_mapper_scope.contract_type |
| MAPPER-IN [working_time_type]: Full-time 35-hour week, 151.67 hours a month | Y | N | N | Y | option_mapper_scope.working_time_type |
| MAPPER-IN [working_time_type]: Part-time, with the social security ceiling prorated on the hours ratio | Y | N | N | Y | option_mapper_scope.working_time_type |
| MAPPER-IN [working_time_type]: Annual day-count arrangement (forfait annuel en jours), typically 218 days - no overtime | Y | N | N | Y | option_mapper_scope.working_time_type |
| MAPPER-IN [withholding_rate_type]: Taux personnalise - personal rate transmitted by the tax administration | Y | N | Y | Y | option_mapper_scope.withholding_rate_type |
| MAPPER-IN [withholding_rate_type]: Taux individualise - individualised rate within a couple | Y | N | Y | Y | option_mapper_scope.withholding_rate_type |
| MAPPER-IN [withholding_rate_type]: Taux non personnalise - the statutory default grid, by territory (metropolitan; Guadeloupe, Martinique and La Reuni | Y | N | Y | Y | option_mapper_scope.withholding_rate_type |
| MAPPER-IN [withholding_rate_type]: Retenue a la source non-resident - General Tax Code Article 182 A, 0/12/20 bands, or 0/8/14.4 for overseas-source i | Y | N | Y | Y | General Tax Code Article 182 A, 0/12/20 bands, or 0/8/14 |
| MAPPER-IN [correction_codes]: Cancel-and-replace declaration for a month whose deadline has not passed | Y | N | N | Y | option_mapper_scope.correction_codes |
| MAPPER-IN [correction_codes]: Contribution regularisation carried in the contribution-base block with the start and end dates of the period of attachm | Y | N | N | Y | option_mapper_scope.correction_codes |
| MAPPER-IN [correction_codes]: Withholding regularisation carried in the dedicated block, dated to the month of the original error | Y | N | N | Y | option_mapper_scope.correction_codes |
| MAPPER-IN [correction_codes]: Amending or cancelling event signal | Y | N | N | Y | option_mapper_scope.correction_codes |
| MAPPER-IN [benefit_type]: Company vehicle | Y | N | N | Y | option_mapper_scope.benefit_type |
| MAPPER-IN [benefit_type]: Accommodation | Y | N | N | Y | option_mapper_scope.benefit_type |
| MAPPER-IN [benefit_type]: Meals | Y | N | N | Y | option_mapper_scope.benefit_type |
| MAPPER-IN [benefit_type]: Communication tools | Y | N | N | Y | option_mapper_scope.benefit_type |
| MAPPER-IN [benefit_type]: Meal vouchers | Y | N | N | Y | option_mapper_scope.benefit_type |
| MAPPER-IN [benefit_type]: Public transport season ticket reimbursement | Y | N | N | Y | option_mapper_scope.benefit_type |
| MAPPER-IN [benefit_type]: Sustainable mobility allowance | Y | N | N | Y | option_mapper_scope.benefit_type |
| MAPPER-IN [benefit_type]: Compulsory health cover | Y | N | N | Y | option_mapper_scope.benefit_type |
| MAPPER-IN [benefit_type]: Death-and-disability cover | Y | N | N | Y | option_mapper_scope.benefit_type |
| MAPPER-IN [benefit_type]: Supplementary pension scheme | Y | N | N | Y | option_mapper_scope.benefit_type |
| MAPPER-IN [benefit_type]: Company savings plan and collective retirement savings plan employer contributions | Y | N | N | Y | option_mapper_scope.benefit_type |
| MAPPER-IN [residence_status]: Tax resident (domicilie fiscalement en France) under General Tax Code Article 4 B, as modified by any applicable treaty | Y | N | Y | Y | General Tax Code Article 4 B, as modified by any applicable treaty |
| MAPPER-IN [residence_status]: Non-resident | Y | N | Y | Y | option_mapper_scope.residence_status |
| MAPPER-IN [residence_status]: Affiliated to the French social security scheme | Y | N | Y | Y | option_mapper_scope.residence_status |
| MAPPER-IN [residence_status]: Posted worker holding a portable document A1 for another state - no French contributions | Y | N | Y | Y | option_mapper_scope.residence_status |
| MAPPER-IN [leave_type]: Paid annual leave (conges payes), in working days (jours ouvrables, 30 a year) or worked days (jours ouvres, 25 a year) - the  | Y | N | N | Y | option_mapper_scope.leave_type |
| MAPPER-IN [leave_type]: Working-time reduction days (jours de RTT) | Y | N | N | Y | option_mapper_scope.leave_type |
| MAPPER-IN [leave_type]: Seniority leave (conges d'anciennete) | Y | N | N | Y | option_mapper_scope.leave_type |
| MAPPER-IN [leave_type]: Maternity, paternity and child-welcome, adoption, birth leave | Y | N | N | Y | option_mapper_scope.leave_type |
| MAPPER-IN [leave_type]: Supplementary birth leave (new from 1 July 2026, up to 2 months per parent at 70% then 60% of net pay) | Y | N | N | Y | option_mapper_scope.leave_type |
| MAPPER-IN [leave_type]: Sick leave, non-occupational | Y | N | N | Y | option_mapper_scope.leave_type |
| MAPPER-IN [leave_type]: Work accident and occupational disease leave | Y | N | N | Y | option_mapper_scope.leave_type |
| MAPPER-IN [leave_type]: Family event leave, and bereavement leave for a child | Y | N | N | Y | option_mapper_scope.leave_type |
| MAPPER-IN [leave_type]: Parental education leave, carer's leave, parental presence leave | Y | N | N | Y | option_mapper_scope.leave_type |
| MAPPER-IN [leave_type]: Unpaid leave by agreement (conge sans solde) - no statutory framework, agreed in writing case by case | Y | N | N | Y | option_mapper_scope.leave_type |
| MAPPER-IN [leave_type]: Time savings account (compte epargne-temps) | Y | N | N | Y | option_mapper_scope.leave_type |
| INTEG-OUTBOUND: FR-BANK-001 - The employee's bank | Y | N | N | Y | XML / monthly; pmr=n/a |
| INTEG-OUTBOUND: FR-PAYSLIP-001 - The employee, and the electronic archiving service | Y | N | N | Y | PDF / monthly; pmr=n/a |
| INTEG-OUTBOUND: FR-GL-001 - The client's general ledger | Y | N | N | Y | CSV / monthly; pmr=n/a |
| INTEG-INBOUND: FR-CLIENT-001 - The client's HRMS | Y | N | Y | Y | CSV / monthly; pmr=True |
| INTEG-INBOUND: FR-CLIENT-002 - The outgoing payroll provider, on migration | Y | N | Y | Y | XLSX / one-off; pmr=True |
| INTEG-INBOUND: FR-COURT-001 - Court enforcement officers (commissaires de justice) and DGFiP | Y | N | Y | Y | PDF / per event; pmr=True |

# Part 4 - scope_manifest.json (full)

| Key | Value |
|---|---|
| `_comment` | Produced by Agent 1 (CCG). Every downstream agent reads this and rejects out-of-scope items. |
| `country` | France |
| `country_code` | FR |
| `code` | FR |
| `currency` | EUR |
| `year` | 2026 |
| `generated` | 2026-08-26T16:40:00+02:00 |
| `scope_version` | 1.1 |
| `scope_decided_by` | Wallisson Gomes |
| `scope_decided_on` | 2026-08-26 |
| `source_artifact` | FR-CCG-001-v1.0.docx |
| `mandate_document` | FR-compliance/00-official-sources/ccg-sources/FR-CCG-source-register.md |


### employment_types

| Key | Value |
|---|---|
| `rationale` | Scope is the French general social security scheme (regime general) for private-sector employment, locked before Stage 1 by Wallisson Gomes on 26 August 2026: URSSAF for social contributions, CNAM for health, CNAV for the basic pension, AGIRC-ARRCO for the supplementary pension, France Travail / UNEDIC for unemployment and CNAF for family benefits. The regimes speciaux listed above are acknowledged as existing and are deliberately not researched. Two territorial layers are IN scope because they modify the regime general rather than replace it - Alsace-Moselle (the 1.30% local employee health contribution, triggered by the place of work not by residence, plus two extra public holidays) and the overseas departments for withholding purposes. What is out of scope in the overseas departments is only the LODEOM exemption arithmetic. Company officers treated as employees are in scope with one deliberate exception carried through every artifact: they are excluded from unemployment insurance and the wage guarantee scheme for want of an employment contract. |


#### in_scope (12 items)

- Permanent contract (contrat a duree indeterminee, CDI)
- Fixed-term contract (contrat a duree determinee, CDD), including the 10% end-of-contract indemnity
- Part-time employees, including the prorated social security ceiling and additional hours (heures complementaires)
- Managerial grade (cadre) and non-managerial employees
- Employees on an annual day-count arrangement (forfait annuel en jours)
- Apprenticeship contracts (contrat d'apprentissage)
- Professionalisation contracts (contrat de professionnalisation)
- Interns (stagiaires) receiving a statutory gratuity, exempt to 15% of the hourly ceiling per hour of attendance
- Temporary-agency workers (interimaires), where the client is the agency and therefore the employer
- Company officers treated as employees (assimiles salaries): chair or managing director of a SAS or SA, minority or equal-shareholding manager of a SARL - full contributions except unemployment insurance and the wage guarantee scheme
- Employees whose place of work is in Alsace-Moselle (Bas-Rhin, Haut-Rhin, Moselle): the general scheme plus the 1.30% local employee health contribution and two extra public holidays
- Non-resident employees working in France and affiliated to the French scheme, withheld under General Tax Code Article 182 A


#### out_of_scope (13 items)


##### out_of_scope #1

| Key | Value |
|---|---|
| `employment_type` | RATP scheme (Paris transport) |
| `descoping_reason` | Regime special outside the regime general. Descoped before Stage 1 by the scope owner, 26 August 2026. Rates and mechanics deliberately not researched. |
| `client_impact` | A client with RATP-scheme staff requires a separate scoping exercise before any build. |


##### out_of_scope #2

| Key | Value |
|---|---|
| `employment_type` | ENIM scheme (maritime and seafarers) |
| `descoping_reason` | Regime special outside the regime general. Descoped before Stage 1 by the scope owner, 26 August 2026. |
| `client_impact` | Separate scoping required. |


##### out_of_scope #3

| Key | Value |
|---|---|
| `employment_type` | CNBF scheme (lawyers) |
| `descoping_reason` | Regime special outside the regime general. Descoped before Stage 1 by the scope owner, 26 August 2026. |
| `client_impact` | Separate scoping required. |


##### out_of_scope #4

| Key | Value |
|---|---|
| `employment_type` | CRPCEN scheme (notarial staff) |
| `descoping_reason` | Regime special outside the regime general. Descoped before Stage 1 by the scope owner, 26 August 2026. |
| `client_impact` | Separate scoping required. |


##### out_of_scope #5

| Key | Value |
|---|---|
| `employment_type` | CAVIMAC scheme (clergy) |
| `descoping_reason` | Regime special outside the regime general. Descoped before Stage 1 by the scope owner, 26 August 2026. |
| `client_impact` | Separate scoping required. |


##### out_of_scope #6

| Key | Value |
|---|---|
| `employment_type` | CNIEG and CAMIEG schemes (gas and electricity sector) |
| `descoping_reason` | Regime special outside the regime general. Descoped before Stage 1 by the scope owner, 26 August 2026. |
| `client_impact` | Separate scoping required. |


##### out_of_scope #7

| Key | Value |
|---|---|
| `employment_type` | Any other sector-specific caisse outside the regime general |
| `descoping_reason` | Catch-all for the regimes speciaux. Acknowledged as existing in the CCG; rates and mechanics deliberately not researched, per the locked scope decision of 26 August 2026. |
| `client_impact` | Any client population outside the regime general must be raised before build. |


##### out_of_scope #8

| Key | Value |
|---|---|
| `employment_type` | Agricultural employees under the MSA scheme (regime agricole) |
| `descoping_reason` | A separate collection network (Mutualite Sociale Agricole) with its own DSN channel, its own contribution set and its own paid-leave arrangements. Outside the URSSAF regime general to which this build is scoped. |
| `client_impact` | An agricultural client needs an MSA variant of the DSN and of the contribution model. |


##### out_of_scope #9

| Key | Value |
|---|---|
| `employment_type` | Majority-shareholding managers of a SARL, and other self-employed workers (travailleurs non salaries) |
| `descoping_reason` | Self-employed under the SSI scheme. Contributions are assessed and paid personally, outside payroll entirely. Not an employment type the engine can process. |
| `client_impact` | Refer to the client's accountant; these individuals must not be loaded as employees. |


##### out_of_scope #10

| Key | Value |
|---|---|
| `employment_type` | Public-sector statutory staff (fonctionnaires) and their pension schemes |
| `descoping_reason` | Outside the private-sector regime general to which this build is scoped. |
| `client_impact` | Not applicable to private-sector clients. |


##### out_of_scope #11

| Key | Value |
|---|---|
| `employment_type` | Workers posted into France who remain affiliated to a foreign scheme under a portable document A1 |
| `descoping_reason` | No French social security contributions are due and the foreign employer pays the worker. There is no French payslip to produce. The posting declaration (SIPSI) is an administrative obligation of the receiving entity, not a payroll output. |
| `client_impact` | The receiving entity must file the SIPSI posting declaration and apply the French core labour standards; refer to the client's mobility function. |


##### out_of_scope #12

| Key | Value |
|---|---|
| `employment_type` | Mayotte |
| `descoping_reason` | A distinct social security scheme with its own contribution set and its own minimum wage (EUR 9.56 an hour from 1 June 2026 against EUR 12.31 nationally). Documented in the CCG for awareness; not modelled. |
| `client_impact` | A Mayotte population requires a separate parameter set. |


##### out_of_scope #13

| Key | Value |
|---|---|
| `employment_type` | Overseas departments - the LODEOM specific exemption schemes (Guadeloupe, Martinique, Guyane, La Reunion) |
| `descoping_reason` | The general degressive reduction is replaced by the overseas exemption schemes, which are more generous and structured differently. Their existence, the reduced non-resident withholding rates (8% and 14.4%) and the territorial withholding grids ARE documented in the CCG; the exemption-scheme arithmetic is not modelled. |
| `client_impact` | An overseas-department population needs the LODEOM exemption schemes built before go-live; the ordinary contribution set and the withholding grids are already covered. |


### authority_filings


#### in_scope (15 items)


##### in_scope #1

| Key | Value |
|---|---|
| `filing_id` | FR-DSN-001 |
| `authority` | URSSAF (and, through the same file, CNAV, CPAM, AGIRC-ARRCO, France Travail, DGFiP, supplementary health and death-and-disability insurers) |
| `frequency` | monthly |
| `format` | TXT |
| `integration_type` | outbound |
| `product_mapping_required` | true |
| `rationale` | The Declaration Sociale Nominative is the single monthly payroll declaration and the primary artifact of the whole France build. It is generated directly from the payroll result in the NEODeS structured-file format, technical specification CT2026.1.2, and deposited on net-entreprises.fr. Deadline the 5th of the following month for employers of 50 or more paying wages in the same month, the 15th otherwise. It carries the contribution bases, the individual and aggregate contributions, the net social amount, the net taxable amount, the withholding rate and the income tax withheld. Full product mapping is required for every block. |
| `spec_file` | 04-reports-spec/FR-DSN-001-DSNMensuelle-Spec.xlsx |
| `spec_link_basis` | Verified at the pre-submission audit gate, 27 Aug 2026: the named workbook's own 'Version Control' sheet carries Document ID = FR-DSN-001. The 15 filings and the 15 specs form an exact 1:1 bijection on that field - no filing is unspecced and no spec is orphaned. |
| `sir_authority` | NETENT-DSN |
| `sir_runbook` | 03-statutory-integrations/NETENT-DSN/ |


##### in_scope #2

| Key | Value |
|---|---|
| `filing_id` | FR-DSN-002 |
| `authority` | France Travail, via net-entreprises.fr |
| `frequency` | per event, within 5 days |
| `format` | TXT |
| `integration_type` | outbound |
| `product_mapping_required` | true |
| `rationale` | DSN event signal for the end of a contract (signalement fin de contrat de travail). Replaces the paper end-of-contract certificate transmitted to France Travail and opens the employee's unemployment entitlement. Transmission through the DSN does NOT dispense the employer from giving the employee a signed copy: the two acts are complementary. |
| `spec_file` | 04-reports-spec/FR-DSN-002-FinContratUnique-Spec.xlsx |
| `spec_link_basis` | Verified at the pre-submission audit gate, 27 Aug 2026: the named workbook's own 'Version Control' sheet carries Document ID = FR-DSN-002. The 15 filings and the 15 specs form an exact 1:1 bijection on that field - no filing is unspecced and no spec is orphaned. |
| `sir_authority` | NETENT-DSN |
| `sir_runbook` | 03-statutory-integrations/NETENT-DSN/ |


##### in_scope #3

| Key | Value |
|---|---|
| `filing_id` | FR-DSN-003 |
| `authority` | Caisse Primaire d'Assurance Maladie (CPAM), via net-entreprises.fr |
| `frequency` | per event, within 5 days |
| `format` | TXT |
| `integration_type` | outbound |
| `product_mapping_required` | true |
| `rationale` | DSN event signals for a work stoppage (arret de travail) and for the resumption of work. Triggers and closes the sickness, maternity, paternity, adoption and work-accident daily benefits. Drives the subrogation logic on the payslip. |
| `spec_file` | 04-reports-spec/FR-DSN-003-ArretTravailReprise-Spec.xlsx |
| `spec_link_basis` | Verified at the pre-submission audit gate, 27 Aug 2026: the named workbook's own 'Version Control' sheet carries Document ID = FR-DSN-003. The 15 filings and the 15 specs form an exact 1:1 bijection on that field - no filing is unspecced and no spec is orphaned. |
| `sir_authority` | NETENT-DSN |
| `sir_runbook` | 03-statutory-integrations/NETENT-DSN/ |


##### in_scope #4

| Key | Value |
|---|---|
| `filing_id` | FR-URSSAF-001 |
| `authority` | URSSAF, via net-entreprises.fr |
| `frequency` | per hire |
| `format` | XML |
| `integration_type` | outbound |
| `product_mapping_required` | true |
| `rationale` | Declaration Prealable A l'Embauche. Due within the 8 days preceding the start and in any event before the employee begins work. This remains a SEPARATE filing in 2026: the technical specification provides for it to move into the DSN as event signal type 10, but production was deferred and is not expected before 1 January 2027. A build must not assume it is inside the DSN. |
| `spec_file` | 04-reports-spec/FR-URSSAF-001-DPAE-Spec.xlsx |
| `spec_link_basis` | Verified at the pre-submission audit gate, 27 Aug 2026: the named workbook's own 'Version Control' sheet carries Document ID = FR-URSSAF-001. The 15 filings and the 15 specs form an exact 1:1 bijection on that field - no filing is unspecced and no spec is orphaned. |
| `sir_authority` | URSSAF-DPAE |
| `sir_runbook` | 03-statutory-integrations/URSSAF-DPAE/ |


##### in_scope #5

| Key | Value |
|---|---|
| `filing_id` | FR-DGFIP-001 |
| `authority` | Direction Generale des Finances Publiques (DGFiP) |
| `frequency` | monthly, with a quarterly option below 11 employees |
| `format` | TXT |
| `integration_type` | both |
| `product_mapping_required` | true |
| `rationale` | Withholding at source (prelevement a la source). Declared INSIDE the monthly DSN and collected by direct debit initiated from it - there is no separate income tax return for payroll. Remittance due the 8th of the following month for employers of 50 or more, the 18th otherwise. Classified as 'both' because the outbound leg (net taxable amount, rate applied, amount withheld) and the inbound leg (the rate the administration transmits) are two halves of one obligation. The remitted amount is rounded to the whole euro; the per-employee figures are carried at two decimals. |
| `spec_file` | 04-reports-spec/FR-DGFIP-001-PrelevementSource-Spec.xlsx |
| `spec_link_basis` | Verified at the pre-submission audit gate, 27 Aug 2026: the named workbook's own 'Version Control' sheet carries Document ID = FR-DGFIP-001. The 15 filings and the 15 specs form an exact 1:1 bijection on that field - no filing is unspecced and no spec is orphaned. |
| `sir_authority` | NETENT-DSN |
| `sir_runbook` | 03-statutory-integrations/NETENT-DSN/ |


##### in_scope #6

| Key | Value |
|---|---|
| `filing_id` | FR-DGFIP-002 |
| `authority` | DGFiP |
| `frequency` | monthly, quarterly or annual by amount |
| `format` | TXT |
| `integration_type` | inbound |
| `product_mapping_required` | true |
| `rationale` | The withholding rate return (compte rendu metier) delivered by DGFiP against each monthly DSN and collected from net-entreprises.fr. This is the ONLY lawful source of an employee's withholding rate - the employer never collects a tax number and never computes a rate. The engine must parse the rate, its type (personal, individualised, default) and its validity period, apply it from the following payslip, and date-check it on every run. Where no rate is held or the rate has expired, the statutory default grid applies. Never default this inbound flow to not-in-scope. |
| `spec_file` | 04-reports-spec/FR-DGFIP-002-CompteRenduPAS-Spec.xlsx |
| `spec_link_basis` | Verified at the pre-submission audit gate, 27 Aug 2026: the named workbook's own 'Version Control' sheet carries Document ID = FR-DGFIP-002. The 15 filings and the 15 specs form an exact 1:1 bijection on that field - no filing is unspecced and no spec is orphaned. |
| `sir_authority` | NETENT-DSN |
| `sir_runbook` | 03-statutory-integrations/NETENT-DSN/ |


##### in_scope #7

| Key | Value |
|---|---|
| `filing_id` | FR-CARSAT-001 |
| `authority` | Caisse d'Assurance Retraite et de la Sante au Travail (CARSAT), via the compte AT/MP on net-entreprises.fr |
| `frequency` | annual, and on any reclassification |
| `format` | XML |
| `integration_type` | inbound |
| `product_mapping_required` | true |
| `rationale` | Dematerialised notification of the establishment-specific industrial-accident and occupational-disease net rate and risk code. Subscribing to the AT/MP account has been compulsory from the first employee since 1 January 2022; failure attracts a penalty of 0.5% to 1.5% of the monthly ceiling per employee (1% for 20 to 149 employees, the maximum rate above). The rate is establishment-level, must be stored per SIRET, and only a fixed 0.49 points of it is imputable against the general reduction. |
| `spec_file` | 04-reports-spec/FR-CARSAT-001-NotificationTauxATMP-Spec.xlsx |
| `spec_link_basis` | Verified at the pre-submission audit gate, 27 Aug 2026: the named workbook's own 'Version Control' sheet carries Document ID = FR-CARSAT-001. The 15 filings and the 15 specs form an exact 1:1 bijection on that field - no filing is unspecced and no spec is orphaned. |
| `sir_authority` | NETENT-DSN |
| `sir_runbook` | 03-statutory-integrations/NETENT-DSN/ |


##### in_scope #8

| Key | Value |
|---|---|
| `filing_id` | FR-URSSAF-002 |
| `authority` | URSSAF, via net-entreprises.fr |
| `frequency` | monthly |
| `format` | TXT |
| `integration_type` | inbound |
| `product_mapping_required` | true |
| `rationale` | The URSSAF and old-age fund return: certification or rejection of each employee's social security number (NIR) with correction of civil-status data, plus blocking and non-blocking anomalies, plus the annual reminder issued in March. From June 2026 an anomaly left uncorrected on the CAPPED GROSS BASE may be corrected by the authority itself under the substituted-declaration power, with the corrected figure sent to the pension bodies. Uncorrected anomalies therefore now cause the employer's records and the authority's to diverge, so this flow must be parsed and acted on, not merely archived. |
| `spec_file` | 04-reports-spec/FR-URSSAF-002-CompteRenduMetier-Spec.xlsx |
| `spec_link_basis` | Verified at the pre-submission audit gate, 27 Aug 2026: the named workbook's own 'Version Control' sheet carries Document ID = FR-URSSAF-002. The 15 filings and the 15 specs form an exact 1:1 bijection on that field - no filing is unspecced and no spec is orphaned. |
| `sir_authority` | NETENT-DSN |
| `sir_runbook` | 03-statutory-integrations/NETENT-DSN/ |


##### in_scope #9

| Key | Value |
|---|---|
| `filing_id` | FR-URSSAF-003 |
| `authority` | URSSAF, on behalf of Agefiph |
| `frequency` | annual |
| `format` | TXT |
| `integration_type` | outbound |
| `product_mapping_required` | true |
| `rationale` | Declaration Obligatoire d'Emploi des Travailleurs Handicapes. Employers with at least 20 employees must employ disabled workers to 6% of the average annual workforce or pay a contribution. Since the 2018 reform there is NO separate annual return: the data is consolidated from the twelve monthly DSN flows and declared inside the APRIL DSN, due 5 or 15 May. Payroll scope, not HR scope, because it is filed through the DSN and produces a contribution. The transitional capping of contribution increases no longer applies for the 2026 campaign. |
| `spec_file` | 04-reports-spec/FR-URSSAF-003-DOETH-Spec.xlsx |
| `spec_link_basis` | Verified at the pre-submission audit gate, 27 Aug 2026: the named workbook's own 'Version Control' sheet carries Document ID = FR-URSSAF-003. The 15 filings and the 15 specs form an exact 1:1 bijection on that field - no filing is unspecced and no spec is orphaned. |
| `sir_authority` | NETENT-DSN |
| `sir_runbook` | 03-statutory-integrations/NETENT-DSN/ |


##### in_scope #10

| Key | Value |
|---|---|
| `filing_id` | FR-URSSAF-004 |
| `authority` | URSSAF |
| `frequency` | annual |
| `format` | TXT |
| `integration_type` | outbound |
| `product_mapping_required` | true |
| `rationale` | Balance of the apprenticeship tax (solde de la taxe d'apprentissage), 0.09% of the payroll of the preceding year. Declared and collected inside the APRIL DSN, due 5 or 15 May. Distinct from the 0.68% apprenticeship tax itself, which is collected monthly. |
| `spec_file` | 04-reports-spec/FR-URSSAF-004-SoldeTaxeApprentissage-Spec.xlsx |
| `spec_link_basis` | Verified at the pre-submission audit gate, 27 Aug 2026: the named workbook's own 'Version Control' sheet carries Document ID = FR-URSSAF-004. The 15 filings and the 15 specs form an exact 1:1 bijection on that field - no filing is unspecced and no spec is orphaned. |
| `sir_authority` | NETENT-DSN |
| `sir_runbook` | 03-statutory-integrations/NETENT-DSN/ |


##### in_scope #11

| Key | Value |
|---|---|
| `filing_id` | FR-DGFIP-003 |
| `authority` | DGFiP |
| `frequency` | monthly, quarterly or annual by amount |
| `format` | XML |
| `integration_type` | outbound |
| `product_mapping_required` | true |
| `rationale` | Payroll tax (taxe sur les salaires), forms 2501-SD and 2502-SD, filed by EDI or online at impots.gouv.fr. CONDITIONAL: due only from employers not liable to value added tax on at least 90% of turnover - banks, insurers, associations, health bodies, holding companies. Bands 4.25% / 8.50% / 13.60%. Filing rhythm follows the amount: below EUR 4,000 an annual 2502-SD by 15 January; EUR 4,000 to 10,000 three quarterly 2501-SD then a 2502-SD by 31 January; above EUR 10,000 eleven monthly 2501-SD then a 2502-SD by 31 January. For a client outside the liable population the filing must be SUPPRESSED, not filed nil. |
| `spec_file` | 04-reports-spec/FR-DGFIP-003-TaxeSurLesSalaires-Spec.xlsx |
| `spec_link_basis` | Verified at the pre-submission audit gate, 27 Aug 2026: the named workbook's own 'Version Control' sheet carries Document ID = FR-DGFIP-003. The 15 filings and the 15 specs form an exact 1:1 bijection on that field - no filing is unspecced and no spec is orphaned. |
| `sir_authority` | DGFIP-EDI |
| `sir_runbook` | 03-statutory-integrations/DGFIP-EDI/ |


##### in_scope #12

| Key | Value |
|---|---|
| `filing_id` | FR-CPAM-002 |
| `authority` | CPAM, via net-entreprises.fr |
| `frequency` | per event, within 48 hours |
| `format` | XML |
| `integration_type` | outbound |
| `product_mapping_required` | false |
| `rationale` | Work accident declaration (declaration d'accident du travail). An online form completed from incident data held outside payroll; payroll supplies only the employee identity and pay reference. No wage-type or option-mapper dependency, so no product mapping is required - but it is in scope because it is filed on the payroll portal and it feeds the establishment's claims history and therefore its future AT/MP rate. |
| `spec_file` | 04-reports-spec/FR-CPAM-002-AccidentTravail-Spec.xlsx |
| `spec_link_basis` | Verified at the pre-submission audit gate, 27 Aug 2026: the named workbook's own 'Version Control' sheet carries Document ID = FR-CPAM-002. The 15 filings and the 15 specs form an exact 1:1 bijection on that field - no filing is unspecced and no spec is orphaned. |
| `sir_authority` | CNAM-DIRECT |
| `sir_runbook` | none - portal/manual authority, no runbook produced (per FR-SIR-INDEX-001) |


##### in_scope #13

| Key | Value |
|---|---|
| `filing_id` | FR-CDC-001 |
| `authority` | Caisse des Depots, SOLTeA platform |
| `frequency` | annual |
| `format` | XLSX |
| `integration_type` | outbound |
| `product_mapping_required` | false |
| `rationale` | Allocation of the apprenticeship tax balance to chosen training establishments. The PAYMENT is compulsory and is handled by FR-URSSAF-004; the ALLOCATION is optional and is a client business decision made on a web platform, with a default distribution rule where no allocation is made. The 2026 window ran from 26 May to 21 October. No payroll data mapping is required beyond the amount already declared. |
| `spec_file` | 04-reports-spec/FR-CDC-001-SOLTeA-Spec.xlsx |
| `spec_link_basis` | Verified at the pre-submission audit gate, 27 Aug 2026: the named workbook's own 'Version Control' sheet carries Document ID = FR-CDC-001. The 15 filings and the 15 specs form an exact 1:1 bijection on that field - no filing is unspecced and no spec is orphaned. |
| `sir_authority` | CDC-SOLTEA |
| `sir_runbook` | none - portal/manual authority, no runbook produced (per FR-SIR-INDEX-001) |


##### in_scope #14

| Key | Value |
|---|---|
| `filing_id` | FR-CPAM-003 |
| `authority` | Caisse Primaire d'Assurance Maladie (CPAM) |
| `frequency` | per event |
| `format` | TXT |
| `integration_type` | inbound |
| `product_mapping_required` | true |
| `rationale` | Daily social security benefit statements (indemnites journalieres) delivered where the employer is subrogated to the employee's benefit. Needed to reconcile the offsetting payslip line against the employer's cash position. |
| `spec_file` | 04-reports-spec/FR-CPAM-003-BPIJ-Spec.xlsx |
| `spec_link_basis` | Verified at the pre-submission audit gate, 27 Aug 2026: the named workbook's own 'Version Control' sheet carries Document ID = FR-CPAM-003. The 15 filings and the 15 specs form an exact 1:1 bijection on that field - no filing is unspecced and no spec is orphaned. |
| `sir_authority` | CNAM-DIRECT |
| `sir_runbook` | none - portal/manual authority, no runbook produced (per FR-SIR-INDEX-001) |


##### in_scope #15

| Key | Value |
|---|---|
| `filing_id` | FR-AGIRC-001 |
| `authority` | AGIRC-ARRCO institutions, via the DSN return flow |
| `frequency` | monthly |
| `format` | TXT |
| `integration_type` | inbound |
| `product_mapping_required` | true |
| `rationale` | Membership and point-allocation feedback for the compulsory supplementary pension scheme. The institution is identified by its membership reference; a wrong reference silently misroutes the contribution. |
| `spec_file` | 04-reports-spec/FR-AGIRC-001-RetourAgircArrco-Spec.xlsx |
| `spec_link_basis` | Verified at the pre-submission audit gate, 27 Aug 2026: the named workbook's own 'Version Control' sheet carries Document ID = FR-AGIRC-001. The 15 filings and the 15 specs form an exact 1:1 bijection on that field - no filing is unspecced and no spec is orphaned. |
| `sir_authority` | NETENT-DSN |
| `sir_runbook` | 03-statutory-integrations/NETENT-DSN/ |


#### out_of_scope (13 items)


##### out_of_scope #1

| Key | Value |
|---|---|
| `filing_id` | FR-HR-001 |
| `authority` | Ministry of Labour, Egapro platform |
| `descoping_reason` | HR-scope - requires data beyond payroll system. The professional equality index (Index de l'egalite professionnelle femmes-hommes), due annually by 1 March from employers with 50 or more employees, scores pay gaps by age band and occupational category but ALSO requires promotion rates, pay-rise rates and the sex of the ten highest earners. Promotion and pay-review data are held in the human-resources system, not in payroll. |
| `client_impact` | Refer to HRMS team. Payroll can supply the remuneration and headcount inputs as an extract but cannot compute or file the index. |


##### out_of_scope #2

| Key | Value |
|---|---|
| `filing_id` | FR-HR-002 |
| `authority` | Works council (comite social et economique) |
| `descoping_reason` | HR-scope - requires data beyond payroll system. The social report (bilan social), due from employers with 300 or more employees, requires recruitment, training, health-and-safety, industrial-relations and working-conditions data. |
| `client_impact` | Refer to HRMS team. |


##### out_of_scope #3

| Key | Value |
|---|---|
| `filing_id` | FR-HR-003 |
| `authority` | Works council |
| `descoping_reason` | HR-scope - requires data beyond payroll system. The economic, social and environmental database (BDESE) requires investment, environmental and governance data. |
| `client_impact` | Refer to HRMS team. |


##### out_of_scope #4

| Key | Value |
|---|---|
| `filing_id` | FR-HR-004 |
| `authority` | DARES, Ministry of Labour statistical service |
| `descoping_reason` | HR-scope - requires data beyond payroll system. The ACEMO survey of labour activity and employment conditions is a sampled statistical survey requiring vacancy and working-conditions data. |
| `client_impact` | Refer to HRMS team. |


##### out_of_scope #5

| Key | Value |
|---|---|
| `filing_id` | FR-HR-005 |
| `authority` | Ministry of Labour |
| `descoping_reason` | HR-scope - requires data beyond payroll system. The gender-balance obligation for senior executives and governing bodies, applying to employers above 1,000 employees with a 30% target from 1 March 2026, requires the composition of governing bodies, which is corporate-secretariat data. |
| `client_impact` | Refer to the client's corporate secretariat. |


##### out_of_scope #6

| Key | Value |
|---|---|
| `filing_id` | FR-FIN-001 |
| `authority` | DGFiP |
| `descoping_reason` | Not a payroll filing. The taxes on the use of vehicles for economic purposes (which replaced the former taxe sur les vehicules de societe) are assessed on the fleet - emissions, age and use - not on remuneration. Distinct from the company-vehicle benefit in kind, which IS in payroll scope and is covered in CCG Module 7.2. |
| `client_impact` | Refer to the client's finance or fleet function. Payroll continues to value and contribute the benefit in kind. |


##### out_of_scope #7

| Key | Value |
|---|---|
| `filing_id` | FR-FIN-002 |
| `authority` | DGFiP |
| `descoping_reason` | Not a payroll filing. The construction investment obligation (participation des employeurs a l'effort de construction) for employers of 50 or more is discharged by direct investment, with a levy on any unfulfilled part declared to DGFiP with the corporate tax return. Payroll supplies only the wage base. |
| `client_impact` | Refer to the client's finance function; payroll provides the annual payroll figure on request. |


##### out_of_scope #8

| Key | Value |
|---|---|
| `filing_id` | FR-MSA-001 |
| `authority` | Mutualite Sociale Agricole |
| `descoping_reason` | Outside the regime general. The agricultural scheme has its own collection network, its own DSN channel and its own contribution set. |
| `client_impact` | An agricultural client requires an MSA variant of the DSN; this build does not produce one. |


##### out_of_scope #9

| Key | Value |
|---|---|
| `filing_id` | FR-CIBTP-001 |
| `authority` | Sector paid-leave funds (caisses de conges payes) in construction, public works, entertainment, dockers and transport |
| `descoping_reason` | Sector-specific flow not built for the baseline France build. In these sectors the FUND pays the employee's holiday pay and the employer pays a contribution to the fund, so the employer shows no holiday pay on the payslip and pays NO compensatory leave indemnity on termination. The mechanism is documented in CCG Modules 2.1, 8.1 and 9.1 so that it is not missed; the fund declaration itself is not specified. |
| `client_impact` | A construction, public-works or entertainment client needs this flow scoped and built before go-live. A general-regime payroll configuration will be wrong for them in BOTH the payslip and the DSN - this is a go/no-go item, not a refinement. |


##### out_of_scope #10

| Key | Value |
|---|---|
| `filing_id` | FR-DGFIP-004 |
| `authority` | DGFiP |
| `descoping_reason` | Not a payroll obligation. The withholding under General Tax Code Article 182 B, at 25% on sums paid to a non-resident for services rendered or used in France, is an accounts-payable obligation on payments to self-employed service providers, not an employer withholding on remuneration. |
| `client_impact` | Flag to the client's finance function - it is frequently missed - but it must not be modelled in the payroll engine. |


##### out_of_scope #11

| Key | Value |
|---|---|
| `filing_id` | FR-DGFIP-005 |
| `authority` | DGFiP |
| `descoping_reason` | Assessment-level, not withholding-level. The minimum assessment rate for non-residents under General Tax Code Article 197 A (20% up to EUR 29,579 of French net taxable income and 30% above; 14.4% and 20% for overseas-source income) is applied by the tax administration on the annual assessment and is displaceable by proof of a lower worldwide rate. |
| `client_impact` | Must NOT be modelled in the payroll engine, the wage type catalogue or the data dictionary. The employer applies only the Article 182 A scale. Recorded explicitly because an assessment-level levy was wrongly propagated into withholding artifacts in an earlier country in this pipeline. |


##### out_of_scope #12

| Key | Value |
|---|---|
| `filing_id` | FR-URSSAF-005 |
| `authority` | URSSAF |
| `descoping_reason` | Out of the employment-type scope. Contributions for company officers who are self-employed (majority-shareholding SARL managers and other travailleurs non salaries) are assessed and paid personally under the SSI scheme. |
| `client_impact` | Refer to the client's accountant; these individuals must not be loaded as employees. |


##### out_of_scope #13

| Key | Value |
|---|---|
| `filing_id` | FR-DGFIP-006 |
| `descoping_reason` | Not an employer payroll filing for the regime general. PASRAU (NEORAU norm, technical specification CT2026.1.1 for 2026) is the withholding-at-source declaration for income OTHER than wages and salaries. Its own specification limits its perimeter to bodies paying non-wage income - pension and retirement funds, bodies paying replacement income directly, and the single-window schemes. Withholding on employment income for this population travels in the DSN (FR-DSN-001), so the payroll engine builds no PASRAU file. Individual employers are expressly excluded from PASRAU. |
| `client_impact` | None for the in-scope population. Where a third-party body pays income directly to an employee and files its own PASRAU, payroll must not withhold on that income nor carry it in the DSN individual block - the engine needs a payment-source flag distinguishing 'paid by employer' from 'paid directly by third-party body'. Subrogated payments made through the employer remain in the DSN and are unaffected. Reversal (e.g. client entity begins paying pensions or annuities) is a contained addition of one outbound flow. |


### wage_type_categories


#### in_scope (35 items)

- Base salary for the contractual working time (salaire de base), smoothed at 151.67 hours for a full-time 35-hour week
- Overtime, base and premium (25% for the first eight hours beyond 35 in the week, 50% thereafter, floor of 10% by agreement)
- Additional hours for part-time employees (heures complementaires), 10% within the first tenth and 25% beyond
- Days worked beyond an annual day-count arrangement, premiumed at at least 10%
- Seniority bonus (prime d'anciennete)
- Thirteenth month (13eme mois)
- Holiday bonus (prime de vacances)
- Performance and objectives bonus
- Commission, including a contractual guaranteed minimum against commission
- On-call, shift, Sunday and night premiums
- Paid annual leave pay, computed as the higher of the one-tenth rule and the salary maintenance rule
- Public holiday pay, including the 100% premium for work on 1 May
- Working-time reduction days (jours de RTT) and their monetisation
- Employer top-up on sickness (90% for 30 days, 66.66% for the next 30, after one year's service and a seven-day waiting period)
- Daily social security benefits transiting the payslip where the employer is subrogated
- Partial activity (activite partielle) allowance
- Benefits in kind: company vehicle, accommodation, meals (EUR 5.50 per meal for 2026), communication tools
- Meal vouchers, employer share exempt to EUR 7.32 per voucher at 50% to 60% of face value
- 50% reimbursement of the public transport season ticket (compulsory)
- Sustainable mobility allowance
- Professional expense reimbursements, within and above the statutory limits
- Value-sharing bonus (prime de partage de la valeur), standard and enhanced regimes
- Compensatory notice indemnity (ordinary pay)
- Compensatory leave indemnity (ordinary pay)
- Fixed-term end-of-contract indemnity, 10% or 6% (ordinary pay)
- Non-compete indemnity (ordinary pay)
- Statutory and collectively agreed redundancy payments, with the three-layer exemption
- Mutually agreed termination and compulsory retirement indemnities, with the 40% employer contribution
- Voluntary retirement indemnity (fully contributable and taxable outside a collective redundancy plan)
- Impatriation premium under General Tax Code Article 155 B, real amount or 30% flat
- Expatriation supplements exempt within 40% under General Tax Code Article 81 A
- Employee and employer contributions to the compulsory health cover, death-and-disability cover and supplementary pension schemes
- Advance on the current month (acompte) as a netting line, NOT a separate pay run
- Advance in the strict sense (avance), recoverable at one tenth of pay per period
- Wage attachments, maintenance orders paid by direct payment, and tax levy notices


#### out_of_scope (7 items)

- Attendance fees (jetons de presence) paid to non-executive directors - taxed as investment income at 12.8% plus capital social levies of 18.6%, with a 20% flat social contribution owed by the company; outside the gross-to-net chain
- Free share acquisition gains and share option exercise gains - taxable in the year of DISPOSAL, outside withholding at source and outside the ordinary contribution bands. Only the 30% employer contribution (and, above EUR 300,000, the 10% employee contribution) touch the DSN
- Profit-sharing and incentive-scheme amounts (participation, interessement) once invested - outside gross pay, with their own regime and their own scheme administrator
- Employee payments into a company savings plan or collective retirement savings plan - a saving, not a contribution
- Self-employed contractor invoices - not remuneration, no employer withholding
- Holiday pay in the construction, public works and entertainment sectors - paid by the sector fund, not by the employer
- Student loan repayments - NO SUCH DEDUCTION EXISTS IN FRANCE. Recorded explicitly so that a requirement referring to one is raised as an error rather than configured


#### special_rules (16 items)

- THREE SEPARATE LIABILITIES: a component's treatment for social security contributions, for the 9.70% social levies and for income tax are three independent questions with three possibly different answers. The employer's compulsory health-cover contribution is the canonical case - exempt from contributions within limits, subject to the social levies at 100% with NO 1.75% allowance, AND added to the net taxable amount.
- THE EMPLOYER'S SUPPLEMENTARY PENSION CONTRIBUTION BEHAVES DIFFERENTLY AGAIN: exempt from contributions within the Social Security Code Article D242-1 limit, inside the social levies base at 100%, and OUTSIDE the net taxable amount within the General Tax Code Article 83, 2 limit. Two employer benefit contributions, two different answers - do not generalise from one to the other.
- TWO EXEMPTION LIMITS ON THE SAME PREMIUM: the income tax limit (General Tax Code Article 83) and the social security limit (Social Security Code Article D242-1) are different figures under different texts. Testing one and assuming the other is the standard failure in this area.
- FIVE DISTINCT BASES, NOT ONE TAXABLE INCOME: capped and uncapped contribution bases, the social levies base (98.25% of pay up to four annual ceilings, PLUS employer supplementary-cover contributions at 100%), the net social amount, the net taxable amount, and the net payable. A system that derives one from another by a simple offset will produce a non-compliant payslip.
- THREE NET FIGURES MUST APPEAR ON EVERY PAYSLIP and they are never equal: net payable before income tax, net social amount (montant net social, compulsory since 1 July 2023) and net taxable amount.
- THE NET TAXABLE AMOUNT IS HIGHER THAN THE NET PAYABLE BEFORE TAX, because the non-deductible general social contribution (2.40%), the social debt repayment contribution (0.50%) and the employer health-cover contribution are all added back. Withholding on the net payable systematically under-withholds.
- TWO MINIMUM-WAGE PARAMETERS ARE SIMULTANEOUSLY LIVE IN 2026: the live pay reference (EUR 12.02 to 31 May, EUR 12.31 from 1 June) and the reference frozen at EUR 12.02 for the whole year inside the general reduction, per Decret n. 2026-509 of 12 June 2026. An engine reading one 'current minimum wage' variable will overstate the relief from June onward.
- TWO DEFAULT WITHHOLDING GRIDS COEXIST IN 2026: the grid carried over from 2025 for income PAID from January to April, and the 2026 grid for income paid from 1 May. The applicable grid follows the DATE OF PAYMENT, and no retrospective adjustment is made.
- OVERTIME CARRIES THREE SEPARATE RELIEFS with three different mechanics: an employee old-age relief capped at 11.31%, an employer flat deduction of EUR 1.50 an hour below 20 employees and EUR 0.50 at 20 and above (the former 250-employee exclusion was removed from 1 January 2026), and an income tax exemption capped at EUR 7,500 net per year per employee. None of them touches the 9.70% social levies.
- THE GENERAL REDUCTION ENDS IN A CLIFF, NOT A TAPER: the coefficient floors at Tmin = 0.0200 and the relief then stops because annual pay has passed 3 x EUR 21,876.40 = EUR 65,629.20. It must also be capped against the employer contributions it is actually imputed against, of which only 0.49 points of the industrial-accident rate qualify.
- TERMINATION PAY SPLITS INTO ORDINARY PAY AND EXEMPT INDEMNITY: salary, notice, the leave payout and the fixed-term end-of-contract indemnity are ordinary pay in every respect; only the severance family carries the three-layer exemption, and the social levies exemption uses a DIFFERENT comparison from the income tax one.
- TERMINATION PACKAGES ABOVE 10 PASS (EUR 480,600) LOSE EVERY SOCIAL EXEMPTION FROM THE FIRST EURO. A cliff on the aggregate, tested before any other exemption test.
- NO SALARY SACRIFICE: the non-substitution principle appears in every exemption text. An exempt payment loses its exemption if it substitutes for any element of remuneration, unless twelve months have elapsed.
- NEGATIVE GROSS IS NOT A PAYSLIP LINE: a correction to a base already declared is a DSN regularisation carrying the period concerned, not a negative wage type in the current month.
- THE COLLECTIVE AGREEMENT IDENTIFIER (IDCC) IS A FIRST-CLASS CONFIGURATION KEY, not an informational field. It determines minimum pay scales, the seniority bonus, the thirteenth month, notice periods, severance above the statutory floor, sick-pay top-ups and most non-statutory leave.
- THE VALUE-SHARING BONUS ENHANCED REGIME EXPIRES ON 31 DECEMBER 2026 - a dated parameter requiring a review flag, not a permanent setting.


### option_mapper_scope

| Key | Value |
|---|---|
| `_comment` | For each option mapper, the codes that ARE in scope. Out-of-scope codes must be excluded from ALL artifacts. |


#### personal_id_type (2 items)

- NIR - numero d'inscription au repertoire, 15 characters (13 digits + 2-digit key); key = 97 minus (the 13-digit number modulo 97); Corsican department codes 2A and 2B are converted before the key is computed
- NTT - numero technique temporaire, up to 40 characters, conventionally the SIRET plus an internal sequence; used only until the NIR is issued and must be replaced as soon as it is


#### insurance_type (6 items)

- Regime general - URSSAF, CNAM, CNAV
- Regime general plus the Alsace-Moselle local health scheme (additional 1.30% employee contribution, triggered by the place of work)
- AGIRC-ARRCO supplementary pension (bands 1 and 2)
- Compulsory supplementary health cover (complementaire sante), employer share at least 50%
- Managerial-grade death-and-disability cover, 1.50% of the capped band, wholly employer-paid
- Optional death-and-disability and supplementary pension schemes, collective and compulsory


#### contract_type (6 items)

- CDI - permanent contract
- CDD - fixed-term contract
- Apprenticeship contract
- Professionalisation contract
- Temporary-agency assignment
- Internship agreement (convention de stage) - gratuity, not a wage


#### working_time_type (3 items)

- Full-time 35-hour week, 151.67 hours a month
- Part-time, with the social security ceiling prorated on the hours ratio
- Annual day-count arrangement (forfait annuel en jours), typically 218 days - no overtime


#### withholding_rate_type (4 items)

- Taux personnalise - personal rate transmitted by the tax administration
- Taux individualise - individualised rate within a couple
- Taux non personnalise - the statutory default grid, by territory (metropolitan; Guadeloupe, Martinique and La Reunion; Guyane and Mayotte) and by period (monthly, quarterly, weekly, daily, hourly)
- Retenue a la source non-resident - General Tax Code Article 182 A, 0/12/20 bands, or 0/8/14.4 for overseas-source income


#### correction_codes (4 items)

- Cancel-and-replace declaration for a month whose deadline has not passed
- Contribution regularisation carried in the contribution-base block with the start and end dates of the period of attachment
- Withholding regularisation carried in the dedicated block, dated to the month of the original error
- Amending or cancelling event signal


#### benefit_type (11 items)

- Company vehicle
- Accommodation
- Meals
- Communication tools
- Meal vouchers
- Public transport season ticket reimbursement
- Sustainable mobility allowance
- Compulsory health cover
- Death-and-disability cover
- Supplementary pension scheme
- Company savings plan and collective retirement savings plan employer contributions


#### residence_status (5 items)

- Tax resident (domicilie fiscalement en France) under General Tax Code Article 4 B, as modified by any applicable treaty
- Non-resident
- Affiliated to the French social security scheme
- Posted worker holding a portable document A1 for another state - no French contributions
- Note: tax residence and social security affiliation are INDEPENDENT tests decided by independent criteria. An individual may be one without the other.


#### leave_type (11 items)

- Paid annual leave (conges payes), in working days (jours ouvrables, 30 a year) or worked days (jours ouvres, 25 a year) - the two units must NEVER be mixed in one calculation
- Working-time reduction days (jours de RTT)
- Seniority leave (conges d'anciennete)
- Maternity, paternity and child-welcome, adoption, birth leave
- Supplementary birth leave (new from 1 July 2026, up to 2 months per parent at 70% then 60% of net pay)
- Sick leave, non-occupational
- Work accident and occupational disease leave
- Family event leave, and bereavement leave for a child
- Parental education leave, carer's leave, parental presence leave
- Unpaid leave by agreement (conge sans solde) - no statutory framework, agreed in writing case by case
- Time savings account (compte epargne-temps)


### integrations

| Key | Value |
|---|---|
| `_note` | Inbound files where HRB must parse/act = product_mapping_required=true. Never default inbound=not-in-scope. |


#### outbound (12 items)


##### 1. FR-DSN-001

| Key | Value |
|---|---|
| `id` | FR-DSN-001 |
| `to` | URSSAF and all attached bodies, via net-entreprises.fr |
| `format` | TXT |
| `frequency` | monthly |
| `note` | NEODeS structured file, technical specification CT2026.1.2. The single monthly payroll declaration. |


##### 2. FR-DSN-002

| Key | Value |
|---|---|
| `id` | FR-DSN-002 |
| `to` | France Travail, via net-entreprises.fr |
| `format` | TXT |
| `frequency` | per event, within 5 days |
| `note` | End-of-contract event signal. Does not dispense the employer from giving the employee a signed copy. |


##### 3. FR-DSN-003

| Key | Value |
|---|---|
| `id` | FR-DSN-003 |
| `to` | CPAM, via net-entreprises.fr |
| `format` | TXT |
| `frequency` | per event, within 5 days |
| `note` | Work stoppage and resumption event signals. |


##### 4. FR-URSSAF-001

| Key | Value |
|---|---|
| `id` | FR-URSSAF-001 |
| `to` | URSSAF, via net-entreprises.fr |
| `format` | XML |
| `frequency` | per hire |
| `note` | Pre-hire declaration. Still a SEPARATE filing in 2026; its move into the DSN is deferred to 1 January 2027 at the earliest. |


##### 5. FR-URSSAF-003

| Key | Value |
|---|---|
| `id` | FR-URSSAF-003 |
| `to` | URSSAF for Agefiph |
| `format` | TXT |
| `frequency` | annual, inside the April DSN |
| `note` | Disabled-worker employment return, due 5 or 15 May. |


##### 6. FR-URSSAF-004

| Key | Value |
|---|---|
| `id` | FR-URSSAF-004 |
| `to` | URSSAF |
| `format` | TXT |
| `frequency` | annual, inside the April DSN |
| `note` | Apprenticeship tax balance, 0.09% of the preceding year's payroll. |


##### 7. FR-DGFIP-003

| Key | Value |
|---|---|
| `id` | FR-DGFIP-003 |
| `to` | DGFiP, impots.gouv.fr |
| `format` | XML |
| `frequency` | monthly, quarterly or annual by amount |
| `note` | Payroll tax forms 2501-SD and 2502-SD. Conditional on the client being liable; suppress rather than file nil. |


##### 8. FR-CPAM-002

| Key | Value |
|---|---|
| `id` | FR-CPAM-002 |
| `to` | CPAM, via net-entreprises.fr |
| `format` | XML |
| `frequency` | per event, within 48 hours |
| `note` | Work accident declaration. |


##### 9. FR-CDC-001

| Key | Value |
|---|---|
| `id` | FR-CDC-001 |
| `to` | Caisse des Depots, SOLTeA |
| `format` | XLSX |
| `frequency` | annual |
| `note` | Allocation of the apprenticeship tax balance. Optional client decision. |


##### 10. FR-BANK-001

| Key | Value |
|---|---|
| `id` | FR-BANK-001 |
| `to` | The employee's bank |
| `format` | XML |
| `frequency` | monthly |
| `note` | SEPA credit transfer of net pay, ISO 20022 payment initiation. Compulsory above EUR 1,500 net a month, where cash payment is prohibited by Labour Code Article L3241-1. The account must be one the employee holds or jointly holds. |


##### 11. FR-PAYSLIP-001

| Key | Value |
|---|---|
| `id` | FR-PAYSLIP-001 |
| `to` | The employee, and the electronic archiving service |
| `format` | PDF |
| `frequency` | monthly |
| `note` | The payslip must be in French. Where issued electronically, availability must be guaranteed for 50 YEARS, or until the employee reaches 75, whichever is later - an obligation that survives the end of the service contract. A five-year retention setting on an electronic payslip archive is a breach. |


##### 12. FR-GL-001

| Key | Value |
|---|---|
| `id` | FR-GL-001 |
| `to` | The client's general ledger |
| `format` | CSV |
| `frequency` | monthly |
| `note` | Not a statutory obligation. Mapped to the client's own accounting periods, which need not be the calendar year even though every statutory output is. |


#### inbound (8 items)


##### 1. FR-DGFIP-002

| Key | Value |
|---|---|
| `id` | FR-DGFIP-002 |
| `from` | DGFiP, via the DSN return flow (compte rendu metier) on net-entreprises.fr |
| `format` | TXT |
| `frequency` | monthly |
| `product_mapping_required` | true |
| `note` | The withholding rate, its type and its validity period. The ONLY lawful source of an employee's rate - the employer never collects a tax number and never computes a rate. Must be parsed, applied from the following payslip, and DATE-CHECKED on every run; on expiry, revert to the default grid. |


##### 2. FR-URSSAF-002

| Key | Value |
|---|---|
| `id` | FR-URSSAF-002 |
| `from` | URSSAF and the old-age insurance fund, via net-entreprises.fr |
| `format` | TXT |
| `frequency` | monthly, plus an annual reminder in March |
| `product_mapping_required` | true |
| `note` | Certification or rejection of each social security number, correction of civil-status data, and blocking and non-blocking anomalies. From June 2026 an uncorrected anomaly on the CAPPED GROSS BASE may be substituted by the authority itself, after which the employer's records and the authority's diverge. |


##### 3. FR-CARSAT-001

| Key | Value |
|---|---|
| `id` | FR-CARSAT-001 |
| `from` | CARSAT, via the compte AT/MP on net-entreprises.fr |
| `format` | XML |
| `frequency` | annual, and on reclassification |
| `product_mapping_required` | true |
| `note` | The establishment-specific industrial-accident net rate and risk code, stored per SIRET. Subscribing has been compulsory from the first employee since 1 January 2022, on penalty of 0.5% to 1.5% of the monthly ceiling per employee. |


##### 4. FR-CPAM-003

| Key | Value |
|---|---|
| `id` | FR-CPAM-003 |
| `from` | CPAM |
| `format` | TXT |
| `frequency` | per event |
| `product_mapping_required` | true |
| `note` | Daily social security benefit statements where the employer is subrogated. Needed to reconcile the offsetting payslip line and the employer's cash position. |


##### 5. FR-AGIRC-001

| Key | Value |
|---|---|
| `id` | FR-AGIRC-001 |
| `from` | AGIRC-ARRCO institutions, through the DSN return flow |
| `format` | TXT |
| `frequency` | monthly |
| `product_mapping_required` | true |
| `note` | Membership and point-allocation feedback. Supplementary pension data travels inside the DSN; the institution is identified by its membership reference, and a wrong reference silently misroutes the contribution. |


##### 6. FR-CLIENT-001

| Key | Value |
|---|---|
| `id` | FR-CLIENT-001 |
| `from` | The client's HRMS |
| `format` | CSV |
| `frequency` | monthly |
| `product_mapping_required` | true |
| `note` | Master data, absences, and variable pay. Must carry the collective agreement identifier (IDCC), the occupational category code (PCS-ESE), the workplace SIRET, the managerial-grade flag, the contractual working time and the day-count arrangement where applicable - each of these drives a calculation, not merely a report. |


##### 7. FR-CLIENT-002

| Key | Value |
|---|---|
| `id` | FR-CLIENT-002 |
| `from` | The outgoing payroll provider, on migration |
| `format` | XLSX |
| `frequency` | one-off |
| `product_mapping_required` | true |
| `note` | Year-to-date counters. A provider change does not change the employer, so every cumulative mechanism continues: capped and uncapped bases and ceiling entitlement since 1 January, annual pay for the general reduction, the four-annual-ceiling cap on the 1.75% allowance, exempt overtime against the EUR 7,500 cap, net taxable pay and tax withheld, leave balances by accrual period, seniority date, and value-sharing bonus already paid. Reconcile against the DSN already filed, not against payslips alone. |


##### 8. FR-COURT-001

| Key | Value |
|---|---|
| `id` | FR-COURT-001 |
| `from` | Court enforcement officers (commissaires de justice) and DGFiP |
| `format` | PDF |
| `frequency` | per event |
| `product_mapping_required` | true |
| `note` | Records of wage attachment, maintenance orders enforced by direct payment, and tax levy notices. Since 1 July 2025 the procedure is conducted by enforcement officers rather than the courts; the employer must respond within fifteen days and pay monthly to the DISTRIBUTING enforcement officer, never apportioning between creditors itself. |


#### both (1 items)


##### 1. FR-DGFIP-001

| Key | Value |
|---|---|
| `id` | FR-DGFIP-001 |
| `with` | DGFiP |
| `format` | TXT |
| `frequency` | monthly, quarterly option below 11 employees |
| `product_mapping_required` | true |
| `note` | Withholding at source. Outbound: the net taxable amount, the rate applied and the amount withheld, declared inside the DSN and collected by direct debit (the 8th or the 18th of the following month by headcount). Inbound: the rate the administration transmits. Two halves of one obligation - a failure in the DSN is simultaneously a social security failure and a tax failure. |


### known_failure_patterns_to_check (22 items)

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


### failure_pattern_notes

| Key | Value |
|---|---|
| `F18` | Stale law references. The 2026 France build supersedes: the pre-2026 reduction Fillon parameters (coefficient 0.3193/0.3233 at 1.6 SMIC), the separate 7% reduced employer sickness rate capped at 2.25 SMIC, the separate 3.45% reduced family-allowance rate capped at 3.5 SMIC (all replaced by the single degressive general reduction from 1 January 2026); the 2025 default withholding grids for income paid from 1 May 2026; the 2025 non-resident scale; the 30% employer contribution on mutually agreed terminations (now 40%); the pre-April-2025 sickness daily allowance cap of 1.8 SMIC (now 1.4); and capital social levies at 17.2% (now 18.6%). None of these values may appear in any France artifact. |
| `F19` | HR-scope reports. Five filings are descoped to the HRMS team above (FR-HR-001 to FR-HR-005). The professional equality index is the highest-risk of them because it looks like a pay report: it requires promotion rates, pay-rise rates and the sex of the ten highest earners, which payroll does not hold. |
| `F20` | WTC tax codes must come from France's own legend - the DSN remuneration type codes, bonus and indemnity type codes, contribution-base codes and individual contribution codes of the NEODeS technical specification CT2026.1.2 - and not from a neighbouring country's catalogue. |
| `F21` | Filing mechanics. VERIFIED, NOT ASSUMED (C4): France CONSOLIDATES. Social security contributions and the income tax withheld are declared inside ONE monthly DSN and collected by direct debit initiated from it. There is no separate income tax return for payroll. Deadlines follow HEADCOUNT, not pay frequency: DSN and contributions on the 5th (50 or more employees) or the 15th; the withholding remittance on the 8th or the 18th. The quarterly option below 11 employees changes the PAYMENT rhythm only - the DSN remains monthly. The disabled-worker return and the apprenticeship tax balance are annual obligations discharged INSIDE the April DSN, not as separate filings. |
| `F22` | See the wage_type_categories.special_rules block, which records the sixteen cross-cutting rules that generate most France defects. |


### scope_manifest_changelog (1 items)


#### scope_manifest_changelog #1

| Key | Value |
|---|---|
| `version` | 1.1 |
| `date` | 2026-08-27 |
| `by` | Wallisson Gomes |
| `change` | Pre-submission audit gate. Added spec_file, spec_link_basis, sir_authority and sir_runbook to all 15 in_scope filings. Before this, 0 of 15 declared a spec link: C18 could not resolve coverage mechanically and C20 reported FAIL. The links were read from each spec's own Document ID cell and gated on an exact 1:1 bijection, not inferred from filenames. Seeded known_limitations, which was null, with the three open items the build's own logs had registered locally but never promoted to the country-level register (failure pattern F30). |


### known_limitations (3 items)


#### 1. FR-LIM-001

| Key | Value |
|---|---|
| `id` | FR-LIM-001 |
| `title` | 199 spec rows marked payroll master data have no Data Dictionary counterpart |
| `raised_by` | 07-qa-crosscheck/FR-ALIGNMENT-PATCH.md (27 Aug 2026) |
| `detail` | 148 distinct NEODeS rubriques. Mostly change-history echoes (57) and the share-scheme block already flagged in the DD build log (30). At least one looks like a genuine omission: employee e-mail address. |
| `what_would_close_it` | A Stage-4 scope decision on whether to add up to 148 fields to the Data Dictionary. Deliberately not taken during the alignment patch, because adding fields is a scope change, not an alignment edit. |
| `status` | open |


##### consumers (2 items)

- 05-data-dictionary/FR-DD-001-v1.0.xlsx
- 04-reports-spec/ (all 15 specs, column L)


#### 2. FR-LIM-002

| Key | Value |
|---|---|
| `id` | FR-LIM-002 |
| `title` | FR-CARSAT-001 notification field layout not obtained |
| `raised_by` | 04-reports-spec/FR-CARSAT-001-NotificationTauxATMP-Spec.xlsx (File Structure sheet) |
| `detail` | The AT/MP rate notification is consulted on the net-entreprises.fr portal. No published field layout exists, so Position/Length are recorded as NOT OBTAINED rather than invented. The field set itself is sourced and complete. |
| `what_would_close_it` | CARSAT publishing a machine-readable layout for the notification. |
| `status` | open_by_design |


##### consumers (1 items)

- 04-reports-spec/FR-CARSAT-001-NotificationTauxATMP-Spec.xlsx


#### 3. FR-LIM-003

| Key | Value |
|---|---|
| `id` | FR-LIM-003 |
| `title` | SOLTeA employer portal guide is an image-only PDF; text extraction failed |
| `raised_by` | 03-statutory-integrations/integration-landscape.json (CDC-SOLTEA specifications note) |
| `detail` | Guide-utilisateur-portail-employeur.pdf was retrieved but could not be text-extracted in this environment on 27 Aug 2026. CDC-SOLTEA is in any case a portal-only authority with no machine-to-machine channel, so no runbook depends on it. |
| `what_would_close_it` | OCR of the guide, or CDC publishing a text PDF. |
| `status` | open |


##### consumers (2 items)

- 04-reports-spec/FR-CDC-001-SOLTeA-Spec.xlsx
- 03-statutory-integrations/FR-SIR-INDEX-001-v1.0.docx

