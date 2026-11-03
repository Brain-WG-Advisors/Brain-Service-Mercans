# -*- coding: utf-8 -*-
"""Build 01-ccg/modules/m02_master_data.md from the CCG facts (US build)."""
from ccglib import *

U = "m02_master_data"
set_unit(U)
o = []
A = o.append
PKG = MAN("package", "version")
DD = f"US-DD-001 v{PKG}"

A("# Module 2: Master Data Configuration")
A("*Purpose: To define the mandatory employer and employee information for processing and reporting.*")
A("")
A(f"Field-level definitions (data types, formats, option lists, validations) are owned by the Data Dictionary {DD}"
  ". This module states which master data the law makes necessary and why; it does not "
  "reproduce the field tables.")

# ---------------------------------------------------------------- 2.1
A(H(2, "2.1 Employer Information"))
A(H(3, "What are the different boards or authorities where an employer must register?"))
A("An employer registers once at the federal level and then separately in every State (and locality) whose layer "
  "applies to at least one employee. Statutory filings in this build go through a third-party filing provider "
  "(build manifest `_scope.filing_channel`); the provider acts under the employer's authorisation, and the "
  f"employer stays liable: {Q('fed.reporting_agent.authorization')} {R('fed.reporting_agent.authorization')}.")
A("")
A("| Authority | Why the employer is known to it | Fact |")
A("|---|---|---|")
A(f"| Internal Revenue Service (IRS) | Federal income tax withholding and FICA on the quarterly return; FUTA on the annual return | {K('fed.form941.frequency')}; {K('fed.form940.due')} |")
A(f"| Social Security Administration (SSA) | Annual wage statements (W-2 Copy A) in the EFW2 file format | {K('fed.efw2.edition')} |")
A(f"| State revenue authority, each State where withholding applies | State income-tax withholding account and returns | {K('multi.ui_wage_report.routing')} |")
A(f"| State workforce (unemployment) agency of the `sui_state` | Unemployment insurance account and quarterly wage report | {K('multi.ui_wage_report.routing')}; {K('multi.sui.localization_test')} |")
A(f"| State Directory of New Hires | New-hire reports | {K('fed.newhire.deadline_days')}; {K('multi.newhire.designated_state')} |")
A(f"| State paid-leave / disability agencies where a programme exists | Contribution returns (for example the Washington combined Paid Leave and WA Cares quarterly report) | {K('wa.report.pfml_ltc.due')} |")
A(f"| Local tax collectors | Local income or payroll taxes with their own return | {COV('local_regimes')} |")
A("")
A(UNR("multi.newhire.registration_channel", "the channel through which a multistate employer registers its designated new-hire State with HHS is not established in the facts"))
def _ein():
    """fed.ein.format (Pub. 15 (2026) sec. 1, register US-FEDS5-029). QA r3c: agent 2 aligned the two facts
    files on one wording and one register row; render that single fact. A divergence now fails the build
    (no fallback to a stale entry)."""
    vals = {(str(x["value"]), x["register_id"]) for x in FACTS["fed.ein.format"]}
    if len(vals) != 1:
        raise SystemExit(f"fed.ein.format is not aligned across facts files: {sorted(vals)}")
    return f"{T('fed.ein.format')} [{next(iter(vals))[1]}]"


A(H(3, "What is the configuration/format of registration numbers allotted by each authority?"))
A("The facts name the federal employer identification number (FEIN) as a required new-hire data element "
  f"({K('fed.newhire.fields')}) and state that the employer identification number is never truncated on wage statements "
  f"{R('fed.ssn.truncation.format')}. FEIN format: {_ein()}. The structure of the State withholding and unemployment "
  "account numbers is not established from an official source (limitation below).")
A("")
A(GAP("fed.registration.number_formats",
      "the format (length, separators, check rules) of each State withholding and unemployment account number is not in the facts",
      "What is the official format of the federal Employer Identification Number (length, hyphen position) per IRS, and the format of each State's withholding account number and unemployment account number per the issuing agency's specification?",
      "CCG m02 §2.1 registration-number formats empty; DD validation rules for employer identifiers cannot be sourced",
      "statutory_reporting", tier="A.2", shape="per authority: pattern, length, example format, source page"))
A(H(3, "Are registration numbers allotted at the central level or at the state/township level?"))
A("Both, in layers. The FEIN is one national number used on every federal return and on the new-hire report "
  f"({K('fed.newhire.fields')}). State withholding and unemployment accounts are separate registrations in each "
  f"State whose layer applies, because each State receives its own returns ({K('multi.ui_wage_report.routing')}). "
  "Where a locality administers its own tax, a local account is added (Module 6, local layer).")

