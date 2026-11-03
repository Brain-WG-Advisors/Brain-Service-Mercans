# -*- coding: utf-8 -*-
"""Federal Report Specifications: Forms W-2/W-3 (EFW2), 1042-S, 1094-C/1095-C, 941-X."""
import re
from decimal import Decimal

from us_common import (DD_REF, CCG_REF, tag, tagr, rid, url, src, fact, num, pct, m2, money, gap, at)
from us_rows import row, section
from us_federal import (FIELD_MODEL, RQ_941, RQ_EFW2, RQ_W2BOX, RQ_1042S, RQ_ACA, RQ_941X, accuracy, ein_row,
                        name_row, common_remarks)
from us_fed_annual import fed_book, gap_field, NO_SAMPLE, AGENT

SSA = "Social Security Administration (SSA), with the IRS"


def positions(text, label):
    """'<label> a-b' or '<label> a' from a layout fact value -> (start, end)."""
    m = re.search(re.escape(label) + r"[^0-9;]*?(\d+)(?:-(\d+))?", text)
    if not m:
        raise KeyError(f"{label!r} not in layout")
    a = int(m.group(1))
    b = int(m.group(2) or m.group(1))
    return a, b


def pos_row(kind, P, n, rec, name, label, key, mand, cond, fmt, example, mapping, expl, opts, vtype, payroll="Y",
            neg="N", rounding="Not applicable"):
    at(f"{P}-{n:03d}")
    v = fact(key)["value"]
    a, b = positions(v, label)
    return row(kind, name, label, rec, f"{P}-{n:03d}", payroll, mand, cond, f"{a}-{b}" if a != b else f"{a}",
               str(b - a + 1), fmt, example, mapping, f"{expl} Layout: {tagr(key)}. {src(key)}",
               "Yes" if payroll == "Y" else "System / technical", opts, rounding, neg, vtype, "Annual")


