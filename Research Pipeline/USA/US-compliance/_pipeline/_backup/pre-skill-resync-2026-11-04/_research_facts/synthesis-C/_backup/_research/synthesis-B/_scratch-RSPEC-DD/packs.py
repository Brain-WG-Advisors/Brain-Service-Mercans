import json, re, os, csv, collections
HERE = os.path.dirname(os.path.abspath(__file__)); BASE = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
R = json.load(open(os.path.join(BASE, '_research', 'RSPEC-facts.json'), encoding='utf-8'))
DDJ = json.load(open(os.path.join(BASE, '_research', 'DD-8_sheets-facts.json'), encoding='utf-8'))
s5 = open(os.path.join(HERE, 's5.md'), encoding='utf-8').read()
rf = R['facts'] + R['_facts_pending_register_id_pattern']; df = DDJ['facts'] + DDJ['_facts_pending_register_id_pattern']
pend_r = {f['key'] for f in R['_facts_pending_register_id_pattern']}; pend_d = {f['key'] for f in DDJ['_facts_pending_register_id_pattern']}
rkeys = {f['key'] for f in rf}; dkeys = {f['key'] for f in df}
NAMES = {'FED':'Federal','MULTI':'Multistate','AK':'Alaska','AL':'Alabama','AR':'Arkansas','AZ':'Arizona','CA':'California','CO':'Colorado','CT':'Connecticut','DC':'District of Columbia','DE':'Delaware','FL':'Florida','GA':'Georgia','HI':'Hawaii','IA':'Iowa','ID':'Idaho','IL':'Illinois','IN':'Indiana','KS':'Kansas','KY':'Kentucky','LA':'Louisiana','MA':'Massachusetts','MD':'Maryland','ME':'Maine','MI':'Michigan','MN':'Minnesota','MO':'Missouri','MS':'Mississippi','MT':'Montana','NC':'North Carolina','ND':'North Dakota','NE':'Nebraska','NH':'New Hampshire','NJ':'New Jersey','NM':'New Mexico','NV':'Nevada','NY':'New York','OH':'Ohio','OK':'Oklahoma','OR':'Oregon','PA':'Pennsylvania','RI':'Rhode Island','SC':'South Carolina','SD':'South Dakota','TN':'Tennessee','TX':'Texas','UT':'Utah','VA':'Virginia','VT':'Vermont','WA':'Washington','WI':'Wisconsin','WV':'West Virginia','WY':'Wyoming'}
REPORT = {'wh_return':'State withholding return','wh_deposit':'Withholding deposits','wh_payment':'Withholding payment','wh_remit':'Withholding remittance','wh_status':'Withholding payer status','wh_qtr_report':'Quarterly wage and withholding report','annual_recon':'Annual reconciliation','w2_state':'State W-2 filing','w2_employee':'Employee W-2 duty','ui_qtr':'Quarterly UI wage report','ui_monthly':'Monthly UI wage report','pfml_qtr':'PFML / paid-leave report','pfml_ltc_qtr':'Paid Leave + WA Cares report','pfml':'PFML','new_hire':'New-hire report','contractor_report':'Contractor report (OUT of scope)','local':'Local returns','registration':'Registration','poa':'Third-party authorisation','household':'Household / agricultural','annual':'Annual forms','other_forms':'Other UI forms','oq':'Form OQ (combined)','nys45':'NYS-45 (combined)','nys1':'NYS-1 deposit','mctmt':'MCTMT','mbt':'Modified Business Tax','school_district':'School-district returns','municipal':'Municipal returns','efile':'E-file mandate','separation':'Separation notice','mass_separation':'Mass separation','tdi':'TDI','notice':'Employee notices','permit':'Permit','wc_report':'Workers compensation report','reporting_agent':'Reporting agent','form941':'Form 941','form944':'Form 944','form940':'Form 940','w2':'Form W-2/W-3','aca':'ACA 1094-C/1095-C','deposit':'Federal deposits'}
def chan(text):
    t = text.lower(); c = []
    if 'xml' in t: c.append('xml')
    if re.search(r'upload|file_upload|sftp|ftp|efw2|icesa|csv|\.txt|fixed|import|mmref|delimited|layout|record', t): c.append('file_upload')
    if re.search(r'online|portal|manual|key-and-send|keying|key entry|e-services|\bess\b|essp|\btap\b|mytax|data entry|myconnect|intime', t): c.append('online_form')
    if re.search(r'\bach\b|web service', t): c.append('api')
    if 'paper' in t and 'not accepted' not in t and 'refused' not in t: c.append('paper')
    return ' / '.join(dict.fromkeys(c)) or '-'
