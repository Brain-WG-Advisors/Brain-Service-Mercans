# Module 8: Statutory Leave Management

*Purpose: To define the rules for all statutory leave types.*

## 8.1 Leave Entitlements

Leave in the United States sits on two layers. The federal layer sets job-protected leave and no paid leave for private employers. The State and local layer sets paid sick leave and the paid family and medical leave (PFML) or temporary disability insurance (TDI) programmes. Payroll accrues the first and withholds premiums for the second. The State or its insurer pays the benefit. Per-State detail is in the jurisdiction annexes. This module gives the federal rules and the comparison tables.

### For each type of statutory leave, what are the eligibility criteria and accrual methodology?

**Federal layer.**

| Leave | Entitlement | Paid by | Source |
|---|---|---|---|
| Family and Medical Leave Act (FMLA) | Up to [[FACT:fed.fmla.weeks=12]] workweeks of job-protected leave; up to [[FACT:fed.fmla.military_caregiver.weeks=26]] workweeks to care for a covered servicemember. The leave may be unpaid. | Unpaid (the employer may require accrued paid leave to run concurrently) | [US-FEDS5-026] |
| Paid leave for private employers | None at federal level: no federal paid-leave mandate | — | [US-FEDS5-026] |

FMLA eligibility (employer size, employee service and hours) is not carried as a fact. ⚠️ RESEARCH-GAP: FMLA employer-coverage and employee-eligibility thresholds (29 U.S.C. 2611) are not keyed.

Paid sick leave for federal contractors under Executive Order 13706: ⚠️ RESEARCH-GAP: the accrual rate and annual cap of paid sick leave for federal contractors under Executive Order 13706 (29 CFR 13.5) are not keyed.

**State paid sick leave (Table 8.1.1).** Accrual is per hour worked, so it follows the hours actually worked. A cap limits either the annual accrual or the use, as the key says. Paid sick leave does not have to be paid out at separation wherever the facts carry a payout key (Table 8.1.3). Coverage of employees who work only partly in a State is per State and not established at multistate level: ⚠️ RESEARCH-GAP: paid-sick-leave coverage of employees who work only partly in a State is set per State and is not keyed at multistate level.

