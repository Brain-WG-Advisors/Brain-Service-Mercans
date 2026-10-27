# BE-QA-REPORT — Stage 10 Cross-Check, Belgium (BE)

| | |
|---|---|
| **Date** | 2026-08-21 |
| **Mode** | Read-only regression sweep over a delivered country. Nothing was edited. |
| **Reviewer** | compliance-qa-auditor (independent; did not build any BE artifact) |
| **Scope** | The 9 Stage-10 checks, verbatim from the pipeline prompt, run against every artifact read from disk |
| **Score** | **4 of 9 checks fully PASS** · 4 PASS-WITH-FINDINGS · 1 FAIL |
| **Verdict** | **NOT READY FOR DEV HANDOVER** — 1 CRITICAL, 6 MAJOR open |

---

## 0. Provenance and deviations from the task brief

Three things in the brief did not match the disk. All were resolved by searching the tree; nothing was marked N/A.

| Brief said | On disk | Consequence |
|---|---|---|
| `mercans_pipeline_v2_4.sh` Stage 10 | Only `~/mercans-pipeline/mercans_pipeline_v2_9.sh` exists | The 9 checks were run exactly as written in the prompt. Where v2.9 doctrine differs from the v2.4 wording, the divergence is recorded (see Check 8, payslip 5-sheet vs 8-sheet). |
| `01-ccg/BE-CCG-001-v1.1-DRAFT-2026-08-21.docx` | `01-ccg/BE-CCG-001-v1.0.docx` (18 Aug 10:20) — **no v1.1 and no DRAFT-2026-08-21 file exists** | The v1.0 file was audited. |
| `05-data-dictionary/BE-DD-001-v1.3-DRAFT-2026-08-21.xlsx` | `05-data-dictionary/BE-DD-001-v1.1.xlsx` (17 Aug 18:19) — **no v1.2, no v1.3** | The v1.1 file was audited. Every downstream citation on disk also names `BE-DD-001-v1.1`, so v1.1 is the live version, not a stale one. |

### The prior partial pass, re-verified claim by claim

The brief's summary was **not** used as ground truth. Each claim was re-tested:

| Prior claim | Verdict after re-test | Evidence |
|---|---|---|
| "91/91 DD citations in the one available report spec resolved correctly" | **CONFIRMED, but not generalisable.** `BE-NSSO-004-DRS-Spec.xlsx!'DRS Spec'` carries exactly 91 `BE-DD-001-v1.1 — 'Field'(Sheet)` citations and all 91 resolve. Across all nine specs there are **318** such citations and all 318 resolve — but **5 of the 9 specs carry none at all** (see Check 4, ISSUE-2). | measured |
| "46/46 conditional fields had reasons" | **SUPERSEDED — the real number is 503/503.** Across all nine specs there are 503 rows with Mandatory = C, and every one carries a Conditional Reason in column G. The DRS spec alone has 46. | measured |
| "0 scope-discipline violations either direction" | **CONFIRMED** across all artifacts (Check 6). | measured |
| NSSO Annexe 7 (zone 00067) / Annexe 8 (zone 00062) only partially known | **CONFIRMED and honestly recorded in the artifacts.** `BE-NSSO-002-DmfA-Spec.xlsx!'Field Options'!A8` and `!A16` both carry `NOT FOUND` rows stating the code set is not reproduced. | measured |
| Annexe 12 (zone 00430) fully unknown | **PARTLY WRONG.** For the DRS ZIMA scenario, yes — `BE-NSSO-004-DRS-Spec.xlsx!'Field Options'!E3` says "Annexe 12 NOT HELD". But zone 00430 is **fully specified** for the work-accident scenario: `BE-FEDRIS-001-WorkAccident-Spec.xlsx!'Field Options'!A2:E5` gives 001/002 with the glossary as source, and 20 conditional rules in column G key off it. |
| DRS-specific zone 00221 truncated at value 4 | **CONFIRMED as a shape, not as a defect.** `BE-NSSO-004-DRS-Spec.xlsx!'Field Options'!A42:A46` gives 5 rows for zone 00221, and `!'DRS Spec'!O11` carries the full glossary legend. Same 5-row treatment in Dimona (`A42:A45`), DmfA (`A55:A59`) and WorkAccident (`A35:A39`). No truncation defect found. |
| DD zone 00625 / 00096 fixes not propagated to the DRS-Spec's Field Options | **FALSE — the opposite is true.** `BE-NSSO-004-DRS-Spec.xlsx!'Field Options'!A85:A89` carries Days Justification (00625) and `!A111:A114` carries Legal Basis (00096). The propagation gap is in a **different** file: `BE-NSSO-003-DmfAModification-Spec.xlsx` (see ISSUE-6). |
| WTC Tax Credit still says "reform NOT CONFIRMED AS ENACTED" while CCG 6.3 says "CONFIRMED ENACTED" via the Law of 15 July 2026 / RD of 30 July 2026 | **FALSE — no inconsistency exists.** `BE-WTC-001-v1.0.xlsx!'Tax Credit'!B5` does carry "NOT CONFIRMED AS ENACTED", and the CCG **agrees with it**: `BE-CCG-001-v1.0.docx` Module 7.1 states "Both readings are stated because the enactment is unconfirmed." A full-document search finds **0** occurrences of "CONFIRMED ENACTED", **0** of "30 July 2026", and the single hit for "15 July 2026" is in Module 6.1.1 about the EUR 11,170 / 11,550 allowance, not the work bonus. The fiscal work bonus sits in Module **7.1**, not 6.3. A residual wording gap does exist and is ISSUE-9. |

---

## 1. Executive summary

Belgium's **statutory content is strong** and its **traceability discipline is unusually good**: a 63-row `legal-basis-register.csv` exists (contradicting the assumption that BE predates the register), 33 rows at tier A.1 and 27 at A.2, `consumed_by` populated on all 63, and a documented rejection row (`BE-PIT-006`, EUR 11,180, tier B, "REGISTERED SO THAT IT CAN BE REJECTED") showing the L4/F18 superseded-figure trap was met and beaten.

What is wrong is **propagation**, in exactly the shape the failure log predicts (F27). On **18 Aug 08:35** `02-wtc/_apply_l13_bik.py` appended three benefit-in-kind wage types — `BE-056`, `BE-057`, `BE-058` — to the Wage Type Catalogue. The catalogue went from 355 rows to **358** and from 55 Belgian additions to **58**. **Nine downstream cells across three artifacts were never re-synced**, and the WTC's own internal coverage audit still certifies a catalogue that no longer exists. That is CRITICAL, and it is one script run away from being closed.

The second real problem is **buildability, not accuracy** (G-BUILD, F25). Four of the nine report specs cite the Data Dictionary the right way — `BE-DD-001-v1.1 — 'Field Name' (Country Fields)` — and 318 of 318 such citations resolve. The other five state DD provenance as a **prose category** ("Employee master data — INSZ.") that a developer cannot mechanically reconcile. Counting honestly, DD-bucket alignment across all nine specs is **318 of 544 = 58.5%**, not the ~100% a single-spec sample suggests.

| # | Check | Verdict | Headline number |
|---|---|---|---|
| 1 | CCG ↔ WTC | **PASS with 1 MAJOR** | 60 of 61 CCG M3–9 components exist in the WTC = **98.4%** |
| 2 | CCG ↔ DD | **PASS** | Module 2 delegates to the DD by design; every named field resolves |
| 3 | CCG ↔ Report Specs | **PASS** | 9 payroll-scope reports → 9 spec files; 10 exclusions all carry a descoping decision |
| 4 | DD ↔ Report Specs (4-bucket) | **FAIL (MAJOR)** | **318 of 544 DD-bucket rows = 58.5%**; 226 rows unresolvable |
| 5 | Global WTC coverage | **FAIL (CRITICAL)** | 300 of 300 included = **100% coverage**, but the audit sheet is stale by 3 codes and 299 of 300 baseline descriptions are silently renamed |
| 6 | Scope discipline | **PASS** | 0 violations in either direction, verified mechanically |
| 7 | Report Spec format (×9) | **PASS with 1 MAJOR, 1 MINOR** | 9/9 sheets, 21/21 columns, `FF4472C4` header on 9/9; **3 miscoloured scope cells** |
| 8 | v2.4 standards | **PASS with 1 MAJOR** | CCG 13/13 modules exact; DD/WTC/PSL contracts all met; **Report Matrix version 1.0 vs Version Control 1.2 on 8 specs** |
| 9 | Composite key / inter-field | **PASS with 2 MINOR** | C13 47 rows; C16 **503/503**; C17 present but a 2-row stub; C20 complete |

