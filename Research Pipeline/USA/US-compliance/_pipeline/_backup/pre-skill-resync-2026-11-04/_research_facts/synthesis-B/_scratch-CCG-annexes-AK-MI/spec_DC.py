NAME = 'District of Columbia'
SUMMARY = 'Minimum wage 17.95 -> 18.40 (2026-07-01, CPI Washington MSA); tipped wage 10.30 = 56% of the minimum, rising to 75% by 2034; non-hotel tipped employers must use a third-party payroll business. Income tax withheld by a percentage method/tables with no standard deduction in withholding; the 2026 method after D.C. Act 26-416 (personal exemptions repealed) is UNPUBLISHED and the D-4/D-4A are "under review" (blocking open question). Nonresidents not taxed (Home Rule Act, D-4A). SUI base 9,000, new 2.7%, +0.2% admin assessment; PFL 0.75% employer-only, no cap. Itemised pay statement with tip lines and, from 2026, compensation sources. Overall confidence 85%.'
U = 'USD'
FACTS = [
 ('labour_code','dc.minwage.hourly',17.95,'US-DCS5-011','2025-07-01','2026-06-30',{'u':U}),
 ('labour_code','dc.minwage.hourly',18.40,'US-DCS5-011','2026-07-01',None,{'u':U,'n':'G-DERIVE: 17.95 x 1.024 (CPI-U Washington MSA) = 18.3808 -> 18.40 (nearest 0.05) [US-DCS5-001, 32-1003(a)(6)]. 2027 due by ~June 2027.'}),
 ('labour_code','dc.minwage.tipped.cash_wage',10.00,'US-DCS5-011','2024-07-01','2026-06-30',{'u':U}),
 ('labour_code','dc.minwage.tipped.cash_wage',10.30,'US-DCS5-011','2026-07-01',None,{'u':U,'n':'= 56% x 18.40 = 10.304 -> 10.30; employer tops up weekly shortfall.'}),
 ('labour_code','dc.minwage.tipped.percent_of_minimum',56,'US-DCS5-001','2026-07-01','2028-06-30',{'u':'percent','n':'D.C. Law 26-55 s.2222(a): 56% from 2026-07-01, 60% 2028, 65% 2030, 70% 2032, 75% 2034.'}),
 ('labour_code','dc.minwage.tipped.percent_of_minimum',60,'US-DCS5-001','2028-07-01','2030-06-30',{'u':'percent'}),
 ('labour_code','dc.minwage.tipped.percent_of_minimum',65,'US-DCS5-001','2030-07-01','2032-06-30',{'u':'percent'}),
 ('labour_code','dc.minwage.tipped.percent_of_minimum',70,'US-DCS5-001','2032-07-01','2034-06-30',{'u':'percent'}),
 ('labour_code','dc.minwage.tipped.percent_of_minimum',75,'US-DCS5-001','2034-07-01',None,{'u':'percent'}),
 ('labour_code','dc.tipped.third_party_payroll.required',True,'US-DCS5-010','2025-12-06',None,{'n':'32-1008(a-1): employers paying the tipped wage, other than hotels.'}),
 ('labour_code','dc.minwage.coverage','> 50% of working time in DC, or DC-based with substantial DC time and <= 50% in any one state; any employee with >= 2 h in DC in a workweek gets DC MW for DC hours (32-1003(b),(b-1))','US-DCS5-001','2026-01-01',None,{}),
 ('labour_code','dc.overtime.weekly_threshold_hours',40,'US-DCS5-001','2026-01-01',None,{'u':'hours','n':'1.5x over 40; no daily OT; retail/service commission exemption.'}),
 ('labour_code','dc.pay_frequency.rule','at least twice per calendar month on paydays designated in advance; EAP or contract/custom monthly; at most 10 working days from period end to payday','US-DCS5-002','2026-01-01',None,{}),
 ('labour_code','dc.payment.method','lawful US money or checks payable on demand (32-1302); no DC direct-deposit/paycard statute found','US-DCS5-002','2026-01-01',None,{'c':'medium'}),
 ('income_tax','dc.wh.statutory_method','percentage method or tables similar to IRC 3402; no standard-deduction allowance in withholding; wages may be computed to nearest dollar (47-1812.08(b))','US-DCS5-025','2026-01-01',None,{}),
 ('income_tax','dc.wh.lump_sum_retirement.rate',10.75,'US-DCS5-025','2026-01-01',None,{'u':'percent','n':'Resident lump-sum retirement distributions at highest rate (47-1812.08(m), amended by D.C. Law 26-89 / Act 26-214).'}),
 ('income_tax','dc.wh.certificate.status','D-4 and D-4A marked "currently under review" on the OTR forms page, no fill-in link','US-DCS5-013','2026-11-02',None,{}),
 ('income_tax','dc.pit.personal_exemption.repealed',True,'US-DCS5-021','2025-01-01',None,{'n':'D.C. Act 26-416 (emergency, in force 2026-08-13 for <= 90 days, ~to 2026-11-11); tax subtitle as of 2025-01-01; DC standard deduction 15,000 / 22,500 / 30,000 for 2025, COLA from 2026 rounded down to 50. Operating level ASSESSMENT; no change to 47-1812.08.'}),
 ('income_tax','dc.pit.obbba_deductions','disallowed TY2025; allowed as DC deductions from TY2026; operating level assessment only (no withholding change)','US-DCS5-021','2026-01-01',None,{}),
 ('social_security','dc.sui.wage_base',9000,'US-DCS5-017','2026-01-01',None,{'u':U,'n':'51-103(e)(6); fixed. No explicit other-state credit found (open).'}),
 ('social_security','dc.sui.new_employer.rate',2.7,'US-DCS5-016','2026-01-01',None,{'u':'percent'}),
 ('social_security','dc.sui.employer.rate.min',1.9,'US-DCS5-017','2026-01-01',None,{'u':'percent','n':'Tax Table VI 1.9%-7.4% (51-103(c)(8)(A)).'}),
 ('social_security','dc.sui.employer.rate.max',7.4,'US-DCS5-017','2026-01-01',None,{'u':'percent'}),
 ('social_security','dc.sui.admin_assessment.rate',0.2,'US-DCS5-017','2026-01-01',None,{'u':'percent','n':'(m)(1) administrative funding assessment on taxable wages [US-DCP7-001]. 0.1% interest surcharge (l)(1) billing in 2026 unconfirmed [US-DCP7-003].'}),
 ('social_security','dc.sui.employee.rate',0,'US-DCS5-017','2026-01-01',None,{'u':'percent','n':'Contributions may not be deducted from wages (d).'}),
 ('social_security','dc.pfl.employer.rate',0.75,'US-DCS5-019','2024-07-01',None,{'u':'percent','n':'100% employer-funded, not deductible from pay, no wage cap (US-DCS5-020). History: 0.62% to 2022-Q2, 0.26% to 2024-Q2.'}),
 ('social_security','dc.pfl.wage_cap.exists',False,'US-DCS5-020','2026-01-01',None,{}),
 ('social_security','dc.pfl.coverage','> 50% of work time in DC, or DC-based with substantial DC time and <= 50% elsewhere (32-541.01(3)); not by residence','US-DCS5-007','2026-01-01',None,{}),
 ('social_security','dc.pfl.benefit.weekly_max',1100,'US-DCS5-021','2026-10-01',None,{'u':U,'n':'D.C. Act 26-416 (emergency); CPI-indexed thereafter; durations parental 12 / family 6 / medical 10 / pre-natal 2 weeks for claims 2026-10-01..2030-09-30. Benefit side, not payroll.'}),
 ('payslip_statute','dc.payslip.items','date of payment; gross wages; deductions and additions with separate gratuities line; net wages; hours worked; tip-declaration form split cash/card; from 2026-01-01 list of compensation sources beyond base wages and tips','US-DCS5-010','2026-01-01',None,{'n':'32-1008(b), (b)(6A).'}),
 ('payslip_statute','dc.hire_notice.language','English and also the employee primary language where a Mayor template exists (32-1008(c))','US-DCS5-010','2026-01-01',None,{}),
 ('data_protection','dc.records.retention_years',3,'US-DCS5-010','2026-01-01',None,{'u':'years','n':'Or federal standard if longer; DOB for employees under 19.'}),
 ('reporting_instruments','dc.report.wh.fr900q','FR-900Q electronic on MyTax.DC.gov (mandatory since TY2023); deposits weekly/semi-weekly/monthly/quarterly as assigned by 20th of following month; returns due Apr 30, Jul 31, Oct 31, Jan 31; zero return required; payments over 5,000 electronic (ACH code 00300); FR-900A annual if under 200/yr','US-DCS5-014','2026-01-01',None,{}),
 ('reporting_instruments','dc.report.w2','EFW2/EFW2C with required RS record via MyTax.DC.gov; mandatory electronic at 25+ forms (else paper with WT or manual entry); due January 31','US-DCS5-015','2025-01-01',None,{'c':'medium','n':'TY2025 edition read; TY2026 not yet published.'}),
 ('reporting_instruments','dc.report.w2.efile_threshold',25,'US-DCS5-015','2025-01-01',None,{'u':'forms'}),
 ('reporting_instruments','dc.report.sui.quarterly','UC-30 via DOES ESSP, due last day of month after quarter; household annual April 15; 250+ employees machine-readable; penalty 10% (min 100), interest 1.5%/month','US-DCS5-018','2026-01-01',None,{}),
 ('reporting_instruments','dc.report.pfl.quarterly','same ESSP channel and due dates (Apr 30, Jul 31, Oct 31, Jan 31)','US-DCS5-019','2026-01-01',None,{}),
 ('reporting_instruments','dc.newhire.report_days',20,'US-DCS5-022','2026-01-01',None,{'u':'days','n':'dc-newhire.com online/mail/fax; employee name/address/SSN, employer name/address/FEIN, hire date; penalty 25/employee.'}),
 ('leave','dc.leave.sick.accrual.100_plus','1 h per 37 h worked, up to 7 days/yr','US-DCS5-004','2026-01-01',None,{'n':'25-99: 1/43 up to 5 days; <=24: 1/87 up to 3 days; tipped restaurant/bar 1/43 up to 5 days at full MW; use after 90 days; reinstated on rehire within 1 year.'}),
 ('leave','dc.leave.sick.accrual.25_99','1 h per 43 h worked, up to 5 days/yr','US-DCS5-004','2026-01-01',None,{}),
 ('leave','dc.leave.sick.accrual.under_25','1 h per 87 h worked, up to 3 days/yr','US-DCS5-004','2026-01-01',None,{}),
 ('leave','dc.leave.sick.payout_on_separation',False,'US-DCS5-024','2026-01-01',None,{'c':'medium'}),
 ('termination','dc.final_pay.rule','discharge: working day after (4 days if employee handled employer money); resignation: next regular payday or 7 days, whichever first; liquidated damages lesser of 10%/working day or treble; CBA may override','US-DCS5-003','2026-01-01',None,{}),
 ('deductions_garnishments','dc.garn.creditor.rule','max 25% of weekly disposable wages exceeding 40 x DC minimum wage; one attachment at a time (16-572)','US-DCS5-006','2026-01-01',None,{}),
 ('deductions_garnishments','dc.garn.creditor.weekly_threshold',736,'US-DCS5-006','2026-07-01',None,{'u':U,'vm':'derived arithmetically','n':'40 x 18.40.'}),
 ('collective_agreements','dc.living_wage.hourly',17.95,'US-DCS5-012','2026-01-01','2026-06-30',{'u':U,'n':'DC contractors/assistance >= 100,000 (subs 15,000/50,000) [US-DCS5-009]; CPI-U capped 3% each 1 Jan; floor = minimum wage.'}),
 ('collective_agreements','dc.living_wage.hourly',18.40,'US-DCS5-012','2026-07-01',None,{'u':U}),
 ('collective_agreements','dc.living_wage.contract_threshold',100000,'US-DCS5-009','2026-01-01',None,{'u':U}),
]
LEGACY = [
 ('income_tax','dc.pit.rate_schedule','<=10,000 4%; 10,000-40,000 400+6%; 40,000-60,000 2,200+6.5%; 60,000-250,000 3,500+8.5%; 250,000-500,000 19,650+9.25%; 500,000-1,000,000 42,775+9.75%; >1,000,000 91,525+10.75%','US-DCP52-001','2022-01-01',None,'Base amounts re-derived in Python (match). Not indexed.'),
 ('income_tax','dc.wh.notice_2022_08','apply current rate schedule with the federal allowance amount (no FR-230 after 2018); applying to 2026 is an inference','US-DCP51-002','2022-01-01',None,''),
 ('non_resident','dc.nonres.taxable',False,'US-DCP51-006','2026-01-01',None,'Home Rule Act bars taxing nonresidents; D-4A stops DC withholding; resident credit for other-state tax at assessment.'),
]
CITED = ['US-DCS5-005','US-DCS5-008','US-DCS5-023','US-DCP7-001','US-DCP7-003','US-DCR3-001','US-DCR3-002','US-DCP51-001','US-DCP51-004','US-DCP51-007','US-DCP51-014','US-DCP52-003','US-DCP52-004','US-DCP52-005','US-MULTI-016']
NARR = {
 'income_tax': 'TRAP (brief): DC 2026 withholding method is unpublished. 47-1812.08 is unchanged, but D.C. Act 26-416 repealed personal exemptions (the old D-4 allowance basis) and the D-4/D-4A are under review. Until OTR publishes, the only published instruction is Notice 2022-08 (rate schedule with federal allowance amount) - an inference for 2026; the engine must flag this. No flat supplemental rate: bonuses withheld as regular wages [US-DCR3-001, US-DCR3-002].',
 'non_resident': 'DC exempts all nonresidents (Home Rule Act); MD and VA appear in the MULTI matrix because they exempt DC residents [US-MULTI-016].',
 'local_tax': 'None: DC is itself the local layer.',
 'payslip_statute': 'Electronic delivery: no DC rule found. Reach follows 32-1003(b)/(b-1) coverage (inference).',
 'termination': 'Accrued vacation payout: no statutory rule (policy). UI separation notice: no DC form found.',
 'benefits_in_kind': 'DC income tax starts from federal gross income: federal exclusions (401(k), 125, HSA, transit, GTL) flow through (70%; 47-1803.02 not read). UI wages include non-cash and customary tips, exclude employer retirement/sickness/medical/death plans [US-DCS5-008].',
 'deductions_garnishments': 'Child support: OAG CSSD sends IWO within 2 business days of the new-hire entry [US-DCS5-022]; DC fees/priority not read. No DC wage-deduction authorisation rule read.',
 'collective_agreements': 'Sector prevailing wage for underground electrical and gas utility work at Davis-Bacon rates [US-DCP52-005 legacy].',
 'indexation': 'MW July 1 CPI-U Washington MSA (0.05); tipped % of MW; living wage Jan 1 CPI-U capped 3%; SUI base fixed; PFL rate statutory; PFL max benefit CPI from 2026-10-01; DC standard deduction COLA (assessment); brackets not indexed.',
 'data_protection': 'New-hire reports carry the SSN; no truncation rule found; D.C. Code 28-3851 not read (40%).',
 'live_change': 'D.C. Act 26-416 (emergency, 2026-08-13 to ~2026-11-11; status of the permanent FY2027 BSA unconfirmed); D.C. Law 26-55 (in force 2025-12-06: tipped %, compensation-sources payslip line); MW 18.40 / tipped 10.30 from 2026-07-01; D.C. Law 26-89 and Act 26-214 amend lump-sum retirement withholding only.',
}
SPECIAL = '''- Domestic: covered by MW; household withholding on FR-900Q; UI annual April 15; casual babysitters excluded from ASSLA [US-DCS5-013, US-DCS5-018, US-DCS5-005].
- Agricultural: no DC rule (federal).
- Minors: no youth subminimum; DOB on records under 19 [US-DCS5-001, US-DCS5-010].
- Tipped: 10.30 (56%) with top-up; mandatory third-party payroll (non-hotel); tip lines on payslip; ASSLA 1/43 at full MW [US-DCS5-001, US-DCS5-010, US-DCS5-011, US-DCS5-004].
- Clergy and students: excluded from ASSLA [US-DCS5-005].
- Nonresidents incl. NRAs living outside DC: no DC withholding with D-4A [US-DCP51-006, US-MULTI-016].
- Government: DC government excluded from tipped schedule, covered by ASSLA; District reimburses UI [US-DCS5-001, US-DCS5-005, US-DCS5-017].
- Security officers in office buildings: SCA Guard 1 wage + fringe; workers with disabilities: MW unless 14(c) certificate [US-DCS5-001].'''
LANG = 'Hire notice in English and the primary language where a Mayor template exists (32-1008(c)) [US-DCS5-010]; payslip English (US-OWN-006). DC postings page unreadable (recorded limit).'
UNRES = [
 {'key':'dc.wh.method','why':'2026 DC withholding method after D.C. Act 26-416 repealed personal exemptions is unpublished; D-4/D-4A "under review"; OTR withholding-instructions page 403.','attempted':['otr.cfo.dc.gov withholding instructions (403)','OTR forms page (D-4 under review)'],'close':'OTR tax notice or 2026/2027 FR-230 or D-4 revision (OTR Individual Income Tax Division), or the live instructions page via the orchestrator browser pass.','blocking':True},
 {'key':'dc.wh.supplemental.rate','why':'No flat supplemental rate in statute or any FR-230 edition; bonuses modelled as regular wages.','close':'An OTR statement in a future FR-230 or notice.','blocking':False},
 {'key':'dc.live.fy2027_bsa_permanent','why':'D.C. Law number and congressional-review end of the permanent FY2027 BSA not confirmed; decides whether 26-416 tax and PFL changes survive ~2026-11-11.','close':'code.dccouncil.gov laws page for the permanent act or LIMS B26 bill history.','blocking':True},
 {'key':'dc.sui.wage_base.other_state_credit','why':'51-103(e)(6) as read states no explicit credit for wages subject to another state UI.','close':'7 DCMR chapter 3 or DOES UI Employer Handbook.'},
 {'key':'dc.pit.std_deduction.cola','why':'2026 COLA amount of the DC standard deduction (assessment level) not read.','close':'OTR 2026 D-40 instructions.','blocking':False},
 {'key':'dc.payslip.electronic_and_deductions','why':'No DC rule found for electronic payslips, direct deposit, deduction authorisation or SSN truncation.','close':'7 DCMR chapter 9 and D.C. Code 28-3851 et seq.'},
 {'key':'dc.termination.vacation_and_ui_notice','why':'No DC statutory rule found for vacation payout or a UI separation notice.','close':'7 DCMR chapter 3 and the DOES OWH FAQ.'},
 {'key':'dc.leave.sick.coverage_threshold','why':'DOES fact sheet says at least 50% of time in DC while 32-1003(b) and 32-541.01 say more than 50%.','close':'7 DCMR 3299 (ASSLA definitions).'},
 {'key':'dc.report.sui.uc30_fields','why':'UC-30 / ESSP bulk-upload field layout is behind the employer login (gated).','close':'DOES ESSP file-upload specification from an employer account (owner/client).'},
]
