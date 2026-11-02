# -*- coding: utf-8 -*-
"""Post-release review 2026-10-30 (second pass): consistency between the CCG and the specs / WTC / Payslip, decided on
primary sources (no question sent back). Merged into release_edits by the same mechanism as residuos_corrections.py,
applied by release.py and proven by release_crosscheck.py.

Sources read (raw/docs/oficiais/CO/ unless stated):
- DIAN Concepto 013840 int. 1568 of 1 October 2025 (2026-10-30-DIAN-Concepto-13840-2025-normograma.htm), items 3(vii), 4, 5.
- Technical Annex of the electronic payroll support document v1.0 (DIAN Caja de Herramientas V1-0, table 5.5.5:
  25 / 75 / 35 / 100 / 75 / 150 / 110); DIAN micrositio snapshot 2026-10-21 lists no later annex.
- Ley 2466 de 2025 art. 14 (CST art. 179 and its parágrafo transitorio: 80% from 1-7-2025, 90% from 1-7-2026, 100% from
  1-7-2027, or 100% from the outset at the employer's option) (2026-10-30-Ley-2466-2025-SecretariaSenado.html).
- Corte Constitucional C-543 de 2007, resolutive part (2026-10-22-CorteConstitucional-C-543-2007.htm).
- Concepto MinSalud 202311602174531 of 20 October 2023 (2026-10-30-MinSalud-Concepto-202311602174531-2023-normograma-Supersalud.htm).
- Decreto-Ley 2090 de 2003 art. 5 and Decreto 1435 de 2025 as quoted in CCG Module 5.1.1; Decreto 1470 de 2025 art. 1.
- AT2 v30 (24-07-2026) campos 57-60 (2026-10-29-MinSalud-AT2-v30-2026-07-24-PILA-activos.txt, lines 5417-5436).
- Ley 1393 de 2010 art. 32 (2026-10-21-Ley-1393-2010-SecretariaSenado.html).
"""

C13840 = 'DIAN Concepto 013840 de 2025'


def _ne_m(code, name, printed, a, b, c):
    return (f"The premium percentage applied. Technical Annex table 5.5.5 assigns code {code} to '{name}' with printed percentage "
            f"{printed}, built on the pre-reform 75% rest-day premium. Report the percentage actually applied under CST art. 179 "
            f"(Ley 2466 de 2025 art. 14): {a} from 1 July 2025, {b} from 1 July 2026, {c} from 1 July 2027 or from the date the "
            f"employer applies the full 100% premium. The annex percentage is read in accordance with the rules in force "
            f"({C13840}, items 3(vii) and 5). Taken from the configured rate table, never hard-coded. This is the only place the "
            f"XML carries the rate; the amount in @Pago must be consistent with it.")


