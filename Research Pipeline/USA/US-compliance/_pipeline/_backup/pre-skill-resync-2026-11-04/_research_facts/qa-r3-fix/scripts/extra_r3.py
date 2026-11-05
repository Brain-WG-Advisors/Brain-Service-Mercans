# QA r3 major 5: three more gaps answered by the local Pub. 15 (2026) copy (RQ-531, RQ-524 closed; RQ-556 narrowed).
import sys, os, json
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
sys.path.insert(0, r'C:/Users/instituto/Documents/brain-service/Research Pipeline/USA/US-compliance/_research/qa-r3-fix/scripts')
from lib import *
import jsonschema
TODAY = '2026-11-02'
fields, rows = load_reg(); R = {r['id']: r for r in rows}
G = '_research/gaps.json'; RQF = '_research/CCG-research-request.json'
g = json.load(open(G, encoding='utf-8')); rq = json.load(open(RQF, encoding='utf-8'))
GI = {e['id']: e for e in g['gaps']}; RI = {r['id']: r for r in rq['requests']}
RID = 'US-FEDQ1-002'; r = R[RID]
def mk(key, value, note):
    return dict(key=key, value=value, effective_from='2026-01-01', effective_to='2026-12-31', register_id=RID, tier=r['tier'], verification_method='quoted from authority page',
                authority=r['authority'], url=r['url'], confidence='high', note=note)
items = {
 'RQ-531': [mk('fed.fit.supplemental.aggregate_method', 'Supplemental wages identified separately, income tax withheld from regular wages in the current or preceding year: either flat 22% or aggregate - add the supplemental wages to the concurrently paid regular wages (or, if none, to the regular wages of the current or preceding payroll period), figure the tax as if one regular-period payment, subtract the tax withheld or to be withheld from the regular wages, withhold the remainder; earlier supplemental payments of the same period are aggregated too. No income tax withheld from regular wages in the current or preceding year: aggregate method only. Supplemental wages paid with regular wages without specifying each amount: withhold on the total as one regular payment.',
                        'Pub. 15 (2026) sec. 7 Supplemental Wages, p.24.')],
 'RQ-524': [mk('fed.vacation_payout.supplemental_status', 'Vacation pay is withheld on as regular wages; when it is in addition to regular wages for the vacation period (e.g. an annual lump-sum payment for unused vacation leave) it is a supplemental wage payment; vacation pay for longer than the usual payroll period is spread over the pay periods for which it is paid.',
                        'Pub. 15 (2026) sec. 7, Vacation pay, p.25.')],
 'RQ-556': [mk('fed.ein.format', 'Nine-digit number arranged 00-0000000', 'Pub. 15 (2026) sec. 1 Employer Identification Number (EIN), p.13.')],
}
added = []
for gid, facts in items.items():
    unit = RI[gid].get('_unit') or 'm10_reporting'
    p = f'_research/CCG-{unit}-facts.json'
    d = json.load(open(p, encoding='utf-8'))
    for nf in facts:
        d['facts'] = [f for f in d['facts'] if not (f['key'] == nf['key'] and f['effective_from'] == nf['effective_from'])] + [nf]
        added.append(f'{unit}:{nf["key"]}')
    d['generated_on'] = TODAY
    bk = '_research/qa-r3-fix/_backup/' + p.replace('/', '__')
    if not os.path.exists(bk): open(bk, 'w', encoding='utf-8').write(open(p, encoding='utf-8').read())
    open(p, 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    tok = f'CCG/{unit}'
    if tok not in r['consumed_by'].split(';'): r['consumed_by'] += ';' + tok
    e = GI[gid]
    e['searched'] = [f'00-official-sources/ccg-sources/FED/FED_IRS-p15-2026_2026-11-02.pdf {facts[0]["note"].split(", ")[-1]} - read {TODAY} (agent 2, QA r3)'] + [s for s in e['searched'] if s.startswith('local-files sweep')]
    e['local_searched'] = True; e['searched_on'] = TODAY
    if gid == 'RQ-556':
        e['status'] = 'open'; e['_narrowed'] = 'EIN format answered (fed.ein.format, US-FEDQ1-002 p.13); the State withholding / UI account-number formats remain open'
        e['what_would_close_it'] = 'each State revenue and workforce agency registration page stating its account-number format (fan-out per State)'
        RI[gid]['_status'] = 'open (narrowed)'
    else:
        e.update(status='closed', closed_on=TODAY, closed_by_keys=[f['key'] for f in facts], closed_by_register_ids=[RID], closed_in=p.split('/')[-1],
                 what_would_close_it='closed: answered from the local registered copy listed in searched[]', closure_source=RID)
        RI[gid].update(_status='closed', _closed_on=TODAY, _closed_by=f'agent 2 (QA r3): {facts[0]["key"]} in {p.split("/")[-1]}; row {RID}')
    schema = json.load(open(r'C:/Users/instituto/mercans-pipeline/shared/schemas/facts.schema.json', encoding='utf-8'))
    errs = list(jsonschema.Draft202012Validator(schema).iter_errors(d)); print(p, 'schema errors', len(errs))
r['verified_on'] = TODAY
save_reg(fields, rows)
st = {}
for e in g['gaps']: st[e['status']] = st.get(e['status'], 0) + 1
g['counts'] = st; g['never_searched_by_url'] = [e['id'] for e in g['gaps'] if e['status'] == 'open' and not e.get('url_searched')]
open(G, 'w', encoding='utf-8').write(json.dumps(g, ensure_ascii=False, indent=2) + '\n')
open(RQF, 'w', encoding='utf-8').write(json.dumps(rq, ensure_ascii=False, indent=2) + '\n')
print(added, st, len(g['never_searched_by_url']))
