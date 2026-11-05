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
  "withholding, State unemployment insurance, State-mandated payroll programmes, local taxes by flag and the minimum wage rate for "
  "the 50 States and the District of Columbia. Every special population accepted "
  f"by the owner is in {R('US-OWN-005')}; State-level rules for special populations are a scope statement deferred to a later "
  "release, not a gap.", "",
  "**How to read the design.** Part 1 declares every flag with its values. Part 2 lists the accounts and the wage types they "
  "read or write. Part 3 gives the order of the regulations. Part 4 gives each regulation and the jurisdiction register they share. "
  "Part 5 gives the taxability matrix of the wage-type catalogue. Part 6 lists the open items, each with both readings where the "
  "design and the research differ; the research wins. Every rate, ceiling and threshold is written as a bound value; a value valid "
  "for a different period is written with that period. Annex section ids (for example `FED.2`, `UT.2`) name the section of "
  f"`US-CCG-001 v{C.PKG}` that holds the table or rule.", "", "---", "")

# ===================================================================== PART 0
at("part0")
A("## PART 0 — Special-category sweep", "",
  "Two sweeps ran against the Configuration Guide: one on every row of the coverage matrix, one on every population the owner "
  "accepted. A category is *in core* when a flag and a regulation of this design implement it; *no branch* when the research "
  "shows no differential treatment; *by reference* when the rule lives in a jurisdiction annex.", "")
