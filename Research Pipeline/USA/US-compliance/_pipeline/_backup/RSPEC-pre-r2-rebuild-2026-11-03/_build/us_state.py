# -*- coding: utf-8 -*-
"""The 11 per-jurisdiction Report Specifications (State, local and programme returns, new hires)."""
import datetime as dt
import re
from decimal import Decimal

from us_common import (STATES, STATE_NAMES, DD_REF, CCG_REF, fact, tag, tagr, rid, url, src, num, pct, m2, money,
                       gap, at, limitation, quote)
from us_rows import row, section
from us_federal import FIELD_MODEL, ein_row
from us_state_core import state_book, keys_for
from us_federal import accuracy
from us_common import gap_close as gap_close_txt

NO_TAX = {"AK": "rspec.ak.wh_return.applicable", "FL": "rspec.fl.wh_return.applicable", "NH": "rspec.nh.wh_return.applicable",
          "NV": "rspec.nv.wh_return.applicable", "SD": "rspec.sd.wh_return.applicable", "TN": "rspec.tn.wh_return.applicable",
          "TX": "rspec.tx.wh_return.applicable", "WA": "rspec.wa.wh_return.applicable", "WY": "rspec.wy.wh_return.applicable"}
TAXED = [s for s in STATES if s not in NO_TAX]


def R(P, n, kind, name, local, rec, payroll, mand, cond, pos, length, fmt, example, mapping, expl, rel, opts, rounding,
      neg, vtype, freq, query=None):
    at(f"{P}-{n:03d}")
    args = [kind, name, local, rec, f"{P}-{n:03d}", payroll, mand, cond, pos, length, fmt, example, mapping, expl, rel,
            opts, rounding, neg, vtype, freq]
    return row(*args) if query is None else row(*args, t=query)


def numbers_in(text):
    return [Decimal(x.replace(",", "")) for x in re.findall(r"\d[\d,]*(?:\.\d+)?", str(text))]


def scope(who, timing, amounts, special):
    return [("WHO GETS REPORTED", who), ("TIMING & RELATIONSHIP", timing), ("AMOUNTS & CALCULATIONS", amounts),
            ("SPECIAL CASES", special)]


SPECIAL_COMMON = [
    ("Nonresident alien employees", "PARTIAL", "Reported like other employees unless the jurisdiction rule in its section "
                                               "says otherwise; federal treaty exemptions do not change State reporting by themselves."),
    ("Household and agricultural employees (State level)", "NO",
     "State-level rules for special populations are deferred to a later round [US-OWN-005]."),
    ("Independent contractors", "NO", "Out of scope [US-OWN-008]."),
]


# ============================================================ DOR-001 ===
def dor_withholding():
    D, P = "US-DOR-001", "DOR"
    at(f"{D} common")
    common = [
        ein_row(1, "DOR-C", "State withholding return"),
        R("DOR-C", 2, "payroll", "State withholding account number", "State account number", "Header (employer)", "Y", "Y",
          "Not conditional.", "Logical field (field model)", "Per State", "Per State format", "Per State",
          f"{DD_REF}: per-State employer account identifiers (forward reference)",
          f"Account number issued by each State revenue department: {tagr('dd.employer.state_account_ids')}. Format and check "
          f"rules are State-specific and are applied as stated in the State section.",
          "Yes: employer master data", "Per State", "Not applicable", "N", "Identifier", "Per return"),
        R("DOR-C", 3, "system", "Filing period and frequency", "Filing period", "Header (period)", "N", "Y", "Not conditional.",
          "Logical field (field model)", "Per State", "Code", "2026Q1 or 2026-01",
          f"{DD_REF}: employer State filing frequency (master data), forward reference",
          "Period of the return. The frequency is assigned by each State or derived from the State's lookback amount, as "
          "stated in the State section, and is held as employer master data.",
          "Yes: selects the period", "See Field Options and the State section", "Not applicable", "N", "Code", "Per State schedule"),
        R("DOR-C", 4, "payroll", "State wages subject to withholding", "State wages", "Amounts", "Y", "Y", "Not conditional.",
          "Logical field (field model)", "Amount", "Decimal 13.2", "52,000.00", "Payroll result: State taxable wage accumulator per State",
          f"Wages subject to the State's income-tax withholding in the period, per State of withholding: "
          f"{tagr('rspec.multi.ui_qtr.recipient')}. Sourcing of wages between work State and residence State follows "
          f"{CCG_REF} Annex MULTI.", "Yes: per-State base", "Not applicable", "Cents unless the State rule says whole dollars",
          "N", "Amount", "Per State schedule"),
        R("DOR-C", 5, "payroll", "State income tax withheld", "State tax withheld", "Amounts", "Y", "Y", "Not conditional.",
          "Logical field (field model)", "Amount", "Decimal 13.2", "1,820.00", "Payroll result: State withholding accumulator per State",
          f"State income tax withheld in the period for the State; computation per {CCG_REF} Module 6 and the State annex.",
          "Yes: per-State tax", "Not applicable", "Cents unless the State rule says whole dollars", "N", "Amount", "Per State schedule"),
        R("DOR-C", 6, "payroll", "Payments and deposits for the period", "Payments", "Amounts", "Y", "Y", "Not conditional.",
          "Logical field (field model)", "Amount", "Decimal 13.2", "1,820.00", "Payroll result: State payment register",
          "Payments made to the State for the period on the State deposit schedule (State section). Balance due = row DOR-C-005 "
          "minus this row.", "Yes: reconciliation", "Not applicable", "Cents", "Y", "Amount", "Per State schedule"),
        R("DOR-C", 7, "constant", "Zero-return indicator", "Zero return", "Header", "N", "C",
          "Only for a period with no wages or no tax in a State that requires a return even with zero (State section rows "
          "classified Zero-return rule or Return form).", "Logical field (field model)", "1", "Flag", "Y",
          "Jurisdiction configuration (system constant)",
          "Many States require a return for every period even with nothing withheld; examples: "
          f"{tag('rspec.co.wh_return.zero')} [{rid('rspec.co.wh_return.zero')}]; {tag('rspec.al.wh_return.quarterly')}.",
          "Yes: completeness of the filing calendar", "Y / N", "Not applicable", "N", "Flag", "Per State schedule"),
        R("DOR-C", 8, "payroll", "Local tax carried on the State return", "Local withholding", "Amounts", "Y", "C",
          "Only for Indiana county tax, Maryland county tax and New York City / Yonkers tax, which are reported on the State "
          "withholding return; back-reference to US-LOC-001.", "Logical field (field model)", "Amount", "Decimal 13.2",
          "120.00", "Payroll result: local withholding per locality",
          f"Inputs: {tag('dd.in.county_residence_jan1')}; {tag('dd.md.county_residence')}; {tag('dd.ny.nyc_yonkers_residence')}. "
          "These localities are reported with the State return, not on a separate locality return "
          "[US-INS5-007, US-MDP51-001, US-NY-008].",
          "Yes: local tax", "Locality codes per State", "Cents", "N", "Amount", "Per State schedule"),
        R("DOR-C", 9, "payroll", "Other items on a combined State return", "Combined return items", "Amounts", "Y", "C",
          "Only for States whose return also carries UI, programme or levy items; back-reference to US-UI-001, US-PFML-001, "
          "US-DOR-004 and US-WC-001.", "Logical field (field model)", "Amount per item", "Decimal 13.2", "See State section",
          "Payroll results of the items listed",
          f"Oregon: {tag('rspec.or.oq.form')}. New York: {tag('rspec.ny.nys45.form')}. New Mexico: {tag('rspec.nm.wh_qtr_report.form')}. "
          f"Vermont: {tag('rspec.vt.wh_return.form')}.",
          "Yes: combined filing", "Per State", "Cents", "N", "Amount", "Quarterly"),
        R("DOR-C", 10, "payroll", "State of withholding per employee", "Work and residence State", "Routing", "Y", "Y",
          "Not conditional.", "Logical field (field model)", "2", "USPS code", "NY",
          f"{DD_REF}: work State and residence State (forward reference)",
          f"{tag('dd.multi.work_state')}; {tag('dd.multi.residence_state')}. Decide which States receive a withholding return.",
          "Yes: routing", "USPS State codes", "Not applicable", "N", "Code", "Per payment"),
        R("DOR-C", 11, "constant", "Agent authorisation per State", "Power of attorney", "Header (agent)", "N", "C",
          "Only in States that require their own agent form; examples California and Colorado.", "Not applicable",
          "Not applicable", "Text", "Form on file", "Provider hand-off configuration (system constant)",
          f"California: {tagr('rspec.ca.poa.form')}. Colorado: {tagr('rspec.co.poa.form')}. Federal Form 8655 extends to State "
          f"returns only where the State accepts it.", "Yes: precondition of the hand-off", "Not applicable", "Not applicable",
          "N", "Flag", "Once per employer and State"),
    ]
    gaps = {"DE": "rspec.de.wh_return.indexed_thresholds_2026", "IN": "rspec.in.wh_return.xml_schema", "NM": "rspec.nm.tap.bulk_schema"}
    at(f"{D} example")
    mo = num("mo.report.mo941.quarter_monthly_threshold")
    ine = num("rspec.in.wh_payment.eft_threshold")
    ex = [("WORKED EXAMPLE 1: THRESHOLD COMPARISONS (constructed)", [
        ("9,500.00", "Missouri withholding in each of two months of the prior 12",
         f"9,500.00 against {tag('mo.report.mo941.quarter_monthly_threshold')}", "At or above the published figure"
         if Decimal("9500") >= mo else "Below the published figure"),
        ("6,200.00", "Indiana average monthly payment", f"6,200.00 against {tag('rspec.in.wh_payment.eft_threshold')}",
         "Above: EFT required" if Decimal("6200") > ine else "Not above"),
    ]), ("WORKED EXAMPLE 2: BALANCE DUE (constructed)", [
        ("1,820.00", "State tax withheld (DOR-C-005)", "Constructed input", "Input"),
        ("1,500.00", "Payments for the period (DOR-C-006)", "Constructed input", "Input"),
        (m2(Decimal("1820") - Decimal("1500")), "Balance due", "1,820.00 - 1,500.00", "Calculation"),
    ])]
    return state_book(
        D, "StateWithholdingReturns", "State Withholding Spec", "US-DOR-001 State Income-Tax Withholding Returns and Deposits",
        "State departments of revenue / taxation (one per State; see Report Matrix)", "State income tax withheld (and local tax carried on the State return)",
        "Annual reconciliation and State W-2 in US-DOR-002; local returns in US-LOC-001", "Per State schedule (Report Matrix)",
        "Per State (Report Matrix)", f"Per State channel (Report Matrix). {FIELD_MODEL}.", "Header; Amounts; Routing; State sections",
        "State revenue department pages cited per row", "State pages as read for this release", "US-DOR-002; US-IRS-001",
        "Every State where withholding applies receives its periodic withholding return and payments; States without a wage "
        "income tax are listed with no return.", STATES, "State income-tax withholding return and deposits", "Per State schedule",
        common,
        scope([("Employees with wages subject to a State's withholding", "YES", tag("rspec.multi.ui_qtr.recipient")),
               ("States without a wage income tax", "NO", "AK, FL, NH, NV, SD, TN, TX, WA, WY: see Report Matrix rows.")],
              [("Periodic returns and deposits per State schedule", "YES", "State sections."),
               ("Annual reconciliation", "NO", "Specified in US-DOR-002.")],
              [("Indiana county, Maryland county, NYC / Yonkers local tax", "YES", "Carried on the State return (DOR-C-008).")],
              SPECIAL_COMMON + [("Multistate employees", "YES", "One return per State where withholding applies (DOR-C-010)."),
                                ("Connecticut household and agricultural returns", "NO",
                                 f"Deferred with State special populations [US-OWN-005]: {tag('rspec.ct.household.forms')}."),
                                ("Oregon household and agricultural annual returns", "NO",
                                 f"Deferred with State special populations [US-OWN-005]: {tag('rspec.or.annual.forms')}.")]),
        [("FILING FREQUENCY (DOR-C-003): internal configuration codes", [("Frequency", c, d, d, "Internal configuration code; the frequency itself is named by the State (State section)") for c, d in
                                           [("A", "Annual"), ("Q", "Quarterly"), ("M", "Monthly"), ("SM", "Semi-monthly"),
                                            ("SW", "Semi-weekly or accelerated"), ("W", "Weekly / eighth-monthly / quad-monthly")]])],
        [("MANDATORY FIELD RULES", [
            ("Routing", "DOR-C-010", "Work and residence State", "Generate a return for every State where the employer withholds "
             "in the period, and a zero return where the State requires one even without wages.",
             "An employee working in two States produces amounts on two State returns for the same period.")]),
         ("PAYROLL-SPECIFIC POPULATION RULES", [
             ("Conditional", "DOR-C-008 local tax", "Locality master data",
              "Fill only for Indiana counties, Maryland counties and New York City / Yonkers, from the locality held for the employee; "
              "these amounts travel on the State return, not on a separate locality return.",
              "A change of county of residence after 1 January follows the State rule stated in the annex."),
             ("Conditional", "DOR-C-009 combined return", "Payroll results",
              "For Oregon, New York, New Mexico and Vermont add the UI, programme and levy items the combined return carries, from "
              "the payroll results of those items.", "Items with no amount in the period are reported as zero where the form requires it."),
             ("Conditional", "DOR-C-007 zero return", "Jurisdiction configuration",
              "Where a State requires a return for every period, generate it with zero amounts when no wages were paid; never skip the period.",
              "A closed account stops the calendar only after the State confirms the closure.")])],
        ex, [("RECORD STRUCTURE", ["Header (employer, State account, period); amounts; routing; State-specific items."])],
        gaps=gaps, none=NO_TAX)