NE = {
 ('Nomina Electronica Spec', 'M109'): ('set', _ne_m(4, 'Hora Extra Diurna Dominical y Festivos', '100.00', '105.00', '115.00', '125.00')),
 ('Nomina Electronica Spec', 'M114'): ('set', _ne_m(5, 'Hora Recargo Diurno Dominical y Festivos', '75.00', '80.00', '90.00', '100.00')),
 ('Nomina Electronica Spec', 'M119'): ('set', _ne_m(6, 'Hora Extra Nocturna Dominical y Festivos', '150.00', '155.00', '165.00', '175.00')),
 ('Nomina Electronica Spec', 'M124'): ('set', _ne_m(7, 'Hora Recargo Nocturno Dominical y Festivos', '110.00', '115.00', '125.00', '135.00')),
 ('Nomina Electronica Spec', 'K109'): ('set', '115.00'),
 ('Nomina Electronica Spec', 'K114'): ('set', '90.00'),
 ('Nomina Electronica Spec', 'K119'): ('set', '165.00'),
 ('Nomina Electronica Spec', 'K124'): ('set', '125.00'),
 ('Field Options', 'D61'): ('set', 'Sunday / holiday day overtime. Annex percentage 100.00; reported at 25% + the CST art. 179 premium: 105.00 from 1 July 2025, 115.00 from 1 July 2026, 125.00 from 1 July 2027.'),
 ('Field Options', 'D62'): ('set', 'Sunday / holiday day surcharge. Annex percentage 75.00; reported at the CST art. 179 premium: 80.00 from 1 July 2025, 90.00 from 1 July 2026, 100.00 from 1 July 2027.'),
 ('Field Options', 'D63'): ('set', 'Sunday / holiday night overtime. Annex percentage 150.00; reported at 75% + the CST art. 179 premium: 155.00 from 1 July 2025, 165.00 from 1 July 2026, 175.00 from 1 July 2027.'),
 ('Field Options', 'D64'): ('set', 'Sunday / holiday night surcharge. Annex percentage 110.00; reported at 35% + the CST art. 179 premium: 115.00 from 1 July 2025, 125.00 from 1 July 2026, 135.00 from 1 July 2027.'),
 ('Field Options', 'A65'): ('set', '(statutory rate)'),
 ('Field Options', 'D65'): ('set', "STATUTORY RATE REPORTED. The annex percentages for codes 4, 5, 6 and 7 embed the pre-reform 75% Sunday / public-holiday premium. Law 2466 of 2025 art. 14 (CST art. 179) sets that premium at 80% from 1 July 2025, 90% from 1 July 2026 and 100% from 1 July 2027 (or 100% from the outset at the employer's option). The annex is still at version 1.0 and table 5.5.5 has not been reissued. DIAN Concepto 013840 int. 1568 of 1 October 2025: the table percentage 'debe leerse en consonancia con la normatividad vigente para cada caso específico', employers report the surcharges 'liquidados con el porcentaje aplicable según la normatividad vigente', and different percentages within one month do not prevent the generation, transmission and validation of the document. @Porcentaje therefore carries the statutory percentage from the configured rate table, split by date where a month straddles 1 July."),
}

