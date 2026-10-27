# Belgium WTC (BE-WTC-001-v1.0.xlsx) - Independent Verification Log

Built out of pipeline order (Stage 5 before Stages 3/4) at Wallisson's explicit decision,
using the fully-corrected BE-CCG-001-v1.0.docx as primary source. Verified independently
rather than trusting the building agent's self-report.

## Structural verification - all confirmed
- 6 sheets present: Version Control, Wage Type Catalogue, Sick Leave Paid By Employer, Tax Credit, Global WTC Coverage, Form Reference Guide
- Cell fill colors compared directly against the original CZ template, column by column - exact match, confirming formatting was preserved (not just cell values)
- Orange columns (1, 4, 8, 9, 11, 12, 13, 19, 20 - Mercans Code, Explanation, Calculation Type, Prorating Method, Ignore If 0, Enforce Setting, In Period Reconciliation, YTD Load, YTD Remarks): 100% empty across all 355 data rows, as required
- Blue columns: 355/355 populated in every case checked
- 300 Global WTC V1.0 baseline codes: cross-referenced directly against shared/Global_WTC_V1_0.xlsx (not the agent's claim) - 300 unique in baseline, 300 unique in the Coverage sheet's mapping table, zero missing, zero extra, zero duplicated
- Specialization sample (7 codes spread across the range): every generic baseline description maps to a sensible, CCG-consistent Belgian specialization (e.g. "Bonuses - discretionary or one-time" -> "Sport and culture vouchers"; "Arrears - Car allowance" -> "Arrears - company car benefit in kind")

## Verified reference values present in the correct rows
13.07% (126 rows), EUR 86,700 (employer exemption row, alongside the correct 24.92%/8.86%/3.80% breakdown), EUR 18,440 (flexi-job), EUR 4,255/3,701 (CBA90, same row as expected), GMMI progression (2,154.11 -> 2,233.61, same row), EUR 765 (fiscal work bonus)

## Flagged-not-guessed items confirmed genuine
- Special social security contribution: carries the full verified 2026 band table; the still-unconfirmed phase-out reform is NOT given an invented percentage - matches the CCG's own honest treatment of this same open item
- Non-competition indemnity / Decava levy: mechanism documented, rate explicitly left unspecified ("rates vary by age of beneficiary and by restructuring status") rather than invented
- Form Reference Guide: exactly the minimal PENDING placeholder requested - header row + one status row, no scope creep

## Two verifier errors self-caught during this review (not file defects)
1. First cross-check compared the Coverage sheet's generic baseline-derived name against the CATALOGUE's specialized Belgian name and flagged 100% of a spread sample as "DIVERGE" - this was the verifier's own logic error (comparing against the wrong reference); re-run comparing Coverage against the actual baseline file resolved to zero divergences.
2. Category comparison was case-sensitive ('deduction' vs 'Deduction'), producing a false mismatch signal alongside the above.

## Not yet independently content-reviewed (lower priority, structural presence confirmed only)
- Sick Leave Paid By Employer (17 populated rows) and Tax Credit (13 populated rows) sheets - confirmed non-empty, not yet checked line-by-line against the CCG's Module 8 guaranteed-salary table and Module 7 fiscal-work-bonus/overtime-relief content
- "Posting allowance" and "Mobility budget pillar 2" flagged notes - seen only as truncated snippets, full context not yet read
- No French-language column exists yet (Dutch only) - Version Control is stated to document this as a known gap, not yet independently re-read in full
- No DD alignment cross-check was performed (expected, given DD does not exist yet)

**Status: substantively verified at the structural and cross-reference level. No real defects found in this first verification pass** - the only "errors" surfaced were in the verification script itself, corrected during the same session.

---

## Systematic sweep of CCG-inherited uncertainty (see CCG_CONTENT_REVIEW.md for full detail)

Two items required a fix in the WTC as a direct consequence of the CCG sweep:
1. Tax Credit sheet - fiscal work bonus 2027-2029 phase-in now carries the "not confirmed enacted" caveat, matching the corrected CCG text
2. Wage Type Catalogue, CO2 solidarity contribution row - multiplier corrected from 2.75 to 4 for 2026 (confirmed via 4 independent sources)

Both defects existed because the WTC-building agent correctly followed instructions to treat the CCG as authoritative - the CCG itself had not yet been corrected on these two points at build time. No fault in the WTC-building process itself; the fix cascades from the CCG fix.

---

## MAJOR FINDING FROM REGRESSION AUDIT - WTC join key missing, since fixed

Discovered via a partial run of the compliance-qa-auditor subagent in regression mode
(BE-compliance/_qa/REGRESSION-BE-r1.json + narrative). The auditor found column A
(Mercans Code) in Wage Type Catalogue was empty across all 355 rows - a direct,
literal reading of the orange-column convention I applied from the original pipeline
template. diff_wtc_baseline.py, the toolkits own authoritative preservation-check
tool, reads column A as the join key against Global_WTC_V1_0.xlsx and reported
MISSING 300 / BASELINE VIOLATED - not because the baseline content was lost, but
because no automated system had any way to identify which row was which wage type.
My own earlier verification of the Coverage sheet had confirmed the HUMAN-READABLE
documentation was internally consistent, but never tested whether a MACHINE could
actually consume the file the way it is meant to be consumed - a real, meaningful
gap in my own verification approach this session.

### Fixed
- Populated column A: the 300 baseline rows (2-301) with their real Global WTC codes
  (copied from the already-verified Coverage sheet mapping, not re-derived), the 55
  Belgium-specific rows (302-356) with BE-001 through BE-055.
- Removed a residual "placeholder" marker in Version Control!C18 (a C29 lint failure
  validate_workbook.py should have caught but was never run against this file until now).
- Updated two narrative cells (Version Control!C28, Global WTC Coverage!A2) that
  claimed column A was orange-and-therefore-empty - both now describe the populated
  reality, while correctly noting the fill color itself remains orange (matching the
  CZ precedent, which populates its own orange Mercans Code column for all 398 rows -
  orange signals dev-team ownership, not mandatory emptiness).

### Independently verified by me directly (not just accepted from the fix agents report)
- diff_wtc_baseline.py re-run: KEPT 300, MISSING 0 (was 300) - the core defect is
  resolved.
- RENAMED 299 is NOT a regression - it is a pre-existing condition that could not be
  detected before (with an empty column A, nothing joined, so the description
  comparison never ran). The fix agent tested the SAME script against the actual CZ
  reference template itself and found it ALSO fails this check (KEPT 241/MISSING 59/
  RENAMED 148) - confirming RENAMED is an inherent property of any properly-localized
  country WTC, not a Belgium-specific defect, and correctly declined to fix it by
  overwriting real Belgian content with generic baseline text (which the instructions
  explicitly forbade).
- validate_workbook.py re-run: PASS, blocker=0, both before the narrative-cell fix and
  after - confirming the two text-only changes did not affect anything structural.
- Backup (.bak-before-joinkey-fix) confirmed present, correct size, not deleted.

### Recommendation flagged, not actioned (out of scope - a toolkit change, not a BE fix)
The fix agent recommends the toolkits own verdict rule treat MISSING/duplicates as
the blocker condition and RENAMED as advisory only, since the current all-or-nothing
BASELINE INTACT/VIOLATED verdict makes any legitimately localized WTC fail by design.
This is a suggestion for whoever owns mercans-artifact-toolkit, not something to
change unilaterally here.

**Status: the real defect (missing join key) is fixed and independently confirmed.
The tool still reports BASELINE VIOLATED due to RENAMED, which is expected,
inherent, and not something further action should try to eliminate.**
