import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import Pack, BASE

P = Pack('annex_FED')
f, u = P.f, P.u
USD = 'USD'
Y26 = dict(ef='2026-01-01', et='2026-12-31')

# 1 labour
f('labour_code', 'fed.minwage.hourly', 7.25, 'US-FEDS5-017', cur=USD, note='FLSA 206(a)(1)(C); not indexed; no 2026/2027 change enacted. Employer pays the highest of federal, state and local minimum (state annexes).')
f('labour_code', 'fed.overtime.weekly_threshold_hours', 40, 'US-FEDS5-018', uom='hours', note='No federal daily overtime; daily OT is state law (state annexes).')
f('labour_code', 'fed.overtime.premium.multiplier', 1.5, 'US-FEDS5-018', uom='ratio', note='0.5 premium portion = qualified overtime compensation for P.L. 119-21 / W-2 code TT.')
f('labour_code', 'fed.tipped.cash_wage.hourly', 2.13, 'US-FEDS5-019', cur=USD)
f('labour_code', 'fed.tipped.tip_credit.max_hourly', 5.12, 'US-FEDS5-019', cur=USD, vm='derived arithmetically', note='7.25 - 2.13 = 5.12 (US-FEDS5-017 minimum wage minus cash wage).')
f('labour_code', 'fed.tipped.monthly_tips_threshold', 30, 'US-FEDS5-019', cur=USD, note='Tipped employee = customarily and regularly receives more than 30/month in tips (29 USC 203(t)).')
for per, v in [('weekly', 684), ('biweekly', 1368), ('semimonthly', 1482), ('monthly', 2964)]:
    f('labour_code', f'fed.exempt.salary_floor.{per}', v, 'US-FEDS5-020', cur=USD, note='EAP exemption, 29 CFR 541.600 current eCFR text (2024 increase not in the CFR).')
f('labour_code', 'fed.exempt.salary_floor.territories_weekly', 455, 'US-FEDS5-020', cur=USD, note='CNMI, Guam, PR, USVI.')
f('labour_code', 'fed.exempt.salary_floor.american_samoa_weekly', 380, 'US-FEDS5-020', cur=USD)

# 2 FIT
f('income_tax', 'fed.fit.method', 'IRS Pub. 15-T (2026) Worksheet 1A with the Annual Percentage Method tables (STANDARD schedule; Step-2-checked schedule when W-4 Step 2 box checked)', 'US-FEDS5-001', **Y26, level='withholding')
f('income_tax', 'fed.fit.worksheet1a.line1g.mfj', 12900, 'US-FEDS5-001', cur=USD, **Y26, note='Applied when the W-4 Step 2 box is NOT checked.')
f('income_tax', 'fed.fit.worksheet1a.line1g.other', 8600, 'US-FEDS5-001', cur=USD, **Y26)
f('income_tax', 'fed.fit.allowance.pre2020_value', 4300, 'US-FEDS5-001', cur=USD, **Y26, note='Per allowance on a pre-2020 Form W-4 (line 1k).')
rates = [0, 10, 12, 22, 24, 32, 35, 37]
sched = {
    'standard.mfj': [0, 19300, 44100, 120100, 230700, 422850, 531750, 788000],
    'standard.single': [0, 7500, 19900, 57900, 113200, 209275, 263725, 648100],
    'standard.hoh': [0, 15550, 33250, 83000, 121250, 217300, 271750, 656150],
    'step2.mfj': [0, 16100, 28500, 66500, 121800, 217875, 272325, 400450],
    'step2.single': [0, 8050, 14250, 33250, 60900, 108938, 136163, 328350],
    'step2.hoh': [0, 12075, 20925, 45800, 64925, 112950, 140175, 332375],
}
from decimal import Decimal as D
for s, th in sched.items():
    cum = [D(0)]
    for i in range(1, 8):
        cum.append(cum[-1] + (D(th[i]) - D(th[i - 1])) * D(rates[i - 1]) / 100)
    for i in range(8):
        n = i + 1
        f('income_tax', f'fed.fit.{s}.bracket.{n}.floor', th[i], 'US-FEDS5-001', cur=USD, **Y26,
          note=('Single schedule also used for MFS.' if 'single' in s and n == 1 else None))
        f('income_tax', f'fed.fit.{s}.bracket.{n}.rate', rates[i], 'US-FEDS5-001', uom='percent', **Y26)
        if s.startswith('standard'):
            c = float(cum[i])
            f('income_tax', f'fed.fit.{s}.bracket.{n}.cumulative_tax', c, 'US-FEDS5-001', cur=USD, **Y26,
              vm='derived arithmetically',
              note='Column C re-derived in Python from column A thresholds and the 0/10/12/22/24/32/35/37 rates; top values 206,583.50 (MFJ) / 192,979.25 (Single) / 191,171.00 (HoH) equal the figures in US-FEDS5-001.')
