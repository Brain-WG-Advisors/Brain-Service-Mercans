## @labour
- **Minimum wage (MWA Sec. 4(a.1); 34 Pa. Code 231.101a) [US-PAS5-001, US-PAS5-002]:** {{pa.minwage.hourly}} USD per hour statewide; the state rate rises automatically to any higher FLSA rate. Not indexed; nothing enacted for 2027 (pending bills are not law; Section 13).
- **Local minimum wage:** preempted (MWA Sec. 14.1): {{pa.local_mandates.preempted}} [US-PAS5-001].
- **Tipped employees [US-PAS5-002, US-PAS5-004]:** cash wage {{pa.minwage.tipped.cash_wage}} USD per hour, the employer making up any shortfall to the minimum wage; a tipped employee customarily receives more than {{pa.labour.tip_credit.monthly_tip_threshold}} USD per month in tips (231.1); written notice of the tip credit (231.34); no deduction of card-processing fees from tips.
- **Overtime [US-PAS5-001, US-PAS5-003]:** {{pa.overtime.premium.multiplier}} times the regular rate over {{pa.overtime.weekly_threshold_hours}} hours per workweek; the 8-and-80 system is allowed for hospitals; no daily overtime; comp time in lieu of overtime is not legal. **Departure from the FLSA:** salaried non-exempt regular rate = {{pa.labour.overtime.salaried_nonexempt_regular_rate}} (231.43(g)) [US-PAS5-002].
- **Exempt salary level:** {{pa.exempt.salary.weekly_min}} USD per week with the federal duties tests (the PA-specific salary sections are abrogated) [US-PAS5-003].
- **Pay timing (WPCL Sec. 3(a)) [US-PAS5-005]:** {{pa.labour.pay_timing}}; notice at hire of payday, place and rate (Sec. 4).
- **Method of payment:** "lawful money of the United States or check" (WPCL Sec. 3); {{pa.payment.method}} [US-PAV6B-002].
- **Records:** {{pa.records.retention_years}} years (MWA Sec. 8; 231.31) [US-PAS5-001, US-PAS5-002].
- **Child labour (Act 151 of 2012) [US-PAV6B-010]:** {{pa.labour.child_labour}}.

## @income_tax
- **State PIT [US-PAS5-009, US-PA-001, US-PA-008]:** flat {{pa.pit.rate.flat}} % on compensation, for residents (services in or outside Pennsylvania) and nonresidents (services in Pennsylvania). Method: compensation of the payroll period times the rate; no PA W-4, no allowances, no brackets. Supplemental pay is added to the current period. Rounding: {{pa.pit.rounding}} [US-PAP52-002]. No oracle is needed beyond the flat-rate product. No 2027 change located.
- **Reciprocity:** {{pa.reciprocity.states}} [US-PA-001, US-MULTI-007]. Residents get a credit for tax paid to another state; a foreign country does not count as a state [US-PAS5-012].
- **Not subject to PA withholding (DSM-12) [US-PA-001]:** agricultural and H-2A workers not subject to FICA (may elect), clergy not subject to federal withholding, domestic workers who are not employees federally, casual non-trade employees, foreign-government employees, PA-resident nonresident aliens working outside the US, statutory employees and minor newspaper carriers, federally exempt interstate transport workers.
- **Local income taxes (T4 layer).**
  - **Act 32 Earned Income Tax (Local Tax Enabling Act) [US-PAS5-017, US-PAS5-018]:** {{pa.pit.local.eit.rule}}. Rates come per address from the DCED Address Search Application (no static table); worksites include the residences of home-based employees; a residency certificate is collected at hire and on change of address; quarterly return and payment to each work location's tax officer; annual return due {{pa.pit.local.eit.annual_due}}. Temporary assignments follow the statutory day-count rule.
  - **Local Services Tax (LTEA 301.1, 312) [US-PAS5-017]:** capped at {{pa.pit.local.lst.annual_cap}} USD per person per year, collected pro rata per payroll period (annual levy / number of periods, rounded down to the cent) where the levy exceeds the statutory minimum; such a levy must exempt anyone earning under {{pa.pit.local.lst.low_income_exemption}} USD in the subdivision; mandatory exemptions for fully disabled veterans and reservists called to active duty; situs is the place of employment on the first day of each period.
  - **Philadelphia Wage Tax (Sterling Act; Act 32 does not apply) [US-PAS5-022]:**

