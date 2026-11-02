# -*- coding: utf-8 -*-
"""Post-release review 2026-10-30: residual Test 0 items (T0-09, T0-10, T0-11, T0-18, T0-20, T0-21, C1-C7) decided on
primary sources and applied to the finals. Merged into release_edits by the same mechanism as test0_corrections.py,
applied by release.py and proven by release_crosscheck.py. Decisions, literal source extracts and confidence:
final/test0/RESIDUOS-DECISOES.md. Sources downloaded on 2026-10-30 are under raw/docs/oficiais/CO/."""

SU = 'Consejo de Estado, Seccion Cuarta, SU 25185 of 9 December 2021'
AB_PACTED = 'This wage type is non-salary, is not included in the calculation base for payroll levies or statutory benefits, but is included in the Ley 1393 calculation base'
AB_CAR = ("Default 'Non-Salary - pacted': a cash car / fuel / maintenance allowance paid under the contract is salary (CST art. 127) "
          "unless a written CST art. 128 pact excludes it, and then it is inside the Ley 1393 40% test. Where the amount is paid only so "
          "that the employee can travel for the job (means of transport, CST art. 128), configure it as 'Non-Salary - non-remunerative' "
          "with health, solidarity fund, occupational risk and pension = No: outside the contribution base and the 40% test (" + SU + ").")
AB_NONREM = ('Non-salary by nature (CST art. 128): not in the contribution base, the payroll-levy base or the statutory-benefit base, '
             'and outside the Ley 1393 40% test (' + SU + ').')
AB_BIRTH = ('Occasional payment by mere liberality: non-salary by law (CST art. 128), outside the contribution base and the Ley 1393 '
            "40% test (" + SU + "). Where it is owed under a collective agreement or the contract, use 'Non-Salary - pacted'.")

FL_PACTED = {'Q': 'Yes/No', 'R': 'Yes/No', 'S': 'Yes/No', 'T': 'No', 'U': 'Yes/No', 'V': 'Non-Salary - pacted', 'W': 'No', 'X': 'No'}
FL_NONREM = {'Q': 'No', 'R': 'No', 'S': 'No', 'T': 'No', 'U': 'No', 'V': 'Non-Salary - non-remunerative', 'W': 'No', 'X': 'No'}
FL_SALARY = {'Q': 'Yes', 'R': 'Yes', 'S': 'Yes', 'T': 'Yes', 'U': 'Yes', 'V': 'Salary', 'W': 'Yes', 'X': 'Yes'}

# current values of the finals (only cells whose value changes are declared)
CUR = {
 175: {'Q': 'Yes/No', 'R': 'Yes/No', 'S': 'Yes/No', 'T': 'Yes/No', 'U': 'Yes/No', 'V': 'Non-Salary - non-remunerative', 'W': 'No', 'X': 'No'},
 176: {'Q': 'Yes/No', 'R': 'Yes/No', 'S': 'Yes/No', 'T': 'No', 'U': 'Yes/No', 'V': 'Non-Salary - non-remunerative', 'W': 'No', 'X': 'No'},
}
_NR_YN = {'Q': 'Yes/No', 'R': 'Yes/No', 'S': 'Yes/No', 'T': 'No', 'U': 'Yes/No', 'V': 'Non-Salary - non-remunerative', 'W': 'No', 'X': 'No'}
for _r in (201, 202, 206, 214, 215, 216, 217, 226, 267): CUR[_r] = dict(_NR_YN)
for _r in (203, 204, 205): CUR[_r] = dict(FL_SALARY)
for _r in (228, 229): CUR[_r] = dict(FL_PACTED)

TARGET = {175: FL_SALARY, 176: FL_SALARY, 217: FL_NONREM, 226: FL_NONREM, 228: FL_NONREM, 229: FL_NONREM, 267: FL_PACTED}
for _r in (201, 202, 203, 204, 205, 206, 214, 215, 216): TARGET[_r] = FL_PACTED