for st, v, z in [('mfj', 32200, 19300), ('single', 16100, 7500), ('hoh', 24150, 15550)]:
    f('income_tax', f'fed.fit.std_deduction.{st}', v, 'US-FEDS5-010', cur=USD, **Y26,
      vm='second independent authority',
      note=f'Rev. Proc. 2025-32; G-DERIVE: standard deduction minus line 1g = zero bracket {z} of Pub. 15-T (US-FEDS5-001).')
f('income_tax', 'fed.fit.pay_periods_per_year', '2 / 4 / 12 / 24 / 26 / 52 / 260 (semiannual, quarterly, monthly, semimonthly, biweekly, weekly, daily)', 'US-FEDS5-001', **Y26)
f('income_tax', 'fed.fit.rounding', 'Optional: wages may be rounded to the nearest dollar and the period tax rounded to the nearest dollar (drop under 50 cents, 50-99 cents up)', 'US-FED-001')
f('income_tax', 'fed.fit.supplemental.flat_rate', 22, 'US-FEDS5-003', uom='percent', note='Optional flat method; made permanent by P.L. 119-21.', level='withholding')
f('income_tax', 'fed.fit.supplemental.mandatory_rate', 37, 'US-FEDS5-003', uom='percent', level='withholding')
f('income_tax', 'fed.fit.supplemental.mandatory_threshold', 1000000, 'US-FEDS5-003', cur=USD, note='Supplemental wages above 1,000,000 paid to one employee in the calendar year.')
f('income_tax', 'fed.fit.backup_withholding.rate', 24, 'US-FEDS5-003', uom='percent')
f('income_tax', 'fed.w4.input_fields', 'filing status (Single/MFS, MFJ/QSS, HoH); Step 2 flag; Step 3 amount; Step 4(a); Step 4(b); Step 4(c); exempt checkbox', 'US-FEDS5-006', **Y26)
f('income_tax', 'fed.w4.exempt.validity', '2026 only: the exemption checkbox certification lapses; a new W-4 is required for 2027', 'US-FEDS5-006', **Y26)
# 2b NRA
nra2 = [('weekly', 309.60), ('biweekly', 619.20), ('semimonthly', 670.80), ('monthly', 1341.70), ('quarterly', 4025.00), ('semiannual', 8050.00), ('annual', 16100.00), ('daily', 61.90)]
nra1 = [('weekly', 226.90), ('biweekly', 453.80), ('semimonthly', 491.70), ('monthly', 983.30), ('quarterly', 2950.00), ('semiannual', 5900.00), ('annual', 11800.00), ('daily', 45.40)]
for per, v in nra2:
    f('income_tax_nonresident', f'fed.fit.nra.addon.table2.{per}', v, 'US-FEDS5-002', cur=USD, **Y26, level='withholding',
      note='Table 2: 2020+ W-4 or first paid 2020+. Added to wages for the FIT computation only (not on W-2, no FICA/FUTA effect); not applied to 22%/37% supplemental. Annual = single standard deduction 16,100.')
for per, v in nra1:
    f('income_tax_nonresident', f'fed.fit.nra.addon.table1.{per}', v, 'US-FEDS5-002', cur=USD, **Y26, level='withholding',
      note='Table 1: first paid before 2020 with no 2020+ W-4. Annual 11,800 = 16,100 - 4,300.')