| State | Keyed rule (parameter: value) | Register |
|---|---|---|
| Alaska (AK) | hours worked per hour accrued: [[FACT:ak.leave.sick.accrual.hours_worked_per_hour=30]]; cap, 15+ FTE employers (hours): [[FACT:ak.leave.sick.cap_hours.15_plus_fte=56]]; cap, under 15 FTE employers (hours): [[FACT:ak.leave.sick.cap_hours.under_15_fte=40]]; balance reinstated on rehire within (months): [[FACT:ak.leave.sick.rehire_reinstatement_months=6]] | US-AKS5-001 |
| Alabama (AL) | statewide paid-sick-leave law: no | US-ALS5-010 |
| Arizona (AZ) | hours worked per hour accrued: [[FACT:az.leave.sick.accrual.hours_worked_per_hour=30]]; cap, 15+ employees (hours): [[FACT:az.leave.sick.cap_hours.15_plus=40]]; cap, under 15 employees (hours): [[FACT:az.leave.sick.cap_hours.under_15=24]]; balance reinstated on rehire within (months): [[FACT:az.leave.sick.rehire_reinstatement_months=9]]; waiting period (days): [[FACT:az.leave.sick.waiting_days=90]] | US-AZS5-008 |
| California (CA) | hours worked per hour accrued: [[FACT:ca.leave.sick.accrual.hours_worked_per_hour=30]]; accrual cap (hours): [[FACT:ca.leave.sick.accrual_cap_hours=80]]; use cap (hours): [[FACT:ca.leave.sick.usage_cap_hours=40]] | US-CAS5-011 |
| Colorado (CO) | hours worked per hour accrued: [[FACT:co.leave.sick.accrual.hours_worked_per_hour=30]]; cap (hours): [[FACT:co.leave.sick.cap_hours=48]] | US-COS5-005 |
| Connecticut (CT) | hours worked per hour accrued: [[FACT:ct.leave.sick.accrual.hours_worked_per_hour=30]]; cap (hours): [[FACT:ct.leave.sick.cap_hours=40]]; employer-size threshold for paid leave (employees): [[FACT:ct.leave.sick.coverage_threshold_employees=11]] (2026-01-01 to 2026-12-31); [[FACT:ct.leave.sick.coverage_threshold_employees=1]] (from 2027-01-01); usable after (days): [[FACT:ct.leave.sick.use_after_days=120]] | US-CTS5-021 |
| District of Columbia (DC) | accrual,  employees: [[FACT:dc.leave.sick.accrual.100_plus=1 h per 37 h worked, up to 7 days/yr]]; accrual,  employees: [[FACT:dc.leave.sick.accrual.25_99=1 h per 43 h worked, up to 5 days/yr]]; accrual,  employees: [[FACT:dc.leave.sick.accrual.under_25=1 h per 87 h worked, up to 3 days/yr]] | US-DCS5-004 |
| Delaware (DE) | statewide paid-sick-leave law: no | US-DES5-021 |
| Florida (FL) | statewide paid-sick-leave law: no | US-FLS5-009 |
| Georgia (GA) | statewide paid-sick-leave law: no | US-GAS5-016 |
| Hawaii (HI) | statewide paid-sick-leave law: no | US-HIS5-024 |
| Iowa (IA) | statewide paid-sick-leave law: no | US-IAS5-021 |
| Idaho (ID) | statewide paid-leave mandate: no | US-IDS5-025 |
| Illinois (IL) | PLAWA accrual: [[FACT:il.leave.plawa.accrual=1 h per 40 h worked up to 40 h per 12 months (front-load allowed); use after 90 days; exempt deemed 40 h/week; no separation payout unless in a vacation/PTO bank; tipped/commissioned paid at least full MW; not in Chicago/Cook]]; PLAWA cap (hours): [[FACT:il.leave.plawa.cap_hours=40]] | US-ILS5-019 |
| Indiana (IN) | statewide paid-sick-leave law: no | US-INS5-002 |
| Kansas (KS) | statewide paid-sick-leave law: no | US-KSS5-012 |
| Massachusetts (MA) | cap (hours): [[FACT:ma.leave.sick.cap_hours=40]]; employer-size threshold for paid leave (employees): [[FACT:ma.leave.sick.employer_threshold_paid=11]] | US-MAS5-006 |
| Maryland (MD) | ESSL hours worked per hour accrued: [[FACT:md.leave.essl.accrual.hours_worked_per_hour=30]]; ESSL annual earning cap (hours): [[FACT:md.leave.essl.annual_earn_cap_hours=40]]; ESSL employer-size threshold for paid leave (employees): [[FACT:md.leave.essl.paid_employer_threshold=15]]; ESSL use cap (hours): [[FACT:md.leave.essl.use_cap_hours=64]] | US-MDS5-013 |
| Maine (ME) | earned paid leave hours worked per hour accrued: [[FACT:me.leave.earned_paid.accrual.hours_worked_per_hour=40]]; earned paid leave cap (hours): [[FACT:me.leave.earned_paid.cap_hours=40]]; earned paid leave employer-size threshold for paid leave (employees): [[FACT:me.leave.earned_paid.employer_threshold=10]] | US-MES5-008 |
| Michigan (MI) | ESTA hours worked per hour accrued: [[FACT:mi.leave.esta.accrual.hours_worked_per_hour=30]]; ESTA cap,  employers (hours): [[FACT:mi.leave.esta.cap_hours.large=72]]; ESTA cap,  employers (hours): [[FACT:mi.leave.esta.cap_hours.small=40]]; ESTA small-employer threshold (employees): [[FACT:mi.leave.esta.small_employer_threshold=10]] | US-MIS5-004 |
| Minnesota (MN) | ESST hours worked per hour accrued: [[FACT:mn.leave.esst.accrual_ratio_hours_worked=30]]; ESST annual accrual cap (hours): [[FACT:mn.leave.esst.annual_accrual_cap_hours=48]]; ESST balance cap (hours): [[FACT:mn.leave.esst.balance_cap_hours=80]] | US-MNS5-011 |
| Missouri (MO) | statewide paid-sick-leave law: no | US-MOS5-003 |
| Mississippi (MS) | statewide paid-sick-leave law: no | US-MSS5-009 |
| Montana (MT) | statewide paid-sick-leave law: no | US-MTP52-002 |
| North Carolina (NC) | statewide paid-sick-leave law: no | US-NCS5-001 |
| North Dakota (ND) | statewide paid-sick-leave law: no | US-NDP52-002 |
| Nebraska (NE) | hours worked per hour accrued: [[FACT:ne.leave.paid_sick.accrual_ratio_hours_worked=30]]; annual cap,  employers (hours): [[FACT:ne.leave.paid_sick.annual_cap.other_hours=56]]; annual cap,  employers (hours): [[FACT:ne.leave.paid_sick.annual_cap.small_hours=40]]; employer-size threshold for paid leave (employees): [[FACT:ne.leave.paid_sick.coverage_min_employees=11]] | US-NES5-007 US-NES5-009 |
| New Hampshire (NH) | statewide paid-sick-leave law: no | US-NHS5-011 |
| New Mexico (NM) | hours worked per hour accrued: [[FACT:nm.leave.paid_sick.accrual_ratio_hours_worked=30]]; annual cap (hours): [[FACT:nm.leave.paid_sick.annual_cap_hours=64]] | US-NMS5-001 |
| Nevada (NV) | hours accrued per hour worked: [[FACT:nv.leave.paid.accrual_per_hour_worked=0.01923]]; employer-size threshold for paid leave (employees): [[FACT:nv.leave.paid.coverage_min_employees=50]] | US-NVS5-001 |
| New York (NY) | hours worked per hour accrued: [[FACT:ny.leave.paid_sick.accrual_ratio_hours_worked=30]]; annual hours,  employees: [[FACT:ny.leave.paid_sick.annual_hours.100plus=56]]; annual hours,  employees: [[FACT:ny.leave.paid_sick.annual_hours.5_99=40]] | US-NYS5-007 |
| Ohio (OH) | statewide paid-sick-leave law: no | US-OHS5-012 |
| Oklahoma (OK) | statewide paid-sick-leave law: no | US-OKS5-002 |
| Oregon (OR) | hours worked per hour accrued: [[FACT:or.leave.sick.accrual_ratio_hours_worked=30]]; employer-size threshold for paid leave (employees): [[FACT:or.leave.sick.paid_employer_threshold=10]] | US-ORS5-007 |
| Pennsylvania (PA) | statewide paid-sick-leave law: no | US-PAS5-003 |
| Rhode Island (RI) | hours worked per hour accrued: [[FACT:ri.leave.paid_sick.accrual_ratio_hours_worked=35]]; annual cap (hours): [[FACT:ri.leave.paid_sick.annual_cap_hours=40]]; employer-size threshold for paid leave (employees): [[FACT:ri.leave.paid_sick.employer_threshold=18]] | US-RIS5-009 |
| South Carolina (SC) | statewide paid-sick-leave law: no | US-SCS5-013 |
| South Dakota (SD) | statewide paid-sick-leave law: no | US-SDS5-011 |
| Tennessee (TN) | statewide paid-sick-leave law: no | US-TNS5-001 |
| Texas (TX) | statewide paid-sick-leave law: no | US-TXS5-005 |
| Utah (UT) | statewide paid-sick-leave law: no | US-UTS5-012 |
| Virginia (VA) | hours worked per hour accrued: [[FACT:va.leave.paid_sick.accrual_ratio_hours_worked=30]] (from 2027-07-01); general, start: [[FACT:va.leave.paid_sick.general.start=2027-07-01 (50+); 2028-01-01 (25+); 2029-01-01 (all)]] (from 2027-07-01); home health only: yes | US-VAS5-005 US-VAS5-022 |
| Vermont (VT) | earned sick time hours worked per hour accrued: [[FACT:vt.leave.est.accrual_ratio_hours_worked=52]]; earned sick time annual cap (hours): [[FACT:vt.leave.est.annual_cap_hours=40]] | US-VTS5-008 |
| Washington (WA) | hours worked per hour accrued: [[FACT:wa.leave.paid_sick.accrual_ratio_hours_worked=40]] | US-WAS5-001 |
| Wisconsin (WI) | statewide paid-sick-leave law: no | US-WIS5-006 |
| Wyoming (WY) | statewide paid-sick-leave law: no | US-WYP51-004 |

