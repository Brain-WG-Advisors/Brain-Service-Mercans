import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import Pack, BASE

P = Pack('annex_MULTI')
f, u = P.f, P.u
USD = 'USD'

# 1 labour - overlay and CA reach rulings
f('labour_code', 'multi.wage_hour.overlay_rule', 'FLSA does not excuse a higher State/municipal minimum wage, a lower maximum workweek or a stricter child-labour standard: apply the more protective standard of the place where the work is performed', 'US-MULTIS5-008')
f('labour_code', 'multi.ca.oman.rule', 'Oman v. Delta Air Lines, Cal. S. Ct. S248726 (2020-06-29), Lab. Code 204 and 226: do not reach pay periods in which the employee works in CA only episodically and for less than a day at a time, unless the employee works primarily in CA in that period, or works primarily in no State and has the CA base of operations. Minimum-wage reach left undecided.',
  'US-MULTIS5-019', level='employer pay timing and pay statement', note='STATUS: in force (final answer to certified question).')

# 2.1 general sourcing
f('income_tax', 'multi.pit.sourcing.general', 'No general federal rule: each State taxes residents on all wages (credit at assessment for tax paid to the work State) and nonresidents on wages for services performed in the State; federal limits only for transport workers and military spouses. 4 U.S.C. 114 is retirement income only, not wages.', 'US-FED-P5-1-009')

# 2.2 resident working in another State (withholding level)
res = [
    ('ct', 'All wages subject; where the employer must withhold for the other jurisdiction, CT tax is prorated and only the excess remitted', 'US-CTP10-001'),
    ('ks', 'KS tax on total wages less the other State\'s required withholding (example 250 - 130 = 120); zero if the other State\'s withholding is higher', 'US-KS-P5-1-003'),
    ('vt', 'Compute on the full payment, then reduce by tax withheld for the State where services were performed', 'US-VT-P5-1-003'),
    ('nc', 'Withhold on all wages wherever earned, except no NC withholding on wages for services in a State that requires the employer to withhold', 'US-NC-P5-1-002'),
    ('co', 'Withhold CO on all wages except wages for services in another State that itself requires withholding', 'US-CO-P5-1-002'),
    ('ga', 'No GA withholding if the other State requires withholding; otherwise withhold GA', 'US-GAS5-004'),
    ('sc', 'Withhold for the other State; if that State has no income tax, withhold 100% SC (12-8-520(C)(1))', 'US-SCR3-003'),
    ('ok', 'Residents are withheld on services within or without Oklahoma (68 O.S. 2385.1 employee definition)', 'US-OKS5-010'),
    ('oh', 'Every employer with an office or transacting business in Ohio withholds on residents (resident credit IT RC at assessment)', 'US-OH-P5-2-006'),
    ('ny', 'Withhold NYS tax for NY residents even if wages are earned outside NY', 'US-NY-013'),
    ('la', 'LA residents working in another State may be subject to LA withholding if those wages are not subject to withholding there', 'US-LA-P5-1-001'),
    ('ms', 'Withhold MS on total wages except to the extent withheld for another State; commuter to a no-income-tax State is withheld MS on total wages (credit at assessment). Corrects MULTI.md 2.2, which listed MS as credit-only.', 'US-MSS5-004'),
    ('ma', 'MA amount minus the other jurisdiction\'s amount (credit method, 830 CMR 62B.2.1(9)(b)); employer without MA office may withhold for MA residents as a convenience', 'US-MAS5-023'),
    ('wi', 'Residents working outside WI: withholding on all wages; Minnesota special arrangement - no WI withholding if MN withholds', 'US-WIS5-011'),
    ('il', 'IL resident working entirely in another State whose compensation is subject to that State\'s withholding: no IL withholding (credit on the return)', 'US-ILS5-014'),
]
for st, rule, rid in res:
    f('income_tax', f'multi.resident_out_of_state.{st}.withholding_rule', rule, rid, level='withholding')