# ---------------------------------------------------------------- 2.2
A(H(2, "2.2 Employee Information"))
A(H(3, "What are the different residential statuses for an individual?"))
A("Three independent residence tests apply, and each drives a different layer:")
A("")
A("| Test | Values | Drives | Fact |")
A("|---|---|---|---|")
A(f"| Federal tax residence | Resident (US citizen or resident alien) / nonresident alien (NRA) | Federal withholding method: NRA rules for Form W-4 and the NRA wage add-on (Module 6) | {K('fed.fit.nra.w4.rule')}; {COV('non_resident_employee')} |")
A(f"| State of residence vs State of work | Resident of the work State / nonresident of the work State / resident working in another State | Which State withholds on which wages (reciprocity, thresholds, convenience rules: Module 6) | {K('multi.sit.work_location.rule')}; {K('multi.pit.sourcing.general')} |")
A(f"| Local residence | Resident / nonresident of a taxing locality | Local rate (for example Philadelphia resident {T('pa.local.philadelphia.resident.rate', on='2026-07-01')}% / nonresident {T('pa.local.philadelphia.nonresident.rate', on='2026-07-01')}% from {D('pa.local.philadelphia.resident.rate', on='2026-07-01')}) | {R('pa.local.philadelphia.resident.rate', on='2026-07-01')} |")
A("")
A("State unemployment insurance does **not** follow residence: it follows the localization test, and residence is "
  f"only its last step ({Q('multi.sui.localization_test')} {R('multi.sui.localization_test')}). A military spouse may "
  f"elect a residence for State withholding: {Q('multi.military_spouse.rule', on='2026-07-01')} {R('multi.military_spouse.rule', on='2026-07-01')}.")
A(H(3, "What employee fields are required for processing payroll and statutory reporting?"))
A(f"The full field list is in {DD}. The law makes the following groups necessary:")
A("")
A("| Group | Required content | Why (fact) |")
A("|---|---|---|")
A(f"| Identity and hire | {Q('fed.newhire.fields')} | New-hire report within {T('fed.newhire.deadline_days')} days {R('fed.newhire.deadline_days')} |")
A(f"| Federal withholding certificate (Form W-4, 2020 or later) | {Q('fed.w4.input_fields')} | {R('fed.w4.input_fields')} |")
A(f"| Pre-2020 Form W-4 still in force | Number of allowances; each allowance is worth USD {T('fed.fit.allowance.pre2020_value')} in the computation | {R('fed.fit.allowance.pre2020_value')} |")
A(f"| Nonresident alien flag | Drives the NRA W-4 rule and the wage add-on table (Table 1 or Table 2) | {K('fed.fit.nra.w4.rule')}; {K('fed.fit.nra.addon.table2.annual')} |")
A(f"| Exempt-from-withholding claim | Valid for one year only: {Q('fed.w4.exempt.validity')} | {R('fed.w4.exempt.validity')} |")
A("| State withholding certificate | Per State; some States use their own form, some reuse the federal W-4, and a missing certificate has a State default (table below) | annexes |")
A("| Routing keys | `work_location_jurisdiction` (State and locality, down to school district), `residence_jurisdiction`, `sui_state` | build manifest `tier._sub_national_key` |")
A("| Reciprocity / nonresidence certificate | Certificate that stops work-State withholding for a resident of a partner State (table below) | `multi.reciprocity.*` |")
A(f"| State report fields | Examples: Alaska unemployment report {Q('ak.report.sui.employee_fields')} {R('ak.report.sui.employee_fields')}; Washington paid-leave report adds hours and date of birth {R('wa.report.pfml_ltc.fields')} | annexes |")
A("")
A("**State certificate defaults (examples).**")
A("")
A("| State | Certificate rule | Fact |")
A("|---|---|---|")
for k in ["ca.cert.default_no_certificate", "ct.cert.default_no_certificate", "nd.wh.certificate", "ut.wh.certificate",
          "ky.wh.certificate", "id.wh.certificate"]:
    A(f"| {k.split('.')[0].upper()} | {Q(k)} | {R(k)} |")
