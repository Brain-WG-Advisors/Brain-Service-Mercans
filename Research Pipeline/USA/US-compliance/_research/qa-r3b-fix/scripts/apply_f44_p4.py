"""Agent 2 - F44 closure (P4 shard merge + browser-pass P4 follow-ups), 2026-11-02.
Local only, no fetch. Writes: legal-basis-register.csv, _research/*-facts.json, _research/*-research-pack.md.
Backups: _research/qa-r3b-fix/_backup2/. Log: _research/qa-r3b-fix/apply-f44-p4-log.json
"""
import csv, io, json, glob, os, re, sys

BASE = sys.argv[1]
TODAY = '2026-11-02'
REG = os.path.join(BASE, '00-official-sources', 'legal-basis-register.csv')
SHARD = os.path.join(BASE, '00-official-sources', '_register-shards', 'S5B-P4.csv')
RES = os.path.join(BASE, '_research')
log = {'register': [], 'facts': [], 'packs': [], 'special': []}

# ---------- register ----------
regraw = open(REG, encoding='utf-8', newline='').read()
rows = list(csv.reader(io.StringIO(regraw)))
hdr, body = rows[0], rows[1:]
H = {h: i for i, h in enumerate(hdr)}
assert len(hdr) == 20
byid = {r[0]: r for r in body}
shard = list(csv.DictReader(open(SHARD, encoding='utf-8', newline='')))
assert len(shard) == 41
succ = {}  # old id -> new id
for s in shard:
    assert s['id'] not in byid
    old = byid[s['supersedes']]
    succ[s['supersedes']] = s['id']
    toks = [t for t in old[H['consumed_by']].split(';') if t]
    for t in s['consumed_by'].split(';'):
        if t and t not in toks:
            toks.append(t)
    s['consumed_by'] = ';'.join(toks)
    prev = (old[H['effective_to']], old[H['status']])
    old[H['effective_to']] = TODAY
    old[H['status']] = 'superseded'
    body.append([s[h] for h in hdr])
    byid[s['id']] = body[-1]
    log['register'].append({'old': old[0], 'new': s['id'], 'old_prev_effective_to_status': prev,
                            'consumed_by_carried': s['consumed_by']})

def add_tok(rid, tok):
    r = byid[rid]
    toks = [t for t in r[H['consumed_by']].split(';') if t]
    if tok not in toks:
        toks.append(tok)
        r[H['consumed_by']] = ';'.join(toks)

# PA-009: decimal quote into verification_method
pa = byid['US-PA-009']
pa_quote = ('F44 2026-11-02 (agent 2): keyed figures ARE in the local copy PA_US-PA-009_r2-curl_2026-11-02.html, '
            'in decimal form (x100 = percent): "The minimum experience-based contribution rate is .014190" (=1.419%); '
            '"The maximum experience-based contribution rate is .103734" (=10.3734%); '
            '"The newly liable non-construction employer contribution rate is .038220" (=3.822%); '
            '"The newly liable construction employer contribution rate is .105924" (=10.5924%); '
            'each "(this includes the 9.2 percent Surcharge ...)"; the r2 "NOT located" note was a percent/decimal matcher miss')
if 'F44 2026-11-02 (agent 2)' not in pa[H['verification_method']]:
    pa[H['verification_method']] += ' | ' + pa_quote
pa[H['verified_on']] = TODAY

# ---------- facts ----------
SPECIAL_NY = 'US-NY-005'  # successor depends on key: DBL -> WCL 209 (NYB5-401)
def successor(rid, key):
    if rid == SPECIAL_NY and key.startswith('ny.dbl.'):
        return 'US-NYB5-401'
    return succ.get(rid)

idpat = re.compile(r'US-[A-Z0-9]+-[0-9]+[A-Z]?(?![0-9A-Za-z])')

def fmt_of(raw):
    for ind in (2, 1, 4):
        d = json.loads(raw)
        for ea in (False, True):
            s = json.dumps(d, indent=ind, ensure_ascii=ea)
            if raw == s: return ind, ea, ''
            if raw == s + '\n': return ind, ea, '\n'
    return 2, False, '\n'

def append_note(f, txt):
    n = f.get('note') or ''
    if txt in n: return
    f['note'] = (n.rstrip() + ' ' if n and n != '-' else '') + txt

