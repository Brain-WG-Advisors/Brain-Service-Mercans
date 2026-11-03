"""QA r1 fix (agent 2, compliance-source-hunter), 2026-11-02.
Register rows + facts corrections routed by _qa/CCG-review-r1.json. Run once, after alias_apply.py.
Usage: python -I r1_fix.py <BASE>
"""
import csv, glob, json, os, re, sys

BASE = sys.argv[1]
R = os.path.join(BASE, '_research')
REG = os.path.join(BASE, '00-official-sources', 'legal-basis-register.csv')
TODAY = '2026-11-02'
LOG = []

def log(*a):
    LOG.append(' '.join(str(x) for x in a))

# ------------------------------------------------------------------ register
with open(REG, encoding='utf-8', newline='') as fh:
    rd = csv.DictReader(fh)
    COLS = rd.fieldnames
    rows = list(rd)
byid = {r['id']: r for r in rows}

FEDDIR = '00-official-sources/ccg-sources/FED/'
NEW = [
 dict(id='US-FEDQ1-001', domain='income_tax', instrument_name='IRS Publication 15-B (2026) Employer\'s Tax Guide to Fringe Benefits - Employee Stock Options; Section 83(i) election',
      instrument_type='official_guide', tier='A.2', authority='IRS', url='https://www.irs.gov/pub/irs-pdf/p15b.pdf',
      article_or_section='Pub. 15-B (2026) sec. 2, Employee Stock Options, pp. 13-14 (incl. Section 83(i) election and Reporting requirements)',
      publication_date='2025-12', effective_from='2026-01-01',
      figure_or_rule_carried='Three kinds of options: ISO, ESPP option, nonstatutory (NSO). SS/Medicare/FUTA wages exclude remuneration from exercise of ISO/ESPP options and from disposition of the stock; no FIT withholding required on a disqualifying disposition of ISO/ESPP stock or on the ESPP discount at a qualifying disposition, but the employer reports that income in W-2 box 1. NSO: excess of FMV at exercise over price reported in W-2 boxes 1, 3 (to the SS base) and 5 and box 12 code V (Reg. 1.83-7). 83(i) election (private company, 80% broad-based plan): defers FIT only, no effect on SS/Medicare/FUTA; FIT withheld at 37% in the year the deferred amount is included; W-2 box 12 code GG (income included) and HH (aggregate deferrals).',
      language='en', local_file=FEDDIR + 'FED_IRS-p15b-2026_2026-11-02.pdf'),
 dict(id='US-FEDQ1-002', domain='income_tax', instrument_name='IRS Publication 15 (2026) Circular E - sec. 5 Wages and Other Compensation (fringe benefits list) and sec. 7 Supplemental Wages',
      instrument_type='official_guide', tier='A.2', authority='IRS', url='https://www.irs.gov/pub/irs-pdf/p15.pdf',
      article_or_section='Pub. 15 (2026) sec. 5 (Fringe benefits list incl. Employee stock options) and sec. 7 Supplemental Wages, pp. 23-25',
      publication_date='2025-12', effective_from='2026-01-01',
      figure_or_rule_carried='Supplemental wages include bonuses, commissions, ... and "other payments subject to the supplemental wage rules include taxable fringe benefits and expense allowances paid under a nonaccountable plan"; sec. 5 lists employee stock options among fringe benefits (Pub. 15-B). Above 1,000,000 of supplemental wages in the year: 37% mandatory regardless of W-4. Otherwise, if FIT was withheld from regular wages in the current or preceding year: method 1a flat 22% or 1b aggregate; else 1b. Regardless of method, supplemental wages are subject to SS, Medicare and FUTA. Sec. 8: withhold for the regular payroll period even if the employee does not work the full period.',
      language='en', local_file=FEDDIR + 'FED_IRS-p15-2026_2026-11-02.pdf'),
 dict(id='US-FEDQ1-003', domain='income_tax', instrument_name='IRS Publication 525 (for 2025 returns, dated 2026-02-25) Taxable and Nontaxable Income - Stock Options; Restricted Property',
      instrument_type='official_guide', tier='A.3', authority='IRS', url='https://www.irs.gov/pub/irs-pdf/p525.pdf',
      article_or_section='Pub. 525 (2025), Employee Compensation: Stock Options (Nonstatutory Stock Options; ISOs; Employee stock purchase plan; Section 83(i)) and Restricted Property, pp. 10-14',
      publication_date='2026-02-25', effective_from='2025-01-01',
      figure_or_rule_carried='NSO without readily determinable FMV at grant: no income at grant; income at exercise = FMV - amount paid (if stock not substantially vested at exercise, at vesting); employer reports the spread in W-2 box 12 code V and in boxes 1, 3 (to the SS base) and 5. ISO/ESPP: ordinary income at a disqualifying disposition (or ESPP discount at a qualifying disposition) reported as wages in W-2 box 1; Forms 3921/3922. Restricted property: FMV minus amount paid included when substantially vested, unless the 83(b) election includes it in the year of transfer. Individual-taxpayer guide (TY2025 edition): mechanics, not a 2026 number.',
      language='en', local_file=FEDDIR + 'FED_IRS-p525_2026-11-02.pdf'),
 dict(id='US-FEDQ1-004', domain='social_security', instrument_name='26 CFR 31.3121(v)(2)-1 Treatment of amounts deferred under certain nonqualified deferred compensation plans (eCFR, as of 2026-10-01)',
      instrument_type='regulation', tier='A.1', authority='Treasury / IRS (eCFR, Office of the Federal Register)',
      url='https://www.ecfr.gov/current/title-26/chapter-I/subchapter-C/part-31/subpart-B/section-31.3121(v)(2)-1',
      article_or_section='26 CFR 31.3121(v)(2)-1(a)(1)-(2); (b)(4)(ii) stock options and stock value rights; (b)(4)(iii) restricted property',
      publication_date='2026-10-01', effective_from='2000-01-01',
      figure_or_rule_carried='FICA general timing: wages taken into account when actually or constructively paid. Special timing rule: an amount deferred under a nonqualified deferred compensation plan is wages for FICA as of the later of (A) performance of the services and (B) the date the right is no longer subject to a substantial risk of forfeiture; nonduplication rule. (b)(4)(ii): grant of a stock option/SAR/stock value right is not a deferral, and amounts received on exercise in the year of exercise are not deferred compensation. (b)(4)(iii): property received under a plan is not a deferral merely because it is restricted (section 83), but a plan giving a legally binding right to receive property in a future year may be a nonqualified deferred compensation plan.',
      language='en', local_file=FEDDIR + 'FED_eCFR-26CFR31.3121v2-1_2026-11-02.xml'),
 dict(id='US-FEDQ1-005', domain='social_security', instrument_name='26 CFR 31.3306(r)(2)-1 FUTA treatment of amounts deferred under certain nonqualified deferred compensation plans (eCFR, as of 2026-10-01)',
      instrument_type='regulation', tier='A.1', authority='Treasury / IRS (eCFR, Office of the Federal Register)',
      url='https://www.ecfr.gov/current/title-26/chapter-I/subchapter-C/part-31/subpart-C/section-31.3306(r)(2)-1',
      article_or_section='26 CFR 31.3306(r)(2)-1(a)', publication_date='2026-10-01', effective_from='2000-01-01',
      figure_or_rule_carried='Section 3306(r)(2) special timing rule for FUTA: the rules of 31.3121(v)(2)-1 apply to FUTA (references to FICA read as FUTA).',
      language='en', local_file=FEDDIR + 'FED_eCFR-26CFR31.3306r2-1_2026-11-02.xml'),
 dict(id='US-FEDQ1-006', domain='income_tax_nonresident', instrument_name='IRS Publication 515 (2026) - Source of income (employees, multiyear compensation, geographic fringe benefits) and Wages Paid to Employees - Graduated Withholding',
      instrument_type='official_guide', tier='A.2', authority='IRS', url='https://www.irs.gov/pub/irs-pdf/p515.pdf',
      article_or_section='Pub. 515 (2026) Source of Income - Personal services (Multiyear compensation; Employees: time basis and geographic fringe benefits); Pay for Personal Services Performed - Wages Paid to Employees--Graduated Withholding, pp. 51-53',
      publication_date='2026', effective_from='2026-01-01',
      figure_or_rule_carried='Pay for services partly in and partly outside the US: US-source = total x US workdays / total workdays (time basis). Multiyear compensation (included in 1 year, attributable to 2+ years) is sourced on a time basis over the period to which it is attributable (facts and circumstances). Employees: allocation on a time basis except housing, education, local transportation (main job location), tax reimbursement (taxing jurisdiction), hazardous duty pay, moving reimbursement (new main job location), sourced geographically (Reg. 1.861-4(b)(2)(ii)(D)). Salaries, wages, bonuses or any other pay of NRA employees: graduated withholding as for citizens/residents, add the Pub. 15-T NRA amount for withholding only (not on W-2); report on W-2 (Form 1042-S only for treaty-exempt wages claimed on Form 8233). FICA generally applies; F-1/J-1/M-1/Q nonimmigrants exempt from FICA and FUTA.',
      language='en', local_file=FEDDIR + 'FED_IRS-p515-2026_2026-11-02.pdf'),
 dict(id='US-FEDQ1-007', domain='income_tax', instrument_name='IRS Publication 15-T (2026) - Introduction (NRA procedure and supplemental wages) and Worksheet 1A Table 3 (pay periods per year)',
      instrument_type='official_guide', tier='A.2', authority='IRS', url='https://www.irs.gov/pub/irs-pdf/p15t.pdf',
      article_or_section='Pub. 15-T (2026) Introduction, Withholding Adjustment for Nonresident Alien Employees - Supplemental wage payment; sec. 1 Worksheet 1A step 1b and Table 3',
      publication_date='2025-12', effective_from='2026-01-01',
      figure_or_rule_carried='NRA procedure (add-on) does not apply to a supplemental wage payment if the 37% mandatory flat rate applies or the 22% optional flat rate is used. Methods of Pub. 15-T cannot be used when the 22% or 37% flat rate is used. Worksheet 1A: annualise the payroll-period wages by the number of pay periods per year from Table 3: semiannually 2, quarterly 4, monthly 12, semimonthly 24, biweekly 26, weekly 52, daily 260. No provision adjusts the Table 3 count for a 27th biweekly or 53rd weekly payday (full text searched).',
      language='en', local_file=FEDDIR + 'FED_IRS-p15t-2026_2026-11-02.pdf'),
 dict(id='US-FEDQ1-008', domain='benefits_in_kind', instrument_name='IRS Publication 15-B (2026) - Group-Term Life Insurance Coverage (exclusion, employment tax treatment) and sec. 4 Rules for Withholding, Depositing, and Reporting',
      instrument_type='official_guide', tier='A.2', authority='IRS', url='https://www.irs.gov/pub/irs-pdf/p15b.pdf',
      article_or_section='Pub. 15-B (2026) Group-Term Life Insurance Coverage (Exclusion from wages; Coverage over the limit) and sec. 4 Rules for Withholding, Depositing, and Reporting, p. 31',
      publication_date='2025-12', effective_from='2026-01-01',
      figure_or_rule_carried='Taxable noncash fringe benefits may be treated as paid on a pay period, quarter, semiannual, annual or other basis (at least annually; all 2026 benefits treated as paid by 2026-12-31); not for cash fringes or transfers of investment/real property (actual transfer date). Withholding: add the fringe value to regular wages for the payroll period, or withhold FIT at the flat 22% supplemental rate (37% above 1,000,000). Group-term life over 50,000: cost is wages in W-2 boxes 1, 3 and 5 (SS/Medicare apply); no FIT withholding and no FUTA required.',
      language='en', local_file=FEDDIR + 'FED_IRS-p15b-2026_2026-11-02.pdf'),
 dict(id='US-FEDQ1-009', domain='labour_code', instrument_name='5 U.S.C. 6103 Holidays (United States Code, 2023 edition, govinfo)',
      instrument_type='statute', tier='A.1', authority='US Congress / GPO (govinfo)',
      url='https://www.govinfo.gov/content/pkg/USCODE-2023-title5/html/USCODE-2023-title5-partIII-subpartE-chap61-subchapI-sec6103.htm',
      article_or_section='5 U.S.C. 6103(a) legal public holidays; 6103(b)(1) Saturday holiday observed the preceding Friday',
      publication_date='2024', effective_from='2021-06-17',
      figure_or_rule_carried='Legal public holidays: New Year\'s Day Jan 1; Birthday of Martin Luther King, Jr. third Monday in January; Washington\'s Birthday third Monday in February; Memorial Day last Monday in May; Juneteenth National Independence Day June 19; Independence Day July 4; Labor Day first Monday in September; Columbus Day second Monday in October; Veterans Day Nov 11; Thanksgiving Day fourth Thursday in November; Christmas Day Dec 25. (b)(1): instead of a holiday on a Saturday, the Friday before is a legal public holiday for Mon-Fri employees (pay and leave). effective_from = Juneteenth amendment (Pub. L. 117-17, 2021-06-17).',
      language='en', local_file=FEDDIR + 'FED_GOVINFO-5USC6103_2026-11-02.htm'),
 dict(id='US-FEDQ1-010', domain='labour_code', instrument_name='OPM Federal Holidays - 2026 and 2027 Holiday Schedules',
      instrument_type='authority_page', tier='A.2', authority='US Office of Personnel Management',
      url='https://www.opm.gov/policy-data-oversight/pay-leave/federal-holidays/',
      article_or_section='2026 Holiday Schedule; 2027 Holiday Schedule (with 5 U.S.C. 6103(b) and EO 11582 sec. 3(a) footnotes)',
      publication_date='', effective_from='2026-01-01',
      figure_or_rule_carried='2026: Thu Jan 01 New Year\'s Day; Mon Jan 19 MLK; Mon Feb 16 Washington\'s Birthday; Mon May 25 Memorial Day; Fri Jun 19 Juneteenth; Fri Jul 03 Independence Day (observed; Jul 4 is Saturday); Mon Sep 07 Labor Day; Mon Oct 12 Columbus Day; Wed Nov 11 Veterans Day; Thu Nov 26 Thanksgiving; Fri Dec 25 Christmas. 2027: Fri Jan 01; Mon Jan 18; Mon Feb 15; Mon May 31; Fri Jun 18 (observed); Mon Jul 05 (observed); Mon Sep 06; Mon Oct 11; Thu Nov 11; Thu Nov 25; Fri Dec 24 (observed). Sunday holiday observed the following Monday (EO 11582 sec. 3(a)).',
      language='en', local_file=FEDDIR + 'FED_OPM-holidays-2026_2026-11-02.html'),
 dict(id='US-FEDQ1-011', domain='reporting', instrument_name='IRS Publication 15 (2026) Circular E - Calendar (Saturday/Sunday/legal holiday rule) and sec. 11 Deposits Due on Business Days Only / Legal holiday list 2026',
      instrument_type='official_guide', tier='A.2', authority='IRS', url='https://www.irs.gov/pub/irs-pdf/p15.pdf',
      article_or_section='Pub. 15 (2026) Calendar introduction; sec. 11 Deposits Due on Business Days Only and Legal holiday, pp. 33-34',
      publication_date='2025-12', effective_from='2026-01-01',
      figure_or_rule_carried='Filing/furnishing/deposit date on a Saturday, Sunday or legal holiday -> next business day; legal holiday = any legal holiday in the District of Columbia; a statewide legal holiday delays a filing due date only if the IRS office of filing is in that State and never delays federal tax deposits. Semiweekly depositors have at least 3 business days after the semiweekly period; one extra day for each legal holiday in those 3 weekdays. Legal holidays for 2026: Jan 1; Jan 19; Feb 16; Apr 16 (District of Columbia Emancipation Day); May 25; Jun 19; Jul 3 (Independence Day observed); Sep 7; Oct 12; Nov 11; Nov 26; Dec 25.',
      language='en', local_file=FEDDIR + 'FED_IRS-p15-2026_2026-11-02.pdf'),
 dict(id='US-FEDQ1-012', domain='indexation', instrument_name='26 U.S.C. 1(f)(3)-(4) Cost-of-living adjustment (United States Code, 2024 edition, govinfo)',
      instrument_type='statute', tier='A.1', authority='US Congress / GPO (govinfo)',
      url='https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partI-sec1.htm',
      article_or_section='26 U.S.C. 1(f)(3)(A)-(C) and 1(f)(4)', publication_date='2025', effective_from='2018-01-01',
      figure_or_rule_carried='Cost-of-living adjustment for a calendar year = percentage by which the C-CPI-U for the preceding calendar year exceeds the CPI for 2016, multiplied by C-CPI-U(2016)/CPI(2016); CPI for a year = average CPI for the 12 months ending August 31. The indexing caliber is the chained CPI-U (C-CPI-U). effective_from = Pub. L. 115-97 switch to C-CPI-U for taxable years after 2017.',
      language='en', local_file='00-official-sources/ccg-sources/FED/USC_26-1_govinfo-2024ed_2026-11-02.html', supersedes='US-FED-026'),
 dict(id='US-MULTIQ1-001', domain='income_tax', instrument_name='4 U.S.C. 114 Limitation on State income taxation of certain pension income (United States Code, 2024 edition, govinfo)',
      instrument_type='statute', tier='A.1', authority='US Congress / GPO (govinfo)',
      url='https://www.govinfo.gov/content/pkg/USCODE-2024-title4/html/USCODE-2024-title4-chap4-sec114.htm',
      article_or_section='4 U.S.C. 114(a)-(b)', publication_date='2025', effective_from='1996-01-10',
      figure_or_rule_carried='(a) No State may impose an income tax on any retirement income of an individual who is not a resident or domiciliary of that State; (b) retirement income = income from 401(a) trusts, SEPs, 403(a)/(b), IRAs, 457 eligible plans, governmental plans, 501(c)(18) trusts and certain 3121(v)(2)(C) arrangements. Covers retirement income only: not a wage-sourcing or mobile-worker statute. Read with the other federal limits held in the register (49 U.S.C. 14503, 11502, 40116; 46 U.S.C. 11108; 50 U.S.C. 4001): no general federal statute sources the wages of a non-transport mobile employee.',
      language='en', local_file='00-official-sources/ccg-sources/MULTI/USC_4-114_govinfo-2024ed_2026-11-02.html', supersedes='US-FEDP51-009'),
]
for n in NEW:
    if n['id'] in byid:
        continue
    row = {c: '' for c in COLS}
    row.update(n)
    row.update(retrieved_on=TODAY, verified_on=TODAY, status='active',
               verification_method=('second independent authority' if n['id'] in ('US-FEDQ1-010', 'US-FEDQ1-011', 'US-FEDQ1-009')
                                    else 'quoted from authority page'))
    rows.append(row)
    byid[row['id']] = row
    log('register add', row['id'])

