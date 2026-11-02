# -*- coding: utf-8 -*-
"""Test 0 (independent reviewer, 2026-10-30): findings confirmed and corrected in the finals.
Each correction is applied by release.py (merged into release_edits) and proven by release_crosscheck.py.
Sources were re-read by the release author (not only the reviewer): Circular 101 vigencia note, Ley 797 arts. 7-8,
ET art. 55, Ley 2466 art. 14 par. transitorio (raw/docs/oficiais/CO/)."""
REV = ' (revoked by Resolution 2708 of 2026)'
SRC_C101 = 'raw/docs/oficiais/CO/2026-10-30-Circular-MinTrabajo-101-2025-normograma-Cancilleria.htm: "NOTA DE VIGENCIA: Circular derogada por el artículo 1 de la Resolución 2708 de 2026"'
T41 = "salary-constituting payments of the month AND health IBC both below 10 SMMLV - see CO-PILA-003 T2R2-076"

DOCX = [
 # T0-01 Circular 101 of 2025 (revoked): removed from legal-basis lists, qualified where it is narrated, statute cited where it was the only source
 ('and restated by Ministry of Labour Circular 101 of 22 September 2025 §4.', 'and restated by Ministry of Labour Circular 101 of 22 September 2025 §4' + REV + '.'),
 ('Circular 101 of 2025 §5 stresses that', 'Circular 101 of 2025 §5' + REV + ' stressed that'),
 ('; Ministry of Labour Circular 101 of 22 September 2025 §§4 and 5.', '.'),
 ('as substituted by Law 2466 of 2025 art. 12; Circular 101 of 2025 §3', 'as substituted by Law 2466 of 2025 art. 12'),
 ('Decree 1074 of 2015; Law 1266 of 2008; Ministry of Labour Circular 101 of 2025 §3.', 'Decree 1074 of 2015; Law 1266 of 2008.'),
 ('Circular 101 of 2025 §2.3–2.4 confirms expressly', 'Circular 101 of 2025 §2.3–2.4' + REV + ' confirmed expressly'),
 ('Circular 101 of 2025', 'Circular 101 of 2025' + REV, {'eq': True, 'n': 2}),
 ('; Ministry of Labour Circular 101 of 2025 §§2.3, 2.4;', ';'),
 ('Ministry of Labour Circular 101 of 22 September 2025 publishes the table:', 'It follows from the 42-hour week of Law 2101 of 2021 art. 3 (Ministry of Labour Circular 101 of 2025, which published the table, was revoked by Resolution 2708 of 2026):'),
 ('Tax Code arts. 383 par. 3, 387, 387-1; Ministry of Labour Circular 101 of 2025.', 'Tax Code arts. 383 par. 3, 387, 387-1.'),
 ('Decree 780 of 2016 art. 3.2.1.5 (Decree 1990 of 2016 art. 1); Ministry of Labour Circular 101 of 2025.', 'Decree 780 of 2016 art. 3.2.1.5 (Decree 1990 of 2016 art. 1).'),
 ('(Labour Code art. 164, confirmed by Circular 101 of 2025 §2.1)', '(Labour Code art. 164)'),
 ('Included — Circular 101 of 2025 §§2.3–2.4 is explicit that', 'Included — Circular 101 of 2025 §§2.3–2.4' + REV + ' was explicit that'),
 ('Circular 101 derives the resulting maxima', 'Circular 101 of 2025' + REV + ' derived the resulting maxima'),
 ('Circular 101 of 2025 §5.1 contains an internal inconsistency', 'Circular 101 of 2025' + REV + ' §5.1 contained an internal inconsistency'),
 ('; Ministry of Labour Circular 101 of 22 September 2025 §§2.1, 2.3, 2.4, 3, 4, 5, 5.1;', ';'),
 ('Resolution DIAN 000227 of 2025 arts. 1.5.3.2.2 and 1.5.3.4.1.1; Ministry of Labour Circular 101 of 2025.', 'Resolution DIAN 000227 of 2025 arts. 1.5.3.2.2 and 1.5.3.4.1.1.'),
 ('Labour Code art. 162 num. 2 (Law 2466 of 2025 art. 12); Circular 101 of 2025 §3.', 'Labour Code art. 162 num. 2 (Law 2466 of 2025 art. 12).'),
 ('Labour Code art. 162 num. 2; Circular 101 of 2025 §3', 'Labour Code art. 162 num. 2 (Law 2466 of 2025 art. 12)'),
 ('Law 1581 of 2012; Decree 1074 of 2015; Ministry of Labour Circular 101 of 2025 §3.', 'Law 1581 of 2012; Decree 1074 of 2015.'),
 ('from 1 July, 90%. Circular 101 of 2025 §4', 'from 1 July, 90%. Labour Code art. 179 transitional paragraph (Law 2466 of 2025 art. 14)'),
 ('a rise of about 4.8% in every premium. Circular 101 of 2025', 'a rise of about 4.8% in every premium. Law 2101 of 2021 art. 3'),
 ('; Ministry of Labour Circular 101 of 22 September 2025 §§2.1, 4, 5.1;', ';'),
 # T0-06 72 UVT in the Module 3 diagram
 ('[the 72-unit-per-dependant deduction sits OUTSIDE this cap]', '[the 72-unit-per-dependant deduction is NOT applied in withholding: annual return only (DIAN Concepto 011383 of 2024, IV.2)]'),
 # T0-07 integral salary: 70% first, then the Law 1393 excess (approved T4-2)
 ('2c  all-inclusive salary: contribution base = 70% of the salary  (Law 100 art. 18)', '2c  all-inclusive salary: contribution base = 70% of the salary  (Law 100 art. 18); the 2b excess is added after the 70% and is not reduced'),
 ('All-inclusive salary: 70%. Law 100 art. 18 final paragraph. The payroll-levy base is likewise', 'All-inclusive salary: 70% of the salary (Law 100 art. 18 final paragraph); the Law 1393 excess is then added and is not reduced to 70% (Council of State SU 25185 of 2021; exp. 25907 of 2022). The payroll-levy base is likewise'),
 ('reduced to 70% (Labour Code art. 132 num. 3).', 'reduced to 70% (Labour Code art. 132 num. 3) and never takes the excess.'),
 # T0-08 occasional gratuity (approved T4-5)
 ('Only above the 40% clamp', 'No — non-salary by nature (mere liberality); outside the contribution base and the 40% test (Council of State SU 25185 of 2021, rule 3)', {'prev2': 'Occasional gratuity'}),
 # T0-14 art. 114-1 test, two limbs (approved T4-1)
 ('The exemption test is on what the employee earns, not on the contribution base. Testing on the 70%', 'The exemption test has two limbs that must both be below 10 minimum wages: the salary-constituting payments of the month (here the full 25,000,000) and the health contribution base (PILA field 76). The first limb fails here, so testing only the 70%'),
]

