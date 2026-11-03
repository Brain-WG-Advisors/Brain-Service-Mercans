# QA r3b task 7: triage of the 181 local gap candidates (agent 2). Writes facts, gaps, register (consumed_by / article note).
import sys, json, re, collections
sys.path.insert(0, r"C:/Users/instituto/Documents/brain-service/Research Pipeline/USA/US-compliance/_research/qa-r3-fix/scripts")
from lib import *
import pymupdf
TODAY = '2026-11-02'
def jload(p): return json.load(open(p, encoding='utf-8'))
def jsave(p, d): open(p, 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
fields, rows = load_reg(); byid = {r['id']: r for r in rows}
log = {'facts_added': [], 'ct_parse': {}}

# ---------- CT Tables C, D, E (IP 2026(1) PDF pp.28-30) ----------
CTPDF = '00-official-sources/pdfs/CT/CT_IP-2026-1_2026-11-02.pdf'
doc = pymupdf.open(CTPDF)
def toks(page_ix, start_marker):
    t = re.sub(r'\s+', ' ', doc[page_ix].get_text())
    t = t[t.find(start_marker) + len(start_marker):] if start_marker in t[:400] else t
    out = []
    for m in re.finditer(r'\$\s*([\d,]+)|(and up)|(?<![\d$])(\.\d\d)(?!\d)', t):
        if m.group(1): out.append(int(m.group(1).replace(',', '')))
        elif m.group(2): out.append('UP')
        else: out.append(float(m.group(3)))
    return out
def triples(tk):
    res = []; i = 0
    while i < len(tk):
        lo = tk[i]
        if i + 1 < len(tk) and tk[i + 1] == 'UP': res.append((lo, None, tk[i + 2])); i += 3
        else: res.append((lo, tk[i + 1], tk[i + 2])); i += 3
    return res
def split_cols(tr, ncol):
    cols = [[] for _ in range(ncol)]
    for k, x in enumerate(tr): cols[k % ncol].append(x)
    return cols
def check(col):
    ok = all(isinstance(a[0], int) for a in col) and col[-1][1] is None
    ok = ok and all(col[k][1] == col[k + 1][0] for k in range(len(col) - 1))
    return ok
def fmt(col, money=True):
    parts = []
    for lo, hi, v in col:
        vv = (f'{v:,}' if money else f'{v:.2f}')
        parts.append(f"{lo:,}-{hi:,}: {vv}" if hi is not None else f"over {lo:,}: {vv}")
    return '; '.join(parts)
tc = split_cols(triples(toks(27, 'Table C - 2% Tax Rate Phase-Out Add-Back')), 4)   # A/D, B, C, F
p29 = re.sub(r'\s+', ' ', doc[28].get_text()); p29 = p29[p29.find('Table D - Tax Recapture') + 23:]
td = split_cols(triples([int(m.group(1).replace(',', '')) if m.group(1) else 'UP' for m in re.finditer(r'\$\s*([\d,]+)|(and up)', p29)]), 3)  # A/D/F, B, C
te = split_cols(triples(toks(29, 'Table E - Personal Tax Credits')), 4)  # A, B, C, F
tables = {'table_c': (tc, ['code_a_d', 'code_b', 'code_c', 'code_f'], True, '2% tax rate phase-out add-back (USD) by annualized salary (more than - less than or equal to)', 28),
          'table_d': (td, ['code_a_d_f', 'code_b', 'code_c'], True, 'tax recapture amount (USD) by annualized salary (more than - less than or equal to)', 29),
          'table_e': (te, ['code_a', 'code_b', 'code_c', 'code_f'], False, 'personal tax credit decimal by annualized salary (more than - less than or equal to); code D: 0.00', 30)}
ct_reg = 'US-CTP10-001'
for tname, (cols, names, money, desc, pg) in tables.items():
    for col, nm in zip(cols, names):
        ok = check(col); log['ct_parse'][f'{tname}.{nm}'] = {'rows': len(col), 'contiguous_and_open_ended': ok, 'first': col[0], 'last': col[-1]}
        if not ok: continue
        f = {"key": f"ct.wh.{tname}.{nm}", "value": fmt(col, money), "effective_from": "2026-01-01", "effective_to": "2026-12-31",
             "register_id": ct_reg, "tier": "A.2", "verification_method": "inspected directly",
             "authority": "Connecticut Department of Revenue Services (DRS)",
             "url": byid[ct_reg]['url'], "confidence": "high",
             "note": (f"TPG-211, 2026 Withholding Calculation Rules (Rev. 12/25), {desc}; printed in IP 2026(1) Circular CT, local copy {CTPDF} PDF p.{pg}. "
                      f"Parsed with PyMuPDF; {len(col)} rows, each lower bound equals the previous upper bound, last row open-ended (QA r3b, RQ-509). "
                      "Use: TPG-211 Steps 8 (Table C), 9 (Table D), 11-12 (Table E: withholding x (1.00 - decimal))."),
             "_domain": "income_tax"}
        d = jload('_research/CCG-annex_CT-facts.json')
        if not any(x['key'] == f['key'] and x['effective_from'] == f['effective_from'] for x in d['facts']):
            d['facts'].append(f); jsave('_research/CCG-annex_CT-facts.json', d); log['facts_added'].append(f['key'])

# ---------- SC UI coverage thresholds (S.C. Code 41-27-230(5),(6)) ----------
sc_reg = 'US-SCS5-014'
sc_url = byid[sc_reg]['url']
sc_base = {"effective_from": "1980-01-01", "effective_to": None, "register_id": sc_reg, "tier": "A.1", "verification_method": "quoted from authority page",
           "authority": "South Carolina Legislature (S.C. Code Title 41 ch. 27)", "url": sc_url, "confidence": "high", "_domain": "social_security"}
sc_facts = [
  ("sc.ui.coverage.agricultural.cash_per_quarter", 20000, "USD", "41-27-230(5)(a)(i): agricultural labor is employment where the person 'during any calendar quarter in either the current or preceding calendar year paid remuneration in cash of twenty thousand dollars or more to individuals employed in agricultural labor'."),
  ("sc.ui.coverage.agricultural.workers_in_20_weeks", 10, None, "41-27-230(5)(a)(ii): or 'for some portion of a day in each of twenty different calendar weeks ... in either the current or the preceding calendar year, employed in agricultural labor ... ten or more individuals'."),
  ("sc.ui.coverage.domestic.cash_per_quarter", 1000, "USD", "41-27-230: domestic service in a private home, local college club or fraternity/sorority chapter is employment where the person 'paid cash remuneration of one thousand dollars or more ... in the current calendar year or the preceding calendar year to individuals employed in such domestic service in any calendar quarter'."),
]
for k, v, cur, q in sc_facts:
    f = {"key": k, "value": v}
    if cur: f["currency"] = cur
    else: f["unit_of_measure"] = "persons"
    f.update(sc_base); f["note"] = q + " Local copy 00-official-sources/ccg-sources/SC/SC-Code_t41c027_2026-11-02.html (QA r3b, RQ-318). effective_from: the 1980-01-01 cut-over the subsection states for the alien exclusion; the thresholds apply 'after December 31, 1977'."
    if k == 'sc.ui.coverage.domestic.cash_per_quarter': f["effective_from"] = "1978-01-01"
    if k.startswith('sc.ui.coverage.agricultural'): f["effective_from"] = "1978-01-01"; f["note"] = q + " Local copy 00-official-sources/ccg-sources/SC/SC-Code_t41c027_2026-11-02.html (QA r3b, RQ-318). In force as at retrieved_on; the subsection applies to service 'performed after December 31, 1977'."
    if k == 'sc.ui.coverage.domestic.cash_per_quarter': f["note"] = q + " Local copy 00-official-sources/ccg-sources/SC/SC-Code_t41c027_2026-11-02.html (QA r3b, RQ-318). In force as at retrieved_on; applies to remuneration paid 'after December 31, 1977'."
    d = jload('_research/CCG-annex_SC-facts.json')
    if not any(x['key'] == k for x in d['facts']):
        d['facts'].append(f); jsave('_research/CCG-annex_SC-facts.json', d); log['facts_added'].append(k)
r = byid[sc_reg]
if '41-27-230' not in r['article_or_section']:
    r['article_or_section'] += '; 41-27-230(5) agricultural and domestic-service coverage thresholds (QA r3b)'
    r['figure_or_rule_carried'] += ' | 41-27-230: agricultural labor covered at 20,000 cash in a calendar quarter or 10 workers in 20 weeks; domestic service at 1,000 cash in a calendar quarter (current or preceding year).'

# ---------- partial: OR IWO priority; FED EIN format ----------
or_reg = 'US-ORS5-017'
f = {"key": "or.garn.iwo.priority_over_writ", "value": "An order to withhold income (child support) has priority over a writ of garnishment; compliance with the order reduces or eliminates the amount delivered under the writ.",
     "effective_from": "2026-01-01", "effective_to": None, "register_id": or_reg, "tier": byid[or_reg]['tier'], "verification_method": "quoted from authority page",
     "authority": byid[or_reg]['authority'], "url": byid[or_reg]['url'], "confidence": "high",
     "note": "ORS chapter 18 garnishee response form, local copy 00-official-sources/.../OR_ORS018_2026-11-02.html: 'The order to withhold income has priority over the writ of garnishment, and compliance with the order will reduce or eliminate the money that I would otherwise deliver under the writ.' In force as at retrieved_on. Partial answer to RQ-296: the employer fee is still open (QA r3b).",
     "_domain": "deductions"}
d = jload('_research/CCG-annex_OR-facts.json')
if not any(x['key'] == f['key'] for x in d['facts']): d['facts'].append(f); jsave('_research/CCG-annex_OR-facts.json', d); log['facts_added'].append(f['key'])
p15rows = [x for x in rows if 'FED_IRS-p15-2026_2026-11-02.pdf' in x['local_file'] and x['status'] == 'active']
ein_reg = next((x['id'] for x in p15rows if 'EIN' in x['article_or_section'] or 'sec. 1' in x['article_or_section']), p15rows[0]['id'])
f = {"key": "fed.ein.format", "value": "nine digits issued by the IRS, arranged 00-0000000",
     "effective_from": "2026-01-01", "effective_to": None, "register_id": ein_reg, "tier": "A.2", "verification_method": "quoted from authority page",
     "authority": "Internal Revenue Service", "url": byid[ein_reg]['url'], "confidence": "high",
     "note": "Pub. 15 (2026) sec. 1 Employer Identification Number, local copy 00-official-sources/ccg-sources/FED/FED_IRS-p15-2026_2026-11-02.pdf PDF p.13: 'The EIN is a nine-digit number the IRS issues. The digits are arranged as follows: 00-0000000.' Partial answer to RQ-556: State account-number formats still open (QA r3b).",
     "_domain": "reporting_instruments"}
d = jload('_research/CCG-annex_FED-facts.json')
if not any(x['key'] == f['key'] for x in d['facts']): d['facts'].append(f); jsave('_research/CCG-annex_FED-facts.json', d); log['facts_added'].append(f['key'])
log['ein_register_id'] = ein_reg

# ---------- gaps triage ----------
special = {
 'RQ-509': ('closed_from_local', 'Tables C, D and E transcribed from IP 2026(1) PDF pp.28-30 (TPG-211 Rev. 12/25) into ct.wh.table_c.*, ct.wh.table_d.*, ct.wh.table_e.* [US-CTP10-001].'),
 'RQ-318': ('closed_from_local', 'S.C. Code 41-27-230(5) and the domestic-service paragraph read in the local t41c027 copy: sc.ui.coverage.agricultural.cash_per_quarter, .workers_in_20_weeks, sc.ui.coverage.domestic.cash_per_quarter [US-SCS5-014].'),
 'RQ-296': ('local_partial', 'Priority answered from the ORS ch. 18 garnishee form (or.garn.iwo.priority_over_writ [US-ORS5-017]); the employer IWO fee is not in any local OR file.'),
 'RQ-556': ('local_partial', 'EIN format answered from Pub. 15 (2026) PDF p.13 (fed.ein.format); State withholding / UI account-number formats are not in the local files.'),
 'RQ-309': ('local_checked_no_answer', 'Local RIGL 28-41-35 copy (Wayback, predates later amendments) lists only 4 (2014) / 5 (2022) / 6 (2023) weeks; the current cap cannot be stated from it.'),
 'RQ-288': ('local_checked_no_answer', '40 O.S. 185 (leave for military / jury / public office with seniority) is limited by 40 O.S. 186 to railroad-company employees; not a general military-leave rule.'),
 'RQ-461': ('local_checked_no_answer', 'AL booklet states the Act 2025-334 30/31-day rule but no day-counting guidance.'),
 'RQ-171': ('local_checked_no_answer', 'HI Tax Announcement on Act 35 lists conformity changes "including, but not limited to"; not the full 235-2.3(b) list.'),
 'RQ-123': ('local_checked_no_answer', 'NM notice says the bulk schemas are in TAP (Help > FAQ > Bulk); the schema files are not on disk.'),
 'RQ-536': ('local_checked_no_answer', 'Pub. 15-B (2026) p.24 points to IRS.gov/Tax-Professionals/Standard-Mileage-Rates; no 2026 rate on disk.'),
 'RQ-409': ('local_checked_no_answer', 'Pub. 15-B (2026) p.24 points to IRS.gov/Tax-Professionals/Standard-Mileage-Rates; no 2026 rate on disk.'),
 'RQ-526': ('local_checked_no_answer', 'Local Instructions for Form 940 are the 2025 edition (Nov 18, 2025); the TY2026 edition is not on disk.'),
 'RQ-384': ('local_checked_no_answer', 'Local WI ch. 71 text (WI_stat71_2026-11-02.txt) does not contain 71.01(6) or an IRC-as-of date; paragraph not isolable from the copy.'),
 'RQ-557': ('local_checked_no_answer', 'W-2/W-3 instructions describe the ITIN as nine digits formatted like an SSN beginning with 9; no official SSN structure or never-issued ranges on disk.'),
}
c = jload('_research/qa-r3-fix/gap-local-candidates.json')
g = jload('_research/gaps.json'); gm = {x['id']: x for x in g['gaps']}
tri = collections.Counter()
for gid, v in c.items():
    x = gm.get(gid)
    if not x: continue
    if x['status'] == 'closed' and gid not in special:
        tri['already_closed'] += 1; continue
    res, why = special.get(gid, ('local_checked_no_answer', 'candidate file(s) matched the key terms only incidentally (index, menu, unrelated section); no passage answers the question'))
    x['local_triage'] = {'result': res, 'on': TODAY, 'by': 'agent 2 (QA r3b)', 'files': v['files'], 'note': why}
    x['searched'].append(f"QA r3b triage {TODAY}: {', '.join(v['files'][:4])} opened and read at the matching passages - {res}: {why}")
    if res == 'closed_from_local':
        x['status'] = 'closed'; x['closed_on'] = TODAY; x['closure_source'] = why
        x['what_would_close_it'] = 'closed: answered from the local registered copies listed in searched[]'
        x['closed_by_keys'] = [k for k in log['facts_added'] if (gid == 'RQ-509' and k.startswith('ct.wh.table_')) or (gid == 'RQ-318' and k.startswith('sc.ui.coverage'))]
    tri[res] += 1
g['counts'] = dict(collections.Counter(x['status'] for x in g['gaps']))
jsave('_research/gaps.json', g)
log['triage'] = dict(tri); log['gaps_counts'] = g['counts']

# consumed_by for rows newly cited
for rid, tok in [(ct_reg, 'CCG/annex_CT'), (sc_reg, 'CCG/annex_SC'), (or_reg, 'CCG/annex_OR'), (ein_reg, 'CCG/annex_FED')]:
    cur = [t for t in byid[rid]['consumed_by'].split(';') if t]
    if tok not in cur: byid[rid]['consumed_by'] = ';'.join(cur + [tok])
save_reg(fields, rows)
jsave('_research/qa-r3b-fix/triage-r3b-log.json', log)
print(json.dumps({k: log[k] for k in ('facts_added', 'triage', 'gaps_counts', 'ein_register_id')}, ensure_ascii=False, indent=1))
for k, v in log['ct_parse'].items(): print(k, v)
