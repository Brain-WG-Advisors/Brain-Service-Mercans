# -*- coding: utf-8 -*-
"""Colombia design v2.0 - generator and executable validation (model: Chad design v6).

v2.0 = the rules of design v1.2 (final/design/CO_Regulation_Design_v1_2.md), updated to the round-6 finals of 2 November 2026
(CCG v1.7, WTC v1.9, DD v1.6, SIR v1.4), written as regulations in the development team's schema (td.json of Chad: ordinal,
taxGroup, taxRuleGroup, taxationType, assertion, bands with formula and debit/credit accounts, taxabilityRules per wage
type) and executed by co_engine.py. The only Dev regulation that exists for Colombia (draft "CO Draft Regulations", row
9170132 "CO Income Tax Flat", flat, income_tax, simple_tax_post_formula, ordinal 132) fixes the ID / ordinal convention
(ID = 9170000 + ordinal) and the income-tax rule group (no retro_).

Checks (VALIDATION-run.txt, SWEEP-run.txt):
 a) order: every account read by a regulation is an input / flag / constant or is posted by a lower ordinal;
 b) scenarios: every case of the independent calculation (oracle/cases*.json, oracle_v2.py; the annual UVT caps tracked
    year-to-date as in revisao/rodada5/scripts/oracle_r5_ytd.py) = engine, value by value, no tolerance; each difference
    is listed with its cause;
 c) sweep: each of the 405 WTC v1.9 rows, alone on top of a base salary, through the engine; inclusion in each base vs the
    WTC flag (columns N-X);
 d) the same engine on a v1.2-faithful variant (v1.2 IDs / ordinals and formulas) reproduces the independent calculation
    on the monthly cases and shows the v1.2 defects.
Run: python -I _build_v2.py
"""
import os, sys, json, re, csv, copy, importlib.util, collections
from decimal import Decimal as Dc
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import co_engine as E
sys.stdout.reconfigure(encoding='utf-8')
VAL = os.path.join(os.path.dirname(HERE), '2026-10-29-validacao-research')
WTC = os.path.join(VAL, 'final', 'CO-WTC-001-v1.9.xlsx')
ORA = os.path.join(VAL, 'oracle')
OUT = os.path.join(HERE, 'co-design-blueprint-v2')
os.makedirs(OUT, exist_ok=True)
D = E.D
DL = 'Deliberate divergence (law)'

# ================================================================== constants (52xxx), each with effective date and source
CONST = {
 '52501': ('1750905', 'SMMLV 2026', 'Decree 1469 of 29 Dec 2025 art. 1 (provisional suspension revoked by the Consejo de Estado, Section Two, order of 9 July 2026; Decree 0159 of 2026 left without effect by ordinal 3 of the same order)'),
 '52502': ('52374', 'UVT 2026', 'Resolution DIAN 000238 of 15 Dec 2025 art. 1'),
 '52503': ('249095', 'Transport allowance 2026', 'Decree 1470 of 2025 art. 1; Law 15 of 1959 art. 2'),
 '52504': ([('2025-07-15', '220'), ('2026-07-15', '210')], 'Monthly hours divisor (by the date worked)', 'Law 2101 of 2021 art. 3; Labour Code art. 161 (Law 2466 of 2025 art. 11)'),
 '52505': ([('2025-07-01', '0.80'), ('2026-07-01', '0.90'), ('2027-07-01', '1.00')], 'Rest-day / holiday surcharge (by the date worked)', 'Labour Code art. 179 transitional paragraph (Law 2466 of 2025 art. 14)'),
 '52542': ('18', 'Maternity leave, weeks', 'Labour Code art. 236 num. 1 (Law 2114 of 2021)'),
}
CONSTS = {k: (v[0] if not isinstance(v[0], list) else v[0]) for k, v in CONST.items()}

# ================================================================== WTC v1.9 perimeters
import openpyxl
ws = openpyxl.load_workbook(WTC, read_only=True)['Wage Type Catalogue']
WROWS = []
COLS = 'NOPQRSTUVWX'
for i, r in enumerate(ws.iter_rows(min_row=1, values_only=True), start=1):
    if i > 1 and r[1]:
        f = {c: ('' if r[13 + COLS.index(c)] is None else str(r[13 + COLS.index(c)]).strip()) for c in COLS}
        WROWS.append(dict(row=i, key=f'R{i}', name=str(r[1]), cat=str(r[4]), V=f['V'], **{c: f[c] for c in COLS if c != 'V'}))
PER = 'NOPQRSTUWX'
ACTIVE = [w for w in WROWS if not all(w[c] == 'NA' for c in PER)]
BYKEY = {w['key']: w for w in WROWS}
assert len(WROWS) == 405 and len(ACTIVE) == 298, (len(WROWS), len(ACTIVE))
PACTED = 'Non-Salary - pacted'

# routing (design Part 4, by law): rows withheld by their own regulation, not by the monthly Procedure 1 read
PRIMA = ['R320']                          # Decree 1625 of 2016 art. 1.2.4.1.3, Procedure 1: the statutory service bonus has its own table read
INDEMN = ['R339', 'R340', 'R343', 'R344']  # Tax Code art. 401-3; Decree 1625 art. 1.2.4.1.13 (R340: Labour Code art. 65)
BONUS = ['R345']                          # Decree 1625 art. 1.2.4.1.8: retirement bonus


def matrix(col, overrides=None, only=None):
    """taxabilityRules from a WTC column: Yes -> true; No / Yes/No -> false (Yes/No: pacted rows reach the IBC through the
    Law 1393 excess; the other Yes/No rows need a wage-type split at configuration); NA -> not listed."""
    out = []
    for w in ACTIVE:
        if only is not None and w['key'] not in only: continue
        v = w[col] if col else 'Yes'
        if v == 'NA': continue
        t = (v == 'Yes')
        if overrides and w['key'] in overrides: t = overrides[w['key']]
        out.append({'account': w['key'], 'pattern': None, 'isTaxable': t})
    return out


def acc(*names):
    return [{'account': n, 'pattern': None, 'isTaxable': True} for n in names]


TABLE = ('IF(LTE({b};95);0;IF(LTE({b};150);MULTIPLY(SUBTRACT({b};95);0.19);IF(LTE({b};360);ADD(MULTIPLY(SUBTRACT({b};150);0.28);10);'
         'IF(LTE({b};640);ADD(MULTIPLY(SUBTRACT({b};360);0.33);69);IF(LTE({b};945);ADD(MULTIPLY(SUBTRACT({b};640);0.35);162);'
         'IF(LTE({b};2300);ADD(MULTIPLY(SUBTRACT({b};945);0.37);268);ADD(MULTIPLY(SUBTRACT({b};2300);0.39);770)))))))')
def table(b):
    return TABLE.format(b=b)


UP100 = 'MULTIPLY(CEILING(DIVIDE($band_amount_raw;100);1);100)'
RESIDENT = 'EQUALS($64552;1)'
P1 = 'AND(EQUALS($64552;1);EQUALS($58206;1))'
P2 = 'AND(EQUALS($64552;1);EQUALS($58206;2))'
NOT51 = 'GREATER($58216;1)'
PENSION_GATE = 'AND(AND(GREATER($58209;1);GREATER($58211;1));GREATER($58216;1))'
CLASSROOM = 'EQUALS($58208;1)'
DAYF = 'DIVIDE($58295;30)'

# ================================================================== regulations
REGS = []


def reg(o, name, group, trg, ttype, bands, rules=None, assertion='', law='', note='', v12=None, div=''):
    REGS.append(dict(regulationId=str(9170000 + o), systemTaxYearIds=['co_2026'], country='co', name=name, status='active', ordinal=o, currency='COP',
                     taxGroup=group, taxRuleGroup=trg, taxationType=ttype, assertion=assertion,
                     bands=bands, taxabilityRules=rules or [], law=law, note=note, v12=v12, divergence=div))


def band(debit, formula=None, rate=None, rate_acc=None, unit=None, assertion=None):
    return dict(incomeFrom=None, incomeTo=None, employeeRate=rate, employerRate=None, floorAmount=None, ceilingAmount=None,
                creditAmount=None, formula=formula, assertion=assertion, unitAccount=unit, employeeRateAccount=rate_acc,
                employerRateAccount=None, floorAccount=None, ceilingAccount=None, debitAccount=debit, creditAccount='99999')


SS, IT = 'social_security', 'income_tax'
RS, RSF, SF, S = 'retro_simple_tax', 'retro_simple_tax_post_formula', 'simple_tax_post_formula', 'simple_tax'

# ---------------- earnings and payments (posted to WTC rows, before every base) ----------------
reg(9, 'CO All-inclusive Salary for the Period', SS, RSF, 'formula', [band('R303', f'MULTIPLY($64992;{DAYF})')],
    assertion='LESS($58201;2)', law='Labour Code art. 132; 30-day month (art. 134)', v12=('9170010', 10))
reg(10, 'CO Basic Salary for the Period', SS, RSF, 'formula', [band('R302', f'MULTIPLY($64992;{DAYF})')],
    assertion='AND(GREATER($58201;1);LESS($58208;1))', law='30-day month (Labour Code art. 134; CCG Mod. 4.3)', v12=('9170010', 10))
reg(11, 'CO Apprentice Maintenance Support', SS, RSF, 'formula', [band('R338', f'MULTIPLY(MULTIPLY($52501;IF(LESS($58208;2);0.75;1));{DAYF})')],
    assertion='GREATER($58208;0)', law='Labour Code art. 81 (Law 2466 of 2025 art. 21)', v12=('9170096', 96))
OT = [('H308', 'R308', '0.35', 'Labour Code art. 168 num. 1'), ('H306', 'R306', '1.25', 'art. 168 num. 2'), ('H307', 'R307', '1.75', 'art. 168 num. 3'),
      ('H309', 'R309', 'ADD(1;$52505)', 'art. 179'), ('H312', 'R312', 'ADD(1.35;$52505)', 'arts. 168, 179'),
      ('H310', 'R310', 'ADD(1.25;$52505)', 'arts. 168, 179'), ('H311', 'R311', 'ADD(1.75;$52505)', 'arts. 168, 179')]
reg(12, 'CO Overtime and Premium Hours', SS, RSF, 'formula',
    [band(r, f'MULTIPLY(MULTIPLY($hours;DIVIDE($64992;$52504));{f})', unit=u) for u, r, f, _ in OT],
    law='Labour Code arts. 168, 179; hours divisor Law 2101 of 2021 art. 3 (by the date worked)', v12=('9170012', 12))
reg(13, 'CO Transport Allowance', SS, RSF, 'formula',
    [band('R304', f'IF(LTE($64992;MULTIPLY($52501;2));MULTIPLY($52503;{DAYF});0)')],
    assertion=f'AND(GREATER($58201;1);NOT({CLASSROOM}))', law='Decree 1258 of 1959 art. 5; Law 15 of 1959 art. 2; Decree 1470 of 2025', v12=('9170013', 13))
