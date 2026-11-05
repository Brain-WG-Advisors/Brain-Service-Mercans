# Annex WI: Wisconsin


Jurisdiction annex of the United States Country Configuration Guide (US-CCG-001). Layer classification: **T3 - state withholding; local layer absent or piggybacked on the state return**.

The federal layer (federal income tax withholding, FICA, FUTA, Forms W-2, 941 and 940) and the multistate rules (residence and work-location sourcing, reciprocity mechanics) are in the federal reference and the multistate reference and are not repeated here. Independent contractors and Form 1099-NEC reporting are out of scope (owner instruction of 2026-10-29) [US-OWN-008]. Payslip language: English; second-language duties attach to notices and posters only (US-OWN-006).

Every value in this annex is bound to a verified fact and carries its legal-basis register id. A value that changes during the year is shown with its effective dates. A point marked as a research gap has not been closed by the research; it is not filled with an estimate.

## WI.1 Employment and labour code

- **Minimum wage (Wis. Stat. 104.035) [US-WIS5-001, US-WIS5-002]:** 7.25 USD per hour, minors included; opportunity employees (young workers in their first period of employment) 5.90 USD. No increase scheduled for 2026 or 2027.
- **Local minimum wage:** barred (104.001(2)): True [US-WIS5-001].
- **Tipped employees [US-WIS5-002]:** cash wage 2.33 USD per hour (lower for opportunity employees); the tip credit needs a tip declaration signed by the employee every pay period and records showing tips plus wages reach the minimum each week (DWD 272.03(2)(b)).
- **Meal and lodging credits (104.035(1)(b)):** lodging 58 USD per week (daily and meal credits per the statute) [US-WIS5-001].
- **Overtime (DWD 274.03) [US-WIS5-003]:** 1.5 times the regular rate over 40 hours per week; no daily overtime; exemptions read consistently with the FLSA; household domestic service outside the chapter.
- **Pay frequency (109.03(1)) [US-WIS5-004]:** at least monthly, wages to a day max 31 days before payment; logging and farm labour at least quarterly; CBA and school-year exceptions.
- **Method of payment [US-WIS5-005]:** the employer may require direct deposit at no cost to the employee; a stub is still due. No paycard rule located (open point below).

**Parameters (labour code and pay rules)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `wi.minwage.hourly` | 7.25 | USD | from 2009-07-24 | US-WIS5-001 | 104.035; minors too; no 2026/2027 change |
| `wi.labour.minwage.opportunity.hourly` | 5.90 | USD | from 2009-07-24 | US-WIS5-001 | under 20, first 90 consecutive days |
| `wi.local_mandates.preempted` | True |  | from 2009-07-24 | US-WIS5-001 | 104.001(2) |
| `wi.minwage.tipped.cash_wage` | 2.33 | USD | from 2009-07-24 | US-WIS5-002 |  |
| `wi.labour.lodging_credit.weekly` | 58 | USD | from 2009-07-24 | US-WIS5-001 | 8.30/day; meals 87/week or 4.15/meal |
| `wi.overtime.weekly_threshold_hours` | 40 | hours | from 2003-12-01 | US-WIS5-003 | no daily OT; household domestic outside chapter |
| `wi.overtime.premium.multiplier` | 1.5 | ratio | from 2003-12-01 | US-WIL-001 |  |
| `wi.pay_frequency.rule` | at least monthly, wages to a day max 31 days before payment |  | from 2026-01-01 | US-WIS5-004 | 109.03(1); logging/farm quarterly |
| `wi.labour.direct_deposit.employer_may_require` | True |  | from 2026-01-01 | US-WIS5-005 | at no cost; stub still due (DWD page A.3) |

**Open research points**

- Not configured in this release (open gap RQ-386): No WI paycard rule located.

## WI.2 Income tax withholding

- **Method [US-WIP51-001, US-WIS5-011, US-WIS5-010]:** W-166 (1/26) wage-bracket tables or alternate formula; any other method needs DOR permission (71.64(1)). DOR Withholding Tax Update 2026-1 states no plan to change the withholding rates for 2026 [US-WIS5-016].
- **Withholding schedule (W-166) is not the statutory assessment schedule.** The WTC uses W-166 only.

