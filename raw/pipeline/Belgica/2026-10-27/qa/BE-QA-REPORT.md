# BE-QA-REPORT — Belgium payroll-compliance dossier

**Stage 10 — final cross-artifact check and run closure**
**Reviewer:** `compliance-qa-auditor` (independent — built none of the seven artifacts)
**Date:** 2026-08-17 · **Mode:** `report_only` — nothing in any artifact was edited by this pass
**Machine-readable:** `_qa/REGRESSION-BE-XCHECK-r1.json` · **Evidence scripts:** `_qa/x10/`

---

## 0. What this pass is, and what it is not

Every one of the seven BE artifacts was individually regression-audited between 15 and 17 August
and had a fix round applied. This pass is **not** a re-audit of any one of them. It compares all
seven against each other and against `scope_manifest.json` v1.1 **simultaneously**, which is the
only way the findings below become visible.

Two consequences, stated up front because they set the tone of everything that follows:

1. **The fixes worked, with one exception I had to go back and check.** Of the 22 blockers raised
   across the seven sweeps, **17 are closed and I verified each one against the artifact on disk,
   not against a log.** Two are partially closed. **One — `BE-CCG-003`, the tier-B CO2 multiplier —
   was not touched by the 17 August round at all**, and I only established that by re-reading the
   cell rather than trusting the premise that every blocker had been fixed. It is `BE-X10-022`
   below. Of the six blockers now open, four are cross-artifact by nature and could not have been
   closed by any single-artifact fix.
2. **The characteristic residual defect in Belgium is a fix applied in one direction and
   certified as complete.** Four separate findings below have that identical shape. It is the one
   genuinely new failure pattern this run produced, and it is appended as **F29**.

**Verdict: the country is NOT closed.** Six blockers and eleven majors are open. Reported as it
is, per the standing rule that a country is never reported closed while a G-gate is failing.

---

## 1. Tier classification — the honest answer

**There is no tier verdict in Belgium to repeat, in the CCG, in `scope_manifest.json`, or
anywhere else.**

Section 7.1 requires this report to "repeat the tier verdict in the same words used in the CCG
Foundational module and scope manifest". I looked for it and it does not exist:

| Where a tier verdict should be | Present? |
|---|---|
| `_pipeline/build-manifest.json → tier` | **Directory does not exist** |
| `scope_manifest.json` — any `tier` / `complexity` / `T1–T4` key | **Zero occurrences** |
| `01-ccg/BE-CCG-001-v1.0.docx` Foundational module | **Zero occurrences** |
| `BE-COVERAGE.md` | **Zero occurrences** |

BE predates the tier convention, which arrives with `compliance-scaffolder`. **I have not invented
one.** On the employer-operation discriminator the evidence on disk would support T4 for the
statutory-reporting domain (19 outbound and 19 inbound integrations, nine authority filings in
scope, a 498-code error model, three language regions with nullity as the sanction) — but that is
my inference, it is not the project's recorded decision, and it must not be quoted as one.

**What would close it:** a `_pipeline/build-manifest.json` written for BE with a per-domain tier
and its reasoning, and the identical wording placed in the CCG Foundational module and the scope
manifest. Until then every downstream consumer is guessing at Belgium's complexity class.

---

## 2. Per-artifact accuracy — band, justification, and what caps it

Bands are taken from the evidence actually on disk, per the §7.1 rule: official template/XSD +
research → 90–95%; research only → 75–85%; official source + portal verification + real sample →
95–100%. **No figure here is rounded up.**

### 2.1 SIR — `03-statutory-integrations/BE-SIR-001-v1.0.docx` — **93%**

**The best artifact in Belgium, and the only one where P2 was runnable as specified.**

Justification for the band: `00-official-sources/spec-sources/` holds **42 files, 15 of them
authority PDFs** — the NSSO SFTP manual v14, Annexe 30, both DmfA glossaries at 2026/2, the FPS
Finance FinProf XML file description, both Belcotax brochures, the Febelfin pain.001.001.09
guidelines. Every technical claim I re-derived from those primary sources reproduced exactly: 498
anomaly codes over range 001–536; 213 DmfA zones in 32 blocks; 1,344 severity-B and 148 severity-P
pairs; 57 Dimona zones in 16 blocks. That is official-source-plus-real-sample territory. It is not
95%+ because there is no portal round-trip and no accepted filing: **no declaration has ever been
submitted through any of these channels.**

Verified closed by this pass: all five of its blockers. Nineteen inbound and nineteen outbound
flows registered (IN-01…IN-19, OUT-01…OUT-19); **zero** `PENDING` cells remain, against 22 before;
all nine Report Spec filenames named in §2.3 resolve to a file on disk; the 498-code count is
correct in the document *and* in `s05_errors.md` and `selfcheck_be_sir.py`, so a rebuild no longer
regresses it; and the FinProf period codes now read `1011` advance on the fourth quarter, `1012`
fourth quarter, with `1215` correctly assigned to the 15–24 December declaration.

