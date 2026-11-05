import sys, json, collections; sys.path.insert(0, '.')
from lib import *
from fmt import dump
os.chdir(BASE)
TODAY = '2026-11-02'
fields, R = load_reg(); byid = {r['id']: r for r in R}
facts = {os.path.basename(fn): json.load(open(fn, encoding='utf-8')) for fn in facts_files()}
log = []
rev = json.load(open('_qa/CCG-review-r2.json', encoding='utf-8'))

# ---- item 5: 198 rows, no effective_from and no note
NOTE = 'effective_from not stated in the instrument; in force as at retrieved_on (QA r2 note)'
for rid in rev['findings'][31]['_rows']:
    r = byid[rid]
    if not r['effective_from'].strip() and 'in force as at retrieved_on' not in r['verification_method']:
        r['verification_method'] = (r['verification_method'] + ' | ' + NOTE).strip(' |'); log.append(('note_added', rid))

# ---- item 1: NRA FICA / FUTA / totalization
def md5(p): return hashlib.md5(open(p, 'rb').read()).hexdigest()
F = '00-official-sources/ccg-sources/FED/'
NEW = [
 ('US-FEDR2-001', 'social_security', '26 U.S.C. 3121(b)(19) FICA employment exclusion - nonresident aliens in F, J, M or Q status (U.S. Code 2024 ed., govinfo)', 'statute', 'A.1', 'U.S. Congress (OLRC/GPO, govinfo)',
  'https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleC-chap21-subchapC-sec3121.htm', '3121(b)(19); 3121(b)(C) (service designated as employment under a section 233 SSA agreement)',
  'Excluded from FICA employment: service performed by a nonresident alien temporarily present as a nonimmigrant under INA 101(a)(15)(F), (J), (M) or (Q), performed to carry out the purpose of that status.', F + 'FED_USC-26-3121_govinfo-2024_2026-11-02.htm'),
 ('US-FEDR2-002', 'social_security', '26 U.S.C. 3306(c)(19) FUTA employment exclusion - nonresident aliens in F, J, M or Q status (U.S. Code 2024 ed., govinfo)', 'statute', 'A.1', 'U.S. Congress (OLRC/GPO, govinfo)',
  'https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleC-chap23-sec3306.htm', '3306(c)(19)',
  'Excluded from FUTA employment: the same F/J/M/Q nonresident-alien service performed to carry out the purpose of admission.', F + 'FED_USC-26-3306_govinfo-2024_2026-11-02.htm'),
 ('US-FEDR2-003', 'social_security', '26 U.S.C. 3101(c) Relief from FICA employee tax in cases covered by international (totalization) agreements (U.S. Code 2024 ed., govinfo)', 'statute', 'A.1', 'U.S. Congress (OLRC/GPO, govinfo)',
  'https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleC-chap21-subchapA-sec3101.htm', '3101(c)',
  'While a section 233 SSA agreement is in effect, wages are exempt from the employee FICA tax to the extent they are subject under the agreement exclusively to the foreign social security system.', F + 'FED_USC-26-3101_govinfo-2024_2026-11-02.htm'),
 ('US-FEDR2-004', 'social_security', '26 U.S.C. 3111(c) Relief from FICA employer tax in cases covered by international (totalization) agreements (U.S. Code 2024 ed., govinfo)', 'statute', 'A.1', 'U.S. Congress (OLRC/GPO, govinfo)',
  'https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleC-chap21-subchapB-sec3111.htm', '3111(c)',
  'Employer counterpart of 3101(c): wages subject exclusively to the foreign system under a section 233 agreement are exempt from the employer FICA tax.', F + 'FED_USC-26-3111_govinfo-2024_2026-11-02.htm')]
for rid, dom, name, typ, tier, auth, url, art, fig, lf in NEW:
    assert rid not in byid and os.path.exists(lf)
    row = dict.fromkeys(fields, '')
    row.update(id=rid, domain=dom, instrument_name=name, instrument_type=typ, tier=tier, authority=auth, url=url, article_or_section=art, publication_date='2024-01-01',
               figure_or_rule_carried=fig, language='en', local_file=lf, retrieved_on=TODAY, verified_on=TODAY,
               verification_method=f'quoted from authority page | md5 {md5(lf)} | ' + NOTE, consumed_by='CCG/m05_social_security;CCG/annex_FED', status='active')
    R.append(row); byid[rid] = row; log.append(('row_added', rid))
