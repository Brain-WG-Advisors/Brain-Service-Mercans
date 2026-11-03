"""QA r1b (agent 2): items 3 and 4 - facts for the S5B-P3 rows and the CT per-period tables.
Usage: python -I r1b_facts.py <BASE>
Rewrites (backups in _research/qa-r1-fix/_backup2/): CCG-annex_{CA,CO,DE,DC,NY,TX,IL,NM,MI,MA,WV,CT}-facts.json,
WTC-country_specific-facts.json; appends consumed_by in the register; writes r1b_facts.log."""
import csv, json, os, sys, collections

BASE = sys.argv[1]
R = os.path.join(BASE, '_research')
REG = os.path.join(BASE, '00-official-sources', 'legal-basis-register.csv')
TODAY = '2026-11-02'
log = []
L = lambda *a: log.append(' | '.join(str(x) for x in a))

with open(REG, encoding='utf-8', newline='') as fh:
    rd = csv.DictReader(fh); COLS = rd.fieldnames; reg = list(rd)
RX = {r['id']: r for r in reg}

def F(key, value, eff, rid, vm='quoted from authority page', conf='high', to=None, unit=None, cur=None, note=None, level=None):
    r = RX[rid]
    f = {'key': key, 'value': value}
    if cur: f['currency'] = cur
    if unit: f['unit_of_measure'] = unit
    f.update({'effective_from': eff, 'effective_to': to, 'register_id': rid, 'tier': r['tier'], 'verification_method': vm,
              'authority': r['authority'], 'url': r['url'], 'confidence': conf})
    if note: f['note'] = note
    if level: f['_level'] = level
    f['_qa_r1b'] = TODAY
    return f

def U(key, why, close, attempted, blocking):
    return {'key': key, 'why': why, 'attempted': attempted, 'what_would_close_it': close, 'blocking': blocking, '_qa_r1b': TODAY}

P3 = 'browser pass P3 2026-11-02 (_research/stage5/browser-pass-P3.md)'
files = {}
def load(name):
    if name not in files:
        files[name] = json.load(open(os.path.join(R, name), encoding='utf-8'))
    return files[name]

def unit_of(name):
    d = load(name)
    return 'WTC/' + d['unit'] if name.startswith('WTC') else 'CCG/' + d['unit']

def add(name, facts, drop_keys=(), replace=None):
    d = load(name)
    if replace:
        for f in d['facts']:
            if (f['key'], f['effective_from'], f['register_id']) in replace:
                old = dict(f); f.clear(); f.update(replace[(old['key'], old['effective_from'], old['register_id'])])
                L('FACT replaced', name, old['key'], repr(old['value'])[:80], '->', repr(f['value'])[:80], old['register_id'], '->', f['register_id'])
    have = {(f['key'], f['effective_from']) for f in d['facts']}
    for f in facts:
        assert (f['key'], f['effective_from']) not in have, (name, f['key'], f['effective_from'])
        d['facts'].append(f); have.add((f['key'], f['effective_from']))
        L('FACT added', name, f['key'], repr(f['value'])[:70], f['effective_from'], f['register_id'])

def unres(name, close=(), narrow=None, new=()):
    d = load(name)
    keep = []
    for u in d['unresolved']:
        if u['key'] in close:
            L('UNRESOLVED closed', name, u['key']); continue
        if narrow and u['key'] in narrow:
            n = narrow[u['key']]
            for k in ('why', 'what_would_close_it', 'blocking'):
                if k in n: u[k] = n[k]
            u['attempted'] = list(u.get('attempted') or []) + [n['attempt']]
            u['_qa_r1b'] = 'narrowed ' + TODAY
            L('UNRESOLVED narrowed', name, u['key'], 'blocking=%s' % u.get('blocking'))
        keep.append(u)
    for u in new:
        keep.append(u); L('UNRESOLVED added', name, u['key'], 'blocking=%s' % u['blocking'])
    d['unresolved'] = keep

# ------------------------------------------------------------------ CA
ca = 'CCG-annex_CA-facts.json'
cf = [F('ca.minwage.fast_food.hourly', 20.0, '2024-04-01', 'US-CAB5-302', cur='USD',
        note='Fast-food restaurant employees (Lab. Code 1474, AB 1228). The DIR Minimum Wage page and Fast Food FAQ read 2026-11-02 show no Fast Food Council increase after 2024-04-01. Exempt-salary test for these employees: 2 x 20.00 x 40 x 52 = 83,200 (FAQ).')]