Caps the band: the 27-entry gap register (G1–G27) is the best gap discipline in the country and it
is still **local to this document** — none of its 27 entries reached
`scope_manifest.json → known_limitations` (see §4, BE-X10-004's sibling defect).

### 2.2 CCG — `01-ccg/BE-CCG-001-v1.0.docx` — **86%**

**The most reviewed artifact, and the numbers are right.** I re-derived the entire social work
bonus parameter set independently rather than accepting it:

- **All ten dated parameter rows reconcile.** For every row, `full-amount limit + (maximum ÷
  coefficient)` reproduces the published zero point to within 11 cents — e.g. 1 July 2026
  component B: `2,300.62 + (171.99 ÷ 0.2699) = 2,937.86` against a published `2,937.93`.
- **The blue-collar × 1.08 relationship holds on all six maxima and all six coefficient pairs**
  (`165.87 × 1.08 = 179.14`, `0.2699 × 1.08 = 0.2915`, and so on).

Four of the five substantive CCG findings are closed and I verified each in the text: the two-component
degressive formula is present with five dated parameter rows and an explicit correction-of-record
paragraph; the special social security contribution now has **three separately labelled household
tables** with a selection instruction in Module 5; the company-car age coefficient reads 94% for
months 13–24 and **88% for 25–36** with the worked example applying 88%; and the redundancy
example's end-of-year premium line now reads **697.61** in both the detail and the summary. Fedris
appears in the guide (4 occurrences) where previously it appeared zero times.

Why 86% and not higher. One figure in the guide rests on tier B alone and the cell calls it
`CONFIRMED` — the CO2 multiplier, `BE-X10-022`, a live blocker. C30 is unconditional about that, so
the band cannot sit in the 90s no matter how well the rest reconciles. Then three further findings:
the guide now carries a `NOT FOUND`
(the post-July annual cap); Module 4 attributes the work-bonus steps to GMMI dates that its own
tables contradict; and the work bonus's legal basis cites *"Royal Decrees implementing the work
bonus"* with no number and no date, for parameters stated as in force from 1 July 2026. Also still
standing: the notional 7% is asserted flatly twice and used to derive all four withholding rates,
while `known_limitations[6]` says it must be read off the Annex III text first — a **disclosure
defect on a number my own G-DERIVE pass makes almost certainly correct** (`25 × 1.07 = 26.75`, and
so for all four).

### 2.3 WTC — `02-wtc/BE-WTC-001-v1.0.xlsx` — **85%**

**A correction to round 1, recorded deliberately, because it is the largest single reversal this
pass produced.** Round 1 raised three blockers: the Global baseline violated in both dimensions
(`MISSING 300 / KEPT 0`), and a coverage sheet certifying the thing it contradicted. I re-measured
all three against the current file:

| Round-1 claim | Measured 17 Aug | Verdict |
|---|---|---|
| Column A empty in all 355 rows | **355 codes populated** | **closed** |
| 0 of 300 baseline codes present | **300 of 300, in baseline order, rows 2–301** | **closed** |
| 0 of 300 baseline descriptions preserved → "baseline overwritten" | 1 of 300 — **but the CZ precedent preserves only 93 of its 241, i.e. it rewrites 61% too** | **not a defect** |

The join-key fix closed the real half properly, and the description half was never a defect: column
B is *"Wage Type Name in English"* and localising it is what the governing precedent does. The
coverage sheet's claim at `Global WTC Coverage!A2` is now **true**. `Version Control!C18`'s
`placeholder` marker is gone.

Caps the band, hard: `Form Reference Guide!A2:E2` is still five `PENDING` cells asserting the
Report Specs and Data Dictionary *"have not been built for Belgium yet"* (§3, BE-X10-003), and the
fiscal work bonus is coded to Belcotax box 284 with **no wage type for box 360** (§3,
BE-X10-002) — a gap the Belcotax spec itself names in four cells and asks to have raised at the
stage gate.

### 2.4 Report Specs — `04-reports-spec/` (9 files, v1.2) — **86%**

Structure is exact and I measured it: 9 sheets in the right names and order in all nine files, the
core sheet at 21 columns A–U with the header matching
`shared/report-spec-template/ES-M296-001_ResumenAnual_Spec.xlsx` string-for-string.

**The DD write-back landed and I verified it against the files, not the changelog.** Column L
`NOT FOUND` counts moved 153→90 (FEDRIS), 122→40 (DmfA), 122→40 (DmfA Modification), 141→50 (DRS):
**318 mappings written back, exactly as certified.** The DmfA Modification declaration-type
container at `A12` is now differentiated — it reads MODIFICATION and states explicitly that it is
**not** `<DmfAOriginal>` block 90169. All 61 stale `BE-DD-001-v1.0` citations are re-pointed to
v1.1; the nine surviving v1.0 strings are legitimate changelog history in `Version Control!D15`.

Caps the band: 220 column-L cells still assert the DD does not exist while their own Version
Control says they were deliberately left (§3, BE-X10-009); 195 `BE-WTC-001` references resolve to
zero wage-type codes; 13 rows have no field name; 148 Belcotax Query-to-RA cells carry one
document-level question.

### 2.5 Data Dictionary — `05-data-dictionary/BE-DD-001-v1.1.xlsx` — **87%**

Three of the four DD findings you asked about are closed and verified: **0 option rows now carry a
label with no code** (was 57 across 14 blocks); the file is renamed v1.1 with `Version Control`
agreeing; and the four take-on fields carry explicit F26/YTD decision notes at `W32`, `W148`,
`W153`, `W154`, each naming the inbound integration that sources the balance. The mapper block
count measures **87**, matching the certified figure — the three contradictory patch counts of
BE-DD-007 are reconciled.

Caps the band: `Version Control!D14` certifies that *"the 35 NOT FOUND gap markers are registered
in scope_manifest.json known_limitations"*. **The workbook holds 36, and the manifest's
`known_limitations` holds 7 entries, none of them about a code table** (§3, BE-X10-004). A fifth
take-on field, `Country Fields` r156, got no F26/YTD note. `Country Option Mappers!F57` still
back-references `option_mapper_scope.contract_type`, a key the manifest renamed yesterday.

### 2.6 Payslip — `06-payslip/BE_Compliance_Payslip_Generator.xlsx` — **86%**

**The blocker is closed and it was the largest single repair in the dossier.** `Payslip Spec` ran
to 41 mapped rows in five sections; it now runs to **171 rows across fifteen sections**, and every
one of the nine previously unmapped rendered blocks has a section: Working Time, Non-Cash
Entitlements, Employer Contributions and Total Cost, Withholding Tax Calculation Basis,
Year-to-Date Cumulative, Leave Balances, Payment Details, Statutory Notes, Footer. The special
social security contribution note now states the **six-band quarterly table** rather than the
one-band rule. `A109` names all three language regions including German. 16 of 17
`$…custom.<field>` tokens now resolve to a real DD field.

Caps the band: `$employee.custom.working_time_regime` still resolves to nothing (the DD's nearest
field is *Working Time Cycle*); `Belgium (NL)!C16` and `A119` are still English on the legally
effective Dutch sheet; and the payslip is the surviving carrier of the contract-type collision
(§3, BE-X10-005) in both the spec and the delivered render.

### 2.7 scope_manifest.json v1.1 — **78%**

The lowest band in the set, and the band is about **currency and completeness, not correctness.**
The figures in it are clean: all 40 numeric literals in `wage_type_categories` were traced into the
current artifacts with zero contradictions. Its four blockers are closed and verified — inbound
crosswalked to IN-01…IN-19 with a `sir_flow_id` on all 19; form 325.10 moved out of scope; the
stock-option descoping narrowed to the grant-taxed variant; `contract_type` renamed
`contract_duration_type` with a real `contract_type` lock added and bound to `B48:F49`, which I
confirmed is the Full time / Part time mapper.

**And the v1.1 fix is unusually honest: it flags inline, in the entries it touched, the three
contradictions it did not close** — BE-SCOPE-011 on the outbound array, BE-SCOPE-012 on OUT-18, and
BE-SCOPE-014 on Limosa. That is the right way to leave a partial fix and it should be the house
standard.

Caps the band: eleven majors and five minors remain open (§5 reconciles every one against the file
as it stands), the outbound array was never crosswalked at all (§3, BE-X10-001), and
`known_limitations` has not gained a single entry in five days while the corpus opened dozens of
named gaps.

### 2.8 SKILL (Stage 11) — **not built, 0%**

`08-skill/` contains **zero files.** There is nothing to assess and nothing for the F28
propagation edge to point at.

---

## 3. The six open blockers

Full locations, evidence and expected values are in `_qa/REGRESSION-BE-XCHECK-r1.json`.

### BE-X10-001 — the manifest's outbound register was never crosswalked, and it is short by exactly seven flows

`scope_manifest.json!integrations.outbound` (12 entries, no `sir_flow_id` on any) against
`03-statutory-integrations/BE-SIR-001-v1.0.docx` §2.1 (19 outbound flows).

The v1.1 fix took the inbound array from 12 to 19 and stamped `sir_flow_id` on all nineteen. **It
did not touch the outbound array.** Crosswalking the twelve entries that exist leaves seven SIR
outbound flows with no manifest entry:

| Missing | What it is | Has a delivered v1.2 Report Spec? |
|---|---|---|
| OUT-03 | DmfA modification declaration | **yes** — `BE-NSSO-003-DmfAModification-Spec.xlsx` |
| OUT-07 | Work accident declaration | **yes** — `BE-FEDRIS-001-WorkAccident-Spec.xlsx` |
| OUT-08 | Limosa declaration | **yes** — `BE-NSSO-005-Limosa-Spec.xlsx` |
| OUT-16 | Electronic payslip delivery | no |
| OUT-17 | Social balance sheet data supply | no |
| OUT-18 | Checkinatwork presence registration | no |
| OUT-19 | DB2P / Sigedis declarations | no |

Three of the seven have a full Report Specification on disk. Two are already decided in the
manifest's *own other block* — `authority_filings.in_scope` carries `BE-INS-WACC-010` (work
accident) and `BE-PAY-PAYSLIP-008` (payslip), both `outbound` — so two blocks of one file disagree
about the same obligation. This is the same defect BE-SCOPE-001 raised, on the other side of the
register, and it is not described by BE-SCOPE-011, which is about flags and directions on the
twelve entries that do exist.

### BE-X10-002 — the 52.54% half of the fiscal work bonus is never reported on the 281.10

`02-wtc/BE-WTC-001-v1.0.xlsx!Wage Type Catalogue!G304` — wage type `BE-003` *"Fiscal work bonus -
withholding tax reduction"*, Tax Code `284` and nothing else.

The CCG states the fiscal work bonus as **33.14% of component A and 52.54% of component B**. The
Belcotax fiche carries the two halves in two different boxes, and
`04-reports-spec/BE-FIN-002-Belcotax28110-Spec.xlsx` says so in four separate cells:

- `Belcotax 281.10 Spec!D127` — `Zone 2.210 — box 360`, XML tag `<f10_2210_workbonus5254/>`
- `!L127` — *"NOT FOUND - no BE-WTC-001 wage type carries tax code 360."*
- `!N127` — *"NOTE: BE-WTC-001 carries no wage type coded to box 360. **This is a genuine catalogue
  gap to raise at the next stage gate**, not an error in this specification."*
- `File Structure!A80` — *"GAP IN THE OTHER DIRECTION: box 360 (work bonus, 52.54% tax credit,
  zone 2.210)"*

**The spec asked to have this raised at the stage gate. This is that stage gate.** Expected: either
`G304` carries `284; 360`, or `BE-003` splits into two wage types, one per component. The tag name
`workbonus5254` removes any doubt about which component box 360 carries.

### BE-X10-003 — the WTC still tells its reader that two delivered artifacts do not exist

`02-wtc/BE-WTC-001-v1.0.xlsx!Form Reference Guide!A2:E2` — five cells reading `PENDING`, with
`E2`: *"PENDING - Report Specs (Stage 3) and Data Dictionary (Stage 4) have not been built for
Belgium yet."* And `Version Control!C18`: both directories *"are empty for Belgium."*

Nine specs at v1.2 have been on disk since 14 August; `BE-DD-001-v1.1.xlsx` since 16 August. This
survived the join-key repair (15 Aug) and the work-bonus repair (17 Aug 01:23) — **two passes
opened this exact workbook and neither opened this sheet.** F27 in its purest form, now three days
older than when round 1 raised it.

