import csv, json, re, sys
BASE = r"C:/Users/instituto/Documents/brain-service/Research Pipeline/USA/US-compliance"
R = {x['id']: x for x in csv.DictReader(open(BASE + '/00-official-sources/legal-basis-register.csv', encoding='utf-8'))}
PAT = re.compile(r'^[A-Z]{2}-[A-Z0-9]{2,12}-[0-9]{3,4}$')
OK_STATUS = {'active', 'partial'}
OK_TIER = {'A.1', 'A.2', 'A.3'}


def vm(s):
    s0 = (s or '').lower()
    if s0.startswith('derived'):
        return 'derived arithmetically'
    if 'second independent' in s0:
        return 'second independent authority'
    if any(k in s0 for k in ('inspected directly', 'read local', 'pymupdf', 'pdftotext', 'saved pdf', 'extracted', 'local file')):
        return 'direct artifact inspection'
    return 'quoted from authority page'


def build(spec, artifact, unit):
    facts, blocked, unresolved, consumed = [], [], [], set()
    seen = set()
    for s in spec:
        key, value, rid = s['key'], s['value'], s['rid']
        assert key not in seen, key
        seen.add(key)
        x = R.get(rid)
        if x is None:
            unresolved.append({'key': key, 'why': f'register row {rid} cited by the Stage-5 findings does not exist in legal-basis-register.csv',
                               'what_would_close_it': s.get('close', 'merge worker to register the row or re-point the citation'), 'blocking': False})
            continue
        if x['status'] not in OK_STATUS or x['tier'] not in OK_TIER:
            unresolved.append({'key': key, 'why': f"only source is {rid} (status {x['status']}, tier {x['tier']}); not usable for a fact under the brief",
                               'attempted': [x['url']] if x['url'] else [],
                               'what_would_close_it': s.get('close', f"an active A.1/A.2 row replacing {rid}: re-read {x['url'] or 'the official form/page'} on the official host"),
                               'blocking': s.get('blocking', False)})
            continue
        ef = x['effective_from'] or x['publication_date']
        f = {'key': key, 'value': value}
        if 'uom' in s: f['unit_of_measure'] = s['uom']
        if 'cur' in s: f['currency'] = s['cur']
        if ef and re.match(r'^\d{4}-\d{2}-\d{2}$', ef):
            f['effective_from'] = ef
        else:
            f['effective_from'] = '2026-01-01'
            f['_effective_from_basis'] = f"register row {rid} carries no full effective_from ('{x['effective_from']}'); 2026-01-01 = rule read as in force for the build year on {x['verified_on'] or x['retrieved_on']}"
        f['effective_to'] = s.get('to', x['effective_to'] or None) or None
        f['register_id'] = rid
        f['tier'] = x['tier']
        f['verification_method'] = vm(x['verification_method'])
        if f['verification_method'] == 'derived arithmetically' and 'note' not in s:
            s['note'] = 'derivation per register row ' + rid + ': ' + x['figure_or_rule_carried'][:200]
        f['authority'] = x['authority'] or 'see register row'
        f['url'] = x['url'] or x['local_file'] or ('register:' + rid)
        conf = s.get('conf', 'high')
        if x['status'] == 'partial':
            conf = 'low'
        f['confidence'] = conf
        note = s.get('note', '')
        if x['status'] == 'partial':
            note = ('PARTIAL register row: ' + note).strip()
        if note: f['note'] = note
        f['_register_verification_method'] = x['verification_method']
        if PAT.match(rid):
            facts.append(f)
            consumed.add(rid)
        else:
            blocked.append(f)
            consumed.add(rid)
    return facts, blocked, unresolved, consumed


def write(path, artifact, unit, facts, blocked, unresolved, extra):
    doc = {'schema_version': '1.4.0', 'artifact': artifact, 'unit': unit, 'code': 'US', 'year': 2026,
           'generated_on': '2026-11-02', 'facts': facts, 'unresolved': unresolved}
    doc.update(extra)
    if blocked:
        doc['_facts_blocked_by_register_id_pattern'] = {
            '_why': 'facts.schema.json 1.4.0 register_id pattern ^[A-Z]{2}-[A-Z0-9]{2,12}-[0-9]{3,4}$ rejects the multi-segment ids this build issued (e.g. US-FEDP51-002, US-MDP51-005). The rows are active and the facts are sound; they are parked here, outside the validated array, until the orchestrator either loosens the pattern (PATCH bump: looser pattern) or the merge worker issues pattern-compliant alias ids. Builders may read them; QA P2 must treat them as bound to the named register row.',
            'facts': blocked}
    json.dump(doc, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
