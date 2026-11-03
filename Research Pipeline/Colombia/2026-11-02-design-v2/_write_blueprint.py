# -*- coding: utf-8 -*-
"""Writes the co-design-blueprint-v2 package from co_design_v2.json and the validation run (run _build_v2.py first)."""
import os, json, re, collections, sys
sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, 'co-design-blueprint-v2')
VAL = os.path.join(os.path.dirname(HERE), '2026-10-29-validacao-research')
J = json.load(open(os.path.join(HERE, 'co_design_v2.json'), encoding='utf-8'))
S = json.load(open(os.path.join(HERE, '_run-summary.json'), encoding='utf-8'))
RUN = open(os.path.join(HERE, 'VALIDATION-run.txt'), encoding='utf-8').read()
sys.path.insert(0, HERE)
src = open(os.path.join(HERE, '_build_v2.py'), encoding='utf-8').read().split("if __name__ == '__main__':")[0]
B = {'__file__': os.path.join(HERE, '_build_v2.py'), '__name__': '_build_v2'}; exec(compile(src, '_build_v2', 'exec'), B)
REGS = sorted(J['regulations'], key=lambda r: r['ordinal'])
COLNAME = {'N': 'withholding (N)', 'O': 'art. 383 table (O)', 'P': 'non-resident 20% (P)', 'Q': 'health (Q)', 'R': 'solidarity fund (R)',
           'S': 'occupational risk (S)', 'T': 'payroll levies (T)', 'U': 'pension (U)', 'W': 'benefit base (W)', 'X': 'vacation base (X)'}
MATRIX_OF = {'CO Vacation Base': 'X', 'CO Statutory-Benefit Base': 'W', 'CO Gross Earnings': 'every active row', 'CO Salary Payments of the Month': 'V = Salary',
             'CO Pacted Non-Salary Payments': 'V = Non-Salary - pacted', 'CO Contribution Base (IBC) - Health': 'Q', 'CO Payroll-Levy Base': 'T',
             'CO IBC - Pension': 'U', 'CO IBC - Solidarity Fund': 'R', 'CO IBC - Occupational Risk': 'S',
             'CO Taxable Labour Payments (monthly read)': 'N, with R320, R339, R340, R343, R344, R345 false (read by their own regulations)', 'CO Income Tax Flat': 'P'}
H = []
A = H.append


def rules_text(r):
    rs = r['taxabilityRules']
    if not rs: return 'none (formula reads accounts)'
    t = sum(1 for x in rs if x['isTaxable'])
    if all(x['account'][0] != 'R' for x in rs) or len(rs) <= 4:
        return ', '.join(f"`{x['account']}`" for x in rs if x['isTaxable'])
    return f"WTC column {MATRIX_OF.get(r['name'], '?')}: {t} rows true, {len(rs) - t} false (`CO_Taxability_Matrices_v2_0.md`)"


# ------------------------------------------------------------------ Regulation design
A('# CO — Colombia Payroll — Regulation Design v2.0')
A('')
A('**Country:** Colombia (CO) · ISO 3166-1 numeric 170 · Currency **COP** · **Tax year:** 2026 (calendar year)')
A('**Regulation IDs:** `9170000 + ordinal`, the convention of the development team\'s draft regulation for Colombia (`9170132` "CO Income Tax Flat", ordinal 132).')
A('**Design basis:** CO-CCG-001 v1.7, CO-WTC-001 v1.9 (*Wage Type Catalogue*, columns N–X and V), CO-DD-001 v1.6, CO-SIR-001 v1.4, Payslip Generator v1.3 and the report specifications (CO-DIAN-004 v1.3; CO-DIAN-001, CO-DIAN-005, CO-PILA-003, CO-CESANTIAS-006 v1.2; CO-DIAN-002, CO-PILA-007 v1.1), issue of 2 November 2026.')
A('**Machine-readable form:** `co_design_v2.json` (same schema as the development team\'s regulation export: ordinal, taxGroup, taxRuleGroup, taxationType, assertion, bands with formula and debit / credit accounts, taxabilityRules per wage type). Every formula below is the formula in that file.')
A(f"**Executable validation:** the regulations are executed by an engine that reads the JSON ({len(REGS)} regulations; engine semantics in `ASSUMPTIONS.md`). Results: order check 0 defects; {S['cases_v2']} cases / {S['values_v2']} values of an independent calculation written from the statutes - with that calculation's rounding convention, {len(S['shares_diffs'])} differences, each explained; with this design's rounding (one per contributor and fund) and non-taxable income (contributions withheld), the further differences are only those two causes (`VALIDATION.md`); {len(S['extras'])} design checks exact; sweep of the 298 active WTC rows through the engine: 0 differences; column-O check 0; employee / employer coding check 0.")
A('**Method:** clean-room — built from the research artifacts and the primary sources they cite.')
A('')
A('---')
A('')
A('## PART 0 — Special categories (CCG sweep)')
A('')
A('| Category | Disposition (v2.0 regulation) |')
A('|---|---|')
for a, b in [
 ('All-inclusive salary', '`9170009` posts the salary to R303; IBC and levy base 70% (`9170045`, `9170047`; Law 100 of 1993 art. 18; Labour Code art. 132); the Law 1393 excess is added without the 70% (CE SU 25185 of 2021); no transport allowance, no service bonus or severance savings (R303 column W = No).'),
 ('Pacted non-salary payments', '`9170042`–`9170044`: only payments desalarised by written pact enter the 40% test (Law 1393 of 2010 art. 30; CE SU 25185 rule 3); payments non-salary by nature stay out.'),
 ('Art. 114-1 exoneration', '`9170048`: salary payments of the month < 10 SMMLV **and** IBC < 10 SMMLV; removes employer health, SENA and ICBF only (employer band of `9170056`, `9170062`, `9170063`).'),
 ('Apprentices', '`9170011` (support 75% classroom / 100% practical, Labour Code art. 81); IBC never below 1 SMMLV (the floor of `9170045`); classroom phase: no transport allowance (`9170013`), no pension (`RESEARCH_GAPS.md` R2: phase field and the practical-phase split).'),
 ('Employed old-age pensioners', 'Gate `58209` in the pension and solidarity-fund regulations (`9170057`–`9170059`).'),
 ('High-risk pension activity', '`9170054` employer pension rate 22% when `58212 = 1` (Decree-Law 2090 of 2003).'),
 ('Foreign national not affiliated to pension', 'Gate `58211` in the pension and solidarity-fund regulations.'),
 ('Non-residents', '`9170132` "CO Income Tax Flat": 20% on WTC column P (Tax Code art. 408; DIAN Concepto 011108 of 2026 item 10); severance savings and interest outside (Law 100 of 1993 art. 135 par. 3 for every payer, Constitutional Court C-397 of 1994; Decree 1625 art. 1.2.4.1.11). A non-resident who must file applies the art. 206 exemptions in the return (DIAN Concepto 577 of 2020).'),
 ('Contributor type 51', '`9170052`, `9170064`–`9170066` (weekly quarters of the minimum wage; occupational risk on 1 SMMLV; PILA Technical Annex 2 v30).')]:
    A(f'| {a} | {b} |')