# ============================================================ DOR-002 ===
RS_FIELDS = [
    ("state code", 1, "State code (postal numeric)", "Code", "N (2)"),
    ("taxing entity", 1, "Taxing entity code", "Code", "AN (5)"),
    ("SSN", 1, "Employee SSN", "Identifier", "N (9)"),
    ("employee name", 1, "Employee name", "Text", "AN"),
    ("address", 1, "Employee address", "Text", "AN"),
    ("optional code", 1, "Optional code", "Code", "AN (2)"),
    ("reporting period", 1, "Reporting period", "Code", "MMCCYY"),
    ("SQUI total wages", 1, "State quarterly UI total wages", "Amount", "Money"),
    ("SQUI taxable wages", 1, "State quarterly UI taxable wages", "Amount", "Money"),
    ("weeks worked", 1, "Number of weeks worked", "Count", "N (2)"),
    ("date first employed", 1, "Date first employed", "Date", "MMDDCCYY"),
    ("date of separation", 1, "Date of separation", "Date", "MMDDCCYY"),
    ("state employer account number", 1, "State employer account number", "Identifier", "AN (20)"),
    ("state code", 2, "State code (income tax section)", "Code", "N (2)"),
    ("state taxable wages", 1, "State taxable wages", "Amount", "Money"),
    ("state income tax withheld", 1, "State income tax withheld", "Amount", "Money"),
    ("other state data", 1, "Other State data", "Text", "AN"),
    ("tax type code", 1, "Tax type code", "Code", "AN (1)"),
    ("local taxable wages", 1, "Local taxable wages", "Amount", "Money"),
    ("local income tax withheld", 1, "Local income tax withheld", "Amount", "Money"),
    ("state control number", 1, "State control number", "Identifier", "AN"),
    ("supplemental data 1", 1, "Supplemental data 1", "Text", "AN"),
    ("supplemental data 2", 1, "Supplemental data 2", "Text", "AN"),
]


def _pos(text, label, occ):
    ms = list(re.finditer(re.escape(label) + r"[^0-9;]*?(\d+)(?:-(\d+))?", text))
    m = ms[occ - 1]
    a = int(m.group(1))
    return a, int(m.group(2) or a)


def dor_annual():
    D = "US-DOR-002"
    RS = "rspec.fed.efw2.rs.layout"
    v = fact(RS)["value"]
    common = []
    for i, (lab, occ, nm, vt, fmt) in enumerate(RS_FIELDS, start=1):
        a, b = _pos(v, lab, occ)
        payroll = vt in ("Amount", "Identifier", "Date", "Count", "Text") and lab not in ("state control number", "other state data",
                                                                                          "supplemental data 1", "supplemental data 2",
                                                                                          "optional code")
        mand = "Y" if lab in ("state code", "SSN", "employee name", "state employer account number", "state taxable wages",
                              "state income tax withheld", "reporting period") else "C"
        cond = ("Not conditional for a State that takes the RS record." if mand == "Y" else
                "Only where the State's own RS variant (State section) uses the field; blanks otherwise.")
        mp = {"SSN": f"{DD_REF}: employee SSN", "employee name": f"{DD_REF}: employee legal name",
              "address": f"{DD_REF}: employee home address",
              "state employer account number": f"{DD_REF}: per-State employer account identifiers",
              "date first employed": f"{DD_REF}: hire date", "date of separation": f"{DD_REF}: termination date"}.get(
            lab, "Payroll result: State / local accumulator" if vt == "Amount" else "File generator (State layout table)")
        common.append(R("RS", i, "payroll" if payroll else "system", nm, lab, "RS (State record)", "Y" if payroll else "N",
                        mand, cond, f"{a}-{b}" if a != b else f"{a}", str(b - a + 1), fmt, "See Example Analysis", mp,
                        f"{nm}: generic EFW2 RS position. Layout: {tagr(RS)}. Each State may redefine the record; its variant is "
                        f"in the State section and prevails. {src(RS)}",
                        "Yes" if payroll else "System / technical",
                        "Tax type codes: Field Options" if lab == "tax type code" else
                        "State numeric codes: Field Options" if lab == "state code" else "Not applicable",
                        "Cents" if vt == "Amount" else "Not applicable", "N", vt, "Annual"))
    n = len(RS_FIELDS) + 1
    common.append(R("RS", n, "system", "Reserved end of record", "Blank", "RS (State record)", "N", "Y", "Not conditional.",
                    f"488 to the end of the record ({tag('fed.efw2.record_length')} bytes)", "25", "Blanks", "Blanks", "File generator", f"Reserved blanks per {tagr(RS)}.", "System / technical",
                    "Not applicable", "Not applicable", "N", "Text", "Annual"))
    common.append(R("RS", n + 1, "payroll", "State and local boxes 15-20 of Form W-2", "Boxes 15-20", "Form W-2", "Y", "C",
                    "Only for employees with State or local wages; more than two States or localities need another form.",
                    "Not applicable", "Not applicable", "Text", "Two States per form",
                    "Payroll result: State and local accumulators per employee",
                    f"{tagr('rspec.fed.w2.multistate_boxes')}. The RS record of each State carries the same amounts.",
                    "Yes", "Not applicable", "Cents", "N", "Amount", "Annual"))
    gaps = {"GA": "rspec.ga.w2_state.ty2026_layout", "HI": "rspec.hi.w2_state.ef10_layout", "ID": "rspec.id.w2_state.state_record_spec",
            "IL": "rspec.il.w2_state.idr986_spec", "KS": "rspec.ks.w2_state.ty2026_k2mt", "KY": "rspec.ky.w2_state.rs_spec",
            "LA": "rspec.la.w2_state.lawage_format", "MA": "rspec.ma.w2_state.handbook_edition", "MD": "rspec.md.w2_state.ty2026_spec",
            "ME": "rspec.me.w2_state.bulk_spec", "SC": "rspec.sc.w2_state.ty2026_rs1", "WV": "rspec.wv.w2_state.ty2026_it105",
            "NY": "rspec.ny.nys45.annual_mechanics", "NM": "rspec.nm.tap.bulk_schema"}
    at(f"{D} example")
    a1, b1 = _pos(v, "state income tax withheld", 1)
    ex = [("WORKED EXAMPLE 1: FIELD LENGTHS FROM THE RS POSITIONS", [
        ("RS-016", "State income tax withheld", f"end - start + 1 = {b1 - a1 + 1} bytes (positions in row RS-016)", "Matches the money field width"),
    ]), ("WORKED EXAMPLE 2: STATE TOTALS EQUAL THE SUM OF THE RS RECORDS (constructed)", [
        ("52,000.00", "RS record 1, State wages", "Constructed input", "Input"),
        ("48,500.00", "RS record 2, State wages", "Constructed input", "Input"),
        (m2(Decimal("52000") + Decimal("48500")), "State total (reconciliation form or RT / RV total)", "52,000.00 + 48,500.00",
         f"Massachusetts example of the rule: {tag('rspec.ma.w2_state.format')}"),
    ])]
    return state_book(
        D, "StateAnnualReconciliationW2", "State Annual Recon W-2 Spec",
        "US-DOR-002 State Annual Withholding Reconciliation and State Copies of Form W-2",
        "State departments of revenue / taxation (one per State; see Report Matrix)", "State income tax withheld (annual reconciliation)",
        "Reconciles the periodic returns of US-DOR-001; the RS / RV records extend the EFW2 file of US-SSA-001",
        "Annual", "Per State (Report Matrix)",
        f"Per State: EFW2 with the State RS / RV variant, State fixed-length or CSV formats, or portal entry (Report Matrix). {FIELD_MODEL} for the common rows.",
        "RS record (generic); State sections", f"{url(RS)} [{rid(RS)}] and State pages per row", "SSA Publication 42-007 (TY2026) and State pages as read",
        "US-SSA-001; US-DOR-001", "Annual State reconciliation of withholding and the State copy of each employee's Form W-2, per State "
        "with a wage income tax.", TAXED, "State annual reconciliation and State W-2 copies", "Annual", common,
        scope([("Employees with State wages or State tax in the year", "YES", "One RS record or State W-2 per State."),
               ("States without a wage income tax", "NO", "No reconciliation or State W-2 filing.")],
              [("Annual filing", "YES", "Due dates per State section; most are with or before the federal W-2 date.")],
              [("State totals equal the sum of the employee records", "YES", "See Example Analysis.")],
              SPECIAL_COMMON + [("Colorado annual credit notice to employees (DR 0995)", "NO",
                                 f"A notice delivered to employees, not a return: {tag('rspec.co.notice.dr0995')}."),
                                ("States that take no W-2 from the employer (e.g. California, New York)", "NO",
                                 f"{tag('rspec.ca.w2_state.filed')} (CA); {tag('rspec.ny.w2_state.filed')} (NY): see their sections.")]),
        [("RS TAX TYPE CODE (RS-018)", [("Tax type code", c, d, d, f"[{rid(RS)}]") for c, d in
                                        [("C", "City"), ("D", "County"), ("E", "School district"), ("F", "Other")]]),
         ("RS STATE NUMERIC CODE (RS-001, RS-014): codes read in State sections", [
             ("State code", c, STATE_NAMES[s], f"{STATE_NAMES[s]} numeric code", f"[{rid(k)}]") for s, c, k in
             [("AL", "01", "rspec.al.w2_state.rs_positions"), ("AZ", "04", "rspec.az.w2_state.format"),
              ("IA", "19", "rspec.ia.w2_state.format"), ("MS", "28", "rspec.ms.w2_state.format"), ("NE", "31", "rspec.ne.w2_state.format"),
              ("NC", "37", "rspec.nc.w2_state.ty2026_rs_layout"), ("SC", "45", "rspec.sc.w2_state.format"),
              ("VA", "51", "rspec.va.w2_state.format"), ("WV", "54", "rspec.wv.w2_state.format"), ("WI", "55", "rspec.wi.w2_state.format")]])],
        [("MANDATORY FIELD RULES", [
            ("RS record", "RS-001 to RS-016", "Employee and employer master data; annual accumulators",
             "Write one RS record per employee and State with the State's numeric code, the State employer account number, the State "
             "taxable wages and the State tax withheld; the State's variant in its section overrides the generic positions.",
             "States that forbid the RV record or require it are named in their sections; follow the State.")]),
         ("CROSS-FIELD VALIDATIONS", [
             ("Totals", "RS-015, RS-016", "Generator", "The State reconciliation totals equal the sum of the RS amounts and the sum of "
              "the periodic returns of US-DOR-001 for the year.", "A difference is corrected before filing; after filing, by the State "
              "correction route.")])],
        ex, [("RECORD STRUCTURE", ["Generic EFW2 RS record, then each State's variant (State sections)."])], gaps=gaps)


