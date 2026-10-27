# BE-compliance — Stage 10 QA Cross-Check, FINAL

**Date** 24 August 2026
**Scope** Full Stage 10, all 9 checks, re-run after the DD v1.1→v1.3 promotion, the CCG v1.0→v1.1
promotion, the 7 confirmed QA fixes, the 628-cell version-string propagation and the 2 closing CCG items.
**Method** Every number below was measured live against the files on disk in this session with
openpyxl / python-docx / raw-zip inspection. Nothing was carried over from
`BE-QA-REPORT-2026-08-21.md`, from `BE-FIX-LOG-2026-08-21.md` or from the task brief. Where a
figure in those documents was reproduced, it is marked **confirmed**; where it was not, it is
marked **refuted** with the measured value.
**Note on methodology source** No `mercans-pipeline-methodology` skill is installed on this machine
(`~/.claude/skills/` holds `country-build`, `graphify`, `mercans-artifact-toolkit`,
`mercans-pipeline-contracts`). Binary-artifact mechanics were taken from `mercans-artifact-toolkit`;
the C-check definitions from `shared/PRESUBMISSION_AUDIT.md`.

---

## Executive summary

### **8 of 9 checks fully passing. Check 4 passes on citation resolution and fails on option-mapper code-domain propagation.**

| # | Check | Verdict |
|---|---|---|
| 1 | CCG ↔ WTC alignment | **PASS** (1 MINOR) |
| 2 | CCG ↔ DD alignment | **PASS** |
| 3 | CCG ↔ Report Specs alignment (9) | **PASS** |
| 4 | DD ↔ Report Specs, 4-bucket (9) | **FAIL — 1 MAJOR, 2 MINOR** |
| 5 | Global WTC coverage audit | **PASS** — the CRITICAL fix held |
| 6 | Scope discipline (DD/WTC/CCG) | **PASS** (1 MINOR) |
| 7 | Report Spec format compliance (9) | **PASS 9/9** |
| 8 | Format / version standards | **PASS** (3 MINOR) |
| 9 | Composite key / inter-field (C13/C16/C17/C20) | **PASS** |

**The headline.** The promotion, the fix campaign and the 628-cell propagation did what they claim.
Every one of the 53 CCG citations, 636 DD-v1.3 strings, 300 baseline wage-type codes and 521
structured DD citations reproduces exactly on independent measurement. **One thing did not close**:
the v1.1→v1.3 DD promotion widened 9 option-mapper code domains, and only the version *string* was
propagated to the report specs — the resolved *content* was not. For eight of the nine blocks that
is inconsequential; for **Days Justification (NSSO zone 00625)** it means three report specs
publish a 5-code domain, and carry a `NOT FOUND`, for a zone the promoted DD records as
**confirmed complete at codes 1–7**. FIX 7, applied on 24 August, copied that stale table into a
fourth location and cited the contradicting DD block as its authority.

**Readiness: NOT ready for handover.** One MAJOR must be fixed first. It is a contained, ~15-cell
edit across 3 workbooks. Everything else is either MINOR or a documented, deliberately-deferred
open item.

---

## Artifacts read

| Artifact | Path | State |
|---|---|---|
| CCG | `01-ccg/BE-CCG-001-v1.1.docx` | 1 non-DRAFT ✅, v1.0 in `Archived/` ✅ |
| Report Specs | `04-reports-spec/` | 9 files ✅ |
| DD | `05-data-dictionary/BE-DD-001-v1.3.xlsx` | 1 non-DRAFT ✅, v1.1 in `Archived/` ✅ |
| WTC | `02-wtc/BE-WTC-001-v1.0.xlsx` | present |
| SIR | `03-statutory-integrations/BE-SIR-001-v1.0.docx` | present |
| Payslip | `06-payslip/BE_Compliance_Payslip_Generator.xlsx` | **present** — checked, not N/A |
| scope_manifest | `scope_manifest.json` | valid JSON, `scope_version` 2.3 |
| Global WTC | `shared/Global_WTC_V1_0.xlsx` | present, 300 codes — **not N/A** |
| Fix log | `07-qa-crosscheck/BE-FIX-LOG-2026-08-21.md` | read; every claim independently tested below |

`*DRAFT*` files anywhere under `BE-compliance/`: **0** — confirmed.
Zip integrity re-counted: DD **49/49** parts (`image1.png`, `image2.gif`, 3 comment parts, 3 VML
parts intact), CCG **19/19** (`docProps/thumbnail.jpeg` intact), WTC **23/23** (`image1.png`,
4 comment parts, 2 VML). All confirmed.

---

## CHECK 1 — CCG ↔ WTC alignment · **PASS** (1 MINOR)

26 shared statutory anchors were extracted and counted in both artifacts. Every one that appears in
both states the same value; **no contradiction was found**.

| Anchor | CCG | WTC | Anchor | CCG | WTC |
|---|---|---|---|---|---|
| Employee SS 13.07% | 65 | 141 | Overtime relief 66.81% | 2 | 17 |
| Pension levy 8.86% | 18 | 12 | Overtime relief 57.75% | 2 | 17 |
| Insurance premium tax 4.4% | 4 | 11 | Employer exemption 41.25% | 2 | 12 |
| Wijninckx 12.5% | 3 | 5 | Employer exemption 32.19% | 2 | 13 |
| Flexi-job employer 28% | 5 | 18 | Blue-collar 108% base | 22 | 29 |
| Student 2.71% / 5.42% | 3 / 3 | 7 / 7 | Student quota 650 h | 9 | 9 |
| Occasional 33% | 10 | 22 | Voluntary overtime 360 h | 2 | 12 |
| Meal voucher 1.09 / 8.91 | 13 / 5 | 9 / 5 | Fiscal work bonus EUR 765 | 9 | 3 |
| Asbestos 0.01% | 2 | 4 | Art. 23 one-fifth cap | 29 | 18 |

