# BE — Generator / Back-port Drift Diagnosis

**Stage:** 9.7 — diagnosis only, no fixes applied
**Date:** 16 September 2026
**Author:** Claude Code (investigation run on F5A4T8E)
**Status:** READ-ONLY PASS. Nothing in `_backport/`, `verify_generators.py` or any
delivered artefact was modified. This document is the only file written.

---

## 0. Executive summary

Four findings, in order of how much they should worry the reader:

1. **The regression gate is silently blind to the three artefacts everyone cares
   about.** `verify_generators.py` still looks for `BE-DD-001-v1.3.xlsx`,
   `BE-WTC-001-v1.0.xlsx` and `BE-CCG-001-v1.1.docx`. Stage 9.6 renamed those
   files to v1.4 / v1.1 / v1.2. The verifier reports `SKIP — generator or
   artefact missing`, which does **not** count as a failure. The same rename
   also broke two of the six back-port extractors, which read the old names.
2. **The 897 differing cells across the nine report specs are one single
   category** — the Stage 9.6 version-string propagation. Zero content changes.
   Verified by normalising `BE-XXX-001-v1.N` to a placeholder and re-diffing:
   897 of 897 diffs disappear.
3. **The Data Dictionary is the only genuinely large drift** — ~958 new option-mapper
   code rows across 13 of 93 mapper blocks. It is large but *mechanical*: the
   existing `OPTION_MAPPERS` data structure holds it without any structural change.
4. **WTC and CCG drift is tiny** — 14 cells and 6 paragraph hunks respectively.

No generator is broken. All thirteen still run to completion. This is a content
sync problem, not a code problem.

---

## 1. What `_backport/` actually is

### 1.1 It is not one folder — there are three, and the CCG has none

| Location | Files | Lines | On disk |
|---|---:|---:|---:|
| `02-wtc/_backport/` | 1 | 320 | 46 KB |
| `04-reports-spec/_backport/` | 36 | 52,834 | 4.5 MB |
| `05-data-dictionary/_backport/` | 3 | 7,186 | 512 KB |
| `01-ccg/_backport/` | — | — | **does not exist** |

**Every file in all three folders is dated 2026-08-25.** Nothing has been folded
back since. Stage 9.5 and 9.6 both landed on 16 September 2026 — three weeks later,
artefact-side only.

### 1.2 What is in them: data, not code

They are **pure Python data modules**. Each contains one or more module-level
lists of tuples and no logic — no functions, no classes, no I/O. The build scripts
`sys.path.insert` the folder and import the names. The builders keep their own
layout/formatting reasoning; only the *content* comes from `_backport/`.

### 1.3 What corresponds to each artefact type

**Data Dictionary → `05-data-dictionary/_backport/` (3 modules)**

| Module | Exports | Shape |
|---|---|---|
| `dd_fields.py` | `EMPLOYEE_ID_FIELDS`, `COUNTRY_FIELDS` | 9-tuples in the generator's blue-column order |
| `dd_option_mappers.py` | `OPTION_MAPPERS` | `[(mapper_name, [(code, abbr, local, english), …]), …]` |
| `dd_versioncontrol.py` | `VERSION_ROWS` | `(version, datetime, description, status, author)` |

Consumed by `05-data-dictionary/build_be_dd.py` (256 lines), lines 26–31.

**Report Specs → `04-reports-spec/_backport/` (36 modules = 9 specs × 4 kinds)**

Per spec `be_<authority>_<nnn>_<name>_*`:
`_fieldoptions.py` (Field Options sheet), `_versioncontrol.py` (Version Control
sheet), `_spec4.py` (sheet 4, the field-level spec — the big ones, up to 411 KB),
`_sheets.py` (the remaining five sheets). Consumed by
`04-reports-spec/build_01..09_*.py` via the shared `be_common` API
(`sheet_field_options`, `sheet_version_control`, `sheet_spec`, `sheet_report_matrix`).

**WTC → `02-wtc/_backport/wtc_corrections.py` (1 module) — the odd one out**

This one is *not* a content model. It is a **patch list of 23 assert-guarded cell
substitutions**: `(sheet, cell, expected_from_builder, delivered_value)`. The
builder writes its own v1.0 text, asserts that it still matches
`expected_from_builder`, then overwrites with `delivered_value`. If a fix is ever
made at source, the assert raises rather than silently reverting.

Current 23 entries: Version Control ×8, Global WTC Coverage ×6, Form Reference
Guide ×5, Wage Type Catalogue ×2, Tax Credit ×2.
Consumed by `02-wtc/build_be_wtc.py` lines 798–819.

**CCG → no `_backport/`. Its source of truth is `01-ccg/modules/*.md`**

13 markdown modules (`m01_foundational.md` … `m13_*.md`), 3,355 lines total,
assembled by `01-ccg/build_ccg_docx.py` (311 lines). The CCG never needed a
back-port layer because its content already lives outside the generator in
editable markdown. **No module has been edited since 24 August 2026** — confirmed
by mtime and by the rebuild, which reproduces the pre-Stage-9.5 text.

