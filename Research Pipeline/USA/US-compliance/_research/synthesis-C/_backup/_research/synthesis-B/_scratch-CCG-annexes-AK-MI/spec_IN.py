NAME = 'Indiana'
SUMMARY = 'Minimum wage tracks the FLSA (7.25; state law covers only non-FLSA employers with 2+ employees); local mandates pre-empted; weekly overtime. State PIT 2.95% (2.90% from 2027 per DOR) plus county LIT in all 92 counties (rate by Jan-1 county, chart R47/10-26 from 2026-10-01: Boone 0.0171); WH-4 exemptions 1,000/1,500/3,000; supplemental flat 2.95% + county; 30-day nonresident safe harbor; reciprocity KY/MI/OH/PA/WI (county still withheld). UI employer-only, base 9,500, new 2.5%. Pay-statement duty literally limited to non-FLSA employers. Oracle: DN#1 example 13.96 + 4.73.'
U = 'USD'
D = 'US-INS5-007'
FACTS = [
 ('labour_code','in.minwage.hourly',7.25,'US-INS5-001','2009-07-24',None,{'u':U,'n':'IC 22-2-2-4(c): state minimum = FLSA minimum; state law covers employers with 2+ employees NOT subject to FLSA MW (22-2-2-3).'}),
 ('labour_code','in.minwage.tipped.cash_wage',2.13,'US-INS5-001','2026-01-01',None,{'u':U}),
 ('labour_code','in.local_mandates.preempted',True,'US-INS5-002','2026-01-01',None,{'n':'IC 22-2-2-10.5 (MW) and 22-2-16-3 (benefits/leave); not for a unit\'s own employees.'}),
 ('labour_code','in.overtime.weekly_threshold_hours',40,'US-INS5-001','2026-01-01',None,{'u':'hours','n':'1.5x; no daily OT; hospitals 14-day/80 h with 8 h daily trigger; domestic covered.'}),
 ('labour_code','in.pay_frequency.rule','at least semimonthly, or biweekly on request; pay covers wages up to no more than 10 business days before payday (IC 22-2-5-1)','US-INS5-003','2026-01-01',None,{}),
 ('labour_code','in.payment.method','US money, negotiable check, draft, money order, or electronic transfer to institution designated by employee; paycards not named; DD cannot be forced (75%)','US-INS5-003','2026-01-01',None,{}),
 ('labour_code','in.late_wages.liquidated_damages_multiple',2,'US-INS5-003','2026-01-01',None,{'u':'ratio','n':'22-2-5-2 if not in good faith, plus attorney fees.'}),
 ('income_tax','in.pit.rate',2.95,'US-INS5-009','2026-01-01','2026-12-31',{'u':'percent','n':'IC 6-3-2-1 not read (SPA); DOR rates page.'}),
 ('income_tax','in.pit.rate',2.90,'US-INS5-009','2027-01-01',None,{'u':'percent','c':'medium','n':'DOR: "will adjust in 2027 to 2.90%"; statute not read.'}),
 ('income_tax','in.wh.method','taxable wages = gross per period - deduction constants (annual / 52, 26, 24, 12, 365); x 2.95% state and x county rate; 2-decimal constants and results',D,'2026-10-01',None,{'n':'DN#1 R47/10-26 effective 2026-10-01 supersedes R46/01-26 (US-IN-001, effective_to 2026-09-30).'}),
 ('income_tax','in.wh.exemption.personal',1000,D,'2026-01-01',None,{'u':U,'n':'WH-4 line 5; not indexed.'}),
 ('income_tax','in.wh.exemption.dependent',1500,D,'2026-01-01',None,{'u':U,'n':'Lines 6 and 7 (first-time dependent one year only).'}),
 ('income_tax','in.wh.exemption.adopted_child',3000,D,'2026-01-01',None,{'u':U,'n':'Line 8.'}),
 ('income_tax','in.wh.supplemental.rate',2.95,D,'2026-01-01','2026-12-31',{'u':'percent','n':'Flat state rate plus county rate, no exemptions; Indiana does not follow IRC 3402(n).'}),
 ('income_tax','in.wh.certificate','WH-4 (State Form 48845, R10/8-23): counties of residence and principal employment as of Jan 1; additional state/county lines 9-10; new WH-4 within 10 days when exemptions decrease','US-INS5-021','2023-08-01',None,{}),
 ('local_tax','in.local.lit.county_basis','county of residence on Jan 1 (out-of-state residents: county of principal work on Jan 1), fixed for the year; withheld and reported with state tax on WH-1/WH-3/W-2 RS (T3 piggyback); no separate nonresident rate','US-INS5-008','2026-01-01',None,{}),
 ('local_tax','in.local.lit.rate.boone',0.0171,D,'2026-10-01',None,{'u':'ratio','n':'Was 0.017 to 2026-09-30 (R46).'}),
 ('local_tax','in.local.lit.rate.marion',0.0202,D,'2026-10-01',None,{'u':'ratio'}),
 ('local_tax','in.local.lit.rate.min',0.005,D,'2026-10-01',None,{'u':'ratio','n':'Porter.'}),
 ('local_tax','in.local.lit.rate.max',0.03,D,'2026-10-01',None,{'u':'ratio','n':'Randolph. Full 92-county chart in DN#1 R47/10-26 (builder reads the chart).'}),
 ('local_tax','in.local.lit.change_calendar','ordinance Jan 1-Aug 31 -> effective Oct 1 same year; Sep 1-Oct 31 -> Jan 1 next year; Nov 1-Dec 31 -> Oct 1 next year','US-INS5-008','2026-01-01',None,{}),
 ('non_resident','in.nonres.safe_harbor_days',30,'US-INS5-007','2024-01-01',None,{'u':'days','n':'IC 6-3-2-27.5: no state/county withholding when expected <= 30 days in Indiana; time-and-attendance system or WH-4AFF; catch-up once exceeded.'}),
 ('non_resident','in.reciprocity.states','KY, MI, OH, PA, WI','US-INS5-012','2026-01-01',None,{'n':'WH-47; no state tax, but county tax withheld if principal work county on Jan 1 is in Indiana [US-IN-002, US-INS5-008]. NRAs: one exemption only on WH-4.'}),
 ('social_security','in.sui.wage_base',9500,'US-INS5-014','2011-01-01',None,{'u':U,'c':'medium','n':'Not indexed; no 2026-labelled DWD page; IC 22-4-4-2 not read (80%).'}),
 ('social_security','in.sui.new_employer.rate',2.5,'US-INS5-014','2026-01-01',None,{'u':'percent','c':'medium','n':'First 4 calendar years; construction lesser of 4.0% or construction average (2.50% for 2025); government 1.6% [US-IN-003].'}),
 ('social_security','in.sui.employer.rate.min',0.50,'US-INS5-014','2026-01-01',None,{'u':'percent','c':'medium','vm':'derived arithmetically','n':'9,500 x 0.50% = 47.50 (table check).'}),
 ('social_security','in.sui.employer.rate.max',7.40,'US-INS5-014','2026-01-01',None,{'u':'percent','c':'medium','n':'Good standing; delinquent max 9.40%; penalty rate computed + 2% [US-INS5-015 partial]. 2026 solvency surcharge/schedule not obtained.'}),
 ('social_security','in.sui.employee.rate',0,'US-INS5-014','2026-01-01',None,{'u':'percent'}),
 ('payslip_statute','in.payslip.items','hours worked, wages paid, deductions made, each pay period (IC 22-2-2-8(a))','US-INS5-001','2026-01-01',None,{'c':'medium','n':'Scope: binds employers subject to the chapter = 2+ employees NOT subject to FLSA MW (literal reading 70%); build emits the three items anyway. No e-delivery/retention clause; federal 3-year fallback.'}),
 ('reporting_instruments','in.report.wh.wh1','WH-1 via INTIME (online or upload < 10 MB) or SFTP; annual if monthly average <= 83.33, monthly if <= 1,000 (30 days after month end), early filer above','US-INS5-010','2026-01-01',None,{'c':'medium'}),
 ('reporting_instruments','in.report.annual.wh3','WH-3 + state W-2 due Jan 31; electronic mandatory above 25 statements (IC 6-3-4-16.5); XML (schema IDORWTH2016V1.0 not downloaded) / IRIS XML / EFW2 for existing filers; DOR FAQ "Feb 28" conflicts - use Jan 31','US-INS5-011','2026-01-01',None,{'n':'1220 flat file retired 2027-09 [US-INS5-010].'}),
 ('reporting_instruments','in.report.w2.efile_threshold',25,'US-INS5-011','2026-01-01',None,{'u':'statements'}),
 ('reporting_instruments','in.report.sui.quarterly','DWD E S S/UPLINK due Apr 30, Jul 31, Oct 31, Jan 31; electronic filing (646 IAC 5-2-2) and payment (5-2-17) mandatory; penalty 25 per missing report','US-INS5-014','2019-01-01',None,{}),
 ('reporting_instruments','in.newhire.report_days',20,'US-INS5-016','2024-07-01',None,{'u':'days','n':'in-newhire.com, electronic only since 2024-07-01 (SB 148-2024, 4 extra fields); rehire after 60+ days; penalty 25 / 500.'}),
 ('leave','in.leave.sick.state_mandate.exists',False,'US-INS5-002','2026-01-01',None,{}),
 ('leave','in.leave.military_family.days',10,'US-INS5-006','2026-01-01',None,{'u':'working days','n':'IC 22-2-13: unpaid, 12 months and 1,500 hours.'}),
 ('termination','in.final_pay.rule','discharge: regular payday for the period of separation (22-2-9-2); resignation: next usual payday; employer pays conceded part of disputed amount (22-2-9-3)','US-INS5-005','2026-01-01',None,{'n':'No vacation payout statute (open). No mandatory separation notice; answer DWD SF52984.'}),
 ('deductions_garnishments','in.deductions.wage_assignment','written, signed, revocable, employer-agreed, copy within 10 days, listed purpose (IC 22-2-6-2(b)); uniforms/tools lesser of 2,500/yr or 5% weekly disposable; no PPE charge; loan interest max prime + 4%','US-INS5-004','2026-01-01',None,{}),
 ('deductions_garnishments','in.deductions.overpayment_recovery','2 weeks notice; lesser of 25% of weekly disposable or excess over 30 x federal MW (IC 22-2-6-4)','US-INS5-004','2026-01-01',None,{}),
 ('deductions_garnishments','in.garn.child_support.employer_fee',2.00,'US-INS5-017','2026-01-01',None,{'u':U,'n':'IC 31-16-15: start first period within 14 days after service; remit INSCCU each payday; 50+ employees with >1 order electronic; priority except current taxes; lump sums subject to arrears.'}),
 ('deductions_garnishments','in.garn.creditor.max_percent',25,'US-INS5-017','2026-01-01',None,{'u':'percent','n':'Statute moved to IC 37-2-6-4 (P.L.115-2026; effective date tier-B 2026-07-01) [US-INS5-020].'}),
 ('data_protection','in.breach.ag_penalty_max',150000,'US-INS5-018','2026-01-01',None,{'u':U,'c':'medium','n':'[partial] IC 24-4.9.'}),
 ('live_change','in.live.dn1_r47','DN#1 R47/10-26 in force 2026-10-01 (Boone LIT 0.017 -> 0.0171); level withholding',D,'2026-10-01',None,{}),
 ('oracle','in.oracle.dn1.example.state',13.96,D,'2026-10-01',None,{'u':U,'vm':'derived arithmetically','n':'Weekly 800; constants A5 96.15 + B3 86.54 + B1 28.85 + C2 115.38 = 326.92; taxable 473.08 x 0.0295 = 13.96.'}),
 ('oracle','in.oracle.dn1.example.county',4.73,D,'2026-10-01',None,{'u':U,'vm':'derived arithmetically','n':'473.08 x 0.01 = 4.73.'}),
]
LEGACY = []
CITED = ['US-IN-001','US-IN-002','US-IN-003','US-IN-P5-1-001','US-INR3-001','US-INR3-002','US-INR3-005','US-INR3-006','US-INR3-008','US-INP6-001','US-INP9L-001','US-INP7-001','US-INS5-015','US-INS5-019','US-INS5-020','US-KYR3-003','US-OWN-007']
NARR = {
 'social_security': 'No SDI/TDI/PFML/LTC/transit/workforce levy [US-INR3-002, US-KYR3-003, US-OWN-007]. Coverage: domestic 1,000 cash/quarter; agricultural 20,000/quarter or 10 in 20 weeks; clergy excluded.',
 'benefits_in_kind': 'Federal AGI start; withholding duty follows federal duty [US-INS5-012]. IRC conformity date and HSA/125/transit departures not read (low confidence).',
 'collective_agreements': 'No state prevailing wage since 2015-07-01 (HEA 1019-2015) [US-INR3-005, US-INR3-006].',
 'indexation': 'MW tracks FLSA; SUI base fixed since 2011; PIT statutory step 2.95 -> 2.90; LIT by county ordinance (Jan 1 / Oct 1); WH-4 amounts not indexed.',
 'live_change': 'P.L.104-2026 political-subdivision deferred-retirement assignment; P.L.115-2026 UCCC recodified (garnishment cite IC 37-2-6-4); SEA 1-2025 municipal LIT from 2028 (tier-B detail only, US-INS5-019 MANUAL); 1220 flat file retired 2027-09.',
}
SPECIAL = '''- Domestic: state MW law only via FLSA coverage; 40 h OT applies; agency companionship excluded; UI 1,000 cash/quarter; may opt out of withholding [US-INS5-001, US-INS5-014, US-INS5-012].
- Agricultural: excluded from state MW and pay-frequency chapter; UI 20,000/quarter or 10 in 20 weeks [US-INS5-001, US-INS5-003, US-INS5-014].
- Minors: under 16 excluded from state MW; hours limits only [US-INS5-001].
- Tipped: 2.13 + tip credit [US-INS5-001].
- Clergy: excluded from state MW; ministers may choose no withholding; UI-excluded [US-INS5-001, US-INS5-012, US-INS5-014].
- Students: own-school and student nurses excluded from MW [US-INS5-001, US-INS5-021].
- NRAs: one exemption [US-INS5-021]. Nonresidents: 30-day safe harbor; reciprocity with county still withheld [US-INS5-007].
- Commission-only/outside sales: excluded from MW [US-INS5-001].
- Government: wage-assignment chapter applies; UI 1.6% or reimbursable [US-INS5-004, US-INS5-014].
- Casual laborers / pensioners: may choose no withholding [US-INS5-012].'''
LANG = 'IC 22-2-2-8 has no language clause; bilingual expressly permitted [US-INP6-001, US-INP9L-001]; payslip English (US-OWN-006).'
UNRES = [
 {'key':'in.local.lit.chart.2026_01_to_09','why':'County LIT chart R46/01-26 (Boone 0.017; all other counties as in R47) governed 2026-01-01..2026-09-30 but sits on rows now superseded (US-IN-001, US-IN-P5-1-001, effective_to 2026-09-30); superseded rows cannot carry a number under the brief.','close':'Final merge: accept period facts from rows superseded with an explicit effective_to (or register an S5 historical-period row for R46), then emit the Jan-Sep chart with effective_to 2026-09-30.','blocking':False},
 {'key':'in.payslip.scope','why':'IC 22-2-2-8 binds only employers "subject to this chapter" = non-FLSA employers (22-2-2-3); literal reading excludes most employers.','close':'Owner/builder decision; or IDOL guidance on 22-2-2-8 scope. Recommendation: emit hours, wages, deductions anyway.','blocking':False},
 {'key':'in.sui.rate_year.current','why':'2026 solvency surcharge, applied-rate schedule and a 2026-labelled wage base not obtained (partial row).','close':'DWD state-premium-rate page as currently published, or IC 22-4-4-2 / 22-4-11-3.3 from the 2026 IC PDF (browser pass, US exit).'},
 {'key':'in.pit.rate.next_year.statute','why':'2.90% for 2027 rests on the DOR page alone; IC 6-3-2-1 unread (iga.in.gov SPA).','close':'IC 6-3-2-1 from the 2026 IC Title 6 Article 3 PDF (browser pass).','blocking':False},
 {'key':'in.report.wh.xml_schema','why':'WH-1/WH-3 XML schema IDORWTH2016V1.0 and business rules not downloaded; EFW2 guide labelled 2025 and prior.','close':'Schema files and TY2026 EFW2 guide fetched from a US exit.'},
 {'key':'in.final_pay.accrued_vacation','why':'No payout statute; case law (tier-B lead) treats promised vacation as wages.','close':'IDOL knowledge-base article or Indiana Supreme Court decision on courts.in.gov.'},
 {'key':'in.pit.conformity','why':'IRC conformity date and HSA/125/transit departures not read.','close':'IC 6-3-1-11 (2026) or DOR IT-40 2025 instructions, Add-backs.'},
 {'key':'in.garn.creditor.statute_text','why':'IC 37-2-6-4 text, effective date and any employer fee not read.','close':'IC Title 37 Article 2 (2026) via browser pass.'},
 {'key':'in.leave.other_mandated','why':'Jury duty (IC 34-28-4), voting, volunteer firefighter leave not researched.','close':'Those IC sections.','blocking':False},
]