def fmt(v):
    return ('true' if v else 'false') if isinstance(v, bool) else str(v)
# ---------------- RSPEC pack
L = []
L.append('# RSPEC research pack - United States (stage 3, Report Spec)\n')
L.append('Synthesis B worker (RSPEC + DD), 2026-11-02. Built only from rows of `00-official-sources/legal-basis-register.csv` that are `active` (or `partial`, flagged) at tier A, as cited by the stage-5 findings (`_research/stage5/{JUR}.md` section 5). No fetching was done. Facts: `_research/RSPEC-facts.json` (key `rspec.{jur}.{report}.{attribute}`).\n')
L.append('## 0. How to read this pack\n')
L.append('- One section per jurisdiction (federal, multistate, 50 states + DC). Each opens with the **report inventory** generated from the facts (report, attribute, value, register_id, fact key) and then carries the stage-5 reporting findings verbatim, which already cite their register ids inline.')
L.append('- **Channel** is classified in the inventory as `online_form` / `file_upload` / `xml` / `api` / `paper` from the channel/format facts; where several apply they are listed in the order the authority offers them. The **portal is per institution**: the revenue department portal (withholding, W-2) is never the UI agency portal (wage report), and PFML portals are separate again (CT, DE, MA, ME, MN, WA, CO, DC). Mislabelling is check C24.')
L.append('- **Samples on disk:** FL RT XML package (4 samples + 4 test cases; RT-6 Sample.xml validates against RT_FLTransmission.xsd) [US-FLS5-023]; MI MiUI Wage Report Validator Tool and four 2026 format specs [US-MIS5-022]; CT 276-char layout (positions extracted and summed) [US-CTS5-032]; AK CSV guidelines [US-AKS5-014]; SC SUITS spec v1.6 [US-SCS5-006]; MD BEACON file format 2026-04-20 [US-MDS5-017]; IA IDR W-2 spec with RV record [US-IAS5-018]; WV IT-105 with RV record [US-WVS5-013]; AL EFW2 RS positions [US-ALS5-006]; GA Federal Format Rev 01/18 (partial) [US-GAS5-011]. No real filed sample exists for any other jurisdiction.')
L.append('- Facts marked `_facts_pending_register_id_pattern` in the JSON are verified against an active row whose id has more than three segments (e.g. `US-AR-P5-1-002`), which the facts schema 1.4.0 `register_id` pattern rejects. They are listed with a (P) mark below. This is the same convention the CCG annex workers used.\n')
L.append('## 0.1 Cross-cutting rules (all jurisdictions)\n')
L.append('- **Federal EFW2 TY2026 spec is gated** [US-FEDS5-032, gated] - every state RS/RV layout below is read against the TY2025 SSA spec until it is read. Blocking for the W-2 sheets of the Report Spec.')
L.append('- **New-hire reporting:** federal floor 20 days, fields name/address/SSN/first day of work + employer name/address/FEIN [US-FEDS5-024]; multistate electronic employers may designate one state [US-MULTIS5-006]. States shorter than 20 days: AL 7, ME 7, GA 10, VT 10, IA 15, MS 15, MA 14, RI 14, WV 14 (see table 0.2).')
L.append('- **W-2 multistate:** boxes 15-20 carry two states and two localities; more need an extra W-2 [US-MULTIS5-011]. UI wage report goes only to the `sui_state` under the localization test [US-MULTIS5-017].')
L.append('- **Scope traps:** NY files no W-2 with the state (NYS-45 Part C replaces it) [US-NYS5-010]; CA files no W-2 with EDD/FTB (DE 9C carries PIT wages) [US-CAS5-002]; IA has no annual reconciliation and rejects the SSA EFW2 file (IDR-unique format) [US-IAS5-017]; IL and ME have no annual reconciliation [US-ILS5-011, US-ME-P5-2-009]; HI HW-3 dropped [US-HIS5-005]; MS no separate reconciliation [US-MSS5-002]; VA VA-6 is NOT generated by the W-2 upload [US-VAS5-013]; AR forbids the RV record while IA, MD, MO, NE, WV require a state RV [rows in sections]. Contractor new-hire duties (CA DE 542, FL, IL, MA, ME, NH, NJ, OH, OR, VA, IA) exist in law but contractors / 1099-NEC are OUT of scope (owner instruction 2026-10-29, SKELETON-MANIFEST scope line): the Report Spec records them as scope traps, not as reports.')
L.append('- **Special populations (US-OWN-005):** household employers file Schedule H federally, not 941 [US-FED-004]; state household/agricultural variants are in the sections: CT CT-W3 HHE / CT-941 HHE [US-CTS5-014], NJ-927-H [US-NJ-P5-1-001], OR Form OA / WA / OR-STT-A [US-ORS5-010], DC UC-30-H [US-DCS5-018], FL RT-7 [US-FLS5-020], GA DOL-4 [US-GAS5-005], SD 21D/21E [US-SDS5-020], UT annual election [US-UTS5-004], LA domestic annual [US-LAS5-007]. Nonresident aliens: Pub. 515 / Notice 1392, treaty-exempt wages to 1042-S not W-2 [US-FEDS5-016]; FL, NJ refuse ITIN on the wage report [US-FLS5-024, US-NJS5-017].')
L.append('- **Language seam (US-OWN-006):** authority-facing filings in English; no statute fixing filing language located. Spanish/other-language duties attach to notices and posters only (e.g. CO DR 0995 notice in English + the employer\'s usual language [US-COS5-006]).\n')
# 0.2 new-hire table
nh = collections.OrderedDict()
for f in rf:
    m = re.match(r'rspec\.([a-z]+)\.new_hire\.deadline_(days)?', f['key'])
    if m: nh[f['key'].split('.')[1].upper()] = f