SICK_SRC = 'Corte Constitucional C-543 de 2007; Concepto MinSalud 202311602174531 de 2023; '
WTC = {
 ('Employer Sick Pay', 'A30'): ('set', "THE RATE FOR THE EMPLOYER'S FIRST TWO DAYS."),
 ('Employer Sick Pay', 'A34'): ('set', '  thirds for the first 90 days, and Concepto MinSalud 202311602174531 of 20 October 2023 applies it to'),
 ('Employer Sick Pay', 'A35'): ('set', '  days 1-2 (66.6% of salary); a minority practice pays 100%. MERCANS DEFAULT: 66.67%, configurable.'),
 ('Employer Sick Pay', 'A37'): ('set', 'THE MINIMUM-WAGE FLOOR ON INCAPACITY PAYMENTS.'),
 ('Employer Sick Pay', 'A39'): ('set', '  administrative doctrine top the payment up to one minimum wage. Corte Constitucional C-543 de 2007'),
 ('Employer Sick Pay', 'A40'): ('set', '  holds that the sickness benefit may never fall below the minimum legal wage. MERCANS DEFAULT: apply'),
 ('Employer Sick Pay', 'A41'): ('set', '  the floor, configurable.'),
 ('Employer Sick Pay', 'A50'): ('set', '                            through payroll and recovered from the insurer outside the PILA: under AT2 v30 the'),
 ('Employer Sick Pay', 'A51'): ('set', '                            authorisation number and value (T2R2-057 to T2R2-060) are reported blank / zero.'),
 ('Employer Sick Pay', 'A57'): [('sub', 'CST arts. 227, 228, 236, 239; ', 'CST arts. 227, 228, 236, 239; ' + SICK_SRC)],
 ('Tax Credit', 'A68'): [('sub', ' Carried in the QA report.', '')],
 ('Wage Type Catalogue', 'Y327'): [('sub', '; PILA T2R2-057, T2R2-058', '; PILA T2R2-057 / T2R2-058 reported blank / zero (AT2 v30)')],
 ('Wage Type Catalogue', 'Y330'): [('sub', '; PILA T2R2-059, T2R2-060', '; PILA T2R2-059 / T2R2-060 reported blank / zero (AT2 v30)')],
 ('Form Reference Guide', 'E22'): [('sub', 'authorisation number and value at PILA rows 126-127 (T2R2-057, T2R2-058) for the employer\'s recovery.',
                                    'PILA rows 126-127 (T2R2-057, T2R2-058) are reported blank / zero under AT2 v30; the recovery from the EPS runs outside the PILA.')],
 ('Form Reference Guide', 'E23'): [('sub', 'authorisation number and value at PILA rows 128-129.', 'PILA rows 128-129 (T2R2-059, T2R2-060) are reported blank / zero under AT2 v30.')],
 ('Global WTC Coverage', 'C4'): [('sub', ' against CO-CCG-001 Modules 3-7 and the primary law in 00-official-sources/pdfs/.', ' against CO-CCG-001 Modules 3-7 and the primary law.')],
 ('Global WTC Coverage', 'C15'): [('sub', '(2) The auxilio de transporte amount is carried from the CCG because Decreto 1470 de 2025 is not in 00-official-sources.',
                                    '(2) The auxilio de transporte amount (249,095) is fixed by Decreto 1470 de 2025 art. 1.'),
                                   ('sub', '(3) The additional high-risk pension rate is read from the Resolucion 2388 rate table (26% total against 16% standard, implying +10 pp employer-borne), NOT from the implementing decree - see the open items below.',
                                    '(3) The additional high-risk pension rate is +10 points borne by the employer (26% total against 16% standard): Decreto-Ley 2090 de 2003 art. 5, matching the Resolucion 2388 rate table.')],
 ('Global WTC Coverage', 'B16'): ('set', 'Open items and Mercans defaults'),
 ('Global WTC Coverage', 'C16'): [('sub', 'allocates the days but not the rate; Mercans default 66.67%, configurable.',
                                    'allocates the days but not the rate; Concepto MinSalud 202311602174531 of 20 October 2023 applies CST art. 227 (two thirds); Mercans default 66.67%, configurable.'),
                                   ('sub', '(2) The minimum-wage floor on incapacity payments - primary source not retrieved; Mercans default applies the floor, configurable.',
                                    '(2) The minimum-wage floor on incapacity payments - Corte Constitucional C-543 de 2007 (the sickness benefit may not fall below the minimum legal wage); Mercans default applies the floor, configurable.'),
                                   ('sub', '(3) The additional employer pension contribution for Decreto Ley 2090 de 2003 high-risk activities - the 2026 rate and base not confirmed from a primary regulatory source.',
                                    '(3) The additional employer pension contribution for Decreto Ley 2090 de 2003 high-risk activities - +10 points (art. 5), regime extended by Decreto 1435 de 2025 until Congress legislates; no rule found for workers who started a high-risk activity between 1 January 2025 and that decree.')],
 ('Global WTC Coverage', 'B28'): [('sub', ' -- zero rows carrying this code in the main catalogue is expected, not an omission (CO-QA-REPORT.md MINOR-09).',
                                    ' -- zero rows carrying this code in the main catalogue is expected, not an omission.')],
}

PS_EN = ("* Payslip disclosure: the Codigo Sustantivo del Trabajo (CST) has no payslip-content article. Where a graphical representation "
         "of the payroll document is issued it must carry the content of the electronic payroll support document: devengados, "
         "deducciones and neto, itemised by concept, for the period (Resolucion DIAN 000227 de 2025, arts. 1.5.3.3.1 and 1.5.3.8.3). "
         "Separately, Ley 1393 de 2010, Art. 32 requires the employer to inform the employee of the social-security contributions "
         "paid or to ensure that the employee can check that they were paid; itemising them on the payslip is one way to meet it.")
PS_ES = ("* Divulgacion de nomina: el Codigo Sustantivo del Trabajo (CST) no contiene un articulo sobre el contenido del desprendible. "
         "Si se expide una representacion grafica del documento de nomina, debe llevar el contenido del documento soporte de pago de "
         "nomina electronica: devengados, deducciones y neto, detallados por concepto, del periodo (Resolucion DIAN 000227 de 2025, "
         "arts. 1.5.3.3.1 y 1.5.3.8.3). Ademas, la Ley 1393 de 2010, Art. 32 obliga al empleador a informar al trabajador los aportes "
         "pagados a la proteccion social o a garantizar que pueda consultar que fueron abonados; detallarlos en el desprendible es una "
         "forma de cumplirla.")