cov = json.load(open(os.path.join(C.RESEARCH, "CCG-coverage-facts.json"), encoding="utf-8"))["coverage_matrix"]
COV = {
    "resident_employee": ("In core", "58404, 58415, 58416, 58420", "9840021, 9840031, 9840032, 9840041, 9840051, 9840052"),
    "non_resident_employee": ("In core: two meanings kept apart (nonresident alien of the United States; employee working in or living in another State)", "58404, 58418, 58419, 58424", "9840024, 9840031, 9840051"),
    "fixed_term_contract": ("No branch: no federal or general State fixed-term payroll regime", "none", "none"),
    "part_time": ("No branch: no federal part-time payroll regime", "none", "none"),
    "officers_without_employment_contract": ("In core as ordinary employees: corporate officers are employees for payroll; State coverage exclusions are annex rules reported on the State return", "58405", "9840021, 9840052"),
    "apprentices_and_trainees": ("No branch; student employees are a separate flag", "58411", "9840031, 9840032, 9840041"),
    "maternity_paternity_parental": ("By reference: no federal paid leave; State programmes are in 9840053", "58415, 58428", "9840053"),
    "work_accident_occupational_disease": ("By reference: State workers' compensation rows", "58415, 58428", "9840053"),
    "termination_and_final_pay": ("In core: final wages are paid wages; supplemental identification applies", "58413, 58414", "9840022, 9840023"),
    "mid_month_joiner_and_leaver": ("No branch: no proration rule; withholding follows the wages paid", "none", "none"),
    "annual_regularisation": ("No branch: no employer year-end regularisation; accumulators follow the payment year", "58420", "9840031, 9840041"),
    "overtime": ("In core as earnings; the qualified overtime premium is reported only; the minimum wage regulation reads the hours", "none", "9840011, 9840071"),
    "multiple_employers": ("In core: every wage base and accumulator is kept per employer entity", "58420", "9840031, 9840032, 9840041"),
    "local_regimes": ("In core by flag: locality fields of the Data Dictionary select the local rows", "58431, 58432, 58433, 58434, 58435, 58436, 58437, 58438, 58439, 58440", "9840061"),
    "employer_type_and_size": ("By reference: coverage thresholds sit in the programme parameters; health-coverage reporting is outside the calculation", "58415, 58428", "9840053"),
    "mid_year_rate_change": ("In core: dated values selected by the payment date, the date earned or the date the hours were worked", "58420, 58421, 58428", "9840031, 9840051, 9840053, 9840071"),
    "special_pay_cycles": ("In core: pay periods per year from the pay frequency", "58422", "9840021"),
    "accrual_vs_payment": ("In core: federal taxes follow the payment date; State programmes follow the date earned", "58420, 58428", "9840021, 9840031, 9840053"),
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
assert not [k for k in COV if k not in cov]
table(["Category", "Configuration Guide location", "Disposition", "Flags", "Regulations"], rows)

at("part0-populations")
A("**Populations accepted by the owner** " + R("US-OWN-005") + ".", "")
table(["Population", "Flag", "Regulations", "Wage types", "Rule carried by the research"], [
    ["Ordinary common-law employee", "58405 = 1", "9840021, 9840031, 9840032, 9840041, 9840051", f"{W('US-001')}, {W('US-006')}", "Default path of the design."],
    ["Nonresident alien", "58404 = 1, 58424", "9840024, 9840021, 9840031", f"{W('US-004')}, {W('US-033')}, {W('US-029')}", f"Single schedule whatever the marital status; cannot claim exempt; wage add-on added before the table; F-1, J-1, M-1 and Q-1 pay for the purpose of admission is exempt from FICA. {R('US-FEDS5-015')} {R(C.regid('fed.fica.nra.fjmq_exempt'))}"],
    ["Statutory employee", "58406 = 1, 58427", "9840021, 9840031, 9840041", W("US-035"), f"FICA withheld, no income tax withholding, FUTA for drivers and traveling salespersons only. {R(C.regid('fed.statutory_employee.treatment'))}"],
    ["Household employee", "58407 = 1", "9840021, 9840031, 9840041", W("US-028"), f"Income tax withholding only by agreement; FICA and FUTA from the cash-wage thresholds. {R(C.regid('fed.household.fit.withholding'))}"],
    ["Agricultural employee", "58408 = 1", "9840031, 9840041", W("US-036"), f"Own thresholds. {R(C.regid('fed.agricultural.total_threshold'))}"],
    ["Clergy", "58409 = 1", "9840021, 9840031, 9840032", W("US-034"), f"No withholding for income tax, social security or Medicare. {R(C.regid('fed.minister.withholding'))}"],
    ["Employee abroad", "58405 = 7", "9840021", f"{W('US-001')}", f"Withheld normally in package 1.0; the statement that stops withholding is a named limitation. {R(C.regid('fed.citizen_abroad.form673'))}"],
    ["Student employee", "58411 = 1", "9840031, 9840032, 9840041", W("US-038"), f"Private school or college student: income tax withheld, FICA and FUTA exempt. {R(C.regid('fed.students.treatment'))}"],
    ["Election worker", "58430 = 1", "9840031, 9840032", f"{W('US-001')}", f"FICA applies from the annual threshold. {R(C.regid('fed.election_worker.fica_threshold'))}"],
], )
A("Populations in detail (values as carried by the research):", "")
for k, lead in [("fed.statutory_employee.treatment", "Statutory employee"), ("fed.household.fit.withholding", "Household employee, federal income tax"),
                ("fed.minister.withholding", "Clergy"), ("fed.students.treatment", "Student employee"),
                ("fed.citizen_abroad.form673", "Employee abroad (citizen)"), ("fed.fica.nra.fjmq_exempt.scope", "Nonresident alien visa exemption")]:
    A(f"- **{lead}:** {tag(k)} {R(C.regid(k))}")
A(f"- **Household employee thresholds:** cash wages {T('fed.household.fica_cash_threshold')} a year for FICA; FUTA from {T('fed.household.futa_quarter_threshold')} in a quarter {R(C.regid('fed.household.fica_cash_threshold'))}")
A(f"- **Agricultural employee thresholds:** {T('fed.agricultural.per_worker_threshold')} per worker or {T('fed.agricultural.total_threshold')} in total; FUTA from {T('fed.agricultural.futa_quarter_threshold')} in a quarter {R(C.regid('fed.agricultural.total_threshold'))}")
A(f"- **Employee abroad:** foreign earned income exclusion {T('fed.feie.amount')} for {C.YEAR} {R(C.regid('fed.feie.amount'))}")
A(f"- **Nonresident alien commercial traveler:** up to {T('fed.fit.nra.commercial_traveler.max_days')} and {T('fed.fit.nra.commercial_traveler.max_pay')} of pay {R(C.regid('fed.fit.nra.commercial_traveler.max_days'))}")
A(f"- **Election workers:** FICA applies from {T('fed.election_worker.fica_threshold')} a year {R(C.regid('fed.election_worker.fica_threshold'))}")
A("", "**Population rules at State level.**", "")
for k in sorted(k for k in C.FACTS if k.startswith("special_population.")):
    A(f"- {tag(k)} {R(C.regid(k))}")
A("", "State-level rules for the remaining populations are deferred by owner decision " + R("US-OWN-005") + ". They are a scope statement of this release.", "",
  "**Fallback for the two populations not configured in package 1.0.** An employee first paid before 2020 who has no 2020 or later Form W-4 is handled manually: "
  f"the payroll operator enters the withholding, and the engine does not run the employee silently on the 2020 method ({NC('DESIGN-RQ-02')}). "
  f"A citizen abroad who holds a Form 673 statement is withheld normally, as an ordinary employee ({NC('DESIGN-RQ-05')}). Both are carried to version 1.1 of the Data Dictionary as a change request.", "", "---", "")

# ===================================================================== PART 1
at("part1")
A("## PART 1 — Flags and HR fields", "",
  "> The engine reads numbers only; string interpretation lives in flags only, never inside a regulation. Each flag lists its "
  "values; every gate in Part 4 compares a flag against one of its declared values, and every flag with values is used by at least one gate "
  "(a **[SOURCE]** flag is the origin of other flags; a USPS-code flag is a lookup key). A definition written `DD:` names a field "
  "of the Data Dictionary; a wage-type code is written in backticks.", "")
LOC_FLAGS = [
    ("58431", "New York City or Yonkers resident", "New York City or Yonkers residence status", "1 = New York City resident, 2 = Yonkers resident, 3 = neither"),
    ("58432", "Ohio municipality", "Ohio municipality of work", "1 = municipality of work or residence given, 2 = none"),
    ("58433", "Pennsylvania political subdivision", "Pennsylvania PSD code of the work location", "1 = PSD code given, 2 = none"),
    ("58434", "Indiana county", "Indiana county of residence on January 1", "1 = county given, 2 = none"),
    ("58435", "Maryland county", "Maryland county of residence", "1 = county given, 2 = none"),
    ("58436", "Kentucky locality", "Kentucky locality of work", "1 = locality given, 2 = none"),
    ("58437", "Oregon Metro or Multnomah", "Oregon Metro SHS or Multnomah PFA work location", "1 = location given, 2 = none"),
    ("58438", "Michigan city", "Michigan city of residence or predominant place of employment", "1 = city given, 2 = none"),
    ("58439", "Denver occupational privilege tax", "Denver occupational privilege tax work location", "1 = Denver work location, 2 = none"),
    ("58440", "Iowa school district", "Iowa school district of residence", "1 = district given, 2 = none"),
]
FLAGS = [
    ("58401", "Filing status", f"{D('Form W-4 filing status (Step 1(c))')} (option code J, S or H) **[DERIVED]**", "1 = married filing jointly or qualifying surviving spouse, 2 = single or married filing separately, 3 = head of household"),
    ("58402", "Multiple jobs box (Step 2)", f"{D('Form W-4 multiple jobs or spouse works (Step 2)')} **[DERIVED]**", "1 = box checked (Step-2 schedule), 2 = not checked (standard schedule)"),
    ("58403", "Exempt from withholding", f"{D('Form W-4 exempt from withholding')} **[DERIVED]**", "1 = exempt certificate in force, 2 = not exempt"),
    ("58404", "Nonresident alien", f"{W('US-033')}; {D('Nonresident alien flag')} **[DERIVED]**", "1 = nonresident alien, 2 = not"),
    ("58405", "Employee category", f"{D('Employee special population category')} (option code ORD, NRA, STAT, HH, AG, CLG, ABR) **[SOURCE]**", "1 = ordinary, 2 = nonresident alien, 3 = statutory employee, 4 = household, 5 = agricultural, 6 = clergy, 7 = employee abroad"),
    ("58406", "Statutory employee", f"{W('US-035')}; from 58405 **[DERIVED]**", "1 = statutory employee, 2 = not"),
    ("58407", "Household employee", f"{W('US-028')}; from 58405 **[DERIVED]**", "1 = household employee, 2 = not"),
    ("58408", "Agricultural employee", f"{W('US-036')}; from 58405 **[DERIVED]**", "1 = agricultural employee, 2 = not"),
    ("58409", "Clergy", f"{W('US-034')}; from 58405 **[DERIVED]**", "1 = minister of religion, 2 = not"),
    ("58411", "Student employee (exempt case)", f"{W('US-038')} **[DERIVED]**", "1 = student employee whose wages are exempt from FICA and FUTA, 2 = not"),
    ("58413", "Supplemental wage payment", "earning wage type with Special Tax = Yes, or Yes-No resolved as separately identified **[DERIVED]**", "1 = supplemental wages, 2 = regular wages"),
    ("58414", "Supplemental withholding method", f"`IF(EQUALS($58403;1);2;{D('Supplemental wage withholding method election')})`, with the default of the note below **[DERIVED]**", "1 = optional flat rate, 2 = aggregate method"),
    ("58415", "Work State", f"{D('Work State')} **[DERIVED]**", "USPS code of the jurisdiction register in Part 4"),
    ("58416", "Residence State", f"{D('Residence State')} **[DERIVED]**", "USPS code of the jurisdiction register in Part 4"),
    ("58417", "Unemployment insurance State", f"{W('US-041')}; {D('Unemployment insurance State')} **[DERIVED]**", "USPS code of the jurisdiction register in Part 4"),
    ("58418", "State withholding mode", "from 58415, 58416 and 58419 **[DERIVED]**", "1 = work State only, 2 = work State and residence State, 3 = reciprocity: work State does not withhold, residence State does"),
    ("58419", "Reciprocity certificate on file", f"{D('State withholding certificate on file')} **[DERIVED]**", "1 = certificate on file, 2 = none"),
    ("58420", "Payment-year rule set", "`IF(LESS(DATE_FORMAT($period.payment_date;'yyyyMMdd');'20270101');1;2)` **[DERIVED]**", "1 = 2026 rule set, 2 = 2027 rule set"),
    ("58421", "Utah table period", "`IF(LESS(DATE_FORMAT($period.payment_date;'yyyyMMdd');'20260401');1;2)` **[DERIVED]**", "1 = payment date before 2026-04-01, 2 = from 2026-04-01"),
    ("58422", "Pay periods per year", f"{D('Pay frequency')} **[DERIVED]**", "numeric: the count of pay periods of the pay frequency, see 9840021"),
    ("58424", "Nonresident alien visa exemption", f"{D('Nonresident alien visa class')} and {D('Work carries out the purpose of admission')} **[DERIVED]**", "1 = F-1, J-1, M-1 or Q-1 pay for the purpose of admission, 2 = not"),
    ("58425", "Totalization FICA exemption", f"{D('Totalization agreement FICA exemption')} **[DERIVED]**", "1 = exempt under an agreement, 2 = not"),
    ("58426", "Washington Cares exemption", f"{D('Washington Cares exemption status')} **[DERIVED]**", "1 = exempt, 2 = not"),
    ("58427", "Statutory employee liable to FUTA", f"{D('Occupation')} (driver or traveling salesperson) **[DERIVED]**", "1 = driver or traveling salesperson, 2 = other"),
    ("58428", "Earned-year rule set", "`IF(LESS(DATE_FORMAT($period.earned_date;'yyyyMMdd');'20270101');1;2)` **[DERIVED]**", "1 = wages earned in 2026, 2 = wages earned from 2027"),
    ("58429", "State-assigned UI rate on file", f"`IF(IS_NULL({D('State-assigned unemployment insurance rate')});2;1)` **[DERIVED]**", "1 = assigned rate on file, 2 = none: the new-employer rate applies"),
    ("58430", "Election worker", f"{D('Occupation')} (election official or election worker) **[DERIVED]**", "1 = election worker, 2 = not"),
]
for a, n, dd, v in LOC_FLAGS:
    FLAGS.append((a, n, f"{D(dd)} **[DERIVED]**", v))
head = ["Account", "Flag name", "Definition", "Values"]
A("| " + " | ".join(head) + " |", "|---|---|---|---|")
for a, n, d, v in sorted(FLAGS):
    A(f"| {a} | {n} | {d} | {v} |")
A("")
at("part1-notes")
A("**Note on 58420, 58421 and 58428.** Federal taxes follow the payment date, so the rule set is chosen by the payment date and not by the "
  "period worked. 58421 selects the Utah withholding table; the Utah table of the earlier period is " + NC("DESIGN-RQ-01") + ". State programme "
  "rates follow the date the wages were earned: " + tag("ma.pfml.rate.selection_basis") + " " + R(C.regid("ma.pfml.rate.selection_basis")) +
  " The same date rule is applied to every programme row; the research proves it for Massachusetts and the other rows carry the same rule until a State annex says otherwise.", "",
  "**Note on 58413 and 58414.** A payment identified separately from regular wages takes the supplemental path of 9840022 and 9840023. "
  "The payer elects the method in the legal-entity field above; the default when the field is blank is the aggregate method when no income tax was "
  "withheld from regular wages in the current or the preceding year, and the flat rate otherwise: " + tag("fed.fit.supplemental.aggregate_method") + " " +
  R(C.regid("fed.fit.supplemental.aggregate_method")) + ".", "",
  "**Note on 58422.** The pay periods per year are " + tag("fed.fit.pay_periods_per_year") + " " + R(C.regid("fed.fit.pay_periods_per_year")) + ".", "",
  "**Note on 58429.** The assigned rate is entered per State account and year in " + D("State-assigned unemployment insurance rate") +
  "; the way each State notifies the rate is a named limitation " + G("DD-RQ-11") + ".", "", "---", "")

# ===================================================================== PART 2
at("part2")
A("## PART 2 — Account register", "",
  "Accounts `58501` onwards hold bases, intermediates and results. The wage-type code is the row of `US-WTC-001` that carries the "
  "account in the pay run; an account with no catalogue row is an engine intermediate.", "")
ACCTS = [
    ("58501", "Base", "9840011", W("US-011"), "Federal income tax wages of regular wages (accumulator)"),
    ("58502", "Base", "9840011", W("US-012"), "Social security wages, capped accumulator"),
    ("58503", "Base", "9840011", W("US-014"), "Medicare wages and tips, uncapped accumulator"),
    ("58504", "Base", "9840011", W("US-015"), "Wages subject to Additional Medicare Tax withholding"),
    ("58505", "Base", "9840011", W("US-019"), "FUTA taxable wages"),
    ("58522", "Intermediate", "9840011", "none", "Supplemental wages of the payment (earning lines with 58413 = 1)"),
    ("58523", "Intermediate", "9840011", "none", "Supplemental wages of the year, accumulator"),
    ("58525", "Intermediate", "9840011", "none", "State income tax wages (Part 5 State column)"),
    ("58506", "Intermediate", "9840024", W("US-004"), "Nonresident alien wage add-on"),
    ("58507", "Result", "9840021", W("US-001"), "Federal income tax withheld, regular wages"),
    ("58508", "Result", "9840022", W("US-002"), "Federal income tax, supplemental wages at the optional flat rate"),
    ("58524", "Result", "9840022", W("US-001"), "Federal income tax, supplemental wages by the aggregate method"),
    ("58509", "Result", "9840023", W("US-003"), "Federal income tax, supplemental wages above the mandatory threshold"),
    ("58510", "Result", "9840031", Wg("21900"), "Social security tax, employee"),
    ("58511", "Result", "9840031", W("US-005"), "Social security tax, employer"),
    ("58512", "Result", "9840032", W("US-006"), "Medicare tax, employee"),
    ("58513", "Result", "9840032", W("US-007"), "Medicare tax, employer"),
    ("58514", "Result", "9840032", W("US-008"), "Additional Medicare Tax, employee"),
    ("58515", "Result", "9840041", W("US-009"), "FUTA, employer"),
    ("58516", "Result", "9840041", W("US-010"), "FUTA credit reduction, employer"),
    ("58517", "Result", "9840051", "`US-074` to `US-115`", "State income tax withheld, row of the work State"),
    ("58527", "Result", "9840051", "`US-074` to `US-115`", "State income tax withheld, row of the residence State"),
    ("58518", "Result", "9840052", "`US-116` to `US-166`", "State unemployment insurance, employer (one row per State)"),
    ("58519", "Result", "9840052", "`US-167` to `US-169`", "State unemployment insurance, employee"),
    ("58520", "Result", "9840053", "`US-170` to `US-203`, `US-205` to `US-210`", "State programmes, employee and employer"),
    ("58521", "Result", "9840061", "`US-211` to `US-233`", "Local taxes"),
    ("58526", "Result", "9840071", "none", "Applicable minimum hourly rate"),
]
for c_ in ("US-074", "US-115", "US-116", "US-166", "US-167", "US-169", "US-170", "US-203", "US-205", "US-210", "US-211", "US-233"):
    W(c_)
table(["Account", "Type", "Regulation", "Wage type", "Meaning"], ACCTS)
A(f"{W('US-204')} (Illinois Secure Choice) is an elective employee deduction, not a State programme tax; it is outside 9840053.", "", "---", "")

# ===================================================================== PART 3
at("part3")
A("## PART 3 — Regulation sequence", "",
  "Regulations run in this order for each payment. A regulation reads only accounts written by an earlier one.", "")
SEQ = [
    (1, "9840011", "Federal and State wage bases", "earning lines and their wage-type flags, 58413", "58501–58505, 58522, 58523, 58525"),
    (2, "9840024", "Nonresident alien add-on", "58501, 58404, 58422", "58506"),
    (3, "9840021", "Federal income tax, regular wages", "58501, 58506", "58507"),
    (4, "9840022", "Federal income tax, supplemental wages (flat rate and aggregate method)", "58501, 58507, 58522, 58523, 58414", "58508, 58524"),
    (5, "9840023", "Federal income tax, supplemental wages above the mandatory threshold", "58522, 58523", "58509"),
    (6, "9840031", "Social security tax", "58502, 58420", "58510, 58511"),
    (7, "9840032", "Medicare and Additional Medicare tax", "58503, 58504", "58512–58514"),
    (8, "9840041", "FUTA and credit reduction", "58505, 58417", "58515, 58516"),
    (9, "9840051", "State income tax withholding", "58525, 58507–58509, 58524, 58415–58419, 58421", "58517, 58527"),
    (10, "9840052", "State unemployment insurance", "58417, 58420, 58429", "58518, 58519"),
    (11, "9840053", "State programmes", "58415, 58426, 58428", "58520"),
    (12, "9840061", "Local taxes", "58431–58440", "58521"),
    (13, "9840071", "Minimum wage rate", "58415, hours with their work date", "58526"),
]
table(["Order", "Regulation", "Name", "Reads", "Writes"], SEQ)
A("---", "")

# ===================================================================== PART 4
at("part4")
A("## PART 4 — Regulation detail", "",
  "Amounts are rounded half-up to the cent between lines unless a State annex of the Configuration Guide sets another rule; "
  "full precision is carried between lines. A contribution or tax with an annual maximum is always the lesser of the remaining "
  "annual maximum and the rate times the period base; no annualise-then-divide shortcut is used.", "")

# ---- 9840011
A("### 9840011 — Federal and State wage bases", "",
  f"Reads the earning lines. Each earning wage type carries the flags Subject to Tax, Q1 (OASDI), Q2 (Medicare), Q3 (FUTA) and State income tax in "
  f"`US-WTC-001`; where a flag is Yes-No the explanation of the row decides, and Part 5 lists every row. Accumulators: {W('US-011')} "
  f"(58501), {W('US-012')} (58502), {W('US-014')} (58503), {W('US-015')} (58504), {W('US-019')} (58505). Separately identified supplemental wages (58413 = 1) "
  "are kept out of 58501 and held in 58522, so the same wages are never withheld on twice. Configuration Guide section `FED.2`.", "",
  "```",
  "58501 = SUM(IF(EQUALS($58413;2); wages of earnings with Subject to Tax = Yes; 0)) - pre-tax deductions that reduce income tax wages",
  "58522 = SUM(IF(EQUALS($58413;1); wages of earnings with Subject to Tax = Yes; 0))",
  "58523 = 58523_ytd_before + 58522",
  "58502 = SUM(earnings with Q1 = Yes) - pre-tax deductions that reduce FICA wages",
  "58503 = SUM(earnings with Q2 = Yes) - pre-tax deductions that reduce FICA wages",
  "58504 = 58503 year to date, above the Additional Medicare threshold",
  "58505 = SUM(earnings with Q3 = Yes) - payments exempt from FUTA",
  "58525 = SUM(earnings with State income tax = Yes) - deductions the State allows", "```", "",
  "Debit `58501`, `58502`, `58503`, `58504`, `58505`, `58522`, `58523`, `58525`.", "")

# ---- 9840024
A("### 9840024 — Nonresident alien add-on", "",
  f"Reads `$58501` and the flags 58404 and 58422. The add-on is added to the period wages before the schedule is read "
  f"{R(C.regid('fed.fit.nra.addon.table2.annual'))}. A flat-rate supplemental payment is withheld at the flat rate alone. Configuration Guide section `FED.2b`.", "",
  "```", "58506 = IF(EQUALS($58404;1); NRA_ADDON_TABLE2(58422); 0)", "```", "",
  "Add-on amounts per pay period for Table 1 and Table 2, in USD:", "")
PER = ["weekly", "biweekly", "semimonthly", "monthly", "quarterly", "semiannual", "annual", "daily"]
table(["Pay period", "Table 1", "Table 2"],
      [[p.capitalize()] + [Tn(fact(f"fed.fit.nra.addon.table{n}.{p}")) if has(f"fed.fit.nra.addon.table{n}.{p}") else "" for n in (1, 2)] for p in PER])
A(f"Table 1 applies to an employee whose Form W-4 predates the 2020 revision: {NC('DESIGN-RQ-02')}; the fallback is manual handling (Part 0). "
  f"The nonresident alien Form W-4 rule: {tag('fed.fit.nra.w4_rule')} {R(C.regid('fed.fit.nra.w4_rule'))}.", "",
  "Debit `58506`.", "")

# ---- 9840021
A("### 9840021 — Federal income tax, regular wages", "",
  f"Method: {tag('fed.fit.method')} {R(C.regid('fed.fit.method'))}. Configuration Guide section `FED.2`. Reads `$58501` and `$58506`; flags 58401, 58402, 58403, 58406, 58407, 58409, 58422.", "",
  "```",
  "pay_periods   = 58422",
  f"annual_wages  = (58501 + 58506) x pay_periods + {D('Form W-4 other income (Step 4(a))')}",
  f"line_1g       = IF(EQUALS($58402;1); 0; IF(EQUALS($58401;1); {tag('fed.fit.worksheet1a.line1g.mfj')}; {tag('fed.fit.worksheet1a.line1g.other')}))",
  f"adjusted      = MAX(0; annual_wages - {D('Form W-4 deductions (Step 4(b))')} - line_1g)",
  "row           = last row of the schedule with floor <= adjusted",
  "tentative     = cumulative_tax(row) + (adjusted - floor(row)) x rate(row)",
  f"credit        = {D('Form W-4 dependents and other credits (Step 3)')} / pay_periods",
  f"extra         = {D('Form W-4 extra withholding (Step 4(c))')}",
  "58507         = IF(EQUALS($58403;1); 0;",
  "                IF(EQUALS($58406;1); 0;",
  "                IF(EQUALS($58409;1); 0;",
  "                IF(EQUALS($58407;1); household_agreement_amount;",
  "                MAX(0; tentative / pay_periods - credit) + extra))))",
  "```", "",
  f"Schedule: the standard schedule when 58402 = 2, the Step-2 schedule when 58402 = 1. A household employee is withheld only "
  f"under an agreement {R(C.regid('fed.household.fit.withholding'))}, using "
  f"{D('Household employee: federal income tax withholding agreement')}. An employee without a certificate: {tag('fed.w4.default_no_certificate')} "
  f"{R(C.regid('fed.w4.default_no_certificate'))}. The exempt certificate: {tag('fed.w4.exempt.validity')} {R(C.regid('fed.w4.exempt.validity'))}.", "",
  "Debit `58507`.", "")
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
  f"Reads `$58501`, `$58507`, `$58522`, `$58523` and the flags 58403, 58406, 58409, 58414. {tag('fed.fit.supplemental.aggregate_method')} {R(C.regid('fed.fit.supplemental.aggregate_method'))}. "
  f"Configuration Guide section `FED.2`. The first {T('fed.fit.supplemental.mandatory_threshold')} of supplemental wages in the year is withheld by the chosen method; "
  f"only the part above it takes the mandatory rate, incrementally.", "",
  "```",
  f"below   = MAX(0; MIN(58523; {tag('fed.fit.supplemental.mandatory_threshold')}) - MIN(58523_ytd_before; {tag('fed.fit.supplemental.mandatory_threshold')}))",
  f"excess  = MAX(0; 58523 - MAX({tag('fed.fit.supplemental.mandatory_threshold')}; 58523_ytd_before))",
  f"58508 = IF(EQUALS($58406;1); 0; IF(EQUALS($58409;1); 0; IF(EQUALS($58403;1); 0; IF(EQUALS($58414;1); ROUND({tag('fed.fit.supplemental.flat_rate')}% x below); 0))))",
  "58524 = IF(EQUALS($58406;1); 0; IF(EQUALS($58409;1); 0; IF(EQUALS($58414;2); MAX(0; FIT_SCHEDULE(58501 + below) - 58507); 0)))",
  f"58509 = IF(EQUALS($58406;1); 0; IF(EQUALS($58409;1); 0; ROUND({tag('fed.fit.supplemental.mandatory_rate')}% x excess)))",
  "```", "",
  f"The optional flat rate is {T('fed.fit.supplemental.flat_rate')}; the mandatory rate is {T('fed.fit.supplemental.mandatory_rate')} on the part of the year's supplemental "
  f"wages above {T('fed.fit.supplemental.mandatory_threshold')} {R(C.regid('fed.fit.supplemental.flat_rate'))}. "
  f"The aggregate method uses the schedule of 9840021 on the sum of the regular wages and the supplemental wages under the threshold, less the regular withholding already computed. "
  f"An employee with an exempt certificate (58403 = 1) takes the aggregate method, which gives no withholding, but is still withheld at the mandatory rate on the excess. "
  f"Backup withholding is separate at {T('fed.fit.backup_withholding.rate')} {R(C.regid('fed.fit.backup_withholding.rate'))}.", "",
  "Debit `58508`, `58524`, `58509`.", "")

