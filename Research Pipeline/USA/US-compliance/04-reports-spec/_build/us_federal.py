# -*- coding: utf-8 -*-
"""Definitions of the 9 federal Report Specifications (IRS / SSA)."""
from decimal import Decimal

from us_common import (DD_REF, CCG_REF, PKG, tag, tagr, rid, url, src, fact, num, pct, m2, money, gap,
                       limitation, at, gap_subject, gap_close)
from us_rows import row, section, NONE_OPEN
from us_lines import line_rows, line_source_row, fs_line_table

FIELD_MODEL = "FIELD MODEL: logical model - not the wire/submission format"
PROVIDER = ("outbound via the third-party filing provider hand-off: the employer authorises the provider as "
            "reporting agent and keeps the liability; there is no ADP integration")
OUTBOUND = "Outbound statutory return (employer to authority, through the filing provider hand-off)"
RQ_941 = "RSPEC-RQ-01"
RQ_EFW2 = "RSPEC-RQ-02"
RQ_W2BOX = "RSPEC-RQ-03"
RQ_943 = "RSPEC-RQ-04"
RQ_1042S = "RSPEC-RQ-05"
RQ_ACA = "RSPEC-RQ-06"
RQ_941X = "RSPEC-RQ-07"
RQ_940 = "RSPEC-RQ-08"
RQ_SCHH = "RSPEC-RQ-09"


def accuracy(channel, portal, source, status, pct_txt, closes):
    return (f"Channel: {channel} | Portal: {portal} | Source: {source} | {status}. "
            f"Accuracy {pct_txt}. Closes with: {closes}.")


def ein_row(n, prefix, ctx):
    at(f"{prefix}-{n:03d}")
    return row("payroll", "Employer Identification Number (EIN)", "Employer identification number",
               "Header (employer)", f"{prefix}-{n:03d}", "Y", "Y",
               "Not conditional: every return identifies the employer.", "Logical field (field model)",
               "9 digits", "NN-NNNNNNN", "12-3456789 (fictitious)",
               f"{DD_REF}: employer FEIN (forward reference)",
               f"The employer's federal identification number, {tagr('fed.ein.format')}. It identifies the "
               f"employer on the {ctx} and must equal the EIN on every other federal return of the same employer. "
               f"Never truncated. {src('fed.ein.format')}",
               "Yes: employer master data", "Not applicable", "Not applicable", "N", "Identifier",
               "Per return")


def name_row(n, prefix, ctx):
    at(f"{prefix}-{n:03d}")
    return row("payroll", "Employer legal name and address", "Name and address", "Header (employer)",
               f"{prefix}-{n:03d}", "Y", "Y", "Not conditional: every return identifies the employer.",
               "Logical field (field model)", "Text", "Text", "Example Holdings Inc., 100 Main St, Springfield",
               f"{DD_REF}: employer legal name and address (forward reference)",
               f"Legal name and mailing address of the employer as registered with the IRS for the {ctx}. Taken "
               f"from employer master data; a change of address is reported by the employer through the IRS "
               f"channel, not by a payroll field. Source: {CCG_REF} Module 2 (employer registration).",
               "Yes: employer master data", "Not applicable", "Not applicable", "N", "Text", "Per return")


def common_remarks(extra=None):
    r = [("Scope", "One Report Specification per authority return in scope for the United States package "
                   f"v{PKG}. Field-level definitions of master data are owned by the Data Dictionary {DD_REF}; "
                   f"rules and rates by the Country Configuration Guide {CCG_REF}."),
         ("Channel", "Every return is transmitted by the third-party filing provider acting as reporting agent "
                     "(Form 8655 for federal returns). The payroll produces the data set of the field model; the "
                     "provider maps it to the authority wire format."),
         ("Limitations", "Open points are written in place with an open-point reference and listed in the Report "
                         "Matrix accuracy note. No value is assumed where the official source has not been read.")]
    if extra:
        r += extra
    return r


def special_block(rows):
    return ("SPECIAL CASES", rows)


