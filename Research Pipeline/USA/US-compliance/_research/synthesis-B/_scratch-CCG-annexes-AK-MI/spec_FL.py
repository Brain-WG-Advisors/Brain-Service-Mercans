NAME = 'Florida'
SUMMARY = 'T1: no state or local wage tax. Payroll obligations: constitutional minimum wage (14.00 to 2026-09-29, 15.00 from 2026-09-30, first CPI-W indexation effective 2028-01-01), tipped cash wage (credit capped at 3.02), employer-only reemployment tax (base 7,000; 0.1%-5.4%; new 2.7%; RT-6 with fixed-length or XML upload), new-hire reporting including non-employees paid 600+, E-Verify certification, and garnishment/child-support rules. No general pay-statement statute (labor pools only); local wage/leave mandates pre-empted.'
U = 'USD'
F1 = 'US-FLS5-001'
FACTS = [
 ('labour_code','fl.minwage.hourly',14.00,F1,'2025-09-30','2026-09-29',{'u':U,'n':'Fla. Const. Art. X s.24(c). Fla. Stat. 448.110 still prints 6.15 (stale; overridden), but controls coverage (FLSA-covered only).'}),
 ('labour_code','fl.minwage.hourly',15.00,F1,'2026-09-30','2027-12-31',{'u':U,'n':'Steps 10.00 (2021) -> 15.00; first CPI-W adjustment calculated 2027-09-30, effective 2028-01-01: no change in 2027.'}),
 ('labour_code','fl.minwage.tip_credit.max',3.02,F1,'2021-09-30',None,{'u':U,'vm':'derived arithmetically','n':'Capped at the 2003 FLSA tip credit: 5.15 - 2.13 = 3.02 (federal inputs, FED unit).'}),
 ('labour_code','fl.minwage.tipped.cash_wage',10.98,F1,'2025-09-30','2026-09-29',{'u':U,'vm':'derived arithmetically','n':'14.00 - 3.02.'}),
 ('labour_code','fl.minwage.tipped.cash_wage',11.98,F1,'2026-09-30','2027-12-31',{'u':U,'vm':'derived arithmetically','n':'15.00 - 3.02; poster confirmation open (low risk).'}),
 ('labour_code','fl.minwage.pre_suit_notice_days',15,'US-FLS5-002','2026-01-01',None,{'u':'days','n':'448.110; DOR/FloridaCommerce post new rate by 15 Oct, mailed notice by 15 Nov.'}),
 ('labour_code','fl.local_mandates.preempted',True,'US-FLS5-009','2024-07-01',None,{'n':'218.077(2) (ch. 2024-80): no local minimum wage or employment-benefit mandates (sick leave, vacation, holidays) or contractor-wage control; exceptions own employees and direct subsidy recipients.'}),
 ('labour_code','fl.manual_labor.legal_day_hours',10,'US-FLS5-027','2026-01-01',None,{'u':'hours','n':'448.01: extra pay beyond 10 h/day absent written contract; no premium rate fixed. Otherwise FLSA only.'}),
 ('labour_code','fl.everify.employer_threshold',25,'US-FLS5-010','2023-07-01',None,{'u':'employees','n':'448.095: private employers 25+ and all public agencies must use E-Verify within 3 business days; certify on first RT return each year or RT-E Verify [US-FLS5-019].'}),
 ('income_tax','fl.pit.exists',False,'US-FL-001','2026-01-01',None,{}),
 ('social_security','fl.sui.wage_base',7000,'US-FLS5-003','2015-01-01',None,{'u':U,'vm':'second independent authority','n':'Fixed in statute; successor may count predecessor wages; out-of-state wages credited via RT-6NF [US-FLS5-020, US-FLS5-018].'}),
 ('social_security','fl.sui.employer.rate.min',0.1,'US-FLS5-018','2026-01-01','2026-12-31',{'u':'percent','n':'= 7 per employee.'}),
 ('social_security','fl.sui.employer.rate.max',5.4,'US-FLS5-018','2026-01-01','2026-12-31',{'u':'percent','n':'= 378 per employee; +1 point for short-time-compensation employers.'}),
 ('social_security','fl.sui.new_employer.rate',2.7,'US-FLS5-004','2026-01-01',None,{'u':'percent','n':'While chargeable < 8 quarters (statute); DOR: until reported 10 quarters.'}),
 ('social_security','fl.sui.rounding','contribution fraction under half a cent dropped; half a cent or more rounds up to 1 cent','US-FLS5-004','2026-01-01',None,{}),
 ('social_security','fl.sui.employee.rate',0,'US-FLS5-004','2026-01-01',None,{'u':'percent','n':'443.131(1): may not be deducted from wages.'}),
 ('social_security','fl.sui.liability_threshold.quarterly_wages',1500,'US-FLS5-020','2026-01-01',None,{'u':U,'c':'medium','n':'Or 1 employee in 20 weeks or FUTA liability; domestic 1,000 in a quarter.'}),
 ('payslip_statute','fl.payslip.general_statute.exists',False,'US-FLL-002','2026-01-01',None,{'n':'Only labor pools: itemised deductions at each payment (electronic on request) and annual earnings summary by 1 February (448.24(2)(g),(h)).'}),
 ('reporting_instruments','fl.report.sui.rt6','RT-6 (R. 07/23) due 30 Apr, 31 Jul, 31 Oct, 31 Jan (next business day); zero report required; e-payment by 5 pm ET business day before; lines 1 covered employees (12th), 2 gross, 3 excess over 7,000, 4 taxable, 5 tax; wage detail name/SSN/gross/taxable; corrections RT-8A','US-FLS5-021','2023-07-01',None,{}),
 ('reporting_instruments','fl.report.sui.efile_threshold_employees',10,'US-FLS5-006','2026-01-01',None,{'u':'employees','n':'10+ employees in any quarter of prior state fiscal year must e-file/e-pay; non-electronic report 25 + 1/employee max 300; erroneous report greater of 50 or 10% max 300 [US-FLS5-024]; ITIN not accepted.'}),
 ('reporting_instruments','fl.report.sui.flat_file','Flat File Web Import v7 (Dec 2023): fixed-length records 00 Header, 01 Employer, 02 Employee, 03 Totals, 99 Trailer; 2 implied decimals; zip refused','US-FLS5-022','2023-12-01',None,{}),
 ('reporting_instruments','fl.report.sui.xml','FL_RT_XML_Schemas_v2026 1.0: 9 XSD in IRS efile envelope; required above 20,000 employee records; RT-6 sample validates (lxml)','US-FLS5-023','2026-01-01',None,{}),
 ('reporting_instruments','fl.report.sui.xml_required_records',20000,'US-FLS5-023','2026-01-01',None,{'u':'records'}),
 ('reporting_instruments','fl.newhire.report_days',20,'US-FLS5-008','2026-01-01',None,{'u':'days','n':'409.2576; DOB optional; also NON-EMPLOYEES paid 600+ in a year within 20 days (DD/RSPEC scope item).'}),
 ('reporting_instruments','fl.newhire.nonemployee_threshold',600,'US-FLS5-008','2026-01-01',None,{'u':U}),
 ('leave','fl.leave.sick.state_statute.exists',False,'US-FLS5-009','2024-07-01',None,{'n':'None at state level; local mandates pre-empted.'}),
 ('leave','fl.leave.domestic_violence.days',3,'US-FLS5-014','2026-01-01',None,{'u':'working days','n':'Employers 50+, employees 3+ months; up to 3 working days per 12 months, paid or unpaid at employer choice.'}),
 ('termination','fl.final_pay.state_statute.exists',False,'US-FLS5-016','2026-01-01',None,{'c':'medium','n':'No final-pay timing or vacation payout statute; prevailing party fees in wage action (448.08).'}),
 ('benefits_in_kind','fl.sui.wages.taxable_items','personal-use cars, non-convenience meals and lodging, group legal, golden parachutes, excess discounts, below-market loan interest, reported tips','US-FLS5-003','2026-01-01',None,{'n':'443.1217(2)(b)-(g); excluded: sickness/accident/medical/death plan payments, employer-paid employee FICA, convenience meals/lodging, 401(a)/403(a)/SEP/403(b) non-salary-reduction/3121(v)(3). 401(k) deferral treatment open.'}),
 ('deductions_garnishments','fl.garn.head_of_family.weekly_exempt',750,'US-FLS5-012','2026-01-01',None,{'u':U,'n':'222.11: head of family disposable earnings up to 750/week fully exempt; above only with separate written waiver up to CCPA; others CCPA. Not indexed.'}),
 ('deductions_garnishments','fl.garn.child_support.employer_fee.first',5,'US-FLS5-013','2026-01-01',None,{'u':U,'n':'61.1301: 5 first deduction, 2 each after; start first pay date > 14 days after service; remit within 2 days after pay date; arrears +20%; termination notice penalty 250/500.'}),
 ('deductions_garnishments','fl.garn.child_support.employer_fee.subsequent',2,'US-FLS5-013','2026-01-01',None,{'u':U}),
 ('deductions_garnishments','fl.garn.child_support.remit_days',2,'US-FLS5-013','2026-01-01',None,{'u':'days'}),
 ('data_protection','fl.breach.notice_days',30,'US-FLS5-017','2026-01-01',None,{'u':'days','n':'501.171: notice to Dept. of Legal Affairs for 500+ Floridians within 30 days (+15 for good cause). Amended by ch. 2026-52 s.9 (substance not read).'}),
 ('live_change','fl.live.minwage_2026_09_30','minimum wage 15.00 and tipped 11.98 from 2026-09-30, in force',F1,'2026-09-30',None,{}),
]
LEGACY = [
 ('social_security','fl.sdi_pfml.exists',False,'US-FLP52-001','2026-01-01',None,'Title XXXI has no SDI/TDI/PFML chapter; no state WARN. Workers comp employer-funded, employee contribution void (440.21) [US-FLP52-002].'),
 ('collective_agreements','fl.prevailing_wage.state_law.exists',False,'US-FLP52-003','2026-01-01',None,'Ch. 255 scanned in full; local procurement wage control barred (218.077(2)(b)-(c)).'),
]
CITED = ['US-FL-002','US-FLL-001','US-FLL-003','US-FLS5-005','US-FLS5-007','US-FLS5-011','US-FLS5-015','US-FLS5-019','US-FLS5-025','US-FLS5-026','US-FL-005','US-FLP52-002','US-FLP52-004']
NARR = {
 'income_tax': 'No state income tax on natural persons (Fla. Const. Art. VII s.5(a)) [US-FL-001]; DOR tax list has no personal income or withholding tax [US-FL-002, US-FLL-003]. Not applicable: state withholding method, W-4, supplemental, rounding, state W-2, reciprocity, resident/nonresident. Florida residents working elsewhere follow the work state (MULTI).',
 'local_tax': 'None [US-FLL-003].',
 'reporting_instruments': 'Other: BLS-3020 multiple worksite; RT-6EW; RT-6NF; RT-7 annual for domestic-only employers (due 1 Jan, late after 31 Jan). Registration DR-1 online. DR-835 POA / RTS-9 agent [US-FL-005].',
 'oracle': 'No withholding oracle (no wage tax). UI: Line 4 x rate with half-cent rounding; RT-800002 p.9 worked examples (successor wages; NY to FL transfer) and the 4 RT XML test cases [US-FLS5-020, US-FLS5-023].',
 'indexation': 'MW fixed steps to 15.00 (2026-09-30); CPI-W from 2028-01-01; UI base not indexed; UI rates yearly (RT-20); garnishment 750 not indexed.',
}
SPECIAL = '''- Domestic: UI at 1,000 cash/quarter; RT-7 annual option; minor hours limits not applicable; casual private-residence labor not "employee" for E-Verify [US-FLS5-005, US-FLS5-004].
- Agricultural: UI at 10,000 cash/quarter or 5+ workers in 20 weeks; crew-leader rules [US-FLS5-005].
- Minors: 450.081 hours (15 and under 3 h school days/15 h week; 16-17 8 h/30 h in session); no subminimum; newspaper delivery under 18 UI-exempt [US-FLS5-011, US-FLS5-005].
- Tipped: credit 3.02; 11.98 from 2026-09-30; reported tips are UI wages [US-FLS5-001, US-FLS5-020, US-FLS5-021].
- Clergy: churches/ministers UI-exempt; other 501(c)(3) covered at 4+ in 20 weeks [US-FLS5-005, US-FLS5-020].
- Students: own-school, co-op, student nurses/interns, F/J purpose-related work UI-exempt [US-FLS5-005, US-FLS5-020, US-FLS5-025].
- NRAs: no PIT; UI taxable except F/J; ITIN invalid on RT-6 [US-FLS5-025, US-FLS5-024].
- Statutory employees: agent/commission drivers and traveling salespersons UI-covered; commission insurance/real-estate (and barbers) exempt [US-FLS5-005, US-FLS5-020].
- Government: UI covers public employers with exceptions; E-Verify mandatory; own-employee wage autonomy [US-FLS5-005, US-FLS5-010, US-FLS5-009].
- Corporate officers covered; family employment exempt except in corporations [US-FLS5-005, US-FLS5-020].
- Labor pools: 448.24 itemised statement and annual summary [US-FLL-002].'''
LANG = 'Minimum-wage poster in English and Spanish (448.109(3)(a)) [US-FLL-001]; RT-83 poster with Spanish version RT-83SP [US-FLS5-026]; payslip English (US-OWN-006). FL postings page unreadable (recorded limit).'
UNRES = [
 {'key':'fl.sui.wages.401k_deferral','why':'443.1217(2)(f) excludes payments to a 401(a) trust and carves out salary reduction only for 403(b); ambiguous against FUTA 3306(r); DOR guide silent.','close':'A DOR TIP or an answer from DOR e-vendor / Reemployment Tax FAQ.','blocking':True},
 {'key':'fl.termination.separation_notice','why':'443.151(1) defers to rules; whether a FloridaCommerce rule requires a separation form was not read.','close':'Rule chapters 73B-10/73B-11 F.A.C. on flrules.org.'},
 {'key':'fl.live.ch_2026_52','why':'501.171 was amended by ch. 2026-52 s.9; substance not read.','close':'Laws of Florida ch. 2026-52 on laws.flrules.org.','blocking':False},
 {'key':'fl.minwage.tipped.poster_confirmation','why':'11.98 is derived from A.1 but not confirmed on the FloridaCommerce 2026 poster (access gap).','close':'FloridaCommerce 2026 minimum wage poster.','blocking':False},
 {'key':'fl.report.sui.xml_changes_2026','why':'RT_changes.xlsx inside the RT XML package not read.','close':'Read RT_changes.xlsx in FL_DOR_flRtXmlPkg_2026-11-02.zip (Stage 3 / RSPEC).','blocking':False},
 {'key':'fl.live.bulletin_sweep','why':'Full sweep of Laws of Florida 2026 and DOR TIPs 2026 not run within budget.','close':'Laws of Florida 2026 index and DOR Tax Information Publications 2026 (browser pass).'},
]
