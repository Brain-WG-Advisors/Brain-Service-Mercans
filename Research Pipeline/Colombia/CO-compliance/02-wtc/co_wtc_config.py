# -*- coding: utf-8 -*-
"""
Colombia (CO) Wage Type Catalogue — configuration module (part 1 of 2)
======================================================================
Tax-code legend (C9), column layout and configuration profiles for
Colombia FY2026. Consumed by build_co_wtc.py.

EVERY value here was configured FRESH for Colombia 2026 from CO-CCG-001
Modules 3-7 and the primary law in 00-official-sources/pdfs/. Nothing is
copied from any other country.

Verified against primary law this pass:
  * SMMLV 2026 = COP 1,750,905          Decreto 1469 de 2025 art. 1 (PDF, p.94/102)
  * UVT 2026   = COP 52,374             Resolucion DIAN 000238 de 15-12-2025 art. 1
  * IBC ceiling 25 SMMLV / integral 70% Ley 797 de 2003 art. 5 (Ley 100 art. 18)
  * 40% non-salary clamp                Ley 1393 de 2010 art. 30 (arts. 18 y 204 Ley 100)
  * Payroll-levy base incl. paid rest   Ley 21 de 1982 art. 17
  * Rest-day premium 80% -> 90% 1 Jul   Ley 2466 de 2025 art. 14 (CST art. 179)
  * Night window 19:00-06:00            Ley 2466 de 2025 art. 10 (CST art. 160)
  * 42-hour week                        Ley 2466 de 2025 art. 11 (CST art. 161)
  * Salary in kind 50% / 30% caps       CST art. 129
  * Vacation base excludes OT + rest-day CST art. 192
  * Dotacion every 4 months, <= 2 SMMLV CST arts. 230, 232
  * Viaticos permanentes = salary part  CST art. 130
  * Tips are never salary               CST art. 131
  * Apprentice support 75% / 100%       Ley 2466 de 2025 art. 21 (CST art. 81)
  * Connectivity allowance < 2 SMMLV    Ley 2466 de 2025 art. 53 (Ley 1221 art. 6A)
  * Cesantias 8.33% monthly advance     Ley 2466 de 2025 art. 64 (Ley 50/1990 art. 99)
"""

# ---------------------------------------------------------------------------
# 2026 REFERENCE VALUES (COP)
# ---------------------------------------------------------------------------
SMMLV      = "1,750,905"       # Decreto 1469 de 2025 art. 1
UVT        = "52,374"          # Resolucion DIAN 000238 de 15-12-2025
AUX_TTE    = "249,095"         # Decreto 1470 de 2025 art. 1
IBC_CAP    = "43,772,625"      # 25 x SMMLV
FSP_TRIG   = "7,003,620"       # 4 x SMMLV
EXON_CUT   = "17,509,050"      # 10 x SMMLV (ET art. 114-1)
INTEGRAL   = "22,761,765"      # 13 x SMMLV
AUX_CAP    = "3,501,810"       # 2 x SMMLV
SUB_TRIG   = "28,014,480"      # 16 x SMMLV
MEAL_CAP   = "2,147,334"       # 41 UVT  (ET art. 387-1)
MEAL_SAL   = "16,235,940"      # 310 UVT (ET art. 387-1)
EX25_CAP   = "3,447,955"       # 790 UVT / 12 (ET art. 206 num. 10)
CAP1340    = "5,848,430"       # 1,340 UVT / 12 (Decreto 2231 de 2023 art. 9)
CESA_EXEMPT = "18,330,900"     # 350 UVT (ET art. 206 num. 4)
DIVISOR    = "220 to 14 Jul 2026 / 210 from 15 Jul 2026"