reg(14, 'CO Vacation Base', SS, RSF, 'flat', [band('58175', rate=100)], matrix('X'),
    law='Labour Code art. 192 num. 1 (WTC column X)', v12=('9170085', 85))
reg(15, 'CO Vacation Daily Value', SS, RSF, 'formula', [band('58178', 'ROUND(DIVIDE($58175;30))')], assertion='GREATER($58175;0)', v12=('9170085', 85))
reg(16, 'CO Vacation Taken', SS, RSF, 'formula', [band('R323', 'ROUND(MULTIPLY(DIVIDE($58175;30);$58292))')],
    assertion='AND(GREATER($58175;0);GREATER($58292;0))', law='Labour Code arts. 186, 192', v12=('9170085', 85))
reg(17, 'CO Vacation Compensated in Cash', SS, RSF, 'formula', [band('R324', 'ROUND(MULTIPLY(DIVIDE($58175;30);$58293))')],
    assertion='AND(AND(GREATER($58175;0);GREATER($58293;0));LTE($58293;7.5))', law='Labour Code art. 189 num. 1 (at most half of the 15 days)', v12=('9170085', 85))
reg(18, 'CO Vacation Compensation Above Half (block flag)', SS, RSF, 'formula', [band('58217', 'IF(GREATER($58293;7.5);1;2)')],
    law='Labour Code art. 189 num. 1', note='1 = request above half the entitlement: blocked, no payment (17 does not run)', v12=('9170085', 85))
reg(19, 'CO Vacation Paid on Termination', SS, RSF, 'formula', [band('R156', 'ROUND(DIVIDE(MULTIPLY($58175;$58294);720))')],
    assertion='AND(GREATER($58175;0);GREATER($58294;0))', law='Labour Code art. 189 num. 2 (proportional, days / 720)', v12=('9170086', 86))
reg(20, 'CO Statutory-Benefit Base', SS, RSF, 'flat', [band('58171', rate=100)], matrix('W'),
    law='Labour Code art. 253; transport allowance in the base (Law 1 of 1963 art. 7) through WTC row R304 (column W = Yes)', v12=('9170081', 81),
    note='v2: the transport allowance enters only through its WTC row (W = Yes); v1.2 added 52503 again by formula')
reg(21, 'CO Service Bonus', SS, RSF, 'flat', [band('R320', 'ROUND(DIVIDE(MULTIPLY($band_amount_raw;$58297);360))', rate=100)], acc('58171'),
    assertion='GREATER($58297;0)', law='Labour Code art. 306', v12=('9170082', 82))
reg(22, 'CO Severance Savings', SS, RSF, 'flat', [band('R321', 'ROUND(DIVIDE(MULTIPLY($band_amount_raw;$58298);360))', rate=100)], acc('58171'),
    assertion='GREATER($58298;0)', law='Labour Code art. 249; Law 50 of 1990 art. 99', v12=('9170083', 83))
reg(23, 'CO Interest on Severance Savings', SS, RSF, 'flat',
    [band('R322', 'ROUND(DIVIDE(MULTIPLY(MULTIPLY(DIVIDE(MULTIPLY($band_amount_raw;$58298);360);$58298);0.12);360))', rate=100)], acc('58171'),
    assertion='GREATER($58298;0)', law='Law 50 of 1990 art. 99 num. 2; Law 52 of 1975 art. 1', v12=('9170084', 84))
DAILY, FLOORD = 'DIVIDE($64992;30)', 'DIVIDE($52501;30)'
SEG12 = f'MULTIPLY(MAX(MULTIPLY({DAILY};DIVIDE(2;3));{FLOORD});MIN($58290;2))'
SEG390 = f'MULTIPLY(MAX(MULTIPLY({DAILY};DIVIDE(2;3));{FLOORD});MAX(SUBTRACT(MIN($58290;90);2);0))'
SEG91 = f'MULTIPLY(MAX(MULTIPLY({DAILY};0.5);{FLOORD});MAX(SUBTRACT(MIN($58290;180);90);0))'
C543 = 'Constitutional Court C-543 of 2007 (resolutive part: the art. 227 benefit "no podrá ser inferior al salario mínimo legal vigente"), applied per day to every segment'
reg(24, 'CO Illness Benefit Days 1-2 (employer)', SS, RSF, 'formula', [band('R326', f'ROUND({SEG12})')], assertion='GREATER($58290;0)',
    law='Labour Code art. 227 (two thirds); Decree 780 of 2016 art. 3.2.1.10 par. 1; ' + C543, v12=('9170093', 93))
reg(25, 'CO Illness Benefit Days 3-90 (health insurer)', SS, RSF, 'formula', [band('R327', f'ROUND({SEG390})')], assertion='GREATER($58290;2)',
    law='Labour Code art. 227; ' + C543, v12=('9170093', 93))
reg(26, 'CO Illness Benefit Days 91-180 (health insurer)', SS, RSF, 'formula', [band('R327', f'ROUND({SEG91})')], assertion='GREATER($58290;90)',
    law='Labour Code art. 227 (one half from day 91); ' + C543, v12=('9170093', 93),
    note='v2: the minimum-wage floor binds here for salaries below 2 SMMLV (half the daily salary < SMMLV / 30)')
reg(27, 'CO Illness Benefit Total', SS, RSF, 'formula', [band('58196', f'ROUND(ADD(ADD({SEG12};{SEG390});{SEG91}))')], assertion='GREATER($58290;0)', v12=('9170093', 93))
reg(28, 'CO Contribution Base of the Illness Days', SS, RSF, 'formula',
    [band('58195', f'ROUND(MAX(ADD(ADD({SEG12};{SEG390});{SEG91});MULTIPLY($52501;DIVIDE($58290;30))))')], assertion='GREATER($58290;0)',
    law='Decree 780 of 2016 art. 3.2.1.10 (IBC = benefit value, never below the minimum wage)', v12=('9170093', 93))
reg(29, 'CO Maternity Leave Pay', SS, RSF, 'formula', [band('R330', f'ROUND(MULTIPLY({DAILY};MULTIPLY($52542;7)))')], assertion='EQUALS($58291;1)',
    law='Labour Code art. 236 num. 1 (18 weeks, Law 2114 of 2021)', v12=('9170094', 94))
reg(30, 'CO Contribution Base of the Maternity Leave', SS, RSF, 'formula',
    [band('58194', f'ROUND(MAX(MULTIPLY({DAILY};MULTIPLY($52542;7));MULTIPLY({FLOORD};MULTIPLY($52542;7))))')], assertion='EQUALS($58291;1)', v12=('9170094', 94))
GE10 = 'GTE($64992;MULTIPLY($52501;10))'
reg(31, 'CO Art. 64 Indemnity Days', SS, RSF, 'formula',
    [band('58189', f'IF(LTE($58288;360);IF({GE10};20;30);ADD(IF({GE10};20;30);DIVIDE(MULTIPLY(IF({GE10};15;20);SUBTRACT($58288;360));360)))')],
    assertion='AND(EQUALS($58299;1);EQUALS($58220;1))', law='Labour Code art. 64 (Law 789 of 2002 art. 28): fraction prorated', v12=('9170091', 91))
reg(32, 'CO Art. 64 Indemnity', SS, RSF, 'formula', [band('R339', f'ROUND(MULTIPLY({DAILY};$58189))')],
    assertion='AND(EQUALS($58299;1);EQUALS($58220;1))', law='Labour Code art. 64; base = art. 127 salary (SL1659-2025)', v12=('9170091', 91))

# ---------------- bases ----------------
reg(39, 'CO Severance Savings Paid on Termination', SS, RSF, 'formula', [band('58100', 'ADD($R321;$R322)')], assertion='EQUALS($58299;1)',
    law='Labour Code art. 249; Law 50 of 1990 art. 99 num. 3 (deposited to the fund by 14 February; paid to the employee only on termination)', v12=('9170015', 15))
reg(40, 'CO Gross Earnings', SS, RS, 'flat', [band('58100', rate=100)], matrix(None, {'R321': False, 'R322': False}),
    law='every earning row of the WTC (total devengado); deduction rows carry negative amounts (S18); severance savings and interest deposited to the fund are not paid (9170039 adds them on termination)', v12=('9170015', 15))
reg(41, 'CO Salary Payments of the Month', SS, RS, 'flat', [band('58101', rate=100)],
    [{'account': w['key'], 'pattern': None, 'isTaxable': w['V'] == 'Salary'} for w in ACTIVE],
    law='Labour Code art. 127 (WTC column V = Salary)', v12=('9170016', 16))
reg(42, 'CO Pacted Non-Salary Payments', SS, RS, 'flat', [band('58102', rate=100)],
    [{'account': w['key'], 'pattern': None, 'isTaxable': w['V'] == PACTED} for w in ACTIVE],
    law='Labour Code art. 128 (written pact); Law 1393 of 2010 art. 30', v12=('9170017', 17))
reg(43, 'CO Total Remuneration (Law 1393 test)', SS, RSF, 'formula', [band('58103', 'ADD($58101;$58102)')], v12=('9170018', 18))
reg(44, 'CO Law 1393 Excess', SS, RSF, 'formula', [band('58104', 'MAX(SUBTRACT($58102;MULTIPLY(0.40;$58103));0)')],
    law='Law 1393 of 2010 art. 30; CE SU exp. 25185 of 2021 rule 3', v12=('9170019', 19))
LO, HI = f'MULTIPLY($52501;{DAYF})', f'MULTIPLY(MULTIPLY($52501;25);{DAYF})'
FAC = 'IF(LESS($58201;2);0.70;1)'
def ibc(): return f'CEILING(MIN(MAX(ADD(MULTIPLY($band_amount_raw;{FAC});$58104);{LO});{HI});1)'
IBCLAW = 'Law 100 of 1993 arts. 18, 204 (floor 1 / ceiling 25 SMMLV prorated); all-inclusive 70% (art. 18; Labour Code art. 132); Decree 780 art. 3.2.1.5 num. 1 (up to the peso)'
reg(45, 'CO Contribution Base (IBC) - Health', SS, RSF, 'flat', [band('58106', ibc(), rate=100)], matrix('Q'), law=IBCLAW, v12=('9170021', 21))
reg(46, 'CO IBC in Minimum Wages', SS, RSF, 'formula', [band('58107', f'DIVIDE($58106;{LO})')], v12=('9170022', 22))
reg(47, 'CO Payroll-Levy Base', SS, RSF, 'flat', [band('58108', f'MULTIPLY($band_amount_raw;{FAC})', rate=100)], matrix('T'),
    law='Law 21 of 1982 art. 17 (no floor, no ceiling, no Law 1393 excess); Labour Code art. 132 num. 3 (70%)', v12=('9170023', 23))
