# CCG research pack - annex_RI (Rhode Island)

Synthesis-B worker MN-WY, 2026-11-02. Unit `annex_RI` of the CCG (jurisdiction annex, all 13 domains + special populations).
Facts file: `_research/CCG-annex_RI-facts.json` (52 facts, 4 pending on the register_id pattern defect, 8 unresolved). Every claim below carries its register_id inline; numbers may be cited in the CCG only through a fact key.

## 0. How to use this pack

- Body sections 1-13 and Special populations are the stage-5 findings (`_research/stage5/RI.md`), carried verbatim because they are already organised by the 13 CCG domains with register ids inline.
- Federal layer (FIT, FICA, FUTA, W-2/941/940), the multistate rules (reciprocity, sourcing) and the language seams (US-OWN-006: payslip in English; second-language duties attach to notices and posters only) live in annex_FED / annex_MULTI and are not repeated here.
- Special populations (US-OWN-005): the state-level rules are in the Special populations table below; the country-wide coverage matrix is CCG unit `coverage`.
- Values are 2026 unless the fact says otherwise. 2027 values appear only where the row carries an enacted or published 2027 figure; projections are never facts.

## 0.1 Synthesis decisions and traps (bind the builder)

- Two institutions: Division of Taxation (withholding, RI-941, W-3) and DLT (TX-17 UI/TDI/JDA). Do not mix portals.
- Supplemental flat 5.99% - US-RI-006 is wrong; booklet instruction 12 governs.
- UI/TDI wages EXCLUDE employee 401(k) and 125 contributions (departs from FUTA).
- Exemption becomes zero above 290,800 annualised (cliff).
- Oracle: booklet weekly 2,195 / 1 exemption = 87.57.

## 0.2 Register status check of the ids cited in the findings

These ids appear in the findings but are not plain `active`; do not cite them for a number:

- US-RI-001: superseded
- US-RI-002: gated
- US-RI-006: superseded
- US-RIS5-008: partial
- US-RIS5-021: partial

## 0.3 Facts emitted