# ============================================================= UI-001 ===
def ui_wage():
    D = "US-UI-001"
    common = [
        R("UI-C", 1, "payroll", "Employer State UI account number", "UI account number", "Header (employer)", "Y", "Y",
          "Not conditional.", "Logical field (field model)", "Per State", "Per State", "Per State",
          f"{DD_REF}: per-State employer account identifiers (forward reference)", f"{tagr('dd.employer.state_account_ids')}.",
          "Yes: employer master data", "Per State", "Not applicable", "N", "Identifier", "Quarterly"),
        ein_row(2, "UI-C", "State UI wage report"),
        R("UI-C", 3, "payroll", "Recipient State (UI localization)", "State of coverage", "Routing", "Y", "Y", "Not conditional.",
          "Logical field (field model)", "2", "USPS code", "IL", f"{DD_REF}: UI State per employee per period (forward reference)",
          f"{tagr('rspec.multi.ui_qtr.recipient')}. Input: {tag('dd.multi.sui_state')}.", "Yes: routing", "USPS State codes",
          "Not applicable", "N", "Code", "Quarterly"),
        R("UI-C", 4, "payroll", "Employee SSN", "Social security number", "Per employee", "Y", "Y", "Not conditional.",
          "Per State layout", "9", "N (9)", "Valid SSN (fictitious in tests)", f"{DD_REF}: employee SSN",
          f"SSN of each employee paid in the quarter. ITIN is refused in some States: ITIN accepted in Florida: "
          f"{tag('rspec.fl.ui_qtr.itin_accepted')}; New Jersey: {tag('rspec.nj.ui_qtr.form')}. A missing SSN for a new hire may be reported with the "
          f"Georgia temporary-number rule only in Georgia: {tag('rspec.ga.ui_qtr.placeholder_ssn')}.",
          "Yes: employee identifier", "Not applicable", "Not applicable", "N", "Identifier", "Quarterly"),
        R("UI-C", 5, "payroll", "Employee name", "Name", "Per employee", "Y", "Y", "Not conditional.", "Per State layout", "Per State",
          "AN", "DOE JANE A", f"{DD_REF}: employee legal name", "Legal name; some layouts take last name and initials only "
          f"(e.g. {tag('rspec.ok.ui_qtr.format')}).", "Yes", "Not applicable", "Not applicable", "N", "Text", "Quarterly"),
        R("UI-C", 6, "payroll", "Gross wages paid in the quarter", "Total wages", "Per employee", "Y", "Y", "Not conditional.",
          "Per State layout", "Money", "Decimal 13.2", "13,250.00", "Payroll result: UI gross wage accumulator per State",
          f"UI wages paid in the quarter (wages are reported when paid, e.g. {tag('rspec.ak.ui_qtr.wage_basis')}). Some States "
          f"accept whole dollars: {tag('rspec.mn.ui_qtr.fields')}.", "Yes: UI wage base", "Not applicable",
          "Cents unless the State rule says whole dollars", "N", "Amount", "Quarterly"),
        R("UI-C", 7, "payroll", "Taxable (and excess) wages", "Taxable wages", "Per employee / employer", "Y", "Y", "Not conditional.",
          "Per State layout", "Money", "Decimal 13.2", "7,000.00", "Payroll result: UI taxable wage accumulator (State base)",
          "Wages up to the State taxable wage base for the year (State base in the CCG annex); excess = gross minus taxable. "
          f"Prior wages reported to other States can count toward the base: {tag('dd.state.ui.out_of_state_wages')}.",
          "Yes: contribution base", "Not applicable", "Cents", "N", "Amount", "Quarterly"),
        R("UI-C", 8, "payroll", "Monthly employment counts (pay period including the 12th)", "Monthly employment", "Employer",
          "Y", "C", "Only in States whose report asks for monthly counts (e.g. Arizona, Maine, Massachusetts, West Virginia).",
          "Per State layout", "3 counts", "N", "12, 12, 13", f"{DD_REF}: month-12 employment flag (forward reference)",
          f"{tagr('dd.state.ui.month12_count')}. Arizona example: {tag('rspec.az.ui_qtr.form')}.", "Yes", "Not applicable",
          "Not applicable", "N", "Count", "Quarterly"),
        R("UI-C", 9, "payroll", "Hours worked in the quarter", "Hours", "Per employee", "Y", "C",
          "Only in WA, MN, MA (required), NE (optional) and CT (optional from Q3 2026); back-reference to the State sections.",
          "Per State layout", "Per State", "N", "520", f"{DD_REF}: hours per employee per quarter (forward reference)",
          f"Washington: {tag('rspec.wa.ui_qtr.fields')}. Minnesota: {tag('dd.mn.ui.paid_hours')}. Massachusetts: "
          f"{tag('rspec.ma.ui_qtr.fields')}.", "Yes", "Not applicable", "Rounded as the State rule says", "N", "Count", "Quarterly"),
        R("UI-C", 10, "payroll", "Occupation (SOC code or job title)", "Occupation", "Per employee", "Y", "C",
          "Only in AK, WA, IN, WV (required), CT and NE (optional), TX (enhanced content when adopted); back-reference to the State sections.",
          "Per State layout", "6 or 8 digits / text", "Code", "15-1252",
          f"{DD_REF}: SOC code / job title per employee (forward reference)",
          f"Alaska: {tag('dd.ak.ui.occupation_code')}. Washington: {tag('dd.wa.ui.soc_code')}. Indiana: {tag('dd.in.ui.soc_start_date')}. "
          f"West Virginia: {tag('dd.wv.ui.soc_county')}. Texas: {tag('rspec.tx.ui_qtr.enhanced_content')}.",
          "Yes", "SOC list (federal)", "Not applicable", "N", "Code", "Quarterly"),
        R("UI-C", 11, "payroll", "Weeks counted per employee", "Weeks", "Per employee", "Y", "C",
          "Only in NJ (base weeks), PA (credit weeks) and OH (weeks paid); back-reference to the State sections.",
          "Per State layout", "2", "N", "13", f"{DD_REF}: weeks per employee (forward reference)",
          f"New Jersey base week minimum {tagr('rspec.nj.ui_qtr.base_week_amount')} for 2026 and "
          f"{tag('rspec.nj.ui_qtr.base_week_amount', '2027')} [{rid('rspec.nj.ui_qtr.base_week_amount', '2027')}] from 2027-01-01 "
          f"({tag('dd.nj.ui.base_weeks')}); Pennsylvania credit week "
          f"minimum {tagr('pa.report.ui.credit_week.amount')}; Ohio {tag('dd.oh.ui.weeks_paid')}.", "Yes", "Not applicable",
          "Whole weeks", "N", "Count", "Quarterly"),
        R("UI-C", 12, "payroll", "Other State-specific employee data", "State extras", "Per employee", "Y", "C",
          "Only in the State named in each item; back-reference to the State sections.", "Per State layout", "Per State", "Per State",
          "See State section", f"{DD_REF}: State-specific employee fields (forward reference)",
          f"Alaska geographic code: {tag('dd.ak.ui.geographic_code')}. Vermont: {tag('dd.vt.ui.gender_hourly')}. Missouri: "
          f"{tag('dd.mo.ui.separation_probation')}. Massachusetts: {tag('dd.ma.ui.hours_work_location')}. Florida E-Verify: "
          f"{tag('dd.fl.everify_certified')}. Washington exempt officers: {tag('dd.wa.exempt_officer')}.",
          "Yes", "Per State", "Not applicable", "N", "Code", "Quarterly"),
        R("UI-C", 13, "payroll", "UI contributions due", "Contributions", "Employer", "N", "Y", "Not conditional.", "Per State layout",
          "Money", "Decimal 13.2", "See State rate notice", "Calculated by the return generator from UI-C-007 and the State rate",
          "Taxable wages times the employer's State UI rate (rate notice per employer, CCG Module 5), plus levies carried on the "
          "UI return (US-OWN-007). Inbound rate notices are master data.", "Yes", "Not applicable", "Cents", "N", "Calculated",
          "Quarterly"),
    ]
    gaps = {"CO": "rspec.co.ui_qtr.format_due", "DE": "rspec.de.ui_qtr.file_format", "IA": "rspec.ia.ui_qtr.wage_detail_layout",
            "MN": "rspec.mn.ui_qtr.due_format", "MT": "rspec.mt.ui_qtr.efiling_handbook", "NE": "rspec.ne.ui_qtr.ftp_spec",
            "NH": "rspec.nh.ui_qtr.recheck", "NV": "rspec.nv.ui_qtr.form_name", "OH": "rspec.oh.ui_qtr.channel_format",
            "OK": "rspec.ok.ui_qtr.due_date", "SD": "rspec.sd.ui_qtr.upload_format", "TX": "rspec.tx.ui_qtr.enhanced_layout",
            "UT": "rspec.ut.ui_qtr.wage_file_layout", "WY": "rspec.wy.ui_qtr.file_spec", "GA": "rspec.ga.ui_qtr.universal_efile",
            "CT": "rspec.ct.ui_qtr.q3_2026_layout", "AR": "rspec.ar.ui_qtr.efile_threshold", "AZ": "rspec.az.ui_qtr.efile_mandate",
            "NM": "rspec.nm.tap.bulk_schema"}
    at(f"{D} example")
    nj = num("rspec.nj.ui_qtr.base_week_amount")
    nj27 = num("rspec.nj.ui_qtr.base_week_amount", "2027")
    pa = num("pa.report.ui.credit_week.amount")
    weeks = [Decimal(x) for x in ("300", "311", "450", "0", "320", "115", "117")]
    pen_vals = numbers_in(fact("rspec.az.ui_qtr.late_penalty")["value"])
    prate, pmin, pmax = pen_vals[0] / 100, pen_vals[1], pen_vals[2]
    pen = lambda w: min(max(money(w * prate), pmin), pmax)  # noqa: E731
    ex = [("WORKED EXAMPLE 1: NEW JERSEY BASE WEEKS AND PENNSYLVANIA CREDIT WEEKS (constructed)", [
        (", ".join(m2(w) for w in weeks), "Weekly wages of one employee (7 weeks)", "Constructed input", "Input"),
        (str(sum(1 for w in weeks if w >= nj)), "New Jersey base weeks (2026)", f"weeks with wages at or above {tag('rspec.nj.ui_qtr.base_week_amount')}",
         ", ".join(m2(w) for w in weeks if w < nj) + " do not count"),
        (str(sum(1 for w in weeks if w >= nj27)), "New Jersey base weeks (same wages in 2027)",
         f"weeks with wages at or above {tag('rspec.nj.ui_qtr.base_week_amount', '2027')}",
         ", ".join(m2(w) for w in weeks if w < nj27) + " do not count"),
        (str(sum(1 for w in weeks if w >= pa)), "Pennsylvania credit weeks", f"weeks with wages at or above {tag('pa.report.ui.credit_week.amount')}",
         ", ".join(m2(w) for w in weeks if w < pa) + " do not count"),
    ]), ("WORKED EXAMPLE 2: ARIZONA LATE-REPORT PENALTY (constructed)", [
        ("50,000.00", "Quarterly wages", f"50,000.00 x {pen_vals[0]} percent = {m2(money(Decimal('50000') * prate))}; within the limits",
         f"Rule: {tag('rspec.az.ui_qtr.late_penalty')}"),
        ("20,000.00", "Quarterly wages", f"20,000.00 x {pen_vals[0]} percent = {m2(money(Decimal('20000') * prate))}; minimum applies: {m2(pen(Decimal('20000')))}",
         "Minimum from the same rule"),
        ("500,000.00", "Quarterly wages", f"500,000.00 x {pen_vals[0]} percent = {m2(money(Decimal('500000') * prate))}; maximum applies: {m2(pen(Decimal('500000')))}",
         "Maximum from the same rule"),
    ]), ("WORKED EXAMPLE 3: WASHINGTON HOURS ROUNDING (constructed)", [
        ("519.25", "Hours worked in the quarter", "Rounded up to a whole number", f"Rule: {tag('rspec.wa.ui_qtr.fields')}"),
        ("520", "Hours reported", "ceiling(519.25)", "Calculation"),
    ])]
    return state_book(
        D, "StateUIWageReports", "State UI Wage Report Spec", "US-UI-001 State Unemployment Insurance Quarterly Contribution and Wage Reports",
        "State workforce / unemployment insurance agencies (one per State; see Report Matrix)", "State unemployment insurance (employer contributions; employee UI in AK, NJ, PA)",
        "Gives the FUTA credit on Form 940 (US-IRS-004); PFML/SDI items carried on some UI returns (US-PFML-001)",
        "Quarterly (Illinois also monthly wage reports in months 1 and 2 for larger employers)", "Per State (Report Matrix)",
        f"Per State: fixed-length (ICESA, State layouts), CSV, EFW2, XML where the State publishes a schema, or portal entry (Report Matrix). {FIELD_MODEL} for the common rows.",
        "Employer header; per-employee records; employer totals; State sections", "State UI agency pages cited per row",
        "State pages and file specifications as read for this release", "US-IRS-004 Form 940; US-PFML-001",
        "Quarterly UI contribution and wage report to the State of UI coverage of each employee.", STATES,
        "UI quarterly contribution and wage report", "Quarterly", common,
        scope([("Employees covered by the State's UI law (localization test)", "YES", tag("rspec.multi.ui_qtr.recipient")),
               ("Corporate officers without voluntary coverage (Washington)", "PARTIAL", tag("rspec.wa.ui_qtr.exempt_officers"))],
              [("Quarterly report, zero report where required", "YES", "State sections."),
               ("Illinois monthly wage reports", "YES", tag("rspec.il.ui_monthly.rule")),
               ("Separation notices to employees (e.g. NJ BC-10)", "NO",
                f"Delivered to the employee, not a return: {tag('rspec.nj.separation.form')}.")],
              [("Taxable wages up to the State base", "YES", "UI-C-007."), ("Employee UI (AK, NJ, PA)", "YES", "Per CCG Module 5.")],
              SPECIAL_COMMON + [("Event-driven mass-separation reports (SC UCB-113, GA)", "YES", tag("rspec.sc.mass_separation.form"))]),
        [("WEEKS RULE (UI-C-011)", [("Base week (NJ)", "BW", "Week at or above the NJ minimum", tag("rspec.nj.ui_qtr.base_week_amount"), f"[{rid('rspec.nj.ui_qtr.base_week_amount')}]"),
                                    ("Credit week (PA)", "CW", "Week at or above the PA minimum", tag("pa.report.ui.credit_week.amount"), f"[{rid('pa.report.ui.credit_week.amount')}]")])],
        [("MANDATORY FIELD RULES", [
            ("Routing", "UI-C-003", "UI State per employee", "Report each employee only to the State of UI coverage under the localization "
             "test, never to every work State; the withholding returns follow their own routing (US-DOR-001).",
             "An employee moving State mid-quarter is reported to each State for the wages localized there.")]),
         ("PAYROLL-SPECIFIC POPULATION RULES", [
             ("Conditional", "UI-C-008 to UI-C-012", "State-specific fields",
              "Populate each State-specific element only for the States that ask for it (listed in the condition column and the State "
              "section); other States receive the common elements only.",
              "Optional elements (NE hours and job title, CT Q3 2026 fields) are sent when the master data holds them.")])],
        ex, [("RECORD STRUCTURE", ["Employer header; one record per employee paid in the quarter; employer totals; State sections."])],
        gaps=gaps, extra={"FL": ["rspec.fl.other_forms"], "NY": ["rspec.ny.nys45.form", "rspec.ny.nys45.efile"],
                                 "OR": ["rspec.or.oq.form", "rspec.or.oq.due"]})