---

## 2. Per-check results with evidence

### CHECK 1 — CCG ↔ WTC alignment · **PASS with 1 MAJOR**

**Method.** Harvested every component row from the five CCG tables in Modules 3–9 that carry a tax/SS treatment verdict: M4.2 `Component | Social security | Income tax | Note` (16×4), M4.6 `Pay component | Wage Protection Act | NSSO wage | Taxable` (19×5), M7.2 `Benefit | Employee tax | Employer levy` (8×3), M8.1 `Wage type | Effect of an unpaid day` (11×2), M9.1 `Payment | Trigger | Social security | Income tax` (12×4). 61 component rows. Each was then resolved against the 358 rows of `BE-WTC-001-v1.0.xlsx!'Wage Type Catalogue'` by direct keyword search — an automated fuzzy match was run first, produced 18 false negatives (it mapped "Single holiday pay" to "Public holiday pay"), and was **discarded**; every one of the 18 was then checked by hand.

**Score: 60 of 61 = 98.4% matched.**

Hand-resolved examples, all confirmed present with the treatment the CCG states:

- CCG M4.2 "Company car (private use)" → WTC `62500` Company car benefit in kind, SS=No / TAX=Yes, plus `23672` Employer CO2 solidarity contribution. CCG M7.2 says "Included in the car benefit / Included in the CO2 contribution" — matches.
- CCG M7.2 "Free meals" → WTC `BE-056`, SS=Yes / TAX=Yes.
- CCG M7.2 "personal use of a PC or internet" → WTC `BE-057`, SS=Yes / TAX=Yes.
- CCG M7.2 "Free housing, free heating and electricity" → WTC `62400`/`62440`/`62480`, SS=Yes / TAX=Yes.
- CCG M4.6 "Meal vouchers, conditions met" → WTC `62660` face value SS=No/TAX=No, with `BE-011` (employee part min EUR 1.09) and `BE-012` (employer part max EUR 8.91).
- CCG M9.1 "Salary for the notice period worked / Ordinary / Ordinary scale" → carried by basic salary `62100`. Correctly **not** a separate wage type.
- CCG M9.1 "Dismissal compensation allowance (ontslagcompensatievergoeding)" → correctly **absent** from the WTC: the CCG's own Social-security column says "Paid by the National Employment Office, not by the employer", so payroll never pays it. This is F21 handled correctly, not a gap.

**The one genuine miss — ISSUE-4 (MAJOR).** CCG Module 4.2 carries two rows, "Genuine expenses proper to the employer" (`Not subject | Not taxable | Must be justified`) and "Reimbursement of expenses proper to the employer", and CCG Module 4.6 carries "Genuine expense reimbursement" (`No | No | No | Not applicable`). The WTC has **no general-purpose earning wage type** for it. The only three related rows are `62310` "Inbound taxpayer — exempt reimbursement of employer own costs (up to 35%)" (restricted to the inbound-taxpayer regime), `21149` "Requalification — unjustified flat-rate expense allowance" (a Deduction) and `21800` "Recovery — expense advance not justified". An ordinary employee's justified expense reimbursement therefore cannot be paid, and `21149` has nothing to requalify from.

### CHECK 2 — CCG ↔ DD alignment · **PASS**

`BE-CCG-001-v1.0.docx` Module 2 contains 8 tables. Its answer to "What employee fields are required for processing payroll and statutory reporting?" opens *"Grouped by the obligation that drives them (definitions in BE-DD-001)"* and then gives 7 bullet groups — Identification, Tax, Social security, Payment, Contract and remuneration, Leave and absence, Deductions. That is the correct treatment: a summary plus a pointer, not a reproduction of the DD (also satisfying Check 6c).

Every field concept named in those bullets resolves in `BE-DD-001-v1.1.xlsx`:

| CCG M2.2 bullet names | DD location |
|---|---|
| national register number (INSZ/NISS), BIS number | `ID Information!C5`, `!C6` |
| surname, first name, date of birth | `Country Fields!D163`, `!D164`, `!D165` |
| legal home address | `Country Fields!D166` Street · `!D167` House Number · `!D168` Belgian Postal Code · `!D169` Municipality · `!D170` Address Country · `!D171` Address Type |
| place of birth, gender, nationality | `Country Fields!D5`, `!D7`, `!D8` |
| tax residency, marital status, spouse income, dependants | `!D76`, `!D17`, `!D78`, `!D79`–`!D82`, `!D124`–`!D128` |
| NSSO worker code, joint committee, worker status | `!D22`, `ID Information!C28`, `!D23` |
| IBAN and BIC | `Country Fields!D129`, `!D130` |
| garnishment orders, creditor, balance | `!D133`, `!D134`, `!D141` |

The G-BUILD requirement that employee legal name and home address be present in the DD is **satisfied** — checked specifically because no global shared master-data file exists to inherit them from.

The only combo-table entry that did not resolve on a literal string match was "Working time regime", which is carried by `Country Fields!D179` Working Time Cycle, `!D33` Working Days System and `!D34` Mean Weekly Working Hours. Substantively resolved; wording differs.

DD structure measured against the toolkit contract: 8 sheets in the correct order, header row **4**, `ID Information` **A–V (22)**, `Country Fields` labels **B–W** with column A a spacer and the blue band to X, `Country Option Mappers` **B–F (5)**. Repeated mid-sheet header rows found and excluded from every count: `ID Information` row 16, `Country Fields` row 209, `Country Option Mappers` 15 of them (rows 8, 12, 16, 21, 25, 47, 51, 59, 67, 72, 75, 78, 88, 91, 94, …). True field counts: **26** in `ID Information`, **247** in `Country Fields` = **273** fields, **87** distinct option-mapper blocks. `validate_workbook.py --artifact DD` returns **PASS (blocker=0 major=0 minor=0)**.

### CHECK 3 — CCG Module 10 ↔ Report Specs · **PASS**

CCG Module 10.1's table `Report | Authority | Frequency | Format | Due date` (13×5) plus the outbound table in 10.2 give the payroll-scope report population. Every one maps to a delivered spec:

| CCG Module 10 report | Spec file | Doc ID |
|---|---|---|
| Dimona | `BE-NSSO-001-Dimona-Spec.xlsx` | BE-NSSO-001 |
| DmfA | `BE-NSSO-002-DmfA-Spec.xlsx` | BE-NSSO-002 |
| Corrective DmfA (M10.5 error-correction table) | `BE-NSSO-003-DmfAModification-Spec.xlsx` | BE-NSSO-003 |
| Electronic scenario declarations (ASR/DRS) | `BE-NSSO-004-DRS-Spec.xlsx` | BE-NSSO-004 |
| Limosa declaration | `BE-NSSO-005-Limosa-Spec.xlsx` (DESCOPED at v1.3) | BE-NSSO-005 |
| Wage withholding tax return (Finprof) | `BE-FIN-001-Finprof274-Spec.xlsx` | BE-FIN-001 |
| Form 281.10 (Belcotax-on-web) | `BE-FIN-002-Belcotax28110-Spec.xlsx` | BE-FIN-002 |
| Work accident declaration | `BE-FEDRIS-001-WorkAccident-Spec.xlsx` | BE-FEDRIS-001 |
| SEPA credit transfer for net pay | `BE-FEBELFIN-001-SEPACreditTransfer-Spec.xlsx` | BE-FEBELFIN-001 |

**Every report with no spec has a matching descoping decision** in `scope_manifest.json → authority_filings.out_of_scope` (10 entries) — checked one by one, which is where F15 and F21 usually bite:

- Form 325.10 → `BE-FIN-32510-005`, "Derived by FPS Finance from the 281.10 data". CCG M10.1 states it twice ("Yes — derived by FPS Finance from the 281.10", "Not a submission at all"). **F21 correctly avoided.**
- Social balance sheet → `BE-NBB-SOCBAL-011`, HR-scope. Also in CCG M10.1's own exclusion table (5×3) with "Requires headcount by qualification, training…". **F19 correctly avoided.**
- Work rules deposit → `BE-FPS-WORKRULES-016`, HR-scope.
- DB2P → `BE-SIG-DB2P-014`, "declared by the pension institution, not by the employer or the payroll engine". CCG M10.1 agrees: "Filed by the pension institution, not by payroll".
- Also descoped: diversity reporting, occupational-health reporting, form 281.20 (directors), single permit.

