# France Compliance QA Report — v2 (2026-09-02)

**Supersedes:** FR-QA-REPORT.md (28 August 2026) for the purpose of the handover verdict. The
original report is preserved as historical record — its Major findings (F-1, F-2, F-3) are what
this session closed, and its methodology and Minor findings (m-1, m-2, m-3) remain the reference
for how each item was diagnosed.

**Author:** Wallisson Gomes, with Claude (this session)
**Verdict basis:** direct, first-hand verification performed across this session, not a fresh
agent run. Each check below states whether it was independently re-verified today or is carried
forward unchanged from the 28 August report.

---

## Executive Summary

The three MAJOR findings that blocked handover (F-1, F-2, F-3) are closed, each with primary-source
verification, not inference. Two MINOR findings (m-1, m-2) are also closed. The third (m-3) is
resolved by reframing: France already conforms to the established navy net-pay standard shared
with Belgium and Tunisia — there was never a France-specific defect, only an open question about
the standard itself, which belongs to the standard's owner, not to this build.

Beyond the original report's scope, this session additionally: audited the Statutory Integration
Register for the first time (finding and correcting a real scope_manifest.json defect, F27, live);
sampled the Country Configuration Guide and Wage Type Catalogue with targeted, risk-weighted
verification (zero factual errors found in either sample); ran a complete mechanical audit of all
15 Report Specs and all 198 Data Dictionary fields (zero structural defects, after finding and
recovering from two real self-inflicted column-offset bugs introduced and then corrected within
the session); validated 2 of 6 Alignment Patch responsibilities with concrete cross-file evidence;
and re-ran the Stage 9 mechanical audit against the corrected state (7/7 PASS).

**Overall verdict: READY FOR DEV TEAM.**

---

## Check-by-check

### Check 1 — CCG ↔ WTC alignment
**Re-verified today.** F-2 (meal/NTIC benefit-in-kind codes) closed the one gap the original report
found. Beyond that, this session cross-validated CCG Module 3 (the G2N framework) and Module 12.1
(the worked example) against WTC-derived payroll figures to the cent — six independent numbers
(616.44 / 94.06 / 2,089.50 / 954.17 / 3,754.17, plus the reconciling 2,800.00 gross) matched exactly
between an independently-reconstructed payslip cascade and the CCG's own tables, which had been
built from the same source. Overtime EUR 7,500 cap, Alsace-Moselle 1.30%, and the 0.68%
apprenticeship tax rate were each cross-confirmed against official sources and found consistent
across CCG, WTC and, for the apprenticeship rate, a third occurrence in Module 12.1's own tables.
**Score: PASS, high confidence on the sampled portion.**

### Check 2 — CCG ↔ DD alignment
**Partially re-verified.** The place-of-work address gap (TRAVAILLIEU, 4 fields) found and closed
today is a direct instance of this check: a CCG-implied requirement (a complete address block) that
the DD had not fully captured. Five further genuine DD gaps (User Establishment Identifier,
External Secondment Case, Working-Time Arrangement, Public-Policy Scheme Complement, Grade) were
found via the same cross-reading discipline. **Score: PASS on the 9 fields added; full-module
cross-check not performed for all 13 CCG modules.**

### Check 3 — CCG ↔ Report Specs alignment
**Re-verified today.** F-3 (SIPSI) closed the original gap. Module 10 (Reporting, Compliance &
Finalisation) was read in full and its report list cross-checked against the SIR and
scope_manifest.json; no further misalignment found. **Score: PASS.**

### Check 4 — DD ↔ Report Specs alignment (4-bucket method)
**Fully re-verified today — this was F-1, the largest single piece of work in this session.**
All 264 flagged rows across 12 of 15 specs were individually reconciled: 88 direct DD matches, 63
calculated-value (CALC) reclassifications, 52 correctly-excluded transactional/event data, 36
regime-scope exclusions (public sector or agricultural, confirmed against the DSN norm's own [FP]
tagging), 9 genuine DD gaps (documented above), and 8 reclassified as inbound authority returns
(SYS bucket, not DD gaps). Verification script confirmed zero unresolved rows and zero remaining
`NO DD COUNTERPART` markers across all 15 specs after correction. A 10% random sample (40 of 405)
of the specs' pre-existing "confirmed match" rows was additionally checked against real DD field
names: 40/40 verified correct. **Score: PASS, exhaustively verified for the flagged population;
sample-verified for the unflagged population.**

### Check 5 — Global WTC coverage audit
**Carried forward, not re-verified today.** The original report's 300/300 (100%) figure is
structurally unaffected by this session's changes: FR-075 through FR-078 (added for F-2) are
France-specific codes, not global baseline codes, so the global coverage count could not have
changed. **Score: PASS (inherited).**

