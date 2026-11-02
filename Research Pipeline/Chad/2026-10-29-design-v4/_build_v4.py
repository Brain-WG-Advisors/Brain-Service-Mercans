"""Chad design v4 — generator and executable validation.

Builds chad-design-blueprint-claude-v4/SKILL.md from the regulation data below and
runs the regulations, as written, on the scenarios of v3 VALIDATION.md.
Run:  python -I _build_v4.py   (writes SKILL.md and prints the validation table)
"""
import math, os, sys

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'chad-design-blueprint-claude-v4')

# ---------------------------------------------------------------- flags
FLAGS = [
    ('58218', 'Status (global flag)',
     "IF(EQUALS($hr.residency_status::key;'NRES');1;IF(EQUALS($hr.residency_status::key;'DISABLED');2;IF(EQUALS($hr.residency_status::key;'YOUNG-GRAD');3;IF(EQUALS($hr.residency_status::key;'DIPLO');4;0))))",
     '0 resident · 1 non-resident · 2 disabled · 3 young graduate · 4 diplomatic — catalogue numbering; routing uses `LESS($58218;1)` for residents, never an equality test against zero'),
    ('58202', 'CNPS PVID eligible', "IF(EQUALS($hr.cnps_eligibility_pvid::key;'Y');1;2)", '1 yes · 2 no'),
    ('58203', 'CNPS PFM eligible', "IF(EQUALS($hr.cnps_eligibility_pfm::key;'Y');1;2)", '1 yes · 2 no'),
    ('58204', 'CNPS AT/MP eligible', "IF(EQUALS($hr.cnps_eligibility_atmp::key;'Y');1;2)", '1 yes · 2 no'),
    ('58205', 'Young-graduate months consumed',
     'ADD(FLOOR(DIVIDE(DAYS_BETWEEN($hr.young_graduate_employee_exemption_start_date;$period.end_date);30.4375));1)',
     'months since the exemption start, current month included; exemption while ≤ 60 (read by the IRPP-TS report)'),
    ('58206', 'TFE / TAFP relief (entity)',
     "IF(EQUALS($legal_entity_hr.tfe_tafp_relief::key;'100');1;IF(EQUALS($legal_entity_hr.tfe_tafp_relief::key;'50');2;0))",
     '0 none · 1 exempt (new companies, LF 2024) · 2 50% (CGI Art. 158) — **entity field**'),
    ('58207', 'Transport allowance granted to all staff', "IF(EQUALS($legal_entity_hr.transport_uniform::key;'Y');1;2)", '1 yes · 2 no — **new entity field**, default 1'),
    ('58210', 'Plan social (collective redundancy)', "IF(EQUALS($hr.termination_plan_social::key;'Y');1;2)", '1 yes · 2 no — **new DD field**'),
    ('58212', 'Dependent children', '$hr.number_of_dependent_children', 'count — reporting only (DAS)'),
]

NOT_DIPLO = 'NOT(EQUALS($58218;4))'
RESIDENT_SCALE = 'OR(LESS($58218;1);AND(EQUALS($58218;3);GREATER($58205;60)))'
NR = 'EQUALS($58218;1)'
TFE_POP = 'AND(NOT(EQUALS($58218;1));NOT(EQUALS($58218;4)))'

# ---------------------------------------------------------------- matrices (code by code, as v3)
CASH_GROSS = [('62104', '', 'No'), ('62550', '', 'No'), ('62551', '', 'No'), ('62552', '', 'No'), ('62560', '', 'No'), ('62561', '', 'No'),
              ('62562', '', 'No'), ('62563', '', 'No'), ('62570', '', 'No'),
              ('62199', '621%%', 'Yes'), ('62299', '622%%', 'Yes'), ('62399', '623%%', 'Yes'), ('62499', '624%%', 'Yes'), ('62599', '625%%', 'Yes'),
              ('62639', '6263%', 'Yes'), ('62650', '', 'Yes'), ('62669', '6266%', 'Yes'), ('62799', '627%%', 'Yes'), ('62867', '', 'Yes'),
              ('62879', '6287%', 'Yes'), ('62889', '6288%', 'Yes'), ('62890', '', 'Yes'), ('62999', '629%%', 'Yes'), ('65519', '6551%', 'Yes'),
              ('65619', '6561%', 'Yes'), ('65669', '6566%', 'Yes'), ('65799', '657%%', 'Yes'), ('79499', '794%%', 'Yes')]
