"""QA r1b (agent 2): register work, items 1 and 2.
Usage: python -I r1b_register.py <BASE>
 1. merge shard S5B-P3 (22 rows) with id translation and supersessions;
 2. apply effective_from proposals (high/medium only), annotate low/undated rows,
    fix local_file prefixes and the named row corrections.
Every change is logged to _research/qa-r1-fix/r1b_register.log. Backup: _research/qa-r1-fix/_backup2/."""
import csv, os, re, sys, collections

BASE = sys.argv[1]
OS = os.path.join(BASE, '00-official-sources')
REG = os.path.join(OS, 'legal-basis-register.csv')
SHARD = os.path.join(OS, '_register-shards', 'S5B-P3.csv')
RMAP = os.path.join(BASE, '_research', 'stage5', 'ID-RENAME-MAP.csv')
FIX = os.path.join(BASE, '_research', 'qa-r1-fix')
LOG = os.path.join(FIX, 'r1b_register.log')
TODAY = '2026-11-02'
NOTE_UNDATED = 'effective_from not stated in the instrument; in force as at retrieved_on (QA r1 note)'

log = []
def L(*a):
    log.append(' | '.join(str(x) for x in a))

with open(REG, encoding='utf-8', newline='') as fh:
    rd = csv.DictReader(fh)
    COLS = rd.fieldnames
    rows = list(rd)
assert len(COLS) == 20, COLS
idx = {r['id']: r for r in rows}
rename = {r['old_id']: r['new_id'] for r in csv.DictReader(open(RMAP, encoding='utf-8'))}

def app(r, col, text, sep=' | '):
    r[col] = (r[col] + sep + text) if r[col].strip() else text

# ------------------------------------------------------------------ item 1: shard merge
ID_RX = re.compile(r'^US-[A-Z0-9]{2,12}-[0-9]{3,4}$')
TIERS = {'A.1', 'A.2', 'A.3', 'B', 'C', 'owner'}
STAT = {'active', 'superseded', 'MANUAL', 'gated', 'not_applicable', 'partial', 'historical', 'provisional'}
DATE = re.compile(r'^$|^\d{4}(-\d{2}(-\d{2})?)?$')
PATH_RX = re.compile(r'(00-official-sources/[^\s;()]+\.(?:pdf|html?|txt|csv|xlsx|zip|xml|json))')
shard = list(csv.DictReader(open(SHARD, encoding='utf-8', newline='')))
assert len(shard) == 22, len(shard)
errors = []
for r in shard:
    assert list(r.keys()) == COLS, 'shard header differs'
    if r['id'] in rename:
        L('SHARD id translated', r['id'], rename[r['id']]); r['id'] = rename[r['id']]
    if r['supersedes'] in rename:
        L('SHARD supersedes translated', r['id'], r['supersedes'], rename[r['supersedes']]); r['supersedes'] = rename[r['supersedes']]
    if not ID_RX.match(r['id']): errors.append((r['id'], 'id pattern'))
    if r['id'] in idx: errors.append((r['id'], 'id collision'))
    if r['tier'] not in TIERS: errors.append((r['id'], 'tier'))
    if r['status'] not in STAT: errors.append((r['id'], 'status'))
    for c in ('publication_date', 'effective_from', 'effective_to', 'retrieved_on', 'verified_on'):
        if not DATE.match(r[c]): errors.append((r['id'], c, r[c]))
    if r['supersedes'] and r['supersedes'] not in idx: errors.append((r['id'], 'supersedes target missing', r['supersedes']))
    # local_file: paths only; annotations (md5, 'verbatim excerpt', 'pp.') move to verification_method
    paths = PATH_RX.findall(r['local_file'])
    for p in paths:
        if not os.path.exists(os.path.join(BASE, p)): errors.append((r['id'], 'local file missing', p))
    rest = r['local_file']
    for p in paths: rest = rest.replace(p, '')
    rest = re.sub(r'^[\s;]+|[\s;]+$', '', re.sub(r'\s*;\s*', '; ', rest)).strip()
    if rest:
        app(r, 'verification_method', 'local copy notes: ' + rest)
    r['local_file'] = '; '.join(paths)
    L('SHARD row appended', r['id'], r['status'], r['tier'], r['local_file'])