MN_NOTE = ('F44 2026-11-02: DERIVED, not quoted; no page carries 91.27. Inputs, all from US-MNS5-010 '
           '(wh-inst-26 p.34 Computer Formula, local pdfs/MN/wh-inst-26_webfetch-20261030.pdf): step 2 periods 26 '
           '(biweekly); step 3 allowance 5,300 per allowance; single chart row 38,010-114,130: add 1,782.09, 6.80% of '
           'excess over 38,010; step 6 divide by periods. 2,000x26=52,000; 52,000-1x5,300=46,700; '
           '1,782.09+(46,700-38,010)x0.068=2,373.01; 2,373.01/26=91.27 (re-run in Python 2026-11-02).')
PA_KEYS = {'pa.sui.employer.rate.min': '.014190', 'pa.sui.employer.rate.max': '.103734',
           'pa.sui.new_employer.rate': '.038220', 'pa.ui.rate.new_employer.construction': '.105924'}

# MN arithmetic check
mn = round((1782.09 + (2000 * 26 - 5300 - 38010) * 0.068) / 26, 2)
assert mn == 91.27, mn

touched = []
for fp in sorted(glob.glob(os.path.join(RES, '*-facts.json'))):
    raw = open(fp, encoding='utf-8').read()
    ind, ea, tail = fmt_of(raw)
    d = json.loads(raw)
    art = d.get('artifact'); unit = d.get('unit')
    tok = f'{art}/{unit}' if unit else art
    changed = False
    for f in d.get('facts', []):
        k = f.get('key', '')
        rid = f.get('register_id')
        new = successor(rid, k) if rid else None
        if new:
            nr = byid[new]
            f['register_id'] = new
            f['tier'] = nr[H['tier']]
            f['url'] = nr[H['url']]
            if rid == SPECIAL_NY:
                f['authority'] = nr[H['authority']]
            add_tok(new, tok)
            log['facts'].append({'file': os.path.basename(fp), 'key': k, 'old': rid, 'new': new})
            changed = True
        # ids cited elsewhere in the fact (notes, _also_stated_by ...)
        for fld in list(f):
            if fld in ('register_id', 'key'): continue
            v = f[fld]
            if isinstance(v, str):
                nv = idpat.sub(lambda m: (successor(m.group(0), k) or m.group(0)), v)
                if nv != v:
                    f[fld] = nv; changed = True
                    log['facts'].append({'file': os.path.basename(fp), 'key': k, 'field': fld, 'text_repoint': True})
            elif isinstance(v, list) and all(isinstance(x, str) for x in v):
                nv = [idpat.sub(lambda m: (successor(m.group(0), k) or m.group(0)), x) for x in v]
                if nv != v:
                    f[fld] = nv; changed = True
        # ---- specials ----
        if k == 'co.famli.total.rate' and f.get('effective_from') == '2027-01-01' and f['register_id'] != 'US-COB5-301':
            old = f['register_id']; nr = byid['US-COB5-301']
            f['register_id'] = 'US-COB5-301'; f['tier'] = nr[H['tier']]; f['url'] = nr[H['url']]
            f['authority'] = nr[H['authority']]
            append_note(f, 'F44 2026-11-02: cites US-COB5-301 (was ' + old + ', same bulletin); local file '
                        'CO_CDLE_FAMLI-business-brief-2026-09-30_2026-11-02.html carries "The 2027 premium rate will be '
                        '0.86% of wages, down from 0.88% in 2026."')
            add_tok('US-COB5-301', tok); changed = True
            log['special'].append({'file': os.path.basename(fp), 'key': k, 'old': old, 'new': 'US-COB5-301'})
        if k == 'ma.wh.supplemental.rate' and f['register_id'] != 'US-MAP51-003':
            old = f['register_id']; nr = byid['US-MAP51-003']
            f['register_id'] = 'US-MAP51-003'; f['tier'] = nr[H['tier']]; f['url'] = nr[H['url']]
            append_note(f, 'F44 2026-11-02: cites Circular M 2026 US-MAP51-003 (was ' + old + '; mass.gov tax-rates '
                        'has no supplemental line). Local pdfs/MA/circularM-2026_wayback-20261018080456.pdf p.13 section G: '
                        '"5. If the result of step 4 is $1,107,750 or less, withhold 5% of the amount determined in step 3."')
            add_tok('US-MAP51-003', tok); changed = True
            log['special'].append({'file': os.path.basename(fp), 'key': k, 'old': old, 'new': 'US-MAP51-003'})
        if k == 'id.sui.new_employer.rate':
            append_note(f, 'F44 2026-11-02: the 2026 rate array labels the 1.000% row "Standard" (US-IDB5-402 transcription: '
                        '"Standard | 1.000% | 0.97000% | 0.00000% | 0.03000%"); "Standard" = new-employer rate per IDOL Tax '
                        'Handbook p.21 [US-IDS5-021]: "All new employers except cost-reimbursement employers begin with the '
                        'same standard unemployment insurance tax rate for at least the first six calendar quarters."')
            add_tok('US-IDS5-021', tok); add_tok(f['register_id'], tok); changed = True
            log['special'].append({'file': os.path.basename(fp), 'key': k, 'register_id': f['register_id'], 'note': 'standard=new employer quote'})
        if k == 'tn.sui.employee.rate':
            f['confidence'] = 'medium'
            append_note(f, 'F44 2026-11-02 (absence fact, partial): no local TN source states a positive "no employee '
                        'contribution" rule. Basis: DLWD UI tax page [US-TNB5-401] frames premiums only as employer '
                        'liability ("Employers who are liable to pay unemployment taxes include the following"), rates are '
                        'assigned per employer reserve ratio [US-TNS5-002/US-TNS5-003], no employee rate or deduction appears '
                        'on any of them. Would close: T.C.A. 50-7-403 text (premiums payable by employers).')
            for r in ('US-TNS5-002', 'US-TNS5-003'): add_tok(r, tok)
            changed = True
            log['special'].append({'file': os.path.basename(fp), 'key': k, 'register_id': f['register_id'], 'note': 'absence reasoning'})
        if k == 'mn.pit.oracle.example_1.withholding':
            f['verification_method'] = 'derived arithmetically'
            append_note(f, MN_NOTE); changed = True
            log['special'].append({'file': os.path.basename(fp), 'key': k, 'register_id': f['register_id'], 'note': 'derived'})
        if k in PA_KEYS and f.get('register_id') == 'US-PA-009':
            append_note(f, f'F44 2026-11-02: local copy PA_US-PA-009_r2-curl_2026-11-02.html states the rate in decimal '
                           f'form "{PA_KEYS[k]}" (x100 = {f["value"]}%); decimal quote recorded in the register row '
                           f'verification_method.')
            changed = True
            log['special'].append({'file': os.path.basename(fp), 'key': k, 'note': 'PA decimal quote'})
        if k.startswith('ny.dbl.') and f.get('register_id') == 'US-NYB5-401':
            append_note(f, 'F44 2026-11-02: WCL 209(3)(a) local copy NY_WCL-209_nysenate_browser_2026-11-02.txt: '
                           '"one-half of one per centum of the employee\'s wages ... but not in excess of sixty cents per week".')
    if changed:
        out = json.dumps(d, indent=ind, ensure_ascii=ea) + tail
        open(fp, 'w', encoding='utf-8', newline='').write(out)
        touched.append(os.path.basename(fp))

