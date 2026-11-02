## @labour
- **Minimum wage (RIGL 28-12-3) [US-RIS5-001].** Fixed statutory steps, not indexed:

| From | Rate |
|---|---|
| 2025-01-01 | {{ri.minwage.hourly@2025-01-01}} USD |
| 2026-01-01 | {{ri.minwage.hourly@2026-01-01}} USD |
| 2027-01-01 (enacted, P.L. 2025 ch. 222/223) | {{ri.minwage.hourly@2027-01-01}} USD |

- **Local minimum wages:** none located (municipalities cannot levy income-based taxes and no municipal wage ordinance was found; this rests on absence of a find) [US-RIP52-001].
- **Minors and students [US-RIS5-002]:** minors aged 14-15 at least {{ri.labour.minwage.minor_14_15.ratio}} % of the minimum (full minimum in weeks above the statutory hours) (28-12-3.1); full-time students working for nonprofit religious, educational, library or community-service employers at least {{ri.labour.minwage.student_nonprofit.ratio}} % (28-12-5(f)).
- **Tipped employees [US-RIS5-002]:** cash wage at least {{ri.minwage.tipped.cash_wage}} USD per hour (not taxicabs); the tip credit is the minimum wage minus the cash wage.
- **Overtime (28-12-4.1 ff.) [US-RIS5-003]:** {{ri.overtime.premium.multiplier}} times the regular rate above {{ri.overtime.weekly_threshold_hours}} hours a week; no daily overtime; fluctuating workweek barred for delivery drivers and sales merchandisers; retail Sunday and holiday premium hours (5-23-2) excluded from the weekly count; exemptions in 28-12-4.3.
- **Pay frequency (28-14-2.2) [US-RIS5-004]:** {{ri.pay_frequency.rule}}; DLT may approve less-than-weekly pay on petition with a surety bond; payday changes need advance notice.
- **Method of payment [US-RIS5-005]:** {{ri.payment.method}}; free balance inquiry.
- **Deduction remittance [US-RIS5-007]:** payroll deductions paid over within {{ri.deduction.remittance_days}} days after the end of the month in which they were taken.

## @income_tax
- **Method (2026 booklet) [US-RIS5-019]:** {{ri.wh.method}}.

| Annual taxable wages | Withholding |
|---|---|
| up to {{ri.pit.bracket.1.ceiling}} USD | {{ri.pit.bracket.1.rate}} % |
| above that, up to {{ri.pit.bracket.2.ceiling}} USD | {{ri.pit.bracket.2.base_tax}} USD + {{ri.pit.bracket.2.rate}} % of the excess over the first ceiling |
| above the second ceiling | {{ri.pit.bracket.3.base_tax}} USD + {{ri.pit.bracket.3.rate}} % of the excess over the second ceiling |

  Per-period tables are the annual table divided by the number of periods (published in the booklet).
- **Exemption allowance:** {{ri.pit.exemption.annual}} USD per year per exemption, falling to zero when annualised wages exceed {{ri.pit.exemption.cliff.annual_wages}} USD (a cliff, not a phase-out) [US-RIS5-019].
- **Oracle:** booklet worked example (weekly, one exemption): {{ri.pit.oracle.example_1.withholding}} USD, reproduced exactly. Recomputation in Module 12.
- **Certificate:** {{ri.wh.certificate}} [US-RIS5-019].
- **Supplemental wages:** flat {{ri.wh.supplemental.rate}} % (booklet instruction 12) or the aggregate method; the older register row giving a different instruction is superseded [US-RIS5-019].
- **Rounding:** no rule stated; the tables work to the cent.
- **Who withholds [US-RIP52-003, US-RIS5-019]:** wages subject to federal withholding where any part is for services in Rhode Island; nonresidents working in Rhode Island; out-of-state employers may withhold for residents as a convenience. Reciprocity: {{ri.reciprocity.states}}; no day or dollar threshold; no convenience-of-employer rule found. Residents claim a credit for tax paid to another state on Schedule II [US-RIP52-002].
- **Local income taxes:** none (exists: {{ri.local_wage_tax.exists}}) [US-RIP52-001].
- **Conformity:** RI starts from federal AGI with Schedule M modifications and decoupled from federal H.R. 1 in the FY2026 budget; the 2026 withholding method is unchanged by that decoupling [US-RIS5-023].
- **Resident and nonresident matrix.**

| Income type | Rhode Island resident | Nonresident |
|---|---|---|
| Regular salary | Booklet tables, all wages subject to federal withholding | Booklet tables on wages for services in Rhode Island |
| Bonus / supplemental | Flat {{ri.wh.supplemental.rate}} % or aggregate | Same, Rhode Island share |
| Severance, equity, benefits in kind | Follow federal wages (RI withholds where federal withholding applies) | Same, Rhode Island share |
| Military spouse | EXEMPT-MS on the RI W-4 (renewed yearly) | Same |