HC = {  # category key: (label, [(from, to, value)]) - DIR Health Care Worker Minimum Wage FAQ, full schedule table
 'large_system': ('Hospital or integrated health system with 10,000+ FTE (incl. SNFs they operate)', [('2025-07-01', '2026-06-30', 24.0), ('2026-07-01', '2027-12-31', 25.0)]),
 'dialysis_clinic': ('Dialysis clinics', [('2025-07-01', '2026-06-30', 24.0), ('2026-07-01', '2027-12-31', 25.0)]),
 'safety_net_hospital': ('Safety-net hospitals (FAQ 14)', [('2025-07-01', '2026-06-30', 18.63), ('2026-07-01', '2027-06-30', 19.28), ('2027-07-01', '2028-06-30', 19.95), ('2028-07-01', '2029-06-30', 20.65), ('2029-07-01', '2030-06-30', 21.37), ('2030-07-01', '2031-06-30', 22.12), ('2031-07-01', '2032-06-30', 22.89), ('2033-07-01', '2034-12-31', 25.0)]),
 'clinic': ('Intermittent, community or rural health clinics and associated urgent care', [('2024-10-16', '2026-06-30', 21.0), ('2026-07-01', '2027-06-30', 22.0), ('2027-07-01', '2028-12-31', 25.0)]),
 'other_facility': ('All other covered health care facilities not run by counties', [('2024-10-16', '2026-06-30', 21.0), ('2026-07-01', '2028-06-30', 23.0), ('2028-07-01', '2029-12-31', 25.0)]),
 'county_large': ('Covered facilities run by large counties (>5 million people at 2023-01-01)', [('2025-07-01', '2026-06-30', 24.0), ('2026-07-01', '2027-12-31', 25.0)]),
 'county_medium': ('Covered facilities run by medium counties (250,000-5 million)', [('2025-01-01', '2026-06-30', 21.0), ('2026-07-01', '2028-06-30', 23.0), ('2028-07-01', '2029-12-31', 25.0)]),
 'county_small': ('Covered facilities run by small counties (<250,000)', [('2025-07-01', '2026-06-30', 18.63), ('2026-07-01', '2027-06-30', 19.28), ('2027-07-01', '2028-06-30', 19.95), ('2028-07-01', '2029-06-30', 20.65), ('2029-07-01', '2030-06-30', 21.37), ('2030-07-01', '2031-06-30', 22.12), ('2031-07-01', '2032-06-30', 22.89), ('2032-07-01', '2033-06-30', 23.69), ('2033-07-01', '2034-12-31', 25.0)]),
}
for k, (label, sched) in HC.items():
    for fr, to, v in sched:
        n = label + '. SB 525 / Lab. Code 1182.14-1182.16 schedule as shown in the DIR Labor Commissioner FAQ (A.3: an FAQ page, upgrade to the statute text if QA P2 flags it).'
        if k == 'safety_net_hospital' and fr == '2033-07-01':
            n += ' The FAQ table lists no safety-net step for 2032-07-01..2033-06-30 (the small-county column lists 23.69 there); transcribed as printed.'
        cf.append(F('ca.minwage.health_care.%s.hourly' % k, v, fr, 'US-CAB5-301', cur='USD', to=to, conf='high', note=n))
cf.append(F('ca.minwage.health_care.indexation', 'CPI adjustment each January 1 after the last scheduled step (large systems, dialysis and large counties from 2028-01-01; clinics 2029-01-01; other facilities and medium counties 2030-01-01; safety-net and small counties 2035-01-01). Skilled nursing facilities outside a hospital/system: schedule applies only once a patient-care minimum spending requirement is passed.', '2024-10-16', 'US-CAB5-301'))
LOC = [('los_angeles_city', 'US-CAB5-303', [('2025-07-01', '2026-06-30', 17.87), ('2026-07-01', None, 18.42)], 'City of Los Angeles, all employers (LAMC 187.02; CPI-W LA each July 1, announced Feb 1).'),
       ('los_angeles_county_unincorporated', 'US-CAB5-304', [('2025-07-01', '2026-06-30', 17.81), ('2026-07-01', None, 18.47)], 'Unincorporated LA County (County Code 8.100.040). G-DERIVE: 17.81 x 1.037 = 18.469 -> 18.47 (the notice states a 3.7% CPI increase); 17.27 x 1.031 = 17.805 -> 17.81 (FY2025-26 notice, 3.1%).'),
       ('san_francisco', 'US-CAB5-305', [('2025-07-01', '2026-06-30', 19.18), ('2026-07-01', None, 19.61)], 'SF Minimum Wage Ordinance (L.E.C. Art. 1.4), CPI each July 1.'),
       ('san_diego', 'US-CAB5-306', [('2026-01-01', '2026-12-31', 17.75), ('2027-01-01', None, 18.35)], 'Employees working 2+ hours a week in the City; tips do not count (SDMC ch. 3 art. 9 div. 1).'),
       ('berkeley', 'US-CAB5-307', [('2025-07-01', '2026-06-30', 19.18), ('2026-07-01', None, 19.61)], 'Employees working 2+ hours in Berkeley; the City Living Wage (20.01 / 23.33 from 2026-07-01) binds city contractors only and is not a general minimum.'),
       ('oakland', 'US-CAB5-308', [('2026-01-01', None, 17.34)], 'OMC ch. 5.92, employees working 2+ hours a week; 2027 rate not yet on the page (verbatim Chrome excerpt; curl 403).')]
