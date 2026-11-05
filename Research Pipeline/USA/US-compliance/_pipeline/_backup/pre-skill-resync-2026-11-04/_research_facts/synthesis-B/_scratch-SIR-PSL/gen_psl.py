import sys, json
sys.path.insert(0, r"C:/Users/INSTIT~1/AppData/Local/Temp/claude/C--Users-instituto-Documents-brain-service-frentes-eua/272453a3-1ad8-4a54-b824-fda2544cbf81/scratchpad/synthB")
from gen_common import build, write, BASE

S = []
def F(key, value, rid, **kw):
    d = {'key': key, 'value': value, 'rid': rid}; d.update(kw); S.append(d)

# ---------------- federal / cross-cutting ----------------
F('psl.fed.statement.required', False, 'US-FED-010', note='29 CFR 516.2(a) prescribes employer records only; no federal pay-statement content or delivery rule. Content is state law.')
F('psl.fed.retention.payroll_records.years', 3, 'US-FEDS5-021', uom='years', note='29 CFR 516.5 payroll records.')
F('psl.fed.retention.employment_tax_records.years', 4, 'US-FEDS5-003', uom='years', note='IRS employment-tax records.')
F('psl.language.official_federal', 'en: English designated by presidential action of 2025-03-01; no obligation on private employers', 'US-FED-020',
  note='Payslip language rule for the build (payslip en, authority-facing en, es rank 2 seam) is the owner-delegated decision US-OWN-006 (owner row, tier not A.x, so it is carried in _owner_decisions, not as a fact).')
F('psl.w2.ssn_truncation.rule', 'SSN may be truncated to XXX-XX-1234 on employee W-2 copies only; never on Copy A; EIN never truncated', 'US-FEDS5-022')
F('psl.w2.box12.new_codes_2026', 'TP (cash tips), TT (qualified overtime), TA (Trump-account employer contributions)', 'US-FEDS5-007', note='Employer reporting level. TY2025 penalty relief only (US-FEDS5-013); mandatory from TY2026.')
F('psl.w2.box14b.tipped_occupation_code', 'Box 14 split into 14a Other and 14b Treasury Tipped Occupation Code(s) from TY2026', 'US-FEDS5-007')
F('psl.w2.box14.vt_child_care_contribution', 'VT CCC employee share (max 0.11% of wages, of the 0.44% total) reported in W-2 Box 14', 'US-VTS5-030', note='Employer may withhold up to one quarter of the 0.44%; may withhold less or none.')
F('psl.w2.box14.vt_ccc.employee_max_rate', 0.11, 'US-VTS5-030', uom='percent', note='Percent of wages; 0.44 total = 0.11 employee max + 0.33 employer.')
F('psl.w2.box14.me_pfml_label', 'MEPFML', 'US-MES5-025', conf='medium', note='Maine PFML employee contributions; label per Maine Paid Leave employer FAQ (A.3). Employee share withheld after taxes.')
F('psl.w2.box14.ca_sdi', 'CASDI (or VPDI) in Box 14; CA PIT wages Box 16; CA PIT withheld Box 17', 'US-CAS5-018')
F('psl.w2.multistate.boxes_15_20', 'Up to two states and two localities per W-2; more requires a second W-2 repeating boxes a-f, never duplicating federal data on Copy A; W-3 box 15 = X when more than one state', 'US-MULTIS5-011')
F('psl.multi.reach.ca', 'Lab. Code 226 applies when the principal place of work is CA (majority of working time); if no majority state, when CA is the base of work operations and some work is done in CA (Ward v. United Airlines, S248702, 2020-06-29; level: pay-statement content)', 'US-MULTIS5-018', conf='medium')
F('psl.multi.reach.default', 'Default: the pay-statement statute of the work-location state (no other state reach rule researched)', 'US-MULTIS5-018', conf='medium', note='Default is an inference from the CA ruling plus the per-state "employed in this state" texts (IA, OK, WV, WY, DE); not a federal rule.')

