"""Synthesis-B generator for CCG jurisdiction annexes (worker MN-WY).
Usage: python -I gen.py JUR [JUR ...]
Reads specs/JUR.txt, the register and _research/stage5/JUR.md; writes
_research/CCG-annex_JUR-facts.json, _research/CCG-annex_JUR-research-pack.md,
_research/synthesis-B/CCG-annex_JUR-report.md. Fails loudly on any fact whose
register row is not active/partial.
Spec lines:  F|key|value|unit|from|to|rid|conf|note
             U|key|why|what_would_close_it|blocking(y/n)
             T|text   (synthesis decision / trap carried into the pack)
"""
import csv, json, re, sys, subprocess, datetime, os

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
REG = os.path.join(BASE, '00-official-sources', 'legal-basis-register.csv')
SPECS = os.path.join(os.path.dirname(__file__), 'specs')
VALIDATOR = os.path.expanduser('~/mercans-pipeline/shared/schemas/validate_contract.py')
TODAY = '2026-11-02'
ISO = re.compile(r'^\d{4}-\d{2}-\d{2}$')
NAMES = dict(MN='Minnesota', MO='Missouri', MS='Mississippi', MT='Montana', NC='North Carolina',
             ND='North Dakota', NE='Nebraska', NH='New Hampshire', NJ='New Jersey', NM='New Mexico',
             NV='Nevada', NY='New York', OH='Ohio', OK='Oklahoma', OR='Oregon', PA='Pennsylvania',
             RI='Rhode Island', SC='South Carolina', SD='South Dakota', TN='Tennessee', TX='Texas',
             UT='Utah', VA='Virginia', VT='Vermont', WA='Washington', WI='Wisconsin',
             WV='West Virginia', WY='Wyoming')

KEYMAP = {  # align core concepts with the AK-MI annex worker's namespace (country-wide consistency)
 'labour.minwage.state.hourly':'minwage.hourly','labour.tip_credit.cash_wage.hourly':'minwage.tipped.cash_wage',
 'labour.tip_credit.allowed':'minwage.tip_credit.allowed','labour.minwage.indexation':'minwage.indexation',
 'labour.overtime.weekly_threshold_hours':'overtime.weekly_threshold_hours','labour.overtime.daily_threshold_hours':'overtime.daily_threshold_hours',
 'labour.overtime.multiplier':'overtime.premium.multiplier','labour.pay_frequency':'pay_frequency.rule','labour.payment_method':'payment.method',
 'labour.exempt_salary.weekly':'exempt.salary.weekly_min','ui.wage_base.annual':'sui.wage_base','ui.rate.new_employer':'sui.new_employer.rate',
 'ui.employee.rate':'sui.employee.rate','ui.rate.experience_max':'sui.employer.rate.max','ui.rate.min':'sui.employer.rate.min',
 'report.new_hire.days':'newhire.report_days','pit.method':'wh.method','pit.supplemental.flat_rate':'wh.supplemental.rate',
 'pit.local.exists':'local_wage_tax.exists','pit.state_wage_tax.exists':'pit.exists','pit.reciprocity.states':'reciprocity.states',
 'garn.consumer.max_rate':'garn.creditor.max_percent','records.payroll.retention_years':'records.retention_years',
 'leave.paid_sick.payout_at_separation':'leave.sick.payout_on_separation','leave.paid_sick.statutory':'leave.sick.state_statute.exists',
 'payslip.content':'payslip.items','pit.certificate':'wh.certificate','pit.certificate.default':'wh.certificate',
 'term.final_pay':'final_pay.rule','term.final_pay.discharge':'final_pay.discharge','sdi.exists':'sdi_pfml.exists',
 'labour.minwage.state.hourly.next_year':'minwage.hourly.next_year','ui.wage_base.next_year':'sui.wage_base.next_year',
 'ui.wage_base.other_state_credit':'sui.wage_base.other_state_credit','ui.wages.401k_included':'sui.wages.401k_included',
 'ui.wages.section125_included':'sui.wages.section125_included','labour.minwage.local.preempted':'local_mandates.preempted'}
KEYMAP_EXCEPT = {('MN','sdi.exists')}  # MN has PFML: keep the narrower meaning