BIK_REAL = [('65610', '', 'No'), ('65611', '', 'No'), ('65612', '', 'No'), ('65660', '', 'No'), ('65661', '', 'No'), ('65662', '', 'No'),
            ('62670', '', 'Yes'), ('62680', '', 'Yes'), ('65299', '652%%', 'Yes'), ('65499', '654%%', 'Yes'), ('65509', '6550%', 'Yes'),
            ('65520', '', 'Yes'), ('65699', '656%%', 'Yes'), ('65899', '658%%', 'Yes')]
TFE_BASE = [('62104', '', 'No'), ('62180', '', 'No'), ('62181', '', 'No'), ('62182', '', 'No')] + CASH_GROSS[1:] + BIK_REAL
CNPS_GROSS = [(a, '', 'No') for a in ['62104', '62180', '62181', '62182', '62540', '62541', '62542', '62550', '62551', '62552', '62560', '62561',
                                      '62562', '62563', '62570', '62760', '62762', '62900', '62910', '62920', '62930', '65570', '65571', '65572',
                                      '65580', '65581', '65582']] + \
             [('62199', '621%%', 'Yes'), ('62299', '622%%', 'Yes'), ('62399', '623%%', 'Yes'), ('62499', '624%%', 'Yes'), ('62599', '625%%', 'Yes'),
              ('62639', '6263%', 'Yes'), ('62650', '', 'Yes'), ('62669', '6266%', 'Yes'), ('62670', '', 'Yes'), ('62680', '', 'Yes'),
              ('62799', '627%%', 'Yes'), ('62879', '6287%', 'Yes'), ('62890', '', 'Yes'), ('62999', '629%%', 'Yes'), ('65299', '652%%', 'Yes'),
              ('65499', '654%%', 'Yes'), ('65599', '655%%', 'Yes'), ('65699', '656%%', 'Yes'), ('65799', '657%%', 'Yes'), ('65899', '658%%', 'Yes'),
              ('79499', '794%%', 'Yes'), ('58104', '', 'Yes')]

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
    'Cash earnings subject to IRPP (Art. 44); base of the Art. 46 limits. **58105 is the account the DAS report reads** (gross vs the 58106 limit).')
reg(9148013, 'TD Annual Reporting Limit', 'retro_simple_tax_monthly', 'Flat', '', [band(ee=100, floor=60000, ceil=60000, deb='58106')],
    [('58105', '', 'Yes')],
    'Fixed 60,000 XAF a month (Floor = Ceiling, `_monthly`), written only when the employee has cash gross. Read by the DAS report to split employees above / at or below 60,000 XAF.')
reg(9148014, 'TD Limits on Base Salary', 'retro_simple_tax', 'Flat', '',
    [band(ee=30, deb='58171'), band(ee=3.5, deb='58172')], [('58109', '', 'Yes')],
    'Derived limits in their own regulation, applied downstream as ceiling accounts (rulebook §5 · reunião 16/10, Suman): 58171 = 30% of base salary (Art. 45-13°, transport) · 58172 = 3.5% of base salary (Art. 47, retirement). One regulation: same base, two bands.')
reg(9148015, 'TD Limits on Cash Remuneration — Benefits in Kind', 'retro_simple_tax', 'Flat', '',
    [band(ee=b[3], ceil=(b[4] * 12 if b[4] else ''), deb=b[2]) for b in BIK], [('58105', '', 'Yes')],
    'Art. 46-III (LF 2019) caps, one band per benefit, all on the cash remuneration 58105: housing 20 · vehicle 10 · food 15 (and 75,000 XAF a month, stated annually as the band ceiling) · furnishings 5 · domestic 4 · electricity 4 · water 4 · telephone 3 · gas 2. Read as ceiling accounts by 9148031–9148039.')
