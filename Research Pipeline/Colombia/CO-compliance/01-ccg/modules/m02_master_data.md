# Module 2: Master Data Configuration

*Purpose: To define the mandatory employer and employee information for processing and reporting.*

> **Scope note (dev-team filtering rule).** This module gives concise field summaries and the rules that
> govern them. It does **not** reproduce the Data Dictionary field tables. For the complete field-level
> specification — data types, lengths, mandatory/conditional flags, option mappers and consumer mapping —
> see **CO-DD-001, the Colombia Data Dictionary**, and the report specifications CO-RPT-001 to CO-RPT-007.

## 2.1 Employer Information

### What are the different boards or authorities where an employer must register?

A Colombian employer must be registered with, or enrolled through, the following bodies before it can run
a compliant payroll. Only the first two are tax/labour registrations in the strict sense; the remainder
are mandatory affiliations to the social-protection funds.

| # | Authority or entity | What it is | Registration output | Chosen by |
|---|---|---|---|---|
| 1 | **DIAN** — National Tax and Customs Directorate | Tax authority. Registers the employer in the Single Tax Registry (*Registro Único Tributario*, RUT), authorises it as a withholding agent, and enables it for electronic payroll | **Tax identification number (NIT)** + verification digit; RUT certificate; electronic-payroll enablement and software identifier | Mandatory |
| 2 | **Chamber of Commerce** | Commercial registry of the municipality | Commercial registration (*matrícula mercantil*) — required for the small-business payroll-tax scales and for the part-time contribution regime of Law 2466 of 2025 art. 34 | Mandatory for commercial entities |
| 3 | **Occupational risk insurer (ARL)** | Insures workplace accident and occupational disease | Employer affiliation; risk class I–V **per work centre**; contribution rate | **Employer** |
| 4 | **Family compensation fund (CCF)** | Administers the family subsidy and receives the 4% payroll levy | Employer affiliation, generally by department | **Employer** |
| 5 | **SENA** — National Apprenticeship Service | Receives the 2% training levy; administers the apprentice quota | Enrolment is effected through the contribution return; the apprentice quota is set by SENA | Mandatory |
| 6 | **ICBF** — Colombian Family Welfare Institute | Receives the 3% family-welfare levy | Effected through the contribution return | Mandatory |
| 7 | **Health insurers (EPS)** and **pension administrators (AFP / Colpensiones)** | Receive health and pension contributions | The **employee** chooses; the employer must affiliate the employee | Employee |
| 8 | **Severance-savings fund** | Receives the annual severance-savings deposit | The **employee** chooses; affiliation is compulsory even where the employer pays severance savings directly (Labour Code art. 57 par. 4, added by Law 2466 of 2025 art. 15) | Employee |
| 9 | **Licensed information operator** | Private licensed operator through which the integrated contribution return is filed and paid. The employer never transacts directly with the government for social security | Operator account and employer file identifier | Employer |
| 10 | **Ministry of Labour** | Labour inspection. Receives the disability-hiring contract report within 15 days of signature (Law 2466 of 2025 art. 15) | Not a payroll registration; a reporting obligation | Mandatory where applicable |
| 11 | **UGPP** — Pension and Payroll-Levy Management Unit | Audits and collects social-protection contributions; cross-matches tax data against the contribution return | No registration; this is the employer's audit counterparty | — |

**Configuration consequence.** Items 3, 4 and 9 are **employer-level elections** that must be stored once
and inherited by every employee. Items 7 and 8 are **employee-level elections** that change on employee
initiative mid-year and are reported as change events on the contribution return.

### What is the configuration/format of registration numbers allotted by each authority?