def mapkey(jur, k):
    k = k.strip()
    if (jur, k) in KEYMAP_EXCEPT:
        return k
    return KEYMAP.get(k, k)


reg = {r['id']: r for r in csv.DictReader(open(REG, encoding='utf-8'))}


def vmethod(m):
    m = (m or '').lower()
    if 'derived' in m:
        return 'derived arithmetically'
    if 'second independent' in m:
        return 'second independent authority'
    if any(k in m for k in ('pdf', 'pymupdf', 'xlsx', 'workbook', 'xsd', 'extracted')):
        return 'direct artifact inspection'
    return 'quoted from authority page'


WEAK = ('snippet', 'not inspected', 'summarizer', 'unverifiable', 'search-listing', 'search listing')


def parse_value(v):
    v = v.strip()
    if v in ('true', 'false'):
        return v == 'true'
    if re.fullmatch(r'-?\d+(\.\d+)?', v):
        return float(v) if '.' in v else int(v)
    return v


def build(jur):
    lines = open(os.path.join(SPECS, jur + '.txt'), encoding='utf-8').read().splitlines()
    facts, unres, traps, errors, used = [], [], [], [], []
    seen = set()
    for ln in lines:
        if not ln.strip() or ln.startswith('#'):
            continue
        p = ln.split('|')
        if p[0] == 'F':
            p += [''] * (9 - len(p))
            _, key, val, unit, frm, to, rid, conf, note = p[:9]
            key = jur.lower() + '.' + mapkey(jur, key)
            if (key, frm.strip()) in seen:
                errors.append('duplicate key ' + key)
            seen.add((key, frm.strip()))
            row = reg.get(rid.strip())
            if row is None:
                errors.append(f'{key}: register id {rid} not found')
                continue
            if row['status'] not in ('active', 'partial'):
                errors.append(f'{key}: {rid} status={row["status"]}')
                continue
            if row['tier'] == 'B':
                errors.append(f'{key}: {rid} tier B')
                continue
            f = {'key': key, 'value': parse_value(val)}
            unit = unit.strip()
            if unit in ('USD',):
                f['currency'] = 'USD'
            elif unit == 'pct':
                f['unit_of_measure'] = 'percent'
            elif unit and unit != '-':
                f['unit_of_measure'] = unit
            basis = None
            frm = frm.strip()
            if not frm or frm == '-':
                rf = row['effective_from'].strip()
                if ISO.match(rf):
                    frm = rf
                else:
                    frm = '2026-01-01'
                    basis = 'build-year default: in force on 2026-01-01 per the stage-5 reading; register row carries no ISO effective_from'
            f['effective_from'] = frm
            to = to.strip()
            if to == 'null':
                to = None
            elif not to or to == '-':
                rt = row['effective_to'].strip()
                to = rt if ISO.match(rt) else None
            if to and to < frm:
                errors.append(f'{key}: effective_to {to} before effective_from {frm}')
            f['effective_to'] = to
            f['register_id'] = rid.strip()
            f['tier'] = row['tier']
            vm = vmethod(row['verification_method'])
            conf = conf.strip() or 'high'
            if conf == '-':
                conf = 'high'
            notes = []
            if note.strip():
                notes.append(note.strip())
            if 'derived' in conf:  # spec marker 'derived' => fact itself derived
                conf = 'high'
                vm = 'derived arithmetically'
            if row['status'] == 'partial':
                if conf == 'high':
                    conf = 'medium'
                notes.append('register row is PARTIAL - carry the partial flag')
            if any(w in row['verification_method'].lower() for w in WEAK):
                conf = 'low'
                notes.append('register row verification is weak: ' + row['verification_method'][:80])
            if vm == 'derived arithmetically' and not notes:
                notes.append('derivation recorded in the register row ' + rid.strip() + ' and in the stage-5 findings')
            f['verification_method'] = vm
            f['authority'] = row['authority'] or 'unknown authority'
            url = row['url'].strip()
            if not url and row['local_file'].strip():
                url = row['local_file'].strip()
            f['url'] = url or 'see register row ' + rid.strip()
            f['confidence'] = conf
            if notes:
                f['note'] = '; '.join(notes)
            if basis:
                f['_effective_from_basis'] = basis
            facts.append(f)
            used.append(rid.strip())
        elif p[0] == 'U':
            p += [''] * (5 - len(p))
            _, key, why, close, blk = p[:5]
            key = jur.lower() + '.' + mapkey(jur, key)
            u = {'key': key, 'why': why.strip(), 'attempted': ['_research/stage5/' + jur + '.md open questions / ACCESS-GAPS.md (stage-5 worker, 2026-11-02)'],
                 'what_would_close_it': close.strip(), 'blocking': blk.strip() == 'y'}
            unres.append(u)
        elif p[0] == 'T':
            traps.append('|'.join(p[1:]).strip())
        else:
            errors.append('bad line: ' + ln[:60])
    if errors:
        print('\n'.join(errors))
        sys.exit(1)
    RID = re.compile(r'^[A-Z]{2}-[A-Z0-9]{2,12}-[0-9]{3,4}$')
    pending = [f for f in facts if not RID.match(f['register_id'])]
    facts = [f for f in facts if RID.match(f['register_id'])]
    if pending:
        bad = sorted(set(f['register_id'] for f in pending))
        unres.insert(0, {'key': jur.lower() + '.meta.register_id_pattern',
                         'why': f'{len(pending)} facts rest on active register rows whose ids ({", ".join(bad)}) do not match the facts-schema register_id pattern ^[A-Z]{{2}}-[A-Z0-9]{{2,12}}-[0-9]{{3,4}}$ (multi-hyphen legacy ids). They are carried in full in _facts_pending_register_id_pattern and are NOT yet consumable facts.',
                         'attempted': ['no conforming duplicate row exists for these figures in the register (checked by the MN-WY worker)'],
                         'what_would_close_it': 'Orchestrator decision: a PATCH of facts.schema.json loosening the register_id pattern (e.g. ^[A-Z]{2}-[A-Z0-9-]{2,16}-[0-9]{3,4}$), or register alias ids; then run _research/synthesis-B/_work-MN-WY/promote.py to move the pending facts into facts[].',
                         'blocking': True})
    doc = {'schema_version': '1.4.0', 'artifact': 'CCG', 'unit': 'annex_' + jur, 'code': 'US', 'year': 2026,
           'generated_on': TODAY,
           '_note': f'CCG jurisdiction annex {jur} ({NAMES[jur]}). Synthesis-B worker MN-WY. Key namespace: {jur.lower()}.<domain>.<concept>[.<qualifier>].<attribute>; rates in percent with unit_of_measure=percent; money in USD. Built only from active/partial rows of legal-basis-register.csv; no fetching.',
           'facts': facts, 'unresolved': unres}
    if pending:
        doc['_facts_pending_register_id_pattern'] = pending
    out = os.path.join(BASE, '_research', f'CCG-annex_{jur}-facts.json')
    json.dump(doc, open(out, 'w', encoding='utf-8', newline='\n'), indent=1, ensure_ascii=False)
    v = subprocess.run([sys.executable, VALIDATOR, 'facts', out], capture_output=True, text=True)
    vout = (v.stdout + v.stderr).strip()
    print(jur, 'validator exit', v.returncode, vout[-300:])
    # ---- research pack
    src = open(os.path.join(BASE, '_research', 'stage5', jur + '.md'), encoding='utf-8').read()
    cited = sorted(set(re.findall(r'US-[A-Z0-9]+(?:-[A-Z0-9]+)*-\d{3}', src)))
    nonactive = [(c, reg[c]['status']) for c in cited if c in reg and reg[c]['status'] not in ('active',)]
    missing = [c for c in cited if c not in reg]
    parts = re.split(r'\n(?=## )', src)
    body = [s for s in parts[1:] if not re.match(r'## (Open questions|Parallel|Budget)', s)]
    P = [f'# CCG research pack - annex_{jur} ({NAMES[jur]})', '',
         f'Synthesis-B worker MN-WY, {TODAY}. Unit `annex_{jur}` of the CCG (jurisdiction annex, all 13 domains + special populations).',
         f'Facts file: `_research/CCG-annex_{jur}-facts.json` ({len(facts)} facts, {len(pending)} pending on the register_id pattern defect, {len(unres)} unresolved). '
         'Every claim below carries its register_id inline; numbers may be cited in the CCG only through a fact key.', '',
         '## 0. How to use this pack', '',
         '- Body sections 1-13 and Special populations are the stage-5 findings (`_research/stage5/' + jur + '.md`), carried verbatim because they are already organised by the 13 CCG domains with register ids inline.',
         '- Federal layer (FIT, FICA, FUTA, W-2/941/940), the multistate rules (reciprocity, sourcing) and the language seams (US-OWN-006: payslip in English; second-language duties attach to notices and posters only) live in annex_FED / annex_MULTI and are not repeated here.',
         '- Special populations (US-OWN-005): the state-level rules are in the Special populations table below; the country-wide coverage matrix is CCG unit `coverage`.',
         '- Values are 2026 unless the fact says otherwise. 2027 values appear only where the row carries an enacted or published 2027 figure; projections are never facts.', '']
    if traps:
        P += ['## 0.1 Synthesis decisions and traps (bind the builder)', ''] + ['- ' + t for t in traps] + ['']
    P += ['## 0.2 Register status check of the ids cited in the findings', '']
    if nonactive or missing:
        P += ['These ids appear in the findings but are not plain `active`; do not cite them for a number:', '']
        P += [f'- {c}: {s}' for c, s in nonactive] + [f'- {c}: not in register' for c in missing] + ['']
    else:
        P += ['All ids cited in the findings are `active` in the register.', '']
    P += ['## 0.3 Facts emitted', '', '| key | value | from | to | register_id | conf |', '|---|---|---|---|---|---|']
    for f in facts + pending:
        val = f['value']
        val = (str(val) + (' ' + f.get('currency', '') if 'currency' in f else '') + (' %' if f.get('unit_of_measure') == 'percent' else (' ' + f['unit_of_measure'] if 'unit_of_measure' in f else '')))
        P.append(f"| `{f['key']}` | {str(val).replace('|', '/')} | {f['effective_from']} | {f['effective_to'] or ''} | {f['register_id']}{' (PENDING id pattern)' if f in pending else ''} | {f['confidence']} |")
    P += ['', '# Findings by domain (stage 5)', '']
    P += [s.rstrip() + '\n' for s in body]
    P += ['## Open questions', '', 'Mirrors `unresolved[]` of the facts file (same keys, same wording).', '']
    for u in unres:
        P.append(f"- **{u['key']}** ({'blocking' if u['blocking'] else 'non-blocking'}): {u['why']} What would close it: {u['what_would_close_it']}")
    if not unres:
        P.append('- None outstanding.')
    open(os.path.join(BASE, '_research', f'CCG-annex_{jur}-research-pack.md'), 'w', encoding='utf-8', newline='\n').write('\n'.join(P) + '\n')
    # ---- report
    ids = sorted(set(used))
    R = [f'# Synthesis-B report - CCG annex_{jur} ({NAMES[jur]})', '', f'Worker MN-WY, {TODAY}.', '',
         f'- Facts written: {len(facts)} (`_research/CCG-annex_{jur}-facts.json`)',
         f'- Facts pending only because of the register_id pattern defect: {len(pending)} (`_facts_pending_register_id_pattern`)',
         f'- Unresolved: {len(unres)} ({sum(1 for u in unres if u["blocking"])} blocking)',
         f'- Research pack: `_research/CCG-annex_{jur}-research-pack.md`',
         f'- Non-active ids cited in the stage-5 findings (not used for numbers): {", ".join(c + "=" + s for c, s in nonactive) or "none"}',
         '', '## Register ids consumed (for the merge worker: append `CCG/annex_' + jur + '` to consumed_by)', '', '; '.join(ids), '',
         '## Validator output', '', '```', f'$ python validate_contract.py facts _research/CCG-annex_{jur}-facts.json', vout, f'exit {v.returncode}', '```', '']
    open(os.path.join(BASE, '_research', 'synthesis-B', f'CCG-annex_{jur}-report.md'), 'w', encoding='utf-8', newline='\n').write('\n'.join(R))
    return v.returncode


if __name__ == '__main__':
    rc = 0
    for j in sys.argv[1:]:
        rc |= build(j)
    sys.exit(rc)
