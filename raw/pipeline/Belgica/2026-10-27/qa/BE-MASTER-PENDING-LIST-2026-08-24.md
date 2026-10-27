# BE-compliance — MASTER PENDING LIST

**Compiled** 24 August 2026 · **Status** read-only compilation, no artefact was edited to produce it
**Supersedes as the working list** the "Open items for Wallisson" sections of all five sessions of
`BE-FIX-LOG-2026-08-21.md`, the "Issues still open" table of `BE-QA-REPORT-FINAL-2026-08-24.md`,
`handover_status.md` §4, and the per-artifact review logs' own trailing open-item paragraphs. Those
files remain the evidence; this file is the index.

---

## How to read this

Every item has an **ID**, a **location**, a **current state measured or quoted**, and a
**resolution path**:

| Path | Meaning |
|---|---|
| **(a)** | Solvable by more agent work using only what is already on disk. No new information needed. |
| **(b)** | Blocked on a document that is **not** on disk. The document is named. Once obtained, it becomes (a). |
| **(c)** | No document can resolve it — it needs a direct question to an authority, an owner's scope decision, a per-client data contract, or a live pilot submission. |

**Measured live in this session** is marked ⚙. Everything else is quoted from the source file named
and has **not** been independently re-measured here — where a document's claim is old enough to be
suspect, that is said explicitly.

**Counts.** **71 open items**, ⚙ counted from the IDs in this file. Roughly **30** are (a),
**20** are (b) and **21** are (c) or an owner's decision. §1 lists **11** places where two sources on
disk disagree.

**The item count understates the work in two places, deliberately.** `MP-SIR-01` is one line covering
**26 SIR gaps**, and `MP-DD-04` is one line covering **12 mapper blocks**. Both are bundled because
they close as batches — 3 letters and 1 acquisition run respectively — not one at a time. Everything
else is one line per thing that has to be decided or done.

---

# §1 — WHERE TWO SOURCES DISAGREE

These are listed first because acting on the wrong one of a pair wastes a session. None is resolved
here; each names both sides and, where a live measurement settles it, gives it.

### D-01 · The final QA report's verdict is stale by ~40 minutes
`BE-QA-REPORT-FINAL-2026-08-24.md` (written 19:57) concludes **"NOT ready for handover. One MAJOR
blocks it"** — ISSUE-B, Days Justification. Session 4 of `BE-FIX-LOG-2026-08-21.md` (appended 20:37)
**fixed ISSUE-B**, and also ISSUE-C and ISSUE-D. ⚙ Verified live: `BE-NSSO-002!'Field Options'`
r154–161 now carries codes **1–7 plus a closing note**, and the SIR carries **zero**
`BE-CCG-001 v1.0` strings. **The report's MAJOR is closed; its readiness verdict has not been
re-taken.** Nothing on disk records a post-fix Stage-10 verdict. → see **MP-PROC-01**.

### D-02 · `handover_status.md` is a 17 August snapshot presented as current
It states **"6 blockers and 11 majors are open"**. ⚙ Of its 6 blockers, at least **three are now
closed**: BE-X10-002 (WTC box 360 — `Wage Type Catalogue!G304` now reads **`284; 360`**, dual-coded),
BE-X10-004 (DD marker count), BE-X10-022 (CO2 multiplier, closed with a primary source by its own
inline update). BE-X10-012 (Stage 11 skill) is likewise closed — ⚙ `08-skill/payroll-compliance-belgium/`
holds `SKILL.md` + 7 reference files. **Do not work this file's §4 list without re-testing each row.**

### D-03 · `scope_manifest.json` says L-01 and L-04 are still open; `BE-QA-REPORT.md` says both are closed
`known_limitations[16]` (18 Aug) lists **L-01 (no legal-basis-register.csv)** and **L-04 (P5 has no
checklist)** among "STILL OPEN … pipeline process debt". `BE-QA-REPORT.md` §7 rows L-01 and L-04 both
read **CLOSED 2026-08-18**. ⚙ **The QA report is right**:
`00-official-sources/legal-basis-register.csv` exists with **63 rows on the 20-column contract**, and
`PROPAGATION-LEDGER.md` §0 carries the P5 checklist. Same paragraph is also stale on **L-03** (tier)
— ⚙ `scope_manifest.json.tier` and `_pipeline/build-manifest.json.tier` both exist. Only **L-02** of
that group survives, and only partly (see MP-PROC-03).

### D-04 · The DD's `NOT FOUND` marker count: 36 (manifest) vs 21 (live)
`scope_manifest.json known_limitations[7]` certifies **"exactly 36 cells … 18 in column C (Code) and
18 in column F (English Description), over 19 code rows in 16 mapper blocks"** — explicitly measured
against **`BE-DD-001-v1.1.xlsx`**. ⚙ Live count on **v1.3**: **21 cells — 9 in Code, 12 in English
Description**, across **12 blocks**. The v1.3 promotion closed 15 of them. The manifest entry names
v1.1 in its own text, so it is not lying — but it is the registered figure and it is 71% too high.
→ **MP-SCOPE-02**.

### D-05 · `BE-DD-002` — 318 spec System Mapping cells
`DD_REVIEW.md` records BE-DD-002 as **"NOT addressed … Still open"**, evidenced by git history.
`REPORTS_SPEC_REVIEW.md` records the same defect as **BE-RSPEC-002, "FIXED and verified"** — 318
cells filled, 538/538 reconciled. The specs review is the later document and its arithmetic
reconciles. **Treat as closed; `DD_REVIEW.md` was never updated.**

### D-06 · `TAX_ENGINE_FIX_APPLIED.md` §7(c) and `CCG_CONTENT_REVIEW.md`:442 both say the EUR 0.19 error was NOT touched
⚙ It **was** fixed, and fixed consistently. Live in both `modules/m09_termination.md` and
`BE-CCG-001-v1.1.docx`: `697.42`→**0 occurrences**, `697.61`→2; and all three dependent figures moved
with it (`606.53`→`606.34`, `18,588.53`→`18,588.72`, `28,685.12`→`28,684.93`). **Closed. Both
documents are stale on this row.**

### D-07 · `TAX_ENGINE_FIX_APPLIED.md` §7(b) is half-stale
It says `m06_tax.md:219` "currently carries a known-wrong figure" (30% for the inbound-taxpayer
regime) and warns **"do not rebuild the docx from the modules"**. ⚙ The figure is now **35%** in the
module and in the docx, `Up to 30%` returns **0 hits**, and session 3 of the fix log proved a
rebuild reproduces v1.1 with **0 differing units out of 4,814**. The rebuild ban is lifted.
**But the second half of §7(b) is still live** — the same row still asserts the ONSS non-alignment
that `CCG_CONTENT_REVIEW.md` downgraded to *"genuinely unresolved — DO NOT EDIT until resolved with
a primary source"*. → **MP-CCG-01**.

### D-08 · `BRACKET_INVESTIGATION.md` §6 and `CHILDREN_SUPPLEMENT_INVESTIGATION.md` list findings that are now fixed
⚙ Live: the missing 4th-band cumulative constant **20,320.38** is present (2 occurrences); the three
one-cent F-total errors are gone; the 13.92-vs-12 inconsistency is resolved (`m08_leave.md:147` now
uses 13.92 → 47.44%); and the CCG no longer states the disputed child figures 2,030 / 5,230 / 11,720
at all — it uses the **Annex III nr. 38 flat-reduction table** instead. The investigations were never
annotated. **Closed; do not re-open from those files.**

### D-09 · SIR OUT-10 `product_mapping_required` — SIR says false, manifest says true
`scope_manifest.json integrations.outbound[8]._flag_note` states the contradiction inline and does
not resolve it. Neither side has moved. → **MP-SIR-03**.

### D-10 · The DD passes one gate and fails another, and only one is usually quoted
⚙ `validate_workbook.py --artifact DD` → **PASS**. ⚙ `verify_be_dd.py` → **FAIL C1**, 8 unclassified
spec fields. Session 2's STEP 5 proved the C1 failure pre-existing by A/B against archived v1.1;
session 5 re-confirmed it byte-identically. Verification tables that quote only the validator read as
"the DD passes". → **MP-DD-02**.

