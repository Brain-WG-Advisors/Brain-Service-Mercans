"""Assemble references 01, 02, 04, 05, 06 of payroll-compliance-colombia from the 2026-10-30 finals.
Same method as the France skill: verbatim conversion + provenance (bytes, md5) + line-numbered navigation index.
Only change to the artifact text: the client's name is redacted as [client]."""
import os, re, hashlib, sys

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'out')
FIN = r'C:\Users\instituto\Documents\brain-service\Research Pipeline\Colombia\2026-10-29-validacao-research\final'
REF = os.path.join(FIN, 'skill', 'payroll-compliance-colombia', 'references')
os.makedirs(REF, exist_ok=True)

def md5(p): return hashlib.md5(open(p, 'rb').read()).hexdigest()
def size(p): return f'{os.path.getsize(p):,}'
def rd(n): return open(os.path.join(OUT, n), encoding='utf-8').read()
def redact(t):
    t, n = re.subn(r'\bPMI\b', '[client]', t)
    return t, n

NBSP = '&nbsp;&nbsp;&nbsp;&nbsp;'
VERBATIM = ('This file is a complete, verbatim conversion of the artifacts above (python-docx / openpyxl, cached '
            'cell values; empty columns dropped; the first column `Row` of each table is the Excel row number, so '
            'a citation such as "WTC row 156, column Q" can be checked against the workbook). Figures, dates, codes, '
            'Spanish terminology and legal citations are reproduced exactly as delivered; nothing is summarised or '
            'rounded. The only change: the name of the client whose wage-type labels appear in a few rows is '
            'replaced by `[client]`.')

def build(title, intro, prov_rows, notes, body, level_of, fname, verbatim=VERBATIM):
    """level_of(line) -> indentation depth (0..3) or None if the line is not indexed."""
    body, nred = redact(body)
    def assemble(index_rows):
        h = [f'# {title}', '', intro, '', '', '## Provenance', '',
             '| Source artifact | Bytes | MD5 |', '|---|---|---|']
        h += [f'| `{a}` | {b} | `{c}` |' for a, b, c in prov_rows]
        h += ['', verbatim, '']
        if notes:
            h += ['', '## Reading notes (added at compilation, 2026-10-30)', '']
            h += notes
            h += ['']
        h += ['', '## Navigation index', '', 'Read with `offset` / `limit` rather than opening the whole file.', '',
              '| Line | Section |', '|---|---|']
        h += index_rows
        h += ['', '---', '', '']
        return '\n'.join(h) + body
    blines = body.split('\n')
    entries = [(i, level_of(l), l) for i, l in enumerate(blines) if level_of(l) is not None]
    dummy = [f'| 0 | x |' for _ in entries]
    first = assemble(dummy)
    offset = first.count('\n') - body.count('\n')  # number of header lines before body line 0
    rows = []
    for i, lev, l in entries:
        label = re.sub(r'^#+\s*', '', l).strip().replace('|', '\\|')
        rows.append(f'| {i + offset + 1} | {NBSP * lev}{label} |')
    txt = assemble(rows)
    # sanity: each indexed line number points at its heading
    tl = txt.split('\n')
    for (i, lev, l), r in zip(entries, rows):
        n = int(r.split('|')[1])
        assert tl[n - 1] == l, (fname, n, tl[n - 1][:60], l[:60])
    open(os.path.join(REF, fname), 'w', encoding='utf-8', newline='\n').write(txt)
    print(fname, len(txt.encode('utf-8')), 'redactions', nred)

