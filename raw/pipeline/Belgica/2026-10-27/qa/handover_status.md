# handover_status.md — Belgium (BE)

**As at:** 2026-09-16, after the Stage 9.5 gap-closure pass
**Owner of this file:** `compliance-qa-auditor`
**Baseline for this pass:** commit `2ab14ab` *Pre-patch baseline, 17-item gap closure*
**Companion documents:** `BE_gap_closure_patch_spec.md` ·
`07-qa-crosscheck/BE-QA-REPORT-FINAL2-2026-08-24.md` · `PROPAGATION-LEDGER.md` ·
`scope_manifest.json` · previous snapshot preserved at
`handover_status.md.bak-before-stage95`

> Stage 9.5 was fenced to exactly three artefacts — `BE-DD-001-v1.3.xlsx`,
> `BE-WTC-001-v1.0.xlsx`, `BE-CCG-001-v1.1.docx`. Everything in §1–§5 below is
> measured against those three. The country-level findings carried over from the
> 2026-08-25 snapshot are restated unchanged in §7; this pass did not work them
> and does not claim them closed.

---

## 1. Overall verdict

**`READY_FOR_HANDOVER` — for the three artefacts in this pass's scope only.**

**`NOT_READY` at country level**, on findings that were outside this pass's fence and are
unchanged: `BE-X10-010` (owner ruling owed), `BE-X10-006` (not workable as written), `T-05`
(the payslip has no working gate), and `L-15` (nothing has ever been filed through a live
channel). See §7. Do not read §1's first line as clearing Belgium.

The three fenced artefacts meet all three of the gating conditions set for this pass:

| Gate | Result |
|---|---|
| Every patch item confirmed present by diff against the `2ab14ab` baseline | **PASS** — 23 of 23 rows, §2 |
| Zero `NOT FOUND` / `PENDING` / `TODO` / `TBD` markers across all three files | **PASS** — 0 hits, §4 |
| The Bijlage 12 question answered rather than left open | **PASS** — answered, and answered the *opposite* way to the spec's hypothesis, §3 |

---

## 2. Patch items — diff-confirmed against the baseline

Confirmed by reading both sides back out of the delivered binaries: the baseline side straight
from `git show 2ab14ab:…`, the current side from the working tree. Not self-reported by the
patch scripts.

| Item | File | Diff confirms | Evidence |
|---|---|---|---|
| 1 NSSO Worker Status | BE-DD-001 | **Y** | Bijlage 21, 15 → **45** rows |
| 2 NSSO Worker Code | BE-DD-001 | **Y** | Bijlage 2, 13 → **186** rows |
| 3 NSSO Employer Category | BE-DD-001 | **Y** | Bijlage 27, 1 → **289** rows |
| 4 Joint Committee Number | BE-DD-001 | **Y** | Bijlage 26, 17 → **225** rows |
| 5 Reference Type (zone 00221) | BE-DD-001 | **Y** | new block, 0 → **9** rows |
| 6 Payment Category Purpose | BE-DD-001 | **Y** | NSSO row resolved to not-applicable; 5 NSSO purposes added as their own block |
| 7 DmfA Remuneration Code | BE-DD-001 | **Y** | new block, Bijlage 7 / zone 00067, 0 → **44** rows |
| 8 DmfA Service Code | BE-DD-001 | **Y** | new block, Bijlage 8 / zone 00062, 0 → **52** rows |
| 9 Work Reorganisation Measure | BE-DD-001 | **Y** | Bijlage 44, 16 → **58** rows |
| 10 Employment Promotion Measure | BE-DD-001 | **Y** | Bijlage 35, 6 → **15** rows |
| 11 Work Schedule Days Indicator | BE-DD-001 | **Y** | Bijlage 34 day codes, 1 → **28** rows |
| 12 Service Exemption Indicator | BE-DD-001 | **Y** | operator confirmed `>=` on two rows |
| 13 Art. 11bis part-time contract | BE-CCG-001 | **Y** | new table row + legal-basis line |
| 14 Annexe III child reduction | BE-CCG-001 | **N — no patch required** | already present *and already correct*; see §3 |
| 15 Tax Collection District | BE-DD-001 | **Y** | truncated note completed |
| Contract Duration Type (re-label) | BE-DD-001 | **Y** | 4 rows → resolved-not-applicable; wrong zone corrected |
| Bijlage 12 (the never-closed item) | BE-DD-001 | **Y** | new block, 0 → **78** rows |
| 7/8 WTC leg | BE-WTC-001 | **Y** | Form Reference Guide D2 points at the two new DD blocks |
| Work bonus cap | BE-WTC-001 | **Y** | 4 cells, EUR 3,594.36 from 1 Jul 2026 |
| Work bonus cap | BE-CCG-001 | **Y** | same figure, same source |
| Staff-loan reference rates | BE-WTC-001 | **Y** | reworded as a dated future dependency |
| Overtime-ceiling citation | BE-CCG-001 | **Y** | open confirmation closed |
| Zone 00096 legal basis | BE-DD-001 | **Y** | 5 → **10** rows |

