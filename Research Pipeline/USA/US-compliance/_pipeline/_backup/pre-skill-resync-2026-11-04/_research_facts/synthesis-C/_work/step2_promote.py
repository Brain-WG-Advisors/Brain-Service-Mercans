# Synthesis C step 2+3: promote held facts and emit closed-period facts.
# Usage: python -I step2_promote.py <BASE> [--write]
import csv, json, os, re, sys, glob, shutil, importlib.util, subprocess
BASE = sys.argv[1]; WRITE = '--write' in sys.argv
RES = os.path.join(BASE, '_research'); BK = os.path.join(RES, 'synthesis-C', '_backup')
WORK = os.path.join(RES, 'synthesis-C', '_work')
REG = {r['id']: r for r in csv.DictReader(open(os.path.join(BASE, '00-official-sources', 'legal-basis-register.csv'), encoding='utf-8'))}
PAT = re.compile(r'^[A-Z]{2}-[A-Z0-9]{2,12}-[0-9]{3,4}$')

def backup(p):
    dst = os.path.join(BK, os.path.relpath(p, BASE))
    if not os.path.exists(dst):
        os.makedirs(os.path.dirname(dst), exist_ok=True); shutil.copy2(p, dst)

_LF = {}
def local_text(rel):
    if not rel: return ''
    if rel in _LF: return _LF[rel]
    t = ''
    for part in re.split(r'[;|]', rel):
        p = os.path.join(BASE, part.strip())
        if not os.path.isfile(p): continue
        try:
            if p.lower().endswith('.pdf'):
                t += subprocess.run(['pdftotext', '-layout', p, '-'], capture_output=True, text=True, encoding='utf-8', errors='replace').stdout
            elif os.path.getsize(p) < 30_000_000:
                t += open(p, encoding='utf-8', errors='replace').read()
        except Exception:
            pass
    _LF[rel] = t; return t

def variants(v):
    out = set()
    if isinstance(v, bool) or not isinstance(v, (int, float)): return out
    for x in {v, v / 100}:
        out.add(f'{x:g}%')
        for d in (0, 1, 2, 3, 4, 5):
            s = f'{x:,.{d}f}'; out.add(s); out.add(s.replace(',', '')); out.add(s.replace(',', ' '))
        out.add(f'{x:g}')
    return {o for o in out if o not in ('0', '0.0', '0.00', '1', '0.000')}

def check(f):
    v = f['value']; r = REG[f['register_id']]
    if isinstance(v, bool) or not isinstance(v, (int, float)): return 'non-numeric'
    if f.get('verification_method') == 'derived arithmetically' and v not in (0,):
        pass
    txt = ' '.join([r['figure_or_rule_carried'], r['instrument_name'], r['article_or_section']])
    vs = variants(v)
    if not vs: return 'trivial-number'
    if v == 0: return 'row_text' if re.search(r'(?<![0-9.,])0\.00?%', txt) else 'NOT_FOUND'
    def hit(t): return any(re.search(r'(?<![0-9.,])' + re.escape(s) + r'(?![0-9]|[.,][0-9])', t) for s in vs)
    if hit(txt): return 'row_text'
    lt = local_text(r['local_file'])
    if lt and hit(lt): return 'local_file'
    if f.get('verification_method') == 'derived arithmetically': return 'derived (not literal)'
    return 'NOT_FOUND'

def vm_of(row):
    v = row['verification_method'].lower()
    if v.startswith('derived arithmetically'): return 'derived arithmetically'
    if v.startswith('second independent'): return 'second independent authority'
    if 'inspected directly' in v or v.startswith('read local file'): return 'direct artifact inspection'
    return 'quoted from authority page'

def mkfact(key, val, rid, ef, et, unit=None, note=None, vm=None, conf='high', extra=None):
    r = REG[rid]
    o = {'key': key, 'value': val}
    if unit == 'USD': o['currency'] = 'USD'
    elif unit: o['unit_of_measure'] = unit
    o.update({'effective_from': ef, 'effective_to': et, 'register_id': rid, 'tier': r['tier'],
              'verification_method': vm or vm_of(r), 'authority': r['authority'] or 'see register row',
              'url': r['url'] if (r['url'] or '').startswith('http') else (r['local_file'] or r['url'] or 'see register'),
              'confidence': ('medium' if (r['status'] == 'partial' and conf == 'high') else conf)})
    n = note or ''
    if r['status'] == 'partial': n = ('[partial row] ' + n).strip()
    if n: o['note'] = n
    if extra: o.update(extra)
    return o

