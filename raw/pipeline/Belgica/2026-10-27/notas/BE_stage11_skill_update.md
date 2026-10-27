# BELGIUM — STAGE 11: UPDATE THE COUNTRY SKILL AGAINST TODAY'S FIXES

Run this locally on F5A4T8E, via Claude Code. Goal: `payroll-compliance-
belgium` must reflect the current, fixed artifacts —
`BE-DD-001-v1.4.xlsx`, `BE-WTC-001-v1.1.xlsx`, `BE-CCG-001-v1.2.docx` —
including the 17 items closed today (Stage 9.5) and the version renames
(Stage 9.6). It currently does not: the skill was last compiled before any
of today's work.

## STEP 0 — DON'T ASSUME STAGE 11 EXISTS; CHECK THE LIVE SCRIPT

The pipeline's own methodology explicitly warns that whether an automated
Stage 11 / skill-compiler block genuinely exists in the current orchestrator
is disputed between two prior accounts, and instructs checking the live
script rather than trusting either account. Do that now:

```bash
grep -n -i "stage.11\|skill.compil\|agent.?9\|payroll-compliance-" mercans_pipeline_v2_9.sh | head -50
```

Read enough context around any hits to answer plainly:
- Does a real, runnable Stage 11 block exist in THIS script, right now?
- If yes: what does it actually take as input, and does it point at the
  artifacts by their OLD filenames (v1.3/v1.0/v1.1) the way the generator
  `TARGETS` did before Stage 9.8 — check this specifically, since it's the
  exact bug we already found and fixed once elsewhere in this same script.
- If no such block exists (or it's clearly a stub/placeholder, not real
  logic): say so plainly and move to Step 2 (manual path) instead of
  Step 1.

Do not edit `mercans_pipeline_v2_9.sh` in this stage regardless of what
you find — read-only for this file, this pass. If it needs fixing,
that's separate, later work.

## STEP 1 — IF STAGE 11 IS REAL: RUN IT, THEN VERIFY IT WASN'T THIN

If Step 0 confirms a working Stage 11 block, run it against the current
artifacts (correcting any stale filename reference you found, the same way
Stage 9.8 did for the verifier — but only for this run's invocation, not
as a permanent script edit unless that's unambiguously the same one-line
fix and you say so explicitly).

**Before declaring success, check for the exact failure already on
record for this pipeline:** a previously-delivered country skill was
found noticeably thinner than an earlier informal version, traced to
either the router never pulling in its linked references, or those
references being summarized rather than genuinely full content. Check:
- Every reference file's size — anything under ~5KB is a red flag for a
  content type that should hold a full artifact's worth of material.
- Whether the DD's ~958 new code rows, the WTC's work-bonus cap closure,
  and the CCG's Article 11bis / Annexe III content from today's Stage 9.5
  actually appear verbatim in the relevant reference file(s) — spot-check
  by grepping for a specific string from today's work (e.g. "3.594,36" or
  "Bijlage 12") inside the compiled skill's files, not just checking that
  a file changed size.

If either check fails, Stage 11's output is not usable as-is — report
this plainly rather than shipping a thin skill, and fall through to Step
2's manual approach for whatever's missing.

## STEP 2 — IF NO WORKING STAGE 11 EXISTS: LOCATE AND MANUALLY REFRESH

First, find what actually exists today:
- Check `08-skill/` inside `BE-compliance/` for an existing compiled
  package.
- If nothing is there, the previously-delivered 3.1MB
  `payroll-compliance-belgium` may only exist as whatever the user has
  outside this repo (a prior download) — ask for it rather than assuming
  its location or rebuilding from scratch, since "assumed provenance" of
  an unexplained file is exactly the kind of thing this project's own
  standing rules say to verify, not guess.

Once you have the actual current package, confirm its real structure
(thin `SKILL.md` router + `references/` folder — per this pipeline's
convention, one full, verbatim file per artifact type, not a summary).
Then, for each of today's changes:
- Identify which reference file(s) correspond to DD content, WTC content,
  and CCG content.
- For each of the 17 Stage 9.5 items plus the Stage 9.6 version renames,
  confirm whether that specific content is present in the corresponding
  reference file. Build a short table: Item | Reference file | Present
  before this pass Y/N.
- For every N, update that reference file with the real current content
  from the actual artifact — copy the genuine material, don't paraphrase
  or summarize it down, matching the "full, verbatim" convention.
- Update the router's version references and the skill's own changelog/
  version note (if it has one) to point at v1.4/v1.1/v1.2.

## STEP 3 — REPACKAGE AND VERIFY

Rebuild the skill as a zip with the folder (not just SKILL.md) at its
root, matching how it's meant to be uploaded. Confirm:
- Total size is comparable to or larger than the prior 3.1MB (a much
  smaller output after adding ~958 new DD rows and multiple new sections
  would itself be a sign something didn't make it in).
- `SKILL.md`'s own description/frontmatter still accurately describes
  what's covered — update it if the 17 items added coverage areas it
  didn't mention before (e.g. Bijlage 12, DmfA Remuneration/Service
  codes, if those weren't previously named).

## OUTPUT

Report back: the Step 0 grep findings and which path (1 or 2) applied,
whichever path's verification table/checks, and the final zip's location,
size, and a one-line confirmation of what changed versus the previous
package.
