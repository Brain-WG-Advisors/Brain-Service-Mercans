"""SR-106 - TW SI Termination: base export 2026-10-27 -> v1.1.
Source of truth for field rules: NHIA/BLI 三合一批次退保格式說明 (02_Stop3Of1, rev. 114.12.12)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from xlsxpatch import Book
from common import *

BASE = r"C:\Users\instituto\Documents\brain-service\raw\docs\drive-exports\2026-10-27\TW - SI Termination specification.xlsx"
OUT = pathlib.Path(__file__).resolve().parent.parent / "TW - SI Termination specification v1.1.xlsx"

b = Book(BASE)
VC, RM, SP = "Version Control", "Report Matrix", "Spec"

# ---- Version Control
b.set(VC, "B9", "Taiwan")
b.set(VC, "B14", "1.1", num=True, style_from="B13")
b.set(VC, "C14", "2026-10-27", style_from="C13")   # C13 has no date format in this file -> ISO text
b.set(VC, "D14", "Spec review against NHIA/BLI 3-in-1 batch withdrawal format (02_Stop3Of1, rev. 114.12.12): "
                 "field mappings corrected, field 15 added, C/M/O, data types and Report Matrix updated.",
      style_from="D13")
b.set(VC, "E14", VC_STATUS, style_from="E13")
b.set(VC, "F14", VC_BY, style_from="F13")

# ---- Report Matrix
b.set(RM, "B11", ELECTRONIC)
b.set(RM, "B14", "Employees leaving whose LI(+EI)/OAI, LP and NHI are filed by the same unit (insurance type 2). "
                 "NHI-only withdrawals ($hr.insurance_coverage = 3) are filed with NHIA, not in this batch "
                 "(guide 02_Stop3Of1, rev. 114.12.12, field 6 and reminder).")
b.set(RM, "B22", "File on the separation date (離職當日). LI/EI coverage ends at 24:00 on the day the filing reaches "
                 "BLI; NHI ends at 24:00 on the day the withdrawal reason occurs (BLI form 承表L rev. 113.06, instr. 6). "
                 "Dependants' NHI is transferred out automatically: no dependant rows. LP: the filing date is taken "
                 "as the last LP contribution date; if different, file the LP stop form separately with BLI "
                 "(承表L note 3). Electronic batch: Excel upload in the NHIA multi-certificate system; the official "
                 "guide defines column order, values and notes only (no start/end positions, no official TXT layout).")

# ---- Spec: new columns J/K (C/M/O, Data Type)
b.set(SP, "J2", CMO_HEADER, style_from="H2")
b.set(SP, "K2", TYPE_HEADER, style_from="H2")
def mt(row, m, t):
    b.set(SP, "J%d" % row, m, style_from="F%d" % row)
    b.set(SP, "K%d" % row, t, style_from="F%d" % row)

# 1 異動別
b.set(SP, "D3", "2"); mt(3, "M", "Text")
# 2 保險證號
b.set(SP, "C5", "保險證號 (8位數字)"); b.set(SP, "F5", LI_ID_8); mt(5, "M", "Text")
# 3 檢查碼
b.set(SP, "C7", "保險證號檢查碼 (1位英文字母)"); b.set(SP, "F7", LI_CHECK); mt(7, "M", "Text")
# 4 健保投保單位代號
b.set(SP, "F9", NHI_UNIT); mt(9, "M", "Text")
# 5 健保業務組別
b.set(SP, "H11", NHI_DIV); mt(11, "M", "Text")
# 6 投保別
b.set(SP, "D18", "2")
b.set(SP, "F18", 'Always "2" (guide rev. 114.12.12 accepts only "2" = 勞(就)保/災保/勞退/健保). Employees with '
                 '$hr.insurance_coverage = 3 (NHI only) are excluded from this batch.')
b.set(SP, "G18", 'To withdraw "勞(就)保/災保/勞退/健保" (LI/EI, OAI, LP and NHI), enter "2".')
b.set(SP, "G19", 'Value "3" (NHI only) is no longer in the guide.')
b.set(SP, "G20", "NHI-only changes are filed separately with NHIA (guide reminder).")
mt(18, "M", "Text")
# 7 投保者
b.set(SP, "D22", "1"); mt(22, "M", "Text")
# 8 外籍
b.set(SP, "D24", "Y, 1, 2, L, Blank"); b.set(SP, "F24", FOREIGN)
b.set(SP, "G28", FOREIGN_L_NOTE, style_from="G27")
mt(24, "C", "Text")
# 9 姓名
b.set(SP, "C29", "被保險人姓名"); b.set(SP, "F29", NAME_MAP); b.set(SP, "G29", NAME_RULE); mt(29, "M", "Text")
# 10 ID (勞保)
b.set(SP, "C31", "被保險人身分證號"); b.set(SP, "C32", "(居留證統一證號或護照號碼)")
b.set(SP, "F31", ID_LI); mt(31, "M", "Text")
# 11 ARC (健保)
b.set(SP, "C36", "被保險人居留證統一證號"); b.set(SP, "F36", ID_NHI); mt(36, "C", "Text")
# 12 出生日期
mt(40, "M", "Text")
# 13 退保原因別
b.set(SP, "D44", "1, 2")
b.set(SP, "F44", "$hr.health_insurance_withdraw_reason_code::key (1 = withdrawal, 2 = transfer out). Default when "
                 "the HR field is empty: TO BE CONFIRMED BY MOHIT/BA (proposal: 2 for a resignation).")
mt(44, "M", "Text")
# 14 退保原因說明別
b.set(SP, "F47", "$hr.health_insurance_withdraw_reason_explanation::key (if field 13 = 1: M, E, U; if 2: 1, 2, 3, 4). "
                 "Default when empty: TO BE CONFIRMED BY MOHIT/BA (proposal: 1 = resignation).")
b.set(SP, "G50", 'For those who lost eligibility under NHI Act art. 8 or 9 (loss of nationality or household '
                 'registration moved out; residence permit expired), enter "U".')
mt(47, "M", "Text")
# 15 退保原因說明 (text)
b.set(SP, "B56", "Health insurance withdrawal reason description (text)")
b.set(SP, "C56", "健保退保原因說明")
b.set(SP, "F56", "Text derived from field 14: M -> 死亡; E -> 失蹤; U -> 喪失資格; 1 -> 離職; 2 -> 退休; "
                 "3 -> 停、歇業; 4 -> 退會 (short labels of the guide, not the mapper Local Value).")
mt(56, "M", "Text")
# 16 發生日期
b.set(SP, "F60", roc("$employee.last_working_date")); mt(60, "M", "Text")
# Note
b.set(SP, "A65", "NOTE (guide rev. 114.12.12): ※ When the insured person withdraws from NHI, all dependants are "
                 "transferred out; no dependant data is entered. ※ NHI Act art. 8: loss of nationality or household "
                 "registration moved out; art. 9: residence permit expired. ※ NHI-only changes are filed separately "
                 "with NHIA.")

b.save(OUT, log_json=str(pathlib.Path(__file__).resolve().parent / "edits_SR-106.json"))
print("saved", OUT, len(b.log), "edits")