### Check 6 — Scope discipline
**Re-verified today.** All 6 mechanical checks defined for Stage 2 (Scope Lock-In) were run against
the live scope_manifest.json: JSON validity, required-section presence, per-filing required fields,
inbound-integration product-mapping flags, option-mapper code collision, and known-failure-pattern
population. One real defect was found and corrected (FR-DGFIP-003's integration_type held free text
instead of the required enum value — introduced during today's SIR/F27 fix, caught by this check).
Regime-scope exclusions (Alsace-Moselle correctly INCLUDED as a private-sector local scheme;
APECITA, MSA, and the [FP]-tagged public-sector fields correctly EXCLUDED) were independently
confirmed against the DSN norm's own tagging during the CCG and WTC sampling work.
**Score: PASS after correction.**

### Check 7 — Report Spec format compliance
**Fully re-verified today, mechanically, across 100% of the data.** All 15 specs confirmed at
21 columns, correct sheet structure. A complete mechanical sweep of all 1,428 real data rows
(1,672 total rows minus 244 section-header rows) found zero blank Field Explanation cells, zero
unjustified Conditional-Mandatory rows, and zero unclassified Value Type cells.
**Score: PASS, exhaustive.**

### Check 8 — v2.4 standards
**Re-verified today.** CCG: 13 modules, 150 H3 questions (149 plus the new Anti-Fraud Legislation
subsection), zero open-item markers. DD: CZ V2.0 structure preserved, blue-column-only population
confirmed across all 198 fields. WTC: CZ V2.0 + Global WTC baseline + Form Reference Guide sheet
all present and internally consistent. Report Specs: Spain 9-sheet format with 21-column Sheet 4,
confirmed for all 15. Payslip: 5 core Mercans-standard sheets confirmed present in all cases; the
mechanical check's rigid 5-sheet-only expectation was found to be stale against the file's own
by-design 7-8 sheet structure (intro/guide sheets plus a genuine Field Option reconciliation sheet,
itself independently cross-validated against the DD today) — overridden with documented reasoning,
not silently passed. **Score: PASS (6 direct, 1 justified override).**

### Check 9 — Composite key / Inter-field constraints
**Partially re-verified today.** m-1 (37 previously-undocumented composite-key fields) is fully
closed: 90 of 90 identifier fields (SIRET/SIREN/NIC/NIR/NTT-pattern) across all 15 specs now carry
composite-key documentation, verified by an independent re-scan after correction. Bidirectional
conditional-field documentation (the other half of this check) was spot-checked via the Alignment
Patch work (Sex and Contract Nature option-mapper cross-validation, 2 of many option mappers) but
not exhaustively re-run. **Score: PASS on composite keys (exhaustive); PASS on the 2 sampled
option mappers; not exhaustively re-verified beyond that.**

---

## What this session closed (summary)

| Item | Evidence |
|---|---|
| F-1 (264 DD↔Spec rows) | 264/264 resolved, 0 unresolved, 40/40 sample of pre-existing matches verified |
| F-2 (meal/NTIC BIK) | FR-075 to FR-078 in WTC, Payslip Unit Rate Details, Payslip Spec formula, and visual example, all cross-consistent |
| F-3 (SIPSI) | Confirmed consistent (Module 10, scope_manifest, WTC) |
| m-1 (composite keys) | 90/90 |
| m-2 (DD filename refs) | 8/8 operational files |
| m-3 (net-pay colour) | Reframed — France already conforms to the shared standard; not a France defect |
| SIR | Read in full for the first time; F27 found and corrected live in scope_manifest.json |
| CCG | Module 3 (heading-corruption bug found and fixed) and Module 12.1 (proven identical to Payslip, then re-synchronised) read in full; 15 further H3 questions sampled, zero errors; Anti-Fraud Legislation (Loi n° 2026-534) subsection added |
| WTC | 18 of 378 wage types (4.8%) sampled, zero errors, 2 figures independently confirmed against official sources |
| Data Dictionary | 198/198 fields mechanically audited, zero structural defects; 9 genuine new fields added with primary-source citations |
| Report Specs | 100% of 1,428 real data rows mechanically audited, zero structural defects |
| Alignment Patch | 2 of 6 responsibilities tested with concrete cross-file evidence |
| Stage 9 mechanical audit | Re-run against corrected state: 7/7 PASS |
| country_failure_log.md | 3 new failure patterns documented (F32-F34) so the reconciliation-method defect behind F-1 is caught automatically in future country builds |

## What remains genuinely open

- 132 of 150 CCG H3 questions were not independently read this session (sampling, not exhaustive audit)
- 360 of 378 WTC wage types were not independently re-verified this session
- Full CCG↔DD cross-check was not performed module-by-module for all 13 modules
- Bidirectional conditional-field documentation (second half of Check 9) was sampled (2 option mappers), not exhaustive
- Field-level content accuracy of the 15 Report Specs beyond the F-1/m-1 population was mechanically structure-checked, not individually fact-verified
- The country_failure_log.md top-of-document version header (v2.5) does not match the version tags used by its own newest entries (v2.9); flagged, not resolved — needs a decision from whoever owns that document's versioning convention

None of the above blocks handover. Each is a legitimate candidate for a future, separately-scoped
audit pass, not a defect discovered and left unaddressed.

## Sign-off recommendation

**READY FOR DEV TEAM.** All three original MAJOR findings and two of three MINOR findings are
closed with primary-source or mechanically-exhaustive evidence. The third MINOR finding (m-3) is
resolved by correcting the premise, not by further work. No FAIL condition exists in any of the 9
checks as re-verified or carried forward today.

---
*Generated 2026-09-02. Full session detail (research citations, verification commands, and
before/after states for every correction) exists in the France compliance working session log
of the same date.*
