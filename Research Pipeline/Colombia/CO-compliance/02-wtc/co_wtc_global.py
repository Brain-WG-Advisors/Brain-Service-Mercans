# -*- coding: utf-8 -*-
"""
Colombia (CO) Wage Type Catalogue — global-baseline classifier (part 2)
=======================================================================
Configures ALL 300 codes of shared/Global_WTC_V1_0.xlsx FRESH for Colombia
2026. Returns (profile, formula, explanation, xml_element) per code.

Nothing here is inherited from another country. Every branch states the
Colombian statutory consequence: which of the THREE BASES the payment enters
(IBC / payroll-levy / withholding), whether it is salary under CST art. 127
or non-salary under CST art. 128, and whether the Ley 1393/2010 art. 30 40%
clamp can force it back into the IBC.
"""

from co_wtc_config import (
    SMMLV, UVT, AUX_TTE, IBC_CAP, FSP_TRIG, EXON_CUT, INTEGRAL, AUX_CAP,
    MEAL_CAP, MEAL_SAL, CESA_EXEMPT, DIVISOR,
    P_SAL, P_SAL_ADD, P_OT, P_NIGHT, P_COMM, P_TRANSP, P_NONSAL, P_NONSAL_A,
    P_GRATUITY, P_BIK_SAL, P_PRIMA, P_CESANT, P_VAC, P_LEAVE_P, P_NOTINC,
    P_MEAL3P, P_INCAP_ER, P_INCAP_EPS, P_INDEM, P_VIATICO, P_VOLPEN,
    P_RAISVOL, P_EQUITY, P_PENSION, P_UNPAID, P_ANTICIPO,
    P_DED, P_DED_ADD, P_ERC, P_RATE,
)

CLAMP = ("A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the "
         "Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK "
         "into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary "
         "for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its "
         "own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever.")

NORES = ("For a NON-RESIDENT this is withheld at the flat 20% on the gross under ET art. 408 with no "
         "depuration (DIAN Concepto 011108 de 2026); the switch to the art. 383 table is prospective from "
         "the payment following the 183rd day of presence.")