PAYSLIP = {
 ('Colombia (EN)', 'A78'): [('sub', "* Payslip disclosure: Colombia's Codigo Sustantivo del Trabajo (CST) has no single formatted-payslip article; the binding duty to disclose social-security contributions paid on the worker's behalf is Ley 1393 de 2010, Art. 32. The desprendible de nomina must itemise devengados, deducciones and neto for each pay period.", PS_EN)],
 ('Colombia (ES)', 'A78'): [('sub', "* Divulgacion de nomina: el Codigo Sustantivo del Trabajo (CST) no contiene un articulo unico que exija un formato de nomina; la obligacion vinculante de informar al trabajador los aportes a seguridad social pagados a su nombre esta en la Ley 1393 de 2010, Art. 32. El desprendible de nomina debe detallar devengados, deducciones y neto en cada periodo de pago.", PS_ES)],
}

XLSX = {'NE': NE, 'WTC': WTC, 'PAYSLIP': PAYSLIP}

DOCX = [
 # cover date = issue date (Version Control row 1.5)
 ('21 October 2026', '30 October 2026', {'prev2': 'Mercans Compliance Regulations Team'}),
 # Module 4.4: the reported percentage covers the four rest-day codes
 ("The engine therefore reports the real statutory percentage (80% or 90%), not the annex's legacy literal.",
  "The engine therefore reports the statutory percentage, not the annex's legacy literal: on the rest-day surcharge 80% / 90% / 100%, and on the three combined codes the sum shown in the table above (day overtime 105 / 115 / 125, night overtime 155 / 165 / 175, night surcharge 115 / 125 / 135), switching on 1 July 2025, 1 July 2026 and 1 July 2027 (or from the outset where the employer applies the full 100%)."),
 # Module 4 / incapacity: concept content and residual rework wording
 ('has the employer pay the first two days at 66.6% of salary, subject to the minimum-wage floor below. The Mercans default (66.67%, configurable) matches this concept.',
  'has the employer pay the first two days at 66.6% of salary; the minimum-wage floor below also applies. The Mercans default (66.67%, configurable) matches this concept.'),
 (' -- the source the doctrine was missing. The floor is now a cited rule, not an assumed one; the Mercans default (apply the floor) was already the correct position.',
  ' (resolutive part: the benefit "no podrá ser inferior al salario mínimo legal vigente").'),
 # Module 10.3: Law 1393 art. 32
 ('the itemisation of employer contributions for transparency (never a deduction from the employee);',
  'the itemisation of the contributions paid (the employer share is never a deduction from the employee): one way to meet the employer duty to inform the employee of the contributions paid or to let the employee check them (Law 1393 of 2010 art. 32);'),
 ('Substantive Labour Code (Decree 2663 of 1950), full consolidated text — no payslip-content article.',
  'Substantive Labour Code (Decree 2663 of 1950), full consolidated text — no payslip-content article; Law 1393 of 2010 art. 32 (information on contributions paid).'),
]

