"""QA r1b: close / narrow gaps.json entries and CCG-research-request.json statuses for the P3 + CT items.
Closed entries leave gaps.json (precedent of the r1 pass: gaps.json lists open requests only); narrowed
entries stay with their new why / blocking / what_would_close_it, read back from the facts files.
Usage: python -I r1b_gaps.py <BASE>"""
import json, os, sys, collections

BASE = sys.argv[1]
R = os.path.join(BASE, '_research')
TODAY = '2026-11-02'
P3 = 'browser pass P3 2026-11-02 (_research/stage5/browser-pass-P3.md)'
CLOSED = {  # RQ: (key, closing facts / rows)
 'RQ-479': 'ca.minwage.fast_food.hourly; ca.minwage.health_care.*.hourly (US-CAB5-301, -302)',
 'RQ-147': 'de.wh.certificate corrected to the Delaware W-4 (US-DEB5-301); de.wh.certificate.default_and_copies (US-DES5-006)',
 'RQ-272': 'ny.local.nyc.supplemental.rate 4.25; ny.local.yonkers.resident.supplemental.rate 1.95975; ny.local.yonkers.nonresident.supplemental.rate 0.50 (US-NYB5-301, -302)',
 'RQ-337': 'tx.report.ui.enhanced_fields.status = proposed only, not mandatory on 2026-11-02 (US-TXB5-301); adoption watch moved to non-blocking tx.report.ui.enhanced_fields.adoption',
 'RQ-203': 'il.leave.cook.paid_leave.* (US-ILB5-301); 2025 Rules moved to non-blocking il.leave.cook.paid_leave.rules_2025',
 'RQ-118': 'nm.labour.minwage.local.santa_fe_county.* (US-NMB5-301); 2027 rate moved to non-blocking nm.labour.minwage.local.santa_fe_county.next_rate',
 'RQ-497': 'ct.wh.table.<period>.row.<nnn>, ct.wh.table.<period>.max_wages, ct.wh.tables.columns (US-CTQ1B-001); Examples 8-10 reproduced; engine choice moved to non-blocking ct.wh.engine_method',
}
NARROWED = {  # RQ: (facts file, unresolved key)
 'RQ-478': ('CCG-annex_CA-facts.json', 'ca.local_minwage.hourly'),
 'RQ-490': ('CCG-annex_CO-facts.json', 'co.famli.split.next_year'),
 'RQ-491': ('CCG-annex_CO-facts.json', 'co.local_minwage.other_cities'),
 'RQ-146': ('CCG-annex_DC-facts.json', 'dc.live.fy2027_bsa_permanent'),
 'RQ-029': ('CCG-annex_MI-facts.json', 'mi.local.cities.rates'),
 'RQ-255': ('CCG-annex_MA-facts.json', 'ma.report.w2.due_date_conflict'),
 'RQ-388': ('CCG-annex_WV-facts.json', 'wv.pit.tables.start_date'),
}
log = []
gp = os.path.join(R, 'gaps.json'); g = json.load(open(gp, encoding='utf-8'))
rp = os.path.join(R, 'CCG-research-request.json'); rq = json.load(open(rp, encoding='utf-8'))
reqs = {x['id']: x for x in rq['requests']}
gaps = {x['id']: x for x in g['gaps']}
for k in list(CLOSED) + list(NARROWED):
    assert k in gaps and k in reqs, k
for k, why in CLOSED.items():
    gaps.pop(k)
    r = reqs[k]; r['_status'] = 'closed'; r['_closed_by'] = 'agent 2 QA r1b %s: %s' % (TODAY, why)
    log.append('CLOSED %s %s' % (k, r['key']))
for k, (fn, key) in NARROWED.items():
    u = [x for x in json.load(open(os.path.join(R, fn), encoding='utf-8'))['unresolved'] if x['key'] == key][0]
    e = gaps[k]
    e['why_now'] = u['why']; e['what_would_close_it'] = u['what_would_close_it']; e['blocking'] = bool(u.get('blocking'))
    e['severity'] = 'blocker' if e['blocking'] else 'minor'
    e['searched'] = list(e.get('searched') or []) + [P3]
    e['searched_on'] = TODAY
    e['status'] = 'open'
    e['note'] = 'Narrowed by agent 2 QA r1b %s from the S5B-P3 rows; the facts file unresolved[] entry carries the current scope.' % TODAY
    r = reqs[k]; r['_status'] = 'open (narrowed)'; r['_what_would_close_it'] = u['what_would_close_it']
    r['_narrowed_by'] = 'agent 2 QA r1b %s: %s' % (TODAY, u['why'])
    if not e['blocking']:
        r['_downgraded'] = 'blocking -> non-blocking (QA r1b): ' + u['why'][-200:]
    log.append('NARROWED %s %s blocking=%s' % (k, key, e['blocking']))
g['gaps'] = [x for x in g['gaps'] if x['id'] in gaps]
c = collections.Counter(x['status'] for x in g['gaps'])
g['counts'] = dict(c); g['counts']['total'] = len(g['gaps']); g['counts']['blocking'] = sum(1 for x in g['gaps'] if x.get('blocking'))
g['generated_on'] = TODAY
g['generated_by'] = 'compliance-source-hunter (agent 2, QA r1 + r1b)'
rq['_qa_r1b_status_update'] = '%s agent 2: 7 closed (RQ-118, 147, 203, 272, 337, 479, 497), 7 narrowed (RQ-029, 146, 255, 388, 478, 490, 491); see _research/qa-r1-fix/AGENT2-R1b.md' % TODAY
json.dump(g, open(gp, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(rq, open(rp, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
log.append('COUNTS %s' % g['counts'])
open(os.path.join(R, 'qa-r1-fix', 'r1b_gaps.log'), 'w', encoding='utf-8').write('\n'.join(log) + '\n')
print('\n'.join(log))
