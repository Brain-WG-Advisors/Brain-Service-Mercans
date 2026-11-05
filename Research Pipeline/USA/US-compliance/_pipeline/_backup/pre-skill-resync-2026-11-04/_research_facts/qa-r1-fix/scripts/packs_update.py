"""QA r1 (agent 2): rewrite the research-pack sections affected by the r1 fixes. Usage: python -I packs_update.py <BASE>"""
import json, os, re, sys

BASE = sys.argv[1]
R = os.path.join(BASE, '_research')
changed = []

def rw(name, fn):
    p = os.path.join(R, name)
    t = open(p, encoding='utf-8').read()
    n = fn(t)
    if n != t:
        open(p, 'w', encoding='utf-8').write(n)
        changed.append(name)

def facts(name):
    return json.load(open(os.path.join(R, name), encoding='utf-8'))

def line(x):
    v = x['value']
    u = x.get('unit_of_measure') or x.get('currency') or ''
    et = x.get('effective_to') or 'open'
    note = (' - ' + x['note']) if x.get('note') else ''
    return '- `%s` = **%s**%s (%s -> %s) [%s, %s, %s, conf %s]%s' % (
        x['key'], v, (' ' + u) if u else '', x['effective_from'], et, x['tier'], x['register_id'], x['verification_method'], x['confidence'], note)

def insert_before_open(t, block):
    i = t.rfind('\n## Open questions')
    return t[:i] + '\n' + block + t[i:] if i >= 0 else t + '\n' + block

def replace_fact_line(t, key, newline):
    return re.sub(r'(?m)^- `%s` = .*$' % re.escape(key), lambda m: newline, t, count=1)

# ---------------------------------------------------------------- FED
fed = facts('CCG-annex_FED-facts.json')
F = {x['key']: x for x in fed['facts']}
def fed_fn(t):
    t = replace_fact_line(t, 'fed.ssn.truncation.format', line(F['fed.ssn.truncation.format']))
    t = replace_fact_line(t, 'fed.efw2.records', line(F['fed.efw2.records']))
    t = t.replace('US-FED-026', 'US-FEDQ1-012 (supersedes US-FED-026, LII copy)')
    new = [x for x in fed['facts'] if x.get('_qa_r1')]
    m01 = [x for x in facts('CCG-m01_foundational-facts.json')['facts'] if x.get('_qa_r1')]
    block = ['## QA round 1 additions (2026-11-02)', '',
             'Answers to RQ-505, RQ-534, RQ-565 (equity), RQ-566 (NRA fringe benefits), RQ-553 (extra pay period) and RQ-554 (2026/2027 holidays), all from IRS, OPM, GPO and eCFR text held locally under `00-official-sources/ccg-sources/FED/`. Facts file is authoritative.', '',
             '**2 - Income tax / 2b - Non-resident regime: equity compensation.** Pub. 15-B (2026) "Employee Stock Options" [A.2, US-FEDQ1-001]; Pub. 15 (2026) sec. 5 and sec. 7 [A.2, US-FEDQ1-002]; Pub. 525 (TY2025) [A.3, US-FEDQ1-003, mechanics only]; 26 CFR 31.3121(v)(2)-1 [A.1, US-FEDQ1-004] and 31.3306(r)(2)-1 [A.1, US-FEDQ1-005]; Pub. 515 (2026) [A.2, US-FEDQ1-006]; Pub. 15-T (2026) Introduction [A.2, US-FEDQ1-007]. LEVEL: withholding (FIT), withholding (FICA/FUTA), employer reporting (W-2 codes V, GG, HH).', '',
             '**8 - Benefits in kind: NRA employees.** Pub. 15-B sec. 4 and Group-Term Life [A.2, US-FEDQ1-008] with Pub. 15-T and Pub. 515 rows above. LEVEL: withholding.', '',
             'Facts added (annex FED and m06_tax carry the same keys and values):']
    block += [line(x) for x in new]
    block += ['', '**1 - Labour code / reporting calendar (m01 1.3 and 1.4).** 5 U.S.C. 6103 [A.1, US-FEDQ1-009]; OPM 2026/2027 schedules [A.2, US-FEDQ1-010]; Pub. 15 (2026) Calendar and sec. 11 legal-holiday list [A.2, US-FEDQ1-011]. Facts in `CCG-m01_foundational-facts.json`:']
    block += [line(x) for x in m01]
    block += ['', '**Derivation (G-SPOT, G-DERIVE).** Each 2026 and 2027 holiday date was re-derived in Python from the 5 U.S.C. 6103(a) rule (nth weekday / fixed date) with the 6103(b)(1) Saturday-to-Friday and EO 11582 Sunday-to-Monday shifts: all 22 dates equal the OPM schedules; the 11 federal 2026 dates also equal the Pub. 15 (2026) list, which adds DC Emancipation Day (Thursday 2026-04-16).',
              '',
              '**Negative finding (G-SPOT, direct artifact inspection).** Pub. 15-T (2026) and Pub. 15 (2026) were searched in full for any 53-weekly / 27-biweekly provision: none. Worksheet 1A line 1b takes the Table 3 count (weekly 52, biweekly 26) and Pub. 15 sec. 8 withholds per regular payroll period, so the extra payday is one more ordinary period. Fact `fed.fit.extra_pay_period.rule`.',
              '',
              '**Confidence note.** `fed.equity.withholding_treatment.resident` is conf medium only for the RSU income-tax timing limb: no IRS publication read names RSUs in a FIT timing sentence; it rests on settlement in shares (Pub. 15-B 83(i) paragraph) and on 31.3121(v)(2)-1(b)(4)(iii). FICA/FUTA timing for RSUs is A.1 (`fed.equity.rsu.fica_timing`, conf high).',
              '',
              '**Not obtained.** The IRS Equity (Stock)-Based Compensation Audit Techniques Guide URL returned 404; the eCFR API returned only paragraph (a) of 26 CFR 1.861-4, so the grant-to-vest sourcing period for options/RSUs of NRA employees stays open (`fed.equity.nra.sourcing_period`).',
              '',
              '**C30 fix.** `fed.indexation.caliber` now rests on the govinfo text of 26 U.S.C. 1(f)(3) [A.1, US-FEDQ1-012]; the LII row US-FED-026 is superseded.',
              '']
    t = insert_before_open(t, '\n'.join(block))
    # open questions mirror
    t = t.rstrip('\n') + '\n' + '- `fed.equity.nra.sourcing_period` (blocking: false) - ' + [u for u in fed['unresolved'] if u['key'] == 'fed.equity.nra.sourcing_period'][0]['why'] + ' **What would close it:** ' + [u for u in fed['unresolved'] if u['key'] == 'fed.equity.nra.sourcing_period'][0]['what_would_close_it'] + ' Related rows: US-FEDQ1-006.\n'
    return t