# ---------- 01-ccg.md ----------
p = os.path.join(FIN, 'CO-CCG-001-v1.5.docx')
ccg = rd('ccg.md')
ccg = re.sub(r'^(#{1,6}) ', lambda m: '#' + m.group(1) + ' ', ccg, flags=re.M)  # shift headings one level down
notes01 = [
 '- **Version in force:** CO-CCG-001 **v1.5**, issued **30 October 2026** (Version Control row 1.5 and cover date).',
 '- **Ministry of Labour Circular 101 of 2025 is revoked** (Resolution 2708 of 2026). Where the guide still mentions it, the',
 '  mention carries "(revoked by Resolution 2708 of 2026)" and the rule rests on the statute (Law 2101 of 2021 art. 3; Labour',
 '  Code arts. 161, 168, 177, 179 as amended by Law 2466 of 2025). Never cite the Circular as the source of a rule.',
 '- The two former Res. DIAN 000013 of 2021 articles on language and currency appear in the Module 10.3 table as "(art. 26)";',
 '  the compiled number in Res. DIAN 000227 of 2025 is art. 1.5.3.8.5 (same Module, legal basis line).',
 '- Pension reform (Law 2381 of 2024): nothing applies to any 2026 period; the guide dates entry into force at 1 April 2027',
 '  (Constitutional Court C-264 of 2026). The 2027 solidarity-fund bands are written for information only.',
]
build('Colombia Country Configuration Guide (CCG) - CO-CCG-001 v1.5',
      'Complete text of the delivered Colombia CCG: all 13 modules, every rate, threshold, cap, treatment table and worked '
      'example, with the legal citations as delivered. Fiscal year 2026 (calendar year). Currency COP. Private-sector '
      'employees under the Substantive Labour Code (Código Sustantivo del Trabajo).',
      [(f'CO-CCG-001-v1.5.docx', size(p), md5(p))], notes01, ccg,
      lambda l: (0 if l.startswith('## ') else 1 if l.startswith('### ') else 2 if l.startswith('#### ') and re.match(r'#### \d', l) else None),
      '01-ccg.md')

# ---------- 02-wtc.md ----------
p = os.path.join(FIN, 'CO-WTC-001-v1.7.xlsx')
notes02 = [
 '- **Columns of the Wage Type Catalogue sheet** (header row 1). The subjection questions do not move together in Colombia, so',
 '  each is answered separately: *Subject to Tax (Retención en la Fuente)*, *Table Tax (ET art. 383)*, *Special Tax (non-resident',
 '  flat 20%, ET art. 408)*; *Subject to Health / Solidarity Pension Fund / Occupational Risk (ARL) / Payroll Levies (CCF-SENA-ICBF)',
 '  / Pension*; *Salary or Non-Salary (CST arts. 127/128)*; statutory-benefit base; electronic-payroll element; legal basis.',
 '- **`Yes/No`** in a subjection column means the answer depends on the condition in the row. For the class',
 '  `Non-Salary - pacted` it means: out of the IBC, except the part above 40% of total remuneration (Law 1393 of 2010 art. 30),',
 '  which enters health, pension and occupational risk only, never the payroll levies. `Non-Salary - non-remunerative` rows are',
 '  outside the 40% test and outside the IBC. Where the nature of a payment is unclear the row is `pacted` and the DD non-salary',
 '  pact flag decides (header of column V).',
 '- The *Mercans Code* column is empty in the whole sheet: the `CO-` codes are mnemonic and no numeric range has been assigned to',
 '  Colombia yet. Do not state a numeric code for a `CO-` line.',
 '- Sheet *Employer Sick Pay* states, as the CCG v1.5 does, two thirds for incapacity days 1-2 (Labour Code art. 227; Concepto',
 '  MinSalud 202311602174531 of 20 October 2023; default 66.67%, configurable) and the 1-SMMLV floor (Constitutional Court C-543',
 '  of 2007; default on, configurable). The incapacity / leave authorisation fields of the PILA (T2R2-057 to 060) are blank / zero',
 '  under AT2 v30; the recovery from the EPS runs outside the PILA.',
 '- Sheet *Tax Credit*: the 72-UVT dependant deduction of ET art. 336 num. 3 belongs to the annual return only; the 40% / 1,340 UVT',
 '  cap applies in the monthly withholding (Decree 1625 of 2016 art. 1.2.4.1.6 par. 3). The monthly 1/12 apportionment of the',
 '  annual UVT caps is an operating convention, still open.',
]
build('Colombia Wage Type Catalogue (WTC) - CO-WTC-001 v1.7',
      'All six sheets of the delivered Colombia WTC: Version Control, the 405-row Wage Type Catalogue with every subjection '
      'column (withholding, health, solidarity fund, occupational risk, payroll levies, pension, salary class, benefit base, '
      'electronic-payroll element and legal basis), Employer Sick Pay, Tax Credit, Global WTC Coverage and Form Reference Guide.',
      [('CO-WTC-001-v1.7.xlsx', size(p), md5(p))], notes02, rd('wtc.md'),
      lambda l: 0 if l.startswith('## Sheet:') else None, '02-wtc.md')