EUR-amount agreement on shared concepts is exact: GMMI `2,154.11 → 2,189.81 → 2,233.61` in both;
work-bonus figures `127.54`, `137.74`, `171.99`; special SS contribution `182.82`, `154.92`;
CBA 90 / eco-voucher ceilings `3,701` and `4,255`.

The WTC's 2 CCG citations are both `BE-CCG-001-v1.1` and resolve (Module 7.2, byte-identical
between v1.0 and v1.1).

> **MINOR — ISSUE-A.** `BE-WTC-001!'Wage Type Catalogue'!F323` and `!'Global WTC Coverage'!E37`
> configure **BE-022 Mobility budget pillar 3** with a **38.07% special employee contribution**.
> The CCG documents the mobility budget's three-pillar structure and pillar 2's double exemption
> (`CCG_v11` P650, Law of 17 March 2019) but **never states the 38.07% rate**. The rate is correct
> in Belgian law; the defect is that the WTC configures a parameter its own business source of
> truth does not carry. **Fix:** add the pillar-3 38.07% rate to CCG Module 7.2 with its legal
> basis, or record it as a WTC-side sourcing note.

---

## CHECK 2 — CCG ↔ DD alignment · **PASS**

| Measurement | Value |
|---|---|
| DD field names, `ID Information` | 26 |
| DD field names, `Country Fields` | 247 |
| Distinct union | **272** |
| Option-mapper blocks | **87** |
| Option-mapper code rows | **858** |
| DD → CCG citations | 1 (`Version Control!D13`), **v1.1**, resolves |
| CCG → DD references | 4, all **deliberately bare** `BE-DD-001` (no version) |

The CCG's four references are correct delegation, not stale citation — e.g. P80: *"Field-level
definitions, formats, mandatory flags and option-mapper codes are held in the Belgium Data
Dictionary (BE-DD-001) and are deliberately…"*. A CCG that named a DD version would go stale on
every DD release; leaving them unversioned is the right call and should not be "fixed".

**DD blue/orange discipline: PASS.** Orange columns (`ID Information` B, D, L–U; `Country Fields`
C, E, M–V) are empty on **every** data row — 0 populated cells, excluding the CZ template's own
mid-sheet header repeats. Header row 4, fill `FF4472C4`, Times New Roman 9pt bold, on all three
country sheets.

---

## CHECK 3 — CCG ↔ Report Specs alignment (all 9) · **PASS**

The CCG's Module 10.1 "all other mandatory reports" table (13 rows) was extracted with heading
context and reconciled against the 9 specs and against `scope_manifest.json`:

| CCG 10.1 / 10.2 row | Spec | Manifest |
|---|---|---|
| Dimona | `BE-NSSO-001` | in_scope `BE-NSSO-DIMONA-001` |
| DmfA | `BE-NSSO-002` | in_scope `BE-NSSO-DMFA-002` |
| Corrective DmfA (10.5) | `BE-NSSO-003` | within `BE-NSSO-DMFA-002` |
| Wage withholding tax return | `BE-FIN-001` | in_scope `BE-FIN-BV-003` |
| Form 281.10 | `BE-FIN-002` | in_scope `BE-FIN-28110-004` |
| ASR/DRS scenarios | `BE-NSSO-004` | in_scope `BE-NSSO-ASR-006` |
| Work accident (AOAT) | `BE-FEDRIS-001` | in_scope `BE-INS-WACC-010` |
| Limosa | `BE-NSSO-005` (**Descoped**) | **out_of_scope** `BE-NSSO-LIMOSA-009` |
| SEPA credit transfer (10.2) | `BE-FEBELFIN-001` | integration, outbound |
| 325.10, social balance sheet, work rules, individual account, DB2P | — | out_of_scope, each with a reason |

**Coverage is complete and the exclusions match the manifest item-for-item.**

50 CCG citations across the 9 specs, all `BE-CCG-001-v1.1`. `selfcheck_be_sir.py` CCG traceability:
**6/6 PASS** (Modules 1.2, 10.1, 10.2, 10.3, 10.4, 10.5).

---

## CHECK 4 — DD ↔ Report Specs, 4-bucket method (all 9) · **FAIL**

### 4a. Bucket census — every sheet-4 column-L cell classified

| Bucket | Cells |
|---|---|
| **B1** — explicit `BE-DD-001-v1.3 – 'Field' (Sheet)` citation | **521** |
| **B2** — `No DD field by design: …` | **242** |
| **B3** — other named system source (engine, constant, T&A, config) | **428** |
| **B4** — unresolved / `NOT FOUND` / `TBD` | **0** |
| (blank column L on a data row) | 209 |

### 4b. Citation resolution against the **live v1.3 DD** — the core test

Every citation was parsed and resolved against the field inventory of the named sheet of
`BE-DD-001-v1.3.xlsx` as it exists on disk right now.

```
521 citations parsed across the 9 specs
  wrong version (not v1.3)          0
  unknown sheet name                0
  field not present on named sheet  0
  ------------------------------------
  UNRESOLVED                        0     ✅
```