**Rows not confirmed: 0.** Item 14 is the only non-`Y`, and it is non-`Y` because the correct
action was to change nothing — see §3.

`Country Option Mappers`: **87 blocks / 1,043 rows → 92 blocks / 2,023 rows.**

---

## 3. The two open questions, and three prior conclusions that turned out to be wrong

### 3.1 Bijlage 12 — **EXISTS, is current, and is not a DmfA annex**

The spec expected this to close as *retired, not applicable*, reasoning from the DmfA
Glossarium's own bijlage index jumping 11 → 21. **That reasoning was sound and the conclusion
was wrong.**

- The live `bijlagen.nsf` index is frame-based and did not render, exactly as predicted — but it
  did not need to. Bijlage 12 *"Identification du risque / Identificatie van het risico"* is
  carried verbatim in **all three DRS glossaries already held on disk** at edition **2026/2**
  (published 01/06/2026): DRS/AMI scenario 1, DRS/FAT scenario 1, DRS/ONEM scenario 3. Annex
  content version **AN2025-1-FR12**, 9 pages.
- The DmfA glossary's annex inventory measures as **1–11, 21, 23, 24, 31, 35, 42–46**. The 11 → 21
  jump is real, and its cause is not retirement: **Bijlage 12 belongs to the DRS annex series,
  which the DmfA glossary does not carry.**
- Per Step 3's own instruction — *"If it DOES exist: extract the current code table and patch the
  DD row with the real content"* — the table is in, **78 rows**, keyed `Identification / Code`
  the way the annex itself keys it. Zone 00430 `IdentificationOfRisk` is recorded as carrying the
  three-digit code alone (permitted values 001–008), with the form identification travelling
  separately in zone 00296.

### 3.2 Annexe III point label — **published, and the CCG already had it right**

The Securex page named in Step 3 exposes **no point number**; it says only that the child
reduction is "the first reason for reduction". Step 3's fallback would have been to record that
and stop. Going to the instrument instead settled it:

- **Annexe III to the Royal Decree of 11 December 2025** states it plainly:
  **`38. La réduction pour enfants à charge s'élève à (en tenant compte du n° 8)`**.
- The CCG **already cites "Annex III nr. 38"**, and already carries the exact statutory annual
  figures — 624 / 1,656 / 4,404 / 7,620 / 11,100 / 14,592 / 18,120 / 21,996, plus 3,864 per child
  beyond the eighth — which reconcile line by line with the instrument. The disabled-child double
  count is cited to `nr. 8`, which is also correct.
- Every other Annexe III citation in the CCG was checked in the same pass and is correct:
  `nr. 31` (base scale), `nr. 32` (exempt quotity **EUR 11,170**, reduction **EUR 2,987.98** —
  both verbatim), `nr. 12` (rounding).
- The spec proposed "~€52 / ~€138 / ~€367 / ~€632–635". Those are the CCG's annual figures divided
  by twelve. Writing them in would have replaced exact statutory amounts with approximations of
  themselves. **No change made, deliberately.**