Two in-scope filings correctly have no report spec because their artifact is elsewhere: `BE-PAY-PAYSLIP-008` → the Payslip Generator; `BE-EMP-INDACC-007` (individual account, XLSX, annual) → recorded in scope with `product_mapping_required`, not silently dropped.

The Limosa case deserves note because it is the F24 shape. `BE-NSSO-005-Limosa-Spec.xlsx` exists as a full 9-sheet spec **while** `scope_manifest.json` descopes it as `BE-NSSO-LIMOSA-009` ("THE FILER IS A THIRD PARTY"). That is correct, not contradictory: `!'Report Matrix'!A1` reads "[DESCOPED - NOT A BUILD TARGET]", `!A2` is filled red `FFFFC7CE` with the reason, `!'Payroll Scope Summary'!A1` repeats "[DESCOPED - OUT OF SCOPE FOR HRBLIZZ]", and `BE-SIR-001-v1.0.docx` §2.2 carries the same determination — "`BE-NSSO-005-Limosa-Spec.xlsx` exists on disk but is DESCOPED — do not implement from it… It is retained, not deleted, because it documents a real obligation." The decision is worded consistently in all four places.

### CHECK 4 — DD ↔ Report Specs, 4-bucket method · **FAIL (MAJOR)**

**Method.** All nine core sheets read: **1,400 rows**, of which **209** are `═══` section markers and **1,191** are real field rows. Each row's column L (System Mapping) was classified DD / TX / CALC / SYS. TX/CALC/SYS rows were **not** penalised for absence from the DD, per the brief.

| Spec | rows | DD, cited | DD, category only | declared TX/CALC/SYS | TX | CALC | SYS | other |
|---|---|---|---|---|---|---|---|---|
| BE-FEBELFIN-001-SEPACreditTransfer | 26 | 0 | 7 | 0 | 1 | 2 | 9 | 7 |
| BE-FEDRIS-001-WorkAccident | 179 | **63** | 14 | 90 | 2 | 0 | 6 | 4 |
| BE-FIN-001-Finprof274 | 25 | 0 | 4 | 0 | 4 | 2 | 9 | 6 |
| BE-FIN-002-Belcotax28110 | 148 | 0 | 39 | 0 | 27 | 4 | 4 | 74 |
| BE-NSSO-001-Dimona | 77 | 0 | 41 | 0 | 17 | 0 | 4 | 15 |
| BE-NSSO-002-DmfA | 237 | **82** | 31 | 40 | 15 | 20 | 1 | 48 |
| BE-NSSO-003-DmfAModification | 237 | **82** | 31 | 40 | 15 | 20 | 1 | 48 |
| BE-NSSO-004-DRS | 235 | **91** | 32 | 50 | 13 | 0 | 12 | 37 |
| BE-NSSO-005-Limosa (descoped) | 27 | 0 | 27 | 0 | 0 | 0 | 0 | 0 |
| **TOTAL** | **1,191** | **318** | **226** | **220** | **94** | **48** | **46** | **239** |

**Resolvable DD citations: 318. All 318 resolve** — every `BE-DD-001-v1.1 — 'Field Name' (Sheet)` string was parsed and matched against the 273 real DD field names **and against the sheet named in the citation**. Zero wrong field names, zero wrong sheets. Independently, `BE-DD-001` appears 421 times across the nine workbooks (Version Control 32, core sheets 318, Field Options 70+1) and the DD's internal-code columns (`ID Information!D`, `Country Fields!E`) are correctly **empty on all 273 rows** — they are orange, dev-team columns — so a field-name citation is the only citation form available, and it is used correctly where it is used at all.

**Score: 318 of 544 DD-bucket rows = 58.5% alignment.** (Excluding the descoped Limosa spec: 318 of 517 = **61.5%**.)

The 226-row shortfall is ISSUE-2. Rows classified DD by their own wording but naming no DD field:
`BE-NSSO-001-Dimona` 41 · `BE-FIN-002-Belcotax28110` 39 · `BE-NSSO-004-DRS` 32 · `BE-NSSO-002-DmfA` 31 · `BE-NSSO-003-DmfAModification` 31 · `BE-NSSO-005-Limosa` 27 · `BE-FEDRIS-001-WorkAccident` 14 · `BE-FEBELFIN-001-SEPA` 7 · `BE-FIN-001-Finprof274` 4.

The contrast is visible on the same field name in two files:

| Spec | Row | Field | Column L |
|---|---|---|---|
| `BE-NSSO-002-DmfA-Spec.xlsx` | `'DmfA Spec'!L37` | Worker Street | `BE-DD-001-v1.1 — 'Street' (Country Fields).` ✅ resolves |
| `BE-NSSO-001-Dimona-Spec.xlsx` | `'Dimona Spec'!L28` | Worker Street | `Employee master data — street.` ❌ unresolvable |

The reverse direction (C27) is clean: no spec cites a DD field that does not exist, and the 117 rows whose column L reads "Not populated." are correctly out of scope (`E`=N, `N`="No" — e.g. `BE-FIN-002!'Belcotax 281.10 Spec'!A12` Regional Directorate, "No. Withdrawn.").

### CHECK 5 — Global WTC coverage audit · **FAIL (CRITICAL)**

`diff_wtc_baseline.py` against `shared/Global_WTC_V1_0.xlsx` (Sheet1, 300 data rows, 3 columns, no fills, no freeze pane):

```
BASELINE  Global_WTC_V1_0.xlsx  [Sheet1]  300 codes
COUNTRY   BE-WTC-001-v1.0.xlsx  [Wage Type Catalogue]  358 codes
  KEPT     300
  MISSING  0   (every baseline code is mandatory)
  RENAMED  299 (baseline description text is authoritative)
  ADDED    58  (country-specific — this is the allowed direction)
VERDICT   BASELINE VIOLATED     exit 1
```

**Reported coverage: 300 of 300 codes included = 100.0%. 0 excluded.** Applicability is expressed by configuring the row, never by deleting it — correct. Belgian additions: 58 (`BE-001` … `BE-058`, catalogue rows 302–359).

**ISSUE-1 (CRITICAL) — the coverage sheet certifies a catalogue that no longer exists.** Measured on the live file: 358 data rows, last row 359, 58 BE codes. The sheet says:

| Cell | Says | Should say |
|---|---|---|
| `'Global WTC Coverage'!B11` | `55` | `58` |
| `'Global WTC Coverage'!C11` | `302 - 356` | `302 - 359` |
| `'Global WTC Coverage'!B12` | `355` | `358` |
| `'Global WTC Coverage'!C12` | `2 - 356` | `2 - 359` |
| `'Global WTC Coverage'!D69` | `355` (last row of the BE additions list) | `359` |
| `'Global WTC Coverage'!A16:E70` | BE additions list **ends at BE-055 / row 356** | must extend to BE-058 / row 359 |

A search of the whole sheet for `BE-056`, `BE-057`, `BE-058` returns **NONE FOUND**. The three wage types are `BE-056` Benefit in kind — free meals, `BE-057` Benefit in kind — PC/tablet/internet/mobile, `BE-058` Benefit in kind — interest-free or low-interest employer loan (catalogue rows 357–359, all Category=Earning, all Tax Code 250). They were appended by `02-wtc/_apply_l13_bik.py` on **18 Aug 08:35** (backup `BE-WTC-001-v1.0.xlsx.bak-before-l13-bik`, 17 Aug 22:59); the coverage sheet was not recounted.

