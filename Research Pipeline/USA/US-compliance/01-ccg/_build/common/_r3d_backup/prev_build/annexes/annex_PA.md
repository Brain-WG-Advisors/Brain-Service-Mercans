# Annex PA: Pennsylvania


Jurisdiction annex of the United States Country Configuration Guide (US-CCG-001). Layer classification: **T4 - local layer remitted to the locality on its own return** (build manifest, tier rationale). Pennsylvania Act 32 EIT/LST to the local collector [US-PA-004].

The federal layer (federal income tax withholding, FICA, FUTA, Forms W-2, 941 and 940) and the multistate rules (residence and work-location sourcing, reciprocity mechanics) are in Annex FED and Annex MULTI and are not repeated here. Independent contractors and Form 1099-NEC reporting are out of scope (owner instruction of 2026-10-29) [US-OWN-008]. Payslip language: English; second-language duties attach to notices and posters only (US-OWN-006).

Every value in this annex is bound to a verified fact and carries its legal-basis register id. A value that changes during the year is shown with its effective dates. A point marked as a research gap has not been closed by the research; it is not filled with an estimate.

## PA.1 Employment and labour code

- **Minimum wage (MWA Sec. 4(a.1); 34 Pa. Code 231.101a) [US-PAS5-001, US-PAS5-002]:** [[FACT:pa.minwage.hourly=7.25]] USD per hour statewide; the state rate rises automatically to any higher FLSA rate. Not indexed; nothing enacted for 2027 (a House bill is not law, open point below).
- **Local minimum wage:** preempted (MWA Sec. 14.1): [[FACT:pa.local_mandates.preempted=True]] [US-PAS5-001].
- **Tipped employees [US-PAS5-002, US-PAS5-004]:** cash wage [[FACT:pa.minwage.tipped.cash_wage=2.83]] USD per hour, the employer making up any shortfall to the minimum wage; a tipped employee customarily receives more than [[FACT:pa.labour.tip_credit.monthly_tip_threshold=135]] USD per month in tips (231.1); written notice of the tip credit (231.34); no deduction of card-processing fees from tips.
- **Overtime [US-PAS5-001, US-PAS5-003]:** [[FACT:pa.overtime.premium.multiplier=1.5]] times the regular rate over [[FACT:pa.overtime.weekly_threshold_hours=40]] hours per workweek; the 8-and-80 system is allowed for hospitals; no daily overtime; comp time in lieu of overtime is not legal. **Departure from the FLSA:** salaried non-exempt regular rate = [[FACT:pa.labour.overtime.salaried_nonexempt_regular_rate=remuneration / 40 hours (no fluctuating workweek)]] (231.43(g)) [US-PAS5-002].
- **Exempt salary level:** [[FACT:pa.exempt.salary.weekly_min=684]] USD per week with the federal duties tests (the PA-specific salary sections are abrogated) [US-PAS5-003].
- **Pay timing (WPCL Sec. 3(a)) [US-PAS5-005]:** [[FACT:pa.labour.pay_timing=regular paydays; within contract/customary lapse or 15 days after period end]]; notice at hire of payday, place and rate (Sec. 4).
- **Method of payment:** "lawful money of the United States or check" (WPCL Sec. 3); no PA rule read on direct deposit or paycards (open point below).
- **Records:** [[FACT:pa.records.retention_years=3]] years (MWA Sec. 8; 231.31) [US-PAS5-001, US-PAS5-002].

