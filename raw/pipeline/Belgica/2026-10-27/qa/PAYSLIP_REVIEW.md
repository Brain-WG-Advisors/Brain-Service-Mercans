# Belgium Payslip - Independent Verification Log

Built with all prerequisites already in place (CCG, Report Specs, DD, WTC, SIR all
existed) - the first stage this session built in-order rather than out-of-order.
Sample employee (Jan Peeters, PC 200) deliberately chosen to reconcile line-for-line
with CCG Module 12 Example 1.

## Round 1 - 5-sheet build
- Hand-recomputed the full gross-to-net cascade independently: every figure matches,
  using the CORRECTED tax-engine parameters (11,170 allowance, 16,710 and 29,500 bracket
  ceilings, 9,944.05 cumulative constant) - confirms the tax-engine fix propagated
  correctly into a brand-new artifact without needing to be told.
- Employer cost (5,195.03) independently recomputed and matched.
- Build's own self-check: 43 comparisons per sheet, both sheets, 0 failures.

## The 5-vs-8-sheet decision
validate_workbook.py --artifact PSL (found at
C:\Users\instituto\.claude\skills\mercans-artifact-toolkit\scripts\validate_workbook.py
- a Claude Code Skill, not a project-tree file, hence not found by an initial
project-scoped search) requires 8 sheets; the original build followed the v2.4
pipeline script's own documented 5-sheet standard instead. Wallisson chose 8 sheets
(pass the validator) after the conflict was surfaced explicitly rather than resolved
unilaterally either way.

## Round 2 - adding the 3 missing sheets
- Sheet order sourced from the toolkit's own SKILL.md (documented, not guessed).
- De-risked BEFORE writing: tested an openpyxl load-then-save round-trip for image loss
  first, given both the source and target files carry embedded logos.
- Only 4 cells retouched for Belgium-specific content, each guarded by an
  expected-old-value assertion (fails loudly rather than silently miscopying if the
  reference template changes).
- "How to set up Payslip" needed zero changes - its own examples reference Estonia,
  not Mozambique, so no country-name find-and-replace was needed there.

## Independently re-verified (not just trusted from either build log)
- Re-ran validate_workbook.py directly: PASS (blocker=0 major=0 minor=0), 8 sheets
  in the documented order - reproduced myself, not accepted from the report.
- Re-ran _verify_payslip.py directly: TOTAL FAILURES: 0, all 43 lines per sheet,
  including YTD and leave-balance blocks not previously spot-checked by hand.

**Status: fully verified, both content (triple-checked: hand calculation, build's
own independent recomputation, and my own re-run of the verification script) and
structure (validator re-run independently, genuine PASS).** No open items on this
artifact specifically.


---

## REGRESSION AUDIT FINDINGS AND FIX (16 August)

1 blocker, 4 major, 3 minor found. The blocker and 2 majors fixed and verified.

### BE-PSL-001 (blocker) - FIXED and verified
Payslip Spec sheet had 5 sections/37 rows while the actual payslip renders 15
distinct blocks - 58% of displayed content (working time, employer cost, all 18
withholding steps, YTD, leave balances, banking) had no HRP mapping at all. This
survived my own extensive prior verification because I checked the DISPLAYED
NUMBERS were correct (by hand, three times) but never opened the Spec sheet to
confirm it could actually be BUILT FROM. Same class of gap as the earlier WTC
join-key issue: correct output does not imply a buildable specification.
Rebuilt to 15 sections/126 rows. Every new HRP mapping token verified to resolve
to a real BE-DD-001 field or BE-WTC-001 code - not invented. The 37 pre-existing
rows re-emitted programmatically and verified 37/37 preserved verbatim.
Independently reverified: validate_workbook.py PASS; cell-by-cell diff against
backup confirms Belgium (EN)/(NL) sheets have exactly 3 value changes each (the
2 separate text fixes below), 585 diffs in Payslip Spec (the rebuild), 0 diffs
in the other 5 sheets; 55 formula cells 0 divergences; 0 error cells.

### BE-PSL-002 (major) - FIXED and verified
The payslip stated a "one-band rule" for the special SS contribution while
silently applying a six-band table (the underlying figure was always correct -
Q2 lands in a different band due to May's double holiday pay). Corrected the
prose to describe the real six-band mechanism. No formula or figure changed.

### BE-PSL-004 (major) - FIXED and verified
Language-gap note named only French as pending; scope_manifest.json documents
both French AND German (Belgium has three official language regions). Both now
named. Side effect: removing "pending" from the note brought the residual-marker
sweep to 0 hits across all six BE-authored sheets (was 1).

### Still open, explicitly out of scope for this pass
- BE-PSL-003: 3 pre-existing broken $x.custom.* tokens - partially closed as an
  incidental side effect of the new Language Regime row, not directly addressed.
- BE-PSL-005, 006, 008: untranslated NL text and other minors - untouched.

**Status: the blocker and both majors addressed are fixed and independently
confirmed. 3 lower-priority items remain open.**