# ---------------- language seams (notices/posters, not the payslip) ----------------
F('psl.notice_language.ca', 'Hire notice (Lab. Code 2810.5) in the language the employer normally uses', 'US-CAP6-001')
F('psl.notice_language.ny', 'Hire notice (Labor Law 195(1)(a)) in English and the employee primary language', 'US-NYP51-003')
F('psl.notice_language.mn', 'Hire notice (181.032) in English; other language on request', 'US-MNP6-001')
F('psl.notice_language.dc', 'Hire/change notice (32-1008(c)) in English and also the primary language where the Mayor has a template', 'US-DCS5-010')
F('psl.notice_language.nj_gender_equity', 'N.J.S.A. 34:11-56.12(c): employers with 50+ employees post and provide in English, Spanish and Commissioner-available first languages; deliverable as a pay-check insert', 'US-NJP9M-001')
F('psl.notice_language.nj_sick_leave', 'NJ earned sick leave notice in the languages published by NJDOL', 'US-FEDR3-010', conf='medium')
F('psl.notice_language.co_comps', 'COMPS Order Rule 7.4.3: Spanish COMPS Order/poster where LEP employees speak Spanish, or a Division version in another language', 'US-COP9L-001', conf='medium', note='Rule quoted on agency page; rule instrument not read (US-OWN-006 recorded limit).')
F('psl.notice_language.co_paid_leave', 'C.R.S. 8-13.3-408(2): notice in English and the first language of 5%+ of the workforce', 'US-COL-001')
F('psl.notice_language.tx_workplace_violence', 'Workplace-violence reporting notice in English and Spanish, every employer with 1+ employees since 2024-01-08 (HB 915; 40 TAC 800.600)', 'US-TXP9M-001')
F('psl.notice_language.az', 'Minimum-wage and earned-paid-sick-time posters/notice in English and Spanish (A.R.S. 23-375(B))', 'US-AZL-001')
F('psl.notice_language.ct', 'C.G.S. 31-57w(b) paid sick leave poster in English and Spanish', 'US-CTL-001')
F('psl.notice_language.de', '19 Del. C. 3710(c) paid-leave notice in English, Spanish and any first language of 5%+ of the workforce', 'US-DEL-001')
F('psl.notice_language.fl', 'Fla. Stat. 448.109(3)(a) minimum-wage poster in English and Spanish', 'US-FLL-001')
F('psl.notice_language.ma', 'M.G.L. c.149 s.148C(o) earned sick time notice languages', 'US-MAL-002')
F('psl.notice_language.mi', 'ESTA notice/poster in English, Spanish and any language that is the first language of 10%+ of the workforce if LEO translated it', 'US-MIL-001')
F('psl.notice_language.or', 'ORS 652.610(6): BOLI template in English and Spanish for the new-hire earnings/deductions explanation', 'US-ORL-001')
F('psl.notice_language.vt_paycard', '21 V.S.A. 342(f) payroll-card disclosures in the primary language', 'US-VTL-001')

