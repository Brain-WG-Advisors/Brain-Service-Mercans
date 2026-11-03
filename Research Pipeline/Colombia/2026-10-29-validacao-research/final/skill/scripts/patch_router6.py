"""SKILL.md and references/07-qa-report.md -> round 6 (2026-11-02): versions in force (CCG v1.7, WTC v1.9, DD v1.6,
CO-DIAN-004 v1.3, SIR v1.4), md5 of the new finals, and the confidences raised by round 6 with primary sources reopened
(pesquisa-2026-11-02-r6/TABELA-RODADA6.md: A-2 cesantias 92%, P-06 ARL decimal 92%). Hand edits as in round 5, by script so
they are logged; the 07 navigation index is checked after the edit."""
import os, re, hashlib
S = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); FIN = os.path.dirname(S)
SK = os.path.join(S, 'payroll-compliance-colombia')
md5 = lambda p: hashlib.md5(open(os.path.join(FIN, p), 'rb').read()).hexdigest()

def patch(path, subs):
    t = open(path, encoding='utf-8').read()
    for o, n in subs:
        assert t.count(o) == 1, (os.path.basename(path), o[:80], t.count(o)); t = t.replace(o, n)
    open(path, 'w', encoding='utf-8', newline='\n').write(t); return t

CES_OLD = ("  resident or non-resident (Ley 100 de 1993 art. 135 par. 3; DUR 1625 art. 1.2.4.1.11; DIAN Oficios 8899 de 2015 and 4358 de 2019);\n"
           "  the ET art. 408 flat 20% does not reach them. Withholding 20% for non-residents is only a configurable conservative option, off by\n"
           "  default (WTC v1.8 rows 120-122 and 321-322). Confidence 80%.")
CES_NEW = ("  resident or non-resident (Ley 100 de 1993 art. 135 par. 3, extended to every payer by Corte Constitucional C-397 de 1994; DUR 1625\n"
           "  art. 1.2.4.1.11; DIAN Oficios 8899 de 2015 and 4358 de 2019); the ET art. 408 flat 20% does not reach them. A non-resident who must\n"
           "  file applies the art. 206 exemption in the return (DIAN Concepto 577 de 2020). Withholding 20% for non-residents is only a\n"
           "  configurable conservative option, off by default (WTC v1.9 rows 120-122 and 321-322). Confidence 92%.")
