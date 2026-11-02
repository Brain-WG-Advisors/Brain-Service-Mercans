"""Chad design v6 — generator and executable validation.

v6 = v5 (2026-11-01, after 2 QA rounds) rebuilt in the form of the development team's td_2026 design (CT-A-588 / td.json):
regulation IDs, names and ordinals (9148xxx), tax group / rule group / taxation type, intermediate and result accounts,
formula conventions (limits inside MIN(), $period_divisor, annualise -> annual tax -> period tax), band order, flags of the Dev
where they cover the case. Where the law obliges a different rule, the v5 rule is kept and the note says
"Deliberate divergence (law)". Rules with no Dev pair are additional regulations in the Dev pattern.
The regulations are run on the same 12 scenarios + 20 extra checks as v5; the results must be identical to v5
(checked against the expected values and against the v5 engine itself, account by account).
Run:  python -I _build_v6.py   (writes SKILL.md and VALIDATION-run.txt, prints the table)
Base: ../2026-11-01-design-v5/_build_v5.py (read only, not changed). Changes: CHANGELOG.md of the blueprint.
"""
import math, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'chad-design-blueprint-claude-v6')
V5_BUILD = os.path.join(os.path.dirname(HERE), '2026-11-01-design-v5', '_build_v5.py')
PERIODS = 12
CNPS_SRC = "Dec. 1635/PR/PM/MFPT/2009 arts. 1–4, Dec. 1636/PR/PM/MFPT/2009 arts. 1–3, Dec. 1634/2009 (AT/MP; text not obtained, rate from the guide p. 8), effective date 2009-12-04 per the guide p. 8 (Journal Officiel not obtained); CNPS Guide de l'employeur 2019, p. 6–9 and 12"

# ---------------------------------------------------------------- statutory parameters
# CNPS (decided, round 2): PFM 7.5% ER (Dec. 1635), PVID 5% ER + 3.5% EE (Dec. 1636), AT/MP 4% ER (Dec. 1634, via guide p. 8), from 2009-12-04 (guide p. 8);
# ceiling 500,000 a month = 6,000,000 a year, same for the 3 branches (Dec. 1635 art. 4, Dec. 1636 art. 3);
# floor = SMIG 59,995 rounded to 60,000 a month (Dec. 1111/2011; guide p. 7 and 9), only in a month with pay.
CNPS = dict(pvid_ee=3.5, pvid_er=5, pfm_er=7.5, atmp_er=4, floor_m=60000, ceil_m=500000, total=20)

# ---------------------------------------------------------------- flags
FLAGS = [
    ('58218', 'Status (global flag)',
     '$hr.employee_type',
     'As the Dev (`$hr.employee_type`): 0 resident · 1 non-resident · 2 disabled (CGI Art. 45-18°) · 3 young graduate (Art. 3-4°) · 4 diplomatic (Art. 3-2°); routing uses `LESS($58218;1)` for residents, never an equality test against zero'),
    ('58202', 'CNPS PVID eligible', "IF(EQUALS($hr.cnps_eligibility_pvid::key;'N');2;1)",
     '1 yes (default, every employee, **non-residents included**: « quelle que soit… leur nationalité », CNPS guide p. 6) · 2 no — only a seconded employee covered by a bilateral or multilateral convention (CIPRES) with a secondment certificate'),
    ('58203', 'CNPS PFM eligible', "IF(EQUALS($hr.cnps_eligibility_pfm::key;'N');2;1)", '1 yes (default) · 2 no — as 58202'),
    ('58204', 'CNPS AT/MP eligible', "IF(EQUALS($hr.cnps_eligibility_atmp::key;'N');2;1)", '1 yes (default) · 2 no — as 58202'),
    ('58205', 'Art. 3-4° exemption months (young graduate / worker)',
     'CEIL(MULTIPLY(YEARS_BETWEEN($hr.young_graduate_employee_exemption_start_date;$entry.period_end_date);12))',
     'As the Dev formula. Months since the Art. 3-4° exemption start (date of recruitment by the real-regime entity), current month included; IRPP exemption while ≤ 60 (« pendant une période de cinq ans »). The same DD date is used for workers. WTC V3.0 names 58205 "Young Graduate Start Date" but its formula (and the Dev) also yields months; read by the IRPP-TS report'),
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
              ('62619', '6261%', 'Yes'), ('62639', '6263%', 'Yes'), ('62659', '6265%', 'Yes'), ('62669', '6266%', 'Yes'), ('62799', '627%%', 'Yes'), ('62869', '6286%', 'Yes'),   # v6 r3: 6261%, 6265% (QA W1)
              ('62879', '6287%', 'Yes'), ('62889', '6288%', 'Yes'), ('62890', '', 'Yes'), ('62999', '629%%', 'Yes'), ('65519', '6551%', 'Yes'),
              ('65619', '6561%', 'Yes'), ('65669', '6566%', 'Yes'), ('65799', '657%%', 'Yes'), ('79499', '794%%', 'Yes')]
BIK_REAL = [('62679', '6267%', 'Yes'),   # v6 r3: exact No on 65610–65612 / 65660–65662 removed — they kept cash-in-lieu out of TF/TA
             ('62689', '6268%', 'Yes'), ('65299', '652%%', 'Yes'), ('65499', '654%%', 'Yes'), ('65509', '6550%', 'Yes'),
            ('65529', '6552%', 'Yes'), ('65699', '656%%', 'Yes'), ('65899', '658%%', 'Yes')]   # v6 r2: 6267%, 6268%, 6552% (whole series, as the Dev)