A('')
A('## PART 1 — Inputs, flags and constants')
A('')
A('| Account | Meaning | Source |')
A('|---|---|---|')
for k, (m, s) in B['INPUTS'].items():
    A(f'| {k} | {m} | {s} |')
A('')
A('| Constant | Value | Source |')
A('|---|---|---|')
for k, (v, n, s) in B['CONST'].items():
    vv = '; '.join(f'{x[1]} from {x[0]}' for x in v) if isinstance(v, list) else v
    A(f'| {k} {n} | {vv} | {s} |')
A('| (in formulas) | rates and limits written as literals: health 4% / 8.5%, pension 4% / 12% (+10 high risk), solidarity fund 0.5% + 0.5% (+0.2 … +1.0 by band, from 4 SMMLV), occupational-risk class rates 0.522 / 1.044 / 2.436 / 4.350 / 6.960%, CCF 4%, SENA 2%, ICBF 3%, 790 / 1,340 / 3,800 / 2,500 UVT, 25% / 30% / 40%, 32 / 16 / 100 UVT, 204 UVT, art. 383 table | each regulation cites its source in Part 4 |')
A('')
A('## PART 2 — Account register')
A('')
A('| Account | Posted by | Read by |')
A('|---|---|---|')
posted = collections.defaultdict(list); read = collections.defaultdict(set)
for r in REGS:
    for b in r['bands']: posted[b['debitAccount']].append(r['regulationId'])
    vs = set()
    for b in r['bands']: vs |= B['E'].variables(b.get('formula'))
    vs |= B['E'].variables(r.get('assertion'))
    vs |= {t['account'] for t in r['taxabilityRules'] if t['isTaxable']}
    for v in vs: read[re.sub(r'_(raw|ytd)$', '', v)].add(r['regulationId'])
for a in sorted(posted, key=lambda x: (x[0] != 'R', int(x[1:]) if x[0] == 'R' else int(x))):
    A(f"| `{a}` | {', '.join(sorted(set(posted[a])))} | {', '.join(sorted(read.get(a, []))) or 'payslip / reports'} |")
A('')
A('`_raw` = the band amount before the post formula (contributions before the COP 100 rounding feed the non-taxable income); `_ytd` = sum over the prior periods of the calendar year (annual UVT caps).')
A('')
A('## PART 3 — Regulation sequence')
A('')
A('| Ord | ID | Name | Tax group | Tax rule group | Taxation type |')
A('|---|---|---|---|---|---|')
for r in REGS:
    A(f"| {r['ordinal']} | {r['regulationId']} | {r['name']} | {r['taxGroup']} | `{r['taxRuleGroup']}` | {r['taxationType']} |")
A('')
A(f'**{len(REGS)} regulations.** Order rule (checked mechanically): every account a regulation reads is an input, a flag, a constant, or is posted by a lower ordinal. Earnings and payments that feed the bases (vacation, service bonus, severance savings, illness and leave benefits, indemnity) therefore run **before** the bases (ordinals 9–32); the withholding chain runs after the contributions it deducts; the non-resident flat tax keeps the development team\'s ordinal 132, and the totals follow it (139, 141).')
A('')
A('**Contributions.** One regulation per fund, with an employee band (`employeeRate`) and an employer band (`employerRate`), as the development team codes them. The contribution of each contributor and fund is rounded once, up to the next COP 100 (Decree 780 of 2016 art. 3.2.1.5 num. 2: "El valor de los aportes liquidados por cada cotizante … deberá aproximarse al múltiplo de 100 superior más cercano"; PILA AT2 v30 field 47 = IBC × total rate); employee share rounded up, employer share = rounded total − employee share. The non-taxable income uses the contributions withheld from the employee (Tax Code arts. 55, 56: "los aportes obligatorios que efectúen los trabajadores").')
A('')
A('**Rule groups.** Income-tax regulations have no `retro_`, as the development team\'s draft 9170132: Procedure 1 applies the table to the payments made in the month (Decree 1625 of 2016 art. 1.2.4.1.3). Social-security regulations, and the earnings and benefits that feed them, keep `retro_` — **Deliberate divergence (law)**: contributions belong to the period earned, and a retroactive correction is re-filed for that period (PILA Technical Annex 2 v30, planilla N: record A original, record C corrected IBC).')
A('')
A('## PART 4 — Regulation detail')
A('')
A('> Days follow the 30-day convention (Labour Code art. 134). `ROUND` = to the peso, half up; `CEILING(x;1)` = up to the peso; contributions `MULTIPLY(CEILING(DIVIDE($band_amount_raw;100);1);100)` = up to the next COP 100 per contributor and fund (Decree 780 of 2016 art. 3.2.1.5, as substituted by Decree 1990 of 2016 art. 1). No `EQUALS(...;0)` anywhere.')
A('')
for r in REGS:
    A(f"### {r['regulationId']} — {r['name']} (ordinal {r['ordinal']})")
    A('')
    A(f"`{r['taxGroup']}` · `{r['taxRuleGroup']}` · {r['taxationType']}" + (f" · assertion `{r['assertion']}`" if r['assertion'] else ''))
    A('')
    A(f"- **Wage types / accounts:** {rules_text(r)}")
    for b in r['bands']:
        rate = f"rate {b['employeeRate']}%" if b['employeeRate'] is not None else (f"rate from `{b['employeeRateAccount']}`" if b['employeeRateAccount'] else '')
        unit = f"per hours line `{b['unitAccount']}` · " if b['unitAccount'] else ''
        A(f"- **→ `{b['debitAccount']}`** {unit}{rate}" + (f": `{b['formula']}`" if b['formula'] else ''))
    if r['law']: A(f"- **Law:** {r['law']}")
    if r['note']: A(f"- **Note:** {r['note']}")
    if r['divergence'] and r['divergence'].startswith('Deliberate'): A(f"- **{r['divergence'].split(':')[0]}** (see Part 3).")
    A('')