def supersede(old, new, why):
    o = byid[old]
    o['status'] = 'superseded'
    o['effective_to'] = TODAY
    byid[new]['supersedes'] = old if not byid[new]['supersedes'] else byid[new]['supersedes']
    # consumed_by moves to the replacement
    toks = [t for t in (byid[new]['consumed_by'] + ';' + o['consumed_by']).split(';') if t]
    byid[new]['consumed_by'] = ';'.join(dict.fromkeys(toks))
    log('register supersede', old, '->', new, why)

supersede('US-FED-026', 'US-FEDQ1-012', 'LII republication replaced by govinfo official text (C30)')
supersede('US-FEDP51-009', 'US-MULTIQ1-001', 'LII republication replaced by govinfo official text (C30)')
supersede('US-CAEDD-004', 'US-CAP7-002', 'duplicate CA SDI 2026 row; one active row kept (finding CA SDI)')
byid['US-CAP7-002']['verified_on'] = byid['US-CAP7-002']['verified_on'] or TODAY

# article precision for superseded rows whose article is generic (C70 false hits)
SPECIFIC = re.compile(r'\d+[\.\-\(]\d|\b\d{2,}[A-Za-z]?\b|§|sec\.|Sec\.|p\.\s*\d|page|Rule|Part|Table \d|ch\.|Chapter')
for r in rows:
    if r['status'].lower() in ('superseded', 'repealed', 'withdrawn', 'abrogated'):
        a = r['article_or_section'].strip()
        generic = (not SPECIFIC.search(a)) or re.fullmatch(r'\d{4}( rates)?', a)
        if r['id'] in ('US-FED-026', 'US-FEDP51-009'):
            r['article_or_section'] = 'law.cornell.edu (LII) copy - ' + a
            log('article', r['id'], '->', r['article_or_section'])
        elif r['id'] == 'US-CAEDD-004':
            r['article_or_section'] = 'edd.ca.gov rates_and_withholding page, Chrome re-read of the 2026 SDI rate line'
            log('article', r['id'], '->', r['article_or_section'])
        elif len(a) >= 4 and generic:
            r['article_or_section'] = (r['instrument_name'] + ' - ' + a)[:300]
            log('article', r['id'], repr(a), '->', r['article_or_section'][:90])

