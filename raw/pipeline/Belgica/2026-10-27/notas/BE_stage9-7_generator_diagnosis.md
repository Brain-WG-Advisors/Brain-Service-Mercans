# BELGIUM — STAGE 9.7: DIAGNOSE GENERATOR / BACKPORT DRIFT (READ-ONLY — NO FIXES THIS PASS)

Run this locally on F5A4T8E, via Claude Code. This is investigation only.
Do not edit `_backport/`, `verify_generators.py`, or any of the three main
artefacts. The goal is a clear, honest map of the problem so a real fix
can be scoped afterward — not a fix itself. I (the assistant in chat) have
never seen these files and cannot specify a patch blind; this stage exists
to change that.

## SCOPE FENCE

Read-only access to: `_backport/`, `_pipeline/verify_generators.py` (or
wherever it actually lives — confirm the real path, don't assume),
`_pipeline/build-manifest.json`, and the three current artefacts
(`BE-DD-001-v1.4.xlsx`, `BE-WTC-001-v1.1.xlsx`, `BE-CCG-001-v1.2.docx`) for
comparison purposes only.

The only file you may WRITE is a new diagnostic report at
`07-qa-crosscheck/BE-generator-drift-diagnosis-2026-09-16.md`. Do not
modify `_backport/`, do not modify `verify_generators.py`, do not modify
any of the three artefacts, do not touch `mercans_pipeline_v2_9.sh` or
`shared/country_failure_log.md`. If mid-investigation you find something
that seems trivial to fix in passing, don't — note it in the report
instead. This stage produces a map, not a patch.

## STEP 1 — WHAT IS `_backport/`, ACTUALLY

Read enough of `_backport/`'s contents to answer, plainly, for whoever
reads this next (someone who has never seen this folder either):

- What does it contain — data files (JSON/CSV/YAML), Python modules that
  build the artefacts, both, something else?
- For each of the three artefact types (DD, WTC, CCG), what in `_backport/`
  is supposed to correspond to it? Name the actual file(s)/module(s).
- Is there a documented (comment, README, docstring) explanation of how
  `_backport/` relates to the pipeline's normal Stage 4/5/1 generation, or
  is the relationship only inferable from the code itself?
- Roughly how large / how structured is this: a handful of files, or a
  large module tree? Give real numbers (file count, line count), not an
  impression.

## STEP 2 — RUN THE EXISTING VERIFIER, IF IT RUNS

```bash
python3 _pipeline/verify_generators.py
```
(adjust path once Step 1 confirms the real location)

If it runs cleanly: report its output as-is — don't summarize away
specific numbers it gives you.
If it errors: report the exact error. Do not patch the verifier to make
it run — that's a fix, out of scope for this pass. Note what's broken and
move to Step 3 with whatever partial signal you have.
If no such tool exists at all (the path referenced in prior handover notes
doesn't resolve to anything real): say so plainly rather than searching
indefinitely for it.

## STEP 3 — CHARACTERIZE THE DRIFT, NOT JUST COUNT IT

A raw cell-diff count (e.g. "3,172 differing cells") was already reported
once and is not, by itself, useful for scoping a fix — it doesn't say
whether that's 3,172 unrelated one-off edits or 12 categories of change
each hitting ~260 cells the same way. For each of the three artefacts,
answer:

- What are the DISTINCT CATEGORIES of thing that changed and that
  `_backport/` doesn't know about? (e.g. "the 6 new NSSO annex blocks
  added in Stage 9.5 don't exist in the backport data model at all" is one
  category, even if it's 400+ cells; "the version-string propagation from
  Stage 9.6 touched 831 cells across one repeated find/replace" is another
  single category, even though it's a large number)
- For each category: does `_backport/`'s current data structure have ANY
  place to represent this kind of content, or would representing it
  require a structural change (new fields, new module, not just new
  values in an existing one)?
- Which categories look like a small, mechanical sync (copy a table's
  current values into wherever `_backport/` expects them) versus which
  look like they'd need the backport model itself extended first?

## STEP 4 — HONEST SCALE ESTIMATE

Based on Step 3's categorization, give a rough, explicitly-labelled-as-rough
sense of effort for each of the three artefacts separately: "small sync",
"moderate — needs N new fields/entries but no structural change", or
"structural — the backport model doesn't currently have anywhere to put
this category of content." Do not produce a time estimate in hours; that's
not something this investigation can responsibly claim. A relative sense
of scale per artefact is what's useful here.

## STEP 5 — WRITE THE DIAGNOSTIC REPORT

`07-qa-crosscheck/BE-generator-drift-diagnosis-2026-09-16.md`, covering
Steps 1-4 plainly. End with a short "open questions for the owner" section
listing anything Step 1-4 couldn't resolve without a judgment call only
Wallisson can make (e.g. "is `_backport/` meant to be the source of truth
going forward, or is direct-artefact-editing now the accepted practice and
`_backport/` should be retired instead of maintained?" — don't answer that
question yourself, just make sure it's asked if it's live).

## OUTPUT

Report back: the Step 1 answers, Step 2's raw tool output (or the error),
Step 3's category table for each artefact, and Step 4's per-artefact scale
read. Do not propose a fix plan yet — that's the next stage, once this
diagnosis is in hand.