| key | value | from | to | register_id | conf |
|---|---|---|---|---|---|
| `ri.minwage.hourly` | 15.0 USD | 2025-01-01 | 2025-12-31 | US-RIS5-001 | high |
| `ri.minwage.hourly` | 16.0 USD | 2026-01-01 | 2026-12-31 | US-RIS5-001 | high |
| `ri.minwage.hourly` | 17.0 USD | 2027-01-01 |  | US-RIS5-001 | high |
| `ri.labour.minwage.minor_14_15.ratio` | 75 % | 2017-01-01 |  | US-RIS5-002 | high |
| `ri.labour.minwage.student_nonprofit.ratio` | 90 % | 2017-01-01 |  | US-RIS5-002 | high |
| `ri.minwage.tipped.cash_wage` | 3.89 USD | 2017-01-01 |  | US-RIS5-002 | high |
| `ri.overtime.weekly_threshold_hours` | 40 hours | 2019-01-01 |  | US-RIS5-003 | high |
| `ri.overtime.premium.multiplier` | 1.5 ratio | 2019-01-01 |  | US-RIS5-003 | high |
| `ri.pay_frequency.rule` | weekly (unless fixed at biweekly/semi-monthly/monthly/yearly rate); payday within 9 days of period end | 2013-01-01 |  | US-RIS5-004 | high |
| `ri.payment.method` | direct deposit or payroll card only at employee written/electronic request; one free full withdrawal per period | 2015-01-01 |  | US-RIS5-005 | high |
| `ri.deduction.remittance_days` | 21 days | 1990-01-01 |  | US-RIS5-007 | high |
| `ri.wh.method` | percentage method or wage-bracket tables, same for all filing statuses | 2026-01-01 | 2026-12-31 | US-RIS5-019 | high |
| `ri.pit.bracket.1.ceiling` | 82050 USD | 2026-01-01 | 2026-12-31 | US-RIS5-019 | high |
| `ri.pit.bracket.1.rate` | 3.75 % | 2026-01-01 | 2026-12-31 | US-RIS5-019 | high |
| `ri.pit.bracket.2.ceiling` | 186450 USD | 2026-01-01 | 2026-12-31 | US-RIS5-019 | high |
| `ri.pit.bracket.2.rate` | 4.75 % | 2026-01-01 | 2026-12-31 | US-RIS5-019 | high |
| `ri.pit.bracket.2.base_tax` | 3076.88 USD | 2026-01-01 | 2026-12-31 | US-RIS5-019 | high |
| `ri.pit.bracket.3.rate` | 5.99 % | 2026-01-01 | 2026-12-31 | US-RIS5-019 | high |
| `ri.pit.bracket.3.base_tax` | 8035.88 USD | 2026-01-01 | 2026-12-31 | US-RIS5-019 | high |
| `ri.pit.exemption.annual` | 1000 USD | 2026-01-01 | 2026-12-31 | US-RIS5-019 | high |
| `ri.pit.exemption.cliff.annual_wages` | 290800 USD | 2026-01-01 | 2026-12-31 | US-RIS5-019 | high |
| `ri.pit.oracle.example_1.withholding` | 87.57 USD | 2026-01-01 | 2026-12-31 | US-RIS5-019 | high |
| `ri.wh.certificate` | RI W-4 (2026) mandatory in addition to federal W-4; max 10 allowances; EXEMPT renewed yearly | 2020-01-01 | 2026-12-31 | US-RIS5-019 | high |
| `ri.wh.supplemental.rate` | 5.99 % | 2026-01-01 | 2026-12-31 | US-RIS5-019 | high |
| `ri.sui.wage_base` | 30800 USD | 2026-01-01 | 2026-12-31 | US-RIP9V-001 | high |
| `ri.ui.wage_base.highest_rate` | 32300 USD | 2026-01-01 | 2026-12-31 | US-RIP9V-001 | high |
| `ri.sui.employer.rate.min` | 0.9 % | 2026-01-01 | 2026-12-31 | US-RIP9V-001 | high |
| `ri.sui.employer.rate.max` | 9.4 % | 2026-01-01 | 2026-12-31 | US-RIP9V-001 | high |
| `ri.sui.new_employer.rate` | 1.21 % | 2026-01-01 | 2026-12-31 | US-RIP9V-001 | high |
| `ri.ui.jda.rate` | 0.21 % | 2026-01-01 | 2026-12-31 | US-RIP7-001 | high |
| `ri.sui.employee.rate` | 0 % | 2026-01-01 |  | US-RIP9V-001 | high |
| `ri.sui.wage_base.other_state_credit` | True | 2026-01-01 |  | US-RIS5-013 | high |
| `ri.tdi.employee.rate` | 1.1 % | 2026-01-01 | 2026-12-31 | US-RIP9V-001 | high |
| `ri.tdi.wage_base.annual` | 100000 USD | 2026-01-01 | 2026-12-31 | US-RIP9V-001 | high |
| `ri.tdi.employee.max_annual` | 1100.0 USD | 2026-01-01 | 2026-12-31 | US-RIP9V-001 | high |
| `ri.tdi.coverage_test` | follows UI localization | 2026-01-01 |  | US-RIS5-016 | high |
| `ri.tdi.late_deduction.recoverable` | False | 2022-04-11 |  | US-RIS5-017 | high |
| `ri.ui_tdi.wages.401k_section125_excluded` | True | 2022-04-11 |  | US-RIS5-017 | high |
| `ri.report.wh.weekly_threshold.monthly` | 600 USD | 2026-01-01 |  | US-RIS5-018 | high |
| `ri.report.ri941.due` | last day of month after quarter | 2026-01-01 |  | US-RIS5-018 | high |
| `ri.report.w3.due` | 31 January | 2026-01-01 | 2026-12-31 | US-RIS5-019 | high |
| `ri.report.w2.efile_threshold` | 25 | 2026-01-01 | 2026-12-31 | US-RIS5-019 | high |
| `ri.report.tx17.due` | Jan 31; Apr 30; Jul 31; Oct 31 | 2022-04-11 |  | US-RIS5-017 | high |
| `ri.newhire.report_days` | 14 days | 1997-10-01 |  | US-RIS5-010 | high |
| `ri.leave.paid_sick.employer_threshold` | 18 | 2020-01-01 |  | US-RIS5-009 | high |
| `ri.leave.paid_sick.accrual_ratio_hours_worked` | 35 hours | 2020-01-01 |  | US-RIS5-009 | high |
| `ri.leave.paid_sick.annual_cap_hours` | 40 hours | 2020-01-01 |  | US-RIS5-009 | high |
| `ri.leave.sick.payout_on_separation` | False | 2020-01-01 |  | US-RIS5-009 | high |
| `ri.final_pay.rule` | next regular payday; within 24 hours on liquidation/merger/sale/move out of state | 2004-01-01 |  | US-RIS5-006 | high |
| `ri.term.vacation.payout_after_years` | 1 years | 2004-01-01 |  | US-RIS5-006 | high |
| `ri.garn.consumer.state_exempt_amount` | 50 USD | 2025-06-10 |  | US-RIS5-012 | high |
| `ri.data.ssn.mailed_prohibited` | True | 2008-01-01 |  | US-RIS5-020 | high |
| `ri.reciprocity.states` | none | 2026-01-01 |  | US-RI-P5-2-003 (PENDING id pattern) | high |
| `ri.local_wage_tax.exists` | False | 2026-01-01 |  | US-RI-P5-2-001 (PENDING id pattern) | high |
| `ri.payslip.items` | hours worked (non-exempt), every deduction with explanation; regular hourly rate in commercial construction | 2026-01-01 |  | US-RI-P5-1-002 (PENDING id pattern) | high |
| `ri.prevailing_wage.threshold` | 1000 USD | 2026-01-01 |  | US-RI-P5-1-003 (PENDING id pattern) | high |