### D-11 · `WTC_REVIEW.md` requires the YTD columns to be empty; `handover_status.md` BE-X10-010 calls their emptiness a MAJOR
⚙ Live: `YTD Load` and `YTD Remarks` are populated on **exactly one** of 359 data rows — **row 360,
BE-059**, the wage type added on 21 August. So the artefact now satisfies neither reading. This needs
one decision, not two fixes. → **MP-WTC-02**.

---

# §2 — DATA DICTIONARY · `05-data-dictionary/BE-DD-001-v1.3.xlsx`

## (a) — solvable with what is on disk

### MP-DD-01 · Two more `Additional Notes` cells still describe a held domain as unheld
**Location** `'Country Fields'` column **W**, rows **38** (`Remuneration Method`) and **67**
(`Apprenticeship Type`).
**State** ⚙ Both read *"Domain is defined by reference to an NSSO annexe that is not held."* ⚙ Both
domains are fully held in `'Country Option Mappers'` — `Remuneration Method` at rows 176–178
(**3 codes**, full four-column content, **no `NOT FOUND` remainder row**) and `Apprenticeship Type`
at rows 169–173 (**5 codes**, every one with a description, no remainder row, including the
quarter-2019/4 recoding history).
**Why it is here** This is the identical defect that session 5 fixed in five cells (r22, r23, r49,
r64, r66). Session 4's list of five was **not complete**; these two were found during session 5's
full column-W sweep and deliberately left untouched under that brief.
**Also checked and correct — do not "fix" it**: r36 `Work Schedule Days Indicator` says Annexe 34 "is
not held", and its mapper block (row 181) is a single `NOT FOUND` placeholder recorded as a
*confirmed dead end after extensive alternative-source research (20 Aug 2026)*. The note is true.
**Path (a)** — two-cell edit, same shape as the five: point at the mapper block, do not restate codes.

### MP-DD-02 · `BE-DD-001-v1.3` does not pass its own verifier
**Location** `05-data-dictionary/verify_be_dd.py`, check **C1**.
**State** ⚙ `FAIL C1 — 8 spec fields are not classified` into any of DD/TX/CALC/SYS:
`FEDRIS-001` rows 106 `Environment At Accident Moment`, 110 `Type Of Work`, 114 `Activity At
Accident Moment`, 115 `Which Events`, 146 `How Injured`, 198 `Subdivision Usage`; `NSSO-004` rows
154 `Nature Advantage Starting Date`, 155 `Nature Advantage Ending Date`. Everything else passes
(272 DD fields, 1183 spec rows classified, 0 DD-bucket fields missing, 0 orange populated, 0 C29
markers, 0 WTC collisions). Pre-existing — identical output against archived v1.1.
**Note** Six of the eight are FEDRIS accident-circumstance fields whose code tables are themselves a
`NOT FOUND` (see MP-RSPEC-05), so the classification question and the source question may be the same
question.
**Path (a)** — either classify the eight in `dd_crosscheck_map.py`, or establish that the verifier's
expectation is wrong and re-scope C1. Neither has been diagnosed.

### MP-DD-03 · `'Version Control'` changelog holes
**Location** `'Version Control'` cells **D15, E15, F15** and **F16**.
**State** ⚙ Row 15 is version **1.2**, effective 2026-08-20, and has **no Change Description, no
Status and no Updated By**. Row 16 (v1.3) is `Released` but its **Updated By is empty**, where rows
13 and 14 both credit Wallisson Gomes. This is QA-FINAL **ISSUE-F** and fix-log session-2 open item
3, unchanged since.
**Path (a) for F15/F16 · (c) for D15** — nobody has a source for what v1.2 changed. Session 2
declined to guess and said so; that judgment still holds. D15 needs the person who cut v1.2.

## (b) — blocked on a document not on disk

### MP-DD-04 · 21 residual `NOT FOUND` cells on `'Country Option Mappers'`
⚙ Measured live on v1.3: **9 in the Code column, 12 in English Description, over 12 blocks.** Each
block carries its own closing note naming what would close it. Registered collectively as **L-10**.

| Block | Rows | What is missing | Document needed |
|---|---|---|---|
| Contract Duration Type | 54–57 | **4 of 6 codes have no code value.** NSSO zone 00885 publishes only 0 (indefinite) and 1 (fixed term); which of the two covers *Clearly defined work*, *Replacement*, *Student* and *Flexi-job* is unknown | **(c)** — NSSO. The manifest's `option_mapper_scope.contract_duration_type._open_item` says so outright |
| NSSO Worker Status | 81, 82 | **14 of an unknown larger total.** Current annex is AN2015-1-NL21, 3 pages; the held 14 come from an AVIQ mirror of circulars 997/56 and 997/73. Code `VA` has no description at all | **(b)** — NSSO Annexe 21, current 3-page edition |
| NSSO Worker Code | 97 | **12 of 100+.** 17-page annex AN2024-3-NL2. Codes 023, 406, 407, 601, 608, 609, 671, 672, 676, 711, 840, 841, 848, 849, 879, 883 are referenced by number elsewhere but have no description | **(b)** — NSSO Annexe 2, v2024/3 |
| NSSO Employer Category | 100 | code value `NOT FOUND` | **(b)** — NSSO employer-category annex |
| Joint Committee Number | 119 | **16 of 164** (SPF Emploi counts 98 main + 66 sub as at 1 Jan 2026) | **(b)** — SPF Emploi joint-committee register |
| Work Reorganisation Measure | 158 | descriptions for codes 506–510, 515, 516, 517, 531, 541–546, 599 — confirmed valid, text not captured | **(b)** — NSSO Annexe 44 |
| Employment Promotion Measure | 165, 166 | **code 5's description is truncated in the source snippet** (AN2007-1-Fr35); the domain's upper bound is inferred from the annex being one page, not sourced | **(b)** — NSSO Annexe 35 |
| Work Schedule Days Indicator | 181 | **the whole domain.** Recorded as a *confirmed dead end after extensive alternative-source research (20 Aug 2026)* | **(b)** — NSSO Annexe 34, TechLib only |
| Tax Collection District and Office | 686 | code value | **(b)** — *Register van ambtsgebieden* (see MP-RSPEC-04) |
| Payment Category Purpose | 788 | code value | **(c)** — NSSO or the client's bank |
| Service Exemption Indicator | 940 | **the comparison operator before "20%" is an unrenderable control character** in the held source, so whether the threshold is *at least* or *at most* 20% cannot be stated | **(b)** — a clean copy of the source; flagged since the Stage-8 alignment patch |
| Legal Basis for Part-Time Work With Benefit Retention | 1033 | code value | **(b)** — NSSO/LOIC glossary |

### MP-DD-05 · Two widened domains reach no specification, and one has no DD field
Fix-log session-4 open item 5, ⚙ still true. `Work Reorganisation Measure` and `Employment Promotion
Measure` are bound to DD fields and quoted by spec column O, but **no spec publishes their codes**;
`Health Insurance Fund Code` (79 codes) has **no `Country Fields` binding at all** — it is reached
only from `ID Information`. 3 of the 9 widened domains currently benefit no downstream artefact.
**Path (a) or a decision** — the fix is cheap; whether it is wanted is not an audit call.

---

# §3 — WAGE TYPE CATALOGUE · `02-wtc/BE-WTC-001-v1.0.xlsx`

## (a)

### MP-WTC-01 · `'Form Reference Guide'` is still a 2-row delegation stub
⚙ `max_row = 2`. Its five headers (`Wage Type Name in English`, `Statutory form / report`, `Report
Spec reference (row no.)`, `Data Dictionary field`, `Status`) describe a per-form index; row 2 is one
blanket delegation row. Its **content is now correct and current** (A2 = 359, B2 names the per-spec
versions, D2 points at v1.3, E2 says *"CROSSWALK MAINTAINED ELSEWHERE — not pending"*). Only the
structure is unbuilt. QA-FINAL **ISSUE-7**, `handover_status` **BE-X10-003** (content half closed).
**Path (a) or accept** — build the 9-row per-form index, or record the stub as a design decision. It
has been carried as "optional" through four sessions without either being done.