# ===================================================================== W-2 ===
def ssa_w2():
    P = "W2"
    at("SSA-001 metadata")
    L = "fed.efw2.record_length"
    rows = [section("FILE: EFW2 SUBMISSION (SSA Publication 42-007, tax year 2026)")]
    at(f"{P}-001")
    rows.append(row("constant", "Record order and required records", "Record identifiers", "File", f"{P}-001", "N", "Y",
                    "Not conditional.", "1-2 of every record", "2", "AN", "RA", "File generator (system constant)",
                    f"Every record is {tag(L)} bytes. {tagr('fed.efw2.records')}. Edition: {tag('fed.efw2.edition')}. "
                    f"{src('fed.efw2.records')}",
                    "System / technical", "RA, RE, RW, RO, RS, RT, RU, RV, RF (see Field Options)", "Not applicable", "N",
                    "Code", "Annual"))
    at(f"{P}-002")
    rows.append(row("constant", "Tax year 2026 changes", "TY2026 changes", "File", f"{P}-002", "N", "Y", "Not conditional.",
                    "Not applicable", "Not applicable", "Text", "Signature PIN in RE", "File generator (system constant)",
                    f"{tagr('fed.efw2.ty2026_changes')}. The generator applies them from tax year 2026 and never writes the "
                    f"combined Code A+B money field. {src('fed.efw2.ty2026_changes')}",
                    "System / technical", "Not applicable", "Not applicable", "N", "Text", "Annual"))
    rows.append(gap_field(3, P, "RA submitter record and RT total record positions", RQ_EFW2,
                          "Positions of the RA submitter record, of the RW money and identity fields and of the RT totals are "
                          "in the held edition of Publication 42-007 but are not part of this release.", "Annual"))
    rows.append(section("RE: EMPLOYER RECORD"))
    RE = "rspec.fed.efw2.re.layout_ty2026"
    re_fields = [
        ("EIN", "Employer EIN", "Y", "Not conditional.", "N (9)", "123456789 (fictitious)",
         f"{DD_REF}: employer FEIN", f"Employer EIN without hyphen ({tag('fed.ein.format')}); never truncated "
         f"({tag('rspec.fed.w2.ssn_truncation')}).", "Not applicable", "Identifier"),
        ("Establishment Number", "Establishment number", "N", "Optional: used by employers that separate establishments.",
         "AN (4)", "0001", f"{DD_REF}: employer establishment (forward reference)",
         "Optional establishment identifier of the employer.", "Not applicable", "Identifier"),
        ("Other EIN", "Other EIN", "C", "Only when the employer used another EIN for this tax year.", "N (9)", "Blank",
         f"{DD_REF}: prior or other FEIN (forward reference)", "Another EIN used by the employer in the year.",
         "Not applicable", "Identifier"),
        ("Kind of Employer", "Kind of employer", "Y", "Not conditional.", "AN (1)", "Code per Field Options",
         f"{DD_REF}: employer kind (forward reference)", f"Kind-of-employer code; code list is an open point {gap(RQ_EFW2)}.",
         f"Open point {gap(RQ_EFW2)}", "Code"),
        ("Employment Code", "Employment code", "Y", "Not conditional.", "AN (1)", "Code per Field Options",
         f"{DD_REF}: employment type of the W-2 batch (forward reference)",
         f"Employment code of the batch; code list is an open point {gap(RQ_EFW2)}.", f"Open point {gap(RQ_EFW2)}", "Code"),
        ("Tax Jurisdiction Code", "Tax jurisdiction code", "Y", "Not conditional.", "AN (1)", "Blank for the 50 States and DC",
         "File generator (system constant)", f"Tax jurisdiction code; the code list is an open point {gap(RQ_EFW2)}. "
         "Territories are out of scope [US-FEDP52-007].", f"Open point {gap(RQ_EFW2)}", "Code"),
        ("Third-Party Sick Pay Indicator", "Third-party sick pay indicator", "C",
         "Only for a batch of third-party sick pay.", "AN (1)", "Blank",
         "Payroll result: third-party sick pay batch flag", "Indicator for third-party sick pay batches.",
         f"Open point {gap(RQ_EFW2)}", "Flag"),
        ("Employer Signature PIN", "Employer Signature PIN", "C",
         "Only when the employer holds a Signature PIN; blanks otherwise (new for tax year 2026).", "AN (10)",
         "Blank (no PIN)", f"{DD_REF}: employer Signature PIN (forward reference)",
         "New in tax year 2026. Composite key: uppercase S, hyphen, six characters, hyphen, one Luhn check character; hyphens "
         "are required. The check character must pass the Luhn algorithm before the file is released.",
         "Not applicable", "Identifier"),
    ]
    for i, (lab, nm, mand, cond, fmt, ex, mp, ex2, opts, vt) in enumerate(re_fields, start=4):
        rows.append(pos_row("payroll" if mand != "Y" or vt != "Code" else "system", P, i, "RE", nm, lab, RE, mand, cond, fmt,
                            ex, mp, ex2, opts, vt, payroll="Y" if vt in ("Identifier",) else "N"))
    rows.append(section("RW: EMPLOYEE WAGE RECORD"))
    at(f"{P}-012")
    rows.append(row("payroll", "Employee SSN", "Social security number", "RW", f"{P}-012", "Y", "Y", "Not conditional.",
                    f"Positions: open point {gap(RQ_EFW2)}", "9", "N (9)", "Valid SSN (fictitious in tests)",
                    f"{DD_REF}: employee SSN", f"Full SSN on the SSA copy. Truncation is allowed {tagr('rspec.fed.w2.ssn_truncation')}; "
                    f"the employee-copy mask is {tag('fed.ssn.truncation.format')}.",
                    "Yes: employee identifier", "Not applicable", "Not applicable", "N", "Identifier", "Annual"))
    at(f"{P}-013")
    rows.append(row("payroll", "Employee name and address", "Employee name and address", "RW", f"{P}-013", "Y", "Y",
                    "Not conditional.", f"Positions: open point {gap(RQ_EFW2)}", "Text", "AN", "DOE JANE A",
                    f"{DD_REF}: employee legal name and home address",
                    "Legal name as on the social security card and the home address held in master data. A multistate employee "
                    "keeps one name and address on every form issued.",
                    "Yes: employee master data", "Not applicable", "Not applicable", "N", "Text", "Annual"))
    money_fields = [
        ("Wages, tips, other compensation", "Federal taxable wages of the year: same base as Form 941 row F941-005, "
         "summed over the year [US-FEDS5-031]."),
        ("Federal income tax withheld", "FIT withheld in the year [US-FEDS5-031]."),
        ("Social security wages", f"Social security wages, capped at {tagr('fed.fica.oasdi.wage_base')} per employee for 2026."),
        ("Social security tax withheld", f"Employee share at {tag('fed.fica.oasdi.rate.employee')}% of the social security wages "
         "[US-FEDS5-005]."),
        ("Medicare wages and tips", "All Medicare wages, no cap [US-FEDS5-005]."),
        ("Medicare tax withheld", f"Employee share at {tag('fed.fica.medicare.rate.employee')}% plus Additional Medicare at "
         f"{tag('fed.fica.addl_medicare.rate')}% above {tag('fed.fica.addl_medicare.withholding_threshold')} [US-FEDS5-005]."),
    ]
    for i, (nm, ex2) in enumerate(money_fields, start=14):
        at(f"{P}-{i:03d}")
        rows.append(row("payroll", nm, nm, "RW", f"{P}-{i:03d}", "Y", "Y", "Not conditional.",
                        f"Positions: open point {gap(RQ_EFW2)}", "Money field", "Cents, no decimal point (EFW2 money field)",
                        "See Example Analysis", "Payroll result: annual accumulator",
                        f"{ex2} W-2 box number: open point {gap(RQ_W2BOX)}. Amounts reconcile with the four Forms 941 of the year.",
                        "Yes: annual total per employee", "Not applicable", "Cents", "N", "Amount", "Annual"))
    TW = "rspec.fed.efw2.rw.tipped_occupation_code"
    rows.append(pos_row("payroll", P, 20, "RW", "Primary Treasury Tipped Occupation Code (box 14b)", "Primary", TW, "C",
                        "Only when RO Code TP is present (cash tips reported); back-reference to W2-030.", "N (3)", "Code per Field Options",
                        f"{DD_REF}: Treasury Tipped Occupation Code per employee (forward reference)",
                        f"Box 14b: {tag('rspec.fed.w2.box14b')} [{rid('rspec.fed.w2.box14b')}]. New for tax year 2026.",
                        "Treasury Tipped Occupation Code list: Field Options", "Code"))
    rows.append(pos_row("payroll", P, 21, "RW", "Secondary Treasury Tipped Occupation Code", "Secondary", TW, "C",
                        "Only when the employee worked in more than one tipped occupation; back-reference to W2-020.", "N (3)",
                        "Blank", f"{DD_REF}: second Treasury Tipped Occupation Code (forward reference)",
                        "Second occupation code, only for employees with several tipped occupations.", "As W2-020", "Code"))
    rows.append(section("RO: EMPLOYEE OPTIONAL RECORD (box 12 money fields, 11 bytes)"))
    RO = "rspec.fed.efw2.ro.ty2026_money_fields"
    ro = [("combined Codes A+B", "Combined Codes A and B (not for 2026)"), ("Code A", "Box 12 Code A"), ("Code B", "Box 12 Code B"),
          ("Code J", "Box 12 Code J"), ("Code K", "Box 12 Code K"), ("Code L", "Box 12 Code L"), ("Code P", "Box 12 Code P"),
          ("Code TA", "Box 12 Code TA (employer Trump-account contributions)"), ("Code TP", "Box 12 Code TP (cash tips)"),
          ("Code TT", "Box 12 Code TT (qualified overtime)")]
    for i, (lab, nm) in enumerate(ro, start=22):
        old = lab.startswith("combined")
        rows.append(pos_row("excluded" if old else "payroll", P, i, "RO", nm, lab, RO, "N" if old else "C",
                            "Never populated for tax year 2026 (valid through tax year 2025 only)." if old else
                            f"Only when the employee has an amount under {lab}.",
                            "Money (11)", "Zeros" if old else "See Example Analysis",
                            "Not mapped" if old else f"Payroll result: box 12 {lab} accumulator",
                            "Retired field: the generator writes zeros." if old else
                            (f"New 2026 box 12 codes: {tag('rspec.fed.w2.box12.new_codes')} [{rid('rspec.fed.w2.box12.new_codes')}]."
                             if lab in ("Code TA", "Code TP", "Code TT") else f"Money field of box 12 {lab}, split out from tax year 2026."),
                            "Box 12 codes: Field Options", "Amount", payroll="N" if old else "Y", rounding="Cents"))
    rows.append(section("RS / RV: STATE RECORDS (see US-DOR-002)"))
    at(f"{P}-032")
    rows.append(row("system", "State record and state total record", "RS / RV", "RS, RV", f"{P}-032", "N", "C",
                    "Only where a State takes the W-2 data in the EFW2 file; SSA does not read them.", "See US-DOR-002",
                    tag(L), "AN", "See US-DOR-002", "File generator (State layouts in US-DOR-002)",
                    f"{tag('rspec.fed.efw2.rv_rf.layout')} The RS layout and each State's variant are specified in US-DOR-002 "
                    f"[{rid('rspec.fed.efw2.rv_rf.layout')}].", "System / technical", "Not applicable", "Not applicable", "N",
                    "Text", "Annual"))
    rows.append(section("RU: TOTAL OPTIONAL RECORD (15 bytes) AND RF: FINAL RECORD"))
    RU = "rspec.fed.efw2.ru.ty2026_money_fields"
    ru = [("combined A+B", "Combined Codes A and B (not for 2026)")] + ro[1:]
    for i, (lab, nm) in enumerate(ru, start=33):
        old = lab.startswith("combined")
        rows.append(pos_row("excluded" if old else "system", P, i, "RU", f"Total {nm}", lab, RU, "N" if old else "C",
                            "Never populated for tax year 2026." if old else f"Only when an RO record carries {lab}.",
                            "Money (15)", "Zeros" if old else "Sum of the RO field", "Calculated by the file generator",
                            "Retired field: zeros." if old else f"Total of RO {lab} over the employer's RO records.",
                            "Not applicable", "Calculated", payroll="N", rounding="Cents"))
    at(f"{P}-043")
    rows.append(pos_row("system", P, 43, "RF", "Number of RW records", "number of RW records", "rspec.fed.efw2.rv_rf.layout",
                        "Y", "Not conditional.", "N (9)", "000000037", "Calculated by the file generator",
                        "Count of RW records in the file.", "Not applicable", "Calculated", payroll="N"))
    rows.append(section("FORM W-2 RULES"))
    for i, (nm, key, mand, cond, vt) in enumerate([
        ("Due date to SSA and employees", "fed.w2.due_date", "Y", "Not conditional.", "Date"),
        ("Filing threshold without withholding", "fed.w2.no_withholding_threshold", "C",
         "Applies to employees with no federal withholding.", "Amount"),
        ("Two States and two localities per form", "rspec.fed.w2.multistate_boxes", "C",
         "Only for employees with more than two States or localities.", "Rule"),
        ("Corrections (Form W-2c, EFW2C)", "fed.efw2c.publication", "C", "Only after an error is found.", "Rule"),
    ], start=44):
        at(f"{P}-{i:03d}")
        rows.append(row("system", nm, nm, "Form rules", f"{P}-{i:03d}", "N", mand, cond, "Not applicable", "Not applicable",
                        "Rule", "See Example Analysis", "Filing calendar / form generator (system constant)",
                        f"{tagr(key)}. {src(key)}", "Yes", "Not applicable", "Not applicable", "N", vt, "Annual"))

    matrix = [["US-SSA-001", "Forms W-2 Wage and Tax Statement / W-3 Transmittal (and W-2c corrections)", "Forms W-2, W-3, W-2c",
               "Social Security Administration (SSA)", "Annual", tag("fed.w2.due_date"),
               "file_upload: EFW2 file transmitted by the reporting agent through SSA Business Services Online",
               f"EFW2 fixed-length records of {tag(L)} bytes (SSA Publication 42-007; W-2c in EFW2C, {tag('fed.efw2c.publication')}) "
               "via SSA Business Services Online",
               f"[{rid('fed.efw2.edition')}] {tag('fed.efw2.edition')}; [{rid('fed.w2.due_date')}]; {url('fed.efw2.edition')}",
               accuracy("file_upload", "SSA Business Services Online", url("fed.efw2.edition"), "CONFIRMED (channel), TO CONFIRM (full RW/RA/RT positions)",
                        "85% (official file specification read; RA, RW identity/money and RT positions not carried)",
                        f"the RA, RW and RT positions of Publication 42-007 TY2026 {gap(RQ_EFW2)} and the W-2 box map {gap(RQ_W2BOX)}")]]
    at("W2 example")
    cap = num("fed.fica.oasdi.wage_base")
    w = Decimal("231000.00")
    ssw = min(w, cap)
    thr = num("fed.fica.addl_medicare.withholding_threshold")
    ex = [("WORKED EXAMPLE 1: ANNUAL FICA AMOUNTS ON ONE W-2 (constructed)", [
        ("231,000.00", "Wages for the year", "Constructed input", "Input"),
        (tag('fed.fica.oasdi.wage_base'), "Social security wages (W2-016)", f"lesser of 231,000.00 and {tag('fed.fica.oasdi.wage_base')}", "Annual cap"),
        (m2(money(ssw * pct('fed.fica.oasdi.rate.employee'))), "Social security tax withheld (W2-017)",
         f"{tag('fed.fica.oasdi.wage_base')} x {tag('fed.fica.oasdi.rate.employee')}%", "Half-up to the cent"),
        (m2(w), "Medicare wages (W2-018)", "No cap", "Calculation"),
        (m2(money(w * pct('fed.fica.medicare.rate.employee')) + money((w - thr) * pct('fed.fica.addl_medicare.rate'))),
         "Medicare tax withheld (W2-019)",
         f"231,000.00 x {tag('fed.fica.medicare.rate.employee')}% + (231,000.00 - {tag('fed.fica.addl_medicare.withholding_threshold')}) "
         f"x {tag('fed.fica.addl_medicare.rate')}% = {m2(money(w * pct('fed.fica.medicare.rate.employee')))} + "
         f"{m2(money((w - thr) * pct('fed.fica.addl_medicare.rate')))}", "Each term half-up to the cent"),
    ]), ("WORKED EXAMPLE 2: MULTISTATE AND THRESHOLD (constructed)", [
        ("3", "States with wages for one employee", "Constructed input", "Input"),
        ("2", "Forms W-2 issued", f"ceiling(3 / 2) = 2: {tag('rspec.fed.w2.multistate_boxes')}", "Second form repeats boxes a-f"),
        ("2,150.00", "Wages with no withholding", f"2,150.00 against {tag('fed.w2.no_withholding_threshold')}", "W-2 required"),
    ]), ("WORKED EXAMPLE 3: FIELD LENGTHS FROM POSITIONS", [
        ("490-492", "Primary Treasury Tipped Occupation Code", "492 - 490 + 1 = 3 bytes", "Matches the published 3-digit code"),
        ("RE Signature PIN", "Employer Signature PIN", "end - start + 1 = 10 bytes (positions in row W2-011)", "S, hyphen, 6 characters, hyphen, check character"),
    ])]
    return fed_book(
        "US-SSA-001", "FormW2W3", "W-2 EFW2 Spec", "US-SSA-001 Forms W-2 and W-3 (EFW2) Wage and Tax Statements",
        "Annual wage and tax statement (federal, with State and local boxes)",
        "Annual totals reconcile with Forms 941 (US-IRS-001); State records (RS/RV) in US-DOR-002",
        "Annual", tag("fed.w2.due_date"),
        f"EFW2 fixed-length records of {tag(L)} bytes (SSA Publication 42-007; W-2c in EFW2C) via SSA Business Services Online",
        "RA, RE, RW, RO, RS, RT, RU, RV, RF", f"{url('fed.efw2.edition')} [{rid('fed.efw2.edition')}]",
        tag("fed.efw2.edition"), "US-DOR-002 State W-2 and annual reconciliation", matrix,
        "Every employee paid wages in the year gets a Form W-2; SSA receives them in one EFW2 file per employer.",
        [("WHO GETS REPORTED", [("Employees paid wages in 2026", "YES", "One RW record per employee and EIN."),
                                ("Employees with wages and no withholding", "YES", tag("fed.w2.no_withholding_threshold")),
                                ("Treaty-exempt wages of nonresident aliens", "NO", "Reported on Form 1042-S (US-IRS-006) [US-FEDS5-016]."),
                                ("Independent contractors", "NO", "Out of scope [US-OWN-008].")]),
         ("TIMING & RELATIONSHIP", [("Annual file", "YES", tag("fed.w2.due_date")),
                                    ("Corrections", "YES", tag("fed.efw2c.publication"))]),
         ("AMOUNTS & CALCULATIONS", [("Social security cap", "YES", tag("fed.fica.oasdi.wage_base")),
                                     ("New 2026 box 12 codes", "YES", tag("rspec.fed.w2.box12.new_codes"))]),
         ("SPECIAL CASES", [("More than two States or localities", "YES", tag("rspec.fed.w2.multistate_boxes")),
                            ("Household and agricultural batches", "PARTIAL", f"Separate employment code per batch; code list open point {gap(RQ_EFW2)}.")])],
        rows,
        [("FILE FORMAT", [f"Fixed-length ASCII records of {tag(L)} bytes, one record per line.",
                          tag("fed.efw2.records"), "FORMAT TO CONFIRM vs a real filing for the positions marked as open points."]),
         ("RECORD STRUCTURE", ["RA submitter (1)", "RE employer (1 per EIN batch)", "RW employee (1 per employee)",
                               "RO employee optional (when box 12 codes or other optional amounts exist)",
                               "RS state (optional, State-defined: US-DOR-002)", "RT total (1 per RE)",
                               "RU total optional (when RO exists)", "RV state total (optional, State-defined)", "RF final (1)"]),
         ("SECTION LAYOUT", [f"RE: {tag('rspec.fed.efw2.re.layout_ty2026')}", f"RW: {tag(TW)}", f"RO: {tag(RO)}", f"RU: {tag(RU)}",
                             f"RV / RF: {tag('rspec.fed.efw2.rv_rf.layout')}"])],
        [("RECORD IDENTIFIER (W2-001)", [(f"Record identifier", r, f"{r} record", f"{r}", f"[{rid('fed.efw2.records')}]")
                                         for r in ("RA", "RE", "RW", "RO", "RS", "RT", "RU", "RV", "RF")]),
         ("BOX 12 NEW CODES 2026 (W2-029 to W2-031)", [
             ("Box 12 code", "TA", "Employer Trump-account contributions", tag("rspec.fed.w2.box12.new_codes"), f"[{rid('rspec.fed.w2.box12.new_codes')}]"),
             ("Box 12 code", "TP", "Cash tips reported", tag("rspec.fed.w2.box12.new_codes"), f"[{rid('rspec.fed.w2.box12.new_codes')}]"),
             ("Box 12 code", "TT", "Qualified overtime compensation", tag("rspec.fed.w2.box12.new_codes"), f"[{rid('rspec.fed.w2.box12.new_codes')}]")]),
         ("TREASURY TIPPED OCCUPATION CODE (W2-020, W2-021)", [
             ("Tipped occupation code", "3-digit list", f"Code list: open point {gap(RQ_W2BOX)}", tag('rspec.fed.w2.box14b'), f"[{rid('rspec.fed.w2.box14b')}]")])],
        [("MANDATORY FIELD RULES", [
            ("Identity", "W2-012, W2-013", "Employee master data",
             "Full SSN and legal name on every SSA record; truncation only on employee copies; the EIN is never truncated.",
             "An employee without SSN at year end is reported once the SSN is issued; the file is not held for others.")]),
         ("PAYROLL-SPECIFIC POPULATION RULES", [
             ("Conditional", "W2-020 / W2-021 tipped occupation", "Tipped occupation per employee",
              "Write the primary code whenever RO Code TP carries an amount; write the secondary code only for employees working in "
              "more than one tipped occupation in the year. Both blank otherwise.",
              "An employee with tips only in a non-tipped occupation still needs the code once Code TP is present."),
             ("Conditional", "W2-023 to W2-031 box 12 amounts", "Payroll results per box 12 code",
              "Write an RO record only when at least one RO money field is non-zero; Codes A and B go in their separate 2026 fields and "
              "the combined field stays zero.", "Codes TA, TP, TT exist from tax year 2026 only."),
             ("Conditional", "W2-046 multistate", "State and locality accumulators",
              "Up to two States and two localities per form; a third State or locality starts another form that repeats boxes a to f "
              "and carries no federal amounts on Copy A.", "Nonresident State withholding counts as a State for this rule."),
             ("Conditional", "W2-004 to W2-011 RE fields", "Employer master data",
              "Other EIN only when the employer used another EIN in the year; Signature PIN only when issued (blanks otherwise); "
              "third-party sick pay indicator only for a sick pay batch.", "A PIN failing the Luhn check blocks the file.")]),
         ("CROSS-FIELD VALIDATIONS", [
             ("Reconciliation", "W2-014 to W2-019", "Generator",
              "Each money total over all RW records equals the RT total, and the year equals the sum of the four Forms 941.",
              "Differences are corrected on Form W-2c (EFW2C) and Form 941-X.")])],
        ex, NO_SAMPLE.format(ch="EFW2 file transmitted by the reporting agent through SSA Business Services Online"),
        extension=".txt (EFW2 ASCII)", encoding="ASCII", record_length=f"{tag(L)} bytes", authority=SSA)


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
    rows.append(gap_field(6, P, "Income code, exemption code and treaty article boxes", RQ_1042S,
                          "The 2026 Form 1042-S box codes for treaty-exempt wages are not part of this release.", "Annual"))
    matrix = [["US-IRS-006", "Form 1042-S, Foreign Person's U.S. Source Income Subject to Withholding (treaty-exempt wages)",
               "Form 1042-S", "Internal Revenue Service (IRS)", "Annual", tag("fed.form1042s.channel"),
               "file_upload: electronic filing through IRIS by the reporting agent",
               f"Electronic filing through IRIS ({tag('fed.form1042s.channel')}). {FIELD_MODEL}.",
               f"[{rid('fed.form1042s.channel')}]; {url('fed.form1042s.channel')}",
               accuracy("file_upload", "IRS IRIS", url("fed.form1042s.channel"), "CONFIRMED (channel), TO CONFIRM (box codes)",
                        "70% (rule and channel read; box codes not read)", f"the 2026 Instructions for Form 1042-S {gap(RQ_1042S)}")]]
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
        "Withholding agent; Recipient; Amounts; Open point (box codes)",
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
                          f"Box codes: open point {gap(RQ_1042S)}.", "FORMAT TO CONFIRM vs a real filing."])],
        [("VISA CLASS (F1042S-004)", [("Visa class", "Per Data Dictionary", tag("dd.fed.nra.visa_class"), "Visa class as issued",
                                       f"[{rid('dd.fed.nra.visa_class')}]")])],
        [("PAYROLL-SPECIFIC POPULATION RULES", [
            ("Conditional", "F1042S-005 treaty-exempt wages", "NRA flag; Form 8233 claim",
             "Accumulate only the wages covered by an accepted treaty claim while the employee is a nonresident alien; the same pay is "
             "excluded from the W-2 wage box and never reported twice.",
             "A claim that exceeds the treaty limit during the year stops at the limit; pay above it goes to Form W-2.")])],
        ex, NO_SAMPLE.format(ch="electronic filing through IRIS by the reporting agent"))


