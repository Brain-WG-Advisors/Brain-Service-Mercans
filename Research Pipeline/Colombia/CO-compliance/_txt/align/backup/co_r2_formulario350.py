# -*- coding: utf-8 -*-
"""
CO-DIAN-002 - Formulario 350, Declaracion de retenciones en la fuente.
Filing ID: CO-DIAN-F350-MONTHLY-002.

EVERY casilla number, label and arithmetic rule in this module is taken verbatim
from the OFFICIAL form design and instructivo held at
  00-official-sources/pdfs/Formulario_350_01082024.pdf
(prescribed by Resolucion DIAN 000031 of 29 February 2024, in force from
1 August 2024, and compiled at art. 1.2.2.26 of Resolucion DIAN 000227 of
23 September 2025). Extraction artefact: _txt/form350.txt.

C19 code pattern: the identifiers on this form are CASILLA NUMBERS, integers in
the ranges 1-155 (hoja 1 and hoja 2) plus the reserved 980-997 signature block.
Pattern: ^([1-9][0-9]{0,2})$ with the value present on the printed form. No
casilla number in this Spec is derived - each was read off the form design.
"""

from build_co_specs import (R_F350, R_NONE, RA)
from co_scope_common import SCOPE_WHO, SCOPE_TIMING


def F(en, es, rec, pos, mand, cond, xpath, length, fmt, ex, mapping, expl,
      rel, opts, rnd, neg, vt, freq, q, ra, kind):
    return [en, es, rec, pos, "", mand, cond, xpath, length, fmt, ex, mapping,
            expl, rel, opts, rnd, neg, vt, freq, q, ra, kind]


NA_NOTE = ("Not produced by payroll. Present on the form because Formulario 350 aggregates EVERY "
           "withholding the employer makes, not only payroll withholding. Populated by the client's "
           "accounts-payable or tax function; payroll contributes nothing to this casilla.")

