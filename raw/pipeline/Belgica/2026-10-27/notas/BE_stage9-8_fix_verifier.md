# BELGIUM — STAGE 9.8: FIX THE VERIFIER ITSELF (NOT THE DRIFT IT REPORTS)

Run this locally on F5A4T8E, via Claude Code. This fixes exactly two bugs
in `verify_generators.py`, confirmed by the Stage 9.7 diagnosis: it points
at filenames that no longer exist, and it silently treats "could not check
this artefact" the same as "this artefact is fine." It does not sync any
drift, does not touch `_backport/`, and does not touch the two broken
extractors (`extract_dd.py`, `extract_wtc_corrections.py`) — those are
separate, later work.

## SCOPE FENCE

You may edit exactly one file: `_pipeline/verify_generators.py` (confirm
this is the real path first — Stage 9.7 reported it, but read it fresh
rather than trusting the prior report, per standing practice on this
project). You may READ the three current artefacts
(`BE-DD-001-v1.4.xlsx`, `BE-WTC-001-v1.1.xlsx`, `BE-CCG-001-v1.2.docx`) and
`_backport/` to confirm the fix works when run, but write to none of them.
Do not touch `extract_dd.py`, `extract_wtc_corrections.py`,
`mercans_pipeline_v2_9.sh`, or `shared/country_failure_log.md`.

## STEP 0 — BASELINE COMMIT

```bash
cd ~/mercans-pipeline/BE-compliance
git add _pipeline/verify_generators.py
git commit -m "Pre-fix baseline, verify_generators.py TARGETS + SKIP bug"
```

## STEP 1 — READ THE ACTUAL CURRENT LOGIC, DON'T ASSUME THE PARAPHRASE

Open `verify_generators.py` and confirm, from the real source, not from
memory of the Stage 9.7 report:
- The exact name and structure of whatever maps generators to expected
  artefact filenames (called `TARGETS` in the prior report — confirm the
  real name).
- The exact current filename strings it holds for the DD, WTC and CCG
  entries.
- The exact place in `main()` (or wherever) where DRIFT / SKIP / OK
  verdicts are produced, and the exact place where the final
  pass/fail decision and exit code are computed. Confirm SKIP is genuinely
  excluded from whatever list drives that decision, as reported — if the
  real code turns out to already handle this correctly and the prior
  report was wrong, say so and stop rather than "fixing" something that
  isn't broken.

## STEP 2 — FIX THE STALE FILENAMES

Update the three entries to the current, correct filenames:
- DD: `BE-DD-001-v1.4.xlsx`
- WTC: `BE-WTC-001-v1.1.xlsx`
- CCG: `BE-CCG-001-v1.2.docx`

Change only these three string values. Don't touch the nine spec entries,
which Step 1 of the Stage 9.7 diagnosis already confirmed are correct
(glob-based, unaffected by the rename).

## STEP 3 — FIX THE SKIP-AS-SUCCESS BUG

A SKIP verdict means "could not be checked" — it must never be treated as
equivalent to OK. After this fix:
- A run containing any SKIP must exit non-zero, same as a run containing
  any DRIFT.
- The final summary must distinguish the three verdicts explicitly, not
  just report a pass count — something like "N reproduced, M drifted, K
  could not be checked" rather than a single "All N reproduce" line that
  would read as clean when K > 0.
- Do not make SKIP disappear by, e.g., excluding those three generators
  from the run instead of reporting them — the point is visibility, not a
  quieter false-clean result.

## STEP 4 — RE-RUN AND REPORT THE REAL, CURRENT OUTPUT

```bash
python3 _pipeline/verify_generators.py
```

Report the full, actual output verbatim. The DD, WTC and CCG will very
likely now show real DRIFT — that is expected and correct, not a new
problem: Stage 9.7 already established none of the three has been synced
to `_backport/` since 25 August. This stage's job is only to make the tool
report that truthfully; syncing the drift itself is separate, later work
that depends on the still-open question of whether `_backport/` stays the
source of truth.

## STEP 5 — VERIFY WITH GIT DIFF

```bash
git diff -- _pipeline/verify_generators.py
```
Confirm the diff shows exactly the TARGETS filename changes and the
SKIP-handling change, nothing else.

## STEP 6 — APPEND ONE SHORT NOTE

Append a short dated note to the existing
`07-qa-crosscheck/BE-generator-drift-diagnosis-2026-09-16.md` (don't
create a new report file) recording: the two bugs fixed, and the real
Step 4 output now that the gate can actually see all 13 generator/artefact
pairs. Leave the rest of that document as Stage 9.7 wrote it.

## OUTPUT

Report back: the Step 1 findings (confirming or correcting the prior
report), the exact diff from Step 5, and the full Step 4 verifier output.
