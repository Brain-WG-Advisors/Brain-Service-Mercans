# Module 2: Master Data Configuration
*Purpose: To define the mandatory employer and employee information for processing and reporting.*

Field-level definitions (data types, formats, option lists, validations) are owned by the Data Dictionary US-DD-001 v1.0. This module states which master data the law makes necessary and why; it does not reproduce the field tables.

## 2.1 Employer Information

### What are the different boards or authorities where an employer must register?

An employer registers once at the federal level and then separately in every State (and locality) whose layer applies to at least one employee. Statutory filings in this build go through a third-party filing provider; the provider acts under the employer's authorisation, and the employer stays liable: Form 8655 (Rev. Jan 2024); agent may sign/file 940/941 and deposit; taxpayer stays liable [US-FED-008].

| Authority | Why the employer is known to it | Fact |
|---|---|---|
| Internal Revenue Service (IRS) | Federal income tax withholding and FICA on the quarterly return; FUTA on the annual return | `fed.form941.frequency` [US-FEDS5-031]; `fed.form940.due` [US-FEDS5-031] |
| Social Security Administration (SSA) | Annual wage statements (W-2 Copy A) in the EFW2 file format | `fed.efw2.edition` [US-FEDS5-032] |
| State revenue authority, each State where withholding applies | State income-tax withholding account and returns | `multi.ui_wage_report.routing` [US-MULTIS5-017] |
| State workforce (unemployment) agency of the `sui_state` | Unemployment insurance account and quarterly wage report | `multi.ui_wage_report.routing` [US-MULTIS5-017]; `multi.sui.localization_test` [US-MULTIS5-017] |
| State Directory of New Hires | New-hire reports | `fed.newhire.deadline_days` [US-FEDS5-024]; `multi.newhire.designated_state` [US-MULTIS5-006] |
| State paid-leave / disability agencies where a programme exists | Contribution returns (for example the Washington combined Paid Leave and WA Cares quarterly report) | `wa.report.pfml_ltc.due` [US-WAB5-003] |
| Local tax collectors | Local income or payroll taxes with their own return | coverage row `local_regimes` [US-PAS5-022, US-MIR3-002, US-INS5-009, US-MULTIS5-011] |

Not configured in this release (open gap RQ-527): The channel through which a multistate employer registers its designated new-hire State with HHS is not established from an official source.

### What is the configuration/format of registration numbers allotted by each authority?

The facts name the federal employer identification number (FEIN) as a required new-hire data element (`fed.newhire.fields` [US-FEDS5-024]) and state that the employer identification number is never truncated on wage statements [US-FEDS5-022]. FEIN format: nine-digit number issued by the IRS, arranged 00-0000000 [US-FEDS5-029]. The structure of the State withholding and unemployment account numbers is not established from an official source (limitation below).

Not configured in this release (open gap RQ-556): The format (length, separators, check rules) of each State withholding and unemployment account number is not established from an official source.

### Are registration numbers allotted at the central level or at the state/township level?

Both, in layers. The FEIN is one national number used on every federal return and on the new-hire report (`fed.newhire.fields` [US-FEDS5-024]). State withholding and unemployment accounts are separate registrations in each State whose layer applies, because each State receives its own returns (`multi.ui_wage_report.routing` [US-MULTIS5-017]). Where a locality administers its own tax, a local account is added (Module 6, local layer).

## 2.2 Employee Information

### What are the different residential statuses for an individual?

Three independent residence tests apply, and each drives a different layer:

