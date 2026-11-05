# QA r3: close the 8 disk-answerable RQs, add minor-9 gap entries, local-files sweep of the rest.
import sys, os, json, re, glob, shutil
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
sys.path.insert(0, r'C:/Users/instituto/Documents/brain-service/Research Pipeline/USA/US-compliance/_research/qa-r3-fix/scripts')
from lib import *
TODAY = '2026-11-02'; BK = '_research/qa-r3-fix/_backup'
def backup(p):
    dst = os.path.join(BK, p.replace('/', '__'))
    if not os.path.exists(dst): shutil.copy2(p, dst)
G = '_research/gaps.json'; RQF = '_research/CCG-research-request.json'
backup(G); backup(RQF)
g = json.load(open(G, encoding='utf-8')); rq = json.load(open(RQF, encoding='utf-8'))
GI = {e['id']: e for e in g['gaps']}; RI = {r['id']: r for r in rq['requests']}
fields, rows = load_reg(); R = {r['id']: r for r in rows}
LOG = {'closed': [], 'added': [], 'swept': 0, 'candidates': 0}

FED = '00-official-sources/ccg-sources/FED/'
closures = {
 'RQ-559': (['fed.retirement.pretax.tax_treatment', 'fed.base.401k_deferral.*', 'fed.base.403b_salary_reduction.*', 'fed.base.457b_salary_reduction.*', 'fed.base.simple_salary_reduction.*', 'fed.base.section125.rule', 'fed.base.section125_health.*', 'fed.base.dependent_care.*', 'fed.base.hsa_contribution.*'],
            ['US-FEDS5-029', 'US-FEDS5-008', 'US-FEDQ3-001', 'US-FEDQ3-002', 'US-FEDQ3-003'], 'CCG-m03_gross_to_net-facts.json (+ WTC-global_baseline)',
            [FED + 'FED_IRS-p15-2026_2026-11-02.pdf pp.47, 51 (sec. 15 table)', FED + 'FED_IRS-p15b-2026_2026-11-02.pdf pp.4, 6, 10, 17', FED + 'FED_USC-26-3121_govinfo-2024_2026-11-02.htm (a)(5)(G), (v)(1)', FED + 'FED_USC-26-3306_govinfo-2024_2026-11-02.htm (b)(5)(G), (r)(1)', FED + 'FED_USC-26-3401_govinfo-2024_2026-11-02.htm (a)(12) (govinfo curl HTTP 200 2026-11-02)']),
 'RQ-562': (['fed.fica.wage_definition.exclusions', 'fed.futa.wage_definition.exclusions', 'fed.wages.general_definition', 'fed.base.tips.*', 'fed.base.group_term_life.*', 'fed.base.educational_assistance.*', 'fed.base.transportation.*', 'fed.base.dependent_care.*'],
            ['US-FEDQ3-002', 'US-FEDQ3-003', 'US-FEDQ1-002', 'US-FEDS5-029', 'US-FEDS5-008'], 'CCG-m04_compensation-facts.json (+ m03, WTC-global_baseline)',
            [FED + 'FED_USC-26-3121_govinfo-2024_2026-11-02.htm (a)', FED + 'FED_USC-26-3306_govinfo-2024_2026-11-02.htm (b)', FED + 'FED_IRS-p15-2026_2026-11-02.pdf p.18 (sec. 5), pp.46-52 (sec. 15)', FED + 'FED_IRS-p15b-2026_2026-11-02.pdf p.6 (Table 2-1)']),
 'RQ-567': (['fed.fit.wage_definition', 'fed.fit.wage_definition.exclusions'], ['US-FEDQ3-001'], 'CCG-m06_tax-facts.json',
            [FED + 'FED_USC-26-3401_govinfo-2024_2026-11-02.htm (a)(1)-(23); fetched by curl from govinfo.gov, HTTP 200, 2026-11-02']),
 'RQ-568': (['fed.w4.default_no_certificate', 'fed.w4.default_no_certificate.pre2020_employee', 'fed.w4.exempt_not_renewed.default', 'fed.ssn.not_issued.w2_rule'], ['US-FEDQ3-004'], 'CCG-m06_tax-facts.json',
            [FED + 'FED_IRS-p15-2026_2026-11-02.pdf pp.11, 17, 26, 27 (no higher wage-withholding rate for a missing SSN is stated in sec. 4 or sec. 9; inspected directly)']),
 'RQ-570': (['fed.bik.exclusion_conditions', 'fed.bik.hsa.conditions', 'fed.bik.health_fsa.conditions', 'fed.bik.dependent_care.conditions', 'fed.bik.educational_assistance.conditions', 'fed.bik.transportation.conditions', 'fed.bik.trump_account.conditions', 'fed.base.*'],
            ['US-FEDS5-008', 'US-FEDR3-005'], 'CCG-m07_deductions-facts.json; Trump-account FICA/FUTA treatment stays unresolved (fed.bik.trump_account.employment_tax_treatment)',
            [FED + 'FED_IRS-p15b-2026_2026-11-02.pdf pp.4, 6, 10-11, 17', '00-official-sources/pdfs/FED/irs_p15a.html (Trump accounts)']),
 'RQ-572': (['fed.bik.valuation.general_rule', 'fed.bik.valuation.taxable_amount', 'fed.bik.vehicle.valuation_methods', 'fed.bik.vehicle.commuting_rule.value_per_one_way', 'fed.bik.treated_as_paid', 'fed.bik.withholding.method', 'fed.bik.vehicle.election_not_to_withhold_fit'],
            ['US-FEDS5-008'], 'CCG-m07_deductions-facts.json', [FED + 'FED_IRS-p15b-2026_2026-11-02.pdf pp.4, 26-27, 31-32']),
 'RQ-508': (['ca.pit.bracket.married.N.rate/ceiling/base', 'ca.pit.bracket.hoh.N.rate/ceiling/base', 'ca.pit.bracket.married.rates'], ['US-CAS5-001'], 'CCG-annex_CA-facts.json',
            ['00-official-sources/pdfs/CA/de44_wb.pdf p.48 (PDF p.56) Method B Tables 6 and 7, annual']),
 'RQ-506': (['al.wh.std_deduction.phaseout_steps', 'al.wh.std_deduction.{single,married_separate,married,head_of_family}.phaseout.*'], ['US-ALS5-001'], 'CCG-annex_AL-facts.json (+ WTC-country_specific)',
            ['00-official-sources/pdfs/AL/whbooklet_0126_webfetch-20261029.pdf pp.6-7']),
}
for gid, (keys, rids, where, searched) in closures.items():
    e = GI[gid]
    e['searched'] = [f'{s} - read {TODAY} (agent 2, QA r3)' for s in searched]   # only searches made for this key
    e['searched_on'] = TODAY; e['status'] = 'closed'; e['local_searched'] = True
    e['closed_on'] = TODAY; e['closed_by_keys'] = keys; e['closed_by_register_ids'] = rids; e['closed_in'] = where
    e['what_would_close_it'] = 'closed: answered from the local registered copies listed in searched[]'; e['closure_source'] = '; '.join(rids)
    r = RI[gid]; r['_status'] = 'closed'; r['_closed_on'] = TODAY; r['_closed_by'] = f'agent 2 (QA r3): keys {", ".join(keys)} in {where}; rows {", ".join(rids)}'
    LOG['closed'].append(gid)