# ---------------------------------------------------------------------------
# TAX CODE LEGEND (C9 - every code defined and sourced to a Colombian authority
# publication: DIAN, MinTrabajo, MinSalud or the statute itself. No code is
# guessed and none is borrowed from another country's legend.)
# ---------------------------------------------------------------------------
TAX_CODES = {
    "CO-TX-01": (
        "Ordinary taxable work income - RESIDENT. Enters the total taxable payments of the month, "
        "is depurated under ET art. 388 (non-taxable income, art. 387 deductions, exempt income, the "
        "40% cap and the 1,340-UVT annual cap) and is withheld on the ET art. 383 progressive table "
        "(0/19/28/33/35/37/39%) under Procedure 1 (art. 385) or at the fixed percentage under "
        "Procedure 2 (art. 386). No preferential rate and no tax-free allowance exists for any "
        "individual earning type.",
        "Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 "
        "art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by "
        "Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT " + UVT + ")."),
    "CO-TX-02": (
        "Severance savings and the interest on them (cesantias e intereses). EXCLUDED from the monthly "
        "withholding base under BOTH procedures - they never enter the monthly table read. Exempt IN FULL "
        "where the average monthly income of the last 6 months is <= 350 UVT (" + CESA_EXEMPT + "); above "
        "that the untaxed portion tapers 90/80/60/40/20/0% through 650 UVT. The 25% exemption of art. 206 "
        "num. 10 does NOT apply to them (art. 206 par. 2).",
        "ET arts. 206 num. 4 and par. 2, 385, 386; Ley 50 de 1990 art. 99; Ley 52 de 1975 art. 1; "
        "Ley 2466 de 2025 art. 64 (8.33% monthly advance deposit)."),
    "CO-TX-03": (
        "Statutory minimum service bonus (prima de servicios legal). Under Procedure 1 it is withheld "
        "SEPARATELY, on its own read of the ET art. 383 table, and is NOT added to the month's salary. "
        "Under Procedure 2 it is folded into the ordinary monthly base (the 13 divisor of art. 386 already "
        "prorates its effect). Any excess above the statutory minimum bonus goes to the ordinary monthly base.",
        "ET arts. 385 and 386; CST arts. 306 (as amended by Ley 1788 de 2016 art. 1), 307 and 308."),
    "CO-TX-04": (
        "Non-taxable income - ingreso no constitutivo de renta ni ganancia ocasional. Subtracted at step "
        "(B) of the ET art. 388 depuration, i.e. BEFORE the 40% cap reference figure is struck, which makes "
        "it more valuable than exempt income. Covers the employee mandatory pension 4%, the solidarity "
        "pension fund 1% + 0.2-1.0%, the mandatory health 4%, and voluntary contributions to the individual "
        "pension account within 25% of annual labour income / 2,500 UVT.",
        "ET arts. 55 and 56; ET art. 388 num. 1; Formato 2276 v4 numerals N23 and N24 (which group the "
        "pension and solidarity-fund contributions on a single line)."),
    "CO-TX-05": (
        "Conditionally not income - third-party meal payments (pagos de alimentacion a terceros). NOT income "
        "to the employee where BOTH conditions hold: the employee's salary does not exceed 310 UVT "
        "(" + MEAL_SAL + ") AND the payment is made to a THIRD PARTY. Where the month's payments exceed "
        "41 UVT (" + MEAL_CAP + ") the EXCESS is taxable employment income. Cash paid to the employee for "
        "food is salary and gets none of this treatment.",
        "ET art. 387-1; Formato 2276 v4 numerals N08 (excess) and N32 (within-limit amount), which report "
        "the two portions separately; Formulario 220 casillas 37 and 38."),
    "CO-TX-06": (
        "Not income and not remuneration - amounts given not to enrich the employee but to enable the work: "
        "statutory work clothing (dotacion), work tools, protective equipment, means of transport, "
        "representation expenses, occasional viaticos for transport, and genuine documented "
        "business-expense reimbursement. Outside EVERY base - tax, contribution, payroll-levy, "
        "statutory-benefit and vacation.",
        "CST arts. 128 and 230 (art. 230 as modified by Ley 11 de 1984 art. 7); CST arts. 130 and 232; "
        "ET art. 387-1 final paragraph (representation expenses expressly outside the meal rule)."),
    "CO-TX-07": (
        "Exempt income LIMITED TO THE STATUTORY MINIMUM AMOUNT - accident and illness indemnities, "
        "maternity-protection indemnities and employee burial expenses, and by extension the sickness, "
        "maternity, paternity and occupational-injury cash benefits paid by the EPS or the ARL. ET art. 206 "
        "par. 1 is explicit that the exemption 'operates only on the amounts corresponding to the statutory "
        "minimum' and that the excess is not exempt.",
        "ET art. 206 nums. 1, 2, 3 and par. 1; CST arts. 227, 236; Decreto 780 de 2016 art. 3.2.1.10 "
        "(Decreto 2943 de 2013 art. 1, employer days 1-2)."),
    "CO-TX-08": (
        "NON-RESIDENT flat withholding - 20% ON THE GROSS PAYMENT, with NO art. 388 depuration, NO 25% "
        "exempt income, NO art. 387 deductions and NO tax-free band, for Colombian-source work income. "
        "Determined at the moment of EACH payment on the status then held; the switch to the art. 383 table "
        "is PROSPECTIVE from the payment following the 183rd day, never retroactive. Where the service is "
        "performed entirely outside Colombia the income is foreign-source and there is NO withholding.",
        "ET arts. 10, 408-415; DIAN Concepto 011108 de 29 junio 2026 (upholding Concepto 1789 int. 14595 "
        "de 2025); DIAN Oficio 28380 de 2019; Formulario 350 casillas 109-112 and hoja 2 casillas 141-155."),
    "CO-TX-09": (
        "Exempt income - renta exenta - for voluntary pension fund contributions (art. 126-1) and "
        "construction-savings / long-term-savings account contributions (arts. 126-4 AFC/AVC), employee or "
        "employer-paid on the employee's behalf. Subtracted at step (E) INSIDE the 40% and 1,340-UVT caps, "
        "within a single shared annual limit of the lower of 30% of labour income or 3,800 UVT "
        "(COP 199,021,200 for 2026).",
        "ET arts. 126-1 and 126-4; ET art. 388 num. 2; Formulario 220 casillas 56, 57 and 58; "
        "Formato 2276 v4 numerals N26, N27 and N28."),
    "CO-TX-10": (
        "Pension income and refunds of pension savings. A retirement, invalidity, old-age, survivor or "
        "occupational-risk pension is taxable only on the monthly amount exceeding 1,000 UVT "
        "(COP 52,374,000). The 40% limit of art. 388 expressly does not apply to pension payments, pension "
        "substitution indemnities or refunds of pension savings. Paid by the pension administrator, so OUT "
        "OF SCOPE of employer gross-to-net per scope_manifest; retained for completeness and for Formulario "
        "220 casilla 50 / Formato 2276 numeral N21.",
        "ET arts. 206 num. 5 and par. 3, 383 (first paragraph, which brings pensions into the same table), "
        "388 final sentence; Formulario 220 casilla 50; Formato 2276 v4 numeral N21."),
    "CO-NA": (
        "Not a remuneration line - an employee deduction, an employer contribution or accrual, a "
        "calculation base, an intermediary, a notional, a rate or a configuration flag. Every taxability "
        "and subjection column is NA because the row is a mechanism, not a payment to the employee.",
        "N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina "
        "electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record "
        "(Resolucion MSPS 2388 de 2016 Anexo Tecnico 2)."),
}