| Annual wages after deductions | Withholding rate | Register id |
|---|---|---|
| up to 12,760 USD | 3.54 % | US-WIP51-001 |
| up to 25,520 USD | 4.65 % | US-WIP51-001 |
| up to 280,950 USD | 5.3 % | US-WIP51-001 |
| above | 7.65 % | US-WIP51-001 |

  The statutory assessment rates (71.06(1r), tax years after 2024, brackets indexed from 2026) are 3.50;4.40;5.30;7.65 (%) [US-WIS5-010]; they apply at assessment and are never moved into the withholding engine. The 2026 indexed assessment brackets are not needed for withholding (open point below).
- **Alternate formula [US-WIP51-001]:** annualise; subtract the standard deduction (single 6702 USD, married 9461 USD, each phased out above statutory wage levels) and 400 USD per exemption; apply the schedule; divide by the pay periods.
- **Oracle (W-166 worked examples, re-derived):** example 1 7.59 USD; example 2 14.34 USD; example 3 22.08 USD; the guide rounds the bracket portion separately, so only the annual intermediate differs by a cent [US-WIS5-011]. Recomputation in Module 12.
- **Supplemental wages [US-WIP51-001]:** aggregate, or a flat rate by estimated annual gross: 3.54 (0-12,760); 4.65 (to 25,520); 5.30 (to 280,950); 7.65 (above) by estimated annual gross.
- **Rounding:** none stated [US-WIS5-011].
- **Certificate [US-WIS5-011, US-WIS5-016]:** WT-4; federal W-4 not accepted; none = zero exemptions; exempt claims renewed yearly; copies to DOR above the statutory thresholds; DOR lock-in letters bind the employer. WT-4 edition: open point below.
- **Residents and nonresidents (71.63(2)) [US-WIS5-010, US-WIS5-011]:** residents withheld on all wages; nonresidents only on wages for Wisconsin work, with exceptions for interstate carriers, reciprocity, air carriers, military spouses and expected Wisconsin earnings below 1500 USD (catch-up once exceeded). Reciprocity: IL;IN;KY;MI (W-220); MN arrangement [US-MULTI-006].
- **Local income tax:** none (exists: False) [US-WIR3-001].
- **Resident and nonresident matrix.**

| Income type | Wisconsin resident | Nonresident |
|---|---|---|
| Regular salary | W-166 tables or formula on all wages | W-166 on wages for Wisconsin work, unless reciprocity (W-220) or another exception applies |
| Bonus / supplemental | Aggregate or flat rate by estimated annual gross | Same, Wisconsin share |
| Pensions | Not wages; withheld only on written request | Same |
| Benefits in kind | Federal treatment with the box-16 differences in Section 8 | Same, Wisconsin share |
| Wages paid after death | Not subject to Wisconsin withholding | Same |

