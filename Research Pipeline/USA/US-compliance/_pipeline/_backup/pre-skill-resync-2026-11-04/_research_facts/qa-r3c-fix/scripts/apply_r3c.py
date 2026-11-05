# QA r3c fix (agent 2, 2026-11-02): findings 1 (F44 zero employee UI), 6 (CT table rows),
# 7 (mis-cited keys + rows without local file), 8 (effective_from) and the fact-note part of 3/4.
# Reads/writes only 00-official-sources/legal-basis-register.csv and _research/*-facts.json.
import csv, json, glob, os, re, sys, hashlib, collections
sys.stdout.reconfigure(encoding='utf-8')
BASE = sys.argv[1]
TODAY = '2026-11-02'
REG = os.path.join(BASE, '00-official-sources', 'legal-basis-register.csv')
LOG = collections.OrderedDict(new_rows=[], local_file=[], eff_from=[], repoint=[], fact_edit=[], note_edit=[], added_facts=[], unresolved_removed=[])

def md5(rel):
    return hashlib.md5(open(os.path.join(BASE, rel), 'rb').read()).hexdigest()

rows = list(csv.DictReader(open(REG, encoding='utf-8', newline='')))
FIELDS = list(rows[0].keys())
R = {r['id']: r for r in rows}

# ---------- finding 1: ten statute / agency rows ----------
CS = '00-official-sources/ccg-sources/'
NOTE_EFF = 'effective_from not stated in the instrument; in force as at retrieved_on'
NEW = [
 dict(st='NY', id='US-NYR3C-001', name='N.Y. Labor Law sec. 570 Payment of contributions (Article 18 Unemployment Insurance Law), subd. 6 Agreement to contributions by employees void',
      itype='statute', tier='A.1', auth='New York State Senate (Consolidated Laws of New York, official host)', url='https://www.nysenate.gov/legislation/laws/LAB/570', art='570(6)',
      fig="Employees do not contribute to UI: 'No agreement by an employee to pay any portion of the payment made by his employer for the purpose of providing benefits required by this article shall be valid and no employer shall make a deduction for such purpose from the remuneration of any employee.'",
      lf=CS+'NY/NY_LAB-570_nysenate_wayback-20250803153024.html', eff='',
      vm='inspected directly (Wayback snapshot 2025-08-03 of the official nysenate.gov page; the live host answers 403 to scripted requests)',
      fnote="N.Y. Labor Law 570(6): no agreement by an employee to pay any part of the employer's UI contribution is valid, and no employer may deduct it from the employee's remuneration."),
 dict(st='WA', id='US-WAR3C-001', name='RCW 50.24.010 Payment of contributions (Employment Security Act)',
      itype='statute', tier='A.1', auth='Washington State Legislature (RCW, official host app.leg.wa.gov)', url='https://app.leg.wa.gov/RCW/default.aspx?cite=50.24.010', art='50.24.010',
      fig="Contributions are paid by each employer 'and shall not be deducted, in whole or in part, from the remuneration of individuals in employment of the employer. Any deduction in violation of the provisions of this section shall be unlawful.'",
      lf=CS+'WA/WA_RCW-50.24.010_leg-wa_2026-11-02.htm', eff='', vm='inspected directly (curl of the official RCW page, HTTP 200)',
      fnote='RCW 50.24.010: UI contributions are paid by the employer and shall not be deducted, in whole or in part, from employee remuneration; any such deduction is unlawful.'),
 dict(st='WV', id='US-WVR3C-001', name='W. Va. Code 21A-5-14 Deduction of payments from wages prohibited',
      itype='statute', tier='A.1', auth='West Virginia Legislature (W. Va. Code, official host code.wvlegislature.gov)', url='https://code.wvlegislature.gov/21A-5-14/', art='21A-5-14',
      fig="'An employer shall not deduct payments in whole or in part from the wages of an individual in his employ.' (Chapter 21A Unemployment Compensation, Article 5 Employer Coverage and Responsibility; enacted 1936 2nd Ex. Sess. HB 1)",
      lf=CS+'WV/WV_Code-21A-5-14_wayback-20260118213926.html', eff='',
      vm='inspected directly (Wayback snapshot 2026-01-18 of the official code page; the live host redirects scripted requests away from the code)',
      fnote='W. Va. Code 21A-5-14: an employer shall not deduct UI payments, in whole or in part, from the wages of an employee.'),
 dict(st='OH', id='US-OHR3C-001', name='Ohio Revised Code 4141.23 Contributions; payment (version effective 2025-09-30)',
      itype='statute', tier='A.1', auth='Ohio Legislative Service Commission (codes.ohio.gov)', url='https://codes.ohio.gov/ohio-revised-code/section-4141.23', art='4141.23(A)',
      fig="Contributions accrue and are paid by each employer 'and shall not be deducted, in whole or in part, from the remuneration of individuals in the employer's employ.' Page notes a new version of 4141.23 effective 2026-06-16 (not held).",
      lf=CS+'OH/OH_ORC-4141.23_wayback-20260517053955.html', eff='2025-09-30',
      vm='inspected directly (Wayback snapshot 2026-05-17 of the official codes.ohio.gov page; live host timed out); version effective 2025-09-30 (HB 96, 136th GA); the version effective 2026-06-16 was not retrieved',
      fnote="Ohio Rev. Code 4141.23(A): UI contributions are paid by the employer and shall not be deducted, in whole or in part, from employees' remuneration."),
 dict(st='IL', id='US-ILR3C-001', name='820 ILCS 405/1400 Payment of contributions (Unemployment Insurance Act)',
      itype='statute', tier='A.1', auth='Illinois General Assembly (ILCS, official host ilga.gov)', url='https://www.ilga.gov/Documents/legislation/ilcs/documents/082004050K1400.htm', art='405/1400',
      fig="Contributions are paid quarterly by the employer; 'Such contributions shall not be deducted, in whole or in part, from the wages of individuals in such employer's employ.'",
      lf=CS+'IL/IL_820ILCS405-1400_wayback-20260123104639.htm', eff='',
      vm='inspected directly (Wayback snapshot 2026-01-23 of the official ilga.gov section text; live host timed out)',
      fnote="820 ILCS 405/1400: UI contributions shall not be deducted, in whole or in part, from employees' wages."),
 dict(st='NE', id='US-NER3C-001', name='Neb. Rev. Stat. 48-648 Combined tax; payment; not deducted from wages (Employment Security Law)',
      itype='statute', tier='A.1', auth='Nebraska Legislature (official host nebraskalegislature.gov)', url='https://nebraskalegislature.gov/laws/statutes.php?statute=48-648', art='48-648(1)',
      fig="The combined tax is due and paid by each employer; 'Such combined tax shall not be deducted, in whole or in part, from the wages of individuals in such employer's employ.' (history ends Laws 2025, LB265, sec. 12)",
      lf=CS+'NE/NE_NRS-48-648_wayback-20260511062111.html', eff='',
      vm='inspected directly (Wayback snapshot 2026-05-11 of the official statute page; live host timed out)',
      fnote="Neb. Rev. Stat. 48-648(1): the combined UI tax shall not be deducted, in whole or in part, from employees' wages."),
 dict(st='DE', id='US-DER3C-001', name='19 Del. C. 3346 Deductibility of employer\'s assessments from employee\'s wages (ch. 33 subch. III)',
      itype='statute', tier='A.1', auth='Delaware Code Online (official host delcode.delaware.gov)', url='https://delcode.delaware.gov/title19/c033/sc03/index.html', art='3346',
      fig="'Assessments payable by the employer under this chapter shall not be deducted by the employer, in whole or in part, from the wages of individuals in such employer's employ.'",
      lf=CS+'DE/delcode-title19-c033-sc03_2026-11-02.html', eff='', vm='inspected directly (curl of the official Delaware Code subchapter page, HTTP 200)',
      fnote="19 Del. C. 3346: UI assessments payable by the employer shall not be deducted, in whole or in part, from employees' wages."),
 dict(st='KS', id='US-KSR3C-001', name='K.S.A. 44-710(a) Employer contributions; payment (Employment Security Law)',
      itype='statute', tier='A.1', auth='Kansas Office of Revisor of Statutes (official host ksrevisor.gov)', url='https://www.ksrevisor.gov/statutes/chapters/ch44/044_007_0010.html', art='44-710(a)',
      fig="Contributions are paid by each contributing employer 'and shall not be deducted, in whole or in part, from the wages of individuals in such employer's employ.' Reimbursing-employer payments likewise (44-710(e)(C)).",
      lf=CS+'KS/KSA_044_007_0010_2026-11-02.html', eff='', vm='inspected directly (curl of the official Revisor page, HTTP 200)',
      fnote="K.S.A. 44-710(a): UI contributions shall not be deducted, in whole or in part, from employees' wages."),
 dict(st='UT', id='US-UTR3C-001', name='Utah Code 35A-4-302 Contributions (Employment Security Act)',
      itype='statute', tier='A.1', auth='Utah State Legislature (official host le.utah.gov)', url='https://le.utah.gov/xcode/Title35A/Chapter4/35A-4-S302.html', art='35A-4-302(1)(b)',
      fig="'(b) Contributions may not be deducted, in whole or in part, from the wages of individuals in the employer's employ.' Version C35A-4-S302_1800010118000101 (renumbered and amended by ch. 240, 1996 General Session) is the default version on the section page as at 2026-01-23.",
      lf=CS+'UT/UT_Code-35A-4-302_C35A-4-S302_1800010118000101_wayback-20170217012041.pdf;'+CS+'UT/UT_Code-35A-4-302_page_wayback-20260123024134.html', eff='',
      vm='inspected directly (section PDF of version 1800010118000101 via Wayback 2017-02-17; the 2026-01-23 Wayback snapshot of the section page names the same version as the default; live host timed out)',
      fnote='Utah Code 35A-4-302(1)(b): UI contributions may not be deducted, in whole or in part, from employees\' wages.'),
 dict(st='TN', id='US-TNR3C-001', name='TN DLWD Handbook for Employers (Division of Employment Security), Premiums and Taxes (T.C.A. 50-7-402, 50-7-403)',
      itype='authority_guide', tier='A.3', auth='Tennessee Department of Labor and Workforce Development', url='https://www.tn.gov/content/dam/tn/workforce/documents/employers/HandbookforEmployers6-13-19.pdf', art='Premiums and Taxes, p.27',
      fig="'The Tennessee unemployment insurance program is financed solely by employer premiums paid to the state and employer federal unemployment taxes paid to the Internal Revenue Service.' No employee premium exists.",
      lf=CS+'TN/TN_DLWD_HandbookforEmployers_wayback-20250314182155.pdf', eff='',
      vm='inspected directly (Wayback snapshot 2025-03-14 of the DLWD PDF, file revised 2024-06-10; the live URL now returns 404). T.C.A. 50-7-403 text not held: the official Tennessee Code is published only through the LexisNexis public-access site, which is not retrievable by script',
      fnote="TN DLWD Handbook for Employers (Premiums and Taxes, T.C.A. 50-7-402 and 50-7-403): 'The Tennessee unemployment insurance program is financed solely by employer premiums'; there is no employee premium."),
]
for n in NEW:
    assert n['id'] not in R, n['id']
    lfs = n['lf'].split(';')
    sums = '; '.join(f'md5 {md5(x)}' for x in lfs)
    vm = n['vm'] + f'; {sums}' + ('' if n['eff'] else f'; {NOTE_EFF}')
    row = {k: '' for k in FIELDS}
    row.update(id=n['id'], domain='social_security', instrument_name=n['name'], instrument_type=n['itype'], tier=n['tier'], authority=n['auth'], url=n['url'],
               article_or_section=n['art'], effective_from=n['eff'], figure_or_rule_carried=n['fig'], language='en', local_file=';'.join(lfs),
               retrieved_on=TODAY, verified_on=TODAY, verification_method=vm, consumed_by='', status='active')
    rows.append(row); R[n['id']] = row
    LOG['new_rows'].append({'id': n['id'], 'local_file': lfs, 'md5': sums})