| Test | Values | Drives | Fact |
|---|---|---|---|
| Federal tax residence | Resident (US citizen or resident alien) / nonresident alien (NRA) | Federal withholding method: NRA rules for Form W-4 and the NRA wage add-on (Module 6) | `fed.fit.nra.w4.rule` [US-FEDS5-015]; coverage row `non_resident_employee` [US-FEDS5-002, US-FEDS5-016, US-MULTIS5-017, US-MULTI-021, US-MULTIS5-013] |
| State of residence vs State of work | Resident of the work State / nonresident of the work State / resident working in another State | Which State withholds on which wages (reciprocity, thresholds, convenience rules: Module 6) | `multi.sit.work_location.rule` [US-MULTIS5-023]; `multi.pit.sourcing.general` [US-MULTIQ1-001] |
| Local residence | Resident / nonresident of a taxing locality | Local rate (for example Philadelphia resident 3.735% / nonresident 3.425% from 2026-07-01) | [US-PAS5-022] |

State unemployment insurance does **not** follow residence: it follows the localization test, and residence is only its last step (One State covers the entire service with one employer, in order: (1) localized (entirely in the State, or out-of-state service incidental: temporary, transitory, isolated); (2) else some service in the base-of-operations State; (3) else some service in the State of direction or control; (4) else some service in the State of residence [US-MULTIS5-017]). A military spouse may elect a residence for State withholding: A military spouse present in a State solely to be with the servicemember under military orders neither loses nor acquires residence or domicile; the spouse's income for services performed in that State is not income for services performed or from sources within that State if the spouse is not a resident of it; for any taxable year the spouse may elect the residence of the servicemember, the spouse's own residence or the permanent duty station (50 U.S.C. 4001(a)(2), (c)). Payroll effect: on the employee's State certificate of nonresidence, stop work-State withholding. [US-MULTIS5-005].

### What employee fields are required for processing payroll and statutory reporting?

The full field list is in US-DD-001 v1.0. The law makes the following groups necessary:

| Group | Required content | Why (fact) |
|---|---|---|
| Identity and hire | employee name, address, SSN, date services first performed; employer name, address, FEIN | New-hire report within 20 days [US-FEDS5-024] |
| Federal withholding certificate (Form W-4, 2020 or later) | filing status (Single/MFS, MFJ/QSS, HoH); Step 2 flag; Step 3 amount; Step 4(a); Step 4(b); Step 4(c); exempt checkbox | [US-FEDS5-006] |
| Pre-2020 Form W-4 still in force | Number of allowances; each allowance is worth USD 4,300 in the computation | [US-FEDS5-001] |
| Nonresident alien flag | Drives the NRA W-4 rule and the wage add-on table (Table 1 or Table 2) | `fed.fit.nra.w4.rule` [US-FEDS5-015]; `fed.fit.nra.addon.table2.annual` [US-FEDS5-002] |
| Exempt-from-withholding claim | Valid for one year only: 2026 only: the exemption checkbox certification lapses; a new W-4 is required for 2027 | [US-FEDS5-006] |
| State withholding certificate | Per State; some States use their own form, some reuse the federal W-4, and a missing certificate has a State default (table below) | annexes |
| Routing keys | `work_location_jurisdiction` (State and locality, down to school district), `residence_jurisdiction`, `sui_state` | tier classification |
| Reciprocity / nonresidence certificate | Certificate that stops work-State withholding for a resident of a partner State (table below) | `multi.reciprocity.*` |
| State report fields | Examples: Alaska unemployment report SSN, name, reportable wages, occupational code (6 or 8 digit), 2-digit geographic code [US-AKS5-013]; Washington paid-leave report adds hours and date of birth [US-WAB5-003] | annexes |

**State certificate defaults (examples).**

| State | Certificate rule | Fact |
|---|---|---|
| CA | No valid DE 4 -> Single, zero allowances; federal W-4 is for FIT only since 2020 | [US-CAS5-004] |
| CT | No CT-W4 -> withhold flat 6.99% without exemption | [US-CTS5-011] |
| ND | federal Form W-4 (no state certificate); none on file = single | [US-NDS5-001] |
| UT | federal W-4 filing status only (no Utah W-4; allowances ignored) | [US-UTS5-013] |
| KY | K-4 (42A804): no allowances; exemption claims only (no liability; Fort Campbell nonresident; SCRA/MSRRA; reciprocal-state residents) | [US-KYS5-013] |
| ID | federal W-4 required; Form ID W-4 (EFO00307) strongly encouraged: A Single/HoH, B Married, C Married at single rate; allowances = children 16 or under (+2 HoH) | [US-IDS5-013] |

