# -*- coding: utf-8 -*-
"""
CO-DIAN-004 - Formulario 220, Certificado de ingresos y retenciones por rentas
de trabajo y de pensiones.
Filing ID: CO-DIAN-F220-ANNUAL-004.

EVERY casilla number, label and rule in this module is taken verbatim from the
OFFICIAL form design and instructivo held at
  00-official-sources/pdfs/Formulario_220_CertificadoIngresosRetenciones.pdf
(form prescribed by Resolucion DIAN 000022 of 20 February 2024; obligation from
ET arts. 378, 379, 380 and DUR 1625 de 2016 art. 1.6.1.13.2.40).
Extraction artefact: _txt/form220.txt.

C19 code pattern: casilla numbers 4 to 82 as printed on the form, plus the
reserved signature area. Pattern ^([1-9][0-9]{0,2})$, each value read off the
form design - nothing derived.
"""

from build_co_specs import (R_F220, R_NONE, RA)
from co_scope_common import SCOPE_WHO, SCOPE_TIMING


def F(en, es, rec, pos, mand, cond, xpath, length, fmt, ex, mapping, expl,
      rel, opts, rnd, neg, vt, freq, q, ra, kind):
    return [en, es, rec, pos, "", mand, cond, xpath, length, fmt, ex, mapping,
            expl, rel, opts, rnd, neg, vt, freq, q, ra, kind]


def M(en, es, pos, ex, mapping, expl, mand="Y", cond="", opts="-", kind="payroll",
      rec="Concepto de los ingresos", vt="Amount", rnd=R_F220, q=""):
    """Money casilla helper - all money casillas share format and rounding."""
    return F(en, es, rec, str(pos), mand, cond, "Casilla %s" % pos, "12",
             "N (whole pesos, nearest 1,000; zero where nil)", ex, mapping, expl,
             "Y" if kind == "payroll" else "N", opts, rnd, "N", vt, "Annual", q, RA, kind)


