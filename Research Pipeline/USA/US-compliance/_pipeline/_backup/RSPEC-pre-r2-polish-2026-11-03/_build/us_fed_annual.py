# -*- coding: utf-8 -*-
"""Federal Report Specifications: Form 944, Form 943, Form 940, Schedule H routing."""
import re
from decimal import Decimal

from us_common import (DD_REF, CCG_REF, tag, tagr, rid, url, src, num, pct, m2, money, gap, at, fact, per_draft,
                       retag, limitation, note_use)
from us_rows import row, section
from us_lines import line_rows, line_source_row, fs_line_table, split_top
from us_federal import (FIELD_MODEL, OUTBOUND, RQ_941, RQ_943, RQ_940, RQ_SCHH, accuracy, ein_row, name_row,
                        common_remarks)


def fed_book(doc_id, report_name, sheet, title, tax_type, relationship, frequency, deadline, file_format,
             record_types, official, last_update, similar, matrix, purpose, scope_blocks, rows, fs, fo, pr, ex,
             sample_note, extension="Provider-defined (logical field model)", encoding="Provider-defined",
             record_length="Not applicable (logical field model)",
             authority="Internal Revenue Service (IRS), U.S. Department of the Treasury", remarks=None,
             report_type=OUTBOUND):
    return dict(doc_id=doc_id, report_name=report_name, sheet_name=sheet, title=title, authority=authority,
                report_type=report_type, tax_type=tax_type, relationship=relationship, frequency=frequency,
                deadline=deadline, file_format=file_format, extension=extension, encoding=encoding,
                record_length=record_length, record_types=record_types, official_source=official,
                last_update=last_update, similar_to=similar, matrix_rows=matrix, scope_purpose=purpose,
                scope_blocks=scope_blocks, spec_rows=rows, fs_blocks=fs, fo_blocks=fo, pr_blocks=pr, ex_blocks=ex,
                sample_note=sample_note, remarks=remarks or common_remarks())


CORR = ("A correction after filing is never made on a later return: it goes through the correction route of the "
        "return named in the IRS instructions.")

NO_SAMPLE = ("No official sample is held and none is constructed. Verified channel: {ch}. The provider produces the "
             "transmission from the field model.")
AGENT = "electronic return transmitted by the authorised reporting agent"


def gap_field(n, prefix, name, rq, why, freq, section_label="Open point"):
    at(f"{prefix}-{n:03d}")
    return row("system", name, "Authority form lines", section_label, f"{prefix}-{n:03d}", "N", "C",
               "Applies once the open point is closed; the logical field model rows above are used meanwhile.",
               "Not configured in this release", "Not applicable", "Text", "No value configured",
               "Provider hand-off configuration (system constant)",
               f"{why} Not configured in this release {gap(rq)}. The return is prepared from the logical field model "
               f"and the provider's import layout until the authority layout is read.",
               "Yes: completeness of the return", "Not applicable", "Not applicable", "N", "Text", freq,
               f"Open point {gap(rq)}: read the official form and instructions for tax year 2026 and record the line map.")


def amount_rows(P, start, items, freq, mapping):
    out = []
    for n, (nm, expl, mand, cond) in enumerate(items, start=start):
        at(f"{P}-{n:03d}")
        out.append(row("payroll", nm, nm, "Amounts", f"{P}-{n:03d}", "Y", mand, cond,
                       "Logical field (field model)", "Amount", "Decimal 13.2", "See Example Analysis", mapping,
                       expl, f"Yes: {freq.lower()} total", "Not applicable", "Cents (2 decimals)", "N", "Amount", freq))
    return out


def ca_2025_example():
    """Example cell of the credit-reduction row: the 2025 California rate, bound to a 2025 fact.
    A dedicated 2025 CA rate key is used when the facts carry one; otherwise the 2025 list fact is tagged whole."""
    for k in ("fed.futa.credit_reduction.ca.rate", "fed.futa.credit_reduction.ca.final.rate",
              "rspec.fed.futa.credit_reduction.ca.rate"):
        try:
            f = fact(k, "2025")
        except KeyError:
            continue
        if str(f.get("effective_from") or "").startswith("2025"):
            return f"CA {tag(k, '2025')}% (2025)"
    return f"2025 list: {tag('rspec.fed.futa.credit_reduction.states', '2025')}"