### 3.3 Three findings in the delivered corpus that were wrong, found while working the spec

| Was recorded as | Actually | Where it now stands |
|---|---|---|
| Work Schedule Days Indicator: *"confirmed dead end after extensive alternative-source research (20 Aug 2026) … requires direct manual navigation of the gated structured-annex PDF"* | **Bijlage 34 is held locally**, in the DRS/ONEM glossary 2026/2. The full day-code table was on disk the whole time. | 28 codes loaded, verified to carry identical meaning across all four grid lengths (7/14/21/28), so one numbering serves all four |
| Contract Duration Type, four rows: *"NSSO zone 00885 offers only 0 and 1"* | **No zone 00885 exists** in any held glossary. The contract-type zone is **00050** (`ContractType`, block 90015), domain `0 = voltijds`, `1 = deeltijds` | zone corrected on all four rows; rows re-labelled resolved-not-applicable |
| Zone 00096: *"Values beyond 4 not confirmed to exist"* | Domain runs **1 to 10** and is printed in full in the held DRS/ONEM glossary, which had not been read for that zone | 10 rows loaded; codes 5/6 are the Vande Lanotte plans, 7 the public-sector redistribution plan, 8–10 the CBA no. 103 time-credit regimes |

Each was closed from a source **already sitting in `00-official-sources/`**. The common cause is
not bad research; it is that the held glossaries were searched for some zones and not others.

---

## 4. Audit results

### 4.1 Residual-marker scan — the Step 5 criterion

Scanned every cell of every sheet and every paragraph, table cell, header and footer, for
`NOT FOUND` · `PENDING` · `TODO` · `TBD` · `FIXME` · `XXX` · `placeholder` · `to be confirmed` ·
`to be verified` · `VERIFY No.`

| File | Hits |
|---|---|
| `BE-DD-001-v1.3.xlsx` | **0** |
| `BE-WTC-001-v1.0.xlsx` | **0** |
| `BE-CCG-001-v1.1.docx` | **0** |
| **Total** | **0** |

This is the *stricter* list Stage 9.5 specified. The pipeline's own C29 vocabulary does not
include `NOT FOUND` or `PENDING`; both files were clean under C29 before this pass and are clean
under the stricter list now.

### 4.2 Structural gates

| Gate | Result |
|---|---|
| `validate_workbook.py --artifact DD` | **PASS** — blocker 0, major 0, minor 0; 8 sheets in contract order |
| `validate_workbook.py --artifact WTC` | **PASS** — blocker 0, major 0, minor 0; 6 sheets in contract order |
| `inspect_docx.py` C29 scan on the CCG | **clean**; 14 H1, 212 headings, 148 tables, 1 section |
| DD archive integrity | 49/49 entries, both media files, all 3 comment parts + VML preserved |
| WTC archive integrity | 23/23 entries |
| CCG archive integrity | 19/19 entries |

All three were edited at XML level and repacked entry by entry in original order.
`openpyxl.save()` and any LibreOffice resave were avoided throughout, per the standing rule for
files carrying embedded drawings.

### 4.3 `_audit_v24_mechanical.py` — 33-check mechanical audit

Run before and after this pass. **Byte-identical results: `PASS 14 · MANUAL 2 · FAIL 1`.**
No check changed verdict or detail. This pass introduced **zero regressions**.

C1 **PASS** (13 modules) · C8 **PASS** (no open-item markers) · C11 **PASS** (96/96) ·
C29 **PASS** · C12, C21–C24, C26, C28, C30–C32 **PASS**.

Two notes on running it, neither a content defect:

- The local `_audit_v24_mechanical.py` is a **v2.4 copy** that hard-codes
  `01-ccg/BE-CCG-001-v1.0.docx`. The delivered CCG is **v1.1**, so C1/C8/C11 report
  *"CCG missing"* on a first run. Re-run with the path resolved and all three PASS. The stale
  path was **not** fixed — the script is outside this pass's fence.
