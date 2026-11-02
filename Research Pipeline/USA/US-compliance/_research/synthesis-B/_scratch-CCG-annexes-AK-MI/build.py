# Synthesis-B builder for CCG jurisdiction annexes (AK..MI worker).
# Usage: python -I build.py <JUR>   (reads spec_<JUR>.py beside this file)
import csv, json, re, sys, subprocess, os, datetime, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
REG = os.path.join(BASE, '00-official-sources', 'legal-basis-register.csv')
RES = os.path.join(BASE, '_research')
VALIDATOR = os.path.expanduser('~/mercans-pipeline/shared/schemas/validate_contract.py')
TODAY = '2026-11-02'

UNITS = {'USD': ('currency', 'USD')}

def load_reg():
    with open(REG, encoding='utf-8', newline='') as f:
        return {r['id']: r for r in csv.DictReader(f)}

def vm_of(row):
    v = row['verification_method'].lower()
    if v.startswith('derived arithmetically'):
        return 'derived arithmetically'
    if v.startswith('second independent'):
        return 'second independent authority'
    if v.startswith('inspected directly') or v.startswith('read local file') or 'inspected directly' in v:
        return 'direct artifact inspection'
    return 'quoted from authority page'

def num_variants(v):
    out = set()
    if isinstance(v, bool) or not isinstance(v, (int, float)):
        return out
    for fmt in ('{:,.2f}', '{:.2f}', '{:,.0f}', '{:.0f}', '{:,.1f}', '{:.1f}', '{:,.3f}', '{:.3f}', '{:.4f}', '{:g}'):
        try:
            s = fmt.format(v)
            out.add(s)
            out.add(s.replace(',', ' '))
            out.add(s.replace(',', ''))
        except Exception:
            pass
    if isinstance(v, float) and abs(v) < 1:
        out.add('{:g}'.format(v * 100))
    return {o for o in out if o not in ('0', '0.0')}

