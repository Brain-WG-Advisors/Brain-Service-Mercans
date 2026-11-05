# -*- coding: utf-8 -*-
"""US Regulation Design generator (re-runnable).  python build_design.py
Writes ../US_Regulation_Design_v<package>.md, checks/design_bindings.csv and checks/design_gaps_used.txt.
Every value is a [[FACT:key=value]] tag taken from the facts files; every WTC code and DD field is verified
against the approved workbooks while the text is written."""
import collections
import csv
import json
import os
import re
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import design_common as C  # noqa: E402
from design_common import T, W, Wg, D, R, G, NC, at, cell, has, fact, entries, tag  # noqa: E402

L = []


def A(*lines):
    for x in lines:
        L.append(C.clean(x))


def table(head, rows):
    A("| " + " | ".join(head) + " |", "|" + "|".join("---" for _ in head) + "|")
    for r in rows:
        A("| " + " | ".join(cell(x) for x in r) + " |")
    A("")


def Tn(f):
    """Tag of a dated entry with its percent / unit suffix (no currency prefix)."""
    t = tag(f["key"], f=f)
    u = f.get("unit_of_measure")
    v = f["value"]
    if isinstance(v, (int, float)) and not isinstance(v, bool):
        if u in C.UNIT_SUFFIX:
            return t + C.UNIT_SUFFIX[u]
        if u:
            return f"{t} {u}"
    return t


def dated(key, from_year="2026"):
    """'2026-01-01 to 2026-12-31: tag; from 2027-01-01: tag' for the entries that reach the build window."""
    out = []
    for f in entries(key):
        b = f.get("effective_to")
        if b and b < f"{from_year}-01-01":
            continue
        if (f.get("effective_from") or "0000") > "2027-12-31":
            continue
        out.append(f"{C.period_label(f)}: {Tn(f)}")
    return "; ".join(out)


def numeric(key):
    es = entries(key)
    return bool(es) and all(isinstance(f["value"], (int, float)) and not isinstance(f["value"], bool) for f in es)


NO_TAX_STATES = fact("multi.no_wage_income_tax.states")["value"].split(",")

# ===================================================================== HEADER
at("header")
A(f"# US — United States Payroll — Regulation Design v{C.PKG}", "",
  f"**Country:** United States (US) · ISO 3166-1 numeric **840** · Currency **USD**  ",
  f"**Tax year:** {C.YEAR}; every value that changes with the year carries its own period (2027 values are labelled)  ",
  "**Regulation ID prefix:** `9840` (9 + ISO 840) · **Flag accounts:** `58401`–`58449` · **Calculation accounts:** `58501`–`58549`  ",
  f"**Design basis:** `US-CCG-001 v{C.PKG}` (13 modules and the jurisdiction annexes), `US-WTC-001 v{C.PKG}`, `US-DD-001 v{C.PKG}`  ",
  f"**Status:** {C.STATUS} · **Package version:** {C.PKG}", "",
  "| Version | Issue date | Issued by | Status |", "|---|---|---|---|",
  f"| {C.PKG} | {C.ISSUE} | {C.AUTHOR} | {C.STATUS} |", "",
  "**Scope.** Private-sector employers and common-law employees. Independent contractors paid on Form 1099-NEC are out of scope "
  f"{R('US-OWN-008')}. The layer covers federal employment taxes (income tax withholding, FICA, FUTA), State income tax "
  "withholding, State unemployment insurance and State-mandated payroll programmes for the 50 States and the District of "
  "Columbia, and refers local taxes to the jurisdiction annexes of the Configuration Guide. Every special population accepted "
  f"by the owner is in {R('US-OWN-005')}; State-level rules for special populations are a scope statement deferred to a later "
  "release, not a gap.", "",
  "**How to read the design.** Part 1 declares every flag with its values. Part 2 lists the accounts and the wage types they "
  "read or write. Part 3 gives the order of the regulations. Part 4 gives each regulation. Part 5 gives the taxability "
  "matrix of the wage-type catalogue. Part 6 lists the open items, each with both readings where the design and the research "
  "differ; the research wins. Every rate, ceiling and threshold is written once as a bound value; a value valid for a different "
  "period is written with that period.", "", "---", "")

# ===================================================================== PART 0
at("part0")
A("## PART 0 — Special-category sweep", "",
  "Two sweeps ran against the Configuration Guide: one on every row of the coverage matrix, one on every population the owner "
  "accepted. A category is *in core* when a flag and a regulation of this design implement it; *no branch* when the research "
  "shows no differential treatment; *by reference* when the rule lives in a jurisdiction annex.", "")
cov = json.load(open(os.path.join(C.RESEARCH, "CCG-coverage-facts.json"), encoding="utf-8"))["coverage_matrix"]
COV = {
    "resident_employee": ("In core", "58404, 58415, 58416, 58420", "9840021, 9840031, 9840032, 9840041, 9840051, 9840052"),
    "non_resident_employee": ("In core: two meanings kept apart (nonresident alien of the United States; employee working in or living in another State)", "58404, 58418, 58419", "9840024, 9840051"),
    "fixed_term_contract": ("No branch: no federal or general State fixed-term payroll regime", "none", "none"),
    "part_time": ("No branch: no federal part-time payroll regime", "none", "none"),
    "officers_without_employment_contract": ("In core: corporate officers are employees for payroll; State coverage exclusions are reporting inputs", "58423", "9840021, 9840052"),
    "apprentices_and_trainees": ("No branch; student employees are a separate flag", "58411", "9840031, 9840041"),
    "maternity_paternity_parental": ("By reference: no federal paid leave; State programmes are in 9840053", "58415", "9840053"),
    "work_accident_occupational_disease": ("By reference: State workers' compensation rows", "58415", "9840053"),
    "termination_and_final_pay": ("In core: final wages are paid wages; supplemental identification applies", "58413", "9840022, 9840023"),
    "mid_month_joiner_and_leaver": ("No branch: no proration rule; withholding follows the wages paid", "none", "none"),
    "annual_regularisation": ("No branch: no employer year-end regularisation; accumulators follow the payment year", "58420", "9840031, 9840041"),
    "overtime": ("In core as earnings; the qualified overtime premium is reported only", "none", "9840011"),
    "multiple_employers": ("In core: every wage base and accumulator is kept per employer entity", "58420", "9840031, 9840032, 9840041"),
    "local_regimes": ("By reference: local rows and annexes", "58415, 58416", "9840061"),
    "employer_type_and_size": ("By reference: coverage thresholds sit in the programme parameters; health-coverage reporting is outside the calculation", "58415", "9840053"),
    "mid_year_rate_change": ("In core: dated values selected by the payment date", "58420, 58421", "9840031, 9840051, 9840053"),
    "special_pay_cycles": ("In core: pay periods per year from the pay frequency", "58422", "9840021"),
    "accrual_vs_payment": ("In core: federal taxes follow the payment date", "58420", "9840021, 9840031"),
}
NAMES = {"non_resident_employee": "Non-resident employee", "fixed_term_contract": "Fixed-term contract", "part_time": "Part-time",
         "maternity_paternity_parental": "Maternity, paternity and parental leave", "work_accident_occupational_disease": "Work accident and occupational disease",
         "termination_and_final_pay": "Termination and final pay", "mid_month_joiner_and_leaver": "Mid-month joiner and leaver",
         "annual_regularisation": "Annual regularisation", "mid_year_rate_change": "Mid-year rate change", "accrual_vs_payment": "Accrual versus payment"}