**Confirmed.** The fix log's "521 resolve" is exactly reproduced. Its one stated non-resolver
(`BE-WTC-001!'Form Reference Guide'!C2`, a citation *template* string) is correctly excluded from
the spec-side count. 18 further Limosa cells mention `BE-DD-001-v1.3` inside descoping prose
(*"'Posting Start Date' was REMOVED from BE-DD-001-v1.3 when the Limosa declaration was
DESCOPED"*) — correctly bucket B2, not citations, and each names a field that is indeed absent
from v1.3.

### 4c. Residual `v1.0` / `v1.1` citation strings — raw-XML byte sweep

Every zip part of every live deliverable (Archived and `_qa`/`_pipeline` scratch excluded):

| String | Count | Where |
|---|---|---|
| `BE-DD-001-v1.3` | **636** | 9 specs + WTC + DD |
| `BE-DD-001-v1.2` | 0 | — |
| `BE-DD-001-v1.1` | **0** | — ✅ |
| `BE-DD-001-v1.0` | **9** | 1 per spec, **all** at `'Version Control'!D15` |
| `BE-CCG-001-v1.1` | **53** | 50 specs + 2 WTC + 1 DD |
| `BE-CCG-001-v1.0` | **1** | SIR only (+2 spaced form) — see ISSUE-D |
| `BE-SIR-001-v1.0` | 55 | unmoved |
| `BE-WTC-001-v1.0` | 51 | unmoved |

**Zero stale DD citations.** The 9 remaining `v1.0` strings are the changelog rows that *narrate
the swap itself* — e.g. *"DD version alignment. 3 references to BE-DD-001-v1.0 updated to
BE-DD-001-v1.3."* Rewriting those would falsify the audit trail. Strictly the brief's "zero
residual v1.0 anywhere" is not met; substantively it is, and correctly so.

The `BE-SIR-001-v1.0 ×51` / `BE-WTC-001-v1.0 ×49` / `BE-DD-001-v1.0 ×9` census recorded in the fix
log is **confirmed to the digit** (my 51/55 figures differ only because I also count the SIR's and
WTC's own self-identifying strings).

Also **confirmed**: `BE-NSSO-003!'Field Options'!E28` is the single surviving `v1.1` substring
(`"BE-NSSO-002-DmfA-Spec.xlsx v1.1, sheet Field Options"`) — a spec-to-spec reference, proving the
swap was anchored on the full document id and not a blind `v1.1`.

### 4d. Option-mapper code domains — **where this check fails**

The STEP 4 gate tested that the DD's **field inventory** was unchanged (27/27, 248/248, 0 added,
0 removed) and concluded "the pure string swap was legitimate". That gate is sound for field names.
It does not cover **option-mapper code domains**, and 9 of them widened:

| DD block | v1.1 | v1.3 | Spec impact |
|---|---|---|---|
| NIS Country Code | 2 | 417 | Dimona r52 still `NOT FOUND` |
| Health Insurance Fund Code | 1 | 79 | none |
| Activity With Risk | 1 | **18** | Dimona r50, DmfA r29, FEDRIS r9 still `NOT FOUND` |
| Work Reorganisation Measure | 1 | 15 | none |
| NSSO Worker Status | 3 | 14 | none |
| NSSO Worker Code | 1 | 12 (+`NOT FOUND` remainder) | partial |
| Joint Committee Number | 8 | 16 (+`NOT FOUND` remainder) | partial |
| Employment Promotion Measure | 1 | 5 | none |
| **Days Justification** | **6** | **7** | **3 specs stale — MAJOR** |

Block **titles** are identical between v1.1 and v1.3 in membership *and* order (87 = 87, 0 added,
0 removed) — **confirmed**. Only code rows moved (299 → 858).

> ### **ISSUE-B — MAJOR. Days Justification (zone 00625): three report specs publish a 5-code domain the promoted DD contradicts.**
>
> `BE-DD-001-v1.3!'Country Option Mappers'!r906–r913` holds codes **1–7** and an explicit
> completeness certificate at `F913`:
> *"CONFIRMED SUBSTANTIALLY COMPLETE (21 Aug 2026): codes 1–7 verified across two independent
> passes — the original NSSO glossary domain-of-definition text (codes 1–5, with 5 corrected here
> to its full un-truncated wording) and the current ONSS administrative instructions 2024/3–2026/2."*
> The DD's own v1.3 changelog (`Version Control!D16`) says it outright: *"Days Justification zone
> 00625 completed to codes 1-7 (was 1-5, truncated)."*
>
> Three specs still carry codes **1–5** only, each ending on the superseded gap note
> *"NOT FOUND - the definition domain quoted in column O of sheet 4 is TRUNCATED mid-sentence at
> value 5"*:
>
> | Location | Rows |
> |---|---|
> | `BE-NSSO-002-DmfA-Spec!'Field Options'!A97:E101` | codes 1–5 |
> | `BE-NSSO-004-DRS-Spec!'Field Options'!A85:E89` | codes 1–5 |
> | `BE-NSSO-003-DmfAModification-Spec!'Field Options'!A30:E34` | codes 1–5 |
>
> **The third is worse than stale — it was created after the DD had already resolved the gap.**
> FIX 7 (24 August) propagated the DRS table verbatim into `BE-NSSO-003`, and `E30` cites
> *"NSSO DRS glossary 2026/2, zone 00625; **BE-DD-001-v1.3 option mapper "Days Justification"**"*
> as its authority — a citation to the very block that contradicts it. The section marker at `A29`
> reads *"THE FULL GLOSSARY DOMAIN OF THE ZONE"*, which is now false.
>
> **Failure scenario.** Zone 00625 is a live DmfA/DRS zone (`DmfA Modification Spec!D80` declares
> it). A build validating this zone against the specs' Field Options rejects codes **6**
> (*combination of 3+5 or 4+5*) and **7** (*no services due for the quarter*) as out-of-domain.
> Code 7 is not an edge case — it covers any worker with a zero work regime for a quarter.
>
> **Fix.** Add code 6 and code 7 rows to all three tables from `BE-DD-001-v1.3!'Country Option
> Mappers'!r911:r912`; replace the code-5 `NOT FOUND` note in column E with the DD's corrected
> un-truncated wording; re-point the `A29` marker text. ~15 cells across 3 workbooks. Then re-run
> `validate_workbook.py --artifact RSPEC` and `verify_specs.py` to confirm the 11-error baseline
> is unmoved.

> **MINOR — ISSUE-C.** The v1.3 DD resolved research gaps that 5 spec `NOT FOUND` rows still
> declare open: **Activity With Risk (00041)** — DD holds all 18 codes (001–006, 401–412) with no
> remainder row, while `BE-NSSO-001!'Field Options'!B50`, `BE-NSSO-002!B29` and
> `BE-FEDRIS-001!B9` still say *"requires NSSO Annexe 6 from the TechLib"*; and **NIS country codes**
> — DD holds all 417, while `BE-NSSO-001!'Field Options'!B52` still says *"requires the NIS country
> code table from Statbel"*. Also `BE-NSSO-004!'Field Options'!E114` still calls the Legal Basis
> (00096) domain *"TRUNCATED mid-sentence at value 4"*, which the DD's 21 Aug LOIC-glossary pass
> superseded (`F1033`: *"That source shows NO 5th value"*). **Fix:** replace each with a pointer to
> the DD block. Joint Committee Number and NSSO Worker Code keep an explicit `NOT FOUND` remainder
> in the DD itself, so those spec rows are not false — but they should point at the partial list.

Total `NOT FOUND` option rows across the 9 specs: **39**. The other 34 are genuine, correctly
recorded external dependencies (NSSO TechLib annexes 2/3/4/7/8/12/34, WECH/ZIMA/TWCT glossaries,
Limosa web-only, Finprof enquiries).

---

## CHECK 5 — Global WTC coverage audit · **PASS — the CRITICAL finding stayed fixed**

`shared/Global_WTC_V1_0.xlsx` is present (300 codes, 3 columns). **Not N/A.**

`diff_wtc_baseline.py` against the live catalogue:

```
BASELINE  Global_WTC_V1_0.xlsx [Sheet1]  300 codes
  KEPT     300      MISSING  0      ADDED  59      RENAMED  299
  duplicate codes in country: 0      in baseline: 0
```

### Coverage sheet vs. live catalogue — every certified number re-measured

| `'Global WTC Coverage'` asserts | Live measurement | |
|---|---|---|
| 300 baseline codes at catalogue rows **2–301** | 300 non-BE codes, rows **2–301** | ✅ |
| of which deduction **54** | Global WTC type `deduction` = **54** | ✅ |
| of which contribution **5** | `contribution` = **5** | ✅ |
| of which earning **240** | `earning` = **240** | ✅ |
| of which rate **1** | `rate` = **1** | ✅ |
| Belgium-specific additions **59**, rows **302–360** | 59 rows, `BE-001`…`BE-059`, rows 302–360 | ✅ |
| **TOTAL CATALOGUE ROWS 359**, rows 2–360 | **359** data rows, 2–360 | ✅ |

**The coverage certificate is internally consistent with the live catalogue in every field.** The
CRITICAL finding from two passes ago is closed and survived both the promotion and the propagation.

### Tax-Code family — independently re-measured

| Metric | Fix log | Measured now | |
|---|---|---|---|
| Wage types (data rows) | 359 | **359** | ✅ |
| Last spreadsheet row | 360 | **360** | ✅ |
| BE-prefix additions | 59 | **59** | ✅ |
| Distinct Tax Code values | 24 | **24** | ✅ |
| Real Belcotax box codes (excl. `NA`) | 23 | **23** | ✅ |
| Rows with Tax Code = **250** | 147 | **147** | ✅ |
| Rows with Tax Code = `NA` | 125 | **125** | ✅ |

**Every figure in the fix log's catalogue table is confirmed.** BE-059 is present at catalogue row
360 with `Tax Code = NA`, exactly as claimed.

### The 355 → 359 / 144 → 147 propagation family

Swept across all 9 specs and the WTC. Every live count now reads **359** and **147**; `125` appears
correctly in `BE-FIN-002!'Population Rules'!D14`. The **355** strings that survive (one per spec,
`'Version Control'!C18`/`C19`) are inside the explicitly-quoted superseded justification followed by
`SUPERSEDED 17 August 2026` — **correctly left alone**. `BE-WTC-001!'Version Control'!D13`'s
*"plus 55 Belgium-specific wage types"* is the **version-1 changelog row dated 13 August 2026**,
when there were exactly 55 — historically correct, **confirmed as a non-defect**. The surviving
`144` strings are joint-committee code `144` and NSSO anomaly codes, not counts.

`RENAMED 299` remains the documented by-design divergence (Belgian descriptions replace generic
baseline text while codes and order are preserved). Unchanged from the 21 August figure.

---

## CHECK 6 — Scope discipline (DD / WTC / CCG) · **PASS** (1 MINOR)

`scope_manifest.json`: valid JSON, `scope_version` 2.3, decided by Wallisson Gomes on 2026-08-12,
last updated 2026-08-18. **8** in-scope authority filings, **10** out-of-scope, each with a written
`descoping_reason`. `_revision_history` 14 entries, `known_limitations` 17,
`known_failure_patterns_to_check` 28 (F1–F28 as objects). `mandate_document`
`BE-compliance/BE-COVERAGE.md` — **verified present on disk**.

**Limosa is the discipline test, and it passes cleanly.** Descoped in the manifest as two separate
items (`BE-NSSO-LIMOSA-009` the declaration, `BE-NSSO-LIMOSA-L1-VERIFY` the article-141 check), and
the descope is stated consistently in all four places:

- CCG P84, P944–P949: a full sub-section explaining that the filer is the *foreign posting employer*,
  with legal basis, and *"an unqualified 'mandatory' in a table a Belgian payroll implementer reads
  is a scope error rather than a nuance"*;
- CCG Module 10.1 table row: *"mandatory for the FOREIGN posting employer, NOT for the Belgian
  payroll client. Out of scope for this build"*;
- `BE-SIR-001` registers it as OUT-08, descoped and exception-only;
- `BE-NSSO-005-Limosa-Spec.xlsx` carried at **v1.3, Status `Descoped`**, and its 18 sheet-4 cells
  say *"was REMOVED from BE-DD-001-v1.3 when the Limosa declaration was DESCOPED"* — the DD
  confirms those fields are absent.

This is exactly the manifest's own rule ("out-of-scope codes MAY be carried with an explicit
descoping note; removing them is not the correct treatment"). Out-of-scope employment types
(directors, self-employed, agency workers, A1-covered posted workers) are likewise retained as
guarded exclusions — e.g. DD Worker Status code 9 carries a 5-line descoping note rather than being
deleted.

### Mapper-block comment vs the live v1.3 sheet — re-measured, not reused

Every claim in `scope_manifest.json → option_mapper_scope._comment` was tested:

| Claim | Measured | |
|---|---|---|
| 87 live mapper blocks | **87** | ✅ |
| 11 scope keys named | 12 keys − `_comment` = **11** | ✅ |
| Sheet grew 475 → 1043 rows | `Country Option Mappers` max_row **475** (v1.1) → **1043** (v1.3) | ✅ |
| Block titles identical in membership **and order**, 0 added / 0 removed | **True** | ✅ |
| Only **6 of 11** keys bind to a block | 6 — and all 6 named header rows verified: r12, r47, r51, r59, r102, r696 | ✅ |
| "other" = **81**, superseding 76 | 87 − 6 = **81** | ✅ |
| Exactly **9** blocks widened, with the stated counts | **9**, all counts exact | ✅ |
| The lock covers **one** widened block (Joint Committee 8 → 16) | Confirmed — `worker_status` binds to r59, unchanged at 6 codes | ✅ |
| The self-correction: `NSSO Worker Status` is a *different* mapper (r67) and nothing binds to it | Confirmed | ✅ |

**The mapper-block comment is accurate in every particular, including its own two self-corrections.**
The "6 of 87 locked / 81 unlocked" figure in the brief is confirmed by live re-measurement.

> **MINOR — ISSUE-E.** `scope_manifest.json` still carries **14 × `BE-DD-001-v1.1`** and
> **4 × `BE-DD-001-v1.0`** inside `option_mapper_scope.*._bound_to` pointers — e.g.
> `contract_type._bound_to: "BE-DD-001-v1.1.xlsx!Country Option Mappers!B48:F49"`. The 628-cell
> propagation covered `.xlsx` cells only and never touched the manifest. The row ranges still
> resolve (blocks r47/r51 are unchanged), so nothing is *wrong* — but a lock that names a superseded
> file is the same class of defect the propagation existed to remove. **Fix:** re-point the 14 v1.1
> `_bound_to` strings to `BE-DD-001-v1.3.xlsx`. Leave `source_artifact: "BE-CCG-001-v1.0.docx"`
> and the 4 historical v1.0 strings alone — those record what the scope was *decided from* on
> 2026-08-12 and are correct as history.

---

## CHECK 7 — Report Spec format compliance, all 9 · **PASS 9/9**

`validate_workbook.py --artifact RSPEC` on each of the nine:

```
BE-FEBELFIN-001  PASS  blocker=0 major=0 minor=0      BE-NSSO-002  PASS  0/0/0
BE-FEDRIS-001    PASS  blocker=0 major=0 minor=0      BE-NSSO-003  PASS  0/0/0
BE-FIN-001       PASS  blocker=0 major=0 minor=0      BE-NSSO-004  PASS  0/0/0
BE-FIN-002       PASS  blocker=0 major=0 minor=0      BE-NSSO-005  PASS  0/0/0
BE-NSSO-001      PASS  blocker=0 major=0 minor=0
```

All nine: **9 sheets in contract order**, core sheet at index 4 named `<Report> Spec`, header
**row 1**, **21/21 columns A–U** populated, header fill `FF4472C4`, **Google Sans 11pt bold**,
freeze `B2`. Sheet 9 is named `Sample File` in all nine (the toolkit's `<Fmt> Sample File` is the
Spain precedent's convention; the BE set is internally consistent and `validate_workbook.py`
accepts it).

`verify_specs.py`: **11 ERRORS — C6 × 8 + C7 × 3.** **Confirmed identical to the documented
baseline**; no regression from the promotion, the propagation or the citation swap.

- **C6 × 8** — Version Control lacks the Stage 4 / DD pending note. Now arguably obsolete: Stage 4
  is delivered and every citation resolves. The check, not the file, is stale.
- **C7 × 3** — `BE-NSSO-005-Limosa-Spec!'Payroll Scope Summary'!B15`, `B17`, `B18` answer `NO` but
  are filled green `FFC6EFCE` instead of red `FFFFC7CE`. **Independently re-confirmed: exactly
  these three, and every other `NO` in the sheet (B11, B12, B13, B16, B23) is correctly red.** This
  is OPTIONAL ISSUE-5, deliberately not fixed. A 3-cell fill change.

---

## CHECK 8 — Format / version standards · **PASS** (3 MINOR)

| Gate | Result |
|---|---|
| `validate_workbook.py --artifact DD` | **PASS** blocker=0 major=0 minor=0 |
| `validate_workbook.py --artifact WTC` | **PASS** blocker=0 major=0 minor=0 |
| `validate_workbook.py --artifact PSL` | **PASS** blocker=0 major=0 minor=0 |
| `validate_workbook.py --artifact RSPEC` × 9 | **PASS 9/9** |
| **C29 residual-marker lint, 14 live deliverables** | **0 hits** ✅ |
| `selfcheck_be_sir.py` | **0 failures** |
| `selfcheck_be_wtc.py` | 1 failure — the documented `ORANGE populated` (column A Mercans Code), by design per CZ precedent, stated in `WTC!'Version Control'!C28` |
| `verify_be_dd.py` | `FAIL C1` — 8 unclassified spec fields, `592 resolve / 0 missing` |

**The `verify_be_dd.py` pre-existence claim: independently confirmed.** I re-ran the verifier against
the **archived v1.1** DD and got identical output — the same 8 fields (6 FEDRIS accident-circumstance
fields, 2 DRS nature-advantage dates), the same `592 resolve / 0 missing`. **Not a promotion
regression.**

**CCG structure.** 1253 paragraphs, 212 headings (14 H1 + 39 H2 + 159 H3), **148 tables**, 27,670
words. Cover line `Version 1.1 — 21 August 2026`, title `… BE-CCG-001 v1.1`, footer
`BE-CCG-001 v1.1 | Mercans Compliance Regulations Team | 2026` — **all three promoted, confirmed.**

**Payslip: 8/8 contract sheets present** — `How to set up Payslip`, `Compliance Payslip`,
`Belgium (EN)`, `Belgium (NL)`, `Payslip Spec` (header row 3), `Field Option`, `Population Range`,
`Unit Rate Details` (header row 2). The three sheets past builds deleted are all present.

> **MINOR — ISSUE-F.** `BE-DD-001-v1.3!'Version Control'!D15`, `E15` and `F15` are **all empty**.
> Row 15 is version **1.2**, effective 2026-08-20 — it has a version number and a date but **no
> Change Description, no Status and no Updated By**, while rows 13 (v1.0) and 14 (v1.1) carry all
> three. `F16` (Updated By for v1.3) is **also empty**. STEP 1 found and fixed `E16` (Status →
> `Released`) but did not sweep the rest of the block. A promoted deliverable should not ship a
> blank changelog row. **Fix:** populate `D15`/`E15`/`F15` and `F16`.

> **MINOR — ISSUE-G.** **All 9 report specs are Status `Draft`.** Every spec's Version Control
> shows `1.0 [Draft] ; 1.1 [Draft] ; 1.2 [Draft]` — none declares itself Released. (Limosa adds
> `1.3 [Descoped]`, which is correct.) The DD says `Released` and the CCG is promoted; the specs
> were left behind. **Fix:** set the current-version Status to `Released` on the eight in-scope
> specs once ISSUE-B is closed.

> **MINOR — ISSUE-D.** **The SIR was left out of the citation swap entirely**, and one of its
> three stale references is a **dead file path**:
>
> | Location | Text |
> |---|---|
> | `BE-SIR-001!P14` | *"Source of business content: BE-CCG-001 **v1.0**, read in full."* |
> | `BE-SIR-001!` table 0 [r1,c1] | *"BE-CCG-001 **v1.0**, read in full from the current document, principally Modules 1.2, 10.1…"* |
> | `BE-SIR-001!` table 43 [r1,c1] | **`BE-compliance/01-ccg/BE-CCG-001-v1.0.docx`** — **this path no longer exists**; the file is now at `01-ccg/Archived/`. |
>
> ITEM A's scope was "9 report specs + WTC + DD"; the SIR was never in it, and the fix log does not
> flag the omission. The A.3 safety proof already covers this: Modules 1.2, 10.1–10.5 are all
> byte-identical between v1.0 and v1.1, so the swap is provably safe. **Fix:** update
> `sections/s00_control.md:19`, `sections/s07_sources.md:9` and `build_sir_docx.py:4,261`, then
> re-run `build_sir_docx.py` — the same source-first discipline ITEM B applied to the CCG.

---

## CHECK 9 — Composite key / inter-field constraints · **PASS**

**C13 — composite-key construction rules** (sheet 4 column M: composite / construction / check
digit / modulo / concatenate / unique key). **47 rows**, distributed exactly as the prior pass
recorded:

| Dimona | DmfA | DmfA Mod | Finprof | DRS | WorkAcc | SEPA | Limosa | Belcotax |
|---|---|---|---|---|---|---|---|---|
| 12 | 9 | 9 | 5 | 5 | 3 | 2 | 2 | **0** |

Belcotax's 0 is correct — its identifiers are single-valued box codes, not composites. **PASS.**

**C16 — inter-field constraint documentation.**

```
Rows with Mandatory = 'C'            503
  ...carrying a Conditional Reason   503     100.0%, zero gaps
Zone references in Conditional Reason absent from own workbook:  0
```

**Confirmed at 503/503.** The prior pass's ISSUE-10 (two conditional rules keying off unresolvable
zones) is **now closed, and one half of it was a misreading**:

- `BE-FEDRIS-001!'Work Accident Spec'!G99` now carries an explicit Stage-8 alignment note:
  *"this condition cites zone 00431 for Has Changed Of Function, but that field is recorded at zone
  00432 on row 100 of this sheet. One of the two numbers is a transcription error in the held
  source."* The conflict is documented rather than hidden — acceptable.
- `BE-NSSO-004!'DRS Spec'!G85`'s "20072" is **a quarter identifier (2007 Q2)**, not a zone:
  *"…une administration provinciale ou locale et un trimestre antérieur à 20072…"*. There was never
  a missing zone here. **The prior pass's finding is refuted.**

**C17 — cross-reference table.** `BE-WTC-001!'Form Reference Guide'` present as sheet 6. Still
**2 rows** (1 header + 1 blanket delegation row) — ISSUE-7, confirmed open and deliberately not
restructured. Its *content* is now correct and current: `A2` reads **359** (not 355), `B2` reads
**23 box codes + NA across 359 rows** and correctly states *"eight at v1.2, BE-NSSO-005 at v1.3
(DESCOPED)"*, `D2` points at **BE-DD-001-v1.3**, and `E2` reads *"CROSSWALK MAINTAINED ELSEWHERE —
not pending"*. **The stale-355 and the unresolved OPEN ITEM are both gone from the artifact.** The
remaining gap is structural only (a 9-row per-form index was never built).

