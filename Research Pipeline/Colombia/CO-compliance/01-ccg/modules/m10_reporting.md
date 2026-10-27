# Module 10: Reporting, Compliance & Finalisation

*Purpose: To define all statutory reporting obligations and final processing rules.*

> **Scope note (dev-team filtering rule).** This module gives the summary table and the mechanics. It does
> **not** reproduce field-level specification content. For layouts, code tables, validation rules, XML
> paths and field-by-field detail, see the Colombia Report Specifications **CO-RPT-001 to CO-RPT-007** and
> the Statutory Integrations Register **CO-SIR-001 to CO-SIR-007**.

## 10.1 Statutory Reporting

### Describe the country's primary digital payroll reporting system.

Colombia's primary digital payroll reporting system is the **Electronic Payroll Support Document**
(*Documento Soporte de Pago de Nómina Electrónica*), implemented by **Resolution DIAN 000013 of 11 February
2021** and its 269-page Technical Annex, currently at **version 1.0** with **XSD version 1.0.6**.

| Aspect | Detail |
|---|---|
| **What it is** | The electronic document that constitutes the **tax support for the costs and deductions** arising from an employment relationship. Without it the employer cannot deduct payroll costs for income-tax purposes |
| **Who must issue** | Every taxpayer who deducts payroll costs, in respect of payments derived from an employment or statutory relationship, and payments to pensioners at the employer's charge |
| **Frequency** | **Monthly**, one document per employee per month, *"irrespective of whether the obliged party makes payments in different or shorter periods"* (art. 3). A semi-monthly payroll therefore produces **one** monthly XML |
| **Content** | Three totals: accrued payroll (*devengados*), deducted payroll (*deducciones*), and the difference (art. 2), itemised by concept |
| **Deadline** | Transmitted for validation **within the first 10 days of the month following** the payment or credit (art. 8) |
| **Channel** | **Genuine machine-to-machine** — SOAP 1.2, operation `SendNominaSync`, payload is the **base64 encoding of a ZIP containing the XML**, maximum **500 KB**, **UTF-8 only** |
| **Authentication** | X.509 certificate from a certification authority accredited by the national accreditation body, **XAdES-EPES** signature with a claimed role of `thirdparty` or `supplier` |
| **Response** | Synchronous base64 `ApplicationResponse` carrying the validation result |
| **Unique identifier** | **CUNE**, a 96-character SHA-384 hexadecimal, computed over the document's key fields plus the software identifier and secret PIN |
| **Corrections** | **Adjustment note** (`NominaIndividualDeAjuste`) — a replacement or cancellation document referencing the original |
| **Version literal** | The `Version` element must carry the exact literal `V1.0: Documento Soporte de Pago de Nómina Electrónica`; a mismatch is a rejection (rule NIE022) |
| **Uniqueness** | A given document number may be transmitted **only once per employee** (global rule 90) |
| **Employer enablement** | The issuer must be enabled by the tax authority; global rule 92 rejects any document from a non-enabled issuer |

**This is genuinely machine-to-machine — and it is the exception, not the rule, in Colombia.** The country
runs **three different integration postures at once**:

| System | Posture |
|---|---|
| Electronic payroll support document | **Machine-to-machine** — SOAP web service, digital signature, synchronous response |
| Form 350 monthly withholding return; Form 220; the information return | **Portal round-trip** — prepared and submitted through the tax authority's electronic filing portal |
| **Integrated social-security contribution return** | **Portal round-trip through a licensed private information operator.** The employer never reaches the government directly for social security |

### Deliverable: Data Disaggregation Mapping Guide describing main reporting categories

The electronic payroll XML requires payroll data to be disaggregated into a **fixed taxonomy of named
elements**. The engine cannot report a single "gross pay" figure; each concept must map to its own element.
The following is the mapping guide at category level; the element-by-element specification is in
**CO-RPT-001**.

**Category 1 — Header and identification**