WTC = {}
for r, tgt in TARGET.items():
    for c, v in tgt.items():
        if CUR[r][c] != v:
            WTC[('Wage Type Catalogue', f'{c}{r}')] = ('set', v)
# column AB (YTD remarks)
WTC[('Wage Type Catalogue', 'AB175')] = ('set', '')
WTC[('Wage Type Catalogue', 'AB176')] = ('set', '')
for r in (201, 202, 203, 204, 205, 206, 214, 215, 216):
    WTC[('Wage Type Catalogue', f'AB{r}')] = ('set', AB_CAR)
    WTC[('Wage Type Catalogue', f'Y{r}')] = ('set', 'Devengados / Auxilio (AuxilioNS, NIE142, where non-salary under the pact; otherwise AuxilioS, NIE141)')
WTC[('Wage Type Catalogue', 'AB217')] = ('set', AB_NONREM)
WTC[('Wage Type Catalogue', 'AB226')] = ('set', AB_NONREM)
WTC[('Wage Type Catalogue', 'AB228')] = ('set', AB_BIRTH)
WTC[('Wage Type Catalogue', 'D229')] = ('set', AB_BIRTH)
# T0-11: pension flag of the pacted education allowances, same as rows 255-259
for r in (260, 261, 262, 263, 264): WTC[('Wage Type Catalogue', f'U{r}')] = ('set', 'Yes/No')
# C7: payroll levies on the employer disability top-up
WTC[('Wage Type Catalogue', 'D123')] = [('sub', "(Consejo de Estado, Seccion Cuarta, SU 25185 of 2021); an employer-paid disability top-up is neither. UGPP ABC Empleadores 2025 says incapacity and maternity values are to be 'taken into account' for payroll levies. This is an interpretation; confirm with UGPP. Configurable.",
  "(Consejo de Estado, Seccion Cuarta, SU 25185 of 2021). The incapacity benefit is not salary (CST arts. 128 and 227) and is excluded from the SENA / ICBF / CCF base (Consejo de Estado, Seccion Cuarta, 19 August 2021, exp. 23856); an employer-paid top-up of that benefit has the same nature and is not paid rest. UGPP ABC Empleadores 2025 tells employers to take incapacity and maternity values into account for payroll levies; the Consejo de Estado ruling is followed here. Configurable.")]

XLSX = {
 'WTC': WTC,
 'DD': {
  ('Country Fields', 'W46'): [('sub', 'the additional 72 UVT per dependant per year under art. 336 num. 3, up to four dependants)',
                              'the additional 72 UVT per dependant per year under art. 336 num. 3, up to four dependants, which is for the annual return only and is not applied in withholding - DIAN Concepto 011383 de 2024, IV.2)')],
 },
 'NE': {
  ('Nomina Electronica Spec', 'M135'): [('sub', 'Non-salary portion of a bonus. Counts toward the 40% non-salary clamp of Ley 1393 de 2010 art. 30 for contribution purposes.',
                                         'Non-salary portion of a bonus. Counts toward the 40% non-salary clamp of Ley 1393 de 2010 art. 30 only where it is non-salary under an express written CST art. 128 pact; an occasional bonus paid by mere liberality is non-salary by law and stays outside the clamp (' + SU + ').')],
 },
 'PAYSLIP': {
  ('Colombia (EN)', 'A84'): [('sub', 'paternity 2 weeks (CST Art. 236A, Ley 2114 de 2021)', 'paternity 2 weeks (CST Art. 236 par. 2, as amended by Ley 2114 de 2021 art. 2)')],
  ('Colombia (ES)', 'A84'): [('sub', 'licencia de paternidad 2 semanas (CST Art. 236A, Ley 2114 de 2021)', 'licencia de paternidad 2 semanas (CST Art. 236 par. 2, mod. Ley 2114 de 2021 art. 2)')],
  ('Population Range', 'C7'): [('sub', '(CST Arts. 236 & 236A; Ley 1822 de 2017; Ley 2114 de 2021)', '(CST Art. 236, paternity in par. 2; Ley 1822 de 2017; Ley 2114 de 2021 art. 2)')],
  # T0-18: FSP = PILA fields 51 (solidarity sub-account 0.5%) and 52 (subsistence sub-account), each rounded up to the next 100
  ('Colombia (EN)', 'H36'): ('formula', 'ROUNDUP(ROUND(SUM($H$26:$H$29)*0.005,2),-2)+ROUNDUP(ROUND(SUM($H$26:$H$29)*0.005,2),-2)', '192000'),
  ('Colombia (ES)', 'H36'): ('formula', 'ROUNDUP(ROUND(SUM($H$26:$H$29)*0.005,2),-2)+ROUNDUP(ROUND(SUM($H$26:$H$29)*0.005,2),-2)', '192000'),
 },
}