| Identifier | Format | Validation | Consumed by |
|---|---|---|---|
| **Tax identification number (NIT)** | Numeric, **9–10 digits**, stored and transmitted **without dots, hyphens or the verification digit** | Issued by DIAN on RUT registration | Every statutory artefact |
| **Verification digit (DV)** | **1 digit**, 0–9, stored and transmitted as a **separate field** from the NIT | Computed by DIAN weighted modulus 11 — see below | Every statutory artefact |
| **Commercial registration number** | Alphanumeric, format set by each Chamber of Commerce | — | Small-business levy scales |
| **Occupational risk insurer code** | 6-digit institution code | From the contribution-return institution tables | Contribution return |
| **Family compensation fund code** | Institution code | From the contribution-return institution tables | Contribution return |
| **Electronic payroll software identifier** | String assigned by DIAN at software activation | Paired with a **secret PIN** that never appears in the XML | Electronic payroll XML |
| **Electronic payroll security code** | SHA-384 hexadecimal of `SoftwareID + PIN + document number` | Computed | Electronic payroll XML |
| **Document prefix and sequence** | Employer-defined; the document number is prefix + sequence and must be **unique per employee** | Global validation rule 90 rejects a repeat | Electronic payroll XML |

**Verification-digit algorithm (verified).** DIAN weighted modulus 11, weights applied right to left:

```
W = [3, 7, 13, 17, 19, 23, 29, 37, 41, 43, 47, 53, 59, 67, 71]
S = Σ (digit_i × W_i)      # i = 0 for the rightmost digit
R = S mod 11
DV = R          if R < 2
DV = 11 − R     if R ≥ 2
```

Verified against published pairs: NIT 902025831 → DV 4; NIT 800197268 → DV 4.

The number and its verification digit are always **two distinct fields**. Electronic-payroll validation
rules NIE038 and NIE041 require the employer number *"sin guiones ni DV"* in one attribute and the
verification digit in another. An engine that concatenates them will fail schema validation.

### Are registration numbers allotted at the central level or at the state/township level?

**Predominantly central.** Colombia is a unitary state; there is no state or provincial payroll tax and
no sub-national employer tax number.

| Level | Registrations |
|---|---|
| **Central (national)** | Tax identification number and RUT (DIAN); withholding-agent status; electronic-payroll enablement; apprenticeship and family-welfare levy obligations; health, pension and occupational-risk affiliation; severance-savings fund |
| **Municipal / departmental** | **Commercial registration** with the Chamber of Commerce of the municipality of domicile. **Family compensation fund** affiliation is in practice organised by department, and the fund's institution code differs accordingly |
| **Work-centre level** | The **occupational-risk class (I–V)** attaches to the *work centre*, not to the company. A company with a corporate office and a manufacturing plant legitimately carries **two different risk classes and two different rates**, and each employee's contribution follows the class of the centre where they work |

The three sub-national elements — Chamber of Commerce, family compensation fund and work-centre risk
class — are the only places where Colombian payroll registration is not purely national. Branches and
agencies trading under the same corporate name are **not** separate registrations: for the purposes of
the electronic/assisted contribution-return threshold, the headcount of all branches under the same legal
person is aggregated (Decree 780 of 2016 art. 3.2.3.9 par.).

*Legal basis: Tax Code (Decree-Law 624 of 1989) arts. 555-2, 868; Resolution DIAN 000013 of 2021 arts. 1,
5, 22; Decree 780 of 2016 arts. 3.2.3.9, 3.2.3.10, 3.2.3.11 (as substituted by Decree 1990 of 2016);
Decree 1072 of 2015 arts. 2.2.4.2.5.6, 2.2.4.3.6; Decree 768 of 2022; Law 21 of 1982 arts. 9, 12;
Law 89 of 1988 art. 1; Law 2466 of 2025 arts. 15, 34; Substantive Labour Code art. 57 par. 4.*

---

## 2.2 Employee Information

### What are the different residential statuses for an individual?

Colombia distinguishes residence for **tax** purposes from residence for **immigration and social
security** purposes. The two are independent, and payroll must carry both.

**(a) Tax residence — Tax Code article 10.** An individual is a Colombian tax resident where any of the
following holds:

| Test | Threshold |
|---|---|
| Physical presence | **More than 183 calendar days**, continuous or not, in any **365-day period**. Where the period straddles two years, residence attaches to the year in which the 183rd day falls |
| Diplomatic status | Serving abroad in a Colombian diplomatic or consular post and exempt from tax in the host state |
| Nationality-plus-connection | A Colombian national whose spouse, dependants, 50%+ of assets, 50%+ of income, or place of asset administration is in Colombia, or who is tax resident in a jurisdiction classified as a non-cooperative regime, unless 50%+ of income or assets are in the other jurisdiction |