FIELDS = [
    "DECLARANT AND PERIOD (hoja 1, casillas 1-12)",
    F("Tax year", "Ano", "Datos del declarante", "1", "Y", "",
      "Hoja 1, casilla 1", "4", "N (AAAA)", "2026", "PayPeriod.Year",
      "Calendar year of the period being declared. The form is prescribed for periods from "
      "1 August 2024 onward (Res. DIAN 000031 de 2024 art. 3).",
      "Y", "-", R_NONE, "N", "Date", "Monthly", "", RA, "system"),
    F("Period", "Periodo", "Datos del declarante", "3", "Y", "",
      "Hoja 1, casilla 3", "2", "N (01-12)", "03", "PayPeriod.Month",
      "Calendar month being declared, 01 to 12. Formulario 350 is a MONTHLY return; there is no "
      "quarterly or annual variant for withholding agents.",
      "Y", "-> Sheet 6: Periodo", R_NONE, "N", "Code", "Monthly", "", RA, "system"),
    F("Form number", "Numero de formulario", "Datos del declarante", "4", "Y", "",
      "Hoja 1, casilla 4", "13", "N", "1120500123456", "System.DIAN_Form_Number",
      "Assigned by the DIAN electronic filing service, not by the declarant - the form prints "
      "'Espacio reservado para la DIAN' against it. It becomes the reference quoted in casilla 26 "
      "of any later corrective return.",
      "N", "-", R_NONE, "N", "Identifier", "Monthly", "", RA, "system"),
    F("Employer NIT", "Numero de Identificacion Tributaria (NIT)", "Datos del declarante", "5", "Y", "",
      "Hoja 1, casilla 5", "Var", "N (no dots, no hyphens)", "900123456", "Company.NIT",
      "Tax identification number of the withholding agent, taken from casilla 5 of the RUT. The last "
      "digit of this number determines the filing deadline (7th to 16th business day of the "
      "following month). Join key to the nomina electronica (NIE033) and to PILA.",
      "Y", "-", R_NONE, "N", "Identifier", "Monthly", "", RA, "payroll"),
    F("NIT verification digit", "DV", "Datos del declarante", "6", "Y", "",
      "Hoja 1, casilla 6", "1", "N", "7", "Company.NIT_DV",
      "DIAN check digit of the NIT, from casilla 6 of the RUT.",
      "Y", "-", R_NONE, "N", "Identifier", "Monthly", "", RA, "payroll"),
    F("First surname", "Primer apellido", "Datos del declarante", "7", "C",
      "Populated only where the withholding agent is a NATURAL person. Mutually exclusive with "
      "'Corporate name' (casilla 11): a legal person populates 11 and leaves 7 to 10 blank, and a "
      "natural person does the reverse.",
      "Hoja 1, casilla 7", "Var", "A", "-", "Company.First_Surname",
      "First surname of a natural-person withholding agent, from casilla 31 of the RUT. Auto-filled "
      "by the DIAN service from the RUT.",
      "Y", "-", R_NONE, "N", "Text", "Monthly", "", RA, "payroll"),
    F("Second surname", "Segundo apellido", "Datos del declarante", "8", "C",
      "Populated only for a natural-person withholding agent. Mutually exclusive with 'Corporate "
      "name' (casilla 11).",
      "Hoja 1, casilla 8", "Var", "A", "-", "Company.Second_Surname",
      "Second surname of a natural-person withholding agent, from casilla 32 of the RUT.",
      "Y", "-", R_NONE, "N", "Text", "Monthly", "", RA, "payroll"),
    F("First name", "Primer nombre", "Datos del declarante", "9", "C",
      "Populated only for a natural-person withholding agent. Mutually exclusive with 'Corporate "
      "name' (casilla 11).",
      "Hoja 1, casilla 9", "Var", "A", "-", "Company.First_Name",
      "First given name of a natural-person withholding agent, from casilla 33 of the RUT.",
      "Y", "-", R_NONE, "N", "Text", "Monthly", "", RA, "payroll"),
    F("Other names", "Otros nombres", "Datos del declarante", "10", "C",
      "Populated only for a natural-person withholding agent. Mutually exclusive with 'Corporate "
      "name' (casilla 11).",
      "Hoja 1, casilla 10", "Var", "A", "-", "Company.Other_Names",
      "Remaining given names of a natural-person withholding agent, from casilla 34 of the RUT.",
      "Y", "-", R_NONE, "N", "Text", "Monthly", "", RA, "payroll"),
    F("Corporate name", "Razon social", "Datos del declarante", "11", "C",
      "Populated only where the withholding agent is a LEGAL person. Mutually exclusive with the "
      "natural-person name casillas 7, 8, 9 and 10.",
      "Hoja 1, casilla 11", "Var", "A", "MERCANS COLOMBIA S.A.S.", "Company.Legal_Name",
      "Corporate name, auto-filled by the DIAN service from casilla 35 of the RUT. The instructivo "
      "says expressly that it 'se diligencia automaticamente' - do not attempt to override it.",
      "Y", "-", R_NONE, "N", "Text", "Monthly", "", RA, "payroll"),
    F("Sectional office code", "Cod. Direccion seccional", "Datos del declarante", "12", "Y", "",
      "Hoja 1, casilla 12", "2", "N (code)", "32", "Company.DIAN_Seccional_Code",
      "Code of the DIAN sectional office of the taxpayer's principal domicile, from casilla 12 of "
      "the RUT. A configuration attribute of the entity, not a period value.",
      "Y", "-> Sheet 6: Direccion seccional", R_NONE, "N", "Code", "Constant", "", RA, "payroll"),

    "CORRECTION BLOCK (hoja 1, casillas 25-26)",
    F("Correction code", "Cod. (correccion)", "Correccion", "25", "C",
      "Populated ONLY where this return corrects an earlier one. Bidirectional pair with 'Previous "
      "form number' (casilla 26): where 25 is populated 26 must be populated, and vice versa. Both "
      "blank on an initial return.",
      "Hoja 1, casilla 25", "1", "N (code)", "-", "Mercans.Correction_Type",
      "Set by the DIAN service: 1 = correction of the taxpayer's own return; 2 = correction of a "
      "DIAN-generated correction under Ley 962 de 2005 art. 43; 3 = correction prompted by an "
      "administrative act.",
      "N", "-> Sheet 6: Codigo de correccion", R_NONE, "N", "Code", "Per event", "", RA, "system"),
    F("Previous form number", "Numero de formulario anterior", "Correccion", "26", "C",
      "Populated ONLY on a corrective return. Bidirectional pair with 'Correction code' "
      "(casilla 25). Carries the casilla-4 number of the return being corrected.",
      "Hoja 1, casilla 26", "13", "N", "-", "Mercans.Prior_Form_Number",
      "The casilla 4 form number of the return, or of the administrative act, being corrected. This "
      "is the link that lets DIAN supersede the earlier filing rather than treat this one as a "
      "duplicate.",
      "N", "-", R_NONE, "N", "Identifier", "Per event", "", RA, "system"),

    "SELF-WITHHOLDING CONFIGURATION (hoja 1, casillas 27-28)",
    F("Self-withholding activity code (art. 114-1 exonerated legal persons)",
      "Autorretenedores Personas Juridicas exonerados de aportes (Art. 114-1 E.T.) - Actividad "
      "economica principal", "Autorretencion", "27", "C",
      "Fillable EXCLUSIVELY by legal persons that are exonerated from employer contributions under "
      "ET art. 114-1. Bidirectional pair with 'Self-withholding rate' (casilla 28), which the DIAN "
      "service derives automatically once 27 is chosen.",
      "Hoja 1, casilla 27", "4", "N (CIIU code)", "6920", "Company.CIIU_Code",
      "Principal economic-activity code from casilla 46 of the RUT, chosen from the codes in DIAN "
      "Resoluciones 000114 of 21 December 2020, 001232 of 16 September 2022 and 000086 of 24 May "
      "2023. THE SAME ART. 114-1 EXONERATION that drives this casilla also drives PILA archivo tipo "
      "1 field 33 and Registro Tipo 2 field 76 - the employer that is exonerated from employer "
      "health, SENA and ICBF for employees under 10 SMMLV is the employer that self-withholds here.",
      "Y", "-> Sheet 6: Actividad economica (CIIU)", R_NONE, "N", "Code", "Constant", "", RA, "payroll"),
    F("Self-withholding rate", "Tarifa", "Autorretencion", "28", "C",
      "Derived automatically by the DIAN service from 'Self-withholding activity code' (casilla 27); "
      "cannot be keyed independently. Bidirectional pair with casilla 27.",
      "Hoja 1, casilla 28", "Var", "N (percentage)", "0.40", "Mercans.Self_Withholding_Rate",
      "The self-withholding rate for the chosen activity, applied to ALL payments received. Set by "
      "DUR 1625 de 2016 art. 1.2.6.8. Not a payroll figure - it applies to the employer's own "
      "income, not to its employees.",
      "N", "-", "Rate as printed by the DIAN service.", "N", "Rate", "Constant", "", RA, "system"),

    "PAYROLL WITHHOLDING - THE TWO CASILLAS THAT PAYROLL OWNS (hoja 1, 77 and 93)",
    F("Base - work income (natural persons)", "Rentas de trabajo - base sujeta a retencion",
      "Retenciones renta - personas naturales", "77", "Y", "",
      "Hoja 1, casilla 77", "12", "N (whole pesos, nearest 1,000)", "8190000",
      "SUM(Employee.Taxable_Base_Art388)",
      "THE PRINCIPAL PAYROLL CASILLA ON THE BASE SIDE. The instructivo defines it as 'los pagos "
      "gravables (base sujeta a retencion) efectuados a personas naturales por concepto de salarios, "
      "comisiones, prestaciones sociales, viaticos, gastos de representacion, honorarios, "
      "emolumentos eclesiasticos, compensaciones recibidas por el trabajo asociado cooperativo, "
      "pagos en especie, pagos en acciones y, en general, las compensaciones por servicios "
      "personales'. NOTE that it is the DEPURATED taxable base, not the gross: for a resident it is "
      "the ET art. 388 base after non-constitutive income, art. 387 deductions and the 25% exempt "
      "income; for a NON-RESIDENT taxed under art. 408 the base is the GROSS, because art. 408 "
      "admits no depuration. Note also that it sweeps in honorarios paid to natural persons under "
      "the art. 383 table, which are not employment income - payroll supplies only the employment "
      "component.",
      "Y", "-", R_F350, "N", "Amount", "Monthly", "", RA, "payroll"),
    F("Withholding - work income (natural persons)", "Rentas de trabajo - retenciones a titulo de renta",
      "Retenciones renta - personas naturales", "93", "Y", "",
      "Hoja 1, casilla 93", "12", "N (whole pesos, nearest 1,000)", "617000",
      "SUM(Employee.Income_Tax_Withheld)",
      "THE PRINCIPAL PAYROLL CASILLA ON THE WITHHOLDING SIDE. The month's total retencion en la "
      "fuente on work income paid to natural persons. Must reconcile to the sum of RetencionFuente "
      "(NIE177) across every nomina electronica document for the same month, after the "
      "nearest-1,000 rounding. It is one of the forty-two casillas summed into casilla 130.",
      "Y", "-", R_F350, "N", "Amount", "Monthly", "", RA, "payroll"),
    F("Base - pension income (natural persons)", "Rentas de pensiones - base sujeta a retencion",
      "Retenciones renta - personas naturales", "78", "C",
      "Populated only where the EMPLOYER itself pays a pension. Bidirectional pair with 'Withholding "
      "- pension income' (casilla 94): a base without a withholding, or the reverse, is an "
      "inconsistency. Blank for an ordinary corporate payroll, where pensions are paid by a fund.",
      "Hoja 1, casilla 78", "12", "N (whole pesos, nearest 1,000)", "-",
      "SUM(Employee.Pension_Taxable_Base)",
      "The monthly pension payment EXCEEDING 1,000 UVT (COP 52,374,000 in 2026) under ET art. 206 "
      "num. 5, for retirement, invalidity, old-age, survivor and occupational-risk pensions and for "
      "substitute indemnities and returns of pension savings. Only the excess over 1,000 UVT is "
      "taxable, so the casilla is nil for the overwhelming majority of pensions.",
      "Y", "-", R_F350, "N", "Amount", "Monthly", "", RA, "payroll"),
    F("Withholding - pension income (natural persons)", "Rentas de pensiones - retenciones",
      "Retenciones renta - personas naturales", "94", "C",
      "Populated only where the employer pays a pension. Bidirectional pair with 'Base - pension "
      "income' (casilla 78).",
      "Hoja 1, casilla 94", "12", "N (whole pesos, nearest 1,000)", "-",
      "SUM(Employee.Pension_Tax_Withheld)",
      "Withholding on the taxable excess of employer-paid pension income. Summed into casilla 130.",
      "Y", "-", R_F350, "N", "Amount", "Monthly", "", RA, "payroll"),

    "NON-RESIDENT PAYMENTS ABROAD - hoja 1 summary casillas (v2.8 control B1)",
    F("Base - payments abroad, no treaty (legal persons)",
      "Pagos o abonos en cuenta al exterior a paises sin convenio - base",
      "Pagos exterior - personas juridicas", "55", "C",
      "Auto-derived by the DIAN service from the hoja 2 annex: it is the sum of the casilla 145 "
      "values where casilla 141 = SIN CONVENIO and casilla 143 = Persona juridica. Bidirectional "
      "pair with 'Withholding - payments abroad, no treaty (legal persons)' (casilla 57) and with "
      "hoja 2 total casilla 148.",
      "Hoja 1, casilla 55", "12", "N (whole pesos, nearest 1,000)", "-",
      "(derived from hoja 2 casilla 148)",
      "Base of payments to foreign ENTITIES without a Colombian domicile, in countries with no "
      "double-tax treaty. Not a payroll casilla - a foreign entity is not an employee - but shown "
      "here because it shares the hoja 2 annex with the non-resident EMPLOYEE casillas.",
      "N", "-", R_F350, "N", "Amount", "Monthly", "", RA, "na"),
    F("Withholding - payments abroad, no treaty (legal persons)",
      "Pagos o abonos en cuenta al exterior a paises sin convenio - retenciones",
      "Pagos exterior - personas juridicas", "57", "C",
      "Auto-derived from hoja 2 total casilla 150. Bidirectional pair with casilla 55.",
      "Hoja 1, casilla 57", "12", "N (whole pesos, nearest 1,000)", "-",
      "(derived from hoja 2 casilla 150)",
      "Withholding on payments to foreign entities in non-treaty countries. Summed into casilla 130.",
      "N", "-", R_F350, "N", "Amount", "Monthly", "", RA, "na"),
    F("Base - payments abroad, treaty (legal persons)",
      "Pagos o abonos en cuenta al exterior a paises con convenio vigente - base",
      "Pagos exterior - personas juridicas", "56", "C",
      "Auto-derived from hoja 2 total casilla 152. Bidirectional pair with casilla 58.",
      "Hoja 1, casilla 56", "12", "N (whole pesos, nearest 1,000)", "-",
      "(derived from hoja 2 casilla 152)",
      "Base of payments to foreign entities in countries with a double-tax treaty in force.",
      "N", "-", R_F350, "N", "Amount", "Monthly", "", RA, "na"),
    F("Withholding - payments abroad, treaty (legal persons)",
      "Pagos o abonos en cuenta al exterior a paises con convenio vigente - retenciones",
      "Pagos exterior - personas juridicas", "58", "C",
      "Auto-derived from hoja 2 total casilla 154. Bidirectional pair with casilla 56.",
      "Hoja 1, casilla 58", "12", "N (whole pesos, nearest 1,000)", "-",
      "(derived from hoja 2 casilla 154)",
      "Withholding on payments to foreign entities in treaty countries.",
      "N", "-", R_F350, "N", "Amount", "Monthly", "", RA, "na"),
    F("Base - payments abroad, no treaty (NATURAL persons)",
      "Pagos o abonos en cuenta al exterior a paises sin convenio - base - personas naturales",
      "Pagos exterior - personas naturales", "109", "C",
      "THE NON-RESIDENT EMPLOYEE BASE CASILLA where the employee's country has no treaty. "
      "Auto-derived by the DIAN service from hoja 2 total casilla 149 - the sum of casilla 145 where "
      "casilla 141 = SIN CONVENIO and casilla 143 = Persona natural. Bidirectional pair with "
      "'Withholding - payments abroad, no treaty (natural persons)' (casilla 111).",
      "Hoja 1, casilla 109", "12", "N (whole pesos, nearest 1,000)", "-",
      "SUM(Employee.NonResident_Gross) WHERE treaty = none",
      "Gross payments to non-resident natural persons in non-treaty countries. For an employee this "
      "is the GROSS salary - ET art. 408 admits no depuration - reported through hoja 2 concepto de "
      "pago 5, 'Prestaciones de servicios y compensacion por servicios personales'.",
      "Y", "-", R_F350, "N", "Amount", "Monthly", "", RA, "payroll"),
    F("Withholding - payments abroad, no treaty (NATURAL persons)",
      "Pagos o abonos en cuenta al exterior a paises sin convenio - retenciones - personas naturales",
      "Pagos exterior - personas naturales", "111", "C",
      "Auto-derived from hoja 2 total casilla 151. Bidirectional pair with casilla 109.",
      "Hoja 1, casilla 111", "12", "N (whole pesos, nearest 1,000)", "-",
      "SUM(Employee.NonResident_Withholding) WHERE treaty = none",
      "Withholding on those payments - the flat 20% of ET art. 408 for employment income. Summed "
      "into casilla 130.",
      "Y", "-", R_F350, "N", "Amount", "Monthly", "", RA, "payroll"),
    F("Base - payments abroad, treaty (NATURAL persons)",
      "Pagos o abonos en cuenta al exterior a paises con convenio vigente - base - personas naturales",
      "Pagos exterior - personas naturales", "110", "C",
      "THE NON-RESIDENT EMPLOYEE BASE CASILLA where a double-tax treaty applies. Auto-derived from "
      "hoja 2 total casilla 153. Bidirectional pair with 'Withholding - payments abroad, treaty "
      "(natural persons)' (casilla 112).",
      "Hoja 1, casilla 110", "12", "N (whole pesos, nearest 1,000)", "-",
      "SUM(Employee.NonResident_Gross) WHERE treaty = yes",
      "Gross payments to non-resident natural persons in treaty countries, reported through hoja 2 "
      "concepto de pago 24, 'Rentas de trabajo' - the concept whose own definition is 'rentas de "
      "trabajo de cualquier naturaleza en relacion con un empleo a favor de personas naturales no "
      "residentes'. This is the exact place a non-resident EMPLOYEE with treaty cover is reported.",
      "Y", "-", R_F350, "N", "Amount", "Monthly", "", RA, "payroll"),
    F("Withholding - payments abroad, treaty (NATURAL persons)",
      "Pagos o abonos en cuenta al exterior a paises con convenio vigente - retenciones - personas "
      "naturales", "Pagos exterior - personas naturales", "112", "C",
      "Auto-derived from hoja 2 total casilla 155. Bidirectional pair with casilla 110.",
      "Hoja 1, casilla 112", "12", "N (whole pesos, nearest 1,000)", "-",
      "SUM(Employee.NonResident_Withholding) WHERE treaty = yes",
      "Withholding after treaty relief. Where the treaty assigns taxing rights to the residence "
      "state the rate may be reduced to nil. Mercans applies treaty relief ONLY on written client "
      "instruction supported by a residence certificate.",
      "Y", "-", R_F350, "N", "Amount", "Monthly", "", RA, "payroll"),

    "NON-RESIDENT ANNEX - hoja 2 (casillas 141-155)",
    F("Treaty status", "A paises con o sin convenio", "Hoja 2 - anexo", "141", "C",
      "One row per payment concept, country and person type. Drives which concepto list applies in "
      "casilla 142 and which of the four totals (148, 149, 152, 153) the row feeds. Bidirectional "
      "with casilla 142 and casilla 143.",
      "Hoja 2, casilla 141", "Var", "Selection", "CON CONVENIO", "Employee.Treaty_Country_Code",
      "Drop-down: SIN CONVENIO or CON CONVENIO. Choosing CON CONVENIO switches casilla 142 to the "
      "treaty concept list (19 to 33) and requires the applicable double-tax treaty to be consulted "
      "for the rate.",
      "Y", "-> Sheet 6: Convenio", R_NONE, "N", "Code", "Per record", "", RA, "payroll"),
    F("Payment concept", "Concepto de pago", "Hoja 2 - anexo", "142", "C",
      "The list offered depends on 'Treaty status' (casilla 141): concepts 1-18 for SIN CONVENIO, "
      "19-33 for CON CONVENIO. Bidirectional pair with casilla 141.",
      "Hoja 2, casilla 142", "2", "N (code)", "24", "Mercans.Foreign_Payment_Concept",
      "For a NON-RESIDENT EMPLOYEE the two relevant concepts are: SIN CONVENIO concepto 5, "
      "'Prestaciones de servicios y compensacion por servicios personales'; CON CONVENIO concepto "
      "24, 'Rentas de trabajo' - expressly 'rentas de trabajo de cualquier naturaleza en relacion "
      "con un empleo'. Concepto 25 covers directors' fees and concepto 27 pensions. NOTE the "
      "documentation conflict recorded in the RA query column.",
      "Y", "-> Sheet 6: Concepto de pago (hoja 2)", R_NONE, "N", "Code", "Per record",
      "SOURCE CONFLICT, escalate. Res. DIAN 000227 de 2025 art. 1.2.2.26 par. 3 refers to 'la "
      "Casilla 91 - Concepto de pago de la hoja dos' and to options '01. Enajenacion de activos "
      "fijos y otras retenciones' and '14. Otras rentas'. On the currently prescribed form the "
      "hoja-2 concepto de pago is CASILLA 142, and its option 14 is 'Servicios de transporte "
      "internacional' - option 1 is 'Intereses'. The compilation resolution appears to cite a "
      "superseded form. Confirm the correct casilla and option codes for reporting significant "
      "economic presence (ET art. 20-3) with the RA.", RA, "payroll"),
    F("Person type", "Tipo de persona", "Hoja 2 - anexo", "143", "C",
      "Determines whether the row feeds the legal-person totals (148 / 150 / 152 / 154) or the "
      "natural-person totals (149 / 151 / 153 / 155). Bidirectional with casillas 141 and 142. This "
      "column is NEW in the 2024 form.",
      "Hoja 2, casilla 143", "Var", "Selection", "Persona natural", "Mercans.Counterparty_Type",
      "Persona juridica or Persona natural. A non-resident EMPLOYEE is always Persona natural; this "
      "is the field that separates employee withholding from supplier withholding in the annex.",
      "Y", "-> Sheet 6: Tipo de persona", R_NONE, "N", "Code", "Per record", "", RA, "payroll"),
    F("Recipient country", "Pais", "Hoja 2 - anexo", "144", "C",
      "Required on every annex row. Where 'Treaty status' (casilla 141) = CON CONVENIO the country "
      "must be one with a treaty in force.",
      "Hoja 2, casilla 144", "Var", "Country code", "ES", "Employee.Treaty_Country_Code",
      "Country receiving the payment, with its country code. Colombia's treaty network in force "
      "includes Spain, Chile, Switzerland, Canada, Mexico, South Korea, Portugal, India, the Czech "
      "Republic, the United Kingdom, France, Italy and Japan, plus Andean Community Decision 578.",
      "Y", "-> Sheet 6: Paises con convenio", R_NONE, "N", "Code", "Per record", "", RA, "payroll"),
    F("Payments or credits", "Pagos o abonos en cuenta", "Hoja 2 - anexo", "145", "C",
      "Required on every annex row. Together with 'Rate' (casilla 146) it produces 'Withholding "
      "value' (casilla 147) automatically.",
      "Hoja 2, casilla 145", "12", "N (whole pesos, nearest 1,000)", "12000000",
      "Employee.NonResident_Gross",
      "GROSS amount paid or credited to the non-resident. For an employee this is the whole salary - "
      "ET art. 408 taxes the gross, with no deduction of the mandatory social-security contributions.",
      "Y", "-", R_F350, "N", "Amount", "Per record", "", RA, "payroll"),
    F("Rate", "Tarifa (%)", "Hoja 2 - anexo", "146", "C",
      "Required on every annex row. Determined by ET art. 408 for non-treaty payments, or by the "
      "applicable treaty article for treaty payments. Bidirectional pair with casilla 141: the "
      "treaty status determines which rate source applies.",
      "Hoja 2, casilla 146", "Var", "N (percentage)", "20.00", "Mercans.NonResident_Rate",
      "20% is the general ET art. 408 rate for employment income and personal services. Special "
      "rates in the instructivo include 15% for long-term foreign credits, 5% for international "
      "transport and for APP-financing interest, 33% for head-office management charges, 1% for "
      "aircraft leasing and reinsurance premiums, and 7% for foreign professors on contracts of up "
      "to four months.",
      "Y", "-> Sheet 6: Tarifas pagos al exterior", "Rate as a percentage.", "N", "Rate",
      "Per record", "", RA, "system"),
    F("Withholding value", "Valor retencion", "Hoja 2 - anexo", "147", "C",
      "Computed automatically by the DIAN service as casilla 145 x casilla 146. Not keyed. "
      "Bidirectional with casillas 145 and 146.",
      "Hoja 2, casilla 147", "12", "N (whole pesos, nearest 1,000)", "2400000",
      "Employee.NonResident_Withholding",
      "The instructivo states expressly that 'el SI de Diligenciamiento calcula automaticamente los "
      "valores de las retenciones multiplicando el valor registrado en la casilla 145 por la tarifa "
      "registrada en la casilla 146'. Payroll supplies 145 and 146; it must NOT attempt to key 147.",
      "Y", "-", R_F350, "N", "Amount", "Per record", "", RA, "payroll"),
    F("Total base - no treaty, legal persons", "Pagos al exterior paises sin convenio persona juridica",
      "Hoja 2 - totales", "148", "C", "Auto-summed where casilla 141 = SIN CONVENIO and casilla 143 "
      "= Persona juridica. Feeds hoja 1 casilla 55.",
      "Hoja 2, casilla 148", "12", "N (whole pesos, nearest 1,000)", "-", "(system total)",
      "Sum of casilla 145 across the matching annex rows. Carried up to hoja 1 casilla 55.",
      "N", "-", R_F350, "N", "Amount", "Monthly", "", RA, "na"),
    F("Total base - no treaty, natural persons",
      "Pagos al exterior paises sin convenio persona natural", "Hoja 2 - totales", "149", "C",
      "Auto-summed where casilla 141 = SIN CONVENIO and casilla 143 = Persona natural. Feeds hoja 1 "
      "casilla 109.",
      "Hoja 2, casilla 149", "12", "N (whole pesos, nearest 1,000)", "-", "(system total)",
      "Sum of casilla 145 across the matching annex rows. This is where a non-resident employee in a "
      "non-treaty country lands. Carried up to hoja 1 casilla 109.",
      "N", "-", R_F350, "N", "Amount", "Monthly", "", RA, "system"),
    F("Total withholding - no treaty, legal persons", "Valor retencion sin convenio persona juridica",
      "Hoja 2 - totales", "150", "C", "Auto-summed; feeds hoja 1 casilla 57.",
      "Hoja 2, casilla 150", "12", "N (whole pesos, nearest 1,000)", "-", "(system total)",
      "Sum of casilla 147 across the matching annex rows.",
      "N", "-", R_F350, "N", "Amount", "Monthly", "", RA, "na"),
    F("Total withholding - no treaty, natural persons",
      "Valor retencion sin convenio persona natural", "Hoja 2 - totales", "151", "C",
      "Auto-summed; feeds hoja 1 casilla 111.",
      "Hoja 2, casilla 151", "12", "N (whole pesos, nearest 1,000)", "-", "(system total)",
      "Sum of casilla 147 across the matching annex rows - the non-resident employee withholding in "
      "non-treaty countries.",
      "N", "-", R_F350, "N", "Amount", "Monthly", "", RA, "system"),
    F("Total base - treaty, legal persons", "Pagos al exterior paises con convenio persona juridica",
      "Hoja 2 - totales", "152", "C", "Auto-summed; feeds hoja 1 casilla 56.",
      "Hoja 2, casilla 152", "12", "N (whole pesos, nearest 1,000)", "-", "(system total)",
      "Sum of casilla 145 across the matching annex rows.",
      "N", "-", R_F350, "N", "Amount", "Monthly", "", RA, "na"),
    F("Total base - treaty, natural persons", "Pagos al exterior paises con convenio persona natural",
      "Hoja 2 - totales", "153", "C", "Auto-summed; feeds hoja 1 casilla 110.",
      "Hoja 2, casilla 153", "12", "N (whole pesos, nearest 1,000)", "12000000", "(system total)",
      "Sum of casilla 145 across the matching annex rows - where a non-resident employee covered by "
      "a treaty lands, under concepto de pago 24.",
      "N", "-", R_F350, "N", "Amount", "Monthly", "", RA, "system"),
    F("Total withholding - treaty, legal persons", "Valor retencion con convenio persona juridica",
      "Hoja 2 - totales", "154", "C", "Auto-summed; feeds hoja 1 casilla 58.",
      "Hoja 2, casilla 154", "12", "N (whole pesos, nearest 1,000)", "-", "(system total)",
      "Sum of casilla 147 across the matching annex rows.",
      "N", "-", R_F350, "N", "Amount", "Monthly", "", RA, "na"),
    F("Total withholding - treaty, natural persons",
      "Retenciones sobre pagos al exterior paises con convenio persona natural",
      "Hoja 2 - totales", "155", "C", "Auto-summed; feeds hoja 1 casilla 112.",
      "Hoja 2, casilla 155", "12", "N (whole pesos, nearest 1,000)", "2400000", "(system total)",
      "Sum of casilla 147 across the matching annex rows - the non-resident employee withholding "
      "after treaty relief.",
      "N", "-", R_F350, "N", "Amount", "Monthly", "", RA, "system"),

    "NON-PAYROLL WITHHOLDING CONCEPTS - NOT PRODUCED BY PAYROLL",
    F("Bases and withholdings on legal persons", "Bases y retenciones a personas juridicas",
      "Retenciones renta - personas juridicas", "29-54", "C",
      "Populated by the client's accounts-payable function where the corresponding payment was made. "
      "Payroll contributes nothing.",
      "Hoja 1, casillas 29 to 54", "12", "N (whole pesos, nearest 1,000)", "-",
      "(client accounts payable)",
      "Fourteen concept pairs for payments to legal persons - honorarios (29 / 42), comisiones "
      "(30 / 43), servicios (31 / 44), rendimientos financieros (32 / 45), arrendamientos (33 / 46), "
      "regalias (34 / 47), dividendos (35 / 48), compras (36 / 49), tarjetas (37 / 50), contratos de "
      "construccion (38 / 51), loterias (39 / 52), hidrocarburos (40 / 53) and otros pagos (41 / 54). "
      + NA_NOTE,
      "N", "-", R_F350, "N", "Amount", "Monthly", "", RA, "na"),
    F("Bases and withholdings on natural persons, non-employment concepts",
      "Bases y retenciones a personas naturales - conceptos no laborales",
      "Retenciones renta - personas naturales", "79-92 / 95-108", "C",
      "Populated by accounts payable. Payroll contributes only casillas 77 / 93 and, where "
      "applicable, 78 / 94.",
      "Hoja 1, casillas 79 to 92 and 95 to 108", "12", "N (whole pesos, nearest 1,000)", "-",
      "(client accounts payable)",
      "The same concept grid repeated for natural persons - honorarios (79 / 95), comisiones "
      "(80 / 96), servicios (81 / 97), and so on to otros pagos (92 / 108), plus enajenacion de "
      "activos fijos (89 / 105) which exists only in the natural-person column. Honorarios paid to a "
      "natural person under the art. 383 table can straddle 77 / 93 and 79 / 95; the boundary is a "
      "client decision, documented in the Population Rules. " + NA_NOTE,
      "N", "-", R_F350, "N", "Amount", "Monthly", "", RA, "na"),
    F("Self-withholding blocks", "Autorretenciones", "Autorretenciones", "59-76 / 113-128", "C",
      "Populated where the employer is an authorised self-withholding agent. Casilla 59 / 68 is the "
      "art. 114-1 self-withholding driven by casillas 27 and 28.",
      "Hoja 1, casillas 59 to 76 and 113 to 128", "12", "N (whole pesos, nearest 1,000)", "-",
      "(client tax function)",
      "Self-withholding on the employer's OWN income - ventas, honorarios, comisiones, servicios, "
      "rendimientos financieros, mining exports and otros conceptos, for legal persons (59-76) and "
      "natural persons (113-128). " + NA_NOTE,
      "N", "-", R_F350, "N", "Amount", "Monthly", "", RA, "na"),
    F("VAT and stamp-duty withholding", "Retenciones IVA y timbre nacional",
      "Otros impuestos", "131-135", "C",
      "Populated by the client's tax function. Casilla 132 is the withholding on services supplied "
      "by non-residents or non-domiciled persons.",
      "Hoja 1, casillas 131 to 135", "12", "N (whole pesos, nearest 1,000)", "-",
      "(client tax function)",
      "131 VAT withheld from VAT-responsible suppliers; 132 VAT withheld on services from "
      "non-residents; 133 excess or undue VAT withholding reversed; 134 total VAT withholding "
      "(131 + 132 - 133); 135 national stamp-duty withholding. " + NA_NOTE,
      "N", "-", R_F350, "N", "Amount", "Monthly", "", RA, "na"),

    "TOTALS, PENALTIES AND SIGNATURE",
    F("Less excess or undue withholding", "Menos retenciones practicadas en exceso o indebidas",
      "Totales", "129", "C",
      "Populated where withholding was practised in excess or in error, or on transactions annulled, "
      "rescinded or resolved. Subtracted in casilla 130.",
      "Hoja 1, casilla 129", "12", "N (whole pesos, nearest 1,000)", "-",
      "Payroll.Withholding_Reversal",
      "Amounts over-withheld or wrongly withheld, and reversals of withholding on cancelled "
      "transactions. Where the month's withholding is insufficient to absorb the credit, the "
      "instructivo permits carrying it to the immediately following periods. Payroll DOES feed this "
      "casilla where an employee's withholding is corrected downward in a later month.",
      "Y", "-", R_F350, "N", "Amount", "Monthly", "", RA, "payroll"),
    F("Total income-tax withholding", "Total retenciones renta y complementario", "Totales", "130", "Y", "",
      "Hoja 1, casilla 130", "12", "N (whole pesos, nearest 1,000)", "617000", "(system total)",
      "The instructivo prints the arithmetic in full: the sum of casillas 42, 43, 44, 45, 46, 47, 48, "
      "49, 50, 51, 52, 53, 54, 57, 58, 68, 69, 70, 71, 72, 73, 74, 75, 76, 93, 94, 95, 96, 97, 98, "
      "99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 111, 112, 121, 122, 123, 124, 125, 126, 127 "
      "and 128, LESS casilla 129. Payroll's contribution enters through 93, 94, 111 and 112.",
      "Y", "-", R_F350, "N", "Amount", "Monthly", "", RA, "system"),
    F("Total withholding", "Total retenciones", "Totales", "136", "Y", "",
      "Hoja 1, casilla 136", "12", "N (whole pesos, nearest 1,000)", "617000", "(system total)",
      "Casilla 130 (income tax) plus casilla 134 (VAT) plus casilla 135 (stamp duty).",
      "N", "-", R_F350, "N", "Amount", "Monthly", "", RA, "system"),
    F("Penalties", "Sanciones", "Totales", "137", "C",
      "Populated where a penalty arises on this filing - late filing or correction. Feeds casilla 138.",
      "Hoja 1, casilla 137", "12", "N (whole pesos, nearest 1,000)", "-", "Mercans.Penalty_Amount",
      "Total penalties arising from this return. The instructivo warns that the penalty declared "
      "cannot be less than the minimum penalty of 10 UVT (COP 523,740 in 2026) for late filing, and "
      "that for a corrective return the minimum is 10 UVT of the year in which the ORIGINAL return "
      "was filed.",
      "N", "-", R_F350, "N", "Amount", "Per event", "", RA, "system"),
    F("Total withholding plus penalties", "Total retenciones mas sanciones", "Totales", "138", "Y", "",
      "Hoja 1, casilla 138", "12", "N (whole pesos, nearest 1,000)", "617000", "(system total)",
      "Casilla 136 plus casilla 137. This is the amount that must be PAID IN FULL: a withholding "
      "return filed without full payment produces NO legal effect, with no administrative act "
      "needed to say so (ET art. 580-1, quoted in the instructivo).",
      "N", "-", R_F350, "N", "Amount", "Monthly", "", RA, "system"),
    F("Signatory identification", "No. Identificacion signatario", "Firmas", "139", "Y", "",
      "Hoja 1, casilla 139", "Var", "N", "79123456", "Company.Legal_Rep_ID",
      "NIT assigned by DIAN to the person signing the return - the legal representative or an "
      "authorised agent.",
      "Y", "-", R_NONE, "N", "Identifier", "Monthly", "", RA, "payroll"),
    F("Signatory verification digit", "DV signatario", "Firmas", "140", "Y", "",
      "Hoja 1, casilla 140", "1", "N", "3", "Company.Legal_Rep_ID_DV",
      "Verification digit of the signatory's NIT.",
      "Y", "-", R_NONE, "N", "Identifier", "Monthly", "", RA, "payroll"),
    F("Total payment", "Pago total", "Firmas", "980", "Y", "",
      "Hoja 1, casilla 980", "12", "N (whole pesos)", "617000", "Mercans.Payment_Amount",
      "The amount actually paid with the return. Reserved-range casilla. Must equal casilla 138 for "
      "the return to have legal effect.",
      "N", "-", R_F350, "N", "Amount", "Monthly", "", RA, "system"),
    F("Representation code", "Cod. Representacion", "Firmas", "981", "Y", "",
      "Hoja 1, casilla 981", "2", "N (code)", "01", "Mercans.Representation_Code",
      "Type of representation of the person signing for the declarant, taken from casilla 98 of the "
      "RUT.",
      "N", "-> Sheet 6: Codigo de representacion", R_NONE, "N", "Code", "Monthly", "", RA, "system"),
    F("Accountant or statutory auditor code", "Codigo Contador o Revisor Fiscal", "Firmas", "982", "C",
      "Populated where the return must be signed by an accountant or a statutory auditor. "
      "Bidirectional set with 'Professional card number' (casilla 983) and 'With qualifications' "
      "(casilla 994): where 982 is populated, 983 is mandatory and 994 becomes available.",
      "Hoja 1, casilla 982", "1", "N (code)", "2", "Mercans.Accountant_Type",
      "1 = Contador, 2 = Revisor fiscal. The instructivo sets the thresholds: an accountant must "
      "sign where the taxpayer keeps books and gross assets at the preceding year end exceeded "
      "100,000 UVT; a statutory auditor must sign for joint-stock companies, for companies whose "
      "gross assets reach 5,000 SMMLV, and for companies whose gross income reaches 3,000 SMMLV.",
      "N", "-> Sheet 6: Contador o revisor fiscal", R_NONE, "N", "Code", "Monthly", "", RA, "system"),
    F("Professional card number", "No. Tarjeta profesional", "Firmas", "983", "C",
      "Mandatory where 'Accountant or statutory auditor code' (casilla 982) is populated; blank "
      "otherwise. Bidirectional pair with casilla 982.",
      "Hoja 1, casilla 983", "Var", "A", "123456-T", "Mercans.Accountant_Card_Number",
      "Professional card number issued by the Junta Central de Contadores.",
      "N", "-", R_NONE, "N", "Identifier", "Monthly", "", RA, "system"),
    F("With qualifications", "Con salvedades", "Firmas", "994", "C",
      "Available only where 'Accountant or statutory auditor code' (casilla 982) is populated. "
      "Bidirectional pair with casilla 982.",
      "Hoja 1, casilla 994", "1", "Flag (x)", "-", "Mercans.Signed_With_Qualifications",
      "Marked with an x where the accountant or statutory auditor signs with qualifications.",
      "N", "-", R_NONE, "N", "Flag", "Monthly", "", RA, "system"),
    F("Collecting-entity stamp", "Espacio exclusivo para el sello de la entidad recaudadora",
      "Firmas", "997", "N", "",
      "Hoja 1, casilla 997", "-", "Display-only", "-", "(not an input)",
      "DISPLAY-ONLY. Reserved for the collecting bank's stamp on a paper receipt. It is not a data "
      "field, is not keyed and is not transmitted; it exists on the printed representation only.",
      "N", "-", R_NONE, "N", "Text", "Monthly", "", RA, "na"),
]