### BE-X10-004 — the DD certifies a registration in a file that does not contain it

`05-data-dictionary/BE-DD-001-v1.1.xlsx!Version Control!D14`: *"The 35 NOT FOUND gap markers are
registered in scope_manifest.json known_limitations."*

Measured, both sides:

- The workbook holds **36** markers, not 35 — 18 in the Code column, 18 in English Description.
- `scope_manifest.json!known_limitations` holds **7 entries and not one is about a code table.**

Both halves of the sentence are false. The claim was written 16 August about a file the pass never
opened; the manifest was next edited on 17 August and still does not carry them. This is the
G-CLEAN failure in its most dangerous form: not an unregistered gap, but an unregistered gap with a
written assurance that it was registered — which is what stops the next reader from looking.

### BE-X10-005 — the contract-type collision survives in the payslip, including in the delivered render

Three locations in `06-payslip/BE_Compliance_Payslip_Generator.xlsx`:

- `Payslip Spec!E40` — *"Indefinite duration, fixed term, clearly defined work or replacement. …
  **Source: BE-DD-001 Country Fields, 'Contract Type'**."*
- `Payslip Spec!D40` — the binding `$employee.custom.contract_type`
- `Belgium (EN)!A24` / `C24` — label **"Contract Type"** over the rendered value **"Indefinite
  duration (onbepaalde duur)"**

The DD is unambiguous and holds both fields separately: `Country Fields` r24 *Contract Type* →
mapper *Contract Type* `{0 = Full time, 1 = Part time}` (NSSO zone 00050), and r25 *Contract
Duration Type* → mapper *Contract Duration Type*. The payslip cites the first and lists the values
of the second. The manifest fixed its own instance of this collision on 17 August; the payslip is
the third carrier and the only one where the wrong pairing is **rendered on the delivered
document**.

### BE-X10-022 — the CO2 multiplier rests on four tier-B sources and the cell calls that CONFIRMED

`01-ccg/BE-CCG-001-v1.0.docx` Module 7.2, CO2 solidarity contribution parameter table, the row
*"Multiplier for combustion vehicles ordered from 1 July 2023"*:

> *"4 for 2026 (CONFIRMED - Agoria, Cellule Mobilite, Van Mossel, Dynamik HR all independently
> state x4 for 2026, not the previously-stated 2.75), rising further in later years under the
> greening law (Dynamik HR cites 5.50 from 2027, not independently re-verified here)."*

Not one of the four named sources is the NSSO or the greening law: an industry federation, a
mobility cell, **a car dealer group** and a payroll consultancy. Corroboration among four tier-B
sources is not promotion to tier A, and the word **CONFIRMED** in the cell asserts that it is. C30
is unconditional — a figure resting on tier B alone is a FAIL — and this one multiplies the CO2
solidarity contribution that the WTC builds as a wage type (`Wage Type Catalogue!F59`) and the DmfA
declares per vehicle per month.

**This is the one blocker from the seven individual sweeps that the 17 August round did not close,
and it is why this report says 17 of 22 rather than 18.** Carried forward from `BE-CCG-003`.

**The containment, recorded as the genuine positive it is.** I measured where the number went: the
values 4 / 2.75 / 5.50 and all four vendor names appear **in the CCG and nowhere else in the
corpus.** The DD (`Country Fields!G167`), the DmfA spec (`Field Options!C36`, `Population Rules!D14`)
and the SIR (gap G22) each reference the multiplier by its *selector* — the vehicle order date —
without the value. **No downstream artifact inherited the weak figure.** That is precisely the
discipline that stops a tier-B number spreading, and it worked.

---

## 4. The eleven open majors

| id | Location | What is wrong |
|---|---|---|
| **BE-X10-006** | CCG line 1456 · WTC `Wage Type Catalogue!F303`, `Version Control!C25`, `Tax Credit!B6` · PSL `Belgium (EN)!N83`, `Belgium (NL)!N83` | The work-bonus fix propagated a `NOT FOUND` (the post-1-July annual cap) into three artifacts and six cells and registered it in no limitation register. The propagation itself is correct and consistent — including the Dutch `NIET GEVONDEN` — but the CCG was the only BE artifact to pass the widened C29 lint and no longer does. |
| **BE-X10-007** | CCG Module 4, the *Social work bonus* bullet under *"Does the minimum wage impact any tax or social security calculations?"* | Attributes the work-bonus steps to GMMI dates its own tables contradict. Module 4's GMMI table steps **1 Jan / 1 Apr / 1 Aug**; the prose says the limits *"moved with it"* on **1 April and 1 August** and then dates the moves **1 July** and **1 September**; Module 5.1.1's table steps 1 Jan / 1 Mar / 1 Apr / 1 Jul / 1 Sep with **no 1 August row**. Module 11's calendar gets it right. Row selection is *"by the pay month"*, so a reader who follows Module 4 looks for an August row that does not exist. |
| **BE-X10-008** | CCG Module 5.1.1, *Legal basis* line | *"Programme Law of 24 December 2002, Article 353bis; **Royal Decrees implementing the work bonus**; NSSO administrative instructions editions 2026/1 and 2026/2"* — no number, no date, no 2026 instrument named, for parameters stated as in force from 1 July 2026. The discipline exists elsewhere in the same guide: the Programme Law of **30 May 2026, Articles 109-110** is cited by number for the high-wage measure, and the Royal Decree of **11 December 2025** eight times for Annex III. |
| **BE-X10-009** | 4 spec files, column L: FEDRIS ×90, DmfA ×40, DmfA Mod ×40, DRS ×50 | 220 cells read verbatim *"NOT FOUND - mapping not yet decided; requires the Stage 4 Data Dictionary"* while `Version Control!D15` of each says those same cells were *"deliberately left NOT FOUND (transactional, calculated or system-generated, no DD field by design)"*. The decision was taken; the wording was never updated. Two contradictory statements about the same cells in one workbook. |
| **BE-X10-010** | WTC `Wage Type Catalogue!S,T` (0 of 355 populated) · DD `Country Fields` r156 | The YTD-Load mechanism is entirely unused, and a fifth take-on field — *Belgium Months of Service in the Holiday Service Year*, *"loaded at implementation"* — got no F26/YTD decision note when the other four did. The defect class was swept incompletely again. |
| **BE-X10-011** | All 9 specs, column L | 195 `BE-WTC-001` references; **zero** resolve to any of the 355 wage-type codes now in column A. The join key exists and nothing uses it. |
| **BE-X10-012** | `08-skill/` | Stage 11 not built — zero files. Every artifact now carries version-specific references (DD v1.1, specs v1.2) with no skill to propagate into, so the F28 edge has no target. |
| **BE-X10-013** | PSL `Payslip Spec!D37` | `$employee.custom.working_time_regime` resolves to no DD field. Nearest is `Country Fields` r188 *Working Time Cycle*. Last survivor of BE-PSL-003; the other two tokens now resolve. |
| **BE-X10-014** | PSL `Belgium (NL)!C16`, `!A119` | English text on the legally effective Dutch sheet: *"Insurer enterprise number 0850.123.440"* (its own label above is translated) and *"This document has been generated by Mercans Payroll System"* (A120 beneath it **is** Dutch). Of 13 identical EN/NL strings, 11 are proper nouns and IBANs that must be identical; these 2 are the exceptions. On the artifact whose own `A109` states the sanction for the wrong language is nullity. |
| **BE-X10-015** | FEDRIS `!A` ×6, DRS `!A` ×7 | 13 field rows whose Field Name (EN) is literally `NOT FOUND`, column H blank. A row with no name and no position cannot be built, mapped, or raised with the authority. |
| **BE-X10-016** | Belcotax `!T3:T166` | One document-level question (gap G15) bulk-filled into 148 of 166 Query-to-RA cells, hiding any real per-field query. |

---

## 5. `scope_manifest.json` `_revision_history[1].still_open` — every item verified against the file as it stands

You asked me to verify rather than assume in either direction. I read the current manifest for each
one. **Three moved; thirteen did not.**

