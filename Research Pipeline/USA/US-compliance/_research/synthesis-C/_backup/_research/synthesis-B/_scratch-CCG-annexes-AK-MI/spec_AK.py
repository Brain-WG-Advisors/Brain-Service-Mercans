NAME = 'Alaska'
SUMMARY = 'No individual income tax and no state withholding; no local wage tax. Payroll obligations are UI (employee 0.50% inside which STEP 0.10% and TVEP 0.25% are carved out), minimum wage 14.00 from 2026-07-01 with daily overtime over 8 h, paid sick leave from 2025-07-01, an itemised pay statement (8 AAC 15.160(h), as amended 2025-09-25) and the TQ01C quarterly report. Stage-5 overall confidence about 88%.'
U = 'USD'
FACTS = [
 ('labour_code','ak.minwage.hourly',13.00,'US-AKS5-001','2025-07-01','2026-06-30',{'u':U}),
 ('labour_code','ak.minwage.hourly',14.00,'US-AKS5-002','2026-07-01','2027-06-30',{'u':U,'n':'Confirmed on the DOLWD Wage and Hour page updated 2026-05-01.'}),
 ('labour_code','ak.minwage.hourly',15.00,'US-AKS5-001','2027-07-01',None,{'u':U,'n':'Enacted (2024 Ballot Measure 1). From 2028-01-01 indexed to CPI-U Anchorage, rounded up to the next 0.10.'}),
 ('labour_code','ak.minwage.tip_credit.allowed',False,'US-AKS5-001','2025-07-01',None,{'n':'AS 23.10.065(a): the full minimum wage is due in cash to tipped employees.'}),
 ('labour_code','ak.minwage.school_bus_driver.hourly',28.00,'US-AKS5-001','2026-07-01','2027-06-30',{'u':U,'n':'2x the state minimum wage (AS 23.10.065(b)).'}),
 ('labour_code','ak.overtime.daily_threshold_hours',8,'US-AKS5-001','2026-01-01',None,{'u':'hours','n':'AS 23.10.060: 1.5x over 8 h/day and over 40 h/week; daily OT hours not double-counted toward 40. Employers with fewer than 4 employees exempt.'}),
 ('labour_code','ak.overtime.weekly_threshold_hours',40,'US-AKS5-001','2026-01-01',None,{'u':'hours'}),
 ('labour_code','ak.overtime.premium.multiplier',1.5,'US-AKS5-001','2026-01-01',None,{'u':'ratio'}),
 ('labour_code','ak.exempt.salary.weekly_min',1040.00,'US-AKS5-001','2025-07-01','2026-06-30',{'u':U,'vm':'derived arithmetically','n':'AS 23.10.055(b): 2 x state minimum wage x 40 h = 2 x 13.00 x 40.'}),
 ('labour_code','ak.exempt.salary.weekly_min',1120.00,'US-AKS5-001','2026-07-01','2027-06-30',{'u':U,'vm':'derived arithmetically','n':'2 x 14.00 x 40 (AS 23.10.055(b)).'}),
 ('labour_code','ak.exempt.salary.weekly_min',1200.00,'US-AKS5-001','2027-07-01',None,{'u':U,'vm':'derived arithmetically','n':'2 x 15.00 x 40 (AS 23.10.055(b)); enacted rate.'}),
 ('labour_code','ak.pay_frequency.rule','monthly or semi-monthly at the employee\'s election (AS 23.05.140(a))','US-AKS5-001','2026-01-01',None,{}),
 ('labour_code','ak.direct_deposit.requires_voluntary_authorisation',True,'US-AKS5-001','2026-01-01',None,{'n':'AS 23.10.043: only if the employee voluntarily authorises it, to the bank of the employee\'s choice.'}),
 ('income_tax','ak.pit.exists',False,'US-AKP9W-001','2026-01-01',None,{'n':'No individual income tax and no state income-tax withholding; no state W-4, no withholding return, no state W-2 filing.'}),
 ('local_tax','ak.local_wage_tax.exists',False,'US-AKR3-001','2026-01-01',None,{'n':'No local wage, payroll or income tax; municipal powers are property and sales tax only (US-AKR3-002).'}),
 ('social_security','ak.sui.wage_base',54200.00,'US-AKS5-003','2026-01-01','2026-12-31',{'u':U,'n':'Same figure printed on TQ01C (2/26) [US-AKS5-013]. Mechanism 75% of the AK average annual wage; not re-derived (AK-OQ-1).'}),
 ('social_security','ak.sui.employee.rate',0.50,'US-AKS5-003','2026-01-01','2026-12-31',{'u':'percent','n':'Employee UI contribution deducted by the employer. G-DERIVE: 0.27 x ABCR = 0.12%, so the 0.50% floor applies [US-AKS5-006].'}),
 ('social_security','ak.sui.employer.rate.classes_01_20',1.00,'US-AKS5-003','2026-01-01','2026-12-31',{'u':'percent'}),
 ('social_security','ak.sui.employer.rate.class_21',5.40,'US-AKS5-003','2026-01-01','2026-12-31',{'u':'percent'}),
 ('social_security','ak.sui.new_employer.rate',1.00,'US-AKS5-004','2026-01-01','2026-12-31',{'u':'percent','n':'Every industry; total with employee share 1.50%.'}),
 ('social_security','ak.sui.abcr',0.004615,'US-AKS5-006','2026-01-01','2026-12-31',{'u':'ratio','vm':'derived arithmetically','n':'ABCR = (131,477,612 / 45,628,865,425) / (10,852,857,547 / 17,381,530,724), DOLWD UI Tax Calculation Cookbook 2026 (updated 2025-12-04). Reproduces every published 2026 rate.'}),
 ('social_security','ak.step.rate_within_employee_ui',0.10,'US-AKP7-001','2026-01-01',None,{'u':'percent','n':'Collected inside the employee 0.50% and credited back; net cost nil. No employer STEP tax (SB 217 not enacted).'}),
 ('social_security','ak.tvep.rate_within_employee_ui',0.25,'US-AKP7-002','2026-01-01',None,{'u':'percent','n':'Collected inside the employee 0.50%; net cost nil.'}),
 ('social_security','ak.sdi_pfml.exists',False,'US-AKP9W-001','2026-01-01',None,{'n':'No SDI/TDI/PFML/LTC/transit levy. AFLA covers public employers only and is unpaid.'}),
 ('payslip_statute','ak.payslip.required',True,'US-AKS5-001','2025-09-25',None,{'n':'8 AAC 15.160(h): written or electronic statement each pay period: rate, gross, net, period dates, FIT and FICA, AK ESA contributions, board/lodging, advances, straight-time and OT hours, other deductions, sick leave used in accrual year and sick leave balance (PTO used/balance satisfies, FAQ Q13 US-AKS5-010).'}),
 ('payslip_statute','ak.payslip.sick_leave_balance.required',True,'US-AKS5-001','2025-09-25',None,{}),
 ('data_protection','ak.records.wage_hour.retention_years',3,'US-AKS5-001','2026-01-01',None,{'u':'years','n':'AS 23.10.100, at the place of employment (central in-state office counts, 8 AAC 15.900).'}),
 ('data_protection','ak.records.ui.retention_years',5,'US-AKS5-005','2026-01-01',None,{'u':'years','c':'medium','n':'ES Tax Handbook (A.3).'}),
 ('reporting_instruments','ak.report.sui.quarterly.form','TQ01C (2/26) with wage schedule; due last day of month after quarter; zero report required; wages reported in quarter paid','US-AKS5-013','2026-01-01',None,{}),
 ('reporting_instruments','ak.report.sui.quarterly.late_penalty_min',10.00,'US-AKS5-005','2026-01-01',None,{'u':U,'c':'medium'}),
 ('reporting_instruments','ak.report.sui.employee_fields','SSN, name, reportable wages, occupational code (6 or 8 digit), 2-digit geographic code','US-AKS5-013','2026-01-01',None,{'n':'Alaska-specific DD fields.'}),
 ('reporting_instruments','ak.report.sui.channel','file_upload (CSV, no headings; header 11 cols, detail 12 cols, rev. 2016-05-17) or online keying or paper','US-AKS5-014','2026-01-01',None,{}),
 ('reporting_instruments','ak.report.sui.online_mandatory_threshold_employees',50,'US-AKS5-005','2026-01-01',None,{'u':'employees','c':'medium','n':'Also mandatory with 1M+ taxable wages in current or prior year, or when a payroll agent files.'}),
 ('reporting_instruments','ak.newhire.report_days',20,'US-AKS5-007','2026-01-01',None,{'u':'days','c':'medium','n':'AS 25.27.075 (statute text not read). Online via myAlaska; fax no longer accepted. Penalty 10 USD/employee.'}),
 ('leave','ak.leave.sick.accrual.hours_worked_per_hour',30,'US-AKS5-001','2025-07-01',None,{'u':'hours','n':'1 h per 30 h worked, overtime included (AS 23.10.067).'}),
 ('leave','ak.leave.sick.cap_hours.under_15_fte',40,'US-AKS5-001','2025-07-01',None,{'u':'hours','n':'Cap on accrual and use per year; FTE counted on prior calendar year (8 AAC 15.106).'}),
 ('leave','ak.leave.sick.cap_hours.15_plus_fte',56,'US-AKS5-001','2025-07-01',None,{'u':'hours'}),
 ('leave','ak.leave.sick.payout_on_separation',False,'US-AKS5-001','2025-07-01',None,{'n':'AS 23.10.068(a)(1). Reinstated on rehire within 6 months.'}),
 ('leave','ak.leave.sick.rehire_reinstatement_months',6,'US-AKS5-001','2025-07-01',None,{'u':'months'}),
 ('termination','ak.final_pay.discharge.working_days',3,'US-AKS5-001','2026-01-01',None,{'u':'working days','n':'AS 23.05.140(b). Resignation: next regular payday at least 3 days after notice.'}),
 ('termination','ak.final_pay.penalty.max_working_days',90,'US-AKS5-001','2026-01-01',None,{'u':'working days'}),
 ('benefits_in_kind','ak.sui.wages.excludes_401k_deferrals',True,'US-AKS5-005','2026-01-01',None,{'c':'medium','n':'AS 23.20.530 per ES Tax Handbook (A.3): 401(k)/403(b)/457/SEP/SIMPLE deferrals excluded from UI wages, unlike FUTA; dependent care, adoption, group legal and cash cafeteria elections ARE UI wages.'}),
 ('benefits_in_kind','ak.board_lodging.no_determination_max_per_day',20.00,'US-AKS5-001','2026-01-01',None,{'u':U,'n':'8 AAC 15.160(d)-(f); prior written notice and signed acceptance required.'}),
 ('deductions_garnishments','ak.garn.exempt.weekly',473.00,'US-AKS5-017','2026-01-01',None,{'u':U,'c':'medium','n':'Greater of 473/week or 75% of disposable earnings (AS 09.38.030, CPI-adjusted per 8 AAC 95.030, not read; amounts via CIV-530 8/24). Monthly / 4.3, semi-monthly / 2.17.'}),
 ('deductions_garnishments','ak.garn.exempt.weekly_household_support',743.00,'US-AKS5-017','2026-01-01',None,{'u':U,'c':'medium'}),
 ('deductions_garnishments','ak.garn.exempt.liquid_assets_monthly',1890.00,'US-AKS5-017','2026-01-01',None,{'u':U,'c':'medium'}),
 ('live_change','ak.live.sb217_employer_step.status','not enacted (in S FIN since 2026-04-15); would operate at UI employer contribution level','US-AKS5-012','2026-04-15',None,{}),
 ('live_change','ak.live.hb161_sick_leave.status','not enacted (referred H L&C 2025-03-28, never moved)','US-AKS5-011','2025-03-28',None,{}),
]
CITED = ['US-AK-WT-001','US-AK-P5-1-003','US-AK-P5-2-001','US-AK-P5-2-002','US-AK-P5-1-005','US-AKS5-018','US-AKS5-008','US-AKS5-009','US-AKS5-010','US-AKS5-015','US-AKS5-016','US-AKR3-002','US-AKR3-003','US-AK-WT-002','US-AKP7-001','US-AKP7-002','US-AK-P5-1-006','US-AKL-001','US-AKP9L-001']
NARR = {
 'collective_agreements': 'Title 36 public construction over 25,000 USD: DOLWD prevailing-wage determination (Pamphlet 600) [US-AK-P5-1-005 — legacy id, narrative only: its id fails the facts.schema pattern, so the threshold is not emitted as a fact]. Certified payroll, Notice of Work and Notice of Completion to DOLWD LSS; online/bulk upload optional, paper allowed [US-AKS5-018]. Multiemployer CBA funds may satisfy sick leave (068(e)).',
 'income_tax': 'No wage tax: AK has no state W-4, supplemental rate, withholding return, reciprocity or state W-2 filing [US-AK-WT-001, US-AK-WT-002, US-AKP9W-001]. Oracle for income tax: none; the DOLWD UI Tax Calculation Cookbook 2026 is the agency worked example for UI rates [US-AKS5-006].',
 'non_resident': 'Not applicable: no state income tax, so no resident/non-resident treatment and no reciprocity [US-AK-WT-001]. SUI wage-base credit: wages taxed in another state in the same year for a transferred employee count toward the 54,200 base; TQ01C carries a "wages reported to other states" flag [US-AKS5-005, US-AKS5-013].',
 'social_security': 'G-DERIVE done in Stage 5 (Python) from the Cookbook: reserve rate 811,365,166 / 17,381,530,724 = 4.668% > 3.3%, solvency credit capped 0.40%; employer 0.73 x ABCR x factor - 0.004 <= 0.16%, so classes 1-20 floor 1.00% and class 21 floor 5.40% [US-AKS5-006]. Workers compensation is an insurer premium outside payroll.',
 'reporting_instruments': 'No state withholding return/reconciliation/W-2 filing. Quarterly UI TQ01C with employer-level monthly counts (12th), excess wages and other-states flag; corrections on TADJ [US-AKS5-013]. Registration TREG; Notice to Employees placard 07-1012 [US-AKS5-015]. New hire within 20 days via myAlaska; CSED ACSESS Business Portal since 2025-10-06 [US-AKS5-007, US-AKS5-008].',
 'termination': 'No statute requires vacation payout (AK-OQ-2 open); no state WARN; return-transport duty AS 23.10.375-.400 not modelled.',
 'deductions_garnishments': 'Deductions only by written agreement and never below minimum wage/overtime (8 AAC 15.160(a)-(g)). Child support IWO per federal CCPA, remitted via CSED ACSESS [US-AKS5-008]; AK fee/priority unread (AK-OQ-4). Nonresident debtor: federal 30x/75% rule [US-AKS5-017].',
 'data_protection': 'AS 45.48.400-.480: SSN not on mailed material; recommendation omit/truncate SSN on every pay statement [US-AKS5-016].',
 'indexation': 'Minimum wage CPI-U Anchorage from 2028-01-01 (no indexed value yet, so no derivation possible); EAP threshold and school-bus rate follow at 2x; UI base 75% of AAW (2027 not published, HTTP 404 on 2026-11-02); garnishment exemptions CPI (AS 09.38.115).',
}
SPECIAL = '''- Domestic/household: exempt from W&H minimum wage, OT and sick leave (23.10.055(a)(4)); UI-excluded under 1,000/quarter [US-AKS5-001, US-AKS5-005].
- Agricultural: exempt from MW, OT, sick leave; UI-excluded under 20,000/quarter or fewer than 10 workers [US-AKS5-001, US-AKS5-005].
- Commercial fishing: crews exempt from W&H and sick leave; UI-excluded if fewer than 10 crew paid on shares; seamen OT-exempt [US-AKS5-001, US-AKS5-005].
- Minors under 18 part-time (30 h/week or less): exempt from W&H and sick leave except in a week over 30 h (8 AAC 15.135) [US-AKS5-001, US-AKS5-010].
- Tipped: no tip credit; full minimum wage in cash (8 AAC 15.907) [US-AKS5-001].
- Clergy/religious orders: UI-excluded; religious nonprofit volunteers W&H-exempt [US-AKS5-005, US-AKS5-001].
- Students at own school and work-study under 22: UI-excluded; student learners MW exemption by certificate (8 AAC 15.125) [US-AKS5-005, US-AKS5-001].
- Nonresident aliens: no state rule beyond federal [US-AK-WT-001].
- Corporate officers: UI-excluded unless the employer elects coverage for all officers; commission insurance/real-estate/stock agents UI-excluded when FUTA-excluded [US-AKS5-005].
- Government: W&H MW/OT and sick-leave exempt; UI contributory or reimbursable; AFLA unpaid leave [US-AKS5-001, US-AKS5-005].
- Nonprofit: UI at 250/quarter or 4+ employees in 20 weeks; reimbursable option; summer camps reduced wage up to 12 weeks [US-AKS5-005, US-AKS5-001].
- Multistate: SUI credit for other-state wages of transferred employees [US-AKS5-005]; sick-leave reach to partly-in-state workers open (AK-OQ-6).'''
LANG = 'No language clause in the pay-statement rule or posters [US-AKL-001, US-AKP9L-001]: payslip and filings in English (US-OWN-006).'
UNRES = [
 {'key':'ak.sui.wage_base.derivation','why':'The 2026 wage base 54,200 is published but not re-derived: the average annual wage worksheet (75% rule) was not obtained.','attempted':['labor.alaska.gov/estax rate pages','live.laborstats.alaska.gov'],'close':'DOLWD Research and Analysis "Tax Base Calculation worksheet" 2026, or the signed "AK UI Tax Rates 2026 Full Document" (2026-01-21) attached to SB 217 on BASIS.'},
 {'key':'ak.final_pay.accrued_vacation.payout','why':'No statute requires vacation payout; whether accrued vacation is wages due under AS 23.05.140(b) absent a forfeiture policy was not read.','attempted':['Pamphlet 100 (Oct 2025)'],'close':'DOLWD Wage and Hour position (Pamphlet 100 index or W&H FAQ) or Alaska Supreme Court case law on an official host.'},
 {'key':'ak.paycard.rule','why':'No paycard statute located; AS 23.10.040 requires money or negotiable check and AS 23.10.043 voluntary deposit authorisation.','attempted':['Pamphlet 100'],'close':'A DOLWD Wage and Hour opinion on payroll cards.'},
 {'key':'ak.garn.iwo.employer_fee','why':'AS 25.27.062 IWO employer fee, priority and remittance deadline not read; akleg.gov unreachable (HTTP 000) and CSED employer pages 404 after the 2025-10 site change.','attempted':['https://www.akleg.gov/basis/statutes.asp (HTTP 000)','https://childsupport.alaska.gov/child-support-enforcement/employers/new-hire-wage-withholding (HTTP 404)'],'close':'AS 25.27.062 read through VPN on akleg, or the CSED ACSESS Business Portal employer guide.'},
 {'key':'ak.prevailing_wage.certified_payroll.frequency','why':'AS 36.05.040 not read (akleg unreachable) and the Pamphlet 600 edition in force not confirmed.','attempted':['akleg.gov (HTTP 000)','Wayback CDX (no snapshot)'],'close':'AS 36.05.040 on akleg and the current Pamphlet 600 at labor.alaska.gov/lss.'},
 {'key':'ak.leave.sick.multistate_coverage','why':'The sick leave statute covers employers in Alaska with no hours-in-state threshold; the FAQ (2026-01-28) is silent on partly-in-state and remote workers.','attempted':['DOLWD sick leave FAQ'],'close':'A DOLWD LSS interpretation on coverage of employees working partly in Alaska.'},
 {'key':'ak.live.bulletin_sweep','why':'The Alaska Administrative Register 2026 (8 AAC amendments) and 2026 special sessions were not swept (akleg unreachable without VPN).','attempted':['akleg.gov (HTTP 000)'],'close':'Lt. Governor Online Public Notices / Administrative Register issues 2026-01..10 and the BASIS Passed Legislation list of the 34th Legislature, read with VPN.'},
 {'key':'ak.sui.wage_base.next_year','why':'2027 wage base and rates not yet published (labor.alaska.gov/estax/2027-experience-rates.html HTTP 404 on 2026-11-02): timing gap.','attempted':['https://labor.alaska.gov/estax/2027-experience-rates.html (404)'],'close':'DOLWD 2027 experience-rates page once published (normally December).'},
]
LEGACY = [('collective_agreements','ak.prevailing_wage.threshold',25000.00,'US-AK-P5-1-005','2026-01-01',None,'Title 36 public construction over 25,000 USD.')]
