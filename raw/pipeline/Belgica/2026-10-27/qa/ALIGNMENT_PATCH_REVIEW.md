# Belgium Alignment Patch (Stage 8) - Independent Verification Log

Covered Checks 1-3 (option mapper alignment, option values completeness, conditional
bidirectionality) since field-classification alignment was already done exhaustively
during the DD build. Scale: 13 content mismatches, 39 binding defects, 37 missing
mappers, 137 bidirectional gaps, 178 fields with a code table but no Sheet 6 entry
- 10 files patched.

## Urgent process gap found and corrected immediately
The patch agent deleted its own pre-patch backups as "scratch cleanup," and
BE-compliance/ was never under version control - meaning the exact pre-patch state
was unrecoverable. Immediately git-committed the current (post-patch) state as a
baseline (commit f670bfa) so future changes are protected, even though the specific
pre-patch snapshot is genuinely lost. Lesson for future agent prompts: explicitly
instruct "do not delete backups until told to."

## Independently verified - the two most consequential findings
- **Gender mapper**: confirmed cell-by-cell. Code 1/2 now carry the correct NSSO
  zone 00029 citation; code X is explicitly flagged "NO NSSO CODE EXISTS" with
  resolution deferred to INSZ parity - matches the patch report exactly.
- **Charge Bearer / DEBT (SEPA)**: confirmed cell-by-cell. SLEV is marked (in the
  file's own emphasis) as the only value usable on a European Credit Transfer; DEBT/
  CRED/SHAR are explicitly marked not permitted on that transfer type. This is the
  fix the report said would have produced a rejected payment file if left as the DD
  originally had it.

## Noted, not independently re-verified (lower priority given time)
- 18 fields moved off a generic Yes/No Boolean mapper onto the correct NSSO
  transmission codes (0/1, 0/1/9, 0-5)
- 137 bidirectional conditional-reference fixes
- 407 bilingual code rows added across 5 specs, DD mapper count 47 -> 87
- A pre-existing (not newly introduced) C29 lint failure on BE-FEDRIS-001, unrelated
  to this patch's own scope, fixed as a byproduct (rephrased a literal "XXX" BIC
  branch-code description that the lint was matching as a residual marker)
- WTC required no changes - confirmed unaffected, including re-confirming the
  already-known box-360 gap is still present (0 wage types), consistent with the
  earlier Reports Spec review finding

## Explicitly flagged as unresolved by the patch itself (not resolved here either)
- FEDRIS zone 00431 vs 00432 transcription discrepancy - which is correct not
  determined
- A dangling SEPA field reference (InitgPty/Id) specified nowhere in the workbook
- 5 truncated source-domain definitions - values recorded as far as the source goes,
  marked NOT FOUND identically on both sides rather than guessed
- One zone's comparison operator is an unrenderable control character - direction
  (at-least vs at-most) cannot be stated from the source as held

**Status: the two highest-stakes findings independently confirmed correct. The
process gap (deleted backups, no git baseline) was the most important thing this
review caught, and has been corrected going forward.**