# ---------------------------------------------------------------------------
# COLUMN LAYOUT
#   colour: 'B' = blue (CZ theme8 header), 'O' = orange (FFFF9900)
#
#   Column meaning adopted for Colombia (documented on the Coverage sheet):
#     N  SubjTax   = subject to retencion en la fuente at all
#     O  TableTax  = subject to the ET art. 383 progressive table (Proc. 1 / 2)
#     P  SpecialTax= subject to the NON-RESIDENT flat 20% of ET art. 408
#     Q1 Salud     = health, IBC, cap 25 SMMLV, EE 4% + ER 8.5% (ER exonerable)
#     Q2 FSP       = solidarity pension fund, IBC, EE-only, trigger 4 SMMLV
#     Q3 ARL       = occupational risk, IBC, ER-only 0.348-8.7%
#     Q4 Parafisc. = CCF 4% / SENA 2% / ICBF 3% on the Ley 21/1982 levy base, NO ceiling
#     R  Pension   = pension, IBC, cap 25 SMMLV, EE 4% + ER 12% (never exonerable)
#     S  Salary?   = the hard CST art. 127/128 salary flag the nomina electronica
#                    demands at element level (paired S / NS element names)
#     T  BenefBase = enters the prima / cesantias / intereses base
#     U  VacBase   = enters the vacation base (CST art. 192)
# ---------------------------------------------------------------------------
COLUMNS = [
    ("Mercans Code", "O"),                                                              # 1  A
    ("Wage Type Name in English", "B"),                                                 # 2  B
    ("Wage Type Name in Local Language (Spanish)", "B"),                                # 3  C
    ("Wage Type Explanation", "O"),                                                     # 4  D
    ("Category", "B"),                                                                  # 5  E
    ("Formula", "B"),                                                                   # 6  F
    ("Tax Code", "B"),                                                                  # 7  G
    ("Calculation Type", "O"),                                                          # 8  H
    ("Prorating Method", "O"),                                                          # 9  I
    ("Occurrence", "B"),                                                                # 10 J
    ("Ignore If 0", "O"),                                                               # 11 K
    ("Enforce Setting", "O"),                                                           # 12 L
    ("In Period Reconciliation", "O"),                                                  # 13 M
    ("Subject to Tax (Retencion en la Fuente)", "B"),                                   # 14 N
    ("Table Tax (ET art. 383 progressive table 0/19/28/33/35/37/39%)", "B"),            # 15 O
    ("Special Tax (Non-resident flat 20% on gross, ET art. 408)", "B"),                 # 16 P
    ("Subject to Health - Salud EPS (EE 4% + ER 8.5%; IBC, cap 25 SMMLV " + IBC_CAP + ")", "B"),   # 17 Q1
    ("Subject to Solidarity Pension Fund - FSP (EE 1% + 0.2-1.0%; IBC >= 4 SMMLV " + FSP_TRIG + ")", "B"),  # 18 Q2
    ("Subject to Occupational Risk - ARL (ER only 0.348-8.7%; IBC)", "B"),              # 19 Q3
    ("Subject to Payroll Levies - CCF 4% / SENA 2% / ICBF 3% (Ley 21/1982 base, NO ceiling)", "B"),  # 20 Q4
    ("Subject to Pension - Pension Obligatoria (EE 4% + ER 12%; IBC, cap 25 SMMLV)", "B"),          # 21 R
    ("Salary or Non-Salary (CST arts. 127 / 128) - hard flag for the nomina electronica S / NS elements", "B"),  # 22 S
    ("Statutory-Benefit Base (prima de servicios / cesantias / intereses)", "B"),       # 23 T
    ("Vacation Base (CST art. 192 - excludes overtime and rest-day work only)", "B"),   # 24 U
    ("Nomina Electronica Element (Res. DIAN 000013 de 2021, Anexo Tecnico v1.0)", "B"), # 25 V
    ("Tax Code Source (C9 - official reference)", "B"),                                 # 26 W
    ("YTD Load (Yes/ No)", "O"),                                                        # 27 X
    ("YTD Remarks", "O"),                                                               # 28 Y
]
NCOL = len(COLUMNS)  # 28