A('## PART 5 — Taxability matrices')
A('')
A('Built mechanically from WTC v1.9 columns N–X (`CO_Taxability_Matrices_v2_0.md`, `CO_Taxability_Perimeters_Extract_v2_0.csv`; 405 rows, 298 active). The WTC has no Mercans codes yet, so every rule is an exact wage-type rule keyed by the WTC row (`R302`); re-key one to one when codes are assigned.')
A('- `Yes/No` has no third state. **Pacted** non-salary rows (54) are false in the IBC matrices and reach the IBC only through the Law 1393 excess (`9170044`) — the sweep confirms the excess for every pacted row. The other **21** `Yes/No` rows (R6, R37, R227, R241–R248, R282, R284–R286, R338, R346 withholding, R349, R350, R353, R358) need a wage-type split at configuration (exempt part / subject part); they are false here.')
A('- **Routing (law):** the statutory service bonus R320 is withheld on its own table read under Procedure 1 and folded into the monthly base under Procedure 2 (`9170073`) (Decree 1625 art. 1.2.4.1.3); the indemnities R339, R340, R343, R344 by Tax Code art. 401-3 / Decree 1625 art. 1.2.4.1.8 (`9170089`) and the retirement bonus R345 by Decree 1625 art. 1.2.4.1.8 (`9170090`); all are false in the monthly read `9170072`. Deduction wage types (R6, R37) carry negative amounts.')
A('- Report-side points (no regulation impact): electronic payroll element of pacted rows AuxilioNS (NIE142) where the pact holds, otherwise AuxilioS (NIE141) (WTC v1.9 column Y); payment method 46 (Transferencia Débito Interbancario) is account-based like 47 where a client adds it to the DD mapper (DD v1.6); PILA occupational-risk rate written as a decimal (`0.0052200`).')
A('')
A('## PART 6 — Open items')
A('')
A('See `RESEARCH_GAPS.md` (statutory and data gaps) and `ASSUMPTIONS.md` (engine semantics to confirm in the production engine).')
A('')
A('## PART 7 — Self-review')
A('')
A(f"- Order check: 0 defects (the v1.2 order had {len(S['v12_order'])}: vacation, illness, maternity, service bonus, severance, indemnity and type-51 results read before they were posted).")
A(f"- Independent calculation: {S['cases_v2']} cases, {S['values_v2']} values; {len(S['shares_diffs'])} differences with its rounding convention (C-543 floor on days 91–180; one-peso type-51 pension total; one-cent annual-cap consumption); with this design's rounding the added differences are the employer residue and the non-taxable income only (`VALIDATION.md`).")
A('- Sweep: 298 rows × 9 bases = 2,682 checks, 0 differences.')
A(f"- Design checks (hand calculation from the law): {len(S['extras'])} / {len(S['extras'])} exact, including the four CCG v1.7 worked examples with the annual caps tracked year-to-date and the Procedure 2, retirement-bonus, short-service, projection, 204-UVT, rounding and gross / net checks.")
A('- Employee / employer coding: 0 errors; a copy with the employer health band coded as employee is caught. Column O (table read): 0 findings.')
A('')
A('**Change log.** v2.0 (2 November 2026): rules of v1.2 rewritten in the development team\'s schema and executed; finals of 2 November 2026 (CCG v1.7, WTC v1.9, DD v1.6, SIR v1.4); regulation-by-regulation table in `CHANGELOG.md`.')
open(os.path.join(OUT, 'CO_Regulation_Design_v2_0.md'), 'w', encoding='utf-8', newline='\n').write('\n'.join(H) + '\n')

# ------------------------------------------------------------------ CHANGELOG
C = ['# CHANGELOG — Colombia design v1.2 → v2.0 (2 November 2026)', '',
     'Basis: v1.2 of 2 November 2026 (57 regulations, prose and formulas) → v2.0 (machine-readable `co_design_v2.json`, executed). Basis documents: CCG v1.7, WTC v1.9, DD v1.6, SIR v1.4.', '',
     '## Defects of v1.2 found by executing it (v1.2-faithful variant, same engine)', '',
     f"1. **Order** — {len(S['v12_order'])} reads of an account before the regulation that posts it (e.g. the IBC `9170021` read vacation, illness and maternity amounts posted at ordinals 85–94; gross `9170015` read the service bonus posted at 82; the indemnity withholding `9170064` read the indemnity posted at 91; total contributions read the type-51 amounts posted at 97). Fixed: every earning / payment runs before the bases.",
     '2. **Transport allowance counted twice in the statutory-benefit base** — v1.2 `58171` = matrix I (which contains the transport-allowance row, WTC W304 = Yes) + 52503 by formula. Service bonus and severance savings 12% too high for salaries ≤ 2 SMMLV (P01: 1,749,095 instead of 1,624,548). Fixed: the allowance enters only through its WTC row.',
     '3. **Non-resident base** — v1.2 used the column-N base `58150`; the WTC has its own column P, which differs on 15 rows (pensions R241–R248, end-of-service gratuities R282, R284–R286 are P = Yes; employer voluntary pension R349–R350 and occasional per diem R353 are P = No). Fixed: `9170132` reads column P.',
     '4. **Service bonus and indemnities in the monthly table read** — v1.2 matrix A (column N) included R320 and R339 although the design reads them separately (Decree 1625 art. 1.2.4.1.3 Procedure 1; Tax Code art. 401-3). Fixed: false in `9170072` (with R340 and the retirement bonus R345), read by `9170089`–`9170093`; under Procedure 2 the service bonus enters the monthly base through `9170073`.',
     '5. **Indemnity withholding base** — only the art. 64 indemnity; Tax Code art. 401-3 covers "las indemnizaciones derivadas de una relación laboral". Fixed: R339, R343, R344.',
     '6. **Illness floor** — v1.2 stated "no validation case triggers it"; the floor of C-543 of 2007 binds on days 91–180 for salaries below 2 SMMLV (half the daily salary < SMMLV / 30). The v1.2 formula already had the floor; its check text (I03 days 91–100 = 500,000) was wrong: 583,635.',
     '7. **Rule groups** — the 17 income-tax regulations of v1.2 were `retro_simple_tax*`; v2.0 uses `simple_tax*` (no retro_), as the development team\'s draft 9170132, because Procedure 1 applies the table to the payments made in the month (Decree 1625 art. 1.2.4.1.3).',
     '', '## Changes after the independent review', '',
     '- Procedure 2: the service bonus is folded into the monthly base (`9170073`; Decree 1625 art. 1.2.4.1.3, Procedure 2: "la totalidad de tales pagos gravables"; CCG v1.7 Module 6). Check X12: 1,057,500.',
     '- Retirement bonus R345: out of the monthly read, withheld by Decree 1625 art. 1.2.4.1.8 (`9170090`; "bonificaciones por retiro definitivo del trabajador"; the 20% of Tax Code art. 401-3 is for indemnities). Check X13.',
     '- Termination average: divided by the months of service when fewer than 12 (`9170088`, input `58259`; Decree 1625 art. 1.2.4.1.8 lit. a). Check X14: 194,649.',
     '- Contributions: one regulation per fund with an employee band (`employeeRate`) and an employer band (`employerRate` / `employerRateAccount`), as the development team codes them; the employer band is written from the base and reads no other band. Check that a band coded on the wrong side is caught.',
     '- Projection for periods shorter than 30 days: Procedure 1 only (`9170074`). Check X15: 341,250.',
     '- Late-payment indemnity R340 (Labour Code art. 65, "como indemnización") withheld with the indemnities of Tax Code art. 401-3; 204-UVT test on the monthly salary, as the CCG v1.7 worked example (Module 9). Check X16.',
     '- Non-resident flat tax reads `$64552`, the account of the development team\'s draft; JSON keys `regulationId` and `systemTaxYearIds`.',
     '- Rounding: each contributor and fund rounded once, up to the next COP 100 (Decree 780 art. 3.2.1.5 num. 2; AT2 v30 field 47); employee share = statutory rate to the peso, employer share = rounded fund total - employee share; non-taxable income = contributions withheld (Tax Code arts. 55, 56). Check X17.',
     '- Gross and net in cash: severance savings deposited to the fund out of the gross (added when paid on termination), deduction wage types negative; net pay less salary in kind and voluntary pension / AFC / RAIS deductions. Checks X18–X20.',
     '- Column-O (table read) check added; memo and matrices texts aligned; apprentice practical phase listed in the research gaps.',
     '', '## Regulation by regulation', '', '| v1.2 | v2.0 ID (ordinal) | Name | Change |', '|---|---|---|---|']