def classify_global(code, desc, gtype):
    """Return (profile, formula, explanation, xml_element) for one global code."""
    d = desc.lower()
    c = int(code)

    # =====================================================================
    # DEDUCTION-SIDE MECHANISM CODES (21xxx)
    # =====================================================================
    if gtype == "deduction":
        if c in (21610, 21611):
            return (P_DED,
                    "Employee mandatory health = IBC x 4.00%, rounded UP to the next multiple of 100 "
                    "(Decreto 1990 de 2016 art. 1); or a private health / life premium by written authorisation",
                    "Employee health withholding line, or a private health / life insurance premium deducted on "
                    "the employee's written authorisation for each case (CST art. 149 num. 1). The mandatory 4% "
                    "is NON-TAXABLE INCOME to the employee (ET art. 56) and is subtracted at step (B) of the "
                    "art. 388 depuration. Subjection columns NA - this is the deduction, not an earning.",
                    "Deducciones / Salud (NIE161, NIE163)")
        if c in (21640, 21641, 21642, 21645):
            return (P_DED,
                    "Employee mandatory pension = IBC x 4.00% (rounded UP to the next multiple of 100); "
                    "voluntary pension fund / AFC-AVC contributions on written authorisation",
                    "Employee pension withholding, and voluntary pension / long-term-savings deductions. The "
                    "mandatory 4% is NON-TAXABLE INCOME (ET art. 55); voluntary pension fund and AFC/AVC amounts "
                    "are EXEMPT INCOME inside the 40% and 1,340-UVT caps (ET arts. 126-1, 126-4), and voluntary "
                    "contributions to the individual pension account are non-taxable income within 25% of annual "
                    "labour income / 2,500 UVT. No pension contribution is due from an employed old-age pensioner "
                    "(PILA worker sub-type 01).",
                    "Deducciones / FondoPension (NIE164, NIE166); PensionVoluntaria (NIE198); AFC (NIE179)")
        if c == 21900:
            return (P_DED,
                    "Fondo de Solidaridad Pensional = IBC x 1.00% where IBC >= 4 SMMLV (" + FSP_TRIG + "), PLUS "
                    "the subsistence sub-account 0.2/0.4/0.6/0.8/1.0% by SMMLV band from 16 SMMLV",
                    "Solidarity pension fund - an EMPLOYEE-ONLY surcharge ADDITIONAL to the 4% pension, which "
                    "must NEVER be merged into the pension line: the nomina electronica carries FOUR separate "
                    "attributes (solidarity percentage and amount, subsistence percentage and amount). It is "
                    "non-taxable income (ET art. 55), grouped with the pension contribution on Formato 2276 "
                    "numeral N24. Not exonerable, employer share nil.",
                    "Deducciones / FondoSP (NIE167-NIE170)")
        if c == 21670:
            return (P_DED,
                    "Employee share of an employer benefits plan (prepaid medicine, complementary health plan, "
                    "group life), on written authorisation for each case",
                    "Post-tax benefits-plan deduction. A prepaid-medicine or health-insurance premium separately "
                    "generates an ET art. 387 lits. a) and b) DEDUCTION of up to 16 UVT per month (COP 837,984) "
                    "against the withholding base, provided the provider is supervised by the National Health "
                    "Superintendence or the Financial Superintendence.",
                    "Deducciones / PlanComplementarios (NIE182)")
        if c == 21800:
            return (P_DED_ADD,
                    "Recovery of an expense advance not supported by documentation",
                    "Recovery line for an unsubstantiated expense advance. Requires the employee's written "
                    "authorisation (CST art. 149 num. 1) and may not take pay below the SMMLV or into the "
                    "non-attachable portion without a court order (art. 149 num. 2).",
                    "Deducciones / Anticipos (NIE196)")
        if c == 21810:
            return (P_DED, "Employee parking charge, on written authorisation",
                    "Voluntary post-tax deduction. Written order signed for each case (CST art. 149 num. 1); "
                    "protected by the SMMLV floor.",
                    "Deducciones / OtrasDeducciones (NIE197)")
        if c == 21820:
            return (P_DED_ADD, "Employee-authorised donation (e.g. to an employee welfare fund)",
                    "Voluntary post-tax deduction; no withholding effect. Written authorisation required.",
                    "Deducciones / OtrasDeducciones (NIE197)")
        if c == 21890:
            return (P_DED_ADD, "Employee-borne exercise price / share-purchase amount recovered through payroll",
                    "Offsetting deduction against the equity earnings line, so that net cash pay is unchanged "
                    "while the withholding on the taxable spread is correctly computed (CCG Module 7.2).",
                    "Deducciones / OtrasDeducciones (NIE197)")
        if c == 21190:
            return (P_DED_ADD, "Reversal / recovery of an employer-paid disability top-up",
                    "Recovery counterpart of the long-term disability earnings line, typically where the EPS or "
                    "the pension administrator subsequently pays the certified benefit that the employer advanced.",
                    "Deducciones / Reintegro (NIE184)")
        if c in (21400, 21520):
            return (P_DED,
                    "Negative counterpart of the housing / transport allowance earnings line "
                    "(non-entitlement, absence or overpayment recovery)",
                    "Deduction counterpart. NOTE for the transport allowance: it is not payable for days of "
                    "unpaid leave, sickness incapacity or maternity / paternity leave (no travel occurs), so the "
                    "recovery line is a routine monthly event, prorated on the 30-day commercial month.",
                    "Deducciones / OtrasDeducciones (NIE197)")
        # generic negative counterparts: basic salary, overtime, salary addition, premium pay
        return (P_DED,
                "Negative recovery / adjustment counterpart of the matching earnings code "
                "(absence, overpayment, advance recovery); prorated S x days / 30",
                "Deduction mechanism, not remuneration. Subject to CST art. 149: no deduction without the "
                "employee's written order for each case or a court order, and none may breach the SMMLV floor or "
                "the non-attachable portion. Every subjection column NA.",
                "Deducciones / OtrasDeducciones (NIE197)")

    # =====================================================================
    # EMPLOYER CONTRIBUTION CODES (23xxx)
    # =====================================================================
    if gtype == "contribution":
        if c == 23640:
            return (P_ERC,
                    "Employer pension = IBC x 12.00% (NEVER exonerated); employer voluntary pension fund "
                    "contribution on the employee's behalf within 30% of labour income / 3,800 UVT",
                    "Employer pension liability. The 12% is never relieved by the ET art. 114-1 exoneration - "
                    "only employer health 8.5%, SENA 2% and ICBF 3% are. Rounded UP to the next multiple of 100. "
                    "A high-risk-activity employee (Decreto Ley 2090 de 2003) carries an ADDITIONAL employer "
                    "pension contribution: the Resolucion 2388 de 2016 rate table shows a 26% total against the "
                    "standard 16%, implying +10 percentage points employer-borne - see CO-ER-PENSION-ALTO-RIESGO, "
                    "an open item carried in the QA report.",
                    "PILA T2R2-046, T2R2-047, T2R2-050; not a nomina electronica element")
        if c == 23670:
            return (P_ERC,
                    "Employer share of a benefits plan (prepaid medicine, complementary health plan, group life)",
                    "Employer-borne benefit cost. Structured as NON-SALARY under a written CST art. 128 pact in "
                    "market practice, which keeps it out of the IBC, the levy base and the statutory-benefit base "
                    "- subject always to the 40% clamp. It is nonetheless a TAXABLE benefit to the employee (see "
                    "CO-MEDICINA-PREPAGADA-ER). No fringe-benefits tax exists in Colombia.",
                    "Devengados / Auxilio (AuxilioNS, NIE142) for the employee-side value")
        return (P_ERC,
                "Employer-borne contribution liability: health 8.5% + pension 12% + ARL 0.348-8.7% on the IBC; "
                "CCF 4% + SENA 2% + ICBF 3% on the Ley 21/1982 levy base (no ceiling); plus the statutory "
                "benefit accruals 8.3333% + 8.3333% + 1.0000% + 4.1667% = 21.8333%",
                "Employer contribution / accrual line, computed IN PARALLEL with the employee gross-to-net and "
                "never touching net pay. Employer health 8.5%, SENA 2% and ICBF 3% are EXONERATED where the "
                "employee earns STRICTLY LESS THAN 10 SMMLV (" + EXON_CUT + ") and the employer is an "
                "income-tax-filing legal person (ET art. 114-1); pension 12%, ARL and CCF 4% are never "
                "exonerated. Each amount rounds UP to the next multiple of 100.",
                "PILA T2R2-046 to T2R2-073; not a nomina electronica element")

    # =====================================================================
    # RATE LINE
    # =====================================================================
    if gtype == "rate":
        return (P_RATE,
                "Ordinary hour value = monthly salary / D, where D = " + DIVISOR + " "
                "(MinTrabajo Circular Externa 101 de 22 septiembre 2025)",
                "Rate driver, not a paid amount. THE HOURLY DIVISOR IS THE SINGLE BIGGEST 2026 CALCULATION "
                "CHANGE: the 42-hour week starts on 15 JULY 2026 (Ley 2101 de 2021 art. 3; CST art. 161 as "
                "substituted by Ley 2466 de 2025 art. 11), taking the divisor from 220 to 210. A July 2026 "
                "payroll spans BOTH divisors and must be split at 15 July. The legacy divisor of 240 is obsolete "
                "and understates every premium by about 14.3%.",
                "Derived - feeds every hour-type Pago element")

    # =====================================================================
    # EARNINGS FAMILIES (62xxx)
    # =====================================================================

    # --- family allowance: paid by the CCF to the employee, not by the employer ---
    if "family allowance" in d:
        return (P_NOTINC,
                "Subsidio familiar paid BY the Caja de Compensacion Familiar to the employee - not an employer "
                "payroll payment (the employer's obligation is the 4% CCF levy)",
                "OUT OF SCOPE per scope_manifest: the family subsidy is a CCF fund benefit paid to the employee "
                "by the fund, not a payment run through employer gross-to-net. Retained for global-code "
                "completeness and configured outside every base. The employer's related obligation is the CCF 4% "
                "levy on the Ley 21/1982 base, which is NEVER exonerated - see CO-ER-CCF.",
                "Not a nomina electronica element (fund-paid benefit)")

    # --- medical insurance / medical care: employer-paid prepaid health ---
    if "medical" in d:
        return (P_NONSAL,
                "Employer-paid prepaid medicine (medicina prepagada) or complementary health plan premium; "
                "employee may deduct up to 16 UVT/month (COP 837,984) against the withholding base",
                "Employer-paid prepaid health is NOT a statutory exclusion in Colombia - it is a TAXABLE benefit "
                "to the employee, reported as an earnings line and withheld in the ordinary monthly base. The "
                "employee separately obtains an ET art. 387 lits. a) and b) DEDUCTION of up to 16 UVT per month, "
                "on a provider certificate, where the provider is supervised by the National Health "
                "Superintendence or the Financial Superintendence. " + CLAMP,
                "Devengados / Auxilio (AuxilioNS, NIE142)")

    # --- per diem: CST art. 130 splits viaticos into a salary and a non-salary part ---
    if "per diem" in d:
        return (P_VIATICO,
                "Viaticos: the part destined to MANUTENCION and ALOJAMIENTO is salary; the part for TRANSPORT "
                "and REPRESENTATION EXPENSES is not. Occasional viaticos are never salary (CST art. 130)",
                "CST art. 130, verbatim: 'Los viaticos permanentes constituyen salario en aquella parte "
                "destinada a proporcionar al trabajador manutencion y alojamiento; pero no en lo que solo tenga "
                "por finalidad proporcionar los medios de transporte o los gastos de representacion. Siempre que "
                "se paguen debe especificarse el valor de cada uno de estos conceptos. Los viaticos accidentales "
                "no constituyen salario en ningun caso.' The value of EACH concept must therefore be specified "
                "on payment, and the nomina electronica enforces the split with PAIRED elements "
                "ViaticoManuAlojS (NIE072) and ViaticoManuAlojNS (NIE073). Configure two wage types, not one - "
                "see CO-VIATICOS-PERMANENTES and CO-VIATICOS-OCASIONALES.",
                "Devengados / Transporte - ViaticoManuAlojS (NIE072) / ViaticoManuAlojNS (NIE073)")

    # --- genuine reimbursements ---
    if "relocation" in d or "travel ticket" in d or "expense reimbursement" in d:
        return (P_NOTINC,
                "Genuine reimbursement of documented employer expenditure, or an amount given to enable the work "
                "(means of transport, work tools, representation expenses) - not remuneration",
                "CST art. 128 excludes sums given 'no para su beneficio, ni para enriquecer su patrimonio, sino "
                "para desempenar a cabalidad sus funciones'. Outside EVERY base - withholding, IBC, payroll-levy, "
                "statutory-benefit and vacation. Relocation and travel-ticket costs paid in the employer's "
                "interest and evidenced by documentation are reimbursements; a round, undocumented or "
                "habitual cash payment is instead ordinary salary and must be reclassified.",
                "Not a nomina electronica devengado where a true reimbursement; otherwise "
                "Devengados / OtroConcepto (NIE146-NIE148)")

    # --- transport allowance (the statutory auxilio de transporte) ---
    if "transportation allowance" in d:
        return (P_TRANSP,
                "Auxilio de transporte = " + AUX_TTE + " x days worked / 30, where the employee earns up to "
                "2 SMMLV (" + AUX_CAP + ") and public transport is available (Decreto 1470 de 2025 art. 1)",
                "THE COUNTER-INTUITIVE COLOMBIAN LINE. The statutory transport allowance is NOT salary and is "
                "therefore OUT of the IBC and OUT of the Ley 21/1982 payroll-levy base - but it IS in the "
                "statutory-benefit base, so it enters the prima de servicios, the cesantias and the interest on "
                "them. It is NOT in the vacation base. It is taxable income (usually within the 0% band). Not "
                "payable for days of unpaid leave, sickness incapacity or maternity / paternity leave. Prorated "
                "on the 30-day commercial month. A teleworker earning less than 2 SMMLV receives the auxilio de "
                "conectividad INSTEAD, never both (Ley 2466 de 2025 art. 53).",
                "Devengados / Transporte - AuxilioTransporte (NIE071)")

    # --- car & transportation allowance (cash) ---
    if "car & transportation" in d:
        return (P_SAL,
                "Cash car / transport allowance paid to the employee (not the statutory auxilio de transporte)",
                "A contractual CASH car or transport allowance is ordinary salary under CST art. 127 - direct "
                "consideration for the service - and enters every base. It must not be confused with the "
                "statutory auxilio de transporte (see CO-AUX-TRANSPORTE), nor with a means of transport supplied "
                "to enable the work, which is excluded by art. 128. " + NORES,
                "Devengados / Auxilio (AuxilioS, NIE141)")

    # --- car allowances, fuel, maintenance (cash) ---
    if "car" in d:
        return (P_SAL,
                "Cash car / fuel / maintenance allowance per contract",
                "Cash car, fuel and maintenance allowances are ordinary salary (CST art. 127) and enter the IBC, "
                "the payroll-levy base, the statutory-benefit base and the vacation base. A COMPANY CAR provided "
                "in kind for private use is instead salary in kind under art. 129, valued CONTRACTUALLY - "
                "Colombia has NO published company-car valuation scale, and art. 129 num. 2 routes an unvalued "
                "benefit to expert appraisal (estimacion pericial), not to a table. " + CLAMP,
                "Devengados / Auxilio (AuxilioS, NIE141)")

    # --- housing / rent allowances (cash) ---
    if "housing" in d or "rent allowance" in d:
        return (P_SAL,
                "Cash housing / rent allowance per contract; employer-provided housing in kind is salary in kind "
                "valued contractually, capped at 50% of total salary (30% at the SMMLV)",
                "A cash housing allowance is ordinary salary under CST art. 127 and enters every base. Housing "
                "supplied IN KIND is salary in kind under art. 129 - 'alimentacion, habitacion o vestuario que el "
                "empleador suministra al trabajador o a su familia' - which 'debe valorarse expresamente en todo "
                "contrato de trabajo', with expert appraisal in default of agreement, and which may not exceed "
                "50% of total salary, or 30% where the employee earns the legal minimum wage. Where the parties "
                "have an EXPRESS WRITTEN art. 128 non-salary pact over housing, reclassify to "
                "CO-BONIF-NOSALARIAL. " + CLAMP,
                "Devengados / Auxilio (AuxilioS, NIE141)")

    # --- education / schooling ---
    if "education" in d or "schooling" in d:
        return (P_SAL,
                "Cash education / schooling allowance per contract or collective agreement",
                "Colombia has NO statutory education or schooling exemption. A habitual cash education allowance "
                "is salary under CST art. 127 and enters every base; an EXPRESS WRITTEN art. 128 pact moves it to "
                "non-salary for labour purposes, subject to the 40% clamp, with NO tax effect. Distinguish "
                "'apoyos economicos educativos financiados con recursos publicos', which are reported separately "
                "(Formulario 220 casilla 51 / Formato 2276 numeral N16) and are outside private-sector payroll.",
                "Devengados / Auxilio (AuxilioS, NIE141); Deducciones / Educacion (NIE183) for an employee debt")

    # --- birth and marriage allowance ---
    if "birth and marriage" in d or "marriage" in d:
        return (P_GRATUITY,
                "One-off birth / marriage payment (mera liberalidad)",
                "An occasional, purely gratuitous payment is excluded from salary by CST art. 128 num. 1, so it "
                "is out of the statutory-benefit base and the vacation base - but it is FULLY TAXABLE employment "
                "income, and being a 'pago laboral no constitutivo de salario' it is counted in the Ley 1393 de "
                "2010 art. 30 40% clamp test. " + CLAMP,
                "Devengados / Bonificacion (BonificacionNS, NIE140)")

    # --- severance & seniority / statutory gratuity / EOS ---
    if ("severance & seniority" in d or "statutory gratuity" in d or "gratuity, eos" in d):
        return (P_CESANT,
                "Auxilio de cesantias = (monthly salary + auxilio de transporte) x days of service / 360; "
                "interest = cesantias balance x 12% x days / 360",
                "Cesantias and the interest on them are STATUTORY BENEFITS excluded from salary by CST art. 128, "
                "so out of the IBC and out of the payroll-levy base. They are EXCLUDED FROM THE MONTHLY "
                "WITHHOLDING BASE ENTIRELY under BOTH procedures (ET arts. 385 and 386) - not merely exempt - and "
                "the ET art. 206 num. 4 exemption is applied when the payment is made: exempt in full where the "
                "average monthly income of the last 6 months is <= 350 UVT (" + CESA_EXEMPT + "), then tapering "
                "90/80/60/40/20/0%. The 25% exemption of art. 206 num. 10 does NOT apply (art. 206 par. 2). "
                "Liquidated at 31 December and DEPOSITED TO THE EMPLOYEE'S FUND BY 14 FEBRUARY; late deposit "
                "costs one day's salary per day of delay. The interest is paid TO THE EMPLOYEE during January, "
                "not to the fund. Ley 2466 de 2025 art. 64 permits an 8.33% monthly advance deposit by agreement.",
                "Devengados / Cesantias - Pago (NIE120), Porcentaje (NIE121), PagoIntereses (NIE122)")

    # --- post-termination payments ---
    if "post-termination payment" in d or "gratuity, eos, post-termination" in d:
        return (P_INDEM,
                "Indemnizacion CST art. 64: below 10 SMMLV -> 30 days' salary for the first year + 20 days per "
                "subsequent year and pro rata; at or above 10 SMMLV (" + EXON_CUT + ") -> 20 days + 15 days",
                "Termination payments are FULLY TAXABLE ordinary employment income entering the ordinary monthly "
                "base, and are OUT of the IBC and the payroll-levy base. Colombia has NO concessional cap on "
                "termination payments: only the statutory-minimum indemnities of ET art. 206 nums. 1-3 are exempt "
                "and even those only up to the legal minimum amount (art. 206 par. 1). A negotiated "
                "mutual-termination bonus and a payment in lieu of notice are frequently and WRONGLY assumed "
                "exempt - they are not. Employees with 10 or more years of continuous service at the entry into "
                "force of Ley 789 de 2002 retain the earlier Ley 50 de 1990 art. 6 scale. Note the CST art. 65 "
                "par. 1 gate: the employer must evidence payment of the last three months' contributions within "
                "60 days of the termination, failing which the termination HAS NO EFFECT. " + NORES,
                "Devengados / Indemnizacion (NIE160); BonifRetiro (NIE159) for a settlement bonus")

    # --- stock options and grants ---
    if "stock option" in d:
        return (P_EQUITY,
                "Taxable spread = market value at exercise or vesting less the exercise price paid",
                "Equity and share-incentive awards are TAXABLE EMPLOYMENT INCOME AT EXERCISE OR VESTING, on the "
                "spread, entering the ordinary monthly base and the ET art. 383 table. The subsequent disposal is "
                "a separate capital transaction outside payroll. Generally non-salary (an occasional, "
                "non-consideration benefit) so out of the statutory-benefit and vacation bases, but " + CLAMP + " "
                "For a non-resident, ET art. 408 applies at 20% where the underlying service was performed in "
                "Colombia; where the service was performed abroad the income is foreign-source and not taxable.",
                "Devengados / OtroConcepto (NIE146-NIE148)")

    # --- 13th / 14th month -> prima de servicios ---
    if "supplemental basic" in d or "13th" in d or "14th" in d:
        return (P_PRIMA,
                "Prima de servicios = (monthly salary + auxilio de transporte) x days in the semester / 360, "
                "i.e. 30 days' salary per year - half by 30 June, half by 20 December",
                "The statutory service bonus is Colombia's 13th-month equivalent. CST art. 307: 'La prima anual "
                "no es salario, ni se computara como factor del salario en ningun caso' - so it is OUT of the "
                "IBC and OUT of the payroll-levy base. TAX TREATMENT DIVERGES SHARPLY BY PROCEDURE and is one of "
                "the most commonly mis-implemented rules in Colombian payroll: under PROCEDURE 1 the statutory "
                "minimum bonus is withheld SEPARATELY on its own read of the art. 383 table (ET art. 385) and is "
                "NOT added to the month's salary; under PROCEDURE 2 it is folded into the ordinary monthly base, "
                "the 13 divisor of art. 386 having already prorated its effect. Any excess above the statutory "
                "minimum goes to the ordinary monthly base under both. Contractual and Christmas bonuses are set "
                "off against it (CST art. 308). Absorbed by an all-inclusive salary.",
                "Devengados / Primas - Cantidad (NIE117), Pago (NIE118), PagoNS (NIE119)")

    # --- basic salary family ---
    if "basic salary" in d or "historic pay" in d:
        return (P_SAL,
                "Salario basico: full month = S; partial month = S x days worked / 30 (30-day commercial month, "
                "so February and a 31-day month are both 30 payroll days); minimum " + SMMLV + "/month",
                "Salario basico - the agreed remuneration for the ordinary working day, by unit of time, task, "
                "piece or output (CST art. 132 num. 1). Salary under CST art. 127, so it enters ALL THREE BASES: "
                "the IBC (floor 1 SMMLV pro-rated to contributory days, ceiling 25 SMMLV = " + IBC_CAP + ", "
                "rounded UP to the whole peso), the Ley 21/1982 payroll-levy base (NO ceiling), and the ET "
                "art. 388 withholding base. Also the base of the statutory benefits and of the CST art. 64 "
                "indemnity scale. NOT prorated: the 1-SMMLV contribution-base floor, so a low-paid part-month "
                "still contributes on the pro-rated minimum wage. " + NORES,
                "Devengados / Basico - DiasTrabajados (NIE069), SueldoTrabajado (NIE070)")

    # --- unpaid leave of absence ---
    if "unpaid loa" in d:
        return (P_UNPAID,
                "Unpaid absence = -(monthly salary x unpaid days / 30); the auxilio de transporte is likewise "
                "not payable for those days",
                "Licencia no remunerada / contract suspension. Reported on the PILA with the SLN change event, "
                "which reduces the contributory days: the Resolucion 2388 de 2016 rate table shows health moving "
                "to 8.5% or 0% and pension to 12% or 16% depending on the variant, and THE PAYROLL LEVIES FALLING "
                "TO 0%. Statutory-benefit and vacation accrual are SUSPENDED, although CST art. 53 permits the "
                "employer to count the period for cesantias and pension purposes if it pays the corresponding "
                "contributions. The month's taxable payments fall, so the withholding follows automatically.",
                "Devengados / LicenciaNR (NIE136-NIE138); PILA T2R2-024, T2R2-083, T2R2-084")

    # --- overtime ---
    if "overtime" in d:
        return (P_OT,
                "Day overtime = (S / D) x 1.25 x H; night overtime = (S / D) x 1.75 x H; on an obligatory rest "
                "day add the art. 179 premium (+80% to 30 Jun 2026, +90% from 1 Jul 2026). D = " + DIVISOR,
                "Overtime is SALARY by express statutory definition - CST art. 127 lists 'el valor del trabajo "
                "suplementario o de las horas extras' - so it is fully in the IBC and fully in the payroll-levy "
                "base, and in the prima / cesantias / interest base. IT IS EXCLUDED FROM THE VACATION BASE: "
                "CST art. 192 excludes ONLY 'el valor del trabajo en dias de descanso obligatorio y el valor del "
                "trabajo suplementario en horas extras'. Fully taxable - there is no preferential rate and no "
                "exempt overtime allowance in Colombia. CST art. 168 num. 4 is critical: each premium 'se produce "
                "de manera exclusiva, es decir, sin acumularse con ningun otro', so the night, day-overtime and "
                "night-overtime premiums are ALTERNATIVES; only the art. 179 rest-day premium is added to them. "
                "Volume limit: 2 hours per day and 12 per week (CST art. 22 of Ley 50 de 1990 as substituted by "
                "Ley 2466 de 2025 art. 13), so 56 total weekly hours to 14 July 2026 and 54 from 15 July. "
                "Ministry authorisation was abolished by Ley 2466 art. 12 and replaced by a mandatory "
                "supplementary-work REGISTER; failure to keep it lets inspectors suspend all overtime for six "
                "months. Reported with quantity, start and end time, percentage and amount per hour type.",
                "Devengados / HED (NIE074-078), HEN (NIE079-083), HEDDF (NIE089-093), HENDF (NIE099-103)")

    # --- long term disability ---
    if "long term disability" in d:
        return (P_INCAP_ER,
                "Employer-paid disability top-up beyond the certified EPS or pension-administrator benefit",
                "An employer-paid top-up is taxable and fully contributory (it is an employer payment in "
                "consideration of the relationship). The CERTIFIED BENEFIT ITSELF is paid by the EPS to day 180 "
                "(66.67% to day 90, 50% days 91-180) and thereafter by the pension administrator, is exempt "
                "within the statutory minimum (ET art. 206 nums. 1-2 and par. 1), and contributions CONTINUE on "
                "the base throughout (PILA change event IGE). Occupational incapacity is paid by the ARL at 100% "
                "of the IBC from the day after the event (change event IRL).",
                "Devengados / Incapacidad - Tipo (NIE126), Pago (NIE127)")

    # --- annual leave ---
    if "annual leave" in d:
        payout = "payout" in d
        return (P_VAC,
                ("Compensacion en dinero de vacaciones - up to HALF the accrued leave, on the employee's PRIOR "
                 "WRITTEN request (CST art. 189 num. 1)") if payout else
                "Vacaciones = (ordinary salary EXCLUDING overtime and rest-day work) x working days of vacation "
                "/ 30; variable pay -> average of the immediately preceding year; accrual 15 working days / 360",
                "VACATION IS NOT A STATUTORY BENEFIT - IT IS PAID REST, and the consequences are counter-"
                "intuitive and must be configured deliberately. Vacation pay ENTERS THE IBC (contributions "
                "continue during leave, PILA change event VAC/LR) and ENTERS THE PAYROLL-LEVY BASE, because "
                "Ley 21 de 1982 art. 17 expressly covers 'los verificados por descansos remunerados de ley y "
                "convencionales o contractuales'. Its own calculation base excludes overtime and rest-day work "
                "ONLY (CST art. 192), so the night premium and commissions STAY IN. The auxilio de transporte is "
                "NOT in the vacation base. An ALL-INCLUSIVE SALARY DOES NOT ABSORB VACATION (CST art. 132 num. 2 "
                "expressly excepts it), so vacation is owed on the FULL 100% while contributions run on 70%. "
                "Fully taxable.",
                "Devengados / VacacionesCompensadas (NIE115, NIE116)" if payout else
                "Devengados / VacacionesComunes (NIE109-NIE112)")

    # --- holiday allowance -> extra-statutory vacation bonus ---
    if "holiday allowance" in d:
        return (P_SAL,
                "Prima de vacaciones extralegal - a contractual amount paid on taking leave (commonly a "
                "proportion of one month's salary); no statutory entitlement exists",
                "There is NO statutory vacation bonus in Colombia - only the 15 working days of paid vacation and "
                "the prima de servicios. An extra-statutory prima de vacaciones is contractual: SALARY where it "
                "is habitual (CST art. 127 'primas, sobresueldos, bonificaciones habituales'), and therefore "
                "contributory and in every base, UNLESS the parties have expressly agreed IN WRITING that it does "
                "not constitute salary under art. 128, in which case reclassify to CO-BONIF-NOSALARIAL. "
                "Configured here as the conservative default - salary. " + CLAMP,
                "Devengados / Primas - PagoNS (NIE119) or Bonificacion (NIE139 / NIE140)")

    # --- on-call duty ---
    if "on-call" in d:
        return (P_SAL,
                "Recargo por disponibilidad / astreinte per contract or collective agreement; hours actually "
                "worked while on call are paid as ordinary or overtime hours with their own premia",
                "On-call / standby remuneration is direct consideration for the service, so SALARY under CST "
                "art. 127, entering the IBC, the payroll-levy base, the statutory-benefit base and the vacation "
                "base, and fully taxable. Colombia has no statutory on-call rate - the amount is contractual. "
                "Hours actually worked during the on-call window attract the ordinary, night, overtime or "
                "rest-day treatment on their own facts.",
                "Devengados / OtroConcepto - ConceptoS (NIE147)")

    # --- premium pay / shift premium -> recargo nocturno ---
    if "premium pay" in d or "shift" in d:
        return (P_NIGHT,
                "Recargo nocturno = (S / D) x 0.35 x H for hours in the 19:00-06:00 window; rest-day / holiday "
                "premium = (S / D) x 0.80 x H to 30 Jun 2026 and x 0.90 from 1 Jul 2026. D = " + DIVISOR,
                "THE NIGHT WINDOW MOVED. CST art. 160 as substituted by Ley 2466 de 2025 art. 10: day work is "
                "06:00-19:00 and night work is 19:00-06:00. Art. 160 par. 2 delayed entry into force by six "
                "months from the 25 June 2025 sanction, so the 19:00 boundary has applied SINCE 25 DECEMBER 2025 "
                "and governs the whole of 2026 - two extra hours a day now attract the 35% premium compared with "
                "the pre-reform 21:00 boundary. The night premium is salary, fully contributory, and UNLIKE "
                "overtime it STAYS IN THE VACATION BASE (CST art. 192 excludes only rest-day work and "
                "supplementary overtime hours). No night premium and no rest-day premium apply on the 6-hour / "
                "36-hour-week successive shift system (CST arts. 161(d) and 168 num. 1).",
                "Devengados / HRN (NIE084-NIE088), HRDDF (NIE094-NIE098), HRNDF (NIE104-NIE108)")

    # --- profit sharing ---
    if "profit sharing" in d or "profit-sharing" in d:
        return (P_GRATUITY,
                "Participacion de utilidades / excedentes per the company scheme; no statutory profit-sharing "
                "entitlement exists in Colombia",
                "CST art. 128 expressly excludes 'la participacion de utilidades' and solidarity-economy "
                "surpluses from salary, so profit sharing is out of the statutory-benefit and vacation bases - "
                "but it is FULLY TAXABLE employment income and, as a 'pago laboral no constitutivo de salario', "
                "it counts in the Ley 1393 de 2010 art. 30 40% clamp test. " + CLAMP,
                "Devengados / Bonificacion (BonificacionNS, NIE140)")

    # --- discretionary / one-time bonuses ---
    if "discretionary" in d or "one-time" in d:
        return (P_GRATUITY,
                "One-off discretionary amount (mera liberalidad), not habitual and not contractually owed",
                "An occasional and purely gratuitous sum is excluded from salary by CST art. 128 num. 1, so out "
                "of the statutory-benefit and vacation bases, but FULLY TAXABLE. THE HABITUALITY TEST IS THE "
                "RISK: CST art. 127 brings 'bonificaciones habituales' INTO salary, and a payment repeated year "
                "on year will not survive a UGPP contribution audit as occasional. Where the payment is habitual "
                "but the parties have an EXPRESS WRITTEN art. 128 pact, use CO-BONIF-NOSALARIAL. " + CLAMP,
                "Devengados / Bonificacion (BonificacionNS, NIE140)")

    # --- other bonuses and recognition awards ---
    if "bonus" in d or "recognition award" in d:
        return (P_SAL_ADD,
                "Contractual bonus (performance, sign-on, retention, referral) per the scheme; SALARY where "
                "habitual, non-salary only under an express written CST art. 128 pact",
                "Non-statutory bonuses are entirely contractual. They are SALARY if habitual - CST art. 127 "
                "expressly lists 'primas, sobresueldos, bonificaciones habituales' - and therefore contributory "
                "and in every base, UNLESS the parties have expressly agreed in writing that they do not "
                "constitute salary, subject always to the 40% clamp. Configured here as the conservative default "
                "- salary. Tax: no preferential bonus rate, no separate annualisation and no tax-free bonus "
                "allowance exists; the bonus enters the ordinary monthly base under both procedures (only the "
                "STATUTORY MINIMUM prima de servicios gets the separate art. 385 table read). " + CLAMP,
                "Devengados / Bonificacion - BonificacionS (NIE139) / BonificacionNS (NIE140)")

    # --- expat allowances ---
    if "expat" in d:
        return (P_SAL,
                "Expatriate / assignment allowance per the assignment letter; taxable and contributory on the "
                "same rates as a local employee",
                "Colombia applies NO separate expatriate contribution regime: a resident or non-resident foreign "
                "national employed under a Colombian contract carries FULL health, pension, occupational-risk and "
                "levy obligations at the ordinary rates. THE ONE DIVERGENCE IS TAX, AND IT IS THE SINGLE LARGEST "
                "CONFIGURATION RISK IN COLOMBIAN EXPATRIATE PAYROLL: until tax residence is acquired the "
                "withholding is a FLAT 20% ON THE GROSS under ET art. 408 with no depuration, no 25% exemption "
                "and no tax-free band, switching PROSPECTIVELY to the art. 383 table from the payment following "
                "the 183rd day of presence (DIAN Concepto 011108 de 29 junio 2026, which rejected applying "
                "art. 383 from day one in anticipation of residence). On COP 8,000,000 that is COP 1,600,000 of "
                "withholding against COP 92,049 for a resident - a 17-fold difference. ONE PENSION RELIEF EXISTS: "
                "a foreign employee who PROVES affiliation to a pension system abroad may opt out of Colombian "
                "pension affiliation on written election with evidence (Decreto 1072 de 2015 art. 2.2.1.2.1.4; "
                "PILA field T2R2-007 'extranjero no obligado a cotizar a pensiones').",
                "Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto (NIE147)")

    # --- pensions and pension refunds paid to the employee ---
    if "pension" in d:
        return (P_PENSION,
                "Pension or refund of pension savings paid by the pension administrator; taxable only on the "
                "monthly amount exceeding 1,000 UVT (COP 52,374,000)",
                "OUT OF SCOPE per scope_manifest - pension payments are made by the pension administrator, not by "
                "the employer, and the bono pensional is a transfer between regimes. Retained for global-code "
                "completeness. Where an employer does pay pension income it is taxable only above 1,000 UVT per "
                "month (ET art. 206 num. 5), the ET art. 388 40% limit expressly does not apply to pensions, "
                "pension substitution indemnities or refunds of pension savings, and the payment is reported at "
                "Formulario 220 casilla 50 and Formato 2276 numeral N21. A withdrawal of a voluntary "
                "individual-account contribution that fails the qualifying conditions is withheld at 35%.",
                "Not a nomina electronica devengado; Formulario 220 casilla 50 / Formato 2276 N21")

    # --- social raise / social allowance ---
    if "social raise" in d or "social allowance" in d:
        return (P_SAL,
                "Recurring social / cost-of-living supplement (sobresueldo) per contract or collective agreement",
                "A recurring supplement of a remunerative character is salary under CST art. 127 - the article "
                "expressly names 'primas, sobresueldos' - and enters the IBC, the payroll-levy base, the "
                "statutory-benefit base and the vacation base. Note that the PUBLIC-SECTOR prima especial and "
                "prima de costo de vida sit OUTSIDE the 40% and 1,340-UVT tax caps (ET art. 206 par. 4) but are "
                "out of Mercans private-sector scope; the engine must nonetheless carry the flag so it does not "
                "silently clamp them if such an employee is loaded.",
                "Devengados / OtroConcepto - ConceptoS (NIE147)")

    # --- benefits plan ---
    if "benefits plan" in d:
        return (P_NONSAL,
                "Employer-funded flexible-benefits value, typically structured as non-salary under a written "
                "CST art. 128 pact",
                "A benefits-plan value delivered as a habitual or occasional BENEFIT OR ALLOWANCE (food, "
                "housing, clothing) can validly be pacted non-salary in writing under CST art. 128 - the "
                "Colombian workhorse. Three tests for a valid pact: it must be (a) EXPRESS, (b) WRITTEN, and "
                "(c) attached to a benefit or allowance, not to consideration for the service itself. A "
                "'non-salary' label on what is plainly remuneration for work will not survive a UGPP "
                "contribution audit. " + CLAMP,
                "Devengados / Auxilio (AuxilioNS, NIE142)")

    # --- covid-19 allowance ---
    if "covid" in d:
        return (P_GRATUITY,
                "Extraordinary health-emergency aid (auxilio extraordinario), one-off and gratuitous",
                "An extraordinary, non-recurring aid payment is an occasional purely gratuitous sum under CST "
                "art. 128 num. 1, so out of the statutory-benefit and vacation bases, but FULLY TAXABLE. No "
                "Colombian statute exempts emergency aid from employment income. " + CLAMP,
                "Devengados / Auxilio (AuxilioNS, NIE142)")

    # --- personal / special allowances and salary additions ---
    if "allowance" in d or "salary addition" in d:
        return (P_SAL,
                "Recurring cash allowance / salary supplement per contract; SALARY where it is consideration for "
                "the service",
                "A recurring cash allowance of a remunerative character is salary under CST art. 127 and enters "
                "all three bases and the vacation base. Only two routes take it out of the IBC: an EXPRESS "
                "WRITTEN art. 128 non-salary pact over a genuine benefit or allowance (subject to the 40% clamp, "
                "no tax effect), or the art. 128 exclusion for amounts given to enable the work. " + CLAMP,
                "Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto - ConceptoS (NIE147)")

    # --- arrears / adjustments / advances that reached here ---
    if "arrears" in d:
        return (P_SAL_ADD,
                "Retroactive salary / allowance adjustment (retroactivo) for one or more prior periods",
                "Arrears are salary of the period to which they relate and enter every base. TWO ENGINE POINTS: "
                "for social security a retroactive increase is reported with a VSP (permanent) or VST "
                "(transitory) salary-variation change event on the PILA; for tax, a payment covering a period "
                "LONGER than a month is handled under the ET art. 385 mechanics (CCG Module 9.2), and where the "
                "increase takes the employee's MONTH TOTAL across 10 SMMLV (" + EXON_CUT + ") the ET art. 114-1 "
                "exoneration is lost FOR THE WHOLE MONTH - the test is on the month, not on the segment.",
                "Devengados / OtroConcepto - ConceptoS (NIE147); PILA T2R2-021 / T2R2-023")

    if "advance" in d:
        return (P_ANTICIPO,
                "Anticipo: an advance OF the period's salary, or a recoverable advance repaid by payroll "
                "deduction under a written CST art. 151 agreement",
                "CONDITIONAL BY DESIGN. Where the amount is an advance OF the period's salary it IS salary and "
                "enters every base in the period to which it relates. Where it is a recoverable advance or loan "
                "it is not remuneration at all: the nomina electronica carries paired Anticipos elements in both "
                "the devengados (NIE194) and the deducciones (NIE196) blocks precisely so the two legs net to "
                "zero. CST art. 151 requires the instalment and the amortisation period to be agreed IN WRITING, "
                "and the employer may not unilaterally reschedule; art. 149 num. 2 bars any recovery that would "
                "breach the SMMLV floor or the non-attachable portion without a court order.",
                "Devengados / Anticipos (NIE194); Deducciones / Anticipos (NIE196)")

    if "adjustment" in d:
        return (P_SAL_ADD,
                "In-period correction to the matching earnings code",
                "Adjustment mechanism carrying the same Colombian treatment as its parent earning. Where the "
                "correction affects a CLOSED social-security month the fix is a CORRECTION PLANILLA (type N) "
                "with paired A / C record groups, in which the sum of the contribution bases and of the day "
                "counts in the C records must be >= those in the A records - so the correction planilla is built "
                "for under-declaration, not over-declaration. Where it affects a filed Formulario 350, file a "
                "correction return (ET art. 589 applies within one year where the declared value falls).",
                "Devengados / OtroConcepto (NIE146-NIE148); nomina de ajuste (NIAE214)")

    # =====================================================================
    # DEFAULT — unknown earning -> conservative ordinary taxable salary
    # =====================================================================
    return (P_SAL,
            "Recurring cash remuneration of a remunerative character per contract",
            "Configured as ordinary taxable salary for Colombia: salary under CST art. 127, in the IBC (floor "
            "1 SMMLV, ceiling 25 SMMLV = " + IBC_CAP + "), in the Ley 21/1982 payroll-levy base (no ceiling), in "
            "the statutory-benefit and vacation bases, and in the ET art. 388 withholding base on the art. 383 "
            "table. This is the CONSERVATIVE default: it over-contributes rather than under-contributes, which "
            "is the correct direction of error against a UGPP audit. Confirm the classification with the "
            "Regulation Analyst before go-live if the payment is in truth a benefit or allowance capable of an "
            "art. 128 pact. " + NORES,
            "Devengados / OtroConcepto - ConceptoS (NIE147)")