# Findings by domain (stage 5)

## 1. labour_code
- **State minimum wage** [US-RIS5-001, A.1, RIGL 28-12-3(o)-(q)]:

  | From | Rate (USD/h) |
  |---|---|
  | 2025-01-01 | 15.00 |
  | 2026-01-01 | 16.00 |
  | 2027-01-01 | 17.00 (already enacted, P.L. 2025 ch. 222/223, effective 2025-06-24) |

  These are fixed statutory steps. There is no indexation clause. Confidence: high.
- **Local minimum wages.** None located. RI has no municipal minimum-wage layer in the sources read: the House Fiscal report says cities and towns cannot levy income-based taxes [US-RI-P5-2-001], and no municipal wage ordinance was found. Confidence: medium. This rests on the absence of a find, not on a statutory preemption I read.
- **Minors and students** [US-RIS5-002]:
  - Minors aged 14-15 get at least 75% of the minimum. For every hour in a week where they work more than 24 hours, the full minimum applies (28-12-3.1).
  - Full-time students under 19 working for nonprofit religious, educational, library or community-service employers get at least 90% (28-12-5(f)).
- **Tipped employees** [US-RIS5-002]. Covers restaurants, hotels and other industries, except taxicabs. The cash wage is at least **USD 3.89/h** (since 2017-01-01). The maximum tip credit is therefore 16.00 − 3.89 = **12.11** in 2026 and **13.11** in 2027 (derived).
- **Overtime** [US-RIS5-003, A.1]:
  - 1.5× the regular rate above 40 hours a week. There is no daily overtime.
  - The fluctuating-workweek method is barred for delivery drivers and sales merchandisers.
  - Retail Sunday and holiday hours already paid at 1.5× under 5-23-2 are excluded from the weekly count.
  - Municipal firefighters: 42-hour average over 8 weeks.
  - Exemptions (28-12-4.3): FLSA white-collar employees on a salary of at least USD 200/week, summer camps, police, public comp-time agreements, motor carriers, vehicle and farm-implement dealers, agriculture, and air-carrier voluntary shift trades.
- **Pay frequency and timing** [US-RIS5-004]:
  - **Weekly pay** is the rule (28-14-2.2(a)), except for employees whose compensation is fixed at a biweekly, semi-monthly, monthly or yearly rate. Public employers and religious, literary or charitable corporations are excluded.
  - DLT may approve less-than-weekly pay (at least twice a month) on petition, with a surety bond.
  - The payday must fall within **9 days** of the end of the pay period.
  - A payday change needs **3 paydays'** notice (28-14-2).
- **Method of payment** [US-RIS5-005]. Direct deposit or payroll card only at the employee's written or electronic request, and with the employer's consent. A payroll card must allow one free withdrawal of full net pay per pay period (weekly if pay is more frequent) and free balance inquiry.
- **Deduction remittance** [US-RIS5-007]. Any payroll deduction must be paid over within 21 days after the end of the month in which it was taken.