reg(48, 'CO Art. 114-1 Exoneration Test', SS, RSF, 'formula',
    [band('58215', 'IF(AND(AND(LESS($58203;2);LESS($58101;MULTIPLY($52501;10)));LESS($58106;MULTIPLY($52501;10)));1;2)')],
    law='Tax Code art. 114-1; DIAN Conceptos 8380 of 2024, 7196 of 2025; AT2 v30 field 76', v12=('9170025', 25))
reg(49, 'CO IBC - Pension', SS, RSF, 'flat', [band('58112', ibc(), rate=100)], matrix('U'), law=IBCLAW, v12=('9170026', 26))
reg(50, 'CO IBC - Solidarity Fund', SS, RSF, 'flat', [band('58113', ibc(), rate=100)], matrix('R'), law=IBCLAW, v12=('9170027', 27))
reg(51, 'CO IBC - Occupational Risk', SS, RSF, 'flat', [band('58114', ibc(), rate=100)], matrix('S'),
    law=IBCLAW + '; no occupational risk on vacation, incapacity and leave days (Decree 1072 of 2015 art. 2.2.4.2.1.6)', v12=('9170028', 28))
Q = 'IF(LTE($58295;7);1;IF(LTE($58295;14);2;IF(LTE($58295;21);3;4)))'
reg(52, 'CO Contributor Type 51 Bases', SS, RSF, 'formula', [band('58197', f'MULTIPLY($52501;DIVIDE({Q};4))'), band('58198', '$52501')], assertion='EQUALS($58216;1)',
    law='PILA Technical Annex 2 v30, contributor type 51 (weekly quarters of the minimum wage)', v12=('9170097', 97))
M = '$58107'
FSPSUB = (f'ADD(0.5;IF(AND(GTE({M};16);LTE({M};17));0.2;IF(AND(GREATER({M};17);LTE({M};18));0.4;IF(AND(GREATER({M};18);LTE({M};19));0.6;'
          f'IF(AND(GREATER({M};19);LTE({M};20));0.8;IF(GREATER({M};20);1;0))))))')
reg(53, 'CO Solidarity Fund Subsistence Rate', SS, RSF, 'formula', [band('52515', FSPSUB)], assertion=f'GTE({M};4)',
    law='Law 100 of 1993 arts. 20 and 27 (Law 797 of 2003 arts. 7 and 8)', v12=('9170034', 34))
reg(54, 'CO Employer Pension Rate', SS, RSF, 'formula', [band('52516', 'IF(EQUALS($58212;1);22;12)')],
    law='Law 100 of 1993 art. 20; Decree-Law 2090 of 2003 (+10 points, high risk)', v12=('9170032', 32))
reg(55, 'CO Occupational-Risk Rate', SS, RSF, 'formula',
    [band('52519', 'IF(EQUALS($58204;1);0.522;IF(EQUALS($58204;2);1.044;IF(EQUALS($58204;3);2.436;IF(EQUALS($58204;4);4.35;6.96))))')],
    law='Decree 1772 of 1994 art. 13; Decree 1072 of 2015 art. 2.2.4.3.5 (class initial rate; insurer rate per work centre overrides, RESEARCH_GAPS R5)', v12=('9170043', 43))
# ---------------- contributions: one regulation per fund, employee band (employeeRate) and employer band (employerRate), as the
# development team codes them (td.json "TD CNPS Contribution EE and ER"). Rounding: the contribution of each contributor and fund
# is rounded once, up to the next COP 100 (Decree 780 of 2016 art. 3.2.1.5 num. 2, Decree 1990 of 2016 art. 1: "El valor de los
# aportes liquidados por cada cotizante ... deberá aproximarse al múltiplo de 100 superior más cercano"; AT2 v30 field 47 =
# IBC x total rate, with the rounding rule). Employee share = the statutory rate rounded to the peso (Law 100 arts. 20, 204: 4%);
# employer share = rounded fund total - employee share, written from the base (no read of the sibling band). Where the employee
# pays the whole fund (exonerated health, solidarity fund) the employee band carries the rounding.
R780 = 'Decree 780 of 2016 art. 3.2.1.5 num. 2 (Decree 1990 of 2016 art. 1): the contribution of each contributor and fund up to the next COP 100; PILA AT2 v30 field 47 (IBC x total rate)'


def ER_REST(ee):
    return f'SUBTRACT(MULTIPLY(CEILING(DIVIDE(ADD($band_amount_raw;${ee}_raw);100);1);100);${ee})'


def ebandr(debit, formula, rate=None, rate_acc=None, assertion=None):
    b = band(debit, formula, assertion=assertion); b['employerRate'] = rate; b['employerRateAccount'] = rate_acc
    return b


reg(56, 'CO Health Contribution (EE and ER)', SS, RSF, 'flat',
    [band('58121', f'IF(GREATER($58215;1);ROUND($band_amount_raw);{UP100})', rate=4),
     ebandr('58141', 'SUBTRACT(MULTIPLY(CEILING(DIVIDE(MULTIPLY($58106;0.125);100);1);100);ROUND(MULTIPLY($58106;0.04)))', rate=8.5, assertion='GREATER($58215;1)')], acc('58106'), assertion=NOT51,
    law='Law 100 art. 204 (4% + 8.5%); Tax Code art. 114-1 (employer share exonerated); ' + R780, v12=('9170031', 31))
reg(57, 'CO Pension Contribution (EE and ER)', SS, RSF, 'flat',
    [band('58122', 'ROUND($band_amount_raw)', rate=4),
     ebandr('58142', 'SUBTRACT(MULTIPLY(CEILING(DIVIDE(MULTIPLY($58112;DIVIDE(ADD(4;$52516);100));100);1);100);ROUND(MULTIPLY($58112;0.04)))', rate_acc='52516')], acc('58112'), assertion=PENSION_GATE,
    law='Law 100 art. 20 (4% + 12%; +10 high risk, Decree-Law 2090 of 2003); ' + R780, v12=('9170032', 32))
reg(58, 'CO Solidarity Fund - Solidarity (EE)', SS, RSF, 'flat', [band('58123', UP100, rate=0.5)], acc('58113'), assertion=f'AND({PENSION_GATE};GTE({M};4))', law='Law 100 art. 27; ' + R780, v12=('9170033', 33))
reg(59, 'CO Solidarity Fund - Subsistence (EE)', SS, RSF, 'flat', [band('58124', UP100, rate_acc='52515')], acc('58113'), assertion=f'AND({PENSION_GATE};GTE({M};4))', law='Law 100 art. 27; ' + R780, v12=('9170034', 34))
reg(60, 'CO Occupational Risk (ER)', SS, RSF, 'flat', [ebandr('58143', UP100, rate_acc='52519')], acc('58114'), assertion=NOT51, law='Decree 1772 of 1994 art. 13; ' + R780, v12=('9170043', 43))
reg(61, 'CO Family Compensation Fund (ER) 4%', SS, RSF, 'flat', [ebandr('58144', UP100, rate=4)], acc('58108'), assertion=NOT51, law='Law 21 of 1982 arts. 12, 17 (never exonerated); ' + R780, v12=('9170044', 44))
reg(62, 'CO SENA (ER) 2%', SS, RSF, 'flat', [ebandr('58145', UP100, rate=2)], acc('58108'), assertion=f'AND(GREATER($58215;1);{NOT51})', law='Law 21 of 1982 art. 12; Tax Code art. 114-1; ' + R780, v12=('9170045', 45))
reg(63, 'CO ICBF (ER) 3%', SS, RSF, 'flat', [ebandr('58146', UP100, rate=3)], acc('58108'), assertion=f'AND(GREATER($58215;1);{NOT51})', law='Law 89 of 1988 art. 1; Tax Code art. 114-1; ' + R780, v12=('9170046', 46))
reg(64, 'CO Contributor Type 51 Pension (EE and ER)', SS, RSF, 'flat',
    [band('58127', 'ROUND($band_amount_raw)', rate=4), ebandr('58137', 'SUBTRACT(ROUND(MULTIPLY($58197;0.16));ROUND(MULTIPLY($58197;0.04)))', rate=12)], acc('58197'),
    assertion='EQUALS($58216;1)', law='PILA AT2 v30 contributor type 51 (amounts to the peso, as the annex examples; field 47 = IBC x 16%, rounded once)', v12=('9170097', 97))
reg(65, 'CO Contributor Type 51 Occupational Risk (ER)', SS, RSF, 'flat', [ebandr('58138', 'ROUND($band_amount_raw)', rate_acc='52519')], acc('58198'), assertion='EQUALS($58216;1)',
    law='PILA AT2 v30 type 51: occupational risk always on 1 SMMLV', v12=('9170097', 97))
reg(66, 'CO Contributor Type 51 Family Compensation Fund (ER)', SS, RSF, 'flat', [ebandr('58139', 'ROUND($band_amount_raw)', rate=4)], acc('58197'), assertion='EQUALS($58216;1)', v12=('9170097', 97))
reg(67, 'CO Total Employee Contributions', SS, RSF, 'formula', [band('58129', 'ADD(ADD(ADD($58121;$58122);ADD($58123;$58124));$58127)')], v12=('9170039', 39))
reg(68, 'CO Total Employer Contributions and Levies', SS, RSF, 'formula',
    [band('58149', 'ADD(ADD(ADD(ADD($58141;$58142);ADD($58143;$58144));ADD($58145;$58146));ADD(ADD($58137;$58138);$58139))')], v12=('9170049', 49))
# ---------------- withholding (income_tax: no retro_, Decree 1625 of 2016 art. 1.2.4.1.3) ----------------
NOWH = {k: False for k in PRIMA + INDEMN + BONUS}
reg(72, 'CO Taxable Labour Payments (monthly read)', IT, S, 'flat', [band('58150', rate=100)], matrix('N', NOWH),
    law='Tax Code arts. 103, 383, 388; Decree 1625 art. 1.2.4.1.3 (service bonus read separately under Procedure 1); arts. 1.2.4.1.8 and 1.2.4.1.13 (indemnities and retirement bonus withheld outside the monthly base)', v12=('9170051', 51),
    note='R320 (service bonus), R339 / R340 / R343 / R344 (indemnities) and R345 (retirement bonus) are false here; R320 enters 58150 under Procedure 2 through 9170073')
reg(73, 'CO Service Bonus in the Procedure 2 Base', IT, S, 'flat', [band('58150', rate=100)], acc('R320'), assertion=P2,
    law='Decree 1625 art. 1.2.4.1.3, Procedure 2: the fixed percentage applies to "la totalidad de tales pagos gravables" other than severance savings and their interest; CCG v1.7 Module 6: "Under Procedure 2 ... the service bonus is folded into the ordinary monthly base"', v12=None)
