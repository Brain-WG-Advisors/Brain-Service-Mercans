# -*- coding: utf-8 -*-
"""Declared release edits (CO, issue 2026-10-30). Read by release.py (applies them) and by
release_crosscheck.py (proves that these are the ONLY text differences between each approved DRAFT and its final).

xlsx: {(sheet, cell): [('sub', old, new), ...]} or ('set', text) or ('num', value)
docx: [(old, new), ...]  - 'old' must occur exactly once in the accepted text of exactly one paragraph.
Style-only change, applied to every workbook and not listed here: every review highlight fill FFDDEBF7 is removed
(the cell keeps all its other formatting; see release.py, unblue()).
"""
ISSUE = '2026-10-30'
ISSUE_SERIAL = '46325'  # Excel serial of 2026-10-30 (Version Control dates in the DD / WTC are serial numbers)
AUTHOR = 'Wallisson Gomes'

P_CONF = 'Position - confidence '

VC_SPEC = {
 'NE': "Statutory validation of the specification: sample XML aligned with XSD v1.0.6 (namespaces, adjustment-note element names, illustrative CUNE); worked example with the employee withholding not rounded (617,232) and the dependent totals; service time on the 360/30 convention (1880.00); numbering prefix, payment-means list, overtime hours format and the night window (Ley 2101 de 2021, Ley 2466 de 2025); no negative amounts (DIAN Concepto 014745 de 2025); days not worked; transmitted-payload size; occupational incapacity types; rejected-number rule.",
 'F350': "Statutory validation of the specification: casilla 28 disabled from the June 2026 period (DIAN Oficio 15662 de 2026); worked example on the unrounded employee withholding, approximated to the nearest 1,000 only on the return (DUR 1625 de 2016 art. 1.6.1.11.11); casilla 996 added (File Structure, Sample File).",
 'F220': "Statutory validation of the specification: gross income total 169,440,000 and the non-resident variant (20% = 33,888,000); casilla 59 six-month average 13,000,000 with a note on its composition; annual withholding 12 x 617,232 approximated to the nearest 1,000.",
 'F2276': "Statutory validation of the specification: official XSD element names; N22 gross income 169,440,000; N33 six-month average 13,000,000 with a note on its composition; N29 withholding 7,406,784 (no 1,000 approximation in this format).",
 'CES006': "Statutory validation of the specification: casillas 48 / 49 in the worked example; transport allowance in the severance base (Ley 1 de 1963 art. 7); fund-code mapping; CST art. 310 without a minimum month (Corte Constitucional C-078 de 2023); minimum wage and transport allowance (Decretos 1469 and 1470 de 2025).",
 'PILA003': "Statutory validation of the specification: ET art. 114-1 exoneration test (monthly salary and health contribution base both below 10 SMMLV, PILA campo 76); integral salary contribution base with the Ley 1393 excess; seven-position rate fields written as decimals; contributor type 75 and contributor subtypes; solidarity fund bands; document types and identifier rules (AT2 v30); correction returns (type N); header sequence, legal-representative block, hire date, contributor types and work-centre rules; system names aligned with CO-DD-001 v1.4.",
 'PILA007': "Statutory validation of the specification: document type PC (PEP-Tutor) added to the identification lists; pension field note (M104); IBC rounding note (P108).",
}