# ---------- packs ----------
for fp in sorted(glob.glob(os.path.join(RES, '*-research-pack.md'))):
    txt = open(fp, encoding='utf-8', newline='').read()
    lines = txt.split('\n'); n = 0
    for i, ln in enumerate(lines):
        def rep(m):
            o = m.group(0)
            if o == SPECIAL_NY:
                return 'US-NYB5-401' if re.search(r'(?i)dbl|disability', ln) else 'US-NYB5-402'
            return succ.get(o, o)
        nl = idpat.sub(rep, ln)
        if nl != ln:
            n += 1; lines[i] = nl
    if n:
        open(fp, 'w', encoding='utf-8', newline='').write('\n'.join(lines))
        log['packs'].append({'file': os.path.basename(fp), 'lines_changed': n})

# ---------- write register ----------
o = io.StringIO()
csv.writer(o, lineterminator='\r\n' if '\r\n' in regraw else '\n').writerows([hdr] + body)
open(REG, 'w', encoding='utf-8', newline='').write(o.getvalue())
log['facts_files_touched'] = touched
json.dump(log, open(os.path.join(RES, 'qa-r3b-fix', 'apply-f44-p4-log.json'), 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
print('register rows', len(body), 'facts touched', len(touched), 'repoints', sum(1 for x in log['facts'] if 'new' in x),
      'special', len(log['special']), 'packs', log['packs'])