## 2. income_tax
- **Method (2026)** [US-RIS5-019, A.2, 2026 booklet pp. 9-10]:
  - Percentage method or wage-bracket tables, the same for **all filing statuses**.
  - Annual brackets: **0–82,050 at 3.75%**; **82,050–186,450: 3,076.88 + 4.75%**; **over 186,450: 8,035.88 + 5.99%**.
  - Per-period tables are the annual table divided by the number of periods, rounded to whole dollars: weekly 1,578 / 3,586; biweekly 3,156 / 7,171; semimonthly 3,419 / 7,769; monthly 6,838 / 15,538; quarterly 20,513 / 46,613; semiannual 41,025 / 93,225; daily 315.58 / 717.12.
- **Allowances.** One withholding exemption is worth **1,000 a year**: weekly 19.23, biweekly 38.46, semimonthly 41.67, monthly 83.33, quarterly 250, semiannual 500, daily 3.85.
  - The exemption becomes **zero** when period wages exceed 290,800 a year (weekly 5,592.31, biweekly 11,184.62, semimonthly 12,116.67, monthly 24,233.33, quarterly 72,700, semiannual 145,400).
  - The cut-off is a cliff: period wages above the threshold get no exemption at all. It is not a gradual phase-out.
- **G-DERIVE.** I reproduced the booklet's worked example in Python, and it is the oracle: weekly 2,195.00 with 1 exemption → 2,175.77 taxable → 59.18 + (2,175.77 − 1,578) × 4.75% = **87.57**, which matches.
  - The annual breakpoints divided by 52, 26, 24, 12 and 4 round to the published per-period breakpoints.
  - 82,050 × 3.75% = 3,076.88 and 3,076.88 + 104,400 × 4.75% = 8,035.88, both matching.
- **Form.** The **RI W-4 (2026 edition)** is mandatory in addition to the federal W-4 (since 2020-01-01).
  - Allowances are capped at 10 (line 1E).
  - "EXEMPT" (no liability last year or this year) and "EXEMPT-MS" (MSRRA military spouse) must be renewed every year.
  - The employer keeps the form on file [US-RIS5-019].
- **Supplemental wages.** Flat **5.99%** (instruction 12), or the aggregate method (instruction 4).
- **Rounding.** The booklet states no rounding rule. The tables work to the cent.
- **Who must withhold** [US-RI-P5-2-003, US-RIS5-019 instr. 3]:
  - wages subject to federal withholding, where any part is for services performed in RI;
  - nonresidents working in RI;
  - out-of-state employers may withhold for RI residents as a convenience.
  - **No reciprocity agreements** and no day or dollar threshold.
  - Resident credit for tax paid to another state: Schedule II [US-RI-P5-2-002].
  - No convenience-of-employer rule was found.
- **Local income taxes.** None. Municipalities are barred from income-based taxes [US-RI-P5-2-001].
- **Conformity.** RI starts from federal AGI and applies Schedule M modifications [US-RI-P5-2-002 source file]. RI **decoupled from federal H.R. 1** in the FY2026 budget (H 5076 Sub A, Art. 5) [US-RIS5-023]. The 2026 withholding method is unchanged by that decoupling.

## 3. social_security
- **UI (DLT Employer Tax Unit)** [US-RIP9V-001]:
  - 2026 taxable wage base **30,800**; 32,300 for employers at the highest rate (reserve ratio of −24.00 or below).
  - Schedule F: **0.9%–9.4%**, each reduced by 0.21 to offset the employer **Job Development Assessment 0.21%** [US-RIP7-001].
  - New-employer rate **1.21%**, JDA included.
  - No employee UI contribution.
- **Wage-base indexation** [US-RIS5-014]. 46.5% of the prior-year average annual wage, computed each 30 September and rounded **up** to the next 200. The highest-rate employers pay on that base + 1,500, and 30,800 + 1,500 = 32,300 reconciles.
- **SUI wage-base credit for other-state wages** (MULTI-OQ-2) [US-RIS5-013, A.1]. **Yes.** For the base, "employment" includes services covered by another state's or the federal employment-security law. Wages the same employer (or a predecessor) already paid in the year for other-state employment count toward the RI base.
- **TDI / TCI** (employee-only, no employer share) [US-RIP9V-001, US-RIS5-015]:
  - 2026 rate **1.1%** on a taxable wage base of **100,000**, so the maximum is **1,100.00**.
  - 2025 for comparison: 1.3% on 89,200, maximum 1,159.60.
  - Derivations checked in Python: 89,200 × 1.3% = 1,159.60; a full-time worker at 16.00 × 2,080 = 33,280 pays 366.08 (matches the DLT release).
  - Base formula: the greater of 38,000 or max WBA × 30 / 0.36, rounded up to 100. A base of 100,000 implies a maximum WBA of 1,200, but I did not read the WBA itself.
  - Rate = fund cost rate, set by 15 November.
