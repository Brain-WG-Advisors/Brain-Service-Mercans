# WTC - build log
Artifact: WTC | Country: US | Round: 1 | Built: 2026-11-03
Manifest: _pipeline/build-manifest.json (USD, minor units 2, tier T4, package 1.0)
Inputs: _research/WTC-global_baseline-facts.json, WTC-country_specific-facts.json, WTC-research-pack.md, scope_manifest.json, approved DD (US-DD-001 v1.0, 143 field names read), 20 approved Report Specs (read only), _research/precheck-next/PRECHECK.md.
Output: 02-wtc/US-WTC-001-v1.0.xlsx, built by 02-wtc/_build/build_wtc.py (re-runnable; C71 PASS). Sidecars: _research/WTC-crosswalk.json, _research/WTC-research-request.json, WTC-RQ-nn entries in _research/gaps.json (backup in 02-wtc/_build/_backup/gaps.json.bak), 02-wtc/_build/checks/wtc_recon.csv, _pipeline/WTC-bindings.csv.

## Precedent inspection (L1)
_CZ_Wage_Type_Catalogue_V2_0.xlsx opened with openpyxl: sheets Version Control, Wage Type Catalogue, Sick Leave Paid By Employer, Tax Credit; main sheet header row 1, columns A-T, freeze C1, data from row 2, autofilter A1:T590, 12 data validations (replaced for the new row range). Global_WTC_V1_0.xlsx: one sheet, 3 columns, rows 2-301 = 300 codes (240 earning, 54 deduction, 5 contribution, 1 rate); all 300 are present, codes unchanged (C12 lint). Output sheets: Version Control, Wage Type Catalogue, Sick Leave Paid By Employer, Tax Credit, Global WTC Coverage, Form Reference Guide.
Header row: Q expanded to Q1-Q5 (OASDI, Medicare, FUTA, SUI, State programmes), R Subject to Pension, YTD Load, YTD Remarks, then five added columns (Subject to State Income Tax, Subject to Local Income Tax, Reporting Code, Legal Basis, Tax Code Official Source). 29 columns A-AC. Deviation from the 20-column contract (A-T): 9 added or expanded columns (Q split into Q1-Q5 = 4 added; State and Local income tax, Reporting Code, Legal Basis, Tax Code Official Source = 5 added); precedent FR 24 columns, CO 28 columns.

## Result
533 rows: 300 global + 233 country additions (US-001 to US-233; federal tax, bases, flags, fringe, reporting, garnishments; 42 State income tax rows, 51 SUI employer rows, 3 SUI employee rows, State programme, levy and local rows). 1,272 [[FACT:]] tags. Tax code legend: US-TX-01..11 and US-NA, defined on the Global WTC Coverage sheet with official source (register rows).

## Deviations and decisions
- Orange columns: Formula, Calculation Type, Prorating, Ignore If 0, Enforce, In Period Reconciliation, YTD Load, YTD Remarks left empty. A and D are populated (code and the mandatory explanation, as in the France precedent). Accumulator needs are written in column D and carried by the Subject-to flags.
- Column R is NA on every row (no statutory pension contribution at payroll besides OASDI = Q1).
- Local name column holds the English name (official and payroll language is English, US-OWN-006).
- Global 21900 (Custom Social Security employee) is configured as OASDI employee tax; global stock option codes 62890/62990/62991/62993/62994 carry the equity cases.
- Family anchors carry the figures; followers point to the anchor (no repeated tagged boilerplate).
- Out of scope: backup withholding and Form 1099-NEC (US-OWN-008); no row.
- Period-aware: every key renders all its dated values (ga.sui.new_employer.rate.contribution 2026 and 2027; ma.pfml.* 2026 and 2027; fed.fica.oasdi.wage_base 2026 and 2027).
- Code scheme US-nnn collides with the C49 pattern for form ids such as KW-100 (see QA items).

## Gaps (neutral cell wording + request + gaps.json)
75 distinct gaps, none blocking: WTC-RQ-01..09 (builder: allowance exclusions, advance/benefit-plan treatment, Roth and W-2 code table, employer plan contributions, LTD/sick pay, pension payments, SUI/programme wage definition by family, reporting code table, Wyoming fund) and WTC-RQ-20..85 (one per open item of the facts, e.g. DC SIT method WTC-RQ-25 and UT Pub 14 effective date WTC-RQ-42, both flagged blocking in the facts; written as not configured).