**C20 — scope decision audit trail.** Complete: `scope_version` 2.3, decided-by/on and last-updated
all populated, `_revision_history` 14, `known_limitations` 17,
`known_failure_patterns_to_check` 28, `tier.by_domain` across 13 domains with a written rationale,
8 in / 10 out filings each with a reason, `mandate_document` present on disk. **PASS.**

---

## Fix-log claim register — confirmed or refuted, item by item

| # | Claim | Verdict |
|---|---|---|
| — | Live catalogue: 359 rows / last row 360 / 59 BE / 24 tax codes / 23 real / 147 at 250 / 125 NA | **CONFIRMED — all 7 figures exact** |
| FIX 3 | BE-059 added at catalogue row 360, `Tax Code = NA` | **CONFIRMED** |
| FIX 1 | Global WTC Coverage certifies the live catalogue (300/54/5/240/1/59/359, rows 2–301 & 302–360) | **CONFIRMED — every field** |
| FIX 1 ext | 355→359 and 144→147 corrected in 13 cells; 355 kept only in the quoted superseded text; `D13`'s "55" historically correct | **CONFIRMED** |
| FIX 2 | 226 DD-bucket rows now cite the DD resolvably | **CONFIRMED** — only **4** `master data` rows remain in column L, and all 4 legitimately use the phrase to explain why no DD field exists (*"transactional rather than master data"*) |
| FIX 4 | Stale version labels corrected | **CONFIRMED** |
| FIX 5 | Mapper count corrected (11 keys / 87 blocks) | **CONFIRMED** |
| FIX 6 | "placeholder" wording removed from the SIR | **CONFIRMED** — C29 lint 0 hits across all 14 deliverables |
| FIX 7 | Days Justification 00625 propagated into `BE-NSSO-003`; Legal Basis 00096 **deliberately not** propagated | **CONFIRMED as executed** — table written at `'Field Options'!A29:E34`; zone 00096/00095 appear nowhere in `BE-NSSO-003` (only an unrelated `Report Matrix!I26` header), so withholding it was **correct**. Zone 00625 *is* declared at `'DmfA Modification Spec'!D80`, so placing it there was correct. **BUT the propagated content was already stale — see ISSUE-B.** |
| FIX 7 | DRS Days Justification holds codes **1–5**, not 1–7 as the audit said | **CONFIRMED for the DRS spec, but the conclusion drawn from it is now wrong** — the DD was completed to 1–7 on 21 Aug, three days before FIX 7 ran. "There is no source on disk for codes 6 or 7" is **refuted**: `BE-DD-001-v1.3!'Country Option Mappers'!r911–r913` is that source. |
| ISSUE-5 | 3 green `NO` fills in Limosa Payroll Scope Summary, exactly B15/B17/B18 | **CONFIRMED — still open, still exactly 3** |
| ISSUE-7 | Form Reference Guide still a 2-row sheet | **CONFIRMED — still 2 rows; content now accurate** |
| STEP 1 | DD promoted; 1 non-DRAFT; 0 DRAFT files; `E16 = Released`; 49/49 parts | **CONFIRMED** (see ISSUE-F for what was missed) |
| STEP 2 | CCG promoted; cover/title/footer all v1.1; 19/19 parts; 1253 paras / 212 headings | **CONFIRMED** |
| STEP 3 | 87 blocks; titles identical; 9 widened; 6 of 11 keys bind; 81 not 76 | **CONFIRMED in every particular** |
| STEP 4 | 628 cells swapped, 0 left at v1.1; `BE-NSSO-003!'Field Options'!E28` the only surviving `v1.1` substring; other families unmoved | **CONFIRMED** — live totals `v1.3 = 636`, `v1.1 = 0`, `v1.0 = 9` (all changelog prose) |
| STEP 5 | 521 of 522 citations resolve | **CONFIRMED — 521/521 spec-side citations resolve, 0 unresolved** |
| STEP 5 | `verify_be_dd.py` C1 failure is pre-existing, proven by A/B against archived v1.1 | **CONFIRMED — I re-ran the A/B myself; output identical** |
| STEP 5 | `verify_specs.py` 11 errors = baseline, no regression | **CONFIRMED — C6 × 8 + C7 × 3** |
| STEP 5 | `diff_wtc_baseline.py` kept 300 / missing 0 / renamed 299 / added 59 | **CONFIRMED exactly** |
| ITEM A.1 | 53 v1.0 CCG citations: 50 specs + 2 WTC + 1 DD, with the stated per-file split | **CONFIRMED to the cell** |
| ITEM A.2 | v1.0 and v1.1 structurally identical: 1253 / 212 / 148 | **CONFIRMED** |
| ITEM A.5 | Post-swap: `BE-CCG-001-v1.0 = 0`, `v1.1 = 53` across the 11 files | **CONFIRMED by raw-XML byte sweep** |
| ITEM A.5 | `BE-NSSO-003!'Population Rules'!E4` deliberately unswapped (bare `Module 5.1.1`) | **CONFIRMED** |
| ITEM B | `build_ccg_docx.py` reproduces v1.1 exactly | **CONFIRMED — I regenerated the CCG in a sandbox from the live `modules/` sources: 4,814 comparable units, 0 differing, header/footer identical** |

