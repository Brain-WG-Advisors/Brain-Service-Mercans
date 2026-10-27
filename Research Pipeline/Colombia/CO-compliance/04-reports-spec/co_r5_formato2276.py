# -*- coding: utf-8 -*-
"""
CO-DIAN-005 - Formato 2276 version 4, Informacion de ingresos y retenciones por
rentas de trabajo y de pensiones (informacion exogena).
Filing ID: CO-DIAN-EXO2276-ANNUAL-005.

THE THIRTY-SIX NUMERALS, the Entidad Informante code table and paragraphs 1 to 7
are transcribed VERBATIM from the OFFICIAL source held at
  00-official-sources/pdfs/Resolucion 000227 de 23-09-2025.pdf
(Resolucion Unica en Materia Tributaria, Aduanera y Cambiaria de la DIAN),
Articulo 1.3.7.1.1, and the filing calendar from Articulo 1.3.9.1.3.
Extraction artefact: _txt/res227.txt.

SOURCE LIMIT, STATED PLAINLY: Res. 227 art. 1.3.7.1.1 prescribes WHAT must be
reported ("de acuerdo con los parametros establecidos en las especificaciones
tecnicas del Formato 2276 Version 4") but the XML tag names, field ordering and
column lengths live in a SEPARATE technical-specification annex that DIAN
publishes alongside the format and which is NOT in the local source registry.
Field identifiers in this Spec are therefore the RESOLUTION'S OWN NUMERALS -
authoritative for content - while the XML element names are marked DERIVED and
must be confirmed against the published especificaciones tecnicas before any
productive layout is configured.

C19 code pattern: ^N(0[1-9]|[12][0-9]|3[0-6])$ where the numeric part is the
numeral in art. 1.3.7.1.1. Nothing is invented.
"""

from build_co_specs import (R_2276, R_NONE, RA)
from co_scope_common import SCOPE_WHO, SCOPE_TIMING

DERIVED_XML = ("DERIVED - the XML element name is not published in Res. 227; confirm against the "
               "DIAN especificaciones tecnicas for Formato 2276 v4.")


def F(en, es, rec, pos, mand, cond, xpath, length, fmt, ex, mapping, expl,
      rel, opts, rnd, neg, vt, freq, q, ra, kind):
    return [en, es, rec, pos, "", mand, cond, xpath, length, fmt, ex, mapping,
            expl, rel, opts, rnd, neg, vt, freq, q, ra, kind]


def N(num, en, es, ex, mapping, expl, mand="Y", cond="", opts="-", kind="payroll",
      vt="Amount", rnd=R_2276, rec="Valores", q="", length="14", fmt=None):
    """Formato 2276 numeral helper."""
    return F(en, es, rec, "N%02d" % num, mand, cond,
             "Numeral %d, art. 1.3.7.1.1 (XML element DERIVED)" % num, length,
             fmt or "N (whole pesos, no decimals, no separators; zero when nil)", ex, mapping, expl,
             "Y" if kind == "payroll" else "N", opts, rnd, "N", vt, "Annual",
             q or DERIVED_XML, RA, kind)