for st, rid in [('dc', 'US-DC-P5-1-007'), ('me', 'US-ME-P5-2-004'), ('ri', 'US-RI-P5-2-002'), ('sc', 'US-SCR3-004'), ('oh', 'US-OH-P5-2-004'),
                ('ar', 'US-ARS5-006'), ('ok', 'US-OK-P5-2-002'), ('ms', 'US-MSS5-019'), ('az', 'US-AZ-WH-003')]:
    f('income_tax', f'multi.resident_credit.{st}.level', 'assessment', rid, level='assessment',
      note='Credit for tax paid to another State is claimed on the individual return; the WTC/DD must NOT model it as a payroll deduction.' + (' AZ: nonresident credit conditioned on reciprocity of credit.' if st == 'az' else ''))

# 2.3 reciprocity
rec = [
    ('dc', 'MD, VA (from the partner side; DC taxes no nonresident at all)', 'D-4A', 'US-MULTI-016'),
    ('ia', 'IL', 'IA 44-016 (IL resident in IA); IL-W-5-NR (IA resident in IL)', 'US-MULTI-018'),
    ('il', 'IA, KY, MI, WI', 'IL-W-5-NR', 'US-ILS5-014'),
    ('in', 'KY, MI, OH, PA, WI (county tax still withheld)', 'WH-47', 'US-IN-002'),
    ('ky', 'IL, IN, MI, OH (unless 20% S-corp shareholder-employee), VA (daily commuters only), WV, WI', '42A809', 'US-MULTI-009'),
    ('md', 'DC, PA, VA, WV (not for abode in MD > 6 months and 183+ days, except WV)', 'MW507', 'US-MULTI-008'),
    ('mi', 'IL, IN, KY, MN, OH, WI', 'per MI Guide 446 (form not named in the row)', 'US-MULTI-010'),
    ('mn', 'MI, ND (employee returns home at least monthly)', 'MWR (yearly; copies to MN DOR by Mar 31)', 'US-MULTI-013'),
    ('mt', 'ND', 'MW-4 (annual renewal)', 'US-MT-P5-1-004'),
    ('nd', 'MN, MT', 'NDW-R (yearly, by Feb 28 or within 30 days)', 'US-MULTI-014'),
    ('nj', 'PA (compensation only)', 'NJ-165 (PA resident in NJ); REV-419EX (NJ resident with PA employer)', 'US-MULTI-011'),
    ('oh', 'IN, KY, MI, PA, WV', 'IT 4 (combined certificate)', 'US-MULTI-005'),
    ('pa', 'IN, MD, NJ, OH, VA, WV', 'REV-419', 'US-MULTI-007'),
    ('va', 'DC, KY (daily commuters), MD, PA, WV', 'VA certificate (not named in the row; VA annex)', 'US-MULTI-004'),
    ('wi', 'IL, IN, KY, MI', 'W-220', 'US-MULTI-006'),
    ('wv', 'KY, MD, OH, PA, VA', 'WV/IT-104', 'US-MULTI-015'),
]
for st, partners, cert, rid in rec:
    f('income_tax', f'multi.reciprocity.{st}.partners', partners, rid, level='withholding',
      note='Bilateral exemption from work-State withholding on the employee nonresidence certificate; 30 pairs confirmed on both sides (MULTI.md 2.3). Local taxes are outside State reciprocity.')
    f('income_tax', f'multi.reciprocity.{st}.certificate', cert, {'il': 'US-IL-P5-1-001'}.get(st, rid), level='withholding')
f('income_tax', 'multi.reciprocity.az.unilateral', 'AZ exempts residents of CA, IN, OR, VA on Form WEC (they can claim the AZ credit); one-way - an AZ resident working in CA is withheld by CA', 'US-MULTI-017', level='withholding')
f('income_tax', 'multi.reciprocity.dc.nonresident_exempt', 'D.C. Code 1-206.02(a)(5): DC may not tax any nonresident\'s personal income; DC withholding stops for ANY nonresident (D-4A: domicile outside DC and under 183 days)', 'US-DC-P5-1-006', level='withholding')
for st, rid, txt in [('de', 'US-MULTI-019', 'none'), ('mo', 'US-MOS5-001', 'none'), ('me', 'US-ME-P5-2-005', 'none in force (agreements authorised by statute, none identified)'),
                     ('ct', 'US-CTP10-001', 'none'), ('ar', 'US-AR-P5-2-001', 'none (zero hits for reciprocity in the AR instructions)'),
                     ('vt', 'US-VT-P5-2-003', 'none (four official withholding texts, none lists one)'), ('nc', 'US-NC-P5-1-002', 'none'), ('ga', 'US-GA-P5-2-003', 'none')]:
    f('income_tax', f'multi.reciprocity.{st}.partners', txt, rid, level='withholding')

