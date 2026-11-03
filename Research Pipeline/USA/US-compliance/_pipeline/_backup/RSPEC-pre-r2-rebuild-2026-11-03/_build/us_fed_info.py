# -*- coding: utf-8 -*-
"""Federal Report Specifications: Forms W-2/W-3 (EFW2), 1042-S, 1094-C/1095-C, 941-X."""
import re
from decimal import Decimal

from us_common import (DD_REF, CCG_REF, tag, tagr, rid, url, src, fact, num, pct, m2, money, gap, at, per_draft,
                       is_draft, note_use, quote)
from us_rows import row, section, NONE_OPEN
from us_lines import line_rows, line_source_row, fs_line_table, parse_codes
from us_federal import (FIELD_MODEL, RQ_941, RQ_EFW2, RQ_W2BOX, RQ_1042S, RQ_ACA, RQ_941X, accuracy, ein_row,
                        name_row, common_remarks)
from us_fed_annual import fed_book, gap_field, NO_SAMPLE, AGENT

SSA = "Social Security Administration (SSA), with the IRS"


# =================================================================== 1042-S ===
def irs_1042s():
    P = "F1042S"
    at("IRS-006 metadata")
    rows = [section("WITHHOLDING AGENT AND RECIPIENT"), ein_row(1, P, "Form 1042-S"), name_row(2, P, "Form 1042-S")]
    at(f"{P}-003")
    rows.append(row("payroll", "Recipient nonresident alien flag and treaty claim", "Recipient status", "Recipient", f"{P}-003",
                    "Y", "Y", "Not conditional: only flagged recipients enter the return.", "Logical field (field model)",
                    "1", "Flag", "Y", f"{DD_REF}: nonresident alien flag, Form 8233 treaty claim (forward reference)",
                    f"{tagr('dd.fed.nra.flag')}. Only treaty-exempt wages claimed on Form 8233 are reported here: "
                    f"{tag('fed.fit.nra.treaty_exempt.reporting')}. {src('fed.fit.nra.treaty_exempt.reporting')}",
                    "Yes: selects the population", "Y / N", "Not applicable", "N", "Flag", "Annual"))
    at(f"{P}-004")
    rows.append(row("payroll", "Recipient visa class", "Immigration status", "Recipient", f"{P}-004", "Y", "Y", "Not conditional.",
                    "Logical field (field model)", "Text", "Code", "J-1", f"{DD_REF}: visa class (forward reference)",
                    f"{tagr('dd.fed.nra.visa_class')}.", "Yes: recipient classification", "See Field Options",
                    "Not applicable", "N", "Code", "Annual"))
    at(f"{P}-005")
    rows.append(row("payroll", "Treaty-exempt wages paid in the year", "Gross income", "Amounts", f"{P}-005", "Y", "Y",
                    "Not conditional.", "Logical field (field model)", "Amount", "Decimal 13.2", "24,000.00",
                    "Payroll result: treaty-exempt wage accumulator",
                    f"Wages exempt under a treaty claim; excluded from the W-2 wage box (US-SSA-001) "
                    f"[{rid('fed.fit.nra.treaty_exempt.reporting')}]. FICA treatment follows the visa class (US-IRS-001 row F941-015).",
                    "Yes: annual amount", "Not applicable", "Cents (2 decimals)", "N", "Amount", "Annual"))
    rows.append(section("FORM 1042-S BOX CODES FOR TREATY-EXEMPT WAGES"))
    WC = "rspec.fed.form1042s.wage_codes"
    qwc = (f"Confirm against a real filing: the pairing of the chapter 4 code and the status codes for wages is applied "
           f"from the instruction text [{rid(WC)}].")
    at(f"{P}-006")
    rows.append(row("constant", "Box codes for treaty-exempt wages (source)", "Box codes", "Box codes", f"{P}-006", "N", "Y",
                    "Not conditional.", "Not applicable", "Not applicable", "Text", "See rows F1042S-007 to F1042S-011",
                    "Return generator code table (system constant)",
                    f"Box codes for treaty-exempt wages, as read: {quote(WC)}. Rows F1042S-007 to F1042S-011 give each "
                    f"box. {src(WC)}",
                    "Yes: completeness of the return", "See Field Options", "Not applicable", "N", "Display-only (Text)",
                    "Annual", qwc))
    for n, (nm, box, key, txt, kind, mand, cond) in enumerate([
        ("Income code", "Box 1", "rspec.fed.form1042s.income_code.dependent_personal_services",
         "Income code for compensation for dependent personal services of a nonresident alien employee. Teaching, "
         "studying or training and artist or athlete income use the other codes listed in row F1042S-006.",
         "system", "Y", "Not conditional."),
        ("Chapter 3 exemption code and rate", "Boxes 3, 3a, 3b", "rspec.fed.form1042s.ch3_exemption_code.treaty",
         "Chapter 3 exemption code for income exempt or reduced under a tax treaty, with the chapter indicator and the "
         "withholding rate as stated in row F1042S-006.", "system", "Y", "Not conditional."),
        ("Chapter 4 exemption code and rate", "Boxes 4a, 4b", "rspec.fed.form1042s.ch4_exemption_code.excluded_nonfinancial",
         "Chapter 4 exemption code for an excluded nonfinancial payment, with the rate as stated in row F1042S-006.",
         "system", "Y", "Not conditional."),
        ("Recipient country and status codes", "Boxes 13b, 13j, 13k", WC,
         "Recipient country code (a treaty country when the chapter 3 exemption code is the treaty code) and the chapter 3 / "
         "chapter 4 status codes of an individual, as stated in row F1042S-006. The treaty article is documented on Form 8233, "
         "not on Form 1042-S.", "payroll", "Y", "Not conditional."),
        ("Withholding allowance and net income", "Boxes 5, 6", WC,
         "Used only where the treaty exempts income up to a specific amount: the allowance goes in box 5 and the net income in "
         "box 6, as stated in row F1042S-006.", "payroll", "C",
         "Only when the treaty exempts up to a specific amount; back-reference to F1042S-005."),
    ], start=7):
        at(f"{P}-{n:03d}")
        if key == WC:
            note_use(WC)
            val = "See row F1042S-006"
        else:
            val = tag(key)
        rows.append(row(kind, f"{box}: {nm}", nm, "Box codes", f"{P}-{n:03d}", "N" if kind == "system" else "Y", mand, cond,
                        box, "Code", "Code", val if key != WC else "As held",
                        "Return generator code table (system constant)" if kind == "system" else
                        f"{DD_REF}: recipient country and treaty claim (forward reference)",
                        f"{box}: {txt} Code: {val}. {src(key)}", "Yes: box of the return",
                        "See Field Options" if key != WC else "Not applicable", "Not applicable", "N",
                        "Input (Code)", "Annual", qwc if key == WC else NONE_OPEN))
    matrix = [["US-IRS-006", "Form 1042-S, Foreign Person's U.S. Source Income Subject to Withholding (treaty-exempt wages)",
               "Form 1042-S", "Internal Revenue Service (IRS)", "Annual", tag("fed.form1042s.channel"),
               "file_upload: electronic filing through IRIS by the reporting agent",
               f"Electronic filing through IRIS ({tag('fed.form1042s.channel')}). {FIELD_MODEL}.",
               f"[{rid('fed.form1042s.channel')}]; {url('fed.form1042s.channel')}",
               accuracy("file_upload", "IRS IRIS", url("fed.form1042s.channel"), "CONFIRMED (channel and box codes), TO CONFIRM (code pairing for wages)",
                        "80% (rule, channel and box codes read; pairing for wages applied from the instruction text)",
                        "one accepted real filing for a treaty-exempt employee")]]
    at("1042S example")
    ex = [("WORKED EXAMPLE: ROUTING OF A TREATY CLAIM (constructed)", [
        ("24,000.00", "Wages of a J-1 researcher with a Form 8233 treaty claim", "Constructed input", "Input"),
        ("24,000.00", "Form 1042-S amount (F1042S-005)", "Treaty-exempt wages", tag("fed.fit.nra.treaty_exempt.reporting")),
        ("0.00", "W-2 federal wages for the same pay", "Excluded from the W-2 wage box", "No double reporting"),
    ])]
    return fed_book(
        "US-IRS-006", "Form1042S", "Form 1042-S Spec", "US-IRS-006 Form 1042-S Treaty-Exempt Wages of Nonresident Aliens",
        "Federal income tax treaty exemption reporting", "Excluded wages do not enter the W-2 wage box (US-SSA-001)",
        "Annual", tag("fed.form1042s.channel"), f"Electronic filing through IRIS. {FIELD_MODEL}.",
        "Withholding agent; Recipient; Amounts; Box codes",
        f"{url('fed.form1042s.channel')} [{rid('fed.form1042s.channel')}]", "Publication 515 as read for this release",
        "US-SSA-001 Forms W-2/W-3", matrix,
        "Nonresident alien employees whose wages are exempt under a tax treaty claimed on Form 8233.",
        [("WHO GETS REPORTED", [("Nonresident aliens with an accepted Form 8233 treaty claim", "YES", tag("fed.fit.nra.treaty_exempt.reporting")),
                                ("Nonresident aliens without a treaty claim", "NO", "Their wages go on Form W-2 (US-SSA-001).")]),
         ("TIMING & RELATIONSHIP", [("Annual filing through IRIS", "YES", tag("fed.form1042s.channel"))]),
         ("AMOUNTS & CALCULATIONS", [("Treaty-exempt wages", "YES", "Row F1042S-005.")]),
         ("SPECIAL CASES", [("Recipient becomes a resident alien during the year", "PARTIAL",
                             "Only pay while a nonresident alien with the treaty claim is reported here.")])],
        rows,
        [("FILE FORMAT", [f"Electronic filing through IRIS ({tag('fed.form1042s.channel')}).", f"{FIELD_MODEL}.",
                          "Box codes: rows F1042S-006 to F1042S-011.", "FORMAT TO CONFIRM vs a real filing."]),
         ("BOX CODES (wages)", [f"As read: {quote('rspec.fed.form1042s.wage_codes')}"])],
        [("VISA CLASS (F1042S-004)", [("Visa class", "Per Data Dictionary", tag("dd.fed.nra.visa_class"), "Visa class as issued",
                                       f"[{rid('dd.fed.nra.visa_class')}]")]),
         ("BOX CODES FOR TREATY-EXEMPT WAGES (F1042S-007 to F1042S-009)", [
             ("Box 1 income code", tag("rspec.fed.form1042s.income_code.dependent_personal_services"),
              "Compensation for dependent personal services", "Income code", f"[{rid('rspec.fed.form1042s.income_code.dependent_personal_services')}]"),
             ("Box 3a chapter 3 exemption code", tag("rspec.fed.form1042s.ch3_exemption_code.treaty"),
              "Exempt or reduced withholding under a tax treaty", "Exemption code", f"[{rid('rspec.fed.form1042s.ch3_exemption_code.treaty')}]"),
             ("Box 4a chapter 4 exemption code", tag("rspec.fed.form1042s.ch4_exemption_code.excluded_nonfinancial"),
              "Excluded nonfinancial payment", "Exemption code", f"[{rid('rspec.fed.form1042s.ch4_exemption_code.excluded_nonfinancial')}]")])],
        [("PAYROLL-SPECIFIC POPULATION RULES", [
            ("Conditional", "F1042S-005 treaty-exempt wages", "NRA flag; Form 8233 claim",
             "Accumulate only the wages covered by an accepted treaty claim while the employee is a nonresident alien; the same pay is "
             "excluded from the W-2 wage box and never reported twice.",
             "A claim that exceeds the treaty limit during the year stops at the limit; pay above it goes to Form W-2."),
            ("Conditional", "F1042S-011 withholding allowance", "Treaty claim (Form 8233)",
             "Fill the allowance and net income boxes only when the treaty exempts income up to a specific amount; for a full "
             "exemption the gross income box carries the treaty-exempt wages and the allowance box stays empty.",
             "A treaty limit reached during the year moves the excess to Form W-2 and leaves the allowance at the limit.")])],
        ex, NO_SAMPLE.format(ch="electronic filing through IRIS by the reporting agent"))


