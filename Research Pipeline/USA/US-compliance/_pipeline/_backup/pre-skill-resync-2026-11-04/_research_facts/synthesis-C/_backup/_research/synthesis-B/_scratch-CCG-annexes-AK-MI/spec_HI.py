NAME = 'Hawaii'
SUMMARY = 'Minimum wage 16.00 (2026-2027), 18.00 from 2028; tip credit 1.25. Withholding per Booklet A (Rev. 2025): allowance 1,144 + lump-sum 4,350, brackets 1.40%-7.90%, HW-4 (no exempt status), no flat supplemental, no reciprocity, no local tax; 2027 tables will change under Act 24 SLH 2026 (2.5% / 5% / new 13%) - unpublished. UI employer-only, base 64,500 (AAW-indexed), new 2.40%, E&T 0.01%; TDI employee max 0.5% capped 7.50/week; Prepaid Health Care threshold 1,387/month. 14-item pay statement (HRS 387-6(c)). Oracle: Booklet A Part 1 example 9.58.'
U = 'USD'
B = 'US-HIS5-004'
FACTS = [
 ('labour_code','hi.minwage.hourly',16.00,'US-HIS5-001','2026-01-01','2027-12-31',{'u':U,'vm':'second independent authority','n':'HRS 387-2 and DLIR agree [US-HIS5-002]; no 2027 step; no indexation; no county rates.'}),
 ('labour_code','hi.minwage.hourly',18.00,'US-HIS5-001','2028-01-01',None,{'u':U,'n':'Enacted (L 2022 c 114).'}),
 ('labour_code','hi.minwage.tip_credit',1.25,'US-HIS5-001','2024-01-01','2027-12-31',{'u':U,'n':'Only if wage + tips >= MW + 7.00; tipped = > 20/month tips [US-HIS5-003]; cash wage 14.75. 1.50 from 2028.'}),
 ('labour_code','hi.minwage.tip_credit',1.50,'US-HIS5-001','2028-01-01',None,{'u':U}),
 ('labour_code','hi.minwage.tip_credit.min_total_over_minwage',7.00,'US-HIS5-001','2024-01-01',None,{'u':U}),
 ('labour_code','hi.minwage.exempt.guaranteed_monthly',4000,'US-HIS5-003','2024-07-01',None,{'u':U,'n':'HRS 387-1 carve-out (L 2024 c 73); also agriculture < 20 employees, coffee harvesting, casual domestic/companionship.'}),
 ('labour_code','hi.overtime.weekly_threshold_hours',40,'US-HIS5-003','2026-01-01',None,{'u':'hours','n':'1.5x; regular-rate divisors weekly /40, biweekly /2/40, semimonthly x24/52/40, monthly x12/52/40; seasonal ag 20 weeks OT after 48; public works OT after 8/day and weekends/holidays.'}),
 ('labour_code','hi.pay_frequency.rule','at least twice each calendar month on designated paydays; monthly only by secret-ballot majority (2 years) or director permission; due within 7 days after period end (15 with permission)','US-HIS5-007','2026-01-01',None,{}),
 ('labour_code','hi.paycard.rules','employee chooses DD/check/card, never condition of hire; 10-pt disclosure; free 3 withdrawals per period, 24/7 balance, 60-day history, 1 replacement/yr; no overdraft/balance fees; switch within two pay periods (HRS 388-5.7)','US-HIS5-017','2026-01-01',None,{}),
 ('income_tax','hi.wh.method','wage-bracket tables (Part 3), annualized formula (Part 1) or per-period formula (Part 2), Booklet A Rev. 2025, effective 2026-01-01',B,'2026-01-01','2026-12-31',{'n':'Still current 2026-11-02 [US-HIS5-005]. Supplemental: no flat rate; aggregate with current/preceding period or average over periods covered. No withholding below 0.10 per payment.'}),
 ('income_tax','hi.wh.allowance.annual',1144,B,'2026-01-01','2026-12-31',{'u':U,'n':'Weekly 22.00.'}),
 ('income_tax','hi.wh.lump_sum_allowance.annual',4350,B,'2026-01-01','2026-12-31',{'u':U,'n':'Every employee; weekly 83.65 (4,350/52, re-derived).'}),
]
sb = [(9600,1.40,0),(14400,3.20,134),(19200,5.50,288),(24000,6.40,552),(36000,6.80,859),(48000,7.20,1675),(125000,7.60,2539),(None,7.90,8391)]
mb = [(19200,1.40,0),(28800,3.20,269),(38400,5.50,576),(48000,6.40,1104),(72000,6.80,1718),(96000,7.20,3350),(250000,7.60,5078),(None,7.90,16782)]
for tag, tbl in (('single',sb),('married',mb)):
    for i,(c,r,base) in enumerate(tbl,1):
        if c is not None:
            FACTS.append(('income_tax',f'hi.wh.bracket.{tag}.{i}.ceiling',c,B,'2026-01-01','2026-12-31',{'u':U}))
        FACTS.append(('income_tax',f'hi.wh.bracket.{tag}.{i}.rate',r,B,'2026-01-01','2026-12-31',{'u':'percent'}))
        if base:
            FACTS.append(('income_tax',f'hi.wh.bracket.{tag}.{i}.base_tax',base,B,'2026-01-01','2026-12-31',{'u':U,'vm':'derived arithmetically','n':'Cumulative bracket sum rounded to whole dollars (re-derived in Python).'}))