f('income_tax_nonresident', 'fed.fit.nra.w4.rule', 'Check Single or MFS regardless of marital status; write NRA below Step 4(c); exempt not allowed; Step 3 only for residents of Canada, Mexico, South Korea or India (students/apprentices)', 'US-FEDS5-015', level='withholding', note='Notice 1392 (Rev. 1-2020) still the posted edition.')
f('income_tax_nonresident', 'fed.fit.nra.treaty_exempt.reporting', 'Treaty-exempt wages claimed on Form 8233 are reported on Form 1042-S (not W-2 box 1); 2026 Forms 1042-S due 2027-03-15 and must be e-filed via IRIS', 'US-FEDS5-016', level='employer reporting')
f('income_tax_nonresident', 'fed.fit.nra.commercial_traveler.max_days', 90, 'US-FEDS5-016', uom='days', note='Exception from withholding: NRA present <= 90 days, total pay <= 3,000, foreign employer not engaged in US trade/business.')
f('income_tax_nonresident', 'fed.fit.nra.commercial_traveler.max_pay', 3000, 'US-FEDS5-016', cur=USD)

# 3 FICA / FUTA
f('social_security', 'fed.fica.oasdi.rate.employee', 6.2, 'US-FEDS5-005', uom='percent', **Y26)
f('social_security', 'fed.fica.oasdi.rate.employer', 6.2, 'US-FEDS5-005', uom='percent', **Y26)
f('social_security', 'fed.fica.oasdi.wage_base', 184500, 'US-FEDS5-005', cur=USD, **Y26, vm='derived arithmetically',
  note='G-DERIVE (US-FED-003, Federal Register 2025-19763): 60,600 x AWI(2024) 69,846.57 / AWI(1992) 22,935.42 = 184,548.71, rounded to a multiple of 300 = 184,500.')
f('social_security', 'fed.fica.oasdi.wage_base', 192300, 'US-FED-022', cur=USD, ef='2027-01-01', et='2027-12-31', conf='medium',
  note='SSA published 2027 figure (cbb.html table 1937-2027). Re-verification on 2026-11-02 blocked (ssa.gov 403); not derived (AWI 2025 not held).')
f('social_security', 'fed.fica.medicare.rate.employee', 1.45, 'US-FEDS5-005', uom='percent', **Y26, note='No wage base.')
f('social_security', 'fed.fica.medicare.rate.employer', 1.45, 'US-FEDS5-005', uom='percent', **Y26)
f('social_security', 'fed.fica.addl_medicare.rate', 0.9, 'US-FEDS5-005', uom='percent', **Y26, note='Employee only, no employer match.')
f('social_security', 'fed.fica.addl_medicare.withholding_threshold', 200000, 'US-FEDS5-005', cur=USD, **Y26, note='Wages paid in excess of 200,000 in the calendar year, regardless of filing status.', level='withholding')
f('social_security', 'fed.futa.rate.gross', 6.0, 'US-FED-007', uom='percent')
f('social_security', 'fed.futa.credit.max', 5.4, 'US-FED-007', uom='percent')
f('social_security', 'fed.futa.rate.net', 0.6, 'US-FED-007', uom='percent', note='Plus any credit reduction for the state of the wages (Schedule A).')
f('social_security', 'fed.futa.wage_base', 7000, 'US-FED-007', cur=USD, note='Per employee per employer per calendar year across all States (US-MULTIS5-009).')
f('social_security', 'fed.futa.credit_reduction.ca', 1.2, 'US-FEDS5-009', uom='percent', ef='2025-01-01', et='2025-12-31', note='FINAL for 2025 (Form 940 for 2025, Schedule A).')
f('social_security', 'fed.futa.credit_reduction.vi', 4.5, 'US-FEDS5-009', uom='percent', ef='2025-01-01', et='2025-12-31', note='FINAL for 2025, U.S. Virgin Islands.')
f('social_security', 'fed.futa.deposit_threshold', 500, 'US-FEDS5-031', cur=USD, note='Deposit FUTA for a quarter when accumulated liability exceeds 500.')

# 4 payslip
f('payslip_statute', 'fed.payslip.statute.exists', False, 'US-FEDS5-021', note='No federal pay-statement content/delivery rule; FLSA prescribes records only (29 CFR 516.2, US-FED-010). Pay statements = state law.')
f('payslip_statute', 'fed.records.flsa.retention_years', 3, 'US-FEDS5-021', uom='years', note='29 CFR 516.5; supplementary records 2 years (516.6).')
f('payslip_statute', 'fed.records.irs.retention_years', 4, 'US-FEDS5-003', uom='years')

