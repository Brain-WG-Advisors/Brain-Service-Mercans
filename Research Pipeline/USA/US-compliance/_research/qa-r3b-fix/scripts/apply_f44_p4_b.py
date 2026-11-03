"""Agent 2 F44 closure, pass b (2026-11-02): re-point the 41 P4-superseded ids wherever they still appear in
facts files outside facts[] (_history, unresolved, key->source maps), and close the two FED 2027 OASDI
re-verification items now answered by US-FEDB5-401's local copy. Preserves CRLF/LF per file."""
import csv, glob, json, os, re, sys
BASE = sys.argv[1]; RES = os.path.join(BASE, '_research')
REG = os.path.join(BASE, '00-official-sources', 'legal-basis-register.csv')
shard = list(csv.DictReader(open(os.path.join(BASE, '00-official-sources', '_register-shards', 'S5B-P4.csv'), encoding='utf-8')))
succ = {s['supersedes']: s['id'] for s in shard}
idpat = re.compile(r'US-[A-Z0-9]+-[0-9]+[A-Z]?(?![0-9A-Za-z])')
log = []

def walk(o, key=''):
    if isinstance(o, dict):
        k = o.get('key', key) if isinstance(o.get('key'), str) else key
        for f in list(o):
            o[f] = walk(o[f], k)
        return o
    if isinstance(o, list):
        return [walk(x, key) for x in o]
    if isinstance(o, str):
        def rep(m):
            i = m.group(0)
            if i == 'US-NY-005':
                return 'US-NYB5-401' if key.startswith('ny.dbl.') else 'US-NYB5-402'
            return succ.get(i, i)
        return idpat.sub(rep, o)
    return o

FED_Q = 'For earnings in 2027, this base is $192,300.'
FED_NOTE = ('F44 2026-11-02: verified on the P4 browser copy of SSA cbb.html (US-FEDB5-401, '
            'FED/FED_SSA_cbb_browser_2026-11-02.txt l.4): "' + FED_Q + '"; table row "2027 192,300".')
lf = open(os.path.join(BASE, '00-official-sources', 'ccg-sources', 'FED', 'FED_SSA_cbb_browser_2026-11-02.txt'), encoding='utf-8').read()
assert FED_Q in lf and '2027 192,300' in lf

for fp in sorted(glob.glob(os.path.join(RES, '*-facts.json'))):
    b = open(fp, 'rb').read(); crlf = b.count(b'\r\n') == b.count(b'\n') and b'\n' in b
    raw = b.decode('utf-8').replace('\r\n', '\n')
    d = json.loads(raw)
    ind = 1 if raw.startswith('{\n "') else 2
    before = json.dumps(d, sort_keys=True)
    d = walk(d)
    name = os.path.basename(fp)
    if name in ('CCG-annex_FED-facts.json', 'WTC-global_baseline-facts.json'):
        for x in d['facts']:
            if x['key'] == 'fed.fica.oasdi.wage_base' and x.get('effective_from') == '2027-01-01' and FED_NOTE not in x.get('note', ''):
                x['note'] = x.get('note', '') + ' ' + FED_NOTE
                x['confidence'] = 'high'
                log.append({'file': name, 'key': x['key'], 'action': 'note+confidence high'})
        keep = []
        for u in d.get('unresolved', []):
            if u.get('key') in ('fed.fica.oasdi.wage_base.next_year_reverification', 'fed.fica.oasdi.wage_base.2027_reverify'):
                u['_closed'] = '2026-11-02 agent 2 F44: ' + FED_NOTE
                d.setdefault('_history', []).append({'closed_unresolved': u})
                log.append({'file': name, 'key': u['key'], 'action': 'unresolved closed -> _history'})
            else:
                keep.append(u)
        d['unresolved'] = keep
    if json.dumps(d, sort_keys=True) != before:
        s = json.dumps(d, indent=ind, ensure_ascii=False) + '\n'
        if not raw.endswith('\n'): s = s[:-1]
        if crlf: s = s.replace('\n', '\r\n')
        open(fp, 'wb').write(s.encode('utf-8'))
        log.append({'file': name, 'action': 'rewritten'})

# packs: FED closure wording
def fix(f, old, new):
    p = os.path.join(RES, f); t = open(p, 'rb').read().decode('utf-8')
    if old in t:
        open(p, 'wb').write(t.replace(old, new).encode('utf-8')); log.append({'pack': f, 'replaced': old[:60]})
fix('CCG-annex_FED-research-pack.md', 'is an SSA-published value carried with medium confidence because re-verification on 2026-11-02 was blocked (ssa.gov 403).',
    'is an SSA-published value, verified 2026-11-02 on the browser-pass copy of SSA cbb.html [US-FEDB5-401]: "For earnings in 2027, this base is $192,300."')
fix('CCG-annex_FED-research-pack.md', 'quoted from authority page, conf medium] — SSA published 2027 figure', 'quoted from authority page, conf high] — SSA published 2027 figure')
fix('WTC-research-pack.md', '| US-FEDB5-401 (A.2) | medium |', '| US-FEDB5-401 (A.2) | high |')
fix('CCG-research-pack.md', '(SSA published; re-verification blocked, medium confidence)', '(SSA published; verified 2026-11-02 on the SSA cbb.html browser copy)')
for f, k in (('CCG-annex_FED-research-pack.md', 'fed.fica.oasdi.wage_base.next_year_reverification'), ('WTC-research-pack.md', 'fed.fica.oasdi.wage_base.2027_reverify')):
    p = os.path.join(RES, f); t = open(p, 'rb').read().decode('utf-8')
    nl = '\r\n' if '\r\n' in t else '\n'
    lines = t.split(nl)
    for i, ln in enumerate(lines):
        if ln.startswith('- `' + k + '`'):
            lines[i] = '- ~~`' + k + '`~~ CLOSED 2026-11-02 (agent 2 F44): ' + FED_NOTE
            log.append({'pack': f, 'closed': k})
    open(p, 'wb').write(nl.join(lines).encode('utf-8'))
json.dump(log, open(os.path.join(RES, 'qa-r3b-fix', 'apply-f44-p4-b-log.json'), 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
print(json.dumps(log, ensure_ascii=False)[:2500])