FACTS += [
 ('income_tax','hi.wh.certificate.form','HW-4 (Rev. 2022): Single / Married / Married-withhold-Single / Certified Disabled / Nonresident Military Spouse; no exempt status; federal W-4 not accepted; no HW-4 = Single 0; HoH withheld as Single + extra allowance; copy to Tax Assessor for excessive (>10) allowances','US-HIS5-026','2022-01-01',None,{}),
 ('income_tax','hi.pit.ot_deduction.conformed',False,'US-HIS5-029','2026-01-01',None,{'n':'Act 35 SLH 2026 (in force 2026-05-26, TY2026): IRC conformity 2025-12-31; IRC 224 tips deduction conformed (assessment); IRC 225 overtime NOT conformed; 132(f) bicycle suspended; IRC 128 Trump Account exclusion conformed.'}),
 ('social_security','hi.sui.wage_base',64500,'US-HIS5-011','2026-01-01','2026-12-31',{'u':U,'vm':'derived arithmetically','n':'HRS 383-61(b): AAW 4 quarters to 30 June rounded to 100; DCD AAW 64,471.82 -> 64,500 (G-CALIBER: both DLIR state averages, assumed same caliber). Other-state wages combine toward base [US-HIS5-012].'}),
 ('social_security','hi.sui.new_employer.rate',2.4,'US-HIS5-011','2026-01-01','2026-12-31',{'u':'percent','n':'Schedule C; rate at reserve ratio .0000.'}),
 ('social_security','hi.sui.employer.rate.max',5.6,'US-HIP9V-001','2026-01-01','2026-12-31',{'u':'percent'}),
 ('social_security','hi.sui.et_assessment.rate',0.01,'US-HIP9V-001','2026-01-01','2026-12-31',{'u':'percent','n':'Employers above 0% and below schedule max; not FUTA-creditable.'}),
 ('social_security','hi.sui.employee.rate',0,'US-HIS5-010','2026-01-01',None,{'u':'percent','n':'HRS 383-61(a) forbids deduction.'}),
 ('social_security','hi.tdi.employee.max_rate',0.5,'US-HIS5-014','2026-01-01',None,{'u':'percent','n':'Employer may withhold half the cost, max 0.5% of weekly wages; eligibility 400 + 14 weeks of 20+ h in prior 52 weeks; insurer-funded, no state return.'}),
 ('social_security','hi.tdi.max_weekly_wage_base',1500.21,'US-HIS5-015','2026-01-01','2026-12-31',{'u':U,'vm':'derived arithmetically','n':'64,471.82 / 52 x 1.21 [US-HI-003].'}),
 ('social_security','hi.tdi.employee.max_weekly_deduction',7.50,'US-HIS5-015','2026-01-01','2026-12-31',{'u':U}),
 ('social_security','hi.tdi.benefit.weekly_max',871.00,'US-HIS5-015','2026-01-01','2026-12-31',{'u':U}),
 ('social_security','hi.phc.min_monthly_wage',1387.00,'US-HIS5-015','2026-01-01','2027-12-31',{'u':U,'n':'Prepaid Health Care: regular employees 20+ h/week earning >= 86.67 x MW (1,386.72 rounded up by DCD); employee share max half premium and max 1.5% of wages [US-HIS5-016]. 2028 derived 1,560.06 not published.'}),
 ('social_security','hi.phc.employee_share.max_percent_of_wages',1.5,'US-HIS5-015','2026-01-01',None,{'u':'percent'}),
 ('payslip_statute','hi.payslip.items','employee name; employer name, address, phone; total hours; regular and OT hours; straight-time pay; OT pay; other compensation incl. MW allowances; gross; amount and purpose of each deduction; net; pay date; pay period; rates and basis incl. OT and piece rates/counts','US-HIS5-007','2026-01-01',None,{'c':'medium','n':'HRS 387-6(c) 14 items [US-HI-P5-2-001 legacy]; electronic with written authorization; direct deposit still requires statement.'}),
 ('reporting_instruments','hi.report.wh.hw14','HW-14 quarterly due Apr 15/Jul 15/Oct 15/Jan 15, filed even with no wages; VP-1 deposits quarterly <= 5,000, monthly 5,000-40,000 (15th), semi-weekly > 40,000 or federal semi-weekly (no lookback)','US-HIS5-005','2026-01-01',None,{}),
 ('reporting_instruments','hi.report.wh.semiweekly_threshold',40000,'US-HIS5-005','2026-01-01',None,{'u':U}),
 ('reporting_instruments','hi.report.w2.efile_threshold_forms',10,'US-HIS5-006','2026-01-01',None,{'u':'forms','n':'TA 2025-05; also if liability > 40,000; penalty 25/form up to 50/employee; W-2/HW-2 to DOTAX by 31 Jan; EFW2 upload (EF-10), Simple File Import <= 1,000 records (EF-12), Bulk SFTP (EF-9); HW-30 paper transmittal only.'}),
 ('reporting_instruments','hi.report.sui.ucb6','UC-B6 quarterly wage/contribution/E&T report due last day of month after quarter, even with no wages; name, SSN, total wages; late report 30, late contributions 10% (min 100) + 2/3%/month; registration within 20 days after first hire','US-HIS5-012','2026-01-01',None,{'c':'medium'}),
 ('reporting_instruments','hi.newhire.report_days',20,'US-HIS5-021','2026-01-01',None,{'u':'days','n':'CSEA: copy of W-4 by fax/mail or SFTP FLO101 fixed-width; rehire after 60+ days; penalty 25 / 500.'}),
 ('leave','hi.leave.sick.state_mandate.exists',False,'US-HIS5-024','2026-01-01',None,{'c':'medium'}),
 ('leave','hi.leave.family.employer_threshold',100,'US-HIS5-023','2026-01-01',None,{'u':'employees','c':'medium','n':'HRS ch. 398 (HRS 398-1 not read): 4 weeks unpaid per year after 6 months; up to 10 days accrued sick leave usable [US-HIS5-018].'}),
 ('termination','hi.final_pay.rule','discharge: at discharge or next working day; resignation: next regular payday (at quitting if one pay period notice); layoff: next regular payday (HRS 388-3)','US-HIS5-008','2026-01-01',None,{'n':'Accrued vacation not wages (108 H. 411, 2005): policy governs. No employer UI separation notice.'}),
 ('deductions_garnishments','hi.deductions.rule','only if required by statute/court or authorised in writing; never fines, till shortages, breakage, dishonored checks, non-wilful losses, required medical exams (HRS 388-6)','US-HIS5-009','2026-01-01',None,{}),
 ('deductions_garnishments','hi.garn.creditor.schedule','5% of first 100/month, 10% of next 100, 20% above 200 (weekly equivalent) on wages after required deductions; apply lower of this and CCPA','US-HIS5-019','2026-01-01',None,{}),
 ('deductions_garnishments','hi.garn.child_support.employer_fee',2,'US-HIS5-022','2003-01-01',None,{'u':U,'c':'medium','n':'FEN125 (2003, A.3): remit within 5 working days after payday; start first period within 7 business days of mailing; CCPA 50/60% + 5%.'}),
 ('deductions_garnishments','hi.garn.child_support.remit_working_days',5,'US-HIS5-022','2003-01-01',None,{'u':'working days','c':'medium'}),
 ('collective_agreements','hi.prevailing_wage.certified_payroll','weekly certified payroll + fringe-benefit form to contracting agency (GC for subs); records 3 years, produced within 10 days','US-HIS5-020','2026-01-01',None,{}),
 ('live_change','hi.live.act24_2026','in force (TA 2026-06, 2026-07-31): TY2027 2nd bracket 3.2 -> 2.5%, 3rd 5.5 -> 5%, new 13% top bracket; level assessment from TY2027 and withholding from 2027-01-01 once the 2027 Booklet A issues','US-HIS5-029','2026-07-31',None,{'c':'medium','n':'Act text gated (403) [US-HIS5-030]; HRS 235-51 snapshot superseded in part [US-HIS5-027 partial].'}),
 ('oracle','hi.oracle.booklet_a.part1.withholding_weekly',9.58,B,'2026-01-01','2026-12-31',{'u':U,'vm':'derived arithmetically','n':'Single, 3 allowances, 500/week: 26,000 - 3,432 - 4,350 = 18,218; 288 + 3,818 x 5.5% = 497.99; /52 = 9.58. Re-derived exactly.'}),
]
LEGACY = [('non_resident','hi.nonres.exempt_days',60,'US-HI-P5-1-002','2026-01-01',None,'Booklet A s.13: nonresident <= 60 days exempt with HW-6, paid from outside HI, regular workplace outside HI; HW-7 with original HW-6; never construction contractor employees. Resident = domicile or > 200 days. No reciprocity, no local tax [US-HIP9V-002].'),('collective_agreements','hi.prevailing_wage.threshold',2000,'US-HI-P5-2-002','2026-01-01',None,'HRS ch. 104 public-works construction over 2,000.')]
CITED = ['US-HIS5-002','US-HIS5-013','US-HIS5-016','US-HIS5-018','US-HIS5-025','US-HIS5-027','US-HIS5-028','US-HIS5-031','US-HI-002','US-HI-003','US-HIP7-002','US-HIP7-003','US-HIP9V-002','US-HIL-001','US-HIL-002','US-HIL-003','US-HIP9L-001','US-HIP9L-002','US-HI-P5-1-001','US-HI-P5-1-003','US-HI-P5-2-001']
NARR = {
 'income_tax': 'Withholding stops at 7.90%; the assessment schedule (HRS 235-51) continues to 8.25/9/10/11% above 175,000 single [US-HIS5-027, partial]. Withholding required on agricultural and domestic wages even where federal is not. Exclusions: MSRRA spouses; ministers; tips < 20/month; casual domestic; newspaper carriers < 18; interstate crew; convenience meals/lodging.',
 'social_security': 'No PFML (TDI only). Only employer levy is E&T. Schedule C minimum rate not transcribed (Q2).',
 'reporting_instruments': 'Registration BB-1 / Hawaii Tax Online. TDI and PHC via insurers, no state wage return. BLS 3020 for 10+ at secondary sites.',
 'data_protection': 'HRS 487J-2: no public display/mailing of full SSN (employer-employee mail allowed if not visible) [US-HIS5-028]. Full SSN on UC-B6, new hire, W-2/HW-2. Pay statement retention 6 years (388-7) [US-HI-P5-1-003 legacy].',
 'indexation': 'UI base AAW (nearest 100); TDI max weekly AAW/52 x 1.21; PHC 86.67 x MW; MW statutory steps; PIT statutory (Act 24 changes 2027).',
}
SPECIAL = '''- Domestic: withholding required unless casual (< 50 cash/quarter or not regular); UI at 1,000/quarter; casual domestic/companionship outside wage-hour law [US-HIS5-013].
- Agricultural: withholding required; UI excluded < 20,000/quarter and <= 9 workers/19 weeks; H-2A excluded; MW excludes farms < 20 and coffee harvesting [US-HIS5-013, US-HIS5-003].
- Minors: CL-1 (14-15) / eCL-3 (16-17); newspaper carriers < 18 outside withholding and UI [US-HIS5-025, US-HIS5-013].
- Tipped: tip credit 1.25 with MW + 7.00 test; withholding on reported tips >= 20/month; IRC 224 deduction at assessment [US-HIS5-001, US-HIS5-029].
- Clergy: no withholding; ordained church members outside UI [US-HIS5-013].
- Students: own-school, school-to-work, student nurses/interns outside UI [US-HIS5-013].
- NRAs: general nonresident rules (HW-6/60 days) and treaty exclusion.
- Statutory employees: commission insurance/real-estate/travel agents and direct sellers outside UI [US-HIS5-013].
- Government: federal/other-state service outside UI; State and counties outside PHC [US-HIS5-013, US-HIS5-016].
- Certified blind/deaf/disabled and MSRRA spouses: no withholding [US-HIS5-026].
- Construction contractor employees: no 60-day exemption. Crew: no withholding. Family employment outside UI.'''
LANG = 'No rule requires a non-English pay statement [US-HIL-001, US-HIL-002, US-HIP9L-001, US-HIP9L-002]; payslip English (US-OWN-006).'
UNRES = [
 {'key':'hi.wh.bracket.next_year','why':'TY2027 thresholds/cumulative amounts after Act 24 SLH 2026 and the 2027 withholding tables are unpublished; Act text gated (403).','close':'DOTAX 2027 Booklet A (tax.hawaii.gov/geninfo/a2_b2_4empl_whhold/, expected Dec 2026) or Act 24 text via browser pass. Do not derive from TA 2026-06 alone.','blocking':True},
 {'key':'hi.sui.employer.rate.min','why':'Minimum rate and full Schedule C table not in the page text (image Table 2).','close':'DLIR Table 2 on labor.hawaii.gov/ui/contribution-rates-explained/ or HRS 383-68 (Wayback).'},
 {'key':'hi.pit.conformity.list','why':'Full HRS 235-2.3(b) non-operative IRC list after Act 35 not read (HSA etc.).','close':'Act 35 SLH 2026 or HRS 235-2.3 as amended, or a DOTAX TIR on Act 35.'},
 {'key':'hi.report.w2.efw2_notes','why':'Hawaii-specific EFW2 RS requirements (Tax ID position) not read.','close':'DOTAX Publication EF-10 on tax.hawaii.gov/eservices/.'},
 {'key':'hi.report.sui.ucb6_format','why':'Bulk/file format for UC-B6 beyond online entry not located (gated).','close':'DLIR UI employer reporting instructions behind uiclaims.hawaii.gov or a DLIR wage-file spec.'},
 {'key':'hi.garn.state_tax_levy','why':'DOTAX wage levy not researched.','close':'HRS 231 read or DOTAX collections page.','blocking':False},
 {'key':'hi.tdi.multistate','why':'HRS 392-4/392-5 localization not read; recommendation: key TDI to sui_state = HI meanwhile.','close':'Wayback read of HRS 392-4 and 392-5.'},
 {'key':'hi.sui.wage_base.next_year','why':'December 2026 DLIR (UI base/schedule) and DCD (TDI) notices not yet published.','close':'DLIR 2027 Tax Rate Schedule page and DCD 2027 notice.'},
 {'key':'hi.payslip.items.register_alias','why':'The 14-item list of HRS 387-6(c) is carried by legacy row US-HI-P5-2-001; the fact cites US-HIS5-007 at medium confidence.','close':'Final merge: alias row for HRS 387-6(c) with S5-pattern id.','blocking':False},
]
