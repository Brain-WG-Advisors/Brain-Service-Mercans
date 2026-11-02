NAME = 'Louisiana'
SUMMARY = 'No state minimum wage (FLSA 7.25); local wage/leave mandates prohibited (23:642). Flat 3.09% withholding (R-1306 1/26): (S - 12,875/N) x 0.0309 or (S - 25,750/N) x 0.0309; no supplemental rate; no local tax (constitutional bar), no reciprocity; Act 382 / LAC 61:I.1923 30-day nonresident mobile-workforce exemption (adopted LR 52:358, 2026-03-20). UI base 7,000, rates 0.09%-6.20%, no employee share. No pay-statement statute. Final pay earlier of next payday or 15 days. Child-support max 50%. Oracle: R-1306 examples 13.98 / 111.54.'
U = 'USD'
R = 'US-LAS5-001'
FACTS = [
 ('labour_code','la.minwage.state_law.exists',False,'US-LAS5-006','2026-01-01',None,{'n':'FLSA 7.25 for covered employers; no 2027 rate.'}),
 ('labour_code','la.local_mandates.preempted',True,'US-LAS5-005','2026-01-01',None,{'n':'R.S. 23:642: no local minimum wage or mandatory vacation/sick days.'}),
 ('labour_code','la.pay_frequency.rule','notice at hire of wage, method and frequency; undesignated paydays 1st and 16th; manufacturing/oil-boring/mining 10+ and public-service corporations at least twice monthly; FLSA-exempt outside; fine 25-250/day (23:633)','US-LAS5-004','2026-01-01',None,{}),
 ('income_tax','la.pit.rate.flat',3.09,R,'2026-01-01',None,{'u':'percent'}),
 ('income_tax','la.wh.method','no deduction: W = S x 0.0309; L-4 "1" (single/MFS): (S - 12,875/N) x 0.0309; L-4 "2" (MFJ/QSS/HoH): (S - 25,750/N) x 0.0309; N = 365/52/26/24/12/1; negative term = 0; round to cent',R,'2026-01-01','2026-12-31',{}),
 ('income_tax','la.wh.std_deduction.single',12875,R,'2026-01-01','2026-12-31',{'u':U,'n':'Indexed by prior-year CPI-U (R.S. 47:294(B)); set by emergency rule LAC 61:I.1501 effective 2026-01-01 (RIB 26-005, 2026-01-12) [US-LAS5-011]; official value may differ slightly once Jan-2026 CPI-U applied. 12,875/12,500 = 1.03 (2025 base tier-B only).'}),
 ('income_tax','la.wh.std_deduction.joint',25750,R,'2026-01-01','2026-12-31',{'u':U,'vm':'derived arithmetically','n':'= 2 x 12,875.'}),
 ('income_tax','la.wh.who','residents; nonresidents performing services in LA (subject to the 30-day rule); residents working outside LA if not withheld in the other state','US-LAS5-003','2026-01-01',None,{}),
 ('non_resident','la.nonres.mobile_workforce.days',30,'US-LAS5-002','2026-01-01',None,{'u':'days','n':'Act 382 (2025) R.S. 47:112.2(A), 47:248 [US-MULTIS5-021]; LAC 61:I.1923 adopted LR 52:358 (2026-03-20): <= 30 days exempt (C.1.a says "less than 30" - statute governs); employee notifies within 10 days from day 31; employer begins withholding and reports on L-1 from the period of the 31st day; exemption lost with other LA-source income; home-state condition repealed. Level withholding. Catch-up of days 1-30 open (LA-OQ-1). Build: per-employee LA workday counter (employer + related entities) and other-LA-income flag.'}),
 ('social_security','la.sui.wage_base',7000,'US-LAP9V-001','2026-01-01','2026-12-31',{'u':U,'c':'medium','n':'23:1536 mechanism not read (tier-B: 7,700 in 2025).'}),
 ('social_security','la.sui.employer.rate.max',6.20,'US-LAP9V-002','2026-01-01','2026-12-31',{'u':'percent','c':'medium'}),
 ('social_security','la.sui.new_employer.rate','average rate of its NAICS industrial classification; experience rating after 24 months','US-LAP9V-001','2026-01-01',None,{'n':'Social charges (non-charge, IWTP, Integrity) inside the total rate; IWTP and Integrity not FUTA-creditable [US-LAS5-007].'}),
 ('social_security','la.agency.name','Louisiana Works (replaces Louisiana Workforce Commission); keep laworks.net','US-LAS5-004','2026-01-01',None,{}),
 ('reporting_instruments','la.report.wh.l1','L-1 quarterly, electronic (LaTAP/software), zero returns required, due Apr 30 / Jul 31 / Oct 31 / Jan 31; payment quarterly < 500/month average, monthly 500 to < 5,000, semi-monthly >= 5,000','US-LAS5-003','2026-01-01',None,{'n':'[US-LAS5-008].'}),
 ('reporting_instruments','la.report.annual.l3','L-3 + W-2s due first business day after January 31 (30 days on closure); electronic mandatory at 50+ W-2s via LaWage; no magnetic media/CD; state boxes 16-18','US-LAS5-009','2026-01-01',None,{}),
 ('reporting_instruments','la.report.w2.efile_threshold',50,'US-LAS5-009','2026-01-01',None,{'u':'forms'}),
 ('reporting_instruments','la.report.sui.quarterly','due last day of month after quarter; domestic annual Jan 31; mandatory electronic (LAWATS); DE students earning credit not reported','US-LAS5-007','2025-04-01',None,{'c':'medium'}),
 ('reporting_instruments','la.newhire.report_days',20,'US-LAS5-010','2026-01-01',None,{'u':'days','n':'DCFS: name, address, SSN, occupation, first day; employer name, address, EIN; rehire incl. return from layoff/furlough/leave (no 60-day threshold in statute); penalty 25 / 500.'}),
 ('leave','la.leave.jury.paid_days',1,'US-LAS5-013','2026-01-01',None,{'u':'days','n':'R.S. 23:965: one paid day without loss of wages or leave; fines 100-500 / 100-1,000 + reinstatement.'}),
 ('termination','la.final_pay.rule','discharge or resignation: earlier of next regular payday (for the cycle worked) or 15 days; customary place/method or prepaid mail; CBA override; earned eligible vacation is due and cannot be forfeited; commissions/bonuses due if earned (23:631)','US-LAR3-002','2026-01-01',None,{}),
 ('termination','la.final_pay.max_days',15,'US-LAR3-002','2026-01-01',None,{'u':'days'}),
 ('termination','la.final_pay.penalty_wages.max_days',90,'US-LAR3-001','2026-01-01',None,{'u':'days','n':'23:632: lesser of 90 days wages or full wages from demand + fees; good-faith dispute: wages + interest.'}),
 ('termination','la.test_cost_recovery.working_days',90,'US-LAS5-004','2026-01-01',None,{'u':'working days','n':'23:634(B): only if pay >= federal MW + 1 and not part-time/seasonal.'}),
 ('deductions_garnishments','la.garn.creditor.exempt_percent',75,'US-LAS5-012','2026-01-01',None,{'u':'percent','n':'R.S. 13:3881(A)(1)(a): 75% of weekly disposable exempt, never less than 30 x federal MW (CCPA-equivalent); disposable also after retirement/medical/life-insurance deductions and amounts owed to employer.'}),
 ('deductions_garnishments','la.garn.child_support.max_percent',50,'US-LAS5-012','2026-01-01',None,{'u':'percent','n':'Exemption 50% child support, 60% spousal (stricter than CCPA); mixed/unclear DCFS order = child support.'}),
 ('deductions_garnishments','la.deductions.fines','prohibited except wilful/negligent damage or theft of employer funds, capped at actual damage (23:635)','US-LAS5-004','2026-01-01',None,{}),
 ('collective_agreements','la.cba.fringe_as_wages',True,'US-LAS5-015','2026-01-01',None,{'n':'R.S. 23:640: CBA fringe amounts treated as wages for penalty-wage rules. Prevailing wage repealed 1988 [US-LAP6-001].'}),
 ('live_change','la.live.lac_61_i_1923','adopted LR 52:358 (2026-03-20), supersedes the NOI (US-MULTIS5-022); level withholding','US-LAS5-002','2026-03-20',None,{}),
 ('live_change','la.live.sb133_2025','not codified (technical; adds "laborers")','US-LAS5-014','2025-01-01',None,{'c':'medium'}),
 ('oracle','la.oracle.r1306.example1.withholding',13.98,R,'2026-01-01','2026-12-31',{'u':U,'vm':'derived arithmetically','n':'(700 - 12,875/52) x 0.0309 = 13.9793 -> 13.98.'}),
 ('oracle','la.oracle.r1306.example2.withholding',111.54,R,'2026-01-01','2026-12-31',{'u':U,'vm':'derived arithmetically','n':'(4,600 - 25,750/26) x 0.0309 = 111.5371 -> 111.54.'}),
]
LEGACY = [
 ('social_security','la.sui.employer.rate.min',0.09,'US-LA-SUI-001','2026-01-01','2026-12-31','2026 LWC rate table: 0.09% at reserve ratio 9.5+ to 6.20%.'),
 ('income_tax','la.wh.supplemental.method','withheld like regular wages; no flat supplemental rate (vacation pay likewise)','US-LA-P5-1-002','2026-01-01',None,''),
 ('local_tax','la.local_income_tax.exists',False,'US-LA-P5-2-001','2026-01-01',None,'Constitution bars parish/municipal income tax.'),
]
CITED = ['US-LA-PIT-001','US-LA-P5-1-001','US-LA-SUI-001','US-LAP9V-001','US-LAR3-001','US-LAL-001','US-LAL-002','US-LAP6-001','US-LA-P5-2-005','US-LAP9M-001','US-MULTIS5-021','US-LAS5-016','US-LA-P5-2-002']
NARR = {
 'labour_code': 'Overtime: no state statute located (FLSA; medium). Direct deposit/paycard: no consent statute; 23:633 requires only notice of method (LA-OQ-3).',
 'income_tax': 'Certificate R-1300 (L-4); edition not re-fetched (404). 2027 standard deduction unpublished.',
 'social_security': 'No SDI/TDI/PFML [US-LA-P5-2-002 legacy, DOL WB list]. No employee contribution.',
 'payslip_statute': 'No itemised pay-statement statute in R.S. 23:631-638 (all read) [US-LAR3-002]; only hire notice of rate/method/frequency [US-LAS5-004]. Retention unread.',
 'benefits_in_kind': 'No LA source read (LDR cafeteria FAQ 404); LA starts from federal AGI (lead). Confidence 30%.',
 'indexation': 'Std deduction CPI-U (R.S. 47:294(B)); SUI base mechanism unread; no MW law.',
 'data_protection': 'Not researched (20%).',
}
SPECIAL = '''- Nonresidents (incl. NRAs working in LA): 30-day mobile-workforce exemption; withhold from period of day 31; lost with other LA-source income [US-MULTIS5-021, US-LAS5-002].
- Domestic: UI annual filers Jan 31; household withholding FAQ unread [US-LAS5-007].
- Students: UI DE students earning credit not reported [US-LAS5-007].
- Minors: Act 61 (2026) employment certificates; no payroll rule [US-LAS5-016].
- Tipped: federal tip credit only [US-LAS5-006].
- FLSA-exempt staff outside 23:633; part-time/seasonal excluded from test-cost recovery [US-LAS5-004].
- Agricultural, clergy, statutory, government: no state rule read (federal assumed, LA-OQ-12). Military spouses: L-4E exists (title only).'''
LANG = 'Posters in Spanish available [US-LAP9M-001]; no language clause in 23:631-638 [US-LAL-001, US-LAL-002]; payslip English (US-OWN-006).'
UNRES = [
 {'key':'la.nonres.mobile_workforce.catch_up','why':'From day 31, whether days 1-30 are withheld as a lump catch-up in the period of the 31st day: MULTI row (Act text) says yes; the regulation only says begin withholding in that period.','close':'Codified R.S. 47:112.2(A) text or an LDR RIB/FAQ on the mobile workforce exemption.','blocking':True},
 {'key':'la.report.w2.lawage_format','why':'LaWage bulk W-2 file format (EFW2 or LA layout) not read.','close':'LDR LaWage / W-2 electronic filing specification on dam.ldr.la.gov.'},
 {'key':'la.payment.direct_deposit_consent','why':'No consent statute located beyond 23:633 notice.','close':'Louisiana Works wage-payment FAQ.','blocking':False},
 {'key':'la.records.retention','why':'No LA payroll-record retention rule read.','close':'R.S. 23:1660 and any LDR withholding-record retention rule.','blocking':False},
 {'key':'la.report.sui.format','why':'UI form name and LAWATS upload format (ICESA?) and a 2026 FAQ copy not read.','close':'Louisiana Works LAWATS file specification.'},
 {'key':'la.leave.other','why':'Voting, military, school conference, bone marrow/organ donation leave not read.','close':'R.S. 23:961-1015 via Wayback.','blocking':False},
 {'key':'la.termination.ui_separation_notice','why':'LWC Form 1 separation duty not read.','close':'LAC 40:IV or a Louisiana Works employer page.'},
 {'key':'la.pit.conformity','why':'State treatment of 125, 401(k), HSA, transit, GTL not read (LDR FAQ 403/404).','close':'LDR cafeteria-plan FAQ and R.S. 47:293.','blocking':True},
 {'key':'la.garn.iwo_specifics','why':'IWO employer fee, priority, SDU remittance not read.','close':'R.S. 46:236.3 / 9:303 and the DCFS employer page.'},
 {'key':'la.sui.wage_base.mechanism','why':'R.S. 23:1536 wage-base mechanism and other-state wage credit not read.','close':'Wayback read of R.S. 23:1536.'},
 {'key':'la.data_protection.ssn','why':'SSN display statutes not researched.','close':'LA SSN display statutes and R.S. 51:3071 et seq. via Wayback.','blocking':False},
 {'key':'la.special_populations.other','why':'Household withholding, ag/clergy/statutory/government UI coverage (R.S. 23:1472) and L-4E reporting not read.','close':'LDR FAQ pages and R.S. 23:1472.'},
 {'key':'la.live.acts_2026_sweep','why':'Only page 1 (Acts 1-100) of the 2026 Acts list readable (ASP.NET postback).','close':'Remaining 2026 Acts pages via browser pass.','blocking':False},
]