# ====================================================================== ACA ===
def aca_codes(key):
    """'1A qualifying offer (...); 1B ...' -> [(code, description)]."""
    import re as _re
    from us_lines import split_top
    out = []
    for it in split_top(str(fact(key)["value"]), "; "):
        m = _re.match(r"^(\d[A-Z](?:,\s*\d[A-Z])*)\s+(.*)$", it.strip())
        if m:
            out.append((m.group(1), m.group(2)))
    note_use(key)
    return out


def irs_aca():
    P = "ACA"
    at("IRS-007 metadata")
    rows = [section("ALE DETERMINATION AND EMPLOYER RETURN (1094-C)"), ein_row(1, P, "Form 1094-C"), name_row(2, P, "Form 1094-C")]
    at(f"{P}-003")
    rows.append(row("payroll", "Applicable large employer status", "ALE member", "1094-C", f"{P}-003", "Y", "Y", "Not conditional.",
                    "Logical field (field model)", "1", "Flag", "Y", "Calculated from the monthly full-time and FTE counts",
                    f"An employer with {tagr('fed.aca.ale.fte_threshold')} or more full-time employees including full-time "
                    f"equivalents in the prior year files Forms 1094-C and 1095-C. The final 2026 instructions are not yet issued; "
                    f"the line codes and dates below are per 2026 draft {gap('rspec.fed.aca.ty2026_due_dates')}. "
                    f"{src('fed.aca.ale.fte_threshold')}",
                    "Yes: decides whether the return exists", "Y / N", "Not applicable", "N", "Flag", "Annual"))
    at(f"{P}-004")
    rows.append(row("payroll", "Monthly full-time and FTE status per employee", "Full-time status", "1095-C", f"{P}-004", "Y", "Y",
                    "Not conditional.", "Logical field (field model)", "12 monthly values", "Code per month", "FT, FT, FT, ...",
                    f"{DD_REF}: monthly full-time / FTE status (forward reference)",
                    f"{tagr('dd.fed.aca.fte_tracking')}. Feeds both the ALE test and the monthly lines of Form 1095-C.",
                    "Yes: monthly tracking", "See Field Options", "Not applicable", "N", "Code", "Monthly (tracked), annual (filed)"))
    at(f"{P}-005")
    rows.append(row("system", "Affordability percentage", "Affordability", "1095-C", f"{P}-005", "N", "Y", "Not conditional.",
                    "Logical field (field model)", "Rate", "Percent", f"{tag('fed.aca.affordability.rate')}%",
                    "System constant (yearly)",
                    f"Affordability percentage for 2026: {tagr('fed.aca.affordability.rate')}%; the same figure is applied to the "
                    f"percentage references of the affordability safe harbors and the Qualifying Offer Method for plan years beginning in 2026 "
                    f"({tagr('rspec.fed.aca.affordability_pct')}%).{per_draft('rspec.fed.aca.affordability_pct')} Used to test the "
                    f"employee's required contribution for the lowest-cost self-only coverage. {src('fed.aca.affordability.rate')}",
                    "Yes: offer of coverage codes", "Not applicable", "Two decimals as published", "N", "Rate", "Annual"))
    at(f"{P}-006")
    rows.append(row("system", "Electronic filing threshold", "E-file threshold", "1094-C", f"{P}-006", "N", "C",
                    "Applies when the employer files the threshold number of information returns or more.",
                    "Not applicable", "Not applicable", "Count", "Electronic", "Provider hand-off configuration",
                    f"Electronic filing is mandatory at {tagr('fed.aca.efile_threshold')} or more information returns in aggregate "
                    f"(tax year 2025 rule).", "Yes: channel", "Not applicable", "Not applicable", "N", "Count", "Annual"))
    rows.append(section("FORM 1095-C MONTHLY LINES (per employee, per 2026 draft)"))
    q_aca = f"Confirm against the final 2026 revision [{rid('rspec.fed.aca.form1095c.line14_codes')}]."
    for n, (nm, key, kind, mand, cond, fmt, opts, mapping) in enumerate([
        ("Line 14: offer of coverage code (per month)", "rspec.fed.aca.form1095c.line14_codes", "payroll", "Y",
         "Not conditional: one code for each month (or the All 12 Months box).", "Code (2)", "Line 14 codes (Field Options)",
         f"{DD_REF}: monthly offer of coverage per employee (forward reference)"),
        ("Line 15: employee required contribution (per month)", "rspec.fed.aca.form1095c.line15_rule", "payroll", "C",
         "Only with the line 14 codes named in column M; back-reference to ACA-007.", "Decimal 7.2", "Not applicable",
         "Payroll result: employee share of the lowest-cost self-only coverage per month"),
        ("Line 16: section 4980H safe harbor and other relief code (per month)", "rspec.fed.aca.form1095c.line16_codes",
         "payroll", "C", "Only when a safe harbor or relief applies to the month; back-reference to ACA-007.", "Code (2)",
         "Line 16 codes (Field Options)", f"{DD_REF}: monthly status and safe harbor per employee (forward reference)"),
        ("Line 17: ZIP code (per month)", "rspec.fed.aca.form1095c.line17_rule", "payroll", "C",
         "Only with the ICHRA line 14 codes named in column M; back-reference to ACA-007.", "N (5)", "Not applicable",
         f"{DD_REF}: employee residence or work-site ZIP code"),
        ("Filing and furnishing dates (tax year 2026)", "rspec.fed.aca.ty2026_due", "system", "Y", "Not conditional.",
         "Date", "Not applicable", "Filing calendar of the payroll (system constant)"),
    ], start=7):
        at(f"{P}-{n:03d}")
        rows.append(row(kind, nm, nm.split(":")[0], "1095-C" if n < 11 else "1094-C / 1095-C", f"{P}-{n:03d}",
                        "Y" if kind == "payroll" else "N", mand, cond, "Form line (per month)" if n < 11 else "Not applicable",
                        "12 monthly values" if n < 11 else "Date", fmt, "1E" if n == 7 else "See column M", mapping,
                        f"{tagr(key)}.{per_draft(key)} {src(key)}", "Yes: employee statement and IRS return", opts,
                        "Cents (2 decimals)" if n == 8 else "Not applicable", "N",
                        "Input (Code)" if n in (7, 9) else "Input (Amount)" if n == 8 else "Input (Text)" if n == 10 else "Input (Date)",
                        "Monthly (tracked), annual (filed)" if n < 11 else "Annual", q_aca))
    rows.append(section("FORM 1094-C TRANSMITTAL LINES (per 2026 draft)"))
    rows.append(line_source_row(P, "rspec.fed.aca.form1094c.line_map", "Form 1094-C", "Annual"))
    lrows, lpr, _ = line_rows(P, "rspec.fed.aca.form1094c.line_map", "Form 1094-C", "Annual",
                              fm={"1": f"{P}-002", "2": f"{P}-001"}, mandatory={"1", "2", "18", "20"})
    rows += lrows
    matrix = [["US-IRS-007", "Forms 1094-C / 1095-C (Affordable Care Act employer reporting)", "Forms 1094-C, 1095-C",
               "Internal Revenue Service (IRS)", "Annual", f"{tag('rspec.fed.aca.ty2026_due')} (per 2026 draft)",
               "file_upload: electronic filing by the reporting agent",
               f"Electronic filing (threshold per Instructions: {tag('fed.aca.efile_threshold')} returns). {FIELD_MODEL}.",
               f"[{rid('fed.aca.ale.fte_threshold')}] (2025 instructions) [{rid('fed.aca.affordability.rate')}] "
               f"[{rid('rspec.fed.aca.form1095c.line14_codes')}] (2026 draft); {url('fed.aca.ale.fte_threshold')}",
               accuracy("file_upload", "IRS electronic filing through the reporting agent", url("fed.aca.ale.fte_threshold"), "TO CONFIRM",
                        "75% (line codes, 1094-C lines and dates per 2026 draft; final 2026 instructions not issued)",
                        f"the final 2026 Instructions for Forms 1094-C and 1095-C {gap('rspec.fed.aca.ty2026_due_dates')}")]]
    at("ACA example")
    r = pct("fed.aca.affordability.rate")
    inc = Decimal("36000.00")
    ex = [("WORKED EXAMPLE: AFFORDABILITY LIMIT (constructed)", [
        ("36,000.00", "Annual amount used for the affordability test", "Constructed input", "Input"),
        (m2(money(inc * r)), "Annual affordability limit", f"36,000.00 x {tag('fed.aca.affordability.rate')}%", "Half-up to the cent"),
        (m2(money(inc * r / 12)), "Monthly affordability limit", f"{m2(money(inc * r))} / 12", "Half-up to the cent"),
    ])]
    return fed_book(
        "US-IRS-007", "Forms1094C1095C", "ACA 1094-C 1095-C Spec", "US-IRS-007 Forms 1094-C and 1095-C (ACA Employer Reporting)",
        "Employer shared responsibility information return", "Uses the monthly employee status held in the Data Dictionary",
        "Annual", f"{tag('rspec.fed.aca.ty2026_due')} (per 2026 draft)",
        f"Electronic filing (threshold per Instructions). {FIELD_MODEL}.", "1094-C transmittal; 1095-C per employee (lines 14 to 17)",
        f"{url('fed.aca.ale.fte_threshold')} [{rid('fed.aca.ale.fte_threshold')}] [{rid('rspec.fed.aca.form1094c.line_map')}]",
        "Forms 1094-C / 1095-C and instructions for 2026 (IRS early-release draft); 2025 instructions", "US-SSA-001 Forms W-2/W-3", matrix,
        "Applicable large employers report the offer of health coverage to each full-time employee.",
        [("WHO GETS REPORTED", [("Full-time employees of an ALE member", "YES", tag("fed.aca.ale.fte_threshold")),
                                ("Employers below the ALE threshold", "NO", "No 1094-C / 1095-C filing.")]),
         ("TIMING & RELATIONSHIP", [("Annual filing", "YES", f"{tag('rspec.fed.aca.ty2026_due')} (per 2026 draft)")]),
         ("AMOUNTS & CALCULATIONS", [("Affordability percentage 2026", "YES", f"{tag('fed.aca.affordability.rate')}%")]),
         ("SPECIAL CASES", [("Employees changing status during the year", "PARTIAL", "Monthly status per row ACA-004.")])],
        rows,
        [("FILE FORMAT", [f"Electronic filing at {tag('fed.aca.efile_threshold')} or more returns.", f"{FIELD_MODEL}.",
                          "Form 1095-C lines 14 to 17 per employee and month (rows ACA-007 to ACA-010); Form 1094-C lines in "
                          "the transmittal rows.", "FORMAT TO CONFIRM vs a real filing."]),
         ("FORM 1094-C LINE MAP (2026 draft)", fs_line_table("rspec.fed.aca.form1094c.line_map", "Form 1094-C"))],
        [("MONTHLY STATUS (ACA-004)", [("Monthly status", "Per Data Dictionary", tag("dd.fed.aca.fte_tracking"), "Monthly status",
                                        f"[{rid('dd.fed.aca.fte_tracking')}]")]),
         ("FORM 1095-C LINE 14 OFFER OF COVERAGE CODES (ACA-007, per 2026 draft)",
          [f"Source list: {tag('rspec.fed.aca.form1095c.line14_codes')}"] +
          [("Line 14", c, d, d, f"[{rid('rspec.fed.aca.form1095c.line14_codes')}]") for c, d in aca_codes("rspec.fed.aca.form1095c.line14_codes")]),
         ("FORM 1095-C LINE 16 SAFE HARBOR AND RELIEF CODES (ACA-009, per 2026 draft)",
          [f"Source list: {tag('rspec.fed.aca.form1095c.line16_codes')}"] +
          [("Line 16", c, d, d, f"[{rid('rspec.fed.aca.form1095c.line16_codes')}]") for c, d in aca_codes("rspec.fed.aca.form1095c.line16_codes")])],
        [("PAYROLL-SPECIFIC POPULATION RULES", [
            ("Conditional", "ACA-006 electronic filing", "Count of information returns",
             "Count all information returns the employer files for the year; at or above the threshold the provider files "
             "electronically, below it paper remains possible but the provider route is electronic in this build.",
             "The 2026 threshold is read from the 2025 instructions until the 2026 edition is issued."),
            ("Conditional", "ACA-008 line 15", "Payroll result per month",
             "Report the employee required contribution for the lowest-cost self-only minimum value coverage only in the months "
             "whose line 14 code is one of the codes named in row ACA-008; leave it blank with the Qualifying Offer code.",
             "A mid-month change of contribution uses the amount the line 15 rule assigns to the month."),
            ("Conditional", "ACA-009 line 16", "Monthly status and safe harbor",
             "Enter a line 16 code for a month only when the employee was not employed, not full-time, enrolled, in a limited "
             "non-assessment period, or covered by an affordability safe harbor or relief listed in Field Options.",
             "Only one line 16 code per month."),
            ("Conditional", "ACA-010 line 17", "Employee residence or work-site ZIP",
             "Enter the ZIP code only for the months with an individual coverage HRA code on line 14, using the residence ZIP or "
             "the work-site ZIP as the code itself states.", "A move during the year changes the ZIP from the month of the move.")]),
         ("FORM 1094-C LINES", lpr)],
        ex, NO_SAMPLE.format(ch="electronic filing by the reporting agent"))