**Parameters (income tax withholding (state and local))**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `wi.wh.method` | W-166 (1/26) wage-bracket tables or alternate formula |  | from 2022-01-01 | US-WIS5-011 | other methods need DOR permission (71.64(1)); rates unchanged for 2026 (US-WIS5-016) |
| `wi.pit.statutory.rates` | 3.50;4.40;5.30;7.65 |  | from 2025-01-01 | US-WIS5-010 | ASSESSMENT brackets 14,680/50,480/323,290 single (71.06(1r)); CPI-indexed from 2026 - never in the WTC |
| `wi.pit.oracle.example_1.withholding` | 7.59 | USD | from 2022-01-01 | US-WIS5-011 | W-166 weekly 350 single 1 exemption |
| `wi.pit.oracle.example_2.withholding` | 14.34 | USD | from 2022-01-01 | US-WIS5-011 | weekly 500 single 3 exemptions |
| `wi.pit.oracle.example_3.withholding` | 22.08 | USD | from 2022-01-01 | US-WIS5-011 | biweekly 1,000 married 3 exemptions; annual 745.79/574.17 vs guide 745.78/574.16 (1-cent residual in annual only) |
| `wi.pit.rounding` | none stated |  | from 2026-01-01 | US-WIS5-011 |  |
| `wi.wh.certificate` | WT-4; federal W-4 not accepted; none = zero exemptions |  | from 2026-01-01 | US-WIS5-011 | exempt renewed by April 30 |
| `wi.pit.nonresident.de_minimis` | 1500 | USD | from 2026-01-01 | US-WIS5-011 | expected WI earnings under 1,500 (catch-up once exceeded) |
| `wi.reciprocity.states` | IL;IN;KY;MI (W-220); MN arrangement |  | from 2026-01-01 | US-MULTI-006 |  |
| `wi.local_wage_tax.exists` | False |  | from 2026-01-01 | US-WIR3-001 |  |
| `wi.pit.wh.bracket.1.ceiling` | 12,760 | USD | from 2022-01-01 | US-WIP51-001 | 3.54% |
| `wi.pit.wh.bracket.1.rate` | 3.54 | % | from 2022-01-01 | US-WIP51-001 |  |
| `wi.pit.wh.bracket.2.ceiling` | 25,520 | USD | from 2022-01-01 | US-WIP51-001 | 4.65%; cumulative 451.70 |
| `wi.pit.wh.bracket.2.rate` | 4.65 | % | from 2022-01-01 | US-WIP51-001 |  |
| `wi.pit.wh.bracket.3.ceiling` | 280,950 | USD | from 2022-01-01 | US-WIP51-001 | 5.30%; cumulative 1,045.04 |
| `wi.pit.wh.bracket.3.rate` | 5.3 | % | from 2022-01-01 | US-WIP51-001 |  |
| `wi.pit.wh.bracket.4.rate` | 7.65 | % | from 2022-01-01 | US-WIP51-001 | cumulative 14,582.83 |
| `wi.pit.wh.std_deduction.single` | 6702 | USD | from 2022-01-01 | US-WIP51-001 | below 17,780; reduced 12% of excess; 0 at 73,630 |
| `wi.pit.wh.std_deduction.married` | 9461 | USD | from 2022-01-01 | US-WIP51-001 | below 25,727; reduced 20%; 0 at 73,032 |
| `wi.pit.wh.exemption` | 400 | USD | from 2022-01-01 | US-WIP51-001 | each |
| `wi.pit.supplemental.flat_rates` | 3.54 (0-12,760); 4.65 (to 25,520); 5.30 (to 280,950); 7.65 (above) by estimated annual gross |  | from 2022-01-01 | US-WIP51-001 | or aggregate |

**Open research points**

- Not configured in this release (open gap RQ-382): Not established from an official source.
- Not configured in this release (open gap RQ-387): 2026 CPI-indexed assessment brackets not read (assessment only).

## WI.2b Non-resident regime and reciprocity

The non-resident and reciprocity rules of this jurisdiction are written in WI.2.

## WI.2c Local wage taxes

The local wage taxes of this jurisdiction, where any exist, are written in WI.2.

## WI.3 Social insurance: unemployment, disability, paid leave and payroll levies

- **Unemployment insurance (DWD) [US-WIS5-014, US-WIS5-019].** Taxable wage base 14,000 USD, fixed in statute and not indexed. Rate schedule D for 2026 and 2027 (total rate = basic + solvency), up to 12 %. New employer 3.05 % below the large-payroll threshold and 3.25 % at or above it (construction rates differ), for the first years [US-WIR3-002]. Annual increase cap (108.18(5)).
- **Employee contribution:** 0 % [US-WIR3-003].
- **SDI, TDI, PFML:** none (exists: False) [US-WIR3-004]; Wisconsin FMLA leave is unpaid (103.10(5)(a)) [US-WIS5-006]. Only the solvency component as an employer levy [US-WIP7-001].