# ===================================================================== 944 ===
def irs_944():
    P = "F944"
    at("IRS-002 metadata")
    rows = [section("HEADER: EMPLOYER AND YEAR"), ein_row(1, P, "Form 944"), name_row(2, P, "Form 944")]
    at(f"{P}-003")
    rows.append(row("constant", "Form 944 filing requirement (IRS notice)", "Notice to file Form 944", "Header (eligibility)",
                    f"{P}-003", "N", "Y", "Not conditional: the return exists only for an employer notified in writing.",
                    "Logical field (field model)", "1", "Flag", "Y",
                    f"{DD_REF}: employer federal return type (Form 941 or Form 944), forward reference",
                    f"Form 944 is filed {tagr('rspec.fed.form944.rule')}, replacing the four Forms 941 of the year. The "
                    f"maximum liability is {tag('fed.form944.max_liability')}. Without the IRS notice the employer files "
                    f"Form 941 (US-IRS-001). {src('rspec.fed.form944.rule')}",
                    "Yes: selects the annual return", "Y = Form 944 employer, N = Form 941 employer", "Not applicable",
                    "N", "Flag", "Annual"))
    at(f"{P}-004")
    rows.append(row("system", "Tax year", "Year", "Header (period)", f"{P}-004", "N", "Y", "Not conditional.",
                    "Logical field (field model)", "4", "YYYY", "2026", "Payroll calendar (year of the payment date)",
                    f"Calendar year of the return [{rid('rspec.fed.form944.rule')}]. Deposit lookback for Form 944 filers: "
                    f"{tag('fed.deposit.lookback_period')}.",
                    "Yes: selects the payments aggregated", "Not applicable", "Not applicable", "N", "Code", "Annual"))
    rows.append(section("AMOUNTS FOR THE YEAR"))
    nc = "Not conditional."
    rows += amount_rows(P, 5, [
        ("Wages, tips and other compensation", "Total wages subject to federal income tax paid in the year, same "
         "definition as row F941-005 of US-IRS-001 [US-FEDS5-031]. Same population filters as US-IRS-001 rows F941-014 to F941-016.", "Y", nc),
        ("Federal income tax withheld", "Federal income tax withheld from wages paid in the year [US-FEDS5-031], computed per "
         f"period as stated in {CCG_REF} Module 6. It is taken from the annual FIT withheld accumulator and must equal the sum "
         "of the FIT withheld on the period payroll results of the year (same definition as row F941-006 of US-IRS-001). "
         "Reported in cents, never negative. " + CORR, "Y", nc),
        ("Taxable social security wages", f"Wages subject to social security tax paid in the year, capped per employee at "
         f"{tag('fed.fica.oasdi.wage_base')} [{rid('fed.fica.oasdi.wage_base')}]: per payment the taxable amount is the lesser "
         f"of the remaining annual base and the period wages, so an employee crossing the base mid-year stops adding to this "
         f"field. Tax = wages x ({tag('fed.fica.oasdi.rate.employee')}% employee + {tag('fed.fica.oasdi.rate.employer')}% "
         f"employer) [US-FEDS5-005]. Taken from the OASDI wage accumulator of the payroll results, in cents; pay exempt under "
         f"the F, J, M, Q rule or a totalization agreement is excluded, as in US-IRS-001. " + CORR, "Y", nc),
        ("Taxable Medicare wages and tips", f"All wages and tips subject to Medicare tax paid in the year, without annual cap. "
         f"Tax = wages x ({tag('fed.fica.medicare.rate.employee')}% employee + {tag('fed.fica.medicare.rate.employer')}% "
         f"employer) [US-FEDS5-005]. Taken from the Medicare wage accumulator of the payroll results, in cents; the same "
         f"exemptions as social security apply. Additional Medicare Tax withholding above "
         f"{tag('fed.fica.addl_medicare.withholding_threshold')} per employee is reported on its own line of the form "
         f"(line rows below). " + CORR, "Y", nc),
        ("Deposits made for the year", f"Sum of the federal tax deposits made for the year, taken from the federal deposit "
         f"register of the payroll (EFTPS confirmations), in cents. The deposit schedule depends on the lookback liability "
         f"({tag('rspec.fed.deposit.lookback_threshold')}; {tag('fed.deposit.lookback_period')}) "
         f"[{rid('rspec.fed.deposit.lookback_threshold')}]. Balance due or overpayment = the total tax of the year minus this "
         f"field; an overpayment is shown as such on the form, never as a negative deposit.", "Y", nc),
    ], "Annual", "Payroll result: annual accumulator")
    at(f"{P}-010")
    rows.append(row("system", "Due date of the 2026 return", "Due date", "Header (period)", f"{P}-010", "N", "Y",
                    "Not conditional.", "Not applicable", "Date", "YYYY-MM-DD", "2027-02-01",
                    "Filing calendar of the payroll (system constant)",
                    f"{tagr('rspec.fed.form944.due')}.{per_draft('rspec.fed.form944.due')} {src('rspec.fed.form944.due')}",
                    "Yes: filing calendar", "Not applicable", "Not applicable", "N", "Date", "Annual",
                    f"Confirm against the final 2026 revision [{rid('rspec.fed.form944.due')}]."))
    rows.append(section("FORM 944 LINES (2026), MAPPED TO THE FIELD MODEL"))
    rows.append(line_source_row(P, "rspec.fed.form944.line_map", "Form 944", "Annual"))
    lrows, lpr, _ = line_rows(P, "rspec.fed.form944.line_map", "Form 944", "Annual",
                              fm={"1": f"{P}-005", "2": f"{P}-006", "4a": f"{P}-007", "4c": f"{P}-008", "10": f"{P}-009"},
                              mandatory={"1", "2", "4a", "4c", "4e", "5", "7", "9", "10"})
    rows += lrows
    matrix = [["US-IRS-002", "Form 944, Employer's Annual Federal Tax Return", "Form 944", "Internal Revenue Service (IRS)",
               "Annual", tag("rspec.fed.form944.due"), "file_upload: electronic return transmitted by the reporting agent",
               f"Electronic return (e-file through the reporting agent). {FIELD_MODEL}.",
               f"[{rid('rspec.fed.form944.rule')}] Publication 15 (2026); {url('rspec.fed.form944.rule')}",
               accuracy("file_upload", "IRS e-file through the authorised reporting agent (Form 8655)",
                        url("rspec.fed.form944.rule"), "TO CONFIRM",
                        "80% (line map and due date per 2026 draft of Form 944; no real filing)",
                        "the final 2026 Form 944 and its instructions, and one accepted real filing")]]
    at("F944 example")
    ex = [("WORKED EXAMPLE: ELIGIBILITY (constructed)", [
        ("940.00", "Expected annual liability", "Constructed input", "Input"),
        ("Y", "Form 944 employer (row F944-003)",
         f"940.00 does not exceed {tag('fed.form944.max_liability')} and the IRS notice is on file", "Both conditions required"),
    ])]
    return fed_book(
        "US-IRS-002", "Form944", "Form 944 Spec", "US-IRS-002 Form 944 Employer's Annual Federal Tax Return",
        "Federal income tax withheld, social security and Medicare (FICA)",
        "Replaces the four Forms 941 (US-IRS-001) for a notified employer; reconciles with Forms W-2/W-3 (US-SSA-001)",
        "Annual", tag("rspec.fed.form944.due"), f"Electronic return (e-file through the reporting agent). {FIELD_MODEL}.",
        "Header; Amounts; Form 944 lines (2026)", f"{url('rspec.fed.form944.rule')} [{rid('rspec.fed.form944.rule')}]",
        "Form 944 for 2026 (IRS early-release draft) and IRS Publication 15 (2026)", "US-IRS-001 Form 941", matrix,
        "Employers notified by the IRS to file one annual return instead of four quarterly returns.",
        [("WHO GETS REPORTED", [("Employers notified in writing by the IRS", "YES", tag("rspec.fed.form944.rule")),
                                ("Employers without the notice", "NO", "They file Form 941 (US-IRS-001).")]),
         ("TIMING & RELATIONSHIP", [("Annual return", "YES", f"One return per calendar year; {tag('rspec.fed.form944.due')}."),
                                    ("Quarterly Form 941 for the same year", "NO", "Never both for the same year.")]),
         ("AMOUNTS & CALCULATIONS", [("Same amount definitions as Form 941", "YES", "Rows F944-005 to F944-009.")]),
         ("SPECIAL CASES", [("Household and agricultural employees", "NO", "Schedule H (US-IRS-005) and Form 943 (US-IRS-003).")])],
        rows,
        [("FILE FORMAT", [f"{FIELD_MODEL}.", "The line rows of the core sheet map each form line to the field model "
                          "(per 2026 draft).", "FORMAT TO CONFIRM vs a real filing."]),
         ("RECORD STRUCTURE", ["Header; annual amounts; deposits; Form 944 lines."]),
         ("FORM 944 LINE MAP (2026 draft)", fs_line_table("rspec.fed.form944.line_map", "Form 944"))],
        [("FORM 944 EMPLOYER FLAG (F944-003)", [
            ("Return type", "Y", "Form 944 employer", "Annual return on IRS notice", f"[{rid('rspec.fed.form944.rule')}]"),
            ("Return type", "N", "Form 941 employer", "Quarterly returns", f"[{rid('rspec.fed.form941.frequency')}]")])],
        [("PAYROLL-SPECIFIC POPULATION RULES", [
            ("Conditional", "F944-003 Form 944 employer flag", "Employer master data",
             "Set the flag only on receipt of the IRS written notice; without it the payroll generates Form 941 every quarter. "
             "The flag is reviewed every year because the notice can be withdrawn.",
             "An employer whose liability grows above the limit during the year keeps the return type the IRS notified for that year.")]),
         ("CROSS-FIELD VALIDATIONS", [("Reconciliation", "F944-005 to F944-009", "Generator",
                                       "Annual amounts reconcile with the W-2/W-3 totals of the same year (US-SSA-001).",
                                       "The correction route for Form 944 is outside this release.")]),
         ("FORM 944 LINES", lpr)],
        ex, NO_SAMPLE.format(ch=AGENT))