# ============================================================ PFML-001 ===
def pfml():
    D = "US-PFML-001"
    common = [
        R("PFML-C", 1, "payroll", "Premium State per employee", "Premium State", "Routing", "Y", "Y", "Not conditional.",
          "Logical field (field model)", "2", "USPS code", "WA", f"{DD_REF}: UI State per employee (forward reference)",
          f"{tagr('rspec.multi.pfml.state_key')}.", "Yes: routing", "USPS State codes", "Not applicable", "N", "Code", "Quarterly"),
        R("PFML-C", 2, "payroll", "Wages subject to the programme in the quarter", "Programme wages", "Per employee", "Y", "C",
          "Only where the programme report carries employee-level data (not Connecticut, see PFML-C-004).", "Per programme layout",
          "Money", "Decimal 13.2", "13,250.00", "Payroll result: programme wage accumulator",
          f"Washington: {tag('wa.report.pfml_ltc.fields')}.", "Yes", "Not applicable", "Cents", "N", "Amount", "Quarterly"),
        R("PFML-C", 3, "payroll", "Hours associated with wages", "Hours", "Per employee", "Y", "C",
          "Only in programmes that ask for hours (Washington, Delaware).", "Per programme layout", "Per programme", "N", "520",
          f"{DD_REF}: hours per employee per quarter (forward reference)",
          f"Delaware: {tag('dd.de.paid_leave.hours')}. Washington rule in PFML-C-002.", "Yes", "Not applicable",
          "Rounded up to whole hours (Washington)", "N", "Count", "Quarterly"),
        R("PFML-C", 4, "payroll", "Employer-level totals only (Connecticut)", "Return elements", "Employer", "Y", "C",
          "Only for Connecticut Paid Leave.", "Per programme layout", "Per programme", "XML or CSV", "See CT section",
          "Payroll results: CT wages, counts and contributions",
          f"{tag('rspec.ct.pfml_qtr.return_elements')}. {tag('rspec.ct.pfml_qtr.employee_records')}.", "Yes", "Not applicable",
          "Cents", "N", "Amount", "Quarterly"),
        R("PFML-C", 5, "payroll", "Premiums withheld and employer premiums", "Premiums", "Employer", "N", "Y", "Not conditional.",
          "Per programme layout", "Money", "Decimal 13.2", "See Example Analysis", "Calculated by the return generator",
          "Employee premiums withheld and employer premiums for the quarter, from the programme rates in CCG Module 5.",
          "Yes", "Not applicable", "Cents", "N", "Calculated", "Quarterly"),
    ]
    jurs = ["CA", "CO", "CT", "DC", "DE", "HI", "MA", "MD", "ME", "MN", "WA"]
    gaps = {"MA": "rspec.ma.pfml_qtr.return"}
    at(f"{D} example")
    r = pct("ca.sdi.employee.rate")
    ex = [("WORKED EXAMPLE 1: CALIFORNIA SDI ON THE STATE WAGE RETURN (constructed)", [
        ("10,000.00", "California SDI wages in the quarter", "Constructed input", "No wage cap"),
        (m2(money(Decimal("10000") * r)), "SDI withheld", f"10,000.00 x {tag('ca.sdi.employee.rate')}%", "Reported on DE 9 / DE 9C (US-UI-001)"),
    ]), ("WORKED EXAMPLE 2: WASHINGTON HOURS FOR A SALARIED FULL-TIME EMPLOYEE (constructed)", [
        ("13", "Weeks in the quarter", "Constructed input", "Input"),
        (str(40 * 13), "Hours reported", "40 x 13", f"Rule: {tag('wa.report.pfml_ltc.fields')}"),
    ])]
    return state_book(
        D, "PFMLProgrammeReports", "PFML SDI Report Spec", "US-PFML-001 State PFML / SDI / LTC Programme Reports",
        "State programme agencies (one per programme; see Report Matrix)", "Paid family and medical leave, disability and long-term care premiums",
        "Programmes filed on the State wage or UI return are in US-UI-001 / US-DOR-001 (CA, OR, NJ, RI)", "Quarterly (per programme)",
        "Per programme (Report Matrix)", f"Per programme channel (Report Matrix). {FIELD_MODEL} for the common rows.",
        "Routing; per-employee or employer totals; programme sections", "Programme pages cited per row",
        "Programme pages and file specifications as read for this release", "US-UI-001",
        "Programme reports filed separately from the State wage return.", jurs, "PFML / SDI / LTC programme report", "Quarterly",
        common,
        scope([("Employees covered by a State programme", "YES", tag("rspec.multi.pfml.state_key"))],
              [("Separate programme report", "YES", "Programme sections."),
               ("Programmes on another return", "NO", "CA SDI on DE 9 / DE 9C; OR Paid Leave on Form OQ; NJ TDI / FLI on NJ-927 / WR-30; "
                                                     "RI TDI on TX-17 (US-UI-001, US-DOR-001)."),
               ("Insurer-funded programmes without State report (NY DBL / PFL, HI TDI)", "NO", tag("rspec.hi.tdi.state_return"))],
              [("Premiums per programme rates", "YES", "CCG Module 5.")],
              SPECIAL_COMMON + [("Maryland FAMLI", "NO", f"No contribution in 2026: {tag('rspec.md.pfml.start')}.")]),
        [], [("PAYROLL-SPECIFIC POPULATION RULES", [
            ("Conditional", "PFML-C-002 to PFML-C-004", "Programme configuration",
             "Send employee-level wages and hours only to programmes that take them; Connecticut receives employer totals only and "
             "rejects employee-level records.", "A file with employee records for Connecticut is not processed.")])],
        ex, [("RECORD STRUCTURE", ["Programme header; employee records or employer totals; programme sections."])], gaps=gaps)