**Parameters (social insurance and payroll levies)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `wi.sui.wage_base` | 14,000 | USD | from 2013-01-01 | US-WIS5-014 | fixed in statute, not indexed; second authority US-WIS5-019 |
| `wi.ui.schedule.in_effect` | D |  | 2026-01-01 to 2027-12-31 | US-WIS5-019 | 2026 and 2027 |
| `wi.sui.employer.rate.max` | 12 | % | 2026-01-01 to 2027-12-31 | US-WIS5-019 | payroll <500,000: 0.00-12.00; >=500,000: 0.05-12.00 |
| `wi.ui.rate.new_employer.small` | 3.05 | % | 2026-01-01 to 2027-12-31 | US-WIS5-019 | <500,000 payroll (2.50+0.55); construction 2.50 |
| `wi.ui.rate.new_employer.large` | 3.25 | % | 2026-01-01 to 2027-12-31 | US-WIS5-019 | >=500,000 (2.50+0.75); construction 2.70 |
| `wi.sui.employee.rate` | 0 | % | from 2026-03-16 | US-WIR3-003 |  |
| `wi.sdi_pfml.exists` | False |  | from 2024-03-01 | US-WIR3-004 | WFMLA unpaid (US-WIS5-006) |

## WI.4 Pay statement

- **Content (103.457; DWD 272.10) [US-WIP52-001, US-WIS5-002]:** on the paycheck, envelope or accompanying paper: hours worked, rate, amount and reason for each deduction; a coding system allowed. Electronic stub allowed if printable free; required even with direct deposit [US-WIS5-005].
- **Retention:** payroll records at least 3 years (DWD 272.11, 274.06) [US-WIS5-002, US-WIS5-003]. No payslip language rule [US-WIL-002].

**Parameters (payslip statute and payroll records)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `wi.records.retention_years` | 3 | years | from 2009-07-24 | US-WIS5-002 | DWD 272.11 |
| `wi.payslip.items` | hours worked, rate, amount and reason for each deduction |  | from 2026-01-01 | US-WIP52-001 | 103.457; DWD 272.10; electronic if printable free |

## WI.5 Statutory reporting

- **WT-6 withholding deposit report [US-WIS5-011, US-WIS5-016]:** DOR assigns the frequency each November (no published thresholds); zero reports required; electronic only unless waived.
- **WT-7 annual reconciliation:** due January 31 (TY2026: February 1, 2027), rejected until all WT-6s are filed.
- **State W-2 [US-WIS5-012, US-WIS5-015]:** same due date; electronic filing at 10 or more W-2s; SSA EFW2 with RS record; MTA keying, upload or sFTP.
- **Quarterly UI contribution and wage report [US-WIS5-013, US-WIS5-014, US-WIS5-020]:** due end of month after quarter, filed even at a zero rate; electronic filing mandatory above the employee threshold; DWD stops mailing reports in 2027 and opens a new employer portal in fall 2026.
- **New hire [US-WIS5-013]:** within 20 days of the start date; multistate employers may elect one state.
- **Registration and agents:** one withholding account per legal entity; payroll service providers register and test with DOR; POA A-222 (DOR) and UCT-8291-E (UI) [US-WIS5-011, US-WIS5-016, US-WIP52-003, US-WIP51-002].

**Parameters (statutory reporting)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `wi.report.wt7.due` | January 31 (TY2026: February 1, 2027) |  | from 2026-01-01 | US-WIS5-016 | WT-6 frequency assigned by DOR |
| `wi.report.w2.efile_threshold` | 10 |  | from 2026-01-01 | US-WIS5-012 | EFW2 with RS record, state code 55 |
| `wi.report.ui.quarterly_due` | end of month after quarter |  | from 2026-03-16 | US-WIS5-013 | electronic at 25+ employees |
| `wi.newhire.report_days` | 20 | days | from 2026-03-16 | US-WIS5-013 | incl. DOB |

## WI.6 Leave

- **Paid sick leave:** no state statute (exists: False); local mandates preempted (103.10(1m), 103.12) [US-WIS5-006].
- **Wisconsin FMLA (103.10) [US-WIS5-006]:** employers with 50 or more permanent employees; service tests; unpaid, with substitution of paid leave. Bone marrow and organ donation leave unpaid (103.11). Vacation and holiday pay not mandated [US-WIS5-005].

**Parameters (leave)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `wi.leave.sick.state_statute.exists` | False |  | from 2026-01-01 | US-WIS5-006 | locals preempted |
| `wi.leave.wfmla.employer_threshold` | 50 |  | from 2026-01-01 | US-WIS5-006 | unpaid; 52 weeks + 1,000 hours |

