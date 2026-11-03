import sys, json, glob, re, os, collections
os.chdir(r"C:/Users/instituto/Documents/brain-service/Research Pipeline/USA/US-compliance/_research")
TODAY = '2026-11-02'
G = json.load(open('gaps.json', encoding='utf-8'))
gaps = G['gaps']
REQ = {q['id']: q for q in json.load(open('CCG-research-request.json', encoding='utf-8'))['requests']}
UNR = {}
for fn in glob.glob('*-facts.json'):
    for u in json.load(open(fn, encoding='utf-8')).get('unresolved', []): UNR.setdefault(u['key'], u)
PACK = collections.defaultdict(list)
for fn in glob.glob('*-research-pack.md') + glob.glob('stage5/*.md'):
    for line in open(fn, encoding='utf-8'):
        for k in re.findall(r'`([a-z][a-z0-9_]*(?:\.[a-z0-9_]+)+)`', line):
            PACK[k].append((os.path.basename(fn), line.strip()))
def aliases(x):
    q = REQ.get(x['id'], {}); al = [x['key']]
    for a in q.get('attempted_by_requester', []):
        al += re.findall(r'\(([a-z][a-z0-9_]*(?:\.[a-z0-9_]+)+)\)', a)
    return list(dict.fromkeys(al))
URLRE = re.compile(r'https?://[^\s)\]>`|"\']+')
HOSTRE = re.compile(r'\b(?:www\.)?[a-z0-9-]+(?:\.[a-z0-9-]+)*\.(?:gov|us|org|com|net|edu)(?:/[^\s,;)`]*)?', re.I)
def has_url(s): return bool(URLRE.search(s) or HOSTRE.search(s))
# 1. attempts recorded in facts files
att = collections.defaultdict(list)
for fn in glob.glob('*-facts.json'):
    for u in json.load(open(fn, encoding='utf-8')).get('unresolved', []):
        for a in u.get('attempted', []): att[u['key']].append(a)
# 2. ACCESS-GAPS lines per jurisdiction
acc = collections.defaultdict(list); cur = None
for line in open('stage5/ACCESS-GAPS.md', encoding='utf-8'):
    m = re.match(r'## (\w+) \(', line)
    if m: cur = m.group(1); continue
    if cur and line.startswith('- ') and URLRE.search(line): acc[cur].append(line[2:].strip())
# 3. browser-pass and stage5 jurisdiction files: lines mentioning the key
bp = []
for fn in glob.glob('stage5/*.md'):
    if 'ACCESS-GAPS' in fn or 'SYNTHESIS' in fn: continue
    for line in open(fn, encoding='utf-8'):
        if '`' in line or 'http' in line: bp.append((os.path.basename(fn), line.strip()))