# ============================================================ LOC-001 ===
def local_tax():
    D = "US-LOC-001"
    common = [
        R("LOC-C", 1, "payroll", "Locality of work and residence", "Locality", "Routing", "Y", "Y", "Not conditional.",
          "Logical field (field model)", "Per locality", "Code", "Per locality", f"{DD_REF}: locality codes (forward reference)",
          f"Ohio: {tag('dd.oh.municipality_work')}; {tag('dd.oh.municipal_rate_table')}. Pennsylvania: {tag('dd.pa.psd_code')}. "
          f"Kentucky: {tag('dd.ky.locality')}. Michigan: {tag('dd.mi.city_residence_work')}. Colorado: {tag('dd.co.denver_opt')}. "
          f"Oregon: {tag('dd.or.metro_multnomah')}.", "Yes: routing", "Per locality", "Not applicable", "N", "Code", "Per locality schedule"),
        R("LOC-C", 2, "payroll", "Local taxable wages", "Local wages", "Amounts", "Y", "Y", "Not conditional.",
          "Logical field (field model)", "Money", "Decimal 13.2", "4,000.00", "Payroll result: local wage accumulator",
          "Wages subject to the local tax in the period, per locality (CCG Module 6 and the State annex).", "Yes", "Not applicable",
          "Cents", "N", "Amount", "Per locality schedule"),
        R("LOC-C", 3, "payroll", "Local tax withheld", "Local tax", "Amounts", "Y", "Y", "Not conditional.",
          "Logical field (field model)", "Money", "Decimal 13.2", "50.00", "Payroll result: local tax accumulator",
          "Local tax withheld (and employer part where the locality has one, e.g. Denver OPT).", "Yes", "Not applicable", "Cents",
          "N", "Amount", "Per locality schedule"),
        R("LOC-C", 4, "payroll", "Ohio school district code", "School district", "Per employee", "Y", "C",
          "Only for Ohio residents in a school district with an income tax.", "Logical field (field model)", "4", "N (4)", "Per list",
          f"{DD_REF}: Ohio school district of residence (forward reference)",
          f"{tag('dd.oh.school_district_code')}. List: {tag('rspec.oh.school_district.list')}.", "Yes", "School district list",
          "Not applicable", "N", "Code", "Per return"),
    ]
    jurs = ["AL", "CO", "DE", "KY", "MI", "MO", "OH", "OR", "PA", "WV"]
    extra = {"WV": ["wv.local.charleston.service_fee.weekly"]}
    gaps = {"WV": "rspec.wv.local.other_municipal_service_fees", "OR": "rspec.or.local.annual_xml_guide"}
    at(f"{D} example")
    wil = pct("de.local.wilmington.eit.rate")
    lex = pct("ky.local.lexington.rate")
    ex = [("WORKED EXAMPLE 1: DENVER OCCUPATIONAL PRIVILEGE TAX (constructed)", [
        ("2,000.00", "Earned in Denver in the month", f"2,000.00 against {tag('co.local.opt.denver.threshold_monthly')}: tax applies",
         f"Rule: {tag('rspec.co.local.denver_opt')}"),
        (tag("co.local.opt.denver.employee_monthly"), "Employee part withheld for the month", "Fixed monthly amount", "From the same rule"),
        (tag("co.local.opt.denver.employer_monthly"), "Employer part for the month", "Fixed monthly amount", "From the same rule"),
    ]), ("WORKED EXAMPLE 2: PERCENTAGE LOCAL TAXES (constructed)", [
        ("4,000.00", "Wilmington wages", f"4,000.00 x {tag('de.local.wilmington.eit.rate')}% = {m2(money(Decimal('4000') * wil))}",
         f"Rule: {tag('rspec.de.local.wilmington')}"),
        ("5,000.00", "Lexington-Fayette wages", f"5,000.00 x {tag('ky.local.lexington.rate')}% = {m2(money(Decimal('5000') * lex))}",
         f"Rule: {tag('rspec.ky.local.lexington')}"),
    ])]
    return state_book(
        D, "LocalIncomeWageTaxReturns", "Local Tax Return Spec", "US-LOC-001 Local Income / Wage Tax Returns",
        "Local taxing authorities (cities, counties, school districts, collectors; see Report Matrix)", "Local income, earnings and occupational taxes",
        "Indiana county, Maryland county and NYC / Yonkers tax travel on the State return (US-DOR-001); city employer payroll "
        "taxes in US-LOC-002 and US-LOC-003", "Per locality schedule", "Per locality (Report Matrix)",
        f"Per locality channel (Report Matrix). {FIELD_MODEL} for the common rows.", "Routing; amounts; State sections",
        "Local authority pages cited per row", "Local pages as read for this release", "US-DOR-001; US-LOC-002",
        "Separate locality returns in the 11 jurisdictions with local returns (New Jersey local employer taxes are in US-LOC-002).",
        jurs, "local income / wage tax returns", "Per locality schedule", common,
        scope([("Employees working or living in a locality with its own return", "YES", "State sections."),
               ("Indiana county, Maryland county, NYC / Yonkers", "NO", "Reported on the State return (US-DOR-001 row DOR-C-008).")],
              [("Periodic returns and annual reconciliation per locality", "YES", "State sections.")],
              [("Flat amounts and percentage taxes", "YES", "See Example Analysis.")], SPECIAL_COMMON),
        [], [("PAYROLL-SPECIFIC POPULATION RULES", [
            ("Conditional", "LOC-C-004 Ohio school district", "School district of residence",
             "Report the four-digit school district code of residence for Ohio residents of a taxing district on the SD returns and on the "
             "W-2; full-year nonresidents follow the code in the list.", "A move during the year splits the wages by period of residence.")])],
        ex, [("RECORD STRUCTURE", ["Locality header; employee or employer amounts per locality; State sections."])], gaps=gaps, extra=extra,
        what={"WV": "Other municipal service fee returns"},
        custom={"WV": lambda pfx, n0: [R(pfx, n0, "system", "Municipal service fee returns confirmed", "Service fee returns",
                                         "Jurisdiction parameter: WV", "N", "C",
                                         "Applies only in the municipalities named in column M; back-reference to the city rows above.",
                                         "Return level (not a file position)", "Not applicable", "Text", "Charleston CSF-2",
                                         "Jurisdiction configuration (system constant)",
                                         f"West Virginia municipal service fee returns, as read: "
                                         f"{quote('rspec.wv.local.service_fee_returns')}. {src('rspec.wv.local.service_fee_returns')}",
                                         "Yes: city fee returns", "Value as stated in column M", "Not applicable", "N", "Rule",
                                         "Quarterly")]},
        skip={"rspec.wv.local.service_fee_returns"},
        matrix_fix={"WV": {
            5: (f"Charleston and Morgantown: quarterly (rows LOC-WV-001 and LOC-WV-002); other municipalities: "
                f"{gap('rspec.wv.local.other_municipal_service_fees')}"),
            6: "paper",
            7: f"City fee return forms (Charleston CSF-2, Morgantown MSF-1) filed on paper with the city. {FIELD_MODEL}.",
            9: accuracy("paper", "City finance offices (Charleston, Morgantown)", url("rspec.wv.local.charleston.service_fee_return"),
                        "TO CONFIRM", "75% (Charleston and Morgantown city documents read; other municipalities not read)",
                        f"{gap_close_txt('rspec.wv.local.other_municipal_service_fees')} "
                        f"{gap('rspec.wv.local.other_municipal_service_fees')}")}})


# ============================================================ LOC-002 ===
def city_employer():
    D = "US-LOC-002"
    common = [
        R("CITY-C", 1, "payroll", "Payroll expense subject to the city tax", "Payroll expense", "Amounts", "Y", "Y", "Not conditional.",
          "Logical field (field model)", "Money", "Decimal 13.2", "250,000.00", "Payroll result: city payroll expense accumulator",
          "Compensation paid for work in the city in the period (base per city in the CCG annex).", "Yes", "Not applicable", "Cents",
          "N", "Amount", "Quarterly"),
        R("CITY-C", 2, "payroll", "Employer payroll tax due", "Tax due", "Amounts", "N", "Y", "Not conditional.",
          "Logical field (field model)", "Money", "Decimal 13.2", "See Example Analysis", "Calculated by the return generator",
          f"Base x city rate: Newark {tag('nj.pit.local.newark.employer_payroll_tax.rate')}%, Jersey City "
          f"{tag('nj.pit.local.jersey_city.employer_payroll_tax.rate')}%, St. Louis payroll expense "
          f"{tag('mo.pit.local.st_louis.payroll_expense_tax.rate')}%, Pittsburgh {tag('pa.pit.local.pittsburgh.payroll_expense.rate')}%. "
          "Employer-borne, never withheld.", "Yes", "Not applicable", "Cents", "N", "Calculated", "Quarterly"),
        R("CITY-C", 3, "payroll", "Earnings tax withheld from employees (St. Louis)", "Earnings tax", "Amounts", "Y", "C",
          "Only for St. Louis, where one return carries both taxes.", "Logical field (field model)", "Money", "Decimal 13.2",
          "See Example Analysis", "Payroll result: St. Louis earnings tax accumulator", f"{tagr('rspec.mo.local.st_louis')}.",
          "Yes", "Not applicable", "Cents", "N", "Amount", "Quarterly"),
    ]
    jurs = ["MO", "NJ", "PA"]
    extra = {"PA": ["pa.pit.local.pittsburgh.payroll_expense.rate"], "NJ": ["nj.pit.local.newark.employer_payroll_tax.rate",
                                                                            "nj.pit.local.jersey_city.employer_payroll_tax.rate"],
             "MO": ["mo.pit.local.st_louis.payroll_expense_tax.rate"]}
    gaps = {"PA": "rspec.pa.local.pittsburgh_payroll_expense.form_2026"}
    at(f"{D} example")
    base = Decimal("250000.00")
    ex = [("WORKED EXAMPLE: CITY EMPLOYER TAXES ON 250,000.00 OF PAYROLL EXPENSE (constructed)", [
        (m2(money(base * pct("nj.pit.local.newark.employer_payroll_tax.rate"))), "Newark",
         f"250,000.00 x {tag('nj.pit.local.newark.employer_payroll_tax.rate')}%", "Half-up to the cent"),
        (m2(money(base * pct("mo.pit.local.st_louis.payroll_expense_tax.rate"))), "St. Louis payroll expense tax",
         f"250,000.00 x {tag('mo.pit.local.st_louis.payroll_expense_tax.rate')}%", "Half-up to the cent"),
        (m2(money(base * pct("pa.pit.local.pittsburgh.payroll_expense.rate"))), "Pittsburgh payroll expense tax",
         f"250,000.00 x {tag('pa.pit.local.pittsburgh.payroll_expense.rate')}%", "Half-up to the cent"),
    ])]
    return state_book(
        D, "CityEmployerPayrollTaxes", "City Employer Tax Spec",
        "US-LOC-002 City Employer Payroll Taxes (Jersey City, Newark, St. Louis, Pittsburgh)", "City tax offices (see Report Matrix)",
        "Employer payroll expense taxes (St. Louis return also carries the earnings tax withheld)",
        "Specified once here; the local income tax workbook US-LOC-001 cross-references it", "Quarterly (per city)",
        "Per city (Report Matrix)", f"Per city channel (Report Matrix). {FIELD_MODEL}.", "Amounts; city sections",
        "City pages cited per row", "City pages as read for this release", "US-LOC-001; US-LOC-003",
        "Employer-borne city payroll taxes filed on separate city returns.", jurs, "city employer payroll tax return", "Quarterly",
        common,
        scope([("Employers with payroll expense in the city", "YES", "City sections.")],
              [("Quarterly city returns", "YES", tag("rspec.nj.local.newark_jersey_city"))],
              [("Employer-borne tax on payroll expense", "YES", "Never deducted from employees.")],
              SPECIAL_COMMON),
        [], [], ex, [("CITY RETURN CONTENT (Pittsburgh Form ET-1)", [
            f"{tag('rspec.pa.local.pittsburgh_payroll_expense.return')} [{rid('rspec.pa.local.pittsburgh_payroll_expense.return')}]",
            f"2026 edition not read: {gap('rspec.pa.local.pittsburgh_payroll_expense.form_2026')}."])],
        gaps=gaps, extra=extra, what={"PA": "2026 edition of the return form"},
        matrix_fix={"PA": {
            5: "Quarterly; due dates in row LOC-PA-001 (2025 edition of Form ET-1)",
            6: "paper",
            7: f"Paper Form ET-1 filed with the City of Pittsburgh Department of Finance (structure of the 2025 edition). {FIELD_MODEL}.",
            9: accuracy("paper", "City of Pittsburgh Department of Finance", url("rspec.pa.local.pittsburgh_payroll_expense.return"),
                        "TO CONFIRM", "75% (2025 Form ET-1 read; 2026 edition not read)",
                        f"{gap_close_txt('rspec.pa.local.pittsburgh_payroll_expense.form_2026')} "
                        f"{gap('rspec.pa.local.pittsburgh_payroll_expense.form_2026')}")}})


