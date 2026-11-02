"""Chad design v5 — generator and executable validation.

Builds chad-design-blueprint-claude-v5/SKILL.md from the regulation data below and runs the
regulations, as written, on the 12 scenarios (10 of v4 + 11 non-resident + 12 family allowance with
6 children) and on 20 extra checks of the v5 changes. Expected values are hand-computed from the law
(CGI 2026, DGI edition; CNPS decrees 1635/1636 of 2009 and the CNPS employer guide 2019) and written
below; they are NOT produced by this engine.
Run:  python -I _build_v5.py   (writes SKILL.md and VALIDATION-run.txt, prints the table)

Base: _build_v4.py (2026-10-29-design-v4, not changed). Changes: CHANGELOG.md of the blueprint.
Round 2 (2026-11-01): decisions of LEI-VEREDITOS.md "Revisao 2026-11-01 (b)" applied (CNPS, non-resident on the
scale, leave ticket / per diem, 6274x / 6580x, IRPP rounding as technical convention).
Round 3 (2026-11-01, after QA-REVIEW.md): band limits at the round figure, TFE paid to the franc (technical convention),
Art. 3-4 IRPP exemption (age, real regime, workers), WTC V3.0 intermediate accounts reused, TAFP base per Art. 173,
6251x in the transport exemption, technical decisions of the front on transport/CNPS and 62867 (pending the user’s ok).
Round 4 (after QA round 2): Art. 3-4° needs a start date (58205 > 0); worker under 35 at recruitment (restrictive reading);
labels of the two decisions corrected (front, not user); D2/R28 reference.
"""
import math, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'chad-design-blueprint-claude-v5')
CNPS_SRC = "Dec. 1635/PR/PM/MFPT/2009 arts. 1–4, Dec. 1636/PR/PM/MFPT/2009 arts. 1–3, Dec. 1634/2009 (AT/MP; text not obtained, rate from the guide p. 8), effective date 2009-12-04 per the guide p. 8 (Journal Officiel not obtained); CNPS Guide de l'employeur 2019, p. 6–9 and 12"

# ---------------------------------------------------------------- statutory parameters
# CNPS (decided, round 2): PFM 7.5% ER (Dec. 1635), PVID 5% ER + 3.5% EE (Dec. 1636), AT/MP 4% ER (Dec. 1634, via guide p. 8), from 2009-12-04 (guide p. 8);
# ceiling 500,000 a month = 6,000,000 a year, same for the 3 branches (Dec. 1635 art. 4, Dec. 1636 art. 3);
# floor = SMIG 59,995 rounded to 60,000 a month (Dec. 1111/2011; guide p. 7 and 9), only in a month with pay.
CNPS = dict(pvid_ee=3.5, pvid_er=5, pfm_er=7.5, atmp_er=4, floor_m=60000, ceil_m=500000, total=20)

# ---------------------------------------------------------------- flags
FLAGS = [
    ('58218', 'Status (global flag)',
     "IF(EQUALS($hr.residency_status::key;'NRES');1;IF(EQUALS($hr.residency_status::key;'DISABLED');2;IF(EQUALS($hr.residency_status::key;'YOUNG-GRAD');3;IF(EQUALS($hr.residency_status::key;'DIPLO');4;0))))",
     '0 resident · 1 non-resident · 2 disabled (CGI Art. 45-18°) · 3 young graduate (Art. 3-4°) · 4 diplomatic (Art. 3-2°) — catalogue numbering; routing uses `LESS($58218;1)` for residents, never an equality test against zero'),
    ('58202', 'CNPS PVID eligible', "IF(EQUALS($hr.cnps_eligibility_pvid::key;'N');2;1)",
     '1 yes (default, every employee, **non-residents included**: « quelle que soit… leur nationalité », CNPS guide p. 6) · 2 no — only a seconded employee covered by a bilateral or multilateral convention (CIPRES) with a secondment certificate'),
    ('58203', 'CNPS PFM eligible', "IF(EQUALS($hr.cnps_eligibility_pfm::key;'N');2;1)", '1 yes (default) · 2 no — as 58202'),
    ('58204', 'CNPS AT/MP eligible', "IF(EQUALS($hr.cnps_eligibility_atmp::key;'N');2;1)", '1 yes (default) · 2 no — as 58202'),
    ('58205', 'Art. 3-4° exemption months (young graduate / worker)',
     'ADD(FLOOR(DIVIDE(DAYS_BETWEEN($hr.young_graduate_employee_exemption_start_date;$period.end_date);30.4375));1)',
     'months since the Art. 3-4° exemption start (date of recruitment by the real-regime entity), current month included; IRPP exemption while ≤ 60 (« pendant une période de cinq ans »). The same DD date is used for workers. WTC V3.0 names 58205 "Young Graduate Start Date" but its formula (and the Dev) also yields months; read by the IRPP-TS report'),
    ('58206', 'TFE / TAFP relief (entity)',
     "IF(EQUALS($legal_entity_hr.tfe_tafp_relief::key;'100');1;IF(EQUALS($legal_entity_hr.tfe_tafp_relief::key;'50');2;0))",
     '0 none · 1 exempt (LF 2020 Art. 14 as amended by LF 2024 Art. 6 / LF 2026 Art. 6) · 2 50% (CGI Art. 158) — **entity field**'),
    ('58207', 'Transport allowance granted to all staff', "IF(EQUALS($legal_entity_hr.transport_uniform::key;'Y');1;2)", '1 yes · 2 no — **entity field**, default 1 (Art. 45-13°)'),
    ('58210', 'Plan social (collective redundancy)', "IF(EQUALS($hr.termination_plan_social::key;'Y');1;2)", '1 yes · 2 no — **DD field** (Art. 45-10°)'),
    ('58212', 'Dependent children', '$hr.number_of_dependent_children',
     'count of **children** (not dependants) — DAS report and the Art. 45-4° cap (5,000 XAF per child per month)'),
    ('58213', 'CNPS family allowance received (monthly)', '$hr.cnps_family_allowance_monthly',
     'XAF a month paid by the CNPS for the children — **new DD field**, default 0. Art. 45-4°: imputed on the 5,000 XAF per-child cap'),
    ('58215', 'Entity under the real regime (régime du réel)', "IF(EQUALS($legal_entity_hr.tax_regime::key;'REEL');1;2)",
     '1 yes · 2 no — **new entity field**, default 1. Condition of Art. 188-10° and Art. 174-3°'),
    ('58216', 'Employee age (years)', 'FLOOR(DIVIDE(DAYS_BETWEEN($hr.date_of_birth;$period.end_date);365.25))',
     'completed years at period end — `under 35` test of Art. 188-10° and Art. 174-3° (TF/TA, read each month)'),
    ('58225', 'Age at the Art. 3-4° exemption start', 'FLOOR(DIVIDE(DAYS_BETWEEN($hr.date_of_birth;$hr.young_graduate_employee_exemption_start_date);365.25))',
     'completed years at recruitment — `under 35` test of the young graduate in Art. 3-4° (IRPP), checked at recruitment because the exemption then runs five years (A27)'),
    ('58217', 'Worker (ouvrier)', "IF(EQUALS($hr.worker_category::key;'OUVRIER');1;2)", '1 yes · 2 no — **new DD field**, default 2'),
    ('58219', 'TFE / TAFP exempt payroll share (youth, disabled, workers)',
     'IF(AND(EQUALS($58215;1);OR(EQUALS($58218;2);AND(EQUALS($58218;3);LESS($58216;35));AND(EQUALS($58217;1);LESS($58216;35))));1;0)',
     '1 = the pay of this employee is outside TFE and TAFP: real-regime entity and (disabled, or young graduate under 35, or worker under 35). Art. 188-10° (TF) and Art. 174-3° (TA), CGI 2026 p. 59–61 — no five-year limit in these articles'),
    ('58226', 'Art. 3-4° IRPP exempt (derived)',
     'IF(AND(EQUALS($58215;1);GREATER($58205;0);LESS($58205;61);LESS($58225;35);OR(EQUALS($58218;3);EQUALS($58217;1)));1;0)',
     '1 = IRPP exempt: CGI Art. 3-4° (p. 15) « Les salaires versés aux jeunes diplômés âgés de moins de 35 ans et aux ouvriers recrutés par les entreprises du régime du réel… pendant une période de cinq ans » — real-regime entity (58215), start date given and within 60 months (0 < 58205 ≤ 60; **the start date is mandatory in the DD when 58218 = 3 or 58217 = 1** — without it there is no exemption), under 35 at recruitment (58225), and young graduate (58218 = 3) or worker (58217 = 1). Round 4: the under-35 limit is applied to workers too — technical decision of the front, 60% (A34): Art. 3-4° attaches the age to « jeunes diplômés » only, but does not expressly set it aside for « ouvriers », and Arts. 188-10° / 174-3° of the same policy (LFI 2021) say « les ouvriers âgés de moins de 35 ans »'),
    ('58223', 'Leave travel ticket — annual limit', '$hr.leave_ticket_annual_limit',
     'XAF a year: one ticket a year per person (employee, spouse, dependants) at the normal fare from the place of work to the place of origin — **new DD field**, default 0. CGI Art. 45-15°'),
]
DERIVED = ['58219', '58226']   # flags computed from other flags inside the run