CHG = {
 'CO Statutory-Benefit Base': 'transport allowance only through its WTC row (defect 2)', 'CO Taxable Labour Payments (monthly read)': 'R320, R339, R340, R343, R344, R345 false (defect 4); rule group retro_ -> simple_tax (item 7)',
 'CO Service Bonus in the Procedure 2 Base': 'new: service bonus in the Procedure 2 base', 'CO Withholding - Retirement Bonus': 'new: retirement bonus by Decree 1625 art. 1.2.4.1.8', 'CO Termination Withholding Percentage (12-month average)': 'average by the months of service when fewer than 12',
 'CO Severance Savings Paid on Termination': 'new: severance savings paid on termination in the gross', 'CO Gross Earnings': 'deposited severance savings out; deductions negative',
 'CO Net Pay': 'less salary in kind and voluntary pension / AFC / RAIS deductions', 'CO Withholding - Procedure 2': 'service bonus in the base; no projection',
 'CO Health Contribution (EE and ER)': 'employee and employer bands in one regulation; one rounding per contributor and fund',
 'CO Pension Contribution (EE and ER)': 'employee and employer bands in one regulation; one rounding per contributor and fund',
 'CO Contributor Type 51 Pension (EE and ER)': 'employee and employer bands; total rounded once', 'CO Non-taxable Income (contributions and voluntary RAIS)': 'contributions withheld, not before rounding',
 'CO Income Tax Flat': 'ID, name, ordinal, rule group and assertion `EQUALS($64552;2)` of the development team\'s draft; base column P (defect 3)',
 'CO Withholding - Indemnities': 'base R339 + R340 + R343 + R344 (defect 5); 204-UVT test on the monthly salary',
 'CO Illness Benefit Days 91-180 (health insurer)': 'split into segments; floor binds (defect 6)', 'CO Projection Factor for Periods Shorter than 30 Days': 'new: Decree 1625 art. 1.2.4.1.3 lits. a-b option, off by default; Procedure 1 only',
 'CO Service Bonus Exempt 25%': 'new split of the separate read: 25% within the annual 790 UVT left after the salary read', 'CO Service Bonus Reliefs within the Cap': 'new split of the separate read',
 'CO Solidarity Fund Subsistence Rate': 'rate as an account (band rate), so the contribution keeps its raw value', 'CO Employer Pension Rate': 'rate as an account', 'CO Occupational-Risk Rate': 'rate as an account',
 'CO Procedure 1 Tax before Rounding': 'raw tax kept (÷ projection factor); rounding in the next regulation', 'CO Vacation Compensation Above Half (block flag)': 'block written as a flag (v1.2: "must be blocked")',
 'CO All-inclusive Salary for the Period': 'split out of v1.2 9170010: the all-inclusive salary is posted to its own WTC row R303 (column W = No)',
 'CO Illness Benefit Total': 'information', 'CO Contribution Base of the Illness Days': 'information', 'CO Contribution Base of the Maternity Leave': 'information', 'CO Vacation Daily Value': 'information',
}
for r in REGS:
    v = r['v12']
    old = f"{v[0]} ({v[1]})" if v else '—'
    ch = CHG.get(r['name'], 'same rule; renumbered (order rule; ID = 9170000 + ordinal)' if v and v[1] != r['ordinal'] else 'same rule')
    if r['taxGroup'] == 'income_tax' and v and 'retro_' not in ch and r['name'] not in ('CO Taxable Labour Payments (monthly read)',): ch += '; rule group retro_ -> simple_tax (item 7)'
    if r['ordinal'] < 40 and v and v[1] > 40: ch = 'moved before the bases (defect 1)' + ('; ' + CHG[r['name']] if r['name'] in CHG else '')
    C.append(f"| {old} | {r['regulationId']} ({r['ordinal']}) | {r['name']} | {ch} |")
C += ['', 'Basis texts of the 2 November 2026 issue reflected: Constitutional Court C-397 of 1994 and DIAN Concepto 577 of 2020 (severance savings of non-residents); Decree 1469 of 2025 with Decree 0159 of 2026 left without effect (SMMLV); C-543 of 2007 (illness floor); incapacity and leave outside SENA / ICBF / CCF (WTC column T; Consejo de Estado exp. 23856 of 2021; Superintendencia del Subsidio Familiar Concepto 2-2018-083606); payment method 46 (report side).']
open(os.path.join(OUT, 'CHANGELOG.md'), 'w', encoding='utf-8', newline='\n').write('\n'.join(C) + '\n')

