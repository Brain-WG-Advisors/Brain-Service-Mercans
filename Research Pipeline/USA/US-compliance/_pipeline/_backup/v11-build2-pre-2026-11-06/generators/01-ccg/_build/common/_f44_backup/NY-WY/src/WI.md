## @labour
- **Minimum wage (Wis. Stat. 104.035) [US-WIS5-001, US-WIS5-002]:** {{wi.minwage.hourly}} USD per hour, minors included; opportunity employees (young workers in their first period of employment) {{wi.labour.minwage.opportunity.hourly}} USD. No increase scheduled for 2026 or 2027.
- **Local minimum wage:** barred (104.001(2)): {{wi.local_mandates.preempted}} [US-WIS5-001].
- **Tipped employees [US-WIS5-002]:** cash wage {{wi.minwage.tipped.cash_wage}} USD per hour (lower for opportunity employees); the tip credit needs a tip declaration signed by the employee every pay period and records showing tips plus wages reach the minimum each week (DWD 272.03(2)(b)).
- **Meal and lodging credits (104.035(1)(b)):** lodging {{wi.labour.lodging_credit.weekly}} USD per week (daily and meal credits per the statute) [US-WIS5-001].
- **Overtime (DWD 274.03) [US-WIS5-003]:** {{wi.overtime.premium.multiplier}} times the regular rate over {{wi.overtime.weekly_threshold_hours}} hours per week; no daily overtime; exemptions read consistently with the FLSA; household domestic service outside the chapter.
- **Pay frequency (109.03(1)) [US-WIS5-004]:** {{wi.pay_frequency.rule}}; logging and farm labour at least quarterly; CBA and school-year exceptions.
- **Method of payment [US-WIS5-005]:** the employer may require direct deposit at no cost to the employee ({{wi.labour.direct_deposit.employer_may_require}}); a stub is still due. No paycard rule located (open point below).

## @income_tax
- **Method [US-WIP51-001, US-WIS5-011, US-WIS5-010]:** {{wi.wh.method}}; any other method needs DOR permission (71.64(1)). DOR Withholding Tax Update 2026-1 states no plan to change the withholding rates for 2026 [US-WIS5-016].
- **Withholding schedule (W-166) is not the statutory assessment schedule.** The WTC uses W-166 only.

| Annual wages after deductions | Withholding rate | Register id |
|---|---|---|
| up to {{wi.pit.wh.bracket.1.ceiling}} USD | {{wi.pit.wh.bracket.1.rate}} % | US-WIP51-001 |
| up to {{wi.pit.wh.bracket.2.ceiling}} USD | {{wi.pit.wh.bracket.2.rate}} % | US-WIP51-001 |
| up to {{wi.pit.wh.bracket.3.ceiling}} USD | {{wi.pit.wh.bracket.3.rate}} % | US-WIP51-001 |
| above | {{wi.pit.wh.bracket.4.rate}} % | US-WIP51-001 |

  The statutory assessment rates (71.06(1r), tax years after 2024, brackets indexed from 2026) are {{wi.pit.statutory.rates}} (%) [US-WIS5-010]; they apply at assessment and are never moved into the withholding engine. The 2026 indexed assessment brackets are not needed for withholding (open point below).