## Precheck re-points (lesson 5)
35 used facts carry `_figure_located`, 68 flags `_precheck_unmatched` (list: 02-wtc/_build/checks/precheck_used.txt). Quotes in context read from the note for the figure-bearing ones (mn.paid_leave.total.rate 0.88, oh.sit.method 2.99, or.sit.method 4.75, wv two-earner 18,750, mt 16,100, ny rsf 0.075, pittsburgh, DOL credit reductions, futa net). Token-only (word, form id, date) ones were NOT confirmed in context and need QA: al.sit.certificate, ar.sit.low_income_tables, id.sit.method, in.local.county_lit.rule, la.sit.nonresident.threshold, nj.sit.method, nj.base.hsa.git, ri.base.401k_125.ui_tdi, wa.pfml.base.tips, sc.sit.method, va.pfml.contributions.start, special_population.wa_cares.niv_exempt, fed.equity.rsu.fica_timing, fed.fit.extra_pay_period.rule, oh municipal rate table. co.famli.employee.rate / employer.rate: the located snippet is a page number ("43"), not the figure: unconfirmed.

## Reconciliation (checks/wtc_recon.csv)
RSPEC -> WTC: 137 payroll-result and correction-register rows mapped, 0 unmapped. WTC -> DD: every listed input exists in the approved DD (486 links). DD -> WTC: of the DD elements without a spec consumer, 11 are consumed here (W-4 steps and exempt, state certificate, allowances, transport worker type, military spouse, vacation forfeiture ...); 1 exception: Employee primary language (notice template, consumed by the SIR, not a wage type).

## Checks
| Check | Result |
|---|---|
| C12 structure (wtc_lint) | 0 problems; 6 sheets in order; 300 global codes; no dev column filled; all flags in domain |
| C29 (shared v2.12 HARD list and X-run, own scan of every cell) | 0 |
| C30, WORD/PATH, FRAC/PCT/UNIT | 0 / 0 / 0 |
| C46 period-aware | 1,272 tags, 0 mismatches, 0 missing keys, 0 unbound |
| C46 shared (package-wide) | FAIL: known limitation (multi-period keys, CCG tags); WTC lint 0 |
| C42, C43 shared | PASS |
| C48 | PASS vacuously (0 reporting codes: no authority code table; WTC-RQ-08) |
| C49 | FAIL 1: CCG table cell cites form id KW-100, matches the US-nnn pattern (false positive, CCG not edited) |
| C50, C70 | PASS (533 wage types; 0 problems) |
| C71 | PASS (rebuilt workbook identical) |
| Excel open (open_check.ps1) | OK |
| validate_contract --all | PASS 91 files |

## Accuracy
About 85%: structure and every figure bound to facts; the rest limited by the gaps above and by token-only precheck re-points. Closing it needs the facts for the allowance exclusions, the W-2 code table and the 2027 values.