NOT_DIPLO = 'NOT(EQUALS($58218;4))'
SCALE = 'AND(OR(LESS($58218;2);EQUALS($58218;3));NOT(EQUALS($58226;1)))'       # resident, non-resident, young graduate — unless Art. 3-4° exempt
RESIDENT_SCALE = 'AND(OR(LESS($58218;1);EQUALS($58218;3));NOT(EQUALS($58226;1)))'
NR = 'EQUALS($58218;1)'
NR_SCALE = 'AND(EQUALS($58218;1);NOT(EQUALS($58226;1)))'
TFE_POP = 'AND(NOT(EQUALS($58218;4));NOT(EQUALS($58219;1)))'
R_IRPP = 'FLOOR(ADD($band_amount_raw;0.5))'
R_CNPS = 'FLOOR(ADD($band_amount_raw;0.5))'

# ---------------------------------------------------------------- matrices (code by code against the WTC)
CASH_GROSS = [('62104', '', 'No'), ('62560', '', 'No'), ('62561', '', 'No'), ('62562', '', 'No'), ('62563', '', 'No'),
              ('65579', '6557%', 'Yes'), ('65589', '6558%', 'Yes'),
              ('62199', '621%%', 'Yes'), ('62299', '622%%', 'Yes'), ('62399', '623%%', 'Yes'), ('62499', '624%%', 'Yes'), ('62599', '625%%', 'Yes'),
              ('62639', '6263%', 'Yes'), ('62650', '', 'Yes'), ('62669', '6266%', 'Yes'), ('62799', '627%%', 'Yes'), ('62869', '6286%', 'Yes'),
              ('62879', '6287%', 'Yes'), ('62889', '6288%', 'Yes'), ('62890', '', 'Yes'), ('62999', '629%%', 'Yes'), ('65519', '6551%', 'Yes'),
              ('65619', '6561%', 'Yes'), ('65669', '6566%', 'Yes'), ('65799', '657%%', 'Yes'), ('79499', '794%%', 'Yes')]
BIK_REAL = [('65610', '', 'No'), ('65611', '', 'No'), ('65612', '', 'No'), ('65660', '', 'No'), ('65661', '', 'No'), ('65662', '', 'No'),
            ('62670', '', 'Yes'), ('62680', '', 'Yes'), ('65299', '652%%', 'Yes'), ('65499', '654%%', 'Yes'), ('65509', '6550%', 'Yes'),
            ('65520', '', 'Yes'), ('65699', '656%%', 'Yes'), ('65899', '658%%', 'Yes')]
TFE_BASE = [('62104', '', 'No'), ('62180', '', 'No'), ('62181', '', 'No'), ('62182', '', 'No'), ('62649', '6264%', 'Yes')] + CASH_GROSS[1:] + BIK_REAL
# TAFP: Art. 173 — « y compris les gratifications servies régulièrement »: one-time / discretionary bonuses 6222x out; pensions 6264x not listed
TAFP_BASE = [m for m in TFE_BASE if m[1] != '6264%'] + [('62229', '6222%', 'No')]
CNPS_GROSS = [(a, '', 'No') for a in ['62104', '62180', '62181', '62182', '62540', '62541', '62542', '62550', '62551', '62552', '62560', '62561',
                                      '62562', '62563', '62570', '62900', '62910', '62920', '62930', '65570', '65571', '65572',
                                      '65580', '65581', '65582']] + \
             [('62519', '6251%', 'No'), ('62529', '6252%', 'No'), ('62759', '6275%', 'No'), ('62769', '6276%', 'No'), ('62789', '6278%', 'No'),
              ('62869', '6286%', 'Yes'), ('62879', '6287%', 'No'), ('65669', '6566%', 'No')] + \
             [('62199', '621%%', 'Yes'), ('62299', '622%%', 'Yes'), ('62399', '623%%', 'Yes'), ('62499', '624%%', 'Yes'), ('62599', '625%%', 'Yes'),
              ('62639', '6263%', 'Yes'), ('62650', '', 'Yes'), ('62669', '6266%', 'Yes'), ('62670', '', 'Yes'), ('62680', '', 'Yes'),
              ('62799', '627%%', 'Yes'), ('62890', '', 'Yes'), ('62999', '629%%', 'Yes'), ('65299', '652%%', 'Yes'),
              ('65499', '654%%', 'Yes'), ('65599', '655%%', 'Yes'), ('65699', '656%%', 'Yes'), ('65799', '657%%', 'Yes'), ('65899', '658%%', 'Yes'),
              ('79499', '794%%', 'Yes')]
FAMILY = [('62759', '6275%', 'Yes'), ('62769', '6276%', 'Yes'), ('62789', '6278%', 'Yes'), ('62866', '', 'Yes')]
FUNCTION_ALLOWANCE = [('62879', '6287%', 'Yes'), ('62570', '', 'Yes'), ('65579', '6557%', 'Yes'), ('65589', '6558%', 'Yes')]
LEAVE_TICKET = [('62559', '6255%', 'Yes')]