DOCX = [
 # C1: ET art. 10 num. 1 - straddling period: resident from the second year
 ('Where the period straddles two years, residence attaches to the year in which the 183rd day falls',
  'Where the 365-day period spans two calendar years, residence starts in the second year (Tax Code art. 10 num. 1; DIAN Concepto 011108 of 2026, item 13)'),
 ('; where the period straddles two years, residence attaches to the year in which the 183rd day falls.',
  '; where the 365-day period spans two calendar years, residence starts in the second year (DIAN Concepto 011108 of 2026, item 13).'),
 ('Residence attaches to the whole tax year in which the 183rd day falls,',
  'Residence attaches to the whole tax year in which it is acquired (the second year where the 365-day period spans two calendar years; Tax Code art. 10 num. 1),'),
 ('Where the year straddles the threshold, residence attaches to the year in which the 183rd day falls.',
  'Where the 365-day period spans two calendar years, residence starts in the second year (Tax Code art. 10 num. 1; DIAN Concepto 011108 of 2026, item 13).'),
 # C2: day count of the worked example (entry 1 July 2026, entry day counted)
 ('The employee exceeds 183 days of presence (the 184th day) on or about 30 December 2026.',
  'The employee exceeds 183 days of presence on 31 December 2026 (the 184th day, counting the day of entry, 1 July; Tax Code art. 10 num. 1).'),
]