**ISSUE-3 (MAJOR) — 299 of 300 baseline descriptions silently renamed.** Codes are preserved exactly; descriptions are not. `Wage Type Catalogue!B2` = "Basic salary reduction - unpaid absence" against baseline "Basic salary deduction"; `!B3` = "Basic salary reduction - retroactive correction (current year)" against "Adjustment - Basic salary deduction"; `!B4` = "Recovery of salary advance (Wage Protection Act art. 23)" against "Advance - Basic salary deduction". The Belgian names are better, but toolkit hard rule 5 makes the baseline description authoritative, the rename is recorded nowhere, and `'Global WTC Coverage'!A72` "FULL BASELINE MAPPING — all 300 global codes" (rows 73–373, columns `Global Pay Element Code | Global description | Global type | Catalogue row | Belgium wage type name (English)`) preserves the mapping **but never states that a rename occurred**. A developer diffing on description finds 299 mismatches with no explanation.

### CHECK 6 — Scope discipline · **PASS**

- **No calculated amounts and no Base Salary in the DD.** All 273 field names were regex-screened for amount / gross / net / total / YTD / contribution / calculated / wage / salary / tax patterns; 16 candidates surfaced and every one was opened. All 16 are configuration attributes, not per-payrun values: `Country Fields!D44` Sectoral Wage Scale (a scale code), `!D77` Withholding Tax Scale, `!D132` Wage Payment Method, `!D212` Wage Withholding Tax Filing Frequency, `!D228` Payroll Pay Date, `ID Information!C25` Wage Withholding Tax Registration Number, etc. **No `Base Salary` field exists.**
  Two decimal-typed fields were inspected in full against the DD INCLUDE/EXCLUDE tree and **accepted**: `Country Fields!D145` "Departure Holiday Pay Settled by the Previous Employer" whose own description (`!G145`) reads *"loaded at implementation from the holiday certificate… It is a take-on"* — an externally supplied take-on value, not payroll output; and `!D128` "Dependant Own Net Resources", an employee-declared fiscal attribute tested against the Article 1409 thresholds. Both carry an explicit `F26 / YTD DECISION` audit note in column W (`W144`, `W145`, and also `W32`, `W139`, `W147`) recording the date and the pass that ruled on them. **F26 correctly handled and evidenced.**
- **No identification data in the WTC.** All 358 wage-type names screened for INSZ / national register / surname / first name / address / date of birth / IBAN / BIC / enterprise number. Seven apparent hits were all the substring "BIC" inside "bicycle" (`62510` company bicycle, `62530` bicycle allowance CBA no. 164, etc.). **True hits: zero.**
- **No full field specs in CCG Module 2 or Module 10.** Module 2.2 gives 7 bullet groups plus "definitions in BE-DD-001". Module 10.1 gives summary tables (`Report | Authority | Frequency | Format | Due date`) and points to the specs. Neither reproduces a field-level schema. This matches the v2.9 instruction at lines 609–611.

**0 violations in either direction.**

### CHECK 7 — Report Spec format compliance, all nine · **PASS with 1 MAJOR, 1 MINOR**

Measured on every file, not sampled:

| Requirement | Result |
|---|---|
| Exactly 9 sheets, correct names and order | **9/9 files PASS.** `Version Control · Report Matrix · Payroll Scope Summary · <Report> Spec · File Structure · Field Options · Population Rules · Example Analysis · Sample File` |
| Sheet 4 = 21 columns A–U with correct headers | **9/9 PASS.** All 21 labelled A–U, identical header text in all nine: `Field Name (EN) · Field Name (local) · Record Type · Field Position · Payroll Field (Y/N) · Mandatory (Y/N/C) · Conditional Reason · Position (Start-End) · Field Length · Format · Example · System Mapping · Field Explanation · Relevant for Payroll · Option Values · Rounding · Negative (Y/N) · Value Type · Reporting Frequency · Query to RA · RA Comments`. Columns V–Y exist in `max_column` but are **empty in all nine** (verified cell by cell) — no stray content. |
| Header row blue `FF4472C4`, white bold | **9/9 PASS.** `A1` fill `FF4472C4`, `bold=True`, font colour `FFFFFFFF`, **Google Sans 11pt** — the measured Spain-standard spec font. |
| Column M width | 62.0 on all nine (precedent measures 55.0 on `ES-M296-001`; a widened Field Explanation column, not a defect) |
| Freeze panes on the core sheet | `B2` on all nine — matches the measured precedent |
| Row colours applied | Present and correct: amber `FFFFEB9C` payroll, blue `FFBDD7EE` system, green `FFC6EFCE`, red `FFFFC7CE`, grey `FFD6DCE4` on `═══` rows, band `FFD9E2F3`. The convention is documented in every file at `'Version Control'!B22` ("ROW COLOUR CONVENTION (Sheet 4)"). |
| Payroll Scope Summary green/red | **8 of 9 PASS — see ISSUE-5.** Header band `FF1F4E78` (the correct navy; `1F4E79` appears nowhere). |
| Population Rules completed | **9/9 PASS.** 15–25 rows each: SEPA 20, WorkAccident 18, Finprof 18, Belcotax 25, Dimona 18, DmfA 20, DmfAMod 15, DRS 18, Limosa 15. |
| Zero error cells, full recalculation | **9/9 PASS.** No `#REF!` `#VALUE!` `#N/A` `#DIV/0!` `#NAME?` `#NULL!` `#NUM!` anywhere. |
| C25 no fabricated sample | 9/9 have a real `Sample File` sheet, 38–106 rows |

**ISSUE-5 (MAJOR).** `BE-NSSO-005-Limosa-Spec.xlsx!'Payroll Scope Summary'` — three cells answer **NO** but are filled green `FFC6EFCE` instead of red `FFFFC7CE`:

| Cell | Item | Answer | Fill | Expected |
|---|---|---|---|---|
| `B15` | Assignment and identity master data | NO | `FFC6EFCE` | `FFFFC7CE` |
| `B17` | Storing the Limosa-1 receipt | NO | `FFC6EFCE` | `FFFFC7CE` |
| `B18` | Tracking the A1 validity against the posting period | NO | `FFC6EFCE` | `FFFFC7CE` |

All three notes begin "**CHANGED AT v1.3 - previously YES**". The answer flipped at the v1.3 descope; the fill was never repainted. `B16` on the same block answers NO and *is* red, which proves the convention and isolates the defect. Colour is the fastest read of a scope summary, so three cells now say the opposite of their text. All 18 other scope rows in this file and all 180 across the other eight files are correctly coloured (0 mismatches).

**ISSUE-8 (MINOR).** `'Version Control'!C23` in eight files (`C25` in Limosa) contains the literal string `'NOT FOUND - requires direct inquiry to [authority]'`. It is a **meta-description of the gap convention**, not a live placeholder, and v2.9's three-tier C29 does not fail it. But the bracketed token trips any `\[\s*placeholder-class\s*\]` bracket lint, including the toolkit's. Reword to `NOT FOUND - requires direct inquiry to <the authority named in the row>`.

### CHECK 8 — v2.4 standards · **PASS with 1 MAJOR**

**CCG.** `BE-CCG-001-v1.0.docx` — 1,253 paragraphs, **47,934 words**, 148 tables, 1 section, portrait 8.5×11in. **212 headings: 14 H1 (Table of Contents + 13 modules), 39 H2, 159 H3.** All 13 module titles match `mercans_pipeline_v2_9.sh` lines 549–561 **character for character**: Foundational Jurisdictional Parameters · Master Data Configuration · The Gross-to-Net Calculation Framework · Gross Compensation · Social Security & Pension Systems · Income Tax Withholding System · Deductions, Exemptions & Benefits · Statutory Leave Management · Termination & Irregular Payments · Reporting, Compliance & Finalisation · Advanced Scenarios & Cross-Cutting Logic · Gross-to-Net Worked Examples · Common Business Practices & Non-Statutory Rules. H3-per-template-question format confirmed (e.g. "What is the statutory tax year?", "Can employers adopt an alternate tax year?…"). **C29 residual-marker scan: clean.** For context, the Bulgaria precedent has 14 H1 / 310 headings / 18,276 words / 3 tables — BE is 2.6× the words and 49× the tables, which is the "tables over prose" instruction actually followed.

**DD.** CZ V2.0 contract met in full (Check 2). **Blue-columns-only discipline: PASS** — every orange column (`ID Information` B, D, L–U; `Country Fields` C, E, M–V) is empty on all 273 data rows. The only non-empty orange cells are the repeated header rows `B16/D16/L16…` and `C209/E209/M209…`, which are the CZ template's own mid-sheet header repeats.

