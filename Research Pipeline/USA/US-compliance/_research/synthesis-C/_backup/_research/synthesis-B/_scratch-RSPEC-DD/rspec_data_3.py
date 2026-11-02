# RSPEC facts, part 3 (OH..WY)
D = {}
D['OH'] = [
 ('wh_return.form', 'IT 501 electronic; quarterly <=2,000 lookback; monthly 2,000-84,000 (15 days); partial-weekly >=84,000; next banking day >=100,000 in one period', 'US-OH-009', None, None),
 ('annual_recon.form', 'IT 941 by Jan 31; W-2/1099 upload (OH|TAX Upload Income Statement) by Jan 31; CD eliminated', 'US-OH-009', None, None),
 ('w2_state.school_district_code', 'W-2 carries four-digit school district code', 'US-OHS5-018', None, None),
 ('school_district.returns', 'SD 101 periodic and SD 141 annual (Jan 31); bulk FSET XML 4.4; agent WT 8655', 'US-FIL-012', None, None),
 ('municipal.frequency', 'monthly (15 days) if prior-year >2,399 or any month of preceding quarter >200, else quarterly; municipality may require semimonthly', 'US-OH-P5-2-003', 'returns per municipality/collector; CCA Form CCA-102 (US-OH-010); RITA gated', None),
 ('ui_qtr.fields', 'total and taxable remuneration; employee name, SSN, wages, number of weeks paid; last day of month after quarter', 'US-OHS5-020', 'portal channel/format not read', None),
 ('new_hire.deadline_days', 20, 'US-OHS5-009', 'fields add DOB; contractors also reported', 'days'),
]
D['OK'] = [
 ('wh_return.due', 'quarterly return 20th of month after quarter; zero return when no wages', 'US-OKS5-010', None, None),
 ('wh_remit.schedule', '<500/quarter quarterly; >=500 monthly (20th); federal semiweekly depositors on federal dates; >=5,000/month electronic', 'US-OKS5-014', None, None),
 ('w2_state.format', 'EFW2 upload (SSA 42-007) or manual entry via OkTAP by Jan 31; no magnetic media/paper', 'US-OK-001', None, None),
 ('w2_employee.ssn', 'employee statement may show only last 4 digits of SSN', 'US-OKS5-014', None, None),
 ('ui_qtr.form', 'OES-3 via EZ Tax Express, manual or upload; every active account even no wages', 'US-OKS5-020', 'statutory due date not confirmed from A source (OESC 404)', None),
 ('ui_qtr.format', 'ICESA fixed 275-character ASCII CR/LF; E, S, T required, P optional (TPA); S: name as on SS card in upper case, SSN, total and taxable wages', 'US-OKS5-020', None, None),
 ('new_hire.deadline_days', 20, 'US-OKS5-007', 'resides or works in OK; field state of hire; optional OESC account, salary, DOB, health insurance', 'days'),
]
D['OR'] = [
 ('oq.form', 'Form OQ combined quarterly (withholding, UI, Paid Leave, WBF, TriMet, Lane Transit, STT) + Schedule B + Form 132 (wage and hour detail) via Frances Online', 'US-ORS5-010', None, None),
 ('oq.due', '2026: 04-30, 07-31, 11-02, 2027-02-01; filed even with no payroll', 'US-ORS5-010', None, None),
 ('annual.forms', 'Form OA (household); Form WA and OR-STT-A (agricultural)', 'US-ORS5-010', None, None),
 ('annual_recon.form', 'OR-WR; W-2s via iWire in EFW2 or DOR template by Jan 31 (ORS 316.202)', 'US-ORS5-010', None, None),
 ('local.portland_metro_multnomah', 'quarterly returns + annual reconciliation on Portland Revenue Online; XML ReturnBatch schemaVersion 1.0; W-2 EFW2 by Jan 31 no extension', 'US-ORS5-024', 'Account IDs SHW-########## Metro, MCW-########## Multnomah; annual-reconciliation XML guide not downloaded', None),
 ('new_hire.deadline_days', 20, 'US-ORS5-016', 'DOJ Child Support Program; contractors since 2024-01-01; fields add DOB, dependent health coverage and waiting period', 'days'),
]
D['PA'] = [
 ('wh_deposit.schedule', 'quarterly, monthly, semi-monthly or semi-weekly by quarterly amount; quarterly W-3 return', 'US-PAS5-009', None, None),
 ('annual_recon.form', 'REV-1667 + W-2s by Jan 31; electronic (myPATH) at 10+ statements; EFW2 or CSV, EFW2C corrections', 'US-PAS5-010', None, None),
 ('ui_qtr.form', 'UC-2 + UC-2A (per employee SSN, name, gross wages, credit weeks), Apr 30 / Jul 31 / Oct 31 / Jan 31, online mandatory; zero report required', 'US-PAS5-013', None, None),
 ('ui_qtr.credit_week_amount', 116, 'US-PAS5-013', 'credit week = week with remuneration of at least 116', 'USD'),
 ('ui_qtr.layout', 'UC-2010 ICESA/CSV', 'US-FIL-008', None, None),
 ('new_hire.deadline_days', 20, 'US-PAS5-008', 'field adds employer contact', 'days'),
 ('local.eit_lst', 'EIT/LST quarterly returns within 30 days of quarter end and W2-R by Feb 28 with PSD work-location code to the collector', 'US-PAS5-017', None, None),
 ('local.philadelphia', 'Philadelphia wage tax employer returns', 'US-PAS5-022', None, None),
]
D['RI'] = [
 ('wh_deposit.schedule', 'weekly >=600/month (next banking day, electronic); monthly 50-599 (RI-941M by 20th); quarterly <50/month', 'US-RIS5-018', None, None),
 ('wh_return.form', 'RI-941 quarterly return and reconciliation, last day of month after quarter', 'US-RIS5-018', None, None),
 ('annual_recon.form', 'RI W-3 due Jan 31', 'US-RIS5-018', None, None),
 ('w2_state.format', 'EFW2 .txt ASCII, RS required, zip if >5 MB, max 49 MB via Tax Portal; due Jan 31', 'US-RIS5-019', None, None),
 ('w2_state.efile_threshold', 25, 'US-RIS5-019', 'mandatory if employer must e-file with SSA and has 25+ RI employees, or claims any RI credit', 'employees'),
 ('ui_qtr.form', 'TX-17 Quarterly Tax and Wage Report (UI/TDI/JDA), one report and payment; Jan 31 / Apr 30 / Jul 31 / Oct 31; zero report required', 'US-RIS5-017', None, None),
 ('ui_qtr.efile_threshold', 25, 'US-RIS5-017', 'electronic wage data mandatory at 25+ employees incl. payroll providers', 'employees'),
 ('new_hire.deadline_days', 14, 'US-RIS5-010', 'field state of hire; statutory list 15-24-5 not read', 'days'),
]
D['SC'] = [
 ('wh_return.form', 'WH-1605 Q1-Q3 (Apr 30, Jul 31, Oct 31); WH-1606 Q4 + annual reconciliation Jan 31; zero returns required', 'US-SCS5-002', None, None),
 ('wh_payment.efile', 'electronic required at 15,000+/quarter or 24+ payments a year; paper WH-1601', 'US-SCS5-018', None, None),
 ('w2_state.format', 'EFW2 .txt with SC RS (state code 45, full SSN), or Excel template (<=30 employees), or manual entry; filing with SSA does not satisfy SC', 'US-SCS5-016', 'TY2026 RS-1 edition not yet published', None),
 ('w2_state.efile_threshold', 10, 'US-SCS5-016', 'paper filers send WH-1612', 'forms'),
 ('ui_qtr.channel', 'SUITS online or upload in ICESA, EFW2, XML or CSV (spec v1.6, 2023-10-25); last day of month after quarter', 'US-SCS5-006', 'RW record: SSN 9 digits (999999999 if unavailable), names as on SSN card', None),
 ('ui_qtr.agent_efile', 'agents filing for 10+ employees must file electronically (41-31-160)', 'US-SC-P5-2-005', None, None),
 ('new_hire.deadline_days', 20, 'US-SCS5-011', 'newhire.sc.gov or SC W-4 copy with boxes 8-10', 'days'),
 ('mass_separation.form', 'UCB-113 per worker within 10 days, 10+ workers in one establishment', 'US-SCS5-007', None, None),
]
D['SD'] = [
 ('wh_return.applicable', False, 'US-SDS5-013', 'no wage tax', None),
 ('ui_qtr.form', 'Form 21 quarterly RA wage report, received by Apr 30 / Jul 31 / Oct 31 / Jan 31; zero reports required; corrections 21C', 'US-SDS5-013', None, None),
 ('ui_qtr.layout', 'CD/DVD 85-byte E and S records; S: SSN, names, total and taxable wages (2 implied decimals), state code 46, DLR account', 'US-SDS5-014', 'comma-delimited upload format not obtained', None),
 ('new_hire.deadline_days', 20, 'US-SDS5-007', 'quarterly report does not count as new-hire reporting', 'days'),
]
D['TN'] = [
 ('wh_return.applicable', False, 'US-TNS5-005', 'no wage tax', None),
 ('ui_qtr.form', 'Wage Report LB-0851 + Premium Report LB-0456, last day of month after quarter', 'US-TNS5-007', None, None),
 ('ui_qtr.channel', 'Employer e-Services (since 2025-05-27): manual, abbreviated ICESA, 58-character text, full ICESA', 'US-TNS5-005', None, None),
 ('new_hire.deadline_days', 20, 'US-TNS5-008', 'TN DHS tnnewhire.com', 'days'),
]
D['TX'] = [
 ('wh_return.applicable', False, 'US-TXS5-001', 'no income tax', None),
 ('ui_qtr.channel', 'electronic only: Unemployment Tax Services or QuickFile in ICESA, MMREF-1 or delimited', 'US-TX-SUI-006', None, None),
 ('ui_qtr.enhanced_content', 'Labor Code 204.0025: wage, industry, occupation, full/part-time, county of primary employment, remote-work status inside wage filings', 'US-TXS5-008', 'TWC implementing layout not read; mandatory-from quarter unknown', None),
 ('new_hire.deadline_days', 20, 'US-TXS5-012', 'OAG; required FEIN, IWO address, SSN, hire date, name, address; optional TWC account, DOB, salary', 'days'),
]
D['UT'] = [
 ('wh_return.form', 'TC-941E e-file only: quarterly default (<1,000/month); >=1,000/month quarterly return + monthly payments; annual for Schedule H/944 filers', 'US-UTS5-013', None, None),
 ('annual_recon.due', 'with Q4/annual return Jan 31, electronic with all W-2s and 1099s, even with zero activity', 'US-UTR3-001', None, None),
 ('w2_state.format', 'EFW2 with RS required (after RW), RV optional, RCS corrections; lowercase .txt; fixed-length mandatory at 250+ forms', 'US-UTS5-014', 'TI-03 Rev. 12/24', None),
 ('w2_state.content', 'FEIN and 14-digit Utah withholding account ending WTH; the word Utah and the SSN', 'US-UTS5-013', None, None),
 ('ui_qtr.form', 'Employer Quarterly Wage List and Contribution Report, online only, within 30 days of quarter end; zero reports required', 'US-UTS5-004', 'DWS wage file layout not read', None),
 ('new_hire.deadline_days', 20, 'US-UTS5-003', 'seven mandatory elements; DOB optional', 'days'),
]
D['VA'] = [
 ('wh_return.form', 'VA-5 quarterly (<100/month) or monthly (100-999, 25th); VA-15 semi-weekly (>=1,000) + VA-16 quarterly; all electronic', 'US-VAS5-013', None, None),
 ('annual_recon.form', 'VA-6 by Jan 31 or 30 days after last wages; filed separately from W-2 upload', 'US-VAS5-009', None, None),
 ('w2_state.format', 'Web Upload EFW2 / Pub 1220 (state code 51) or eForms; due Jan 31', 'US-VAS5-013', None, None),
 ('ui_qtr.channel', 'VEC: ESS, eForm or Web Upload (Excel, MMREF/EFW2, ICESA, delimited); last day of month after quarter; amendments FC-34', 'US-VAS5-014', None, None),
 ('new_hire.deadline_days', 20, 'US-VAS5-006', 'contractors within 20 days of contract (OUT of scope)', 'days'),
]
D['VT'] = [
 ('wh_return.form', 'WHT-436 quarterly reconciliation (carries CCC), 25th after quarter; deposits semiweekly / monthly (25th) / quarterly', 'US-VTS5-030', None, None),
 ('annual_recon.form', 'WHT-434 by Jan 31, transmittal for W-2/1099; e-file at 10+ forms and always for payroll services; no CF/SF', 'US-VTS5-017', 'W-2 file format not stated in GB-1210', None),
 ('ui_qtr.fields', 'name, SSN, gross wages; for hourly workers also gender and hourly wage (1314a(a)(2))', 'US-VTS5-007', None, None),
 ('ui_qtr.due', 'Apr 30 / Jul 31 / Oct 31 / Jan 31 or next business day, via Employer e-Services, every quarter', 'US-VTS5-009', None, None),
 ('new_hire.deadline_days', 10, 'US-VTS5-014', 'calendar days from first day worked for pay; rehire after 60+ days', 'days'),
]
D['WA'] = [
 ('wh_return.applicable', False, 'US-WAS5-013', 'no income tax; no state W-2', None),
 ('ui_qtr.fields', 'name, SSN, gross pay, hours worked in quarter (rounded up; 40/week if salaried hours untracked; paid leave hours included), SOC code', 'US-WAS5-013', None, None),
 ('ui_qtr.due', 'Apr 30 / Jul 31 / Oct 31 / Jan 31 in EAMS via SAW; nil report required', 'US-WAS5-013', None, None),
 ('ui_qtr.exempt_officers', 'corporate officers without voluntary coverage in Exempt Officer section (count + combined wages)', 'US-WAS5-027', None, None),
 ('pfml_ltc_qtr.form', 'combined Paid Leave + WA Cares quarterly report (wages and hours) on paidleave.wa.gov', 'US-WA-PFML-001', 'field list and deadline rest on older row; portal blocked', None),
 ('new_hire.deadline_days', 20, 'US-WAS5-018', 'DSHS DCS; DOB required; rehire after 60+ days', 'days'),
 ('local.seattle', 'Seattle payroll expense tax (employer, SMC 5.38) and Social Housing Tax; Taxpayer Authorization Form per client', 'US-WA-P5-1-001', None, None),
]
D['WI'] = [
 ('wh_deposit.form', 'WT-6 per DOR-assigned frequency (annual/quarterly/monthly/semi-monthly); no published thresholds; zero report filed; electronic only', 'US-WIS5-011', None, None),
 ('annual_recon.form', 'WT-7 by Jan 31 (TY2026: 2027-02-01); rejected until all WT-6 filed', 'US-WIS5-016', None, None),
 ('w2_state.format', 'EFW2 with RS (state code 55 in 3-4 and 274-275); 10+ W-2s electronic; MTA, upload, sFTP; no transmittal', 'US-WIS5-012', None, None),
 ('ui_qtr.efile_threshold', 25, 'US-WIS5-014', '108.205(2); paper penalty 20 per employee; layouts include modified E/S record', 'employees'),
 ('ui_qtr.due', 'end of month after quarter, even at zero rate', 'US-WIS5-013', 'new UI Employer Portal fall 2026; no mailed reports 2027', None),
 ('new_hire.deadline_days', 20, 'US-WIS5-013', 'field adds DOB', 'days'),
]
D['WV'] = [
 ('wh_return.form', 'IT-101Q quarterly, last day of month after quarter, even nil; remit by 15th; annual IT-101A <600/yr', 'US-WVS5-014', None, None),
 ('annual_recon.form', 'IT-103 + state W-2 by Jan 31 via MyTaxes (Letter of Intent)', 'US-WVS5-010', None, None),
 ('w2_state.format', 'EFW2 only, 512-byte; RS required (state code 54); WV RV record with IT-103 totals (money fields differ from EFW2); every RE needs an RV', 'US-WVS5-013', 'IT-105 2025 latest; 2026 edition not out', None),
 ('w2_state.efile_threshold', 10, 'US-WVS5-010', 'or using a payroll service, periods after 2024-12-31; stale copy of 11-21-74 says 25/50', 'employees'),
 ('ui_qtr.fields', 'name, SSN, gross wages, SOC or job title, county, monthly employee counts; wages in quarter paid', 'US-WV-UI-001', None, None),
 ('new_hire.deadline_days', 14, 'US-WVS5-016', 'regardless of hours; DOB; rehire if not employed prior 60 days', 'days'),
]
D['WY'] = [
 ('wh_return.applicable', False, 'US-WY-P5-1-001', 'no income tax', None),
 ('ui_qtr.due', 'Apr 30 / Jul 31 / Oct 31 / Jan 31 (delinquent next day), next business day', 'US-WYS5-009', 'WYUI file spec not read', None),
 ('ui_qtr.peo', 'service supplier files separate quarterly report per client and a quarterly client list', 'US-WYS5-019', None, None),
 ('wc_report.frequency', 'workers compensation payroll report monthly (quarterly by permission), joint UI/WC reporting', 'US-WYS5-007', None, None),
 ('new_hire.deadline_days', 20, 'US-WYS5-006', 'W-4 or DWS equivalent', 'days'),
]