# ------------------------------------------------------------------ ASSUMPTIONS
doc = B['E'].__doc__
sem = doc[doc.index('S1 '):].strip()
AS = ['# ASSUMPTIONS — Colombia design v2.0', '', '## Engine semantics (not confirmed in the production engine; each is a switch or a rule in the engine)', '', '```', sem, '```', '',
      '## Design assumptions', '', '| # | Assumption | Effect | Confidence |', '|---|---|---|---|',
      '| A1 | Service bonus and salary in the same month (Procedure 1): the salary read uses the annual 790 / 1,340 UVT room first; the service-bonus read uses what is left (`9170091`, `9170092`). The law does not say how the annual cap is shared between the two reads. | the service-bonus withholding in a month where the annual cap is nearly used | 80% — configurable |',
      '| A2 | One rounding per contributor and fund, up to the next COP 100 (Decree 780 art. 3.2.1.5 num. 2: "El valor de los aportes liquidados por cada cotizante … múltiplo de 100 superior"; AT2 v30 field 47). The employee share is the statutory rate rounded to the peso (Law 100 arts. 20, 204: 4%); the employer pays the residue of the rounded total. Where the employee pays the whole fund (exonerated health, solidarity fund) the employee share carries the rounding. The split itself is not regulated. | the employer bears the rounding | 92% |',
      '| A3 | The 70% factor of the all-inclusive salary is applied to the whole IBC and levy matrix (salary rows) of an all-inclusive employee. | only if an all-inclusive employee also has non-integral salary rows | 90% |',
      '| A4 | Sub-30-day projection of Procedure 1 (Decree 1625 art. 1.2.4.1.3 lits. a-b: "podrá") is an entity option, off by default (`58214`). | withholding in hiring / leaving months | 95% (the decree makes it optional) |',
      '| A5 | Tax residence is read from `$64552` (1 resident, 2 non-resident), the account of the development team\'s draft 9170132; the DD field Tax Residence Status must feed it. | none | — |',
      '| A6 | `DAYS360` (30/360, inclusive) is available for the service days of the art. 64 indemnity (`58288`), as the development team computes month counts with `YEARS_BETWEEN`. | indemnity days | — |',
      '| A7 | `CEILING(x;n)` exists in the formula vocabulary; if not, an equivalent must be confirmed on boundary values (IBC 992,179.50 → 992,180). | IBC and every contribution | — (blocking if absent) |',
      '| A8 | The illness benefit floor (C-543 of 2007) is applied per day to every segment, days 91–180 included; a client paying more is lawful (Labour Code art. 13). | days 91–180 below 2 SMMLV | 93% |',
      '| A9 | Non-taxable income = the contributions withheld from the employee, rounded (Tax Code arts. 55, 56: "los aportes obligatorios que efectúen los trabajadores"). | withholding base up to COP 100 per fund lower than with the contributions before rounding | 90% |',
      '| A10 | `regulationId` carries the 9170xxx code (the development team stores a UUID there and the code in name / ordinal); `systemTaxYearIds` = `co_2026` by analogy with `td_2026`. | none | — |']
open(os.path.join(OUT, 'ASSUMPTIONS.md'), 'w', encoding='utf-8', newline='\n').write('\n'.join(AS) + '\n')

# ------------------------------------------------------------------ RESEARCH GAPS
RG = ['# RESEARCH GAPS — Colombia design v2.0', '', '| # | Gap | Severity | What closes it |', '|---|---|---|---|',
      '| R1 | 21 `Yes/No` wage types need an exempt / subject split at configuration (R6, R37, R227, R241–R248, R282, R284–R286, R338, R346 withholding, R349, R350, R353, R358). | 🟡 | configuration of the split wage types |',
      '| R2 | Apprentice in the practical phase ("all rights of an employment contract", Labour Code art. 81; CCG v1.7): the WTC marks the support R338 `Yes/No` in pension (U), solidarity fund (R), levies (T), benefit base (W) and vacation base (X), so the practical-phase pension, solidarity fund, CCF and statutory benefits are 0 until the support is split by phase (classroom: health and occupational risk only). | 🟡 | split wage type + phase field in the DD |',
      '| R3 | History reads: Procedure 2 fixed percentage (12 months ÷ 13, art. 386; input `58250`, not computed), termination percentage (taxable payments of the 12 months before termination, input `58255`, and months of service, input `58259`; Decree 1625 art. 1.2.4.1.8), severance-savings exemption (6-month average, art. 206 num. 4). | 🟡 | engine history-read mechanism |',
      '| R4 | IBC of the absence days (vacation taken: IBC before the vacation, Decree 780 art. 3.2.5.1; incapacity / leave: benefit value) needs a per-novelty day split; this design gives the benefit IBC as information (`58195`, `58194`). | 🟡 | PILA novelty fields |',
      '| R5 | Occupational-risk rate notified by the insurer per work centre overrides the class initial rate (`9170055`). | 🟡 | DD link work centre → employee |',
      '| R6 | Multi-employer: the 25-SMMLV ceiling applies to the sum across employers. | 🟡 | not modelled |',
      '| R7 | 204-UVT test of the indemnity withholding reads the monthly salary (`$64992`), as the CCG v1.7 worked example (Module 9: 4,500,000 = 85.92 UVT; termination payments out); Tax Code art. 401-3 ("trabajadores que devenguen ingresos superiores a 204 UVT") does not define the income measured. | 🟡 75% | DIAN doctrine |',
      '| R8 | Penalties R341 / R342 (late deposit of severance savings / unpaid interest; Law 50 of 1990 art. 99, text not read): whether they are "indemnizaciones derivadas de una relación laboral" for Tax Code art. 401-3; kept in the monthly read. R340 (Labour Code art. 65, "como indemnización") is routed with the indemnities. | 🟡 | DIAN doctrine |',
      '| R9 | Art. 64 variants (fixed-term contract, work contract, probation, Law 789 transitional table) not built. | 🟡 | research |',
      '| R10 | Solidarity-fund bands of Law 2381 of 2024 from 1 April 2027 (Constitutional Court C-264 of 2026): effective-date the band table. | 🟡 2027 | — |',
      '| R11 | Electronic payroll incapacity type labels 2 / 3 (report side): only a DIAN consultation closes it (75%). | report | DIAN |',
      '| R12 | CCG v1.7 is internally inconsistent on the payroll-levy base of the all-inclusive salary: one passage caps it at 25 SMMLV (43,772,625), another says "no ceiling at all". This design follows Law 21 of 1982 art. 17 (no ceiling). To correct in the CCG. | 🟡 source | CCG |',
      '| R13 | PILA AT2 v30 describes the distribution of contributions under Law 2381 of 2024 from a 2025 period, while the CCG v1.7 dates Law 2381 at 1 April 2027 (Constitutional Court C-264 of 2026). This design follows the CCG; re-check before 2027. | 🟡 2027 | — |']