# ===================================================================== 943 ===
# percentages printed in the Form 943 line labels, bound to their facts (C46): a rate that is a fact is
# re-tagged; a combined rate printed by the form (employee + employer share) is written as the sum of its facts.
FICA_RETAG = ("fed.fica.addl_medicare.rate", "fed.fica.oasdi.rate.combined", "fed.fica.medicare.rate.combined")
FICA_SUMS = (("fed.fica.medicare.rate.employee", "fed.fica.medicare.rate.employer"),
             ("fed.fica.oasdi.rate.employee", "fed.fica.oasdi.rate.employer"))
def irs_943():
    P = "F943"
    at("IRS-003 metadata")
    rows = [section("HEADER: EMPLOYER AND YEAR"), ein_row(1, P, "Form 943"), name_row(2, P, "Form 943")]
    at(f"{P}-003")
    rows.append(row("constant", "Agricultural employer return period", "Annual return", "Header (period)", f"{P}-003", "N", "Y",
                    "Not conditional.", "Logical field (field model)", "4", "YYYY", "2026", "Payroll calendar (year of the payment date)",
                    f"Agricultural labor is reported annually: {tagr('fed.fica.return_period')}. Deposit lookback for "
                    f"Form 943 filers: {tag('fed.deposit.lookback_period')}. {src('fed.fica.return_period')}",
                    "Yes: annual period", "Not applicable", "Not applicable", "N", "Code", "Annual"))
    rows.append(section("COVERAGE TESTS"))
    at(f"{P}-004")
    rows.append(row("payroll", "Agricultural FICA coverage test", "Coverage test", "Eligibility", f"{P}-004", "Y", "C",
                    "Applies to each agricultural employee; back-reference to F943-005.", "Logical field (field model)",
                    "1", "Flag", "Y",
                    f"{DD_REF}: agricultural employee flag (forward reference); payroll result: annual cash wages per worker",
                    f"Thresholds read from the source: {tagr('fed.agricultural.per_worker_threshold')} per worker and "
                    f"{tag('fed.agricultural.total_threshold')} in total for the year; FUTA coverage uses "
                    f"{tag('fed.agricultural.futa_quarter_threshold')} per quarter. How the tests combine is stated in "
                    f"{CCG_REF} Annex FED. {src('fed.agricultural.per_worker_threshold')}",
                    "Yes: decides whether wages enter the return", "Y = covered, N = not covered", "Not applicable", "N",
                    "Flag", "Annual"))
    rows.append(section("AMOUNTS FOR THE YEAR"))
    rows += amount_rows(P, 5, [
        ("Taxable social security wages (agricultural)",
         f"Cash wages paid in the year to agricultural employees who meet the coverage test of row F943-004, capped per "
         f"employee at {tag('fed.fica.oasdi.wage_base')} [US-FEDS5-005]: per payment the taxable amount is the lesser of the "
         f"remaining annual base and the period cash wages. Tax = wages x ({tag('fed.fica.oasdi.rate.employee')}% employee + "
         f"{tag('fed.fica.oasdi.rate.employer')}% employer). Taken from the agricultural OASDI wage accumulator, in cents; "
         f"non-cash pay and wages of employees below the coverage test are excluded. " + CORR,
         "C", "Only covered wages (F943-004 = Y)."),
        ("Taxable Medicare wages (agricultural)",
         f"All covered agricultural cash wages paid in the year, without annual cap [US-FEDS5-005]. Tax = wages x "
         f"({tag('fed.fica.medicare.rate.employee')}% employee + {tag('fed.fica.medicare.rate.employer')}% employer). Taken "
         f"from the agricultural Medicare wage accumulator, in cents; the coverage test of row F943-004 applies as for social "
         f"security, and Additional Medicare withholding is reported on its own line (line rows below). " + CORR, "C",
         "Only covered wages (F943-004 = Y)."),
        ("Federal income tax withheld (agricultural)",
         "Federal income tax withheld from agricultural wages paid in the year [US-FEDS5-031], computed per period as stated "
         f"in {CCG_REF} Module 6. Taken from the annual agricultural FIT withheld accumulator; it must equal the sum of the "
         "FIT withheld on the period payroll results of agricultural employees. Reported in cents, never negative. " + CORR,
         "Y", "Not conditional."),
        ("Deposits made for the year",
         f"Sum of the federal tax deposits made for the agricultural return of the year, taken from the federal deposit "
         f"register (EFTPS confirmations), in cents. The deposit schedule follows the lookback period: "
         f"{tag('fed.deposit.lookback_period')} [{rid('fed.deposit.lookback_period')}]. Balance due or overpayment = the total "
         f"tax of the year minus this field.",
         "Y", "Not conditional."),
    ], "Annual", "Payroll result: agricultural annual accumulator")
    at(f"{P}-009")
    rows.append(row("system", "Due date of the 2026 return", "Due date", "Header (period)", f"{P}-009", "N", "Y",
                    "Not conditional.", "Not applicable", "Date", "YYYY-MM-DD", "2027-02-01",
                    "Filing calendar of the payroll (system constant)",
                    f"{tagr('rspec.fed.form943.due')}.{per_draft('rspec.fed.form943.due')} {src('rspec.fed.form943.due')}",
                    "Yes: filing calendar", "Not applicable", "Not applicable", "N", "Date", "Annual",
                    f"Confirm against the final 2026 revision [{rid('rspec.fed.form943.due')}]."))
    rows.append(section("FORM 943 LINES (2026), MAPPED TO THE FIELD MODEL"))
    rows.append(line_source_row(P, "rspec.fed.form943.line_map", "Form 943", "Annual"))
    lrows, lpr, _ = line_rows(P, "rspec.fed.form943.line_map", "Form 943", "Annual",
                              fm={"2": f"{P}-005", "4": f"{P}-006", "8": f"{P}-007", "14": f"{P}-008"},
                              mandatory={"1", "2", "3", "4", "5", "8", "9", "11", "13", "14"},
                              retag_keys=FICA_RETAG, sums=FICA_SUMS)
    rows += lrows
    matrix = [["US-IRS-003", "Form 943, Employer's Annual Federal Tax Return for Agricultural Employees", "Form 943",
               "Internal Revenue Service (IRS)", "Annual", f"Annual ({tag('fed.fica.return_period')}); {tag('rspec.fed.form943.due')}",
               "file_upload: electronic return transmitted by the reporting agent",
               f"Electronic return (e-file through the reporting agent). {FIELD_MODEL}.",
               f"[{rid('fed.fica.return_period')}] [US-FEDR3-006] [US-FED-028] [{rid('rspec.fed.form943.line_map')}]; {url('fed.fica.return_period')}",
               accuracy("file_upload", "IRS e-file through the authorised reporting agent (Form 8655)", url("fed.fica.return_period"),
                        "TO CONFIRM", "80% (line map and due date per 2026 draft of Form 943; no real filing)",
                        "the final 2026 Form 943 and its instructions, and one accepted real filing")]]
    at("F943 example")
    ex = [("WORKED EXAMPLE: THRESHOLD COMPARISON (constructed)", [
        ("2,600.00", "Employer's total agricultural cash wages for the year", "Constructed input", "Input"),
        ("At or above", "Total test", f"2,600.00 against {tag('fed.agricultural.total_threshold')}",
         f"Combination of the tests per {CCG_REF} Annex FED"),
    ])]
    return fed_book(
        "US-IRS-003", "Form943", "Form 943 Spec", "US-IRS-003 Form 943 Employer's Annual Federal Tax Return for Agricultural Employees",
        "Federal income tax withheld, social security and Medicare (FICA) on agricultural wages",
        "Agricultural wages are excluded from Form 941 (US-IRS-001 row F941-014)", "Annual",
        f"Annual ({tag('fed.fica.return_period')}); {tag('rspec.fed.form943.due')}",
        f"Electronic return (e-file through the reporting agent). {FIELD_MODEL}.",
        "Header; Coverage tests; Amounts; Form 943 lines (2026)",
        f"{url('fed.fica.return_period')} [{rid('fed.fica.return_period')}] [US-FEDR3-006] [{rid('rspec.fed.form943.line_map')}]",
        "Form 943 for 2026 (IRS early-release draft); coverage figures as read for this release", "US-IRS-001 Form 941; US-IRS-002 Form 944", matrix,
        "Agricultural (farm) employees at the federal layer (US-OWN-005).",
        [("WHO GETS REPORTED", [("Agricultural employees meeting the coverage tests", "YES", "Row F943-004."),
                                ("Non-agricultural employees of the same employer", "NO", "Form 941 (US-IRS-001).")]),
         ("TIMING & RELATIONSHIP", [("Annual return", "YES", f"{tag('fed.fica.return_period')}; {tag('rspec.fed.form943.due')}")]),
         ("AMOUNTS & CALCULATIONS", [("Social security cap applies", "YES", tag("fed.fica.oasdi.wage_base"))]),
         ("SPECIAL CASES", [("State agricultural annual returns (e.g. OR Form WA)", "NO",
                             "State-level special-population rules are deferred to a later round [US-OWN-005].")])],
        rows,
        [("FILE FORMAT", [f"{FIELD_MODEL}.", "The line rows of the core sheet map each form line to the field model "
                          "(per 2026 draft).", "FORMAT TO CONFIRM vs a real filing."]),
         ("RECORD STRUCTURE", ["Header; coverage tests; annual amounts; Form 943 lines."]),
         ("FORM 943 LINE MAP (2026 draft)", fs_line_table("rspec.fed.form943.line_map", "Form 943",
                                                            retag_keys=FICA_RETAG, sums=FICA_SUMS))],
        [("COVERAGE FLAG (F943-004)", [("Covered", "Y", "Wages covered", "Covered agricultural wages", "[US-FEDR3-006]"),
                                       ("Covered", "N", "Wages not covered", "Below the tests", "[US-FEDR3-006]")])],
        [("PAYROLL-SPECIFIC POPULATION RULES", [
            ("Conditional", "F943-004 / F943-005 / F943-006", "Agricultural flag; annual cash wages",
             "Run the coverage tests at each payment on year-to-date cash wages per worker and in total; once covered, the wages "
             "of the year enter F943-005 and F943-006 from the first payment.",
             "Non-cash agricultural pay is outside the cash tests; a worker moving to non-agricultural duties is split by payment date.")]),
         ("FORM 943 LINES", lpr)],
        ex, NO_SAMPLE.format(ch=AGENT))


