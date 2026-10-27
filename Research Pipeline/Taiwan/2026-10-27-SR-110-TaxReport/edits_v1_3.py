# -*- coding: utf-8 -*-
"""SR-110 Taiwan Tax Report Spec v1.3 - cell edits (content in English).
Source abbreviations used in the cells:
  要點 114 = MOF Fiscal Information Agency, 綜合所得稅資料電子申報作業要點 (amended 2025-12-10, ROC 114)
             raw/docs/oficiais/TW/2026-10-27-綜合所得稅資料電子申報作業要點_1141210.pdf, Ch.2 Sec.1
  操作實務   = MOF, 各類所得扣免繳憑單網路申報操作實務 (raw/docs/oficiais/TW/2026-10-27-...pdf)
  ITA        = Income Tax Act (所得稅法) art. 92
Each entry: sheet -> {cell: (value, wrap)}; value str -> inline string, float -> number.
"""
import datetime

SRC = "要點 114"

EDITS = {
"Version Control": {
    "B14": (1.3, False),
    "C14": (float((datetime.date(2026, 10, 27) - datetime.date(1899, 12, 30)).days), False),
    "D14": ("Spec review (SR-110) against 綜合所得稅資料電子申報作業要點 (ROC 114 ed.): Mohit's 3 points reflected "
            "(resident YTD / non-resident per payment date; field 9 = tax withheld; income period by hire/termination month); "
            "serial, year, period, payment date, pension, country, treaty, TIN, name, address and file format rules corrected; "
            "open points marked TO BE CONFIRMED BY MOHIT/BA.", True),
    "E14": ("Draft", False),
    "F14": ("Wallisson Gomes", False),
},
"Report Matrix": {
    "B4": ("TO BE CONFIRMED BY MOHIT/BA", False),
    "B5": ("Resident (residential_status = 0): annual – file by 31 Jan of the following year (5 Feb if January has 3+ consecutive "
           "national holidays); certificate to the employee by 10 Feb (15 Feb). Non-resident (residential_status = 1): per payment "
           "date – tax paid and certificate filed within 10 days from the withholding date (+5 days if 3+ consecutive national "
           "holidays), not per calendar month. Src: ITA art. 92; " + SRC + " Ch.2 Sec.1 壹–貳.", True),
    "B7": ("TXT", False),
    "B8": ("Resident: {UBN 8}.{ROC year 3}.U8 (e.g. 00000123.114.U8). Non-resident: {UBN 8}.{payment date ROC yyymmdd 7}.U8 "
           "(e.g. 00000123.1150110.U8). UBN = $legal_entity_hr.company_registration_number. Src: 操作實務 p.5.", True),
    "B9": ("One file per UBN. Resident file: residential_status = 0, YTD of the tax year. Non-resident file: residential_status = 1, "
           "one file per payment date. One record per employee per income format (50, 93).", True),
    "B11": ("None – amounts in NT$ (TWD)", False),
    "B12": ("Whole NT$, no decimals, no negative amounts (fields 8, 9, 10, 20). Src: " + SRC + " items 8–10, 18(1).", True),
    "B13": ("| (pipe) – UTF-8; 32 fields per record (31 separators); empty field = adjacent separators, no padding spaces. "
            "Src: " + SRC + " Ch.2 Sec.1 參.二 and 參.三.(一).", True),
    "B14": ("Withholding and non-withholding statement (各類所得扣繳暨免扣繳憑單) for salary (format 50) and retirement income "
            "(format 93), filed electronically with the National Taxation Bureau: residents once a year, non-residents per payment.", True),
    "B16": ("v1.3 (2026-10-27): rules checked against 綜合所得稅資料電子申報作業要點 amended 2025-12-10 (ROC 114, latest edition found). "
            "File format: the official .U8 file must also contain the declaration records (各類所得扣繳暨免扣繳憑單申報書) and the payer "
            "basic data (申報單位基本資料), otherwise it is rejected (" + SRC + " 參.一); alternatively a CSV (Big5) can be converted/"
            "imported through the MOF IMX software, which generates them (操作實務 pp.41–46). TO BE CONFIRMED BY MOHIT/BA: full .U8 "
            "or CSV for IMX. Testing and Testing1 tabs = pre-v1.3 test record, not changed.", True),
},
"Spec": {
    "I7": ("Income format code (所得格式): 50 = salary income; 93 = retirement income (severance). Other format codes are not "
           "produced by this report. Src: " + SRC + " item 5.", True),
    "J9": ("[0] National individual.\n[1] Business organization.\n[3] Foreigner or mainland Chinese who stayed in Taiwan 183 days or more.\n"
           "[4] Taiwan branch of an enterprise with head office outside Taiwan.\n[5] Mainland Chinese who stayed in Taiwan fewer than 183 days.\n"
           "[6] Unit in the mainland area.\n[7] Foreigner (other than mainland Chinese) who stayed in Taiwan fewer than 183 days.\n"
           "[8] Legal person, body or other institution with head office outside Taiwan.\n[9] National individual who is not a resident.\n"
           "[A] Foreigner or mainland Chinese working 183 days or more on a Taiwan-flagged fishing vessel without a residence permit.\n"
           "Src: " + SRC + " item 7.", True),
    "H4": ("IF(EQUALS($hr.residential_status::key; '0'); LPAD($row_number; 8; '0'); CONCAT('00'; LPAD($row_number; 6; '0')))", True),
    "J4": ("Resident: positions 1–2 alphanumeric, 3–8 digits. Non-resident: positions 1–2 fixed \"00\", 3rd alphanumeric, 4–8 digits. "
           "Must not repeat for the same business number (UBN). Src: " + SRC + " item 2.\n"
           "TO BE CONFIRMED BY MOHIT/BA: zero-pad function name in the formula engine; whether the non-resident counter runs per file "
           "or per year for the same UBN.", True),
    "H10": ("Format 50 (salary): resident = YTD of CONTAINS($entry.account; RANGE('58008 + 58009 + 62200:62209')); non-resident = "
            "same accounts for the payment date only.\nFormat 93 (retirement/severance): resident = YTD of 62180:62182; non-resident = "
            "62180:62182 for the payment date. 6218x is reported under 93 only.\nTO BE CONFIRMED BY MOHIT/BA: whether 62200:62209 are "
            "already included in 58008 (double count) and that 6218x is not included in 58008/58009.", True),
    "K10": ("See H10 (v1.3). Previous: CONTAINS($entry.account; RANGE('58008 + 58009 + 62200:62209'))", True),
    "B11": ("Tax Withheld Amount", True),
    "H11": ("Format 50: resident = YTD of 2552 + 2572 + 2582 + 2592; non-resident = 2593 for the payment date.\n"
            "Format 93: resident = YTD of 2594.\n0 when nothing was withheld; never negative. Src: " + SRC + " item 9.\n"
            "TO BE CONFIRMED BY MOHIT/BA: account for format 93 paid to a non-resident.", True),
    "K11": ("Superseded in v1.3, see H11. Field 9 is the tax withheld (扣繳稅額), not an exemption. Previous mapping "
            "CONTAINS($entry.account; RANGE('58100 + 58105')): 58100 = Meal Allowance Pre-Tax Deduction; 58105 does not exist in WTC V2.8.", True),
    "H12": ("Field 8 − Field 9 (Total Payment − Tax Withheld Amount); must match exactly; never negative. "
            "Src: " + SRC + " 參.三.(三) note 1, item 10.", True),
    "D13": ("Alphanumeric(12)", False),
    "J13": ("Employee staff ID; max 12 characters (official type X, length 12). Src: " + SRC + " item 11(9).", True),
    "H18": ("Resident: SUBTRACT(DATE_FORMAT($meta.as_of_date; 'yyyy'); 1911), as_of_date inside the tax year reported.\n"
            "Non-resident: SUBTRACT(DATE_FORMAT(<payment date>; 'yyyy'); 1911).\n"
            "TO BE CONFIRMED BY MOHIT/BA: system variable for the payment date.", True),
    "J18": ("ROC year (3 digits) in which the income was paid (所得給付年度); ROC year = Gregorian year − 1911 (113 = 2024). "
            "Src: " + SRC + " item 14.", True),
    "H19": ("$employee_name: Chinese name if the employee has one (at least 2 Chinese characters); foreigner without a Chinese name: "
            "English name as in the passport (first 50 characters). Trim leading/trailing spaces; all full-width or all half-width; max 50.\n"
            "TO BE CONFIRMED BY MOHIT/BA: DD field holding the Chinese name (DD V3.3 has no dedicated field).", True),
    "J19": ("Chinese names: at least 2 characters, no spaces before, after or between characters (rare character = full-width "
            "underscore). Foreigner without a Chinese name: passport English name. Src: " + SRC + " item 15 and 參.三.(三) note 2.", True),
    "H20": ("CONCAT($hr.employee_postcode; $hr.taiwan_city; $hr.district; $address.address_line_1; $address.address_line_2) with no "
            "separators or commas, so the first 3 characters are the postcode digits. Household-registration (戶籍) address. Foreigner or "
            "mainland Chinese without a Chinese address: employer address. Max 100 characters (if longer, omit 鄰/里). All full-width or "
            "all half-width.\nTO BE CONFIRMED BY MOHIT/BA: variable for the employer address.", True),
    "J20": ("First 3 characters: postcode in Arabic numerals or the county/city name. Principle: household-registration address; "
            "foreigner without a Chinese address: employer address. Src: " + SRC + " item 16 and 參.三.(三) note 2.", True),
    "H21": ("Resident: CONCAT(YYY; IF(hire date in the tax year; MM of hire date; '01'); YYY; IF(termination date in the tax year; "
            "MM of termination date; '12')), YYY = tax year − 1911.\nNon-resident: CONCAT(YYY; MM; YYY; MM) of the month the paid income "
            "relates to (e.g. 1150111501).\nTO BE CONFIRMED BY MOHIT/BA: system variables for hire and termination dates.", True),
    "J21": ("10 digits YYYMMYYYMM: start and end ROC year (3) and month (2) of the period the income belongs to (所得所屬期間); "
            "year-month, not dates. Src: " + SRC + " item 17.", True),
    "H22": ("Format 50 only: resident = YTD of 2517 (LPN EE, employee voluntary labor pension contribution); non-resident = 2517 for "
            "the payment date; 0 or blank if none. Format 93: blank.", True),
    "J22": ("Amount contributed under the labor / civil-service pension laws that is not counted as taxable salary "
            "(依勞工、軍公教及政務人員退撫相關法令提(撥)繳(不計入薪資課稅)之金額); NT$, max 12 digits, not negative; non-salary income: "
            "0 or blank. Src: " + SRC + " item 18(1).", True),
    "K22": ("Superseded in v1.3, see H22. Previous: 'Resident: 58160 take YTD value / Non-resident (monthly): 58160' "
            "(58160 = Severance Base Before Exemption); H22 used $58105, which does not exist in WTC V2.8.", True),
    "H30": ("IF(CONTAINS($hr.identity_type; LIST('3'; '5'; '6'; '7'; '8'; '9'; 'A')); IF(IS_NULL(<country of residence>); 'ZZ'; "
            "<country of residence>); '')\nTO BE CONFIRMED BY MOHIT/BA: field for the country of residence (the address country may be "
            "the Taiwan address) and that its key matches the code list in Annex 41.", True),
    "J30": ("ID types 3, 5, 6, 7, 8, 9, A: 2-letter code of the country/region of residence (Annex 41); 'ZZ' only when it cannot be "
            "determined. Other ID types: blank. Src: " + SRC + " item 22.", True),
    "H31": ("'' (blank) by default. ID types 5–9 with a tax treaty applied: 2-character treaty code from Annex 42 ('XX' is not a valid "
            "code).\nTO BE CONFIRMED BY MOHIT/BA: DD field for the treaty code (none in DD V3.3).", True),
    "J31": ("ID types 5, 6, 7, 8, 9: treaty code (Annex 42) or blank. Other ID types: blank. Src: " + SRC + " item 23.", True),
    "H33": ("IF(EQUALS($hr.residential_status::key; '0'); DATE_FORMAT($report.generation_time; 'MMdd'); DATE_FORMAT(<payment date>; 'MMdd'))\n"
            "TO BE CONFIRMED BY MOHIT/BA: system variable for the payment date.", True),
    "J33": ("MMDD. Resident: file production date. Non-resident: payment date. Src: " + SRC + " item 25.", True),
    "H34": ("IF(CONTAINS($hr.identity_type; LIST('3'; '5'; '6'; '7'; '8'; '9'; 'A')); IF(IS_NULL(<foreign TIN>); 'NOTIN'; <foreign TIN>); '')\n"
            "TO BE CONFIRMED BY MOHIT/BA: DD field for the TIN in the country of residence (none in DD V3.3).", True),
    "J34": ("ID types 3, 5, 6, 7, 8, 9, A: tax identification number of the recipient in the country/region of residence; if there is "
            "no TIN, fill in [NOTIN]. Other ID types: blank. Src: " + SRC + " item 26.", True),
    "K34": ("Superseded in v1.3, see H34. Previous: 'Blank: Taiwanese employee / NORTIN: foreign employee' (the value is NOTIN and it "
            "depends on the ID type, not on residential status).", True),
    "L34": ("Superseded in v1.3, see H34 (NOTIN, by ID type).", True),
},
}

