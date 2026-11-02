"""Chad — design comparison workbook: our v5 × the development team's td_2026.

Builds TD_Design_Comparison_v4_v5_v6_vs_Dev.xlsx (default) — and, with --v5-only, the earlier TD_Design_Comparison_v5_vs_Dev.xlsx — in this folder, in the layout of the models in ./modelos
(TD_Design_Comparison_Ours_vs_Dev.xlsx + the "Question for the call" column of BH_Design_Comparison_Dev_vs_Ours.xlsx).
Reads only (never writes) the sources:
  ../2026-11-01-design-v5/_build_v5.py          our v5 (regulations, engine, 12 scenarios + 20 extra checks)
  ../2026-11-01-design-v5/simulacao/sim_dev.py  the Dev engine (reads td.json from the Drive, read only)
  ../2026-10-29-teste-design-hrblizz/2026-10-30-export-ram/CHAD-WTC_V3.0-export-2026-11-01.xlsx   WTC V3.0
Run:  python -I build_comparacao.py
"""
import os, sys, importlib.util
sys.dont_write_bytecode = True
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.formatting.rule import CellIsRule

HERE = os.path.dirname(os.path.abspath(__file__))
CHAD = os.path.dirname(HERE)
V5 = os.path.join(CHAD, '2026-11-01-design-v5')
WTC = os.path.join(CHAD, '2026-10-29-teste-design-hrblizz', '2026-10-30-export-ram', 'CHAD-WTC_V3.0-export-2026-11-01.xlsx')
OUT = os.path.join(HERE, 'TD_Design_Comparison_v5_vs_Dev.xlsx')

sys.path.insert(0, os.path.join(V5, 'simulacao'))
import sim_dev  # noqa: E402
spec = importlib.util.spec_from_file_location('v5', os.path.join(V5, '_build_v5.py'))
v5 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v5)
DEV = sim_dev.load()
DEVBY = {r['ordinal']: r for r in DEV}
V5BY = {r['id']: r for r in v5.R}
assert len(DEV) == 31 and len(v5.R) == 35

# ---------------------------------------------------------------- styles (from the models)
F = lambda sz=9, b=False, name='Arial': Font(name=name, size=sz, bold=b)
GREY, BLUE, GREEN, YELLOW, ORANGE, RED, CODE = 'FFD9D9D9', 'FFDDEBF7', 'FFE2EFDA', 'FFFFF2CC', 'FFFCE4D6', 'FFFFC7CE', 'FFF7F7F7'
fill = lambda c: PatternFill('solid', fgColor=c)
thin = Side(style='thin', color='FFBFBFBF')
BOX = Border(left=thin, right=thin, top=thin, bottom=thin)
WRAP = Alignment(wrap_text=True, vertical='top')
CENTER = Alignment(wrap_text=True, vertical='center', horizontal='center')
NUM = '#,##0;\\(#,##0\\);\\-'
STATUS_FILL = {'Same': GREEN, 'Different': YELLOW, 'Only theirs': ORANGE, 'Only ours': BLUE}
WHO_FILL = {'Both': GREEN, 'Ours': BLUE, 'Dev': ORANGE, 'Neither': RED, 'Open': YELLOW}


def title(ws, text, sub, last):
    ws['A1'] = text; ws['A1'].font = F(12, True)
    ws['A2'] = sub; ws['A2'].font = F(9)
    ws.merge_cells(f'A1:{last}1'); ws.merge_cells(f'A2:{last}2')


def header(ws, row, names, widths=None):
    for i, n in enumerate(names, 1):
        c = ws.cell(row, i, n)
        c.font = F(10, True); c.fill = fill(GREY); c.alignment = CENTER; c.border = BOX
    if widths:
        for i, w in enumerate(widths, 1):
            ws.column_dimensions[openpyxl.utils.get_column_letter(i)].width = w


def put(ws, row, col, value, bold=False, fmt=None, bg=None, code=False, center=False):
    c = ws.cell(row, col, value)
    c.font = F(8, False, 'Courier New') if code else F(9, bold)
    c.alignment = CENTER if center else WRAP
    c.border = BOX
    if fmt:
        c.number_format = fmt
    if bg:
        c.fill = fill(bg)
    elif code:
        c.fill = fill(CODE)
    return c


# ---------------------------------------------------------------- formula text extracted from each design
def n3(x):
    return '' if x in (None, '') else f'{float(x):,.3f}'


def dev_text(o):
    r = DEVBY[o]
    L = [f"9148{o:03d} · {r['taxationType'].capitalize()} · {r['taxRuleGroup']}"]
    if r.get('assertion'):
        L.append(f"Pre: {r['assertion']}")
    for b in r['bands']:
        s = []
        if b['incomeFrom'] is not None or b['incomeTo'] is not None:
            s.append(f"{n3(b['incomeFrom'])}–{n3(b['incomeTo'])}")
        if b['employeeRate'] is not None:
            s.append(f"EE {n3(b['employeeRate'])}")
        if b['employerRate'] is not None:
            s.append(f"ER {n3(b['employerRate'])}")
        if b['floorAmount'] is not None or b['ceilingAmount'] is not None:
            s.append(f"floor {n3(b['floorAmount'])} / ceil {n3(b['ceilingAmount'])}")
        if b['formula']:
            s.append(b['formula'])
        if b.get('assertion'):
            s.append(f"[{b['assertion']}]")
        s.append(f"→ {b['debitAccount']}/{b['creditAccount']}")
        L.append('  '.join(s))
    L.append(f"Matrix: {len(r['taxabilityRules'])} rules")
    return '\n'.join(L)


def v5_text(i):
    r = V5BY[i]
    L = [f"{i} · {r['ttype']} · {r['trg']}"]
    if r['pre']:
        L.append(f"Pre: {r['pre']}")
    for b in r['bands']:
        s = []
        if b['f'] != '' or b['t'] != '':
            s.append(f"{n3(b['f'])}–{n3(b['t'])}")
        if b['ee'] != '':
            s.append(f"EE {n3(b['ee'])}")
        if b['er'] != '':
            s.append(f"ER {n3(b['er'])}")
        if b['floor'] != '' or b['ceil'] != '':
            s.append(f"floor {n3(b['floor'])} / ceil {n3(b['ceil'])}")
        if b['ceilacc']:
            s.append(f"ceilingAccount {b['ceilacc']}")
        if b['formula']:
            s.append(b['formula'])
        if b['assertion']:
            s.append(f"[{b['assertion']}]")
        s.append(f"→ {b['deb']}/{b['cred']}")
        L.append('  '.join(s))
    L.append(f"Matrix: {len(r['matrix'])} rules")
    return '\n'.join(L)


def dev_name(o):
    return f"9148{o:03d} — {DEVBY[o]['name']}"


def v5_name(i):
    return f"{i} — {V5BY[i]['name']}"