**Parameters (labour code and pay rules)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `pa.minwage.hourly` | [[FACT:pa.minwage.hourly=7.25]] | USD | from 2009-07-24 | US-PAS5-002 | MWA Sec. 4(a.1) follows FLSA; not indexed; no 2027 change enacted |
| `pa.local_mandates.preempted` | [[FACT:pa.local_mandates.preempted=True]] |  | from 2009-07-24 | US-PAS5-001 | MWA Sec. 14.1 (except ordinances in force 2006-01-01) |
| `pa.minwage.tipped.cash_wage` | [[FACT:pa.minwage.tipped.cash_wage=2.83]] | USD | from 2022-08-05 | US-PAS5-002 |  |
| `pa.labour.tip_credit.monthly_tip_threshold` | [[FACT:pa.labour.tip_credit.monthly_tip_threshold=135]] | USD | from 2022-08-05 | US-PAS5-002 |  |
| `pa.overtime.weekly_threshold_hours` | [[FACT:pa.overtime.weekly_threshold_hours=40]] | hours | from 2009-07-24 | US-PAS5-002 | no daily OT; 8-and-80 for hospitals |
| `pa.overtime.premium.multiplier` | [[FACT:pa.overtime.premium.multiplier=1.5]] | ratio | from 2009-07-24 | US-PAS5-001 |  |
| `pa.labour.overtime.salaried_nonexempt_regular_rate` | [[FACT:pa.labour.overtime.salaried_nonexempt_regular_rate=remuneration / 40 hours (no fluctuating workweek)]] |  | from 2022-08-05 | US-PAS5-002 | 231.43(g) |
| `pa.exempt.salary.weekly_min` | [[FACT:pa.exempt.salary.weekly_min=684]] | USD | from 2026-01-01 | US-PAS5-003 | DLI follows 2019 federal level (A.3 FAQ); 231.82-84 abrogated |
| `pa.labour.pay_timing` | [[FACT:pa.labour.pay_timing=regular paydays; within contract/customary lapse or 15 days after period end]] |  | from 1977-07-14 | US-PAS5-005 | WPCL Sec. 3(a) |

**Open research points**

- Not configured in this release [[GAP:RQ-299]]: Direct deposit, paycards and electronic pay statements: no PA rule located.
- Not configured in this release [[GAP:RQ-307]]: Child Labor Act 2012 hours/permits not read (no text layer).

## PA.2 Income tax withholding

- **State PIT [US-PAS5-009, US-PA-001, US-PA-008]:** flat [[FACT:pa.pit.rate.flat=3.07]] % on compensation, for residents (services in or outside Pennsylvania) and nonresidents (services in Pennsylvania). Method: compensation of the payroll period times the rate; no PA W-4, no allowances, no brackets. Supplemental pay is added to the current period. Rounding: [[FACT:pa.pit.rounding=none published]] [US-PAP52-002]. No oracle is needed beyond the flat-rate product. No 2027 change located.
- **Reciprocity:** [[FACT:pa.reciprocity.states=IN;MD;NJ;OH;VA;WV (REV-419)]] [US-PA-001, US-MULTI-007]. Residents get a credit for tax paid to another state; a foreign country does not count as a state [US-PAS5-012].
- **Not subject to PA withholding (DSM-12) [US-PA-001]:** agricultural and H-2A workers not subject to FICA (may elect), clergy not subject to federal withholding, domestic workers who are not employees federally, casual non-trade employees, foreign-government employees, PA-resident nonresident aliens working outside the US, statutory employees and minor newspaper carriers, federally exempt interstate transport workers.
- **Local income taxes (T4 layer).**
  - **Act 32 Earned Income Tax (Local Tax Enabling Act) [US-PAS5-017, US-PAS5-018]:** [[FACT:pa.pit.local.eit.rule=withhold greater of resident EIT and work-location nonresident EIT (DCED register)]]. Rates come per address from the DCED Address Search Application (no static table); worksites include the residences of home-based employees; a residency certificate is collected at hire and on change of address; quarterly return and payment to each work location's tax officer; annual return due [[FACT:pa.pit.local.eit.annual_due=28 February (W2-R with PSD codes)]]. Temporary assignments follow the statutory day-count rule.
  - **Local Services Tax (LTEA 301.1, 312) [US-PAS5-017]:** capped at [[FACT:pa.pit.local.lst.annual_cap=52]] USD per person per year, collected pro rata per payroll period (annual levy / number of periods, rounded down to the cent) where the levy exceeds the statutory minimum; such a levy must exempt anyone earning under [[FACT:pa.pit.local.lst.low_income_exemption=12,000]] USD in the subdivision; mandatory exemptions for fully disabled veterans and reservists called to active duty; situs is the place of employment on the first day of each period.
  - **Philadelphia Wage Tax (Sterling Act; Act 32 does not apply) [US-PAS5-022]:**

