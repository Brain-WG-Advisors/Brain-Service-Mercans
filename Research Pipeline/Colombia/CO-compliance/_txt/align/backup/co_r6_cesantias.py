# -*- coding: utf-8 -*-
r"""
CO-CESANTIAS-006 - Consignacion anual de cesantias al fondo elegido por el
trabajador (annual severance-savings deposit).
Filing ID: CO-CESANTIAS-DEPOSIT-ANNUAL-006.

SOURCE STATUS - this filing is the ONLY one of the six with no single
government-published schema, because the deposit is made to a PRIVATE fund
(or to the state-owned FNA) through a licensed operador de informacion, not to
an authority. It is nevertheless BETTER sourced than scope_manifest assumed.
What is held locally, in 00-official-sources/pdfs/:

  PRIMARY - LAW (the obligation, the base, the deadline, the penalty):
    * Ley_2466_de_2025.pdf -> art. 15 (CST art. 57 par. 4, direct payment is
      discharging) and art. 64 (two new paragraphs to Ley 50 de 1990 art. 99:
      the 8.33% monthly advance deposit and the 1% monthly interest option),
      both transcribed VERBATIM from _txt/ley2466.txt.
    * Decreto_2663_de_1950.pdf -> CST arts. 249, 250, 253, 254, 310.
    * Ley 50 de 1990 art. 99 num. 3 quoted verbatim from the secondary source
      cited in column T (the statute itself is not in the local registry).
    * Decreto-1469-de-2025-SMMLV-2026.pdf -> SMMLV 2026 and the transport
      allowance, which set the minimum-recaudo validation and the base.

  PRIMARY - PUBLISHED FILE LAYOUT (byte-exact, positions 1-258):
    * pagosimple_cesantias.pdf, "Manual Cesantias - Pago Simple / Cesantias
      Simple", Simple S.A. (licensed operador de informacion), sections 3.1
      and 3.2 -> the "Envio de Archivo Unificado de Cesantias": a 16-column
      XLS 97-2003 layout (columns A to P) AND a 20-field / 258-position
      fixed-width TXT layout with Inicial-Final positions, lengths, types,
      validations and the five-value fondo code table. Extracted to
      _txt/pagosimple_cesantias.txt. THIS IS THE FIELD-LEVEL SOURCE for
      Sheet 4 and it closes what scope_manifest recorded as DERIVED.

  PRIMARY - PUBLISHED CHANNEL (independent second operator):
    * soi_planilla_cesantias.pdf, "Instructivo para elaboracion de planilla
      Cesantias" v2, code DDS-DES-INS-008, ACH Colombia S.A. (SOI) ->
      confirms the same two-channel model (Planilla En Linea keyed in the
      portal, or Liquidacion Por Archivo uploading .txt / .csv, compressed
      above 1 MB), the Asofondos name-validation step and the planilla-number
      / comprobante round-trip. Extracted to _txt/soi_cesantias.txt.

  DRAFT, NOT IN FORCE (flagged as such on every row it touches):
    * proyecto_decreto_cesantias_2026.pdf - MinTrabajo draft decree amending
      Decreto 1072 de 2015 arts. 2.2.1.3.1, 2.2.1.3.4, 2.2.1.3.5 and
      2.2.1.3.13 to implement Ley 2466 art. 64. Extracted to
      _txt/proyecto_decreto_cesantias.txt. It is the operational rule set for
      the monthly advance and it is NOT YET LAW - see the MONTHLY ADVANCE
      section, every row of which is marked NOT OPERABLE.

C19 code patterns actually used, none invented:
  ^T(0[1-9]|1[0-9]|20)$   the campo numbers 1 to 20 of the published
                          fixed-width layout (Simple S.A. manual s. 3.2)
  ^[A-P]$                 the column letters of the published XLS layout
                          (Simple S.A. manual s. 3.1)
  ^(02|03|10|15|19)$       the fondo de cesantias code table, quoted verbatim
  ^(CC|CE|TI|PA|CD|SC|PE|PT)$  the identity-document code table, verbatim
  ^E\d\d$                 NOT official codes. Mercans working identifiers
                          for the portal-keyed planilla envelope (E01-E11) and
                          for the inbound confirmation values (E90-E93).
  ^MA0[1-5]$              Mercans working identifiers for the monthly-advance
                          variant, which has no published layout at all.
  ^IN0[1-3]$              Mercans working identifiers for the interest
                          computation, which is paid to the employee and is
                          not part of this file. Every E / MA / IN row says
                          DERIVED or DRAFT in column T.
"""

from build_co_specs import RA, R_NONE
from co_scope_common import SCOPE_WHO, SCOPE_TIMING

# ---------------------------------------------------------------------------
#  ROUNDING - a fourth Colombian convention, and it is NOT the PILA one
# ---------------------------------------------------------------------------
R_CES = ("Whole Colombian pesos. No decimals, no thousand separators, no sign. The published layout "
         "gives amount fields 9 integer positions, right-aligned and zero-filled, with a 4-position "
         "zero filler in front of each. Round the computed liquidation to the peso - do NOT round up "
         "to the next 100 as PILA requires (Decreto 1990 de 2016 art. 1 governs contributions, not "
         "the cesantias deposit), and do NOT round to the nearest 1,000 as Formulario 350 requires "
         "(ET art. 577). Blending the three conventions is the classic Colombian defect.")

DERIVED = ("DERIVED - not a field of the published detail layout. Mercans working identifier for a "
           "value the channel captures at planilla level, computes, or returns.")

DRAFT = ("DRAFT NORM, NOT IN FORCE as at 4 September 2026. MinTrabajo draft decree amending Decreto "
         "1072 de 2015 (proyecto_decreto_cesantias_2026.pdf). Build the field, leave the feature "
         "switched OFF until the decree is published AND the MinSalud PILA regulation exists.")

SRC_SIMPLE = ("Simple S.A. 'Manual Cesantias', s. 3.2, published fixed-width layout "
              "(_txt/pagosimple_cesantias.txt).")
SRC_SIMPLE_XLS = ("Simple S.A. 'Manual Cesantias', s. 3.1, published XLS 97-2003 layout "
                  "(_txt/pagosimple_cesantias.txt).")
SRC_SOI = ("ACH Colombia S.A. (SOI) 'Instructivo para elaboracion de planilla Cesantias' v2, code "
           "DDS-DES-INS-008 (_txt/soi_cesantias.txt).")


def F(en, es, rec, pos, mand, cond, posfile, length, fmt, ex, mapping, expl,
      rel, opts, rnd, neg, vt, freq, q, ra, kind):
    """21 columns A-U plus the row-colour kind. Column E is derived by the
    orchestrator from column L, so it is passed empty."""
    return [en, es, rec, pos, "", mand, cond, posfile, length, fmt, ex, mapping,
            expl, rel, opts, rnd, neg, vt, freq, q, ra, kind]


def T(num, en, es, ini, fin, length, typ, xls, ex, mapping, expl, mand="Y", cond="",
      opts="-", kind="payroll", vt="Amount", rnd=None, q=None, fmt=None):
    """A campo of the published 20-field / 258-position fixed-width detail record."""
    return F(en, es, "Registro de detalle (tipo 02)", "T%02d" % num, mand, cond,
             "TXT positions %d-%d | XLS column %s" % (ini, fin, xls),
             str(length), fmt or ("%s (%d)" % (typ, length)), ex, mapping, expl,
             "Y", opts, rnd or (R_CES if vt == "Amount" else R_NONE), "N", vt,
             "Per employee, per accrual year", q or SRC_SIMPLE, RA, kind)


def E(num, en, es, ex, mapping, expl, mand="Y", cond="", opts="-", kind="system",
      vt="Code", rnd=None, q=None, fmt="AN", length="-",
      rec="Cabecera de planilla (portal)"):
    """A planilla-envelope value keyed in the portal, not carried in the detail file."""
    return F(en, es, rec, "E%02d" % num, mand, cond,
             "Not in the detail file - keyed in the portal / returned by it",
             length, fmt, ex, mapping, expl, "Y", opts, rnd or R_NONE, "N", vt,
             "Per planilla", q or (DERIVED + " " + SRC_SOI), RA, kind)