| Status | Withholding treatment of employment income |
|---|---|
| **Resident** | Progressive table, Tax Code art. 383, after the full depuration of art. 388 |
| **Non-resident under an employment contract with a Colombian employer** | **The same progressive art. 383 table.** Article 383 is drafted by reference to the *source and nature* of the payment — payments *"arising from an employment relationship, or from a statutory and regulatory relationship"* — not by reference to the recipient's residence. A non-resident employee on a Colombian payroll is withheld exactly as a resident is |
| **Non-resident receiving non-employment Colombian-source income** | Flat 20% or 35% under Tax Code arts. 406–415, **outside payroll scope** |

This is a genuine Colombian peculiarity and it is set out in full in the resident/non-resident matrix at
Module 6.2.

**(b) Immigration and social-security status.** This drives the identity-document type and the
affiliation rules, not the tax rate:

| Status | Typical document | Social security |
|---|---|---|
| Colombian national | Citizen identity card (*cédula de ciudadanía*), code 13 | Full affiliation |
| Resident foreign national | Foreigner identity card (*cédula de extranjería*), code 22 | Full affiliation. Pension affiliation may be waived only where the employee proves affiliation to a pension system abroad (Decree 1072 of 2015 art. 2.2.1.2.1.4) |
| Regularised migrant | Temporary Protection Permit (PPT), Decree 216 of 2021 — **no code exists** in the electronic-payroll annex; see the open item below | Full affiliation |
| Migrant under the earlier regime | Special Permanence Permit (PEP), code 47 | Full affiliation |
| Non-resident foreign national | Passport, code 41 | Depends on the assignment structure |
| Authorised minor (15–17) | Identity card (*tarjeta de identidad*), code 12 | Full affiliation; restricted working hours |

**Open item.** The electronic-payroll annex is still at version 1.0 (February 2021) and contains **no
document-type code for the Temporary Protection Permit**, which post-dates it by one month and is now
held by the large majority of regularised Venezuelan migrants. Code 47 (its legally superseded
predecessor) is the only available proxy. Carried as an open item in the QA report.

### What employee fields are required for processing payroll and statutory reporting?

Summarised by group. The authoritative, field-level list — with types, lengths, mandatory/conditional
flags and per-artefact consumers — is in **CO-DD-001**.