| Period | Resident | Nonresident |
|---|---|---|
| 2025-07-01 to 2026-06-30 | [[FACT:pa.local.philadelphia.resident.rate=3.74]] % | [[FACT:pa.local.philadelphia.nonresident.rate=3.43]] % |
| from 2026-07-01 | [[FACT:pa.local.philadelphia.resident.rate=3.735]] % | [[FACT:pa.local.philadelphia.nonresident.rate=3.425]] % |

  Philadelphia: residents pay wherever they work; nonresidents pay on work in the city. Quarterly returns on the Philadelphia Tax Center; no annual reconciliation.
  - **Pittsburgh payroll expense tax** (employer): [[FACT:pa.pit.local.pittsburgh.payroll_expense.rate=0.55]] % [US-PAB5-401].
- **Resident and nonresident matrix.**

| Income type | PA resident | Nonresident |
|---|---|---|
| Regular salary | Flat [[FACT:pa.pit.rate.flat=3.07]] % on all compensation, wherever earned | Flat rate on PA-service compensation, unless resident of a reciprocity state (REV-419 on file) |
| Bonus / supplemental | Added to the period, same flat rate | Same, PA-service share |
| Retirement deferrals (401(k), 403(b), 457(b)) | Taxable when deferred (Section 8) | Same, PA-service share |
| Local EIT | Greater of resident EIT and work-location nonresident EIT | Work-location nonresident EIT |
| Philadelphia | Resident rate wherever working | Nonresident rate on city work |

**Parameters (income tax withholding (state and local))**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `pa.pit.rate.flat` | [[FACT:pa.pit.rate.flat=3.07]] | % | from 2026-01-01 | US-PAS5-009 | residents all services; nonresidents PA services; no PA W-4, allowances or brackets; supplemental added to period |
| `pa.reciprocity.states` | [[FACT:pa.reciprocity.states=IN;MD;NJ;OH;VA;WV (REV-419)]] |  | from 2026-01-01 | US-PA-001 |  |
| `pa.pit.local.eit.rule` | [[FACT:pa.pit.local.eit.rule=withhold greater of resident EIT and work-location nonresident EIT (DCED register)]] |  | from 2018-05-04 | US-PAS5-017 |  |
| `pa.pit.local.eit.annual_due` | [[FACT:pa.pit.local.eit.annual_due=28 February (W2-R with PSD codes)]] |  | from 2018-05-04 | US-PAS5-017 | quarterly by last day of month after quarter |
| `pa.pit.local.lst.annual_cap` | [[FACT:pa.pit.local.lst.annual_cap=52]] | USD | from 2018-05-04 | US-PAS5-017 | pro rata per period rounded down to the cent; >10 levy exempts <12,000 earners |
| `pa.pit.local.lst.low_income_exemption` | [[FACT:pa.pit.local.lst.low_income_exemption=12,000]] | USD | from 2018-05-04 | US-PAS5-017 |  |
| `pa.local.philadelphia.resident.rate` | [[FACT:pa.local.philadelphia.resident.rate=3.74]] | % | 2025-07-01 to 2026-06-30 | US-PAS5-022 |  |
| `pa.local.philadelphia.resident.rate` | [[FACT:pa.local.philadelphia.resident.rate=3.735]] | % | from 2026-07-01 | US-PAS5-022 |  |
| `pa.local.philadelphia.nonresident.rate` | [[FACT:pa.local.philadelphia.nonresident.rate=3.43]] | % | 2025-07-01 to 2026-06-30 | US-PAS5-022 |  |
| `pa.local.philadelphia.nonresident.rate` | [[FACT:pa.local.philadelphia.nonresident.rate=3.425]] | % | from 2026-07-01 | US-PAS5-022 |  |
| `pa.pit.local.pittsburgh.payroll_expense.rate` | [[FACT:pa.pit.local.pittsburgh.payroll_expense.rate=0.55]] | % | from 2026-01-01 | US-PAB5-401 | employer |
| `pa.pit.rounding` | [[FACT:pa.pit.rounding=none published]] |  | from 2026-01-01 | US-PAP52-002 |  |

**Open research points**

- Not configured in this release [[GAP:RQ-302]]: Local EIT compensation base vs PA PIT and DCED register cadence not verified.

## PA.2b Non-resident regime and reciprocity

The non-resident and reciprocity rules of this jurisdiction are written in PA.2.

## PA.2c Local wage taxes

The local wage taxes of this jurisdiction, where any exist, are written in PA.2.

## PA.3 Social insurance: unemployment, disability, paid leave and payroll levies