# 2.4 nonresident thresholds
thr = [
    ('al', 'days', 30, 'US-ALS5-003', '30 or fewer AL days, duties in more than one State, home State has a similar exclusion or no PIT; from day 31 all AL income for the year is withheld/reported. Qualifying States as of 2026-10-01: AK, FL, GA, IL, IN, LA, MT, NV, NH, SD, TN, TX, WA, WV, WY. Excludes athletes, entertainers, public figures.'),
    ('az', 'days', 60, 'US-MULTI-017', 'Withholding starts after 60 days present (transit, personal days and unrelated training excluded) unless both agree earlier.'),
    ('ct', 'days', 15, 'US-CTP10-001', 'Above 15 days, all CT days including the first 15.'),
    ('hi', 'days', 60, 'US-HI-P5-1-002', 'Exempt if HW-6 on file, 60 days or fewer, paid from an office outside HI, regular workplace outside HI; employer files HW-7. Not for construction-contractor employees.'),
    ('id', 'amount', 1000, 'US-ID-P5-2-002', 'No withholding for a nonresident earning under 1,000 USD in Idaho in the calendar year.'),
    ('il', 'days', 30, 'US-MULTIS5-023', 'No withholding for a nonresident with fewer than 31 days of service in IL whose service is not localized in IL (localization rules first); IL-W-6 certificate of days for nonresidents expected to work more than 30 days.'),
    ('la', 'days', 30, 'US-MULTIS5-021', 'Act 382 (2025), in force for tax periods from 2026-01-01: 30 or fewer days exempt (was 25); home-State condition repealed. LAC 61:I.1923 adopted LR 52:358, 2026-03-20 (US-LAS5-002): employer begins withholding and reports on L-1 from the period in which the 31st day fell; employee notifies within 10 days of the 31st day; exemption lost if other LA-source income.'),
    ('me', 'days', 12, 'US-ME-P5-2-003', 'Taxable only if present MORE than 12 days AND more than 3,000 USD gross Maine-source.'),
    ('mt', 'days', 30, 'US-MT-P5-1-003', 'No withholding if fewer than 30 days in MT AND work in more than one State; not for athletes, entertainers, per-event payees, construction workers, key employees.'),
    ('ne', 'days', 7, 'US-NE-P5-1-002', 'From tax years beginning 2025-01-01: NE-sourced if services in NE exceed seven days.'),
    ('nm', 'days', 15, 'US-NM-P5-2-002', 'Not required to withhold from nonresidents working in NM 15 or fewer days in the calendar year.'),
    ('ok', 'amount', 300, 'US-OKS5-010', 'Nonresident whose OK income in any calendar quarter is not more than 300 USD excluded (68 O.S. 2385.1).'),
    ('ut', 'days', 20, 'US-UT-P5-1-002', 'No UT withholding: no other UT income, 20 days or less, resident of a no-tax or similar-exclusion State; not athletes, entertainers, prominent persons.'),
    ('vt', 'days', 30, 'US-VT-P5-2-003', 'Out-of-state employers need not begin VT withholding until the employee has worked from a VT location for thirty days.'),
    ('wv', 'days', 30, 'US-MULTI-015', '30 days or less in WV, working in more than one State, not athlete/entertainer.'),
    ('ga', 'amount', 5000, 'US-GAS5-004', 'Taxable nonresident: more than 5% of wages or more than 5,000 USD attributable to GA.'),
    ('mn', 'amount', 15300, 'US-MNS5-010', 'No MN withholding if expected pay under 15,300 (2026), or MI/ND reciprocity with MWR.'),
    ('wi', 'amount', 1500, 'US-WIS5-011', 'Expected WI earnings under 1,500 (catch-up once exceeded).'),
]
for st, kind, v, rid, rule in thr:
    if kind == 'days':
        f('income_tax', f'multi.nonresident.{st}.threshold_days', v, rid, uom='days', level='withholding', note=rule)
    else:
        f('income_tax', f'multi.nonresident.{st}.threshold_amount', v, rid, cur=USD, level='withholding', note=rule)