| Reporting category | Content | Source |
|---|---|---|
| Environment and document type | Production or test; document type; version literal | Configuration |
| Numbering | Prefix + sequence, unique per employee; CUNE; QR link | Engine |
| Software provenance | Software identifier, security code (SHA-384 of identifier + PIN + document number), provider tax number and verification digit | Configuration |
| Employer | Tax number without separators, verification digit, corporate or personal name, country, department, municipality, address | Employer master data |
| Employee | Document type from the closed list, document number, first and second surname, first and other given names, place-of-work country, department, municipality and address, worker type and sub-type, contract type, high-risk pension flag, all-inclusive-salary flag, contractual salary, internal employee number | Employee master data |
| Period | Hire date, termination date, settlement start and end, time worked, pay frequency | Employment master data |
| Payment | Payment form, payment method, bank, account type, account number, payment date | Payment master data |

**Category 2 — Accrued payroll (*Devengados*)**

| Reporting category | Disaggregation required |
|---|---|
| Basic | Days worked; salary paid for the period |
| Transport | Transport allowance; travel and accommodation allowances, split **salary / non-salary** |
| Overtime and premiums | Each hour type separately, with quantity, start and end time, percentage and amount: day overtime, night overtime, night premium, rest-day and holiday premium, and their combinations |
| Vacation | Vacation taken and vacation compensated in cash, with quantity and amount |
| Statutory benefits | Service bonus; severance savings; interest on severance savings |
| Incapacity | Each incapacity, by type — general illness, occupational, professional disease — with quantity and amount |
| Leave | Maternity or paternity leave; remunerated leave; unremunerated leave, each with quantity and amount |
| Bonuses and allowances | **Paired salary / non-salary elements** for bonus, allowance, generic concept, generic payment, meal payment, travel/accommodation allowance |
| Other | Work clothing; apprentice maintenance support; commissions; third-party payments; advances; reimbursements; compensation; other concepts |
| **Total** | Total accrued |

**Category 3 — Deducted payroll (*Deducciones*)**

| Reporting category | Disaggregation required |
|---|---|
| Health | Percentage and amount |
| Pension | Percentage and amount |
| **Solidarity pension fund** | **Four attributes** — the solidarity percentage and amount, and the subsistence percentage and amount. Must **not** be merged into the pension line |
| Withholding tax | Amount |
| Voluntary contributions | Voluntary pension; long-term savings; individual-account voluntary contributions |
| Court orders and third parties | Judicial withholdings; maintenance debts; cooperatives; third parties; commercial establishments |
| Loans and advances | Employer loans; advances; other deductions |
| Union and welfare | Union dues; funeral funds; employee welfare funds |
| Sanctions and reimbursements | Public sanctions; private sanctions; reimbursements; educational debt |
| **Total** | Total deducted |

**Category 4 — Totals and rounding**

| Element | Content |
|---|---|
| Total accrued | Sum of category 2 |
| Total deducted | Sum of category 3 |
| **Rounding** | The explicit `Redondeo` element carrying the residual difference — the tolerance is ±2.00 and the rounding convention is round-half-to-even |
| Total to pay | Accrued less deducted, adjusted for rounding |

**The single most important mapping rule.** The XML separates salary from non-salary **at element level**,
with paired element names carrying an explicit `S` or `NS` suffix. The engine must therefore carry a
**hard salary/non-salary flag on every wage type**, set at configuration time, and must not attempt to
derive it at reporting time.

### List all other mandatory reports, stating the frequency, file format, due date, reporting authority.