open(os.path.join(OUT, 'RESEARCH_GAPS.md'), 'w', encoding='utf-8', newline='\n').write('\n'.join(RG) + '\n')

# ------------------------------------------------------------------ VALIDATION
V = ['# VALIDATION — Colombia design v2.0', '',
     '**Reference:** an independent calculation written from the statutes (separate code, not derived from this design), on the cases of the validation suite and the research examples (minimum wage, all-inclusive, 4 / 10 / 16–20 / 25 SMMLV bands, overtime and the 14 / 15 July 2026 change, transport allowance at 2 SMMLV, art. 114-1, Law 1393, service bonus, severance savings and interest, vacation, illness, maternity, art. 64 indemnity, contributor type 51, the 18 art. 383 table boundaries), with the 790 / 1,340 UVT caps tracked year-to-date (same pay since 1 January). Design checks by hand calculation from the law cover what the suite does not exercise (Procedure 2, retirement bonus, short service, projection, 204-UVT test, rounding, gross / net).', '',
     '**What the sweep proves.** The matrices are generated from the WTC columns, so their content is equal by construction; the sweep runs each row through the engine and checks the mechanism (bases, floors, the Law 1393 excess, routing, signs) against the flags.', '',
     '## Results', '', '```', RUN.strip(), '```', '',
     '## The remaining differences, each explained', '',
     '| Case | Lines | Cause | Who is right |', '|---|---|---|---|',
     '| I03, I04 | days 91–180, total, IBC of the incapacity | the independent calculation applies 1/2 of the daily salary on days 91–180 without the minimum-wage floor; C-543 of 2007 (resolutive part) conditions all of Labour Code art. 227: the benefit "no podrá ser inferior al salario mínimo legal vigente" | the design (floor per day) |', '',
     '**Against the adjusted independent calculation** (same code, with the contribution of each contributor and fund rounded once - Decree 780 art. 3.2.1.5 num. 2, AT2 v30 field 47 - and the contributions withheld out of the withholding base - Tax Code arts. 55, 56): only the six I03 / I04 lines above remain. Against the unadjusted calculation, the further differences come from those two conventions only (employer share, withholding chain; one cent on C23 from its cent-rounded annual consumption).', '',
     '## Reproduction of v1.2 (same engine, v1.2 IDs / ordinals / formulas)', '',
     f"Monthly cases: 59 cases, 2,153 values, 11 differences — the one-cent C23 consumption (4) and RC01 (7: the sub-30-day projection option did not exist in v1.2). The v1.2 method is therefore reproduced on the monthly chain. On the other modules and checks the v1.2 defects appear: order ({len(S['v12_order'])} reads), transport allowance twice in the benefit base (P01, P02, P04, P05, RC08, RC12), the sweep (non-resident base misses column P on 12 rows; service bonus, indemnities and retirement bonus in the monthly read) — see `CHANGELOG.md`.", '',
     '## Not validated', '', '- Production engine (no Colombia regulation set loaded there yet): the semantics of `ASSUMPTIONS.md` are to be confirmed on acceptance.', '- Procedure 2 fixed-percentage computation, history reads, apprentice practical phase, absence-day IBC split (`RESEARCH_GAPS.md`).']
open(os.path.join(OUT, 'VALIDATION.md'), 'w', encoding='utf-8', newline='\n').write('\n'.join(V) + '\n')