# ---- FICA
at("part4-fica")
A("### 9840031 — Social security tax (OASDI)", "",
  f"Reads `$58502` and the flags 58420, 58409, 58411, 58424, 58425, 58407, 58408, 58430. Employee row {Wg('21900')}; employer row {W('US-005')}. The wage base applies per employer. "
  "Configuration Guide section `FED.3`.", "",
  "```",
  f"limit_2026 = {tag('fed.fica.oasdi.wage_base', '2026')}   (payment dates in 2026)",
  f"limit_2027 = {tag('fed.fica.oasdi.wage_base', '2027')}   (payment dates from 2027-01-01)",
  "limit  = IF(EQUALS($58420;1); limit_2026; limit_2027)",
  "fica_exempt = IF(EQUALS($58411;1); 1; IF(EQUALS($58424;1); 1; IF(EQUALS($58425;1); 1; IF(EQUALS($58409;1); 1; 0))))",
  "below_threshold = IF(EQUALS($58407;1); household_cash_wages_ytd < household_threshold;",
  "                  IF(EQUALS($58408;1); agricultural_wages_ytd < agricultural_thresholds;",
  "                  IF(EQUALS($58430;1); election_wages_ytd < election_threshold; 0)))",
  f"58510 = IF(fica_exempt = 1; 0; IF(below_threshold; 0; ROUND({tag('fed.fica.oasdi.rate.employee')}% x MIN(58502; MAX(0; limit - 58502_ytd)))))",
  f"58511 = IF(fica_exempt = 1; 0; IF(below_threshold; 0; ROUND({tag('fed.fica.oasdi.rate.employer')}% x MIN(58502; MAX(0; limit - 58502_ytd)))))",
  "```", "",
  f"Social security base: {T('fed.fica.oasdi.wage_base', '2026')} for {C.YEAR} (period {C.period_label(fact('fed.fica.oasdi.wage_base', '2026'))}) "
  f"and {T('fed.fica.oasdi.wage_base', '2027')} from {fact('fed.fica.oasdi.wage_base', '2027')['effective_from']}; employee and employer each at {T('fed.fica.oasdi.rate.employee')} "
  f"{R(C.regid('fed.fica.oasdi.wage_base', '2026'))}. A student employee (58411 = 1) is exempt from FICA {R(C.regid('fed.students.treatment'))}; "
  f"an employee under a totalization agreement is exempt to the extent the agreement says so: {tag('fed.fica.totalization.exemption_rule')} "
  f"{R(C.regid('fed.fica.totalization.exemption_rule'))}; a nonresident alien in F-1, J-1, M-1 or Q-1 status working for the purpose of admission is exempt "
  f"{R(C.regid('fed.fica.nra.fjmq_exempt'))}. Thresholds: household cash wages {T('fed.household.fica_cash_threshold')} a year; agricultural wages "
  f"{T('fed.agricultural.per_worker_threshold')} per worker or {T('fed.agricultural.total_threshold')} in total; election workers {T('fed.election_worker.fica_threshold')} a year.", "",
  "Debit `58510`, `58511`.", "")