- **Unemployment compensation (DLI) [US-PAS5-019, US-PA-009, US-PA-007].** Employer taxable wage base [[FACT:pa.sui.wage_base=10,000]] USD per employee per year, fixed by statute (UC Law 4(x)(1)), not indexed. 2026 new-employer rate [[FACT:pa.sui.new_employer.rate=3.822]] % (construction [[FACT:pa.ui.rate.new_employer.construction=10.5924]] %); computed experience range [[FACT:pa.sui.employer.rate.min=1.419]] % to [[FACT:pa.sui.employer.rate.max=10.3734]] %. Surcharge and additional contributions are included in the published rates.
- **Employee UC contribution:** [[FACT:pa.sui.employee.rate=0.07]] % of all gross wages, with no cap, withheld in trust (UC Law 301.4) and rounded to the cent [US-PAS5-019, US-PAP52-003].
- **SDI, TDI, PFML:** none (exists: [[FACT:pa.sdi_pfml.exists=False]]) [US-PAL-002]. Employer levies per the levy census [US-OWN-007].

**Parameters (social insurance and payroll levies)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `pa.sui.wage_base` | [[FACT:pa.sui.wage_base=10,000]] | USD | from 2018-01-01 | US-PAS5-019 | UC Law 4(x)(1) fixed, not indexed |
| `pa.sui.new_employer.rate` | [[FACT:pa.sui.new_employer.rate=3.822]] | % | 2026-01-01 to 2026-12-31 | US-PA-009 | Non-construction. Rate published in decimal form .038220 (= [[FACT:pa.sui.new_employer.rate=3.822]]%). |
| `pa.ui.rate.new_employer.construction` | [[FACT:pa.ui.rate.new_employer.construction=10.5924]] | % | 2026-01-01 to 2026-12-31 | US-PA-009 | Rate published in decimal form .105924 (= [[FACT:pa.ui.rate.new_employer.construction=10.5924]]%). |
| `pa.sui.employer.rate.min` | [[FACT:pa.sui.employer.rate.min=1.419]] | % | 2026-01-01 to 2026-12-31 | US-PA-009 |  |
| `pa.sui.employer.rate.max` | [[FACT:pa.sui.employer.rate.max=10.3734]] | % | 2026-01-01 to 2026-12-31 | US-PA-009 | Includes the surcharge and the additional contribution. Rate published in decimal form .103734 (= [[FACT:pa.sui.employer.rate.max=10.3734]]%). |
| `pa.sui.employee.rate` | [[FACT:pa.sui.employee.rate=0.07]] | % | from 2023-01-01 | US-PAS5-019 | on ALL gross wages, no cap; rounded to cent |
| `pa.sdi_pfml.exists` | [[FACT:pa.sdi_pfml.exists=False]] |  | from 2026-01-01 | US-PAL-002 |  |

## PA.4 Pay statement

- **Content (34 Pa. Code 231.36) [US-PAP51-001]:** [[FACT:pa.payslip.items=hours worked, rates, gross, allowances toward minimum wage, deductions, net]]; the DLI FAQ adds tax and other deductions and the pay-period dates [US-PAS5-003]. Retention [[FACT:pa.records.retention_years=3]] years [US-PAS5-002]. No PA rule on electronic delivery located (open point in Section 1).

**Parameters (payslip statute and payroll records)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `pa.records.retention_years` | [[FACT:pa.records.retention_years=3]] | years | from 2009-07-24 | US-PAS5-001 | MWA Sec. 8 |
| `pa.payslip.items` | [[FACT:pa.payslip.items=hours worked, rates, gross, allowances toward minimum wage, deductions, net]] |  | from 2026-01-01 | US-PAP51-001 | 34 Pa. Code 231.36 with every payment |

## PA.5 Statutory reporting