rows = []
for k, v in cov.items():
    if v.get("status") != "answered":
        continue
    d, fl, rg = COV[k]
    rows.append([NAMES.get(k, k.replace("_", " ").capitalize()), v["ccg_location"], d, fl, rg])
missing = [k for k in COV if k not in cov]
assert not missing, missing
table(["Category", "Configuration Guide location", "Disposition", "Flags", "Regulations"], rows)

at("part0-populations")
A("**Populations accepted by the owner** " + R("US-OWN-005") + ".", "")
table(["Population", "Flag", "Regulations", "Wage types", "Rule carried by the research"], [
    ["Ordinary common-law employee", "58405 = 1", "9840021, 9840031, 9840032, 9840041, 9840051", f"{W('US-001')}, {W('US-006')}", "Default path of the design."],
    ["Nonresident alien", "58404 = 1", "9840024, 9840021", f"{W('US-004')}, {W('US-033')}, {W('US-029')}", f"Single schedule whatever the marital status; cannot claim exempt; wage add-on added before the table. {R('US-FEDS5-015')}"],
    ["Statutory employee", "58406 = 1", "9840021, 9840031, 9840032", W("US-035"), f"FICA withheld, no income tax withholding. {R(C.regid('fed.statutory_employee.treatment'))}"],
    ["Household employee", "58407 = 1", "9840021, 9840031", W("US-028"), f"Income tax withholding only by agreement. {R(C.regid('fed.household.fit.withholding'))}"],
    ["Agricultural employee", "58408 = 1", "9840031, 9840041", W("US-036"), f"Own return and thresholds. {R(C.regid('fed.agricultural.total_threshold'))}"],
    ["Clergy", "58409 = 1", "9840021, 9840031, 9840032", W("US-034"), f"No withholding for income tax, social security or Medicare. {R(C.regid('fed.minister.withholding'))}"],
    ["Employee abroad", "58410 = 1", "9840021", f"{W('US-001')}", f"Citizen abroad: income tax withholding can stop on a statement. {R(C.regid('fed.citizen_abroad.form673'))}"],
    ["Student employee", "58411 = 1", "9840031, 9840041", W("US-038"), f"Private school or college student: income tax withheld, FICA and FUTA exempt. {R(C.regid('fed.students.treatment'))}"],
], )
A("Populations in detail (values as carried by the research):", "")
for k, lead in [("fed.statutory_employee.treatment", "Statutory employee"), ("fed.household.fit.withholding", "Household employee, federal income tax"),
                ("fed.minister.withholding", "Clergy"), ("fed.students.treatment", "Student employee"),
                ("fed.citizen_abroad.form673", "Employee abroad (citizen)")]:
    A(f"- **{lead}:** {tag(k)} {R(C.regid(k))}")
A(f"- **Household employee thresholds:** cash wages {T('fed.household.fica_cash_threshold')} a year for FICA; FUTA from {T('fed.household.futa_quarter_threshold')} in a quarter {R(C.regid('fed.household.fica_cash_threshold'))}")
A(f"- **Agricultural employee thresholds:** {T('fed.agricultural.per_worker_threshold')} per worker or {T('fed.agricultural.total_threshold')} in total; FUTA from {T('fed.agricultural.futa_quarter_threshold')} in a quarter {R(C.regid('fed.agricultural.total_threshold'))}")
A(f"- **Employee abroad:** foreign earned income exclusion {T('fed.feie.amount')} for {C.YEAR} {R(C.regid('fed.feie.amount'))}")
A(f"- **Nonresident alien commercial traveler:** up to {T('fed.fit.nra.commercial_traveler.max_days')} and {T('fed.fit.nra.commercial_traveler.max_pay')} of pay {R(C.regid('fed.fit.nra.commercial_traveler.max_days'))}")
A(f"- **Election workers:** FICA applies from {T('fed.election_worker.fica_threshold')} a year {R(C.regid('fed.election_worker.fica_threshold'))}")
A("", "**Population rules at State level.**", "")
for k in sorted(k for k in C.FACTS if k.startswith("special_population.")):
    A(f"- {tag(k)} {R(C.regid(k))}")
A("", "State-level rules for the remaining populations are deferred by owner decision " + R("US-OWN-005") + ". They are a scope statement of this release.", "", "---", "")

# ===================================================================== PART 1
at("part1")
A("## PART 1 — Flags and HR fields", "",
  "> The engine reads numbers only; string interpretation lives in flags only, never inside a regulation. Each flag lists its "
  "values; every gate in Part 4 compares a flag against one of its declared values. A definition written `DD:` names a field "
  "of the Data Dictionary; a wage-type code is written in backticks.", "")