States with no paid-sick-leave key in the facts files: AR, KY, LA, NJ, WV. ⚠️ RESEARCH-GAP: the facts files carry neither a paid-sick-leave rule nor a statement that none exists for these States; see each jurisdiction annex.

**Local paid-leave ordinances (Table 8.1.2).** These apply on top of the State rule for work performed in the city.

| Locality | Keyed rule (parameter: value) |
|---|---|
| Chicago (IL) | accrual: [[FACT:il.leave.chicago.accrual=1 h paid leave AND 1 h paid sick leave per 35 h worked from day 1 for anyone with >= 80 h in 120 days; notices with first paycheck and around July 1]] |
| New York City (NY) | paid hours, max, 100plus: [[FACT:ny.leave.nyc_pto.paid_hours.max.100plus=56]] (from 2026-02-22); paid hours, max, under100: [[FACT:ny.leave.nyc_pto.paid_hours.max.under100=40]] (from 2026-02-22); pay statement items: [[FACT:ny.leave.nyc_pto.pay_statement_items=Each pay period, on the pay statement or other written documentation: PTO accrued in the period; paid and unpaid PTO used in the period; unpaid immediately available hours available in the calendar year; accrued PTO available for use in the calendar year]] (from 2026-02-22); prenatal paid hours: [[FACT:ny.leave.nyc_pto.prenatal_paid_hours=20]] (from 2026-02-22); unpaid hours immediate: [[FACT:ny.leave.nyc_pto.unpaid_hours_immediate=32]] (from 2026-02-22) |
| Philadelphia (PA) | annual cap (hours): [[FACT:pa.leave.philadelphia.annual_cap_hours=40]]; employer-size threshold for paid leave (employees): [[FACT:pa.leave.philadelphia.employer_threshold=10]] |
| Pittsburgh (PA) | hours worked per hour accrued: [[FACT:pa.leave.pittsburgh.accrual.hours_worked_per_hour=30]]; annual cap,  employees (hours): [[FACT:pa.leave.pittsburgh.annual_cap_hours.15plus=72]]; annual cap,  employees (hours): [[FACT:pa.leave.pittsburgh.annual_cap_hours.under15=48]]; rule: [[FACT:pa.leave.pittsburgh.rule=Carryover required unless the employer front-loads 72 h (15+) / 48 h (<15) at the start of each year; reinstated on rehire within 6 months; paid at the same base rate and benefits, never below the PA minimum wage; no pay for lost tips or commissions]]; waiting period (days): [[FACT:pa.leave.pittsburgh.waiting_period_days=90]] |

