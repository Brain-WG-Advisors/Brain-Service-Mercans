# QA r3b fix, agent 2 (source hunter). Tasks 1-6. Reads 01-ccg read-only; writes _research and register only.
import sys, json, re, glob, os, collections
sys.path.insert(0, r"C:/Users/instituto/Documents/brain-service/Research Pipeline/USA/US-compliance/_research/qa-r3-fix/scripts")
from lib import *   # chdir BASE
TODAY = '2026-11-02'
log = {'tasks': {}}
def jload(p): return json.load(open(p, encoding='utf-8'))
def jsave(p, d): open(p, 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')

def add_fact(path, fact, after_key=None):
    d = jload(path)
    if any(f['key'] == fact['key'] and f['effective_from'] == fact['effective_from'] for f in d['facts']):
        return 'exists'
    idx = len(d['facts'])
    if after_key:
        for i, f in enumerate(d['facts']):
            if f['key'] == after_key: idx = i + 1
    d['facts'].insert(idx, fact); jsave(path, d); return 'added'

# ---------- Task 2: CA ----------
ca = {"key": "ca.wh.status_table_map",
  "value": ("DE 4 filing status -> DE 44 Method B table: 'Single or Married (with two or more incomes)' -> Table 5 'Single Persons, Dual Income Married or Married with Multiple Employers'; "
            "'Married (one income)' -> Table 6 'Married Persons'; 'Head of Household' -> Table 7 'Unmarried/Head of Household' (annual payroll period; the same three-way order repeats for every payroll period in Tables 8-28). "
            "Table 1 (low income exemption) and Table 3 (standard deduction): 'Single or Married (with two or more incomes)' -> column 'Single, Dual Income Married or Married with Multiple Employers'; "
            "'Married (one income)' -> column 'Married' for '0' or '1' allowances, or column 'Married' for '2' or more allowances (allowances on DE 4 or Form W-4); 'Head of Household' -> column 'Unmarried Head of Household'. No DE 4 on file -> Single with zero allowances."),
  "effective_from": "2026-01-01", "effective_to": "2026-12-31", "register_id": "US-CAS5-001", "tier": "A.2",
  "verification_method": "inspected directly",
  "authority": "California Employment Development Department (EDD)", "url": "https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf", "confidence": "high",
  "note": ("Table titles read in the local copy 00-official-sources/pdfs/CA/de44_wb.pdf (DE 44 Rev. 52 (4-26)): PDF p.56 'Annual Payroll Period Tax Rate Tables', Method B Tables 5, 6, 7; "
           "PDF p.54 Method B Table 1 and PDF p.55 Method B Table 3 column headings; PDF p.24: no existing withholding certificate -> 'Single with Zero withholding allowance'. "
           "DE 4 status wording from DE 4 (Rev. 56 1-26) p.1 'Filing Status' [US-CAS5-015, 00-official-sources/ccg-sources/CA/CA_EDD_DE4_2026-11-02.pdf]. "
           "Consequence: a married employee who checks 'Single or Married (with two or more incomes)' is withheld on the single table (Table 5), never on Table 6."),
  "_domain": "income_tax"}
log['tasks']['2_CA'] = add_fact('_research/CCG-annex_CA-facts.json', ca, after_key='ca.pit.bracket.married.rates')

# ---------- Task 3: CO ----------
co = {"key": "co.sui.new_employer.rate.total", "value": 1.7, "unit_of_measure": "percent",
  "effective_from": "2027-01-01", "effective_to": "2027-12-31", "register_id": "US-COP51-004", "tier": "A.2",
  "verification_method": "quoted from authority page",
  "authority": "Colorado Department of Labor and Employment, UI Division",
  "url": "https://cdle.colorado.gov/ui/employers/requirements/premiums/introductory-rates", "confidence": "high",
  "note": ("2027 Introductory Rates, non-construction / general construction / trades: beginning 0.0153 + support .0017 + surcharge .00 = combined 0.0170 "
           "(page: 'The Solvency Surcharge is not in affect for the 2027 calendar year'); heavy construction 0.0406; political subdivision 0.0020. "
           "Local copy 00-official-sources/ccg-sources/CO/CO_US-COP51-004_r2-curl_2026-11-02.html. Same value as WTC-country_specific-facts.json."),
  "_domain": "social_security"}
log['tasks']['3_CO'] = add_fact('_research/CCG-annex_CO-facts.json', co, after_key='co.sui.new_employer.rate.total')

# ---------- Task 4: AL ----------
al_base = {"currency": "USD", "effective_from": "2026-01-01", "effective_to": None, "register_id": "US-ALS5-001", "tier": "A.2",
  "verification_method": "quoted from authority page", "authority": "Alabama Department of Revenue, Withholding Tax Section",
  "url": "https://www.revenue.alabama.gov/wp-content/uploads/2026/01/whbooklet_0126.pdf", "confidence": "high", "_domain": "income_tax"}
al_new = [
  ("al.wh.std_deduction.married_separate.min", 2500, "Employee claims 'Married Filing Separately (MS)' exemption: 'GI of $17,750 or more deduct $2,500'.", "al.wh.std_deduction.married_separate.max"),
  ("al.wh.std_deduction.head_of_family.min", 2500, "Employee claims 'Head of Family (H)' exemption: 'GI of $35,500 or more deduct $2,500'.", "al.wh.std_deduction.head_of_family.max"),
]
log['tasks']['4_AL'] = {}
order = ["key","value","currency","effective_from","effective_to","register_id","tier","verification_method","authority","url","confidence","note","_domain"]
for k, v, q, after in al_new:
    f = dict(al_base); f.update({"key": k, "value": v,
      "note": "ADOR withholding booklet rev. 01/2026, Formula For Computing Alabama Withholding Tax, step 2A (local copy 00-official-sources/pdfs/AL/whbooklet_0126_webfetch-20261029.pdf, PDF p.8, printed label 'PAGE 7'): " + q + " Minimum deduction per status: single 2,500 / married filing separately 2,500 / married filing jointly 5,000 / head of family 2,500."})
    f = {kk: f[kk] for kk in order}
    log['tasks']['4_AL'][k] = add_fact('_research/CCG-annex_AL-facts.json', f, after_key=after)

# ---------- Task 1: gaps ----------
g = jload('_research/gaps.json')
for x in g['gaps']:
    if x['id'] == 'RQ-545' and x['status'] != 'closed':
        x['status'] = 'closed'; x['closed_on'] = TODAY
        x['closure_source'] = 'US-FEDS5-029 (Pub. 15 (2026) sec. 15 table: 401(k)/403(b)/457(b)/SIMPLE salary reductions); US-FEDS5-008 (Pub. 15-B (2026) Table 2-1: section 125 cafeteria plan benefits)'
        x['closed_by_keys'] = ['fed.base.401k_deferral.fit', 'fed.base.401k_deferral.fica', 'fed.base.401k_deferral.futa',
                               'fed.base.section125.rule', 'fed.base.section125_health.fit', 'fed.base.section125_health.fica', 'fed.base.section125_health.futa']
        x['closed_in_facts'] = '_research/CCG-m03_gross_to_net-facts.json (same keys in _research/WTC-global_baseline-facts.json)'
        x['what_would_close_it'] = 'closed: answered by the fed.base.* facts listed in closed_by_keys'
        x['builder_note'] = ('m12 must use the fed.base.* keys (401(k) deferral: FIT wages reduced, FICA and FUTA wages unchanged; section 125 health premium: '
                             'excluded from FIT, FICA and FUTA wages) instead of the RQ-545 limitation sentence; pointer: Module 3 Step 2 [US-FEDS5-029].')
        x['searched'].append('_research/CCG-m03_gross_to_net-facts.json fed.base.* (QA r3b fix, agent 2, 2026-11-02): treatment established on US-FEDS5-029 and US-FEDS5-008')
if not any(x['id'] == 'RQ-592' for x in g['gaps']):
    g['gaps'].append({"id": "RQ-592", "key": "de.termination.separation_notice_warn",
      "subject": "RQ-592 - Does Delaware require a UI separation notice to a separating employee, and does it impose a State plant-closing / mass-layoff notice duty in addition to federal WARN (thresholds, notice period)?",
      "location": "01-ccg/annexes/annex_DE.md!DE.7!L124", "research_request_id": "RQ-592", "blocking": False, "severity": "minor",
      "searched": [
        "_research/CCG-annex_DE-facts.json facts[] and unresolved[] (no termination-notice key; unresolved de.report.sui.uc8a_format names the separation-notice duty as not read)",
        "_research/CCG-annex_DE-research-pack.md DE.7",
        "local-files sweep 2026-11-02 (agent 2, QA r3b): 37 local files of active US-DE* register rows searched for 'separation notice', 'notice of separation', 'plant closing', 'mass layoff', 'WARN', 'UC-119'",
        "lead, not an answer: 19 Del. C. 3302(10)(F) [US-DES5-010, delcode-title19-c033-sc01_2026-11-02.html] refers to 'the advance notice of a mass layoff, plant closing or relocation that is required by Chapter 19 of this title' - a State notice duty exists in 19 Del. C. ch. 19, but its text (thresholds, notice period) is not in any local file",
        "19 Del. C. 3357 [US-DEL-003 / US-DEP9V-001] mentions employer response to a separation notice only for COVID-19 claims (2020); DOL UI employer FAQs [US-DES5-011] describe Form UC-119 'Request for Separation Information' sent by the Department, not an employer-initiated notice"],
      "searched_on": TODAY,
      "what_would_close_it": "19 Del. C. ch. 19 (Delaware plant-closing provisions: coverage threshold, mass-layoff / plant-closing / relocation definitions, notice period) read on delcode.delaware.gov, and the Delaware DOL UI regulation or employer handbook stating whether the employer must hand a separation notice to the employee (form, content, deadline).",
      "status": "open", "url_searched": False, "closure_source": "19 Del. C. ch. 19 on delcode.delaware.gov; Delaware DOL Division of Unemployment Insurance employer handbook",
      "local_searched": True, "_origin": "artifact-builder r3b request RQ-592; gaps entry added by agent 2 (QA r3b minor finding 4)"})
g['counts'] = dict(collections.Counter(x['status'] for x in g['gaps']))
if 'QA r3b fix' not in g['generated_by']: g['generated_by'] = g['generated_by'].rstrip() + ' + QA r3b fix'
jsave('_research/gaps.json', g)
log['tasks']['1_gaps'] = g['counts']

# ---------- Task 5/6: register ----------
fields, rows = load_reg()
byid = {r['id']: r for r in rows}
need = collections.defaultdict(set)
for fn in facts_files():
    d = jload(fn); tok = d['artifact'] + ('/' + d['unit'] if d.get('unit') else '')
    for f in d['facts']: need[f['register_id']].add(tok)
    for rid in set(re.findall(r'\bUS-[A-Z0-9]+-\d{3}\b', json.dumps(d['facts']))): need[rid].add(tok)
    for rid in set(re.findall(r'\bUS-[A-Z0-9]+-\d{3}\b', json.dumps(d.get('coverage_matrix', '')))): need[rid].add(tok)
rid_re = re.compile(r'\bUS-[A-Z0-9]+-\d{3}\b')
for p in glob.glob('01-ccg/annexes/*.md') + glob.glob('01-ccg/modules/*.md'):
    stem = os.path.splitext(os.path.basename(p))[0]
    for rid in set(rid_re.findall(open(p, encoding='utf-8').read())):
        need[rid].add('CCG/' + stem)
changed = {}; unknown = []
for rid, toks in need.items():
    r = byid.get(rid)
    if not r: unknown.append(rid); continue
    cur = [t for t in (r['consumed_by'] or '').split(';') if t.strip()]
    add = sorted(t for t in toks if t not in cur)
    if add:
        r['consumed_by'] = ';'.join(cur + add); changed[rid] = add
log['tasks']['5_consumed_by'] = {'rows_changed': len(changed), 'rows_gaining_a_CCG_token': sum(1 for v in changed.values() if any(t.startswith('CCG') for t in v)),
    'unknown_register_ids_cited': sorted(set(unknown)), 'US-FEDQ1-005': byid['US-FEDQ1-005']['consumed_by'],
    'US-FEDQ3-001': byid['US-FEDQ3-001']['consumed_by'], 'US-FEDQ3-004': byid['US-FEDQ3-004']['consumed_by']}
log['consumed_by_changes'] = changed

usc_tail = '; amendments after the 2024 edition (e.g. Pub. L. 119-21 of 2025) are not in the local copy; the section text is in force as at retrieved_on'
ef = {
 'US-FEDQ3-001': ('2018-01-01', "26 U.S.C. 3401 as printed in the 2024 edition: latest amendment Pub. L. 115-97, applicable to taxable years beginning after Dec. 31, 2017 (Effective Date of 2017 Amendment note in the local copy)" + usc_tail),
 'US-FEDQ3-002': ('2020-01-01', "26 U.S.C. 3121 as printed in the 2024 edition: latest amendment Pub. L. 116-94, applicable to taxable years beginning after Dec. 31, 2019 (Effective Date of 2019 Amendment note)" + usc_tail),
 'US-FEDR2-001': ('2020-01-01', "26 U.S.C. 3121 as printed in the 2024 edition: latest amendment Pub. L. 116-94, applicable to taxable years beginning after Dec. 31, 2019 (Effective Date of 2019 Amendment note)" + usc_tail),
 'US-FEDQ3-003': ('2014-12-19', "26 U.S.C. 3306 as printed in the 2024 edition: latest amendment Pub. L. 113-295, effective Dec. 19, 2014 (Effective Date of 2014 Amendment note)" + usc_tail),
 'US-FEDR2-002': ('2014-12-19', "26 U.S.C. 3306 as printed in the 2024 edition: latest amendment Pub. L. 113-295, effective Dec. 19, 2014 (Effective Date of 2014 Amendment note)" + usc_tail),
 'US-FEDR2-003': ('2014-12-19', "26 U.S.C. 3101 as printed in the 2024 edition: latest amendment Pub. L. 113-295, effective Dec. 19, 2014 (Effective Date of 2014 Amendment note)" + usc_tail),
 'US-FEDR2-004': ('2023-01-01', "26 U.S.C. 3111 as printed in the 2024 edition: latest amendment Pub. L. 117-169, applicable to taxable years beginning after Dec. 31, 2022 (Effective Date of 2022 Amendment note)" + usc_tail),
 'US-FED-028': ('2024-01-01', "revision date printed on the form (Rev. 1-2024); the form states no separate effective date"),
 'US-AKS5-009': ('2024-08-01', "revision date printed on the form (CIV-530 (8/24)); the form states no separate effective date"),
 'US-UTP6-002': ('2026-09-01', "revision date printed on the form (TC-737 rev. 09/26); the form states no separate effective date"),
 'US-UTP6-003': ('2024-08-01', "revision date printed on the form (Rev. 08/24); the form states no separate effective date"),
 'US-LAP6-001': ('1988-06-27', "date the repeal took effect: 'Repealed by Acts 1988, No. 18, 1; Acts 1988, No. 90, 1, eff. June 27, 1988' (local copy)"),
}
log['tasks']['6_effective_from'] = {}
for rid, (d, why) in ef.items():
    r = byid[rid]; old = r['effective_from']
    if not old:
        r['effective_from'] = d
        vm = re.sub(r'\s*\|\s*effective_from not (stated in the instrument; in force as at retrieved_on|set:[^|]*?)\s*\((QA r[0-9a-z]+ note)\)', '', r['verification_method'])
        r['verification_method'] = vm + ' | effective_from ' + d + ': ' + why + ' (QA r3b fix)'
    log['tasks']['6_effective_from'][rid] = [old, r['effective_from']]
r = byid['US-TXB5-301']
if 'QA r3b' not in r['verification_method']:
    r['verification_method'] += ' | effective_from deliberately empty: proposed rule, not adopted and not in force as at retrieved_on 2026-11-02; no date exists to record (QA r3b fix)'
r = byid['US-NH-001']
if 'r3b' not in r['verification_method']:
    r['verification_method'] += ' | QA r3b re-try 2026-11-02: WebFetch of the NHDRA notice HTTP 403; verified_on still empty on purpose'
still = [x['id'] for x in rows if x['status'] == 'active' and not x['effective_from'] and any(t.startswith('CCG') for t in x['consumed_by'].split(';'))
         and 'in force as at retrieved_on' not in x['verification_method'] and 'deliberately empty' not in x['verification_method']]
log['tasks']['6_still_empty_no_note'] = still
save_reg(fields, rows)
jsave('_research/qa-r3b-fix/apply-r3b-log.json', log)
print(json.dumps(log['tasks'], ensure_ascii=False, indent=1)[:4000])