rw('CCG-annex_FED-research-pack.md', fed_fn)

# ---------------------------------------------------------------- MULTI
mul = {x['key']: x for x in facts('CCG-annex_MULTI-facts.json')['facts']}
def mul_fn(t):
    t = replace_fact_line(t, 'multi.military_spouse.rule', line(mul['multi.military_spouse.rule']))
    t = t.replace('US-FEDP51-009', 'US-MULTIQ1-001')
    t = insert_before_open(t, '## QA round 1 corrections (2026-11-02)\n\n'
        '- `multi.military_spouse.rule` is one open-ended fact from 2018-12-31 (50 U.S.C. 4001 unchanged since Pub. L. 117-333); the 2018-12-31..2025-12-31 / 2026-01-01 split (Synthesis C period copy) is removed, in this file and in WTC global_baseline.\n'
        '- `multi.pit.sourcing.general` and `multi.convenience.default` rest on the govinfo text of 4 U.S.C. 114 [A.1, US-MULTIQ1-001], which supersedes the LII row US-FEDP51-009 (C30).\n'
        '- 27 alias keys of this file were renamed to the canonical State key (e.g. `multi.sui.other_state_wage_credit.ks` -> `ks.sui.other_state_credit`): `_research/qa-r1-fix/KEY-ALIAS-MAP.csv`.\n')
    return t
rw('CCG-annex_MULTI-research-pack.md', mul_fn)