# ============================================================ LOC-003 ===
def seattle():
    D = "US-LOC-003"
    common = [
        R("SEA-C", 1, "payroll", "Seattle payroll expense", "Payroll expense", "Amounts", "Y", "Y", "Not conditional.",
          "Logical field (field model)", "Money", "Decimal 13.2", "See Example Analysis", "Payroll result: Seattle compensation accumulator",
          f"{tagr('wa.local.seattle.payroll_expense_tax')}. Base for 2026: Seattle payroll expense of employees whose annual "
          f"compensation is at least {tagr('rspec.wa.local.seattle.pet.employee_comp_threshold')}; tiers and rates in the WA "
          f"section.", "Yes", "Not applicable", "Cents", "N", "Amount", "Quarterly"),
        R("SEA-C", 2, "payroll", "Social Housing Tax base and rate", "Social Housing Tax", "Amounts", "Y", "C",
          "Only for employees whose Seattle compensation exceeds the Social Housing Tax threshold; back-reference to SEA-C-001.",
          "Logical field (field model)", "Money", "Decimal 13.2", "See Example Analysis",
          "Payroll result: Seattle compensation accumulator per employee",
          f"Rate {tagr('wa.local.seattle.social_housing.rate')}% ({tagr('rspec.wa.local.seattle.sht.rate')}%) of each employee's "
          f"compensation above {tagr('rspec.wa.local.seattle.sht.excess_comp_threshold')} (not indexed). Payment rule: "
          f"{tag('rspec.wa.local.seattle.sht.due')}.", "Yes", "Not applicable", "Cents", "N", "Amount", "Quarterly"),
        R("SEA-C", 3, "constant", "Taxpayer Authorization Form", "Authorization", "Header (agent)", "N", "Y", "Not conditional.",
          "Not applicable", "Not applicable", "Flag", "On file", "Provider hand-off configuration",
          f"{tagr('sir.wa.local.seattle_pet')}.", "Yes: precondition", "Not applicable", "Not applicable", "N", "Flag", "Once per employer"),
    ]
    BT = "rspec.wa.local.seattle.base_thresholds_due"

    def sea_rows(pfx, n0):
        out = []
        for i, (nm, keys, txt) in enumerate([
            ("PET applicability test (prior-year Seattle payroll)", ["rspec.wa.local.seattle.pet.prior_year_payroll_threshold"],
             "The 2026 tax applies only when the employer's 2025 Seattle payroll expense is at least {0}."),
            ("PET compensation bands (per employee)", ["rspec.wa.local.seattle.pet.employee_comp_threshold",
                                                      "rspec.wa.local.seattle.pet.comp_level_2_floor"],
             "Only employees with annual compensation of at least {0} enter the base; the higher rate band starts at {1}."),
            ("PET payroll tiers (employer)", ["rspec.wa.local.seattle.pet.tier_2_floor", "rspec.wa.local.seattle.pet.tier_3_floor"],
             "Tier 2 starts at a payroll expense of {0} and tier 3 at {1}; the rate per tier and band is in the row of the "
             "2026 base, thresholds and due dates."),
        ], start=n0):
            at(f"{pfx}-{i:03d}")
            vals = [tagr(k) for k in keys]
            out.append(R(pfx, i, "system", nm, "Threshold", f"Jurisdiction parameter: WA", "N", "C",
                         "Applies to the 2026 return only (the figures are indexed each year); back-reference to SEA-C-001.",
                         "Return level (not a file position)", "Amount", "Whole dollars", "See Example Analysis",
                         "Jurisdiction configuration per year (system constant)",
                         f"Seattle, {nm}: " + txt.format(*vals) + f" Valid for 2026 only. {src(keys[0])}",
                         "Yes: decides the base and the rate", "Value as stated in column M", "Whole units as published", "N",
                         "Amount", "Quarterly"))
        for j, (nm, key, txt) in enumerate([
            ("2026 base, rates by tier and band, due dates and channel", BT,
             "Rates per tier and compensation band, due dates and filing channel for 2026, as published by the city."),
            ("Social Housing Tax payment schedule", "rspec.wa.local.seattle.sht.due",
             "Payment and return schedule of the Social Housing Tax."),
        ], start=n0 + 3):
            at(f"{pfx}-{j:03d}")
            out.append(R(pfx, j, "system", nm, "City rule", "Jurisdiction parameter: WA", "N", "Y",
                         "Not conditional: applies to every employer filing the Seattle return.",
                         "Return level (not a file position)", "Not applicable", "Text", "See column M",
                         "Jurisdiction configuration per year (system constant)",
                         f"Seattle, {nm}: {tagr(key)}. {txt} {src(key)}", "Yes: computes and files the city return",
                         "Value as stated in column M", "Rates as published", "N", "Rule", "Quarterly",
                         (f"Confirm against a real filing: the source carries confidence {fact(key).get('confidence')} "
                          f"[{rid(key)}]." if fact(key).get("confidence") != "high" else None)))
        return out
    at(f"{D} example")
    comp = Decimal("1180000.00")
    sht_thr = num("rspec.wa.local.seattle.sht.excess_comp_threshold")
    sht = money((comp - sht_thr) * pct("rspec.wa.local.seattle.sht.rate"))
    prior, payroll, ecomp = Decimal("20000000.00"), Decimal("50000000.00"), Decimal("300000.00")
    pthr = num("rspec.wa.local.seattle.pet.prior_year_payroll_threshold")
    t2 = num("rspec.wa.local.seattle.pet.tier_2_floor")
    t3 = num("rspec.wa.local.seattle.pet.tier_3_floor")
    c1 = num("rspec.wa.local.seattle.pet.employee_comp_threshold")
    c2 = num("rspec.wa.local.seattle.pet.comp_level_2_floor")
    tier = 1 if payroll < t2 else (2 if payroll < t3 else 3)
    band = "below the base threshold" if ecomp < c1 else ("lower band" if ecomp < c2 else "higher band")
    sea_ex = [("WORKED EXAMPLE 1: SOCIAL HOUSING TAX FOR ONE EMPLOYEE (constructed)", [
        (m2(comp), "Seattle compensation of the employee in the year", "Constructed input", "Input"),
        (m2(comp - sht_thr), "Compensation above the threshold", f"{m2(comp)} - {tag('rspec.wa.local.seattle.sht.excess_comp_threshold')}",
         "Calculation"),
        (m2(sht), "Social Housing Tax", f"{m2(comp - sht_thr)} x {tag('rspec.wa.local.seattle.sht.rate')}%", "Half-up to the cent"),
    ]), ("WORKED EXAMPLE 2: PAYROLL EXPENSE TAX TIER AND BAND (constructed)", [
        (m2(prior), "2025 Seattle payroll expense", f"{m2(prior)} against {tag('rspec.wa.local.seattle.pet.prior_year_payroll_threshold')}",
         "At or above: the 2026 tax applies" if prior >= pthr else "Below: no 2026 tax"),
        (m2(payroll), "2026 Seattle payroll expense", f"against {tag('rspec.wa.local.seattle.pet.tier_2_floor')} and "
         f"{tag('rspec.wa.local.seattle.pet.tier_3_floor')}", f"Tier {tier}"),
        (m2(ecomp), "Annual compensation of one employee", f"against {tag('rspec.wa.local.seattle.pet.employee_comp_threshold')} and "
         f"{tag('rspec.wa.local.seattle.pet.comp_level_2_floor')}", f"In the base, {band}; rate of tier {tier} for that band per the WA section"),
    ])]
    return state_book(
        D, "SeattlePETSocialHousing", "Seattle PET SHT Spec", "US-LOC-003 Seattle Payroll Expense Tax and Social Housing Tax Returns",
        "City of Seattle, Department of Finance and Administrative Services", "Employer business taxes on Seattle payroll expense",
        "City employer taxes elsewhere in US-LOC-002", "Quarterly", f"Quarterly; dates in the Report Matrix ({tag(BT)})",
        "FileLocal portal / city return form; Taxpayer Authorization Form for payroll processors. " + FIELD_MODEL + ".",
        "Amounts; WA section", f"{url('rspec.wa.local.seattle')}; {url(BT)}", "City of Seattle FAS pages (2026 thresholds) as read for this release",
        "US-LOC-002",
        "Employers with Seattle payroll expense above the thresholds.", ["WA"], "Seattle payroll expense tax and Social Housing Tax return",
        "Quarterly", common,
        scope([("Employers with Seattle payroll expense above the threshold", "YES", tag("wa.local.seattle.payroll_expense_tax"))],
              [("Quarterly city return", "YES", tag("rspec.wa.local.seattle.sht.due"))],
              [("Employer-borne", "YES", "Not withheld from wages."),
               ("2026 thresholds (indexed yearly)", "YES", f"{tag('rspec.wa.local.seattle.pet.prior_year_payroll_threshold')}; "
                f"{tag('rspec.wa.local.seattle.pet.employee_comp_threshold')}")], SPECIAL_COMMON),
        [], [("PAYROLL-SPECIFIC POPULATION RULES", [
            ("Conditional", "SEA-C-002 Social Housing Tax", "Seattle compensation per employee",
             "For each employee, compare the year-to-date Seattle compensation with the Social Housing Tax threshold and report "
             "the excess at the rate of the WA section; quarterly installments may be estimated from the prior year's excess and "
             "corrected on the fourth-quarter return.", "An employee crossing the threshold late in the year enters from that quarter.")])],
        sea_ex, [("SEATTLE 2026 PARAMETERS", [f"{tag(BT)} [{rid(BT)}]"])],
        extra={"WA": ["wa.local.seattle.payroll_expense_tax", "wa.local.seattle.social_housing.rate", "sir.wa.local.seattle_pet"]},
        custom={"WA": sea_rows},
        matrix_fix={"WA": {
            5: f"Quarterly; due dates in row LOC-WA-008 ({tag('rspec.wa.local.seattle.sht.due')})",
            6: "online_form (FileLocal), paper",
            7: f"FileLocal portal or mail; Taxpayer Authorization per client for payroll providers. {FIELD_MODEL}.",
            9: accuracy("online_form, paper", f"FileLocal {url(BT)}", url(BT), "TO CONFIRM",
                        "85% (city pages read: 2026 thresholds, rates by tier and band, due dates and channel; no real filing)",
                        "a real filing or the provider's acceptance report for Seattle")}},
        skip={BT, "rspec.wa.local.seattle.sht.due",
              "rspec.wa.local.seattle.pet.prior_year_payroll_threshold", "rspec.wa.local.seattle.pet.employee_comp_threshold",
              "rspec.wa.local.seattle.pet.comp_level_2_floor", "rspec.wa.local.seattle.pet.tier_2_floor",
              "rspec.wa.local.seattle.pet.tier_3_floor", "rspec.wa.local.seattle.sht.rate",
              "rspec.wa.local.seattle.sht.excess_comp_threshold"})