FIXES = []
LOG = []  # (file, key, value, register_id, kind, check)
PROBLEMS = []
def ok_row(f, src):
    r = REG.get(f['register_id'])
    if r is None: PROBLEMS.append(f'{src} {f["key"]}: {f["register_id"]} not in register'); return False
    if not PAT.match(f['register_id']): PROBLEMS.append(f'{src} {f["key"]}: id pattern'); return False
    if r['status'] not in ('active', 'partial'): PROBLEMS.append(f'{src} {f["key"]}: {f["register_id"]} status {r["status"]}'); return False
    if r['tier'] not in ('A.1', 'A.2', 'A.3'): PROBLEMS.append(f'{src} {f["key"]}: {f["register_id"]} tier {r["tier"]}'); return False
    return True

# AK-MI LEGACY specs
LEG = {}
D = os.path.join(RES, 'synthesis-B', '_scratch-CCG-annexes-AK-MI')
for p in glob.glob(os.path.join(D, 'spec_*.py')):
    s = importlib.util.spec_from_file_location('s', p); m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    for lg in getattr(m, 'LEGACY', []): LEG[lg[1]] = lg
LEG_UNIT = {'ak.prevailing_wage.threshold': 'USD', 'ar.wh.supplemental.rate': 'percent', 'ar.report.w2.efile_threshold_employees': 'employees',
            'ar.records.withholding.retention_years': 'years', 'co.sui.wage_base': 'USD', 'co.sui.wage_base.next_year': 'USD',
            'co.sui.new_employer.rate.total': 'percent', 'co.famli.rate.total.2026': 'percent', 'co.prevailing_wage.threshold': 'USD',
            'de.local.wilmington.eit.rate': 'percent', 'ga.sui.wage_base': 'USD', 'hi.nonres.exempt_days': 'days',
            'hi.prevailing_wage.threshold': 'USD', 'id.sui.new_employer.rate': 'percent', 'la.sui.employer.rate.min': 'percent',
            'md.sui.wage_base': 'USD', 'me.wh.bracket.single.1.ceiling': 'USD', 'me.wh.bracket.single.2.ceiling': 'USD',
            'me.report.wh.semiweekly_threshold': 'USD', 'me.sui.new_employer.rate.total': 'percent'}

# Step 3 closed-period facts (rows re-activated with effective_to)
CLOSED = {
 'CCG-annex_ID-facts.json': ([
   ('id.wh.zero_bracket.single.annual', 15000, 'US-IDS5-012', 'USD'),
   ('id.wh.zero_bracket.married.annual', 30000, 'US-IDS5-012', 'USD'),
   ('id.wh.zero_bracket.single.biweekly', 577, 'US-IDS5-012', 'USD')], '2025-04-28', '2026-07-22',
   'EPB00744 edition 04-28-2025: governs 2026 payrolls through 2026-07-22 (closed period; replaced prospectively by the 07-23-2026 edition, US-IDS5-011).',
   ['id.wh.zero_bracket.h1_2026']),
 'CCG-annex_IN-facts.json': ([
   ('in.local.lit.rate.boone', 0.017, 'US-IN-001', 'ratio'),
   ('in.local.lit.rate.marion', 0.0202, 'US-IN-001', 'ratio'),
   ('in.local.lit.rate.min', 0.005, 'US-IN-001', 'ratio'),
   ('in.local.lit.rate.max', 0.03, 'US-IN-001', 'ratio')], '2026-01-01', '2026-09-30',
   'DN#1 R46/01-26 county chart (local copy inspected: Boone 0.017, Marion 0.0202, Porter 0.005, Randolph 0.03); periods 2026-01-01..2026-09-30; replaced by R47 (US-INS5-007) from 2026-10-01.',
   ['in.local.lit.chart.2026_01_to_09']),
 'CCG-annex_OH-facts.json': ([
   ('oh.pit.wh.method.period_a', 'formula: TW=pay x PP-650 x exemptions; 1.775% to 26,050; 462.39+2.990% to 100,000; 2,673.50+3.640% above; no rounding instruction', 'US-OHP52-001', None),
   ('oh.pit.wh.rate.1', 1.775, 'US-OHP52-001', 'percent'),
   ('oh.pit.wh.rate.2', 2.99, 'US-OHP52-001', 'percent'),
   ('oh.pit.wh.rate.3', 3.64, 'US-OHP52-001', 'percent'),
   ('oh.pit.wh.break.1', 26050, 'US-OHP52-001', 'USD'),
   ('oh.pit.wh.break.2', 100000, 'US-OHP52-001', 'USD'),
   ('oh.pit.wh.base_tax.2', 462.39, 'US-OHP52-001', 'USD'),
   ('oh.pit.wh.base_tax.3', 2673.50, 'US-OHP52-001', 'USD')], '2025-10-01', '2026-07-31',
   'Optional Computer Formula eff. 2025-10-01: governs pay dates 2025-10-01..2026-07-31 (closed period; retro corrections); replaced by US-OHS5-001 from 2026-08-01.',
   ['oh.pit.wh.method.period_a']),
 'WTC-country_specific-facts.json': ([
   ('id.sit.zero_bracket.single', 15000, 'US-IDS5-012', 'USD'),
   ('id.sit.zero_bracket.married', 30000, 'US-IDS5-012', 'USD')], '2025-04-28', '2026-07-22',
   'EPB00744 edition 04-28-2025: governs 2026 payrolls through 2026-07-22 (closed period); replaced by US-IDS5-011 from 2026-07-23.',
   ['id.sit.zero_bracket.2026_h1']),
}
CLOSED_WTC_IN = ([('in.local.county_lit.rate.boone', 0.017, 'US-IN-001', 'ratio')], '2026-01-01', '2026-09-30',
   'DN#1 R46/01-26 county chart (local copy inspected): periods 2026-01-01..2026-09-30; replaced by R47 (US-INS5-007) from 2026-10-01.')

