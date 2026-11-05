NAME = 'Kentucky'
SUMMARY = 'Minimum wage 7.25 following federal; tipped-employee definition changed 2026-04-10 (HB 185); OT over 40 plus a KY 7th-day rule; paid rest breaks. Flat 3.5% PIT (2027 3.5% on the statute); formula (annual wage - 3,360) x 3.5%; K-4 exemption-only; no supplemental rate; reciprocity IL/IN/MI/WV/WI/VA(commuters)/OH; local occupational license taxes (Louisville 1.45%/2.2%, Lexington 2.25%, others uncatalogued). UI employer-only, base 12,000 (cap reached), new 2.70%, Schedule A 0.30%-9.00%. Deductions statement for 10+ employers. Final pay later of next payday or 14 days. Oracle: 42A003 formula examples.'
U = 'USD'
FACTS = [
 ('labour_code','ky.minwage.hourly',7.25,'US-KYS5-001','2009-07-01',None,{'u':U,'n':'KRS 337.275(1); rises automatically with federal 29 USC 206(a)(1). Tipped: federal cash wage with records.'}),
 ('labour_code','ky.tipped.definition','more than 30/month in tips AND work directly supporting the tipped service function (2026 Ky. Acts ch. 72)','US-KYS5-021','2026-04-10',None,{}),
 ('labour_code','ky.tip_pool.rule','employer may not keep tips except required withholding; pools may include tipped employees, not salaried staff/managers/supervisors (KRS 337.065)','US-KYS5-008','2026-04-10',None,{}),
 ('labour_code','ky.overtime.weekly_threshold_hours',40,'US-KYS5-002','2026-01-01',None,{'u':'hours','n':'KRS 337.285(1); exemptions incl. retail selling, restaurant/hotel/motel, companionship; public comp time.'}),
 ('labour_code','ky.overtime.seventh_day_rule','1.5x for time worked on the 7th day of a workweek unless not allowed to work over 40 h that week; OT already paid for same hours credited (KRS 337.050)','US-KYS5-003','2026-01-01',None,{}),
 ('labour_code','ky.rest_break.paid_minutes_per_4h',10,'US-KYS5-015','2026-01-01',None,{'u':'minutes','n':'KRS 337.365; lunch between 3rd and 5th hour (337.355).'}),
 ('labour_code','ky.pay_frequency.rule','at least semimonthly; pay covers wages to a day not more than 18 days before payday; absent employee within 6 days of demand; EAP excluded','US-KYS5-004','2026-01-01',None,{'c':'medium'}),
 ('labour_code','ky.payment.method','legal tender, check, direct deposit or payroll card (no activation fee, one free withdrawal per period up to full balance) (KRS 337.010(1)(c)1)','US-KYS5-006','2026-01-01',None,{'c':'medium'}),
 ('income_tax','ky.pit.rate.flat',3.5,'US-KYS5-009','2026-01-01',None,{'u':'percent','n':'KRS 141.020(2)(f); 2027 stays 3.5% on the statute unless Budget Director report + General Assembly act (HB 152 stalled, tier-B).'}),
 ('income_tax','ky.wh.method','(period wage x periods - 3,360) x 3.5% / periods (2026 formula sheet 42A003 TCF)','US-KY-002','2026-01-01','2026-12-31',{'vm':'derived arithmetically','n':'Bi-weekly example prints 35,730 where 35,640 is correct (35,640 x 3.5% = 1,247.40 as printed): typo. Per-period rounding unstated (sheet shows 47 for 47.98).'}),
 ('income_tax','ky.wh.std_deduction',3360,'US-KY-002','2026-01-01','2026-12-31',{'u':U,'n':'Indexed annually (KRS 141.081(2)(a)). Extra 117.60 for multiple W-2 = 3,360 x 3.5%.'}),
 ('income_tax','ky.wh.rounding','employer may compute WAGES to nearest dollar (KRS 141.310(4)); no rounding rule for the tax','US-KYS5-010','2026-01-01',None,{}),
 ('income_tax','ky.wh.supplemental.method','no separate rate; bonuses and severance through the same formula; film-incentive companies at max 141.020 rate','US-KY-001','2026-01-01',None,{'c':'medium'}),
 ('income_tax','ky.wh.certificate','K-4 (42A804): no allowances; exemption claims only (no liability; Fort Campbell nonresident; SCRA/MSRRA; reciprocal-state residents)','US-KYS5-013','2026-01-01',None,{}),
 ('non_resident','ky.reciprocity.states','IL, IN, MI, WV, WI; VA daily commuters only; OH unless 20%+ S-corp shareholder','US-KY-001','2026-01-01',None,{'n':'Certificate 42A809 [US-MULTI-009]. Nonresidents taxed on KY labour only; out-of-state employers withhold on KY-earned wages (103 KAR 18:010(2)) [US-KYS5-023]. Other-state credit at assessment (KRS 141.070).'}),
 ('local_tax','ky.local.louisville.rate.all_wages',1.45,'US-KYP9W-001','2026-01-01',None,{'u':'percent','n':'Metro 1.25% + TARC 0.20% on all wages earned in Louisville Metro; residents + 0.75% school boards = 2.2%; W-1 quarterly, W-1D monthly if > 3,000/quarter, W-3 by Feb 28 [US-KYP9W-002].'}),
 ('local_tax','ky.local.louisville.rate.resident_total',2.2,'US-KYP9W-001','2026-01-01',None,{'u':'percent'}),
 ('local_tax','ky.local.lexington.rate',2.25,'US-KYS5-024','2026-01-01',None,{'u':'percent','n':'LFUCG: withheld by employer; 220-221 quarterly (preprinted, mailed Jan), monthly if quarterly > 300; 222 annual reconciliation; base (125/deferred comp) unread.'}),
 ('local_tax','ky.local.basis','work-location occupational license taxes on separate returns per locality; DOR does not administer','US-KYS5-024','2026-01-01',None,{'c':'medium'}),
 ('social_security','ky.sui.wage_base',12000,'US-KY-003','2026-01-01',None,{'u':U,'vm':'derived arithmetically','n':'KRS 341.030(7): 9,000 from 2012 + 300 each Jan 1 to 12,000 cap (suspended if fund < 200M on Sept 30): 11,400 + 300 + 300 = 12,000; 2027 = 12,000 unless amended [US-KYS5-012].'}),
 ('social_security','ky.sui.new_employer.rate',2.70,'US-KY-003','2026-01-01','2026-12-31',{'u':'percent','c':'medium','n':'12,000 x 2.7% = 324 max per employee [US-KYS5-019].'}),
 ('social_security','ky.sui.employer.rate.min',0.30,'US-KY-003','2026-01-01','2026-12-31',{'u':'percent','c':'medium','n':'Schedule A 0.30%-9.00%.'}),
 ('social_security','ky.sui.employer.rate.max',9.00,'US-KY-003','2026-01-01','2026-12-31',{'u':'percent','c':'medium'}),
 ('social_security','ky.sui.scuf.rate',0.0115,'US-KYP7-001','2027-01-01',None,{'u':'percent','n':'Inside the rate (diverted), no extra cost; 0% in 2026 (SB 129).'}),
 ('social_security','ky.sui.wage_base.other_state_credit',True,'US-KYS5-018','2026-01-01',None,{'n':'KRS 341.030(7)(a).'}),
 ('social_security','ky.sui.coverage','non-ag 1,500/quarter or 1 in 20 weeks; ag 20,000/quarter or 10 in 20 weeks; domestic 1,000/quarter; 501(c)(3) 4 in 20 weeks; officers covered; proprietor spouse/parent/child < 21 not','US-KYS5-019','2026-01-01',None,{}),
 ('payslip_statute','ky.payslip.deduction_statement.employer_threshold',10,'US-KYP8-001','2026-01-01',None,{'u':'employees','n':'Employers with 10+ employees making deductions: paper or electronic statement of each deduction and purpose at payment (electronic requires computer/printer access); no other content mandated.'}),
 ('data_protection','ky.records.retention_years',1,'US-KYP8-002','2026-01-01',None,{'u':'years','n':'KRS 337.320: pay and hours records at least 1 year.'}),
 ('reporting_instruments','ky.report.wh.frequency','annual < 400 (K-3 Jan 31); quarterly 400-1,999 (K-1 last day of month after quarter); monthly 2,000-49,999 (K-1 15th); twice-monthly >= 50,000 (25th / 10th); >= 100,000 in a period by EFT next banking day; zero returns required; MyTaxes electronic','US-KYS5-013','2026-01-01',None,{}),
 ('reporting_instruments','ky.report.w2','due Jan 31 via MyTaxes or CD; SSA EFW2 with DOR RS record or K-5; electronic mandatory at 26+ statements (103 KAR 18:050(4)); paper W-2 not processed','US-KYS5-013','2026-01-01',None,{}),
 ('reporting_instruments','ky.report.w2.efile_threshold',26,'US-KYS5-013','2026-01-01',None,{'u':'statements'}),
 ('reporting_instruments','ky.report.sui.quarterly','KUIP (replaced KEWES 2026), due last day of month after quarter, zero reports required; late 25/75 first, 125/175 later; interest 1.5%/month','US-KYS5-019','2026-01-01',None,{}),
 ('reporting_instruments','ky.newhire.report_days',20,'US-KYS5-020','2025-07-01',None,{'u':'days','n':'Recipient Office of the Attorney General since 2025-07-01; residents or workers in KY; includes state EIN.'}),
 ('leave','ky.leave.adoption.weeks',6,'US-KYS5-016','2026-01-01',None,{'u':'weeks','n':'KRS 337.015: child under 10; match benefits given to birth parents.'}),
 ('leave','ky.leave.voting.hours',4,'US-KYS5-025','2026-01-01',None,{'u':'hours','n':'KRS 118.035; no pay rule.'}),
 ('termination','ky.final_pay.rule','later of next normal payday or 14 days after separation, discharge or resignation (KRS 337.055); vested vacation and earned bonuses are wages','US-KYS5-005','2026-01-01',None,{'n':'[US-KYS5-006] vacation; public comp time paid at higher of 3-year average or final rate.'}),
 ('termination','ky.final_pay.max_days',14,'US-KYS5-005','2026-01-01',None,{'u':'days'}),
 ('benefits_in_kind','ky.pit.conformity_date','2025-12-31 (KRS 141.010(21), effective 2026-07-15, TY2026)','US-KYS5-022','2026-07-15',None,{}),
 ('benefits_in_kind','ky.wh.chart_42a003','not required: 125/flex, DCAP, health, GTL*, 401(k)*, SEP*, TSP*, IRA, fringe*, meals/lodging*, travel*; required: company cars, moving, severance, bonuses, vacation/sick pay*, tips > 20/month','US-KYS5-023','2026-01-01',None,{}),
 ('deductions_garnishments','ky.deductions.rule','only if required by law or expressly authorised in writing (insurance, medical dues); union dues written consent; fines, shared-till shortages etc. prohibited','US-KYS5-007','2026-01-01',None,{}),
 ('deductions_garnishments','ky.garn.creditor.rule','lesser of 25% of disposable or excess over 30 x federal MW (217.50/week) (KRS 427.010); support/Ch. 13/tax outside','US-KYS5-014','2026-01-01',None,{}),
 ('oracle','ky.oracle.formula.monthly_3270',104.65,'US-KY-002','2026-01-01','2026-12-31',{'u':U,'vm':'derived arithmetically','n':'Monthly 3,270: (39,240 - 3,360) x 3.5% = 1,255.80 / 12 = 104.65.'}),
 ('oracle','ky.oracle.formula.biweekly_1500.annual',1247.40,'US-KY-002','2026-01-01','2026-12-31',{'u':U,'vm':'derived arithmetically','c':'medium','n':'Bi-weekly 1,500: (39,000 - 3,360) = 35,640 x 3.5% = 1,247.40 (sheet prints 35,730 - typo); /26 = 47.98, sheet shows 47 (rounding unexplained, Q2).'}),
]
LEGACY = [('collective_agreements','ky.prevailing_wage.state_law.exists',False,'US-KY-P5-2-004','2017-01-01',None,'Repealed 2017 (KRS 337.505-.550); Davis-Bacon only.')]
CITED = ['US-KYS5-011','US-KYS5-012','US-KYS5-014','US-KYS5-017','US-KYS5-026','US-KYP9W-002','US-KYP9V-001','US-KYR3-001','US-KYR3-002','US-KYR3-003','US-KY-P5-1-001','US-KY-P5-1-002','US-KY-P5-2-001','US-KY-P5-2-002','US-MULTI-009','US-KYP9L-001']
NARR = {
 'social_security': 'No SDI/TDI/PFML; KRS 304.53 only voluntary group PFL insurance [US-KYR3-001..003]. Workers compensation premiums may not be deducted.',
 'leave': 'No paid sick leave statute; local PSL pre-emption not read. Court appearance protected (337.415) [US-KYS5-017]; jury/military not read.',
 'deductions_garnishments': 'Child-support IWO fee 1 per payment and lump-sum reporting 150+ for 20+ employers rest only on tier-B MANUAL US-KYS5-026: not facts (Q11). AG Office of Child Support Services administers.',
 'indexation': 'Std deduction indexed yearly (141.081(2)(a)); PIT rate trigger review; SUI base +300 to 12,000 cap (reached); schedule by fund balance Sept 30; MW follows federal; garnishment floor 30 x federal MW.',
 'data_protection': 'No SSN truncation rule read; KRS 141.335 lists SSN on the annual statement; W-2 by Jan 31 or last wage payment day [US-KYS5-011].',
}
SPECIAL = '''- Domestic: excluded from state MW/OT unless more than one domestic regularly employed; withholding not required; UI 1,000/quarter [US-KYS5-006, US-KYS5-023, US-KYS5-019].
- Agricultural: excluded from state MW/OT; withholding per IRC 3121(a) test; UI 20,000/quarter or 10 in 20 weeks [US-KYS5-006, US-KYS5-023, US-KYS5-019].
- Minors: no subminimum; KRS 339 not read.
- Tipped: federal cash wage; new definition 2026-04-10; tip pools; tips > 20/month withheld [US-KYS5-001, US-KYS5-021, US-KYS5-008, US-KYS5-023].
- Clergy: withholding not required; religious camps <= 210 days excluded from MW chapter [US-KYS5-023, US-KYS5-006].
- Students/learners/apprentices: subminimum only with commissioner certificate [US-KYS5-006].
- NRAs: withholding required [US-KYS5-023]. Statutory employees: direct sellers excluded from MW; withholding per IRC 3401 [US-KYS5-006, US-KYS5-013].
- Government: federal and certain state employees excluded from MW chapter; county/city comp-time regime [US-KYS5-006, US-KYS5-002].
- Small retail/service (< 95,000 gross) and family: excluded from MW chapter [US-KYS5-006].
- Military / Fort Campbell nonresidents and SCRA/MSRRA spouses exempt [US-KYS5-013].'''
LANG = 'No language clause in KRS 337.070/.320/.325 [US-KYP8-001..003 per MANDATE]; payslip English (US-OWN-006).'
UNRES = [
 {'key':'ky.pit.rate.next_year','why':'TY2027 rate is 3.5% on the statute; the Budget Director report of 2026-09-05 was not read.','close':'OSBD 2026-09-05 report to the IJC on A&R plus the DOR 2027 formula sheet 42A003 (TCF)(10-2026).','blocking':False},
 {'key':'ky.wh.rounding.tax','why':'Formula sheet shows 47 for 47.98 bi-weekly; KRS 141.310(4) rounds only wages.','close':'DOR written answer or a corrected 2026/2027 formula sheet.'},
 {'key':'ky.local.occupational_tax.census','why':'Only Louisville and Lexington verified; other cities, counties and school districts uncatalogued.','close':'Kentucky Occupational License Association / DLG local rate list, then each locality; parallel fan-out.','blocking':True},
 {'key':'ky.local.lexington.base','why':'LFUCG withholding base (125/deferred comp) and Fayette County Board of Education tax not read; tier-B says included.','close':'LFUCG License Fee Regulations 5th ed. and Code ch. 13.'},
 {'key':'ky.report.rs_and_kuip_specs','why':'KY EFW2 RS-record spec and KUIP wage-file layout not read.','close':'DOR Software-Developer page (revenue.ky.gov/Software-Developer/) and KUIP TPA file specs on ui.ky.gov.'},
 {'key':'ky.local_mandates.preemption','why':'2016 KY Supreme Court Louisville MW decision known only from tier B; PSL pre-emption unread.','close':'Kentucky Restaurant Ass\'n v. Louisville/Jefferson County Metro Gov\'t (2016) on kycourts.gov and any KRS 65 pre-emption section.','blocking':False},
 {'key':'ky.leave.jury_military_minors','why':'KRS 29A.160, 38.238/38.460 and KRS 339 / 803 KAR 1:100 not read.','close':'LRC statute texts.','blocking':False},
 {'key':'ky.termination.ui_separation_notice','why':'Only claim-driven UI-412A/UI-412 found.','close':'787 KAR 1 index (OUI regulations).','blocking':False},
 {'key':'ky.garn.state_tax_levy','why':'DOR wage levy / priority not researched.','close':'KRS 131.500-.510 text.','blocking':False},
 {'key':'ky.data_protection.ssn_paystub','why':'SSN truncation statutes not read.','close':'KRS 365.725-.734 / KRS 367 texts.','blocking':False},
 {'key':'ky.garn.child_support.employer_fee','why':'1 USD fee and 150 USD lump-sum reporting rest on tier-B MANUAL US-KYS5-026.','close':'KRS 405.465 / 40 KAR 1:410 text read with US VPN.'},
]