# BIK: (account, name, limit account, rate %, monthly cap or None, matrix)
BIK = [
    ('58120', 'Housing', '58161', 20, None, [('65499', '654%%', 'Yes')]),
    ('58121', 'Vehicle', '58162', 10, None, [('65509', '6550%', 'Yes'), ('65520', '', 'Yes')]),
    ('58122', 'Food', '58163', 15, 75000, [('65659', '6565%', 'Yes'), ('65679', '6567%', 'Yes')]),
    ('58123', 'Interior Furnishings', '58164', 5, None, [('65853', '', 'Yes')]),
    ('58124', 'Domestic Help / Security', '58165', 4, None, [('65854', '', 'Yes')]),
    ('58125', 'Electricity', '58166', 4, None, [('65855', '', 'Yes')]),
    ('58126', 'Water', '58167', 4, None, [('65856', '', 'Yes')]),
    ('58127', 'Telephone', '58168', 3, None, [('65609', '6560%', 'Yes'), ('65620', '', 'Yes')]),
    ('58128', 'Gas', '58169', 2, None, [('65857', '', 'Yes')]),
]


def band(**k):
    b = dict(f='', t='', ee='', er='', floor='', ceil='', credit='', formula='', assertion='', ceilacc='', deb='', cred='99999')
    b.update(k)
    return b


R = []  # regulations


def reg(rid, name, trg, ttype, pre, bands, matrix, note, group='Income Tax'):
    R.append(dict(id=rid, ord=rid - 9148000, name=name, trg=trg, ttype=ttype, pre=pre, bands=bands, matrix=matrix, note=note, group=group))


reg(9148011, 'TD Base Salary', 'simple_tax', 'Flat', '', [band(ee=100, deb='58109')],
    [('62100', '', 'Yes'), ('62101', '', 'Yes'), ('62102', '', 'Yes'), ('62103', '', 'Yes'), ('62109', '', 'Yes')],
    'Basic salary series 6210 (62104 rate flag, 62105 and 62108 Historic Pay excluded). Measure for the 30% transport limit and the 3.5% retirement limit.')
reg(9148012, 'TD Cash Gross', 'simple_tax', 'Flat', '', [band(ee=100, deb='58105')], CASH_GROSS,
    'Cash earnings subject to IRPP (CGI Art. 44-I, Art. 46-I); base of the Art. 46 caps and of the Art. 45-2° 15% limit. v5: the whole 6286x series is in (meal/food 62860–62865, birth 62866, death 62867, gift 62868–62869; WTC V3.0) — Art. 45 exempts none of them, Art. 44-I includes « gratifications ». 62866 is then relieved by the Art. 45-4° cap (9148022). Round 2: leave travel ticket 6255x and per diem 62570 / 6557x / 6558x are in (relieved by 9148025 and 9148024); relocation 2 (6256x, reimbursement) stays out. 6274x schooling allowance taxable (627%%). '
    '62867 (death allowance) is taxable (technical decision of the Chade front (source: WTC V3.0 code name "Death allowance" read as an employer allowance, not the « capital décès » of Art. 45-11°), pending the user’s ok; alternative and its effect in ASSUMPTIONS D2 / RESEARCH_GAPS R28). Pensions 6264x out (Art. 45-1°). **58105 is the account the DAS report reads.**')
reg(9148013, 'TD Annual Reporting Limit', 'retro_simple_tax_monthly', 'Flat', '', [band(ee=100, floor=60000, ceil=60000, deb='58106')],
    [('58105', '', 'Yes')],
    'Fixed 60,000 XAF a month (Floor = Ceiling, `_monthly`), written only when the employee has cash gross. Read by the DAS report to split employees above / at or below 60,000 XAF. Reporting parameter, not a statutory value.')
reg(9148014, 'TD Limits on Base Salary', 'retro_simple_tax', 'Flat', '',
    [band(ee=30, deb='58103'), band(ee=3.5, deb='58172')], [('58109', '', 'Yes')],
    'Derived limits in their own regulation, applied downstream as ceiling accounts: 58103 = 30% of base salary (CGI Art. 45-13°, transport; WTC V3.0 account "TD Transport Allowance Exemption") · 58172 = 3.5% of the appointments (CGI Art. 47-I, retirement).')
reg(9148015, 'TD Limits on Cash Remuneration', 'retro_simple_tax', 'Flat', '',
    [band(ee=b[3], ceil=(b[4] * 12 if b[4] else ''), deb=b[2]) for b in BIK] + [band(ee=15, deb='58173')], [('58105', '', 'Yes')],
    'Bands 1–9: CGI Art. 46-III caps, one band per benefit, on the cash remuneration 58105 (Art. 46-I/II): housing 20 · vehicle 10 · food 15 (and 75,000 XAF a month, stated annually as the band ceiling) · furnishings 5 · domestic 4 · electricity 4 · water 4 · telephone 3 · gas 2. '
    '**Band 10 (v5): 58173 = 15% of the cash remuneration**, CGI Art. 45-2° (« 15 % calculé sur la masse globale des salaires et desdites allocations »; 58105 already contains the allowance). Read as ceiling accounts by 9148024 and 9148031–9148039.')
reg(9148016, 'TD Family Allowance Exemption Limit', 'simple_tax', 'Formula', NOT_DIPLO,
    [band(ee=100, formula='MAX(ADD(MULTIPLY(5000;$58212);MULTIPLY(-1;$58213));0)', deb='58107')], FAMILY,
    'v5, structure taken from the Dev (limit in its own regulation, matrix = the family codes, so it only matters when a family allowance is paid; account 58107 as in WTC V3.0). Scope: the cap is written for « l\'employeur autre que l\'État, les Communes ou les organismes para administratifs » — every Mercans client entity is private, so it is applied to all (A29). '
    'CGI Art. 45-4° (CGI 2026 p. 29; LF 2026 Art. 8, p. 15): the allowances paid by an employer other than the State « ne peut excéder mensuellement par enfant la somme de 5.000 Francs sur laquelle viennent… s\'imputer les allocations versées par la CNPS ». Limit = max(0; 5,000 × children (58212) − CNPS family allowance (58213)). Monthly amount, no period division.')
reg(9148021, 'TD Transport Allowance — Exempt Portion', 'retro_simple_tax', 'Flat', '',
    [band(ee=100, ceilacc='58103', assertion='EQUALS($58207;1)', deb='99999', cred='58104')], [('62519', '6251%', 'Yes'), ('62529', '6252%', 'Yes')],
    'CGI Art. 45-13°: exempt up to 30% of base salary when granted to all staff (58207). Round 3: 6251x "Car & Transportation allowance" and 6252x "Transportation allowance" share the one 30% limit (58103, ceiling account) — both are transport, as in the CNPS base where both are out. Negative in 58104; subtracts in the IRPP taxable base only (not in TFE/TAFP, Arts. 173 and 189). v5 round 2: no longer used in the CNPS base — the whole transport allowance is outside CNPS (9148051). 58104 is read by the DAS report.')
reg(9148022, 'TD Family Allowance — Exempt Portion', 'retro_simple_tax', 'Flat', '',
    [band(ee=100, ceilacc='58107', deb='99999', cred='58108')], FAMILY,
    'v5: CGI Art. 45-4° — exempt only up to the limit 58107 (5,000 XAF per child per month, less the CNPS allowance); the excess is taxable IRPP. v4 exempted the whole amount on the basis of `correcoes.md` 2026-07-07, which the Art. 45-4° text contradicts. Codes: 6275x, 6276x (Family allowance, WTC V3.0), 6278x (Family allowance), 62866 (Birth allowance: « allocation d\'assistance à famille »). Negative in 58108, read by the DAS report. Still in the TFE/TAFP base (Art. 189-1° « allocations »).')