# ---------------------------------------------------------------- Regulation Comparison (hand-written assessment; sources in LEI-VEREDITOS.md, COMPARACAO.md, v5 CHANGELOG)
# (block, dev ordinal, v5 id, status, cause, adherence, difference, legal basis, who, confidence, question, star)
RC = [
    ('Bases', 9, 9148013, 'Same', '(e) internal convention', 1, 'Same reporting constant (60,000 a month, floor = ceiling, monthly). v5 adds retro_.', 'Not a statutory value (DAS report parameter)', 'n/a', None, '', False),
    ('Bases', 10, 9148012, 'Different', '(b) benefits in kind and pensions in the cash base', 0.5, 'Dev 58105 holds benefits in kind at full value (65%%%), pensions 6264x, per diem/ticket codes; this base drives the BIK % caps, so they are inflated. v5: cash only (Art. 46-I/II), with 6286x, 6255x, 62570/6557x/6558x and 6287x relieved by their own exemptions.', 'CGI Art. 46-I/II (p. 30): base = cash pay « ainsi que de tous les avantages en argent »', 'Ours', 0.90, 'Can 58105 — the base of the benefit caps — hold cash pay only? Art. 46-II computes the caps on the cash items of Art. 46-I.', False),
    ('IRPP', 11, 9148074, 'Different', '(b) non-resident method', 0.25, 'Dev: gross without the Art. 45 exemptions, then 18%. v5: the non-resident uses the same taxable income 58552 and the progressive scale; 58592 is only a copy for the IRPP-TS report.', 'CGI Arts. 44-II-2° (p. 29), 847 (p. 168); Art. 116 (p. 43) covers only Art. 2-VI and Art. 60', 'Ours', 0.85, 'For non-resident employees, can we move from 18% to the progressive scale? Art. 116 reaches only royalties / BNC (Art. 2-VI) and artists (Art. 60); salaries fall under Art. 44-II-2° and Art. 847.', True),
    ('Exemptions', 21, 9148014, 'Different', '(d) structure', 0.75, 'Same 30% limit into 58103. v5 adds the 3.5% retirement limit (58172) in the same regulation and uses base salary 58109 (62100–62103, 62109); Dev uses 6210% (includes 62104/62105).', 'CGI Art. 45-13° (p. 30) « salaire de base mensuel »; Art. 47-I « 3.5 % des appointements »', 'Both', 0.90, 'Should the 30% transport limit use base salary only (62100–62103, 62109), without 62104 / 62105?', False),
    ('Exemptions', 31, 9148021, 'Different', '(b) missing condition · (d) ceiling account vs MIN()', 0.75, 'v5 applies the 30% only when the allowance is paid to all staff (entity flag 58207) and lets 6251x Car & Transportation share the 30%; Dev: 6252% only, no condition, MIN() in the formula.', 'CGI Art. 45-13° (p. 30): « lorsqu’elles profitent à tout le personnel de l’entreprise »', 'Ours', 0.95, 'The 30% transport exemption applies only when the allowance goes to all staff (Art. 45-13°). Can we add that entity flag, and let 6251x Car & Transportation share the 30%?', False),
    ('Exemptions', 32, 9148016, 'Different', '(b) per child and CNPS imputation', 0.75, 'Dev: 5,000 × all dependants (58212 = number_of_dependents). v5: 5,000 × children − the CNPS family allowance (58213), codes 6275x, 6276x, 6278x and 62866 Birth allowance.', 'CGI Art. 45-4° (p. 29); LF 2026 Art. 8 (p. 15): « par enfant… 5.000 Francs sur laquelle viennent… s’imputer les allocations versées par la CNPS »', 'Ours', 0.95, 'The cap in Art. 45-4° is per child, less what the CNPS already pays. Can the limit read the number of children and a CNPS-allowance field instead of all dependants?', True),
    ('Exemptions', 33, 9148022, 'Different', '(d) ceiling account vs MIN()', 0.9, 'Same mechanism (exempt part into 58108, read by the DAS report). v5 uses 58107 as ceiling account and the wider family code list.', 'CGI Art. 45-4° (p. 29)', 'Both', 0.95, '', False),
] + [
    ('BIK', o, 9148031 + k, 'Different', '(c) cap vs forfait', 0.5,
     f"Dev: always {p} × 58105 (forfait), whatever the real value. v5: MIN(real value; {p} of cash pay) — « plafonnés ».",
     'CGI Art. 46-III (p. 30) « Ceux-ci sont plafonnés »; Art. 46-V « dans la limite des taux »', 'Ours', 0.85,
     ('Art. 46-III says the benefit values are capped: tax the real value up to the %, not always the %. Can the nine BIK regulations take MIN(real value; % × cash pay)?' if k == 0 else 'Same as the housing benefit (cap, not forfait).'),
     k == 0)
    for k, (o, p) in enumerate([(41, '20%'), (51, '10%'), (61, '15% (max 75,000)'), (71, '5%'), (81, '4%'), (91, '4%'), (101, '4%'), (111, '3%'), (121, '2%')])
] + [
    ('Bases', 131, 9148041, 'Different', '(b) severance · (b) scholarship / allowances', 0.5, 'Dev excludes all severance 6218x, the 6274x schooling allowance and health insurance 65630; v5 taxes individual severance (only plan social exempt), 6274x and 65630, and excludes the 6580x scholarship (Art. 45-9°).', 'CGI Art. 44-I (p. 29); Art. 45-9°, 45-10° (p. 30)', 'Ours', 0.90, 'Individual severance (6218x) is taxable under Art. 44-I; only plan-social severance is exempt (Art. 45-10°). Can 6218x go back into the IRPP gross, with a plan-social flag for the exempt case?', True),
    ('TFE / TAFP', 141, 9148082, 'Different', '(b) Art. 45 carve-outs in the TA base', 0.5, 'Dev takes the exempt transport (58104) and 6276x out of the TAFP base. v5: Art. 173 gross base, minus only one-time / discretionary bonuses 6222x (not « servies régulièrement ») and pensions 6264x; minus the Art. 174-3° share (58219).', 'CGI Art. 173 (p. 59); Art. 174-3°; Art. 177', 'Ours', 0.85, 'Arts. 173 and 189 have no Art. 45 carve-out. Can the TFE / TAFP bases keep the exempt transport and family allowances? The TAFP leaves out only non-regular bonuses.', True),
    ('TFE / TAFP', 151, 9148081, 'Different', '(b) Art. 45 carve-outs · (b) missing Art. 188-10°', 0.5, 'Dev takes exempt transport, 6276x and 6222x out of the TFE base. v5 keeps them (Art. 189-1° « indemnités diverses, allocations, gratifications »), adds pensions 6264x, and excludes the pay of disabled employees and of young graduates / workers under 35 at real-regime entities.', 'CGI Art. 189 (p. 61); Art. 188-10°', 'Ours', 0.85, 'Can the TFE and TAFP bases leave out the pay of disabled employees and of young graduates or workers under 35 hired by real-regime companies (Art. 188-10°, Art. 174-3°)?', False),
    ('CNPS', 155, 9148051, 'Different', '(b) transport, 6286x, scholarship · (c) guide vs decree', 0.6, 'v5 takes the whole transport allowance out (guide p. 8 — technical decision of the front, pending the user’s ok) and includes 6286x meal/food, 6274x and 6580x; Dev takes only the exempt 30% out and leaves 6286x out by omission. Both exclude family allowances, meal cash 6566x, severance, per diem.', 'Dec. 1635/2009 art. 3; Dec. 1636/2009 art. 2; CNPS guide 2019 p. 7–8', 'Ours', 0.75, 'The CNPS guide (p. 8) lists the monthly transport allowance among the exclusions, with no 30% limit. Is it right to take the whole transport allowance out of the CNPS base?', True),
    ('CNPS', 161, 9148052, 'Different', '(b) floor without pay', 0.75, 'Same floor 60,000 / ceiling 500,000 a month. Dev applies the floor even in a month with no pay (CNPS on 60,000 with zero salary); v5 only when 58130 > 0.', 'CNPS guide p. 7 (« versés… entre le premier et le dernier jour du mois »), p. 9, 12; Dec. 1635 art. 4', 'Ours', 0.75, 'In a month with no pay, should the 60,000 floor still create CNPS? The guide charges contributions on pay actually paid in the month.', False),
    ('CNPS', 171, 9148053, 'Different', '(e) GL pairs inverted · (b) no branch flags', 0.75, 'Same rates (3.5 + 5 PVID, 7.5 PFM, 4 AT/MP). Dev posts the 3.5% employee band to 6020/2550 and the 7.5% employer band to 2610/2551 — inverted against the WTC (2551 = EE); v5: EE 2610/2551, ER 2537/2550/2560, each band gated by a branch flag (seconded employees under a convention).', 'Dec. 1635 arts. 1–2; Dec. 1636 art. 1; CNPS guide p. 6, 8; WTC V3.0 (2551 "TD CNPS Contribution EE")', 'Ours', 0.95, 'The 3.5% employee band posts to 6020 / 2550 and the 7.5% employer band to 2610 / 2551, the reverse of the WTC (2551 = employee). Is this intended?', True),
    ('Exemptions', 181, 9148061, 'Different', '(b) missing cap and compulsory test', 0.5, 'Dev deducts 2164x Voluntary Contribution in full; v5 deducts only compulsory contributions (2164x = No), up to 3.5% of base salary.', 'CGI Art. 47-I/II (p. 30): « dans la limite de 3.5 % » · « doivent revêtir un caractère obligatoire »', 'Ours', 0.95, 'Art. 47 deducts only compulsory pension contributions, up to 3.5%. 2164x is a voluntary contribution — should it be deductible at all?', True),
    ('IRPP', 191, 9148071, 'Different', '(d) more exemption accounts', 0.75, 'Same chain (gross − exemptions − EE CNPS − retirement). v5 adds plan social 58113, the 15% allowance 58114 and the leave ticket 58115.', 'CGI Art. 47-I (p. 30); Art. 45', 'Ours', 0.90, '', False),
    ('IRPP', 201, 9148072, 'Different', '(d) structure — annualisation', 0.75, 'Dev annualises in its own regulation (×period divisor); v5 lets the engine annualise the bands (retro_simple_tax). Both annualise every month ×12, irregular payments included.', 'CGI Art. 1-I/1-IV (p. 14) « impôt annuel »; Art. 847 (DGI barème, not obtained)', 'Open', 0.50, 'For irregular payments (severance, 13th month), do you also annualise the month ×12? Does the DGI barème (Art. 847) prescribe a cumulative method?', True),
    ('IRPP', 211, 9148072, 'Different', '(b) band limits x.99', 0.9, 'Same rates and thresholds. Dev writes 800,000.99 / 6,000,000.99…; v5 writes 800,000 / 6,000,000… (next band starts at the same figure), so a half franc rounds as the table says (scenarios 8 and 12: 1 XAF).', 'CGI Art. 1-IV (p. 14); LF 2026 Art. 3', 'Ours', 0.90, 'Can the band limits be written 800,000 / 6,000,000 with the next band starting at the same figure? With 800,000.99 the tax is 1 XAF lower at half a franc.', False),
    ('IRPP', 221, 9148072, 'Different', '(d) structure', 0.75, 'Dev divides the annual tax by the period divisor in its own regulation; v5 does it inside the differential regulation.', 'CGI Art. 1-IV', 'Both', 0.90, '', False),
    ('IRPP', 231, 9148073, 'Different', '(b) Art. 3-4° conditions', 0.75, 'Dev: young graduate exempt while ≤ 60 months, nothing else. v5: Art. 3-4° needs a real-regime employer, a start date, age under 35 at recruitment, and covers workers (ouvriers).', 'CGI Art. 3-4° (p. 15)', 'Ours', 0.85, 'The young-graduate exemption (Art. 3-4°) also needs a real-regime employer and age under 35, and covers workers (ouvriers). Can the condition use those fields?', False),
    ('IRPP', 241, 9148075, 'Different', '(b) non-resident method', 0.25, 'Dev: 18% on 58592. v5: the progressive-scale result posted to 2592 (so the report still separates residents and non-residents).', 'CGI Arts. 44-II-2°, 847, 116', 'Ours', 0.85, 'Same question as row 3 (non-resident on the scale).', False),
    ('TFE / TAFP', 251, 9148084, 'Different', '(b) missing relief', 0.75, 'Same 12‰, truncation to the 1,000 and rounding to the 10. v5 applies the 50% / 100% relief (58206) to the TAFP too; Dev has none on the TAFP.', 'CGI Art. 178, 177 (p. 60); Art. 158 (p. 56) « 50% de la taxe d’apprentissage »', 'Ours', 0.95, 'Art. 158 gives 50% relief on both TF and TA, and new companies are exempt from both. Can the TAFP use the same relief flag as the TFE?', True),
    ('TFE / TAFP', 261, 9148083, 'Different', '(b) missing 50% relief · (e) payment to the franc', 0.75, 'Same 7.5%. Dev: only the total exemption (58206 = 1); no 50% relief. v5: 0 / 50% / 100% and payment to the whole franc (technical convention; Art. 190 has no rounding rule).', 'CGI Art. 190 (p. 61); Art. 158', 'Ours', 0.95, 'Same relief question as the TAFP. And how do you pay a fraction of a franc on the TFE (7.5% can leave 0.5 XAF)?', False),
    ('Bases', None, 9148011, 'Only ours', '(d) structure', None, 'Base salary in its own account (58109) — measure of the 30% and 3.5% limits.', 'CGI Art. 45-13°, 47-I', 'n/a', None, '', False),
    ('Exemptions', None, 9148015, 'Only ours', '(d) structure', None, 'The nine Art. 46 caps and the 15% Art. 45-2° limit as ceiling accounts (Dev puts the % inside each formula).', 'CGI Art. 46-III; Art. 45-2°', 'n/a', None, '', False),
    ('Exemptions', None, 9148023, 'Only ours', '(d) with an error on their side', None, 'Plan-social severance exempt only with flag 58210; the Dev exempts all severance from the gross instead (row 17).', 'CGI Art. 45-10° (p. 30)', 'Ours', 0.95, 'See row 17 (severance).', False),
    ('Exemptions', None, 9148024, 'Only ours', '(b) missing in their design', None, 'Function-expense allowances and fixed per diem exempt up to 15% of pay. Wage type 6287x proposed (not in WTC V3.0).', 'CGI Art. 45-2° (p. 29)', 'Ours', 0.85, 'Art. 45-2° exempts function-expense allowances and fixed per diem up to 15% of pay. Is there a wage type for them? We propose 6287x.', True),
    ('Exemptions', None, 9148025, 'Only ours', '(b) missing in their design', None, 'Leave travel ticket exempt up to one ticket a year per person (annual limit from a new DD field 58223).', 'CGI Art. 45-15° (p. 30)', 'Ours', 0.75, 'Art. 45-15° exempts one leave ticket a year per person. Can we add a DD field with the annual fare limit?', False),
    ('Levies', None, 9148091, 'Only ours', '(b) missing in their design', None, 'Food-security levy, 400 XAF a month per employee, employee deduction, recovered as IRPP.', 'CGI Arts. 837–839 (p. 166)', 'Ours', 1.0, 'The PSA (400 FCFA a month per employee, Arts. 837–839) is not in the design. Can we add it as an employee deduction and a WTC code (2570)?', True),
]
assert sorted(r[1] for r in RC if r[1]) == sorted(DEVBY), 'every Dev regulation must appear once'
assert set(r[2] for r in RC) == set(V5BY), 'every v5 regulation must appear'

