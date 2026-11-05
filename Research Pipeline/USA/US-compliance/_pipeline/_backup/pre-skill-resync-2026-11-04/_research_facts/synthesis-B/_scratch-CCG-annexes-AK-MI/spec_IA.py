NAME = 'Iowa'
SUMMARY = 'Minimum wage 7.25 (6.35 first 90 days); local mandates void (364.3(12)); FLSA overtime. Flat 3.8% PIT; 2026 withholding formula T1=G-D, x3.80%, less W/P, + A, computed TO THE CENT (correction: not whole dollar as US-IA-001 and the MANDATE currency block say); supplemental 3.8%; reciprocity with IL only; school/EMS surtaxes at assessment. UI employer-only, base 20,400 (2026) / 21,100 (2027) after SF 607, max 5.4%, new 1.0%; other-state wages do NOT count. Pay statement 91A.6. New hire within 15 days. Oracle: IDR formula PDF examples.'
U = 'USD'
F = 'US-IAS5-005'
FACTS = [
 ('labour_code','ia.minwage.hourly',7.25,'US-IAS5-001','2008-01-01',None,{'u':U,'n':'91D.1(1)(a),(b): or federal if higher; enterprises under 300,000 gross exempt (not laundries, construction, hospitals, care, schools, public agencies). Not indexed.'}),
 ('labour_code','ia.minwage.first_90_days.hourly',6.35,'US-IAS5-001','2008-01-01',None,{'u':U}),
 ('labour_code','ia.local_mandates.preempted',True,'US-IAS5-021','2017-03-30',None,{'n':'364.3(12): no city minimum/living wage, leave, benefits or scheduling ordinances.'}),
 ('labour_code','ia.pay_frequency.rule','at least monthly, semimonthly or biweekly on designated paydays; payday at most 12 days after period end excluding Sundays/holidays; written agreement may vary; commissions true-up at least every 12 months (91A.3(1))','US-IAS5-002','2026-01-01',None,{}),
 ('labour_code','ia.payment.method','US currency or negotiable instrument; in kind with written consent; direct deposit may be a condition of employment for hires from 2005-07-01 (3 exceptions); employer pays overdraft charges from late pay; expenses reimbursed within 30 days','US-IAS5-002','2026-01-01',None,{}),
 ('labour_code','ia.late_wages.liquidated_damages_percent_per_day',5,'US-IAS5-027','2026-01-01',None,{'u':'percent','n':'91A.2(6): excluding Sundays, holidays and first 7 days; capped at unpaid amount.'}),
 ('labour_code','ia.minor.under16.school_week_max_hours',28,'US-IAS5-014','2026-01-01',None,{'u':'hours','n':'92.7: 7am-9pm (11pm June-Labor Day); 8 h/day, 40 h/week; 6 h/day and 28 h/week in session; 30-min break for 5+ h.'}),
 ('income_tax','ia.pit.rate.flat',3.8,'US-IAS5-006','2025-01-01',None,{'u':'percent','n':'422.5(1)(a); nonresident fraction at assessment; resident credit at assessment.'}),
 ('income_tax','ia.wh.method','T1 = G - D; T2 = T1 x 3.80%; T3 = T2 - W/P; T4 = T3 + A (2026 formula, released Nov 2025); tables alternative [US-IAS5-015]',F,'2026-01-01','2026-12-31',{'vm':'derived arithmetically','n':'Six 2024+ IA W-4 examples re-derived in Python to the cent. P: daily 260, weekly 52, biweekly 26, semimonthly 24, monthly 12.'}),
 ('income_tax','ia.wh.rounding','to the cent, half-up (no whole-dollar rounding in 2026)',F,'2026-01-01','2026-12-31',{'n':'Tables Step 5: "rounded to the nearest cent" [US-IAS5-015]. Supersedes the rounding clause of US-IA-001 and the MANDATE currency block listing IA as whole-dollar (S5A-MERGE note on US-IA-001).'}),
 ('income_tax','ia.wh.deduction.other',13000,F,'2026-01-01','2026-12-31',{'u':U,'n':'Other / MFJ spouse with income / missing status; weekly 250, biweekly 500, semimonthly 541.67, monthly 1,083.33, daily 50. Pre-2024 W-4: Single 13,000, Married 26,000, W = allowances x 40.'}),
 ('income_tax','ia.wh.deduction.hoh',19500,F,'2026-01-01','2026-12-31',{'u':U}),
 ('income_tax','ia.wh.deduction.mfj_one_earner_qss',26000,F,'2026-01-01','2026-12-31',{'u':U}),
 ('income_tax','ia.wh.allowance.per_dependent',40,'US-IAS5-029','2026-01-01',None,{'u':U,'n':'2026 IA W-4 44-019a (11/13/2025); due within 15 days of hire; none on file = zero allowances; keep 4 years; new W-4 within 10 days when allowances decrease.'}),
 ('income_tax','ia.wh.supplemental.rate',3.8,'US-IAS5-016','2026-01-01',None,{'u':'percent','vm':'second independent authority','n':'422.16(2)(e) and 701 IAC 307.2(1)(c) [US-IAS5-006]: when treated separately and federal withheld at flat rate; otherwise aggregate.'}),
 ('income_tax','ia.wh.exempt.threshold.single_under65',9000,'US-IAS5-016','2026-01-01',None,{'u':U,'n':'13,500 MFJ/HoH under 65; 32,000 / 24,000 at 65+; nonresidents may not claim EXEMPT.'}),
 ('income_tax','ia.wh.exempt.threshold.mfj_hoh_under65',13500,'US-IAS5-016','2026-01-01',None,{'u':U}),
 ('income_tax','ia.pit.obbba','tips, overtime, car-loan interest conformed at ASSESSMENT only (no withholding allowance); senior deduction (up to 6,000) may be claimed as an IA W-4 allowance','US-IAS5-019','2026-01-01',None,{}),
 ('non_resident','ia.reciprocity.states','IL','US-IAS5-016','2026-01-01',None,{'n':'IL resident in IA files 44-016 (employer withholds IL); IA resident in IL files IL-W-5-NR [US-MULTI-018]. Nonresidents otherwise withheld at resident rate from first day (no threshold); exceptions interstate carriers, film/TV (44-017), disaster workers (29C.24).'}),
 ('local_tax','ia.local.surtax.withheld',False,'US-IAS5-029','2026-01-01',None,{'n':'School-district and EMS surtaxes settled on IA 1040 by residence; employee may adjust allowances/line 8 [US-IAP51-005, US-IAP52-001].'}),
 ('social_security','ia.sui.wage_base',20400,'US-IAS5-009','2026-01-01','2026-12-31',{'u':U,'vm':'derived arithmetically','n':'96.1A(36) as amended by SF 607: 1/3 of AAW rounded up to next 100, not below FUTA: 61,098.90/3 = 20,366.30 -> 20,400 [US-IAS5-008]. 2025: 39,500.'}),
 ('social_security','ia.sui.wage_base',21100,'US-IAS5-010','2027-01-01',None,{'u':U,'vm':'derived arithmetically','n':'Announced 2026-06-30: 63,213.58/3 = 21,071.19 -> 21,100.'}),
 ('social_security','ia.sui.employer.rate.max',5.4,'US-IAP9V-001','2026-01-01','2026-12-31',{'u':'percent','n':'Table D, ranks 1-9, 0.000%-5.400% (max cut from 9%, tables 8 -> 4).'}),
 ('social_security','ia.sui.employer.rate.min',0,'US-IAP9V-001','2026-01-01','2026-12-31',{'u':'percent'}),
 ('social_security','ia.sui.new_employer.rate',1.0,'US-IAS5-011','2026-01-01','2026-12-31',{'u':'percent','n':'Non-construction: rank-4 rate but not less than 1.000% until 12 chargeable quarters; construction rank 9 = 5.400%.'}),
 ('social_security','ia.sui.new_employer.construction.rate',5.4,'US-IAS5-011','2026-01-01','2026-12-31',{'u':'percent'}),
 ('social_security','ia.sui.employee.rate',0,'US-IAS5-024','2026-01-01',None,{'u':'percent','n':'871 IAC 23.6(2).'}),
 ('social_security','ia.sui.wage_base.other_state_credit',False,'US-IAS5-024','2026-01-01',None,{'n':'23.6(3): only wages reported to Iowa UI count; successor with experience transfer may count predecessor wages (23.6(4)). Reported tips are UI wages (23.5).'}),
 ('payslip_statute','ia.payslip.items','hours worked, wages earned, deductions made, each regular payday (91A.6(4)); mail, secure electronic, workplace or view access, no separate consent; itemised computation within 10 working days on request','US-IAS5-027','2026-01-01',None,{'c':'medium','n':'Statute row is legacy US-IAP51-002; reach follows Iowa work location (91A.2(3),(4)).'}),
 ('reporting_instruments','ia.report.wh.filer_class','quarterly < 6,000/yr and <= 500/month; monthly 6,000-120,000 (15th); semimonthly > 5,000 per semimonthly period (25th / 10th, electronic); annual election <= 2 employees; quarterly return last day of month after quarter via GovConnectIowa, zero returns required','US-IAS5-016','2026-01-01',None,{'n':'422.16(4) [US-IAS5-007].'}),
 ('reporting_instruments','ia.report.annual_reconciliation.exists',False,'US-IAS5-017','2026-01-01',None,{'n':'VSPs no longer required.'}),
 ('reporting_instruments','ia.report.w2','e-file via GovConnectIowa by February 15 only W-2/1099 with IA withholding; IDR-unique 512-byte EFW2-based format (SSA file rejected); RS state code 19, permit 248-267; IA RV record; Key & Send; employee copy Jan 31, terminated on request within 30 days','US-IAS5-018','2023-01-09',None,{'c':'medium','n':'Spec page dated 2023-01-09 (TY2023-2025); TY2026 edition not seen.'}),
 ('reporting_instruments','ia.report.sui.quarterly','Employer Contribution and Payroll Report 65-5300 + wage detail by SSN, electronic, due last day of month after quarter (871 IAC 23.8(1))','US-IAS5-024','2026-01-01',None,{}),
 ('reporting_instruments','ia.newhire.report_days',15,'US-IAS5-012','2026-01-01',None,{'u':'days','n':'252G.3: employer name/address/FEIN; employee name/address/SSN/DOB; dependent health coverage availability and date; IWO address; independent contractors too.'}),
 ('leave','ia.leave.sick.state_mandate.exists',False,'US-IAS5-021','2026-01-01',None,{'c':'medium'}),
 ('termination','ia.final_pay.rule','next regular payday for the period in which wages were earned (no discharge/resignation distinction); commission true-up within 30 days; vacation only per agreement/pro-rata policy (91A.4)','US-IAS5-003','2026-01-01',None,{}),
 ('termination','ia.separation.wage_request_response_days',10,'US-IAS5-026','2026-01-01',None,{'u':'days','c':'medium','n':'No separation notice statute; IWD Notice of Separation and Wage Request answered within 10 days.'}),
 ('benefits_in_kind','ia.pit.conformity','rolling IRC conformity from TY2023; withholding on same wages as federal; 401(k)/125/HSA/transit/GTL follow federal','US-IAS5-020','2023-01-01',None,{'c':'medium'}),
 ('deductions_garnishments','ia.deductions.rule','required by law, court order, or written authorisation for employee benefit; prohibited: shared till shortages, dishonoured checks, non-wilful breakage, lost non-assigned property, gratuities, PPE, relocation over 20 (91A.5)','US-IAS5-004','2026-01-01',None,{}),
 ('deductions_garnishments','ia.garn.creditor.annual_cap_schedule','per judgment creditor by expected annual earnings: < 12,000: 250; 12,000-16,000: 400; 16,000-24,000: 800; 24,000-35,000: 1,500; 35,000-50,000: 2,000; >= 50,000: 10% (plus CCPA)','US-IAS5-013','2026-01-01',None,{'n':'642.21; not for support; not indexed.'}),
 ('deductions_garnishments','ia.garn.child_support.employer_fee',2,'US-IAS5-022','2026-01-01',None,{'u':U,'n':'252D.17: per payment within CCPA; IWO priority; remit to CSC within 7 business days.'}),
 ('deductions_garnishments','ia.garn.child_support.remit_business_days',7,'US-IAS5-022','2026-01-01',None,{'u':'business days'}),
 ('data_protection','ia.breach.notice','without unreasonable delay; processor notifies owner immediately (715C.2)','US-IAS5-023','2026-01-01',None,{}),
 ('live_change','ia.live.hf2212.status','NOT enacted (introduced 2026-01-29, referred House HHS): direct-care minimum 20.00 - do not model','US-IAS5-028','2026-01-29',None,{}),
 ('oracle','ia.oracle.formula.example6.withholding',114.92,F,'2026-01-01','2026-12-31',{'u':U,'vm':'derived arithmetically','c':'medium','n':'Formula PDF example 6 (monthly 5,000, HoH, W = 160) printed WITHOUT its final figure; derived 114.92 = (5,000 - 1,625) x 3.8% - 160/12. The other examples (e.g. 59.26, 38.72, 145.50) are printed and reproduced to the cent.'}),
]
LEGACY = []
CITED = ['US-IA-001','US-IA-002','US-IAL-001','US-IAL-002','US-IAS5-015','US-IAS5-025','US-IAP9W-001','US-IAP9L-001','US-IAP9L-002','US-IAP51-002','US-IAP51-005','US-IAP52-001','US-IAP52-002','US-IAP52-004','US-IAP51-001','US-IAP51-003','US-IAP51-004','US-MULTI-018']
NARR = {
 'labour_code': 'No state overtime rule: ch. 91D adopts FLSA (negative on 91D.1 only, 85%). HF 2212 not enacted.',
 'social_security': 'No SDI/TDI/PFML [US-IAP52-004 legacy; mandate US-MQ-32]. 260E/260F training items are credits diverting withholding (NJC 1.5%/3%, SJC 1.5%, ACE up to 10%, TJC 3%), claimed on the quarterly return - not levies [US-IAS5-016]. 2027 rate table unpublished.',
 'collective_agreements': 'No state prevailing-wage law (DOL WHD list 2023) [US-IAP51-001 legacy].',
 'indexation': 'UI base 1/3 AAW yearly (late-June release); rate table by fund formula; PIT flat not indexed (deduction amounts reissued each November); MW and garnishment brackets fixed.',
 'live_change': 'SF 607 in force CY2026 (employer UI level); 2027 base 21,100; 2026 formula/IA W-4 (withholding); OBBBA deductions (assessment); sports wagering 3.8% (non-wage). Full 2026 Acts sweep not done.',
}
SPECIAL = '''- Domestic: generally excluded from IA withholding; UI at 1,000/quarter [US-IAS5-016, US-IAS5-025].
- Agricultural: withholding follows federal; UI 20,000/quarter or 10+ in 20 weeks [US-IAS5-016, US-IAS5-025, US-IAS5-027].
- Minors: no youth rate beyond 90-day rate; under-16 hours; child under 18 for parent UI-excluded [US-IAS5-001, US-IAS5-014, US-IAS5-025].
- Tipped: tip credit up to 40% of MW (cash wage 4.35 derived on 7.25) for restaurants/hotels/motels/inns/cabins with > 30/month tips; tips UI wages; OBBBA tip deduction at assessment [US-IAS5-001, US-IAS5-024].
- Clergy: excluded from IA withholding; church service excluded from UI [US-IAS5-016, US-IAS5-025].
- Students: own-school and curricular work UI-excluded [US-IAS5-025].
- NRAs: IDR additional withholding guidance (15,000 or 29,200 / P x 3.8%) via line 8; no EXEMPT [US-IAS5-016, US-IAS5-029].
- Statutory employees: follow federal [US-IAS5-016].
- Government: withholding agents; reimbursing UI employers; ch. 91D applies [US-IAS5-025].
- Military spouses: MSRRA/VBTA box [US-IAS5-016, US-IAS5-029]. Interstate transport nonresidents: no IA withholding. New employees first 90 days: 6.35. Corporate officers: UI employees.'''
LANG = 'No language rule; payslip English [US-IAL-001, US-IAP9L-001, US-IAP9L-002] (US-OWN-006).'
UNRES = [
 {'key':'ia.wh.rounding.history','why':'US-IA-001 and the MANDATE currency block say whole-dollar; 2026 formula/tables say nearest cent. The 2025 formula was not read.','close':'Synthesis supersedes the rounding clause of US-IA-001 by US-IAS5-005/-015 (done in S5A note); optionally IDR 2025 formula PDF. Scaffolder to amend the MANDATE currency block (US-MQ-01).','blocking':False},
 {'key':'ia.sui.rate_table.next_year','why':'CY2027 rate table not yet published.','close':'IWD "Information on Rate Computations for Private Employers 2027" or November 2026 rate notices.'},
 {'key':'ia.report.sui.file_format','why':'myIowaUI quarterly wage-detail upload layout not acquired.','close':'IWD myIowaUI file specification (UI Tax Bureau, iwduitax@iwd.iowa.gov).'},
 {'key':'ia.report.w2.spec_next_edition','why':'IDR W-2 spec covers TY2023-2025 filed in 2026.','close':'IDR TY2026 edition on the same URL (late 2026).'},
 {'key':'ia.live.acts_2026_sweep','why':'Full sweep of 2026 enrolled Acts touching chs. 91A, 91D, 92, 96, 252D, 422, 642 not done.','close':'Iowa Legislature Acts and Joint Resolutions 2026 list or Iowa Code 2027 supplement.'},
 {'key':'ia.data_protection.ssn_paystub','why':'Iowa Code 715A not read.','close':'Iowa Code 715A.10 and 715A.8 text.','blocking':False},
 {'key':'ia.garn.state_tax_levy','why':'IDR wage-levy procedure not read.','close':'Iowa Code 422.26 / 626 levy provisions or the IDR levy page.','blocking':False},
 {'key':'ia.overtime.state_rule','why':'Negative rests on 91D.1 only.','close':'DIAL Labor Services wage-hour FAQ or the rest of ch. 91D.','blocking':False},
 {'key':'ia.leave.jury_military','why':'Not researched.','close':'Iowa Code 607A.45 and 29A.43.','blocking':False},
]