L.append('## 0.2 New-hire deadlines (all jurisdictions with a registered row)\n')
L.append('| Jur | Deadline | Note | register_id |\n|---|---|---|---|')
for j, f in sorted(nh.items()):
    L.append(f"| {j} | {fmt(f['value'])}{' days' if isinstance(f['value'], int) else ''} | {f.get('note','')} | {f['register_id']} |")
L.append('')
# 0.3 e-file thresholds
L.append('## 0.3 Electronic-filing thresholds\n')
L.append('| Fact key | Value | Unit | register_id | Note |\n|---|---|---|---|---|')
for f in rf:
    if re.search(r'efile_threshold|machine_readable|eft_threshold|accelerated_threshold|quarter_monthly', f['key']):
        L.append(f"| {f['key']} | {fmt(f['value'])} | {f.get('unit_of_measure', f.get('currency',''))} | {f['register_id']} | {f.get('note','')} |")
L.append('')
# per jurisdiction
blocks = {b.split(' ::')[0].strip(): b.split('\n', 1)[1] if '\n' in b else '' for b in re.split(r'\n#### ', s5)[1:]}
order = ['FED', 'MULTI'] + sorted(k for k in NAMES if k not in ('FED', 'MULTI'))
for j in order:
    L.append(f'## {j} - {NAMES[j]}\n')
    js = [f for f in rf if f['key'].split('.')[1] == j.lower()]
    groups = collections.OrderedDict()
    for f in js: groups.setdefault(f['key'].split('.')[2], []).append(f)
    L.append('**Report inventory (from facts).**\n')
    L.append('| Report | Attribute | Value | Channel | register_id | Fact key |\n|---|---|---|---|---|---|')
    for g, fs in groups.items():
        for f in fs:
            attr = '.'.join(f['key'].split('.')[3:])
            ch = chan(fmt(f['value'])) if re.search(r'channel|format|formats|layout|flat_file|xml|form$', attr) else ''
            mark = ' (P)' if f['key'] in pend_r else ''
            L.append(f"| {REPORT.get(g, g)} | {attr} | {fmt(f['value'])}{(' ['+f['note']+']') if f.get('note') else ''} | {ch} | {f['register_id']}{mark} | `{f['key']}` |")
    opens = [u for u in R['unresolved'] if u['key'].split('.')[1] == j.lower()]
    if opens:
        L.append('\n**Open for this jurisdiction:** ' + '; '.join(f"`{u['key']}` ({'blocking' if u.get('blocking', True) else 'non-blocking'})" for u in opens))
    L.append('\n**Stage-5 reporting findings (verbatim, register ids inline).**\n')
    L.append(blocks.get(j, '_no section 5 found_').strip() + '\n')
