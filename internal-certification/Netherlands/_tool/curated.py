"""Reviewed findings per client (written after reading every exception in
_evidence/checks.json against the source documents). The automated checks are
the evidence; this file is the register."""

COMMON_ASSUMPTIONS = [
    ("A1", "The loonaangifte XML in the pack is the message that was submitted. "
           "For Quest and Excerpta no Digipoort response was supplied; for Sherwin "
           "the response supplied belongs to another loonheffingennummer (see "
           "findings)."),
    ("A2", "Systematiek: loon-over, confirmed by Wallisson Gomes on 14-10-2026 for "
           "this certification. Basis: HRBLIZZ files corrections for earlier 2026 "
           "periods together with the current return (Handboek Loonheffingen 2026 "
           "§9.2.1, condition 3). The carve-out in §9.2.1 (payments relating to 2025 "
           "or earlier are always loon-in) does not apply: every correction block in "
           "these packs is a 2026 period. Bestendige gedragslijn not evidenced in the "
           "pack; to be confirmed with the client."),
    ("A3", "Statutory parameters 2026 from Handboek Loonheffingen 2026 (versie maart "
           "2026), Bijlage 1: Aof laag 6,27%, Aof hoog 7,63%, AWf laag 2,74%, AWf hoog "
           "7,74%, Opslag Wko 0,50%, Ufo 0,68%, werkgeversheffing Zvw 6,10%, bijdrage "
           "Zvw 4,85%, maximumpremieloon EUR 79.409 per year / EUR 6.617,41 per month, "
           "AOW age 67 (2024-2027)."),
    ("A4", "Withholding recalculated with the official Witte Maandloon-tabel 2026 and "
           "the witte/groene tabel bijzondere beloningen 2026 (all 'uitgave januari "
           "2026'; no later edition published - checked on download.belastingdienst.nl "
           "14-10-2026). Tables read cell by cell with word positions; above the last "
           "tabelloon (11.092,50) the table footer rule applies (49,50% of the excess, "
           "rounded in the employee's favour). AOW column from the 1st day of the month "
           "in which the AOW age is reached (Handboek 2026 §9.3.3)."),
    ("A5", "Bijzondere beloningen: the rate is derived by the engine from 'Jaarloon "
           "BT'. Tested: (1) the applied rate is a rate of the applicable column "
           "(column membership) and (2) where the payslip prints Jaarloon BT, the rate "
           "is the bracket rate for that jaarloon. The derivation of Jaarloon BT itself "
           "is not tested (it needs the prior-year wage)."),
    ("A6", "Payslips are compared by presence: every amount of the return/G2N that "
           "must appear (net pay, tabelloon, table tax, bb wage, bb tax) is searched on "
           "that employee's payslip pages; header fields are read where the PDF text "
           "layer allows it. Fields that could not be read reliably are listed under "
           "Not Tested, never as Pass."),
    ("A7", "Whk (gedifferentieerde premie) is set per employer by beschikking, which "
           "is not in the pack. The rate is inferred from the return and tested for "
           "consistency only. No L-code exists for a nil Whk premium."),
    ("A8", "Zvw: the Zvw and SV maxima are equal in 2026 (Tabel 11). Werkgeversheffing "
           "Zvw is tested as 6,10% of the capped premium wage declared for Whk; "
           "differences are investigated per employee (AOW-age employees have no Whk "
           "base but still owe Zvw)."),
    ("A9", "Severity: High = wrong amount withheld or declared, or no evidence that "
           "the return was accepted; Medium = a filed-return field or a client-facing "
           "document is wrong without moving money this period; Low = presentation or "
           "rounding (<= EUR 0,10); Observation = needs the client's confirmation "
           "before it can be classified."),
]