p515 = byid['US-FEDS5-016']
p515['verification_method'] += (' | QA r2 2026-11-02: NRA social security read in the local PDF - p.53 "Social security and Medicare taxes" (F-1/J-1/M-1/Q not subject to FICA) and'
    ' "Federal unemployment tax (FUTA)" (F/J/M/Q not subject to FUTA); p.55 "Social security and Medicare taxes" under students/teachers (purpose-of-admission test, CPT/OPT, resident-alien'
    ' carve-back, other nonimmigrant visas fully liable unless a totalization agreement exemption applies; SSA agreement texts at SSA.gov/international/totalization_agreements.html)')
for t in ('CCG/m05_social_security', 'CCG/annex_FED'):
    if t not in p515['consumed_by'].split(';'): p515['consumed_by'] += ';' + t
P515 = dict(register_id='US-FEDS5-016', tier='A.2', authority='IRS', url='https://www.irs.gov/pub/irs-pdf/p515.pdf')
def fact(key, value, rid, vm, conf, note, extra=None):
    r = byid[rid]
    f = {'key': key, 'value': value, 'effective_from': '2026-01-01', 'effective_to': None, 'register_id': rid, 'tier': r['tier'], 'verification_method': vm,
         'authority': r['authority'], 'url': r['url'], 'confidence': conf}
    if note: f['note'] = note
    return f
NRA = [
 fact('fed.fica.nra.fjmq_exempt', True, 'US-FEDR2-001', 'second independent authority', 'high',
      'Applies only to pay for services performed to carry out the purpose of the F/J/M/Q admission (IRS Pub. 515 (2026) agrees, incl. authorized CPT/OPT); employee and employer FICA both not due. Level: payroll withholding and employer contribution.'),
 fact('fed.fica.nra.fjmq_exempt.scope', 'Exempt: pay of a nonresident alien in F-1, J-1, M-1 or Q status for services that carry out the purpose of admission, on or off campus, including authorized Curricular and Optional Practical Training. Not exempt: other employment of the same person (e.g. an unrelated part-time job), and any pay once the person is a resident alien.',
      'US-FEDS5-016', 'quoted from authority page', 'high', None),
 fact('fed.futa.nra.fjmq_exempt', True, 'US-FEDR2-002', 'second independent authority', 'high',
      'IRC 3306(c)(19) and IRS Pub. 515 (2026): wages of F/J/M/Q nonresident aliens are not subject to FUTA. State UI coverage follows each state statute separately.'),
 fact('fed.fica.nra.other_visas.liable', True, 'US-FEDS5-016', 'quoted from authority page', 'high',
      'Nonresident aliens on other nonimmigrant visas (e.g. H-1B, L-1) or in refugee/asylee status are fully liable for social security and Medicare unless a totalization agreement exemption applies.'),
 fact('fed.fica.totalization.exemption_rule', 'Wages are exempt from employee FICA (IRC 3101(c)) and employer FICA (IRC 3111(c)) while a section 233 Social Security Act agreement is in effect, to the extent the agreement makes them subject exclusively to the foreign social security system.',
      'US-FEDR2-003', 'second independent authority', 'high',
      'Employer FICA counterpart: IRC 3111(c) (register US-FEDR2-004). The list of agreements in force and the certificate-of-coverage procedure are SSA documents not held locally (see unresolved).')]
for fn in ('CCG-m05_social_security-facts.json', 'CCG-annex_FED-facts.json'):
    d = facts[fn]; have = {f['key'] for f in d['facts']}
    for f in NRA:
        if f['key'] not in have: d['facts'].append(dict(f)); log.append(('fact_added', fn, f['key']))
    if 'fed.fica.totalization.agreements_in_force' not in {u['key'] for u in d['unresolved']}:
        d['unresolved'].append({'key': 'fed.fica.totalization.agreements_in_force',
            'why': 'The list of totalization agreements in force and the certificate-of-coverage procedure are published by SSA; ssa.gov returns HTTP 403 to curl from a non-US exit (2026-11-02).',
            'attempted': ['https://www.ssa.gov/international/agreements_overview.html - HTTP 403 (2026-11-02)', 'https://www.ssa.gov/international/status.html - HTTP 403 (2026-11-02)'],
            'what_would_close_it': 'SSA Office of International Programs pages "U.S. International Social Security Agreements" (ssa.gov/international/agreements_overview.html) and the certificate-of-coverage page, read from a US exit or a browser pass.',
            'blocking': False}); log.append(('unresolved_added', fn, 'fed.fica.totalization.agreements_in_force'))

