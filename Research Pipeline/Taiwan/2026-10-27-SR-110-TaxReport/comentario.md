# SR-110: rascunho de comentário (EN). NÃO postado

> Para o usuário revisar. Anexo só depois do ok: `Taiwan Tax Report Spec_v1.3.xlsx` (changed cells in light blue).

---

@mjain Spec review done against the MOF e-filing rules (綜合所得稅資料電子申報作業要點, Dec 2025 edition); spec v1.3 attached, changes in light blue.

**Verdict:** your 3 points are right, but none of them was in the spec yet. They are now in, along with the other gaps. Not ready for development until the open points below are answered.

**Changes**
1. Resident = YTD for the tax year, one file a year. Non-resident = one file **per payment date**, not per calendar month (file name, serial starting "00", field 31 = payment date, year = payment year).
2. Field 9 is the **tax withheld**, not an exemption: renamed "Tax Withheld Amount" and mapped per column P (2552+2572+2582+2592 YTD; 2594 for format 93; 2593 non-resident). The old mapping 58100+58105 is why it was not coming.
3. Period: resident = hire month (or 01) to termination month (or 12); non-resident = YYYMMYYYMM of the month paid (year-month, not dates).
4. Also corrected: voluntary pension = 2517 (58105 does not exist); country code blank unless ID type 3/5/6/7/8/9/A; treaty code blank instead of "XX"; TIN "NOTIN" by ID type; address starts with the postcode; ID type list; file format (UTF-8, "|", 32 fields) and file name.

**Questions**
1. Do we generate the full .U8 (with the declaration and payer records) or a CSV to import into IMX?
2. Are 62200:62209 already inside 58008 (double count)?
3. Which system fields hold the payment date, hire/termination dates, Chinese name, country of residence, foreign TIN and treaty code? Marked "TO BE CONFIRMED BY MOHIT/BA" in column H.
4. Which tax account applies when format 93 (severance) is paid to a non-resident?

@manjitbali could you share the current output after your January changes?