| ID | Report | Authority | Frequency | Format | Due date |
|---|---|---|---|---|---|
| **CO-RPT-001** | Electronic Payroll Support Document | DIAN | **Monthly** | **XML** (base64 of a ZIP, ≤ 500 KB, UTF-8), machine-to-machine SOAP | Within the first **10 days** of the following month |
| **CO-RPT-002** | **Form 350** — monthly withholding-tax return | DIAN | **Monthly** | Portal form; values rounded to the nearest 1,000 | **7th to 16th business day** of the following month, by the last digit of the employer tax number |
| **CO-RPT-003** | **Integrated contribution return** (PILA) — social security and payroll levies | Ministry of Health and Social Protection, filed through a licensed information operator | **Monthly** | **Fixed-width flat file**: type 1 file (employer data, 34 fields, 567 positions) and type 2 file (header record, 22 fields, 359 positions, plus a detail record per contributor) | **2nd to 16th business day** of the following month, by the last two digits of the employer tax number |
| **CO-RPT-004** | **Form 220** — annual income and withholding certificate to each employee | DIAN (issued to the employee) | **Annual** | Prescribed form, whole pesos | **Last business day of March** |
| **CO-RPT-005** | **Format 2276 version 4** — third-party information return on work and pension income | DIAN | **Annual** | XML through the tax authority's information-return service | **May–June**, by the employer tax number |
| **CO-RPT-006** | **Severance-savings deposit** allocation to each employee's fund | Severance-savings funds | **Annual** | Fund-specific file or portal | **By 14 February** |
| **CO-RPT-007** | **Disability-hiring contract report** | Ministry of Labour | **Per event** | Portal | Within **15 days** of contract signature |

**Two obligations that are payments, not reports, but sit on the same calendar:**

| Obligation | Deadline |
|---|---|
| Interest on severance savings, paid **to the employee** | During **January** |
| Service bonus, two instalments | By **30 June** and by **20 December** |

**Consolidated 2026 employer filing calendar**

| Month | Obligation |
|---|---|
| **January** | Pay the interest on severance savings to employees. Reparameterise for the new minimum wage and tax unit |
| **February** | **Deposit severance savings to each employee's fund by 14 February** |
| **March** | **Issue Form 220 to every employee by the last business day** |
| **April** | Work-clothing delivery by **30 April** |
| **May–June** | File the **information return, Format 2276** |
| **June** | **Recalculate the fixed withholding percentage** for employees on Procedure 2. Pay the **first half of the service bonus by 30 June** |
| **1 July** | **Rest-day and holiday premium steps from 80% to 90%** |
| **15 July** | **42-hour week and the 210 hourly divisor take effect** |
| **August** | Work-clothing delivery by **31 August** |
| **December** | **Recalculate the fixed withholding percentage.** Pay the **second half of the service bonus by 20 December.** Work-clothing delivery by **20 December**. Liquidate severance savings at 31 December |
| **Every month** | Electronic payroll XML (10 days); Form 350 (7th–16th business day); integrated contribution return (2nd–16th business day) |

### What pay elements are required as intermediates from payroll for reporting?

These are engine outputs that no single artefact displays but that several artefacts consume. They must be
computed and stored, not derived at reporting time.

| Intermediate | Consumed by | Why it cannot be derived later |
|---|---|---|
| **Contribution base per fund** (health, pension, occupational risk, family compensation fund) | Contribution return, XML | The bases legitimately differ — the first three are capped at 25 minimum wages; the payroll-levy base is uncapped |
| **Payroll-levy base**, separate from the contribution base | Contribution return | Different statutory definition (Law 21 of 1982 art. 17) — includes paid rest days, no ceiling |
| **Contributory days per fund** | Contribution return | Each subsystem carries its own day count |
| **Change-event flags and their day counts** | Contribution return | Hire, termination, transfers, salary variation, unpaid leave, incapacity, maternity, vacation |
| **Salary and non-salary payment totals for the period** | Calculation, XML | Required to apply the 40% clamp and to populate the paired `S` / `NS` elements |
| **The 40% clamp excess added back** | Contribution return | Must be identifiable, because it is in the contribution base but out of the statutory-benefit base |
| **Exemption flag per employee per month** | Contribution return field 33, employer cost | The exemption test is monthly and per employee |
| **Overtime hours by type, with start and end times and percentages** | XML, overtime register | The XML requires quantity, times and percentage per hour type; the register requires the day/night split |
| **Rolling 6-month average labour income** | Information return field 33; the severance-savings exemption taper | Must be maintained year-round |
| **Rolling 12-month taxable payments** | Procedure 2 semi-annual recalculation | The ÷13 average |
| **Meal payments split at the 41-tax-unit threshold** | Information return fields 32 and 8 | Two separate fields |
| **Severance savings split three ways** — paid to the employee, deposited to the fund, and under the pre-1991 regime | Information return fields 18, 19, 20 | Three separate lines |
| **Withholding by counterparty type** — natural persons vs legal persons | Form 350 | The 2024 form separates them |
| **Statutory benefit accruals**, by concept | Employer cost, termination settlement | Four separate accruals with different bases |
| **Vacation balance, taken, compensated, and accumulation age** | Vacation register; termination | Art. 190 accumulation limits |
| **Daily and weekly overtime counters** | Compliance | The 2-per-day and 12-per-week limits |
| **Hourly divisor applied**, with its effective date | Audit trail | The 220 → 210 change on 15 July 2026 |
| **Rest-day premium percentage applied**, with its effective date | XML, audit trail | The 80% → 90% change on 1 July 2026 |