# ---------------------------------------------------------------------------
# Round 2 (2026-10-27): independent review findings 1-9 (REVISAO-independente.md).
# Values below replace/add to the round-1 entries; the build still starts from the base export.
R2 = {
"Version Control": {
    "E14": ("Under Review", False),
},
"Spec": {
    # 1. serial: no collision resident x non-resident in the same UBN
    "H4": ("IF(EQUALS($hr.residential_status::key; '0'); CONCAT('01'; LPAD($row_number; 6; '0')); "
           "CONCAT('00'; LPAD(<non-resident serial counter per UBN in the year>; 6; '0')))", True),
    "J4": ("Resident: positions 1–2 alphanumeric, 3–8 digits; prefix '01' (never '00', which is reserved for non-residents; "
           "no letters in position 1, which is reserved for the file ID code A–Y). Non-resident: positions 1–2 fixed \"00\", 3rd "
           "alphanumeric, 4–8 digits; the counter must not restart per payment-date file. A serial must not repeat for the same "
           "business number (UBN). Src: " + SRC + " item 2 (PDF p.24).\n"
           "TO BE CONFIRMED BY MOHIT/BA: zero-pad function name; variable for the non-resident counter per UBN in the year.", True),
    # 2. name/address width
    "H19": ("Chinese name (if held): whole string converted to full-width, trimmed, at least 2 Chinese characters, max 50. "
            "Otherwise passport English name ($employee_name): whole string half-width, trimmed, first 50 characters. "
            "Never mix full- and half-width in the field.", True),
    "J19": ("Chinese names: at least 2 characters, no spaces before, after or between characters (rare character = full-width "
            "underscore). Foreigner without a Chinese name: passport English name. The field must be all full-width or all "
            "half-width. Src: " + SRC + " item 15 (PDF p.29) and 參.三.(三) note 2 (PDF p.32).\n"
            "TO BE CONFIRMED BY MOHIT/BA: DD field holding the Chinese name (DD V3.3 has none); full-/half-width conversion "
            "function in the formula engine.", True),
    "H20": ("FULLWIDTH(CONCAT($hr.employee_postcode; $hr.taiwan_city; $hr.district; $address.address_line_1; "
            "$address.address_line_2)): whole string converted to full-width, postcode digits included (e.g. １００), no separators "
            "or commas; first 3 characters = postcode. Household-registration (戶籍) address. Foreigner or mainland Chinese without a "
            "Chinese address: employer address, same conversion. Max 100 characters (if longer, omit 鄰/里).", True),
    "J20": ("First 3 characters: postcode in Arabic numerals or the county/city name. The field must be all full-width or all "
            "half-width. Principle: household-registration address; foreigner without a Chinese address: employer address. "
            "Src: " + SRC + " item 16 (PDF p.29) and 參.三.(三) note 2 (PDF p.32).\n"
            "TO BE CONFIRMED BY MOHIT/BA: FULLWIDTH function name in the formula engine; variable for the employer address.", True),
    # 3. field 5 mapping + alignment
    "H7": ("One record per employee per income format:\n'93' = retirement income: accounts 62180:62182 (Severance Payment; the "
           "only PEs with Severance Tax = Yes in WTC V2.8);\n'50' = salary: all other taxable accounts of H10.\n"
           "An employee with both in the period gets two records (one 50, one 93).", True),
    "J7": ("50 = salary income (薪資所得); 93 = retirement income (退職所得: pension, severance, retirement/leaving payments, "
           "ITA art. 14 cat. 9). Src: " + SRC + " item 5 (PDF pp.24–26).\n"
           "TO BE CONFIRMED BY MOHIT/BA: 62640:62649 'Pension' and 62930 'Gratuity/EOS/Post-termination' are taxed by table in "
           "WTC V2.8; if they are retirement/leaving payments they belong to format 93, not 50.", True),
    "H10": ("Format per H7.\nFormat 50 (salary): resident = YTD of CONTAINS($entry.account; RANGE('58008 + 58009 + 62200:62209')); "
            "non-resident = same accounts for the payment date only.\nFormat 93 (retirement/severance): resident = YTD of "
            "62180:62182; non-resident = 62180:62182 for the payment date. 6218x is reported under 93 only.\n"
            "TO BE CONFIRMED BY MOHIT/BA: whether 62200:62209 are already included in 58008 (double count) and that 6218x is not "
            "included in 58008/58009.", True),
    "H11": ("Format per H7.\nFormat 50: resident = YTD of 2552 + 2572 + 2582 + 2592; non-resident = 2593 for the payment date.\n"
            "Format 93: resident = YTD of 2594.\n0 when nothing was withheld; never negative. Src: " + SRC + " item 9.\n"
            "TO BE CONFIRMED BY MOHIT/BA: account for format 93 paid to a non-resident.", True),
    "H22": ("Format per H7. Format 50 only: resident = YTD of 2517 (LPN EE, employee voluntary labor pension contribution); "
            "non-resident = 2517 for the payment date; 0 or blank if none. Format 93: blank.", True),
    # 5.
    "I22": ("Employee voluntary labor pension contribution not counted as taxable salary; salary records (format 50) only, "
            "blank for retirement income (93).", True),
    # 6.
    "L10": ("Superseded in v1.3, see H10. Previous: 'Resident: Annual taxable amount / Non-resident: Monthly taxable amount' "
            "(non-resident is per payment date, not monthly).", True),
    "L11": ("Superseded in v1.3, see H11. Previous: 'Withheld tax amount. Resident: annual tax amount. Non-resident: monthly tax "
            "amount' (non-resident is per payment date, not monthly).", True),
    # 7.
    "G31": ("(blank)", False),
    # 8. official type X
    "D18": ("Alphanumeric(3)", False),
    "D21": ("Alphanumeric(10)", False),
    "D28": ("Alphanumeric(1)", False),
    "D33": ("Alphanumeric(4)", False),
    # 9.
    "J5": ("8-digit UBN. Refer to " + SRC + " Ch.2 Sec.1 item 3 (PDF p.24) and the check method in Annex 7 / 7-1 (PDF pp.188–189).", True),
    "J8": ("Refer to " + SRC + " Ch.2 Sec.1 item 6 (PDF p.27) and the check method in Annex 6 / 6-1 (PDF pp.186–187).", True),
},
}
for _sh, _cells in R2.items():
    EDITS.setdefault(_sh, {}).update(_cells)