# ---------- finding 7b: rows without a local file ----------
LF = {
 'US-FED-019': (CS+'FED/FED_govinfo_40USC3142_2026-11-02.htm', 'curl of the registered govinfo URL, HTTP 200'),
 'US-FED-023': (CS+'FED/FED_IRS_IR-2025-111_401k-limits_2026-11-02.htm', 'curl of the registered irs.gov newsroom URL, HTTP 200'),
 'US-FED-024': (CS+'FED/FED_IRS-RevProc-2025-19_2026-11-02.pdf', 'curl of the registered irs.gov PDF URL, HTTP 200'),
 'US-FED-025': (CS+'FED/FED_IRS-RevProc-2025-32_2026-11-02.pdf', 'same document and URL as US-FEDS5-010 (local copy shared)'),
 'US-CAP7-001': (CS+'CA/CA_EDD_rates-and-withholding_2026-11-02.htm', 'curl of the registered EDD URL, HTTP 200; page carries the 2026 and 2027 rates'),
 'US-CAP7-002': (CS+'CA/CA_EDD_rates-and-withholding_2026-11-02.htm', 'curl of the registered EDD URL, HTTP 200; page carries the 2026 and 2027 rates'),
 'US-CAP7-003': (CS+'CA/CA_EDD_rates-and-withholding_2026-11-02.htm', 'curl of the registered EDD URL, HTTP 200; page carries the 2026 and 2027 rates'),
 'US-CAEDD-001': (CS+'CA/CA_EDD_rates-and-withholding_2026-11-02.htm', 'curl of the registered EDD URL, HTTP 200; page carries the 2026 and 2027 rates'),
 'US-GA-001': ('00-official-sources/pdfs/GA/GA-DOR-2026-Employers-Withholding-Guide_rev-Sept2026_download-2026-10-29.pdf', 'same document and URL as US-GAP52-003 (local copy shared)'),
 'US-NY-001': ('00-official-sources/pdfs/NY/nys50tnys_wb.pdf', 'same document and URL as US-NYP52-001 (local copy shared)'),
 'US-DCP52-001': (CS+'DC/DC_OTR_income-tax-rates_2026-11-02.htm', 'curl of the registered OTR URL, HTTP 200'),
}
for rid, (lf, how) in LF.items():
    r = R[rid]; assert not r['local_file'].strip(), rid
    assert os.path.exists(os.path.join(BASE, lf)), lf
    r['local_file'] = lf
    r['verification_method'] = (r['verification_method'] + f'; local copy {TODAY}: {how}; md5 {md5(lf)}').strip('; ')
    r['verified_on'] = TODAY
    if not r['retrieved_on']: r['retrieved_on'] = TODAY
    LOG['local_file'].append({'id': rid, 'local_file': lf, 'md5': md5(lf)})

