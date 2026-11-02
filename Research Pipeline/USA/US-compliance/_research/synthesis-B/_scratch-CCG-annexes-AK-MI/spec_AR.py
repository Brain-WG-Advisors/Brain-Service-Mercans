NAME = 'Arkansas'
SUMMARY = 'State minimum wage 11.00 (employers with 4+ employees), weekly overtime only. State withholding on the DFA Formula Method 2026 (standard deduction 2,470, personal credit 29 per AR4EC exemption, top rate 3.7% from 2026-01-01 after Act 1 of 2026 1st Ex. Sess.) plus separate low-income tables. No local income tax, no reciprocity (Texarkana exemption). SUI base 7,000, new employer 2.0%, no employee UI, no SDI/PFML. No pay-statement statute; no paid sick leave statute. Several key employer-guide figures sit on legacy-id rows (US-ARP51-002 etc.) and are listed as non-fact lines pending re-key.'
U = 'USD'
F = 'US-ARS5-001'
FACTS = [
 ('labour_code','ar.minwage.hourly',11.00,'US-ARS5-002','2021-01-01',None,{'u':U,'n':'2018 Initiated Act (Issue 5); employers with 4+ employees; higher of state/FLSA. No 2027 increase enacted; 2026-11-03 ballot carries no initiative [US-ARS5-004].'}),
 ('labour_code','ar.minwage.employer_size_min',4,'US-ARS5-002','2021-01-01',None,{'u':'employees'}),
 ('labour_code','ar.minwage.tipped.cash_wage',2.63,'US-ARS5-002','2021-01-01',None,{'u':U,'c':'medium','n':'Tip credit up to minimum wage; written notice each time the tip-credit amount changes (11 CAR 11).'}),
 ('labour_code','ar.overtime.weekly_threshold_hours',40,'US-ARS5-002','2026-01-01',None,{'u':'hours','n':'1.5x over 40/week (11-4-211); no daily OT; agricultural and FLSA-exempt excluded.'}),
 ('labour_code','ar.paycard.free_withdrawals_per_load',1,'US-ARS5-003','2019-07-24',None,{'u':'count','n':'11-4-403(f) (Act 853 of 2019): direct deposit or preloaded card lawful; no employee-consent clause in the text.'}),
 ('income_tax','ar.wh.method','DFA Formula Method 2026: annualise; less standard deduction; band midpoint (USD 50) below 100,001; bracket formula; round annual tax to dollar; less 29 per exemption; divide by periods',F,'2026-01-01',None,{}),
 ('income_tax','ar.wh.std_deduction',2470,F,'2026-01-01',None,{'u':U}),
 ('income_tax','ar.wh.personal_credit.per_exemption',29.00,F,'2026-01-01',None,{'u':U}),
 ('income_tax','ar.pit.bracket.1.ceiling',5599,F,'2026-01-01',None,{'u':U,'n':'0% band.'}),
 ('income_tax','ar.pit.bracket.2.ceiling',11199,F,'2026-01-01',None,{'u':U,'n':'2% - 111.98'}),
 ('income_tax','ar.pit.bracket.2.rate',2,F,'2026-01-01',None,{'u':'percent'}),
 ('income_tax','ar.pit.bracket.2.subtract',111.98,F,'2026-01-01',None,{'u':U}),
 ('income_tax','ar.pit.bracket.3.ceiling',15999,F,'2026-01-01',None,{'u':U}),
 ('income_tax','ar.pit.bracket.3.rate',3,F,'2026-01-01',None,{'u':'percent'}),
 ('income_tax','ar.pit.bracket.3.subtract',223.97,F,'2026-01-01',None,{'u':U}),
 ('income_tax','ar.pit.bracket.4.ceiling',26399,F,'2026-01-01',None,{'u':U}),
 ('income_tax','ar.pit.bracket.4.rate',3.4,F,'2026-01-01',None,{'u':'percent'}),
 ('income_tax','ar.pit.bracket.4.subtract',287.97,F,'2026-01-01',None,{'u':U}),
 ('income_tax','ar.pit.bracket.5.ceiling',94700,F,'2026-01-01',None,{'u':U}),
 ('income_tax','ar.pit.bracket.5.rate',3.7,F,'2026-01-01',None,{'u':'percent','n':'94,701-97,600: 3.7% with stepped adjustments 369.90 down to 89.90; 97,601+: 3.7% - 79.90.'}),
 ('income_tax','ar.pit.bracket.5.subtract',367.16,F,'2026-01-01',None,{'u':U}),
 ('income_tax','ar.pit.bracket.top.subtract',79.90,F,'2026-01-01',None,{'u':U}),
 ('income_tax','ar.pit.top_rate',3.7,'US-ARS5-013','2026-01-01',None,{'u':'percent','n':'Act 1 of 2026 1st Ex. Sess. (HB 1001 = SB 1), signed week of 2026-05-04, retroactive to 2026-01-01; operating level assessment for all 2026 and withholding via the reissued formula. Table switch date open (AR-OQ-1). Corporate 4.1% from 2027.'}),
 ('income_tax','ar.wh.low_income_tables.single_weekly_zero_to',281.60,'US-ARS5-011','2026-01-01',None,{'u':U,'n':'Separate table-only method for AR4EC line 5; 281.60x52 = 14,643.20 consistent with the AR4ECSP ceiling.'}),
 ('income_tax','ar.wh.certificate.form','AR4EC (R 12/04/2025); federal W-4 not used; no certificate = zero exemptions; decrease reported within 10 days','US-ARS5-009','2025-12-04',None,{}),
 ('income_tax','ar.wh.exemption_certificate.ar4ecsp.ceiling.single',14643,'US-ARS5-010','2026-01-01',None,{'u':U,'n':'AR4ECSP 2026 ceilings 14,643 / 24,695 / 29,722 / 20,820 / 24,818 (statuses per form).'}),
 ('non_resident','ar.nonres.sourcing','physical presence: work performed in AR when physically located in AR (convenience rule ended for tax years from 2021); apportion by AR working days / total working days','US-ARS5-006','2021-01-01',None,{'n':'Act 1019 of 2021, 26-51-202(c), 504(a)(1), 902(5); level assessment and withholding. No day/dollar threshold (HB1116 of 2025 died).'}),
 ('local_tax','ar.local_wage_tax.exists',False,'US-ARP9V-003','2026-01-01',None,{}),
 ('social_security','ar.sui.wage_base',7000,'US-ARP9V-001','2026-01-01',None,{'u':U,'n':'11-10-215; credit for wages paid toward the former state base when an employee permanently moves with the same employer.'}),
 ('social_security','ar.sui.new_employer.rate',2.0,'US-ARP9V-002','2026-01-01','2026-12-31',{'u':'percent'}),
 ('social_security','ar.sui.employer.rate.min',0.2,'US-ARP9V-002','2026-01-01','2026-12-31',{'u':'percent','n':'0.2-5.1% experienced; deficit 6.1/8.1/10.1%; includes 0.1% Administrative Assessment; conditional 0.2% advance interest and 0.1% extended benefit.'}),
 ('social_security','ar.sui.employer.rate.max',5.1,'US-ARP9V-002','2026-01-01','2026-12-31',{'u':'percent'}),
 ('social_security','ar.sui.admin_assessment.rate',0.1,'US-ARP9V-002','2026-01-01','2026-12-31',{'u':'percent'}),
 ('social_security','ar.sui.employee.rate',0,'US-ARP9V-001','2026-01-01',None,{'u':'percent','c':'medium'}),
 ('social_security','ar.sui.wages.section125_excluded',True,'US-ARP9V-001','2026-01-01',None,{'c':'medium'}),
 ('reporting_instruments','ar.report.sui.quarterly','Tax21 online or paper DWS-ARK-209B/209BR/209BS; due 30 Apr, 31 Jul, 31 Oct, 31 Jan, also when no wages','US-ARP9V-001','2026-01-01',None,{}),
 ('reporting_instruments','ar.report.sui.efile_threshold_employees',250,'US-ARP9V-001','2026-01-01',None,{'u':'employees'}),
 ('reporting_instruments','ar.newhire.report_days',20,'US-ARP9V-001','2026-01-01',None,{'u':'days','n':'Via Tax21; all employees living or working in AR.'}),
 ('reporting_instruments','ar.child_support.verification_response_days',30,'US-ARS5-008','2026-01-01',None,{'u':'days'}),
 ('termination','ar.final_pay.discharge','next regular payday; double wages if unpaid within 7 days of that payday','US-ARS5-003','2019-07-24',None,{'n':'11-4-405 (Act 853 of 2019). Resignation deadline not located (AR-OQ-2). Vacation payout only if policy promises it [US-ARS5-014].'}),
 ('termination','ar.final_pay.double_wages_after_days',7,'US-ARS5-003','2019-07-24',None,{'u':'days'}),
 ('deductions_garnishments','ar.deductions.nonstandard_below_minwage',False,'US-ARS5-002','2026-01-01',None,{'n':'Breakage/shortages/fines may not reduce pay below minimum wage; court orders, assignments, board/lodging/apparel may.'}),
 ('deductions_garnishments','ar.garn.child_support.arrears_addon.percent',10,'US-ARS5-007','2026-01-01',None,{'u':'percent','c':'medium','n':'Usually 10% of current support toward arrears, now 20% in some cases (act unnamed, AR-OQ-4); CCPA cap; Arkansas Child Support Clearinghouse; OCSE MyWorkers [US-ARS5-008].'}),
 ('data_protection','ar.records.wage_hour.retention_years',3,'US-ARL-001','2026-01-01',None,{'u':'years','n':'11-4-217.'}),
 ('live_change','ar.live.act1_2026_ex_sess.status','in force retroactive 2026-01-01 (signed week of 2026-05-04); level assessment + withholding','US-ARS5-005','2026-01-01',None,{'c':'medium'}),
 ('oracle','ar.oracle.example.1.input','monthly 2,127.00, 2 exemptions (Formula Method 2026)',F,'2026-01-01',None,{}),
 ('oracle','ar.oracle.example.1.withholding',36.50,F,'2026-01-01',None,{'u':U,'vm':'derived arithmetically','n':'Reproduced in Python: 25,524 - 2,470 = 23,054 -> midpoint 23,050 x 3.4% - 287.97 = 495.73 -> 496 - 58 = 438 / 12 = 36.50.'}),
]
LEGACY = [
 ('income_tax','ar.wh.supplemental.rate',3.7,'US-ARP51-002','2026-01-01',None,'Bonus/commission with regular wages; vacation pay in addition to regular pay treated as supplemental.'),
 ('income_tax','ar.wh.texarkana.exemption','Texarkana AR residents exempt on all income; Texarkana TX residents exempt on wages earned in Texarkana AR (26-52-604); AR-TX-4EC; AR-3Q-TEX due 28 Feb','US-ARP51-002','2026-01-01',None,''),
 ('labour_code','ar.pay_frequency.rule','corporations pay semimonthly; corporations with gross income >= 500,000 may pay FLSA-exempt managers earning > 25,000 at least monthly (11-4-401)','US-ARP51-004','2026-01-01',None,'2008 compilation; later amendment not checked.'),
 ('reporting_instruments','ar.report.wh.monthly','AR941M by the 15th of following month (zero voucher if nil); annual AR941A by 31 Jan when deposits under 1,000; EFT mandatory at average 20,000+/month; AR3MAR due 28 Feb','US-ARP51-002','2026-01-01',None,''),
 ('reporting_instruments','ar.report.w2.efile_threshold_employees',125,'US-ARP51-002','2026-01-01',None,'EFW2 via ATAP; RA, RE, RW, RS, RT, RF, RCS required; RV not allowed.'),
 ('data_protection','ar.records.withholding.retention_years',6,'US-ARP51-002','2026-01-01',None,'Including AR4EC copies.'),
 ('payslip_statute','ar.payslip.state_statute.exists',False,'US-ARP52-006','2026-07-21',None,'11 CAR 11 compilation 2026-07-21; tip-credit change notice in writing.'),
 ('collective_agreements','ar.prevailing_wage.state_law.exists',False,'US-ARP51-001','2017-01-01',None,'Repealed 2017; Davis-Bacon only.'),
]
CITED = ['US-ARS5-012','US-ARS5-014','US-ARP9L-001','US-ARP52-002','US-ARP52-001']
NARR = {
 'non_resident': 'No reciprocity (no statutory authority). Rail/motor carriers withhold only for AR residents and nonresidents with all duties in AR; air carriers where 50%+ of scheduled flight time in AR [US-ARP51-002]. Pass-through entity withholding (3.7% / 4.3%) is outside payroll.',
 'social_security': 'No SDI/TDI/PFML/LTC/transit programme: absence settled at mandate level (US-OWN-007 levy census, AR admin assessment 0.1% the only levy [US-ARP9V-001]); the per-state PFML row US-ARP52-007 is tier-B MANUAL and is not relied on. UI coverage: domestic 1,000 cash/quarter; agricultural 20,000/quarter or 10 workers in 20 weeks; exclusions: family employment, commission-only insurance/real-estate agents, students at own school, student nurses [US-ARP9V-001].',
 'leave': 'No paid sick leave statute (absence finding, medium) [US-ARS5-002, US-ARP9L-001, US-ARS5-004]; no PFML. Vacation entitlement by written policy [US-ARS5-014]. Jury/voting/military leave not researched (AR-OQ-5).',
 'benefits_in_kind': 'Excluded IRC 112, 125, 219, 401(k), 403(b), 408(k), 408(p), 457; non-cash wages at FMV; tips of 20+/month are wages [US-ARP51-002 legacy]. HSA outside 125, transit, GTL open (AR-OQ-3).',
 'deductions_garnishments': 'Creditor exemption 16-66-208 (first 25/week) rests only on tier-B MANUAL row US-ARS5-012 — not a fact; CCPA limits apply until replaced (AR-OQ-8).',
 'indexation': 'Minimum wage not indexed; SUI base fixed; withholding amounts republished yearly by legislation, no index factor.',
}
SPECIAL = '''- Domestic: exempt from AR withholding; UI at 1,000 cash/quarter [US-ARP51-002 legacy; US-ARP9V-001].
- Agricultural: withholding required with 4+ agricultural employees in a period; no state OT; UI 20,000/quarter or 10 in 20 weeks [US-ARP51-002, US-ARP51-004 legacy; US-ARP9V-001].
- Tipped: cash wage 2.63; written tip-credit notice; tips 20+/month withheld [US-ARS5-002; US-ARP52-006].
- Clergy: ministers exempt from AR withholding [US-ARP51-002].
- Students: 85% of minimum wage with DOLL certificate (11-4-210(b)); UI excludes students at own school [US-ARP51-004; US-ARP9V-001].
- NRAs: no AR rule beyond federal. Commission agents UI-excluded.
- Government/nonprofit: covered by withholding; UI reimbursable option [US-ARP9V-001].
- Military: active-duty pay 100% exempt (Act 1408 of 2013); spouses ARW-4MS yearly [US-ARP51-002].
- Texarkana residents: see income tax. Employers with fewer than 4 employees: outside AR MW Act [US-ARS5-002].
- Minors: not researched (AR-OQ-5).'''
LANG = 'No language rule for pay records; posters [US-ARP9L-001]; payslip/filings en per US-OWN-006.'
UNRES = [
 {'key':'ar.wh.formula.switch_date','why':'DFA documents read do not state the date employers had to switch to the 3.7% formula/tables in 2026 or whether a catch-up was required; only a tier-B lead says 2026-05-29.','close':'DFA withholding release/notice of May 2026, or the text of Act 1 of 2026 (1st Ex. Sess.).','blocking':True},
 {'key':'ar.final_pay.resignation','why':'No statutory deadline for final pay on resignation located; current text of 11-4-405 not confirmed for a resignation clause.','close':'Current Ark. Code 11-4-405 text (LexisNexis public portal or arkleg Act history).'},
 {'key':'ar.pit.wages.hsa_transit_gtl','why':'Employer HSA outside 125, IRC 132(f) transit and IRC 79 GTL not in the employer guide exclusion list.','close':'DFA Rule 2.26-51 conformity list or the AR IRC-conformity act (26-51-404).'},
 {'key':'ar.garn.iwo.employer_fee','why':'Employer child-support fee only on a tier-B lead (2.50 per pay period, 9-14-218); the act raising arrears add-on to 20% is unnamed.','close':'OCSE MyWorkers employer guide (Chrome pass) or Ark. Code 9-14-218 / 9-14-226.'},
 {'key':'ar.leave.mandated_leave','why':'Jury, voting, military, crime-victim leave and child-labour hour limits not researched this run.','close':'DOLL child-labour page and Ark. Code 16-31-106 and 7-1-102 (official text).'},
 {'key':'ar.data_protection.ssn_paystub','why':'No AR rule on SSN on pay statements located; absence not verified.','close':'Official text of Ark. Code 4-86-107.'},
 {'key':'ar.live.bulletin_sweep','why':'2025 Regular and 2026 Fiscal Session acts not swept (arkleg TLS failure).','close':'arkleg Acts index via the orchestrator browser pass.'},
 {'key':'ar.garn.creditor.exempt_weekly','why':'16-66-208 creditor exemption (first 25/week of net wages of laborers and mechanics) rests only on tier-B MANUAL row US-ARS5-012.','close':'Official Ark. Code 16-66-208 text.'},
]
