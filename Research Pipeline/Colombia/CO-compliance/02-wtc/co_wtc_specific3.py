# -*- coding: utf-8 -*-
"""
Colombia (CO) Wage Type Catalogue — bases, intermediaries, rates and flags
(part 3c). These rows make Colombia's THREE-BASE structure explicit in the
catalogue, which is the country's defining payroll feature.
"""

from co_wtc_config import (
    SMMLV, IBC_CAP, EXON_CUT, INTEGRAL, EX25_CAP, CAP1340, DIVISOR,
    P_BASE, P_INT, P_FLAG, P_RATE, P_NOTIONAL,
)
from co_wtc_specific import C

BAND0 = "4,975,530"   # 95 UVT — top of the 0% withholding band

CO_STRUCTURAL = [
    C("CO-BASE-IBC", "Social-security contribution base", "Ingreso Base de Cotizacion (IBC)", P_BASE,
      "SUM salary-constituting payments (transport / connectivity allowance, prima, cesantias and interest "
      "EXCLUDED; vacation INCLUDED) -> apply the 40% clamp -> all-inclusive salary = 70% -> FLOOR 1 SMMLV "
      "(" + SMMLV + ") pro-rated to contributory days -> CEILING 25 SMMLV (" + IBC_CAP + ") -> round UP to "
      "the whole peso",
      "BASE 1 OF THREE, AND THE ORDER OF THE FOUR ADJUSTMENTS MATTERS: applying the ceiling before the 40% "
      "clamp gives a different and wrong answer. Ley 100 de 1993 art. 18 as substituted by Ley 797 de 2003 "
      "art. 5. The SAME base serves health (art. 204 par. 1), pension, the solidarity fund and occupational "
      "risk (Decreto 1072 de 2015 art. 2.2.4.3.3). ACTUAL salary, not notional - Colombia has no banded, "
      "class or scheduled contribution wage, so a variable-pay employee has a different IBC every month and "
      "can legitimately cross the 4-SMMLV solidarity trigger, the 10-SMMLV exoneration line and the 25-SMMLV "
      "ceiling in different directions in successive months. Where actual pay falls below the floor the base "
      "is RAISED to one SMMLV pro-rated to contributory days, so the employee still contributes 4% + 4% of "
      "the raised base even though the salary was lower. Note the asymmetry the engine must implement: the "
      "SMMLV floor protects NET PAY against voluntary deductions, while the IBC is SEPARATELY floored at one "
      "SMMLV - two different floors doing two different jobs.",
      "PILA T2R2-042 (IBC pension), T2R2-043 (IBC salud), T2R2-044 (IBC riesgos laborales)"),

    C("CO-BASE-PARAFISCAL", "Payroll-levy base",
      "Base de Aportes Parafiscales (Nomina Mensual de Salarios)", P_BASE,
      "SUM all salary elements PLUS statutory and contractual PAID REST DAYS; all-inclusive salary = 70%; "
      "NO FLOOR AND NO CEILING; round UP to the whole peso",
      "BASE 2 OF THREE - AND IT IS NOT THE IBC. Ley 21 de 1982 art. 17, verified verbatim against the "
      "gazette: the nomina mensual de salarios means 'la totalidad de los pagos hechos por concepto de los "
      "diferentes elementos integrantes del salario en los terminos de la ley laboral, cualquiera que sea su "
      "denominacion y ademas, los verificados por descansos remunerados de ley y convencionales o "
      "contractuales. Los pagos hechos en moneda extranjera deberan incluirse en la respectiva nomina, "
      "liquidados al tipo de cambio oficial y vigente el ultimo dia del mes al cual corresponde el pago.' TWO "
      "DIFFERENCES FROM THE IBC: it has NO CEILING at all - nothing is capped at 25 SMMLV - and paid rest "
      "days are included BY NAME. The Ley 1393/2010 art. 30 40% clamp does NOT reach this base, because "
      "art. 30 bites only 'para los efectos relacionados con los articulos 18 y 204 de la Ley 100 de 1993'. "
      "Serves the CCF 4%, SENA 2% and ICBF 3%; falls to zero for the days of an SLN unpaid-leave event.",
      "PILA T2R2-045 (IBC CCF), T2R2-095 (IBC otros parafiscales), T2R1-020 (valor total de la nomina)"),

    C("CO-BASE-RETENCION", "Withholding tax base", "Base Gravable de Retencion (ET art. 388)", P_BASE,
      "(A) taxable payments - (B) non-taxable income - (D) art. 387 deductions - (E) exempt income, where "
      "(D+E) <= 40% of (C = A - B) AND <= 1,340 UVT/year, with the 25% exemption computed LAST and capped at "
      "790 UVT/year, LESS the 72-UVT-per-dependant deduction which sits OUTSIDE the caps",
      "BASE 3 OF THREE - neither gross pay nor the IBC. ET art. 388 added by Ley 1819 de 2016 art. 18, with "
      "the absolute annual cap added by Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 as modified by Decreto "
      "2231 de 2023 art. 9. Cesantias and their interest NEVER enter it. OPEN ITEM: the 790-UVT and "
      "1,340-UVT caps are stated ANNUALLY yet withholding is monthly; market practice, which Mercans "
      "follows, apportions them at one twelfth - 65.8333 UVT = " + EX25_CAP + " and 111.6667 UVT = "
      + CAP1340 + " - and tests each month against the apportioned figure. No regulation prescribes the "
      "apportionment expressly; carried in the QA report. The CURRENT year's UVT applies to the annual caps "
      "(DIAN Concepto 015007 int. 973 de 13 septiembre 2023). NOT DEDUCTIBLE AGAINST WITHHOLDING: the 1% / "
      "240-UVT invoice-based deduction of ET art. 336 num. 5, expressly excluded and confirmed by the same "
      "Concepto - it is available only in the employee's own annual return. ALSO OUTSIDE THE CAPS BUT OUTSIDE "
      "MERCANS SCOPE: ET art. 206 par. 4 places nums. 6 to 9, the prima especial and the prima de costo de "
      "vida outside the 40% and 1,340-UVT limits; these attach to military, judicial, diplomatic and public "
      "university staff, but the engine must carry the flag so it does not silently clamp them if such an "
      "employee is loaded.",
      "Formulario 350 casilla 77; Deducciones / RetencionFuente (NIE177)"),

    C("CO-BASE-PRESTACIONAL", "Statutory-benefit base",
      "Base Prestacional (Prima, Cesantias e Intereses)", P_BASE,
      "monthly salary PLUS the auxilio de transporte or auxilio de conectividad; variable pay at the semester "
      "or annual average as the particular benefit requires",
      "The base of the prima de servicios, the cesantias and the 12% interest. ITS DEFINING ODDITY: it "
      "INCLUDES the auxilio de transporte, which is excluded from BOTH the IBC and the payroll-levy base, and "
      "it EXCLUDES the prima, cesantias and interest themselves. A valid written CST art. 128 non-salary pact "
      "removes a payment from this base PERMANENTLY - unlike the IBC, where the 40% clamp can force the "
      "excess back in. Overtime and rest-day work ARE in this base, unlike the vacation base.",
      "Derived - feeds Devengados / Primas (NIE117-NIE119) and Cesantias (NIE120-NIE122)"),

    C("CO-BASE-VACACIONES", "Vacation base", "Base de Vacaciones (CST art. 192)", P_BASE,
      "ordinary salary being earned on the day leave begins, EXCLUDING ONLY the value of work on obligatory "
      "rest days and the value of supplementary overtime hours; variable salary -> average of the immediately "
      "preceding year",
      "CST art. 192, verified verbatim: 'Durante el periodo de vacaciones el trabajador recibira el salario "
      "ordinario que este devengando el dia en que comience a disfrutar de ellas. En consecuencia, SOLO se "
      "excluiran para la liquidacion de vacaciones el valor del trabajo en dias de descanso obligatorio y el "
      "valor del trabajo suplementario en horas extras.' The word 'solo' is doing the work: THE NIGHT PREMIUM "
      "AND COMMISSIONS STAY IN, and only those two things come out. The auxilio de transporte is not in this "
      "base either. An all-inclusive salary does NOT absorb vacation, so the base is the FULL 100% of it "
      "while contributions run on 70%.",
      "Derived - feeds Devengados / VacacionesComunes (NIE112) and VacacionesCompensadas (NIE116)"),

    C("CO-INT-CLAMP40", "Non-salary excess forced back into the contribution base",
      "Excedente No Salarial Reintegrado al IBC (Ley 1393 de 2010 art. 30)", P_INT,
      "IF total non-salary payments > 40% x total remuneration THEN excess = non-salary total - (0.40 x total "
      "remuneration), added to the IBC; ELSE 0. Computed BEFORE the 70% all-inclusive reduction, the floor "
      "and the ceiling",
      "THE INTERMEDIARY THAT MAKES TWO BASES DIVERGE PERMANENTLY. Ley 1393 de 2010 art. 30, verified verbatim "
      "against the gazette: 'Sin perjuicio de lo previsto para otros fines, para los efectos relacionados con "
      "los articulos 18 y 204 de la Ley 100 de 1993, los pagos laborales no constitutivos de salario de los "
      "trabajadores particulares no podran ser superiores al 40% del total de la remuneracion.' WORKED "
      "ILLUSTRATION (CCG Module 6.3): salary 8,000,000 plus a 20,000,000 retention bonus under a valid "
      "non-salary pact gives total remuneration 28,000,000, of which non-salary is 71.4%; permitted "
      "non-salary is 40% x 28,000,000 = 11,200,000, so 8,800,000 is FORCED BACK IN and the IBC becomes "
      "8,000,000 + 8,800,000 = 16,800,000 - while the whole 20,000,000 remains non-salary for the prima, "
      "cesantias, interest and vacation, and fully taxable for withholding. The clamp reaches Ley 100 "
      "arts. 18 and 204 only, so it does not touch the CCF / SENA / ICBF levy base. See also Resolucion "
      "MinProteccion 2641 de 2011. UGPP audit exposure sits squarely on this line: it cross-matches "
      "tax-authority data against filed contribution returns.",
      "Derived - feeds PILA T2R2-042, T2R2-043, T2R2-044"),

    C("CO-RATE-HORA-ORDINARIA", "Ordinary hour value", "Valor de la Hora Ordinaria", P_RATE,
      "monthly salary / D, where D = 220 to 14 July 2026 and 210 from 15 July 2026 (MinTrabajo Circular "
      "Externa 101 de 22 septiembre 2025). Minimum hourly value: 7,958.66 then 8,337.64",
      "THE SINGLE BIGGEST 2026 CALCULATION CHANGE. Circular 101 publishes the gradual path: 47h/235 from "
      "15 July 2023, 46h/230 from 15 July 2024, 44h/220 from 15 July 2025 and 42h/210 FROM 15 JULY 2026 "
      "(Ley 2101 de 2021 art. 3; CST art. 161 as substituted by Ley 2466 de 2025 art. 11, verified verbatim: "
      "'una jornada maxima de cuarenta y dos (42) horas a la semana', distributable by agreement over five or "
      "six days, always preserving the rest day and WITHOUT REDUCING SALARY). THE LEGACY DIVISOR OF 240 IS "
      "OBSOLETE AND UNDERSTATES EVERY PREMIUM BY ABOUT 14.3%. A JULY 2026 PAYROLL SPANS BOTH DIVISORS and "
      "must be split at 15 July - and separately at 1 July for the rest-day premium step from 80% to 90%. Two "
      "cut-overs, two weeks apart; never collapse them. Where the week is distributed over five days with "
      "Saturday and/or Sunday rest, the ordinary daily shift may be extended by up to two hours WITHOUT "
      "paying supplementary work (CST art. 164; Circular 101 SS2.1).",
      "Derived - feeds every hour-type Porcentaje / Pago element"),

    C("CO-PCT-RETENCION-PROC2", "Procedure 2 fixed withholding percentage",
      "Porcentaje Fijo de Retencion (Procedimiento 2)", P_RATE,
      "fixed % = table(sum of the preceding 12 months' taxable payments / 13) expressed as a percentage of "
      "that average; recomputed each JUNE and DECEMBER and applied to each of the FOLLOWING SIX MONTHS' "
      "depurated bases",
      "ET art. 386. THE DIVISOR IS 13, NOT 12 - art. 386 says 'dividir por 13' - because the 13 prorates the "
      "13th-month effect of the prima de servicios, which under Procedure 2 sits INSIDE the ordinary base "
      "rather than receiving the separate art. 385 table read; using 12 over-withholds by roughly 8%. A "
      "BACKWARD-LOOKING ACCUMULATOR, NOT A PROJECTION: Colombia is not an annualised or cumulative "
      "withholding system, so there is no annual estimate, no notional annual salary, no projected bonus and "
      "no year-end catch-up. CESANTIAS AND THEIR INTEREST ARE EXPRESSLY EXCLUDED from the accumulator; "
      "everything else is included - salary, overtime, the night and rest-day premia, commissions, habitual "
      "bonuses, the prima de servicios, salary in kind, the transport allowance, vacation pay and "
      "cash-compensated vacation. Art. 387 par. 1 requires the art. 387 deductions to be used BOTH in "
      "computing the fixed percentage AND in computing the monthly base it is applied to. A new hire has no "
      "12-month history so no fixed percentage exists: read the table on the month's own taxable payments "
      "until the first semi-annual calculation, whose divisor is then the ACTUAL months of service, not 13. A "
      "large mid-year increase produces under-withholding for the rest of the semester and THE EMPLOYER MAY "
      "NOT UNILATERALLY RAISE THE FIXED PERCENTAGE MID-SEMESTER - the employee's only remedy is a written "
      "request for a higher rate under art. 383 par. 3.",
      "Derived - feeds Deducciones / RetencionFuente (NIE177)"),

    C("CO-REDONDEO", "Rounding residual (electronic payroll)", "Redondeo", P_NOTIONAL,
      "residual difference such that total accrued - total deducted +/- redondeo = total payable, within a "
      "tolerance of +/-2.00, using ROUND-HALF-TO-EVEN",
      "THREE ROUNDING REGIMES COEXIST IN ONE COLOMBIAN PAYROLL MONTH AND MUST NEVER BE UNIFIED: the PILA "
      "rounds UP - the IBC to the whole peso and each contribution to the next multiple of 100 (Decreto 1990 "
      "de 2016 art. 1, substituting Decreto 780 de 2016 art. 3.2.1.5); the nomina electronica uses "
      "ROUND-HALF-TO-EVEN with a +/-2.00 tolerance and carries this EXPLICIT Redondeo element for the "
      "residual; and the DIAN return forms round to the NEAREST 1,000 (ET art. 577). Net pay itself is not "
      "separately rounded to any statutory rule - it is the arithmetic residue after each deduction has "
      "already been rounded under its own regime.",
      "NominaIndividual / Redondeo (NIE186), DevengadosTotal (NIE187), DeduccionesTotal (NIE188), "
      "ComprobanteTotal (NIE189)"),

    C("CO-FLAG-SALARIO-INTEGRAL", "All-inclusive salary flag", "Indicador de Salario Integral", P_FLAG,
      "TRUE where a WRITTEN all-inclusive salary agreement exists and the salary is >= 13 SMMLV "
      "(" + INTEGRAL + "); drives IBC = 70% and payroll-levy base = 70%, but vacation at 100%",
      "A REQUIRED field of the nomina electronica (NIE056) and of the PILA (T2R2-041). Requires an ORDINARY "
      "salary above 10 SMMLV plus a benefit factor of at least 30%, agreed IN WRITING (CST art. 132 num. 2). "
      "Drives the 70% reduction of BOTH the IBC (Ley 100 art. 18 final paragraph) and the payroll-levy base "
      "(CST art. 132 num. 3: 'los aportes se disminuiran en un treinta por ciento (30%)') - but NEVER of "
      "vacation, which stays at 100% because art. 132 num. 2 expressly excepts it.",
      "Trabajador / SalarioIntegral (NIE056); Sueldo (NIE062); PILA T2R2-041"),

    C("CO-FLAG-EXONERACION-114-1", "ET art. 114-1 exoneration flag",
      "Indicador de Exoneracion de Aportes (ET art. 114-1)", P_FLAG,
      "TRUE where the employer is an income-tax-filing legal person (or a natural person employing 2 or more "
      "workers) AND the employee's month earnings are STRICTLY LESS THAN 10 SMMLV (" + EXON_CUT + "); "
      "suppresses employer health 8.5%, SENA 2% and ICBF 3%",
      "TESTED PER EMPLOYEE, PER MONTH, on what the employee devenga - not on the contractual salary, and not "
      "on a segment of the month, so a mid-month increase that takes the MONTH TOTAL across the line loses "
      "the exoneration for the WHOLE month. AT EXACTLY 10 SMMLV THE EXONERATION IS LOST - the statute says "
      "'menos de diez (10) salarios minimos', so the test is strictly less than - costing approximately COP "
      "2,363,800 per month and taking the employer cost factor from about 1.3836 to about 1.52. PENSION 12%, "
      "OCCUPATIONAL RISK AND THE CCF 4% ARE NEVER EXONERATED. Carried on the PILA at both employer level "
      "(A1-033) and contributor level (T2R2-076), and on Formulario 350 casilla 27 for the related "
      "self-withholding configuration.",
      "PILA A1-033, T2R2-076; Formulario 350 casilla 27"),

    C("CO-FLAG-RESIDENCIA-FISCAL", "Tax residence flag with effective date",
      "Indicador de Residencia Fiscal con Fecha de Efecto", P_FLAG,
      "TRUE where the employee is a Colombian tax resident AT THE DATE OF THIS PAYMENT (ET art. 10: more "
      "than 183 calendar days, continuous or not, in any 365-day period, or the diplomatic or "
      "nationality-plus-connection tests); drives the art. 383 table versus the art. 408 flat 20%",
      "THE MOST CONSEQUENTIAL FLAG IN COLOMBIAN PAYROLL - a 17-fold withholding difference on the same "
      "salary. Must be RE-EVALUATED EVERY PAYROLL PERIOD and switched PROSPECTIVELY from the payment "
      "FOLLOWING the date the test is met; never applied retroactively through payroll (DIAN Concepto 011108 "
      "de 29 junio 2026). Where the 183-day period straddles two years, residence attaches to the year in "
      "which the 183rd day falls. A SECOND CONDITION SITS BESIDE IT: where the service is performed entirely "
      "outside Colombia by a non-resident the income is foreign-source and there is no withholding at all "
      "(DIAN Oficio 28380 de 2019), so the engine also needs a place-of-service flag - the nomina "
      "electronica carries LugarTrabajoPais (NIE050) for exactly this.",
      "Trabajador / LugarTrabajoPais (NIE050); Formulario 350 hoja 2 casillas 141, 144"),

    C("CO-FLAG-ALTO-RIESGO-PENSION", "High-risk pension activity flag",
      "Indicador de Actividad de Alto Riesgo Pensional", P_FLAG,
      "TRUE where the employee performs an activity listed in Decreto-Ley 2090 de 2003; drives the additional "
      "employer pension contribution and a reduced retirement age",
      "A REQUIRED field of the nomina electronica (NIE043) with a matching PILA special-pension-rate "
      "indicator (T2R2-079). The FLAG itself is mandatory and must be populated for EVERY employee, "
      "high-risk or not, or the XML fails validation. OPEN ITEM as to the 2026 additional RATE - see "
      "CO-ER-PENSION-ALTO-RIESGO and the QA report.",
      "Trabajador / AltoRiesgoPension (NIE043); PILA T2R2-079"),

    C("CO-FLAG-PACTO-NO-SALARIAL", "Written non-salary pact flag",
      "Indicador de Pacto de Exclusion Salarial (CST art. 128)", P_FLAG,
      "TRUE where an EXPRESS, WRITTEN, SIGNED CST art. 128 pact exists over a genuine benefit or allowance; "
      "drives the salary / non-salary element split and the 40% clamp computation",
      "THREE TESTS FOR A VALID PACT: it must be (a) EXPRESS, (b) WRITTEN, and (c) attached to a BENEFIT OR "
      "ALLOWANCE, not to consideration for the service itself. A 'non-salary' label on what is plainly "
      "remuneration for work will not survive a UGPP contribution audit. THE FLAG IS A HARD CONFIGURATION "
      "VALUE, NOT A RUNTIME DERIVATION: the nomina electronica separates salary from non-salary AT ELEMENT "
      "LEVEL with paired S / NS element names - bonus, allowance, generic concept, generic payment, voucher "
      "payment, meal payment and travel/accommodation allowance - so the engine must carry the flag on every "
      "wage type and must not attempt to derive it at reporting time. NOTE THE TWO ASYMMETRIES: the pact "
      "removes the payment from the labour-law bases PERMANENTLY but from the IBC only up to 40%, and IT HAS "
      "NO TAX EFFECT AT ALL. Colombian benefit structuring is a social-security optimisation, never a tax "
      "optimisation; any engine that treats a non-salary flag as a tax exclusion will systematically "
      "under-withhold. THERE IS NO SALARY-SACRIFICE REGIME IN COLOMBIAN LAW - CST art. 13 makes the minimum "
      "labour rights irrenounceable.",
      "Drives every paired S / NS element (NIE139/140, NIE141/142, NIE147/148, NIE151/152, NIE153/154, "
      "NIE072/073)"),

    C("CO-FLAG-PENSIONADO-ACTIVO", "Employed old-age pensioner flag", "Indicador de Pensionado en Activo", P_FLAG,
      "TRUE where the employee is an old-age pensioner in active service; suppresses BOTH the 4% employee and "
      "the 12% employer pension contribution",
      "PENSION CONTRIBUTION CEASES ENTIRELY for an employed old-age pensioner - neither share is due - while "
      "health, occupational risk and the payroll levies continue. Reported with PILA worker sub-type 01. "
      "REACHING RETIREMENT AGE DOES NOT BY ITSELF STOP THE CONTRIBUTION: being a PENSIONER IN ACTIVE SERVICE "
      "does. Retirement age (57 for women, 62 for men in the public defined-benefit regime) affects "
      "entitlement and the point at which the contribution ceases, never the rate - there is NO "
      "gender-differentiated rate, base, floor, ceiling or trigger anywhere in the eight Colombian "
      "contributions, and CST art. 143 as amended by Ley 1496 de 2011 expressly forbids salary differences by "
      "gender.",
      "Trabajador / SubTipoTrabajador (NIE042); PILA T2R2-005, T2R2-006"),

    C("CO-FLAG-PROCEDIMIENTO-RETENCION", "Withholding procedure election flag",
      "Indicador de Procedimiento de Retencion (1 o 2)", P_FLAG,
      "1 = ET art. 385 monthly table read, with the statutory minimum prima withheld SEPARATELY; 2 = ET "
      "art. 386 fixed percentage set each June and December, binding for the following six months",
      "ELECTED BY THE EMPLOYER, PER EMPLOYEE. Once Procedure 2 is elected it applies for the whole six-month "
      "period following the June or December calculation, and market practice is to change procedure only at "
      "a semester boundary. THE ELECTION MATERIALLY CHANGES JUNE AND DECEMBER NET PAY: under Procedure 1 the "
      "statutory minimum prima gets its own table read and is frequently withheld at 0%, while under "
      "Procedure 2 it is folded into a single larger base, usually producing higher withholding in that month "
      "offset by lower withholding in others. Worked comparison in CCG Module 4.5: on a COP 8,000,000 salary "
      "with a COP 4,000,000 first-half prima, Procedure 1 yields COP 92,049.30 for June (the prima read alone "
      "falling in the 0% band) against a materially higher single-base result under Procedure 2.",
      "Not reported - a configuration flag driving Deducciones / RetencionFuente (NIE177)"),

    C("CO-FLAG-DEPENDIENTES", "Dependants declaration flag and count",
      "Indicador y Numero de Dependientes Economicos", P_FLAG,
      "Count of qualifying dependants with each dependant's identity document; drives BOTH the ET art. 387 "
      "deduction of 10% of gross capped at 32 UVT/month (COP 1,675,968) AND the art. 336 num. 3 deduction of "
      "72 UVT per dependant per year (COP 3,770,928 each, maximum 4 dependants = 6 UVT = COP 314,244 per "
      "dependant per month)",
      "TWO DEDUCTIONS, AND AN EMPLOYEE MAY TAKE BOTH FOR THE SAME DEPENDANT. Decreto 2231 de 2023 art. 3: "
      "'el mismo dependiente solo dara lugar a una de estas dos deducciones, EXCEPTO cuando el contribuyente "
      "tenga ingresos por rentas de trabajo provenientes de una relacion laboral o legal y reglamentaria, en "
      "cuyo caso podran aplicarse ambas deducciones por el mismo dependiente.' The art. 387 deduction is 10% "
      "OF GROSS REGARDLESS OF THE NUMBER OF DEPENDANTS - it does not multiply; the art. 336 deduction is per "
      "dependant AND SITS OUTSIDE THE 40% AND 1,340-UVT CAPS ('en adicion al limite establecido en el inciso "
      "anterior'). WHO QUALIFIES (ET art. 387 par. 2, nums. 2 and 3 as amended by Ley 2411 de 2024 art. 2): "
      "children up to 18; children 18-25 whose higher or technical education the taxpayer finances; children "
      "over 18 in a certified state of physical or psychological dependence; a spouse or permanent partner "
      "dependent by absence of income or with annual income below 260 UVT (COP 13,617,240) certified by a "
      "public accountant, or by certified dependence; and parents and siblings on the same conditions. THE "
      "DEPENDANT'S IDENTITY DOCUMENT IS REQUIRED, not merely a count - the information return demands the "
      "document (numeral N34) and the deduction is not sustainable on audit without it.",
      "Formulario 220 casillas 79-82; Formato 2276 numeral N34"),
]