# ===================================================================== 941 ===
def irs_941():
    P = "F941"
    at("IRS-001 metadata")
    freq = tag("rspec.fed.form941.frequency")
    rows = [section("HEADER: EMPLOYER AND PERIOD")]
    rows.append(ein_row(1, P, "Form 941"))
    rows.append(name_row(2, P, "Form 941"))
    at(f"{P}-003")
    rows.append(row("system", "Reporting quarter and year", "Quarter", "Header (period)", f"{P}-003", "N", "Y",
                    "Not conditional.", "Logical field (field model)", "6", "YYYYQn", "2026Q1",
                    "Payroll calendar (quarter of the payment date)",
                    f"Calendar quarter of the return. Form 941 is {freq} [{rid('rspec.fed.form941.frequency')}]. "
                    f"Wages are assigned to the quarter in which they are paid, not earned. "
                    f"{src('rspec.fed.form941.frequency')}",
                    "Yes: selects the payments aggregated", "Q1, Q2, Q3, Q4 (see Field Options)", "Not applicable",
                    "N", "Code", "Quarterly"))
    at(f"{P}-004")
    rows.append(row("constant", "Reporting agent authorisation", "Form 8655", "Header (agent)", f"{P}-004", "N", "Y",
                    "Not conditional: the build files every federal return through the provider.",
                    "Logical field (field model)", "Not applicable", "Text", "Authorisation on file",
                    "Provider hand-off configuration (system constant)",
                    f"The employer authorises the provider as reporting agent on {tagr('rspec.fed.reporting_agent.form')}; "
                    f"the agent may sign and file the return and make deposits while the employer keeps the "
                    f"liability ({tagr('fed.reporting_agent.authorization')}). The authorisation is held once per employer in "
                    f"the provider hand-off configuration as the form on file; it is not a line of Form 941. Without it on "
                    f"file the hand-off to the provider does not start (column N). {src('rspec.fed.reporting_agent.form')}",
                    "Yes: precondition of the hand-off", "Not applicable", "Not applicable", "N", "Flag",
                    "Once per employer"))
    rows.append(section("AMOUNTS FOR THE QUARTER (aggregated from payroll results)"))
    base = tag("fed.fica.oasdi.wage_base")
    at(f"{P}-005")
    rows.append(row("payroll", "Wages, tips and other compensation", "Wages, tips and other compensation",
                    "Amounts", f"{P}-005", "Y", "Y", "Not conditional.", "Logical field (field model)",
                    "Amount", "Decimal 13.2", "126,400.00", "Payroll result: federal taxable wages accumulator (quarter)",
                    f"Total of wages subject to federal income tax paid in the quarter: taxable earnings less pre-tax "
                    f"exclusions, as defined in {CCG_REF} Module 10 [US-FEDS5-031]. Amounts are reported in cents "
                    f"({tag('rspec.fed.form941.frequency')}). Treaty-exempt wages of nonresident aliens are excluded "
                    f"and reported on Form 1042-S [US-FEDS5-016].",
                    "Yes: quarter total of the FIT wage base", "Not applicable", "Cents (2 decimals), no rounding to dollars",
                    "N", "Amount", "Quarterly"))
    at(f"{P}-006")
    rows.append(row("payroll", "Federal income tax withheld", "Federal income tax withheld", "Amounts", f"{P}-006",
                    "Y", "Y", "Not conditional.", "Logical field (field model)", "Amount", "Decimal 13.2", "14,310.00",
                    "Payroll result: FIT withheld accumulator (quarter)",
                    f"Federal income tax withheld from wages paid in the quarter, as computed per period under "
                    f"{CCG_REF} Module 6 [US-FEDS5-031]. It must equal the sum of the FIT withheld on the period "
                    f"payroll results of the quarter. Reported in cents.",
                    "Yes: quarter total of FIT withheld", "Not applicable", "Cents (2 decimals)", "N", "Amount",
                    "Quarterly"))
    at(f"{P}-007")
    rows.append(row("payroll", "Taxable social security wages", "Taxable social security wages", "Amounts",
                    f"{P}-007", "Y", "Y", "Not conditional.", "Logical field (field model)", "Amount", "Decimal 13.2",
                    "118,500.00", "Payroll result: OASDI wage accumulator capped per employee per year",
                    f"Wages subject to social security tax paid in the quarter, capped per employee at the annual "
                    f"base of {base} [{rid('fed.fica.oasdi.wage_base')}]: per payment the taxable amount is the lesser "
                    f"of the remaining annual base and the period wages. Tax = wages x ({tag('fed.fica.oasdi.rate.employee')}% "
                    f"employee + {tag('fed.fica.oasdi.rate.employer')}% employer) [US-FEDS5-005]. Pay exempt under "
                    f"the F, J, M, Q rule or a totalization agreement is excluded (rows {P}-015, {P}-016).",
                    "Yes: OASDI base after the annual cap", "Not applicable", "Cents (2 decimals)", "N", "Amount",
                    "Quarterly"))
    at(f"{P}-008")
    rows.append(row("payroll", "Taxable Medicare wages and tips", "Taxable Medicare wages and tips", "Amounts",
                    f"{P}-008", "Y", "Y", "Not conditional.", "Logical field (field model)", "Amount", "Decimal 13.2",
                    "126,400.00", "Payroll result: Medicare wage accumulator (no cap)",
                    f"All wages subject to Medicare tax paid in the quarter, without annual cap. Tax = wages x "
                    f"({tag('fed.fica.medicare.rate.employee')}% employee + {tag('fed.fica.medicare.rate.employer')}% "
                    f"employer) [US-FEDS5-005]. Same exemptions as social security (rows {P}-015, {P}-016).",
                    "Yes: Medicare base", "Not applicable", "Cents (2 decimals)", "N", "Amount", "Quarterly"))
    at(f"{P}-009")
    rows.append(row("payroll", "Wages subject to Additional Medicare Tax withholding",
                    "Wages subject to Additional Medicare Tax withholding", "Amounts", f"{P}-009", "Y", "C",
                    f"Only for an employee whose year-to-date Medicare wages from this employer exceed "
                    f"{tag('fed.fica.addl_medicare.withholding_threshold')}; see also {P}-008.",
                    "Logical field (field model)", "Amount", "Decimal 13.2", "30,000.00",
                    "Payroll result: Additional Medicare wage accumulator",
                    f"Medicare wages paid in the quarter above the withholding threshold of "
                    f"{tagr('fed.fica.addl_medicare.withholding_threshold')} per employee per year; the employee-only "
                    f"rate is {tag('fed.fica.addl_medicare.rate')}%. Zero for employees below the threshold.",
                    "Yes: employee-only withholding", "Not applicable", "Cents (2 decimals)", "N", "Amount",
                    "Quarterly"))
    at(f"{P}-010")
    rows.append(row("payroll", "Total tax liability for the quarter", "Total taxes", "Amounts", f"{P}-010", "N", "Y",
                    "Not conditional.", "Logical field (field model)", "Amount", "Decimal 13.2", "See Example Analysis",
                    "Calculated by the return generator from rows F941-006 to F941-009",
                    f"FIT withheld plus social security tax (both shares) plus Medicare tax (both shares) plus Additional "
                    f"Medicare withheld. The generator computes it from the field model rows; it is never keyed. "
                    f"Rates: {tag('fed.fica.oasdi.rate.employee')}% + {tag('fed.fica.oasdi.rate.employer')}%, "
                    f"{tag('fed.fica.medicare.rate.employee')}% + {tag('fed.fica.medicare.rate.employer')}% [US-FEDS5-005].",
                    "Yes: reconciles to deposits", "Not applicable", "Cents (2 decimals)", "N", "Calculated",
                    "Quarterly"))
    at(f"{P}-011")
    rows.append(row("payroll", "Deposits made for the quarter", "Total deposits", "Amounts", f"{P}-011", "Y", "Y",
                    "Not conditional.", "Logical field (field model)", "Amount", "Decimal 13.2", "52,875.00",
                    "Payroll result: federal deposit register (EFTPS confirmations)",
                    f"Sum of the federal tax deposits made for the quarter. The deposit schedule depends on the "
                    f"lookback liability ({tag('rspec.fed.deposit.lookback_threshold')}; {tag('fed.deposit.lookback_period')}) "
                    f"[{rid('rspec.fed.deposit.lookback_threshold')}]. Balance due or overpayment = row {P}-010 minus "
                    f"this row. {src('rspec.fed.deposit.lookback_threshold')}",
                    "Yes: reconciliation of liability and deposits", "Not applicable", "Cents (2 decimals)", "Y",
                    "Amount", "Quarterly"))
    at(f"{P}-012")
    rows.append(row("system", "Depositor status", "Deposit schedule", "Deposit schedule", f"{P}-012", "N", "Y",
                    "Not conditional.", "Logical field (field model)", "1", "Code", "M",
                    f"{DD_REF}: employer federal depositor status (master data), forward reference",
                    f"Monthly depositor when the lookback liability is at most {tag('fed.deposit.monthly_max_lookback_liability')}, "
                    f"semiweekly above it; any day with {tag('fed.deposit.next_day_threshold')} or more accumulated is "
                    f"deposited the next business day [{rid('fed.deposit.monthly_max_lookback_liability')}]. The status "
                    f"is set once a year from the lookback period and drives the liability detail in row {P}-013.",
                    "Yes: deposit calendar", "M = monthly, S = semiweekly (Field Options)", "Not applicable", "N",
                    "Code", "Annual (status), quarterly (return)"))
    at(f"{P}-013")
    rows.append(row("payroll", "Tax liability by deposit period", "Liability detail", "Deposit schedule",
                    f"{P}-013", "Y", "C",
                    f"Content depends on {P}-012: monthly depositors give the liability of each month of the quarter; "
                    f"semiweekly depositors give the liability of each payday.",
                    "Logical field (field model)", "Amount per period", "Decimal 13.2", "Month 1: 17,625.00",
                    "Payroll result: liability per payment date",
                    f"Liability assigned to the date wages were paid, never to the period worked. Sum over the quarter "
                    f"must equal row {P}-010 (Form 941 line 12). Monthly depositors complete line 16 (row {P}-L21); "
                    f"semiweekly depositors attach Schedule B (row {P}-017): {tagr('rspec.fed.form941.schedule_b.structure')}.",
                    "Yes: proves timely deposits", "See Field Options (depositor status)",
                    "Cents (2 decimals)", "N", "Amount", "Quarterly"))
    rows.append(section("SPECIAL CASES"))
    at(f"{P}-014")
    rows.append(row("excluded", "Household and agricultural employees", "Excluded populations", "Scope filter",
                    f"{P}-014", "N", "C", "Excludes employees flagged household or agricultural.",
                    "Not applicable", "Not applicable", "Flag", "Household employee: not on Form 941",
                    f"{DD_REF}: employee category flags (household, agricultural), forward reference",
                    f"Agricultural labor is reported annually on Form 943 ({tag('fed.fica.return_period')}) "
                    f"[{rid('fed.fica.return_period')}]; household wages are reported by the household employer on "
                    f"Schedule H [US-FEDS5-029]. The generator excludes both populations from every amount of this return.",
                    "Yes: population filter", "Not applicable", "Not applicable", "N", "Flag", "Quarterly"))
    at(f"{P}-015")
    rows.append(row("payroll", "Nonresident alien FICA exemption (F, J, M, Q)", "Exempt pay", "Scope filter",
                    f"{P}-015", "Y", "C",
                    "Only for nonresident aliens holding F-1, J-1, M-1 or Q status whose services carry out the purpose of admission; "
                    f"back-reference to {P}-007 and {P}-008.", "Not applicable", "Not applicable", "Flag",
                    "J-1 researcher: social security and Medicare wages 0.00",
                    f"{DD_REF}: nonresident alien flag and visa class (forward reference)",
                    f"{tagr('fed.fica.nra.fjmq_exempt.scope')}. Exempt pay stays in the FIT wages of {P}-005 when it is "
                    f"not treaty-exempt, and is excluded from {P}-007 and {P}-008. Other visa classes are liable "
                    f"({tag('fed.fica.nra.other_visas.liable')}).",
                    "Yes: FICA base filter", "Visa classes: see Field Options", "Not applicable", "N", "Flag",
                    "Quarterly"))
    at(f"{P}-016")
    rows.append(row("payroll", "Totalization agreement exemption", "Certificate of coverage", "Scope filter",
                    f"{P}-016", "Y", "C",
                    f"Only for an employee holding a certificate of coverage under an agreement; back-reference to {P}-007 and {P}-008.",
                    "Not applicable", "Not applicable", "Flag", "Seconded employee with certificate: 0.00 FICA wages",
                    f"{DD_REF}: totalization country and exemption flag (forward reference)",
                    f"{tagr('fed.fica.totalization.exemption_rule')}. While the certificate is valid the employee's wages "
                    f"are excluded from the social security and Medicare amounts of the return. The flag and the agreement "
                    f"country come from the Data Dictionary (certificate of coverage on file, with its validity dates); the "
                    f"payroll excludes the wages only for pay dates inside that validity. The flag acts only on the social "
                    f"security and Medicare amounts (rows {P}-007 and {P}-008).",
                    "Yes: FICA base filter", "Not applicable", "Not applicable", "N", "Flag", "Quarterly"))
    at(f"{P}-017")
    rows.append(row("payroll", "Schedule B daily liability", "Report of Tax Liability for Semiweekly Schedule Depositors",
                    "Schedule B (Form 941)", f"{P}-017", "Y", "C",
                    f"Only for semiweekly depositors ({P}-012 = S) and for monthly depositors who accumulated a next-day "
                    f"liability; back-reference to {P}-013.", "Logical field (field model)", "Amount per day",
                    "Decimal 13.2", "Day 15 of Month 2: 17,625.00", "Payroll result: liability per payment date",
                    f"{tagr('rspec.fed.form941.schedule_b.structure')}. The total for the quarter equals Form 941 line 12 "
                    f"(row {P}-010). Each daily amount is the part of that liability arising on the payment date, taken from "
                    f"the payroll results per payment date, in cents. A day without wages paid is left empty; the schedule is "
                    f"attached only for the depositors named in column G. {src('rspec.fed.form941.schedule_b.structure')}",
                    "Yes: proves timely deposits", "Days 1 to 31 of Month 1, 2, 3", "Cents (2 decimals)", "N", "Amount",
                    "Quarterly"))
    rows.append(section("FORM 941 LINES (Rev. 3-2026), MAPPED TO THE FIELD MODEL"))
    rows.append(line_source_row(P, "rspec.fed.form941.line_map", "Form 941", "Quarterly"))
    lrows, lpr, _ = line_rows(P, "rspec.fed.form941.line_map", "Form 941", "Quarterly",
                              fm={"2": f"{P}-005", "3": f"{P}-006", "5a": f"{P}-007", "5c": f"{P}-008",
                                  "5d": f"{P}-009", "12": f"{P}-010", "13": f"{P}-011", "16": f"{P}-012 / {P}-013"},
                              mandatory={"1", "2", "3", "5a", "5c", "5e", "6", "10", "12", "13", "16"})
    rows += lrows

    matrix = [["US-IRS-001", "Form 941, Employer's Quarterly Federal Tax Return", "Form 941", "Internal Revenue Service (IRS)",
               f"{tag('rspec.fed.form941.frequency')}", f"{tag('rspec.fed.form941.frequency')}",
               "file_upload: electronic return transmitted by the reporting agent",
               f"Electronic return (e-file through the reporting agent). {FIELD_MODEL}.",
               f"[{rid('rspec.fed.form941.frequency')}] Publication 15 (2026); [{rid('rspec.fed.reporting_agent.form')}] Form 8655; "
               f"{url('rspec.fed.form941.frequency')}",
               accuracy("file_upload", "IRS e-file through the authorised reporting agent (Form 8655)",
                        url("rspec.fed.form941.frequency"), "TO CONFIRM",
                        "85% (Form 941 Rev. 3-2026 line map and Schedule B read; no real filing)",
                        "the provider import layout and one accepted real filing")]]
    scope_blocks = [
        ("WHO GETS REPORTED", [
            ("Common-law employees of a private-sector employer paid in the quarter", "YES",
             "Every employee with wages paid in the quarter enters the amounts of the return [US-OWN-008]."),
            ("Statutory employees (federal layer)", "YES",
             "Included at the federal layer; FICA applies, FIT per the CCG rules [US-OWN-005, US-FEDR3-005]."),
            ("Independent contractors (Form 1099-NEC)", "NO", "Out of scope by owner instruction [US-OWN-008]."),
            ("Household employees", "NO", "Reported by the household employer on Schedule H (US-IRS-005) [US-FEDS5-029]."),
            ("Agricultural employees", "NO", f"Reported on Form 943 (US-IRS-003): {tag('fed.fica.return_period')}."),
        ]),
        ("TIMING & RELATIONSHIP", [
            ("Quarterly return", "YES", f"{tag('rspec.fed.form941.frequency')} [{rid('rspec.fed.form941.frequency')}]."),
            ("Employer notified to file Form 944 instead", "NO",
             f"An employer notified in writing files Form 944 (US-IRS-002): {tag('rspec.fed.form944.rule')}."),
            ("Corrections of a filed quarter", "NO", "Filed on Form 941-X (US-IRS-008), never on a later Form 941."),
            ("Reconciliation with Forms W-2/W-3", "YES",
             "The four quarters must reconcile with the W-2/W-3 totals of the year (US-SSA-001) [US-FEDS5-031]."),
        ]),
        ("AMOUNTS & CALCULATIONS", [
            ("Social security wages capped per employee", "YES",
             f"Annual base {tag('fed.fica.oasdi.wage_base')}; lesser of remaining base and period wages."),
            ("Additional Medicare above the threshold", "YES",
             f"Employee-only {tag('fed.fica.addl_medicare.rate')}% above {tag('fed.fica.addl_medicare.withholding_threshold')}."),
            ("Amounts in cents", "YES", f"{tag('rspec.fed.form941.frequency')}."),
        ]),
        ("SPECIAL CASES", [
            ("Nonresident aliens in F, J, M or Q status", "PARTIAL",
             f"FIT wages reported; FICA amounts exclude exempt pay ({tag('fed.fica.nra.fjmq_exempt')})."),
            ("Employees under a totalization agreement", "PARTIAL", "FICA amounts exclude covered wages [US-FEDR2-003]."),
            ("Multistate employees", "YES", "Form 941 is federal; State amounts go to the State returns (US-DOR-001)."),
            ("US citizens or residents working abroad", "YES",
             "Included at the federal layer under the CCG rules [US-OWN-005, US-FEDR3-007]."),
        ]),
    ]
    # example
    at("F941 example")
    rate_e = pct("fed.fica.oasdi.rate.employee")
    rate_r = pct("fed.fica.oasdi.rate.employer")
    med_e = pct("fed.fica.medicare.rate.employee")
    med_r = pct("fed.fica.medicare.rate.employer")
    cap = num("fed.fica.oasdi.wage_base")
    ytd, q4 = Decimal("180000.00"), Decimal("15200.00")
    ss_w = min(q4, max(cap - ytd, Decimal(0)))
    ex = [("WORKED EXAMPLE 1: SOCIAL SECURITY CAP INSIDE A QUARTER (constructed)", [
        ("180,000.00", "Year-to-date wages before Q4", "Employee A, wages paid Q1-Q3", "Constructed input"),
        ("15,200.00", "Q4 wages paid", "Wages paid in Q4", "Constructed input"),
        (m2(cap - ytd), "Remaining annual base", f"{tag('fed.fica.oasdi.wage_base')} - 180,000.00",
         "Calculation"),
        (m2(ss_w), "Taxable social security wages Q4 (row F941-007)",
         "lesser of remaining base and Q4 wages", "Lesser-of rule, never annualised"),
        (m2(money(ss_w * rate_e)), "Social security tax, employee share",
         f"{m2(ss_w)} x {tag('fed.fica.oasdi.rate.employee')}%", "Half-up to the cent"),
        (m2(money(ss_w * rate_r)), "Social security tax, employer share",
         f"{m2(ss_w)} x {tag('fed.fica.oasdi.rate.employer')}%", "Half-up to the cent"),
        (m2(money(q4 * med_e)), "Medicare tax, employee share (row F941-008 base 15,200.00)",
         f"15,200.00 x {tag('fed.fica.medicare.rate.employee')}%", "No cap"),
        (m2(money(q4 * med_r)), "Medicare tax, employer share",
         f"15,200.00 x {tag('fed.fica.medicare.rate.employer')}%", "No cap"),
        ("0.00", "Additional Medicare wages (row F941-009)",
         f"year-to-date 195,200.00 does not exceed {tag('fed.fica.addl_medicare.withholding_threshold')}", "Threshold test"),
    ]), ("WORKED EXAMPLE 2: DEPOSITOR STATUS (constructed)", [
        ("48,250.00", "Lookback liability", f"Lookback period: {tag('fed.deposit.lookback_period')}", "Constructed input"),
        ("M", "Depositor status (row F941-012)",
         f"48,250.00 is not more than {tag('fed.deposit.monthly_max_lookback_liability')}: monthly depositor",
         "Comparison with the published limit"),
    ])]
    return dict(
        doc_id="US-IRS-001", report_name="Form941", sheet_name="Form 941 Spec",
        title="US-IRS-001 Form 941 Employer's Quarterly Federal Tax Return",
        authority="Internal Revenue Service (IRS), U.S. Department of the Treasury", report_type=OUTBOUND,
        tax_type="Federal income tax withheld, social security and Medicare (FICA)",
        relationship="Corrected by Form 941-X (US-IRS-008); replaced by Form 944 on IRS notice (US-IRS-002); "
                     "reconciles with Forms W-2/W-3 (US-SSA-001)",
        frequency=tag("rspec.fed.form941.frequency"), deadline=tag("rspec.fed.form941.frequency"),
        file_format=f"Electronic return (e-file through the reporting agent). {FIELD_MODEL}.",
        extension="Provider-defined (logical field model)", encoding="Provider-defined",
        record_length="Not applicable (logical field model)",
        record_types="Header (employer, period, agent); Amounts; Deposit schedule; Special cases; Form 941 lines (Rev. 3-2026)",
        official_source=f"{url('rspec.fed.form941.frequency')} [{rid('rspec.fed.form941.frequency')}]",
        last_update="Form 941 Rev. 3-2026, Schedule B Rev. 3-2024 and IRS Publication 15 (2026) as read for this release", similar_to="US-IRS-002 Form 944; US-IRS-003 Form 943",
        matrix_rows=matrix,
        scope_purpose="Who and what the quarterly federal employment tax return carries, built from the payroll "
                      "results of the wages paid in the quarter.",
        scope_blocks=scope_blocks, spec_rows=rows,
        fs_blocks=[("FILE FORMAT", [
            f"Submission: electronic return transmitted by the reporting agent ({tag('rspec.fed.reporting_agent.form')}).",
            f"{FIELD_MODEL}. The provider maps the field model to the IRS electronic return.",
            "The field model rows carry the amounts; the line rows of the core sheet map each form line to them.",
            "FORMAT TO CONFIRM vs a real filing."]),
            ("FORM 941 LINE MAP (Rev. 3-2026)", fs_line_table("rspec.fed.form941.line_map", "Form 941")),
            ("SCHEDULE B (FORM 941)", [f"{tag('rspec.fed.form941.schedule_b.structure')} [{rid('rspec.fed.form941.schedule_b.structure')}]"]),
            ("RECORD STRUCTURE", ["Header (one per return): EIN, name and address, quarter, agent authorisation.",
                                  "Amounts (one per return): rows F941-005 to F941-011.",
                                  "Deposit schedule: depositor status and liability per month or per payday.",
                                  "Special cases: population filters applied before aggregation.",
                                  "Form lines: one row per line of Form 941 Rev. 3-2026, mapped to the field model."])],
        fo_blocks=[("DEPOSITOR STATUS (F941-012)", [
            ("Depositor status", "M", "Monthly depositor", "Monthly schedule depositor",
             f"[{rid('fed.deposit.monthly_max_lookback_liability')}]"),
            ("Depositor status", "S", "Semiweekly depositor", "Semiweekly schedule depositor",
             f"[{rid('fed.deposit.monthly_max_lookback_liability')}]")]),
            ("REPORTING QUARTER (F941-003)", [
                ("Quarter", f"Q{i}", f"Calendar quarter {i}", f"Quarter {i}", f"[{rid('rspec.fed.form941.frequency')}]")
                for i in range(1, 5)]),
            ("NONRESIDENT ALIEN VISA CLASS (F941-015)", [
                ("Visa class", "Per Data Dictionary", tag("dd.fed.nra.visa_class"), "Visa class as issued",
                 f"[{rid('dd.fed.nra.visa_class')}]")])],
        pr_blocks=[("MANDATORY FIELD RULES", [
            ("Header", "F941-001, F941-002, F941-003", "Employer master data; payroll calendar",
             "EIN, name and address come from employer master data; the quarter is the quarter of the payment date of "
             "each payroll included. A payroll paid on 2026-04-01 for March work belongs to Q2.",
             "Off-cycle payments are assigned to the quarter of their own payment date.")]),
            ("PAYROLL-SPECIFIC POPULATION RULES", [
                ("Conditional", "F941-009 Additional Medicare wages", "Payroll result",
                 f"Populate only with the Medicare wages of employees whose year-to-date Medicare wages from this employer exceed "
                 f"{tag('fed.fica.addl_medicare.withholding_threshold')}; the excess paid in the quarter is the base.",
                 "An employee crossing the threshold mid-quarter contributes only the part above the threshold."),
                ("Conditional", "F941-013 Liability by deposit period", "Payroll result",
                 "Monthly depositors (F941-012 = M) report the liability per calendar month of the quarter; semiweekly "
                 "depositors (S) report it per payday. The sum always equals F941-010.",
                 "A next-day deposit day still counts in the month or payday of the payment date."),
                ("Conditional", "F941-014 Household and agricultural employees", "Employee category flags",
                 "Exclude household employees (Schedule H routing, US-IRS-005) and agricultural employees (Form 943, US-IRS-003) "
                 "from every amount; a mixed employer files both returns.",
                 "An employee who changes category mid-year is split by payment date."),
                ("Conditional", "F941-015 NRA F/J/M/Q exemption", "Nonresident alien flag and visa class",
                 "For a nonresident alien in F-1, J-1, M-1 or Q status whose services carry out the purpose of admission, exclude "
                 "the pay from F941-007 and F941-008; keep it in F941-005 unless treaty-exempt (then Form 1042-S, US-IRS-006).",
                 "Status ends when the individual becomes a resident alien; FICA applies from that date."),
                ("Conditional", "F941-016 Totalization exemption", "Totalization flag",
                 "Exclude from F941-007 and F941-008 the wages of an employee holding a valid certificate of coverage under a "
                 "section 233 agreement for the period it covers.",
                 "A certificate received late does not change returns already filed; correct them on Form 941-X."),
                ("Conditional", "F941-017 Schedule B", "Payroll result",
                 "Semiweekly depositors (F941-012 = S), and monthly depositors who accumulated a next-day liability, report the "
                 "liability of each payment date in the day boxes of each month; the monthly totals add up to Form 941 line 12.",
                 "A payment date falling on the last day of a month stays in that month even if it is deposited in the next.")]),
            ("FORM 941 LINES", lpr),
            ("CROSS-FIELD VALIDATIONS", [
                ("Reconciliation", "F941-010, F941-011", "Generator",
                 "Total liability minus deposits gives the balance due or the overpayment; the four quarters of the year must "
                 "reconcile with the W-2/W-3 totals (US-SSA-001).",
                 "A difference found after filing is corrected on Form 941-X, not in the next quarter.")])],
        ex_blocks=ex,
        sample_note=("No official sample return is held and none is constructed. Verified channel: electronic return "
                     "transmitted by the authorised reporting agent (Form 8655). The provider produces the transmission "
                     "file from the field model."),
        remarks=common_remarks(),
    )
