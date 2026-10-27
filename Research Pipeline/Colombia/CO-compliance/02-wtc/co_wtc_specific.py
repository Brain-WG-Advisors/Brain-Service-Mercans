# -*- coding: utf-8 -*-
"""
Colombia (CO) Wage Type Catalogue — Colombia-specific wage types (part 3)
=========================================================================
Locally-named wage types beyond the global baseline. Every
wage_type_categories.in_scope item of scope_manifest.json is represented
here or among the 300 configured global codes.
"""

from co_wtc_config import (
    SMMLV, UVT, AUX_TTE, IBC_CAP, FSP_TRIG, EXON_CUT, INTEGRAL, AUX_CAP,
    SUB_TRIG, MEAL_CAP, MEAL_SAL, EX25_CAP, CAP1340, CESA_EXEMPT, DIVISOR,
    P_SAL, P_SAL_ADD, P_SALINT, P_OT, P_NIGHT, P_COMM, P_TRANSP, P_NONSAL,
    P_NONSAL_A, P_GRATUITY, P_BIK_SAL, P_PRIMA, P_CESANT, P_VAC, P_LEAVE_P,
    P_NOTINC, P_MEAL3P, P_INCAP_ER, P_INCAP_EPS, P_INDEM, P_APRENDIZ,
    P_VIATICO, P_VOLPEN, P_RAISVOL, P_EQUITY, P_PENSION, P_UNPAID, P_ANTICIPO,
    P_DED, P_DED_ADD, P_TAX, P_ERC, P_BASE, P_INT, P_FLAG, P_RATE, P_NOTIONAL,
)


def C(code, en, es, p, formula, expl, xml):
    return dict(code=code, en=en, es=es, p=p, formula=formula, expl=expl, xml=xml)