# ============================================================ DOR-003 ===
def nv_mbt():
    D = "US-DOR-003"
    common = [
        R("MBT-C", 1, "payroll", "Gross wages as reported for UI", "UI gross wages", "Amounts", "Y", "Y", "Not conditional.",
          "Logical field (field model)", "Money", "Decimal 13.2", "180,000.00", "Payroll result: Nevada UI gross wages of the quarter",
          f"Base definition: {tagr('nv.mbt.base')}. {tag('rspec.nv.mbt.ui_match')}.", "Yes", "Not applicable", "Cents", "N", "Amount", "Quarterly"),
        R("MBT-C", 2, "payroll", "Employer-paid health benefits deducted", "Health benefits", "Amounts", "Y", "C",
          "Only when the employer pays health benefits.", "Logical field (field model)", "Money", "Decimal 13.2", "10,000.00",
          "Payroll result: employer health benefit cost", f"Deducted from the base: {tag('nv.mbt.base')}.", "Yes", "Not applicable",
          "Cents", "N", "Amount", "Quarterly"),
        R("MBT-C", 3, "payroll", "Taxable wages and tax due", "Tax due", "Amounts", "N", "Y", "Not conditional.",
          "Logical field (field model)", "Money", "Decimal 13.2", "See Example Analysis", "Calculated by the return generator",
          f"(Base minus {tag('nv.mbt.general.quarterly_threshold')} a quarter) x {tag('nv.mbt.general.rate')}% (general business); "
          f"financial institutions and mining {tag('nv.mbt.financial_mining.rate')}%.", "Yes", "Not applicable", "Cents", "N",
          "Calculated", "Quarterly"),
    ]
    at(f"{D} example")
    base = Decimal("180000") - Decimal("10000")
    thr = num("nv.mbt.general.quarterly_threshold")
    tax = money((base - thr) * pct("nv.mbt.general.rate"))
    ex = [("WORKED EXAMPLE: GENERAL BUSINESS MBT FOR ONE QUARTER (constructed)", [
        ("180,000.00", "UI gross wages (MBT-C-001)", "Constructed input", "Input"),
        ("10,000.00", "Employer-paid health benefits (MBT-C-002)", "Constructed input", "Input"),
        (m2(base), "Base", "180,000.00 - 10,000.00", "Calculation"),
        (m2(base - thr), "Taxable wages", f"{m2(base)} - {tag('nv.mbt.general.quarterly_threshold')}", "Calculation"),
        (m2(tax), "MBT due", f"{m2(base - thr)} x {tag('nv.mbt.general.rate')}%", "Half-up to the cent"),
    ])]
    return state_book(
        D, "NevadaMBT", "Nevada MBT Spec", "US-DOR-003 Nevada Modified Business Tax Return (Form TAX-F003, general business)",
        "Nevada Department of Taxation", "Modified Business Tax (employer payroll tax)", "Wages must match the Nevada UI report (US-UI-001)",
        "Quarterly", tag("nv.report.mbt.due"), "My Nevada Tax e-file or paper. " + FIELD_MODEL + ".", "Amounts; NV section",
        url("rspec.nv.mbt.form"), "Department of Taxation pages as read", "US-UI-001",
        "Nevada employers with UI wages above the quarterly exclusion.", ["NV"], "Modified Business Tax return", "Quarterly", common,
        scope([("Nevada employers liable for UI", "YES", tag("nv.mbt.base"))],
              [("Quarterly return, even with no tax", "YES", tag("rspec.nv.mbt.form"))],
              [("Quarterly exclusion and rate", "YES", f"{tag('nv.mbt.general.quarterly_threshold')}; {tag('nv.mbt.general.rate')}%")],
              SPECIAL_COMMON),
        [], [("CROSS-FIELD VALIDATIONS", [("Match", "MBT-C-001", "Nevada UI report",
                                           "The MBT wages equal the gross wages of the Nevada UI report of the same quarter; a mismatch "
                                           "creates a deficiency.", "Amended UI reports require an amended MBT return.")])],
        ex, [], extra={"NV": ["nv.mbt.general.rate", "nv.mbt.general.quarterly_threshold", "nv.mbt.base", "nv.report.mbt.due"]})


# ============================================================ DOR-004 ===
def transit():
    D = "US-DOR-004"
    common = [
        R("TRN-C", 1, "payroll", "Payroll subject to the transit levy", "Payroll", "Amounts", "Y", "Y", "Not conditional.",
          "Logical field (field model)", "Money", "Decimal 13.2", "100,000.00", "Payroll result: wages per transit district / zone",
          f"Oregon: wages for work in the district ({tag('dd.or.transit_district')}). New York: {tag('dd.employer.ny_mctmt_zone')}.",
          "Yes", "Not applicable", "Cents", "N", "Amount", "Quarterly"),
        R("TRN-C", 2, "payroll", "Employer transit tax due", "Tax due", "Amounts", "N", "Y", "Not conditional.",
          "Logical field (field model)", "Money", "Decimal 13.2", "See Example Analysis", "Calculated by the return generator",
          f"TriMet {tag('or.transit.trimet.employer.rate')}%, Lane Transit {tag('or.transit.lane.employer.rate')}% [US-ORS5-010]; "
          f"New York MCTMT: zone payroll x the rate of its payroll band (rate table in the NY section).", "Yes", "Not applicable",
          "Cents", "N", "Calculated", "Quarterly"),
    ]
    MK = "rspec.ny.mctmt"
    ceil = [num(f"{MK}.band.{i}.ceiling") for i in (1, 2, 3)]

    def band_of(x):
        return next((i for i, c in enumerate(ceil, start=1) if x <= c), 4)

    def mct_rows(pfx, n0):
        out = []
        at(f"{pfx}-{n0:03d}")
        out.append(R(pfx, n0, "system", "MCTMT quarterly payroll threshold", "Line 1c test", "Jurisdiction parameter: NY", "N", "Y",
                     "Not conditional: tested every quarter.", "Form line 1c", "Amount", "Whole dollars", "See Example Analysis",
                     "Jurisdiction configuration (system constant)",
                     f"New York: an employer whose total MCTD payroll expense of the quarter (MTA-305 line 1c) is not above "
                     f"{tagr(f'{MK}.quarterly_threshold')} is not subject for that quarter. {src(f'{MK}.quarterly_threshold')}",
                     "Yes: decides whether MTA-305 tax is due", "Value as stated in column M", "Whole units as published", "N",
                     "Amount", "Quarterly"))
        for z, (zn, line) in enumerate((("Zone 1", "2a"), ("Zone 2", "2b")), start=1):
            i = n0 + z
            at(f"{pfx}-{i:03d}")
            bands = (f"payroll up to {tag(f'{MK}.band.1.ceiling')}: {tag(f'{MK}.zone{z}.band.1.rate')}%; above "
                     f"{tag(f'{MK}.band.1.ceiling')} up to {tag(f'{MK}.band.2.ceiling')}: {tag(f'{MK}.zone{z}.band.2.rate')}%; above "
                     f"{tag(f'{MK}.band.2.ceiling')} up to {tag(f'{MK}.band.3.ceiling')}: {tag(f'{MK}.zone{z}.band.3.rate')}%; above "
                     f"{tag(f'{MK}.band.3.ceiling')}: {tag(f'{MK}.zone{z}.band.4.rate')}%")
            out.append(R(pfx, i, "system", f"MCTMT {zn} rate table (line {line})", f"{zn} rates", "Jurisdiction parameter: NY",
                         "N", "C", f"Only for payroll expense in {zn}; back-reference to TRN-C-001 and TRN-C-002.",
                         f"Form line {line}", "Rate", "Percent", "See Example Analysis",
                         f"{DD_REF}: MCTMT zone of the work location, forward reference; rate table per zone (system constant)",
                         f"New York MCTMT, {zn}, quarters from 2025-07-01: {bands} [{rid(f'{MK}.zone{z}.band.1.rate')}]. The rate of "
                         f"the band applies to the whole {zn} payroll of the quarter (no marginal split). Counties and the local "
                         f"government rule: row of the MTA-305 lines and rates. {src(f'{MK}.zone{z}.band.1.rate')}",
                         "Yes: computes MTA-305 line " + line, "Bands as stated in column M", "Rates as published", "N",
                         "Rate", "Quarterly",
                         f"Confirm against a real filing: the band is read from the {zn} payroll of the quarter [{rid(f'{MK}.rates_lines')}]."))
        return out
    at(f"{D} example")
    z1, z2 = Decimal("1000000.00"), Decimal("200000.00")
    b1, b2 = band_of(z1), band_of(z2)
    r1, r2 = pct(f"{MK}.zone1.band.{b1}.rate"), pct(f"{MK}.zone2.band.{b2}.rate")
    t1, t2 = money(z1 * r1), money(z2 * r2)
    ex_ny = ("WORKED EXAMPLE 2: NEW YORK MCTMT FOR ONE QUARTER (constructed)", [
        (m2(z1), "Zone 1 payroll expense (line 1a)", "Constructed input", "Input"),
        (m2(z2), "Zone 2 payroll expense (line 1b)", "Constructed input", "Input"),
        (m2(z1 + z2), "Total MCTD payroll expense (line 1c)", f"{m2(z1)} + {m2(z2)}; above {tag(f'{MK}.quarterly_threshold')}: subject",
         "Threshold test"),
        (m2(t1), "Zone 1 tax (line 2a)", f"{m2(z1)} is in band {b1}: {m2(z1)} x {tag(f'{MK}.zone1.band.{b1}.rate')}%",
         "Whole zone payroll at the band rate; half-up to the cent"),
        (m2(t2), "Zone 2 tax (line 2b)", f"{m2(z2)} is in band {b2}: {m2(z2)} x {tag(f'{MK}.zone2.band.{b2}.rate')}%",
         "Whole zone payroll at the band rate; half-up to the cent"),
        (m2(t1 + t2), "Total MCTMT (line 2c)", f"{m2(t1)} + {m2(t2)}", "Calculation"),
    ])
    ex = [("WORKED EXAMPLE: OREGON EMPLOYER TRANSIT TAXES ON 100,000.00 (constructed)", [
        (m2(money(Decimal("100000") * pct("or.transit.trimet.employer.rate"))), "TriMet", f"100,000.00 x {tag('or.transit.trimet.employer.rate')}%", "Half-up"),
        (m2(money(Decimal("100000") * pct("or.transit.lane.employer.rate"))), "Lane Transit", f"100,000.00 x {tag('or.transit.lane.employer.rate')}%", "Half-up"),
    ]), ex_ny]
    return state_book(
        D, "PayrollTransitLevies", "Transit Levy Spec", "US-DOR-004 Employer Payroll Transit Levies (Oregon, New York)",
        "Oregon Department of Revenue; New York State Department of Taxation and Finance", "Employer payroll transit taxes",
        "Oregon levies are carried on Form OQ (US-DOR-001 OR section)", "Quarterly", "Per levy (Report Matrix)",
        "Per levy channel: Oregon on Form OQ; New York MCTMT on Form MTA-305. " + FIELD_MODEL + ".", "Amounts; OR and NY sections",
        f"{url('rspec.or.oq.form')}; {url('rspec.ny.mctmt.form')}", "Pages as read for this release", "US-DOR-001",
        "Employer-borne payroll transit levies.", ["NY", "OR"], "employer payroll transit levy", "Quarterly", common,
        scope([("Employers with payroll in a transit district or MCTMT zone", "YES", "Sections.")],
              [("Oregon on the combined Form OQ", "YES", tag("rspec.or.oq.form")), ("New York MTA-305", "YES", tag("rspec.ny.mctmt.form"))],
              [("Employer-borne rates", "YES", "TRN-C-002."),
               ("Oregon statewide transit tax (employee)", "NO", f"Withheld from employees, on Form OQ (US-DOR-001): {tag('or.stt.employee.rate')}%.")],
              SPECIAL_COMMON),
        [], [("PAYROLL-SPECIFIC POPULATION RULES", [
            ("Conditional", "TRN-NY MCTMT zone rate tables", "Work location zone; payroll expense per zone",
             "Each quarter, total the payroll expense per MCTMT zone from the work location of each employee; if the total of "
             "both zones is not above the quarterly threshold no MCTMT is due for the quarter, otherwise each zone's payroll is "
             "taxed at the rate of its band.", "Local government employers follow the special rule of the MTA-305 instructions "
             "(row of the MTA-305 lines and rates).")])],
        ex, [("NEW YORK FORM MTA-305", [f"{tag(MK + '.rates_lines')} [{rid(MK + '.rates_lines')}]"])],
        extra={"OR": ["rspec.or.oq.form", "rspec.or.oq.due", "or.transit.trimet.employer.rate", "or.transit.lane.employer.rate"],
               "NY": ["dd.employer.ny_mctmt_zone"]},
        custom={"NY": mct_rows},
        matrix_fix={"NY": {
            5: f"Quarterly; due dates in row DOR-NY-002 ({tag('rspec.ny.mctmt.form')})",
            6: "online_form (NY DTF Web File)",
            7: f"Form MTA-305 through NY DTF Web File. {FIELD_MODEL}.",
            9: accuracy("online_form", f"NY DTF Web File {url(MK + '.rates_lines')}", url(MK + '.rates_lines'), "TO CONFIRM",
                        "85% (MTA-305 instructions read: lines, rates by zone and band, threshold, due dates; form PDF not held)",
                        "the MTA-305 form itself and a real filing or the provider's acceptance report")}},
        skip={f"{MK}.quarterly_threshold"} | {f"{MK}.zone{z}.band.{b}.rate" for z in (1, 2) for b in (1, 2, 3, 4)}
             | {f"{MK}.band.{b}.ceiling" for b in (1, 2, 3)})