# ===================================================================== 940 ===
def irs_940():
    P = "F940"
    at("IRS-004 metadata")
    rows = [section("HEADER: EMPLOYER AND YEAR"), ein_row(1, P, "Form 940"), name_row(2, P, "Form 940")]
    at(f"{P}-003")
    rows.append(row("system", "Tax year", "Year", "Header (period)", f"{P}-003", "N", "Y", "Not conditional.",
                    "Logical field (field model)", "4", "YYYY", "2026", "Payroll calendar",
                    f"Calendar year of the FUTA return, due {tagr('rspec.fed.form940.due')}; for the 2026 return the due date "
                    f"falls in 2027 under the same rule. The final 2026 form and instructions are not yet issued; the line map "
                    f"below is per 2026 draft {gap('rspec.fed.form940.ty2026_instructions')}. {src('rspec.fed.form940.due')}",
                    "Yes: annual period", "Not applicable", "Not applicable", "N", "Code", "Annual"))
    rows.append(section("AMOUNTS FOR THE YEAR"))
    at(f"{P}-004")
    rows.append(row("payroll", "Total payments to employees", "Total payments", "Amounts", f"{P}-004", "Y", "Y", "Not conditional.",
                    "Logical field (field model)", "Amount", "Decimal 13.2", "30,000.00", "Payroll result: FUTA gross accumulator",
                    f"All payments to employees in the year before the FUTA wage base is applied [{rid('fed.futa.wage_base')}]. "
                    f"Exempt populations are removed by row F940-008.",
                    "Yes: starting amount", "Not applicable", "Cents (2 decimals)", "N", "Amount", "Annual"))
    at(f"{P}-005")
    rows.append(row("payroll", "FUTA taxable wages", "Taxable FUTA wages", "Amounts", f"{P}-005", "Y", "Y", "Not conditional.",
                    "Logical field (field model)", "Amount", "Decimal 13.2", "7,000.00",
                    "Payroll result: FUTA wage accumulator capped per employee",
                    f"Wages up to the first {tagr('fed.futa.wage_base')} per employee per year; the lesser of the remaining base "
                    f"and the period wages at each payment. {src('fed.futa.wage_base')}",
                    "Yes: FUTA base", "Not applicable", "Cents (2 decimals)", "N", "Amount", "Annual"))
    at(f"{P}-006")
    rows.append(row("payroll", "FUTA tax after the State credit", "FUTA tax", "Amounts", f"{P}-006", "N", "Y", "Not conditional.",
                    "Logical field (field model)", "Amount", "Decimal 13.2", "42.00", "Calculated by the return generator",
                    f"FUTA wages x net rate {tag('fed.futa.rate.net')}% (gross {tag('fed.futa.rate.gross')}% less the maximum State "
                    f"credit {tag('fed.futa.credit.max')}%) [{rid('fed.futa.rate.net')}]. {tag('fed.futa.legal_basis.state_credit')}. "
                    f"Wages paid in a credit-reduction State add the reduction on Schedule A (rows F940-009 to F940-011).",
                    "Yes: annual FUTA liability", "Not applicable", "Cents (2 decimals)", "N", "Calculated", "Annual"))
    at(f"{P}-007")
    rows.append(row("payroll", "FUTA liability by quarter and deposits", "Quarterly liability", "Deposit schedule", f"{P}-007",
                    "Y", "Y", "Not conditional.", "Logical field (field model)", "Amount per quarter", "Decimal 13.2",
                    "Q1: 42.00", "Payroll result: FUTA liability per quarter",
                    f"FUTA liability of each quarter and the deposits made for it. FUTA is deposited when the accumulated "
                    f"liability exceeds {tag('fed.futa.deposit_threshold')} [{rid('fed.futa.deposit_threshold')}]; a smaller "
                    f"amount carries to the next quarter ({tag('rspec.fed.form940.due')}). The quarterly liability is taken "
                    f"from the FUTA liability accumulator of the payroll results (FUTA wages of the quarter up to "
                    f"{tag('fed.futa.wage_base')} per employee for the year, x the net rate of row F940-006), in cents; a "
                    f"credit reduction of Schedule A is added to the fourth quarter only. The four quarters must add up to "
                    f"the total FUTA liability of the year.",
                    "Yes: deposit timing", "Q1 to Q4", "Cents (2 decimals)", "N", "Amount",
                    "Quarterly (deposits), annual (return)"))
    rows.append(section("SPECIAL CASES"))
    at(f"{P}-008")
    rows.append(row("payroll", "Exempt payments (NRA F, J, M, Q; household; agricultural)", "Exempt FUTA payments", "Scope filter",
                    f"{P}-008", "Y", "C", "Only for exempt populations; back-reference to F940-004 and F940-005.",
                    "Not applicable", "Not applicable", "Flag", "J-1 researcher: FUTA wages 0.00",
                    f"{DD_REF}: nonresident alien flag and visa class; employee category flags",
                    f"F, J, M, Q pay is exempt from FUTA ({tagr('fed.futa.nra.fjmq_exempt')}). Household employers report FUTA on "
                    f"Schedule H (US-IRS-005; quarter test {tag('fed.household.futa_quarter_threshold')}); agricultural FUTA "
                    f"coverage uses {tag('fed.agricultural.futa_quarter_threshold')} per quarter.",
                    "Yes: FUTA base filter", "Not applicable", "Not applicable", "N", "Flag", "Annual"))
    rows.append(section("SCHEDULE A (FORM 940): MULTI-STATE EMPLOYERS AND CREDIT REDUCTION"))
    at(f"{P}-009")
    rows.append(row("payroll", "Schedule A: States of UI contributions and credit reduction", "Schedule A (Form 940)",
                    "Schedule A", f"{P}-009", "Y", "C",
                    "Only for an employer that paid State unemployment tax in more than one State or paid wages in a "
                    "credit-reduction State (Form 940 lines 1b and 2); back-reference to F940-010.",
                    "Logical field (field model)", "Per State", "USPS code + Decimal 13.2", "CA: 7,000.00",
                    "Payroll result: FUTA taxable wages per UI State (US-UI-001 State of coverage)",
                    f"{tagr('rspec.fed.form940.schedule_a.structure')}.{per_draft('rspec.fed.form940.schedule_a.structure')} "
                    f"{src('rspec.fed.form940.schedule_a.structure')}",
                    "Yes: credit reduction per State", "USPS State codes", "Cents (2 decimals)", "N", "Amount", "Annual",
                    f"Confirm against the final 2026 revision [{rid('rspec.fed.form940.schedule_a.structure')}]."))
    at(f"{P}-010")
    rows.append(row("system", "Credit-reduction States and rates", "Credit reduction rate", "Schedule A", f"{P}-010", "N", "C",
                    "Applies only to FUTA wages paid in a State on the list for the year; back-reference to F940-009.",
                    "Not applicable", "Rate per State", "Percent", ca_2025_example(),
                    "System constant per year (credit-reduction table)",
                    f"Final list for 2025, shown for reference and for 2025 returns: "
                    f"{tag('rspec.fed.futa.credit_reduction.states', '2025')} "
                    f"({src('rspec.fed.futa.credit_reduction.states', '2025')}). Potential 2026 figures published by the U.S. "
                    f"Department of Labor (estimates, not final): California {tag('fed.futa.credit_reduction.ca.potential.rate')}%, "
                    f"Virgin Islands {tag('fed.futa.credit_reduction.vi.potential.rate')}% "
                    f"[{rid('fed.futa.credit_reduction.ca.potential.rate')}]. The 2026 list is applied only once final "
                    f"(row F940-011).",
                    "Yes: raises the fourth-quarter liability", "Per State", "Rate as published", "N", "Rate", "Annual"))
    at(f"{P}-011")
    rows.append(row("system", "2026 credit-reduction list", "Credit reduction 2026", "Schedule A", f"{P}-011", "N", "C",
                    "Applies once the final 2026 list is published; until then no 2026 credit reduction is configured.",
                    "Not applicable", "Rate per State", "Percent", "No value configured",
                    "System constant per year (credit-reduction table)",
                    limitation("rspec.fed.futa.credit_reduction.states_2026",
                               "2026 credit-reduction table not configured in this release") +
                    " A State added to the final list raises the fourth-quarter FUTA liability of wages paid there.",
                    "Yes: completeness of Schedule A", "Not applicable", "Not applicable", "N", "Rate", "Annual",
                    f"Open point {gap('rspec.fed.futa.credit_reduction.states_2026')}: the final 2026 list (published after "
                    f"the November repayment date)."))
    rows.append(section("FORM 940 LINES (2026), MAPPED TO THE FIELD MODEL"))
    rows.append(line_source_row(P, "rspec.fed.form940.line_map", "Form 940", "Annual"))
    lrows, lpr, _ = line_rows(P, "rspec.fed.form940.line_map", "Form 940", "Annual",
                              fm={"3": f"{P}-004", "7": f"{P}-005", "11": f"{P}-009", "12": f"{P}-006", "16a": f"{P}-007",
                                  "2": f"{P}-009", "1b": f"{P}-009"},
                              mandatory={"3", "7", "8", "12", "13"},
                              retag_keys=("fed.futa.wage_base", "fed.futa.deposit_threshold"))
    rows += lrows
    matrix = [["US-IRS-004", "Form 940, Employer's Annual Federal Unemployment (FUTA) Tax Return", "Form 940",
               "Internal Revenue Service (IRS)", "Annual", tag("rspec.fed.form940.due"),
               "file_upload: electronic return transmitted by the reporting agent",
               f"Electronic return (e-file through the reporting agent). {FIELD_MODEL}.",
               f"[{rid('rspec.fed.form940.due')}] [{rid('rspec.fed.form940.line_map')}] [{rid('fed.futa.wage_base')}]; {url('rspec.fed.form940.due')}",
               accuracy("file_upload", "IRS e-file through the authorised reporting agent (Form 8655)", url("rspec.fed.form940.due"),
                        "TO CONFIRM", "80% (line map and Schedule A per 2026 draft; 2026 credit-reduction list not final)",
                        f"the final 2026 Form 940 and instructions {gap('rspec.fed.form940.ty2026_instructions')} and the final "
                        f"2026 credit-reduction list {gap('rspec.fed.futa.credit_reduction.states_2026')}")]]
    at("F940 example")
    rate_net = pct("fed.futa.rate.net")
    base = num("fed.futa.wage_base")
    futa_w = min(Decimal("30000.00"), base)
    tax1 = money(futa_w * rate_net)
    net_chk = num("fed.futa.rate.gross") - num("fed.futa.credit.max")
    ex = [("WORKED EXAMPLE: FUTA FOR ONE EMPLOYEE (constructed)", [
        ("30,000.00", "Total payments (F940-004)", "Constructed input", "Input"),
        (m2(futa_w), "FUTA wages (F940-005)", f"lesser of 30,000.00 and {tag('fed.futa.wage_base')}", "Annual cap"),
        (f"{net_chk}", "Net rate check (%)",
         f"{tag('fed.futa.rate.gross')} - {tag('fed.futa.credit.max')} = {net_chk}; published net rate {tag('fed.futa.rate.net')}",
         "Arithmetic check of the published net rate"),
        (m2(tax1), "FUTA tax (F940-006)", f"{m2(futa_w)} x {tag('fed.futa.rate.net')}%", "Half-up to the cent"),
        (m2(tax1 * 13), "Accumulated liability, 13 such employees", f"{m2(tax1)} x 13", "Calculation"),
        ("Deposit due", "Deposit test (F940-007)", f"{m2(tax1 * 13)} exceeds {tag('fed.futa.deposit_threshold')}",
         "Comparison with the published limit"),
    ])]
    return fed_book(
        "US-IRS-004", "Form940", "Form 940 Spec", "US-IRS-004 Form 940 Employer's Annual Federal Unemployment (FUTA) Tax Return",
        "Federal unemployment tax (FUTA), employer only", "State UI contributions (US-UI-001) give the FUTA credit",
        "Annual", tag("rspec.fed.form940.due"), f"Electronic return (e-file through the reporting agent). {FIELD_MODEL}.",
        "Header; Amounts; Deposit schedule; Special cases; Schedule A; Form 940 lines (2026)",
        f"{url('rspec.fed.form940.due')} [{rid('rspec.fed.form940.due')}] [{rid('rspec.fed.form940.line_map')}]",
        "Form 940 and Schedule A for 2026 (IRS early-release draft); Instructions for Form 940 (2025 edition)",
        "US-UI-001 State UI wage reports", matrix,
        "Employer-only federal unemployment tax on the first FUTA wages of each employee.",
        [("WHO GETS REPORTED", [("Employees of a FUTA-liable employer", "YES", "FUTA base per employee."),
                                ("Nonresident aliens in F, J, M, Q status", "NO", tag("fed.futa.nra.fjmq_exempt"))]),
         ("TIMING & RELATIONSHIP", [("Annual return with quarterly deposits", "YES", tag("rspec.fed.form940.due"))]),
         ("AMOUNTS & CALCULATIONS", [("Annual wage base per employee", "YES", tag("fed.futa.wage_base")),
                                     ("Employee deduction", "NO", "FUTA is employer-only [US-FED-007].")]),
         ("SPECIAL CASES", [("Household employers", "NO", "Schedule H (US-IRS-005)."),
                            ("Multistate employers", "YES", "One federal return; State credit per State of UI coverage; Schedule A (F940-009)."),
                            ("Wages paid in a credit-reduction State", "YES",
                             f"Schedule A; 2025 final list {tag('rspec.fed.futa.credit_reduction.states', '2025')}; 2026 list not final "
                             f"{gap('rspec.fed.futa.credit_reduction.states_2026')}.")])],
        rows,
        [("FILE FORMAT", [f"{FIELD_MODEL}.", "The line rows of the core sheet map each form line to the field model "
                          "(per 2026 draft).", "FORMAT TO CONFIRM vs a real filing."]),
         ("RECORD STRUCTURE", ["Header; annual amounts; quarterly liability; exemptions; Schedule A; Form 940 lines."]),
         ("FORM 940 LINE MAP (2026 draft)", fs_line_table("rspec.fed.form940.line_map", "Form 940")),
         ("SCHEDULE A (FORM 940)", [f"{tag('rspec.fed.form940.schedule_a.structure')} [{rid('rspec.fed.form940.schedule_a.structure')}]"])],
        [("QUARTER (F940-007)", [("Quarter", f"Q{i}", f"Calendar quarter {i}", f"Quarter {i}",
                                  f"[{rid('fed.futa.deposit_threshold')}]") for i in range(1, 5)])],
        [("PAYROLL-SPECIFIC POPULATION RULES", [
            ("Conditional", "F940-008 exempt payments", "Employee flags",
             "Exclude F, J, M, Q pay of nonresident aliens, household wages (Schedule H) and agricultural wages below the "
             "agricultural FUTA test from F940-004 and F940-005; they never generate FUTA liability on this return.",
             "A household employer that also has business employees reports the business wages here and the household wages on Schedule H.")]),
         ("CROSS-FIELD VALIDATIONS", [("Reconciliation", "F940-006, F940-007", "Generator",
                                       "The quarterly liabilities add up to the annual FUTA tax; deposits equal the liability less the "
                                       "amount carried below the deposit threshold.",
                                       "A credit reduction raises the liability of the fourth quarter.")]),
         ("SCHEDULE A AND CREDIT REDUCTION", [
             ("Conditional", "F940-009 / F940-010 / F940-011", "UI State of coverage per employee; credit-reduction table",
              "Mark every State where State unemployment tax was paid; for each State with a credit-reduction rate above zero, "
              "multiply the FUTA taxable wages paid in that State by the rate and carry the total to Form 940 line 11.",
              "The 2026 rates are applied only once the final list is published; a 2025 return uses the 2025 final list.")]),
         ("FORM 940 LINES", lpr)],
        ex, NO_SAMPLE.format(ch=AGENT))