**Other statutory leaves keyed in the facts (Table 8.1.4).** Examples only; the complete set per State is in the annexes.

| State | Leave (parameter) | Value | Register |
|---|---|---|---|
| AL | jury / full time usual compensation | yes | US-ALS5-012 |
| AL | voting / hours | [[FACT:al.leave.voting.hours=1]] | US-ALS5-012 |
| FL | domestic violence / days | [[FACT:fl.leave.domestic_violence.days=3]] | US-FLS5-014 |
| HI | family / employer threshold | [[FACT:hi.leave.family.employer_threshold=100]] | US-HIS5-023 |
| IN | military family / days | [[FACT:in.leave.military_family.days=10]] | US-INS5-006 |
| KY | adoption / weeks | [[FACT:ky.leave.adoption.weeks=6]] | US-KYS5-016 |
| KY | voting / hours | [[FACT:ky.leave.voting.hours=4]] | US-KYS5-025 |
| LA | jury / paid days | [[FACT:la.leave.jury.paid_days=1]] | US-LAS5-013 |
| NH | lactation / min employees | [[FACT:nh.leave.lactation.min_employees=6]] | US-NHS5-011 |
| NV | dv sa / hours per 12 months | [[FACT:nv.leave.dv_sa.hours_per_12_months=160]] | US-NVS5-001 |
| NY | prenatal / hours per 52 weeks | [[FACT:ny.leave.prenatal.hours_per_52_weeks=20]] | US-NYS5-007 |
| OK | voting / paid hours | [[FACT:ok.leave.voting.paid_hours=2]] | US-OKS5-023 |
| SD | voting / paid hours | [[FACT:sd.leave.voting.paid_hours=2]] | US-SDS5-008 |
| TN | jury duty / paid | yes | US-TNS5-012 |
| TX | voting / paid | yes | US-TXS5-014 |
| WA | pfml / job protection / employer threshold | [[FACT:wa.leave.pfml.job_protection.employer_threshold=25]] | US-WAS5-028 |
| WI | wfmla / employer threshold | [[FACT:wi.leave.wfmla.employer_threshold=50]] | US-WIS5-006 |
| WY | voting / paid hours | [[FACT:wy.leave.voting.paid_hours=1]] | US-WYS5-016 |