- **TDI multistate coverage** (MULTI-OQ-3) [US-RIS5-016, A.1]. TDI "employment" has the same definition as UI (chapter 42), so TDI follows the **UI localization test**. DLT FAQ restates localization (28-42-4/5/6) and says a remote RI employee is registered at their home address [US-RIS5-017].
- **TDI not deducted on time** [US-RIS5-017]. The employer cannot recover it from later pay and becomes liable itself (28-40-4).
- **Coverage exclusions (UI and TDI)** [US-RIS5-022, 28-42-8]: domestic service below 1,000/quarter, family employment, churches and ministers, 501(a) organisations below 50/quarter, co-op students, AmeriCorps, commission-only real-estate and insurance agents, and others listed in the row.
- **Other levies.** None beyond JDA and TDI [US-RIP9V-002, US-OWN-007].
- **No PFML programme separate from TCI.**

## 4. payslip_statute
- **Content** [US-RI-P5-1-002, 28-14-2.1]. Every regular payday: hours worked (except employees exempt under 28-12-4.3), every deduction with an explanation, and, in commercial construction only, the regular hourly rate.
- **Delivery.** The statement may be electronic. A free printed copy goes to any employee who asks in writing. No language clause [US-RIL-001].
- **Records** [US-RIS5-008, partial]. Hours and wages per pay period, kept **3 years**. That is the version effective until 2026-01-01.
  - A **new 28-14-12 took effect 2026-01-01**. Per tier-B leads it is H 5679 (2025), which became law without the Governor's signature and requires a written notice of employment terms at hire.
  - The official text was **not reachable** (ACCESS gap), so the 2026 record-keeping/retention content and the hiring-notice fields are unconfirmed.
- **SSN** [US-RIS5-020, 6-48-8]. See section 12.
- **Reach to out-of-state work** (MULTI-OQ-8). 28-14-2.1 has no territorial clause. Default: it applies to employees working in RI. No RI ruling located.

## 5. reporting_instruments
There are two institutions and two portals [US-RIS5-024].
- **Division of Taxation (withholding)** [US-RIS5-018, US-RIS5-019]:
  - **Weekly deposit**: if 600/month or more, due the next banking day after the Sunday–Saturday week, electronic only.
  - **Monthly deposit**: 50–599/month, with WTM (RI-941M) due the 20th.
  - **Quarterly deposit**: under 50/month.
  - **RI-941** quarterly return and reconciliation, due the last day of the month after the quarter, for every withholding employer.
  - **RI W-3** annual reconciliation, due 31 January.
  - **E-file/e-pay mandate**: averaging 200/month or more, or an entity with 5,000 or more of combined annual liability, or gross income over 100,000.
  - **W-2 to RI**: due 31 January, **EFW2** (.txt, ASCII, RS record required, zip if over 5 MB, max 49 MB) through the Tax Portal. Mandatory electronic if the employer must e-file with SSA and has **25 or more RI employees**, or claims any RI tax credit.
  - Bulk filers register through a Payroll Letter of Intent.
  - 1099s must be filed even without RI withholding.
  - The 2026 payment calendar is in the booklet (e.g. Q3 RI-941 due 2026-11-02, Q4 due 2027-02-01).
- **DLT Employer Tax Unit (UI/TDI/JDA)** [US-RIS5-017]:
  - **TX-17 Quarterly Tax and Wage Report**: one report and one payment for all three funds, due Jan 31 / Apr 30 / Jul 31 / Oct 31. A zero report is required.
  - **Electronic wage data** is mandatory at 25 or more employees, including for payroll providers.
  - Payment by ACH credit or debit, no card.
  - Corrections: 3 years.
  - Penalties: 1.5%/month interest; 25 per late report plus 25/month, up to 200; 10% of unpaid tax.
  - **Registration**: Business Application and Registration (BAR) form; the liability date is the first wages paid in RI. Account closure: TX-13.
  - PEOs and common paymasters are not recognised: each entity reports under its own account.
  - The Employer Tax unit moved from Taxation to DLT on 2022-04-11 [US-RIS5-024].
