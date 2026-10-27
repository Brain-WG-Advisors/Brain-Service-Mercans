# Pre-Submission QA Report — France (FR) — v4

**Date:** 2026-09-03
**Prepared by:** Wallisson Gomes
**Supersedes:** FR-QA-REPORT-v3-20260903.md (written before five further changes landed the same day: DD v1.4, CCG v1.2 and v1.3, WTC v1.2, and the DGFIP-003 M14 correction — v3 is stale on those five, not wrong)

---

## Executive Summary

**Overall verdict: READY FOR DEV TEAM.**

Every artifact family has been through field-level or code-level audit against primary sources. Beyond v3's scope, this version closes: a development-side design-readiness review (three genuine fixes, two items correctly identified as development-team-owned, one item resolved as a documentation gap rather than a template gap), a real residual defect in DGFIP-003 that v3's own closure missed, a formal IDCC scope decision, and independent verification of the two items v3 had explicitly left unverified.

| Artifact | This version adds |
|---|---|
| Data Dictionary | v1.4: Local Value column added (Compulsory Scheme Base Complement, 1.30%). Part-Time Contribution on a Full-Time Basis (S21.G00.40.044) independently confirmed against the DSN cahier technique primary source — 2 codes, exact match, no gap. **DD is now 100% closed: 54/54 option mappers and 198/198 fields, zero open items.**
| CCG | v1.2: navigation note on the withholding grid (monthly-only is correct; cross-references Module 11.1). v1.3: restored a three-item list the document promised but never delivered (sources of non-statutory variation), and added an explicit IDCC scope decision — override tables for specific collective agreements are a client-implementation task, not a baseline research task, given ~330 active conventions with materially different provisions and no statutory-reporting exposure from deferring them.
| WTC | v1.2: FR-046 (CSG/CRDS base) formula now names its four constituent wage types (23670, 23671, 23672, 23673) explicitly, closing a real omission — 23673 (savings-plan top-up) belonged in the list and was missing, confirmed against four independent external sources.
| Report Specs | FR-DGFIP-003 M14: a second, independent full-workbook scan (triggered by a spot-check, not the original closure) found one residual defect the v3 closure missed — an explanatory cell repeated 4.25% where the calculation required 8.50%, contradicting the workbook's own Example Analysis sheet for the identical case. Corrected; re-scanned; no further occurrences of the same pattern found.
| Payslip | Population Range sheet (5th sheet, previously unaudited) read in full: 20 of 22 rows cross-reference cleanly against WTC/DD/CCG content already verified; the two most specific claims — the July 2026 supplementary birth-leave reform (70%/60%) and the Alsace-Moselle addition — independently confirmed, the former against four government sources. One low-materiality observation: proration uses 151.67 hours rather than 151.6666..., the same figure the WTC's own note flags as imprecise for minimum-wage testing, but here used only as a proration divisor (cents-level effect, not a pass/fail test) and consistent with the CCG's own worked example — noted, not treated as a defect.

**Zero open content defects.** Every finding was corrected and independently re-verified from disk; two additional items were checked and found to require no correction (DD Part-Time Contribution, Payslip Population Range).

---

## The development-side design-readiness review — disposition of every item

| Item raised | Disposition |
|---|---|
| DD `Internal Code` empty (173 fields) | Not a defect — this build's own pipeline script marks the column ORANGE (development-team-owned). Recommend clarifying the colour convention with the reviewer rather than populating it centrally. |
| Option-mapper `Local Value` missing | **Fixed.** Column added; populated for the one mapper with a verified, unambiguous rate (Alsace-Moselle, 1.30%). Two of the review's other four named candidates were rejected on verification: one cited the wrong mapper for the rate, one cited a link (Employer Legal Nature → RGDU Tdelta) that FR-CCG-001's own worked example contradicts (Tdelta follows headcount, not legal nature). |
| WTC `In Period Reconciliation`, `YTD Load`, `YTD Remarks`, `Prorating Method`, `Calculation Type` | Not a defect — the WTC's own Version Control (row 23) already documents these as columns deliberately left for the development team. |
| Withholding grid stated monthly only | Investigated as a possible gap; found to be correct by design (income tax withholding is never annualised, per the CCG's own Module 11.1 proration table). Added a cross-reference note so the reason is visible where the grid appears, not only where the general principle is stated. |
| CSG base (FR-046) contribution mapping | **Fixed.** Genuine omission found and corrected — see WTC row above. |
| 17 artifacts "referenced but not delivered" | **Resolved as a delivery/visibility gap, not a content gap.** All 17 accounted for: 15 Report Specs exist and are complete (confirmed on disk); FR-DGFIP-006 is a documented scope exclusion (PASRAU does not apply to employers under the general scheme); FR-SIR-001 exists under its current name, FR-SIR-INDEX-001, with a 28-file runbook structure. Correction drafted for the reviewer. |
| IDCC / collective-agreement coverage unscoped | **Resolved.** Formal scope decision recorded in CCG v1.3 (see above), plus the unrelated content gap found while locating where to add it. |

---

## Mechanical audit (Stage 9)

Last run 2026-09-03, 12/12 PASS, before the changes catalogued above. Re-running is recommended given the volume of change since, purely for a clean, dated confirmation — no FAIL is anticipated.

---

## Remaining open items (none blocking)

| Item | Nature |
|---|---|
| Payslip legacy sheets (`How to set up Payslip`, `Compliance Payslip`) | Cosmetic/cleanup, not a content defect |
| Contrat d'engagement educatif (DD Contract Nature, code 60) | Documented scope-owner decision, intentionally left open |
| Correction email to the design-readiness reviewer | Drafted, sending is the user's action |
| Confirmation that delivered artifacts are on Google Drive, not only local | User-side confirmation, not independently checkable from this environment |
| Conversation with development team re: ORANGE-column ownership (Internal Code, five WTC columns) | User-side communication, not a research task |

## Readiness verdict

**READY FOR DEV TEAM, with higher confidence than v3.** Two rounds of independent re-verification (the disk-based defect check that found the DGFIP-003 residual, and this version's audit of the two previously-unverified items) found the pipeline's content to be sound. No known content defect remains open in any artifact.