# ---------------------------------------------------------------- legal themes (LEI-VEREDITOS R1 + (b), re-read for v5)
LT = [
    (1, 'IRPP scale', 'same rates/thresholds', 'same', 'Both', 1.0, 'Art. 1-IV, p. 14'),
    (2, 'IRPP rounding', 'FLOOR(x+0.5)', 'FLOOR(x+0.5), technical convention', 'No rule', None, 'no rule in the CGI; Art. 847 barème not obtained'),
    (3, 'EE CNPS deducted from IRPP', 'yes', 'yes', 'Both', 1.0, 'Art. 47-I, p. 30'),
    (4, 'Family allowance cap', '5,000 × dependants', '5,000 × children − CNPS allowance', 'Ours', 0.95, 'Art. 45-4°, p. 29'),
    (5, 'Transport 30%', 'yes', 'yes', 'Both', 1.0, 'Art. 45-13°, p. 30'),
    (6, 'Transport only if paid to all staff', 'no', 'yes (58207)', 'Ours', 1.0, 'Art. 45-13°, p. 30'),
    (7, 'Severance: plan social vs individual (IRPP)', 'all exempt', 'only plan social exempt', 'Ours', 0.95, 'Arts. 44-I, 45-10°, p. 29–30'),
    (8, 'Supplementary pension: 3.5% cap, compulsory only', 'no cap, voluntary deducted', 'cap, compulsory only', 'Ours', 0.95, 'Art. 47-I/II, p. 30'),
    (9, 'Non-resident: rate', '18%', 'progressive scale', 'Ours', 0.85, 'Arts. 44-II-2°, 847, 116, 2-VI, 60'),
    (10, 'Non-resident: base', 'gross, no Art. 45', 'same as residents (Arts. 45–47)', 'Ours', 0.85, 'Art. 45 « Sont affranchis de l’Impôt »'),
    (11, 'Non-resident: TFE / TAFP', 'yes', 'yes', 'Both', 0.95, 'Arts. 187, 173'),
    (12, 'Non-resident: CNPS', 'all branches', 'all branches (flags only for seconded staff)', 'Both', 0.80, 'CNPS guide p. 6'),
    (13, 'Disabled / young graduate / worker: IRPP and TF/TA exemptions', 'IRPP only, no age / regime test, no workers, no TF/TA', 'Arts. 3-4°, 45-18°, 188-10°, 174-3° (worker under 35: 60%)', 'Ours', 0.85, 'Arts. 3-4°, 45-18°, 188-10°, 174-3°'),
    (14, 'CNPS rates', '3.5 / 5 / 7.5 / 4', 'same', 'Both', 0.95, 'Dec. 1635, 1636/2009; guide p. 8'),
    (15, 'CNPS floor and ceiling', '60,000 / 500,000', 'same', 'Both', 0.85, 'Dec. 1635 art. 4; guide p. 7, 9'),
    (16, 'CNPS floor in a month without pay', 'applies', 'not applied', 'Ours', 0.75, 'guide p. 7'),
    (17, 'Family allowance outside CNPS', 'yes', 'yes', 'Both', 0.90, 'guide p. 8; Dec. 1635 art. 3'),
    (18, 'Meal cash 6566x outside CNPS', 'out', 'out', 'Both', 0.75, 'guide p. 7 (prime de panier)'),
    (19, '6286x meal / food allowance', 'IRPP, TF, TA; CNPS out by omission', 'IRPP, TF, TA and CNPS', 'Ours', 0.75, 'Art. 44-I; Dec. 1635 art. 3'),
    (20, 'BIK: forfait vs MIN(real; %)', 'forfait', 'MIN', 'Ours', 0.85, 'Art. 46-III/V, p. 30'),
    (21, 'BIK percentages', 'same', 'same', 'Both', 1.0, 'Art. 46-III, p. 30'),
    (22, 'BIK: base of the %', '58105 incl. benefits', 'cash only', 'Ours', 0.90, 'Art. 46-I/II, p. 30'),
    (23, 'BIK in TF / TA at real value', 'yes', 'yes', 'Both', 0.95, 'Arts. 189-2°, 173'),
    (24, 'Schooling allowance 6274x / scholarship 6580x', 'out of everything', '6274x taxable; 6580x out of IRPP, in TF/TA/CNPS', 'Ours', 0.75, 'Art. 45-9°; Arts. 173, 189; Dec. 1635 art. 3'),
    (25, 'Health insurance 65630 in IRPP', 'out', 'taxable', 'Ours', 0.80, 'Art. 45 (no exemption); Art. 9-I'),
    (26, 'Leave ticket, per diem, relocation', 'out of everything', 'ticket: 1 a year exempt; per diem: 15%; TF/TA in', 'Ours', 0.75, 'Art. 45-2°, 45-15°; Arts. 189-1°, 173'),
    (27, 'TFE 7.5%', 'yes', 'yes', 'Both', 1.0, 'Art. 190, p. 61'),
    (28, 'TF / TA base without Art. 45 carve-outs', 'carve-outs', 'broad base', 'Ours', 0.90, 'Arts. 189-1°, 173'),
    (29, 'TAFP 1.2% and rounding', 'yes', 'yes', 'Both', 1.0, 'Arts. 178, 177, p. 60'),
    (30, 'TF / TA relief 0 / 50 / 100%', 'TF total only', 'TF and TA, 50% and 100%', 'Ours', 0.95, 'Art. 158, p. 56; LF 2020 Art. 14'),
    (31, 'Reporting limit 58106 and rate 58131', 'yes', 'yes', 'Not law', None, 'report parameter'),
    (32, 'Late penalties and TAFP training credit', 'notionals incl. TAFP credit', 'none (credit goes against IS)', 'Ours', 0.85, 'LF 2026 Art. 47; Arts. 1051–1052'),
    (33, '15% function-expense exemption (no 30% abatement)', 'missing', 'built (9148024)', 'Ours', 0.85, 'Art. 45-2°, p. 29; Art. 47'),
    (34, 'PSA 400 FCFA a month', 'missing', 'built (9148091)', 'Ours', 1.0, 'Arts. 837–839, p. 166'),
    (35, 'TFE fraction of a franc', 'not rounded (engine pays ?)', 'paid to the franc, technical convention', 'No rule', None, 'Art. 190 has no rule'),
    (36, 'TAFP: only regular gratifications', 'one-time bonus out of TF and TA', 'out of TA only', 'Ours', 0.70, 'Art. 173 « servies régulièrement »; Art. 189-1°'),
    (37, 'Transport in the CNPS base', 'only exempt 30% out', 'out in full (front decision, pending ok)', 'Ours', 0.75, 'CNPS guide p. 8 (decrees silent)'),
    (38, '62867 Death allowance', 'taxable', 'taxable (front decision, pending ok)', 'Open', 0.65, 'Art. 45-11° « capital décès »'),
    (39, 'Worker (ouvrier) age limit in Art. 3-4°', 'no worker category', 'under 35 (front decision, 60%)', 'Open', 0.60, 'Art. 3-4° × Arts. 188-10°, 174-3°'),
    (40, 'Irregular payments: annualise ×12 or cumulative', 'annualise', 'annualise (A26)', 'Open', 0.50, 'Arts. 1-I, 1-IV, 847 (barème not obtained)'),
]

# ---------------------------------------------------------------- Results: both engines on the 12 scenarios + 20 extras
LINES = [('Cash gross 58105', lambda A, d: A.get('58105', 0)), ('IRPP gross 58008', lambda A, d: A.get('58008', 0)),
         ('CNPS gross 58130', lambda A, d: A.get('58130', 0)), ('CNPS insurable 58550', lambda A, d: A.get('58550', 0)),
         ('TFE base 58563', lambda A, d: A.get('58563', 0)), ('TAFP base 58534', lambda A, d: A.get('58534', 0)),
         ('Transport exempt 58104', lambda A, d: A.get('58104', 0)), ('Family exempt 58108', lambda A, d: A.get('58108', 0)),
         ('EE CNPS deduction 58100', lambda A, d: A.get('58100', 0)), ('Retirement deduction 58101', lambda A, d: A.get('58101', 0)),
         ('Taxable income 58552', lambda A, d: A.get('58552', 0)), ('IRPP (2552 + 2592)', lambda A, d: A.get('2552', 0) + A.get('2592', 0)),
         ('TFE 2563', lambda A, d: A.get('2563', 0)), ('TAFP 2534', lambda A, d: A.get('2534', 0)),
         ('CNPS EE PVID 3.5% (ours 2551 / theirs 2550)', lambda A, d: A.get('2550' if d else '2551', 0)),
         ('CNPS ER PFM 7.5% (ours 2550 / theirs 2551)', lambda A, d: A.get('2551' if d else '2550', 0)),
         ('CNPS ER PVID 5% 2537', lambda A, d: A.get('2537', 0)), ('CNPS ER AT/MP 4% 2560', lambda A, d: A.get('2560', 0)),
         ('PSA 2570', lambda A, d: A.get('2570', 0))]
PSA_CAUSE = ('PSA exists only in v5 and v6 (not in v4 or the Dev)', 'Ours (100%) — CGI Arts. 837–839')
CAUSE = {
    '1': None, '3': None, 'E6': None, 'E18': None, 'E19': None,
    '2': ('Dev applies the CNPS floor with no pay (9148161 has no 58130 > 0 test); v5 only in a month with pay', 'Ours (75%) — CNPS guide p. 7'),
    '4': ('Dev: BIK forfait on a 58105 that includes the benefit (9148010/041); v5: MIN(real; 20% of cash)', 'Ours (85%) — Art. 46-I/II/III'),
    '5': ('Dev excludes all severance 6218x from the IRPP gross (9148131); v5/v6 tax individual severance · TF: v6 (r3) also puts severance in the TF base, Dev / v4 / v5 leave it out', 'Ours (95% IRPP; 75% TF) — Arts. 44-I, 45-10°, 189-1°'),
    'E23': ('Medical insurance 6261x: v6 (r3) taxes it everywhere; v4 and v5 left it out of every base (matrix defect); Dev in IRPP, CNPS, TF, TA (626%%)', 'Both v6 and Dev (80%) — verdict 25; Arts. 9-I, 44-I'),
    'E24': ('Social allowance 6265x: v6 (r3) taxes it everywhere; v4 and v5 left 62651–62653 out of every base; Dev in (626%%)', 'Both v6 and Dev (85%) — Art. 44-I'),
    'E25': ('EOS gratuity 62900: v6 keeps it out of the CNPS and (r3) of the TA; Dev in CNPS and TA', 'Ours (60–75%) — Dec. 1635 art. 3; Art. 173'),
    'E26': ('Phone cash 6561x: v6 (r3) in the TF/TA base; v4 and v5 kept it out by an exact No; Dev differs on the CNPS / TF base it uses', 'Ours (85%) — Arts. 173, 189-1°'),
    '6': ('Dev deducts the pension without the 3.5% cap (9148181)', 'Ours (95%) — Art. 47-I'),
    '7': ('CNPS: v5 takes the whole transport out (guide p. 8, front decision pending the user’s ok), Dev only the exempt 30% · TF/TA: Dev takes exempt transport out, v5 keeps it', 'Ours (75% CNPS; 90% TF/TA) — guide p. 8; Arts. 173, 189'),
    '8': ('TF/TA: Dev takes 6276x out (9148141/151), v5 keeps it · IRPP 1 XAF: Dev band limits x.99', 'Ours (90%) — Arts. 173, 189-1°, 1-IV'),
    '9': ('Dev has no 50% relief and no TAFP relief (input 58206 = 0 in the Dev: its flag is 0/1)', 'Ours (95%) — Art. 158'),
    '10': ('v5 exempts TF/TA on the pay of a young graduate under 35 at a real-regime entity; Dev does not', 'Ours (90%) — Arts. 188-10°, 174-3°'),
    '11': ('IRPP: v5 progressive scale, Dev 18%', 'Ours (85%) — Arts. 44-II-2°, 847, 116'),
    '12': ('TF/TA: Dev takes 6276x out, v5 keeps it · IRPP 1 XAF: Dev band limits x.99', 'Ours (90%) — Arts. 173, 189-1°, 1-IV'),
    'E1': ('Dev counts dependants and does not impute the CNPS allowance (9148032) · TF/TA as scenario 8', 'Ours (95%) — Art. 45-4°'),
    'E2': ('6580x scholarship: Dev puts it in 58105 but out of IRPP, CNPS, TF/TA; v5 out of IRPP only, in TF/TA and CNPS', 'Ours (75%) — Art. 45-9°; Arts. 173, 189; Dec. 1635 art. 3'),
    'E3': ('6286x meal allowance: in CNPS in v5, out by omission in the Dev', 'Ours (75%) — Dec. 1635 art. 3'),
    'E4': ('6287x function allowance: not in the Dev matrices (code proposed by v5, R15); v5 taxes the excess over 15%', 'Ours (85%) — Art. 45-2°'),
    'E5': ('Dev has no worker category: v5 exempts IRPP (Art. 3-4°) and TF/TA (Arts. 188-10°, 174-3°)', 'Ours (85%; worker age 60%)'),
    'E7': ('Dev deducts the voluntary 2164x contribution', 'Ours (95%) — Art. 47-II'),
    'E8': ('Leave ticket 6255x: Dev leaves it out of every base; v5 taxes the excess over one ticket a year and keeps it in TF/TA', 'Ours (75%) — Art. 45-15°; Arts. 173, 189'),
    'E9': ('Per diem 62570 and 6287x: out of the Dev IRPP/TF/TA; v5 taxes the excess over the joint 15% cap', 'Ours (75%) — Art. 45-2°'),
    'E10': ('Dev: CNPS on every branch (no eligibility flags) and 18%; v5: branches off for a seconded employee, progressive scale', 'Ours (80%) — guide p. 6; Arts. 44-II-2°, 847'),
    'E11': ('6274x: out of every Dev base; v5 taxable everywhere (cash allowance, not a « bourse »)', 'Ours (75%) — Art. 45-9° a contrario; Dec. 1635 art. 3'),
    'E12': ('Dev exempts every young graduate within 60 months; v5 needs under 35 at recruitment', 'Ours (90%) — Art. 3-4°'),
    'E13': ('Dev exempts every young graduate within 60 months; v5 needs a real-regime employer', 'Ours (90%) — Art. 3-4°'),
    'E14': ('TF/TA: v5 still exempts the worker under 35 (no period in Arts. 188-10°, 174-3°); Dev has no worker category', 'Ours (85%)'),
    'E15': ('Dev takes the one-time bonus 6222x out of the TFE (6222% No); v5 keeps it in the TFE and takes it out of the TAFP only', 'Ours (70%) — Art. 189-1°; Art. 173'),
    'E16': ('6251x: Dev gives no 30% exemption (matrix 6252% only) and keeps it in CNPS; v5 exempts 30% and takes it out of CNPS', 'Ours (75%) — Art. 45-13°; guide p. 8'),
    'E17': ('Pension 6264x: Dev includes it in IRPP, CNPS and TAFP; v5 out of IRPP (45-1°), CNPS and TA, in TF', 'Ours (85%) — Arts. 45-1°, 173, 187, 189-1°'),
    'E21': ('Car fuel arrears 65521: Dev counts it at the 10% forfait on its 58105; v6 at MIN(real; 10% of cash) and at real value in TF/TA — v4 and v5 left it out of IRPP / TF / TA (matrix series defect, fixed in v6 r2)', 'Ours v6 (85%) — Art. 46-III; Arts. 173, 189-2°'),
    'E22': ('Arrears 62101 taxed in the month paid by both (no retro_); differences only from the PSA', 'Both — CNPS guide p. 7; Art. 189-1°'),
    'E20': ('Dev exempts a young graduate with no start date; v5 taxes until the date is recorded · TF/TA: v5 exempts, Dev does not', 'Ours (85%) — Arts. 3-4°, 188-10°, 174-3°'),
}


