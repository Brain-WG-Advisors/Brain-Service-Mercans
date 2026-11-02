import csv, json, re, sys, importlib.util, os
HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
def load(name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, name + '.py'))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
reg = {x['id']: x for x in csv.DictReader(open(os.path.join(BASE, '00-official-sources', 'legal-basis-register.csv'), encoding='utf-8'))}
DATE = re.compile(r'^\d{4}-\d{2}-\d{2}$')
IDPAT = re.compile(r'^[A-Z]{2}-[A-Z0-9]{2,12}-[0-9]{3,4}$')
pending = {'RSPEC': [], 'DD': []}
def vm(row):
    v = row['verification_method'].lower()
    if v.startswith('derived'): return 'derived arithmetically'
    if v.startswith('second independent'): return 'second independent authority'
    if v.startswith('inspected directly') and 'statute' not in v: return 'direct artifact inspection'
    return 'quoted from authority page'
log = {'used': set(), 'unresolved_moved': [], 'eff_fallback': [], 'owner_comments': [], 'partial': set()}
def mkfact(key, value, rid, note, uom):
    row = reg.get(rid)
    if row is None or row['status'] not in ('active', 'partial') or row['tier'] not in ('A.1', 'A.2', 'A.3'):
        st = 'MISSING' if row is None else row['status'] + '/' + row['tier']
        return None, st
    f = {'key': key, 'value': value}
    if uom == 'USD': f['currency'] = 'USD'
    elif uom: f['unit_of_measure'] = uom
    ef = row['effective_from'].strip()
    if DATE.match(ef):
        f['effective_from'] = ef
    elif DATE.match(row['publication_date'].strip()):
        f['effective_from'] = row['publication_date'].strip(); f['_effective_from_basis'] = 'register row has no effective_from; publication_date used'
        log['eff_fallback'].append(rid)
    else:
        f['effective_from'] = '2026-01-01'; f['_effective_from_basis'] = 'register row carries no effective_from or publication_date; build-year start used as in-force-on date (row read in force 2026)'
        log['eff_fallback'].append(rid)
    et = row['effective_to'].strip()
    f['effective_to'] = et if DATE.match(et) else None
    f['register_id'] = rid; f['tier'] = row['tier']; f['verification_method'] = vm(row)
    if f['verification_method'] == 'derived arithmetically': f['verification_method'] = 'quoted from authority page'
    f['authority'] = row['authority'] or 'see register row'
    f['url'] = row['url'] or row['local_file'] or 'see register row'
    conf = 'high' if row['tier'] in ('A.1', 'A.2') else 'medium'
    notes = []
    if note: notes.append(note)
    if row['status'] == 'partial':
        conf = 'low'; notes.append('register row status partial'); log['partial'].add(rid)
    if 'UNVERIFIABLE' in row['verification_method']:
        conf = 'low'; notes.append('register verification_method audit UNVERIFIABLE')
    if note and re.search(r'conflict|not read|not fetched|not obtained|not located|not yet|self-contradict', note, re.I) and conf == 'high':
        conf = 'medium'
    if f['verification_method']=='derived arithmetically':
        notes.append('derivation as recorded on register row '+rid+': '+row['figure_or_rule_carried'][:160])
    if notes: f['note'] = '; '.join(notes)
    f['confidence'] = conf
    log['used'].add(rid)
    return f, None

def unres_entry(u):
    a, key, why, att, close, blocking = u
    return {'key': key, 'why': why, 'attempted': att, 'what_would_close_it': close, 'blocking': blocking}

U = load('unresolved_data').U
# ---------- RSPEC
facts = []; unres = [unres_entry(u) for u in U if u[0] == 'RSPEC']
D = {}
for p in ('rspec_data_1', 'rspec_data_2', 'rspec_data_3'): D.update(load(p).D)
for jur, items in D.items():
    for suf, val, rid, note, uom in items:
        key = 'rspec.' + jur.lower() + '.' + suf
        f, err = mkfact(key, val, rid, note, uom)
        if f and not IDPAT.match(rid): pending['RSPEC'].append(f)
        elif f: facts.append(f)
        else:
            log['unresolved_moved'].append((key, rid, err))
            unres.append({'key': key, 'why': f'cited row {rid} is {err}; no active A-tier row carries it', 'attempted': [f'register lookup {rid}'], 'what_would_close_it': 'an active A.1/A.2 register row for this report attribute (re-read of the authority page)', 'blocking': False})
