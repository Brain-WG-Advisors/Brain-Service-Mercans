import sys, json, collections; sys.path.insert(0, '.')
from lib import *
from fmt import dump
from decimal import Decimal as D
os.chdir(BASE)
fields, R = load_reg(); byid = {r['id']: r for r in R}
facts = {fn: json.load(open(fn, encoding='utf-8')) for fn in facts_files()}
log = []
def regnote(rid, txt):
    byid[rid]['verification_method'] += ' | QA r2 2026-11-02: ' + txt
def addcb(rid, fn):
    d = facts[fn]; t = d['artifact'] + ('/' + d['unit'] if d.get('unit') else '')
    cb = [x for x in byid[rid]['consumed_by'].split(';') if x]
    if t not in cb: cb.append(t); byid[rid]['consumed_by'] = ';'.join(cb)
def each(key, eff=None):
    for fn, d in facts.items():
        for f in d['facts']:
            if f['key'] == key and (eff is None or f.get('effective_from') == eff): yield fn, d, f
# 1. derivations (statute multiplier x minimum wage fact)
DER = [('il.garn.creditor.weekly_floor', '2025-01-01', 675, '45', '15.00', '735 ILCS 5/12-803: 45 x the greater of the federal or IL minimum hourly wage (il.minwage.hourly 15.00, 2025-01-01)'),
 ('ma.garn.creditor.weekly_exempt_floor', '2023-01-01', 750, '50', '15.00', 'MGL c.246 s.28: 50 x the greater of the federal or MA minimum wage (ma.minwage.hourly 15.00)'),
 ('nm.garn.consumer.exempt.weekly.state', '2023-07-01', 480, '40', '12.00', 'NMSA 35-12-7 (SB 216, 2023): forty x the highest applicable minimum hourly wage (nm.minwage.hourly 12.00)'),
 ('sd.garn.consumer.floor.weekly', '2026-01-01', 474, '40', '11.85', 'SDCL 21-18-51 worksheet: forty x the federal or state minimum wage, if greater (sd.minwage.hourly 11.85, 2026)'),
 ('wv.garn.consumer.floor.weekly', '2026-01-01', 362.5, '50', '7.25', 'W. Va. Code 38-5A-3: fifty x the federal minimum hourly wage (fed.minwage.hourly 7.25)'),
 ('dc.garn.creditor.weekly_threshold', '2026-07-01', 736, '40', '18.40', 'D.C. Code 16-572: 40 x the DC minimum hourly wage (dc.minwage.hourly 18.40 from 2026-07-01)'),
 ('md.garn.creditor.weekly_exempt_floor', '2024-01-01', 450, '30', '15.00', 'Md. Code CL 15-601.1: 30 x the State minimum hourly wage (md.minwage.hourly 15.00)'),
 ('ak.exempt.salary.weekly_min', '2025-07-01', 1040, '80', '13.00', 'AS 23.10.055 (DOLWD Pamphlet 100): two times the state minimum wage for the first 40 hours = 2 x 40 x ak.minwage.hourly 13.00'),
 ('ak.exempt.salary.weekly_min', '2026-07-01', 1120, '80', '14.00', 'same rule, 2 x 40 x 14.00 (2026-07-01)'),
 ('ak.exempt.salary.weekly_min', '2027-07-01', 1200, '80', '15.00', 'same rule, 2 x 40 x 15.00 (2027-07-01)'),
 ('nd.minwage.tipped.cash_wage', '2012-10-01', 4.86, '0.67', '7.25', 'NDAC 46-02-07: tip credit max 33% of the minimum wage, cash wage = 7.25 x 0.67 = 4.8575 -> 4.86'),
 ('ma.minwage.tip_credit.max', '2023-01-01', 8.25, None, None, 'MGL c.151 s.7: tip credit = minimum wage 15.00 - service rate 6.75 = 8.25')]
for key, eff, val, mult, base, why in DER:
    n = 0; rid = None
    for fn, d, f in each(key, eff):
        if mult:
            prod = D(mult) * D(base); ok = abs(prod - D(str(val))) <= D('0.005')
        else:
            prod = D('15.00') - D('6.75'); ok = prod == D(str(val))
        if not ok: log.append(('derivation_FAILED', key, eff, str(prod))); continue
        f['verification_method'] = 'derived arithmetically'; n += 1; rid = f['register_id']
    if n:
        regnote(rid, f'{key}={val} ({eff}) derived arithmetically: {why} = {prod}'); log.append(('derived', key, eff, str(prod), n))
    else: log.append(('derivation_no_fact', key, eff))