# ---------- finding 8: effective_from ----------
for rid in ['US-OHB5-401', 'US-NYB5-401', 'US-MAB5-402', 'US-MIB5-401', 'US-VAB5-401', 'US-VAB5-402', 'US-MULTIB5-401', 'US-ORB5-401']:
    r = R[rid]; assert not r['effective_from'].strip(), rid
    if NOTE_EFF not in r['verification_method']:
        r['verification_method'] = r['verification_method'].rstrip('; ') + f'; {NOTE_EFF}'
    LOG['eff_from'].append({'id': rid, 'action': 'standard note added: ' + NOTE_EFF})

# ---------- fact edits ----------
SUI = {n['st'].lower() + '.sui.employee.rate': n for n in NEW}
REPOINT = {  # key -> (new register id, reason)
 'ct.oracle.ip2026_1.ex8.withheld_allocated': ('US-CTP10-001', 'IP 2026(1) Example 8 text carries $17.65 x .60 = $10.59'),
 'ct.oracle.ip2026_1.ex9.week1_allocated': ('US-CTP10-001', 'IP 2026(1) Example 9 text carries $39.97 x .40 = $15.99'),
 'de.report.w2.paper_max_forms': ('US-DES5-008', "W-2/1099 FAQ: paper accepted only for '10 W2s/1099Rs or less'"),
 'tx.prevailing_wage.penalty.per_worker_day': ('US-TXS5-015', 'Gov. Code 2258.023 local copy: $60 for each worker for each calendar day'),
 'tx.newhire.report_days': ('US-TXS5-017', "TWC guidebook: 'within 20 calendar days of the hire' (Family Code 234.101-234.104 refers to 42 USC 653a)"),
 'nv.sui.employee.rate': ('US-NVS5-006', "NRS 612 (612.540-.550 area): contributions 'must not be deducted, in whole or in part, from the wages'"),
 'oh.newhire.report_days': ('US-OHS5-014', "ORC 3121.893: report 'not later than twenty days after the date on which the employer hires'"),
 'la.nonres.mobile_workforce.days': ('US-MULTIS5-021', 'Act 382 of 2025 (R.S. 47:112.2, 47:248): thirty-day threshold'),
 'ri.report.w2.efile_threshold': ('US-RIS5-018', "Division of Taxation filing requirements: W-2 e-file where SSA e-filer with 'a minimum of twenty-five (25) employees in the State'"),
 'va.sui.employee.rate': ('US-VAP51-003', "VEC FAQ: 'Are unemployment benefits or taxes deducted from my pay? No. Benefits are funded through taxes on employers'"),
}
CT_ROW = re.compile(r'^ct\.wh\.table\.[a-z_]+\.row\.\d+$')
used = collections.defaultdict(set)   # register id -> consumer tokens
def unit_token(fname, d):
    a = d.get('artifact'); u = d.get('unit')
    return f'{a}/{u}' if u else a

