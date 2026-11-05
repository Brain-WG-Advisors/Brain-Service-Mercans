import sys, json, collections; sys.path.insert(0, '.')
from lib import *
fields, R = load_reg(); byid = {r['id']: r for r in R}
res = json.load(open('_research/qa-r2-fix/locate.json', encoding='utf-8'))
VETO = set('''co.local.opt.denver.employer_monthly ma.leave.sick.employer_threshold_paid mo.records.retention_years nc.pit.oracle.example_2.nra_withholding
nc.pit.oracle.example_1.withholding ms.pit.oracle.example_1.withholding mo.pit.local.st_louis.earnings_tax.rate fed.oracle.pub15t.nra_example.withholding fed.futa.rate.gross
ma.pit.rate ma.wh.supplemental.rate id.sui.new_employer.rate oh.pit.municipal.rate_cap_without_vote oh.garn.iwo.employer_fee.min tn.sui.employer.rate.max ne.data.ssn.max_digits_displayed
nv.labour.lodging_credit.weekly_multiple_of_minwage mi.local.cities.count pa.leave.pittsburgh.annual_cap_hours.15plus sc.labour.pay_change_notice.days sc.records.wage.retention_years
ma.overtime.weekly_threshold_hours wa.pit.high_income_tax.agi_threshold wv.sui.employer.rate.max wv.ui.rate.reduction.sb1053 ri.report.w2.efile_threshold'''.split())
def printable(s): return sum(32 <= ord(c) < 127 for c in s) / max(1, len(s)) > 0.9
def unit_token(fn):
    d = json.load(open(fn, encoding='utf-8')); return d['artifact'] + ('/' + d['unit'] if d.get('unit') else '')
facts = {fn: json.load(open(fn, encoding='utf-8')) for fn in facts_files()}
log = []; ev = collections.defaultdict(list); used = collections.defaultdict(set)
for k, L in res.items():
    for e in L:
        v = e['value']; f = facts[e['file']]['facts'][e['idx']]
        assert f['key'] == k and f['value'] == v and f['register_id'] == e['rid'], (k, e['file'])
        own = e['own_loc']; new = e['new']
        if own and own['score'] >= 1 and printable(own['snip']):
            ev[e['rid']].append((k, v, own)); log.append(('context_quote_own', k, v, e['rid'], e['file'])); continue
        small = isinstance(v, (int, float)) and float(v).is_integer() and abs(v) < 100
        ok = new and k not in VETO and v != 0 and printable(new['snip']) and new['score'] >= (3 if small else 2)
        if ok:
            f['register_id'] = new['id']; f['tier'] = byid[new['id']]['tier']; f['url'] = byid[new['id']]['url'] or f.get('url')
            f['authority'] = byid[new['id']]['authority'] or f.get('authority')
            ev[new['id']].append((k, v, new)); used[new['id']].add(unit_token(e['file']))
            log.append(('repointed', k, v, e['rid'] + '->' + new['id'], e['file']))
        elif own and printable(own['snip']):
            ev[e['rid']].append((k, v, own)); log.append(('context_quote_own_weak', k, v, e['rid'], e['file']))
        else:
            log.append(('unresolved_location', k, v, e['rid'], e['file']))
for rid, items in ev.items():
    r = byid[rid]; parts = []
    seen = set()
    for k, v, loc in items:
        if (k, v) in seen: continue
        seen.add((k, v)); q = loc['snip'][60:200].replace('"', "'").replace('|', '/')
        parts.append(f"{k}={v} at {os.path.basename(loc['file'])}{' p.' + loc['page'] if loc['page'] else ''}: '...{q}...'")
    r['verification_method'] = (r['verification_method'] + ' | QA r2 2026-11-02 figure located: ' + ' ; '.join(parts)).strip(' |')
    cb = [x for x in r['consumed_by'].split(';') if x]
    for t in sorted(used.get(rid, ())):
        if t not in cb: cb.append(t)
    r['consumed_by'] = ';'.join(cb)
save_reg(fields, R)
for fn, d in facts.items():
    json.dump(d, open(fn, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(log, open('_research/qa-r2-fix/repoint-log.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
print(collections.Counter(x[0] for x in log))
mk = set(json.load(open('_qa/CCG-review-r2.json', encoding='utf-8'))['findings'][29]['_mis_cited_keys'])
print('miscited remaining:', sorted({x[1] for x in log if x[1] in mk and x[0] == 'unresolved_location'}))