COL_WIDTHS = {1: 26, 2: 44, 3: 46, 4: 74, 5: 20, 6: 62, 7: 11, 8: 14, 9: 14, 10: 12,
              11: 10, 12: 16, 13: 18, 14: 14, 15: 20, 16: 18, 17: 22, 18: 22, 19: 20,
              20: 22, 21: 22, 22: 18, 23: 18, 24: 16, 25: 30, 26: 62, 27: 11, 28: 34}

# taxability / subjection columns (1-based) = N O P Q1 Q2 Q3 Q4 R = 14..21
TAX_SS_COLS_1B = list(range(14, 22))
# the three Colombia-specific base columns (1-based) = S T U = 22..24
BASE_COLS_1B = [22, 23, 24]

# ---------------------------------------------------------------------------
# VALUE VOCABULARY
# ---------------------------------------------------------------------------
Y, N, NA, YN = "Yes", "No", "NA", "Yes/No"
SAL, NSAL, REST, COND = "Salary", "Non-Salary", "Paid Rest", "Conditional"


def prof(cat, tc, occ, n, o, p, q1, q2, q3, q4, r, s, t, u):
    return dict(cat=cat, tc=tc, occ=occ, N=n, O=o, P=p,
                Q1=q1, Q2=q2, Q3=q3, Q4=q4, R=r, S=s, T=t, U=u)


