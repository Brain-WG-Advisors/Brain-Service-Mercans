# -*- coding: utf-8 -*-
"""
Colombia (CO) Wage Type Catalogue — auxiliary sheet writers (part 4).
Version Control, Employer Sick Pay, Tax Credit (repurposed),
Global WTC Coverage and Form Reference Guide.
"""

import copy
import datetime

from openpyxl.styles import Alignment, Font

from co_wtc_config import (
    TAX_CODES, SMMLV, UVT, AUX_TTE, IBC_CAP, FSP_TRIG, EXON_CUT, INTEGRAL,
    EX25_CAP, CAP1340, CESA_EXEMPT, MEAL_CAP, MEAL_SAL, DIVISOR,
)


# ---------------------------------------------------------------------------
def write_version_control(vc):
    vc["B8"] = "Wage Type Catalogue"
    vc["B9"] = "Colombia (CO)"
    vc["B12"], vc["C12"], vc["D12"], vc["E12"], vc["F12"] = (
        "Version", "Effective Date", "Change Description", "Status", "Updated By")
    vc["B13"], vc["C13"] = 1.0, datetime.datetime(2026, 9, 4)
    vc["D13"] = (
        "Initial Colombia Wage Type Catalogue for FY2026. All 300 global baseline codes configured fresh for "
        "Colombia (CST arts. 127/128 salary classification, the THREE separate bases, the Ley 1393/2010 40% "
        "clamp, the ET art. 114-1 exoneration cliff, the ET art. 388 depuration and the art. 383 table) plus "
        "102 Colombia-specific wage types. Social-insurance column expanded into five per-fund columns "
        "(Salud / FSP / ARL / Parafiscales / Pension) and three Colombia-specific base columns added "
        "(salary flag / statutory-benefit base / vacation base). Includes the Global WTC Coverage sheet and "
        "the Form Reference Guide (C17); every tax code defined and sourced to a Colombian authority "
        "publication (C9). Wage-type code numbers for Colombia-specific rows are DERIVED (no Mercans code "
        "range has been assigned for Colombia).")
    vc["E13"], vc["F13"] = "Released", "Mercans Compliance (build_co_wtc.py)"
    vc["B26"], vc["B27"] = "Business Analyst", "Regulation Analyst"


