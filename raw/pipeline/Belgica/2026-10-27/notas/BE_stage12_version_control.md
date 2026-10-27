# BELGIUM — STAGE 12: NORMALIZE VERSION CONTROL ACROSS ALL ARTIFACTS

Run this locally on F5A4T8E, via Claude Code. Every artifact's own "1.0"
row (Initial Version) stays untouched. Every later version row gets a
short, factual, one-line description of what actually changed at that
version — filled in where missing/vague, never invented where the real
cause isn't known.

## SCOPE FENCE

You may read and edit the Version Control sheet/section of: `BE-DD-001-
v1.4.xlsx`, `BE-WTC-001-v1.1.xlsx`, `BE-CCG-001-v1.2.docx` (if it has one
— see Step 1), the 9 files in `04-reports-spec/`, `BE-SIR-001-v1.0.docx`,
and the payslip generator workbook. Touch ONLY the Version Control
sheet/section of each file — not any other content in it. Do not touch
`mercans_pipeline_v2_9.sh`, `shared/country_failure_log.md`, `_backport/`,
or `08-skill/` in this stage.

## STEP 0 — BASELINE COMMIT

```bash
cd ~/mercans-pipeline/BE-compliance
git add BE-DD-001-v1.4.xlsx BE-WTC-001-v1.1.xlsx BE-CCG-001-v1.2.docx \
        04-reports-spec/ 03-statutory-integrations/BE-SIR-001-v1.0.docx \
        06-payslip/
git commit -m "Pre-normalization baseline, Stage 12 Version Control pass"
```
(Add only paths that exist and are tracked, by name — no `-A`.)

## STEP 1 — READ EVERY ARTIFACT'S ACTUAL CURRENT VERSION CONTROL STATE FIRST

Don't assume any of this from memory of prior stages — read each file
fresh. For each artifact, confirm:
- Does it have a Version Control sheet (xlsx) or section (docx) at all?
- If yes: list every row (version number, date, author/agent, and
  whatever "change" or "description" field it uses), exactly as it
  currently reads.
- If no: say so plainly, don't create one yet — see the CCG note below.

**The CCG is a known special case — do not silently fix it either way.**
Stage 9.6/11 already found and logged (`BE-TF-011`) that `BE-CCG-001` has
**no Version Control section at all**, unlike the DD, WTC, and the
Bulgaria reference CCG which all have one. That finding was deliberately
left open, not fixed, pending an owner decision. Confirm this is still
true by reading the current v1.2 file fresh. If it's still missing,
**do not create one on your own initiative** — list it in your report as
still-open and move on to the artifacts that do have one. Creating a new
section is a bigger structural decision than filling in existing rows,
and this pass is scoped to the latter.

Produce a table: Artifact | Has Version Control Y/N | Row count | Which
rows (if any) are blank/vague vs. already well-formed.

## STEP 2 — NORMALIZE, DON'T INVENT

For every artifact that has a Version Control table:

- **Leave the "1.0" row exactly as it is.** Do not reword it, even if its
  phrasing differs slightly from other artifacts' 1.0 rows. It is the
  baseline; consistency-for-its-own-sake is not a goal here.
- **For every later row:** if it already has a short, factual, one-line
  description of what changed (matching this project's own standing
  convention — brief and only what's confirmed, no padding, no
  speculation), leave it untouched. Editing a row that's already correct
  just to match a "standard phrasing" creates diff noise for no reason.
- **For every later row that's blank, vague ("various fixes", "updates"),
  or missing entirely for a version bump that clearly happened** (the
  filename or another artifact's cross-reference shows a version exists
  but the Version Control table has no row for it): fill it in — but only
  using what this session actually knows happened at that version. For
  DD v1.4, WTC v1.1, and CCG v1.2, that's fully documented in this
  session's own record: the 17 Stage 9.5 gap-closure items, the specific
  Bijlage/zone/code-table additions, the version-string propagation from
  Stage 9.6. Write the real, specific change — not a generic placeholder.
- **For any version row whose actual cause is genuinely NOT known from
  this session's record** (most likely: older bumps on the report specs,
  or DD/WTC/CCG versions from before today that were never detailed to
  you) — do not guess or invent a plausible-sounding reason. Mark it
  explicitly as unable to determine without inventing, and list it in
  your report as a gap for Wallisson to fill from his own memory or
  ticket history, rather than writing something that reads as confirmed
  but isn't.

## STEP 3 — EDIT SAFELY

xlsx Version Control sheets: XML-level surgery + zipfile repack per this
project's standing rule — never `openpyxl.save()` or a LibreOffice resave
on a file with embedded drawings/images. Validate well-formedness and run
a byte-identical drawings check after saving, same as every prior stage
this session.

docx (SIR): a targeted paragraph/table-cell edit, not a full regenerate.

## STEP 4 — VERIFY WITH GIT DIFF

```bash
git diff --stat
```
Then look at the actual diff for each touched file's Version Control
area specifically, confirming only that section changed — not any other
content in the artifact.

## OUTPUT

Report back: the Step 1 table for every artifact (including the CCG
special case, confirmed fresh), exactly which rows you filled in and
with what text, which rows you left alone because they were already
fine, and which rows (if any) you flagged as undeterminable rather than
guessed at. End with the CCG's status restated plainly as still open,
not decided in this pass.