# ============================================================== Schedule H ===
def irs_schedule_h():
    P = "SCHH"
    at("IRS-005 metadata")
    rows = [section("ROUTING FLAG (no return produced by the payroll)")]
    at(f"{P}-001")
    rows.append(row("payroll", "Household employee flag", "Household employee", "Routing", f"{P}-001", "Y", "Y",
                    "Not conditional: every employee carries the flag (Y or N).", "Logical field (field model)", "1", "Flag", "Y",
                    f"{DD_REF}: employee category = household (forward reference)",
                    "Marks wages paid by a household employer. Those wages are reported by the household employer on Schedule H "
                    "with the personal return [US-FEDS5-029]; the payroll does not file that return and excludes the wages from "
                    "Forms 941 and 940 (US-IRS-001, US-IRS-004).",
                    "Yes: routing of the wages", "Y / N", "Not applicable", "N", "Flag", "Annual"))
    at(f"{P}-002")
    rows.append(row("payroll", "Household cash wages for the FICA test", "Cash wages", "Routing", f"{P}-002", "Y", "C",
                    "Only when SCHH-001 = Y.", "Logical field (field model)", "Amount", "Decimal 13.2", "3,200.00",
                    "Payroll result: household cash wages per employee per year",
                    f"Cash wages paid to the household employee in the year, compared with {tagr('fed.household.fica_cash_threshold')}; "
                    f"at or above it the wages are FICA wages. {src('fed.household.fica_cash_threshold')}",
                    "Yes: FICA coverage test", "Not applicable", "Cents (2 decimals)", "N", "Amount", "Annual"))
    at(f"{P}-003")
    rows.append(row("payroll", "Household cash wages per quarter for the FUTA test", "Quarterly cash wages", "Routing", f"{P}-003",
                    "Y", "C", "Only when SCHH-001 = Y.", "Logical field (field model)", "Amount per quarter", "Decimal 13.2",
                    "1,100.00", "Payroll result: household cash wages per quarter (all household employees)",
                    f"Total household cash wages in a calendar quarter compared with {tagr('fed.household.futa_quarter_threshold')} "
                    f"for FUTA. {src('fed.household.futa_quarter_threshold')}",
                    "Yes: FUTA coverage test", "Q1 to Q4", "Cents (2 decimals)", "N", "Amount", "Quarterly"))
    at(f"{P}-004")
    rows.append(row("payroll", "Federal income tax withholding by agreement", "Voluntary withholding", "Routing", f"{P}-004",
                    "Y", "C", "Only when SCHH-001 = Y and the employee asked for withholding.", "Logical field (field model)",
                    "1", "Flag", "N", f"{DD_REF}: household withholding agreement flag (forward reference)",
                    f"Switch for federal income tax withholding on household wages: it is withheld "
                    f"{tagr('fed.household.fit.withholding')} between the household employer and the employee. Held as a "
                    f"Y / N flag in the Data Dictionary; when Y the payroll withholds FIT per {CCG_REF} Module 6 and the "
                    f"amount enters the annual statement below, when N no FIT is withheld. Social security, Medicare and "
                    f"FUTA coverage follow their own cash-wage tests (rows above), not this flag.",
                    "Yes: withholding switch", "Y / N", "Not applicable", "N", "Flag", "Per payment"))
    rows.append(section("ANNUAL STATEMENT HANDED TO THE HOUSEHOLD EMPLOYER (Schedule H amounts)"))
    SK = "rspec.fed.schedule_h.employer_statement"
    at(f"{P}-005")
    rows.append(row("constant", "Schedule H statement (source)", "Annual amounts for Schedule H", "Statement", f"{P}-005", "N", "Y",
                    "Not conditional: produced for every household employer with household employees (SCHH-001 = Y).",
                    "Not applicable", "Not applicable", "Text", "See the item rows below",
                    "Statement generator (system constant)",
                    f"{tagr(SK)}. Each item below is one line of this statement. {src(SK)}",
                    "Yes: completeness of the hand-off", "Not applicable", "Not applicable", "N", "Display-only (Text)", "Annual"))
    head, _, body = str(fact(SK)["value"]).partition(": ")
    rk = ("rspec.fed.household.fica_cash_wage_threshold", "fed.fica.oasdi.wage_base",
          "fed.fica.addl_medicare.withholding_threshold", "fed.futa.wage_base", "rspec.fed.household.futa_quarter_threshold")
    n = 6
    for it in split_top(body, "; "):
        at(f"{P}-{n:03d}")
        note_use(SK)
        nm = re.sub(r"^plus the ", "", it.split(" (")[0].strip())
        nm = nm[0].upper() + nm[1:]
        calc = "tax amounts" in it
        rows.append(row("payroll", f"Statement: {nm}", nm, "Statement", f"{P}-{n:03d}", "Y", "C",
                        "Only when SCHH-001 = Y and the amount arises for the employee in the year; back-reference to SCHH-002 "
                        "and SCHH-003 for the coverage tests.", "Not applicable", "Amount", "Decimal 13.2",
                        "See Example Analysis",
                        "Calculated from the household payroll results" if calc else
                        "Payroll result: household annual accumulator per employee",
                        f"Statement item for the household employer's Schedule H: {retag(it, rk)}. The payroll hands the "
                        f"amount over once a year; the household employer files it with the personal return. {src(SK)}",
                        "Yes: hand-off to the household employer", "Not applicable", "Cents (2 decimals)", "N",
                        "Calculated" if calc else "Amount", "Annual"))
        n += 1
    at(f"{P}-{n:03d}")
    rows.append(row("system", "Schedule H due date", "Due date", "Statement", f"{P}-{n:03d}", "N", "Y", "Not conditional.",
                    "Not applicable", "Date", "YYYY-MM-DD", "2027-04-15", "Filing calendar of the payroll (system constant)",
                    f"{tagr('rspec.fed.schedule_h.due')}. The statement is handed over early enough for the household employer to "
                    f"file by that date; Forms W-2 for household employees follow US-SSA-001. {src('rspec.fed.schedule_h.due')}",
                    "Yes: hand-off calendar", "Not applicable", "Not applicable", "N", "Date", "Annual"))
    n += 1
    at(f"{P}-{n:03d}")
    rows.append(row("system", "Household coverage thresholds (Schedule H)", "Thresholds", "Statement", f"{P}-{n:03d}", "N", "Y",
                    "Not conditional.", "Not applicable", "Amount", "Decimal", "See column M",
                    "System constant per year",
                    f"FICA cash-wage test {tagr('rspec.fed.household.fica_cash_wage_threshold')} per employee in the year; FUTA "
                    f"test {tagr('rspec.fed.household.futa_quarter_threshold')} of cash wages in any calendar quarter. Same "
                    f"figures as SCHH-002 and SCHH-003. {src('rspec.fed.household.fica_cash_wage_threshold')}",
                    "Yes: coverage tests", "Not applicable", "Whole dollars as published", "N", "Amount", "Annual"))
    matrix = [["US-IRS-005", "Schedule H routing (household employees)", "Schedule H (household employer's individual return)", "Internal Revenue Service (IRS)",
               "Annual", f"With the household employer's personal return: {tag('rspec.fed.schedule_h.due')}",
               "Not transmitted by the payroll: routing flag only",
               "Routing flag only: household-employee wages are reported by the household employer on Schedule H. "
               "Not a file produced by the payroll.",
               "[US-FEDS5-029]",
               accuracy("none (routing flag)", "Not applicable", url("rspec.fed.schedule_h.employer_statement"), "CONFIRMED",
                        "90% (routing rule, thresholds, statement content and due date read)",
                        "one household employer's filed Schedule H checked against the statement")]]
    at("SCHH example")
    ex = [("WORKED EXAMPLE: COVERAGE TESTS (constructed)", [
        ("3,200.00", "Cash wages in the year (SCHH-002)", f"3,200.00 against {tag('fed.household.fica_cash_threshold')}",
         "At or above: FICA wages"),
        ("1,100.00", "Cash wages in Q2 (SCHH-003)", f"1,100.00 against {tag('fed.household.futa_quarter_threshold')}",
         "At or above: FUTA coverage"),
    ])]
    return fed_book(
        "US-IRS-005", "ScheduleHRouting", "Schedule H Spec", "US-IRS-005 Schedule H Routing (Household Employees)",
        "Household employment taxes (reported by the household employer)",
        "Excluded from Form 941 (US-IRS-001) and Form 940 (US-IRS-004)", "Annual",
        f"With the household employer's personal return: {tag('rspec.fed.schedule_h.due')}",
        "Routing flag only: household-employee wages are reported by the household employer on Schedule H. "
        "Not a file produced by the payroll.",
        "Routing flag; coverage tests; annual statement to the household employer",
        f"[US-FEDS5-029] [{rid('rspec.fed.schedule_h.employer_statement')}]",
        "Schedule H (2026) line references and IRS household employer guidance as read for this release",
        "US-IRS-001 Form 941", matrix,
        "Flag household employees so that their wages are routed to the household employer's Schedule H.",
        [("WHO GETS REPORTED", [("Household (domestic) employees", "YES", "Flag only [US-OWN-005, US-FEDS5-029]."),
                                ("Filing of the household employer's own return", "NO", "Out of scope: filed with the personal return.")]),
         ("TIMING & RELATIONSHIP", [("Annual coverage tests", "YES", "Rows SCHH-002, SCHH-003.")]),
         ("AMOUNTS & CALCULATIONS", [("FICA cash-wage test", "YES", tag("fed.household.fica_cash_threshold")),
                                     ("FUTA quarter test", "YES", tag("fed.household.futa_quarter_threshold"))]),
         ("SPECIAL CASES", [("State household returns (e.g. CT-W3 HHE, NJ-927-H, OR Form OA)", "NO",
                             "State-level special-population rules are deferred to a later round [US-OWN-005].")])],
        rows,
        [("FILE FORMAT", ["No file is produced by the payroll for this filing.",
                          "Hand-off: one annual statement per household employer with the Schedule H amounts of each household "
                          "employee (rows SCHH-005 onwards)."]),
         ("STATEMENT CONTENT", [f"{tag('rspec.fed.schedule_h.employer_statement')} [{rid('rspec.fed.schedule_h.employer_statement')}]"])],
        [("HOUSEHOLD FLAG (SCHH-001)", [
            ("Household employee", "Y", "Household employee", "Domestic service in a private home", "[US-FEDS5-029]"),
            ("Household employee", "N", "Other employee", "Not household", "[US-FEDS5-029]")])],
        [("PAYROLL-SPECIFIC POPULATION RULES", [
            ("Conditional", "SCHH-002, SCHH-003, SCHH-004", "Household flag; payroll results",
             "When SCHH-001 = Y, accumulate cash wages per employee per year and per quarter for all household employees, apply "
             "the FICA and FUTA tests, and withhold federal income tax only if the employee and employer agreed to it.",
             "Non-cash household pay is outside the cash tests."),
            ("Conditional", "SCHH-006 onwards (statement items)", "Household payroll results",
             "For each household employer, total each statement item per household employee for the calendar year and hand the "
             "statement over before the Schedule H due date; items whose coverage test is not met stay at zero.",
             "A household employee crossing the FICA cash-wage test late in the year brings all cash wages of the year into "
             "the FICA items.")])],
        ex, "No file is produced for this filing; the payroll sets a routing flag. No sample exists.")
