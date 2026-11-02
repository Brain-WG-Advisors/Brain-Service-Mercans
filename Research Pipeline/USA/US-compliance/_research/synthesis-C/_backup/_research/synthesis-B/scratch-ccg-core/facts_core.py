# Fact definitions for CCG m01..m13 + coverage (exec'd by build.py; F/U/P/USD in scope)
D = 'derived arithmetically'; S2 = 'second independent authority'

# ================= m01_foundational =================
u = 'm01_foundational'
F(u, 'fit.legal_basis.withholding_statute', '26 U.S.C. 3402: employer withholds federal income tax per tables/procedures prescribed by the Secretary (federal tax only)', 'US-FED-012')
F(u, 'fica.legal_basis.return_period', 'calendar quarter (Form 941); agricultural labor annual; Form 944 annual option', 'US-FED-015')
F(u, 'futa.legal_basis.rate_statute', '26 U.S.C. 3301: 6 percent of total wages paid during the calendar year', 'US-FED-013')
F(u, 'futa.legal_basis.state_credit', 'State UI contributions credited against FUTA, capped at 90% of the tax; credit reduced for states with outstanding Title XII advances', 'US-FED-014')
F(u, 'tax_year.basis', 'calendar year (W-2 on calendar-year basis)', 'US-FED-006')
F(u, 'flsa.relation_to_state_law', 'FLSA does not excuse a higher state/municipal minimum wage, lower maximum workweek or stricter child-labour standard: the more protective standard of the place whose law applies prevails', 'US-MULTIS5-008')
F(u, 'language.official.federal', 'English designated official language (presidential action 2025-03-01); no obligation on private employers', 'US-FED-020', note='Payslip/authority-facing language rule is the owner decision US-OWN-006 (MANDATE US-MQ-03): payslip in English, es seam for notices; owner rows cannot be fact register_ids (tier owner).')
F(u, 'sit.no_wage_tax.tx', True, 'US-TXS5-001', note='Tex. Const. art. 8 sec. 24-a: no tax on net incomes of individuals. No-wage-tax set: AK, FL, NV, NH, SD, TN, TX, WA, WY (MULTI.md 2.1); AK/FL/WY facts carried by their annexes.')
F(u, 'sit.no_wage_tax.wa', True, 'US-WAS5-017', note='WA has no individual income tax in 2026; a 9.9% tax on individuals with AGI over USD 1M is enacted from 2028-01-01 (assessment level; not modelled in 2026 payroll).', ef='2026-01-01', et='2027-12-31')
F(u, 'sit.no_wage_tax.nv', True, 'US-NV-001')
F(u, 'sit.no_wage_tax.sd', True, 'US-SD-001')
F(u, 'sit.no_wage_tax.tn', True, 'US-TN-001', note='Hall tax on interest/dividends repealed from 2021-01-01; never a wage tax.')
F(u, 'sit.no_wage_tax.nh', True, 'US-NHP9W-003')
F(u, 'live.mobile_workforce_bill.status', 'S. 1443 (introduced 2025-04-10, Senate Finance) and H.R. 10271 (introduced 2026-09-03, House Judiciary): draft, NOT enacted - do not model', 'US-MULTIS5-020', note='Companion H.R. 10271 = US-MULTIS5-025. Level if enacted: state withholding and tax (residence State + State of >30 days presence).')
F(u, 'oracle.federal.source', 'IRS Pub. 15-T (2026): only two worked examples (NRA weekly 300 -> 31; tribal 6,000 -> 584.09); Stage 9b re-derives from Worksheet 1A + Annual Percentage Method tables', 'US-FED-027')
F(u, 'oracle.federal.not_an_oracle', 'IRS Tax Withholding Estimator is an employee tool, not an employer withholding engine - not an oracle', 'US-FED-021')
U(u, 'sit.no_wage_tax.ak', 'The AK no-wage-tax row (US-AK-WT-002) has an id that fails the facts.schema register_id pattern; no other AK row states it directly.', 'Annex AK worker cites it in prose, or the contract owner widens the register_id pattern (see report: 407 active/partial ids affected).')
U(u, 'sit.no_wage_tax.fl', 'No FL register row with a schema-valid id states the absence of a wage income tax (FL findings carry it in prose).', 'Annex FL fact citing Fla. Const. art. VII s.5 if a row exists, or a new register row in the merge.')
U(u, 'sit.no_wage_tax.wy', 'No WY register row with a schema-valid id states the absence of a wage income tax.', 'Annex WY fact or a register row for the WY DOR statement.')

# ================= m02_master_data =================
u = 'm02_master_data'
F(u, 'w4.fields', 'Step 1(c) filing status (Single/MFS, MFJ/QSS, HoH); Step 2 multiple-jobs checkbox; Step 3 dependents amount; Step 4(a) other income; 4(b) deductions; 4(c) extra withholding; exempt checkbox below 4(c)', 'US-FEDS5-006', ef='2026-01-01', et='2026-12-31')
F(u, 'w4.exempt.expiry', 'Exempt status lapses each year: a new 2027 W-4 is required to keep exemption', 'US-FEDS5-006')
F(u, 'w4.nra.rules', 'NRA: check Single/MFS, write NRA below Step 4(c), may not claim exempt; Step 3 only for residents of Canada, Mexico, South Korea or India', 'US-FEDS5-015')
F(u, 'w4.pre2020.allowance.annual', 4300, 'US-FEDS5-001', cur=USD)
F(u, 'newhire.deadline.days', 20, 'US-FEDS5-024', uom='days', note='Federal maximum; many states shorter (e.g. AL/ME 7 days, RI 14 days - annexes).')
F(u, 'newhire.fields.federal', 'employee name, address, SSN, date services first performed; employer name, address, FEIN', 'US-FEDS5-024')
F(u, 'newhire.multistate.designation', 'Employer with employees in 2+ States reporting electronically may designate ONE State for all new-hire reports after written notice to HHS', 'US-MULTIS5-006')
F(u, 'ssn.truncation.w2', 'SSN may be truncated (XXX-XX-1234) on employee W-2 copies only; never on Copy A; EIN never truncated', 'US-FEDS5-022')
F(u, 'records.flsa.retention.years', 3, 'US-FEDS5-021', uom='years')
F(u, 'routing.sui_state.test', 'Localization test in order: (1) service localized in a State; (2) base of operations; (3) direction or control; (4) residence', 'US-MULTIS5-017', note='Second document: UIPL 20-04 (US-MULTIS5-016). Drives the sui_state routing key; WA PFML follows the same test (US-MULTIS5-024).')
F(u, 'routing.work_location.rule', 'Wages taxed by the State where services are physically performed, plus the residence State on all wages with a resident credit (assessment); exceptions: convenience States, reciprocity, federal transport/military-spouse limits', 'US-MULTIS5-023', note='IL Pub. 130 restates the sourcing; general rule per MULTI.md 2.1. Routing keys: work_location_jurisdiction, residence_jurisdiction, sui_state.')
F(u, 'cert.ct.default_no_certificate', 'No CT-W4 -> withhold flat 6.99% without exemption', 'US-CTS5-011', note='Example of a state certificate default; each annex carries its own (CA DE 4: Single 0 allowances, US-CAS5-004).')
F(u, 'cert.ca.default_no_certificate', 'No valid DE 4 -> Single, zero allowances; federal W-4 is for FIT only since 2020', 'US-CAS5-004')

# ================= m03_gross_to_net =================
u = 'm03_gross_to_net'
F(u, 'fit.worksheet1a.line1g.mfj', 12900, 'US-FEDS5-001', cur=USD, note='Applied when W-4 Step 2 box is NOT checked.')
F(u, 'fit.worksheet1a.line1g.other', 8600, 'US-FEDS5-001', cur=USD)
F(u, 'fit.rounding.optional', 'Wages may be rounded to nearest dollar; per-period tax may be rounded to nearest dollar (optional)', 'US-FED-001')
F(u, 'rpt.941.amounts_in_cents', 'Form 941: do not round to whole dollars, always show cents', 'US-FED-005')
F(u, 'gtn.order.al_fit_before_sit', 'Alabama deducts federal income tax withheld from the state base: compute FIT before AL SIT', 'US-ALS5-001')
F(u, 'gtn.order.or_federal_subtraction_cap', 8750, 'US-ORS5-009', cur=USD, note='OR subtracts federal tax withheld (cap 8,750; phase-out by income). DOR 2026 publication also prints 8,500 in places - use 8,750 (pp.6-7 formula).')
F(u, 'gtn.ia.rounding', 'Iowa 2026 withholding computed to the cent (not rounded to the dollar)', 'US-IAS5-005', note='Supersedes the rounding clause of US-IA-001 (S5A-MERGE).')
F(u, 'gtn.oh.municipal_base', 'Ohio municipal income tax base = Medicare wages less 125 deductions; 401(k) deferrals taxable', 'US-OHS5-001', check=False, conf='medium', note='From the OH findings (journal round A); row carries the state formula; annex OH holds the municipal rows.')
F(u, 'fica.employee.oasdi.rate', 6.2, 'US-FEDS5-005', uom=P, ef='2026-01-01', et='2026-12-31')
F(u, 'fica.employee.medicare.rate', 1.45, 'US-FEDS5-005', uom=P)
F(u, 'fica.employee.addl_medicare.rate', 0.9, 'US-FEDS5-005', uom=P)

