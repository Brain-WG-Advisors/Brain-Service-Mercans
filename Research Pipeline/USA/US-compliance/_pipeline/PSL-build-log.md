# PSL - build log
Artifact: PSL | Country: US | Round: 2 | Built: 2026-11-04
Manifest: _pipeline/build-manifest.json (USD, minor units 2, tier T4, package v1.0, status For QA)
Pack: _research/PSL-research-pack.md | Facts: _research/PSL-facts.json (168 facts, 13 unresolved entries)
Output: 06-payslip/US_Compliance_Payslip_Generator.xlsx (8 sheets) | Generator: 06-payslip/_build/build_psl.py (re-runnable; previous builds in _build/_backup/)

## Precedent inspection (L1)
Opened with openpyxl (REFERENCE_Payslip_Mozambique.xlsx, REFERENCE_Payslip_Tunisia.xlsx, 2026-11-04).
- Mozambique: 9 sheets: How to set up Payslip, Compliance Payslip, SAmple, Mozambique (EN), Mozambique (PT), NEW Specification, Payslip Spec 1, Field Option, Population Range. No `Unit Rate Details` sheet.
- Tunisia: 5 sheets: Tunisia (EN), Tunisia (FR), Payslip Spec, Unit Rate Details, Population Range. No `How to set up Payslip`, `Compliance Payslip` or `Field Option` sheet.
- Payslip grid (both): columns A-J, rows 12 pt, Arial 6/7 pt, labels DCDCDC, section bars A9A9A9, gross / deduction / net totals as SUM formulas over columns H:J, logo image at A1. Payslip Spec: 4 columns B-E (Field Name, Field Local Name, HRP Mapping (TA & BA), Field Explanation), section bars. Unit Rate Details: B Earning Description, C Earning Code, D Rate Account, E Unit Account.
- The v2.9 statement that the Mozambique reference already holds the 8 sheets is wrong; the sheets were mapped one by one:

| Built sheet | From | Note |
|---|---|---|
| How to set up Payslip | Mozambique `How to set up Payslip` | text steps, document control and one Version Control row added |
| Compliance Payslip | Mozambique `Compliance Payslip` | language-neutral master; same layout as the EN tab |
| United States (EN) / (ES) | Mozambique `{country} (EN)`, `{country} (PT)`; Tunisia `(EN)`, `(FR)` | local tab is Spanish: es is the documented second-language seam (build manifest languages.seams) |
| Payslip Spec | Tunisia `Payslip Spec` (4-column layout) | 5 sections; HRP syntax as in the references |
| Field Option | Mozambique `Field Option` (Field Name, Option Value, Option Description, Usage Context) | holds the controlled values and the State rule blocks |
| Population Range | Mozambique / Tunisia `Population Range` | 3 columns |
| Unit Rate Details | Tunisia `Unit Rate Details` | rate and unit accounts taken from the approved WTC |
| dropped | Mozambique `SAmple`, `NEW Specification` | not part of the contract |

## Fact bindings
219 bindings (location, key, register_id, also_register_ids) in `_pipeline/PSL-bindings.csv`. Keys by facts file: CCG-m03_gross_to_net-facts.json 1; CCG-m06_tax-facts.json 1; PSL-facts.json 166; WTC-global_baseline-facts.json 11. Priority PSL, WTC, DD, SIR, RSPEC, CCG; period-aware (build year 2026).
Workbook tags: 219; distinct tags checked against the local copy of the cited row: 179, misses 0.

| Location block | Bindings | Example (key -> register_id) |
|---|---|---|
| Compliance Payslip | 11 | `fed.fica.oasdi.wage_base` -> US-FEDS5-005 |
| Field Option | 169 | `psl.fed.statement.required` -> US-FED-010 |
| Payslip Spec | 13 | `psl.multi.reach.default` -> US-MULTIS5-018 |
| Population Range | 4 | `psl.ca.statement.household_exclusion` -> US-CAS5-005 |
| United States (EN) | 11 | `fed.fica.oasdi.wage_base` -> US-FEDS5-005 |
| United States (ES) | 11 | `fed.fica.oasdi.wage_base` -> US-FEDS5-005 |