- **Withholding (DOR, myPATH) [US-PAS5-009, US-PAS5-010]:** deposits quarterly, monthly, semi-monthly or semi-weekly by amount; quarterly return; annual reconciliation REV-1667 with W-2s due [[FACT:pa.report.rev1667.due=31 January (with W-2s; electronic for 10+)]]; uploads in PA W-2 EFW2 or CSV. 1099 withholding on a separate account.
- **UC quarterly (DLI, UCMS) [US-PAS5-013]:** UC-2 and UC-2A due [[FACT:pa.report.ui.quarterly_due=Apr 30; Jul 31; Oct 31; Jan 31]]; zero report required; online filing mandatory; a credit week is a week with remuneration of at least [[FACT:pa.report.ui.credit_week.amount=116]] USD. File layouts UC-2010 ICESA / CSV [US-FIL-008].
- **New hire [US-PAS5-008]:** within [[FACT:pa.newhire.report_days=20]] days of hire, or two monthly electronic transmissions.
- **Local:** EIT and LST quarterly returns and the annual W2-R to the collector [US-PAS5-017, US-PAS5-018]; Philadelphia quarterly returns [US-PAS5-022].
- **Third-party authorisation:** REV-677 (DOR); UCMS TPA handshake (UC) [US-PAP51-004, US-FIL-010].

**Parameters (statutory reporting)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `pa.report.rev1667.due` | [[FACT:pa.report.rev1667.due=31 January (with W-2s; electronic for 10+)]] |  | from 2026-01-01 | US-PAS5-010 | myPATH EFW2 or CSV |
| `pa.report.ui.quarterly_due` | [[FACT:pa.report.ui.quarterly_due=Apr 30; Jul 31; Oct 31; Jan 31]] |  | from 2023-09-01 | US-PAS5-013 |  |
| `pa.report.ui.credit_week.amount` | [[FACT:pa.report.ui.credit_week.amount=116]] | USD | from 2023-09-01 | US-PAS5-013 |  |
| `pa.newhire.report_days` | [[FACT:pa.newhire.report_days=20]] | days | from 2026-01-01 | US-PAS5-008 |  |

## PA.6 Leave

- **State:** no statewide paid sick leave (statewide law: [[FACT:pa.leave.paid_sick.statewide=False]]); vacation, holiday and severance follow policy and become wages once promised (WPCL) [US-PAS5-003, US-PAS5-005].
- **Philadelphia (Code ch. 9-4100) [US-PAS5-015]:** paid sick time where the employer has at least [[FACT:pa.leave.philadelphia.employer_threshold=10]] employees; accrual and use capped at [[FACT:pa.leave.philadelphia.annual_cap_hours=40]] hours per year; carry-over unless front-loaded; rehire within the statutory period restores the balance. The accrual rate is open (below).
- **Pittsburgh Paid Sick Days Act (from 2026-01-01) [US-PAB5-402]:** one hour per [[FACT:pa.leave.pittsburgh.accrual.hours_worked_per_hour=30]] hours worked in Pittsburgh, all employers; annual cap [[FACT:pa.leave.pittsburgh.annual_cap_hours.15plus=72]] hours for employers with 15 or more employees and [[FACT:pa.leave.pittsburgh.annual_cap_hours.under15=48]] hours below; use from day [[FACT:pa.leave.pittsburgh.waiting_period_days=90]] of employment; payout at separation: [[FACT:pa.leave.pittsburgh.payout_at_separation=False]]. Rule: [[FACT:pa.leave.pittsburgh.rule=Carryover required unless the employer front-loads 72 h (15+) / 48 h (<15) at the start of each year; reinstated on rehire within 6 months; paid at the same base rate and benefits, never below the PA minimum wage; no pay for lost tips or commissions]].