Idaho's certificate fact is the edition dated 2025-04-28; the 2026 edition is addressed in Annex ID (ID.2).

**Joiners** (coverage row `mid_month_joiner_and_leaver` [US-FEDS5-001, US-FEDS5-024, US-MULTIS5-009]): the employee files Form W-4 and the State certificate at hire, and the employer reports the hire to the State Directory of New Hires within 20 days (shorter in many States, see annexes); electronic filers may instead use Electronic/magnetic filers: two monthly transmissions, not less than 12 nor more than 16 days apart [US-FEDB5-001]. A multistate employer reporting electronically may use one State: A multistate employer reporting electronically may send all new-hire reports to ONE designated State in which it has employees, after notifying HHS in writing [US-MULTIS5-006]. States may fine up to USD 25 per unreported hire, or USD 500 where the failure results from a conspiracy [US-FEDB5-001]. **Leavers** receive final pay under the work State's rule (Module 9).

### What is the configuration/format of registration numbers (e.g., tax ID, social security number) allotted to employees?

The employee identifier on every federal and State filing is the Social Security number (SSN), named in the new-hire data elements (`fed.newhire.fields` [US-FEDS5-024]). On employee copies of the W-2 it may be shown truncated, with only the last four digits visible (truncated taxpayer identification number); truncation is never allowed on Copy A filed with SSA [US-FEDS5-022]. Washington accepts an SSN or an ITIN on its paid-leave report [US-WAB5-003].

Not configured in this release (open gap RQ-557): The SSN and ITIN structure (digit count, separators, invalid ranges) is not established from an official source.

### Provide any relevant combo values or sample inputs for each field.

Form W-4 (2020 or later) values, from `fed.w4.input_fields` [US-FEDS5-006]:

| W-4 field | Combo values / input type |
|---|---|
| Step 1(c) filing status | Single or Married filing separately / Married filing jointly or Qualifying surviving spouse / Head of household |
| Step 2 multiple jobs | Checked / not checked |
| Step 3 dependents | Annual amount (USD) |
| Step 4(a) other income | Annual amount (USD) |
| Step 4(b) deductions | Annual amount (USD) |
| Step 4(c) extra withholding | Amount per pay period (USD) |
| Exempt | Checked / not checked (one year) |

Reciprocity certificates (combo value = certificate on file, yes or no), from the multistate facts:

| Work State | Partner States | Certificate | Fact |
|---|---|---|---|
| DC | MD, VA (from the partner side; DC taxes no nonresident at all) | D-4A | [US-MULTI-016] |
| IA | IL | IA 44-016 (IL resident in IA); IL-W-5-NR (IA resident in IL) | [US-MULTI-018] |
| IL | IA, KY, MI, WI | IL-W-5-NR | [US-ILP51-001] |
| IN | KY, MI, OH, PA, WI (county tax still withheld) | WH-47 | [US-IN-002] |
| KY | IL, IN, MI, OH (unless 20% S-corp shareholder-employee), VA (daily commuters only), WV, WI | 42A809 | [US-MULTI-009] |
| MD | DC, PA, VA, WV (not for abode in MD > 6 months and 183+ days, except WV) | MW507 | [US-MULTI-008] |
| MI | IL, IN, KY, MN, OH, WI | per MI Guide 446 (form not named in the row) | [US-MULTI-010] |
| MN | MI, ND (employee returns home at least monthly) | MWR (yearly; copies to MN DOR by Mar 31) | [US-MULTI-013] |
| MT | see annex | MW-4 (annual renewal) | [US-MTP51-004] |
| ND | MN, MT | NDW-R (yearly, by Feb 28 or within 30 days) | [US-MULTI-014] |
| NJ | PA (compensation only) | NJ-165 (PA resident in NJ); REV-419EX (NJ resident with PA employer) | [US-MULTI-011] |
| OH | IN, KY, MI, PA, WV | IT 4 (combined certificate) | [US-MULTI-005] |
| PA | IN, MD, NJ, OH, VA, WV | REV-419 | [US-MULTI-007] |
| VA | DC, KY (daily commuters), MD, PA, WV | VA certificate (not named in the row; VA annex) | [US-MULTI-004] |
| WI | IL, IN, KY, MI | W-220 | [US-MULTI-006] |
| WV | KY, MD, OH, PA, VA | WV/IT-104 | [US-MULTI-015] |
| AZ (one-way) | AZ exempts residents of CA, IN, OR, VA on Form WEC (they can claim the AZ credit); one-way - an AZ resident working in CA is withheld by CA | Form WEC | [US-MULTIB5-401] |