# minor 9: unresolved items of agent 2 that had no gaps entry, + the two new ones of this round
newkeys = [('fed.fica.totalization.agreements_in_force', 'CCG-annex_FED', 'annex_FED', 'social_security'), ('ga.ui.rate_exclusion.thresholds', 'CCG-annex_GA', 'annex_GA', 'social_security'),
           ('hi.garn.child_support.remit_working_days', 'CCG-annex_HI', 'annex_HI', 'deductions_garnishments'), ('ia.pfml.state_program.none', 'CCG-annex_IA', 'annex_IA', 'social_security'),
           ('in.garn.statute_move.effective_date', 'CCG-annex_IN', 'annex_IN', 'deductions_garnishments'), ('ky.garn.child_support.iwo_fee_per_payment', 'CCG-annex_KY', 'annex_KY', 'deductions_garnishments'),
           ('ky.garn.child_support.lump_sum.reporting_threshold', 'CCG-annex_KY', 'annex_KY', 'deductions_garnishments'), ('ma.pit.ballot_ip25_18.rate', 'CCG-annex_MA', 'annex_MA', 'live_legal_change'),
           ('nc.labour.minwage.student_learner.hourly', 'CCG-annex_NC', 'annex_NC', 'labour_code'), ('ar.report.sui.efile_threshold_employees', 'CCG-annex_AR', 'annex_AR', 'reporting_instruments'),
           ('fed.bik.trump_account.employment_tax_treatment', 'CCG-m07_deductions', 'm07_deductions', 'benefits_in_kind')]