## WI.7 Termination and final pay

- **Final pay (109.03(2)) [US-WIS5-004]:** earlier of next regular payday or 31-day limit (quit and discharge); commission sales agents and fixed-term contracts excepted. Death of an employee: wages payable on demand to the family (109.03(3)).
- **Accrued vacation:** payable if written policy with no written forfeiture clause [US-WIS5-005].
- **Plant closing (109.07):** 60 days' notice [US-WIS5-004]. UI separation forms only on DWD request; poster UCB-7-P [US-WIS5-013].

**Parameters (termination)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `wi.final_pay.rule` | earlier of next regular payday or 31-day limit (quit and discharge) |  | from 2026-01-01 | US-WIS5-004 | 109.03(2) |
| `wi.term.vacation.payout` | payable if written policy with no written forfeiture clause |  | from 2026-01-01 | US-WIS5-005 | DWD page |
| `wi.term.plant_closing.notice_days` | 60 | days | from 2026-01-01 | US-WIS5-004 | 109.07, 50+ in WI |

## WI.8 Benefits in kind and taxable wages

- **Conformity:** Wisconsin generally conforms to the IRC; W-166 defers to Pub 15 and 15-A; HSAs follow federal rules [US-WIS5-011]. Individual IRC conformity paragraph not isolated (open point below).
- **2026 box-16 differences (Wisconsin wages higher than federal) [US-WIS5-016]:** IRC 112, 127, 128, 129 (above WI exemption), 132 moving/bicycle.
- **Transit and parking:** 340 USD per month each for 2026, federal and Wisconsin alike.

**Parameters (benefits in kind and the taxable base)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `wi.bik.wi.box16_differences` | IRC 112, 127, 128, 129 (above WI exemption), 132 moving/bicycle |  | from 2026-01-01 | US-WIS5-016 | WI wages higher than federal |
| `wi.bik.transit_parking.monthly` | 340 | USD | 2026-01-01 to 2026-12-31 | US-WIS5-016 | federal and WI |

**Open research points**

- Not configured in this release (open gap RQ-384): Individual IRC conformity paragraph 71.01(6) not isolated.

## WI.9 Deductions and garnishments

- **Deductions for damage, loss or faulty work (103.455):** written authorisation, joint determination or court finding; double damages for violations [US-WIS5-007].
- **Creditor garnishment (812.34) [US-WIS5-008]:** at most 20 % of disposable earnings (stricter than the CCPA); total exemption below the poverty line or with need-based aid; garnishee fee 15 USD plus a small fee per later payment, deducted from the creditor's share.
- **Child support IWO (767.75) [US-WIS5-009]:** remit within 5 days of payday; CCPA cap; the employer may keep up to 3 USD per payment; the IWO has priority over other state-law process. DOR wage attachment: open point below.

**Parameters (deductions and garnishments)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `wi.garn.creditor.max_percent` | 20 | % | from 2026-01-01 | US-WIS5-008 | 812.34; stricter than CCPA; poverty-line protection |
| `wi.garn.garnishee_fee` | 15 | USD | from 2026-01-01 | US-WIS5-008 | plus 3 per payment after first, from creditor share |
| `wi.garn.iwo.remit_days` | 5 | days | from 2026-01-01 | US-WIS5-009 | employer may keep up to 3 per payment |
| `wi.garn.iwo.employer_fee.per_payment` | 3 | USD | from 2026-01-01 | US-WIS5-009 |  |

**Open research points**

- Not configured in this release (open gap RQ-383): DOR wage attachment percentage and priority not read.

## WI.10 Collective agreements and prevailing wage

Prevailing wage (public works) is an optional informational flag [US-OWN-009]: this guide documents prevailing-wage laws, thresholds and certified-payroll duties as an overlay, and the payroll build does not produce certified payroll reports.

- **No current prevailing-wage regime** (exists: False) [US-WIP52-002]; the repealing acts were not read (open point below). CBAs may set a different pay frequency (109.03(1)(a)) [US-WIS5-004].