FIELDS = [
    "WITHHOLDING AGENT (casillas 4-11)",
    F("Certificate number", "Numero de formulario", "Informacion del agente retenedor", "4", "Y", "",
      "Casilla 4", "Var", "N", "2026-000417", "Mercans.Certificate_Number",
      "SHARP CONTRAST WITH FORMULARIO 350. The instructivo says this number is 'asignado por la "
      "persona natural o juridica que expide la certificacion' - the EMPLOYER assigns it, not DIAN. "
      "On Form 350 casilla 4 is DIAN-assigned. The engine must therefore maintain its own "
      "certificate numbering series and keep it stable, because the employee quotes it.",
      "Y", "-", R_NONE, "N", "Identifier", "Annual", "", RA, "system"),
    F("Employer NIT", "Numero de Identificacion Tributaria (NIT)",
      "Informacion del agente retenedor", "5", "Y", "",
      "Casilla 5", "Var", "N (no dots, no hyphens, no DV)", "900123456", "Company.NIT",
      "NIT of the withholding agent as it appears in casilla 5 of the RUT, WITHOUT the verification "
      "digit. The instructivo is emphatic: 'En ningun caso escriba puntos, guiones o letras'.",
      "Y", "-", R_NONE, "N", "Identifier", "Annual", "", RA, "payroll"),
    F("NIT verification digit", "DV", "Informacion del agente retenedor", "6", "Y", "",
      "Casilla 6", "1", "N", "7", "Company.NIT_DV",
      "Verification digit as it appears in casilla 6 of the RUT.",
      "Y", "-", R_NONE, "N", "Identifier", "Annual", "", RA, "payroll"),
    F("First surname", "Primer apellido", "Informacion del agente retenedor", "7", "C",
      "Populated only where the withholding agent is a NATURAL person. Mutually exclusive with "
      "'Corporate name' (casilla 11), which the instructivo says a natural person must NOT fill.",
      "Casilla 7", "Var", "A", "-", "Company.First_Surname",
      "First surname of a natural-person agent, matching casilla 31 of the RUT. The instructivo "
      "directs that where it does not match, THE RUT MUST BE UPDATED BEFORE THE CERTIFICATE IS "
      "ISSUED - the form does not override the register.",
      "Y", "-", R_NONE, "N", "Text", "Annual", "", RA, "payroll"),
    F("Second surname", "Segundo apellido", "Informacion del agente retenedor", "8", "C",
      "Populated only for a natural-person agent. Mutually exclusive with 'Corporate name' "
      "(casilla 11).",
      "Casilla 8", "Var", "A", "-", "Company.Second_Surname",
      "Second surname, matching casilla 32 of the RUT.",
      "Y", "-", R_NONE, "N", "Text", "Annual", "", RA, "payroll"),
    F("First name", "Primer nombre", "Informacion del agente retenedor", "9", "C",
      "Populated only for a natural-person agent. Mutually exclusive with 'Corporate name' "
      "(casilla 11).",
      "Casilla 9", "Var", "A", "-", "Company.First_Name",
      "First given name, matching casilla 33 of the RUT.",
      "Y", "-", R_NONE, "N", "Text", "Annual", "", RA, "payroll"),
    F("Other names", "Otros nombres", "Informacion del agente retenedor", "10", "C",
      "Populated only for a natural-person agent. Mutually exclusive with 'Corporate name' "
      "(casilla 11).",
      "Casilla 10", "Var", "A", "-", "Company.Other_Names",
      "Remaining given names, matching casilla 34 of the RUT.",
      "Y", "-", R_NONE, "N", "Text", "Annual", "", RA, "payroll"),
    F("Corporate name", "Razon social", "Informacion del agente retenedor", "11", "C",
      "Populated only where the withholding agent is a LEGAL person or a sociedad de hecho. The "
      "instructivo states that a natural-person issuer 'no debe diligenciar esta casilla'. Mutually "
      "exclusive with casillas 7 to 10.",
      "Casilla 11", "Var", "A", "MERCANS COLOMBIA S.A.S.", "Company.Legal_Name",
      "Full corporate name, matching casilla 35 of the RUT.",
      "Y", "-", R_NONE, "N", "Text", "Annual", "", RA, "payroll"),

    "EMPLOYEE OR PENSIONER (casillas 24-29)",
    F("Employee document type", "Tipo de documento", "Datos del trabajador o pensionado", "24",
      "Y", "", "Casilla 24", "2", "N (code)", "13", "Employee.Document_Type",
      "The instructivo prints a SIX-VALUE list on the form itself: 12 Tarjeta de identidad, "
      "13 Cedula de ciudadania, 21 Tarjeta de extranjeria, 22 Cedula de extranjeria, 31 NIT, "
      "41 Pasaporte. That is NARROWER than the nomina electronica list at Anexo table 5.2.1, which "
      "also carries 11 Registro civil, 42 Documento de identificacion extranjero, 47 PEP, 50 NIT de "
      "otro pais and 91 NUIP. An employee holding a PEP or a PPT therefore has NO exact code here.",
      "Y", "-> Sheet 6: Tipo de documento (Form 220)", R_NONE, "N", "Code", "Annual",
      "The Form 220 document-type list omits 47 (PEP) and has no PPT code at all. Confirm with the "
      "RA how a PEP or PPT holder should be certified - 41 (Pasaporte) and 22 (Cedula de "
      "extranjeria) are the only near neighbours and neither is correct.", RA, "payroll"),
    F("Employee identification number", "Numero de identificacion",
      "Datos del trabajador o pensionado", "25", "Y", "",
      "Casilla 25", "Var", "N / AN", "1020304050", "Employee.Document_Number",
      "Identification number exactly as it appears on the identity document. Join key to the nomina "
      "electronica NIE045, to PILA Registro Tipo 2 campo 4 and to Formato 2276 numeral 2.",
      "Y", "-", R_NONE, "N", "Identifier", "Annual", "", RA, "payroll"),
    F("Employee first surname", "Primer apellido", "Datos del trabajador o pensionado", "26",
      "Y", "", "Casilla 26", "Var", "A", "PEREZ", "Employee.First_Surname",
      "First surname exactly as on the identity document.",
      "Y", "-", R_NONE, "N", "Text", "Annual", "", RA, "payroll"),
    F("Employee second surname", "Segundo apellido", "Datos del trabajador o pensionado", "27",
      "N", "", "Casilla 27", "Var", "A", "GOMEZ", "Employee.Second_Surname",
      "Second surname. Not mandatory here, in contrast with the nomina electronica where it is "
      "use=required (CO-GAP-07).",
      "Y", "-", R_NONE, "N", "Text", "Annual", "", RA, "payroll"),
    F("Employee first name", "Primer nombre", "Datos del trabajador o pensionado", "28", "Y", "",
      "Casilla 28", "Var", "A", "JUAN", "Employee.First_Name",
      "First given name exactly as on the identity document.",
      "Y", "-", R_NONE, "N", "Text", "Annual", "", RA, "payroll"),
    F("Employee other names", "Otros nombres", "Datos del trabajador o pensionado", "29", "N", "",
      "Casilla 29", "Var", "A", "CARLOS", "Employee.Other_Names",
      "Remaining given names.", "Y", "-", R_NONE, "N", "Text", "Annual", "", RA, "payroll"),

    "CERTIFICATION PERIOD AND PLACE (casillas 30-35)",
    F("Period certified - from", "Periodo de la certificacion, DE", "Periodo", "30", "Y", "",
      "Casilla 30", "8", "AAAA MM DD", "2026 01 01", "PayPeriod.Year_Start",
      "First day of the certified period. Normally 1 January, but the hire date where the employee "
      "joined during the year. Bidirectional pair with casilla 31.",
      "Y", "-", R_NONE, "N", "Date", "Annual", "", RA, "payroll"),
    F("Period certified - to", "Periodo de la certificacion, A", "Periodo", "31", "Y", "",
      "Casilla 31", "8", "AAAA MM DD", "2026 12 31", "PayPeriod.Year_End",
      "Last day of the certified period. Normally 31 December, but the termination date where the "
      "employee left during the year. Bidirectional pair with casilla 30.",
      "Y", "-", R_NONE, "N", "Date", "Annual", "", RA, "payroll"),
    F("Date of issue", "Fecha de expedicion", "Periodo", "32", "Y", "",
      "Casilla 32", "8", "AAAA MM DD", "2027 03 31", "System.Certificate_Issue_Date",
      "Date the certificate is issued, in year-month-day order. Must be on or before the LAST "
      "BUSINESS DAY OF MARCH following the fiscal year - the statutory deadline.",
      "N", "-", R_NONE, "N", "Date", "Annual", "", RA, "system"),
    F("Place where the withholding was made", "Lugar donde se practico la retencion", "Periodo",
      "33", "Y", "", "Casilla 33", "Var", "A", "BOGOTA D.C.", "Company.City_Code",
      "City or municipality where the withholding was practised - not necessarily the employer's "
      "registered domicile, and not necessarily the employee's place of work.",
      "Y", "-", R_NONE, "N", "Text", "Annual", "", RA, "payroll"),
    F("Department code", "Cod. Dpto.", "Periodo", "34", "Y", "",
      "Casilla 34", "2", "N (DANE)", "11", "Company.Department_Code",
      "DANE department code of the place in casilla 33. The instructivo directs the use of the DANE "
      "'Codigo de departamentos' tables.",
      "Y", "-> Sheet 6: DIVIPOLA (DANE)", R_NONE, "N", "Code", "Annual", "", RA, "payroll"),
    F("City or municipality code", "Cod. Ciudad/Municipio", "Periodo", "35", "Y", "",
      "Casilla 35", "3", "N (DANE)", "001", "Company.City_Code",
      "DANE municipality code of the place in casilla 33. Like PILA and unlike the nomina "
      "electronica, Form 220 splits the DIVIPOLA code across two casillas.",
      "Y", "-> Sheet 6: DIVIPOLA (DANE)", R_NONE, "N", "Code", "Annual", "", RA, "payroll"),

    "INCOME CONCEPTS (casillas 36-52)",
    M("Salary payments", "Pagos por salarios", 36, "144000000", "SUM(Payroll.Salary_Payments)",
      "Total salary payments ACTUALLY MADE in the period to a resident natural person whose income "
      "derives from an employment or statutory relationship. The instructivo quotes CST art. 127 in "
      "full: salary is not only the ordinary fixed or variable remuneration but everything the "
      "employee receives in money or in kind as direct consideration for the service - primas, "
      "sobresueldos, habitual bonuses, overtime, work on mandatory rest days, sales percentages and "
      "commissions. EXCLUSION RULE: do NOT include here any value belonging in casillas 38 to 46."),
    M("Payments made with vouchers, cheques, cards or vales",
      "Pagos realizados con bonos electronicos o de papel de servicio, cheques, tarjetas, vales, "
      "etc.", 37, "0", "SUM(Payroll.Voucher_Payments)",
      "Payments made in electronic or paper service vouchers, cheques, cards or vales - for fuel, "
      "school supplies, footwear and clothing, or any other purpose. Deductible for the employer "
      "and income for the employee. THREE EXPLICIT NOTES in the instructivo: (1) INCLUDE meal "
      "payments for an employee earning MORE than 310 UVT per month; (2) do NOT include meal "
      "payments for an employee earning up to 310 UVT - those go to casilla 38; (3) do NOT include "
      "anything already reported in casilla 36.",
      opts="-> Sheet 6: Umbrales UVT 2026"),
    M("Excess meal payments over 41 UVT (ET art. 387-1)",
      "Valor del exceso de los pagos por alimentacion mayores a 41 UVT, art. 387-1 E.T.", 38, "0",
      "SUM(Payroll.Meal_Excess_41UVT)",
      "Where the employer pays a THIRD PARTY for the employee's or their family's meals - a "
      "restaurant, own or third-party, or vouchers for food - the payment is deductible for the "
      "employer and is NOT income for the employee but for the supplier, PROVIDED the employee's "
      "salary does not exceed 310 UVT (COP 16,235,940 per month in 2026). Where the monthly "
      "payments exceed 41 UVT (COP 2,147,334 in 2026), THE EXCESS is taxable income of the employee "
      "and is withheld as employment income. The instructivo adds that the rule does not apply to "
      "company representation expenses, which remain deductible. Do NOT include amounts already in "
      "casilla 36.",
      cond="Populated only where meal payments to a third party exceed 41 UVT in a month AND the "
           "employee's salary does not exceed 310 UVT. Bidirectional pair with casilla 37: where "
           "the salary exceeds 310 UVT the WHOLE meal payment goes to casilla 37 instead, and "
           "casilla 38 stays nil.",
      mand="C", opts="-> Sheet 6: Umbrales UVT 2026"),
    M("Fee payments", "Pagos por honorarios", 39, "0", "SUM(Payroll.Honorarios)",
      "Fees paid to natural persons providing services in which the INTELLECTUAL factor predominates "
      "over the technical, material, manual or mechanical - typically a professional qualification "
      "or substantial expertise in a field. The instructivo also directs that ECCLESIASTICAL "
      "EMOLUMENTS be included here, in money or in kind, direct or indirect, whatever the "
      "denomination and whatever the religious orientation.",
      mand="C",
      cond="Populated only where the employer paid fees to this natural person. Not employment "
           "income; present because Form 220 certifies all work income of ET art. 383, not only "
           "employment income."),
    M("Service payments", "Pagos por servicios", 40, "0", "SUM(Payroll.Servicios)",
      "Payments for services - any activity, labour or work performed WITHOUT an employment "
      "relationship, resulting in an obligation to do, in which the technical and manual "
      "predominate over the intellectual.",
      mand="C",
      cond="Populated only where the employer paid such services to this natural person."),
    M("Commission payments", "Pagos por comisiones", 41, "0", "SUM(Payroll.Comisiones)",
      "Commissions - remuneration for acts, operations, dealings, mandates, business or sales "
      "carried out in one's own name but for the account of another, whether or not commercial. "
      "NOTE: commissions paid UNDER AN EMPLOYMENT CONTRACT are salary under CST art. 127 and belong "
      "in casilla 36; this casilla is for non-employment commissions.",
      mand="C",
      cond="Populated only where the employer paid non-employment commissions to this natural "
           "person. Mutually exclusive with casilla 36 for the same amount."),
    M("Statutory benefit payments", "Pagos por prestaciones sociales", 42, "12000000",
      "SUM(Payroll.Prestaciones_Sociales)",
      "Statutory benefits OTHER THAN severance savings and the interest on them. The instructivo "
      "lists prima de servicios, vacaciones and dotaciones among them, and directs expressly that "
      "severance savings paid to the employee go to casilla 47 and severance savings deposited to "
      "the fund go elsewhere. RECORDED DEFECT: the instructivo for THIS casilla says the deposited "
      "severance goes to 'la casilla 48', but the form's own printed label makes casilla 48 the "
      "TRADITIONAL-REGIME severance and casilla 49 the amount deposited to the fund. The form "
      "layout is authoritative.",
      q="DEFECT IN THE OFFICIAL INSTRUCTIVO, recorded. The casilla-42 instruction cross-refers "
        "severance deposited to the fund to 'casilla 48'; the form's printed label puts it at "
        "casilla 49, and casilla 48 is the traditional-regime severance. Confirm with the RA that "
        "the form layout governs."),
    M("Per diem payments", "Pagos por viaticos", 43, "0", "SUM(Payroll.Viaticos)",
      "Per diems paid to cover transport, subsistence and accommodation while the employee works "
      "away from the habitual place of work. The instructivo cites Ministerio del Trabajo Concepto "
      "23959 of 13 February. Note the split that matters elsewhere: the PERMANENT portion is salary "
      "under CST art. 130 and feeds the contribution base, while the accidental portion does not - "
      "the nomina electronica carries them as the paired ViaticoManuAlojS / NS elements.",
      mand="C",
      cond="Populated where per diems were paid in the period. Related to the nomina electronica "
           "paired elements NIE072 / NIE073, which split the same amount by salary character."),
    M("Representation expense payments", "Pagos por gastos de representacion", 44, "0",
      "SUM(Payroll.Gastos_Representacion)",
      "Representation expenses paid to the employee. The instructivo notes at casilla 38 that "
      "company representation expenses are deductible for the company and fall outside the "
      "meal-payment rule of ET art. 387-1.",
      mand="C", cond="Populated where representation expenses were paid in the period."),
    M("Cooperative associated-work compensation",
      "Pagos por compensaciones por el trabajo asociado cooperativo", 45, "0",
      "SUM(Payroll.Coop_Compensation)",
      "Compensation for associated cooperative work. Corresponds to the nomina electronica "
      "Compensacion elements (NIE149 / NIE150) and applies only to worker type 31.",
      mand="C", cond="Populated only for a member of an associated-work cooperative - PILA "
                     "contributor type 31 and nomina electronica TipoTrabajador 31."),
    M("Other payments", "Otros pagos", 46, "0", "SUM(Payroll.Other_Work_Payments)",
      "Work-income payments not falling in any other casilla. Use sparingly: DIAN expects a concept "
      "with a dedicated casilla to use that casilla.",
      mand="C", cond="Populated where a work-income payment has no dedicated casilla."),
    M("Severance savings and interest paid to the employee",
      "Auxilio de cesantia e intereses efectivamente pagados al empleado", 47, "1440000",
      "Payroll.Cesantias_Paid_To_Employee",
      "THE FIRST OF THREE SEVERANCE LINES. Severance savings and the interest on them ACTUALLY PAID "
      "to the employee in the period - typically the January interest payment and any authorised "
      "partial withdrawal or termination settlement. Excluded from the monthly withholding base "
      "under ET art. 206 num. 4 but still certified here.",
      opts="-> Sheet 6: Las tres lineas de cesantias"),
    M("Severance savings under the traditional CST regime",
      "Auxilio de cesantia reconocido a trabajadores del regimen tradicional del Codigo Sustantivo "
      "del Trabajo, contenido en el Capitulo VII, Titulo VIII Parte Primera", 48, "0",
      "Payroll.Cesantias_Traditional_Regime",
      "THE SECOND OF THREE SEVERANCE LINES. Severance RECOGNISED - not necessarily paid - to "
      "employees remaining under the pre-1991 retroactive regime of CST Chapter VII, Title VIII, "
      "Part One, rather than the Ley 50 de 1990 annual-deposit regime. A shrinking but real "
      "population: employees hired before 1 January 1991 who did not elect the new regime.",
      mand="C",
      cond="Populated only for an employee under the pre-1991 traditional severance regime. "
           "Mutually exclusive with 'Severance savings deposited to the fund' (casilla 49) for the "
           "same employee: a traditional-regime employee has no annual fund deposit.",
      opts="-> Sheet 6: Las tres lineas de cesantias"),
    M("Severance savings deposited to the fund",
      "Auxilio de cesantia consignado al fondo de cesantias", 49, "12000000",
      "Payroll.Cesantias_Deposited_To_Fund",
      "THE THIRD OF THREE SEVERANCE LINES. The amount DEPOSITED to the employee's chosen severance "
      "fund by 14 February for the balance at the preceding 31 December, under Ley 50 de 1990 "
      "art. 99. The engine must maintain all three buckets - paid to the employee, traditional "
      "regime, deposited to the fund - separately from the outset; they cannot be split "
      "retrospectively out of a single cesantias figure.",
      mand="C",
      cond="Populated for an employee under the Ley 50 de 1990 regime. Mutually exclusive with "
           "'Severance savings under the traditional CST regime' (casilla 48) for the same "
           "employee. Must reconcile to the amount actually deposited under CO-CESANTIAS-006.",
      opts="-> Sheet 6: Las tres lineas de cesantias"),
    M("Retirement, old-age or invalidity pensions", "Pensiones de jubilacion, vejez o invalidez",
      50, "0", "SUM(Payroll.Pension_Payments)",
      "Pension income paid BY THE EMPLOYER. Taxable only above 1,000 UVT per month "
      "(COP 52,374,000 in 2026) under ET art. 206 num. 5. Nil for an ordinary corporate payroll, "
      "where pensions are paid by a fund and the fund is the withholding agent.",
      mand="C", cond="Populated only where the employer itself pays a pension. Bidirectional with "
                     "Formulario 350 casillas 78 and 94, which carry the same population monthly."),
    M("Non-reimbursable educational support financed with public funds",
      "Apoyos economicos educativos financiados con recursos publicos, no reembolsables o "
      "condonados", 51, "0", "SUM(Payroll.Educational_Support)",
      "Non-reimbursable or forgiven educational support delivered or financed by the State. Where "
      "the EMPLOYER pays it directly it is reported here and in Formato 2276 numeral 16; where a "
      "third party administers it, Res. DIAN 000227 de 2025 art. 1.3.7.1.1 par. 7 sends it to "
      "Formato 5247 concepto 5102 instead.",
      mand="C",
      cond="Populated only where non-reimbursable educational support financed with public funds "
           "was paid DIRECTLY by the employer. Where administered by a third party it is reported "
           "in Formato 5247, not here."),
    M("Total gross income", "Total de ingresos brutos", 52, "157440000", "SUM(casillas 36 to 51)",
      "The form prints the arithmetic on its face: 'Sume 36 a 51'. Sixteen casillas, summed. This "
      "is GROSS income, before the contributions and deductions in casillas 53 to 58.",
      kind="system", rec="Concepto de los ingresos"),

    "EMPLOYEE CONTRIBUTIONS AND WITHHOLDING (casillas 53-60)",
    M("Mandatory health contributions borne by the employee",
      "Aportes obligatorios por salud a cargo del trabajador", 53, "5760000",
      "SUM(Payroll.Health_Employee_Contribution)",
      "The employee's own mandatory health contributions ACTUALLY DEDUCTED in the period. These are "
      "ingresos no constitutivos de renta and are what reduces the ET art. 388 depurated base. Must "
      "reconcile to twelve months of nomina electronica NIE163 and to the employee portion of PILA "
      "Registro Tipo 2 campo 55.",
      rec="Concepto de los aportes"),
    M("Mandatory pension and solidarity-fund contributions borne by the employee",
      "Aportes obligatorios a fondos de pensiones y solidaridad pensional a cargo del trabajador",
      54, "7200000", "SUM(Payroll.Pension_Employee + Payroll.FSP)",
      "The employee's mandatory pension contributions AND the solidarity-fund surcharge, TAKEN "
      "TOGETHER IN ONE CASILLA. Note the asymmetry with the nomina electronica, which insists on "
      "reporting them as separate elements (NIE166 for pension, NIE168 and NIE170 for the two "
      "solidarity sub-accounts). The engine must keep them separate internally and sum them only "
      "here.",
      rec="Concepto de los aportes"),
    M("Voluntary contributions to the individual-account pension regime (RAIS)",
      "Cotizaciones voluntarias al regimen de ahorro individual con solidaridad - RAIS", 55, "0",
      "SUM(Payroll.Voluntary_RAIS)",
      "Voluntary contributions to the RAIS under ET art. 55 and DUR 1625 de 2016 art. 1.2.1.12.9. "
      "DISTINCT from voluntary contributions to a VOLUNTARY pension fund, which go to casilla 56. "
      "The nomina electronica has ONE element (PensionVoluntaria, NIE198) for both, so the engine "
      "must carry the distinction itself.",
      mand="C",
      cond="Populated where the employee made voluntary RAIS contributions. Mutually distinct from "
           "'Voluntary contributions to voluntary pension funds' (casilla 56) - the two have "
           "different legal bases and must not be combined.",
      rec="Concepto de los aportes"),
    M("Voluntary contributions to voluntary pension funds",
      "Aportes voluntarios a fondos de pensiones", 56, "0", "SUM(Payroll.Voluntary_Pension_Fund)",
      "Voluntary contributions to voluntary pension funds under ET art. 126-1 and DUR 1625 de 2016 "
      "art. 1.2.1.22.41. Shares the ET art. 336 40% / 1,340-UVT annual cap with AFC and AVC.",
      mand="C",
      cond="Populated where the employee made voluntary pension-fund contributions. Distinct from "
           "'Voluntary RAIS contributions' (casilla 55).",
      rec="Concepto de los aportes"),
    M("AFC account contributions", "Aportes a cuentas AFC", 57, "0", "SUM(Payroll.AFC)",
      "Deductions to Ahorro para el Fomento de la Construccion accounts - programmed housing "
      "savings. Corresponds to nomina electronica NIE179.",
      mand="C", cond="Populated where AFC deductions were made.",
      rec="Concepto de los aportes"),
    M("AVC account contributions", "Aportes a cuentas AVC", 58, "0", "SUM(Payroll.AVC)",
      "Deductions to the Fondo Nacional del Ahorro as programmed savings for housing or education. "
      "The nomina electronica has no dedicated element for AVC; it falls to OtraDeduccion (NIE197), "
      "so the engine must tag it to be able to report it here.",
      mand="C", cond="Populated where AVC deductions to the FNA were made.",
      rec="Concepto de los aportes"),
    M("Average labour income of the last six months",
      "Ingreso laboral promedio de los ultimos seis meses anteriores (numeral 4 art. 206 E.T.)",
      59, "13120000", "Payroll.Rolling_6M_Average_Labour_Income",
      "THE ROLLING SIX-MONTH AVERAGE that drives the ET art. 206 num. 4 severance exemption and its "
      "taper. Severance savings and the interest on them are EXEMPT IN FULL where this average does "
      "not exceed 350 UVT (COP 18,330,900 per month in 2026), and tapered above it. THE ENGINE MUST "
      "MAINTAIN THIS AVERAGE YEAR-ROUND - it cannot be reconstructed at year end from annual totals "
      "because it is a moving six-month window, and on a termination it is the average of the last "
      "six months OF EMPLOYMENT.",
      mand="C",
      cond="Required only for employees to whom ET art. 206 num. 4 applies - that is, where "
           "severance savings or interest were paid or deposited. Bidirectional with casillas 47, "
           "48 and 49: a certificate carrying any of those three should carry this average.",
      opts="-> Sheet 6: Umbrales UVT 2026", rec="Concepto de los aportes"),
    M("Withholding on labour and pension income",
      "Valor de la retencion en la fuente por ingresos laborales y de pensiones", 60, "7404000",
      "SUM(Payroll.Income_Tax_Withheld)",
      "THE PRINCIPAL WITHHOLDING CASILLA. Total retencion en la fuente practised on this employee's "
      "work and pension income during the certified period. Feeds casilla 75 together with casilla "
      "74. Must reconcile to twelve months of nomina electronica NIE177 for this employee, and the "
      "sum of casilla 60 across all employees must reconcile to twelve months of Formulario 350 "
      "casilla 93 - allowing for the rounding conventions.",
      rec="Concepto de los aportes"),

    "OTHER INCOME OF THE EMPLOYEE (casillas 61-75)",
    M("Rentals - amount received", "Arrendamientos - valor recibido", 61, "0",
      "(employee declaration)",
      "SECTION HEADED 'DATOS A CARGO DEL TRABAJADOR O PENSIONADO' - data the EMPLOYEE supplies, not "
      "payroll. Rental income received by the employee from any source. Paired with casilla 68, the "
      "amount withheld on it.",
      mand="C",
      cond="Supplied BY THE EMPLOYEE where they received such income. Bidirectional pair with "
           "'Rentals - amount withheld' (casilla 68).",
      kind="na", rec="Datos a cargo del trabajador"),
    M("Fees, commissions and services - amount received",
      "Honorarios, comisiones y servicios - valor recibido", 62, "0", "(employee declaration)",
      "Employee-supplied. Fees, commissions and service income received from OTHER payers. Paired "
      "with casilla 69.",
      mand="C",
      cond="Supplied by the employee. Bidirectional pair with casilla 69.",
      kind="na", rec="Datos a cargo del trabajador"),
    M("Interest and financial yields - amount received",
      "Intereses y rendimientos financieros - valor recibido", 63, "0", "(employee declaration)",
      "Employee-supplied. Paired with casilla 70.",
      mand="C", cond="Supplied by the employee. Bidirectional pair with casilla 70.",
      kind="na", rec="Datos a cargo del trabajador"),
    M("Disposal of fixed assets - amount received",
      "Enajenacion de activos fijos - valor recibido", 64, "0", "(employee declaration)",
      "Employee-supplied. Paired with casilla 71.",
      mand="C", cond="Supplied by the employee. Bidirectional pair with casilla 71.",
      kind="na", rec="Datos a cargo del trabajador"),
    M("Lotteries, raffles and betting - amount received",
      "Loterias, rifas, apuestas y similares - valor recibido", 65, "0", "(employee declaration)",
      "Employee-supplied. Paired with casilla 72.",
      mand="C", cond="Supplied by the employee. Bidirectional pair with casilla 72.",
      kind="na", rec="Datos a cargo del trabajador"),
    M("Other income - amount received", "Otros - valor recibido", 66, "0",
      "(employee declaration)",
      "Employee-supplied. Paired with casilla 73.",
      mand="C", cond="Supplied by the employee. Bidirectional pair with casilla 73.",
      kind="na", rec="Datos a cargo del trabajador"),
    M("Total other income received", "Totales - valor recibido", 67, "0", "SUM(casillas 61 to 66)",
      "The form prints the arithmetic: 'Sume 61 a 66'.",
      kind="system", rec="Datos a cargo del trabajador"),
    M("Other income - amounts withheld (casillas 68 to 73)",
      "Valor retenido - arrendamientos, honorarios, intereses, activos fijos, loterias, otros",
      "68-73", "0", "(employee declaration)",
      "Employee-supplied withholding amounts corresponding one for one to casillas 61 to 66. Each "
      "is a bidirectional pair with its received-amount counterpart: 68 with 61, 69 with 62, 70 "
      "with 63, 71 with 64, 72 with 65, 73 with 66.",
      mand="C",
      cond="Supplied by the employee alongside the corresponding received amount in casillas 61 to "
           "66. A withheld amount without a received amount, or the reverse, is an inconsistency.",
      kind="na", rec="Datos a cargo del trabajador"),
    M("Total other income withheld", "Totales - valor retenido", 74, "0",
      "SUM(casillas 68 to 73)",
      "The form prints the arithmetic: 'Sume 68 a 73'.",
      kind="system", rec="Datos a cargo del trabajador"),
    M("Total withholding for the tax year", "Total retenciones ano gravable", 75, "7404000",
      "Casilla 60 + casilla 74",
      "The form prints the arithmetic: 'Sume 60 + 74'. It combines the employer's own withholding "
      "on work income with the employee-declared withholding on other income. Only casilla 60 comes "
      "from payroll.",
      kind="system", rec="Datos a cargo del trabajador"),

    "ASSETS, DEBTS AND DEPENDANTS (casillas 76-82)",
    F("Identification of assets held", "Identificacion de los bienes poseidos",
      "Datos a cargo del trabajador", "76", "C",
      "Supplied BY THE EMPLOYEE. Bidirectional pair with 'Asset value' (casilla 77): an asset "
      "described without a value, or a value without a description, is incomplete. Three rows are "
      "printed on the form.",
      "Casilla 76", "Var", "A", "-", "(employee declaration)",
      "Free-text description of each asset held at 31 December. Employee-supplied; payroll neither "
      "knows nor certifies it. It exists because the certificate SUBSTITUTES for the income-tax "
      "return where the employee meets the ET art. 380 conditions.",
      "N", "-", R_NONE, "N", "Text", "Annual", "", RA, "na"),
    F("Asset value", "Valor patrimonial", "Datos a cargo del trabajador", "77", "C",
      "Supplied by the employee. Bidirectional pair with 'Identification of assets held' "
      "(casilla 76).",
      "Casilla 77", "12", "N (whole pesos, nearest 1,000)", "-", "(employee declaration)",
      "Tax value of each asset at 31 December.",
      "N", "-", R_F220, "N", "Amount", "Annual", "", RA, "na"),
    F("Debts outstanding at 31 December", "Deudas vigentes a 31 de diciembre",
      "Datos a cargo del trabajador", "78", "C",
      "Supplied by the employee. Related to casillas 76 and 77, which give the asset side of the "
      "same net-worth statement.",
      "Casilla 78", "12", "N (whole pesos, nearest 1,000)", "-", "(employee declaration)",
      "Total debts outstanding at 31 December. Employee-supplied.",
      "N", "-", R_F220, "N", "Amount", "Annual", "", RA, "na"),
    F("Dependant document type", "Tipo documento (dependiente economico)",
      "Identificacion del dependiente economico", "79", "C",
      "Populated where the employee claimed the ET art. 387 par. 2 dependants deduction during the "
      "period. Bidirectional set with casillas 80, 81 and 82 - all four are populated together or "
      "none is.",
      "Casilla 79", "2", "N (code)", "13", "Employee.Dependant_Document_Type",
      "Identity document type of the economic dependant, under ET art. 387 par. 2. The dependants "
      "deduction is 10% of gross employment income capped at 32 UVT per month "
      "(COP 1,675,968 in 2026), so a claimed dependant materially reduces the withholding base and "
      "must be evidenced.",
      "Y", "-> Sheet 6: Tipo de documento (Form 220)", R_NONE, "N", "Code", "Annual", "", RA, "payroll"),
    F("Dependant document number", "No. Documento (dependiente economico)",
      "Identificacion del dependiente economico", "80", "C",
      "Populated with casillas 79, 81 and 82. Bidirectional set.",
      "Casilla 80", "Var", "N / AN", "1122334455", "Employee.Dependant_Document_Number",
      "Identity number of the dependant. Also reported in Formato 2276 numeral 34, which is where "
      "DIAN cross-checks a dependant claimed by more than one taxpayer.",
      "Y", "-", R_NONE, "N", "Identifier", "Annual", "", RA, "payroll"),
    F("Dependant surnames and names", "Apellidos y Nombres (dependiente economico)",
      "Identificacion del dependiente economico", "81", "C",
      "Populated with casillas 79, 80 and 82. Bidirectional set.",
      "Casilla 81", "Var", "A", "MARIA PEREZ RUIZ", "Employee.Dependant_Name",
      "Full name of the dependant.",
      "Y", "-", R_NONE, "N", "Text", "Annual", "", RA, "payroll"),
    F("Relationship", "Parentesco", "Identificacion del dependiente economico", "82", "C",
      "Populated with casillas 79, 80 and 81. Bidirectional set.",
      "Casilla 82", "Var", "A", "HIJA", "Employee.Dependant_Relationship",
      "Relationship of the dependant to the employee. ET art. 387 par. 2 recognises children under "
      "18; children between 18 and 23 in education; children over 23 with a certified physical or "
      "psychological dependency; a spouse or partner in a state of dependency for the same reasons; "
      "and parents or siblings in a certified state of dependency.",
      "Y", "-> Sheet 6: Parentesco (art. 387 par. 2)", R_NONE, "N", "Text", "Annual", "", RA, "payroll"),

    "EMPLOYEE CERTIFICATION UNDER ET ART. 380 - DISPLAY-ONLY DECLARATIONS",
    F("Employee's six non-filing declarations", "Certifico que durante el ano gravable (6 items)",
      "Certificacion del trabajador", "(unnumbered)", "C",
      "The employee signs these ONLY where they intend the certificate to substitute for their "
      "income-tax return under DUR 1625 de 2016 art. 1.6.1.13.2.7. All six must be true together.",
      "Printed block above the employee's signature", "-", "Display-only declaration", "-",
      "(employee declaration)",
      "DISPLAY-ONLY - not a data field, not populated by payroll, not transmitted. The six "
      "declarations are: (1) gross wealth did not exceed 4,500 UVT; (2) gross income was below "
      "1,400 UVT; (3) not a VAT-responsible person at 31 December; (4) credit-card consumption did "
      "not exceed 1,400 UVT; (5) total purchases and consumption did not exceed 1,400 UVT; "
      "(6) total bank deposits, receipts or financial investments did not exceed 1,400 UVT. Where "
      "all six hold, the note on the form states that THIS CERTIFICATE SUBSTITUTES FOR ALL LEGAL "
      "PURPOSES for the income-tax return. THIS IS THE ONLY REASON THE EMPLOYEE-DECLARED SECTIONS "
      "EXIST ON THE FORM.",
      "N", "-> Sheet 6: Umbrales UVT 2026", R_NONE, "N", "Flag", "Annual", "", RA, "na"),
    F("Employee signature", "Firma del Trabajador o Pensionado", "Certificacion del trabajador",
      "(unnumbered)", "C",
      "Signed only where the employee makes the six art. 380 declarations. Bidirectional with the "
      "declaration block above it.",
      "Printed signature line", "-", "Display-only", "-", "(employee)",
      "DISPLAY-ONLY. The employee's signature validating the declarations. Not a payroll field.",
      "N", "-", R_NONE, "N", "Text", "Annual", "", RA, "na"),
    F("Payer or withholding agent name", "Nombre del pagador o agente retenedor",
      "Firma del agente retenedor", "(unnumbered)", "Y", "",
      "Printed signature line", "-", "Text", "MERCANS COLOMBIA S.A.S.", "Company.Legal_Name",
      "Name of the payer or withholding agent above the issuing signature. The certificate is "
      "ISSUED TO THE EMPLOYEE and RETAINED BY THE EMPLOYER - it is not filed with DIAN.",
      "Y", "-", R_NONE, "N", "Text", "Annual", "", RA, "payroll"),
]