XLSX = {
 'WTC': {
  ('Version Control', 'B19'): ('set', '1.7'),
  ('Version Control', 'C19'): ('num', ISSUE_SERIAL),
  ('Version Control', 'D19'): ('set', "Statutory validation against an independent recalculation and the primary sources: payroll-levy, occupational-risk and statutory-benefit-base flags of long-term disability, incapacity, maternity / paternity / parental leave and vacation compensated in cash; cooperative associated-work compensation and representation expenses taxable, occasional per diem exempt only under DUR 1625 de 2016 art. 1.2.4.7; employer voluntary contributions to the mandatory pension fund non-taxable up to 25% / 2,500 UVT; night premium on rest days outside the vacation base; interest on severance savings taxable; integral salary contribution base with the Ley 1393 excess and the payroll-levy base without it; termination indemnity base (CST art. 127 salary with its variable parts); the 72-UVT dependant deduction left to the annual return (Tax Credit sheet); salary-nature values of column V; profit-sharing and transport allowance notes."),
  ('Version Control', 'E19'): ('set', 'Approved'),
  ('Version Control', 'F19'): ('set', AUTHOR),
  ('Wage Type Catalogue', 'D123'): [('sub', 'Position - confidence 75%, confirm with UGPP. Configurable.', 'This is an interpretation; confirm with UGPP. Configurable.')],
  ('Wage Type Catalogue', 'D134'): [('sub', 'Position - confidence 70%, confirm with the client\'s plan documents (depends on the plan design).', 'Confirm against the client\'s plan documents (depends on the plan design).')],
  ('Wage Type Catalogue', 'D156'): [('sub', 'Position - confidence 70%, confirm with a labour-law review (no express CSJ ruling located).', 'This is an interpretation (no express Supreme Court ruling located); confirm with a labour-law review.')],
  ('Wage Type Catalogue', 'D324'): [('sub', 'Position - confidence 70%, confirm with a labour-law review (no express CSJ ruling located).', 'This is an interpretation (no express Supreme Court ruling located); confirm with a labour-law review.')],
 },
 'DD': {
  ('Version Control', 'B17'): ('set', '1.4'),
  ('Version Control', 'C17'): ('num', ISSUE_SERIAL),
  ('Version Control', 'D17'): ('set', "Statutory validation against the primary sources: new fields for subsidised-regime permanence (worker type 75), PILA salary type, special pension rate indicator, work-centre ARL economic activity and the work-centre / risk-class link, housing-loan interest and voluntary-savings certificates, termination cause, and pension payer / pensioner data for CO-PILA-007; apprentice codes under Ley 2466 de 2025; document types and identifier rules aligned with PILA Technical Annex 2 v30; bank payment-method list; mandatory / conditional flags and references aligned with the report specifications v1.1."),
  ('Version Control', 'E17'): ('set', 'Approved'),
  ('Version Control', 'F17'): ('set', AUTHOR),
  ('ID Information', 'H7'): [('sub', 'Position - confidence 75%, confirm with DIAN: the bank / non-bank classification of each code is ours.', 'The bank / non-bank classification of each code is an interpretation; confirm with DIAN.')],
  ('ID Information', 'V19'): [('sub', 'confirm with RA.', 'confirm the format with the registering Chamber of Commerce.')],
  ('Country Fields', 'W95'): [('sub', ' (DD-24).', '.')],
  ('Country Fields', 'B108'): ('set', 'Additions v1.4: subsidised-regime permanence, PILA salary type, special pension rate indicator, work-centre ARL economic activity, housing-loan interest certificate, pension payer and pensioner data for CO-PILA-007'),
  ('Country Fields', 'W111'): [('sub', 'Added with Worker Type 75 (DD-05).', 'Added with Worker Type 75.')],
  ('Country Fields', 'W175'): [('sub', ' DD-10 (COVAL round 4).', '')],
  ('Country Fields', 'W176'): [('sub', ' Position - confidence 80%. DD-15 (COVAL round 4).', '')],
  ('Country Fields', 'W177'): [('sub', ' Position - confidence 80%. DD-15 (COVAL round 4).', '')],
  ('Country Fields', 'W178'): [('sub', ' DD-16 (COVAL round 4).', '')],
  ('Country Fields', 'W179'): [('sub', ' DD-24 (COVAL round 4).', '')],
 },
 'NE': {
  ('Field Options', 'D68'): [('sub', ' Position - confidence 65%, confirm with DIAN.', ' Confirm with DIAN.')],
  ('Field Options', 'D69'): [('sub', ' Position - confidence 65%, confirm with DIAN.', ' Confirm with DIAN.')],
  ('Example Analysis', 'C44'): [('sub', " (the value used earlier was the Technical Annex's own example, p.247)", '')],
 },
 'F220': {
  ('Example Analysis', 'C26'): [('sub', 'is our reading;', 'is an interpretation;'), ('sub', ' Position - confidence 75%, confirm with DIAN.', ' Confirm with DIAN.')],
 },
 'F2276': {
  ('Example Analysis', 'C28'): [('sub', 'is our reading;', 'is an interpretation;'), ('sub', ' Position - confidence 75%, confirm with DIAN.', ' Confirm with DIAN.')],
  ('Example Analysis', 'D37'): [('sub', 'THREE DIFFERENT DEADLINE RULES across the pipeline:', 'THREE DIFFERENT DEADLINE RULES across these filings:')],
 },
 'PILA003': {
  **{('PILA Spec', 'P%d' % r): [('sub', ' Position - confidence 75%, confirm with the information operator during set-up.', ' Confirm with the information operator during set-up.')] for r in (114, 123, 137, 139, 141, 143, 145)},
  ('Population Rules', 'C17'): [('sub', 'T2R2-061 (nine positions) is unchanged. Position - confidence 75%, confirm with the information operator during set-up.', 'T2R2-061 (nine positions) keeps its own format. Confirm with the information operator during set-up.')],
 },
 'PAYSLIP': {
  ('Payslip Spec', 'B85'): ('set', 'v1.2'),
  ('Payslip Spec', 'C85'): ('set', ISSUE),
  ('Payslip Spec', 'D85'): ('set', "Statutory validation against an independent recalculation and the primary sources: worked example completed (solidarity fund, withholding, occupational risk, family compensation fund, severance savings and interest, contribution base), net pay 15,221,235.40 and employer contributions 5,764,300; prima and vacation provisions at 1/12 and 15/360; payslip fields of Res. DIAN 000227 de 2025 (payment means, generation time, signature, provider and software); citations updated (Res. DIAN 000227 de 2025, Decretos 1469 and 1470 de 2025, ET art. 114-1, occupational-risk classes, severance savings)."),
  ('Payslip Spec', 'E85'): ('set', AUTHOR),
  ('Payslip Spec', 'E12'): [('sub', 'Format XXX.XXX.XXX-DV.', 'Format NNN.NNN.NNN-DV (nine digits and the check digit).')],
  ('Unit Rate Details', 'G2'): ('set', 'Illustrative account codes; align them to the CO-WTC-001 wage-type codes during set-up.'),
 },
}

