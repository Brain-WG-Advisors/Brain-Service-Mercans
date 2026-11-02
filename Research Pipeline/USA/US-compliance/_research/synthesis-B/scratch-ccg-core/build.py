# Synthesis B - CCG core modules m01..m13 + coverage. Builder.
# Reads the register, fills tier/authority/url/dates from the cited row, checks that every
# quoted number appears in the row text, writes one facts file per unit, then validates.
import csv, json, re, sys, os, subprocess, datetime
BASE = sys.argv[1]
REG = os.path.join(BASE, '00-official-sources', 'legal-basis-register.csv')
OUT = os.path.join(BASE, '_research')
rows = {x['id']: x for x in csv.DictReader(open(REG, encoding='utf-8'))}
IDPAT = re.compile(r'^[A-Z]{2}-[A-Z0-9]{2,12}-[0-9]{3,4}$')
ISO = re.compile(r'^\d{4}-\d{2}-\d{2}$')
TODAY = '2026-11-02'
problems, consumed = [], {}
UNITS = ['m01_foundational','m02_master_data','m03_gross_to_net','m04_compensation','m05_social_security',
         'm06_tax','m07_deductions','m08_leave','m09_termination','m10_reporting','m11_advanced',
         'm12_worked_examples','m13_practices']
facts = {u: [] for u in UNITS}
unres = {u: [] for u in UNITS}

def variants(v):
    out = set()
    if isinstance(v, bool) or not isinstance(v, (int, float)):
        return out
    for d in (0, 1, 2, 3, 4):
        s = f'{v:,.{d}f}'; out.add(s); out.add(s.replace(',', ''))
    s = repr(v); out.add(s)
    if isinstance(v, float) and v == int(v): out.add(f'{int(v):,}'); out.add(str(int(v)))
    return out

def F(unit, key, value, rid, vm='quoted from authority page', conf='high', note=None, uom=None, cur=None,
      ef=None, et='row', check=True):
    r = rows.get(rid)
    if r is None: problems.append(f'{unit} {key}: unknown row {rid}'); return
    if not IDPAT.match(rid): problems.append(f'{unit} {key}: id pattern {rid}'); return
    if r['status'] not in ('active', 'partial'): problems.append(f'{unit} {key}: row {rid} status {r["status"]}'); return
    if r['tier'] not in ('A.1', 'A.2', 'A.3'): problems.append(f'{unit} {key}: row {rid} tier {r["tier"]}'); return
    if check and vm != 'derived arithmetically' and isinstance(value, (int, float)) and not isinstance(value, bool):
        txt = r['figure_or_rule_carried'] + ' ' + r['instrument_name'] + ' ' + r['article_or_section']
        if not any(s in txt for s in variants(value)):
            problems.append(f'{unit} {key}: value {value} not found in {rid} text')
    if ef is None:
        ef = r['effective_from'] if ISO.match(r['effective_from'] or '') else '2026-01-01'
        if not ISO.match(r['effective_from'] or ''):
            note = ((note + ' | ') if note else '') + 'effective_from: register row carries no date; value in force on 2026-01-01 per the row'
    if et == 'row':
        et = r['effective_to'] if ISO.match(r['effective_to'] or '') else None
    if r['status'] == 'partial':
        note = ((note + ' | ') if note else '') + 'PARTIAL register row: carry the partial flag'
    if vm == 'derived arithmetically' and not note:
        raise SystemExit(f'derived fact without note: {key}')
    key = remap(key)
    f = {'key': key, 'value': value}
    if uom: f['unit_of_measure'] = uom
    if cur: f['currency'] = cur
    f.update({'effective_from': ef, 'effective_to': et, 'register_id': rid, 'tier': r['tier'],
              'verification_method': vm, 'authority': r['authority'] or 'see register row',
              'url': r['url'] if len(r['url'] or '') >= 5 else (r['local_file'] or 'see register'),
              'confidence': conf})
    if note: f['note'] = note
    facts[unit].append(f)
    consumed.setdefault(rid, set()).add(f'CCG/{unit}')