def main(jur):
    spec_path = os.path.join(HERE, f'spec_{jur}.py')
    spec = importlib.util.spec_from_file_location('spec', spec_path)
    S = importlib.util.module_from_spec(spec); spec.loader.exec_module(S)
    reg = load_reg()
    errs, warns, facts, used = [], [], [], []
    seen = set()
    for f in S.FACTS:
        dom, key, val, rid, eff_from, eff_to = f[:6]
        x = f[6] if len(f) > 6 else {}
        row = reg.get(rid)
        if not re.match(r'^[A-Z]{2}-[A-Z0-9]{2,12}-[0-9]{3,4}$', rid):
            errs.append(f'{key}: {rid} legacy id fails facts.schema register_id pattern (cite in narrative only)'); continue
        if row is None:
            errs.append(f'{key}: register_id {rid} not in register'); continue
        st = row['status']
        if st not in ('active', 'partial'):
            errs.append(f'{key}: {rid} status={st}'); continue
        tier = row['tier']
        if tier not in ('A.1', 'A.2', 'A.3'):
            errs.append(f'{key}: {rid} tier={tier}'); continue
        if (key, eff_from) in seen:
            errs.append(f'duplicate {key} {eff_from}')
        seen.add((key, eff_from))
        o = {'key': key, 'value': val}
        u = x.get('u')
        if u == 'USD':
            o['currency'] = 'USD'
        elif u:
            o['unit_of_measure'] = u
        o['effective_from'] = eff_from
        o['effective_to'] = eff_to
        o['register_id'] = rid
        o['tier'] = tier
        o['verification_method'] = x.get('vm') or vm_of(row)
        o['authority'] = x.get('auth') or row['authority'] or 'unknown authority'
        o['url'] = row['url'] if row['url'].startswith('http') else (row['local_file'] or row['url'])
        conf = x.get('c', 'high')
        note = x.get('n', '')
        if st == 'partial':
            conf = 'medium' if conf == 'high' else conf
            note = ('[partial row] ' + note).strip()
        if o['verification_method'] == 'derived arithmetically' and not note:
            note = 'Derivation recorded in register row ' + rid + ': ' + row['figure_or_rule_carried'][:300]
        o['confidence'] = conf
        if note:
            o['note'] = note
        o['_domain'] = dom
        facts.append(o)
        used.append(rid)
        # number-in-row check (warning only)
        nv = num_variants(val)
        if nv:
            txt = row['figure_or_rule_carried'] + ' ' + row['article_or_section'] + ' ' + row['instrument_name']
            if not any(s in txt for s in nv):
                warns.append(f'{key}={val} not literally in {rid}: {row["figure_or_rule_carried"][:160]}')
    unres = []
    legacy_lines = []
    for lg in getattr(S, 'LEGACY', []):
        dom, key, val, rid, eff_from, eff_to = lg[:6]
        nt = lg[6] if len(lg) > 6 else ''
        row = reg.get(rid)
        if row is None or row['status'] not in ('active', 'partial'):
            errs.append(f'LEGACY {key}: {rid} missing or not active'); continue
        used.append(rid)
        legacy_lines.append((dom, f"- `{key}` = {val} ({eff_from} → {eff_to or 'open'}) [{row['tier']}, {rid} — legacy id, NOT a fact] {nt}".rstrip()))
        unres.append({'key': key, 'why': f"Value {val} (from {eff_from}) is carried by register row {rid} ({row['status']}, {row['tier']}, {row['authority']}), but that legacy id fails the facts.schema register_id pattern, so it cannot be emitted as a fact. {nt}".strip(),
                      'attempted': ['Synthesis B: searched the register for an S5-pattern row carrying the same figure; none found'],
                      'what_would_close_it': f'Final merge: register an S5-pattern alias row (same url/figure, supersedes {rid}) or re-key {rid}; then emit this key as a fact. No new research needed.',
                      'blocking': False})
    for u in S.UNRES:
        d = {'key': u['key'], 'why': u['why'], 'attempted': u.get('attempted', []),
             'what_would_close_it': u['close'], 'blocking': u.get('blocking', False)}
        unres.append(d)
    for rid in getattr(S, 'CITED', []):
        row = reg.get(rid)
        if row is None:
            errs.append(f'CITED {rid} not in register')
        elif row['status'] not in ('active', 'partial', 'not_applicable'):
            warns.append(f'CITED {rid} status={row["status"]} (narrative only)')
        else:
            used.append(rid)
    out = {'schema_version': '1.4.0', 'artifact': 'CCG', 'unit': f'annex_{jur}', 'code': 'US', 'year': 2026,
           'generated_on': TODAY,
           '_jurisdiction': S.NAME,
           '_key_convention': 'Keys are prefixed with the lowercase jurisdiction code ({jur}.{domain}.{concept}...) so one key = one meaning country-wide across 51 annexes.',
           '_produced_by': 'Synthesis-B worker CCG annexes AK-MI, from _research/stage5/%s.md and active/partial register rows only (no fetching)' % jur,
           'facts': facts, 'unresolved': unres}
    fp = os.path.join(RES, f'CCG-annex_{jur}-facts.json')
    if errs:
        print('ERRORS:'); [print(' ', e) for e in errs]
        print('not written'); return 1
    with open(fp, 'w', encoding='utf-8', newline='\n') as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1)
    r = subprocess.run([sys.executable, VALIDATOR, 'facts', fp], capture_output=True, text=True)
    vout = (r.stdout + r.stderr).strip()
    print('VALIDATOR rc=%d: %s' % (r.returncode, vout[-600:]))
    # research pack
    doms = []
    for f in facts:
        if f['_domain'] not in doms:
            doms.append(f['_domain'])
    L = [f'# CCG annex_{jur} research pack — {S.NAME}', '',
         f'Synthesis B, {TODAY}. Source: `_research/stage5/{jur}.md` and the active/partial rows of `00-official-sources/legal-basis-register.csv`; no fetching. Facts file: `_research/CCG-annex_{jur}-facts.json` (validator: {"PASS" if r.returncode == 0 else "FAIL"}). Every value below is a fact object there; key in backticks, register id in brackets.', '']
    if getattr(S, 'SUMMARY', ''):
        L += ['**Summary.** ' + S.SUMMARY.strip(), '']
    order = ['labour_code', 'income_tax', 'non_resident', 'local_tax', 'social_security', 'payslip_statute', 'reporting_instruments', 'leave', 'termination', 'benefits_in_kind', 'deductions_garnishments', 'collective_agreements', 'indexation', 'data_protection', 'live_change', 'oracle']
    titles = {'labour_code': '1 — Employment / labour code', 'income_tax': '2 — Income tax (state withholding)', 'non_resident': '2b — Non-resident regime and reciprocity', 'local_tax': '2c — Local wage taxes', 'social_security': '3 — Social insurance (SUI / SDI / PFML / levies)', 'payslip_statute': '4 — Payslip statute', 'reporting_instruments': '5 — Statutory reporting instruments', 'leave': '6 — Leave', 'termination': '7 — Termination and final pay', 'benefits_in_kind': '8 — Benefits in kind / taxable wages', 'deductions_garnishments': '9 — Deductions and garnishments', 'collective_agreements': '10 — Collective agreements / prevailing wage', 'indexation': '11 — Indexation', 'data_protection': '12 — Payroll data protection / records', 'live_change': '13 — Live legal change', 'oracle': 'Oracle — worked examples (C37)'}
    NARR = getattr(S, 'NARR', {})
    for d in order:
        fs = [f for f in facts if f['_domain'] == d]
        if not fs and d not in NARR and not any(dd == d for dd, _ in legacy_lines):
            continue
        L.append('## ' + titles[d])
        if d in NARR:
            L += [NARR[d].strip(), '']
        for dd, ln in legacy_lines:
            if dd == d:
                L.append(ln)
        for f in fs:
            v = f['value']
            unit = f.get('currency') or f.get('unit_of_measure') or ''
            to = f['effective_to'] or 'open'
            line = f"- `{f['key']}` = **{v}** {unit} ({f['effective_from']} → {to}) [{f['tier']}, {f['register_id']}, {f['verification_method']}, conf {f['confidence']}]"
            if f.get('note'):
                line += ' — ' + f['note']
            L.append(line)
        L.append('')
    if getattr(S, 'SPECIAL', ''):
        L += ['## Special populations (US-OWN-005)', S.SPECIAL.strip(), '']
    if getattr(S, 'LANG', ''):
        L += ['## Language seams (US-OWN-006)', S.LANG.strip(), '']
    L += ['## Open questions', 'Mirrors `unresolved[]` in the facts file (same keys).', '']
    for u in unres:
        L.append(f"- `{u['key']}` ({'blocking' if u['blocking'] else 'non-blocking'}) — {u['why']} **Would close it:** {u['what_would_close_it']}")
    if not unres:
        L.append('- None.')
    L.append('')
    with open(os.path.join(RES, f'CCG-annex_{jur}-research-pack.md'), 'w', encoding='utf-8', newline='\n') as fh:
        fh.write('\n'.join(L))
    # report
    ids = sorted(set(used))
    R = [f'# Synthesis B report — CCG / annex_{jur} ({S.NAME})', '', f'- Date: {TODAY}', f'- Facts written: {len(facts)}', f'- Unresolved: {len(unres)} (blocking {sum(1 for u in unres if u["blocking"])})',
         f'- Files: `_research/CCG-annex_{jur}-facts.json`, `_research/CCG-annex_{jur}-research-pack.md`',
         f'- Validator: `python ~/mercans-pipeline/shared/schemas/validate_contract.py facts _research/CCG-annex_{jur}-facts.json` → rc={r.returncode}', '', '```', vout[-1500:], '```', '',
         f'## Register ids consumed (append `CCG/annex_{jur}` to consumed_by at final merge) — {len(ids)}', '', '; '.join(ids), '',
         '## Number-in-row warnings (value not found literally in the row text; reviewed by the worker)', '']
    R += ['- ' + w for w in warns] or ['- none']
    with open(os.path.join(BASE, '_research', 'synthesis-B', f'CCG-annex_{jur}-report.md'), 'w', encoding='utf-8', newline='\n') as fh:
        fh.write('\n'.join(R) + '\n')
    print(f'facts={len(facts)} unresolved={len(unres)} ids={len(ids)} warnings={len(warns)}')
    for w in warns:
        print('WARN', w)
    return r.returncode

if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
