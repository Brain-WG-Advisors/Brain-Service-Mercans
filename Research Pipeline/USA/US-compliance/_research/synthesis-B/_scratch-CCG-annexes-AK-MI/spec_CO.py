NAME = 'Colorado'
SUMMARY = 'State minimum wage 15.16 (2026), Denver 19.29; overtime after 40/week or 12/day. Flat 4.40% withholding (DR 1098 method; DR 0004 optional; OBBBA overtime deduction not allowed for CO withholding). Occupational Privilege Taxes in Denver, Greenwood Village, Glendale (Sheridan tier C). UI chargeable wage limit 30,600 (2026) / 32,100 (2027), new employer 3.05% total; FAMLI 0.88% (2026, split 0.44/0.44) and 0.86% (2027). Wage Act pay statement + COMPS Rule 7 items. Several base figures (DR 1098 method, UI wage limit, FAMLI 2026) sit on legacy-id rows and are listed as non-fact lines pending re-key.'
U = 'USD'
C1 = 'US-COS5-001'
FACTS = [
 ('labour_code','co.minwage.hourly',15.16,C1,'2026-01-01','2026-12-31',{'u':U,'n':'COMPS Rule 3; highest applicable (local) minimum applies. 2027 15.71 is tier-B only (US-COS5-011 MANUAL), not a fact.'}),
 ('labour_code','co.minwage.tip_credit.max',3.02,C1,'2026-01-01','2026-12-31',{'u':U}),
 ('labour_code','co.minwage.tipped.cash_wage',12.14,C1,'2026-01-01','2026-12-31',{'u':U,'vm':'derived arithmetically','n':'15.16 - 3.02.'}),
 ('labour_code','co.minwage.minor_reduction.percent',15,C1,'2026-01-01',None,{'u':'percent','n':'Unemancipated minors; not for some local minimum wages.'}),
 ('labour_code','co.local_minwage.denver.hourly',19.29,'US-COS5-010','2026-01-01','2026-12-31',{'u':U,'n':'G-DERIVE: 18.81 x 1.0256 (CPI-W Denver-Aurora-Lakewood H1/H1) = 19.2915 -> 19.29.'}),
 ('labour_code','co.local_minwage.denver.tipped_food_beverage',16.27,'US-COS5-010','2026-01-01','2026-12-31',{'u':U,'n':'19.29 - 3.02, with at least 3.02 actual tips.'}),
 ('labour_code','co.overtime.rule','1.5x after 40 h/week, 12 h/day or 12 consecutive hours; no comp time; agriculture after 48 h (56 highly seasonal)',C1,'2026-01-01',None,{}),
 ('labour_code','co.overtime.daily_threshold_hours',12,C1,'2026-01-01',None,{'u':'hours'}),
 ('labour_code','co.exempt.salary.annual_min',57784,C1,'2026-01-01','2026-12-31',{'u':U}),
 ('labour_code','co.rest_break.paid_minutes_per_4h',10,C1,'2026-01-01',None,{'u':'minutes','n':'Unprovided rest time paid as extra pay; meal 30 min for shifts over 5 h.'}),
 ('labour_code','co.pay_frequency.rule','period no longer than one calendar month or 30 days; payday no later than 10 days after period close unless agreed (8-4-103(1)(a)); paydays posted','US-COS5-002','2025-08-06',None,{}),
 ('labour_code','co.payment.method','checks negotiable without discount; direct deposit only with voluntary authorisation; paycard only with free access to full net pay once per period or alternative (8-4-102)','US-COS5-002','2025-08-06',None,{}),
 ('income_tax','co.pit.rate.flat',4.40,'US-COS5-012','2026-01-01','2026-12-31',{'u':'percent','n':'DR 0004 line 3 at 4.40%; method in DR 1098 2026 [US-COP51-001 legacy]. DR 1098 for 2027 not yet published.'}),
 ('income_tax','co.wh.std_allowance.dr1098.single',5500,'US-COS5-012','2026-01-01','2026-12-31',{'u':U,'c':'medium','n':'DR 1098: subtract 5,500 (11,000 MFJ/QSS) or DR 0004 line 2.'}),
 ('income_tax','co.wh.dr0004.table1.single.1_job',14000,'US-COS5-012','2026-01-01','2026-12-31',{'u':U,'n':'Single/MFS 14,000 / 7,000 / 4,500 / 3,500 by jobs 1/2/3/4+.'}),
 ('income_tax','co.wh.dr0004.table1.hoh.1_job',22000,'US-COS5-012','2026-01-01','2026-12-31',{'u':U,'n':'HoH 22,000 / 11,000 / 7,500 / 5,500.'}),
 ('income_tax','co.wh.dr0004.table1.mfj.1_job',30000,'US-COS5-012','2026-01-01','2026-12-31',{'u':U,'n':'MFJ/QSS 30,000 / 15,000 / 10,000 / 7,500.'}),
 ('income_tax','co.wh.obbba_overtime_deduction.allowed',False,'US-COS5-012','2026-01-01',None,{'n':'Worksheet 1 removes the qualified overtime deduction from W-4 Step 4(b); confirmed in the Guide [US-COS5-007].'}),
 ('income_tax','co.wh.wages.conformity','wages subject to CO withholding = wages subject to federal withholding; federal exclusions generally flow through','US-COS5-007','2026-01-01',None,{}),
 ('income_tax','co.wh.exempt_w4_copy_threshold_weekly',200,'US-COS5-006','2026-01-01',None,{'u':U,'n':'W-4 claiming exempt with pay over 200/week and no DR 0004: copy to CDOR.'}),
 ('non_resident','co.nonres.rules','residents: all wages except where another state requires withholding; nonresidents: CO-source wages by days present; federal carve-outs rail/air (<=50% CO pay)/motor carrier/military/military spouse; telecommuters not taxed on work outside CO','US-COS5-007','2026-01-01',None,{'n':'No reciprocity (Guide word search).'}),
 ('local_tax','co.local.opt.greenwood_village.employee_monthly',2,'US-COS5-015','2026-01-01',None,{'u':U,'n':'Employer 2/month; trigger 250+ earned in the month in the Village; multiple OPT cities: city where most work done, primary employer only.'}),
 ('local_tax','co.local.opt.greenwood_village.employer_monthly',2,'US-COS5-015','2026-01-01',None,{'u':U}),
 ('local_tax','co.local.opt.greenwood_village.threshold_monthly',250,'US-COS5-015','2026-01-01',None,{'u':U}),
 ('local_tax','co.local.opt.glendale.employee_monthly',5,'US-COS5-016','2026-01-01',None,{'u':U,'n':'Employer 5/month; trigger more than 750 in the month.'}),
 ('local_tax','co.local.opt.glendale.employer_monthly',5,'US-COS5-016','2026-01-01',None,{'u':U}),
 ('local_tax','co.local.opt.glendale.threshold_monthly',750,'US-COS5-016','2026-01-01',None,{'u':U}),
 ('local_tax','co.local.opt.denver.employee_monthly',5.75,'US-COP7-004','2025-01-01',None,{'u':U,'c':'medium','n':'Earnings >= 500/month; 2025 Tax Guide edition, 2026 edition not read (CO-OQ-5).'}),
 ('local_tax','co.local.opt.denver.employer_monthly',4.00,'US-COP7-005','2025-01-01',None,{'u':U,'c':'medium','n':'2026 edition not read.'}),
 ('local_tax','co.local.opt.denver.threshold_monthly',500,'US-COP7-004','2025-01-01',None,{'u':U,'c':'medium'}),
 ('social_security','co.famli.rate.total',0.86,'US-COS5-008','2027-01-01',None,{'u':'percent','n':'2027 total; split and <10-employee exemption not read on a primary page (US-COP7-001 MANUAL).'}),
 ('social_security','co.sui.coverage','follows FUTA thresholds: employer 20 weeks / 1,500 quarter; agricultural 10 workers in 20 weeks or 20,000 quarter; domestic 1,000 quarter; excluded commission insurance/real-estate agents, casual labour, part-time for exempt nonprofits, students at own school','US-COS5-014','2023-01-01',None,{'c':'medium'}),
 ('payslip_statute','co.payslip.comps_rule7_items','total pay, rate, tips, credits and time worked (in addition to Wage Act items); kept 3 years',C1,'2026-01-01',None,{}),
 ('reporting_instruments','co.report.wh.frequency','< 7,000/yr quarterly (last day of month after quarter); 7,000-50,000 monthly (15th); >= 50,000 weekly Sat-Fri (3rd business day after Friday, EFT mandatory); zero returns required; paper DR 1094','US-COS5-006','2026-01-01',None,{}),
 ('reporting_instruments','co.report.wh.quarterly_threshold',7000,'US-COS5-006','2026-01-01',None,{'u':U}),
 ('reporting_instruments','co.report.wh.weekly_threshold',50000,'US-COS5-006','2026-01-01',None,{'u':U}),
 ('reporting_instruments','co.report.w2','due 31 January to employees and CDOR; e-file mandatory when federal e-file required (10+); Revenue Online .txt or XLSX template (10-100 employees, TY2026); paper with DR 1093; DR 0995 credit notice to every employee','US-COS5-006','2026-01-01',None,{}),
 ('reporting_instruments','co.report.w2.xlsx_template','RE: tax year, employer name, ID type, EIN, address; RS: ID type/EIN, names, SSN (999999999 if none), address, boxes 1, 2, 15, 16, 17; optional local 18-20, second state, dates, weeks, SUI wages','US-COS5-013','2026-01-01',None,{}),
 ('reporting_instruments','co.report.famli.quarterly','My FAMLI+ Employer, due one month after quarter end; file and API specs published; ITINs in bulk files from 2026-10-01','US-COS5-008','2026-01-01',None,{}),
 ('leave','co.leave.sick.accrual.hours_worked_per_hour',30,'US-COS5-005','2022-01-01',None,{'u':'hours','n':'HFWA 2023 text (partial row): cap 48 h/yr; carry over up to 48; front-load allowed; no payout; reinstated on rehire within 6 months; PHE supplement 80 h; amendments 2024-2026 unchecked.'}),
 ('leave','co.leave.sick.cap_hours',48,'US-COS5-005','2022-01-01',None,{'u':'hours'}),
 ('leave','co.leave.sick.payout_on_separation',False,'US-COS5-005','2022-01-01',None,{}),
 ('termination','co.final_pay.rule','discharge: immediately (6 h after next workday start if payroll unit closed, 24 h if off-site); resignation: next regular payday; unclaimed check mailed after 60 days','US-COS5-003','2025-08-06',None,{}),
 ('termination','co.final_pay.penalty.min',1000,'US-COS5-003','2025-08-06',None,{'u':U,'n':'Greater of 2x unpaid wages or 1,000 if unpaid 14 days after written demand (8-4-109(3)(b)).'}),
 ('termination','co.final_pay.vacation_payout',True,'US-COS5-003','2025-08-06',None,{'n':'Earned and determinable vacation is wages (8-4-101(14)(a)(III)); owed even if fired for cause [US-COS5-001]. Severance not wages.'}),
 ('benefits_in_kind','co.lodging_credit.weekly_min',25,C1,'2026-01-01',None,{'u':U,'n':'Lodging credit 25-100/week; meals at cost or value; no uniform charges.'}),
 ('benefits_in_kind','co.lodging_credit.weekly_max',100,C1,'2026-01-01',None,{'u':U}),
 ('deductions_garnishments','co.deductions.permitted','(a) required by law; (a.5) auto-enrolment retirement; (b) written agreement for loans/advances/goods/equipment; (c) theft after police report; (d) revocable authorisation; (e) unreturned property of terminated employee with notice within 10 days (8-4-105)','US-COS5-004','2025-08-06',None,{}),
 ('deductions_garnishments','co.garn.creditor.max_percent',20,'US-COS5-009','2022-01-01',None,{'u':'percent','c':'medium','n':'Form 26 SC (R 1/22): exempt greater of 80% of disposable earnings or 40x/80x/86.67x/173.3x higher of state/federal MW; disposable earnings also deduct employer-provided health insurance (CO departure); support first; start first pay date >= 21 days after service.'}),
 ('deductions_garnishments','co.garn.creditor.weekly_floor',606.40,'US-COS5-009','2026-01-01','2026-12-31',{'u':U,'vm':'derived arithmetically','n':'40 x 15.16.'}),
]
LEGACY = [
 ('income_tax','co.wh.method','annualise; subtract 5,500 (11,000 MFJ/QSS) or DR 0004 line 2; x 4.40%; divide by periods; add DR 0004 line 3; no supplemental rate, no rounding rule','US-COP51-001','2026-01-01',None,'DR 1098 (2026).'),
 ('social_security','co.sui.wage_base',30600,'US-COP51-003','2026-01-01','2026-12-31','Chargeable wage limit; 32,100 for 2027; employer only.'),
 ('social_security','co.sui.wage_base.next_year',32100,'US-COP51-003','2027-01-01',None,''),
 ('social_security','co.sui.new_employer.rate.total',3.05,'US-COP51-004','2026-01-01','2026-12-31','1.53% + support surcharge 0.17% + solvency 1.35% (non-construction); heavy construction 6.285%; 2027 1.70% combined, no solvency.'),
 ('social_security','co.famli.rate.total.2026',0.88,'US-COFAMLI-001','2026-01-01','2026-12-31','0.44% employer + 0.44% employee on wages up to the SS wage base (184,500); statutory cap 1.2%.'),
 ('payslip_statute','co.payslip.items','gross wages, withholdings/deductions, net wages, pay-period dates, employee name or SSN, employer name and address; at least monthly or each payment; records 3 years; fine up to 250 per employee per month max 7,500 (8-4-103(4))','US-COP51-005','2025-08-06',None,''),
 ('collective_agreements','co.prevailing_wage.threshold',500000,'US-COP52-002','2026-01-01',None,'C.R.S. 24-92-201 ff.; weekly pay required.'),
]
CITED = ['US-COP51-002','US-COP51-006','US-COP52-001','US-COP52-003','US-COL-001','US-COL-002','US-COP9L-001','US-COP7-001','US-COP7-006','US-COS5-011']
NARR = {
 'labour_code': '2027 state 15.71 / tipped 12.69 and Denver 19.84, and 2026 Edgewater 18.17 / Boulder 16.82 are tier-B leads only [US-COS5-011 MANUAL]: not facts (CO-OQ-3).',
 'local_tax': 'OPTs are flat monthly amounts on separate city returns (T4). Sheridan 3+3 rests on tier-C MANUAL US-COP7-006: not a fact. Aurora OPT repealed 2025 (corroborated only).',
 'social_security': 'Experienced-employer support/solvency surcharges rest on MANUAL rows (US-COL-004, US-COP7-002/003). No employee UI share. FAMLI wage cap follows the SS wage base (FED). Employee may top up FAMLI with PTO.',
 'payslip_statute': 'Electronic delivery consent: no rule read (open). SSN may appear instead of name (8-4-103(4)(e)).',
 'reporting_instruments': 'UI quarterly wage report format/due date not read (CDLE 403); TPA authorisation in MyUI Employer+ [US-COP52-003 legacy]. New hire: CO page unreachable, federal default 20 days (42 USC 653a, FED unit). POA DR 0145.',
 'indexation': 'State MW CPI-indexed yearly (PAY CALC Order/COMPS poster); Denver CPI-W H1/H1; EAP threshold yearly; UI limit statutory steps 27,200 -> 30,600 -> 32,100; FAMLI set yearly (cap 1.2%); OPTs fixed.',
 'data_protection': 'C.R.S. 6-1-713/-713.5/-716 not read (coag.gov 202-empty). No truncation duty on the pay statement.',
 'live_change': 'FAMLI 2027 0.86%; UI 2027 base 32,100 and new 1.70%; OBBBA overtime decoupling; XLSX W-2 route; FAMLI ITIN files 2026-10-01; SecureSavings registration duty (programme page not read). CDLE news and Colorado Register not swept (403).',
}
SPECIAL = '''- Domestic: UI FUTA threshold 1,000/quarter [US-COS5-014].
- Agricultural: OT after 48 h (56 seasonal); migratory-laborer disclosures in worker language (8-4-117); 5% language rule [US-COS5-001, US-COS5-014, US-COL-002, US-COP9L-001].
- Minors: 15% below state MW for unemancipated minors [US-COS5-001].
- Tipped: tip credit 3.02; state 12.14; Denver 16.27; tips employee property [US-COS5-001, US-COS5-010, US-COS5-002].
- Clergy / statutory employees: no state rule beyond federal [US-COS5-007, US-COS5-014].
- Students: UI excludes students at own school (not student nurses) [US-COS5-014].
- NRAs: W-2 template SSN 999999999 if none, CO withholding required without valid TIN; FAMLI accepts ITINs [US-COS5-013, US-COS5-008].
- Government: Wage Act excludes state/counties/municipalities/school districts; HFWA includes them, excludes federal [US-COS5-002, US-COS5-005].
- Military/spouses and interstate transport: nonresident exemptions [US-COS5-007].
- Multistate: HFWA covers all employees working in CO (only CO hours accrue - inference); SUI other-state credit and FAMLI multistate coverage open.'''
LANG = 'CO 8-13.3-408(2) English + first language of 5% of workforce for HFWA notice [US-COL-001]; COMPS Rule 7.4.3 Spanish COMPS/poster [US-COP9L-001]; DR 0995 notice in English plus usual language [US-COS5-006]; payslip English (US-OWN-006).'
UNRES = [
 {'key':'co.sui.wage_base.other_state_credit','why':'C.R.S. 8-76-102 text and CDLE premiums page unreachable (403).','close':'C.R.S. 8-76-102 text, CDLE Employer Handbook, or DOL Significant Provisions of State UI Laws 2026 CO line.'},
 {'key':'co.famli.split.next_year','why':'2027 employee/employer split, under-10-employee employer exemption and multistate coverage not read on a primary page (famli.colorado.gov 403).','close':'7 CCR 2702-3 and C.R.S. 8-13.3-507 via famli.colorado.gov or Colorado Register (browser pass).','blocking':True},
 {'key':'co.local_minwage.other_cities','why':'Edgewater, City of Boulder, Boulder County 2026 and state/Denver 2027 values are tier B only; the CDLE PAY CALC Order (7 CCR 1103-14) is a 403 page.','close':'CDLE 2026/2027 PAY CALC Order and Denver Finance 2026 news release (browser pass).','blocking':True},
 {'key':'co.report.sui.quarterly','why':'CDLE MyUI Employer+ wage-report format/due date and CO new-hire specifics not read (CDLE 403; childsupport.colorado.gov timeout).','close':'CDLE MyUI Employer+ wage-report guide and Colorado State Directory of New Hires page.'},
 {'key':'co.local.opt.denver.current_edition','why':'Denver OPT figures come from the 2025 Tax Guide; 2026 edition not read; Sheridan only tier C.','close':'Denver Tax Guide Topic 61 2026 revision and the Sheridan city page.'},
 {'key':'co.leave.sick.amendments_and_payslip_econsent','why':'HFWA amendments 2024-2026 and electronic pay-statement consent unread (CDLE 403).','close':'CDLE current HFWA text and INFO #6/#13 (browser pass).'},
 {'key':'co.data_protection.statutes','why':'6-1-713/-713.5/-716 and SecureSavings payroll-deduction duties unread (coag.gov 202-empty).','close':'coag.gov data-protection page and the Colorado SecureSavings employer page.','blocking':False},
]