f('income_tax', 'multi.nonresident.me.threshold_amount', 3000, 'US-ME-P5-2-003', cur=USD, level='withholding', note='Joint test with more than 12 days.')
f('income_tax', 'multi.nonresident.ga.threshold_share', 5, 'US-GAS5-004', uom='percent', level='withholding', note='More than 5% of wages attributable to GA (alternative to 5,000).')
f('income_tax', 'multi.nonresident.la.employer_start_rule', 'Begin withholding and report on Form L-1 beginning in the period in which the 31st day fell', 'US-LAS5-002', level='withholding and employer reporting',
  note='Adopted rule LR 52:358 effective 2026-03-20; supersedes the NOI row US-MULTIS5-022. Drafting inconsistency C.1.a "less than 30" vs statute "30 or fewer": statute governs.')
f('income_tax', 'multi.nonresident.ms.threshold_rule', 'Day 1 by earnings ratio, except no withholding when annual MS earnings will be below the standard deduction for the filing status', 'US-MSS5-019', level='withholding')
f('income_tax', 'multi.nonresident.nd.threshold_rule', 'Mobile workforce exclusion (57-38-59.3): present 20 days or fewer, no other ND income, home State reciprocal exclusion or no income tax; not athletes, entertainers, persons of prominence, construction workers, key employees', 'US-NDS5-004', level='withholding')
for st, rid, rule in [('ca', 'US-MULTIS5-010', 'No threshold: working-day ratio from day 1 (commission pay: volume ratio)'),
                      ('co', 'US-CO-P5-1-002', 'No threshold: apportioned by days worked in CO (a day counts if majority of working time is in CO)'),
                      ('ny', 'US-MULTIS5-013', 'No threshold: NY working days / total working days with the convenience test'),
                      ('ar', 'US-AR-P5-1-002', 'No threshold: apportioned by AR working days (HB1116 of 2025, 15 days / 2,500, died)'),
                      ('ms', 'US-MS-P5-2-002', 'Earnings ratio; principal place of employment in MS -> total wages unless the other State requires withholding')]:
    f('income_tax', f'multi.nonresident.{st}.allocation_rule', rule, rid, level='withholding')

# 2.5 convenience
f('income_tax', 'multi.convenience.ny.rule', '20 NYCRR 132.18(a): nonresident allocates by NY working days / total working days; days outside NY count only if worked of NECESSITY; home-office days are NY days unless the home is a bona fide employer office', 'US-MULTIS5-013', level='withholding and assessment')
f('income_tax', 'multi.convenience.pa.rule', '61 Pa. Code 109.8: same necessity test as NY; PA reciprocal agreements prevail', 'US-MULTIS5-014', level='withholding and assessment')
f('income_tax', 'multi.convenience.de.rule', '30 Del. C. 1124(b)(1): compensation is DE-source if attributable to employment in DE and not required to be performed elsewhere; working from home does not qualify for the PIT-SCW exclusion', 'US-DES5-004', level='assessment',
  note='Assessment-level exclusion via Form PIT-SCW (US-MULTIS5-015).')
f('income_tax', 'multi.convenience.ne.rule', 'From 2025: services performed outside NE for the nonresident\'s convenience are NE-sourced (77-2733(8)(c))', 'US-NE-P5-1-002', level='withholding and assessment')
f('income_tax', 'multi.convenience.nj.rule', 'From 2023 NJ applies the convenience rule against residents of States that apply one (DE, NE, NY; CT by reciprocal law); PA residents excluded by the reciprocal agreement', 'US-MULTI-012', level='withholding and assessment')
f('income_tax', 'multi.convenience.ct.rule', 'From tax years beginning 2019-01-01 CT applies the resident State\'s convenience test to nonresidents working for a CT employer', 'US-MULTI-020', level='assessment')
f('income_tax', 'multi.convenience.ar.rule', 'Not a convenience State: Act 1019 of 2021 (SB 484), in force from TY2021 - a nonresident works in AR only when physically located in AR', 'US-ARS5-006', level='withholding and assessment',
  note='Closes MULTI-OQ-5 from the primary text (A.1).')
