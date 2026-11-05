# QA r3 fix (agent 2). Run once: python -I apply_r3.py   (writes backups first)
import sys, os, json, csv, re, shutil, glob, hashlib
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
sys.path.insert(0, r'C:/Users/instituto/Documents/brain-service/Research Pipeline/USA/US-compliance/_research/qa-r3-fix/scripts')
from lib import *   # chdir to BASE
import jsonschema

TODAY = '2026-11-02'
BK = '_research/qa-r3-fix/_backup'
LOG = {'facts_added': [], 'facts_changed': [], 'facts_moved_to_unresolved': [], 'register_new': [], 'register_changed': [],
       'gaps_closed': [], 'gaps_added': [], 'gaps_local_swept': 0, 'validation': {}}

def backup(p):
    dst = os.path.join(BK, p.replace('/', '__'))
    if not os.path.exists(dst): shutil.copy2(p, dst)

def jload(p): return json.load(open(p, encoding='utf-8'))
def jsave(p, d):
    backup(p)
    open(p, 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')

fields, rows = load_reg(); R = {r['id']: r for r in rows}
backup(REG)

# ---------------------------------------------------------------- register: new rows
FEDDIR = '00-official-sources/ccg-sources/FED/'
def md5(p): return hashlib.md5(open(p, 'rb').read()).hexdigest()
NOTE_EFF = 'effective_from not stated in the instrument; in force as at retrieved_on (QA r2 note)'
new_rows = [
 dict(id='US-FEDQ3-001', domain='income_tax', instrument_name='26 U.S.C. 3401(a) Definitions - wages subject to income-tax withholding, and exclusions (a)(1)-(23) (U.S. Code 2024 ed., govinfo)',
      instrument_type='statute', tier='A.1', authority='U.S. Congress (OLRC/GPO, govinfo)',
      url='https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleC-chap24-sec3401.htm',
      article_or_section='3401(a) (wages); (a)(2),(3),(12),(14),(16),(18),(19),(21),(22); last sentence (409A amounts are wages)', publication_date='2024-01-01',
      effective_from='', effective_to='', supersedes='',
      figure_or_rule_carried='Wages = all remuneration (other than fees paid to a public official) for services performed by an employee for his employer, including the cash value of all remuneration (including benefits) paid in any medium other than cash, except (a)(1)-(23); (a)(12) payments to/from 401(a) trusts, 403(a), SEP 402(h), SIMPLE 408(p), governmental 457(b); (a)(14) group-term life; (a)(16) non-cash tips and cash tips under $20 a month; (a)(18) 127/129/134(b)(4)-(5); (a)(19) 74(c)/108(f)(4)/117/132; (a)(21) 106(b); (a)(22) 106(d) HSA; amounts includible under 409A are wages.',
      language='en', local_file=FEDDIR + 'FED_USC-26-3401_govinfo-2024_2026-11-02.htm', retrieved_on=TODAY, verified_on=TODAY,
      verification_method='quoted from authority page | md5 ' + md5(FEDDIR + 'FED_USC-26-3401_govinfo-2024_2026-11-02.htm') + ' | curl HTTP 200 2026-11-02 | ' + NOTE_EFF,
      consumed_by='', status='active'),
 dict(id='US-FEDQ3-002', domain='social_security', instrument_name='26 U.S.C. 3121(a) FICA wages and exclusions, and 3121(v)(1) salary-reduction deferrals treated as wages (U.S. Code 2024 ed., govinfo)',
      instrument_type='statute', tier='A.1', authority='U.S. Congress (OLRC/GPO, govinfo)', url=R['US-FEDR2-001']['url'],
      article_or_section='3121(a) (a)(2),(5)(A)-(I) incl. (5)(G) cafeteria plan,(12) tips,(18),(19),(20); 3121(v)(1)(A)-(B)', publication_date='2024-01-01',
      effective_from='', effective_to='', supersedes='',
      figure_or_rule_carried='FICA wages = all remuneration for employment incl. non-cash, except (a)(1)-(23). (a)(5)(G): section 125 cafeteria-plan payments that would not be wages outside the plan are excluded. 3121(v)(1)(A): employer contributions under a 401(k) cash or deferred arrangement (elective deferrals) and designated Roth contributions remain FICA wages; (v)(1)(B): 414(h)(2) salary-reduction pickups remain wages.',
      language='en', local_file=R['US-FEDR2-001']['local_file'], retrieved_on=R['US-FEDR2-001']['retrieved_on'], verified_on=TODAY,
      verification_method='quoted from authority page | same local copy as US-FEDR2-001 | ' + NOTE_EFF, consumed_by='', status='active'),
 dict(id='US-FEDQ3-003', domain='social_security', instrument_name='26 U.S.C. 3306(b) FUTA wages and exclusions, and 3306(r)(1) salary-reduction deferrals treated as wages (U.S. Code 2024 ed., govinfo)',
      instrument_type='statute', tier='A.1', authority='U.S. Congress (OLRC/GPO, govinfo)', url=R['US-FEDR2-002']['url'],
      article_or_section='3306(b) (b)(2),(5)(A)-(H) incl. (5)(G) cafeteria plan,(13),(14),(16),(17),(18); 3306(r)(1)(A)-(B)', publication_date='2024-01-01',
      effective_from='', effective_to='', supersedes='',
      figure_or_rule_carried='FUTA wages = all remuneration for employment incl. non-cash, except (b)(1)-(20). (b)(5)(G): section 125 cafeteria-plan payments that would not be wages outside the plan are excluded; (b)(18): HSA payments excludable under 106(d). 3306(r)(1)(A): 401(k) elective deferrals remain FUTA wages.',
      language='en', local_file=R['US-FEDR2-002']['local_file'], retrieved_on=R['US-FEDR2-002']['retrieved_on'], verified_on=TODAY,
      verification_method='quoted from authority page | same local copy as US-FEDR2-002 | ' + NOTE_EFF, consumed_by='', status='active'),
 dict(id='US-FEDQ3-004', domain='income_tax', instrument_name="IRS Publication 15 (2026) Circular E - sec. 9 Form W-4 default when none is furnished (p.26), exempt-certificate expiry (pp.11, 27); sec. 4 SSN not yet issued (p.17)",
      instrument_type='guide', tier='A.2', authority='IRS', url='https://www.irs.gov/pub/irs-pdf/p15.pdf',
      article_or_section='sec. 9 p.26 (new employee without Form W-4), p.27 (exemption expires Feb 15), Calendar p.11; sec. 4 p.17 (Applying for an SSN)', publication_date='2025-12-01',
      effective_from='2026-01-01', effective_to='2026-12-31', supersedes='',
      figure_or_rule_carried="No Form W-4 from a new employee in 2026 (incl. rehires): treat as Single or Married filing separately in Step 1(c) with no entries in Steps 2-4; employee paid before 2020 who never furnished a W-4: single, zero allowances (2019 form). Exempt W-4 not renewed by Feb 15: same default. SSN applied for but not issued: 'Applied For' on paper W-2, all zeros electronically, then W-2c.",
      language='en', local_file=FEDDIR + 'FED_IRS-p15-2026_2026-11-02.pdf', retrieved_on=TODAY, verified_on=TODAY,
      verification_method='quoted from authority page | pp.11, 17, 26, 27 read with PyMuPDF 2026-11-02', consumed_by='', status='active'),
]
for nr in new_rows:
    assert nr['id'] not in R
    row = {k: nr.get(k, '') for k in fields}
    rows.append(row); R[row['id']] = row; LOG['register_new'].append(row['id'])

def reg_append(rid, col, text, sep=' | '):
    r = R[rid]
    if text in r[col]: return
    r[col] = (r[col] + sep + text) if r[col] else text
    LOG['register_changed'].append(f'{rid}.{col}')

def reg_set(rid, col, val):
    if R[rid][col] != val:
        R[rid][col] = val; LOG['register_changed'].append(f'{rid}.{col}')

# ---------------------------------------------------------------- facts helpers
def mk(key, value, rid, note=None, eff='2026-01-01', to=None, vm='quoted from authority page', conf='high', **extra):
    r = R[rid]
    f = dict(key=key, value=value)
    for k in ('unit_of_measure', 'currency'):
        if k in extra: f[k] = extra.pop(k)
    f.update(effective_from=eff, effective_to=to, register_id=rid, tier=r['tier'], verification_method=vm,
             authority=r['authority'], url=r['url'], confidence=conf)
    if note: f['note'] = note
    f.update(extra)
    return f

def upsert(path, facts, drop_unresolved=()):
    d = jload(path)
    for nf in facts:
        hit = [i for i, f in enumerate(d['facts']) if f['key'] == nf['key'] and f.get('effective_from') == nf['effective_from']]
        if hit:
            d['facts'][hit[0]] = nf; LOG['facts_changed'].append(f"{os.path.basename(path)}:{nf['key']}")
        else:
            d['facts'].append(nf); LOG['facts_added'].append(f"{os.path.basename(path)}:{nf['key']}")
    if drop_unresolved:
        d['unresolved'] = [u for u in d['unresolved'] if u['key'] not in drop_unresolved]
    d['generated_on'] = TODAY
    jsave(path, d)

def edit_fact(path, key, eff=None, **chg):
    d = jload(path); n = 0
    for f in d['facts']:
        if f['key'] == key and (eff is None or f.get('effective_from') == eff):
            for k, v in chg.items():
                if v is None: f.pop(k, None)
                else: f[k] = v
            n += 1
    assert n, (path, key, eff)
    jsave(path, d); LOG['facts_changed'].append(f'{os.path.basename(path)}:{key}@{eff or "*"}')

P = lambda n: f'_research/{n}-facts.json'

# ================================================================= 1. federal gross-to-net (RQ-559/562/567/568/570/572)
S15, S15B, ST3401, ST3121, ST3306, W4 = 'US-FEDS5-029', 'US-FEDS5-008', 'US-FEDQ3-001', 'US-FEDQ3-002', 'US-FEDQ3-003', 'US-FEDQ3-004'
p51 = 'Pub. 15 (2026) sec. 15 table, Retirement and pension plans, p.51'
m03 = [
 mk('fed.retirement.pretax.tax_treatment',
    '401(k), 403(b) and 457(b) elective deferrals and SIMPLE salary-reduction contributions reduce federal income-tax withholding wages only (within the 402(g) / 457(b) limits); they remain FICA and FUTA wages. Section 125 cafeteria-plan salary reductions for a qualified benefit (accident and health premiums, health FSA, dependent care, HSA) take the treatment of that benefit outside the plan, so they reduce income-tax, FICA and FUTA wages within the benefit limits.',
    S15, note=p51 + ' rows 2, 4, 5, 8; cafeteria row p.47; Pub. 15-B (2026) Table 2-1 p.6 (US-FEDS5-008); IRC 3121(v)(1)(A) and 3306(r)(1)(A) (US-FEDQ3-002/003).', vm='second independent authority'),
 mk('fed.base.401k_deferral.fit', 'excluded (up to the section 402(g) limit)', S15, note=p51 + ' row 2: "Generally exempt, but see section 402(g) for limitation." IRC 3401(a)(12)(A) (US-FEDQ3-001).', vm='second independent authority'),
 mk('fed.base.401k_deferral.fica', 'included', S15, note=p51 + ' row 2: "Taxable." IRC 3121(v)(1)(A) (US-FEDQ3-002).', vm='second independent authority'),
 mk('fed.base.401k_deferral.futa', 'included', S15, note=p51 + ' row 2: "Taxable." IRC 3306(r)(1)(A) (US-FEDQ3-003).', vm='second independent authority'),
 mk('fed.base.403b_salary_reduction.fit', 'excluded (up to the section 402(g) limit)', S15, note=p51 + ' row 4.'),
 mk('fed.base.403b_salary_reduction.fica', 'included', S15, note=p51 + ' row 4: "Exempt, except amounts contributed through a salary reduction agreement are taxable."'),
 mk('fed.base.403b_salary_reduction.futa', 'included', S15, note=p51 + ' row 4 (same cell spans social security/Medicare and FUTA).'),
 mk('fed.base.457b_salary_reduction.fit', 'excluded (up to the section 457(b) limit)', S15, note=p51 + ' row 8.'),
 mk('fed.base.457b_salary_reduction.fica', 'included', S15, note=p51 + ' row 8: "Taxable."'),
 mk('fed.base.457b_salary_reduction.futa', 'included', S15, note=p51 + ' row 8: "Taxable."'),
 mk('fed.base.simple_salary_reduction.fit', 'excluded', S15, note=p51 + ' row 5: "Exempt."'),
 mk('fed.base.simple_salary_reduction.fica', 'included', S15, note=p51 + ' row 5: "Taxable."'),
 mk('fed.base.simple_salary_reduction.futa', 'included', S15, note=p51 + ' row 5: "Taxable."'),
 mk('fed.base.section125.rule', 'Benefit chosen under a section 125 cafeteria plan: if the employee chooses cash or another taxable benefit, it is subject to all employment taxes; if the employee chooses a nontaxable (qualified) benefit, the treatment is the same as if the benefit were provided outside the plan.',
    S15, note='Pub. 15 (2026) sec. 15 table, "Cafeteria plan benefits under section 125", p.47; IRC 3121(a)(5)(G) and 3306(b)(5)(G) (US-FEDQ3-002/003).', vm='second independent authority'),
 mk('fed.base.section125_health.fit', 'excluded', S15B, note='Pub. 15-B (2026) Table 2-1 p.6, Accident and health benefits: "Exempt (except 2% shareholder-employees of S corporations)".'),
 mk('fed.base.section125_health.fica', 'excluded', S15B, note='Pub. 15-B (2026) Table 2-1 p.6: Exempt. IRC 3121(a)(2) and (5)(G).'),
 mk('fed.base.section125_health.futa', 'excluded', S15B, note='Pub. 15-B (2026) Table 2-1 p.6: Exempt. IRC 3306(b)(2) and (5)(G).'),
 mk('fed.base.dependent_care.fit', 'excluded up to 7,500 a year (3,750 married filing separately)', S15B, note='Pub. 15-B (2026) Table 2-1 p.6 and DCAP p.10; Pub. 15 (2026) p.47 (section 129). IRC 3401(a)(18).'),
 mk('fed.base.dependent_care.fica', 'excluded up to 7,500 a year (3,750 married filing separately)', S15B, note='Pub. 15-B (2026) Table 2-1 p.6. IRC 3121(a)(18).'),
 mk('fed.base.dependent_care.futa', 'excluded up to 7,500 a year (3,750 married filing separately)', S15B, note='Pub. 15-B (2026) Table 2-1 p.6. IRC 3306(b)(13).'),
 mk('fed.base.hsa_contribution.fit', 'excluded for a qualified individual up to the HSA contribution limit (employer or section 125 salary-reduction contributions)', S15B, note='Pub. 15-B (2026) Table 2-1 p.6; HSA employer contributions and cafeteria plans p.17. IRC 3401(a)(22).'),
 mk('fed.base.hsa_contribution.fica', 'excluded for a qualified individual up to the HSA contribution limit (employer or section 125 salary-reduction contributions)', S15B, note='Pub. 15-B (2026) p.6, p.17.'),
 mk('fed.base.hsa_contribution.futa', 'excluded for a qualified individual up to the HSA contribution limit (employer or section 125 salary-reduction contributions)', S15B, note='Pub. 15-B (2026) p.6, p.17. IRC 3306(b)(18).'),
]
m04 = [
 mk('fed.fica.wage_definition.exclusions',
    'FICA wages (IRC 3121(a)) are all remuneration for employment, including non-cash remuneration, except among others: (a)(1) pay above the OASDI wage base (OASDI only); (a)(2) sickness, accident, medical and hospitalization plan payments; (a)(5) payments to or from qualified plans (401(a), 403(a), SEP, 403(b) other than salary reduction, governmental 457, SIMPLE other than elective contributions) and (5)(G) section 125 cafeteria-plan benefits that would not be wages outside the plan; (a)(12) non-cash tips and cash tips under 20 a month; (a)(18) 127/129/134 benefits; (a)(19) meals and lodging excludable under 119; (a)(20) 74(c), 108(f)(4), 117 and 132 fringes. 3121(v)(1): 401(k) elective deferrals and 414(h) salary-reduction pickups remain FICA wages.',
    ST3121, note='Pub. 15 (2026) sec. 5 p.18 (US-FEDQ1-002) and sec. 15 table pp.46-52 (US-FEDS5-029) apply the same rules.', vm='second independent authority'),
 mk('fed.futa.wage_definition.exclusions',
    'FUTA wages (IRC 3306(b)) are all remuneration for employment, including non-cash remuneration, except among others: (b)(1) pay above the 7,000 FUTA wage base; (b)(2) sickness, accident, medical plan payments; (b)(5) qualified-plan payments as in 3121(a)(5), incl. (5)(G) section 125 cafeteria-plan benefits; (b)(13) 127/129/134 benefits; (b)(14) meals and lodging under 119; (b)(16) 74(c), 117, 132 fringes; (b)(17) 106(b); (b)(18) 106(d) HSA. 3306(r)(1): 401(k) elective deferrals remain FUTA wages. Tips: only cash tips of 20 or more a month reported in writing are FUTA wages (Pub. 15 p.52).',
    ST3306, note='Pub. 15 (2026) sec. 15 table pp.46-52 (US-FEDS5-029).', vm='second independent authority'),
 mk('fed.wages.general_definition', 'Wages subject to federal employment taxes generally include all pay given to an employee for services, in cash or other forms (salaries, vacation allowances, bonuses, commissions, taxable fringe benefits), however measured or paid; signing bonuses and payments for cancellation of an employment contract are wages for social security, Medicare, FUTA and income-tax withholding; pay to a former employee for services performed while employed is wages.',
    'US-FEDQ1-002', note='Pub. 15 (2026) sec. 5, p.18.'),
 mk('fed.base.tips.fit', 'withhold on cash tips of 20 or more in a month (tips under 20 a month and non-cash tips: exempt)', S15, note='Pub. 15 (2026) sec. 15 table, Tips, p.52; IRC 3401(a)(16).', vm='second independent authority'),
 mk('fed.base.tips.fica', 'included for cash tips of 20 or more in a month; excluded under 20 a month', S15, note='Pub. 15 (2026) p.52; IRC 3121(a)(12).', vm='second independent authority'),
 mk('fed.base.tips.futa', 'included for all tips of 20 or more in a month reported in writing to the employer; excluded under 20 a month', S15, note='Pub. 15 (2026) p.52.'),
 mk('fed.base.group_term_life.fit', 'excluded (employer may at its option withhold on the cost of coverage over 50,000)', S15B, note='Pub. 15-B (2026) Table 2-1 p.6 and footnote 6. IRC 3401(a)(14).', vm='second independent authority'),
 mk('fed.base.group_term_life.fica', 'excluded up to the cost of 50,000 of coverage; the cost of coverage over 50,000 less employee payments is included (W-2 boxes 1, 3, 5 and box 12 code C)', S15B, note='Pub. 15-B (2026) Table 2-1 p.6, footnote 6.'),
 mk('fed.base.group_term_life.futa', 'excluded', S15B, note='Pub. 15-B (2026) Table 2-1 p.6.'),
 mk('fed.base.educational_assistance.fit', 'excluded up to 5,250 a year under a qualifying educational assistance program', S15B, note='Pub. 15-B (2026) Table 2-1 p.6 and p.11. IRC 3401(a)(18).'),
 mk('fed.base.educational_assistance.fica', 'excluded up to 5,250 a year under a qualifying educational assistance program', S15B, note='Pub. 15-B (2026) Table 2-1 p.6. IRC 3121(a)(18).'),
 mk('fed.base.educational_assistance.futa', 'excluded up to 5,250 a year under a qualifying educational assistance program', S15B, note='Pub. 15-B (2026) Table 2-1 p.6. IRC 3306(b)(13).'),
 mk('fed.base.transportation.fit', 'excluded up to 340 a month for commuter highway vehicle and transit passes and 340 a month for qualified parking', S15B, note='Pub. 15-B (2026) Table 2-1 p.6 (exemption not for 2% S-corporation shareholders).'),
 mk('fed.base.transportation.fica', 'excluded up to 340 a month for commuter highway vehicle and transit passes and 340 a month for qualified parking', S15B, note='Pub. 15-B (2026) Table 2-1 p.6.'),
 mk('fed.base.transportation.futa', 'excluded up to 340 a month for commuter highway vehicle and transit passes and 340 a month for qualified parking', S15B, note='Pub. 15-B (2026) Table 2-1 p.6.'),
]
m06 = [
 mk('fed.fit.wage_definition', 'Wages for income-tax withholding (IRC 3401(a)): all remuneration (other than fees paid to a public official) for services performed by an employee for his employer, including the cash value of all remuneration (including benefits) paid in any medium other than cash, except the exclusions in 3401(a)(1)-(23). Amounts includible in gross income under section 409A are wages.',
    ST3401, note='26 U.S.C. 3401(a), U.S. Code 2024 ed. (local govinfo copy).'),
 mk('fed.fit.wage_definition.exclusions', 'Exclusions relevant to private-sector employees: (a)(2) agricultural labor unless FICA wages; (a)(3) domestic service in a private home; (a)(4) non-business service under 50 a quarter; (a)(8) certain pay abroad / in possessions; (a)(12) payments to or from qualified plans (401(a) trust incl. 401(k) deferrals, 403(a), SEP 402(h), SIMPLE 408(p), governmental 457(b)); (a)(14) group-term life insurance; (a)(15) moving-expense reimbursements deductible under 217; (a)(16) non-cash tips and cash tips under 20 a month; (a)(18) 127 educational assistance, 129 dependent care, 134(b)(4)-(5); (a)(19) 74(c), 108(f)(4), 117 and 132 benefits; (a)(20) self-insured medical reimbursements; (a)(21) 106(b) Archer MSA; (a)(22) 106(d) HSA.',
    ST3401, note='26 U.S.C. 3401(a)(1)-(23).'),
 mk('fed.w4.default_no_certificate', 'Single or Married filing separately in Step 1(c), no entries in Step 2, Step 3 or Step 4 of the 2026 Form W-4', W4, to='2026-12-31',
    note='Pub. 15 (2026) sec. 9, p.26: applies to a new employee (incl. a rehire in 2026) who does not furnish a completed Form W-4. Optional computational bridge: same status with 8,600 in Step 4(a) and zero in Step 4(b).'),
 mk('fed.w4.default_no_certificate.pre2020_employee', 'Employee paid wages before 2020 who never furnished a Form W-4: single with zero allowances on a 2019 Form W-4', W4, to='2026-12-31', note='Pub. 15 (2026) sec. 9, p.26.'),
 mk('fed.w4.exempt_not_renewed.default', 'Exempt Form W-4 not renewed by February 15: withhold as Single or Married filing separately in Step 1(c) with no entries in Steps 2-4; a later exempt Form W-4 applies to future wages only, without refund', W4, to='2026-12-31', note='Pub. 15 (2026) p.27 and Calendar p.11.'),
 mk('fed.ssn.not_issued.w2_rule', "Employee applied for an SSN but has none when Form W-2 is due: enter 'Applied For' on a paper W-2, all zeros in an electronic file; when the SSN is received file Form W-2c (Copy A) with SSA and furnish copies to the employee", W4, note='Pub. 15 (2026) sec. 4, p.17.'),
]
m07 = [
 mk('fed.bik.exclusion_conditions', 'See the per-benefit keys fed.bik.*.conditions; employment-tax treatment per benefit is in fed.base.* (Pub. 15-B (2026) Table 2-1 p.6).', S15B, note='Pub. 15-B (2026) section 2.'),
 mk('fed.bik.hsa.conditions', 'Qualified individual covered by a high deductible health plan and by no other health coverage except permitted coverage; 2026 HDHP: deductible at least 1,700 self-only / 3,400 family, out-of-pocket max 8,500 / 17,000; no contributions after Medicare enrolment; employer contributions comparable for comparable coverage (35% excise otherwise) unless made through a cafeteria plan, where cafeteria nondiscrimination rules apply; partners and 2% S-corporation shareholders cannot make pre-tax contributions; report in W-2 box 12 code W.',
    S15B, note='Pub. 15-B (2026) HSAs, p.17.'),
 mk('fed.bik.health_fsa.conditions', 'Offered only through a section 125 cafeteria plan; salary reduction for plan years beginning in 2026 capped at 3,400 (a plan without the cap is not a cafeteria plan); optional carryover instead of a grace period.', S15B, note='Pub. 15-B (2026) Cafeteria Plans, p.4.'),
 mk('fed.bik.dependent_care.conditions', 'Written dependent care assistance program for employees only; services for a qualifying person and needed to let the employee work; exclusion up to 7,500 (3,750 married filing separately) and not above the smaller of the employee\'s or spouse\'s earned income; not for highly compensated employees unless the program is nondiscriminatory (section 129(d)).',
    S15B, note='Pub. 15-B (2026) Dependent Care Assistance, pp.10-11.'),
 mk('fed.bik.educational_assistance.conditions', 'Separate written educational assistance program for employees only; nondiscriminatory in favour of highly compensated employees; not more than 5% of benefits to more-than-5% owners; no choice of cash instead; covers tuition, fees, books, supplies, equipment and qualified student-loan payments; exclusion up to 5,250 a year.',
    S15B, note='Pub. 15-B (2026) Educational Assistance, p.11; Table 2-1 p.6.'),
 mk('fed.bik.transportation.conditions', 'Commuter highway vehicle and transit passes up to 340 a month and qualified parking up to 340 a month are excluded; not available to 2% S-corporation shareholders; cannot be offered through a cafeteria plan.', S15B, note='Pub. 15-B (2026) Table 2-1 p.6 and p.4 (benefits not allowed in a cafeteria plan).'),
 mk('fed.bik.trump_account.conditions', 'From 2026-07-04 the employer may contribute up to 2,500 a year toward the 5,000 Trump account limit of an employee or dependent, excluded from gross income if paid under a separate written plan for the exclusive benefit of employees meeting requirements similar to section 129(d)(2), (3), (6), (7) and (8).',
    'US-FEDR3-005', eff='2026-07-04', note='Pub. 15-A (2026) What\'s New and sec. 5 Employer Contributions to Trump Accounts (local HTML). FICA/FUTA treatment not stated: see unresolved fed.bik.trump_account.employment_tax_treatment.'),
 mk('fed.bik.valuation.general_rule', 'Fair market value: the amount an employee would have to pay a third party in an arm\'s-length transaction to buy or lease the benefit, on all facts and circumstances; neither the employee\'s view of the value nor the employer\'s cost determines it.', S15B, note='Pub. 15-B (2026) section 3, General Valuation Rule, p.26.'),
 mk('fed.bik.valuation.taxable_amount', 'Include in pay the amount by which the value of the benefit exceeds the sum of any amount the law excludes and any amount the recipient paid for it.', S15B, note='Pub. 15-B (2026) section 1, p.4.'),
 mk('fed.bik.vehicle.valuation_methods', 'Employer-provided vehicle personal use: fair market value (lease cost of a comparable vehicle) or one of three special rules: cents-per-mile, commuting (commuting use only) and lease value.', S15B, note='Pub. 15-B (2026) pp.26-27, p.32.'),
 mk('fed.bik.vehicle.commuting_rule.value_per_one_way', 1.5, S15B, currency='USD', note='Pub. 15-B (2026) Commuting Rule p.27: each one-way commute valued at 1.50 per employee.'),
 mk('fed.bik.treated_as_paid', 'Taxable noncash fringe benefits may be treated as paid per pay period, quarter, half-year, year or other basis, at least annually and all by 31 December; special accounting rule: benefits actually provided in November-December may be treated as paid in the next year. Not for transfers of investment-type personal property or real property (actual transfer date).',
    S15B, note='Pub. 15-B (2026) section 4, pp.31-32.'),
 mk('fed.bik.withholding.method', 'Add the value to regular wages for the payroll period and withhold on the total, or withhold at the 22% supplemental flat rate (37% on supplemental wages over 1 million); income tax, social security and Medicare are withheld on the date(s) the benefit is treated as paid.', S15B, note='Pub. 15-B (2026) section 4, p.31.'),
 mk('fed.bik.vehicle.election_not_to_withhold_fit', True, S15B, note='Pub. 15-B (2026) p.32: the employer may choose not to withhold income tax on personal use of an employer-provided highway motor vehicle, by written notice to the employee by 31 January or within 30 days after the vehicle is first provided, and must include the value in W-2 boxes 1, 3, 5 and 14; social security and Medicare are still withheld.'),
]
fed_unres_m07 = [dict(key='fed.bik.trump_account.employment_tax_treatment',
    why='Pub. 15 (2026) p.3 and Pub. 15-A (2026) state the income-tax exclusion of employer Trump account contributions (from 2026-07-04) but not their social security, Medicare and FUTA treatment; Pub. 15-A says "Monitor IRS.gov for more information".',
    attempted=['00-official-sources/ccg-sources/FED/FED_IRS-p15-2026_2026-11-02.pdf p.3', '00-official-sources/pdfs/FED/irs_p15a.html (What\'s New; sec. 5)', '00-official-sources/ccg-sources/FED/FED_IRS-p15b-2026_2026-11-02.pdf (no Trump account entry)'],
    what_would_close_it='IRS guidance on employer contributions to Trump accounts (a notice or the 2027 Pub. 15-B / Pub. 15-A) stating FICA and FUTA treatment, on irs.gov.')]

upsert(P('CCG-m03_gross_to_net'), m03)
upsert(P('CCG-m04_compensation'), m04)
upsert(P('CCG-m06_tax'), m06)
d = jload(P('CCG-m07_deductions')); d['unresolved'] = [u for u in d['unresolved'] if u['key'] != fed_unres_m07[0]['key']] + fed_unres_m07; jsave(P('CCG-m07_deductions'), d)
upsert(P('CCG-m07_deductions'), m07)
# WTC global_baseline: subject-to flags from the same rows
wtc_fed = [f for f in m03 + m04 if f['key'].startswith('fed.base.')] + [f for f in m07 if f['key'] in ('fed.bik.vehicle.election_not_to_withhold_fit', 'fed.bik.vehicle.commuting_rule.value_per_one_way', 'fed.bik.withholding.method')] \
          + [f for f in m06 if f['key'] == 'fed.w4.default_no_certificate']
upsert(P('WTC-global_baseline'), [dict(f, _mirrored_from='CCG (QA r3 fix)') for f in wtc_fed])

# ================================================================= 2. CA married / HoH Method B annual (RQ-508)
CA = 'US-CAS5-001'
rates = [1.1, 2.2, 4.4, 6.6, 8.8, 10.23, 11.33, 12.43, 13.53, 14.63]
sched = {'married': ([22158, 52528, 82904, 115084, 145448, 742958, 891542, 1000000, 1485906],
                     [0, 243.74, 911.88, 2248.42, 4372.30, 7044.33, 68169.60, 85004.17, 98485.50, 164228.58], 'Table 6 Married Persons'),
         'hoh': ([22173, 52530, 67716, 83805, 98990, 505208, 606251, 1000000, 1010417],
                 [0, 243.90, 911.75, 1579.93, 2641.80, 3978.08, 45534.18, 56982.35, 105925.35, 107334.77], 'Table 7 Unmarried/Head of Household')}
ca_facts, derive = [], []
for st, (ceil, base, tname) in sched.items():
    lo = [0] + ceil
    for i in range(1, 10):   # base_i = base_{i-1} + rate_{i-1} * band_{i-1}
        calc = round(base[i - 1] + rates[i - 1] / 100 * (lo[i] - lo[i - 1]), 2)
        assert abs(calc - base[i]) <= 0.011, (st, i, calc, base[i])
    derive.append(f'{st}: every printed base (Plus column) reproduced from the prior band to within 0.01')
    loc = f'DE 44 Rev. 52 (4-26) p.48 (PDF p.56), Method B {tname}, Annual Payroll Period'
    for n in range(1, 11):
        ca_facts.append(mk(f'ca.pit.bracket.{st}.{n}.rate', rates[n - 1], CA, unit_of_measure='percent', eff='2026-01-01', to='2026-12-31', note=loc))
        if n <= 9: ca_facts.append(mk(f'ca.pit.bracket.{st}.{n}.ceiling', ceil[n - 1], CA, currency='USD', eff='2026-01-01', to='2026-12-31', note=loc))
        ca_facts.append(mk(f'ca.pit.bracket.{st}.{n}.base', base[n - 1], CA, currency='USD', eff='2026-01-01', to='2026-12-31', note=loc + '; tax = base + rate x (taxable income - band floor)'))
ca_facts.append(mk('ca.pit.bracket.married.rates', '1.1 / 2.2 / 4.4 / 6.6 / 8.8 / 10.23 / 11.33 / 12.43 / 13.53 / 14.63 percent, bands per ca.pit.bracket.married.N.ceiling', CA, eff='2026-01-01', to='2026-12-31', note='DE 44 (2026) Method B Table 6 (annual); same rates in Table 7 for head of household (ca.pit.bracket.hoh.N.rate).'))
upsert(P('CCG-annex_CA'), ca_facts)
reg_append(CA, 'verification_method', 'QA r3: married (Table 6) and HoH (Table 7) annual per-band rates and bases transcribed from p.48 (PDF p.56); ' + '; '.join(derive))

# ================================================================= 3. AL standard-deduction phase-out (RQ-506)
AL = 'US-ALS5-001'
al_loc = 'ADOR withholding booklet rev. 01/2026, p.6 Formula step 2A; p.7 Schedule of Standard Deduction Amounts'
al = []
for st, mx, step, size, start, end, floor in (('single', 3000, 25, 500, 25999, 35500, 2500), ('married_separate', 4250, 88, 250, 12999, 17750, 2500),
                                           ('married', 8500, 175, 500, 25999, 35500, 5000), ('head_of_family', 5200, 135, 500, 25999, 35500, 2500)):
    nsteps = -(-(end - 1 - start) // size)   # increments "or part thereof" above start for GI just below end
    last = mx - step * nsteps
    assert last >= floor, (st, last)
    al += [mk(f'al.wh.std_deduction.{st}.phaseout.start_gi', start, AL, currency='USD', note=al_loc),
           mk(f'al.wh.std_deduction.{st}.phaseout.reduction_per_step', step, AL, currency='USD', note=al_loc),
           mk(f'al.wh.std_deduction.{st}.phaseout.step_size', size, AL, currency='USD', note=al_loc + ' ("for each ' + str(size) + ' increment or part thereof of GI above ' + f'{start:,}' + '")'),
           mk(f'al.wh.std_deduction.{st}.phaseout.floor_from_gi', end, AL, currency='USD', note=al_loc + f'; at GI of {end:,} or more the deduction is {floor:,}; last stepped value {last:,}')]
    derive.append(f'AL {st}: {mx} - {step} x {nsteps} = {last} >= floor {floor}')
al.append(mk('al.wh.std_deduction.phaseout_steps', 'Standard deduction by Alabama-certificate status: 0/S 3,000 up to GI 25,999, less 25 per 500 (or part) above 25,999, 2,500 from 35,500; MS 4,250 up to 12,999, less 88 per 250 above, 2,500 from 17,750; M 8,500 up to 25,999, less 175 per 500 above, 5,000 from 35,500; H 5,200 up to 25,999, less 135 per 500 above, 2,500 from 35,500.', AL, note=al_loc))
# spot check against the printed schedule (p.7): MFJ 26,000-26,499 -> 8,325 ; MS 13,000-13,249 -> 4,162
assert 8500 - 175 == 8325 and 4250 - 88 == 4162
upsert(P('CCG-annex_AL'), al)
upsert(P('WTC-country_specific'), [dict(f, _mirrored_from='CCG annex_AL (QA r3 fix)') for f in al])
reg_append(AL, 'verification_method', 'QA r3: phase-out steps for all four statuses read on p.6 and checked against the p.7 schedule (MFJ 26,000-26,499 = 8,325; MS 13,000-13,249 = 4,162); ' + '; '.join(d_ for d_ in derive if d_.startswith('AL')))

# ================================================================= 4. Major 6 - re-point / prove the open keys
for k in ('sc.pit.wh.band.2.rate', 'sc.pit.wh.band.3.rate'):
    edit_fact(P('CCG-annex_SC'), k, register_id='US-SCP51-002', url=R['US-SCP51-002']['url'], tier=R['US-SCP51-002']['tier'], authority=R['US-SCP51-002']['authority'])
reg_append('US-SCP51-002', 'verification_method', 'QA r3: p.1 subtraction method "$3,640 $18,230 3%, then subtract $109.20 / $18,230 and above 6%, then subtract $656.10" carries sc.pit.wh.band.2/3.rate')
for fp in (P('CCG-annex_OH'), P('WTC-country_specific')):
    edit_fact(fp, 'oh.wh.supplemental.rate', register_id='US-OHS5-007', url=R['US-OHS5-007']['url'], tier=R['US-OHS5-007']['tier'], authority=R['US-OHS5-007']['authority'],
              note='ORC 5747.02(A)(3)(c): for taxable years beginning in 2026 and thereafter, 332.00 plus 2.75% above 26,050, so 2.75% is the highest (A)(3) rate; OAC 5703-7-10 (US-OHS5-017) requires supplemental withholding at that highest rate.')
reg_append('US-OHS5-007', 'verification_method', 'QA r3: (A)(3)(c) "For taxable years beginning in 2026 and thereafter, $332.00 plus 2.75% of the amount in excess of $26,050" carries oh.wh.supplemental.rate')
for fp in (P('CCG-annex_CO'), P('WTC-country_specific')):
    for k in ('co.famli.employee.rate', 'co.famli.employer.rate'):
        edit_fact(fp, k, eff='2027-01-01', verification_method='derived arithmetically')
reg_append('US-COB5-301', 'verification_method', 'G-DERIVE (QA r3): 0.86% total 2027 premium ("The 2027 premium rate will be 0.86% of wages") x 50% employee cap = 0.43% employee; 0.86 - 0.43 = 0.43% employer')
reg_append('US-COB5-003', 'verification_method', 'QA r3 quote: "The premiums are set to 0.88% of the employee\'s wage, with 0.44% paid by the employer and 0.44% paid by the employee"')
for fp in (P('CCG-annex_MA'), P('WTC-country_specific')):
    edit_fact(fp, 'ma.pfml.medical.rate', eff='2026-01-01', verification_method='derived arithmetically')
    edit_fact(fp, 'ma.pfml.family.rate', eff='2027-01-01', verification_method='derived arithmetically')
reg_append('US-MAS5-012', 'verification_method', 'G-DERIVE (QA r3): 2026 medical 0.28% employee (40%) + 0.42% employer (60%) = 0.70% (also 0.88% total - 0.18% family = 0.70%); 2027 family 0.28% (40%) + 0.42% (60%) = 0.70%; 0.18% family 2026 / medical 2027 quoted')
reg_append('US-DEP52-001', 'verification_method', 'QA r3 quote (file is a PDF saved as .bin; read with PyMuPDF): p.11 Sec. 201 "at the rate of one and one quarter percent (1.25%)"')
reg_append('US-NCS5-003', 'verification_method', 'QA r3 word-form quote: G.S. 95-25.4(a) "at a rate of not less than time and one half of the regular rate of pay" = 1.5')
reg_append('US-PAS5-001', 'verification_method', 'QA r3 word-form quote: Act 5 of 1968 sec. 4(c), p.3 "not less than one and one-half times the employe\'s regular rate" = 1.5')
reg_append('US-NDS5-017', 'verification_method', 'QA r3 word-form quote: NDCC 51-30, p.1 "any breach of the security system which exceeds two hundred fifty individuals" = 250')
reg_append('US-SDS5-017', 'verification_method', 'QA r3 word-form quote: SDCL 22-40-20 "any breach of system security that exceeds two hundred fifty residents of this state" = 250')
reg_append('US-WAS5-017', 'verification_method', 'QA r3 word-form quote: "annual adjusted gross income exceeding $1 million" = 1,000,000')
x = round((460 * 52 - 2300 - 10000) * 0.04 / 52, 2); assert x == 8.94
edit_fact(P('CCG-m12_worked_examples'), 'ms.oracle.weekly_460_0ex.withholding', verification_method='derived arithmetically')
reg_append('US-MSS5-003', 'verification_method', f'G-DERIVE (QA r3): (460 x 52 - 2,300 single standard deduction - 0 exemptions - 10,000 zero band) x 4.0% / 52 = {x} (flowchart p.1: STDED single 2,300; 4.0% of TI over 10,000)')
edit_fact(P('CCG-annex_OH'), 'oh.pit.municipal.count_in_force', verification_method='direct artifact inspection')
reg_append('US-OHB5-002', 'verification_method', 'QA r3 recount (python csv): 1,083 rows, 685 distinct municipal codes, 678 with begin <= 20261101 <= end')
for fp in (P('CCG-annex_WV'),):
    edit_fact(fp, 'wv.sui.employer.rate.max', verification_method='derived arithmetically')
reg_append('US-WVS5-015', 'verification_method', 'G-DERIVE (QA r3): highest debit-balance rate "seven and five-tenths percent" + "one percent surtax" (21A-5-10, pp.3-4) = 8.5%')
# AR: no local A-tier file carries 250 -> unresolved
d = jload(P('CCG-annex_AR'))
d['facts'] = [f for f in d['facts'] if f['key'] != 'ar.report.sui.efile_threshold_employees']
d['unresolved'] = [u for u in d['unresolved'] if u['key'] != 'ar.report.sui.efile_threshold_employees'] + [dict(key='ar.report.sui.efile_threshold_employees',
    why='The 250-employee electronic-filing threshold is not in the local copy of the DWS Employer Handbook (US-ARP9V-001) nor in any other local Arkansas register file (searched for "250" and "two hundred fifty").',
    attempted=['00-official-sources/pdfs/AR/DWS-Employer-Handbook_2026-11-01.pdf (full text)', 'all local files of active US-AR* register rows (QA r3 local sweep 2026-11-02)'],
    what_would_close_it='Ark. Code Ann. 11-10-215 or the DWS employer reporting page stating the employee-count threshold for mandatory electronic wage reports (reemployment.arkansas.gov / arkleg.state.ar.us).')]
jsave(P('CCG-annex_AR'), d); LOG['facts_moved_to_unresolved'].append('CCG-annex_AR:ar.report.sui.efile_threshold_employees')

# ================================================================= 5. Major 8 - consumed_by + WTC / DD facts for FEDR2 / FEDQ1
m05 = jload(P('CCG-m05_social_security')); fedann = jload(P('CCG-annex_FED')); m06d = jload(P('CCG-m06_tax')); m01d = jload(P('CCG-m01_foundational'))
want = {'fed.fica.nra.fjmq_exempt', 'fed.fica.nra.fjmq_exempt.scope', 'fed.futa.nra.fjmq_exempt', 'fed.fica.nra.other_visas.liable', 'fed.fica.totalization.exemption_rule'}
mir = [dict(f, _mirrored_from='CCG m05 (QA r3 fix)') for f in m05['facts'] if f['key'] in want]
q1 = {'US-FEDQ1-00%d' % i for i in range(1, 9)}
mir += [dict(f, _mirrored_from='CCG m06/m01 (QA r3 fix)') for f in m06d['facts'] + m01d['facts'] if f['register_id'] in q1]
upsert(P('WTC-global_baseline'), mir)
dd = [mk('dd.fed.nra.visa_class', 'Immigration status for nonresident aliens: visa class (F-1, J-1, M-1, Q-1/Q-2, H-1B, L-1, other), whether the work carries out the purpose of admission (incl. authorised CPT/OPT), and resident/nonresident alien status; drives the FICA (IRC 3121(b)(19)) and FUTA (IRC 3306(c)(19)) exemption flags.',
         'US-FEDR2-001', vm='second independent authority', note='IRC 3121(b)(19), 3306(c)(19) (US-FEDR2-002); scope per Pub. 515 (2026) pp.53, 55 (US-FEDS5-016).', _consumers='calc:FICA/FUTA subject-to flags; W-2 boxes 3-6'),
      mk('dd.fed.totalization.exemption', 'Totalization agreement country and exemption flag (employee covered exclusively by a foreign social security system under a section 233 agreement): exempts employee FICA (IRC 3101(c)) and employer FICA (IRC 3111(c)).',
         'US-FEDR2-003', note='Employer side IRC 3111(c) (US-FEDR2-004). The list of agreements and the certificate-of-coverage procedure are SSA documents not held locally (unresolved fed.fica.totalization.agreements_in_force).', _consumers='calc:FICA employee and employer')]
upsert(P('DD-8_sheets'), dd)

# ================================================================= consumed_by from every facts file touched (rule: a fact handed over is consumed)
def unit_token(path):
    d = jload(path); a = d['artifact']; u = d.get('unit')
    return f'{a}/{u}' if u else a
touched = sorted({P(n) for n in ['CCG-m03_gross_to_net', 'CCG-m04_compensation', 'CCG-m06_tax', 'CCG-m07_deductions', 'CCG-annex_CA', 'CCG-annex_AL', 'CCG-annex_SC', 'CCG-annex_OH', 'CCG-annex_CO', 'CCG-annex_MA', 'CCG-annex_AR', 'CCG-annex_WV', 'CCG-m12_worked_examples', 'WTC-global_baseline', 'WTC-country_specific', 'DD-8_sheets', 'CCG-m05_social_security', 'CCG-annex_FED']})
for p in touched:
    tok = unit_token(p)
    for f in jload(p)['facts']:
        rid = f['register_id']
        if rid in R and tok not in R[rid]['consumed_by'].split(';'):
            reg_append(rid, 'consumed_by', tok, sep=';')
# register rows referenced in notes as co-sources
for rid, toks in {'US-FEDQ3-002': ['CCG/m03_gross_to_net', 'WTC/global_baseline'], 'US-FEDQ3-003': ['CCG/m03_gross_to_net', 'WTC/global_baseline'], 'US-FEDQ3-001': ['CCG/m03_gross_to_net', 'CCG/m04_compensation'],
                  'US-FEDR2-002': ['DD/8_sheets'], 'US-FEDR2-004': ['CCG/m05_social_security', 'CCG/annex_FED', 'WTC/global_baseline', 'DD/8_sheets', 'CCG/m06_tax'],
                  'US-FEDR2-001': ['CCG/m06_tax'], 'US-FEDR2-003': ['CCG/m06_tax'], 'US-FEDS5-016': ['DD/8_sheets'], 'US-OHS5-017': ['CCG/annex_OH']}.items():
    for t in toks:
        if t not in R[rid]['consumed_by'].split(';'): reg_append(rid, 'consumed_by', t, sep=';')
for rid in ['US-FEDS5-029', 'US-FEDS5-008', 'US-FEDQ1-002', 'US-FEDR3-005', CA, AL, 'US-SCP51-002', 'US-OHS5-007', 'US-FEDR2-001', 'US-FEDR2-002', 'US-FEDR2-003', 'US-FEDR2-004']:
    reg_set(rid, 'verified_on', TODAY)

# ================================================================= 7. minor 13
for rid in ['US-AKS5-009', 'US-FED-028', 'US-LAP6-001', 'US-TXB5-301', 'US-UTP6-002', 'US-UTP6-003']:
    if not R[rid]['effective_from']:
        extra = {'US-LAP6-001': ' (instrument is a repealed section; status kept for the repeal statement)', 'US-TXB5-301': ' (proposed rule, not adopted: no effective date exists yet)'}.get(rid, '')
        reg_append(rid, 'verification_method', NOTE_EFF + extra)
reg_append('US-NH-001', 'verification_method', 'QA r3 re-verification attempted 2026-11-02 and failed: revenue.nh.gov HTTP 403 (curl), web.archive.org HTTP 429, gc.nh.gov RSA 77 HTTP 403; verified_on left empty on purpose (no date without a re-read); closes with one browser or US-exit read of the NHDRA notice')

save_reg(fields, rows)

# ================================================================= validation
schema = json.load(open(r'C:/Users/instituto/mercans-pipeline/shared/schemas/facts.schema.json', encoding='utf-8'))
V = jsonschema.Draft202012Validator(schema)
ids = {r['id'] for r in rows}
for p in touched:
    d = jload(p); errs = [e.message[:160] for e in V.iter_errors(d)]
    bad = [f['key'] for f in d['facts'] if f['register_id'] not in ids]
    LOG['validation'][os.path.basename(p)] = {'schema_errors': errs[:5], 'n_errors': len(errs), 'unresolved_register_ids': bad}
LOG['derivations'] = derive
json.dump(LOG, open('_research/qa-r3-fix/apply-r3-log.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(json.dumps({k: (len(v) if isinstance(v, list) else v) for k, v in LOG.items() if k != 'validation'}, ensure_ascii=False))
print(json.dumps(LOG['validation'], ensure_ascii=False, indent=0)[:3000])
