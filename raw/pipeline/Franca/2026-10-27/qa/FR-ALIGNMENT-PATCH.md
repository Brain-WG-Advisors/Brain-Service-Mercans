# FR-ALIGNMENT-PATCH — Data Dictionary vs Report Specs

**Date:** 2026-08-27
**Patched by:** Wallisson Gomes
**Scope:** `FR-compliance/05-data-dictionary/FR-DD-001-v1.0.xlsx` (v1.0 → v1.1) against the
15 delivered specs in `FR-compliance/04-reports-spec/` (each v1.0 → v1.1).

## Inputs actually read

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

## Patch log

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

## Check 2 — why nothing was changed

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

## Open items — NOT fixed, and why

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

## Verification

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