TFE_BASE = [('62104', '', 'No'), ('62649', '6264%', 'Yes')] + CASH_GROSS[1:] + BIK_REAL   # v6 r3: severance 6218x in the TF (Art. 189-1°), as the EOS gratuities 629xx — front decision pending the user's ok (reverses correcoes.md 2026-07-07)
# TAFP: Art. 173 — « y compris les gratifications servies régulièrement »: one-time / discretionary bonuses 6222x out; pensions 6264x not listed
TAFP_BASE = [m for m in TFE_BASE if m[1] != '6264%'] + [('62229', '6222%', 'No'),
                                                        # v6 r3: termination payments out of the TA — severance and EOS gratuities are neither pay nor regular gratifications (Art. 173)
                                                        ('62189', '6218%', 'No'), ('62900', '', 'No'), ('62909', '', 'No'),
                                                        ('62919', '6291%', 'No'), ('62929', '6292%', 'No'), ('62939', '6293%', 'No')]
CNPS_GROSS = [(a, '', 'No') for a in ['62104', '62180', '62181', '62182', '62540', '62541', '62542', '62550', '62551', '62552', '62560', '62561',
                                      '62562', '62563', '62570', '62900', '62909', '65570', '65571', '65572',
                                      '65580', '65581', '65582']] + \
             [('62519', '6251%', 'No'), ('62529', '6252%', 'No'), ('62759', '6275%', 'No'), ('62769', '6276%', 'No'), ('62789', '6278%', 'No'),
              ('62869', '6286%', 'Yes'), ('62879', '6287%', 'No'), ('65669', '6566%', 'No')] + \
             [('62199', '621%%', 'Yes'), ('62299', '622%%', 'Yes'), ('62399', '623%%', 'Yes'), ('62499', '624%%', 'Yes'), ('62599', '625%%', 'Yes'),
              ('62919', '6291%', 'No'), ('62929', '6292%', 'No'), ('62939', '6293%', 'No'),
              ('62619', '6261%', 'Yes'), ('62639', '6263%', 'Yes'), ('62659', '6265%', 'Yes'), ('62669', '6266%', 'Yes'), ('62679', '6267%', 'Yes'), ('62689', '6268%', 'Yes'),
              ('62799', '627%%', 'Yes'), ('62890', '', 'Yes'), ('62999', '629%%', 'Yes'), ('65299', '652%%', 'Yes'),
              ('65499', '654%%', 'Yes'), ('65599', '655%%', 'Yes'), ('65699', '656%%', 'Yes'), ('65799', '657%%', 'Yes'), ('65899', '658%%', 'Yes'),
              ('79499', '794%%', 'Yes')]
FAMILY = [('62759', '6275%', 'Yes'), ('62769', '6276%', 'Yes'), ('62789', '6278%', 'Yes'), ('62866', '', 'Yes')]
FUNCTION_ALLOWANCE = [('62879', '6287%', 'Yes'), ('62570', '', 'Yes'), ('65579', '6557%', 'Yes'), ('65589', '6558%', 'Yes')]
LEAVE_TICKET = [('62559', '6255%', 'Yes')]