XLSX = {
 'WTC': {
  ('Wage Type Catalogue', 'F65'): [('sub', '(MinTrabajo Circular Externa 101 de 22 septiembre 2025)', '(Ley 2101 de 2021 art. 3)')],
  ('Wage Type Catalogue', 'F396'): [('sub', '(MinTrabajo Circular Externa 101 de 22 septiembre 2025)', '(Ley 2101 de 2021 art. 3)')],
  ('Global WTC Coverage', 'C14'): [('sub', ' Circular MinTrabajo 0101 de 2025,', '')],
  ('Wage Type Catalogue', 'F400'): [('sub', "AND the employee's month earnings are STRICTLY LESS THAN 10 SMMLV (17,509,050);", "AND the employee's salary-constituting payments of the month (CST art. 127; non-salary payments, vacation pay, social benefits and indemnities excluded; DIAN Conceptos 008380 de 2024 and 007196 de 2025) are STRICTLY LESS THAN 10 SMMLV (17,509,050) AND the health IBC (PILA campo 43) is also below 10 SMMLV (AT2 v30 campo 76; otherwise N and flag for review);")],
  ('Tax Credit', 'A54'): [('sub', '        per month .....', '        ...............')],
 },
 'PAYSLIP': {
  ('Unit Rate Details', 'B8'): ('set', 'Sunday/Holiday Surcharge (Recargo Dominical y Festivo 80% to 30-Jun-2026 / 90% from 1-Jul-2026)'),
  ('Unit Rate Details', 'B9'): ('set', 'Sunday/Holiday Overtime (Hora Extra Dominical/Festiva: overtime 25% day / 75% night plus the rest-day surcharge 80% / 90%)'),
  ('Colombia (EN)', 'A79'): [('sub', 'FSP (Art. 27 Ley 100, mod. Art. 7 Ley 797 de 2003)', 'FSP (Ley 100 arts. 20 and 27, as amended by Ley 797 de 2003 arts. 7 and 8)')],
  ('Colombia (ES)', 'A79'): [('sub', 'FSP (Art. 27 Ley 100, mod. Art. 7 Ley 797 de 2003)', 'FSP (Arts. 20 y 27 Ley 100, mod. Arts. 7 y 8 Ley 797 de 2003)')],
  ('Colombia (EN)', 'A82'): [('sub', 'max 1,340 UVT/year (Art. 336).', 'max 1,340 UVT/year (DUR 1625 de 2016 art. 1.2.4.1.6 par. 3; Art. 336).')],
  ('Colombia (ES)', 'A82'): [('sub', 'maximo 1.340 UVT/ano (Art. 336).', 'maximo 1.340 UVT/ano (DUR 1625 de 2016 art. 1.2.4.1.6 par. 3; Art. 336).')],
 },
 'NE': {
  ('Nomina Electronica Spec', 'M193'): [('sub', 'Voluntary contribution to a pension fund. Reduces the withholding base within the ET art. 336 40% / 1,340 UVT annual limit.', 'Voluntary contribution to a pension fund. RAIS voluntary contributions are non-constitutive income (ET art. 55: up to 25% of annual labour income, capped at 2,500 UVT) and are subtracted before the 40% / 1,340 UVT cap; voluntary pension-fund contributions (ET art. 126-1) are exempt income inside the 40% / 1,340 UVT cap (DUR 1625 de 2016 art. 1.2.4.1.6 par. 3).')],
  ('Nomina Electronica Spec', 'M194'): [('sub', 'Shares the ET art. 336 40% / 1,340 UVT cap with voluntary pension contributions.', 'Shares the 40% / 1,340 UVT cap (DUR 1625 de 2016 art. 1.2.4.1.6 par. 3; ET art. 336) with voluntary pension-fund contributions.')],
  ('Nomina Electronica Spec', 'M87'): [('sub', 'but IS included in the base of cesantias, prima and the severance indemnity (CST art. 7 of Ley 1 de 1963)', 'but IS included in the base of cesantias, interest on cesantias and prima (Ley 1 de 1963 art. 7); it is NOT in the base of the CST art. 64 dismissal indemnity, which is computed on salary (CST art. 127)')],
  ('Payroll Scope Summary', 'C25'): [('sub', 'but IS in the base of cesantias, prima and the severance indemnity.', 'but IS in the base of cesantias, interest on cesantias and prima (Ley 1 de 1963 art. 7); not in the base of the CST art. 64 dismissal indemnity.')],
  ('Population Rules', 'D23'): [('sub', 'IS included in the base of cesantias, prima and the severance indemnity (Ley 1 de 1963 art. 7).', 'IS included in the base of cesantias, interest on cesantias and prima (Ley 1 de 1963 art. 7); it is not in the base of the CST art. 64 dismissal indemnity (salary, CST art. 127).')],
  ('Example Analysis', 'D32'): [('sub', 'but in the base of cesantias, prima and the severance indemnity.', 'but in the base of cesantias, interest on cesantias and prima (not of the CST art. 64 dismissal indemnity).')],
 },
 'PILA003': {
  ('Payroll Scope Summary', 'C26'): [('sub', 'It IS in the base of cesantias, prima and the severance indemnity - a different base,', 'It IS in the base of cesantias, interest on cesantias and prima (Ley 1 de 1963 art. 7), not of the CST art. 64 dismissal indemnity - a different base,')],
  ('PILA Spec', 'G107'): [('sub', 'Where X, the four IBC fields (T2R2-042 to T2R2-045) must be 70% of the integral salary.', 'Where X, T2R2-042 to T2R2-044 must be 70% of the integral salary plus any Ley 1393 de 2010 art. 30 excess (not reduced to 70%), within floor and ceiling; T2R2-045 (IBC CCF) is 70% of the integral salary and never takes the excess.')],
 },
 'DD': {
  ('Country Fields', 'W36'): [('sub', 'HARD RULE: where set, the four PILA contribution-base fields must be 70% of the integral salary.', 'HARD RULE: where set, PILA T2R2-042 to T2R2-044 must be 70% of the integral salary plus any Ley 1393 de 2010 art. 30 excess (not reduced to 70%); T2R2-045 (CCF) is 70% of the integral salary and never takes the excess.')],
  ('Country Fields', 'W97'): [('sub', 'It is also disapplied per employee where the health contribution base reaches 10 minimum wages', 'It applies per employee only where the salary-constituting payments of the month AND the health contribution base are both below 10 minimum wages')],
 },
 'F350': {
  ('Population Rules', 'C22'): [('sub', 'employees earning less than 10 SMMLV (COP 17,509,050 in 2026)', 'employees earning less than 10 SMMLV (COP 17,509,050 in 2026; ' + T41 + ')')],
  ('Formulario 350 Spec', 'M19'): [('sub', 'for employees under 10 SMMLV is', 'for employees under 10 SMMLV (' + T41 + ') is')],
  ('Example Analysis', 'B38'): ('set', 'Equals SUM(NIE177) for March 2026 (617,232), approximated to the nearest 1,000'),
 },
 'F220': {('Example Analysis', 'B36'): ('set', 'Equals 12 x electronic payroll NIE177 (7,406,784), approximated to the nearest 1,000')},
 'F2276': {('Example Analysis', 'D27'): [('sub', 'Equals Form 220 casilla 60;', 'Equals Form 220 casilla 60 before the certificate\'s approximation to the nearest 1,000 (7,407,000);')]},
 'PILA007': {('Example Analysis', 'D4'): [('sub', '(Decreto 0159 de 2026)', '(Decreto 1469 de 2025; provisional suspension revoked by the Consejo de Estado on 9 July 2026)')]},
}