def results():
    rows = []
    for name, inp, fo, exp in v5.SCEN + v5.EXTRA:
        key = name.split()[0]
        f = dict(v5.RES); f.update(fo)
        A = v5.run(inp, f)
        dinp = dict(inp)
        if '21600' in dinp:                      # the Dev deductible pension code (as comparar.py)
            dinp['21640'] = dinp.pop('21600')
        df = {k: f.get(k, 0) for k in ('58218', '58205', '58212')}
        df['58206'] = 1 if f.get('58206') == 1 else 0   # Dev flag is 0/1 only
        D = sim_dev.run_dev(dinp, df, DEV)
        out = []
        for lab, fn in LINES:
            out.append((lab, fn(A, False), fn(D, True)))
        for A_, inp_, dev in ((A, inp, False), (D, dinp, True)):
            pass
        cash = lambda i: sum(v for k, v in i.items() if k[:2] == '62')
        ben = lambda i: sum(v for k, v in i.items() if k[:2] in ('65', '79'))
        ded = lambda i: sum(v for k, v in i.items() if k[:2] == '21')
        ee = lambda X, d: X.get('2550' if d else '2551', 0)
        er = lambda X, d: X.get('2551' if d else '2550', 0) + X.get('2537', 0) + X.get('2560', 0)
        irpp = lambda X: X.get('2552', 0) + X.get('2592', 0)
        net_o = cash(inp) - ee(A, False) - irpp(A) - A.get('2570', 0) - ded(inp)
        net_d = cash(dinp) - ee(D, True) - irpp(D) - D.get('2570', 0) - ded(dinp)
        cost_o = cash(inp) + ben(inp) + er(A, False) + A.get('2563', 0) + A.get('2534', 0)
        cost_d = cash(dinp) + ben(dinp) + er(D, True) + D.get('2563', 0) + D.get('2534', 0)
        out += [('Net pay', net_o, net_d), ('Employer cost', cost_o, cost_d)]
        # check our side against the v5 validation tuple (EE, IRPP, TFE, TAFP, PSA, Net)
        got = (ee(A, False), irpp(A), A.get('2563', 0), A.get('2534', 0), A.get('2570', 0), net_o)
        assert all(abs(g - e) < 0.005 for g, e in zip(got, exp)), (name, got, exp)
        typ = 'Scenario' if key[0].isdigit() else 'Extra check'
        for lab, o, d in out:
            if abs(o - d) < 0.5:
                cause, closer = '', ''
            elif lab == 'PSA 2570' or (CAUSE.get(key) is None):
                cause, closer = PSA_CAUSE
            elif lab in ('Net pay', 'Employer cost') and set(l for l, a, b in out if abs(a - b) >= 0.5) <= {'PSA 2570', 'Net pay'}:
                cause, closer = PSA_CAUSE
            else:
                cause, closer = CAUSE[key]
            rows.append((key, name, typ, lab, round(o, 2), round(d, 2), cause, closer))
    return rows


# ---------------------------------------------------------------- Matrices: code by code over WTC V3.0
def wtc_codes():
    wb = openpyxl.load_workbook(WTC, read_only=True, data_only=True)
    ws = wb['Wage Type Catalogue']
    codes = []
    for r in ws.iter_rows(min_row=2, values_only=True):
        if r[0] is None:
            continue
        c = str(int(r[0])) if isinstance(r[0], (int, float)) else str(r[0]).strip()
        if c.startswith('58') or len(c) != 5:      # intermediates, flags and tax accounts are not pay elements
            continue
        codes.append((c, r[1] or ''))
    return codes


PERIM = [('Cash gross (BIK cap base)', 10, 9148012), ('IRPP gross', 131, 9148041), ('CNPS base', 155, 9148051), ('TFE base', 151, 9148081),
         ('TAFP base', 141, 9148082), ('Taxable income', 191, 9148071), ('Non-resident base', 11, 9148074), ('Transport exemption', 31, 9148021),
         ('Family exemption', 33, 9148022), ('Retirement deduction', 181, 9148061),
         ('BIK housing', 41, 9148031), ('BIK vehicle', 51, 9148032), ('BIK food', 61, 9148033), ('BIK furnishings', 71, 9148034),
         ('BIK domestic', 81, 9148035), ('BIK electricity', 91, 9148036), ('BIK water', 101, 9148037), ('BIK telephone', 111, 9148038),
         ('BIK gas', 121, 9148039), ('15% function allowance', None, 9148024), ('Leave ticket', None, 9148025)]
MAINDIFF = {
    'Cash gross (BIK cap base)': 'Theirs: benefits in kind 65%%% at full value, pensions 6264x, scholarship. Ours: 6286x, leave ticket, per diem, 6287x (each relieved by its exemption).',
    'IRPP gross': 'Theirs excludes severance 6218x, 6274x, health insurance 65630. Ours excludes the 6580x scholarship (Art. 45-9°).',
    'CNPS base': 'Ours: whole transport out (6251x/6252x), 6286x, 6274x, 6580x in. Theirs: 58104 subtraction only.',
    'TFE base': 'Theirs takes exempt transport, 6276x, 6222x out. Ours adds pensions 6264x.',
    'TAFP base': 'Theirs takes exempt transport and 6276x out. Ours takes 6222x and 6264x out (Art. 173).',
    'Taxable income': 'Ours adds 58113, 58114, 58115 (plan social, 15%, ticket).',
    'Non-resident base': 'Theirs: gross pay codes; ours: 58552 (the scale base).',
    'Transport exemption': 'Ours adds 6251x.',
    'Family exemption': 'Ours adds 6278x and 62866.',
    'Retirement deduction': 'Theirs: 2164x voluntary; ours: 216xx compulsory, 2164x out.',
}


# a code reaches a perimeter directly or through an intermediate account the perimeter adds (e.g. 58105 in the IRPP gross,
# 58120-58128 capped BIK values): accounts produced positively by another regulation are expanded to that regulation's matrix.
DEVPROD, V5PROD = {}, {}
for r in DEV:
    for b in r['bands']:
        if b['creditAccount'] in ('99999', '99998') and b['debitAccount'] not in ('99999', '99998'):
            DEVPROD.setdefault(b['debitAccount'], r['ordinal'])
for r in v5.R:
    for b in r['bands']:
        if b['cred'] in ('99999', '99998') and b['deb'] not in ('99999', '99998'):
            V5PROD.setdefault(b['deb'], r['id'])


def dev_in(o, code, seen=()):
    rules = DEVBY[o]['taxabilityRules']
    if sim_dev.matrix_sum(rules, {code: 1.0}) > 0:
        return True
    for m in rules:
        a = m['account']
        if not m['pattern'] and m['isTaxable'] and a in DEVPROD and DEVPROD[a] not in seen and DEVPROD[a] != o:
            if dev_in(DEVPROD[a], code, seen + (o,)):
                return True
    return False


def v5_in(i, code, seen=()):
    mat = V5BY[i]['matrix']
    if v5.matrix_sum(mat, {code: 1.0}) > 0:
        return True
    for a, pat, y in mat:
        if not pat and y == 'Yes' and a in V5PROD and V5PROD[a] not in seen and V5PROD[a] != i:
            if v5_in(V5PROD[a], code, seen + (i,)):
                return True
    return False


def perim_col(dev_o, v5_id, codes):
    col = []
    for c, _ in codes:
        d = bool(dev_o) and dev_in(dev_o, c)
        o = v5_in(v5_id, c)
        col.append('Both' if d and o else 'Only theirs' if d else 'Only ours' if o else '—')
    return col


# ---------------------------------------------------------------- open points
OPEN = [
    ('Transport allowance in the CNPS base', 'Out in full (6251x, 6252x) — technical decision of the Chade front, pending the user’s ok', 'Only the exempt 30% out (v4, Dev, correcoes.md 2026-07-07): scenario 7 EE CNPS 10,500 → 11,550', 'CNPS guide 2019 p. 8 (level A−); Dec. 1635 art. 3 / 1636 art. 2 do not name transport', 0.75, 'User ok, then correct correcoes.md and the hub'),
    ('62867 Death allowance', 'Taxable everywhere — technical decision of the front, pending the user’s ok', 'Capital décès: IRPP-exempt (Art. 45-11°), still in TF/TA (Arts. 189-1°, 173) and CNPS (Dec. 1635 art. 3) — needs its own code (R28)', 'WTC V3.0 code name; Art. 45-11°', 0.65, 'User ok; ask the Dev / client what the code pays'),
    ('Worker (ouvrier) age limit in Art. 3-4°', 'Under 35 at recruitment, as Arts. 188-10° / 174-3° — technical decision, 60%', 'No age limit for workers: a worker hired at 40 pays IRPP 0 instead of 28,464 (E19)', 'Art. 3-4° (p. 15); DGI circular missing (R32)', 0.60, 'Source hunter: DGI circular on LFI 2025 Art. 23'),
    ('Irregular payments (severance, 13th month, bonuses)', 'Annualise the month ×12 (as the Dev)', 'Cumulative / YTD: scenario 5 withholds ≈ 117,898 instead of 208,600; scenario 3 ≈ 11,100 less', 'Arts. 1-I, 1-IV, 847 — DGI barème not obtained (R23)', 0.50, 'Source hunter: DGI barème; question for the call'),
    ('CNPS annual ceiling (December regularisation)', '500,000 a month, no December regularisation built', 'YTD regularisation on 6,000,000 a year', 'CNPS guide p. 12', 0.90, 'Design with the Dev (engine YTD semantics)'),
    ('Equal band limits in the engine', 'incomeTo 800,000 = next incomeFrom', 'x.99 limits (Dev): 1 XAF lower at half a franc', 'Art. 1-IV; engine behaviour unknown (A21)', 0.90, 'Question for the call'),
    ('Missing sources', '—', '—', 'SMIG of 2026 (R22) · DGI barème (R23) · Dec. 1634/2009 text (R24) · CNPS valuation arrêté (R25) · CNPS circulars 2025 (R26) · Journal Officiel date of the 2009 decrees (R29) · diplomats outside CNPS/TF (R30) · DGI circular on Art. 3-4° (R32)', None, 'Source hunter'),
]