A("### 9840032 — Medicare tax and Additional Medicare Tax", "",
  f"Reads `$58503` and `$58504`, and the flags 58409, 58411, 58424, 58425, 58407, 58408, 58430 through `fica_exempt` and `below_threshold` of 9840031. The Medicare base has no annual cap. Employee row {W('US-006')}; employer row {W('US-007')}; "
  f"Additional Medicare row {W('US-008')}. Configuration Guide section `FED.3`.", "",
  "```",
  f"58512 = IF(fica_exempt = 1; 0; IF(below_threshold; 0; ROUND({tag('fed.fica.medicare.rate.employee')}% x 58503)))",
  f"58513 = IF(fica_exempt = 1; 0; IF(below_threshold; 0; ROUND({tag('fed.fica.medicare.rate.employer')}% x 58503)))",
  f"58514 = IF(fica_exempt = 1; 0; IF(below_threshold; 0; ROUND({tag('fed.fica.addl_medicare.rate')}% x MAX(0; 58503_ytd_after - MAX({tag('fed.fica.addl_medicare.withholding_threshold')}; 58503_ytd_before)))))",
  "```", "",
  f"Rates: employee {T('fed.fica.medicare.rate.employee')}, employer {T('fed.fica.medicare.rate.employer')}; Additional Medicare {T('fed.fica.addl_medicare.rate')} on wages above "
  f"{T('fed.fica.addl_medicare.withholding_threshold')} in the year, employee only {R(C.regid('fed.fica.medicare.rate.employee'))}. Clergy (58409 = 1) are not withheld for Medicare or Additional Medicare.", "",
  "Debit `58512`, `58513`, `58514`.", "")