## Scope decisions
| Item | Verdict | Basis |
|---|---|---|
| Payslip language | English first build, Spanish label tab as the seam | build manifest languages (owner decision US-OWN-006) |
| State rules | all 51 jurisdictions, one row each in Field Option STATE_STATEMENT_RULE | PSL facts content / scope keys |
| Worked example | one fictitious biweekly employee, work location TX, federal lines only | State lines are listed in the catalogue (160 wage types with payslip true) |
| Statutory lines | every crosswalk wage type with payslip true is in Field Option PAYSLIP_LINE (160) | `_research/WTC-crosswalk.json`, C57 |
| Totals | formulas on total rows only: Gross, Total deductions, Net, Total employer, leave balance, calculation blocks | house rule |
| Social security | lesser of (remaining annual maximum) or (rate x period base), never annualised-then-divided | house rule; sample is mid-year near the wage base |
| Currency | USD, two decimals (not in the zero-minor-unit set) | build manifest |
| Employee legal name and home address | present in Payslip Spec (Employee Full Name, Employee Home Address), mapped to the DD fields | DD confirmation |
| Contractors (Form 1099-NEC) | NO | scope, owner instruction recorded in the manifest |

## Deviations from the agent's stated constants and from the references
- Pay element lines read `code - wage type name` (for example `62100 - Basic salary`), not `XXXXX - ...`: the shared C29 rule bars an X-run next to a dash. Codes come from the WTC crosswalk.
- Display label of a line is the crosswalk (US) label, which is the WTC `Name in Local Language (English)` column; the WTC column `Name in English` carries the global name (for example 21900).
- Payslip Spec has 57 field rows (target 25-35, minimum 20): the union of the State elements and the federal lines needs more.
- Unit Rate Details: the approved WTC holds one rate wage type (62104, basic salary, listed only as the rate account of 62100) and one hours accumulator (US-030); the unit account US-030 is given only to the six time-based lines (62100, 62110, 62150, 62160, 62170, 62300); every other earning reads 'Amount only'.
- Palette (QA1-17, owner default): the payslip tabs use only the fills measured in the two payslip references (DCDCDC labels, net row and employer block; A9A9A9 title band and section bars; white rows). The navy, green, F2F2F2 and FCE4D6 fills are removed. The WTC and DD palettes (4472C4 / FF9900 / D9E1F2) belong to those artifacts; the payslip references mandate their own palette, which is kept here, and the Payslip Spec headers keep the 0B5394 / 4BACC6 of the Tunisia reference.
- Printed tabs: the three payslip tabs print the label and the value only; the calculation blocks sit below the print area. release.py strips [[FACT:]] tags only; nothing else needs stripping on those tabs. No release_rules.json is written: its text rules act on every package file, and register ids in brackets are a convention of the other artifacts.
- Payslip rows with no DD field (bank name, account, payment method, employer operating name, separate employer mailing address): the Spec says so in column E; the DD owner decides whether these become master data. The DD does hold the employer physical-address fields, which the Employer Address row maps.
- Reference sheets use Arial 6 pt on the payslip grid; kept (file prevails over the standard table). Title band and section bars A9A9A9, labels, net row and employer block DCDCDC.
- Wage-type codes (US-nnn, 5-digit) are treated as identifiers by the period-aware lint (same convention as the WTC build); the shared C46 reads them as numbers and reports a few collisions with unrelated fact values.
- Shared C46 (non-period-aware) reads the last dated value of a key and reports the 2026 wage base tag against the 2027 value; the period-aware C46 is 0 mismatches.