f('income_tax', 'multi.convenience.default', 'Everywhere else wages follow the place of physical performance', 'US-FED-P5-1-009')

# 2.6 transport / 2.7 military spouse / 2.8 bills
f('income_tax', 'multi.transport.motor_carrier', 'Employee with regularly assigned duties in 2+ States: taxable ONLY by the residence State/subdivision (49 U.S.C. 14503)', 'US-MULTIS5-001', level='withholding')
f('income_tax', 'multi.transport.rail', 'Residence State/subdivision only (49 U.S.C. 11502)', 'US-MULTIS5-002', level='withholding')
f('income_tax', 'multi.transport.air_carrier', 'Residence State plus the State where more than 50% of carrier pay is earned (scheduled flight time) (49 U.S.C. 40116(f))', 'US-MULTIS5-003', level='withholding')
f('income_tax', 'multi.transport.air_carrier.share_threshold', 50, 'US-MULTIS5-003', uom='percent', level='withholding')
f('income_tax', 'multi.transport.seamen', 'Seamen\'s wages may not be withheld for State/local tax; multi-State vessel crew and pilots taxable only by the residence State (46 U.S.C. 11108)', 'US-MULTIS5-004', level='withholding')
f('income_tax', 'multi.military_spouse.rule', 'Spouse\'s service income not sourced to the duty State; election of the servicemember\'s residence, the spouse\'s residence or the permanent duty station (50 U.S.C. 4001); payroll effect: stop work-State withholding on the State certificate', 'US-MULTIS5-005', level='withholding')
f('live_legal_change', 'multi.mobile_workforce_bill.senate', 'S. 1443 (introduced 2025-04-10, Senate Finance): DRAFT, NOT ENACTED - do not model', 'US-MULTIS5-020', level='withholding and tax (if enacted)')
f('live_legal_change', 'multi.mobile_workforce_bill.house', 'H.R. 10271 (introduced 2026-09-03, House Judiciary): DRAFT, NOT ENACTED - do not model', 'US-MULTIS5-025', level='withholding and tax (if enacted)')

# 3 UI localization
f('social_security', 'multi.sui.localization_test', 'One State covers the entire service with one employer, in order: (1) localized (entirely in the State, or out-of-state service incidental: temporary, transitory, isolated); (2) else some service in the base-of-operations State; (3) else some service in the State of direction or control; (4) else some service in the State of residence', 'US-MULTIS5-017', vm='second independent authority',
  note='DOL OUI restatement; same test in the 2023 DOL Comparison (US-FED-P5-2-005, still the latest edition per US-MULTIS5-026) and UIPL 20-04 (US-MULTIS5-016); statutory instance Fla. Stat. 443.1216 (US-MULTI-001).', level='employer UI reporting')
f('social_security', 'multi.sui.localization.telecommuting', 'UIPL 20-04 (2004, continuing) reissues the UIPL 291 interpretation with telecommuting examples', 'US-MULTIS5-016', level='employer UI reporting')
f('social_security', 'multi.sui.reciprocal_coverage_election', 'Where no test resolves the case, employer, employee and States may elect coverage of all service in one State (performance, residence or place of business); CA CUIC 602/603', 'US-MULTIS5-010', level='employer UI reporting')
f('social_security', 'multi.futa.wage_base.scope', 'FUTA 7,000 counts remuneration paid by the employer in the calendar year across all States: one base per employer, not per State; successor carry-over', 'US-MULTIS5-009')
f('social_security', 'multi.sui.employee_contribution_states', 'AK, NJ, PA (only three States levy employee UI contributions; take 2026 rates from the State annexes)', 'US-FED-P5-2-006')