# 4. today's re-tests (curl from a Brazilian exit, VPN off)
CURL = {
 'RQ-021': ['https://www.maine.gov/labor/unemployment/employers/tax-rates.html - HTTP 403', 'https://www.maine.gov/unemployment/employers/tax-rates - HTTP 403'],
 'RQ-029': ['https://www.michigan.gov/treasury/local/city-income-tax - HTTP 403', 'https://www.michigan.gov/taxes/business-taxes/withholding/city-income-tax - HTTP 403'],
 'RQ-089': ['https://dol.nebraska.gov/conciliation/minimumwage - curl 000 (DNS: could not resolve host)', 'https://dol.nebraska.gov/LaborStandards/Wage/MinimumWage - curl 000', 'https://dol.nebraska.gov/ - curl 000 (could not resolve host)', 'https://revenue.nebraska.gov/ - curl 000'],
 'RQ-138': ['https://otr.cfo.dc.gov/page/withholding-instructions-and-tables - HTTP 404', 'https://otr.cfo.dc.gov/page/2026-withholding-tax-forms - HTTP 404'],
 'RQ-146': ['https://lims.dccouncil.gov/Legislation/B26-0661 - HTTP 200, script-rendered shell (5,979 bytes, no enrolled text)', 'https://code.dccouncil.gov/us/dc/council/laws/26-189 - HTTP 404 (law not yet codified)'],
 'RQ-156': ['https://floridarevenue.com/taxes/taxesfees/Pages/reemployment.aspx - HTTP 200, no 401(k)/salary-reduction text', 'https://floridarevenue.com/taxes/tips/Pages/default.aspx - HTTP 200, no TIP on the point'],
 'RQ-165': ['https://dor.georgia.gov/federal-format-layout - HTTP 200; lists only an undated Federal_Format_Specs.pdf, no TY2026 specification or G-1003 2026 template'],
 'RQ-189': ['https://tax.idaho.gov/taxes/income-tax/withholding/forms/ - curl 000 (no connection)', 'https://tax.idaho.gov/wp-content/uploads/forms/EFO00307/EFO00307_2026.pdf - curl 000'],
 'RQ-202': ['https://www.chicago.gov/content/dam/city/depts/bacp/OLS/PaidLeave/PaidLeaveFAQs.pdf - HTTP 403', 'https://www.chicago.gov/city/en/depts/bacp/supp_info/minimumwageinformation.html - HTTP 200, minimum wage only'],
 'RQ-227': ['https://kentuckyola.org/ - curl 000', 'https://kydlgweb.ky.gov/Entities/TaxRates.cfm - HTTP 404'],
 'RQ-236': ['https://revenue.louisiana.gov/IndividualIncomeTax/FAQ - HTTP 403', 'https://legis.la.gov/Legis/Law.aspx?d=101682 (R.S. 47:293) - curl 000'],
 'RQ-237': ['https://legis.la.gov/Legis/Law.aspx?d=1225337 (R.S. 47:112.2) - curl 000'],
 'RQ-250': ['https://www.mass.gov/info-details/massachusetts-tax-treatment-of-fringe-benefits - HTTP 403', 'https://www.mass.gov/lists/technical-information-releases-tirs - HTTP 403'],
 'RQ-308': ['https://webserver.rilegislature.gov/Statutes/TITLE28/28-14/28-14-12.htm - curl 000'],
 'RQ-315': ['https://dor.sc.gov/withholding - HTTP 200, no revised WH-1603/WH-1603F after Act 110', 'https://dor.sc.gov/forms-site/Forms/WH1603F_2027.pdf - HTTP 404'],
 'RQ-343': ['https://tax.utah.gov/withholding - HTTP 403 (Cloudflare)', 'https://tax.utah.gov/forms/pubs/pub-14.pdf - HTTP 403'],
 'RQ-352': ['https://www.vec.virginia.gov/employers/tax-rates - HTTP 403', 'https://www.vec.virginia.gov/employers/Unemployment-Taxes - HTTP 403'],
 'RQ-388': ['https://tax.wv.gov/Business/Withholding/Pages/WithholdingTaxes.aspx - HTTP 404', 'https://tax.wv.gov/Documents/TaxForms/it100.2a.pdf - HTTP 404'],
 'RQ-390': ['https://www.huntingtonwv.gov/finance - curl 000', 'https://www.cityofwheeling.org/finance - curl 000'],
 'RQ-391': ['https://workforcewv.org/businesses/unemployment-tax-information/ - HTTP 200, no SB 1053 fee base stated', 'https://www.wvlegislature.gov/Bill_Status/bills_history.cfm?input=1053&year=2025&sessiontype=RS - HTTP 200, bill history only'],
 'RQ-398': ['https://dws.wyo.gov/ - HTTP 200, no 2026 rate release', 'https://dws.wyo.gov/dws-division/unemployment-insurance-employers/ui-tax-rates/ - HTTP 404'],
 'RQ-458': ['https://www.almonline.org/ - HTTP 200, no occupational-tax list', 'https://www.auburnalabama.org/finance/business-and-licensing-forms/occupational-license - curl 000'],
 'RQ-463': ['https://www.dfa.arkansas.gov/office/taxes/income-tax-administration/withholding-tax-branch/ - HTTP 200, no 3.7% start-date notice'],
 'RQ-478': ['https://www.sanjoseca.gov/.../office-of-equality-assurance/minimum-wage-ordinance - HTTP 403 (Akamai)'],
 'RQ-491': ['https://www.edgewaterco.gov/ - HTTP 403', 'https://denvergov.org/.../Denver-Labor/Policy-Rules-Resources/Minimum-Wage - HTTP 200, 537-byte WAF challenge'],
 'RQ-358': ['https://labor.vermont.gov/wage-and-hour/minimum-wage - HTTP 404', 'https://labor.vermont.gov/news - HTTP 200, no 2027 minimum wage item'],
}
# reason per blocking item: access vs not yet published
ACCESS = {'RQ-021', 'RQ-029', 'RQ-189', 'RQ-202', 'RQ-227', 'RQ-236', 'RQ-237', 'RQ-250', 'RQ-308', 'RQ-343', 'RQ-352', 'RQ-390', 'RQ-458', 'RQ-478', 'RQ-491'}
UNPUB = {'RQ-138', 'RQ-146', 'RQ-156', 'RQ-165', 'RQ-315', 'RQ-388', 'RQ-391', 'RQ-398', 'RQ-463'}
CLOSE = {
 'RQ-308': 'R.I. Gen. Laws 28-14-12 as amended effective 2026-01-01 (webserver.rilegislature.gov/Statutes/TITLE28/28-14/28-14-12.htm) or the RI DLT Labor Standards employer notice (dlt.ri.gov).',
 'RQ-315': 'SCDOR revised WH-1603 / WH-1603F reflecting Act 110, or an SCDOR Information Letter fixing their effective date (dor.sc.gov/withholding).',
 'RQ-343': 'Utah State Tax Commission Pub 14 PDF revision or tax notice stating the effective date of the 485/970 schedules (tax.utah.gov/forms/pubs/pub-14.pdf), read from a US exit.',
 'RQ-352': 'VEC 2026 tax-rate notice or employer handbook stating the pool-cost charge and the new-employer rate composition (vec.virginia.gov), read from a US exit.',
 'RQ-390': "Each city's service-fee ordinance or finance page (Huntington, Wheeling, Morgantown, Parkersburg, Fairmont, Weirton, Chester, Romney; municipal codes on library.municode.com / codelibrary.amlegal.com).",
 'RQ-391': 'WorkForce West Virginia employer notice on the SB 1053 fee base (workforcewv.org/businesses/unemployment-tax-information) or the enrolled SB 1053 text (wvlegislature.gov).',
 'RQ-398': 'Wyoming DWS 2026 UI contribution-rate release or employer rate-notice table with minimum/maximum rates, industry new-employer rates and the adjustment factor (dws.wyo.gov).',
 'RQ-291': 'Multnomah County Code ch. 11 PFA section (multco.us) or the county PFA withholding notice stating the +0.8% step year.',
 'RQ-351': 'Virginia Tax 2027 employer withholding instructions / formula (tax.virginia.gov), normally issued in December 2026.',
 'RQ-358': 'VDOL 2027 minimum wage press release (labor.vermont.gov) or BLS CPI-U August-to-August change for the 21 V.S.A. 384 derivation (bls.gov).',
 'RQ-371': "Each city's 2027 minimum-wage notice (Seattle OLS, SeaTac, Tukwila, Renton, Bellingham, Burien, Everett) or the WA L&I local minimum wage page (lni.wa.gov).",
 'RQ-089': 'NDOL 2027 minimum wage announcement under Neb. Rev. Stat. 48-1203 (dol.nebraska.gov), read from a US exit or a browser pass; the host does not resolve from the build machine.'}