# 2. re-points read by hand
RP = [('oh.pit.wh.rate.1', '2026-08-01', 'US-OH-006'), ('oh.pit.wh.rate.3', '2026-08-01', 'US-OH-006'), ('wa.pfml.wage_cap.annual', '2026-01-01', 'US-WAB5-002'),
      ('in.minwage.hourly', '2009-07-24', 'US-FEDS5-017'), ('tx.minwage.hourly', '2003-09-01', 'US-FEDS5-017')]
for key, eff, rid in RP:
    r = byid[rid]; ents = list(each(key, eff))
    if not ents: log.append(('repoint_no_fact', key, eff)); continue
    hit = [p for p in files_of(r) if find(ents[0][2]['value'], text_of(p))]
    if not hit: log.append(('repoint_skipped_no_value', key, rid)); continue
    for fn, d, f in ents:
        old = f['register_id']; f['register_id'] = rid; f['tier'] = r['tier']; f['url'] = r['url']; f['authority'] = r['authority']; addcb(rid, fn)
        log.append(('repointed', key, eff, old + '->' + rid, fn))
    regnote(rid, f"{key} ({eff}) re-pointed here (figure is in this row's file {os.path.basename(hit[0])})")
# 3. word-form evidence on own row
WF = [('ne.labour.minwage.youth.hourly', 'US-NES5-001', 'thirteen dollars and fifty cents'), ('ne.minwage.tipped.cash_wage', 'US-NES5-001', 'two dollars and thirteen cents'),
      ('nh.overtime.premium.multiplier', 'US-NHS5-003', 'time and one-half'), ('nc.overtime.premium.multiplier', 'US-NCS5-003', 'time and one-half'),
      ('pa.overtime.premium.multiplier', 'US-PAS5-001', 'one and one-half')]
for key, rid, phrase in WF:
    found = False
    for p in files_of(byid[rid]):
        t = text_of(p); i = t.lower().find(phrase)
        if i >= 0:
            regnote(rid, f"{key} read in words: '...{snippet(t, i, 80)}...'"); log.append(('wordform', key, rid)); found = True; break
    if not found: log.append(('wordform_not_found', key, rid, phrase))
# 4. OH municipal count: rows of the official CSV
r = byid['US-OHB5-002']
for p in files_of(r):
    log.append(('oh_file', p))
    if p.lower().endswith('.csv'):
        import csv as _c; rows = list(_c.reader(open(p, encoding='utf-8', errors='ignore'))); log.append(('oh_csv_rows', p, len(rows)))
# 5. NC student-learner: 90% x 7.25 = 6.525, not 6.5 -> unresolved, number removed
for fn, d in facts.items():
    keep = []
    for f in d['facts']:
        if f['key'] == 'nc.labour.minwage.student_learner.hourly' and f['value'] == 6.5:
            d['unresolved'].append({'key': 'nc.labour.minwage.student_learner.hourly', 'why': 'G.S. 95-25.3(b) sets the full-time student / learner / apprentice / messenger rate at ninety percent of the minimum wage; 0.90 x 7.25 = 6.525, which does not reproduce the 6.50 previously keyed, and no NCDOL page stating a rounded hourly figure is on disk (QA r2 2026-11-02).', 'attempted': ['local copy of G.S. 95-25.3 (US-NCS5-002), read 2026-11-02'], 'what_would_close_it': 'NCDOL Wage and Hour Bureau publication stating the hourly student-learner rate (labor.nc.gov); otherwise state the rule as 90% of the minimum wage without an hourly figure.', 'blocking': False})
            log.append(('moved_to_unresolved', f['key'], fn)); continue
        keep.append(f)
    d['facts'] = keep
save_reg(fields, R)
for fn, d in facts.items(): dump(d, fn, '_research/qa-r2-fix/_backup/' + os.path.basename(fn))
json.dump(log, open('_research/qa-r2-fix/apply2-log.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
for l in log: print(l)