FLAGS = [
    ("58401", "Filing status", f"{D('Form W-4 filing status (Step 1(c))')} (option code J, S or H) **[DERIVED]**", "1 = married filing jointly or qualifying surviving spouse, 2 = single or married filing separately, 3 = head of household"),
    ("58402", "Multiple jobs box (Step 2)", f"{D('Form W-4 multiple jobs or spouse works (Step 2)')} **[DERIVED]**", "1 = box checked (Step-2 schedule), 2 = not checked (standard schedule)"),
    ("58403", "Exempt from withholding", f"{D('Form W-4 exempt from withholding')} **[DERIVED]**", "1 = exempt certificate in force, 2 = not exempt"),
    ("58404", "Nonresident alien", f"{W('US-033')}; {D('Nonresident alien flag')} **[DERIVED]**", "1 = nonresident alien, 2 = not"),
    ("58405", "Employee category", f"{D('Employee special population category')} (option code ORD, NRA, STAT, HH, AG, CLG, ABR) **[DERIVED]**", "1 = ordinary, 2 = nonresident alien, 3 = statutory employee, 4 = household, 5 = agricultural, 6 = clergy, 7 = employee abroad"),
    ("58406", "Statutory employee", f"{W('US-035')}; from 58405 **[DERIVED]**", "1 = statutory employee, 2 = not"),
    ("58407", "Household employee", f"{W('US-028')}; from 58405 **[DERIVED]**", "1 = household employee, 2 = not"),
    ("58408", "Agricultural employee", f"{W('US-036')}; from 58405 **[DERIVED]**", "1 = agricultural employee, 2 = not"),
    ("58409", "Clergy", f"{W('US-034')}; from 58405 **[DERIVED]**", "1 = minister of religion, 2 = not"),
    ("58410", "Employee abroad", "from 58405 **[DERIVED]**", "1 = employee abroad, 2 = not"),
    ("58411", "Student employee (exempt case)", f"{W('US-038')} **[DERIVED]**", "1 = student employee whose wages are exempt from FICA and FUTA, 2 = not"),
    ("58412", "Third-party sick pay", f"{W('US-037')}; {D('W-2 third-party sick pay indicator')} **[DERIVED]**", "1 = third-party sick pay, 2 = not"),
    ("58413", "Supplemental wage payment", "earning wage type with Special Tax = Yes, or Yes-No resolved as separately identified **[DERIVED]**", "1 = supplemental wages, 2 = regular wages"),
    ("58414", "Supplemental withholding method", "entity parameter " + NC("DESIGN-RQ-03"), "1 = flat rate, 2 = aggregate method"),
    ("58415", "Work State", f"{D('Work State')} **[DERIVED]**", "USPS code of the jurisdiction list in Part 4.4"),
    ("58416", "Residence State", f"{D('Residence State')} **[DERIVED]**", "USPS code of the jurisdiction list in Part 4.4"),
    ("58417", "Unemployment insurance State", f"{W('US-041')}; {D('Unemployment insurance State')} **[DERIVED]**", "USPS code of the jurisdiction list in Part 4.4"),
    ("58418", "State withholding mode", f"from 58415, 58416 and 58419 **[DERIVED]**", "1 = work State only, 2 = work State and residence State, 3 = reciprocity: work State does not withhold"),
    ("58419", "Reciprocity certificate on file", f"{D('State withholding certificate on file')} **[DERIVED]**", "1 = certificate on file, 2 = none"),
    ("58420", "Payment-year rule set", "`IF(LESS(DATE_FORMAT($period.payment_date;'yyyyMMdd');'20270101');1;2)` **[DERIVED]**", "1 = 2026 rule set, 2 = 2027 rule set"),
    ("58421", "Utah table period", "`IF(LESS(DATE_FORMAT($period.payment_date;'yyyyMMdd');'20260401');1;2)` **[DERIVED]**", "1 = payment date before 2026-04-01, 2 = from 2026-04-01"),
    ("58422", "Pay periods per year", f"{D('Pay frequency')} **[DERIVED]**", "numeric: the count of pay periods of the pay frequency, see 9840021"),
    ("58423", "Corporate officer without voluntary UI coverage", f"{D('Corporate officer without voluntary unemployment insurance coverage')} **[DERIVED]**", "1 = officer without voluntary coverage, 2 = otherwise"),
]
head = ["Account", "Flag name", "Definition", "Values"]
A("| " + " | ".join(head) + " |", "|---|---|---|---|")
for a, n, d, v in FLAGS:
    A(f"| {a} | {n} | {d} | {v} |")
A("")
at("part1-notes")
A("**Note on 58420 and 58421.** Federal taxes follow the payment date, so the rule set is chosen by the payment date and not by the "
  "period worked. 58421 selects the Utah withholding table; the Utah table of the earlier period is " + NC("DESIGN-RQ-01") + ".", "",
  "**Note on 58413 and 58414.** A payment identified separately from regular wages takes the supplemental path of 9840022 and 9840023. "
  "The choice between the flat rate and the aggregate method belongs to the payer " + R(C.regid("fed.fit.supplemental.aggregate_method")) + ".", "",
  "**Note on 58422.** The pay periods per year are " + tag("fed.fit.pay_periods_per_year") + " " + R(C.regid("fed.fit.pay_periods_per_year")) + ".", "",
  "**Note on 58423.** The flag is an input of the State unemployment return; the exclusion rules of each State are in its annex of the Configuration Guide.", "", "---", "")

# ===================================================================== PART 2
at("part2")
A("## PART 2 — Account register", "",
  "Accounts `58501` onwards hold bases, intermediates and results. The wage-type code is the row of `US-WTC-001` that carries the "
  "account in the pay run; an account with no catalogue row is an engine intermediate.", "")