# ==================================================================== 941-X ===
def irs_941x():
    P = "F941X"
    at("IRS-008 metadata")
    rows = [section("HEADER"), ein_row(1, P, "Form 941-X"), name_row(2, P, "Form 941-X")]
    at(f"{P}-003")
    rows.append(row("system", "Quarter and year corrected", "Quarter corrected", "Header", f"{P}-003", "N", "Y", "Not conditional.",
                    "Logical field (field model)", "6", "YYYYQn", "2026Q1", "Correction register (quarter of the original Form 941)",
                    "The quarter of the Form 941 being corrected; one Form 941-X per quarter corrected [US-FEDS5-031].",
                    "Yes: identifies the return corrected", "Q1 to Q4", "Not applicable", "N", "Code", "Event-driven"))
    rows.append(section("CORRECTED AMOUNTS (per line of US-IRS-001)"))
    for i, nm in enumerate(["Wages, tips and other compensation", "Federal income tax withheld", "Taxable social security wages",
                            "Taxable Medicare wages and tips", "Wages subject to Additional Medicare Tax withholding"], start=4):
        at(f"{P}-{i:03d}")
        rows.append(row("payroll", f"{nm}: originally reported / corrected / difference", nm, "Corrections", f"{P}-{i:03d}", "Y", "C",
                        "Only for the amounts that change; unchanged amounts are left blank.", "Logical field (field model)",
                        "3 amounts", "Decimal 13.2", "See Example Analysis", "Correction register: original and corrected payroll results",
                        f"Three values per amount: as filed on Form 941, corrected, and the difference. Same definitions as US-IRS-001. "
                        f"Tax effect uses {tag('fed.fica.oasdi.rate.employee')}% + {tag('fed.fica.oasdi.rate.employer')}% and "
                        f"{tag('fed.fica.medicare.rate.employee')}% + {tag('fed.fica.medicare.rate.employer')}% [US-FEDS5-005].",
                        "Yes: correction", "Not applicable", "Cents (2 decimals)", "Y", "Amount", "Event-driven"))
    rows.append(section("PROCESS CHOICE AND TIME LIMITS"))
    at(f"{P}-009")
    rows.append(row("system", "Adjustment or claim process", "Process (line 1 or line 2)", "Process", f"{P}-009", "N", "Y",
                    "Not conditional: every Form 941-X selects one process.", "Form lines 1 and 2", "1", "Flag", "Adjustment",
                    "Correction register: direction of the correction (under- or over-reported) and date found",
                    f"{tagr('rspec.fed.form941x.process_rule')}. {src('rspec.fed.form941x.process_rule')}",
                    "Yes: selects the correction route", "Adjustment process (line 1) / claim process (line 2)",
                    "Not applicable", "N", "Input (Code)", "Event-driven"))
    at(f"{P}-010")
    rows.append(row("system", "Filing deadline and period of limitations", "Deadlines", "Process", f"{P}-010", "N", "Y",
                    "Not conditional.", "Not applicable", "Date rule", "Rule", "Error found 2026-05-12: file by 2026-07-31",
                    "Filing calendar of the payroll (system constant)",
                    f"{tagr('rspec.fed.form941x.deadlines')}. {src('rspec.fed.form941x.deadlines')}",
                    "Yes: correction calendar", "Not applicable", "Not applicable", "N", "Input (Date rule)", "Event-driven"))
    rows.append(section("FORM 941-X LINES (Rev. 4-2026), MAPPED TO THE FIELD MODEL"))
    rows.append(line_source_row(P, "rspec.fed.form941x.line_map", "Form 941-X", "Event-driven"))
    lrows, lpr, _ = line_rows(P, "rspec.fed.form941x.line_map", "Form 941-X", "Event-driven",
                              fm={"6": f"{P}-004", "7": f"{P}-005", "8": f"{P}-006", "12": f"{P}-007", "13": f"{P}-008",
                                  "1": f"{P}-009", "2": f"{P}-009"},
                              mandatory={"3", "23", "27", "43"})
    rows += lrows
    matrix = [["US-IRS-008", "Form 941-X, Adjusted Employer's Quarterly Federal Tax Return or Claim for Refund", "Form 941-X",
               "Internal Revenue Service (IRS)", "Event-driven (after an error is found)", tag("rspec.fed.form941x.deadlines"),
               "file_upload: electronic return transmitted by the reporting agent",
               f"Electronic return (e-file through the reporting agent). {FIELD_MODEL}.", f"[US-FEDS5-031] [{rid('rspec.fed.form941x.line_map')}]",
               accuracy("file_upload", "IRS e-file through the authorised reporting agent (Form 8655)", url("rspec.fed.form941x.line_map"),
                        "TO CONFIRM", "85% (Form 941-X Rev. 4-2026 lines, process rule and time limits read; no real filing)",
                        "the provider import layout and one accepted real filing")]]
    at("941X example")
    d = Decimal("2000.00")
    rate = pct("fed.fica.oasdi.rate.employee") + pct("fed.fica.oasdi.rate.employer")
    ex = [("WORKED EXAMPLE: UNDER-REPORTED SOCIAL SECURITY WAGES (constructed)", [
        ("10,000.00", "Social security wages as filed", "Original Form 941", "Input"),
        ("12,000.00", "Social security wages corrected", "Payroll correction", "Input"),
        (m2(d), "Difference (F941X-006)", "12,000.00 - 10,000.00", "Calculation"),
        (m2(money(d * rate)), "Social security tax difference",
         f"{m2(d)} x ({tag('fed.fica.oasdi.rate.employee')}% + {tag('fed.fica.oasdi.rate.employer')}%)", "Half-up to the cent"),
    ])]
    return fed_book(
        "US-IRS-008", "Form941X", "Form 941-X Spec", "US-IRS-008 Form 941-X Adjusted Employer's Quarterly Federal Tax Return",
        "Federal income tax withheld, social security and Medicare (FICA): corrections", "Corrects Form 941 (US-IRS-001)",
        "Event-driven", tag("rspec.fed.form941x.deadlines"), f"Electronic return (e-file through the reporting agent). {FIELD_MODEL}.",
        "Header; Corrected amounts; Process and time limits; Form 941-X lines (Rev. 4-2026)",
        f"[US-FEDS5-031] [{rid('rspec.fed.form941x.line_map')}]", "Form 941-X Rev. 4-2026 and IRS Publication 15 (2026)",
        "US-IRS-001 Form 941", matrix, "Corrections of a filed Form 941 quarter.",
        [("WHO GETS REPORTED", [("Employees whose amounts change in a filed quarter", "YES", "Rows F941X-004 to F941X-008.")]),
         ("TIMING & RELATIONSHIP", [("Filed after the error is found", "YES", "Never corrected on a later Form 941."),
                                    ("One Form 941-X per quarter corrected", "YES", "Row F941X-009.")]),
         ("AMOUNTS & CALCULATIONS", [("Original, corrected and difference", "YES", "Three values per amount.")]),
         ("SPECIAL CASES", [("Matching Form W-2c", "YES", "Wage corrections of a closed year also need Form W-2c (US-SSA-001).")])],
        rows,
        [("FILE FORMAT", [f"{FIELD_MODEL}.", "The line rows of the core sheet map each form line to the field model.",
                          "FORMAT TO CONFIRM vs a real filing."]),
         ("FORM 941-X LINE MAP (Rev. 4-2026)", fs_line_table("rspec.fed.form941x.line_map", "Form 941-X"))],
        [("QUARTER (F941X-003)", [("Quarter", f"Q{i}", f"Calendar quarter {i}", f"Quarter {i}", "[US-FEDS5-031]") for i in range(1, 5)])],
        [("PAYROLL-SPECIFIC POPULATION RULES", [
            ("Conditional", "F941X-004 to F941X-008", "Correction register",
             "Populate only the amounts that changed, each with the value filed, the corrected value and the difference; the "
             "difference drives the tax effect at the published rates.",
             "A correction that also changes a closed year's W-2 is paired with a Form W-2c.")]),
         ("FORM 941-X LINES", lpr)],
        ex, NO_SAMPLE.format(ch=AGENT))