# re-verified rows (read again this pass)
for rid in ('US-ILR3-001', 'US-VAS5-013', 'US-WAB5-002', 'US-WAS5-017', 'US-FEDS5-022', 'US-FEDS5-032', 'US-GA-001',
            'US-GAS5-009', 'US-MULTIS5-005', 'US-FEDS5-001', 'US-FEDS5-002', 'US-FEDS5-016', 'US-IAS5-005', 'US-WAS5-015'):
    byid[rid]['verified_on'] = TODAY

# ------------------------------------------------------------------ facts
def load(name):
    p = os.path.join(R, name)
    return p, json.load(open(p, encoding='utf-8'))

def save(p, d):
    json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

def fact(key, value, ef, et, rid, method, conf, note=None, level=None, unit=None, cur=None, domain=None):
    r = byid[rid]
    f = {'key': key, 'value': value}
    if unit:
        f['unit_of_measure'] = unit
    if cur:
        f['currency'] = cur
    f.update({'effective_from': ef, 'effective_to': et, 'register_id': rid, 'tier': r['tier'],
              'verification_method': method, 'authority': r['authority'], 'url': r['url'], 'confidence': conf})
    if note or level:
        f['note'] = ((note + ' ') if note else '') + (('LEVEL: ' + level + '.') if level else '')
    if level:
        f['_level'] = level
    if domain:
        f['_domain'] = domain
    f['_qa_r1'] = 'added 2026-11-02 (agent 2, QA r1)'
    return f