F = '$58240'
reg(74, 'CO Projection Factor for Periods Shorter than 30 Days', IT, SF, 'formula',
    [band('58240', 'IF(AND(AND(EQUALS($58206;1);LESS($58214;2));AND(GREATER($58295;0);LESS($58295;30)));DIVIDE(30;$58295);1)')],
    assertion=RESIDENT, law='Decree 1625 of 2016 art. 1.2.4.1.3 Procedure 1 lits. a-b ("podrá"): payments / days x 30 -> table percentage -> applied to the real payments; Procedure 1 only (factor 1 under Procedure 2)',
    note='option flag 58214 (1 = project, 2 = not; default 2)', v12=None)
reg(75, 'CO Non-taxable Income (contributions and voluntary RAIS)', IT, SF, 'formula',
    [band('58151', f'ADD(MULTIPLY(ADD(ADD($58121;$58122);ADD($58123;$58124));{F});MIN($58258;MIN(MULTIPLY(0.25;$58150);MAX(SUBTRACT(MULTIPLY(2500;$52502);$58258_ytd);0))))')],
    assertion=RESIDENT, law='Tax Code arts. 55, 56: "Los aportes obligatorios que efectúen los trabajadores ... no harán parte de la base para aplicar la retención" - the contributions withheld from the employee (58121-58124, rounded); voluntary RAIS 2,500 UVT a year tracked year-to-date', v12=('9170052', 52))
reg(76, 'CO Net Income', IT, SF, 'formula', [band('58152', f'SUBTRACT(MULTIPLY($58150;{F});$58151)')], assertion=RESIDENT, v12=('9170053', 53))
reg(77, 'CO Dependants Deduction', IT, SF, 'formula', [band('58153', f'IF(GREATER($58207;0);MIN(MULTIPLY(0.10;MULTIPLY($58150;{F}));MULTIPLY(32;$52502));0)')],
    assertion=RESIDENT, law='Tax Code art. 387; Decree 1625 art. 1.2.4.1.6 num. 4.3 (the 72 UVT of art. 336 num. 3 belong to the annual return: DIAN Concepto 011383 of 2024 IV.2)', v12=('9170054', 54))
reg(78, 'CO Prepaid Health Deduction', IT, SF, 'formula', [band('58154', 'MIN($58254;MULTIPLY(16;$52502))')], assertion=RESIDENT, law='Tax Code art. 387', v12=('9170055', 55))
reg(79, 'CO Mortgage Interest Deduction', IT, SF, 'formula', [band('58155', 'MIN($58256;MULTIPLY(100;$52502))')], assertion=RESIDENT, law='Tax Code art. 119; Decree 1625 art. 1.2.4.1.27', v12=('9170056', 56))
reg(80, 'CO Voluntary Pension / AFC Exempt', IT, SF, 'formula',
    [band('58156', f'MIN($58257;MIN(MULTIPLY(0.30;MULTIPLY($58150;{F}));MAX(SUBTRACT(MULTIPLY(3800;$52502);$58156_ytd);0)))')], assertion=RESIDENT,
    law='Tax Code arts. 126-1, 126-4; Decree 1625 art. 1.2.1.22.43 (3,800 UVT a year, tracked year-to-date)', v12=('9170057', 57))
ROOM25 = 'MAX(SUBTRACT(SUBTRACT(MULTIPLY(790;$52502);$58157_ytd);$58166_ytd);0)'
ROOMCAP = 'MAX(SUBTRACT(SUBTRACT(MULTIPLY(1340;$52502);$58159_ytd);$58167_ytd);0)'
reg(81, 'CO 25% Exempt Labour Income (computed last)', IT, SF, 'formula',
    [band('58157', f'MIN(MULTIPLY(0.25;MAX(SUBTRACT(SUBTRACT($58152;ADD(ADD($58153;$58154);$58155));$58156);0));{ROOM25})')], assertion=RESIDENT,
    law='Tax Code art. 206 num. 10 (790 UVT a year); Consejo de Estado S4 rad. 24047 of 2021', v12=('9170058', 58))
reg(82, 'CO 40% / 1,340 UVT Cap', IT, SF, 'formula', [band('58158', f'MIN(MULTIPLY(0.40;$58152);{ROOMCAP})')], assertion=RESIDENT,
    law='Tax Code art. 336 num. 3; Decree 1625 art. 1.2.4.1.6 par. 3 (Decree 2231 of 2023 art. 9); CE S4 rad. 24047 of 2021', v12=('9170059', 59))
reg(83, 'CO Reliefs Applied within the Cap', IT, SF, 'formula',
    [band('58159', 'MIN(ADD(ADD(ADD($58153;$58154);ADD($58155;$58156));$58157);MAX($58158;0))')], assertion=RESIDENT, v12=('9170059', 59))
reg(84, 'CO Taxable Base', IT, SF, 'formula', [band('58160', 'MAX(SUBTRACT($58152;$58159);0)')], assertion=RESIDENT, v12=('9170060', 60))
reg(85, 'CO Procedure 1 Tax before Rounding', IT, SF, 'formula',
    [band('58242', f'DIVIDE(MULTIPLY({table("DIVIDE($58160;$52502)")};$52502);{F})')], assertion=P1,
    law='Tax Code art. 383 (table in UVT, flat lookup per band, open on the left)', v12=('9170061', 61))
reg(86, 'CO Withholding - Procedure 1', IT, SF, 'formula', [band('58161', 'ROUND($58242)')], assertion=P1, law='Tax Code art. 383; rounded to the peso', v12=('9170061', 61))
reg(87, 'CO Withholding - Procedure 2', IT, SF, 'formula', [band('58162', 'ROUND(MULTIPLY($58160;DIVIDE($58250;100)))')],
    assertion=P2, law="Tax Code art. 386; Decree 1625 arts. 1.2.4.1.3 and 1.2.4.1.4 (fixed percentage 58250, recomputed in June and December, applied to the month's taxable payments, service bonus included)", v12=('9170062', 62))
MONTHS = 'MIN(12;MAX($58259;1))'
AVG = f'DIVIDE(DIVIDE($58255;{MONTHS});$52502)'
reg(88, 'CO Termination Withholding Percentage (12-month average)', IT, SF, 'formula',
    [band('58243', f'IF(GREATER({AVG};0);DIVIDE({table(AVG)};{AVG});0)')], assertion=RESIDENT,
    law='Decree 1625 art. 1.2.4.1.8 lits. a-b: taxable payments of the 12 months before the termination "dividiendo por doce (12), o por el número de meses de vinculación si es inferior a doce (12)"; table percentage of that average', v12=('9170064', 64))
reg(89, 'CO Withholding - Indemnities', IT, SF, 'flat',
    [band('58164', 'ROUND(MULTIPLY($band_amount_raw;IF(GREATER(DIVIDE($64992;$52502);204);0.20;$58243)))', rate=100)],
    acc(*INDEMN), assertion=RESIDENT, law='Tax Code art. 401-3 and Decree 1625 art. 1.2.4.1.13 ("las indemnizaciones derivadas de una relación laboral": 20% where the worker earns more than 204 UVT); otherwise Decree 1625 art. 1.2.4.1.8. The 204-UVT test reads the monthly salary, as the CCG v1.7 worked example (Module 9: 4,500,000 = 85.92 UVT; the termination payments stay out)',
    v12=('9170064', 64), note='base: R339 (art. 64), R340 (Labour Code art. 65, "como indemnización"), R343, R344')
reg(90, 'CO Withholding - Retirement Bonus', IT, SF, 'flat', [band('58168', 'ROUND(MULTIPLY($band_amount_raw;$58243))', rate=100)], acc(*BONUS), assertion=RESIDENT,
    law='Decree 1625 art. 1.2.4.1.8 ("bonificaciones por retiro definitivo del trabajador": table percentage of the 12-month average applied to the bonus); the 20% of Tax Code art. 401-3 covers indemnities only', v12=None)
reg(91, 'CO Service Bonus Exempt 25%', IT, SF, 'flat', [band('58166', f'MIN(MULTIPLY(0.25;$band_amount_raw);MAX(SUBTRACT({ROOM25};$58157);0))', rate=100)], acc('R320'),
    assertion=P1, law='Tax Code art. 206 num. 10; Decree 1625 art. 1.2.4.1.3 Procedure 1 (own table read of the service bonus)', v12=('9170065', 65))
reg(92, 'CO Service Bonus Reliefs within the Cap', IT, SF, 'flat', [band('58167', f'MIN($58166;MIN(MULTIPLY(0.40;$band_amount_raw);MAX(SUBTRACT({ROOMCAP};$58159);0)))', rate=100)], acc('R320'),
    assertion=P1, v12=('9170065', 65))
reg(93, 'CO Withholding - Service Bonus (Procedure 1)', IT, SF, 'flat',
    [band('58165', f'ROUND(MULTIPLY({table("DIVIDE(SUBTRACT($band_amount_raw;$58167);$52502)")};$52502))', rate=100)], acc('R320'),
    assertion=P1, law='Decree 1625 art. 1.2.4.1.3 Procedure 1: "el valor a retener es el que figure frente al intervalo al cual corresponda la respectiva prima"', v12=('9170065', 65))
reg(132, 'CO Income Tax Flat', IT, SF, 'flat', [band('58163', 'ROUND($band_amount_raw)', rate=20)], matrix('P'),
    assertion='EQUALS($64552;2)', law='Tax Code art. 408; DIAN Concepto 011108 of 29 June 2026 item 10; severance savings and interest outside the base (Law 100 of 1993 art. 135 par. 3, every payer: Constitutional Court C-397 of 1994; Decree 1625 art. 1.2.4.1.11)',
    v12=('9170063', 63), note="ID, name, taxation type, tax group, rule group, assertion and ordinal of the development team's draft (CO Draft Regulations, 9170132); base = WTC column P")
reg(139, 'CO Total Withholding', IT, SF, 'formula',
    [band('58169', 'MAX(ADD(ADD(ADD($58161;$58162);ADD($58163;$58164));ADD($58165;$58168));MULTIPLY($58150;DIVIDE($58213;100)))')],
    law='Tax Code art. 383 par. 3 (higher rate requested in writing)', v12=('9170069', 69))
reg(141, 'CO Net Pay', IT, SF, 'formula', [band('58170', 'SUBTRACT(SUBTRACT(SUBTRACT(SUBTRACT($58100;$R319);$58129);$58169);ADD($58257;$58258))')],
    law='arithmetic residue in cash: gross less salary in kind, employee contributions, withholding and the voluntary pension / AFC / RAIS deductions; Labour Code art. 149', v12=('9170071', 71))

RETRO_LAW = (DL + ': retro_ kept for social security and the earnings that feed it - contributions belong to the period earned, and a '
             'retroactive correction is re-filed for that period (PILA Technical Annex 2 v30, "Disposiciones comunes a la Planilla N": record A = '
             'original, record C = corrected IBC). The only Colombian regulation of the development team (draft 9170132) is income tax, without retro_.')