reg(9148021, 'TD Transport Allowance — Exempt Portion', 'retro_simple_tax', 'Flat', '',
    [band(ee=100, ceilacc='58171', assertion='EQUALS($58207;1)', deb='99999', cred='58104')], [('62529', '6252%', 'Yes')],
    'Art. 45-13°: exempt up to 30% of base salary when granted to all staff (58207). Limit from 58171 as the ceiling account. Credit side → 58104 negative; subtracts in the taxable and CNPS bases (not in TFE/TAFP, Art. 189). 58104 is read by the DAS report.')
reg(9148022, 'TD Family Allowance — Exempt', 'simple_tax', 'Flat', '', [band(ee=100, deb='99999', cred='58108')],
    [('62759', '6275%', 'Yes'), ('62769', '6276%', 'Yes')],
    'CGI Art. 45: family allowances exempt from IRPP in full; no per-child cap in Chadian law (the 5,000 XAF wording is the Congo-Brazzaville CGI, Art. 38-2°). Negative in 58108, read by the DAS report.')
reg(9148023, 'TD Plan-Social Severance — Exempt Portion', 'simple_tax', 'Flat', 'EQUALS($58210;1)', [band(ee=100, deb='99999', cred='58113')],
    [('62189', '6218%', 'Yes')], 'Art. 45-10°: severance under a collective-redundancy plan is fully exempt. Individual severance stays taxable. Negative in 58113.')
for i, b in enumerate(BIK):
    cap = f'{b[3]}% of the cash remuneration' + (' and 75,000 XAF a month' if b[4] else '')
    reg(9148031 + i, f'TD BIK {b[1]} — Capped Value for IRPP', 'retro_simple_tax', 'Flat', '',
        [band(ee=100, ceilacc=b[2], deb=b[0])], b[5],
        f'CGI Art. 46-III (LF 2019): « plafonnés » — IRPP takes the real value, capped at {cap} (limit {b[2]}, ceiling account). CNPS, TFE and TAFP take the real value. {b[0]} is the account the DAS report reads.')
reg(9148041, 'TD IRPP Gross', 'simple_tax', 'Flat', NOT_DIPLO, [band(ee=100, deb='58008')],
    [('58105', '', 'Yes')] + [(b[0], '', 'Yes') for b in BIK] + [(a, '', 'No') for a in ['65853', '65854', '65855', '65856', '65857']] +
    [('62670', '', 'Yes'), ('62680', '', 'Yes'), ('65299', '652%%', 'Yes'), ('65630', '', 'Yes'), ('65899', '658%%', 'Yes')],
    'Cash gross plus each benefit at its capped value. Benefit codes with no Art. 46 category enter at real value. 58008 is read by the DAS report.')
reg(9148051, 'TD CNPS Gross', 'simple_tax', 'Flat', NOT_DIPLO, [band(ee=100, deb='58130')], CNPS_GROSS,
    'Art. 7 CNPS guide: salaries, indemnities, bonuses and benefits at REAL value; exempt transport (58104) out. Rupture indemnities, family allowance, prime de panier and statutory EOS gratuity outside (WTC). Uncapped; **58130 is the account the CNPS Récapitulatif reads** (months worked, cumulative salary).', 'Social Security')
reg(9148052, 'TD CNPS Insurable Salary', 'retro_simple_tax_period', 'Flat', f'AND({NOT_DIPLO};GREATER($58130;0))',
    [band(ee=100, floor=720000, ceil=6000000, deb='58550', cred='99998')], [('58130', '', 'Yes')],
    'Floor 60,000 / ceiling 500,000 a month, stated annually. Confirmed on 16/10 (Suman): with an empty matrix the floor still applies, so the `GREATER($58130;0)` condition is what keeps a month with no salary out. `_period` + 99998: report-feeding base (Appel Mensuel, DNTS, Récapitulatif).', 'Social Security')