# ================= m04_compensation =================
u = 'm04_compensation'
F(u, 'minwage.federal.hourly', 7.25, 'US-FEDS5-017', cur=USD, note='Not indexed; no 2026/2027 change enacted. Employer pays the highest of federal, state and local.')
F(u, 'ot.federal.multiplier', 1.5, 'US-FEDS5-018', uom='ratio')
F(u, 'ot.federal.weekly_threshold_hours', 40, 'US-FEDS5-018', uom='hours', note='No federal daily overtime.')
F(u, 'tip.federal.threshold_monthly', 30, 'US-FEDS5-019', cur=USD)
F(u, 'tip.federal.cash_wage.hourly', 2.13, 'US-FEDS5-019', cur=USD)
F(u, 'tip.federal.max_tip_credit', 5.12, 'US-FEDS5-019', cur=USD)
F(u, 'flsa.eap.salary_floor.weekly', 684, 'US-FEDS5-020', cur=USD, note='Territories 455; American Samoa 380. 2024 increase vacated (Nov 2024) and not in eCFR.')
F(u, 'minwage.state.ca.hourly', 16.90, 'US-CAS5-006', cur=USD)
F(u, 'minwage.state.ca.hourly', 17.40, 'US-CAS5-007', cur=USD, ef='2027-01-01')
F(u, 'minwage.state.wa.hourly', 17.13, 'US-WAS5-006', cur=USD, et='2026-12-31')
F(u, 'minwage.state.wa.hourly', 17.73, 'US-WAS5-007', cur=USD)
F(u, 'minwage.state.ny.nyc_li_westchester.hourly', 17.00, 'US-NYS5-001', cur=USD, note='Remainder of state 16.00; unchanged on 2027-01-01 (off-ramp).')
F(u, 'minwage.state.ny.rest.hourly', 16.00, 'US-NYS5-001', cur=USD)
F(u, 'minwage.state.fl.hourly', 15.00, 'US-FLS5-001', cur=USD, ef='2026-09-30', note='14.00 before 2026-09-30; Fla. Stat. 448.110 still prints 6.15 (stale) - follow the Constitution.')
F(u, 'minwage.state.tx.hourly', 7.25, 'US-TXS5-002', cur=USD)
F(u, 'minwage.state.dc.hourly', 18.40, 'US-DCS5-011', cur=USD, ef='2026-07-01', note='17.95 until 2026-06-30; indexed each July 1 (CPI-U Washington MSA, nearest 0.05). Mid-year change.')
F(u, 'minwage.state.or.standard.hourly', 15.55, 'US-ORS5-002', cur=USD, ef='2026-07-01', et='2027-06-30', note='Metro 16.80, nonurban 14.55; 15.05 until 2026-06-30. Mid-year change.')
F(u, 'minwage.state.ak.hourly', 14.00, 'US-AKS5-001', cur=USD, ef='2026-07-01', et='2027-06-30', note='15.00 from 2027-07-01; no tip credit; daily OT over 8h.')
F(u, 'minwage.state.nj.general.hourly', 15.92, 'US-NJS5-009', cur=USD)
F(u, 'ot.state.ca.rule', 'Daily: 1.5x over 8h/day and first 8h of 7th consecutive day; 2x over 12h/day and over 8h on 7th day; weekly 1.5x over 40h', 'US-CAS5-008')
F(u, 'ot.state.nv.daily_threshold_wage', 18.00, 'US-NVS5-003', cur=USD, note='From 2026-07-01 employees earning under 18.00/h get 1.5x over 8h in 24h.')
F(u, 'ot.federal.qualified_overtime.deduction_level', 'assessment (employee return); withholding only via W-4 Step 4(b); employer reports W-2 Box 12 TT; overtime remains fully subject to FICA', 'US-FEDS5-030')

# ================= m05_social_security =================
u = 'm05_social_security'
F(u, 'fica.oasdi.wage_base', 184500, 'US-FEDS5-005', cur=USD, ef='2026-01-01', et='2026-12-31', vm=S2, note='Second document family: SSA FR notice US-FED-003 (AWI derivation 60,600 x 69,846.57/22,935.42 = 184,548.71 -> 184,500).')
F(u, 'fica.oasdi.wage_base', 192300, 'US-FED-022', cur=USD, ef='2027-01-01', conf='medium', note='SSA published 2027 value; re-verification blocked (ssa.gov 403 on 2026-11-02) - FED open question 3.')
F(u, 'fica.employer.oasdi.rate', 6.2, 'US-FEDS5-005', uom=P)
F(u, 'fica.employer.medicare.rate', 1.45, 'US-FEDS5-005', uom=P)
F(u, 'fica.addl_medicare.threshold', 200000, 'US-FEDS5-005', cur=USD, note='Per employer, calendar year, regardless of filing status; no employer match.')
F(u, 'futa.rate.gross', 6.0, 'US-FED-007', uom=P)
F(u, 'futa.rate.max_credit', 5.4, 'US-FED-007', uom=P)
F(u, 'futa.rate.net', 0.6, 'US-FED-007', uom=P)
F(u, 'futa.wage_base', 7000, 'US-MULTIS5-009', cur=USD, note='Per employer per calendar year across all States; successor carry-over.')
F(u, 'futa.credit_reduction.ca', 1.2, 'US-FEDS5-009', uom=P, ef='2025-01-01', et='2025-12-31', note='FINAL for 2025 (Form 940 Schedule A). 2026 potential CA 5.3% / USVI 4.8% final only if advance unpaid on 2026-11-10 - unresolved.')
F(u, 'futa.credit_reduction.vi', 4.5, 'US-FEDS5-009', uom=P, ef='2025-01-01', et='2025-12-31')
F(u, 'sui.ca.wage_credit_other_state', 'CUIC 930.1: wages reported to another State count toward the CA UI base in the same year on transfer to CA', 'US-MULTIS5-010')
F(u, 'sui.wa.wage_base', 78200, 'US-WAS5-012', cur=USD)
F(u, 'sui.ak.wage_base', 54200, 'US-AKS5-003', cur=USD)
F(u, 'sui.ak.employee.rate', 0.50, 'US-AKS5-003', uom=P, note='Employee UI contributions exist only in AK, NJ, PA (DOL Comparison 2023, row id fails pattern; NJ/PA rates in annexes).')
F(u, 'pfml.wa.total.rate', 1.13, 'US-WAS5-015', uom=P, ef='2026-01-01', et='2026-12-31', note='Row US-WAS5-015 is dated 2027-01-01 but carries both years; 2026 = 1.13%. Split 29.3% employer / 70.7% employee (annex WA).')
F(u, 'pfml.wa.total.rate', 1.2, 'US-WAS5-015', uom=P, ef='2027-01-01')
F(u, 'pfml.dc.employer.rate', 0.75, 'US-DCS5-020', uom=P, note='Employer only, no wage cap.')
F(u, 'pfml.ma.total.rate', 0.88, 'US-MAS5-012', uom=P, note='25+ covered individuals; <25: 0.46%. Cap = SS wage base.')
F(u, 'pfml.ma.split.2026', 'family 0.18% (up to 100% from employee) + medical 0.70% (employee up to 40% = 0.28%, employer 0.42%)', 'US-MAS5-012', ef='2026-01-01', et='2026-12-31',
  note='DECISION (synthesis B, 2026-11-02): payroll follows DFML - 2026 split unchanged, swap from 2027-01-01. Ch. 101/2026 s.45 (US-MAS5-026) makes ss.25-26 apply "for taxable years beginning on or after January 1, 2026"; read on the Act text, s.45 is the tax-year commencement clause shared with the c.62/c.63 provisions, while c.175M contributions are set by DFML under s.7(e) per calendar year and the Act (approved 2026-06-12) gives no retroactive re-split mechanism. Employee maximum share is 0.46% under both DFML years. Residual risk recorded as unresolved pfml.ma.split.effective_date.')
F(u, 'pfml.ma.split.2027', 'family 0.70% (employee up to 40% = 0.28%, employer 0.42%) + medical 0.18% (up to 100% from employee); total 0.88%', 'US-MAS5-012', ef='2027-01-01')
F(u, 'household.fica.threshold', 3000, 'US-FEDS5-029', cur=USD, note='Cash wages in 2026; FUTA if 1,000+ in any quarter.')
F(u, 'household.futa.quarter_threshold', 1000, 'US-FEDS5-029', cur=USD)
F(u, 'pfml.benefits.w2_treatment', 'State PFML: employee contribution and employer voluntary payment are W-2 wages (Rev. Rul. 2025-4, Notice 2026-6)', 'US-FEDS5-007')