## Round 2: QA r1 builder items
| Item | Change |
|---|---|
| QA1-01 | Employer social security is a formula, lesser of the remaining annual maximum and rate x period base, on the 3 tabs (calc rows under the print area) |
| QA1-02 | New input row 'Medicare wages paid before this payslip' (no wage base); Additional Medicare and YTD Medicare use it; YTD Medicare = prior tax + Medicare + Additional Medicare |
| QA1-03 | Employer Medicare is a formula; YTD gross = input 'gross paid before' + gross of the payslip |
| QA1-04 | 'Total Hours Worked' row (SUM of the hours column) and Spec row; PSL-legal-items 'hours' matches it |
| QA1-05 | 6 Spec rows: Bank Name, Account (masked), Payment Method, Compensation Sources, Pay-Code Guide Reference, Compensatory Time |
| QA1-06 | State-switched rows and Spec rows: AZ sick pay received, NYC PTO accrued / paid used / unpaid used / unpaid available |
| QA1-07 | Leave block of the TX sample reads 'not printed' |
| QA1-08 | Spec SSN mapping returns no digits for MD; the Employee ID is the identifier |
| QA1-09 | MN 181.032(b) items mapped: operating name, mailing address, meals and lodging allowances, 268B.14 deduction line (US-185), hours, rate basis |
| QA1-10 | NM benefits-earned row and Spec row; RATE_OF_PAY_BASIS adds Shift, Day, Week, Other; NY 195(3) industry items are a named limitation (gap request) |
| QA1-11 | Population Range C12 cites psl.ca.statement.household_exclusion; psl.va.statement.content removed from C13 |
| QA1-12 | Field Option NOT_CONFIGURED block removed |
| QA1-13 | Payslip tabs print label and value only; print area set; calculation blocks outside it |
| QA1-14 | 'Build rule / Build default / generator' wording replaced; the 3 fact values arrive reworded (R2) |
| QA1-15 | Spanish with diacritics on the ES tab and Spec column C; Hourly, Biweekly, Single or MFS, job title, bank translated |
| QA1-16 | Unit Rate Details: 62104 row dropped; US-030 only on time-based lines; one specific basis text per row |
| QA1-17 | Reference payslip palette applied (see deviations) |
| QA1-18 | Payment details: header Amount, value = net pay formula |
| QA1-19 | Spec EIN mapping adds the State employer account number for OR |
| QA1-22 | PSL-bindings.csv is written from the cells of the finished workbook: one row per tag, location sheet!cell |

### Worked example recomputed by hand (integer cents, independent of the generator)
- Gross = 80 x 36.00 + 4 x 54.00 + 17,000.00 = 20,096.00; 401(k) 5% = 1,004.80; cafeteria plan 85.00; FICA wages = 20,011.00
- Employee social security: remaining = 6.2% x 184,500.00 - 6.2% x 181,500.00 = 186.00; period = 6.2% x 20,011.00 = 1,240.68; withheld = lesser = 186.00
- Employer social security: same rate, same base, same prior wages, so lesser = 186.00 (before: uncapped 1,240.68)
- Medicare: 1.45% x 20,011.00 = 290.16 employee and 290.16 employer
- Additional Medicare: Medicare wages YTD = 181,500.00 + 20,011.00 = 201,511.00; above 200,000.00 = 1,511.00 (limited to this payslip); 0.9% x 1,511.00 = 13.60
- Employer total = 476.16; YTD Medicare = 2,631.75 + 290.16 + 13.60 = 2,935.51; YTD gross = 185,000.00 + 20,096.00 = 205,096.00

## Open items (not configured in this release)
13 requests, all non-blocking: {'open': 13}. Each has a cell reading 'Not configured in this release [[GAP:PSL-RQ-nn]]', an entry in `_research/gaps.json` and a request in `_research/PSL-research-request.json`.