# ---------------- per jurisdiction ----------------
# AK
F('psl.ak.statement.content', 'Written or electronic, each pay period: rate; gross and net; pay-period dates; FIT and FICA; AK ESA contributions; board/lodging deductions; advances; straight-time and overtime hours; other authorised deductions; sick leave used in accrual year; sick leave balance', 'US-AKS5-001')
F('psl.ak.sick_leave.on_statement', 'Sick leave used in the accrual year and sick leave balance on every statement (since 2025-09-25); a combined PTO plan satisfies it by showing PTO used and balance', 'US-AKS5-001', note='PTO equivalence per FAQ Q13 [US-AKS5-010].')
F('psl.ak.statement.electronic_delivery', 'Written or electronic; no separate consent rule', 'US-AKS5-001')
F('psl.ak.ssn.rule', 'SSN may not be printed on mailed material unless authorised by law (AS 45.48.400-.480); 8 AAC 15.160(h) does not require it: omit or truncate', 'US-AKS5-016')
F('psl.ak.retention.wage_hour.years', 3, 'US-AKS5-001', uom='years', note='AS 23.10.100; UI payroll records 5 years [US-AKS5-005].')
# AL
F('psl.al.statement.scope', 'none: no state pay-statement content statute; federal records rules apply', 'US-ALP52-001')
# AR
F('psl.ar.statement.scope', 'none: no itemised pay-statement statute; tipped employees get the tip-credit amount per hour in writing each time it changes (11 CAR 11)', 'US-ARP52-006', conf='medium')
F('psl.ar.retention.withholding_records.years', 6, 'US-ARP51-002', uom='years', note='Figure read in the registered local file (DFA Withholding Tax Instructions p.11 Recordkeeping), not in the row summary text.')
# AZ
F('psl.az.statement.scope', 'Statement (no content list) required only when paying by direct deposit or payroll card (A.R.S. 23-351(E),(F))', 'US-AZS5-001')
F('psl.az.sick_leave.on_statement', 'Every regular paycheck or attachment: earned paid sick time available, used to date in the year, and pay received as sick time (A.R.S. 23-375(C))', 'US-AZS5-011')
F('psl.az.retention.payroll_records.years', 4, 'US-AZS5-006', uom='years', note='A.R.S. 23-364(D): hours each day, wages, sick time paid.')
# CA
F('psl.ca.statement.content', 'Lab. Code 226(a), semimonthly or each payment: gross; total hours (not for salaried exempt); piece units and rates; deductions; net; pay-period dates; name + last 4 SSN or employee ID; employer legal name and address; each hourly rate with hours', 'US-CAS5-005')
F('psl.ca.sick_leave.on_statement', 'Available paid sick leave on the wage statement or a separate writing each payday', 'US-CAS5-011')
F('psl.ca.ssn.rule', 'Only the last 4 SSN digits or an employee ID (226(a)(7))', 'US-CAS5-005')
F('psl.ca.retention.wage_statements.years', 3, 'US-CAS5-005', uom='years')
F('psl.ca.penalty.max_per_employee', 4000, 'US-CAS5-005', cur='USD', note='50 first / 100 subsequent per violation up to 4,000; plus 750 for failing an inspection request.')
# CO
F('psl.co.statement.content', 'C.R.S. 8-4-103(4), at least monthly or each payment: gross; all withholdings and deductions; net; pay-period dates; employee name or SSN; employer name and address. COMPS Rule 7 adds rate, tips, credits and time worked', 'US-COP51-005', note='COMPS Rule 7 content per [US-COS5-001].')
F('psl.co.statement.comps_rule7', 'Statement shows total pay, rate, tips, credits and time worked; kept 3 years', 'US-COS5-001', conf='medium')
F('psl.co.ssn.rule', 'SSN may appear instead of the name (8-4-103(4)(e)); no truncation rule in the Wage Act', 'US-COP51-005', conf='medium', note='Build default: name, not SSN.')
# CT
F('psl.ct.statement.content', 'Each payment: hours worked; gross pay with straight time and overtime separate; itemised deductions; net (hours and split not for OT-exempt)', 'US-CTP51-005')
F('psl.ct.statement.electronic_delivery', 'Electronic only with the employee explicit consent, a secure private way to access and print, and confidentiality safeguards (31-13a(b))', 'US-CTS5-027')
F('psl.ct.pay_code_guide.url_on_pay_record', 'From 2026-10-01 (PA 26-12 sec. 38, 31-13a(c)): employers with 100+ employees publish a pay-code guide (overtime and common differentials, min 10 codes where applicable) in English, Spanish and other common languages; its URL appears on every pay record and is given at hire; a payroll provider guide satisfies it', 'US-CTS5-028', note='Codification lag: consolidated ch. 557 copy still lacks subsection (c); cite PA 26-12 sec. 38.')
F('psl.ct.pay_code_guide.employer_threshold', 100, 'US-CTS5-028', uom='employees')
F('psl.ct.retention.wage_records.years', 3, 'US-CTS5-027', uom='years')
# DC
F('psl.dc.statement.content', 'Each payment (32-1008(b)): date of payment; gross; deductions and additions with gratuities on a separate line; net; hours worked; tip declaration split cash/card; from 2026-01-01 a list of compensation sources beyond base wages and tips', 'US-DCS5-010')
F('psl.dc.retention.payroll_records.years', 3, 'US-DCS5-010', uom='years')
# DE
F('psl.de.statement.content', 'Employers with more than 3 employees, each payment: wages due; pay period; total deductions each separately specified; total hours for hourly employees (19 Del. C. 1108)', 'US-DES5-002')
F('psl.de.statement.employer_threshold', 'more than 3 employees', 'US-DES5-002')
F('psl.de.statement.electronic_delivery', 'On the check, a separate slip, or electronically if the employee can retain it; employee may ask for paper', 'US-DES5-002')
F('psl.de.retention.wage_records.years', 3, 'US-DES5-001', uom='years')
# FL
F('psl.fl.statement.scope', 'none for general employers; labor pools only (448.24(2)(g),(h)): itemised deductions each payment and annual earnings summary by 1 February', 'US-FLL-002')
# GA
F('psl.ga.statement.scope', 'none: O.C.G.A. 34-7-2 has no statement duty; GDOL handbook has no pay-stub rule', 'US-GAP9L-001', conf='medium')
F('psl.ga.retention.gdol_records.years', 7, 'US-GAS5-005', uom='years', note='O.C.G.A. 34-8-121 employment records incl. full SSN.')
# HI
F('psl.hi.statement.content', 'HRS 387-6(c), 14 items: employee name; employer name; employer address and phone; total hours; regular and OT hours; straight-time pay; OT pay; other compensation incl. allowances toward minimum wage; gross; amount and purpose of each deduction; net; pay date; pay period; rates and basis incl. OT and piece rates with counts', 'US-HIP52-001')
F('psl.hi.statement.electronic_delivery', 'Electronic with the employee written authorization; direct deposit still requires a statement', 'US-HIS5-007')
F('psl.hi.ssn.rule', 'Not required on the statement; HRS 487J-2 bars public display and mailing a visible full SSN', 'US-HIS5-028')
# IA
F('psl.ia.statement.content', 'Each regular payday: hours worked, wages earned, deductions (91A.6(4)); itemised computation within 10 working days on request', 'US-IAP51-002')
F('psl.ia.statement.electronic_delivery', 'Mail, secure electronic means, at the workplace, or access to view; no separate consent', 'US-IAP51-002')
F('psl.ia.statement.reach', 'Employees employed in Iowa (work location, not residence) (91A.2(3),(4))', 'US-IAS5-027')
F('psl.ia.retention.payroll_records.years', 3, 'US-IAP51-002', uom='years')
# ID
F('psl.id.statement.scope', 'deductions_only: written statement of deductions for each pay period with deductions (45-609(2))', 'US-IDP51-002')
F('psl.id.retention.employment_records.years', 3, 'US-IDS5-006', uom='years')
# IL
F('psl.il.statement.content', 'Pay stub each pay period with itemized deductions (820 ILCS 115/10 as amended by P.A. 103-953); payroll-card payees also get hours, rate and deductions', 'US-ILS5-024', note='Content list in 56 Ill. Adm. Code 300.600 not read.')
F('psl.il.statement.electronic_access', 'Stubs kept 3 years; copies within 21 days on request (max twice per 12 months; former employees for one year); if electronic stubs become inaccessible after separation, offer prior-year stubs by the final pay period and record the offer', 'US-ILS5-024')
F('psl.il.retention.pay_stubs.years', 3, 'US-ILS5-024', uom='years')
# IN
F('psl.in.statement.content', 'Each pay period at least hours worked, wages paid, deductions (IC 22-2-2-8(a))', 'US-INP6-001')
F('psl.in.statement.scope', 'Duty binds employers subject to IC 22-2-2 = 2+ employees NOT subject to the FLSA minimum wage (IC 22-2-2-3); literal reading excludes FLSA-covered employers; build emits hours/wages/deductions anyway', 'US-INS5-001', conf='low', note='Scope reading 70%.')
# KS
F('psl.ks.statement.scope', 'on_request: itemized statement of deductions on request for each pay period with deductions (K.S.A. 44-320(d))', 'US-KSP52-001')
F('psl.ks.retention.records.years', 3, 'US-KSS5-011', uom='years')
# KY
F('psl.ky.statement.content', 'Employers with 10+ employees that make deductions: each payment, paper or electronic statement of each deduction and its purpose; electronic requires access to a computer and printer (KRS 337.070)', 'US-KYP8-001')
F('psl.ky.statement.employer_threshold', 10, 'US-KYP8-001', uom='employees')
F('psl.ky.retention.pay_records.years', 1, 'US-KYP8-002', uom='years', note='KRS 337.320 minimum; federal 3-year rule is longer and governs the build.')
# LA
F('psl.la.statement.scope', 'none: no itemised pay-statement statute in R.S. 23:631-638; only the hire notice of rate, method and frequency', 'US-LAR3-002', conf='medium')
# MA
F('psl.ma.statement.content', 'Each payment (c.149 s.148): employer name; employee name; date; hours worked; hourly rate; deductions or increases for the period', 'US-MAP51-008')
F('psl.ma.retention.payroll_records.years', 3, 'US-MAS5-005', uom='years')
# MD
F('psl.md.statement.content', 'LE 3-504: employer name, address, phone; pay date and period; hours (unless exempt); rates; gross and net; each deduction by name and amount; other bases of pay; written or online', 'US-MDP51-005')
F('psl.md.sick_leave.on_statement', 'Available earned sick and safe leave balance each time wages are paid; an online balance system satisfies it (LE 3-1305(f))', 'US-MDS5-013')
F('psl.md.ssn.rule', 'No SSN at all on the wage check, any attachment, a direct-deposit notice or a card-credit notice (LE 3-502(d)); treat truncated SSN as barred too', 'US-MDS5-008', note='Stricter than truncation; no truncation safe harbour in the text.')
F('psl.md.statement.tip_credit', 'Tip Credit Wage Statement for restaurants', 'US-MDS5-007', conf='medium')
# ME
F('psl.me.statement.content', 'Each payment: date of the pay period, hours, total earnings, itemized deductions (26 MRSA 665(1))', 'US-MES5-006', note='Corrects earlier "no itemised duty" rows (US-MEP51-004 / -2-006 superseded).')
F('psl.me.statement.electronic_delivery', 'Electronic allowed only with ready access and printing at no cost; same record due when a direct deposit is made', 'US-MES5-006')
F('psl.me.retention.wage_records.years', 3, 'US-MES5-006', uom='years')
# MI
F('psl.mi.statement.content', 'At payment (MCL 408.479(2)): hours worked, gross, pay-period identification, separate itemisation of deductions; comp time earned or paid', 'US-MIS5-009', note='Comp time per US-MIS5-002. Hours may be omitted for EAP-exempt staff.')
F('psl.mi.ssn.rule', 'No more than 4 sequential SSN digits displayed (SSN Privacy Act, MCL 445.83/.84); employer must publish an SSN privacy policy', 'US-MIS5-013')
F('psl.mi.retention.records.years', 3, 'US-MIS5-009', uom='years')
# MN
F('psl.mn.statement.content', 'Earnings statement each pay period, 12 content items (181.032)', 'US-MNP6-001')
F('psl.mn.statement.electronic_delivery', 'Electronic requires access to an employer computer during work hours and statements kept available 3 years', 'US-MNP6-001')
F('psl.mn.sick_leave.on_statement', 'ESST hours available and used each pay period, on or attached to the statement or via an electronic system', 'US-MNS5-011')
F('psl.mn.retention.payroll_records.years', 3, 'US-MNS5-020', uom='years')
# MO
F('psl.mo.statement.scope', 'deductions_only: statement of total deductions at least monthly (290.080)', 'US-MOP52-002')
F('psl.mo.ssn.rule', 'No public display; SSN or (since 2016) last four digits may not be used as employee number (407.1355); no explicit pay-statement rule', 'US-MOS5-016')
F('psl.mo.retention.records.years', 3, 'US-MOP52-003', uom='years')
# MS
F('psl.ms.statement.scope', 'none: no MS statute requires a pay statement (US-OWN-006 recorded limit)', 'US-MSP9L-001', conf='medium')
F('psl.ms.retention.records.years', 3, 'US-MSS5-019', uom='years')
# MT
F('psl.mt.statement.content', 'Every payment: itemized statement of state and federal income tax, social security and other deductions with amounts; statement saying none if nothing deducted (MCA 39-3-101)', 'US-MTP51-006')
F('psl.mt.retention.payroll_tax_records.years', 5, 'US-MTS5-005', uom='years')
# NC
F('psl.nc.statement.scope', 'deductions_only: itemized statement of deductions each pay period with deductions (G.S. 95-25.13), plus hire wage notice', 'US-NCW1B-003')
F('psl.nc.statement.electronic_delivery', 'In writing, printable e-mail or any means the employee can keep; no separate consent', 'US-NCS5-024')
F('psl.nc.ssn.rule', 'G.S. 75-62: no SSN on mailed material unless law requires; safe build = truncated SSN', 'US-NCS5-016', conf='medium')
# ND
F('psl.nd.statement.content', 'Each pay period a check stub or pay voucher: hours worked, rate, required state and federal deductions, authorized deductions (NDAC 46-02-07-02(10))', 'US-NDS5-007', note='Reverses the earlier "no provision" reading (US-ND-003).')
# NE
F('psl.ne.statement.content', 'Each regular payday: employer identity, hours paid, wages earned, deductions (48-1230(2)); hours not required for FLSA-exempt unless OT/hours-based', 'US-NEP51-004')
F('psl.ne.ssn.rule', 'No more than the last 4 SSN digits displayed publicly or to coworkers (48-237)', 'US-NES5-013')
# NH
F('psl.nh.statement.scope', 'deductions_only: statement of deductions each pay period with a deduction (RSA 275:49 IV); written monthly accounting for 275:48 I(d) deductions', 'US-NHP51-001')
F('psl.nh.retention.records.years', 3, 'US-NHS5-003', uom='years')
# NJ
F('psl.nj.statement.content', 'Statement of deductions each pay period with deductions; employers with 10+ employees add gross, net, rate and hours where relevant (34:11-4.6(c))', 'US-NJP8-001')
F('psl.nj.statement.employer_threshold_full', 10, 'US-NJP8-001', uom='employees')
F('psl.nj.statement.electronic_delivery', 'Electronic allowed unless the employee asks for paper', 'US-NJP8-001')
F('psl.nj.retention.wage_hour.years', 6, 'US-NJS5-022', uom='years')
# NM
F('psl.nm.statement.content', 'Written receipt each payday: employer identity; gross; hours worked; total wages and benefits earned; itemized deductions (50-4-2(B))', 'US-NMP8-001')
F('psl.nm.sick_leave.on_statement', 'Year-to-date earned sick leave accrued and used, at least quarterly, on the earnings statement or electronically', 'US-NMS5-002')
# NV
F('psl.nv.statement.content', 'Itemized list of deductions at each payment (NRS 608.110(2))', 'US-NVR3-001')
F('psl.nv.paid_leave.on_statement', 'Accounting of available paid-leave hours on every payday, employers with 50+ NV employees (608.0197(1)(h))', 'US-NVS5-001')
F('psl.nv.paid_leave.employer_threshold', 50, 'US-NVS5-001', uom='employees')
F('psl.nv.retention.wage_records.years', 2, 'US-NVS5-001', uom='years')
# NY
F('psl.ny.statement.content', 'Labor Law 195(3), every payment: dates of work; names; employer address and phone; rates and basis; gross; deductions; allowances toward minimum wage; net; non-exempt: regular and OT rates and hours; piece rates and counts', 'US-NYS5-006')
F('psl.ny.retention.payroll_records.years', 6, 'US-NYS5-006', uom='years')
F('psl.ny.ssn.rule', 'Labor Law 203-d: no public display, no SSN on badges or time cards; not a required statement field', 'US-NYS5-009')
# OH
F('psl.oh.statement.content', 'ORC 4113.14 (from 2025-04-09), each pay period written or electronic: employee name and address; employer name; gross and net; amount and purpose of each addition and deduction; pay date and period; hourly employees hours and rate', 'US-OHP51-001')
F('psl.oh.retention.wage_hour.years', 3, 'US-OHS5-004', uom='years')
# OK
F('psl.ok.statement.scope', 'deductions_only: brief itemized statement of all deductions with each payment (40 O.S. 165.2)', 'US-OKS5-003')
F('psl.ok.ssn.rule', 'No SSN on materials mailed to the employee unless law requires (40 O.S. 173.1); mask on mailed payslips', 'US-OKS5-008')
F('psl.ok.retention.payroll_tax_records.years', 4, 'US-OKS5-014', uom='years')
# OR
F('psl.or.statement.content', 'ORS 652.610(1)(b): payment date; dates of work; employee name; employer name and registry/ID number; employer address and phone; rates; basis; gross; net; each deduction with amount and purpose; allowances toward minimum wage; non-exempt regular and OT rates, hours and pay; piece rates and counts', 'US-ORS5-026')
F('psl.or.statement.electronic_delivery', 'Electronic only with the employee express agreement and ability to print or store on receipt (652.610(1)(c))', 'US-ORS5-026')
F('psl.or.new_hire_explanation', 'From 2026-01-01 (SB 906): written explanation of earnings and deductions incl. all payroll codes at hire, updated by 1 January each year', 'US-ORS5-022')
F('psl.or.retention.records.years', 2, 'US-ORS5-019', uom='years')
# PA
F('psl.pa.statement.content', 'Every payment: hours worked, rates, gross, allowances toward minimum wage, deductions, net (34 Pa. Code 231.36)', 'US-PAP51-001')
F('psl.pa.ssn.rule', 'Act 60 of 2006: no SSN on mailed materials unless law requires; mailed stubs omit the SSN', 'US-PAS5-020')
# RI
F('psl.ri.statement.content', 'Every regular payday: hours worked (except 28-12-4.3 exempt), every deduction with explanation; commercial construction also regular hourly rate (28-14-2.1); electronic allowed, free printed copy on written request', 'US-RIP51-002')
F('psl.ri.ssn.rule', 'No part of the SSN on material mailed to the individual unless law requires (6-48-8)', 'US-RIS5-020')
# SC
F('psl.sc.statement.content', 'Itemized statement of gross pay and deductions each pay period (41-10-30(C)); direct deposit: statement of earnings and withholdings (41-10-40(B))', 'US-SCP52-006')
F('psl.sc.statement.exemptions', 'Domestic labour in private homes and employers with fewer than 5 employees at all times in the preceding 12 months are exempt (41-10-20)', 'US-SCP52-006')
F('psl.sc.ssn.rule', 'No 6 or more SSN digits on mailed material or public display (37-20-180): mailed statements show 5 digits at most', 'US-SCS5-009')
F('psl.sc.retention.wage_records.years', 3, 'US-SCP52-006', uom='years')
# SD
F('psl.sd.statement.scope', 'none: no SD statute requires a pay statement (Title 60 full-text scan)', 'US-SDS5-001')
# TN
F('psl.tn.statement.scope', 'none: no TN itemised pay-statement statute located; federal records rules', 'US-TNS5-001', conf='medium')
# TX
F('psl.tx.statement.scope', 'non_flsa_only: Labor Code 62.003 earnings statement (name, rate, gross, each deduction and purpose, net, hours or units; signed by employer or agent) applies only to employees not covered by the FLSA (62.151); best practice for everyone else', 'US-TXS5-003', conf='medium', note='Corrects the sealed US-MQ-63 part 6 line "no pay-statement requirement".')
F('psl.tx.ssn.rule', 'Bus. & Com. Code 501.001: no SSN on mailed material unless law requires; mask on paper payslips', 'US-TXS5-013', conf='medium')
# UT
F('psl.ut.statement.scope', 'deductions_only: statement of each deduction on each regular payday (34-28-3(4)); construction-trade licensees full statement (34-28-3(5))', 'US-UTP6-001')
F('psl.ut.statement.format', 'All lawful offsets itemized on a statement or detachable check stub (R610-3-20)', 'US-UTS5-012')
# VA
F('psl.va.statement.content', 'Each regular pay date, paystub or online accounting: employer name and address; hours (hourly and salaried below the FLSA level); rate; gross; amount and purpose of each deduction; enough detail to work out gross and net', 'US-VAS5-003')
F('psl.va.retention.pay_statements.years', 3, 'US-VAS5-003', uom='years')
# VT
F('psl.vt.statement.content', 'Detailed written statement with each weekly pay: gross, hours, hourly rate, itemised deductions incl. meals', 'US-VTP9-001')
F('psl.vt.ssn.rule', 'No full SSN on mailed materials (9 V.S.A. 2440); redacted SSN permitted', 'US-VTS5-015')
# WA
F('psl.wa.statement.content', 'Every payday, separate from the paycheck: hours or days worked, rates, gross, all deductions, pay period, payment date (WAC 296-126-040)', 'US-WAS5-004')
F('psl.wa.sick_leave.on_statement', 'At least monthly: paid sick leave accrued, used and available; may be on the regular pay statement (WAC 296-128-755(2))', 'US-WAS5-005')
F('psl.wa.statement.electronic_delivery', 'Electronic if the employee can receive and copy it on payday; otherwise paper', 'US-WAS5-004')
F('psl.wa.retention.esd_records.years', 4, 'US-WAS5-030', uom='years')
# WI
F('psl.wi.statement.content', 'Hours worked, rate, amount and reason for each deduction, on the check, envelope or accompanying paper; coding system allowed (103.457; DWD 272.10)', 'US-WIP52-001')
F('psl.wi.retention.payroll_records.years', 3, 'US-WIS5-002', uom='years')
# WV
F('psl.wv.statement.content', 'Scheduled payday itemized statement: hourly rate or salary; hours paid; OT rate; bonus or incentive pay; itemized deductions (42 CSR 5 s.7.3, sunset 2029-07-01)', 'US-WVS5-008')
F('psl.wv.retention.payroll_records.years', 5, 'US-WVS5-008', uom='years')
# WY
F('psl.wy.statement.scope', 'deductions_only: detachable part of the check or attached slip with an itemized statement of all deductions (27-4-101(b)); agricultural operations exempt', 'US-WYP51-005')
F('psl.wy.retention.payroll_records.years', 2, 'US-WYS5-001', uom='years')