FIELDS = [
    "REPORTING ENTITY AND BENEFICIARY (numerals 1 to 4)",
    N(1, "Reporting entity concept", "Entidad informante", "1", "Mercans.Informante_Concept",
      "A CODE, not a name. Res. 227 art. 1.3.7.1.1 par. 3 prints the eight-value table: "
      "1 Informante general, 2 Fiduciarias, 3 Mandatario y/o Administrador delegado, 4 Consorcio "
      "y/o Union Temporal, 5 Exploracion y Explotacion de hidrocarburos, gases y minerales, "
      "6 Joint Venture, 7 Gestor en Cuentas en Participacion, 8 Convenios de cooperacion con "
      "entidades publicas. Par. 4 is categorical for payroll: 'cuando el empleador reporte pagos "
      "o abonos en cuenta por concepto de rentas de trabajo y de pensiones, la casilla Entidad "
      "Informante se debe diligenciar con el concepto 1 - Informante general', and the fideicomiso "
      "and contract-participant fields are then NOT filled.",
      opts="-> Sheet 6: Entidad informante", vt="Code", rec="Entidad informante",
      length="1", fmt="N (code 1 to 8)"),
    N(2, "Beneficiary document type and identification number",
      "Tipo de documento y numero de identificacion del beneficiario", "13 / 1020304050",
      "Employee.Document_Type + Employee.Document_Number",
      "COMPOSITE FIELD as drafted in the resolution - numeral 2 names BOTH the document type and "
      "the number in a single numeral, and the technical specification splits them into two columns. "
      "Sub-field 1 = the identity-document type code; sub-field 2 = the identification number "
      "without dots or hyphens. PERSISTENCE: this pair is the join key across every Colombian "
      "artefact for the employee - nomina electronica NIE044 / NIE045, PILA Registro Tipo 2 campos "
      "3 and 4, Formulario 220 casillas 24 and 25.",
      vt="Identifier", rec="Beneficiario", length="2 + 16", fmt="N (code) + AN (number)",
      rnd=R_NONE),
    N(3, "Beneficiary surnames and names", "Apellidos y nombres del beneficiario",
      "PEREZ GOMEZ JUAN CARLOS", "Employee.First_Surname + Second_Surname + First_Name + Other_Names",
      "COMPOSITE FIELD. The resolution names one numeral; the technical specification splits it "
      "into four columns - primer apellido, segundo apellido, primer nombre, otros nombres - in "
      "the same order as every other DIAN artefact. Sub-field order matters: DIAN matches on the "
      "surname columns.",
      vt="Text", rec="Beneficiario", length="60 x 4", fmt="A", rnd=R_NONE),
    N(4, "Beneficiary location", "Ubicacion del beneficiario", "11 / 001",
      "Employee.Department_Code + Employee.Municipality_Code",
      "COMPOSITE FIELD - department and municipality of the beneficiary, on the DANE DIVIPOLA "
      "catalogue. Note that this is the BENEFICIARY's location, not the place of work reported in "
      "the nomina electronica (NIE051 / NIE052) nor the place where the withholding was practised "
      "reported in Formulario 220 (casillas 34 / 35). Three artefacts, three different geographic "
      "questions.",
      opts="-> Sheet 6: DIVIPOLA (DANE)", vt="Code", rec="Beneficiario",
      length="2 + 3", fmt="N (DIVIPOLA)", rnd=R_NONE),

    "WORK INCOME PAID (numerals 5 to 17)",
    N(5, "Salary payments", "Pagos por salarios", "144000000", "SUM(Payroll.Salary_Payments)",
      "Annual salary payments to the employee. Maps to Formulario 220 casilla 36 and must equal it "
      "for the same employee and year."),
    N(6, "Ecclesiastical emolument payments", "Pagos por emolumentos eclesiasticos", "0",
      "SUM(Payroll.Ecclesiastical_Emoluments)",
      "A SEPARATE NUMERAL HERE, with no counterpart casilla on Formulario 220 - Form 220 folds "
      "ecclesiastical emoluments into casilla 39 (honorarios). Payments in money or in kind, direct "
      "or indirect, compensating the personal service of a minister of religion, whatever the "
      "denomination and whatever the creed.",
      mand="C",
      cond="Populated only where the employer paid ecclesiastical emoluments. Distinct from "
           "'Fee payments' (numeral 9) even though Formulario 220 combines the two."),
    N(7, "Payments made with vouchers, cheques, cards or vales",
      "Pagos realizados con bonos electronicos o de papel de servicio, cheques, tarjetas, vales, "
      "etc.", "0", "SUM(Payroll.Voucher_Payments)",
      "Payments in vouchers, cheques, cards or vales. Res. 227 art. 1.3.7.1.1 par. 6 imposes a HARD "
      "EXCLUSION: 'El valor reportado en el numeral 7 NO DEBE CONTENER la informacion reportada en "
      "los demas numerales del Formato 2276'. It is a residual concept, and double-reporting it "
      "against numerals 5, 8 or 17 is a validation failure.",
      mand="C",
      cond="Populated where such payments were made AND the amount is not already reported under "
           "any other numeral (par. 6). Bidirectional exclusion with every other numeral of the "
           "format."),
    N(8, "Excess meal payments over 41 UVT (ET art. 387-1)",
      "Valor del exceso de los pagos por alimentacion mensuales mayores a 41 UVT, articulo 387-1 "
      "E.T.", "0", "SUM(Payroll.Meal_Excess_41UVT)",
      "The EXCESS over 41 UVT per month (COP 2,147,334 in 2026) of employer payments to third "
      "parties for the employee's or their family's meals. Taxable income of the employee. "
      "BIDIRECTIONAL PAIR WITH NUMERAL 32, which carries the amount UP TO 41 UVT and is "
      "informative only - the same underlying payment is split across two numerals at the 41-UVT "
      "line, and the engine must maintain that split monthly.",
      mand="C",
      cond="Populated only where monthly meal payments to a third party exceed 41 UVT. Bidirectional "
           "pair with numeral 32 (the amount up to 41 UVT). The whole benefit is unavailable where "
           "the employee's monthly salary exceeds 310 UVT, in which case the payment falls to "
           "numeral 7 instead.",
      opts="-> Sheet 6: Umbrales UVT 2026"),
    N(9, "Fee payments", "Pagos por honorarios", "0", "SUM(Payroll.Honorarios)",
      "Fees paid to a natural person. Res. 227 par. 5 is the governing rule: payments to natural "
      "persons receiving work income NOT arising from an employment, legal or statutory "
      "relationship, but subject to withholding under ET art. 383, ARE reported in Formato 2276. "
      "Where such a payment is NOT subject to art. 383 withholding, it is reported instead in the "
      "ordinary payments-and-withholdings formats.",
      mand="C",
      cond="Populated where fees were paid AND the payment was withheld under ET art. 383 "
           "(art. 383 par. 2, added by Ley 2277 de 2022 art. 8). Where art. 383 did not apply, the "
           "payment belongs in a different format, not here."),
    N(10, "Service payments", "Pagos por servicios", "0", "SUM(Payroll.Servicios)",
      "Service payments to a natural person, subject to the same par. 5 test as numeral 9.",
      mand="C", cond="Populated where services were paid AND withheld under ET art. 383."),
    N(11, "Commission payments", "Pagos por comisiones", "0", "SUM(Payroll.Comisiones)",
      "Commissions to a natural person, subject to the same par. 5 test. Commissions paid UNDER an "
      "employment contract are salary under CST art. 127 and belong in numeral 5.",
      mand="C",
      cond="Populated where non-employment commissions were paid AND withheld under ET art. 383. "
           "Mutually exclusive with numeral 5 for the same amount."),
    N(12, "Statutory benefit payments", "Pagos por prestaciones sociales", "12000000",
      "SUM(Payroll.Prestaciones_Sociales)",
      "Statutory benefits OTHER THAN severance and its interest, which have their own three "
      "numerals (18, 19, 20). Prima de servicios, vacation pay and dotaciones. Maps to Formulario "
      "220 casilla 42."),
    N(13, "Per diem payments", "Pagos por viaticos", "0", "SUM(Payroll.Viaticos)",
      "Per diems for transport, subsistence and accommodation away from the habitual workplace. "
      "Maps to Formulario 220 casilla 43.",
      mand="C", cond="Populated where per diems were paid in the year."),
    N(14, "Representation expense payments", "Pagos por gastos de representacion", "0",
      "SUM(Payroll.Gastos_Representacion)",
      "Representation expenses. Maps to Formulario 220 casilla 44.",
      mand="C", cond="Populated where representation expenses were paid in the year."),
    N(15, "Cooperative associated-work compensation",
      "Pagos por compensaciones por el trabajo asociado cooperativo", "0",
      "SUM(Payroll.Coop_Compensation)",
      "Compensation for associated cooperative work. Applies only to a member of an associated-work "
      "cooperative - PILA contributor type 31 and nomina electronica TipoTrabajador 31. Maps to "
      "Formulario 220 casilla 45.",
      mand="C", cond="Populated only for a member of an associated-work cooperative."),
    N(16, "Non-reimbursable educational support financed with public funds",
      "Valor apoyos economicos no reembolsables o condonados, entregados por el Estado o "
      "financiados con recursos publicos, para financiar programas educativos", "0",
      "SUM(Payroll.Educational_Support)",
      "Non-reimbursable or forgiven educational support from the State or financed with public "
      "funds. Res. 227 par. 7 draws the line by WHO ADMINISTERS IT: where the EMPLOYER pays it "
      "directly it is reported here; where a THIRD PARTY administers it, it is reported in Formato "
      "5247 under concepto 5102 instead. Par. 7 was added by Resolucion 188 de 2024 art. 8 and, "
      "under par. 5 of art. 1.3.9.1.3, first applies to tax year 2025, filed in calendar 2026.",
      mand="C",
      cond="Populated only where the employer paid the support DIRECTLY. Where a third party "
           "administers it, report Formato 5247 concepto 5102 and leave this numeral nil - the two "
           "are mutually exclusive for the same payment."),
    N(17, "Other payments", "Otros pagos", "0", "SUM(Payroll.Other_Work_Payments)",
      "Work-income payments with no dedicated numeral. Note the interaction with par. 6: numeral 7 "
      "must not repeat anything reported here.",
      mand="C", cond="Populated where a work-income payment has no dedicated numeral."),

    "THE THREE SEVERANCE LINES (numerals 18, 19, 20) - ORDER DIFFERS FROM FORM 220",
    N(18, "Severance and interest actually paid to the employee",
      "Cesantias e intereses de cesantias efectivamente pagadas al empleado", "1440000",
      "Payroll.Cesantias_Paid_To_Employee",
      "THE FIRST OF THREE SEVERANCE NUMERALS. Amounts ACTUALLY PAID to the employee - the January "
      "interest payment, an authorised partial withdrawal, or a termination settlement. Maps to "
      "Formulario 220 casilla 47.",
      opts="-> Sheet 6: Las tres lineas de cesantias"),
    N(19, "Severance deposited to the severance fund",
      "Cesantias consignadas al fondo de cesantias", "12000000",
      "Payroll.Cesantias_Deposited_To_Fund",
      "THE SECOND OF THREE. The amount DEPOSITED to the employee's chosen fund by 14 February "
      "under Ley 50 de 1990 art. 99. MAPS TO FORMULARIO 220 CASILLA 49 - NOT casilla 48. The "
      "second and third severance lines are TRANSPOSED between the two artefacts, and a positional "
      "mapping swaps them.",
      mand="C",
      cond="Populated for an employee under the Ley 50 de 1990 regime. Mutually exclusive with "
           "'Severance under the traditional CST regime' (numeral 20) for the same employee. Must "
           "reconcile to the deposit made under CO-CESANTIAS-006.",
      opts="-> Sheet 6: Las tres lineas de cesantias"),
    N(20, "Severance recognised under the traditional CST regime",
      "Auxilio de cesantias reconocido a trabajadores del regimen tradicional del Codigo Sustantivo "
      "del Trabajo, contenido en el Capitulo VII, Titulo VIII Parte Primera", "0",
      "Payroll.Cesantias_Traditional_Regime",
      "THE THIRD OF THREE. Severance RECOGNISED under the pre-1991 retroactive regime, for "
      "employees hired before 1 January 1991 who did not elect the Ley 50 de 1990 regime. MAPS TO "
      "FORMULARIO 220 CASILLA 48 - NOT casilla 49.",
      mand="C",
      cond="Populated only for an employee under the pre-1991 traditional regime. Mutually "
           "exclusive with 'Severance deposited to the fund' (numeral 19) for the same employee.",
      opts="-> Sheet 6: Las tres lineas de cesantias"),

    "PENSIONS AND TOTAL (numerals 21, 22)",
    N(21, "Retirement, old-age or invalidity pensions",
      "Pensiones de jubilacion, vejez o invalidez", "0", "SUM(Payroll.Pension_Payments)",
      "Pension income paid BY THE EMPLOYER. Taxable only above 1,000 UVT per month "
      "(COP 52,374,000 in 2026) under ET art. 206 num. 5. Nil for ordinary corporate payroll, where "
      "the paying fund is the withholding agent and the reporting party.",
      mand="C", cond="Populated only where the employer itself paid a pension."),
    N(22, "Total gross income from work or pension payments",
      "Total ingresos brutos por pagos de rentas de trabajo o pensiones", "157440000",
      "SUM(numerals 5 to 21)",
      "The gross total. Maps to Formulario 220 casilla 52 and must equal it for the same employee "
      "and year. Note that numeral 32 (meal payments up to 41 UVT) is INFORMATIVE and does NOT "
      "enter this total - par. 1 says so expressly.",
      kind="system"),

    "EMPLOYEE CONTRIBUTIONS AND VOLUNTARY SAVINGS (numerals 23 to 28)",
    N(23, "Mandatory health contributions borne by the employee",
      "Aportes obligatorios por salud a cargo del trabajador", "5760000",
      "SUM(Payroll.Health_Employee_Contribution)",
      "The employee's own mandatory health contributions actually deducted. Maps to Formulario 220 "
      "casilla 53 and must reconcile to twelve months of nomina electronica NIE163 and to the "
      "employee portion of PILA Registro Tipo 2 campo 55."),
    N(24, "Mandatory pension and solidarity-fund contributions borne by the employee",
      "Aportes obligatorios a fondos de pensiones y solidaridad pensional a cargo del trabajador",
      "7200000", "SUM(Payroll.Pension_Employee + Payroll.FSP)",
      "Pension AND the solidarity-fund surcharge in ONE numeral, exactly as Formulario 220 casilla "
      "54 combines them. The nomina electronica and PILA both keep them separate, so the engine "
      "must sum only at this point."),
    N(25, "Voluntary contributions to the individual-account regime (RAIS)",
      "Aportes voluntarios al Regimen de Ahorro Individual con Solidaridad (RAIS)", "0",
      "SUM(Payroll.Voluntary_RAIS)",
      "Voluntary RAIS contributions under ET art. 55. DISTINCT from numeral 26. Maps to Formulario "
      "220 casilla 55.",
      mand="C",
      cond="Populated where the employee made voluntary RAIS contributions. Distinct from "
           "'Voluntary contributions to voluntary pension funds' (numeral 26) - different legal "
           "bases, and the nomina electronica cannot tell them apart (one element, NIE198)."),
    N(26, "Voluntary contributions to voluntary pension funds",
      "Aportes voluntarios a fondos de pensiones voluntarias", "0",
      "SUM(Payroll.Voluntary_Pension_Fund)",
      "Voluntary contributions under ET art. 126-1. Maps to Formulario 220 casilla 56.",
      mand="C",
      cond="Populated where the employee made voluntary pension-fund contributions. Distinct from "
           "numeral 25."),
    N(27, "AFC account contributions", "Aportes a cuentas AFC", "0", "SUM(Payroll.AFC)",
      "Ahorro para el Fomento de la Construccion. Maps to Formulario 220 casilla 57 and to nomina "
      "electronica NIE179.",
      mand="C", cond="Populated where AFC deductions were made."),
    N(28, "AVC account contributions", "Aportes a cuentas AVC", "0", "SUM(Payroll.AVC)",
      "Ahorro Voluntario Contractual with the Fondo Nacional del Ahorro. Maps to Formulario 220 "
      "casilla 58. The nomina electronica has NO dedicated element for AVC - it falls to "
      "OtraDeduccion (NIE197) - so the wage type must be tagged to recover the amount here.",
      mand="C", cond="Populated where AVC deductions to the FNA were made."),

    "WITHHOLDING AND VAT (numerals 29 to 31)",
    N(29, "Withholding on work or pension income",
      "Valor de las retenciones en la fuente por pagos de rentas de trabajo o pensiones", "7404000",
      "SUM(Payroll.Income_Tax_Withheld)",
      "THE PRINCIPAL WITHHOLDING NUMERAL. For a RESIDENT it is the ET art. 383 table result under "
      "Procedure 1 or 2; for a NON-RESIDENT it is the flat 20% of ET art. 408 on the gross. Maps "
      "to Formulario 220 casilla 60, and the sum across the population reconciles to twelve months "
      "of Formulario 350 casilla 93."),
    N(30, "VAT as a higher cost or expense",
      "Impuesto sobre las Ventas (IVA), mayor valor del costo o gasto", "0",
      "(client tax function)",
      "Non-deductible VAT treated as a higher cost or expense. Not a payroll figure; present in the "
      "format because Formato 2276 is a third-party information return covering all art. 383 work "
      "income, including payments to contractors.",
      mand="C", cond="Populated by the client's tax function where non-deductible VAT attached to "
                     "the payment. Payroll contributes nothing.",
      kind="na"),
    N(31, "VAT withholding", "Retencion en la fuente a titulo de Impuesto sobre las Ventas (IVA)",
      "0", "(client tax function)",
      "VAT withheld on the payment. Not a payroll figure - Colombian employment income carries no "
      "VAT. Relevant only where the beneficiary is a VAT-responsible contractor paid under the "
      "art. 383 table.",
      mand="C", cond="Populated by the client's tax function where VAT was withheld from the "
                     "payment. Payroll contributes nothing.",
      kind="na"),

    "INFORMATIVE AND SPECIAL NUMERALS (numerals 32 to 36)",
    N(32, "Monthly meal payments up to 41 UVT",
      "Pagos por alimentacion mensuales hasta 41 UVT", "0", "SUM(Payroll.Meal_Payment_Under_41UVT)",
      "INFORMATIVE ONLY. Res. 227 par. 1 says expressly: 'El valor a que hace referencia el numeral "
      "32 de este articulo SE CONSIDERA DE CARACTER INFORMATIVO y corresponde a lo dispuesto en el "
      "articulo 387-1 del Estatuto Tributario'. It therefore does NOT enter the gross total in "
      "numeral 22 - the amount is not income of the employee at all, but of the food supplier. "
      "BIDIRECTIONAL PAIR WITH NUMERAL 8, which carries the excess above 41 UVT. Formulario 220 "
      "has NO counterpart casilla for this amount.",
      mand="C",
      cond="Populated where the employer made meal payments to a third party for an employee whose "
           "monthly salary does not exceed 310 UVT. Bidirectional pair with numeral 8 (the excess). "
           "Where the salary exceeds 310 UVT the whole payment falls to numeral 7 and BOTH this "
           "numeral and numeral 8 stay nil.",
      opts="-> Sheet 6: Umbrales UVT 2026"),
    N(33, "Average labour income of the last six months",
      "Valor ingreso laboral promedio de los ultimos seis meses. Unicamente para trabajadores que "
      "aplique el numeral 4 articulo 206 E.T.", "13120000",
      "Payroll.Rolling_6M_Average_Labour_Income",
      "The rolling six-month average that drives the ET art. 206 num. 4 severance exemption and its "
      "taper - full exemption where it does not exceed 350 UVT (COP 18,330,900 per month in 2026). "
      "The resolution restricts it expressly: 'UNICAMENTE para trabajadores que aplique el numeral "
      "4 articulo 206 E.T.'. The engine must maintain the average YEAR-ROUND; it cannot be "
      "reconstructed from annual totals.",
      mand="C",
      cond="Populated ONLY for employees to whom ET art. 206 num. 4 applies - that is, where "
           "severance or its interest was paid or deposited. Bidirectional with numerals 18, 19 and "
           "20: a record carrying any of those three should carry this average.",
      opts="-> Sheet 6: Umbrales UVT 2026"),
    N(34, "Economic dependant document type and identification number",
      "Tipo de documento y numero de identificacion del dependiente economico", "13 / 1122334455",
      "Employee.Dependant_Document_Type + Employee.Dependant_Document_Number",
      "COMPOSITE FIELD - document type and number of the economic dependant claimed under ET "
      "art. 387 par. 2. Sub-field 1 = document type code; sub-field 2 = the number. THIS IS THE "
      "FIELD DIAN USES TO CROSS-CHECK a dependant claimed by more than one taxpayer, which is why "
      "it must agree with Formulario 220 casillas 79 and 80 exactly.",
      mand="C",
      cond="Populated only where the employee claimed the ET art. 387 par. 2 dependants deduction "
           "during the year. Bidirectional with Formulario 220 casillas 79 to 82, which carry the "
           "same dependant with the addition of the name and relationship.",
      vt="Identifier", rec="Beneficiario", length="2 + 16", fmt="N (code) + AN (number)",
      rnd=R_NONE),
    N(35, "Trust identification", "Identificacion del fideicomiso", "", "Mercans.Fideicomiso_ID",
      "Populated ONLY where the reporting entity concept (numeral 1) is 2 - Fiduciarias - because "
      "the work income was paid out of trust assets. Res. 227 par. 4 directs that for an ordinary "
      "employer reporting under concepto 1 this field 'no se debe diligenciar'.",
      mand="C",
      cond="MANDATORY where 'Reporting entity concept' (numeral 1) = 2 (Fiduciarias); MUST BE BLANK "
           "where numeral 1 = 1 (Informante general). Mutually exclusive with 'Contract participant "
           "document type and identification' (numeral 36). Bidirectional set with numeral 1.",
      vt="Identifier", rec="Entidad informante", length="Var", fmt="AN", rnd=R_NONE, kind="na"),
    N(36, "Contract participant document type and identification number",
      "Tipo documento e identificacion del participante en contrato", "",
      "Mercans.Contract_Participant_ID",
      "COMPOSITE FIELD, populated ONLY where the reporting entity concept (numeral 1) is a "
      "collaboration-contract concept - 3 Mandatario, 4 Consorcio o Union Temporal, 5 Exploracion y "
      "explotacion, 6 Joint Venture, 7 Gestor en Cuentas en Participacion, 8 Convenios de "
      "cooperacion. Res. 227 par. 4 directs that for concepto 1 it 'no se debe diligenciar', and "
      "that where a collaboration contract IS reported, the trust field (numeral 35) is left blank "
      "instead.",
      mand="C",
      cond="MANDATORY where 'Reporting entity concept' (numeral 1) is 3, 4, 5, 6, 7 or 8; MUST BE "
           "BLANK where numeral 1 = 1 or 2. Mutually exclusive with 'Trust identification' "
           "(numeral 35). Bidirectional set with numeral 1.",
      vt="Identifier", rec="Entidad informante", length="2 + 16", fmt="N (code) + AN (number)",
      rnd=R_NONE, kind="na"),

    "FILING CONTROL FIELDS (not numerals - envelope and deadline drivers)",
    F("Informant NIT", "NIT del informante", "Envelope", "ENV-01", "Y", "",
      "Envelope / file name (DERIVED)", "Var", "N", "900123456", "Company.NIT",
      "NIT of the reporting employer. Res. 227 art. 1.3.9.1.3 keys the DEADLINE to it: the LAST "
      "digit for a Gran Contribuyente, the LAST TWO digits for a legal or natural person. This is a "
      "third deadline rule, different again from Formulario 350 (last digit, 7th-16th business day) "
      "and PILA (last two digits, 2nd-16th business day).",
      "Y", "-> Sheet 6: Calendario de la exogena", R_NONE, "N", "Identifier", "Annual",
      DERIVED_XML, RA, "payroll"),
    F("Taxpayer category", "Calidad del informante", "Envelope", "ENV-02", "Y", "",
      "Envelope (DERIVED)", "Var", "Code", "Persona juridica", "Mercans.Taxpayer_Category",
      "Gran Contribuyente, persona juridica y asimilada, or persona natural y asimilada. Res. 227 "
      "art. 1.3.9.1.3 par. 1 fixes the point at which it is tested: 'de acuerdo con la calidad de "
      "Gran Contribuyente, persona juridica o persona natural QUE SE POSEA EN EL MOMENTO DE "
      "INFORMAR' - the status held at the moment of filing, not at the year end being reported.",
      "N", "-> Sheet 6: Calendario de la exogena", R_NONE, "N", "Code", "Annual",
      DERIVED_XML, RA, "system"),
    F("Tax year reported", "Ano gravable", "Envelope", "ENV-03", "Y", "",
      "Envelope (DERIVED)", "4", "N (AAAA)", "2026", "PayPeriod.Year",
      "The fiscal year whose payments are reported. Filed in May or June of the FOLLOWING calendar "
      "year.",
      "Y", "-", R_NONE, "N", "Date", "Annual", DERIVED_XML, RA, "system"),
    F("Format and version", "Formato y version", "Envelope", "ENV-04", "Y", "",
      "Envelope (DERIVED)", "Var", "Code", "2276 / 4", "Mercans.Exogena_Format_Version",
      "A CONSTANT for this filing: Formato 2276, version 4. Res. 227 art. 1.3.10.1 lists it in the "
      "formats-and-technical-specifications table as T3.45. A version mismatch is rejected at "
      "upload.",
      "N", "-> Sheet 6: Formato y version", R_NONE, "N", "Code", "Annual", DERIVED_XML, RA, "const"),
]