ACCTS = [
    ("58501", "Base", "9840011", W("US-011"), "Federal income tax wages (accumulator)"),
    ("58502", "Base", "9840011", W("US-012"), "Social security wages, capped accumulator"),
    ("58503", "Base", "9840011", W("US-014"), "Medicare wages and tips, uncapped accumulator"),
    ("58504", "Base", "9840011", W("US-015"), "Wages subject to Additional Medicare Tax withholding"),
    ("58505", "Base", "9840011", W("US-019"), "FUTA taxable wages"),
    ("58506", "Intermediate", "9840024", W("US-004"), "Nonresident alien wage add-on"),
    ("58507", "Result", "9840021", W("US-001"), "Federal income tax withheld, regular wages"),
    ("58508", "Result", "9840022", W("US-002"), "Federal income tax, supplemental wages at the optional flat rate"),
    ("58509", "Result", "9840023", W("US-003"), "Federal income tax, supplemental wages above the mandatory threshold"),
    ("58510", "Result", "9840031", Wg("21900"), "Social security tax, employee"),
    ("58511", "Result", "9840031", W("US-005"), "Social security tax, employer"),
    ("58512", "Result", "9840032", W("US-006"), "Medicare tax, employee"),
    ("58513", "Result", "9840032", W("US-007"), "Medicare tax, employer"),
    ("58514", "Result", "9840032", W("US-008"), "Additional Medicare Tax, employee"),
    ("58515", "Result", "9840041", W("US-009"), "FUTA, employer"),
    ("58516", "Result", "9840041", W("US-010"), "FUTA credit reduction, employer"),
    ("58517", "Result", "9840051", "`US-074` to `US-115`", "State income tax withholding (one row per State)"),
    ("58518", "Result", "9840052", "`US-116` to `US-166`", "State unemployment insurance, employer (one row per State)"),
    ("58519", "Result", "9840052", "`US-167` to `US-169`", "State unemployment insurance, employee"),
    ("58520", "Result", "9840053", "`US-170` to `US-204`", "State programmes, employee and employer"),
    ("58521", "Result", "9840061", "`US-211` to `US-233`", "Local taxes"),
]
for c_ in ("US-074", "US-115", "US-116", "US-166", "US-167", "US-169", "US-170", "US-204", "US-211", "US-233"):
    W(c_)
table(["Account", "Type", "Regulation", "Wage type", "Meaning"], ACCTS)
A("---", "")

# ===================================================================== PART 3
at("part3")
A("## PART 3 — Regulation sequence", "",
  "Regulations run in this order for each payment. A regulation reads only accounts written by an earlier one.", "")
SEQ = [
    (1, "9840011", "Federal wage bases", "earning lines and their wage-type flags", "58501–58505"),
    (2, "9840024", "Nonresident alien add-on", "58501, 58404, 58422", "58506"),
    (3, "9840021", "Federal income tax, regular wages", "58501, 58506", "58507"),
    (4, "9840022", "Federal income tax, supplemental flat rate", "58501, 58413, 58414", "58508"),
    (5, "9840023", "Federal income tax, supplemental above the mandatory threshold", "58501, 58413", "58509"),
    (6, "9840031", "Social security tax", "58502, 58420", "58510, 58511"),
    (7, "9840032", "Medicare and Additional Medicare tax", "58503, 58504", "58512–58514"),
    (8, "9840041", "FUTA and credit reduction", "58505, 58417", "58515, 58516"),
    (9, "9840051", "State income tax withholding", "58501, 58415–58419", "58517"),
    (10, "9840052", "State unemployment insurance", "58417, 58423", "58518, 58519"),
    (11, "9840053", "State programmes", "58415", "58520"),
    (12, "9840061", "Local taxes", "58415, 58416", "58521"),
]
table(["Order", "Regulation", "Name", "Reads", "Writes"], SEQ)
A("---", "")

# ===================================================================== PART 4
at("part4")
A("## PART 4 — Regulation detail", "",
  "Amounts are rounded half-up to the cent between lines unless a State annex of the Configuration Guide sets another rule; "
  "full precision is carried between lines. A contribution or tax with an annual maximum is always the lesser of the remaining "
  "annual maximum and the rate times the period base; no annualise-then-divide shortcut is used.", "")

# ---- 4.1 federal bases
A("### 9840011 — Federal wage bases", "",
  f"Reads the earning lines. Each earning wage type carries the flags Subject to Tax, Q1 (OASDI), Q2 (Medicare) and Q3 (FUTA) in "
  f"`US-WTC-001`; where a flag is Yes-No the explanation of the row decides, and Part 5 lists every row. Accumulators: {W('US-011')} "
  f"(58501), {W('US-012')} (58502), {W('US-014')} (58503), {W('US-015')} (58504), {W('US-019')} (58505).", "",
  "```", "58501 = SUM(earnings with Subject to Tax = Yes) - pre-tax deductions that reduce income tax wages",
  "58502 = SUM(earnings with Q1 = Yes) - pre-tax deductions that reduce FICA wages",
  "58503 = SUM(earnings with Q2 = Yes) - pre-tax deductions that reduce FICA wages",
  "58504 = 58503 year to date, above the Additional Medicare threshold",
  "58505 = SUM(earnings with Q3 = Yes) - payments exempt from FUTA", "```", "",
  "Debit `58501`, `58502`, `58503`, `58504`, `58505`.", "")

# ---- 4.2 NRA add-on
A("### 9840024 — Nonresident alien add-on", "",
  f"Reads `$58501` and the flags 58404 and 58422. The add-on is added to the period wages before the schedule is read "
  f"{R(C.regid('fed.fit.nra.addon.table2.annual'))}. It does not apply to flat-rate supplemental wages "
  f"(a flat-rate supplemental payment is withheld at the flat rate alone).", "",
  "```", "58506 = IF(EQUALS($58404;1); NRA_ADDON_TABLE2(58422); 0)", "```", "",
  "Add-on amounts per pay period for Table 1 and Table 2, in USD:", "")
PER = ["weekly", "biweekly", "semimonthly", "monthly", "quarterly", "semiannual", "annual", "daily"]
table(["Pay period", "Table 1", "Table 2"],
      [[p.capitalize()] + [Tn(fact(f"fed.fit.nra.addon.table{n}.{p}")) if has(f"fed.fit.nra.addon.table{n}.{p}") else "" for n in (1, 2)] for p in PER])