reg(9148053, 'TD CNPS Contributions', 'simple_tax_$$_post_formula', 'Flat', '',
    [band(ee=3.5, formula='FLOOR(ADD($band_amount_raw;0.5))', assertion='EQUALS($58202;1)', deb='2610', cred='2551'),
     band(er=5, formula='FLOOR(ADD($band_amount_raw;0.5))', assertion='EQUALS($58202;1)', deb='6037', cred='2537'),
     band(er=7.5, formula='FLOOR(ADD($band_amount_raw;0.5))', assertion='EQUALS($58203;1)', deb='6020', cred='2550'),
     band(er=4, formula='FLOOR(ADD($band_amount_raw;0.5))', assertion='EQUALS($58204;1)', deb='6040', cred='2560'),
     band(ee=3.5, formula='FLOOR(ADD($band_amount_raw;0.5))', assertion='EQUALS($58202;1)', deb='99999', cred='58141'),
     band(ee=100, formula='20', deb='58131')],
    [('58550', '', 'Yes')],
    'One regulation, one base, all branches as bands (rulebook §5). PVID 3.5% EE + 5% ER, PFM 7.5%, AT/MP 4%, each gated by its eligibility flag. Band 5: negative copy of the EE share for the IRPP deduction. Band 6: total rate 20 in 58131, read by the CNPS Récapitulatif (expected annual contribution) — the report percentages live in the design (Mohit, 16/10). `_$$`: the EE share is gross-up eligible (Suman, 16/10). GL pairs: EE 2551 / ER 2550 coherent pair as on 16/10; the report specs map them the other way round (research gap R13).', 'Social Security')
reg(9148061, 'TD Supplementary Retirement — Deductible Portion', 'retro_simple_tax', 'Flat', '',
    [band(ee=100, ceilacc='58172', deb='99999', cred='58142')],
    [('21610', '', 'No'), ('21611', '', 'No'), ('21670', '', 'No'), ('21699', '216%%', 'Yes')],
    'Art. 47 CGI: compulsory employee retirement contributions deductible up to 3.5% of base salary — limit 58172 as the ceiling account. Negative in 58142.')
reg(9148071, 'TD IRPP Taxable Income', 'simple_tax', 'Flat', NOT_DIPLO, [band(ee=100, deb='58552')],
    [(a, '', 'Yes') for a in ['58008', '58104', '58108', '58113', '58141', '58142']],
    'IRPP gross less the exempt portions, the EE CNPS share and the deductible retirement contribution — negatives summed in the matrix (Art. 47). **58552 is the account the IRPP-TS and DAS reports read** (residents, young graduates and disabled alike), so it runs for every status except diplomatic.')
reg(9148072, 'TD IRPP-TS — Resident Scale', 'retro_simple_tax', 'Differential', RESIDENT_SCALE,
    [band(f=0, t=800000.99, ee=0, deb='58152'), band(f=800001, t=6000000.99, ee=10.5, deb='58152'),
     band(f=6000001, t=7500000.99, ee=15, deb='58152'), band(f=7500001, t=9000000.99, ee=20, deb='58152'),
     band(f=9000001, t=12000000.99, ee=25, deb='58152'), band(f=12000001, t=9999999999999, ee=30, deb='58152')],
    [('58552', '', 'Yes')],
    'Art. 1-IV CGI, annual bands auto-divided by the period; last band closed (Suman, 16/10: an open last band takes nothing). Resident (58218 = 0), or young graduate past 60 months (58205 > 60).')
reg(9148073, 'TD IRPP-TS — Resident Withholding', 'simple_tax_$$_post_formula', 'Flat', RESIDENT_SCALE,
    [band(ee=100, formula='FLOOR(ADD($band_amount_raw;0.5))', deb='2610', cred='2552')], [('58152', '', 'Yes')],
    'Rounded once, on the total, to the whole XAF. `_$$`: gross-up eligible (Suman, 16/10). 2552 read by IRPP-TS and DAS.')
reg(9148074, 'TD Non-Resident Tax Base', 'simple_tax_period', 'Flat', NR, [band(ee=100, deb='58592', cred='99998')],
    [(a, '', 'Yes') for a in ['58105', '58104', '58108', '58113']],
    'Art. 116: 18% on the remuneration paid, net of the amounts Art. 45 exempts. Report-feeding base (IRPP-TS reads 58592).')
