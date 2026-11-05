NAME = 'California'
SUMMARY = 'Minimum wage 16.90 (2026) / 17.40 (2027, DOF-certified); daily overtime and double time; semimonthly paydays. PIT withheld by EDD on DE 4 (Method A tables or Method B exact; 2026 brackets 1.1%-14.63%); supplemental flat 10.23% bonus/stock options and 6.6% other. UI 7,000 base (employer only, new 3.4%), ETT 0.1%, SDI 1.3% employee with no wage cap (2027 rate unpublished). Lab. Code 226 nine-item wage statement plus sick-leave balance. DE 9/DE 9C quarterly, W-2 not filed with EDD. Local minimum wages not registered (fan-out).'
U = 'USD'
M = 'US-CAS5-001'
FACTS = [
 ('labour_code','ca.minwage.hourly',16.90,'US-CAS5-006','2026-01-01','2026-12-31',{'u':U,'n':'All employers; learners 85% for first 160 hours.'}),
 ('labour_code','ca.minwage.hourly',17.40,'US-CAS5-007','2027-01-01',None,{'u':U,'vm':'second independent authority','n':'DOF certified 2026-07-31 (+2.99%); DIR News 2026-66 + Governor release. Check 16.90 x 1.0299 = 17.405 -> 17.40.'}),
 ('labour_code','ca.minwage.learner.percent',85,'US-CAS5-006','2026-01-01',None,{'u':'percent','n':'First 160 hours of employment.'}),
 ('labour_code','ca.exempt.salary.annual_min',70304,'US-CAS5-006','2026-01-01','2026-12-31',{'u':U,'vm':'derived arithmetically','n':'2 x 16.90 x 2,080.'}),
 ('labour_code','ca.exempt.salary.annual_min',72384,'US-CAS5-007','2027-01-01',None,{'u':U,'n':'Quoted by DIR (= 2 x 17.40 x 2,080).'}),
 ('labour_code','ca.overtime.rule','1.5x over 8 h/day, over 40 h/week and first 8 h of 7th consecutive day; 2x over 12 h/day and over 8 h on 7th day (Lab. Code 510); alternative workweek exceptions','US-CAS5-008','2026-01-01',None,{}),
 ('labour_code','ca.overtime.daily_threshold_hours',8,'US-CAS5-008','2026-01-01',None,{'u':'hours'}),
 ('labour_code','ca.overtime.double_time_daily_threshold_hours',12,'US-CAS5-008','2026-01-01',None,{'u':'hours'}),
 ('labour_code','ca.pay_frequency.rule','twice a month: 1st-15th paid 16th-26th; 16th-end paid 1st-10th next month; EAP monthly by 26th; weekly/biweekly/semimonthly within 7 days of period close; OT by next regular payday (Lab. Code 204)','US-CAS5-009','2026-01-01',None,{}),
 ('labour_code','ca.direct_deposit.requires_voluntary_authorisation',True,'US-CAS5-009','2026-01-01',None,{'n':'Lab. Code 213(d).'}),
 ('income_tax','ca.wh.certificate.form','DE 4 Rev. 56 (1-26); federal W-4 for FIT only since 2020; no valid DE 4 = Single 0 allowances; exempt status renewed by Feb 15','US-CAS5-015','2026-01-01',None,{}),
 ('income_tax','ca.wh.method','Method A (wage-bracket tables, wages < 1M) or Method B (exact calculation), DE 44 Rev. 52 (4-26)',M,'2026-01-01',None,{}),
 ('income_tax','ca.wh.low_income_exemption.single',18896,M,'2026-01-01','2026-12-31',{'u':U,'n':'Single / Married 0-1 allowances; Married 2+ / HoH 37,791.'}),
 ('income_tax','ca.wh.low_income_exemption.married_2plus_hoh',37791,M,'2026-01-01','2026-12-31',{'u':U}),
 ('income_tax','ca.wh.std_deduction.single',5706,M,'2026-01-01','2026-12-31',{'u':U}),
 ('income_tax','ca.wh.std_deduction.married_2plus_hoh',11412,M,'2026-01-01','2026-12-31',{'u':U}),
 ('income_tax','ca.wh.allowance_credit.per_allowance',168.30,M,'2026-01-01','2026-12-31',{'u':U}),
 ('income_tax','ca.wh.estimated_deduction.per_allowance',1000,M,'2026-01-01','2026-12-31',{'u':U}),
]
sb = [(1.1,11079),(2.2,26264),(4.4,41452),(6.6,57542),(8.8,72724),(10.23,371479),(11.33,445771),(12.43,742953),(13.53,1000000)]
for i,(r,c) in enumerate(sb,1):
    FACTS.append(('income_tax',f'ca.pit.bracket.single.{i}.rate',r,M,'2026-01-01','2026-12-31',{'u':'percent'}))
    FACTS.append(('income_tax',f'ca.pit.bracket.single.{i}.ceiling',c,M,'2026-01-01','2026-12-31',{'u':U}))
