NAME = 'Maine'
SUMMARY = 'Minimum wage 15.10 (2026) / 15.70 (2027), CPI-W indexed; Portland 16.75 / 17.75 / 19.00; tip credit max 50%; salaried-exempt threshold 3,000 x MW. Withholding per 2026 booklet: 5,300 per W-4ME allowance; withholding standard deduction 12,450 / 27,750 with phase-out (NOT the return-level 15,300 / 30,600); 5.80 / 6.75 / 7.15%; round to dollar; supplemental 5%; nonresident 12 days AND 3,000 threshold; no reciprocity, no local tax. UI base 12,000, new 2.54% (2.23 + CSSF 0.14 + UPAF 0.17); PFML 1.0% (15+) / 0.5% (<15). Pay statement REQUIRED (26 MRSA 665(1), corrects earlier rows). New hire within 7 days. Oracle: booklet examples 0 / 33 / 257.'
U = 'USD'
B = 'US-MES5-011'
FACTS = [
 ('labour_code','me.minwage.hourly',15.10,'US-MES5-002','2026-01-01','2026-12-31',{'u':U,'n':'Agricultural and non-agricultural; CPI-W Northeast Aug-Aug rounded to 0.05 each Jan 1 [US-MES5-001]; step 15.10 -> 15.70 not reproduced (CPI not fetched).'}),
 ('labour_code','me.minwage.hourly',15.70,'US-MES5-003','2027-01-01',None,{'u':U,'n':'2027 poster (rev. 9/26).'}),
 ('labour_code','me.minwage.tip_credit.max_percent',50,'US-MES5-001','2026-01-01',None,{'u':'percent','n':'Cash wage >= 7.55 in 2026 (derived); notice items A-F; weekly shortfall test; card tips by next payday without fee.'}),
 ('labour_code','me.minwage.tipped.cash_wage',7.55,'US-MES5-001','2026-01-01','2026-12-31',{'u':U,'vm':'derived arithmetically','n':'15.10 x 0.5.'}),
 ('labour_code','me.local_minwage.portland.hourly',16.75,'US-MES5-012','2026-01-01','2026-12-31',{'u':U,'n':'Hours within city limits; City employees from 2026-07-01; tip credit max half city rate; emergency work 1.5x; CPI-U Northeast from 2029. State does not pre-empt local MW (paid leave is pre-empted).'}),
 ('labour_code','me.local_minwage.portland.hourly',17.75,'US-MES5-012','2027-01-01','2027-12-31',{'u':U}),
 ('labour_code','me.local_minwage.portland.hourly',19.00,'US-MES5-012','2028-01-01',None,{'u':U}),
 ('labour_code','me.overtime.weekly_threshold_hours',40,'US-MES5-001','2026-01-01',None,{'u':'hours','n':'1.5x; no daily OT; regular rate includes bonuses/commissions; exemptions auto sales/service, mariners, most public employees, listed ag/fish processing [US-MES5-005].'}),
 ('labour_code','me.exempt.salary.weekly_min',871.16,'US-MES5-002','2026-01-01','2026-12-31',{'u':U,'n':'Annualised pay must exceed 3,000 x State MW (or FLSA level): 3,000 x 15.10 / 52 = 871.1538 -> poster 871.16 (first cent above). 2027 poster 905.79 vs formula 905.77 (Q2): safe rule salary must EXCEED 3,000 x MW.'}),
 ('labour_code','me.pay_frequency.rule','intervals not exceeding 16 days; each payment covers wages to within 8 days of payday; closed-day payday moves to next business day; lengthening interval needs 30 days written notice; rate decrease needs prior notice','US-MES5-004','2026-01-01',None,{}),
 ('labour_code','me.direct_deposit.fee_prohibited',True,'US-MES5-004','2026-01-01',None,{'n':'621-A(7); no consent/paycard rule in text read.'}),
 ('income_tax','me.wh.method','annualise (52/26/24/12/260); - 5,300 per W-4ME allowance; - withholding standard deduction; apply schedule; divide by periods; round to nearest dollar',B,'2026-01-01','2026-12-31',{'n':'2026 booklet (rev. Dec 2025). Do not reduce for federal W-4 Step 4(b) deductions.'}),
 ('income_tax','me.wh.allowance.annual',5300,B,'2026-01-01','2026-12-31',{'u':U}),
 ('income_tax','me.wh.std_deduction.single',12450,B,'2026-01-01','2026-12-31',{'u':U,'n':'If wages <= 102,250; else 12,450 x (177,250 - W) / 75,000; zero from 177,250. NOT the return-level 15,300 (US-ME-P5-2-001 S5A note).'}),
 ('income_tax','me.wh.std_deduction.married',27750,B,'2026-01-01','2026-12-31',{'u':U,'n':'If wages <= 204,550; else 27,750 x (354,550 - W) / 150,000; zero from 354,550.'}),
 ('income_tax','me.wh.std_deduction.single.phaseout_start',102250,B,'2026-01-01','2026-12-31',{'u':U}),
 ('income_tax','me.wh.std_deduction.single.phaseout_end',177250,B,'2026-01-01','2026-12-31',{'u':U}),
 ('income_tax','me.wh.bracket.married.1.ceiling',54850,B,'2026-01-01','2026-12-31',{'u':U,'n':'5.80% below 54,850; 3,181 + 6.75% to 129,750; 8,237 + 7.15% above.'}),
 ('income_tax','me.wh.bracket.married.2.ceiling',129750,B,'2026-01-01','2026-12-31',{'u':U}),
 ('income_tax','me.wh.bracket.1.rate',5.80,B,'2026-01-01','2026-12-31',{'u':'percent'}),
 ('income_tax','me.wh.bracket.2.rate',6.75,B,'2026-01-01','2026-12-31',{'u':'percent'}),
 ('income_tax','me.wh.bracket.3.rate',7.15,B,'2026-01-01','2026-12-31',{'u':'percent'}),
 ('income_tax','me.wh.supplemental.rate',5,B,'2026-01-01',None,{'u':'percent','n':'Aggregated or flat 5% when paid separately; backup withholding 5%.'}),
 ('income_tax','me.wh.certificate','W-4ME required; none valid = single, zero allowances; more allowances need MRS Allowance Variance Certificate; copy to MRS when IRS demands W-4 or non-Maine-address exempt claimant expects >= 5,000 Maine-source pay',B,'2026-01-01',None,{}),
 ('non_resident','me.nonres.threshold','taxable only if present in Maine more than 12 days AND more than 3,000 Maine-source pay in the year (training, inspection, R&D, project-team days excluded)','US-MES5-011','2026-01-01',None,{'c':'medium','n':'Rule on legacy US-ME-P5-2-003; resident credit [US-ME-P5-2-004]; no reciprocity in force [US-ME-P5-2-005].'}),
 ('local_tax','me.local_wage_tax.exists',False,'US-MER3-001','2026-01-01',None,{'n':'[US-MER3-002].'}),
 ('social_security','me.sui.wage_base',12000,'US-MES5-020','2026-01-01',None,{'u':U,'n':'Fixed, not indexed; other-state wages by same legal entity and predecessor wages count (26 MRSA 1043(19)); non-cash remuneration at cash value.'}),
 ('social_security','me.pfml.rate.total.15_plus',1.0,'US-MEP6-001','2025-01-01','2027-12-31',{'u':'percent','c':'medium','n':'FAQ (A.3) + statute ceiling 1.0% [US-MES5-024]: 15+ employees employer remits 1.0%, employee max 0.5%; < 15: 0.5% remitted, all deductible. From 2028 department sets by Oct 1. Cap SSA base; employee share deducted AFTER tax; employer-paid employee share is taxable wages; W-2 box 14 "MEPFML"; late 1% of quarterly payroll; coverage follows UI localization.'}),
 ('social_security','me.pfml.rate.total.under_15',0.5,'US-MEP6-001','2025-01-01','2027-12-31',{'u':'percent','c':'medium'}),
 ('social_security','me.pfml.employee.max_rate',0.5,'US-MEP6-001','2025-01-01','2027-12-31',{'u':'percent','c':'medium'}),
 ('social_security','me.pfml.employee_deduction.after_tax',True,'US-MES5-025','2025-01-01',None,{'c':'medium'}),
 ('social_security','me.pfml.w2_box14_label','MEPFML','US-MES5-025','2025-01-01',None,{'c':'medium'}),
 ('payslip_statute','me.payslip.required',True,'US-MES5-006','2026-01-01',None,{'n':'26 MRSA 665(1): with each payment: pay-period date, hours, total earnings, itemized deductions; same record at time of electronic transfer; electronic only with ready access and free printing. CORRECTS US-ME-P5-1-004 / US-ME-P5-2-006 (superseded).'}),
 ('payslip_statute','me.payslip.items','date of the pay period, hours, total earnings, itemized deductions','US-MES5-006','2026-01-01',None,{}),
 ('data_protection','me.records.retention_years',3,'US-MES5-006','2026-01-01',None,{'u':'years','n':'665(1); 622 date/amount and daily time records except salaried exempt [US-MES5-026]. SSN not requestable on applications [US-MES5-009].'}),
 ('reporting_instruments','me.report.wh.941me','quarterly, due last day of month after quarter; electronic mandatory (Rule 104) even if nothing to report; deposits semiweekly if look-back >= 18,000 else quarterly; 900ME voucher; no W-3ME after TY2023',B,'2026-01-01',None,{}),
 ('reporting_instruments','me.report.w2','electronic with MRS by 31 January, paper not accepted; Maine Tax Portal Bulk File Upload Specifications (EFW2 acceptance open); 50 per missing statement',B,'2026-01-01',None,{}),
 ('reporting_instruments','me.report.sui.uc1','ME UC-1 quarterly, last day of month after quarter, via ReEmployME (file spec published) or paper, filed with MRS; monthly employment (12th), gross/excess/taxable wages, UC rate, CSSF, UPAF; interest 10% from 2026-01-01','US-MES5-021','2026-01-01',None,{}),
 ('reporting_instruments','me.newhire.report_days',7,'US-MES5-016','2026-01-01',None,{'u':'days','n':'To DHHS within 7 days of first services (stricter than federal 20); rehires after 60+ days; DOB; employer UI/UBI number; independent contractors expected >= 2,500 also within 7 days.'}),
 ('reporting_instruments','me.newhire.contractor_threshold',2500,'US-MES5-016','2026-01-01',None,{'u':U}),
 ('leave','me.leave.earned_paid.employer_threshold',10,'US-MES5-008','2026-01-01',None,{'u':'employees','n':'26 MRSA 637: MORE than 10 employees for > 120 days; 1 h per 40 h up to 40 h/yr, any purpose; use after 120 days; carryover (PL 2025 c.438 does not reduce next year accrual); base rate; seasonal excluded; local ordinances pre-empted.'}),
 ('leave','me.leave.earned_paid.accrual.hours_worked_per_hour',40,'US-MES5-008','2026-01-01',None,{'u':'hours'}),
 ('leave','me.leave.earned_paid.cap_hours',40,'US-MES5-008','2026-01-01',None,{'u':'hours'}),
 ('termination','me.final_pay.rule','no later than next established payday (discharge or resignation); on demand earlier of next payday or 2 weeks; accrued vacation from 2023-01-01 payable (not employers with <= 10 employees or public; CBA overrides); liquidated damages 2x','US-MES5-007','2026-01-01',None,{}),
 ('termination','me.severance.mass_layoff','establishments with 100+ employees: one week pay per year of service, within one pay period after last day; 90 days notice','US-MES5-010','2026-01-01',None,{}),
 ('benefits_in_kind','me.pit.conformity_date','2025-12-31 (fixed); no additions for HSA, 125, transit, 401(k) (36 MRSA 5122) - federal exclusions followed','US-MES5-018','2026-01-01',None,{'n':'[US-MES5-027].'}),
 ('deductions_garnishments','me.garn.creditor.rule','least of 25% of disposable, excess over 40 x higher of federal/State MW, or the total','US-MES5-013','2026-01-01',None,{}),
 ('deductions_garnishments','me.garn.creditor.weekly_protected',604.00,'US-MES5-013','2026-01-01','2026-12-31',{'u':U,'vm':'derived arithmetically','n':'40 x 15.10.'}),
 ('deductions_garnishments','me.garn.employer_fee_per_check',1,'US-MES5-014','2026-01-01',None,{'u':U,'n':'Answer within 20 days; no discharge.'}),
 ('deductions_garnishments','me.garn.child_support.remit_business_days',7,'US-MES5-015','2026-01-01',None,{'u':'business days','n':'Order adds 2/week; priority over non-support; processing fee only by DHHS rule.'}),
 ('collective_agreements','me.prevailing_wage.threshold',50000,'US-MES5-017','2026-01-01',None,{'u':U,'n':'State-funded public works >= 50,000 (< 10,000 never construction); energy projects >= 2 MW; certified payroll filed monthly; records 3 years; fine >= 250/employee/day.'}),
 ('oracle','me.oracle.booklet.examples_weekly','0 / 33 / 257',B,'2026-01-01','2026-12-31',{'vm':'derived arithmetically','n':'Booklet Examples 1-3 reproduced in Python (weekly, rounded to dollar). No official calculator [US-ME-P5-2-009].'}),
]
LEGACY = [
 ('income_tax','me.wh.bracket.single.1.ceiling',27400,'US-ME-P5-2-001','2026-01-01','2026-12-31','Single 5.80% below 27,400; 1,589 + 6.75% to 64,850; 4,117 + 7.15% above. Same booklet file as US-MES5-011; use 12,450/27,750 withholding standard deduction from US-MES5-011, NOT the 15,300/30,600 in this row.'),
 ('income_tax','me.wh.bracket.single.2.ceiling',64850,'US-ME-P5-2-001','2026-01-01','2026-12-31',''),
 ('reporting_instruments','me.report.wh.semiweekly_threshold',18000,'US-ME-P5-2-002','2026-01-01',None,'Look-back 12 months to prior 30 June; semiweekly Wed-Fri -> Wednesday, Sat-Tue -> Friday; electronic payment if combined Maine tax >= 10,000.'),
 ('social_security','me.sui.new_employer.rate.total',2.54,'US-ME-P5-1-001','2026-01-01','2026-12-31','2.23% UI + 0.14% CSSF + 0.17% UPAF (UPAF conflict vs UC-1 0.16%, Q1).'),
 ('social_security','me.sui.employer.rate.combined.range','0.31% - 6.60% (categories 01-20; adjusted UI 0.00%-6.29%)','US-ME-P5-1-001','2026-01-01','2026-12-31',''),
]
CITED = ['US-MES5-019','US-MES5-022','US-MES5-024','US-MES5-026','US-MES5-027','US-MES5-028','US-ME-P5-2-001','US-ME-P5-2-002','US-ME-P5-2-003','US-ME-P5-2-004','US-ME-P5-2-005','US-ME-P5-2-009','US-ME-P5-1-001','US-MEP6-001','US-MEP7-001','US-MEP7-002','US-MER3-002','US-MEP9V-001','US-MEP9L-001','US-MEL-001','US-ME-P5-1-004']
NARR = {
 'social_security': 'No SDI/TDI, transit or other levy [US-MEP9V-001, US-OWN-007]. PFML rate rests on A.3 FAQ + A.1 ceiling (no A.2 table) - G-NUMBER residual flagged at seal attempt 6.',
 'leave': 'PFML benefits from 2026-05-01 (FAQ lead), paid by the State fund; retro deduction of missed employee premiums during leave; health coverage continues [US-MES5-025]. Earned paid leave payout at separation depends on policy (Q8).',
 'termination': 'Separating employees receive the Employment Security Law notice (poster copy) [US-MES5-021]. Deductions from final pay: overcompensation and signed loans/advances [US-MES5-007].',
 'indexation': 'MW CPI-W Northeast; Portland fixed steps then CPI-U; exempt threshold 3,000 x MW; PIT chained CPI ~Sept 15; UI base fixed; UPAF yearly; PFML cap SSA base; garnishment floor follows MW.',
}
SPECIAL = '''- Domestic: UI at 1,000/quarter; no MW exclusion found [US-MES5-020, US-MES5-005].
- Agricultural: poster applies 15.10 to agriculture while 663(3)(A) excludes ag from the subchapter (Q13).
- Minors: hours limits (774); full MW; newspaper delivery under 18 and child for parent UI-excluded [US-MES5-028, US-MES5-020].
- Tipped: cash >= 50% (7.55); Portland half of 16.75 [US-MES5-001, US-MES5-012].
- Clergy: UI-excluded; no withholding rule beyond federal [US-MES5-020].
- Students: co-op/OJT, student nurses/interns UI-excluded; camp counselors MW-subchapter excluded [US-MES5-020, US-MES5-005].
- NRAs: 12-day / 3,000 nonresident threshold applies.
- Government: most public employees OT-exempt; public employers exempt from vacation payout; PFML exemption under 2023 CBAs until expiry [US-MES5-005, US-MES5-007, US-MES5-024].
- Family members dependent on employer: excluded from MW subchapter and 621-A; own child/spouse UI-excluded [US-MES5-005, US-MES5-020].
- Small employers: <= 10 no earned paid leave or vacation payout; < 15 PFML 0.5% [US-MES5-008, US-MES5-007, US-MES5-024].'''
LANG = 'No language requirement; bilingual permitted [US-MEL-001, US-MEP9L-001]. Maine DOES require a pay statement (content, not language) - see US-OWN-006 dated note. Payslip English.'
UNRES = [
 {'key':'me.sui.upaf.rate.conflict','why':'Rate-year 2026 array says UPAF 0.17%; 2026 UC-1 instructions say 0.16%.','close':'An employer 2026 MDOL rate notice or MDOL BUC confirmation of the 2026 UPAF predetermined yield.','blocking':True},
 {'key':'me.exempt.salary.next_year','why':'2027 poster 905.79 vs statute formula 905.77.','close':'MDOL overtime guidance page; safe rule: salary must exceed 3,000 x MW.','blocking':False},
 {'key':'me.minwage.derivation','why':'CPI-W Northeast Aug 2025/Aug 2026 not fetched; 15.10 -> 15.70 not reproduced.','close':'BLS series CWUR0100SA0 values.','blocking':False},
 {'key':'me.local_minwage.other','why':'Other municipal minimum wages (e.g. Rockland) not checked.','close':'Municipal ordinance check or MDOL minimum-wage FAQ.'},
 {'key':'me.payment.paycard_consent','why':'No paycard/direct-deposit consent rule beyond no-fee.','close':'MDOL rule or Bureau of Consumer Credit Protection guidance.','blocking':False},
 {'key':'me.pfml.rate.a2_source','why':'1.0%/0.5% split rests on A.3 FAQ plus A.1 ceiling; no A.2 rate table.','close':'12-702 CMR ch. 1 contributions section or an MDOL 2026 rate notice.'},
 {'key':'me.report.w2.bulk_spec','why':'Maine Tax Portal Bulk File Upload Specifications not fetched (EFW2 acceptance open).','close':'MRS bulk file specifications.'},
 {'key':'me.leave.earned_paid.payout','why':'Payout of earned paid leave at separation is an interpretation via 626.','close':'MDOL rule 12-170 CMR ch. 18 or FAQ.'},
 {'key':'me.pit.obbba_decoupling','why':'Decoupling from federal tips/overtime deductions for 2026 not checked (assessment).','close':'2026 MRS individual instructions or the conformity act.','blocking':False},
 {'key':'me.deductions.authorisation','why':'26 MRSA 629/635 not read.','close':'Statute read.','blocking':False},
 {'key':'me.data_protection.breach_ssn','why':'SSN on pay statements and breach law not read.','close':'10 MRSA 1346-1350-B and 1272-B.','blocking':False},
 {'key':'me.wh.tables.next_year','why':'2027 withholding tables not published.','close':'MRS 27_wh_tab_instr.pdf (December 2026).'},
 {'key':'me.minwage.agricultural_basis','why':'Poster applies 15.10 to agriculture while 663(3)(A) excludes ag workers from the subchapter.','close':'26 MRSA 664 as amended or the MDOL basis for the agricultural rate.'},
]