- **New-hire reporting** [US-RIS5-010, US-RIS5-011]:
  - Due within **14 days** of hire or rehire. Electronic reporters may instead send two monthly transmissions 12–16 days apart.
  - Goes to the RI State Directory of New Hires (designee of the Division of Taxation; OCSS page).
  - Fields: name, address, SSN, date of hire, state of hire (multistate). These are from the OCSS page lead. The statutory list in 15-24-5 was not read.
  - Penalty 20 per violation, 500 for conspiracy. Multistate employers may designate one state.
- **POA.** RI-2848 [US-RI-P5-1-004].

## 6. leave
- **Paid sick and safe leave** [US-RIS5-009, A.1, RIGL 28-57]. Applies to employers with **18 or more employees** (counted in RI).
  - Accrual: 1 hour per 35 hours worked, up to **40 hours/year** for both accrual and use.
  - FLSA-exempt employees are assumed to work 40 hours a week.
  - Unused leave must carry over (use is still capped at 40), or the employer pays it out at year-end and front-loads the next year.
  - Use waiting period: 90 days for new hires; temporary workers 180 days; seasonal workers 150 days.
  - **No payout at separation.** Leave is reinstated on rehire within 135 days.
  - Pay: the same rate and benefits as normal, never below the state minimum. The employer may set a minimum increment of no more than 4 hours.
  - Employers under 18 employees: 40 hours of unpaid, protected leave.
  - A PTO policy of 40 hours or more is exempt from accrual tracking, carryover and payout.
  - Municipal and state employees are excluded.
- **Coverage of employees working partly in RI** (MULTI-OQ-4). The statute has no hours-in-state threshold. The employer-size count is of employees "in Rhode Island". No DLT rule was read. Default: hours worked in RI accrue.
- **TCI (family leave benefit, insurance-paid)** [US-RIS5-021, partial]:
  - Job restoration, and the employer must keep existing health benefits during the leave (the employee keeps paying their share).
  - 30 days' written notice.
  - Week cap: the archived statute says 6 weeks (from 2023), the DLT release of 2025-12-18 says 7, and tier-B leads say **8 from 2026-01-01**. Not settled at tier A. This affects benefits only, not the payroll deduction.

## 7. termination
- **Final pay** [US-RIS5-006, 28-14-4]:
  - Resignation or discharge: wages are due on the **next regular payday**.
  - Liquidation, merger, sale of the business or a move out of state: **within 24 hours**.
- **Accrued vacation** is payable at separation **after 1 year of service**, in full or prorated, if it was accrued or awarded under a CBA, a written or verbal policy, or an agreement.
- **Paid sick leave** is not paid out [US-RIS5-009].
- **Public-employee comp time** is paid at termination at the higher of the 3-year average or the final rate [US-RIS5-003].
- **UI separation notice / WARN.** Not researched (out of budget; no payroll computation impact).

## 8. benefits_in_kind
- **Income tax.** RI starts from federal AGI, so the federal exclusions (401(k) deferrals, §125, HSA, transit, group-term life within federal limits) carry through. The 2025 Schedule M keyword scan found no addition modification for these [US-RI-P5-2-002 source file]. The H.R. 1 decoupling items are not itemised here [US-RIS5-023]. Confidence: medium.
- **UI/TDI.** Employee contributions to 401(k), medical and disability insurance plans and §125 plans are **excluded** from both total and taxable UI and TDI wages [US-RIS5-017, A.2]. RI departs from FUTA here: under FUTA, 401(k) elective deferrals are FUTA wages.

## 9. deductions_garnishments
- **Remittance.** 21 days after the end of the month [US-RIS5-007]. Authorisation rules beyond that were not read (28-14-3.2 is in the index only).
- **Wage exemption** [US-RIS5-012, 9-26-4(8)]:
  - Only **50** of ordinary wages is exempt under state law, which is less protective than the CCPA. The federal 75% / 30× limit [US-FED-011] therefore governs ordinary garnishment.
  - Full exemption applies to debtors on public relief, and for 1 year after the relief ends. This is state-specific.
- **Child support.** e-IWO is accepted (OCSS employer menu). RI fees and priority rules were not read. Interstate orders follow the work-state law [MULTI section 9].
- **State tax levies.** Not researched.

## 10. collective_agreements
- **Prevailing wage** [US-RI-P5-1-003, US-RI-P5-1-005]. Public works contracts over **1,000** must state the prevailing wages set by the DLT director, paid weekly. Certified-payroll mechanics were not read.