*Legal basis: Resolution DIAN 000013 of 11 February 2021 arts. 1, 2, 3, 5, 8, 15, 22, 23, 24, 26 and its
Technical Annex; Resolution DIAN 000031 of 2024; Resolution DIAN 000022 of 20 February 2024; Resolution
DIAN 000227 of 2025 arts. 1.3.7.1.1 and 1.3.9.1; Decree 1625 of 2016 arts. 1.6.1.13.2.33 and 1.6.1.13.2.40
(as set by Decree 2229 of 2023); Decree 780 of 2016 art. 3.2.2.1 (substituted by Decree 1990 of 2016
art. 2); Resolution MSPS 2388 of 2016 and Technical Annex 2; Law 21 of 1982 art. 17; Law 50 of 1990
art. 99; Law 52 of 1975 art. 1; Substantive Labour Code arts. 232, 306; Law 2466 of 2025 art. 15; DIAN
Concepto 013840 int. 1568 of 1 October 2025.*

---

## 10.2 Integrations

### Is there any mandatory inbound integration?

**Yes — three, and they must not be defaulted to out of scope.**

| # | Inbound integration | From | Format | What the engine must do with it |
|---|---|---|---|---|
| **1** | **Validation response to the electronic payroll document** (`ApplicationResponse`) | DIAN, synchronously in the same SOAP call | **base64 XML** | **Parse it.** A document is legally issued only once validated. The engine must store the validation status and the CUNE, retry or correct rejections, and block the tax deduction of an unvalidated payroll cost. This is a **hard inbound dependency**, not a receipt |
| **2** | **Contribution-return settlement response** | The licensed information operator | Operator-specific file or portal output | Reconcile the settled contributions against the engine's computation, capture the return number and payment date, and detect rejected contributor records |
| **3** | **Health-insurer and occupational-risk benefit determinations** | Health insurer (EPS) and occupational-risk insurer (ARL) | Portal output or file | Determine the amount and period of the sickness, maternity, paternity and occupational-injury benefit actually recognised, so the employer's payroll advance can be reconciled and any shortfall recovered from the employee or absorbed |

**Two further inbound flows that are operational rather than statutory** but that a production
implementation will need: the severance-savings fund's confirmation of the February deposit, and the
payroll lender's instalment schedule under a *libranza* authorisation.

**Why this matters for the scope manifest.** Inbound files that the engine must parse and act on carry
`product_mapping_required: true`. Item 1 in particular is not optional — an employer that transmits without
consuming the validation response cannot demonstrate that its payroll costs are supported, which is the
entire purpose of the document.

### Is there any mandatory outbound integration beyond standard reporting?

**Yes — two, plus the payment file.**