# ------------------------------------------------------------------ MEMO (v1.2 positions, updated)
m = open(os.path.join(VAL, 'final', 'design', 'CO_Statutory_Research_Memo_v1_2.md'), encoding='utf-8').read()
SUBS0 = [('**Design effect:** `9170048`; gates of `9170062`, `9170066`, `9170067`.', '**Design effect:** `9170048`; gates of the employer band of `9170056`, `9170062`, `9170063`.'), ('**Design effect:** `9170074`, `9170076`, `9170079`–`9170082` (year-to-date reads); no 72-UVT regulation.', '**Design effect:** `9170075`, `9170077`, `9170080`–`9170083` (year-to-date reads); no 72-UVT regulation.'), ('**Design effect:** `9170087` (outside the monthly read `9170072`).', '**Design effect:** `9170088`–`9170090` (outside the monthly read `9170072`).')]
SUBS = [
 ('**Companion to:** `CO_Regulation_Design_v1_2.md` (57 regulations) and `CO_Taxability_Matrices_v1_2.md`', f'**Companion to:** `CO_Regulation_Design_v2_0.md` ({len(REGS)} regulations, `co_design_v2.json`) and `CO_Taxability_Matrices_v2_0.md`'),
 ('**Basis:** CO-CCG-001 v1.6, CO-WTC-001 v1.8 and CO-DD-001 v1.5 (issue of 2 November 2026)', '**Basis:** CO-CCG-001 v1.7, CO-WTC-001 v1.9 and CO-DD-001 v1.6 (issue of 2 November 2026)'),
 ('(`CEILING`, history reads, the art. 383 table construct — design Part 6 items 1 and 4, Part 4 `9170061`)', '(`CEILING`, history reads, the art. 383 table construct — `ASSUMPTIONS.md` A7, `RESEARCH_GAPS.md` R3, regulation `9170084`)'),
 ('**Design effect:** `9170025`; gates of `9170041`, `9170045`, `9170046`.', '**Design effect:** `9170048`; gates of `9170062`, `9170066`, `9170067`.'),
 ('**Design effect:** `9170019`–`9170021`.', '**Design effect:** `9170044`, `9170045`.'),
 ('**Design effect:** matrix K split; `9170017`.', '**Design effect:** WTC column V; `9170042`.'),
 ('(CCG v1.6 Module 6.3: September 2026 retention bonus, withholding 3,947,554.80)', '(CCG v1.7 Module 6.3: September 2026 retention bonus, withholding 3,947,554.80 — reproduced by the engine)'),
 ('**Design effect:** `9170052`, `9170054`, `9170057`–`9170059` (year-to-date reads); no 72-UVT regulation.', '**Design effect:** `9170074`, `9170076`, `9170079`–`9170082` (year-to-date reads); no 72-UVT regulation.'),
 ('**Position.** 20% of the indemnity where the employee\'s income exceeds 204 UVT (Tax Code art. 401-3; Decree 1625 of 2016 art. 1.2.4.1.13)', '**Position.** 20% of the indemnities derived from the employment relationship — the art. 64 indemnity, the early-termination indemnity of a fixed-term or work contract and the indemnity for dismissal during protected status (WTC R339, R343, R344) — where the employee\'s income exceeds 204 UVT (Tax Code art. 401-3: "Las indemnizaciones derivadas de una relación laboral … a una tarifa del veinte por ciento (20%) para trabajadores que devenguen ingresos superiores al equivalente de doscientas cuatro (204) UVT"; Decree 1625 of 2016 art. 1.2.4.1.13)'),
 ('**Design effect:** `9170064`.', '**Design effect:** `9170087` (outside the monthly read `9170072`).'),
 ('Severance savings and their interest are **not** withheld, for a non-resident as for a resident: Law 100 of 1993 art. 135 par. 3 ("en ningún caso" subject to withholding), Decree 1625 of 2016 art. 1.2.4.1.11 and DIAN Oficios 8899 of 2015 and 4358 of 2019.',
  'The base is WTC column P (pensions and end-of-service gratuities included; employer voluntary pension contributions and the occasional per diem excluded). Severance savings and their interest are **not** withheld, for a non-resident as for a resident: Law 100 of 1993 art. 135 par. 3 ("en ningún caso" subject to withholding), whose limitation to payments "por parte de la Nación" was struck down by the Constitutional Court (C-397 of 1994), Decree 1625 of 2016 art. 1.2.4.1.11 and DIAN Oficios 8899 of 2015 and 4358 of 2019; a non-resident who must file applies the art. 206 exemptions in the return (DIAN Concepto 577 of 2020: Tax Code art. 26 with arts. 178 and 235-2).'),
 ('**Design effect:** `9170063` (severance rows `No` in matrices A and C); design open item 10 closed.\n**Confidence:** 90% (salary); 80% (severance savings not withheld).',
  '**Design effect:** `9170132` "CO Income Tax Flat" (ID, name and ordinal of the development team\'s draft; severance rows false in columns N and P).\n**Confidence:** 90% (salary); 92% (severance savings not withheld).'),
 ('**Design effect:** constants `52504`, `52505`; `9170012`.', '**Design effect:** constants `52504`, `52505` read at the date of each hours line; `9170012`.'),
 ('Not salary: out of the IBC and the levy base, in the service-bonus and severance-savings base.', 'Not salary: out of the IBC and the levy base, in the service-bonus and severance-savings base — once, through its WTC row (W304 = Yes).'),
 ('**Design effect:** `9170013`, `9170081`.', '**Design effect:** `9170013`, `9170020`.'),
 ('but in the levy base (Law 21 of 1982 art. 17).', 'but in the levy base: it is paid rest ("descanso remunerado") under Law 21 of 1982 art. 17 (Consejo de Estado, Sala de Consulta, concepto 2027 of 2010; Consejo de Estado, Sección Cuarta, exp. 27226 of 11 May 2023; UGPP ABC Empleadores 2025 p. 7); cash compensation of vacation is not salary but a kind of indemnity (Supreme Court SL467-2019).'),
 ('**Design effect:** `9170085`, `9170086`; matrices I, J, G.\n**Confidence:** 85% on the cash formula and on the IBC / benefit-base exclusion; 70% on the inclusion in the payroll-levy base (UGPP practice diverges).',
  '**Design effect:** `9170016`, `9170017`, `9170019`; WTC columns W, X, T.\n**Confidence:** 85% on the cash formula and on the IBC / benefit-base exclusion; 94% on the inclusion in the payroll-levy base.'),
 ('**Design effect:** `9170096`; open item 7 (phase field, transport allowance).', '**Design effect:** `9170011`; `RESEARCH_GAPS.md` R2 (phase field, practical-phase levy split).'),
 ('**Design effect:** `52520`.', '**Design effect:** `9170055`.'),
 ('**Design effect:** `9170091`.', '**Design effect:** `9170031`, `9170032`.'),
 ('2/3 of the salary (days 1–2 employer, from day 3 health insurer; 1/2 from day 91), never below the minimum-wage equivalent (Labour Code art. 227; Constitutional Court C-543 of 2007, resolutive part).',
  '2/3 of the salary (days 1–2 employer, from day 3 health insurer; 1/2 from day 91), never below the minimum-wage equivalent per day, in every segment (Labour Code art. 227; Constitutional Court C-543 of 2007, resolutive part: the art. 227 benefit "no podrá ser inferior al salario mínimo legal vigente"). For a salary below 2 SMMLV the floor binds on days 91–180 (3,000,000: 58,363.50 a day instead of 50,000).'),
 ('**Design effect:** `9170093`, constant `52544`.\n**Confidence:** 90%.', '**Design effect:** `9170024`–`9170028`.\n**Confidence:** 93%.'),
 ('| 15 — Illness floor | Minimum wage, configurable | Nothing |', '| 15 — Illness floor | Minimum wage per day, every segment | Nothing |\n| 16 — Levies on incapacity and leave | Not due | Nothing |\n| 17 — Rule groups | Income tax without retro_; social security with retro_ | Nothing |'),
 ('| 7 — Non-resident | Flat 20%; severance savings and interest not withheld (20% optional, off by default) | Nothing |', '| 7 — Non-resident | Flat 20% on column P; severance savings and interest not withheld (20% optional, off by default) | Nothing |'),
 ('| 6 — Indemnity withholding | 20% above 204 UVT, else 12-month table % | Measured income (open item 11) |', '| 6 — Indemnity withholding | 20% above 204 UVT on R339 / R343 / R344, else 12-month table % | Measured income (R7) |'),
]
for o, n in SUBS:
    assert m.count(o) == 1, o[:70]
    m = m.replace(o, n)
