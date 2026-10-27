# BELGIUM — STAGE 12B: FIX F38 (ORPHANED TABLE OBJECTS) ON BE-DD-001, THEN APPLY D15

Run this locally on F5A4T8E, via Claude Code. Do this in order — the D15
edit from Stage 12 should not be applied on top of a structurally broken
file.

## STEP 0 — CONFIRM EXCEL IS CLOSED AND NOTHING WAS SAVED

```bash
tasklist | grep -i excel
```
If Excel still appears, STOP and report — do not proceed.

If it's gone, confirm the on-disk file still matches what git already has
(i.e. nothing was saved from the repaired-in-memory session):
```bash
git status -- 05-data-dictionary/BE-DD-001-v1.4.xlsx
git diff --stat -- 05-data-dictionary/BE-DD-001-v1.4.xlsx
```
Both should show no changes. If the file shows as modified here, someone
saved the Excel repair — stop, do not apply D15 or the table fix yet, and
report exactly what changed instead, since the fix approach would need to
account for whatever Excel's repair actually altered.

## STEP 1 — CONFIRM THE F38 PATTERN ON THIS SPECIFIC FILE

Don't assume the "[Reparado]" title means the exact F38 mechanism — verify:
```bash
python3 -c "
import zipfile
z = zipfile.ZipFile('05-data-dictionary/BE-DD-001-v1.4.xlsx')
tables = [n for n in z.namelist() if n.startswith('xl/tables/table')]
print('Table parts found:', tables)
for t in tables:
    print('---', t)
    print(z.read(t).decode('utf-8', errors='replace')[:400])
"
```
For each table part found, report its declared range (the `ref=` attribute)
and, by reading the actual current sheet, whether that range still
corresponds to anything meaningful in today's (much larger, post-Stage-9.5)
DD content — or whether it's a stale leftover from the original CZ
template, per F38's documented root cause. State plainly whether this
confirms F38 or is something different.

## STEP 2 — APPLY THE F38 FIX, EXACTLY AS ALREADY DOCUMENTED

This procedure is already written and proven — it's in
`shared/country_failure_log.md` under F38. Use it as-is:

```python
import zipfile, re, shutil
from pathlib import Path
src = Path('05-data-dictionary/BE-DD-001-v1.4.xlsx')
tmp = src.with_suffix('.tmp.xlsx')
with zipfile.ZipFile(src) as zin, zipfile.ZipFile(tmp, 'w', zipfile.ZIP_DEFLATED) as zout:
    for item in zin.infolist():
        n = item.filename
        d = zin.read(n)
        if re.match(r'xl/tables/table\d+\.xml$', n):
            continue  # drop the table part
        if re.match(r'xl/worksheets/sheet\d+\.xml$', n):
            d = re.sub(rb'<tableParts.*?</tableParts>|<tableParts[^>]*/>', b'', d, flags=re.S)
        if re.match(r'xl/worksheets/_rels/sheet\d+\.xml\.rels$', n):
            d = re.sub(rb'<Relationship[^>]*tables/table\d+\.xml[^>]*/>', b'', d)
        if n == '[Content_Types].xml':
            d = re.sub(rb'<Override[^>]*/xl/tables/table\d+\.xml[^>]*/>', b'', d)
        zout.writestr(item, d)
tmp.replace(src)
```

Before running for real: back up first (`.bak-before-f38fix`), run on the
backup copy, and validate — same standard as every prior stage:
- Part count and order otherwise identical
- All drawing/media/comment/VML parts byte-identical (MD5 match)
- XML well-formedness passes on every remaining part
- Zero cell VALUES changed — this fix touches only table metadata, not
  cell content

Only apply to the real file once the validation copy passes clean.

## STEP 3 — RE-VERIFY AND APPLY THE D15 EDIT

Step 2 touches `xl/worksheets/sheet1.xml` (stripping `<tableParts>`), so
before reusing `_work_stage12/apply_dd_d15.py` as-is, re-confirm its `OLD`
pattern (`<c r="D15" s="21" t="n"></c>`) still matches exactly once in the
post-Step-2 file — table-part removal shouldn't touch cell content, but
confirm rather than assume. Then apply it, same validation standard as
Step 2.

## STEP 4 — THE VISUAL CHECK ONLY A HUMAN CAN DO

Per F38's own conclusion: no script check can confirm this is fully fixed,
because the file is valid until Excel opens it. State this plainly in
your report rather than declaring victory on mechanical checks alone.
**Wallisson still needs to open the file in Excel afterward and confirm
the title bar shows no `[Repaired]`/`[Reparado]` marker before this is
considered closed.**

## STEP 5 — QUICK CHECK, NOT A FIX: DOES WTC HAVE THE SAME ISSUE?

F38's original finding named both France and Belgium **Data Dictionaries**
specifically — it did not test the WTC. Run the same Step 1 probe against
`02-wtc/BE-WTC-001-v1.1.xlsx`. If it also carries orphaned table parts,
do NOT fix it in this pass — just report the finding plainly as a separate,
later decision. If it's clean, say so and close the question.

