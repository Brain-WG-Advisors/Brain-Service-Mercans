# Colombia (CO) PAYSLIP GENERATOR — SPAIN-REFERENCE FORMAT, FY2026

Build the Colombia Compliance Payslip Generator by copying the ACTUAL Spain
production workbook and adapting its country-specific sheets to Colombia.
This is the real 8-sheet format currently in production use.

## APPROACH — copy Spain, then modify in place

```python
import shutil
shutil.copy(
    "/c/Users/Wallison Gomes/mercans-pipeline/shared/REFERENCE_Payslip_Spain.xlsx",
    "/c/Users/Wallison Gomes/mercans-pipeline/CO-compliance/06-payslip/CO_Compliance_Payslip_Generator.xlsx"
)
```

Open the COPY with openpyxl. Modify ONLY the sheets/cells described below.
Everything else (fonts, fills, merges, column widths, row heights, the
embedded Mercans logo image, print/page setup) must be preserved exactly.

## RESEARCH REQUIREMENTS — do this BEFORE writing any content

You must research Colombia's FY2026 payroll compliance via web search,
citing primary/authoritative sources (tax authority, social security
authority, ministry of labour, official gazette — not blogs or accounting
firm marketing pages). At minimum, establish and cite the legal basis for:

1. **Currency**: confirm COP is correct (ISO 4217).
2. **Income tax**: system type (flat/progressive), current FY2026 rate(s)
   or bracket structure, any standard deduction/allowance.