| Gap id | Key | Reason | First cell |
|---|---|---|---|
| PSL-RQ-02 | `psl.ca.statement.electronic_consent` | open | Field Option!ELECTRONIC_DELIVERY_RULE CA |
| PSL-RQ-03 | `psl.co.statement.electronic_consent` | open | Field Option!ELECTRONIC_DELIVERY_RULE CO |
| PSL-RQ-07 | `psl.il.statement.content_rule_300_600` | open | Field Option!STATE_STATEMENT_RULE IL |
| PSL-RQ-08 | `psl.in.statement.scope_confirmation` | open | Field Option!STATE_STATEMENT_RULE IN |
| PSL-RQ-10 | `psl.la.statement.scope` | open | Field Option!STATE_STATEMENT_RULE LA |
| PSL-RQ-11 | `psl.ma.statement.electronic_consent` | open | Field Option!ELECTRONIC_DELIVERY_RULE MA |
| PSL-RQ-14 | `psl.ms.statement.scope` | open | Field Option!STATE_STATEMENT_RULE MS |
| PSL-RQ-22 | `psl.nv.statement.electronic_consent` | open | Field Option!ELECTRONIC_DELIVERY_RULE NV |
| PSL-RQ-23 | `psl.ny.statement.electronic_consent` | open | Field Option!ELECTRONIC_DELIVERY_RULE NY |
| PSL-RQ-24 | `psl.ri.retention_and_hire_notice_2026` | open | Field Option!RETENTION_PERIOD RI |
| PSL-RQ-26 | `psl.ssn_rule.unread_states` | open | Field Option!SSN_DISPLAY_RULE open |
| PSL-RQ-28 | `psl.tx.statement.scope_confirmation` | open | Field Option!STATE_STATEMENT_RULE TX |
| PSL-RQ-29 | `psl.ny.statement.industry_extras` | open | Field Option!STATE_STATEMENT_RULE NY |

## Reconciliation
| Kind | Status | Rows |
|---|---|---|
| CATALOGUE_LINE | MAPPED | 131 |
| CATALOGUE_LINE | MAPPED_NO_DD_FIELD | 29 |
| EXAMPLE_LINE | MAPPED | 21 |
| EXAMPLE_LINE | MAPPED_NO_DD_FIELD | 12 |
| SPEC_FIELD | MAPPED | 19 |
| SPEC_FIELD | MAPPED_NO_DD_FIELD | 38 |
`MAPPED_NO_DD_FIELD`: the amount is a payroll result or input of the wage type and no DD master-data field holds it (F26). Unmapped 0.