Note that the CCG generator also hard-codes version strings in three places
(`OUT`, `FOOTER`, `TITLE`, lines 21–24) — those are generator-source edits, not
data edits.

### 1.4 Is the relationship documented?

**Yes, and well.** `_pipeline/backport_extractors/README.md` (2.4 KB) states the
purpose, a script→reads→writes table, the working rule, and — usefully — a
"What these are not" section clarifying they are not a patch layer. Each data
module additionally carries a docstring naming the source file and extraction
date, and the instruction *"Generated data: re-extract rather than editing by hand."*

The README also records *why* this exists: every correction made between 14 and
25 August 2026 was applied by one-shot `_apply_*.py` scripts straight to the
binary artefact and never folded back, so a rebuild would have reverted **8,703
cells**. `_backport/` was the remedy for exactly the situation we are now in again.

The README states the working rule explicitly:

> 1. Edit the delivered artefact. 2. Run the matching extractor.
> 3. Run `verify_generators.py` — it must report 0 drift.
> Step 3 is the one that actually catches the mistake. Skipping it is how this
> whole class of bug got in.

Stages 9.5 and 9.6 performed step 1 and skipped steps 2 and 3.

### 1.5 The extractors

`_pipeline/backport_extractors/` — 6 scripts, 753 lines, plus the README. These
read a delivered artefact and regenerate the `_backport/` modules. **Two of the
six are broken by the Stage 9.6 rename:**

| Extractor | Reads | Status |
|---|---|---|
| `extract_spec_fieldoptions.py` | `04-reports-spec/*.xlsx` (glob) | OK — glob, names unchanged |
| `extract_spec_versioncontrol.py` | `04-reports-spec/*.xlsx` (glob) | OK |
| `extract_spec_sheet4.py` | `04-reports-spec/*.xlsx` (glob) | OK |
| `extract_spec_othersheets.py` | `04-reports-spec/*.xlsx` (glob) | OK |
| `extract_dd.py` | `BE-DD-001-v1.3.xlsx` (hard-coded, line 24) | **BROKEN** — file is now v1.4 |
| `extract_wtc_corrections.py` | `BE-WTC-001-v1.0.xlsx` (line 18) **and** `~/be-tf/scratch/WTC-regen.xlsx` (line 19) | **BROKEN ×2** — artefact is now v1.1, and the scratch regen does not exist (only `DD-regen.xlsx` and `CCG-regen.docx` are there) |

The `.bak-before-stage9x` files do **not** pollute the spec glob (they end
`.xlsx.bak-…`, so `*.xlsx` does not match them).

---

## 2. Verifier run — raw output

The tool exists and runs. Confirmed real path: **`_pipeline/verify_generators.py`**
(255 lines). Invoked as `python _pipeline/verify_generators.py`, Python 3.14.7,
openpyxl 3.1.5, python-docx present.

```
==============================================================================
GENERATOR REPRODUCIBILITY -- does each build script reproduce what shipped?
==============================================================================
DRIFT    BE-NSSO-001 Dimona                 103 value, 0 fill
DRIFT    BE-NSSO-002 DmfA                   235 value, 0 fill
DRIFT    BE-NSSO-003 DmfA Modification      128 value, 0 fill
DRIFT    BE-FIN-001 Finprof 274             12 value, 0 fill
DRIFT    BE-FIN-002 Belcotax 281.10         47 value, 0 fill
DRIFT    BE-NSSO-004 DRS                    170 value, 0 fill
DRIFT    BE-FEDRIS-001 Work Accident        134 value, 0 fill
DRIFT    BE-NSSO-005 Limosa                 56 value, 0 fill
DRIFT    BE-FEBELFIN-001 SEPA               12 value, 0 fill
SKIP     BE-DD-001 Data Dictionary          generator or artefact missing
SKIP     BE-WTC-001 Wage Type Catalogue     generator or artefact missing
SKIP     BE-CCG-001 Country Config Guide    generator or artefact missing
OK       BE-SIR-001 Statutory Integrations  0 value, 0 fill
------------------------------------------------------------------------------
DRIFT in 9 generator(s): BE-NSSO-001 Dimona, BE-NSSO-002 DmfA, BE-NSSO-003 DmfA
Modification, BE-FIN-001 Finprof 274, BE-FIN-002 Belcotax 281.10, BE-NSSO-004
DRS, BE-FEDRIS-001 Work Accident, BE-NSSO-005 Limosa, BE-FEBELFIN-001 SEPA
```

Exit code 1.

### 2.1 Read this output carefully — the three SKIPs are the story

The three artefacts this investigation was asked about are **exactly** the three
the verifier cannot see. `TARGETS` (lines 30–66) hard-codes:

```
"05-data-dictionary/BE-DD-001-v1.3.xlsx"   -> actual file is BE-DD-001-v1.4.xlsx
"02-wtc/BE-WTC-001-v1.0.xlsx"              -> actual file is BE-WTC-001-v1.1.xlsx
"01-ccg/BE-CCG-001-v1.1.docx"              -> actual file is BE-CCG-001-v1.2.docx
```

`main()` treats a missing artefact as `SKIP` and — critically — **does not append
it to `failures`**. So a SKIP never turns the exit code non-zero.

**Consequence:** once the nine spec drifts are fixed, this tool will print
*"All 13 generators reproduce their delivered artefact"* and exit 0 while having
actually checked only 10 of 13 — and having never once looked at the Data
Dictionary, the Wage Type Catalogue or the CCG. A green gate that has silently
stopped testing three artefacts is worse than a red one.

The per-target output-path regexes (`out_re`) also still match the old `v1.0`/`v1.1`
literals in the generator source. Those regexes happen to still be correct, because
the *generators* were never version-bumped — only the delivered files were. Any
fix must keep the two in step.

---

## 3. Drift characterisation

Method: each generator was copied to a temporary sibling with its `OUT` line
redirected into a scratch directory (the same technique `verify_generators.py`
itself uses), run, and the result diffed against the **current** delivered file.
Diffs were then classified by normalising every `BE-XXX-001-v1.N` token to a
placeholder and re-comparing — this separates "the version string changed" from
"the content changed". Delivered artefacts were opened read-only; the scratch
copies were deleted afterwards.

### 3.1 The nine Report Specs — ONE category, fully mechanical

| Spec | Total diffs | Version-string only | Content changed | New/removed |
|---|---:|---:|---:|---:|
| BE-NSSO-001 Dimona | 103 | 103 | 0 | 0 |
| BE-NSSO-002 DmfA | 235 | 235 | 0 | 0 |
| BE-NSSO-003 DmfA Modification | 128 | 128 | 0 | 0 |
| BE-FIN-001 Finprof 274 | 12 | 12 | 0 | 0 |
| BE-FIN-002 Belcotax 281.10 | 47 | 47 | 0 | 0 |
| BE-NSSO-004 DRS | 170 | 170 | 0 | 0 |
| BE-FEDRIS-001 Work Accident | 134 | 134 | 0 | 0 |
| BE-NSSO-005 Limosa | 56 | 56 | 0 | 0 |
| BE-FEBELFIN-001 SEPA | 12 | 12 | 0 | 0 |
| **Total** | **897** | **897** | **0** | **0** |

**Category SPEC-1 — Stage 9.6 version-string propagation (897 cells, 9 files).**
Every one is `BE-DD-001-v1.3 -> v1.4`, `BE-WTC-001-v1.0 -> v1.1`, or
`BE-CCG-001-v1.1 -> v1.2` inside a citation string. Examples:

```
Dimona Spec!r13c12   "BE-DD-001-v1.4 — 'NSSO Employer Registration Number'…"
                 vs  "BE-DD-001-v1.3 — 'NSSO Employer Registration Number'…"
Field Options!r62c5  'BE-WTC-001-v1.1 Wage Type Catalogue'
                 vs  'BE-WTC-001-v1.0 Wage Type Catalogue'
Field Options!r9c5   'BE-CCG-001-v1.2 Module 2.2 — this format IS sourced'
                 vs  'BE-CCG-001-v1.1 Module 2.2 — this format IS sourced'
```

- **Can `_backport/` represent it?** Yes, trivially — these are plain strings
  already sitting in `*_spec4.py` / `*_fieldoptions.py`. No structural change.
- **Sync or structural?** Pure mechanical sync. The four spec extractors all use
  a glob and are unbroken, so re-running them regenerates all 36 modules as-is.

### 3.2 BE-DD-001 Data Dictionary — the only large one

Positional cell diff: **7,538 differing cells** (delivered 11,837 populated cells,
rebuilt 7,957). **That number is misleading and should not be used for scoping.**
7,531 of the 7,538 fall in one sheet, *Country Option Mappers*, where the delivered
sheet has 2,023 rows against the rebuild's 1,043. Because ~980 rows were inserted,
every row below an insertion point compares as "different" purely from being
shifted down. Re-diffed as row *sequences* rather than by coordinate:

```
delivered rows=2023  rebuilt rows=1043  (delta +980)
  identical rows   961
  replace          864
  delete           198
```

And by mapper block — **only 13 of the 93 delivered blocks differ at all:**