A("")
A("Idaho's certificate fact is the edition dated " + D("id.wh.certificate") + "; the 2026 edition is addressed in Annex ID (ID.2).")
A("")
A(f"**Joiners** ({COV('mid_month_joiner_and_leaver')}): the employee files Form W-4 and the State certificate at hire, "
  f"and the employer reports the hire to the State Directory of New Hires within {T('fed.newhire.deadline_days')} days "
  f"(shorter in many States, see annexes); electronic filers may instead use {Q('fed.newhire.electronic_interval')} "
  f"{R('fed.newhire.electronic_interval')}. A multistate employer reporting electronically may use one State: "
  f"{Q('multi.newhire.designated_state')} {R('multi.newhire.designated_state')}. States may fine up to USD "
  f"{T('fed.newhire.state_penalty.max_per_hire')} per unreported hire, or USD {T('fed.newhire.state_penalty.conspiracy.max_per_hire')} "
  f"where the failure results from a conspiracy {R('fed.newhire.state_penalty.max_per_hire')}. **Leavers** receive final pay "
  "under the work State's rule (Module 9).")
A(H(3, "What is the configuration/format of registration numbers (e.g., tax ID, social security number) allotted to employees?"))
A("The employee identifier on every federal and State filing is the Social Security number (SSN), named in the "
  f"new-hire data elements ({K('fed.newhire.fields')}). On employee copies of the W-2 it may be shown truncated, with "
  "only the last four digits visible (truncated taxpayer identification number); truncation is never allowed on "
  f"Copy A filed with SSA {R('fed.ssn.truncation.format')}. Washington accepts an SSN or an ITIN on its paid-leave "
  f"report {R('wa.report.pfml_ltc.fields')}.")
A("")
A(GAP("fed.ssn.format",
      "the SSN and ITIN structure (digit count, separators, invalid ranges) is not in the facts",
      "What is the official structure of the Social Security number and of the IRS Individual Taxpayer Identification Number (digit count, display format, ranges SSA/IRS state are never issued), per SSA and IRS publications?",
      "CCG m02 §2.2 employee-identifier format unstated; DD SSN/ITIN validation cannot be sourced",
      "payroll_data_protection", tier="A.2", shape="pattern and invalid ranges with source page"))
A(H(3, "Provide any relevant combo values or sample inputs for each field."))
A(f"Form W-4 (2020 or later) values, from {K('fed.w4.input_fields')}:")
A("")
A("| W-4 field | Combo values / input type |")
A("|---|---|")
A("| Step 1(c) filing status | Single or Married filing separately / Married filing jointly or Qualifying surviving spouse / Head of household |")
A("| Step 2 multiple jobs | Checked / not checked |")
A("| Step 3 dependents | Annual amount (USD) |")
A("| Step 4(a) other income | Annual amount (USD) |")
A("| Step 4(b) deductions | Annual amount (USD) |")
A("| Step 4(c) extra withholding | Amount per pay period (USD) |")
A("| Exempt | Checked / not checked (one year) |")
A("")
A("Reciprocity certificates (combo value = certificate on file, yes or no), from the multistate facts:")
A("")
A("| Work State | Partner States | Certificate | Fact |")
A("|---|---|---|---|")
for st in ["dc", "ia", "il", "in", "ky", "md", "mi", "mn", "mt", "nd", "nj", "oh", "pa", "va", "wi", "wv"]:
    pk = f"multi.reciprocity.{st}.partners"
    ck = f"multi.reciprocity.{st}.certificate"
    on = "2026-07-01" if len(FACTS.get(pk, [])) > 1 else None
    part = Q(pk, on=on) if has(pk) else "see annex"
    cert = Q(ck) if has(ck) else "see annex"
    A(f"| {st.upper()} | {part} | {cert} | {R(ck) if has(ck) else R(pk, on=on)} |")
A(f"| AZ (one-way) | {Q('multi.reciprocity.az.unilateral')} | Form WEC | {R('multi.reciprocity.az.unilateral')} |")
A(H(3, "What previous employment information must new joiners declare?"))
A(f"None for federal payroll purposes. Each employer applies the withholding method and the wage bases independently "
  f"({COV('multiple_employers')}): the OASDI and FUTA bases are per employer, the Additional Medicare threshold of USD "
  f"{T('fed.fica.addl_medicare.withholding_threshold')} is applied per employer, and the employee coordinates income tax "
  f"across jobs on Form W-4 Step 2 {R('fed.w4.input_fields')}. Wages paid by a previous employer in the same year do not "
  f"count toward this employer's FUTA base, except successor carry-over on an acquisition: {Q('multi.futa.wage_base.scope')} "
  f"{R('multi.futa.wage_base.scope')}. Excess OASDI from several employers is refunded to the employee at assessment, not by "
  f"payroll ({COV('annual_regularisation')}).")
A("")
A(UNR("fed.common_paymaster.rule"))