**Parameters (leave)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `pa.leave.paid_sick.statewide` | [[FACT:pa.leave.paid_sick.statewide=False]] |  | from 2026-01-01 | US-PAS5-003 | policy-based; Philadelphia and Pittsburgh ordinances |
| `pa.leave.philadelphia.employer_threshold` | [[FACT:pa.leave.philadelphia.employer_threshold=10]] |  | from 2016-04-13 | US-PAS5-015 | Max 40 h/yr; covered if 40+ h/yr in city; partly confirmed by the published source (accrual rate not confirmed by an official source). |
| `pa.leave.philadelphia.annual_cap_hours` | [[FACT:pa.leave.philadelphia.annual_cap_hours=40]] | hours | from 2016-04-13 | US-PAS5-015 | Partly confirmed by the published source. |
| `pa.leave.pittsburgh.accrual.hours_worked_per_hour` | [[FACT:pa.leave.pittsburgh.accrual.hours_worked_per_hour=30]] | hours | from 2026-01-01 | US-PAB5-402 | 1 hour of paid sick time per 30 hours worked in Pittsburgh, all employers with 1+ employees; FLSA-exempt staff assumed 40 h/week. |
| `pa.leave.pittsburgh.annual_cap_hours.15plus` | [[FACT:pa.leave.pittsburgh.annual_cap_hours.15plus=72]] | hours | from 2026-01-01 | US-PAB5-402 | Cap per calendar year and on access, employers with 15+ employees, unless the employer sets a higher cap. |
| `pa.leave.pittsburgh.annual_cap_hours.under15` | [[FACT:pa.leave.pittsburgh.annual_cap_hours.under15=48]] | hours | from 2026-01-01 | US-PAB5-402 |  |
| `pa.leave.pittsburgh.waiting_period_days` | [[FACT:pa.leave.pittsburgh.waiting_period_days=90]] | days | from 2026-01-01 | US-PAB5-402 | Use from the 90th calendar day of employment. |
| `pa.leave.pittsburgh.payout_at_separation` | [[FACT:pa.leave.pittsburgh.payout_at_separation=False]] |  | from 2026-01-01 | US-PAB5-402 |  |
| `pa.leave.pittsburgh.rule` | [[FACT:pa.leave.pittsburgh.rule=Carryover required unless the employer front-loads 72 h (15+) / 48 h (<15) at the start of each year; reinstated on rehire within 6 months; paid at the same base rate and benefits, never below the PA minimum wage; no pay for lost tips or commissions]] |  | from 2026-01-01 | US-PAB5-402 |  |

**Open research points**

- Not configured in this release [[GAP:RQ-300]]: The Philadelphia accrual rate rests on a secondary source only; the ordinance text was not reached.

## PA.7 Termination and final pay

- **Final pay (WPCL Sec. 5(a)) [US-PAS5-005, US-PAS5-003]:** [[FACT:pa.final_pay.rule=next regular payday (any separation)]]; by certified mail on request; liquidated damages on late wages.
- **Accrued vacation:** [[FACT:pa.term.vacation.payout=only if policy or contract promises]] [US-PAS5-003].
- **UC availability notice at separation (UC Law Sec. 206.1):** required ([[FACT:pa.term.uc_notice.required=True]]); form UC-1609 recommended, other formats allowed [US-PAS5-014]. No state WARN located.

**Parameters (termination)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `pa.final_pay.rule` | [[FACT:pa.final_pay.rule=next regular payday (any separation)]] |  | from 1977-07-14 | US-PAS5-005 | WPCL Sec. 5(a); liquidated damages 25% or 500 |
| `pa.term.vacation.payout` | [[FACT:pa.term.vacation.payout=only if policy or contract promises]] |  | from 2026-01-01 | US-PAS5-003 |  |
| `pa.term.uc_notice.required` | [[FACT:pa.term.uc_notice.required=True]] |  | from 2024-08-01 | US-PAS5-014 | UC Law 206.1; form UC-1609 recommended |

## PA.8 Benefits in kind and taxable wages

- **PA PIT departs from federal [US-PAS5-011]:**
  - employee deferrals to 401(k), 403(b) and 457(b) are taxable when made: [[FACT:pa.bik.pa.401k_403b_457.taxable=True]];
  - cafeteria-plan salary reductions for dependent care are taxable: [[FACT:pa.bik.pa.dependent_care_125.taxable=True]] (health, accident, disability and life reductions are excluded as federally);
  - employer-paid group-term life is taxable: [[FACT:pa.bik.pa.group_term_life.taxable=False]] (no imputed income at any amount);
  - personal use of employer property, employer parking, meals and lodging are nontaxable fringes.
- **HSA:** PA follows the federal rules as a deduction [US-PAS5-012]; treatment at withholding open (below). Local EIT base: open (below).

**Parameters (benefits in kind and the taxable base)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `pa.bik.pa.401k_403b_457.taxable` | [[FACT:pa.bik.pa.401k_403b_457.taxable=True]] |  | from 2026-01-01 | US-PAS5-011 | employee deferrals taxable for PA PIT |
| `pa.bik.pa.dependent_care_125.taxable` | [[FACT:pa.bik.pa.dependent_care_125.taxable=True]] |  | from 2026-01-01 | US-PAS5-011 |  |
| `pa.bik.pa.group_term_life.taxable` | [[FACT:pa.bik.pa.group_term_life.taxable=False]] |  | from 2026-01-01 | US-PAS5-011 | no 50,000 imputed income |

**Open research points**