reg(9148023, 'TD Plan-Social Severance — Exempt Portion', 'simple_tax', 'Flat', 'EQUALS($58210;1)', [band(ee=100, deb='99999', cred='58113')],
    [('62189', '6218%', 'Yes')], 'CGI Art. 45-10°: severance under a collective-redundancy plan is fully exempt. Individual severance stays taxable (Art. 44-I). Negative in 58113.')
reg(9148024, 'TD Function Expense Allowance — Exempt Portion (15%)', 'retro_simple_tax', 'Flat', '',
    [band(ee=100, ceilacc='58173', deb='99999', cred='58114')], FUNCTION_ALLOWANCE,
    'v5, new. CGI Art. 45-2° (CGI 2026 p. 29): « allocations spéciales destinées à couvrir les frais inhérents à la fonction ou à l\'emploi et effectivement utilisées conformément à leur objet » exempt while they do not exceed 15% of salaries plus those allowances. Exempt = MIN(allowances; 58173), one cap shared by all the codes in the matrix. Negative in 58114; subtracts in the IRPP base only (TFE/TAFP: Art. 189-1° « indemnités diverses, allocations », no carve-out; CNPS: outside, 9148051). '
    'Codes (round 2, decision of 1 Nov on Art. 45-2°): per diem allowance 62570 and per diem benefit 6557x / 6558x (fixed amounts, no receipts) and 6287x "Function expense allowance (Art. 45-2°)" — **6287x not in WTC V3.0**, to be created (R15). A reimbursement of real expenses with receipts is not income (Art. 44-I) and must be paid on a code outside every base (as relocation 2, 6256x). No 30% professional-expense deduction exists for salaries (Art. 47 allows only compulsory pension and social security) and none is built.')
reg(9148025, 'TD Leave Travel Ticket — Exempt Portion', 'retro_simple_tax', 'Flat', '',
    [band(ee=100, ceilacc='58223', deb='99999', cred='58115')], LEAVE_TICKET,
    'v5 round 2, new. CGI Art. 45-15° (p. 30): « frais de voyage pour congé réellement exposés… dans la limite de la valeur d\'un billet par an et par personne au tarif normal du lieu de travail au lieu d\'origine ». Travel ticket allowance 6255x is now in the cash gross (IRPP) and the TFE/TAFP base; the exempt part = MIN(amount; 58223, the annual ticket limit from the DD) goes negative to 58115 and leaves the IRPP base only. CNPS: outside (« indemnités de déplacement », guide p. 8). '
    'The limit is annual and applied per payment (A24: assumes one ticket payment a year; a YTD version needs `_ytd` on 58223 vs the year\'s 58115).')
for i, b in enumerate(BIK):
    cap = f'{b[3]}% of the cash remuneration' + (' and 75,000 XAF a month' if b[4] else '')
    reg(9148031 + i, f'TD BIK {b[1]} — Capped Value for IRPP', 'retro_simple_tax', 'Flat', '',
        [band(ee=100, ceilacc=b[2], deb=b[0])], b[5],
        f'CGI Art. 46-III: « plafonnés » — IRPP takes the real value, capped at {cap} (limit {b[2]}, ceiling account). CNPS, TFE and TAFP take the real value (Art. 189-2°, Art. 173). {b[0]} is the account the DAS report reads.')
reg(9148041, 'TD IRPP Gross', 'simple_tax', 'Flat', NOT_DIPLO, [band(ee=100, deb='58008')],
    [('58105', '', 'Yes')] + [(b[0], '', 'Yes') for b in BIK] + [(a, '', 'No') for a in ['65853', '65854', '65855', '65856', '65857']] +
    [('62670', '', 'Yes'), ('62680', '', 'Yes'), ('65299', '652%%', 'Yes'), ('65630', '', 'Yes'), ('65809', '6580%', 'No'), ('65899', '658%%', 'Yes')],
    'Cash gross plus each benefit at its capped value. Benefit codes with no Art. 46 category enter at real value. v5: **6580x School Scholarship out** (CGI Art. 45-9°, « bourses d\'enseignement ou de perfectionnement »; WTC V3.0) — it stays in the TFE/TAFP base (Art. 189-1°, Art. 173). 58008 is read by the DAS report.')
reg(9148051, 'TD CNPS Gross', 'simple_tax', 'Flat', NOT_DIPLO, [band(ee=100, deb='58130')], CNPS_GROSS,
    f'Base decided in round 2 ({CNPS_SRC}): « salaires, gains, indemnités (à l\'exception de celles ayant un caractère de remboursement de frais), primes, gratifications… et tous autres avantages versés… entre le premier et le dernier jour du mois » (guide p. 7) — benefits in kind at real value in (Dec. 1635 art. 3, « contre valeur des avantages en nature »); 6286x meal/food in; **6274x schooling allowance and 6580x scholarship in** (« tout autre avantage en espèce »). '
    'Out: family allowances 6275x/6276x/6278x (guide p. 8; Dec. 1635 art. 3), prime de panier / meal cash 6566x (guide p. 7), severance 6218x (« indemnités ayant un caractère de dédommagement », Dec. 1635 art. 3, Dec. 1636 art. 2), travel ticket, per diem, relocation 6254x–6257x, 6557x, 6558x and the 6287x function allowance (« indemnités de déplacement », reimbursement of expenses). '
    '**Transport 6251x / 6252x out in full** — technical decision of the Chade front (source: CNPS guide p. 8), pending the user’s ok (« Indemnité mensuelle de transport » among the exclusions); the decrees (Dec. 1635 art. 3, Dec. 1636 art. 2) exclude only expense reimbursements and « indemnités ayant un caractère de dédommagement » and do not name transport. The 30% limit is IRPP only. Would supersede `correcoes.md` 2026-07-07 ("excess subject to CNPS") once the user agrees. Uncapped; **58130 is the account the CNPS Récapitulatif reads**.', 'Social Security')
reg(9148052, 'TD CNPS Insurable Salary', 'retro_simple_tax_period', 'Flat', f'AND({NOT_DIPLO};GREATER($58130;0))',
    [band(ee=100, floor=CNPS['floor_m'] * 12, ceil=CNPS['ceil_m'] * 12, deb='58550', cred='99998')], [('58130', '', 'Yes')],
    f'Floor {CNPS["floor_m"]:,} a month = SMIG 59,995 rounded (Dec. 1111/PR/PM/MFPT/2011; guide p. 7 and 9), applied **only in a month with pay** — the `GREATER($58130;0)` condition (guide p. 7: contributions on what is « versé… entre le premier et le dernier jour du mois »; with an empty matrix the engine would still apply the floor). '
    f'Ceiling {CNPS["ceil_m"]:,} a month, the same for the three branches (Dec. 1635 art. 4; Dec. 1636 art. 3), stated annually ({CNPS["ceil_m"] * 12:,}). The ceiling is **annual**: « l\'employeur doit procéder à une régularisation… en fin d\'année » (guide p. 12) — December regularisation not built as a regulation (A23). `_period` + 99998: report-feeding base (Appel Mensuel, DNTS, Récapitulatif).', 'Social Security')