# ================= m06_tax =================
u = 'm06_tax'
# Full Pub. 15-T 2026 bracket tables (STANDARD and Step-2) are carried by annex_FED keys fed.fit.standard.* / fed.fit.step2.* - not duplicated here.
F(u, 'fit.std_deduction.single', 16100, 'US-FEDS5-010', cur=USD, note='Zero bracket = std deduction - line 1g (16,100 - 8,600 = 7,500), re-derived in FED unit.')
F(u, 'fit.std_deduction.mfj', 32200, 'US-FEDS5-010', cur=USD)
F(u, 'fit.std_deduction.hoh', 24150, 'US-FEDS5-010', cur=USD)
F(u, 'fit.supplemental.flat.rate', 22, 'US-FEDS5-003', uom=P, note='Optional.')
F(u, 'fit.supplemental.mandatory.rate', 37, 'US-FEDS5-003', uom=P)
F(u, 'fit.supplemental.mandatory.threshold', 1000000, 'US-FEDS5-003', cur=USD)
F(u, 'fit.backup.rate', 24, 'US-FEDS5-003', uom=P)
F(u, 'fit.nra.addon.table2.annual', 16100, 'US-FEDS5-002', cur=USD, note='Added to wages for withholding computation only; not on W-2; no FICA/FUTA effect; not applied to 22%/37% supplemental.')
F(u, 'fit.nra.addon.table2.weekly', 309.60, 'US-FEDS5-002', cur=USD)
F(u, 'fit.nra.addon.table1.annual', 11800, 'US-FEDS5-002', cur=USD)
F(u, 'fit.nra.commercial_traveler.max_days', 90, 'US-FEDS5-016', uom='days', note='And pay <= 3,000 from a foreign employer not engaged in US trade/business.')
F(u, 'fit.nra.commercial_traveler.max_pay', 3000, 'US-FEDS5-016', cur=USD)
F(u, 'fit.nra.treaty.reporting', 'Treaty-exempt wages claimed on Form 8233 are reported on Form 1042-S, not W-2 box 1; 2026 1042-S e-filed via IRIS', 'US-FEDS5-016')
F(u, 'fit.pl119_21.tips_overtime.level', 'assessment; withholding only via W-4 Step 4(b); employer reporting W-2 TP/TT/14b; FICA unchanged', 'US-FEDS5-030')
# state structure examples (annexes hold full tables)
F(u, 'sit.ga.statutory_rate', 4.99, 'US-GAS5-009', uom=P, note='5.19% before; 2026 withholding tables changed mid-year (GA annex: 2026-05-11). 2027 step conditional on OPB report 2026-12-01.')
F(u, 'sit.in.rate', 2.95, 'US-INS5-009', uom=P, note='2027 2.90%. County rates change in January and October (DN#1 R47/10-26).')
F(u, 'sit.ut.rate', 4.45, 'US-UTS5-001', uom=P)
F(u, 'sit.oh.statutory', 'TY2026 flat 2.75% above 26,050 (ORC 5747.02 as amended by HB 96); withholding tables still graduated to 3.4% - two instruments', 'US-OHS5-007')
F(u, 'sit.oh.withholding_tables.effective_from', '2026-08-01', 'US-OHS5-001')
F(u, 'sit.md.top_rate', 6.50, 'US-MDS5-001', uom=P, ef='2025-01-01', note='Plus county tax (24 counties, max 3.30%; MD annex).')
F(u, 'sit.reciprocity.pa.partners', 'IN, MD, NJ, OH, VA, WV (REV-419)', 'US-MULTI-007')
F(u, 'sit.reciprocity.va.partners', 'DC, KY (daily commuters), MD, PA, WV', 'US-MULTI-004')
F(u, 'sit.reciprocity.oh.partners', 'IN, KY, MI, PA, WV', 'US-MULTI-005')
F(u, 'sit.reciprocity.wi.partners', 'IL, IN, KY, MI (W-220)', 'US-MULTI-006')
F(u, 'sit.reciprocity.md.partners', 'DC, PA, VA, WV (not if abode >6 months and 183+ days, except WV)', 'US-MULTI-008')
F(u, 'sit.reciprocity.ky.partners', 'IL, IN, MI, OH (unless 20% S-corp owner), VA (daily commuters), WV, WI (42A809)', 'US-MULTI-009')
F(u, 'sit.reciprocity.mi.partners', 'IL, IN, KY, MN, OH, WI', 'US-MULTI-010')
F(u, 'sit.reciprocity.nj.partners', 'PA (compensation only; NJ-165)', 'US-MULTI-011')
F(u, 'sit.reciprocity.mn.partners', 'MI, ND (monthly return home; yearly MWR)', 'US-MULTI-013')
F(u, 'sit.reciprocity.nd.partners', 'MN, MT (yearly NDW-R)', 'US-MULTI-014')
F(u, 'sit.reciprocity.wv.partners', 'KY, MD, OH, PA, VA (WV/IT-104)', 'US-MULTI-015')
F(u, 'sit.reciprocity.ia.partners', 'IL only (IA 44-016 / IL-W-5-NR)', 'US-MULTI-018')
F(u, 'sit.reciprocity.de.partners', 'none', 'US-MULTI-019')
F(u, 'sit.reciprocity.az.unilateral', 'AZ exempts residents of CA, IN, OR, VA (Form WEC); one-way, not reciprocal', 'US-MULTI-017')
F(u, 'sit.nonres_threshold.az.days', 60, 'US-MULTI-017', uom='days')
F(u, 'sit.nonres_threshold.al.days', 30, 'US-MULTI-021', uom='days', note='Act 2025-334; only if home State has a similar exclusion or no PIT; day 31+ = all AL wages for the year.')
F(u, 'sit.nonres_threshold.la.days', 30, 'US-MULTIS5-021', uom='days', ef='2026-01-01', note='Act 382 (2025); from day 31 withhold for every day incl. first 30; adopted rule LR 52:358 (2026-03-20, US-LAS5-002).')
F(u, 'sit.nonres_threshold.il.working_days', 30, 'US-MULTIS5-023', uom='days', note='More than 30 working days, non-localized service; localization rules first.')
F(u, 'sit.nonres_threshold.wv.days', 30, 'US-MULTI-015', uom='days')
F(u, 'sit.convenience.ny', '20 NYCRR 132.18(a): out-of-NY days count only if of necessity; home-office days are NY days unless bona fide employer office', 'US-MULTIS5-013')
F(u, 'sit.convenience.pa', '61 Pa. Code 109.8 necessity test (PA reciprocal agreements prevail)', 'US-MULTIS5-014')
F(u, 'sit.convenience.de', 'Working from home does not qualify for the PIT-SCW exclusion (assessment level)', 'US-MULTIS5-015')
F(u, 'sit.convenience.nj', 'From 2023 NJ applies the convenience rule against residents of States that apply one (DE, NE, NY; CT by reciprocal law); PA excluded', 'US-MULTI-012')
F(u, 'sit.convenience.ct', 'From 2019 CT applies the resident-State convenience test to nonresidents working for a CT employer', 'US-MULTI-020')
F(u, 'sit.transport.motor_carrier', 'Residence State only (2+ States, 49 U.S.C. 14503)', 'US-MULTIS5-001')
F(u, 'sit.transport.rail', 'Residence State only (49 U.S.C. 11502)', 'US-MULTIS5-002')
F(u, 'sit.transport.air', 'Residence State + State where >50% of pay earned (scheduled flight time) (49 U.S.C. 40116(f))', 'US-MULTIS5-003')
F(u, 'sit.transport.seamen', 'No State withholding on seamen wages; multi-State crew/pilots taxed by residence only (46 U.S.C. 11108)', 'US-MULTIS5-004')
F(u, 'sit.military_spouse.rule', 'Spouse service income not sourced to duty State; election of servicemember residence, spouse residence or duty station (50 U.S.C. 4001)', 'US-MULTIS5-005')
F(u, 'local.pa.philadelphia.resident.rate', 3.735, 'US-PAS5-022', uom=P, ef='2026-07-01', note='Nonresident 3.425% from 2026-07-01 (3.74/3.43 before). Mid-year change.')
F(u, 'local.pa.philadelphia.nonresident.rate', 3.425, 'US-PAS5-022', uom=P, ef='2026-07-01')
F(u, 'local.in.county.change_dates', 'County rates may change in January and October (DN#1 R47/10-26 from 2026-10-01)', 'US-INS5-009')

# ================= m07_deductions =================
u = 'm07_deductions'
F(u, 'garn.ccpa.ordinary.max.rate', 25, 'US-FEDS5-023', uom=P)
F(u, 'garn.ccpa.protected.weekly', 217.50, 'US-FEDS5-023', cur=USD, note='30 x 7.25. States may be stricter (e.g. AZ 10%, WA 35x/75%, CO 80% or 40x - annexes).')
F(u, 'garn.support.max.supporting', 50, 'US-FEDS5-023', uom=P, note='55% with arrears >12 weeks.')
F(u, 'garn.support.max.not_supporting', 60, 'US-FEDS5-023', uom=P, note='65% with arrears >12 weeks.')
F(u, 'garn.irs_levy.single0.weekly', 309.62, 'US-FEDS5-014', cur=USD)
F(u, 'garn.irs_levy.per_dependent.weekly', 101.92, 'US-FEDS5-014', cur=USD)
F(u, 'garn.iwo.interstate_law', "Law of the obligor's principal place of employment governs fee, maximum, timing, priority; remit to SDU within 7 business days", 'US-MULTIS5-007')
F(u, 'garn.iwo.form.omb_expiry', '2029-08-31', 'US-FEDS5-028', note='OMB 0970-0154 approved without change 2026-08-25; current form extended one year while states reprogram (gig fields).')
F(u, 'ret.401k.deferral.limit', 24500, 'US-FED-023', cur=USD)
F(u, 'ret.401k.catchup.limit', 8000, 'US-FED-023', cur=USD)
F(u, 'ret.401k.catchup_60_63.limit', 11250, 'US-FED-023', cur=USD)
F(u, 'hsa.limit.self', 4400, 'US-FED-024', cur=USD)
F(u, 'hsa.limit.family', 8750, 'US-FED-024', cur=USD)
F(u, 'fsa.health.limit', 3400, 'US-FEDS5-010', cur=USD)
F(u, 'fsa.health.carryover', 680, 'US-FEDS5-010', cur=USD)

