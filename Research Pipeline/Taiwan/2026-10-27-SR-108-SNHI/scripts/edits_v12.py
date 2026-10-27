# -*- coding: utf-8 -*-
"""SR-108 TW SNHI spec v1.1 -> v1.2: lista fechada de celulas alteradas/novas.
Cada entrada: (parte XML, celula, tipo, valor, fonte). Tipos: str | num | date.
Nada fora desta lista pode mudar (conferido por compare_v12.py)."""
import datetime

S1 = "xl/worksheets/sheet1.xml"  # Version Control
S2 = "xl/worksheets/sheet2.xml"  # Report Matrix
S3 = "xl/worksheets/sheet3.xml"  # Spec(TXT)
SHEET_NAME = {S1: "Version Control", S2: "Report Matrix", S3: "Spec(TXT)"}

TBC = "TO BE CONFIRMED BY MOHIT/BA"
FW = ("converted to full-width characters and padded with full-width spaces (U+3000) "
      "to 25 characters (50 bytes BIG5); truncate after 25 characters")
UBN_G = ("Withholding agent's Unified Business Number (扣費單位統一編號), 8 characters. "
         "Same value in sections A, B and C.")
UBN_I = ("$legal_entity_hr.company_registration_number (公司統一編號, DD V3.3); "
         "same field as C33 (Lisa, J33: company registration number)")