reg(9148053, 'TD CNPS Contributions', 'simple_tax_$$_post_formula', 'Flat', '',
    [band(ee=CNPS['pvid_ee'], formula=R_CNPS, assertion='EQUALS($58202;1)', deb='2610', cred='2551'),
     band(er=CNPS['pvid_er'], formula=R_CNPS, assertion='EQUALS($58202;1)', deb='6037', cred='2537'),
     band(er=CNPS['pfm_er'], formula=R_CNPS, assertion='EQUALS($58203;1)', deb='6020', cred='2550'),
     band(er=CNPS['atmp_er'], formula=R_CNPS, assertion='EQUALS($58204;1)', deb='6040', cred='2560'),
     band(ee=CNPS['pvid_ee'], formula=R_CNPS, assertion='EQUALS($58202;1)', deb='99999', cred='58100'),
     band(ee=100, formula=str(CNPS['total']), assertion='GREATER($58550;0)', deb='58131')],
    [('58550', '', 'Yes')],
    f'Rates from 2009-12-04: PVID {CNPS["pvid_ee"]}% EE + {CNPS["pvid_er"]}% ER (Dec. 1636 art. 1), PFM {CNPS["pfm_er"]}% ER (Dec. 1635 arts. 1–2; 0.25% of it passed by the CNPS to ONAPE, no extra rate), AT/MP {CNPS["atmp_er"]}% ER, single rate (Dec. 1634/2009; guide p. 8); total {CNPS["total"]}%. Each band gated by its eligibility flag; **non-residents pay every branch** (flags default 1; guide p. 6). '
    'Accounts: **employee share → 2610 / 2551** (WTC V3.0: 2551 "TD CNPS Contribution EE"); **employer shares → 6037 / 2537, 6020 / 2550, 6040 / 2560** (WTC V3.0: 2537, 2550, 2560 "TD CNPS Contribution ER"). The Dev posts the 3.5% EE band to 6020/2550 and the 7.5% ER band to 2610/2551 — inverted; v5 keeps the v4 pairs. '
    'Band 5: negative copy of the EE share for the IRPP deduction (CGI Art. 47-I « retenues effectuées au titre de la sécurité sociale »). Band 6: total rate in 58131, only when there is an insurable salary (read by the Récapitulatif; WTC V3.0 names 58131 "TD CNPS Contribution EE" — rename requested, R27). `_$$`: the EE share is gross-up eligible.', 'Social Security')
reg(9148061, 'TD Supplementary Retirement — Deductible Portion', 'retro_simple_tax', 'Flat', '',
    [band(ee=100, ceilacc='58172', deb='99999', cred='58101')],
    [('21610', '', 'No'), ('21611', '', 'No'), ('21670', '', 'No'), ('21649', '2164%', 'No'), ('21699', '216%%', 'Yes')],  # 2160x compulsory-scheme code to create (R16)
    'CGI Art. 47-I: employee retirement contributions deductible up to 3.5% of the appointments (58172, ceiling account); **Art. 47-II (v5): only if compulsory** (« doivent revêtir un caractère obligatoire »). 2164x is "Voluntary Contribution" in WTC V3.0 → **No**. Other 216xx = compulsory scheme codes (none in WTC V3.0 today: research gap R16). Negative in 58101.')
reg(9148071, 'TD IRPP Taxable Income', 'simple_tax', 'Flat', NOT_DIPLO, [band(ee=100, deb='58552')],
    [(a, '', 'Yes') for a in ['58008', '58104', '58108', '58113', '58114', '58115', '58100', '58101']],
    'IRPP gross less the Art. 45 exempt portions (transport 58104, family 58108, plan social 58113, function allowance / per diem 58114, leave ticket 58115), the EE CNPS share (58100) and the deductible compulsory retirement contribution (58101; WTC V3.0 names it "TD Voluntary Contribution" — rename requested, R27) — CGI Art. 47-I. **58552 is the account the IRPP-TS and DAS reports read**; it runs for every status except diplomatic, non-residents included.')
reg(9148072, 'TD IRPP-TS — Progressive Scale', 'retro_simple_tax', 'Differential', SCALE,
    [band(f=0, t=800000, ee=0, deb='58112'), band(f=800000, t=6000000, ee=10.5, deb='58112'),
     band(f=6000000, t=7500000, ee=15, deb='58112'), band(f=7500000, t=9000000, ee=20, deb='58112'),
     band(f=9000000, t=12000000, ee=25, deb='58112'), band(f=12000000, t=9999999999999, ee=30, deb='58112')],
    [('58552', '', 'Yes')],
    'CGI Art. 1-IV (CGI 2026 p. 14; LF 2026 Art. 3): « 0 et 800 000 0% … Plus de 12 000 000 30% », annual bands auto-divided by the period; last band closed. Round 3: limits written at the round figure (incomeTo 800,000 = incomeFrom of the next band), so the tax starts at the 800,001st franc as the table says (the `x.99` limits of v4 and the Dev taxed 0.99 XAF a year less and gave 1 XAF less at a half franc). Annualisation: each month × 12 — irregular payments see ASSUMPTIONS A26. Runs for residents (58218 = 0), **non-residents (58218 = 1, round 2)** and young graduates (3), except the Art. 3-4° exempt (58226 = 1: real-regime entity, start date given and ≤ 60 months, under 35 at recruitment, young graduate or worker). Disabled (Art. 45-18°) and diplomatic (Art. 3-2°) do not run it. '
    'Non-resident (decided 1 Nov): the salary of a non-domiciled employee working in Chad for an employer established in Chad is Art. 44 income (Art. 44-II-2°, p. 29), withheld on the scale (Art. 847, p. 168) with the Art. 45 exemptions, Art. 46 caps and Art. 47 deductions; the 18% of Art. 116 (p. 43) covers only Art. 2-VI (royalties, BNC of Art. 49) and Art. 60 (artists).')
reg(9148073, 'TD IRPP-TS — Resident Withholding', 'simple_tax_$$_post_formula', 'Flat', RESIDENT_SCALE,
    [band(ee=100, formula=R_IRPP, deb='2610', cred='2552')], [('58112', '', 'Yes')],
    'Rounded once, on the total, to the whole XAF — **technical convention, no rule in the CGI** (no IRPP rounding rule in the CGI 2026; Art. 847 refers to a DGI barème not obtained; XAF has no subunit). `_$$`: gross-up eligible. 2552 read by IRPP-TS and DAS.')
reg(9148074, 'TD Non-Resident Tax Base', 'simple_tax_period', 'Flat', NR, [band(ee=100, deb='58592', cred='99998')],
    [('58552', '', 'Yes')],
    'Round 2: copy of the non-resident\'s taxable income 58552 (same base as residents) into 58592, kept only because the IRPP-TS report reads 58592 for non-residents. Report-feeding base (`_period`, 99998).')
reg(9148075, 'TD IRPP-TS — Non-Resident Withholding (scale)', 'simple_tax_$$_post_formula', 'Flat', NR_SCALE,
    [band(ee=100, formula=R_IRPP, deb='2610', cred='2592')], [('58112', '', 'Yes')],
    'Round 2: **progressive scale, not 18%** — the 9148072 result for a non-resident, posted to 2592 so the IRPP-TS report keeps residents (2552) and non-residents (2592) apart. Same rounding convention as 9148073. `_$$`: gross-up eligible.')