ITEMS = []
_d = [
 ('PR-01', 'NE', 'Nomina Electronica Spec!K109, K114, K119, K124, M109, M114, M119, M124; Field Options!A65, D61:D65',
  'The rest-day overtime / surcharge codes 4-7 carried the annex literals 100 / 75 / 150 / 110 pending "a written DIAN position", while CCG Module 4.4 reports the statutory percentage',
  "@Porcentaje carries the statutory percentage from the configured rate table: code 4 = 105 / 115 / 125, code 5 = 80 / 90 / 100, code 6 = 155 / 165 / 175, code 7 = 115 / 125 / 135 (from 1 July 2025 / 2026 / 2027); example values for July-December 2026",
  'DIAN Concepto 013840 int. 1568 of 1-10-2025 items 3(vii), 4 and 5 ("porcentaje que debe leerse en consonancia con la normatividad vigente"); CST art. 179 par. transitorio (Ley 2466 de 2025 art. 14); Technical Annex v1.0 table 5.5.5 (no later version)'),
 ('PR-01', 'CCG', 'paragraph (Module 4.4, reporting conflict)', 'Only the rest-day surcharge (80% / 90%) was named as the reported percentage',
  'The reported percentages of the three combined codes and the 1 July 2027 step are stated, in line with the NE specification', 'Same sources as above'),
 ('PR-02', 'WTC', 'Employer Sick Pay!A30, A34:A35, A37, A39:A41, A57; Global WTC Coverage!B16, C16',
  "'OPEN ITEM 1 / 2' (rate for the employer's first two days; minimum-wage floor 'not retrieved') although CCG Module 6 cites the sources",
  'Open-item labels removed; the rate cites Concepto MinSalud 202311602174531 of 2023 and the floor C-543 of 2007, as in the CCG; defaults unchanged',
  'Corte Constitucional C-543 de 2007 resolutive part ("no podrá ser inferior al salario mínimo legal vigente"); Concepto MinSalud 202311602174531 of 20-10-2023 ("serán asumidos por el empleador teniendo en cuenta el 66.6% del salario")'),
 ('PR-03', 'WTC', 'Global WTC Coverage!C15, C16', 'High-risk pension +10 points described as not confirmed from a primary source, while CCG Module 5.1.1 quotes Decreto-Ley 2090 de 2003 art. 5',
  '+10 points employer-borne under art. 5; the only open point kept is the one the CCG keeps (workers who started between 1-1-2025 and Decreto 1435 de 2025)', 'Decreto-Ley 2090 de 2003 art. 5; Decreto 1435 de 2025 (CCG Module 5.1.1)'),
 ('PR-04', 'WTC', 'Employer Sick Pay!A50:A51; Wage Type Catalogue!Y327, Y330; Form Reference Guide!E22, E23',
  'Incapacity / leave authorisation number and value said to be carried on the PILA (T2R2-057 to 060) for the recovery, while CO-PILA-003 reports them blank / zero',
  'Stated as blank / zero under AT2 v30; the recovery from the EPS runs outside the PILA', 'AT2 v30 (24-07-2026) campos 57-60 ("Debe reportarse en blanco" / "en cero")'),
 ('PR-05', 'WTC', 'Global WTC Coverage!B28, C4, C15; Tax Credit!A68', 'Internal working references (00-official-sources folder, QA report, finding id) in the product text; Decreto 1470 said not to be in the sources',
  'References removed; the transport allowance cites Decreto 1470 de 2025 art. 1', 'Decreto 1470 de 2025 art. 1 ($249.095)'),
 ('PR-06', 'PAYSLIP', 'Colombia (EN)!A78, Colombia (ES)!A78',
  'Ley 1393 de 2010 art. 32 presented as the binding payslip-disclosure duty and the itemisation as a labour rule, while the CCG (Module 10.3) bases the itemisation on Resolution DIAN 000227 and does not cite art. 32',
  'Itemisation based on Res. DIAN 000227 de 2025 arts. 1.5.3.3.1 and 1.5.3.8.3; art. 32 kept with its actual content (inform or let the employee check the contributions paid)',
  'Ley 1393 de 2010 art. 32 ("informar a los empleados sobre los aportes pagados ... o garantizar que estos puedan consultar"); CCG Module 10.3'),
 ('PR-06', 'CCG', 'paragraphs (Module 10.3 practice list and legal basis)', 'Law 1393 art. 32 not cited; contribution itemisation described only as transparency',
  'Art. 32 cited as the duty the itemisation helps meet; added to the legal basis', 'Ley 1393 de 2010 art. 32'),
 ('PR-07', 'CCG', 'paragraphs (Module 6, incapacity rate and floor)', 'The MinSalud concept was described as applying the minimum-wage floor, and the floor paragraph kept rework wording',
  'The floor is attributed to C-543 of 2007 only, with its resolutive text', 'Concepto MinSalud 202311602174531 (no floor statement); C-543 de 2007 resolutive part'),
 ('PR-08', 'CCG', 'paragraph (cover, Date)', "Cover date '21 October 2026' while the Version Control issues v1.5 on 30 October 2026", '30 October 2026', 'Version Control row 1.5'),
]
for i, a, w, fi, co, so in _d:
    ITEMS.append(dict(id=i, artifact=a, where=w, finding=fi, correction=co, source=so))