**WTC.** 6 sheets in the correct order: `Version Control · Wage Type Catalogue · Sick Leave Paid By Employer · Tax Credit · Global WTC Coverage · Form Reference Guide` — the CZ V2.0 4-sheet template plus the two pipeline additions. Sheet 3 is correctly named `Sick Leave Paid By Employer` (not "Employer Sick Pay"). `Wage Type Catalogue`: header row 1, **20 columns A–T**, Times New Roman 11pt, freeze `A2`, 358 true data rows out of `max_row` 1505. Global WTC baseline present (Check 5). Form Reference Guide present but a stub — ISSUE-7. `validate_workbook.py --artifact WTC` → **PASS (0/0/0)**.

**Report Specs.** Spain 9-sheet / 21-column standard met on all nine (Check 7).

**Payslip — the C21 divergence, recorded and resolved.** The brief says "5-sheet Mercans standard"; `PRESUBMISSION_AUDIT.md` C21 is titled *Payslip 5-Sheet Structure*; v2.9 (lines 63, 1738) and current doctrine require **8 sheets**. **Applied 8.** The file has exactly the 8 required sheets in the right order: `How to set up Payslip · Compliance Payslip · Belgium (EN) · Belgium (NL) · Payslip Spec · Field Option · Population Range · Unit Rate Details`. All three sheets that past builds deleted — *How to set up Payslip*, the language-neutral *Compliance Payslip* master, *Field Option* — are **present**. `validate_workbook.py --artifact PSL` → **PASS (0/0/0)**. Arial 6pt body, `FFDCDCDC` field labels, 2-decimal accounting mask `_(* #,##0.00_);…` (correct: EUR has 2 minor units, so C28 is satisfied), 62 formula cells on `Belgium (EN)`, logo image on 5 sheets. `Unit Rate Details` has 34 earning codes and **all 34 resolve to the WTC**; the `Rate Account` column being blank while `Unit Account` carries 63xxx **matches `REFERENCE_Payslip_Tunisia.xlsx!'Unit Rate Details'` exactly** (checked to avoid a false finding) and is not a defect.

**ISSUE-6 (MAJOR) — version inconsistency on 8 of 9 specs.** Each spec's `'Version Control'` table records **1.2 / 2026-08-16** as its current version (row 15; Limosa additionally has **1.3 / 2026-08-17 / Descoped** at row 16). But each spec's `'Report Matrix'` "Version" field still reads **1.0**:

| File | `'Version Control'` current | `'Report Matrix'` Version |
|---|---|---|
| BE-FEBELFIN-001 · BE-FEDRIS-001 · BE-FIN-001 · BE-FIN-002 · BE-NSSO-001 · BE-NSSO-002 · BE-NSSO-003 · BE-NSSO-004 | **1.2** | **1.0** ❌ |
| BE-NSSO-005-Limosa | 1.3 | 1.3 ✅ |

Also in this family: `BE-WTC-001-v1.0.xlsx!'Form Reference Guide'!E2` asserts the specs were "re-issued at v1.2 on 16 August 2026" — true for eight, stale for Limosa which moved to v1.3 and **Descoped** on 17 August. And all nine specs carry `Status = Draft` in their latest version-control row; no spec is marked Final.

### CHECK 9 — Composite key and inter-field constraints · **PASS with 2 MINOR**

**C13 — composite-key construction rules in Sheet 4 column M.** 47 rows across eight of nine specs carry a construction rule (composite / construction / check digit / modulo / concatenate / unique key): Dimona 12, DmfA 9, DmfAModification 9, Finprof 5, DRS 5, WorkAccident 3, SEPA 2, Limosa 2. Example of the depth achieved: `BE_Compliance_Payslip_Generator.xlsx!'Payslip Spec'!E16` — "Ten digits, first digit 0 or 1, last two a modulo-97 check on the preceding eight." `BE-FIN-002-Belcotax28110-Spec.xlsx` returns 0 — its identifiers are single-valued box codes, not composites. **PASS.**

**C16 — bidirectional documentation on conditional fields.** **503 rows across the nine specs carry Mandatory = C, and 503 of 503 carry a Conditional Reason in column G — 100.0%, zero gaps.** Per file: Belcotax 111, DmfA 110, DmfAModification 110, WorkAccident 64, DRS 46, Dimona 44, SEPA 10, Limosa 7, Finprof 1. (This supersedes the prior pass's "46/46", which was the DRS file alone.)

Bidirectional *resolution* was then tested by extracting every 5-digit zone reference out of column G and checking it exists in the same workbook: **124 references, 100 resolve, 24 apparent failures**. 22 of the 24 are `90xxx` **block** identifiers, not zones, and every one resolves to a `═══ BLOCK …` marker row (e.g. `BE-NSSO-002-DmfA-Spec.xlsx!'DmfA Spec'!A111` "BLOCK 90438 — SIMULTANEOUS WORK REORGANISATION MEASURES"; `BE-NSSO-001-Dimona-Spec.xlsx!A63` "BLOCK 90107 — USING EMPLOYER"). **Two are genuine — ISSUE-10 (MINOR):**

- `BE-FEDRIS-001-WorkAccident-Spec.xlsx!'Work Accident Spec'!G99` conditions on zone **00431** ("si la victime a changé de fonction au cours de l'année précédente"). Zone 00431 appears nowhere in the workbook. The concept exists in the DD as `Country Fields!D176` Function Changed Indicator, so the data is available — only the zone row is missing.
- `BE-NSSO-004-DRS-Spec.xlsx!'DRS Spec'!G85` conditions on zone **20072** ("si la déclaration DRS concerne une administration provinciale"). Zone 20072 appears nowhere; the spec is private-sector-only, so this rule can never fire and should be marked out of scope rather than left dangling.

**C17 — Form Reference Guide present in the WTC.** Present as sheet 6. **ISSUE-7 (MINOR/MAJOR boundary).** It is **2 rows** — a header (`Wage Type Name in English | Statutory form / report | Report Spec reference (row no.) | Data Dictionary field | Status`) and one blanket row that delegates rather than crosswalks: `A2` = "ALL 355 wage types … They are not repeated here", `C2` = "Maintained in column L (System Mapping) of sheet 4 of each of the nine report specifications … deliberately NOT duplicated on this sheet so that exactly one copy is authoritative. **OPEN ITEM: finding BE-X10-011** records that the 195 BE-WTC-001 references across those nine specifications name this catalogue in prose but do not yet resolve to a Mercans [code]". The single-authoritative-copy argument is sound. Two problems remain: (a) the sheet repeats the stale **355**; (b) it carries an unresolved **OPEN ITEM** inside a delivered artifact, and BE-X10-011 is understated — the same prose-not-citation defect affects **226** DD-bucket rows (ISSUE-2), not only the WTC references.

**C20 — scope decision audit trail.** Complete and unusually well kept. `scope_manifest.json`: `scope_version` 2.3, `scope_decided_by` Wallisson Gomes, `scope_decided_on` 2026-08-12, `scope_last_updated` 2026-08-18, `_revision_history` **14 entries**, `known_limitations` **17 entries**, `known_failure_patterns_to_check` **28 entries** (F1–F28 as objects, not a bare code list), `tier.by_domain` across 13 domains with a written rationale, `authority_filings` 8 in / 10 out each with a `descoping_reason`. Supported by `04-reports-spec/_work/SCOPE-DECISION.md` and a **116 KB** `PROPAGATION-LEDGER.md`. **PASS.**

**Scope-manifest re-validation against the real artifacts** (the "WTC exists" trigger — validating a JSON schema is not validating it against the artifact it describes):

- `option_mapper_scope` — the `_comment` says *"it locks 10 of the 87 live mapper blocks in BE-DD-001-v1.1"*. The **87 is exactly right** (measured: 87 distinct mapper blocks in `Country Fields`… `Country Option Mappers!B`). The **10 is wrong — the block contains 11 mappers**: `personal_id_type, insurance_type, contract_type, contract_duration_type, correction_codes, benefit_type, withholding_scale, worker_status, dmfa_remuneration_code, dmfa_service_code, joint_committee`. **ISSUE-11 (MINOR).** The manifest correctly records that the other 76 are unlocked and that absence is not a descoping decision (open finding BE-SCOPE-005).
- `wage_type_categories` — 32 in-scope / 7 out-of-scope / 11 special-rules narrative entries, all consistent with the WTC's contents; but the manifest twice repeats the stale **355** catalogue count (ISSUE-1's blast radius).