EDITS = [
    # ---------------- Version Control ----------------
    (S1, "B15", "num", 1.2, "pedido"),
    (S1, "C15", "date", datetime.date(2026, 10, 27), "pedido"),
    (S1, "D15", "str",
     "Spec review against the NHIA TXT layout for income type 62 and the Supplementary Premium "
     "Regulations: section C totals = sum of the detail lines (not YTD); UBN in sections A/B/C; "
     "NHI insured unit code (93-101); ROC dates; declaration number; Income Payment Date and "
     "Total Entries mapped; periodicity, filing method, encoding; N fields never negative; "
     "sample values. Open points marked " + TBC + ".", "pedido"),
    (S1, "E15", "str", "Draft", "pedido"),
    (S1, "F15", "str", "Wallisson Gomes", "pedido"),

    # ---------------- Report Matrix ----------------
    (S2, "B5", "str", "Period, Tax Year", "F2 art. 10; F5 p.1"),
    (S2, "B6", "str", "Period", "F2 art. 10; F5 p.1 (C1)"),
    (S2, "B8", "str",
     "BIG5 (NHIA: data code ASCII and BIG5; numeric/code fields single-byte, name fields in "
     "full-width characters)", "F3 nota 3 (C3)"),
    (S2, "B11", "str",
     "Section A (withholding unit): 1 line per file. Section B (detail): 1 line per bonus "
     "payment with SNHI withheld. Section C (totals): 1 line per file = totals of the section B "
     "lines. Every line is 200 bytes.", "F3 seções 一/二/三"),
    (S2, "B12", "str", "Electronic: Upload online ", "F5 p.1; F2 art. 10 §3 (C2)"),
    (S2, "B13", "str", "Not applicable (TXT data file; name fields in Traditional Chinese, full-width)",
     "F3 A9/B13/C8"),
    (S2, "B15", "str",
     "Category 1 insured employees of the entity (active and terminated) who received a bonus in "
     "the period. A bonus paid after termination is included (4x the insured amount at "
     "withdrawal applies).", "F2 art. 6"),
    (S2, "B16", "str",
     "Bonus payment with SNHI employee premium withheld (2558 > 0) in the period. One file per "
     "payment year (a file cannot span two years).", "F2 art. 10; F3 A4/A5"),
    (S2, "B17", "str", "TWD (whole NT$, no decimals)", "F3 B9/B10"),
    (S2, "B21", "str",
     "Detail declaration (扣費明細) of the supplementary NHI premium withheld on bonuses, income "
     "type 62: the part of the bonus paid by the employee's own insured unit that, accumulated "
     "from 1 January to the payment date, exceeds 4x the insured amount of the month (NHI Act "
     "art. 31(1)(1); Supplementary Premium Regulations arts. 3, 4 and 6). Rate 2.11% from "
     "2021-01-01. Filing: electronically together with each monthly premium payment (premium due "
     "by the end of the month following payment), which waives the annual filing; or annually by "
     "31 January of the following year (5 February if January has 3 or more consecutive public "
     "holidays) (Regulations art. 10). The employer's own supplementary premium (code 61, NHI Act "
     "art. 34) needs no detail and is outside this report.", "F1 art. 31; F2 arts. 3,4,6,10; F5; F6"),
    (S2, "B23", "str",
     "        1.        Type N fields = numbers, right-aligned, pad left with zeros\n"
     "        2.        Type C fields = characters, left-aligned, pad right with spaces\n"
     "        3.        Encoding: ASCII or BIG5\n"
     "        4.        Do not use commas or currency symbols in numeric values\n"
     "        5.        Type N fields can never be negative\n"
     "        6.        Section C totals (positions 12-20, 21-40, 41-56) = count and sums of the "
     "section B lines in the same file", "F3 notas 1-2; F3 seção 三 campos 4-6"),

    # ---------------- Spec(TXT) ----------------
    (S3, "G4", "str", UBN_G, "F3 seção 一 campo 2 (C4)"),
    (S3, "I4", "str", UBN_I, "F3 seção 一 campo 2; DD V3.3 Country Fields (C4)"),
    (S3, "F6", "str",
     "Format: yyymm (ROC year = Gregorian year - 1911, e.g. 11406 = June 2025); earliest payment "
     "month of the detail lines in the file; cannot span across years", "F3 A4 (C6)"),
    (S3, "F7", "str",
     "Format: yyymm (ROC year); latest payment month of the detail lines in the file; same year "
     "as the start month", "F3 A5 (C6)"),
    (S3, "F8", "str", "Format: yyymmdd (ROC year, 7 characters)", "F3 A6 (C5)"),
    (S3, "I8", "str",
     "CONCAT(SUBTRACT(DATE_FORMAT($report.generation_time; 'yyyy'); 1911); "
     "DATE_FORMAT($report.generation_time; 'MMdd'))", "F3 A6 (C5); padrão TW Tax Report Spec H18/H33"),
    (S3, "I9", "str",
     "Blank (8 spaces) for a single unit. Filled with the head office UBN only when the entity "
     "has a head office (總機構); no such field in DD V3.3.", "F3 A7"),
    (S3, "I11", "str", "$legal_entity.name, " + FW, "F3 A9"),
    (S3, "E14", "str", "08628407", "amostra NHIA (SNHI_sample.txt)"),
    (S3, "G14", "str", UBN_G, "F3 seção 二 campo 2 (C4)"),
    (S3, "I14", "str", UBN_I, "F3 seção 二 campo 2 (C4)"),
    (S3, "I16", "str",
     "Sequential per detail line in the file: 000000001, 000000002, ... (N, 9, left-padded with "
     "zeros)", "F3 B4"),
    (S3, "I17", "str",
     "I (new). R (replace) is not supported by the product (Mohit, L17); corrections are made "
     "outside this report.", "F3 B5; L17"),
    (S3, "F18", "str", "Format: yyymmdd (ROC year, 7 characters)", "F3 B6"),
    (S3, "I18", "str",
     "Actual payment date of the bonus (Regulations art. 2: actual, transfer or remittance date), "
     "ROC yyymmdd: CONCAT(SUBTRACT(DATE_FORMAT(<payment date>; 'yyyy'); 1911); "
     "DATE_FORMAT(<payment date>; 'MMdd')). " + TBC + ": engine variable holding the payment "
     "date of the payroll run.", "F3 B6; F2 arts. 2 e 10"),
    (S3, "F20", "str",
     "Alphanumeric (C), left-aligned, padded with spaces on the right; no duplicates", "F3 B8 (C7)"),
    (S3, "I20", "str",
     "'1' by default; '2', '3', ... when the same recipient has 2 or more bonus payments on the "
     "same payment date (NHIA CSV layout rule). Letters and digits only, left-aligned, "
     "right-padded with spaces to 30 characters (not left-padded with 0).", "F3 B8; F4 (C7)"),
    (S3, "I21", "str",
     "Current period value of 58009.\n" + TBC + ": 58009 must be the same bonus base that drives "
     "2558 (bonus not included in the insured amount, e.g. year-end bonus, festival bonus, "
     "profit share; Regulations art. 3(1)). Full amount of this payment, N 14, never negative.",
     "F3 B9; F2 art. 3"),
    (S3, "G23", "str",
     "Block of 4 sub-fields (rows 24-27). Mandatory for income types 62 and 66.", "F3 B11 + nota 4"),
    (S3, "I23", "str",
     "No value of its own: filled by rows 24-27 (positions 93-101, 102-107, 108-117, 118-132).",
     "F3 nota 4"),
    (S3, "B24", "str", "Insured Unit Code (投保單位代號)", "F3 nota 4 (C8)"),
    (S3, "F24", "str",
     "NHI insured unit code, C, 9 characters (NHIA sample 123456789). Not the UBN.", "F3 nota 4; amostra"),
    (S3, "I24", "str",
     TBC + ": proposed $legal_entity_hr.health_insure_id (DD V3.3 'Health Insurance ID' 健保證號, "
     "9 digits; same field used for the NHI unit code in the TW SI Termination spec). Previous "
     "mapping social_security_integrate_number is the 8-digit UBN (統一編號).",
     "F3 nota 4; DD V3.3 ID Information (C8)"),
    (S3, "I25", "str",
     TBC + ": PE 58139 does not exist in WTC V2.8; proposed 64550 (SNHI Interim Base = "
     "$hr.nhi_grade::orLabel). Insured amount of the month of payment; for a bonus paid after "
     "termination, the insured amount at withdrawal (Regulations art. 6). N 6, never negative.",
     "F3 nota 4; F2 art. 6; WTC V2.8 (C9)"),
    (S3, "I26", "str",
     "YTD of 58009 including current month 58009 value (1 January to this payment date, "
     "Regulations art. 6). " + TBC + ": same bonus base as I21. N 10, never negative.",
     "F3 nota 4; F2 art. 6"),
    (S3, "I29", "str", "$employee_name, " + FW, "F3 B13"),
    (S3, "I35", "str",
     "COUNT of section B (detail) lines in this file. N 9, left-padded with zeros.",
     "F3 seção 三 campo 4"),
    (S3, "I36", "str",
     "SUM of positions 69-82 (Bonus Payment Amount) of all section B lines in this file; not YTD. "
     "N 20, left-padded with zeros.", "F3 seção 三 campo 5 (C10)"),
    (S3, "E36", "str", "00000000000000286942", "amostra NHIA (C13)"),
    (S3, "I37", "str",
     "SUM of positions 83-92 (Supplementary Insurance Fee) of all section B lines in this file; "
     "not YTD. N 16, left-padded with zeros.", "F3 seção 三 campo 6 (C11)"),
    (S3, "E37", "str", "0000000000002101", "amostra NHIA (C13)"),
    (S3, "E38", "str", "27065866#1111", "amostra NHIA (C13)"),
    (S3, "I39", "str",
     "Contact person (聯絡人姓名), " + FW + ". " + TBC + ": DD V3.3 has no contact-person field; "
     "$legal_entity_hr.representative (代表人, legal representative) is used until one exists.",
     "F3 seção 三 campo 8 (C12)"),
]

