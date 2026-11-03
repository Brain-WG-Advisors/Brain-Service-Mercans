# -*- coding: utf-8 -*-
"""US-SSA-001 Forms W-2 / W-3: the EFW2 wire format (SSA Publication 42-007, tax year 2026).

Every record position comes from a layout fact (RA, RE, RW, RT full 512-byte records; RO / RU
tax-year 2026 money fields; RS; RV / RF). Full records are checked contiguous 1..512 at build
time (G-SPOT). The File Structure sheet is the wire format."""
import re
from decimal import Decimal

from us_common import (DD_REF, tag, tagr, rid, url, src, fact, num, pct, m2, money, gap, at, note_use, retag)
from us_rows import row, section, NONE_OPEN
from us_federal import accuracy
from us_fed_annual import fed_book, NO_SAMPLE
from us_lines import parse_layout, parse_named_positions, parse_codes, check_contiguous, split_top

SSA = "Social Security Administration (SSA), with the IRS"
P = "W2"
LEN = "fed.efw2.record_length"
MONEY = "rspec.fed.efw2.money_field.format"
BOX = "rspec.fed.w2.box_map"
LAYOUT = {"RA": "rspec.fed.efw2.ra.layout", "RE": "rspec.fed.efw2.re.layout", "RW": "rspec.fed.efw2.rw.layout",
          "RT": "rspec.fed.efw2.rt.layout"}
RO = "rspec.fed.efw2.ro.ty2026_money_fields"
RU = "rspec.fed.efw2.ru.ty2026_money_fields"
RS = "rspec.fed.efw2.rs.layout"
RVRF = "rspec.fed.efw2.rv_rf.layout"
CODES = {"Agent Indicator Code": "rspec.fed.efw2.re.agent_indicator.codes",
         "Kind of Employer": "rspec.fed.efw2.re.kind_of_employer.codes",
         "Employment Code": "rspec.fed.efw2.re.employment_code.codes",
         "Tax Jurisdiction Code": "rspec.fed.efw2.re.tax_jurisdiction.codes",
         "Third-Party Sick Pay Indicator": "rspec.fed.efw2.re.third_party_sick_pay.codes"}
TTOC = "rspec.fed.w2.box14b.ttoc_codes"
REC_NAME = {"RA": "submitter", "RE": "employer", "RW": "employee wage", "RO": "employee optional", "RT": "total",
            "RU": "total optional", "RS": "State", "RF": "final"}


# ---------------------------------------------------------------- box map ---
def box_positions():
    """(record, start, end) -> W-2 box id, from the box-map fact."""
    out = {}
    for it in split_top(str(fact(BOX)["value"]), "; "):
        m = re.match(r"^(\d{1,2}[a-z]?(?:-\d{1,2}[a-z]?)?)\s+(.*)$", it)
        if not m:
            continue
        box = m.group(1)
        pm = re.search(r"\((R[A-Z])\s+([^)]*)\)\s*$", it)
        if not pm:
            continue
        rec = pm.group(1)
        for a, b in re.findall(r"(\d{1,3})(?:-(\d{1,3}))?", pm.group(2)):
            out[(rec, int(a), int(b or a))] = box
    return out


def box_items():
    rows = []
    for it in split_top(str(fact(BOX)["value"]), "; "):
        m = re.match(r"^(\d{1,2}[a-z]?(?:-\d{1,2}[a-z]?)?)\s+(.*)$", it)
        if m:
            rows.append((m.group(1), m.group(2)))
    return rows


# --------------------------------------------------------- field classes ---
def is_money(rec, a, b, name):
    return (rec in ("RW", "RT", "RO", "RU") and (b - a + 1) in (11, 15)
            and not re.search(r"name|address|city|province|postal|number of", name, re.I))