| Option mapper | Delivered rows | Rebuilt rows | Delta |
|---|---:|---:|---:|
| NSSO Employer Category | 289 | 1 (`NOT FOUND`) | +288 |
| Joint Committee Number | 225 | 16 | +209 |
| NSSO Worker Code | 169 | 12 | +157 |
| Risk Identification (DRS Annexe 12) | 78 | 0 | +78 |
| DmfA Service Code | 52 | 0 | +52 |
| DmfA Remuneration Code | 44 | 0 | +44 |
| Work Reorganisation Measure | 58 | 15 | +43 |
| NSSO Worker Status | 45 | 14 | +31 |
| Work Schedule Days Indicator | 28 | 1 (`NOT FOUND`) | +27 |
| Employment Promotion Measure | 15 | 5 | +10 |
| Reference Type | 9 | 0 | +9 |
| NSSO Contribution Payment Purpose | 5 | 0 | +5 |
| Legal Basis for Part-Time Work With Benefit Re… | 10 | 5 | +5 |
| **Total code rows** | **1,816** | **858** | **+958** |

Categories:

**Category DD-1 — five whole new mapper blocks (~188 code rows).**
`DmfA Remuneration Code`, `DmfA Service Code`, `NSSO Contribution Payment Purpose`,
`Reference Type`, `Risk Identification (DRS Annexe 12)`. Present in delivered,
absent from `_backport` entirely (appended at delivered rows 1826–2023).
- *Representable?* **Yes.** `OPTION_MAPPERS` is a list of `(name, rows)` pairs;
  five more appended entries. No structural change.

**Category DD-2 — eight existing blocks expanded from stub to full code table
(~770 code rows).** The largest are the NSSO code tables that were `NOT FOUND`
or a short excerpt at the 25 August snapshot and were filled in afterwards
(NSSO Employer Category 1→289, Joint Committee Number 16→225, NSSO Worker Code
12→169).
- *Representable?* **Yes.** More 4-tuples inside existing blocks. No structural change.

**Category DD-3 — `NOT FOUND` → resolution text (a few dozen cells).**
Stage 9.5 resolutions, e.g. Country Option Mappers r54–r56: `NOT FOUND` → `n/a`,
with the description rewritten to *"RESOLVED — NOT A DmfA REPORTING FIELD,
16 September 2026. The NSSO contract-type zone is 00050…"*.
- *Representable?* **Yes.** Value edits inside existing tuples.

**Category DD-4 — one new Version Control changelog row (5 cells).**
Delivered row 14 = `('1.4', 2026-09-16, '…STAGE 9.5 GAP CLOSURE…', 'Released',
'Wallisson Gomes')`.
- *Representable?* **Yes.** `VERSION_ROWS` is exactly this 5-tuple shape.

**Category DD-5 — one wording change on ID Information (1 cell).**
`ID Information!r21c6`: *"…until the definitive number is allocated."* vs
*"…while the definitive number is still pending."*
- *Representable?* **Yes.** One string in `dd_fields.py`.

**Sheets with zero drift:** Country Fields, Introduction, Instructions,
Currency Codes, Country Codes. Sheet set and order are identical between
delivered and rebuilt.

**Verdict:** large in volume, but **every category fits the existing data model
without a structural change**. `extract_dd.py` is designed to regenerate all of
this in one shot — its only defect is the hard-coded `v1.3` filename.

### 3.3 BE-WTC-001 Wage Type Catalogue — 14 cells

| Sheet | Diffs | Breakdown |
|---|---:|---|
| Version Control | 8 | 5 new-row cells, 2 version-string, 1 content |
| Form Reference Guide | 3 | 1 version-string, 2 content |
| Wage Type Catalogue | 2 | 2 content |
| Tax Credit | 1 | 1 content |
| **Total** | **14** | 6 content, 5 new, 3 version-string |

**Category WTC-1 — new v1.1 changelog row (5 cells).** Version Control r14c2–c6:
`1.1` / `2026-09-16` / *"STAGE 9.5 GAP CLOSURE…"* / `Released` / `Wallisson Gomes`.
- *Representable?* **Yes.** The builder's application loop (`build_be_wtc.py`
  lines 806–818) has a `_blank()` helper that explicitly tolerates
  `expected_from_builder is None`, so a correction may write into a cell the
  builder left empty. Eight existing entries already use `None`. Adding a row is
  five new `CORRECTIONS` entries — no structural change.

**Category WTC-2 — Stage 9.5 work-bonus cap closure (4 content cells).**
`Tax Credit!B6`, `Wage Type Catalogue!F303`, `Version Control!C25`, plus the
loan-rate wording at `Wage Type Catalogue!F359`.
- *Representable?* **Yes.** Existing cell-substitution entries, value updated.

**Category WTC-3 — Stage 9.6 version-string + Form Reference Guide wording (5 cells).**
`Form Reference Guide!r2c4` (`BE-DD-001-v1.3` → `v1.4`), `r2c5`
(*"not pending"* → *"not outstanding"*).
- *Representable?* **Yes.** Existing entries.

**Verdict:** small, entirely mechanical. The blocker is not the model — it is that
`extract_wtc_corrections.py` needs both a filename fix *and* a freshly generated
`~/be-tf/scratch/WTC-regen.xlsx`, which is currently absent.

### 3.4 BE-CCG-001 Country Configuration Guide — 6 hunks