| # | Outbound integration | To | Format | Nature |
|---|---|---|---|---|
| **1** | **Electronic payroll document transmission** | DIAN | SOAP 1.2 `SendNominaSync`; base64 of a ZIP containing the XML; ≤ 500 KB; UTF-8; XAdES-EPES signature with an X.509 certificate from an accredited certification authority | **Genuine machine-to-machine.** This goes beyond "standard reporting" — it is a real-time signed web-service call with a synchronous validation response |
| **2** | **Graphical representation of the payroll document to the employee** | The employee | PDF or printed | Permissive under Resolution DIAN 000013 of 2021 art. 24 — but **if issued**, it must carry the art. 5 content and a **QR code of at least 2 cm on every page** |
| **3** | **Bank payment file** | The employer's paying bank | Bank-specific fixed-width or delimited format | **Colombia does not use IBAN.** Domestic account numbers are numeric, of bank-specific length (commonly 10–17 digits), with no national check-digit standard. The bank-entity code catalogue is bank- and clearing-house-specific and must be obtained per client |

**Third-party operation.** Where Mercans generates or transmits the electronic payroll document on the
client's behalf, Resolution DIAN 000013 of 2021 art. 22 requires that the provider be enabled by the tax
authority, be registered in the tax registry, and that **both parties retain the mandate document**
accrediting the arrangement. This is a contractual precondition to go-live, not a technical one.

**Ownership note (control B7).** The following are **explicitly owned upstream** and are not Mercans
deliverables: the licensed information operator's own file format and portal (owned by the operator); the
severance-savings fund's deposit interface (owned by the fund); the payroll lender's schedule (owned by the
lender); and the bank's payment-file specification (owned by the client's bank). Each implies an **inbound
data contract** the engine must receive — respectively the settlement response, the deposit confirmation,
the instalment schedule and the payment acknowledgement. Reversing any of these scope calls is a contained
change to one interface, not a redesign.

---

## 10.3 Payslip Requirements

### List all mandatory components that must be itemized on an employee payslip.

**The headline finding: Colombia has no statutory payslip-content article in its labour code.** The
Substantive Labour Code was grep-tested across its full consolidated text for the seven Spanish terms used
for a payslip — *desprendible*, *comprobante de pago*, *colilla*, *volante de pago*, *recibo de pago*,
*constancia de pago* and *detalle de la liquidación* — with **zero hits**. Law 2466 of 2025 added none.

**The operative itemisation rule is therefore tax law, not labour law: Resolution DIAN 000013 of 2021
article 5**, which lists the mandatory content of the electronic payroll support document, combined with
**article 24**, which makes the graphical representation permissive but requires it to carry that content
if it is issued.

**Mandatory content — Resolution DIAN 000013 of 2021 art. 5 (13 items):**

| # | Item |
|---|---|
| 1 | Employer's or issuer's surnames and names, or corporate name, and tax identification number |
| 2 | Employee's or beneficiary's surnames and names, and identity document number |
| 3 | Identification of the electronic payroll support document — a unique consecutive number preceded by the authorised prefix |
| 4 | Generation date |
| 5 | Payment or credit date |
| 6 | **Accrued payroll values** (*valores devengados de nómina*), itemised by concept |
| 7 | **Deducted payroll values** (*valores deducidos de nómina*), itemised by concept |
| 8 | **Total difference** between accrued and deducted |
| 9 | Payment or credit period |
| 10 | **Payment method and medium** |
| 11 | Country, department and municipality of origin |
| 12 | Content of the authorised technical annex |
| 13 | **CUNE** — the unique electronic payroll code |

**Additional mandatory formal requirements where a graphical representation is issued:**

| Requirement | Rule |
|---|---|
| **Language** | **Spanish**, mandatory. Another language may be **added**, never substituted (art. 26) |
| **Currency** | **Colombian pesos**, mandatory. Another currency may be added (art. 26) |
| **QR code** | **At least 2 cm × 2 cm on every page**, encoding the tax authority's document-search URL with the CUNE as the key (Technical Annex §13.1) |
| **Legal status** | The paper or PDF document is a **representation** of the electronic document, not the document itself. Its legal validity derives from the validated XML |

**Mercans practice — items that are good practice but not legally required:**