def field_row(rec, n, a, b, name, key, boxes):
    loc = f"{P}-{rec}-{n:03d}"
    at(loc)
    if rec == "RO" and name == "Allocated Tips":
        key = BOX          # position read from the W-2 box map (box 8)
    note_use(key)
    ln = b - a + 1
    pos = f"{a}-{b}" if a != b else f"{a}"
    box = boxes.get((rec, a, b))
    if not box and rec == "RO" and name.startswith("Code ") and len(name) <= 7:
        box = f"12 ({name})"
    box_txt = f" W-2 box {box} [{rid(BOX)}]." if box else ""
    low = name.lower()
    s = src(key)
    if key == BOX:   # box text from the W-2 instructions; EFW2 position from Pub. 42-007
        s = f"{s} EFW2 position per [{rid(LAYOUT['RW'])}]."
    q = NONE_OPEN
    # defaults: content field of the record
    kind, pay, mand, vtype, fmt, ex = "payroll", "Y", "C", "Input (Text)", "Text (fixed length, see column I)", "As held"
    cond = ("Written when the data item exists for the " + REC_NAME.get(rec, rec) + " record; FORMAT TO CONFIRM vs a real "
            "filing for the content rules of the field.")
    mapping = f"{DD_REF}: employer master data (forward reference)"
    expl = f"{name}: {REC_NAME.get(rec, rec)} record field."
    opts = "Not applicable"
    rnd = "Not applicable"
    if re.match(r"record identifier", low):
        kind, pay, mand, vtype, fmt, ex = "constant", "N", "Y", "Output (Code)", "Constant", rec
        cond = "Not conditional: identifies the record."
        mapping = "File generator (system constant)"
        expl = f"Record identifier, always '{rec}'. Order of records: {tag('fed.efw2.records')}."
        opts = "See Field Options (record identifier)"
    elif low == "blank":
        kind, pay, mand, vtype, fmt, ex = "constant", "N", "Y", "Output (Filler)", "Blanks", "Spaces"
        cond = "Not conditional: blank-filled positions of the fixed-length record."
        mapping = "File generator (system constant)"
        expl = ("Unused positions: written as blanks so that every record keeps its fixed length. No payroll data is mapped "
                "to these positions; the generator fills them with spaces for the length in column I.")
    elif name in CODES:
        ck = CODES[name]
        kind, pay, vtype, fmt, ex = "system", "N", "Input (Code)", "Code (1)", parse_codes(fact(ck)["value"])[0][0]
        mand = "Y" if name == "Third-Party Sick Pay Indicator" else "C"
        cond = ("Not conditional: 1 or 0 on every record." if mand == "Y" else
                "Written per the code list in column M; blank where the code list says blank.")
        mapping = (f"{DD_REF}: employer W-2 batch configuration (forward reference)" if rec == "RE" else
                   "Payroll result: third-party sick pay flag per employee")
        expl = f"{name}: {tagr(ck)}."
        opts = "See Field Options (code list)"
    elif is_money(rec, a, b, name):
        kind, pay, mand, vtype, ex, rnd = "payroll", "Y", "Y", "Input (Amount)", "See Example Analysis", "Cents (assumed decimal)"
        fmt = f"Money ({ln}): see row {P}-003"
        cond = "Not conditional: zero-filled when the employee or batch has no amount (row W2-003)."
        if rec in ("RT", "RU"):
            kind, pay, vtype = "system", "N", "Calculated (Amount)"
            mapping = "Calculated by the file generator: sum of the matching employee field over the RE batch"
            expl = (f"{name}: total over the {'RW' if rec == 'RT' else 'RO'} records of the employer batch; it must equal the "
                    f"sum of the matching employee field.")
        else:
            mapping = f"Payroll result: annual accumulator per employee{(' (W-2 box ' + box + ')') if box else ''}"
            expl = f"{name}: annual amount per employee.{box_txt}"
            if box in ("3", "7"):
                expl += f" Boxes 3 and 7 together do not exceed {tagr('fed.fica.oasdi.wage_base')} for 2026."
            if name.startswith("combined"):
                kind, pay, mand, vtype, mapping = "excluded", "N", "N", "Display-only (Amount)", "Not mapped"
                cond = "Never populated for tax year 2026: the combined field is valid through tax year 2025 only."
                expl = ("Retired combined field: written as zeros for tax year 2026 (codes A and B have their own fields). "
                        "No payroll amount is mapped to it; amounts for codes A and B go to their own RO fields (rows above).")
            elif name in ("Code TA", "Code TP", "Code TT"):
                mand = "C"
                cond = f"Only when the employee has an amount under {name}; the RO record exists only with a non-zero RO field."
                expl += f" New 2026 box 12 codes: {tag('rspec.fed.w2.box12.new_codes')}."
            elif rec == "RO":
                mand = "C"
                cond = f"Only when the employee has an amount for this field; the RO record exists only with a non-zero RO field."
    elif re.search(r"tipped occupation", low):
        kind, pay, vtype, fmt, ex = "payroll", "Y", "Input (Code)", "N (3)", "Code per Field Options"
        mand = "C"
        prim = low.startswith("primary")
        cond = ("Only when RO Code TP (cash tips) carries an amount; back-reference to the secondary code row." if prim else
                "Only when the employee had tips in more than one occupation; back-reference to the primary code row.")
        mapping = f"{DD_REF}: Treasury Tipped Occupation Code per employee (forward reference)"
        expl = (f"{name} (box 14b): {tagr('rspec.fed.w2.box14b.rule')}. Code list: Field Options "
                f"({tag('rspec.fed.w2.box14b.ttoc_count')} occupation codes plus 000)."
                + (f" Valid from tax year 2026: {tag('rspec.fed.efw2.rw.tipped_occupation_code')}." if prim else ""))
        opts = "Treasury Tipped Occupation Codes (Field Options)"
    elif re.search(r"indicator", low):
        kind, pay, vtype, fmt, ex = "payroll", "Y", "Input (Flag)", "Code (1)", "Per Publication 42-007"
        cond = "Written per the indicator rule of the field; FORMAT TO CONFIRM vs a real filing for the code values."
        mapping = "Payroll result / employee master data (box 13 flags)" if box else f"{DD_REF}: employer master data"
        expl = f"{name}.{box_txt}"
    elif re.search(r"\bssn\b", low):
        mand, vtype, fmt, ex = "Y", "Input (Identifier)", "N (9)", "Valid SSN (fictitious in tests)"
        cond = "Not conditional: full SSN on the SSA record."
        mapping = f"{DD_REF}: employee SSN"
        expl = (f"Employee SSN, full on the SSA record. Truncation {tagr('rspec.fed.w2.ssn_truncation')}; employee-copy "
                f"mask {tag('fed.ssn.truncation.format')}.")
    elif re.search(r"\bein\b", low):
        mand = "Y" if re.search(r"submitter|employer/agent", low) else "C"
        vtype, fmt, ex = "Input (Identifier)", "N (9)", "123456789 (fictitious)"
        cond = ("Not conditional." if mand == "Y" else
                "Only when the agent indicator or another EIN used in the year requires it (column M).")
        mapping = (("Provider hand-off configuration (submitter = reporting agent)" if rec == "RA" else
                    f"{DD_REF}: employer FEIN"))
        expl = f"{name}: nine digits without hyphen ({tag('fed.ein.format')}); never truncated."
    elif re.search(r"tax year", low):
        kind, pay, mand, vtype, fmt, ex = "system", "N", "Y", "Input (Code)", "CCYY", "2026"
        cond = "Not conditional."
        mapping = "Payroll calendar (tax year of the file)"
        expl = "Tax year of the wages reported in the batch."
    elif re.search(r"signature pin", low):
        mand, vtype, fmt, ex = "C", "Input (Identifier)", "AN (10)", "Blank (no PIN)"
        cond = "Only when the employer holds a Signature PIN; blanks otherwise (new for tax year 2026)."
        mapping = f"{DD_REF}: employer Signature PIN (forward reference)"
        expl = ("Employer Signature PIN, new in tax year 2026. Composite key: uppercase S, hyphen, six characters, hyphen, "
                "one Luhn check character; hyphens are required. The check character must pass the Luhn algorithm before "
                "the file is released.")
    elif re.search(r"first name|last name|company name|employer name|submitter name", low):
        mand, vtype = "Y", "Input (Text)"
        cond = "Not conditional."
        mapping = (f"{DD_REF}: employee legal name" if rec == "RW" else
                   "Provider hand-off configuration (submitter = reporting agent)" if rec == "RA" else
                   f"{DD_REF}: employer legal name")
        expl = f"{name}." + (" Legal name as on the social security card." if rec == "RW" else "")
    else:
        if rec == "RA":
            kind, pay = "system", "N"
            mapping = "Provider hand-off configuration (submitter = reporting agent)"
        elif rec == "RW":
            mapping = (f"{DD_REF}: employee home address" if re.search(r"address|city|state|zip|province|postal|country", low)
                       else f"{DD_REF}: employee master data")
        elif re.search(r"number of rw", low):
            kind, pay, mand, vtype, fmt, ex = "system", "N", "Y", "Calculated (Count)", "N (zero-filled)", "37"
            cond = "Not conditional."
            mapping = "Calculated by the file generator: count of RW records"
            expl = f"{name}: count of RW records."
    if not re.match(r"(record identifier|blank)", low) and kind != "excluded":
        expl += (f" Taken from {mapping[0].lower() + mapping[1:]}." if not mapping.startswith(DD_REF) else
                 f" Taken from {mapping}.")
        expl += " The file generator writes it at the positions in column H with the length in column I."
    m_text = f"{rec} record. {expl} {s}"
    return row(kind, f"{rec} {name}", name, rec, loc, pay, mand, cond, pos, str(ln), fmt, ex, mapping, m_text,
               "Yes" if pay == "Y" else "System / technical", opts, rnd, "N", vtype, "Annual", q)