## Checks (latest run)
```
## build (exit 0)
recon rows 250 {('EXAMPLE_LINE', 'MAPPED'): 21, ('EXAMPLE_LINE', 'MAPPED_NO_DD_FIELD'): 12, ('CATALOGUE_LINE', 'MAPPED_NO_DD_FIELD'): 29, ('CATALOGUE_LINE', 'MAPPED'): 131, ('SPEC_FIELD', 'MAPPED_NO_DD_FIELD'): 38, ('SPEC_FIELD', 'MAPPED'): 19} UNMAPPED 0
bindings 219 requests 13 unmapped 0
written C:\Users\instituto\Documents\brain-service\Research Pipeline\USA\US-compliance\06-payslip\US_Compliance_Payslip_Generator.xlsx

## C12 / C29 / WORD+PATH / FRAC+PCT+UNIT / C30 / C46 period-aware / GAP (psl_lint) (exit 0)
{
 "C29": 0,
 "WORD": 0,
 "mismatch": 0,
 "missing_key": 0,
 "unbound": 0,
 "C30": 0,
 "FRAC": 0,
 "PCT": 0,
 "UNIT": 0,
 "tags": 219,
 "C12": 0,
 "GAP": 0,
 "info": {
  "sheets": 8,
  "spec_rows": 57,
  "unit_rows": 26,
  "payslip_lines": 160,
  "states": 51,
  "tags": 219,
  "images": {
   "How to set up Payslip": 1,
   "Compliance Payslip": 1,
   "United States (EN)": 1,
   "United States (ES)": 1
  },
  "gap_ids": 13
 }
}

## f44_self (exit 0)
F44 self-check: 179 distinct tags, 0 misses, 0 tags without a local copy

## recon (payslip lines x WTC x DD; PSL facts placed) (exit 0)
recon rows 250; UNMAPPED 0; payslip lines of the crosswalk missing 0; PSL facts not placed 0

## C71 identical rebuild (exit 0)
C71: 0 differences

## shared consistency C42 / C43 (whole package) (exit 0)
C42: PASS  {'hits': 0}
C43: PASS  {'package_version': '1.0', 'problems': 0}

## shared C46 on the payslip workbook alone (not period-aware: known limit, see build log) (exit 1)
  {'file': '06-payslip\\US_Compliance_Payslip_Generator.xlsx', 'where': 'Field Option!B201', 'text': '21100', 'keys': ['ia.sui.wage_base'], 'why': 'fact value not carried by a [[FACT:]] tag'}
  {'file': '06-payslip\\US_Compliance_Payslip_Generator.xlsx', 'where': 'Field Option!D201', 'text': '21100', 'keys': ['ia.sui.wage_base'], 'why': 'fact value not carried by a [[FACT:]] tag'}
  {'file': '06-payslip\\US_Compliance_Payslip_Generator.xlsx', 'where': 'Field Option!B323', 'text': '175', 'keys': ['al.wh.std_deduction.married.phaseout.reduction_per_step', 'ut.pit.oracle.example_6.wages'], 'why': 'fact value not carried by a [[FACT:]] tag'}
  {'file': '06-payslip\\US_Compliance_Payslip_Generator.xlsx', 'where': 'Field Option!D323', 'text': '175', 'keys': ['al.wh.std_deduction.married.phaseout.reduction_per_step', 'ut.pit.oracle.example_6.wages'], 'why': 'fact value not carried by a [[FACT:]] tag'}
  {'file': '06-payslip\\US_Compliance_Payslip_Generator.xlsx', 'where': 'Field Option!B345', 'text': '214', 'keys': ['oh.pit.school_district.count'], 'why': 'fact value not carried by a [[FACT:]] tag'}
  {'file': '06-payslip\\US_Compliance_Payslip_Generator.xlsx', 'where': 'Field Option!D345', 'text': '214', 'keys': ['oh.pit.school_district.count'], 'why': 'fact value not carried by a [[FACT:]] tag'}
  {'file': '06-payslip\\US_Compliance_Payslip_Generator.xlsx', 'where': 'Field Option!B354', 'text': '225', 'keys': ['nv.report.ui.registration_threshold.quarterly'], 'why': 'fact value not carried by a [[FACT:]] tag'}
  {'file': '06-payslip\\US_Compliance_Payslip_Generator.xlsx', 'where': 'Field Option!D354', 'text': '225', 'keys': ['nv.report.ui.registration_threshold.quarterly'], 'why': 'fact value not carried by a [[FACT:]] tag'}

## shared content C49 / C57 / C70 (exit 1)
C49: FAIL  {'wtc': '02-wtc\\US-WTC-001-v1.0.xlsx', 'codes_checked': 259, 'problems': 1}
      {'file': '01-ccg\\US-CCG-001-v1.0.docx', 'where': 'table 206 r11c2', 'code': 'KW-100', 'why': "not in the WTC (cited as 'residents working in other states; nonresidents')"}
C57: PASS  {'payslip': '06-payslip\\US_Compliance_Payslip_Generator.xlsx', 'items': 22, 'problems': 0}
C70: PASS  {'citations_checked': 7, 'not_in_register': 0, 'repealed_cited': 0, 'gap_problems': 0}

## validate_contract --all (exit 0)
ok    C:\Users\instituto\Documents\brain-service\Research Pipeline\USA\US-compliance\_qa\WTC-review-r2.json   [review.schema.json]
ok    C:\Users\instituto\Documents\brain-service\Research Pipeline\USA\US-compliance\_qa\WTC-review-r3.json   [review.schema.json]
PASS  (102 files)

## Excel open check (exit 0)


OPEN CHECK: 1 file(s), 0 not clean
```

## Accuracy
85% - official reference structure (Mozambique and Tunisia workbooks), approved WTC and DD, and research with a register row for every rule; the worked example is computed from the facts. No real US payslip sample was available, and the State rules are statute readings, not tested against a filed statement. 13 items are open (statements not proven in the saved source copy, or not yet read). Closing the gap needs the authority pages named in each request (agent 2) and a payslip accepted by one payroll operator (development team).