**Parameters (collective agreements and prevailing wage)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `wi.prevailing_wage.exists` | False |  | from 2026-01-01 | US-WIP52-002 | ch. 103 text has no prevailing wage; repealing act not read |

**Open research points**

- Not configured in this release (open gap RQ-385): Repealing acts (2017 Act 59; 2015 Act 55) not read.

## WI.11 Indexation

- **Indexed:** the statutory assessment brackets (CPI-U) from 2026 [US-WIS5-010].
- **Not indexed:** minimum wage; UI wage base [US-WIS5-014]; the withholding tables (revised by publication only; no change for 2026) [US-WIS5-016].

## WI.12 Payroll data protection and records

- **Breach notification (134.98) [US-WIS5-018]:** within a reasonable time, at most 45 days. No statute restricting SSNs on pay statements found; SSN truncation allowed on employee copies of W-2 and 1099 but not on copies filed with DOR [US-WIS5-012, US-WIS5-011]. Personnel file inspection (103.13) [US-WIS5-007].

**Parameters (payroll data protection)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `wi.data.breach.notice_days` | 45 | days | from 2026-01-01 | US-WIS5-018 |  |

## WI.13 Live legal change

- **DOR Withholding Tax Update 2026-1 (2026-10-30):** no withholding rate change; tax year 2026 due dates; new box-16 differences [US-WIS5-016].
- **Assessment-level changes** (bracket expansion, retirement subtraction) for tax years after 2024 [US-WIS5-010].
- **DWD:** Schedule D continues in 2027; mailing ends in 2027; new portal fall 2026 [US-WIS5-020]. 2025 Acts 145 and 144: no withholding or contribution effect [US-WIS5-021].

## WI.14 Authority worked examples (oracle values)

No authority worked example is reproduced in this annex; recomputed withholding examples are in Module 12.

## WI.15 Special populations

| Population | Wisconsin rule | Register id |
|---|---|---|
| Domestic / household | Not wages for Wisconsin withholding (71.63(6)(c)); W-2 still reported; UI above a quarterly cash test; outside DWD 274 | US-WIS5-010, US-WIS5-011, US-WIS5-013, US-WIS5-003 |
| Agricultural (incl. H-2A) | Not wages for withholding (71.63(6)(b)), voluntary by agreement; UI coverage tests; quarterly pay allowed | US-WIS5-016, US-WIS5-013, US-WIS5-004 |
| Minors | Work permit under 16 (103.70); minimum and opportunity wages per Section 1 | US-WIS5-022, US-WIS5-001 |
| Tipped | Cash wage and tip declaration per Section 1 | US-WIS5-002 |
| Clergy / religious | Ministers and religious orders excluded from withholding wages (71.63(6)(f)) | US-WIS5-010 |
| Students | UI exclusions for work-study, student nurses and interns, short camp employment | US-WIS5-023 |
| Nonresident aliens | UI exclusion for certain visa classes; general nonresident withholding rule | US-WIS5-023, US-WIS5-011 |
| Statutory employees | Direct sellers and real-estate agents are not employees for withholding; corporate officers are | US-WIS5-010, US-WIS5-023 |
| Government employees | Employees for withholding; separate public-employee coverage rules (DWD 274.08) | US-WIS5-010, US-WIS5-003 |
| Nonresidents / multistate | Reciprocity and de minimis per Section 2; military spouse W-221 | US-MULTI-006, US-WIS5-011 |
| Pensioners | Withheld only on written request | US-WIS5-016 |
| Nonresident entertainers | Contract-price withholding unless bonded (WT-11 / WT-12) | US-WIS5-016, US-WIS5-011 |

## WI.16 Language

No language rule for employee documents is written for this jurisdiction in this annex.

## WI.S Sources

Authorities:

- Decided under the owner's delegation: US-OWN-006
- Owner (Wallisson Gomes): US-OWN-008
- State of Wisconsin, Office of the Governor: US-WIS5-021
- US DOL Women's Bureau: US-WIR3-004
- WI official authority: US-WIP7-001
- Wisconsin DOR: US-MULTI-006
- Wisconsin DWD (published by LRB): US-WIS5-002, US-WIS5-003
- Wisconsin DWD Equal Rights Division: US-WIS5-005
- Wisconsin DWD Unemployment Insurance Division: US-WIR3-002, US-WIR3-003, US-WIS5-013, US-WIS5-019, US-WIS5-020, US-WIS5-023
- Wisconsin Department of Revenue: US-WIP51-001, US-WIP52-003, US-WIS5-011, US-WIS5-012, US-WIS5-015, US-WIS5-016
- Wisconsin Department of Revenue, Division of State and Local Finance: US-WIR3-001
- Wisconsin Department of Workforce Development: US-WIP51-002
- Wisconsin Legislature: US-WIP52-002
- Wisconsin Legislature (LRB): US-WIS5-001, US-WIS5-004, US-WIS5-006, US-WIS5-007, US-WIS5-008, US-WIS5-009, US-WIS5-010, US-WIS5-014, US-WIS5-018, US-WIS5-022
- Wisconsin Legislature (published 10-1-26): US-WIL-001
- Wisconsin Legislature / DWD: US-WIP52-001
- Wisconsin Legislature; DWD: US-WIL-002


## Fact index

Every value above with its key, effective period and register id.