# ---- FUTA
A("### 9840041 — FUTA and credit reduction", "",
  f"Reads `$58505` and the flags 58417, 58411, 58406, 58427, 58407, 58408. Rows {W('US-009')} and {W('US-010')}. Configuration Guide section `FED.3`.", "",
  "```",
  f"net_rate = {tag('fed.futa.rate.net')}%",
  "futa_exempt = IF(EQUALS($58411;1); 1; IF(EQUALS($58406;1); IF(EQUALS($58427;1); 0; 1); 0))",
  "below_futa_threshold = IF(EQUALS($58407;1); household_wages_quarter < household_futa_threshold;",
  "                       IF(EQUALS($58408;1); agricultural_wages_quarter < agricultural_futa_threshold; 0))",
  f"58515 = IF(futa_exempt = 1; 0; IF(below_futa_threshold; 0; ROUND(net_rate x MIN(58505; MAX(0; {tag('fed.futa.wage_base')} - 58505_ytd)))))",
  f"58516 = IF(futa_exempt = 1; 0; IF(below_futa_threshold; 0; ROUND(credit_reduction_rate(58417) x MIN(58505; MAX(0; {tag('fed.futa.wage_base')} - 58505_ytd)))))",
  "```", "",
  f"Gross rate {T('fed.futa.rate.gross')}, maximum credit {T('fed.futa.credit.max')}, net rate {T('fed.futa.rate.net')} on the first {T('fed.futa.wage_base')} of each employee's wages "
  f"{R(C.regid('fed.futa.rate.net'))}. The quarterly deposit applies when the liability exceeds {T('fed.futa.deposit_threshold')} {R(C.regid('fed.futa.deposit_threshold'))}. "
  f"Household FUTA starts at {T('fed.household.futa_quarter_threshold')} of cash wages in a quarter and agricultural FUTA at {T('fed.agricultural.futa_quarter_threshold')}. "
  f"A statutory employee is liable only as a driver or traveling salesperson {R(C.regid('fed.statutory_employee.treatment'))}. "
  f"Credit reduction for California ({T('fed.futa.credit_reduction.ca.potential.rate')}) and the Virgin Islands ({T('fed.futa.credit_reduction.vi.potential.rate')}) is a potential rate "
  f"for {C.YEAR}: {NC('RQ-402')} and {NC('RQ-403')}.", "",
  "Debit `58515`, `58516`.", "")