- the itemisation of **employer contributions** for transparency (never a deduction from the employee);
- the **statutory benefit accruals** and balances;
- the **vacation balance**;
- the **hourly divisor and rest-day premium percentage applied**, given the two mid-2026 cut-overs;
- the contract type, hire date and pay frequency;
- year-to-date totals.

**A formatting rule that must not be blended.** The payslip carries the **XML** figures — two decimals,
round-half-to-even. It must **not** display the contribution-return figures (rounded up to the nearest 100)
as if they were the deduction, nor the Form 350 figure (rounded to the nearest 1,000). Where the client
requires the contribution-return figure to be shown, it must be shown as a **separate, labelled line**.

*Legal basis: Resolution DIAN 000013 of 11 February 2021 arts. 5, 24, 26 and Technical Annex §13.1;
Substantive Labour Code (Decree 2663 of 1950), full consolidated text — no payslip-content article.*

---

## 10.4 Other Compliance

### Is payroll software certification mandatory?

**Not certification in the formal sense — but *enablement* is mandatory, and it functions as a gate.**

| Requirement | Status |
|---|---|
| **Formal software certification or accreditation scheme** | **No.** There is no Colombian payroll-software certification body, no certificate of conformity and no periodic recertification |
| **Enablement (*habilitación*) of the issuer with the tax authority** | **Mandatory.** Global validation rule 92 rejects any document from a non-enabled issuer. The employer, or the third-party provider acting for it, must complete the enablement process in the tax authority's test environment before transmitting in production |
| **Software identifier and secret PIN** | **Mandatory.** Assigned by the tax authority at software activation. The PIN never appears in the XML; it feeds both the software security code and the CUNE |
| **Software security code** | **Mandatory.** SHA-384 of `SoftwareID + PIN + document number` |
| **Digital certificate** | **Mandatory.** X.509 from a certification authority accredited by the national accreditation body, used for the XAdES-EPES signature |
| **Third-party provider registration** | **Mandatory** where a provider generates or transmits. The provider must be enabled and registered in the tax registry, and both parties must retain the mandate document (art. 22) |
| **Contribution-return software** | **No certification.** Filing is through a licensed information operator, and the operator's technical guide governs the file it accepts |

**Practical consequence.** Enablement is a **project prerequisite with a lead time**, not a configuration
step. It requires the employer's digital certificate, the tax-registry registration, and a successful pass
through the test environment. It must be scheduled at the start of an implementation, not at go-live.

**Other compliance obligations that are not software-related:**

| Obligation | Source |
|---|---|
| **Overtime register** — activity, total supplementary hours, day/night split, evidence of payment; available to employees and to administrative and judicial authorities | Labour Code art. 162 num. 2 (Law 2466 of 2025 art. 12); Circular 101 of 2025 §3. Failure allows inspectors to **suspend all supplementary work for six months** |
| **Vacation register** — entry date, start and end of each vacation, remuneration paid | Labour Code art. 187 num. 3 |
| **Internal work rules** (*reglamento de trabajo*), published | Labour Code art. 120, as substituted by Law 2466 of 2025 art. 8 |
| **Disciplinary due process** before any sanction | Labour Code art. 115, as substituted by Law 2466 of 2025 art. 7 |
| **Disability-hiring quota** — employers with up to 500 employees must have at least **two employees with a disability per 100**; from 501 employees, one additional per 100-employee tranche, on the permanent headcount, with health-ministry certification. Contracts must be **reported to the Ministry of Labour within 15 days** of signature. The values are optional in the law's first year and mandatory from the second | Law 2466 of 2025 art. 15 |
| **Apprentice quota**, or its monetisation | Law 789 of 2002 art. 34, as substituted by Law 2466 of 2025 art. 23 |
| **Data-protection compliance** — internal data-treatment policy, privacy notice, database registration | Law 1581 of 2012; Decree 1074 of 2015 |

---

## 10.5 Year-End Processing and Finalisation