# =====================================================================
# RODADA 2 (2026-10-27): achados 1-7 de REVISAO-independente.md.
# Cada entrada substitui a da rodada 1 na mesma célula ou acrescenta célula nova.
# Perguntas saem da coluna I (mapeamento) e vão para a coluna K (Questions), como K16/K17/K20.
# =====================================================================
UBN_X = "PREPAD($legal_entity_hr.company_registration_number; 8; '0')"
ROC = ("CONCAT(PREPAD(SUBTRACT(DATE_FORMAT({d}; 'yyyy'); 1911); 3; '0'); DATE_FORMAT({d}; '{f}'))")
ROUND2 = [
    (S1, "D15", "str",
     "Spec review against the NHIA TXT layout for income type 62 and the Supplementary Premium "
     "Regulations: section C totals = sum of the detail lines (not YTD); UBN in sections A/B/C; "
     "NHI insured unit code (93-101); ROC dates; declaration number; Total Entries mapped, "
     "Income Payment Date proposed; periodicity, filing method, encoding; N fields never "
     "negative; sample values. 3 open questions in Spec(TXT) column K.", "achado 1"),
    (S2, "B16", "str",
     "Proposed (inference from Regulations art. 10, which requires the detail of the premium "
     "withheld): bonus payments with SNHI employee premium withheld (2558 > 0) in the period. "
     "I5 uses MAX(58133+58009+58132;0) > 0 (YTD bonus above 4x the insured amount, per WTC "
     "names); both should select the same payments when 2558 is calculated on that excess, but "
     "the 2558 formula is not in WTC V2.8 (question in Spec(TXT)!K21). One file per payment year "
     "(a file cannot span two years).", "achado 4; F2 art. 10; F3 A4/A5"),
    (S2, "B23", "str",
     "        1.        Type N fields = numbers, right-aligned, pad left with zeros\n"
     "        2.        Type C fields = characters, left-aligned, pad right with spaces\n"
     "        3.        Encoding: ASCII and BIG5\n"
     "        4.        Do not use commas or currency symbols in numeric values\n"
     "        5.        Type N fields can never be negative\n"
     "        6.        Section C totals (positions 12-20, 21-40, 41-56) = count and sums of the "
     "section B lines in the same file", "achado 7; F3 nota 3"),
    (S3, "I4", "str", UBN_X + " (公司統一編號, DD V3.3: Number, maximum 8 digits; output 8 characters "
     "with leading zeros); same field as C33 (Lisa, J33)", "achado 3; F3 campo 2"),
    (S3, "I14", "str", UBN_X + " (公司統一編號, DD V3.3: Number, maximum 8 digits; output 8 characters "
     "with leading zeros); same field as C33 (Lisa, J33)", "achado 3; F3 campo 2"),
    (S3, "I33", "str", UBN_X, "achado 3; F3 seção 三 campo 2"),
    (S3, "I6", "str",
     "Take period in which first bonus is paid from pay element 58009 date within the tax year. "
     "Output in ROC yyymm: " + ROC.format(d="that payment date", f="MM"), "achado 5; F3 A4"),
    (S3, "I7", "str",
     "Take period in which latest bonus is paid from pay element 58009 date within the tax year. "
     "Output in ROC yyymm: " + ROC.format(d="that payment date", f="MM"), "achado 5; F3 A5"),
    (S3, "I8", "str", ROC.format(d="$report.generation_time", f="MMdd"), "achado 6; F3 A6"),
    (S3, "I18", "str",
     "Proposed: actual payment date of the payroll run in which the bonus (58009) is paid "
     "(Regulations art. 2), in ROC yyymmdd with the same formula as I8 (ROC year with 3 digits "
     "+ MMdd). Engine variable: question in K18.", "achado 1; F3 B6; F2 art. 2"),
    (S3, "K18", "str",
     "Which engine variable holds the actual payment date of the payroll run? I18 needs it in "
     "ROC yyymmdd.", "achado 1"),
    (S3, "I20", "str",
     "CONCAT(" + UBN_X + "; '62'; Income Payment Date (positions 22-28, ROC yyymmdd); Serial "
     "Number (positions 12-20)) = 26 characters, e.g. 08628407621050412000000001; left-aligned, "
     "right-padded with spaces to 30. Employer numbering, letters and digits only, no "
     "duplicates (TXT layout); the payment date keeps it unique across monthly files, since the "
     "serial restarts in each file.", "achado 2; F3 B8; amostra E20"),
    (S3, "I21", "str",
     "Current period value of 58009. Full amount of this payment, N 14, never negative. "
     "Bonus base: question in K21.", "achado 1; F3 B9"),
    (S3, "K21", "str",
     "Is 58009 the same bonus base that drives 2558? 58009 sums 6221x and 6222x only; "
     "should 6220x Bonus (Annual/Referral) be included (year-end bonus, Regulations art. 3(1))? "
     "Are bonus payments with no premium withheld (YTD still below 4x) listed (Report Matrix B16 "
     "assumes 2558 > 0)?", "achado 1 e 4"),
    (S3, "I24", "str",
     "PREPAD($legal_entity_hr.health_insure_id; 9; '0') (proposed: DD V3.3 'Health Insurance ID' "
     "健保證號, 9 digits; same field as the NHI unit code in the TW SI specs). Previous mapping "
     "social_security_integrate_number is the 8-digit UBN (統一編號). Question in K24.",
     "achado 1 e 3; F3 nota 4"),
    (S3, "K24", "str",
     "Is $legal_entity_hr.health_insure_id the NHI insured unit code (投保單位代號, 9 characters)?",
     "achado 1"),
    (S3, "I25", "str",
     "Proposed: 64550 (SNHI Interim Base = $hr.nhi_grade::orLabel) of the month of payment; for "
     "a bonus paid after termination, the insured amount at withdrawal (Regulations art. 6). "
     "N 6, never negative. Previous mapping SUM(58139): PE 58139 does not exist in WTC V2.8. "
     "Question in K25.", "achado 1; F3 nota 4; F2 art. 6"),
    (S3, "K25", "str",
     "PE 58139 is not in WTC V2.8. Is 64550 the insured amount of the month of payment?", "achado 1"),
    (S3, "I26", "str",
     "YTD of 58009 including current month 58009 value (1 January to this payment date, "
     "Regulations art. 6). Same bonus base as I21 (question in K21). N 10, never negative.",
     "achado 1; F2 art. 6"),
    (S3, "I39", "str",
     "Contact person (聯絡人姓名), " + FW + ". Proposed until a contact field exists: "
     "$legal_entity_hr.representative (代表人). Question in K39.", "achado 1; F3 seção 三 campo 8"),
    (S3, "K39", "str",
     "DD V3.3 has no contact-person field. Use $legal_entity_hr.representative or create a "
     "contact field?", "achado 1"),
]
_r1 = {(p, c): i for i, (p, c, *_x) in enumerate(EDITS)}
ROUND1 = list(EDITS)
for e in ROUND2:
    k = (e[0], e[1])
    if k in _r1: EDITS[_r1[k]] = e
    else: EDITS.append(e)