reg(9148075, 'TD IRPP — Non-Resident 18%', 'simple_tax_$$_post_formula', 'Flat', NR,
    [band(ee=18, formula='FLOOR(ADD($band_amount_raw;0.5))', deb='2610', cred='2592')], [('58592', '', 'Yes')],
    'Flat 18%, final. `_$$` as for residents. Disabled (2), young graduate within 60 months (3) and diplomatic (4) run neither 9148073 nor 9148075; CNPS still applies to 2 and 3.')
reg(9148081, 'TD TFE Base', 'simple_tax_period', 'Flat', TFE_POP, [band(ee=100, deb='58563', cred='99998')], TFE_BASE,
    'Art. 189: gross salaries, indemnities, allowances and gratifications, and benefits at REAL value. No Art. 45 carve-out: exempt transport and family allowances stay in. Severance (damages in nature) out. TFE report reads 58563.')
reg(9148082, 'TD TAFP Base', 'simple_tax_post_formula_period', 'Flat', TFE_POP,
    [band(ee=100, formula='MULTIPLY(FLOOR(DIVIDE($band_amount_raw;1000));1000)', deb='58534', cred='99998')], TFE_BASE,
    'Same base as TFE (Art. 173, Art. 189). Fraction below 1,000 XAF dropped (CCG, Art. 177). TAFP report reads 58534.')
reg(9148083, 'TD TFE — Employer Lump-Sum Tax', 'simple_tax_post_formula', 'Flat', '',
    [band(er=7.5, formula='FLOOR(ADD(MULTIPLY($band_amount_raw;IF(EQUALS($58206;1);0;IF(EQUALS($58206;2);0.5;1)));0.5))', deb='6063', cred='2563')],
    [('58563', '', 'Yes')], 'Art. 190, 7.5%. Reduced by 50% (CGI Art. 158) or exempt (LF 2024) per entity flag 58206.')
reg(9148084, 'TD TAFP — Apprenticeship & Training Tax', 'simple_tax_post_formula', 'Flat', '',
    [band(er=1.2, formula='MULTIPLY(FLOOR(DIVIDE(ADD(MULTIPLY($band_amount_raw;IF(EQUALS($58206;1);0;IF(EQUALS($58206;2);0.5;1)));5);10));10)', deb='6034', cred='2534')],
    [('58534', '', 'Yes')], 'Art. 178, 12‰, rounded to the nearest 10 XAF. Same relief as TFE (58206).')


# ---------------------------------------------------------------- SKILL.md writer
def num(v):
    if v == '' or v is None:
        return ''
    return f'{v:,.3f}'


def write_skill():
    L = ['---', 'name: "chad-design-blueprint-claude-v4"',
         'description: "Chad (TD) payroll regulation design v4 — built by Claude from CCG v1.2, WTC v1.2 (compliance sheet), DD v1.0 and the 7 report specs, applying KB_Design_Rulebook_v4 and the answers of the 16 Oct 2026 design call. Design Blueprint format, tax year td_2026."',
         '---', '',
         '> **Analysis instructions:** read and follow `Regulation_Design_Analysis_Engine.md` before interpreting or computing any regulation below.', '',
         '> **Companions:** `CHANGELOG.md` — what changed from v3 and which rule drove it · `ASSUMPTIONS.md` — what is still not settled · `RESEARCH_GAPS.md` — what compliance must fix · `VALIDATION.md` — the scenarios executed.', '',
         '# 0 - Flags', '', '| Account | Flag | Formula | Values |', '| --- | --- | --- | --- |']
    for a, n, f, v in FLAGS:
        L.append(f'| {a} | {n} | `{f}` | {v} |')
    L += ['', 'Flags take the meaning the global catalogue gives them: 58218 status, 58205 young-graduate months, 58206 TFE relief, 58212 dependants. 58201 is reserved for advanced reconciliation and is not used.', '', '---', '']
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


# ---------------------------------------------------------------- engine (as the analysis file describes)
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