### What previous employment information must new joiners declare?

None for federal payroll purposes. Each employer applies the withholding method and the wage bases independently (coverage row `multiple_employers` [US-FEDS5-006, US-MULTIS5-009, US-FEDS5-005]): the OASDI and FUTA bases are per employer, the Additional Medicare threshold of USD 200,000 is applied per employer, and the employee coordinates income tax across jobs on Form W-4 Step 2 [US-FEDS5-006]. Wages paid by a previous employer in the same year do not count toward this employer's FUTA base, except successor carry-over on an acquisition: FUTA 7,000 counts remuneration paid by the employer in the calendar year across all States: one base per employer, not per State; successor carry-over [US-MULTIS5-009]. Excess OASDI from several employers is refunded to the employee at assessment, not by payroll (coverage row `annual_regularisation` [US-FEDS5-007, US-FEDS5-005, US-FEDS5-006]).

Not configured in this release (open gap RQ-533): Common-paymaster relief for related employers (multiple_employers row) is not established from an official source.

## 2.3 Data Management and Retention

### What are the statutory requirements for payroll record retention (e.g., number of years)?

| Record | Retention | Fact |
|---|---|---|
| FLSA payroll records (29 CFR 516.5); supplementary records 2 years (516.6) | 3 years | [US-FEDS5-021] |
| IRS employment-tax records | 4 years | [US-FEDS5-003] |
| Davis-Bacon certified payroll (federal construction contracts) | weekly, to the contracting agency; prime responsible for subcontractors; optional form WH-347; records 3 years | [US-FEDS5-027] |
| State payroll records | Per State annex | annexes |

Configure the longest applicable period per record type; the IRS period is the binding federal maximum in the facts.

### Are there specific data privacy laws (like GDPR) that govern the storage and handling of employee payroll data?

The facts carry identifier-display rules, not a general data-protection statute:

| Rule | Fact |
|---|---|
| SSN may be truncated to the last four digits on employee W-2 copies only, never on Copy A; the EIN is never truncated | [US-FEDS5-022] |
| Maryland: the SSN may not be printed on the wage check, any attachment, direct-deposit notice or card-credit notice | `md.payslip.ssn.prohibited` [US-MDS5-008] |

State rules on the SSN on pay statements are not established for several States (for example Arkansas, Georgia, Iowa, Illinois and Kentucky); each is stated in section 12 of the State annex.

Not configured in this release (open gap RQ-558): No official source read for this release states whether a general federal or State data-protection statute (beyond SSN display rules) governs the storage and handling of employee payroll data.

### How should historical payroll data (e.g., from a previous provider) be handled for cumulative calculations?

Every federal and State base is an annual amount per employer, applied to wages **paid** in the calendar year (coverage row `accrual_vs_payment` [US-FED-003, US-FED-006, US-MULTIS5-009, US-MAS5-012]). A mid-year conversion inside the same employer must therefore load year-to-date balances, or the new engine will restart each base and over-collect:

| Accumulator to load | Why | Fact |
|---|---|---|
| OASDI taxable wages and tax | Base USD 184,500 in 2026 | [US-FEDS5-005] |
| Medicare wages | Additional Medicare starts above USD 200,000 paid by this employer | [US-FEDS5-005] |
| FUTA taxable wages | USD 7,000 per employer across all States | `multi.futa.wage_base.scope` [US-MULTIS5-009] |
| SUI taxable wages per State | State bases; many States credit wages already reported to another State in the same year (for example `multi.sui.other_state_wage_credit.ca` [US-MULTIS5-010]) | `multi.sui.other_state_wage_credit.*` |
| PFML/SDI taxable wages where capped | For example Washington paid leave capped at USD 184,500 | [US-WAB5-002] |
| Supplemental wages paid in the year | Mandatory 37% applies above USD 1,000,000 in the calendar year | [US-FEDS5-003] |
| W-2 box totals (federal, State, local) | The W-2 covers the whole calendar year | `fed.tax_year.basis` [US-FED-006] |
| Retirement deferrals and HSA contributions | Annual limits, for example elective deferrals USD 24,500 | [US-FED-023] |


## Fact index

Every value above with its key, effective period and register id.

| Key | Value | Effective | Register id |
|---|---|---|---|
| `ak.report.sui.employee_fields` | SSN, name, reportable wages, occupational code (6 or 8 digit), 2-digit geographic code | from 2026-01-01 | US-AKS5-013 |
| `ca.cert.default_no_certificate` | No valid DE 4 -> Single, zero allowances; federal W-4 is for FIT only since 2020 | from 2026-01-01 to 2026-12-31 | US-CAS5-004 |
| `ct.cert.default_no_certificate` | No CT-W4 -> withhold flat 6.99% without exemption | from 2026-01-01 | US-CTS5-011 |
| `fed.davis_bacon.certified_payroll.frequency` | weekly, to the contracting agency; prime responsible for subcontractors; optional form WH-347; records 3 years | from 2023-10-23 | US-FEDS5-027 |
| `fed.ein.format` | nine-digit number issued by the IRS, arranged 00-0000000 | from 2026-01-01 | US-FEDS5-029 |
| `fed.fica.addl_medicare.withholding_threshold` | 200,000 | from 2026-01-01 to 2026-12-31 | US-FEDS5-005 |
| `fed.fica.oasdi.wage_base` | 184,500 | from 2026-01-01 to 2026-12-31 | US-FEDS5-005 |
| `fed.fit.allowance.pre2020_value` | 4,300 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.supplemental.mandatory_rate` | 37 | from 2026-01-01 | US-FEDS5-003 |
| `fed.fit.supplemental.mandatory_threshold` | 1,000,000 | from 2026-01-01 | US-FEDS5-003 |
| `fed.futa.wage_base` | 7,000 | from 2025-01-01 | US-FED-007 |
| `fed.newhire.deadline_days` | 20 | from 1997-10-01 | US-FEDS5-024 |
| `fed.newhire.electronic_interval` | Electronic/magnetic filers: two monthly transmissions, not less than 12 nor more than 16 days apart | from 1997-10-01 | US-FEDB5-001 |
| `fed.newhire.fields` | employee name, address, SSN, date services first performed; employer name, address, FEIN | from 1997-10-01 | US-FEDS5-024 |
| `fed.newhire.state_penalty.conspiracy.max_per_hire` | 500 | from 1997-10-01 | US-FEDB5-001 |
| `fed.newhire.state_penalty.max_per_hire` | 25 | from 1997-10-01 | US-FEDB5-001 |
| `fed.records.flsa.retention_years` | 3 | from 2026-11-02 | US-FEDS5-021 |
| `fed.records.irs.retention_years` | 4 | from 2026-01-01 | US-FEDS5-003 |
| `fed.reporting_agent.authorization` | Form 8655 (Rev. Jan 2024); agent may sign/file 940/941 and deposit; taxpayer stays liable | from 2012-11-19 | US-FED-008 |
| `fed.retirement.401k.elective_deferral_limit` | 24,500 | from 2026-01-01 to 2026-12-31 | US-FED-023 |
| `fed.w4.exempt.validity` | 2026 only: the exemption checkbox certification lapses; a new W-4 is required for 2027 | from 2026-01-01 to 2026-12-31 | US-FEDS5-006 |
| `fed.w4.input_fields` | filing status (Single/MFS, MFJ/QSS, HoH); Step 2 flag; Step 3 amount; Step 4(a); Step 4(b); Step 4(c); exempt checkbox | from 2026-01-01 to 2026-12-31 | US-FEDS5-006 |
| `id.wh.certificate` | federal W-4 required; Form ID W-4 (EFO00307) strongly encouraged: A Single/HoH, B Married, C Married at single rate; allowances = children 16 or under (+2 HoH) | from 2025-04-28 | US-IDS5-013 |
| `ky.wh.certificate` | K-4 (42A804): no allowances; exemption claims only (no liability; Fort Campbell nonresident; SCRA/MSRRA; reciprocal-state residents) | from 2026-01-01 | US-KYS5-013 |
| `multi.futa.wage_base.scope` | FUTA 7,000 counts remuneration paid by the employer in the calendar year across all States: one base per employer, not per State; successor carry-over | from 2026-01-01 | US-MULTIS5-009 |
| `multi.military_spouse.rule` | A military spouse present in a State solely to be with the servicemember under military orders neither loses nor acquires residence or domicile; the spouse's income for services performed in that State is not income for services performed or from sources within that State if the spouse is not a resident of it; for any taxable year the spouse may elect the residence of the servicemember, the spouse's own residence or the permanent duty station (50 U.S.C. 4001(a)(2), (c)). Payroll effect: on the employee's State certificate of nonresidence, stop work-State withholding. | from 2018-12-31 | US-MULTIS5-005 |
| `multi.newhire.designated_state` | A multistate employer reporting electronically may send all new-hire reports to ONE designated State in which it has employees, after notifying HHS in writing | from 2026-01-01 | US-MULTIS5-006 |
| `multi.reciprocity.az.unilateral` | AZ exempts residents of CA, IN, OR, VA on Form WEC (they can claim the AZ credit); one-way - an AZ resident working in CA is withheld by CA | from 2026-01-01 | US-MULTIB5-401 |
| `multi.reciprocity.dc.certificate` | D-4A | from 2026-01-01 | US-MULTI-016 |
| `multi.reciprocity.dc.partners` | MD, VA (from the partner side; DC taxes no nonresident at all) | from 2026-01-01 | US-MULTI-016 |
| `multi.reciprocity.ia.certificate` | IA 44-016 (IL resident in IA); IL-W-5-NR (IA resident in IL) | from 2026-01-01 | US-MULTI-018 |
| `multi.reciprocity.ia.partners` | IL | from 2026-01-01 | US-MULTI-018 |
| `multi.reciprocity.il.certificate` | IL-W-5-NR | from 2026-02-01 | US-ILP51-001 |
| `multi.reciprocity.il.partners` | IA, KY, MI, WI | from 2026-02-01 | US-ILS5-014 |
| `multi.reciprocity.in.certificate` | WH-47 | from 2026-01-01 | US-IN-002 |
| `multi.reciprocity.in.partners` | KY, MI, OH, PA, WI (county tax still withheld) | from 2026-01-01 | US-IN-002 |
| `multi.reciprocity.ky.certificate` | 42A809 | from 2026-01-01 | US-MULTI-009 |
| `multi.reciprocity.ky.partners` | IL, IN, MI, OH (unless 20% S-corp shareholder-employee), VA (daily commuters only), WV, WI | from 2026-01-01 | US-MULTI-009 |
| `multi.reciprocity.md.certificate` | MW507 | from 2026-01-01 | US-MULTI-008 |
| `multi.reciprocity.md.partners` | DC, PA, VA, WV (not for abode in MD > 6 months and 183+ days, except WV) | from 2026-01-01 | US-MULTI-008 |
| `multi.reciprocity.mi.certificate` | per MI Guide 446 (form not named in the row) | from 2026-01-01 | US-MULTI-010 |
| `multi.reciprocity.mi.partners` | IL, IN, KY, MN, OH, WI | from 2026-01-01 | US-MULTI-010 |
| `multi.reciprocity.mn.certificate` | MWR (yearly; copies to MN DOR by Mar 31) | from 2026-01-01 | US-MULTI-013 |
| `multi.reciprocity.mn.partners` | MI, ND (employee returns home at least monthly) | from 2026-01-01 | US-MULTI-013 |
| `multi.reciprocity.mt.certificate` | MW-4 (annual renewal) | from 2026-01-01 | US-MTP51-004 |
| `multi.reciprocity.nd.certificate` | NDW-R (yearly, by Feb 28 or within 30 days) | from 2026-01-01 | US-MULTI-014 |
| `multi.reciprocity.nd.partners` | MN, MT | from 2026-01-01 | US-MULTI-014 |
| `multi.reciprocity.nj.certificate` | NJ-165 (PA resident in NJ); REV-419EX (NJ resident with PA employer) | from 2026-01-01 | US-MULTI-011 |
| `multi.reciprocity.nj.partners` | PA (compensation only) | from 2026-01-01 | US-MULTI-011 |
| `multi.reciprocity.oh.certificate` | IT 4 (combined certificate) | from 2026-01-01 | US-MULTI-005 |
| `multi.reciprocity.oh.partners` | IN, KY, MI, PA, WV | from 2026-01-01 | US-MULTI-005 |
| `multi.reciprocity.pa.certificate` | REV-419 | from 2026-01-01 | US-MULTI-007 |
| `multi.reciprocity.pa.partners` | IN, MD, NJ, OH, VA, WV | from 2026-01-01 | US-MULTI-007 |
| `multi.reciprocity.va.certificate` | VA certificate (not named in the row; VA annex) | from 2026-01-01 | US-MULTI-004 |
| `multi.reciprocity.va.partners` | DC, KY (daily commuters), MD, PA, WV | from 2026-01-01 | US-MULTI-004 |
| `multi.reciprocity.wi.certificate` | W-220 | from 2026-01-01 | US-MULTI-006 |
| `multi.reciprocity.wi.partners` | IL, IN, KY, MI | from 2026-01-01 | US-MULTI-006 |
| `multi.reciprocity.wv.certificate` | WV/IT-104 | from 2026-01-01 | US-MULTI-015 |
| `multi.reciprocity.wv.partners` | KY, MD, OH, PA, VA | from 2026-01-01 | US-MULTI-015 |
| `multi.sui.localization_test` | One State covers the entire service with one employer, in order: (1) localized (entirely in the State, or out-of-state service incidental: temporary, transitory, isolated); (2) else some service in the base-of-operations State; (3) else some service in the State of direction or control; (4) else some service in the State of residence | from 2026-01-01 | US-MULTIS5-017 |
| `nd.wh.certificate` | federal Form W-4 (no state certificate); none on file = single | from 2026-01-01 to 2026-12-31 | US-NDS5-001 |
| `pa.local.philadelphia.nonresident.rate` | 3.425 | from 2026-07-01 | US-PAS5-022 |
| `pa.local.philadelphia.resident.rate` | 3.735 | from 2026-07-01 | US-PAS5-022 |
| `ut.wh.certificate` | federal W-4 filing status only (no Utah W-4; allowances ignored) | from 2026-01-01 | US-UTS5-013 |
| `wa.pfml.wage_cap.annual` | 184,500 | from 2026-01-01 to 2026-12-31 | US-WAB5-002 |