for city, rid, sched, note in LOC:
    for fr, to, v in sched:
        vm = 'derived arithmetically' if city == 'los_angeles_county_unincorporated' else 'quoted from authority page'
        cf.append(F('ca.local_minwage.%s.hourly' % city, v, fr, rid, vm=vm, cur='USD', to=to, note=note))
cf.append(F('ca.local_minwage.san_francisco.government_supported.hourly', 17.35, '2026-07-01', 'US-CAB5-305', cur='USD', note='Government Supported Employees rate (SF OLSE historical rates, 2026).'))
add(ca, cf)
unres(ca, close={'ca.industry_minwage.fast_food_health_care'},
      narrow={'ca.local_minwage.hourly': {'why': 'Six local minimums are now facts (LA City, LA County unincorporated, SF, San Diego, Berkeley, Oakland). San Jose stays unread: its site is Akamai-blocked to Chrome and curl from the Brazil exit; other CA localities with their own minimum (DIR keeps no list) are not inventoried from an official list.',
                                          'what_would_close_it': 'San Jose Office of Equality Assurance minimum wage notice for 2026 and 2027 (sanjoseca.gov), read from a US exit; then any further city the client footprint needs.',
                                          'blocking': True, 'attempt': P3 + ': LA City, LA County, SF, San Diego, Berkeley, Oakland read (US-CAB5-303..308); San Jose blocked (Akamai)'}})

# ------------------------------------------------------------------ CO
co = 'CCG-annex_CO-facts.json'
add(co, [
    F('co.famli.employee.rate', 0.43, '2027-01-01', 'US-COB5-301', vm='derived arithmetically', conf='medium', unit='percent',
      note='Maximum employee share 2027: 0.86% x 50% = 0.43%. The 0.86% total is on the CDLE bulletin of 2026-09-30; the 50% employee cap is the standing rule on famli.colorado.gov (US-COB5-003, 2026 page) and is not restated in the bulletin.'),
    F('co.famli.employer.rate', 0.43, '2027-01-01', 'US-COB5-301', vm='derived arithmetically', conf='medium', unit='percent',
      note='0.86% - 0.43% employee share = 0.43%, for employers with 10+ employees that deduct the full employee share. Employers with 9 or fewer employees owe no employer share (co.famli.small_employer.max_employees, open-ended).'),
    F('co.local_minwage.boulder_county_unincorporated.hourly', 16.82, '2026-01-01', 'US-COB5-302', to='2026-12-31', cur='USD', note='Unincorporated Boulder County (ordinance amended November 2025).'),
    F('co.local_minwage.boulder_county_unincorporated.hourly', 17.43, '2027-01-01', 'US-COB5-302', cur='USD'),
    F('co.local_minwage.boulder_city.hourly', 16.82, '2026-01-01', 'US-COB5-303', to='2026-12-31', cur='USD', note='City of Boulder Ord. 8664 schedule: 15.57 (2025), 16.82 (2026), 18.17 (2027), CPI from 2028.'),
    F('co.local_minwage.boulder_city.hourly', 18.17, '2027-01-01', 'US-COB5-303', cur='USD', conf='medium', note='From the Ord. 8664 FAQ written for the 2025 launch; no later City amendment found (the County lowered its own 2027 step to 17.43 in Nov 2025). Re-check before 2027-01-01.'),
])
for f in load(co)['facts']:
    if f['key'] == 'co.famli.total.rate' and f['effective_from'] == '2027-01-01':
        f['note'] = '2027 total (CDLE FAMLI Business Brief 2026-09-30; the same bulletin is also registered as US-COB5-301, P3 copy). Split: co.famli.employee.rate / co.famli.employer.rate 2027 (derived, 50% cap).'
        L('FACT note updated', co, 'co.famli.total.rate 2027')
unres(co, narrow={
    'co.famli.split.next_year': {'why': '2027 total 0.86% is published (CDLE bulletin, US-COS5-008 / US-COB5-301) and the 2027 split 0.43/0.43 is derived from the standing 50% employee cap read on the 2026 employer page (US-COB5-003). Not read: an A.1 text of the 50% cap and the small-employer exemption (C.R.S. 8-13.3-507, 7 CCR 2702-3).',
                                 'what_would_close_it': 'C.R.S. 8-13.3-507 or 7 CCR 2702-3 text (Colorado Register / famli.colorado.gov), only to upgrade the split from derived to A.1.',
                                 'blocking': False, 'attempt': P3 + ': CDLE bulletin 2026-09-30 read (0.86% from 2027-01-01, US-COB5-301)'},
    'co.local_minwage.other_cities': {'why': 'City of Boulder and unincorporated Boulder County 2026/2027 are now facts (US-COB5-302/-303). Edgewater 2026 (lead 18.17) and Denver 2027 (lead 19.84) still rest only on tier-B leads (US-COS5-011 MANUAL): edgewaterco.com returns Akamai 403 and denvergov.org a WAF block from the Brazil exit.',
                                      'what_would_close_it': 'City of Edgewater minimum wage ordinance/notice for 2026 and the Denver Labor 2027 minimum wage notice, read from a US exit.',
                                      'blocking': True, 'attempt': P3 + ': Boulder County and City of Boulder read; Edgewater blocked (Akamai 403); Denver not retried (WAF)'}})