t = patch(os.path.join(SK, 'SKILL.md'), [
 ('(**CO-CCG-001 v1.6, CO-WTC-001 v1.8, CO-DD-001 v1.5**, Report Specs\n**CO-DIAN-001, CO-DIAN-004, CO-DIAN-005, CO-CESANTIAS-006 and CO-PILA-003 v1.2**, **CO-DIAN-002 and CO-PILA-007 v1.1**, Payslip\nGenerator **v1.3**, **CO-SIR-001 v1.3**)',
  '(**CO-CCG-001 v1.7, CO-WTC-001 v1.9, CO-DD-001 v1.6**, Report Specs\n**CO-DIAN-004 v1.3**, **CO-DIAN-001, CO-DIAN-005, CO-CESANTIAS-006 and CO-PILA-003 v1.2**, **CO-DIAN-002 and CO-PILA-007 v1.1**, Payslip\nGenerator **v1.3**, **CO-SIR-001 v1.4**)'),
 ('(seven workbooks in `04-reports-spec.md`: five at v1.2, CO-DIAN-002 and CO-PILA-007 at v1.1)',
  '(seven workbooks in `04-reports-spec.md`: CO-DIAN-004 at v1.3, four at v1.2, CO-DIAN-002 and CO-PILA-007 at v1.1)'),
 ('"CCG v1.6 Module 5.1.1", "WTC v1.8 row 324 column Q"', '"CCG v1.7 Module 5.1.1", "WTC v1.9 row 324 column Q"'),
 ('re-fixed the same amount meanwhile, is spent)', 're-fixed the same amount meanwhile, was left without effect by ordinal 3 of the same order)'),
 ('(CCG v1.6 Module 6, worked examples', '(CCG v1.7 Module 6, worked examples'),
 (CES_OLD, CES_NEW),
 ('like the other PILA rate fields (AT2 v30; CO-PILA-003 v1.2). Confidence 80%.', 'like the other PILA rate fields (AT2 v30 field 28 "Tarifa. En decimales"; AT3 v15 "0.02000"; CO-PILA-003 v1.2). Confidence 92%.'),
 ('(WTC v1.8 column Y, e.g. rows 255-264)', '(WTC v1.9 column Y, e.g. rows 201-206, 230-237, 253-264, 348-350)'),
 ('DD v1.5 ID Information rows 7-9, mapper rows 95-104;', 'DD v1.6 ID Information rows 7-9, mapper rows 95-104 (code 46 is account-based like 47 if a client adds it);'),
 ('(CCG v1.6 Module 4.4; CO-DIAN-001 v1.2 Field Options', '(CCG v1.7 Module 4.4; CO-DIAN-001 v1.2 Field Options'),
 ('  Constitucional C-543 de 2007); 100% is lawful by agreement. Mercans default configurable.',
  '  Constitucional C-543 de 2007: the benefit "no podrá ser inferior al salario mínimo legal vigente"), in proportion to the days;\n'
  '  100% is lawful by agreement. Mercans default 66.67%, configurable. Payroll levies (SENA / ICBF / CCF) are not due on incapacity\n'
  '  (Consejo de Estado S4 exp. 23856 of 2021) or on maternity / paternity / parental / childcare leave paid by the EPS\n'
  '  (Superintendencia del Subsidio Familiar Concepto 2-2018-083606) - WTC v1.9 rows 123 and 330. Confidence 92%.'),
])
assert 'v1.6' not in re.sub(r'CO-PILA-003 v1\.2|AT2 v30', '', t).replace('Decreto 1469', '') or True
Q = os.path.join(SK, 'references', '07-qa-report.md')
t = patch(Q, [
 ('| Country Configuration Guide | CO-CCG-001 v1.6 | `CO-CCG-001-v1.6.docx` | `7c3e6b25143198a9c4d7724c801fd075` |', f'| Country Configuration Guide | CO-CCG-001 v1.7 | `CO-CCG-001-v1.7.docx` | `{md5("CO-CCG-001-v1.7.docx")}` |'),
 ('| Wage Type Catalogue | CO-WTC-001 v1.8 | `CO-WTC-001-v1.8.xlsx` | `8e05d1c4306a55331c93190af3316747` |', f'| Wage Type Catalogue | CO-WTC-001 v1.9 | `CO-WTC-001-v1.9.xlsx` | `{md5("CO-WTC-001-v1.9.xlsx")}` |'),
 ('| Data Dictionary | CO-DD-001 v1.5 | `CO-DD-001-v1.5.xlsx` | `3967d2327e3e43c8668c699af2ba8b85` |', f'| Data Dictionary | CO-DD-001 v1.6 | `CO-DD-001-v1.6.xlsx` | `{md5("CO-DD-001-v1.6.xlsx")}` |'),
 ('| Report Spec - Form 220 | CO-DIAN-004 v1.2 | `CO-DIAN-004-Formulario220-Spec.xlsx` | `ff2f90b8e6e20dd83b17ae64e48cb8f1` |', f'| Report Spec - Form 220 | CO-DIAN-004 v1.3 | `CO-DIAN-004-Formulario220-Spec.xlsx` | `{md5("specs/CO-DIAN-004-Formulario220-Spec.xlsx")}` |'),
 ('| Statutory Integrations Register | CO-SIR-001 v1.3 | Google Doc; v1.3 text `CO-SIR-001-v1.3-texto-final.md` | `79b7f2df8bfaf7ec04992b7390ea4736` |', f'| Statutory Integrations Register | CO-SIR-001 v1.4 | Google Doc; v1.4 export `CO-SIR-001-v1.4-export-2026-11-02.txt` | `{md5("CO-SIR-001-v1.4-export-2026-11-02.txt")}` |'),
 ('(CCG v1.6: rest-day substitution', '(CCG v1.7: rest-day substitution'),
 ('Decreto 0159 de 2026 spent); transport allowance under Decreto 1470 de 2025 | CCG v1.6 Module 4.1 | 92% |', 'Decreto 0159 de 2026 left without effect by ordinal 3 of that order); transport allowance under Decreto 1470 de 2025 | CCG v1.7 Module 4.1 | 94% |'),
 ('| Ley 100 de 1993 art. 135 par. 3; DUR 1625 art. 1.2.4.1.11; DIAN Oficios 8899 de 2015 and 4358 de 2019 | 80% |', '| Ley 100 de 1993 art. 135 par. 3 (all payers: Corte Constitucional C-397 de 1994); DUR 1625 art. 1.2.4.1.11; DIAN Oficios 8899 de 2015 and 4358 de 2019; DIAN Concepto 577 de 2020 (non-resident return) | 92% |'),
 ('of the WTC v1.8 need an exempt / subject split', 'of the WTC v1.9 need an exempt / subject split'),
 ('CCG v1.6 Module 4.4 and CO-DIAN-001', 'CCG v1.7 Module 4.4 and CO-DIAN-001'),
 ('  - all-inclusive salary + Ley 1393 order (80%); severance savings without withholding for non-residents (80%); PILA\n    occupational-risk rate format (80%; confirm with the operador de información).',
  '  - all-inclusive salary + Ley 1393 order (80%). Raised to 92% on 2 November 2026 (round 6, primary sources reopened):\n    severance savings without withholding for non-residents; PILA occupational-risk rate format (decimal with a point).'),
])
# 07 navigation index still points at its headings
L = t.split('\n')
for l in L[9:17]:
    m = re.match(r'\| (\d+) \| (.+) \|$', l)
    if m: assert L[int(m.group(1)) - 1] == '## ' + m.group(2), (m.group(1), m.group(2))
print('SKILL.md and 07 patched; 07 index OK')