# ================= m08_leave =================
u = 'm08_leave'
F(u, 'leave.fmla.weeks', 12, 'US-FEDS5-026', uom='weeks', note='26 for military caregiver; may be unpaid; employer may require substitution of accrued paid leave.')
F(u, 'leave.fmla.military_caregiver.weeks', 26, 'US-FEDS5-026', uom='weeks')
F(u, 'leave.federal.paid_leave_private', False, 'US-FEDS5-026', note='No federal paid sick or annual leave for private employers; state law/state PFML.')
F(u, 'pfml.ma.max_weekly_benefit', 1230.39, 'US-MAS5-025', cur=USD, et='2026-12-31')
F(u, 'pfml.ma.max_weekly_benefit', 1284.61, 'US-MAS5-025', cur=USD, ef='2027-01-01')
F(u, 'pfml.benefits.w2_treatment', 'State PFML: employee contribution and employer voluntary payment are W-2 wages', 'US-FEDS5-007')
U(u, 'leave.eo13706.accrual', 'EO 13706 federal-contractor paid sick leave accrual figures were not transcribed (FED OQ 6).', '29 CFR 13.5 read from eCFR (one fetch).')

# ================= m09_termination =================
u = 'm09_termination'
F(u, 'term.final_pay.federal_rule', 'No federal rule: final-pay timing and vacation payout are state law; FLSA wages due by the regular payday', 'US-FEDS5-025')
F(u, 'term.warn.notice_days', 60, 'US-FEDS5-025', uom='days')
F(u, 'term.severance.wage_status', 'Severance pay = wages for FIT, FICA and FUTA', 'US-FEDS5-029')
F(u, 'term.w2.early_furnishing', 'Terminated employee: W-2 no later than January 31 of following year (earlier on request)', 'US-FED-016')
F(u, 'term.final_pay.sd', 'Next regular payday (or when property returned)', 'US-SDS5-010', note='Example; per-state final-pay rules in annexes.')

# ================= m10_reporting =================
u = 'm10_reporting'
F(u, 'dep.lookback.monthly_threshold', 50000, 'US-FEDS5-004', cur=USD, note='Lookback 2024-07-01..2025-06-30; <=50,000 monthly (15th of next month); >50,000 semiweekly.')
F(u, 'dep.next_day.threshold', 100000, 'US-FEDS5-004', cur=USD, check=True)
F(u, 'rpt.941.frequency', 'quarterly; due last day of month after quarter', 'US-FED-015', check=False)
F(u, 'rpt.940.frequency', 'annual; due January 31 (10 more days if all FUTA deposited on time); FUTA deposits when liability > 500', 'US-FEDS5-031')
F(u, 'rpt.w2.due_date', '2027-02-01', 'US-FEDS5-007', note='TY2026 W-2 Copy A to SSA and employee copies.')
F(u, 'rpt.w2.no_withholding_threshold', 2000, 'US-FEDS5-007', cur=USD)
F(u, 'rpt.w2.box12.new_codes', 'TP (cash tips), TT (qualified overtime), TA (Trump-account employer contribution); Box 14b Treasury Tipped Occupation Code', 'US-FEDS5-007')
F(u, 'rpt.w2.state_boxes', 'Boxes 15-20 hold up to TWO States and TWO localities; more -> second W-2 repeating boxes a-f', 'US-MULTIS5-011')
F(u, 'rpt.aca.ale_threshold', 50, 'US-FEDS5-012', uom='employees', note='Full-time incl. FTEs in prior year; e-file at 10+ returns. TY2025 instructions (partial row).')
F(u, 'rpt.aca.efile_threshold', 10, 'US-FEDS5-012', uom='returns')
F(u, 'rpt.1042s.channel', 'IRIS (FIRE retired for TY2026); due 2027-03-15', 'US-FEDS5-016')
F(u, 'rpt.davis_bacon.certified_payroll', 'Weekly certified payroll to the contracting agency; prime responsible for subcontractors (WH-347 optional)', 'US-FEDS5-027')
F(u, 'rpt.agent.authorization', 'Form 8655 authorises reporting agent to sign/file 940/941 and make deposits; employer remains liable', 'US-FED-008')
U(u, 'rpt.efw2.ty2026.layout', 'SSA EFW2 TY2026 (Pub. 42-007) not read: ssa.gov 403, Wayback 404, archive API 429 (US-FEDS5-032 gated).', 'SSA Pub. 42-007 TY2026 downloaded in the browser pass or from a non-blocked network.', ['https://www.ssa.gov/employer/efw/26efw2.pdf (403)', 'https://www.ssa.gov/employer/EFW2&EFW2C.htm (403)'])
U(u, 'rpt.i940.ty2026', 'TY2026 Instructions for Forms 940 and 1094-C/1095-C not yet issued; 2025 editions read.', 'IRS releases of the TY2026 instructions (usually Dec-Jan).')

# ================= m11_advanced =================
u = 'm11_advanced'
F(u, 'pop.statutory_employee.treatment', 'FICA yes, FIT withholding no (four categories)', 'US-FEDR3-005')
F(u, 'pop.minister.treatment', 'No FIT/FICA withholding even if common-law employee; SE tax; voluntary FIT agreement; parsonage excluded from box 1', 'US-FED-030')
F(u, 'pop.farmworker.cash_threshold', 150, 'US-FEDR3-006', cur=USD, note='Or total farmwork pay >= 2,500 in the year; Form 943.')
F(u, 'pop.farmworker.employer_threshold', 2500, 'US-FEDR3-006', cur=USD)
F(u, 'pop.citizen_abroad.form673', 'Employer may stop FIT withholding on Form 673 statement (FEIE/housing); citizens only', 'US-FEDR3-007')
F(u, 'pop.citizen_abroad.feie', 132900, 'US-FED-025', cur=USD)
F(u, 'bik.parking.monthly', 340, 'US-FEDS5-008', cur=USD)
F(u, 'bik.transit.monthly', 340, 'US-FEDS5-008', cur=USD)
F(u, 'bik.dependent_care.limit', 7500, 'US-FEDS5-008', cur=USD, note='3,750 MFS; raised from 5,000 by P.L. 119-21.')
F(u, 'bik.educational_assistance.limit', 5250, 'US-FEDS5-008', cur=USD)
F(u, 'bik.group_term_life.exclusion', 50000, 'US-FEDS5-008', cur=USD, note='Coverage above 50,000: FICA wages at Table 2-2 cost.', check=False)
F(u, 'bik.trump_account.employer.limit', 2500, 'US-FEDS5-030', cur=USD, ef='2026-07-04', note='Excluded under sec. 128 from 2026-07-04; W-2 Box 12 TA.')
F(u, 'aca.affordability.rate', 9.96, 'US-FEDS5-011', uom=P, et='2026-12-31')
U(u, 'bik.mileage.rate', 'The 2026 business standard mileage rate is not printed in Pub. 15-B (FED OQ 7).', 'IRS 2026 standard mileage notice.')