- **C20 FAIL is pre-existing and unrelated.** It lists spec ids in a superseded naming scheme
  (`BE-NSSO-DIMONA-001` etc.) against delivered specs named `BE-NSSO-001`…; C12 independently
  passes with *"All 9 specs have adequate schema"*. It concerns `04-reports-spec`, untouched here,
  and measured identically before and after.
- **C33 MANUAL (88 local-language passages in CCG prose)** is pre-existing and unchanged at 88.

### 4.4 Global WTC baseline

`diff_wtc_baseline.py` reports **MISSING 0** (all 300 baseline codes present) but **RENAMED 299**,
verdict `BASELINE VIOLATED`. **Measured identically on the pre-patch file** — this pass touched no
wage-type row, no formula, no tax code. Reported here rather than absorbed; it is a
Belgium-localisation-versus-baseline-wording question that predates Stage 9.5 and needs an owner's
ruling, not a builder's edit.

---

## 5. Remaining issues inside this pass's scope

**One, and it is a convention rather than a defect.**

**The language convention on the new annex blocks.** The NSSO publishes Bijlagen 2, 7, 8, 12, 21,
26, 27, 34, 35 and 44 in Dutch and French only. Where an English term is established, the English
Description column gives it. Where it is not, that column gives the applicability flags, the
validity window and the source in English **together with the authority's own wording quoted
verbatim**, rather than an unofficial translation.

This was a deliberate choice and it has a measurement behind it: a draft of this pass wrote
English renderings of the Bijlage 21 mnemonics by inferring from the letter codes, and was **wrong
on 13 of 40** — `BA` was read as "volunteer ambulance worker" when it is *worker employed outside
the normal labour circuit*, `PJ` as "judicial police" when it is *recognised professional
journalist*, `EC`/`MN`/`MY` as clergy-versus-medical inversions, and so on. That draft was
discarded and every entry rewritten against the printed label. An invented English rendering of a
statutory category reads as authoritative, which is precisely why it must not be written.

**If the owner wants full English renderings of Bijlagen 2, 26 and 27** (roughly 700 long
statutory descriptions), that is a translation commission with review, not a builder task. The
code lists themselves are complete and authoritative as delivered.

---

## 6. Sign-off recommendation

**Sign off the three Stage 9.5 artefacts.** Every spec item is diff-confirmed, the marker scan is
clean, both structural validators pass, the mechanical audit is unchanged, and the two open
questions were answered from primary sources rather than guessed.

**Do not sign off Belgium.** §7 is unchanged and unworked.

Three things the owner should note before signing:

1. **`L-05` and `L-10` in the previous snapshot are now closed** and should be struck from the
   `compliance-source-hunter` queue. `L-05` (work-bonus cap after the 1 July 2026 indexation)
   closed at **EUR 3,594.36** from the now-published NSSO instructions **2026/3** — read from the
   instruction, not extrapolated, and independently reconciled against the monthly component
   maxima (171.99 + 127.54 = 299.53 × 12). `L-10` (the DD code tables) closed in full.
2. **Three artefacts carry a version of record that differs from their file name.** The DD is
   version **1.4** in a file still named `BE-DD-001-v1.3.xlsx`; the WTC is **1.1** in
   `BE-WTC-001-v1.0.xlsx`; the CCG records a 16 September revision while staying **v1.1**.
   This was deliberate: renaming would break the citations carried by the nine report
   specifications, the CCG and the WTC, which is outside this pass's fence. **The rename is the
   owner's call and is still owed.**

   > **CLOSED 16 September 2026 by the Stage 9.6 version-and-file-name pass.** The wording above
   > is left standing rather than rewritten, so the sequence of decisions stays auditable. Read it
   > as superseded. See §8 below. One of its three claims did not survive verification: the CCG's
   > internal version and its file name did **not** disagree — both read 1.1 — so the CCG needed a
   > version **bump**, not a rename.