files = {os.path.basename(p): p for p in glob.glob(os.path.join(R, '*-facts.json'))}
D = {n: json.load(open(p, encoding='utf-8')) for n, p in files.items()}
touched = set()

def addf(fname, f):
    D[fname]['facts'] = [x for x in D[fname]['facts']
                         if not (x['key'] == f['key'] and x['effective_from'] == f['effective_from'])]
    D[fname]['facts'].append(f)
    touched.add(fname)

def drop_unresolved(fname, key):
    before = len(D[fname].get('unresolved', []))
    D[fname]['unresolved'] = [u for u in D[fname].get('unresolved', []) if u.get('key') != key]
    if len(D[fname]['unresolved']) != before:
        touched.add(fname)

# history bucket for prior-year configuration facts (C41)
def to_history(fname, pred, why):
    keep, hist = [], D[fname].setdefault('_history', [])
    for x in D[fname]['facts']:
        if pred(x):
            x['_moved_to_history'] = why
            hist.append(x)
            log('history', fname, x['key'], x['effective_from'], x.get('effective_to'))
        else:
            keep.append(x)
    if len(keep) != len(D[fname]['facts']):
        D[fname]['facts'] = keep
        touched.add(fname)

for fname, d in D.items():
    for x in d['facts']:
        k, v = x['key'], x['value']
        # GA level split (C32)
        if k == 'ga.sit.rate':
            x['_renamed_from'] = k
            x['key'] = 'ga.wh.rate'
            x['_level'] = 'withholding'
            touched.add(fname)
        # WA no income tax 2026-2027
        if k == 'wa.pit.exists' and v is False:
            x['effective_from'], x['effective_to'] = '2026-01-01', '2027-12-31'
            x['note'] = 'No Washington individual income tax on wages in 2026 or 2027. From 2028-01-01 SB 6346 creates a 9.9% tax on AGI over 1,000,000 (see wa.pit.high_income_tax.*), assessment-level. LEVEL: withholding.'
            touched.add(fname)
        # WA PFML 2026 employee share: one register row everywhere
        if k == 'wa.pfml.employee.share' and v == 71.43:
            x.update(register_id='US-WAB5-002', tier='A.2', url=byid['US-WAB5-002']['url'],
                     authority='Washington Employment Security Department (Paid Leave)', verification_method='quoted from authority page')
            x['effective_from'], x['effective_to'] = '2026-01-01', '2026-12-31'
            touched.add(fname)
        if k == 'wa.pfml.employee.share' and v == 70.7:
            x['effective_from'], x['effective_to'] = '2027-01-01', None
            touched.add(fname)
        # C46: no square brackets in values
        if isinstance(v, str) and ('[' in v or ']' in v):
            nv = v.replace('[US-IAS5-015]', '(register US-IAS5-015)').replace('[', '(').replace(']', ')')
            x['value'] = nv
            touched.add(fname)
            log('brackets', fname, k)
        # C29 rewording (meaning unchanged)
        if k == 'fed.ssn.truncation.format':
            x['value'] = 'TTIN: first five digits of the SSN masked (asterisks or X characters), last four digits shown, e.g. ***-**-1234; allowed on employee W-2 copies only; never on Copy A; EIN never truncated'
            touched.add(fname)
        if k in ('ga.report.sui.dol4n', 'ga.live.gdol_rules_2026') and isinstance(v, str) and 'placeholder' in v:
            x['value'] = v.replace('placeholder SSN', 'temporary substitute SSN')
            touched.add(fname)
        # C30: LII -> govinfo rows
        if x['register_id'] == 'US-FED-026':
            x.update(register_id='US-FEDQ1-012', tier='A.1', url=byid['US-FEDQ1-012']['url'],
                     authority='US Congress / GPO (govinfo, US Code 2024 ed.)', verification_method='quoted from authority page')
            x['effective_from'] = x['effective_from'] or '2018-01-01'
            touched.add(fname)
        if x['register_id'] == 'US-FEDP51-009':
            x.update(register_id='US-MULTIQ1-001', tier='A.1', url=byid['US-MULTIQ1-001']['url'],
                     authority='US Congress / GPO (govinfo, US Code 2024 ed.)', verification_method='direct artifact inspection')
            x.pop('_ef_basis', None)
            touched.add(fname)
        if x['register_id'] == 'US-CAEDD-004':
            x.update(register_id='US-CAP7-002')
            touched.add(fname)
        # mixed units: Indiana LIT ratio -> percent; per-hour money
        if k.startswith('in.local.lit.rate.') and x.get('unit_of_measure') == 'ratio' and isinstance(v, (int, float)):
            x['value'] = round(v * 100, 4)
            x['unit_of_measure'] = 'percent'
            x['_unit_converted'] = 'ratio %s -> percent %s (QA r1)' % (v, x['value'])
            touched.add(fname)
        if k in ('or.wbf.rate.per_hour', 'or.levy.wbf.hourly', 'wa.wc.supplemental_pension.rate'):
            x['unit_of_measure'] = 'USD per hour'
            x['currency'] = 'USD'
            touched.add(fname)
        # IL-700-T example 1 residual explained
        if k == 'il.oracle.il700t.example1.withholding':
            x['note'] = ('IL-700-T p.3 table-method example: 300 weekly, 2 Line-1 + 1 Line-2 allowances: weekly table 300-302 row, 2 allowances = 9.33, minus 0.95 per Line-2 allowance = 8.38. '
                         'The table values are computed at the bracket midpoint (301): (301 - 2 x 2,925/52) x 4.95% = 9.33. The automated payroll method on exactly 300 gives 8.33 '
                         '(il.oracle.il700t.example1.automated_method_result). Both are correct for their method; the 0.05 residual is the table midpoint, not a booklet defect.')
            x['verification_method'] = 'derived arithmetically'
            touched.add(fname)