| Period | Resident | Nonresident |
|---|---|---|
| 2025-07-01 to 2026-06-30 | {{pa.local.philadelphia.resident.rate@2025-07-01}} % | {{pa.local.philadelphia.nonresident.rate@2025-07-01}} % |
| from 2026-07-01 | {{pa.local.philadelphia.resident.rate@2026-07-01}} % | {{pa.local.philadelphia.nonresident.rate@2026-07-01}} % |

  Philadelphia: residents pay wherever they work; nonresidents pay on work in the city. Quarterly returns on the Philadelphia Tax Center; no annual reconciliation.
  - **Pittsburgh payroll expense tax** (employer): {{pa.pit.local.pittsburgh.payroll_expense.rate}} % [US-PAP7-005].
- **Resident and nonresident matrix.**

| Income type | PA resident | Nonresident |
|---|---|---|
| Regular salary | Flat {{pa.pit.rate.flat}} % on all compensation, wherever earned | Flat rate on PA-service compensation, unless resident of a reciprocity state (REV-419 on file) |
| Bonus / supplemental | Added to the period, same flat rate | Same, PA-service share |
| Retirement deferrals (401(k), 403(b), 457(b)) | Taxable when deferred (Section 8) | Same, PA-service share |
| Local EIT | Greater of resident EIT and work-location nonresident EIT | Work-location nonresident EIT |
| Philadelphia | Resident rate wherever working | Nonresident rate on city work |

## @social
- **Unemployment compensation (DLI) [US-PAS5-019, US-PA-009, US-PA-007].** Employer taxable wage base {{pa.sui.wage_base}} USD per employee per year, fixed by statute (UC Law 4(x)(1)), not indexed. 2026 new-employer rate {{pa.sui.new_employer.rate}} % (construction {{pa.ui.rate.new_employer.construction}} %); computed experience range {{pa.sui.employer.rate.min}} % to {{pa.sui.employer.rate.max}} %. Surcharge and additional contributions are included in the published rates.
- **Employee UC contribution:** {{pa.sui.employee.rate}} % of all gross wages, with no cap, withheld in trust (UC Law 301.4) and rounded to the cent [US-PAS5-019, US-PAP52-003].
- **SDI, TDI, PFML:** none (exists: {{pa.sdi_pfml.exists}}) [US-PAL-002]. Employer levies per the levy census [US-OWN-007].

## @payslip
- **Content (34 Pa. Code 231.36) [US-PAP51-001]:** {{pa.payslip.items}}; the DLI FAQ adds tax and other deductions and the pay-period dates [US-PAS5-003]. Retention {{pa.records.retention_years}} years [US-PAS5-002]. Where wages are paid to an account or a payroll card, the statement of earnings may be written or electronic (Act 161 of 2016; Section 1) [US-PAV6B-002].

## @reporting
- **Withholding (DOR, myPATH) [US-PAS5-009, US-PAS5-010]:** deposits quarterly, monthly, semi-monthly or semi-weekly by amount; quarterly return; annual reconciliation REV-1667 with W-2s due {{pa.report.rev1667.due}}; uploads in PA W-2 EFW2 or CSV. 1099 withholding on a separate account.
- **UC quarterly (DLI, UCMS) [US-PAS5-013]:** UC-2 and UC-2A due {{pa.report.ui.quarterly_due}}; zero report required; online filing mandatory; a credit week is a week with remuneration of at least {{pa.report.ui.credit_week.amount}} USD. File layouts UC-2010 ICESA / CSV [US-FIL-008].
- **New hire [US-PAS5-008]:** within {{pa.newhire.report_days}} days of hire, or two monthly electronic transmissions.
- **Local:** EIT and LST quarterly returns and the annual W2-R to the collector [US-PAS5-017, US-PAS5-018]; Philadelphia quarterly returns [US-PAS5-022].
- **Third-party authorisation:** REV-677 (DOR); UCMS TPA handshake (UC) [US-PAP51-004, US-FIL-010].