3. **The generator-reproducibility gate has not been re-run.** This pass edited delivered files
   directly, which is the same shape as the F29 pattern that produced the 8,703-cell drift. The
   `_backport/` modules and `_pipeline/verify_generators.py` were **outside the fence and were not
   touched**, so the generators no longer reproduce the DD, the WTC or the CCG. **Run
   `_pipeline/verify_generators.py`, then fold these changes back into the `_backport/` data
   modules, before the next rebuild.** Treat this as the highest-priority follow-up.

---

## 7. Country-level findings carried forward, unchanged and unworked

Restated from the 2026-08-25 snapshot, which is preserved verbatim at
`handover_status.md.bak-before-stage95`. **This pass did not work any of these and does not claim
them closed.**

- **`BE-X10-010` — OPEN, owner ruling owed.** WTC `YTD Load` (col S) empty on all 359 rows.
  Column S is orange, and orange is the development team's. Do not fill it on a builder's
  initiative.
- **`BE-X10-006` — OPEN, not workable as written.** The finding names "6 cells across 3 artifacts";
  those 6 cells can no longer be identified. Re-scope before working.
- **`BE-TF-008`** DD changelog gaps at v1.2/v1.3 · **`BE-TF-009`** 7 `Sample File` header lines
  stored as formula cells (Excel will render `#NAME?`) · **`BE-TF-010`** SIR §2 / §2.3 wording.
- **`T-01`–`T-04`, `T-06`** tooling findings. **`T-05` — the payslip verifier still aborts on
  `IFERROR`, so the payslip remains the one artefact with no working gate.**
- **`L-06`** NSSO check-digit rule · **`L-07`** FinProf IY2026 period codes · **`L-08`** Belcotax
  IY2026 schema · **`L-09`** ITC 92 Art. 412 thresholds · **§4.5** the social-security side of
  severance (DmfA codes 3 and 9 confirmed; **812/90001 not confirmed**).
- **`L-15` — nothing has ever been submitted through a live channel.** This is what holds every
  accuracy band below 95%, and no amount of desk verification moves it.

---

## 8. Stage 9.6 — version of record reconciled with file name (16 September 2026)

Closes follow-up item 2 of §6. Scope was the three artefacts, the nine report specs,
`scope_manifest.json` and this file. Nothing else was edited.

**Step 1 — state confirmed by reading each file, not carried over from the Stage 9.5 handover:**

| File | Internal version, as read | Filename version | Mismatch |
|---|---|---|---|
| `BE-DD-001-v1.3.xlsx` | **1.4** (Version Control r17, eff. 2026-09-16, Released) | 1.3 | **Yes** |
| `BE-WTC-001-v1.0.xlsx` | **1.1** (Version Control r14, eff. 2026-09-16, Released) | 1.0 | **Yes** |
| `BE-CCG-001-v1.1.docx` | **1.1** (cover, 21 Aug 2026) | 1.1 | **No — but a bump was owed** |

The handover's claim that all three were mismatched was wrong on the CCG. The CCG carried a
16 September content revision at an unchanged version number, with the deferral stated on its own
cover. That deferral's only stated reason — keeping existing citations resolvable — is what this
pass exists to clear, and the DD and WTC both bumped for the same Stage 9.5 content. The CCG was
therefore bumped **1.1 → 1.2** (cover title, version line, revision note and page footer) before
being renamed. The CCG has **no Version Control section** at all, unlike the DD, the WTC and the
Bulgaria reference CCG, which carry one; that structural gap was found here, is **not** fixed, and
is logged as new open item **`BE-TF-011`**.

**Step 2 — renames, all by `git mv`:**

- `05-data-dictionary/BE-DD-001-v1.3.xlsx` → `BE-DD-001-v1.4.xlsx`
- `02-wtc/BE-WTC-001-v1.0.xlsx` → `BE-WTC-001-v1.1.xlsx`
- `01-ccg/BE-CCG-001-v1.1.docx` → `BE-CCG-001-v1.2.docx`