NORETRO = ('As the draft 9170132 of the development team: no retro_ - Procedure 1 applies the table to "la totalidad de dichos pagos que se hagan al '
           'trabajador ... durante el respectivo mes" (Decree 1625 of 2016 art. 1.2.4.1.3).')
for r_ in REGS:
    if r_['taxRuleGroup'].startswith('retro_'): r_['divergence'] = RETRO_LAW
    elif r_['taxGroup'] == IT: r_['divergence'] = NORETRO
DESIGN = {'country': 'co', 'regulationCount': len(REGS), 'regulations': REGS}

# ================================================================== inputs / flags (documented accounts)
INPUTS = {
 '64992': ('Contractual monthly salary', '$hr.salary (DD)'), '58295': ('Contributory days (30-day convention)', '$actual_prorata_days'),
 '58201': ('All-inclusive salary 1 / ordinary 2', 'DD All-Inclusive Salary Flag'), '58203': ('Employer eligible for art. 114-1: 1 / 2', 'DD legal-entity field'),
 '58204': ('Occupational-risk class 1-5', 'DD Work Centre Occupational Risk Class'), '64552': ('Tax residence 1 resident / 2 non-resident', 'DD Tax Residence Status, in the account the development team reads in 9170132'), '58259': ('Months of service in the 12 months before termination (1-12)', 'history read'),
 '58206': ('Withholding procedure 1 / 2', 'DD Withholding Procedure'), '58207': ('Number of dependants', 'DD'), '58208': ('Apprentice phase 0 / 1 classroom / 2 practical', 'DD Contract Type 4 + phase field (RESEARCH_GAPS R2)'),
 '58209': ('Employed pensioner 1 / 2', 'DD Worker Sub-Type 01'), '58211': ('Foreign national not affiliated to pension 1 / 2', 'DD'), '58212': ('High-risk pension activity 1 / 2', 'DD'),
 '58213': ('Requested higher withholding rate (%)', 'DD'), '58214': ('Sub-30-day projection option 1 / 2 (default 2)', 'entity option'), '58216': ('Contributor type 51 1 / 2', 'DD Contributor Type'),
 '58220': ('Dismissal without just cause, indefinite-term contract 1 / 2', 'termination record'), '58250': ('Procedure 2 fixed percentage', 'computed in June / December (RESEARCH_GAPS R3)'),
 '58254': ('Prepaid health paid (month)', 'certificate'), '58255': ('Taxable labour payments of the 12 months before termination', 'history read (RESEARCH_GAPS R3)'),
 '58256': ('Mortgage interest paid (month)', 'certificate'), '58257': ('Voluntary pension / AFC contribution (month)', 'payroll deduction'), '58258': ('Voluntary RAIS contribution (month)', 'payroll deduction'),
 '58288': ('Service days 360 (inclusive)', 'DAYS360($hr.contract_start_date;$employee.last_working_date) [ASSUMED function]'),
 '58290': ('Illness incapacity days (from day 1)', 'novelty'), '58291': ('Maternity leave 1 / 2', 'novelty'), '58292': ('Vacation business days taken', 'novelty'),
 '58293': ('Vacation days compensated in cash', 'novelty'), '58294': ('Days without vacation at termination', 'termination record'),
 '58297': ('Days of the semester for the service bonus (0 outside June / December / termination)', 'payroll calendar'),
 '58298': ('Days of the year for severance savings (0 outside December / termination)', 'payroll calendar'), '58299': ('Separation flag 1 / 2', 'DD'),
}
DEFAULT = {'64992': 0, '58295': 30, '58201': 2, '58203': 1, '58204': 1, '64552': 1, '58206': 1, '58259': 12, '58207': 0, '58208': 0, '58209': 2, '58211': 2,
           '58212': 2, '58213': 0, '58214': 2, '58216': 2, '58220': 2, '58250': 0, '58254': 0, '58255': 0, '58256': 0, '58257': 0, '58258': 0,
           '58288': 0, '58290': 0, '58291': 2, '58292': 0, '58293': 0, '58294': 0, '58297': 0, '58298': 0, '58299': 2}
ROWS_INPUT = {w['key'] for w in WROWS}
CONST_ACCTS = set(CONST)
OUT_LOG = []
def log(s=''):
    OUT_LOG.append(s); print(s)


# ================================================================== v1.2-faithful variant (for reproduction)
ER_ACC = {'58141', '58142', '58143', '58144', '58145', '58146', '58137', '58138', '58139'}
EE_ACC = {'58121', '58122', '58123', '58124', '58127'}


def shares_variant(design):
    """Round-1 rounding (each share rounded separately; non-taxable income on the contributions before rounding): the
    convention of the independent calculation. Used to show that every other mechanism matches it exactly."""
    d = copy.deepcopy(design)
    for r in d['regulations']:
        for b in r['bands']:
            if b['debitAccount'] in ('58121', '58122', '58141', '58142'): b['formula'] = UP100
            if b['debitAccount'] == '58137': b['formula'] = 'ROUND($band_amount_raw)'
            if b['debitAccount'] == '58151':
                b['formula'] = b['formula'].replace('ADD(ADD($58121;$58122);ADD($58123;$58124))', 'ADD(ADD($58121_raw;$58122_raw);ADD($58123_raw;$58124_raw))')
    return d


def v12_variant():
    d = shares_variant(DESIGN)
    regs = []
    for r in d['regulations']:
        if r['v12'] is None:
            continue        # regulations new in v2.0 (projection, Procedure 2 service bonus, retirement bonus)
        r = copy.deepcopy(r)
        r['regulationId'], r['ordinal'] = r['v12'][0], r['v12'][1] + r['ordinal'] / 1000.0   # v1.2 order (sub-order kept inside a v1.2 regulation)
        if r['name'] == 'CO Statutory-Benefit Base':
            r['bands'][0]['formula'] = 'ADD($band_amount_raw;IF(LTE($64992;MULTIPLY($52501;2));$52503;0))'
        if r['name'] == 'CO Taxable Labour Payments (monthly read)':
            r['taxabilityRules'] = matrix('N')
        if r['name'] == 'CO Income Tax Flat':
            r['taxabilityRules'] = acc('58150'); r['taxRuleGroup'] = RS
        if r['name'] == 'CO Withholding - Indemnities':
            r['taxabilityRules'] = acc('R339')
            r['bands'][0]['formula'] = 'ROUND(MULTIPLY($band_amount_raw;IF(GREATER(DIVIDE($58150;$52502);204);0.20;$58243)))'
        if r['name'] == 'CO Termination Withholding Percentage (12-month average)':
            r['bands'][0]['formula'] = r['bands'][0]['formula'].replace('MIN(12;MAX($58259;1))', '12')
        if r['name'] == 'CO Gross Earnings':
            r['taxabilityRules'] = matrix(None)
        if r['name'] == 'CO Severance Savings Paid on Termination':
            continue
        if r['name'] == 'CO Total Withholding':
            r['bands'][0]['formula'] = r['bands'][0]['formula'].replace('ADD($58165;$58168)', '$58165')
        if r['name'] == 'CO Net Pay':
            r['bands'][0]['formula'] = 'SUBTRACT(SUBTRACT($58100;$58129);$58169)'
        for b in r['bands']:
            if b.get('formula'): b['formula'] = b['formula'].replace(f';{F}', ';1').replace(f'({F}', '(1')
        regs.append(r)
    d['regulations'] = regs
    return d


# ================================================================== check (a): order
def order_check(design, label):
    regs = sorted(design['regulations'], key=lambda r: r['ordinal'])
    posted_at = {}
    for r in regs:
        for j, b in enumerate(r['bands']):
            posted_at.setdefault(b['debitAccount'], []).append(r['ordinal'])
    defects = []
    for r in regs:
        reads = set()
        reads |= E.variables(r.get('assertion'))
        earlier = set()
        for b in r['bands']:
            vs = E.variables(b.get('formula')) | E.variables(b.get('assertion'))
            for k in ('employeeRateAccount', 'employerRateAccount'):
                if b.get(k): vs.add(b[k])
            reads |= vs                                     # strict: no band reads another band of its own regulation
            earlier.add(b['debitAccount'])
        reads |= {t['account'] for t in r['taxabilityRules'] if t['isTaxable']}
        for v in sorted(reads):
            if v in ('band_amount_raw', 'hours'): continue
            base = v[:-4] if v.endswith('_ytd') or v.endswith('_raw') else v
            if v.endswith('_ytd') and base in posted_at: continue      # prior periods (S14)
            if base in CONST_ACCTS or base in INPUTS: continue
            ps = posted_at.get(base)
            if ps is None:
                if base in ROWS_INPUT: continue                         # WTC row paid as an input
                defects.append((r['regulationId'], r['ordinal'], v, 'never posted')); continue
            if not any(o < r['ordinal'] for o in ps):
                defects.append((r['regulationId'], r['ordinal'], v, f'posted only at ordinal {", ".join(str(int(o)) for o in sorted(set(ps)))}'))
    log(f'[a] order check ({label}): {len(defects)} defect(s)')
    for d in defects: log(f'    {d[0]} (ordinal {int(d[1])}) reads ${d[2]}: {d[3]}')
    return defects


# ================================================================== independent calculation (oracle_v2, read only)
spec = importlib.util.spec_from_file_location('oracle_v2', os.path.join(ORA, 'oracle_v2.py'))
O = importlib.util.module_from_spec(spec); spec.loader.exec_module(O)
UVT = O.UVT
for k, pk in (('52501', 'SMMLV_2026'), ('52502', 'UVT_2026'), ('52503', 'AUX_TRANSPORTE_2026')):
    assert D(CONST[k][0]) == D(O.V(pk)), (k, pk)


def load(fn):
    c = json.load(open(os.path.join(ORA, fn), encoding='utf-8'))
    return c['cases'] if isinstance(c, dict) else c


CASES = load('cases.json') + load('cases_v2r4.json') + load('cases_research.json')
A790, A1340 = Dc(790) * UVT, Dc(1340) * UVT
K25, KCAP = 'RET_EXENTA25_UVT_ANO', 'RET_CAP_UVT_ANO'


def oracle_month(c, room25, roomcap):
    old25, oldcap = O.PAR[K25]['value'], O.PAR[KCAP]['value']
    try:
        O.PAR[K25]['value'] = str(max(room25, Dc(0)) * 12 / UVT)
        O.PAR[KCAP]['value'] = str(max(roomcap, Dc(0)) * 12 / UVT)
        return O.monthly(c)
    finally:
        O.PAR[K25]['value'], O.PAR[KCAP]['value'] = old25, oldcap


PRIOR = {'RC05': {'nonsalary': 0}}   # bonus only in the month of the case (CCG premise), as revisao/rodada5/scripts/oracle_r5_ytd.py