### How are unpaid or partially paid leaves handled?

- **Unpaid leave (FMLA or employer-approved).** No wages are paid, so nothing is withheld or contributed for the period. Federal income tax, FICA and FUTA attach to wages *paid* in the calendar year ([[FACT:fed.tax_year.basis=calendar year (W-2 on calendar-year basis)]]) [US-FED-006]. The OASDI and FUTA wage bases run per employer per calendar year from the first payment. They are not prorated for the absence [US-FED-007].
- **Partially paid leave through a State programme.** PFML and TDI benefits are paid by the State fund or by the employer's approved insurer, not by payroll (Table 8.1.5). The employee's PFML contribution withheld by payroll counts as W-2 wages (employee contribution is W-2 wages) [US-FEDS5-007].
- **Employer top-up of a State benefit.** The facts do not key how an employer supplement paid alongside a State benefit is taxed. ⚠️ RESEARCH-GAP: treatment of an employer top-up paid during State PFML/TDI leave is not keyed.

### Which wage types are affected by unpaid/partially paid leave?

The hours-based earnings for the absent hours are not paid. Every wage type whose base follows those hours therefore falls with them: regular pay, shift and hours-based premiums, and the paid-sick-leave accrual (accrual is per hour worked, Table 8.1.1). Contributions whose base is wages paid fall automatically: OASDI, Medicare, FUTA, SUI, and PFML/TDI premiums. The Wage Type Catalogue (WTC) carries the codes and their Subject-to flags. Massachusetts PFML is the exception to the payment-date rule: its rates apply to wages *earned* on or after 1 January [US-MAS5-012].

### Are there any mandatory national military service leaves?

The United States has no national service obligation in peacetime that payroll must model. Re-employment and leave rights of reservists and guard members (USERRA) are not carried as a fact. ⚠️ RESEARCH-GAP: USERRA leave and benefit-continuation rules (38 U.S.C. 4301-4335) are not keyed.

State military-family leave keyed in the facts: Indiana [[FACT:in.leave.military_family.days=10]] days [US-INS5-006].

### Are any other kinds of leave paid by government authorities?

Yes. The State PFML and TDI programmes pay wage-replacement benefits from a State fund, an approved private plan or the employer's insurer. Payroll collects the premium (Module 5 carries the rates and wage bases). It does not pay the benefit (Table 8.1.5).

**Table 8.1.5: State programmes that pay leave benefits**

| Programme | Benefit paid by | Maximum weekly benefit (USD) | Register |
|---|---|---|---|
| California SDI / PFL | EDD fund (or voluntary plan, W-2 Box 14 label [[FACT:ca.sdi.voluntary_plan.w2_box14_label=VPDI]]) | not keyed | [US-CAP7-002] |
| Colorado FAMLI | State FAMLI fund | not keyed | [US-COB5-003] |
| Connecticut Paid Leave | CT Paid Leave Authority | [[FACT:ct.pfml.benefit.weekly_max=1,016.40]] | [US-CTS5-020] |
| Delaware Paid Leave | State fund | [[FACT:de.pfml.benefit.weekly_max=900]] | [US-DES5-012] |
| District of Columbia Paid Family Leave | DC fund (employer-funded) | not keyed | [US-DCS5-020] |
| Hawaii TDI | Employer's insured plan | [[FACT:hi.tdi.benefit.weekly_max=871]] | [US-HIS5-015] |
| Maryland FAMLI | State fund; contributions start [[FACT:md.pfml.contributions.start=2027-01-01 (no contribution in 2026)]] | not keyed | [US-MDS5-014] |
| Massachusetts PFML | Department of Family and Medical Leave | [[FACT:ma.pfml.max_weekly_benefit=1,230.39]] (2026); [[FACT:ma.pfml.max_weekly_benefit=1,284.61]] (from 2027-01-01) | [US-MAS5-025] |
| Maine PFML | State fund | not keyed | [US-MES5-025] |
| Minnesota Paid Leave | State fund | not keyed | [US-MNP52-003] |
| New Jersey TDI / FLI | State fund or private plan | [[FACT:nj.tdi.max_weekly_benefit=1,119]] | [US-NJS5-010] |
| New York PFL / DBL | Employer's insurer | PFL: [[FACT:ny.pfl.benefit.rate_of_aww=67]]% of the employee's average weekly wage, capped at [[FACT:ny.pfl.benefit.max_weekly=1,228.53]] | [US-NYB5-002] |
| Oregon Paid Leave | State fund | not keyed | [US-ORS5-003] |
| Rhode Island TDI | State fund | not keyed | [US-RIP9V-001] |
| Washington PFML and WA Cares | State fund | not keyed | [US-WAS5-011] |
| Virginia PFML | State fund; contributions start [[FACT:va.pfml.contributions_start=2028-04-01]] | not keyed | [US-VAS5-016] |