### Describe the mandatory year-end finalisation process.

Colombia's year end is a **settlement and certification** process, not a reconciliation. There is no annual
tax true-up and no annual social-security reconciliation.

```
DECEMBER 2026
  1. Pay the SECOND HALF of the service bonus         by 20 December
     = (salary + transport allowance) x days in the semester / 360
  2. Deliver the third WORK-CLOTHING issue            by 20 December
  3. RECALCULATE the fixed withholding percentage for every employee on
     Procedure 2:  (sum of 12 months' taxable payments) / 13 -> table -> %
     Binds January to June 2027.
  4. LIQUIDATE SEVERANCE SAVINGS at 31 December
     = (salary + transport allowance) x days of service in the year / 360
     Base rule (art. 253): the LAST monthly salary if unchanged in the last
     3 months; otherwise the average of the last year.
  5. Compute the INTEREST on the 31 December balance
     = balance x 12% x days / 360
  6. Run the December payroll and transmit the December XML by 10 January.

JANUARY 2027
  7. PAY THE INTEREST ON SEVERANCE SAVINGS TO THE EMPLOYEE, during January.
     Not to the fund - directly to the employee.
     Failure = an indemnity equal to the interest owed, once only.
  8. REPARAMETERISE: new minimum wage, new transport allowance, new tax unit.
     Every floor, ceiling, trigger and band boundary moves.
  9. File the December contribution return and Form 350 on the ordinary
     business-day calendar.

FEBRUARY 2027
 10. DEPOSIT SEVERANCE SAVINGS to each employee's chosen fund
     BEFORE 15 FEBRUARY (i.e. by 14 February).
     Late deposit = ONE DAY'S SALARY FOR EACH DAY OF DELAY.
     Exception: where the employer proves direct payment to the employee,
     that payment is discharging and no penalty applies
     (art. 57 par. 4, Law 2466 of 2025 art. 15) - but fund affiliation
     remains compulsory.

MARCH 2027
 11. ISSUE FORM 220, the annual income and withholding certificate,
     to EVERY employee, by the LAST BUSINESS DAY OF MARCH.

MAY-JUNE 2027
 12. File the INFORMATION RETURN, Format 2276 version 4, by the deadline
     applicable to the employer's tax number.
```

**The most expensive year-end failure** is the severance-savings deposit. One day's salary per day of delay
accrues without cap until the deposit is made, and it is a per-employee penalty. For a workforce of 100
employees on the minimum wage, a two-week delay is roughly **COP 81.7 million**.

### What documentation or annual statements must be provided to employees?

| Document | Deadline | Content | Source |
|---|---|---|---|
| **Form 220 — Certificate of Income and Withholdings** | **Last business day of March** | The employer's and employee's identification; total payments by concept; total withheld. Where the employee is **not** required to file an annual return, art. 380 requires the certificate to carry the employee's own declarations of their other income, assets and liabilities, and it then substitutes for the employee's return | Tax Code arts. 378–379; Decree 1625 of 2016 art. 1.6.1.13.2.40; form prescribed by Resolution DIAN 000022 of 20 February 2024 |
| **Graphical representation of the electronic payroll document** | Monthly, if issued | The 13 art. 5 items plus a ≥ 2 cm QR on every page. **Permissive** — the employer is not obliged to issue it, but if it does, this content is mandatory | Resolution DIAN 000013 of 2021 arts. 5 and 24 |
| **Severance-savings deposit certificate** | February | Evidence of the deposit. Issued by the fund, but the employer must be able to evidence it | Law 50 of 1990 art. 99 |
| **Interest payment evidence** | January | Evidence that the 12% interest was paid to the employee | Law 52 of 1975 art. 1 |
| **Certificate of service** | On request | Time of service, nature of the work, salary earned | Labour Code art. 57 num. 7 |
| **Social-security payment evidence for the last 3 months** | **Within 60 days of termination** | To the employee's last registered address. **Without it the termination does not take effect** | Labour Code art. 65 par. 1 |
| **Overtime register extract** | On request | The employee is expressly entitled to see it | Labour Code art. 162 num. 2; Circular 101 of 2025 §3 |