**One fix-log conclusion is refuted** (FIX 7's "no source on disk for codes 6 or 7"), and **one
omission is unflagged** (the SIR was outside ITEM A's scope). Everything else the fix log claims is
true on independent measurement.

---

## Issues still open

| ID | Sev | Check | Location | Issue | Fix |
|---|---|---|---|---|---|
| **B** | **MAJOR** | 4 | `BE-NSSO-002!'Field Options'!A97:E101`, `BE-NSSO-004!A85:E89`, `BE-NSSO-003!A30:E34` | Days Justification (00625) published as a 5-code domain with a superseded `NOT FOUND`; DD v1.3 records codes 1–7 as confirmed complete. `BE-NSSO-003!E30` cites the contradicting DD block as its authority. | Add codes 6 & 7 from `DD!'Country Option Mappers'!r911:r912`; replace the code-5 note with the DD's un-truncated wording; correct the `A29` marker. ~15 cells. |
| **C** | MINOR | 4 | `BE-NSSO-001!'Field Options'!B50,B52`, `BE-NSSO-002!B29`, `BE-FEDRIS-001!B9`, `BE-NSSO-004!E114` | Spec `NOT FOUND` rows for Activity With Risk (00041), NIS country codes and Legal Basis (00096) that the v1.3 DD has since resolved. | Replace each with a pointer to the DD block. |
| **D** | MINOR | 8 | `BE-SIR-001!P14`, table 0[1,1], table 43[1,1] + `sections/s00_control.md:19`, `s07_sources.md:9`, `build_sir_docx.py:4,261` | SIR still cites CCG v1.0; one reference is a **dead path** (`01-ccg/BE-CCG-001-v1.0.docx`). SIR was outside ITEM A's scope. | Edit the 3 sources, re-run `build_sir_docx.py`. Safety already proven by A.3. |
| **E** | MINOR | 6 | `scope_manifest.json → option_mapper_scope.*._bound_to` | 14 × `BE-DD-001-v1.1` (+4 historical v1.0) survive the propagation; ranges still resolve. | Re-point the 14 to v1.3; leave the historical v1.0 strings. |
| **F** | MINOR | 8 | `BE-DD-001-v1.3!'Version Control'!D15,E15,F15,F16` | v1.2 changelog row has no Description, Status or Updated By; v1.3 has no Updated By. | Populate the 4 cells. |
| **G** | MINOR | 8 | All 9 specs, `'Version Control'` Status column | Every spec still `Draft`; DD is `Released`, CCG promoted. | Set current-version Status to `Released` on the 8 in-scope specs after ISSUE-B closes. |
| **A** | MINOR | 1 | `BE-WTC-001!'Wage Type Catalogue'!F323`, `'Global WTC Coverage'!E37` | WTC configures the 38.07% mobility-budget pillar-3 contribution; the CCG never states the rate. | Add it to CCG Module 7.2 with legal basis. |
| ISSUE-5 | OPTIONAL | 7 | `BE-NSSO-005!'Payroll Scope Summary'!B15,B17,B18` | Three `NO` answers filled green instead of red. Raises 3 of the 11 `verify_specs.py` errors. | 3-cell fill change to `FFFFC7CE`. |
| ISSUE-7 | OPTIONAL | 9 | `BE-WTC-001!'Form Reference Guide'` | Still a 2-row delegation stub rather than a 9-row per-form index. Content now correct. | Structural rebuild, or accept and record as a design decision. |
| C6 × 8 | INFO | 7 | 8 specs, `'Version Control'` | `verify_specs.py` demands a "Stage 4 / DD pending" note. Stage 4 is delivered and every citation resolves — **the check is stale, not the files.** | Retire the C6 assertion or re-scope it. |

---

## Readiness verdict

### **NOT ready for handover. One MAJOR blocks it. Everything else is MINOR or a recorded design decision.**

**What is genuinely closed.** This build is in good shape and today's chain of work substantially
did what it claims. The CRITICAL coverage-certificate defect is fixed and **stayed** fixed through
both the promotion and the propagation — all 300 baseline codes, the 54/5/240/1 type split, the 59
BE additions and the 359-row total reconcile exactly with the live catalogue, as do all seven
Tax-Code figures. Both promotions are clean: one non-DRAFT file each, predecessors archived, zero
DRAFT files anywhere, zip parts and embedded media intact. All 53 CCG citations and all 636 DD-v1.3
strings reproduce to the cell under a raw-XML byte sweep. **All 521 structured DD citations resolve
against the live v1.3 DD, with zero broken references** — the single most important result in this
report. C29 residual-marker lint is clean across all 14 deliverables. The twelve
`validate_workbook.py` gates pass with zero findings. `verify_specs.py` sits exactly on its
11-error baseline with no regression. C16 is 503/503 with no gaps, and the prior pass's ISSUE-10 is
resolved — half of it having been a misreading. The CCG generator reproduces the live v1.1 document
with **0 differing units out of 4,814**, so the source-of-truth sync is real. The scope-manifest
mapper-block comment is accurate in every particular including its own two self-corrections. The
Limosa descope is handled consistently across four artifacts.

**What blocks it.** The version-string propagation was gated on the DD's *field inventory* being
unchanged, which it was. But the promotion also widened **9 option-mapper code domains**, and that
content was never propagated. For eight blocks it does not matter. For **Days Justification (zone
00625)** it means three report specs publish a 5-code domain — and a stale `NOT FOUND` — for a zone
the promoted DD certifies as complete at codes 1–7. A build validating that zone against the specs
rejects code 6 and code 7 as out-of-domain, and code 7 (*no services due for the quarter*) is a
routine case, not an edge case.

FIX 7 makes this sharper rather than softer. It ran on 24 August, three days *after* the DD closed
the gap, copied the stale DRS table into a fourth location, labelled it *"THE FULL GLOSSARY DOMAIN
OF THE ZONE"*, and cited `BE-DD-001-v1.3` — the block that contradicts it — as its authority. The
fix log's reasoning at the time (*"There is no source on disk for codes 6 or 7"*) was wrong when
written: `BE-DD-001-v1.3!'Country Option Mappers'!r911–r913` is exactly that source, and the DD's
own changelog announces it.

**The gap to close is narrow.** ISSUE-B is roughly 15 cells across 3 workbooks, all with the
authoritative content already sitting in the DD. Fixing it alongside ISSUE-C, D, E, F and G is
comfortably a single short session. I'd sequence it as: **ISSUE-B first** (it is the only one that
can produce a wrong build), then **C** (same root cause, same sweep), then **D/E/F/G** as version
hygiene, then re-run `validate_workbook.py` × 12, `verify_specs.py` and `diff_wtc_baseline.py` to
confirm the 11-error baseline and the 300/0/59 baseline are both unmoved.

**One process recommendation.** The STEP 4 gate — "field inventory unchanged, therefore the string
swap is legitimate" — is the thing that let this through, and it will let the next one through
too. A DD version promotion needs a **second** gate: *diff the option-mapper code domains, and for
every block that widened, sweep the report specs for a `NOT FOUND` or a short domain on that zone.*
Nine blocks widened here; a one-line check would have caught all four affected specs before FIX 7
propagated the stale one.

---

*Measured and written 24 August 2026. Working artifacts under
`07-qa-crosscheck/_final_qa/` (corpus dumps, resolution engines, bucket census, mapper diffs).*