def oracle_ytd(c, prior_over=None):
    per = int(str(c.get('period', '2026-03'))[5:7])
    used25 = usedcap = Dc(0); o = None
    for m in range(1, per + 1):
        cc = c if (not prior_over or m == per) else dict(c, **prior_over)
        o = oracle_month(cc, A790 - used25, A1340 - usedcap)
        if 'ret_exenta_25' in o:
            used25 += Dc(str(o['ret_exenta_25'])); usedcap += Dc(str(o['ret_beneficios_aplicados']))
    return o


# ================================================================== engine inputs from a case
HMAP = {'RN': 'H308', 'HED': 'H306', 'HEN': 'H307', 'DOM': 'H309', 'RN_DOM': 'H312', 'HED_DOM': 'H310', 'HEN_DOM': 'H311'}
RISK = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5}


def monthly_inputs(c):
    inp = dict(DEFAULT)
    inp['64992'] = c['salary']; inp['58295'] = c.get('days', 30)
    inp['58201'] = 1 if c.get('integral') else 2
    inp['58203'] = 1 if c.get('exonerated', True) else 2
    inp['58204'] = RISK[c.get('risk', 'I')]
    if c.get('commission'): inp['R314'] = c['commission']
    if c.get('nonsalary'):
        inp['R316' if c.get('nonsalary_kind', 'pacted') == 'pacted' else 'R318'] = c['nonsalary']
    if c.get('nonsalary_natural'): inp['R318'] = inp.get('R318', 0) + c['nonsalary_natural']
    r = c.get('ret', {})
    inp['58207'] = 1 if r.get('dependientes') else 0
    inp['58254'] = r.get('prepagada', 0); inp['58256'] = r.get('vivienda', 0); inp['58257'] = r.get('afc', 0)
    if r.get('sub30'): inp['58214'] = 1
    lines = [{'unit': HMAP[h['type']], 'hours': h['hours'], 'date': h['date']} for h in c.get('extras', [])]
    return inp, lines


def engine_month(design, c, prior_over=None):
    per = int(str(c.get('period', '2026-03'))[5:7])
    months = {}
    for m in range(1, per + 1):
        cc = c if (not prior_over or m == per) else dict(c, **prior_over)
        months[m] = monthly_inputs(cc)
    return E.run_year(design, CONSTS, months, per)


def f2(x): return round(float(x), 2)


MAPM = [('basic', None), ('extras_total', None), ('auxilio_transporte', 'R304'), ('ley1393_exceso', '58104'), ('IBC', '58106'),
        ('IBC_en_SMMLV', '58107'), ('exonerado_114_1', '58215'),
        ('salud_trab', '58121'), ('pension_trab', '58122'), ('fsp_solidaridad', '58123'), ('fsp_subsistencia', '58124'),
        ('salud_emp', '58141'), ('pension_emp', '58142'), ('arl', '58143'), ('ccf', '58144'), ('sena', '58145'), ('icbf', '58146'),
        ('ret_ingreso_laboral', '58150'), ('ret_incrngo_ss', '58151'), ('ret_subtotal_tras_incrngo', '58152'), ('ret_deduc_dependientes', '58153'),
        ('ret_deduc_prepagada', '58154'), ('ret_deduc_vivienda', '58155'), ('ret_exenta_afc', '58156'), ('ret_exenta_25', '58157'),
        ('ret_cap_40_1340', '58158'), ('ret_beneficios_aplicados', '58159'), ('ret_base_gravable', '58160'),
        ('ret_valor_retener_raw', '58242'), ('ret_valor_retener', '58161')]
EXTRAS = ['R306', 'R307', 'R308', 'R309', 'R310', 'R311', 'R312']


def cmp_monthly(design, c, diffs):
    o = oracle_ytd(c, PRIOR.get(c['id'])) if c.get('retention', True) else O.monthly(c)
    r = engine_month(design, c, PRIOR.get(c['id']))
    A = r.A
    g = lambda k: A.get(k, Dc(0))
    n = 0
    proj = c.get('ret', {}).get('sub30') and c.get('days', 30) < 30
    for ok, ek in MAPM:
        if ok not in o: continue
        if ok.startswith('ret') and not c.get('retention', True): continue
        if ok == 'basic': e = g('R303') if c.get('integral') else g('R302')
        elif ok == 'extras_total': e = sum((g(x) for x in EXTRAS), Dc(0))
        else: e = g(ek)
        ov = o[ok]
        if ok == 'exonerado_114_1': ev_, oval = (e == 1), ov
        elif ok == 'IBC_en_SMMLV': ev_, oval = round(float(e), 6), ov
        elif ok in ('salud_trab', 'pension_trab', 'fsp_solidaridad', 'fsp_subsistencia', 'salud_emp', 'pension_emp', 'arl', 'ccf', 'sena', 'icbf', 'IBC', 'ret_valor_retener'):
            ev_, oval = int(e), ov
        elif ok == 'ret_ingreso_laboral' and proj: ev_, oval = f2(e * g('58240')), ov
        else: ev_, oval = f2(e), ov
        n += 1
        if ok == 'ret_valor_retener' and proj: n -= 1; continue     # the independent calculation keeps the projected (not prorated) figure here
        if ev_ != oval: diffs.append((c['id'], ok, oval, ev_))
        # contributions before rounding
        if ok in ('salud_trab', 'pension_trab', 'fsp_solidaridad', 'fsp_subsistencia', 'salud_emp', 'pension_emp', 'arl', 'ccf', 'sena', 'icbf') and ok + '_raw' in o:
            er = f2(r.raw.get(ek, Dc(0))); n += 1
            if er != o[ok + '_raw']: diffs.append((c['id'], ok + '_raw', o[ok + '_raw'], er))
    return n


def module_inputs(c):
    inp = dict(DEFAULT); inp['64992'] = c.get('salary', 0)
    if c.get('integral'): inp['58201'] = 1
    return inp


def cmp_module(design, c, diffs):
    m = c['module']; o = O.MOD[m](c); n = 0
    if m == 'ret_table':
        inp = dict(DEFAULT); inp['58160'] = c['base_cop']; inp['58240'] = 1
        sub = {'regulations': [r for r in design['regulations'] if r['name'] in ('CO Procedure 1 Tax before Rounding', 'CO Withholding - Procedure 1')]}
        r = E.Run(sub, CONSTS, inp).go()
        pairs = [('valor_retener', int(r.A['58161']))]
    else:
        inp = module_inputs(c)
        if m == 'prestaciones':
            inp['58297' if c['kind'] == 'prima' else '58298'] = c['days']
            if c['kind'] == 'all': inp['58297'] = inp['58298'] = c['days']
        elif m == 'vacaciones':
            md = c['mode']
            if md == 'gozadas': inp['58292'] = c['dias_habiles']
            elif md == 'compensadas': inp['58293'] = c['dias_habiles']
            elif md == 'mixta': inp['58292'], inp['58293'] = c['gozadas'], c['compensadas']
            elif md == 'causacion': inp['58294'] = c['days_worked']
        elif m == 'incapacidad': inp['58290'] = c['days']
        elif m == 'maternidad': inp['58291'] = 1
        elif m == 'terminacion':
            inp['58299'], inp['58220'] = 1, 1
            inp['58288'] = O.days360(c['start'], c['end'])
        elif m == 'pila51':
            inp['58216'] = 1; inp['58295'] = c['days']; inp['64992'] = 0
            inp['58204'] = RISK[c.get('risk', 'I')]
        r = E.Run(design, CONSTS, inp).go()
        A = r.A; g = lambda k: A.get(k, Dc(0)); T = r.trace
        tv = lambda nm: T[nm][1] if nm in T else Dc(0)
        pairs = []
        if m == 'prestaciones':
            pairs.append(('base_prima_cesantias', int(D(g('58171')).quantize(Dc('1'), rounding='ROUND_HALF_UP'))))
            if 'prima' in o: pairs.append(('prima', int(g('R320'))))
            if 'cesantias' in o: pairs += [('cesantias', int(g('R321'))), ('intereses_cesantias', int(g('R322')))]
        elif m == 'vacaciones':
            if 'vac_valor_dia' in o: pairs.append(('vac_valor_dia', int(g('58178'))))
            if c['mode'] == 'gozadas': pairs.append(('vac_pago', int(g('R323'))))
            if c['mode'] == 'compensadas':
                pairs.append(('compensacion_excede_mitad', g('58217') == 1))
                pairs.append(('vac_pago', int(g('R324')) if g('58217') != 1 else ('blocked', o['vac_pago'])))
            if c['mode'] == 'mixta':
                pairs += [('vac_pago_gozadas', int(g('R323'))), ('vac_pago_compensadas', int(g('R324'))), ('vac_total', int(g('R323') + g('R324')))]
            if c['mode'] == 'causacion': pairs.append(('vac_causada', int(g('R156'))))
        elif m == 'incapacidad':
            for k in o:
                if k.startswith('inc_dias_1_2'): pairs.append((k, int(tv('CO Illness Benefit Days 1-2 (employer)'))))
                if k.startswith('inc_dias_3_90'): pairs.append((k, int(tv('CO Illness Benefit Days 3-90 (health insurer)'))))
                if k.startswith('inc_dias_91_180'): pairs.append((k, int(tv('CO Illness Benefit Days 91-180 (health insurer)'))))
            pairs += [('inc_total', int(g('58196'))), ('IBC_incapacidad', int(g('58195')))]
        elif m == 'maternidad':
            pairs += [('lic_valor', int(g('R330'))), ('lic_IBC', int(g('58194')))]
        elif m == 'terminacion':
            pairs += [('indemnizacion_dias', float(g('58189'))), ('indemnizacion_valor', int(g('R339')))]
        elif m == 'pila51':
            ib = g('58197')
            pairs += [('IBC_pension', int(ib.quantize(Dc('1'), rounding='ROUND_HALF_UP'))), ('pension_trab', int(g('58127'))), ('pension_emp', int(g('58137'))),
                      ('IBC_ccf', int(ib.quantize(Dc('1'), rounding='ROUND_HALF_UP'))), ('ccf', int(g('58139'))), ('arl', int(g('58138'))),
                      ('pension_total', int(g('58127') + g('58137')))]
    for k, e in pairs:
        n += 1
        if isinstance(e, tuple):
            continue    # documented: blocked by the design, the independent calculation shows the amount with the flag
        if e != o[k]: diffs.append((c['id'], k, o[k], e))
    return n