## Round 2 fix (2026-11-04; review r1 batch items 2, 4, 6, 8, 10, 11, 13-17; facts R2-FACTS-READY.md STATUS: COMPLETE)
Backup before the change: 02-wtc/_build/_backup/r1fix-2026-11-03/ (workbook, crosswalk). One rebuild from the current facts (build_wtc.py).
| Item | Change |
|---|---|
| 2/17 | Regenerated from the R1 + R2 facts; C46 period-aware 0 mismatches, 0 missing, 0 unbound (1,266 tags); C71 PASS |
| 4 | Global WTC Coverage!A3 defines class 1 (reversal deduction: flags of the reversed earning, Yes = the signed amount reduces the base) and class 2 (salary reduction / pre-tax: No = removed before the tax); the class is stated in column D of the reversal rows, the 401(k)/403(b)/457(b)/SIMPLE rows and the health plan row |
| 6 | 62901: O/P = Yes-No (flags of the bonus family), D points to anchor 62200 |
| 8 | Column B = Global_WTC_V1_0 description verbatim for the 300 codes (202 restored); the US disambiguation stays in column C and D. diff_wtc_baseline: MISSING 0, RENAMED 0 |
| 10 | US-005 (D306, AB306) cites US-FEDR2-003 and US-FEDR2-004 |
| 11 | US-043: T/U = Yes-No; D names the WA PFML exclusion (wa.pfml.base.tips) |
| 13 | wtc_recon.csv reason: notice template input (NY LL 195.1, CO PSL notice) per DD; not a wage-type input. Ledger line 94: WTC side closed, open for SIR/PSL |
| 14 | Column count corrected above (29 A-AC, deviation listed) |
| 15 | C49 FAIL 1 is a false positive: KW-100 is the Kansas withholding guide form id (US-KSS5-001), not a wage-type code; the WTC is not changed. Needs validation_exemptions.C49 by the owner or a {CODE}- prefix in the check |
| 16 | gaps.json and the request file: WTC-RQ-25 (DC) blocking=true with _wtc_impact 'none: catalogue carries no method'; WTC-RQ-43 (UT effective date, was RQ-42; ids are allocated in order of use) blocking=true, 'D412 dating'. Named limitations for the QA report and the handover |
| 1 | Crosswalk code_table = 02-wtc/_build/checks/US-W2-box12-codes.json, derived from the IRS table 00-official-sources/code-tables/US-W2-box12.json (source file not edited; its codes are a list of objects, the check needs code -> validity). reporting_codes filled for 25 rows (24 distinct codes) from the column AA text; WTC-RQ-08 closed (no GAP written); WTC-RQ-03 reduced to the tax treatment of the Roth, 408(k)(6) and 501(c)(18)(D) deferrals, the code definitions are tagged from fed.w2.box12.code.* |
| R2 facts | 5: 62110 and US-045 bind fed.obbba.overtime_deduction.level; 7: advance rows 62103/62403/62503/62523/62563 lose 'Same tax treatment' and print the gap for fed.wages.advance_of_wages.classification; 3: UT prints the 2026-04-01 values only plus the gap for ut.sit.schedule.before_2026_04_01; 9: bindings follow the new register ids; ak/il/mo st_louis x2 printed as 'Not configured in this release [[GAP:WTC-RQ-nn]]'; ma.pfml x2 (RQ-10), ma.sui table (RQ-11), fed.ccpa.protected_weekly (RQ-12), fed.iwo.priority (RQ-13), fed.equity resident (RQ-14), fed.fit.nra.bik (RQ-15) printed as gaps with gaps.json entries; rspec.fed.w2.box_map stays bound (39 of 39 numbers located, also id US-FEDS5-032) |
Cell diff vs backup: Global WTC Coverage A3, D359, D420 (items 4, 6, 11 summaries); Wage Type Catalogue B x202 (8); D x164 (4, 5, 6, 7, 10, 11, R2 facts, R1 rewording); AB x24 (bindings, 10); O283/P283 (6); T344/U344 (11). No other cell changed.
Checks: wtc_lint C12 0, C29 0, WORD 0, C30 0, FRAC/PCT/UNIT 0, C46 period-aware 0, unbound 0; C42/C43 PASS; C46 shared FAIL (known package-wide limit); C70 PASS; C71 PASS; baseline BASELINE INTACT (RENAMED 0); Excel open_check 0 not clean; validate_contract --all PASS (92 files).
Open: C48 1 problem: US-051 code TA is valid from 2026-07-04 (IRS table), not the whole of 2026; needs the owner ruling or validation_exemptions.C48. C50 1 problem: US-126 (GA SUI, employer) quotes the Georgia fact ga.sui.base.section125 verbatim ('employer and employee premiums'), which the check reads as both sides; value is the authority wording, the row side is ER (source hunter to reword the fact). C49 KW-100 (item 15).
md5_final: 117c230d396f617aa828986f35bcf1cf  02-wtc/US-WTC-001-v1.0.xlsx

## Round 3 fix (2026-11-04; review r2)
Backup: 02-wtc/_build/_backup/r2fix-2026-11-04/. Cause of the stale ids: periods() took the first fact per key and the CCG annex facts files (old register ids) came before the WTC files. periods() now takes the WTC facts files first, so every tag, WTC-bindings.csv, column AB and AC follow the current register_id (+ also ids). US-051: column D and AA carry 'effective from 2026-07-04' (facts dated 2026-07-04). Cell diff vs backup: D x23, AA352, AB x11, AC x99 (tax code source), Global WTC Coverage D14/D17 (legend source). Bindings: 1,257, 0 differ from the facts' ids (_bind_check.py); C46 period-aware 0; C70 PASS; C71 PASS; baseline INTACT; validate_contract --all PASS (93). The text check of local copies (F44) is run by the auditor; no script in the toolkit. C48 TA stays a checker limit (exemption by the owner).
md5_final: dccad368fbcea716ed1637ce88908414  02-wtc/US-WTC-001-v1.0.xlsx
