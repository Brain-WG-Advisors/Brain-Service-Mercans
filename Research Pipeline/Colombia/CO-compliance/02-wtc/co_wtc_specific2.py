# -*- coding: utf-8 -*-
"""
Colombia (CO) Wage Type Catalogue — Colombia-specific deductions, employer
contributions, bases, intermediaries and flags (part 3b).
"""

from co_wtc_config import (
    SMMLV, UVT, IBC_CAP, FSP_TRIG, EXON_CUT, INTEGRAL, SUB_TRIG,
    EX25_CAP, CAP1340, DIVISOR,
    P_DED, P_DED_ADD, P_TAX, P_ERC, P_BASE, P_INT, P_FLAG, P_RATE, P_NOTIONAL,
)
from co_wtc_specific import C

TOP_SUB = "35,018,100"   # 20 x SMMLV — top of the subsistence band
BAND0   = "4,975,530"    # 95 UVT — top of the 0% withholding band

# ===========================================================================
# EMPLOYEE DEDUCTIONS
# ===========================================================================
CO_DEDUCTIONS = [
    C("CO-DED-SALUD", "Health contribution (employee) 4%", "Aporte a Salud - Empleado (4%)", P_DED,
      "IBC x 4.00%, rounded UP to the next multiple of 100 (Decreto 1990 de 2016 art. 1)",
      "Ley 100 de 1993 art. 204 as substituted by Ley 1122 de 2007 art. 10 (total 12.5%: employee 4% + "
      "employer 8.5%). Base = the IBC, floor 1 SMMLV (" + SMMLV + "), ceiling 25 SMMLV (" + IBC_CAP + "), so "
      "the maximum monthly amount is " + SMMLV + ". NON-TAXABLE INCOME to the employee (ET art. 56), "
      "subtracted at step (B) of the art. 388 depuration BEFORE the 40% cap reference figure is struck. "
      "Payable by every employee, including an employed old-age pensioner. Rounds UP to the next multiple "
      "of 100 - one of the THREE ROUNDING REGIMES coexisting in a single Colombian payroll month, alongside "
      "the nomina electronica's round-half-to-even with a +/-2.00 tolerance and the DIAN forms' rounding to "
      "the nearest 1,000 (ET art. 577). Never unify them.",
      "Deducciones / Salud - Porcentaje (NIE161), Deduccion (NIE163); PILA T2R2-054, T2R2-055"),

    C("CO-DED-PENSION", "Mandatory pension contribution (employee) 4%",
      "Aporte a Pension Obligatoria - Empleado (4%)", P_DED,
      "IBC x 4.00%, rounded UP to the next multiple of 100; 0% for an employed old-age pensioner",
      "Ley 100 de 1993 art. 20 as substituted by Ley 797 de 2003 art. 7 (total 16%: employee 4% + employer "
      "12%). Ceiling verified verbatim in Ley 797 art. 5: 'El limite de la base de cotizacion sera de "
      "veinticinco (25) salarios minimos legales mensuales vigentes para trabajadores del sector publico y "
      "privado.' NON-TAXABLE INCOME (ET art. 55). NOT PAYABLE by an employed old-age pensioner - neither the "
      "4% employee nor the 12% employer share is due, and the employee is reported with PILA worker sub-type "
      "01, while health, occupational risk and the levies continue. A foreign employee who PROVES affiliation "
      "to a pension system abroad may opt out on written election with evidence (Decreto 1072 de 2015 "
      "art. 2.2.1.2.1.4; PILA field T2R2-007 'extranjero no obligado a cotizar a pensiones'). Where the "
      "employee has two or more employers the contributions are proportional to each remuneration and "
      "accumulate against the SHARED 25-SMMLV ceiling, and health must use the same base (Ley 100 art. 18 "
      "par. 1). NEWEST-LAW CHECK: Ley 2381 de 2024 replaces the whole pension architecture, but its entry "
      "into force was suspended by Constitutional Court Auto 841 de 18 junio 2025 and deferred to 1 APRIL "
      "2027 by Judgment C-264 de 25 agosto 2026 - NO PART OF IT MAY BE CONFIGURED AS LIVE FOR ANY 2026 "
      "PERIOD. It leaves the 16% total and the 12/4 split unchanged in any event (expressed as 75% / 25% of "
      "the total contribution).",
      "Deducciones / FondoPension - Porcentaje (NIE164), Deduccion (NIE166); PILA T2R2-046, T2R2-047"),

    C("CO-DED-FSP-SOLIDARIDAD", "Solidarity pension fund - solidarity sub-account 1%",
      "Fondo de Solidaridad Pensional - Subcuenta de Solidaridad (1%)", P_DED,
      "IBC x 1.00% where the IBC is >= 4 SMMLV (" + FSP_TRIG + "), rounded UP to the next multiple of 100",
      "Ley 100 de 1993 art. 20 as substituted by Ley 797 de 2003 art. 7. EMPLOYEE-ONLY and ADDITIONAL to the "
      "4% pension - it must NEVER be merged into the pension line. Tested on the MONTHLY IBC, so a "
      "variable-pay employee can legitimately cross the trigger in different directions in successive "
      "months. NON-TAXABLE INCOME (ET art. 55), confirmed by Formato 2276 numeral N24, which groups the "
      "pension and solidarity contributions on one line. Subject to the same 25-SMMLV ceiling. The nomina "
      "electronica requires FOUR separate attributes for the fund - solidarity percentage and amount, "
      "subsistence percentage and amount. This two-account structure is REPLACED by a single five-band "
      "1.5%-3.0% scale on 1 April 2027 under Ley 2381 de 2024 art. 20 nums. 1-5 - the one employee-facing "
      "deduction that reform changes - and is NOT live for any 2026 period.",
      "Deducciones / FondoSP - Porcentaje (NIE167), DeduccionSP (NIE168); PILA T2R2-051"),

    C("CO-DED-FSP-SUBSISTENCIA", "Solidarity pension fund - subsistence sub-account 0.2%-1.0%",
      "Fondo de Solidaridad Pensional - Subcuenta de Subsistencia (0,2%-1,0%)", P_DED,
      "IBC x 0.2% / 0.4% / 0.6% / 0.8% / 1.0% for an IBC in the 16-17 / 17-18 / 18-19 / 19-20 / above-20 "
      "SMMLV band; trigger 16 SMMLV = " + SUB_TRIG + "; rounded UP to the next multiple of 100",
      "Ley 100 de 1993 art. 20 as substituted by Ley 797 de 2003 art. 7. EMPLOYEE-ONLY, additional to both "
      "the 4% pension and the 1% solidarity account, so the total employee solidarity surcharge runs from "
      "1.0% at 4 SMMLV to 2.0% above 20 SMMLV (" + TOP_SUB + "), taking the total employee burden from 8.0% "
      "to 10.0%. Non-taxable income (ET art. 55). Reported as its own pair of nomina electronica attributes "
      "and its own PILA field, separate from the solidarity sub-account.",
      "Deducciones / FondoSP - PorcentajeSub (NIE169), DeduccionSub (NIE170); PILA T2R2-052"),

    C("CO-RETENCION-FUENTE", "Income tax withholding on work income (resident)",
      "Retencion en la Fuente sobre Rentas de Trabajo", P_TAX,
      "PROCEDURE 1 (ET art. 385): read the art. 383 table on the month's art. 388 depurated base - 0% to 95 "
      "UVT (" + BAND0 + "), then 19% / 28% / 33% / 35% / 37% / 39% above 95 / 150 / 360 / 640 / 945 / 2,300 "
      "UVT. PROCEDURE 2 (art. 386): fixed % = table(sum of the preceding 12 months' taxable payments / 13), "
      "recomputed each JUNE and DECEMBER and applied to the month's depurated base",
      "THE ONLY PAYROLL WITHHOLDING IN COLOMBIA - there is no employer payroll tax on income and no local, "
      "municipal, departmental, church or solidarity surcharge on employment income. NON-CUMULATIVE: each "
      "month stands alone under Procedure 1, and there is NO employer year-end true-up of any kind - the "
      "employee reconciles in their own annual return. TWO ORDERING RULES DOMINATE: (1) the 25% exempt income "
      "of art. 206 num. 10 is computed LAST, on the figure net of non-taxable income, the art. 387 deductions "
      "and other exempt income - computing 25% of GROSS overstates it and under-withholds; (2) the "
      "72-UVT-per-dependant deduction of art. 336 num. 3 sits OUTSIDE the 40% and 1,340-UVT caps. Caps: "
      "(D+E) <= 40% of (C = A - B) AND <= 1,340 UVT/year (" + CAP1340 + "/month as apportioned), with the 25% "
      "exemption itself capped at 790 UVT/year (" + EX25_CAP + "/month). CESANTIAS AND THEIR INTEREST NEVER "
      "ENTER THE MONTHLY BASE under either procedure. A SUB-30-DAY PERIOD IS A PERCENTAGE RULE, NOT AN AMOUNT "
      "RULE: divide the payments by the days, multiply by 30, read the table PERCENTAGE, then apply that "
      "percentage to the actual smaller payment (art. 385) - reading the table for an AMOUNT on the grossed-up "
      "figure would grossly over-withhold. The employee may request a HIGHER rate in writing, effective from "
      "the month AFTER the request (art. 383 par. 3); it overrides upward only, never downward. Where an "
      "identifier or an employee declaration is missing there is NO penalty rate - the employee simply loses "
      "the deduction and is over-withheld.",
      "Deducciones / RetencionFuente (NIE177); Formulario 350 casillas 77 and 93"),

    C("CO-RETENCION-NO-RESIDENTE", "Income tax withholding - non-resident (flat 20%)",
      "Retencion en la Fuente a No Residentes (20% - ET art. 408)", P_TAX,
      "gross payment x 20%, with NO art. 388 depuration, NO art. 387 deductions, NO 25% exempt income and NO "
      "tax-free band - 20% from the first peso",
      "ET art. 408. THE SINGLE LARGEST CONFIGURATION RISK IN COLOMBIAN EXPATRIATE PAYROLL: on COP 8,000,000 "
      "the withholding is COP 1,600,000 against COP 92,049 for a resident - a 17-fold difference on the same "
      "salary. THE RESIDENCE SWITCH IS PROSPECTIVE, NEVER RETROACTIVE: DIAN Concepto 011108 de 29 junio 2026, "
      "upholding Concepto 1789 int. 14595 de 2025, rejected the argument that a foreign employee on a "
      "contract exceeding 183 days may be withheld under art. 383 from day one in anticipation of future "
      "residence. Withholding is determined AT THE MOMENT OF EACH PAYMENT on the status then held, and the "
      "switch to the art. 383 table takes effect FROM THE PAYMENT FOLLOWING the date the 183-day test of "
      "art. 10 is met, with NO true-up of the earlier months through payroll. Where the service is performed "
      "ENTIRELY OUTSIDE COLOMBIA by a non-resident the income is foreign-source and there is NO WITHHOLDING "
      "AT ALL (DIAN Oficio 28380 de 2019). Non-residents are IN SCOPE for Mercans Colombia payroll - a "
      "foreign national employed under a Colombian contract before acquiring residence is a common case - so "
      "the engine must carry a residence flag with an effective date and support the mid-year switch. Treaty "
      "relief is a CLIENT DECISION requiring a residence certificate and is applied only on written client "
      "instruction.",
      "Deducciones / RetencionFuente (NIE177); Formulario 350 casillas 109-112 and hoja 2 casillas 141-155"),

    C("CO-DED-PENSION-VOLUNTARIA", "Voluntary pension fund contribution (employee)",
      "Aporte Voluntario a Fondo de Pensiones Voluntarias", P_DED,
      "Amount authorised in writing, within the SHARED cap of the lower of 30% of labour income or 3,800 UVT "
      "per year = COP 199,021,200 (shared with AFC / AVC)",
      "ET art. 126-1. EXEMPT INCOME, subtracted at step (E) of the depuration INSIDE the 40% and 1,340-UVT "
      "caps - so it is LESS valuable than a voluntary contribution to the individual pension account, which "
      "is non-taxable income deducted before the cap reference figure is struck. Employer contributions on "
      "the employee's behalf count toward the SAME cap and are exempt income in the employee's hands. "
      "Requires the employee's written authorisation and a fund certificate. Reported at Formulario 220 "
      "casilla 56 / Formato 2276 numeral N26.",
      "Deducciones / PensionVoluntaria (NIE198)"),

    C("CO-DED-AFC-AVC", "AFC / AVC long-term savings contribution (employee)",
      "Aporte a Cuentas AFC / AVC", P_DED,
      "Amount authorised in writing, within the SAME shared 30% / 3,800-UVT annual cap as the voluntary "
      "pension fund",
      "ET art. 126-4 - construction-savings (AFC) and long-term-savings (AVC) accounts. EXEMPT INCOME inside "
      "the 40% and 1,340-UVT caps, sharing ONE combined annual limit with the voluntary pension fund, so the "
      "engine must maintain a SINGLE shared accumulator across both vehicles, not two. Evidenced by a "
      "financial-institution certificate. Reported at Formulario 220 casillas 57 and 58 / Formato 2276 "
      "numerals N27 and N28, which are separate lines for the two account types.",
      "Deducciones / AFC (NIE179)"),

    C("CO-DED-RAIS-VOLUNTARIO", "Voluntary contribution to the individual pension account (employee)",
      "Cotizacion Voluntaria al Regimen de Ahorro Individual (RAIS)", P_DED,
      "Amount authorised in writing, within the lower of 25% of annual labour income or 2,500 UVT per year "
      "= COP 130,935,000",
      "ET art. 55. NON-TAXABLE INCOME, deducted at step (B) BEFORE the 40% cap reference figure is struck, "
      "which makes it MATERIALLY MORE VALUABLE than exempt income and the single most efficient voluntary "
      "vehicle in the Colombian depuration. Available to employees affiliated to the private "
      "individual-account regime. A WITHDRAWAL THAT DOES NOT MEET THE QUALIFYING CONDITIONS IS WITHHELD AT "
      "35%. Evidenced by a pension administrator certificate; reported on the PILA as the AVP change event "
      "and at Formulario 220 casilla 55 / Formato 2276 numeral N25.",
      "Deducciones / OtrasDeducciones (NIE197); PILA T2R2-028, T2R2-048, T2R2-053"),

    C("CO-DED-SINDICATO", "Union dues", "Cuota Sindical", P_DED,
      "Percentage or amount fixed by the union's statutes, deducted at the union's request for its members",
      "CST art. 150 - one of the deductions requiring NO individual written order from the employee. "
      "Post-tax, with no withholding effect. May NOT reduce pay below the SMMLV or into the non-attachable "
      "portion (art. 149 num. 2), so it ranks behind mandatory social security, withholding tax and "
      "court-ordered garnishments and must be SUSPENDED for the period where the protected floor is reached, "
      "with the arrears made visible on the payslip. The nomina electronica carries both a percentage and an "
      "amount attribute.",
      "Deducciones / Sindicato - Porcentaje (NIE171), Deduccion (NIE172)"),

    C("CO-DED-COOPERATIVA", "Cooperative and employee savings-fund dues",
      "Aportes a Cooperativas y Fondos de Empleados", P_DED,
      "Amount fixed by the cooperative or fund, where legally authorised",
      "CST art. 150 - no individual written order required where the cooperative or savings fund is legally "
      "authorised. Post-tax, no withholding effect, protected by the SMMLV floor. NOTE THE ASYMMETRY: a "
      "cooperative DEBT enforced by court order falls within the CST art. 156 exception and may reach up to "
      "50% OF THE WHOLE SALARY including the minimum-wage portion, whereas an ordinary voluntary cooperative "
      "due may not breach the floor at all.",
      "Deducciones / Cooperativa (NIE180)"),

    C("CO-DED-SANCION-DISCIPLINARIA", "Disciplinary sanction", "Sancion Disciplinaria", P_DED_ADD,
      "Amount fixed by the duly approved reglamento interno de trabajo",
      "CST art. 150 permits the deduction with NO individual written order, but ONLY where the sanction is "
      "imposed under a DULY APPROVED set of work rules - the engine must therefore carry a flag confirming "
      "that an approved reglamento exists, because without one the deduction is unlawful. Post-tax, no "
      "withholding effect, protected by the SMMLV floor. The nomina electronica distinguishes a PUBLIC "
      "sanction (SancionPublic) from a PRIVATE one (SancionPriv).",
      "Deducciones / Sancion - SancionPublic (NIE173) / SancionPriv (NIE174)"),

    C("CO-DED-SABES", "Higher-education solidarity contribution",
      "Contribucion Solidaria a la Educacion Superior (Contribucion Sabes)", P_DED,
      "Amount fixed under the scheme for a beneficiary of the higher-education credit programme",
      "Added to the CST art. 150 list of permitted deductions by LEY 1911 DE 2018 ART. 22, so it requires NO "
      "individual written order. IT IS A DEDUCTION, NOT A TAX - it must not be aggregated with the retencion "
      "en la fuente on Formulario 350, which is the most common misclassification of this line. Post-tax, no "
      "withholding effect, protected by the SMMLV floor.",
      "Deducciones / Educacion (NIE183) or OtrasDeducciones (NIE197)"),

    C("CO-DED-LIBRANZA", "Payroll lending repayment", "Libranza (Ley 1527 de 2012)", P_DED,
      "Instalment fixed in the libranza authorisation; the AGGREGATE of libranza deductions must leave the "
      "employee at least 50% OF NET SALARY after all statutory deductions",
      "Ley 1527 de 2012. Requires the employee's written authorisation, after which the employer MUST deduct "
      "and remit the instalment to the lender - CST art. 149 num. 3 makes the employer LIABLE IN DAMAGES "
      "('responsable de los perjuicios') for failing to make an authorised, lawful deduction in good time, so "
      "an employer that quietly drops a libranza can be sued by the lender. Competing libranzas are applied "
      "in DATE ORDER OF THE AUTHORISATIONS. Post-tax, no withholding effect. Two floors bind simultaneously: "
      "the art. 149 num. 2 SMMLV / non-attachable floor and the Ley 1527 50%-of-net floor.",
      "Deducciones / Libranza - Descripcion (NIE175), Deduccion (NIE176)"),

    C("CO-DED-PRESTAMO", "Employer loan and advance recovery",
      "Prestamo y Anticipo del Empleador (CST art. 151)", P_DED,
      "Instalment agreed IN WRITING, stating the instalment amount and the amortisation period",
      "CST art. 151 permits written agreements on loans, advances and set-offs. THE EMPLOYER MAY NOT "
      "UNILATERALLY RESCHEDULE - art. 151 requires the instalment and the amortisation period to be agreed in "
      "writing, and unilateral variation entitles the employee to go to the labour inspector. Where the "
      "protected floor is reached the instalment must be SUSPENDED for the period and carried forward, "
      "notified on the payslip as an explicit informational line so the arrears are visible; the shortfall "
      "may never be recovered by set-off in a later period without a fresh written authorisation, and never "
      "at a rate that breaches the floor again. Post-tax, no withholding effect.",
      "Deducciones / Anticipos (NIE196) or Deuda (NIE185)"),

    C("CO-DED-EMBARGO", "Judicial or tax attachment", "Embargo Judicial o Fiscal", P_DED,
      "Up to 20% (ONE FIFTH) of the EXCESS OVER THE SMMLV - CST art. 155. On COP 3,000,000 the excess is "
      "1,249,095 and the maximum attachable is 249,819",
      "CST art. 154 makes salary UNATTACHABLE as the general rule; art. 155 opens only the excess over the "
      "minimum wage, and only to one fifth of that excess. A TAX LEVY BY DIAN counts as a court order for "
      "CST art. 149 purposes because the tax authority holds jurisdictional powers under ET arts. 823 et "
      "seq. and may issue an attachment order without going to court; UGPP social-security enforcement is "
      "treated the same way. Competing ordinary attachments share the art. 155 headroom IN DATE ORDER OF "
      "SERVICE on the employer. WHERE COMPETING ORDERS EXCEED THE CEILING the employer applies them in "
      "priority to the cap and NOTIFIES the court or authority whose order cannot be satisfied, stating the "
      "competing orders and the amounts applied - it must NOT apportion pro rata on its own initiative and "
      "must NOT exceed the ceiling to satisfy all orders. Post-tax, no withholding effect.",
      "Deducciones / EmbargoFiscal (NIE181)"),

    C("CO-DED-ALIMENTOS", "Maintenance / child-support garnishment", "Embargo por Alimentos", P_DED,
      "Up to 50% OF THE WHOLE SALARY, INCLUDING THE MINIMUM-WAGE PORTION - CST art. 156",
      "CST art. 156 is the one broad exception to Colombia's otherwise robust salary protection: for "
      "MAINTENANCE obligations and debts owed to COOPERATIVES, up to half the whole salary is attachable, "
      "minimum wage included. Maintenance ranks FIRST among garnishments - the obligation is of "
      "constitutional rank (Political Constitution art. 44, the prevailing rights of the child) - and it may "
      "lawfully take net pay BELOW the minimum wage, which no voluntary deduction ever can. Served by "
      "judicial order from a family judge, or a conciliation agreement approved by a family commissioner or "
      "the ICBF, on receipt of which the employer becomes a RETAINING AGENT and must acknowledge the order, "
      "apply it from the next payroll falling due after service, remit to the specified account, report any "
      "termination, unpaid leave or salary change affecting it, and keep the order and remittance evidence "
      "for the retention period. THE TWO CEILINGS ARE NOT CUMULATIVE ALLOWANCES: art. 156 (50% of the whole) "
      "and art. 155 (20% of the excess) are different ceilings for different claim types - apply the "
      "maintenance order first within its own 50% ceiling, then the commercial attachment only to the extent "
      "that the art. 155 headroom on the excess over the SMMLV remains unused.",
      "Deducciones / EmbargoFiscal (NIE181) or PagosTerceros (NIE195)"),

    C("CO-DED-MEDICINA-PREPAGADA", "Prepaid health / supplementary plan (employee share)",
      "Medicina Prepagada y Plan Complementario - Empleado", P_DED,
      "Premium authorised in writing; separately generates an ET art. 387 DEDUCTION of up to 16 UVT/month "
      "= COP 837,984 against the withholding base",
      "A POST-TAX PAYROLL DEDUCTION requiring the employee's written authorisation for each case (CST "
      "art. 149), which SEPARATELY generates a withholding-base deduction under ET art. 387 lits. a) and b) "
      "on a provider certificate, provided the provider is supervised by the National Health Superintendence "
      "(prepaid medicine) or the Financial Superintendence (health insurance). The two are distinct "
      "mechanisms and BOTH must be configured: the cash deduction from net pay, and the reduction of the "
      "taxable base. It does not replace the compulsory 12.5% health contribution.",
      "Deducciones / PlanComplementarios (NIE182)"),

    C("CO-DED-OTRAS", "Other authorised deduction", "Otras Deducciones Autorizadas", P_DED,
      "Amount authorised in writing by the employee for each case (CST art. 149 num. 1)",
      "Catch-all for employee-authorised voluntary deductions - insurance premiums other than qualifying "
      "health cover, employee purchases of the employer's goods and services, funeral funds and welfare "
      "funds. CST art. 149 num. 1 is the controlling rule: the employer 'no puede deducir, retener o "
      "compensar suma alguna del salario, sin orden suscrita por el trabajador para cada caso, o sin "
      "mandamiento judicial'. Post-tax, no withholding effect, protected by the SMMLV floor.",
      "Deducciones / OtrasDeducciones (NIE197)"),
]