STOP = {'rate', 'next', 'year', 'hourly', 'current', 'value', 'values', 'local', 'state', 'other', 'total', 'annual', 'weekly', 'employer', 'employee', 'report', 'labour', 'records'}
def toks(key):
    return [t for s in key.split('.')[1:] for t in s.split('_') if len(t) >= 4 and t not in STOP]
never = []
for x in gaps:
    jur = x['key'].split('.')[0].upper()
    s = []
    s += [f'{u} ({TODAY}, QA r2 re-test, curl from a non-US exit)' for u in CURL.get(x['id'], [])]
    ts = toks(x['key'])
    for k in aliases(x):
        for a in att.get(k, []):
            if a not in s: s.append(a)
        for fn, line in PACK.get(k, []):
            if has_url(line) and line[:300] not in s: s.append(f'{line[:300]} ({fn})')
    for line in acc.get(jur, []) + acc.get('MULTI' if jur == 'MULTI' else jur, []):
        low = line.lower()
        if any(t in low for t in ts) and line not in s: s.append(f'{line} (stage 5 ACCESS-GAPS, {TODAY})')
    for fn, line in bp:
        if x['key'] in line and has_url(line) and line[:300] not in s: s.append(f'{line[:300]} ({fn})')
    for old in x.get('searched', []):
        if old not in s: s.append(old)
    x['searched'] = s
    x['searched_on'] = TODAY
    urls = [e for e in s if has_url(e) and not e.startswith('_research/')]
    x['url_searched'] = bool(urls)
    if not urls: never.append(x['id'])
    if not x['what_would_close_it'].strip() and x['id'] in CLOSE: x['what_would_close_it'] = CLOSE[x['id']]
    if not x['what_would_close_it'].strip():
        for k in aliases(x):
            if k in UNR and UNR[k].get('what_would_close_it', '').strip(): x['what_would_close_it'] = UNR[k]['what_would_close_it']; break
    if not x['what_would_close_it'].strip():
        q = REQ.get(x['id'], {}); m = re.search(r'Expected closing source:\s*(.+)', q.get('question', '')) or re.search(r'Source to read:\s*(.+?)(?:$)', q.get('question', ''))
        if q.get('_what_would_close_it'): x['what_would_close_it'] = q['_what_would_close_it']
        elif m: x['what_would_close_it'] = m.group(1).strip()
    if x['id'] in CLOSE and x['id'] in ('RQ-089',): x['what_would_close_it'] = CLOSE[x['id']]
    x['closure_source'] = x['what_would_close_it']
    if x['blocking'] is True or x['id'] in ACCESS | UNPUB:
        if x['id'] in ACCESS | UNPUB:
            x['status'] = 'documented_limitation'; x['blocking'] = False
            x['reason'] = 'access (non-US exit)' if x['id'] in ACCESS else 'not yet published'
            x['decided_by'] = 'orchestrator journal 2026-11-02 (round 3); re-tested by source hunter ' + TODAY
    if x['id'] == 'RQ-089':
        x['status'] = 'open'; x['blocking'] = False; x['reason'] = 'access (non-US exit): publication date 2026-10-15 has passed; dol.nebraska.gov does not resolve from the build machine (2026-11-02)'
        x['expected_publication'] = 'overdue (due 2026-10-15); re-read on the next US-exit / browser pass'
G['counts'] = dict(collections.Counter(g['status'] for g in gaps)); G['counts']['total'] = len(gaps); G['counts']['blocking'] = sum(1 for g in gaps if g['blocking'])
G['counts']['url_searched'] = sum(1 for g in gaps if g['url_searched']); G['counts']['never_searched_by_url'] = len(never)
G['never_searched_by_url'] = never
G['generated_on'] = TODAY; G['generated_by'] = 'compliance-source-hunter (agent 2, QA r1 + r1b + r2 prep + r2 fix)'
G['schema_note'] += ' r2 fix: searched[] now carries the official URLs tried (today\'s curl re-test, facts unresolved[].attempted, stage-5 ACCESS-GAPS and browser-pass lines) before the internal files; url_searched=false marks entries never searched by URL (listed in never_searched_by_url); closure_source mirrors what_would_close_it; reason = access (non-US exit) / not yet published for documented limitations.'
json.dump(G, open('gaps.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(G['counts']); print('empty close:', [g['id'] for g in gaps if not g['what_would_close_it'].strip()])
print('blocking left:', [g['id'] for g in gaps if g['blocking']])