# SUI other-state wage credit per State
yes = [('ak', 'US-AKS5-005', 'Transfer to AK within the same company: credit for other-state taxable wages in the same calendar year; TQ01C item 9 flag (US-AKS5-013).'),
       ('al', 'US-ALS5-009', '25-4-16(b)(1).'), ('ca', 'US-MULTIS5-010', 'CUIC 930.1: on transfer to CA in the same year.'),
       ('ct', 'US-CTS5-016', '31-222(b)(1)(A).'), ('de', 'US-DES5-010', '3302(28)(A)(x).'), ('fl', 'US-FLS5-020', 'Out-of-state wages credited via form RT-6NF.'),
       ('hi', 'US-HIS5-012', 'DLIR handbook: wages reported to another State may be combined with Hawaii wages.'),
       ('ks', 'US-KSS5-020', '44-703(o)(2)(C)(i).'), ('ky', 'US-KYS5-018', 'KRS 341.030(7)(a).'),
       ('me', 'US-MES5-020', '26 MRSA 1043(19): same legal entity in any other State.'), ('mi', 'US-MIS5-010', 'MCL 421.44.'),
       ('ms', 'US-MSS5-011', '71-5-353(4).'), ('nc', 'US-NCS5-015', 'G.S. 96-9.3: wages paid in another State with contributions there.'),
       ('nd', 'US-NDS5-009', '52-04-03(1); same employer.'), ('ne', 'US-NES5-011', '48-648.02.'),
       ('nh', 'US-NHS5-007', '282-A:69 I.'), ('nv', 'US-NVS5-006', 'NRS 612.545(2)(b): where that State\'s contributions were required.'),
       ('ok', 'US-OKS5-005', '40 O.S. 1-201(48).'), ('or', 'US-ORS5-015', 'ORS 657.095(2): same Oregon employer, proof prescribed by OED.'),
       ('ri', 'US-RIS5-013', '28-42-3.'), ('sc', 'US-SCS5-014', '41-27-380(B).'), ('sd', 'US-SDS5-002', '61-1-46.'),
       ('vt', 'US-VTS5-010', '21 V.S.A. 1321(b)(2).'), ('wv', 'US-WVS5-001', 'SB 841 (2024): where contributions were required and paid.'),
       ('wy', 'US-WYS5-003', '27-3-102(a)(xviii)(A).')]
for st, rid, note in yes:
    f('social_security', f'multi.sui.other_state_wage_credit.{st}', True, rid, level='employer UI reporting', note='Wages the same employer already paid under another State\'s UI law in the same calendar year count toward this State\'s taxable wage base. ' + note)
f('social_security', 'multi.sui.other_state_wage_credit.id', 'conditional: only if tax was paid on them to that State (72-1349(1))', 'US-IDS5-021', conf='medium', level='employer UI reporting', note='A.3 handbook; statute text not read.')
f('social_security', 'multi.sui.other_state_wage_credit.ia', False, 'US-IAS5-024', level='employer UI reporting', note='871 IAC 23.6(3): only wages reported to Iowa count; successor with experience transfer excepted.')
f('social_security', 'multi.sui.other_state_wage_credit.mt', False, 'US-MTS5-025', level='employer UI reporting', note='DLI handbook: wages reported to other States may not be used to reach the MT base.')

# PFML/TDI coverage
for st, rid, rule in [
    ('wa', 'US-MULTIS5-024', 'Follows the UI localization test (RCW 50A.05.010(8))'),
    ('ct', 'US-CTS5-035', 'Follows UI localization: employees for whom CT UI and payroll taxes are paid are working in CT'),
    ('me', 'US-MES5-025', 'Follows the Maine UI localization test (FAQ 6)'),
    ('or', 'US-ORS5-014', 'Follows UI localization (ORS 657B.175); employer size counts out-of-state employees too (US-ORS5-013)'),
    ('md', 'US-MDS5-019', 'FAMLI covers employees in positions localized in MD (LE 8-202 UI localization); contributions start 2027-01-01 (US-MDS5-014)'),
    ('ri', 'US-RIS5-016', 'TDI follows the UI localization test (28-39-2 uses the chapter 42 definition)'),
    ('dc', 'US-DCS5-007', 'More than 50% of work time in DC, or DC-based with substantial DC time and not more than 50% elsewhere; not by residence'),
    ('de', 'US-DES5-012', 'Follows the primary DE worksite (3701(6)a), not UI localization')]:
    f('social_security', f'multi.pfml.coverage_test.{st}', rule, rid, level='employer withholding and reporting')