# ---------------------------------------------------------------- GA
ga = facts('CCG-annex_GA-facts.json')
G = [x for x in ga['facts'] if x['key'] in ('ga.wh.rate', 'ga.pit.rate.flat')]
def ga_fn(t):
    lines = '\n'.join(line(x) for x in sorted(G, key=lambda x: (x['key'], x['effective_from'])))
    t = re.sub(r'(?m)^- `ga\.pit\.rate\.flat` = \*\*5\.19\*\*.*\n', '', t)
    t = replace_fact_line(t, 'ga.pit.rate.flat', lines)
    for k in ('ga.report.sui.dol4n', 'ga.live.gdol_rules_2026'):
        x = [y for y in ga['facts'] if y['key'] == k][0]
        t = replace_fact_line(t, k, line(x))
    t = insert_before_open(t, '## QA round 1 corrections (2026-11-02)\n\n'
        'One truth for the 2026 rate, split by level (C32): `ga.wh.rate` (withholding) 5.19% 2026-01-01..2026-05-10 [US-GA-001] and 4.99% from 2026-05-11 [US-GAS5-009]; '
        '`ga.pit.rate.flat` (assessment) 4.99% for the whole of taxable year 2026, retroactive (HB 463). The 2025 value 5.19% left the configuration facts (`_history` of the facts file). '
        'WTC `ga.sit.rate` is renamed `ga.wh.rate` with the same two periods. C29: "placeholder SSN" reworded "temporary substitute SSN" (meaning unchanged).\n')
    return t
rw('CCG-annex_GA-research-pack.md', ga_fn)

# ---------------------------------------------------------------- WA
wa = facts('CCG-annex_WA-facts.json')
def wa_fn(t):
    t = re.sub(r'(?m)^\| `wa\.pit\.exists` \| False \| 2028-01-01 \|  \| US-WAS5-017 \| high \|$',
               '| `wa.pit.exists` | False | 2026-01-01 | 2027-12-31 | US-WAS5-017 | high |\n'
               '| `wa.pit.high_income_tax.rate` | 9.9 % (assessment) | 2028-01-01 |  | US-WAS5-017 | high |\n'
               '| `wa.pit.high_income_tax.agi_threshold` | 1000000 USD | 2028-01-01 |  | US-WAS5-017 | high |', t)
    t = t.replace('| `wa.pfml.employee.share` | 71.43 % | 2026-01-01 | 2026-12-31 | US-WAS5-011 | high |',
                  '| `wa.pfml.employee.share` | 71.43 % | 2026-01-01 | 2026-12-31 | US-WAB5-002 | high |')
    t = insert_before_open(t, '## QA round 1 corrections (2026-11-02)\n\n'
        '- `wa.pit.exists` = False is dated 2026-01-01..2027-12-31 (was effective_from 2028-01-01, inverted). The SB 6346 tax from 2028 is two separate assessment-level facts (`wa.pit.high_income_tax.rate` 9.9%, `wa.pit.high_income_tax.agi_threshold` 1,000,000) [US-WAS5-017, DOR page re-read 2026-11-02].\n'
        '- `wa.pfml.employee.share`: 71.43% for 2026 rests on the Paid Leave employer page [A.2, US-WAB5-002] in CCG and WTC alike; 70.7% from 2027-01-01 on the ESD release [A.2, US-WAS5-015].\n'
        '- `wa.wc.supplemental_pension.rate` carries unit "USD per hour".\n')
    return t
rw('CCG-annex_WA-research-pack.md', wa_fn)

# ---------------------------------------------------------------- IL
il = {x['key']: x for x in facts('CCG-annex_IL-facts.json')['facts']}
def il_fn(t):
    t = replace_fact_line(t, 'il.oracle.il700t.example1.withholding',
                          line(il['il.oracle.il700t.example1.withholding']) + '\n' + line(il['il.oracle.il700t.example1.automated_method_result']))
    t = insert_before_open(t, '## QA round 1: IL-700-T example 1 residual explained (2026-11-02)\n\n'
        'Re-read of the local IL-700-T (R-12/25) p.3 [US-ILR3-001]. Example 1 is a TABLE-method example: weekly 300-302 row, 2 Line-1 allowances = 9.33; minus 0.95 for the Line-2 allowance = 8.38. '
        'Derivation (Python): (301 - 2 x 2,925/52) x 0.0495 = 9.3308 -> 9.33 (tables are computed at the bracket midpoint); 1,000/52 x 0.0495 = 0.9519 -> 0.95; 9.33 - 0.95 = 8.38. '
        'The automated payroll method on exactly 300 gives (300 - 6,850/52) x 0.0495 = 8.3293 -> 8.33. Both are correct for their method; the 0.05 residual is the table midpoint, not a booklet defect. '
        'The CCG must label example 1 as the table method (oracle 8.38) and may show 8.33 as the formula result.\n')
    return t