reg(9148081, 'TD TFE Base', 'simple_tax_period', 'Flat', TFE_POP, [band(ee=100, deb='58563', cred='99998')], TFE_BASE,
    'CGI Art. 189: gross salaries, « indemnités diverses, allocations, gratifications », and benefits « pour leur montant réel ». No Art. 45 carve-out (exempt transport, family allowances, scholarships, leave ticket 6255x and per diem 62570 / 6557x / 6558x stay in — round 2; reimbursements with receipts, 6256x, out). v5: **non-residents in** (Art. 187: tax on the payer, no residence condition) — only diplomatic (4) and the Art. 188-10° exempt share (58219 = 1: real-regime entity paying a disabled person, or a young graduate or worker under 35) are out. Severance 6218x out as in v4 (see ASSUMPTIONS A20). Round 3: pensions 6264x in (Arts. 187, 189-1° « pensions »). TFE report reads 58563.')
reg(9148082, 'TD TAFP Base', 'simple_tax_post_formula_period', 'Flat', TFE_POP,
    [band(ee=100, formula='MULTIPLY(FLOOR(DIVIDE($band_amount_raw;1000));1000)', deb='58534', cred='99998')], TAFP_BASE,
    'CGI Art. 173: « montant brut des appointements, salaires, avantages en nature et rétributions quelconques, **y compris les gratifications servies régulièrement** ». Round 3: own matrix — TFE base less one-time / discretionary bonuses 6222x (a contrario, not regular; WTC V3.0 Apprenticeship No) and less pensions 6264x (not in Art. 173). Annual bonus 6220x treated as regular (A30). v5: non-residents in (Art. 173: paid by the enterprise, no residence condition); Art. 174-3° exempt share out (58219). Fraction up to 1,000 XAF dropped (Art. 177) — per employee here, while Art. 177 speaks of the « montant global » (A31). TAFP report reads 58534.')
reg(9148083, 'TD TFE — Employer Lump-Sum Tax', 'simple_tax_post_formula', 'Flat', '',
    [band(er=7.5, formula='FLOOR(ADD(MULTIPLY($band_amount_raw;IF(EQUALS($58206;1);0;IF(EQUALS($58206;2);0.5;1)));0.5))', deb='6063', cred='2563')],
    [('58563', '', 'Yes')], 'CGI Art. 190: « 7,5 % du montant brut des sommes imposables ». Art. 190 has no rounding rule (only the TAFP has one, Art. 177); round 3: the amount is **paid to the whole franc — technical payment convention, FLOOR(x+0.5), not a statutory rounding** (XAF has no subunit), the same convention as the IRPP. Reduced by 50% (Art. 158) or exempt (LF 2020 Art. 14) per entity flag 58206.')
reg(9148084, 'TD TAFP — Apprenticeship & Training Tax', 'simple_tax_post_formula', 'Flat', '',
    [band(er=1.2, formula='MULTIPLY(FLOOR(DIVIDE(ADD(MULTIPLY($band_amount_raw;IF(EQUALS($58206;1);0;IF(EQUALS($58206;2);0.5;1)));5);10));10)', deb='6034', cred='2534')],
    [('58534', '', 'Yes')], 'CGI Art. 178, 12‰; Art. 177: « arrondi à la dizaine de Francs la plus voisine ». Same relief as TFE (58206; Art. 158 « 50% de la taxe d\'apprentissage »).')
reg(9148091, 'TD PSA — Food Security Levy', 'simple_tax_$$_monthly', 'Flat', f'AND({NOT_DIPLO};GREATER($58105;0))',
    [band(ee=100, floor=400, ceil=400, deb='2610', cred='2570')], [('58105', '', 'Yes')],
    'v5, new. CGI Arts. 837–839 (LF 2024 Art. 21; CGI 2026 p. 166): « dû par les employés du secteur public, du secteur formel privé… » · « établi, recouvré… comme en matière d\'impôt sur le revenu des personnes physiques » · « fixé à 400 FCFA/mois et par employé ». Employee deduction, 400 XAF a month (Floor = Ceiling, `_monthly`), every status except diplomatic, only in a month with cash pay. Liability 2570 — **new WTC code needed** (research gap R17); reported with the IRPP. `_$$`: employee withholding, gross-up eligible as the IRPP.')


# ---------------------------------------------------------------- SKILL.md writer
def num(v):
    if v == '' or v is None:
        return ''
    return f'{v:,.3f}'


def write_skill():
    L = ['---', 'name: "chad-design-blueprint-claude-v5"',
         'description: "Chad (TD) payroll regulation design v5 — v4 plus the statutory verdicts of 1 Nov 2026 read in the CGI 2026 (DGI edition) and the WTC V3.0, the CNPS decrees of 2009 and the CNPS employer guide (round 2, same day), and the engine structures where the Dev design is better. Design Blueprint format, tax year td_2026. Round 3 after the independent QA review."',
         '---', '',
         '> **Analysis instructions:** read and follow `Regulation_Design_Analysis_Engine.md` before interpreting or computing any regulation below.', '',
         '> **Companions:** `CHANGELOG.md` — what changed from v4 and the article behind it · `ASSUMPTIONS.md` — decisions taken, alternatives and what is still not settled · `RESEARCH_GAPS.md` — what compliance must fix · `VALIDATION.md` — the scenarios executed, expected × obtained, and v5 × Dev.', '',
         '> **Source of every article cited:** Code Général des Impôts du Tchad 2026, DGI edition (`raw/docs/oficiais/TD/2026-11-01-CGI-TCHAD-2026-FINAL-dgi.pdf`, md5 139d5326…); LF 2024–2026 where the CGI says so; CNPS: Dec. 1635 and 1636/PR/PM/MFPT/2009 and the CNPS Guide de l’employeur 2019 (`raw/docs/oficiais/TD/2026-11-01-*`).', '',
         '# 0 - Flags', '', '| Account | Flag | Formula | Values |', '| --- | --- | --- | --- |']
    for a, n, f, v in FLAGS:
        L.append(f'| {a} | {n} | `{f}` | {v} |')
    L += ['', 'Flag numbers follow the WTC V3.0 / Dev where they exist (58205, 58206, 58212, 58218 — 58212 counts children, not all dependants); the others are new (ASSUMPTIONS A14). 58219 and 58226 are derived from the other flags. 58201 is reserved for advanced reconciliation and is not used.', '', '---', '']
    hdr = '| incomeFrom | incomeTo | employeeRate | employerRate | floorAmount | ceilingAmount | creditAmount | Formula | assertion | Start Date | End Date | unit account | employeeRateAccount | employerRateAccount | floorAccount | ceilingAccount | debitAccount | creditAccount |'
    for r in R:
        L += [f"# {r['id']} - {r['name']}", '', f"## **Regulation Name: {r['name']}**", '', '**System Tax Years:** td_2026', '',
              '**System Reporting Periods:**', '', f"**Regulation ID:** {r['id']}", '', '**Status:** active', '',
              f"**Processing Order (Ordinal):** {r['ord']}", '', '**1. Classification**', '', f"* **Tax Group:** {r['group']}",
              f"* **Tax Rule Group:** {r['trg']}", f"* **Taxation Type:** {r['ttype']}", '* **Currency:** XAF', '',
              '**2. Execution Conditions (Assertions)**', '', f"* **Pre-condition:** {r['pre']}", '', '**3. Calculation Logic (Bands)**', '',
              hdr, '| ' + ' | '.join(['---'] * 18) + ' |']
        for b in r['bands']:
            L.append('| ' + ' | '.join([num(b['f']), num(b['t']), num(b['ee']), num(b['er']), num(b['floor']), num(b['ceil']), '',
                                         b['formula'], b['assertion'], '01-01-2026', '', '', '', '', '', b['ceilacc'], b['deb'], b['cred']]) + ' |')
        L += ['', '**4. Taxability Rules (Applicable Accounts)**', '', '| Account | Pattern | Is Taxable? |', '| --- | --- | --- |']
        for a, p, y in r['matrix']:
            L.append(f'| {a} | {p} | {y} |')
        L += ['', f"> {r['note']}", '', '---', '']
    with open(os.path.join(OUT, 'SKILL.md'), 'w', encoding='utf-8', newline='\n') as fh:
        fh.write('\n'.join(L))