### MP-WTC-02 · YTD columns: populated on exactly one row of 359
⚙ `YTD Load (Yes/No)` (col S) and `YTD Remarks` (col T) are populated **only on row 360, BE-059**.
Both are orange columns. `WTC_REVIEW.md` verified their emptiness as *"as required"*;
`handover_status` **BE-X10-010** calls the emptiness a MAJOR and notes *"a fifth take-on field
missed"*. See **D-11**.
**Path — decision first, then (a).** Either the orange convention governs and row 360 should be
cleared, or take-on data is owed and 358 rows are missing it. Do not fix before ruling.

### MP-WTC-03 · `selfcheck_be_wtc.py` fails on `ORANGE populated`
⚙ Live: **1 failure**, `('A', 2..11)` — column A `Mercans Code`, 10 cells reported. Documented as
by-design (the CZ precedent populates its own orange Mercans Code column; orange signals dev-team
ownership, not mandatory emptiness) and stated in `WTC!'Version Control'!C28`. Column A had to be
populated for `diff_wtc_baseline.py` to join at all.
**Path (a)** — amend the self-check's expectation so a green run means something, or leave it and
accept a permanently-red gate. It has been "the single documented pre-existing failure" for eight days.

### MP-WTC-04 · `diff_wtc_baseline.py` reports `BASELINE VIOLATED` by design
`renamed=299` — inherent to any properly localised country catalogue (the CZ reference template
itself fails the same check at 241/59/148). `kept 300, missing 0, added 59` is the real result.
**Path — a toolkit change, not a Belgium fix.** `WTC_REVIEW.md` recommends the verdict rule treat
MISSING/duplicates as the blocker and RENAMED as advisory. Owner: whoever owns
`mercans-artifact-toolkit`. Not actionable inside this dossier.

## (b)/(c)

### MP-WTC-05 · BE-059's legal citation is at article level, not paragraph level
Sourced to *Article 19 of the Royal Decree of 28 November 1969* **via the CCG**, which says
"Articles 19 and following" and names no paragraph.
**Path (b)** — the Royal Decree of 28 November 1969 text itself. Fix-log session-1 open item 4.

---

# §4 — CCG · `01-ccg/BE-CCG-001-v1.1.docx` (+ `modules/*.md`)

## (a)

### MP-CCG-01 · The ONSS non-alignment assertion is stated as fact but was formally downgraded to unresolved
**Location** ⚙ `modules/m06_tax.md:223` and the matching docx row — *"Note: NSSO/ONSS did not adopt
the same reform — for social security purposes the prior EUR 75,000 minimum and EUR 90,000 annual cap
… still apply."*
**State** `CCG_CONTENT_REVIEW.md` §"Downgraded to genuinely unresolved" records that a later source
(Andersen, May 2026, citing the same 1 April 2026 circular) **states the opposite**, and rules
*"no edit will be made to any module (2, 5, 6, 7, 11) on this point until the actual circular text or
ONSS's current published guidance is read directly."* The module nonetheless asserts one side.
**Path (b)** — Circulaire 2026/C/51 of 1 April 2026, or ONSS's current published guidance. Until
then the CCG is asserting a claim its own review log forbids asserting.

### MP-CCG-02 · The fiscal work bonus percentage: the CCG contradicts itself across two modules
⚙ `m07_deductions.md:40` reasons that **63%** on component B *"is the one that governs this guide's
income year"* if the reform is enacted, and :38 records the two July 2026 texts as **enacted** while
noting the specific figures were not re-confirmed against them. ⚙ `m12_examples.md:5, :126, :230`
compute every worked example at **52.54%** with no caveat.
**Path (b) then (a)** — the actual Annex III nr. 46.2.2 / Article 154bis wording introduced by the
Royal Decree of 30 July 2026. Then either recompute m12 E4 and E6 or add the caveat there too.
Recorded as `TAX_ENGINE_FIX_APPLIED.md` §5 item 2, unchanged.

### MP-CCG-03 · Arrears may belong on Annex III nr. 58, not nr. 53
⚙ Live: `m09_termination.md:313` still says a retroactive increase relating to a previous year is
*"taxed at the exceptional-payment percentage"*, and `m04_compensation.md:295` routes overtime
relating to a previous year to *"the exceptional-payment rules of Module 9.2"*. `BRACKET_INVESTIGATION.md`
§7 rates the nr. 58 reading **Probable, not confirmed**: nr. 58 is headed *Achterstallen*, but nr. 53
does not exclude arrears by name (it excludes only *opzeggingsvergoedingen*, which is why the
severance half was fixed). **~14 WTC arrears wage types** carry the same "exceptional-remuneration
percentage × 13.92" wording.
**Path (b)** — the Annex III text at nrs. 53 and 58. `TAX_ENGINE_FIX_APPLIED.md` §5 item 1a calls
this *"the highest-value remaining item"*. It is the largest unactioned money item in the dossier.

## (b) — named documents

### MP-CCG-04 · Overtime relief raised ceilings not stated
⚙ `m04_compensation.md:286`, `m07_deductions.md:48`, `m05:355`, `m06:108` all state **180 hours** and
say only that *"higher ceilings apply in construction … and in the hotel and catering sector"*. The
specific **360** (hotel) and **280** (qualifying road/rail) ceilings from Article 2 of the Royal
Decree of 24 July 2026, retroactive to 1 January 2026, appear nowhere. ⚙ `"280 hours"` returns **0
hits**. (The one `"360 hours"` hit is the *voluntary overtime quota* at m04:277 — a different rule.
Do not conflate them.)
**Path (b)** — Royal Decree of 24 July 2026. `ALLOWANCE_INVESTIGATION.md` §5.4(c).

### MP-CCG-05 · Legal-basis citation refresh not applied
⚙ `"24 July 2026"` returns **0 hits** across `modules/`. Both `ALLOWANCE_INVESTIGATION.md` §5.3 and
`BRACKET_INVESTIGATION.md` §5.5 call for the **Royal Decree of 24 July 2026** to be added alongside
the 11 December 2025 citation, with nrs. 31 / 32 / 38 cited specifically. The **Law of 15 July 2026**
half *was* applied (⚙ 6 hits). Carried as `TAX_ENGINE_FIX_APPLIED.md` §5 item 6.
**Path (b)** — the decree; then (a).

### MP-CCG-06 · Child relief on exceptional remuneration (Annex III nr. 55) is absent
⚙ `"nr. 55"` returns **0 hits**. `CHILDREN_SUPPLEMENT_INVESTIGATION.md` §6(c) flags this as a
**potential systematic over-withholding on bonuses** — the nr. 55 percentage table is the mechanism
by which family situation reduces the exceptional-payment rate, and m04/m08 model no such reduction.
**Path (b)** — Annex III nr. 55.

### MP-CCG-07 · Scale II and the spouse thresholds are unverified
Annex III **nrs. 33, 40.2, 40.3**. ⚙ `"nr. 40"` returns **0 hits**.
`CHILDREN_SUPPLEMENT_INVESTIGATION.md` §6(d). **Path (b)** — Annex III.

### MP-CCG-08 · Watch item — the Annex III amendment for the reformed allowance
`ALLOWANCE_INVESTIGATION.md` §5.4 / `TAX_ENGINE_FIX_APPLIED.md` §5 item 8: the Royal Decree amending
Annex III for the reformed basic allowance had **not landed** as at 14 August 2026. When it does,
re-verify against the decree and **do not use the projected 11,540**. ⚙ The CCG currently runs on
**11,170** (21 occurrences) with **11,550** appearing 4 times as the assessment-side counterpart.
**Path (c) then (b)** — nothing to do until the decree is published.

### MP-CCG-09 · The two-figure explanation (11,170 vs 11,550) recommended but never written
`ALLOWANCE_INVESTIGATION.md` §7.3 recommends stating explicitly that withholding runs on 11,170 and
assessment on 11,550 with the difference refunded. `TAX_ENGINE_FIX_APPLIED.md` §5 item 7 records it
as deliberately not added, being new explanatory content.
**Path (a)** — a decision to add it, then write it.

### MP-CCG-10 · ISSUE-A — the WTC configures a rate the CCG never states
⚙ `38.07%` (mobility-budget pillar-3 contribution) is present at `BE-WTC-001!'Wage Type
Catalogue'!F323` and `!'Global WTC Coverage'!E37`, and returns **0 hits** in both
`BE-CCG-001-v1.1.docx` and `modules/`. QA-FINAL **ISSUE-A**.
**Path (b)** — the legal basis for the pillar-3 rate; then add it to CCG Module 7.2.