files = sorted(glob.glob(os.path.join(BASE, '_research', '*-facts.json')))
data = {fp: json.load(open(fp, encoding='utf-8')) for fp in files}

def setrow(f, rid, vm=None):
    r = R[rid]
    f['register_id'] = rid; f['tier'] = r['tier']; f['url'] = r['url'].split(' ')[0]
    f['authority'] = r['authority'].split(' (')[0]
    if vm: f['verification_method'] = vm

for fp, d in data.items():
    fn = os.path.basename(fp); tok = unit_token(fn, d)
    for f in d.get('facts', []):
        k = f['key']; old = f.get('register_id')
        if k in SUI:
            n = SUI[k]
            setrow(f, n['id'], 'quoted from authority page')
            f['confidence'] = 'medium' if n['st'] == 'TN' else 'high'
            f['note'] = n['fnote']
            LOG['repoint'].append({'file': fn, 'key': k, 'from': old, 'to': n['id']}); used[n['id']].add(tok)
        elif k in REPOINT:
            rid, why = REPOINT[k]
            setrow(f, rid, 'quoted from authority page')
            LOG['repoint'].append({'file': fn, 'key': k, 'from': old, 'to': rid, 'evidence': why}); used[rid].add(tok)
        elif CT_ROW.match(k) and old == 'US-CTB5-401':
            setrow(f, 'US-CTP10-001'); used['US-CTP10-001'].add(tok)
            LOG.setdefault('ct_rows', collections.Counter())[fn] += 1
        elif k == 'fed.ccpa.support.arrears_addon':
            f['verification_method'] = 'derived arithmetically'
            f['note'] = '15 U.S.C. 1673(b)(2): where support arrears are older than 12 weeks, the 50% and 60% limits become 55% and 65%; 55 - 50 = 5 percentage points.'
            LOG['fact_edit'].append({'file': fn, 'key': k, 'change': 'verification_method -> derived arithmetically (55-50 from the cited statute)'})
        elif k == 'ca.sdi.employee.rate' and fn == 'CCG-annex_CA-facts.json':
            f['note'] = 'Includes PFL; no wage cap since 2024-01-01 (SB 951); no employer share. 2027 rate: 1.4% (EDD Rates and Withholding page).'
            LOG['fact_edit'].append({'file': fn, 'key': k, 'change': 'note corrected: EDD now publishes the 2027 SDI rate 1.4%'})
        if f.get('register_id') in LF: used[f['register_id']].add(tok)
    # 2027 SDI rate, new fact object under the same key (CCG annex CA only)
    if fn == 'CCG-annex_CA-facts.json':
        if not any(f['key'] == 'ca.sdi.employee.rate' and f['effective_from'] == '2027-01-01' for f in d['facts']):
            base = next(f for f in d['facts'] if f['key'] == 'ca.sdi.employee.rate')
            nf = dict(base); nf.update(value=1.4, effective_from='2027-01-01', effective_to=None, note="EDD Rates and Withholding page: 'The SDI withholding rate for 2027 is 1.4 percent.' Includes PFL; no wage cap; no employer share.")
            d['facts'].insert(d['facts'].index(base) + 1, nf)
            LOG['added_facts'].append({'file': fn, 'key': 'ca.sdi.employee.rate', 'value': 1.4, 'effective_from': '2027-01-01', 'register_id': 'US-CAP7-002'})
            used['US-CAP7-002'].add(tok)
        before = len(d.get('unresolved', []))
        d['unresolved'] = [u for u in d.get('unresolved', []) if u.get('key') != 'ca.sdi.employee.rate.next_year']
        if len(d['unresolved']) < before: LOG['unresolved_removed'].append({'file': fn, 'key': 'ca.sdi.employee.rate.next_year', 'closed_by': 'US-CAP7-002 local copy 2026-11-02'})