# ---------- 04-reports-spec.md ----------
order = [('CO-DIAN-001-NominaElectronica-Spec', 'Documento Soporte de Pago de Nómina Electrónica (+ Nota de Ajuste)', 'DIAN - SOAP 1.2 web service (machine-to-machine)', 'Monthly, one document per employee per month', 'First ten days of the following month (Res. DIAN 000227 de 2025 art. 1.5.3.4.1.1)'),
         ('CO-DIAN-002-Formulario350-Spec', 'Formulario 350 - Declaración mensual de retenciones en la fuente', 'DIAN - Muisca portal (no upload file)', 'Monthly', '7th-16th business day, by the last NIT digit (DUR 1625 de 2016 art. 1.6.1.13.2.33)'),
         ('CO-PILA-003-AportesSeguridadSocial-Spec', 'PILA - employees (Anexo Técnico 2 v30, Res. MSPS 1529 de 2026)', 'Licensed private operador de información', 'Monthly', '2nd-16th business day, by the last two digits of the NIT (Decreto 780 de 2016 art. 3.2.2.1)'),
         ('CO-DIAN-004-Formulario220-Spec', 'Formulario 220 - Certificado de ingresos y retenciones', 'Issued to each employee; not filed with DIAN', 'Annual', 'Last business day of March of the following year (DUR 1625 de 2016 art. 1.6.1.13.2.40)'),
         ('CO-DIAN-005-Formato2276-Spec', 'Formato 2276 - Información exógena, rentas de trabajo y pensiones', 'DIAN - exógena service (XML)', 'Annual', 'May-June of the following year, by NIT (Res. DIAN 000227 de 2025 art. 1.3.9.1.3)'),
         ('CO-CESANTIAS-006-ConsignacionAnual-Spec', 'Consignación anual de cesantías', 'Severance-savings fund, through an operator (not a government authority)', 'Annual', 'Before 15 February of the following year (Ley 50 de 1990 art. 99 num. 3)'),
         ('CO-PILA-007-AportesPensionados-Spec', 'PILA - pensioners paid by the employer (Anexo Técnico 3 v15)', 'Licensed private operador de información', 'Monthly', 'Decreto 780 de 2016 art. 3.2.2.1 bands')]
prov, body, idx = [], [], ['| Spec ID | Filing | Authority / channel | Frequency | Deadline |', '|---|---|---|---|---|']
for b, name, ch, fr, dl in order:
    p = os.path.join(FIN, 'specs', b + '.xlsx')
    prov.append((f'specs/{b}.xlsx (v1.1)', size(p), md5(p)))
    sid = re.match(r'(CO-[A-Z]+-\d+)', b).group(1)
    idx.append(f'| **{sid}** | {name} | {ch} | {fr} | {dl} |')
    body.append(f'\n\n## {sid} - `{b}.xlsx` (version 1.1)\n')
    body.append(re.sub(r'^## Sheet:', '### Sheet:', rd(f'spec-{b}.md'), flags=re.M))