def record_rows(rec, layout, key, boxes):
    return [field_row(rec, i, a, b, nm, key, boxes) for i, (a, b, nm) in enumerate(layout, start=1)]


def fs_table(rec, layout, key, boxes):
    r = rid(key)
    lines = [f"|  Pos.     | Len | Field{' ' * 50}| W-2 box | Source"]
    for a, b, nm in layout:
        box = boxes.get((rec, a, b), "")
        pos = f"{a}-{b}" if a != b else f"{a}"
        lines.append(f"|  {pos:<8} | {b - a + 1:>3} | {nm:<55}| {box:<7} | [{r}]")
    return lines


def efw2_money(x):
    """Money field encoding of an amount: cents, right-justified, zero-filled."""
    return f"{int(money(x) * 100):011d}"


# ===================================================================== W-2 ===
def ssa_w2():
    at("SSA-001 metadata")
    boxes = box_positions()
    lay = {r: parse_layout(fact(k)["value"]) for r, k in LAYOUT.items()}
    for r, l in lay.items():
        check_contiguous(l, int(num(LEN)), r)
    # the TY2026 change summary (RE partial layout) must agree with the full RE layout
    full_re = {(a, b) for a, b, _ in lay["RE"]}
    for a, b, nm in parse_named_positions(fact("rspec.fed.efw2.re.layout_ty2026")["value"]):
        if (a, b) not in full_re:
            raise ValueError(f"RE TY2026 summary {nm} {a}-{b} disagrees with the full RE layout")
    ro = parse_named_positions(fact(RO)["value"])
    ru = parse_named_positions(fact(RU)["value"])
    rs = parse_named_positions(fact(RS)["value"])
    ro_tips = [(a, b, "Allocated Tips") for (rec, a, b), bx in boxes.items() if rec == "RO" and bx == "8"]
    rf = [(a, b, "Number of RW Records" if "RW" in nm else "Blank")
          for a, b, nm in parse_named_positions(str(fact(RVRF)["value"]).split("RF: ", 1)[1])]
    rf += [(int(a), int(b), "Blank") for a, b in re.findall(r"(\d{1,3})-(\d{1,3}) blank", str(fact(RVRF)["value"]).split("RF: ", 1)[1])]

    rows = [section("FILE: EFW2 SUBMISSION (SSA Publication 42-007, tax year 2026)")]
    at(f"{P}-001")
    rows.append(row("constant", "Record order and required records", "Record identifiers", "File", f"{P}-001", "N", "Y",
                    "Not conditional.", "1-2 of every record", "2", "AN", "RA", "File generator (system constant)",
                    f"Every record is {tag(LEN)} bytes. {tagr('fed.efw2.records')}. Edition: {tag('fed.efw2.edition')}. "
                    f"The generator writes the records in that order: one RA per file, one RE per employer batch, one RW per "
                    f"employee, an RT closing each batch and an RF closing the file. Optional records are written only when "
                    f"they carry data (RO, RU) or a State takes them (RS, RV). {src('fed.efw2.records')}",
                    "System / technical", "RA, RE, RW, RO, RS, RT, RU, RV, RF (see Field Options)", "Not applicable", "N",
                    "Output (Code)", "Annual"))
    at(f"{P}-002")
    rows.append(row("constant", "Tax year 2026 changes", "TY2026 changes", "File", f"{P}-002", "N", "Y", "Not conditional.",
                    "Not applicable", "Not applicable", "Text", "Signature PIN in RE", "File generator (system constant)",
                    f"{tagr('fed.efw2.ty2026_changes')}. RE fields changed for 2026: "
                    f"{tag('rspec.fed.efw2.re.layout_ty2026')}; these positions agree with the full RE record (rows {P}-RE-*). "
                    f"The generator never writes the combined Code A+B money field. {src('fed.efw2.ty2026_changes')}",
                    "System / technical", "Not applicable", "Not applicable", "N", "Display-only (Text)", "Annual"))
    at(f"{P}-003")
    mf = fact(MONEY)["value"]
    rows.append(row("constant", "Money field format", "Money fields", "File", f"{P}-003", "N", "Y", "Not conditional.",
                    "Every money field", "11 (RW, RO) / 15 (RT, RU)", "Numeric, assumed decimal", efw2_money(Decimal("59.60")),
                    "File generator (system constant)",
                    f"{tagr(MONEY)}. The generator converts each amount to cents and right-justifies it with leading zeros; "
                    f"negative amounts are never written (no sign position). Every amount comes from the payroll results "
                    f"already rounded to the cent; a field with no amount is written as zeros, never as blanks. {src(MONEY)}",
                    "System / technical", "Not applicable", "Cents (assumed decimal)", "N", "Display-only (Text)", "Annual"))
    at(f"{P}-004")
    rows.append(row("constant", "Form W-2 box map", "Box map", "File", f"{P}-004", "N", "Y", "Not conditional.",
                    "Not applicable", "Not applicable", "Text", "Box 1 = RW wages field", "File generator (system constant)",
                    f"{tagr(BOX)}. Box content per [{rid(BOX)}] (W-2 / W-3 instructions); EFW2 record positions per "
                    f"[{rid(LAYOUT['RW'])}] (SSA Publication 42-007). The RW, RO and RS rows below name their W-2 box; the full "
                    f"box list is in Field Options. {src(BOX)}", "Yes: employee statement", "W-2 boxes (Field Options)", "Not applicable", "N",
                    "Display-only (Text)", "Annual"))
    for rec, title in (("RA", "RA: SUBMITTER RECORD (one per file; full fixed-length record)"),
                       ("RE", "RE: EMPLOYER RECORD (one per EIN batch; full fixed-length record)"),
                       ("RW", "RW: EMPLOYEE WAGE RECORD (one per employee; full fixed-length record)")):
        rows.append(section(title))
        rows += record_rows(rec, lay[rec], LAYOUT[rec], boxes)
    rows.append(section("RO: EMPLOYEE OPTIONAL RECORD (tax-year 2026 money fields and allocated tips)"))
    rows += record_rows("RO", sorted(ro_tips + ro), RO, boxes)
    at(f"{P}-RO-900")
    rows.append(row("system", "RO other fields", "RO record (other fields)", "RO", f"{P}-RO-900", "N", "C",
                    "Applies to RO fields not listed above, when the employee has such an amount.",
                    "Not configured in this release", "Not applicable", "Text", "No value configured",
                    "File generator layout table (system constant)",
                    f"Positions of the other RO fields are not configured in this release {gap('RSPEC-RQ-15')}: "
                    f"the field list above carries allocated tips (box 8) and the tax-year 2026 money fields. Closes with: "
                    f"the RO and RU record tables of SSA Publication 42-007 (TY2026).",
                    "Yes: completeness of the RO record", "Not applicable", "Not applicable", "N", "Display-only (Text)",
                    "Annual", f"Open point {gap('RSPEC-RQ-15')}."))
    rows.append(section("RS / RV: STATE RECORDS (State-defined; see US-DOR-002)"))
    at(f"{P}-RS-001")
    rows.append(row("system", "State record and State total record", "RS / RV", "RS, RV", f"{P}-RS-001", "N", "C",
                    "Only where a State takes the W-2 data in the EFW2 file; SSA does not read them.", "See US-DOR-002",
                    tag(LEN), "AN", "See US-DOR-002", "File generator (State layouts in US-DOR-002)",
                    f"Generic RS positions: {tagr(RS)} (table in File Structure). {tag(RVRF)}. Each State's variant is "
                    f"specified in US-DOR-002 [{rid(RVRF)}].", "System / technical", "Not applicable", "Not applicable", "N",
                    "Display-only (Text)", "Annual"))
    rows.append(section("RT: TOTAL RECORD (one per RE batch; full fixed-length record)"))
    rows += record_rows("RT", lay["RT"], LAYOUT["RT"], boxes)
    rows.append(section("RU: TOTAL OPTIONAL RECORD (tax-year 2026 money fields)"))
    rows += record_rows("RU", ru, RU, boxes)
    at(f"{P}-RU-900")
    rows.append(row("system", "RU other fields", "RU record (other fields)", "RU", f"{P}-RU-900", "N", "C",
                    "Applies to RU fields not listed above, when an RO record carries such an amount.",
                    "Not configured in this release", "Not applicable", "Text", "No value configured",
                    "File generator layout table (system constant)",
                    f"Positions of the other RU fields are not configured in this release {gap('RSPEC-RQ-15')}. Closes with: "
                    f"the RO and RU record tables of SSA Publication 42-007 (TY2026).",
                    "Yes: completeness of the RU record", "Not applicable", "Not applicable", "N", "Display-only (Text)",
                    "Annual", f"Open point {gap('RSPEC-RQ-15')}."))
    rows.append(section("RF: FINAL RECORD (one per file)"))
    rows += record_rows("RF", rf, RVRF, boxes)
    rows.append(section("FORM W-2 RULES"))
    W2_RULE_EXTRA = {
        1: ("Held in the filing calendar as a date (YYYY-MM-DD) and used for both deliveries named in the field: the EFW2 "
            "file to SSA and the employee copies of Form W-2. The provider hand-off schedules both deliveries from this one "
            "date, and the date is re-read each year from the W-2 / W-3 instructions."),
        2: ("Applied by the form generator to the employees named in column G: their annual pay is compared with this "
            "amount to decide whether a Form W-2 is produced. The amount is held in whole dollars in the form generator "
            "configuration."),
        3: ("Applied by the form generator per employee: State and local lines beyond the capacity of one form go to an "
            "additional Form W-2, as the rule above states. The same State and local amounts appear in the RS records of "
            "US-DOR-002 (row RS-025)."),
        4: ("A correction of a filed Form W-2 is made on Form W-2c and transmitted in the EFW2C format of the publication "
            "above. The corrected and the originally reported amounts are taken from the correction register of the payroll."),
        5: ("Applied when box 12 code TP is reported (column G): the employee's Treasury Tipped Occupation Code is written in "
            "box 14b. The codes and their rule are in the tipped occupation rows of the RW record and in Field Options."),
    }
    for i, (nm, key, mand, cond, vt) in enumerate([
        ("Due date to SSA and employees", "fed.w2.due_date", "Y", "Not conditional.", "Date"),
        ("Filing threshold without withholding", "fed.w2.no_withholding_threshold", "C",
         "Applies to employees with no federal withholding.", "Amount"),
        ("Two States and two localities per form", "rspec.fed.w2.multistate_boxes", "C",
         "Only for employees with more than two States or localities.", "Rule"),
        ("Corrections (Form W-2c, EFW2C)", "fed.efw2c.publication", "C", "Only after an error is found.", "Rule"),
        ("Box 14b Treasury Tipped Occupation Codes", "rspec.fed.w2.box14b", "C", "Only when box 12 code TP is reported.", "Rule"),
    ], start=1):
        at(f"{P}-R{i:02d}")
        rows.append(row("system", nm, nm, "Form rules", f"{P}-R{i:02d}", "N", mand, cond, "Not applicable", "Not applicable",
                        "Rule", "See Example Analysis", "Filing calendar / form generator (system constant)",
                        f"{tagr(key)}. {W2_RULE_EXTRA[i]} {src(key)}", "Yes", "Not applicable", "Not applicable", "N", vt, "Annual"))

    matrix = [["US-SSA-001", "Forms W-2 Wage and Tax Statement / W-3 Transmittal (and W-2c corrections)", "Forms W-2, W-3, W-2c",
               "Social Security Administration (SSA)", "Annual", tag("fed.w2.due_date"),
               "file_upload: EFW2 file transmitted by the reporting agent through SSA Business Services Online",
               f"EFW2 fixed-length records of {tag(LEN)} bytes (SSA Publication 42-007; W-2c in EFW2C, {tag('fed.efw2c.publication')}) "
               "via SSA Business Services Online",
               f"[{rid('fed.efw2.edition')}] {tag('fed.efw2.edition')}; [{rid('fed.w2.due_date')}] [{rid(BOX)}] [{rid(LAYOUT['RW'])}]; {url('fed.efw2.edition')}",
               accuracy("file_upload", "SSA Business Services Online", url("fed.efw2.edition"),
                        "CONFIRMED (channel and RA, RE, RW, RT, RF positions), TO CONFIRM (other RO / RU positions)",
                        "90% (official file specification read: full RA, RE, RW, RT records, code lists, box map; no real filing)",
                        f"the RO and RU record tables {gap('RSPEC-RQ-15')} and one accepted real submission")]]

    at("W2 example")
    cap = num("fed.fica.oasdi.wage_base")
    w = Decimal("231000.00")
    ssw = min(w, cap)
    thr = num("fed.fica.addl_medicare.withholding_threshold")
    ss_tax = money(ssw * pct("fed.fica.oasdi.rate.employee"))
    med_tax = money(w * pct("fed.fica.medicare.rate.employee")) + money((w - thr) * pct("fed.fica.addl_medicare.rate"))
    pos = {nm: (a, b) for a, b, nm in lay["RW"]}

    def rw(nm):
        a, b = pos[nm]
        return f"RW {a}-{b}"
    ex = [("WORKED EXAMPLE 1: ANNUAL FICA AMOUNTS ON ONE W-2 AND THEIR EFW2 ENCODING (constructed)", [
        ("231,000.00", "Wages for the year", "Constructed input", "Input"),
        (efw2_money(w), f"Medicare Wages and Tips ({rw('Medicare Wages and Tips')}, box 5)", "No cap; cents, zero-filled",
         f"Encoding per row {P}-003"),
        (efw2_money(ssw), f"Social Security Wages ({rw('Social Security Wages')}, box 3)",
         f"lesser of 231,000.00 and {tag('fed.fica.oasdi.wage_base')}" + (" = the annual base" if ssw == cap else f" = {m2(ssw)}"),
         "Annual cap"),
        (efw2_money(ss_tax), f"Social Security Tax Withheld ({rw('Social Security Tax Withheld')}, box 4)",
         f"{tag('fed.fica.oasdi.wage_base') if ssw == cap else m2(ssw)} x {tag('fed.fica.oasdi.rate.employee')}% = {m2(ss_tax)}",
         "Half-up to the cent"),
        (efw2_money(med_tax), f"Medicare Tax Withheld ({rw('Medicare Tax Withheld')}, box 6)",
         f"231,000.00 x {tag('fed.fica.medicare.rate.employee')}% + (231,000.00 - {tag('fed.fica.addl_medicare.withholding_threshold')}) "
         f"x {tag('fed.fica.addl_medicare.rate')}% = {m2(money(w * pct('fed.fica.medicare.rate.employee')))} + "
         f"{m2(money((w - thr) * pct('fed.fica.addl_medicare.rate')))} = {m2(med_tax)}", "Each term half-up to the cent"),
    ]), ("WORKED EXAMPLE 2: MULTISTATE AND THRESHOLD (constructed)", [
        ("3", "States with wages for one employee", "Constructed input", "Input"),
        ("2", "Forms W-2 issued", f"ceiling(3 / 2) = 2: {tag('rspec.fed.w2.multistate_boxes')}", "Second form repeats boxes a-f"),
        ("2,150.00", "Wages with no withholding", f"2,150.00 against {tag('fed.w2.no_withholding_threshold')}", "W-2 required"),
    ]), ("WORKED EXAMPLE 3: RECORD LENGTH CHECK (computed from the layouts)", [
        (tag(LEN) if sum(b - a + 1 for a, b, _ in lay[r]) == int(num(LEN)) else "MISMATCH", f"{r} record length",
         f"sum of the {len(lay[r])} field lengths of the {r} layout", "Equals the published record length")
        for r in ("RA", "RE", "RW", "RT")
    ])]

    fo = [("RECORD IDENTIFIER (W2-001)", [("Record identifier", r, f"{r} record", f"{r}", f"[{rid('fed.efw2.records')}]")
                                          for r in ("RA", "RE", "RW", "RO", "RS", "RT", "RU", "RV", "RF")])]
    for nm, ck in CODES.items():
        note_use(ck)
        fo.append((f"RE / RW {nm.upper()} (code list)", [(nm, c, d, d, f"[{rid(ck)}]") for c, d in parse_codes(fact(ck)["value"])]))
    fo.append(("BOX 12 NEW CODES 2026 (RO Code TA, TP, TT)", [
        ("Box 12 code", c, d, tag("rspec.fed.w2.box12.new_codes"), f"[{rid('rspec.fed.w2.box12.new_codes')}]")
        for c, d in (("TA", "Employer Trump-account contributions"), ("TP", "Cash tips reported"),
                     ("TT", "Qualified overtime compensation"))]))
    tt = parse_codes(fact(TTOC)["value"])
    n_occ = sum(1 for c, _ in tt if c != "000")
    if n_occ != int(num("rspec.fed.w2.box14b.ttoc_count")):
        raise ValueError(f"TTOC list has {n_occ} occupation codes, fact count {num('rspec.fed.w2.box14b.ttoc_count')}")
    note_use(TTOC)
    fo.append(("TREASURY TIPPED OCCUPATION CODE (box 14b; RW primary and secondary)",
               [f"Source list: {tag(TTOC)}"] +
               [("Tipped occupation code", c, d, d, f"[{rid(TTOC) if c != '000' else rid('rspec.fed.w2.box14b.rule')}]")
                for c, d in tt]))
    note_use(BOX)
    fo.append(("FORM W-2 BOX MAP (box -> EFW2 field)",
               [("W-2 box", bx, retag(lab, ("fed.fica.oasdi.wage_base",)), retag(lab, ("fed.fica.oasdi.wage_base",)),
                 f"[{rid(BOX)}] [{rid(LAYOUT['RW'])}]" if re.search(r"\(R[A-Z]", lab) else f"[{rid(BOX)}]")
                for bx, lab in box_items()]))

    fs = [("FILE FORMAT (wire format)", [
        f"Fixed-length ASCII records of {tag(LEN)} bytes, one record per line; record order: {tag('fed.efw2.records')}.",
        f"Money fields: {tag(MONEY)}.",
        f"Edition: {tag('fed.efw2.edition')}. W-2c corrections use {tag('fed.efw2c.publication')}.",
        "Positions below are the published positions; every full record (RA, RE, RW, RT) covers positions 1 to "
        f"{tag(LEN)} with no gap and no overlap.",
        "FORMAT TO CONFIRM vs a real filing (no accepted submission held)."]),
          ("RECORD STRUCTURE", ["RA submitter (1)", "RE employer (1 per EIN batch)", "RW employee (1 per employee)",
                                "RO employee optional (only with a non-zero RO field)",
                                "RS state (optional, State-defined: US-DOR-002)", "RT total (1 per RE)",
                                "RU total optional (only when RO records exist)", "RV state total (optional, State-defined)",
                                "RF final (1)"])]
    for rec in ("RA", "RE", "RW", "RT"):
        fs.append((f"{rec} RECORD LAYOUT ({REC_NAME[rec]})", [f"Layout: {tag(LAYOUT[rec])}"] + fs_table(rec, lay[rec], LAYOUT[rec], boxes)))
    fs.append(("RO RECORD (tax-year 2026 money fields and allocated tips)",
               [f"Layout: {tag(RO)}"] + fs_table("RO", sorted(ro_tips + ro), RO, boxes) +
               [f"Other RO positions: not configured in this release {gap('RSPEC-RQ-15')}."]))
    fs.append(("RS RECORD (generic, State-defined; not read by SSA)", [f"Layout: {tag(RS)}"] + fs_table("RS", rs, RS, boxes)))
    fs.append(("RU RECORD (tax-year 2026 money fields)", [f"Layout: {tag(RU)}"] + fs_table("RU", ru, RU, boxes) +
               [f"Other RU positions: not configured in this release {gap('RSPEC-RQ-15')}."]))
    fs.append(("RV AND RF RECORDS", [f"Layout: {tag(RVRF)}"] + fs_table("RF", rf, RVRF, boxes)))

    def rows_of(rec):
        return [r[1][3] for r in rows if r[0] != "section" and str(r[1][3]).startswith(f"{P}-{rec}-")]

    pr = [("MANDATORY FIELD RULES", [
        ("Identity", f"{P}-RW SSN, first and last name", "Employee master data",
         "Full SSN and legal name on every RW record; truncation only on employee copies; the EIN is never truncated.",
         "An employee without SSN at year end is reported once the SSN is issued; the file is not held for others."),
        ("Money fields", f"{P}-RW, {P}-RT money fields", "Payroll results", f"Every money field is written on every record "
         f"(zero-filled when there is no amount) in the encoding of row {P}-003; RT totals equal the sum of the RW fields of "
         f"the batch.", "A negative amount is never written: corrections go to Form W-2c (EFW2C).")]),
        ("PAYROLL-SPECIFIC POPULATION RULES", [
            ("Conditional", f"{P}-RA content fields ({rows_of('RA')[0]} to {rows_of('RA')[-1]})", "Provider configuration",
             "The submitter record carries the reporting agent (provider) as submitter: its EIN, BSO user identification, "
             "contact and preparer data; resubmission fields only for a file resubmitted at SSA's request.",
             "One RA record per file even when the file carries several employer batches."),
            ("Conditional", f"{P}-RE content fields ({rows_of('RE')[0]} to {rows_of('RE')[-1]})", "Employer master data",
             "Agent for EIN only with an agent indicator code; Other EIN only when the employer used another EIN in the year; "
             "Kind of Employer, Employment Code and Tax Jurisdiction Code from the code lists; Signature PIN only when issued.",
             "A batch of household or agricultural employees is a separate RE batch with its own employment code."),
            ("Conditional", f"{P}-RW address and optional identity fields", "Employee master data",
             "Domestic address fields for a US address; foreign State/province, postal code and country code only for a "
             "foreign address; middle name and suffix only where held.", "A multistate employee keeps one name and address."),
            ("Conditional", f"{P}-RW tipped occupation codes", "Tipped occupation per employee",
             f"Write the primary code whenever RO Code TP carries an amount; the secondary code only for tips in more than one "
             f"occupation; code 000 when any tips came from a non-qualifying occupation ({tag('rspec.fed.w2.box14b.rule')}).",
             "Codes TA, TP, TT and box 14b exist from tax year 2026 only."),
            ("Conditional", f"{P}-RO fields", "Payroll results per box 12 code",
             "Write an RO record only when at least one RO money field is non-zero; Codes A and B go in their separate 2026 "
             "fields and the combined field stays zero.", "Allocated tips (box 8) are never included in boxes 1, 3, 5 or 7."),
            ("Conditional", f"{P}-R03 multistate", "State and locality accumulators",
             "Up to two States and two localities per form; a third State or locality starts another form that repeats boxes "
             "a to f and carries no federal amounts on Copy A.", "Nonresident State withholding counts as a State for this rule.")]),
        ("CROSS-FIELD VALIDATIONS", [
            ("Reconciliation", f"{P}-RW money fields, {P}-RT totals", "Generator",
             "Each RT total equals the sum of the matching RW field over the batch; the RF count equals the number of RW "
             "records; the year equals the sum of the four Forms 941.",
             "Differences are corrected on Form W-2c (EFW2C) and Form 941-X.")])]

    return fed_book(
        "US-SSA-001", "FormW2W3", "W-2 EFW2 Spec", "US-SSA-001 Forms W-2 and W-3 (EFW2) Wage and Tax Statements",
        "Annual wage and tax statement (federal, with State and local boxes)",
        "Annual totals reconcile with Forms 941 (US-IRS-001); State records (RS/RV) in US-DOR-002",
        "Annual", tag("fed.w2.due_date"),
        f"EFW2 fixed-length records of {tag(LEN)} bytes (SSA Publication 42-007; W-2c in EFW2C) via SSA Business Services Online",
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
                            ("Household and agricultural batches", "PARTIAL",
                             f"Separate RE batch per employment code: {tag('rspec.fed.efw2.re.employment_code.codes')}.")])],
        rows, fs, fo, pr, ex,
        NO_SAMPLE.format(ch="EFW2 file transmitted by the reporting agent through SSA Business Services Online"),
        extension=".txt (EFW2 ASCII)", encoding="ASCII", record_length=f"{tag(LEN)} bytes", authority=SSA)