summary = {}
for p in sorted(glob.glob(os.path.join(RES, '*-facts.json'))):
    fn = os.path.basename(p)
    if re.match(r'CCG-(m\d\d_|coverage)', fn): continue  # rebuilt by scratch-ccg-core/build.py
    d = json.load(open(p, encoding='utf-8'))
    before = len(d['facts']); prom = []; kept_unres = []; removed = []
    for f in d.pop('_facts_pending_register_id_pattern', []) or []:
        prom.append(('pending', f))
    blk = d.pop('_facts_blocked_by_register_id_pattern', None)
    if blk: prom += [('blocked', f) for f in blk.get('facts', [])]
    for u in d['unresolved']:
        w = u['why'] + ' ' + u['what_would_close_it']
        if u['key'].endswith('.meta.register_id_pattern'):
            removed.append(u['key']); continue
        if 'legacy id fails the facts.schema register_id pattern' in w and u['key'] in LEG:
            dom, key, val, rid, ef, et = LEG[u['key']][:6]; nt = LEG[u['key']][6] if len(LEG[u['key']]) > 6 else ''
            unit = LEG_UNIT.get(key) if isinstance(val, (int, float)) and not isinstance(val, bool) else None
            prom.append(('legacy', mkfact(key, val, rid, ef, et, unit, nt or None, extra={'_domain': dom})))
            removed.append(u['key']); continue
        if '_value' in u and 'pattern' in w:
            prom.append(('wtc-carry', mkfact(u['key'], u['_value'], u['_register_id'], u['_effective_from'], u['_effective_to'], u.get('_unit'), u.get('_note'))))
            removed.append(u['key']); continue
        if fn.startswith('WTC-country') and u['key'] == 'mt.sui.rate_schedule':
            removed.append(u['key']); continue
        kept_unres.append(u)
    d['unresolved'] = kept_unres
    if fn in CLOSED:
        items, ef, et, note, drop = CLOSED[fn]
        for key, val, rid, unit in items:
            prom.append(('closed-period', mkfact(key, val, rid, ef, et, unit, note, vm='direct artifact inspection' if rid == 'US-IN-001' else None)))
        d['unresolved'] = [u for u in d['unresolved'] if not (u['key'] in drop and removed.append(u['key']) is None)]
    if fn == 'WTC-country_specific-facts.json':
        items, ef, et, note = CLOSED_WTC_IN
        for key, val, rid, unit in items:
            prom.append(('closed-period', mkfact(key, val, rid, ef, et, unit, note, vm='direct artifact inspection')))
    existing = {(f['key'], f['effective_from']) for f in d['facts']}
    added = 0
    for kind, f in prom:
        if isinstance(f['value'], str) and re.fullmatch(r'-?[0-9]+(\.[0-9]+)?', f['value'].strip()):
            sv = f['value'].strip(); f['value'] = float(sv) if '.' in sv else int(sv)
            FIXES.append((fn, f['key'], f'numeric string {sv!r} -> number'))
        if f['key'] == 'mo.pit.local.kansas_city.earnings_tax.rate' and f['register_id'] == 'US-MOP52-006':
            r = REG['US-MOP9W-001']
            f.update({'register_id': 'US-MOP9W-001', 'tier': r['tier'], 'authority': r['authority'], 'url': r['url'], 'confidence': 'high'})
            f['note'] = (f.get('note', '') + ' | Synthesis C: rebound from US-MOP52-006 (St. Louis row, does not carry KC) to US-MOP9W-001 (KC earnings tax page, 1%).').strip(' |')
            FIXES.append((fn, f['key'], 'register_id US-MOP52-006 -> US-MOP9W-001'))
        if f['key'].endswith('oracle.biweekly_2000_1ex.result') and f['register_id'] == 'US-MIPIT-001':
            f['verification_method'] = 'derived arithmetically'
            f['note'] = ((f.get('note') or '') + ' | Derivation: 5,900/26 = 226.92; (2,000 - 226.92) x 4.25% = 75.356 -> 75.36 (Guide 446 Rev. 02-26 rate and exemption).').strip(' |')
            FIXES.append((fn, f['key'], 'verification_method -> derived arithmetically (derivation added)'))
        if f['key'] == 'co.sui.new_employer.total.rate' and f['register_id'] == 'US-COP51-003':
            r = REG['US-COP51-004']
            f.update({'register_id': 'US-COP51-004', 'tier': r['tier'], 'authority': r['authority'], 'url': r['url']})
            f['note'] = ((f.get('note') or '') + ' | Synthesis C: rebound from US-COP51-003 (wage-limit page, no 3.05) to US-COP51-004 (introductory rates: 1.53+0.17+1.35 = 3.05).').strip(' |')
            FIXES.append((fn, f['key'], 'register_id US-COP51-003 -> US-COP51-004'))
        if not ok_row(f, fn):
            # keep it visible as unresolved rather than drop
            d['unresolved'].append({'key': f['key'], 'why': f'Held fact (value {f["value"]!r}) could not be promoted: register row {f["register_id"]} is {REG.get(f["register_id"], {}).get("status")} / {REG.get(f["register_id"], {}).get("tier")}.',
                                    'attempted': ['Synthesis C promotion 2026-11-02'], 'what_would_close_it': f'An active A-tier register row carrying this value (replace {f["register_id"]}).', 'blocking': False})
            continue
        if (f['key'], f['effective_from']) in existing:
            LOG.append((fn, f['key'], f['value'], f['register_id'], kind, 'DUPLICATE key+effective_from: skipped')); continue
        c = check(f)
        if c in ('NOT_FOUND', 'trivial-number') and f['value'] == 0 and re.search(r'(not|never|no|cannot)[^.]{0,60}(deduct|withh|employee)', REG[f['register_id']]['figure_or_rule_carried'], re.I):
            c = 'zero by rule (row states no employee deduction)'
        if c == 'NOT_FOUND':
            f['confidence'] = 'medium' if f['confidence'] == 'high' else f['confidence']
            f['note'] = ((f.get('note') or '') + ' | Synthesis C: value not found literally in the register row text or local file; bound to the row by the Stage 5 reading.').strip(' |')
        d['facts'].append(f); existing.add((f['key'], f['effective_from'])); added += 1
        LOG.append((fn, f['key'], f['value'], f['register_id'], kind, c))
    summary[fn] = {'facts_before': before, 'promoted': added, 'unresolved_removed': len(removed), 'facts_after': len(d['facts']), 'unresolved_after': len(d['unresolved'])}
    if WRITE and (added or removed):
        backup(p)
        json.dump(d, open(p, 'w', encoding='utf-8', newline='\n'), ensure_ascii=False, indent=1)
with open(os.path.join(WORK, 'step2-promotion-log.csv'), 'w', encoding='utf-8', newline='') as fh:
    w = csv.writer(fh, lineterminator='\n'); w.writerow(['file', 'key', 'value', 'register_id', 'kind', 'number_check']); w.writerows(LOG)
json.dump({'summary': summary, 'problems': PROBLEMS, 'fixes': FIXES}, open(os.path.join(WORK, 'step2-summary.json'), 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
import collections
print('promoted total', sum(v['promoted'] for v in summary.values()))
print(collections.Counter((k, c) for _, _, _, _, k, c in LOG))
print('PROBLEMS', len(PROBLEMS)); [print(' ', x) for x in PROBLEMS[:40]]
for fn, v in summary.items():
    if v['promoted'] or v['unresolved_removed']: print(fn, v)
