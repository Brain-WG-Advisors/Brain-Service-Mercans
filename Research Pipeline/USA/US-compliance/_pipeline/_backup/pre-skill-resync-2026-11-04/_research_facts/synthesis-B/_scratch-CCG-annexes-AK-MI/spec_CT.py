NAME = 'Connecticut'
SUMMARY = 'Minimum wage 16.94 (2026) / 17.48 (2027), ECI-indexed; weekly overtime only. Withholding by TPG-211 rules or DRS tables (codes A-F on CT-W4; 6.99% with no CT-W4); no supplemental flat rate; no reciprocity; 15-day rule; convenience rule. UI base 27,000 (ECI-indexed), new employer 1.9%, 1.0% fund solvency tax; CT Paid Leave 0.5% employee on wages to 184,500. Pay record with explicit e-consent; pay-code guide URL on every pay record for 100+ employers from 2026-10-01. Oracle: IP 2026(1) Examples 8-10 (table-based).'
U = 'USD'
T = 'US-CTS5-010'
FACTS = [
 ('labour_code','ct.minwage.hourly',16.94,'US-CTS5-008','2026-01-01','2026-12-31',{'u':U,'n':'G-DERIVE: 16.35 x 1.036 (ECI) = 16.9386 -> 16.94 (Decimal ROUND_HALF_UP).'}),
 ('labour_code','ct.minwage.hourly',17.48,'US-CTS5-009','2027-01-01',None,{'u':U,'n':'Announced; 16.94 x 1.032 = 17.48208 -> 17.48.'}),
 ('labour_code','ct.minwage.indexation','every 1 January by ECI (wages and salaries, all civilian workers) for 12 months to preceding 30 June, nearest cent; announced by 15 October; never below federal MW + 0.5%','US-CTS5-001','2023-06-01',None,{}),
 ('labour_code','ct.overtime.weekly_threshold_hours',40,'US-CTS5-003','2026-01-01',None,{'u':'hours','n':'1.5x; no daily OT; fluctuating workweek allowed except certain delivery drivers/sales merchandisers.'}),
 ('labour_code','ct.pay_frequency.rule','weekly or biweekly regular payday designated in advance; period ends no more than 8 days before payday; Commissioner waiver never less than monthly','US-CTS5-004','2026-01-01',None,{}),
 ('labour_code','ct.payment.method','cash or check; direct deposit only at employee written/electronic request; payroll card only if DD and check also offered and employee authorises voluntarily (31-71k)','US-CTS5-004','2026-01-01',None,{}),
 ('labour_code','ct.tipped.employer_share.hotel_restaurant',6.38,'US-CTS5-002','2026-01-01',None,{'u':U,'n':'Fixed employer cash wage; max tip credit 2026 10.56 (16.94-6.38), 2027 11.10. Bartenders 8.23 (credit 8.71 / 9.25). Other industries credit max 0.35. Meals 0.85 full / 0.45 light. No cannabis tip credit from 2026-10-01 (PA 26-12 s.6) [US-CTS5-028].'}),
 ('labour_code','ct.tipped.employer_share.bartender',8.23,'US-CTS5-002','2026-01-01',None,{'u':U}),
 ('labour_code','ct.tipped.max_tip_credit.hotel_restaurant',10.56,'US-CTS5-002','2026-01-01','2026-12-31',{'u':U,'vm':'derived arithmetically','n':'16.94 - 6.38.'}),
 ('labour_code','ct.minwage.minor.hourly',14.40,'US-CTS5-001','2026-01-01','2026-12-31',{'u':U,'vm':'derived arithmetically','n':'Under 18 not emancipated: greater of 85% of MW (first 90 days) or 10.10: 0.85 x 16.94 = 14.40 (2027: 14.86).'}),
 ('income_tax','ct.wh.method','TPG-211 2026 Withholding Calculation Rules (Rev. 12/25) or DRS tables (IP 2026(1)); no percentage method; 2026 rules/tables unchanged from 2025',T,'2026-01-01','2026-12-31',{'n':'Steps: annualise; less Table A exemption; Table B rates; + Table C phase-out add-back + Table D recapture; x (1 - Table E credit); / periods; + CT-W4 line 2 - line 3. Extract Table E with word-level PyMuPDF, never pdftotext -layout (drops bounds).'}),
 ('income_tax','ct.wh.table_a.exemption.a',12000,T,'2026-01-01','2026-12-31',{'u':U,'n':'A 12,000; B 19,000; C 24,000; F 15,000; D 0; phases out 1,000 per 1,000 of income.'}),
 ('income_tax','ct.wh.table_a.exemption.b',19000,T,'2026-01-01','2026-12-31',{'u':U}),
 ('income_tax','ct.wh.table_a.exemption.c',24000,T,'2026-01-01','2026-12-31',{'u':U}),
 ('income_tax','ct.wh.table_a.exemption.f',15000,T,'2026-01-01','2026-12-31',{'u':U}),
 ('income_tax','ct.pit.rates','2.0 / 4.5 / 5.5 / 6.0 / 6.5 / 6.9 / 6.99 percent',T,'2026-01-01','2026-12-31',{}),
 ('income_tax','ct.pit.bracket_breaks.a_d_f','10,000 / 50,000 / 100,000 / 200,000 / 250,000 / 500,000',T,'2026-01-01','2026-12-31',{}),
 ('income_tax','ct.pit.bracket_breaks.b','16,000 / 80,000 / 160,000 / 320,000 / 400,000 / 800,000',T,'2026-01-01','2026-12-31',{}),
 ('income_tax','ct.pit.bracket_breaks.c','20,000 / 100,000 / 200,000 / 400,000 / 500,000 / 1,000,000',T,'2026-01-01','2026-12-31',{}),
 ('income_tax','ct.wh.no_certificate.rate',6.99,'US-CTS5-011','2026-01-01',None,{'u':'percent','n':'No CT-W4: flat 6.99% without exemption; code E expires 15 Feb, then 6.99% from 16 Feb.'}),
 ('income_tax','ct.wh.certificate.form','CT-W4 (Rev. 12/25), codes A/B/C/D/E/F; exempt certificates to DRS above 36,000 MFS / 45,000 S / 57,000 HoH / 72,000 MFJ; MSRRA with LES','US-CTS5-011','2025-12-01',None,{}),
 ('income_tax','ct.wh.supplemental.method','aggregate only (no flat supplemental rate)','US-CTS5-012','2026-01-01',None,{}),
 ('income_tax','ct.wh.pension_lump_sum.suspension','withholding on lump-sum retirement distributions suspended 2025-07-01 to 2026-12-31 (CT-W4P on request)',T,'2025-07-01','2026-12-31',{}),
 ('non_resident','ct.nonres.rules','residents: all wages, prorated where another qualifying jurisdiction requires withholding; nonresidents: CT-service wages via CT-W4NA or records, else all wages; 15-day rule; no reciprocity; convenience-of-employer rule from 2019 (reciprocal)','US-CTP10-001','2026-01-01',None,{}),
 ('social_security','ct.sui.wage_base',27000,'US-CTP9V-001','2026-01-01','2026-12-31',{'u':U,'n':'G-DERIVE: 26,100 x 1.036 = 27,039.6 -> 27,000 (nearest 100) [US-CTS5-016]. 2027 derived 27,900 is a projection only (DOL page 404): not a fact.'}),
 ('social_security','ct.sui.new_employer.rate',1.9,'US-CTP9V-001','2026-01-01','2026-12-31',{'u':'percent'}),
 ('social_security','ct.sui.employer.rate.min',0.1,'US-CTP9V-001','2026-01-01','2026-12-31',{'u':'percent','n':'Charged 0.1-8.9% plus 1.0% fund solvency (combined 1.1-9.9%).'}),
 ('social_security','ct.sui.employer.rate.max',8.9,'US-CTP9V-001','2026-01-01','2026-12-31',{'u':'percent'}),
 ('social_security','ct.sui.fund_solvency.rate',1.0,'US-CTP9V-001','2026-01-01','2026-12-31',{'u':'percent'}),
 ('social_security','ct.sui.employee.rate',0,'US-CTS5-031','2026-01-01',None,{'u':'percent','c':'medium'}),
 ('social_security','ct.sui.wage_base.other_state_credit',True,'US-CTS5-016','2026-01-01',None,{'n':'31-222(b); each concurrent employer reports to the max; predecessor wages only for successor.'}),
 ('social_security','ct.pfml.employee.rate',0.5,'US-CTP7-001','2026-01-01','2026-12-31',{'u':'percent','n':'Statutory cap 0.5%; subject earnings = UI total wages excl. FICA-excluded benefits; each employer withholds to cap separately; no employer share.'}),
 ('social_security','ct.pfml.wage_cap',184500,'US-CTP7-001','2026-01-01','2026-12-31',{'u':U,'n':'= SS wage base.'}),
 ('social_security','ct.pfml.benefit.weekly_max',1016.40,'US-CTS5-020','2026-01-01','2026-12-31',{'u':U,'vm':'derived arithmetically','n':'60 x 16.94; 2027 60 x 17.48 = 1,048.80. Paid by the Authority, not payroll.'}),
 ('social_security','ct.pfml.multistate','employee for whom employer pays CT UI and CT payroll taxes is working in CT (follows UI localization)','US-CTS5-035','2026-01-01',None,{'c':'medium'}),
 ('payslip_statute','ct.payslip.items','hours worked, gross pay with straight time and overtime separately, itemised deductions, net pay (hours/split not for OT-exempt); electronic only with explicit consent and secure access','US-CTS5-027','2026-01-01',None,{}),
 ('payslip_statute','ct.payslip.pay_code_guide_url.employer_threshold',100,'US-CTS5-028','2026-10-01',None,{'u':'employees','n':'PA 26-12 s.38 (31-13a(c)): guide (>=10 codes, en/es/other common languages, dispute contact) URL on every pay record and at hire. Consolidated 31-13a text lags (F18): cite PA 26-12.'}),
 ('data_protection','ct.records.retention_years',3,'US-CTS5-027','2026-01-01',None,{'u':'years','n':'31-66, at place of employment.'}),
 ('reporting_instruments','ct.report.wh.remitter_class','weekly if lookback > 10,000 (Wednesday after Sat-Fri week); monthly 2,000-10,000 (15th); quarterly <= 2,000 (last day of month after quarter); all via myconneCT EFT','US-CTS5-013','2026-01-01',None,{}),
 ('reporting_instruments','ct.report.wh.ct941','quarterly due 4/30, 7/31, 10/31, 1/31 even if zero; annual status on request by 31 March','US-CTS5-013','2026-01-01',None,{}),
 ('reporting_instruments','ct.report.w2.ctw3','CT-W3 + all W-2s by 31 January via myconneCT (key-and-send, EFW2 upload or DRS CSV); box 15 CT + registration number; 5 per return up to 2,000','US-CTS5-013','2026-01-01',None,{}),
 ('reporting_instruments','ct.report.sui.quarterly','ReEmployCT electronic (manual, upload, TPA, FSET); due 4/30, 7/31, 10/31, 1/31; 276-char fixed-length S/T records; zero report required; late file 25, late pay greater of 50 or 10%','US-CTS5-032','2026-01-01',None,{'n':'Optional occupation/hours/worksite ZIP from Q3 2026 (31-225a(j)(1)(B)) [US-CTS5-018] have no positions in the 2022 spec.'}),
 ('reporting_instruments','ct.report.sui.record_length',276,'US-CTS5-032','2022-01-01',None,{'u':'characters'}),
 ('reporting_instruments','ct.newhire.report_days',20,'US-CTS5-019','2026-01-01',None,{'u':'days','n':'Rehire = separated > 60 days; copy of CT-W4, DOL website or fax.'}),
 ('reporting_instruments','ct.report.pfml.quarterly','My Account portal or batch SFTP XML/CSV; due last day of the quarter, no penalty if paid by last day of following month','US-CTS5-022','2026-01-01',None,{}),
 ('leave','ct.leave.sick.coverage_threshold_employees',11,'US-CTS5-021','2026-01-01','2026-12-31',{'u':'employees','n':'CT headcount for week containing 1 Jan; 1+ from 2027-01-01.'}),
 ('leave','ct.leave.sick.coverage_threshold_employees',1,'US-CTS5-021','2027-01-01',None,{'u':'employees'}),
 ('leave','ct.leave.sick.accrual.hours_worked_per_hour',30,'US-CTS5-021','2026-01-01',None,{'u':'hours','n':'Cap 40 h/yr; carryover 40; use from day 120; pay greater of normal wage or MW; no payout; seasonal <= 120 days excluded.'}),
 ('leave','ct.leave.sick.cap_hours',40,'US-CTS5-021','2026-01-01',None,{'u':'hours'}),
 ('leave','ct.leave.sick.use_after_days',120,'US-CTS5-021','2026-01-01',None,{'u':'days'}),
 ('termination','ct.final_pay.rule','discharge: business day after; quit/layoff: next regular payday','US-CTS5-005','2026-01-01',None,{'n':'Vacation/PTO payout only if policy/CBA provides (31-76k). Double damages for unpaid wages from 2027-01-01 (PA 26-12 s.56) [US-CTS5-028].'}),
 ('termination','ct.separation_notice','UC-21 Separation Packet with UC-21A to every separating employee','US-CTS5-031','2026-01-01',None,{}),
 ('deductions_garnishments','ct.deductions.rule','only if required by law, written authorisation on a Labor Commissioner-approved form, medical/hospital without employer benefit, auto-enrolment retirement/CRSP, or another state withholding requirement','US-CTS5-006','2026-01-01',None,{}),
 ('deductions_garnishments','ct.garn.creditor.max_percent',25,'US-CTS5-024','2026-01-01',None,{'u':'percent','n':'52-361a: lesser of 25% of disposable earnings or excess over 40 x higher of federal/CT MW; 20-day stay; one execution at a time.'}),
 ('deductions_garnishments','ct.garn.creditor.weekly_protected',677.60,'US-CTS5-024','2026-01-01','2026-12-31',{'u':U,'vm':'derived arithmetically','n':'40 x 16.94; 2027 699.20.'}),
 ('deductions_garnishments','ct.garn.child_support.remit_business_days',7,'US-CTS5-025','2026-01-01',None,{'u':'business days','n':'52-362: exempt greater of 85% of first 145/week disposable or CCPA amount; start first period after 14 days; SDU pro-rates, current support first.'}),
 ('collective_agreements','ct.prevailing_wage.threshold.new_construction',1000000,'US-CTS5-023','2026-01-01',None,{'u':U,'n':'Remodeling/repair 100,000; weekly certified payroll to contracting agency (failure class D felony).'}),
 ('collective_agreements','ct.prevailing_wage.threshold.remodel',100000,'US-CTS5-023','2026-01-01',None,{'u':U}),
 ('oracle','ct.oracle.ip2026_1.ex8.withholding',17.65,'US-CTS5-011','2026-01-01','2026-12-31',{'u':U,'c':'medium','n':'IP 2026(1) Ex. 8: code F, 700 weekly (table-based). TPG-211 rules give 17.79 (residual 0.14).'}),
 ('oracle','ct.oracle.ip2026_1.ex9.withholding',39.97,'US-CTS5-011','2026-01-01','2026-12-31',{'u':U,'c':'medium','n':'Ex. 9: code A, 1,000 weekly (tables). Rules give 39.86 (residual 0.11).'}),
 ('oracle','ct.oracle.ip2026_1.ex10.withholding',78.82,'US-CTS5-011','2026-01-01','2026-12-31',{'u':U,'c':'medium','n':'Ex. 10: code B, 2,300 biweekly (tables). Rules give 79.30 (residual 0.48).'}),
]
LEGACY = []
CITED = ['US-CTS5-007','US-CTS5-014','US-CTS5-015','US-CTS5-017','US-CTS5-018','US-CTS5-026','US-CTS5-029','US-CTS5-030','US-CTS5-033','US-CTS5-034','US-CTP9W-001','US-CTP9W-002','US-CTL-001','US-CTL-002','US-CTP9L-001','US-CTP51-005','US-CTP52-002','US-MULTI-020']
NARR = {
 'income_tax': 'Decision record (brief trap "CT tables x rules", CT-OQ-1): DRS permits either the TPG-211 rules or the tables [US-CTS5-010]. The DRS worked examples (oracle) are table-based; an engine implementing the rules is lawful and will show residuals up to 0.48 per period against them, which are method-explained, not defects. The engine method choice is the builder/owner decision; if tables, parse IP 2026(1) pp. 31-39 and reproduce Ex. 8-10 exactly. Rounding: no rule beyond computed per-period amount. Wage definition follows federal.',
 'social_security': 'Coverage [US-CTS5-017]: domestic at 1,000 cash/quarter; agricultural 20,000/quarter or 10 workers on 20 days in 20 weeks; churches/ministers, family, students and spouses, student nurses/interns, newspaper carriers under 18, co-op students excluded. No SDI/TDI; no other DRS wage levy [US-CTP9W-001/-002].',
 'benefits_in_kind': 'Withholding follows federal wage definition; no CT departure located for 401(k), 125, HSA, transit, GTL (medium; 12-701(a)(20) not read). CTPL base excludes FICA-excluded benefits. 2026 new subtractions operate at assessment [US-CTS5-030].',
 'collective_agreements': '2026 changes (OLR pointers, texts not read) [US-CTS5-029]: PA 26-12 s.54 amends 31-53 (2026-10-01); PA 26-68 ss.371-373 daily attendance records weekly and journeyman benefit rate (2027-01-01); PA 26-17 comptroller withholding (2026-10-01).',
 'indexation': 'One caliber, two uses (G-CALIBER): ECI wages and salaries, all civilian workers, 12 months to 30 June, drives both the minimum wage (nearest cent) and the UI wage base (nearest 100). 2025 ECI 4.2% implied: 15.69 x 1.042 = 16.349 -> 16.35 and 25,000 x 1.042 = 26,050 -> 26,100.',
 'data_protection': '42-470/42-471: no public SSN display, secure transmission, privacy protection policy for SSN collectors [US-CTS5-026]. No truncation statute for pay statements; 31-13a does not require the SSN.',
 'live_change': 'In force: sick leave 11+ (2026-01-01); pay-code guide URL (2026-10-01); minor-league baseball MW/OT exclusion and no cannabis tip credit (2026-10-01); optional UI report fields from Q3 2026. Enacted for 2027: sick leave 1+; MW 17.48; double damages; UI shared-work non-charge; prevailing-wage records. Pension lump-sum suspension ends 2026-12-31. No ruling found. PA 26-15 s.26: AI-related layoff disclosure in WARN notices to DOL (pointer).',
}
SPECIAL = '''- Domestic: MW/OT excludes private-home domestic service except FLSA domestic service employment; UI at 1,000 cash/quarter; withholding voluntary (CT-941 HHE, CT-W3 HHE); extended hiring notice [US-CTS5-034, US-CTS5-017, US-CTS5-014, US-CTS5-007].
- Agricultural: withhold where federal applies (Pub. 51); annual CT-941 option; UI farm thresholds [US-CTS5-014, US-CTS5-017].
- Minors: 85% MW first 90 days or 10.10, greater (2026 14.40, 2027 14.86); newspaper carriers under 18 UI-excluded [US-CTS5-001, US-CTS5-017].
- Tipped: employer share 6.38 / 8.23; 0.35 elsewhere; no cannabis tip credit from 2026-10-01 [US-CTS5-002, US-CTS5-028].
- Clergy: UI excludes churches and ministers; withholding federal definition [US-CTS5-017, US-CTS5-011].
- Students: UI exclusions; RAs excluded from MW [US-CTS5-017, US-CTS5-034].
- NRAs / statutory employees: no CT rule beyond federal [US-CTS5-011].
- Government: CT state/municipal service UI-covered; CTPL excludes governments unless opted in; sick leave no government exclusion [US-CTS5-017, US-CTS5-020, US-CTS5-021].
- Military/MSRRA: nonresident military pay not CT wages; spouses exempt on CT-W4 [US-CTS5-014].
- Seasonal (<=120 days): excluded from sick leave [US-CTS5-021].'''
LANG = 'Pay-code guide in English, Spanish and other common languages (PA 26-12 s.38) [US-CTS5-028]; 31-57w(b) notice en + es poster [US-CTL-001]; payslip English (US-OWN-006).'
UNRES = [
 {'key':'ct.wh.tables.per_period','why':'DRS withholding tables (IP 2026(1) pp. 31+) not parsed; TPG-211 rules differ from tables by up to 0.48 per period, so the oracle examples are only reproducible from tables.','close':'Builder/owner decides the engine method; if tables, parse IP 2026(1) pp. 31-39 (held PDF md5 a64b2bbb...) and reproduce Ex. 8-10 (17.65 / 39.97 / 78.82).','blocking':True},
 {'key':'ct.report.sui.optional_fields_layout','why':'The 2022 ReEmployCT 276-char layout has no positions for the optional occupation/hours/ZIP data from Q3 2026; ICESA/MMREF bulk options are leads only.','close':'CT DOL bulk-filer file-format page or updated ReEmployCT spec (Employer Tax Accounting Unit, dol.etau@ct.gov).'},
 {'key':'ct.report.pfml.file_spec','why':'CT Paid Leave File Specification Toolkit (XML/CSV) linked but not downloaded.','close':'Download and parse the toolkit from ctpaidleave.org/remit-contributions/batch-process.'},
 {'key':'ct.sui.wage_base.next_year','why':'2027 UI base not published (DOL page 404); 27,900 is a projection only.','close':'CT DOL "Information on Unemployment Tax Rate for Calendar Year 2027" (December).'},
 {'key':'ct.pit.departures_from_federal','why':'Only DRS guide-level conformity checked; chapter 229 modification list not read.','close':'Conn. Gen. Stat. 12-701(a)(20) text.','blocking':False},
 {'key':'ct.leave.sick.multistate','why':'31-57r/s has no apportionment or threshold rule for employees partly in CT.','close':'CT DOL Wage and Workplace Standards paid-sick-leave FAQ 2025/2026.'},
 {'key':'ct.garn.employer_fee','why':'No employer administrative fee seen in the 52-361a/52-362 text read.','close':'Full read of 52-362 (held file) and 52-361a(j)-(k).'},
 {'key':'ct.live.public_act_texts','why':'PA 26-68 (ss.195, 371-373), PA 26-17, PA 26-15 s.26 known only via OLR summaries (A.3).','close':'Act PDFs on cga.ct.gov via the Wayback route.'},
 {'key':'ct.payslip.consolidated_text_lag','why':'Consolidated 31-13a (2026-10-20 capture) predates PA 26-12 s.38.','close':'Re-verify consolidated 31-13a at next synthesis; cite PA 26-12 until then.','blocking':False},
]