## (c)

### MP-CCG-11 · Items the content review flagged and never verified
`CCG_CONTENT_REVIEW.md` carries a standing list of *"flagged — not yet independently verified"*
items, none of which has been revisited. Grouped, they are: wage-moderation contribution parameters
(5.67% / 7.48% cap, 4.27% / 5.12% reduced); social work-bonus limits and maxima; CO2 solidarity
constants F = 768/600/990 and the monthly floors 33.93 / 42.34; flexi-job ceiling EUR 18,440;
inbound-taxpayer eligibility specifics (60-month lookback, 150 km test, 5+3 year duration);
garnishment dependent-child resource thresholds (4,015 / 5,799 / 7,352); KBO/BCE and NSSO
check-digit formulas; document retention periods; community-day dates; the 15 December 2025
replacement-day deadline; JC 200's 2.21% January 2026 indexation; GMMI baseline 2,154.11; the
special-SS-contribution band formulas; the exceptional-payment band table; the 2025 corrective-filing
deadlines; the *Chefquet* legislative status; and *"variable pay averaged over the 12 months
preceding dismissal"*.
**Path (b) mostly, some (c)** — each needs its own primary source. The review is explicit that these
are **unverified, not wrong**. Treat as a research backlog, not a defect list.

### MP-CCG-12 · The 13.92 annualisation factor is a Mercans convention carried as if statutory
⚙ `legal-basis-register.csv` row **BE-PIT-017**, **tier B**, states it plainly:
*"Normal annual gross remuneration = current monthly gross × 13.92 … **THIS IS NOT A STATUTORY
FIGURE.** Annex III nr. 53 …"*. ⚙ 13.92 appears **13 times** across `modules/`, driving the band
selection in several worked examples. One of only **two tier-B rows** in the whole register
(the other, BE-PIT-006, is registered *"so that it can be rejected"*).
**Path (c)** — either confirm the administrative practice with FPS Finance or record it explicitly in
the CCG as a Mercans convention. A tier-B number is currently load-bearing in operative content.

---

# §5 — REPORT SPECS (9) · `04-reports-spec/`

## (a)