# ---- item 7: OH path in fact value; IA MANUAL statement
for fn, d in facts.items():
    for f in d['facts']:
        if f['key'] == 'oh.pit.school_district.full_list' and isinstance(f['value'], str) and '00-official-sources' in f['value']:
            v = re.sub(r'[;,.]?\s*local file\s+00-official-sources/\S+', '', f['value']).rstrip(' ;,')
            f['value'] = v + ('' if v.endswith('.') else '.'); log.append(('oh_path_stripped', fn))
UNR = {
 'CCG-annex_IA-facts.json': [('ia.pfml.state_program.none', 'The statement that Iowa has no state SDI/TDI/PFML programme rests only on the US DOL Women\'s Bureau summary (US-IAP52-004, tier B); a negative cannot be proved from an Iowa A-tier source on disk.', ['US DOL Women\'s Bureau paid-leave page (US-IAP52-004)'], 'An Iowa Workforce Development or Iowa Code statement on paid family/medical or disability leave; otherwise state it as "no Iowa programme identified" in the limitation list.')],
 'CCG-annex_KY-facts.json': [('ky.garn.child_support.iwo_fee_per_payment', 'The 1 USD per-payment IWO fee rests only on a secondary source (US-KYS5-026).', ['US-KYS5-026 (secondary)'], 'KRS 405.465 text (apps.legislature.ky.gov) or the Kentucky Child Support Services employer guide.'),
                             ('ky.garn.child_support.lump_sum.reporting_threshold', 'The 150 USD lump-sum reporting threshold for employers with 20 or more employees rests only on a secondary source (US-KYS5-026).', ['US-KYS5-026 (secondary)'], 'KRS 405.465 / 403.215 text or the Kentucky Child Support Services employer guide.')],
 'CCG-annex_HI-facts.json': [('hi.garn.child_support.remit_working_days', 'FEN125 (2003) timing figures (remit within 5 working days after payday; start within 7 business days) are cited from a secondary description of the form, not from the CSEA form or HRS 576D on disk.', ['US-HIS5-022 (CSEA page, fee only)'], 'HRS 576D-14/576E-16 text (capitol.hawaii.gov) or the CSEA employer handbook.')],
 'CCG-annex_IN-facts.json': [('in.garn.statute_move.effective_date', 'The 2026-07-01 effective date of the move of the garnishment limit to IC 37-2-6-4 (P.L.115-2026) is stated only by a secondary source.', ['US-INS5-020 local copy (IC Title 22 Article 2 2026)'], 'P.L.115-2026 enrolled act text (iga.in.gov) showing the effective-date section.')],
 'CCG-annex_LA-facts.json': [('la.sui.wage_base.mechanism', 'The R.S. 23:1536 wage-base mechanism was not read; the 7,700 (2025) figure in the text comes from a secondary source.', ['US-LAP9V-001 (LWC 2026 page, 7,000 only)'], 'R.S. 23:1536 text (legis.la.gov, unreachable from a non-US exit on 2026-11-02, curl 000) or the LWC 2025 rate notice.')],
 'CCG-annex_MA-facts.json': [('ma.pit.ballot_ip25_18.rate', 'The 4.67% (2027) rate of initiative petition IP 25-18 and its exclusion from the ballot (SJC-13885) rest on a secondary source; the SJC opinion URL returned 404.', ['US-MAS5-027 (secondary)'], 'The SJC-13885 opinion (mass.gov/sjc) or the Secretary of the Commonwealth 2026 ballot question list.')],
 'CCG-annex_GA-facts.json': [('ga.ui.rate_exclusion.thresholds', 'The 40,000 sales (and related) thresholds for state UI rate exclusions rest only on a secondary source.', ['GA DOL pages read in stage 5 (no threshold stated)'], 'O.C.G.A. 34-8-35 / 34-8-151 text or Georgia DOL Rule 300-2-x on employer rate exclusions.')]}
for fn, items in UNR.items():
    d = facts[fn]; have = {u['key'] for u in d['unresolved']}
    for key, why, att, close in items:
        if key in have: continue
        d['unresolved'].append({'key': key, 'why': why + ' (QA r2 2026-11-02: the number must be removed from the CCG text and carried as a limitation.)', 'attempted': att, 'what_would_close_it': close, 'blocking': False})
        log.append(('unresolved_added', fn, key))
save_reg(fields, R)
for fn, d in facts.items(): dump(d, '_research/' + fn, '_research/qa-r2-fix/_backup/' + fn)
json.dump(log, open('_research/qa-r2-fix/apply3-log.json', 'w', encoding='utf-8'), indent=0, ensure_ascii=False)
print(collections.Counter(x[0] for x in log)); print([x for x in log if x[0] != 'note_added'][:40])
