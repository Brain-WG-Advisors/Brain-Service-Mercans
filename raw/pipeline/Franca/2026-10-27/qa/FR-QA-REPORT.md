# FRANCE — QA CROSS-CHECK REPORT

**Artifact set:** `FR-compliance/` · **Standard:** v2.4 · **Filing year:** 2026 · **Currency:** EUR
**Date:** 2026-08-28 · **Auditor:** independent QA cross-check (did not build these artifacts)
**Method:** every figure below was measured mechanically from the delivered binaries, not read from
a build log or a prior report. The superseded report of 12:21 today is preserved at
`FR-QA-REPORT.md.bak-20260828-124820`; where this audit reaches a different number, the
divergence is stated explicitly and the measurement is shown.

---

## EXECUTIVE SUMMARY

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

## PER-CHECK ALIGNMENT SCORES

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

### Check 1 — CCG ↔ WTC alignment · 2 confirmed gaps

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

### Check 2 — CCG Module 2 ↔ DD · 35 of 35 (100%)

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

### Check 3 — CCG Module 10 ↔ Report Specs · 11 of 12 (91.7%)

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

### Check 4 — DD ↔ Report Specs (4-bucket) · 720 of 984 as delivered (73.2%)

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

### Check 5 — Global WTC coverage · 300 of 300 (100%)

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

### Check 6 — Scope discipline · 0 violations

| Rule | Result |
|---|---|
| No calculated amounts or Base Salary in the DD | ✅ 0 of 189 field names match calculated/base-salary patterns |
| No identification data in the WTC | ✅ only "Birth allowance" (row 228) trips an identifier regex — a wage type, not identity data |
| No full field specs in CCG Module 2 | ✅ six data groups, explicit pointer to the DD |
| No full field specs in CCG Module 10 | ✅ *"Field-level layouts … are held in the France Report Specifications and are not reproduced here."* |

---

### Check 7 — Report Spec format compliance · 15 of 15 (100%)

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

### Check 8 — v2.4 standards · 5 of 5 artifact classes

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

### Check 9 — v2.4 NEW · composite key / inter-field constraints · 3 of 4

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

## GLOBAL WTC COVERAGE SUMMARY

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

## ISSUES

### MAJOR

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

### MINOR

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

## v2.4 COMPLIANCE SUMMARY

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

## SCORING

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

## READINESS VERDICT

# ⚠️ NEEDS PATCHES

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

## AUDIT METHOD AND DIVERGENCES FROM THE SUPERSEDED REPORT

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