---

## 3. Source fidelity (run as a standing check, not one of the nine)

`00-official-sources/legal-basis-register.csv` — **63 rows**, 20 columns, `consumed_by` populated on **all 63** (zero blanks — this is the column that makes propagation a checklist rather than a guess). Tier distribution: **A.1 = 33, A.2 = 27, A.3 = 1, B = 2**.

The two tier-B rows were both opened:

- `BE-PIT-006`, status **superseded** — EUR 11,180, *"REGISTERED SO THAT IT CAN BE REJECTED. 4,785 × 2.3356 = 11,175.85 rounded to the nearest 10… it never [came into force]"*. `consumed_by` = SKILL only. This is the L4/F18 trap — a plausible, correct-looking, superseded figure — registered explicitly so it cannot be picked up. The live figure is EUR **11,170** (`BE-WTC-001!'Tax Credit'!B10`, CCG Module 6.1.1), re-derived from the A.1 coefficient 2.3356 and the reform's 4,945 step. **Handled correctly.**
- `BE-PIT-017`, status **active** — *"Normal annual gross remuneration = current monthly gross × 13.92… **THIS IS NOT A STATUTORY FIGURE.** Annex III nr. 53 prescribes no factor"*. **ISSUE-12 (MAJOR).** A Mercans convention with no statutory basis drives the exceptional-payment annualisation, and `consumed_by` names **eight** artifacts: CCG m04, m06, m08, m09, m12, WTC, PSL, SKILL. It is transparently labelled — which is the right thing to have done — but under C30 a live figure resting on tier B alone is a fail and needs an A.1/A.2 replacement or an explicit client-signed convention.

**ISSUE-13 (MAJOR) — the register was retrofitted.** **35 of 63 rows** carry `retrieved_on = "NOT AVAILABLE - RETROFIT"`, and 3 also carry `url = "NOT AVAILABLE - RETROFIT"` (`BE-PIT-001`, `BE-PIT-006`, `BE-PIT-017`, `BE-RPT-008`). `verified_on` is present and recent throughout (2026-08-13 → 2026-08-18) and `verification_method` is populated (`inspected directly`), so the figures were checked — but the retrieval leg of the chain of custody cannot be reconstructed for more than half the register. `BE-PIT-002` is the model of how it should read, including its own caveat: *"the annex text was extracted from the Securex reproduction of the decree, not from the Staatsblad edition itself; it was corroborated by an internal arithmetic proof of all three cumulative constants and by two independent houses."*

**Declared gap census — `NOT FOUND` cells, which must be named limitations rather than buried markers:** Limosa **174** (expected — no published technical spec exists for a web declaration), DRS 52, WorkAccident 48, DmfA 46, Finprof 44, Belcotax 43, DmfAModification 24, SEPA 23, Dimona 16, DD 37, WTC 4, Payslip 1. **Total 512.** Each is a sanctioned `NOT FOUND - requires direct inquiry to [authority]` per the documented convention, and the largest concentrations are honest (`BE-NSSO-002!'Field Options'!A8` and `!A16` state plainly that the Annexe 7 and Annexe 8 code sets are not reproduced). They are listed here so the count is visible to the dev team rather than discovered during build.

**C29 residual-marker lint, all artifacts:** CCG **clean**. DD, WTC, Payslip **clean** (0 hard markers). Nine specs: the `[authority]` convention string only (ISSUE-8). SIR: one hit — ISSUE-14.

**ISSUE-14 (MINOR).** `BE-SIR-001-v1.0.docx` paragraph 24 contains the word "placeholder": *"At that time BE-compliance/04-reports-spec/ was empty, and every outbound integration carried a placeholder in its Related Report Spec field rather than a guessed filename."* This is a historical narrative about a state that has since been resolved — the SIR now names all nine real spec files (`BE-FEBELFIN-001` ×6, the other eight ×1 each). v2.9's three-tier C29 does not fail bare "placeholder" in prose; the toolkit's `inspect_docx.py` lint does. Reword to "carried an explicit 'specification not yet built' note".

**Cross-artifact fact consistency (C32) — the stale-count sweep.** Every delivered `.xlsx`, `.docx` and `scope_manifest.json` was searched for the superseded catalogue counts. **9 genuine locations** (coincidental matches such as the CCG's "55,355.00" bracket boundary and Dimona's "00913-…" anomaly codes were excluded by inspection):

| # | Location | Says | Should say |
|---|---|---|---|
| 1 | `BE-WTC-001-v1.0.xlsx!'Global WTC Coverage'!B11` | 55 | 58 |
| 2 | `…!'Global WTC Coverage'!C11` | 302 - 356 | 302 - 359 |
| 3 | `…!'Global WTC Coverage'!B12` | 355 | 358 |
| 4 | `…!'Global WTC Coverage'!C12` | 2 - 356 | 2 - 359 |
| 5 | `…!'Global WTC Coverage'!D69` | 355 | 359 |
| 6 | `…!'Form Reference Guide'!A2` | ALL 355 wage types | ALL 358 wage types |
| 7 | `…!'Form Reference Guide'!B2` | 24 distinct box codes across the 355 rows | 23 box codes + NA, across 358 rows |
| 8 | `BE-FIN-002-Belcotax28110-Spec.xlsx!'Belcotax 281.10 Spec'!N47` | 144 of its 355 wage types | 147 of its 358 |
| 9 | `scope_manifest.json` | "144 of the 355 rows carry it" | 147 of 358 |

The 144 → **147** correction is a second-order consequence of the same event: `BE-056`, `BE-057` and `BE-058` all carry Tax Code **250**, so the measured count of tax-code-250 rows is now **147**, not 144. The same stale 144 also appears at `BE-FIN-002!'Belcotax 281.10 Spec'!L38`, `!'Field Options'!E56`, `!'Population Rules'!D14` and `!'Example Analysis'!D18`. Distinct tax codes measured: **24 values, of which one is `NA`** → 23 real box codes, so the "24 distinct box codes" claim is off by one.

---

## 4. Issues list