- **Alternate formula [US-WIP51-001]:** annualise; subtract the standard deduction (single {{wi.pit.wh.std_deduction.single}} USD, married {{wi.pit.wh.std_deduction.married}} USD, each phased out above statutory wage levels) and {{wi.pit.wh.exemption}} USD per exemption; apply the schedule; divide by the pay periods.
- **Oracle (W-166 worked examples, re-derived):** example 1 {{wi.pit.oracle.example_1.withholding}} USD; example 2 {{wi.pit.oracle.example_2.withholding}} USD; example 3 {{wi.pit.oracle.example_3.withholding}} USD; the guide rounds the bracket portion separately, so only the annual intermediate differs by a cent [US-WIS5-011]. Recomputation in Module 12.
- **Supplemental wages [US-WIP51-001]:** aggregate, or a flat rate by estimated annual gross: {{wi.pit.supplemental.flat_rates}}.
- **Rounding:** {{wi.pit.rounding}} [US-WIS5-011].
- **Certificate [US-WIS5-011, US-WIS5-016]:** {{wi.wh.certificate}}; exempt claims renewed yearly; copies to DOR above the statutory thresholds; DOR lock-in letters bind the employer. WT-4 edition: open point below.
- **Residents and nonresidents (71.63(2)) [US-WIS5-010, US-WIS5-011]:** residents withheld on all wages; nonresidents only on wages for Wisconsin work, with exceptions for interstate carriers, reciprocity, air carriers, military spouses and expected Wisconsin earnings below {{wi.pit.nonresident.de_minimis}} USD (catch-up once exceeded). Reciprocity: {{wi.reciprocity.states}} [US-MULTI-006].
- **Local income tax:** none (exists: {{wi.local_wage_tax.exists}}) [US-WIR3-001].
- **Resident and nonresident matrix.**

| Income type | Wisconsin resident | Nonresident |
|---|---|---|
| Regular salary | W-166 tables or formula on all wages | W-166 on wages for Wisconsin work, unless reciprocity (W-220) or another exception applies |
| Bonus / supplemental | Aggregate or flat rate by estimated annual gross | Same, Wisconsin share |
| Pensions | Not wages; withheld only on written request | Same |
| Benefits in kind | Federal treatment with the box-16 differences in Section 8 | Same, Wisconsin share |
| Wages paid after death | Not subject to Wisconsin withholding | Same |

## @social
- **Unemployment insurance (DWD) [US-WIS5-014, US-WIS5-019].** Taxable wage base {{wi.sui.wage_base}} USD, fixed in statute and not indexed. Rate schedule {{wi.ui.schedule.in_effect}} for 2026 and 2027 (total rate = basic + solvency), up to {{wi.sui.employer.rate.max}} %. New employer {{wi.ui.rate.new_employer.small}} % below the large-payroll threshold and {{wi.ui.rate.new_employer.large}} % at or above it (construction rates differ), for the first years [US-WIR3-002]. Annual increase cap (108.18(5)).
- **Employee contribution:** {{wi.sui.employee.rate}} % [US-WIR3-003].
- **SDI, TDI, PFML:** none (exists: {{wi.sdi_pfml.exists}}) [US-WIR3-004]; Wisconsin FMLA leave is unpaid (103.10(5)(a)) [US-WIS5-006]. Only the solvency component as an employer levy [US-WIP7-001].

## @payslip
- **Content (103.457; DWD 272.10) [US-WIP52-001, US-WIS5-002]:** on the paycheck, envelope or accompanying paper: {{wi.payslip.items}}; a coding system allowed. Electronic stub allowed if printable free; required even with direct deposit [US-WIS5-005].
- **Retention:** payroll records at least {{wi.records.retention_years}} years (DWD 272.11, 274.06) [US-WIS5-002, US-WIS5-003]. No payslip language rule [US-WIL-002].

## @reporting
- **WT-6 withholding deposit report [US-WIS5-011, US-WIS5-016]:** DOR assigns the frequency each November (no published thresholds); zero reports required; electronic only unless waived.
- **WT-7 annual reconciliation:** due {{wi.report.wt7.due}}, rejected until all WT-6s are filed.
- **State W-2 [US-WIS5-012, US-WIS5-015]:** same due date; electronic filing at {{wi.report.w2.efile_threshold}} or more W-2s; SSA EFW2 with RS record; MTA keying, upload or sFTP.
- **Quarterly UI contribution and wage report [US-WIS5-013, US-WIS5-014, US-WIS5-020]:** due {{wi.report.ui.quarterly_due}}, filed even at a zero rate; electronic filing mandatory above the employee threshold; DWD stops mailing reports in 2027 and opens a new employer portal in fall 2026.
- **New hire [US-WIS5-013]:** within {{wi.newhire.report_days}} days of the start date; multistate employers may elect one state.
- **Registration and agents:** one withholding account per legal entity; payroll service providers register and test with DOR; POA A-222 (DOR) and UCT-8291-E (UI) [US-WIS5-011, US-WIS5-016, US-WIP52-003, US-WIP51-002].