FIELDS = [

    # =====================================================================
    "PLANILLA ENVELOPE - KEYED IN THE OPERATOR PORTAL, NOT IN THE DETAIL FILE",
    # =====================================================================
    E(1, "Contributor document type and number", "Tipo y numero de documento del aportante",
      "NI / 9001234567", "Company.Document_Type + Company.Document_Number",
      "COMPOSITE FIELD. The employer authenticates to the operador de informacion with the pair "
      "(document type, document number) plus a user document pair and a password; the aportante "
      "identity is then taken from the operator's registration record, not re-keyed per planilla. "
      "Composite Key: sub-field 1 = document type (NI for a legal person); sub-field 2 = the NIT "
      "without the check digit, without dots and without hyphens. PERSISTENCE: fixed for the life of "
      "the legal entity; it must be the SAME NIT used on the PILA planilla and on Formulario 350, "
      "because Simple S.A. offers to seed the cesantias planilla from the last PILA planilla paid "
      "for the selected year and the seed matches on this pair.",
      vt="Identifier", length="2 + 16"),
    E(2, "Service to be settled", "Servicio a liquidar", "Cesantias", "Constant",
      "A constant for this filing. The operator portals treat cesantias as one of the Pagos "
      "Complementarios a la Seguridad Social (PCSS) services and it is selected explicitly; "
      "selecting the wrong service produces a PILA planilla, not a cesantias planilla.",
      kind="const", opts="-> Sheet 6: Servicio PCSS"),
    E(3, "Accrual year of the severance savings", "Ano causado de cesantias", "2026",
      "Mercans.Cesantias_Accrual_Year",
      "THE PERIOD OF THIS FILING IS A YEAR, NOT A MONTH. This is the single most important "
      "structural difference from every other Colombian payroll filing: the nomina electronica, "
      "Formulario 350 and PILA are monthly and keyed to a payment date, whereas the cesantias "
      "planilla is keyed to the accrual YEAR that closed on 31 December and is paid in the "
      "FOLLOWING February. A planilla built in February 2027 carries ano causado = 2026.",
      vt="Date", fmt="AAAA (4)", length="4"),
    E(4, "Affiliation type of the planilla", "Tipo de afiliacion de la planilla", "Dependiente",
      "Constant for employer payroll",
      "Three values exist - Agremiado (contributions for associated or unionised independents), "
      "Dependiente (contributions arising from an employment contract, payroll-deducted) and "
      "Independiente (a natural person contributing for themselves). For an employer filing this "
      "return it is ALWAYS Dependiente. The values offered depend on the aportante type under which "
      "the employer registered on the platform.",
      kind="const", opts="-> Sheet 6: Tipo de afiliacion"),
    E(5, "Payment method", "Medio de pago", "PSE", "Mercans.Payment_Channel_Config",
      "Selected before the detail is loaded, because it changes the OUTPUT: SOI records that where "
      "the medio de pago is Pago Credito the system issues ONE PLANILLA NUMBER PER ADMINISTRADORA "
      "contained in the settlement, whereas an electronic payment (PSE) yields a single planilla "
      "number. The engine's reconciliation must therefore expect either one or many planilla "
      "numbers back for the same run. See E10.",
      cond="", opts="-> Sheet 6: Medio de pago"),
    E(6, "Planilla short name", "Nombre corto planilla", "CESANTIAS 2026 NOMINA MENSUAL",
      "Mercans.Planilla_Label",
      "Optional free-text label. Both operator manuals mark it optional. Use it to carry the run "
      "identifier so that the returned planilla number can be tied back to the payroll run without "
      "relying on the portal's own chronology.",
      mand="N", vt="Text"),
    E(7, "Single-fund-for-all indicator and selected fund",
      "Indicador de fondo unico para todos los empleados y fondo seleccionado", "N",
      "Mercans.Cesantias_Single_Fund_Flag + Employee.Cesantias_Fund_Code",
      "CONDITIONAL PAIR. Simple S.A. asks 'Deseas que las cesantias de todos los empleados "
      "incluidos en esta planilla sean enviadas a un solo fondo de cesantias?'. Answering YES "
      "overwrites the per-employee fund with one value for the whole planilla. For a real employer "
      "the answer is almost always NO, because the fund is the EMPLOYEE'S statutory choice (Ley 50 "
      "de 1990 art. 99 num. 3: 'en el fondo de cesantia que el mismo elija'). Answering YES to save "
      "keystrokes deposits other people's money into the wrong fund and does not discharge the "
      "obligation. Set to N and let T09 carry the per-employee value.",
      mand="C", cond="If = Y the value of T09 (Codigo del Fondo de Cesantias) is IGNORED for every "
                     "record and replaced by the single fund selected here. If = N, T09 governs. "
                     "See T09, whose Conditional Reason back-references this field.",
      vt="Flag", length="1"),
    E(8, "Seed-from-last-PILA-planilla indicator", "Indicador de generacion a partir de la ultima PILA",
      "N", "Mercans.Cesantias_Seed_From_PILA_Flag",
      "Simple S.A. offers to build the cesantias planilla from the contributor list of the last PILA "
      "planilla paid for the chosen year. Convenient and dangerous: the PILA population is the "
      "population that was PAID in a month, which is not the population ENTITLED to a cesantias "
      "deposit for the year - leavers who left in June are absent from the December PILA but are "
      "still owed a pro rata deposit, and salario integral employees are present in PILA but owed "
      "nothing. The engine must generate the population itself and set this to N.",
      vt="Flag", length="1"),
    E(9, "Asofondos name-validation auto-adjust answer",
      "Respuesta al ajuste automatico de validacion Asofondos", "NO",
      "Mercans.Asofondos_Autoadjust_Answer",
      "BOTH operators validate the surnames and names in the planilla against the affiliate base "
      "that ASOFONDOS delivers to the operadores de informacion ANNUALLY, and present a downloadable "
      "Excel difference report. Answering SI replaces the employer's values with the Asofondos "
      "values; answering NO keeps the employer's values. Answer NO and investigate: a mismatch is "
      "usually either a genuine misspelling in payroll master data (fix it at source, it will also "
      "be wrong on Formulario 220 and Formato 2276) or an affiliate whose fund record is stale. "
      "Silently accepting SI hides a master-data defect that recurs every year.",
      mand="C", cond="Presented only where the validation returns at least one difference. Where the "
                     "report is empty the question is not asked. Depends on T05, T06, T07 and T08, "
                     "which are the values validated; each of those back-references this field.",
      vt="Flag", length="2", opts="-> Sheet 6: Respuesta validacion Asofondos"),
    E(10, "Planilla number assigned by the operator", "Numero de planilla asignado", "1234567890",
      "Mercans.Cesantias_Planilla_Number (stored on return)",
      "OUTPUT, not input. Assigned when the settlement is finalised and printed on the pre-payment "
      "comprobante PDF. Store it per run - and note the cardinality trap in E05: with Pago Credito "
      "there is one number PER FONDO, so the store must be one-to-many. This number is the key for "
      "the later planilla recovery, the per-fund and per-affiliate reports and the audit trail that "
      "evidences compliance with the February deadline.",
      mand="N", vt="Identifier", length="10"),
    E(11, "Total value payable in the planilla", "Valor total a pagar de la planilla", "2000000",
      "Mercans.Cesantias_Planilla_Total (control total)",
      "CONTROL TOTAL. Displayed on the settlement summary and on the comprobante. It must equal the "
      "sum of T14 across the detail records of the planilla; where the medio de pago splits the "
      "planilla per fondo, the sum of the per-fondo totals must equal the run total. This is the "
      "only arithmetic check the channel gives you - there is no header record in the file carrying "
      "a declared total, so a truncated upload is NOT self-detecting. Compare the returned total "
      "against the engine's own sum before paying.",
      mand="N", rnd=R_CES, vt="Amount"),

    # =====================================================================
    "DETAIL RECORD - IDENTIFICATION (published layout, campos 1 to 8)",
    # =====================================================================
    T(1, "Record type", "Tipo de registro", 1, 2, 2, "N", "not present", "02", "Constant",
      "Campo obligatorio, siempre debe ser 02. A CONSTANT, quoted verbatim from the published "
      "layout: every detail line of the unified cesantias file is a type-02 record. There is no "
      "type-01 header record and no trailer record in this layout - the aportante data and the "
      "period live in the portal envelope (E01 to E06), not in the file. Consequence: the file has "
      "NO declared record count and NO declared control total, so the engine must reconcile the "
      "returned planilla total (E11) against its own sum.",
      kind="const", vt="Code", fmt="N (2) - constant '02'"),
    T(2, "Sequence number", "Secuencia", 3, 7, 5, "N", "not present", "00001",
      "Mercans.Record_Sequence",
      "Campo obligatorio where the data are uploaded as a flat file. Must START AT 00001 and be "
      "consecutive for the remaining records. Zero-padded to 5 positions, so the layout admits at "
      "most 99,999 employees in one planilla. Composite Key: positions 1-7 of every line are the "
      "record key - positions 1-2 the constant '02' and positions 3-7 the sequence - and the "
      "operator's structure validation reads them first, so an off-by-one sequence rejects the whole "
      "file before any content is validated.",
      kind="system", vt="Code", fmt="N (5) zero-padded, starts at 00001"),
    T(3, "Contributor document type", "Tipo de documento del cotizante", 8, 9, 2, "A", "A", "CC",
      "Employee.Document_Type",
      "ALPHABETIC two-character code, validated against the list printed in the layout: CC, CE, TI, "
      "PA, CD, SC, PE - and, in the XLS variant of the SAME manual, also PT (Permiso temporal). "
      "THIS IS NOT THE PILA CODE SET: PILA Registro Tipo 2 campo 3 uses the same two-letter "
      "mnemonics but a different admitted list, and Formulario 220 / Formato 2276 use DIAN NUMERIC "
      "document-type codes. The engine must hold one document type and three mappers. Note the "
      "SOI-documented length trap: where the document is a Permiso Especial de Permanencia the "
      "NUMBER (T04) must be exactly 15 digits.",
      vt="Code", opts="-> Sheet 6: Tipo de documento (cesantias)",
      cond="Determines the validation applied to T04 (length, and the PEP 15-digit rule). T04 "
           "back-references this field."),
    T(4, "Contributor identification number", "Numero de identificacion del cotizante", 10, 25, 16,
      "N", "B", "0000001020304050", "Employee.Document_Number",
      "Obligatorio. RIGHT-ALIGNED, ZERO-FILLED to 16 positions - this is the only field in the "
      "layout with an explicit alignment rule and it is the one most often got wrong, because the "
      "XLS variant of the same layout takes the number LEFT-aligned with a 15-character maximum. "
      "Composite Key: together with T03 this pair is the join key for the employee across every "
      "Colombian artefact - nomina electronica NIE044/NIE045, PILA Registro Tipo 2 campos 3 and 4, "
      "Formulario 220 casillas 24/25, Formato 2276 numeral 2 - and it is also the key the operator "
      "uses to match the Asofondos affiliate base. Strip dots, commas, spaces and hyphens before "
      "padding. PERSISTENCE: stable for life except on a document-type change (TI to CC on reaching "
      "majority, PEP/PPT to CE on regularisation), which must be notified to the fund, or the "
      "deposit lands on an orphan account.",
      vt="Identifier", fmt="N (16) right-aligned, zero-filled",
      cond="Length and content validation depend on T03 (document type); a Permiso Especial de "
           "Permanencia must be exactly 15 digits. T03 back-references this field."),
    T(5, "First surname", "Primer apellido", 26, 45, 20, "A", "C", "PEREZ",
      "Employee.First_Surname",
      "Obligatorio, supplied by the aportante. Left-aligned, space-filled to 20. Validated against "
      "the ASOFONDOS affiliate base (see E09) - a difference does not reject the file but raises a "
      "difference report the employer must answer SI or NO to. Strip accents and the special "
      "characters the operators reject; do not truncate silently, because a truncated surname "
      "produces a mismatch against the fund's record every single year.",
      vt="Text", rnd=R_NONE,
      cond="Validated as a SET with T06, T07 and T08 against the Asofondos base; the answer is "
           "given once, in E09, for the whole planilla. E09 back-references this field."),
    T(6, "Second surname", "Segundo apellido", 46, 65, 20, "A", "D", "GOMEZ",
      "Employee.Second_Surname",
      "Supplied by the aportante; the published layout does NOT mark it obligatorio, and the XLS "
      "variant states 'Campo Opcional - Hasta 20 caracteres'. Space-fill the whole 20 positions "
      "where the person has no second surname - do NOT shift the following fields up, because the "
      "record is positional and the fund code at 106-107 would then be read out of the name.",
      mand="C", vt="Text", rnd=R_NONE,
      cond="Conditional on the person having a second surname; space-filled when absent. Validated "
           "as a SET with T05, T07 and T08 against the Asofondos base - see E09, which "
           "back-references this field."),
    T(7, "First name", "Primer nombre", 66, 85, 20, "A", "E", "JUAN", "Employee.First_Name",
      "Obligatorio, supplied by the aportante. Left-aligned, space-filled to 20. Both operators "
      "note that names are pre-loaded automatically from the Asofondos base held in their systems "
      "and are editable - which means the portal may DISPLAY a name the employer never sent.",
      vt="Text", rnd=R_NONE,
      cond="Validated as a SET with T05, T06 and T08 against the Asofondos base - see E09, which "
           "back-references this field."),
    T(8, "Second name", "Segundo nombre", 86, 105, 20, "A", "F", "CARLOS", "Employee.Other_Names",
      "Supplied by the aportante; not marked obligatorio, and the XLS variant states 'Campo "
      "Opcional'. Maps to the Data-Dictionary Other_Names field, which is the same field that feeds "
      "nomina electronica OtrosNombres and Formulario 220 - keep one source of truth.",
      mand="C", vt="Text", rnd=R_NONE,
      cond="Conditional on the person having a second name; space-filled when absent. Validated as "
           "a SET with T05, T06 and T07 against the Asofondos base - see E09, which back-references "
           "this field."),

    # =====================================================================
    "DETAIL RECORD - FUND, DAYS AND AMOUNTS (published layout, campos 9 to 14)",
    # =====================================================================
    T(9, "Severance-savings fund code of the affiliate",
      "Codigo del Fondo de Cesantias al que pertenece el afiliado", 106, 107, 2, "N", "G", "03",
      "Employee.Cesantias_Fund_Code",
      "Campo obligatorio, validated against the funds registered in the operator's system. The "
      "published layout admits exactly FIVE values and prints them: 02 Proteccion, 03 Porvenir, "
      "10 Colfondos, 15 Fondo Nacional del Ahorro (FNA), 19 Old Mutual (antes Skandia). STALE "
      "LABEL, LIVE CODE: code 19's printed label is out of date - the entity trades as Skandia "
      "again (Skandia Administradora de Fondos de Pensiones y Cesantias S.A., authorised by the "
      "Superintendencia Financiera in January 2025 as SKANDIA AFP-ACCAI S.A. under Ley 2381 de "
      "2024). Send the CODE, not the name. The fund is the EMPLOYEE'S choice under Ley 50 de 1990 "
      "art. 99 num. 3 and is master data on the employee, not a company default.",
      vt="Code", rnd=R_NONE, opts="-> Sheet 6: Codigo del Fondo de Cesantias",
      cond="IGNORED where E07 (single-fund indicator) = Y, in which case the planilla-level fund "
           "overwrites this value for every record. E07 back-references this field."),
    T(10, "Number of days worked", "Numero de dias trabajados", 108, 110, 3, "N", "H", "360",
      "Mercans.Cesantias_Days",
      "Obligatorio. Admits values from 1 to 360 - a 360-DAY COMMERCIAL YEAR, not 365. A full year "
      "of service is 360, and every partial year is the actual days of service counted on the "
      "commercial convention (each month 30 days). Include the days of paid leave and of "
      "employer-paid or institution-paid incapacity, which count as service. The 3-position field "
      "cannot carry more than one year, which is the layout's way of saying that this filing is "
      "strictly one accrual year per record.",
      vt="Amount", rnd=R_NONE, fmt="N (3), 1 to 360",
      cond="Feeds the auto-calculation of T14 together with T12; the layout's formula is "
           "salario basico * (dias trabajados / 360). T12 and T14 back-reference this field."),
    T(11, "Zero filler before the salary field", "Espacio con ceros (0)", 111, 114, 4, "N",
      "not present", "0000", "Constant",
      "Obligatorio - 'Debe contener ceros'. A four-position filler that exists only in the "
      "fixed-width variant; the XLS layout has no equivalent column. Read it together with campo "
      "14's note, which explains the intent: 'antes de cada valor deben ir 4 espacios (pueden ser "
      "rellenos con ceros o en blanco)'. In other words the two amount fields are really 13 "
      "positions each, of which the leading 4 must be zeros or blanks. Write ZEROS, not blanks - "
      "the campo-11 rule is categorical where the campo-14 note is permissive, and zeros satisfy "
      "both.",
      kind="const", vt="Code", rnd=R_NONE, fmt="N (4) - constant '0000'",
      cond="Immediately precedes T12 and is part of its 13-position amount frame; T12 "
           "back-references this field."),
    T(12, "Basic salary reported in the last month", "Salario basico reportado en el ultimo mes",
      115, 123, 9, "N", "I", "001750905", "Contract.Contractual_Salary (December of the accrual year)",
      "Obligatorio. Nine integers, no decimals, no commas, no points, not less than zero. The "
      "layout is explicit about WHICH salary: 'el ultimo salario basico reportado en el mes de "
      "diciembre del ano causado de cesantias'. THIS IS THE OPERATOR'S REPORTING FIELD, NOT THE "
      "STATUTORY BASE. CST art. 253 fixes the statutory base as the last monthly salary provided it "
      "has not varied in the last three months, otherwise the average of the last year of service "
      "(or of the whole period if shorter), INCLUDING the auxilio de transporte. The field name "
      "says 'basico' and the operator's calculator uses it alone - see the trap documented at T14. "
      "Report the December basic here and compute T14 yourself.",
      vt="Amount", fmt="N (9) whole pesos, zero-filled",
      cond="Framed by the T11 zero filler and feeds the auto-calculation of T14 with T10. T11 and "
           "T14 back-reference this field."),
    T(13, "Zero filler before the severance-savings value", "Espacio con ceros (0)", 124, 127, 4,
      "N", "not present", "0000", "Constant",
      "Obligatorio - 'Debe contener ceros'. The second four-position filler, framing the amount at "
      "128-136 exactly as T11 frames the amount at 115-123. Absent from the XLS layout. Write "
      "zeros.",
      kind="const", vt="Code", rnd=R_NONE, fmt="N (4) - constant '0000'",
      cond="Immediately precedes T14 and is part of its 13-position amount frame; T14 "
           "back-references this field."),
    T(14, "Value of the severance savings deposited", "Valor de las cesantias", 128, 136, 9, "N",
      "J", "002000000", "Mercans.Cesantias_Annual_Liquidation",
      "Obligatorio, nine integers. TWO RULES AND ONE TRAP. Rule one, the floor: 'el valor minimo "
      "del recaudo debe ser de un (1) dia de un (1) SMLMV del ano causado' - for accrual year 2026 "
      "one day of the SMMLV of COP 1,750,905 is COP 58,363.50, so a record below that is rejected. "
      "Rule two, the override: the layout's own formula is salario basico * (dias trabajados / 360) "
      "BUT 'en este campo el aportante puede especificar un valor diferente y no se haran calculos "
      "automaticos de este valor'. THE TRAP: the operator's formula omits the AUXILIO DE TRANSPORTE, "
      "which CST art. 253 requires in the base. For an employee on the 2026 minimum wage the "
      "operator would compute 1,750,905 while the statute requires (1,750,905 + 249,095) = "
      "2,000,000 - a shortfall of COP 249,095 that is a SHORT DEPOSIT, penalised at one day's "
      "salary for every day of delay under Ley 50 de 1990 art. 99 num. 3, uncapped. ALWAYS write "
      "the engine's own figure into this field and never rely on the portal calculator. Where the "
      "monthly advance regime of MA01 is in use, this field carries the CONSOLIDATED annual figure "
      "and only the difference computed at MA05 is actually deposited in February.",
      vt="Amount", fmt="N (9) whole pesos, zero-filled",
      cond="Framed by the T13 zero filler; auto-calculated from T10 and T12 if left blank, which "
           "must never be allowed. T10, T12 and T13 back-reference this field."),

    # =====================================================================
    "DETAIL RECORD - AFFILIATE CONTACT DATA (published layout, campos 15 to 20)",
    # =====================================================================
    T(15, "Employee residential address", "Direccion de residencia del empleado", 137, 186, 50,
      "CHAR", "K", "CALLE 26 NO 68-35 APTO 502", "Employee.Address",
      "The employee's residential address, 50 positions, left-aligned and space-filled. This is the "
      "AFFILIATE'S address for the fund's own statutory communications with its member, which is "
      "why the layout asks for the residence and not the work address - contrast nomina electronica "
      "and PILA, which carry the WORK municipality. Do not send the work address; the fund will "
      "post the member's statements to it. Composite Key: the affiliate's domicile is carried "
      "across THREE fields that must describe one place - T15 the free-text street address, T16 the "
      "two-digit DANE department and T17 the three-digit DANE municipality. Within T15 itself, "
      "Colombian addresses decompose as via type (CALLE / CARRERA / DIAGONAL / TRANSVERSAL), via "
      "number, the NO separator, the cross-via number, the hyphen, the door number and any "
      "complement (APTO / TORRE / INT). Abbreviate by a documented rule where the whole exceeds 50 "
      "positions - never cut mid-token, because the fund cannot repair a truncated address.",
      mand="C", vt="Text", rnd=R_NONE,
      cond="Should be consistent with T16 and T17 (the DANE department and municipality of the same "
           "address); those two fields back-reference this one."),
    T(16, "Department code (DANE)", "Codigo departamento", 187, 188, 2, "N", "L", "11",
      "Employee.Department_Code",
      "Two positions, per the DANE list. The DANE divipola code is hierarchical: the two-digit "
      "department prefix plus the three-digit municipality suffix form the five-digit municipality "
      "code (11 + 001 = 11001, Bogota D.C.). Composite Key: T16 and T17 must be written as the two "
      "halves of ONE divipola code, never picked from two different lists.",
      mand="C", vt="Code", rnd=R_NONE, opts="-> Sheet 6: Codigos DANE (referencia)",
      cond="Must be the department half of the same DANE divipola code whose municipality half is "
           "T17, and must correspond to the address in T15. T15 and T17 back-reference this field."),
    T(17, "Municipality code (DANE)", "Codigo municipio", 189, 191, 3, "N", "M", "001",
      "Employee.Municipality_Code",
      "Three positions, per the DANE list, and it is the SUFFIX only - not the five-digit code. "
      "Writing the full 11001 into a three-position field truncates to 110 and silently relocates "
      "the affiliate. Composite Key: see T16.",
      mand="C", vt="Code", rnd=R_NONE, opts="-> Sheet 6: Codigos DANE (referencia)",
      cond="Must be the municipality half of the same DANE divipola code whose department half is "
           "T16, and must correspond to the address in T15. T15 and T16 back-reference this field."),
    T(18, "Employee landline telephone", "Telefono fijo del empleado", 192, 198, 7, "N", "N",
      "6013456", "Employee.Phone",
      "'Solo admite 7 numeros' - exactly seven digits, so the field cannot carry a mobile number "
      "(10 digits in Colombia) nor a number written with the area code. Where only a mobile is held, "
      "the field must be zero- or space-filled rather than truncated; a truncated mobile is a "
      "wrong-number record on the fund's affiliate file.",
      mand="C", vt="Text", rnd=R_NONE,
      cond="Conditional on a 7-digit landline being held for the employee; filled with spaces or "
           "zeros where only a mobile number exists. Paired in the layout with T19 as the "
           "affiliate's contact block; T19 back-references this field."),
    T(19, "Employee e-mail address", "Correo electronico (E-mail) del empleado", 199, 248, 50,
      "CHAR", "O", "juan.perez@empresa.com.co", "Employee.Email",
      "Fifty positions. The layout prints its own validation: letters A-Z, digits 0-9, hyphen, "
      "underscore, apostrophe and full stop are admitted in the local part; the @ is the mandatory "
      "indicator; the domain may contain only letters, digits and the hyphen, and the hyphen may be "
      "neither the first nor the last character of the domain. Composite Key: local-part + '@' + "
      "domain; the operator validates the three parts separately, so an address that merely 'looks' "
      "valid can still be rejected on the domain rule.",
      mand="C", vt="Text", rnd=R_NONE,
      cond="Conditional on an e-mail being held. Paired in the layout with T18 as the affiliate's "
           "contact block; T18 back-references this field."),
    T(20, "Employee hire date", "Fecha de ingreso del empleado", 249, 258, 10, "N", "P",
      "2019-03-01", "Contract.Start_Date",
      "Format AAAA-MM-DD, ten positions INCLUDING the two hyphens - note that the published layout "
      "types this field N while its content is not purely numeric, so a strict numeric writer would "
      "emit 20190301 and shift nothing (the field is last) but would still fail the format "
      "validation. Composite Key: positions 249-252 year, 253 hyphen, 254-255 month, 256 hyphen, "
      "257-258 day. THIS IS THE HIRE DATE OF THE CONTRACT, NOT THE START OF THE ACCRUAL PERIOD: for "
      "an employee hired in 2019 and reported for accrual year 2026 the value is still 2019-03-01, "
      "while T10 carries 360 days. Sending the 1 January of the accrual year here is a common "
      "defect and it corrupts the fund's seniority record.",
      vt="Date", rnd=R_NONE, fmt="AAAA-MM-DD (10)"),

    # =====================================================================
    "MONTHLY ADVANCE DEPOSIT - Ley 2466 de 2025 art. 64 par. 1 (NOT YET OPERABLE)",
    # =====================================================================
    F("Written agreement for the monthly advance deposit",
      "Acuerdo escrito para la consignacion mensual anticipada",
      "Regimen simple laboral (no file field)", "MA01", "C",
      "Gates every other MA field: where this is N, MA02 to MA05 are not produced and the ordinary "
      "annual detail record (campos 1 to 20 of the published layout) is the only route. MA02, MA03, "
      "MA04 and MA05 each back-reference this field.",
      "Not in any published layout - engine-held configuration", "1", "Flag (Y/N)", "N",
      "Contract.Cesantias_Regime",
      "Ley 2466 de 2025 art. 64 added par. 1 to Ley 50 de 1990 art. 99 permitting the employer to "
      "deposit monthly, to the cesantias fund, 8.33% of the base. The statute grants the option to "
      "the EMPLOYER ('El empleador podra aportar mensualmente'); the MinTrabajo draft decree "
      "additionally requires the employee's agreement - draft art. 4 par. 2: 'constituye un "
      "mecanismo voluntario que podra ser adoptado por el empleador previo acuerdo con el "
      "trabajador, sin que sustituya el regimen legal de consignacion anual'. Hold the flag per "
      "contract, not per company. " + DRAFT,
      "Y", "-", R_NONE, "N", "Flag", "Per contract", DRAFT, RA, "system"),
    F("Monthly advance base", "Salario base de liquidacion mensual",
      "Regimen simple laboral (no file field)", "MA02", "C",
      "Produced only where MA01 = Y, that is only where a written monthly-advance agreement exists. "
      "Feeds MA03, which is 8.33% of this value, and is reconciled at year end against the "
      "statutory annual base through MA05. MA01, MA03 and MA05 back-reference this field.",
      "Not in any published layout - PILA field to be defined by MinSalud", "9",
      "N (whole pesos)", "2000000",
      "Mercans.Cesantias_Monthly_Advance_Base",
      "Ley 2466 art. 64 par. 1 defines the base VERBATIM as 'el salario base de liquidacion "
      "compuesto por el salario mensual sumado al auxilio de transporte en los casos en que a este "
      "hubiere lugar'. So, unlike the operator's annual calculator (see T14), the STATUTE for the "
      "monthly advance includes the transport allowance expressly. The draft decree adds the "
      "variable-salary rule: 'la consignacion mensual anticipada correspondera al 8,33% de lo "
      "devengado por el trabajador en el respectivo mes, adicionado con el auxilio de transporte "
      "cuando haya lugar'. " + DRAFT,
      "Y", "-", R_CES, "N", "Amount", "Per month", DRAFT, RA, "payroll"),
    F("Monthly advance amount at 8.33%", "Consignacion mensual anticipada del 8,33%",
      "Regimen simple laboral (no file field)", "MA03", "C",
      "Produced only where MA01 = Y and computed from MA02. MA01 and MA02 back-reference this "
      "field; MA05 consumes the accumulated total.",
      "Not in any published layout - PILA field to be defined by MinSalud", "9",
      "N (whole pesos)", "166600",
      "Mercans.Cesantias_Monthly_Advance_Amount",
      "8.33% of MA02. Note that 8.33% is an APPROXIMATION of one twelfth (8.3333...%), so twelve "
      "monthly advances do NOT reconcile exactly to one twelfth-based annual liquidation: on a "
      "2,000,000 base, 12 x 166,600 = 1,999,200 against an annual entitlement of 2,000,000, a "
      "shortfall of 800 pesos. The statute fixes the rate at 8.33% and the draft decree requires "
      "the year-end consolidation to absorb the difference (see MA05) - so the residual is expected "
      "and must be paid, not written off. " + DRAFT,
      "Y", "-", R_CES, "N", "Amount", "Per month", DRAFT, RA, "payroll"),
    F("PILA contribution type for the cesantias advance",
      "Tipo de cotizacion PILA para la consignacion anticipada",
      "Regimen simple laboral (no file field)", "MA04", "C",
      "Produced only where MA01 = Y. Depends on a MinSalud regulation that does not yet exist. "
      "MA01 back-references this field.",
      "PILA - position not yet defined by MinSalud",
      "Not yet fixed", "Numeric contribution-type code, width not yet published",
      "Not yet issued",
      "Mercans.PILA_Cesantias_Contribution_Type",
      "THE CHANNEL FOR THE MONTHLY ADVANCE IS NOT THIS FILING - IT IS PILA. Ley 2466 art. 64 par. 1 "
      "instructs MinSalud to regulate the PILA accordingly, and the draft decree makes the point "
      "twice: the advance is paid 'exclusivamente a traves de la Planilla Integrada de Liquidacion "
      "de Aportes -PILA-' (draft art. 4 par. 3) and 'debera reportarse en la PILA como aportes al "
      "sistema de cesantias mediante el tipo de cotizacion que defina el Ministerio de Salud y "
      "Proteccion Social' (draft art. 1 par. 2). The same paragraph gives MinSalud SIX MONTHS from "
      "the decree's entry into force to adjust PILA, and the funds and operadores de informacion a "
      "FURTHER SIX MONTHS from that regulation to build. As at 4 September 2026 the decree is a "
      "draft and no PILA contribution type exists, so the feature cannot be switched on and the "
      "annual planilla remains the only lawful route. " + DRAFT,
      "Y", "-", R_NONE, "N", "Code", "Per month", DRAFT, RA, "na"),
    F("Year-end consolidation adjustment", "Consolidacion definitiva y ajustes al cierre anual",
      "Regimen simple laboral (no file field)", "MA05", "C",
      "Produced only where MA01 = Y; it is the reconciling item between the sum of MA03, whose base "
      "is MA02, and the statutory annual liquidation in T14. MA01, MA02 and MA03 back-reference "
      "this field; T14 carries the consolidated figure.",
      "Feeds T14 of the annual planilla", "9", "N (whole pesos, may be nil)", "800",
      "Mercans.Cesantias_Consolidation_Adjustment",
      "THE MONTHLY ADVANCE DOES NOT REPLACE THE ANNUAL LIQUIDATION. Draft art. 1 par. 1 is "
      "categorical: 'al cierre del respectivo periodo anual, el empleador debera efectuar la "
      "consolidacion definitiva del auxilio de cesantia con base en el promedio de lo devengado en "
      "el ultimo ano de servicio ... y realizar los ajustes a que haya lugar. Lo anterior sin que "
      "ello implique pago anticipado, parcial o fraccionado del auxilio de cesantia, el cual se "
      "entendera consolidado unicamente al cierre del respectivo periodo anual'. And draft art. 4 "
      "par. 4 preserves the deadline while relaxing the monthly rhythm: 'La omision de uno o varios "
      "pagos mensuales no configurara mora, siempre que se complete el valor total anual a mas "
      "tardar el 14 de febrero del ano siguiente, configurandose la mora a partir del 15 de "
      "febrero'. So the engine must still run the annual liquidation, compare it with the sum of "
      "the advances, and deposit the difference by the February deadline. " + DRAFT,
      "Y", "-", R_CES, "Y", "Amount", "Per accrual year", DRAFT, RA, "payroll"),

    # =====================================================================
    "INTEREST ON SEVERANCE SAVINGS - PAID TO THE EMPLOYEE, NEVER TO THE FUND",
    # =====================================================================
    F("31 December severance-savings balance", "Saldo de cesantias al 31 de diciembre",
      "Interes de cesantias (not a file field)", "IN01", "N",
      "Not conditional. Feeds IN02 and IN03.",
      "NOT in this filing - engine output, evidenced to the employee", "-", "N (whole pesos)",
      "2000000", "Mercans.Cesantias_YearEnd_Balance",
      "The balance in the employee's favour at 31 December, or at the date of definitive withdrawal "
      "or partial settlement. It is the base of the Ley 52 de 1975 art. 1 interest. Deliberately "
      "shown on this Spec as a NOT-APPLICABLE row: it is not a field of the cesantias planilla, but "
      "it is computed from the same liquidation and the two are routinely confused.",
      "Y", "-", R_CES, "N", "Amount", "Per accrual year", "Ley 52 de 1975 art. 1; CCG Module 9.",
      RA, "na"),
    F("Annual interest on severance savings at 12%", "Intereses de cesantias del 12% anual",
      "Interes de cesantias (not a file field)", "IN02", "N",
      "Not conditional. Computed from IN01. IN03 is the monthly alternative to this field.",
      "NOT in this filing - paid directly to the employee", "-", "N (whole pesos)", "240000",
      "Mercans.Cesantias_Interest_Annual",
      "12% per annum on the IN01 balance, pro-rated on days over 360. PAID TO THE EMPLOYEE "
      "DIRECTLY, IN THE MONTH OF JANUARY of the following year - not to the fund, and not in "
      "February. The two obligations have different payees, different deadlines and different "
      "penalties: failure to deposit the principal costs one day's salary per day of delay, whereas "
      "failure to pay the interest costs an indemnity equal to the interest owed, ONCE ONLY (Ley 52 "
      "de 1975 art. 1). The draft decree would add a further precision at art. 4: the interest is "
      "'entregado directamente al trabajador dentro del mes siguiente a la fecha de liquidacion del "
      "auxilio de cesantia'. No interest on interest may be liquidated.",
      "Y", "-", R_CES, "N", "Amount", "Per accrual year",
      "Ley 52 de 1975 art. 1; Decreto 1072 de 2015 arts. 2.2.1.3.4 and 2.2.1.3.5.", RA, "na"),
    F("Monthly interest option at 1%", "Mensualizacion de intereses del 1%",
      "Interes de cesantias (not a file field)", "IN03", "C",
      "Available only where a WRITTEN agreement exists between employer and employee; it replaces "
      "the January payment of IN02 with twelve monthly payments. IN02 back-references this field.",
      "NOT in this filing - paid directly to the employee", "-", "N (whole pesos)", "20000",
      "Mercans.Cesantias_Interest_Monthly",
      "Ley 2466 de 2025 art. 64 par. 2, verbatim: 'Las partes podran acordar por escrito la "
      "mensualizacion de los intereses sobre las cesantias, pagando al trabajador el 1% del salario "
      "base de liquidacion compuesto por el salario mensual sumado al auxilio de transporte en los "
      "casos en que a este hubiere lugar'. Three engine consequences. First, it needs a written "
      "agreement, so the flag is per contract. Second, the base is the SAME monthly base as MA02 "
      "(salary + transport allowance), not the accumulated balance - so the monthly route and the "
      "annual route give different figures and the draft decree confirms the 1% monthly "
      "'correspondiente al doce por ciento (12%) anual previsto en la ley'. Third, the draft decree "
      "sets the payment window: 'dentro del mes calendario siguiente al de su causacion'. " + DRAFT,
      "Y", "-", R_CES, "N", "Amount", "Per month",
      "Ley 2466 de 2025 art. 64 par. 2 (in force); " + DRAFT, RA, "na"),

    # =====================================================================
    "INBOUND - DEPOSIT CONFIRMATION AND COMPLIANCE EVIDENCE (CO-IN-CESANTIAS-CONFIRMATION)",
    # =====================================================================
    E(90, "Planilla payment date", "Fecha de pago de la planilla", "2027-02-10",
      "Mercans.Cesantias_Payment_Date (stored on return)",
      "INBOUND. The date the planilla was actually PAID, which is the date that matters for the "
      "deadline - not the date the planilla was built. Both operators separate settlement from "
      "payment: the planilla is liquidated, a pre-payment comprobante is issued, and payment then "
      "follows by PSE or by credit. A planilla liquidated on 13 February and paid on 17 February is "
      "LATE. Store the payment date, not the liquidation date, as the compliance evidence. Composite "
      "Key: AAAA-MM-DD - positions 1-4 the year, 5 the hyphen, 6-7 the month, 8 the hyphen, 9-10 "
      "the day; the same 10-character date frame as T20, and the pair (E10 planilla number, E90 "
      "payment date) is the key of the compliance evidence held per accrual year.",
      mand="N", vt="Date", fmt="AAAA-MM-DD", length="10", kind="system", rec="Confirmacion de consignacion (entrante)"),
    E(91, "Deposit compliance status per employee",
      "Estado de cumplimiento de la consignacion por empleado", "ON TIME",
      "Mercans.Cesantias_Deposit_Status",
      "INBOUND / DERIVED. Per employee and per accrual year, one of ON TIME, LATE (with the day "
      "count), SHORT (with the shortfall) or DISCHARGED BY DIRECT PAYMENT. This is the field that "
      "quantifies the exposure, because the Ley 50 de 1990 art. 99 num. 3 penalty is one day's "
      "salary for EACH DAY of delay, PER EMPLOYEE, and uncapped - on 100 minimum-wage employees a "
      "fortnight's delay is of the order of COP 81.7 million. Recompute it from E90 against the "
      "deadline in the Report Matrix, and hold it for the employee's three-year limitation period "
      "(CST art. 488 as substituted by Ley 2466 de 2025 art. 62). Where E92 records a discharge by "
      "proven direct payment, set this field to DISCHARGED BY DIRECT PAYMENT instead of deriving it "
      "from E90 - see E92.",
      mand="N", vt="Code", opts="-> Sheet 6: Estado de cumplimiento", kind="system", rec="Confirmacion de consignacion (entrante)"),
    E(92, "Direct-payment discharge evidence", "Prueba del pago directo liberatorio", "N",
      "Mercans.Cesantias_Direct_Payment_Flag",
      "CST art. 57 par. 4, added by Ley 2466 de 2025 art. 15, verbatim: 'Cuando el empleador "
      "acredite de manera fehaciente el pago directo al trabajador del valor correspondiente a las "
      "cesantias, dicho pago se considerara liberatorio de la obligacion, y no procedera sancion "
      "por no consignacion, salvo que se demuestre que el pago no se realizo en condiciones de "
      "libertad y que no fue utilizado en fines autorizados por la ley. No obstante, la afiliacion "
      "a Fondo de Cesantias es obligatoria.' Three limits the engine must respect: the discharge "
      "needs FEHACIENTE evidence, it is rebuttable on the freedom-and-purpose test, and it does NOT "
      "remove the duty to affiliate the employee to a fund. A DRAFTING NOTE on the citation: art. "
      "15's enacting formula announces only 'los paragrafos 2 y 3' of CST art. 57, yet the "
      "published text prints a Paragrafo 4 and this is it - so cite CST art. 57 par. 4 as added by "
      "Ley 2466 de 2025 art. 15, and expect the discrepancy to be raised.",
      mand="C", cond="Where = Y, no annual detail record is produced for that employee (campos 1 "
                     "to 20 of the published layout are not written) and E91 is set to DISCHARGED "
                     "BY DIRECT PAYMENT. E91 back-references this field.",
      vt="Flag", length="1", kind="system", rec="Confirmacion de consignacion (entrante)"),
    E(93, "Fund deposit certificate", "Certificado de consignacion del fondo", "PDF / Excel",
      "Mercans.Cesantias_Fund_Certificate_Ref",
      "INBOUND. Both operators issue reports after payment - por fondo, por afiliado and a "
      "consolidated informe completo, in PDF or Excel - and the fund itself issues the deposit "
      "certificate. CCG Module 10 records that the certificate is issued by the FUND but the "
      "EMPLOYER must be able to evidence it. Store the reference against E10 and E90; it is the "
      "primary evidence in a claim, and the employee's claim period runs three years.",
      mand="N", vt="Text", kind="system", rec="Confirmacion de consignacion (entrante)"),
]