f('social_security', 'multi.pfml.coverage_test.default', 'Key the PFML/SDI premium State to sui_state unless the State annex proves otherwise (WA, CT, ME, OR, MD, RI proven; DC and DE differ)', 'US-MULTIS5-024')

# 4 payslip reach
f('payslip_statute', 'multi.ca.ward.rule', 'Ward v. United Airlines, Cal. S. Ct. S248702 (2020-06-29), Lab. Code 226: applies if the PRINCIPAL place of work is in CA (majority of working time); with no majority State, where CA is the base of work operations and some work is done in CA. Employer location, residence, place of pay receipt, taxes paid and a CBA are irrelevant.',
  'US-MULTIS5-018', level='employer pay-statement output', note='STATUS: in force.')
f('payslip_statute', 'multi.payslip.reach.default', 'Default: the pay-statement statute of the work-location State (no other State reach rule researched); payslip in English (US-OWN-006)', 'US-MULTIS5-018')

# 5 reporting
f('reporting', 'multi.w2.states_per_form', 2, 'US-MULTIS5-011', uom='count', note='Boxes 15-20 carry up to TWO States and TWO localities; for more, a second W-2 repeating boxes a-f, never duplicating federal data on Copy A; W-3 box 15 = X when more than one State.', level='employer reporting')
f('reporting', 'multi.newhire.designated_state', 'A multistate employer reporting electronically may send all new-hire reports to ONE designated State in which it has employees, after notifying HHS in writing', 'US-MULTIS5-006', level='employer reporting')
f('reporting', 'multi.ui_wage_report.routing', 'UI quarterly wage report to the sui_state only (localization); State income-tax withholding returns to every State where withholding applies', 'US-MULTIS5-017', level='employer reporting')

# 9 IWO
f('deductions_garnishments', 'multi.iwo.governing_law', 'Interstate IWO: apply the income-withholding law of the State of the obligor\'s PRINCIPAL PLACE OF EMPLOYMENT for the employer fee, the maximum withheld, timing, priority among obligees and terms not in the order', 'US-MULTIS5-007', level='employer withholding')
f('deductions_garnishments', 'multi.iwo.remittance_business_days', 7, 'US-MULTIS5-007', uom='days', note='Remit to the SDU within 7 business days.', level='employer withholding')

# unresolved
u('multi.nonresident.la.catch_up_rule', 'Act 382 says from day 31 every LA day incl. the first 30 is taxable, but LAC 61:I.1923 only says begin withholding in the period of the 31st day; how days 1-30 are caught up is not stated (LA-OQ-1).',
  'The codified R.S. 47:112.2(A) text, or an LDR RIB/FAQ on the mobile workforce exemption.', [], False, ['US-MULTIS5-021', 'US-LAS5-002'])
unk_open = {'co': 'C.R.S. 8-76-102 (chargeable wages) or the CDLE Employer Handbook (CO-OQ-1)',
            'dc': '7 DCMR chapter 3 or the DOES UI Employer Handbook (51-103(e)(6) as read is silent)',
            'la': 'R.S. 23:1536 read via Wayback (LA-OQ-10)',
            'mo': 'In-force RSMo 288.036 or the DES MODES-4-5 instructions (MO-OQ-2)',
            'nm': 'NMSA 51-1-11 and 51-1-42 or 11.3.300 NMAC',
            'ut': 'Utah Code 35A-4-303 current text or the DWS Employer Handbook, Contributions chapter (UT-OQ-3)',
            'md': 'LE Title 8 taxable-wage definition (the BEACON optional field "Out of State taxable wages" implies yes, US-MDS5-017, but is a file spec, not a rule)'}
for st, close in unk_open.items():
    u(f'multi.sui.other_state_wage_credit.{st}', 'The State unit searched but did not reach the statute or rule that decides whether other-State UI wages count toward the base.', close, [], False)
u('multi.sui.other_state_wage_credit.ar', 'The AR unit reports a credit on permanent transfer with the same employer (handbook example: MO wages 6,000 in Q1, only 1,000 AR-taxable in Q2), but the cited active row US-ARP9V-001 (same handbook) does not carry that clause in figure_or_rule_carried, so no fact can cite it.',
  'The merge worker appends the transfer-credit clause to US-ARP9V-001 (or registers the handbook page that states it); then emit True with that register_id.', [], False, ['US-ARP9V-001'])