# ===========================================================================
# EMPLOYER CONTRIBUTIONS, LEVIES AND STATUTORY-BENEFIT ACCRUALS
# ===========================================================================
CO_EMPLOYER = [
    C("CO-ER-SALUD", "Health contribution (employer) 8.5%", "Aporte a Salud - Empleador (8,5%)", P_ERC,
      "IBC x 8.50%, rounded UP to the next multiple of 100; ZERO where the ET art. 114-1 exoneration applies",
      "Ley 100 de 1993 art. 204 (total 12.5%). EXONERATED where the employee earns STRICTLY LESS THAN 10 "
      "SMMLV (" + EXON_CUT + ") and the employer is an income-tax-filing legal person - a natural-person "
      "employer qualifies only if it employs two or more workers (ET art. 114-1). THE EXONERATION IS TESTED "
      "PER EMPLOYEE, PER MONTH, on what the employee devenga that month, so an overtime or commission month "
      "can lose it, and where a mid-month increase takes the MONTH TOTAL across the line the exoneration is "
      "lost for the WHOLE month - the test is on the month, not on the segment. AT EXACTLY 10 SMMLV THE "
      "EXONERATION IS LOST, costing the employer approximately COP 2,363,800 per month and taking the "
      "employer cost factor from about 1.3836 to about 1.52 - the single largest step-change in Colombian "
      "employer cost. Reported on the PILA with the exoneration flags A1-033 (employer level) and T2R2-076 "
      "(contributor level).",
      "PILA T2R2-054, T2R2-055; A1-033; T2R2-076"),

    C("CO-ER-PENSION", "Mandatory pension contribution (employer) 12%",
      "Aporte a Pension Obligatoria - Empleador (12%)", P_ERC,
      "IBC x 12.00%, rounded UP to the next multiple of 100; NEVER exonerated",
      "Ley 100 de 1993 art. 20 as substituted by Ley 797 de 2003 art. 7 (total 16%). NEVER RELIEVED by the "
      "ET art. 114-1 exoneration - only employer health 8.5%, SENA 2% and ICBF 3% are exonerable. Not due "
      "for an employed old-age pensioner. The employer pays its own share and withholds the employee's share "
      "at the moment of payment (Ley 100 art. 22). Ley 2381 de 2024 leaves both the 16% total and the 12/4 "
      "split unchanged when it takes effect on 1 April 2027.",
      "PILA T2R2-046, T2R2-047, T2R2-050"),

    C("CO-ER-ARL", "Occupational risk contribution (employer)",
      "Aporte a Riesgos Laborales - ARL (0,348%-8,7%)", P_ERC,
      "IBC x the work centre's class rate. Class INITIAL rates: I 0.522%, II 1.044%, III 2.436%, IV 4.350%, "
      "V 6.960%. Global bounds 0.348% to 8.700%. Rounded UP to the next multiple of 100",
      "Decreto 1772 de 1994 art. 13, compiled in Decreto 1072 de 2015 arts. 2.2.4.3.4 and 2.2.4.3.5. "
      "EMPLOYER-ONLY - the employee rate is 0.00%. NEVER exonerated. 'Todo empleador que se afilie por "
      "primera vez al Sistema General de Riesgos Laborales cotizara por el valor correspondiente al valor "
      "inicial de la clase de riesgo que le corresponda', and the initial rates are independently "
      "corroborated by the Resolucion 2388 de 2016 rate tables. THE CLASS VARIES BY WORK CENTRE, NOT BY "
      "GEOGRAPHY, so one company can legitimately carry two classes and two rates; where a person performs "
      "several occupations they contribute at the HIGHEST class (Decreto 1072 art. 2.2.4.2.5.6). A DEFECT IN "
      "AN OFFICIAL DOCUMENT, RECORDED FOR TRACEABILITY: Decreto 1072 art. 2.2.4.3.5 prints the CLASS IV "
      "MAXIMUM AS 6.060%, while some secondary transcriptions state 6.960% - which is in fact class V's "
      "INITIAL rate and no class IV figure at all; the correct class IV maximum is 6.060%, verified against "
      "the government compilation of Decreto 1772 de 1994 art. 13. DO NOT CONFUSE TABLES: the 11-column "
      "minimum/maximum table at art. 2.2.4.2.5.7 applies ONLY to the voluntary affiliation of independent "
      "workers under Decreto 1563 de 2016, never to employees.",
      "PILA T2R2-061, T2R2-062, T2R2-063, T2R2-077, T2R2-078"),

    C("CO-ER-CCF", "Family compensation fund levy 4%",
      "Aporte a Caja de Compensacion Familiar - CCF (4%)", P_ERC,
      "PAYROLL-LEVY BASE x 4.00% (Ley 21 de 1982 art. 17 nomina mensual de salarios, INCLUDING paid rest "
      "days), NO CEILING AT ALL; rounded UP to the next multiple of 100",
      "Ley 21 de 1982 arts. 9 and 12. NEVER EXONERATED - the ET art. 114-1 relief reaches employer health, "
      "SENA and ICBF only, so the CCF 4% is payable on every employee at every salary level. TWO DIFFERENCES "
      "FROM THE IBC THAT THE ENGINE MUST MODEL SEPARATELY: the levy base has NO 25-SMMLV ceiling, and it "
      "EXPRESSLY INCLUDES statutory and contractual PAID REST DAYS. The fund is organised by department so "
      "the receiving institution code differs, but the 4% rate does not. The subsidio familiar the fund then "
      "pays to the employee is a fund benefit, not an employer payment, and is out of scope. Ley 1429 de 2010 "
      "provides a graduated scale for qualifying micro and small enterprises with a special regime for "
      "AMAZONAS, GUAINIA AND VAUPES, visible in the Resolucion 2388 rate tables as contributor classes C and "
      "D - not applicable to standard corporate payroll.",
      "PILA T2R2-045 (IBC CCF), T2R2-064, T2R2-065; T2R2-035 (CCF code); T2R2-039 (CCF days)"),

    C("CO-ER-SENA", "Apprenticeship training levy 2%", "Aporte al SENA (2%)", P_ERC,
      "PAYROLL-LEVY BASE x 2.00%, NO CEILING; ZERO where the ET art. 114-1 exoneration applies; rounded UP "
      "to the next multiple of 100",
      "Ley 21 de 1982 art. 9. EXONERATED where the employee earns strictly less than 10 SMMLV "
      "(" + EXON_CUT + ") and the employer is an income-tax-filing legal person (ET art. 114-1), tested per "
      "employee per month. Computed on the Ley 21/1982 art. 17 base - the same base as the CCF and the ICBF, "
      "which includes paid rest days and has NO ceiling - and NOT on the IBC. The PILA carries a separate "
      "'IBC otros parafiscales diferentes a CCF' field (T2R2-095) precisely because the two levy bases can "
      "diverge where one levy is exonerated and the CCF is not.",
      "PILA T2R2-095, T2R2-066, T2R2-067"),

    C("CO-ER-ICBF", "Family welfare levy 3%", "Aporte al ICBF (3%)", P_ERC,
      "PAYROLL-LEVY BASE x 3.00%, NO CEILING; ZERO where the ET art. 114-1 exoneration applies; rounded UP "
      "to the next multiple of 100",
      "Ley 89 de 1988 art. 1, which raised the levy from 2% to 3%. EXONERATED on the same ET art. 114-1 terms "
      "as employer health and SENA. Same Ley 21/1982 art. 17 base as the CCF and SENA - paid rest days "
      "included, no ceiling. Together the three levies are 9% of the levy base, of which 5% is exonerable "
      "and the CCF's 4% never is. During unpaid leave (SLN) the payroll levies fall to 0%.",
      "PILA T2R2-095, T2R2-068, T2R2-069"),

    C("CO-ER-PENSION-ALTO-RIESGO", "Additional employer pension contribution - high-risk activity",
      "Aporte Patronal Adicional de Pension de Alto Riesgo", P_ERC,
      "IBC x an additional employer-borne rate above the standard 12%: the Resolucion 2388 de 2016 rate table "
      "shows a TOTAL pension rate of 26% for a high-risk contributor against the standard 16%, implying "
      "+10 percentage points employer-borne",
      "Decreto-Ley 2090 de 2003 establishes the high-risk activities that carry an additional employer "
      "pension contribution and a reduced retirement age, and the nomina electronica carries a REQUIRED "
      "AltoRiesgoPension flag (NIE043) with the PILA carrying a special-pension-rate indicator (T2R2-079). "
      "OPEN ITEM: the 2026 confirmation of the additional rate and its precise base was not obtained from a "
      "primary regulatory source this pass - the 26% total is read from the Resolucion 2388 rate table, not "
      "from the implementing decree. CONFIGURE ONLY AGAINST THE CURRENT IMPLEMENTING DECREE and confirm with "
      "the Regulation Analyst before go-live; carried in the QA report.",
      "PILA T2R2-079; Trabajador / AltoRiesgoPension (NIE043)"),

    C("CO-PROV-PRIMA", "Service bonus accrual (employer)", "Provision de Prima de Servicios (8,3333%)", P_ERC,
      "8.3333% (30 / 360) of (monthly salary + auxilio de transporte)",
      "Statutory-benefit accrual, computed IN PARALLEL with the employee gross-to-net and never touching net "
      "pay. THE TRANSPORT ALLOWANCE IS IN THIS BASE even though it is out of the IBC and out of the "
      "payroll-levy base. Paid in two instalments - half by 30 June and half by 20 December. Absorbed by an "
      "all-inclusive salary. Together with cesantias 8.3333%, interest 1.0000% and vacation 4.1667% the "
      "total statutory benefit accrual is 21.8333% of pay.",
      "Not a PILA or nomina electronica field - an accounting provision"),

    C("CO-PROV-CESANTIAS", "Severance-savings accrual (employer)", "Provision de Cesantias (8,3333%)", P_ERC,
      "8.3333% (30 / 360) of (monthly salary + auxilio de transporte)",
      "Statutory-benefit accrual. The transport allowance is IN this base. Liquidated at 31 December and "
      "deposited to the employee's chosen fund BY 14 FEBRUARY; late deposit costs one day's salary per day of "
      "delay (Ley 50 de 1990 art. 99 num. 3). Ley 2466 de 2025 art. 64 permits an 8.33% MONTHLY ADVANCE "
      "DEPOSIT to the fund by written agreement, which is expressly NOT a partial payment of the cesantias. "
      "Absorbed by an all-inclusive salary.",
      "Consignacion Cesantias planilla T14; MA02 / MA03 for the monthly advance"),

    C("CO-PROV-INTERESES-CESANTIAS", "Severance-interest accrual (employer)",
      "Provision de Intereses a las Cesantias (1,0000%)", P_ERC,
      "1.0000% per month (12% per year) of the cesantias base",
      "Statutory-benefit accrual for the 12% annual interest of Ley 52 de 1975 art. 1. PAID TO THE EMPLOYEE "
      "DURING JANUARY - not to the fund, unlike the principal. Optionally monthly at 1% by written agreement "
      "(Ley 2466 de 2025 art. 64). Absorbed by an all-inclusive salary.",
      "Interes de cesantias IN01 / IN02 / IN03 (not a file field)"),

    C("CO-PROV-VACACIONES", "Vacation accrual (employer)", "Provision de Vacaciones (4,1667%)", P_ERC,
      "4.1667% (15 working days / 360) of salary EXCLUDING the auxilio de transporte, overtime and rest-day "
      "work; accrual = salary x days / 720",
      "Statutory accrual for the 15 working days of annual leave. THE TRANSPORT ALLOWANCE IS EXCLUDED from "
      "this base, unlike the prima and cesantias bases - the single most common accrual error in Colombian "
      "payroll. NOT ABSORBED BY AN ALL-INCLUSIVE SALARY (CST art. 132 num. 2 expressly excepts vacation), and "
      "owed on the FULL 100% of an all-inclusive salary while contributions run on 70%. Accrual suspended "
      "during unpaid leave.",
      "Not a PILA or nomina electronica field - an accounting provision"),
]