# ================= m12_worked_examples (oracle) =================
u = 'm12_worked_examples'
EX = [
 ('fed.nra_weekly', 31, 'US-FED-027', 'Pub. 15-T 2026: NRA weekly 300 + 226.90 table add-on = 526.90 -> wage-bracket result 31'),
 ('fed.tribal_monthly', 584.09, 'US-FED-027', 'Pub. 15-T 2026: tribal gaming monthly 6,000 -> 584.09'),
 ('ca.de44_f.monthly', 7.17, 'US-CAS5-001', 'DE 44 Method B ex. F: 57,000-11,412=45,588 -> 243.74+2.2%x23,430=759.20-673.20=86.00/yr = 7.17/month; ex. E 4.13 semimonthly'),
 ('ga.mfj_semimonthly', 27.03, 'US-GAS5-001', '(2,000-1,250-208.33) x 4.99% = 27.029 -> 27.03; tables and formula "differ slightly"'),
 ('il.weekly_800', 32.13, 'US-ILR3-001', 'IL-700-T 2026 example 800/week = 32.13'),
 ('in.weekly_800.state', 13.96, 'US-INS5-007', 'DN#1: 473.08 x 2.95% = 13.96'),
 ('in.weekly_800.county', 4.73, 'US-INS5-007', 'DN#1: 473.08 x 1% = 4.73'),
 ('wi.weekly_350_s1', 7.59, 'US-WIS5-011', 'W-166 ex.1; annual figures differ 1 cent from guide (bracket rounding), per-period equal'),
 ('wi.biweekly_1000_m3', 22.08, 'US-WIS5-011', 'W-166 ex.3 (ex.2 weekly 500 S3 = 14.34)'),
 ('de.weekly_25000', 13.88, 'US-DES5-006', 'Guide ex.1 single 1 allowance 25,000/yr: tax 832.00 -> 13.88 weekly'),
 ('de.supplemental', 269.63, 'US-DES5-006', 'Guide ex.2 reproduces 269.625 -> 269.63 (half-up to cent)'),
 ('hi.weekly_500_s3', 9.58, 'US-HIS5-004', 'Booklet A: 26,000-3,432-4,350=18,218; 288+3,818x5.5%=497.99/52=9.58'),
 ('la.weekly_700', 13.98, 'US-LAS5-001', '(700-12,875/52) x 3.09% = 13.9793 -> 13.98'),
 ('la.biweekly_4600', 111.54, 'US-LAS5-001', '(4,600-25,750/26) x 3.09% = 111.5371 -> 111.54'),
 ('ma.weekly_155_0ex', 7.16, 'US-MAS5-024', 'Circular M weekly bracket 150-160 re-derived: 7.16/2.93/1.96/1.00 for 0-3 exemptions'),
 ('me.example3.weekly', 257, 'US-MES5-011', 'Booklet examples 1-3 = 0 / 33 / 257 per week'),
 ('mo.annual_married', 707.81, 'US-MOS5-001', 'DOR example married 35,000: 263 + 9,464x4.7% = 707.81/yr = 59/month'),
 ('ms.weekly_460_0ex', 8.94, 'US-MSS5-003', '(460x52-2,300-10,000) x 4% /52 = 8.94 -> table 9'),
 ('ri.weekly_2195', 87.57, 'US-RIS5-019', '2,175.77 taxable -> 59.18+(2,175.77-1,578)x4.75% = 87.57'),
 ('vt.weekly_1800_m2', 45.77, 'US-VTS5-016', 'GB-1210-2026 p.6: (1,592.30-226)x3.35% = 45.77'),
 ('al.weekly_850_m2', 29.59, 'US-ALS5-001', 'M-2 weekly 850, FIT 35.19: 20+200+26,370x5%=1,538.50/52 = 29.59 (FIT computed first)'),
 ('ar.monthly_2127_2ex', 36.50, 'US-ARS5-001', '25,524-2,470=23,054 -> 23,050 x3.4%-287.97=495.73 -> 496-58=438/12 = 36.50'),
 ('nd.section2_booklet', 734, 'US-NDS5-001', 'BOOKLET DEFECT: Section 2 example prints 734/yr and 14/week; table gives 701.51 -> 13. Oracle uses the table, not the printed example'),
]
for k, v, rid, note in EX:
    F(u, f'oracle.{k}.withholding', v, rid, note=note, cur=USD)
DEX = [
 ('ct.ex8_f_weekly700', 17.65, 'US-CTS5-010', 'IP 2026(1) ex.8 (tables); TPG-211 rules give 17.79 - tables vs rules differ up to 0.48 (CT-OQ-1)'),
 ('ct.ex9_a_weekly1000', 39.97, 'US-CTS5-010', 'IP 2026(1) ex.9 (tables); rules give 39.86'),
 ('ct.ex10_b_biweekly2300', 78.82, 'US-CTS5-010', 'IP 2026(1) ex.10 (tables); rules give 79.30'),
 ('mi.detroit.resident_biweekly_2000', 47.45, 'US-MIR3-002', 'Detroit resident 2.4%: (2,000-23.08) x 0.024 = 47.45 (600/26 = 23.08 per Form 5469)'),
 ('mn.biweekly_2000_s1', 91.27, 'US-MNS5-010', '52,000-5,300=46,700; 1,782.09+(46,700-38,010)x6.80% = 2,373.01/26 = 91.27 (91 if rounded)'),
 ('oh.biweekly_2000_1ex', 45.13, 'US-OHS5-001', 'Tables eff. 2026-08-01: TW 51,350 -> (25,300x0.0299+416.80)/26 = 45.13; table route equal'),
 ('ny.nys50t.example2', 258.50, 'US-NYS5-001', 'PLACEHOLDER'),
 ('nc.weekly_450_s2', 4.44, 'US-NC-001', 'NC-30: (450-245.19-96.16) x 4.09% = 4.44'),
 ('nd.section1_weekly_1800_s2', 10, 'US-NDS5-001', '(1,606-1,108) x 1.95% = 9.71 -> 10 as printed'),
 ('nm.weekly_1000_married', 41.80, 'US-NM-P5-2-001', 'PLACEHOLDER'),
 ('ok.semimonthly_1825_m2', 37.00, 'US-OK-001', '1,825-83.34=1,741.66; 9.10+(1,741.66-1,129)x4.5% = 36.67 -> 37.00 (OW-2 p.7)'),
 ('or.annual_25000', 1789, 'US-ORS5-009', 'Ex.1 lines compute BASE 21,090 -> 941+9,690x8.75% = 1,789/yr; DOR prints 21,165/1,798 (publication defect)'),
 ('ut.monthly_married_7800', 347, 'US-UTS5-013', 'PLACEHOLDER'),
 ('ia.example6_monthly_5000_hoh', 114.92, 'US-IAS5-005', 'Example 6 printed without its final figure; worker derivation 114.92'),
 ('ky.biweekly_1500', 47.98, 'US-KY-002', 'PLACEHOLDER'),
 ('id.biweekly_1212_single', 31, 'US-IDS5-008', '5.3% x (1,212-619) = 31.43 -> 31 (07-23-2026 table)'),
 ('sc.weekly_750_3al', 10.58, 'US-SCS5-004', 'WH-1603F example: 750x52=39,000-15,000-3,900=20,100; x6%-656.10=549.90/52=10.58 (2026 tables 0/3/6%, not Act 110). The row quoting the example, US-SC-P5-1-002, fails the register_id pattern'),
 ('ks.weekly_threshold_single', 69, 'US-KSS5-001', '3,605/52 = 69.33 -> 69 (KW-100 per-period threshold)'),
]
for k, v, rid, note in DEX:
    if note == 'PLACEHOLDER':
        continue
    F(u, f'oracle.{k}.withholding', v, rid, vm=D, note='Worker re-derivation (Stage 5, Python) on the method row: ' + note, cur=USD,
      conf='medium' if k.startswith(('ct.', 'ia.', 'or.')) else 'high')
U(u, 'oracle.ny.nys50t.example2.withholding', 'NYS-50-T-NYS Method II examples 1, 3, 4 reproduce (8.01, 3,576.63, 44.10); example 2 prints 12.43/258.51 while half-up arithmetic gives 12.42/258.50. The only NY row carrying the booklets (US-NY-P5-2-001) has an id that fails the facts register_id pattern.', 'DTF statement of the rounding convention or the DTF calculator result for the same case; plus a schema-valid register id for the NYS-50-T row.', blocking=False)
U(u, 'oracle.nm.weekly_1000_married.withholding', 'FYI-104 example (weekly married 1,000: 12.77+210x4.3% = 21.80 + 20.00 extra = 41.80) reproduces, but the FYI-104 row id US-NM-P5-2-001 fails the facts register_id pattern.', 'Schema-valid alias row for FYI-104 in the merge, or pattern widening by the contract owner.', blocking=False)
U(u, 'oracle.ky.biweekly_1500.withholding', 'KY 2026 formula sheet: 1,247.40/26 = 47.98 but sheet shows 47 (no stated rule) and prints 35,730 for 35,640; the row US-KY-002 fails the facts register_id pattern.', 'DOR KY confirmation of the per-period rounding, and a schema-valid id for the 42A003 row.', blocking=False)
U(u, 'oracle.ut.pub14.examples.withholding', 'Pub 14 (04/26) six examples reproduce (weekly S 400 -> 12; biweekly S 2,600 -> 116; semimonthly M 1,200 -> 18; monthly M 7,800 -> 347; quarterly S 9,000 -> 367; daily M 175 -> 5) but no schema-valid register row carries Pub 14 (US-UT-PIT-003 pattern fails); Pub 14 effective date (2026-06-01?) open (UT-OQ-1).', 'Schema-valid register row for Pub 14 Rev. 04/26 with its effective date.', blocking=False)
U(u, 'oracle.mi.biweekly_2000_1ex.withholding', 'MI seed (2,000-226.92) x 4.25% = 75.36 reproduces from Guide 446 (Rev. 02-26), but the only row carrying the 4.25% rate and 5,900 exemption (US-MI-PIT-001) fails the facts register_id pattern; the Treasury withholding calculator is the official oracle and was not run.', 'Schema-valid alias row for Guide 446 Rev. 02-26, plus one Treasury calculator run for the same case.', blocking=False)
U(u, 'oracle.dc.2026', 'DC has no published 2026 withholding method: D.C. Act 26-416 (emergency, effective 2026-08-13, max 90 days) revoked personal exemptions; D-4 under review (US-DCS5-021).', 'OTR 2026 withholding instructions/tables (otr.cfo.dc.gov, 403 to curl) or the permanent FY2027 BSA act.', blocking=False)
U(u, 'oracle.md.calculator', 'MD oracle is the Comptroller withholding calculator and Central Payroll net pay calculator; neither was run.', 'One run of the Comptroller calculator for a fixed case in the browser pass.', blocking=False)