No `Archived/` copy was made: this is a filename correction to existing content, not a new version
superseding an old one. No stale prior-version deliverable sits in any artefact folder root — the
earlier `BE-CCG-001-v1.0.docx` and `BE-DD-001-v1.1.xlsx` were already in their `Archived/` folders.

**Step 3 — propagation, measured before it was promised:**

| File renamed | Old string | Hits found | Updated | Deliberately left |
|---|---|---|---|---|
| DD | `BE-DD-001[- ]v1.3` | 850 | 831 | 19 |
| WTC | `BE-WTC-001[- ]v1.0` | 54 | 52 | 2 |
| CCG | `BE-CCG-001[- ]v1.1` | 53 | 51 | 2 |

Found = updated + deliberately left, for every row. The hits span the 9 report specs (837 / 49 / 50),
`scope_manifest.json` (2 / 5 / 0) and the artefacts' own cross-citations (DD 1 / 0 / 1; WTC 10 / 0 / 2)
— not one sheet and not one file, which is why the count was taken before any edit.

The **23 left** are the cases where swapping the string would make a true sentence false: dated
records of a past edit (`"1 reference to BE-DD-001-v1.0 updated to BE-DD-001-v1.3"`), dated
existence claims (`"BE-DD-001-v1.3.xlsx since 16 August 2026"`), the name of a past event
(`"the BE-DD-001 v1.3 promotion"`), build provenance (`"Built from BE-CCG-001-v1.1"`), and the
literal on-disk name of a retained backup (`BE-WTC-001-v1.0.xlsx.bak-before-limosa-wording-fix`).
Two sentences that the rename made outright false were **rewritten**, not swapped: the DD's own
`FILE NAME UNCHANGED at BE-DD-001-v1.3.xlsx …` note (Version Control D17) and the CCG cover's
`Version number and file name deliberately unchanged …`.

**Step 4 — one stored figure genuinely moved, and it was not the rename that moved it.**
`scope_manifest.json` `option_mapper_scope._comment` measured its lock against **87** live mapper
blocks. Re-counted against the renamed file: **92 blocks / 1,816 code rows**. Stage 9.5 added five
blocks (Reference Type, NSSO Contribution Payment Purpose, Risk Identification, DmfA Remuneration
Code, DmfA Service Code); all 87 earlier blocks survive with identity intact, 0 removed, 0 renamed.
The lock's binding count therefore moves **6 of 11 → 8 of 11**, because `dmfa_remuneration_code`
and `dmfa_service_code` are recorded there as having no block of their own and now have one. Bound
header rows were restated against the live sheet (`joint_committee` r102 → r593, `withholding_scale`
r696 → r1473; the other four unchanged). Appended as a dated re-measurement; the original wording
is left standing. The `joint_committee` scope decision flagged in that block is **not** taken here.

**Verification.** Staged blobs were re-read from the index, not from the working tree: 831 / 49 / 51
new strings present, residual old strings exactly the 23 listed above, 0 unaccounted. All 11 edited
workbooks match their pre-edit backups on sheet names, sheet dimensions and populated-cell count;
the CCG keeps 1,255 paragraphs and 148 tables.

**Out of fence — found, reported, NOT edited.** Old version strings survive in files this pass was
not allowed to touch. They are now dangling, and closing them is owed:
`BE-SIR-001-v1.0.docx` (DD 2, WTC 1, CCG 3), `06-payslip/BE_Compliance_Payslip_Generator.xlsx`
(WTC 1), the five `08-skill/payroll-compliance-belgium/references/*.md`, `PROPAGATION-LEDGER.md`,
`05-data-dictionary/DD-CROSSCHECK-TABLE.md`, `_pipeline/build-manifest.json`, and the `_backport/`
generator modules. The historical QA reports under `07-qa-crosscheck/` also cite the old strings and
should stay as they are. Logged as new open item **`BE-TF-012`**.

**Item 3 of §6 is unaffected and still open.** This pass edited delivered files directly and did not
touch `_backport/` or `_pipeline/verify_generators.py`, so the generator-reproducibility gap is now
wider, not narrower.