## 11. indexation
| Item | Mechanism | Value 2026 | Publication |
|---|---|---|---|
| Minimum wage | Fixed statutory steps, not indexed | 16.00; 17.00 from 2027 | RIGL 28-12-3 [US-RIS5-001] |
| UI wage base | 46.5% of avg annual wage, rounded up to 200; +1,500 for highest-rate employers | 30,800 / 32,300 | DLT December release [US-RIS5-014, US-RIP9V-001] |
| TDI wage base | max(38,000; max WBA × 30 / 0.36), rounded up to 100 | 100,000 | DLT release [US-RIS5-015] |
| TDI rate | Fund cost rate by 15 November, rounded down to 0.1% | 1.1% | DLT release |
| PIT brackets / exemption cut-off | Annual (booklet) | 82,050 / 186,450; 1,000; 290,800 | Withholding booklet (Nov/Dec) [US-RIS5-019] |
| Tip cash wage | Fixed since 2017 | 3.89 | 28-12-5 [US-RIS5-002] |

The 2027 UI/TDI release and the 2027 booklet are not yet published (expected December 2026). They are next_year items.

## 12. data_protection
- **SSN** [US-RIS5-020, 6-48-8]. No one may print any part of an SSN on material **mailed** to the individual unless law requires it, show it to the public, or require it over an unsecured connection. Internal administrative use is allowed.
- **Effect on payroll.** A mailed pay statement must carry **no** part of the SSN. For electronic statements there is no specific truncation rule, but public exposure is barred.
- Payroll records are kept 3 years (old 28-14-12; the 2026 version is unread).

## 13. live_legal_change (2026-01-01 → 2026-11-02)
- Minimum wage 16.00 from 2026-01-01 and 17.00 enacted for 2027-01-01 [US-RIS5-001].
- TDI rate 1.3% → 1.1%; TDI base 89,200 → 100,000; UI base 29,800 → 30,800; UI Schedule G → F [US-RIP9V-001].
- New 28-14-12 effective 2026-01-01 (hiring notice / records). Text unread [US-RIS5-008, partial].
- TCI week cap raised (7 or 8 weeks). Not settled at tier A [US-RIS5-021, partial].
- RI decoupled from H.R. 1 (FY2026 budget). PIT emergency regulation 280-RICR-20-55-16 effective 2025-12-15 [US-RIS5-023].
- Non-payroll taxes effective in 2026 (hotel, short-term rental, kratom, non-owner-occupied property tax): no payroll impact [US-RIS5-023].
- **Sweep limit.** I read the Taxation "recent changes" banner and the H.R. 1 page. I did not read the DLT news list or the 2026 General Assembly public laws, because rilegislature.gov was unreachable and the CDX index was offline.

## Special populations (state level)
| Population | RI rule | register_id |
|---|---|---|
| Domestic / household workers | UI and TDI apply at 1,000 or more cash wages in any calendar quarter (current or prior year); minimum wage applies | US-RIS5-022, US-RIS5-017 |
| Agricultural | Exempt from state overtime (28-12-4.3(a)(9)). Not among the UI exclusions in 28-42-8 (UI coverage of farm work not confirmed) | US-RIS5-003, US-RIS5-022 |
| Minors | 14-15: at least 75% of minimum, full minimum in weeks over 24 hours. Family employment of a child under 18 by a parent sole proprietor is excluded from UI/TDI | US-RIS5-002, US-RIS5-022 |
| Tipped | Cash wage at least 3.89; tip credit up to minimum − 3.89 (12.11 in 2026) | US-RIS5-002 |
| Clergy / religious | Churches, church-controlled organisations, ministers and members of religious orders excluded from UI/TDI; income tax follows federal withholding (RI withholds only where federal withholding applies) | US-RIS5-022, US-RIS5-019 |
| Students | Full-time co-op students in credit programs excluded from UI/TDI; full-time students under 19 at nonprofits: at least 90% of minimum | US-RIS5-022, US-RIS5-002 |
| Nonresident aliens | No state rule beyond federal: RI withholding applies where federal withholding applies (booklet instr. 3); MSRRA military spouses may claim EXEMPT-MS | US-RIS5-019 |
| Statutory employees | No state rule located beyond federal; commission-only real-estate and insurance agents are excluded from UI/TDI | US-RIS5-022 |
| Government employees | Other-state and federal employment excluded from RI UI; state/municipal employees excluded from paid sick leave and from weekly-pay rule; comp-time option | US-RIS5-022, US-RIS5-009, US-RIS5-004, US-RIS5-003 |

