# -*- coding: utf-8 -*-
"""Declared release edits (CO, issue 2026-11-02: CCG v1.6, WTC v1.8, DD v1.5, five specs v1.2, Payslip v1.3, SIR v1.3).
Read by release_r5.py (applies them) and by release_crosscheck_r5.py (proves that these are the ONLY text differences
between each DRAFT-R5 and its final). Same format as release_edits.py:
xlsx: {(sheet, cell): ('set', text) | ('num', value) | [('sub', old, new), ...]}
docx: [(old, new), ...]  - 'old' occurs exactly once in the accepted text of exactly one paragraph.
FOOTER: {part: [(old, new)]} - text edits in the docx footer parts.
Style-only change, applied to every workbook and not listed here: every review highlight fill FFDDEBF7 is removed.
"""
ISSUE = '2026-11-02'
ISSUE_SERIAL = '46328'  # Excel serial of 2026-11-02
AUTHOR = 'Wallisson Gomes'
REL = ' Released 2026-11-02 — approved by Wallisson Gomes.'
SP = 'Statutory validation, second pass: '

# DRAFT-R5 -> final (paths relative to the validation folder) ; base = final in force before (moved to _historico)
H = 'final/_historico/2026-10-30/'
R5 = 'revisao/rodada5/'
PAIRS = [
 # (artefato, draft, base, final, versao)
 ('CCG', R5 + 'CO-CCG-001-v1.6-DRAFT-R5.docx', H + 'CO-CCG-001-v1.5.docx', 'CO-CCG-001-v1.6.docx', '1.6'),
 ('WTC', R5 + 'CO-WTC-001-v1.8-DRAFT-R5.xlsx', H + 'CO-WTC-001-v1.7.xlsx', 'CO-WTC-001-v1.8.xlsx', '1.8'),
 ('DD', R5 + 'CO-DD-001-v1.5-DRAFT-R5.xlsx', H + 'CO-DD-001-v1.4.xlsx', 'CO-DD-001-v1.5.xlsx', '1.5'),
 ('NE', R5 + 'CO-DIAN-001-NominaElectronica-Spec-v1.2-DRAFT-R5.xlsx', H + 'specs/CO-DIAN-001-NominaElectronica-Spec.xlsx', 'specs/CO-DIAN-001-NominaElectronica-Spec.xlsx', '1.2'),
 ('F220', R5 + 'CO-DIAN-004-Formulario220-Spec-v1.2-DRAFT-R5.xlsx', H + 'specs/CO-DIAN-004-Formulario220-Spec.xlsx', 'specs/CO-DIAN-004-Formulario220-Spec.xlsx', '1.2'),
 ('F2276', R5 + 'CO-DIAN-005-Formato2276-Spec-v1.2-DRAFT-R5.xlsx', H + 'specs/CO-DIAN-005-Formato2276-Spec.xlsx', 'specs/CO-DIAN-005-Formato2276-Spec.xlsx', '1.2'),
 ('CES006', R5 + 'CO-CESANTIAS-006-ConsignacionAnual-Spec-v1.2-DRAFT-R5.xlsx', H + 'specs/CO-CESANTIAS-006-ConsignacionAnual-Spec.xlsx', 'specs/CO-CESANTIAS-006-ConsignacionAnual-Spec.xlsx', '1.2'),
 ('PILA003', R5 + 'CO-PILA-003-AportesSeguridadSocial-Spec-v1.2-DRAFT-R5.xlsx', H + 'specs/CO-PILA-003-AportesSeguridadSocial-Spec.xlsx', 'specs/CO-PILA-003-AportesSeguridadSocial-Spec.xlsx', '1.2'),
 ('PAYSLIP', R5 + 'CO_Compliance_Payslip_Generator-v1.3-DRAFT-R5.xlsx', H + 'CO_Compliance_Payslip_Generator.xlsx', 'CO_Compliance_Payslip_Generator.xlsx', '1.3'),
]
UNCHANGED = ['specs/CO-DIAN-002-Formulario350-Spec.xlsx', 'specs/CO-PILA-007-AportesPensionados-Spec.xlsx']
SIR = (R5 + 'CO-SIR-001-v1.3-DRAFT-R5-texto.md', H + 'CO-SIR-001-v1.2-texto-final.md', 'CO-SIR-001-v1.3-texto-final.md', '1.3')

