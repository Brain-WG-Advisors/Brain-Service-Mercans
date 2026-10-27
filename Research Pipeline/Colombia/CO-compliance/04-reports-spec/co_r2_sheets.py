# -*- coding: utf-8 -*-
"""CO-DIAN-002 - Sheets 5 to 9 for Formulario 350."""

from co_r2_formulario350 import CFG

# ===========================================================================
#  SHEET 5 - FILE STRUCTURE (neutral field model - this is a PORTAL FORM)
# ===========================================================================
CFG["filestruct"] = [
    ("##", "SUBMISSION FORMAT - VERIFIED (v2.7 STEP 3.5)"),
    ("Channel", "online_form. Data is keyed, or robotically entered, directly into the DIAN "
                "Servicios Informaticos Electronicos (Muisca) form at www.dian.gov.co."),
    ("Why this is NOT XML", "DIAN publishes NO XSD, NO cahier des charges and NO import template for "
                            "Formulario 350. Res. DIAN 000227 de 2025 art. 1.2.2.26 par. 1 says only "
                            "that filers must use 'los Servicios Informaticos dispuestos por la "
                            "entidad, utilizando el Instrumento de Firma Electronica (IFE)', and "
                            "that DIAN 'pondra a disposicion el Formulario numero 350 en forma "
                            "virtual en la pagina web'. Contrast the nomina electronica, which has a "
                            "published XSD and a SOAP contract."),
    ("Authentication", "Instrumento de Firma Electronica (IFE) authorised by DIAN - an authenticated "
                       "portal credential. NOT an X.509 document signature."),
    ("Consequence for the model below", "The structure below is a LOGICAL MODEL - the field list and "
                                        "hierarchy of the return - NOT the wire or submission "
                                        "format. There is no wire format to document."),
    ("Payment", "The return must be paid IN FULL. ET art. 580-1: a withholding return filed without "
                "full payment produces no legal effect, with no administrative act needed to declare "
                "it so. Casilla 980 must equal casilla 138."),

    ("##", "LOGICAL MODEL - HOJA 1 (casillas 1 to 140, plus 980-997)"),
    ("Block 1 - Datos del declarante", "1 Ano | 3 Periodo | 4 Numero de formulario (DIAN-assigned) | "
                                       "5 NIT | 6 DV | 7-10 apellidos y nombres (natural person) | "
                                       "11 Razon social (legal person) | 12 Cod. Direccion seccional"),
    ("Block 2 - Correccion", "25 Cod. correccion | 26 Numero de formulario anterior. Both blank on "
                             "an initial return; both populated on a corrective one."),
    ("Block 3 - Autorretencion art. 114-1", "27 Actividad economica principal (CIIU) | 28 Tarifa "
                                            "(derived by the portal from 27)"),
    ("Block 4 - Renta, personas juridicas",
     "Bases 29-41 paired with retenciones 42-54, by concept: honorarios, comisiones, servicios, "
     "rendimientos financieros, arrendamientos, regalias, dividendos, compras, tarjetas, contratos "
     "de construccion, loterias, hidrocarburos, otros pagos."),
    ("Block 5 - Pagos al exterior, personas juridicas",
     "55 base sin convenio | 56 base con convenio | 57 retencion sin convenio | 58 retencion con "
     "convenio. All four are DERIVED by the portal from the hoja-2 annex."),
    ("Block 6 - Autorretenciones, personas juridicas",
     "59 base art. 114-1 | 60-67 bases by concept | 68 retencion art. 114-1 | 69-76 retenciones by "
     "concept."),
    ("Block 7 - Renta, personas naturales  <-- PAYROLL",
     "77 base rentas de trabajo  <-- PAYROLL | 78 base rentas de pensiones | 79-92 bases by other "
     "concept || 93 retencion rentas de trabajo  <-- PAYROLL | 94 retencion rentas de pensiones | "
     "95-108 retenciones by other concept. Note that 89 / 105 (enajenacion de activos fijos y "
     "actividades de transito) exist only in the natural-person column."),
    ("Block 8 - Pagos al exterior, personas naturales  <-- PAYROLL (non-resident)",
     "109 base sin convenio | 110 base con convenio | 111 retencion sin convenio | 112 retencion con "
     "convenio. All four DERIVED by the portal from the hoja-2 annex."),
    ("Block 9 - Autorretenciones, personas naturales", "113-120 bases | 121-128 retenciones."),
    ("Block 10 - Totales renta", "129 menos retenciones en exceso o indebidas | 130 total "
                                 "retenciones renta y complementario."),
    ("Block 11 - Otros impuestos", "131 IVA a responsables | 132 IVA por servicios a no residentes | "
                                   "133 menos IVA en exceso | 134 total IVA | 135 timbre nacional."),
    ("Block 12 - Total", "136 total retenciones | 137 sanciones | 138 total retenciones mas "
                         "sanciones."),
    ("Block 13 - Firmas", "139 NIT signatario | 140 DV signatario | 980 pago total | 981 cod. "
                          "representacion | 982 codigo contador o revisor fiscal | 983 no. tarjeta "
                          "profesional | 994 con salvedades | 997 sello entidad recaudadora "
                          "(DISPLAY-ONLY, not an input)."),

    ("##", "LOGICAL MODEL - HOJA 2 (anexo de pagos al exterior, casillas 141 to 155)"),
    ("Repeating annex row (45 rows on the printed form)",
     "141 A paises con o sin convenio | 142 Concepto de pago | 143 Tipo de persona | 144 Pais + Cod. "
     "| 145 Pagos o abonos en cuenta | 146 Tarifa (%) | 147 Valor retencion (computed as 145 x 146)"),
    ("Annex totals", "148 sin convenio persona juridica (base)   -> hoja 1 casilla 55"),
    ("", "149 sin convenio persona natural (base)    -> hoja 1 casilla 109  <-- NON-RESIDENT EMPLOYEE"),
    ("", "150 sin convenio persona juridica (ret.)   -> hoja 1 casilla 57"),
    ("", "151 sin convenio persona natural (ret.)    -> hoja 1 casilla 111  <-- NON-RESIDENT EMPLOYEE"),
    ("", "152 con convenio persona juridica (base)   -> hoja 1 casilla 56"),
    ("", "153 con convenio persona natural (base)    -> hoja 1 casilla 110  <-- NON-RESIDENT EMPLOYEE"),
    ("", "154 con convenio persona juridica (ret.)   -> hoja 1 casilla 58"),
    ("", "155 con convenio persona natural (ret.)    -> hoja 1 casilla 112  <-- NON-RESIDENT EMPLOYEE"),

    ("##", "ARITHMETIC PUBLISHED IN THE INSTRUCTIVO"),
    ("Casilla 130", "42 + 43 + 44 + 45 + 46 + 47 + 48 + 49 + 50 + 51 + 52 + 53 + 54 + 57 + 58 + 68 + "
                    "69 + 70 + 71 + 72 + 73 + 74 + 75 + 76 + 93 + 94 + 95 + 96 + 97 + 98 + 99 + 100 "
                    "+ 101 + 102 + 103 + 104 + 105 + 106 + 107 + 108 + 111 + 112 + 121 + 122 + 123 + "
                    "124 + 125 + 126 + 127 + 128, MINUS 129."),
    ("Casilla 134", "131 + 132, MINUS 133."),
    ("Casilla 136", "130 + 134 + 135."),
    ("Casilla 138", "136 + 137."),
    ("Casilla 147", "145 x 146, computed by the portal."),
    ("Casilla 28", "Derived by the portal from the CIIU code chosen in casilla 27."),

    ("##", "AMOUNT AND ROUNDING CONVENTION"),
    ("Rounding", "Whole pesos, then to the NEAREST 1,000 (ET art. 577). This is the third of the "
                 "three Colombian conventions and must never be blended with the nomina electronica "
                 "(2 decimals, round-half-to-even) or with PILA (round UP to the next 100)."),
    ("Minimum penalty", "10 UVT = COP 523,740 for 2026. For a corrective return the minimum is 10 "
                        "UVT of the year in which the ORIGINAL return was filed, not of the current "
                        "year."),
]