# 5 reporting
f('reporting', 'fed.deposit.lookback_period', '2024-07-01 to 2025-06-30 (Form 941 filers); CY2024 for 943/944/945 filers', 'US-FEDS5-004', **Y26)
f('reporting', 'fed.deposit.monthly_max_lookback_liability', 50000, 'US-FEDS5-004', cur=USD, note='<= 50,000 monthly depositor (by the 15th of the following month); > 50,000 semiweekly (Wed/Thu/Fri paydays -> following Wednesday; Sat-Tue -> following Friday).')
f('reporting', 'fed.deposit.next_day_threshold', 100000, 'US-FEDS5-004', cur=USD, note='100,000 or more accumulated on any day -> deposit next business day; deposit holidays = DC legal holidays.')
f('reporting', 'fed.form941.frequency', 'quarterly; due last day of the month after the quarter; amounts in cents', 'US-FEDS5-031')
f('reporting', 'fed.form944.max_liability', 1000, 'US-FEDS5-031', cur=USD, note='Annual Form 944 only on written IRS notice.')
f('reporting', 'fed.form940.due', 'January 31 (10 more days if all FUTA deposited on time)', 'US-FEDS5-031')
f('reporting', 'fed.w2.due_date', '2027-02-01', 'US-FEDS5-007', note='TY2026 Copy A to SSA and employee copies.')
f('reporting', 'fed.w2.no_withholding_threshold', 2000, 'US-FEDS5-007', cur=USD, note='W-2 required at 2,000+ wages even with no withholding (was 600); indexed after 2026 (US-FEDS5-003).')
f('reporting', 'fed.w2.box12.new_codes', 'TP (cash tips reported to employer); TT (qualified overtime compensation); TA (employer Trump-account contributions)', 'US-FEDS5-007', level='employer reporting')
f('reporting', 'fed.w2.box14b', 'Box 14 split into 14a Other and 14b Treasury Tipped Occupation Code(s)', 'US-FEDS5-007', level='employer reporting')
f('reporting', 'fed.aca.ale.fte_threshold', 50, 'US-FEDS5-012', uom='employees', ef='2025-01-01', note='TY2025 instructions (TY2026 edition not yet published).')
f('reporting', 'fed.aca.efile_threshold', 10, 'US-FEDS5-012', uom='returns', ef='2025-01-01')
f('reporting', 'fed.aca.affordability.rate', 9.96, 'US-FEDS5-011', uom='percent', **Y26, note='Required contribution percentage, plan years beginning in 2026.')
f('reporting', 'fed.newhire.deadline_days', 20, 'US-FEDS5-024', uom='days', note='Or, electronic filers, two monthly transmissions 12-16 days apart; state deadlines shorter per state annex.')
f('reporting', 'fed.newhire.fields', 'employee name, address, SSN, date services first performed; employer name, address, FEIN', 'US-FEDS5-024')
f('reporting', 'fed.reporting_agent.authorization', 'Form 8655 (Rev. Jan 2024); agent may sign/file 940/941 and deposit; taxpayer stays liable', 'US-FED-008')

# 6 leave
f('leave', 'fed.fmla.weeks', 12, 'US-FEDS5-026', uom='weeks', note='In a 12-month period; may be unpaid; employer may require substitution of accrued paid leave.')
f('leave', 'fed.fmla.military_caregiver.weeks', 26, 'US-FEDS5-026', uom='weeks')
f('leave', 'fed.paid_leave.private_employers.exists', False, 'US-FEDS5-026', note='No federal paid sick or annual leave for private employers; contractors under EO 13706 (accrual not transcribed).')
f('leave', 'fed.pfml.employee_contribution.is_w2_wages', True, 'US-FEDS5-007', note='State PFML employee contribution and employer voluntary payment are W-2 wages (Rev. Rul. 2025-4, Notice 2026-6).')

# 7 termination
f('termination', 'fed.final_pay.rule', 'No federal immediate final-pay rule; wages due by the regular payday; timing and vacation payout are state law', 'US-FEDS5-025')
f('termination', 'fed.warn.notice_days', 60, 'US-FEDS5-025', uom='days', note='Pay in lieu = back-pay liability (29 USC 2104).')
f('termination', 'fed.severance.is_wages', True, 'US-FEDS5-029', note='Severance is wages for FIT, FICA and FUTA.')