def U(unit, key, why, close, attempted=None, blocking=False):
    key = remap(key)
    e = {'key': key, 'why': why, 'attempted': attempted or [], 'what_would_close_it': close, 'blocking': blocking}
    unres[unit].append(e)

P, USD = 'percent', 'USD'
exec(open(os.path.join(os.path.dirname(__file__), 'keymap.py'), encoding='utf-8').read())
exec(open(os.path.join(os.path.dirname(__file__), 'facts_core.py'), encoding='utf-8').read())

# ---- drop keys owned by an annex unit (single source of truth); module cites the annex key
import glob
annex_keys = {}
for p in glob.glob(os.path.join(OUT, 'CCG-annex_*-facts.json')):
    for af in json.load(open(p, encoding='utf-8')).get('facts', []):
        annex_keys.setdefault(af['key'], os.path.basename(p))
dropped = {}
for u in UNITS:
    keep = []
    for f in facts[u]:
        if f['key'] in annex_keys:
            dropped.setdefault(u, []).append((f['key'], annex_keys[f['key']], f['register_id']))
        else:
            keep.append(f)
    facts[u] = keep
json.dump(dropped, open(os.path.join(os.path.dirname(__file__), 'dropped.json'), 'w'), indent=0)
print('dropped (annex-owned keys):', sum(len(v) for v in dropped.values()))
# ---- write + validate
written = []
for u in UNITS:
    doc = {'schema_version': '1.4.0', 'artifact': 'CCG', 'unit': u, 'code': 'US', 'year': 2026,
           'generated_on': TODAY,
           '_note': 'Synthesis B (CCG core worker), 2026-11-02. No fetching: every fact is drawn from an active/partial row of legal-basis-register.csv. Per-state detail lives in the annex units (annex_XX); here state rows appear only as examples or comparison tables. consumed_by is NOT written to the register by this worker (final merge worker does it; ids listed in _research/synthesis-B/CCG-core-report.md).',
           '_annex_keys_cited': {k: f'{src} ({rid})' for k, src, rid in dropped.get(u, [])},
           '_annex_keys_note': 'Keys owned by an annex unit are not duplicated here (one key, one value); the module text cites them from the named annex facts file. Re-run scratch-ccg-core/build.py after the last annex worker so late annex keys are also de-duplicated.',
           'facts': facts[u], 'unresolved': unres[u]}
    p = os.path.join(OUT, f'CCG-{u}-facts.json')
    json.dump(doc, open(p, 'w', encoding='utf-8', newline='\n'), ensure_ascii=False, indent=1)
    written.append(p)
if 'COVERAGE' in globals():
    for row in COVERAGE['coverage_matrix'].values():
        if 'fact_keys' in row: row['fact_keys'] = [remap(k) for k in row['fact_keys']]
    for e in COVERAGE['unresolved']: e['key'] = remap(e['key'])
    p = os.path.join(OUT, 'CCG-coverage-facts.json')
    json.dump(COVERAGE, open(p, 'w', encoding='utf-8', newline='\n'), ensure_ascii=False, indent=1)
    written.append(p)
    for row in COVERAGE['coverage_matrix'].values():
        for s in row.get('sources', []):
            rid = s['register_id']; r = rows.get(rid)
            if r is None or r['status'] not in ('active', 'partial') or r['tier'] not in ('A.1','A.2','A.3'):
                problems.append(f'coverage source {rid}: {r and (r["status"], r["tier"])}')
            elif r['url'] != s['url']:
                problems.append(f'coverage source {rid}: url mismatch')
            consumed.setdefault(rid, set()).add('CCG/coverage')
json.dump({k: sorted(v) for k, v in sorted(consumed.items())},
          open(os.path.join(os.path.dirname(__file__), 'consumed.json'), 'w'), indent=0)
print('PROBLEMS:', len(problems)); [print(' ', x) for x in problems]
for u in UNITS: print(u, len(facts[u]), 'facts', len(unres[u]), 'unresolved')
print('rows consumed:', len(consumed))