# ===========================================================================
#  SHEET 6 - FIELD OPTIONS
# ===========================================================================
CFG["options"] = [
    "PERIODO (casilla 3)",
    ("01", "ENE", "Enero", "January. The return is always monthly for a withholding agent."),
    ("02", "FEB", "Febrero", "February."),
    ("03", "MAR", "Marzo", "March - the period used in the worked example."),
    ("04 - 12", "ABR - DIC", "Abril a Diciembre", "The remaining months."),

    "CODIGO DE CORRECCION (casilla 25)",
    ("1", "PRIV", "Correccion a la declaracion privada", "The taxpayer corrects its own return."),
    ("2", "962", "Correccion a la correccion generada por la DIAN",
     "Correction of a DIAN-generated correction under Ley 962 de 2005 art. 43."),
    ("3", "ACTO", "Correccion provocada por acto administrativo",
     "Correction prompted by an administrative act."),

    "TIPO DE PERSONA - hoja 2 (casilla 143), NEW in the 2024 form",
    ("PJ", "PJ", "Persona juridica", "Foreign entity without a Colombian domicile. Rolls into "
     "casillas 148 / 150 / 152 / 154."),
    ("PN", "PN", "Persona natural", "Non-resident natural person, including a NON-RESIDENT EMPLOYEE. "
     "Rolls into casillas 149 / 151 / 153 / 155."),

    "TRATAMIENTO DE CONVENIO - hoja 2 (casilla 141)",
    ("SIN CONVENIO", "SC", "Paises sin convenio", "No double-tax treaty in force. Concepto de pago "
     "list 1 to 18. Rates from ET arts. 408-415."),
    ("CON CONVENIO", "CC", "Paises con convenio vigente", "A double-tax treaty is in force. Concepto "
     "de pago list 19 to 33. The rate must be taken from the applicable treaty."),

    "CONCEPTO DE PAGO - hoja 2, SIN CONVENIO (casilla 142, codes 1-18)",
    ("1", "INT", "Intereses", "Interest on credits of any nature."),
    ("2", "DIV", "Dividendos y participaciones", "Dividends, ET art. 407."),
    ("3", "RF-1A", "Rendimientos financieros - creditos exterior >= 1 ano",
     "Financial yields on foreign credits of one year or more, and leasing finance costs. 15%."),
    ("4", "REG", "Regalias y explotacion de intangibles",
     "Royalties, industrial and intellectual property, films, software, know-how."),
    ("5", "SERV-PER", "Prestaciones de servicios y compensacion por servicios personales",
     "THE NON-RESIDENT EMPLOYEE CONCEPT for a country with NO treaty. Remuneration of services in "
     "favour of non-resident natural persons and foreign entities. Rate 20% under ET art. 408."),
    ("6", "SERV-TEC", "Servicios tecnicos, de asistencia tecnica y consultoria",
     "Technical services, technical assistance and consultancy, including from abroad."),
    ("7", "COM", "Comisiones", "Commissions."),
    ("8", "HON", "Honorarios", "Professional fees."),
    ("9", "ARR", "Arrendamientos", "Rental of movable and immovable property."),
    ("10", "LEAS", "Contratos de leasing sobre naves, helicopteros y/o aerodinos", "1%."),
    ("11", "REAS", "Prima cedida por reaseguros", "1%."),
    ("12", "RF-8A", "Rendimientos financieros - creditos APP >= 8 anos", "5%, APP infrastructure."),
    ("13", "CASA", "Administracion o direccion a la casa matriz", "33%, ET art. 124."),
    ("14", "TRANS", "Servicios de transporte internacional", "5%."),
    ("15", "PES", "Venta y/o servicios por Presencia Economica Significativa - PES", "ET art. 20-3."),
    ("16", "JNC", "Jurisdicciones no cooperantes o de baja o nula imposicion",
     "General corporate income-tax rate."),
    ("17", "PROF-EXT", "Pagos a profesores extranjeros",
     "7%, foreign professors on ICFES-approved contracts of up to four months."),
    ("18", "OTROS", "Otros conceptos", "Any other beneficially owned income not listed above."),

    "CONCEPTO DE PAGO - hoja 2, CON CONVENIO (casilla 142, codes 19-33)",
    ("19", "INM", "Rentas inmobiliarias", "Income from immovable property situated in Colombia."),
    ("20", "DIV-CC", "Dividendos y participaciones", "Dividends under the treaty dividend article."),
    ("21", "INT-CC", "Intereses", "Interest under the treaty interest article."),
    ("23", "GC", "Ganancias de capital", "Gains on the disposal of Colombian immovable property."),
    ("24", "RT", "Rentas de trabajo",
     "THE NON-RESIDENT EMPLOYEE CONCEPT for a treaty country. The form's own definition is 'rentas "
     "de trabajo de cualquier naturaleza EN RELACION CON UN EMPLEO a favor de personas naturales no "
     "residentes o sucesiones iliquidas de personas naturales que no eran residentes en Colombia'."),
    ("25", "HON-DIR", "Honorarios de directores",
     "Directors' fees and similar payments to a member of a board or equivalent organ. NOT the "
     "employee concept."),
    ("26", "ART", "Artistas y deportistas", "Entertainers and sportspersons."),
    ("27", "PEN", "Pensiones", "Pensions and similar remuneration. Use where the EMPLOYER pays the "
     "pension to a non-resident."),
    ("28", "FUN", "Funciones publicas", "Government service."),
    ("(others)", "-", "Restantes conceptos con convenio",
     "The remaining treaty concepts up to code 33 are printed on the form's hoja-2 instructivo."),

    "TARIFAS - pagos al exterior (casilla 146)",
    ("20.00", "20%", "Tarifa general ET art. 408",
     "The general rate for employment income and personal services paid to non-residents. THE "
     "PAYROLL RATE."),
    ("15.00", "15%", "Rendimientos financieros creditos >= 1 ano", "ET art. 408 special rate."),
    ("5.00", "5%", "Transporte internacional; intereses APP >= 8 anos", "ET special rates."),
    ("33.00", "33%", "Administracion o direccion a casa matriz", "ET art. 124."),
    ("1.00", "1%", "Leasing de naves y aerodinos; prima cedida por reaseguros", "ET special rates."),
    ("7.00", "7%", "Profesores extranjeros", "Contracts of up to four months with ICFES-approved "
     "institutions."),
    ("(treaty)", "-", "Tarifa del convenio",
     "For CON CONVENIO rows the rate comes from the applicable double-tax treaty and may be lower "
     "than 20%, or nil. Mercans applies treaty relief ONLY on written client instruction supported "
     "by a residence certificate."),

    "PAISES CON CONVENIO VIGENTE (casilla 144, treaty rows)",
    ("ES / CL / CH", "-", "Espana, Chile, Suiza", "Treaties in force."),
    ("CA / MX / KR", "-", "Canada, Mexico, Corea del Sur", "Treaties in force."),
    ("PT / IN / CZ", "-", "Portugal, India, Republica Checa", "Treaties in force."),
    ("GB / FR / IT / JP", "-", "Reino Unido, Francia, Italia, Japon", "Treaties in force."),
    ("(CAN)", "-", "Decision 578 de la Comunidad Andina",
     "Bolivia, Ecuador and Peru, under Andean Community Decision 578 rather than a bilateral treaty."),

    "CODIGO CONTADOR O REVISOR FISCAL (casilla 982)",
    ("1", "CONT", "Contador",
     "Required where the taxpayer keeps books and gross assets at the preceding year end exceeded "
     "100,000 UVT."),
    ("2", "RF", "Revisor fiscal",
     "Required for joint-stock companies; for companies where the administration does not fall to "
     "all partners; where partners excluded from management holding at least 20% of capital so "
     "require; for any commercial company whose gross assets at 31 December reach 5,000 SMMLV; and "
     "for any whose gross income in the preceding year reaches 3,000 SMMLV."),

    "CODIGO DE REPRESENTACION (casilla 981)",
    ("(RUT casilla 98)", "-", "Tipo de representacion",
     "Taken from casilla 98 of the RUT. Typical values are legal representative (principal or "
     "alternate), agent with power of attorney, liquidator and administrator. The catalogue is "
     "maintained by DIAN in the RUT, not on this form."),

    "DIRECCION SECCIONAL (casilla 12)",
    ("(RUT casilla 12)", "-", "Codigo de la direccion seccional",
     "The DIAN sectional office of the taxpayer's principal domicile, taken from casilla 12 of the "
     "RUT. A configuration attribute of the entity; the catalogue is maintained by DIAN."),

    "ACTIVIDAD ECONOMICA - CIIU (casilla 27)",
    ("(CIIU Rev. 4 A.C.)", "-", "Codigo de actividad economica principal",
     "From casilla 46 of the RUT, per DIAN Resoluciones 000114 of 21 December 2020, 001232 of "
     "16 September 2022 and 000086 of 24 May 2023. The chosen code drives the self-withholding rate "
     "auto-filled into casilla 28 under DUR 1625 de 2016 art. 1.2.6.8."),

    "FILING CALENDAR - by the LAST DIGIT of the NIT",
    ("1 to 0", "-", "Del septimo al decimo sexto dia habil del mes siguiente",
     "DUR 1625 de 2016 art. 1.6.1.13.2.33 as set by Decreto 2229 de 2023. NIT ending 1 files on the "
     "7th business day, ending 2 on the 8th, and so on to ending 0 on the 16th. Contrast PILA, "
     "which is keyed to the last TWO digits and runs from the 2nd to the 16th business day."),
]