# ---- Jurisdiction register
at("part4-4-table")
A("### Jurisdiction register (read by 9840051, 9840052, 9840053 and 9840071)", "",
  "One row per State and the District of Columbia. *No wage tax* and *flat rate* come from the research; a flat rate is applied after the allowances, "
  "deductions or bands of the State annex, and the Massachusetts surtax is carried in its row. *Table or formula* means the State publishes tables or a formula. "
  "The *Annex* column names the section of the Configuration Guide that holds the rule (`.2` income tax withholding, `.3` unemployment insurance and payroll levies). "
  "Wage-base cells carry their own period.", "")
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
                   and c not in (sit, sui, suie, "US-204") and int(c[3:]) >= 167)
    if st in NO_TAX_STATES:
        cls = "No wage tax"
    elif has(f"{low}.pit.rate.flat") and numeric(f"{low}.pit.rate.flat"):
        cls = "Flat rate " + dated(f"{low}.pit.rate.flat") + ", after the State's allowances, deductions or bands"
    elif has(f"{low}.pit.rate") and numeric(f"{low}.pit.rate") and len(entries(f"{low}.pit.rate")) <= 2:
        cls = "Flat rate " + dated(f"{low}.pit.rate") + ", after the State's allowances, deductions or bands"
    else:
        cls = "Table or formula"
    if st == "MA" and has("ma.pit.surtax.rate"):
        cls += f"; surtax {Tn(fact('ma.pit.surtax.rate'))} above USD {Tn(fact('ma.pit.surtax.threshold'))}"
    wb_ = dated(f"{low}.sui.wage_base") if numeric(f"{low}.sui.wage_base") else "per annex"
    if has(f"{low}.sui.new_employer.rate") and numeric(f"{low}.sui.new_employer.rate"):
        nw = dated(f"{low}.sui.new_employer.rate")
    else:
        nw = NC("DESIGN-RQ-06")
        nc6.append(st)
    ee = dated(f"{low}.sui.employee.rate") if (has(f"{low}.sui.employee.rate") and numeric(f"{low}.sui.employee.rate")
                                               and any(f["value"] for f in entries(f"{low}.sui.employee.rate"))) else "none"
    if st == "NJ" and has("nj.ui.employee.wf_swf.rate"):
        ee += "; workforce and supplemental workforce fund " + dated("nj.ui.employee.wf_swf.rate")
    for c_ in [x for x in (sit, sui, suie) if x] + progs:
        W(c_)
    rows.append([nm, st, f"{st}.2 / {st}.3", sit or "none", cls, sui or "none", wb_, nw, f"{suie} {ee}" if suie else ee,
                 ", ".join(progs) or "none"])
