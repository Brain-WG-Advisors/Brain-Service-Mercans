NAME = 'Kansas'
SUMMARY = 'Minimum wage 7.25 (state law only for non-FLSA employers; OT after 46 h for them); local mandates pre-empted. Withholding: KW-100 tables in force since 2024-07-01, two rates 5.2% / 5.58%; SB 269 rate-cut trigger NOT met for 2026 or 2027; K-4 allowances 9,160 / 18,320 / 2,320; supplemental 5%; no reciprocity, no local tax. UI employer-only, base 15,100 (25% of SAAW, indexed from 2026), Schedule C 0%-6.95%, new 1.75% (construction 5.55%). No routine pay statement (deductions statement on request). New hire within 20 business days.'
U = 'USD'
K = 'US-KSS5-001'
FACTS = [
 ('labour_code','ks.minwage.hourly',7.25,'US-KSS5-008','2010-01-01',None,{'u':U,'n':'K.S.A. 44-1203; not for FLSA-covered employers/employees; not indexed; SB 471 (16/h) died [US-KSS5-027].'}),
 ('labour_code','ks.minwage.tipped.cash_wage',2.13,'US-KSS5-008','2010-01-01',None,{'u':U}),
 ('labour_code','ks.local_mandates.preempted',True,'US-KSS5-012','2026-01-01',None,{'n':'K.S.A. 12-16,130: wages, leave, benefits, scheduling.'}),
 ('labour_code','ks.overtime.non_flsa.weekly_threshold_hours',46,'US-KSS5-010','2026-01-01',None,{'u':'hours','n':'44-1204: only employees not covered by FLSA s.7; EMS/fire/police 258 h per 28 days. FLSA 40 h governs most employers.'}),
 ('labour_code','ks.pay_frequency.rule','at least once per calendar month on designated paydays; period ends no more than 15 days before payday (44-314)','US-KSS5-013','2026-01-01',None,{}),
 ('labour_code','ks.payment.method','cash, check, EFT to designated account, or payroll card (one free withdrawal up to net pay per period, no fees); EFT-only employers offer default alternative; forum/education 30 days before EFT-only or card-only programme','US-KSS5-013','2026-01-01',None,{}),
 ('income_tax','ks.pit.bracket.single.1.ceiling',23000,'US-KSS5-004','2024-01-01',None,{'u':U,'n':'K.S.A. 79-32,110: single/HoH/MFS 5.2% to 23,000 then 1,196 + 5.58%; MFJ 5.2% to 46,000 then 2,392 + 5.58%.'}),
 ('income_tax','ks.pit.bracket.mfj.1.ceiling',46000,'US-KSS5-004','2024-01-01',None,{'u':U}),
 ('income_tax','ks.pit.bracket.1.rate',5.2,'US-KSS5-004','2024-01-01',None,{'u':'percent'}),
 ('income_tax','ks.pit.bracket.2.rate',5.58,'US-KSS5-004','2024-01-01',None,{'u':'percent'}),
 ('income_tax','ks.pit.std_deduction.single',3605,'US-KSS5-005','2024-01-01',None,{'u':U,'n':'Married 8,240, HoH 6,180; fixed, not indexed.'}),
 ('income_tax','ks.pit.std_deduction.married',8240,'US-KSS5-005','2024-01-01',None,{'u':U}),
 ('income_tax','ks.pit.exemption.single',9160,'US-KSS5-006','2025-01-01',None,{'u':U,'n':'79-32,121: 18,320 MFJ; 2,320 per dependent.'}),
 ('income_tax','ks.pit.exemption.mfj',18320,'US-KSS5-006','2025-01-01',None,{'u':U}),
 ('income_tax','ks.pit.exemption.dependent',2320,'US-KSS5-006','2025-01-01',None,{'u':U}),
 ('income_tax','ks.wh.method','KW-100 (wages paid on and after 2024-07-01): gross - allowance for period (annual 9,160 Single / 18,320 Joint / 2,320 per dependent; HoH + one extra 2,320) then period table; annual Single 0% to 3,605, 5.2% to 26,605, then 1,196 + 5.58%; Married 0% to 8,240, 5.2% to 54,240, then 2,392 + 5.58%',K,'2024-07-01',None,{'vm':'derived arithmetically','n':'TRAP: table thresholds (26,605 / 54,240) = standard deduction + statutory band, not the statutory brackets (23,000 / 46,000). Period thresholds = annual / periods (weekly 69 / 512 / 23.00; semimonthly married 343.33 / 2,260 / 99.67). KW-100 header still says "January 1, 2021" - figures are 2024 (never-do 6).'}),
 ('income_tax','ks.wh.table.single.zero_bracket.annual',3605,K,'2024-07-01',None,{'u':U}),
 ('income_tax','ks.wh.table.single.band1_ceiling.annual',26605,K,'2024-07-01',None,{'u':U}),
 ('income_tax','ks.wh.table.married.zero_bracket.annual',8240,K,'2024-07-01',None,{'u':U}),
 ('income_tax','ks.wh.table.married.band1_ceiling.annual',54240,K,'2024-07-01',None,{'u':U}),
 ('income_tax','ks.wh.allowance.weekly.single',176.15,K,'2024-07-01',None,{'u':U,'vm':'derived arithmetically','n':'9,160/52; joint 352.31; dependent 44.62.'}),
 ('income_tax','ks.wh.supplemental.rate',5,K,'2024-07-01',None,{'u':'percent','n':'When stated separately with federal flat %, or other percentage-withheld payments; aggregated: tables.'}),
 ('income_tax','ks.wh.rounding','percentage-method result may be rounded to nearest dollar (under 50c down, 50c+ up)',K,'2024-07-01',None,{}),
 ('income_tax','ks.wh.certificate','K-4 (Rev. 7-24): Single or Joint allowance rate (married with earning spouse marks Single); no K-4 = Single, no allowance; exempt needs KDOR verification; federal W-4 not accepted','US-KSS5-025','2024-07-01',None,{}),
 ('income_tax','ks.pit.rate_cut_trigger.2026','not triggered: FY2025 collections 88,481,523 below inflation-adjusted base (Notice 25-06)','US-KSS5-002','2026-01-01','2026-12-31',{}),
 ('income_tax','ks.pit.rate_cut_trigger.2027','not triggered: FY2026 collections 214,339,364 below base (Notice 26-11, 2026-10-15)','US-KSS5-003','2027-01-01','2027-12-31',{}),
 ('non_resident','ks.nonres.rules','full-time in KS: as resident; partly in KS: KS tax on total wages x KS share (hours/days/commissions), K-4C allocation; interstate carriers P.L. 91-569; residents working elsewhere: KS tax less other-state required withholding; NRAs withheld when federal applies; no reciprocity',K,'2024-07-01',None,{'n':'Level withholding; nonresident ratio at assessment (79-32,110(b)).'}),
 ('local_tax','ks.local_wage_tax.exists',False,'US-KSP9V-002','2026-01-01',None,{'c':'medium','n':'KDOR tax list only wage item is withholding; 12-16,130 does not itself bar a local income tax.'}),
 ('social_security','ks.sui.wage_base',15100,'US-KSS5-023','2026-01-01','2026-12-31',{'u':U,'n':'44-703(o)(2): 25% of prior-year SAAW rounded to 100 for 2026-27 (30% 2028, 35% 2029, 40% 2030-31) [US-KSS5-020]. G-DERIVE: max WBA 637 = 55% SAWW -> SAAW 60,225-60,320 -> 25% = 15,056-15,080 -> 15,100. 2025: 14,000. 2027 projection ~15,700 NOT a fact.'}),
 ('social_security','ks.sui.employer.rate.min',0,'US-KSS5-023','2026-01-01','2026-12-31',{'u':'percent','n':'Schedule C (HB 2570): 0%-6.95%; not re-traced into 44-710a tables.'}),
 ('social_security','ks.sui.employer.rate.max',6.95,'US-KSS5-023','2026-01-01','2026-12-31',{'u':'percent'}),
 ('social_security','ks.sui.new_employer.rate',1.75,'US-KSS5-029','2026-01-01',None,{'u':'percent','vm':'second independent authority','n':'44-710a(a)(1) until 24 months chargeability; KDOL table [US-KSS5-023].'}),
 ('social_security','ks.sui.new_employer.construction.rate',5.55,'US-KSS5-029','2026-01-01',None,{'u':'percent'}),
 ('social_security','ks.sui.government_rated.rate',0.10,'US-KSS5-023','2025-01-01','2027-12-31',{'u':'percent'}),
 ('social_security','ks.sui.wage_base.other_state_credit',True,'US-KSS5-020','2026-01-01',None,{'n':'44-703(o)(2)(C)(i). Coverage: agricultural 20,000/quarter or 10 in 20 weeks; domestic 1,000/quarter; tips >= 20/month are UI wages.'}),
 ('social_security','ks.sui.employee.rate',0,'US-KSS5-023','2026-01-01',None,{'u':'percent','c':'medium'}),
 ('payslip_statute','ks.payslip.required','itemized statement of deductions on request for each pay period with deductions (44-320(d)); no routine pay statement; payroll card net shown on earnings statement (44-314(d))','US-KSS5-013','2026-01-01',None,{'c':'medium','n':'44-320(d) on legacy row US-KS-P5-2-001.'}),
 ('data_protection','ks.records.retention_years',3,'US-KSS5-011','2026-01-01',None,{'u':'years','n':'44-1209: name, occupation, rate, amount paid, daily/weekly hours; FLSA records acceptable.'}),
 ('reporting_instruments','ks.report.wh.deposit_frequency','quad-monthly > 100,000/yr (7th/15th/21st/last, 3 banking days); semi-monthly 8,000-100,000 (25th / 10th); monthly 1,200-8,000 (15th); quarterly 200-1,200 (25th after quarter); annual <= 200 (Jan 25); KW-5 every period even if zero','US-KSS5-007','2026-01-01',None,{}),
 ('reporting_instruments','ks.report.annual.kw3','KW-3 electronic by January 31 with state W-2s and 1099s with KS withholding; closure within 30 days after month of closure',K,'2024-07-01',None,{}),
 ('reporting_instruments','ks.report.w2.efile_threshold_forms',51,'US-KSS5-026','2025-10-01',None,{'u':'forms','n':'EFW2 with KS RS (K-2MT Rev. 10-25; RA/RE/RW/RS/RT/RF) or KW-2CSV; box 15 036-XXXXXXXXXF-01; no CF/SF. TY2026 K-2MT not located.'}),
 ('reporting_instruments','ks.report.sui.quarterly','wage report + contribution return due Apr 30 / Jul 31 / Oct 31 / Jan 31; MMREF / NASWA upload; paper K-CNS-100 for small employers','US-KSS5-022','2026-01-01',None,{'n':'E-file threshold 25+ (EDI, from 2024-07-01) vs 26+ (FAQ) conflict open.'}),
 ('reporting_instruments','ks.newhire.report_business_days',20,'US-KSS5-019','2026-01-01',None,{'u':'business days','n':'K.S.A. 75-5743 (statute governs over KDOL "20 days"); rehire after 60+ days.'}),
 ('leave','ks.leave.sick.state_mandate.exists',False,'US-KSS5-012','2026-01-01',None,{}),
 ('termination','ks.final_pay.rule','next regular payday for discharge and resignation, by mail on request; willful non-payment 1%/day after 8th day, max 100% (44-315)','US-KSS5-014','2026-01-01',None,{'n':'Vacation payout only by policy/contract (Mid America Aerospace, 1985).'}),
 ('termination','ks.final_wage.deductions','with written notice for unreturned property, loans, overpayment, merchandise; never below MW (44-319(c),(e))','US-KSS5-016','2026-01-01',None,{}),
 ('benefits_in_kind','ks.pit.conformity','KS AGI = federal AGI + modifications (79-32,117(a)); federal exclusions flow through; departure: KPERS employer-picked-up contributions are a KS addition (79-32,117(b)(vi))','US-KSS5-028','2026-01-01',None,{}),
 ('deductions_garnishments','ks.deductions.authorised','required by law; medical without employer benefit; signed authorisation for employee benefit; retirement auto-enrolment; written agreement for loans/overpayment/merchandise; charity and union dues; never below MW (44-319)','US-KSS5-016','2026-01-01',None,{}),
 ('deductions_garnishments','ks.garn.creditor.rule','lesser of 25% of disposable, excess over 30 x federal MW (217.50/week), or the claim; one garnishment per creditor per 30 days (60-2310)','US-KSS5-017','2026-01-01',None,{}),
 ('deductions_garnishments','ks.garn.child_support.cap_percent',50,'US-KSS5-018','2026-01-01',None,{'u':'percent','n':'23-3104/3105: total cap 50% of disposable incl. fee and medical premiums; start next pay after 14 days; remit within 7 business days; fee lesser of 5/period or 10/month on top; IV-D contact 14 days before lump sum with arrears.'}),
 ('deductions_garnishments','ks.garn.child_support.fee_per_period',5,'US-KSS5-018','2026-01-01',None,{'u':U}),
 ('deductions_garnishments','ks.garn.child_support.fee_monthly_max',10,'US-KSS5-018','2026-01-01',None,{'u':U}),
 ('live_change','ks.live.sb471.status','died at end of 2025-2026 biennium (minimum wage 16/h) - do not model','US-KSS5-027','2026-01-01',None,{}),
]
LEGACY = [('collective_agreements','ks.prevailing_wage.state_law.exists',False,'US-KS-P5-2-002','1987-01-01',None,'Repealed 1987 (K.S.A. 44-201); Davis-Bacon only.')]
CITED = ['US-KSS5-009','US-KSS5-011','US-KSS5-015','US-KSS5-021','US-KSS5-024','US-KSP9V-001','US-KS-P5-1-003','US-KS-P5-1-005','US-KS-P5-2-001','US-KS-P5-2-003','US-LA-P5-2-002','US-LA-P5-2-004','US-FED-P5-2-006','US-KSP9L-002']
NARR = {
 'labour_code': 'State MW/OT exclusions (44-1202(e)) [US-KSS5-009]: agriculture; private-home domestic; EAP and outside commission sales; federal employees; nonprofit volunteers; 18 or under occasional/part-time; USD EAP staff.',
 'social_security': 'No SDI/TDI/PFML [US-LA-P5-2-002 legacy]; no levy beyond UI [US-KSP9V-001].',
 'indexation': 'MW, std deduction, exemptions fixed; PIT revenue-contingent cut certified each Aug 15 (not triggered 2026/2027); UI base % of SAAW yearly; WBA 55% SAWW July 1; schedule yearly (KDOL by Dec 1).',
 'data_protection': 'SSN commercial use limited, internal administrative use exempt, penalty up to 1,000 (K.S.A. 75-3520) [US-KSS5-024]; no truncation rule; breach law 50-7a01 not read.',
}
SPECIAL = '''- Domestic: withholding follows federal (voluntary); UI 1,000 cash/quarter; excluded from state MW [US-KSS5-001, US-KSS5-020, US-KSS5-009].
- Agricultural: withholding follows federal; UI 20,000/quarter or 10 in 20 weeks (non-cash not UI wages); state MW excluded [US-KSS5-001, US-KSS5-020].
- Minors: 18 or under occasional/part-time excluded from state MW; UI excludes newspaper delivery under 18 and child under 21 for parent [US-KSS5-009, US-KSS5-020].
- Tipped: 2.13 (non-FLSA employers); tips >= 20/month UI wages [US-KSS5-008, US-KSS5-020].
- Clergy: UI excludes church employment and ministers; withholding follows federal [US-KSS5-020, US-KSS5-001].
- Students: own-school and work-study UI-excluded [US-KSS5-020, US-KSS5-009].
- NRAs / statutory employees: follow federal; PEO = employer [US-KSS5-001].
- Government: withholding required; rated governmental UI 0.10%; KPERS pick-up addition (open) [US-KSS5-001, US-KSS5-023, US-KSS5-028].
- Motion-picture extras under 14 days/yr: exempt from KS withholding [US-KSS5-001].'''
LANG = 'Bilingual agency documents expressly permitted; official-language designation government-only [US-KSP9L-002]; payslip English (US-OWN-006).'
UNRES = [
 {'key':'ks.wh.kpers_pickup','why':'79-32,117(b)(vi) adds KPERS picked-up contributions to KS income; whether KS withholding applies to them on public-employer payroll is not stated.','close':'KDOR KW-100 PDF or a Revenue Ruling on picked-up contributions.'},
 {'key':'ks.report.sui.efile_threshold','why':'KDOL FAQ says 26+ employees, the EDI section says 25+ (from 2024-07-01).','close':'KDOL Employer Handbook e-filing section or the K.A.R. / act that set the mandate.'},
 {'key':'ks.termination.ui_separation_notice','why':'No Kansas separation notice requirement located.','close':'KDOL Employer Handbook (UI) separations section or K.A.R. 50-3.'},
 {'key':'ks.leave.jury_military','why':'Jury duty (K.S.A. 43-173) and state military leave not read.','close':'Those Revisor pages.','blocking':False},
 {'key':'ks.report.w2.k2mt_next_edition','why':'TY2026 K-2MT edition (RS layout for files due 2027-01-31) not posted.','close':'KDOR forms-btwh.html when Rev. 2026 is posted.'},
 {'key':'ks.sui.wage_base.next_year','why':'2027 base unpublished; ~15,700 is a projection only.','close':'KDOL Employer Tax Rates table for rate year 2027 (by Dec 1, 2026).'},
 {'key':'ks.sui.schedule_c.statute_trace','why':'44-710a Schedule C table not traced row by row against KDOL 0%-6.95%.','close':'Parse the schedule tables in KSA_044_007_0010a (on disk).','blocking':False},
]