### MP-RSPEC-01 · ISSUE-C residual — three specs still assert Annexe 6 is unavailable, in the Example column
**Location** ⚙ `BE-NSSO-001!'Dimona Spec'!K56`, `BE-NSSO-002!'DmfA Spec'!K58`,
`BE-NSSO-003!'DmfA Modification Spec'!K58` — all three the **`Example`** column of the
`Activity With Risk` (zone 00041) row.
**State** ⚙ All three read `NOT FOUND - code list is NSSO Annexe 6` (the Dimona one adds *"not held
in 00-official-sources"*). On the **same row**, column L already cites
`BE-DD-001-v1.3 — 'Activity With Risk' (Country Fields)`, and ⚙ that DD block holds **all 18 codes**
and records itself *substantially complete* against the live NSSO administrative instructions.
**Why it survived** Session 4's FIX B swept the `Field Options` sheets and column O; it did not
sweep the `Example` column of the specification sheets. Same defect family as ISSUE-C, one column over.
**Path (a)** — three cells; the DD supplies a real example code (e.g. `001`).

### MP-RSPEC-02 · ISSUE-G — all nine specs are still Status `Draft`
⚙ Measured on every spec's `'Version Control'`: FEBELFIN, FIN-001, FIN-002 → `1.0/1.1/1.2` all
**Draft**; FEDRIS, NSSO-001/002/003/004 → `1.0/1.1/1.2/1.3` all **Draft**; NSSO-005 →
`1.3 [Descoped]`, which is correct. The DD says `Released` and the CCG is promoted.
QA-FINAL **ISSUE-G**, whose fix was gated on ISSUE-B closing — ⚙ **ISSUE-B is now closed**, so the
gate is open.
**Path (a)** — set the current-version Status to `Released` on the eight in-scope specs.

### MP-RSPEC-03 · ISSUE-5 — three green `NO` fills in the Limosa scope summary
⚙ Live: `BE-NSSO-005!'Payroll Scope Summary'!B15`, `B17`, `B18` answer `NO` and are filled
`FFC6EFCE` (green) instead of `FFFFC7CE` (red). ⚙ Every other `NO` in the sheet (B11, B12, B13, B16,
B23) is correctly red. ⚙ These raise **3 of the 11** `verify_specs.py` errors.
**Path (a)** — three fill changes. Confirmed open and unfixed across four consecutive sessions.

### MP-RSPEC-04 · `verify_specs.py` sits at 11 errors, and 8 of them may be a stale check
⚙ Live: **11 ERRORS — C6 × 8 + C7 × 3**, exactly the documented baseline.
**C6 × 8** = *"Version Control lacks the Stage 4 / Data Dictionary pending note"* on all specs except
FEBELFIN. QA-FINAL's assessment: *"Stage 4 is delivered and every citation resolves — the check, not
the file, is stale."* **C7 × 3** = MP-RSPEC-03.
**Path (a)** — retire or re-scope the C6 assertion. Until then no spec run can ever be green, and a
real regression would hide inside a familiar 11.

### MP-RSPEC-05 · Residual `NOT FOUND` option rows: 44 across the nine specs
⚙ Measured live on the `Field Options` sheets: FEBELFIN 5, FEDRIS 4, FIN-001 3, FIN-002 0,
NSSO-001 2, NSSO-002 12, NSSO-003 2, NSSO-004 10, NSSO-005 6. QA-FINAL counted 39 before session 4's
edits added closing-note rows. Most are **genuine external dependencies**, not defects — the NSSO
TechLib annexes (2, 3, 4, 7, 8, 12, 34), the WECH/ZIMA/TWCT glossaries, the Limosa web-only channel,
and the Finprof enquiries. They are itemised under **(b)/(c)** below and in MP-DD-04.

## (b) — named documents

| ID | Location | Missing | Document |
|---|---|---|---|
| **MP-RSPEC-06** | `BE-NSSO-002!'Field Options'` r8, r16 | Remuneration Code, Service Code — whole domains | NSSO **Annexe 7** (*Codification des rémunérations*) and **Annexe 8** (*Codification des données de temps*), TechLib |
| **MP-RSPEC-07** | `BE-NSSO-003!'Field Options'` r11, r26 | Attestation Status (00110) domain | NSSO, or the **DmfA XSD** from the TechLib |
| **MP-RSPEC-08** | `BE-NSSO-003!'Field Options'` r14 | Annexes **3, 4, 7 and 8** still missing (Annexe 2 became partial, so the row was corrected `NOT FOUND` → `PARTIAL` in session 4) | the four NSSO annexes |
| **MP-RSPEC-09** | `BE-NSSO-004!'Field Options'` r6, r13, r14 | Risk Identification full code table; WECH unemployment scenario 1; WECH scenarios 2, 4 and others | NSSO **Annexe 12**; the **WECH scenario glossaries**, TechLib |
| **MP-RSPEC-10** | `BE-FEDRIS-001!'Field Options'` r59 | Accident circumstance, location and injury code tables — the six fields that also fail DD C1 (**MP-DD-02**) | the **FEDRIS annexes** referenced per zone in column O |
| **MP-RSPEC-11** | `BE-FIN-001!'Field Options'` r60 | Secretariat Code domain | the **register of recognised social secretariats** (NSSO / FPS Social Security) |
| **MP-RSPEC-12** | `BE-FIN-001!'Field Options'` r68 + `'Finprof 274 Spec'!O24` | District and Office (Receipt) | the ***Register van ambtsgebieden*** — same gap as DD mapper row 686 |
| **MP-RSPEC-13** | `BE-FIN-002` (whole spec) | **L-08** — the spec declares income year **2026** while every artefact it names is income year **2025** (the held brochure `FPS-Finance_Belcotax-on-web_brochure_inkomsten-2025_20260114.pdf` and the matching XSD). Belcotax zone numbering and validation rules change between years | the **IY2026 Belcotax brochure and XSD** |

## (c) — no document resolves these

| ID | Location | Question | Owner |
|---|---|---|---|
| **MP-RSPEC-14** | `BE-FIN-001!'Field Options'` r69 | **L-07** — the Finprof **period-code series for IY2026**. The published table stops at 2015 and the series rotate on a four-year cycle, so it cannot be derived without guessing. Digits 8–10 of **every** withholding-tax payment reference depend on it; a wrong reference misposts the payment | `info.finprof@minfin.fed.be` |
| **MP-RSPEC-15** | `BE-FEBELFIN-001!'Field Options'` r22, r42 | Category Purpose code; OUT-10 structured communication format | NSSO Directorate of Collection, **or the client's bank** — partly a per-client contract |
| **MP-RSPEC-16** | `BE-FEBELFIN-001!'Field Options'` r44 | Authentication *"NOT FOUND at authority level"* — bank-specific by nature | per-client (SIR **G25**) |
| **MP-RSPEC-17** | `BE-NSSO-005` (26 cells, `'Limosa Spec'` col O) | 26 field rows read *"NOT FOUND — no code table is published"* | **No action.** The spec is `Descoped` at v1.3 and these are correctly retained with descoping notes, per the manifest's own rule |

## Structural / build-integrity

### MP-RSPEC-18 · The spec builders no longer reproduce the delivered workbooks
**Location** `scope_manifest.json._revision_history[13].still_open[0]` — *"THE REAL FINDING OF THIS
PASS, AND IT IS NOT CLOSED."*
**State** Running all nine builders from the corrected sources into a clean tree and diffing against
`04-reports-spec/` yields **3,172 differing cells**: FEDRIS 905, NSSO-002 990, NSSO-004 626,
FIN-002 268, NSSO-003 251, NSSO-005 68, NSSO-001 36, FIN-001 14, FEBELFIN 14. Roughly **fifteen**
post-hoc patch passes wrote into the workbooks and never went back into a builder — the Stage-8
alignment patch, the DD rename, the wage-type code write-back, `_apply_x10_011_joinkey.py` and
others. **A rebuild of any spec silently reverts real corrections.**
**Path (a)** — large but purely mechanical: back-port each patch family into its builder and re-diff
to zero. This is the single largest (a)-class item in the dossier.

### MP-RSPEC-19 · `BE-NSSO-003` sheet 4 row 12 — container block never identified
*"DECLARATION TYPE CONTAINER — block number and XML label NOT FOUND."* Registered by manifest v1.9
`still_open[1]` and **still not registered in `known_limitations`**, which v1.9 itself said it should
be. Confirmed a **genuine source gap, not the BE-X10-015 extraction defect** — it is a container
block rather than a zone, and the held glossary does not publish it.
**Path (b)** — the DmfA modification glossary or XSD. Plus **(a)**: register it in
`known_limitations`, which two passes have now agreed should happen and neither has done.

---

# §6 — SIR · `03-statutory-integrations/BE-SIR-001-v1.0.docx`

⚙ `selfcheck_be_sir.py` → **0 failures**. ⚙ The CCG citation gap (QA-FINAL **ISSUE-D**) is **closed**:
`BE-CCG-001 v1.0` and the dead path `01-ccg/BE-CCG-001-v1.0.docx` both return **0 hits**; the document
now cites v1.1.

### MP-SIR-01 · The gap registry: **G1–G26 open, G27 closed** — path (c) for 21, (c)-per-client for 5
⚙ Confirmed present at `sections/s08_gaps.md`. **Note for the record: the registry tracks G1–G27, not
G1–G4.** Registered collectively as **L-11**.

**G1–G21 — closeable only by a direct enquiry to a named authority** (each row in `s08_gaps.md`
names the owner and, where one exists, a real address):

| Gap | Question | Owner |
|---|---|---|
| G1 | XML character encoding of the DmfA FI declaration file | NSSO — resolvable from the DmfA XSD at build time; **low risk**, arguably (b) not (c) |
| G2 | OAuth access-token lifetime, and whether refresh is supported | NSSO / Smals, via Chaman |
| G3 | Required validity period of the X.509 authentication certificate | NSSO, Chaman documentation owner |
| G4 | Any retry policy — retries, back-off, max attempts, idempotency | NSSO |
| G5 | Whether `POST /declarations` is idempotent, and how a caller distinguishes a duplicate from a loss after a `201` | NSSO |
| G6 | Any response-time SLA on the Dimona GET (`404` covers both *not found* and *not yet processed*) | NSSO |
| G7 | Any published response-time SLA on NSSO batch (the D+1 pattern is a worked example, not an undertaking) | NSSO |
| G8 | Retention period for response files in the NSSO OUT directories | NSSO |
| G9 | Whether an *Annexe 30* anomaly-code list later than 2024/1 exists, given the glossary is at 2026/2 | NSSO glossary publication |
| G10 | Finprof file size / declaration-count limit for SS274EUR-XML | `info.finprof@minfin.fed.be` |
| G11 | Finprof anomaly or validation code list (a sanction regime is published; an error structure is not) | `info.finprof@minfin.fed.be` |
| G12 | Finprof acknowledgement SLA (status is pulled, not pushed) | `info.finprof@minfin.fed.be` |
| G13 | Whether the **26 September 2011** Finprof file description is still authoritative for IY2026 | `info.finprof@minfin.fed.be` |
| G14 | Belcotax XML encoding and file size limit | resolvable from `belcotax-2025.xsd`; else `belcotax@minfin.fed.be` |
| G15 | Belcotax refusal threshold for accumulated waivable errors, and the lifting criteria | `belcotax@minfin.fed.be` |
| G16 | Checkinatwork response-time SLA | NSSO |
| G17 | Whether a machine-readable feed of the provision/debit notice and contribution statement exists | NSSO, Directorate of Collection |
| G18 | Whether Student@work quota consultation has a batch or web-service channel, or is web-only | NSSO |
| G19 | Whether any electronic interchange format exists for the white-collar holiday certificate | NSSO / FPS Employment |
| G20 | Whether RJV/ONVA or the sectoral funds offer an employer-facing channel | RJV / ONVA and the sectoral funds |
| G21 | Whether any electronic channel exists for the declaration of garnishee | National Chamber of Judicial Officers |

**G22–G26 — cannot be closed at country level at all.** These are settled in a **client data
contract**, not in Belgian law: G22 fleet data (format, schema, transport, auth, SLA — the only
published Renta standard is a vehicle return-condition standard); G23 meal/eco voucher issuers;
G24 supplementary pension premium file; G25 SEPA bank channel specifics; G26 T&A and general ledger
(*"no statutory format; by design"*).

### MP-SIR-02 · Sections 3–6 were never read row by row
`SIR_REVIEW.md`: *"Full read-through of Sections 3–6's technical detail row by row"* was sampled via
the self-check's 18 named anchors only, never verified exhaustively against each cited source.
**Path (a)** — a content pass. Structural verification and three high-consequence primary-source
checks (NSSO SFTP port 8022, the SEPA 15 November 2026 date, the Belcotax 48-hour notification) all
passed; the rest is unsampled.

### MP-SIR-03 · OUT-10 `product_mapping_required` — SIR and manifest disagree
See **D-09**. The SIR says `false` (a single instructed amount whose value comes from the NSSO advance
notice and the DmfA balance, neither being a payroll-element mapping); the manifest says `true` and
flags the conflict inline at `integrations.outbound[8]._flag_note`.
**Path (c)** — an owner's ruling. It has sat flagged since 17 August.

### MP-SIR-04 · Watch item — Belcotax-on-web modernisation
`SIR_REVIEW.md` side finding: SPF Finances is preparing a modernised Belcotax-on-web expected
**February 2027** for income-year-2026 filings. Does not affect current accuracy; affects the next
revision. **Path (c)** — track, do not act.

---

# §7 — PAYSLIP · `06-payslip/BE_Compliance_Payslip_Generator.xlsx`

⚙ All **8 contract sheets** present in the documented order. ⚙ `validate_workbook.py --artifact PSL`
is recorded PASS by two independent passes. ⚙ `'Payslip Spec'` = 171 rows (rebuilt from 37 to 126+
by BE-PSL-001).

### MP-PSL-01 · Three broken `$x.custom.*` tokens — recorded open, not reproducible on the live file
`PAYSLIP_REVIEW.md` **BE-PSL-003**: *"3 pre-existing broken `$x.custom.*` tokens — partially closed as
an incidental side effect of the new Language Regime row, not directly addressed."*
⚙ **A sweep of every cell of all 8 sheets returns 0 `$x.` tokens of any kind.** Either the mapping
notation changed, or they were removed, or they never lived in cell values.
**Path (a)** — re-verify against whatever consumes the HRP mapping before either closing or
re-opening this. Do not close it on my sweep alone.

### MP-PSL-02 · BE-PSL-005, 006, 008 — untranslated NL text and other minors
`PAYSLIP_REVIEW.md`: *"untouched."* Not enumerated anywhere on disk beyond that line.
**Path (a)** — they need to be re-derived from the regression-audit JSON in `_qa/REGRESSION-BE-PSL.json`
before they can be worked; the review log does not carry their detail.

### MP-PSL-03 · BE-X10-005 — contract-type collision, and a wrong DD field cited
`handover_status.md` §4.1, a **blocker**: *"Contract-type collision live in the spec and the delivered
render; cites the wrong DD field."* No later document records it as fixed.
**Path (a)** — not re-tested in this session. Verify before working.

### MP-PSL-04 · BE-X10-014 — English text on the legally effective Dutch sheet
`handover_status.md` §4.2, a **major**. Belgium's language rule makes the Dutch sheet the legally
effective document in the Dutch language region, and the sanction for the wrong language is
**nullity**.
**Path (a)** — translate. Related to but distinct from MP-PSL-05.

### MP-PSL-05 · L-16 — French and German payslips not built
`scope_manifest.json known_limitations[5]`: *"German (DE) is an explicit unbuilt seam; French (FR) is
a **mandatory second deliverable, not an option**. Belgium has three language regions and the
sanction for issuing a payslip in the wrong language is NULLITY of the document, so this is a
compliance exposure and not a convenience gap."* Correctly disclosed in the payslip's own `A109`.
**Path (a)** — two further payslip deliverables. This is the largest single unbuilt item in the
dossier and it is a compliance exposure, not a nicety.

### MP-PSL-06 · The payslip generator is not a reliable rebuild path
`CCG_CONTENT_REVIEW.md`: `_build_payslip.py` was **already stale** relative to the delivered artefact
before the work-bonus fix (its language note differs from the shipped A109), and a post-build patch
script `_fix_regression_psl.py` already exists — *"build-then-patch is the established payslip
workflow and the generator is not a reliable rebuild path regardless. Patched here so it is at least
not wrong; resyncing it fully is a separate item, not attempted."*
**Path (a)** — same class as MP-RSPEC-18, one artefact.

---

# §8 — SCOPE MANIFEST · `scope_manifest.json`

⚙ Valid JSON, `scope_version` **2.3**, 17 `known_limitations`, 28 failure patterns, 14
`_revision_history` entries.

### MP-SCOPE-01 · ISSUE-E — 14 `_bound_to` pointers still name a superseded DD
⚙ Live: **14 × `BE-DD-001-v1.1`** and **4 × `BE-DD-001-v1.0`** inside
`option_mapper_scope.*._bound_to`, against only **2 × `BE-DD-001-v1.3`**. The 628-cell propagation
covered `.xlsx` cells only and never touched the manifest. The row ranges still resolve (blocks r47
and r51 are unchanged), so nothing is broken — but a lock that names a superseded file is the defect
class the propagation existed to remove.
**Path (a)** — re-point the 14 v1.1 strings. Leave the 4 v1.0 strings: they record what the scope was
*decided from* and are correct as history.

### MP-SCOPE-02 · The registered DD marker count is 71% too high
See **D-04**. `known_limitations[7]` certifies **36**; ⚙ live is **21**.
**Path (a)** — recount and restate. The entry's own precedent (the `CORRECTED 2026-08-17` clause in
the DD's v1.1 changelog, which exists precisely because a count was asserted without recounting) says
how: *"Do not restate a count here without recounting it."*

### MP-SCOPE-03 · `contract_duration_type._was` contains a statement that is false
It says DD *"row 57 carries a back-reference to `option_mapper_scope.contract_type` that … must be
repointed to `contract_duration_type` — flagged, not fixed by this pass."* Measured in **both** v1.1
and v1.3, `'Country Option Mappers'!F57` **already reads `contract_duration_type`**. The flagged
defect does not exist. Left alone because it is prose inside a scope decision record.
**Path (a)** — a one-line correction, but it belongs to the scope owner.

### MP-SCOPE-04 · `source_artifact` still pins `BE-CCG-001-v1.0.docx`
⚙ Confirmed live. Deliberately left across three sessions: it records which file the scope was
*decided from* on 2026-08-12 and is historically correct.
**Path — a decision, not a defect.** If the field should track the live artefact, that is a conscious
call; if it should stay historical, say so once and stop re-raising it.

### MP-SCOPE-05 · `joint_committee`'s in-scope code list may now be under-specified
The lock was decided against the **8-code** v1.1 domain; v1.3 carries **16**. The only lock-covered
block affected by the widening. Deliberately not taken during a version promotion.
**Path (c)** — a scope decision.

### MP-SCOPE-06 · The older BE-SCOPE findings, still open
`_revision_history[13].still_open[2]` confirms these are **UNAFFECTED and stay open**. From
`BE-QA-REPORT.md` §5:

| id | State |
|---|---|
| BE-SCOPE-005 | No `gender` key, no `charge_bearer` key; `insurance_type` is 4 invented strings and `correction_codes` 3, neither matching any DD block; `benefit_type` grew to 12 values but was never re-pointed at the WTC that owns it |
| BE-SCOPE-006 | `known_limitations[0]` still reads *"No official source PDFs were available…"* while ⚙ **36 files sit in `00-official-sources/spec-sources/`, 15 of them PDFs**. (`BE-QA-REPORT.md` said 42 files; the PDF count is unchanged, the total is not — re-measure before quoting either.) |
| BE-SCOPE-007 | `known_limitations[6]` unchanged; its precondition is still stated as future and is already crossed |
| BE-SCOPE-008 | 7 entries and none added, while the SIR opened 27 gaps, the DD 36 markers, the specs 848 and the CCG 1 |
| BE-SCOPE-009 | `F23`/`F24`/`F25`/`F26` strings verbatim unchanged, including *"not triggered: no source PDFs present"* — false on the same evidence as BE-SCOPE-006 |
| BE-SCOPE-010 | The manifest carries **zero of the 41** work-bonus / GMMI / high-wage figures swept across the seven artefacts |
| BE-SCOPE-011 | Partially closed. Inbound has 9 inline rationales; **outbound is still 12/12 `true` with zero rationales** |
| BE-SCOPE-012 | Partially closed, new contradiction: the Checkinatwork **response** (IN-19) is registered while the Checkinatwork **declaration** is undecided; OUT-16 electronic payslip is absent from `integrations.outbound` though `BE-PAY-PAYSLIP-008` decides it |
| BE-SCOPE-013 | Closed on the wage-type half (BE-056/057/058 added); see MP-SCOPE-07 for the residual |
| BE-SCOPE-015 | Partially closed. Still open: `generated` and `scope_decided_on` frozen at 2026-08-12, `source_artifact` at v1.0, and **no consumers block** listing each artefact at its version on disk |
| BE-SCOPE-016 | `both` still 3 entries; no `BE-BOTH-BV` against `BE-FIN-BV-003`'s `integration_type: both`. True distinct flows 24, expressed as 27 *(note: `_both_note` was later added and the array is now 5 — re-measure before working this row)* |
| BE-SCOPE-017 | `authority_filings.out_of_scope` is out of `filing_id` sequence |
| BE-SCOPE-018 | `known_failure_patterns_to_check` is a bare `F1…F22` with **no descriptions and no outcomes**, alongside a second differently-shaped 6-entry array |
| BE-SCOPE-019 | Both `code` and `country_code` present, both `"BE"`; the template defines only `country_code` |
| BE-SCOPE-020 | The `BE-IN-GARNISHMENT-ORDER` rationale still cites the Art. 1409 bands **without the maintenance-debt exception**, which the DD records at mapper code 3 as *"Attachable WITHOUT ANY LIMIT"* |

**Path — all (a)** except BE-SCOPE-011/012, which need scope rulings **(c)**.

### MP-SCOPE-07 · L-13 residual — the IY2026 loan reference rates cannot exist yet
`BE-058` carries the **IY2025** rates labelled **PROVISIONAL** (fixed-rate mortgage 3.00%; fixed-term
non-mortgage 0.26%/month for vehicle financing and 0.52% otherwise; non-mortgage without determined
term 5.57%) and instructs a recomputation and 281.10 restatement once the definitive rates appear.
They are fixed only by the Royal Decree of the *following* February — **not expected before February
2027**. A second asymmetry is recorded and must not be flattened: the **NSSO does not follow these
rates at all**.
**Path (c) then (b)** — nothing to do until the decree publishes.

### MP-SCOPE-08 · W4 and W5 from the scope lock-in gate, never closed
`scope_validation.md` (12 Aug, W3 updated 17 Aug) closes W1, W2, W3 and leaves:
- **W4** — formats declared without verified schema citations. LIMOSA-as-CSV and the garnishment
  order as CSV *"look inferred rather than verified"*. Auditor **C23 will FAIL any Stage-4 spec
  containing XML without an XSD citation.** → same documents as MP-RSPEC-06/07/13. **Path (b).**
- **W5** — the Annex III **notional surcharge percentage** is asserted at 7% in `special_rules[7]`
  (giving 26.75 / 42.80 / 48.15 / 53.50) **and simultaneously flagged unconfirmed** in
  `known_limitations[6]`. Every withholding figure in the dossier rests on it. **Path (b)** — the
  Annex III text (RD 11 December 2025, last updated 19 March 2026).

Its **Required Actions** 1 (residual — the garnishment field-level contract, Art. 1409 band inputs),
4, 5, 6 (*re-check the Art. 245 corrective bill's enactment status before go-live*) and 7 (*update
`shared/scope_manifest_template.json` from `reason` to `descoping_reason`/`client_impact`*) are all
still open. **7 is a shared-template fix owed before the next country, not a Belgium item.**

---

# §9 — CROSS-CUTTING, PIPELINE AND PROCESS

### MP-PROC-01 · No post-fix Stage-10 verdict exists
The only full Stage-10 result on disk is `BE-QA-REPORT-FINAL-2026-08-24.md`, whose one blocking
MAJOR was closed **after** it was written (**D-01**). ⚙ `_pipeline/build-manifest.json` records
**every artefact as `built` and not one as `qa_pass`**, with an explicit note that this is deliberate
and that *"this field is the orchestrator's to advance."*
**Path (a)** — a re-run of the 9 checks, or at minimum a re-taken readiness verdict on Check 4. Until
then the dossier's own status of record is "not closed" on grounds that no longer hold.

### MP-PROC-02 · The propagation gate that let ISSUE-B through has not been changed
QA-FINAL's process recommendation, verbatim: the STEP 4 gate — *"field inventory unchanged, therefore
the string swap is legitimate"* — *"is the thing that let this through, and it will let the next one
through too. A DD version promotion needs a **second** gate: diff the option-mapper code domains, and
for every block that widened, sweep the report specs for a `NOT FOUND` or a short domain on that
zone."* Nine blocks widened; a one-line check would have caught all four affected specs before FIX 7
propagated the stale one.
**Path (a)** — write the gate. Nothing on disk implements it. This is the highest-leverage (a) item
in the list: it is the root cause of sessions 4 and 5 both existing.

### MP-PROC-03 · L-02 — `_research/` and the per-artifact build logs do not exist
⚙ `_pipeline/build-manifest.json` **exists** (24,811 bytes, schema-shaped, `mandate_status: sealed`,
`pending_research: []`, `tier` present). ⚙ **No `_research/` directory exists** anywhere under
`BE-compliance/`, and ⚙ a search for `*build-log*` and `*-facts.json` returns **nothing**. So of
L-02's three parts, one is closed and two are not: there is still **no section → `register_id` map**,
so no figure is traceable to the source that produced it by machine.
**Path (a)** — retrofit per `mercans-pipeline-contracts`.

### MP-PROC-04 · The legal-basis register exists but is 65% un-sourced by URL
⚙ 63 rows on the 20-column contract, all with `tier`, `verified_on` and `status` populated. But
⚙ **41 of 63 rows carry `NOT AVAILABLE - RETROFIT` in `url`**, **55 of 63 in `local_file`**, and
**35 of 63 in `retrieved_on`**. The register can say what an instrument *is* and what it carries; for
two thirds of its rows it cannot say where it was read or produce the copy.
**Path (b)** — re-acquire the instruments. This is what makes **L-01 "closed"** thinner than it reads.

### MP-PROC-05 · L-15 — nothing has ever been filed
`known_limitations[14]`: *"NO FILING HAS EVER BEEN SUBMITTED THROUGH ANY CHANNEL, and this is the
single item that holds every per-artifact accuracy band in this dossier below 95%."* No portal
round-trip, no accepted declaration, no authority-returned error file, for any flow.
**Path (c)** — a pilot submission per channel in the NSSO simulation and Belcotax test environments.
**This is the ceiling on the whole dossier and no amount of agent work moves it.**

### MP-PROC-06 · The failure-pattern register has no outcomes
`_revision_history[7].still_open`: *"NO PER-PATTERN OUTCOME TABLE EXISTS FOR F1–F22."*
⚙ `known_failure_patterns_to_check` holds 28 entries. Duplicate of BE-SCOPE-018, recorded twice
because two different files raise it.
**Path (a)** — one table.

### MP-PROC-07 · Tooling findings T-01 to T-03
From `handover_status.md` §5. **T-04 (`shared/` untracked in git) is closed** — L-18, `git add shared/`
staged 32 files on 18 August.
- **T-01** — the pipeline's C29 residual-marker lint scans only 4 of 7 artefacts (not the SIR, not the
  payslip, not `scope_manifest.json`), reads the CCG as paragraphs only so **every Word table cell is
  invisible**, and its marker list omits `NOT FOUND`, `PENDING`, bare `placeholder` and effectively
  `XXX`. *"Deterministic PASS is achievable over a corpus holding 892 unresolved-gap markers."*
  ⚙ The artefact-toolkit's own `validate_workbook.py` C29 is the stricter one actually being run —
  it caught the word *"placeholder"* in session 4's own version-bump wording. The **pipeline's**
  C29 is the defective one.