wtc = 'WTC-country_specific-facts.json'
add(wtc, [F('co.famli.employee.rate', 0.43, '2027-01-01', 'US-COB5-301', vm='derived arithmetically', conf='medium', unit='percent', note='0.86% x 50% employee cap (cap on US-COB5-003). Same fact as CCG annex_CO.'),
          F('co.famli.employer.rate', 0.43, '2027-01-01', 'US-COB5-301', vm='derived arithmetically', conf='medium', unit='percent', note='Employers with 10+ employees; 9 or fewer owe no employer share. Same fact as CCG annex_CO.')])
unres(wtc, narrow={'co.famli.split.2027': {'why': '2027 split now carried as derived facts co.famli.employee.rate / co.famli.employer.rate (0.43 / 0.43 from 2027-01-01); only the A.1 text of the 50% cap is unread.', 'what_would_close_it': 'C.R.S. 8-13.3-507 or 7 CCR 2702-3 text.', 'blocking': False, 'attempt': P3 + ': CDLE bulletin 2026-09-30 (US-COB5-301)'}})

# ------------------------------------------------------------------ DE
de = 'CCG-annex_DE-facts.json'
cert = "Delaware W-4 (Employee's Withholding Allowance Certificate, Division of Revenue). A federal W-4 of 2020 or later may NOT be accepted for Delaware withholding; a federal W-4 completed before 2020 may still be relied on."
old_de = [f for f in load(de)['facts'] if f['key'] == 'de.wh.certificate'][0]
add(de, [F('de.wh.certificate.default_and_copies', 'No certificate: withhold as single with no allowances. Send copies to the Division within 5 working days when an employee claims 14+ allowances, or claims exempt with wages expected above 168.50 a week. Nonresidents: worksheet W-4NR.', '2025-01-01', 'US-DES5-006',
          note='Employer\'s Guide (live page, sections 13-17). Split out of the old de.wh.certificate value in QA r1b, which carried these rules on the FAQ row US-DES5-008.')],
    replace={(old_de['key'], old_de['effective_from'], old_de['register_id']): F('de.wh.certificate', cert, '2020-01-01', 'US-DEB5-301', note='Corrected in QA r1b (was "federal W-4", US-DES5-008): the DOR FAQ answers "No" to accepting a 2020-version federal W-4 for Delaware withholding. The Employer\'s Guide (US-DES5-006) still uses pre-2020 W-4/allowance wording. Default without a certificate and the copy-to-Division rule: de.wh.certificate.default_and_copies.', level='withholding')})
unres(de, close={'de.wh.w4_2020_mapping'})
old_w = [f for f in load(wtc)['facts'] if f['key'] == 'de.sit.certificate'][0]
add(wtc, [], replace={(old_w['key'], old_w['effective_from'], old_w['register_id']): F('de.sit.certificate', cert, '2020-01-01', 'US-DEB5-301', note='Corrected in QA r1b (was "federal W-4 (exemption mapping for 2020+ W-4 open)", US-DES5-008). Same value as CCG de.wh.certificate.', level='withholding')})

# ------------------------------------------------------------------ DC
dc = 'CCG-annex_DC-facts.json'
add(dc, [F('dc.live.fy2027_bsa_permanent', 'B26-0661 Fiscal Year 2027 Budget Support Act of 2026: enacted without the Mayor\'s signature 2026-08-14 as D.C. Act 26-418 (73 DCR 11735); transmitted to Congress 2026-08-20; D.C. Law 26-189 effective 2026-10-02 (73 DCR 13120). Status: IN FORCE (congressional review complete), before the emergency Act 26-416 lapses.', '2026-10-02', 'US-DCB5-301',
           conf='high', level='withholding and employer contribution (tax secs. 7111-7113; PFL secs. 4051-4053)',
           note='Status confirmed on Council LIMS (verbatim excerpt). NOT checked: that Law 26-189 carries the same tax (7112) and PFL (4051-4053) text as Act 26-416 - see unresolved dc.live.fy2027_bsa_permanent.')])
unres(dc, narrow={'dc.live.fy2027_bsa_permanent': {'why': 'The permanent FY2027 BSA is D.C. Law 26-189, in force from 2026-10-02 (fact dc.live.fy2027_bsa_permanent). Whether its tax (secs. 7111-7113) and PFL (secs. 4051-4053) text is identical to the emergency Act 26-416 the annex models was not compared (214-page text not read).',
                                                   'what_would_close_it': 'The enrolled text of B26-0661 / D.C. Law 26-189 (LIMS document or code.dccouncil.gov session law), secs. 4051-4053 and 7111-7113, compared with Act 26-416.',
                                                   'blocking': True, 'attempt': P3 + ': LIMS B26-0661 legislative history read (US-DCB5-301)'}})