# ===========================================================================
#  SHEET 7 - POPULATION RULES
# ===========================================================================
CFG["population"] = [
    "MANDATORY FIELD RULES",
    ("Casilla 77 - base rentas de trabajo", "Payroll engine (tax)",
     "Accumulate, across every employee paid in the month, the taxable base actually used to compute "
     "the withholding. For a RESIDENT this is the ET art. 388 DEPURATED base - gross taxable "
     "payments less non-constitutive income (mandatory health, pension and solidarity-fund "
     "contributions), less the art. 387 deductions elected in writing by the employee, less the 25% "
     "exempt income of art. 206 num. 10, subject to the 40% and 1,340-UVT caps. Do NOT report the "
     "gross. Round the accumulated total to the nearest 1,000 (ET art. 577), once, at the end - "
     "never round each employee and then sum.",
     "The casilla also sweeps in honorarios, servicios and comisiones paid to NATURAL persons that "
     "are withheld under the art. 383 table (ET art. 383 par. 2, added by Ley 2277 de 2022 art. 8). "
     "Payroll supplies only the EMPLOYMENT component; the boundary with casilla 79 / 95 is a "
     "client-specific classification that must be agreed and documented at implementation."),
    ("Casilla 93 - retencion rentas de trabajo", "Payroll engine (tax)",
     "Accumulate the retencion en la fuente actually withheld on work income from natural persons in "
     "the month. Each employee's withholding is itself already approximated to the nearest 1,000 "
     "under ET art. 868; accumulate those approximated figures and then apply the art. 577 "
     "nearest-1,000 rounding to the total. Reconcile the result to the sum of RetencionFuente "
     "(NIE177) across every nomina electronica document for the same month BEFORE filing.",
     "An employee whose depurated base falls in the 0% band contributes zero here but still "
     "contributes their base to casilla 77. Excluding the base is a common and material error."),
    ("Casillas 78 / 94 - rentas de pensiones", "Payroll engine (tax)",
     "Populate only where the EMPLOYER itself pays a pension. Report the monthly amount EXCEEDING "
     "1,000 UVT (COP 52,374,000 in 2026) under ET art. 206 num. 5, and the withholding on that "
     "excess. Where the pension is paid by a pension fund, the fund is the withholding agent and "
     "nothing is reported here.",
     "Colombia has no employer year-end reconciliation, so an error here is corrected only by a "
     "corrective return, not by a December true-up."),
    ("Casilla 12 - direccion seccional", "Company master data",
     "Copy the code from casilla 12 of the entity's RUT. It is a static configuration attribute; it "
     "does not change with the period and must not be re-derived monthly.",
     "A branch structure does not change this casilla - the return is filed for the principal "
     "domicile of the legal entity."),

    "CRITICAL VALIDATION RULES",
    ("Nil period", "Engine (control)",
     "Where NO operation subject to withholding occurred in the month, DO NOT file. ET art. 606 "
     "par. 2 makes the return non-obligatory for such a period. This is unusual: the nomina "
     "electronica and PILA have no equivalent exemption, so a month with employees but no "
     "withholding still produces those two filings while producing no Form 350.",
     "Filing an all-zero return is not an error, but it creates a record that must then be corrected "
     "if a late payment is discovered. Prefer not filing where the exemption genuinely applies, and "
     "document the decision."),
    ("Payment must accompany the return", "Engine (control)",
     "Casilla 980 (pago total) must equal casilla 138 (total retenciones mas sanciones). ET "
     "art. 580-1: a withholding return filed WITHOUT full payment produces NO legal effect, and no "
     "administrative act is needed to say so. Until the taxpayer files again WITH payment, the "
     "original filing is treated as never made.",
     "This is the single most expensive procedural trap on this return: a filed-but-unpaid return "
     "accrues late-filing penalties as though nothing had been filed."),
    ("Do not key the portal-derived casillas", "Engine (control)",
     "The DIAN service derives casillas 28 (from 27), 55, 56, 57, 58, 109, 110, 111 and 112 (from "
     "the hoja-2 annex totals 148 to 155), 130, 134, 136, 138 and 147 (145 x 146). Supply only the "
     "inputs. Attempting to key a derived casilla either fails or, worse, creates an inconsistency "
     "the portal silently overwrites.",
     "For the non-resident block this means payroll supplies hoja-2 ROWS - casillas 141 to 146 - "
     "and never the hoja-1 casillas 109 to 112."),
    ("Counterparty-type separation", "Engine (accumulation)",
     "The 2024 form separates withholding on NATURAL persons from withholding on LEGAL persons "
     "across the whole grid. The engine must therefore accumulate withholding by counterparty type "
     "from the transaction level, not classify it at reporting time. The pre-2024 form did not "
     "require this and a migrated accumulation will not carry the flag.",
     "Payroll is inherently natural-person only, so its own accumulation is unambiguous. The risk "
     "lies in a shared withholding ledger where supplier and employee withholding are commingled."),

    "AMOUNT FORMAT RULES",
    ("All money casillas", "Engine (formatting)",
     "Whole pesos, then rounded to the NEAREST 1,000 under ET art. 577. Apply the rounding ONCE, to "
     "the accumulated casilla value, not to each contributing record. No decimals, no thousand "
     "separators in the transmitted value.",
     "Rounding each employee to the nearest 1,000 and then summing produces a total that can differ "
     "from the correctly rounded aggregate by several thousand pesos across a large population."),
    ("Three conventions must not be blended", "Engine (formatting)",
     "The SAME withholding appears as three different numbers across the Colombian artefacts: "
     "nearest-1,000 here; two decimals round-half-to-even in the nomina electronica; and irrelevant "
     "in PILA, which carries contributions not tax. Store the unrounded figure once and apply each "
     "convention at output.",
     "The reconciliation between casilla 93 and SUM(NIE177) must therefore be performed on the "
     "UNROUNDED values with a tolerance, not on the rounded ones."),
    ("Minimum penalty", "Engine (control)",
     "Where casilla 137 is populated, the amount cannot be below 10 UVT. For 2026 that is "
     "10 x 52,374 = COP 523,740. For a CORRECTIVE return the minimum is 10 UVT of the year in which "
     "the ORIGINAL return was filed, not of the current year.",
     "A correction of a 2024 return filed in 2026 uses the 2024 UVT for the minimum penalty. Store "
     "the original filing year with the correction."),

    "PAYROLL-SPECIFIC POPULATION RULES",
    ("Non-resident employees - hoja 2 rows", "Payroll engine (tax)",
     "For each non-resident employee, create one hoja-2 row per country and treaty status. Set "
     "casilla 141 to SIN CONVENIO or CON CONVENIO; casilla 142 to concepto 5 (Prestaciones de "
     "servicios y compensacion por servicios personales) for non-treaty countries or concepto 24 "
     "(Rentas de trabajo) for treaty countries; casilla 143 to Persona natural; casilla 144 to the "
     "country of residence; casilla 145 to the GROSS payment - not a depurated base, because ET "
     "art. 408 admits no depuration; and casilla 146 to 20.00, or to the treaty rate. The portal "
     "computes casilla 147 and the four totals.",
     "Rows for the same country, concept and person type may be aggregated. Do NOT aggregate across "
     "treaty statuses or across concepts - the rate and the treaty article differ. Directors' fees "
     "belong in concepto 25 and employer-paid pensions in concepto 27, never in 24."),
    ("Residence switch mid-year", "Payroll engine (tax)",
     "Carry a residence flag with an effective date on the employee record and re-evaluate it every "
     "period against ET art. 10 - presence exceeding 183 calendar days, continuous or not, in any "
     "365-day period. Until the test is met, report the employee on hoja 2 at the flat 20%. From the "
     "payment FOLLOWING the date the test is met, report on hoja 1 casillas 77 and 93 under the "
     "art. 383 table. Never restate the earlier months.",
     "DIAN Concepto 011108 of 29 June 2026 expressly rejects withholding under art. 383 from day one "
     "in anticipation of future residence, even on a contract exceeding 183 days. Withholding is "
     "determined at the moment of each payment on the status then held. There is no payroll "
     "true-up; the employee reconciles on their own return."),
    ("Work performed entirely abroad", "Payroll engine (tax)",
     "Where a NON-RESIDENT performs the work entirely outside Colombia, the income is foreign-source "
     "and there is NO Colombian withholding and nothing to report on this return - neither hoja 1 "
     "nor hoja 2. Where a RESIDENT performs work abroad, the income IS taxable on the worldwide "
     "basis and goes to casillas 77 and 93 as normal.",
     "The distinguishing evidence is the place-of-work country carried on the nomina electronica "
     "(NIE050). Keep the two records consistent: a document showing LugarTrabajoPais other than CO "
     "for a non-resident should produce no Form 350 line."),
    ("Casilla 129 - reversing an over-withholding", "Payroll engine",
     "Where an employee's withholding is corrected downward in a later month - a retroactive change "
     "to the art. 387 deductions, a cancelled payment, or an arithmetic error - report the reversal "
     "in casilla 129 of the month in which the correction is made, rather than correcting the "
     "earlier return. Where the month's withholding is insufficient to absorb the credit, the "
     "instructivo permits carrying it to the immediately following periods.",
     "Casilla 129 also carries reintegros of non-transferable withholding attributable to a "
     "resident natural-person beneficiary or a resident foreign investor under DUR 1625 de 2016 "
     "art. 1.2.4.37 - not a payroll case, but the same casilla."),
    ("Casilla 27 and the art. 114-1 exoneration", "Company configuration",
     "Populate casilla 27 only where the employer is a LEGAL person exonerated from employer "
     "contributions under ET art. 114-1. The SAME exoneration test - employees earning less than 10 "
     "SMMLV (COP 17,509,050 in 2026) - drives PILA archivo tipo 1 field 33 and PILA Registro Tipo 2 "
     "field 76. Configure the test ONCE and consume it in both places.",
     "The exoneration is tested MONTHLY and PER EMPLOYEE for PILA purposes, but the self-withholding "
     "activity code here is an entity-level, static attribute. Do not conflate the two granularities."),

    "CROSS-FIELD VALIDATIONS",
    ("Casilla 25 and casilla 26", "Engine (validation)",
     "Both blank on an initial return; both populated on a corrective one. Casilla 26 must carry the "
     "casilla-4 form number of the return being corrected.",
     "A corrective return with casilla 26 blank is treated as a new initial return and produces a "
     "duplicate filing for the period."),
    ("Casillas 7-10 versus casilla 11", "Engine (validation)",
     "A LEGAL person populates casilla 11 and leaves 7 to 10 blank; a NATURAL person does the "
     "reverse. The DIAN service auto-fills whichever applies from the RUT.",
     "Both blocks populated is a RUT inconsistency, not a form error - resolve it in the RUT."),
    ("Casilla 27 and casilla 28", "Engine (validation)",
     "Casilla 28 is derived from casilla 27 by the portal. Supply 27 only.",
     "A hard-coded rate in 28 will be overwritten and may mask a wrong CIIU code in 27."),
    ("Casillas 982, 983 and 994", "Engine (validation)",
     "Where casilla 982 is populated, casilla 983 (professional card number) is mandatory and "
     "casilla 994 (with qualifications) becomes available. Where 982 is blank, 983 and 994 must be "
     "blank.",
     "An unsigned return that required an accountant's or auditor's signature is defective."),
    ("Casilla 138 and casilla 980", "Engine (validation)",
     "They must be equal. Block submission where they are not.",
     "ET art. 580-1 makes an underpaid return legally ineffective. This is a hard stop, not a warning."),
    ("Cross-report reconciliation", "Engine (reconciliation)",
     "Before filing, assert: SUM(NIE177) over all nomina electronica documents for the month, "
     "unrounded, equals the unrounded accumulation behind casilla 93, within a tolerance of one peso "
     "per employee. Assert also that the employee count behind casilla 77 equals the number of "
     "validated nomina electronica documents for the month.",
     "A mismatch almost always means either an employee was paid without a nomina electronica "
     "document, or a document was rejected and not re-transmitted. Both are deductibility failures, "
     "not just reporting failures."),
]