# ---------------------------------------------------------------------------
def write_sick_pay(sl):
    for r in range(1, min(sl.max_row, 60) + 1):
        for c in range(1, min(sl.max_column, 14) + 1):
            sl.cell(r, c).value = None
    lines = [
        "COLOMBIA - EMPLOYER SICK PAY AND THE INCAPACITY CASCADE (2026)",
        "",
        "Colombia has NO employer sick-pay scheme of the Czech kind. Cash sickness benefit is a social-security",
        "benefit, and the employer bears only the FIRST TWO DAYS of a general-illness incapacity.",
        "",
        "WHO PAYS WHAT",
        "  General illness, days 1-2 .......... EMPLOYER          66.67% (Mercans default, configurable)",
        "  General illness, days 3-90 ......... EPS (health insurer)   66.67% of the contribution base",
        "  General illness, days 91-180 ....... EPS                    50.00% of the contribution base",
        "  Occupational accident or disease ... ARL (risk insurer)    100.00% of the contribution base,",
        "                                                            from the DAY AFTER the event",
        "  Maternity leave, 18 weeks .......... EPS   salary earned when the leave begins",
        "  Paternity leave, 2 weeks ........... EPS   full salary (expands 1 week per point of structural",
        "                                             unemployment reduction, capped at 5 weeks)",
        "",
        "FORMULAE",
        "  Employer days 1-2 ............. S / 30 x 0.6667 x d, floored at the minimum-wage equivalent",
        "  EPS days 3-90 ................. IBC / 30 x 0.6667 x d, floored at the minimum-wage equivalent",
        "  EPS days 91-180 ............... IBC / 30 x 0.5000 x d, floored at the minimum-wage equivalent",
        "  ARL, occupational ............. IBC / 30 x 1.0000 x d",
        "  Maternity ..................... S / 30 x 126 calendar days",
        "  Paternity ..................... S / 30 x 14 calendar days",
        "  Variable salary ............... average of the year of service preceding the incapacity, or of the",
        "                                  whole period if under a year (CST art. 228)",
        "",
        "OPEN ITEM 1 - THE RATE FOR THE EMPLOYER'S FIRST TWO DAYS.",
        "  Decreto 2943 de 2013 art. 1, compiled at Decreto 780 de 2016 art. 3.2.1.10, allocates 'las",
        "  prestaciones economicas correspondientes a los dos (2) primeros dias de incapacidad originada por",
        "  enfermedad general' to the EMPLOYER but does NOT state the rate. CST art. 227 sets the auxilio at two",
        "  thirds for the first 90 days, and market practice applies 66.67% for days 1-2 on that basis; a",
        "  minority practice pays 100%. MERCANS DEFAULT: 66.67%, configurable. Carried in the QA report.",
        "",
        "OPEN ITEM 2 - THE MINIMUM-WAGE FLOOR ON INCAPACITY PAYMENTS.",
        "  Where 66.67% of salary falls below one SMMLV (" + SMMLV + "), market practice and settled",
        "  administrative doctrine top the payment up to one minimum wage. The primary regulatory source for",
        "  that floor was not retrieved this pass. MERCANS DEFAULT: apply the floor, configurable. Carried in",
        "  the QA report.",
        "",
        "PAYROLL TREATMENT (the counter-intuitive part)",
        "  Employer days 1-2 ....... NOT salary, but IN the IBC, IN the Ley 21/1982 payroll-levy base and IN",
        "                            the statutory-benefit base; TAXABLE.",
        "  EPS / ARL benefits ...... NOT employer salary, so OUT of the payroll-levy base - but CONTRIBUTIONS",
        "                            CONTINUE ON THE BASE (PILA change events IGE, IRL, LMA). Exempt within",
        "                            the statutory minimum (ET art. 206 nums. 1-2 and par. 1, which limits the",
        "                            exemption to 'las cantidades que correspondan al minimo legal' and taxes",
        "                            the excess). Advanced by the employer through payroll and recovered from",
        "                            the insurer; the PILA carries the authorisation number and value",
        "                            (T2R2-057 to T2R2-060) so the recovery can be offset.",
        "  Auxilio de transporte ... NOT PAYABLE for sick days - no travel occurs.",
        "  Overtime and premia ..... Not applicable during incapacity.",
        "  Benefit accrual ......... Continues (the incapacity payment is in the statutory-benefit base for the",
        "                            employer's two days); SUSPENDED only for unpaid leave (CST art. 53).",
        "",
        "Sources: CST arts. 227, 228, 236, 239; Decreto 2943 de 2013 art. 1; Decreto 780 de 2016 art. 3.2.1.10;",
        "ET art. 206 nums. 1-2 and par. 1; Ley 361 de 1997 art. 26; Resolucion MSPS 2388 de 2016 Anexo Tecnico 2;",
        "Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0.",
    ]
    for i, line in enumerate(lines, start=1):
        sl.cell(i, 1, line)
    sl.column_dimensions["A"].width = 118