Delivered 2,314 body lines vs rebuilt 2,312. Six diff hunks, no others.

**Category CCG-1 — version strings hard-coded in the generator (2 hunks).**
Title line *"…BE-CCG-001 v1.2"* vs *"v1.1"*, and the cover block
*"Version 1.2 — 16 September 2026 (supersedes version 1.1 of 21 August 2026)"*
plus its Stage 9.5/9.6 revision paragraph vs a bare *"Version 1.1 — 21 August 2026"*.
- *Representable?* **Partly — and this is the one place a source change is needed.**
  `OUT`, `FOOTER` and `TITLE` are string literals at `build_ccg_docx.py` lines
  21–24, not data. The cover-block prose lives in `modules/m01_foundational.md`.
  So this category splits across generator source *and* markdown.

**Category CCG-2 — Stage 9.5 substantive gap closures (4 hunks).**

1. *Work-bonus annual cap* (delivered line 734): `NOT FOUND — the cap applicable
   after the 1 July 2026 indexation…` → `EUR 3,594.36 from 1 July 2026. CLOSED
   16 September 2026… edition 2026/3 states "het totaal van de vermindering per
   werknemer niet meer bedragen dan 3.594,36 EUR per kalenderjaar"`.
2. *Overtime-ceiling citation* (line 516): `…pending confirmation that no distinct
   Programme Law also touches this ceiling.` → `…CONFIRMED 16 September 2026: no
   distinct Programme Law touches this ceiling. The 180-hour quota is made
   permanent…`.
3. *Article 11bis written part-time contract* — a whole new table row
   (delivered line 1998), absent from the rebuild entirely.
4. *Legal-basis line* (line 2079) — Article 11bis inserted into the citation list.

- *Representable?* **Yes, trivially.** These are markdown paragraphs and table
  rows in `01-ccg/modules/*.md`. No data model to extend — it is prose.

**Confirmed:** no file in `01-ccg/modules/` has been modified since 24 August 2026.
All four Stage 9.5 edits went into the `.docx` only.

---

## 4. Scale estimate (rough — relative, not absolute)

Explicitly labelled as rough. No time estimate is given; this investigation cannot
responsibly produce one.

| Artefact | Scale | Reasoning |
|---|---|---|
| **9 Report Specs** | **Small sync — the most mechanical of the four** | 897 cells, one category, zero content change. The four spec extractors are unbroken (glob-based). Re-running them regenerates all 36 modules. Nothing to decide. |
| **BE-WTC-001** | **Small sync** | 14 cells, 3 categories. The `CORRECTIONS` model already supports every one, including the new changelog row via the `None`/`_blank` path. Blocker is mechanical, not structural: `extract_wtc_corrections.py` needs the v1.1 filename *and* a regenerated `WTC-regen.xlsx` (currently missing from `~/be-tf/scratch/`). |
| **BE-DD-001** | **Moderate — large volume, no structural change** | ~958 new code rows + 5 new blocks + 1 changelog row + 1 wording fix. Every category fits `OPTION_MAPPERS` / `VERSION_ROWS` / `dd_fields` as-is. This is the biggest *number* by far and the smallest *risk* per unit — it is bulk data, and `extract_dd.py` regenerates the lot once its hard-coded `v1.3` filename is corrected. Do not scope this from the 7,538 figure; the real shape is 13 blocks in one sheet. |
| **BE-CCG-001** | **Small — but the only one touching generator source** | 6 hunks. Four are markdown prose edits into `modules/*.md`. Two require editing string literals in `build_ccg_docx.py` itself (`OUT`, `FOOTER`, `TITLE`). There is no extractor for the CCG and no `_backport/` — the sync is a manual markdown edit, which means it is the one artefact where the sync cannot be automated by re-running a tool. |

**Not covered by any of the above — the gate itself.** `verify_generators.py`
needs its three stale `TARGETS` paths corrected, and its SKIP-handling
reconsidered, before any of the four syncs can be *verified*. Doing the syncs
without that leaves the same blind spot in place. This is the smallest change on
the list and the one with the highest leverage.

**Cross-cutting risk worth naming:** the version-string category is circular. The
specs cite `BE-DD-001-v1.4`; the DD's own Form Reference Guide cross-reference and
the WTC cite each other. Whatever order a fix takes, the version strings must be
settled *before* the spec extractors are re-run, or the specs will be re-extracted
carrying values that the next bump invalidates again.

---

## 5. What was NOT done in this pass

Per the scope fence: no fix of any kind was applied.

- `_backport/` — untouched (verified: all files still dated 2026-08-25).
- `_pipeline/verify_generators.py` — untouched, including its three stale paths.
- `_pipeline/backport_extractors/` — untouched, including the two broken extractors.
- The four delivered artefacts and the nine specs — opened read-only only.
- `mercans_pipeline_v2_9.sh`, `shared/country_failure_log.md` — not opened.
- Scratch build products were written to a temporary directory and removed.

Noted-in-passing items deliberately left unfixed, as instructed:

1. `verify_generators.py` `TARGETS` — three stale artefact filenames.
2. `verify_generators.py` `main()` — SKIP does not append to `failures`, so a
   missing artefact cannot fail the gate.
3. `extract_dd.py` line 24 — hard-coded `BE-DD-001-v1.3.xlsx`.
4. `extract_wtc_corrections.py` lines 18–19 — hard-coded `BE-WTC-001-v1.0.xlsx`
   and a `~/be-tf/scratch/WTC-regen.xlsx` that does not exist.
5. `build_ccg_docx.py` lines 21–24 — version strings hard-coded in three literals
   and the module docstring.
6. The `TOLERANCES` entry for BE-DD-001 (70 fill diffs on 14 separator rows) was
   written against v1.3 and has not been re-validated against v1.4.

---

## 6. Open questions for the owner

These need a judgment call only Wallisson can make. They are stated, not answered.

1. **Is `_backport/` still meant to be the source of truth, or has
   direct-artefact-editing become the accepted practice?** Stages 9.5 and 9.6
   both edited the delivered files directly and skipped the extractor step the
   README mandates. That is either a process lapse to correct, or a de facto
   decision that `_backport/` should be retired rather than maintained. The two
   answers lead to completely different fixes — one restores the loop, the other
   deletes 5 MB of data modules and the gate with them. **This is the question
   that gates every other decision below.**

2. **If `_backport/` stays: should the Stage 9.5/9.6 edits be re-extracted from
   the delivered artefacts, or re-applied at source and the artefacts rebuilt?**
   Re-extraction is fast and keeps the current files authoritative. Rebuilding is
   slower but proves the generators genuinely reproduce the artefact. The README's
   design assumes the first; the existence of the gate implies a preference for
   the second.

3. **Should the CCG get a `_backport/`-equivalent, or is `modules/*.md` considered
   sufficient?** The CCG is the one artefact whose sync cannot be automated today,
   because there is no `extract_ccg.py`. It is also the artefact most likely to be
   edited as prose. Should an extractor be written, or is the markdown expected to
   be edited by hand as the primary source with the `.docx` always regenerated?

4. **Should version numbers be centralised?** The `v1.N` strings currently live in
   at least four places: generator literals, `_backport` data, the artefact
   filenames, and cross-citations inside other artefacts. Stage 9.6 had to touch
   897 spec cells for one bump. Is a single version constant worth introducing, or
   is the propagation acceptable as-is?

5. **Should a missing artefact fail the gate?** Changing `SKIP` to count as a
   failure would have caught the 9.6 rename immediately. It would also make the
   gate fail loudly for any artefact legitimately not yet built. Which behaviour
   is wanted?

6. **Is `~/be-tf/scratch/` a durable working location?** `extract_wtc_corrections.py`
   depends on a file there. It currently holds `DD-regen.xlsx` and `CCG-regen.docx`
   but no `WTC-regen.xlsx`. If that directory is transient, the WTC extractor needs
   a different contract.

---

*End of diagnosis. No fix plan is proposed here — that is the next stage.*

---

## Addendum — 2026-09-16, Stage 9.8: the verifier itself was fixed

Stage 9.8 edited exactly one file, `_pipeline/verify_generators.py`. No artefact,
no extractor, no `_backport/` content was touched. Two bugs were closed.

**Bug 1 — stale expected filenames in `TARGETS`.** Three of the thirteen entries
still named the pre-9.6 artefacts, so those three could never be located and were
reported `SKIP`:

| entry | was | now |
|---|---|---|
| BE-DD-001 Data Dictionary | `BE-DD-001-v1.3.xlsx` | `BE-DD-001-v1.4.xlsx` |
| BE-WTC-001 Wage Type Catalogue | `BE-WTC-001-v1.0.xlsx` | `BE-WTC-001-v1.1.xlsx` |
| BE-CCG-001 Country Config Guide | `BE-CCG-001-v1.1.docx` | `BE-CCG-001-v1.2.docx` |

Only the delivered-artefact string changed in each. The `out_re` redirect patterns
were left alone and still match: the generators' own `OUT =` literals were never
bumped by 9.6, so they continue to read `v1.0` / `v1.0` / `v1.1` in source. The nine
report-spec entries were not touched.

**Bug 2 — `SKIP` silently counted as success.** `SKIP` and `ERROR` rows were not
added to the list that drove the exit code, so a run in which an artefact could not
be found or a generator crashed could still print a clean "All 13 generators
reproduce their delivered artefact" and exit 0. The summary is now computed from the
recorded verdicts: `OK` counts as reproduced, `DRIFT` as drifted, and `SKIP`/`ERROR`
together as *could not be checked* — the last of which now fails the gate exactly as
drift does. The single "All N reproduce" line is gone; the three verdicts are always
reported separately, and the drifted and unchecked labels are named. Question 5 in
the open-questions list above is thereby answered in practice: a missing artefact
fails the gate.