# ---------------------------------------------------------------- build
def build():
    wb = openpyxl.Workbook()
    S = wb.active; S.title = 'Summary'
    RCs = wb.create_sheet('Regulation Comparison')
    RS = wb.create_sheet('Results')
    MX = wb.create_sheet('Matrices')
    MD = wb.create_sheet('Matrix Detail')
    LG = wb.create_sheet('Legal Themes')
    OP = wb.create_sheet('Open points')

    # Regulation Comparison
    title(RCs, 'Regulation by regulation — Chad (our v5 × development team td_2026)',
          'Cause: (a) our error · (b) error or outdated in their design · (c) gap or contradiction in the research · (d) different modelling, both valid · (e) internal team convention not in the research.   ★ = most important to close on the call.', 'O')
    header(RCs, 4, ['#', 'Block', 'Development team regulation', 'Development team formula', 'Our regulation (v5)', 'Our formula (v5)', 'Status', 'Cause', 'Adherence', 'Difference', 'Weight (their regs)', 'Legal basis', 'Who is right per the law', 'Confidence', 'Question for the call'],
           [4, 12, 30, 46, 30, 46, 12, 22, 10, 48, 10, 34, 14, 11, 54])
    RCs.freeze_panes = 'C5'
    for i, (blk, o, vid, st, cause, adh, diff, legal, who, conf, q, star) in enumerate(RC, 1):
        r = 4 + i
        put(RCs, r, 1, i); put(RCs, r, 2, blk, True)
        put(RCs, r, 3, dev_name(o) if o else '—', True); put(RCs, r, 4, dev_text(o) if o else '—', code=True)
        put(RCs, r, 5, v5_name(vid), True); put(RCs, r, 6, v5_text(vid), code=True)
        put(RCs, r, 7, st, True, bg=STATUS_FILL[st], center=True); put(RCs, r, 8, cause)
        put(RCs, r, 9, adh, fmt='0%', center=True); put(RCs, r, 10, diff)
        put(RCs, r, 11, 1 if o else 0, center=True); put(RCs, r, 12, legal)
        put(RCs, r, 13, who, True, bg=WHO_FILL.get(who), center=True); put(RCs, r, 14, conf, fmt='0%', center=True)
        put(RCs, r, 15, (q + ' ★') if (q and star) else q, bold=bool(q))
    rc_last = 4 + len(RC)

    # Results
    title(RS, 'Both designs executed on the same cases', 'Ours = _build_v5.py run(); theirs = sim_dev.py on td.json (assumptions S1–S12 at the top of sim_dev.py). 12 scenarios + 20 extra checks of the v5 changes. Difference = theirs − ours. XAF.', 'J')
    header(RS, 4, ['Case', 'Scenario', 'Type', 'Output', 'Ours (v5)', 'Theirs (Dev)', 'Difference', 'Status', 'Cause', 'Closer to the law'], [6, 34, 12, 30, 14, 14, 13, 11, 60, 40])
    RS.freeze_panes = 'A5'
    rr = results()
    for i, (key, name, typ, lab, o, d, cause, closer) in enumerate(rr):
        r = 5 + i
        put(RS, r, 1, key, True); put(RS, r, 2, name); put(RS, r, 3, typ); put(RS, r, 4, lab)
        put(RS, r, 5, o, fmt=NUM); put(RS, r, 6, d, fmt=NUM)
        put(RS, r, 7, f'=F{r}-E{r}', fmt=NUM)
        put(RS, r, 8, f'=IF(ABS(E{r}-F{r})<1,"Same","Different")', True, center=True)
        put(RS, r, 9, cause); put(RS, r, 10, closer)
    rs_last = 4 + len(rr)
    rs_scen_last = 4 + sum(1 for x in rr if x[2] == 'Scenario')
    RS.conditional_formatting.add(f'H5:H{rs_last}', CellIsRule(operator='equal', formula=['"Same"'], fill=PatternFill('solid', bgColor='FFC6EFCE')))
    RS.conditional_formatting.add(f'H5:H{rs_last}', CellIsRule(operator='equal', formula=['"Different"'], fill=PatternFill('solid', bgColor='FFFFC7CE')))

    # Matrix Detail + Matrices
    codes = wtc_codes()
    N = len(codes)
    title(MD, f'Matrix detail — every WTC V3.0 pay element ({N}) × each perimeter', 'Both · Only theirs · Only ours · — (neither). Each design resolved with its own precedence rules (exact code > narrower pattern > wider pattern); a code also counts when it reaches the perimeter through an intermediate account (e.g. 58105 inside the IRPP gross). Intermediates 58xxx and tax accounts are left out.', 'C')
    header(MD, 4, ['Code', 'WTC V3.0 name'] + [p[0] for p in PERIM], [9, 34] + [11] * len(PERIM))
    MD.freeze_panes = 'C5'
    for i, (c, nm) in enumerate(codes):
        put(MD, 5 + i, 1, c); put(MD, 5 + i, 2, nm)
    for j, (lab, o, vid) in enumerate(PERIM):
        col = perim_col(o, vid, codes)
        for i, v in enumerate(col):
            cell = MD.cell(5 + i, 3 + j, v)
            cell.font = F(8); cell.alignment = CENTER; cell.border = BOX
            if v != '—':
                cell.fill = fill({'Both': GREEN, 'Only theirs': ORANGE, 'Only ours': BLUE}[v])
    md_last = 4 + N
    title(MX, f'Taxability matrices — code by code over all {N} WTC V3.0 codes',
          f'Similarity = common ÷ codes at least one design includes (codes both leave out are excluded). Agreement = (common + codes neither includes) ÷ {N}. Counts are live formulas over "Matrix Detail".', 'L')
    header(MX, 4, ['Perimeter', 'Their reg.', 'Theirs', 'Ours', 'Common', 'Only theirs', 'Only ours', 'Our reg.', 'Neither', 'Similarity (≥1 includes)', 'Agreement (all codes)', 'Main differences'],
           [26, 11, 9, 9, 9, 10, 10, 11, 9, 13, 13, 62])
    MX.freeze_panes = 'B5'
    for j, (lab, o, vid) in enumerate(PERIM):
        r = 5 + j
        L = openpyxl.utils.get_column_letter(3 + j)
        rng = f"'Matrix Detail'!{L}5:{L}{md_last}"
        put(MX, r, 1, lab, True); put(MX, r, 2, f'9148{o:03d}' if o else '—')
        put(MX, r, 3, f'=COUNTIF({rng},"Both")+COUNTIF({rng},"Only theirs")')
        put(MX, r, 4, f'=COUNTIF({rng},"Both")+COUNTIF({rng},"Only ours")')
        put(MX, r, 5, f'=COUNTIF({rng},"Both")'); put(MX, r, 6, f'=COUNTIF({rng},"Only theirs")')
        put(MX, r, 7, f'=COUNTIF({rng},"Only ours")'); put(MX, r, 8, str(vid))
        put(MX, r, 9, f'=COUNTIF({rng},"—")')
        put(MX, r, 10, f'=IF((C{r}+D{r}-E{r})=0,1,E{r}/(C{r}+D{r}-E{r}))', fmt='0.0%', center=True)
        put(MX, r, 11, f'=(E{r}+I{r})/{N}', fmt='0.0%', center=True)
        put(MX, r, 12, MAINDIFF.get(lab, 'Theirs: forfait on 58105 (the matrix only triggers the regulation); ours: the real benefit codes.' if lab.startswith('BIK') else 'Only in our design.'))
    mx_last = 4 + len(PERIM)
    pr = mx_last + 2
    put(MX, pr, 1, 'Pooled — all perimeters', True)
    for col in 'CDEFGI':
        put(MX, pr, ' ABCDEFGHI'.index(col), f'=SUM({col}5:{col}{mx_last})', True)
    put(MX, pr, 10, f'=E{pr}/(C{pr}+D{pr}-E{pr})', True, fmt='0.0%', center=True)
    put(MX, pr, 11, f'=(E{pr}+I{pr})/({N}*{len(PERIM)})', True, fmt='0.0%', center=True)
    MX.conditional_formatting.add(f'J5:J{mx_last}', CellIsRule(operator='lessThan', formula=['0.5'], fill=PatternFill('solid', bgColor=RED)))

    # Legal Themes
    title(LG, 'Statutory themes — who is right per the law', 'From LEI-VEREDITOS.md (R1 and § Revisão 2026-11-01 (b)), re-read against v5; themes 35–40 added with v5. "No rule" / "Not law" are left out of the legal-accuracy count; "Open" = not settled.', 'G')
    header(LG, 4, ['#', 'Theme', 'Development team', 'Our v5', 'Who is right per the law', 'Confidence', 'Legal basis'], [5, 40, 30, 34, 14, 11, 40])
    LG.freeze_panes = 'C5'
    for i, (n, th, dv, ov, who, conf, src) in enumerate(LT):
        r = 5 + i
        put(LG, r, 1, n); put(LG, r, 2, th, True); put(LG, r, 3, dv); put(LG, r, 4, ov)
        put(LG, r, 5, who, True, bg=WHO_FILL.get(who), center=True); put(LG, r, 6, conf, fmt='0%', center=True); put(LG, r, 7, src)
    lg_last = 4 + len(LT)

    # Open points
    title(OP, 'Open points — technical decisions pending the user and sources still missing', 'Each is written in the v5 design as the current position; none carries an open mark in the artefact (ASSUMPTIONS D1, D2, A21, A23, A26, A34; RESEARCH_GAPS R22–R32).', 'G')
    header(OP, 4, ['#', 'Point', 'Current position (v5)', 'Alternative and its effect', 'Source / what is missing', 'Confidence', 'Next step'], [4, 30, 40, 44, 44, 11, 30])
    for i, row in enumerate(OPEN, 1):
        r = 4 + i
        put(OP, r, 1, i); put(OP, r, 2, row[0], True); put(OP, r, 3, row[1]); put(OP, r, 4, row[2]); put(OP, r, 5, row[3])
        put(OP, r, 6, row[4], fmt='0%', center=True); put(OP, r, 7, row[5])

    # Summary
    S.column_dimensions['A'].width = 52; S.column_dimensions['B'].width = 16; S.column_dimensions['C'].width = 16; S.column_dimensions['D'].width = 14; S.column_dimensions['E'].width = 58
    S['A1'] = "Chad — our design v5 vs the development team's design td_2026 · similarity and legal accuracy"; S['A1'].font = F(13, True)
    S['A2'] = (f'Ours: chad-design-blueprint-claude-v5 ({len(v5.R)} regulations, 2026-11-01, after 2 QA rounds). Theirs: td_2026 ({len(DEV)} regulations, td.json = CT-A-588). '
               'Both executed locally (no engine run); WTC V3.0 export of 2026-11-01.')
    S['A2'].font = F(9); S.merge_cells('A1:E1'); S.merge_cells('A2:E2')
    RCr = "'Regulation Comparison'"

    def sec(r, text):
        S.cell(r, 1, text).font = F(11, True)

    def hdr(r, names):
        for i, n in enumerate(names, 1):
            c = S.cell(r, i, n); c.font = F(10, True); c.fill = fill(GREY); c.alignment = CENTER; c.border = BOX

    sec(4, 'SIMILARITY'); hdr(5, ['Lens', 'Similarity', 'Basis'])
    sim = [
        (f'Results — {len(v5.SCEN) + len(v5.EXTRA)} cases, {len(rr)} values', f'=COUNTIF(Results!H5:H{rs_last},"Same")/COUNTA(Results!H5:H{rs_last})', 'Both designs executed'),
        (f'Results — the {len(v5.SCEN)} scenarios only', f'=COUNTIF(Results!H5:H{rs_scen_last},"Same")/COUNTA(Results!H5:H{rs_scen_last})', f'{rs_scen_last - 4} values'),
        ('Structure — average per regulation', f"=SUMPRODUCT({RCr}!I5:I{rc_last},{RCr}!K5:K{rc_last})/SUMIFS({RCr}!K5:K{rc_last},{RCr}!I5:I{rc_last},\">=0\")", f'Weighted by their {len(DEV)} regulations'),
        ('Matrices — only codes at least one design includes', f'=Matrices!J{pr}', 'Common ÷ included by ≥1, pooled'),
    ]
    for i, (a, b, c) in enumerate(sim):
        r = 6 + i
        put(S, r, 1, a, True); put(S, r, 2, b, True, fmt='0%'); put(S, r, 3, c)
    put(S, 10, 1, 'OVERALL SIMILARITY — mean of results, structure and matrices', True, bg=BLUE)
    c = put(S, 10, 2, '=AVERAGE(B6,B8,B9)', True, fmt='0%', bg=BLUE); c.font = F(12, True)

    sec(12, 'LEGAL ACCURACY — themes the law resolves'); hdr(13, ['Measure', 'Our v5', 'Development team', 'Themes', 'Basis'])
    who = f'\'Legal Themes\'!E5:E{lg_last}'
    resolved = f'(COUNTIF({who},"Ours")+COUNTIF({who},"Dev")+COUNTIF({who},"Both")+COUNTIF({who},"Neither"))'
    put(S, 14, 1, 'Themes resolved by the law', True); put(S, 14, 4, f'={resolved}'); put(S, 14, 5, f'Of {len(LT)} themes; "Open", "No rule" and "Not law" left out')
    put(S, 15, 1, 'Right per the law (count)', True)
    put(S, 15, 2, f'=COUNTIF({who},"Ours")+COUNTIF({who},"Both")'); put(S, 15, 3, f'=COUNTIF({who},"Dev")+COUNTIF({who},"Both")'); put(S, 15, 5, '"Both" counts for each side')
    put(S, 16, 1, 'LEGAL ACCURACY — share of resolved themes', True, bg=BLUE)
    c = put(S, 16, 2, '=B15/D14', True, fmt='0%', bg=BLUE); c.font = F(12, True)
    c = put(S, 16, 3, '=C15/D14', True, fmt='0%', bg=BLUE); c.font = F(12, True)
    conf = f"'Legal Themes'!F5:F{lg_last}"
    put(S, 19, 1, 'Confidence-weighted legal accuracy', True)
    put(S, 19, 2, f'=(SUMIFS({conf},{who},"Ours")+SUMIFS({conf},{who},"Both"))/D14', fmt='0%')
    put(S, 19, 3, f'=(SUMIFS({conf},{who},"Dev")+SUMIFS({conf},{who},"Both"))/D14', fmt='0%')
    put(S, 19, 5, 'Each verdict weighted by its confidence — the verdicts are our reading of the law (LEI-VEREDITOS), not a ruling')
    put(S, 17, 1, 'Open themes (pending a decision or a source)', True); put(S, 17, 4, f'=COUNTIF({who},"Open")'); put(S, 17, 5, 'See "Open points"')
    rw = f'{RCr}!M5:M{rc_last}'
    rres = f'(COUNTIF({rw},"Ours")+COUNTIF({rw},"Dev")+COUNTIF({rw},"Both")+COUNTIF({rw},"Neither"))'
    put(S, 18, 1, 'By regulation row — right per the law', True)
    put(S, 18, 2, f'=(COUNTIF({rw},"Ours")+COUNTIF({rw},"Both"))/{rres}', fmt='0%'); put(S, 18, 3, f'=(COUNTIF({rw},"Dev")+COUNTIF({rw},"Both"))/{rres}', fmt='0%')
    put(S, 18, 4, f'={rres}'); put(S, 18, 5, 'Rows of "Regulation Comparison" with a legal verdict')

    sec(20, 'MATRIX SIMILARITY — TWO WAYS'); hdr(21, ['Measure', f'All {N} codes', 'Only codes ≥1 includes'])
    put(S, 22, 1, 'Codes both designs leave out', True); put(S, 22, 2, 'count as agreement'); put(S, 22, 3, 'excluded')
    put(S, 23, 1, 'Similarity', True, bg=BLUE); put(S, 23, 2, f'=Matrices!K{pr}', True, fmt='0.0%', bg=BLUE, center=True); put(S, 23, 3, f'=Matrices!J{pr}', True, fmt='0.0%', bg=BLUE, center=True)
    put(S, 23, 5, 'The overall similarity uses the stricter measure, on the right.')

    sec(25, 'SIMILARITY BY BLOCK (structure)'); hdr(26, ['Block', 'Similarity', 'Their regulations'])
    for i, blk in enumerate(['Bases', 'Exemptions', 'BIK', 'CNPS', 'IRPP', 'TFE / TAFP', 'Levies']):
        r = 27 + i
        put(S, r, 1, blk, True)
        if blk == 'Levies':
            put(S, r, 2, 'only ours (PSA)'); put(S, r, 3, 0)
            continue
        put(S, r, 2, f"=SUMPRODUCT(({RCr}!B5:B{rc_last}=\"{blk}\")*{RCr}!I5:I{rc_last}*{RCr}!K5:K{rc_last})/SUMIFS({RCr}!K5:K{rc_last},{RCr}!B5:B{rc_last},\"{blk}\",{RCr}!I5:I{rc_last},\">=0\")", fmt='0%')
        put(S, r, 3, f"=SUMIFS({RCr}!K5:K{rc_last},{RCr}!B5:B{rc_last},\"{blk}\",{RCr}!I5:I{rc_last},\">=0\")")

    sec(35, 'QUESTIONS FOR THE CALL'); hdr(36, ['Measure', 'Count'])
    q = f'{RCr}!O5:O{rc_last}'
    put(S, 37, 1, 'Rows with a question', True); put(S, 37, 2, f'=COUNTIF({q},"?*")')
    put(S, 38, 1, '★ priority questions', True); put(S, 38, 2, f'=COUNTIF({q},"*★*")')
    S['A40'] = ('Reading: the two designs give the same pay in the plain cases; they part where the law is specific — benefit caps, severance, pension cap, non-resident, TF/TA bases and relief, '
                'CNPS details — and our v5 is on the side of the text in almost all of them. The open points are decisions pending the user and two DGI / CNPS sources.')
    S['A40'].font = F(9, True); S['A40'].alignment = WRAP; S.merge_cells('A40:E40'); S.row_dimensions[40].height = 42

    for ws in wb.worksheets:
        ws.page_setup.orientation = 'landscape'
    wb.save(OUT)
    return dict(rc=len(RC), rs=len(rr), codes=N, perim=len(PERIM), lt=len(LT), q=sum(1 for x in RC if x[10]), star=sum(1 for x in RC if x[10] and x[11]))


