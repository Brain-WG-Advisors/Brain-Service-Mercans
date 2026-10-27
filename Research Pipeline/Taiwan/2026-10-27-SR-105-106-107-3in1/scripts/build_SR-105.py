"""SR-105 - TW SI electronic filing Salary Adjustment: base export 2026-10-27 -> v1.1.
Source of truth for field rules: NHIA/BLI 三合一批次薪資調整格式說明 (03_Adj3Of1, rev. 114.12.12)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from xlsxpatch import Book
from common import *
NAME_MAP = NAME_MAP.replace("<foreign field>", "field 6")

BASE = r"C:\Users\instituto\Documents\brain-service\raw\docs\drive-exports\2026-10-27\TW - SI electronic filing Salary Adjustment specification.xlsx"
OUT = pathlib.Path(__file__).resolve().parent.parent / "TW - SI electronic filing Salary Adjustment specification v1.1.xlsx"

b = Book(BASE)
VC, RM, SP = "Version Control", "Report Matrix", "Specification"

# ---- Version Control
b.set(VC, "B14", "1.1", num=True, style_from="B13")
b.set(VC, "C14", VC_DATE_SERIAL, num=True, style_from="C13")
b.set(VC, "D14", "Spec review against NHIA/BLI 3-in-1 batch salary adjustment format (03_Adj3Of1, rev. 114.12.12): "
                 "field mappings, C/M/O, data types and Report Matrix updated.",
      style_from="D13")
b.set(VC, "E14", VC_STATUS, style_from="E13")
b.set(VC, "F14", VC_BY, style_from="F13")

# ---- Report Matrix
b.set(RM, "B6", "Period")
b.set(RM, "B9", "Not prescribed by the official format guide (03_Adj3Of1, rev. 114.12.12).")
b.set(RM, "B11", ELECTRONIC)
b.set(RM, "B14", "Employees of a unit filing LI(+EI)/OAI, LP and NHI together (the guide applies to "
                 "勞(就)保/災保/勞退/健保 and 就保/災保/勞退/健保 units) whose monthly wage total (月薪資總額) "
                 "or NHI insured amount changes.")
b.set(RM, "B20", "Used to notify BLI and NHIA, in one Excel batch, of changes in the LI/EI/OAI insured salary, the LP "
                 "monthly contribution wage and the NHI insured amount. Wage changes Feb-Jul must be filed by the end "
                 "of August; Aug-Jan by the end of February; the new amounts apply from the 1st of the month after "
                 "filing (BLI form 承表S rev. 115.05, instr. 7; NHIA insured-amount guide).")
b.set(RM, "B22", "Electronic batch: Excel file uploaded in the NHIA multi-certificate online system "
                 "(申報批次勞健合一 EXCEL: enrolment, withdrawal, salary adjustment). The official guide (03_Adj3Of1, "
                 "rev. 114.12.12) defines only column order, values and notes: no start/end positions and no "
                 "official TXT layout. Salary reductions require supporting documents uploaded in the NHIA system "
                 "(NHIA East Division flyer). BLI may ask for the last 3 months' payroll records (承表S instr. 8).")

# ---- Specification
b.set(SP, "A1", "Format Explanation for 3-in-1 Batch Salary Adjustment (三合一批次薪資調整格式說明) - NHIA/BLI, "
                "revised 2025-12-12 (ROC 114.12.12). Applies to 勞(就)保/災保/勞退/健保 and 就保/災保/勞退/健保 units.")
# 1 異動別
b.set(SP, "D3", "M"); b.set(SP, "E3", "Text"); b.set(SP, "G3", "3"); b.set(SP, "L3", 'Always "3"')
# 2 保險證號
b.set(SP, "C5", "保險證號 (8位數字)")
b.set(SP, "D5", "M"); b.set(SP, "E5", "Text"); b.set(SP, "L5", LI_ID_8)
# 3 檢查碼
b.set(SP, "C7", "保險證號檢查碼 (1位英文字母)")
b.set(SP, "D7", "M"); b.set(SP, "E7", "Text"); b.set(SP, "L7", LI_CHECK)
# 4 健保投保單位代號
b.set(SP, "D9", "M"); b.set(SP, "E9", "Text"); b.set(SP, "L9", NHI_UNIT)
# 5 健保業務組別
b.set(SP, "D11", "M"); b.set(SP, "E11", "Text"); b.set(SP, "L11", NHI_DIV)
# 6 外籍
b.set(SP, "C18", "<外籍專用> 被保險人外籍")
b.set(SP, "D18", "C"); b.set(SP, "E18", "Text"); b.set(SP, "G18", "Y, 1, 2, L, Blank")
b.set(SP, "L18", FOREIGN)
b.set(SP, "M22", FOREIGN_L_NOTE, style_from="M21")
# 7 姓名
b.set(SP, "C23", "被保險人姓名")
b.set(SP, "D23", "M"); b.set(SP, "E23", "Text"); b.set(SP, "M23", NAME_RULE); b.set(SP, "L23", NAME_MAP)
# 8 ID (勞保)
b.set(SP, "C25", "被保險人身分證號 (居留證統一證號或護照號碼) (勞保專用)")
b.set(SP, "D25", "M"); b.set(SP, "E25", "Text"); b.set(SP, "L25", ID_LI)
# 9 ARC (健保)
b.set(SP, "C30", "被保險人居留證統一證號 (健保專用)")
b.set(SP, "D30", "C"); b.set(SP, "E30", "Text"); b.set(SP, "L30", ID_NHI)
# 10 出生日期
b.set(SP, "D34", "M"); b.set(SP, "E34", "Text"); b.set(SP, "G34", "YYYMMDD (ROC year)"); b.set(SP, "L34", BIRTH)
# 11 調後月薪資總額
b.set(SP, "B36", "Monthly wage total after adjustment [LI(EI)/OAI/LP]")
b.set(SP, "C36", "調後月薪資總額 [勞(就)保/災保/勞退]")
b.set(SP, "D36", "M"); b.set(SP, "E36", "Numeric (integer)")
b.set(SP, "M36", "Enter the monthly wage total after adjustment. BLI classifies it into the LI, OAI and LP band "
                 "tables after receiving the file.")
b.set(SP, "L36", "TO BE CONFIRMED BY MOHIT/BA: new interim pay element = average monthly wage total (月薪資總額) of "
                 "the 3 months before the adjustment (BLI page 0022929, item 2(1)). Include all pay received for work: "
                 "base salary, monthly allowances, meal allowance, overtime, attendance/performance/production "
                 "bonuses. Exclude year-end and assessment bonuses, festival bonuses and profit sharing (NHIA "
                 "insured-amount guide; LSA Enforcement Rules art. 10). Do not use 58008/58009/6220%: 58009 is "
                 "additional pay, 6220x are annual/referral bonuses, 58008 covers taxable recurring pay only.")
# 12 健保調前投保金額
b.set(SP, "B38", "Pre-adjustment NHI insured amount")
b.set(SP, "C38", "健保調前投保金額")
b.set(SP, "D38", "M"); b.set(SP, "E38", "Numeric (integer)")
b.set(SP, "L38", "TO BE CONFIRMED BY MOHIT/BA: $hr.nhi_grade::orLabel in force before the change (requires the "
                 "previous value / history of the HR field). Amount per the NHI insured-amount table.")
# 13 健保調後投保金額
b.set(SP, "B40", "Post-adjustment NHI insured amount")
b.set(SP, "C40", "健保調後投保金額")
b.set(SP, "D40", "M"); b.set(SP, "E40", "Numeric (integer)")
b.set(SP, "L40", "$hr.nhi_grade::orLabel (current value; same base as WTC 64550). Validation: not lower than the "
                 "LI/EI/OAI insured salary and the LP monthly contribution wage (BLI form 承表S instr. 6(3)).")
# 14 特殊身分別
b.set(SP, "D42", "C"); b.set(SP, "E42", "Text"); b.set(SP, "G42", "1, 2, 6, 7, 8, Blank")
b.set(SP, "L42", "$hr.special_identity_code::key when it is 1, 2, 6, 7 or 8; otherwise blank "
                 "(the batch accepts only these values, guide rev. 114.12.12).")
b.set(SP, "M44", 'For "Low-income occupational union member", enter "2"; "Awaiting ship onshore", "6"; '
                 '"Sheltered workers with disabilities", "7". If the pay is below the minimum wage (e.g. part-time), '
                 'the special identity must be filled.', style_from="M43")
# Note
b.set(SP, "A45", "NOTE (guide rev. 114.12.12, field 11): BLI classifies the monthly wage total into the band tables "
                 "after receiving the file. BLI checks whether the worker is an LP contributor; if not, no LP "
                 "contribution or LP wage adjustment is made. If the pay is below the minimum wage (e.g. part-time), "
                 "fill the special identity (field 14).\nThe 104.10.05 rule 'leave fields 2, 3 and 11 blank for an "
                 "NHI-only adjustment' is no longer in the guide: NHI-only adjustments TO BE CONFIRMED BY MOHIT/BA.")


# ================= ROUND 2 (independent review 2026-10-27, items 1, 2, 4, 5, 10) =================
# 1: fields 11-13 as Text (official sample: text, 6 digits with leading zero)
for r in (36, 38, 40):
    b.set(SP, "E%d" % r, "Text (official sample: 6 digits with leading zero, e.g. 040000; %s)" % TBC_LEN)
# 2: special identity field
b.set(SP, "L42", "$hr.special_identity_code::key when it is 1, 2, 6, 7 or 8; otherwise blank (the batch accepts only "
                 "these values, guide rev. 114.12.12). " + SPECIAL_ID_TBC)
# 4: Sample column (J, hidden in the base) - official fictitious sample 03_Adj3Of1 (row 2)
for r, v in [(3, "3"), (5, "01999999"), (7, "B"), (9, "000000000"), (11, "1"), (18, "Y"), (23, "ＤＡＶＩＤ"),
             (25, "W987654"), (30, "AB12345678"), (34, "0731215"), (36, "040000"), (38, "031800"), (40, "043900")]:
    b.set(SP, "J%d" % r, v)

b.save(OUT, log_json=str(pathlib.Path(__file__).resolve().parent / "edits_SR-105.json"))
print("saved", OUT, len(b.log), "edits")
