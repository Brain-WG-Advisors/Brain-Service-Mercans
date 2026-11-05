NAME = 'Illinois'
SUMMARY = 'State minimum wage 15.00 (not indexed), Chicago 17.05 and suburban Cook 15.40 from 2026-07-01 (both indexed); weekly overtime. Flat 4.95% withholding on wages less IL-W-4 exemptions (2,925 + 1,000); no supplemental rate; reciprocity IA/KY/MI/WI; 30-day nonresident rule; no local tax. UI base 14,250, new 3.350%, no employee share; no SDI/PFML. PLAWA paid leave statewide (not in Chicago/Cook). Pay stub retention 3 years, copy rules. IL-941 quarterly, no annual reconciliation; monthly UI wage report for 25+. Oracle: IL-700-T examples 8.38 / 32.13.'
U = 'USD'
T = 'US-ILR3-001'
FACTS = [
 ('labour_code','il.minwage.hourly',15.00,'US-ILS5-001','2025-01-01',None,{'u':U,'vm':'second independent authority','n':'820 ILCS 105/4, adults 18+; no later step, no indexation [US-ILS5-002].'}),
 ('labour_code','il.minwage.youth.hourly',13.00,'US-ILS5-001','2025-01-01',None,{'u':U,'n':'Under 18 working <= 650 h/calendar year.'}),
 ('labour_code','il.minwage.new_hire_reduction',0.50,'US-ILS5-001','2025-01-01',None,{'u':U,'n':'First 90 consecutive days, not day/temporary laborers.'}),
 ('labour_code','il.minwage.tipped.cash_wage',9.00,'US-ILS5-001','2025-01-01',None,{'u':U,'n':'Tip credit up to 40%.'}),
 ('labour_code','il.minwage.coverage.min_employees',4,'US-ILS5-026','2026-01-01',None,{'u':'employees','n':'105/3: fewer than 4 outside the law except domestic workers; also small farms, outside salesmen, religious organisation members, own-college students, etc.'}),
 ('labour_code','il.local_minwage.chicago.hourly',17.05,'US-ILS5-008','2026-07-01','2027-06-30',{'u':U,'n':'Employers 4+; tipped 12.96 (17.05 x 0.76 = 12.958); City contracts 18.50; indexed July 1 by CPI capped 2.5%.'}),
 ('labour_code','il.local_minwage.chicago.tipped',12.96,'US-ILS5-008','2026-07-01','2027-06-30',{'u':U}),
 ('labour_code','il.local_minwage.cook.hourly',15.40,'US-ILS5-009','2026-07-01',None,{'u':U,'n':'Suburban Cook County, employees over 18 with >= 2 h/week in the County; Chicago and opted-out municipalities excluded; tipped 9.25; OT 23.10 (15.40 x 1.5); tipped OT 16.94.'}),
 ('labour_code','il.local_minwage.cook.tipped',9.25,'US-ILS5-009','2026-07-01',None,{'u':U}),
 ('labour_code','il.overtime.weekly_threshold_hours',40,'US-ILS5-001','2026-01-01',None,{'u':'hours','n':'105/4a; no daily OT; exemptions 4a(2).'}),
 ('labour_code','il.pay_frequency.rule','at least semi-monthly, paid within 13 days after period end; EAP and commissions monthly (115/3)','US-ILS5-003','2026-01-01',None,{}),
 ('labour_code','il.payment.method','direct deposit must be voluntary; cash with signed receipt; payroll card voluntary with written fee disclosure, revocable; card/DD offerors must also offer cash or check (115/4, 115/14.5)','US-ILS5-005','2026-01-01',None,{'n':'Payroll card rules [US-ILS5-007].'}),
 ('income_tax','il.pit.rate.flat',4.95,T,'2026-01-01',None,{'u':'percent','n':'IL-700-T R-12/25 re-verified byte-identical 2026-11-02; 35 ILCS 5/201 not read this pass.'}),
 ('income_tax','il.wh.method','.0495 x (wages - exemptions/periods) + IL-W-4 Line 3; exemptions = Line 1 x 2,925 + Line 2 x 1,000 per year',T,'2026-01-01','2026-12-31',{'n':'No rounding rule (tables in cents); no separate supplemental rate - bonus/OT/commission are wages [US-ILR3-002].'}),
 ('income_tax','il.wh.exemption.line1',2925,T,'2026-01-01','2026-12-31',{'u':U,'n':'Indexed by IDOR.'}),
 ('income_tax','il.wh.exemption.line2',1000,T,'2026-01-01','2026-12-31',{'u':U}),
 ('income_tax','il.wh.certificate','IL-W-4 R-07/23 current; no exemptions if AGI > 500k joint / 250k other; none on file = no exemptions; changes effective next quarter date at least 30 days after filing','US-ILS5-010','2023-07-01',None,{}),
 ('non_resident','il.reciprocity.states','IA, KY, MI, WI','US-ILS5-014','2026-01-01',None,{'n':'IL-W-5-NR; military spouses excluded.'}),
 ('non_resident','il.nonres.days_threshold',30,'US-ILS5-014','2026-01-01',None,{'u':'days','n':'No withholding for nonresident with fewer than 31 days of non-localized IL service; IL-W-6 day certificate when > 30 days expected; carrier rules (air > 50% flight miles). IL resident working only in a withholding state: no IL withholding.'}),
 ('local_tax','il.local_wage_tax.exists',False,'US-IL-P5-2-001','2026-01-01',None,{}) if False else ('local_tax','il.local_wage_tax.note','none administered by IDOR (see legacy row US-IL-P5-2-001)','US-ILS5-014','2026-01-01',None,{'c':'medium'}),
 ('social_security','il.sui.wage_base',14250,'US-ILS5-015','2026-01-01','2026-12-31',{'u':U,'n':'2025: 13,916; same values as US-IL-002; 820 ILCS 405/235 formula not read; 2027 expected Dec 2026.'}),
 ('social_security','il.sui.new_employer.rate',3.350,'US-ILS5-015','2026-01-01','2026-12-31',{'u':'percent','n':'Administrative Support & Waste Management 3.450%.'}),
 ('social_security','il.sui.employer.rate.min',0.750,'US-ILS5-015','2026-01-01','2026-12-31',{'u':'percent','n':'Range 0.750%-7.050% incl. fund builder 0.550%; small-employer option 5.4%; state experience factor 102%.'}),
 ('social_security','il.sui.employer.rate.max',7.050,'US-ILS5-015','2026-01-01','2026-12-31',{'u':'percent'}),
 ('social_security','il.sui.fund_builder.rate',0.550,'US-ILS5-015','2026-01-01','2026-12-31',{'u':'percent'}),
 ('social_security','il.sui.employee.rate',0,'US-ILS5-015','2026-01-01',None,{'u':'percent','c':'medium'}),
 ('payslip_statute','il.payslip.rules','pay stub each pay period; itemized deductions; payroll-card payees also hours, rate, deductions; stubs kept >= 3 years; copies within 21 days on request (max twice/12 months; former employees 1 year after separation); offer prior-year stubs if electronic access ends (115/10, P.A. 103-953)','US-ILS5-024','2025-01-01',None,{}),
 ('payslip_statute','il.payslip.copy_response_days',21,'US-ILS5-024','2025-01-01',None,{'u':'days'}),
 ('data_protection','il.records.paystub.retention_years',3,'US-ILS5-024','2025-01-01',None,{'u':'years'}),
 ('reporting_instruments','il.report.wh.il941','IL-941 quarterly, electronic, due last day of month after quarter (2026: 04-30, 07-31, 11-02, 2027-02-01); no annual reconciliation','US-ILS5-011','2026-01-01',None,{'n':'Dates [US-ILS5-012].'}),
 ('reporting_instruments','il.report.wh.deposit','monthly (15th) when look-back <= 12,000; semi-weekly (federal Wed/Fri, electronic) when > 12,000; IL-501','US-ILS5-011','2026-01-01',None,{}),
 ('reporting_instruments','il.report.wh.semiweekly_threshold',12000,'US-ILS5-011','2026-01-01',None,{'u':U}),
 ('reporting_instruments','il.report.w2','electronic only: MyTax (manual, CSV, EFW2 under IDR-996) or bulk EFW2 with ETIN (IDR-986); due Jan 31 (2026 W-2s by 2027-02-01); 1099/W-2G bulk via IRIS (IDR-987) from 2026-09-18','US-ILS5-013','2026-09-18',None,{}),
 ('reporting_instruments','il.report.sui.quarterly','UI-3/40 wage report + contributions due Apr 30 / Jul 31 / Oct 31 / Jan 31','US-ILS5-016','2026-01-01',None,{}),
 ('reporting_instruments','il.report.sui.monthly.employer_threshold',25,'US-ILS5-017','2026-01-01',None,{'u':'employees','n':'Monthly wage report for months 1 and 2 of each quarter: name, SSN, wages; MyTax CSV only (P.A. 97-0689).'}),
 ('reporting_instruments','il.newhire.report_days',20,'US-ILS5-018','2026-01-01',None,{'u':'days','n':'From first day on payroll; rehires and independent contractors.'}),
 ('leave','il.leave.plawa.accrual','1 h per 40 h worked up to 40 h per 12 months (front-load allowed); use after 90 days; exempt deemed 40 h/week; no separation payout unless in a vacation/PTO bank; tipped/commissioned paid at least full MW; not in Chicago/Cook','US-ILS5-019','2024-01-01',None,{'c':'medium'}),
 ('leave','il.leave.plawa.cap_hours',40,'US-ILS5-019','2024-01-01',None,{'u':'hours','c':'medium'}),
 ('leave','il.leave.chicago.accrual','1 h paid leave AND 1 h paid sick leave per 35 h worked from day 1 for anyone with >= 80 h in 120 days; notices with first paycheck and around July 1','US-ILS5-020','2024-07-01',None,{'c':'medium','n':'[partial row] caps, carryover and payout unread.'}),
 ('termination','il.final_pay.rule','in full at separation if possible, no later than next regularly scheduled payday (discharge or resignation); mailed on written request (115/5)','US-ILS5-023','2026-01-01',None,{}),
 ('termination','il.final_pay.vacation_payout',True,'US-ILS5-004','2026-01-01',None,{'n':'Earned vacation paid at final rate, no forfeiture (CBA exception); use-it-or-lose-it allowed with notice (56 IAC 300.520). No statutory severance.'}),
 ('benefits_in_kind','il.wh.wages.conformity','IL withholding follows federal (wages subject to federal withholding); federal exclusions follow; no departure found (not proven)','US-ILR3-002','2026-01-01',None,{'c':'medium'}),
 ('deductions_garnishments','il.deductions.rule','only if required by law, for employee benefit, or wage assignment/order or express written consent at time of deduction; cash advance repayment max 15% per paycheck','US-ILS5-006','2026-01-01',None,{'c':'medium'}),
 ('deductions_garnishments','il.garn.creditor.max_percent_gross',15,'US-ILS5-022','2026-01-01',None,{'u':'percent','n':'735 ILCS 5/12-803: lesser of 15% of GROSS or disposable - 45 x greater of federal/IL MW.'}),
 ('deductions_garnishments','il.garn.creditor.weekly_floor',675,'US-ILS5-022','2025-01-01',None,{'u':U,'vm':'derived arithmetically','n':'45 x 15.00.'}),
 ('deductions_garnishments','il.garn.child_support.employer_fee_monthly',5,'US-ILS5-021','2026-01-01',None,{'u':U,'n':'HFS 3683; remit 1-7 business days after payday; up to 50% of disposable; multiple orders pro rata.'}),
 ('data_protection','il.bipa.retention_max_years',3,'US-ILS5-025','2026-01-01',None,{'u':'years','n':'740 ILCS 14/15: written policy, destroy within 3 years of last interaction; notice + written release before collection (biometric time clocks).'}),
 ('live_change','il.live.14c_end','14(c) sub-minimum licences end 2029-12-31 (enacted)','US-ILS5-002','2029-12-31',None,{}),
 ('oracle','il.oracle.il700t.example1.withholding',8.38,T,'2026-01-01','2026-12-31',{'u':U,'n':'IL-700-T: 300 weekly, 2 + 1 allowances.'}),
 ('oracle','il.oracle.il700t.example2.withholding',32.13,T,'2026-01-01','2026-12-31',{'u':U,'vm':'derived arithmetically','n':'800 weekly, 2 + 2 allowances: 7,850/52 = 150.96; 649.04 x .0495 = 32.13.'}),
]
FACTS = [f for f in FACTS if f[1] != 'il.local_wage_tax.note']
LEGACY = [
 ('local_tax','il.local_wage_tax.exists',False,'US-IL-P5-2-001','2026-01-01',None,'None administered by IDOR.'),
 ('social_security','il.sdi_pfml.exists',False,'US-IL-P5-2-003','2026-01-01',None,'PLAWA is an employer-provided benefit, not a premium.'),
]
CITED = ['US-IL-002','US-IL-P5-1-001','US-IL-P5-2-002','US-IL-P5-2-004','US-IL-004','US-ILP9L-001','US-ILS5-007','US-ILS5-012']
NARR = {
 'social_security': 'Levies: Secure Choice Roth IRA payroll deduction [US-IL-P5-2-002 legacy]; no other levy.',
 'termination': 'IDES lists "Employee Separation Information" as an employer obligation [US-ILS5-018]; the notice/form to the employee not identified.',
 'collective_agreements': 'Prevailing Wage Act 820 ILCS 130: IDOL county rates, certified payroll portal [US-IL-P5-2-004 legacy]. CBA can override vacation payout (115/5).',
 'indexation': 'State MW not indexed; Chicago July 1 CPI capped 2.5%; Cook July 1 CPI (suspended if County unemployment >= 8.5%); UI base yearly; PIT exemption indexed by IDOR; garnishment floor 45 x MW. Chicago CPI derivation impossible (2025 rate not registered).',
 'data_protection': 'No SSN truncation rule found (815 ILCS 505/2RR and 530 not read).',
}
SPECIAL = '''- Domestic: MW Law even under 4 employees; IL withholding only if federal withheld voluntarily [US-ILS5-026, US-ILR3-002].
- Agricultural: no state OT; small farms (<= 500 man-days/quarter), family, some piece-rate harvesters outside MW [US-ILS5-001, US-ILS5-026].
- Minors: 13.00 under 18 <= 650 h/yr; Cook ordinance not under 18 [US-ILS5-001, US-ILS5-009].
- Tipped: state 9.00; Chicago 12.96; Cook 9.25; PLAWA paid at full MW [US-ILS5-001, US-ILS5-008, US-ILS5-009, US-ILS5-019].
- Clergy: religious organisation members outside MW; ministers no IL withholding [US-ILS5-026, US-ILS5-014].
- Students: own-college students outside MW; part-time college students at own school PLAWA-exempt [US-ILS5-026, US-ILS5-019].
- NRAs / statutory employees: follow federal [US-ILR3-002].
- Government: IWPCA excludes State and federal employees; MW covers governmental bodies; UI reimbursement option [US-ILS5-003, US-ILS5-001, US-ILS5-016].
- Other-state residents: reciprocity IA/KY/MI/WI, 30-day rule, IL-W-6 [US-ILS5-014].'''
LANG = 'No language requirement [US-ILP9L-001]; payslip English (US-OWN-006).'
UNRES = [
 {'key':'il.leave.chicago.paid_leave.payout','why':'Chicago Paid Leave caps, carryover and separation payout by employer size not read (partial row).','close':'BACP FAQ PDF or OLS Paid Leave rules (browser pass) or MCC 6-130.','blocking':True},
 {'key':'il.leave.cook.paid_leave','why':'Cook County Paid Leave Ordinance not read.','close':'Cook County Commission on Human Rights Paid Leave FAQ (cookcountyil.gov).','blocking':True},
 {'key':'il.local_minwage.chicago.tipped_schedule','why':'One Fair Wage phase-out percentage for 2026 not read (12.96 = 76% of 17.05).','close':'MCC 6-105-020 text or BACP 2026 notice.'},
 {'key':'il.termination.ui_separation_notice','why':'Whether Illinois requires a separation notice to the employee not identified.','close':'56 Ill. Adm. Code 2770 / 820 ILCS 405 via ftp.ilga.gov or the IDES employer handbook.'},
 {'key':'il.pit.rate.statutory','why':'35 ILCS 5/201(b)(5.4) not read; no 2027 change confirmed.','close':'ftp.ilga.gov/ILCS/Ch 0035/Act 0005 section 201 + IDOR news.','blocking':False},
 {'key':'il.sui.wage_base.next_year','why':'2027 wage base unpublished; 405/235 formula not read.','close':'IDES 2027 rate chart (Dec 2026) and 820 ILCS 405/235 via ftp.ilga.gov.'},
 {'key':'il.payslip.content_list','why':'56 Ill. Adm. Code 300.600 content items not read.','close':'ftp.ilga.gov/JCAR Title 56 Part 300.'},
 {'key':'il.data_protection.ssn_paystub','why':'815 ILCS 505/2RR and 815 ILCS 530 not read.','close':'Those sections via ftp.ilga.gov.','blocking':False},
 {'key':'il.pit.conformity_statement','why':'No IDOR decoupling statement (HSA, 125) read.','close':'IDOR Pub. 101 / IL-1040 subtraction list.','blocking':False},
 {'key':'il.live.news_sweep','why':'IDOL/IDOR/IDES newsrooms 2026 not swept.','close':'One sweep of tax.illinois.gov/research/news.html, labor.illinois.gov/news.html, ides.illinois.gov newsroom.'},
]