# ---------- notes: pipeline wording and '|' (CCG facts files) ----------
CA_SUFFIX = ' schedule as shown in the DIR Labor Commissioner FAQ (A.3: an FAQ page, upgrade to the statute text if QA P2 flags it)'
EXACT = {
 'al.wh.std_deduction.married_separate.min': "ADOR withholding booklet rev. 01/2026, Formula For Computing Alabama Withholding Tax, step 2A (printed page 7): Employee claims 'Married Filing Separately (MS)' exemption: 'GI of $17,750 or more deduct $2,500'. Minimum deduction per status: single 2,500 / married filing separately 2,500 / married filing jointly 5,000 / head of family 2,500.",
 'al.wh.std_deduction.head_of_family.min': "ADOR withholding booklet rev. 01/2026, Formula For Computing Alabama Withholding Tax, step 2A (printed page 7): Employee claims 'Head of Family (H)' exemption: 'GI of $35,500 or more deduct $2,500'. Minimum deduction per status: single 2,500 / married filing separately 2,500 / married filing jointly 5,000 / head of family 2,500.",
 'al.local.leeds.rate': 'City of Leeds: 1% of gross earnings, monthly return to Avenu, annual reconciliation, show on pay stub, records 5 years. A Birmingham 1% rate is not confirmed by an official source and is not stated here.',
 'ca.local_minwage.oakland.hourly': 'OMC ch. 5.92, employees working 2+ hours a week; 2027 rate not yet published on the city page.',
 'ca.wh.status_table_map': "Table titles in DE 44 Rev. 52 (4-26): PDF p.56 'Annual Payroll Period Tax Rate Tables', Method B Tables 5, 6, 7; PDF p.54 Method B Table 1 and PDF p.55 Method B Table 3 column headings; PDF p.24: no existing withholding certificate -> 'Single with Zero withholding allowance'. DE 4 status wording from DE 4 (Rev. 56 1-26) p.1 'Filing Status' [US-CAS5-015]. Consequence: a married employee who checks 'Single or Married (with two or more incomes)' is withheld on the single table (Table 5), never on Table 6.",
 'co.famli.total.rate': "2027 total (CDLE FAMLI Business Brief 2026-09-30): 'The 2027 premium rate will be 0.86% of wages, down from 0.88% in 2026.' Split: co.famli.employee.rate / co.famli.employer.rate 2027 (derived, 50% cap).",
 'co.sui.new_employer.rate.total': "2027 Introductory Rates, non-construction / general construction / trades: beginning 0.0153 + support .0017 + surcharge .00 = combined 0.0170 (page: 'The Solvency Surcharge is not in affect for the 2027 calendar year'); heavy construction 0.0406; political subdivision 0.0020.",
 'co.sui.wage_base': None,
 'ct.oracle.ip2026_1.ex8.withholding': 'IP 2026(1) Ex. 8: code F, 700 weekly (table-based). TPG-211 rules give 17.79 (residual 0.14). The weekly table band 692-701, code F, gives 17.65.',
 'ct.oracle.ip2026_1.ex9.withholding': 'Ex. 9: code A, 1,000 weekly (tables). Rules give 39.86 (residual 0.11). The weekly table band 990-1000, code A, gives 39.97.',
 'ct.oracle.ip2026_1.ex10.withholding': 'Ex. 10: code B, 2,300 biweekly (tables). Rules give 79.30 (residual 0.48). The biweekly table band 2269-2307, code B, gives 78.82.',
 'de.wh.certificate': 'The Division of Revenue FAQ answers "No" to accepting a 2020-version federal W-4 for Delaware withholding. The Employer\'s Guide (US-DES5-006) still uses pre-2020 W-4/allowance wording. Default without a certificate and the copy-to-Division rule: de.wh.certificate.default_and_copies.',
 'de.wh.certificate.default_and_copies': "Employer's Guide (live page, sections 13-17).",
 'fed.fica.oasdi.wage_base': "SSA Contribution and Benefit Base page: 'For earnings in 2027, this base is $192,300.'",
 'fed.iwo.omb_expiry': 'OMB 0970-0154 approved without change 2026-08-25; current form extended one year while states reprogram the revised (gig-worker fields) IWO/e-IWO. LEVEL: employer withholding.',
 'fed.ein.format': "Pub. 15 (2026) sec. 1 Employer Identification Number (EIN), PDF p.13: 'The EIN is a nine-digit number the IRS issues. The digits are arranged as follows: 00-0000000.'",
 'hi.live.act24_2026': 'Act text not publicly accessible at review; HRS 235-51 as last published is partly superseded [US-HIS5-027].',
 'id.sui.new_employer.rate': 'Standard: 1.000% = 0.97000% UI + 0.00000% admin + 0.03000% workforce development; standard rate for at least the first six calendar quarters [US-IDS5-021]. IDOL Tax Handbook p.21: "All new employers except cost-reimbursement employers begin with the same standard unemployment insurance tax rate for at least the first six calendar quarters."',
 **{'in.local.lit.rate.'+c: 'DN#1 R46/01-26 county chart (Boone 0.017, Marion 0.0202, Porter 0.005, Randolph 0.03); periods 2026-01-01..2026-09-30; replaced by R47 (US-INS5-007) from 2026-10-01.' for c in ('marion','min','max')},
 'in.local.lit.rate.boone': 'DN#1 R46/01-26 county chart (Boone 0.017, Marion 0.0202, Porter 0.005, Randolph 0.03); periods 2026-01-01..2026-09-30; replaced by R47 (US-INS5-007) from 2026-10-01.',
 'ma.wh.supplemental.rate': 'Circular M 2026, section G: 5% while cumulative supplemental wages are $1,107,750 or less; above, lesser of 9% of payment or 9% of excess + 5% of remainder. "5. If the result of step 4 is $1,107,750 or less, withhold 5% of the amount determined in step 3."',
 'ma.report.w2.employee_statement.due': '830 CMR 62B.2.1(d) (mass.gov, verbatim excerpt). The regulation sets no deadline for filing W-2 copies with DOR.',
 'me.payslip.required': '26 MRSA 665(1): with each payment: pay-period date, hours, total earnings, itemized deductions; same record at time of electronic transfer; electronic only with ready access and free printing.',
 'mi.local.cities.list': 'Treasury "Which cities impose an income tax?" page (verbatim text), consistent with mi.local.cities.count = 24 (US-MIB5-401, a different Treasury page). The page gives no rates.',
 'mn.pit.oracle.example_1.withholding': 'Derived from the MN Withholding Tax Instructions 2026 computer formula (p.34): biweekly 2,000.00, single, 1 allowance: 2,000 x 26 = 52,000; 52,000 - 5,300 = 46,700; 1,782.09 + (46,700 - 38,010) x 6.80% = 2,373.01; 2,373.01 / 26 = 91.27 (91 if rounded). No published page carries 91.27. Official engine: DOR Withholding Tax Calculator [US-MNR3-002].',
 'mn.garn.iwo.remit_business_days': 'Partly confirmed by the published source.',
 'mn.pit.rounding': '290.92 subd. 2a; formula step 6.',
 'mn.sdi.exists': 'No SDI/TDI program in Minnesota.',
 'mo.pit.local.kansas_city.earnings_tax.rate': 'Residents and nonresidents for work in KC; KC earnings tax page (1%).',
 'ms.labour.pay_frequency.scope': '71-1-35 via DOL WHD summary; statute text not read.',
 'multi.nonresident.la.employer_start_rule': 'Adopted rule LR 52:358 effective 2026-03-20. Drafting inconsistency C.1.a "less than 30" vs statute "30 or fewer": statute governs. LEVEL: withholding and employer reporting.',
 'multi.reciprocity.il.partners': 'Bilateral; confirmed on both sides (MULTI 2.3). Local taxes are outside reciprocity.',
 'nc.report.efile_spec.version': 'NC-3/W-2 fixed-field text file.',
 'nd.minwage.tipped.cash_wage': '7.25 x (1 - 0.33) = 4.8575 -> 4.86 (NDAC 46-02-07-03: tip credit of thirty-three percent of the minimum wage).',
 'nd.prevailing_wage.exists': 'U.S. DOL state prevailing wage table.',
 'ne.sui.wage_base.other_state_credit': '48-648.02.',
 'ne.sui.wages.401k_included': 'NAC 220 ch.2.',
 'ne.report.ui.quarterly_due': 'Late report charge 0.1% of gross wages, minimum 25, maximum 200.',
 'ne.payslip.items': '48-1230(2); hours not required for exempt employees; mail, electronic or at workplace.',
 'ny.dbl.employee.rate': "Max 0.60/week; employer pays the rest. WCL 209(3)(a): \"one-half of one per centum of the employee's wages ... but not in excess of sixty cents per week\".",
 'ny.dbl.employee.max_weekly': "WCL 209(3)(a): \"one-half of one per centum of the employee's wages ... but not in excess of sixty cents per week\".",
 'oh.pit.municipal.rate_table': 'Ohio municipal rate table (1,083 rows; 678 FIPS in force on 2026-11-01; max 3.00% Bedford).',
 'or.garn.iwo.priority_over_writ': "ORS chapter 18 garnishee response form: 'The order to withhold income has priority over the writ of garnishment, and compliance with the order will reduce or eliminate the money that I would otherwise deliver under the writ.' In force as at retrieval. The employer fee is not stated.",
 'pa.sui.new_employer.rate': 'Non-construction. Rate published in decimal form .038220 (= 3.822%).',
 'pa.ui.rate.new_employer.construction': 'Rate published in decimal form .105924 (= 10.5924%).',
 'pa.sui.employer.rate.min': 'Computed range to 10.3734. Rate published in decimal form .014190 (= 1.419%).',
 'pa.sui.employer.rate.max': 'Surcharge 9.2%; additional 0.60%. Rate published in decimal form .103734 (= 10.3734%).',
 'pa.leave.philadelphia.employer_threshold': 'Max 40 h/yr; covered if 40+ h/yr in city; partly confirmed by the published source (accrual rate not confirmed by an official source).',
 'pa.leave.philadelphia.annual_cap_hours': 'Partly confirmed by the published source.',
 'ri.wh.supplemental.rate': 'Or aggregate method.',
 'sc.labour.pay_change_notice.days': 'Written notice before changing time/place of payment (41-10-30(A)).',
 'sc.labour.direct_deposit.free_withdrawal': '41-10-40(A)-(B).',
 'sc.local_wage_tax.exists': None,
 'sc.sui.employee.rate': 'May not be deducted from wages.',
 'sc.payslip.items': '41-10-30(C); domestic and <5 employers exempt.',
 'sc.records.wage.retention_years': 'UI payroll records 5 years (Reg. 47-14, US-SCS5-007).',
 'sc.final_pay.rule': '41-10-50; treble damages.',
 'sc.term.vacation.payout': None,
 'sc.ui.coverage.agricultural.cash_per_quarter': "41-27-230(5)(a)(i): agricultural labor is employment where the person 'during any calendar quarter in either the current or preceding calendar year paid remuneration in cash of twenty thousand dollars or more to individuals employed in agricultural labor'. In force as at retrieval; the subsection applies to service 'performed after December 31, 1977'.",
 'sc.ui.coverage.agricultural.workers_in_20_weeks': "41-27-230(5)(a)(ii): or 'for some portion of a day in each of twenty different calendar weeks ... in either the current or the preceding calendar year, employed in agricultural labor ... ten or more individuals'. In force as at retrieval; the subsection applies to service 'performed after December 31, 1977'.",
 'sc.ui.coverage.domestic.cash_per_quarter': "41-27-230: domestic service in a private home, local college club or fraternity/sorority chapter is employment where the person 'paid cash remuneration of one thousand dollars or more ... in the current calendar year or the preceding calendar year to individuals employed in such domestic service in any calendar quarter'. In force as at retrieval; applies to remuneration paid 'after December 31, 1977'.",
 'sd.prevailing_wage.exists': 'U.S. DOL state prevailing wage table.',
 'tx.pit.exists': 'Const. Art. VIII s.24-a.',
 'ut.pit.oracle.example_6.wages': 'Pub 14 (Rev. 04/26), Example 6 - Use Schedule 8, Daily/Married: payroll period daily, filing status married, Utah taxable wages $175. Input of ut.pit.oracle.example_6.withholding (5).',
 'wv.ui.rate.foreign_construction': '7.5% (21A-5-5(c)) + 1% surtax (21A-5-10(b)) = 8.5; partly confirmed by the published source.',
 'wv.sui.employer.rate.max': 'Debit-balance rates 5.5/6.5/7.5 + 1% surtax (21A-5-10); the fund-solvency column applied for 2026 is not published on the agency pages.',
 'wv.payslip.items': '42 CSR 5 s.7.3; electronic if direct access.',
 'wv.report.efile_threshold.employees': 'Or payroll service; an older archived page says 25/50 (may be out of date).',
 'wy.ui.delinquent_surcharge.rate': 'Partly confirmed by the published source.',
 'ak.no_wage_tax': 'Value in force on 2026-01-01.',
 'dc.pfml.employer.rate': 'Employer only, no wage cap. Value in force on 2026-01-01.',
 'ma.pfml.split': 'DECISION (2026-11-02): payroll follows DFML - 2026 split unchanged, swap from 2027-01-01. Ch. 101/2026 s.45 (US-MAS5-026) makes ss.25-26 apply "for taxable years beginning on or after January 1, 2026"; read on the Act text, s.45 is the tax-year commencement clause shared with the c.62/c.63 provisions, while c.175M contributions are set by DFML under s.7(e) per calendar year and the Act (approved 2026-06-12) gives no retroactive re-split mechanism. Employee maximum share is 0.46% under both DFML years. Residual risk: the effective date of the split remains open.',
 'in.pit.rate': 'DOR rates page; IC 6-3-2-1 not read.',
 'pa.local.philadelphia.resident.rate': None,
 'pa.local.philadelphia.nonresident.rate': None,
 'tn.sui.employee.rate': SUI['tn.sui.employee.rate']['fnote'],
 'ne.sui.employee.rate': SUI['ne.sui.employee.rate']['fnote'],
}
GENERIC = [  # (regex, replacement) applied after EXACT, CCG files only
 (re.compile(r'\s*\(A\.3: an FAQ page, upgrade to the statute text if QA P2 flags it\)'), ''),
 (re.compile(r'(?i);?\s*register row is PARTIAL - carry the partial flag'), '; partly confirmed by the published source'),
 (re.compile(r'(?i);?\s*register row verification is weak:[^|]*'), ''),
 (re.compile(r'\s*\|\s*Synthesis [A-D]:[^|]*'), ''),
 (re.compile(r'^Synthesis [A-D]:[^|]*(\|\s*)?'), ''),
 (re.compile(r'\s*\|\s*effective_from: register row carries no date; value in force on (\d{4}-\d{2}-\d{2}) per the row'), r' Value in force on \1.'),
 (re.compile(r'\s*\((QA r\d[a-z]?(, RQ-\d+)?|stage-5 (finding|derivation))\)'), ''),
 (re.compile(r',? ?local copy 00-official-sources/[^\s,;)]+'), ''),
 (re.compile(r'Parsed with PyMuPDF; '), ''),
]
MARK = re.compile(r'F44|\bP\d\b|browser|curl|wayback|webfetch|pdfs/|ccg-sources|\bpack\b|supersedes column|\bQA\b|\.pdf\b|\.html?\b|\.txt\b|\||stage-?\d|Synthesis|chrome|local (copy|file|pdf)|register row (verification|is)|summari[sz]er', re.I)
left = []
for fp, d in data.items():
    fn = os.path.basename(fp)
    if not fn.startswith('CCG-'): continue
    for f in d.get('facts', []):
        v = f.get('note'); k = f['key']
        if not isinstance(v, str): continue
        new = v
        if k in EXACT:
            new = EXACT[k]
        else:
            for rx, rep in GENERIC: new = rx.sub(rep, new)
            new = new.replace(' | ', '; ').replace('|', '; ').strip()
        if new is None or new.strip() in ('', '-', '-;', '-.'):
            f.pop('note', None); LOG['note_edit'].append({'file': fn, 'key': k, 'old': v, 'new': None}); continue
        new = re.sub(r'^-;\s*', '', new).strip()
        if new != v:
            f['note'] = new; LOG['note_edit'].append({'file': fn, 'key': k, 'old': v, 'new': new})
        if MARK.search(f.get('note', '')): left.append((fn, k, f['note']))
    for f in d.get('facts', []):   # '|' inside string values outside the structured CT table rows
        if isinstance(f.get('value'), str) and '|' in f['value'] and not (CT_ROW.match(f['key']) or f['key'] == 'ct.wh.tables.columns'):
            left.append((fn, f['key'], 'VALUE: ' + f['value']))