**Real output after the fix** (`python3 _pipeline/verify_generators.py`, exit code 1):

```
==============================================================================
GENERATOR REPRODUCIBILITY -- does each build script reproduce what shipped?
==============================================================================
DRIFT    BE-NSSO-001 Dimona                 103 value, 0 fill
DRIFT    BE-NSSO-002 DmfA                   235 value, 0 fill
DRIFT    BE-NSSO-003 DmfA Modification      128 value, 0 fill
DRIFT    BE-FIN-001 Finprof 274             12 value, 0 fill
DRIFT    BE-FIN-002 Belcotax 281.10         47 value, 0 fill
DRIFT    BE-NSSO-004 DRS                    170 value, 0 fill
DRIFT    BE-FEDRIS-001 Work Accident        134 value, 0 fill
DRIFT    BE-NSSO-005 Limosa                 56 value, 0 fill
DRIFT    BE-FEBELFIN-001 SEPA               12 value, 0 fill
DRIFT    BE-DD-001 Data Dictionary          7538 value, 5365 fill
DRIFT    BE-WTC-001 Wage Type Catalogue     14 value, 0 fill
DRIFT    BE-CCG-001 Country Config Guide    2310 value, 0 fill
OK       BE-SIR-001 Statutory Integrations  0 value, 0 fill
------------------------------------------------------------------------------
1 of 13 reproduced, 12 drifted, 0 could not be checked.
  drifted             : BE-NSSO-001 Dimona, BE-NSSO-002 DmfA, BE-NSSO-003 DmfA Modification, BE-FIN-001 Finprof 274, BE-FIN-002 Belcotax 281.10, BE-NSSO-004 DRS, BE-FEDRIS-001 Work Accident, BE-NSSO-005 Limosa, BE-FEBELFIN-001 SEPA, BE-DD-001 Data Dictionary, BE-WTC-001 Wage Type Catalogue, BE-CCG-001 Country Config Guide
```

All thirteen generator/artefact pairs are now actually reached — zero `SKIP`. The
DD, WTC and CCG drift is the expected consequence of their not having been synced
to `_backport/` since 25 August, as diagnosed above; the tool is now reporting it
rather than hiding it behind a `SKIP`.

Worth recording because it was not anticipated when this stage was scoped: the nine
report-spec builders also drift, and did so before this fix as well (their entries
were untouched and their comparison path is unchanged — the pre-9.8 gate would have
listed them under its `DRIFT in N generator(s)` line). The Stage 9.7 finding that
the nine spec entries were "correct" referred to their filename entries surviving
the rename, not to the builders reproducing their artefacts. The drift counts are
consistent with the 9.6 version-string propagation across 897 spec cells never
having been folded back into the builders.

Only BE-SIR-001 reproduces exactly. Syncing any of the twelve remains out of scope
here and still depends on open question 1 — whether `_backport/` stays the source
of truth.

---

## Stage 9.9 — 2026-09-16 — back-port extractor repairs (Step A of the sync plan)

Scope was the two extractors the 9.7 diagnosis flagged at items 3 and 4 of its
blocker list. One is fixed and unblocked; the other is half fixed and the
remaining half is **stopped and escalated**, not worked around.

### `extract_dd.py` — FIXED

Three stale `BE-DD-001-v1.3` literals, not the one at line 24 that 9.7 recorded:

| Line | Before | After |
|---|---|---|
| 3 | `the delivered BE-DD-001-v1.3 content` (module docstring) | `…v1.4 content` |
| 24 | `SRC = os.path.join(DD_DIR, 'BE-DD-001-v1.3.xlsx')` | `…v1.4.xlsx` |
| 54 | `Extracted verbatim from BE-DD-001-v1.3.xlsx …` (`HEAD` template, written into every generated `_backport/dd_*.py`) | `…v1.4.xlsx …` |

Line 10 (`the v1.3 promotion and the note rewrites`) was deliberately **left
alone**. It is a historical statement about what happened between v1.0 and v1.3,
not a reference to the source file; rewriting it to "v1.4" would assert a change
history that is not what that sentence describes.

Dry-checked without executing the extraction: the module-level path literals were
resolved by AST-folding `DD_DIR` / `OUT` / `SRC`, and all three resolve to paths
that exist. A separate read-only probe confirms the extractor can now start —
`BE-DD-001-v1.4.xlsx` loads, all four sheets it reads (`Country Option Mappers`,
`ID Information`, `Country Fields`, `Version Control`) are present, the three
sibling data modules it imports for the employee/legal-entity split
(`be_dd_data_id`, `be_dd_data_emp`, `be_dd_data_emp2`) exist, and the `_backport`
output directory exists. Nothing blocks Step B for the DD.

### `extract_wtc_corrections.py` — problem 1 FIXED, problem 2 STOPPED