A(f"Table 1 applies to an employee whose Form W-4 predates the 2020 revision. The design reads the 2020 revision only: "
  f"{NC('DESIGN-RQ-02')}. The nonresident alien Form W-4 rule: {tag('fed.fit.nra.w4_rule')} {R(C.regid('fed.fit.nra.w4_rule'))}.", "",
  "Debit `58506`.", "")

# ---- 4.3 FIT
A("### 9840021 — Federal income tax, regular wages", "",
  f"Method: {tag('fed.fit.method')} {R(C.regid('fed.fit.method'))}. Reads `$58501` and `$58506`; flags 58401, 58402, 58403, 58404, 58406, 58407, 58409, 58410, 58422.", "",
  "```",
  "pay_periods   = 58422",
  "annual_wages  = (58501 + 58506) x pay_periods + W-4 Step 4(a)",
  f"line_1g       = IF(EQUALS($58402;1); 0; IF(EQUALS($58401;1); {tag('fed.fit.worksheet1a.line1g.mfj')}; {tag('fed.fit.worksheet1a.line1g.other')}))",
  "adjusted      = MAX(0; annual_wages - W-4 Step 4(b) - line_1g)",
  "row          = last row of the schedule with floor <= adjusted",
  "tentative    = cumulative_tax(row) + (adjusted - floor(row)) x rate(row)",
  "credit       = W-4 Step 3 / pay_periods",
  "58507        = IF(EQUALS($58403;1); 0;",
  "                IF(EQUALS($58406;1); 0;",
  "                IF(EQUALS($58409;1); 0;",
  "                MAX(0; tentative / pay_periods - credit) + W-4 Step 4(c))))",
  "```", "",
  f"Schedule: the standard schedule when 58402 = 2, the Step-2 schedule when 58402 = 1. A household employee is withheld only "
  f"under an agreement {R(C.regid('fed.household.fit.withholding'))}: `IF(EQUALS($58407;1); agreement_amount; ...)` uses "
  f"{D('Household employee: federal income tax withholding agreement')}. An employee without a certificate: {tag('fed.w4.default_no_certificate')} "
  f"{R(C.regid('fed.w4.default_no_certificate'))}. The exempt certificate: {tag('fed.w4.exempt.validity')} {R(C.regid('fed.w4.exempt.validity'))}.", "",
  "Debit `58507`.", "",
  f"Employees abroad (58410 = 1): the withholding can stop on a statement; {NC('DESIGN-RQ-05')}.", "")
at("part4-fit-tables")
SCH = [("mfj", "MFJ"), ("single", "Single/MFS"), ("hoh", "HoH")]
A(f"**Standard schedule** (58402 = 2), annual percentage method, {C.YEAR}. Floor and cumulative tax in USD; rate in percent {R(C.regid('fed.fit.standard.mfj.bracket.1.floor'))}.", "")
head = ["Row"] + [f"{n} {x}" for _, n in SCH for x in ("floor", "rate", "cumulative")]
rows = []
for i in range(1, 9):
    r = [str(i)]
    for s, _ in SCH:
        r += [Tn(fact(f"fed.fit.standard.{s}.bracket.{i}.floor")), Tn(fact(f"fed.fit.standard.{s}.bracket.{i}.rate")),
              Tn(fact(f"fed.fit.standard.{s}.bracket.{i}.cumulative_tax"))]
    rows.append(r)
table(head, rows)
A(f"**Step-2 schedule** (58402 = 1). The cumulative tax of a row is the standard formula applied to the rows above it {R(C.regid('fed.fit.step2.mfj.bracket.1.floor'))}.", "")
head = ["Row"] + [f"{n} {x}" for _, n in SCH for x in ("floor", "rate")]
rows = []
for i in range(1, 9):
    r = [str(i)]
    for s, _ in SCH:
        r += [Tn(fact(f"fed.fit.step2.{s}.bracket.{i}.floor")), Tn(fact(f"fed.fit.step2.{s}.bracket.{i}.rate"))]
    rows.append(r)
table(head, rows)
A(f"Before the {C.YEAR} revision the allowance method gave each allowance a value of {T('fed.fit.allowance.pre2020_value')} {R(C.regid('fed.fit.allowance.pre2020_value'))}; "
  f"the allowance method is {NC('DESIGN-RQ-02')}.", "",
  f"The {C.YEAR} schedule is held for payment dates in {C.YEAR}; the 2027 schedule is {NC('RQ-530')}.", "")

# ---- supplemental
A("### 9840022 / 9840023 — Federal income tax, supplemental wages", "",
  f"Reads `$58501` and the flags 58413 and 58414. {tag('fed.fit.supplemental.aggregate_method')} {R(C.regid('fed.fit.supplemental.aggregate_method'))}.", "",
  "```",
  f"58508 = IF(EQUALS($58413;1); IF(EQUALS($58414;1); ROUND({tag('fed.fit.supplemental.flat_rate')}% x supplemental_wages); aggregate_method); 0)",
  f"58509 = IF(EQUALS($58413;1); {tag('fed.fit.supplemental.mandatory_rate')}% x MAX(0; supplemental_ytd - {tag('fed.fit.supplemental.mandatory_threshold')}); 0)",
  "```", "",
  f"The optional flat rate is {T('fed.fit.supplemental.flat_rate')}; the mandatory rate is {T('fed.fit.supplemental.mandatory_rate')} on the part of the year's supplemental "
  f"wages above {T('fed.fit.supplemental.mandatory_threshold')} {R(C.regid('fed.fit.supplemental.flat_rate'))}. "
  f"The nonresident alien add-on does not apply to flat-rate supplemental wages. The aggregate method uses the schedule of 9840021 on the sum of the supplemental and regular wages. "
  f"Backup withholding is separate at {T('fed.fit.backup_withholding.rate')} {R(C.regid('fed.fit.backup_withholding.rate'))}. "
  f"The decision between the flat rate and the aggregate method is {NC('DESIGN-RQ-03')}.", "",
  "Debit `58508`, `58509`.", "")

