# RSPEC facts, part 2 (ID..NY)
D = {}
D['ID'] = [
 ('wh_return.form', 'Form 910 in TAP: semimonthly >=25,000/month or >=300,000/12m; monthly (20th); quarterly <=750/qtr; annual <750/yr (Jan 31); zero return required', 'US-IDS5-009', None, None),
 ('annual_recon.form', 'Form 967 + W-2s, last day of January (1099 with ID withholding last day of February)', 'US-IDS5-010', None, None),
 ('w2_state.format', 'EFW2 (SSA 42-007) plus Idaho state records uploaded in TAP; valid EFW2 generates the 967 (RV record); amounts rounded to dollar', 'US-IDS5-010', 'State-record spec on STC Software Developers page not fetched', None),
 ('ui_qtr.form', 'TX20 (+TX26 continuation; TX20C amendments), last day of month after quarter, no grace; online mandatory; zero reports required', 'US-IDS5-021', None, None),
 ('new_hire.deadline_days', 20, 'US-IDS5-015', 'fields add Idaho UI account number, hire date, multistate flag', 'days'),
 ('registration.form', 'Idaho Business Registration (IBR), one form for STC and IDOL', 'US-IDS5-021', None, None),
]
D['IL'] = [
 ('wh_return.form', 'IL-941 quarterly, electronic (MyTax or software); 2026 due 04-30, 07-31, 11-02, 2027-02-01', 'US-ILS5-012', None, None),
 ('annual_recon.applicable', False, 'US-ILS5-011', 'Illinois has no annual reconciliation', None),
 ('wh_deposit.schedule', 'monthly (15th) when lookback <=12,000; semi-weekly (federal rule, electronic) when >12,000; voucher IL-501', 'US-ILS5-011', None, None),
 ('w2_state.channel', 'electronic only: MyTax manual/CSV/EFW2 upload (IDR-996) or bulk EFW2 with ETIN (IDR-986); due Jan 31 (2026 W-2s by 2027-02-01)', 'US-ILS5-013', 'IDR-986 specification not downloaded', None),
 ('ui_qtr.form', 'UI-3/40 quarterly wage report + contributions, due Apr 30 / Jul 31 / Oct 31 / Jan 31', 'US-ILS5-016', None, None),
 ('ui_monthly.rule', 'monthly wage report months 1 and 2 of each quarter for employers with >=25 employees prior year; name, SSN, wages; MyTax CSV only', 'US-ILS5-017', None, None),
 ('new_hire.deadline_days', 20, 'US-ILS5-018', 'includes rehires and independent contractors; optional IWO address', 'days'),
]
D['IN'] = [
 ('wh_return.form', 'WH-1: annual (avg <=83.33/month, 30 days after period); monthly (<=1,000, 30 days); early filer (>1,000, 20 days); zero returns mandatory', 'US-INS5-010', None, None),
 ('wh_return.format', 'xml (IDORWTH2016V1.0) via INTIME or SFTP (>10 MB), or online_form', 'US-INS5-012', 'XML schema not downloaded (ACCESS gap)', None),
 ('wh_payment.eft_threshold', 5000, 'US-INS5-012', 'EFT required if average >5,000/month', 'USD'),
 ('annual_recon.form', 'WH-3 + state W-2, Jan 31 (use Jan 31 over FAQ Feb 28)', 'US-INS5-011', 'Conflict: DOR FAQ US-INS5-012 says Feb 28', None),
 ('w2_state.efile_threshold', 25, 'US-INS5-011', 'IC 6-3-4-16.5: electronic above 25 statements', 'statements'),
 ('w2_state.format', 'xml; IRIS XML; EFW2 for existing filers only (RS 306-343: county code, local wages, local tax, 10-digit TID + 3-digit location)', 'US-INS5-013', 'EFW2 guide labelled 2025 and prior; new filers XML', None),
 ('ui_qtr.channel', 'DWD E S S/UPLINK: online_form up to 50 workers; file_upload CSV or Indiana-modified ICESA required above 50', 'US-INS5-014', None, None),
 ('ui_qtr.due', 'Apr 30 / Jul 31 / Oct 31 / Jan 31; electronic filing and payment mandatory', 'US-INS5-014', None, None),
 ('ui_qtr.extra_fields', 'SOC code (6 digits) and start date per worker', 'US-INS5-014', None, None),
 ('new_hire.deadline_days', 20, 'US-INS5-016', 'electronic only since 2024-07-01; extra fields job title, SOC, starting compensation, rate-of-pay basis; rehire after 60+ days', 'days'),
]
D['KS'] = [
 ('wh_deposit.schedule', 'quad-monthly >100,000/yr; semi-monthly 8,000-100,000; monthly 1,200-8,000 (15th); quarterly 200-1,200 (25th); annual <=200 (Jan 25)', 'US-KSS5-007', None, None),
 ('wh_deposit.report', 'KW-5 for every period, even when nothing withheld', 'US-KSS5-007', None, None),
 ('annual_recon.form', 'KW-3 electronically by Jan 31 with state W-2s and 1099s with KS withholding', 'US-KSS5-007', None, None),
 ('w2_state.efile_threshold', 51, 'US-KSS5-026', None, 'forms'),
 ('w2_state.format', 'EFW2 with Kansas RS (K-2MT Rev. 10-25, 512 bytes, KS wages only; RA/RE/RW/RS/RT/RF required) or KW-2CSV; no CF/SF', 'US-KSS5-026', 'TY2026 K-2MT not yet located', None),
 ('ui_qtr.due', 'Apr 30 / Jul 31 / Oct 31 / Jan 31', 'US-KSS5-022', None, None),
 ('ui_qtr.efile_threshold', 25, 'US-KSS5-022', 'Page self-contradicts (FAQ 26+, EDI 25+ from 2024-07-01); build uses 25+, the stricter reading', 'employees'),
 ('ui_qtr.format', 'MMREF / NASWA upload; paper K-CNS-100 below threshold', 'US-KSS5-022', None, None),
 ('new_hire.deadline', '20 business days (K.S.A. 75-5743); rehire after 60+ days', 'US-KSS5-019', 'KDOL page says 20 days; statute governs', None),
]
D['KY'] = [
 ('wh_return.frequency', 'annual <400 (K-3 Jan 31); quarterly 400-1,999 (K-1); monthly 2,000-49,999 (K-1 by 15th); twice-monthly >=50,000', 'US-KYS5-013', None, None),
 ('annual_recon.form', 'K-3 by Jan 31', 'US-KYS5-013', None, None),
 ('w2_state.format', 'SSA EFW2 with DOR-defined RS record, or Form K-5, via MyTaxes; paper W-2 not processed', 'US-KYS5-013', 'RS spec not fetched', None),
 ('w2_state.efile_threshold', 26, 'US-KYS5-013', '103 KAR 18:050(4)', 'statements'),
 ('ui_qtr.channel', 'KUIP (replaced KEWES in 2026), last day of month after quarter; zero reports required', 'US-KYS5-019', 'KUIP upload format not read', None),
 ('new_hire.recipient', 'Office of the Attorney General since 2025-07-01; 20 days; hire, rehire or return from layoff/furlough/leave', 'US-KYS5-020', None, None),
 ('local.louisville', 'Louisville OLT: W-1 quarterly; W-1D monthly if >3,000/quarter; W-3 + W-2 data by Feb 28', 'US-KYP9W-002', None, None),
 ('local.lexington', 'Lexington-Fayette occupational license fee 2.25%, employer return 220-221/222', 'US-KYS5-024', None, None),
]
D['LA'] = [
 ('wh_return.form', 'L-1 quarterly electronic (LaTAP), zero returns required; Apr 30 / Jul 31 / Oct 31 / Jan 31', 'US-LAS5-003', None, None),
 ('wh_payment.frequency', 'quarterly <500/month avg; monthly 500-<5,000; semi-monthly >=5,000', 'US-LAS5-008', None, None),
 ('annual_recon.form', 'L-3 + W-2s on or before first business day after Jan 31; within 30 days on closure', 'US-LAS5-003', None, None),
 ('w2_state.efile_threshold', 50, 'US-LAS5-009', 'electronic via LaWage; magnetic media/CD refused; bulk file format not read', 'forms'),
 ('ui_qtr.due', 'last day of month after quarter; domestic annual Jan 31; mandatory electronic (LAWATS)', 'US-LAS5-007', 'A.3 snapshot 2025-04; form name and upload format not read', None),
 ('new_hire.deadline_days', 20, 'US-LAS5-010', 'fields add occupation; no 60-day threshold in statute', 'days'),
]
D['MA'] = [
 ('wh_return.frequency', '<=100 annual Jan 31; 101-1,200 quarterly; 1,201-25,000 monthly (15th); >25,000 quarterly return + 3-business-day payments', 'US-MAS5-013', None, None),
 ('wh_return.efile', 'mandatory for new registrations, payroll service providers and combined liability >=5,000', 'US-MAS5-013', None, None),
 ('w2_state.due', 'Jan 31 to employee, SSA and DOR', 'US-MAS5-015', 'Conflict: Withholding Tax Guide (Aug 2026) says last day of March / Feb 28; recommend Jan 31', None),
 ('w2_state.efile_threshold', 50, 'US-MAS5-015', '49 or fewer may file paper with Form M-3', 'forms'),
 ('w2_state.format', 'EFW2 RA/RE/RS/RT; RS MA wages 276-286, MA withholding 287-297; RT must equal sum of RS; PDF/CSV refused', 'US-MAS5-019', 'Handbook served is Rev. 20191219', None),
 ('ui_qtr.due', 'by 3 p.m. Apr 30 / Jul 31 / Oct 31 / Jan 31; wages reported when paid', 'US-MAS5-018', None, None),
 ('ui_qtr.format', 'CSV, EFW2 or ICESA upload (DUA)', 'US-MAS5-018', None, None),
 ('ui_qtr.fields', 'EAN; SSN; full name; hours worked; gross wages; wages subject to withholding; state income tax withheld; work location; 12th-of-month employment; adjustment reason code', 'US-MAS5-018', None, None),
 ('new_hire.deadline_days', 14, 'US-MAS5-016', 'employees and contractors 600+; rehire after 30+ days; online mandatory 25+ employees; no ITIN', 'days'),
]
D['MD'] = [
 ('wh_return.form', 'MW506: accelerated (15,000+ prior year and 700+ accumulated, 3 business days); monthly (>700 in a quarter); quarterly (<700); annual (<250, Jan 31)', 'US-MDS5-021', None, None),
 ('annual_recon.form', 'MW508 + W-2s due Jan 31; zero MW508 required for any open account', 'US-MDS5-016', None, None),
 ('w2_state.efile_threshold', 25, 'US-MDS5-016', 'TG 13-706.1', 'forms'),
 ('w2_state.format', 'SSA EFW2 modified Maryland format: RS FEIN 328-336, CRN 338-345; RV = MW508 with NAICS 333-338; date-time stamp 497-512', 'US-MDS5-016', 'TY2026 edition not yet posted', None),
 ('ui_qtr.channel', 'BEACON, within 1 month after quarter: online, CSV, XML, ICESA or EFW2 (spec updated 2026-04-20)', 'US-MDS5-017', None, None),
 ('ui_qtr.amount_format', 'cents with no decimal point; adjustment codes 00-10', 'US-MDS5-017', None, None),
 ('new_hire.deadline_days', 20, 'US-MDS5-018', 'fields add starting wage, health insurance offered, MD UI account number', 'days'),
 ('pfml.start', 'FAMLI contributions from 2027-01-01', 'US-MDS5-014', None, None),
]
D['ME'] = [
 ('wh_return.form', '941ME quarterly, last day of month after quarter, electronic mandatory even when nothing to report', 'US-MEP52-002', None, None),
 ('wh_deposit.schedule', 'semiweekly if lookback >=18,000, else quarterly with the return; voucher 900ME', 'US-MES5-011', None, None),
 ('annual_recon.applicable', False, 'US-MEP52-009', 'no W-3ME after TY2023', None),
 ('w2_state.due', 'electronically with MRS by Jan 31; paper not accepted', 'US-MES5-011', 'Bulk File Upload Specifications not fetched; EFW2 acceptance open', None),
 ('ui_qtr.form', 'ME UC-1 quarterly via ReEmployME; monthly employment for the 12th, gross/excess/taxable wages, UC rate, CSSF, UPAF; filed with MRS', 'US-MES5-021', None, None),
 ('pfml_qtr.form', 'PFML quarterly wage report and premium in PFML portal', 'US-MES5-024', None, None),
 ('new_hire.deadline_days', 7, 'US-MES5-016', 'rehire after 60+ days; fields add DOB, UI/UBI number; contractors 2,500+ also reported', 'days'),
]
D['MI'] = [
 ('wh_return.form', 'Form 5080 monthly/quarterly, due 20th after period (Treasury assigns frequency)', 'US-MIS5-018', None, None),
 ('annual_recon.form', 'Form 5081 for 2026 due 2027-02-28; every filer files', 'US-MIS5-021', None, None),
 ('wh_payment.accelerated_threshold', 480000, 'US-MIS5-021', 'prior-year liability 480,000+ = EFT on federal deposit day', 'USD'),
 ('w2_state.format', 'EFW2 / Pub 1220 upload through MTO for 10+ forms; W-2 always direct to Treasury (CF/SF 1099 only); due Jan 31', 'US-MIPIT-001', None, None),
 ('ui_qtr.due', 'Jan 25 / Apr 25 / Jul 25 / Oct 25, next business day', 'US-MIS5-020', None, None),
 ('ui_qtr.formats', 'MiUI four formats: Delimited CSV (2026 spec v3, 2026-04-08), ICESA (v2), EFW2 (v2 2026-04-03, RE/RS 512-byte UIA profile), XML (v1 2026-02-23); MiWAM legacy refused', 'US-MIS5-022', 'Specs on disk; inspected', None),
 ('new_hire.channel', 'Michigan New Hires Operation Center, mi-newhire.com, Form 3281; federal 20 days', 'US-FED-017', 'MI statute and penalty not located; US-MIS5-026 partial', None),
 ('local.detroit', 'Detroit monthly return Form 5323 (15th) and annual reconciliation Form 5321 TY2026 due 2027-02-28; DW-4 certificate', 'US-MIP51-002', None, None),
]
D['MN'] = [
 ('wh_return.due', 'quarterly Apr 30 / Jul 31 / Oct 31 / Jan 31 in e-Services; annual filers (<=500 prior year) Jan 31', 'US-MNS5-010', None, None),
 ('w2_state.due', 'W-2 information to DOR by Jan 31; e-Services mandatory above 10 W-2 + 1099', 'US-MNS5-010', 'Fact Sheets 2/2a on new e-file method not fetched', None),
 ('ui_qtr.fields', 'per employee: name, SSN, wages, paid hours worked (exempt full-time = 40 h/week); wages may be truncated to dollar', 'US-MNS5-015', 'quarterly due date not in this section (open)', None),
 ('pfml_qtr.form', 'Paid Leave quarterly wage detail and premium to DEED, electronic', 'US-MNS5-018', None, None),
 ('new_hire.deadline_days', 20, 'US-MNS5-016', 'rehire after 60+ days; exempt if <2 months and <250/month; private-home domestic excluded', 'days'),
]
D['MO'] = [
 ('wh_return.form', 'MO-941: monthly (500+ in 2 of prior 12 months), quarterly (100+ in any quarter), annual (<100 every quarter); zero return required', 'US-MOS5-001', None, None),
 ('wh_payment.quarter_monthly', 9000, 'US-MOS5-001', 'quarter-monthly at 9,000+ in each of 2 months of prior 12; 3 banking days, electronic', 'USD'),
 ('w2_state.due', 'MO W-3 with W-2s and 1099-R by last day of January (electronic) or end of February (paper)', 'US-MOS5-001', None, None),
 ('w2_state.efile_threshold', 250, 'US-MOS5-001', 'EFW2 with RV record carrying MO W-3 data', 'forms'),
 ('ui_qtr.form', 'MODES-4 (instructions MODES-4-5): name, SSN, quarterly wages, separation dates, probationary flag P with dates', 'US-MOS5-013', None, None),
 ('ui_qtr.channel', 'UInteract (Method B upload; NASWA/ICESA for payroll services; spec M-INF-368); electronic if 50+ employees and W-2s e-filed with SSA', 'US-MOS5-013', None, None),
 ('new_hire.deadline_days', 20, 'US-MOS5-008', 'to MO DOR; MO W-4 copy or equivalent', 'days'),
 ('local.st_louis', 'St. Louis earnings tax 1% withholding and payroll expense tax 0.5%, quarterly W-10/P-10', 'US-MOP52-006', None, None),
 ('local.kansas_city', 'Kansas City 1% earnings tax; RD-100 registration', 'US-MOP52-007', None, None),
]
D['MS'] = [
 ('wh_return.form', '89-105 coupon or TAP, 15th of month after period; monthly if avg >=300/month else quarterly; no depository system', 'US-MSS5-019', None, None),
 ('annual_recon.applicable', False, 'US-MSS5-002', 'no separate annual reconciliation; 89-140 only with paper W-2s (<10)', None),
 ('w2_state.format', 'EFW2 with RS (state code 28) via TAP; mandatory electronic 10+ W-2s; due Jan 31, no extensions', 'US-MSS5-005', 'Pub 89-145 Rev 10/25 on file; TY2026 not seen', None),
 ('ui_qtr.form', 'UI-2 (tax) and UI-3 (wage detail), Apr 30 / Jul 31 / Oct 31 / Jan 31; zero report required', 'US-MSS5-012', None, None),
 ('ui_qtr.format', 'ICESA S record 275 chars (UIWAGE.TXT) or EFW2 RS with required positions 1-2, 3-4, 10-18, 19-68, 197-202, 203-213, 248-267', 'US-MSS5-013', None, None),
 ('new_hire.deadline_days', 15, 'US-MSS5-006', 'fields add DOB, gender, salary, pay frequency, medical-insurance eligibility; employer state EIN', 'days'),
]
D['MT'] = [
 ('wh_deposit.schedule', '>=12,000 accelerated (federal schedule); 1,200-11,999 monthly (15th); <=1,199 annual (Jan 31)', 'US-MTS5-005', None, None),
 ('annual_recon.form', 'MW-3 + all W-2s due Jan 31; federal W-3 not accepted; no truncated SSNs', 'US-MTS5-005', None, None),
 ('w2_state.format', 'TAP single entry or File Processing upload in EFW2 (W-2) / Pub 1220 (1099); PDF refused', 'US-MTS5-005', None, None),
 ('ui_qtr.due', 'Apr 30 / Jul 31 / Oct 31 / Jan 31; electronic mandatory from 2025-07-01 via UI eServices', 'US-MTS5-025', 'E-Filing Handbook not obtained', None),
 ('new_hire.deadline_days', 20, 'US-MTS5-012', 'residential and mailing addresses; optional DOB and dependent health coverage', 'days'),
]
D['NC'] = [
 ('wh_return.form', 'NC-5: quarterly <250/month; monthly 250-<2,000 (15th); semiweekly >=2,000 (NC-5P) + NC-5Q quarterly', 'US-NC-001', None, None),
 ('annual_recon.form', 'NC-3 + W-2/1099 state copies due Jan 31, electronic via eNC3', 'US-NC-001', None, None),
 ('w2_state.format', 'NC-3 and W-2 fixed-field .txt; TY2026 specs version 9-2026 (use beginning Jan 2027)', 'US-NCS5-028', 'Spec not downloaded; 10-2020 layout on disk is partial row US-NCS5-027', None),
 ('ui_qtr.form', 'NCUI 101 via NCSUITS, Apr 30 / Jul 31 / Oct 31 / Jan 31; electronic at 10+ wage items', 'US-NCS5-025', None, None),
 ('new_hire.deadline_days', 20, 'US-NCS5-020', None, 'days'),
]
D['ND'] = [
 ('wh_return.form', 'Form 306 quarterly Apr 30 / Jul 31 / Oct 31 / Jan 31, even zero; annual option if prior-year <1,000', 'US-NDS5-002', None, None),
 ('wh_return.efile', 'mandatory if prior-year withholding >=1,000 or provider e-files federally', 'US-NDS5-003', None, None),
 ('annual_recon.form', 'Form 307 + W-2 due Jan 31; e-file of 307 required even with zero W-2s', 'US-NDS5-002', None, None),
 ('w2_state.format', 'EFW2 (SSA 42-007), W-2c EFW2C, TAP upload/key-entry or web service; W-2 e-file mandatory since 2022', 'US-NDS5-003', None, None),
 ('ui_qtr.channel', 'UI EASY or Secure FTP; due end of month after quarter', 'US-NDS5-011', None, None),
 ('new_hire.deadline_days', 20, 'US-NDS5-013', 'field adds health insurance offered', 'days'),
]
D['NE'] = [
 ('wh_return.form', '941N quarterly, last day of month after quarter; annual filers Jan 31; zero required', 'US-NES5-010', None, None),
 ('wh_deposit.rule', '501N / EFT by 15th when >500 withheld in month 1 or 2; EFT mandatory if prior-year payments >5,000', 'US-NES5-010', None, None),
 ('w2_state.format', 'W-3N + W-2/1099 by Jan 31; >50 forms e-file via NebFile; EFW2 with NE RS (state code 31, entity 31) and RV total record (21EFW2 Nov 2025)', 'US-NES5-017', None, None),
 ('w2_state.box15', 'NE + 4-8 digit Nebraska ID exactly as on 941N/W-3N', 'US-NES5-016', None, None),
 ('ui_qtr.form', 'Combined Tax Report + Wage Report: SSN, last name + initials, gross wages; optional hours and job title; NEworks or FTP', 'US-NES5-011', 'FTP spec not fetched', None),
 ('new_hire.deadline_days', 20, 'US-NES5-014', None, 'days'),
]
D['NH'] = [
 ('wh_return.applicable', False, 'US-NH-006', 'no state wage tax', None),
 ('ui_qtr.form', 'Quarterly Employer Tax and Wage Report (Part 1 tax, Part 2 wages), last day of month after quarter (+2 days WebTax); every quarter even with no employment', 'US-NHS5-013', 'Figures from 2016 Handbook (A.3)', None),
 ('new_hire.deadline_days', 20, 'US-NHS5-006', 'contractors >2,500 also reported (OUT of scope)', 'days'),
]
D['NJ'] = [
 ('wh_return.form', 'NJ-927 quarterly, electronic, 30th of month after quarter, even zero; NJ-500 monthly payment if >500 in month 1 or 2; NJ-927-W weekly (prior-year >=10,000); NJ-927-H domestic annual Jan 31', 'US-NJP51-001', None, None),
 ('annual_recon.form', 'NJ-W-3 by Feb 15 (or 30 days after wages stop); W-2 electronic since TY2020 (online, upload, Axway 100+)', 'US-NJP51-001', None, None),
 ('ui_qtr.form', 'WR-30: SSN (no ITIN), name, gross NJ wages, base weeks; 30th of month after quarter, no weekend extension', 'US-NJS5-017', None, None),
 ('ui_qtr.base_week_amount', 310, 'US-NJS5-010', '2026 base week = 20 x prior-year minimum wage; 319 in 2027; severance under contract 0 base weeks', 'USD'),
 ('separation.form', 'BC-10 at every separation', 'US-NJS5-015', None, None),
 ('new_hire.deadline_days', 20, 'US-NJS5-018', 'contractors also reported; DOB and hire date required per CSESP', 'days'),
 ('local.newark_jersey_city', 'Newark and Jersey City quarterly employer payroll tax returns', 'US-NJP6-002', 'Jersey City US-NJP6-001', None),
]
D['NM'] = [
 ('wh_return.form', 'TRD-41414 monthly/quarterly/semiannual per registration certificate; 25th of month after period; zero required', 'US-NMS5-011', None, None),
 ('wh_qtr_report.form', 'TRD-41431 (new 2026-01-01): WC fee return + employee quarterly wage and withholding report, 25th after quarter', 'US-NMS5-012', None, None),
 ('efile.mandate', 'TRD-41414, TRD-41431, TRD-41409 e-file and e-pay from 2026', 'US-NMS5-012', 'TAP bulk schema not obtained', None),
 ('w2_state.due', 'Jan 31; electronic only from 2026 (TAP TXT or CF/SF code 35)', 'US-NMP52-005', 'Conflict: TRD page US-NMS5-013 says end of February; build on FYI-330', None),
 ('ui_qtr.formats', 'Delimited, ICESA, XML, EFW2; electronic only; last day of month after quarter', 'US-NMS5-008', 'specs not read (403)', None),
 ('new_hire.deadline_days', 20, 'US-NMS5-010', None, 'days'),
]
D['NV'] = [
 ('wh_return.applicable', False, 'US-NVS5-014', 'no state income tax', None),
 ('ui_qtr.form', 'RPT3795 contribution report and NEW0098 wage report; received by Apr 30 / Jul 31 / Oct 31 / Jan 31; wages in quarter paid', 'US-NVS5-008', 'Handbook 2023 edition', None),
 ('ui_qtr.channel', 'ESS data entry, SFTP EFW2 upload, CSV/tab file', 'US-NVS5-008', None, None),
 ('mbt.form', 'MBT quarterly TAX-F003 (V2026.1), last day of month after quarter, even no tax due', 'US-NVS5-010', None, None),
 ('mbt.ui_match', 'from 2026-01-01 MBT wages compared with ESD wages every quarter; mismatch = deficiency', 'US-NVS5-009', None, None),
 ('new_hire.deadline_days', 20, 'US-NVS5-007', 'rehire after 60+ days', 'days'),
]
D['NY'] = [
 ('nys45.form', 'NYS-45 quarterly combined withholding + wage reporting + UI; Parts A, B, C mandatory; due Apr 30 / Jul 31 / Oct 31 / Jan 31', 'US-NYS5-010', None, None),
 ('nys45.efile', 'e-file and ACH mandatory; 50 USD penalty per paper document; upload spec Pub 72.5', 'US-FIL-007', None, None),
 ('nys1.deposit', 'within 3 business days (15,000+ prior-prior year) or 5 business days after payroll taking QTD withholding to 700+', 'US-NYS5-010', None, None),
 ('w2_state.filed', False, 'US-NYS5-010', 'no W-2 copy filed with NY; NYS-45 Part C replaces it', None),
 ('new_hire.deadline_days', 20, 'US-NYS5-010', 'to DTF; dependent health insurance availability and date; NRA from SSN issue', 'days'),
 ('mctmt.form', 'MTA-305 quarterly', 'US-NY-003', None, None),
]