# --- EARNINGS -------------------------------------------------------------
# Ordinary salary-constituting cash pay: taxable, in every base.
P_SAL      = prof("Earning", "CO-TX-01", "Recurring",  Y, Y, Y, Y, Y, Y, Y, Y, SAL,  Y, Y)
P_SAL_ADD  = prof("Earning", "CO-TX-01", "Additional", Y, Y, Y, Y, Y, Y, Y, Y, SAL,  Y, Y)
# All-inclusive salary: IBC and levy base both 70%; benefits absorbed EXCEPT vacation,
# which is owed on the FULL 100%.
P_SALINT   = prof("Earning", "CO-TX-01", "Recurring",  Y, Y, Y, Y, Y, Y, Y, Y, SAL,  N, Y)
# Overtime and rest-day work: salary, fully contributory, but OUT of the vacation base.
P_OT       = prof("Earning", "CO-TX-01", "Additional", Y, Y, Y, Y, Y, Y, Y, Y, SAL,  Y, N)
# Night premium: salary, fully contributory, and IN the vacation base (art. 192 excludes
# only rest-day work and supplementary overtime hours).
P_NIGHT    = prof("Earning", "CO-TX-01", "Additional", Y, Y, Y, Y, Y, Y, Y, Y, SAL,  Y, Y)
# Commissions and sales percentages: salary, in the vacation base.
P_COMM     = prof("Earning", "CO-TX-01", "Recurring",  Y, Y, Y, Y, Y, Y, Y, Y, SAL,  Y, Y)
# Statutory transport / connectivity allowance: NOT salary, OUT of the IBC and the levy
# base, but IN the statutory-benefit base, and taxable income.
P_TRANSP   = prof("Earning", "CO-TX-01", "Recurring",  Y, Y, Y, N, N, N, N, N, NSAL, Y, N)
# Valid written CST art. 128 non-salary pact: no tax effect at all; out of the IBC ONLY up
# to the Ley 1393/2010 art. 30 40% clamp, and the clamp never reaches the payroll levies.
P_NONSAL   = prof("Earning", "CO-TX-01", "Recurring",  Y, Y, Y, YN, YN, YN, N, YN, NSAL, N, N)
P_NONSAL_A = prof("Earning", "CO-TX-01", "Additional", Y, Y, Y, YN, YN, YN, N, YN, NSAL, N, N)
# Occasional, purely gratuitous sums and profit participation (art. 128 nums. 1-2).
P_GRATUITY = prof("Earning", "CO-TX-01", "Additional", Y, Y, Y, YN, YN, YN, N, YN, NSAL, N, N)
# Salary in kind (CST art. 129): salary, every base, capped 50% / 30% at the SMMLV.
P_BIK_SAL  = prof("Earning", "CO-TX-01", "Recurring",  Y, Y, Y, Y, Y, Y, Y, Y, SAL,  Y, Y)
# Statutory service bonus: separate table read under Procedure 1; out of every SS base.
P_PRIMA    = prof("Earning", "CO-TX-03", "Additional", Y, Y, Y, N, N, N, N, N, NSAL, NA, NA)
# Severance savings and interest: excluded from the monthly base; art. 206 num. 4 taper.
P_CESANT   = prof("Earning", "CO-TX-02", "Additional", YN, N, Y, N, N, N, N, N, NSAL, NA, NA)
# Vacation and cash-compensated vacation: PAID REST, so IN the IBC and IN the levy base.
P_VAC      = prof("Earning", "CO-TX-01", "Additional", Y, Y, Y, Y, Y, Y, Y, Y, REST, Y, NA)
# Other paid statutory leave (CST art. 57 num. 6, luto): paid rest, fully contributory.
P_LEAVE_P  = prof("Earning", "CO-TX-01", "Additional", Y, Y, Y, Y, Y, Y, Y, Y, REST, Y, Y)
# Work clothing, tools, protective equipment, reimbursements, occasional viaticos.
P_NOTINC   = prof("Earning", "CO-TX-06", "Additional", N, N, N, N, N, N, N, N, NSAL, N, N)
# Third-party meal payments (ET art. 387-1) - conditional on two thresholds.
P_MEAL3P   = prof("Earning", "CO-TX-05", "Recurring",  YN, YN, YN, N, N, N, N, N, NSAL, N, N)
# Employer sickness days 1-2: not salary, but IN the IBC, the levy base and the benefit base.
P_INCAP_ER = prof("Earning", "CO-TX-01", "Additional", Y, Y, Y, Y, Y, Y, Y, Y, NSAL, Y, N)
# EPS / ARL cash benefits advanced through payroll: exempt within the statutory minimum;
# contributions CONTINUE on the base, but the payments are out of the levy base.
P_INCAP_EPS = prof("Earning", "CO-TX-07", "Additional", YN, YN, Y, Y, Y, Y, N, Y, NSAL, N, N)
# Termination indemnities and penalties: fully taxable, out of every SS base.
P_INDEM    = prof("Earning", "CO-TX-01", "Additional", Y, Y, Y, N, N, N, N, N, NSAL, N, N)
# Apprentice maintenance support: special regime, IBC floored at 1 SMMLV; the classroom
# phase carries health and occupational risk only.
P_APRENDIZ = prof("Earning", "CO-TX-01", "Recurring",  Y, Y, Y, Y, YN, Y, YN, YN, COND, YN, YN)
# Viaticos permanentes - the manutencion / alojamiento part only (CST art. 130).
P_VIATICO  = prof("Earning", "CO-TX-01", "Additional", Y, Y, Y, YN, YN, YN, YN, YN, COND, YN, YN)
# Employer contribution to a voluntary pension fund / AFC / AVC: exempt income.
P_VOLPEN   = prof("Earning", "CO-TX-09", "Recurring",  YN, YN, N, YN, YN, YN, N, YN, NSAL, N, N)
# Employer voluntary contribution to the employee's individual pension account.
P_RAISVOL  = prof("Earning", "CO-TX-04", "Recurring",  N, N, N, YN, YN, YN, N, YN, NSAL, N, N)
# Equity and share-incentive awards: taxable at exercise or vesting on the spread.
P_EQUITY   = prof("Earning", "CO-TX-01", "Additional", Y, Y, Y, YN, YN, YN, N, YN, NSAL, N, N)
# Pension paid by the administrator / refund of pension savings - OUT OF SCOPE, retained.
P_PENSION  = prof("Earning", "CO-TX-10", "Additional", YN, YN, Y, NA, NA, NA, NA, NA, NSAL, NA, NA)
# Unpaid leave / legal strike: a negative or zero line driving the SLN novedad.
P_UNPAID   = prof("Earning", "CO-NA",    "Additional", NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA)
# Advance of pay - conditional: an advance OF salary is salary; a recoverable advance is not.
P_ANTICIPO = prof("Earning", "CO-TX-01", "Additional", YN, YN, YN, YN, YN, YN, YN, YN, COND, YN, YN)

# --- MECHANISM ROWS -------------------------------------------------------
P_DED      = prof("Deduction",             "CO-NA", "Recurring",  NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA)
P_DED_ADD  = prof("Deduction",             "CO-NA", "Additional", NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA)
P_TAX      = prof("Tax",                   "CO-NA", "Recurring",  NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA)
P_ERC      = prof("Employer Contribution", "CO-NA", "Recurring",  NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA)
P_BASE     = prof("Base",                  "CO-NA", "NA",         NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA)
P_INT      = prof("Intermediary",          "CO-NA", "NA",         NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA)
P_FLAG     = prof("Flag",                  "CO-NA", "NA",         NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA)
P_RATE     = prof("Percentage",            "CO-NA", "NA",         NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA)
P_NOTIONAL = prof("Notional",              "CO-NA", "NA",         NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA)