if errors:
    print('SHARD VALIDATION ERRORS', errors); sys.exit(1)
rows.extend(shard)
for r in shard: idx[r['id']] = r

# supersessions declared by the shard
ny = idx['US-NY-011']
app(ny, 'figure_or_rule_carried', '[QA r1b 2026-11-02: NYC 4.25% and Yonkers 1.95975% / 0.50% supplemental rates re-registered from the authority host on US-NYB5-301 (NYS-50-T-NYC 1/26) and US-NYB5-302 (NYS-50-T-Y 1/26), which list this row in supersedes; status stays superseded]', ' ')
L('SUPERSEDE note', 'US-NY-011', 'already superseded (by US-NYP52-001); successors US-NYB5-301/-302 recorded in figure_or_rule_carried')
co = idx['US-COS5-011']
app(co, 'figure_or_rule_carried', '[QA r1b 2026-11-02: City of Boulder 2026/2027 (16.82 / 18.17) and unincorporated Boulder County 2026/2027 (16.82 / 17.43) now on A.2 rows US-COB5-303 and US-COB5-302 (partial supersession, Boulder localities only); this row stays MANUAL for Edgewater 2026 and Denver 2027]', ' ')
L('SUPERSEDE partial', 'US-COS5-011', 'Boulder localities -> US-COB5-302/-303; row stays MANUAL (Edgewater, Denver 2027)')
de = idx['US-DES5-008']
old = de['figure_or_rule_carried']
de['figure_or_rule_carried'] = old.replace('federal W-4 accepted;', 'federal W-4 accepted [CORRECTED 2026-11-02, QA r1b: superseded on this point by US-DEB5-301 - a 2020-or-later federal W-4 may NOT be accepted for Delaware withholding; the employee files the Delaware W-4; a federal W-4 completed before 2020 may still be relied on];')
assert de['figure_or_rule_carried'] != old
idx['US-DEB5-301']['supersedes'] = 'US-DES5-008 (certificate claim only)'
L('SUPERSEDE partial', 'US-DES5-008', "claim 'federal W-4 accepted' corrected; US-DEB5-301.supersedes = 'US-DES5-008 (certificate claim only)'; row stays active for its other claims (registration, W-2, EFW2, penalties)")
d6 = idx['US-DES5-006']
old = d6['figure_or_rule_carried']
d6['figure_or_rule_carried'] = old.replace('Certificate: federal W-4 (text still says', 'Certificate: federal W-4 [CORRECTED 2026-11-02, QA r1b: per US-DEB5-301 a 2020-or-later federal W-4 may NOT be accepted for Delaware withholding; Delaware W-4 required] (text still says')
assert d6['figure_or_rule_carried'] != old
L('CORRECT claim', 'US-DES5-006', 'same certificate contradiction as US-DES5-008; corrected in text, row stays active (computation table unaffected)')

# ------------------------------------------------------------------ item 2a: effective_from proposals
counts = collections.Counter()
for fn in ('effective-from-AK-IN.csv', 'effective-from-KS-NV.csv', 'effective-from-NY-WY.csv'):
    for p in csv.DictReader(open(os.path.join(FIX, fn), encoding='utf-8')):
        r = idx[p['id']]
        conf = (p['confidence'] or '').split(':')[0].strip().lower()
        if r['effective_from']:
            L('EFF skip (already filled)', p['id'], r['effective_from']); counts['skip'] += 1; continue
        if conf in ('high', 'medium') and p['effective_from']:
            assert re.match(r'^\d{4}-\d{2}-\d{2}$', p['effective_from'])
            r['effective_from'] = p['effective_from']
            L('EFF set', fn, p['id'], p['effective_from'], conf, (p['evidence_location'] or '')[:120])
            counts['set_' + conf] += 1
        else:
            if NOTE_UNDATED not in r['verification_method']:
                app(r, 'verification_method', NOTE_UNDATED)
            L('EFF left empty + note', fn, p['id'], conf or 'undated', 'proposed=' + (p['effective_from'] or '-'))
            counts['note_' + (conf or 'undated')] += 1