# 8 BIK
f('benefits_in_kind', 'fed.bik.parking.monthly_exclusion', 340, 'US-FEDS5-008', cur=USD)
f('benefits_in_kind', 'fed.bik.transit.monthly_exclusion', 340, 'US-FEDS5-008', cur=USD)
f('benefits_in_kind', 'fed.bik.health_fsa.salary_reduction_cap', 3400, 'US-FEDS5-010', cur=USD, **Y26)
f('benefits_in_kind', 'fed.bik.health_fsa.carryover_max', 680, 'US-FEDS5-010', cur=USD, **Y26)
f('benefits_in_kind', 'fed.bik.dependent_care.exclusion', 7500, 'US-FEDS5-008', cur=USD, note='3,750 MFS; raised from 5,000 by P.L. 119-21.')
f('benefits_in_kind', 'fed.bik.educational_assistance.exclusion', 5250, 'US-FEDS5-008', cur=USD, note='Exclusion made permanent.')
f('benefits_in_kind', 'fed.bik.group_term_life.excluded_coverage', 50000, 'US-FEDS5-008', cur=USD, note='Imputed cost of coverage above 50,000 is FICA wages; FIT withholding not required.')
for band, v in [('under_25', 0.05), ('25_29', 0.06), ('30_34', 0.08), ('35_39', 0.09), ('40_44', 0.10), ('45_49', 0.15), ('50_54', 0.23), ('55_59', 0.43), ('60_64', 0.66), ('65_69', 1.27), ('70_plus', 2.06)]:
    f('benefits_in_kind', f'fed.bik.group_term_life.monthly_cost_per_1000.{band}', v, 'US-FEDS5-008', cur=USD, note='Pub. 15-B Table 2-2.')
f('benefits_in_kind', 'fed.bik.trump_account.employer_contribution_max', 2500, 'US-FEDS5-030', cur=USD, ef='2026-07-04', note='Sec. 128 program; W-2 code TA; indexed after 2027.')
f('benefits_in_kind', 'fed.bik.moving_and_bicycle.excluded', False, 'US-FEDS5-008', note='Moving-expense and bicycle-commuting exclusions eliminated (moving: except Armed Forces / intelligence community).')
f('benefits_in_kind', 'fed.retirement.401k.elective_deferral_limit', 24500, 'US-FED-023', cur=USD, et='2026-12-31')
f('benefits_in_kind', 'fed.retirement.401k.catch_up_50', 8000, 'US-FED-023', cur=USD, et='2026-12-31')
f('benefits_in_kind', 'fed.retirement.401k.catch_up_60_63', 11250, 'US-FED-023', cur=USD, et='2026-12-31')
f('benefits_in_kind', 'fed.retirement.simple.deferral_limit', 17000, 'US-FED-023', cur=USD, et='2026-12-31', note='18,100 for SIMPLE plans with the higher limit.')
f('benefits_in_kind', 'fed.hsa.limit.self_only', 4400, 'US-FED-024', cur=USD, et='2026-12-31')
f('benefits_in_kind', 'fed.hsa.limit.family', 8750, 'US-FED-024', cur=USD, et='2026-12-31')
f('benefits_in_kind', 'fed.feie.amount', 132900, 'US-FED-025', cur=USD, ef='2026-01-01', et='2026-12-31', note='Rev. Proc. 2025-32 sec. 911 item, also stated in US-FED-P5-2-002 (same document, item .38). Foreign earned income exclusion; employer may stop FIT withholding on the employee statement (US-FEDR3-007).')

# 9 garnishment
f('deductions_garnishments', 'fed.ccpa.max_rate', 25, 'US-FEDS5-023', uom='percent', note='Lesser of 25% of weekly disposable earnings or the amount above 30 x 7.25.')
f('deductions_garnishments', 'fed.ccpa.protected_weekly', 217.50, 'US-FEDS5-023', cur=USD, note='30 x 7.25.')
f('deductions_garnishments', 'fed.ccpa.support.max_rate.with_dependents', 50, 'US-FEDS5-023', uom='percent', note='55% with arrears older than 12 weeks.')
f('deductions_garnishments', 'fed.ccpa.support.max_rate.without_dependents', 60, 'US-FEDS5-023', uom='percent', note='65% with arrears older than 12 weeks.')
f('deductions_garnishments', 'fed.ccpa.support.arrears_addon', 5, 'US-FEDS5-023', uom='percent', vm='quoted from authority page', note='+5 points (55/65) where arrears older than 12 weeks.')
for per, v in [('daily', 61.92), ('weekly', 309.62), ('biweekly', 619.23), ('semimonthly', 670.83), ('monthly', 1341.67)]:
    f('deductions_garnishments', f'fed.levy.exempt.single_0dep.{per}', v, 'US-FEDS5-014', cur=USD, **Y26, note='Pub. 1494 (2026); MFS = Single. Weekly = 16,100/52; monthly = 16,100/12.')