3. **Social security / payroll contributions**: employee and employer rates,
   any contribution ceiling/floor, which authority administers it, whether
   it is single-fund or split across multiple schemes (pension, health,
   unemployment, work injury, etc. — do not assume Spain's multi-fund
   structure applies; research Colombia's actual structure).
4. **Any additional mandatory payroll tax** (e.g. a training levy, solidarity
   contribution, or similar) if one exists in Colombia.
5. **Minimum wage** (current FY2026 figure).
6. **Statutory leave**: annual leave minimum, sick leave (who pays which
   days), maternity/paternity leave duration and funding.
7. **Payslip legal requirement**: what does Colombia's labour code /
   wage payment law actually require the employer to disclose to the
   employee at each payment? Cite the specific article/law.
8. **Local identifiers**: the correct local terminology for (a) employer
   tax/registration number, (b) employee tax ID number — do NOT borrow
   Spain's NIF/CIF or DNI/NIE labels; use Colombia's actual equivalents.

Flag anything you cannot verify confidently as [VERIFY WITH RA] with your
best-effort value already filled in — never leave a field blank or write
"TBD"/"to be confirmed".

No CCG file available — research Colombia's labour code / wage payment law directly (see RESEARCH REQUIREMENTS below) for mandatory payslip content.
No DD available — use the standard employee/employer master-data field set (name, position, hire date, local tax ID, employer registration number, etc.), researching the CORRECT local terminology for Colombia (see RESEARCH REQUIREMENTS below).

## SHEETS — 8 total, exact order: "How to set up Payslip", "Compliance Payslip", "Colombia (EN)", "Colombia (ES)", "Payslip Spec 1", "Field Option", "Population Range", "UnitRate Account Details"

1. **"How to set up Payslip"** — generic, shared across every country. LEAVE
   UNTOUCHED. Contains placeholder Estonia/Mozambique example data unrelated
   to Colombia — do not read it as a content source.
2. **"Compliance Payslip"** — same, generic example sheet, LEAVE UNTOUCHED.
3. Build TWO visual payslip sheets: "Colombia (EN)" (renamed from Spain (EN)) and "Colombia (ES)" (renamed from Spain (ES), fully translated into Spanish — every label genuinely translated, not left in English; Spain's own (ES) sheet left some labels untranslated by mistake, do not repeat that).
4. **"Payslip Spec 1"** — field-level spec, rebuilt for Colombia (9 sections,
   same layout Spain uses: Header Details | Employer Fields | Employee Fields
   | Earning | Deductions & Net Field | Net Pay | Employer Contribution |
   Banking Details | Footer Details. Columns: Field Name | Field Local Name
   | HRB Mapping | Field Explanation (RA) | Query to RA (leave blank — fresh
   build). No CO WTC file is available for this build. Use the SAME 'XXXXX - ' placeholder convention Spain's own visual sheets already use for wage type labels. In the Payslip Spec 1 sheet's HRB Mapping column, write plausible Mercans-style account-series placeholders in the same notation Spain uses (numeric series ranges), and mark every such line explicitly as [VERIFY WITH RA — align to actual CO-WTC account codes once available]. This does not affect the accuracy of the legal/statutory content, only the internal Mercans code numbers, which are illustrative until the real WTC exists.
5. **"Field Option"** — row 2: CURRENCY | COP | (currency full name) |
   Displayed currency in payslip summary and banking section.
6. **"Population Range"** — same 3-column format (Worker Situation | Include?
   YES/NO/CONDITIONAL | Notes). Cover: active full-time, active part-time,
   new hires, terminations, sick leave (with Colombia's actual employer-pay
   vs state-pay day split), maternity/paternity leave, unpaid leave, foreign
   workers, board members/directors, contractors/self-employed (excluded,
   note why). Add any Colombia-specific situation your research surfaces.
7. **"UnitRate Account Details"** — No WTC available — populate with illustrative earning categories (Basic Salary, Overtime, common allowances for Colombia) using placeholder rate/unit account numbers in Spain's numeric-range style, flagged [VERIFY WITH RA] for real account number alignment once the CO-WTC exists.

## QUALITY BAR

The Spain reference has two known imperfections — do NOT repeat either:
- **Leftover residue**: grep every cell you write for "MZN", "Mozambique",
  "Estonia", "Spain", "EUR" (unless COP is genuinely EUR), "EID-",
  "jdoe@" and remove all of it. No leftover artifacts from the template.
- **Incomplete translation**: if building a local-language sheet, EVERY
  label must be genuinely translated — do not leave any English labels
  behind on the local sheet.

No "TBD" / blank placeholder markers may remain anywhere in the file.
Minimum accuracy bar: 95% on statutory content, grounded in the research
above with citations. Wage-type codes may be illustrative placeholders per
the WTC instruction — that does not count against the accuracy bar.

## FIELD-BY-FIELD MAPPING — visual payslip sheet(s)

Mirror the row/section skeleton the Spain copy already gives you.

- **Title**: "Colombia Payslip"
- **Net Pay quick-view**: keep layout, currency = COP, remove all residue.
- **Employer block**: Employer Name, Employer Address, and Colombia's actual
  employer tax/registration identifier (researched above, not Spain's NIF/CIF).
- **Employee block**: Employee Name, Employee Code, Job Title, Department,
  Hire Date, Last Working Date, Completed Years in Service, Colombia's
  actual employee tax ID (researched above, not Spain's DNI/NIE), Days in Month.
- **Salary Detail / Earnings**: No CO WTC file is available for this build. Use the SAME 'XXXXX - ' placeholder convention Spain's own visual sheets already use for wage type labels. In the Payslip Spec 1 sheet's HRB Mapping column, write plausible Mercans-style account-series placeholders in the same notation Spain uses (numeric series ranges), and mark every such line explicitly as [VERIFY WITH RA — align to actual CO-WTC account codes once available]. This does not affect the accuracy of the legal/statutory content, only the internal Mercans code numbers, which are illustrative until the real WTC exists.
- **Deductions**: every mandatory employee-side withholding you researched
  (income tax, employee social security share, any other statutory
  deduction) as SEPARATE lines — never merge distinct legal deductions.
- **Net Pay**: Total Earnings minus all employee deductions.
- **Employer Contribution**: every employer-side statutory contribution you
  researched, matching Colombia's actual fund/scheme structure (do not
  assume it matches Spain's multi-fund breakdown or Ukraine's single-fund
  structure — use what you actually found for Colombia).
- **Banking details**: Beneficiary name, account/IBAN in Colombia's actual
  format, Currency = COP.
- **Footer**: same Mercans footer text as Spain (translated on the local sheet if one exists).
- **Statutory Notes section**: rewrite entirely for Colombia using your
  research, citing the specific laws/articles by name and number, matching
  Spain's citation density.

## SELF-CHECK BEFORE SAVING

```python
from openpyxl import load_workbook
path = "/c/Users/Wallison Gomes/mercans-pipeline/CO-compliance/06-payslip/CO_Compliance_Payslip_Generator.xlsx"
wb = load_workbook(path)
expected = ["How to set up Payslip", "Compliance Payslip", "Colombia (EN)", "Colombia (ES)", "Payslip Spec 1", "Field Option", "Population Range", "UnitRate Account Details"]
actual = wb.sheetnames
assert actual == expected, f"Sheet mismatch! {actual}"
ws = wb["Colombia (EN)"]
assert len(ws._images) > 0, "Logo missing on Colombia (EN) sheet"
residue_terms = ["MZN", "Mozambique", "Estonia", "Spain", "EID-1337", "jdoe@mercan"]
for sheet_name in wb.sheetnames:
    if sheet_name in ("How to set up Payslip", "Compliance Payslip"):
        continue
    s = wb[sheet_name]
    for row in s.iter_rows():
        for cell in row:
            if cell.value and any(term in str(cell.value) for term in residue_terms):
                raise AssertionError(f"Residue '{cell.value}' found at {sheet_name}!{cell.coordinate}")
print("All structural checks pass.")
```

## REPORT BACK — verdict first, no hedging

1. **Verdict**: READY_FOR_HANDOVER or BLOCKED (with the specific blocker)
2. **Accuracy self-assessment**: honest % for the legal/statutory content,
   with primary sources cited for each major rate/rule
3. **Wage-type codes**: real (from WTC) or illustrative placeholder
4. **[VERIFY WITH RA] items remaining**: list each with best-effort value
   already filled in (never blank)
5. **Residue check result**
6. **File location and size**