## @social
- **Unemployment insurance (DLT Employer Tax Unit) [US-RIP9V-001, US-RIP7-001].** 2026 taxable wage base {{ri.sui.wage_base}} USD; employers at the highest rate pay on {{ri.ui.wage_base.highest_rate}} USD. Experience range {{ri.sui.employer.rate.min}} % to {{ri.sui.employer.rate.max}} %, each reduced to offset the employer Job Development Assessment of {{ri.ui.jda.rate}} %. New employer {{ri.sui.new_employer.rate}} % (JDA included). Employee UI contribution {{ri.sui.employee.rate}} %.
- **Wage-base indexation (28-43) [US-RIS5-014]:** a share of the prior-year average annual wage, rounded up; the highest-rate base adds a fixed statutory amount.
- **Other-state wages count toward the base:** {{ri.sui.wage_base.other_state_credit}} [US-RIS5-013].
- **TDI / TCI (employee-only) [US-RIP9V-001, US-RIS5-015]:** 2026 rate {{ri.tdi.employee.rate}} % on wages up to {{ri.tdi.wage_base.annual}} USD, so the annual maximum is {{ri.tdi.employee.max_annual}} USD. Coverage test: {{ri.tdi.coverage_test}} [US-RIS5-016]. TDI not deducted on time is recoverable from later pay: {{ri.tdi.late_deduction.recoverable}}; the employer becomes liable (28-40-4) [US-RIS5-017].
- **UI and TDI wages exclude employee 401(k) and cafeteria-plan contributions:** {{ri.ui_tdi.wages.401k_section125_excluded}} [US-RIS5-017]. This departs from FUTA (Annex FED).
- **No separate PFML programme** beyond TCI; no other levy beyond JDA and TDI [US-RIP9V-002, US-OWN-007].

## @payslip
- **Content (28-14-2.1) [US-RIP51-002]:** {{ri.payslip.items}}. Electronic statement allowed; free printed copy on written request; no language clause [US-RIL-001].
- **Records:** the record-keeping section was replaced from 2026-01-01; the new text and retention period are unconfirmed (blocking open point below) [US-RIS5-008].
- **Reach:** no territorial clause; default applies to employees working in Rhode Island.

## @reporting
- **Two institutions, two portals [US-RIS5-024]:** the Division of Taxation (withholding) and DLT (UI, TDI, JDA). Do not mix them.
- **Division of Taxation [US-RIS5-018, US-RIS5-019]:** weekly electronic deposits once withholding reaches {{ri.report.wh.weekly_threshold.monthly}} USD a month (smaller employers deposit monthly or quarterly); RI-941 quarterly return due {{ri.report.ri941.due}}; RI W-3 annual reconciliation due {{ri.report.w3.due}}; W-2 to Rhode Island in EFW2 through the Tax Portal, mandatory electronic for employers that e-file with SSA and have {{ri.report.w2.efile_threshold}} or more RI employees or claim an RI credit.
- **DLT Employer Tax Unit [US-RIS5-017]:** TX-17 Quarterly Tax and Wage Report (one report and payment for UI, TDI and JDA) due {{ri.report.tx17.due}}; zero report required; electronic wage data mandatory above the employee threshold; registration on the BAR form; PEOs and common paymasters not recognised.
- **New hire [US-RIS5-010, US-RIS5-011]:** within {{ri.newhire.report_days}} days of hire or rehire to the RI State Directory of New Hires; multistate employers may designate one state. Statutory field list: open point below.
- **Power of attorney:** RI-2848 [US-RIP51-004].

## @leave
- **Paid sick and safe leave (RIGL 28-57) [US-RIS5-009]:** employers with {{ri.leave.paid_sick.employer_threshold}} or more employees in Rhode Island; accrual one hour per {{ri.leave.paid_sick.accrual_ratio_hours_worked}} hours worked, up to {{ri.leave.paid_sick.annual_cap_hours}} hours a year (accrual and use). Carry-over or year-end payout with front-loading; statutory waiting periods; payout at separation: {{ri.leave.sick.payout_on_separation}}; reinstatement on rehire within the statutory period. Smaller employers owe the same hours unpaid. Municipal and state employees excluded.
- **TCI (insurance-paid family leave) [US-RIS5-021]:** job restoration and continued health benefits; the week cap is unsettled (open point below); it affects benefits only, not the payroll deduction.