- **T-02** — **C18** (*"every filing in scope_manifest must have a Spec file"*) is prompt text only and
  never runs; **C9** (WTC tax codes against the country's own legend) appears nowhere in the script at
  all. Between them they would have caught BE-X10-001, BE-SCOPE-014, the form-325.10 error and the
  box-360 gap.
- **T-03** — `shared/schemas/review.schema.json` cannot express a regression review (`action` has no
  `report_only`, `artifact` takes one id, `pattern` is `^F[0-9]{1,2}$`), so
  `_qa/REGRESSION-BE-XCHECK-r1.json` extends it with underscore keys. Carried as `BE-META-002`.

**Path — all (a), but the owner is the pipeline/toolkit, not Belgium.** Fixing them here would be
scope-widening; not recording them loses them.

### MP-PROC-08 · Version Control prose that narrates history against the wrong version
Fix-log session-2 open item 5 and session-3 open item 2, unchanged. 19 cells now narrate past actions
using "v1.3"; most are harmless or improved. Two are worth one decision taken for both families at
once: `BE-WTC-001!'Version Control'!D13` and `BE-DD-001-v1.3!'Version Control'!D13` both describe an
*initial build* that in fact happened against v1.0. One genuinely distorted cell:
`BE-WTC-001!'Form Reference Guide'!C2` says fields *"were REMOVED from BE-DD-001-v1.3 when that
declaration was descoped"* — the Limosa removal happened at **v1.1**.
**Path — a decision, then (a).**

### MP-PROC-09 · Nine specs record the 628-cell propagation nowhere in their own history
Fix-log session-2 open item 6, **half closed**: session 4 inserted new `Version Control` rows for the
five specs it bumped to v1.3. The three unbumped in-scope specs (`BE-FIN-001`, `BE-FIN-002`,
`BE-FEBELFIN-001`) still had their r15 rows **rewritten in place** rather than supplemented, so the
propagation is invisible in their history.
**Path (a)** — three rows.

### MP-PROC-10 · The CCG module→docx round-trip is semantically exact but not byte-exact
Fix-log session-3 open item 3. A rebuild produces a **181,554-byte** file where the promoted one is
**173,307 bytes**, because python-docx does not coalesce runs and Word does. Text and formatting are
identical (0 differing units of 4,814). Harmless today; **a future gate that hashes the docx rather
than diffing its content will fire.**
**Path (a)** — know it before writing that gate.

### MP-PROC-11 · FIX 7 / zone 00096 — a scope question left unanswered
Fix-log session-1 open item 3: the Legal Basis code table was **not** added to `BE-NSSO-003` because
that declaration does not contain zone 00096 — verified in session 4 (zone 00096/00095 appear nowhere
in the workbook), so **withholding it was correct**. What remains unanswered is whether the real
intent was to add zone 00096 to the DmfA Modification *field spec*.
**Path (c)** — a scope decision, not a propagation.

### MP-PROC-12 · FIX B Category 2 is reversible if the brief is read more narrowly
Fix-log session-4 open item 2, recorded by its own author. Session 4 fixed two shapes of staleness:
**Category 1**, an enumerated list narrower than the DD (unambiguous), and **Category 2**, a row
asserting *"NOT FOUND … not held"* for a domain the DD now holds. If only Category 1 was meant, the
affected blocks are Activity With Risk (3 specs), Worker Code (4), Joint Committee in NSSO-001 and
FEDRIS, and NIS in NSSO-001. The backups make it a clean revert.
**Path (c)** — a reading of the brief, i.e. an owner's call. Flagged so it is not discovered later as
unauthorised widening.

---

# §10 — VERIFIABLY CLOSED (recorded so it is not re-opened)

⚙ = re-measured live in this session. Several of these are still listed as open in files that were
never updated; see §1.

| Item | Evidence |
|---|---|
| ISSUE-B — Days Justification 00625 published at codes 1–5 | ⚙ `BE-NSSO-002!'Field Options'` r154–161 = codes **1–7 + closing note**; same in NSSO-003 and NSSO-004 |
| ISSUE-D — SIR citing CCG v1.0, one a dead path | ⚙ `BE-CCG-001 v1.0` → **0 hits** in the SIR; v1.1 present |
| BE-X10-002 — no wage type carries Belcotax box 360 | ⚙ `Wage Type Catalogue!G304` (BE-003) = **`284; 360`** |
| BE-X10-012 / L-17 — Stage 11 skill not built | ⚙ `08-skill/payroll-compliance-belgium/SKILL.md` + 7 reference files |
| L-01 — no `legal-basis-register.csv` | ⚙ exists, **63 rows**, 20-column contract *(quality caveat: MP-PROC-04)* |
| L-03 — no tier classification | ⚙ `scope_manifest.json.tier` and `_pipeline/build-manifest.json.tier`, T3 overall, 13 domains |
| L-04 — P5 has no checklist | `PROPAGATION-LEDGER.md` §0 |
| L-12 — 13 unnamed spec field rows, 148 bulk Belcotax cells | 64 cells repaired; unnamed rows now 0 across all nine specs |
| L-14 / BE-SCOPE-014 — Limosa unresolved five ways | Owner ruling 17 Aug; reconciled across manifest, SIR, CCG, spec, DD and WTC |
| L-18 / T-04 — `shared/` untracked | `git add shared/`, 0 → 32 tracked |
| BE-X10-022 — CO2 multiplier on four tier-B sources | Closed with a primary source: Art. 34, 1° of the Law of 25 November 2021 |
| BE-X10-011 — 195 WTC references, none resolving to a code | Closed 17 Aug; re-measured 24 Aug as 206 reference cells against 359 rows |
| BE-DD-001 / BE-DD-004 — 57 empty Code cells, worker-status substitution | Independently re-verified in `DD_REVIEW.md` |
| BE-RSPEC-002 — 538 System Mapping cells | 318 filled, 220 correctly left; 538/538 reconciled |
| BE-RSPEC-003 — NSSO-003 headers byte-identical to NSSO-002 | 1 of 32 changed; root-caused in `build_03_dmfa_mod.py` |
| BE-PSL-001 — Payslip Spec covered 42% of rendered content | Rebuilt 5→15 sections, 37→126 rows; ⚙ now 171 rows |
| The EUR 0.19 error in m09 Step 7 | ⚙ **D-06** — fixed, with all three dependent totals |
| The missing 4th-band constant, the three one-cent F totals, the 13.92-vs-12 split, the disputed child supplements | ⚙ **D-08** |
| ISSUE-10 — two conditional rules keying off unresolvable zones | One documented inline (FEDRIS 00431/00432), one refuted (DRS "20072" is a quarter identifier, not a zone) |
| G27 — Related Report Spec pending on all 19 outbound flows | Stage 3 delivered; Section 2.3 carries the resolved mapping |

---

# §11 — SUGGESTED ORDER OF WORK

Not a plan, just the dependency order that falls out of the above.

1. **MP-PROC-01** — re-take the Stage-10 verdict. Everything downstream is being sequenced against a
   report whose blocking finding is closed.
2. **MP-PROC-02** — write the option-mapper propagation gate **before** the next DD promotion, not
   after.
3. The cheap (a) cluster, one session: **MP-DD-01** (2 cells), **MP-RSPEC-01** (3 cells),
   **MP-RSPEC-03** (3 fills), **MP-RSPEC-02** (8 statuses), **MP-SCOPE-01** (14 strings),
   **MP-SCOPE-02** (one recount), **MP-DD-03** (F15/F16).
4. **MP-RSPEC-18** — the 3,172-cell builder divergence. Large, mechanical, and it silently reverts
   everything in step 3 the moment anyone rebuilds a spec. Arguably belongs before step 3.
5. **MP-PSL-05** (L-16, French and German payslips) — the largest unbuilt deliverable and a nullity
   exposure.
6. **MP-CCG-03** (arrears on nr. 58) — the largest unresolved money question, once the Annex III text
   is in hand.
7. Batch the **(b)** list into one acquisition run: Annex III (nrs. 33, 40.2, 40.3, 53, 55, 58);
   NSSO Annexes 2, 3, 4, 6-adjacent, 7, 8, 12, 21, 34, 35, 44; the DmfA and Belcotax XSDs; the IY2026
   Belcotax brochure; the RD of 24 July 2026; Circulaire 2026/C/51. Roughly **19 items collapse into
   one source-hunter pass**.
8. Batch the **(c)** authority questions into one enquiry per authority: NSSO (G1–G9, G16–G21,
   contract duration type, employer number check digit, work-bonus Q3 cap), FPS Finance /
   `info.finprof@minfin.fed.be` (G10–G13, the period-code series), `belcotax@minfin.fed.be`
   (G14, G15). **21 SIR gaps plus 4 registered limitations collapse into three letters.**
9. Owner decisions, which block nothing else and can be taken in any order: **MP-SIR-03**,
   **MP-SCOPE-05**, **MP-SCOPE-04**, **MP-WTC-02**, **MP-PROC-11**, **MP-PROC-12**, **MP-PROC-08**,
   **MP-WTC-01**.
10. **MP-PROC-05** (L-15, a pilot filing) — whenever a client environment exists. Nothing else lifts
    the accuracy bands.

---

*Compiled read-only on 24 August 2026. Sources read in full:
`BE-FIX-LOG-2026-08-21.md` (all five sessions), `BE-QA-REPORT-FINAL-2026-08-24.md`,
`handover_status.md`, `scope_validation.md`, `CCG_CONTENT_REVIEW.md`, `WTC_REVIEW.md`,
`SIR_REVIEW.md`, `DD_REVIEW.md`, `PAYSLIP_REVIEW.md`, `REPORTS_SPEC_REVIEW.md`,
`ALIGNMENT_PATCH_REVIEW.md`, `TAX_ENGINE_FIX_APPLIED.md`, `ALLOWANCE_INVESTIGATION.md`,
`BRACKET_INVESTIGATION.md`, `CHILDREN_SUPPLEMENT_INVESTIGATION.md`, `APRIL_SALARY_INVESTIGATION.md`,
`scope_manifest.json`, `_pipeline/build-manifest.json`, `00-official-sources/legal-basis-register.csv`,
`03-statutory-integrations/sections/s08_gaps.md`, `BE-QA-REPORT.md` §5 and §7, and the live
`BE-DD-001-v1.3.xlsx` `'Country Option Mappers'` and `'Country Fields'` sheets. Items marked ⚙ were
re-measured against the files on disk in this session rather than quoted.*