CFG = {
    "doc_id": "CO-DIAN-004",
    "filing_id": "CO-DIAN-F220-ANNUAL-004",
    "name_en": "Annual Certificate of Income and Withholding on Work and Pension Income - Form 220",
    "name_es": "Formulario 220 - Certificado de ingresos y retenciones por rentas de trabajo y de "
               "pensiones",
    "spec_sheet": "Formulario 220 Spec",
    "authority_full": "DIAN prescribes the form; the EMPLOYER issues it to each employee and retains "
                      "it. It is NOT filed with DIAN.",
    "frequency": "Annual, one certificate per employee per tax year.",
    "due_date": "By the LAST BUSINESS DAY OF MARCH following the fiscal year (DUR 1625 de 2016 "
                "art. 1.6.1.13.2.40). For the 2026 tax year, the last business day of March 2027.",
    "submission": "ISSUED TO THE EMPLOYEE and retained by the employer. There is NO submission to "
                  "DIAN: this is a certificate, not a return. Delivery may be paper or electronic, "
                  "as agreed with the employee. The employer must retain it for the statutory "
                  "period as evidence of the withholding.",
    "file_format": "Prescribed form, 82 numbered casillas plus an unnumbered certification and "
                   "signature block. All money amounts in Colombian pesos, approximated to the "
                   "NEAREST 1,000, with ZERO written where a casilla has no value.",
    "legal_basis": "ET (Decreto-Ley 624 de 1989) arts. 55, 126-1, 206 (esp. nums. 4 y 5), 378, 379, "
                   "380, 383, 385, 386, 387 y su par. 2, 387-1, 388, 408; DUR 1625 de 2016 arts. "
                   "1.2.1.12.9, 1.2.1.22.41, 1.6.1.13.2.7, 1.6.1.13.2.40; form prescribed by "
                   "Resolucion DIAN 000022 de 20 de febrero de 2024; CST arts. 127, 130; Ley 50 de "
                   "1990 art. 99; Ley 52 de 1975 art. 1; Ministerio del Trabajo Concepto 23959 de "
                   "13 de febrero.",
    "accuracy": "93% (PRIMARY SOURCE). Every casilla number, label and arithmetic rule is read off "
                "the official form design and its four-page instructivo at "
                "00-official-sources/pdfs/Formulario_220_CertificadoIngresosRetenciones.pdf. The 7% "
                "reservation is: (a) a defect in the official instructivo - the casilla-42 "
                "instruction cross-refers severance deposited to the fund to 'casilla 48' when the "
                "form's own label puts it at casilla 49 - escalated in column T; (b) the "
                "document-type list printed on the form has only six values and contains NO code "
                "for a PEP or a PPT holder, so a regularised Venezuelan migrant cannot be certified "
                "with an exactly correct code; (c) the boundary between casilla 36 (salarios) and "
                "casillas 39 to 41 (honorarios, servicios, comisiones) for a person who is both an "
                "employee and a contractor of the same payer is a client-specific classification. "
                "It would rise to 98% with a DIAN clarification on (a) and (b).",
    "source_status": "PRIMARY. Formulario_220_CertificadoIngresosRetenciones.pdf - the prescribed "
                     "form design plus the complete instructivo, extracted to _txt/form220.txt. "
                     "Casilla numbers read off the form; the sum rules for casillas 52, 67, 74 and "
                     "75 are printed on the form's own face.",
    "channel_notes": [
        "Channel: paper or electronic delivery TO THE EMPLOYEE | Portal: none - this artefact is "
        "NOT submitted to any authority | Source: ET arts. 378-380 and the form's own instructivo, "
        "which addresses only the issuing of the certificate | CONFIRMED.",
        "This is the one in-scope Colombian artefact with NO government channel at all. It is "
        "issued to the employee and retained by the employer. DIAN sees the same data annually "
        "through Formato 2276 (CO-DIAN-005), which IS filed - but the two are separate obligations "
        "with different field sets and different deadlines.",
        "The certificate SUBSTITUTES for the employee's income-tax return where the six ET art. 380 "
        "conditions hold (DUR 1625 de 2016 art. 1.6.1.13.2.7), which is why it carries "
        "employee-declared sections that payroll cannot populate.",
    ],
    "integration_notes": [
        "integration_type = OUTBOUND (scope_manifest CO-OUT-F220), to the EMPLOYEE rather than to "
        "an authority. There is no inbound leg.",
        "product_mapping_required = true. The certificate needs per-employee ANNUAL totals by "
        "concept, three separate severance buckets, the meal-payment split at 41 UVT, the rolling "
        "six-month average labour income, and the AVC deduction which has no dedicated nomina "
        "electronica element. None of these can be reconstructed at year end from a single annual "
        "gross figure.",
        "NOT DERIVABLE FROM THE MONTHLY FILINGS (scope_manifest failure check F21). Colombia imposes "
        "NO employer year-end tax reconciliation. This certificate is a SEPARATE annual obligation "
        "built from the annual accumulation, and it additionally carries data the employer never "
        "sees monthly - the employee's own asset, debt and other-income declarations under "
        "ET art. 380.",
    ],
    "b1_notes": [
        "RESIDENT: casilla 60 carries the ET art. 383 progressive-table withholding for the year, "
        "and casillas 53 to 58 carry the contributions and voluntary savings that depurated the "
        "base. The employee may then use the certificate in place of a return under ET art. 380.",
        "NON-RESIDENT: the same certificate is issued, but casilla 60 carries the FLAT 20% of ET "
        "art. 408 applied to the GROSS - so casilla 52 (total gross income) and the withholding in "
        "casilla 60 stand in a simple 20% relationship, with NO depuration visible. The "
        "contributions in casillas 53 and 54 are still reported because they were still deducted, "
        "but they did NOT reduce the withholding base.",
        "The art. 206 num. 4 severance exemption in casilla 59 is an exemption of the RESIDENT "
        "cedula-general regime. It does NOT attach to a non-resident's flat withholding, so for a "
        "non-resident the six-month average is reported for completeness but has no effect on "
        "casilla 60.",
        "An employee who ACQUIRES RESIDENCE mid-year receives ONE certificate covering the whole "
        "period, with casilla 60 carrying the sum of the 20% months and the art. 383 months. The "
        "certificate does not disclose the split; the employee reconciles on their own return. The "
        "engine should retain the split internally for audit.",
        "The employee's own annual return - Formulario 110 - is expressly DESCOPED in "
        "scope_manifest: the employer's duty ends with this certificate.",
    ],
    "related": [
        "Casilla 60 must reconcile to twelve months of nomina electronica RetencionFuente (NIE177) "
        "for this employee - CO-DIAN-001.",
        "Casillas 53 and 54 must reconcile to twelve months of nomina electronica NIE163 and "
        "NIE166 + NIE168 + NIE170, and to the employee portions of PILA campos 55, 47, 51 and 52 - "
        "CO-PILA-003.",
        "The SUM of casilla 60 across all employees must reconcile to twelve months of Formulario "
        "350 casilla 93 - CO-DIAN-002 - but the certificate is NOT derived from those returns.",
        "Casillas 36 to 60 map almost one for one to Formato 2276 numerals 5 to 33 - CO-DIAN-005 - "
        "but the ORDER OF THE THREE SEVERANCE LINES DIFFERS: Form 220 runs 47 paid / 48 traditional "
        "/ 49 fund, while Formato 2276 runs 18 paid / 19 fund / 20 traditional. A positional copy "
        "between the two SWAPS the fund and traditional amounts.",
        "Casilla 49 must reconcile to the amount actually deposited under CO-CESANTIAS-006 by "
        "14 February.",
        "Casillas 79 to 82 (dependants) map to Formato 2276 numeral 34.",
    ],
    "scope": (SCOPE_WHO + [
        "AMOUNTS AND CALCULATIONS",
        ("Annual salary paid", "YES",
         "Casilla 36, on the CST art. 127 definition quoted in full in the instructivo."),
        ("Voucher, cheque, card and vale payments", "YES",
         "Casilla 37, including meal payments for an employee earning MORE than 310 UVT per month."),
        ("Meal payments up to 41 UVT for an employee earning up to 310 UVT", "NO",
         "Not income of the employee at all under ET art. 387-1 - income of the food supplier. Only "
         "the EXCESS over 41 UVT is reported, in casilla 38."),
        ("Statutory benefits other than severance", "YES",
         "Casilla 42 - prima de servicios, vacaciones, dotaciones."),
        ("Severance savings, split three ways", "YES",
         "Casillas 47 (paid to the employee), 48 (traditional pre-1991 regime) and 49 (deposited to "
         "the fund). Three separate buckets that must be maintained year-round."),
        ("Per diems and representation expenses", "YES", "Casillas 43 and 44."),
        ("Employee mandatory contributions", "YES",
         "Casillas 53 and 54. Note that pension and the solidarity fund are COMBINED in casilla 54, "
         "unlike the nomina electronica which separates them."),
        ("Voluntary savings - RAIS, voluntary pension, AFC, AVC", "YES",
         "Casillas 55 to 58, each separately. The nomina electronica has one element for the first "
         "two and none for AVC, so the engine must tag them itself."),
        ("Rolling six-month average labour income", "YES",
         "Casilla 59. Drives the ET art. 206 num. 4 severance exemption and its taper; must be "
         "maintained year-round."),
        ("Employer social-security contributions", "NO",
         "The certificate reports the EMPLOYEE's income and the EMPLOYEE's contributions. The "
         "employer's cost is reported only on PILA."),
        ("The employee's other income, assets and debts", "NO",
         "Casillas 61 to 78 are supplied BY THE EMPLOYEE, not by payroll. They exist so the "
         "certificate can substitute for the income-tax return under ET art. 380."),
    ] + SCOPE_TIMING + [
        "SPECIAL CASES",
        ("Employee who left during the year", "YES",
         "Casillas 30 and 31 carry the actual employment window rather than 1 January to "
         "31 December. The certificate is still issued by the last business day of March."),
        ("Employee whose withholding was nil all year", "YES",
         "A certificate is still issued. Casilla 60 is ZERO - the instructivo directs that a "
         "casilla with no value be written as zero, not left blank."),
        ("Employee who acquired tax residence mid-year", "YES",
         "ONE certificate for the whole period. Casilla 60 sums the 20% months and the art. 383 "
         "months; the split is not disclosed on the form but must be retained internally."),
        ("Employee with a dependant claimed for the art. 387 deduction", "YES",
         "Casillas 79 to 82 identify the dependant. The same dependant is reported in Formato 2276 "
         "numeral 34, where DIAN cross-checks a dependant claimed by more than one taxpayer."),
        ("Employee under the pre-1991 traditional severance regime", "YES",
         "Casilla 48 rather than casilla 49. A shrinking population - employees hired before "
         "1 January 1991 who did not elect the Ley 50 de 1990 regime."),
        ("Employee holding a PEP or PPT", "PARTIAL",
         "Reported, but the form's six-value document-type list has no code for either. Escalated "
         "in column T of casilla 24."),
        ("Certificate substituting for the employee's income-tax return", "YES",
         "Where all six ET art. 380 conditions hold and the employee signs, the form states that it "
         "substitutes 'para todos los efectos legales' for the return."),
    ]),
    "fields": FIELDS,
}