## @leave
- **State:** no statewide paid sick leave (statewide law: {{pa.leave.paid_sick.statewide}}); vacation, holiday and severance follow policy and become wages once promised (WPCL) [US-PAS5-003, US-PAS5-005].
- **Philadelphia (Code ch. 9-4100) [US-PAS5-015]:** paid sick time where the employer has at least {{pa.leave.philadelphia.employer_threshold}} employees; accrual and use capped at {{pa.leave.philadelphia.annual_cap_hours}} hours per year; carry-over unless front-loaded; rehire within the statutory period restores the balance. Accrual: {{pa.leave.philadelphia.accrual}} [US-PAV6B-003].
- **Pittsburgh Paid Sick Days Act (from 2026-01-01) [US-PAB5-001]:** one hour per {{pa.leave.pittsburgh.accrual.hours_worked_per_hour}} hours worked in Pittsburgh, all employers; annual cap {{pa.leave.pittsburgh.annual_cap_hours.15plus}} hours for employers with 15 or more employees and {{pa.leave.pittsburgh.annual_cap_hours.under15}} hours below; use from day {{pa.leave.pittsburgh.waiting_period_days}} of employment; payout at separation: {{pa.leave.pittsburgh.payout_at_separation}}. Rule: {{pa.leave.pittsburgh.rule}}.

## @termination
- **Final pay (WPCL Sec. 5(a)) [US-PAS5-005, US-PAS5-003]:** {{pa.final_pay.rule}}; by certified mail on request; liquidated damages on late wages.
- **Accrued vacation:** {{pa.term.vacation.payout}} [US-PAS5-003].
- **UC availability notice at separation (UC Law Sec. 206.1):** required ({{pa.term.uc_notice.required}}); form UC-1609 recommended, other formats allowed [US-PAS5-014]. No state WARN located.

## @bik
- **PA PIT departs from federal [US-PAS5-011]:**
  - employee deferrals to 401(k), 403(b) and 457(b) are taxable when made: {{pa.bik.pa.401k_403b_457.taxable}};
  - cafeteria-plan salary reductions for dependent care are taxable: {{pa.bik.pa.dependent_care_125.taxable}} (health, accident, disability and life reductions are excluded as federally);
  - employer-paid group-term life is taxable: {{pa.bik.pa.group_term_life.taxable}} (no imputed income at any amount);
  - personal use of employer property, employer parking, meals and lodging are nontaxable fringes.
- **HSA:** PA follows the federal rules as a deduction [US-PAS5-012]; at withholding: {{pa.bik.hsa_withholding}} [US-PAV6B-004]. Local EIT base: {{pa.pit.local.eit.base}} [US-PAV6B-005].

## @deductions
- **Wage deductions:** limited to the 34 Pa. Code 9.1 list, each with a written authorisation; no blanket authorisation at hire; never below minimum wage [US-PAS5-006, US-PAS5-003].
- **Wage attachment is narrower than the CCPA (42 Pa.C.S. 8127) [US-PAS5-007]:** ordinary consumer-creditor garnishment available: {{pa.garn.consumer.available}}. Wages are attachable only for support, divorce, short boarding debts, residential-lease judgments (at most {{pa.garn.lease_judgment.max_rate}} % of net wages, or the poverty-guideline floor if less), PHEAA loans and criminal restitution. Support has first priority, restitution second. Support orders: {{pa.garn.iwo.specifics}} [US-PAV6B-001]. State tax levy: {{pa.garn.state_tax_levy}} [US-PAV6B-006].