| ID | Sev | Check | Location | Problem | Fix |
|---|---|---|---|---|---|
| **ISSUE-1** | **CRITICAL** | 5 | `02-wtc/BE-WTC-001-v1.0.xlsx!'Global WTC Coverage'!B11, C11, B12, C12, D69` and the BE-additions list `A16:E70` | The WTC's own coverage audit certifies 55 BE additions / 355 total rows / range 2–356. The live catalogue has **58 / 358 / 2–359**. `BE-056`, `BE-057`, `BE-058` (catalogue rows 357–359, added 18 Aug 08:35 by `_apply_l13_bik.py`) appear **nowhere** on the sheet. An audit artifact that certifies a superseded state is worse than none. | Re-run the coverage generator: `B11`=58, `C11`="302 - 359", `B12`=358, `C12`="2 - 359", append `BE-056`/`BE-057`/`BE-058` rows to `A16:E70` with their catalogue rows 357/358/359 and their "no global equivalent" reasons. Then propagate to locations 6–9 of the C32 table. |
| **ISSUE-2** | **MAJOR** | 4 | `BE-NSSO-001-Dimona`(41), `BE-FIN-002-Belcotax28110`(39), `BE-NSSO-004-DRS`(32), `BE-NSSO-002-DmfA`(31), `BE-NSSO-003-DmfAModification`(31), `BE-NSSO-005-Limosa`(27), `BE-FEDRIS-001-WorkAccident`(14), `BE-FEBELFIN-001-SEPA`(7), `BE-FIN-001-Finprof274`(4) — sheet 4, column L | 226 DD-bucket rows state DD provenance as a prose category ("Employee master data — street.") with no resolvable field name. Alignment is **318 of 544 = 58.5%**, not the ~100% a single-spec sample implies. Five of nine specs carry **zero** core-sheet DD citations. | Rewrite those 226 cells in the form already used correctly 318 times: `BE-DD-001-v1.1 — 'Street' (Country Fields).` The DD fields exist — `BE-NSSO-002!L37` proves it for the very same field that `BE-NSSO-001!L28` leaves in prose. Then update BE-X10-011 to the real 226-row size. |
| **ISSUE-3** | **MAJOR** | 5 | `BE-WTC-001-v1.0.xlsx!'Wage Type Catalogue'!B2:B301` | 299 of 300 Global WTC baseline descriptions are replaced by Belgium-specific names with no record of the rename. Codes and the `A72` baseline mapping survive, so nothing is lost — but toolkit hard rule 5 makes the baseline text authoritative and a description-based diff shows 299 unexplained mismatches. | Either restore the baseline text and carry the Belgian name in a separate column, or add an explicit note at `'Global WTC Coverage'!A2` recording that 299 of 300 descriptions are deliberately localised and that `A72:E373` is the authoritative crosswalk. |
| **ISSUE-4** | **MAJOR** | 1 | `BE-WTC-001-v1.0.xlsx!'Wage Type Catalogue'` — **no such row exists**; required by `BE-CCG-001-v1.0.docx` Module 4.2 rows "Genuine expenses proper to the employer" / "Reimbursement of expenses proper to the employer" and Module 4.6 row "Genuine expense reimbursement" | No general-purpose earning wage type for a justified expense reimbursement. Only `62310` (inbound-taxpayer regime only), `21149` (requalification, a Deduction) and `21800` (recovery). Payroll cannot pay an ordinary employee's expense reimbursement, and `21149` has nothing to requalify from. | Add `BE-059` "Expense reimbursement — costs proper to the employer (justified)", Category Earning, Subject to Tax = No, Subject to Social Insurance = No, Tax Code NA, paired with `21149`, citing the Wage Protection Act / NSSO expense-allowance rules. Then re-sync the counts in ISSUE-1. |
| **ISSUE-5** | **MAJOR** | 7 | `BE-NSSO-005-Limosa-Spec.xlsx!'Payroll Scope Summary'!B15, B17, B18` | Three cells answer **NO** but are filled green `FFC6EFCE`. All three read "CHANGED AT v1.3 - previously YES" — the answer flipped at the descope, the fill did not. `B16` answers NO and is correctly red, proving the convention. | Repaint `B15`, `B17`, `B18` (and their A:C row bands) to `FFFFC7CE`. Add a build-time assertion: answer NO ⇒ fill `FFFFC7CE`, YES ⇒ `FFC6EFCE`, PARTIAL ⇒ `FFFFEB9C`. |
| **ISSUE-6** | **MAJOR** | 8 | `'Report Matrix'` "Version" row in `BE-FEBELFIN-001`, `BE-FEDRIS-001`, `BE-FIN-001`, `BE-FIN-002`, `BE-NSSO-001`, `BE-NSSO-002`, `BE-NSSO-003`, `BE-NSSO-004`; plus `BE-WTC-001!'Form Reference Guide'!E2` | Eight specs advertise Version **1.0** on the Report Matrix while their own `'Version Control'!B15` records **1.2 / 2026-08-16`. The WTC asserts all nine are "v1.2", stale for Limosa which is at 1.3 **and Descoped**. All nine still carry `Status = Draft`. | Set the Report Matrix Version to 1.2 on the eight; correct `Form Reference Guide!E2` to "eight at v1.2, BE-NSSO-005 at v1.3 (DESCOPED)"; promote Status to Final on acceptance, or state in the handover that all nine ship as Draft. |
| **ISSUE-7** | **MAJOR** | 9 (C17) | `BE-WTC-001-v1.0.xlsx!'Form Reference Guide'!A2:E2` | The C17 cross-reference table is a **2-row stub**: one header, one blanket row. It repeats the stale "355", and `C2` carries an unresolved **OPEN ITEM (BE-X10-011)** inside a delivered artifact rather than as a named limitation in the QA report. | Keep the single-authoritative-copy design but make the sheet a real index: one row per statutory form (9 rows), each naming the spec file, the tax codes that feed it and the DD sheet, with the 355 → 358 correction. Move BE-X10-011 out of the artifact into `handover_status.md` and restate it at its true size (226 rows, ISSUE-2). |
| **ISSUE-8** | MINOR | 7 | `'Version Control'!C23` in eight specs, `!C25` in `BE-NSSO-005-Limosa` | The literal `[authority]` in the gap-convention description trips a bracket-placeholder lint. Not a live placeholder; v2.9's C29 does not fail it. | Reword to `NOT FOUND - requires direct inquiry to <the authority named in the row>`. |
| **ISSUE-9** | MINOR | — | `BE-WTC-001-v1.0.xlsx!'Tax Credit'!B5` vs `BE-CCG-001-v1.0.docx` Module 7.1 | Not the contradiction the prior pass alleged — both say the reform is unenacted. But the CCG states **both readings** ("income year 2026 is assessment year 2027, so the 63% figure — not 52.54% — is the one that governs this guide's income year **if the measure is enacted**… Both readings are stated because the enactment is unconfirmed"), while `B5` gives only the configure-52.54% side. A developer reading only the WTC will not know 63% could become the governing figure for AY2027. | Append the CCG's dual-reading sentence to `'Tax Credit'!B5`, in the CCG's own words, and register a watch item on the enactment. |
| **ISSUE-10** | MINOR | 9 (C16) | `BE-FEDRIS-001-WorkAccident-Spec.xlsx!'Work Accident Spec'!G99` (zone **00431**); `BE-NSSO-004-DRS-Spec.xlsx!'DRS Spec'!G85` (zone **20072**) | Two conditional rules key off zones that appear nowhere in their workbook, so the condition cannot be evaluated. (The other 22 apparent failures are `90xxx` block ids and all resolve to `═══ BLOCK` rows — not defects.) | Add a row for zone 00431 (the DD already has the data at `Country Fields!D176` Function Changed Indicator); mark zone 20072 explicitly out of scope — the spec is private-sector-only, so the rule can never fire. |
| **ISSUE-11** | MINOR | 9 (C20) | `scope_manifest.json → option_mapper_scope._comment` | Says it "locks 10 of the 87 live mapper blocks". The 87 is correct (measured). The block contains **11** mappers. | Change 10 → 11, or drop the count and let the keys speak. |
| **ISSUE-12** | MAJOR | P2/C30 | `legal-basis-register.csv` row `BE-PIT-017`; consumed by CCG m04/m06/m08/m09/m12, WTC, PSL, SKILL | The 13.92 annualisation factor for the exceptional-payment tables is **tier B and a Mercans convention** — the row itself says "THIS IS NOT A STATUTORY FIGURE. Annex III nr. 53 prescribes no factor". Live across eight artifacts. Honestly labelled, but C30 fails a live figure resting on tier B alone. | Route to `compliance-source-hunter` for an A.1/A.2 basis, or obtain client sign-off and re-label the row as an agreed convention rather than a register figure. Do not silently keep it at tier B. |
| **ISSUE-13** | MAJOR | P2 | `legal-basis-register.csv` — 35 of 63 rows | `retrieved_on = "NOT AVAILABLE - RETROFIT"`; four rows also have `url = "NOT AVAILABLE - RETROFIT"` (`BE-PIT-001`, `BE-PIT-006`, `BE-PIT-017`, `BE-RPT-008`). The register was built after the artifacts, so the retrieval leg of the chain of custody cannot be reconstructed for over half of it. `verified_on` and `verification_method` are populated throughout. | Backfill `retrieved_on` and `url` where the local file or browser history still shows it; where it cannot be recovered, keep the RETROFIT marker and name it as a limitation in `handover_status.md`. Register-first ordering on the next country. |
| **ISSUE-14** | MINOR | C29 | `BE-SIR-001-v1.0.docx` paragraph 24 | Contains "placeholder" in a historical narrative about a state now resolved (the SIR names all nine real spec files). Not failed by v2.9's tiered C29; failed by the toolkit's docx lint. | Reword to "carried an explicit 'specification not yet built' note". |

**Totals: 1 CRITICAL · 6 MAJOR · 7 MINOR.**

---

## 5. Manual review items (documented but not automated — control L3)

Verified by grepping `mercans_pipeline_v2_9.sh` with a word-boundary pattern before claiming anything ran. Deterministic Stage 9 blocks present: **C1, C8, C11, C12, C20, C21, C22, C23, C24, C25, C26, C27, C28, C29, C30, C31, C32, C33**. **C5, C6, C7 appear nowhere in the script.** C2, C3, C4, C9, C10 and C13–C19 exist only as prompt text inside earlier stage prompts — instructions to a builder, not audit blocks. Consequently:

1. **C5 (classification cites the establishing article)** — no automation anywhere. Run by hand: **PASS**. The 63-row register is the mechanism; every CCG classification traced back to a register row, and `consumed_by` is populated on all 63 so the reverse lookup works too.
2. **C6 (file format verified against the source PDF)** — no automation. Run by hand: **PASS with a named risk**. `BE-FIN-002-Belcotax28110-Spec.xlsx!'Version Control'!C27` declares "SOURCE IS THE INCOME YEAR 2025 EDITION"; `BE-FIN-001-Finprof274-Spec.xlsx!C25` flags "A MISLABELLED SOURCE FILE — DO NOT USE IT FOR…". Both self-disclosures are correct and must reach the dev team.
3. **C7 (population-rules depth on conditional fields)** — no automation. Run by hand: **PASS**. 503 of 503 conditional rows carry a Conditional Reason, and all nine Population Rules sheets are populated (15–25 rows).
4. **C9 (WTC tax codes against the country's own legend)** — prompt text only; **nothing runs it but this audit**. Run by hand: **PASS**. All 24 distinct Tax Code values in `BE-WTC-001` are Belgian Belcotax 281.10 box codes (250, 252, 254, 233, 234, 242, 285, 305, 308, 317, 335 …) or `NA`. **No code borrowed from another country's legend.** Note the count precision issue at ISSUE-1 location 7.
5. **C14 (option mapper completeness)** — prompt text only. Run by hand: **one finding.** `BE-NSSO-003-DmfAModification-Spec.xlsx!'Field Options'` lists **Attestation Status twice with different value sets**: `A6:C11` gives 0, 1, 3, 4 + NOT FOUND, and `A16:C26` gives 0–8 + NOT FOUND for the same zone 00110. One authoritative list is needed. The sheet's delegation of all other code tables to `BE-NSSO-002` (rows 13 and 28, "See BE-NSSO-002") is **deliberate and correctly labelled** — checked before firing, and it is not the silent truncation it first looks like. The two core sheets are 87.4% identical cell-for-cell, and the 713 differing cells are real (record-type labels "— modification", per-correction frequency in column S, modification-specific explanations in column M), so this is not a clone defect.
6. **C21 divergence** — `PRESUBMISSION_AUDIT.md` says 5-sheet payslip; v2.9 (lines 63, 1738) and current doctrine say 8. **Applied 8.** The file has all 8, including the three that past builds deleted.
7. **L2 note** — the v2.9 script's own header banner under-reports its version relative to its body (the body implements C1–C33 and references v2.10 behaviour). Grepped the body, never the banner.

---

## 6. Readiness verdict

**NOT READY FOR DEVELOPMENT HANDOVER.**

| Artifact | Honest accuracy | Justification |
|---|---|---|
| CCG `BE-CCG-001-v1.0.docx` | **90–93%** | Official-source + research band. 13/13 modules, 159 H3 template answers, 148 tables, 47,934 words, C29 clean, backed by a 63-row register at 60/63 tier A. Held below 95% by ISSUE-4 (missing expense wage type surfaced from Module 4.2/4.6) and ISSUE-9 (dual-reading not mirrored downstream). |
| WTC `BE-WTC-001-v1.0.xlsx` | **80–85%** | Content is excellent — 358 wage types, 300/300 baseline codes kept, 24 real Belgian box codes, no borrowed legend. The **internal audit sheet is wrong** (ISSUE-1 CRITICAL), 299 descriptions are silently renamed (ISSUE-3) and C17 is a stub (ISSUE-7). Cannot be scored above the low 80s while its own coverage certificate is false. |
| DD `BE-DD-001-v1.1.xlsx` | **92–95%** | The strongest artifact. 8/8 sheets, header row 4, exact A–V / B–W / B–F column contracts, 273 fields, 87 mapper blocks, blue/orange discipline perfect, F26 decisions dated and reasoned in column W, `validate_workbook.py` PASS, and 318/318 inbound citations resolve. |
| Report Specs ×9 | **80–85%** | Official template + XSD/glossary + research would justify 90–95%; held down by ISSUE-2 (58.5% DD alignment), ISSUE-5 (3 miscoloured scope cells), ISSUE-6 (version mismatch on 8 of 9), 512 declared `NOT FOUND` gaps, and all nine still at `Status = Draft`. Structure itself is flawless: 9/9 sheets, 21/21 columns, `FF4472C4` headers, 503/503 conditional reasons. |
| SIR `BE-SIR-001-v1.0.docx` | **90–93%** | 19 IN + 19 OUT flows, 69 headings, 50 tables, 19,188 words; Limosa descope propagated correctly to OUT-08/IN-17 with the arithmetic shown ("10 live + 1 descoped + 8 none"); all nine spec filenames now resolved. One cosmetic C29 hit (ISSUE-14). **F27 met for the change that was made.** |
| Payslip `BE_Compliance_Payslip_Generator.xlsx` | **88–92%** | All 8 required sheets including the three usually deleted; 34/34 Unit Rate earning codes resolve to the WTC; `Rate Account` blank matches the Tunisia precedent exactly; correct 2-decimal EUR accounting mask; `validate_workbook.py` PASS. Held below 95% because DD provenance sits in prose in column E (19 mentions, 0 parseable field-name citations) rather than as resolvable citations. |
| `scope_manifest.json` | **90–93%** | 14 revisions, 17 named limitations, F1–F28 as structured objects, tier rationale across 13 domains, 8 in / 10 out filings each with a reason. Docked for the 10-vs-11 mapper count (ISSUE-11) and the stale 355 references. |

**What must close before handover**

1. **ISSUE-1 (CRITICAL)** — re-run the WTC coverage generator and propagate all nine stale-count locations. One script run.
2. **ISSUE-2, 3, 4, 5, 6, 7 (MAJOR ×6)** — ISSUE-5 and ISSUE-6 are minutes of work. ISSUE-2 is the substantial one: 226 cells to rewrite into a form the same workbooks already use correctly 318 times.
3. **ISSUE-12, 13 (MAJOR, source-side)** — route `BE-PIT-017` to `compliance-source-hunter`; decide whether the 35 RETROFIT `retrieved_on` values are backfilled or named as a limitation.

**Named limitations to carry into `handover_status.md` regardless** (G-CLEAN — these belong here, not as markers inside the artifacts):

- **512 `NOT FOUND` cells** across the delivered artifacts, concentrated in Limosa (174, descoped — no published technical specification exists for a web declaration), DRS (52), WorkAccident (48), DmfA (46), Finprof (44), Belcotax (43).
- **NSSO Annexe 7 (remuneration codes, zone 00067) and Annexe 8 (service codes, zone 00062)** — code sets not reproduced; declared at `BE-NSSO-002!'Field Options'!A8` and `!A16`. Closed by obtaining the annexes from the NSSO.
- **NSSO Annexe 12** — not held for the DRS ZIMA scenario (`BE-NSSO-004!'Field Options'!E3`). Zone 00430 **is** fully specified for the work-accident scenario.
- **Belcotax source is the income year 2025 edition** (`BE-FIN-002!'Version Control'!C27`); **a mislabelled Finprof source file** must not be used for format (`BE-FIN-001!C25`).
- **Fiscal work bonus reform unenacted** — both readings (52.54% / 63%) live; watch item.
- **BE-SCOPE-005** — 76 of 87 DD option-mapper blocks are unlocked, and absence from `option_mapper_scope` is not a descoping decision.
- **All nine Report Specs ship at `Status = Draft`.**
- **35 of 63 register rows have no recoverable `retrieved_on`.**

**Closing note on method.** Two candidate findings were killed by opening the precedent instead of trusting prose, which is the whole of control L1. The payslip's empty `Rate Account` column looked like a MAJOR gap until `REFERENCE_Payslip_Tunisia.xlsx!'Unit Rate Details'` showed the identical pattern. `BE-NSSO-003`'s 28-row Field Options sheet looked like F16 silent truncation until rows 13 and 28 showed an explicit, labelled delegation to `BE-NSSO-002`. Three of the prior pass's five "new gaps" were also wrong in the direction that matters — they alleged defects that do not exist (the fiscal-work-bonus contradiction, the DRS zone 00625/00096 propagation failure) while the real propagation failure sat three files away in the WTC's own coverage sheet.