ITEMS = []
_d = {
 'T0-01': ('Circular MinTrabajo 101 of 2025 cited as in force (24 CCG paragraphs; WTC F65, F396, Global WTC Coverage C14), although revoked; contradicts the CCG Version Control note', 'Removed from legal-basis lists; qualified "(revoked by Resolution 2708 of 2026)" where narrated; statute cited where it was the only source (Law 2101 of 2021 art. 3; Labour Code art. 179 par. transitorio, Law 2466 of 2025 art. 14)', SRC_C101),
 'T0-02': ('Payslip Unit Rate Details B8/B9: pre-reform 75% Sunday surcharge and 100% Sunday overtime', '80% to 30-Jun-2026 / 90% from 1-Jul-2026; overtime 25%/75% plus the rest-day surcharge', 'Ley 2466 de 2025 art. 14 par. transitorio ("A partir del primero de julio de 2026 ... a 90%")'),
 'T0-03': ('Payslip A79 EN/ES: FSP cited as Ley 797 art. 7 amending Ley 100 art. 27', 'Ley 100 arts. 20 and 27, as amended by Ley 797 arts. 7 and 8', 'Ley 797 de 2003: "ARTÍCULO 7o. El artículo 20 de la Ley 100..."; "ARTÍCULO 8o. El artículo 27 de la Ley 100..."'),
 'T0-04': ('NE M193: RAIS voluntary contributions placed inside the 40% / 1,340 UVT cap', 'RAIS voluntary contributions are non-constitutive income (ET art. 55) before the cap; voluntary pension-fund contributions (ET 126-1) inside it', 'ET art. 55: "Las cotizaciones voluntarias al régimen de ahorro individual con solidaridad son un ingreso no constitutivo de renta ... 25% ... limitado a 2.500 UVT"'),
 'T0-05': ('NE M194, Payslip A82 EN/ES: 1,340 UVT withholding cap attributed only to ET art. 336', 'DUR 1625 de 2016 art. 1.2.4.1.6 par. 3 cited with ET art. 336', 'DUR 1.2.4.1.6 par. 3 (Decreto 2231 de 2023)'),
 'T0-06': ('CCG Module 3 diagram: "the 72-unit-per-dependant deduction sits OUTSIDE this cap" (reads as applied in withholding)', 'Not applied in withholding; annual return only', 'DIAN Concepto 011383 de 2024 IV.2 (approved decision A-08)'),
 'T0-07': ('CCG diagram step 2 and the 70% paragraph: integral salary order (40% clamp, then 70%) contradicts CCG P481 / WTC F303', '70% of the integral salary, then the Law 1393 excess added and not reduced; payroll-levy base never takes the excess', 'Ley 100 art. 18; CE SU 25185 de 2021; CE 25907 de 2022 (approved decision T4-2)'),
 'T0-08': ('CCG classification table, Occasional gratuity: "Only above the 40% clamp"', 'Non-salary by nature (mere liberality); outside the base and the 40% test', 'CE SU 25185 de 2021 rule 3; CST art. 128 (approved decision T4-5)'),
 'T0-12': ('Art. 114-1 test stated on "earnings" only (WTC F400; Form 350 C22 and M19; DD W97 states only the IBC limb)', 'Both limbs: salary-constituting payments AND health IBC below 10 SMMLV (campo 76)', 'AT2 v30 campo 76; DIAN Conceptos 008380/2024 and 007196/2025 (approved decision T4-1)'),
 'T0-13': ('DD W36, PILA-003 G107: integral salary "four IBC fields must be 70%" without the Ley 1393 excess', '042-044 = 70% + excess; 045 (CCF) = 70%, never the excess', 'Ley 1393 art. 30 ("para los efectos relacionados con los artículos 18 y 204 de la Ley 100"); approved T4-2 / T4-4'),
 'T0-14': ('CCG integral-salary example: 114-1 test described with one limb', 'Two limbs (salary of the month and health IBC)', 'AT2 v30 campo 76 (approved decision T4-1)'),
 'T0-15': ('PILA-007 Example Analysis D4: SMLMV cited to Decreto 0159 de 2026 (spent)', 'Decreto 1469 de 2025, suspension revoked 9-Jul-2026', 'CE Sección Segunda auto 2026-07-09 (local copy); consistent with CCG, CESANTIAS-006 D5, Payslip A83'),
 'T0-16': ('NE M87, C25, D23, D32; PILA-003 C26: transport allowance in the base of the severance indemnity', 'In the base of cesantias, interest and prima only; not of the CST art. 64 indemnity (salary, CST art. 127)', 'CST art. 64 ("días de salario"); CESANTIAS-006 D34; approved decision T4-3'),
 'T0-17': ('Reconciliation labels mixing rounded and unrounded values (Form 350 B38, Form 220 B36, Format 2276 D27)', 'Labels state the unrounded sum and the approximation to the nearest 1,000', 'Res. DIAN 0022/2024 guide ("aproximados al múltiplo de mil"); DUR 1.6.1.11.11'),
 'T0-19': ('WTC Tax Credit A54: stray "per month" after "no monthly apportionment"', 'Removed', 'Internal consistency (A53)'),
}
_where = {'T0-01': [('CCG', 'paragraphs'), ('WTC', 'Wage Type Catalogue!F65'), ('WTC', 'Wage Type Catalogue!F396'), ('WTC', 'Global WTC Coverage!C14')],
          'T0-02': [('PAYSLIP', 'Unit Rate Details!B8'), ('PAYSLIP', 'Unit Rate Details!B9')],
          'T0-03': [('PAYSLIP', 'Colombia (EN)!A79'), ('PAYSLIP', 'Colombia (ES)!A79')],
          'T0-04': [('NE', 'Nomina Electronica Spec!M193')],
          'T0-05': [('NE', 'Nomina Electronica Spec!M194'), ('PAYSLIP', 'Colombia (EN)!A82'), ('PAYSLIP', 'Colombia (ES)!A82')],
          'T0-06': [('CCG', 'paragraphs')], 'T0-07': [('CCG', 'paragraphs')], 'T0-08': [('CCG', 'paragraphs')], 'T0-14': [('CCG', 'paragraphs')],
          'T0-12': [('WTC', 'Wage Type Catalogue!F400'), ('F350', 'Population Rules!C22'), ('F350', 'Formulario 350 Spec!M19'), ('DD', 'Country Fields!W97')],
          'T0-13': [('DD', 'Country Fields!W36'), ('PILA003', 'PILA Spec!G107')],
          'T0-15': [('PILA007', 'Example Analysis!D4')],
          'T0-16': [('NE', 'Nomina Electronica Spec!M87'), ('NE', 'Payroll Scope Summary!C25'), ('NE', 'Population Rules!D23'), ('NE', 'Example Analysis!D32'), ('PILA003', 'Payroll Scope Summary!C26')],
          'T0-17': [('F350', 'Example Analysis!B38'), ('F220', 'Example Analysis!B36'), ('F2276', 'Example Analysis!D27')],
          'T0-19': [('WTC', 'Tax Credit!A54')]}
for k, (fi, co, so) in _d.items():
    for art, w in _where[k]:
        ITEMS.append(dict(id=k, artifact=art, where=w, finding=fi, correction=co, source=so))