def run(inputs, flags, periods=12):
    A = {k: float(v) for k, v in flags.items()}
    for r in R:
        if r['pre'] and not ev(r['pre'], A):
            continue
        vals = dict(inputs)
        vals.update({k: v for k, v in A.items() if len(k) == 5 and k.startswith('58')})
        base = matrix_sum(r['matrix'], vals)
        monthly = '_monthly' in r['trg']
        div = 1 if monthly else periods
        if r['ttype'] == 'Differential':
            tot = 0.0
            ann = base * periods
            for b in r['bands']:
                lo = (b['f'] - 1 if b['f'] else 0) if b['f'] != 0 else 0
                lo = r['bands'][r['bands'].index(b) - 1]['t'] if r['bands'].index(b) > 0 else 0
                hi = b['t']
                if ann > lo:
                    tot += (min(ann, hi) - lo) * b['ee'] / 100
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


RES = dict(**{'58218': 0, '58202': 1, '58203': 1, '58204': 1, '58205': 0, '58206': 0, '58207': 1, '58210': 2, '58212': 0})

# (name, inputs, flag overrides, v3 expected EE CNPS, IRPP, TFE, TAFP, Net)
SCEN = [
    ('1 Active baseline 350,000', {'62100': 350000}, {}, (12250, 28464, 26250, 4200, 309286)),
    ('9 Zero salary', {}, {}, (0, 0, 0, 0, 0)),
    ('10 13th month', {'62100': 350000, '62200': 350000}, {}, (17500, 75750, 52500, 8400, 606750)),
    ('Housing real 50,000 under a 120,000 cap', {'62100': 600000, '65400': 50000}, {}, (17500, 65750, 48750, 7800, 516750)),
    ('Individual severance 900,000', {'62100': 300000, '62180': 900000}, {}, (10500, 208600, 22500, 3600, 980900)),
    ('Supplementary pension 30,000 (cap 14,000)', {'62100': 400000, '21610x': 0, '21600': 30000}, {}, (14000, 32060, 30000, 4800, 323940)),
    ('Transport 120,000, granted to all', {'62100': 300000, '62520': 120000}, {}, (11550, 26437, 31500, 5040, 382013)),
    ('Family allowance 30,000', {'62100': 300000, '62760': 30000}, {}, (10500, 23397, 24750, 3960, 296103)),
    ('Entity with 50% relief', {'62100': 350000}, {'58206': 2}, (12250, 28464, 13125, 2100, 309286)),
    ('Young graduate, year 3 (month 30)', {'62100': 350000}, {'58218': 3, '58205': 30}, (12250, 0, 26250, 4200, 337750)),
]


def validate():
    rows = []
    allok = True
    for name, inp, fo, exp in SCEN:
        inp = {k: v for k, v in inp.items() if not k.endswith('x')}
        f = dict(RES)
        f.update(fo)
        A = run(inp, f)
        ee = A.get('2551', 0)
        irpp = A.get('2552', 0) + A.get('2592', 0)
        tfe = A.get('2563', 0)
        tafp = A.get('2534', 0)
        cash = sum(v for k, v in inp.items() if k.startswith('62'))
        ded = sum(v for k, v in inp.items() if k.startswith('21'))
        net = cash - ee - irpp - ded
        got = tuple(round(x) for x in (ee, irpp, tfe, tafp, net))
        ok = got == exp
        allok &= ok
        rows.append((name, got, exp, ok, A.get('58106', 0), A.get('58131', 0)))
    # non-resident CCG B: 800,000, CNPS branches off
    f = dict(RES)
    f.update({'58218': 1, '58202': 2, '58203': 2, '58204': 2})
    A = run({'62100': 800000}, f)
    return rows, allok, A


if __name__ == '__main__':
    write_skill()
    rows, ok, nr = validate()
    print('| Scenario | EE CNPS | IRPP | TFE | TAFP | Net | v3 | match | 58106 | 58131 |')
    for n, g, e, k, lim, rate in rows:
        print(f'| {n} | ' + ' | '.join(f'{x:,}' for x in g) + f" | {'=' if k else e} | {'OK' if k else 'DIFF'} | {lim:,.0f} | {rate:,.0f} |")
    print('NR 800,000 (CCG B): 2592 =', round(nr.get('2592', 0)), '| 58592 =', round(nr.get('58592', 0)), '| 2563 =', nr.get('2563', 0))
    print('ALL MATCH' if ok else 'MISMATCH')
    sys.exit(0 if ok else 1)