| Key | Value | Effective | Register id |
|---|---|---|---|
| `wi.bik.transit_parking.monthly` | 340 | from 2026-01-01 to 2026-12-31 | US-WIS5-016 |
| `wi.bik.wi.box16_differences` | IRC 112, 127, 128, 129 (above WI exemption), 132 moving/bicycle | from 2026-01-01 | US-WIS5-016 |
| `wi.data.breach.notice_days` | 45 | from 2026-01-01 | US-WIS5-018 |
| `wi.final_pay.rule` | earlier of next regular payday or 31-day limit (quit and discharge) | from 2026-01-01 | US-WIS5-004 |
| `wi.garn.creditor.max_percent` | 20 | from 2026-01-01 | US-WIS5-008 |
| `wi.garn.garnishee_fee` | 15 | from 2026-01-01 | US-WIS5-008 |
| `wi.garn.iwo.employer_fee.per_payment` | 3 | from 2026-01-01 | US-WIS5-009 |
| `wi.garn.iwo.remit_days` | 5 | from 2026-01-01 | US-WIS5-009 |
| `wi.labour.direct_deposit.employer_may_require` | True | from 2026-01-01 | US-WIS5-005 |
| `wi.labour.lodging_credit.weekly` | 58 | from 2009-07-24 | US-WIS5-001 |
| `wi.labour.minwage.opportunity.hourly` | 5.90 | from 2009-07-24 | US-WIS5-001 |
| `wi.leave.sick.state_statute.exists` | False | from 2026-01-01 | US-WIS5-006 |
| `wi.leave.wfmla.employer_threshold` | 50 | from 2026-01-01 | US-WIS5-006 |
| `wi.local_mandates.preempted` | True | from 2009-07-24 | US-WIS5-001 |
| `wi.local_wage_tax.exists` | False | from 2026-01-01 | US-WIR3-001 |
| `wi.minwage.hourly` | 7.25 | from 2009-07-24 | US-WIS5-001 |
| `wi.minwage.tipped.cash_wage` | 2.33 | from 2009-07-24 | US-WIS5-002 |
| `wi.newhire.report_days` | 20 | from 2026-03-16 | US-WIS5-013 |
| `wi.overtime.premium.multiplier` | 1.5 | from 2003-12-01 | US-WIL-001 |
| `wi.overtime.weekly_threshold_hours` | 40 | from 2003-12-01 | US-WIS5-003 |
| `wi.pay_frequency.rule` | at least monthly, wages to a day max 31 days before payment | from 2026-01-01 | US-WIS5-004 |
| `wi.payslip.items` | hours worked, rate, amount and reason for each deduction | from 2026-01-01 | US-WIP52-001 |
| `wi.pit.nonresident.de_minimis` | 1500 | from 2026-01-01 | US-WIS5-011 |
| `wi.pit.oracle.example_1.withholding` | 7.59 | from 2022-01-01 | US-WIS5-011 |
| `wi.pit.oracle.example_2.withholding` | 14.34 | from 2022-01-01 | US-WIS5-011 |
| `wi.pit.oracle.example_3.withholding` | 22.08 | from 2022-01-01 | US-WIS5-011 |
| `wi.pit.rounding` | none stated | from 2026-01-01 | US-WIS5-011 |
| `wi.pit.statutory.rates` | 3.50;4.40;5.30;7.65 | from 2025-01-01 | US-WIS5-010 |
| `wi.pit.supplemental.flat_rates` | 3.54 (0-12,760); 4.65 (to 25,520); 5.30 (to 280,950); 7.65 (above) by estimated annual gross | from 2022-01-01 | US-WIP51-001 |
| `wi.pit.wh.bracket.1.ceiling` | 12,760 | from 2022-01-01 | US-WIP51-001 |
| `wi.pit.wh.bracket.1.rate` | 3.54 | from 2022-01-01 | US-WIP51-001 |
| `wi.pit.wh.bracket.2.ceiling` | 25,520 | from 2022-01-01 | US-WIP51-001 |
| `wi.pit.wh.bracket.2.rate` | 4.65 | from 2022-01-01 | US-WIP51-001 |
| `wi.pit.wh.bracket.3.ceiling` | 280,950 | from 2022-01-01 | US-WIP51-001 |
| `wi.pit.wh.bracket.3.rate` | 5.3 | from 2022-01-01 | US-WIP51-001 |
| `wi.pit.wh.bracket.3.rate` | 5.30 | from 2022-01-01 | US-WIP51-001 |
| `wi.pit.wh.bracket.4.rate` | 7.65 | from 2022-01-01 | US-WIP51-001 |
| `wi.pit.wh.exemption` | 400 | from 2022-01-01 | US-WIP51-001 |
| `wi.pit.wh.std_deduction.married` | 9461 | from 2022-01-01 | US-WIP51-001 |
| `wi.pit.wh.std_deduction.single` | 6702 | from 2022-01-01 | US-WIP51-001 |
| `wi.prevailing_wage.exists` | False | from 2026-01-01 | US-WIP52-002 |
| `wi.reciprocity.states` | IL;IN;KY;MI (W-220); MN arrangement | from 2026-01-01 | US-MULTI-006 |
| `wi.records.retention_years` | 3 | from 2009-07-24 | US-WIS5-002 |
| `wi.report.ui.quarterly_due` | end of month after quarter | from 2026-03-16 | US-WIS5-013 |
| `wi.report.w2.efile_threshold` | 10 | from 2026-01-01 | US-WIS5-012 |
| `wi.report.wt7.due` | January 31 (TY2026: February 1, 2027) | from 2026-01-01 | US-WIS5-016 |
| `wi.sdi_pfml.exists` | False | from 2024-03-01 | US-WIR3-004 |
| `wi.sui.employee.rate` | 0 | from 2026-03-16 | US-WIR3-003 |
| `wi.sui.employer.rate.max` | 12 | from 2026-01-01 to 2027-12-31 | US-WIS5-019 |
| `wi.sui.wage_base` | 14,000 | from 2013-01-01 | US-WIS5-014 |
| `wi.term.plant_closing.notice_days` | 60 | from 2026-01-01 | US-WIS5-004 |
| `wi.term.vacation.payout` | payable if written policy with no written forfeiture clause | from 2026-01-01 | US-WIS5-005 |
| `wi.ui.rate.new_employer.large` | 3.25 | from 2026-01-01 to 2027-12-31 | US-WIS5-019 |
| `wi.ui.rate.new_employer.small` | 3.05 | from 2026-01-01 to 2027-12-31 | US-WIS5-019 |
| `wi.ui.schedule.in_effect` | D | from 2026-01-01 to 2027-12-31 | US-WIS5-019 |
| `wi.wh.certificate` | WT-4; federal W-4 not accepted; none = zero exemptions | from 2026-01-01 | US-WIS5-011 |
| `wi.wh.method` | W-166 (1/26) wage-bracket tables or alternate formula | from 2022-01-01 | US-WIS5-011 |