for per, v in [('daily', 20.38), ('weekly', 101.92), ('biweekly', 203.85), ('semimonthly', 220.83), ('monthly', 441.67)]:
    f('deductions_garnishments', f'fed.levy.exempt.per_dependent.{per}', v, 'US-FEDS5-014', cur=USD, **Y26, note='5,300/52 weekly; 5,300/12 monthly.')
f('deductions_garnishments', 'fed.levy.exempt.mfj_0dep.weekly', 619.23, 'US-FEDS5-014', cur=USD, **Y26)
f('deductions_garnishments', 'fed.levy.exempt.mfj_0dep.monthly', 2683.33, 'US-FEDS5-014', cur=USD, **Y26)
f('deductions_garnishments', 'fed.levy.exempt.hoh_0dep.weekly', 464.42, 'US-FEDS5-014', cur=USD, **Y26)
f('deductions_garnishments', 'fed.iwo.priority', 'IWO for support ranks before other garnishments, except an IRS levy served before the underlying support order', 'US-FEDS5-014', note='Stated in US-FEDS5-014 (Pub. 1494 row) citing the OCSS employer page US-FED-P5-1-006.')
f('deductions_garnishments', 'fed.iwo.omb_expiry', '2029-08-31', 'US-FEDS5-028', note='OMB 0970-0154 approved without change 2026-08-25; current form extended one year while states reprogram the revised (gig-worker fields) IWO/e-IWO. Supersedes US-FEDP6-001.', level='employer withholding')

# 10 CBA
f('collective_agreements', 'fed.cba.scope', 'A CBA binds the certified bargaining unit only; no sector-wide extension mechanism', 'US-FED-018')
f('collective_agreements', 'fed.davis_bacon.contract_threshold', 2000, 'US-FED-019', cur=USD, note='Federal construction contracts over 2,000.')
f('collective_agreements', 'fed.davis_bacon.certified_payroll.frequency', 'weekly, to the contracting agency; prime responsible for subcontractors; optional form WH-347; records 3 years', 'US-FEDS5-027')

# 11 indexation
f('indexation', 'fed.indexation.caliber', 'C-CPI-U (chained CPI-U) under 26 U.S.C. 1(f)(3)', 'US-FED-026', note='Rev. Proc. 2025-32 applies it for 2026 (US-FEDS5-010). OASDI base indexed on AWI (US-FED-003). FLSA minimum wage, CCPA multiplier and the 684 salary floor are NOT indexed.')
f('indexation', 'fed.indexation.oasdi_caliber', 'National Average Wage Index (AWI), base rounded to a multiple of 300', 'US-FED-003')

# 12 data protection
f('data_protection', 'fed.ssn.truncation.format', 'XXX-XX-1234 (TTIN); allowed on employee W-2 copies only; never on Copy A; EIN never truncated', 'US-FEDS5-022')

# 13 live change
f('live_legal_change', 'fed.plaw119_21.qualified_tips.deduction_cap', 25000, 'US-FEDS5-030', cur=USD, ef='2025-01-01', et='2028-12-31', level='assessment',
  note='IN FORCE (enacted 2025-07-04). Reaches withholding only via W-4 Step 4(b); employer reporting via W-2 TP/14b; tips stay fully FICA-subject. Do NOT model as a payroll deduction.')
f('live_legal_change', 'fed.plaw119_21.qualified_overtime.deduction_cap', 12500, 'US-FEDS5-030', cur=USD, ef='2025-01-01', et='2028-12-31', level='assessment',
  note='25,000 MFJ. Employer reporting via W-2 TT; overtime stays fully FICA-subject.')