ITEMS = []
_d = [
 ('T0-09', 'WTC', 'Wage Type Catalogue!Q:V228:229, AB228, D229', "Birth / marriage allowance described as mere liberality but classified 'Non-Salary - pacted' with health / solidarity / risk / pension 'Yes/No'",
  "'Non-Salary - non-remunerative'; health, solidarity fund, occupational risk and pension = No; remark rewritten (pacted variant where owed by agreement)",
  'CST art. 128 ("No constituyen salario las sumas que ocasionalmente y por mera liberalidad recibe el trabajador"); CE SU 25185/2021 rules 1 and 3'),
 ('T0-10', 'WTC', 'Wage Type Catalogue!Q:X175:176, AB175:176', "Arrears / adjustment of the expat allowance classified non-salary while the allowance itself (rows 173-174) is salary",
  'Copied from rows 173-174: salary, all bases Yes; remark removed', 'CST art. 127 ("cualquiera que sea la forma o denominación"); internal consistency with rows 173-174'),
 ('T0-10', 'WTC', 'Wage Type Catalogue!V, Q:X, AB of 201-206 and 214-216', "Car / fuel / maintenance allowance family: 'non-remunerative' with 'Yes/No' flags and the 40% remark (201, 202, 206, 214-216) while 203-205 were 'Salary'",
  "One nature for the concept: 'Non-Salary - pacted' (the WTC rule for an unclear nature; salary unless a written CST art. 128 pact), with the means-of-transport variant documented in AB",
  'CST arts. 127 and 128 ("medios de transporte ... para desempeñar a cabalidad sus funciones"); CE SU 25185/2021 rules 1 and 3; WTC column V definition'),
 ('T0-10', 'WTC', 'Wage Type Catalogue!Q:U, AB of 217 and 226', "Relocation allowance (genuine reimbursement / means to work) 'non-remunerative' but health / pension 'Yes/No' and the 40% remark",
  'Health, solidarity fund, occupational risk and pension = No, as rows 218-225; remark rewritten', 'CST art. 128; CE SU 25185/2021 rule 1; CE 25907/2022'),
 ('T0-10', 'WTC', 'Wage Type Catalogue!V267', "Recognition award (contractual bonus, salary unless pacted) classified 'non-remunerative'",
  "'Non-Salary - pacted' (flags 'Yes/No' and remark unchanged)", 'CST arts. 127 and 128 second part; WTC F267 own definition'),
 ('T0-11', 'WTC', 'Wage Type Catalogue!U260:U264', "Pension flag 'Yes' on pacted education allowances, while rows 255-259 and the health flag are 'Yes/No'",
  "'Yes/No' (only the excess over 40% is in the pension base)", 'Ley 1393 de 2010 art. 30 ("para los efectos relacionados con los artículos 18 y 204 de la Ley 100")'),
 ('C7', 'WTC', 'Wage Type Catalogue!D123', 'Payroll-levy flag of the employer disability top-up stated as an unconfirmed interpretation',
  'Basis completed with the Consejo de Estado ruling that incapacity benefits are outside the SENA / ICBF / CCF base; flag unchanged (No)',
  'CE Seccion Cuarta 19-08-2021 exp. 23856 ("se excluye de la base para calcular los aportes con destino al SENA, ICBF y CCF"); Ley 21/1982 art. 17'),
 ('T0-20', 'DD', 'Country Fields!W46', '72 UVT per dependant listed without the annual-return-only limit', 'Limit stated',
  'DIAN Concepto 011383 de 2024, IV.2 (approved decision A-08)'),
 ('T0-21', 'NE', 'Nomina Electronica Spec!M135', 'Non-salary bonus said to count in the 40% clamp without condition',
  'Only where non-salary under a written CST art. 128 pact; mere-liberality bonus outside', 'CE SU 25185/2021 rule 3; CST art. 128'),
 ('C3', 'PAYSLIP', 'Colombia (EN)!A84, Colombia (ES)!A84, Population Range!C7', 'Paternity leave cited to "CST Art. 236A" (no such article)',
  'CST art. 236 par. 2, as amended by Ley 2114 de 2021 art. 2', 'CST art. 236 par. 2 ("El padre tendrá derecho a dos (2) semanas de licencia remunerada de paternidad")'),
 ('T0-18', 'PAYSLIP', 'Colombia (EN)!H36, Colombia (ES)!H36', 'FSP rounded up to 100 as one amount; the reviewer proposed rounding to the peso',
  'Kept the rounding up to 100 (the FSP is employee-only and is paid as calculated on the PILA), applied to each of PILA fields 51 and 52; value unchanged (192,000)',
  'Decreto 780 de 2016 art. 3.2.1.5 num. 2 (Decreto 1990 de 2016 art. 1); AT2 v30 campo 51'),
 ('C1', 'CCG', 'paragraphs (Module 2.2 table, Module 3 residence test, FAQ items)', 'Straddling period: residence attached to "the year in which the 183rd day falls"',
  'Residence starts in the second year', 'ET art. 10 num. 1 ("se considerará que la persona es residente a partir del segundo año o periodo gravable"); DIAN Concepto 011108/2026 item 13'),
 ('C2', 'CCG', 'paragraph (Example 3, the switch)', '184th day "on or about 30 December 2026" for an entry on 1 July 2026',
  '31 December 2026 (184th day, entry day counted)', 'ET art. 10 num. 1 ("incluyendo días de entrada y salida del país")'),
]
for i, a, w, fi, co, so in _d:
    ITEMS.append(dict(id=i, artifact=a, where=w, finding=fi, correction=co, source=so))