# ---------------------------------------------------------------------------
def write_tax_credit(tc):
    for r in range(1, max(tc.max_row, 10) + 1):
        tc.cell(r, 1).value = None
    lines = [
        "COLOMBIA - TAX CREDITS: NOT APPLICABLE. THE EQUIVALENT MECHANISMS ARE DEDUCTIONS AND EXEMPT INCOME.",
        "",
        "Colombia has NO tax credit against the payroll withholding - no personal credit, no child credit, no",
        "disability credit and no non-refundable family credit of the kind the CZ template contemplates. Relief",
        "is delivered instead by SUBTRACTING amounts from the base, in THREE legally distinct classes whose",
        "class determines where each item sits in the ET art. 388 depuration and which caps it consumes.",
        "Getting the class wrong is the most common source of withholding error in Colombia.",
        "",
        "UVT (tax unit) 2026 = COP " + UVT + "   (Resolucion DIAN 000238 de 15 diciembre 2025 art. 1; the 2026",
        "uprating was certified at 5.17%, taking the unit from COP 49,799). Every tax parameter is indexed to",
        "the UVT and NO tax threshold is expressed in minimum wages - that is the one-caliber discipline:",
        "minimum wage for social security and labour, UVT for tax. The two are never mixed.",
        "",
        "CLASS A - NON-TAXABLE INCOME (ingresos no constitutivos de renta ni ganancia ocasional)",
        "  Subtracted at step (B), BEFORE the 40% cap reference figure is struck, so it does NOT consume the cap.",
        "  A1  Mandatory pension contribution ......... 4% of the IBC .................... ET art. 55",
        "  A2  Solidarity pension fund ............... 1% + 0.2-1.0% of the IBC .......... ET art. 55",
        "  A3  Mandatory health contribution ......... 4% of the IBC .................... ET art. 56",
        "  A4  Voluntary contributions to the individual pension account (RAIS):",
        "        the lower of 25% of annual labour income and 2,500 UVT = COP 130,935,000 . ET art. 55",
        "        (a non-qualifying withdrawal is withheld at 35%)",
        "  A5  Third-party meal payments: not income up to 41 UVT/month = " + MEAL_CAP + ",",
        "        where the employee's salary does not exceed 310 UVT = " + MEAL_SAL + " ..... ET art. 387-1",
        "",
        "CLASS B - DEDUCTIONS AND EXEMPT INCOME (deducciones y rentas exentas)",
        "  Subtracted at steps (D) and (E), INSIDE the 40% and 1,340-UVT caps.",
        "  B1  Housing-loan interest and monetary correction ... 100 UVT/month = COP 5,237,400 . ET arts. 119, 387",
        "  B2  Prepaid medicine / health insurance ............  16 UVT/month = COP   837,984 . ET art. 387 lits. a, b",
        "        (the provider must be supervised by the National Health Superintendence or the",
        "         Financial Superintendence)",
        "  B3  Dependants: 10% of the month's gross labour income, capped 32 UVT = COP 1,675,968 . ET art. 387",
        "        NOTE: 10% OF GROSS REGARDLESS OF THE NUMBER OF DEPENDANTS - it does not multiply.",
        "  B4  Voluntary pension funds + AFC / AVC long-term savings: the lower of 30% of labour",
        "        income and 3,800 UVT/year = COP 199,021,200, SHARED between the two vehicles . ET arts. 126-1, 126-4",
        "  B5  THE 25% EXEMPT-INCOME DEDUCTION ................ 790 UVT/year = COP 41,375,460 . ET art. 206 num. 10",
        "        COMPUTED LAST, on the figure net of non-taxable income, the art. 387 deductions and all other",
        "        exempt income: 'El calculo de esta renta exenta se efectuara una vez se detraiga del valor",
        "        total de los pagos laborales recibidos por el trabajador, los ingresos no constitutivos de",
        "        renta, las deducciones y las demas rentas exentas diferentes a la establecida en el presente",
        "        numeral.' Computing 25% of GROSS overstates it and under-withholds.",
        "        Monthly apportionment used: 65.8333 UVT = " + EX25_CAP + ".",
        "  B6  Cesantias and their interest: exempt in full where the average monthly income of the last six",
        "        months is <= 350 UVT = " + CESA_EXEMPT + "; then tapering 90 / 80 / 60 / 40 / 20 / 0%",
        "        through 410 / 470 / 530 / 590 / 650 UVT ......................... ET art. 206 num. 4",
        "        They are EXCLUDED from the monthly base entirely under both procedures, and the 25%",
        "        exemption does NOT apply to them (art. 206 par. 2).",
        "  B7  Pension income: taxable only above 1,000 UVT/month = COP 52,374,000 ...... ET art. 206 num. 5",
        "  B8  Accident, illness and maternity-protection indemnities and burial expenses: exempt ONLY up to",
        "        the statutory minimum amount ................................. ET art. 206 nums. 1-3, par. 1",
        "",
        "CLASS C - OUTSIDE THE CAPS ENTIRELY",
        "  C1  Additional dependants deduction: 72 UVT per dependant per year = COP 3,770,928 each,",
        "        maximum 4 dependants = COP 15,083,712/year, i.e. 6 UVT = COP 314,244 per dependant",
        "        per month ..................................... ET art. 336 num. 3, second paragraph",
        "        'en adicion al limite establecido en el inciso anterior' - it is applied AFTER and OUTSIDE",
        "        the 40% and 1,340-UVT caps.",
        "  STACKING: an EMPLOYEE may take BOTH B3 and C1 FOR THE SAME DEPENDANT. Decreto 2231 de 2023 art. 3:",
        "        'el mismo dependiente solo dara lugar a una de estas dos deducciones, excepto cuando el",
        "        contribuyente tenga ingresos por rentas de trabajo provenientes de una relacion laboral o",
        "        legal y reglamentaria, en cuyo caso podran aplicarse ambas deducciones por el mismo",
        "        dependiente.'",
        "",
        "THE COMBINED CAP",
        "  (D + E) <= 40% of (C = A - B)   AND   (D + E) <= 1,340 UVT/year = COP 70,181,160",
        "  Monthly apportionment used: 111.6667 UVT = " + CAP1340 + ".",
        "  OPEN ITEM: the 790-UVT and 1,340-UVT caps are stated ANNUALLY yet withholding is monthly. Market",
        "  practice, which Mercans follows, apportions them at one twelfth and tests each month against the",
        "  apportioned figure. No regulation prescribes the apportionment expressly. Carried in the QA report.",
        "  The CURRENT year's UVT applies to the annual caps (DIAN Concepto 015007 int. 973 de 13 septiembre 2023).",
        "",
        "NOT AVAILABLE AGAINST WITHHOLDING",
        "  The 1% / 240-UVT invoice-based deduction of ET art. 336 num. 5 is expressly excluded - 'no se tendra",
        "  en cuenta para el calculo de la retencion en la fuente' - confirmed by DIAN Concepto 015007 int. 973",
        "  de 13 septiembre 2023. It is available only in the employee's own annual return.",
        "",
        "NOT A CREDIT, AND NOT A TAX",
        "  The Contribucion Solidaria a la Educacion Superior (Contribucion Sabes) is a CST art. 150 permitted",
        "  DEDUCTION added by Ley 1911 de 2018 art. 22, not a tax and not a credit - it must never be",
        "  aggregated with the retencion en la fuente on Formulario 350.",
        "",
        "DECLARATIONS THE EMPLOYEE MUST MAKE (no relief is automatic except the 25%)",
        "  Housing-loan interest ... lender certificate.  Prepaid health ... provider certificate.",
        "  Dependants .............. number, EACH DEPENDANT'S IDENTITY DOCUMENT, relationship and basis of",
        "                            dependency; for a dependent spouse, parent or sibling, a public",
        "                            accountant's certificate of annual income below 260 UVT (COP 13,617,240)",
        "                            or a certified state of physical or psychological dependence.",
        "  Voluntary pension / AFC / AVC / RAIS ... fund or administrator certificates.",
        "  Higher withholding rate ... written request, effective the month AFTER it is made (ET art. 383 par. 3).",
        "  WHO QUALIFIES AS A DEPENDANT (ET art. 387 par. 2 nums. 2-3 as amended by Ley 2411 de 2024 art. 2):",
        "    children up to 18; children 18-25 whose higher or technical education the taxpayer finances;",
        "    children over 18 in a certified state of dependence; a spouse or permanent partner dependent by",
        "    absence of income or with annual income below 260 UVT; parents and siblings on the same conditions.",
        "",
        "OUT OF MERCANS SCOPE BUT FLAGGED SO THE ENGINE DOES NOT SILENTLY CLAMP THEM",
        "  ET art. 206 par. 4 and Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 place art. 206 nums. 6-9, the",
        "  prima especial and the prima de costo de vida OUTSIDE the 40% and 1,340-UVT limits. These attach to",
        "  military, judicial, diplomatic and public university staff - out of private-sector scope.",
        "",
        "NON-RESIDENTS GET NONE OF THE ABOVE",
        "  ET art. 408: a flat 20% on the GROSS payment, with no depuration, no art. 387 deductions, no 25%",
        "  exempt income and no tax-free band. DIAN Concepto 011108 de 29 junio 2026.",
    ]
    for i, line in enumerate(lines, start=1):
        tc.cell(i, 1, line)
    tc.column_dimensions["A"].width = 118