SOURCES = [
    ("Belastingdienst", "Handboek Loonheffingen 2026", "belastingdienst.nl > brochures "
     "en publicaties > Handboek Loonheffingen", "Versie maart 2026 (latest published "
     "on 14-10-2026)", "Rates (Bijlage 1 Tabel 9, 11, 12), AOW column rule §9.3.3, "
     "loon-over §9.2.1, verloonde uren §29.9"),
    ("Belastingdienst", "Gegevensspecificaties aangifte loonheffingen 2026",
     "belastingdienst.nl > Gegevensspecificaties aangifte loonheffingen",
     "Versie 3.1, 1 juli 2026", "Rubrieken, poortcontroles 0039-0041, 1713, 2024, "
     "2303, 2501"),
    ("Belastingdienst", "Codes voor de aangifte loonheffingen 2026", "belastingdienst.nl",
     "2026", "Code loonbelastingtabel, reden einde arbeidsverhouding"),
    ("Belastingdienst", "Aangifte loonheffingen 2026: tijdvakcodes, aangifte- en "
     "betaaldatums", "belastingdienst.nl", "2026", "Tijdvakcode 6090, deadline "
     "31-10-2026"),
    ("Belastingdienst", "Witte Maandloon-tabel loonbelasting/premie "
     "volksverzekeringen, Nederland, Standaard", "download.belastingdienst.nl/"
     "belastingdienst/dl/rekenhulpen/loonheffing/2026/v01/pdf/wit_mnd_nl_std_20260101.pdf",
     "Uitgave januari 2026; downloaded 14-10-2026", "Regular withholding and "
     "verrekende arbeidskorting"),
    ("Belastingdienst", "Witte tabel bijzondere beloning, Nederland, Standaard",
     ".../2026/v01/pdf/wit_bb_nl_std_20260101.pdf", "Uitgave januari 2026; "
     "downloaded 14-10-2026", "Special-rate column membership and brackets"),
    ("Belastingdienst", "Groene tabel bijzondere beloning, Nederland, Standaard",
     ".../2026/v01/pdf/groen_bb_nl_std_20260101.pdf", "Uitgave januari 2026; "
     "downloaded 14-10-2026", "Ontslag-/transitievergoeding (SrtIV 62, LbTab 020)"),
    ("ISO 20022", "pain.001.001.03 CustomerCreditTransferInitiation", "iso20022.org",
     "v03", "Amount format, NbOfTxs/CtrlSum, EndToEndId"),
]

