NAME = 'Massachusetts'
SUMMARY = 'Minimum wage 15.00 (not indexed; service rate 6.75; agricultural 8.00); weekly overtime. PIT 5.0% + 4% surtax above 1,107,750 (2026); M-4 exemptions; Circular M tables or percentage method (they differ by up to 0.02); supplemental 5% (9% above threshold); no reciprocity (credit method), no local tax. UI base 15,000, new 2.42%, Schedule E 0.94%-14.37% + COVID Recovery Assessment 0.178%-2.716%; EMAC 0.12/0.24/0.34%; WTF 0.056%; PFML 0.88% (25+) / 0.46% (<25) with the Chapter 101 family/medical swap applied from 2027-01-01 (decision recorded). Pay slip c.149 s.148. Discharge: pay same day.'
U = 'USD'
C = 'US-MAS5-013'
FACTS = [
 ('labour_code','ma.minwage.hourly',15.00,'US-MAS5-001','2023-01-01',None,{'u':U,'n':'Never less than federal + 0.50; not indexed; no 2027 rate enacted [US-MAS5-017].'}),
 ('labour_code','ma.minwage.service_rate',6.75,'US-MAS5-003','2023-01-01',None,{'u':U,'n':'Tipped cash wage; max tip credit 15.00 - 6.75 = 8.25 (derived); top-up per shift.'}),
 ('labour_code','ma.minwage.tip_credit.max',8.25,'US-MAS5-003','2023-01-01',None,{'u':U,'vm':'derived arithmetically','n':'15.00 - 6.75.'}),
 ('labour_code','ma.minwage.agricultural',8.00,'US-MAS5-004','2026-01-01',None,{'u':U,'n':'Not children 17 or under or immediate family; agriculture exempt from state OT [US-MAS5-002].'}),
 ('labour_code','ma.overtime.weekly_threshold_hours',40,'US-MAS5-002','2026-01-01',None,{'u':'hours','n':'1.5x; no daily OT; commissions/bonuses/incentives excluded from regular rate.'}),
 ('income_tax','ma.pit.rate',5.0,'US-MAR3-002','2026-01-01',None,{'u':'percent','n':'Plus 4% surtax above 1,107,750 (2026); withholding at combined 9% above threshold. IP 25-18 (4.67% 2027) excluded from ballot per tier-B (SJC-13885) - do not model.'}),
 ('income_tax','ma.pit.surtax.rate',4.0,'US-MAR3-002','2026-01-01',None,{'u':'percent'}),
 ('income_tax','ma.pit.surtax.threshold',1107750,'US-MAR3-002','2026-01-01','2026-12-31',{'u':U,'n':'Indexed (CPI mechanism not re-read); published in Circular M.'}),
 ('income_tax','ma.wh.method','Circular M wage-bracket tables or percentage method: wages - FICA/Medicare/retirement (max 2,000/yr) - exemption amount for period; x 5%; - HoH / blind reduction',C,'2026-01-01',None,{'n':'Methods not numerically identical (table vs percentage differ up to 0.02 weekly); engine must use one method consistently [US-MAS5-024].'}),
 ('income_tax','ma.wh.exemption.weekly','19n + 66',C,'2026-01-01',None,{'n':'Daily 3n+9; biweekly 38n+131; semimonthly 42n+141; monthly 83n+284; annual 1,000n+3,400 (n = exemptions).'}),
 ('income_tax','ma.wh.exemption.annual','1,000n + 3,400',C,'2026-01-01',None,{}),
 ('income_tax','ma.wh.fica_retirement_deduction.annual_max',2000,C,'2026-01-01',None,{'u':U}),
 ('income_tax','ma.wh.hoh_reduction.weekly',2.31,C,'2026-01-01',None,{'u':U,'n':'Biweekly 4.62, semimonthly 5.00, monthly 10.00, daily 0.33.'}),
 ('income_tax','ma.wh.blind_reduction.weekly',2.12,C,'2026-01-01',None,{'u':U,'n':'Per person; biweekly 4.23, semimonthly 4.58, monthly 9.17, daily 0.30.'}),
 ('income_tax','ma.wh.certificate','M-4: line 1 personal (1, or 2 if 65+), line 2 spouse (4, or 5 if 65+), line 3 dependents, line 5 additional; boxes A HoH, B blind, C spouse blind, D full-time student <= 8,000 (no withholding); none filed = zero exemptions; new M-4 within 10 days on decrease; exemptions only with principal employer','US-MAS5-014','2026-01-01',None,{'n':'Edition date not printed in extracted text.'}),
 ('income_tax','ma.wh.student_box_d.income_max',8000,'US-MAS5-014','2026-01-01',None,{'u':U}),
 ('income_tax','ma.wh.supplemental.rule','5% while annualized regular + supplemental to date + this payment <= 1,107,750; above: lesser of 9% of payment or 9% of excess plus 5% of remainder','US-MAP51-003','2026-01-01',None,{}) if False else ('income_tax','ma.wh.supplemental.rate',5,'US-MAR3-002','2026-01-01',None,{'u':'percent','c':'medium','n':'Circular M [US-MAP51-003 legacy]: 5% while cumulative <= 1,107,750; above, lesser of 9% of payment or 9% of excess + 5% of remainder.'}),
 ('income_tax','ma.wh.rounding','wages may be computed to nearest dollar (830 CMR 62B.2.1(8))','US-MAS5-023','2026-06-05',None,{}),
 ('non_resident','ma.nonres.rules','residents on all wages; nonresidents on MA-performed services; nonresident not working in MA not withheld even if paid from MA office; courtesy withholding for residents by out-of-state employers; no reciprocity - credit method: MA amount minus other jurisdiction amount (830 CMR 62B.2.1(9)(b))',C,'2026-01-01',None,{'n':'No MA withholding where no federal duty (household); MSRRA M-4-MS: do not withhold [US-MAS5-024].'}),
 ('local_tax','ma.local_wage_tax.exists',False,'US-MAR3-002','2026-01-01',None,{'n':'No local wage/payroll/income tax [US-MAR3-001, US-MAR3-003].'}),
 ('social_security','ma.sui.new_employer.rate',2.42,'US-MAS5-022','2026-01-01','2026-12-31',{'u':'percent','n':'Under 3 years; construction 6.08%; base 15,000 fixed (c.151A s.14, legacy US-MAP51-005); no employee UI.'}),
 ('social_security','ma.sui.new_employer.construction.rate',6.08,'US-MAS5-022','2026-01-01','2026-12-31',{'u':'percent'}),
 ('social_security','ma.sui.employer.rate.min',0.94,'US-MAS5-020','2026-01-01','2026-12-31',{'u':'percent','n':'Schedule E; COVID Recovery Assessment 0.178%-2.716% on same base; effective 1.118%-17.086% (UI + COVID = effective in every band, Python).'}),
 ('social_security','ma.sui.employer.rate.max',14.37,'US-MAS5-020','2026-01-01','2026-12-31',{'u':'percent'}),
 ('social_security','ma.sui.covid_recovery.rate.min',0.178,'US-MAS5-020','2026-01-01','2026-12-31',{'u':'percent'}),
 ('social_security','ma.sui.covid_recovery.rate.max',2.716,'US-MAS5-020','2026-01-01','2026-12-31',{'u':'percent'}),
 ('social_security','ma.sui.wage_base',15000,'US-MAS5-020','2026-01-01',None,{'u':U,'n':'Fixed by statute, not indexed.'}),
 ('social_security','ma.sui.coverage','1 employee 13 weeks or 1,500/quarter; agricultural 40,000/quarter or 10 for 20 weeks; domestic 1,000 cash/quarter; out-of-state employers 200 MA wages/quarter; notices by Jan 31; review requests before Jun 20; 12% late interest','US-MAS5-022','2026-01-01',None,{}),
 ('social_security','ma.emac.rate.year4',0.12,'US-MAS5-021','2026-01-01',None,{'u':'percent','n':'EMAC on 15,000 base: years 1-3 exempt; year 4 0.12%; year 5 0.24%; year 6+ 0.34%; fewer than 6 employees in a quarter exempt.'}),
 ('social_security','ma.emac.rate.year5',0.24,'US-MAS5-021','2026-01-01',None,{'u':'percent'}),
 ('social_security','ma.emac.rate.year6_plus',0.34,'US-MAS5-021','2026-01-01',None,{'u':'percent'}),
 ('social_security','ma.wtf.rate',0.056,'US-MAP7-001','2026-01-01',None,{'u':'percent','c':'medium','n':'c.151A s.14L; 2026 DUA value not confirmed (commissioner may adjust).'}),
 ('social_security','ma.pfml.rate.total.25_plus',0.88,'US-MAS5-012','2026-01-01',None,{'u':'percent','n':'Unchanged total in 2027. Cap: SS wage base (c.175M s.6(f)) [US-MAS5-010].'}),
 ('social_security','ma.pfml.rate.total.under_25',0.46,'US-MAS5-012','2026-01-01',None,{'u':'percent','n':'No employer share.'}),
 ('social_security','ma.pfml.family.rate',0.18,'US-MAS5-012','2026-01-01','2026-12-31',{'u':'percent','n':'Up to 100% from employee.'}),
 ('social_security','ma.pfml.medical.rate',0.70,'US-MAS5-012','2026-01-01','2026-12-31',{'u':'percent','n':'Employee up to 40% (0.28%), employer 0.42% (25+).'}),
 ('social_security','ma.pfml.family.rate',0.70,'US-MAS5-012','2027-01-01',None,{'u':'percent','n':'Chapter 101 swap: employee up to 40% (0.28%), employer 0.42%.'}),
 ('social_security','ma.pfml.medical.rate',0.18,'US-MAS5-012','2027-01-01',None,{'u':'percent','n':'Up to 100% from employee.'}),
 ('social_security','ma.pfml.employee.max_total.25_plus',0.46,'US-MAS5-012','2026-01-01',None,{'u':'percent','vm':'derived arithmetically','n':'2026: 0.18 + 0.28; 2027: 0.28 + 0.18 - the employee and employer totals (0.46 / 0.42) are identical either side of the swap; only the family/medical labelling (benefit tax treatment) changes.'}),
 ('social_security','ma.pfml.split.decision','Chapter 101 ss.25-26 family/medical deduction-cap swap applied from 2027-01-01 per DFML; 2026 payroll uses the DFML 2026 table','US-MAS5-012','2026-01-01',None,{'c':'medium','n':'DECISION (brief trap): s.45 of Ch. 101 [US-MAS5-026] says ss.25-26 apply "for taxable years beginning on or after January 1, 2026"; DFML, the administering authority, implements from 2027-01-01 [US-MAS5-012]. Decided for DFML: (1) "taxable years" is income-tax language and the swap was made to address the IRS tax treatment of benefits, an assessment-level matter; (2) the contribution totals withheld (0.46% employee / 0.42% employer) are identical under both readings, so no 2026 payroll amount changes; (3) DFML has issued no 2026 re-split or catch-up instruction. Re-open only if DFML/DOR (458 CMR 2.00) issues a transition notice.'}),
 ('social_security','ma.pfml.benefit.weekly_max',1230.39,'US-MAS5-025','2026-01-01','2026-12-31',{'u':U,'vm':'derived arithmetically','n':'64% x SAWW 1,922.48; benefit side, paid by DFML (not payroll).'}),
 ('social_security','ma.pfml.benefit.weekly_max',1284.61,'US-MAS5-025','2027-01-01',None,{'u':U,'vm':'derived arithmetically','n':'64% x 2,007.20.'}),
 ('payslip_statute','ma.payslip.items','employer name, employee name, date (day/month/year), hours worked, hourly rate, deductions or increases for the period (c.149 s.148)','US-MAS5-005','2026-01-01',None,{'c':'medium','n':'Statute row is legacy US-MAP51-008; e-delivery consent not located.'}),
 ('data_protection','ma.records.retention_years',3,'US-MAS5-005','2026-01-01',None,{'u':'years','n':'c.151 s.15; employees may inspect; DOR withholding records 3 years.'}),
 ('reporting_instruments','ma.report.wh.frequency','<= 100/yr annual (Jan 31); 101-1,200 quarterly; 1,201-25,000 monthly by 15th (quarter-end months on last day of following month); > 25,000 quarterly return + payment within 3 business days when >= 500 accumulated by 7th/15th/22nd/last; e-file mandatory for new registrations, payroll providers, combined liability >= 5,000',C,'2026-01-01',None,{}),
 ('reporting_instruments','ma.report.w2','due Jan 31; 50+ W-2s electronic via MassTaxConnect/Bulk File Portal; <= 49 paper with M-3; corrections paper W-2c; EFW2 RA/RE/RS/RT, RS MA wages 276-286, MA tax 287-297, RT = sum RS','US-MAS5-015','2026-01-30',None,{'n':'Format [US-MAS5-019] handbook Rev. 20191219. Guide (Aug 2026) says last day of March / Feb 28 - conflict (Q4); use Jan 31.'}),
 ('reporting_instruments','ma.report.w2.efile_threshold',50,'US-MAS5-015','2026-01-30',None,{'u':'forms'}),
 ('reporting_instruments','ma.report.sui.quarterly','DUA wage detail by 3 p.m. Apr 30 / Jul 31 / Oct 31 / Jan 31; CSV, EFW2 or ICESA; EAN, SSN, name, hours, gross, wages subject to withholding, state tax withheld, work location, 12th-of-month, adjustment reason; wages when paid','US-MAS5-018','2026-01-01',None,{}),
 ('reporting_instruments','ma.newhire.report_days',14,'US-MAS5-016','2026-01-01',None,{'u':'days','n':'Employees and contractors 600+; rehires after 30+ days; SSN only (no ITIN); 25+ employees online.'}),
 ('leave','ma.leave.sick.employer_threshold_paid',11,'US-MAS5-006','2026-01-01',None,{'u':'employees','n':'c.149 s.148C: 1 h per 30 h; use from day 90; 40 h/yr paid (11+) or unpaid; carryover 40; no payout; certification after 24 consecutive scheduled hours.'}),
 ('leave','ma.leave.sick.cap_hours',40,'US-MAS5-006','2026-01-01',None,{'u':'hours'}),
 ('leave','ma.leave.sick.payout_on_separation',False,'US-MAS5-006','2026-01-01',None,{}),
 ('deductions_garnishments','ma.garn.creditor.exempt_rule','greater of 85% of gross wages or 50 x higher of federal/MA MW per week; support orders: CCPA (c.246 s.28)','US-MAS5-009','2026-01-01',None,{}),
 ('deductions_garnishments','ma.garn.creditor.weekly_exempt_floor',750,'US-MAS5-009','2023-01-01',None,{'u':U,'vm':'derived arithmetically','n':'50 x 15.00.'}),
 ('collective_agreements','ma.prevailing_wage.certified_payroll','weekly certified payroll with signed statement to awarding authority; apprentice ID copies; records 3 years after contract; compliance statement within 15 days of completion; no dollar threshold (s.27B)','US-MAS5-007','2026-01-01',None,{}),
 ('benefits_in_kind','ma.pit.irc_decoupling','c.62C s.90 (Ch. 101 s.13, from TY2026): same-year IRC amendments do not affect MA gross income; accountable-plan reimbursements not wages','US-MAS5-026','2026-01-01',None,{'n':'Level assessment flowing into withholding definition.'}),
 ('live_change','ma.live.chapter_101_2026','enacted (emergency, approved 2026-06-12): PFML split swap (applied 2027-01-01, see decision), IRC same-year decoupling, P.L. 119-21 s.70302(f) deduction (subject unchecked)','US-MAS5-026','2026-06-12',None,{}),
]
FACTS = [f for f in FACTS if f[1] != 'ma.wh.supplemental.rule']
LEGACY = [
 ('income_tax','ma.wh.supplemental.rule','5% while annualized regular + supplemental to date + this payment <= 1,107,750; above, lesser of 9% of payment or 9% of excess plus 5% of remainder; percentage method excludes supplemental','US-MAP51-003','2026-01-01',None,'Circular M 2026.'),
 ('termination','ma.final_pay.rule','discharge: in full on the day of discharge; resignation: next regular payday (or following Saturday); agreed vacation/holiday pay are wages payable at termination (c.149 s.148)','US-MAP51-008','2026-01-01',None,''),
 ('collective_agreements','ma.prevailing_wage.rule','wages at least the commissioner rate on public works (c.149 s.26)','US-MAP51-009','2026-01-01',None,''),
]
CITED = ['US-MAS5-008','US-MAS5-010','US-MAS5-011','US-MAS5-017','US-MAS5-019','US-MAS5-024','US-MAS5-027','US-MAS5-028','US-MAR3-001','US-MAR3-003','US-MAP7-002','US-MAP9W-004','US-MAP51-005','US-MAL-002']
NARR = {
 'labour_code': 'Pay weekly or biweekly within 6 days of period end (7 if 7-day week); casual within 7 days [legacy US-MAP51-008]. Payment method/e-stub consent not located (Q1). No local MW located (commissioner power under c.151 s.7 unused).',
 'social_security': 'No SDI/TDI; PFML the only employee-funded program [US-MAP9W-004]. PFML benefits paid by DFML (optional 5%/10% withholding), not payroll.',
 'reporting_instruments': 'Registration MassTaxConnect (DOR, PFML) and DUA portal. PFML quarterly return mechanics unread (Q8).',
 'leave': 'PFML benefit: 7-day wait; 80% of AWW to 50% SAWW + 50% above; caps 20/12/26 weeks. Parental, small necessities, DV, jury leave not read.',
 'termination': 'Sick time no payout. UI separation notice instrument not located (Q10).',
 'indexation': 'MW and UI base not indexed; UI/COVID and PFML rates yearly; PFML cap = SS base; PFML max benefit 64% SAWW; surtax threshold indexed; M-4 factors static.',
 'data_protection': 'No SSN-on-slip rule located; c.93H / 201 CMR 17.00 not read.',
}
SPECIAL = '''- Domestic: MW/OT apply (incl. au pairs); written agreement for 16+ h/week; meal deductions max 1.50/2.25; lodging max 35/30/25 per week; UI 1,000 cash/quarter; paystub records 3 years [US-MAS5-028, US-MAS5-022].
- Agricultural: MW 8.00 (not family/under 18); OT-exempt; UI 40,000/quarter or 10 for 20 weeks [US-MAS5-004, US-MAS5-002, US-MAS5-022].
- Minors: MW applies; UI-exempt working for a parent; permits/hours not read [US-MAS5-001, US-MAS5-022].
- Tipped: service rate 6.75; tips 20+/month reported by 10th are withheld on [US-MAS5-003, US-MAS5-013].
- Clergy: religious order members excluded from MW; some religious work UI-exempt; religious organisations still withhold [US-MAS5-017, US-MAS5-022, US-MAS5-013].
- Students: M-4 box D (<= 8,000) no withholding; nonprofit/public work-training UI-exempt [US-MAS5-014, US-MAS5-024, US-MAS5-022].
- NRAs: follow federal duty [US-MAS5-013]. MSRRA: M-4-MS no withholding [US-MAS5-024]. Statutory employees: no state rule.
- Government: must withhold and report new hires; municipal employees excluded from c.151 MW; earned sick time only on local acceptance [US-MAS5-013].
- Interstate carriers: residents and nonresidents with all duties in MA [US-MAS5-013]. Family employment UI-exempt [US-MAS5-022].'''
LANG = 'Earned sick time notice languages c.149 s.148C(o) [US-MAL-002]; payslip English (US-OWN-006).'
UNRES = [
 {'key':'ma.payment.method_and_estub_consent','why':'Direct deposit, paycard and electronic pay-stub consent rules not located.','close':'AG Fair Labor Division wage-payment advisory or 454 CMR 27.00.'},
 {'key':'ma.wh.certificate.edition','why':'M-4 revision date not printed in extracted text.','close':'Form footer or DOR withholding forms list.','blocking':False},
 {'key':'ma.report.w2.handbook_edition','why':'W-2 e-file handbook served is Rev. 20191219 though reissued yearly.','close':'TY2026 edition from DOR bulk-file support.'},
 {'key':'ma.report.w2.due_date_conflict','why':'Jan 31 (W-2 page 2026-01-30, handbook) vs last day of March / Feb 28 (Withholding Tax Guide Aug 2026).','close':'DOR Directive/TIR fixing the W-2/M-3 due date (Directives 97-1, 07-2, 09-8).','blocking':True},
 {'key':'ma.report.quarterly_wage_report.single','why':'Whether the DUA wage detail report is the only quarterly wage report (DOR guide mentions DOR reports).','close':'DOR "File quarterly wage reports" page.'},
 {'key':'ma.sui.wtf.current','why':'2026 Workforce Training Fund rate as published by DUA not read.','close':'DUA WTF page or 430 CMR 14.00.'},
 {'key':'ma.report.pfml.quarterly','why':'PFML quarterly return mechanics not read.','close':'DFML page "Wage contributions & reporting for PFML".'},
 {'key':'ma.pit.conformity.items','why':'401(k)/403(b), 125, HSA, transit, GTL treatment not read in a DOR source.','close':'DOR fringe-benefit tax treatment guidance or TIRs.','blocking':True},
 {'key':'ma.garn.iwo_and_deductions','why':'c.149 s.150 deduction authorisation and MA IWO fees/priority not read.','close':'c.149 s.150 text and DOR Child Support Services employer page.'},
 {'key':'ma.pfml.split.transition_notice','why':'Ch. 101 s.45 vs DFML effective date (decided for DFML 2027-01-01; totals unaffected).','close':'DFML/DOR notice or 458 CMR 2.00 transition rule.','blocking':False},
 {'key':'ma.pit.chapter101_s8_deduction','why':'Subject of the P.L. 119-21 s.70302(f) deduction and any withholding effect unchecked.','close':'DOR TIR implementing Chapter 101.','blocking':False},
 {'key':'ma.live.bulletin_sweep','why':'2026 DOR TIRs/Directives and DUA/DFML news not swept.','close':'DOR TIR index 2026 and DFML/DUA news pages.'},
 {'key':'ma.live.ip_25_18','why':'IP 25-18 exclusion rests on tier-B (US-MAS5-027 MANUAL); SJC opinion URL 404.','close':'SJC-13885 opinion on mass.gov/sjc or the Secretary of the Commonwealth 2026 ballot list.','blocking':False},
 {'key':'ma.other_leave_and_minors','why':'c.149 ss.52D, 52E, 105D, jury c.234A s.48 and child labour ss.60-66 not read.','close':'Statute texts on malegislature.gov.','blocking':False},
 {'key':'ma.termination.ui_separation_notice','why':'DUA separation notice form/rule not located (430 CMR 5.00 index only).','close':'430 CMR 4.00/5.00 PDF text or DUA employer guide.'},
]