# military spouse: one open-ended fact
MS_VALUE = ("A military spouse present in a State solely to be with the servicemember under military orders neither loses nor acquires residence or domicile; "
            "the spouse's income for services performed in that State is not income for services performed or from sources within that State if the spouse is not a resident of it; "
            "for any taxable year the spouse may elect the residence of the servicemember, the spouse's own residence or the permanent duty station (50 U.S.C. 4001(a)(2), (c)). "
            "Payroll effect: on the employee's State certificate of nonresidence, stop work-State withholding.")
for fname, d in D.items():
    ms = [x for x in d['facts'] if x['key'] == 'multi.military_spouse.rule']
    if ms:
        d['facts'] = [x for x in d['facts'] if x['key'] != 'multi.military_spouse.rule']
        d['facts'].append(fact('multi.military_spouse.rule', MS_VALUE, '2018-12-31', None, 'US-MULTIS5-005',
                               'quoted from authority page', 'high', level='withholding', domain='income_tax'))
        touched.add(fname)

# GA: CCG facts carry the withholding level explicitly
GA_WH_1 = lambda: fact('ga.wh.rate', 5.19, '2026-01-01', '2026-05-10', 'US-GA-001', 'quoted from authority page', 'high',
                       note='Employers kept withholding 5.19% until HB 463 was signed (2026-05-11).', level='withholding', unit='percent', domain='income_tax')
GA_WH_2 = lambda: fact('ga.wh.rate', 4.99, '2026-05-11', None, 'US-GAS5-009', 'second independent authority', 'high',
                       note='Withholding at 4.99% from 2026-05-11 (DOR Employer Guide US-GA-001 states the start date; HB 463 the rate).', level='withholding', unit='percent', domain='income_tax')
for fname in ('CCG-annex_GA-facts.json', 'CCG-m06_tax-facts.json'):
    addf(fname, GA_WH_1())
    addf(fname, GA_WH_2())