Where the maximum weekly benefit is "not keyed", payroll does not need the figure: the benefit is computed and paid outside payroll.

### What are the payout rules for statutory leaves?

- **FMLA:** no payout; the leave is unpaid unless accrued paid leave is substituted.
- **State PFML/TDI:** the State or insurer pays the benefit directly to the employee. Payroll pays nothing.
- **Paid sick leave:** paid at the employee's regular rate when used. It is not paid out at separation in any State where the facts carry a payout key (Table 8.1.3).
- **Vacation / PTO:** no federal or general statutory entitlement. Where an employer grants it, payout at separation is State law (Table 8.1.3 and Module 9, Table 9.1.1).

### How are unused paid leaves treated upon termination?

**Table 8.1.3: Unused leave at separation (keyed States).** "yes" means the accrued balance is wages due at separation; "no" means it is not paid out.

| State | Keyed rule (parameter: value) | Register |
|---|---|---|
| Alaska (AK) | Sick leave, paid out at separation: no | US-AKS5-001 |
| Arizona (AZ) | Sick leave, paid out at separation: no | US-AZS5-008 |
| California (CA) | Vacation/PTO, vested vacation paid out: yes; Sick leave, paid out at separation: no | US-CAS5-010 US-CAS5-011 |
| Colorado (CO) | Vacation/PTO, vacation payout: yes; Sick leave, paid out at separation: no | US-COS5-003 US-COS5-005 |
| District of Columbia (DC) | Sick leave, paid out at separation: no | US-DCS5-024 |
| Illinois (IL) | Vacation/PTO, vacation payout: yes | US-ILS5-004 |
| Massachusetts (MA) | Sick leave, paid out at separation: no | US-MAS5-006 |
| Michigan (MI) | Sick leave, ESTA paid out at separation: no | US-MIS5-004 |
| Minnesota (MN) | Sick leave, ESST paid out at separation: no | US-MNS5-011 |
| Montana (MT) | Vacation/PTO, vacation paid out at separation: yes | US-MTS5-018 |
| North Carolina (NC) | Vacation/PTO, vacation payout: [[FACT:nc.term.vacation.payout=per employer policy; forfeiture only with advance written notice]] | US-NCS5-008 |
| North Dakota (ND) | Vacation/PTO, PTO paid out at separation: yes | US-NDS5-007 |
| Nebraska (NE) | Sick leave, paid out at separation: no; Vacation/PTO, vacation payout: yes | US-NES5-004 US-NES5-007 |
| New Hampshire (NH) | Vacation/PTO, vacation payout: [[FACT:nh.term.vacation.payout=per written policy (no statutory duty); accrued benefits do not lapse on policy change]] | US-NHS5-004 |
| New Mexico (NM) | Sick leave, paid out at separation: no; Vacation/PTO, vacation payout: [[FACT:nm.term.vacation.payout=owed if written policy grants it (vacation pay is wages)]] | US-NMS5-001 US-NMS5-003 |
| Nevada (NV) | Sick leave, paid out at separation: no | US-NVS5-001 |
| Oklahoma (OK) | Vacation/PTO, vacation payout: [[FACT:ok.term.vacation.payout=per agreement or established policy]] | US-OKS5-003 |
| Oregon (OR) | Sick leave, paid out at separation: no; Vacation/PTO, vacation payout: [[FACT:or.term.vacation.payout=per established policy or agreement]] | US-ORS5-007 US-ORS5-021 |
| Pennsylvania (PA) | Sick leave, paid out at separation: no; Vacation/PTO, vacation payout: [[FACT:pa.term.vacation.payout=only if policy or contract promises]] | US-PAB5-001 US-PAS5-003 |
| Rhode Island (RI) | Sick leave, paid out at separation: no; Vacation/PTO, vacation payout after years: [[FACT:ri.term.vacation.payout_after_years=1]] | US-RIS5-006 US-RIS5-009 |
| South Carolina (SC) | Vacation/PTO, vacation payout: [[FACT:sc.term.vacation.payout=only if due under policy or contract]] | US-SCP52-006 |
| Tennessee (TN) | Vacation/PTO, vacation payout: [[FACT:tn.term.vacation.payout=only if policy or labour agreement requires]] | US-TNS5-001 |
| Texas (TX) | Vacation/PTO, vacation payout: [[FACT:tx.term.vacation.payout=only if written policy or agreement promises it]] | US-TXS5-004 |
| Utah (UT) | Vacation/PTO, vacation payout: [[FACT:ut.term.vacation.payout=only if due under agreement or policy]] | US-UTS5-012 |
| Vermont (VT) | Sick leave, earned sick time paid out at separation: no; Vacation/PTO, vacation payout: [[FACT:vt.term.vacation.payout=only if written policy/agreement provides]] | US-VTS5-011 US-VTS5-025 |
| Washington (WA) | Sick leave, paid out at separation: no | US-WAS5-001 |
| Wisconsin (WI) | Vacation/PTO, vacation payout: [[FACT:wi.term.vacation.payout=payable if written policy with no written forfeiture clause]] | US-WIS5-005 |
| West Virginia (WV) | Vacation/PTO, accrued leave balance is wages in final pay: yes | US-WVS5-009 |
| Wyoming (WY) | Vacation/PTO, vacation payout: [[FACT:wy.term.vacation.payout=payable unless written forfeiture policy acknowledged in writing by employee]] (from 2026-05-08) | US-WYS5-002 |