- Not configured in this release [[GAP:RQ-301]]: HSA salary reductions at PA withholding (exclude vs employee deduction) open.

## PA.9 Deductions and garnishments

- **Wage deductions:** limited to the 34 Pa. Code 9.1 list, each with a written authorisation; no blanket authorisation at hire; never below minimum wage [US-PAS5-006, US-PAS5-003].
- **Wage attachment is narrower than the CCPA (42 Pa.C.S. 8127) [US-PAS5-007]:** ordinary consumer-creditor garnishment available: [[FACT:pa.garn.consumer.available=False]]. Wages are attachable only for support, divorce, short boarding debts, residential-lease judgments (at most [[FACT:pa.garn.lease_judgment.max_rate=10]] % of net wages, or the poverty-guideline floor if less), PHEAA loans and criminal restitution. Support has first priority, restitution second. IWO specifics and state tax levies: open (below).

**Parameters (deductions and garnishments)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `pa.garn.consumer.available` | [[FACT:pa.garn.consumer.available=False]] |  | from 2026-01-01 | US-PAS5-007 | 42 Pa.C.S. 8127: only support, divorce, board, residential lease (max 10% net), PHEAA, restitution |
| `pa.garn.lease_judgment.max_rate` | [[FACT:pa.garn.lease_judgment.max_rate=10]] | % | from 2026-01-01 | US-PAS5-007 | of net wages or poverty floor |

**Open research points**

- Not configured in this release [[GAP:RQ-303]]: PA DOR administrative wage levy not established from an official source.
- Not configured in this release [[GAP:RQ-305]]: Child-support IWO fee and SCDU remittance not read.

## PA.10 Collective agreements and prevailing wage

- **Prevailing Wage Act [US-PAP51-003, US-PAP51-006]:** public works above [[FACT:pa.prevailing_wage.threshold=25,000]] USD (DLI Bureau of Labor Law Compliance). Certified payroll: open (below).

**Parameters (collective agreements and prevailing wage)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `pa.prevailing_wage.threshold` | [[FACT:pa.prevailing_wage.threshold=25,000]] | USD | from 2026-01-01 | US-PAP51-003 | PA Prevailing Wage Act |

**Open research points**

- Not configured in this release [[GAP:RQ-304]]: Certified payroll form/frequency not read.

## PA.11 Indexation

- **Nothing in PA payroll indexes automatically.** The minimum wage follows the FLSA by statute; the UC employer base is fixed; the employee UC rate is set yearly under UC Law 301.7; employer UC rates are published yearly (UC-748) [US-PA-007, US-PA-009]; the LST cap and the PIT rate are statutory; Philadelphia sets wage-tax rates every July 1 [US-PAS5-022]; EIT rates are published in the DCED register.

## PA.12 Payroll data protection and records

- **SSN Privacy Law (Act 60 of 2006) [US-PAS5-020]:** no public display, no SSN on access cards, secure transmission, no SSN on mailed materials unless required; no pay-stub truncation rule, so mailed pay stubs omit the SSN.
- **Breach Notification Act [US-PAS5-021]:** notify without unreasonable delay; above [[FACT:pa.data.breach.ag_threshold=500]] affected residents, notify the Attorney General and credit reporting agencies; credit monitoring where SSN, bank or ID numbers are breached (Act 33 of 2024).

**Parameters (payroll data protection)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `pa.data.breach.ag_threshold` | [[FACT:pa.data.breach.ag_threshold=500]] |  | from 2024-09-26 | US-PAS5-021 | 12 months credit monitoring where SSN/bank/ID breached |

## PA.13 Live legal change

- **Act 55 of 2025 (UC Law, domestic-violence eligibility):** benefit side and employer account charging only; no payroll calculation change [US-PAS5-019].
- **2026-01-01:** Pittsburgh Paid Sick Days Act: higher accrual and caps [US-PAB5-402].
- **2026-07-01:** Philadelphia wage tax rates (Section 2) [US-PAS5-022]; further cuts announced but not published.
- **Minimum-wage bill:** passed by the House, not acted on by the Senate; not enacted (open point below).

**Open research points**

- Not configured in this release [[GAP:RQ-306]]: Not established from an official source.

## PA.14 Authority worked examples (oracle values)

No authority worked example is reproduced in this annex; recomputed withholding examples are in Module 12.

## PA.15 Special populations