CFG = {
    "doc_id": "CO-DIAN-002",
    "filing_id": "CO-DIAN-F350-MONTHLY-002",
    "name_en": "Monthly Withholding Tax Return - Form 350",
    "name_es": "Formulario 350 - Declaracion de retenciones en la fuente",
    "spec_sheet": "Formulario 350 Spec",
    "authority_full": "Direccion de Impuestos y Aduanas Nacionales (DIAN)",
    "frequency": "Monthly. NOT required for a period in which no operation subject to withholding "
                 "occurred (ET art. 606 par. 2).",
    "due_date": "Between the 7th and the 16th BUSINESS DAY of the month following the period, by the "
                "LAST DIGIT of the employer NIT (DUR 1625 de 2016 art. 1.6.1.13.2.33 as set by "
                "Decreto 2229 de 2023). A return filed without full payment produces NO legal effect "
                "(ET art. 580-1).",
    "submission": "PORTAL ROUND-TRIP. Prepared and filed through the DIAN Servicios Informaticos "
                  "Electronicos (Muisca), www.dian.gov.co, signed with the Instrumento de Firma "
                  "Electronica (IFE). Res. DIAN 000227 de 2025 art. 1.2.2.26 par. 1 makes electronic "
                  "filing compulsory and states that DIAN 'pondra a disposicion el Formulario numero "
                  "350 en forma virtual en la pagina web'.",
    "file_format": "Online portal form (Servicio Informatico de Diligenciamiento), 155 casillas over "
                   "two hojas plus the 980-997 reserved signature block. NOT an XML or file-upload "
                   "submission: there is no published XSD or import layout for Form 350. Amounts in "
                   "whole pesos rounded to the nearest 1,000 (ET art. 577).",
    "legal_basis": "Resolucion DIAN 000031 de 29 de febrero de 2024 (form prescribed, in force from "
                   "1 August 2024), compiled at art. 1.2.2.26 de la Resolucion DIAN 000227 de 23 de "
                   "septiembre de 2025; ET arts. 365, 368, 383, 385, 386, 387, 387-1, 388, 401, "
                   "408-415, 437-2, 577, 580-1, 606; DUR 1625 de 2016 arts. 1.2.6.6, 1.2.6.8, "
                   "1.6.1.13.2.33 (as set by Decreto 2229 de 2023); Ley 2010 de 2019 art. 42; "
                   "Ley 2277 de 2022 art. 8; DIAN Concepto 011108 de 29 de junio de 2026.",
    "accuracy": "92% (PRIMARY SOURCE for the form itself). Every casilla number, label and "
                "arithmetic rule is read off the official form design and instructivo at "
                "00-official-sources/pdfs/Formulario_350_01082024.pdf, including the full casilla-130 "
                "summation and the hoja-2 annex mechanics. The 8% reservation is: (a) DIAN publishes "
                "no import schema for Form 350, so the mapping from payroll into the portal is a "
                "keying or robotic-process step whose exact screen behaviour is client-specific; "
                "(b) Res. 000227 de 2025 art. 1.2.2.26 par. 3 cites a hoja-2 'Casilla 91 Concepto de "
                "pago' and option codes that do not exist on the currently prescribed form (the "
                "concepto de pago is casilla 142) - an unresolved conflict in the official sources, "
                "escalated in column T; (c) the boundary between casilla 77/93 (rentas de trabajo) "
                "and casilla 79/95 (honorarios to natural persons) for a natural person taxed under "
                "the art. 383 table is a client-specific classification decision. It would rise to "
                "98% with a DIAN clarification on point (b) and a client-agreed classification "
                "boundary on point (c).",
    "source_status": "PRIMARY. Formulario_350_01082024.pdf - the prescribed form design (hoja 1 and "
                     "hoja 2) plus the complete four-page instructivo and the hoja-2 annex "
                     "instructivo. Extracted to _txt/form350.txt. Casilla numbers are read off the "
                     "form, never derived. Res. DIAN 000031 de 2024 and the compiling Res. 000227 de "
                     "2025 art. 1.2.2.26 are also held locally.",
    "channel_notes": [
        "Channel: online_form | Portal: DIAN Servicios Informaticos Electronicos (Muisca), "
        "www.dian.gov.co | Source: Res. DIAN 000227 de 2025 art. 1.2.2.26 par. 1 and the form's own "
        "instructivo, which repeatedly refers to 'el SI de Diligenciamiento' computing casillas "
        "automatically | CONFIRMED.",
        "This is a PORTAL ROUND-TRIP, not machine-to-machine. Do not model it on the nomina "
        "electronica: DIAN publishes no XSD, no cahier des charges and no import template for "
        "Form 350. The engine's deliverable is a reconciled casilla-value set, not a file.",
        "The DIAN service computes several casillas itself - 55, 56, 57, 58, 109, 110, 111, 112 from "
        "the hoja-2 annex; 130, 134, 136 and 138 as totals; 147 as 145 x 146; and 28 from 27. "
        "Payroll must not attempt to supply those.",
        "Signature is by the Instrumento de Firma Electronica (IFE) authorised by DIAN - an "
        "authenticated portal credential, not an X.509 document signature as in the nomina "
        "electronica.",
        "The tax portal is NOT the social-security channel. PILA is filed through a licensed private "
        "operador de informacion and never touches Muisca.",
    ],
    "integration_notes": [
        "integration_type = OUTBOUND (scope_manifest CO-OUT-F350). There is no inbound file: the "
        "portal returns an on-screen acknowledgement and a form number (casilla 4), which the engine "
        "should capture for the audit trail and for any later corrective return (casilla 26).",
        "product_mapping_required = true. The engine must accumulate withholding BY COUNTERPARTY "
        "TYPE - natural person versus legal person - and, within natural persons, must separate "
        "resident employment income (casillas 77 / 93) from payments to non-residents (the hoja-2 "
        "annex). The 2024 redesign introduced that separation; the pre-2024 form did not have it.",
        "Payroll owns four casillas directly - 77, 93 and, for non-residents, the hoja-2 rows that "
        "roll into 109 / 111 or 110 / 112 - plus casilla 129 where a prior over-withholding is "
        "reversed. Everything else on the form comes from accounts payable or the tax function.",
    ],
    "b1_notes": [
        "RESIDENT employees are reported on HOJA 1: the depurated ET art. 388 base in casilla 77 and "
        "the withholding under the art. 383 progressive table in casilla 93.",
        "NON-RESIDENT employees are reported on HOJA 2 and roll up to casillas 109 / 111 (no treaty) "
        "or 110 / 112 (treaty). The base in casilla 145 is the GROSS payment, because ET art. 408 "
        "admits no depuration, and the rate in casilla 146 is 20%.",
        "The hoja-2 concepto de pago (casilla 142) for a non-resident employee is concepto 5, "
        "'Prestaciones de servicios y compensacion por servicios personales', for a non-treaty "
        "country, and concepto 24, 'Rentas de trabajo', for a treaty country. Concepto 24's own "
        "definition on the form is 'rentas de trabajo de cualquier naturaleza EN RELACION CON UN "
        "EMPLEO a favor de personas naturales no residentes' - it is unambiguously the employee "
        "concept.",
        "The same employee therefore MOVES BETWEEN SHEETS during the year when residence is "
        "acquired: hoja 2 while non-resident, hoja 1 from the payment following the date the "
        "183-day test is met. The switch is prospective only; the earlier months are not restated "
        "(DIAN Concepto 011108 of 29 June 2026).",
        "Directors' fees to a non-resident go to concepto 25 (Honorarios de directores) and "
        "employer-paid pensions to concepto 27 (Pensiones) - neither is the employee concept, and "
        "mis-selecting them changes the treaty article applied.",
    ],
    "related": [
        "Casilla 93 must reconcile to the sum of RetencionFuente (NIE177) across every nomina "
        "electronica document for the same month - CO-DIAN-001 - after the nearest-1,000 rounding.",
        "Casilla 27 (art. 114-1 exonerated self-withholder) rests on the SAME exoneration test as "
        "PILA archivo tipo 1 field 33 and Registro Tipo 2 field 76 - CO-PILA-003.",
        "The twelve monthly casilla-93 figures do NOT produce Formulario 220. Colombia imposes no "
        "employer year-end reconciliation; Formulario 220 (CO-DIAN-004) is a SEPARATE per-employee "
        "obligation built from the annual accumulation, not from the monthly returns.",
        "Casilla 77 is an AGGREGATE base; the per-employee detail behind it is reported annually in "
        "Formato 2276 (CO-DIAN-005), which is why the two cannot be derived from one another.",
        "Formulario 350 aggregates every withholding the employer makes, including on supplier "
        "payments and VAT. Payroll is one contributor among several; the return is owned by the "
        "client's tax function.",
    ],
    "scope": (SCOPE_WHO + [
        "AMOUNTS AND CALCULATIONS",
        ("Depurated taxable base of resident employees", "YES",
         "Casilla 77. The ET art. 388 base after non-constitutive income, art. 387 deductions and "
         "the 25% exempt income - NOT the gross."),
        ("Withholding on resident employees", "YES",
         "Casilla 93. The art. 383 progressive table result, approximated to the nearest 1,000."),
        ("Gross payments to non-resident employees", "YES",
         "Hoja 2 casilla 145, rolling up to casilla 109 or 110. The GROSS, because art. 408 admits "
         "no depuration."),
        ("Withholding on non-resident employees", "YES",
         "Hoja 2 casilla 147, rolling up to casilla 111 or 112. The flat 20% of art. 408, or the "
         "treaty rate."),
        ("Employer-paid pension income above 1,000 UVT", "YES",
         "Casillas 78 / 94, where the employer itself pays a pension."),
        ("Reversal of excess or undue withholding", "YES",
         "Casilla 129, where an employee's withholding is corrected downward in a later month."),
        ("Employer social-security contributions", "NO",
         "Not a withholding. Reported on PILA. Formulario 350 is a TAX return only."),
        ("Employee social-security contributions", "NO",
         "Not a withholding by the employer in the ET sense. They reduce the casilla-77 base as "
         "non-constitutive income, but are never declared as a retencion."),
        ("Payments in the 0% band of the art. 383 table", "PARTIAL",
         "The payment IS included in the casilla-77 base; the withholding in casilla 93 is simply "
         "nil for that employee. Do not exclude the base."),
        ("Withholding on supplier and contractor payments", "NO",
         "Present on the form (casillas 29-54, 79-92, 95-108) but not produced by payroll. Owned by "
         "the client's accounts-payable function."),
        ("VAT and stamp-duty withholding", "NO",
         "Casillas 131-135. Owned by the client's tax function."),
    ] + SCOPE_TIMING + [
        "SPECIAL CASES",
        ("A month in which no withholding was practised", "NO",
         "ET art. 606 par. 2: the return is NOT obligatory for a period with no operation subject to "
         "withholding. This is unusual among Colombian filings - the nomina electronica and PILA do "
         "not have an equivalent exemption."),
        ("Employee whose withholding is nil because the base is in the 0% band", "YES",
         "The BASE still goes in casilla 77. Only the withholding is nil."),
        ("Employee who acquires tax residence mid-year", "YES",
         "Reported on hoja 2 for the months before residence and on hoja 1 from the payment "
         "following the date the 183-day test is met. Prospective only - the earlier months are "
         "never restated."),
        ("Non-resident whose work is performed entirely outside Colombia", "NO",
         "Foreign-source income, not taxable in Colombia, no withholding and nothing to declare "
         "(DIAN Oficio 28380 of 2019)."),
        ("Filing the return without paying it", "NO",
         "ET art. 580-1: a withholding return filed without full payment produces NO legal effect, "
         "with no administrative act required. Casilla 980 must equal casilla 138."),
        ("Correcting a filed return", "YES",
         "By a corrective return carrying casilla 25 (correction code) and casilla 26 (the form "
         "number being corrected). The minimum penalty is 10 UVT of the year the ORIGINAL return "
         "was filed."),
    ]),
    "fields": FIELDS,
}