# BIK: (account, name, limit account, rate %, monthly cap or None, matrix)
BIK = [
    ('58120', 'Housing', '58161', 20, None, [('65499', '654%%', 'Yes')]),
    ('58121', 'Vehicle', '58162', 10, None, [('65509', '6550%', 'Yes'), ('65529', '6552%', 'Yes')]),   # v6 r2: Car Fuel Benefit series 65520–65523
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
IT, SS = 'income_tax', 'social_security'
DL = 'Deliberate divergence (law)'


def reg(rid, name, trg, ttype, pre, bands, matrix, note, group=IT, v5src='', law=''):
    R.append(dict(id=rid, ord=rid - 9148000, name=name, trg=trg, ttype=ttype, pre=pre, bands=bands, matrix=matrix, note=note,
                  group=group, v5=v5src, law=law))


BASE_SALARY = [('62104', '', 'No'), ('62105', '', 'No'), ('62108', '', 'No'), ('62109', '6210%', 'Yes')]
RF = 'IF(EQUALS($58206;1);0;IF(EQUALS($58206;2);0.5;1))'   # TF/TA relief factor

reg(9148009, 'TD Annual Reporting Limit', 'simple_tax_monthly', 'flat', '', [band(ee=100, floor=60000, ceil=60000, deb='58106')],
    CASH_GROSS,
    'As the Dev: fixed 60,000 XAF a month (Floor = Ceiling), ordinal 9, before 58105 exists — so, as the Dev, the matrix is the cash pay codes themselves (the same matrix as 9148010); written only when the employee has cash pay; read by the DAS report. Reporting parameter, not a statutory value.',
    v5src='9148013')
reg(9148010, 'TD Gross Salary', 'simple_tax', 'flat', '', [band(ee=100, deb='58105')], CASH_GROSS,
    'Cash pay subject to IRPP (CGI Art. 44-I, Art. 46-I) and base of the Art. 46 caps and of the Art. 45-2° 15% limit. '
    f'{DL}: cash only — benefits in kind 65%%% and pensions 6264x are not in 58105 (Art. 46-I/II; Art. 45-1°); 6286x, 6255x, 62570 / 6557x / 6558x and 6287x are in, each relieved by its own exemption. 62867 Death allowance taxable (technical decision of the front, pending the user’s ok; ASSUMPTIONS D2). **58105 is read by the DAS report.**',
    v5src='9148012', law='cash-only matrix (Art. 46-I/II, 45-1°)')
reg(9148021, 'TD Transport Allowance Exemption', 'simple_tax', 'flat', NOT_DIPLO, [band(ee=30, deb='58103')], BASE_SALARY,
    'As the Dev: 30% of base salary into 58103 (CGI Art. 45-13° « salaire de base mensuel »). Pattern 6210% as the Dev; 62104 (rate flag), 62105 and 62108 (Historic Pay) left out as in v5.',
    v5src='9148014 (band 1)')
reg(9148031, 'TD Transport Allowance - Exempt', 'simple_tax_post_formula', 'flat', NOT_DIPLO,
    [band(ee=100, formula='MIN($band_amount_raw;$58103)', assertion='EQUALS($58207;1)', deb='99999', cred='58104')],
    [('62519', '6251%', 'Yes'), ('62529', '6252%', 'Yes')],
    f'As the Dev: MIN($band_amount_raw;$58103) into 58104 (negative), read by the DAS report. {DL}: only when the allowance is paid to all staff (58207; Art. 45-13° « lorsqu’elles profitent à tout le personnel ») and 6251x Car & Transportation shares the 30%. Leaves the IRPP base only (not TF/TA, Arts. 173, 189; not CNPS: whole transport out, 9148155).',
    v5src='9148021', law='all-staff condition, 6251x (Art. 45-13°)')
reg(9148032, 'TD Family Allowance Exemption', 'simple_tax', 'formula', NOT_DIPLO,
    [band(ee=100, formula='MAX(ADD(MULTIPLY(5000;$58212);MULTIPLY(-1;$58213));0)', deb='58107')], FAMILY,
    f'As the Dev: limit in 58107, matrix = family codes. {DL}: 5,000 per **child** (58212 reads children) less the CNPS family allowance (58213) — CGI Art. 45-4° (p. 29; LF 2026 Art. 8, p. 15) « par enfant… sur laquelle viennent… s’imputer les allocations versées par la CNPS ». Codes 6275x, 6276x, 6278x, 62866.',
    v5src='9148016', law='per child, CNPS imputed (Art. 45-4°)')
reg(9148033, 'TD Family Allowance final Exemption', 'simple_tax_post_formula', 'flat', NOT_DIPLO,
    [band(ee=100, formula='MIN($band_amount_raw;$58107)', deb='99999', cred='58108')], FAMILY,
    'As the Dev: MIN($band_amount_raw;$58107) into 58108 (negative), read by the DAS report. Excess taxable IRPP; still in the TF/TA base (Art. 189-1° « allocations »).',
    v5src='9148022')
reg(9148034, 'TD Plan-Social Severance Exemption', 'simple_tax', 'flat', 'EQUALS($58210;1)', [band(ee=100, deb='99999', cred='58113')],
    [('62189', '6218%', 'Yes')],
    f'Additional regulation (no Dev pair), Dev pattern. {DL}: only plan-social severance is exempt (CGI Art. 45-10°); individual severance stays taxable (Art. 44-I). The Dev excludes all 6218x from the gross instead.',
    v5src='9148023', law='only plan social exempt (Arts. 44-I, 45-10°)')
reg(9148035, 'TD Function Allowance Exemption', 'simple_tax_post_formula', 'flat', NOT_DIPLO,
    [band(ee=100, formula='MIN($band_amount_raw;MULTIPLY($58105;0.15))', deb='99999', cred='58114')], FUNCTION_ALLOWANCE,
    f'Additional regulation (no Dev pair), in the Dev convention (limit inside the formula, % × 58105). {DL}: CGI Art. 45-2° (p. 29) — function-expense allowances and fixed per diem exempt up to 15% of salaries plus those allowances. Codes 6287x (to create, R15), 62570, 6557x, 6558x. IRPP base only.',
    v5src='9148015 (band 10) + 9148024', law='Art. 45-2° 15% exemption')
reg(9148036, 'TD Leave Ticket Exemption', 'simple_tax_post_formula', 'flat', NOT_DIPLO,
    [band(ee=100, formula='MIN($band_amount_raw;$58223)', deb='99999', cred='58115')], LEAVE_TICKET,
    f'Additional regulation (no Dev pair), Dev convention. {DL}: CGI Art. 45-15° (p. 30) — one ticket a year per person (annual limit 58223 from the DD, applied per payment, A24). IRPP base only; in TF/TA; out of CNPS.',
    v5src='9148025', law='Art. 45-15° leave ticket')
for k, (o, b) in enumerate(zip([41, 51, 61, 71, 81, 91, 101, 111, 121], BIK)):
    devname = ['TD Housing Capped Value for Tax', 'TD Vehicle Capped Value for Tax', 'TD Food Capped Value for Tax', 'TD Interior furnishings Capped Value for Tax',
               'TD Domestic help / security staff Capped Value for Tax', 'TD Electricity Capped Value for Tax', 'TD Water Capped Value for Tax',
               'TD Phone Capped Value for Tax', 'TD Gas Capped Value for Tax'][k]
    cap = f'MULTIPLY($58105;{b[3] / 100:.2f})'
    if b[4]:
        cap = f'MIN({cap};{b[4]})'
    reg(9148000 + o, devname, 'simple_tax_post_formula', 'flat', '',
        [band(ee=100, formula=f'MIN($band_amount_raw;{cap})', deb=b[0])], b[5],
        f'As the Dev: ID, name, ordinal, rule group, % × 58105 inside the formula, account {b[0]} (read by the DAS report). {DL}: MIN(real value; {cap}) instead of the forfait {cap} — CGI Art. 46-III « Ceux-ci sont plafonnés », Art. 46-V « dans la limite des taux »; the matrix holds the real benefit codes.',
        v5src=f'9148015 (band {k + 1}) + 91480{31 + k}', law='cap, not forfait (Art. 46-III/V)')
reg(9148131, 'TD Gross Taxable Salary', 'simple_tax', 'flat', NOT_DIPLO, [band(ee=100, deb='58008')],
    [('58105', '', 'Yes')] + [(b[0], '', 'Yes') for b in BIK] + [(a, '', 'No') for a in ['65853', '65854', '65855', '65856', '65857']] +
    [('62679', '6267%', 'Yes'), ('62689', '6268%', 'Yes'), ('65299', '652%%', 'Yes'), ('65630', '', 'Yes'), ('65809', '6580%', 'No'), ('65899', '658%%', 'Yes')],
    f'As the Dev: 58008, read by the DAS report. {DL}: built on the cash gross 58105 plus the capped BIK values; individual severance in (Art. 44-I), 6274x and health insurance 65630 in, 6580x scholarship out (Art. 45-9°).',
    v5src='9148041', law='severance, 6274x, 65630 in; 6580x out (Arts. 44-I, 45-9°)')
reg(9148141, 'TD Apprenticeship Base', 'simple_tax_post_formula_period', 'flat', TFE_POP,
    [band(ee=100, formula='MULTIPLY(FLOOR(DIVIDE($band_amount_raw;1000));1000)', deb='58534', cred='99998')], TAFP_BASE,
    f'As the Dev: rule group, truncation to the 1,000 (Art. 177), 58534 read by the TAFP report. {DL}: gross base of Art. 173 (no Art. 45 carve-out; one-time bonuses 6222x, pensions 6264x and — v6 r3 — termination payments 6218x, 62900/62909, 6291x–6293x out: Art. 173 lists remuneration and regular gratifications only) and the Art. 174-3° share out (58219).',
    v5src='9148082', law='Art. 173 base, Art. 174-3° exemption')
reg(9148151, 'TD Employer Lump-Sum Tax Base', 'simple_tax_period', 'flat', TFE_POP, [band(ee=100, deb='58563', cred='99998')], TFE_BASE,
    f'As the Dev: rule group, 58563 read by the TFE report. {DL}: gross base of Art. 189 (« indemnités diverses, allocations, gratifications », pensions; benefits at real value) — v6 r3: severance 6218x and EOS gratuities 629xx **in** (« indemnités diverses ») — technical decision of the front, pending the user’s ok; reverses `correcoes.md` 2026-07-07 ("severance outside the TFE"; ASSUMPTIONS A20), medical insurance 6261x and social allowance 6265x in, cash-in-lieu 6561x / 6566x in; the Art. 188-10° share out (58219).',
    v5src='9148081', law='Art. 189 base, Art. 188-10° exemption')
reg(9148155, 'TD CNPS Insurable Salary without capping', 'simple_tax', 'flat', NOT_DIPLO, [band(ee=100, deb='58130')], CNPS_GROSS,
    f'As the Dev: 58130, read by the CNPS Récapitulatif. {DL}: base per Dec. 1635 art. 3 / Dec. 1636 art. 2 and the CNPS guide p. 7–8 — benefits in kind, 6286x, 6274x, 6580x in; family allowances, meal cash 6566x, severance, ticket, per diem, relocation, 6287x out; transport 6251x/6252x out in full (technical decision of the front, guide p. 8, pending the user’s ok; ASSUMPTIONS D1).',
    group=SS, v5src='9148051', law='CNPS base (Dec. 1635 art. 3; guide p. 7–8)')
reg(9148161, 'TD CNPS Insurable Salary', 'simple_tax_period', 'flat', f'AND({NOT_DIPLO};GREATER($58130;0))',
    [band(ee=100, floor=CNPS['floor_m'] * 12, ceil=CNPS['ceil_m'] * 12, deb='58550', cred='99998')], [('58130', '', 'Yes')],
    f'As the Dev: rule group, floor 720,000 / ceiling 6,000,000 a year (60,000 / 500,000 a month; Dec. 1635 art. 4, Dec. 1636 art. 3; guide p. 9), 58550. {DL}: `GREATER($58130;0)` — no floor in a month without pay (guide p. 7). December regularisation of the annual ceiling not built (A23).',
    group=SS, v5src='9148052', law='floor only with pay (guide p. 7)')
reg(9148171, 'TD CNPS Contribution EE and ER', 'simple_tax_$$_post_formula', 'flat', NOT_DIPLO,
    [band(ee=CNPS['pvid_ee'], formula=R_CNPS, assertion='EQUALS($58202;1)', deb='2610', cred='2551'),
     band(er=CNPS['pfm_er'], formula=R_CNPS, assertion='EQUALS($58203;1)', deb='6020', cred='2550'),
     band(er=CNPS['atmp_er'], formula=R_CNPS, assertion='EQUALS($58204;1)', deb='6040', cred='2560'),
     band(er=CNPS['pvid_er'], formula=R_CNPS, assertion='EQUALS($58202;1)', deb='6037', cred='2537'),
     band(ee=CNPS['pvid_ee'], formula=R_CNPS, assertion='EQUALS($58202;1)', deb='99999', cred='58100'),
     band(ee=100, formula=str(CNPS['total']), assertion='GREATER($58550;0)', deb='58131')],
    [('58550', '', 'Yes')],
    'As the Dev: one regulation, band order (3.5 EE · 7.5 PFM · 4 AT/MP · 5 PVID ER · 3.5 deduction to 58100 · rate 20 to 58131), FLOOR(ADD(x;0.5)), `_$$`. '
    f'Not copied: the Dev posts the 3.5% employee band to 6020/2550 and the 7.5% employer band to 2610/2551 — an error against the WTC V3.0 (2551 = EE, 2550 = ER); v6 keeps EE 2610/2551, PFM 6020/2550. {DL}: each band gated by a branch flag (seconded employee under a convention, guide p. 6); rate 58131 only when 58550 > 0. Rates: Dec. 1635 arts. 1–2, Dec. 1636 art. 1, Dec. 1634/2009 (guide p. 8).',
    group=SS, v5src='9148053', law='branch flags (guide p. 6); EE/ER accounts per WTC')
reg(9148175, 'TD Retirement Contribution Limit', 'simple_tax', 'flat', NOT_DIPLO, [band(ee=3.5, deb='58172')], BASE_SALARY,
    f'Additional regulation (no Dev pair), Dev pattern. {DL}: 3.5% of the appointments, the deduction cap of CGI Art. 47-I (p. 30), into 58172, read by 9148181.',
    v5src='9148014 (band 2)', law='3.5% cap (Art. 47-I)')
reg(9148181, 'TD Voluntary Contribution', 'simple_tax_post_formula', 'flat', NOT_DIPLO,
    [band(ee=100, formula='MIN($band_amount_raw;$58172)', deb='99999', cred='58101')],
    [('21610', '', 'No'), ('21611', '', 'No'), ('21670', '', 'No'), ('21649', '2164%', 'No'), ('21699', '216%%', 'Yes')],
    f'As the Dev: ID, name, ordinal, account 58101. {DL}: capped at 3.5% (MIN with 58172, Art. 47-I) and only compulsory schemes — 2164x "Voluntary Contribution" No (Art. 47-II « caractère obligatoire »); compulsory-scheme code to create (R16).',
    v5src='9148061', law='3.5% cap, compulsory only (Art. 47-I/II)')
reg(9148191, 'TD Taxable Income', 'simple_tax', 'flat', NOT_DIPLO, [band(ee=100, deb='58552')],
    [(a, '', 'Yes') for a in ['58008', '58104', '58108', '58113', '58114', '58115', '58100', '58101']],
    f'As the Dev: 58552 = IRPP gross less the exempt parts and deductions (CGI Art. 47-I), read by the IRPP-TS and DAS reports. {DL}: also nets plan social 58113, the 15% allowance 58114 and the leave ticket 58115.',
    v5src='9148071', law='58113-58115 (Arts. 45-2°, 45-10°, 45-15°)')
reg(9148192, 'TD Non-Resident Tax Base', 'simple_tax_period', 'flat', NR, [band(ee=100, deb='58592', cred='99998')], [('58552', '', 'Yes')],
    f'{DL} (replaces Dev 9148011): the non-resident employee is taxed on the progressive scale with the Art. 45–47 reliefs (CGI Arts. 44-II-2°, 847; Art. 116 covers only Art. 2-VI and Art. 60), so its base is 58552, known only after 9148191; copied into 58592 for the IRPP-TS report.',
    v5src='9148074', law='non-resident on the scale (Arts. 44-II-2°, 847, 116)')
reg(9148201, 'TD Taxable Income - Annualised', 'simple_tax_post_formula', 'flat', SCALE,
    [band(ee=100, formula='MULTIPLY($band_amount_raw;$period_divisor)', deb='58110')], [('58552', '', 'Yes')],
    'As the Dev: 58552 × period divisor into 58110. Pre-condition SCALE instead of the Dev NOT(EQUALS($58218;4)) so that 58110–58112 stay 0 for the exempt (disabled, Art. 3-4°), as in v5 — the reports must not read a tax for someone who owes none. Irregular payments are annualised with the month (A26: method depends on the DGI barème, Art. 847).',
    v5src='9148072 (split)')
reg(9148211, 'TD Taxable Income - Annual Tax', 'simple_tax_monthly', 'differential', '',
    [band(f=0, t=800000, ee=0, deb='58111'), band(f=800000, t=6000000, ee=10.5, deb='58111'),
     band(f=6000000, t=7500000, ee=15, deb='58111'), band(f=7500000, t=9000000, ee=20, deb='58111'),
     band(f=9000000, t=12000000, ee=25, deb='58111'), band(f=12000000, t=9999999999999, ee=30, deb='58111')],
    [('58110', '', 'Yes')],
    f'As the Dev: annual scale on 58110 (`_monthly`: bands not divided), result 58111. CGI Art. 1-IV (p. 14; LF 2026 Art. 3). {DL}: limits at the round figure (incomeTo 800,000 = next incomeFrom) — the tax starts at the 800,001st franc; the Dev\'s `x.99` limits give 1 XAF less at a half franc.',
    v5src='9148072 (split)', law='band limits per Art. 1-IV')
reg(9148221, 'TD Taxable Income - Period Tax', 'simple_tax_post_formula', 'flat', NOT_DIPLO,
    [band(ee=100, formula='DIVIDE($band_amount_raw;$period_divisor)', deb='58112')], [('58111', '', 'Yes')],
    'As the Dev: annual tax ÷ period divisor into 58112.', v5src='9148072 (split)')
reg(9148231, 'TD Taxable Income - Period Tax - Resident', 'simple_tax_$$_post_formula', 'flat', RESIDENT_SCALE,
    [band(ee=100, formula=R_IRPP, deb='2610', cred='2552')], [('58112', '', 'Yes')],
    f'As the Dev: FLOOR(ADD(x;0.5)) on 58112 (technical convention, no rule in the CGI), `_$$`, 2610/2552. {DL}: pre-condition with the Art. 3-4° test (58226: real-regime employer, start date, ≤ 60 months, under 35 at recruitment, young graduate or worker); disabled (Art. 45-18°) and diplomatic (Art. 3-2°) out.',
    v5src='9148073', law='Art. 3-4° conditions')
reg(9148241, 'TD Taxable Income - Period Tax - Non-Resident', 'simple_tax_$$_post_formula', 'flat', NR_SCALE,
    [band(ee=100, formula=R_IRPP, deb='2610', cred='2592')], [('58112', '', 'Yes')],
    f'As the Dev: ID, rule group, rounding, 2610/2592. {DL}: 100% of the scale result 58112, not 18% (CGI Arts. 44-II-2°, 847; Art. 116 only for Art. 2-VI and Art. 60).',
    v5src='9148075', law='non-resident on the scale')
reg(9148251, 'TD Apprenticeship Tax', 'simple_tax_post_formula', 'flat', NOT_DIPLO,
    [band(er=1.2, formula=f'MULTIPLY(FLOOR(DIVIDE(ADD(MULTIPLY($band_amount_raw;{RF});5);10));10)', deb='6034', cred='2534')],
    [('58534', '', 'Yes')],
    f'As the Dev: 12‰ (Art. 178), rounding to the nearest 10 (Art. 177), 6034/2534. {DL}: relief 50% / 100% (58206; CGI Art. 158 « 50% de la taxe d’apprentissage »; LF 2020 Art. 14).',
    v5src='9148084', law='TA relief (Art. 158)')
reg(9148261, 'TD Lump Sum Tax', 'simple_tax_post_formula', 'flat', NOT_DIPLO,
    [band(er=7.5, formula=f'FLOOR(ADD(MULTIPLY($band_amount_raw;{RF});0.5))', deb='6063', cred='2563')], [('58563', '', 'Yes')],
    f'As the Dev: 7.5% (Art. 190), 6063/2563. {DL}: relief 0 / 50% / 100% (58206; Art. 158; the Dev only has the total exemption) and payment to the whole franc, FLOOR(x+0.5) — technical payment convention (Art. 190 has no rounding rule).',
    v5src='9148083', law='TF 50% relief (Art. 158)')
reg(9148271, 'TD Food Security Levy (PSA)', 'simple_tax_$$_monthly', 'flat', f'AND({NOT_DIPLO};GREATER($58105;0))',
    [band(ee=100, floor=400, ceil=400, deb='2610', cred='2570')], [('58105', '', 'Yes')],
    f'Additional regulation (no Dev pair), Dev pattern (floor = ceiling, `_monthly`, as 9148009). {DL}: CGI Arts. 837–839 (p. 166) — 400 FCFA a month per employee, employee deduction, recovered as IRPP. Liability 2570, new WTC code (R17).',
    v5src='9148091', law='PSA (Arts. 837–839)')


# ---------------------------------------------------------------- SKILL.md writer
def num(v):
    if v == '' or v is None:
        return ''
    return f'{v:,.3f}'


def write_skill():
    L = ['---', 'name: "chad-design-blueprint-claude-v6"',
         'description: "Chad (TD) payroll regulation design v6 — the v5 rules (CGI 2026, CNPS decrees and guide, two QA rounds) in the form of the development team\'s td_2026 design: same regulation IDs, names, ordinals, rule groups, accounts and formula conventions wherever the law allows; each remaining difference is marked Deliberate divergence (law). Design Blueprint format, tax year td_2026."',
         '---', '',
         '> **Analysis instructions:** read and follow `Regulation_Design_Analysis_Engine.md` before interpreting or computing any regulation below.', '',
         '> **Companions:** `CHANGELOG.md` — v5 → v6 changes of form, regulation by regulation (and the v4 → v5 history) · `ASSUMPTIONS.md` — decisions taken, alternatives and what is still not settled · `RESEARCH_GAPS.md` — what compliance must fix · `VALIDATION.md` — the scenarios executed: v6 = v5, value by value.', '',
         '> **Source of every article cited:** Code Général des Impôts du Tchad 2026, DGI edition (`raw/docs/oficiais/TD/2026-11-01-CGI-TCHAD-2026-FINAL-dgi.pdf`, md5 139d5326…); LF 2024–2026 where the CGI says so; CNPS: Dec. 1635 and 1636/PR/PM/MFPT/2009 and the CNPS Guide de l’employeur 2019 (`raw/docs/oficiais/TD/2026-11-01-*`).', '',
         '# 0 - Flags', '', '| Account | Flag | Formula | Values |', '| --- | --- | --- | --- |']
    for a, n, f, v in FLAGS:
        L.append(f'| {a} | {n} | `{f}` | {v} |')
    L += ['', 'Flags of the Dev reused where they cover the case: 58218 (`$hr.employee_type`) and 58205 (Dev formula) as the Dev; 58206 (relief 0 / 1 / 2 — the Dev field is 0 / 1: Deliberate divergence (law), Art. 158 50%) and 58212 (children, not all dependants — Deliberate divergence (law), Art. 45-4°) keep the Dev number with the field the law needs; the others have no Dev equivalent (ASSUMPTIONS A14). 58219 and 58226 are derived from the other flags. 58201 is reserved for advanced reconciliation and is not used.', '', '---', '']
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
    e = e.replace('$period_divisor', repr(float(PERIODS)))
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
        if r['ttype'].lower() == 'differential':
            tot = 0.0
            ann = base if monthly else base * periods      # `_monthly`: the base is already annual (Dev: 58110)
            for i, b in enumerate(r['bands']):
                lo = r['bands'][i - 1]['t'] if i > 0 else 0
                if ann > lo:
                    tot += (min(ann, b['t']) - lo) * b['ee'] / 100
            A[r['bands'][0]['deb']] = A.get(r['bands'][0]['deb'], 0) + (tot if monthly else tot / periods)
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
    ('5 Individual severance 900,000', {'62100': 300000, '62180': 900000}, {}, (10500, 208600, 90000, 3600, 400, 980500)),   # v6 r3: TFE on 1,200,000 (Art. 189-1°)
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
    ('E21 Arrears of car fuel benefit 65521 50,000 -> vehicle cap 30,000 in IRPP; real value in TF/TA and CNPS (v6 r2, QA V1)', {'62100': 300000, '65521': 50000}, {}, (12250, 26364, 26250, 4200, 400, 260986)),
    ('E22 Arrears of base salary 62101 100,000 on base 450,000 -> taxed in the month paid (no retro_, QA V2)', {'62100': 450000, '62101': 100000}, {}, (17500, 50375, 41250, 6600, 400, 481725)),
    ('E23 Medical insurance 62610 50,000 -> taxable everywhere (verdict 25; v6 r3, QA W1)', {'62100': 300000, '62610': 50000}, {}, (12250, 28464, 26250, 4200, 400, 308886)),
    ('E24 Social allowance 62651 20,000 -> taxable everywhere (Art. 44-I; v6 r3, QA W1)', {'62100': 300000, '62651': 20000}, {}, (11200, 25424, 24000, 3840, 400, 282976)),
    ('E25 Statutory EOS gratuity 62900 100,000 -> IRPP and TF; out of CNPS and TA (v6 r3, QA W2)', {'62100': 300000, '62900': 100000}, {}, (10500, 33898, 30000, 3600, 400, 355202)),
    ('E26 Phone cash benefit 65610 20,000 -> IRPP, CNPS, TF and TA (v6 r3, sweep)', {'62100': 300000, '65610': 20000}, {}, (11200, 25424, 24000, 3840, 400, 262976)),
]
# the only cases where v6 must differ from v5 — matrix fixes after the v6 QA (v5 also affected)
V1_CASES = {'5': 'r3 W2: severance in the TF base', 'E21': 'r2 V1: car fuel arrears 6552%', 'E23': 'r3 W1: medical insurance 6261%',
            'E24': 'r3 W1: social allowance 6265%', 'E25': 'r3 W2: EOS gratuity out of the TA', 'E26': 'r3 sweep: cash-in-lieu 6561x in TF/TA'}
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