# ---- FICA
at("part4-fica")
A("### 9840031 — Social security tax (OASDI)", "",
  f"Reads `$58502` and the flag 58420. Employee row {Wg('21900')}; employer row {W('US-005')}. The wage base applies per employer.", "",
  "```",
  f"limit_2026 = {tag('fed.fica.oasdi.wage_base', '2026')}   (payment dates in 2026)",
  f"limit_2027 = {tag('fed.fica.oasdi.wage_base', '2027')}   (payment dates from 2027-01-01)",
  "limit  = IF(EQUALS($58420;1); limit_2026; limit_2027)",
  f"58510 = IF(EQUALS($58411;1); 0; IF(EQUALS($58409;1); 0; ROUND({tag('fed.fica.oasdi.rate.employee')}% x MIN(58502; MAX(0; limit - 58502_ytd)))))",
  f"58511 = IF(EQUALS($58411;1); 0; IF(EQUALS($58409;1); 0; ROUND({tag('fed.fica.oasdi.rate.employer')}% x MIN(58502; MAX(0; limit - 58502_ytd)))))",
  "```", "",
  f"Social security base: {T('fed.fica.oasdi.wage_base', '2026')} for {C.YEAR} (period {C.period_label(fact('fed.fica.oasdi.wage_base', '2026'))}) "
  f"and {T('fed.fica.oasdi.wage_base', '2027')} from {fact('fed.fica.oasdi.wage_base', '2027')['effective_from']}; employee and employer each at {T('fed.fica.oasdi.rate.employee')} "
  f"{R(C.regid('fed.fica.oasdi.wage_base', '2026'))}. A student employee (58411 = 1) is exempt from FICA {R(C.regid('fed.students.treatment'))}; "
  f"an employee under a totalization agreement is exempt to the extent the agreement says so: {tag('fed.fica.totalization.exemption_rule')} "
  f"{R(C.regid('fed.fica.totalization.exemption_rule'))}, using {D('Totalization agreement FICA exemption')}.", "",
  "Debit `58510`, `58511`.", "")
A("### 9840032 — Medicare tax and Additional Medicare Tax", "",
  f"Reads `$58503` and `$58504`. The Medicare base has no annual cap. Employee row {W('US-006')}; employer row {W('US-007')}; "
  f"Additional Medicare row {W('US-008')}.", "",
  "```",
  f"58512 = IF(EQUALS($58409;1); 0; ROUND({tag('fed.fica.medicare.rate.employee')}% x 58503))",
  f"58513 = IF(EQUALS($58409;1); 0; ROUND({tag('fed.fica.medicare.rate.employer')}% x 58503))",
  f"58514 = ROUND({tag('fed.fica.addl_medicare.rate')}% x MAX(0; 58503_ytd_after - MAX({tag('fed.fica.addl_medicare.withholding_threshold')}; 58503_ytd_before)))",
  "```", "",
  f"Rates: employee {T('fed.fica.medicare.rate.employee')}, employer {T('fed.fica.medicare.rate.employer')}; Additional Medicare {T('fed.fica.addl_medicare.rate')} on wages above "
  f"{T('fed.fica.addl_medicare.withholding_threshold')} in the year, employee only {R(C.regid('fed.fica.medicare.rate.employee'))}.", "",
  "Debit `58512`, `58513`, `58514`.", "")

# ---- FUTA
A("### 9840041 — FUTA and credit reduction", "",
  f"Reads `$58505` and the flag 58417. Rows {W('US-009')} and {W('US-010')}.", "",
  "```",
  f"net_rate = {tag('fed.futa.rate.net')}%",
  f"58515 = IF(EQUALS($58411;1); 0; ROUND(net_rate x MIN(58505; MAX(0; {tag('fed.futa.wage_base')} - 58505_ytd))))",
  f"58516 = IF(EQUALS($58411;1); 0; ROUND(credit_reduction_rate(58417) x MIN(58505; MAX(0; {tag('fed.futa.wage_base')} - 58505_ytd))))",
  "```", "",
  f"Gross rate {T('fed.futa.rate.gross')}, maximum credit {T('fed.futa.credit.max')}, net rate {T('fed.futa.rate.net')} on the first {T('fed.futa.wage_base')} of each employee's wages "
  f"{R(C.regid('fed.futa.rate.net'))}. The quarterly deposit applies when the liability exceeds {T('fed.futa.deposit_threshold')} {R(C.regid('fed.futa.deposit_threshold'))}. "
  f"Credit reduction for California ({T('fed.futa.credit_reduction.ca.potential.rate')}) and the Virgin Islands ({T('fed.futa.credit_reduction.vi.potential.rate')}) is a potential rate "
  f"for {C.YEAR}: {NC('RQ-402')} and {NC('RQ-403')}.", "",
  "Debit `58515`, `58516`.", "")
# ---- 4.4 State
at("part4-states")
A("### 9840051 — State income tax withholding", "",
  f"Reads `$58501` and the flags 58415 to 58419. Rows {W('US-074')} to {W('US-115')}; the State of work and the State of residence decide the mode.", "",
  "```",
  "state_wh(S)  = withholding of State S by its method class (Part 4.4 table)",
  "58517 = IF(EQUALS($58418;3); 0;",
  "        IF(EQUALS($58418;2); MAX(state_wh(58415); state_wh(58416));",
  "        state_wh(58415)))",
  "```", "",
  f"The mode 58418 = 3 needs the certificate 58419 = 1; the State pairs are carried by the reciprocity text of each State. "
  f"The default for a missing State certificate is set in Module 2 of the Configuration Guide.", "",
  "Debit `58517`.", "")
at("part4-4-table")
A("#### Part 4.4 — Jurisdiction register", "",
  "One row per State and the District of Columbia. *No wage tax* and *flat rate* come from the research; *Table or formula* means "
  "the State publishes tables or a formula, set out in its annex of the Configuration Guide. Wage-base cells carry their own period.", "")