VC_SPEC = {
 'NE': SP + "the 790-UVT and 1,340-UVT caps tracked year-to-date, with no monthly one-twelfth limit (Population Rules, Example Analysis); severance savings and their interest not withheld for non-residents (Population Rules); bank attributes for the account-crediting payment methods 42, 45, 47 and 98 (Nomina Electronica Spec NIE066, Population Rules).",
 'F220': SP + "casilla 59 six-month average 12,000,000 (the six months of the year before the deposit, salary only); severance savings and their interest not withheld for non-residents (non-resident variant 20% x 156,000,000 = 31,200,000); the 790-UVT and 1,340-UVT caps tracked year-to-date (Field Options).",
 'F2276': SP + "N33 six-month average 12,000,000 (the six months of the year before the deposit, salary only); severance savings and their interest not withheld for non-residents (non-resident N29 = 20% x 156,000,000 = 31,200,000; control N29 / (N22 - N18 to N20)).",
 'CES006': SP + "severance savings and their interest not withheld for non-residents (Report Matrix).",
 'PILA003': SP + "occupational-risk rate T2R2-061 written as a decimal with a point, zero-filled to nine positions (0.0052200), as the other rate fields (PILA Spec, Population Rules, Example Analysis, Sample File).",
}

XLSX = {
 'WTC': {
  ('Version Control', 'B20'): ('set', '1.8'),
  ('Version Control', 'C20'): ('num', ISSUE_SERIAL),
  ('Version Control', 'D20'): ('set', SP + "the 790-UVT and 1,340-UVT caps and the shared 3,800-UVT cap of voluntary pension funds and AFC / AVC accounts are annual and tracked year-to-date, with no monthly one-twelfth limit (Tax Credit; Global WTC Coverage); severance savings and their interest are not withheld for any employee, resident or non-resident (rows 120-122 and 321-322); third-party meal payments 'Non-Salary - pacted' (row 346); nomina electronica elements of the pacted education allowances, the holiday allowance and the bonus rows (column Y) and of the header of column V." + REL),
  ('Version Control', 'E20'): ('set', 'Approved'),
  ('Version Control', 'F20'): ('set', AUTHOR),
 },
 'DD': {
  ('Version Control', 'B18'): ('set', '1.5'),
  ('Version Control', 'C18'): ('num', ISSUE_SERIAL),
  ('Version Control', 'D18'): ('set', SP + "bank attributes only for account-crediting payment methods (ID Information rows 7-9); payment method 98 (CATS) added to the Payment Method mapper (row 104)." + REL),
  ('Version Control', 'E18'): ('set', 'Approved'),
  ('Version Control', 'F18'): ('set', AUTHOR),
 },
 'PAYSLIP': {
  ('Payslip Spec', 'B86'): ('set', 'v1.3'),
  ('Payslip Spec', 'C86'): ('set', ISSUE),
  ('Payslip Spec', 'D86'): ('set', SP + "the 790-UVT and 1,340-UVT caps are annual and tracked year-to-date (no monthly one-twelfth limit); worked example (August 2026, same pay since January) withholding 1,993,152.00 and net pay 15,478,848.00; note on the withholding (row 82)." + REL),
  ('Payslip Spec', 'E86'): ('set', AUTHOR),
 },
}
for _k, _d in VC_SPEC.items():
    d = XLSX.setdefault(_k, {})
    d[('Version Control', 'B15')] = ('set', '1.2')
    d[('Version Control', 'C15')] = ('set', ISSUE)
    d[('Version Control', 'D15')] = ('set', _d + REL)
    d[('Version Control', 'E15')] = ('set', 'Approved')
    d[('Version Control', 'F15')] = ('set', AUTHOR)
    d[('Report Matrix', 'B19')] = ('set', 'v1.2')

CCG_DRAFT_DESC = ('Validation corrections, round 5 (DRAFT): the 790-unit and 1,340-unit caps are annual and tracked year-to-date (worked examples recalculated with the premise written: retention bonus, performance bonus, all-inclusive salary), and so is the shared 3,800-unit cap of voluntary pension funds and long-term savings accounts; severance savings and their interest are not withheld for any employee (non-resident matrix); citations of the revoked Circular 101 of 2025 replaced by the statute (rest-day substitution, hourly divisors, piece-rate workers, overtime maxima).')
DOCX = {
 'CCG': [
  ('CO-CCG-001  ·  Version 1.5  ·  Fiscal Year 2026', 'CO-CCG-001  ·  Version 1.6  ·  Fiscal Year 2026'),
  ('CO-CCG-001 v1.5', 'CO-CCG-001 v1.6'),
  ('1.6 (DRAFT)', '1.6'),
  (CCG_DRAFT_DESC,
   SP + 'the 790-unit and 1,340-unit caps and the shared 3,800-unit cap of voluntary pension funds and long-term savings accounts are annual and tracked year-to-date, with no monthly one-twelfth limit (worked examples recalculated with the premise written: retention bonus, performance bonus, all-inclusive salary, voluntary savings); severance savings and their interest are not withheld for any employee (non-resident matrix); citations of the revoked Circular 101 of 2025 replaced by the statute (rest-day substitution, hourly divisors, piece-rate workers, overtime maxima).' + REL),
 ],
}
FOOTER = {'CCG': {'word/footer1.xml': [('CO-CCG-001 v1.4 |', 'CO-CCG-001 v1.6 |')]}}