# ------------------------------------------------------------------ NY (keys shared with WTC)
ny = 'CCG-annex_NY-facts.json'
nyf = [F('ny.local.nyc.supplemental.rate', 4.25, '2026-01-01', 'US-NYB5-301', to='2026-12-31', unit='percent', note='NYS-50-T-NYC (1/26) p. 3, method (a); or (b) aggregate with the latest regular wages minus tax already withheld. If no tax was withheld from regular wages, only (b).', level='withholding'),
       F('ny.local.yonkers.resident.supplemental.rate', 1.95975, '2026-01-01', 'US-NYB5-302', to='2026-12-31', unit='percent', note='NYS-50-T-Y (1/26) p. 3, method (a); or (b) aggregate. If no tax was withheld from regular wages, only (b).', level='withholding'),
       F('ny.local.yonkers.nonresident.supplemental.rate', 0.5, '2026-01-01', 'US-NYB5-302', to='2026-12-31', unit='percent', note='NYS-50-T-Y (1/26) p. 3, method (a); or (b) aggregate.', level='withholding')]
add(ny, nyf)
unres(ny, close={'ny.pit.supplemental.local_rates'})
add(wtc, [dict(f) for f in nyf])
unres(wtc, close={'ny.local.nyc.supplemental.rate', 'ny.local.yonkers.resident.supplemental.rate', 'ny.local.yonkers.nonresident.supplemental.rate'})

# ------------------------------------------------------------------ TX
tx = 'CCG-annex_TX-facts.json'
add(tx, [F('tx.report.ui.enhanced_fields.status', 'PROPOSED ONLY: TWC proposed amendment to 40 TAC 815.107 (51 TexReg 5161, 2026-08-07; approved for proposal 2026-07-21, comments to 2026-09-07) would add to the quarterly wage report: wages, industry, occupation field, full/part-time status, county of primary employment, remote-work status (Labor Code 204.0025) and data for the 302.0205 Regional Labor Demand Assessment. Not adopted in the Texas Register adopted-rules issues of 2026-09-25 to 2026-10-30: on 2026-11-02 no field is mandatory and no start quarter is set.', '2026-08-07', 'US-TXB5-301',
           conf='high', level='employer reporting (quarterly UI wage report)',
           note='G-RULING: identity 40 TAC 815.107 (proposed), 51 TexReg 5161; status proposal, not adopted; level employer reporting. Configure nothing as mandatory; re-check adopted-rules issues from November 2026.')])
for f in load(tx)['facts']:
    if f['key'] == 'tx.report.ui.enhanced_fields':
        f['note'] = 'Labor Code 204.0025 (2025) lists the data; TWC implementation is a PROPOSED rule only (tx.report.ui.enhanced_fields.status, US-TXB5-301) - not mandatory on 2026-11-02.'
        L('FACT note updated', tx, 'tx.report.ui.enhanced_fields')
unres(tx, close={'tx.report.ui.enhanced_fields_layout'},
      new=[U('tx.report.ui.enhanced_fields.adoption', 'The 815.107 amendment is proposed only; adoption date, first mandatory quarter and the TWC file layout are not published (twc.texas.gov layout pages geo-blocked from Brazil).',
             'Texas Register adopted-rules notice for 40 TAC 815.107 (from November 2026) and the TWC wage-report file layout.', [P3 + ': adopted-rules issues 2026-09-25..10-30 searched for 815.107: none'], False)])

# ------------------------------------------------------------------ IL
il = 'CCG-annex_IL-facts.json'
add(il, [F('il.leave.cook.paid_leave.in_force', 'Cook County Paid Leave Ordinance in force from 2023-12-31 (2025-01-01 for park and school districts); does not apply in the City of Chicago (own ordinance); a prior Earned Sick Leave Ordinance opt-out does not carry over.', '2023-12-31', 'US-ILB5-301'),
         F('il.leave.cook.paid_leave.accrual', '1 hour of paid leave per 40 hours worked, usable for any reason; FLSA-exempt employees deemed to work 40 hours a week; front-loading allowed.', '2023-12-31', 'US-ILB5-301'),
         F('il.leave.cook.paid_leave.carryover_cap.min_hours', 40, '2023-12-31', 'US-ILB5-301', unit='hours', note='An employer carry-over cap may not be set below 40 hours.'),
         F('il.leave.cook.paid_leave.payout_at_separation', 'Not required, unless the leave is credited to a PTO bank or vacation account; then unused leave is paid within 15 days of separation.', '2023-12-31', 'US-ILB5-301')])
