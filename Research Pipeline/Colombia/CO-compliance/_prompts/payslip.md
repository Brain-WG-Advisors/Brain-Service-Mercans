# Colombia PAYSLIP GENERATOR — v2.4 MERCANS 5-SHEET STANDARD

Build the Colombia Compliance Payslip Generator following the Mercans 8-sheet
standard. The Mozambique reference ALREADY contains these 8 sheets; the prior
pipeline mistakenly mandated a 5-sheet OUTPUT, dropping the setup guide, the
language-neutral master, and the field-option sheet. v2.7 outputs the full 8
and enforces a higher formatting + formula-hygiene bar (the Spain quality bar).

## APPROACH — copy the Mozambique 8-sheet reference and adapt

The proven pattern:

1. **Copy** the Mozambique reference workbook (8-sheet) as your base
2. **Preserve** its formatting exactly: navy title band, section headers in
   #A9A9A9 (white bold, centred), labels in #DCDCDC, green NET PAY highlight
   (#C6EFCE), Arial, merged header/section bands, full borders per section,
   column widths, the accounting number format
3. **Modify** values in place for Colombia content; rebuild the two language
   tabs and the master with Colombia fields

This inherits the visual standard rather than rebuilding formatting from scratch.

## INPUTS

1. **Master template:** ~/mercans-pipeline/shared/REFERENCE_Payslip_Mozambique.xlsx
   - 8-sheet reference (How-to, master, EN/local, spec, field option, ranges)
   - Will be the BASE that you copy and modify

2. **Reference for spec sheet structure:** ~/mercans-pipeline/shared/REFERENCE_Payslip_Tunisia.xlsx
   - Has the Payslip Spec sheet with HRP Mapping column layout
   - Use this for column structure of "Payslip Spec" and "Unit Rate Details"

3. **Mercans logo:** ~/mercans-pipeline/shared/mercans_logo.png
   - Already embedded in Mozambique template; preserve it

4. **Colombia content sources:**
   - CCG: ~/mercans-pipeline/CO-compliance/01-ccg/CO-CCG-001-v1.0.docx
     (Module 10.3 / equivalent for payslip mandatory components per labor code)
   - WTC: ~/mercans-pipeline/CO-compliance/02-wtc/CO-WTC-001-v1.0.xlsx
     (pick representative earnings/deductions for the visual payslip example)
   - DD: ~/mercans-pipeline/CO-compliance/05-data-dictionary/CO-DD-001-v1.0.xlsx
     (employee/employer fields)

## OUTPUT

Save as: ~/mercans-pipeline/CO-compliance/06-payslip/CO_Compliance_Payslip_Generator.xlsx

## 8-SHEET STRUCTURE — MANDATORY (v2.7)

The output workbook MUST have exactly these 8 sheets in this order:
1. How to set up Payslip      (setup instructions)
2. Compliance Payslip         (language-neutral MASTER template; pay-element
                               names shown as "XXXXX — earning/deduction/..." )
3. Colombia (EN)
4. Colombia (ES)
5. Payslip Spec
6. Field Option               (allowed values for coded fields, e.g. Salary
                               Type, Payment Method, Residential Status — keep
                               consistent with the DD option mappers)
7. Population Range
8. Unit Rate Details

NO standalone Payslip Spec file. The spec lives inside this workbook as a sheet.

## v2.7 FORMATTING & FORMULA REQUIREMENTS (enforced by C26)

Formatting tokens (match the Spain reference):
- Title band: navy fill, white bold ~15pt, merged across the sheet width.
- Section headers ("Employer", "Employee", "Earnings", "Deductions",
  "Employer contributions", "Leave balances", "YTD", "Statutory notes"):
  fill #A9A9A9, white, bold, centred, merged full width.
- Field labels / table column headers: fill #DCDCDC, bold.
- NET PAY row: fill #C6EFCE (green), bold; also show a NET PAY highlight near the
  title that references the net cell.
- Full thin borders on every info/table cell; merge label/value blocks so text
  is never clipped (a long employer address gets its own full-width row).

Currency / number format:
- Use the accounting format. For ZERO-MINOR-UNIT currencies (XAF, XOF, etc.)
  use the INTEGER variant (no decimals): _(* #,##0_);_(* \(#,##0\);_(* "-"??_);_(@_)
- For currencies WITH a minor unit, keep 2 decimals.

Formula hygiene (no manual-rework bugs):
- Totals are FORMULAS and appear ONLY on total rows:
    Gross = SUM(earnings amount range), Total deductions = SUM(...),
    Net = Gross_cell - Deductions_cell, Total employer = SUM(...),
    Leave Balance = Entitlement_cell - Taken_cell.
- Use ONE consistent amount column for SUM ranges (do not mix H:J vs H).
- NEVER put a CONCATENATE/total formula on a data row, and never duplicate a
  total. No #NAME?/#VALUE! literals anywhere.

## AUDIT CHECKS
- C26: all 8 sheets present in correct order; totals are formulas on total rows;
       zero-minor-unit currency uses the integer format; no fabricated/duplicated
       totals.
- C22: Payslip Spec has 5 sections (Header Details, Employer Fields,
       Employee Fields, Earnings Fields, Deductions Fields) with 20+ field rows total

### Sheet 1 — "Colombia (EN)"

Visual payslip in English. Sample employee using a typical Colombia name.

Layout — copy Mozambique (EN) structure exactly:
- Mercans logo top-left (preserved from template, do NOT remove)
- Title bar: navy #1F3864 fill, white "Colombia Payslip" text
- Pay period block (period start - end, pay date)
- Net Pay bar (navy #1F3864 fill, white text, prominent)
- Employer block (legal name, tax ID, address) with header gray #A9A9A9 fill
- Employee block (full name, ID, position, dept, etc.)
- Earnings section (gray header, light gray #F2F2F2 alternating rows)
- Deductions section (gray header)
- Employer contributions block (informative — light orange #FCE4D6)
- Leave balance table (statutory leave types for Colombia)
- Statutory notes (light gray #F2F2F2, italic, citing 2026 rates)
- Footer: "This document has been generated by Mercans Payroll System | © All rights reserved — Mercans"

Use realistic Colombia 2026 numbers:
- Mid-level professional salary in COP
- Calculate ALL deductions correctly at 2026 statutory rates from WTC
- Show correct gross-to-net with actual numbers

### Sheet 2 — "Colombia (ES)"

Identical layout to (EN) but with Spanish labels.
- Translate "Net Pay" → Spanish equivalent
- Translate section headers and field labels
- Currency formatting per Colombia convention (thousands separator, decimals)
- Same sample data, just Spanish labels

### Sheet 3 — "Payslip Spec"

The formal spec, embedded as a sheet. 4-column layout (matching Tunisia reference):

| Field Name (EN) | Field Name (Spanish) | HRP Mapping (TA & BA) | Field Explanation |

5 sections (section header rows in navy fill, white bold text):
1. Header Details (Payslip title, Company logo)
2. Employer Fields (legal name, tax ID, address, etc.)
3. Employee Fields (name, ID, position, etc.)
4. Earnings Fields (basic salary, overtime, allowances, etc. — from WTC)
5. Deductions Fields (SS contributions, income tax, etc. — from WTC)

HRP Mapping syntax (copy patterns from Tunisia reference):
- Single field: $entity.field → e.g. $legal_entity.name
- Concatenation: CONCAT($entity.f1, ', ', $entity.f2)
- Date format: DATE_FORMAT($entity.field, 'DD/MM/YYYY')
- Sum: SUM($payroll.earnings.*)
- Code series: (XXXXX:XXXXX) for WTC code ranges

Target ~25-35 field rows total across the 5 sections.
C22 requires all 5 sections + minimum 20 field rows total.

### Sheet 4 — "Unit Rate Details"

Map Colombia WTC earnings to rate/unit accounts. Column structure (from Tunisia):
- Earning Description (EN)
- Earning Code (from WTC)
- Rate Account
- Unit Account
- Notes

Cover at least the top 20 earnings codes from CO-WTC-001-v1.0.xlsx
(Basic Salary, Overtime, Family Allowance, Commissions, Bonuses, Leave Payments,
Severance, etc.)

### Sheet 5 — "Population Range"

3-column table:
| Worker Situation | Include? (YES/NO) | Notes |

Rows to cover (adjust to Colombia legal framework):
- Active employees (full-time) — YES
- Active employees (part-time) — YES
- New hires during period — YES
- Terminations during period — YES (per Colombia severance law)
- Sick leave — YES
- Maternity / paternity leave — YES
- Unpaid leave — YES
- Suspended employees — YES (if applicable)
- Pensioners receiving pension only — NO (no employment payslip)
- External contractors — NO (not payroll-managed)

## Colombia-SPECIFIC PAYSLIP CONTENT

Read CCG Module 10.3 for Colombia payslip mandatory items (per labour code).
Common requirements:
1. Employer identification (tax ID, name, address)
2. Employee identification (national ID, name, position)
3. Pay period
4. Each remuneration item separately
5. Each legal deduction separately
6. Each voluntary deduction with written authorisation
7. Net pay
8. SS institution names and rates
9. Worked days / absent days for the period

Pull current 2026 rates from WTC for the example.

## BUILD APPROACH

```python
import shutil
from openpyxl import load_workbook

# 1. Copy Mozambique template as starting point
shutil.copy(
    '/Users/wallissongomes/mercans-pipeline/shared/REFERENCE_Payslip_Mozambique.xlsx',
    '/Users/wallissongomes/mercans-pipeline/CO-compliance/06-payslip/CO_Compliance_Payslip_Generator.xlsx'
)

# 2. Open the copy
wb = load_workbook('/Users/wallissongomes/mercans-pipeline/CO-compliance/06-payslip/CO_Compliance_Payslip_Generator.xlsx')

# 3. Mozambique template ALREADY has 8 sheets — keep all of them:
#    "How to set up Payslip", "Compliance Payslip", "Mozambique (EN)",
#    "Mozambique (PT)", "Payslip Spec 1", "Field Option", "Population Range",
#    "Unit Rate Details".

# 4. Rename and modify values in place, preserving formatting/merges/images:
#    "Mozambique (EN)" → "Colombia (EN)"
#    "Mozambique (PT)" → "Colombia (ES)"
#    "Payslip Spec 1"  → "Payslip Spec"
#    Update the "Compliance Payslip" master (keep XXXXX pay-element placeholders),
#    "How to set up Payslip" (country touches), "Field Option" (country options),
#    "Population Range" and "Unit Rate Details".

# 5. v2.7 — DO NOT delete "How to set up Payslip", "Compliance Payslip" or
#    "Field Option". They are part of the required 8-sheet structure. (The old
#    pipeline deleted them, which is why prior payslips were incomplete.)

# 6. Verify sheet order matches the required 8-sheet layout:
#    How to set up Payslip, Compliance Payslip, Colombia (EN),
#    Colombia (ES), Payslip Spec, Field Option,
#    Population Range, Unit Rate Details

wb.save('/Users/wallissongomes/mercans-pipeline/CO-compliance/06-payslip/CO_Compliance_Payslip_Generator.xlsx')
```

## SELF-CHECK BEFORE SAVING

```python
from openpyxl import load_workbook
wb = load_workbook('/Users/wallissongomes/mercans-pipeline/CO-compliance/06-payslip/CO_Compliance_Payslip_Generator.xlsx')
expected = ['How to set up Payslip', 'Compliance Payslip', 'Colombia (EN)', 'Colombia (ES)', 'Payslip Spec', 'Field Option', 'Population Range', 'Unit Rate Details']
actual = wb.sheetnames
print(f"Expected: {expected}")
print(f"Actual:   {actual}")
assert actual == expected, f"Sheet mismatch! Expected {expected}, got {actual}"
ws = wb['Colombia (EN)']
if not getattr(ws, '_images', []):
    print("WARN: no embedded logo on EN sheet — branding via the navy title band is acceptable")
print("All checks pass")
```

Report back: final sheet names, logo present yes/no, row counts per sheet,
confirmation of save.