# ================================================================ MULTI-VERSION WORKBOOK (v4 · v5 · v6 vs Dev), added 2026-11-02
OUT_MULTI = os.path.join(HERE, 'TD_Design_Comparison_v4_v5_v6_vs_Dev.xlsx')


def _load(path, name):
    s = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


v4 = _load(os.path.join(CHAD, '2026-10-29-design-v4', '_build_v4.py'), 'v4')
v6 = _load(os.path.join(CHAD, '2026-11-02-design-v6', '_build_v6.py'), 'v6')
VERS = [('v4', v4, '2026-10-29, before the legal review'), ('v5', v5, '2026-11-01, reviewed against the law'), ('v6', v6, '2026-11-02, v5 rules in the Dev structure')]
VBY = {k: {r['id']: r for r in m.R} for k, m, _ in VERS}
DED = {'v4': ('58141', '58142'), 'v5': ('58100', '58101'), 'v6': ('58100', '58101')}

# pairing: Dev ordinal → regulation of each version (from the v5 pairing of RC)
V6_FROM_V5_ONLY = {9148011: 9148175, 9148015: None, 9148023: 9148034, 9148024: 9148035, 9148025: 9148036, 9148091: 9148271}


def pair(row):
    blk, o, vid = row[0], row[1], row[2]
    p4 = vid if vid in VBY['v4'] else None
    if o:
        p6 = 9148192 if o == 11 else 9148000 + o
    else:
        p6 = V6_FROM_V5_ONLY[vid]
    return p4, vid, p6


def gtext(ver, i):
    if i is None:
        return '—'
    r = VBY[ver][i]
    L = [f"{i} · {r['ttype']} · {r['trg']}"]
    if r['pre']:
        L.append(f"Pre: {r['pre']}")
    for b in r['bands']:
        s = []
        if b['f'] != '' or b['t'] != '':
            s.append(f"{n3(b['f'])}–{n3(b['t'])}")
        if b['ee'] != '':
            s.append(f"EE {n3(b['ee'])}")
        if b['er'] != '':
            s.append(f"ER {n3(b['er'])}")
        if b['floor'] != '' or b['ceil'] != '':
            s.append(f"floor {n3(b['floor'])} / ceil {n3(b['ceil'])}")
        if b['ceilacc']:
            s.append(f"ceilingAccount {b['ceilacc']}")
        if b['formula']:
            s.append(b['formula'])
        if b['assertion']:
            s.append(f"[{b['assertion']}]")
        s.append(f"→ {b['deb']}/{b['cred']}")
        L.append('  '.join(s))
    L.append(f"Matrix: {len(r['matrix'])} rules")
    return '\n'.join(L)


def _num(x):
    return None if x in (None, '') else round(float(x), 6)


def form_score(o, ver, i):
    """Structural adherence to the Dev regulation, computed the same way for every version (0–1)."""
    d, r = DEVBY[o], VBY[ver][i]
    jac = lambda a, b: 1.0 if not a and not b else len(a & b) / len(a | b)
    dev_acc = {(b['debitAccount'], b['creditAccount']) for b in d['bands']}
    our_acc = {(b['deb'], b['cred']) for b in r['bands']}
    dev_rate = {_num(b['employeeRate'] if b['employeeRate'] is not None else b['employerRate']) for b in d['bands']}
    our_rate = {_num(b['ee'] if b['ee'] != '' else b['er']) for b in r['bands']}
    dev_f = {b['formula'] or '' for b in d['bands']}
    our_f = {b['formula'] or '' for b in r['bands']}
    dev_m = {(m['account'], m['pattern'] or '', m['isTaxable']) for m in d['taxabilityRules']}
    our_m = {(a, p, y == 'Yes') for a, p, y in r['matrix']}
    parts = [r['id'] == 9148000 + o, r['name'] == d['name'], r['trg'] == d['taxRuleGroup'], r['ttype'].lower() == d['taxationType'].lower(),
             (r['pre'] or '') == (d.get('assertion') or ''), jac(dev_acc, our_acc), jac(dev_rate, our_rate), jac(dev_f, our_f), jac(dev_m, our_m)]
    return sum(float(x) for x in parts) / len(parts)


V4_THEME = {1: ('same', 'Both'), 2: ('FLOOR(x+0.5)', 'No rule'), 3: ('yes', 'Both'), 4: ('fully exempt', 'Dev'), 5: ('yes', 'Both'), 6: ('yes (58207)', 'Ours'),
            7: ('only plan social exempt', 'Ours'), 8: ('3.5% cap, voluntary deducted', 'Ours'), 9: ('18%', 'Neither'), 10: ('cash net of Art. 45', 'Ours'),
            11: ('not computed', 'Dev'), 12: ('branch flags', 'Dev'), 13: ('IRPP only, no TF/TA exemption', 'Neither'), 14: ('same', 'Both'), 15: ('same', 'Both'),
            16: ('not applied', 'Ours'), 17: ('yes', 'Both'), 18: ('in', 'Dev'), 19: ('only 62867', 'Dev'), 20: ('MIN', 'Ours'), 21: ('same', 'Both'),
            22: ('cash only', 'Ours'), 23: ('yes', 'Both'), 24: ('taxable everywhere', 'Neither'), 25: ('taxable', 'Ours'), 26: ('out of everything', 'Neither'),
            27: ('yes', 'Both'), 28: ('broad base', 'Ours'), 29: ('yes', 'Both'), 30: ('TF and TA, 50% and 100%', 'Ours'), 31: ('yes', 'Not law'),
            32: ('none', 'Ours'), 33: ('missing', 'Neither'), 34: ('missing', 'Neither'), 35: ('FLOOR(x+0.5)', 'No rule'), 36: ('in TF and TA', 'Neither'),
            37: ('only exempt 30% out', 'Neither'), 38: ('taxable', 'Open'), 39: ('no worker category', 'Open'), 40: ('annualise', 'Open')}


def results_multi():
    rows = []
    for name, inp, fo, exp in v6.SCEN + v6.EXTRA:      # v6 cases = the 32 v5 cases + E21, E22 (v6 QA round 2)
        key = name.split()[0]
        f = dict(v5.RES); f.update(fo)
        outs = {}
        for ver, m, _ in VERS:
            fv = dict(m.RES); fv.update(f)
            outs[ver] = m.run(inp, fv)
        dinp = dict(inp)
        if '21600' in dinp:
            dinp['21640'] = dinp.pop('21600')
        df = {k: f.get(k, 0) for k in ('58218', '58205', '58212')}
        df['58206'] = 1 if f.get('58206') == 1 else 0
        D = sim_dev.run_dev(dinp, df, DEV)

        def lines(A, ver, ip):
            dev = ver == 'dev'
            e, r_ = ('58100', '58101') if dev else DED[ver]
            ee = A.get('2550' if dev else '2551', 0)
            pfm = A.get('2551' if dev else '2550', 0)
            irpp = A.get('2552', 0) + A.get('2592', 0)
            cash = sum(v for k, v in ip.items() if k[:2] == '62')
            ben = sum(v for k, v in ip.items() if k[:2] in ('65', '79'))
            ded = sum(v for k, v in ip.items() if k[:2] == '21')
            g = A.get
            return [('Cash gross 58105', g('58105', 0)), ('IRPP gross 58008', g('58008', 0)), ('CNPS gross 58130', g('58130', 0)),
                    ('CNPS insurable 58550', g('58550', 0)), ('TFE base 58563', g('58563', 0)), ('TAFP base 58534', g('58534', 0)),
                    ('Transport exempt 58104', g('58104', 0)), ('Family exempt 58108', g('58108', 0)),
                    ('EE CNPS deduction (v4 58141 · v5/v6/Dev 58100)', g(e, 0)), ('Retirement deduction (v4 58142 · v5/v6/Dev 58101)', g(r_, 0)),
                    ('Taxable income 58552', g('58552', 0)), ('IRPP (2552 + 2592)', irpp), ('TFE 2563', g('2563', 0)), ('TAFP 2534', g('2534', 0)),
                    ('CNPS EE PVID 3.5% (ours 2551 · Dev 2550)', ee), ('CNPS ER PFM 7.5% (ours 2550 · Dev 2551)', pfm),
                    ('CNPS ER PVID 5% 2537', g('2537', 0)), ('CNPS ER AT/MP 4% 2560', g('2560', 0)), ('PSA 2570', g('2570', 0)),
                    ('Net pay', cash - ee - irpp - g('2570', 0) - ded), ('Employer cost', cash + ben + pfm + g('2537', 0) + g('2560', 0) + g('2563', 0) + g('2534', 0))]
        Ld = lines(D, 'dev', dinp)
        Lv = {ver: lines(outs[ver], ver, inp) for ver, _, _ in VERS}
        if key not in v6.V1_CASES:
            for v6l, v5l in zip(Lv['v6'], Lv['v5']):
                assert abs(v6l[1] - v5l[1]) < 0.005, ('v6 must equal v5', name, v6l, v5l)
        typ = 'Scenario' if key[0].isdigit() else 'Extra check'
        for k, (lab, dv) in enumerate(Ld):
            o5 = Lv['v6'][k][1]          # causes describe the current rules (v6 = v5 except E21)
            if abs(o5 - dv) < 0.5:
                cause, closer = '', ''
            elif lab == 'PSA 2570' or CAUSE.get(key) is None:
                cause, closer = PSA_CAUSE
            elif lab in ('Net pay', 'Employer cost') and all(abs(Lv['v5'][j][1] - Ld[j][1]) < 0.5 for j in range(len(Ld)) if Ld[j][0] not in ('PSA 2570', 'Net pay')):
                cause, closer = PSA_CAUSE
            else:
                cause, closer = CAUSE[key]
            rows.append((key, name, typ, lab, round(dv, 2), round(Lv['v4'][k][1], 2), round(Lv['v5'][k][1], 2), round(Lv['v6'][k][1], 2), cause, closer))
    return rows