# SIR v1.3: text edits on the DRAFT-R5 markdown (header, review markers, version history, related deliverables, Appendix A)
SIR_EDITS = None  # built in release_r5.py (needs the DRAFT text); declared there and logged

# Cross-references updated to current versions (2026-11-02, after the release): citations of another artifact's version
# that the release left behind (CO-PILA-003 and CO-CESANTIAS-006 are v1.2 in this issue). Applied on the released final
# by release_xref.py (XML surgery, clean edit: no highlight, no tracked change); the Version Control rows are not touched.
# Merged into XLSX so that release_crosscheck_r5.py proves DRAFT-R5 -> final with them declared.
XREF = {
 'DD': {
  ('Country Fields', 'W36'): [('sub', 'CO-PILA-003 v1.1', 'CO-PILA-003 v1.2')],
  ('Country Fields', 'W38'): [('sub', 'CO-PILA-003 v1.1', 'CO-PILA-003 v1.2')],
  ('Country Fields', 'W61'): [('sub', 'CO-PILA-003 v1.1', 'CO-PILA-003 v1.2')],
  ('Country Fields', 'W99'): [('sub', 'CO-CESANTIAS-006 v1.1', 'CO-CESANTIAS-006 v1.2')],
  ('Country Fields', 'W112'): [('sub', 'CO-PILA-003 v1.1', 'CO-PILA-003 v1.2')],
  ('Country Fields', 'W113'): [('sub', 'CO-PILA-003 v1.1', 'CO-PILA-003 v1.2')],
 },
}
XREF_BEFORE = {'DD': ('CO-DD-001-v1.5.xlsx', '13915006b2ed6396f881f399ae7ea690')}  # final as released at 09:44, before the xref edits
for _a, _d in XREF.items():
    for _k, _v in _d.items():
        assert _k not in XLSX[_a]
        XLSX[_a][_k] = _v

# Residuals corrected before the Drive upload (2026-11-02, after the release and the xref update): applied on the
# released finals by release_residuos.py (XML surgery, clean edit: no highlight, no tracked change). Merged into
# XLSX / DOCX so that release_crosscheck_r5.py still proves DRAFT-R5 -> final with them declared.
#  R1 CCG Module 12 Example 4 line (E): 'monthly cap' -> the annual 790-unit cap tracked year-to-date (decision A-1;
#     Consejo de Estado S4 rad. 24047 of 2021); cover date = issue date.
#  R2 payment methods: DD ID Information!H7 and CO-DIAN-001 NIE066 / Population Rules cite only the codes of the DD
#     Payment Method mapper (rows 95-104); account-crediting = 42, 45, 47, 98 (Anexo Tecnico NE v1.0 tables 5.3.3.1 /
#     5.3.3.2); NE Version Control row of v1.2 (VC_SPEC['NE'] above) mentions it.
RESID = {
 'DD': {
  ('ID Information', 'H7'): [
   ('sub', 'account-crediting payment methods (Anexo', 'account-crediting payment methods of the Payment Method mapper (Anexo'),
   ('sub', ', 46 (Transferencia Debito Interbancario), 47 (Transferencia Debito Bancaria) and 98 (CATS: Nequi, Daviplata), and 30 / 31 (Transferencia Credito / Debito) if used; left empty for 10 (Efectivo), 20, 23, 25 and 26 (cheques), 71 (Bonos), 72 (Vales) and ZZZ (Acuerdo mutuo).',
           ', 47 (Transferencia Debito Bancaria) and 98 (CATS: Nequi, Daviplata); left empty for 10 (Efectivo), 20 (Cheque), 71 (Bonos) and 72 (Vales).')],
 },
 'NE': {
  ('Nomina Electronica Spec', 'G73'): [('sub', 'is a bank-mediated medium (42, 45, 46, 47, 48, 49 and similar).',
                                       'is a bank-mediated medium (42, 45, 47 and 98; 48 and 49 only where the card is linked to a salary account).')],
  ('Population Rules', 'C30'): [('sub', 'is a bank-mediated medium (42, 45, 46, 47, 48, 49),',
                                 'is a bank-mediated medium (42, 45, 47 and 98; 48 and 49 only where the card is linked to a salary account),')],
  ('Version Control', 'D15'): ('set', VC_SPEC['NE'] + REL),
 },
}
RESID_DOCX = {
 'CCG': [
  ('25% × 3,469,095 = 867,273.75; within the monthly cap', '25% × 3,469,095 = 867,273.75; within the 790-unit annual cap (COP 41,375,460), tracked year-to-date'),
  ('30 October 2026', '2 November 2026', {'prev2': 'Mercans Compliance Regulations Team'}),
 ],
}
# finals as they stood before the residual edits (md5 of MD5-FINAIS.txt of 10:12); copies in _historico/2026-11-02-antes-residuos/
RESID_BEFORE = {'CCG': ('CO-CCG-001-v1.6.docx', '1abe3d6c07ae864f0d8911e86cececc1'),
                'DD': ('CO-DD-001-v1.5.xlsx', '326f3e1d9c529b6b15c2c2ca5ac182a2'),
                'NE': ('specs/CO-DIAN-001-NominaElectronica-Spec.xlsx', 'fc404dae17c10c5692c3b9aac38b0d7d')}