unres(il, close={'il.leave.cook.paid_leave'},
      new=[U('il.leave.cook.paid_leave.rules_2025', 'The Cook County Paid Leave Substantive and Procedural Rules approved 2025-04-10 are listed on the CCHR page but not read; they may refine the FAQ (corrected 04/2024) details carried in the il.leave.cook.paid_leave.* facts.',
             'CCHR Paid Leave Ordinance Rules (approved 2025-04-10) on cookcountyil.gov.', [P3 + ': CCHR page and FAQ read (US-ILB5-301)'], False)])

# ------------------------------------------------------------------ NM
nm = 'CCG-annex_NM-facts.json'
add(nm, [F('nm.labour.minwage.local.santa_fe_county.hourly', 15.0, '2025-03-01', 'US-NMB5-301', to='2026-02-28', cur='USD', note='Unincorporated Santa Fe County living wage (Ord. 2014-1 as amended), previous-rates table.'),
         F('nm.labour.minwage.local.santa_fe_county.hourly', 15.4, '2026-03-01', 'US-NMB5-301', cur='USD', note='From 2026-03-01 (County news release 2026-02-12); adjusted each March 1 by CPI-W West. 15.40/15.00 = 1.0267.'),
         F('nm.labour.minwage.local.santa_fe_county.tipped_base.hourly', 4.5, '2025-03-01', 'US-NMB5-301', to='2026-02-28', cur='USD'),
         F('nm.labour.minwage.local.santa_fe_county.tipped_base.hourly', 4.62, '2026-03-01', 'US-NMB5-301', cur='USD', note='Tipped base = 30% of the living wage: 15.40 x 0.30 = 4.62; 15.00 x 0.30 = 4.50 (arithmetic check only, ratio not stated on the page).')])
unres(nm, close={'nm.labour.minwage.local.other'},
      new=[U('nm.labour.minwage.local.santa_fe_county.next_rate', 'The Santa Fe County rate from 2027-03-01 is set by CPI-W West and published in early 2027.', 'Santa Fe County living wage notice / news release of February 2027.', [P3 + ': 2026 rate read (US-NMB5-301)'], False)])

# ------------------------------------------------------------------ MI
mi = 'CCG-annex_MI-facts.json'
add(mi, [F('mi.local.cities.list', 'Treasury-administered: Detroit. Self-administered (23): Albion, Battle Creek, Benton Harbor, Big Rapids, East Lansing, Grand Rapids, Flint, Grayling, Hamtramck, Highland Park, Hudson, Ionia, Jackson, Lansing, Lapeer, Muskegon, Muskegon Heights, Pontiac, Port Huron, Portland, Saginaw, Springfield, Walker.', '2026-01-01', 'US-MIB5-301',
           note='Treasury "Which cities impose an income tax?" page (verbatim Chrome text), consistent with mi.local.cities.count = 24 (US-MIR3-001, a different Treasury page). The page gives no rates.'),
         F('mi.local.detroit.eservices_from', '2026-11-12', '2026-11-12', 'US-MIB5-301', note='Detroit city income taxes move to Michigan Treasury eServices on 2026-11-12 (michigan.gov/taxes/citytax, read 2026-11-02).', level='employer reporting and payment')])
unres(mi, narrow={'mi.local.cities.rates': {'why': 'The census is closed (24 cities, named in mi.local.cities.list). The per-city rates, withholding forms and due dates of the 23 self-administered cities are on each city\'s own site; Treasury publishes none of them.',
                                            'what_would_close_it': 'Each self-administered city\'s 2026 employer withholding instructions (city income-tax department page): parallel lookups, one per city, ideally limited to the cities in the client footprint.',
                                            'blocking': True, 'attempt': P3 + ': Treasury city list read (US-MIB5-301), no rates'}})

# ------------------------------------------------------------------ MA
ma = 'CCG-annex_MA-facts.json'
add(ma, [F('ma.report.w2.employee_statement.due', 'Furnish the wage statement to each employee on or before January 31 of the following year, or within 30 days of the last payment if employment ends earlier.', '2026-01-01', 'US-MAB5-301',
           note='830 CMR 62B.2.1(d) (mass.gov, verbatim Chrome excerpt). The regulation sets no deadline for filing W-2 copies with DOR.', level='employer reporting')])
unres(ma, narrow={'ma.report.w2.due_date_conflict': {'why': 'The Feb 28 (paper) / Mar 31 (electronic) dates come from DOR Directive 07-2 (2007, US-MAB5-302), which the Aug 2026 Withholding Tax Guide still echoes. The newer DOR W-2 page (updated 2026-01-30, US-MAS5-015) says January 31, and 830 CMR 62B.2.1(d) fixes January 31 for the employee statement (US-MAB5-301). No TIR or Directive formally replacing 07-2 was found. Filing by January 31 meets every candidate deadline, so the build can configure January 31 without risk.',
                                                     'what_would_close_it': 'A DOR TIR/Directive superseding Directive 07-2, or a DOR confirmation that January 31 applies to W-2 filing with DOR.',
                                                     'blocking': False, 'attempt': P3 + ': 830 CMR 62B.2.1 and Directive 07-2 read (US-MAB5-301/-302)'}})