# specs: Version Control row 14 and Report Matrix version
for _k in ('NE', 'F350', 'F220', 'F2276', 'CES006', 'PILA003', 'PILA007'):
    d = XLSX.setdefault(_k, {})
    d[('Version Control', 'B14')] = ('set', '1.1')
    d[('Version Control', 'C14')] = ('set', ISSUE)
    d[('Version Control', 'D14')] = ('set', VC_SPEC[_k])
    d[('Version Control', 'E14')] = ('set', 'Approved')
    d[('Version Control', 'F14')] = ('set', AUTHOR)
    d[('Report Matrix', 'B19')] = ('set', 'v1.1')

DOCX = {
 'CCG': [
  ('CO-CCG-001  ·  Version 1.4  ·  Fiscal Year 2026', 'CO-CCG-001  ·  Version 1.5  ·  Fiscal Year 2026'),
  ('CO-CCG-001 v1.4', 'CO-CCG-001 v1.5'),
  ('1.5 (DRAFT)', '1.5'),
  ('29 October 2026', '30 October 2026'),
  ('Mercans Compliance (COVAL)', AUTHOR),
  ('Validation corrections (COVAL): A-01, A-02, A-03, A-04, A-05, A-06, A-09, A-13, A-15, A-16, F-01, F-03, F-04, F-05, F-06. Round 4 (30 October 2026, official research of 30 October): T4-1, T4-2, T4-3, T4-4, T4-5, A-08, A-10, A-11, A-12, A-14, F-09, F-10, F-11, F-12, F-13 (provisional position), F-14, SIM-06, SIM-10.',
   "Statutory validation against an independent recalculation and the primary sources: termination and non-resident withholding; Tax Code art. 114-1 exoneration (monthly salary and health contribution base both below 10 minimum wages; PILA field 76); integral salary contribution base with the Law 1393 excess; 40% test limited to pacted non-salary payments; payroll-levy base without the Law 1393 excess; 72-unit dependant deduction left to the annual return, with the 40% / 1,340-unit cap kept in withholding; occupational-risk class IV maximum 6.960%; Form 350 correction period of 3 years; record-retention, residence and overtime-divisor wording; transport allowance pro rata to days worked; vacation cash compensation; night premium on rest days; pension contribution and 2027 solidarity bands; garnishment priority; public-employer, voluntary-contribution, occupational-incapacity and severance-savings rules; non-resident severance; citations of the revoked Circular 101 of 2025 replaced by the statute."),
  ('Position — confidence 75%, confirm with the Ministry of Labour: interpretation consistent with Ministry of Labour Radicado', 'This is an interpretation (confirm with the Ministry of Labour), consistent with Ministry of Labour Radicado'),
  ('Position — confidence 70%, confirm with DIAN: flat 20% on the nominal payment', 'Interpretation (confirm with DIAN): flat 20% on the nominal payment'),
  ('with a 1-minimum-wage floor (operating practice; legal basis to be confirmed)', 'with a 1-minimum-wage floor (operating practice; legal basis not confirmed)'),
  ('floored at 1 minimum wage (operating practice; legal basis to be confirmed)', 'floored at 1 minimum wage (operating practice; legal basis not confirmed)'),
  ('The result is unchanged: 83.40 tax units is within the 0% band.', 'The withholding is nil: 83.40 tax units is within the 0% band.'),
 ],
}

