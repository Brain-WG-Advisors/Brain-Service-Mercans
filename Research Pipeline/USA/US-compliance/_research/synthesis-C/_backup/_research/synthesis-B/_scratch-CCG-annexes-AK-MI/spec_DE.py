NAME = 'Delaware'
SUMMARY = 'Minimum wage 15.00 (fixed since 2025-01-01, not indexed); FLSA overtime. PIT 0-6.6% (30 Del. C. 1102, not indexed); withholding per Employer Guide (standard deduction 3,250/6,500, 110 credit per exemption); statutory convenience rule; no reciprocity; Wilmington 1.25% EIT. SUI employer-only, base 14,500 (2026) / 16,500 (2027), new 1.0%; Operations & Technology 0.2% billed separately by letter from 2026. Delaware Paid Leave 0.80% (2025-2026), employee share up to 50%. Pay statement for employers with more than 3 employees. Oracle: Employer Guide examples (13.88 weekly; 269.63 supplemental).'
U = 'USD'
G = 'US-DES5-006'
FACTS = [
 ('labour_code','de.minwage.hourly',15.00,'US-DES5-001','2025-01-01',None,{'u':U,'n':'19 Del. C. 902(a)(5): last statutory step, not indexed, no 2027 step; equals federal if federal exceeds.'}),
 ('labour_code','de.minwage.tipped.cash_wage',2.23,'US-DES5-001','2026-01-01',None,{'u':U,'n':'Make-up to 15.00; mandatory tip pool capped at 15%; tips withheld as supplemental [US-DES5-021, US-DES5-006].'}),
 ('labour_code','de.minwage.exclusions','agriculture; private-home domestic service; EAP and outside sales; US government; fishing; under-18 camp counselors; DOC inmates; CBA minor-league baseball (901(3))','US-DES5-001','2026-01-01',None,{}),
 ('labour_code','de.pay_frequency.rule','at least once per calendar month on paydays designated in advance; due within 7 days of period close; nonwork-day payday moves earlier (1102)','US-DES5-002','2026-01-01',None,{}),
 ('labour_code','de.payment.method','cash or check cashable at full value nearby; direct deposit only on employee written request; no paycard rule','US-DES5-002','2026-01-01',None,{}),
 ('labour_code','de.wage_theft.penalty.max',20000,'US-DES5-002','2026-01-01',None,{'u':U,'n':'1102A: 2,000-20,000 per violation per employee for failing to withhold, failing to forward within 7 days, misclassification.'}),
 ('labour_code','de.minor.work_permit.required',True,'US-DES5-017','2026-01-01',None,{'n':'19 Del. C. 504, under 18.'}),
 ('income_tax','de.pit.bracket.1.ceiling',2000,'US-DES5-003','2014-01-01',None,{'u':U,'n':'0%.'}),
 ('income_tax','de.pit.bracket.2.ceiling',5000,'US-DES5-003','2014-01-01',None,{'u':U}),
 ('income_tax','de.pit.bracket.2.rate',2.2,'US-DES5-003','2014-01-01',None,{'u':'percent'}),
 ('income_tax','de.pit.bracket.3.ceiling',10000,'US-DES5-003','2014-01-01',None,{'u':U}),
 ('income_tax','de.pit.bracket.3.rate',3.9,'US-DES5-003','2014-01-01',None,{'u':'percent'}),
 ('income_tax','de.pit.bracket.4.ceiling',20000,'US-DES5-003','2014-01-01',None,{'u':U}),
 ('income_tax','de.pit.bracket.4.rate',4.8,'US-DES5-003','2014-01-01',None,{'u':'percent'}),
 ('income_tax','de.pit.bracket.5.ceiling',25000,'US-DES5-003','2014-01-01',None,{'u':U}),
 ('income_tax','de.pit.bracket.5.rate',5.2,'US-DES5-003','2014-01-01',None,{'u':'percent'}),
 ('income_tax','de.pit.bracket.6.ceiling',60000,'US-DES5-003','2014-01-01',None,{'u':U}),
 ('income_tax','de.pit.bracket.6.rate',5.55,'US-DES5-003','2014-01-01',None,{'u':'percent'}),
 ('income_tax','de.pit.bracket.7.rate',6.6,'US-DES5-003','2014-01-01',None,{'u':'percent','n':'Over 60,000.'}),
 ('income_tax','de.wh.method','annualise (daily x300, weekly x52, biweekly x26, semi-monthly x24, monthly x12); less standard deduction; table 0/66/261/741/1,001/2,943.50 + marginal rate; less 110 x exemptions; divide by periods',G,'2025-01-01',None,{'n':'Guide table "Effective January 1, 2025", live page. Base amounts re-derived from statute rates (Python). Rounding: none stated; examples round half-up to the cent.'}),
 ('income_tax','de.wh.std_deduction.single',3250,G,'2025-01-01',None,{'u':U,'n':'MFJ 6,500; MFS 3,250.'}),
 ('income_tax','de.wh.std_deduction.mfj',6500,G,'2025-01-01',None,{'u':U}),
 ('income_tax','de.wh.personal_credit.per_exemption',110,G,'2025-01-01',None,{'u':U}),
 ('income_tax','de.wh.duty','withhold whenever wages are subject to federal withholding ("If you withhold Federal tax, then you must withhold State tax"); residents and nonresidents','US-DES5-005','2026-01-01',None,{}),
 ('income_tax','de.wh.certificate','federal W-4 (DE worksheets SD/W-4A, W-4NR); no certificate = single, no allowances; copy to Division within 5 working days for 14+ allowances or exempt with wages over 168.50/week','US-DES5-008','2026-01-01',None,{'c':'medium','n':'Mapping of 2020+ W-4 to exemptions open (DE-OQ-1).'}),
 ('income_tax','de.wh.supplemental.method','with regular wages: one payment; separately: annualized-with minus annualized-without; tips same; deferred compensation recommended 5%',G,'2026-01-01',None,{}),
 ('income_tax','de.wh.deferred_comp.recommended_rate',5,G,'2026-01-01',None,{'u':'percent'}),
 ('non_resident','de.nonres.convenience_rule',True,'US-DES5-004','2026-01-01',None,{'n':'30 Del. C. 1124(b)(1)b statutory. Nonresident tax = resident-basis tax less 110 credits x DE-source / DE AGI (1121). Resident credit for other-state tax at assessment only (1111) [US-DES5-003]. No reciprocity [US-DES5-008].'}),
 ('non_resident','de.reciprocity.exists',False,'US-DES5-008','2026-01-01',None,{}),
 ('social_security','de.sui.wage_base',14500,'US-DES5-010','2026-01-01','2026-12-31',{'u':U,'vm':'second independent authority','n':'3302(28)(A)(viii); confirmed by DOL Merit Rate Table [US-DES5-022]. DOL FAQ still printing 18,500/10,500 is stale [US-DES5-011]. Other-state employment counts (3302(28)(A)(x)).'}),
 ('social_security','de.sui.wage_base',16500,'US-DES5-010','2027-01-01',None,{'u':U,'n':'Enacted (or FUTA base if higher).'}),
 ('social_security','de.sui.new_employer.rate',1.0,'US-DES5-022','2026-01-01','2026-12-31',{'u':'percent','n':'Construction new employer 1.0%; delinquent 6.3% (2025: 1.2% / 6.5%).'}),
 ('social_security','de.sui.employer.rate.min',0.3,'US-DES5-022','2026-01-01','2026-12-31',{'u':'percent','n':'Range 0.3%-5.4%; whether it excludes the separately billed Op & Tech 0.2% is open.'}),
 ('social_security','de.sui.employer.rate.max',5.4,'US-DES5-022','2026-01-01','2026-12-31',{'u':'percent'}),
 ('social_security','de.sui.employee.rate',0,'US-DES5-011','2026-01-01',None,{'u':'percent','c':'medium'}),
 ('social_security','de.sui.op_tech_assessment.rate',0.2,'US-DEL-003','2026-01-01','2026-12-31',{'u':'percent','n':'Billed separately by letter from 2026 (Q1 due 2026-08-31, Q2 2026-09-30; Op & Tech Lockbox) [US-DES5-011]; 0.175% from 2027. Separate DD/RSPEC payable line.'}),
 ('social_security','de.sui.op_tech_assessment.rate',0.175,'US-DEL-003','2027-01-01',None,{'u':'percent'}),
 ('social_security','de.pfml.rate.total',0.80,'US-DES5-012','2025-01-01','2026-12-31',{'u':'percent','n':'19 Del. C. 3705: medical 0.40 + caregiving 0.08 + parental 0.32; employer may deduct up to 50% of each; FICA wage base; 10-24 employees parental only (0.32%); 25+ all three; <=9 exempt. From 2027 DOL-set, cap 1.00% (unpublished).'}),
 ('social_security','de.pfml.rate.medical',0.40,'US-DES5-012','2025-01-01','2026-12-31',{'u':'percent'}),
 ('social_security','de.pfml.rate.family_caregiving',0.08,'US-DES5-012','2025-01-01','2026-12-31',{'u':'percent'}),
 ('social_security','de.pfml.rate.parental',0.32,'US-DES5-012','2025-01-01','2026-12-31',{'u':'percent'}),
 ('social_security','de.pfml.employee_share.max_percent',50,'US-DES5-012','2025-01-01',None,{'u':'percent'}),
 ('social_security','de.pfml.rate.cap',1.00,'US-DES5-012','2027-01-01',None,{'u':'percent'}),
 ('social_security','de.pfml.benefit.weekly_max',900,'US-DES5-012','2026-01-01','2027-12-31',{'u':U,'n':'80% of AWW, min 100; CPI-U Philadelphia-Camden-Wilmington after 2027.'}),
 ('social_security','de.pfml.multistate','coverage by primary worksite: employees primarily reporting to a DE worksite (3701(6)a), not UI localization','US-DES5-012','2026-01-01',None,{}),
 ('payslip_statute','de.payslip.employer_threshold',3,'US-DES5-002','2026-01-01',None,{'u':'employees','n':'1108: employers with MORE than 3 employees: at each payment (check, slip, or electronic if retainable; paper on request): wages due, pay period, each deduction, total hours for hourly. Hire notice of rate and payday.'}),
 ('payslip_statute','de.payslip.items','wages due; pay period; total deductions each separately specified; total hours for hourly employees','US-DES5-002','2026-01-01',None,{}),
 ('data_protection','de.records.retention_years',3,'US-DES5-002','2026-01-01',None,{'u':'years','n':'1108(6); 907 adds hours each day and week [US-DES5-001].'}),
 ('reporting_instruments','de.report.wh.frequency','July-June lookback: quarterly up to 4,500; monthly 4,500-25,000; eighth-monthly over 25,000 (statutory, indexed under 30 Del. C. 515; 2026 values not read)','US-DES5-005','2026-01-01',None,{'c':'medium'}),
 ('reporting_instruments','de.report.wh.calendar','quarterly: last day of month after quarter; monthly: 15th; eighth-monthly: 3 working days after periods ending 3rd/7th/11th/15th/19th/22nd/25th/last; tax type 01106','US-DES5-007','2026-01-01',None,{}),
 ('reporting_instruments','de.report.annual.wth_rec','WTH-REC (rev. 02/03/26) replaces W-3, due last day of January with W-2s; e-file if federal e-file; paper only for 10 or fewer forms; EFW2 with DE RS records; no SSN truncation','US-DES5-009','2026-02-03',None,{}),
 ('reporting_instruments','de.report.w2.paper_max_forms',10,'US-DES5-009','2026-02-03',None,{'u':'forms'}),
 ('reporting_instruments','de.report.sui.quarterly','UC-8 tax report + UC-8A wage report, due end of month after quarter; late 1.5%/month interest and 17.50 per late report; Online Employer Services Portal','US-DES5-011','2026-01-01',None,{}),
 ('reporting_instruments','de.report.pfml.quarterly','Hours & Wage Report and contributions in Delaware LaborFirst','US-DES5-013','2026-01-01',None,{}),
 ('reporting_instruments','de.newhire.report_days',20,'US-DES5-005','2026-01-01',None,{'u':'days','n':'30 Del. C. 1156A; rehire after 60+ days; fine 25 per failure.'}),
 ('reporting_instruments','de.report.w2.employee_on_termination_days',30,'US-DES5-005','2026-01-01',None,{'u':'days','n':'By Jan 31 or within 30 days of last wage payment on termination (1152).'}),
 ('leave','de.leave.sick.state_statute.exists',False,'US-DES5-021','2026-01-01',None,{'n':'DOL KB: no private-sector paid sick leave or required days off; policies must be made available (1108(3)).'}),
 ('leave','de.pfml.leave.parental_weeks',12,'US-DES5-012','2026-01-01',None,{'u':'weeks','n':'Medical/caregiving 6 weeks per 24 months; eligibility 12 months and 1,250 hours; employer decides within 5 business days and notifies DOL within 3.'}),
 ('termination','de.final_pay.rule','later of next regular payday or 3 business days after last day worked (quit, discharge, suspension, layoff); liquidated damages lower of 10%/day or unpaid wages','US-DES5-002','2026-01-01',None,{'n':'Vacation payout per written policy (1109, within 30 days); death: up to 300 to family without probate (1106).'}),
 ('benefits_in_kind','de.pit.conformity','rolling: DE taxable income = federal AGI as in effect with ch. 11 modifications (1105); federal exclusions flow through; no HSA/125 add-back found','US-DES5-019','2026-01-01',None,{'c':'medium'}),
 ('deductions_garnishments','de.deductions.rule','only if required by law, medical care without employer benefit, or signed authorization for a lawful purpose benefiting the employee (1107)','US-DES5-002','2026-01-01',None,{}),
 ('deductions_garnishments','de.garn.creditor.exempt_percent',85,'US-DES5-014','2026-01-01',None,{'u':'percent','n':'10 Del. C. 4913: max 15% of wages; apply lower of DE 15% of wages and CCPA 25% of disposable; one attachment at a time; not for State fines/taxes.'}),
 ('deductions_garnishments','de.garn.child_support.arrears_addon_percent',20,'US-DES5-016','2026-01-01',None,{'u':'percent','n':'13 Del. C. 513: CCPA cap; priority except federal tax liens; arrears up to 20% of current or 20/month; start within 7 days after first payday; EFT/EDI for 50+ employees; fee amount not in statute.'}),
 ('collective_agreements','de.prevailing_wage.threshold.new_construction',500000,'US-DES5-015','2026-01-01',None,{'u':U,'n':'29 Del. C. 6960; alteration/repair/renovation/demolition 45,000; weekly pay and weekly certified payroll to DOL; penalties 1,000-5,000 + treble.'}),
 ('collective_agreements','de.prevailing_wage.threshold.alteration',45000,'US-DES5-015','2026-01-01',None,{'u':U}),
 ('data_protection','de.breach.notice_days',60,'US-DES5-020','2026-01-01',None,{'u':'days','n':'6 Del. C. ch. 12B: AG notice > 500 residents; 1 year credit monitoring if SSN breached. Full SSN required on W-2 RS and IWO remittances.'}),
 ('live_change','de.live.hb13_hs2.status','draft in House Revenue & Finance Committee since 2025-06-17, NOT enacted; would act at assessment and withholding','US-DES5-018','2025-06-17',None,{}),
 ('oracle','de.oracle.guide.example1.withholding_weekly',13.88,G,'2025-01-01',None,{'u':U,'vm':'derived arithmetically','n':'Guide example 1: single, 1 allowance, 25,000 annual -> tax 832.00; weekly 13.88. Reproduced in Python.'}),
 ('oracle','de.oracle.guide.example2.supplemental',269.63,G,'2025-01-01',None,{'u':U,'vm':'derived arithmetically','n':'Guide example 2: 500/week + 5,000 bonus, single, 1 allowance -> 269.625, shown 269.63 (half-up to cent).'}),
]
LEGACY = [
 ('local_tax','de.local.wilmington.eit.rate',1.25,'US-DE-P5-2-001','2023-01-01',None,'Wilmington EIT: residents wherever they earn, nonresidents for work in the City; separate return and reconciliation to City Finance. Regulations rev. 2023 not re-verified; 2026 rate assumed at the 22 Del. C. 901-902 cap.'),
]
CITED = ['US-DES5-013','US-DES5-021','US-DEL-001','US-DEL-002','US-DEP9V-001','US-DEP7-001','US-DE-P5-2-002','US-MULTI-019','US-DEP9L-001']
NARR = {
 'labour_code': 'Overtime: no state premium rule (ch. 9 read in full); FLSA 1.5x over 40 (85%). No local minimum wages (absence, 85%). No youth subminimum.',
 'social_security': 'Industry and employer-size assessments (3350E/F) first payable 2027 [US-DEP9V-001]. Blue Collar training tax remains an open MANUAL item from P7 (US-DEL-004). No SDI/TDI.',
 'termination': 'UI separation notice and WARN not researched.',
 'indexation': 'MW, PIT brackets, standard deduction and 110 credit not indexed; SUI base statutory steps; withholding filing thresholds indexed under 30 Del. C. 515 (2026 values not read; Guide prints 6,020/33,460 undated); Paid Leave rate statutory to 2026 then DOL-set; max benefit CPI after 2027.',
}
SPECIAL = '''- Domestic: excluded from state MW (FLSA applies); UI at 1,000 cash/quarter; PIT follows federal (none required) [US-DES5-001, US-DES5-010, US-DES5-005].
- Agricultural: excluded from MW; UI at 20,000/quarter or 10+ workers in 20 weeks [US-DES5-001, US-DES5-010].
- Minors: work permit; no youth subminimum; under-18 camp counselors excluded; child working for parent UI-excluded [US-DES5-017, US-DES5-001, US-DES5-010].
- Tipped: cash wage 2.23 with make-up; tips employee property; pool cap 15%; supplemental withholding [US-DES5-001, US-DES5-021, US-DES5-006].
- Clergy/religious organisations: UI exclusion per 3302(15)(E); volunteers MW-excluded [US-DES5-010, US-DES5-001].
- Students: own-school and work-study UI-excluded [US-DES5-010].
- NRAs: no DE rule beyond federal [US-DES5-005]. Other-state employees: DE-source wages, convenience rule [US-DES5-004, US-DES5-008].
- Commission agents/direct sellers: UI-excluded [US-DES5-010].
- Government: excluded from ch. 11 and UI (except 3302(14)(B)); US employees MW-excluded; State-plan employees excluded from Paid Leave [US-DES5-002, US-DES5-010, US-DES5-012].
- Family employment: UI-excluded [US-DES5-010, US-DES5-011].
- Small employers: payslip duty only above 3 employees; Paid Leave <10 exempt, 10-24 parental only [US-DES5-002, US-DES5-012].'''
LANG = 'Paid-leave poster in English, Spanish and any first language of 5%+ of the workforce (19 Del. C. 3710(c)) [US-DEL-001]; bilingual expressly permitted [US-DEP9L-001]; payslip English (US-OWN-006).'
UNRES = [
 {'key':'de.wh.w4_2020_mapping','why':'The Employer Guide uses pre-2020 allowance wording; how a 2020+ W-4 maps to DE personal exemptions for the 110 credit is not stated.','close':'Division of Revenue memo/FAQ on the 2020+ W-4 (Withholding unit 302-577-8779) or a DE-specific certificate.','blocking':True},
 {'key':'de.report.wh.thresholds.current','why':'2026 indexed withholding filing thresholds not read (Guide prints 6,020 / 33,460 undated).','close':'2026 lookback notice or 30 Del. C. 515 adjustment table from the Division of Revenue.'},
 {'key':'de.pfml.rate.next_year','why':'2027 Paid Leave contribution rate is DOL-set (cap 1.00%) and unpublished on 2026-11-02.','close':'DOL Delaware Paid Leave notice or regulation for 2027.'},
 {'key':'de.garn.iwo.employer_fee','why':'13 Del. C. 513(b)(8)a refers to a State-set fee without stating it.','close':'DCSS employer page or regulation stating the fee.'},
 {'key':'de.sui.rate_range.op_tech_inclusion','why':'Unclear whether the 2026 0.3%-5.4% range excludes the separately billed 0.2% Op & Tech.','close':'A 2026 DOL employer rate letter or the DOL Employer Handbook.'},
 {'key':'de.report.sui.uc8a_format','why':'UI separation-notice duty and UC-8A electronic wage-file format not read (budget).','close':'DOL Employer Handbook linked from the employer-services page.'},
 {'key':'de.live.session_law_amendments','why':'Content of 85 Del. Laws c. 301 (amending 1154) and enactment date of the 1103 three-business-day wording not identified.','close':'Session-law pages on legis.delaware.gov.','blocking':False},
 {'key':'de.local.wilmington.eit.current','why':'Wilmington EIT regulations (rev. 2023) not re-verified; 2026 rate assumed at the statutory 1.25% cap.','close':'City of Wilmington Finance EIT page or the 2026 employer reconciliation form.'},
]
