# Colombia WAGE TYPE CATALOGUE — CZ V2.0 + GLOBAL WTC BASELINE

You are building the Colombia Wage Type Catalogue using the CZ V2.0 template format.

## STEP 1: READ THE GLOBAL WTC BASELINE FIRST
Open: ~/mercans-pipeline/shared/Global_WTC_V1_0.xlsx
This has ~300 standard global wage type codes and descriptions.
These are the BASELINE. They have codes and names ONLY — ZERO configuration.
You MUST configure every included wage type fresh for Colombia.
The same wage type has completely different tax/SS treatment in different countries.

ALL ~300 global codes are MANDATORY — include every single one. Do NOT exclude
any global code. Every country must have all global codes. The ONLY thing that
changes per country is the taxability configuration.

For each global code:
- Configure it fully for Colombia 2026 tax/SS rules
- Do NOT skip it — every code must appear in the WTC

## STEP 2: ADD Colombia-SPECIFIC WAGE TYPES
Research Colombia-specific types not in the global list:
- Colombia-specific allowances and benefits
- Colombia-specific SS fund contribution types
- Any locally-named statutory payments

## FORMAT REFERENCE
Load: ~/mercans-pipeline/shared/_CZ_Wage_Type_Catalogue_V2_0.xlsx
Do NOT create a new Workbook(). Load CZ file, clear data rows, populate
preserving all formatting.

## 5 SHEETS IN OUTPUT (4 from CZ template + 1 new)
1. Version Control
2. Wage Type Catalogue (main sheet)
3. Employer Sick Pay (if applicable in Colombia)
4. Tax Credit (if applicable in Colombia)
5. Global WTC Coverage (NEW — confirm all ~300 global codes included +
   list any Colombia-specific additions beyond the global baseline)

## v2.4 — Form Reference Guide (C17)
Add a 6th sheet: "Form Reference Guide"
Maps every wage type category to its target row in each statutory report.
Columns: Wage Type Category | Spec File | Sheet Name | Row Number | Notes
This is mandatory per v2.4 C17 check. Build by cross-referencing your wage type
categories against the spec files in 04-reports-spec/.

## COLUMN RULES
POPULATE ONLY BLUE columns. Leave ORANGE empty.

Wage Type Catalogue columns:
A: Mercans Code ORANGE | B: Name EN BLUE | C: Name Local (Spanish) BLUE
D: Explanation ORANGE | E: Category BLUE (Earning/Deduction/Base/Employer Contribution/Flag/Intermediary/Notional/Tax/Percentage)
F: Formula BLUE (plain text with 2026 rates) | G: Tax Code BLUE | H-I: ORANGE
J: Occurrence BLUE (Recurring/Additional/NA) | K-M: ORANGE
N: Subject to Tax BLUE (Yes/No/Yes-No/NA)
O: Table Tax BLUE (Yes/No/Yes-No/NA)
P: Special Tax BLUE (Yes/No/Yes-No/NA)
Q: Subject to Social Insurance BLUE (Yes/No/Yes-No/NA)
R: Subject to Pension BLUE (Yes/No/Yes-No/NA)
S-T: ORANGE

## SS FUND EXPANSION
If Colombia has multiple distinct SS funds, expand Q-R into per-fund columns:
- Q1: Subject to [Fund 1 Name]
- Q2: Subject to [Fund 2 Name]
- Q3: Subject to [Fund 3 Name] etc.
- R: Subject to Pension
Same BLUE formatting, same Yes/No/Yes-No/NA dropdowns.
Research Colombia SS fund structure from CCG Module 5.

## CONFIGURATION REQUIREMENTS
For EACH wage type, research Colombia 2026 rules specifically:
- Exact formula with 2026 rates/thresholds in COP
- Subject to income tax? Which type? (table rate / flat rate / exempt)
- Subject to each SS fund? Any contribution ceiling?
- Any special tax treatment (exempt amount, benefit-in-kind valuation method)?

DO NOT copy treatment from other countries. Research Colombia specifically.

## v2.4 — TAX CODE VERIFICATION (C9)
Every tax code in WTC must be verified against the country's specific tax
authority publication. Add a column or note for the official source of each
tax code. Never guess or copy from another country.

## v2.5 — POST-GENERATION VALIDATION CHECKLIST (C3)

Before saving the final WTC, verify in code:

```python
import json, openpyxl
manifest = json.load(open(f'/Users/wallissongomes/mercans-pipeline/CO-compliance/scope_manifest.json'))
wb = openpyxl.load_workbook(f'/Users/wallissongomes/mercans-pipeline/CO-compliance/02-wtc/CO-WTC-001-v1.0.xlsx')
ws = wb['Wage Type Catalogue']
codes_in_wtc = {row[1].value for row in ws.iter_rows(min_row=2) if row[1].value}

# Check 1 — every scope_manifest wage type category is represented
required = set()
for cat in manifest.get('wage_type_categories', {}).get('in_scope', []):
    required.add(cat)
missing = required - codes_in_wtc
assert not missing, f'Missing wage types from WTC: {missing}'

# Check 2 — every tax code referenced is in the defined country tax code legend
defined_tax_codes = set()  # populate from the Tax Code legend sheet
for row in ws.iter_rows(min_row=2):
    tc = row[6].value  # column G — Tax Code
    if tc and tc not in defined_tax_codes:
        print(f'WARN: tax code {tc} not in legend for row {row[0].row}')

# Check 3 — no 'Yes-No' ambiguity in core taxability columns unless explicitly justified
for row in ws.iter_rows(min_row=2):
    for col_idx in [13, 14, 15, 16, 17]:  # N-R: Subject to Tax/Table/Special/SS/Pension
        val = row[col_idx].value
        if val == 'Yes-No':
            # require a note in the explanation column
            assert row[3].value, f'Yes-No in row {row[0].row} requires explanation'

print('WTC post-generation validation PASSED')
```

Specifically guard against the Egypt failures (F20):
- Commission wage type MISSING from output entirely
- Tax codes from legends of OTHER countries (e.g. EG-TX-3 when EG legend is EG-TX-1 through 7)
- 'Yes-No' on SS subject flags without an explanation cell

## SOURCES
1. Global WTC baseline: ~/mercans-pipeline/shared/Global_WTC_V1_0.xlsx
2. CZ format template: ~/mercans-pipeline/shared/_CZ_Wage_Type_Catalogue_V2_0.xlsx
3. CCG Modules 3-7: ~/mercans-pipeline/CO-compliance/01-ccg/CO-CCG-001-v1.0.docx
4. Official PDFs: ~/mercans-pipeline/CO-compliance/00-official-sources/pdfs/
5. scope_manifest.json (wage_type_categories.in_scope vs out_of_scope)

## OUTPUT
Save to: ~/mercans-pipeline/CO-compliance/02-wtc/CO-WTC-001-v1.0.xlsx
Use openpyxl. Load CZ template, add Global WTC Coverage sheet + Form Reference
Guide sheet, populate all sheets.