# ================= m13_practices (traps) =================
u = 'm13_practices'
F(u, 'practice.sc.withholding_rates_2026', 'Use WH-1603 tables 0/3/6% for 2026 withholding; Act 110 rates (1.99%/5.21%) apply at the 2026 annual return only', 'US-SCS5-004', note='Act 110 row: US-SCS5-005. Level: assessment.')
F(u, 'practice.wi.use_w166_tables', 'Withholding uses W-166 schedule (3.54/4.65/5.30/7.65%), not the assessment brackets (3.50/4.40/5.30/7.65%)', 'US-WIS5-010', note='Statutory brackets in US-WIS5-010; W-166 in US-WIS5-011.')
F(u, 'practice.ne.use_circular_en_tables', 'Withholding uses DOR Circular EN tables (2026 2.26-4.60%), not the statutory 4.55% rate', 'US-NES5-018')
F(u, 'practice.ks.kw100_header_stale', 'KW-100 header prints "wages paid on and after January 1, 2021" but figures are the 2024 values in force for 2026 (5.20/5.58%)', 'US-KSS5-001')
F(u, 'practice.mi.tips_ot_deduction_level', 'MI 2025 PA 24 tips/overtime deduction (TY2026-2028) is ASSESSMENT only; no change to withholding', 'US-MIS5-017')
F(u, 'practice.va.std_deduction_2027_not_modelled', 'Statute: 2027 standard deduction 9,200/18,400; do not model 2027 withholding until Virginia Tax publishes the 2027 formula (guide Rev. 10/26 says the deduction sunsets - wrong)', 'US-VAS5-018')
F(u, 'practice.dc.2026_method_unpublished', 'D.C. Act 26-416 (emergency, from 2026-08-13) revoked personal exemptions; no 2026 withholding method published (D-4 under review)', 'US-DCS5-021', conf='medium')
F(u, 'practice.ct.tables_vs_rules', 'DRS permits tables or TPG-211 rules; results differ up to 0.48/period; engine must choose one method (CT-OQ-1)', 'US-CTS5-010')
F(u, 'practice.oh.flat_rate_vs_tables', 'TY2026 statute flat 2.75% but withholding tables graduated to 3.4% (5747.06 rule vs 5747.02 rate) - use the tables', 'US-OHS5-007')
F(u, 'practice.or.federal_cap', 'Use 8,750 federal-tax subtraction cap (pp.6-7 formula); DOR publication also prints 8,500 and its example 1 is mis-computed', 'US-ORS5-009')
F(u, 'practice.hi.2027_tables_pending', 'Act 24 SLH 2026 changes TY2027 brackets (new 13% top); 2027 withholding indeterminate until DOTAX issues 2027 Booklet A', 'US-HIS5-029')
F(u, 'practice.ga.rate_change_2026', '4.99% for TY2026 (5.19% before); 2027 0.125-point step conditional on OPB report of 2026-12-01', 'US-GAS5-009')
F(u, 'practice.ma.pfml_split', 'Follow DFML: 2026 split unchanged, swap from 2027-01-01 (Ch. 101/2026 s.45 conflict recorded)', 'US-MAS5-012', conf='medium', note='Decision rows: US-MAS5-026 (Ch. 101 s.25-26, s.45) and US-MAS5-012 (DFML). See m05 pfml.ma.split.2026.')
F(u, 'practice.al.fit_before_sit', 'AL state base deducts federal withholding: order FIT before AL SIT', 'US-ALS5-001')
F(u, 'practice.fed.estimator_not_oracle', 'IRS Tax Withholding Estimator is not an employer engine or oracle', 'US-FED-021')
F(u, 'practice.fed.pl119_21_withholding', 'Do not reduce FIT withholding for tips/overtime deductions except through W-4 Step 4(b)', 'US-FEDS5-030')
U(u, 'pfml.ma.split.effective_date', 'Ch. 101/2026 s.45 says ss.25-26 apply for taxable years beginning on or after 2026-01-01; DFML implements the swap from 2027-01-01. Decision taken: follow DFML (rows US-MAS5-026, US-MAS5-012).', 'A DFML/DOR notice or 458 CMR 2.00 amendment on the transition (MA Q14).', blocking=False)
U(u, 'practice.dol_paid_leave_list', 'DOL WB featured-paid-leave page (19 P9 rows reverted to B/MANUAL) returns 404; the DOL prevailing-wage list still says MI has no law (MI restored 2023).', 'Saved copy of the DOL WB paid-leave page; never use the DOL lists for MI.', blocking=False)
U(u, 'contract.register_id_pattern', '407 of 2,177 active/partial register ids (style US-XX-YYY-NNN, e.g. US-NY-P5-2-001, US-CA-EDD-004, US-FED-P5-2-005) fail facts.schema register_id ^[A-Z]{2}-[A-Z0-9]{2,12}-[0-9]{3,4}$, so facts resting only on them could not be emitted.', 'Contract owner widens the pattern (MINOR/PATCH bump) or the merge adds schema-valid alias rows.', blocking=False)

# ================= FED/MULTI open questions carried at module level =================
U('m05_social_security', 'futa.credit_reduction.2026', 'Potential 2026 credit reductions CA 5.3% (1.5 + BCR 3.8) and USVI 4.8% become final only if advances remain unpaid on 2026-11-10 (US-FEDS5-009 partial).', 'DOL OUI FUTA credit-reduction page/xlsx after 2026-11-10, or the 2026 Schedule A (Form 940) instructions.', ['https://oui.doleta.gov/unemploy/futa_credit.asp'], blocking=False)
U('m05_social_security', 'sui.wage_credit_other_state', 'SUI wage-base credit for wages reported to another State: annex_MULTI now carries multi.sui.other_state_wage_credit.* for 28 States plus CA; the remaining States (incl. AZ, CO, GA, IL, IN, LA, MA, MD, MN, MO, NJ, NM, NY, OH, PA, TN, TX, UT, VA, WA, WI, DC) are not yet keyed at MULTI level.', 'Each remaining State taxable-wage definition (annex rows) or DOL Significant Provisions July 2026.', blocking=False)
U('m05_social_security', 'pfml.multistate.coverage', 'PFML/SDI coverage of multistate workers: annex_MULTI keys CT, DC, DE, MD, ME, OR, RI, WA and a default (localization); CA, NJ, NY, MA, CO, MN, VT not keyed at MULTI level (MULTI-OQ-3).', 'Each programme coverage definition (annex units).', blocking=False)
U('m05_social_security', 'sdi.ca.rate', 'CA SDI 1.3% (2026, no wage cap) rests on US-CA-EDD-004, whose id fails the facts register_id pattern; 2027 rate not published (CA OQ 3).', 'Schema-valid id for the DE 44/EDD row; EDD 2027 rate notice.', blocking=False)
U('m06_tax', 'fed.indexation.2027', 'TY2027 Rev. Proc., 401(k)/IRA notice and 2027 Pub. 15-T not published as of 2026-11-02 (IR-2026-117..129 checked).', 'IRS releases expected Nov-Dec 2026.', blocking=False)
U('m08_leave', 'leave.sick.multistate_threshold', 'Paid-sick-leave coverage of employees working partly in a State is per State and not researched at MULTI level (MULTI-OQ-4).', 'Per-state statutes in the annexes.', blocking=False)
U('m10_reporting', 'newhire.multistate.registration_channel', 'HHS/OCSS multistate employer registration page returned 202 empty (MULTI-OQ-6); statute 42 U.S.C. 653a(b)(1)(B) carries the rule.', 'Browser read of the ACF multistate registration page.', ['https://www.acf.hhs.gov/css/form/multistate-employer-registration-form (202 empty)'], blocking=False)
U('m10_reporting', 'garn.iwo.revised_form.state_golive', 'States go live with the revised (gig-field) IWO/e-IWO within the one-year extension; dates not known (FED OQ 8).', 'OCSE Action Transmittal implementing ICR 202607-0970-002.', blocking=False)

# ================= COVERAGE MATRIX (18 rows) =================
def src(rid, art=None, covers=None):
    r = rows[rid]; s = {'register_id': rid, 'url': r['url']}
    if art: s['article'] = art
    if covers: s['covers'] = covers
    return s
IT, SS, RP = 'income_tax', 'social_security', 'reporting'
def A(treat, it, ss, rp, loc, sources, keys=None):
    d = {'status': 'answered', 'treatment': treat, 'effects': {'income_tax': it, 'social_security': ss, 'reporting': rp},
         'ccg_location': loc, 'sources': sources}
    if keys: d['fact_keys'] = keys
    return d
CM = {}
CM['resident_employee'] = A('Ordinary employee: FIT per W-4 and Pub. 15-T percentage/wage-bracket method; FICA employee+employer; FUTA and SUI employer-paid (SUI to the localization State); state income tax of the work State and, for residents working elsewhere, the residence State per its own rule (credit, difference withholding or reciprocity).',
  'FIT Pub. 15-T 2026 Worksheet 1A; state withholding per annex', 'OASDI 6.2%+6.2% to 184,500; Medicare 1.45%+1.45%; Additional Medicare 0.9% over 200,000; FUTA 0.6% net on 7,000; SUI per sui_state', 'Form 941 quarterly, 940 annual, W-2 by 2027-02-01; state withholding and UI returns',
  'm03_gross_to_net; m05_social_security; m06_tax', [src('US-FEDS5-001', 'Worksheet 1A', [IT]), src('US-FEDS5-005', '941 lines 5a-5d', [SS]), src('US-FEDS5-007', 'W-2 2026', [RP]), src('US-MULTIS5-017', 'localization test', [SS])],
  ['fit.worksheet1a.line1g.mfj', 'fica.oasdi.wage_base', 'futa.rate.net', 'routing.sui_state.test'])