## MULTI hand-offs, answered for RI
- **OQ-2 (SUI credit for other-state wages): YES** [US-RIS5-013].
- **OQ-3 (TDI coverage): follows UI localization** [US-RIS5-016, US-RIS5-017].
- **OQ-4 (paid sick leave, partly-in-state workers):** no statutory threshold; employee count is "in Rhode Island" [US-RIS5-009]. Confidence: medium.
- **OQ-8 (pay-statement reach):** no territorial clause; default is work in RI [US-RI-P5-1-002].

## ACCESS gaps (exact URLs)
1. `https://webserver.rilegislature.gov/Statutes/TITLE28/28-14/28-14-12_28-14-12.htm`: 28-14-12 [Effective January 1, 2026]. Live host curl 000; Wayback `2026id_` 404 (not archived).
2. `https://webserver.rilegislature.gov/BillText25/HouseText25/H5679A.htm`: 2025 H 5679 text. Live curl 000; Wayback 404. The exact bill-text file name is a guess.
3. `https://webserver.rilegislature.gov/Statutes/TITLE44/44-30/44-30-71.htm`: withholding duty (keeps US-RI-002 gated). Live curl 000; Wayback 404.
4. `https://web.archive.org/cdx/search/cdx?url=webserver.rilegislature.gov/Statutes/TITLE28/28-14/28-14-12*` and `...BillText25/HouseText25/H5679*`: "Internet Archive temporarily offline" at 08:39 BRT.
5. `https://rules.sos.ri.gov/regulations/part/280-20-55-10`: regulation text (US-RI-006). Not re-tried this run; known to show only the table of contents.
6. `https://dlt.ri.gov/` and `https://tax.ri.gov/tax-sections/withholding-tax`: 403 to plain curl (VPN off). All DLT/Taxation reads used Wayback.

## Confidence
- Withholding, UI/TDI, minimum wage, pay timing, final pay, sick leave, new hire, filings: **90-95%**, all A.1/A.2 with local files and arithmetic reproduced.
- Records/hiring notice 2026, TCI weeks, deductions authorisation and IWO specifics: **50-60%**.
- Overall unit: **85%**.

## Open questions

Mirrors `unresolved[]` of the facts file (same keys, same wording).

- **ri.meta.register_id_pattern** (blocking): 4 facts rest on active register rows whose ids (US-RI-P5-1-002, US-RI-P5-1-003, US-RI-P5-2-001, US-RI-P5-2-003) do not match the facts-schema register_id pattern ^[A-Z]{2}-[A-Z0-9]{2,12}-[0-9]{3,4}$ (multi-hyphen legacy ids). They are carried in full in _facts_pending_register_id_pattern and are NOT yet consumable facts. What would close it: Orchestrator decision: a PATCH of facts.schema.json loosening the register_id pattern (e.g. ^[A-Z]{2}-[A-Z0-9-]{2,16}-[0-9]{3,4}$), or register alias ids; then run _research/synthesis-B/_work-MN-WY/promote.py to move the pending facts into facts[].
- **ri.records.2026_version** (blocking): New 28-14-12 (effective 2026-01-01) text unread; hiring notice and retention unconfirmed (US-RIS5-008 partial). What would close it: Official section text (browser pass with VPN) or P.L. 2025 chapter text for H 5679.
- **ri.leave.tci.max_weeks** (non-blocking): TCI week cap 6/7/8 not settled at tier A (US-RIS5-021 partial). What would close it: Current 28-41-35 text or DLT TDI/TCI program page.
- **ri.pit.regulation_text** (non-blocking): 280-RICR-20-55-10 text not read (US-RI-006 MANUAL). What would close it: RICR PDF from rules.sos.ri.gov.
- **ri.report.new_hire.fields** (non-blocking): 15-24-5 statutory field list not read. What would close it: Section text on rilegislature.gov.
- **ri.bik.hr1_decoupling** (non-blocking): H.R. 1 decoupling items for individuals not itemised. What would close it: Taxation advisories ADV 2025-18 / 2025-20.
- **ri.garn.iwo_deductions_separation** (non-blocking): IWO fee/priority, 28-14-3.2 deduction authorisation, UI separation notice and state tax levy not researched. What would close it: RIGL 15-5-24 ff., 28-14-3.2 and DLT UI employer page.
- **ri.rates.next_year** (non-blocking): 2027 booklet and DLT 2027 UI/TDI release not published. What would close it: December 2026 releases.