**Problem 1 (mechanical), fixed.** Three stale `BE-WTC-001-v1.0.xlsx` literals →
`v1.1`: line 18 (the `LIVE` workbook it actually opens), and lines 58 and 72 in the
`HEAD` template written into the generated `wtc_corrections.py`. Lines 4 and 57
("still emits the **v1.0 text**") were left alone — they describe the *builder's*
output vintage, not a filename.

**Problem 2, left open. The 9.7 premise was wrong, and the true situation is worse.**

1. `~/be-tf/scratch/WTC-regen.xlsx` **exists** — 425,108 bytes, 2026-08-25 09:25.
   The 9.7 note that "only `DD-regen.xlsx` and `CCG-regen.docx` are there" was
   incomplete; `WTC-regen.xlsx` and `SIR-regen.docx` are present too. `os.path.
   expanduser` resolves the literal in line 19 to that file under this `HOME`.
   So there is nothing to create, and the extractor now opens all its inputs.

2. **But the file is the wrong kind of file.** The extractor's model is
   `(sheet, cell, expected_from_builder, delivered_value)`, where
   `expected_from_builder` comes from `GEN` — so `GEN` must be the **un**corrected
   builder output. Tested against the live `02-wtc/_backport/wtc_corrections.py`
   (23 entries): the existing `WTC-regen.xlsx` holds the **delivered** value at
   **23 of 23** correction cells and the pre-correction builder value at **0 of 23**.
   It is a *post*-correction regen — the verification copy made to prove the
   back-port reproduced the delivered workbook — not the baseline the extractor needs.

3. **Why the "just re-run the builder" answer does not work.** `build_be_wtc.py`
   ends (lines 798–819) by importing `CORRECTIONS` from `_backport/` and applying
   all 23 assert-guarded substitutions *before* `wb.save(OUT)`. Its output is
   corrected by construction. `build_be_wtc.py` is also the **only** one of the
   thirteen builders with such a post-hoc correction layer — `build_be_dd.py`
   (lines 24–31) imports its `_backport/dd_*.py` as ordinary *source data* with no
   asserts and no substitution pass. That is why the scratch `DD-regen.xlsx` /
   `CCG-regen.docx` / `SIR-regen.docx` genuinely *are* plain builder-output copies,
   and why that pattern **does not transfer** to the WTC: the WTC regen cannot be a
   plain builder-output copy and still serve as `GEN`. (Those three scratch files
   are in any case not extractor inputs — `extract_dd.py` reads the delivered
   workbook alone, and `verify_generators.py` writes its own regens to a temp dir,
   so `~/be-tf/scratch/` is an Aug-25 session leftover, not a live pipeline path.)

4. **Running the extractor as it now stands would be actively destructive.** With
   `LIVE` = v1.1 and `GEN` = the corrected Aug-25 regen, the 23 already-corrected
   cells are equal on both sides and drop out of the diff; only the ~14 new v1.1
   deltas survive. `wtc_corrections.py` would shrink 23 → ~14, and because the
   builder no longer carries those 23, the next `build_be_wtc.py` run would
   **silently revert** them — the exact failure class this whole back-port layer
   was built to prevent. Do not run this extractor in Step B until the question
   below is answered.

### Open question for Step B — WTC only, decision needed from the artefact owner

Producing a correct `GEN` requires suppressing `build_be_wtc.py`'s `CORRECTIONS`
layer for the duration of one build. That is a judgment call about **which
corrections form the baseline and which are deltas**, so it was left open per the
stage's stop condition rather than guessed. Two defensible readings, and they
produce different `wtc_corrections.py` files:

- **(a) Cumulative.** Regenerate `GEN` from `build_be_wtc.py` with `CORRECTIONS`
  bypassed, so the diff yields all 23 original corrections **plus** the ~14 v1.1
  deltas in one list of ~37. Keeps the extractor's "re-extract, never hand-edit"
  contract intact. Requires a one-build bypass of the correction block — e.g.
  pre-seeding a stub `wtc_corrections` module into `sys.modules` so the builder's
  `from wtc_corrections import CORRECTIONS` picks up an empty list — which touches
  `build_be_wtc.py`'s runtime and was outside the 9.9 scope fence.
- **(b) Incremental.** Keep the existing 23 and append only the ~14 v1.1 deltas,
  which makes `wtc_corrections.py` a partly hand-maintained file and breaks the
  "generated data: re-extract rather than editing by hand" contract the other
  five extractors hold to.

Related trap for whoever executes this: `build_be_wtc.py` line 34 still has
`OUT` hardcoded to `BE-WTC-001-v1.0.xlsx`, so an unredirected build would write a
stale-named workbook into `02-wtc/`. `verify_generators.py` already rewrites that
line by regex for its own runs (`TARGETS`, WTC entry); any manual regen must do the
same and write to scratch, not to the delivery folder.

This is a decision about the intended shape of the back-port layer, not a research
question that could be resolved from the sources — it needs the artefact owner.
`extract_dd.py` is unblocked and Step B can proceed for the DD independently.