def ver_in(ver, i, code, seen=()):
    m = dict(VERS_M)[ver]
    mat = VBY[ver][i]['matrix']
    if m.matrix_sum(mat, {code: 1.0}) > 0:
        return True
    prod = PROD[ver]
    for a, pat, y in mat:
        if not pat and y == 'Yes' and a in prod and prod[a] not in seen and prod[a] != i:
            if ver_in(ver, prod[a], code, seen + (i,)):
                return True
    return False


VERS_M = [(k, m) for k, m, _ in VERS]
PROD = {}
for _k, _m, _ in VERS:
    PROD[_k] = {}
    for _r in _m.R:
        for _b in _r['bands']:
            if _b['cred'] in ('99999', '99998') and _b['deb'] not in ('99999', '99998'):
                PROD[_k].setdefault(_b['deb'], _r['id'])

# perimeter: (label, Dev ordinal, v4 id, v5 id, v6 id)
PERIM_M = [('Cash gross (BIK cap base)', 10, 9148012, 9148012, 9148010), ('IRPP gross', 131, 9148041, 9148041, 9148131),
           ('CNPS base', 155, 9148051, 9148051, 9148155), ('TFE base', 151, 9148081, 9148081, 9148151), ('TAFP base', 141, 9148082, 9148082, 9148141),
           ('Taxable income', 191, 9148071, 9148071, 9148191), ('Non-resident base', 11, 9148074, 9148074, 9148192),
           ('Transport exemption', 31, 9148021, 9148021, 9148031), ('Family exemption', 33, 9148022, 9148022, 9148033),
           ('Retirement deduction', 181, 9148061, 9148061, 9148181)] + \
          [(lab, o, 9148031 + k, 9148031 + k, 9148000 + o) for k, (lab, o) in enumerate([('BIK housing', 41), ('BIK vehicle', 51), ('BIK food', 61), ('BIK furnishings', 71),
                                                                                         ('BIK domestic', 81), ('BIK electricity', 91), ('BIK water', 101), ('BIK telephone', 111), ('BIK gas', 121)])] + \
          [('15% function allowance', None, None, 9148024, 9148035), ('Leave ticket', None, None, 9148025, 9148036)]