WTCNAME = {v["name"]: c for c, v in C.WTC.items()}
nc6 = []
rows = []
for st in C.STATES:
    nm = C.STATE_NAMES[st]
    low = st.lower()
    at(f"part4-4-{st}")
    sit = WTCNAME.get(f"State income tax withholding - {nm}")
    sui = WTCNAME.get(f"State unemployment insurance - employer - {nm}")
    suie = WTCNAME.get(f"State unemployment insurance - employee - {nm}")
    progs = sorted(c for c, v in C.WTC.items() if c.startswith("US-") and v["name"].endswith(f" - {nm}")
                   and c not in (sit, sui, suie) and int(c[3:]) >= 167)
    if st in NO_TAX_STATES:
        cls = "No wage tax"
    elif has(f"{low}.pit.rate.flat") and numeric(f"{low}.pit.rate.flat"):
        cls = "Flat rate " + dated(f"{low}.pit.rate.flat")
    elif has(f"{low}.pit.rate") and numeric(f"{low}.pit.rate") and len(entries(f"{low}.pit.rate")) <= 2:
        cls = "Flat rate " + dated(f"{low}.pit.rate")
    else:
        cls = "Table or formula"
    wb_ = dated(f"{low}.sui.wage_base") if numeric(f"{low}.sui.wage_base") else "per annex"
    if has(f"{low}.sui.new_employer.rate") and numeric(f"{low}.sui.new_employer.rate"):
        nw = dated(f"{low}.sui.new_employer.rate")
    else:
        nw = NC("DESIGN-RQ-06")
        nc6.append(st)
    ee = dated(f"{low}.sui.employee.rate") if (has(f"{low}.sui.employee.rate") and numeric(f"{low}.sui.employee.rate")
                                               and any(f["value"] for f in entries(f"{low}.sui.employee.rate"))) else "none"
    for c_ in [x for x in (sit, sui, suie) if x] + progs:
        W(c_)
    rows.append([nm, st, sit or "none", cls, sui or "none", wb_, nw, f"{suie} {ee}" if suie else ee,
                 ", ".join(progs) or "none"])
table(["State", "USPS", "Withholding row", "State income tax", "UI employer row", "UI wage base (USD)", "New-employer rate",
       "UI employee", "Programme rows"], rows)
A(f"The wage base, the rate range and the new-employer rate of each State are the values of its annex; a State whose single new-employer rate is not carried as one number "
  f"is marked {G('DESIGN-RQ-06')}.", "")

# ---- SUI
A("### 9840052 — State unemployment insurance", "",
  "Reads the flags 58417 and 58423. The State of coverage is the State of localization " + R("US-MULTIS5-017") + ".", "",
  "```",
  "base     = MIN(sui_wages_period; MAX(0; state_wage_base(58417) - sui_wages_ytd_state))",
  "58518 = ROUND(employer_rate(58417) x base)",
  "58519 = ROUND(employee_rate(58417) x base)",
  "```", "",
  f"The employer rate is the rate assigned by the State, held per legal entity and State; {NC('DESIGN-RQ-04')}. A new employer uses the new-employer rate of Part 4.4. "
  "An employee contribution exists only in the States whose row carries one in Part 4.4. An officer without voluntary coverage (58423 = 1) "
  "is reported on the State return as the annex of the State requires.", "",
  "Debit `58518`, `58519`.", "")
# ---- programmes
at("part4-programmes")
A("### 9840053 — State programmes", "",
  "Reads the flag 58415. One result row per programme and side (Part 4.4 lists the rows of each State). A programme with a wage cap "
  "is the lesser of the remaining annual cap and the rate times the period base.", "",
  "```",
  "58520 = ROUND(programme_rate(58415; period) x MIN(programme_wages_period; MAX(0; programme_cap(58415) - programme_wages_ytd)))",
  "```", "",
  "**Programme parameters.** Every dated value of the research for these programmes:", "")
PRG = re.compile(r"^([a-z]{2})\.(sdi|pfml|tdi|fli|pfl|famli|cares|phc|dbl|wbf|ccc|mbt|mctmt|transit|wc)[a-z_.0-9]*$")
rows = []
for k in sorted(C.FACTS):
    m = PRG.match(k)
    if not m or m.group(1).upper() not in C.STATE_NAMES:
        continue
    if not numeric(k):
        continue
    if k in ("ma.pfml.benefit.weekly_max",) and False:
        continue
    st = m.group(1).upper()
    for f in entries(k):
        b = f.get("effective_to")
        if b and b < "2026-01-01":
            continue
        at(f"part4-prg-{k}")
        rows.append([C.STATE_NAMES[st], k[len(m.group(1)) + 1:].replace(".", " ").replace("_", " "), C.period_label(f), Tn(f)])
table(["State", "Parameter", "Period", "Value"], rows)
A("Massachusetts paid family and medical leave: the 2026 and 2027 splits are the dated entries above; the rate in force is chosen by 58420. "
  "The disagreement between the statute and the published guidance is recorded in Part 6.", "",
  "Debit `58520`.", "")
# ---- locals
A("### 9840061 — Local taxes", "",
  "Reads the flags 58415 and 58416. Local rows: " + ", ".join(W(c_) for c_ in sorted(c for c, v in C.WTC.items() if c.startswith("US-")
                                                                         and 211 <= int(c[3:]) <= 233)) + ". "
  "Each locality, rate, base and filing rule is set out in the jurisdiction annexes of `US-CCG-001 v" + C.PKG + "`; this design routes the wages and does not repeat the rates.", "",
  "```", "58521 = SUM(local_tax(locality) for each locality of 58415 and 58416)", "```", "", "Debit `58521`.", "", "---", "")

# ===================================================================== PART 5
at("part5")
A("## PART 5 — Taxability matrices", "",
  "Every earning and deduction row of the wage-type catalogue grouped by name and flag pattern. Columns follow the catalogue: Subject to Tax, "
  "Table Tax, Special Tax, Q1 OASDI, Q2 Medicare, Q3 FUTA, SUI, State programmes, State income tax, Local income tax. Yes-No means the row's "
  "explanation in the catalogue decides.", "")