CFG = {
    "doc_id": "CO-DIAN-005",
    "filing_id": "CO-DIAN-EXO2276-ANNUAL-005",
    "name_en": "Third-party Information Return on Work and Pension Income - Format 2276 version 4",
    "name_es": "Formato 2276 version 4 - Informacion de ingresos y retenciones por rentas de "
               "trabajo y de pensiones (informacion exogena)",
    "spec_sheet": "Formato 2276 Spec",
    "authority_full": "Direccion de Impuestos y Aduanas Nacionales (DIAN)",
    "frequency": "Annual, one record per beneficiary per tax year.",
    "due_date": "May or June of the year following the fiscal year, by the LAST digit of the NIT for "
                "a Gran Contribuyente (17th business day of April to 8th business day of May) and "
                "by the LAST TWO digits for a legal or natural person (9th business day of May to "
                "9th business day of June). Res. DIAN 000227 de 2025 art. 1.3.9.1.3, which prints "
                "the full calendar - reproduced on Sheet 6.",
    "submission": "PORTAL ROUND-TRIP through the DIAN informacion exogena service at "
                  "www.dian.gov.co, using the Instrumento de Firma Electronica (IFE). The file is "
                  "prepared to the published especificaciones tecnicas for Formato 2276 version 4 "
                  "and uploaded; DIAN returns a validation outcome on screen.",
    "file_format": "XML prepared to the DIAN especificaciones tecnicas for Formato 2276 version 4 "
                   "(referenced at Res. 227 art. 1.3.10.1, table entry T3.45) and uploaded to the "
                   "informacion exogena service. FORMAT TO CONFIRM: the technical-specification "
                   "annex that fixes the XML element names, ordering and column lengths is NOT in "
                   "the local source registry - only the resolution that prescribes the CONTENT. "
                   "Amounts in whole pesos, zero-filled where nil (Res. 227 art. 1.3.7.1.1 par. 2).",
    "legal_basis": "Resolucion DIAN 000227 de 23 de septiembre de 2025 (Resolucion Unica en Materia "
                   "Tributaria, Aduanera y Cambiaria), arts. 1.3.7.1.1 (content), 1.3.9.1.3 "
                   "(deadlines) y 1.3.10.1 (formatos y especificaciones tecnicas), which compile "
                   "art. 51 de la Resolucion 162 de 2023 with par. 7 added by el art. 8 de la "
                   "Resolucion 188 de 2024; ET art. 631-3 (the enabling power), arts. 55, 126-1, "
                   "206 num. 4, 383 y su par. 2, 387 par. 2, 387-1, 408; Ley 2277 de 2022 art. 8; "
                   "Ley 50 de 1990 art. 99; Ley 52 de 1975 art. 1.",
    "accuracy": "85% (PRIMARY for content, DERIVED for layout). The THIRTY-SIX NUMERALS, the "
                "eight-value Entidad Informante code table, the seven paragraphs of interpretive "
                "rules and the complete filing calendar are transcribed VERBATIM from Res. DIAN "
                "000227 de 2025 arts. 1.3.7.1.1 and 1.3.9.1.3, held locally. What is NOT in the "
                "source registry is the separate especificaciones tecnicas annex that fixes the XML "
                "ELEMENT NAMES, field ordering and column lengths - the resolution only points to "
                "it. Every XML path in this Spec is therefore marked DERIVED in column T and must "
                "be confirmed before a productive layout is configured. Content coverage is "
                "effectively complete; layout coverage is not. It would rise to 97% with the "
                "published especificaciones tecnicas for Formato 2276 v4.",
    "source_status": "PRIMARY for content (Res. DIAN 000227 de 23 Sep 2025, art. 1.3.7.1.1 numerals "
                     "1-36 verbatim, pars. 1-7, and art. 1.3.9.1.3 calendar; extracted to "
                     "_txt/res227.txt). DERIVED for the XML layout - the especificaciones tecnicas "
                     "annex for Formato 2276 v4 is not held locally. C19 pattern "
                     "^N(0[1-9]|[12][0-9]|3[0-6])$ over the resolution's own numerals.",
    "channel_notes": [
        "Channel: file_upload (XML) into the DIAN informacion exogena service | Portal: "
        "www.dian.gov.co, Servicios Informaticos Electronicos, with the Instrumento de Firma "
        "Electronica (IFE) | Source: Res. DIAN 000227 de 2025 arts. 1.3.7.1.1 and 1.3.10.1 | "
        "CONFIRMED as to channel; FORMAT TO CONFIRM as to the XML schema.",
        "This is NOT machine-to-machine. Unlike the nomina electronica there is no SOAP service, no "
        "document signature and no synchronous ApplicationResponse - the employer uploads a file "
        "through an authenticated portal session and reads the outcome on screen.",
        "The word 'XML' is used here because Res. 227 art. 1.3.10.1 lists Formato 2276 among the "
        "formats with published especificaciones tecnicas, and the exogena service accepts XML. It "
        "is NOT used because an XSD has been cited - none is in the local registry. Column T marks "
        "every element path DERIVED accordingly.",
        "The tax portal is not the social-security channel and not the operador de informacion. "
        "Formato 2276 goes to DIAN; PILA never does.",
    ],
    "integration_notes": [
        "integration_type = OUTBOUND (scope_manifest CO-OUT-2276). No inbound file: the portal "
        "returns an on-screen validation outcome, which the engine should capture for the audit "
        "trail.",
        "product_mapping_required = true. The format needs three separate cesantias lines, the "
        "meal-payment split at the 41-UVT threshold across TWO numerals, the rolling six-month "
        "average labour income, the RAIS-versus-voluntary-pension split that the nomina electronica "
        "cannot make, the AVC amount that has no nomina electronica element at all, and each "
        "dependant's identity document. None of these is derivable at year end from annual totals.",
        "NOT DERIVABLE FROM THE MONTHLY FILINGS. It has its own field list, its own validation and "
        "its own deadline. It also carries concepts Formulario 220 does not - numeral 6 "
        "(ecclesiastical emoluments), numeral 32 (meal payments up to 41 UVT, informative) and "
        "numerals 30, 31, 35 and 36.",
    ],
    "b1_notes": [
        "RESIDENT: numeral 29 carries the ET art. 383 progressive-table withholding, and numerals "
        "23 to 28 carry the contributions and voluntary savings that depurated the base.",
        "NON-RESIDENT: numeral 29 carries the FLAT 20% of ET art. 408 on the GROSS. Numerals 23 and "
        "24 still report the contributions actually deducted, but they did NOT reduce the base - "
        "art. 408 admits no depuration. Numeral 33 is reported where severance was paid but has no "
        "effect, because the art. 206 num. 4 exemption belongs to the resident cedula-general "
        "regime.",
        "The format has NO residence field. Residence is therefore invisible to DIAN in this return "
        "except through the arithmetic relationship between numerals 22 and 29 - a non-resident's "
        "numeral 29 is close to exactly 20% of numeral 22, which is itself a useful internal "
        "control.",
        "Res. 227 par. 5 draws a SECOND distinction that is easy to confuse with residence: "
        "payments to natural persons receiving work income NOT from an employment relationship are "
        "reported HERE where they were withheld under ET art. 383, and in the ordinary "
        "payments-and-withholdings formats where they were not. That test is about the WITHHOLDING "
        "REGIME, not about residence.",
        "Where a non-resident's work was performed ENTIRELY outside Colombia the income is "
        "foreign-source, was not withheld, and is not reported here at all (DIAN Oficio 28380 of "
        "2019).",
    ],
    "related": [
        "Numerals 5 to 33 map almost one for one to Formulario 220 casillas 36 to 60 "
        "(CO-DIAN-004) - but THE SECOND AND THIRD SEVERANCE LINES ARE TRANSPOSED: numeral 19 is "
        "Form 220 casilla 49 and numeral 20 is casilla 48. Map by meaning, never by position.",
        "Numeral 29 summed across the population reconciles to twelve months of Formulario 350 "
        "casilla 93 (CO-DIAN-002), and per employee to twelve months of nomina electronica NIE177 "
        "(CO-DIAN-001).",
        "Numerals 23 and 24 reconcile to the employee portions of PILA Registro Tipo 2 campos 55, "
        "47, 51 and 52 (CO-PILA-003).",
        "Numeral 19 must reconcile to the deposit made under CO-CESANTIAS-006 by 14 February.",
        "Numeral 34 must agree with Formulario 220 casillas 79 and 80 - DIAN cross-checks a "
        "dependant claimed by more than one taxpayer.",
        "Numeral 16 is mutually exclusive with Formato 5247 concepto 5102 for the same payment "
        "(Res. 227 par. 7): employer-paid educational support is reported here, third-party "
        "administered support there. Formato 5247 is not a payroll filing.",
        "Numerals 30, 31, 35 and 36 are NOT payroll fields - VAT and collaboration-contract "
        "identifiers, owned by the client's tax function.",
    ],
    "scope": (SCOPE_WHO + [
        "AMOUNTS AND CALCULATIONS",
        ("Annual salary and work income by concept", "YES",
         "Numerals 5 to 17, itemised in thirteen separate concepts."),
        ("Ecclesiastical emoluments as a separate concept", "YES",
         "Numeral 6 - a concept Formulario 220 does NOT separate, folding it into casilla 39."),
        ("Meal payments up to 41 UVT", "YES, but informative only",
         "Numeral 32. Res. 227 par. 1: 'se considera de caracter informativo'. It does NOT enter "
         "the gross total in numeral 22, because it is income of the food supplier, not of the "
         "employee. Formulario 220 has no counterpart casilla."),
        ("Meal payments above 41 UVT", "YES",
         "Numeral 8, as taxable income of the employee."),
        ("Severance, split three ways", "YES",
         "Numerals 18 (paid to the employee), 19 (deposited to the fund) and 20 (traditional "
         "pre-1991 regime). Note the ordering difference against Formulario 220."),
        ("Employee mandatory contributions", "YES",
         "Numerals 23 and 24. Pension and the solidarity fund are COMBINED in numeral 24."),
        ("Voluntary savings, split four ways", "YES",
         "Numerals 25 (RAIS), 26 (voluntary pension funds), 27 (AFC) and 28 (AVC). The nomina "
         "electronica has one element for the first two and none for the fourth."),
        ("Rolling six-month average labour income", "YES",
         "Numeral 33, but ONLY for employees to whom ET art. 206 num. 4 applies."),
        ("Withholding practised", "YES",
         "Numeral 29, resident or non-resident alike."),
        ("Employer social-security contributions", "NO",
         "The return reports the BENEFICIARY's income and the BENEFICIARY's contributions. The "
         "employer's cost appears only on PILA."),
        ("VAT as a higher cost and VAT withholding", "NO",
         "Numerals 30 and 31 exist in the format but are not payroll figures - Colombian employment "
         "income carries no VAT. Owned by the client's tax function."),
        ("Trust and collaboration-contract identifiers", "NO",
         "Numerals 35 and 36. Res. 227 par. 4: for an ordinary employer reporting under concepto 1 "
         "they 'no se deben diligenciar'."),
    ] + SCOPE_TIMING + [
        "SPECIAL CASES",
        ("Employee who left during the year", "YES",
         "One record covering the payments actually made in the year. There is no partial-year "
         "marker; the amounts simply reflect the shorter period."),
        ("Employee whose withholding was nil", "YES",
         "A record is still required. Res. 227 par. 2: 'Las casillas de valores son de obligatorio "
         "diligenciamiento. En caso de no tener ningun valor, se deben diligenciar con cero (0)'."),
        ("Natural person paid work income OUTSIDE an employment relationship", "YES",
         "Res. 227 par. 5: reported here WHERE the payment was withheld under ET art. 383. Where "
         "art. 383 did not apply, it goes to the ordinary payments-and-withholdings formats "
         "instead - not here."),
        ("Work income paid out of trust assets", "PARTIAL",
         "Reported with numeral 1 = 2 (Fiduciarias) and the trust identified in numeral 35. Not an "
         "ordinary corporate payroll case; where it arises, the reporting party is the fiduciaria, "
         "not the employer."),
        ("Educational support administered by a third party", "NO",
         "Res. 227 par. 7 sends it to Formato 5247 concepto 5102. Only support paid DIRECTLY by the "
         "employer goes to numeral 16."),
        ("Employee with a dependant claimed under art. 387 par. 2", "YES",
         "Numeral 34. Must agree with Formulario 220 casillas 79 and 80 - this is where DIAN "
         "cross-checks a dependant claimed twice."),
        ("Employee who acquired residence mid-year", "YES",
         "ONE record. Numeral 29 sums the 20% months and the art. 383 months; the format has no "
         "field to disclose the split."),
    ]),
    "fields": FIELDS,
}