# ------------------------------------------------------------------ WV
wv = 'CCG-annex_WV-facts.json'
add(wv, [F('wv.pit.rate_cut.sb392', 'SB 392 signed 2026-03-31; W. Va. Code 11-21-4j effective 2026-06-12 with a 5% rate cut retroactive to 2026-01-01; the Tax Division updated the 2026 withholding tables (IT-100.2A/B dated March 2026).', '2026-01-01', 'US-WVB5-301',
           note='Neither the Tax Division page nor IT-100.2A states the date employers must switch to the March 2026 tables, nor whether Jan-May over-withholding must be refunded or caught up (see unresolved wv.pit.tables.start_date).', level='assessment (retroactive rate) and withholding (tables)')])
unres(wv, narrow={'wv.pit.tables.start_date': {'why': 'Now sourced (US-WVB5-301): law effective 2026-06-12, rate cut retroactive to 2026-01-01, tables dated March 2026. Still not stated by the Tax Division: the date from which employers must apply the March 2026 tables, and whether over-withholding from January to the switch must be adjusted by the employer or is settled at assessment.',
                                               'what_would_close_it': 'A WV Tax Division employer notice or TSD on SB 392 withholding (switch date and treatment of January-switch over-withholding), or a written answer from the Tax Division withholding unit.',
                                               'blocking': True, 'attempt': P3 + ': Tax Division SB 392 page and IT-100.2A (March 2026) read'}})

# ------------------------------------------------------------------ CT tables (item 4)
ct = 'CCG-annex_CT-facts.json'
TBL = os.path.join(R, 'qa-r1-fix', 'ct-tables', 'CT-2026-withholding-tables.csv')
ver = json.load(open(os.path.join(R, 'qa-r1-fix', 'ct-tables', 'verify.json')))
assert ver['all_checks_pass'] and ver['examples_reproduce']
CTR = 'US-CTQ1B-001'
if CTR not in RX:
    row = {c: '' for c in COLS}
    row.update({'id': CTR, 'domain': 'income_tax', 'instrument_name': 'DRS IP 2026(1) Connecticut Employer\'s Tax Guide (Circular CT): State of Connecticut 2026 Withholding Tables (Effective January 1, 2026), weekly, bi-weekly, semi-monthly and monthly payroll periods',
                'instrument_type': 'rate_table', 'tier': 'A.2', 'authority': 'Connecticut Department of Revenue Services',
                'url': 'https://portal.ct.gov/-/media/drs/publications/pubsip/2026/ip-2026-1.pdf', 'article_or_section': 'pp. 31-38 (weekly 31-32, bi-weekly 33-34, semi-monthly 35-36, monthly 37-38); Examples 8-10 pp. 11-12',
                'publication_date': '2026', 'effective_from': '2026-01-01', 'effective_to': '2026-12-31', 'supersedes': '',
                'figure_or_rule_carried': 'Per-period withholding amounts by wage band and withholding code A/B/C/D/F: 139 bands per period (weekly to 1,932; bi-weekly to 3,865; semi-monthly to 4,187; monthly to 8,375; above: "Refer to TPG-211, Withholding Calculation Rules"). Examples 8-10 reproduce from the tables: weekly 700 code F = 17.65 (x 60% = 10.59); weekly 1,000 code A = 39.97 (x 40% = 15.99); bi-weekly 2,300 code B = 78.82. Parsed table: _research/qa-r1-fix/ct-tables/CT-2026-withholding-tables.csv.',
                'language': 'en', 'local_file': '00-official-sources/pdfs/CT/CT_IP-2026-1_2026-11-02.pdf', 'retrieved_on': '2026-11-02', 'verified_on': TODAY,
                'verification_method': 'inspected directly: table pages have no text layer (glyphs are vector paths); decoded with PyMuPDF get_drawings, each glyph labelled by path signature and by bitmap template (zero disagreements in the table body), 556 rows; checks: bands contiguous from 0 to the TPG-211 threshold, every code column non-decreasing, Examples 8-10 reproduced, 3 row groups compared by eye with the rendered page; md5 a64b2bbb855163fb832396939efc74ef; scripts _research/qa-r1-fix/scripts/ct_tables_parse.py, ct_tables_build.py',
                'consumed_by': '', 'status': 'active'})
    reg.append(row); RX[CTR] = row
    L('REGISTER row added', CTR)
rows = list(csv.DictReader(open(TBL, encoding='utf-8')))
ctf = [F('ct.wh.tables.columns', 'wages_greater_than|wages_less_than_or_equal_to|A|B|C|D|F (USD; withholding code from Form CT-W4; amounts per pay period)', '2026-01-01', CTR, vm='direct artifact inspection', to='2026-12-31',
         note='Layout of every ct.wh.table.<period>.row.<nnn> value. Lookup: the band with greater_than < taxable wages <= less_than_or_equal_to; take the code column.')]