States not listed have no payout key in the facts files. Their annex states the rule or carries the gap. Where a State makes the balance wages due, payroll pays it with the final wages (Module 9.1 for the withholding method).

### Provide the calculation logic for each leave type where applicable.

```
# paid sick leave accrual (per State, Table 8.1.1)
accrued_hours += hours_worked / RATIO            # RATIO = hours worked per hour accrued
accrued_hours  = min(accrued_hours, ANNUAL_CAP)  # where the State caps the annual accrual
usable_hours   = min(balance, USE_CAP)           # where the State caps the annual use
pay_for_leave  = hours_taken x regular_rate      # wages: FIT, FICA, FUTA, SUI apply
# Nevada accrues a fraction of an hour per hour worked (Table 8.1.1)
# State PFML/TDI: payroll computes only the premium (Module 5); the benefit is paid by the State or insurer
```

The State-specific RATIO, caps and employer-size thresholds are the values in Table 8.1.1. New York PFL is an example of a benefit computed outside payroll: [[FACT:ny.pfl.benefit.rate_of_aww=67]]% of the average weekly wage, capped at [[FACT:ny.pfl.benefit.max_weekly=1,228.53]] [US-NYB5-002]. Payroll does not compute it.

### How does extended unpaid leave impact social security contributions, tax status, and accrual?

- **Contributions:** none for the unpaid period. Federal and State payroll taxes follow wages paid [US-FED-006]. The annual wage bases are not reduced or prorated, so contributions resume on the first pay after return. They resume against the same annual base already used in the calendar year.
- **Tax status:** unchanged. The Form W-4 and the State certificates stay in force. A 2026 claim of exemption from withholding lapses at year end regardless of leave ([[FACT:fed.w4.exempt.validity=2026 only: the exemption checkbox certification lapses; a new W-4 is required for 2027]]) [US-FEDS5-006].
- **Accrual:** paid-sick-leave accrual stops, because it is earned per hour worked (Table 8.1.1). Vacation accrual during unpaid leave is a matter of employer policy; no statutory rule is keyed.
- **State PFML/TDI premiums:** none while no wages are paid. The benefit is paid by the State or insurer.