for fname, d in D.items():
    for x in d['facts']:
        if x['key'] == 'ga.pit.rate.flat' and x['value'] == 4.99:
            x['note'] = 'Statutory rate for taxable year 2026, retroactive to 2026-01-01 (HB 463); the year-end assessment applies 4.99% to all 2026 wages. Withholding level: ga.wh.rate. LEVEL: assessment.'
            x['_level'] = 'assessment'
            touched.add(fname)
# WTC ga.wh.rate registers per the finding
for x in D['WTC-country_specific-facts.json']['facts']:
    if x['key'] == 'ga.wh.rate' and x['value'] == 4.99:
        x['effective_from'] = '2026-05-11'

# WA 2028 tax as a separate assessment-level fact
addf('CCG-annex_WA-facts.json', fact('wa.pit.high_income_tax.rate', 9.9, '2028-01-01', None, 'US-WAS5-017', 'quoted from authority page', 'high',
     note='SB 6346 (2026): individuals and joint filers with AGI over 1,000,000; first returns due April 2029. No employer withholding guidance published as of 2026-11-02.', level='assessment', unit='percent', domain='income_tax'))
addf('CCG-annex_WA-facts.json', fact('wa.pit.high_income_tax.agi_threshold', 1000000, '2028-01-01', None, 'US-WAS5-017', 'quoted from authority page', 'high',
     level='assessment', cur='USD', domain='income_tax'))

# IA / VA keyed facts
addf('CCG-annex_IA-facts.json', fact('ia.wh.formula.rate', 3.8, '2026-01-01', '2026-12-31', 'US-IAS5-005', 'quoted from authority page', 'high',
     note='Rate applied at step T2 of the 2026 withholding formula.', level='withholding', unit='percent', domain='income_tax'))
for x in D['CCG-annex_VA-facts.json']['facts'] + D['WTC-country_specific-facts.json']['facts']:
    if x['key'] in ('va.wh.method', 'va.sit.method'):
        x['value'] = ('Annualise: T = G x P - (standard deduction + 930 x E1 + 800 x E2); annual tax on T by brackets va.pit.bracket.1-4 '
                      '(2% to 3,000; 60 + 3% to 5,000; 120 + 5% to 17,000; 720 + 5.75% above 17,000); withholding = annual tax / P')
for key, val, unit in (('va.pit.bracket.1.rate', 2, 'percent'), ('va.pit.bracket.2.rate', 3, 'percent'), ('va.pit.bracket.3.rate', 5, 'percent'),
                       ('va.pit.bracket.2.base_tax', 60, None), ('va.pit.bracket.3.base_tax', 120, None), ('va.pit.bracket.4.base_tax', 720, None)):
    addf('CCG-annex_VA-facts.json', fact(key, val, '2025-07-01', None, 'US-VAS5-013', 'quoted from authority page', 'high',
         level='withholding', unit=unit, cur=(None if unit else 'USD'), domain='income_tax'))
touched.update({'CCG-annex_VA-facts.json', 'WTC-country_specific-facts.json'})

# IL automated-method companion fact
addf('CCG-annex_IL-facts.json', fact('il.oracle.il700t.example1.automated_method_result', 8.33, '2026-01-01', '2026-12-31', 'US-ILR3-001',
     'derived arithmetically', 'high', note='(300 - (2 x 2,925 + 1 x 1,000)/52) x 4.95% = 168.27 x 4.95% = 8.33 (automated payroll method, IL-700-T p.3).', cur='USD', domain='oracle'))

# prior-year configuration facts -> _history (C41)
PRIOR = lambda x: bool(x.get('effective_to')) and x['effective_to'] < '2026-01-01'
for fname in list(D):
    if fname.startswith(('CCG-', 'WTC-')):
        to_history(fname, PRIOR, 'prior-year value (effective_to before 2026-01-01) moved out of the configuration facts on 2026-11-02 (QA r1 C41); history kept here and in the register. '
                   'FUTA 2025 credit reductions apply to 2025 wages on the 2025 Form 940 filed by 2026-02-02.')

# ------------------------------------------------------------------ federal answers
def fed(fname, *fs):
    for f in fs:
        addf(fname, f)

EQ_RES = ('Resident employee, 2026: (1) Nonstatutory option (NSO): the spread at exercise (FMV - price) is wages - a taxable fringe benefit subject to the supplemental-wage rules (22% optional flat or aggregate; 37% on supplemental wages above 1,000,000), '
          'FICA and FUTA wages, timed at the actual exercise (transfer) date; W-2 boxes 1, 3 (to the SS base), 5 and box 12 code V. '
          '(2) ISO and ESPP options: no FICA or FUTA at grant, exercise or disposition; no FIT withholding required on a disqualifying disposition or on the ESPP discount at a qualifying disposition, but the ordinary income is W-2 box 1 wages. '
          '(3) Restricted stock (actual shares subject to forfeiture): FMV minus amount paid is wages when substantially vested (or at transfer with an 83(b) election). '
          '(4) RSU (legally binding right to receive shares in a future year): FICA and FUTA wages at the later of service performance and vesting (special timing rule, 26 CFR 31.3121(v)(2)-1 / 31.3306(r)(2)-1); FIT withholding when the shares are delivered (settlement) as supplemental wages. '
          '(5) 83(i) election (private company): FIT deferred up to 5 years and withheld at 37% when included; FICA/FUTA not deferred; W-2 codes GG/HH.')
EQ_NRA = ('Nonresident alien employee, 2026: equity income is wages subject to graduated withholding as for residents, with the Pub. 15-T NRA add-on, except that no add-on applies when the payment is withheld at the 22% optional or 37% mandatory flat supplemental rate. '
          'Only the U.S.-source part is wages for U.S. withholding: compensation attributable to several years is sourced on a time basis (U.S. workdays / total workdays over the period to which it is attributable, facts and circumstances). '
          'FICA/FUTA follow the resident rules (NSO spread and RSU at vesting are FICA wages) unless the employee is exempt as an F-1/J-1/M-1/Q nonimmigrant. '
          'Reporting on Form W-2; Form 1042-S only for wages exempt under a treaty claimed on Form 8233.')