# ============================================================= WC-001 ===
def workers_comp():
    D = "US-WC-001"
    common = [
        R("WC-C", 1, "payroll", "Hours worked or employees covered in the period", "Hours / employees", "Amounts", "Y", "Y",
          "Not conditional.", "Logical field (field model)", "Count", "N", "520", "Payroll result: hours per risk class / covered employees",
          f"Washington premiums are per hour by risk class ({tag('wa.wc.employee_deduction.rule')}); the Oregon Workers' Benefit Fund "
          f"is {tag('or.wbf.rate.per_hour')} USD per hour; the New Mexico fee is per employee per quarter.", "Yes", "Not applicable",
          "Whole hours", "N", "Count", "Quarterly"),
        R("WC-C", 2, "payroll", "Employee share deducted", "Employee share", "Amounts", "Y", "Y", "Not conditional.",
          "Logical field (field model)", "Money", "Decimal 13.2", "See Example Analysis", "Payroll result: WC employee deduction",
          f"New Mexico employee part {tag('nm.wc.admin_fee.employee.quarterly')} USD a quarter; Washington employee half of the "
          f"hourly premiums; Oregon half of the WBF (CCG annexes).", "Yes", "Not applicable", "Cents", "N", "Amount", "Quarterly"),
        R("WC-C", 3, "payroll", "Employer share", "Employer share", "Amounts", "N", "Y", "Not conditional.",
          "Logical field (field model)", "Money", "Decimal 13.2", "See Example Analysis", "Calculated by the return generator",
          f"New Mexico employer part {tag('nm.wc.admin_fee.employer.quarterly')} USD a quarter; Wyoming monopolistic State fund premiums "
          f"({tag('rspec.wy.wc_report.frequency')}).", "Yes", "Not applicable", "Cents", "N", "Calculated", "Quarterly"),
    ]
    at(f"{D} example")
    nmt = num("nm.wc.admin_fee.employee.quarterly") + num("nm.wc.admin_fee.employer.quarterly")
    wbf = num("or.wbf.rate.per_hour")
    ex = [("WORKED EXAMPLE: STATE-FUND AMOUNTS FOR ONE EMPLOYEE AND QUARTER (constructed)", [
        (m2(nmt), "New Mexico fee", f"{tag('nm.wc.admin_fee.employee.quarterly')} + {tag('nm.wc.admin_fee.employer.quarterly')}", "Per employee per quarter"),
        ("520", "Oregon hours worked", "Constructed input", "Input"),
        (m2(money(Decimal(520) * wbf)), "Oregon WBF", f"520 x {tag('or.wbf.rate.per_hour')}", "Split half employee / half employer"),
    ])]
    return state_book(
        D, "StateFundWorkersComp", "State Fund WC Spec",
        "US-WC-001 State-Fund Workers' Compensation Premiums and Fees Collected through Payroll (WA, NM, OR, WY)",
        "WA Department of Labor & Industries; NM Taxation and Revenue Department; OR Department of Revenue; WY Department of Workforce Services",
        "Workers' compensation premiums and fees", "NM fee on TRD-41431 and OR WBF on Form OQ (US-DOR-001); WY joint UI / WC report (US-UI-001)",
        "Quarterly (WY monthly, quarterly by permission)", "Per State (Report Matrix)", "Per State channel (Report Matrix). " + FIELD_MODEL + ".",
        "Amounts; State sections", "State pages cited per row", "Pages as read for this release", "US-DOR-001; US-UI-001",
        "Workers' compensation amounts collected through payroll for State funds; private insurer premiums are outside payroll.",
        ["NM", "OR", "WA", "WY"], "State-fund workers' compensation report", "Quarterly", common,
        scope([("Employees covered by a State fund collected through payroll", "YES", "State sections."),
               ("Private insurer premiums in other States", "NO", "Outside payroll (MANDATE workers' compensation row).")],
              [("Quarterly or monthly reports", "YES", tag("rspec.wy.wc_report.frequency"))],
              [("Employee shares deducted", "YES", "WC-C-002.")], SPECIAL_COMMON),
        [], [], ex, [],
        extra={"NM": ["rspec.nm.wh_qtr_report.form", "nm.wc.admin_fee.employer.quarterly", "nm.wc.admin_fee.employee.quarterly"],
               "OR": ["rspec.or.oq.form", "or.wbf.rate.per_hour"], "WA": ["wa.wc.employee_deduction.rule", "wa.wc.supplemental_pension.rate"]},
        gaps={"WA": "rspec.wa.lni_wc_qtr.report"})


# =========================================================== SDNH-001 ===
def new_hire():
    D = "US-SDNH-001"
    at(f"{D} common")
    common = [
        R("NH-C", 1, "payroll", "Federal new-hire data elements", "Federal elements", "Per new hire", "Y", "Y", "Not conditional.",
          "Logical field (field model)", "7 elements", "Per State channel", "Name, address, SSN, hire date; employer name, address, FEIN",
          f"{DD_REF}: employee name, home address, SSN, date services first performed; employer name, address, FEIN",
          f"{tagr('rspec.fed.new_hire.fields')}. Form: {tag('fed.newhire.form')}. Date of hire: {tag('dd.fed.new_hire.date_first_services')}.",
          "Yes", "Not applicable", "Not applicable", "N", "Text", "Per event"),
        R("NH-C", 2, "system", "Federal deadline and electronic interval", "Deadline", "Timing", "N", "Y", "Not conditional.",
          "Not applicable", "Not applicable", "Date rule", "Hire 2026-03-02: federal deadline 2026-03-22",
          "Filing calendar (system constant)",
          f"Within {tagr('fed.newhire.deadline_days')} days, or shorter State period (State sections). Electronic filers: "
          f"{tag('rspec.fed.new_hire.electronic_interval')}.", "Yes", "Not applicable", "Not applicable", "N", "Rule", "Per event"),
        R("NH-C", 3, "system", "Multistate designation", "Designated State", "Routing", "N", "C",
          "Only for an employer with employees in several States that reports electronically and has notified HHS.",
          "Not applicable", "Not applicable", "Code", "One designated State", f"{DD_REF}: designated new-hire State (forward reference)",
          f"{tagr('rspec.fed.new_hire.multistate_designation')}.", "Yes", "USPS State codes", "Not applicable", "N", "Code", "Per event"),
        R("NH-C", 4, "payroll", "Date of birth and other State elements", "State elements", "Per new hire", "Y", "C",
          "Only in States that add elements (State sections).", "Logical field (field model)", "Per State", "Per State",
          "1990-05-14", f"{DD_REF}: date of birth and State-specific new-hire fields (forward reference)",
          f"{tag('dd.state.new_hire.dob')}. Rehire rule: {tag('dd.state.new_hire.rehire_gap_days')} days separated in the States that set it.",
          "Yes", "Per State", "Not applicable", "N", "Date", "Per event"),
        R("NH-C", 5, "excluded", "Penalty cap (federal limit on State penalties)", "Penalty cap", "Information", "N", "N",
          "Informational.", "Not applicable", "Not applicable", "Amount", "No value transmitted", "Not mapped",
          f"{tagr('rspec.fed.new_hire.state_penalty_cap')}.", "No", "Not applicable", "Not applicable", "N", "Amount", "Per event"),
    ]
    gaps = {"CO": "rspec.co.new_hire.state_specifics", "PA": "rspec.pa.new_hire.portal", "RI": "rspec.ri.new_hire.statutory_fields",
            "MI": "rspec.mi.new_hire.statute"}
    at(f"{D} example")
    hire = dt.date(2026, 3, 2)

    def plus_business(d, n):
        while n:
            d += dt.timedelta(days=1)
            if d.weekday() < 5:
                n -= 1
        return d
    al = int(num("al.newhire.report_days"))
    fd = int(num("fed.newhire.deadline_days"))
    ex = [("WORKED EXAMPLE: DEADLINES FOR A HIRE ON 2026-03-02 (constructed)", [
        ("2026-03-02", "Date services first performed", "Constructed input", "Input"),
        (str(hire + dt.timedelta(days=fd)), "Federal deadline", f"2026-03-02 + {tag('fed.newhire.deadline_days')} days",
         "Calendar days; weekend roll-forward per State practice"),
        (str(hire + dt.timedelta(days=al)), "Alabama deadline", f"2026-03-02 + {tag('al.newhire.report_days')} days", "Shorter State period"),
        (str(plus_business(hire, 20)), "Kansas deadline", f"20 business days after 2026-03-02: {tag('rspec.ks.new_hire.deadline')}",
         "Weekends skipped; Kansas holidays not applied in this example"),
    ])]
    return state_book(
        D, "NewHireReport", "New Hire Report Spec", "US-SDNH-001 New-Hire Report (State Directories of New Hires)",
        "State Directories of New Hires (one per State; HHS designation for multistate employers)", "Child-support new-hire reporting",
        "Uses employee master data; no amounts", "Event-driven", "Federal maximum or the shorter State period (State sections)",
        f"W-4 copy or an equivalent form; electronic filers two monthly transmissions. {FIELD_MODEL} for the common rows.",
        "Per new hire; State sections", f"{url('rspec.fed.new_hire.fields')} [{rid('rspec.fed.new_hire.fields')}]",
        "Federal and State new-hire pages as read for this release", "None",
        "Every new hire and rehire is reported to the State Directory of New Hires.", STATES, "new-hire report", "Per event", common,
        scope([("New hires and rehires", "YES", tag("rspec.fed.new_hire.fields")),
               ("Independent contractors (reported in some States, e.g. California DE 542)", "NO",
                f"Out of scope [US-OWN-008]: {tag('rspec.ca.contractor_report.form')}.")],
              [("Within the federal or shorter State period", "YES", tag("fed.newhire.deadline_days"))],
              [("No amounts except where a State asks for salary", "YES", "State sections.")], SPECIAL_COMMON),
        [], [("MANDATORY FIELD RULES", [
            ("Event", "NH-C-001", "Employee master data at hire",
             "Generate one report per hire or rehire from the master data entered at hire; the hire date is the first day services are "
             "performed for wages.", "A rehire is reported when the State's separation gap is met.")])],
        ex, [], gaps=gaps)