# ---------- consumed_by ----------
for rid, toks in used.items():
    r = R[rid]; cur = [t for t in r['consumed_by'].split(';') if t]
    for t in sorted(toks):
        if t not in cur: cur.append(t)
    r['consumed_by'] = ';'.join(cur)
for rid in set(x[0] for x in REPOINT.values()) | {'US-CTP10-001'}:
    R[rid]['verified_on'] = TODAY

# ---------- write ----------
with open(REG, 'w', encoding='utf-8', newline='') as fh:
    w = csv.DictWriter(fh, fieldnames=FIELDS, quoting=csv.QUOTE_MINIMAL, lineterminator='\n'); w.writeheader(); w.writerows(rows)
for fp, d in data.items():
    txt = json.dumps(d, ensure_ascii=False, indent=1)
    old = open(fp, encoding='utf-8').read()
    if json.loads(old) != d:
        open(fp, 'w', encoding='utf-8').write(txt + '\n')
        LOG.setdefault('files_written', []).append(os.path.basename(fp))
LOG['marker_left_in_ccg_notes'] = left
LOG['consumed_by_added'] = {k: sorted(v) for k, v in used.items()}
json.dump(LOG, open(os.path.join(BASE, '_research', 'qa-r3c-fix', 'apply-r3c-log.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1, default=dict)
print({k: (len(v) if hasattr(v, '__len__') else v) for k, v in LOG.items()})
for x in left: print('LEFT', x)