| Group | Fields (summary) | Primary consumer |
|---|---|---|
| **Identity** | Document type (closed code list), document number (numeric only, no dots, no verification digit), first surname, second surname, first given name, other given names | XML, contribution return, Form 220, information return |
| **Contact and location** | Country, department, municipality (5-digit national statistics code), address of the place of work — all four required attributes on the worker element | XML |
| **Employment** | Hire date, termination date, period start and end, time worked, contract type (5 values), worker type, worker sub-type, internal employee number, pay frequency | XML, contribution return, calculation |
| **Remuneration structure** | Contractual monthly salary, salary actually paid in the period, all-inclusive-salary flag, salary-in-kind valuation, non-salary pact reference | Calculation, XML |
| **Working time** | Weekly hours (≤ 42 from 15 July 2026), days worked per week (5 or 6), designated obligatory rest day, 36-hour shift-system flag, telework mode | Calculation |
| **Social-security profile** | Health insurer code, pension administrator code, pension regime (public defined-benefit or private individual-account), severance-savings fund code, occupational-risk insurer and work centre, family compensation fund, high-risk pension activity flag, active-pensioner flag, multi-employer flag | Contribution return, calculation |
| **Withholding profile** | Withholding procedure (1 or 2), fixed withholding percentage, employee-requested higher rate, housing-loan interest, prepaid health premiums, dependants (count **and** each dependant's identity document), voluntary pension and long-term savings contributions, voluntary individual-account contributions, third-party meal payments | Calculation, Form 220, information return |
| **Payment** | Payment form, payment method, bank, account type, account number | XML, bank payment file |
| **Accumulators** | Rolling 6-month average labour income, rolling 12-month taxable payments, salary and non-salary totals for the 40% clamp, benefit accruals, leave balances, daily and weekly overtime counters | Calculation, information return |

**Two schema traps the engine must handle at implementation**, both documented in CO-DD-001 and the QA
report:

1. The worker document-number attribute is typed as an **integer** in the XML schema. A passport or
   foreign identity number containing letters cannot be schema-valid. No official workaround is published.
2. The **second surname is a required attribute**, yet many Colombians and virtually all foreign nationals
   have only one surname. A placeholder must be emitted or validation fails. No official guidance exists.

### What is the configuration/format of registration numbers (e.g., tax ID, social security number) allotted to employees?

**Colombia does not issue a separate social-security number.** The employee's **identity-document number
is the social-security identifier**, the tax identifier for withholding purposes, and the key across the
contribution return, the electronic payroll XML, the annual certificate and the information return. The
document type plus the document number together form the composite key.

| Document | Code | Format | Check digit |
|---|---|---|---|
| Citizen identity card (*cédula de ciudadanía*) | **13** | Numeric. Historic issues up to 8 digits; issues from the 1990s are 10 digits beginning with `1` (the 1,000,000,000 series) | **None** |
| Foreigner identity card (*cédula de extranjería*) | **22** | Numeric, typically 6–7 digits. Issued by Migración Colombia | **None** |
| Identity card, minors 7–17 (*tarjeta de identidad*) | 12 | Numeric | None |
| Civil birth registration | 11 | Numeric — under-7s, never an employee | None |
| Foreigner card, minors | 21 | Alphanumeric in practice — see the integer-typing trap above | None |
| Passport | 41 | **Alphanumeric** — see the integer-typing trap | None |
| Foreign identity document | 42 | Alphanumeric | None |
| Special Permanence Permit (PEP) | 47 | 15 numeric digits | None |
| National unique personal identifier (NUIP) | 91 | Numeric. **Employee use only** — this document type is not held in the tax-registry database |
| Tax identification number (NIT) | 31 | Numeric 9–10. Rare for an employee; used where the beneficiary is a legal person | Yes — separate field |
| Foreign tax number | 50 | Alphanumeric | — |

**Bank account.** Colombia does **not** use IBAN. Domestic account numbers are numeric, of bank-specific
length (commonly 10–17 digits), with no national check-digit standard. The account type is "savings"
(*ahorros*) or "current" (*corriente*).

### Provide any relevant combo values or sample inputs for each field.

| Field | Permitted values | Sample |
|---|---|---|
| Document type | 11, 12, 13, 21, 22, 31, 41, 42, 47, 50, 91 | `13` |
| Document number | Numeric, no separators, no verification digit | `1020304050` |
| Employer tax number / verification digit | 9–10 numeric / 1 numeric, separate fields | `900123456` / `7` |
| Contract type | 1 fixed-term · 2 indefinite · 3 specific work or task · 4 apprenticeship · 5 internship | `2` |
| Worker type | `01` dependent employee (standard private sector). Codes 18, 30, 47, 58 are public sector and out of scope | `01` |
| Worker sub-type | `00` not applicable · `01` employed old-age pensioner | `00` |
| Pay frequency | 1 weekly · 2 ten-day · 3 fourteen-day · 4 semi-monthly · 5 monthly · 6 other | `4` |
| Pension regime | Public defined-benefit (Colpensiones) · Private individual account | `Private individual account` |
| Occupational risk class | I, II, III, IV, V | `I` |
| Occupational risk rate | Decimal between the class minimum and maximum | `0.522` |
| Withholding procedure | `1` or `2` | `1` |
| All-inclusive salary flag | Boolean; requires salary ≥ 13 minimum wages and a **written** agreement | `false` |
| High-risk pension activity | Boolean, required attribute | `false` |
| Country / department / municipality | ISO 3166-1 alpha-2 · ISO 3166-2:CO · 5-digit national statistics code | `CO` / `CO-VAC` / `76520` (Palmira) |
| Payment method | 42 bank deposit · 45 bank credit transfer · 47 bank debit transfer · 10 cash · 20 cheque · 48/49 credit/debit card | `45` |
| Payment form | `1` cash settlement (the only published value) | `1` |
| Obligatory rest day | Weekday. **Sunday is presumed** unless a written agreement says otherwise | `Sunday` |
| Days worked per week | `5` or `6` | `5` |
| Weekly hours | ≤ 44 to 14 July 2026; ≤ **42** from 15 July 2026 | `42` |

### What previous employment information must new joiners declare?

Colombia has **no cumulative-withholding carry-over between employers** and **no P45-equivalent
document**. A new employer starts the employee's withholding calculation fresh, from its own payments
only. This is a material contrast with cumulative-withholding jurisdictions and must not be
mis-configured.

What the new joiner must nonetheless declare, and why:

| Declaration | Statutory purpose | Consequence if missing |
|---|---|---|
| **Health insurer, pension administrator, pension regime and severance-savings fund already chosen** | These are employee elections that survive a change of employer. The new employer affiliates to the **existing** entities | Wrong institution codes on the contribution return; rejected or misdirected contributions |
| **Whether the employee has another concurrent employer**, and the contribution base with that employer | Law 100 of 1993 art. 18 par. 1 — where there are two or more employers, contributions are made **proportionally** to each remuneration and accumulate up to the 25-minimum-wage ceiling, and *"contributions to the health system must be made on the same base"* | Over- or under-contribution against the shared ceiling; contribution-audit exposure |
| **Whether the employee is a pensioner in active service** | An old-age pensioner in active service does **not** contribute to pension; worker sub-type `01` | Incorrect pension deduction |
| **Dependants**, with each dependant's identity document, relationship and basis of dependency | Tax Code arts. 336 num. 3 and 387; the information return requires the dependant's document, not merely a count | Deduction disallowed; information-return rejection |
| **Housing-loan interest, prepaid health premiums, voluntary pension and long-term savings contributions** | Tax Code arts. 119, 126-1, 126-4, 387 — all employee-declared and evidence-backed | Over-withholding |
| **Withholding Procedure 2 only: months of service and taxable payments over the preceding 12 months** | Tax Code art. 386. Where the employee has served fewer than 12 months, the divisor is the actual number of months of service; a genuinely new hire is withheld on the month's own taxable payments until the first semi-annual calculation | Wrong fixed percentage for a whole semester |
| **Certificate of service from the previous employer** on request | Labour Code art. 57 num. 7 — time of service, nature of the work and salary earned | Seniority-driven entitlements (severance-savings base, indemnity tier, work-clothing eligibility) mis-set |

The employee's own annual income-tax return, not the payroll, reconciles income from multiple employers.
Nothing about the previous employer's withholding is imported into the new employer's calculation.

*Legal basis: Tax Code (Decree-Law 624 of 1989) arts. 10, 336, 383, 386, 387, 406–415; Law 100 of 1993
art. 18 par. 1 (as substituted by Law 797 of 2003 art. 5); Substantive Labour Code art. 57 num. 7;
Decree 1072 of 2015 art. 2.2.1.2.1.4; Decree 216 of 2021; Resolution DIAN 000013 of 2021 and Technical
Annex §§5.2.1, 5.3.3, 5.4, 5.5.1–5.5.4.*

---

## 2.3 Data Management and Retention

### What are the statutory requirements for payroll record retention (e.g., number of years)?

Colombia sets retention obligations in **three separate statutes with different periods**. The engine
must retain to the **longest applicable** period, which is effectively **ten years** for accounting and
tax-supporting payroll records.

| Record | Retention period | Source |
|---|---|---|
| **Accounting books and the vouchers supporting them** — which expressly includes the electronic payroll support document, since it is the tax voucher for payroll costs and deductions | **10 years** from the last entry | Commercial Code art. 28 and art. 60; Law 962 of 2005 art. 28 |
| **Electronic payroll XML and the DIAN validation message** | Must be conserved for the legal period applicable to the supporting document | Resolution DIAN 000013 of 2021 arts. 15 and 23 |
| **Third-party generation mandate**, where a provider generates or transmits the XML | Both parties keep the accrediting document | Resolution DIAN 000013 of 2021 art. 22 |
| **Tax-return supporting evidence**, including withholding calculations | Aligned to the tax-assessment limitation period — ordinarily 3 years from the filing deadline, extended to 5 years where losses are offset or a special regime applies | Tax Code arts. 632, 714 |
| **Labour claims limitation** | **3 years** from the date each obligation became enforceable — the period runs from enforceability, a clarification introduced by the labour reform | Labour Code art. 488, as substituted by Law 2466 of 2025 art. 62 |
| **Overtime register** — activity performed, total supplementary hours, split between day and night hours, and evidence of payment | No period stated; must be available on demand to employees, the labour inspectorate and the courts | Labour Code art. 162 num. 2, as substituted by Law 2466 of 2025 art. 12; Circular 101 of 2025 §3 |
| **Vacation register** — entry date, start and end of each vacation, remuneration paid | No period stated; kept as a special register | Labour Code art. 187 num. 3 |
| **Evidence of social-security payment for the last 3 months before termination** | Must be **delivered to the employee within 60 days** of termination; retained as proof | Labour Code art. 65 par. 1 |

**Mercans default: retain all Colombian payroll data for 10 years** from the end of the fiscal year to
which it relates. That satisfies every period above with margin.

**A retention rule with teeth.** Labour Code art. 65 par. 1 makes the *termination itself* conditional on
proving the last three months' contributions: *"If the employer does not prove payment of those
contributions, the termination of the contract shall have no effect"* — the employer may cure by paying within
the following 60 days with late-payment interest. The three months of contribution evidence is therefore
not merely archival; it is a legal precondition to an effective dismissal.

### Are there specific data privacy laws (like GDPR) that govern the storage and handling of employee payroll data?

**Yes.** Colombia has a comprehensive personal-data protection regime, of which payroll data is squarely
within scope.

| Instrument | Content relevant to payroll |
|---|---|
| **Political Constitution art. 15** | The fundamental right to *habeas data* — to know, update and rectify information held about oneself |
| **Law 1581 of 2012** (General Personal Data Protection Regime) | The principal statute. Establishes lawfulness, purpose, freedom, truthfulness, transparency, restricted access, security and confidentiality as governing principles; requires **prior, express and informed authorisation** from the data subject; grants rights of access, update, rectification, revocation and deletion |
| **Decree 1074 of 2015** (Single Commerce Regulatory Decree, Book 2 Part 2 Title 2 Chapter 25, compiling Decree 1377 of 2013) | Implementing rules: content of the privacy notice, form of authorisation, the mandatory **internal data-treatment policy**, transfer and transmission rules |
| **Law 1266 of 2008** | Financial and credit data — relevant where payroll data feeds a payroll-lending arrangement |
| **National Register of Databases** | Databases containing personal data must be registered with the Superintendence of Industry and Commerce, which is the supervisory authority and holds the sanctioning power |

Points that bind a payroll implementation:

1. **Sensitive data.** Health data — sickness certificates, disability certification, maternity records —
   is *sensitive* under Law 1581 art. 5. Processing requires explicit authorisation, the data subject may
   not be compelled to authorise, and access must be restricted to those with an operational need.
2. **International transfer.** Law 1581 art. 26 prohibits transfer to countries that do not provide
   adequate protection, unless the data subject has given express and unequivocal authorisation, or one
   of the listed exceptions applies, or the Superintendence has issued a declaration of conformity.
   Where Mercans processes Colombian payroll outside Colombia, the client's employee authorisation must
   cover the transfer, and a data-transmission agreement must be in place with Mercans as processor.
3. **Processor status.** Mercans acts as the *encargado del tratamiento* (processor); the client employer
   is the *responsable* (controller). The controller's data-treatment policy and privacy notice govern.
4. **Retention versus deletion.** The right to deletion does **not** override the statutory retention
   duties in the previous question. Where a legal or contractual duty to retain exists, deletion is
   refused on that basis and the record is retained to the statutory period.

### How should historical payroll data (e.g., from a previous provider) be handled for cumulative calculations?

Colombia has **few genuinely cumulative payroll calculations**, which makes a mid-year migration
materially simpler than in a cumulative-withholding jurisdiction — but the accumulators that do exist are
unforgiving if loaded wrongly.

**What is NOT cumulative (and must not be carried over):**

- Wage withholding tax under Procedure 1. Each month stands alone. There is no year-to-date true-up.
- Social security, occupational risk and the payroll levies. Each month stands alone on that month's
  contribution base.
- Contributions from a **previous employer**. Nothing is imported. Only a **concurrent** second employer
  matters, and only for the shared 25-minimum-wage ceiling.

**What IS cumulative and must be migrated — the mandatory opening-balance set:**

| Accumulator | Why it must be loaded | Consequence of omission |
|---|---|---|
| **Service date and continuous-service history** | Drives the severance-savings entitlement, the service-bonus proration, vacation accrual, the work-clothing three-month qualification and the dismissal-indemnity tier | Understated termination liability |
| **Severance-savings balance and the last deposit date** | The annual liquidation runs to 31 December and is deposited by 14 February | Late-deposit penalty of one day's salary per day of delay |
| **Accrued but unpaid service bonus** (since 1 January or 1 July) | Paid in two halves, by 30 June and by 20 December | Underpayment on the next payment date |
| **Vacation days accrued, taken and cash-compensated**, with accumulation age | Labour Code art. 190 — 6 days per year are non-accumulable; the remainder accumulates 2 years (4 for technical, specialised, trusted, management and certain foreign staff) | Loss of the employee's right, or an unquantified liability |
| **Rolling 12-month taxable payments** | Required for the June/December fixed-percentage recalculation under Withholding Procedure 2 | Wrong fixed percentage for a whole semester |
| **Rolling 6-month average labour income** | Required for the severance-savings exemption taper (Tax Code art. 206 num. 4) and for field 33 of the information return | Wrong exemption on a termination payout |
| **Year-to-date figures for annual caps** — the 790-unit exempt-income cap, the 1,340-unit combined cap, the 72-unit-per-dependant deduction, the 3,800-unit voluntary-savings cap | These are **annual**, so a mid-year migration must load consumption to date | Caps breached; under-withholding and employee assessment exposure |
| **Year-to-date withholding**, split by counterparty type | Needed for the annual certificate (Form 220) and the information return | Certificate cannot be issued |
| **Salary and non-salary payment totals for the year** | Needed for the 40% non-salary clamp | Contribution base understated; audit exposure |
| **Meal payments within and above the monthly threshold** | Reported as two separate fields on the information return | Information-return rejection |
| **Severance savings paid to the employee, deposited to the fund, and under the pre-1991 regime** | **Three separate lines** on the information return | Information-return rejection |

**Migration procedure.**

1. **Cut over at a month end**, never mid-month. Both the contribution return and the electronic payroll
   XML are monthly artefacts keyed to the payment month; a mid-month cut-over splits an indivisible
   filing.
2. **Reconcile the opening balances to source**: the previous provider's payroll registers, the last 12
   contribution returns, the last electronic payroll validation messages, and the severance-savings fund
   statement.
3. **Load year-to-date consumption of every annual cap** as at the cut-over date.
4. **Verify institution codes** — health insurer, pension administrator, pension regime, severance-savings
   fund, occupational-risk insurer, work centre, family compensation fund — against the last filed
   contribution return, not against the HR record.
5. **Do not restate prior-period filings.** Corrections to periods filed by the previous provider are made
   through the correction mechanisms of each authority — the correction planilla for social security, an
   amended return for withholding tax, an adjustment note for the electronic payroll XML.
6. **Retain the previous provider's records** for the 10-year period; migration does not restart the clock.

*Legal basis: Commercial Code arts. 28 and 60; Law 962 of 2005 art. 28; Tax Code arts. 206 num. 4, 386,
632, 714; Substantive Labour Code arts. 65 par. 1, 162 num. 2, 187 num. 3, 190, 488 (as substituted by
Law 2466 of 2025 arts. 12 and 62); Resolution DIAN 000013 of 2021 arts. 15, 22, 23; Political
Constitution art. 15; Law 1581 of 2012; Decree 1074 of 2015; Law 1266 of 2008; Ministry of Labour
Circular 101 of 2025 §3.*