# ---------------------------------------------------------------------------
def write_coverage(gc, blue_hdr, n_rows, n_specific, n_earn, n_ded, n_er, n_struct):
    for ci, h in enumerate(["#", "Item", "Detail"], start=1):
        gc.cell(1, ci, h)._style = copy.copy(blue_hdr)
    cov = [
        ("Global baseline file", "shared/Global_WTC_V1_0.xlsx"),
        ("Global codes in the baseline", "300"),
        ("Global codes included in the Colombia WTC",
         "300 - ALL of them. None excluded. Every code configured FRESH for Colombia 2026 against CO-CCG-001 "
         "Modules 3-7 and the primary law in 00-official-sources/pdfs/."),
        ("Global codes excluded", "0"),
        ("Colombia-specific additions",
         "%d CO-prefixed wage types: %d earnings (core pay, the six premium hour types, the statutory "
         "benefits, the leave cascade, the termination heads), %d employee deductions, %d employer "
         "contributions and accruals, %d bases / intermediaries / rates / flags."
         % (n_specific, n_earn, n_ded, n_er, n_struct)),
        ("Total rows in the Wage Type Catalogue", str(n_rows)),
        ("SS-fund column expansion (why five, not one)",
         "Colombia has EIGHT mandatory contributions across THREE insurance branches, THREE payroll levies "
         "and ONE employee-only solidarity surcharge, and they do NOT share a base. Q1 = Salud (EE 4% + ER "
         "8.5%, IBC, cap 25 SMMLV, ER exonerable). Q2 = Fondo de Solidaridad Pensional (EE only, 1% from 4 "
         "SMMLV plus 0.2-1.0% from 16 SMMLV, IBC). Q3 = Riesgos Laborales / ARL (ER only, 0.348-8.7% by work "
         "centre, IBC). Q4 = Parafiscales CCF 4% + SENA 2% + ICBF 3% on the LEY 21 DE 1982 ART. 17 BASE WITH "
         "NO CEILING. R = Pension (EE 4% + ER 12%, IBC, cap 25 SMMLV, never exonerable). Collapsing Q4 into "
         "the others would silently cap the levies at 25 SMMLV and would drop paid rest days from their base."),
        ("Three Colombia-specific base columns added (S, T, U)",
         "S = the HARD CST art. 127 / 128 salary flag, which the nomina electronica demands at ELEMENT LEVEL "
         "through paired S / NS element names and which must never be derived at reporting time. T = the "
         "statutory-benefit base (prima / cesantias / intereses), which INCLUDES the auxilio de transporte "
         "even though the IBC and the levy base exclude it. U = the vacation base of CST art. 192, which "
         "excludes ONLY rest-day work and supplementary overtime hours, so the night premium and commissions "
         "stay in. Values: Salary / Non-Salary / Paid Rest / Conditional / NA for S; Yes / No / Yes-No / NA "
         "for T and U."),
        ("Column meaning adopted (N, O, P)",
         "N = subject to retencion en la fuente at all. O = subject to the ET art. 383 progressive table "
         "(0 / 19 / 28 / 33 / 35 / 37 / 39% on the art. 388 depurated base). P = SPECIAL TAX is used for the "
         "NON-RESIDENT flat 20% on gross of ET art. 408 - the treatment that produces a 17-fold withholding "
         "difference on the same salary and is the single largest configuration risk in Colombian expatriate "
         "payroll."),
        ("Yes-No entries and their justification",
         "Every Yes-No (rendered 'Yes/No') marks a genuine statutory conditionality, and column D carries the "
         "explanation in every case, as the v2.5 C3 guard requires. The recurring reasons are: (a) the LEY "
         "1393/2010 ART. 30 40% CLAMP, which excludes a validly pacted non-salary payment from the IBC only "
         "up to 40% of total remuneration and forces the excess back in; (b) the ET art. 387-1 meal "
         "thresholds; (c) the ET art. 206 num. 4 cesantias taper; (d) the ET art. 206 par. 1 "
         "statutory-minimum limit on EPS / ARL benefit exemptions; (e) the apprentice's phase-dependent "
         "regime; (f) the CST art. 130 viaticos split; and (g) the conditional character of an anticipo."),
        ("2026 parameters used, and their verification",
         "SMMLV " + SMMLV + " (Decreto 1469 de 2025 art. 1 - VERIFIED in the source PDF, which also records "
         "that the Council of State suspended the decree on 12 February 2026, that Decreto 0159 de 2026 "
         "re-fixed the identical amount, and that the suspension was revoked on 9 July 2026, so the AMOUNT "
         "was never in dispute). UVT " + UVT + " (Resolucion DIAN 000238 de 15-12-2025 art. 1 - VERIFIED in "
         "the source PDF). Auxilio de transporte " + AUX_TTE + " (Decreto 1470 de 2025 art. 1 - the decree "
         "itself is not in 00-official-sources; the figure is carried from CO-CCG-001 and is corroborated by "
         "the exact COP 2,000,000 combined minimum cash entitlement). IBC ceiling 25 SMMLV = " + IBC_CAP + " "
         "and salario integral at 70% (Ley 797 de 2003 art. 5 - VERIFIED verbatim). 40% clamp (Ley 1393 de "
         "2010 art. 30 - VERIFIED verbatim). Levy base including paid rest days (Ley 21 de 1982 art. 17 - "
         "VERIFIED verbatim). Rest-day premium 80% -> 90% on 1 July 2026 (Ley 2466 de 2025 art. 14 - VERIFIED "
         "verbatim). Night window 19:00-06:00 (Ley 2466 art. 10 - VERIFIED verbatim). 42-hour week (Ley 2466 "
         "art. 11 - VERIFIED verbatim). Salary in kind 50% / 30% (CST art. 129 - VERIFIED verbatim). Vacation "
         "base (CST art. 192 - VERIFIED verbatim). Viaticos (CST art. 130 - VERIFIED verbatim). Tips "
         "(CST art. 131 - VERIFIED verbatim). Dotacion every four months (CST arts. 230, 232 - VERIFIED "
         "verbatim). Apprentice 75% / 100% (Ley 2466 art. 21 - VERIFIED verbatim). Connectivity allowance "
         "(Ley 2466 art. 53 - VERIFIED verbatim). Cesantias 8.33% monthly advance (Ley 2466 art. 64 - "
         "VERIFIED verbatim)."),
        ("Newest-law check (control C2)",
         "LEY 2381 DE 2024, the complete replacement of the Colombian pension architecture, is the newest "
         "pension law on the statute book and it does NOT govern any 2026 payroll period. Its own art. 94 set "
         "entry into force at 1 July 2025; Constitutional Court Auto 841 de 18 junio 2025 SUSPENDED that "
         "entry into force; and Judgment C-264 de 25 agosto 2026 upheld art. 94 on the understanding that the "
         "upheld provisions take effect on 1 APRIL 2027. Every 2026 period therefore runs on Ley 100 de 1993 "
         "as amended by Ley 797 de 2003, and NO part of Ley 2381 is configured as live. What changes in 2027: "
         "only the solidarity-fund surcharge, which becomes a single five-band 1.5% / 1.8% / 2.5% / 2.8% / "
         "3.0% scale - the 16% total, the 12 / 4 split and the 25-SMMLV ceiling are unchanged. Recorded as a "
         "2027 change-control item."),
        ("Configuration source",
         "Configured fresh for Colombia from CO-CCG-001 v1.0 Modules 3-10, the 04-reports-spec files, and the "
         "primary law in 00-official-sources/pdfs/ (CST Decreto 2663 de 1950, Ley 100 de 1993, Ley 797 de "
         "2003, Ley 1122 de 2007, Ley 1393 de 2010, Ley 21 de 1982, Ley 89 de 1988, Ley 2101 de 2021, Ley "
         "2381 de 2024, Ley 2466 de 2025, Decreto 1469 de 2025, Decreto 0223 de 2026, Decreto 1990 de 2016, "
         "Decreto Ley 624 de 1989, Decreto Ley 2090 de 2003, Resoluciones DIAN 000227 y 000238 de 2025, "
         "Resolucion 2388 de 2016 y Anexo 2, Circular MinTrabajo 0101 de 2025, Oficio DIAN 13840 de 2025). "
         "NOT copied from Czechia, Cote d'Ivoire or any other country."),
        ("DERIVED flags",
         "(1) The Mercans code numbers for the 102 Colombia-specific rows are DERIVED - no Mercans numeric "
         "code range has been assigned for Colombia, so mnemonic CO- codes are used and must be renumbered at "
         "system configuration. (2) The auxilio de transporte amount is carried from the CCG because Decreto "
         "1470 de 2025 is not in 00-official-sources. (3) The additional high-risk pension rate is read from "
         "the Resolucion 2388 rate table (26% total against 16% standard, implying +10 pp employer-borne), NOT "
         "from the implementing decree - see the open items below."),
        ("Open items carried to the QA report",
         "(1) The rate for the employer's first two sick days - Decreto 780 de 2016 art. 3.2.1.10 allocates "
         "the days but not the rate; Mercans default 66.67%, configurable. (2) The minimum-wage floor on "
         "incapacity payments - primary source not retrieved; Mercans default applies the floor, "
         "configurable. (3) The additional employer pension contribution for Decreto Ley 2090 de 2003 "
         "high-risk activities - the 2026 rate and base not confirmed from a primary regulatory source. "
         "(4) The monthly apportionment of the annual 790-UVT and 1,340-UVT tax caps - no regulation "
         "prescribes it expressly; Mercans applies one twelfth."),
        ("Egypt F20 guards",
         "COMMISSION IS PRESENT as a first-class wage type (CO-COMISIONES) with its own nomina electronica "
         "element, and the global commission-bearing codes are configured, not dropped. EVERY tax code in "
         "column G is drawn from the Colombian legend below (CO-TX-01 to CO-TX-10 and CO-NA) and the "
         "validator rejects any code that does not start with 'CO-'. NO Yes-No appears in a taxability or "
         "subjection column without an explanation in column D."),
    ]
    for ri, (item, detail) in enumerate(cov, start=2):
        gc.cell(ri, 1, ri - 1)
        gc.cell(ri, 2, item).font = Font(bold=True)
        c3 = gc.cell(ri, 3, detail)
        c3.alignment = Alignment(wrap_text=True, vertical="top")

    base = len(cov) + 3
    gc.cell(base, 1, "TAX CODE LEGEND (C9 - every code defined and sourced to a Colombian authority "
                     "publication)").font = Font(bold=True)
    for ci, h in enumerate(["Tax Code", "Meaning", "Official Source"], start=1):
        gc.cell(base + 1, ci, h)._style = copy.copy(blue_hdr)
    for i, (code, (mean, src)) in enumerate(TAX_CODES.items(), start=base + 2):
        gc.cell(i, 1, code).font = Font(bold=True)
        gc.cell(i, 2, mean).alignment = Alignment(wrap_text=True, vertical="top")
        gc.cell(i, 3, src).alignment = Alignment(wrap_text=True, vertical="top")
    gc.column_dimensions["A"].width = 16
    gc.column_dimensions["B"].width = 58
    gc.column_dimensions["C"].width = 96


# ---------------------------------------------------------------------------
def write_form_reference(fr, blue_hdr, form_map):
    for ci, h in enumerate(["Wage Type Category", "Spec File", "Sheet Name", "Row Number", "Notes"], start=1):
        fr.cell(1, ci, h)._style = copy.copy(blue_hdr)
    for ri, vals in enumerate(form_map, start=2):
        for ci, v in enumerate(vals, start=1):
            cell = fr.cell(ri, ci, v)
            cell.alignment = Alignment(wrap_text=True, vertical="top")
    for col, w in zip("ABCDE", (52, 46, 26, 30, 86)):
        fr.column_dimensions[col].width = w
