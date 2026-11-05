NAME = 'Alabama'
SUMMARY = 'No state minimum wage, overtime, pay-statement, final-pay or sick-leave statute (federal FLSA applies; local mandates pre-empted by Ala. Code 25-7-41). State income tax withheld on the booklet formula with federal FIT as a deduction (FIT must be computed before AL SIT); A4 certificate; municipal occupational taxes (T4, no state census). SUI wage base 8,000, new employer 2.70%, no employee UI, no SDI/PFML. Stage-5 confidence: state 85-95%, local 55%.'
U = 'USD'
B = 'US-ALS5-001'
FACTS = [
 ('labour_code','al.minwage.state.exists',False,'US-ALS5-010','2016-02-25',None,{'c':'medium','n':'Agency states AL has no state wage-hour laws; federal 7.25 applies (FED unit). 25-7-41(b)-(c) voids local wage/leave mandates (public employees excepted, 25-7-43).'}),
 ('labour_code','al.local_wage_leave_mandates.preempted',True,'US-ALS5-010','2016-02-25',None,{}),
 ('labour_code','al.equal_pay.wage_history_refusal_protected',True,'US-ALS5-015','2026-01-01',None,{'n':'Clarke-Figures Equal Pay Act, 25-1-30 (sex and race).'}),
 ('income_tax','al.wh.method','annualise; subtract standard deduction (phase-out by GI), annualised federal FIT withheld, personal exemption, dependents; apply 2/4/5% brackets; divide by pay periods',B,'2026-01-01',None,{'n':'Booklet rev. 01/2026 p. 6; Ala. Code 40-18-71/-74 [US-ALS5-011]. Order FIT before AL SIT.'}),
 ('income_tax','al.wh.federal_fit_deductible',True,'US-ALS5-011','2026-01-01',None,{'n':'40-18-71(a).'}),
 ('income_tax','al.pit.bracket.single.1.ceiling',500,B,'2026-01-01',None,{'u':U,'n':'0/S/H/MS: 2% first 500, 4% next 2,500, 5% above 3,000.'}),
 ('income_tax','al.pit.bracket.single.2.ceiling',3000,B,'2026-01-01',None,{'u':U}),
 ('income_tax','al.pit.bracket.married.1.ceiling',1000,B,'2026-01-01',None,{'u':U,'n':'M: 2% first 1,000, 4% next 5,000, 5% above 6,000.'}),
 ('income_tax','al.pit.bracket.married.2.ceiling',6000,B,'2026-01-01',None,{'u':U}),
 ('income_tax','al.pit.bracket.1.rate',2,B,'2026-01-01',None,{'u':'percent'}),
 ('income_tax','al.pit.bracket.2.rate',4,B,'2026-01-01',None,{'u':'percent'}),
 ('income_tax','al.pit.bracket.3.rate',5,B,'2026-01-01',None,{'u':'percent'}),
 ('income_tax','al.wh.std_deduction.single.max',3000,B,'2026-01-01',None,{'u':U,'n':'0/S: 3,000 if GI <= 25,999; less 25 per 500 above; floor 2,500 from 35,500.'}),
 ('income_tax','al.wh.std_deduction.single.min',2500,B,'2026-01-01',None,{'u':U}),
 ('income_tax','al.wh.std_deduction.married.max',8500,B,'2026-01-01',None,{'u':U,'n':'M: 8,500; less 175 per 500 above 25,999; floor 5,000 from 35,500.'}),
 ('income_tax','al.wh.std_deduction.married.min',5000,B,'2026-01-01',None,{'u':U}),
 ('income_tax','al.wh.std_deduction.married_separate.max',4250,B,'2026-01-01',None,{'u':U,'n':'MS: 4,250; less 88 per 250 above 12,999; floor 2,500 from 17,750.'}),
 ('income_tax','al.wh.std_deduction.head_of_family.max',5200,B,'2026-01-01',None,{'u':U,'n':'H: 5,200; less 135 per 500; floor 2,500 from 35,500.'}),
 ('income_tax','al.wh.personal_exemption.single',1500,B,'2026-01-01',None,{'u':U,'n':'0 status: 0; S/MS 1,500; M/H 3,000.'}),
 ('income_tax','al.wh.personal_exemption.married',3000,B,'2026-01-01',None,{'u':U}),
 ('income_tax','al.wh.dependent.gi_to_50000',1000,B,'2026-01-01',None,{'u':U,'n':'Per dependent: 1,000 if GI <= 50,000; 500 if <= 100,000; 300 above.'}),
 ('income_tax','al.wh.dependent.gi_to_100000',500,B,'2026-01-01',None,{'u':U}),
 ('income_tax','al.wh.dependent.gi_above_100000',300,B,'2026-01-01',None,{'u':U}),
 ('income_tax','al.wh.supplemental.rate',5,B,'2026-01-01',None,{'u':'percent','n':'May be withheld at 5%.'}),
 ('income_tax','al.wh.certificate.form','A4 REV. 4/2025 (federal W-4 not accepted; no A4 = zero exemptions; A4-MS military spouse)','US-ALS5-005','2025-04-01',None,{'n':'ADOR page text still says "Revised March 2014" but the PDF prints REV. 4/2025 [US-ALS5-002] (never-do 6).'}),
 ('income_tax','al.wh.certificate.inflated_penalty',500,'US-ALS5-005','2025-04-01',None,{'u':U}),
 ('income_tax','al.wh.severance.exempt_max',50000,B,'2026-01-01',None,{'u':U,'n':'Severance/downsizing pay exempt up to 50,000 with prior ADOR approval.'}),
 ('income_tax','al.pit.overtime_premium_deduction.max',1000,'US-ALS5-004','2026-01-01','2028-12-31',{'u':U,'n':'Act 2026-604, operating level ASSESSMENT only: no change to wages, withholding or tax; W-2 box 12 code TT informational; total OT stays in box 16. Prior withholding-level exemption (Acts 2023-421/2024-437) shown as previous by ADOR.'}),
 ('non_resident','al.nonres.safe_harbor.days',30,'US-ALS5-003','2026-01-01',None,{'u':'days','n':'Act 2025-334, operating level WITHHOLDING: nonresidents with <=30 AL days working in more than one state whose home state has a similar exclusion or no PIT (list as of 2026-10-01: AK, FL, GA, IL, IN, LA, MT, NV, NH, SD, TN, TX, WA, WV, WY). At 31+ days all AL income of the year taxable. Athletes/entertainers/public figures excluded.'}),
 ('non_resident','al.reciprocity.exists',False,B,'2026-01-01',None,{'n':'Booklet lists no agreement. Residents withheld wherever they work except when the employer withholds for the work state; nonresidents only on AL-earned wages.'}),
 ('local_tax','al.local.occupational_tax.exists',True,B,'2026-01-01',None,{'n':'Municipal/county occupational taxes withheld by the employer, remitted to the city/county; ADOR does not administer them. No state census (AL-OQ-2).'}),
 ('local_tax','al.local.leeds.rate',1,'US-ALS5-017','2026-01-01',None,{'u':'percent','n':'City of Leeds: 1% of gross earnings, monthly return to Avenu, annual reconciliation, show on pay stub, records 5 years. Birmingham 1% is tier C (US-ALP7-001 MANUAL) - not a fact.'}),
 ('social_security','al.sui.wage_base',8000,'US-ALS5-009','2026-01-01',None,{'u':U,'n':'25-4-16(b)(1), fixed in statute; other-state UC wages count toward it.'}),
 ('social_security','al.sui.new_employer.rate',2.70,'US-ALS5-007','2026-01-01',None,{'u':'percent'}),
 ('social_security','al.sui.employer.rate.min',0.20,'US-ALS5-007','2026-01-01',None,{'u':'percent','n':'Range 0.20%-6.80% incl. 0.06% ESA across schedules A-D plus shared cost; 2026 schedule letter/shared cost not located (AL-OQ-1).'}),
 ('social_security','al.sui.employer.rate.max',6.80,'US-ALS5-007','2026-01-01',None,{'u':'percent'}),
 ('social_security','al.sui.esa.rate',0.06,'US-ALS5-007','2026-01-01',None,{'u':'percent','n':'Employment Security Enhancement Assessment inside the UC rate; no FUTA credit for it (handbook p. 19, US-ALR3-001).'}),
 ('social_security','al.sui.employee.rate',0,'US-ALR3-001','2026-01-01',None,{'u':'percent','n':'No UC tax withheld from employees.'}),
 ('social_security','al.sui.wages.cafeteria_cash_option_included',True,'US-ALS5-007','2026-01-01',None,{'n':'Cafeteria plan reductions with a cash option are UC wages (departs from income tax).'}),
 ('social_security','al.sdi_pfml.exists',False,'US-ALS5-007','2026-01-01',None,{}),
 ('payslip_statute','al.payslip.state_statute.exists',False,'US-ALS5-007','2026-01-01',None,{'c':'medium','n':'Agency: no state wage-hour laws [US-AL-P5-2-001, legacy id]; 29 CFR 516 applies. Leeds asks occupational tax to be shown on the pay stub [US-ALS5-017].'}),
 ('reporting_instruments','al.report.wh.monthly.a6.threshold',1000,B,'2026-01-01',None,{'u':U,'n':'A-6 monthly if more than 1,000 withheld in month 1 or 2 of the quarter; due 15th of next month; e-file/EFT mandatory for single payment >= 750.'}),
 ('reporting_instruments','al.report.wh.eft_mandatory_payment',750,B,'2026-01-01',None,{'u':U,'c':'medium'}),
 ('reporting_instruments','al.report.wh.quarterly.form','A-1 due last day of month after quarter; file when nil',B,'2026-01-01',None,{}),
 ('reporting_instruments','al.report.annual.a3','A-3 + W-2s due 31 January; EFW2 RS record only, 512 bytes; e-file mandatory for 10+ statements (Form 10, 8/24); RS cols 298-307 carry federal FIT withheld','US-ALS5-006','2026-01-01',None,{}),
 ('reporting_instruments','al.report.w2.efile_threshold',10,'US-ALS5-006','2026-01-01',None,{'u':'statements'}),
 ('reporting_instruments','al.report.w2.furnish_threshold',1500,B,'2026-01-01',None,{'u':U,'n':'W-2 to every employee paid 1,500+ AL wages or with AL tax withheld.'}),
 ('reporting_instruments','al.report.sui.quarterly','Quarterly Contribution and Wage Report via eGov only (online_form or file_upload); due last day of month after quarter; corrections UC-10C','US-ALS5-007','2026-01-01',None,{}),
 ('reporting_instruments','al.newhire.report_days',7,'US-ALS5-008','2026-01-01',None,{'u':'days','n':'From hire or recall; electronic twice a month 12-16 days apart; electronic mandatory for 5+ employees.'}),
 ('leave','al.leave.sick.state_statute.exists',False,'US-ALS5-010','2026-01-01',None,{'n':'Local sick-leave mandates barred (25-7-41).'}),
 ('leave','al.leave.jury.full_time_usual_compensation',True,'US-ALS5-012','2026-01-01',None,{'n':'12-16-8(c), 12-16-8.1: full-time employee entitled to usual compensation; cannot be forced to use leave.'}),
 ('leave','al.leave.voting.hours',1,'US-ALS5-012','2026-01-01',None,{'u':'hours','n':'17-1-5; silent on pay.'}),
 ('termination','al.ui.separation_info.return_working_days',6,'US-ALR3-001','2026-01-01',None,{'u':'working days','n':'BEN-241 on a claim. No state final-pay statute (federal + policy).'}),
 ('deductions_garnishments','al.garn.exempt.percent',75,'US-ALS5-013','2026-01-01',None,{'u':'percent','n':'6-10-7: 75% of resident wages exempt; apply with CCPA disposable-earnings limit, more protective governs. Garnishee pays in after 30 days, then monthly.'}),
 ('deductions_garnishments','al.garn.child_support.remit_business_days',7,'US-ALS5-013','2026-01-01',None,{'u':'business days','n':'30-3-61/-67/-70: IWO priority over garnishments; current before arrears.'}),
 ('deductions_garnishments','al.garn.termination_report_days',15,'US-ALS5-013','2026-01-01',None,{'u':'days'}),
 ('benefits_in_kind','al.hsa.conforms',True,'US-ALS5-020','2026-01-01',None,{}),
 ('live_change','al.live.act_2025_334.status','in force 2026-01-01; operating level withholding + filing','US-ALS5-003','2026-01-01',None,{}),
 ('live_change','al.live.act_2026_604.status','in force 2026-01-01 to 2028-12-31; operating level assessment (W-2 box 12 TT information)','US-ALS5-004','2026-01-01','2028-12-31',{}),
 ('live_change','al.live.hurricane_isaias_relief','individual returns to 2027-02-04; withholding relief case by case (notice 2026-10-15)','US-ALS5-019','2026-10-15',None,{}),
 ('oracle','al.oracle.example.1.input','M-2, weekly 850.00, federal withholding 35.19',B,'2026-01-01',None,{}),
 ('oracle','al.oracle.example.1.withholding',29.59,B,'2026-01-01',None,{'u':U,'vm':'derived arithmetically','n':'Booklet example re-derived in Python: 850x52=44,200; deductions 5,000+1,830 (35.19x52=1,829.88 rounded by booklet)+3,000+2,000=11,830; taxable 32,370; tax 20+200+26,370x5%=1,538.50/yr; /52 = 29.59 (30 if rounded to dollar).'}),
]
CITED = ['US-ALS5-002','US-ALS5-014','US-ALS5-016','US-ALS5-018','US-ALS5-021','US-ALR3-002','US-ALR3-003','US-AL-P5-1-001','US-AL-P5-2-001','US-ALL-001','US-ALL-002','US-ALP7-002','US-AL-P5-2-002','US-ALP9L-001']
NARR = {
 'labour_code': 'No state minimum wage, overtime, pay-frequency, payment-method or paycard statute; FLSA (7.25, 1.5x over 40) applies (FED unit) [US-AL-P5-2-001, US-ALL-001 — legacy ids, narrative only]. Confidence 85% (negative rests on the agency statement).',
 'social_security': 'UC wages include tips and bonuses; room and board at employee option valued (full board 63.00/week; meals 42.00/week or 2.00/meal; lodging 21.00/week or 3.00/day) per handbook rev. 2021 [US-ALR3-001] — admin rule not read, so not emitted as facts. Employer levies: only the 0.06% ESA [US-ALP7-002].',
 'reporting_instruments': 'ADOR registration and filings through My Alabama Taxes. Penalties: late return greater of 10% or 50; late payment 10%; 50 per late W-2/1099 [US-ALS5-001]. New-hire file specs from newhire@workforce.alabama.gov. Municipal occupational tax returns per city (Leeds/Avenu, Birmingham/HdL) [US-ALS5-017, US-ALS5-018].',
 'termination': 'No final-pay or vacation-payout statute (confidence 80%); no state WARN found.',
 'benefits_in_kind': 'AL wages follow federal unless AL law conflicts; excluded IRC 125, 219, 401(k), 403(b), 408(k), 408(p), 457 [US-ALS5-001]. Transit 132(f) and group-term life 79 not listed (AL-OQ-3). Agricultural cash wages not withheld.',
 'collective_agreements': 'No state prevailing-wage law; Davis-Bacon only (FED). 25-7-42 bars local labour-peace/PLA mandates.',
 'indexation': 'Nothing indexed: SUI base fixed in statute; withholding amounts statutory; no state minimum wage. Only the annual UC schedule A-D/shared cost (25-4-54), published per employer on UC-216.',
 'data_protection': 'Data Breach Notification Act 2018 ch. 8-38 [US-ALS5-016, partial: definitions only]; no SSN truncation statute located.',
}
SPECIAL = '''- Domestic/household: exempt from AL withholding; UC-covered at 1,000 cash wages in a quarter [US-ALS5-001, US-ALS5-007].
- Agricultural: exempt from withholding (AL does not follow the federal rule); UC at 10+ workers in 20 weeks or 20,000/quarter [US-ALS5-001, US-ALS5-007, US-ALS5-014].
- Minors: under 16 barred except agriculture; 14-15 outside school hours; no youth wage [US-ALS5-014].
- Tipped: federal tip credit; tips are UC wages [US-ALR3-001].
- Clergy: ministers exempt from AL withholding; church employment not UC-covered [US-ALS5-001, US-ALS5-007].
- Students / NRAs / statutory employees: no AL rule beyond federal [US-ALS5-001].
- Other-state workers: 30-day safe harbor; carrier carve-outs (P.L. 91-569, 101-322, 106-489); 3-mile coastal rule [US-ALS5-003, US-ALS5-001].
- Government/nonprofit: 501(c)(3) UC at 4+ workers in 20 weeks; pre-emption does not cover public employees [US-ALS5-007, US-ALS5-010].
- Military spouses: A4-MS (MSRRA) [US-ALS5-001, US-ALS5-002].
- Downsizing severance: up to 50,000 exempt with ADOR approval [US-ALS5-001].'''
LANG = 'English; a Spanish A4 exists (optional seam) [US-ALS5-005]; posters [US-ALP9L-001]. Payslip/filings en per US-OWN-006.'
UNRES = [
 {'key':'al.sui.rate_schedule.current','why':'The 2026 UC rate schedule letter (A-D) and shared-cost percentage are not on any public page; the FAQ points to the per-employer UC-216 notice in eGov.','attempted':['Workforce Alabama UC tax pages','FAQ'],'close':'Workforce Alabama 2026 tax-rate announcement (Experience Rating Section) or an employer 2026 UC-216 notice from the owner/client.'},
 {'key':'al.local.occupational_tax.census','why':'No state list of levying localities; only Leeds is A.2, Birmingham tier C; Auburn site timed out (HTTP 000).','attempted':['https://www.auburnalabama.org/finance/business-and-licensing-forms/occupational-license (timeout)','library.municode.com Birmingham (script-rendered)'],'close':'Alabama League of Municipalities occupational-tax list, then each city ordinance/tax page (Birmingham Title 3 Ch. 2, Auburn, Bessemer, Gadsden, Opelika, Fairfield, Macon County). Parallel fan-out per locality.','blocking':True},
 {'key':'al.pit.wages.transit_group_term_life','why':'IRC 132(f) transit and IRC 79 group-term life are not on the booklet exclusion list; AL treatment unconfirmed.','close':'ADOR Admin. Code 810-3-71 or an ADOR fringe-benefit FAQ.'},
 {'key':'al.garn.iwo.employer_fee','why':'The AL employer processing fee under a child-support IWO was not located in the sections read.','close':'Ala. Code 30-3-60..71 in full via ALISON GraphQL, or the DHR Child Support employer page.'},
 {'key':'al.nonres.safe_harbor.day_counting_guidance','why':'A 2026 ADOR rule/FAQ on day-counting under Act 2025-334 is suggested only by a tier-B lead (Bradley, 2026-09).','close':'ADOR Rules page / Alabama Administrative Monthly 2026 (810-3-71 amendments).'},
 {'key':'al.live.overtime_withholding_exemption.end_date','why':'End date 2025-06-30 of the Acts 2023-421/2024-437 withholding-level overtime exemption rests on tier-B leads only.','close':'ADOR page "Overtime Pay Exemption Amended Pursuant to Act 2024-437" linked from US-ALS5-004.'},
]