for _a, _d in RESID.items():
    for _k, _v in _d.items():
        if _k in XLSX[_a]:
            assert XLSX[_a][_k] == _v, f'{_a} {_k}: residual edit differs from the declared release edit'
        else:
            XLSX[_a][_k] = _v
for _a, _l in RESID_DOCX.items():
    DOCX[_a] = DOCX[_a] + _l

# Residuals, second batch (2026-11-02, after release_residuos.py): coherence edits applied on the finals by
# release_residuos2.py (same surgery, clean edit: no highlight, no tracked change). Merged into XLSX / DOCX so that
# release_crosscheck_r5.py still proves DRAFT-R5 -> final with them declared.
#  R4 CCG Module 7, B1 housing-loan interest, Limit row: the monthly 100-unit cap is statutory (Decree 1625 of 2016
#     art. 1.2.4.1.27: "sin que exceda de cien (100) Unidades de Valor (UVT) mensuales"), not market practice.
#  R5 CCG payment-method row and CO-DIAN-001 Field Options: code 98 (CATS: Nequi, Daviplata) listed, as in the DD Payment
#     Method mapper (10, 20, 42, 45, 47, 48, 49, 71, 72, 98). Field Options has no free row in the Medio de pago block
#     (rows 79-87, followed by row 88 and the next block at row 89): 98 is written explicitly in D88 and the block header
#     A78 no longer limits the subset to codes 1-97; no row inserted (keeps every row, merge and cross-check reference).
RESID2 = {
 'NE': {
  ('Field Options', 'A78'): [('sub', 'REALISTIC PAYROLL SUBSET OF THE 1-97 LIST', 'REALISTIC PAYROLL SUBSET OF THE ANNEX LIST')],
  ('Field Options', 'D88'): [
   ('sub', 'The complete UN/EDIFACT', 'Also in the realistic payroll subset: 98 - CATS - Cuentas de Ahorro de Tramite Simplificado (Nequi, Daviplata, etc.) - simplified savings account credited directly; the Banco, TipoCuenta and NumeroCuenta attributes (NIE066-NIE068) are filled as for 42, 45 and 47. The complete UN/EDIFACT'),
   ('sub', 'plus 98 (Cuentas de Ahorro de Tramite Simplificado - CATS: Nequi, Daviplata, etc.) and ZZZ', 'plus 98 and ZZZ'),
   ('sub', 'Only the subset above is realistic', 'Only the subset above, with code 98, is realistic')],
 },
}
RESID2_DOCX = {
 'CCG': [
  ('(the monthly figure is derived from the annual 1,200-unit limit of Tax Code art. 119; the monthly apportionment is market practice — see the QA report)',
   '(statutory monthly limit: Decree 1625 of 2016 art. 1.2.4.1.27 — the monthly deductible amount may not exceed 100 tax units, "sin que exceda de cien (100) Unidades de Valor (UVT) mensuales"; annual limit 1,200 units, Tax Code art. 119)'),
  ('47 bank debit transfer · 10 cash', '47 bank debit transfer · 98 CATS simplified savings account (Nequi, Daviplata) · 10 cash'),
 ],
}
# finals as they stood before this batch (md5 of MD5-FINAIS.txt of 10:24); copies in _historico/2026-11-02-antes-residuos2/
RESID2_BEFORE = {'CCG': ('CO-CCG-001-v1.6.docx', '8d0f35c37a049032d9c0336b209fe577'),
                 'NE': ('specs/CO-DIAN-001-NominaElectronica-Spec.xlsx', '15c97ce2adc0fae97c6f92bed3e36d66')}
for _a, _d in RESID2.items():
    for _k, _v in _d.items():
        assert _k not in XLSX[_a], f'{_a} {_k}: already edited'
        XLSX[_a][_k] = _v
for _a, _l in RESID2_DOCX.items():
    DOCX[_a] = DOCX[_a] + _l