f('live_legal_change', 'fed.plaw119_21.qualified_overtime.deduction_cap_mfj', 25000, 'US-FEDS5-030', cur=USD, ef='2025-01-01', et='2028-12-31', level='assessment')
f('live_legal_change', 'fed.plaw119_21.reporting_penalty_relief', 'TY2025 only (Notice 2025-62); separate reporting of tips/TTOC/overtime mandatory from TY2026', 'US-FEDS5-013', level='employer reporting')

# special populations
f('special_populations', 'fed.household.fica_cash_threshold', 3000, 'US-FEDS5-029', cur=USD, **Y26, note='FICA if cash wages 3,000+ in 2026 (exempt under 18 unless principal occupation); FIT only by agreement; Schedule H.')
f('special_populations', 'fed.household.futa_quarter_threshold', 1000, 'US-FEDS5-029', cur=USD, note='FUTA if 1,000+ cash wages in any quarter of current or prior year.')
f('special_populations', 'fed.agricultural.per_worker_threshold', 150, 'US-FEDR3-006', cur=USD, note='Cash wages 150+ to a farmworker in a year, or 2,500+ total farm pay, make cash wages subject to FICA and FIT; Form 943.')
f('special_populations', 'fed.agricultural.total_threshold', 2500, 'US-FEDR3-006', cur=USD)
f('special_populations', 'fed.agricultural.futa_quarter_threshold', 20000, 'US-FEDR3-006', cur=USD, note='Or 10+ farmworkers on some part of a day in 20+ weeks.')
f('special_populations', 'fed.election_worker.fica_threshold', 2500, 'US-FEDS5-003', cur=USD, **Y26)
f('special_populations', 'fed.tips.reporting_threshold_monthly', 20, 'US-FEDS5-003', cur=USD, note='Tips of 20+ in a month are subject to FIT/FICA.')
f('special_populations', 'fed.minister.withholding', 'No FIT, social security or Medicare withholding (SE tax; voluntary FIT withholding agreement allowed); parsonage allowance excluded from W-2 box 1', 'US-FED-030')
f('special_populations', 'fed.statutory_employee.treatment', 'FICA withheld, no FIT withholding; W-2 box 13 checked; FUTA for drivers and traveling salespersons only', 'US-FEDR3-005')
f('special_populations', 'fed.family_employment.treatment', 'Child under 18 of a sole proprietor/parents-only partnership: FICA exempt, FUTA exempt under 21; spouse: FUTA exempt; parent employed by child: FUTA exempt', 'US-FEDS5-029')
f('special_populations', 'fed.students.treatment', 'Private school/college students: FIT withheld, FICA and FUTA exempt; public school: FICA exempt unless sec. 218 agreement; work-experience full-time student: FICA taxable', 'US-FEDS5-029')
f('special_populations', 'fed.government_employee.treatment', 'FIT withheld; no FUTA; FICA with sec. 218 / Medicare-only exceptions', 'US-FEDS5-029')

# oracle (federal; also offered to m12)
f('oracle', 'fed.oracle.pub15t.nra_example.wages', 526.90, 'US-FED-027', cur=USD, note='Weekly wages 300 + Table 1 add-on 226.90 = 526.90 (Pub. 15-T 2026 example).')
f('oracle', 'fed.oracle.pub15t.nra_example.withholding', 31, 'US-FED-027', cur=USD, note='Wage-bracket result for 526.90 weekly; residual none recorded. Stage 9b re-derives the percentage method from Worksheet 1A (no full percentage-method example is published).')
f('oracle', 'fed.oracle.pub15t.tribal_example.payment', 6000, 'US-FED-027', cur=USD, note='Tribal monthly gaming payment example.')
f('oracle', 'fed.oracle.pub15t.tribal_example.withholding', 584.09, 'US-FED-027', cur=USD)

# unresolved
u('fed.futa.credit_reduction.ca', 'The 2026 California credit reduction (potential 5.3% = 1.5% advance + 3.8% BCR add-on) becomes final only if the Title XII advance is outstanding on 2026-11-10; on 2026-11-02 only the potential figure is published (US-FEDS5-009, partial).',
  'The DOL OUI "FUTA Credit Reductions" page/xlsx after 2026-11-10, or the 2026 Schedule A (Form 940) instructions.', ['https://oui.doleta.gov/unemploy/futa_credit.asp (2026-11-02, page updated 2026-09-11)'], False, ['US-FEDS5-009'])
