NAME = 'Arizona'
SUMMARY = 'Flat-percentage withholding elected on Form A-4 (0.5-3.5%, default 2.0%) on federal wages; no local income tax. State minimum wage CPI-indexed (2026 15.15 / 2027 15.65 are derived from an unconfirmed 2025 base: MANUAL, not facts); Tucson local minimum wage 15.45 / 16.00. Earned paid sick time with mandatory paycheck content (23-375(C)). SUI base 8,000, new employer 2.00%, no employee UI; UI Operating Fund 3.15% of UI liability from 2027. Stricter creditor-garnishment cap (10%).'
U = 'USD'
FACTS = [
 ('labour_code','az.minwage.indexation','each 1 January by Aug-over-Aug CPI-U (US city average), increase rounded to nearest 0.05 (A.R.S. 23-363(B))','US-AZS5-005','2021-01-01',None,{}),
 ('labour_code','az.minwage.tip_credit.max',3.00,'US-AZS5-005','2021-01-01',None,{'u':U,'n':'Employer may pay up to 3.00/h below the minimum if tips + wages reach it each week.'}),
 ('labour_code','az.local_minwage.allowed',True,'US-AZS5-006','2026-01-01',None,{'n':'23-364(I) (voter-protected) permits county/city ordinances above the state rate; the azleg copy of 23-362 (1997 version, US-AZS5-004) says otherwise. Build rule: local rates apply; flag for counsel.'}),
 ('labour_code','az.local_minwage.tucson.hourly',15.45,'US-AZS5-027','2026-01-01','2026-12-31',{'u':U,'n':'Employees with 5+ hours per pay cycle in the city; tip credit max 3.00; State/federal/tribal employers excluded. G-DERIVE: 15.00 x 1.029162 = 15.437 -> 15.45.'}),
 ('labour_code','az.local_minwage.tucson.hourly',16.00,'US-AZS5-027','2027-01-01',None,{'u':U,'n':'Published 2027 rate; G-DERIVE 15.45 x 1.033965 = 15.975 -> 16.00.'}),
 ('labour_code','az.cpi_u.aug2025_over_aug2024.percent',2.9162,'US-AZS5-026','2025-08-01',None,{'u':'percent','vm':'derived arithmetically','n':'BLS CPI-U Aug 2024 314.796, Aug 2025 323.976: 323.976/314.796 - 1.'}),
 ('labour_code','az.cpi_u.aug2026_over_aug2025.percent',3.3965,'US-AZS5-026','2026-08-01',None,{'u':'percent','vm':'derived arithmetically','n':'BLS CPI-U Aug 2026 334.980 / Aug 2025 323.976 - 1.'}),
 ('labour_code','az.pay_frequency.rule','two or more fixed paydays a month, no more than 16 days apart; monthly allowed for FLSA-exempt staff of out-of-state employers with centralized payroll; up to 5 days held back; OT due within 16 days after period','US-AZS5-001','2026-01-01',None,{}),
 ('labour_code','az.payment.method','cash or negotiable check; direct deposit with written consent; payroll card if DD offered and employee neither consents nor names an institution; one free withdrawal per deposit','US-AZS5-001','2026-01-01',None,{}),
 ('labour_code','az.minor.under16.school_week_max_hours',18,'US-AZS5-013','2026-01-01',None,{'u':'hours','n':'23-233: in session 18 h/week, 3 h/day; outside session 40 h/week, 8 h/day; no night work.'}),
 ('income_tax','az.wh.method','flat percentage of gross taxable wages (federal IRC 3401 wages, W-2 box 1) elected on Form A-4','US-AZS5-024','2026-01-01',None,{'n':'A.R.S. 43-401(A),(E) [US-AZS5-020]. Same percentage applies to bonus and other emolument: no separate supplemental rate (medium-high).'}),
 ('income_tax','az.wh.rate_options','0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5 percent','US-AZS5-024','2026-01-01',None,{}),
 ('income_tax','az.wh.default_rate',2.0,'US-AZS5-024','2026-01-01',None,{'u':'percent','n':'Until the employee elects; A-4 due within 5 days of hire. Zero-percent election renewed yearly.'}),
 ('income_tax','az.wh.supplemental.rate','same elected percentage (no separate supplemental rate)','US-AZS5-020','2026-01-01',None,{'c':'medium'}),
 ('income_tax','az.wh.december_opt_out',True,'US-AZS5-020','2026-01-01',None,{'n':'43-401(B),(F): employer may elect not to withhold in December; tell ADOR and employees before 1 July.'}),
 ('income_tax','az.wh.a4c.remit_days_after_quarter',15,'US-AZS5-020','2026-01-01',None,{'u':'days','n':'A-4C credit-contribution reduction; employee statement within 30 days after year end or 15 days after termination.'}),
 ('income_tax','az.wh.exclusions','nonresident common-carrier employees; domestic service in private home; casual labour; seasonal hand farm labour; nonresidents present < 60 days (not athletes/entertainers); disaster-recovery workers','US-AZS5-021','2026-01-01',None,{'n':'A.R.S. 43-403.'}),
 ('non_resident','az.nonres.withholding_days_threshold',60,'US-AZS5-021','2026-01-01',None,{'u':'days','n':'Nonresident withheld after 60 days (or earlier by agreement). Form WEC exemptions: residents of CA, IN, OR, VA claiming the credit (unilateral; assessment-level credit 43-1096), MSRRA spouses, Native Americans on own reservation [US-AZS5-024]. Resident working outside AZ may opt in with A-4V.'}),
 ('non_resident','az.nonres.wec_states','CA, IN, OR, VA','US-AZS5-024','2026-01-01',None,{}),
 ('local_tax','az.local_wage_tax.exists',False,'US-AZR3-006','2026-01-01',None,{}),
 ('social_security','az.sui.wage_base',8000,'US-AZP9V-001','2026-01-01',None,{'u':U,'n':'Fixed (7,000 before 2023); not indexed.'}),
 ('social_security','az.sui.new_employer.rate',2.00,'US-AZP9V-001','2026-01-01','2026-12-31',{'u':'percent'}),
 ('social_security','az.sui.employer.rate.min',0.03,'US-AZR3-003','2026-01-01','2026-12-31',{'u':'percent','n':'2026 adjusted rates 0.03%-8.36% (UIT-0603A, A.R.S. 23-730).'}),
 ('social_security','az.sui.employer.rate.max',8.36,'US-AZP9V-001','2026-01-01','2026-12-31',{'u':'percent'}),
 ('social_security','az.sui.employee.rate',0,'US-AZR3-001','2026-01-01',None,{'u':'percent','n':'"You cannot take these taxes out of employee pay."'}),
 ('social_security','az.ui_operating_fund.rate_of_ui_liability',3.15,'US-AZR3-004','2027-01-01',None,{'u':'percent','n':'Each quarter of 2027 experience-rated employers pay 3.15% of UI liability to the UI Operating Fund (NOT 2026).'}),
 ('social_security','az.sdi_pfml.exists',False,'US-AZR3-005','2026-01-01',None,{'n':'No SDI/PFML or other levy [US-AZP9V-001, US-AZP9V-002].'}),
 ('payslip_statute','az.payslip.required_when','only for direct deposit or payroll card: written or electronic statement of earnings and withholdings, no content list (23-351(E),(F))','US-AZS5-001','2026-01-01',None,{}),
 ('payslip_statute','az.payslip.sick_time_fields','sick time available; sick time used year to date; pay received as sick time (on paycheck or attachment, every regular paycheck)','US-AZS5-011','2017-07-01',None,{'n':'A.R.S. 23-375(C); hard PSL/DD field set.'}),
 ('data_protection','az.records.payroll.retention_years',4,'US-AZS5-006','2026-01-01',None,{'u':'years','n':'23-364(D): hours each day, wages, sick time paid; employee may inspect and copy.'}),
 ('reporting_instruments','az.report.wh.annual.due','A1-R with W-2s due 31 January (43-412(B)); 30-day extension for good cause','US-AZS5-022','2026-01-01',None,{}),
 ('reporting_instruments','az.report.w2.format','EFW2 (Pub 701 rev. Jan 2025): mandatory electronic .txt via AZTaxes/AZFSET/transmitter; RS required, RV optional, state code 04; no SSN/EIN truncation; 1099s with AZ withholding direct to ADOR (Pub 1220)','US-AZS5-025','2025-01-01',None,{'c':'medium','n':'Edition: Jan 2025 text speaks of calendar 2024; 2026 edition not located.'}),
 ('reporting_instruments','az.newhire.report_days',20,'US-AZS5-012','2026-01-01',None,{'u':'days','n':'23-722.01: DES; electronic two transmissions a month <=16 days apart; includes first day of paid work; no employer penalty.'}),
 ('leave','az.leave.sick.accrual.hours_worked_per_hour',30,'US-AZS5-008','2017-07-01',None,{'u':'hours'}),
 ('leave','az.leave.sick.cap_hours.15_plus',40,'US-AZS5-008','2017-07-01',None,{'u':'hours','n':'Yearly cap 40 h (15+ employees) / 24 h (fewer than 15) unless higher.'}),
 ('leave','az.leave.sick.cap_hours.under_15',24,'US-AZS5-008','2017-07-01',None,{'u':'hours'}),
 ('leave','az.leave.sick.waiting_days',90,'US-AZS5-008','2017-07-01',None,{'u':'days'}),
 ('leave','az.leave.sick.rehire_reinstatement_months',9,'US-AZS5-008','2017-07-01',None,{'u':'months'}),
 ('leave','az.leave.sick.payout_on_separation',False,'US-AZS5-008','2017-07-01',None,{'n':'23-372(F). Paid at normal hourly rate, never below minimum wage; State of AZ and federal employers excluded.'}),
 ('termination','az.final_pay.discharge','within 7 working days or end of next regular pay period, whichever sooner; resignation: regular payday of the period','US-AZS5-003','2026-01-01',None,{'n':'23-353. No vacation-payout rule.'}),
 ('benefits_in_kind','az.irc_conformity_date','2026-01-01','US-AZS5-023','2026-01-01',None,{'n':'43-105(A); withholding base = federal wages, so federal exclusions flow through.'}),
 ('deductions_garnishments','az.deductions.rule','only when required by law, with prior revocable written authorization, or during a good-faith wage dispute (23-352)','US-AZS5-002','2026-01-01',None,{}),
 ('deductions_garnishments','az.garn.creditor.max_percent',10,'US-AZS5-016','2026-01-01',None,{'u':'percent','n':'33-1131(B): lesser of 10% of disposable earnings or excess over 60 x highest applicable minimum wage; support orders 50% exempt. 12-1598.10(F) still cites 25% (AZ OQ-6).'}),
 ('deductions_garnishments','az.garn.creditor.minwage_multiple',60,'US-AZS5-016','2026-01-01',None,{'u':'ratio'}),
 ('deductions_garnishments','az.garn.child_support.remit_business_days',2,'US-AZS5-018','2026-01-01',None,{'u':'business days','n':'25-504: start within 14 days; employer fee 1 per payment, max 4/month; report termination within 10 days; support priority.'}),
 ('deductions_garnishments','az.garn.child_support.employer_fee_per_payment',1,'US-AZS5-018','2026-01-01',None,{'u':U}),
 ('deductions_garnishments','az.garn.child_support.employer_fee_monthly_max',4,'US-AZS5-018','2026-01-01',None,{'u':U}),
]
LEGACY = [
 ('reporting_instruments','az.report.wh.deposit_schedule','under 200 average: annual A1-APR due 31 Jan; 200-1,500: quarterly; over 1,500: federal schedule; EFT mandatory at 500+; A1-QRT quarterly even if zero (+10 days for timely payers)','US-AZ-P5-2-005','2026-01-01',None,''),
 ('collective_agreements','az.prevailing_wage.state_mandate.exists',False,'US-AZ-P5-2-003','2026-01-01',None,'34-321(B) bars agencies from requiring prevailing wage.'),
]
CITED = ['US-AZS5-004','US-AZS5-009','US-AZS5-010','US-AZS5-014','US-AZS5-015','US-AZS5-017','US-AZS5-019','US-AZ-P5-1-001','US-AZ-P5-1-002','US-AZ-P5-1-003','US-AZ-WH-002','US-AZ-WH-003','US-AZ-P5-2-001','US-AZ-P5-2-002','US-AZ-P5-2-004','US-AZR3-002','US-AZL-001','US-AZL-002','US-AZP9M-001','US-AZP9L-002','US-AZS5-028']
NARR = {
 'labour_code': 'State minimum wage 2026/2027: the derived 15.15 (2026) and 15.65 (2027) rest on an unconfirmed 2025 base of 14.70 and on the tier-C MANUAL row US-AZS5-028 (ICA page 403). They are NOT facts (see unresolved az.minwage.hourly). The CPI-U steps are facts. Tipped cash wage likewise derived (12.15/12.65) and not emitted. Overtime: no AZ statute located; FLSA applies (medium). Flagstaff local rate unread.',
 'social_security': 'UI exclusions (23-615, 23-617) [US-AZS5-014, US-AZS5-015]: farm labour below 10 workers/20 weeks or 20,000 cash a quarter; family employment; students at own school; 501(c)(3) religious/charitable; churches and ministers; commission-only insurance, real estate, securities, tax-preparer salespeople; under-18 newspaper carriers; casual labour. Domestic UI threshold not extracted.',
 'reporting_instruments': 'Registration on JT-1 (ADOR + DES). POA 821-PSC / UIT-1146A. DES quarterly UI report UC-018: format/deadline open (des.az.gov 403).',
 'data_protection': '44-1373 SSN use rules [US-AZS5-019]; sick-time health info confidential (23-377) [US-AZS5-010]; new-hire data purpose limits [US-AZS5-012].',
 'live_change': '2027: Tucson 16.00; state 2027 poster published 2026-09-25 [US-AZP9M-001] (amount not read); UI Operating Fund 3.15% from 2027-01-01; IRC conformity to 2026-01-01. No ADOR/DES 2026 bulletin sweep (open).',
}
SPECIAL = '''- Domestic: no AZ withholding (43-403(A)(2)); UI threshold not extracted; Tucson MW excludes casual babysitting [US-AZS5-021, US-AZS5-027].
- Agricultural: no withholding for seasonal hand field labour except machine operators (may elect); UI farm thresholds [US-AZS5-021, US-AZS5-014].
- Minors: under-16 hours (23-233); under-18 newspaper carriers UI-excluded [US-AZS5-013, US-AZS5-014].
- Tipped: tip credit up to 3.00 (state and Tucson) [US-AZS5-005, US-AZS5-027].
- Clergy: churches/ministers UI-excluded; no withholding exception (federal wages) [US-AZS5-015, US-AZS5-024].
- Students: own-school students, student nurses/interns, co-op students UI-excluded [US-AZS5-014].
- NRAs / statutory employees: no AZ rule beyond federal; 60-day nonresident rule [US-AZS5-024, US-AZS5-021].
- Government: sick-time law and Tucson MW exclude State and US; school-district pay lag 7 business days [US-AZS5-007, US-AZS5-001].
- Native Americans on own reservation and MSRRA spouses: WEC exemption [US-AZS5-024].
- Nonresident common-carrier/motion-picture/disaster-recovery workers: excluded [US-AZS5-021, US-AZS5-020].'''
LANG = 'Sick-time notice in English and Spanish (23-375(B)) [US-AZL-001]; minimum-wage and sick-time posters en+es both required [US-AZP9M-001]; pay statement itself English (US-OWN-006).'
UNRES = [
 {'key':'az.minwage.hourly','why':'State minimum wage 2026 (15.15) and 2027 (15.65) are only derived from a 2025 base of 14.70 that no source read confirms; the ICA page returned 403 and the row is tier-C MANUAL (US-AZS5-028).','attempted':['https://www.azica.gov (403, Wayback 2026id_ also 403)'],'close':'ICA 2026 and 2027 minimum wage posters (single browser pass); BLS CPI-U from 2019 to check the 2021-2025 chain.','blocking':True},
 {'key':'az.local_minwage.flagstaff.hourly','why':'Flagstaff local minimum wage not read (guessed URL 404).','close':'flagstaff.az.gov minimum wage ordinance page, 2026 and 2027 values.','blocking':True},
 {'key':'az.report.sui.quarterly','why':'DES UC-018 quarterly wage report format, deadline and e-file mandate, UI separation notice and domestic UI threshold not read (des.az.gov 403).','attempted':['des.az.gov (403)'],'close':'DES UC-018 instructions and A.R.S. 23-613.01/23-615 remainder via browser pass.'},
 {'key':'az.wh.rounding','why':'No rounding rule in 43-401 or the ADOR pages read.','close':'A.A.C. R15-2B-101 on azsos.gov.'},
 {'key':'az.report.w2.pub701_edition','why':'Only the Jan 2025 Pub 701 (describing calendar 2024) was found; a 2026 edition not located.','close':'ADOR Pub 701 2026 edition (azdor.gov forms, 403 to curl; browser pass).'},
 {'key':'az.garn.creditor.statute_conflict','why':'33-1131(B) says 10% while 12-1598.10(F) still cites 25%; the 25-510 handling fee amount not read.','close':'Effective date of the Prop. 209 10% amendment and A.R.S. 25-510 text on azleg.'},
 {'key':'az.minwage.statute_23_362_current','why':'azleg serves only the 1997 version of 23-362; Prop. 202 definitional text unseen.','close':'Current 23-362 text (Prop. 202) via azleg or Westlaw public.'},
 {'key':'az.pit.departures_from_federal','why':'Form 140 additions/subtractions (HSA etc.) not read; assessment level, not withholding.','close':'ADOR Form 140 instructions 2026.','blocking':False},
 {'key':'az.live.bulletin_sweep','why':'ADOR and DES news/bulletins 2026-01-01 to date not swept (DES 403; budget).','close':'ADOR news archive and DES employer bulletins 2026 via browser pass.'},
]