# reconciliation
L.append('## R. RSPEC x DD reconciliation (both directions)\n')
L.append('See also `_research/DD-research-pack.md` section R. Generated mechanically from the two facts files.\n')
MAP = [
 ('rspec.ak.ui_qtr.layout', ['dd.ak.ui.occupation_code', 'dd.ak.ui.geographic_code']),
 ('rspec.wa.ui_qtr.fields', ['dd.wa.ui.soc_code', 'dd.wa.ui.hours_quarter']),
 ('rspec.wa.ui_qtr.exempt_officers', ['dd.wa.exempt_officer']),
 ('rspec.vt.ui_qtr.fields', ['dd.vt.ui.gender_hourly']),
 ('rspec.ct.ui_qtr.new_optional_fields', ['dd.ct.ui.occupation_hours_zip']),
 ('rspec.mn.ui_qtr.fields', ['dd.mn.ui.paid_hours']),
 ('rspec.ma.ui_qtr.fields', ['dd.ma.ui.hours_work_location']),
 ('rspec.in.ui_qtr.extra_fields', ['dd.in.ui.soc_start_date']),
 ('rspec.in.new_hire.deadline_days', ['dd.in.new_hire.job_comp']),
 ('rspec.wv.ui_qtr.fields', ['dd.wv.ui.soc_county']),
 ('rspec.mo.ui_qtr.form', ['dd.mo.ui.separation_probation']),
 ('rspec.oh.ui_qtr.fields', ['dd.oh.ui.weeks_paid']),
 ('rspec.nj.ui_qtr.form', ['dd.nj.ui.base_weeks', 'dd.fl.ssn_not_itin']),
 ('rspec.pa.ui_qtr.form', ['dd.pa.ui.credit_weeks']),
 ('rspec.ne.ui_qtr.form', ['dd.ne.ui.hours_job_title']),
 ('rspec.tx.ui_qtr.enhanced_content', ['dd.tx.ui.enhanced']),
 ('rspec.fl.ui_qtr.everify_block', ['dd.fl.everify_certified']),
 ('rspec.fl.ui_qtr.itin_accepted', ['dd.fl.ssn_not_itin']),
 ('rspec.oh.w2_state.school_district_code', ['dd.oh.school_district_code']),
 ('rspec.oh.municipal.frequency', ['dd.oh.municipality_work']),
 ('rspec.pa.local.eit_lst', ['dd.pa.psd_code']),
 ('rspec.in.w2_state.format', ['dd.in.county_residence_jan1']),
 ('rspec.md.w2_state.format', ['dd.md.naics', 'dd.employer.state_account_ids']),
 ('rspec.md.new_hire.deadline_days', ['dd.md.new_hire.wage_health']),
 ('rspec.ms.new_hire.deadline_days', ['dd.ms.new_hire.extra']),
 ('rspec.ga.new_hire.deadline_days', ['dd.ga.new_hire.extra']),
 ('rspec.la.new_hire.deadline_days', ['dd.la.new_hire.occupation']),
 ('rspec.ia.new_hire.deadline_days', ['dd.ia.new_hire.health']),
 ('rspec.de.pfml_qtr.form', ['dd.de.paid_leave.hours']),
 ('rspec.or.oq.form', ['dd.or.form132.hours', 'dd.or.transit_district']),
 ('rspec.or.local.portland_metro_multnomah', ['dd.or.metro_multnomah']),
 ('rspec.ny.nys45.form', ['dd.ny.nyc_yonkers_residence']),
 ('rspec.ny.mctmt.form', ['dd.employer.ny_mctmt_zone']),
 ('rspec.mi.local.detroit', ['dd.mi.city_residence_work']),
 ('rspec.ky.local.louisville', ['dd.ky.locality']),
 ('rspec.co.local.denver_opt', ['dd.co.denver_opt']),
 ('rspec.fed.w2.box14b', ['dd.fed.w2.tipped_occupation_code']),
 ('rspec.fed.new_hire.fields', ['dd.fed.new_hire.date_first_services']),
 ('rspec.fed.aca.ale_threshold', ['dd.fed.aca.fte_tracking']),
 ('rspec.multi.ui_qtr.recipient', ['dd.multi.sui_state', 'dd.multi.work_state']),
 ('rspec.multi.pfml.state_key', ['dd.multi.sui_state']),
 ('rspec.ut.w2_state.content', ['dd.employer.state_account_ids']),
 ('rspec.mi.ui_qtr.formats', ['dd.state.ui.month12_count']),
 ('rspec.fl.ui_qtr.flat_file', ['dd.state.ui.month12_count']),
 ('rspec.ak.ui_qtr.layout', ['dd.state.ui.out_of_state_wages']),
]
L.append('### R.1 RSPEC -> DD (every report field that is not a computed amount has a DD source)\n')
L.append('| RSPEC fact | needs DD field | status |\n|---|---|---|')
gaps = []
for rk, dks in MAP:
    for dk in dks:
        st = 'ok' if (rk in rkeys and dk in dkeys) else ('MISSING RSPEC ' + rk if rk not in rkeys else 'MISSING DD ' + dk)
        if st != 'ok': gaps.append(st)
        L.append(f'| `{rk}` | `{dk}` | {st} |')