## STEP 6 — VERIFY AND COMMIT

```bash
git diff --stat
```
Confirm the diff touches only `05-data-dictionary/BE-DD-001-v1.4.xlsx`
(both the table-part removal and D15), nothing else. Do not commit
automatically — leave it staged for Wallisson to review and commit
himself, same as Stage 12.

## OUTPUT

Report back: Step 0's confirmation, Step 1's findings (table ranges vs.
actual content, confirming or refuting F38), Step 2 and 3's validation
results, the explicit reminder from Step 4, and Step 5's WTC finding.

---

# STAGE 12B — EXECUTION RECORD (16 Sep 2026, F5A4T8E)

## Step 0 — Excel closed, nothing saved — CONFIRMED

- `tasklist | grep -i excel` -> no match. Excel is not running.
- `git status -- 05-data-dictionary/BE-DD-001-v1.4.xlsx` -> empty (clean).
- `git diff --stat -- 05-data-dictionary/BE-DD-001-v1.4.xlsx` -> empty.

The on-disk file still matched git exactly (md5 `f9faace0d0e354c620563df68e0d3a0d`,
766,439 bytes, mtime 13:57 — the Stage 9.6 write). Excel's in-memory repair was
never saved. Safe to proceed.

## Step 1 — F38 CONFIRMED, verbatim

13 table parts present: `xl/tables/table1.xml` ... `table13.xml`.
F38's own text names three signatures on the France DD; all three are present
here byte-for-byte:

| F38 says | BE-DD-001-v1.4 | Match |
|---|---|---|
| `Table_2` at `A13:V17` | `Table_2` `ref="A13:V17"` | exact |
| `Table_3` at `B42:X292` | `Table_3` `ref="B42:X292"` | exact |
| `Table_7` with `headerRowCount="0"` | `Table_7` `headerRowCount="0" totalsRowCount="1"` | exact |

**Ranges vs. actual content.** Sheet-to-table mapping and what each declared range
actually sits on today:

| Table | Sheet | ref | Declared header row holds | Verdict |
|---|---|---|---|---|
| Table_1 | Instructions | B4:C18 | `Field Name` / `Instructions/Descriptions` | **correct** (untouched reference tab) |
| Table_2 | ID Information | A13:V17 | *data*: `Belgium` / `Health Insurance Fund Name` | **stale** — data runs to row 33, table stops at 17 |
| Table_3 | Country Fields | B42:X292 | *data*: `Belgium` / `Usual Profession Seniority Code` | **stale** — real data ends at row 254; ref runs 38 rows into blank space |
| Table_4 | Option Mappers | B4:F9 | correct header | **stale** — cuts the Binary Indicator block mid-way (row 10 is still its data) |
| Table_5 | Option Mappers | B11:F16 | **entirely empty** | **broken** — a table whose header row has no values; the real header is row 16 |
| Table_6 | Option Mappers | B36:F40 | *data*: `STU` / `Student` | **stale** |
| Table_7 | Option Mappers | B43:F49 | `headerRowCount="0"`, `totalsRowLabel="RBP Miners' Brotherhood Health Insurance Fund"` | **CZ residue** — RBP = *Revirni bratrska pokladna*, a Czech health insurance fund, still written into BE table metadata |
| Table_8 | Option Mappers | B52:F1469 | *data*: `Contract Duration Type` block row | **stale** — spans 1,417 rows across unrelated blocks |
| Table_9 | Option Mappers | B1471:F1477 | *data* | **stale** — last rows empty; real header is at row 1478 |
| Table_10 | Option Mappers | B1479:F1484 | *data* | **stale** |
| Table_11 | Option Mappers | B1486:F1491 | **entirely empty** | **broken** — whole declared range is blank |
| Table_12 | Currency Codes ISO 4217 | B4:F272 | correct header, ends exactly at last row | **correct** (untouched reference tab) |
| Table_13 | Country Codes ISO 3166-1 | B4:C253 | correct header, ends exactly at last row | **correct** (untouched reference tab) |

Ten of thirteen are stale. The three that are still correct (1, 12, 13) are exactly
the three sheets the BE build never repopulated — which is the tell: the refs did not
drift randomly, they froze at CZ geometry and only the repopulated sheets moved out
from under them. Option Mappers now runs to row 2,023, some 530 rows past the last
table's end. `Table_7`'s Czech health-fund label is the CZ template signature in
plain text.

**This confirms F38.** It is not a different mechanism and not merely a cosmetic
`[Reparado]` title.

## Step 2 — F38 fix applied, validated

Backup: `05-data-dictionary/BE-DD-001-v1.4.xlsx.bak-before-f38fix`.
Script run verbatim as documented in `shared/country_failure_log.md` F38
(`_work_stage12b/f38_fix.py`), first on `_work_stage12b/candidate.xlsx`.

Validation of the candidate against the backup:

- **Part count / order** — 49 -> 36. Removed set is *exactly* the 13 table parts,
  nothing added, surviving part order unchanged.