| id | Recorded status | **Verified status, 17 Aug** | Evidence |
|---|---|---|---|
| BE-SCOPE-005 | open | **OPEN** | No `gender` key, no `charge_bearer` key. `insurance_type` still 4 invented strings, `correction_codes` still 3, neither matching any DD block. `benefit_type` grew to 12 values as a side effect of the BE-SCOPE-003 fix but was not re-pointed at the WTC that owns it. |
| BE-SCOPE-006 | open | **OPEN** | `known_limitations[0]` verbatim unchanged: *"No official source PDFs were available…"*. Disk: 42 files in `spec-sources/`, **15 of them PDFs**. |
| BE-SCOPE-007 | open | **OPEN** | `known_limitations[6]` unchanged, precondition still stated as future, still crossed. |
| BE-SCOPE-008 | open | **OPEN** | 7 entries, none added. Meanwhile the SIR opened 27 gaps, the DD 36 markers, the specs 848, the CCG 1. |
| BE-SCOPE-009 | open | **OPEN** | `F23`/`F24`/`F25`/`F26` strings verbatim unchanged, including *"not triggered: no source PDFs present"*. |
| BE-SCOPE-010 | open | **OPEN, now measured** | I swept 41 work-bonus / GMMI / high-wage figures across all seven artifacts. The manifest carries **zero of the 41.** Not one component limit, maximum, coefficient, cap, GMMI step or the 86,700 threshold. |
| BE-SCOPE-011 | open | **PARTIALLY CLOSED** | Inbound now carries 9 inline rationales and two `product_mapping_required: false`. Outbound is still 12/12 `true` with **zero** rationales and no `sir_flow_id`. The manifest's own `_inbound_note` declares this open — correctly. Now compounded by BE-X10-001. |
| BE-SCOPE-012 | open | **PARTIALLY CLOSED, new internal contradiction** | `BE-IN-CHECKINATWORK-RESPONSE` (IN-19) is now registered in scope — so the manifest registers the Checkinatwork **response** while the Checkinatwork **declaration** itself is still undecided. OUT-16 electronic payslip is likewise absent from `integrations.outbound` though `authority_filings.in_scope` `BE-PAY-PAYSLIP-008` decides it. Both flagged inline by the fix. |
| BE-SCOPE-013 | open | **OPEN, confirmed by measurement** | Across all 355 WTC wage-type names: `pc` 0, `tablet` 0, `internet` 0, `mobile` 0, `laptop` 0, `smartphone` 0. Meals: only the six meal-**voucher** lines, no free-meals BIK at flat statutory value. Loans: one line only, *"Repayment of salary advance or company loan"* — a repayment deduction, not the interest benefit. Against **11 housing, 5 heating, 3 electricity** wage types built from the same manifest entry. The asymmetry is what makes it an omission rather than a design choice. |
| BE-SCOPE-014 | open, escalated | **CLOSED 2026-08-17 by owner ruling** | The ruling went the way the manifest had argued: the Limosa declaration is filed by the **foreign posting employer**, never by the Belgian host company (*Programmawet/Loi-programme (I) du 27 décembre 2006*, arts. 139 and 155, executed by the RD of 20 March 2007), and the posted population stays on its home-country payroll under an A1, so it is **out of scope for HRBLIZZ**. The only Belgian-side duty is the exception-based art. 141 check — verify the Limosa-1, report to the NSSO only if it cannot be produced — which is HR/onboarding scope. One reconciliation pass across all four artefacts: manifest keeps both descopings with consolidated primary-source rationale, registers the spec as a descoped artefact, and **removed IN-17** (`BE-IN-LIMOSA-RECEIPT`) — there is no inbound flow to narrow, since the receipt is returned to the foreign declarant, not to this product; SIR OUT-08/IN-17 retained for contiguity but reclassified as descoped and exception-only; spec to v1.3, descoped on its Report Matrix and Payroll Scope Summary and retained rather than deleted; CCG Modules 2.2, 10.1 and 11.2 now qualify **who** it is mandatory for. A separate defect was found and fixed in the same pass: the CCG and the spec both cited the *Law of 11 February 2013* for Limosa, which is the Directive 2009/52/EC transposition on sanctions against employers of illegally staying third-country nationals — the wrong instrument. ~~**Newly surfaced, not fixed:** BE-DD-001 still carries Limosa-driven fields sourced from the now-descoped spec (see the manifest's `_revision_history` v1.3 `still_open`).~~ **FIXED 2026-08-17 by owner decision:** the **13** Country Fields rows that existed solely to feed the descoped filing were **deleted** from `BE-DD-001-v1.1.xlsx` — A1 Certificate Reference, A1 Issuing Institution, A1 Validity Start/End Date, Posting Start/End Date, the three Limosa Declarant fields and the four Foreign Posting Employer fields. `A1 Certificate Held Indicator` was **kept**: it is not a Limosa field — it decides whether Belgian social security contributions are due at all, is sourced to CCG Modules 5.1 / 11.2 and carries no `BE-NSSO-005` reference, so it fails the removal test the decision itself set. `validate_workbook.py --artifact DD` **PASS (blocker=0 major=0 minor=0)**; `verify_be_dd.py` **PASS**, C2 still 0 missing because the 12 `BE-NSSO-005` Sheet 4 keys that targeted the deleted fields were reclassified in `dd_crosscheck_map.py` as DD-shaped-but-descoped rather than left dangling. ~~**Still owed, and narrower than before:** 9 DD fields retaining a `BE-NSSO-005` reference were outside this decision's scope — see `L-14`.~~ **SECOND BATCH, same day: the remainder was ruled on and the DD-side exposure is now CLOSED.** The **6** fields that were Limosa-only on their face were **deleted** as rows from `BE-DD-001-v1.1.xlsx` (backup `...bak-before-limosa-field-removal2`, retained): *Place of Work in Belgium* (LIM-032), *Nature of the Posted Services* (LIM-033), *Posted Worker Working Time Schedule* (LIM-034), *Belgian Client Name* (LIM-040), *Belgian Client Enterprise Number* (LIM-041), *Belgian Client Address* (LIM-042). Country Fields **253 → 247**. `validate_workbook.py --artifact DD` **PASS (blocker=0 major=0 minor=0)**; `verify_be_dd.py` **PASS**, C2 still 0 missing because the 6 corresponding `BE-NSSO-005` Sheet 4 keys were reclassified DD-shaped-but-descoped under a separate `LIM2` reason string (12 + 6 = **18** total), each first re-verified exclusive to `BE-NSSO-005` **against the live spec workbooks rather than the cached dump**. **Closure measured, not asserted:** the 8 DD fields still carrying a `BE-NSSO-005` reference each have a documented non-Limosa consumer, so **zero Limosa-only fields remain in the DD**. ~~**The only Limosa loose end left in the repository is the `BE-WTC-001` half** — wage type BE-054's narrative says posted workers "require a Limosa declaration" without qualifying who files it, the same defect class fixed in CCG Module 10.1 by the 1C pass. Not fixed here and deliberately not absorbed into a DD pass; see `L-14` and `PROPAGATION-LEDGER.md` 1E.6.~~ **THE WTC HALF RECEIVED ITS OWN PASS ON 2026-08-17 AND BE-SCOPE-014 IS NOW CLOSED IN FULL — NO LIMOSA LOOSE END REMAINS IN THE REPOSITORY.** One cell changed: `BE-WTC-001-v1.0.xlsx` `Wage Type Catalogue!F355` (BE-054), whose closing sentence now reads *"…but it is filed by the foreign posting employer itself — or by the foreign self-employed person under art. 155 — and never by the Belgian payroll client, so the declaration is out of scope for this payroll build (Programme Law (I) of 27 December 2006, arts. 139 and 155; Royal Decree of 20 March 2007); the only Belgian-side duty is the art. 141 check that the declaration was made, an HR onboarding control rather than a payroll step."* (613 → **1,049** chars, measured on the delivered workbook; `logs/wtc_limosa_wording.log` states 1,073, which is **wrong by 24 characters** — the *before* figure of 613 is correct, and the count is the only thing in that log that did not survive re-measurement). Wording was **aligned to CCG Module 11.2 rather than freshly composed**, so the WTC now states the determination the reconciliation pass already made, in the same terms. The `Limosa` token is retained, so the `selfcheck_be_wtc.py:131` `BE_MARKERS` anchor still binds and did not have to move. **Root-caused, not surface-patched:** `be_wtc_data_part7.py:460` (the BE-054 generator tuple) carried the old sentence and was given the same text, asserted equal to the workbook cell programmatically, so a rebuild cannot resurrect it. Backup `BE-WTC-001-v1.0.xlsx.bak-before-limosa-wording-fix` taken before any edit, MD5-verified and **retained**. **VERIFICATION:** `validate_workbook.py --artifact WTC` **PASS (blocker=0 major=0 minor=0)**; `selfcheck_be_wtc.py` baseline captured before the edit and re-run after — **identical**, the same pre-existing `ORANGE populated [10 cells, A2..A11]` assertion, same count, **no new failure introduced**; cell-level diff across all 6 sheets (values plus fill/font/number-format/alignment/borders, dimensions, freeze panes, column widths) **`TOTAL DIFFS: 1`**, the F355 value alone, no style drift even on that cell; zip-level diff confirms exactly one changed entry (`xl/worksheets/sheet2.xml`) with the embedded image and both cell-comment/VML parts **byte-identical** to the backup — the edit was made inside the zip precisely because an openpyxl round-trip would have dropped them. **LIMOSA IS NOW FULLY RESOLVED ACROSS ALL FIVE ARTEFACTS IT TOUCHED** — `scope_manifest.json`, `BE-SIR-001`, `BE-CCG-001`, `BE-NSSO-005-Limosa-Spec.xlsx` and `BE-DD-001-v1.1.xlsx` — **plus this WTC wording-precision fix**, on the single statutory basis carried unchanged since the 1C ruling: *Programmawet (I) van 27 december 2006 / Loi-programme (I) du 27 décembre 2006*, Title IV, Chapter VIII, **arts. 137, 139, 141 and 155**, MB/BS 28 December 2006, executed by the *Arrêté royal / Koninklijk besluit* of 20 March 2007. |
| BE-SCOPE-015 | open | **PARTIALLY CLOSED** | Closed: `scope_version` 1.1, `scope_last_updated` 2026-08-17, `_revision_history` added, and the mapper `_bound_to` fields now name `BE-DD-001-v1.1.xlsx` and `BE-NSSO-002-DmfA-Spec.xlsx` — so "zero references to downstream artifacts" is no longer true. Still open: `generated` = `2026-08-12T00:00:00`, `scope_decided_on` = `2026-08-12`, `source_artifact` = `BE-CCG-001-v1.0.docx`, and **no consumers block** listing each artifact at the version on disk. |
| BE-SCOPE-016 | open (minor) | **OPEN** | `both` still 3 entries, still no `BE-BOTH-BV` against `BE-FIN-BV-003`'s `integration_type: both`, still no note that `both` is a view and must not be counted separately. True distinct flows: 24, expressed as 27. |
| BE-SCOPE-017 | open (minor) | **OPEN** | `authority_filings.out_of_scope` order is `011, 012, 013, 014, 015, 016, 017, 009, LIMOSA-L1-VERIFY, 005` — the appended entries sit at the end, out of `filing_id` sequence. |
| BE-SCOPE-018 | open (minor) | **OPEN** | `known_failure_patterns_to_check` still a bare `F1…F22` with no descriptions and no outcomes, alongside a second differently-shaped 6-entry array. |
| BE-SCOPE-019 | open (minor) | **OPEN** | Both `code` and `country_code` present, both `"BE"`; the template defines only `country_code`. |
| BE-SCOPE-020 | open (minor) | **OPEN** | `integrations.inbound` `BE-IN-GARNISHMENT-ORDER` rationale still says the engine *"must apply the Judicial Code Art. 1409 net-wage bands"* without qualification. The word "maintenance" does not appear in it. The DD records the exception at mapper code 3: *"Attachable WITHOUT ANY LIMIT - the protected bands do not apply."* |

**One new minor from this pass:** the v1.1 fix introduced **10 `NOT FOUND` strings into
`scope_manifest.json` itself** — inside `option_mapper_scope.contract_duration_type`, for the four
contractual variants whose NSSO zone-00885 mapping is unknown. They are the first C29-class markers
in that file, and they sit in the scope lock rather than in `known_limitations`, which is the
G-CLEAN-correct home.

---

## 6. The two items that are genuinely unresolved, not defective

You asked me to distinguish these from confirmed defects. Both are.

### 6.1 The RSZ / NSSO 9-digit employer-number check digit — **unresolved, and correctly so**

**Not a defect. Not a contradiction.** The corpus states it identically everywhere it appears —
CCG Module 2.2 and `BE-NSSO-005-Limosa-Spec.xlsx` `Field Options!C11` and `Population Rules!D7`:
*"9 or 12 positions, composed of an employer category prefix, a registration number, and a
two-digit modulo-97 check on the preceding positions."* C32 passes.

What is missing is not a value but a **specification**: the sentence never says which positions the
check spans in the 9-position variant versus the 12-position one, and — the part that matters — it
never says whether the check is the **remainder** mod 97 or the **complement** to 97.

That distinction is load-bearing, and the corpus proves it knows so, on a *different* number.
`BE-FIN-001-Finprof274-Spec.xlsx!File Structure!A80` runs a block headed *"CHECK-DIGIT ALGORITHMS
— TWO OF THEM, AND THEY ARE NOT THE SAME"*, and `Population Rules!E8` states: *"the reference
number takes the COMPLEMENT to 97, the payment reference takes the REMAINDER. Implementing one for
both yields a file that passes structural validation and produces an unmatched payment."* The same
spec fully specifies the 10-digit FPS Finance reference number and then says only that *"nine
digits instead of ten remains permitted"* — without giving the nine-digit rule.

**Status:** genuinely unresolved from held sources. **What would close it:** the NSSO's employer
identification documentation, or the DmfA XSD from the NSSO TechLib, obtained by
`compliance-source-hunter` — routed, never fetched by this pass. **What is wrong today:** it is
unresolved and **named nowhere** — not in `known_limitations`, not in the SIR's G1–G27, not in any
spec's accuracy statement. That part is a defect, and it is the same one as BE-X10-004.

### 6.2 The post-1-July-2026 social work bonus annual cap — unresolved and honestly documented

The CCG states the cap at EUR 3,466.44 from 1 January and EUR 3,523.92 from 1 April, then records
the July value as `NOT FOUND`, names the exact source that would close it (*"the NSSO
administrative instructions edition covering the third quarter of 2026, the werkbonus annex"*), and
warns in terms: *"Do not extrapolate it from the 2% indexation applied to the other parameters."*
**That is the correct handling of an unresolvable gap and it should be the model.** Its only defect
is that it lives in the artifact rather than in a limitation register (BE-X10-006).

---

## 7. Every open limitation, with what would close it

| # | Limitation | What closes it |
|---|---|---|
| L-01 | ~~**No `legal-basis-register.csv`.**~~ **CLOSED 2026-08-18 — THE REGISTER EXISTS, WITH THE SCOPE OF ITS COVERAGE STATED RATHER THAN IMPLIED.** `00-official-sources/legal-basis-register.csv`, **63 rows on the pipeline's own 20-column contract** (`compliance-source-hunter` §3.3, referenced by `shared/schemas/README.md`) — not the 9-column fallback, which was conditional on no spec existing. Built exactly as this row prescribed: **retrospectively, from citations already in the corpus**, with **`consumed_by` populated on 61 of 63 rows and MEASURED, not asserted** — 384 tokens over 28 artifact units (CCG 194, WTC 46, RSPEC 32, SKILL 29, SCOPE 28, PSL 24, DD 18, SIR 13), each derived by matching per-row regex probes against a plain-text dump of all eight delivered artifacts, with nine false-positive consumers caught and removed by a probe-level audit. Tier **A.1 33 / A.2 27 / A.3 1 / B 2**; `verification_method` is one of the three G-SPOT methods on every row. ~~P2 cannot be run as specified anywhere in Belgium; it was re-based onto C32 cross-artifact consistency plus direct re-derivation from the 15 authority PDFs.~~ **P2 can now be run as specified for any figure that has a row.** | ~~Build the register retrospectively...~~ **DONE for the load-bearing figures; NOT a completeness claim.** This is a retrofit of the ~60 most significant figures — every figure this run found, fixed or re-sourced, plus the constants many worked examples depend on — against a corpus holding thousands of values, and **no existing artifact literal was given a `register_id`**: the traceability runs register → artifact through `consumed_by`, not artifact → register through an inline id. What would close the residue: extending the register (next candidates named at `PROPAGATION-LEDGER.md` §3.6) and, separately, stamping `register_id` into the artifacts themselves. |
| L-02 | **No `_pipeline/build-manifest.json`, no `_research/`, no per-artifact build log.** No section → `register_id` map exists, so no figure is traceable to the source that produced it. | Retrofit the three contracts per `mercans-pipeline-contracts`. |
| L-03 | **No tier classification** (§1). | A `build-manifest.json` with per-domain tier, echoed verbatim in the CCG Foundational module and the scope manifest. |
| L-04 | ~~**P5 has no checklist.**~~ **CLOSED 2026-08-18 — P5 NOW HAS A CHECKLIST, AND THE LEDGER SAYS EXACTLY WHAT THAT DOES AND DOES NOT CHANGE.** `PROPAGATION-LEDGER.md` §0 was reframed (§1I.4): from 18 August 2026 a figure that moves is propagated by reading its register row's `consumed_by`, opening every unit it names and writing one ledger line per consumer with a verdict — **a missing consumer line is now a defect, not a limitation.** ~~every propagation edge ... is therefore incomplete by construction~~ **§1–§1H are NOT reissued against the register and are not claimed to be complete:** they stay as written, historically accurate for what was actually checked at the time, each line naming the file re-opened. Rewriting them against a source they did not have would convert an honest record of a hand sweep into a false claim of a systematic one. §1B.5's *"fourth argument for the register"* now records that its own missed edge is register row `BE-SSC-014`, whose `consumed_by` names the WTC — the artifact the hand sweep missed. | ~~The register at L-01.~~ **DONE.** Residual, declared at §3.6: propagation of any figure **without** a register row is exactly as unchecked as it was on 17 August. |
| L-05 | **The post-July work-bonus annual cap** is unknown (§6.2). | NSSO administrative instructions, edition covering Q3 2026, werkbonus annex. **REGISTERED 2026-08-18** in `scope_manifest.json` `known_limitations` as out of reach: not resolvable through documentation research, and not attempted. It was already registered - `known_limitations` entry 9, with its own WHAT CLOSES IT line and its own DO NOT EXTRAPOLATE warning - and that entry was **confirmed unchanged**, not rewritten. One correction of record made alongside: `scope_manifest.json` `_revision_history` v1.9 cited this item as *L-13*; it is **L-05**, and the mislabel was corrected in place with the reason stated. |
| L-06 | **The NSSO 9-position employer-number check-digit rule** is unspecified (§6.1). | NSSO employer identification documentation or the DmfA XSD from the NSSO TechLib. **REGISTERED 2026-08-18** in `scope_manifest.json` `known_limitations` as out of reach: not resolvable through documentation research, and not attempted. It was already registered - `known_limitations` entry 8, which states the real defect precisely (not a missing value but a missing specification: which positions the check spans in the 9-position variant, and whether the two digits are the *remainder* mod 97 or the *complement* to 97) and forbids implementing a modulo-97 check on the employer number until the authority answers. **Confirmed unchanged**, not rewritten. |
| L-07 | **The FinProf period-code series for income year 2026** is unknown — the published source table stops at 2015 and the series rotate on a four-year cycle. Digits 8–10 of every withholding-tax payment reference depend on it. | `info.finprof@minfin.fed.be`, or a current FPS Finance file description (SIR gap G13 is adjacent but does not name the series). **REGISTERED 2026-08-18** in `scope_manifest.json` `known_limitations` as out of reach: not resolvable through documentation research, and not attempted. New entry: it was **not in `known_limitations` at all** before this pass. It now names the closing condition from this row, and states the silent failure mode - a wrong series produces a payment that passes structural validation and is then never matched to the declaration - plus an explicit DO NOT EXTRAPOLATE FROM THE 2015 TABLE. |
| L-08 | **Belcotax income-year-2026 schema.** The register declares itself IY2026 and names only IY2025 artefacts. | `belcotax@minfin.fed.be`; the IY2026 brochure and XSD. **REGISTERED 2026-08-18** in `scope_manifest.json` `known_limitations` as out of reach: not resolvable through documentation research, and not attempted. New entry: it was **not in `known_limitations` at all** before this pass. It now names the closing condition from this row and the consequence - Belcotax zone numbering and validation rules change between income years, so a spec built on the IY2025 layout and labelled IY2026 is structurally accepted and semantically wrong. |
| L-09 | **ITC 92 Art. 412 thresholds** rest on a police-zone manual, with an "indexation" equivalence implying a 2.0096 coefficient stated nowhere. | Routed to `compliance-source-hunter`; primary FPS Finance text. **REGISTERED 2026-08-18** in `scope_manifest.json` `known_limitations` as out of reach: not resolvable through documentation research, and not attempted. New entry: it was **not in `known_limitations` at all** before this pass. It now names the closing condition from this row and forbids configuring the unsourced 2.0096 coefficient on the strength of the police-zone manual alone, stating why it matters: Article 412 governs the *timing* of the withholding-tax payment obligation, so an unsourced coefficient yields a wrong payment calendar. |
| L-10 | **36 DD code tables unresolved** (`NOT FOUND` in Code and English Description) — Contract Duration Type, NSSO Worker Status/Code/Employer Category, Joint Committee Number, NIS Country Code, Health Insurance Fund Code, Days Justification and others. | The NSSO glossary code lists and the DmfA XSD, per table. **PARTIALLY CLOSED 2026-08-18 - REGISTERED, NOT SOLVED.** What was done is bookkeeping only: a consolidated `known_limitations` entry that names all 16 mapper blocks and points at the DD's own `Country Option Mappers` sheet as the register of record, where every marker names its own missing source. **THE UNDERLYING EXTERNAL SOURCING REMAINS GENUINELY UNRESOLVED.** No code list has been obtained from any authority, no marker has been replaced by a value, and the count on disk is still **exactly 36**. The registration makes the gap findable and auditable; it does not narrow it, and this row must not be read as closed. What closes it is unchanged and is not a documentation-research task. |
| L-11 | **SIR gaps G1–G27** — 21 closeable by authority inquiry (named owners and real addresses), 5 only in a client contract, G27 closed. | The named enquiry per row; G22–G26 close per client, not per country. **REGISTERED 2026-08-18** in `scope_manifest.json` `known_limitations` as out of reach: not resolvable through documentation research, and not attempted. New entry: it was **not in `known_limitations` at all** before this pass. It now carries this row's own split - 21 closeable only by an inquiry to a named authority owner, 5 (G22-G26) not closeable at country level at all because they settle in a client data contract, G27 closed - and says why the split is registered rather than left implicit: a future pass that treats G22-G26 as research items will spend effort on questions that have no country-level answer. |
| L-12 | **13 spec fields with no name** and **148 bulk-filled Belcotax query cells** (BE-X10-015, -016). | FEDRIS and DRS field layouts from their authorities; one document-level G15 question. **CLOSED 2026-08-17.** Closed by `BE-X10-015` and `BE-X10-016`, and the first half was **never a source gap**: all 13 XML labels were already published in the primary sources held at `00-official-sources/spec-sources/`, and the `NOT FOUND` markers came from a parser that read the `(Label XML:...)` marker only on the line *after* the zone header, so any title wrapping onto a second line was missed. 64 cells repaired across FEDRIS, DRS, DmfA and DmfA Modification; **unnamed field rows across all nine specs: 0**. The 148 bulk-filled Belcotax cells now carry 148 distinct field-specific queries, G15 retained once on the control-total row. Registered closed in `scope_manifest.json` v2.0. See `PROPAGATION-LEDGER.md` 1G.7 and 1G.8. |
| L-13 | **Three statutory benefits in kind have no wage type** — free meals, PC/tablet/internet/mobile, interest-free loan (§5, BE-SCOPE-013). | A WTC round adding them, or a recorded decision to descope with the CCG Table 74 reference. **CLOSED ON THE WAGE-TYPE HALF 2026-08-18, ONE RESIDUAL OPEN.** The first of the two options this row named was taken - a WTC round - because the second, a recorded descope, was not available: `scope_manifest.json` locks all three benefits in scope twice over. **BE-056** (free meals), **BE-057** (PC, tablet, internet connection, mobile phone or telephone subscription for private use) and **BE-058** (interest-free or low-interest employer loan) added at rows **357-359** of `BE-WTC-001-v1.0.xlsx`, on the flat valuations of **Article 18, para. 3 of the Royal Decree implementing ITC 92 (RD of 27 August 1993)**: 6 degrees and 8 degrees for the meals (EUR 0.55 breakfast / EUR 1.09 main meal / EUR 0.84 evening meal per day, **not indexed**); 10 degrees for the devices and services (EUR 72.00 PC, EUR 36.00 tablet, EUR 36.00 mobile phone, EUR 60.00 internet, EUR 48.00 telephone subscription per year, as substituted by the **RD of 2 November 2017**, BS 13 November 2017, numac 2017013902, in force 1 January 2018); 1 degrees for the loan. All three are **within the NSSO wage concept**, unlike the company car, and the NSSO adopts the identical flat amounts for the meals and the devices. **THE RESIDUAL, AND IT IS A GENUINE `NOT FOUND`: the income-year-2026 reference interest rates for the loan benefit are not published** - they are fixed only by the Royal Decree of the *following* February (the IY2025 set came by the RD of 8 February 2026, BS 17 February 2026), so they are not expected before February 2027. BE-058 carries the IY2025 rates labelled **PROVISIONAL** (fixed-rate mortgage 3.00%; fixed-term non-mortgage a monthly charge of 0.26% for vehicle financing and 0.52% otherwise; non-mortgage without a determined term 5.57%) and instructs a recomputation and a 281.10 restatement once the definitive rates appear. A second asymmetry is recorded and must not be flattened: **the NSSO does not follow these rates at all** - it values the loan advantage at its actual value against a market-conform rate, and treats the loan as a mere wage advance carrying no benefit where repayment begins shortly after payment, runs for at most one year and the amount is reasonable against one month of net pay. `validate_workbook.py --artifact WTC` **PASS (blocker=0 major=0 minor=0)**. See `PROPAGATION-LEDGER.md` 1H and `scope_manifest.json` v2.0. |
| L-14 | ~~**Limosa is unresolved four-and-a-half ways** (§5, BE-SCOPE-014). **Escalated to a human** — this is a scope decision, not an audit finding.~~ **CLOSED 2026-08-17.** The owner ruled Limosa **out of scope** — filed by the foreign posting employer, posted population not on Belgian payroll, Belgian-side duty limited to the exception-based art. 141 Limosa-1 check (HR scope). The reconciliation pass across manifest, SIR, spec and CCG has been run; see BE-SCOPE-014 in §5. | ~~An owner's ruling, then one reconciliation pass across manifest, SIR, spec and CCG.~~ **Done.** ~~Residual, and separate: BE-DD-001's Limosa-driven fields were built to populate the descoped filing and their keep-or-descope status is still owed.~~ **The residual was decided on 2026-08-17: descope with the filing.** 13 Country Fields rows **deleted** from `BE-DD-001-v1.1.xlsx` (backup `BE-DD-001-v1.1.xlsx.bak-before-limosa-field-removal`, retained) — A1 Certificate Reference, A1 Issuing Institution, A1 Validity Start Date, A1 Validity End Date, Posting Start Date, Posting End Date, Limosa Declarant Type / Identification / Contact Details, Foreign Posting Employer Name / Address / Country / Registration Number. Removed as rows, not blanked; 266 → **253** Country Fields rows. `A1 Certificate Held Indicator` kept — it governs whether Belgian contributions are due, not the filing. Propagated in the same pass: `dd_crosscheck_map.py` (12 `BE-NSSO-005` keys reclassified DD-shaped-but-descoped, so C2 does not dangle), `DD-CROSSCHECK-TABLE.md` regenerated, `be_dd_data_emp.py` / `be_dd_data_le.py` field definitions deleted so a rebuild cannot resurrect them, DD `Version Control` D14. **NARROWED, NOT CLOSED — 9 DD fields keeping a `BE-NSSO-005` reference were outside the decision's scope and are retained:** *Posted Worker Indicator* and *Multi-State Activity Indicator* (both have live non-Limosa consumers — DmfA Posted Worker, and the art. 13 applicable-legislation test of CCG Module 5.1), *Belgian Representative of the Foreign Employer* (CCG Module 2.1, a Belgian-side appointment independent of the filing), and 6 that appear Limosa-only on their face: *Place of Work in Belgium*, *Nature of the Posted Services*, *Posted Worker Working Time Schedule*, *Belgian Client Name*, *Belgian Client Enterprise Number*, *Belgian Client Address*. ~~Those 6 are the honest remainder of this finding and need the same keep-or-descope ruling.~~ **THE 6 RECEIVED THAT RULING ON 2026-08-17, SAME DAY, SECOND BATCH: descoped with the filing and DELETED as rows** (backup `BE-DD-001-v1.1.xlsx.bak-before-limosa-field-removal2`, retained; Country Fields **253 → 247**; DD fields 278 → **272**). Propagated in the same pass: `be_dd_data_emp.py` (3) and `be_dd_data_le.py` (3) definitions deleted so a rebuild cannot resurrect them — sources now yield 247, matching the workbook; `dd_crosscheck_map.py` 6 keys reclassified DD-shaped-but-descoped under a separate `LIM2` string so the record shows which pass retired which key; `DD-CROSSCHECK-TABLE.md` regenerated; DD `Version Control` D14, which also **supersedes** its own earlier sentence listing these 6 as "still owed" rather than rewriting it. **One judgement worth reading:** *Belgian Client Enterprise Number* also cited `Source: CCG Module 2.2` — the very pattern that saved *A1 Certificate Held Indicator* in the first batch — so Module 2.2 was opened and read rather than assumed. It cites the enterprise number only in its sample-inputs table for the generic `0nnn.nnn.nnn` format shared by every Belgian enterprise number; that justifies the field's format cell, not a consumer of the field. A format citation is not a consumer, so the field goes, while the A1 indicator's substantive Module 5.1 basis kept it. **THE 4 KEPT FIELDS ARE UNTOUCHED AND VERIFIED PRESENT:** *A1 Certificate Held Indicator*, *Posted Worker Indicator*, *Multi-State Activity Indicator*, *Belgian Representative of the Foreign Employer*. **This finding's DD half is now CLOSED, measured not asserted:** all 8 DD fields still carrying a `BE-NSSO-005` reference have a documented non-Limosa consumer, so zero Limosa-only fields remain. ~~**STILL OPEN, the last Limosa loose end in the repository:** `BE-WTC-001` wage type **BE-054** ends its narrative with *"Posted workers into Belgium also require a Limosa declaration before starting."* — unqualified as to who files, the same defect class the 1C pass fixed in CCG Module 10.1, plus a `selfcheck_be_wtc.py` anchor on the token *Limosa*. The sentence is legally true and does not assert the Belgian client files, so it does not contradict the ruling; it needs its own pass with a WTC backup and rebuild, on an artifact whose selfcheck already fails on a pre-existing *ORANGE populated*. Deliberately not absorbed into a DD pass — see `PROPAGATION-LEDGER.md` 1E.6.~~ **THAT PASS WAS RUN ON 2026-08-17 AND L-14 IS NOW CLOSED IN FULL. NO LIMOSA LOOSE END REMAINS IN THE REPOSITORY.** `Wage Type Catalogue!F355` was the sole changed cell: the closing sentence now qualifies who files — *filed by the foreign posting employer itself, or by the foreign self-employed person under art. 155, and never by the Belgian payroll client, so the declaration is out of scope for this payroll build; the only Belgian-side duty is the art. 141 check that it was made, an HR onboarding control rather than a payroll step* (613 → **1,049** chars, re-measured on the delivered workbook; the fix log's 1,073 is wrong by 24). The wording was **taken from the determination already in CCG Module 11.2 rather than freshly composed**, and its citation style matched to the rest of column F (pure-ASCII English legal-citation form, that column carrying zero non-ASCII characters). The `Limosa` token is retained, so the `selfcheck_be_wtc.py:131` anchor still binds and did not need moving. **Root-caused:** `be_wtc_data_part7.py:460`, the BE-054 generator tuple, carried the old sentence and was given the same text with generator-string-equals-workbook-cell asserted programmatically, so a rebuild cannot resurrect it. Backup `BE-WTC-001-v1.0.xlsx.bak-before-limosa-wording-fix` taken before any edit, MD5-verified, **retained**. **Verification:** `validate_workbook.py --artifact WTC` **PASS (blocker=0 major=0 minor=0)**; `selfcheck_be_wtc.py` re-run against a pre-edit baseline — **identical**, the same pre-existing *ORANGE populated (10 cells, A2..A11)* and **no new failure**; cell-level diff across all 6 sheets **`TOTAL DIFFS: 1`** (the F355 value, no style drift), and a zip-level diff showing one changed entry (`xl/worksheets/sheet2.xml`) with the embedded image and both comment/VML parts byte-identical — the edit was made inside the zip because an openpyxl round-trip would have silently dropped them. **LIMOSA IS NOW FULLY RESOLVED ACROSS ALL FIVE ARTEFACTS** — `scope_manifest.json`, `BE-SIR-001`, `BE-CCG-001`, `BE-NSSO-005-Limosa-Spec.xlsx`, `BE-DD-001-v1.1.xlsx` — **plus this WTC wording-precision fix**, on the statutory basis unchanged since the 1C ruling: *Programme Law (I) of 27 December 2006*, Title IV, Chapter VIII, **arts. 137, 139, 141 and 155**, MB/BS 28 December 2006, executed by the Royal Decree of 20 March 2007. See `PROPAGATION-LEDGER.md` 1E.6 and `scope_manifest.json` `_revision_history` v1.6. |
| L-15 | **No filing has ever been submitted through any channel.** No portal round-trip, no accepted declaration, no authority-returned error file. This is what holds every band below 95%. | A pilot submission per channel in the NSSO simulation and Belcotax test environments. **REGISTERED 2026-08-18** in `scope_manifest.json` `known_limitations` as out of reach: not resolvable through documentation research, and not attempted. New entry: it was **not in `known_limitations` at all** before this pass. It now names the closing condition from this row and records what this row already says - that this is the single item holding every accuracy band below 95%, because every figure and layout in the dossier is verified against a published specification and never against an authority's actual acceptance behaviour, which is where undocumented validation rules live. |
| L-16 | **French and German payslips not built.** Belgium has three language regions and the sanction for the wrong language is nullity of the document. | Two further payslip deliverables. Correctly disclosed in `known_limitations[5]` and payslip `A109`. **REGISTERED 2026-08-18** in `scope_manifest.json` `known_limitations` as out of reach: not resolvable through documentation research, and not attempted. It was already disclosed in `known_limitations[5]` and payslip `A109`, as this row states, but the entry was **unnumbered and carried no closing condition**. It now carries both, and states that the sanction for the wrong language is **nullity of the document**, so the gap is a compliance exposure rather than a convenience one. |
| L-17 | **Stage 11 SKILL not built** (§2.8). | A skill build with `references/` read from the current versions — DD v1.1, specs v1.2 — never a hardcoded v1.0. **CLOSED 2026-08-17.** `payroll-compliance-belgium` built under `08-skill/` - a thin router plus seven reference files - and built against the **current** artifact versions, DD v1.1 and specs v1.2, never a hardcoded v1.0, which is the condition this row attached to closing it. Registered closed in `scope_manifest.json` v2.0. |
| L-18 | **`shared/` is untracked in git.** The playbook, the failure log and the portal registry — the pipeline's compounding assets — have no version history. | `git add shared/`. **CLOSED 2026-08-18.** `git add shared/` run: **0 tracked files before, 32 after**, all staged as `A`. The playbook (`CCG-Playbook-Learnings.md`), the failure log (`country_failure_log.md`) and the portal registry (`country_portal_registry.md`) now have version history, along with the four JSON contract schemas, the report-spec template and the CZ/Spain/Mozambique/Tunisia reference workbooks. **Staged, not committed** - the commit is the owner's call. Registered closed in `scope_manifest.json` v2.0. |

---

## 8. What genuinely passed, and how it was measured

An audit that only lists defects is not calibrated. Each of these was measured this pass, not
inherited from a sibling review:

- **C32 across all seven artifacts: zero contradictions.** 41 work-bonus, GMMI and high-wage
  figures swept in both `1,234.56` and `1.234,56` renderings across CCG, WTC, PSL, DD, SIR, all
  nine specs and the manifest. Then a near-variant hunt on 13 load-bearing prefixes to catch a
  transcription slip: the only variants found (`2,935.00`, `2,935.01`, `3,408.87`) are withholding
  bracket boundaries and a worked-example product, not parameter drift.
- **The work-bonus parameter table is arithmetically sound** — all ten dated rows reconcile their
  own zero points, and the blue-collar × 1.08 relationship holds on every maximum and every
  coefficient pair (§2.2).
- **The WTC Global baseline is intact**: 300 of 300 codes, in baseline order, rows 2–301 — and the
  description-rewrite that round 1 read as a violation is what the CZ precedent does too (§2.3).
- **The 318 DD write-back landed**, verified column by column in the four spec files (§2.4).
- **All nine Report Spec filenames named in SIR §2.3 resolve to a file on disk.** None guessed.
- **The weakest figure in the dossier did not spread.** The CO2 multiplier's tier-B value appears in
  the CCG and nowhere else; four downstream artifacts reference it by its selector (the vehicle order
  date) rather than by its value. Measured across the whole corpus, not assumed from the SIR sweep.
- **16 of 17 payslip `custom` tokens resolve** to a real DD field; 13 payslip wage-type codes still
  join to the WTC after two WTC rebuilds.
- **The SIR's house-style insulation held again.** Zero `BE-DD` references, so the v1.0 → v1.1
  rename that touched 61 spec citations left the SIR untouched and dangling-free. The Stage 6
  Definition of Done — cite box and block numbers, never DD internal codes — is doing exactly what
  it was written to do, and it is the strongest structural decision in the dossier.
- **The v1.1 manifest fix flags its own incompleteness inline**, in the three entries it touched
  but could not resolve. That is the correct way to leave a partial fix.
- **L3 re-verified from the script body, not from its documentation.** A naive `\bC[0-9]{1,2}:`
  grep of `mercans_pipeline_v2_9.sh` returns 23 ids and would have had me contradict the prior
  sweeps. The discriminating test is the deterministic blocks' own reporting shape,
  `return ('Cnn', …)`, which returns **18** — C1, C8, C11, C12, C20–C33, exactly L3's claim. C13,
  C15, C16, C18, C19 are prompt bullet text at lines 898–902. **The prior sweeps were right and my
  first grep was wrong**; recorded because "never trust a count you did not take yourself" has to
  include one's own.

### A method note on the docx extraction

Two prior sweeps deduplicated merged table cells with `id(cell._tc)`; lxml recycles proxy-object
addresses, so cells vanished non-deterministically and one sweep nearly filed *"325.10 is absent
from the CCG"* against a guide that names it five times. I did not reuse that method or its
scratch output. `_qa/x10/dump.py` keys on `tree.getpath()` per paragraph element, and every table
cited in a finding here was dumped and read in full before the finding was written.

---

## 9. Two findings against the tooling, both measured

Recorded here because they gate every future country, not just Belgium.

**T-01 — C29, the lint named "residual-marker lint across ALL artifacts", covers four of seven
artifacts and cannot see inside a Word table.** From `mercans_pipeline_v2_9.sh` lines 2417–2462:

- Scan targets are `01-ccg`, `04-reports-spec`, `02-wtc`, `05-data-dictionary`. **Not**
  `03-statutory-integrations` (the SIR), **not** `06-payslip`, **not** `scope_manifest.json`.
- The CCG is read as `'\n'.join(p.text for p in Document(str(ccg)).paragraphs)` — **paragraphs
  only**. Every table cell in the CCG is invisible to it. The CCG's one live `NOT FOUND` is inside
  a table.
- The marker list is `TODO`, `TBD`, `FIXME`, `VERIFY No`, `[placeholder]`, `[CHECK]`, `[?]`, *"to
  be confirmed"*, *"to be verified"*. It does **not** carry `NOT FOUND`, `PENDING`, bare
  `placeholder`, or `XXX` — and `\bXXX\b` cannot match `XXXXX`, which is why 18 payslip cells pass.

Measured consequence: the deterministic lint returns PASS over a corpus carrying **848 `NOT FOUND`
cells in the specs, 36 in the DD, 5 `PENDING` in the WTC, 1 in the CCG and 2 in the payslip.**

**T-02 — C18, the one check specified to validate the scope manifest against the specs, is prompt
text and has never run.** `mercans_pipeline_v2_9.sh:901` reads *"C18: every filing in
scope_manifest must have a Spec file"* — a bullet inside a builder prompt, with no deterministic
block. `scope_manifest` appears 33 times in the script and **no deterministic check validates it
against any artifact.** That is precisely why the manifest is the one BE deliverable that went
five days without a correction: nothing was ever pointed at it. C18 as specified would have caught
BE-X10-001, BE-SCOPE-014 and the form-325.10 error. So would C9, the WTC tax-code check, which
would have caught BE-X10-002 — and C9 appears nowhere in the script at all, not even as prompt
text.

---

## 10. Where to spend the next pass

Ranked by value per unit of effort, which is not the same as by severity:

1. **BE-X10-003** — five cells in one sheet. Pure deletion of a false statement, no research.
2. **BE-X10-009** — 220 cells, one find-and-replace per spec, and the correct replacement text is
   already written in the Version Control cell above them.
3. **BE-X10-005** — three cells, and the DD already holds the correct answer.
4. **BE-X10-001** — seven outbound entries. The SIR has already done the analysis; this is
   transfer, as BE-SCOPE-001 was.
5. **BE-X10-004 and the whole of §7** — one country-level limitation register that is the **union**
   of the SIR's G1–G27, the DD's 36, the specs' 848, the CCG's 1, and L-01…L-18 above. This is the
   largest job on the list and the one that closes the most findings at once: BE-X10-004,
   BE-X10-006, BE-SCOPE-008, and L-05, L-06, L-07, L-10, L-13.
6. **BE-X10-002** — needs a decision (two tax codes on one wage type, or two wage types), not
   research. The Belcotax spec has already specified the answer.

**BE-X10-022, BE-X10-007 and BE-X10-008 should be routed to `compliance-source-hunter`, not to the
builder.** BE-X10-022 needs the NSSO instruction or the greening law article for the multiplier —
not a fourth vendor agreeing with the other three.
Both are about which instrument, on which date, governs the work-bonus parameters — and this pass
does not research. Guessing at the pegging relationship would be worse than the contradiction.

---

*Round 1 of 3 for the cross-artifact gate. Nothing in this pass was applied. Findings, evidence,
locations and expected values in `_qa/REGRESSION-BE-XCHECK-r1.json`; scripts and dumps in
`_qa/x10/`. Propagation in `PROPAGATION-LEDGER.md`. C-check results and the deterministic-vs-manual
split in `07-qa-crosscheck/handover_status.md`.*