nxt = max(int(x[3:]) for x in RI) + 1
existing_keys = {e.get('key') for e in g['gaps']}
for key, fn, unit, dom in newkeys:
    if key in existing_keys: continue
    d = json.load(open(f'_research/{fn}-facts.json', encoding='utf-8'))
    u = [x for x in d['unresolved'] if x['key'] == key][0]
    gid = f'RQ-{nxt}'; nxt += 1
    loc = f'01-ccg/annexes/{unit}.md' if unit.startswith('annex_') else f'01-ccg/modules/{unit}.md'
    e = dict(id=gid, key=key, subject=f'{gid} - {u["why"][:180]}', location=loc, research_request_id=gid, blocking=False, severity='minor',
             searched=[f'{a} (as recorded in {fn}-facts.json unresolved[].attempted)' for a in u.get('attempted', [])], searched_on=TODAY,
             what_would_close_it=u['what_would_close_it'], status='open', url_searched=any('http' in a or '.gov' in a for a in u.get('attempted', [])),
             closure_source=u['what_would_close_it'], _origin='agent 2 unresolved item without a gaps entry (QA r3 minor 9)')
    g['gaps'].append(e); GI[gid] = e
    rq['requests'].append(dict(id=gid, key=key, location=loc, question=f'Close unresolved item {key}: {u["why"]}', why_blocking='non-blocking: the CCG states the limitation instead of the value',
                               domain=dom, acceptable_tier='A.2', attempted_by_requester=u.get('attempted', []), severity='minor', _unit=unit, _blocking=False,
                               _origin='agent 2 unresolved (QA r3 minor 9); added so the builder can tag [[GAP:' + gid + ']]', _status='open'))
    LOG['added'].append(f'{gid}={key}')

# major 5 (partial): local-files sweep for the open entries never searched by URL
STOP = set('rate rates rule rules employee employer employees report reporting threshold amount current value date effective state annex limit max min count list table form level treatment applies exists other wage wages'.split())
JUR = {r['id']: r['id'].split('-')[1][:2] for r in rows}
by_j = {}
for r in rows:
    if r['status'] in ('active', 'partial') and r['local_file']:
        j = r['id'][3:5] if not r['id'].startswith('US-FED') else 'FE'
        if r['id'].startswith('US-MULTI'): j = 'MU'
        by_j.setdefault(j, []).append(r)
cands = {}
for e in g['gaps']:
    if e['status'] != 'open' or e.get('url_searched') or e.get('local_searched'): continue
    k = e.get('key') or ''
    pre = k.split('.')[0]
    j = {'fed': 'FE', 'multi': 'MU'}.get(pre, pre.upper()[:2])
    terms = [t for t in re.split(r'[._]', '.'.join(k.split('.')[1:])) if len(t) >= 4 and t not in STOP][:3]
    rs = by_j.get(j, [])
    nfiles, hits = 0, []
    for r in rs:
        for p in files_of(r):
            t = text_of(p)
            if not t: continue
            nfiles += 1
            if terms and all(re.search(re.escape(x), t, re.I) for x in terms):
                hits.append(f'{r["id"]}:{os.path.basename(p)}')
    e['searched'] = [s for s in e.get('searched', []) if not (k and 'ssa.gov/oact/cola/cbb.html' in s and 'oasdi' not in k)]
    e['searched'].append(f'local-files sweep {TODAY} (agent 2, QA r3): {nfiles} local files of {len(rs)} active {j} register rows searched for all of {terms or "[no distinctive term in key]"}; '
                         + (f'{len(hits)} files contain all terms (candidates, not judged to answer the question): {", ".join(hits[:3])}' if hits else 'no file contains all terms'))
    e['local_searched'] = True; e['searched_on'] = TODAY
    LOG['swept'] += 1
    if hits: cands[e['id']] = {'key': k, 'terms': terms, 'files': hits[:10]}
LOG['candidates'] = len(cands)
g['schema_note'] += ' r3 fix: closed entries carry closed_on / closed_by_keys / closed_by_register_ids; local_searched=true marks entries swept against the local files of their jurisdiction (searched=local-files) - candidates in _research/qa-r3-fix/gap-local-candidates.json.'
g['generated_on'] = TODAY; g['generated_by'] += ' + QA r3 fix'
st = {}
for e in g['gaps']: st[e['status']] = st.get(e['status'], 0) + 1
g['counts'] = st; g['never_searched_by_url'] = [e['id'] for e in g['gaps'] if e['status'] == 'open' and not e.get('url_searched')]
open(G, 'w', encoding='utf-8').write(json.dumps(g, ensure_ascii=False, indent=2) + '\n')
open(RQF, 'w', encoding='utf-8').write(json.dumps(rq, ensure_ascii=False, indent=2) + '\n')
json.dump(cands, open('_research/qa-r3-fix/gap-local-candidates.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(LOG, open('_research/qa-r3-fix/gaps-r3-log.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(json.dumps({k: (v if not isinstance(v, list) else len(v)) for k, v in LOG.items()}), st, len(g['never_searched_by_url']))
print(LOG['added'])