FACTS += [
 ('income_tax','ca.pit.bracket.single.10.rate',14.63,M,'2026-01-01','2026-12-31',{'u':'percent','n':'Over 1,000,000 (base 114,220.27).'}),
 ('income_tax','ca.pit.brackets.married.ceilings','22,158 / 52,528 / 82,904 / 115,084 / 145,448 / 742,958 / 891,542 / 1,000,000 / 1,485,906; 14.63% over; base 164,228.58',M,'2026-01-01','2026-12-31',{'n':'Rates per DE 44 Method B Married table (read the table, not this summary, for the rate attached to each band around the 1,000,000 kink).'}),
 ('income_tax','ca.pit.brackets.hoh.ceilings','22,173 / 52,530 / 67,716 / 83,805 / 98,990 / 505,208 / 606,251 / 1,000,000 / 1,010,417; base 107,334.77',M,'2026-01-01','2026-12-31',{'n':'Rates per DE 44 Method B HoH table.'}),
 ('income_tax','ca.wh.supplemental.rate.bonus_stock_options',10.23,'US-CAS5-004','2026-01-01',None,{'u':'percent','n':'When paid separately: aggregate or flat; with regular wages: aggregate.'}),
 ('income_tax','ca.wh.supplemental.rate.other',6.6,'US-CAS5-004','2026-01-01',None,{'u':'percent','n':'Overtime, commissions, severance, vacation pay etc. paid separately.'}),
 ('income_tax','ca.wh.household.by_agreement_only',True,'US-CAS5-004','2026-01-01',None,{}),
 ('non_resident','ca.nonres.sourcing','residents: all wages with credit for other-state withholding (withhold excess only); nonresidents wholly in CA: all wages; split-state: CA working days / total working days (volume ratio for commissions); military spouse exclusion on DE 4','US-CAS5-004','2026-01-01',None,{'n':'No reciprocity agreement and no local wage tax in the full DE 44 scan [US-CA-EDD-005, legacy id].'}),
 ('social_security','ca.sui.wage_base',7000,'US-CAS5-016','2026-01-01',None,{'u':U,'n':'Kept for 2027.'}),
 ('social_security','ca.sui.new_employer.rate',3.4,'US-CAS5-016','2026-01-01',None,{'u':'percent','c':'medium','n':'2-3 years; range 1.5%-6.2% (Schedule F+ incl. 15% emergency surcharge, US-CAP7-003); employer only; max 434/employee.'}),
 ('social_security','ca.sui.employer.rate.min',1.5,'US-CAP7-003','2026-01-01','2026-12-31',{'u':'percent'}),
 ('social_security','ca.sui.employer.rate.max',6.2,'US-CAP7-003','2026-01-01','2026-12-31',{'u':'percent'}),
 ('social_security','ca.ett.rate',0.1,'US-CAP7-001','2026-01-01',None,{'u':'percent','n':'On first 7,000 (max 7/employee); same 2027 [US-CAS5-016].'}),
 ('social_security','ca.sdi.employee.rate',1.3,'US-CAP7-002','2026-01-01','2026-12-31',{'u':'percent','n':'Includes PFL; no wage cap since 2024-01-01 (SB 951); no employer share. A WebFetch summary saying 1.4% is WRONG. 2027 rate unpublished (open).'}),
 ('social_security','ca.sdi.wage_cap.exists',False,'US-CAP7-002','2024-01-01',None,{}),
 ('social_security','ca.sdi.voluntary_plan.w2_box14_label','VPDI','US-CAS5-018','2026-01-01',None,{}),
 ('payslip_statute','ca.payslip.items','gross wages; total hours (not salaried exempt); piece-rate units and rates; deductions; net wages; pay-period dates; employee name + last 4 SSN or employee ID; employer legal name and address; every hourly rate with hours','US-CAS5-005','2026-01-01',None,{'n':'Lab. Code 226(a); semimonthly or with each payment; household excluded (226(d)); public employers only SSN rule (226(i)).'}),
 ('payslip_statute','ca.payslip.sick_leave_balance.required',True,'US-CAS5-011','2026-01-01',None,{'n':'On the statement or a separate writing each payday (Lab. Code 246(i)).'}),
 ('payslip_statute','ca.payslip.inspection_response_days',21,'US-CAS5-005','2026-01-01',None,{'u':'days'}),
 ('payslip_statute','ca.payslip.penalty.max',4000,'US-CAS5-005','2026-01-01',None,{'u':U,'n':'50 first / 100 subsequent per violation up to 4,000; 750 for failing an inspection request.'}),
 ('data_protection','ca.records.wage_statement.retention_years',3,'US-CAS5-005','2026-01-01',None,{'u':'years'}),
 ('data_protection','ca.records.edd_payroll.retention_years',4,'US-CAS5-003','2026-01-01',None,{'u':'years','n':'8 years for non-employee payments.'}),
 ('data_protection','ca.ccpa.request_response_days',45,'US-CAS5-021','2023-01-01',None,{'u':'days','c':'medium','n':'Extendable to 90; employee data in scope since 2023-01-01 (A.3).'}),
 ('reporting_instruments','ca.registration.de1.trigger',100,'US-CAS5-002','2026-01-01',None,{'u':U,'n':'DE 1 within 15 days after paying more than 100 in wages in a quarter; DE 1P PIT-only.'}),
 ('reporting_instruments','ca.report.deposit.de88','follows federal schedule: next-day if accumulated PIT > 400; semi-weekly; monthly by 15th if >= 350; quarterly if < 350; EFT by 3rd business day; 15% failure-to-deposit penalty','US-CAS5-002','2026-01-01',None,{}),
 ('reporting_instruments','ca.report.quarterly.de9_de9c','DE 9 + DE 9C electronic only, zero returns filed; due Apr 1/Jul 1/Oct 1/Jan 1, delinquent after Apr 30, Jul 31, Nov 2 2026, Feb 1 2027; DE 9C per employee subject wages, PIT wages, PIT withheld; corrections DE 9ADJ','US-CAS5-002','2026-01-01',None,{}),
 ('reporting_instruments','ca.report.w2.filed_with_state',False,'US-CAS5-018','2026-01-01',None,{'n':'W-2 to employees by 2027-02-01: box 14 CASDI, 16 CA PIT wages, 17 CA PIT withheld; not filed with EDD/FTB. No separate annual reconciliation.'}),
 ('reporting_instruments','ca.newhire.report_days',20,'US-CAS5-018','2026-01-01',None,{'u':'days','n':'DE 34 from start-of-work date; rehire after separation of 60+ days; contractors DE 542 at 600+.'}),
 ('leave','ca.leave.sick.accrual.hours_worked_per_hour',30,'US-CAS5-011','2024-01-01',None,{'u':'hours','n':'Lab. Code 246 (SB 616): eligible after 30 days; alternative 24 h by day 120 and 40 h by day 200; use from day 90; usage cap 40 h/5 days; balance cap 80 h/10 days; front-load 40 h; reinstated on rehire within 1 year; regular rate or 90-day average; increment max 2 h.'}),
 ('leave','ca.leave.sick.usage_cap_hours',40,'US-CAS5-011','2024-01-01',None,{'u':'hours'}),
 ('leave','ca.leave.sick.accrual_cap_hours',80,'US-CAS5-011','2024-01-01',None,{'u':'hours'}),
 ('leave','ca.leave.sick.payout_on_separation',False,'US-CAS5-011','2024-01-01',None,{}),
 ('termination','ca.final_pay.discharge','immediately (72 h for seasonal perishable-food layoffs); quit: within 72 h or last day with 72 h notice; waiting-time penalty 1 day wages per day up to 30 days','US-CAS5-010','2026-01-01',None,{}),
 ('termination','ca.final_pay.waiting_time_penalty_max_days',30,'US-CAS5-010','2026-01-01',None,{'u':'days'}),
 ('termination','ca.final_pay.vested_vacation_payout',True,'US-CAS5-010','2026-01-01',None,{'n':'Lab. Code 227.3: paid at final rate; forfeiture prohibited.'}),
 ('termination','ca.separation_notice','CUIC 1089 Notice to Employee as to Change in Relationship + DE 2320 at discharge, layoff or leave; email only with opt-in','US-CAS5-018','2026-01-01',None,{}),
 ('termination','ca.warn.notice_days',60,'US-CAS5-018','2026-01-01',None,{'u':'days','n':'Cal-WARN Lab. Code 1400-1408; 75-employee threshold not quoted (open).'}),
 ('benefits_in_kind','ca.hsa.conforms',False,'US-CAS5-019','2026-01-01',None,{'n':'Employer and employee HSA contributions subject to UI/ETT, SDI and PIT (not UI/SDI via cafeteria plan); employer HSA (W-2 code W) added back for PIT [US-CAS5-020].'}),
 ('benefits_in_kind','ca.wages.401k_deferrals','UI/SDI subject; PIT not subject','US-CAS5-019','2026-01-01',None,{}),
 ('benefits_in_kind','ca.wages.gtl_over_50k','UI/SDI not subject; PIT not withheld but reportable','US-CAS5-019','2026-01-01',None,{}),
 ('benefits_in_kind','ca.obbba.conforms',False,'US-CAS5-020','2026-01-01',None,{'n':'No state tips or overtime deduction.'}),
 ('benefits_in_kind','ca.meals.value.per_day',15.85,'US-CAS5-003','2026-01-01','2026-12-31',{'u':U,'n':'Breakfast 3.25, lunch 4.90, dinner 7.70, unidentified 5.70.'}),
 ('benefits_in_kind','ca.meals.value.breakfast',3.25,'US-CAS5-003','2026-01-01','2026-12-31',{'u':U}),
 ('benefits_in_kind','ca.meals.value.lunch',4.90,'US-CAS5-003','2026-01-01','2026-12-31',{'u':U}),
 ('benefits_in_kind','ca.meals.value.dinner',7.70,'US-CAS5-003','2026-01-01','2026-12-31',{'u':U}),
 ('benefits_in_kind','ca.lodging.value.min_weekly',66.10,'US-CAS5-003','2026-01-01','2026-12-31',{'u':U,'n':'66 2/3% of rental value, min 66.10/week, max 2,038/month.'}),
 ('benefits_in_kind','ca.lodging.value.max_monthly',2038,'US-CAS5-003','2026-01-01','2026-12-31',{'u':U}),
 ('deductions_garnishments','ca.garn.creditor.max_percent',20,'US-CAS5-013','2026-01-01',None,{'u':'percent','n':'WG-002 Rev. 2026-01-01: lesser of 20% of disposable earnings or 40% of disposable earnings above minimum wage x 48 (weekly) / 96 (biweekly) / 104 (semimonthly) / 208 (monthly); local MW if higher; support first.'}),
 ('deductions_garnishments','ca.garn.creditor.excess_percent',40,'US-CAS5-013','2026-01-01',None,{'u':'percent'}),
 ('deductions_garnishments','ca.garn.creditor.minwage_multiple.weekly',48,'US-CAS5-013','2026-01-01',None,{'u':'ratio'}),
 ('deductions_garnishments','ca.garn.child_support.cap_percent',50,'US-CAS5-022','2026-01-01',None,{'u':'percent','n':'50% after taxes; remit to SDU within 7 business days of pay date electronically (Fam. Code 17309.5); IWO kept 1 year after separation.'}),
 ('deductions_garnishments','ca.garn.child_support.remit_business_days',7,'US-CAS5-022','2026-01-01',None,{'u':'business days'}),
 ('deductions_garnishments','ca.deductions.tip_credit.allowed',False,'US-CAS5-012','2026-01-01',None,{'n':'Lab. Code 224, 351: deductions only if required by law or authorised in writing; no tip credit; card tips without processing fees.'}),
 ('collective_agreements','ca.prevailing_wage.certified_payroll','electronic to Labor Commissioner via DIR eCPR (XML upload spec available)','US-CAS5-017','2026-01-01',None,{}),
 ('live_change','ca.live.ab1514_manicurists','Borello test reinstated for licensed manicurists 2026-01-01 to 2028-12-31; commercial-fisher exception extended','US-CAS5-016','2026-01-01','2028-12-31',{}),
 ('live_change','ca.delinquent_tax.interest_rate',7,'US-CAS5-016','2026-01-01','2026-12-31',{'u':'percent'}),
 ('oracle','ca.oracle.de44.example_f.withholding_monthly',7.17,M,'2026-01-01','2026-12-31',{'u':U,'vm':'derived arithmetically','n':'DE 44 Method B example F: annual 57,000 married 4 allowances; 57,000 - 11,412 = 45,588 -> 243.74 + 2.2% x 23,430 = 759.20 - 673.20 = 86.00/yr = 7.17/month. Reproduced in Python.'}),
 ('oracle','ca.oracle.de44.example_e.withholding_semimonthly',4.13,M,'2026-01-01','2026-12-31',{'u':U,'vm':'derived arithmetically','n':'DE 44 Method B example E, reproduced in Python. Single cumulative bases also re-derive (121.87 ... 114,220.27); 34,084.81 derives as 34,084.80 (intermediate rounding residual 0.01).'}),
 ('oracle','ca.oracle.suite','DE 44 Rev. 52 (4-26) Method B examples A-F',M,'2026-01-01','2026-12-31',{}),
]
LEGACY = []
CITED = ['US-CA-EDD-001','US-CA-EDD-004','US-CA-EDD-005','US-CA-EDD-006','US-CA-LAB-001','US-CA-PW-001','US-CAP6-001','US-CAS5-014']
NARR = {
 'labour_code': 'Local minimum wages: cities/counties may set higher rates (most favourable applies); DIR keeps no list and the Berkeley inventory is tier B, so no local rate is registered (open, fan-out). Industry minimums (fast food, SB 525 health care) not fetched.',
 'collective_agreements': 'State prevailing wage on public works (Lab. Code 1720, 1771) [US-CA-PW-001 legacy]. CBAs may override Lab. Code 204, 227.3 and 510 alternative workweeks.',
 'indexation': 'Minimum wage CPI-indexed, DOF certifies by Aug 1 (Lab. Code 1182.12(d)); exempt threshold 2 x MW x 2,080; PIT tables indexed yearly in DE 44; UI base fixed 7,000; SDI set yearly; meals/lodging yearly; EWO thresholds follow MW.',
 'live_change': '2027 SDI rate and 2027 PIT schedules not yet published (December). DE 2088 rate notices by 2026-12-31. All items in force or enacted; no ruling or draft bill.',
}
SPECIAL = '''- Domestic/household: UI/ETT at 1,000 cash in a quarter; SDI at 750 in a quarter; PIT only by agreement; Lab. Code 226 statement does not apply [US-CAS5-014, US-CAS5-004, US-CAS5-005].
- Agricultural: UI/ETT/SDI subject; PIT withholding not required but PIT wages reportable; H-2A same; AB 1066 phase-in not fetched [US-CAS5-014].
- Minors: learner 85% rule any age; newspaper carriers under 18 excluded from UI/SDI/PIT [US-CAS5-006, US-CAS5-014].
- Tipped: no tip credit [US-CAS5-012, US-CAS5-006].
- Clergy: ministers/religious orders UI/SDI not subject (elective), PIT withholding not required; church employees UI/SDI not subject, PIT subject [US-CAS5-014, US-CAS5-003].
- Students: own-school students, student nurses, work-study under 22, organized-camp students: UI/SDI not subject, PIT subject [US-CAS5-014].
- Nonresident aliens F/J/M/Q: excluded from UI/SDI (CUIC 608); PIT subject unless treaty covers state taxes [US-CAS5-014].
- Statutory employees: UI/SDI covered per DE 231TE/SE; commissioned authors no PIT withholding [US-CAS5-014].
- Government: UI subject, SDI not unless elective, PIT subject; elected officials/judiciary/National Guard UI/SDI not subject [US-CAS5-014, US-CAS5-005].'''
LANG = 'Lab. Code 2810.5 hire notice in the language the employer normally uses [US-CAP6-001]; payslip English (US-OWN-006). CA postings page unreadable (recorded limit).'
UNRES = [
 {'key':'ca.local_minwage.hourly','why':'Local minimum wages (LA City/County, SF, San Jose, Oakland, Berkeley, etc.) are not kept by DIR; only a tier-B inventory exists.','close':'Each city labor-standards office bulletin (LA OWS, SF OLSE, ...) for 2026-07-01 and 2027-01-01 rates; parallel fan-out per city.','blocking':True},
 {'key':'ca.industry_minwage.fast_food_health_care','why':'Fast-food (Lab. Code 1474) and health-care (SB 525) minimums not fetched.','close':'DIR fast-food and health-care minimum wage FAQ pages.','blocking':True},
 {'key':'ca.sdi.employee.rate.next_year','why':'2027 SDI rate not on EDD at read time; tier-B 1.4% projection not used.','close':'EDD Rates and Withholding page or DE 44 2027 (normally December 2026).'},
 {'key':'ca.payslip.electronic_consent','why':'Statute says "in writing"; no electronic-consent rule fetched.','close':'DLSE opinion letter or DIR paydays FAQ on electronic wage statements.'},
 {'key':'ca.report.de9c.file_format','why':'DE 9C/DE 34 electronic file specification not fetched (Stage-3 gap).','close':'EDD e-Services for Business File Transfer spec / DE 9C and DE 34 layouts.'},
 {'key':'ca.sdi.benefit.weekly_max','why':'2026 DI/PFL weekly benefit maximum and replacement rates not fetched.','close':'EDD Quick Statistics page.','blocking':False},
 {'key':'ca.warn.employer_threshold','why':'Cal-WARN 75-employee coverage threshold not quoted from an authority page.','close':'Lab. Code 1400 text or EDD WARN employer page.'},
 {'key':'ca.hsa.conformity_2026','why':'A search summary claims employer HSA contributions excluded 2026-2030; not verified.','close':'Enacted bill on leginfo, FTB 2026 Schedule CA instructions or FTB What\'s New.'},
 {'key':'ca.garn.child_support.employer_fee','why':'Employer fee per payment and FTB/EDD order-to-withhold priority not verified.','close':'Family Code 5235 text and FTB "Earnings Withholding Order for Taxes" employer instructions.'},
 {'key':'ca.prevailing_wage.thresholds','why':'Public-works 1,000 threshold and small-project eCPR exemptions not quoted.','close':'Lab. Code 1725.5 / 1771 / 1773.3 text or DIR registration FAQ.'},
 {'key':'ca.overtime.agricultural_phase_in','why':'AB 1066 agricultural overtime phase-in and child-labour permits not fetched.','close':'Lab. Code 860-864 text and DIR agricultural overtime FAQ.'},
]