table(["State", "USPS", "Annex", "Withholding row", "State income tax", "UI employer row", "UI wage base (USD)", "New-employer rate",
       "UI employee", "Programme rows"], rows)
A(f"A State whose single new-employer rate is not carried as one number is marked {G('DESIGN-RQ-06')}.", "")

# ---- 9840051
at("part4-states")
A("### 9840051 — State income tax withholding", "",
  f"Reads `$58525`, the federal withholding `$58507`, `$58508`, `$58509`, `$58524`, and the flags 58415 to 58419 and 58421. Rows {W('US-074')} to {W('US-115')}. "
  "The State of work and the State of residence decide the mode; the State wages are the State income tax wages of 9840011 (Part 5, State column), "
  "not the federal wages. Alabama and Oregon deduct federal withholding from the State base: "
  f"{tag('practice.al.fit_before_sit')} {R(C.regid('practice.al.fit_before_sit'))}; {tag('practice.or.federal_cap')} {R(C.regid('practice.or.federal_cap'))}.", "",
  "```",
  "fed_wh      = 58507 + 58508 + 58524 + 58509",
  "base(S)     = 58525 - IF(S is AL or OR; fed_wh limited as above; 0)",
  "state_wh(S) = IF(EQUALS($58421;2); STATE_METHOD(S; base(S)); STATE_METHOD_BEFORE_2026_04_01(S; base(S)))   -- the 58421 gate applies to Utah only",
  "work_tax    = state_wh(58415)",
  "res_tax     = state_wh(58416)",
  "credit      = residence-State credit for the work-State tax per the residence annex",
  "58517 = IF(EQUALS($58418;3); 0; work_tax)",
  "58527 = IF(EQUALS($58418;3); res_tax; IF(EQUALS($58418;2); MAX(0; res_tax - credit); 0))",
  "```", "",
  f"Mode 3 needs the certificate 58419 = 1; the work State stops withholding and the employer withholds for the residence State, for example a Pennsylvania resident working in New Jersey "
  f"with the NJ-165 certificate {R(C.regid('multi.reciprocity.nj.certificate'))}. Residence-State rules for residents working elsewhere are in the annex of the residence State; "
  f"for example {tag('multi.resident_out_of_state.ma.withholding_rule')} {R(C.regid('multi.resident_out_of_state.ma.withholding_rule'))}. "
  "Utah: the table in force from 2026-04-01 applies when 58421 = 2; before that date " + NC("DESIGN-RQ-01") + ". The default for a missing State certificate is set in Module 2 of the Configuration Guide.", "",
  "Debit `58517`, `58527`.", "")

# ---- SUI
A("### 9840052 — State unemployment insurance", "",
  "Reads the flags 58417, 58420 and 58429. The State of coverage is the State of localization " + R("US-MULTIS5-017") + ". Configuration Guide section `X.3` of the State.", "",
  "```",
  "base_limit = state_wage_base(58417; 58420)",
  "base       = MIN(sui_wages_period; MAX(0; base_limit - sui_wages_ytd_state))",
  f"rate_er    = IF(EQUALS($58429;1); {D('State-assigned unemployment insurance rate')}; new_employer_rate(58417; 58420))",
  "58518 = ROUND(rate_er x base)",
  "58519 = ROUND(employee_rate(58417; 58420) x base)",
  "```", "",
  "The assigned rate is entered per State account and year. A new employer, or an employer with no assigned rate on file, uses the new-employer rate of the jurisdiction register. "
  "An employee contribution exists only in the States whose row carries one. State UI wages follow the payment year. How each State notifies the assigned rate is a named limitation "
  + G("DD-RQ-11") + ".", "",
  "Debit `58518`, `58519`.", "")

# ---- programmes
at("part4-programmes")
A("### 9840053 — State programmes", "",
  "Reads the flags 58415, 58426 and 58428. One result row per programme and side (the jurisdiction register lists the rows of each State). "
  "Parameters are selected by the date the wages were earned (58428). Washington Cares is not withheld when 58426 = 1. The method of each parameter is in the *Method* column.", "",
  "```",
  "by rate:       58520 = ROUND(rate x MIN(programme_wages; MAX(0; cap - programme_wages_ytd)))",
  "by hour:       58520 = rate_per_hour x hours worked",
  "by week:       58520 = MIN(rate x MIN(weekly_wages; weekly_base); weekly_maximum)",
  "by quarter:    58520 = flat fee per quarter",
  "by threshold:  58520 = rate x wages above the quarterly threshold",
  "by share:      employee part = rate x employee_share; employer part = rate x (1 - employee_share)",
  "WA Cares:      58520 = IF(EQUALS($58426;1); 0; ROUND(rate x wages))",
  "```", "",
  "**Programme parameters.** Every dated value of the research for these programmes:", "")