CM['non_resident_employee'] = A('Two meanings in the US build. (a) Nonresident alien of the US: graduated withholding with the Pub. 15-T NRA add-on (16,100/yr Table 2), W-4 per Notice 1392 (Single, NRA, no exempt), treaty-exempt wages via Form 8233 to Form 1042-S, commercial-traveler exception (<=90 days, <=3,000). (b) Nonresident of a State: work-State withholding subject to reciprocity certificates, day/dollar thresholds (AL/LA/WV 30 days, AZ 60, IL 30 working days), convenience rules (NY, PA, DE, NE; NJ/CT retaliatory) and federal transport/military-spouse limits.',
  'NRA add-on for withholding only; 1042-S for treaty wages; state nonresident sourcing per m06 tables', 'NRA add-on has no FICA/FUTA effect: FICA computed on actual wages as for residents; for state nonresidents SUI follows the localization test, not residence', 'W-2 (or 1042-S for treaty-exempt wages, via IRIS); state nonresident withholding on the work-State return; W-2 boxes 15-20 up to two States',
  'm06_tax (NRA, reciprocity, thresholds); m11_advanced', [src('US-FEDS5-002', 'NRA adjustment tables 1-2', [IT, SS]), src('US-FEDS5-016', 'Pub. 515 pay for personal services', [IT, RP]), src('US-MULTIS5-017', 'localization test', [SS]), src('US-MULTI-021', 'AL 30-day', [IT]), src('US-MULTIS5-013', 'NY convenience', [IT])],
  ['fit.nra.addon.table2.annual', 'fit.nra.commercial_traveler.max_days', 'sit.nonres_threshold.la.days', 'sit.convenience.ny'])
CM['fixed_term_contract'] = A('No federal or general state statutory fixed-term regime: employment is at will (SD, TN rows as examples) and a contract for a fixed period is a matter of contract. Payroll treats a fixed-term worker exactly as any employee; expiry of the term is a separation and triggers the work State final-pay rule.',
  'none: same withholding as any employee', 'none: FICA/FUTA/SUI unchanged; UI benefit eligibility on separation is state law', 'Separation: state final pay and any state separation notice (e.g. TN LB-0489 within 24h - annex); W-2 as usual',
  'm09_termination', [src('US-SDS5-010', 'at-will; final wages', [RP]), src('US-TNS5-012', 'employment at will', [IT]), src('US-FEDS5-025', 'federal final pay', [SS])], ['term.final_pay.federal_rule'])
CM['part_time'] = A('No federal part-time payroll regime: the FLSA minimum wage and 40-hour overtime apply per hour/workweek regardless of schedule; part-time hours count toward ACA full-time-equivalent employees (ALE test 50). State paid-sick-leave accrual is per hour worked (annexes).',
  'none: same withholding method; wage-bracket/percentage method by pay period', 'none: FICA from first dollar; SUI/PFML per State (some States have hours-based coverage)', 'ACA: FTE count for ALE status (1094-C/1095-C); state UI reports with hours where required (e.g. WA hours + SOC)',
  'm04_compensation; m10_reporting', [src('US-FEDS5-017', 'FLSA 206', [SS]), src('US-FEDS5-018', 'FLSA 207', [IT]), src('US-FEDS5-012', 'ALE 50 incl. FTE', [RP])], ['minwage.federal.hourly', 'rpt.aca.ale_threshold'])
CM['officers_without_employment_contract'] = A('Corporate officers are employees for payroll: wages subject to FIT withholding, FICA and FUTA; state law includes corporate officers as employees for withholding (OK 68 O.S. 2385.1) and UI coverage (FL 443.1216(1)(a)). Directors fees and partner/sole-proprietor draws are not wages (self-employment, outside payroll). Statutory employees (four IRS categories) are FICA-only.',
  'Officer wages: FIT withholding as any employee (state law includes officers, e.g. OK)', 'FICA and FUTA on officer wages; SUI covers corporate officers (e.g. FL); some States allow officer exclusions (annexes)', 'W-2 as any employee; statutory employees W-2 box 13',
  'm11_advanced', [src('US-OKS5-010', '2385.1 employee incl. corporate officers', [IT]), src('US-FLS5-005', '443.1216(1)(a)', [SS]), src('US-FEDR3-005', 'statutory employees', [RP, SS])], ['pop.statutory_employee.treatment'])
CM['apprentices_and_trainees'] = A('No federal apprentice payroll regime: FLSA minimum wage applies (sub-minimum only under DOL certificates). Students: private-school/college students employed by their school are FICA and FUTA exempt; public school FICA exempt unless sec. 218; work-experience full-time students FICA taxable. States set learner rates (CA 85% for first 160 h; WA 14-15 year olds 85%).',
  'FIT withheld as any employee', 'Student exemptions from FICA/FUTA as listed; state UI student exclusions (annexes)', 'W-2 as usual',
  'm04_compensation; m11_advanced', [src('US-FEDS5-029', 'sec. 15 special classes (students)', [SS, IT]), src('US-CAS5-006', 'learners 85%', [RP]), src('US-WAS5-006', 'youth 85%', [RP])], ['minwage.state.ca.hourly'])
CM['maternity_paternity_parental'] = A('No federal paid parental leave for private employers: FMLA gives up to 12 workweeks job-protected leave in 12 months (may be unpaid; employer may require substitution of accrued paid leave). Paid leave comes from state PFML/TDI programmes (e.g. WA PFML 1.13%, MA PFML 0.88%, DC PFL 0.75% employer-only; CA SDI/PFL in the CA annex) - premiums withheld/paid by payroll, benefits paid by the State.',
  'State PFML benefits paid by the State are not employer payroll; employee PFML contributions are W-2 wages (Rev. Rul. 2025-4)', 'Employee/employer PFML contributions per State programme, capped as the State sets (e.g. MA cap = SS wage base)', 'State PFML quarterly returns (e.g. MassTaxConnect); W-2 box 14 per State practice',
  'm08_leave; m05_social_security', [src('US-FEDS5-026', '29 U.S.C. 2612', [IT]), src('US-FEDS5-007', 'PFML W-2 treatment', [IT, RP]), src('US-WAS5-015', 'WA PFML rate', [SS]), src('US-MAS5-012', 'MA PFML rates', [SS])], ['leave.fmla.weeks', 'pfml.wa.total.rate', 'pfml.ma.total.rate'])
CM['work_accident_occupational_disease'] = A("Workers' compensation is state law and generally an insured employer cost outside payroll; payroll touches it where a State levies a per-employee fee or allows an employee deduction (NM Workers' Compensation fee on TRD-41431: employer 2.55 + employee fee per quarter; WA employee share of workers' comp premiums - WA annex). No federal payroll rule.",
  'none at payroll: workers compensation benefits are not employer wages', 'NM fee per covered employee per quarter (employer and employee parts); WA employee deduction; no federal levy', 'NM TRD-41431 quarterly (fee + wage report); state annexes',
  'm05_social_security; m07_deductions', [src('US-NMR3-001', '52-5-19 NMSA', [SS, RP]), src('US-FEDS5-029', 'Pub. 15 sec. 15 (no federal WC rule listed)', [IT])])
CM['termination_and_final_pay'] = A('Federal law does not require immediate final pay; final-pay timing and vacation payout are state law (annexes: e.g. SD next payday, NH 72 h, UT 24 h on discharge; ME/MT/WY payout of accrued vacation). Severance is wages for FIT, FICA and FUTA. WARN: 60 days notice for plant closing/mass layoff - pay in lieu is wages. W-2 for a terminated employee by Jan 31 (earlier on request).',
  'Severance and pay in lieu are supplemental wages (22% optional / aggregate)', 'Severance subject to FICA and FUTA', 'W-2 by Jan 31; state separation notices where required',
  'm09_termination', [src('US-FEDS5-025', 'DOL last paycheck; WARN 2102', [RP]), src('US-FEDS5-029', 'severance = wages', [IT, SS]), src('US-FED-016', '31.6051-1(a)(1)', [RP])], ['term.warn.notice_days', 'term.severance.wage_status'])
CM['mid_month_joiner_and_leaver'] = A('No proration rule in federal law: withholding is computed on the wages paid in the pay period with the period frequency of Pub. 15-T (annualise x periods); a joiner files W-4 (and state certificate) at hire and is reported to the State Directory of New Hires within 20 days (shorter in many States); a leaver gets final pay under state law. Wage bases (OASDI, FUTA, SUI) run per employer per calendar year from the first payment.',
  'Pub. 15-T per-period method on wages actually paid; no catch-up or proration', 'Wage bases start at the first payment by this employer in the calendar year; successor employer carry-over for FUTA', 'New-hire report within 20 days; W-2 for any part-year employee',
  'm02_master_data; m03_gross_to_net', [src('US-FEDS5-001', 'pay-period tables', [IT]), src('US-FEDS5-024', '653a(b)', [RP]), src('US-MULTIS5-009', '3306(b)(1)', [SS])], ['newhire.deadline.days', 'futa.wage_base'])
CM['annual_regularisation'] = A('There is no employer year-end income-tax regularisation: the employee settles at assessment (Form 1040 / state returns). The employer reconciles quarterly 941 to annual W-2/W-3, corrects with 941-X / W-2c, and stops OASDI at the wage base and starts Additional Medicare above 200,000 per employer. Excess OASDI from multiple employers is refunded at assessment, not by the employer.',
  'none at payroll: assessment by the employee; W-4 exempt status renewed yearly', 'Per-employer annual bases (OASDI 184,500; FUTA 7,000; SUI per State)', 'W-2/W-3 by 2027-02-01 reconciled to four 941s; 940 annual; state annual reconciliations',
  'm10_reporting; m05_social_security', [src('US-FEDS5-007', 'W-2/W-3 2026', [RP]), src('US-FEDS5-005', 'Additional Medicare', [SS]), src('US-FEDS5-006', 'W-4 exempt expiry', [IT])], ['rpt.w2.due_date', 'fica.addl_medicare.threshold', 'w4.exempt.expiry'])