# ===========================================================================
#  SHEET 8 - EXAMPLE ANALYSIS
# ===========================================================================
CFG["example"] = [
    "WORKED EXAMPLE - MARCH 2026, SINGLE-EMPLOYEE ILLUSTRATION",
    ("(scenario)", "Employer", "MERCANS COLOMBIA S.A.S., NIT 900123456-7, one employee paid in the "
     "month, no supplier withholding, no VAT withholding, no self-withholding.",
     "Deliberately reduced to the payroll contribution so the casilla arithmetic is legible. A real "
     "return aggregates every withholding the employer makes."),
    ("(scenario)", "Employee", "Juan Carlos Perez Gomez, cedula 1020304050, salary COP 12,000,000, "
     "tax RESIDENT.",
     "The same employee as the nomina electronica worked example, so the reconciliation can be "
     "followed across the two workbooks."),

    "HEADER",
    ("2026", "Casilla 1 - Ano", "Tax year 2026.", "-"),
    ("03", "Casilla 3 - Periodo", "March.",
     "The return is due between the 7th and 16th business day of April 2026, by the last digit of "
     "the NIT. NIT 900123456 ends in 6, so the 12th business day of April."),
    ("1120500123456", "Casilla 4 - Numero de formulario", "Assigned by DIAN, not by the declarant.",
     "Capture and store it: a later corrective return quotes it in casilla 26."),
    ("900123456 / 7", "Casillas 5 / 6 - NIT / DV", "Employer tax number and check digit.",
     "The same NIT as nomina electronica NIE033 / NIE034 and as PILA archivo tipo 1 fields 3 and 4."),
    ("MERCANS COLOMBIA S.A.S.", "Casilla 11 - Razon social", "Legal person, so casillas 7 to 10 stay "
     "blank.", "Auto-filled by the DIAN service from RUT casilla 35."),
    ("32", "Casilla 12 - Cod. Direccion seccional", "Bogota sectional office.",
     "Static configuration from RUT casilla 12."),

    "PAYROLL CASILLAS - RESIDENT",
    ("8190000", "Casilla 77 - Base rentas de trabajo",
     "The ET art. 388 DEPURATED base: gross 12,000,000, less non-constitutive contributions "
     "1,080,000 (health 480,000 + pension 480,000 + solidarity fund 120,000) = 10,920,000, less 25% "
     "exempt income 2,730,000 = 8,190,000. Already a multiple of 1,000.",
     "NOT the gross. Reporting 12,000,000 here would overstate the base by 46% and would not tie to "
     "the withholding in casilla 93."),
    ("617000", "Casilla 93 - Retencion rentas de trabajo",
     "8,190,000 / 52,374 = 156.375 UVT; band 150-360 UVT at 28%: (156.375 - 150) x 0.28 + 10 = "
     "11.785 UVT; x 52,374 = COP 617,232; approximated to the nearest 1,000 under ET art. 868 = "
     "COP 617,000.",
     "Must equal SUM(NIE177) across the month's nomina electronica documents. Here there is one "
     "document carrying exactly 617,000.00."),
    ("(blank)", "Casillas 78 / 94 - Rentas de pensiones",
     "The employer pays no pension, so both are blank.",
     "They would be populated only for the excess over 1,000 UVT (COP 52,374,000 per month) of an "
     "employer-paid pension."),

    "PAYROLL CASILLAS - NON-RESIDENT VARIANT (hoja 2)",
    ("CON CONVENIO", "Casilla 141 - Convenio",
     "Had the same employee been a non-resident Spanish national before acquiring residence, and "
     "Spain has a treaty in force with Colombia.",
     "SIN CONVENIO would switch casilla 142 to the 1-18 concept list."),
    ("24", "Casilla 142 - Concepto de pago",
     "Rentas de trabajo - 'rentas de trabajo de cualquier naturaleza en relacion con un empleo a "
     "favor de personas naturales no residentes'.",
     "For a non-treaty country the equivalent is concepto 5, Prestaciones de servicios y "
     "compensacion por servicios personales. Directors' fees would be 25, pensions 27."),
    ("Persona natural", "Casilla 143 - Tipo de persona",
     "An employee is always a natural person.",
     "This is the field that routes the row into totals 153 / 155 rather than 152 / 154. New in the "
     "2024 form."),
    ("ES", "Casilla 144 - Pais", "Spain.",
     "Must be a treaty country where casilla 141 = CON CONVENIO."),
    ("12000000", "Casilla 145 - Pagos o abonos en cuenta",
     "The GROSS salary. ET art. 408 admits no depuration - no deduction of the mandatory "
     "contributions, no exempt income.",
     "Contrast casilla 77 for the resident, which carries the depurated 8,190,000. The non-resident "
     "base is 46% higher for the same salary."),
    ("20.00", "Casilla 146 - Tarifa", "The general ET art. 408 rate.",
     "Where the treaty assigns taxing rights to the residence state the rate may be reduced or nil - "
     "but Mercans applies treaty relief only on written client instruction with a residence "
     "certificate."),
    ("2400000", "Casilla 147 - Valor retencion",
     "Computed by the portal as 12,000,000 x 20% = 2,400,000.",
     "Payroll supplies 145 and 146 only. Nearly four times the resident's 617,000 for the same "
     "salary - the single clearest illustration of why the residence flag matters."),
    ("12000000 -> 2400000", "Casillas 153 -> 110 and 155 -> 112",
     "The annex totals for treaty natural persons roll up to hoja 1 casillas 110 (base) and 112 "
     "(withholding).",
     "Payroll never keys 110 or 112 directly."),

    "TOTALS",
    ("(blank)", "Casilla 129 - Menos retenciones en exceso",
     "No reversal in this month.",
     "Would be populated where an earlier month's withholding is corrected downward."),
    ("617000", "Casilla 130 - Total retenciones renta",
     "The published summation reduces, in this single-employee example, to casilla 93 alone.",
     "In a real return this aggregates forty-two casillas less casilla 129."),
    ("617000", "Casilla 136 - Total retenciones",
     "130 + 134 (VAT, nil) + 135 (stamp duty, nil).", "-"),
    ("(blank)", "Casilla 137 - Sanciones", "Filed on time, so no penalty.",
     "If late, the minimum is 10 UVT = COP 523,740 for 2026 - which would nearly double this "
     "return's liability."),
    ("617000", "Casilla 138 - Total retenciones mas sanciones", "136 + 137.",
     "This is the amount that must be paid."),
    ("617000", "Casilla 980 - Pago total", "Paid in full with the return.",
     "MUST equal casilla 138. ET art. 580-1: a return filed without full payment produces NO legal "
     "effect. This is the most expensive procedural trap on the form."),

    "SIGNATURE",
    ("79123456 / 3", "Casillas 139 / 140 - Signatory NIT and DV",
     "The legal representative signing the return.", "-"),
    ("01", "Casilla 981 - Cod. Representacion", "Legal representative, from RUT casilla 98.", "-"),
    ("2 / 123456-T", "Casillas 982 / 983 - Revisor fiscal and card number",
     "Signed by the statutory auditor.",
     "Required for a joint-stock company, or where gross assets reach 5,000 SMMLV or gross income "
     "reaches 3,000 SMMLV. Casilla 983 is mandatory once 982 is populated."),

    "CROSS-REPORT RECONCILIATION FROM THIS RETURN",
    ("617000", "= SUM(NIE177) for March 2026",
     "Casilla 93 must equal the sum of RetencionFuente across the month's validated nomina "
     "electronica documents.",
     "Reconcile on the UNROUNDED values with a per-employee tolerance, because the two artefacts "
     "round differently."),
    ("1 employee", "= count of validated NE documents", "One employee paid, one document.",
     "A mismatch means either an employee was paid without a document, or a document was rejected "
     "and never re-transmitted - both are tax-deductibility failures."),
    ("(not derivable)", "-> Formulario 220", "The twelve monthly returns do NOT produce Formulario 220.",
     "Colombia imposes no employer year-end reconciliation. Formulario 220 is a separate "
     "per-employee obligation built from the annual accumulation (CO-DIAN-004)."),
]