NRA_BIK = ('Nonresident alien employee, 2026: taxable fringe benefits are wages subject to graduated FIT withholding. Added to regular wages for the payroll period, they are withheld with the Pub. 15-T NRA add-on; withheld separately at the 22% optional flat supplemental rate (37% above 1,000,000), no add-on applies. '
           'Noncash fringes may be treated as paid per pay period, quarter, half-year or year (at least annually). FICA and FUTA apply as for residents unless the employee is an F-1/J-1/M-1/Q nonimmigrant. '
           'Group-term life cost over 50,000: FICA wages, no FIT withholding and no FUTA required, W-2 boxes 1, 3, 5 and box 12 code C. '
           'Only U.S.-source fringes are wages for withholding: housing, education, local transportation (main job location), tax reimbursement (taxing jurisdiction), hazardous duty and moving (new main job location) are sourced geographically, other fringes on a time basis. '
           'Reported on Form W-2 (Form 1042-S only for treaty-exempt wages on Form 8233).')
for fname in ('CCG-annex_FED-facts.json', 'CCG-m06_tax-facts.json'):
    fed(fname,
        fact('fed.equity.withholding_treatment.resident', EQ_RES, '2026-01-01', None, 'US-FEDQ1-001', 'second independent authority', 'medium',
             note='Rows: Pub. 15-B options and 83(i) (US-FEDQ1-001), Pub. 15 sec. 7 (US-FEDQ1-002), Pub. 525 (US-FEDQ1-003), 26 CFR 31.3121(v)(2)-1 (US-FEDQ1-004), 31.3306(r)(2)-1 (US-FEDQ1-005). Confidence medium only for the RSU limb: no IRS publication names RSUs in the FIT timing rule; it follows from settlement in shares (Pub. 15-B 83(i) paragraph) and the NQDC definition in 31.3121(v)(2)-1(b)(4)(iii).',
             level='withholding', domain='income_tax'),
        fact('fed.equity.withholding_treatment.nonresident', EQ_NRA, '2026-01-01', None, 'US-FEDQ1-006', 'second independent authority', 'medium',
             note='Rows: Pub. 515 (US-FEDQ1-006), Pub. 15-T NRA/supplemental (US-FEDQ1-007), Pub. 15-B (US-FEDQ1-001). The grant-to-vest sourcing period for options/RSUs (Treas. Reg. 1.861-4(b)(2)(ii)(F)) was not read: see unresolved fed.equity.nra.sourcing_period.',
             level='withholding', domain='income_tax_nonresident'),
        fact('fed.equity.nso.w2_code', 'V', '2026-01-01', None, 'US-FEDQ1-001', 'second independent authority', 'high',
             note='Also Pub. 525 (US-FEDQ1-003).', level='employer reporting', domain='reporting'),
        fact('fed.equity.iso_espp.fica_futa_applies', False, '2026-01-01', None, 'US-FEDQ1-001', 'quoted from authority page', 'high', level='withholding', domain='social_security'),
        fact('fed.equity.iso_espp.fit_withholding_required', False, '2026-01-01', None, 'US-FEDQ1-001', 'quoted from authority page', 'high',
             note='Ordinary income at a disqualifying disposition (or ESPP discount at a qualifying disposition) is still W-2 box 1 wages.', level='withholding', domain='income_tax'),
        fact('fed.equity.83i.withholding_rate', 37, '2026-01-01', None, 'US-FEDQ1-001', 'quoted from authority page', 'high',
             note='W-2 box 12 codes GG (amount included) and HH (aggregate deferrals).', level='withholding', unit='percent', domain='income_tax'),
        fact('fed.equity.rsu.fica_timing', 'Later of the performance of the services and the date the right is no longer subject to a substantial risk of forfeiture (vesting); FUTA follows the same rule',
             '2026-01-01', None, 'US-FEDQ1-004', 'quoted from authority page', 'high', note='26 CFR 31.3121(v)(2)-1(a)(2)(ii), (b)(4)(iii); 31.3306(r)(2)-1(a) (US-FEDQ1-005).', level='withholding', domain='social_security'),
        fact('fed.fit.nra.bik.treatment', NRA_BIK, '2026-01-01', None, 'US-FEDQ1-008', 'second independent authority', 'high',
             note='Rows: Pub. 15-B sec. 4 and GTL (US-FEDQ1-008), Pub. 15-T NRA/supplemental (US-FEDQ1-007), Pub. 515 (US-FEDQ1-006), Pub. 15 sec. 7 (US-FEDQ1-002).', level='withholding', domain='income_tax_nonresident'),
        fact('fed.fit.nra.addon.flat_rate_supplemental.applies', False, '2026-01-01', None, 'US-FEDQ1-007', 'quoted from authority page', 'high',
             note='Pub. 15-T Introduction: the NRA procedure does not apply when the 22% optional or 37% mandatory flat rate is used.', level='withholding', domain='income_tax_nonresident'),
    )
    drop_unresolved(fname, 'fed.equity.withholding_treatment')
    drop_unresolved(fname, 'fed.fit.nra.bik.treatment')
    D[fname].setdefault('unresolved', []).append({
        'key': 'fed.equity.nra.sourcing_period',
        'why': 'Pub. 515 says multiyear compensation is sourced on a time basis over the period to which it is attributable (facts and circumstances); the specific grant-to-vest period rule for stock options and RSUs in Treas. Reg. 1.861-4(b)(2)(ii)(F) was not read (the eCFR API returned only paragraph (a) of 1.861-4 on 2026-11-02).',
        'attempted': ['https://www.ecfr.gov/api/versioner/v1/full/2026-10-01/title-26.xml?part=1&section=1.861-4 (200, paragraph (a) only)',
                      'https://www.irs.gov/businesses/corporations/equity-stock-based-compensation-audit-techniques-guide (404)'],
        'what_would_close_it': 'Full text of 26 CFR 1.861-4(b)(2)(ii)(F) on ecfr.gov (browser) or govinfo CFR annual edition, title 26 vol. 9.',
        'blocking': False, '_related_register_ids': ['US-FEDQ1-006']})