CLIENTS = {
 "quest": {
  "file": "NL_Quest_2026-09_Validation.xlsx",
  "cover": [
   ("Client", "Quest Software B.V. (pay group NLD_QUEST)"),
   ("Loonheffingennummer", "809615253L01"),
   ("Period", "September 2026 (tijdvak 2026-09-01 to 2026-09-30, tijdvakcode 6090)"),
   ("Return", "809615253L01.09.2026.xml - namespace Loonaangifte/2026/01, version 2.0, "
              "created 2026-09-25 11:39; 5 income relations (4 employees), no correction blocks"),
   ("Received from", "Athul Satheesh (Primary SBC), Google Chat, 09-10-2026 10:02 - "
                     "Quest Software_Netherlands.zip (8 files)"),
   ("Documents checked", "Return XML; Gross To Net (.xls); payslips (4); Deutsche Bank "
                         "SEPA file; 'Kantar' SEPA file; GL report; master data (3 "
                         "employees); HRBLIZZ Wage Tax Overview"),
   ("Product", "HRBLIZZ (Mercans)"),
   ("Prepared", "Compliance team (Wallisson Gomes), 14-10-2026"),
  ],
  "summary": [
   ("Overall conclusion", "Qualified. Within what could be tested, the September 2026 "
    "return is arithmetically and statutorily correct: every withholding matches the "
    "official 2026 monthly table to the cent, every special rate is a valid table rate "
    "and matches the payslip's Jaarloon BT bracket, every employer premium recalculates "
    "at the 2026 rates, and return, G2N, payslips, Deutsche Bank SEPA file and GL tie "
    "per employee and in total. Acceptance by the Belastingdienst is not evidenced."),
   ("Most important", "F-01: verloonde uren declared as working days x 8 (176) instead "
    "of the average monthly hours for a fixed monthly wage (173). F-03: the second bank "
    "file ('Kantar') has invalid amounts and a repeated EndToEndId - confirm it was not "
    "sent."),
   ("Calculation results", "Regular withholding 4/4 white-table IKVs exact; special "
    "rate 3/3 + 1 green-table severance valid; premiums 5/5 IKVs exact; net pay "
    "48.884,10 = SEPA (Deutsche Bank) = GL; loonheffingen 52.395 = TotTeBet = GL."),
  ],
  "findings": [
   ("F-01", "Medium", "Return - verloonde uren",
    "The return declares 176 verloonde uren (22 working days x 8) for the three "
    "employees on a fixed monthly salary; their payslips print 173,33. For a fixed "
    "monthly wage the Handboek requires the average hours per period (here 40 x 52 / 12 "
    "= 173,33, rounded to 173), not the working days of the month.",
    "70030, 76628, 89826: AantVerlU 176; payslip 'Verloonde uren 173.33'; contract "
    "40,00 h/week; the same base salary is paid every month.",
    "No tax or premium effect. The field feeds UWV (WW/WIA daily wage and duration), "
    "the AWf herziening test and CBS.",
    "Handboek Loonheffingen 2026 §29.9 ('Verloonde uren per tijdvak', situation 2 - "
    "gemiddeld maandloon); Gegevensspecificaties 2026, rubriek Aantal verloonde uren.",
    "Open", 3),
   ("F-02", "Low", "Payslip - verloonde uren",
    "The leaver's final payslip prints 173,33 verloonde uren although no salary was "
    "paid for September; the return correctly declares 0.",
    "96083 (end 31-08-2026): payslip 173.33, return IKV 0001 AantVerlU 0.", "Presentation only.",
    "Handboek 2026 §29.9 (hours for which wage is paid).", "Open", 1),
   ("F-03", "Medium", "Bank file",
    "The second SEPA file in the pack is not valid ISO 20022: InstdAmt and CtrlSum use a "
    "thousands separator ('4,960.60', '48,884.10'), all four transfers carry the same "
    "EndToEndId, and the file is named after another client (Kantar). The Deutsche Bank "
    "file is valid and ties exactly to the G2N.",
    "'Kantar Netherlands Bank XML File 2026-09-01 - 2026-09-30.xml', MsgId "
    "2026090114030, EndToEndId KNSAL202609T11 x4. Deutsche Bank file: 4 transfers, "
    "CtrlSum 48884.10 = G2N net.",
    "If this file reached the bank it would be rejected. Confirm which file was "
    "transmitted.", "ISO 20022 pain.001.001.03 (decimal amount, '.' separator; "
    "EndToEndId identifies each transaction).", "Open", 4),
   ("F-04", "Low", "GL - labels",
    "GL pay-element labels for Dutch employer premiums carry other countries' scheme "
    "names: '6064 - EOBI (employer)' for werkgeversheffing Zvw, '6068 - EIS (employer)' "
    "for AWf, '6061/6062 - Social Fund (employer)' for Aof/Wko, '6040 - Work injury' for "
    "WGA. Amounts and accounts reconcile.",
    "Standard gl-report 2026-09, expense lines on account 6040000.",
    "Presentation; misleading for the client's finance team.", "-", "Open", 4),
   ("F-05", "Low", "Wage Tax Overview",
    "The HRBLIZZ 'Wage Tax Overview' prints 'Uiterste aangifte-/betaaldatum 2026-10-30'. "
    "The official deadline for tijdvakcode 6090 is 31-10-2026. The document is a "
    "system summary, not the authority's receipt.",
    "Quest Software B.V..Wage Tax Overview.09.2026 (1).pdf (created 2026-09-16).",
    "None (earlier date).", "Aangifte loonheffingen 2026: tijdvakcodes, aangifte- en "
    "betaaldatums.", "Open", 1),
   ("F-06", "Observation", "Return - arbeidskorting",
    "On the leaver's IKV the tabelloon is 30,79 (a pension refund; the holiday payout "
    "is taxed at the special rate). The table gives verrekende arbeidskorting 0,00; the "
    "return declares 2,25 (G2N 58104 = 2,25). Regular tax 0,00 is correct.",
    "96083 IKV 0001: LnLbPh 13.580,14, LnTabBB 13.549,35, VerrArbKrt 2.25.",
    "No tax effect; a filed-return rubriek. Dev to explain the derivation.",
    "Witte Maandloon-tabel 2026, column verrekende arbeidskorting.", "Open", 1),
   ("F-07", "Observation", "G2N - vacation purchase",
    "Vacation purchase (21216) is deducted from net pay and does not reduce the fiscal "
    "or SV wage. If the scheme is a salary exchange agreed in the employment terms, the "
    "gross wage would be reduced instead. Configuration/contract question; no statutory "
    "error asserted.", "76628 158,61; 96083 744,53 (total 903,14).",
    "Not quantified.", "-", "Open", 2),
  ],
  "overrides": {
   "H-01 / H-02": ("Finding", "See F-01."),
   "H-03": ("Pass", "Reviewed: both zero-hour IKVs are correct - 96083/0001 (no salary "
                     "in September) and 96083/0002 (SrtIV 62 must be 0, poortcontrole 1713)."),
   "D-08": ("Finding", "See F-06."),
   "M-04": ("Pass", "Reviewed: the only employee missing from the master extract is the "
                    "leaver 96083 (extract of active employees)."),
   "G-02 / H-01 / D-11": ("Finding", "See F-01 / F-02."),
   "K-01": ("Finding", "See F-03."),
   "K-07": ("Finding", "See F-04."),
  },
  "not_tested": [
   ("NT-01", "Acceptance of the return by the Belastingdienst",
    "No Digipoort status response or ontvangstbevestiging in the pack; the 'Wage Tax "
    "Overview' is generated by HRBLIZZ.", "Digipoort status response for "
    "809615253L01P20260901 or a screenshot of the Belastingdienst portal."),
   ("NT-02", "Whk rate against the beschikking", "Beschikking not in the pack; implied "
    "rate 1,45% consistent on all 4 IKVs.", "Whk beschikking 2026."),
   ("NT-03", "Payslip cumulative roll-forward (J-02)", "Only September payslips.",
    "August 2026 payslips or a year-to-date G2N."),
   ("NT-04", "Tax and SV base composition per wage type (G-S5)", "No client wage-type "
    "catalogue with LB/SV flags. Spot-checked: fiscal wage = gross - pension - WKR "
    "allowances (54 + 100) for 70030 and 76628.", "Client wage-type catalogue export."),
   ("NT-05", "Jaarloon BT derivation", "Needs the prior-year wage.",
    "Jaarloon BT build-up per employee."),
  ],
 },
 "excerpta": {
  "file": "NL_Excerpta_2026-09_Validation.xlsx",
  "cover": [
   ("Client", "Excerpta Medica B.V. (Omnicom NL; pay group NLEXCMED)"),
   ("Loonheffingennummer", "822945526L01"),
   ("Period", "September 2026 (tijdvak 2026-09-01 to 2026-09-30, tijdvakcode 6090)"),
   ("Return", "822945526L01.09.2026.xml - namespace Loonaangifte/2026/01, version 2.0, "
              "created 2026-09-23 16:07; 85 IKVs (84 employees) + 1 correction block "
              "(August 2026, 1 IKV, saldo 0)"),
   ("Received from", "Suresh Jalihal (Primary SBC), Google Chat, 08-10-2026 12:26 - "
                     "Excerpta Medica B.V._September 2026 reports.zip (8 files)"),
   ("Documents checked", "Return XML; Gross To Net (86 rows); payslips (85 pages); SEPA "
                         "file (84 transfers); Payment Report; GL (2.185 lines); master "
                         "data (83 employees); HRBLIZZ Wage Tax Overview"),
   ("Product", "HRBLIZZ (Mercans)"),
   ("Prepared", "Compliance team (Wallisson Gomes), 14-10-2026"),
  ],
  "summary": [
   ("Overall conclusion", "Qualified. Return, G2N, payslips, payment report, SEPA file "
    "and GL tie per employee and in total; employer premiums (including WAZO 'uitkering' "
    "premiums) recalculate at the 2026 rates on every IKV; special rates are valid and "
    "match the Jaarloon BT bracket. One AOW-age employee is withheld outside the table, "
    "and 19 IKVs differ from the table by one cent. Acceptance by the Belastingdienst is "
    "not evidenced."),
   ("Most important", "F-01: M1023246 (AOW age since January 2026) - regular "
    "withholding 452,16 is not a table amount; the AOW column gives 485,08 "
    "(EUR 32,92 under-withheld in September)."),
   ("Calculation results", "Regular withholding: 64/84 white-table IKVs exact, 19 "
    "within EUR 0,01, 1 off by EUR 32,92; premiums exact on all 85 IKVs; net pay "
    "282.024,00 = payment report = SEPA = GL; loonheffingen 152.069 = TotTeBet = GL."),
  ],
  "findings": [
   ("F-01", "High", "Wage tax - AOW-age employee",
    "M1023246 reached AOW age on 26-01-2026 (born 26-01-1959). From that month the "
    "AOW column applies. September regular loonheffing is 452,16 on a tabelloon of "
    "4.138,61; the monthly table (AOW, born 1946 or later, with loonheffingskorting) "
    "gives 485,08 excluding the alleenstaandeouderenkorting (440,08 including it). "
    "452,16 is not an amount of any column. The payslip shows 'Married', so the "
    "excl.-AOK column applies. Premiums are correctly nil (AOW) and the special rate "
    "59,01% is the AOW bb column.",
    "Return IKV 0002: LnLbPh 4.138,61, IngLbPh 452,16, VerrArbKrt 225,75 (= table); "
    "G2N 2552 452,16; payslip 'Wage Tax 452,16', ZVW/WW/WIA K/No/No.",
    "EUR 32,92 under-withheld in September (excl.-AOK column). Earlier 2026 months not "
    "tested.", "Witte Maandloon-tabel 2026, AOW columns; Handboek 2026 §9.3.3.",
    "Open", 1),
   ("F-02", "Low", "Wage tax - rounding",
    "19 of 84 white-table IKVs differ from the monthly table by EUR 0,01 (6 higher, 13 "
    "lower), two of them above the last table step. The engine appears to calculate "
    "by formula with its own rounding rather than reading the table. Quest (same "
    "engine) matched the table exactly.",
    "e.g. M1022919 table 526,08 / withheld 526,09; M1022921 433,92 / 433,91; M1022923 "
    "(above table top) 4.946,76 / 4.946,75. Full list in the evidence file.",
    "<= EUR 0,01 per employee.", "Witte Maandloon-tabel 2026 (rounding in the "
    "employee's favour, table footer).", "Open", 19),
   ("F-03", "Observation", "Correction block",
    "The August 2026 correction carries one IKV (M1023003) with saldo 0. Under loon-over "
    "a correction is expected when an earlier period changes; a zero saldo fits a "
    "non-monetary change (e.g. hours or an indicator). What changed cannot be seen "
    "without the original August message.",
    "TijdvakCorrectie 2026-08-01..31: collective TotTeBet 448.911; IKV M1023003 "
    "IngLbPh 820,91; SaldoCorrectiesVoorgaandTijdvak 0.", "None on the amount due.",
    "Handboek 2026 §9.2.1 / §14.2.3.", "Open", 1),
   ("F-04", "Observation", "Leaver - loonheffingskorting on two IKVs",
    "M1022936 (fixed-term end 30-09-2026) has loonheffingskorting applied on both "
    "IKVs: the salary (white table) and the transition payment (SrtIV 62, green bb "
    "table at 43,96% = 37,56% + 6,40% 'met loonheffingskorting'). Without the credit "
    "the green rate is 37,56%. Confirm the engine's rule for the credit on a second "
    "IKV of the same employee.",
    "IKV 0002: LnTabBB 1.098,37, IngLbPh 482,84 (43,96%); IndLhKort J on both IKVs.",
    "If the credit should not apply: EUR 70,29 over-withheld (482,84 vs 412,55).",
    "Groene tabel bijzondere beloning 2026; Handboek 2026 h.24.", "Open", 1),
   ("F-05", "Low", "Wage Tax Overview",
    "The HRBLIZZ 'Wage Tax Overview' prints deadline 2026-10-30; the official deadline "
    "for tijdvakcode 6090 is 31-10-2026. It is a system summary, not a receipt.",
    "Excerpta Medica B.V..Wage Tax Overview.09.2026.pdf (created 2026-09-24).",
    "None.", "Tijdvakcodes 2026.", "Open", 1),
  ],
  "overrides": {
   "X-20": ("Pass", "Reviewed: the two G2N-only employees (M1022953, M1022968) left in "
                    "June 2026 and have all-zero rows; they are correctly absent from the "
                    "return (no wage in September)."),
   "E-08": ("Pass", "Reviewed: M1023246 has no Whk base because of AOW age; Zvw "
                    "252,46 = 6,10% of 4.138,61 is correct."),
   "D-02": ("Finding", "See F-01 (and F-02 for the cent differences)."),
   "L-04": ("Finding", "Reviewed: these are the EUR 0,01 differences of F-02 - the "
                       "payslip prints the amount actually withheld."),
   "H-01 / H-02": ("Pass", "Reviewed: 156 = 36 h x 52 / 12, the average monthly hours "
                           "for a fixed monthly wage (Handboek §29.9). Correct."),
   "H-03": ("Pass", "Reviewed: the zero is the SrtIV 62 IKV of M1022936 (must be 0, "
                    "poortcontrole 1713)."),
   "A-09": ("Finding", "See F-03."),
   "M-04": ("Pass", "Reviewed: M1022936 is a leaver (end 30-09-2026), not in the "
                    "active-employee extract."),
   "G-02 / H-01 / D-11": ("Finding", "Reviewed: M1022921 payslip 50,47% vs computed "
                                      "50,50% is the F-02 cent in the regular tax; the "
                                      "applied rate (G2N 2572/58572) is 50,47%."),
  },
  "not_tested": [
   ("NT-01", "Acceptance of the return by the Belastingdienst",
    "No Digipoort response in the pack; the Wage Tax Overview is generated by HRBLIZZ.",
    "Digipoort status response for 822945526L01P20260901."),
   ("NT-02", "Whk rate against the beschikking", "Implied rate 1,71% consistent on 83 "
    "IKVs; beschikking not supplied.", "Whk beschikking 2026."),
   ("NT-03", "What the August correction changed", "Original August message not "
    "supplied.", "August 2026 loonaangifte as first submitted."),
   ("NT-04", "Payslip verloonde uren, written/on-call indicators", "Not readable "
    "reliably from the English payslip template's text layer.", "Structured payslip "
    "export or manual reading."),
   ("NT-05", "Payslip cumulative roll-forward (J-02)", "Only September payslips.",
    "August payslips or year-to-date G2N."),
   ("NT-06", "Tax/SV base composition per wage type (G-S5)", "No client wage-type "
    "catalogue with LB/SV flags.", "Client wage-type catalogue export."),
  ],
 },
 "sherwin": {
  "file": "NL_SherwinWilliams_2026-09_Validation.xlsx",
  "cover": [
   ("Client", "Sherwin Williams Valspar B.V. (REF-1-977; pay group NLD_LELYSTAD_MONTHLY)"),
   ("Loonheffingennummer", "002879487L01 (return NmIP: 'Valspar B.V.')"),
   ("Period", "September 2026 (tijdvak 2026-09-01 to 2026-09-30, tijdvakcode 6090)"),
   ("Return", "002879487L01.09.2026.xml - namespace Loonaangifte/2026/01, version 2.0, "
              "created 2026-09-28 07:49; 222 IKVs (222 employees) + 8 correction blocks "
              "(January-August 2026, saldi total EUR 3.010)"),
   ("Received from", "Umesh Gaikwad (Primary SBC), Google Chat, 08-10-2026 04:09 - "
                     "Netherlands Sherwin Williams REF-1-977.zip (13 files)"),
   ("Documents checked", "Return XML; Gross To Net (222 rows); payslips (317 pages); "
                         "net-pay SEPA file (222 transfers); tax-payment SEPA file; "
                         "garnishment SEPA file; GL detail (5.953 lines); GL interface "
                         "file; master data; Digipoort response (JSON/TXT)"),
   ("Product", "HRBLIZZ (Mercans)"),
   ("Prepared", "Compliance team (Wallisson Gomes), 14-10-2026"),
  ],
  "summary": [
   ("Overall conclusion", "Qualified. Return, G2N, payslips, SEPA files and GL tie in "
    "total; under loon-over the period block carries September only and the retro sits "
    "in the 8 correction blocks (G2N/GL minus period block = EUR 3.008,17 against "
    "correction saldi of EUR 3.010, whole-euro rounding per period). Premiums "
    "recalculate at the 2026 rates on every IKV. The authority response in the pack "
    "belongs to another loonheffingennummer, one AOW-age leaver is over-withheld, and "
    "hours are declared as working days."),
   ("Most important", "F-01: the Digipoort response is for 868240503L01, not this "
    "return. F-02: 0426237 (AOW age) - EUR 155,82 regular tax withheld where the AOW "
    "column gives 0,00."),
   ("Calculation results", "Regular withholding on the 205 IKVs without a "
    "special-rate wage: 145 exact, 49 within EUR 0,01, 9 within EUR 0,09, 2 on the AOK "
    "column (Observation). 17 IKVs with a special-rate wage: every rate valid, 1 "
    "regular-tax error (F-02). Premiums exact on all 222 IKVs; net pay 792.057,21 = "
    "SEPA = GL; payment 478.025 = TotGen = tax SEPA file; garnishments 547,51 = GL."),
  ],
  "findings": [
   ("F-01", "High", "Authority receipt",
    "The Digipoort status response supplied as the receipt belongs to "
    "loonheffingennummer 868240503L01, dated 05-10-2026. This return is for "
    "002879487L01 and was created on 28-09-2026. There is no evidence in the pack that "
    "this return was delivered or accepted, and the pack contains another payroll tax "
    "number's submission data.",
    "'Full original response message (5).json' = 'Original response (FTP Files Download "
    "Business Successful Result) (4).txt' (identical): kenmerk 0e0e0e6b-..., status 100-"
    "800 incl. 500 'Validatie bij de uitvragende partij gelukt', all for 868240503L01.",
    "Acceptance of the September return unproven; data-protection point (other "
    "employer's submission data shared).", "Digipoort getStatussenProces; "
    "Gegevensspecificaties 2026.", "Open", 1),
   ("F-02", "High", "Wage tax - AOW-age leaver",
    "0426237 reached AOW age in March 2026 (born 08-03-1959) and left on 07-09-2026. "
    "On a tabelloon of 1.042,13 the AOW column (born 1946 or later, with "
    "loonheffingskorting) gives 0,00, but 155,82 regular tax was withheld (G2N 2552). "
    "Verrekende arbeidskorting is declared 49,26; the table gives 0,00. The special "
    "rate is correct (1.880,94 = 44,01% of 4.273,89; AOW bb column at Jaarloon BT "
    "72.165). Related: the payslip shows 'Oproep Ja' while the return declares N; the "
    "leaving reason is code 99 (F-06); G2N 58210 'Employee Age' shows 68 (67 in "
    "September).",
    "Return IKV 0001: LnLbPh 5.316,02, LnTabBB 4.273,89, IngLbPh 2.036,76; G2N 2552 "
    "155,82, 2572 1.880,94.", "EUR 155,82 over-withheld from the employee.",
    "Witte Maandloon-tabel 2026, AOW columns; Handboek 2026 §9.3.3.", "Open", 1),
   ("F-03", "Medium", "Return - verloonde uren",
    "190 of 222 IKVs declare 176 verloonde uren (22 working days x 8) while the "
    "payslips of the full-time monthly-paid employees print 173,33. For a fixed "
    "monthly wage the Handboek requires the average monthly hours (173). Same pattern "
    "as Quest.",
    "219 employees where payslip and return differ (e.g. 0416882 slip 173,33 / return "
    "176).", "No tax or premium effect; UWV/CBS/AWf herziening data.",
    "Handboek Loonheffingen 2026 §29.9.", "Open", 190),
   ("F-04", "Medium", "Payslip - Jaarloon BT",
    "Three leavers' payslips print 'Jaarloon BT 0.00' although a special rate was "
    "applied, so the employee cannot verify the rate.",
    "0417692 (56,01%), 1184067 (42,01%), 1209255 (50,47%); each rate is a valid rate "
    "of the white bb column.", "Rate not verifiable from the payslip.",
    "Handboek 2026 §9.3.6.", "Open", 3),
   ("F-05", "Observation", "Wage tax - alleenstaandeouderenkorting",
    "Two AOW-age employees are withheld on the column including the "
    "alleenstaandeouderenkorting (0,00); excluding it the table gives 9,00 and 10,83. "
    "The AOK applies only if the employee is entitled to it (AOW for a single person). "
    "Entitlement is not evidenced in the pack.",
    "0420831 IKV 0002 (tabelloon 2.939,14), 0421178 IKV 0002 (2.947,94); IngLbPh 0,00.",
    "EUR 19,83 for September if not entitled.", "Witte Maandloon-tabel 2026, AOW "
    "columns; Handboek 2026 h.24.", "Open", 2),
   ("F-06", "Medium", "Return - reden einde",
    "Two leavers carry reason code 99 ('een andere, hiervoor niet genoemde reden'). For "
    "0426237, who left after reaching AOW age, a specific code (e.g. 32 pensionering) "
    "may apply. Confirm the actual ground for each.",
    "0421039, 0426237: CdRdnEindArbov 99.", "Data quality of a filed rubriek (UWV).",
    "Codes voor de aangifte loonheffingen 2026, Code reden einde arbeidsverhouding.",
    "Open", 2),
   ("F-07", "Low", "Wage tax - rounding",
    "58 of 205 IKVs differ from the monthly table by a few cents: 49 by EUR 0,01 and "
    "9 by up to EUR 0,09 (four of these above the last table step), where the "
    "verrekende arbeidskorting is also a few cents off. Formula calculation instead of "
    "table lookup (same pattern as Excerpta).", "e.g. 1253724 table 375,92 / withheld "
    "376,00; 0422269 9.469,95 / 9.470,00. Full list in the evidence file.",
    "<= EUR 0,09 per employee.", "Witte Maandloon-tabel 2026.", "Open", 58),
   ("F-08", "Low", "Payslip - start date",
    "134 payslips print 'In dienst' as the original hire date (e.g. 01-09-2016) while "
    "the return and the master data use the start date with this loonheffingennummer "
    "(2017-06-01). The return is consistent with the master data.",
    "e.g. 0416882, 0417022, 0417038.", "Presentation; confirm intended.",
    "Gegevensspecificaties 2026, Datum aanvang inkomstenverhouding.", "Open", 134),
   ("F-09", "Low", "GL - labels",
    "On the expense side AWf laag is posted as 'Premium WE Revised' (the name of the "
    "AWf herzien premium) and AWf hoog as 'Premium WE (haag)'. Liability labels and all "
    "amounts are correct.", "GL account 6036001.", "Presentation.", "-", "Open", 2),
  ],
  "overrides": {
   "X-02": ("Pass", "Reviewed: per-employee differences are the retro paid in "
                    "September. Under loon-over the period block holds September wage "
                    "only and the retro is declared in the correction blocks; in total "
                    "G2N minus period block = EUR 3.008,17 vs correction saldi EUR "
                    "3.010 (whole euros per period). Per-employee proof needs the "
                    "original January-August messages (NT-03)."),
   "D-02": ("Finding", "See F-02, F-05 and F-07."),
   "D-03": ("Finding", "Reviewed: consequence of F-02 (the regular-tax error moves "
                       "into the implied special rate); the applied special rate is "
                       "44,01%, a valid AOW rate."),
   "D-08": ("Finding", "See F-02 (0426237) and F-07 (cent differences)."),
   "D-12": ("Finding", "See F-05."),
   "E-08": ("Pass", "Reviewed: the three IKVs without a Whk base are AOW-age "
                    "employees; Zvw at 6,10% of the wage is correct."),
   "L-04": ("Finding", "Reviewed: the cent differences of F-07 and the regular/BT "
                       "split of F-02; payslips print the amounts actually withheld."),
   "G-02 / H-01 / D-11": ("Finding", "See F-02, F-03, F-04, F-08."),
   "H-01 / H-02": ("Finding", "See F-03."),
   "I-02": ("Finding", "See F-06."),
   "A-10": ("Finding", "See F-01."),
   "M-04": ("Pass", "Reviewed: 1351879 was hired on 01-09-2026; the master extract "
                    "is dated 10-09-2026 and does not yet include the employee."),
  },
  "not_tested": [
   ("NT-01", "Acceptance of this return", "The response in the pack is for another "
    "loonheffingennummer (F-01).", "Digipoort status response for "
    "002879487L01P20260901."),
   ("NT-02", "Whk rate against the beschikking", "Implied rate 1,83% consistent on 219 "
    "IKVs; beschikking not supplied.", "Whk beschikking 2026."),
   ("NT-03", "Per-employee retro allocation (A-07)", "Original January-August "
    "messages and a transaction-level retro export were not supplied; the correction "
    "blocks show corrected values only.", "Original 2026 monthly messages or the "
    "pay-element retro export."),
   ("NT-04", "Payslip loonheffingskorting and ZVW/WW/WIA header fields", "Labels and "
    "values are split across lines in this template's text layer.", "Manual reading "
    "or a structured payslip export."),
   ("NT-05", "Payslip cumulative roll-forward (J-02)", "Several pages per employee "
    "are retro slips of the same run; prior-run payslips not supplied.", "August 2026 "
    "payslips."),
   ("NT-06", "Tax/SV base composition per wage type (G-S5)", "No client wage-type "
    "catalogue with LB/SV flags.", "Client wage-type catalogue export."),
  ],
  "extra_recon": [
   ("Garnishments", "GL deductions CAK + LAVG + STAM", 547.51,
    "garnishment_BankFile.xml (4 transfers)", 547.51),
   ("Correction saldi (loon-over)", "G2N/GL statutory minus period block", 3008.17,
    "Sum of SaldoCorrectiesVoorgaandTijdvak (whole euros)", 3010.00),
  ],
 },
}