## @leave
- **Paid sick leave:** no state statute (exists: {{wi.leave.sick.state_statute.exists}}); local mandates preempted (103.10(1m), 103.12) [US-WIS5-006].
- **Wisconsin FMLA (103.10) [US-WIS5-006]:** employers with {{wi.leave.wfmla.employer_threshold}} or more permanent employees; service tests; unpaid, with substitution of paid leave. Bone marrow and organ donation leave unpaid (103.11). Vacation and holiday pay not mandated [US-WIS5-005].

## @termination
- **Final pay (109.03(2)) [US-WIS5-004]:** {{wi.final_pay.rule}}; commission sales agents and fixed-term contracts excepted. Death of an employee: wages payable on demand to the family (109.03(3)).
- **Accrued vacation:** {{wi.term.vacation.payout}} [US-WIS5-005].
- **Plant closing (109.07):** {{wi.term.plant_closing.notice_days}} days' notice [US-WIS5-004]. UI separation forms only on DWD request; poster UCB-7-P [US-WIS5-013].

## @bik
- **Conformity:** Wisconsin generally conforms to the IRC; W-166 defers to Pub 15 and 15-A; HSAs follow federal rules [US-WIS5-011]. Individual IRC conformity paragraph not isolated (open point below).
- **2026 box-16 differences (Wisconsin wages higher than federal) [US-WIS5-016]:** {{wi.bik.wi.box16_differences}}.
- **Transit and parking:** {{wi.bik.transit_parking.monthly}} USD per month each for 2026, federal and Wisconsin alike.

## @deductions
- **Deductions for damage, loss or faulty work (103.455):** written authorisation, joint determination or court finding; double damages for violations [US-WIS5-007].
- **Creditor garnishment (812.34) [US-WIS5-008]:** at most {{wi.garn.creditor.max_percent}} % of disposable earnings (stricter than the CCPA); total exemption below the poverty line or with need-based aid; garnishee fee {{wi.garn.garnishee_fee}} USD plus a small fee per later payment, deducted from the creditor's share.
- **Child support IWO (767.75) [US-WIS5-009]:** remit within {{wi.garn.iwo.remit_days}} days of payday; CCPA cap; the employer may keep up to {{wi.garn.iwo.employer_fee.per_payment}} USD per payment; the IWO has priority over other state-law process. DOR wage attachment: open point below.

## @cba
- **No current prevailing-wage regime** (exists: {{wi.prevailing_wage.exists}}) [US-WIP52-002]; the repealing acts were not read (open point below). CBAs may set a different pay frequency (109.03(1)(a)) [US-WIS5-004].

## @indexation
- **Indexed:** the statutory assessment brackets (CPI-U) from 2026 [US-WIS5-010].
- **Not indexed:** minimum wage; UI wage base [US-WIS5-014]; the withholding tables (revised by publication only; no change for 2026) [US-WIS5-016].

## @data
- **Breach notification (134.98) [US-WIS5-018]:** within a reasonable time, at most {{wi.data.breach.notice_days}} days. No statute restricting SSNs on pay statements found; SSN truncation allowed on employee copies of W-2 and 1099 but not on copies filed with DOR [US-WIS5-012, US-WIS5-011]. Personnel file inspection (103.13) [US-WIS5-007].

## @live
- **DOR Withholding Tax Update 2026-1 (2026-10-30):** no withholding rate change; tax year 2026 due dates; new box-16 differences [US-WIS5-016].
- **Assessment-level changes** (bracket expansion, retirement subtraction) for tax years after 2024 [US-WIS5-010].
- **DWD:** Schedule D continues in 2027; mailing ends in 2027; new portal fall 2026 [US-WIS5-020]. 2025 Acts 145 and 144: no withholding or contribution effect [US-WIS5-021].

## @special
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