| Population | Pennsylvania rule | Register id |
|---|---|---|
| Domestic / household | Exempt from MWA minimum wage and overtime (Sec. 5(a)(2)); UC only above a quarterly cash test; PA withholding not required when not an employee federally; household pay is PA-taxable to the worker | US-PAS5-001, US-PAS5-019, US-PA-001, US-PAS5-011 |
| Agricultural | Farm labour exempt from the MWA (Sec. 5(a)(1)); UC excludes agricultural labour except covered farms; no PA withholding where FICA does not apply (H-2A may elect) | US-PAS5-001, US-PAS5-019, US-PA-001 |
| Minors | Mandatory meal break for minors; training wage for young workers for an initial period; UC excludes a minor child working for a parent; Child Labor Act not read | US-PAS5-003, US-PAS5-001, US-PAS5-019 |
| Tipped | Cash wage and tip threshold per Section 1; tips paid through the employer are withheld; tips received directly are reported, not withheld | US-PAS5-002, US-PAS5-004, US-PA-001 |
| Clergy / religious | No PA withholding where federal withholding does not apply; cash housing allowance taxable, parsonage value exempt; church service excluded from UC | US-PA-001, US-PAS5-011, US-PAS5-019 |
| Students | Special certificates (sub-minimum, weekly hours cap); seasonal students may be excluded from overtime; UC excludes own-school and some camp students | US-PAS5-001, US-PAS5-002, US-PAS5-019 |
| Nonresident aliens | Same flat rate; exempt only when a PA-resident NRA works outside the US | US-PA-001 |
| Statutory employees | No PA withholding; amounts reported on the W-2 | US-PA-001 |
| Government employees | Government bodies withhold PA tax; MWA excludes elected officials and their policy staff; federal service excluded from PA UC | US-PA-001, US-PAS5-001, US-PAS5-019 |

## PA.16 Language

No language rule for employee documents is written for this jurisdiction in this annex.

## PA.S Sources

Register ids cited in this annex resolve to the build record; the URL of each value is in the facts file. Authorities:

- Build lead (Claude) under owner delegation (Wallisson Gomes): US-OWN-006, US-OWN-007
- City of Philadelphia Department of Revenue: US-PAS5-022
- City of Philadelphia, Office of the Managing Director (filed with Department of Records): US-PAS5-015
- City of Pittsburgh (Office of Equal Protection, Law Department): US-PAB5-402
- Owner (Wallisson Gomes): US-OWN-008
- PA Department of Labor & Industry - Office of UC Tax Services: US-PAP51-004, US-PAP52-003
- PA Department of Revenue: US-FIL-010, US-PA-008
- PA Dept of Community & Economic Development: US-PA-004
- PA Dept of Labor and Industry: US-FIL-008, US-PA-007, US-PA-009
- PA official authority: US-PAB5-401
- Pennsylvania Code & Bulletin (Department of Labor and Industry regulations): US-PAS5-002
- Pennsylvania Code & Bulletin (Department of Labor and Industry): US-PAS5-006
- Pennsylvania Code (PA Bulletin): US-PAP51-001, US-PAP52-002
- Pennsylvania DOR: US-MULTI-007
- Pennsylvania Department of Community & Economic Development: US-PAS5-018
- Pennsylvania Department of Labor and Industry: US-PAS5-004
- Pennsylvania Department of Labor and Industry, Bureau of Labor Law Compliance: US-PAS5-003
- Pennsylvania Department of Labor and Industry, Office of UC Benefits: US-PAS5-014
- Pennsylvania Department of Labor and Industry, Office of UC Tax Services: US-PAS5-013
- Pennsylvania Department of Revenue: US-PA-001, US-PAL-002, US-PAS5-009, US-PAS5-010, US-PAS5-011, US-PAS5-012
- Pennsylvania General Assembly: US-PAS5-005, US-PAS5-017, US-PAS5-019, US-PAS5-020, US-PAS5-021
- Pennsylvania General Assembly (Legislative Reference Bureau): US-PAS5-001
- Pennsylvania General Assembly (palegis.us consolidated statutes): US-PAS5-007, US-PAS5-008
- Pennsylvania General Assembly; administered by Dept of Labor & Industry (Bureau of Labor Law Compliance): US-PAP51-003
- US Department of Labor Wage and Hour Division: US-PAP51-006