KEYS = ['58103', '58172', '58112', '58105', '58008', '58130', '58550', '58563', '58534', '58104', '58108', '58107', '58113', '58114', '58115', '58100', '58101',
        '58552', '58592', '58120', '58121', '58122', '58123', '58124', '58125', '58126', '58127', '58128', '58106', '58131',
        '2551', '2550', '2537', '2560', '2552', '2592', '2563', '2534', '2570']


def against_v5():
    import importlib.util
    sys.dont_write_bytecode = True
    spec = importlib.util.spec_from_file_location('v5', V5_BUILD)
    v5 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(v5)
    assert [s[:3] for s in v5.SCEN + v5.EXTRA] == [s[:3] for s in SCEN + EXTRA][:len(v5.SCEN + v5.EXTRA)], 'same cases as v5 (v6 adds E21, E22)'
    bad, n, v1 = [], 0, []
    for name, inp, fo, exp in SCEN + EXTRA:
        f6 = dict(RES); f6.update(fo)
        f5 = dict(v5.RES); f5.update(fo)
        A6, A5 = run(inp, f6), v5.run(inp, f5)
        for k in KEYS:
            n += 1
            d = abs(A6.get(k, 0) - A5.get(k, 0)) > 0.005
            if d and name.split()[0] in V1_CASES:
                v1.append((name.split()[0], k, A5.get(k, 0), A6.get(k, 0)))
            elif d:
                bad.append((name, k, A5.get(k, 0), A6.get(k, 0)))
        # 58110 / 58111 have no v5 account: check them against v5 58552 and 58112
        if name.split()[0] in V1_CASES:
            continue
        if A6.get('58112', 0) or A5.get('58112', 0):
            n += 2
            if abs(A6.get('58110', 0) - 12 * A5.get('58552', 0)) > 0.005 or abs(A6.get('58111', 0) - 12 * A5.get('58112', 0)) > 0.01:
                bad.append((name, '58110/58111', A5.get('58552', 0), A6.get('58110', 0)))
        elif A6.get('58110', 0) or A6.get('58111', 0):
            bad.append((name, '58110/58111 not 0 for an exempt employee', 0, A6.get('58110', 0)))
    return n, bad, len(v5.R), v1