M01 = 'CCG-m01_foundational-facts.json'
HOL26 = [('new_years_day', '2026-01-01', None), ('mlk_birthday', '2026-01-19', None), ('washingtons_birthday', '2026-02-16', None),
         ('memorial_day', '2026-05-25', None), ('juneteenth', '2026-06-19', None), ('independence_day', '2026-07-03', 'July 4, 2026 is a Saturday; observed Friday July 3 (5 U.S.C. 6103(b)(1)); also the IRS legal holiday.'),
         ('labor_day', '2026-09-07', None), ('columbus_day', '2026-10-12', None), ('veterans_day', '2026-11-11', None),
         ('thanksgiving_day', '2026-11-26', None), ('christmas_day', '2026-12-25', None)]
HOL27 = [('new_years_day', '2027-01-01'), ('mlk_birthday', '2027-01-18'), ('washingtons_birthday', '2027-02-15'), ('memorial_day', '2027-05-31'),
         ('juneteenth', '2027-06-18'), ('independence_day', '2027-07-05'), ('labor_day', '2027-09-06'), ('columbus_day', '2027-10-11'),
         ('veterans_day', '2027-11-11'), ('thanksgiving_day', '2027-11-25'), ('christmas_day', '2027-12-24')]
for name, date, note in HOL26:
    fed(M01, fact('fed.holiday.%s.observed_date' % name, date, '2026-01-01', '2026-12-31', 'US-FEDQ1-011', 'second independent authority', 'high',
                  note=((note + ' ') if note else '') + 'Pub. 15 2026 legal-holiday list = OPM 2026 schedule (US-FEDQ1-010); date re-derived from the 5 U.S.C. 6103 rule (US-FEDQ1-009).',
                  level='employer reporting', domain='labour_code'))
for name, date in HOL27:
    fed(M01, fact('fed.holiday.%s.observed_date' % name, date, '2027-01-01', '2027-12-31', 'US-FEDQ1-010', 'derived arithmetically', 'medium',
                  note='OPM 2027 schedule, re-derived from 5 U.S.C. 6103 and EO 11582; the IRS 2027 list (Pub. 15 for 2027) is not yet published.', level='employer reporting', domain='labour_code'))
fed(M01,
    fact('fed.holiday.dc_emancipation_day.observed_date', '2026-04-16', '2026-01-01', '2026-12-31', 'US-FEDQ1-011', 'quoted from authority page', 'high',
         note='District of Columbia legal holiday: an IRS legal holiday for federal deposit and filing dates, not a 5 U.S.C. 6103 federal holiday.', level='employer reporting', domain='reporting'),
    fact('fed.holidays.legal_public', 'New Year\'s Day; Birthday of Martin Luther King, Jr.; Washington\'s Birthday; Memorial Day; Juneteenth National Independence Day; Independence Day; Labor Day; Columbus Day; Veterans Day; Thanksgiving Day; Christmas Day (11 legal public holidays)',
         '2021-06-17', None, 'US-FEDQ1-009', 'quoted from authority page', 'high', note='5 U.S.C. 6103(a). For IRS due dates the DC holidays apply (adds DC Emancipation Day, April 16).', domain='labour_code'),
    fact('fed.deposit.due_date.non_business_day_rule', 'A filing, furnishing or deposit due date that falls on a Saturday, Sunday or legal holiday moves to the next business day; legal holiday = District of Columbia legal holiday; a statewide holiday never delays a federal deposit; semiweekly depositors get one extra day for each legal holiday in the 3 weekdays after the semiweekly period',
         '2026-01-01', None, 'US-FEDQ1-011', 'quoted from authority page', 'high', level='employer reporting', domain='reporting'),
    fact('fed.fit.extra_pay_period.rule', 'No IRS rule adjusts withholding for a 27th biweekly or 53rd weekly payday: Pub. 15-T Worksheet 1A annualises each payment with the Table 3 count for the payroll period (weekly 52, biweekly 26), and Pub. 15 sec. 8 requires withholding for the regular payroll period, so the extra payday is withheld as one more ordinary period. FICA and FUTA: wages are counted when paid, against the 2026 annual bases for wages paid in 2026.',
         '2026-01-01', '2026-12-31', 'US-FEDQ1-007', 'direct artifact inspection', 'high',
         note='Negative finding: full text of Pub. 15-T (2026) and Pub. 15 (2026) searched for 53/27-period provisions; none. FICA/FUTA paid-basis: Pub. 15 sec. 7/9 and 31.3121(v)(2)-1(a)(1) (US-FEDQ1-004).', level='withholding', domain='income_tax'),
)
drop_unresolved(M01, 'fed.holidays.legal_public_2026')
drop_unresolved(M01, 'fed.fit.extra_pay_period.rule')
D[M01].setdefault('unresolved', []).append({
    'key': 'state.holidays.legal',
    'why': 'State legal holidays (which move State deposit and filing due dates and some State payday rules) are not in the facts; 51 independent jurisdictions.',
    'attempted': ['Not researched in this pass (federal-only scope of agent 2, QA r1, 2026-11-02).'],
    'what_would_close_it': 'Each State revenue department holiday/due-date rule page and the State holiday statute (e.g. the State\'s code section listing legal holidays); a 51-way fan-out, one lookup per jurisdiction.',
    'blocking': False})

# ------------------------------------------------------------------ consumed_by
UNIT = {}
for fname, d in D.items():
    a = d.get('artifact')
    u = d.get('unit')
    tok = '%s/%s' % (a, u) if u else a
    for x in d['facts'] + d.get('_history', []):
        rid = x.get('register_id')
        if rid in byid:
            cur = [t for t in byid[rid]['consumed_by'].split(';') if t]
            if tok not in cur:
                cur.append(tok)
                byid[rid]['consumed_by'] = ';'.join(cur)

# ------------------------------------------------------------------ write
for fname in sorted(touched):
    D[fname]['generated_on'] = TODAY
    save(files[fname], D[fname])
with open(REG, 'w', encoding='utf-8', newline='') as fh:
    w = csv.DictWriter(fh, fieldnames=COLS, lineterminator='\n')
    w.writeheader()
    w.writerows(rows)
open(os.path.join(R, 'qa-r1-fix', 'r1_fix.log'), 'w', encoding='utf-8').write('\n'.join(LOG) + '\nTOUCHED ' + ', '.join(sorted(touched)) + '\n')
print('touched', len(touched), sorted(touched))
print('log lines', len(LOG))