# ====================================================================== ACA ===
def irs_aca():
    P = "ACA"
    at("IRS-007 metadata")
    rows = [section("ALE DETERMINATION AND EMPLOYER RETURN (1094-C)"), ein_row(1, P, "Form 1094-C"), name_row(2, P, "Form 1094-C")]
    at(f"{P}-003")
    rows.append(row("payroll", "Applicable large employer status", "ALE member", "1094-C", f"{P}-003", "Y", "Y", "Not conditional.",
                    "Logical field (field model)", "1", "Flag", "Y", "Calculated from the monthly full-time and FTE counts",
                    f"An employer with {tagr('fed.aca.ale.fte_threshold')} or more full-time employees including full-time "
                    f"equivalents in the prior year files Forms 1094-C and 1095-C. The 2026 instructions are not issued; the 2025 "
                    f"edition was read {gap('rspec.fed.aca.ty2026_due_dates')}. {src('fed.aca.ale.fte_threshold')}",
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
                    f"Affordability percentage for 2026: {tagr('fed.aca.affordability.rate')}%. Used to test the employee's required "
                    f"contribution for the lowest-cost self-only coverage. {src('fed.aca.affordability.rate')}",
                    "Yes: offer of coverage codes", "Not applicable", "Two decimals as published", "N", "Rate", "Annual"))
    at(f"{P}-006")
    rows.append(row("system", "Electronic filing threshold", "E-file threshold", "1094-C", f"{P}-006", "N", "C",
                    "Applies when the employer files the threshold number of information returns or more.",
                    "Not applicable", "Not applicable", "Count", "Electronic", "Provider hand-off configuration",
                    f"Electronic filing is mandatory at {tagr('fed.aca.efile_threshold')} or more information returns in aggregate "
                    f"(tax year 2025 rule).", "Yes: channel", "Not applicable", "Not applicable", "N", "Count", "Annual"))
    rows.append(gap_field(7, P, "Form 1095-C offer, safe-harbor and cost lines", RQ_ACA,
                          "The 2026 line codes of Form 1095-C (offer of coverage, safe harbor, employee required contribution) are not part of this release.",
                          "Annual"))
    matrix = [["US-IRS-007", "Forms 1094-C / 1095-C (Affordable Care Act employer reporting)", "Forms 1094-C, 1095-C",
               "Internal Revenue Service (IRS)", "Annual", f"Open point {gap('rspec.fed.aca.ty2026_due_dates')} (2026 instructions not issued)",
               "file_upload: electronic filing by the reporting agent",
               f"Electronic filing (threshold per Instructions: {tag('fed.aca.efile_threshold')} returns). {FIELD_MODEL}.",
               f"[{rid('fed.aca.ale.fte_threshold')}] (2025 instructions) [{rid('fed.aca.affordability.rate')}]; {url('fed.aca.ale.fte_threshold')}",
               accuracy("file_upload", "IRS electronic filing through the reporting agent", url("fed.aca.ale.fte_threshold"), "TO CONFIRM",
                        "65% (2025 instructions read; 2026 not issued; line codes not read)",
                        f"the 2026 Instructions for Forms 1094-C and 1095-C {gap('rspec.fed.aca.ty2026_due_dates')} {gap(RQ_ACA)}")]]
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
        "Annual", f"Open point {gap('rspec.fed.aca.ty2026_due_dates')}",
        f"Electronic filing (threshold per Instructions). {FIELD_MODEL}.", "1094-C transmittal; 1095-C per employee",
        f"{url('fed.aca.ale.fte_threshold')} [{rid('fed.aca.ale.fte_threshold')}]",
        "Instructions for Forms 1094-C and 1095-C (2025 edition)", "US-SSA-001 Forms W-2/W-3", matrix,
        "Applicable large employers report the offer of health coverage to each full-time employee.",
        [("WHO GETS REPORTED", [("Full-time employees of an ALE member", "YES", tag("fed.aca.ale.fte_threshold")),
                                ("Employers below the ALE threshold", "NO", "No 1094-C / 1095-C filing.")]),
         ("TIMING & RELATIONSHIP", [("Annual filing", "YES", f"Due dates: open point {gap('rspec.fed.aca.ty2026_due_dates')}")]),
         ("AMOUNTS & CALCULATIONS", [("Affordability percentage 2026", "YES", f"{tag('fed.aca.affordability.rate')}%")]),
         ("SPECIAL CASES", [("Employees changing status during the year", "PARTIAL", "Monthly status per row ACA-004.")])],
        rows,
        [("FILE FORMAT", [f"Electronic filing at {tag('fed.aca.efile_threshold')} or more returns.", f"{FIELD_MODEL}.",
                          f"Line codes: open point {gap(RQ_ACA)}.", "FORMAT TO CONFIRM vs a real filing."])],
        [("MONTHLY STATUS (ACA-004)", [("Monthly status", "Per Data Dictionary", tag("dd.fed.aca.fte_tracking"), "Monthly status",
                                        f"[{rid('dd.fed.aca.fte_tracking')}]")])],
        [("PAYROLL-SPECIFIC POPULATION RULES", [
            ("Conditional", "ACA-006 electronic filing", "Count of information returns",
             "Count all information returns the employer files for the year; at or above the threshold the provider files "
             "electronically, below it paper remains possible but the provider route is electronic in this build.",
             "The 2026 threshold is read from the 2025 instructions until the 2026 edition is issued.")])],
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
    rows.append(gap_field(9, P, "Form 941-X lines, process choice and explanation", RQ_941X,
                          "The 2026 Form 941-X lines, the adjustment-or-claim choice and the certification lines are not part of this release.",
                          "Event-driven"))
    matrix = [["US-IRS-008", "Form 941-X, Adjusted Employer's Quarterly Federal Tax Return or Claim for Refund", "Form 941-X",
               "Internal Revenue Service (IRS)", "Event-driven (after an error is found)", f"Open point {gap(RQ_941X)}",
               "file_upload: electronic return transmitted by the reporting agent",
               f"Electronic return (e-file through the reporting agent). {FIELD_MODEL}.", "[US-FEDS5-031]",
               accuracy("file_upload", "IRS e-file through the authorised reporting agent (Form 8655)", url("rspec.fed.form941.frequency"),
                        "TO CONFIRM", "60% (correction route read; form lines not read)", f"the 2026 Form 941-X and instructions {gap(RQ_941X)}")]]
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
        "Event-driven", f"Open point {gap(RQ_941X)}", f"Electronic return (e-file through the reporting agent). {FIELD_MODEL}.",
        "Header; Corrected amounts; Open point", "[US-FEDS5-031]", "IRS Publication 15 (2026) as read for this release",
        "US-IRS-001 Form 941", matrix, "Corrections of a filed Form 941 quarter.",
        [("WHO GETS REPORTED", [("Employees whose amounts change in a filed quarter", "YES", "Rows F941X-004 to F941X-008.")]),
         ("TIMING & RELATIONSHIP", [("Filed after the error is found", "YES", "Never corrected on a later Form 941.")]),
         ("AMOUNTS & CALCULATIONS", [("Original, corrected and difference", "YES", "Three values per amount.")]),
         ("SPECIAL CASES", [("Matching Form W-2c", "YES", "Wage corrections of a closed year also need Form W-2c (US-SSA-001).")])],
        rows,
        [("FILE FORMAT", [f"{FIELD_MODEL}.", f"Lines: open point {gap(RQ_941X)}.", "FORMAT TO CONFIRM vs a real filing."])],
        [("QUARTER (F941X-003)", [("Quarter", f"Q{i}", f"Calendar quarter {i}", f"Quarter {i}", "[US-FEDS5-031]") for i in range(1, 5)])],
        [("PAYROLL-SPECIFIC POPULATION RULES", [
            ("Conditional", "F941X-004 to F941X-008", "Correction register",
             "Populate only the amounts that changed, each with the value filed, the corrected value and the difference; the "
             "difference drives the tax effect at the published rates.",
             "A correction that also changes a closed year's W-2 is paired with a Form W-2c.")])],
        ex, NO_SAMPLE.format(ch=AGENT))