rw('CCG-annex_IL-research-pack.md', il_fn)

# ---------------------------------------------------------------- IN / IA / VA
inf = facts('CCG-annex_IN-facts.json')['facts']
def in_fn(t):
    for x in inf:
        if x['key'].startswith('in.local.lit.rate.') and x.get('unit_of_measure') == 'percent':
            old = x.get('_unit_converted', '').split(' ')[1] if x.get('_unit_converted') else None
            if old:
                t = re.sub(r'(?m)^(- `%s` = \*\*)%s(\*\* )ratio( \(%s)' % (re.escape(x['key']), re.escape(old), re.escape(x['effective_from'])),
                           lambda m: m.group(1) + str(x['value']) + m.group(2) + 'percent' + m.group(3), t)
    return t + '\n\nQA r1 (2026-11-02): Indiana local LIT rates are stored in percent (2.02 = 2.02%), not as ratios, like every other rate fact.\n'
rw('CCG-annex_IN-research-pack.md', in_fn)
ia = {x['key']: x for x in facts('CCG-annex_IA-facts.json')['facts']}
rw('CCG-annex_IA-research-pack.md', lambda t: replace_fact_line(t, 'ia.wh.method', line(ia['ia.wh.method']) + '\n' + line(ia['ia.wh.formula.rate'])))
va = facts('CCG-annex_VA-facts.json')['facts']
V = {x['key']: x for x in va}
def va_fn(t):
    add = '\n'.join(line(V[k]) for k in ('va.pit.bracket.1.rate', 'va.pit.bracket.2.rate', 'va.pit.bracket.3.rate',
                                          'va.pit.bracket.2.base_tax', 'va.pit.bracket.3.base_tax', 'va.pit.bracket.4.base_tax'))
    return replace_fact_line(t, 'va.wh.method', line(V['va.wh.method']) + '\n' + add)
rw('CCG-annex_VA-research-pack.md', va_fn)

# ---------------------------------------------------------------- master pack
def master_fn(t):
    t = t.replace('truncated (XXX-XX-1234)', 'truncated (last four digits shown, first five masked, e.g. ***-**-1234)')
    block = ('## QA round 1 research corrections (2026-11-02, agent 2)\n\n'
             'Routed by `_qa/CCG-review-r1.json`; finding-by-finding log in `_research/qa-r1-fix/AGENT2-R1.md`.\n\n'
             '- **m01 1.3 / 1.4.** Extra pay period rule and the 2026/2027 federal holiday calendar with the IRS business-day rule are in `CCG-m01_foundational-facts.json` (rows US-FEDQ1-007, -009, -010, -011). State legal holidays stay open (`state.holidays.legal`, non-blocking, 51-way fan-out).\n'
             '- **m06 6.0 matrix.** Equity (resident / nonresident cells) and NRA fringe-benefit treatment are answered (rows US-FEDQ1-001..008); see the annex FED pack.\n'
             '- **Key aliases.** 432 alias groups collapsed to one canonical key (plus 31 same-meaning pairs whose periods differed, re-dated to the canonical fact). Rename map for the builders: `_research/qa-r1-fix/KEY-ALIAS-MAP.csv` (old_key -> canonical_key).\n'
             '- **Level split GA.** `ga.wh.rate` (withholding) vs `ga.pit.rate.flat` (assessment).\n'
             '- **Prior-year values.** Facts with effective_to before 2026-01-01 moved to `_history` in their facts files (C41).\n'
             '- **Gaps.** `_research/gaps.json` lists every open research request (id = RQ id) with blocking flag, sources searched and date; the 9 next-year items are `documented_limitation` with the expected publication.\n')
    t = insert_before_open(t, block)
    t = t.rstrip('\n') + '\n- **`state.holidays.legal`** (m01_foundational; blocking=false). Why: State legal holidays (which move State deposit and filing due dates and some State payday rules) are not in the facts; 51 independent jurisdictions. What would close it: each State revenue department holiday/due-date page and the State holiday statute; a 51-way fan-out.\n' \
        '- **`fed.equity.nra.sourcing_period`** (m06_tax; blocking=false). Why: grant-to-vest sourcing period of 26 CFR 1.861-4(b)(2)(ii)(F) not read. What would close it: full text of 1.861-4 on ecfr.gov or the govinfo CFR annual edition.\n'
    return t
rw('CCG-research-pack.md', master_fn)
print('changed', changed)