# ===========================================================================
# EARNINGS — core pay, premia, statutory benefits, leave, terminations
# ===========================================================================
CO_EARNINGS = [
    C("CO-SALARIO-BASICO", "Basic salary", "Salario Basico", P_SAL,
      "full month = S; partial month = S x days worked / 30; minimum " + SMMLV + "/month "
      "(Decreto 1469 de 2025 art. 1)",
      "Salario basico, fixed or variable (CST arts. 127 and 132 num. 1). Enters ALL THREE BASES: the IBC "
      "(floor 1 SMMLV pro-rated to contributory days, ceiling 25 SMMLV = " + IBC_CAP + ", rounded UP to the "
      "whole peso), the Ley 21/1982 payroll-levy base (NO ceiling), and the ET art. 388 withholding base. "
      "Prorated on a 30-day COMMERCIAL month irrespective of calendar days - February and a 31-day month are "
      "both 30 payroll days, and a hire on the 31st counts as day 30. The 2026 amount was fixed by Decreto "
      "1469 de 29 diciembre 2025, provisionally suspended by the Council of State on 12 February 2026, "
      "re-fixed identically by Decreto 0159 de 2026, and restored when the suspension was revoked on 9 July "
      "2026; the AMOUNT has been continuously in force since 1 January 2026 and has never been in dispute.",
      "Devengados / Basico - DiasTrabajados (NIE069), SueldoTrabajado (NIE070)"),

    C("CO-SALARIO-INTEGRAL", "All-inclusive salary", "Salario Integral", P_SALINT,
      "S >= 13 SMMLV = " + INTEGRAL + " (10 SMMLV ordinary + a benefit factor of at least 30%); IBC and "
      "payroll-levy base BOTH = 70% x S; vacation on the FULL 100%",
      "Salario integral (CST art. 132 nums. 2-3, written agreement required). It compensates in advance the "
      "statutory benefits, premia and allowances - night work, overtime, rest-day and holiday work, statutory "
      "and extra-statutory bonuses, cesantias and their interest, subsidies and in-kind supplies - EXCEPT "
      "VACATION. Contributions are calculated on 70% (Ley 797 de 2003 art. 5 substituting Ley 100 art. 18: "
      "'Las cotizaciones de los trabajadores cuya remuneracion se pacte bajo la modalidad de salario integral, "
      "se calculara sobre el 70% de dicho salario'), and the payroll levies are likewise reduced by 30% (CST "
      "art. 132 num. 3), with occupational risk following the same base (Decreto 1072 de 2015 art. 2.2.4.3.3). "
      "THE TRAP: vacation is still owed IN FULL, 15 working days on the WHOLE all-inclusive salary, while "
      "contributions run on 70%. At the 13-SMMLV floor the IBC is 15,933,235.50 rounded up. The former tax "
      "exemption of the benefit factor was replaced by the 25% exempt-income deduction (ET art. 206 par. 2).",
      "Trabajador / SalarioIntegral flag (NIE056); Sueldo (NIE062); PILA T2R2-041"),

    C("CO-AUX-TRANSPORTE", "Statutory transport allowance", "Auxilio de Transporte", P_TRANSP,
      AUX_TTE + " x days worked / 30, where salary <= 2 SMMLV (" + AUX_CAP + ") and public transport is "
      "available (Decreto 1470 de 2025 art. 1)",
      "Mandatory where the employee earns up to 2 SMMLV. NOT salary (Ley 15 de 1959), so OUT of the IBC and "
      "OUT of the Ley 21/1982 payroll-levy base - but IN the statutory-benefit base, so it enters the prima "
      "de servicios, the cesantias and the 12% interest. NOT in the vacation base. Taxable income, though "
      "normally within the 0% withholding band. Not payable for days of unpaid leave, sickness incapacity or "
      "maternity / paternity leave. Uniform nationally - there is no departmental, sectoral or rural variant. "
      "The 2026 combined minimum cash entitlement of wage + allowance is exactly COP 2,000,000.",
      "Devengados / Transporte - AuxilioTransporte (NIE071)"),

    C("CO-AUX-CONECTIVIDAD", "Connectivity allowance (teleworkers)", "Auxilio de Conectividad Digital", P_TRANSP,
      AUX_TTE + " x days worked / 30, for a teleworker earning LESS THAN 2 SMMLV (" + AUX_CAP + "), "
      "IN PLACE OF the transport allowance (Ley 2466 de 2025 art. 53)",
      "Ley 2466 de 2025 art. 53 adds art. 6A to Ley 1221 de 2008: 'El empleador debera otorgar el "
      "reconocimiento de un auxilio de conectividad para teletrabajadores y teletrabajadoras que devenguen "
      "menos de dos (2) salarios minimos legales mensuales vigentes, en reemplazo del auxilio de transporte. "
      "En todo caso, los teletrabajadores y teletrabajadoras, solo tendran derecho a recibir uno de estos "
      "auxilios, independientemente de la modalidad de teletrabajo otorgado.' NEVER PAID TOGETHER WITH THE "
      "TRANSPORT ALLOWANCE - the engine must enforce mutual exclusion on the telework flag. Expressly does not "
      "constitute salary, so out of the IBC and the levy base, but in the statutory-benefit base for employees "
      "up to 2 SMMLV. Taxable income.",
      "Devengados / Transporte - AuxilioTransporte (NIE071); Teletrabajo (NIE158)"),

    C("CO-HED", "Day overtime (+25%)", "Hora Extra Diurna (25%)", P_OT,
      "(S / D) x 1.25 x H for hours 06:00-19:00 beyond the ordinary day; D = " + DIVISOR,
      "CST art. 168 num. 2. Salary, fully in the IBC and the payroll-levy base, in the prima / cesantias / "
      "interest base, and EXCLUDED FROM THE VACATION BASE (CST art. 192). Fully taxable, no preferential "
      "rate. Premia arise exclusively and are not cumulated with one another (art. 168 num. 4); only the "
      "art. 179 rest-day premium is added. Volume limit 2 hours/day and 12/week (Ley 2466 art. 13).",
      "Devengados / HED - Cantidad (NIE076), Porcentaje (NIE077), Pago (NIE078)"),

    C("CO-HEN", "Night overtime (+75%)", "Hora Extra Nocturna (75%)", P_OT,
      "(S / D) x 1.75 x H for hours 19:00-06:00 beyond the ordinary day; D = " + DIVISOR,
      "CST art. 168 num. 3. Same base treatment as day overtime: in the IBC, the levy base and the "
      "statutory-benefit base, OUT of the vacation base, fully taxable. The 19:00 boundary applies since "
      "25 December 2025 (CST art. 160 as substituted by Ley 2466 de 2025 art. 10, par. 2 deferring entry "
      "into force by six months from the 25 June 2025 sanction).",
      "Devengados / HEN - Cantidad (NIE081), Porcentaje (NIE082), Pago (NIE083)"),

    C("CO-RECARGO-NOCTURNO", "Night premium (35%)", "Recargo Nocturno (35%)", P_NIGHT,
      "(S / D) x 0.35 x H for ORDINARY hours falling in the 19:00-06:00 window; D = " + DIVISOR,
      "CST art. 168 num. 1 - a premium for the fact of night work, on ordinary hours, distinct from overtime. "
      "UNLIKE OVERTIME IT STAYS IN THE VACATION BASE: CST art. 192 excludes only rest-day work and "
      "supplementary overtime hours, so the night premium and commissions remain. Salary, fully contributory, "
      "fully taxable. Does NOT apply on the 6-hour / 36-hour-week successive shift system (CST arts. 161(d) "
      "and 168 num. 1). Two extra hours a day attract it since the window moved from 21:00 to 19:00 on "
      "25 December 2025.",
      "Devengados / HRN - Cantidad (NIE086), Porcentaje (NIE087), Pago (NIE088)"),

    C("CO-RECARGO-DOMINICAL", "Obligatory rest-day / holiday premium (80% / 90%)",
      "Recargo Dominical y Festivo (80% hasta 30-jun-2026 / 90% desde 1-jul-2026)", P_OT,
      "(S / D) x 0.80 x H to 30 June 2026; x 0.90 from 1 July 2026; x 1.00 from 1 July 2027 - IN ADDITION TO "
      "the paid rest day itself and the hours actually worked",
      "CST art. 179 as substituted by Ley 2466 de 2025 art. 14, transitional paragraph verified verbatim: "
      "'...80%. A partir del primero de julio de 2026, se incrementara el recargo por laborar en dia de "
      "descanso obligatorio a 90%. A partir del primero de julio de 2027, se dara plena aplicacion al recargo "
      "... sin perjuicio de que ... el empleador se acoja al recargo del 100%.' THE THREE-VALUE STRUCTURE "
      "(MinTrabajo Circular 101 de 2025 SS4): working an obligatory rest day generates THREE independent "
      "payment obligations - (1) the paid rest day itself at one day's ordinary salary (CST art. 173), (2) the "
      "hours actually worked, (3) this additional premium. An engine that pays only the hours plus the premium "
      "UNDERPAYS BY ONE DAY. Occasional = up to 2 rest days in a calendar month; 3 or more is habitual and "
      "gives the employee the choice of a compensatory rest day or the remuneration (arts. 179 par. 1, 180). "
      "OUT of the vacation base. TWO 2026 CUT-OVERS TWO WEEKS APART: this premium steps on 1 JULY, the "
      "42-hour week and the 210 divisor on 15 JULY - never collapse them. A DEFECT RECORDED FOR "
      "TRACEABILITY: Circular 101 SS5.1 states a 75% premium (the pre-reform figure) after correctly stating "
      "the 80/90/100 phase-in in SS4; the SS4 schedule governs and the 75% reference must not be configured. "
      "Likewise the electronic-payroll Technical Annex v1.0 hard-codes the pre-reform 100/75/150/110 "
      "percentages - DIAN Concepto 013840 (int. 1568) de 1 octubre 2025 resolves that the annex percentage "
      "'must be read in accordance with the rules in force for each specific case', so the engine reports the "
      "real statutory percentage.",
      "Devengados / HRDDF - Cantidad (NIE096), Porcentaje (NIE097), Pago (NIE098)"),

    C("CO-HEDDF", "Day overtime on a rest day / holiday (+105% / +115%)",
      "Hora Extra Diurna Dominical y Festiva", P_OT,
      "(S / D) x (1 + 0.25 + 0.80) x H to 30 Jun 2026 = 205%; (1 + 0.25 + 0.90) = 215% from 1 Jul 2026",
      "The art. 168 overtime premium and the art. 179 rest-day premium ARE cumulated with each other (art. 168 "
      "num. 4 bars cumulation only among the art. 168 premia themselves). Combined 2026 uplift: +105% "
      "January-June, +115% July-December. Salary, fully contributory, OUT of the vacation base, fully taxable.",
      "Devengados / HEDDF - Cantidad (NIE091), Porcentaje (NIE092), Pago (NIE093)"),

    C("CO-HENDF", "Night overtime on a rest day / holiday (+155% / +165%)",
      "Hora Extra Nocturna Dominical y Festiva", P_OT,
      "(S / D) x (1 + 0.75 + 0.80) x H to 30 Jun 2026 = 255%; (1 + 0.75 + 0.90) = 265% from 1 Jul 2026",
      "Night overtime worked on an obligatory rest day or public holiday. Combined 2026 uplift: +155% "
      "January-June, +165% July-December. Salary, fully contributory, OUT of the vacation base, fully taxable.",
      "Devengados / HENDF - Cantidad (NIE101), Porcentaje (NIE102), Pago (NIE103)"),

    C("CO-HRNDF", "Night premium on a rest day / holiday (+115% / +125%)",
      "Recargo Nocturno Dominical y Festivo", P_NIGHT,
      "(S / D) x (0.35 + 0.80) x H to 30 Jun 2026 = 115%; (0.35 + 0.90) = 125% from 1 Jul 2026",
      "The night premium on ORDINARY hours worked at night on an obligatory rest day or holiday. Being a night "
      "premium and not overtime, it STAYS IN THE VACATION BASE in respect of its 35% night component; the "
      "art. 179 rest-day component is excluded by CST art. 192. Configure the two components as separate "
      "wage types where the vacation base must be struck exactly.",
      "Devengados / HRNDF - Cantidad (NIE106), Porcentaje (NIE107), Pago (NIE108)"),

    C("CO-DESCANSO-REMUNERADO", "Paid weekly rest day and paid public holidays",
      "Descanso Dominical y Festivo Remunerado", P_LEAVE_P,
      "One day's ordinary salary per obligatory rest day and per statutory public holiday (CST arts. 172, 173, "
      "177); already inside a monthly salary, itemised for daily-rated and piece-rate workers",
      "PAID REST, AND THE ONE ITEM THE PAYROLL-LEVY BASE NAMES EXPRESSLY. Ley 21 de 1982 art. 17, verified "
      "verbatim: the monthly salary payroll is 'la totalidad de los pagos hechos por concepto de los "
      "diferentes elementos integrantes del salario en los terminos de la ley laboral, cualquiera que sea su "
      "denominacion y ademas, los verificados por descansos remunerados de ley y convencionales o "
      "contractuales.' So paid rest days are IN the CCF / SENA / ICBF base by name. Also in the IBC and the "
      "statutory-benefit and vacation bases, and fully taxable. Foreign-currency payments enter the levy "
      "payroll converted at the official rate on the LAST DAY OF THE MONTH.",
      "Devengados / Basico - SueldoTrabajado (NIE070); LicenciaR (NIE132-NIE135) where itemised"),

    C("CO-COMISIONES", "Commissions and sales percentages", "Comisiones y Porcentajes sobre Ventas", P_COMM,
      "Contractual percentage of sales or output; enters the base of the period in which it falls due; "
      "variable pay enters the vacation base at the average of the immediately preceding year",
      "SALARY BY EXPRESS STATUTORY DEFINITION - CST art. 127 names 'porcentajes sobre ventas y comisiones'. In "
      "the IBC, the payroll-levy base, the statutory-benefit base AND THE VACATION BASE (art. 192 excludes only "
      "rest-day work and supplementary overtime hours, so commissions remain). Not prorated for a part month - "
      "paid as earned. Fully taxable. A large commission month can push the employee across the 4-SMMLV "
      "solidarity-fund trigger (" + FSP_TRIG + "), across the 10-SMMLV exoneration line (" + EXON_CUT + ") or "
      "into a higher withholding band, all tested on that month's actual figures. Reported on its own "
      "nomina electronica element and on Formulario 220 casilla 41 / Formato 2276 numeral N11.",
      "Devengados / Comisiones - Comision (NIE155)"),

    C("CO-BONIF-HABITUAL", "Habitual bonus (salary)", "Bonificacion Habitual (Salarial)", P_SAL_ADD,
      "Contractual or customary amount paid habitually",
      "CST art. 127 brings 'bonificaciones habituales' INTO salary, so a habitual bonus without a written "
      "non-salary pact enters every base. The habituality test is the audit risk: a payment repeated year on "
      "year will not survive a UGPP contribution audit as an occasional gratuity. Fully taxable in the "
      "ordinary monthly base under both procedures.",
      "Devengados / Bonificacion - BonificacionS (NIE139)"),

    C("CO-BONIF-NOSALARIAL", "Extra-statutory bonus under a written non-salary pact",
      "Bonificacion Extralegal No Salarial (Pacto CST art. 128)", P_NONSAL_A,
      "Contractual amount under an EXPRESS WRITTEN non-salary pact; excluded from the IBC only up to 40% of "
      "total remuneration (Ley 1393 de 2010 art. 30), the excess forced back in",
      "THE COLOMBIAN WORKHOUSE AND ITS LIMIT. Ley 1393 de 2010 art. 30, verified verbatim: 'Sin perjuicio de "
      "lo previsto para otros fines, para los efectos relacionados con los articulos 18 y 204 de la Ley 100 de "
      "1993, los pagos laborales no constitutivos de salario de los trabajadores particulares no podran ser "
      "superiores al 40% del total de la remuneracion.' A valid pact removes the payment from the labour-law "
      "salary base PERMANENTLY - it never enters the statutory-benefit base or the overtime base - but removes "
      "it from the CONTRIBUTION base only up to 40%. The excess is added back for health, pension, the "
      "solidarity fund and occupational risk while remaining non-salary for the benefits: TWO DIVERGENT BASES, "
      "PERMANENTLY. The clamp reaches arts. 18 and 204 of Ley 100 ONLY - it does not reach the CCF / SENA / "
      "ICBF levies, which have their own Ley 21/1982 base. AND IT HAS NO TAX EFFECT WHATSOEVER: the payment "
      "remains fully taxable employment income. Any engine that treats a non-salary flag as a tax exclusion "
      "will systematically under-withhold. See also Resolucion MinProteccion 2641 de 2011.",
      "Devengados / Bonificacion - BonificacionNS (NIE140)"),

    C("CO-GRATIF-OCASIONAL", "Occasional gratuity (mera liberalidad)", "Gratificacion Ocasional", P_GRATUITY,
      "One-off gratuitous amount, not habitual and not contractually owed",
      "CST art. 128 excludes 'las sumas que ocasionalmente y por mera liberalidad recibe el trabajador del "
      "empleador' from salary, so out of the statutory-benefit and vacation bases - but FULLY TAXABLE, and "
      "counted in the 40% clamp test as a pago laboral no constitutivo de salario.",
      "Devengados / Bonificacion - BonificacionNS (NIE140)"),

    C("CO-SALARIO-ESPECIE", "Salary in kind", "Salario en Especie", P_BIK_SAL,
      "Value stated EXPRESSLY IN THE EMPLOYMENT CONTRACT, or by expert appraisal in default of agreement; "
      "may not exceed 50% of total salary, or 30% where the employee earns the legal minimum wage",
      "CST art. 129, verified verbatim: 'Constituye salario en especie toda aquella parte de la remuneracion "
      "ordinaria y permanente que reciba el trabajador como contraprestacion directa del servicio, tales como "
      "alimentacion, habitacion o vestuario que el empleador suministra al trabajador o a su familia... El "
      "salario en especie debe valorarse expresamente en todo contrato de trabajo. A falta de estipulacion o de "
      "acuerdo sobre su valor real se estimara pericialmente, sin que pueda llegar a constituir y conformar "
      "mas del cincuenta por ciento (50%) de la totalidad del salario. No obstante, cuando un trabajador "
      "devengue el salario minimo legal, el valor por el concepto de salario en especie no podra exceder del "
      "treinta por ciento (30%).' Fully in the IBC, the payroll-levy base, the statutory-benefit base and the "
      "vacation base, and fully taxable. COLOMBIA HAS NO PUBLISHED BENEFIT-IN-KIND VALUATION SCALE - no "
      "company-car table, no accommodation scale, no notional-value list; the absence is principled, because "
      "art. 129 num. 2 routes an unvalued benefit to expert appraisal, not to a table. The engine therefore "
      "REQUIRES a contractual value on every in-kind wage type. There is no fringe-benefits tax and no "
      "separate benefits return. Mechanically the benefit produces a positive earnings line plus an offsetting "
      "deduction line, so net cash pay is unchanged while the withholding and contributions are correct.",
      "Devengados / OtroConcepto - ConceptoS (NIE147)"),

    C("CO-PRIMA-SERVICIOS", "Statutory service bonus", "Prima de Servicios", P_PRIMA,
      "(monthly salary + auxilio de transporte) x days worked in the semester / 360 = 30 days' salary per "
      "year, 15 per semester; half by 30 JUNE and half by 20 DECEMBER; monthly accrual 8.3333%",
      "CST art. 306 as amended by Ley 1788 de 2016 art. 1, universal for every private-sector employee and "
      "expressly including domestic-service employees, family-service drivers, day workers and farm workers. "
      "CST art. 307: 'La prima anual no es salario, ni se computara como factor del salario en ningun caso' - "
      "so OUT of the IBC and OUT of the payroll-levy base. Base = salary PLUS the auxilio de transporte; "
      "variable pay enters at the semester average. Set off against contractual or Christmas bonuses (CST "
      "art. 308), so an employer already paying a 13th-month equivalent does not pay twice. Absorbed by an "
      "all-inclusive salary. TAX: separate art. 383 table read under Procedure 1 for the statutory minimum; "
      "folded into the ordinary base under Procedure 2.",
      "Devengados / Primas - Cantidad (NIE117), Pago (NIE118), PagoNS (NIE119)"),

    C("CO-CESANTIAS", "Severance savings", "Auxilio de Cesantias", P_CESANT,
      "(monthly salary + auxilio de transporte) x days of service / 360 = one month's salary per year; "
      "monthly accrual 8.3333%; liquidated at 31 December and DEPOSITED TO THE FUND BY 14 FEBRUARY",
      "Statutory benefit under CST Titles VIII-IX, excluded from salary by art. 128, so out of the IBC and the "
      "payroll-levy base. EXCLUDED FROM THE MONTHLY WITHHOLDING BASE ENTIRELY under both procedures (ET "
      "arts. 385, 386) - not merely exempt. Exempt in full where the average monthly income of the last six "
      "months is <= 350 UVT (" + CESA_EXEMPT + "), then tapering 90 / 80 / 60 / 40 / 20 / 0% through 650 UVT "
      "(ET art. 206 num. 4); the 25% exemption of art. 206 num. 10 does NOT apply (art. 206 par. 2). LATE "
      "DEPOSIT COSTS ONE DAY'S SALARY PER DAY OF DELAY (Ley 50 de 1990 art. 99 num. 3). Ley 2466 de 2025 "
      "art. 64 adds a paragraph to Ley 50 art. 99 permitting the employer to deposit 8.33% of the base monthly "
      "as an ADVANCE DEPOSIT - verified verbatim: 'En ningun caso la consignacion anticipada podra entenderse "
      "como pago parcial de la cesantia, pues el trabajador solo tendra acceso a la cesantia anticipada en los "
      "terminos que asi lo determine la Ley o a la terminacion del contrato de trabajo.' Reported on three "
      "SEPARATE lines of the information return - paid to the employee (N18), deposited to the fund (N19) and "
      "recognised under the traditional regime (N20).",
      "Devengados / Cesantias - Pago (NIE120); Consignacion Cesantias T14"),

    C("CO-INTERESES-CESANTIAS", "Interest on severance savings", "Intereses a las Cesantias", P_CESANT,
      "cesantias balance at 31 December x 12% per year x days / 360; monthly accrual 1.0000%; PAID TO THE "
      "EMPLOYEE DURING JANUARY (optionally monthly at 1% by written agreement, Ley 2466 de 2025 art. 64)",
      "Ley 52 de 1975 art. 1. Statutory benefit, out of the IBC and the payroll-levy base, and excluded from "
      "the monthly withholding base under both procedures, carrying the same art. 206 num. 4 exemption and "
      "taper as the principal. PAID TO THE EMPLOYEE DIRECTLY, NOT TO THE FUND - unlike the principal. Failure "
      "to pay it costs an indemnity equal to the interest owed, once only.",
      "Devengados / Cesantias - Porcentaje (NIE121), PagoIntereses (NIE122)"),

    C("CO-VACACIONES", "Annual leave taken", "Vacaciones Disfrutadas", P_VAC,
      "(ordinary salary EXCLUDING overtime and rest-day work) x working days of vacation / 30; entitlement 15 "
      "WORKING days per year of service; accrual = salary x days / 720; variable pay -> average of the "
      "immediately preceding year",
      "VACATION IS NOT A PRESTACION SOCIAL - IT IS PAID REST, and every consequence is counter-intuitive. It "
      "ENTERS THE IBC (contributions continue during leave; PILA change event VAC/LR) and ENTERS THE "
      "PAYROLL-LEVY BASE (Ley 21/1982 art. 17 covers descansos remunerados by name). Its own base excludes "
      "overtime and rest-day work ONLY - CST art. 192, verified verbatim: 'solo se excluiran para la "
      "liquidacion de vacaciones el valor del trabajo en dias de descanso obligatorio y el valor del trabajo "
      "suplementario en horas extras' - so the NIGHT PREMIUM AND COMMISSIONS STAY IN. The auxilio de transporte "
      "is NOT in the vacation base. AN ALL-INCLUSIVE SALARY DOES NOT ABSORB IT (CST art. 132 num. 2 expressly "
      "excepts vacation), so vacation is owed on the FULL 100% while contributions run on 70%. Fully taxable. "
      "Accrual suspended during unpaid leave.",
      "Devengados / VacacionesComunes - FechaInicio (NIE109), Cantidad (NIE111), Pago (NIE112)"),

    C("CO-VACACIONES-COMPENSADAS", "Vacation compensated in cash", "Compensacion en Dinero de Vacaciones", P_VAC,
      "Up to HALF the accrued leave, on the employee's PRIOR WRITTEN REQUEST (CST art. 189 num. 1); same base "
      "as vacation taken",
      "Cash compensation of vacation is paid rest on the same footing as leave actually taken: IN the IBC and "
      "IN the payroll-levy base, fully taxable. It is THE MOST COMMONLY MISSED CONTRIBUTORY LINE IN A "
      "TERMINATION SETTLEMENT - accrued vacation paid in cash on termination is contributory, whereas the "
      "accrued prima, cesantias, interest and the dismissal indemnity are not. Requires the employee's prior "
      "written request; the employer may not impose it.",
      "Devengados / VacacionesCompensadas - Cantidad (NIE115), Pago (NIE116)"),

    C("CO-DOTACION", "Work clothing and footwear", "Dotacion de Labor (Calzado y Vestido)", P_NOTINC,
      "One pair of shoes and one work outfit FREE OF CHARGE every four months (three deliveries a year) to "
      "employees whose monthly remuneration is up to 2 SMMLV (" + AUX_CAP + ") and who have more than three "
      "months' service; delivered on 30 APRIL, 31 AUGUST and 20 DECEMBER",
      "CST art. 230 as modified by Ley 11 de 1984 art. 7, verified verbatim: 'Todo empleador que habitualmente "
      "ocupe uno (1) o mas trabajadores permanentes, debera suministrar cada cuatro (4) meses, en forma "
      "gratuita, un (1) par de zapatos y un (1) vestido de labor al trabajador, cuya remuneracion mensual sea "
      "hasta dos (2) meses el salario minimo mas alto vigente. Tiene derecho a esta prestacion el trabajador "
      "que en las fechas de entrega de calzado y vestido haya cumplido mas de tres (3) meses al servicio del "
      "empleador.' Delivery dates from art. 232. Provided to enable the work, so NOT salary, NOT taxable, and "
      "outside every base - the one item on the payslip that is genuinely nil across all five columns. The "
      "nomina electronica gives it a DEDICATED informational element. Where owed but undelivered and settled "
      "in cash on termination it remains non-taxable.",
      "Devengados / Dotacion (NIE156)"),

    C("CO-INCAP-EG-EMPLEADOR", "Sickness incapacity, days 1-2 (employer)",
      "Incapacidad por Enfermedad General - Dias 1 y 2 (Empleador)", P_INCAP_ER,
      "S / 30 x 0.6667 x d for the first two days, floored at the minimum-wage equivalent (Mercans default "
      "66.67%, configurable)",
      "Decreto 2943 de 2013 art. 1, compiled at Decreto 780 de 2016 art. 3.2.1.10, allocates 'las prestaciones "
      "economicas correspondientes a los dos (2) primeros dias de incapacidad originada por enfermedad "
      "general' to the EMPLOYER but does NOT state the rate. CST art. 227 sets the auxilio at two thirds for "
      "the first 90 days and market practice applies 66.67% for days 1-2 on that basis; a minority practice "
      "pays 100%. MERCANS DEFAULT 66.67%, CONFIGURABLE - an open item carried in the QA report, together with "
      "the minimum-wage top-up floor where 66.67% of salary falls below one SMMLV, whose primary regulatory "
      "source was not retrieved this pass. Not salary, but IN the IBC, IN the payroll-levy base and IN the "
      "statutory-benefit base, and taxable. The auxilio de transporte is NOT paid for sick days.",
      "Devengados / Incapacidad - Tipo (NIE126) = enfermedad general, Pago (NIE127); PILA T2R2-025"),

    C("CO-INCAP-EG-EPS", "Sickness incapacity from day 3 (EPS)",
      "Incapacidad por Enfermedad General - desde el Dia 3 (EPS)", P_INCAP_EPS,
      "IBC / 30 x 0.6667 x d for days 3-90 and x 0.50 for days 91-180, floored at the minimum-wage "
      "equivalent; variable salary -> average of the year of service preceding the incapacity (CST art. 228)",
      "Paid by the EPS, in practice ADVANCED by the employer through payroll and recovered from the insurer. "
      "Not employer salary, so OUT of the payroll-levy base - but CONTRIBUTIONS CONTINUE ON THE BASE (PILA "
      "change event IGE), so it is in the IBC column. Exempt within the statutory minimum (ET art. 206 "
      "nums. 1-2 and par. 1, which limits the exemption to 'las cantidades que correspondan al minimo legal' "
      "and taxes the excess). The PILA carries the incapacity authorisation number and value (T2R2-057, "
      "T2R2-058) so the employer can offset the recovery.",
      "Devengados / Incapacidad - Cantidad (NIE125), Pago (NIE127); PILA T2R2-057, T2R2-058"),

    C("CO-INCAP-IRL", "Occupational accident or disease incapacity (ARL)",
      "Incapacidad de Origen Laboral (ARL)", P_INCAP_EPS,
      "IBC / 30 x 1.00 x d from the DAY AFTER the event, at 100% of the contribution base",
      "Paid by the ARL at 100% of the IBC from the day after the event - there is no employer-borne waiting "
      "period as there is for general illness. Not employer salary, out of the payroll-levy base, "
      "contributions continue on the base (PILA change event IRL), exempt within the statutory minimum. NOTE "
      "the coverage gate: occupational-risk cover starts the CALENDAR DAY AFTER affiliation (Decreto 1072 de "
      "2015 art. 2.2.4.2.5.4) and a new hire must be reported to the ARL no later than the business day "
      "following the start date (art. 2.2.4.3.6) - an employee who starts work before affiliation is "
      "uninsured and THE EMPLOYER BEARS THE BENEFIT DIRECTLY.",
      "Devengados / Incapacidad - Tipo (NIE126) = riesgos laborales; PILA T2R2-030, T2R2-093, T2R2-094"),

    C("CO-LIC-MATERNIDAD", "Maternity leave (18 weeks)", "Licencia de Maternidad (18 semanas)", P_INCAP_EPS,
      "S / 30 x 126 calendar days, at the salary earned when the leave begins; variable salary -> average of "
      "the last year",
      "CST art. 236. Paid by the EPS, advanced by the employer and recovered. Not employer salary, out of the "
      "payroll-levy base, contributions CONTINUE on the base (PILA change event LMA), exempt within the "
      "statutory minimum (ET art. 206 num. 2 and par. 1). The auxilio de transporte is not payable. Dismissal "
      "during the protected period without labour-inspector authorisation costs 180 days' salary (art. 239).",
      "Devengados / LicenciaMP - Cantidad (NIE130), Pago (NIE131); PILA T2R2-059, T2R2-060"),

    C("CO-LIC-PATERNIDAD", "Paternity leave (2 weeks)", "Licencia de Paternidad (2 semanas)", P_INCAP_EPS,
      "S / 30 x 14 calendar days at full salary; the leave expands by one week per percentage point of "
      "structural-unemployment reduction, capped at 5 weeks",
      "CST art. 236 par. 1. Paid by the EPS, advanced and recovered. Documentation is exacting - art. 236 "
      "par. 2 requires the CIVIL REGISTRATION OF BIRTH, to be delivered to the EPS within 30 days of the "
      "birth. Not employer salary, out of the payroll-levy base, contributions continue, exempt within the "
      "statutory minimum.",
      "Devengados / LicenciaMP - Cantidad (NIE130), Pago (NIE131)"),

    C("CO-LIC-PARENTAL-COMPARTIDA", "Shared and flexible parental leave",
      "Licencia Parental Compartida y Flexible", P_INCAP_EPS,
      "Transferred weeks of the maternity entitlement, paid on the transferring or receiving parent's own "
      "salary base as the election provides",
      "CST art. 236 pars. 6-7. Paid by the EPS on the same footing as maternity and paternity leave: not "
      "employer salary, out of the payroll-levy base, contributions continue on the base, exempt within the "
      "statutory minimum. The engine must carry the parental election and the transferred week count, since "
      "the leave moves BETWEEN two employees who may be at different employers.",
      "Devengados / LicenciaMP - Cantidad (NIE130), Pago (NIE131)"),

    C("CO-LIC-REMUNERADA", "Statutory paid leave (CST art. 57 num. 6)",
      "Licencia Remunerada Legal (CST art. 57 num. 6)", P_LEAVE_P,
      "S / 30 x days of leave, at full ordinary salary",
      "CST art. 57 num. 6 as modified by Ley 2466 de 2025 art. 15 - paid leave for exercising the vote, "
      "holding a transitory official post of compulsory acceptance, grave domestic calamity, attending a union "
      "commission, medical and dental appointments, school obligations of the employee's children, judicial "
      "summonses, and the bicycle-commuting rest day. PAID REST, so IN the IBC, IN the payroll-levy base "
      "(descansos remunerados de ley, Ley 21/1982 art. 17), IN the statutory-benefit base and IN the vacation "
      "base, and fully taxable. Employer-borne, not EPS-borne.",
      "Devengados / LicenciaR - Cantidad (NIE134), Pago (NIE135); PILA T2R2-027 (VAC-LR)"),

    C("CO-LIC-LUTO", "Bereavement leave (5 working days)", "Licencia de Luto (5 dias habiles)", P_LEAVE_P,
      "S / 30 x 5 working days, at full ordinary salary",
      "CST art. 57 num. 10 (Ley 1280 de 2009): five WORKING days on the death of a spouse or permanent "
      "partner, or a relative within the second degree of consanguinity, the first of affinity or the first "
      "civil. Employer-borne paid rest: in the IBC, the payroll-levy base, the statutory-benefit base and the "
      "vacation base, and fully taxable.",
      "Devengados / LicenciaR - Cantidad (NIE134), Pago (NIE135)"),

    C("CO-LIC-NO-REMUNERADA", "Unpaid leave / contract suspension",
      "Licencia No Remunerada / Suspension del Contrato (SLN)", P_UNPAID,
      "-(S x unpaid days / 30); the auxilio de transporte is likewise not payable for those days",
      "Reported with the SLN change event, which reduces the contributory days. The Resolucion 2388 de 2016 "
      "rate table shows health moving to 8.5% or 0% and pension to 12% or 16% depending on the variant, and "
      "THE PAYROLL LEVIES FALLING TO 0%. Statutory-benefit and vacation accrual are SUSPENDED, though CST "
      "art. 53 lets the employer count the period for cesantias and pension purposes if it pays the "
      "corresponding contributions, and the period is charged against vacation. The month's taxable payments "
      "fall, so the withholding follows automatically.",
      "Devengados / LicenciaNR (NIE136-NIE138); PILA T2R2-024, T2R2-083, T2R2-084"),

    C("CO-HUELGA-LEGAL", "Legal strike days", "Huelga Legal", P_UNPAID,
      "Unpaid for the duration of the lawful strike; days reported for the period",
      "A lawful strike suspends the contract, so the days are unpaid and accrual is suspended on the same "
      "footing as unpaid leave. The nomina electronica carries a dedicated HuelgaLegal block with start date, "
      "end date and day count, so the days must be tracked separately from ordinary unpaid leave.",
      "Devengados / HuelgaLegal - FechaInicio (NIE143), Cantidad (NIE145)"),

    C("CO-APOYO-APRENDIZ", "Apprentice maintenance support", "Apoyo de Sostenimiento del Aprendiz", P_APRENDIZ,
      "DUAL training: 75% of SMMLV = 1,313,178.75 in year 1, 100% = " + SMMLV + " in year 2. TRADITIONAL "
      "training: 75% in the classroom phase, 100% in the practical phase. University student: 100% minimum",
      "CST art. 81 as substituted by Ley 2466 de 2025 art. 21, verified verbatim: 'Si es una formacion dual, "
      "el aprendiz recibira como minimo durante el primer ano el equivalente al setenta y cinco por ciento "
      "(75%) de un (1) salario minimo legal mensual vigente y durante el segundo ano el equivalente al cien "
      "por ciento (100%)... Si es formacion tradicional, el aprendiz recibira como minimo en la fase lectiva "
      "el equivalente al setenta y cinco por ciento (75%)... y en la parte practica, el apoyo del "
      "sostenimiento sera equivalente al cien por ciento (100%).' NOT the minimum wage as such - a maintenance "
      "support payment expressed as a percentage of it. SPECIAL CONTRIBUTION REGIME: Decreto 0223 de 5 marzo "
      "2026 art. 2.2.6.3.3.4 par. 2 provides that 'en todo caso la base de cotizacion debe ser [de] un (1) "
      "salario minimo legal mensual vigente', so an apprentice on 75% of the SMMLV nonetheless contributes on "
      "a FULL minimum wage. The CLASSROOM phase carries health and occupational risk ONLY; the PRACTICAL or "
      "DUAL phase carries the full IBC, the payroll-levy base, the statutory-benefit base and the vacation "
      "base. Taxable. Medical-intern remuneration under CST art. 81A (Ley 2466 art. 22) is paid by the health "
      "system resource administrator and is OUT OF SCOPE per scope_manifest.",
      "Devengados / ApoyoSost (NIE157); Decreto 0223 de 2026 art. 2.2.6.3.3.4"),

    C("CO-INDEM-DESPIDO", "Indemnity for dismissal without just cause",
      "Indemnizacion por Despido sin Justa Causa (CST art. 64)", P_INDEM,
      "Salary BELOW 10 SMMLV (< " + EXON_CUT + "): 30 days' salary for the first year, PLUS 20 days for each "
      "subsequent year and pro rata. Salary AT OR ABOVE 10 SMMLV: 20 days, PLUS 15 days",
      "CST art. 64 as amended by Ley 789 de 2002 art. 28. FULLY TAXABLE ordinary employment income entering "
      "the ordinary monthly base - ET art. 206 nums. 1-3 exempt only accident, illness and maternity-protection "
      "indemnities and art. 206 par. 1 limits even those to the statutory minimum amount, so an art. 64 "
      "indemnity has NO tax-free portion and Colombia has NO concessional cap on termination payments. OUT of "
      "the IBC, the payroll-levy base, the statutory-benefit base and the vacation base. Employees with 10 or "
      "more years of continuous service at the entry into force of Ley 789 de 2002 retain the earlier Ley 50 "
      "de 1990 art. 6 literals b), c) and d) scale. THE EASILY MISSED GATE - CST art. 65 par. 1: the employer "
      "must inform the employee in writing within 60 days of the termination of the payment status of the "
      "contributions on the last three months' salaries, attaching the receipts, and 'si el empleador no "
      "demuestra el pago de dichos aportes, la terminacion del contrato no producira efecto'; the employer may "
      "still pay within a further 60 days with default interest. CST art. 66 requires the cause to be stated "
      "AT THE MOMENT of termination.",
      "Devengados / Indemnizacion (NIE160)"),

    C("CO-INDEM-MORATORIA", "Late-payment penalty", "Indemnizacion Moratoria (CST art. 65)", P_INDEM,
      "One day's salary for each day of delay, up to 24 months, then default interest at the maximum "
      "free-allocation credit rate; employees earning LESS THAN 1 SMMLV stay on the UNCAPPED original rule "
      "(CST art. 65 par. 2)",
      "CST art. 65 as amended by Ley 789 de 2002 art. 29, payable where salaries and statutory benefits are "
      "unpaid at termination. FULLY TAXABLE, out of every social-security base. NOTE THE SPLIT: the 24-month "
      "cap and the subsequent default interest apply to employees earning one SMMLV or more; those earning "
      "LESS remain on the uncapped pre-2002 rule, which can produce a materially larger liability.",
      "Devengados / Indemnizacion (NIE160)"),

    C("CO-SANCION-CESANTIAS", "Penalty for non-deposit of severance savings",
      "Sancion por No Consignacion de Cesantias", P_INDEM,
      "One day's salary for each day of delay beyond 14 February (Ley 50 de 1990 art. 99 num. 3)",
      "A distinct statutory penalty from the CST art. 65 moratoria and cumulable with it. Fully taxable, out "
      "of every social-security base. Triggered by failure to deposit the 31 December cesantias balance to the "
      "employee's chosen fund by 14 February - one of the two hard year-end dates in Colombian payroll.",
      "Devengados / Indemnizacion (NIE160)"),

    C("CO-SANCION-INTERESES", "Penalty for unpaid severance interest",
      "Sancion por No Pago de Intereses a las Cesantias", P_INDEM,
      "An amount EQUAL TO the interest owed, payable ONCE ONLY (Ley 52 de 1975 art. 1)",
      "Ley 52 de 1975 art. 1: where the employer fails to pay the 12% interest it must pay the employee, 'a "
      "titulo de indemnizacion y por una sola vez', an amount equal to the interest owed. Fully taxable, out "
      "of every social-security base. The interest itself is paid TO THE EMPLOYEE during January, not to the "
      "fund - the most common cause of this penalty is treating it like the principal.",
      "Devengados / Indemnizacion (NIE160)"),

    C("CO-INDEM-FIJO-OBRA", "Indemnity for early termination of a fixed-term or work-or-task contract",
      "Indemnizacion por Terminacion Anticipada de Contrato a Termino Fijo u Obra o Labor", P_INDEM,
      "Fixed-term: the salaries for the remaining term. Work or task: the remaining term of the work, NEVER "
      "LESS THAN 15 DAYS",
      "CST art. 64. Fully taxable ordinary employment income, out of every social-security base. The 15-day "
      "floor on a work-or-task contract is absolute and applies however short the remaining term.",
      "Devengados / Indemnizacion (NIE160)"),

    C("CO-INDEM-PROTECCION", "Indemnity for dismissal during protected status",
      "Indemnizacion por Despido en Estado de Proteccion (Fuero)", P_INDEM,
      "180 days' salary for a pregnant or nursing employee (CST art. 239); 180 days' salary PLUS reinstatement "
      "for an employee with a disability dismissed without labour-inspector authorisation (Ley 361 de 1997 "
      "art. 26)",
      "Fully taxable, out of every social-security base. Distinct from and additional to the art. 64 indemnity. "
      "The disability protection carries REINSTATEMENT as well as the indemnity, so the engine must be able to "
      "reverse a termination and restore contributions retroactively.",
      "Devengados / Indemnizacion (NIE160)"),

    C("CO-BONIF-RETIRO", "Retirement or mutual-termination settlement bonus",
      "Bonificacion por Retiro / Acuerdo de Terminacion", P_INDEM,
      "Negotiated contractual amount; no statutory retirement gratuity exists in Colombia",
      "An occasional, gratuitous sum under CST art. 128, so out of every social-security base - but FULLY "
      "TAXABLE, and FREQUENTLY AND WRONGLY ASSUMED EXEMPT. A payment in lieu of notice is on the same footing "
      "(there is no statutory employer notice period in Colombia). A non-compete payment is generally not "
      "salary but is likewise fully taxable. The nomina electronica gives the retirement bonus a dedicated "
      "element, separate from Indemnizacion.",
      "Devengados / BonifRetiro (NIE159)"),

    C("CO-PAGO-ALIMENTACION-3P", "Third-party meal payments", "Pagos de Alimentacion a Terceros", P_MEAL3P,
      "NOT income up to 41 UVT/month = " + MEAL_CAP + " where the employee's salary does NOT exceed 310 UVT = "
      + MEAL_SAL + "; the EXCESS over 41 UVT is taxable employment income",
      "ET art. 387-1. Payments made by the employer TO A THIRD PARTY for the food of the employee or the "
      "employee's family - spouse or permanent partner, children and parents - including the purchase of meal "
      "vouchers or tickets. TWO INDEPENDENT CONDITIONS, BOTH MUST HOLD: the salary ceiling AND payment to a "
      "third party. CASH PAID TO THE EMPLOYEE FOR FOOD IS SALARY AND GETS NONE OF THIS TREATMENT. Within the "
      "limit it is income to the third party supplying the food, not to the employee. Not salary, so out of "
      "every social-security base. Representation expenses are expressly outside this rule. The information "
      "return reports the within-limit amount and the excess on SEPARATE numerals (N32 and N08), so the engine "
      "must carry two accumulators, not one.",
      "Devengados / BonoEPCTV - PagoAlimentacionS (NIE153) / PagoAlimentacionNS (NIE154)"),

    C("CO-BONO-EPCTV", "Voucher, card or non-cash instrument payment",
      "Pago con Bonos Electronicos o de Papel, Cheques, Tarjetas o Vales", P_NONSAL,
      "Face value of the instrument; salary or non-salary according to the CST art. 127 / 128 classification "
      "of the underlying payment",
      "The nomina electronica carries PAIRED salary and non-salary voucher elements, so the engine must set the "
      "salary flag at configuration and must not derive it at reporting time. Where the instrument delivers "
      "FOOD through a third party the ET art. 387-1 regime applies instead (see CO-PAGO-ALIMENTACION-3P); "
      "where it delivers anything else it is remuneration, taxable in full, and salary unless a valid written "
      "art. 128 pact applies. Reported at Formulario 220 casilla 37 / Formato 2276 numeral N07. " ,
      "Devengados / BonoEPCTV - PagoS (NIE151) / PagoNS (NIE152)"),

    C("CO-MEDICINA-PREPAGADA-ER", "Employer-paid prepaid health / supplementary health plan",
      "Medicina Prepagada o Plan Complementario Pagado por el Empleador", P_NONSAL,
      "Premium paid by the employer; the employee may deduct up to 16 UVT/month = COP 837,984 against the "
      "withholding base (ET art. 387 lits. a and b)",
      "NOT a statutory exclusion - a TAXABLE benefit to the employee, reported as an earnings line and "
      "withheld in the ordinary monthly base, with an offsetting deduction line so net cash pay is unchanged. "
      "The employee separately obtains the art. 387 deduction of up to 16 UVT per month on a provider "
      "certificate, where the provider is supervised by the NATIONAL HEALTH SUPERINTENDENCE (prepaid medicine) "
      "or the FINANCIAL SUPERINTENDENCE (health insurance). Market practice structures the employer premium as "
      "non-salary under a written art. 128 pact, which keeps it out of the IBC up to the 40% clamp. It does "
      "NOT replace the compulsory 12.5% health contribution.",
      "Devengados / Auxilio - AuxilioNS (NIE142); Deducciones / PlanComplementarios (NIE182)"),

    C("CO-APORTE-PENSION-VOL-ER", "Employer contribution to a voluntary pension fund",
      "Aporte Patronal a Fondo de Pensiones Voluntarias", P_VOLPEN,
      "Amount contributed, within the SHARED cap of the lower of 30% of labour income or 3,800 UVT per year "
      "= COP 199,021,200 (ET arts. 126-1 and 126-4, shared with AFC / AVC)",
      "EXEMPT INCOME to the employee, subtracted at step (E) of the art. 388 depuration INSIDE the 40% and "
      "1,340-UVT caps. Treated as the employee's own contribution for cap purposes. Deductible for the "
      "employer up to 3,800 UVT per employee (art. 126-1 first paragraph). NO OCCUPATIONAL PENSION SCHEME "
      "EXISTS IN COLOMBIA in the defined-benefit or defined-contribution sense - the mandatory system is "
      "universal and the voluntary fund is an individual product to which an employer may contribute, not an "
      "employer-sponsored plan with its own trustees.",
      "Devengados / Auxilio - AuxilioNS (NIE142); Formulario 220 casilla 56 / Formato 2276 N26"),

    C("CO-APORTE-RAIS-VOL-ER", "Employer voluntary contribution to the individual pension account",
      "Cotizacion Voluntaria al RAIS pagada por el Empleador", P_RAISVOL,
      "Amount contributed, within the lower of 25% of annual labour income or 2,500 UVT per year "
      "= COP 130,935,000 (ET art. 55)",
      "NON-TAXABLE INCOME (ingreso no constitutivo de renta ni ganancia ocasional) under ET art. 55, "
      "subtracted at step (B) of the depuration - BEFORE the 40% cap reference figure is struck, which makes "
      "it MATERIALLY MORE VALUABLE than exempt income. Distinguish it carefully from the voluntary pension "
      "FUND contribution of art. 126-1, which is exempt income inside the caps. A withdrawal that does not "
      "meet the qualifying conditions is WITHHELD AT 35%. Reported on the PILA as the AVP change event.",
      "Devengados / Auxilio - AuxilioNS (NIE142); PILA T2R2-028, T2R2-049; Formato 2276 N25"),

    C("CO-ACCIONES", "Equity and share-incentive awards", "Acciones e Incentivos en Acciones", P_EQUITY,
      "Taxable spread = market value at exercise or vesting LESS the exercise price paid by the employee",
      "TAXABLE EMPLOYMENT INCOME AT EXERCISE OR VESTING, on the spread, in the ordinary monthly base and the "
      "art. 383 table. The subsequent disposal is a separate capital transaction outside payroll. Generally "
      "non-salary, so out of the statutory-benefit and vacation bases, but counted in the 40% clamp test. "
      "Colombia has no notional valuation scale, so the market value must be evidenced. For a non-resident, "
      "ET art. 408 applies at 20% where the underlying service was performed in Colombia; where performed "
      "abroad the income is foreign-source and not taxable in Colombia.",
      "Devengados / OtroConcepto - ConceptoS or ConceptoNS (NIE146-NIE148)"),

    C("CO-VIATICOS-PERMANENTES", "Permanent per diem - board and lodging portion (salary)",
      "Viaticos Permanentes - Manutencion y Alojamiento (Salarial)", P_SAL,
      "The part of a PERMANENT per diem destined to provide the employee MANUTENCION and ALOJAMIENTO; the "
      "value of each concept must be specified whenever paid (CST art. 130)",
      "CST art. 130 as modified by Ley 50 de 1990 art. 17, verified verbatim: 'Los viaticos permanentes "
      "constituyen salario en aquella parte destinada a proporcionar al trabajador manutencion y alojamiento; "
      "pero no en lo que solo tenga por finalidad proporcionar los medios de transporte o los gastos de "
      "representacion. Siempre que se paguen debe especificarse el valor de cada uno de estos conceptos.' This "
      "portion is SALARY: in the IBC, the payroll-levy base, the statutory-benefit base and the vacation base, "
      "and fully taxable. The nomina electronica enforces the split with paired elements, so configure TWO "
      "wage types and never one. Reported at Formulario 220 casilla 43 / Formato 2276 numeral N13.",
      "Devengados / Transporte - ViaticoManuAlojS (NIE072)"),

    C("CO-VIATICOS-OCASIONALES", "Occasional per diem, and the transport / representation portion",
      "Viaticos Accidentales y Porcion de Transporte y Representacion (No Salarial)", P_NOTINC,
      "Occasional per diem paid on an extraordinary, non-habitual or infrequent requirement, and the portion "
      "of any per diem destined only to transport or representation expenses",
      "CST art. 130 final paragraph: 'Los viaticos accidentales no constituyen salario en ningun caso. Son "
      "viaticos accidentales aquellos que solo se dan con motivo de un requerimiento extraordinario, no "
      "habitual o poco frecuente.' Neither salary nor taxable income where it is a genuine reimbursement of "
      "employer expenditure - outside every base. Representation expenses are also expressly outside the "
      "ET art. 387-1 meal rule and are deductible for the employer.",
      "Devengados / Transporte - ViaticoManuAlojNS (NIE073)"),

    C("CO-TELETRABAJO", "Telework allowance", "Auxilio de Teletrabajo", P_NONSAL,
      "Contractual amount toward the cost of the telework arrangement (energy, internet, workstation), "
      "distinct from the statutory auxilio de conectividad",
      "Where the payment REIMBURSES documented telework costs incurred in the employer's interest it falls "
      "under CST art. 128 as an amount given to enable the work and is outside every base. Where it is a "
      "round, undocumented monthly amount it is remuneration - salary unless a valid written art. 128 pact "
      "applies, and taxable either way. Configured here as a pacted non-salary allowance, the market default. "
      "Distinguish the STATUTORY auxilio de conectividad for teleworkers earning less than 2 SMMLV, which "
      "replaces the transport allowance (see CO-AUX-CONECTIVIDAD). The telework mode - autonomous, mobile or "
      "supplementary - must be declared in the telework agreement.",
      "Devengados / Teletrabajo (NIE158)"),

    C("CO-PROPINAS", "Tips", "Propinas", P_NOTINC,
      "Amounts received by the employee from customers; may NOT be stipulated as remuneration for the service",
      "CST art. 131, verified verbatim: 'Las propinas que recibe el trabajador no constituye salario. No puede "
      "pactarse como retribucion del servicio prestado por el trabajador lo que este reciba por propinas.' "
      "Tips are not an employer payment at all, so they are outside every base and outside employer payroll. "
      "Retained as an informational line because a hospitality-sector client will report them, and because an "
      "attempt to treat tips as part of the contractual salary is unlawful and must be blocked at "
      "configuration.",
      "Not a nomina electronica devengado (not an employer payment)"),

    C("CO-COMPENSACION-COOP", "Cooperative associated-work compensation",
      "Compensacion Ordinaria y Extraordinaria del Trabajo Asociado Cooperativo", P_NOTINC,
      "Ordinary and extraordinary compensation fixed by the cooperative's own compensation regime",
      "OUT OF SCOPE of an employment payroll: an associated worker of a cooperative is not an employee and "
      "there is no employment contract, so CST arts. 127 / 128 do not apply and the contribution regime is "
      "the independent-worker one. Retained because the nomina electronica carries dedicated elements and the "
      "information return a dedicated numeral (N15 / Formulario 220 casilla 45), and because a client "
      "operating a cooperative will present the concept. Configured outside every employment base.",
      "Devengados / Compensacion - CompensacionO (NIE149) / CompensacionE (NIE150)"),

    C("CO-PAGO-TERCERO", "Third-party payment (accrued)", "Pago a Terceros (Devengado)", P_NONSAL_A,
      "Amount the employer pays to a third party on the employee's behalf and reports as accrued",
      "The nomina electronica carries PagoTercero in BOTH the devengados (NIE193) and the deducciones (NIE195) "
      "blocks, so the two legs net to zero in net pay while the accrued value is correctly reported. The "
      "underlying payment must still be classified on its own facts under CST arts. 127 / 128 and taxed "
      "accordingly - the third-party route changes the payment mechanics, not the classification. A meal "
      "payment to a third party has its own ET art. 387-1 regime.",
      "Devengados / PagosTerceros - PagoTercero (NIE193)"),

    C("CO-ANTICIPO-NOMINA", "Payroll advance (accrued)", "Anticipo de Nomina (Devengado)", P_ANTICIPO,
      "Advance of the period's pay, or a recoverable advance repaid by deduction under a written CST art. 151 "
      "agreement stating the instalment and the amortisation period",
      "CONDITIONAL BY DESIGN. An advance OF the period's salary is salary and enters every base in the period "
      "to which it relates; a recoverable advance or loan is not remuneration at all, and the paired "
      "devengado / deduccion elements let the two legs net to zero. CST art. 151 requires the instalment and "
      "amortisation period to be agreed in writing and bars unilateral variation; art. 149 num. 2 bars any "
      "recovery that would breach the SMMLV floor or the non-attachable portion without a court order, in "
      "which case the instalment must be SUSPENDED and carried forward with the arrears made visible on the "
      "payslip - never silently rescheduled.",
      "Devengados / Anticipos - Anticipo (NIE194)"),

    C("CO-REINTEGRO", "Reimbursement to the employee (accrued)", "Reintegro (Devengado)", P_NOTINC,
      "Amount returned to the employee for a prior over-deduction or an expense borne on the employer's behalf",
      "A reimbursement is not remuneration and is outside every base. WHERE IT REVERSES AN OVER-WITHHELD TAX "
      "the route is Decreto 1625 de 2016 art. 1.2.4.16: on the employee's WRITTEN REQUEST with evidence, the "
      "employer reimburses the excess and DEDUCTS THE REIMBURSED AMOUNT FROM THE WITHHOLDINGS OF THE FOLLOWING "
      "PERIOD, carrying any surplus forward until absorbed, and must keep the written request. Where it "
      "reverses an over-paid contribution, Mercans practice is to reimburse the employee promptly on the "
      "employer's authority and pursue recovery from the receiving entity separately, because the correction "
      "planilla is structurally built for under-declaration (the C-record bases and day counts must be >= the "
      "A-record ones).",
      "Devengados / Reintegro (NIE201); Deducciones / Reintegro (NIE184)"),
]