# ---------------------------------------------------------------- 2.3
A(H(2, "2.3 Data Management and Retention"))
A(H(3, "What are the statutory requirements for payroll record retention (e.g., number of years)?"))
A("| Record | Retention | Fact |")
A("|---|---|---|")
A(f"| FLSA payroll records (29 CFR 516.5); supplementary records 2 years (516.6) | {T('fed.records.flsa.retention_years')} years | {R('fed.records.flsa.retention_years')} |")
A(f"| IRS employment-tax records | {T('fed.records.irs.retention_years')} years | {R('fed.records.irs.retention_years')} |")
A(f"| Davis-Bacon certified payroll (federal construction contracts) | {Q('fed.davis_bacon.certified_payroll.frequency')} | {R('fed.davis_bacon.certified_payroll.frequency')} |")
A("| State payroll records | Per State annex | annexes |")
A("")
A("Configure the longest applicable period per record type; the IRS period is the binding federal maximum in the facts.")
A(H(3, "Are there specific data privacy laws (like GDPR) that govern the storage and handling of employee payroll data?"))
A("The facts carry identifier-display rules, not a general data-protection statute:")
A("")
A("| Rule | Fact |")
A("|---|---|")
A(f"| SSN may be truncated to the last four digits on employee W-2 copies only, never on Copy A; the EIN is never truncated | {R('fed.ssn.truncation.format')} |")
A(f"| Maryland: {Q('md.payslip.ssn.prohibited') if not isinstance(FACTS['md.payslip.ssn.prohibited'][0]['value'], bool) else 'the SSN may not be printed on the wage check, any attachment, direct-deposit notice or card-credit notice'} | {K('md.payslip.ssn.prohibited')} |")
A("")
A("State rules on the SSN on pay statements are not established for several States (for example Arkansas, Georgia, "
  "Iowa, Illinois and Kentucky); each is stated in section 12 of the State annex.")
A("")
A(GAP("fed.payroll_data_protection.framework",
      "no fact states whether a general federal or State data-protection statute (beyond SSN display rules) governs the storage and handling of employee payroll data",
      "Which federal statutes or regulations, and which State statutes (for example State SSN-protection and data-breach laws), impose obligations on a private employer's storage, access and disposal of employee payroll data, with their sections?",
      "CCG m02 §2.3 privacy question answered only for SSN display; DD/PSL masking and retention rules incomplete",
      "payroll_data_protection", tier="A.1"))
A(H(3, "How should historical payroll data (e.g., from a previous provider) be handled for cumulative calculations?"))
A("Every federal and State base is an annual amount per employer, applied to wages **paid** in the calendar year "
  f"({COV('accrual_vs_payment')}). A mid-year conversion inside the same employer must therefore load year-to-date "
  "balances, or the new engine will restart each base and over-collect:")
A("")
A("| Accumulator to load | Why | Fact |")
A("|---|---|---|")
A(f"| OASDI taxable wages and tax | Base USD {T('fed.fica.oasdi.wage_base', on='2026-06-30')} in 2026 | {R('fed.fica.oasdi.wage_base', on='2026-06-30')} |")
A(f"| Medicare wages | Additional Medicare starts above USD {T('fed.fica.addl_medicare.withholding_threshold')} paid by this employer | {R('fed.fica.addl_medicare.withholding_threshold')} |")
A(f"| FUTA taxable wages | USD {T('fed.futa.wage_base')} per employer across all States | {K('multi.futa.wage_base.scope')} |")
A(f"| SUI taxable wages per State | State bases; many States credit wages already reported to another State in the same year (for example {K('multi.sui.other_state_wage_credit.ca')}) | `multi.sui.other_state_wage_credit.*` |")
A(f"| PFML/SDI taxable wages where capped | For example Washington paid leave capped at USD {T('wa.pfml.wage_cap.annual')} | {R('wa.pfml.wage_cap.annual')} |")
A(f"| Supplemental wages paid in the year | Mandatory {T('fed.fit.supplemental.mandatory_rate')}% applies above USD {T('fed.fit.supplemental.mandatory_threshold')} in the calendar year | {R('fed.fit.supplemental.mandatory_threshold')} |")
A(f"| W-2 box totals (federal, State, local) | The W-2 covers the whole calendar year | {K('fed.tax_year.basis')} |")
A(f"| Retirement deferrals and HSA contributions | Annual limits, for example elective deferrals USD {T('fed.retirement.401k.elective_deferral_limit')} | {R('fed.retirement.401k.elective_deferral_limit')} |")

write_module(U, "\n".join(o))
print("written", U)