### Is there a formal process for correcting errors discovered after the fiscal year has been closed?

**Yes — four separate processes, one per authority. There is no single "prior-year adjustment" mechanism.**

| Error | Correction route | Time limit |
|---|---|---|
| **Withholding-tax return (Form 350) understated** | File a **correction return** increasing the declared value. Tax Code art. 588: within **2 years** of the filing deadline; a correction penalty applies | 2 years |
| **Withholding-tax return overstated** | Correction under **Tax Code art. 589**, which reduces the declared value. Must be filed within **1 year** of the original filing deadline | **1 year** |
| **Withholding practised in excess of, or otherwise than in accordance with, the law** | **Decree 1625 of 2016 art. 1.2.4.16**: on the employee's written request with evidence, the employer reimburses the excess and **deducts the reimbursed amount from the withholdings of the following period**, carrying any surplus forward until absorbed. The employer retains the employee's written request | Ongoing |
| **Social-security contributions under-declared** | **Correction planilla** (type N): paired records, an `A` group carrying the originally settled values and a `C` group carrying the corrected values. The sum of the contribution bases and of the day counts in the `C` records must be **greater than or equal to** those in the `A` records. Filed **only through the same information operator** that carried the original return, absent an authorisation from the financial superintendence. Late-payment interest accrues from each original due date | No statutory limit; the contributions authority's assessment powers run to **5 years** |
| **Social-security contributions over-declared** | The correction planilla is structurally designed for under-declaration. A genuine overpayment requires a **refund claim to each receiving entity** — the health insurer, pension administrator, occupational-risk insurer, family compensation fund, apprenticeship service or family welfare institute — each with its own procedure | Per entity |
| **Electronic payroll document wrong** | **Adjustment note** (`NominaIndividualDeAjuste`) — a replacement or cancellation document referencing the original by its unique identifier | Per the annex |
| **Information return (Format 2276) wrong** | Correction return through the tax authority's information-return service. Penalties apply for late, incorrect or incomplete information under Tax Code art. 651 |
| **Statutory benefits under-paid** | Pay the shortfall directly to the employee, with the applicable indemnity. The limitation period for the employee's claim is **3 years from the date the obligation became enforceable** (Labour Code art. 488, as substituted by Law 2466 of 2025 art. 62) | 3 years |
| **Severance savings deposited late or short** | Pay the shortfall plus **one day's salary for each day of delay** | — |

**Sequencing rule.** Where a single error affects more than one authority — for example an omitted
retrospective salary increase — correct in this order: (1) recompute the statutory benefits and pay the
employee; (2) file the social-security correction planillas for each affected month with interest; (3)
declare the tax effect in the **current** month's Form 350, since withholding tax follows the payment date;
(4) issue an adjustment note for the electronic payroll document; (5) reissue Form 220 if the year has been
certified.

*Legal basis: Tax Code (Decree-Law 624 of 1989) arts. 378, 379, 380, 386, 588, 589, 651, 850; Decree 1625
of 2016 arts. 1.2.4.16 and 1.6.1.13.2.40; Resolution DIAN 000022 of 20 February 2024; Resolution DIAN
000013 of 2021 arts. 5, 22, 24, 26; Resolution DIAN 000227 of 2025; Substantive Labour Code arts. 57
(nums. 7 and par. 4), 65 par. 1, 115, 120, 162 num. 2, 187 num. 3, 232, 249, 253, 306, 488 (as substituted
by Law 2466 of 2025 arts. 7, 8, 12, 15, 62); Law 50 of 1990 art. 99; Law 52 of 1975 art. 1; Law 789 of 2002
art. 34 (as substituted by Law 2466 of 2025 art. 23); Resolution MSPS 2388 of 2016 Technical Annex 2;
Law 1581 of 2012; Decree 1074 of 2015; Ministry of Labour Circular 101 of 2025 §3.*
