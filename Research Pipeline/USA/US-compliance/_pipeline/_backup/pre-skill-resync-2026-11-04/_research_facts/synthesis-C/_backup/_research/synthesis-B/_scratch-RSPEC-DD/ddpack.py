import json, re, os
HERE = os.path.dirname(os.path.abspath(__file__)); BASE = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
DDJ = json.load(open(os.path.join(BASE, '_research', 'DD-8_sheets-facts.json'), encoding='utf-8'))
df = DDJ['facts'] + DDJ['_facts_pending_register_id_pattern']; pend = {f['key'] for f in DDJ['_facts_pending_register_id_pattern']}
recon = json.load(open(os.path.join(HERE, 'recon.json')))
def sheet(k):
    if k.startswith('dd.state.w4.') or k.startswith('dd.fed.w4') or k in ('dd.fed.nra.flag',): return 'Country Fields - tax certificates'
    if k.startswith('dd.multi.') or k in ('dd.la.workday_counter',): return 'Country Fields - work/residence jurisdiction'
    if re.match(r'dd\.(oh|pa|in|md|ny|mi|ky|or|co|ia)\.(school|municip|psd|county|nyc|city|locality|metro|transit|denver)', k): return 'Country Fields - local jurisdiction codes'
    if k.startswith('dd.employer.') or k == 'dd.md.naics': return 'ID Information - employer / account identifiers'
    if 'new_hire' in k or k in ('dd.fed.special_population.category',): return 'Country Fields - hire data and special populations'
    if 'language' in k: return 'Country Fields - notice language seams'
    return 'Country Fields - report-specific fields'
CLASS = {'dd.wa.ui.hours_quarter': 'period input (time data)', 'dd.mn.ui.paid_hours': 'period input (time data)', 'dd.ma.ui.hours_work_location': 'period input + master (work location)', 'dd.ct.ui.occupation_hours_zip': 'master (occupation, ZIP) + period input (hours)', 'dd.de.paid_leave.hours': 'period input (time data)', 'dd.or.form132.hours': 'period input (time data)', 'dd.nj.ui.base_weeks': 'derived per quarter from wages: WTC/report computation, keep out of DD master data (F26); DD carries no input beyond pay dates', 'dd.pa.ui.credit_weeks': 'derived per quarter (F26), as NJ base weeks', 'dd.oh.ui.weeks_paid': 'derived per quarter (F26)', 'dd.state.ui.month12_count': 'derived from employment status on the 12th (report computation)', 'dd.state.ui.out_of_state_wages': 'period input (prior wages reported to other states / predecessor)', 'dd.la.workday_counter': 'period input accumulated per year', 'dd.multi.ny_convenience_days': 'period input (working days)', 'dd.multi.pa_working_days': 'period input (working days)', 'dd.mo.ui.separation_probation': 'master (separation date) + derived flag', 'dd.fed.aca.fte_tracking': 'period input (hours) + derived monthly status', 'dd.nv.mbt_wage_match': 'rule'}
L = ['# DD research pack - United States (stage 4, Data Dictionary, unit 8_sheets)\n']
L.append('Synthesis B worker (RSPEC + DD), 2026-11-02. Built only from active/partial tier-A register rows cited by the stage-5 findings; no fetching. Facts: `_research/DD-8_sheets-facts.json` (key `dd.{scope}.{field}`; `_consumers` names the report or calculation each field feeds).\n')
L.append('## 0. Structure\n')
L.append('The DD workbook has 8 sheets (mercans-artifact-toolkit structural contract, precedent `CZ_Data_Dictionary_V2_0.xlsx`): Version Control - Introduction - Instructions - ID Information - Country Fields - Country Option Mappers - Currency Codes (ISO 4217) - Country Codes (ISO 3166-1). This pack is organised by the sheets that carry country content: **ID Information**, **Country Fields** (split below by family), **Country Option Mappers**. Currency = USD only, 2 minor units (build manifest). Country = US; state codes are an option mapper, not ISO 3166-1 rows.\n')
L.append('**F26 discipline.** Per-payrun computed amounts (tax withheld, taxable/excess wages, contributions, W-2 box 12 TP/TT/TA amounts, NV MBT wage match, AZ sick-time balances on the paycheck) are WTC/PSL/report computations and are deliberately **not** DD facts. Each field below is classified master / period input / derived; the derived ones are listed so the builder can exclude them consciously.\n')
L.append('**Special populations (US-OWN-005).** All populations IN for the federal layer: ordinary, nonresident alien, statutory employee, household, agricultural, clergy, employee abroad -> one option-mapper field `special_population.category` [US-OWN-005, owner row; carried in `_owner_scope` of the facts file]; NRA needs its own flag and treaty data [US-FEDS5-016]; WA exempt corporate officers [US-WAS5-027]; FL E-Verify employer certification [US-FLS5-010]. Contractors / 1099-NEC OUT of scope (owner instruction 2026-10-29, SKELETON-MANIFEST scope line) - no contractor master data.\n')
L.append('**Language seams (US-OWN-006).** No DD language field is needed for the payslip (English). Two notice seams need data: NY employee primary language [US-NYP9L-001] and CO workforce first languages at 5% [US-COL-001].\n')
groups = {}
for f in df: groups.setdefault(sheet(f['key']), []).append(f)
for g in sorted(groups):
    L.append(f'## {g}\n')
    L.append('| DD fact key | Field / content | Class | Consumers | register_id | Note |\n|---|---|---|---|---|---|')
    for f in groups[g]:
        v = f['value'] if not isinstance(f['value'], bool) else str(f['value']).lower()
        L.append(f"| `{f['key']}` | {v}{' ' + f.get('unit_of_measure','') if f.get('unit_of_measure') else ''} | {CLASS.get(f['key'], 'master data')} | {f.get('_consumers','')} | {f['register_id']}{' (P)' if f['key'] in pend else ''} | {f.get('note','')} |")
    L.append('')
