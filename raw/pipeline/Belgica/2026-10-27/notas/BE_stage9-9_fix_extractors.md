# BELGIUM — STAGE 9.9: FIX THE TWO BROKEN EXTRACTORS (STEP A OF THE SYNC PLAN)

Run this locally on F5A4T8E, via Claude Code. This is Step A of the
5-step sync plan agreed after Stage 9.8: fix the tooling that's broken
before any actual `_backport/` sync can happen. Two different extractors,
two different situations — read Part 1 and Part 2 before starting either.

## SCOPE FENCE

You may edit: `extract_dd.py`, `extract_wtc_corrections.py`. You may READ
`_backport/`, the three current artefacts, and `build_be_wtc.py` /
`build_be_dd.py` to understand what each extractor needs. You may CREATE
the missing `WTC-regen.xlsx` file ONLY if Part 2's investigation makes its
correct construction unambiguous — see the stop condition there. Do not
edit anything in `_backport/` itself, do not edit the three artefacts, do
not edit `verify_generators.py` (already fixed in 9.8), do not touch
`mercans_pipeline_v2_9.sh` or `shared/country_failure_log.md`. Do not run
any of the four spec extractors or `extract_dd.py`'s actual extraction —
this stage fixes the tools' ability to run; actually running them to sync
`_backport/` is Step B, not this stage.

## STEP 0 — BASELINE COMMIT

```bash
cd ~/mercans-pipeline/BE-compliance
git add extract_dd.py extract_wtc_corrections.py
git commit -m "Pre-fix baseline, Stage 9.9 extractor repairs"
```
(If either isn't tracked yet, add it by name individually.)

## PART 1 — `extract_dd.py`: mechanical filename fix

Read the file fresh (don't trust the Stage 9.7 paraphrase). Confirm the
hardcoded reference to `BE-DD-001-v1.3.xlsx` and update it to
`BE-DD-001-v1.4.xlsx`. Same category of fix as Stage 9.8's `TARGETS`
correction — a stale literal, not a logic change. If the file has more
than one such reference (e.g. also in a docstring, a log message, a
default argument), update all of them, not just the first one found.

Do not run the extractor yet. Confirm with a dry check appropriate to
however this script is structured (e.g. `python3 -c "import extract_dd;
print(extract_dd.SOURCE_PATH)"` or equivalent) that it now resolves to a
file that actually exists on disk, without executing its extraction
logic.

## PART 2 — `extract_wtc_corrections.py`: two separate problems

**Problem 1, mechanical:** same as Part 1 — update the hardcoded
`BE-WTC-001-v1.0.xlsx` reference to `BE-WTC-001-v1.1.xlsx`. Fix this
regardless of how Problem 2 resolves.

**Problem 2, needs investigation before any action:** the script also
expects `~/be-tf/scratch/WTC-regen.xlsx`, which does not exist. Before
creating anything, answer from the actual source:

- What does `extract_wtc_corrections.py` itself say this file is — read
  its comments, variable names, and how it uses the file once loaded.
  Does it compare this file against the delivered WTC to find corrections
  (mirroring how the DD/spec extractors work), or is it used some other
  way?
- Is there anywhere in this codebase — a comment, a README, a sibling
  script, `_pipeline/backport_extractors/README.md` (already read once in
  Stage 9.7, re-check it for this specific detail) — that says how
  `WTC-regen.xlsx` is supposed to be produced? Look specifically for
  whether it's meant to be a fresh, unmodified output of running
  `build_be_wtc.py` against current `_backport/` data.
- Check `~/be-tf/scratch/` itself: do the DD and CCG regen files that ARE
  present there look like exactly this — a plain builder-output copy with
  no corrections layered in? If so, that's strong evidence the WTC one is
  the same pattern, just never generated.

**Stop condition:** if this investigation gives a single, unambiguous
answer (most likely: "run `build_be_wtc.py` fresh against current
`_backport/`, save its output to that exact path, nothing else"), do it
and confirm the extractor now finds the file. If the investigation is
ambiguous, or if producing this file would require any judgment call
about WHICH corrections to include or exclude, STOP — do not construct a
guessed version of this file. Report exactly what you found and why it's
ambiguous, and leave Problem 2 open rather than fixing it with an
assumption.

## STEP 3 — CONFIRM BOTH EXTRACTORS CAN NOW AT LEAST START

For whichever of the two got fully fixed, confirm (without running a full
extraction) that the script no longer fails on a missing/wrong-named
input file — e.g. it gets as far as opening its source file successfully,
even if you stop short of running the actual extraction logic, which is
Step B's job, not this stage's.

## STEP 4 — VERIFY WITH GIT DIFF

```bash
git diff -- extract_dd.py extract_wtc_corrections.py
```
Confirm the diff shows only the filename-literal changes (and, if Part
2's stop condition was cleared, whatever minimal change let it find
`WTC-regen.xlsx`) — nothing else.

## STEP 5 — RECORD THE RESULT

Append a short dated note to
`07-qa-crosscheck/BE-generator-drift-diagnosis-2026-09-16.md`: what got
fixed in each extractor, and — if Problem 2 was left open — exactly what
question still needs answering and by whom (you, if it's a judgment call
only the artefact owner can make; not a research question I could resolve
some other way).

## OUTPUT

Report back: the Part 1 fix and its dry-check result, Part 2's
investigation findings and whichever of (fixed / stopped-and-flagged)
applies, and the Step 4 diff.