L.append('\nComputed amounts on the reports (gross/taxable/excess wages, tax withheld, contributions, base/credit weeks counts, W-2 box 12 TP/TT/TA amounts) are **WTC/report computations, not DD fields** (F26); the DD only carries the inputs listed above.\n')
L.append('### R.2 DD -> RSPEC / calculation (every DD field is consumed by a report or a calculation)\n')
L.append('| DD fact | consumers | status |\n|---|---|---|')
for f in df:
    cons = f.get('_consumers', '')
    toks = [t.strip() for t in re.split(r';', cons) if t.strip()]
    sts = []
    for t in toks:
        t0 = t.split(' ')[0]
        if t0.startswith('rspec.'):
            pref = t0.replace('*', '')
            ok = any(k.startswith(pref) or re.match(t0.replace('.', r'\.').replace('*', r'[a-z]+'), k) for k in rkeys)
            sts.append('ok' if ok else 'NO RSPEC KEY ' + t0)
        else:
            sts.append('calc/other')
    bad = [s for s in sts if s.startswith('NO')]
    gaps += bad
    L.append(f"| `{f['key']}` | {cons} | {'; '.join(bad) if bad else 'ok'} |")
L.append(f"\n**Reconciliation result:** {len(gaps)} gap(s). " + ('; '.join(gaps) if gaps else 'none: every mapped RSPEC field has a DD source and every DD field has a report or calculation consumer.') + '\n')
L.append('## Open questions\n')
L.append('Mirrors `unresolved[]` of `RSPEC-facts.json` (same keys, same wording).\n')
for u in R['unresolved']:
    L.append(f"- **{u['key']}** ({'blocking' if u.get('blocking', True) else 'non-blocking'}). {u['why']} Attempted: {'; '.join(u.get('attempted', []))}. What would close it: {u['what_would_close_it']}")
open(os.path.join(BASE, '_research', 'RSPEC-research-pack.md'), 'w', encoding='utf-8').write('\n'.join(L) + '\n')
json.dump({'gaps': gaps}, open(os.path.join(HERE, 'recon.json'), 'w'), indent=1)
print('RSPEC pack lines', len(L), 'gaps', gaps)