L.append('## Country Option Mappers (enumerations to carry)\n')
L.append('- Federal W-4 filing status: Single/MFS; MFJ/QSS; HoH [US-FEDS5-006]. State certificate codes: CT-W4 A-F [US-CTS5-011]; per-state allowance/exemption enumerations per form in the tax-certificate table.')
L.append('- Special population category (7 values) [US-OWN-005].')
L.append('- Ohio school district 4-digit codes (9999 = full-year nonresident) [US-OHS5-019, 2026 changes US-OHS5-018]; PA PSD codes [US-PAS5-017/018]; Indiana county codes (2-digit, EFW2 RS 306-307) [US-INS5-013]; Maryland county local-rate tables [US-MD-P5-1-001].')
L.append('- SOC codes (6-digit) for WA, IN, WV, AK (6/8-digit occupational code) [US-WAS5-013, US-INS5-014, US-WV-UI-001, US-AKS5-014]; AK 2-digit geographic codes [US-AKS5-014]; NAICS (MD RV record) [US-MDS5-016].')
L.append('- UI adjustment reason codes: MD 00-10 [US-MDS5-017]; MA adjustment reason code [US-MAS5-018].')
L.append('- Transport-worker type (motor / rail / air / seaman) [US-MULTIS5-001..004].\n')
L.append('## R. RSPEC x DD reconciliation\n')
L.append('The mapping table (RSPEC -> DD) and the consumer check (DD -> RSPEC/calc) are in `_research/RSPEC-research-pack.md` section R; both directions were generated mechanically from the two facts files. ' + (f"Result: {len(recon['gaps'])} gap(s): " + '; '.join(recon['gaps']) if recon['gaps'] else 'Result: 0 gaps.') + ' Report fields that depend on still-unread layouts (TX 204.0025 enhanced fields, CT Q3 2026 optional fields, WA PFML report fields) are carried as DD fields now and flagged in Open questions.\n')
L.append('## Open questions\n')
L.append('Mirrors `unresolved[]` of `DD-8_sheets-facts.json`.\n')
for u in DDJ['unresolved']:
    L.append(f"- **{u['key']}** ({'blocking' if u.get('blocking', True) else 'non-blocking'}). {u['why']} Attempted: {'; '.join(u.get('attempted', []))}. What would close it: {u['what_would_close_it']}")
L.append('\nThe RSPEC open questions on unread file layouts also limit the DD wherever a layout could add a field (see `RSPEC-research-pack.md` Open questions).')
open(os.path.join(BASE, '_research', 'DD-research-pack.md'), 'w', encoding='utf-8').write('\n'.join(L) + '\n')
print('DD pack lines', len(L))
