# BELGIUM — STAGE 9.5: APPLY GAP-CLOSURE PATCHES, THEN VERIFY & FINALIZE

## SCOPE FENCE — READ THIS FIRST, THEN RE-CHECK IT BEFORE EVERY STEP

You may read, edit, and commit ONLY these three files:
- `BE-DD-001.xlsx`
- `BE-WTC-001.xlsx`
- `BE-CCG-001.docx`

This working directory contains a large amount of unrelated in-progress work
from other sessions (other countries' files, the shared pipeline script,
the shared failure log, dozens of loose debug/fix scripts and backups). None
of it is in scope for this task, no matter how related or "worth touching
while you're here" it looks. Do not open, edit, or `git add` anything
outside the three named files — including `mercans_pipeline_v2_9.sh` and
`shared/country_failure_log.md`. If you find yourself about to touch
anything else, stop and report it as a scope question instead of acting.

Run this locally on F5A4T8E, via Claude Code. This is a single, self-
contained action: it applies every item in BE_gap_closure_patch_spec.md
to the three files above, proves each edit with git, then runs the closing
audit.

**If this is a re-run after a max-turns cutoff:** start with `git diff --
BE-DD-001.xlsx BE-WTC-001.xlsx BE-CCG-001.docx` against the baseline commit
before doing anything else. Any item whose NEW content (per the spec) is
already present is done — do not re-touch it, do not re-verify it beyond
confirming it's in the diff. Spend turns only on items not yet reflected.
If no baseline commit exists yet, this is a first run — proceed from Step
0 normally.

Read BE_gap_closure_patch_spec.md (in this same folder) in full before
starting. It has the exact old→new content and source for every item.

## STEP 0 — BASELINE COMMIT, SCOPED TO THE THREE FILES ONLY

```bash
cd ~/mercans-pipeline/BE-compliance
git add BE-DD-001.xlsx BE-WTC-001.xlsx BE-CCG-001.docx
git commit -m "Pre-patch baseline, 17-item gap closure (BE-DD/WTC/CCG only)"
```

**Do NOT run `git add -A` or `git add .`** — this directory has unrelated
uncommitted work from other sessions sitting in it, and a blanket add will
sweep that in under this commit's message. Add only the three named files,
explicitly, by name. If either command errors because one of the three
isn't tracked yet, `git add` that specific file only, still by name — never
fall back to `-A`.

If a commit with this message already exists, don't make a second one —
use the existing baseline.

## STEP 1 — APPLY EACH ITEM, ONE AT A TIME

For each of the 15 content items in BE_gap_closure_patch_spec.md (DD items
1-6, WTC items 7-8, CCG items 9-15):

1. Open the target file (BE-DD-001.xlsx, BE-WTC-001.xlsx, or BE-CCG-001.docx)
2. Locate the cell/field by the OLD placeholder text described in the spec
   (never assume a row number — read the header row first)
3. Apply the NEW content exactly as given in the spec — surgical XML-level
   edit + zipfile repack for xlsx (never openpyxl.save() or a LibreOffice
   resave on a file with embedded drawings/images), tracked-change insert
   for docx per the usual protocol
4. Validate well-formedness immediately after that single edit, before
   moving to the next item

## STEP 2 — CONFIRM EVERY PATCH LANDED (git diff, not self-report)

```bash
git diff -- BE-DD-001.xlsx BE-WTC-001.xlsx BE-CCG-001.docx
```

Read the actual diff output against the Step 0 baseline for each of the
15 items. If an item you believe you patched shows no change in the diff:
it did not land. Flagged is not fixed — re-apply that one item, re-check,
do not mark it done on the strength of having "tried."

Produce a table: Item | File | git diff confirms Y/N | Notes.
Do NOT proceed to Step 3 until every row is Y.

## STEP 3 — RESOLVE THE TWO OPEN QUESTIONS FROM THE SPEC

**Annexe III point label (Item 14):** open
https://www.securex.be/fr/lex4you/employeur/themes/remunerer/charges-salariales-le-precompte-professionel/remunerations-mensuelles-(et-revenus-y-assimiles,-a-l-exception-des-revenus-de-remplacement)
and confirm whether the child-dependent reduction section is explicitly
labelled with a point number. Update the CCG citation to the real number
if found; if the page genuinely doesn't expose one, note "point number not
published on this source, content and figures confirmed" instead of
guessing.

**Bijlage 12 status (the one item never closed):** open
https://www.socialsecurity.be/lambda/portail/glossaires/bijlagen.nsf/web/Bijlagen_Home_Nl
in an actual browser (it uses frames — a fetch tool won't render it) and
check whether Bijlage 12 exists in the current DmfA bijlage list at all.
- If it does NOT exist (matching what the 2024/4 Glossarium's own bijlage
  index showed — the list jumps 11 → 21): write the DD row as
  "RESOLVED — Bijlage 12 not part of current DmfA bijlage set, retired or
  renumbered; not applicable" and close it that way.
- If it DOES exist: open it, extract the current code table, and patch the
  DD row with the real content instead of the resolution note.
Either way, this item gets a real answer here — don't leave it PENDING.

## STEP 4 — RE-LABEL, DON'T RESEARCH FURTHER

Confirm the "Contract Duration Type" DD row now reads as
resolved-not-applicable (per the spec), not as a filled-in code list and
not as still-pending. If it still shows a placeholder, apply that one-line
resolution note now — this does not need more research, only the label
change.

## STEP 5 — MECHANICAL RE-AUDIT

Re-run the country's own audit script (the same C1-style mechanical checks
used at Stage 9 for every other country) against the patched DD, WTC, CCG.
Confirm zero remaining NOT FOUND / PENDING / TODO markers across all three
files. If any turn up that aren't in the patch spec, list them — do not
absorb them silently into this pass; they're a new finding, not something
this session already covered.

## STEP 6 — HANDOVER STATUS

Produce `BE-compliance/07-qa-crosscheck/handover_status.md` in the same
format used for Colombia (Overall verdict, artifacts table, audit results,
remaining issues if any, sign-off recommendation). Overall verdict is
READY_FOR_HANDOVER only if Step 2's diff table is all-Y, Step 5 came back
clean, and Step 3's Bijlage 12 question got a real answer (either patched
or marked not-applicable) rather than left open.

## OUTPUT

Report back: the Step 2 diff table, the two Step 3 answers, and the final
verdict line from Step 6.