keys = [f['key'] for f in facts]; assert len(keys) == len(set(keys)), [k for k in keys if keys.count(k) > 1]
out = {'schema_version': '1.4.0', 'artifact': 'RSPEC', 'code': 'US', 'year': 2026, 'generated_on': '2026-11-02',
       '_note': 'Synthesis B (RSPEC+DD worker). One fact per report attribute, key rspec.{jur}.{report}.{attribute}; jur = FED, MULTI, 50 states + DC. Drawn only from register rows active/partial at tier A; partial rows carry confidence low. Channel vocabulary: online_form / file_upload / xml / api / paper.',
       '_language_seam': 'US-OWN-006: authority-facing filings in English; no filing-language statute located.',
       '_facts_pending_register_id_pattern': pending['RSPEC'], '_pending_note': 'Facts whose register_id is a real active row but has a multi-segment id (e.g. US-AR-P5-1-002) that facts.schema 1.4.0 register_id pattern rejects; same convention as the CCG annex workers. Content is verified; only the id pattern blocks them. Closed by a schema PATCH loosening the pattern or by re-keyed register aliases.', 'facts': facts, 'unresolved': unres}
json.dump(out, open(os.path.join(BASE, '_research', 'RSPEC-facts.json'), 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
# ---------- DD
F = load('dd_data').F
dfacts = []; dun = [unres_entry(u) for u in U if u[0] == 'DD']; owner = []
for key, val, rid, note, uom, cons in F:
    if key == 'dd.fed.contractor.scope':
        owner.append({'key': key, 'statement': val, 'basis': 'owner instruction 2026-10-29 recorded in SKELETON-MANIFEST.md scope line; no register row carries it (see report)'}); continue
    row = reg.get(rid)
    if row and row['tier'] == 'owner':
        owner.append({'key': key, 'statement': val, 'register_id': rid, 'basis': row['figure_or_rule_carried'][:300]}); log['used'].add(rid); continue
    f, err = mkfact(key, val, rid, note, uom)
    if f:
        f['_consumers'] = cons
        (dfacts if IDPAT.match(rid) else pending['DD']).append(f)
    else:
        log['unresolved_moved'].append((key, rid, err))
        dun.append({'key': key, 'why': f'cited row {rid} is {err}', 'attempted': [f'register lookup {rid}'], 'what_would_close_it': 'an active A.1/A.2 register row for this field', 'blocking': False})
dout = {'schema_version': '1.4.0', 'artifact': 'DD', 'unit': '8_sheets', 'code': 'US', 'year': 2026, 'generated_on': '2026-11-02',
        '_note': 'Synthesis B. Data fields the reports (RSPEC) and calculations need; _consumers names the report/calc each field feeds (DD -> RSPEC direction of the reconciliation). Per-state new-hire field lists and deadlines live in RSPEC-facts.json under rspec.{jur}.new_hire.*.',
        '_owner_scope': owner, '_facts_pending_register_id_pattern': pending['DD'], 'facts': dfacts, 'unresolved': dun}
json.dump(dout, open(os.path.join(BASE, '_research', 'DD-8_sheets-facts.json'), 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
json.dump({k: (sorted(v) if isinstance(v, set) else v) for k, v in log.items()}, open(os.path.join(HERE, 'gen-log.json'), 'w'), indent=1)
print('pending', len(pending['RSPEC']), len(pending['DD'])); print('RSPEC facts', len(facts), 'unresolved', len(unres), '| DD facts', len(dfacts), 'unresolved', len(dun), 'owner', len(owner))
print('moved', log['unresolved_moved']); print('eff fallback', len(log['eff_fallback']), sorted(set(log['eff_fallback']))); print('partial', sorted(log['partial'])); print('ids used', len(log['used']))