CFG = {
    "doc_id": "CO-CESANTIAS-006",
    "filing_id": "CO-CESANTIAS-DEPOSIT-ANNUAL-006",
    "name_en": "Annual Severance-Savings Deposit to the Employee's Chosen Fund",
    "name_es": "Consignacion anual de cesantias al fondo de cesantias elegido por el trabajador",
    "spec_sheet": "Consignacion Cesantias Spec",
    "authority_full": "Fondos de Cesantias (Proteccion, Porvenir, Colfondos, Skandia and the "
                      "state-owned Fondo Nacional del Ahorro), reached through a licensed operador "
                      "de informacion. NOT a government authority - this is the only one of the six "
                      "in-scope Colombian filings whose recipient is a private administrator, which "
                      "is why no government schema exists for it.",
    "frequency": "Annual - one record per employee per accrual year, liquidated at 31 December and "
                 "deposited in the following February. Optionally supplemented by a monthly advance "
                 "deposit through PILA (Ley 2466 de 2025 art. 64 par. 1), which is NOT yet operable.",
    "due_date": "BEFORE 15 FEBRUARY of the year following the 31 December liquidation - Ley 50 de "
                "1990 art. 99 num. 3, verbatim: 'El valor liquidado por concepto de cesantia se "
                "consignara antes del 15 de febrero del ano siguiente, en cuenta individual a "
                "nombre del trabajador en el fondo de cesantia que el mismo elija'. The last "
                "compliant day is therefore 14 February, and the MinTrabajo draft decree confirms "
                "the same boundary from the other side: 'configurandose la mora a partir del 15 de "
                "febrero'. NON-BUSINESS-DAY SHIFT - TO CONFIRM: where 14 February falls on a "
                "Saturday, Sunday or holiday, Colombian practice moves the last day to the next "
                "business day, and for accrual year 2025 (14 February 2026 = Saturday) the shift to "
                "Monday 16 February 2026 was reported uniformly by El Tiempo, El Pais, Infobae and "
                "Cronista. No MinTrabajo concepto or Ministry circular stating the rule was located, "
                "so it rests on the general term rule and press consensus. FOR ACCRUAL YEAR 2026 THE "
                "LAST DAY IS SUNDAY 14 FEBRUARY 2027, which on the same reasoning shifts to Monday "
                "15 February 2027 - but 15 February is also the first day of mora on the literal "
                "text, so DO NOT RELY ON THE SHIFT: deposit by Friday 12 February 2027. The penalty "
                "for getting this wrong is one day's salary per day of delay, per employee, uncapped.",
    "submission": "PORTAL, TWO CHANNELS, THROUGH A LICENSED OPERADOR DE INFORMACION - not to a "
                  "government portal. Channel A, online_form: 'Planilla En Linea' / 'Elaborar "
                  "planilla', keying each employee into the operator's form. Channel B, file_upload: "
                  "'Liquidacion Por Archivo' / 'Envio de Archivo Unificado de Cesantias', uploading "
                  "an employer-generated file. Payment then follows by PSE or by credit, and the "
                  "operator returns a planilla number and a comprobante PDF. Verified independently "
                  "in the published manuals of two operators - ACH Colombia S.A. (SOI), "
                  "www.nuevosoi.com.co, instructivo DDS-DES-INS-008 v2, and Simple S.A., "
                  "www.pagosimple.com, 'Manual Cesantias'. This is NOT machine-to-machine: there is "
                  "no XSD, no SOAP service, no document signature and no certificate authentication.",
    "file_format": "For channel B, TWO PUBLISHED LAYOUTS, both without a header row: (1) FIXED-WIDTH "
                   "TXT - 20 fields in 258 positions, record type constant '02', 5-position "
                   "sequence, byte-exact Inicial-Final positions; (2) EXCEL 97-2003 .XLS - 16 "
                   "columns A to P, data from the first row, all records on one sheet. SOI states "
                   ".txt and .csv are accepted and that a file above 1 MB must be compressed before "
                   "upload. NO XML AND NO XSD EXISTS for this filing - the word XML must not appear "
                   "against it. Amounts are whole pesos, right-aligned and zero-filled, with a "
                   "4-position zero filler in front of each amount. NOTE that scope_manifest records "
                   "the format as CSV: CSV is accepted, but the published field-level layouts are "
                   "the fixed-width TXT and the XLS, and this Spec is written to those.",
    "legal_basis": "Ley 50 de 1990 art. 99 nums. 1-3 (the annual liquidation at 31 December, the "
                   "employee's choice of fund, the deposit before 15 February and the one-day's-"
                   "salary-per-day-of-delay penalty), as added to by Ley 2466 de 2025 art. 64 (pars. "
                   "1 and 2: the 8.33% monthly advance deposit and the 1% monthly interest option); "
                   "CST (Decreto 2663 de 1950) arts. 249 (the entitlement), 250 (loss of the right), "
                   "253 (the base), 254 (prohibition of partial payment), 310 (construction workers, "
                   "3 days per completed month); CST art. 57 par. 4 as added by Ley 2466 de 2025 "
                   "art. 15 (direct payment is discharging, affiliation still compulsory); Ley 52 de "
                   "1975 art. 1 (12% interest, paid to the employee in January); Decreto 1072 de "
                   "2015 arts. 2.2.1.3.1, 2.2.1.3.4, 2.2.1.3.5 and 2.2.1.3.13 (the current "
                   "regulation, and the four articles the 2026 MinTrabajo draft decree would amend); "
                   "CST art. 488 as substituted by Ley 2466 de 2025 art. 62 (three-year limitation); "
                   "ET arts. 206 num. 4 and 385-386 (the tax treatment, which lives on Formulario "
                   "220 and Formato 2276, not here); Decreto 1469 de 2025 (SMMLV 2026 = COP "
                   "1,750,905 and transport allowance = COP 249,095, which set both the base and the "
                   "minimum-recaudo validation).",
    "accuracy": "88% (PRIMARY for the obligation, PRIMARY for a published field layout, DERIVED for "
                "per-fund variation). What is byte-exact: the 20-field / 258-position fixed-width "
                "layout and the 16-column XLS layout, taken from the published Simple S.A. 'Manual "
                "Cesantias' sections 3.1 and 3.2 - every position, length, type, validation rule, "
                "the five-value fondo code table and the eight-value document-type table are "
                "transcribed, not derived. That is a material improvement on scope_manifest, which "
                "recorded this filing as having no published layout. The channel is confirmed "
                "independently by a second operator's published instructivo (ACH Colombia / SOI). "
                "The law is verbatim from the local registry for Ley 2466 de 2025 arts. 15 and 64 "
                "and quoted verbatim for Ley 50 de 1990 art. 99 num. 3. WHAT WOULD RAISE IT: (a) "
                "the Fondo Nacional del Ahorro instructivo for private employers, whose published "
                "URL now 404s after the FNA site redesign - FNA is a state entity and its layout "
                "would be the one genuinely official schema; (b) a real filed planilla and its "
                "comprobante, to confirm that the other operadores de informacion accept the same "
                "258-position record rather than an operator-specific variant; (c) the MinSalud PILA "
                "regulation and the enacted decree, which would replace the whole MONTHLY ADVANCE "
                "section's DRAFT flags with real PILA positions. It would then reach 97%.",
    "source_status": "PRIMARY for the law: Ley 2466 de 2025 arts. 15 and 64 verbatim from "
                     "Ley_2466_de_2025.pdf via _txt/ley2466.txt; Ley 50 de 1990 art. 99 num. 3 and "
                     "Ley 52 de 1975 art. 1 quoted verbatim; CST arts. 249-254 and 310 from "
                     "Decreto_2663_de_1950.pdf; SMMLV and transport allowance from "
                     "Decreto-1469-de-2025-SMMLV-2026.pdf. PRIMARY for the field layout: Simple S.A. "
                     "'Manual Cesantias' ss. 3.1 and 3.2 (pagosimple_cesantias.pdf, extracted to "
                     "_txt/pagosimple_cesantias.txt) - 20 campos, 258 positions, all Inicial-Final "
                     "values arithmetically consistent (2+5+2+16+20+20+20+20+2+3+4+9+4+9+50+2+3+7+"
                     "50+10 = 258). PRIMARY for the channel: ACH Colombia S.A. (SOI) instructivo "
                     "DDS-DES-INS-008 v2 (soi_planilla_cesantias.pdf, extracted to "
                     "_txt/soi_cesantias.txt). DRAFT, NOT IN FORCE: MinTrabajo draft decree amending "
                     "Decreto 1072 de 2015 (proyecto_decreto_cesantias_2026.pdf, extracted to "
                     "_txt/proyecto_decreto_cesantias.txt) - every field it supports is flagged. "
                     "DERIVED: the planilla-envelope, monthly-advance, interest and confirmation "
                     "identifiers (E / MA / IN / CF prefixes), which are Mercans working identifiers "
                     "for values the channel captures or returns outside the published record.",
    "channel_notes": [
        "Channel: online_form AND file_upload (fixed-width TXT / XLS 97-2003 / CSV) | Portal: a "
        "licensed operador de informacion - ACH Colombia S.A. (SOI), www.nuevosoi.com.co, and "
        "Simple S.A., www.pagosimple.com, both verified; Aportes en Linea, Asopagos, Enlace "
        "Operativo and MiPlanilla offer the same service | Source: SOI instructivo DDS-DES-INS-008 "
        "v2 and Simple S.A. 'Manual Cesantias' ss. 3.1-3.2, both held in 00-official-sources/pdfs/ "
        "| CONFIRMED as to channel and as to the 258-position layout; TO CONFIRM whether every "
        "operator accepts that same layout.",
        "THE RECIPIENT IS NOT A GOVERNMENT AUTHORITY. The money goes to a private fondo de "
        "cesantias, or to the state-owned FNA, in an individual account in the employee's name. "
        "There is no authority portal, no fiscal receipt and no tax-authority validation - which is "
        "exactly why no XSD exists and why this filing must never be labelled XML.",
        "THE OPERATOR IS THE SAME KIND OF INTERMEDIARY AS FOR PILA, BUT THE SERVICE IS NOT PILA. "
        "Cesantias is a Pago Complementario a la Seguridad Social (PCSS) and is selected as a "
        "distinct service inside the operator's portal, with its own planilla number series and its "
        "own period concept - a YEAR, not a month. Simple S.A. notes that the login is the same one "
        "used for PILA, which is the source of the frequent error of building a PILA planilla and "
        "expecting the cesantias to be in it.",
        "The DIAN portals play no part in this filing. Formulario 350, Formulario 220 and Formato "
        "2276 go to DIAN; the cesantias deposit never does. What DIAN sees of cesantias is the "
        "reporting of the amounts on Formulario 220 casillas 48-49 and Formato 2276 numerals 19-20, "
        "which are separate filings with their own Specs (CO-DIAN-004 and CO-DIAN-005).",
        "File-size and structure constraints from the published instructivos: no header row; the "
        "data start on the first line or row; all records on one Excel sheet; a file above 1 MB "
        "must be compressed before upload (SOI); the fixed-width record is 258 characters and the "
        "sequence must start at 00001 and be consecutive.",
    ],
    "integration_notes": [
        "integration_type = BOTH (scope_manifest). OUTBOUND: the annual planilla, keyed or "
        "uploaded. INBOUND: CO-IN-CESANTIAS-CONFIRMATION, the deposit confirmation evidencing "
        "compliance with the February deadline. Both directions are modelled on Sheet 4 - the "
        "outbound record as T01-T20, the inbound values as E10, E11, E90, E91 and E93.",
        "product_mapping_required = true. The engine must hold the fund code as EMPLOYEE master "
        "data (it is the employee's statutory choice, not a company default), the 360-day service "
        "count, the CST art. 253 base including the transport allowance, the accrual-year period "
        "concept, the per-employee deposit-compliance status and, when the decree is enacted, the "
        "monthly-advance regime flag per contract.",
        "NOT DERIVABLE FROM THE MONTHLY FILINGS. The population is not the PILA population: a "
        "leaver who left in June is absent from the December PILA but is owed a pro rata deposit, "
        "while a salario integral employee is present in PILA and owed nothing here. Do not use the "
        "operator's seed-from-last-PILA convenience (E08).",
        "THE ONE-TO-MANY TRAP ON THE RETURN. Where the medio de pago is Pago Credito, the operator "
        "issues ONE PLANILLA NUMBER PER FONDO, so the reconciliation store must accept many "
        "planilla numbers for one payroll run (E05, E10).",
        "The engine must also produce two things that are NOT in this file and are commonly "
        "conflated with it: the 12% interest paid to the EMPLOYEE in January (IN01-IN03), and the "
        "tax figures that appear on Formulario 220 and Formato 2276. Different payees, different "
        "deadlines, different penalties.",
    ],
    "b1_notes": [
        "RESIDENT AND NON-RESIDENT ARE TREATED IDENTICALLY IN THIS FILING, AND THAT IS THE POINT. "
        "Cesantias is a LABOUR entitlement under the CST, not a tax concept, so it attaches to the "
        "employment relationship and not to tax residence. A non-resident foreign national employed "
        "under a Colombian contract accrues cesantias on the same base, at the same 360-day rate, "
        "is deposited to a fund of their own choosing and is reported in this planilla on exactly "
        "the same record as a resident. There is no non-resident variant of the layout and no "
        "withholding on the deposit.",
        "WHERE RESIDENCE DOES BITE IS THE TAX TREATMENT, WHICH IS NOT THIS FILING. For a RESIDENT, "
        "ET art. 206 num. 4 exempts the severance savings and their interest in full where the "
        "average monthly income of the last six months is at or below 350 UVT (COP 18,330,900 in "
        "2026), then tapers 90 / 80 / 60 / 40 / 20 per cent across the 350-410, 410-470, 470-530, "
        "530-590 and 590-650 UVT bands, with nothing exempt above 650 UVT. For a NON-RESIDENT the "
        "art. 206 num. 4 exemption is unavailable - it belongs to the resident cedula general - and "
        "the payment is taxed at the flat 20% of ET art. 408 on the gross with no art. 388 "
        "depuration. Neither outcome changes a single character of the record sent to the fund.",
        "THE DOCUMENT TYPE IS WHERE THE FOREIGN EMPLOYEE ACTUALLY BREAKS. The layout admits CE, PA, "
        "CD, SC, PE and (in the XLS variant) PT, and SOI records that a Permiso Especial de "
        "Permanencia number must be exactly 15 digits. A regularisation that converts a PEP or PPT "
        "into a Cedula de Extranjeria changes the join key (T03 + T04) that the fund holds, so the "
        "change must reach the fund or the following February's deposit lands on an orphan account. "
        "See T03 and T04.",
        "A Colombian employee posted abroad but retained on a Colombian contract remains in scope; "
        "an employee of a foreign entity with no Colombian employment contract is out of scope "
        "entirely, because there is no CST relationship to accrue cesantias on.",
    ],
    "related": [
        "CO-DIAN-004 (Formulario 220) casillas 48 and 49 - the same cesantias figures reported to "
        "DIAN for the employee's certificate. They must reconcile to this planilla.",
        "CO-DIAN-005 (Formato 2276 v4) numerals 19 and 20 - the same figures again, and NOTE that "
        "numerals 19 and 20 are TRANSPOSED against Formulario 220 casillas 48 and 49. Map by "
        "meaning, per the CO-DIAN-005 Spec.",
        "CO-PILA-003 - the future channel for the monthly advance deposit under Ley 2466 de 2025 "
        "art. 64 par. 1, once MinSalud defines the tipo de cotizacion (see MA04). The PILA Spec "
        "will need a new contribution type when that happens.",
        "CO-DIAN-001 (nomina electronica) - carries the cesantias and the interest as devengado "
        "elements when they are PAID, on the payment-date rule. The XML shows the payment; this "
        "planilla shows the deposit; they are not the same event and can fall in different months.",
        "CCG Module 9 (termination and statutory benefits) for the base, the taper and the "
        "indemnity; CCG Module 10.1 report CO-RPT-006 and the consolidated 2026 filing calendar.",
    ],
    "scope": (SCOPE_WHO + [
        "AMOUNTS AND CONCEPTS REPORTED IN THIS FILING",
        ("Annual severance-savings liquidation at 31 December", "YES",
         "T14. The whole purpose of the filing - one amount per employee per accrual year."),
        ("Basic salary of December of the accrual year", "YES",
         "T12, as the layout expressly requires: 'el ultimo salario basico reportado en el mes de "
         "diciembre del ano causado de cesantias'."),
        ("Auxilio de transporte inside the liquidation base", "YES",
         "CST art. 253 includes it in the base, and Ley 2466 de 2025 art. 64 par. 1 states it "
         "expressly for the monthly advance. It is NOT a separate field - it is inside T14. The "
         "operator's own calculator omits it, which is the single most expensive trap in this "
         "filing; see T14."),
        ("Days of service on the 360-day commercial year", "YES",
         "T10, 1 to 360. Paid leave and recognised incapacity count as service."),
        ("Employee's chosen fund", "YES",
         "T09, one of the five codes 02 / 03 / 10 / 15 / 19. The choice is the employee's under Ley "
         "50 de 1990 art. 99 num. 3."),
        ("Employee residential address, landline, e-mail", "YES",
         "T15 and T18-T19 - the fund needs them to communicate with its own member. Note it is the "
         "RESIDENCE, unlike PILA and the nomina electronica which carry the work location."),
        ("Contract hire date", "YES",
         "T20, and it is the HIRE date, not the start of the accrual period. See T20."),
        ("Interest on severance savings at 12%", "NO",
         "IN01-IN03. Paid DIRECTLY TO THE EMPLOYEE in January under Ley 52 de 1975 art. 1, never to "
         "the fund. Different payee, different deadline, different penalty. Shown on the Spec as "
         "not-applicable rows precisely because it is so often conflated with the deposit."),
        ("Salario integral employees' cesantias", "NO",
         "CST art. 132 num. 2 - the all-inclusive salary ABSORBS the cesantias, so there is no "
         "deposit and the employee must not appear in the planilla at all. They DO appear in PILA, "
         "which is why the seed-from-PILA convenience at E08 is dangerous."),
        ("Partial withdrawals and advances taken during the year", "NO",
         "Not a field of this layout. CST art. 254 prohibits partial payment before termination "
         "except for the authorised housing and education purposes; a lawful partial settlement "
         "reduces the balance and the interest, and is evidenced separately."),
        ("Withholding tax on the severance savings", "NO",
         "No withholding is practised on the DEPOSIT. The tax treatment (ET art. 206 num. 4 for a "
         "resident, ET art. 408 for a non-resident) is settled when the money is PAID to the "
         "employee, and is reported on Formulario 220 and Formato 2276."),
        ("Employer social-security contributions", "NO",
         "Cesantias is a prestacion social and is NOT part of the contribution base (Ley 1393 de "
         "2010 art. 30 and CST art. 128 govern that boundary). Nothing about it appears in PILA "
         "today - the monthly advance under Ley 2466 art. 64 will change the CHANNEL, not the "
         "nature."),
        ("A declared record count or control total inside the file", "NO",
         "The layout has no header and no trailer record. A truncated upload is NOT self-detecting. "
         "Reconcile the operator's returned total (E11) against the engine's own sum."),
        ("Pre-1991 retrospective-regime employees", "PARTIAL",
         "Employees hired before 1 January 1991 who did not migrate remain on the retrospective "
         "annual-adjustment regime, which has NO annual deposit to a fund - the employer holds the "
         "liability and settles on termination. They are therefore out of this planilla, but they "
         "ARE reported as a separate line on Formulario 220 and Formato 2276. Hold the regime as "
         "master data on the contract."),
    ] + SCOPE_TIMING + [
        "SPECIAL CASES",
        ("Employee who left during the accrual year", "NO",
         "The cesantias of a leaver are settled IN THE FINAL SETTLEMENT and paid to the employee, "
         "not deposited to the fund in the following February. Only employees still in service at "
         "31 December generate a planilla record. Including a leaver double-pays."),
        ("Employee hired during the accrual year", "YES",
         "One record, with T10 carrying the actual days of service on the 360-day convention and "
         "T20 still carrying the real hire date."),
        ("Employee whose liquidation is below one day of the SMMLV", "NO",
         "The layout rejects it: 'el valor minimo del recaudo debe ser de un (1) dia de un (1) "
         "SMLMV del ano causado' - COP 58,363.50 for accrual year 2026. Such a residue is settled "
         "with the employee, not deposited."),
        ("Employee paid directly under CST art. 57 par. 4", "NO",
         "Where the employer proves direct payment fehacientemente, the payment discharges the "
         "obligation and no non-deposit penalty applies - so no planilla record. BUT affiliation to "
         "a fund remains compulsory, and the discharge is rebuttable on the freedom-and-purpose "
         "test. See E92."),
        ("Construction worker under CST art. 310", "YES",
         "A special regime - three days' salary per completed month rather than 30 - but the same "
         "planilla record. Only T14 changes; the layout has no field to disclose the regime."),
        ("Apprentice under a contrato de aprendizaje", "YES",
         "Ley 2466 de 2025 art. 21 converted the apprenticeship into a special fixed-term LABOUR "
         "contract, regulated by Decreto 0223 of 5 March 2026, so the ordinary CST prestaciones "
         "including cesantias apply to the productive phase."),
        ("Employee who changed fund during the year", "YES",
         "One record, to the fund the employee has chosen at the time of the deposit. The choice is "
         "the employee's and is master data on the employee; a mid-year change must reach payroll "
         "before the February run or the deposit goes to the old fund."),
        ("Monthly advance deposit already made through the year", "PARTIAL",
         "Not yet operable - the enabling decree is a draft and no MinSalud PILA regulation exists. "
         "When it is, the annual consolidation still runs and only the DIFFERENCE is deposited by "
         "14 February; omitting monthly payments is not mora provided the annual total is completed "
         "by then. See MA01-MA05."),
    ]),
    "fields": FIELDS,
}