not_asked = ['az', 'ga', 'il', 'in', 'ma', 'mn', 'nj', 'ny', 'oh', 'pa', 'tn', 'tx', 'va', 'wa', 'wi']
for st in not_asked:
    u(f'multi.sui.other_state_wage_credit.{st}', 'Not answered in the Stage-5 State unit (no MULTI hand-off section; the SUI base is given but the other-State wage credit is not stated).',
      f'The {st.upper()} UI taxable-wage statute/definition (State annex), or the DOL "Significant Provisions of State UI Laws" 2026 line for {st.upper()}.', [], False)
for st in ['ca', 'nj', 'ny', 'ma', 'co', 'mn', 'vt', 'hi']:
    u(f'multi.pfml.coverage_test.{st}', 'PFML/SDI/TDI coverage definition for multistate workers not read in the State unit (CO and HI: source unreachable; others not addressed).',
      f'The {st.upper()} programme coverage definition (statute or agency rule); until then key the premium to sui_state.', [], False)
u('multi.paid_sick_leave.multistate_scope', 'Paid-sick-leave coverage of employees working partly in a State is answered only in some units (NE 80 h in NE per year US-NES5-009; DC at least 50% of time US-DCS5-024; ME follows UI US-MES5-008; CO, CT, MD, NM, NV, OR, RI, VT: no threshold stated or open).',
  'Per-State PSL statutes/regulations and agency FAQs (State annexes).', [], False)
u('multi.newhire.multistate_registration_channel', 'HHS/OCSS multistate employer registration form/portal not reachable (acf.hhs.gov HTTP 202 empty body; Wayback 404).',
  'A browser read of the ACF multistate employer registration page.', ['https://www.acf.hhs.gov/css/form/multistate-employer-registration-form (202 empty)'], False, ['US-MULTIS5-006'])
u('multi.convenience.ny.litigation_status', 'Live litigation status of the NY convenience rule was not swept.', 'NY DTF / Tax Appeals Tribunal decisions list for 2026.', [], False, ['US-MULTIS5-013'])
u('multi.payslip.reach.other_states', 'Pay-statement reach rules outside CA (e.g. NY, IL) for remote employees not researched; State units mostly found no territorial clause.', 'Per-State pay-statement statute reach (State annexes) or agency guidance.', [], False)
u('multi.ca.minimum_wage.nonresident_reach', 'Oman left the CA minimum-wage reach for nonresidents working episodically in CA undecided.', 'A later CA appellate ruling or DLSE guidance on minimum-wage reach.', [], False, ['US-MULTIS5-019'])
u('multi.nonresident.sc.threshold', 'SC nonresident threshold: MULTI.md cites the IRC 151(d) amount (US-MQ-60) while US-SCR3-001 reads 12-8-520(A) as a 1,000 USD expected-wages test; no single active row states the nonresident threshold.', 'The SC annex reconciles 12-8-520(A) with the SC DOR withholding guide (WH-1603F / WH105).', [], False, ['US-SCR3-001', 'US-SCR3-003'])

out = os.path.join(BASE, '_research', 'CCG-annex_MULTI-facts.json')
P.dump(out, {'_jurisdiction': 'Multistate routing layer (work_location_jurisdiction, residence_jurisdiction, sui_state)',
             '_key_convention': 'Keys are prefixed multi. ; State-specific routing facts carry the lowercase State code after the concept (multi.reciprocity.{st}.partners) so they do not collide with the State annexes ({jur}.*).',
             '_produced_by': 'Synthesis-B worker CCG annexes FED+MULTI, from _research/stage5/MULTI.md, the MULTI hand-off sections of the 51 State findings files and active/partial register rows only (no fetching)'})
json.dump({'ids': sorted(P.ids), 'warnings': P.warnings, 'n_facts': P.n_good, 'n_pending': P.n_bad, 'n_unres': len(P.unresolved)},
          open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'multi_meta.json'), 'w'), indent=1)
print(len(P.facts), P.n_good, P.n_bad, len(P.unresolved), len(P.ids)); print('\n'.join(P.warnings))