def retro_effect():
    # arrears of 100,000 for a month paid 300,000, paid in a month of 900,000: payment basis (v6) vs re-run of the original month
    _, A_cash = outcome({'62100': 900000, '62101': 100000}, {})
    _, A_orig0 = outcome({'62100': 300000}, {})
    _, A_orig1 = outcome({'62100': 300000, '62101': 100000}, {})
    _, A_cur = outcome({'62100': 900000}, {})
    g = lambda A, k: A.get(k, 0)
    irpp = lambda A: g(A, '2552') + g(A, '2592')
    return dict(cash_irpp=irpp(A_cash), retro_irpp=irpp(A_orig1) - irpp(A_orig0) + irpp(A_cur),
                cash_cnps=g(A_cash, '2551'), retro_cnps=g(A_orig1, '2551') - g(A_orig0, '2551') + g(A_cur, '2551'))


WTC_XLSX = os.path.join(os.path.dirname(HERE), '2026-10-29-teste-design-hrblizz', '2026-10-30-export-ram', 'CHAD-WTC_V3.0-export-2026-11-01.xlsx')


def sweep():
    """Every WTC V3.0 Earning code through the engine (300,000 + 10,000 of the code): in which bases does it land? (v6 QA W1)"""
    import openpyxl
    wb = openpyxl.load_workbook(WTC_XLSX, read_only=True, data_only=True)
    base = run({'62100': 300000}, dict(RES))
    keys = ['58008', '58130', '58534', '58563']          # IRPP, CNPS, TA, TF
    none, diff, n = [], [], 0
    for r in wb['Wage Type Catalogue'].iter_rows(min_row=2, values_only=True):
        if r[0] is None or r[4] != 'Earning':
            continue
        n += 1
        c = str(int(r[0])) if isinstance(r[0], (int, float)) else str(r[0])
        A = run({'62100': 300000, c: 10000} if c != '62100' else {'62100': 310000}, dict(RES))
        ours = ['Y' if abs(A.get(k, 0) - base.get(k, 0)) > 0.5 else 'N' for k in keys]
        wtc = [str(x)[:1] for x in (r[10], r[11], r[12], r[13])]   # Tax, CNPS, Apprenticeship, Lump-Sum
        if ours == ['N'] * 4:
            none.append(f'{c} {r[1]} (WTC {"/".join(wtc)})')
        if ours != wtc:
            diff.append(f'{c} {r[1]}: ours {"/".join(ours)} · WTC {"/".join(wtc)}')
    L = [f'Earning codes swept: {n} (columns IRPP/CNPS/TA/TF)', f'In no base at all: {len(none)}'] + ['  ' + x for x in none] +         [f'Different from the WTC V3.0 columns: {len(diff)} (each group is a documented decision — VALIDATION.md, sweep table)'] + ['  ' + x for x in diff]
    with open(os.path.join(HERE, 'SWEEP-run.txt'), 'w', encoding='utf-8', newline=chr(10)) as fh:
        fh.write(chr(10).join(L) + chr(10))
    return n, none, diff


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
    n5, diff5, nr5, v1 = against_v5()
    out.append(f'v6 vs v5 engine: {len(SCEN) + len(EXTRA)} cases x {len(KEYS)} accounts (+ 58110/58111 checks) = {n5} values compared, {len(diff5)} unexpected differences' + ('' if not diff5 else ': ' + repr(diff5[:5])))
    out.append('expected differences (QA V1 fix, v5 also affected): ' + '; '.join(f'{c} {k}: v5 {a:,.0f} -> v6 {b:,.0f}' for c, k, a, b in v1))
    re_ = retro_effect()
    out.append(f"retro_ effect (arrears 100,000 for a 300,000 month, paid in a 900,000 month): IRPP payment basis {re_['cash_irpp']:,.0f} vs re-run of the original month {re_['retro_irpp']:,.0f}; EE CNPS {re_['cash_cnps']:,.0f} vs {re_['retro_cnps']:,.0f}")
    out.append(f'regulations: v6 {len(R)} · v5 {nr5}')
    ns, none, dif = sweep()
    out.append(f'sweep of the WTC V3.0 Earning codes: {ns} codes, {len(none)} in no base (relocation 2 / 6256x reimbursements, A22), {len(dif)} different from the WTC columns (SWEEP-run.txt)')
    bad += len(diff5)
    txt = '\n'.join(out)
    print(txt)
    with open(os.path.join(HERE, 'VALIDATION-run.txt'), 'w', encoding='utf-8', newline='\n') as fh:
        fh.write(txt + '\n')
    sys.exit(0 if not bad else 1)