u('fed.futa.credit_reduction.vi', 'U.S. Virgin Islands 2026 potential 4.8%; same 2026-11-10 determination.', 'Same DOL OUI update after 2026-11-10.', ['https://oui.doleta.gov/unemploy/futa_credit.asp'], False, ['US-FEDS5-009'])
u('fed.efw2.layout', 'SSA EFW2 (Pub. 42-007) TY2026 not read: ssa.gov 403, Wayback 404, archive.org API 429 (US-FEDS5-032 gated).',
  'SSA Pub. 42-007 TY2026 (26efw2.pdf) downloaded in the browser pass or from a non-blocked network.', ['https://www.ssa.gov/employer/efw/26efw2.pdf (403)', 'https://web.archive.org/web/2026id_/https://www.ssa.gov/employer/efw/26efw2.pdf (404)'], False, ['US-FEDS5-032', 'US-FED-P5-1-013'])
u('fed.fica.oasdi.wage_base.next_year_reverification', 'The 2027 OASDI base 192,300 is registered (US-FED-022) but could not be re-verified on 2026-11-02 (ssa.gov/oact/cola/cbb.html 403, Wayback 403).',
  'The SSA 2027 COLA fact sheet or cbb.html read in the browser pass; or the 2027 Federal Register notice of the contribution and benefit base.', ['https://www.ssa.gov/oact/cola/cbb.html (403)'], False, ['US-FED-022'])
u('fed.indexation.next_year', '2027 federal inflation adjustments (Rev. Proc. for TY2027, 401(k)/IRA notice, 2027 Pub. 15-T) not published as of 2026-11-02 (IR-2026-117..129 checked).',
  'IRS releases expected Nov-Dec 2026: the TY2027 Rev. Proc., the 2027 retirement-plan limits notice and the 2027 Pub. 15-T (draft or final).', ['IRS news releases October 2026'], False, ['US-FEDS5-010'])
u('fed.form940.instructions_edition', 'TY2026 Instructions for Form 940 not yet issued; the 2025 edition was read (US-FEDS5-031 partial).', 'IRS i940 (2026), usually December-January.', [], False, ['US-FEDS5-031'])
u('fed.aca.instructions_edition', 'TY2026 Instructions for Forms 1094-C/1095-C not yet issued; TY2025 edition read (US-FEDS5-012 partial).', 'IRS i109495c (2026).', [], False, ['US-FEDS5-012'])
u('fed.leave.eo13706.accrual', 'EO 13706 federal-contractor paid-sick-leave accrual figures not transcribed.', '29 CFR 13.5 from eCFR (one fetch).', [], False, ['US-FEDS5-026'])
u('fed.bik.mileage_rate', '2026 business standard mileage rate (cents-per-mile valuation) not printed in Pub. 15-B and not fetched.', 'The IRS 2026 standard mileage rate notice.', [], False, ['US-FEDS5-008'])
u('fed.iwo.revised_form_go_live', 'The revised IWO/e-IWO (gig-worker fields) must be used after the one-year extension, but the state go-live date is not published.', 'An OCSE Action Transmittal implementing ICR 202607-0970-002.', ['https://www.reginfo.gov/public/do/PRAViewICR?ref_nbr=202607-0970-002'], False, ['US-FEDS5-028'])

out = os.path.join(BASE, '_research', 'CCG-annex_FED-facts.json')
P.dump(out, {'_jurisdiction': 'Federal layer (United States)',
             '_key_convention': 'Keys are prefixed fed. (federal layer) so one key = one meaning country-wide across the 53 CCG annexes; state annexes use {jur}., the multistate routing layer multi.',
             '_produced_by': 'Synthesis-B worker CCG annexes FED+MULTI, from _research/stage5/FED.md and active/partial register rows only (no fetching)'})
json.dump({'ids': sorted(P.ids), 'warnings': P.warnings, 'n_facts': P.n_good, 'n_pending': P.n_bad, 'n_unres': len(P.unresolved)},
          open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fed_meta.json'), 'w'), indent=1)
print(len(P.facts), P.n_good, P.n_bad, len(P.unresolved), len(P.ids)); print('\n'.join(P.warnings))