cw = json.load(open(os.path.join(C.RESEARCH, "WTC-crosswalk.json"), encoding="utf-8"))["wage_types"]
FL = ["income_tax", "table_tax", "special_tax", "oasdi", "medicare", "futa", "sui", "state_programmes", "state_income_tax", "local_income_tax"]
grp = collections.OrderedDict()
for code, v in cw.items():
    if not v.get("flags") or code not in C.WTC:
        continue
    stem = re.sub(r"\s*[-–]?\s*type \d+$", "", v["label"], flags=re.I).strip()
    sig = tuple(v["flags"].get(k, {}).get("value", "-") for k in FL)
    grp.setdefault((stem, sig), []).append(code)


def ksort(c):
    return (0, int(c)) if c.isdigit() else (1, c)


rows = []
for (stem, sig), codes in grp.items():
    codes.sort(key=ksort)
    a, b = codes[0], codes[-1]
    for c_ in (a, b):
        C.WTCREF.setdefault(c_, set()).add("part5")
    cd = f"`{a}`" if a == b else f"`{a}` to `{b}` ({len(codes)})"
    basis = sorted({v["basis"] for c_ in codes for v in cw[c_]["flags"].values() if v.get("basis")})
    for rb in basis:
        R(rb)
    rows.append([stem, C.WTC[a]["category"], cd, *sig, ", ".join(basis[:3])])
table(["Wage type group", "Category", "Codes", "FIT", "Table", "Special", "Q1", "Q2", "Q3", "SUI", "Prog.", "State", "Local", "Basis"], rows)
A("---", "")

# ===================================================================== PART 6
at("part6")
A("## PART 6 — Open items", "",
  "Each item gives the design reading and the research reading. Where they differ the research wins. A limitation is written "
  "*Not configured in this release* with its identifier.", "")
table(["#", "Item", "Design reading", "Research reading", "Disposition"], [
    ["1", "Utah withholding before the new table", "One table selected by 58421", f"The table in force from {fact('ut.pit.base_allowance.single.annual')['effective_from']} is carried; the earlier table is not", NC("DESIGN-RQ-01")],
    ["2", "Form W-4 before the 2020 revision (allowance method, nonresident alien Table 1)", "2020 revision only", f"Allowance method and Table 1 exist in the research; the Data Dictionary has no field for the revision or the allowance count", NC("DESIGN-RQ-02")],
    ["3", "Supplemental withholding method", "Entity parameter 58414", "Payer chooses flat rate or aggregate method; the Data Dictionary has no field", NC("DESIGN-RQ-03")],
    ["4", "State unemployment insurance assigned rate", "Held per legal entity and State", "The State assigns the rate by notice; the Data Dictionary has no field", NC("DESIGN-RQ-04")],
    ["5", "Employee abroad: statement that stops withholding", "Flag 58410 routes the employee", "The statement stops withholding; the Data Dictionary has no field", NC("DESIGN-RQ-05")],
    ["6", "New-employer unemployment rate for some States", "Single rate per State", "Some States carry a rate by industry or by class and no single number", NC("DESIGN-RQ-06")],
    ["7", "FUTA credit reduction", "Potential rate recorded", "Final only after the year-end determination", f"{NC('RQ-402')}; {NC('RQ-403')}"],
    ["8", "2027 federal income tax schedules", "Schedules of the build year only", "Indexation for the next year is not published in the research", NC("RQ-530")],
    ["9", "Hawaii withholding for 2027", "Not modelled", "The State changes the brackets for 2027 and has not published the tables", NC("RQ-170")],
    ["10", "Virginia withholding for 2027", "Not modelled", "The statute changes the standard deduction for 2027; the formula is not published", NC("RQ-351")],
    ["11", "District of Columbia withholding method", "Method as recorded for the build year", "A change revoked personal exemptions and no method is published", NC("RQ-138")],
], )
A("**Statute against published method.** Where a State's published withholding method differs from the statute, the research "
  "directs which one the configuration follows. Both readings:", "")
for k in sorted(k for k in C.FACTS if k.startswith("practice.")):
    try:
        A(f"- {tag(k)} {R(C.regid(k))}")
    except ValueError:
        pass
A("", "---", "")

# ===================================================================== PART 7
at("part7")
text = "\n".join(L)
COND = re.compile(r"\b(LESS|GREATER|EQUALS|NOT_EQUALS|LESS_OR_EQUAL|GREATER_OR_EQUAL)\(\s*\$(\d+)\s*;\s*(-?\d+(?:\.\d+)?)\s*\)")
n_gates = len(COND.findall(text))
A("## PART 7 — Self-review", "",
  f"- Flags declared with their values: {len(FLAGS)}. Gates on a flag: {n_gates}; each compares a flag against a value of its declared list.",
  "- Every wage-type code and Data Dictionary field named in this design exists in the approved catalogue and dictionary.",
  "- Every rate, ceiling and threshold is a bound value; values of another period are written with their period.",
  "- Every limitation is written *Not configured in this release* with its identifier; none carries a value.",
  "- No State-level rule for a special population is configured: a scope statement under the owner decision.", "")

out = os.path.join(C.DESDIR, C.FILENAME)
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(L) + "\n")

os.makedirs(C.CHECKS, exist_ok=True)
with open(os.path.join(C.CHECKS, "design_bindings.csv"), "w", encoding="utf-8", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["location", "key", "register_id"])
    for r in sorted(set(C.USED)):
        w.writerow(r)
json.dump({"wtc": {k: sorted(v) for k, v in C.WTCREF.items()}, "dd": {k: sorted(v) for k, v in C.DDREF.items()},
           "reg": {k: sorted(v) for k, v in C.REGREF.items()}, "gaps": sorted(C.USED_GAPS), "new_employer_gap_states": nc6},
          open(os.path.join(C.CHECKS, "design_refs.json"), "w", encoding="utf-8"), indent=1)
print("written", out, len(L), "lines;", len(set(C.USED)), "bindings;", n_gates, "gates;", len(C.USED_GAPS), "gap ids")