# ---------------------------------------------------------------- engine (as the analysis file describes; same as v4)
def matches(code, acc, pat):
    if pat:
        p = pat.replace('%', '')
        return code.startswith(p) and len(code) == len(pat)
    return code == acc


def matrix_sum(matrix, values):
    tot = 0.0
    for code, v in values.items():
        if v == 0:
            continue
        exact = [m for m in matrix if not m[1] and m[0] == code]
        if exact:
            if exact[0][2] == 'Yes':
                tot += v
            continue
        pats = sorted([m for m in matrix if m[1] and matches(code, m[0], m[1])], key=lambda m: -len(m[1].replace('%', '')))
        if pats and pats[0][2] == 'Yes':
            tot += v
    return max(tot, 0.0)


def ev(expr, A, raw=None):
    """Tiny evaluator for the formula language used in this design."""
    import re
    e = expr.replace('$band_amount_raw', repr(raw) if raw is not None else '0')
    e = re.sub(r'\$(\d{5})', lambda m: repr(A.get(m.group(1), 0.0)), e)
    e = e.replace(';', ',')
    env = dict(FLOOR=math.floor, ADD=lambda a, b: a + b, MULTIPLY=lambda a, b: a * b, DIVIDE=lambda a, b: a / b, MIN=min, MAX=max,
               EQUALS=lambda a, b: a == b, LESS=lambda a, b: a < b, GREATER=lambda a, b: a > b, NOT=lambda a: not a,
               AND=lambda *a: all(a), OR=lambda *a: any(a), IF=lambda c, a, b: a if c else b)
    return eval(e, {'__builtins__': {}}, env)


FLAG_F = {a: f for a, n, f, v in FLAGS}
FLAG_ACCS = {a for a, n, f, v in FLAGS}


def run(inputs, flags, periods=12):
    A = {k: float(v) for k, v in flags.items()}
    for d in DERIVED:
        if d not in flags:
            A[d] = float(ev(FLAG_F[d], A))
    for r in R:
        if r['pre'] and not ev(r['pre'], A):
            continue
        vals = dict(inputs)
        vals.update({k: v for k, v in A.items() if len(k) == 5 and k.startswith('58') and k not in FLAG_ACCS})
        base = matrix_sum(r['matrix'], vals)
        monthly = '_monthly' in r['trg']
        div = 1 if monthly else periods
        if r['ttype'] == 'Differential':
            tot = 0.0
            ann = base * periods
            for i, b in enumerate(r['bands']):
                lo = r['bands'][i - 1]['t'] if i > 0 else 0
                if ann > lo:
                    tot += (min(ann, b['t']) - lo) * b['ee'] / 100
            A[r['bands'][0]['deb']] = A.get(r['bands'][0]['deb'], 0) + tot / periods
            continue
        for b in r['bands']:
            if b['assertion'] and not ev(b['assertion'], A):
                continue
            rate = b['ee'] if b['ee'] != '' else b['er']
            amt = base * rate / 100
            if b['floor'] != '' and base > 0:
                amt = max(amt, b['floor'] / div)
            if b['ceil'] != '':
                amt = min(amt, b['ceil'] / div)
            if b['ceilacc']:
                amt = min(amt, A.get(b['ceilacc'], 0.0))
            if b['formula']:
                amt = ev(b['formula'], A, amt)
            if b['cred'] in ('99999', '99998'):
                A[b['deb']] = A.get(b['deb'], 0) + amt
            elif b['deb'] == '99999':
                A[b['cred']] = A.get(b['cred'], 0) - amt
            else:
                A[b['cred']] = A.get(b['cred'], 0) + amt
    return A


RES = {'58218': 0, '58202': 1, '58203': 1, '58204': 1, '58205': 0, '58206': 0, '58207': 1, '58210': 2, '58212': 0,
       '58213': 0, '58215': 1, '58216': 30, '58217': 2, '58223': 0, '58225': 28}