facts, blocked, unresolved, consumed = build(S, 'PSL', '8_sheets')

# open items from stage5 open questions / access gaps (no active row carries a value)
U = [
 ('psl.ca.statement.electronic_consent', 'CA Lab. Code 226 says "in writing"; no electronic-consent rule fetched', 'Labor Commissioner FAQ on electronic wage statements (dir.ca.gov) read on the official host'),
 ('psl.co.statement.electronic_consent', 'No Colorado statute or rule on electronic pay-statement consent was read', 'CDLE COMPS Order / Wage Act rule on electronic statements read on cdle.colorado.gov'),
 ('psl.ma.statement.electronic_consent', 'AG rule on electronic pay stubs not located; s.148 silent', 'Massachusetts AG Fair Labor Division advisory on electronic pay stubs'),
 ('psl.ny.statement.electronic_consent', 'Labor Law 195(3) silent; NYDOL guidance on electronic statements not read', 'NYDOL Wage Theft Prevention Act FAQ on electronic pay statements'),
 ('psl.nyc.pto.on_statement', 'NYC accrued/used/balance on each pay statement rests only on a tier-B lead (US-NYS5-023 MANUAL)', 'NYC Admin. Code 20-919 / DCWP ESSTA rule text on the official host'),
 ('psl.ri.retention_and_hire_notice_2026', 'New R.I.G.L. 28-14-12 (eff. 2026-01-01, H 5679 of 2025) not reachable; 2026 record-keeping and hire-notice fields unconfirmed (US-RIS5-008 partial)', 'Official text of R.I.G.L. 28-14-12 as amended (webserver.rilegislature.gov)'),
 ('psl.il.statement.content_rule_300_600', '56 Ill. Adm. Code 300.600 full content list not read', '56 Ill. Adm. Code 300.600 from ftp.ilga.gov / JCAR'),
 ('psl.nv.statement.electronic_consent', 'No Nevada statute on electronic pay statements located', 'NRS 608 / NAC 608 read for electronic delivery, or Nevada Labor Commissioner guidance'),
 ('psl.ssn_rule.unread_states', 'SSN display/truncation statutes not read for CO (6-1-713), DC (28-3851), IL (PIPA, 815 ILCS 505), IA (715A), ID (28-51), KY, LA, MA (93H/201 CMR 17), ME (10 MRSA 1346), NJ (C.56:8-164, ACCESS gap), NM (57-12B, 403), TN (47-18-2110), UT (13-45), WV; absence on pay statements is not proven there', 'One targeted read per statute on the official legislature host; build default meanwhile: last 4 digits at most, none in MD'),
 ('psl.nc.retention.withholding_records.years', 'Stage-5 NC.md cites 10 years (NC-30 s.26) under US-NC-001, but that row text does not carry the figure and has no local file', 'Re-register NC-30 (2026) section 26 with the 10-year figure in figure_or_rule_carried'),
 ('psl.in.statement.scope_confirmation', 'IC 22-2-2-3 literal reading excludes FLSA-covered employers from the 22-2-2-8 pay-statement duty; no DOL/agency commentary read (70%)', 'Indiana DOL Wage and Hour guidance on IC 22-2-2-8 applicability'),
 ('psl.tx.statement.scope_confirmation', 'Applying Labor Code 62.151 to limit 62.003 to non-FLSA employees has no TWC commentary read', 'TWC Labor Law guidance page on 62.003 / pay statements'),
]
for k, why, close in U:
    unresolved.append({'key': k, 'why': why, 'what_would_close_it': close, 'blocking': False})

extra = {
 '_owner_decisions': [
  {'register_id': 'US-OWN-006', 'decision': 'Payslip in English (first_build en); authority-facing filings in English; es rank 2 = mandatory-later for statutory notice/poster templates, documented seam for the payslip; other languages are per-state template seams. Decided 2026-11-01 under owner delegation.'},
  {'register_id': 'US-OWN-005', 'decision': 'All federal special populations IN (ordinary, NRA, statutory, household, agricultural, clergy, employees abroad); state-level special-population rules deferred to a later round. 1099-NEC contractors OUT.'}],
 '_source_partial_or_unusable_rows_seen': ['US-NYS5-023 (MANUAL B)', 'US-MSP52-004 (MANUAL B)', 'US-GAP52-002 (MANUAL B)', 'US-GAS5-018 (MANUAL B)', 'US-RIS5-008 (partial)', 'US-TXLAB-001 (MANUAL)', 'US-WVLAB-001 (superseded)'],
}
out = BASE + '/_research/PSL-facts.json'
write(out, 'PSL', '8_sheets', facts, blocked, unresolved, extra)
print('facts', len(facts), 'blocked', len(blocked), 'unresolved', len(unresolved))
print('consumed', ';'.join(sorted(consumed)))