## @cba
- **Prevailing Wage Act [US-PAP51-003, US-PAP51-006]:** public works above {{pa.prevailing_wage.threshold}} USD (DLI Bureau of Labor Law Compliance). Certified payroll: {{pa.prevailing_wage.certified_payroll}} [US-PAV6B-007].

## @indexation
- **Nothing in PA payroll indexes automatically.** The minimum wage follows the FLSA by statute; the UC employer base is fixed; the employee UC rate is set yearly under UC Law 301.7; employer UC rates are published yearly (UC-748) [US-PA-007, US-PA-009]; the LST cap and the PIT rate are statutory; Philadelphia sets wage-tax rates every July 1 [US-PAS5-022]; EIT rates are published in the DCED register.

## @data
- **SSN Privacy Law (Act 60 of 2006) [US-PAS5-020]:** no public display, no SSN on access cards, secure transmission, no SSN on mailed materials unless required; no pay-stub truncation rule, so mailed pay stubs omit the SSN.
- **Breach Notification Act [US-PAS5-021]:** notify without unreasonable delay; above {{pa.data.breach.ag_threshold}} affected residents, notify the Attorney General and credit reporting agencies; credit monitoring where SSN, bank or ID numbers are breached (Act 33 of 2024).

## @live
- **Act 55 of 2025 (UC Law, domestic-violence eligibility):** benefit side and employer account charging only; no payroll calculation change [US-PAS5-019].
- **2026-01-01:** Pittsburgh Paid Sick Days Act: higher accrual and caps [US-PAB5-001].
- **2026-07-01:** Philadelphia wage tax rates (Section 2) [US-PAS5-022]; further cuts announced but not published.
- **Minimum-wage bill:** {{pa.live.minwage_bill}} [US-PAV6B-008].

## @special
| Population | Pennsylvania rule | Register id |
|---|---|---|
| Domestic / household | Exempt from MWA minimum wage and overtime (Sec. 5(a)(2)); UC only above a quarterly cash test; PA withholding not required when not an employee federally; household pay is PA-taxable to the worker | US-PAS5-001, US-PAS5-019, US-PA-001, US-PAS5-011 |
| Agricultural | Farm labour exempt from the MWA (Sec. 5(a)(1)); UC excludes agricultural labour except covered farms; no PA withholding where FICA does not apply (H-2A may elect) | US-PAS5-001, US-PAS5-019, US-PA-001 |
| Minors | Mandatory meal break for minors; training wage for young workers for an initial period; UC excludes a minor child working for a parent; Child Labor Act hours in Section 1 | US-PAS5-003, US-PAS5-001, US-PAS5-019 |
| Tipped | Cash wage and tip threshold per Section 1; tips paid through the employer are withheld; tips received directly are reported, not withheld | US-PAS5-002, US-PAS5-004, US-PA-001 |
| Clergy / religious | No PA withholding where federal withholding does not apply; cash housing allowance taxable, parsonage value exempt; church service excluded from UC | US-PA-001, US-PAS5-011, US-PAS5-019 |
| Students | Special certificates (sub-minimum, weekly hours cap); seasonal students may be excluded from overtime; UC excludes own-school and some camp students | US-PAS5-001, US-PAS5-002, US-PAS5-019 |
| Nonresident aliens | Same flat rate; exempt only when a PA-resident NRA works outside the US | US-PA-001 |
| Statutory employees | No PA withholding; amounts reported on the W-2 | US-PA-001 |
| Government employees | Government bodies withhold PA tax; MWA excludes elected officials and their policy staff; federal service excluded from PA UC | US-PA-001, US-PAS5-001, US-PAS5-019 |

## @gaps
- pa.leave.philadelphia.accrual :: The Philadelphia accrual rate rests on a secondary source only; the ordinance text was not reached. :: Phila. Code 9-4104 text or phila.gov Office of Worker Protections page.