# ================================================================== design-cited extra checks (hand calculation from the law)
def extras(design):
    res = []
    U = UVT; S = D(CONST['52501'][0])
    # X1 indemnity withholding T-B (Tax Code art. 401-3): salary 20,000,000 = 381.87 UVT > 204 -> 20% of the art. 64 indemnity
    inp = dict(DEFAULT); inp.update({'64992': 20000000, '58299': 1, '58220': 1, '58288': O.days360('2024-01-10', '2026-06-30')})
    r = E.Run(design, CONSTS, inp).go()
    days = Dc(20) + Dc(15) * (D(inp['58288']) - 360) / 360
    ind = (Dc(20000000) / 30 * days).quantize(Dc('1'), rounding='ROUND_HALF_UP')
    res.append(('X1 indemnity withholding 20% (T-B)', int(r.A['R339']), int(ind), int(r.A['58164']), int((ind * Dc('0.20')).quantize(Dc('1'), rounding='ROUND_HALF_UP'))))
    # X2 service bonus separate read (PB): 750,000 - 25% = 562,500 = 10.74 UVT -> 0; monthly base without the bonus
    inp = dict(DEFAULT); inp.update({'64992': 3000000, 'R320': 750000})
    r = E.Run(design, CONSTS, inp).go()
    res.append(('X2 service bonus read 750,000 -> 0; monthly base excludes it (salary + transport allowance only)', int(r.A['58165']), 0, f2(r.A['58150']), 3249095.0))
    # X3 non-resident 20% on column P: 10,000,000 + severance savings 1,000,000 (outside) -> 2,000,000
    inp = dict(DEFAULT); inp.update({'64992': 10000000, '64552': 2, 'R321': 1000000})
    r = E.Run(design, CONSTS, inp).go()
    res.append(('X3 non-resident 20% (severance outside)', int(r.A['58163']), 2000000, int(r.A.get('58161', 0)), 0))
    # X4 illness 100 days at 3,000,000 with the C-543 floor per day: 2x66,666.67 + 88x66,666.67 + 10x58,363.50
    inp = dict(DEFAULT); inp.update({'64992': 3000000, '58290': 100})
    r = E.Run(design, CONSTS, inp).go()
    dd = Dc(3000000) / 30; fl = S / 30
    exp91 = (max(dd * Dc('0.5'), fl) * 10).quantize(Dc('1'), rounding='ROUND_HALF_UP')
    res.append(('X4 illness days 91-100 floored at SMMLV / 30 (C-543)', int(r.trace['CO Illness Benefit Days 91-180 (health insurer)'][1]), int(exp91), int(r.A['R326']), int((dd * 2 / 3 * 2).quantize(Dc('1'), rounding='ROUND_HALF_UP'))))
    # X5 all-inclusive salary 25,000,000, July: transport allowance 0, IBC 70% = 17,500,000
    inp = dict(DEFAULT); inp.update({'64992': 25000000, '58201': 1})
    r = E.Run(design, CONSTS, inp).go()
    res.append(('X5 all-inclusive: IBC 70%, no transport allowance', int(r.A['58106']), 17500000, int(r.A.get('R304', 0)), 0))
    # X6 overtime 14 / 15 July 2026 (divisor 220 -> 210), H04 of the design: 10 h each, salary 3,000,000, day overtime
    r = E.Run(design, CONSTS, dict(DEFAULT, **{'64992': 3000000}), [{'unit': 'H306', 'hours': 10, 'date': '2026-07-14'}, {'unit': 'H306', 'hours': 10, 'date': '2026-07-15'}], period='2026-07').go()
    exp = Dc(10) * Dc(3000000) / 220 * Dc('1.25') + Dc(10) * Dc(3000000) / 210 * Dc('1.25')
    res.append(('X6 day overtime across 15 July 2026 (220 -> 210)', f2(r.A['R306']), f2(exp), None, None))
    # X7 apprentice classroom phase: support 75% SMMLV, IBC 1 SMMLV, pension not due (gate 58208), no transport allowance
    inp = dict(DEFAULT); inp.update({'58208': 1, '58209': 2})
    r = E.Run(design, CONSTS, inp).go()
    res.append(('X7 apprentice classroom: support 75%, IBC 1 SMMLV, no transport', f2(r.A['R338']), f2(S * Dc('0.75')), int(r.A['58106']), int(S)))
    # X8-X11 CCG v1.7 worked examples, annual caps tracked year-to-date, same pay since 1 January (CCG premise)
    for nm, c, pr, pub in [
        ('X8 CCG retention bonus Sep 2026 (8,000,000 + 20,000,000 pacted)', {'id': 'T105', 'module': 'monthly', 'salary': 8000000, 'nonsalary': 20000000, 'period': '2026-09'}, {'nonsalary': 0}, '3947554.80'),
        ('X9 CCG habitual bonus Oct 2026 (6,000,000 + 12,000,000)', {'id': 'T180', 'module': 'monthly', 'salary': 6000000, 'commission': 12000000, 'period': '2026-10'}, {'commission': 0}, '1763832.00'),
        ('X10 CCG same with a non-salary pact', {'id': 'T183', 'module': 'monthly', 'salary': 6000000, 'nonsalary': 12000000, 'period': '2026-10'}, {'nonsalary': 0}, '1899912.00'),
        ('X11 CCG all-inclusive 25,000,000, July', {'id': 'T239', 'module': 'monthly', 'salary': 25000000, 'integral': True, 'period': '2026-07'}, None, '3243282.00')]:
        r = engine_month(design, c, pr)
        o = oracle_ytd(c, pr)
        res.append((nm + ' (engine / CCG; independent ' + str(o['ret_valor_retener_raw']) + ')', f2(r.A['58242']), float(pub), None, None))
    # --- round 2 (QA r1): Q1-Q5, m4, m5, m9
    def tax_uvt(b):
        for lo, hi, rate, fix in O.V('RET_TABLA_383'):
            lo, hi, rate, fix = D(lo), D(hi), D(rate), D(fix)
            if b > lo and b <= hi: return (b - lo) * rate + fix
        return Dc(0)
    rd = lambda x: int(D(x).quantize(Dc('1'), rounding='ROUND_HALF_UP'))
    # X12 Q1 Procedure 2, 10%, salary 10,000,000 + service bonus 5,000,000: (15,000,000 - 900,000) x 75% x 10%
    r = E.Run(design, CONSTS, dict(DEFAULT, **{'64992': 10000000, '58206': 2, '58250': 10, 'R320': 5000000})).go()
    res.append(('X12 Procedure 2 with the service bonus in the monthly base', int(r.A['58162']), rd((Dc(15000000) - 900000) * Dc('0.75') * Dc('0.10')), int(r.A.get('58165', 0)), 0))
    # X13 Q2 retirement bonus R345 15,000,000, salary 4,500,000, 12-month payments 58,500,000 -> 4,875,000 = 93.08 UVT -> 0%
    r = E.Run(design, CONSTS, dict(DEFAULT, **{'64992': 4500000, 'R345': 15000000, '58255': 58500000})).go()
    res.append(('X13 retirement bonus withheld by Decree 1625 art. 1.2.4.1.8 (0%), outside the monthly base', int(r.A['58168']), 0, f2(r.A['58150']), 4500000.0))
    # X14 Q3 indemnity 6,000,000 after 6 months: 36,000,000 / 6 = 6,000,000 = 114.56 UVT -> table %
    r = E.Run(design, CONSTS, dict(DEFAULT, **{'64992': 6000000, 'R339': 6000000, '58255': 36000000, '58259': 6})).go()
    av = Dc(36000000) / 6 / UVT
    res.append(('X14 average over the months of service when fewer than 12', int(r.A['58164']), rd(Dc(6000000) * tax_uvt(av) / av), None, None))
    # X15 Q5 Procedure 2 + projection option on, 15 days, 10%: no projection under Procedure 2
    r = E.Run(design, CONSTS, dict(DEFAULT, **{'64992': 10000000, '58206': 2, '58250': 10, '58295': 15, '58214': 1})).go()
    res.append(('X15 projection option on does not reach Procedure 2', int(r.A['58162']), rd((Dc(5000000) - 450000) * Dc('0.75') * Dc('0.10')), f2(r.A['58240']), 1.0))
    # X16 m9 salary 9,000,000 (171.84 UVT < 204) + vacation payout 2,000,000 + indemnity 10,000,000: table % of the 12-month average
    r = E.Run(design, CONSTS, dict(DEFAULT, **{'64992': 9000000, 'R156': 2000000, 'R339': 10000000, '58255': 108000000})).go()
    av = Dc(9000000) / UVT
    res.append(('X16 204-UVT test on the monthly salary (termination payments out)', int(r.A['58164']), rd(Dc(10000000) * tax_uvt(av) / av), None, None))
    # X17 m4 one rounding per contributor and fund at 1 SMMLV
    r = E.Run(design, CONSTS, dict(DEFAULT, **{'64992': 1750905, '58203': 2})).go()
    up = lambda x: int(((D(x) / 100).to_integral_value(rounding='ROUND_CEILING')) * 100)
    res.append(('X17 health and pension EE + ER = total rounded once (Decree 780 art. 3.2.1.5 num. 2)', int(r.A['58121'] + r.A['58141']), up(Dc(1750905) * Dc('0.125')),
                int(r.A['58122'] + r.A['58142']), up(Dc(1750905) * Dc('0.16'))))
    # X18 m5 cash gross / net: severance savings deposited (not paid), salary in kind, voluntary pension deduction
    r = E.Run(design, CONSTS, dict(DEFAULT, **{'64992': 5000000, 'R321': 1000000, 'R319': 300000, '58257': 200000})).go()
    res.append(('X18 gross without deposited severance; net = gross - in kind - EE - tax - voluntary', f2(r.A['58100']), 5300000.0,
                f2(r.A['58170']), f2(Dc(5300000) - 300000 - r.A['58129'] - r.A['58169'] - 200000)))
    r = E.Run(design, CONSTS, dict(DEFAULT, **{'64992': 5000000, 'R321': 1000000, 'R322': 120000, '58299': 1})).go()
    res.append(('X19 severance savings and interest paid on termination are in the gross', f2(r.A['58100']), 6120000.0, None, None))
    # X20 deduction row with a negative amount (S18): unpaid leave R6 -1,000,000 lowers the salary payments
    r = E.Run(design, CONSTS, dict(DEFAULT, **{'64992': 5000000, 'R6': -1000000})).go()
    res.append(('X20 deduction rows carry negative amounts (R6 unpaid leave)', f2(r.A['58101']), 4000000.0, None, None))
    bad = []
    for name, a, b, c2, d2 in res:
        ok = (a == b) and (c2 == d2)
        if not ok: bad.append(name)
    return res, bad