notes04 = [
 'The seven filings (all specs at version 1.1, issued 2026-10-30):', '', *idx, '',
 '- The deadlines above are the rule; the exact calendar dates of each year come from the annual DIAN / Ministry calendars.',
 '- Inbound / non-filed: Formulario 220 is a certificate issued to the employee, not a filing. The MinTrabajo disability-hiring',
 '  report is out of the payroll scope (HR scope) and has no spec.',
 '- Formato 2276 XML element names remain **DERIVED**: the DIAN technical annex / XSD for format 2276 v4 was not obtained.',
 '- The electronic payroll document carries **no negative amount** (DIAN Concepto 014745 de 2025); corrections go by adjustment',
 '  note (TipoXML 103).',
 '- The *Example Analysis* and *Sample File* sheets use synthetic employers and employees.',
]
build('Colombia Statutory Report Specifications - seven Report Specs v1.1',
      'Every sheet of the seven delivered Colombia report specifications (Version Control, Report Matrix, Payroll Scope Summary, '
      'the field spec, File Structure, Field Options, Population Rules, Example Analysis, Sample File): electronic payroll, '
      'Form 350, PILA employees, Form 220, Format 2276, annual severance-savings deposit and PILA pensioners.',
      prov, notes04, ''.join(body),
      lambda l: 0 if l.startswith('## CO-') else 1 if l.startswith('### Sheet:') else None, '04-reports-spec.md')

# ---------- 05-data-dictionary.md ----------
p = os.path.join(FIN, 'CO-DD-001-v1.4.xlsx')
notes05 = [
 '- *ID Information* and *Country Fields* hold one row per master-data field: field name, Spanish label, description,',
 '  M / CM / O status and pre-condition, type and format, option mapper, validations, defaults, permissions, and in *Additional',
 '  Notes* the report fields that consume it. *Country Option Mappers* holds the code lists (document types, worker type and',
 '  sub-type, contract type, PILA planilla types, etc.). The two ISO sheets are the standard Mercans reference lists.',
 '- Document types, identifier rules and PILA code tables are aligned with PILA Technical Annex 2 v30 (Version Control 1.4).',
]
build('Colombia Data Dictionary - CO-DD-001 v1.4',
      'All eight sheets of the delivered Colombia Data Dictionary: Version Control, Introduction, Instructions, ID Information, '
      'Country Fields, Country Option Mappers and the two ISO reference lists.',
      [('CO-DD-001-v1.4.xlsx', size(p), md5(p))], notes05, rd('dd.md'),
      lambda l: 0 if l.startswith('## Sheet:') else None, '05-data-dictionary.md')

# ---------- 06-payslip.md ----------
p = os.path.join(FIN, 'CO_Compliance_Payslip_Generator.xlsx')
notes06 = [
 '- **Version:** Payslip Generator **v1.2**, issued 2026-10-30. Rendered variants `Colombia (EN)` and `Colombia (ES)`.',
 '- Colombia has **no Labour Code article prescribing payslip content**. The binding content rules are those of the electronic',
 '  payroll support document: Res. DIAN 000227 de 2025 art. 1.5.3.3.1 (content), art. 1.5.3.8.3 (optional graphical',
 '  representation with the QR code on every page) and art. 1.5.3.8.5 (Spanish and COP mandatory; another language or currency',
 '  may be added, never substituted). Res. DIAN 000013 de 2021 is compiled in Res. 000227 de 2025.',
 '- Amounts in the example columns are cached values of the workbook formulas (e.g. net pay 15,221,235.4).',
]
build('Colombia Payslip - CO_Compliance_Payslip_Generator v1.2 (8-sheet Mercans PSL contract)',
      'Colombia payslip mandatory content and the full line list: the setup sheet, the Compliance Payslip definition, both '
      'rendered language variants - Colombia (EN) and Colombia (ES) with the Spanish labels - the Payslip Spec, Field Option, '
      'Population Range and Unit Rate Details.',
      [('CO_Compliance_Payslip_Generator.xlsx', size(p), md5(p))], notes06, rd('payslip.md'),
      lambda l: 0 if l.startswith('## Sheet:') else None, '06-payslip.md')
