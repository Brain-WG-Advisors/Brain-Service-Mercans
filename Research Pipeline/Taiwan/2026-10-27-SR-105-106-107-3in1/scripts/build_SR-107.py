"""SR-107 - TW SI electronic filing Joiner: base export 2026-10-27 -> v1.1.
Source of truth for field rules: NHIA/BLI 三合一批次加保格式說明 (01_Apply3Of1, rev. 115.03.11)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from xlsxpatch import Book
from common import *

BASE = r"C:\Users\instituto\Documents\brain-service\raw\docs\drive-exports\2026-10-27\TW - SI electronic filing Joiner Specification.xlsx"
OUT = pathlib.Path(__file__).resolve().parent.parent / "TW - SI electronic filing Joiner Specification v1.1.xlsx"

b = Book(BASE)
VC, RM, SP = "Version Control", "Report Matrix", "Spec"

# ---- Version Control
b.set(VC, "B9", "Taiwan")
b.set(VC, "B14", "1.1", num=True, style_from="B13")
b.set(VC, "C14", VC_DATE_SERIAL, num=True, style_from="C13")
b.set(VC, "D14", "Spec review against NHIA/BLI 3-in-1 batch enrolment format (01_Apply3Of1, rev. 115.03.11): "
                 "field mappings, C/M/O, data types and Report Matrix updated; 'New Specification' tab "
                 "(withholding tax) removed.", style_from="D13")
b.set(VC, "E14", VC_STATUS, style_from="E13")
b.set(VC, "F14", VC_BY, style_from="F13")

# ---- Report Matrix
b.set(RM, "B10", "Employee level: one row per new hire (投保者 = 1) plus one row per NHI dependant (投保者 = 2).")
b.set(RM, "B11", ELECTRONIC)
b.set(RM, "B14", "New hires enrolled by the same unit in LI(+EI)/OAI, LP and NHI (投保別 2) or in OAI, LP and NHI "
                 "(投保別 4). Excluded (guide 01_Apply3Of1, rev. 115.03.11, note to field 6): NHI-only enrolments and "
                 "enrolment of foreign (外籍) employees, for whom LI and NHI are filed separately (NHI with NHIA). "
                 "Whether codes 1/2/L of field 7 are also excluded: TO BE CONFIRMED BY MOHIT/BA.")
b.set(RM, "B22", "File on the hire date (到職當日). LI/EI coverage starts at 00:00 on the filing date; if not filed on "
                 "the hire date, from the next day (BLI form 承表D rev. 115.01, note 2). NHI starts on the day the "
                 "enrolment conditions are met. Electronic batch: Excel upload in the NHIA multi-certificate system; "
                 "the official guide defines column order, values and notes only (no start/end positions, no "
                 "official TXT layout).")

# ---- Spec: new columns K/L (C/M/O, Data Type); J is used by Mohit's note in J8
b.set(SP, "K2", CMO_HEADER, style_from="H2")
b.set(SP, "L2", TYPE_HEADER, style_from="H2")
def mt(row, m, t):
    b.set(SP, "K%d" % row, m, style_from="F%d" % row)
    b.set(SP, "L%d" % row, t, style_from="F%d" % row)

# 1 異動別
b.set(SP, "D3", "4"); b.set(SP, "F3", 'Always "4"'); mt(3, "M", "Text")
# 2 保險證號
b.set(SP, "C4", "保險證號\n(8位數字)"); b.set(SP, "F4", LI_ID_8); mt(4, "M", "Text")
# 3 檢查碼
b.set(SP, "C5", "保險證號檢查碼"); b.set(SP, "F5", LI_CHECK); mt(5, "M", "Text")
# 4 健保投保單位代號
b.set(SP, "F6", NHI_UNIT); mt(6, "M", "Text")
# 5 投保別
b.set(SP, "G7", '"2": LI(EI), OAI, LP and NHI (勞(就)保/災保/勞退/健保);\n"3": NHI (健保);\n'
                '"4": OAI, LP and NHI (災保/勞退/健保) - field 27 is then mandatory.')
b.set(SP, "F7", 'Employee row: $hr.si_enrollment_code::key (2 or 4). Dependant row: "3" (as in the official sample) - '
                'TO BE CONFIRMED BY MOHIT/BA. Pay elements 58140/58120/2517/2560 are not used.')
mt(7, "M", "Text")
# 6 投保者
b.set(SP, "F8", 'Employee row: "1"; dependant row: "2". $hr.number_of_nhi_dependents = number of dependant rows to '
                'generate for the employee. 58212 (tax dependants) is not used.')
mt(8, "M", "Text")
b.set(SP, "G9", '※ If field 5 = "4" (OAI/LP/NHI), field 27 must be filled.\n'
                '※ NHI-only changes, or enrolment of foreign (外籍) employees (LI and NHI filed separately): file with NHIA.\n'
                '※ Pay below the minimum wage (e.g. part-time): fill the special identity (field 13).')
# 7 外籍
b.set(SP, "D10", "Y, 1, 2, L, blank")
b.set(SP, "G10", '"Y": Foreigner\n"1": Foreign spouse (incl. Hong Kong/Macau spouse)\n"2": Mainland Chinese spouse\n'
                 '"L": Permanent-resident foreign professional (永居外專)\nBlank: Taiwanese nationality')
b.set(SP, "F10", FOREIGN); mt(10, "C", "Text")
# 8 ID
b.set(SP, "C11", "被保險人身分證號\n(居留證統一證號/護照號碼)")
b.set(SP, "G11", "For Taiwanese, enter the national ID no.\nFor foreigners, enter the ARC unified ID no. or passport no.")
b.set(SP, "F11", ID_LI); mt(11, "M", "Text")
# 9 姓名
b.set(SP, "C12", "被保險人姓名"); b.set(SP, "G12", NAME_RULE); b.set(SP, "F12", NAME_MAP); mt(12, "M", "Text")
# 10 出生日期
b.set(SP, "F13", BIRTH); mt(13, "M", "Text")
# 11 月薪資總額
b.set(SP, "B14", "Monthly wage total\n[LI(EI)/OAI/LP]")
b.set(SP, "C14", "月薪資總額\n[勞(就)保/災保/勞退]")
b.set(SP, "G14", "Enter the monthly wage total")
b.set(SP, "G15", "※ BLI classifies it into the LI, OAI and LP band tables after receiving the file")
b.set(SP, "F14", "TO BE CONFIRMED BY MOHIT/BA: HR field holding the agreed monthly wage at hire (no payroll result "
                 "exists at the hire event); if none exists -> NEW DD FIELD (proposed): Monthly wage total at hire. "
                 "Must include all regular pay for work (base salary, monthly allowances incl. meal allowance, "
                 "attendance/performance bonuses) and exclude year-end/assessment bonuses, festival bonuses and "
                 "profit sharing (BLI page 0022929; NHIA insured-amount guide; LSA Enforcement Rules art. 10). "
                 "58008/58009/6220% are not used.")
mt(14, "M", "Numeric (integer)")
# 12 健保投保金額
b.set(SP, "B16", "Health Insurance Insured Amount"); b.set(SP, "C16", "健保投保金額")
b.set(SP, "F16", "$hr.nhi_grade::orLabel (same base as WTC 64550; pay element 58139 does not exist in WTC V2.8). "
                 "Validation: not lower than the LI/EI/OAI insured salary and the LP contribution wage "
                 "(BLI form 承表D instr. 9(3)).")
mt(16, "M", "Numeric (integer)")
# 13 特殊身分別
b.set(SP, "F17", "$hr.special_identity_code::key; blank if empty"); mt(17, "C", "Text")
# 14 勞基法特殊身分別
b.set(SP, "F18", "$hr.labor_standards_act_special_identity::key; blank if empty"); mt(18, "C", "Text")
# 15 眷屬身分證號
b.set(SP, "F19", "Dependant row: $hr.id_card_number_dependent_N (national dependants only); employee row: blank. "
                 "NEW DD FIELD (proposed): id_card_number_dependent_4..6 (DD V3.3 has ID/name/birthday for "
                 "dependants 1-3 but relationship for 1-6). Non-national dependants: TO BE CONFIRMED BY MOHIT/BA.")
mt(19, "C", "Text")
# 16 眷屬姓名
b.set(SP, "F20", "Dependant row: $hr.name_dependent_N; employee row: blank. NEW DD FIELD (proposed): "
                 "name_dependent_4..6."); mt(20, "C", "Text")
# 17 眷屬出生日期
b.set(SP, "F21", "Dependant row: " + roc("$hr.birthday_dependent_N") + "; employee row: blank. "
                 "NEW DD FIELD (proposed): birthday_dependent_4..6."); mt(21, "C", "Text")
# 18 稱謂代號
b.set(SP, "C22", "稱謂代號")
b.set(SP, "F22", "Dependant row: $hr.dependent_N_relationship::key (1-9); employee row: blank. The batch does not "
                 "accept 'P' (ward, present in the DD mapper): such dependants TO BE CONFIRMED BY MOHIT/BA.")
mt(22, "C", "Text")
# 19 健保業務組別
b.set(SP, "F23", NHI_DIV); mt(23, "M", "Text")
# 20 健保加保原因別
b.set(SP, "G24", 'Self:\n"1": Employment start\n"2": Union membership\nDependent:\n"4": Affiliated coverage\n'
                 '"5": Change in status\n"6": Marriage\n"7": Adoption\n"8": Newborn\n'
                 'Special cases (dependant transferred in, aged 18 or over, relationship = 3, 5, 7):\n'
                 '"S": Student without job\n"P": Under guardianship\n"A": Disabled & unable to work\n'
                 '"H": Seriously ill without job\n"G": Recent graduate or discharged soldier without job (within 1 year)')
b.set(SP, "F24", 'Employee row: "1" (到職起薪). Dependant row: $hr.adult_2_lineal_relatives_code_N::key (S, P, A, H, G) '
                 'when filled; otherwise NEW DD FIELD (proposed): NHI enrolment reason per dependant (4-8) - '
                 'TO BE CONFIRMED BY MOHIT/BA (proposal: "4").')
mt(24, "M", "Text")
# 21 健保加保原因發生日期
b.set(SP, "F25", "Employee row: " + roc("$hr.health_insurance_enrollment_start_date") + " - DD V3.3 types the "
                 "field as Text: TO BE CONFIRMED BY MOHIT/BA. Dependant row: NEW DD FIELD (proposed): date of the "
                 "dependant's enrolment reason.")
mt(25, "M", "Text")
# 22 性別
b.set(SP, "F26", "IF field 7 is not blank: IF(EQUALS($person.gender; 'male'); 'M'; 'F'); otherwise blank "
                 "(foreigners only). Replaces $hr.residential_status (tax residency).")
mt(26, "C", "Text")
# 23 提繳身分別
b.set(SP, "F27", "$hr.pension_contribution_identity::key (employee row only)"); mt(27, "C", "Text")
# 24 雇主提繳率(%)
b.set(SP, "B28", "Employer Contribution Rate (%)"); b.set(SP, "C28", "雇主提繳率(%)")
b.set(SP, "F28", "Rate as an integer % (e.g. 6). Object holding it: TO BE CONFIRMED BY MOHIT/BA (WTC 52537 = "
                 "DIVIDE($52537.amount;100), i.e. 0.06).")
mt(28, "C", "Numeric")
# 25 個人自願提繳率(%)
b.set(SP, "B29", "Personal Voluntary Contribution Rate (%)"); b.set(SP, "C29", "個人自願提繳率(%)")
b.set(SP, "F29", "Rate as an integer %; blank if 0. Object holding it: TO BE CONFIRMED BY MOHIT/BA (WTC 52517 = "
                 "DIVIDE($52517.amount;100)).")
mt(29, "C", "Numeric")
# 26 勞退提繳日期
b.set(SP, "F30", "Only if the LP contribution date differs from the LI enrolment date and is 1 to 6 days before the "
                 "filing date: " + roc("$hr.labor_pension_contribution_date") + "; otherwise blank. DD V3.3 types "
                 "the field as Text: TO BE CONFIRMED BY MOHIT/BA.")
mt(30, "C", "Text")
# 27 僅參加「災保」條件
b.set(SP, "B31", "OAI-only enrolment condition (Occupational Accident Insurance; insurance type 4 only)")
b.set(SP, "C31", "<勞工職業災害保險>\n僅參加「災保」條件\n(投保別-4專用欄位)")
b.set(SP, "G31", '"1": Already received the LI old-age benefit\n"2": Not received the LI old-age benefit and over 65\n'
                 'Blank: other cases. Mandatory when field 5 = "4".')
b.set(SP, "F31", 'IF field 5 = "4": $hr.received_social_insurance_benefits_type_occupational_accident::key; otherwise '
                 'blank. TO BE CONFIRMED BY MOHIT/BA: DD mapper key 2 reads "received other social insurance benefits '
                 'and over 65"; guide rev. 115.03.11 defines 2 as "not received the LI old-age benefit and over 65".')
mt(31, "C", "Text")

# ---- remove the withholding-tax tab
b.remove_sheet("New Specification")

b.save(OUT, log_json=str(pathlib.Path(__file__).resolve().parent / "edits_SR-107.json"))
print("saved", OUT, len(b.log), "edits")