- **Parts changed** — only `sheet3`-`sheet8.xml`, their six `.rels`, and
  `[Content_Types].xml`. `sheet1.xml` and `sheet2.xml` untouched (no tables there).
- **Drawings / media / comments / VML** — all 12 such parts MD5-identical
  (`drawing1-2.xml`, `comment1-3.xml`, `commentsDrawing1-3.vml`, `image1.png`,
  `image2.gif`).
- **XML well-formedness** — 31 XML/rels parts parse clean, 0 malformed.
  Zero residual `tableParts` elements and zero residual `tables/tableN.xml`
  references anywhere in the archive.
- **Cell values** — 218,304 cells before, 218,304 after, **0 differing** on value,
  style index, type or formula.
- **openpyxl round-trip** — loads clean; 8 sheets in order; merges, column widths,
  row dimensions, freeze panes, autofilters, data validations all preserved; the
  11 cell comments and 2 images still present.

Only then applied to the real file. Real file is byte-identical to the validated
candidate (md5 `004dad25df0e8190c55d93de63b5d7f6`).

**Cosmetic consequence, stated plainly.** Tables 1, 12 and 13 were *not* stale, but
the documented procedure removes all thirteen and that is what was run. Those three
tabs (Instructions, Currency Codes, Country Codes) drew their header shading and row
banding from the table style alone — their cells carry no cell-level fill — so they
will now render as plain unbanded text. This matches the already-delivered France DD,
which carries zero table parts, so the appearance is the accepted precedent, not a
regression introduced here. The repopulated sheets (ID Information, Country Fields)
are unaffected: their headers and banding are cell-level (`FF4472C4` header fill,
`FFD9E1F2` stripe) and survive untouched.

## Step 3 — D15 re-verified, then applied

- Step 2 touched `sheet3`-`sheet8`; the D15 target is `sheet1.xml`
  (`Version Control`), which had no tables and came through **byte-identical**
  (md5 `56830db25a786a62cb34153f9fba10d4` before and after).
- `OLD` pattern `<c r="D15" s="21" t="n"></c>` re-confirmed present **exactly once**
  in the post-Step-2 file. Not assumed — counted.
- `_work_stage12/apply_dd_d15.py` run on a copy first, then validated against the
  post-Step-2 file: 36 parts in, 36 out, order preserved; only `sheet1.xml` changed;
  all drawing/media/comment/VML parts MD5-identical; all 31 XML parts well-formed;
  **exactly 1 cell differs** — D15, style `s="21"` preserved, `t="n"` -> `t="inlineStr"`,
  carrying the BE-TF-008 text. Then applied to the real file.

Combined delta, pre-Stage-12b backup -> final file: **13 table parts removed, 1 cell
populated, 0 other cell changes, 0 binary assets altered.**

(Note: `cmp` between the real file and the candidate reports a byte difference at
offset 11 — that is zip local-header timestamps only. `apply_dd_d15.py` repacks with
`writestr(name, ...)`, which stamps the current clock. Part-by-part content
comparison: identical, no part differs.)

## Step 4 — VISUAL CHECK STILL OUTSTANDING — NOT CLOSED

Per F38's own conclusion: **no script check can confirm this is fixed.** The file was
valid by every mechanical measure *before* this fix too — that is precisely why the
defect reached the owner. Everything above proves the table metadata is gone and no
content moved; it does not prove Excel is satisfied.

**Wallisson must open `05-data-dictionary/BE-DD-001-v1.4.xlsx` in Excel and confirm
the title bar shows no `[Repaired]` / `[Reparado]` marker.** Until that happens this
item stays open. Also worth a glance while it is open: the `Coluna1` / `Coluna2`
artefacts in the ID Information orange columns should be gone, and the three
reference tabs will look flatter (see Step 2's cosmetic note) — that is expected.

## Step 5 — WTC: CLEAN, no action

`02-wtc/BE-WTC-001-v1.1.xlsx`: **zero table parts, zero `tableParts` elements** in
any sheet. F38 does not apply to the WTC. Question closed — nothing to decide later.

Extra read-only sweep over all 31 tracked `.xlsx` in BE-compliance (no fixes applied):
all 9 Report Specs, the Payslip generator and every QA scratch workbook are clean.
Two files still carry the 13 CZ table parts, both non-deliverable:

- `05-data-dictionary/Archived/BE-DD-001-v1.1.xlsx` — archived superseded version
- `_qa/scope/_ddbak.xlsx` — QA scratch backup

Neither ships. Flagged only; deliberately not touched in this pass.

## Step 6 — Staged, not committed

`git add` on `05-data-dictionary/BE-DD-001-v1.4.xlsx` only.
Staged diff: `Bin 766439 -> 759914 bytes`, 1 file.

Three other files show as modified in the working tree —
`BE_stage9-5_verification.md`, `mercans_pipeline_v2_9.sh`,
`shared/country_failure_log.md`. All three were **already modified before this
session began** (present in the opening `git status`); Stage 12b did not touch them.
They are left unstaged. Left for Wallisson to review and commit.