# ===========================================================================
#  SHEET 9 - SAMPLE FILE
# ===========================================================================
CFG["sample_title"] = "VERIFIED CHANNEL STATEMENT AND COMPLETED-FORM RENDERING"
CFG["sample"] = r"""
WHY THERE IS NO SAMPLE FILE
===========================
Formulario 350 is submitted as an ONLINE PORTAL FORM through the DIAN Servicios
Informaticos Electronicos (Muisca) at www.dian.gov.co, signed with the
Instrumento de Firma Electronica (IFE).

DIAN publishes NO XSD, NO cahier des charges and NO import template for this
form. Res. DIAN 000227 de 2025 art. 1.2.2.26 par. 1 states only that filers must
use "los Servicios Informaticos dispuestos por la entidad, utilizando el
Instrumento de Firma Electronica (IFE)", and that DIAN "pondra a disposicion el
Formulario numero 350 en forma virtual en la pagina web www.dian.gov.co para su
diligenciamiento y presentacion".

Fabricating an XML or CSV sample for this filing would therefore be inventing a
format that does not exist. What follows instead is a COMPLETED-FORM RENDERING -
the casilla-value set the engine must deliver to the portal operator or to the
robotic-process step that keys it. This is the actual deliverable.

Casillas marked [PORTAL] are computed by the DIAN service and must NOT be keyed.

-------------------------------------------------------------------------------
HOJA 1 - DECLARACION DE RETENCIONES EN LA FUENTE
Periodo: marzo de 2026        Vence: 12th business day of April 2026 (NIT ends 6)
-------------------------------------------------------------------------------
  1  Ano ................................................. 2026
  3  Periodo ............................................. 03
  4  Numero de formulario ................................ [PORTAL] 1120500123456
  5  Numero de Identificacion Tributaria (NIT) ........... 900123456
  6  DV .................................................. 7
  7  Primer apellido ..................................... (blank - legal person)
  8  Segundo apellido .................................... (blank - legal person)
  9  Primer nombre ....................................... (blank - legal person)
 10  Otros nombres ....................................... (blank - legal person)
 11  Razon social ........................................ MERCANS COLOMBIA S.A.S.
 12  Cod. Direccion seccional ............................ 32

 25  Cod. (correccion) ................................... (blank - initial return)
 26  Numero de formulario anterior ....................... (blank - initial return)

 27  Autorretenedores PJ exonerados art. 114-1 - CIIU .... (blank - not a self-withholder)
 28  Tarifa .............................................. [PORTAL] (blank)

     --- A titulo de impuesto sobre la renta y complementario ---
     Base sujeta a retencion sobre pagos a PERSONAS JURIDICAS
 29-41  Honorarios ... Otros pagos ....................... 0
     Retencion a titulo de renta a PERSONAS JURIDICAS
 42-54  Honorarios ... Otros pagos ....................... 0
 55  Base pagos al exterior sin convenio (PJ) ............ [PORTAL] 0
 56  Base pagos al exterior con convenio (PJ) ............ [PORTAL] 0
 57  Retencion pagos al exterior sin convenio (PJ) ....... [PORTAL] 0
 58  Retencion pagos al exterior con convenio (PJ) ....... [PORTAL] 0
 59-76  Autorretenciones personas juridicas .............. 0

     Base sujeta a retencion sobre pagos a PERSONAS NATURALES
 77  Rentas de trabajo ................................... 8.190.000   <== PAYROLL
 78  Rentas de pensiones ................................. 0
 79-92  Honorarios ... Otros pagos ....................... 0
     Retencion a titulo de renta a PERSONAS NATURALES
 93  Rentas de trabajo ................................... 617.000     <== PAYROLL
 94  Rentas de pensiones ................................. 0
 95-108  Honorarios ... Otros pagos ...................... 0
109  Base pagos al exterior sin convenio (PN) ............ [PORTAL] 0
110  Base pagos al exterior con convenio (PN) ............ [PORTAL] 0
111  Retencion pagos al exterior sin convenio (PN) ....... [PORTAL] 0
112  Retencion pagos al exterior con convenio (PN) ....... [PORTAL] 0
113-128  Autorretenciones personas naturales ............. 0

129  Menos retenciones practicadas en exceso o indebidas . 0
130  Total retenciones renta y complementario ............ [PORTAL] 617.000

131  Retencion IVA a responsables ........................ 0
132  Retencion IVA servicios a no residentes ............. 0
133  Menos retenciones IVA en exceso ..................... 0
134  Total retenciones IVA ............................... [PORTAL] 0
135  Retenciones impuesto de timbre nacional ............. 0

136  Total retenciones ................................... [PORTAL] 617.000
137  Sanciones ........................................... 0
138  Total retenciones mas sanciones ..................... [PORTAL] 617.000

139  No. Identificacion signatario ....................... 79123456
140  DV .................................................. 3
980  Pago total .......................................... 617.000
981  Cod. Representacion ................................. 01
982  Codigo Contador o Revisor Fiscal .................... 2
983  No. Tarjeta profesional ............................. 123456-T
994  Con salvedades ...................................... (unmarked)
997  Sello de la entidad recaudadora ..................... [DISPLAY-ONLY]

-------------------------------------------------------------------------------
HOJA 2 - ANEXO DE PAGOS AL EXTERIOR (non-resident variant)
Shown for the SAME employee treated as a NON-RESIDENT before acquiring residence
-------------------------------------------------------------------------------
Row 141 Convenio    142 Concepto  143 Tipo persona  144 Pais  145 Pagos      146 Tarifa  147 Retencion
--- --------------  ------------  ----------------  --------  ------------   ----------  -------------
 1  CON CONVENIO    24            Persona natural   ES        12.000.000     20,00       [PORTAL] 2.400.000

     Concepto 24 = "Rentas de trabajo": rentas de trabajo de cualquier naturaleza
     EN RELACION CON UN EMPLEO a favor de personas naturales no residentes.
     For a NON-treaty country the concept would be 5, "Prestaciones de servicios
     y compensacion por servicios personales".

148  Pagos al exterior sin convenio persona juridica ..... [PORTAL] 0    -> hoja 1 casilla 55
149  Pagos al exterior sin convenio persona natural ...... [PORTAL] 0    -> hoja 1 casilla 109
150  Retencion sin convenio persona juridica ............. [PORTAL] 0    -> hoja 1 casilla 57
151  Retencion sin convenio persona natural .............. [PORTAL] 0    -> hoja 1 casilla 111
152  Pagos al exterior con convenio persona juridica ..... [PORTAL] 0    -> hoja 1 casilla 56
153  Pagos al exterior con convenio persona natural ...... [PORTAL] 12.000.000  -> hoja 1 casilla 110
154  Retencion con convenio persona juridica ............. [PORTAL] 0    -> hoja 1 casilla 58
155  Retencion con convenio persona natural .............. [PORTAL] 2.400.000   -> hoja 1 casilla 112

-------------------------------------------------------------------------------
CONTRAST THAT MATTERS (v2.8 control B1)
-------------------------------------------------------------------------------
Same employee, same COP 12,000,000 salary, same month:

  RESIDENT      base  8.190.000 (depurated, ET art. 388)   withholding    617.000
  NON-RESIDENT  base 12.000.000 (GROSS, ET art. 408)       withholding  2.400.000

The non-resident withholding is 3.9 times the resident figure, and it is reported
on a DIFFERENT SHEET of the same return. An employee who acquires residence
mid-year moves from hoja 2 to hoja 1 PROSPECTIVELY, from the payment following
the date the 183-day test is met. The earlier months are never restated
(DIAN Concepto 011108 of 29 June 2026).

-------------------------------------------------------------------------------
FORMAT TO CONFIRM AGAINST A REAL FILING
-------------------------------------------------------------------------------
The casilla numbers, labels and arithmetic above are read directly off the
official form design and instructivo. What CANNOT be verified from public
sources is the portal's screen-level behaviour - field ordering, mandatory-field
prompts and any bulk-entry facility DIAN may offer to large filers. Confirm the
keying or robotic-process path against a real filing during implementation.
"""