def build_multi():
    wb = openpyxl.Workbook()
    S = wb.active; S.title = 'Summary'
    RCs = wb.create_sheet('Regulation Comparison'); RS = wb.create_sheet('Results'); MX = wb.create_sheet('Matrices')
    MD = wb.create_sheet('Matrix Detail'); LG = wb.create_sheet('Legal Themes'); OP = wb.create_sheet('Open points')

    # ---------------- Regulation Comparison
    title(RCs, 'Regulation by regulation — Chad: development team td_2026 × our v4 · v5 · v6',
          'Adherence = structural match with the Dev regulation, computed the same way for every version: mean of 9 checks (ID, name, rule group, taxation type, pre-condition, band accounts, rates, formulas, matrix rules). Status: Same (100%) · Different · Only theirs · Only ours.   ★ = most important to close on the call.', 'V')
    header(RCs, 4, ['#', 'Block', 'Development team regulation', 'Development team formula',
                    'v4 regulation', 'v4 formula', 'v4 status', 'v4 adherence',
                    'v5 regulation', 'v5 formula', 'v5 status', 'v5 adherence',
                    'v6 regulation', 'v6 formula', 'v6 status', 'v6 adherence',
                    'Weight (their regs)', 'Difference (v5 / v6 vs Dev)', 'Legal basis', 'Who is right per the law (v5 / v6)', 'Confidence', 'Question for the call'],
           [4, 11, 26, 40, 24, 36, 11, 10, 24, 36, 11, 10, 24, 36, 11, 10, 9, 44, 30, 14, 10, 50])
    RCs.freeze_panes = 'C5'
    for n, row in enumerate(RC, 1):
        r = 4 + n
        blk, o, vid, st, cause, adh, diff, legal, who, conf, q, star = row
        p4, p5, p6 = pair(row)
        put(RCs, r, 1, n); put(RCs, r, 2, blk, True)
        put(RCs, r, 3, dev_name(o) if o else '—', True); put(RCs, r, 4, dev_text(o) if o else '—', code=True)
        for c0, ver, pid in ((5, 'v4', p4), (9, 'v5', p5), (13, 'v6', p6)):
            put(RCs, r, c0, f"{pid} — {VBY[ver][pid]['name']}" if pid else '—', True)
            put(RCs, r, c0 + 1, gtext(ver, pid), code=True)
            if o and pid:
                sc = form_score(o, ver, pid)
                stt = 'Same' if sc >= 0.999 else 'Different'
            elif o:
                sc, stt = 0, 'Only theirs'
            elif pid:
                sc, stt = None, 'Only ours'
            else:
                sc, stt = None, '—'
            put(RCs, r, c0 + 2, stt, True, bg=STATUS_FILL.get(stt), center=True)
            put(RCs, r, c0 + 3, sc, fmt='0%', center=True)
        put(RCs, r, 17, 1 if o else 0, center=True)
        dv6 = ''
        if p6 and VBY['v6'][p6].get('law'):
            dv6 = ' · v6: Deliberate divergence (law) — ' + VBY['v6'][p6]['law']
        put(RCs, r, 18, diff + dv6); put(RCs, r, 19, legal)
        put(RCs, r, 20, who, True, bg=WHO_FILL.get(who), center=True); put(RCs, r, 21, conf, fmt='0%', center=True)
        put(RCs, r, 22, (q + ' ★') if (q and star) else q, bold=bool(q))
    rc_last = 4 + len(RC)
    used = {ver: set() for ver in ('v4', 'v5', 'v6')}
    for row in RC:
        for ver, pid in zip(('v4', 'v5', 'v6'), pair(row)):
            if pid:
                used[ver].add(pid)
    for ver in used:
        assert used[ver] == set(VBY[ver]), (ver, set(VBY[ver]) - used[ver])

    # ---------------- Results
    title(RS, 'All designs executed on the same cases', 'Dev = sim_dev.py on td.json; v4, v5, v6 = run() of each _build_vN.py. 12 scenarios + 26 extra checks (E21–E26 added with the v6 QA rounds). Differences = version − Dev. XAF. v6 is checked equal to v5 on every line except the six cases of the v6 matrix fixes (5, E21, E23–E26), which v5 also has.', 'P')
    header(RS, 4, ['Case', 'Scenario', 'Type', 'Output', 'Dev', 'v4', 'v5', 'v6', 'v4 − Dev', 'v5 − Dev', 'v6 − Dev', 'v4 status', 'v5 status', 'v6 status', 'Cause (v5 / v6 vs Dev)', 'Closer to the law'],
           [6, 30, 11, 30, 13, 13, 13, 13, 11, 11, 11, 10, 10, 10, 52, 34])
    RS.freeze_panes = 'E5'
    rr = results_multi()
    for k, (key, name, typ, lab, dv, a4, a5, a6, cause, closer) in enumerate(rr):
        r = 5 + k
        put(RS, r, 1, key, True); put(RS, r, 2, name); put(RS, r, 3, typ); put(RS, r, 4, lab)
        for c, v in ((5, dv), (6, a4), (7, a5), (8, a6)):
            put(RS, r, c, v, fmt=NUM)
        for c, col in ((9, 'F'), (10, 'G'), (11, 'H')):
            put(RS, r, c, f'={col}{r}-E{r}', fmt=NUM)
        for c, col in ((12, 'F'), (13, 'G'), (14, 'H')):
            put(RS, r, c, f'=IF(ABS({col}{r}-E{r})<1,"Same","Different")', True, center=True)
        put(RS, r, 15, cause); put(RS, r, 16, closer)
    rs_last = 4 + len(rr)
    rs_scen = 4 + sum(1 for x in rr if x[2] == 'Scenario')
    for col in 'LMN':
        RS.conditional_formatting.add(f'{col}5:{col}{rs_last}', CellIsRule(operator='equal', formula=['"Same"'], fill=PatternFill('solid', bgColor='FFC6EFCE')))
        RS.conditional_formatting.add(f'{col}5:{col}{rs_last}', CellIsRule(operator='equal', formula=['"Different"'], fill=PatternFill('solid', bgColor='FFFFC7CE')))

    # ---------------- Matrix Detail / Matrices
    codes = wtc_codes(); N = len(codes)
    title(MD, f'Matrix detail — every WTC V3.0 pay element ({N}) × each perimeter × each version', 'Both · Only theirs · Only ours · — (neither), against the Dev. A code also counts when it reaches the perimeter through an intermediate account the perimeter adds.', 'D')
    heads = ['Code', 'WTC V3.0 name']
    for lab, *_ in PERIM_M:
        heads += [f'{lab} · v4', f'{lab} · v5', f'{lab} · v6']
    header(MD, 4, heads, [9, 30] + [10] * (3 * len(PERIM_M)))
    MD.freeze_panes = 'C5'
    for k, (c, nm) in enumerate(codes):
        put(MD, 5 + k, 1, c); put(MD, 5 + k, 2, nm)
    for j, (lab, o, i4, i5, i6) in enumerate(PERIM_M):
        devcol = [bool(o) and dev_in(o, c) for c, _ in codes]
        for v, (ver, pid) in enumerate((('v4', i4), ('v5', i5), ('v6', i6))):
            col = 3 + 3 * j + v
            for k, (c, _) in enumerate(codes):
                d = devcol[k]
                ours = bool(pid) and ver_in(ver, pid, c)
                val = 'Both' if d and ours else 'Only theirs' if d else 'Only ours' if ours else '—'
                cell = MD.cell(5 + k, col, val)
                cell.font = F(8); cell.alignment = CENTER; cell.border = BOX
                if val != '—':
                    cell.fill = fill({'Both': GREEN, 'Only theirs': ORANGE, 'Only ours': BLUE}[val])
    md_last = 4 + N
    title(MX, f'Taxability matrices — code by code over all {N} WTC V3.0 pay elements, each version against the Dev',
          f'Similarity = common ÷ codes at least one design includes. Agreement = (common + neither) ÷ {N}. Live COUNTIF formulas over "Matrix Detail".', 'Q')
    header(MX, 4, ['Perimeter', 'Their reg.', 'Theirs', 'v4 includes', 'v4 common', 'v4 similarity', 'v4 agreement',
                   'v5 includes', 'v5 common', 'v5 similarity', 'v5 agreement', 'v6 includes', 'v6 common', 'v6 similarity', 'v6 agreement', 'Our regs (v4 / v5 / v6)', 'Main differences (v5 / v6)'],
           [24, 10, 9, 9, 9, 10, 10, 9, 9, 10, 10, 9, 9, 10, 10, 26, 50])
    MX.freeze_panes = 'B5'
    for j, (lab, o, i4, i5, i6) in enumerate(PERIM_M):
        r = 5 + j
        put(MX, r, 1, lab, True); put(MX, r, 2, f'9148{o:03d}' if o else '—')
        L4 = openpyxl.utils.get_column_letter(3 + 3 * j)
        rng = lambda L: f"'Matrix Detail'!{L}5:{L}{md_last}"
        put(MX, r, 3, f'=COUNTIF({rng(L4)},"Both")+COUNTIF({rng(L4)},"Only theirs")')
        for v in range(3):
            L = openpyxl.utils.get_column_letter(3 + 3 * j + v)
            c0 = 4 + 4 * v
            col = lambda c: openpyxl.utils.get_column_letter(c)
            put(MX, r, c0, f'=COUNTIF({rng(L)},"Both")+COUNTIF({rng(L)},"Only ours")')
            put(MX, r, c0 + 1, f'=COUNTIF({rng(L)},"Both")')
            put(MX, r, c0 + 2, f'=IF((C{r}+{col(c0)}{r}-{col(c0 + 1)}{r})=0,1,{col(c0 + 1)}{r}/(C{r}+{col(c0)}{r}-{col(c0 + 1)}{r}))', fmt='0.0%', center=True)
            put(MX, r, c0 + 3, f'=({col(c0 + 1)}{r}+COUNTIF({rng(L)},"—"))/{N}', fmt='0.0%', center=True)
        put(MX, r, 16, ' / '.join(str(x) if x else '—' for x in (i4, i5, i6)))
        put(MX, r, 17, MAINDIFF.get(lab, 'Dev: forfait on 58105; ours: the real benefit codes.' if lab.startswith('BIK') else 'Only in our design.'))
    mx_last = 4 + len(PERIM_M)
    pr = mx_last + 2
    put(MX, pr, 1, 'Pooled — all perimeters', True)
    put(MX, pr, 3, f'=SUM(C5:C{mx_last})', True)
    for v in range(3):
        c0 = 4 + 4 * v
        col = lambda c: openpyxl.utils.get_column_letter(c)
        put(MX, pr, c0, f'=SUM({col(c0)}5:{col(c0)}{mx_last})', True)
        put(MX, pr, c0 + 1, f'=SUM({col(c0 + 1)}5:{col(c0 + 1)}{mx_last})', True)
        put(MX, pr, c0 + 2, f'={col(c0 + 1)}{pr}/(C{pr}+{col(c0)}{pr}-{col(c0 + 1)}{pr})', True, fmt='0.0%', center=True)
        put(MX, pr, c0 + 3, f'=SUMPRODUCT({col(c0 + 3)}5:{col(c0 + 3)}{mx_last})/{len(PERIM_M)}', True, fmt='0.0%', center=True)

    # ---------------- Legal Themes
    title(LG, 'Statutory themes — who is right per the law, each version against the Dev',
          'Verdicts from LEI-VEREDITOS.md (R1, § (b)) re-read for each version. v6 has the v5 rules, so its verdict is the v5 one (formula). "No rule" / "Not law" left out of the count; "Open" = not settled.', 'K')
    header(LG, 4, ['#', 'Theme', 'Development team', 'Our v4', 'Our v5 / v6', 'Who is right — v4 vs Dev', 'Who is right — v5 vs Dev', 'Who is right — v6 vs Dev', 'Confidence', 'Legal basis', 'Note'],
           [5, 36, 26, 26, 30, 14, 14, 14, 10, 34, 20])
    LG.freeze_panes = 'C5'
    for k, (n, th, dvt, ov, who, conf, src) in enumerate(LT):
        r = 5 + k
        t4, w4 = V4_THEME[n]
        put(LG, r, 1, n); put(LG, r, 2, th, True); put(LG, r, 3, dvt); put(LG, r, 4, t4); put(LG, r, 5, ov)
        put(LG, r, 6, w4, True, bg=WHO_FILL.get(w4), center=True)
        put(LG, r, 7, who, True, bg=WHO_FILL.get(who), center=True)
        put(LG, r, 8, f'=G{r}', True, center=True)
        put(LG, r, 9, conf, fmt='0%', center=True); put(LG, r, 10, src)
        put(LG, r, 11, 'v4 verdict from LEI-VEREDITOS R1 / (b)' if w4 != who else '')
    lg_last = 4 + len(LT)
    for col in 'FGH':
        for w, c in WHO_FILL.items():
            LG.conditional_formatting.add(f'{col}5:{col}{lg_last}', CellIsRule(operator='equal', formula=[f'"{w}"'], fill=PatternFill('solid', bgColor=c)))

    # ---------------- Open points
    title(OP, 'Open points — technical decisions pending the user and sources still missing', 'v6 keeps the v5 position on every point (same rules). v4 position shown for history.', 'H')
    header(OP, 4, ['#', 'Point', 'v4 position', 'v5 / v6 position', 'Alternative and its effect', 'Source / what is missing', 'Confidence', 'Next step'], [4, 28, 30, 38, 40, 40, 10, 28])
    V4POS = ['Excess over 30% in CNPS (as the Dev)', 'Taxable (only 62867 of the 6286x series)', 'No worker category', 'Annualise ×12', '500,000 a month, no regularisation', 'x.99 limits', '—']
    for k, row in enumerate(OPEN, 1):
        r = 4 + k
        put(OP, r, 1, k); put(OP, r, 2, row[0], True); put(OP, r, 3, V4POS[k - 1]); put(OP, r, 4, row[1]); put(OP, r, 5, row[2]); put(OP, r, 6, row[3])
        put(OP, r, 7, row[4], fmt='0%', center=True); put(OP, r, 8, row[5])

    # ---------------- Summary
    for c, w in zip('ABCDEFG', (50, 15, 15, 15, 30, 15, 46)):
        S.column_dimensions[c].width = w
    S['A1'] = "Chad — our designs v4 · v5 · v6 vs the development team's design td_2026 · similarity and legal accuracy"; S['A1'].font = F(13, True)
    S['A2'] = ('v4 = ' + VERS[0][2] + f' ({len(v4.R)} regs) · v5 = ' + VERS[1][2] + f' ({len(v5.R)} regs) · v6 = ' + VERS[2][2] + f' ({len(v6.R)} regs) · Dev td_2026 ({len(DEV)} regs, td.json = CT-A-588). '
               'Every number below is a formula over the other sheets.')
    S['A2'].font = F(9); S['A2'].alignment = WRAP; S.merge_cells('A1:G1'); S.merge_cells('A2:G2'); S.row_dimensions[2].height = 30
    S['A4'] = 'SIMILARITY AND LEGAL ACCURACY BY VERSION'; S['A4'].font = F(11, True)
    for i, n in enumerate(['Measure', 'v4', 'v5', 'v6', 'Change v4→v5→v6', 'Development team', 'Basis'], 1):
        c = S.cell(5, i, n); c.font = F(10, True); c.fill = fill(GREY); c.alignment = CENTER; c.border = BOX
    RCr = "'Regulation Comparison'"
    who4, who5, who6 = (f"'Legal Themes'!{c}5:{c}{lg_last}" for c in 'FGH')
    conf = f"'Legal Themes'!I5:I{lg_last}"
    res = lambda w: f'(COUNTIF({w},"Ours")+COUNTIF({w},"Dev")+COUNTIF({w},"Both")+COUNTIF({w},"Neither"))'
    meas = [
        (f'Results — {len(v6.SCEN) + len(v6.EXTRA)} cases, {len(rr)} values', [f'=COUNTIF(Results!{c}5:{c}{rs_last},"Same")/COUNTA(Results!{c}5:{c}{rs_last})' for c in 'LMN'], '', 'Same as the Dev within 1 XAF'),
        (f'Results — the {len(v5.SCEN)} scenarios only', [f'=COUNTIF(Results!{c}5:{c}{rs_scen},"Same")/COUNTA(Results!{c}5:{c}{rs_scen})' for c in 'LMN'], '', f'{rs_scen - 4} values'),
        ('Structure — average adherence per regulation', [f'=SUMPRODUCT({RCr}!{c}5:{c}{rc_last},{RCr}!Q5:Q{rc_last})/SUM({RCr}!Q5:Q{rc_last})' for c in 'HLP'], '', f'Their {len(DEV)} regulations, 9 structural checks each (Only theirs = 0)'),
        ('Matrices — only codes at least one design includes', [f'=Matrices!{c}{pr}' for c in 'FJN'], '', 'Pooled over all perimeters'),
        ('OVERALL SIMILARITY — mean of results, structure and matrices', ['=AVERAGE(B6,B8,B9)', '=AVERAGE(C6,C8,C9)', '=AVERAGE(D6,D8,D9)'], '', ''),
        ('Themes where our position matches our reading of the law',
         [f'=(COUNTIF({w},"Ours")+COUNTIF({w},"Both"))/{res(w)}' for w in (who4, who5, who6)], f'=(COUNTIF({who5},"Dev")+COUNTIF({who5},"Both"))/{res(who5)}', 'Count of themes; our reading of the law, not a ruling, and not the accuracy of the design (matrix defects are not themes — see the defects row)'),
        ('Legal match weighted by confidence (headline)',
         [f'=(SUMIFS({conf},{w},"Ours")+SUMIFS({conf},{w},"Both"))/{res(w)}' for w in (who4, who5, who6)], f'=(SUMIFS({conf},{who5},"Dev")+SUMIFS({conf},{who5},"Both"))/{res(who5)}', 'Each verdict weighted by its confidence (60–100%)'),
        ('Themes resolved by the law (count)', [f'={res(w)}' for w in (who4, who5, who6)], '', 'Of 40 themes'),
        ('Right per the law (count)', [f'=COUNTIF({w},"Ours")+COUNTIF({w},"Both")' for w in (who4, who5, who6)], f'=COUNTIF({who5},"Dev")+COUNTIF({who5},"Both")', 'Dev counted against v5 / v6'),
    ]
    for k, (lab, fs, devf, basis) in enumerate(meas):
        r = 6 + k
        bg = BLUE if lab.startswith(('OVERALL', 'Legal match weighted')) else None
        put(S, r, 1, lab, True, bg=bg)
        cnt = lab.endswith('(count)')
        for c, fml in zip((2, 3, 4), fs):
            cell = put(S, r, c, fml, True, fmt='0' if cnt else '0%', bg=bg, center=True)
            if bg:
                cell.font = F(11, True)
        if cnt:
            put(S, r, 5, f'=TEXT(B{r},"0")&" → "&TEXT(C{r},"0")&" → "&TEXT(D{r},"0")', center=True)
        else:
            put(S, r, 5, f'=TEXT(B{r},"0%")&" → "&TEXT(C{r},"0%")&" → "&TEXT(D{r},"0%")', center=True)
        put(S, r, 6, devf, True, fmt='0' if cnt else '0%', center=True) if devf else put(S, r, 6, '')
        put(S, r, 7, basis)
    rlast = 6 + len(meas)
    put(S, rlast, 1, 'Change v4→v5→v6 (overall similarity · legal accuracy)', True, bg=BLUE)
    put(S, rlast, 5, '="Similarity "&TEXT(B10,"0%")&" → "&TEXT(C10,"0%")&" → "&TEXT(D10,"0%")&" · Legal (weighted) "&TEXT(B12,"0%")&" → "&TEXT(C12,"0%")&" → "&TEXT(D12,"0%")', True, bg=BLUE)
    S.merge_cells(start_row=rlast, start_column=5, end_row=rlast, end_column=7)
    q = f'{RCr}!V5:V{rc_last}'
    put(S, rlast + 2, 1, 'Questions for the call (rows / ★)', True); put(S, rlast + 2, 2, f'=COUNTIF({q},"?*")', center=True); put(S, rlast + 2, 3, f'=COUNTIF({q},"*★*")', center=True)
    lst = '{' + ','.join(f'"{k}"' for k in sorted(v6.V1_CASES)) + '}'
    put(S, rlast + 3, 1, f'v6 = v5 on every Results line except the cases of the v6 matrix fixes ({", ".join(sorted(v6.V1_CASES))})', True)
    put(S, rlast + 3, 2, f'=IF(SUMPRODUCT(ISNA(MATCH(Results!A5:A{rs_last},{lst},0))*ABS(Results!G5:G{rs_last}-Results!H5:H{rs_last}))<0.01,"Yes","No")', True, center=True)
    put(S, rlast + 3, 3, f'=SUMPRODUCT(ISNUMBER(MATCH(Results!A5:A{rs_last},{lst},0))*(ABS(Results!G5:G{rs_last}-Results!H5:H{rs_last})>=0.5))', center=True); put(S, rlast + 3, 4, 'lines that differ in those cases')
    put(S, rlast + 4, 1, 'Defects found by QA after the score (matrix coverage)', True, bg=YELLOW)
    put(S, rlast + 4, 2, 7, True, center=True, bg=YELLOW); put(S, rlast + 4, 3, 7, True, center=True, bg=YELLOW); put(S, rlast + 4, 4, 0, True, center=True, bg=YELLOW)
    put(S, rlast + 4, 5, 'v4 and v5 (same matrices): car fuel arrears 65521–65523 · benefits plans 6267x/6268x series · CNPS gratuity series 6291x–6293x, 62909 · medical insurance 6261x · social allowance 62651–62653 · cash-in-lieu 6561x/6566x out of TF/TA · severance 6218x vs 629xx in TF/TA. v6: all fixed (rounds 2–3), pending the QA round 3 — the legal match above does not count these', bg=YELLOW)
    S.merge_cells(start_row=rlast + 4, start_column=5, end_row=rlast + 4, end_column=7); S.row_dimensions[rlast + 4].height = 54
    S.cell(rlast + 6, 1, 'Reading: v4 → v5 moved the rules to the law at the cost of more differences in pay with the Dev; v5 → v6 changed the form (structure close to the Dev) and, after QA, fixed seven matrix-coverage defects that v4 and v5 share. The legal measures are our reading of the law weighted by confidence, not a ruling.').font = F(9, True)
    S.cell(rlast + 6, 1).alignment = WRAP; S.merge_cells(start_row=rlast + 6, start_column=1, end_row=rlast + 6, end_column=7); S.row_dimensions[rlast + 6].height = 40

    for ws in wb.worksheets:
        ws.page_setup.orientation = 'landscape'
    wb.save(OUT_MULTI)
    return dict(rows=len(RC), results=len(rr), codes=N, perimeters=len(PERIM_M), themes=len(LT), out=os.path.basename(OUT_MULTI))



if __name__ == '__main__':
    if '--v5-only' in sys.argv:
        print(build())          # regenerates TD_Design_Comparison_v5_vs_Dev.xlsx (not run by default: that file is kept as delivered)
    else:
        print(build_multi())