PRG = re.compile(r"^([a-z]{2})\.(sdi|pfml|tdi|fli|pfl|famli|cares|phc|dbl|wbf|ccc|mbt|mctmt|transit|wc|stt|ui\.employee)[a-z_.0-9]*$")
EXTRA = {"or.stt.employee.rate", "nj.ui.employee.wf_swf.rate"}


def method_of(k):
    if re.search(r"per_hour|hourly", k):
        return "per hour"
    if re.search(r"weekly|week", k):
        return "weekly amount or cap"
    if re.search(r"quarterly", k):
        return "flat fee or threshold per quarter" if "threshold" in k else "flat fee per quarter"
    if re.search(r"threshold", k):
        return "threshold test"
    if re.search(r"share", k):
        return "side share"
    if re.search(r"benefit|nysaww", k):
        return "benefit parameter, not withheld"
    if re.search(r"wage_cap|wage_base|annual_max|max_annual|cap", k):
        return "annual cap"
    if re.search(r"rate", k):
        return "rate on wages"
    return "parameter"


rows = []
no2027 = []
for k in sorted(C.FACTS):
    m = PRG.match(k)
    if (not m and k not in EXTRA) or k[:2].upper() not in C.STATE_NAMES:
        continue
    if not numeric(k):
        continue
    st = k[:2].upper()
    es = [f for f in entries(k) if not (f.get("effective_to") and f["effective_to"] < "2026-01-01")]
    if es and not any((f.get("effective_to") is None) or f["effective_to"] >= "2027-01-01" for f in es):
        no2027.append(k)
    for f in es:
        at(f"part4-prg-{k}")
        rows.append([C.STATE_NAMES[st], k[3:].replace(".", " ").replace("_", " "), method_of(k), C.period_label(f), Tn(f)])
table(["State", "Parameter", "Method", "Period", "Value"], rows)
A("Massachusetts paid family and medical leave: the 2026 and 2027 splits are the dated entries above, selected by 58428. The disagreement between the statute and the published guidance is recorded in Part 6. "
  f"{W('US-205')} (Wyoming workers' compensation, employer-specific rate) and {W('US-207')} (New York MCTMT) carry no parameter in the research: {NC('DESIGN-RQ-07')}.", "",
  "Debit `58520`.", "")

# ---- locals
A("### 9840061 — Local taxes", "",
  "Reads the locality flags 58431 to 58440, set from the locality fields of the Data Dictionary. Local rows: " + ", ".join(W(c_) for c_ in sorted(c for c, v in C.WTC.items() if c.startswith("US-")
                                                                         and 211 <= int(c[3:]) <= 233)) + ". "
  "Each locality, rate, base and filing rule is set out in the jurisdiction annexes (section `X.2c`) of `US-CCG-001 v" + C.PKG + "`; this design routes the wages and does not repeat the rates.", "",
  "```",
  f"58521 = IF(EQUALS($58431;1); {W('US-223')} on {D('New York City or Yonkers residence status')}; IF(EQUALS($58431;2); {W('US-223')}; 0))",
  f"      + IF(EQUALS($58432;1); {W('US-224')} on {D('Ohio municipality of work')} and {D('Ohio municipality of residence')}; 0)",
  f"      + IF(EQUALS($58433;1); {W('US-228')} and {W('US-229')} on {D('Pennsylvania PSD code of the work location')} and {D('Pennsylvania PSD code of the residence')}; 0)",
  f"      + IF(EQUALS($58434;1); {W('US-215')} on {D('Indiana county of principal employment on January 1')}; 0)",
  f"      + IF(EQUALS($58435;1); {W('US-217')}; 0)",
  f"      + IF(EQUALS($58436;1); {W('US-216')} on {D('Kentucky locality of residence (school board component)')}; 0)",
  f"      + IF(EQUALS($58437;1); {W('US-226')} and {W('US-227')}; 0)",
  f"      + IF(EQUALS($58438;1); {W('US-218')} and {W('US-219')}; 0)",
  f"      + IF(EQUALS($58439;1); {W('US-212')} and {W('US-213')}; 0)",
  f"      + IF(EQUALS($58440;1); Iowa school district surtax; 0)",
  "```", "",
  f"The Ohio school district tax {W('US-225')} reads {D('Ohio school district of residence')}. The Iowa school district has no catalogue row: {NC('DESIGN-RQ-07')}. "
  "Other local rows of the catalogue are selected by the work location of the Data Dictionary and the annex of the State.", "",
  "Debit `58521`.", "")

# ---- minimum wage
at("part4-minwage")
A("### 9840071 — Minimum wage rate", "",
  "Reads the work State 58415 and the hours of the time data with their work date. The rate is selected by the date the hours were worked, not by the payment date; "
  "hours of a period that spans a change date are split at that date. " + tag("multi.wage_hour.overlay_rule") + " " + R(C.regid("multi.wage_hour.overlay_rule")) + ".", "",
  "```",
  "rate(S; d)  = dated rate of the State table below at the work date d (the federal rate when the State has no entry)",
  "58526 = MAX(federal_rate(d); rate(58415; d); local_rate(d))",
  "```", "",
  f"Federal rate: {T('fed.minwage.hourly')} {R(C.regid('fed.minwage.hourly'))}. Local minimum wages are set out in section `X.1` of the State annex. State rates reaching 2026 or later:", "")
rows = []
for k in sorted(C.FACTS):
    if re.match(r"^[a-z]{2}\.minwage\.hourly$", k) and k[:2].upper() in C.STATE_NAMES and numeric(k):
        st = k[:2].upper()
        for f in entries(k):
            if f.get("effective_to") and f["effective_to"] < "2026-01-01":
                continue
            at(f"part4-minwage-{k}")
            rows.append([C.STATE_NAMES[st], f"{st}.1", C.period_label(f), Tn(f)])
table(["State", "Annex", "Period", "Hourly rate (USD)"], rows)
A("A State with no row follows the federal rate. ", "---", "")