# ================================================================== Q4: employee / employer share coding
def share_check(design):
    """Every band posting an employer contribution uses employerRate / employerRateAccount, every employee band
    employeeRate / employeeRateAccount; in a run, the EE-coded postings add up to 58129, the ER ones to 58149, and nothing
    ER reaches the net pay."""
    errs = []
    for r in design['regulations']:
        for b in r['bands']:
            acct = b['debitAccount']
            er = b.get('employerRate') is not None or b.get('employerRateAccount')
            ee = b.get('employeeRate') is not None or b.get('employeeRateAccount')
            if acct in ER_ACC and (ee or not er): errs.append((r['regulationId'], acct, 'employer share coded as employee'))
            if acct in EE_ACC and (er or not ee): errs.append((r['regulationId'], acct, 'employee share coded as employer'))
    rr = E.Run(design, CONSTS, dict(DEFAULT, **{'64992': 8000000, '58212': 1})).go()
    ee_sum = sum((rr.A[a] for a, s in rr.share.items() if s == 'EE' and a in EE_ACC), Dc(0))
    er_sum = sum((rr.A[a] for a, s in rr.share.items() if s == 'ER' and a in ER_ACC), Dc(0))
    if ee_sum != rr.A['58129']: errs.append(('run', '58129', 'EE postings differ from the employee total'))
    if er_sum != rr.A['58149']: errs.append(('run', '58149', 'ER postings differ from the employer total'))
    if rr.A['58100'] - rr.A['58129'] - rr.A['58169'] != rr.A['58170']: errs.append(('run', '58170', 'net pay includes an employer amount'))
    return errs


BYCAT = {w['key']: w['cat'] for w in WROWS}


def DESIGN_REG(name):
    return next(r for r in DESIGN['regulations'] if r['name'] == name)


# ================================================================== sweep (c)
SWEEP_BASES = [('N', '58150'), ('P', '58163_raw'), ('Q', '58106'), ('R', '58113'), ('S', '58114'), ('T', '58108'), ('U', '58112'), ('W', '58171'), ('X', '58175')]


def sweep(design):
    base_inp = dict(DEFAULT); base_inp['64992'] = 3000000
    def run(extra, nr=False):
        inp = dict(base_inp, **extra)
        if nr: inp['64552'] = 2
        r = E.Run(design, CONSTS, inp).go()
        out = {}
        for col, a in SWEEP_BASES:
            if a.endswith('_raw'): out[col] = r.raw.get(a[:-4], Dc(0)) * 5      # 20% band -> base
            else: out[col] = r.A.get(a, Dc(0))
        out['O'] = None
        return out
    b0 = run({}); b0nr = run({}, True)
    rows = []; diffs = []
    for w in ACTIVE:
        amt = Dc(5000000) if w['V'] == PACTED else Dc(1000000)
        if BYCAT.get(w['key']) == 'Deduction': amt = -amt                        # S18
        r1 = run({w['key']: amt}); r1nr = run({w['key']: amt}, True)
        for col, a in SWEEP_BASES:
            base1, base0 = (r1nr, b0nr) if col == 'P' else (r1, b0)
            delta = base1[col] - base0[col]
            flag = w[col]
            if flag == 'Yes': exp = amt
            elif flag == 'Yes/No' and w['V'] == PACTED and col in 'QRSU':
                exp = max(amt - Dc('0.40') * (Dc(3000000) + amt), Dc(0))          # Law 1393 excess
            else: exp = Dc(0)
            routed = col == 'N' and w['key'] in PRIMA + INDEMN + BONUS and flag == 'Yes'
            if routed: exp = Dc(0)
            if delta != exp:
                diffs.append((w['key'], w['name'], col, flag, f2(exp), f2(delta)))
            rows.append((w['key'], col, flag, f2(delta), f2(exp), 'routed' if routed else ('split' if flag == 'Yes/No' and not (w['V'] == PACTED and col in 'QRSU') else '')))
    # O: every N=Yes row must reach a table read (monthly 58150, service-bonus read or indemnity read) when O = Yes
    # O (art. 383 table): a row subject to withholding (N = Yes) must be read on the table - in the monthly read 9170072, the
    # service-bonus read (9170093 / 9170073) or the termination percentage (9170089 / 9170090); a row with O = No must not be
    # in the monthly read
    mon = {x['account'] for x in DESIGN_REG('CO Taxable Labour Payments (monthly read)')['taxabilityRules'] if x['isTaxable']}
    o_miss = []
    for w in ACTIVE:
        if w['N'] == 'Yes' and w['O'] == 'Yes' and w['key'] not in mon | set(PRIMA + INDEMN + BONUS): o_miss.append((w['key'], 'O = Yes but not read on the table'))
        if w['O'] == 'No' and w['key'] in mon: o_miss.append((w['key'], 'O = No but in the monthly table read'))
        if w['N'] == 'Yes' and w['O'] != 'Yes': o_miss.append((w['key'], 'N = Yes with O = ' + w['O']))
    return rows, diffs, o_miss


# ================================================================== run everything
def scenarios(design, label, monthly_only=False):
    diffs = []; n = 0; ran = 0
    for c in CASES:
        if c.get('pending'): continue
        if c['module'] == 'monthly':
            n += cmp_monthly(design, c, diffs); ran += 1
        elif not monthly_only:
            n += cmp_module(design, c, diffs); ran += 1
    log(f'[b] scenarios ({label}): {ran} cases, {n} values compared, {len(diffs)} difference(s)')
    return diffs, n, ran


if __name__ == '__main__':
    json.dump(DESIGN, open(os.path.join(HERE, 'co_design_v2.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    log(f'co_design_v2.json: {len(REGS)} regulations; WTC {os.path.basename(WTC)}: {len(WROWS)} rows, {len(ACTIVE)} active')
    log('')
    log('=== reproduction: v1.2-faithful variant (v1.2 IDs, ordinals and formulas) ===')
    V12 = v12_variant()
    d12 = order_check(V12, 'v1.2')
    dm12, nm12, _ = scenarios(V12, 'v1.2, monthly cases', monthly_only=True)
    for d in dm12: log(f'    {d}')
    dall12, n12, _ = scenarios(V12, 'v1.2, all cases')
    for d in dall12: log(f'    {d[0]:6} {d[1]:28} independent {d[2]}  engine {d[3]}')
    rows12, sd12, _ = sweep(V12)
    grp = collections.Counter((d[2], d[3]) for d in sd12)
    log(f'[c] sweep (v1.2): {len(rows12)} checks; {len(sd12)} difference(s): ' + '; '.join(f'column {k[0]} flag {k[1]}: {v}' for k, v in sorted(grp.items())))
    for d in sd12[:12]: log(f'    {d}')
    log('')
    log('=== v2.0 ===')
    d2 = order_check(DESIGN, 'v2.0')
    SH = shares_variant(DESIGN)
    dsh, nsh, _ = scenarios(SH, 'v2.0 with the rounding convention of the independent calculation (each share; raw contributions in the non-taxable income)')
    for d in dsh: log(f'    {d[0]:6} {d[1]:28} independent {d[2]}  engine {d[3]}')
    dv2, n2, ran2 = scenarios(DESIGN, 'v2.0 (one rounding per contributor and fund; contributions withheld in the non-taxable income)')
    def cause(k):
        if k in ('salud_emp', 'pension_emp'): return 'employer share = total rounded once - employee share (Decree 780 art. 3.2.1.5 num. 2)'
        if k.startswith('ret_'): return 'non-taxable income = contributions withheld (Tax Code arts. 55, 56)'
        if k in ('salud_trab', 'pension_trab'): return 'employee share = statutory 4% to the peso (Law 100 arts. 20, 204); the rounding goes to the fund total'
        return 'other: ' + k
    known = {(x[0], x[1]) for x in dsh}
    grp = collections.Counter(cause(d[1]) for d in dv2 if (d[0], d[1]) not in known)
    for k, v in grp.items(): log(f'    {v:4} x {k}')
    O_ORIG = O
    spec3 = importlib.util.spec_from_file_location('oracle_v2_r3', os.path.join(HERE, 'oracle_r3', 'oracle_v2_r3.py'))
    O = importlib.util.module_from_spec(spec3); spec3.loader.exec_module(O)
    d3, n3, _ = scenarios(DESIGN, 'v2.0 against the adjusted independent calculation (one rounding per fund; contributions withheld)')
    for d in d3: log(f'    {d[0]:6} {d[1]:28} independent {d[2]}  engine {d[3]}')
    O = O_ORIG
    sc = share_check(DESIGN)
    log(f'[d] employee / employer coding: {len(sc)} error(s)')
    for e in sc: log(f'    {e}')
    sw = copy.deepcopy(DESIGN)
    hb = next(r for r in sw['regulations'] if r['name'] == 'CO Health Contribution (EE and ER)')['bands'][1]
    hb['employeeRate'], hb['employerRate'] = hb['employerRate'], None
    nsw = len(share_check(sw))
    log(f'[d] same check on a copy with the employer health band coded as employee: {nsw} error(s) (must be > 0)')
    ex, bad = extras(DESIGN)
    log(f'[b] design checks (hand calculation): {len(ex)}, {len(ex) - len(bad)} exact')
    for x in ex: log(f'    {x[0]}: engine {x[1]} / expected {x[2]}' + (f'; engine {x[3]} / expected {x[4]}' if x[3] is not None else ''))
    rows, sd, om = sweep(DESIGN)
    log(f'[c] sweep: {len(ACTIVE)} active WTC rows x {len(SWEEP_BASES)} bases = {len(rows)} checks; {len(sd)} difference(s)')
    for d in sd: log(f'    {d}')
    log(f'[c] column O (table read): {len(om)} finding(s)')
    for d in om: log(f'    {d}')
    log('    The sweep tests the mechanism (bases, floors, the Law 1393 excess, routing, signs) against the WTC flags; the matrices are generated from the same columns, so their content is checked by construction.')
    split = sorted({r[0] for r in rows if r[5] == 'split'}, key=lambda k: int(k[1:]))
    log(f'    Yes/No rows set to false pending a wage-type split ({len(split)}): {", ".join(split)}')
    open(os.path.join(HERE, 'VALIDATION-run.txt'), 'w', encoding='utf-8').write('\n'.join(OUT_LOG) + '\n')
    with open(os.path.join(HERE, 'SWEEP-run.txt'), 'w', encoding='utf-8') as fh:
        fh.write('WTC row | base (WTC column) | WTC flag | engine delta | expected delta | note\n')
        for r in rows: fh.write(' | '.join(str(x) for x in r) + '\n')
        fh.write(f'\nDifferences: {len(sd)}\n')
        for d in sd: fh.write(str(d) + '\n')
    json.dump({'v12_order': d12, 'v12_diffs': dall12, 'v2_order': d2, 'v2_diffs': dv2, 'shares_diffs': dsh, 'adjusted_diffs': d3, 'share_check': sc, 'swap_caught': nsw, 'o_check': om, 'extras': ex, 'cause_groups': dict(grp), 'extras_bad': bad, 'sweep_diffs': sd, 'values_v2': n2, 'cases_v2': ran2},
              open(os.path.join(HERE, '_run-summary.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1, default=str)