# (name, inputs, flag overrides, expected EE CNPS, IRPP, TFE, TAFP, PSA, Net) — expected hand-computed from the CGI 2026
# Net = cash pay (62xxx) - EE CNPS - IRPP - PSA - deductions 21xxx
SCEN = [
    ('1 Active baseline 350,000', {'62100': 350000}, {}, (12250, 28464, 26250, 4200, 400, 308886)),
    ('2 Zero salary', {}, {}, (0, 0, 0, 0, 0, 0)),
    ('3 13th month', {'62100': 350000, '62200': 350000}, {}, (17500, 75750, 52500, 8400, 400, 606350)),
    ('4 Housing real 50,000 under a 120,000 cap', {'62100': 600000, '65400': 50000}, {}, (17500, 65750, 48750, 7800, 400, 516350)),
    ('5 Individual severance 900,000', {'62100': 300000, '62180': 900000}, {}, (10500, 208600, 22500, 3600, 400, 980500)),
    ('6 Compulsory supplementary pension 30,000 (cap 14,000)', {'62100': 400000, '21600': 30000}, {}, (14000, 32060, 30000, 4800, 400, 323540)),
    ('7 Transport 120,000, granted to all (CNPS: transport out in full)', {'62100': 300000, '62520': 120000}, {}, (10500, 26548, 31500, 5040, 400, 382552)),
    ('8 Family allowance 30,000, 0 children', {'62100': 300000, '62760': 30000}, {}, (10500, 26548, 24750, 3960, 400, 292552)),
    ('9 Entity with 50% relief', {'62100': 350000}, {'58206': 2}, (12250, 28464, 13125, 2100, 400, 308886)),
    ('10 Young graduate, month 30, age 30, real-regime entity', {'62100': 350000}, {'58218': 3, '58205': 30}, (12250, 0, 0, 0, 400, 337350)),
    ('11 Non-resident 800,000 (all CNPS branches, progressive scale)', {'62100': 800000}, {'58218': 1}, (17500, 97375, 60000, 9600, 400, 684725)),
    ('12 Family allowance 30,000, 6 children', {'62100': 300000, '62760': 30000}, {'58212': 6}, (10500, 23398, 24750, 3960, 400, 295702)),
]
EXTRA = [
    ('E1 Family 30,000, 6 children, CNPS pays 7,300', {'62100': 300000, '62760': 30000}, {'58212': 6, '58213': 7300}, (10500, 24164, 24750, 3960, 400, 294936)),
    ('E2 School scholarship 6580x 50,000', {'62100': 300000, '65800': 50000}, {}, (12250, 23214, 26250, 4200, 400, 264136)),
    ('E3 Meal allowance 62860 40,500 (in CNPS; TFE 25,537.5 paid 25,538)', {'62100': 300000, '62860': 40500}, {}, (11918, 27501, 25538, 4080, 400, 300681)),
    ('E4 Function allowance 6287x 101,000 (15% cap 60,150)', {'62100': 300000, '62870': 101000}, {}, (10500, 27687, 30075, 4810, 400, 362413)),
    ('E5 Worker (ouvrier) aged 25, month 30, real-regime entity -> IRPP, TF, TA exempt', {'62100': 350000}, {'58217': 1, '58216': 25, '58205': 30}, (12250, 0, 0, 0, 400, 337350)),
    ('E6 Same worker, entity not under the real regime -> all due', {'62100': 350000}, {'58217': 1, '58216': 25, '58205': 30, '58215': 2}, (12250, 28464, 26250, 4200, 400, 308886)),
    ('E7 Voluntary pension 2164x 30,000 (Art. 47-II: not deductible)', {'62100': 400000, '21640': 30000}, {}, (14000, 33530, 30000, 4800, 400, 322070)),
    ('E8 Leave ticket 6255x 200,000, annual limit 150,100', {'62100': 300000, '62550': 200000}, {'58223': 150100}, (10500, 28637, 37500, 6000, 400, 460463)),
    ('E9 Per diem 62570 50,000 + function allowance 6287x 51,000 (one 15% cap)', {'62100': 300000, '62570': 50000, '62870': 51000}, {}, (10500, 27687, 30075, 4810, 400, 362413)),
    ('E10 Non-resident 800,000 seconded under a convention (CNPS branches off)', {'62100': 800000}, {'58218': 1, '58202': 2, '58203': 2, '58204': 2}, (0, 101750, 60000, 9600, 400, 697850)),
    ('E11 Schooling allowance 6274x 50,000 (taxable everywhere)', {'62100': 300000, '62740': 50000}, {}, (12250, 28464, 26250, 4200, 400, 308886)),
    ('E12 Young graduate aged 36 at recruitment (now 38), real regime, month 30 -> all due', {'62100': 350000}, {'58218': 3, '58205': 30, '58225': 36, '58216': 38}, (12250, 28464, 26250, 4200, 400, 308886)),
    ('E13 Young graduate under 35, entity not under the real regime -> all due', {'62100': 350000}, {'58218': 3, '58205': 30, '58215': 2}, (12250, 28464, 26250, 4200, 400, 308886)),
    ('E14 Worker aged 25, month 61 -> IRPP due, TF/TA still exempt', {'62100': 350000}, {'58217': 1, '58216': 25, '58205': 61}, (12250, 28464, 0, 0, 400, 308886)),
    ('E15 One-time bonus 6222x 100,000 -> out of the TAFP base only', {'62100': 300000, '62220': 100000}, {}, (14000, 33530, 30000, 3600, 400, 352070)),
    ('E16 Car & transportation allowance 6251x 120,000 -> same as scenario 7', {'62100': 300000, '62510': 120000}, {}, (10500, 26548, 31500, 5040, 400, 382552)),
    ('E17 Pension 6264x 50,000 -> out of IRPP, CNPS, TA; in TF', {'62100': 300000, '62640': 50000}, {}, (10500, 23398, 26250, 3600, 400, 315702)),
    ('E18 Worker aged 45, real regime, NO exemption start date (58205 = 0) -> all due', {'62100': 350000}, {'58217': 1, '58216': 45, '58205': 0}, (12250, 28464, 26250, 4200, 400, 308886)),
    ('E19 Worker aged 40 at recruitment (now 42), real regime, month 30 -> all due (restrictive reading, A34)', {'62100': 350000}, {'58217': 1, '58216': 42, '58225': 40, '58205': 30}, (12250, 28464, 26250, 4200, 400, 308886)),
    ('E20 Young graduate under 35, real regime, NO start date -> IRPP due; TF/TA exempt (Arts. 188-10, 174-3 need no date)', {'62100': 350000}, {'58218': 3, '58205': 0}, (12250, 28464, 0, 0, 400, 308886)),
]
EDGE = set()   # round 3: no tolerance — every column must match the hand calculation exactly


def outcome(inp, fo):
    f = dict(RES)
    f.update(fo)
    A = run(inp, f)
    ee = A.get('2551', 0)
    irpp = A.get('2552', 0) + A.get('2592', 0)
    tfe, tafp, psa = A.get('2563', 0), A.get('2534', 0), A.get('2570', 0)
    cash = sum(v for k, v in inp.items() if k.startswith('62'))
    ded = sum(v for k, v in inp.items() if k.startswith('21'))
    net = cash - ee - irpp - psa - ded
    return (ee, irpp, tfe, tafp, psa, net), A


def validate(scen):
    rows = []
    for name, inp, fo, exp in scen:
        got, A = outcome(inp, fo)
        got = tuple(round(x, 2) for x in got)
        diff = tuple(round(g - e, 2) for g, e in zip(got, exp))
        if all(abs(d) < 0.005 for d in diff):
            st = 'OK'
        else:
            st = 'DIFF'
        rows.append((name, exp, got, diff, st, A))
    return rows


def fmt(x):
    return f'{x:,.2f}'.rstrip('0').rstrip('.') if x != int(x) else f'{int(x):,}'


if __name__ == '__main__':
    write_skill()
    out = []
    bad = 0
    for title, sc in (('12 scenarios', SCEN), ('extra checks of the v5 changes', EXTRA)):
        out.append(f'## {title}')
        out.append('| Scenario | EE CNPS | IRPP | TFE | TAFP | PSA | Net | status |')
        for n, e, g, d, st, A in validate(sc):
            bad += st == 'DIFF'
            cells = [fmt(gv) if abs(dv) < 0.005 else f'{fmt(gv)} (exp. {fmt(ev_)})' for gv, ev_, dv in zip(g, e, d)]
            out.append(f'| {n} | ' + ' | '.join(cells) + f' | {st} |')
    _, A11 = outcome({'62100': 800000}, {'58218': 1})
    _, A12 = outcome({'62100': 300000, '62760': 30000}, {'58212': 6})
    out.append(f"S11: 58552 = {A11.get('58552', 0):,.0f} · 58592 = {A11.get('58592', 0):,.0f} · 2592 = {A11.get('2592', 0):,.0f} · 2552 = {A11.get('2552', 0):,.0f} · 58563 = {A11.get('58563', 0):,.0f} · 58534 = {A11.get('58534', 0):,.0f}")
    out.append(f"S12: 58107 = {A12.get('58107', 0):,.0f} · 58108 = {A12.get('58108', 0):,.0f} · 58552 = {A12.get('58552', 0):,.0f}")
    out.append('ALL EXPECTED (exact, every column)' if not bad else f'{bad} MISMATCH')
    txt = '\n'.join(out)
    print(txt)
    with open(os.path.join(HERE, 'VALIDATION-run.txt'), 'w', encoding='utf-8', newline='\n') as fh:
        fh.write(txt + '\n')
    sys.exit(0 if not bad else 1)