over = {'weekly': 1932, 'biweekly': 3865, 'semimonthly': 4187, 'monthly': 8375}
for p, v in over.items():
    ctf.append(F('ct.wh.table.%s.max_wages' % p, v, '2026-01-01', CTR, vm='direct artifact inspection', to='2026-12-31', cur='USD',
                 note='Wages over this amount: "Refer to TPG-211, Withholding Calculation Rules" (no table row).'))
for r in rows:
    val = '|'.join([r['wages_greater_than'], r['wages_less_than_or_equal_to'], r['A'], r['B'], r['C'], r['D'], r['F']])
    ctf.append(F('ct.wh.table.%s.row.%03d' % (r['period'], int(r['row'])), val, '2026-01-01', CTR, vm='direct artifact inspection', to='2026-12-31'))
ex = ver['examples']
ctf += [F('ct.oracle.ip2026_1.ex8.withheld_allocated', 10.59, '2026-01-01', CTR, vm='direct artifact inspection', to='2026-12-31', cur='USD', note='Example 8: table amount 17.65 (weekly band %s-%s, code F) x 60%% CT-W4NA share = 10.59.' % tuple(ex['Ex8']['band'])),
        F('ct.oracle.ip2026_1.ex9.week1_allocated', 15.99, '2026-01-01', CTR, vm='direct artifact inspection', to='2026-12-31', cur='USD', note='Example 9: table amount 39.97 (weekly band %s-%s, code A) x 40%% of days in CT = 15.99.' % tuple(ex['Ex9']['band']))]
EXN = {'ct.oracle.ip2026_1.ex8.withholding': ('Ex8', 'weekly', 'F'), 'ct.oracle.ip2026_1.ex9.withholding': ('Ex9', 'weekly', 'A'), 'ct.oracle.ip2026_1.ex10.withholding': ('Ex10', 'biweekly', 'B')}
for f in load(ct)['facts']:
    if f['key'] in EXN:
        e_, per, code = EXN[f['key']]
        assert str(f['value']) == ex[e_]['table_amount'] or '%.2f' % f['value'] == ex[e_]['table_amount'], (f['key'], f['value'], ex[e_])
        f['confidence'] = 'high'
        f['note'] = f.get('note', '') + ' QA r1b: reproduced from the parsed %s table, band %s-%s, code %s = %s (US-CTQ1B-001).' % (per, ex[e_]['band'][0], ex[e_]['band'][1], code, ex[e_]['table_amount'])
        f['_qa_r1b'] = TODAY
        L('FACT oracle confirmed', ct, f['key'], f['value'], 'confidence medium -> high')
add(ct, ctf)
unres(ct, close={'ct.wh.tables.per_period'},
      new=[U('ct.wh.engine_method', 'DRS allows the tables (IP 2026(1) pp. 31-38, now keyed as ct.wh.table.*) or the TPG-211 calculation rules; results differ by up to 0.48 per period and the DRS oracle examples reproduce only from the tables. Which one the engine uses is a design decision, not a research gap.',
             'Owner/design decision (CT-OQ-1): tables (ct.wh.table.*) up to the per-period maximum and TPG-211 above it, or TPG-211 throughout.', ['QA r1b 2026-11-02: tables parsed and Examples 8-10 reproduced'], False)])
unres(wtc, narrow={'ct.sit.tables.parsing': {'why': 'Tables parsed (CCG annex_CT keys ct.wh.table.<period>.row.<nnn>, register US-CTQ1B-001; Examples 8-10 reproduce). Open only the owner choice tables vs TPG-211 rules.', 'what_would_close_it': 'Owner decision CT-OQ-1.', 'blocking': False, 'attempt': 'QA r1b 2026-11-02: IP 2026(1) pp. 31-38 decoded'}})

# ------------------------------------------------------------------ write facts, consumed_by
for name, d in files.items():
    d['generated_on'] = TODAY
    json.dump(d, open(os.path.join(R, name), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    unit = unit_of(name)
    for f in d['facts']:
        if f.get('_qa_r1b'):
            r = RX[f['register_id']]
            toks = [t for t in r['consumed_by'].split(';') if t]
            if unit not in toks:
                toks.append(unit); r['consumed_by'] = ';'.join(toks)
                L('CONSUMED_BY', f['register_id'], '+' + unit)
            if r['verified_on'] < TODAY:
                L('VERIFIED_ON older than today (not restamped; not re-verified in this pass)', f['register_id'], r['verified_on'])
with open(REG, 'w', encoding='utf-8', newline='') as fh:
    w = csv.DictWriter(fh, fieldnames=COLS, lineterminator='\n'); w.writeheader(); w.writerows(reg)
open(os.path.join(R, 'qa-r1-fix', 'r1b_facts.log'), 'w', encoding='utf-8').write('\n'.join(log) + '\n')
print('files', sorted(files), 'log lines', len(log), 'register rows', len(reg))