# --- second pass (cross-check findings): pipeline references, obsolete internal note, open-point markers
XLSX['WTC'][('Global WTC Coverage', 'C14')] = [('sub', 'Configured fresh for Colombia from CO-CCG-001 v1.0 Modules 3-10, the 04-reports-spec files, and the primary law in 00-official-sources/pdfs/ (', 'Configured for Colombia from CO-CCG-001 Modules 3-10, the report specifications and the primary law ('), ('sub', " NOT copied from Czechia, Cote d'Ivoire or any other country.", '')]
XLSX['WTC'][('Global WTC Coverage', 'B30')] = [('sub', ' OUT OF SCOPE of employer gross-to-net per scope_manifest;', ' OUT OF SCOPE of employer gross-to-net;')]
XLSX['DD'][('Country Fields', 'W40')] = [('sub', 'INTERNAL CONFLICT TO ESCALATE: CCG Module 2.2 states a non-resident employee is withheld on the same art. 383 table, which contradicts the Module 6.2 matrix and the scope_manifest; Module 6.2 is the authoritative text and is the basis of this field.', 'Consistent with CCG Module 1 and the Module 6.2 matrix (DIAN Concepto 011108 of 2026, item 10: art. 408-415 withholding until the individual acquires tax residence).')]
XLSX['DD'][('Country Option Mappers', 'G64')] = [('sub', ' and descoped in scope_manifest;', ' and out of scope;')]
for _r in ('D33', 'D34', 'D35', 'D41', 'D42', 'D43', 'D53', 'D54', 'D55', 'D58'):
    XLSX['PAYSLIP'][('Payslip Spec', _r)] = [('sub', '[VERIFY WITH RA - align to actual CO-WTC account codes once available]', '(Align the account codes with the CO-WTC-001 wage types at set-up.)')]
for _r in ('D75', 'D76', 'D77', 'D78', 'D79', 'D80', 'D81'):
    XLSX['PAYSLIP'][('Payslip Spec', _r)] = [('sub', '[VERIFY WITH RA - HRB mapping to be assigned] ', '[HRB mapping assigned at set-up] ')]
DOCX['CCG'] += [
  ('A placeholder must be emitted or validation fails.', 'A substitute value must be emitted or validation fails.'),
  ('Mercans default: 66.67%, configurable. Resolution: Decree 780 de 2016', 'Mercans default: 66.67%, configurable. Basis: Decree 780 de 2016'),
  ('The Mercans default (66.67%, configurable) matches; the citation is added and the default is unchanged.', 'The Mercans default (66.67%, configurable) matches this concept.'),
  ('OUT OF SCOPE -- HR-scope, see scope_manifest.json (headcount/qualification data sourced outside payroll)', 'OUT OF SCOPE -- HR scope (headcount/qualification data sourced outside payroll)'),
]

# --- Test 0 corrections (independent reviewer, 2026-10-30): see test0_corrections.py
import test0_corrections as _T0
DOCX['CCG'] += _T0.DOCX
for _a, _cells in _T0.XLSX.items():
    for _k, _ops in _cells.items():
        if _k in XLSX.setdefault(_a, {}):
            assert isinstance(XLSX[_a][_k], list) and isinstance(_ops, list), _k
            XLSX[_a][_k] = XLSX[_a][_k] + _ops
        else:
            XLSX[_a][_k] = _ops

# --- Post-release review 2026-10-30 (residual Test 0 items): see residuos_corrections.py
# xlsx op ('formula', f, cached_value) rewrites a formula cell (release.py) and is proven by release_crosscheck.py
import residuos_corrections as _RS
DOCX['CCG'] += _RS.DOCX
for _a, _cells in _RS.XLSX.items():
    for _k, _ops in _cells.items():
        if _k in XLSX.setdefault(_a, {}):
            assert isinstance(XLSX[_a][_k], list) and isinstance(_ops, list), _k
            XLSX[_a][_k] = XLSX[_a][_k] + _ops
        else:
            XLSX[_a][_k] = _ops

# --- Post-release review 2026-10-30, second pass (CCG x specs / WTC / Payslip consistency): see consistencia_corrections.py
import consistencia_corrections as _CS
DOCX['CCG'] += _CS.DOCX
for _a, _cells in _CS.XLSX.items():
    for _k, _ops in _cells.items():
        if _k in XLSX.setdefault(_a, {}):
            assert isinstance(XLSX[_a][_k], list) and isinstance(_ops, list), _k
            XLSX[_a][_k] = XLSX[_a][_k] + _ops
        else:
            XLSX[_a][_k] = _ops