## @termination
- **Final pay (28-14-4) [US-RIS5-006]:** {{ri.final_pay.rule}}.
- **Accrued vacation:** payable at separation after {{ri.term.vacation.payout_after_years}} year of service if accrued or awarded under a CBA, policy or agreement. Paid sick leave is not paid out [US-RIS5-009]. Public-employee comp time is paid at termination [US-RIS5-003].

## @bik
- **Income tax:** federal exclusions carry through from federal AGI; no Schedule M addition found for them; H.R. 1 decoupling items not itemised (open point below) [US-RIP52-002, US-RIS5-023].
- **UI and TDI:** employee contributions to retirement, medical and disability plans and cafeteria plans are excluded from UI and TDI wages (Section 3) [US-RIS5-017].

## @deductions
- **Wage exemption (9-26-4(8)) [US-RIS5-012]:** the state exempt amount for ordinary wages is {{ri.garn.consumer.state_exempt_amount}} USD, less protective than the CCPA, so the federal limits govern ordinary garnishment (Annex FED); debtors on public relief are fully exempt for a period after relief ends.
- **Child support:** e-IWO accepted; fees and priority not read (open point below).

## @cba
- **Prevailing wage [US-RIP51-003, US-RIP51-005]:** public works contracts above {{ri.prevailing_wage.threshold}} USD must state the prevailing wages set by the DLT director, paid weekly. Certified-payroll mechanics not read.

## @indexation
- **Minimum wage:** fixed statutory steps, not indexed [US-RIS5-001].
- **UI wage base:** share of the prior-year average annual wage, rounded up, published each December [US-RIS5-014].
- **TDI wage base and rate:** formula base and fund cost rate set by 15 November [US-RIS5-015].
- **PIT brackets and exemption cut-off:** annual booklet [US-RIS5-019]. **Tipped cash wage:** fixed since 2017 [US-RIS5-002]. The 2027 booklet and DLT release are not yet published (open point below).

## @data
- **SSN (6-48-8) [US-RIS5-020]:** no part of an SSN on material mailed to the individual unless law requires it ({{ri.data.ssn.mailed_prohibited}}); no public display; no requirement over an unsecured connection. A mailed pay statement carries no part of the SSN.

## @live
- **2026-01-01:** minimum wage step; new record-keeping / hiring-notice section 28-14-12 (text unread); TDI rate and base, UI base and schedule change [US-RIS5-001, US-RIS5-008, US-RIP9V-001].
- **2025-12-15:** PIT emergency regulation 280-RICR-20-55-16; RI decoupled from H.R. 1 [US-RIS5-023].
- **2027-01-01 (enacted):** minimum wage step [US-RIS5-001].
- **Sweep limit:** DLT news and the 2026 public laws were not read (rilegislature.gov unreachable).

## @special
| Population | Rhode Island rule | Register id |
|---|---|---|
| Domestic / household | UI and TDI above a quarterly cash test; minimum wage applies | US-RIS5-022, US-RIS5-017 |
| Agricultural | Exempt from state overtime (28-12-4.3(a)(9)); UI coverage of farm work not confirmed | US-RIS5-003, US-RIS5-022 |
| Minors | Sub-minimum per Section 1; a minor child employed by a parent sole proprietor is excluded from UI and TDI | US-RIS5-002, US-RIS5-022 |
| Tipped | Cash wage {{ri.minwage.tipped.cash_wage}} USD; tip credit up to the minimum | US-RIS5-002 |
| Clergy / religious | Churches, ministers and religious orders excluded from UI and TDI; income tax follows federal withholding | US-RIS5-022, US-RIS5-019 |
| Students | Co-op students in credit programmes excluded from UI and TDI; nonprofit student sub-minimum per Section 1 | US-RIS5-022, US-RIS5-002 |
| Nonresident aliens | RI withholding applies where federal withholding applies | US-RIS5-019 |
| Statutory employees | No state rule beyond federal; commission-only real-estate and insurance agents excluded from UI and TDI | US-RIS5-022 |
| Government employees | Federal and other-state employment excluded from RI UI; state and municipal employees excluded from paid sick leave and the weekly-pay rule | US-RIS5-022, US-RIS5-009, US-RIS5-004, US-RIS5-003 |

## @gaps
- ri.records.2026_version :: The new record-keeping and hiring-notice section 28-14-12 (effective 2026-01-01) was not read; the 2026 retention period and notice fields are unconfirmed. :: Official section text (browser pass with VPN) or P.L. 2025 chapter text for H 5679.
- ri.leave.tci.max_weeks :: The TCI maximum number of weeks is not settled at tier A (sources disagree). :: Current 28-41-35 text or DLT TDI/TCI program page.