M2 = [
 (' and matches the provider payroll', ''),
 (' A client that prefers the conservative position may switch on the 20% for non-residents (configuration option, off by default).', ''),
 ('Flat 20% on column P; severance savings and interest not withheld (20% optional, off by default)', 'Flat 20% on column P; severance savings and interest not withheld'),
 ('| Year-to-date reads (open item 8) |', '| Year-to-date reads (`RESEARCH_GAPS.md` R3) |'),
 ('| Phase field (open item 7) |', '| Phase field and split (`RESEARCH_GAPS.md` R2) |'),
 ('20% above 204 UVT on R339 / R343 / R344, else 12-month table %', '20% above 204 UVT of monthly salary on R339 / R340 / R343 / R344; retirement bonus R345 and the rest by the table % of the 12-month average (÷ months of service if fewer)'),
 ('| 17 — Rule groups | Income tax without retro_; social security with retro_ | Nothing |',
  '| 17 — Rule groups | Income tax without retro_; social security with retro_ | Nothing |\n| 18 — Periods < 30 days | Optional projection, Procedure 1 only | Nothing |\n| 19 — Rounding and non-taxable contributions | One rounding per contributor and fund; contributions withheld out of the base | Split of the rounded total (A2) |'),
 ("; numbered v1.2 because the Drive folder 07 - Design already holds an earlier, separate v1_1 pack dated 5 October", ""),
 ('(Tax Code art. 401-3: "Las indemnizaciones derivadas', '(Labour Code art. 65 late-payment indemnity R340 included: "como indemnización"; Tax Code art. 401-3: "Las indemnizaciones derivadas'),
 ('otherwise the table percentage of the average monthly taxable payments of the previous 12 months (Decree 1625 art. 1.2.4.1.8).',
  'otherwise the table percentage of the average monthly taxable payments of the previous 12 months, divided by the months of service if fewer than 12 (Decree 1625 art. 1.2.4.1.8 lit. a). The retirement bonus (WTC R345) is always withheld by that percentage ("bonificaciones por retiro definitivo del trabajador", art. 1.2.4.1.8); the 20% of art. 401-3 covers indemnities only. The 204-UVT test reads the monthly salary, as the CCG v1.7 worked example (termination payments out).'),

]
for o, n in SUBS0 + M2:
    assert m.count(o) == 1, ('memo', o[:70], m.count(o))
    m = m.replace(o, n)
m = m.replace('\n---\n\n## Summary', '''
---

## Item 19 — Contribution rounding and the non-taxable contributions — ✅ One rounding per contributor and fund; contributions withheld

**Position.** "El valor de los aportes liquidados por cada cotizante … deberá aproximarse al múltiplo de 100 superior más cercano" (Decree 780 of 2016 art. 3.2.1.5 num. 2, as substituted by Decree 1990 of 2016 art. 1); the contribution return validates field 47 as IBC × total pension rate with that rounding (PILA AT2 v30). The total of each fund is therefore rounded once; the employee share is rounded up and the employer pays the residue (the split itself is not regulated). The withholding base excludes "los aportes obligatorios que efectúen los trabajadores" (Tax Code arts. 55, 56): the contributions actually withheld.

**Design effect:** `9170056`, `9170057`, `9170064` (employee and employer bands); `9170075`.
**Confidence:** 95% (rounding of the total); 85% (split); 90% (non-taxable amount).

---

## Summary''', 1)
add = '''
---

## Item 16 — Payroll levies on incapacity and leave — ✅ Not due

**Position.** The incapacity benefit is not salary and is excluded from the SENA / ICBF / CCF base (Consejo de Estado, Sección Cuarta, 19 August 2021, exp. 23856); maternity, paternity, parental and childcare leave are paid by the health insurer, not by the employer, so no payroll levies are due on them (Superintendencia del Subsidio Familiar, Concepto 2-2018-083606). UGPP ABC Empleadores 2025 (p. 7) tells employers to include them, while its own table on p. 6 lists these events only for social security; the guide has no normative force.

**Design effect:** WTC column T = No on R123, R326–R333; the levy base `9170047` leaves them out (sweep: 0 differences).
**Confidence:** 92%.

---

## Item 17 — Retroactive pay: which regulations re-run the past period? — ✅ Social security yes, income tax no

**Position.** Withholding under Procedure 1 applies the table to "la totalidad de dichos pagos que se hagan al trabajador … durante el respectivo mes" (Decree 1625 of 2016 art. 1.2.4.1.3): a retroactive amount is withheld in the month it is paid, as the development team's draft (9170132, `simple_tax_post_formula`). Contributions belong to the period earned: a retroactive salary adjustment is re-filed for that period (PILA Technical Annex 2 v30, planilla N: record A original, record C corrected IBC). Social-security regulations therefore keep `retro_`.

**Design effect:** taxRuleGroup of every regulation (`co_design_v2.json`).
**Confidence:** 92%.

---

## Item 18 — Pay periods shorter than 30 days — ✅ Optional projection

**Position.** Under Procedure 1 only, the employer may project the payments of a period shorter than 30 days to 30 days, take the table percentage of the projected amount and apply it to the real payments (Decree 1625 of 2016 art. 1.2.4.1.3 lits. a and b: "su retención podrá calcularse así"). It is optional; entity option, off by default.

**Design effect:** `9170074` (flag `58214`; Procedure 1 only).
**Confidence:** 95%.
'''
m = m.replace('\n---\n\n## Summary', add + '\n---\n\n## Summary', 1)
m = m.replace('**Change log.** v1.0 (30 October 2026)', '**Change log.** v2.0 (2 November 2026): basis CCG v1.7, WTC v1.9, DD v1.6; regulation references to the v2.0 IDs; item 6 (all employment indemnities), item 7 (column P; C-397 of 1994; Concepto 577 of 2020; 92%), item 10 (levy base 94%), item 15 (floor in every segment); items 16–19 added; items 6, 7 and 18 revised after the independent review (retirement bonus, months of service, R340, Procedure 1 only). v1.0 (30 October 2026)')
SEP = chr(10) + '---' + chr(10)
i19 = m.index('## Item 19'); s19 = m.rfind(SEP, 0, i19); e19 = m.index(SEP, i19)
blk = m[s19:e19]; m = m[:s19] + m[e19:]
k = m.index(SEP + chr(10) + '## Summary'); m = m[:k] + blk + m[k:]
assert '# CO — Statutory Research Memo' in m
open(os.path.join(OUT, 'CO_Statutory_Research_Memo_v2_0.md'), 'w', encoding='utf-8', newline='\n').write(m)
# internal-reference sweep of the package
bad = []
for fn in os.listdir(OUT):
    t = open(os.path.join(OUT, fn), encoding='utf-8').read()
    for w in ['oracle', 'Oracle', 'COVAL', 'rodada', 'pipeline', 'PMI', 'DRAFT', 'agent', 'Chad', 'Chade']:
        if re.search(r'\b' + w + r'\b', t): bad.append((fn, w))
print('written:', sorted(os.listdir(OUT)))
print('internal references:', bad)