# ------------------------------------------------------------------ item 2b: local_file fixes
named = ['US-SCR3-009', 'US-SDP51-003', 'US-FEDR3-007', 'US-MOR3-001', 'US-MSP10-001', 'US-NHP8-001']
for r in rows:
    lf = r['local_file'].strip()
    if not lf:
        continue
    parts = [x.strip() for x in lf.split(';') if x.strip()]
    new, changed, missing = [], False, []
    for x in parts:
        if x.startswith('00-official-sources/') or x.startswith('frentes/'):
            new.append(x)
            if x.startswith('00-official-sources/') and not os.path.exists(os.path.join(BASE, x)):
                missing.append(x)
            continue
        if os.path.exists(os.path.join(OS, x)):
            new.append('00-official-sources/' + x); changed = True
        else:
            new.append(x); missing.append(x)
    if changed:
        L('LOCAL_FILE prefix', r['id'], lf, '->', '; '.join(new)); counts['prefix_fixed'] += 1
        r['local_file'] = '; '.join(new)
    if missing:
        L('LOCAL_FILE missing on disk (unchanged)', r['id'], ';'.join(missing)); counts['missing'] += 1
for i in named:
    assert idx[i]['local_file'].startswith('00-official-sources/'), i
# two-file rows named by QA: verify both files exist
for i in ['US-AKS5-014', 'US-CAS5-022', 'US-DES5-008', 'US-DES5-018', 'US-GAP51-002']:
    fs = [x.strip() for x in idx[i]['local_file'].split(';')]
    ex = [os.path.exists(os.path.join(BASE, x)) for x in fs]
    L('TWO-FILE check', i, list(zip(fs, ex)))
    assert all(ex), i

# CTS5-027: 31-13a sits in ch. 557, 31-66 in ch. 558
c = idx['US-CTS5-027']
c['local_file'] = '00-official-sources/pdfs/CT/cgs-ch557_wayback-20261020184249.html; 00-official-sources/ccg-sources/CT/cgs-chap558_wayback_2026-11-02.html'
c['url'] = 'https://www.cga.ct.gov/current/pub/chap_557.htm'
app(c, 'verification_method', "QA r1b 2026-11-02: local_file and url corrected - Sec. 31-13a is in the ch. 557 file (md5 722d94fe45a5b4e90d74bd0af6261ace, heading 'Employer to furnish record of hours worked, wages earned and deductions' found); Sec. 31-66 stays in the ch. 558 file (https://www.cga.ct.gov/current/pub/chap_558.htm)")
L('FIX', 'US-CTS5-027', 'local_file -> ch.557 + ch.558 files; url -> chap_557.htm')
a = idx['US-ALR3-001']
a['instrument_name'] = "Alabama UC Employer Handbook (2020 edition per its cover; the official file name says 'rev_2021')"
app(a, 'verification_method', "QA r1b 2026-11-02: name corrected - the cover reads '2020 EMPLOYER HANDBOOK'; PDF created 2022-05-31 (metadata); publication_date 2021-01-01 rests only on the URL file name")
L('FIX', 'US-ALR3-001', 'instrument_name rev. 2021 -> 2020 edition per cover')

# ------------------------------------------------------------------ write
ids = [r['id'] for r in rows]
assert len(ids) == len(set(ids)), 'duplicate ids'
assert all(len(r) == 20 for r in rows)
with open(REG, 'w', encoding='utf-8', newline='') as fh:
    w = csv.DictWriter(fh, fieldnames=COLS, lineterminator='\n')
    w.writeheader(); w.writerows(rows)
L('WRITE', REG, len(rows), 'rows', dict(counts))
open(LOG, 'w', encoding='utf-8').write('\n'.join(log) + '\n')
print(len(rows), dict(counts))