CM['overtime'] = A('FLSA: 1.5x the regular rate over 40 hours in a workweek, no federal daily overtime. States add daily overtime (CA 8h/12h and 7th day; AK over 8h; NV for under 18.00/h from 2026-07-01; CO, KY 7th day - annexes). P.L. 119-21 qualified-overtime deduction (premium half) operates at assessment; employer reports W-2 Box 12 TT; FICA unchanged.',
  'Overtime is regular wages for withholding; deduction only via W-4 Step 4(b)', 'Fully subject to FICA/FUTA/SUI', 'W-2 Box 12 TT (qualified overtime) from TY2026',
  'm04_compensation; m10_reporting', [src('US-FEDS5-018', '29 U.S.C. 207(a)(1)', [SS]), src('US-FEDS5-030', 'P.L. 119-21', [IT, RP]), src('US-CAS5-008', 'Lab. Code 510', [RP])], ['ot.federal.multiplier', 'ot.state.ca.rule', 'rpt.w2.box12.new_codes'])
CM['multiple_employers'] = A('Each employer withholds and applies wage bases independently: OASDI and FUTA bases are per employer (successor carry-over only on acquisition); Additional Medicare is triggered per employer at 200,000 regardless of total income. The employee coordinates FIT across jobs on W-4 Step 2 (multiple jobs) - Worksheet 1A line 1g is not subtracted when Step 2 is checked.',
  'W-4 Step 2 checkbox changes the schedule (Step-2-checked thresholds) and line 1g', 'Per-employer OASDI/FUTA/SUI bases; excess OASDI refunded at assessment; common-paymaster rules not researched', 'Separate W-2 per employer',
  'm03_gross_to_net; m05_social_security', [src('US-FEDS5-006', 'Step 2', [IT]), src('US-MULTIS5-009', 'FUTA per employer', [SS]), src('US-FEDS5-005', 'Additional Medicare per employer', [SS, RP])], ['fit.worksheet1a.line1g.mfj', 'futa.wage_base'])
CM['local_regimes'] = A('Local income/payroll taxes exist in a minority of States and are outside state reciprocity: PA EIT (higher of resident or work-municipality rate) and LST; Philadelphia wage tax 3.735%/3.425% from 2026-07-01; OH municipal and school-district taxes (base = Medicare wages less 125); MI city taxes (Detroit 2.4%/1.2%); IN county tax (changes January/October); MD county tax (to 3.30%); KY occupational taxes (Louisville 1.45% incl. TARC); NYC/Yonkers; OR transit levies. Per-locality detail in the annexes.',
  'Local withholding by residence and/or work locality per local rule; W-2 boxes 18-20', 'Local transit/payroll levies (OR state transit 0.1% employee; NY MCTMT employer) per US-OWN-007 scope', 'Local returns per locality; W-2 boxes 18-20 up to two localities',
  'm06_tax (local); annexes PA, OH, MI, IN, MD, KY, NY, OR', [src('US-PAS5-022', 'Philadelphia wage tax', [IT, RP]), src('US-MIR3-002', 'Detroit 5469', [IT]), src('US-INS5-009', 'county rate changes', [IT]), src('US-MULTIS5-011', 'W-2 boxes 15-20', [RP])], ['local.pa.philadelphia.resident.rate', 'local.in.county.change_dates', 'rpt.w2.state_boxes'])
CM['employer_type_and_size'] = A('Size and type thresholds change obligations: ACA ALE at 50 full-time incl. FTEs (1094-C/1095-C, e-file at 10+); deposit schedule by lookback liability (50,000 monthly/semiweekly; 100,000 next-day); household employers (FICA at 3,000, FUTA at 1,000/quarter, Schedule H); agricultural (150/2,500 tests, Form 943); government employers (no FUTA, sec. 218); state size tests (AR minimum wage 4+ employees; MA PFML employer share 25+; NE sick leave 11+; VA paid sick 50+ from 2027-07-01 - annexes).',
  'Household FIT only by agreement; agricultural FIT/FICA from 150/2,500', 'Household and agricultural thresholds; MA PFML <25 no employer share', 'ALE 1094-C/1095-C; Form 943/944/Schedule H routes',
  'm10_reporting; m11_advanced', [src('US-FEDS5-012', 'ALE', [RP]), src('US-FEDS5-004', 'deposit schedule', [RP]), src('US-FEDS5-029', 'household/government', [IT, SS]), src('US-MAS5-012', 'MA PFML <25', [SS])], ['rpt.aca.ale_threshold', 'dep.lookback.monthly_threshold', 'household.fica.threshold'])
CM['mid_year_rate_change'] = A('Several 2026 values change mid-year and must be dated per payment date: DC minimum wage 18.40 from 2026-07-01; OR 15.55 from 2026-07-01; AK 14.00 from 2026-07-01; FL 15.00 from 2026-09-30; NV daily-OT rule from 2026-07-01; Philadelphia wage tax from 2026-07-01; OH withholding tables from 2026-08-01; GA 4.99% tables; IN county rates from 2026-10-01; ID tables 2026-07-23; Trump-account exclusion from 2026-07-04.',
  'Withholding tables effective by payment date (OH 2026-08-01, IN county 2026-10-01, ID 2026-07-23)', 'Rate changes on the effective date (none federal mid-year in 2026)', 'Quarterly returns split by period; W-2 annual totals',
  'm04_compensation; m06_tax; m13_practices', [src('US-DCS5-011', '32-1003', [RP]), src('US-ORS5-002', 'BOLI 2026-07-01', [RP]), src('US-OHS5-001', 'tables 2026-08-01', [IT]), src('US-PAS5-022', 'Philadelphia 2026-07-01', [IT]), src('US-FEDS5-030', 'Trump account 2026-07-04', [IT, SS])],
  ['minwage.state.dc.hourly', 'minwage.state.or.standard.hourly', 'sit.oh.withholding_tables.effective_from', 'local.pa.philadelphia.resident.rate'])
CM['special_pay_cycles'] = A('Pub. 15-T supports daily/weekly/biweekly/semimonthly/monthly/quarterly/semiannual/annual periods (annualise then divide). Supplemental pay (bonus, commissions, severance): flat 22% optional or aggregate; 37% mandatory above 1,000,000 per year. State pay-frequency and payday-timing rules (CA Lab. Code 204 semimonthly windows) and state supplemental rates (CA 10.23% bonus / 6.6% other) are annex detail.',
  'Supplemental methods per Pub. 15 sec. 7; state supplemental rates', 'none: FICA on all wages including supplemental', 'none specific',
  'm03_gross_to_net; m06_tax', [src('US-FEDS5-003', 'sec. 7 supplemental', [IT]), src('US-FEDS5-001', 'periods', [IT]), src('US-CAS5-004', 'DE 44 supplemental', [IT])], ['fit.supplemental.flat.rate', 'fit.supplemental.mandatory.threshold'])
CM['accrual_vs_payment'] = A('Federal payroll taxes follow the PAYMENT date: FIT, FICA and FUTA apply to wages paid in the calendar year (OASDI base for remuneration paid in 2026; W-2 on calendar-year basis; FUTA 7,000 per employer in the calendar year). Exception to watch: MA PFML rates apply to wages EARNED on/after 1 January. A December-earned/January-paid wage takes the new year rates and bases federally.',
  'Withholding at payment; table year = payment date', 'Wage bases by payment date; MA PFML by earning date', 'W-2/941 by payment date',
  'm03_gross_to_net; m05_social_security', [src('US-FED-003', 'base for remuneration paid in 2026', [SS]), src('US-FED-006', 'calendar-year basis', [RP]), src('US-MULTIS5-009', 'paid in the calendar year', [SS]), src('US-MAS5-012', 'wages earned on/after Jan 1', [SS])],
  ['fica.oasdi.wage_base', 'tax_year.basis'])
COVERAGE = {'schema_version': '1.4.0', 'artifact': 'CCG', 'unit': 'coverage', 'code': 'US', 'year': 2026, 'generated_on': TODAY,
  '_note': 'Federal + multistate cut of the special-population matrix (US-OWN-005: all populations IN). State-specific treatments live in the annexes; each row names the annexes it routes to. Owner decision US-OWN-005 cannot be a source (tier owner, no URL).',
  'coverage_matrix': CM, 'facts': [], 'unresolved': [
    {'key': 'coverage.common_paymaster', 'why': 'Common-paymaster relief for related employers (multiple_employers row) was not researched in the FED unit.', 'attempted': [], 'what_would_close_it': 'IRC 3121(s) / Pub. 15-A common paymaster section read into a FED row.', 'blocking': False},
    {'key': 'coverage.workers_comp.employee_share', 'why': 'Only NM fee and WA employee deduction are known; other States allowing employee workers-comp deductions not swept.', 'attempted': [], 'what_would_close_it': 'Annex workers confirm per State (WA L&I rates; NM TRD-41431).', 'blocking': False}]}
