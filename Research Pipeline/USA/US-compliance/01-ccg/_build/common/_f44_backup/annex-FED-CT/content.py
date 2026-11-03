"""Hand-written annex text. {{key}} / {{key@YYYY-MM-DD}} -> [[FACT:]] tag; {{key|v}} -> value with unit.
No quantity is typed here: every amount, rate, threshold or day-count is a placeholder bound to a facts key."""
from decimal import Decimal, ROUND_HALF_UP
import re

INTRO, SECTION_TEXT, AFTER, TAIL, PLACE, TITLES, PIVOTS, GAP_TOPIC = {}, {}, {}, {}, {}, {}, {}, {}

LAYER = ("Read with Annex FED (the federal layer every employee carries) and Annex MULTI (which routes an employee "
         "to this State by work location, residence or UI localization). Every value is shown with its effective "
         "dates and its source (list at the end of the annex). Federal values are not repeated here.")


def state_intro(name, tier_sentence):
    return [f"This annex sets out the {name} payroll rules for the 2026 build year. {LAYER}", tier_sentence]


SP_GAP = ("⚠️ RESEARCH-GAP (non-blocking): the coverage thresholds that apply to these populations (quarterly cash-wage "
          "and headcount thresholds for UI coverage of domestic, agricultural and non-profit employment) are cited "
          "by statute only and carry no facts key; the engine must not hard-code them until they are keyed.")

# =====================================================================================  FED
INTRO["FED"] = [
    "This annex sets out the federal payroll layer for the 2026 build year. It applies to every in-scope employee, "
    "in addition to the State layer that Annex MULTI selects. Every value is shown with its effective dates and its "
    "source (list at the end of the annex).",
    "Classification: federal income tax withholding and FICA are one calculation per employee with one authority "
    "(the IRS); FUTA is federal but its credit depends on the State UI paid and on the State's credit-reduction "
    "status, so it is a cross-layer dependency. Independent contractors and Form 1099-NEC reporting are out of scope "
    "(owner instruction of 2026-10-29) [US-OWN-008].",
]
SECTION_TEXT[("FED", "1")] = [
    "The federal Fair Labor Standards Act sets the floor. The employer pays the highest of the federal, State and "
    "local minimum wage (State annexes; rule in Annex MULTI, {{multi.wage_hour.overlay_rule}}). There is no "
    "federal daily overtime; pay frequency, pay-day timing and the method of payment are State law.",
]
SECTION_TEXT[("FED", "2")] = [
    "**Method.** {{fed.fit.method}}. Employee inputs come from Form W-4: {{fed.w4.input_fields}}. "
    "The computation, per pay period:",
    "```\n"
    "annual_wages   = period_wages x pay_periods            # periods: {{fed.fit.pay_periods_per_year}}\n"
    "adjusted       = annual_wages + W4_Step4a - W4_Step4b\n"
    "if not W4_Step2_checked: adjusted -= line_1g            # MFJ {{fed.fit.worksheet1a.line1g.mfj}}; other {{fed.fit.worksheet1a.line1g.other}}\n"
    "schedule       = STANDARD if not W4_Step2_checked else STEP2_CHECKED   # tables below, by filing status\n"
    "tentative      = schedule.cumulative_tax(bracket) + (adjusted - bracket.floor) x bracket.rate\n"
    "period_tax     = max(0, tentative - W4_Step3) / pay_periods + W4_Step4c\n"
    "```",
    "A pre-2020 Form W-4 is converted with the allowance value {{fed.fit.allowance.pre2020_value|v}} per allowance. "
    "Rounding: {{fed.fit.rounding}}. The exempt status on a 2026 Form W-4 lapses at year end: {{fed.w4.exempt.validity}}.",
    "**Supplemental wages** (bonuses, commissions, severance, back pay): optional flat rate {{fed.fit.supplemental.flat_rate}} %, "
    "or the aggregate method; mandatory rate {{fed.fit.supplemental.mandatory_rate}} % on supplemental wages above "
    "{{fed.fit.supplemental.mandatory_threshold|v}} in the calendar year. Backup withholding ({{fed.fit.backup_withholding.rate}} %) "
    "applies to reportable payments, not to wages.",
    "The cumulative-tax column of each STANDARD schedule was recomputed from the floors and rates (each row = previous "
    "row + (floor difference x previous rate)); every row agrees. The research published no cumulative-tax column for "
    "the Step-2-checked schedules; an engine computes it the same way from the floors and rates shown.",
]
SECTION_TEXT[("FED", "2b")] = [
    "Non-resident aliens are handled at withholding level: the Pub. 15-T add-on (tables below) is added to the wages "
    "used for the federal income tax computation only. It is not reported on the W-2, has no FICA or FUTA effect and "
    "is not applied to flat-rate supplemental wages. Form W-4 rule: {{fed.fit.nra.w4.rule}}. Treaty-exempt wages: "
    "{{fed.fit.nra.treaty_exempt.reporting}}. Commercial-traveller exception: present no more than "
    "{{fed.fit.nra.commercial_traveler.max_days}} days and paid no more than {{fed.fit.nra.commercial_traveler.max_pay|v}} "
    "by a foreign employer not engaged in a US trade or business. Other-State residents are a State matter (Annex MULTI).",
    "**Resident / non-resident matrix (federal income tax)**",
    "| Income type | US citizen or resident alien | Non-resident alien |\n"
    "|---|---|---|\n"
    "| Regular salary | Worksheet 1A, annual percentage method, base = federal income tax wages (FED.2) | Same method; the annual add-on ({{fed.fit.nra.addon.table2.annual|v}}, Table 2; {{fed.fit.nra.addon.table1.annual|v}}, Table 1) is added to the wage base before the computation; W-4 completed per the NRA rule |\n"
    "| Annual bonus / supplemental pay | Optional flat {{fed.fit.supplemental.flat_rate}} % or aggregate; {{fed.fit.supplemental.mandatory_rate}} % above {{fed.fit.supplemental.mandatory_threshold|v}} | Same rates; no add-on on flat-rate supplemental wages |\n"
    "| Severance | Wages ({{fed.severance.is_wages}}); supplemental-wage rules | Same as the non-resident supplemental row |\n"
    "| Equity (option exercise, share vesting) | {{fed.equity.withholding_treatment.resident}}; RSU FICA/FUTA timing: {{fed.equity.rsu.fica_timing}} | {{fed.equity.withholding_treatment.nonresident}} |\n"
    "| Benefits in kind | Taxable fringe benefits are wages; exclusions in FED.8 | {{fed.fit.nra.bik.treatment}} |\n"
    "| Contractor / labour-service pay | Independent contractors and Form 1099-NEC reporting are out of scope (owner instruction of 2026-10-29) [US-OWN-008] | Same |",
]
SECTION_TEXT[("FED", "3")] = [
    "**FICA.** Social security (OASDI): employee {{fed.fica.oasdi.rate.employee}} % and employer {{fed.fica.oasdi.rate.employer}} % "
    "on wages up to the annual base ({{fed.fica.oasdi.wage_base@2026-01-01|v}} for 2026; {{fed.fica.oasdi.wage_base@2027-01-01|v}} "
    "for 2027, carried with medium confidence, see the gap below). Medicare: employee {{fed.fica.medicare.rate.employee}} % and "
    "employer {{fed.fica.medicare.rate.employer}} %, no base. Additional Medicare tax: employee only, "
    "{{fed.fica.addl_medicare.rate}} % on wages paid above {{fed.fica.addl_medicare.withholding_threshold|v}} in the calendar "
    "year, regardless of filing status; no employer match.",
    "```\n"
    "oasdi_ee   = min(period_FICA_wages, max(0, oasdi_base - ytd_FICA_wages)) x oasdi_rate_ee\n"
    "medicare   = period_FICA_wages x medicare_rate_ee\n"
    "addl_med   = max(0, ytd_wages_after - max(addl_threshold, ytd_wages_before)) x addl_medicare_rate\n"
    "```",
    "**FUTA.** Gross rate {{fed.futa.rate.gross}} % less the maximum credit for State UI {{fed.futa.credit.max}} % gives the "
    "net {{fed.futa.rate.net}} % on the first {{fed.futa.wage_base|v}} per employee per year, across all States "
    "({{multi.futa.wage_base.scope}}). A State with an outstanding Title XII advance reduces the credit (2025 final reductions "
    "in the table; 2026 reductions pending, gaps below). Employer only.",
]
SECTION_TEXT[("FED", "4")] = [
    "There is no federal pay-statement statute ({{fed.payslip.statute.exists}}); the FLSA prescribes records only. "
    "Pay-statement content, delivery and language follow the State of the work location (State annexes; Annex MULTI).",
]
SECTION_TEXT[("FED", "5")] = [
    "All federal returns are filed by the third-party filing provider (no system integration in scope). Deposit "
    "schedule from the lookback period; Form 941 quarterly (Form 944 only on IRS notice); Form 940 annually; W-2/W-3 "
    "to SSA in the EFW2 format; ACA Forms 1094-C/1095-C for applicable large employers; new-hire reports to the State "
    "new-hire directory.",
]
SECTION_TEXT[("FED", "8")] = [
    "Federal exclusions below are the baseline the States conform to or depart from (State annexes carry each State's "
    "departures).",
]
SECTION_TEXT[("FED", "9")] = [
    "The federal Consumer Credit Protection Act sets the floor; a State may be stricter (State annexes). An IRS levy "
    "is not subject to the CCPA cap: the employee keeps only the exempt amount from the Publication 1494 tables "
    "(selected rows below). Interstate income-withholding orders follow Annex MULTI.",
]
SECTION_TEXT[("FED", "13")] = [
    "P.L. 119-21 is in force. Its tips and overtime deductions operate at **assessment** level: they reach withholding "
    "only through the employee's W-4 Step 4(b); the employer duty is **reporting** (W-2 box 12 codes and box 14b). "
    "Do not build them as payroll deductions; tips and overtime stay fully subject to FICA.",
]
SECTION_TEXT[("FED", "OR")] = [
    "Pub. 15-T 2026 publishes two worked examples, recorded below as oracle values: a non-resident alien paid weekly "
    "({{fed.oracle.pub15t.nra_example.wages|v}} after the add-on, withholding {{fed.oracle.pub15t.nra_example.withholding|v}} "
    "from the wage-bracket table) and a tribal gaming payment ({{fed.oracle.pub15t.tribal_example.payment|v}}, "
    "withholding {{fed.oracle.pub15t.tribal_example.withholding|v}}). No full percentage-method example is published; "
    "the percentage method is reproduced from Worksheet 1A and the tables in FED.2 in Module 12 (worked examples). "
    "The IRS Tax Withholding Estimator is not an oracle.",
]
SECTION_TEXT[("FED", "SP")] = [
    "All special populations are in scope. Federal rules are below; State rules are in the State annexes. US citizens "
    "working abroad: withholding may stop on the employee's foreign-earned-income-exclusion statement (exclusion "
    "{{fed.feie.amount|v}} for 2026).",
]
SECTION_TEXT[("FED", "LG")] = [
    "English is the only federal official language and places no obligation on private employers; no federal "
    "instrument fixes pay-statement content or language. IRS and SSA filings are in English. Second-language duties "
    "attach to State notices and posters only (State annexes).",
]

# =====================================================================================  MULTI
INTRO["MULTI"] = [
    "This annex is the routing layer. It decides, per employee, which State annexes apply in addition to Annex FED. "
    "Three master-data keys drive every decision: work location (income-tax withholding State and wage-hour law), "
    "residence (resident withholding, reciprocity, transport-worker and military-spouse rules) and the UI State "
    "resulting from the localization test (UI, and by default PFML/SDI). Every value is shown with its effective "
    "dates and its source.",
    "Routing order for the engine:",
    "1. Wage-hour law: the more protective of federal, State and local law at the place of performance ({{multi.wage_hour.overlay_rule}}).\n"
    "2. UI State: the localization test, applied once per employee and employer ({{multi.sui.localization_test}}).\n"
    "3. Work-State income-tax withholding: start when the non-resident threshold of the work State is met (MULTI.2 table), unless reciprocity with the residence State applies and the employee has filed the certificate (MULTI.2 reciprocity table).\n"
    "4. Residence-State withholding: apply the residence State's rule for residents working elsewhere (MULTI.2 table); the credit for tax paid to another State is an assessment matter, never a payroll deduction.\n"
    "5. Federal carve-outs override State sourcing for transport workers, seamen and military spouses.\n"
    "6. PFML/SDI premium State: the UI State unless the State's own coverage test differs (MULTI.3 table).",
]
SECTION_TEXT[("MULTI", "1")] = [
    "Wage-hour law follows the place of performance. California's reach is decided statute by statute (court rulings below).",
]
SECTION_TEXT[("MULTI", "2")] = [
    "General rule: {{multi.pit.sourcing.general}}. Everywhere without a convenience rule: {{multi.convenience.default}}. "
    "Local taxes sit outside State reciprocity (State annexes). The federal Mobile Workforce bills are drafts and are not modelled.",
]
SECTION_TEXT[("MULTI", "3")] = [
    "UI covers the whole service with one employer in one State. Employee UI contributions exist only in the States "
    "listed in {{multi.sui.employee_contribution_states}}. The FUTA base counts wages across all States.",
]
SECTION_TEXT[("MULTI", "4")] = [
    "Default: the pay-statement statute of the work-location State ({{multi.payslip.reach.default}}). California applies its "
    "own rule under the ruling recorded below.",
]
PIVOTS[("MULTI", "2")] = [
    {"title": "Residents working in another State: withholding rule and credit level",
     "regex": r"^multi\.(?:resident_out_of_state\.(?P<st>[a-z]{2})\.(?P<fld>withholding_rule)|resident_credit\.(?P<st2>[a-z]{2})\.(?P<fld2>level))$",
     "columns": [("withholding_rule", "Withholding rule"), ("level", "Credit for other-State tax operates at")]},
]
PIVOTS[("MULTI", "2")] += [
    {"title": "Reciprocity: partner States and exemption certificate",
     "regex": r"^multi\.reciprocity\.(?P<st>[a-z]{2})\.(?P<fld>partners|certificate|unilateral|nonresident_exempt)$",
     "columns": [("partners", "Partners"), ("unilateral", "One-way rule"), ("nonresident_exempt", "Non-resident exemption"), ("certificate", "Certificate")]},
    {"title": "Non-resident thresholds before work-State withholding starts",
     "regex": r"^multi\.nonresident\.(?P<st>[a-z]{2})\.(?P<fld>threshold_days|threshold_amount|threshold_share|threshold_rule|allocation_rule|employer_start_rule|catch_up_rule|threshold)$",
     "columns": [("threshold_days", "Days"), ("threshold_amount", "Amount"), ("threshold_share", "Share"), ("threshold_rule", "Rule"), ("allocation_rule", "Allocation"), ("employer_start_rule", "Employer start"), ("catch_up_rule", "Catch-up"), ("threshold", "Other")]},
    {"title": "Convenience-of-the-employer rules",
     "regex": r"^multi\.convenience\.(?P<st>[a-z]{2}|default)\.(?P<fld>rule|litigation_status)$",
     "columns": [("rule", "Rule"), ("litigation_status", "Litigation")]},
]
PIVOTS[("MULTI", "3")] = [
    {"title": "Other-State wage-base credit for UI (wages reported to another State count toward this State's base)",
     "regex": r"^multi\.sui\.other_state_wage_credit\.(?P<st>[a-z]{2})$",
     "columns": [("", "Credit")]},
    {"title": "PFML / SDI / TDI coverage test",
     "regex": r"^multi\.pfml\.coverage_test\.(?P<st>[a-z]{2}|default)$",
     "columns": [("", "Coverage test")]},
]
SECTION_TEXT[("MULTI", "SP")] = [
    "Transport workers, seamen and military spouses follow the federal carve-outs in MULTI.2. All other special "
    "populations follow the State annexes of the States the routing selects.",
]
SECTION_TEXT[("MULTI", "LG")] = [
    "No multistate language rule: the payslip is in English and its content follows the work-location State.",
]

# =====================================================================================  AK
INTRO["AK"] = state_intro("Alaska", "Classification: T1. Alaska has no wage income tax; the State layer is UI, labour standards and reporting.")
SECTION_TEXT[("AK", "2")] = [
    "Alaska levies no individual income tax and no State income-tax withholding ({{ak.pit.exists}}): no State withholding "
    "certificate, supplemental rate, withholding return, reciprocity or State W-2 filing. Only the federal layer withholds "
    "income tax.",
]
SECTION_TEXT[("AK", "2b")] = [
    "Not applicable: without a State income tax there is no resident or non-resident treatment and no reciprocity; the "
    "income-tax matrix is the federal one (Annex FED, FED.2b). For UI, wages a transferred employee was paid by the same "
    "employer and reported to another State in the same year count toward the Alaska wage base "
    "({{multi.sui.other_state_wage_credit.ak}}); the quarterly report carries a flag for them.",
]
SECTION_TEXT[("AK", "3")] = [
    "UI is funded by an employee contribution, deducted by the employer, and an employer contribution, both on wages up to "
    "the annual base. The STEP and TVEP shares are carved out of the employee contribution, not added to it. For 2026 every "
    "employer class sits at the floor of the schedule. There is no SDI, TDI, PFML, long-term-care or transit levy "
    "({{ak.sdi_pfml.exists}}). Workers' compensation is an insurer premium outside payroll.",
    "```\nak_ui_ee = min(period_UI_wages, max(0, ak_wage_base - ytd_UI_wages)) x ak_ui_employee_rate\n"
    "ak_ui_er = min(period_UI_wages, max(0, ak_wage_base - ytd_UI_wages)) x employer_class_rate\n```",
]
SECTION_TEXT[("AK", "SP")] = [
    "- Domestic and household workers: excluded from the minimum wage, overtime and sick-leave rules (AS 23.10.055(a)(4)); UI coverage only above the quarterly cash-wage threshold.\n"
    "- Agricultural workers: excluded from minimum wage, overtime and sick leave; UI coverage only above the agricultural thresholds.\n"
    "- Commercial fishing: crews excluded from wage-hour and sick-leave rules; small share-paid crews excluded from UI; seamen excluded from overtime.\n"
    "- Minors under 18 working part time: excluded from wage-hour and sick-leave rules except in a week above the part-time limit (8 AAC 15.135).\n"
    "- Tipped employees: no tip credit; the full minimum wage is due in cash.\n"
    "- Clergy and religious orders: excluded from UI; volunteers of religious non-profits excluded from wage-hour rules.\n"
    "- Students at their own school and young work-study students: excluded from UI; student learners may be paid below the minimum wage under a certificate (8 AAC 15.125).\n"
    "- Non-resident aliens: no State rule beyond the federal one.\n"
    "- Corporate officers: excluded from UI unless the employer elects coverage for all officers; commission-only insurance, real-estate and securities agents excluded from UI when excluded from FUTA.\n"
    "- Government: excluded from the minimum-wage, overtime and sick-leave rules; UI contributory or reimbursable.\n"
    "- Non-profit employers: UI above the statutory size thresholds, with a reimbursable option.\n"
    "- Multistate: UI wage-base credit for other-State wages of transferred employees (AK.2b); sick-leave reach to employees working partly in Alaska is open (AK.6).",
    SP_GAP,
]
SECTION_TEXT[("AK", "LG")] = ["No language clause in the pay-statement rule or the posters: payslip and filings in English."]

# =====================================================================================  AL
INTRO["AL"] = state_intro("Alabama", "Classification: T4. Besides State withholding, municipal and county occupational taxes are withheld by the employer and remitted to the locality on its own return.")
SECTION_TEXT[("AL", "1")] = [
    "Alabama has no State minimum-wage, overtime, pay-frequency, payment-method or paycard statute ({{al.minwage.state.exists}}); "
    "the federal floor applies (Annex FED). Local wage and leave mandates are pre-empted ({{al.local_wage_leave_mandates.preempted}}).",
]
SECTION_TEXT[("AL", "2")] = [
    "**Method.** {{al.wh.method}}. The federal income tax withheld is deductible ({{al.wh.federal_fit_deductible}}), so the "
    "federal computation runs first. Certificate: {{al.wh.certificate.form}}.",
    "```\n"
    "annual_wages  = period_wages x pay_periods\n"
    "taxable       = annual_wages - std_deduction(status, annual_wages) - annual_FIT_withheld\n"
    "                - personal_exemption(status) - dependents x dependent_amount(annual_wages)\n"
    "annual_tax    = brackets(status)(taxable)       # rates and ceilings below\n"
    "period_tax    = annual_tax / pay_periods\n"
    "```",
    "Standard deduction by status: single maximum {{al.wh.std_deduction.single.max|v}}, minimum {{al.wh.std_deduction.single.min|v}}; "
    "married maximum {{al.wh.std_deduction.married.max|v}}, minimum {{al.wh.std_deduction.married.min|v}}; married filing "
    "separately maximum {{al.wh.std_deduction.married_separate.max|v}}; head of family maximum {{al.wh.std_deduction.head_of_family.max|v}}. "
    "Personal exemption: single {{al.wh.personal_exemption.single|v}}, married {{al.wh.personal_exemption.married|v}}. "
    "Dependent amount by gross income band: {{al.wh.dependent.gi_to_50000|v}}, {{al.wh.dependent.gi_to_100000|v}}, "
    "{{al.wh.dependent.gi_above_100000|v}}.",
    "**Standard-deduction phase-out** (booklet rev. 01/2026 p.6 formula and p.7 schedule): {{al.wh.std_deduction.phaseout_steps}}",
    "```\n"
    "if GI <= start_gi:        std = max_deduction\n"
    "elif GI >= floor_from_gi: std = min_deduction\n"
    "else:                     std = max_deduction - reduction_per_step x ceil((GI - start_gi) / step_size)\n"
    "```",
    "| Status | Maximum | Phase-out starts above GI | Reduction per step | Step size | Minimum from GI |\n"
    "|---|---|---|---|---|---|\n"
    "| Single (0/S) | {{al.wh.std_deduction.single.max|v}} | {{al.wh.std_deduction.single.phaseout.start_gi|v}} | {{al.wh.std_deduction.single.phaseout.reduction_per_step|v}} | {{al.wh.std_deduction.single.phaseout.step_size|v}} | {{al.wh.std_deduction.single.phaseout.floor_from_gi|v}} |\n"
    "| Married filing separately (MS) | {{al.wh.std_deduction.married_separate.max|v}} | {{al.wh.std_deduction.married_separate.phaseout.start_gi|v}} | {{al.wh.std_deduction.married_separate.phaseout.reduction_per_step|v}} | {{al.wh.std_deduction.married_separate.phaseout.step_size|v}} | {{al.wh.std_deduction.married_separate.phaseout.floor_from_gi|v}} |\n"
    "| Married (M) | {{al.wh.std_deduction.married.max|v}} | {{al.wh.std_deduction.married.phaseout.start_gi|v}} | {{al.wh.std_deduction.married.phaseout.reduction_per_step|v}} | {{al.wh.std_deduction.married.phaseout.step_size|v}} | {{al.wh.std_deduction.married.phaseout.floor_from_gi|v}} |\n"
    "| Head of family (H) | {{al.wh.std_deduction.head_of_family.max|v}} | {{al.wh.std_deduction.head_of_family.phaseout.start_gi|v}} | {{al.wh.std_deduction.head_of_family.phaseout.reduction_per_step|v}} | {{al.wh.std_deduction.head_of_family.phaseout.step_size|v}} | {{al.wh.std_deduction.head_of_family.phaseout.floor_from_gi|v}} |",
    "The minimum deduction of each status is stated in the phase-out rule above.",
    "**Supplemental pay:** may be withheld at {{al.wh.supplemental.rate}} %. **Overtime:** the 2026 overtime-premium deduction "
    "(up to {{al.pit.overtime_premium_deduction.max|v}}) operates at **assessment** level only; it changes neither wages nor "
    "withholding (W-2 box 12 code TT is informational). Do not build it as a payroll deduction.",
]
SECTION_TEXT[("AL", "2b")] = [
    "No reciprocity agreement ({{al.reciprocity.exists}}). Residents are withheld on all wages wherever earned except when the "
    "employer withholds for the work State; non-residents only on Alabama wages. The non-resident safe harbour "
    "({{al.nonres.safe_harbor.days}} days, Act 2025-334) operates at withholding level.",
    "**Resident / non-resident matrix (Alabama income tax)**",
    "| Income type | Resident | Non-resident |\n"
    "|---|---|---|\n"
    "| Regular salary | Formula method (AL.2) on all wages, unless the employer withholds for the work State | Formula method on Alabama wages only, after the {{al.nonres.safe_harbor.days}}-day safe harbour where the home State qualifies |\n"
    "| Annual bonus / supplemental pay | {{al.wh.supplemental.rate}} % or the formula on the aggregate | Same, on the Alabama portion |\n"
    "| Severance | Downsizing severance exempt up to {{al.wh.severance.exempt_max|v}} with prior ADOR approval; otherwise supplemental pay | Same, on the Alabama portion |\n"
    "| Equity | Supplemental-pay treatment; federal classification of equity income in Annex FED (FED.2b) | Same, on the Alabama portion |\n"
    "| Benefits in kind | Included in withholding wages; HSA treatment conforms ({{al.hsa.conforms}}); transit and group-term life open (AL.8) | Same, on the Alabama portion |\n"
    "| Contractor pay | Out of scope | Out of scope |",
]
SECTION_TEXT[("AL", "2c")] = [
    "Municipal and county occupational taxes are withheld by the employer and remitted to the city or county on its own "
    "return; the Department of Revenue does not administer them. The only rate in the research is Leeds (table). The State "
    "keeps no list of levying localities (blocking gap below): the engine needs a locality table before any Alabama "
    "employee can be paid.",
]
SECTION_TEXT[("AL", "3")] = [
    "Employer-only UI ({{al.sui.employee.rate}} % employee) on wages up to the base, plus the Employment Security Assessment. "
    "No SDI, TDI or PFML ({{al.sdi_pfml.exists}}).",
]
SECTION_TEXT[("AL", "4")] = ["Alabama has no pay-statement statute ({{al.payslip.state_statute.exists}}); local rules may require a pay-stub line (Leeds, AL.2c)."]
SECTION_TEXT[("AL", "OR")] = "EXAMPLE_AL"
SECTION_TEXT[("AL", "SP")] = [
    "- Domestic and household workers: exempt from Alabama withholding; UC-covered above the quarterly cash-wage threshold.\n"
    "- Agricultural workers: exempt from withholding (Alabama does not follow the federal rule); UC above the agricultural thresholds.\n"
    "- Minors: child-labour limits; no youth wage.\n"
    "- Tipped employees: federal tip credit; tips are UC wages.\n"
    "- Clergy: ministers exempt from Alabama withholding; church employment not UC-covered.\n"
    "- Students, non-resident aliens, statutory employees: no Alabama rule beyond the federal one.\n"
    "- Other-State workers: non-resident safe harbour (AL.2b); federal carrier carve-outs (Annex MULTI).\n"
    "- Government and non-profit: 501(c)(3) employers UC-covered above the size threshold; the pre-emption rule does not cover public employees.\n"
    "- Military spouses: certificate A4-MS.\n"
    "- Downsizing severance: exempt up to {{al.wh.severance.exempt_max|v}} with ADOR approval.",
    SP_GAP,
]
SECTION_TEXT[("AL", "LG")] = ["English. A Spanish version of the A4 exists (optional seam). Payslip and filings in English."]

# =====================================================================================  AR
INTRO["AR"] = state_intro("Arkansas", "Classification: T3. Separate State withholding and UI; no local wage tax.")
SECTION_TEXT[("AR", "2")] = [
    "**Method.** {{ar.wh.method}}. Certificate: {{ar.wh.certificate.form}}.",
    "```\n"
    "annual_wages = period_wages x pay_periods\n"
    "net_taxable  = annual_wages - ar_std_deduction\n"
    "if net_taxable is in the band-midpoint range of the formula: net_taxable = midpoint of its 100-dollar band\n"
    "annual_tax   = round_to_dollar(net_taxable x bracket.rate - bracket.subtract)   # table below\n"
    "annual_tax  -= exemptions x ar_personal_credit\n"
    "period_tax   = max(0, annual_tax) / pay_periods\n"
    "```",
    "Standard deduction {{ar.wh.std_deduction|v}}; personal credit {{ar.wh.personal_credit.per_exemption|v}} per exemption. "
    "The subtraction column was recomputed from the ceilings and rates (each row = previous subtraction + previous ceiling x "
    "rate step); every row agrees. Above the high-income threshold ({{ar.pit.high_income.threshold|v}}) the statute applies a "
    "two-band table: {{ar.pit.statute.tables}}.",
    "**Rate change in 2026.** The top rate is {{ar.pit.rate.top}} % for tax years from 2026-01-01 (Act 1 of the 2026 First "
    "Extraordinary Session, {{ar.live.act1_2026_ex_sess.status}}). The date from which employers had to apply the reissued "
    "formula is not in the research: blocking gap below. Until it is closed, the engine cannot decide which formula applies "
    "to pay dates before the switch.",
    "**Supplemental pay:** {{ar.wh.supplemental.rate}} %. **Texarkana:** {{ar.wh.texarkana.exemption}}.",
]
SECTION_TEXT[("AR", "2b")] = [
    "No reciprocity. Sourcing: {{ar.nonres.sourcing}}.",
    "**Resident / non-resident matrix (Arkansas income tax)**",
    "| Income type | Resident | Non-resident |\n"
    "|---|---|---|\n"
    "| Regular salary | Formula method (AR.2) on all wages | Formula method on wages for work physically performed in Arkansas, apportioned by Arkansas working days |\n"
    "| Annual bonus / supplemental pay | {{ar.wh.supplemental.rate}} % | {{ar.wh.supplemental.rate}} % on the Arkansas portion |\n"
    "| Severance | ⚠️ RESEARCH-GAP (non-blocking): no Arkansas-specific treatment in the research | Same gap |\n"
    "| Equity | Supplemental-pay treatment; federal classification of equity income in Annex FED (FED.2b) | Same, on the Arkansas portion |\n"
    "| Benefits in kind | Withholding wages; cafeteria-plan exclusion ({{ar.sui.wages.section125_excluded}} for UI); HSA, transit and group-term life open (AR.8) | Same, on the Arkansas portion |\n"
    "| Contractor pay | Out of scope | Out of scope |",
]
SECTION_TEXT[("AR", "3")] = [
    "Employer-only UI ({{ar.sui.employee.rate}} % employee) on wages up to the base, plus the administrative assessment. "
    "No SDI, TDI, PFML, long-term-care or transit levy.",
]
SECTION_TEXT[("AR", "OR")] = "EXAMPLE_AR"
SECTION_TEXT[("AR", "SP")] = [
    "- Domestic workers: exempt from Arkansas withholding; UI above the quarterly cash-wage threshold.\n"
    "- Agricultural workers: withholding required above the agricultural headcount threshold; no State overtime; UI above the agricultural thresholds.\n"
    "- Tipped employees: cash wage {{ar.minwage.tipped.cash_wage|v}}; written tip-credit notice; reported tips are withheld.\n"
    "- Clergy: ministers exempt from Arkansas withholding.\n"
    "- Students: sub-minimum wage only with a Department of Labor certificate (11-4-210(b)); UI excludes students at their own school.\n"
    "- Non-resident aliens: no Arkansas rule beyond the federal one. Commission agents excluded from UI.\n"
    "- Government and non-profit: covered by withholding; UI reimbursable option.\n"
    "- Military: active-duty pay exempt (Act 1408 of 2013); spouses file ARW-4MS yearly.\n"
    "- Small employers below {{ar.minwage.employer_size_min}} employees: outside the State minimum-wage act.\n"
    "- Minors: ⚠️ RESEARCH-GAP [[GAPKEY:ar.leave.mandated_leave]] (non-blocking): child-labour hour limits not in the research (AR.6).",
    SP_GAP,
]
SECTION_TEXT[("AR", "LG")] = ["No language rule for pay records. Payslip and filings in English."]

# =====================================================================================  AZ
INTRO["AZ"] = state_intro("Arizona", "Classification: T3. Separate State withholding and UI; no local wage tax; local minimum wages in Tucson and Flagstaff.")
SECTION_TEXT[("AZ", "1")] = [
    "State minimum wage {{az.minwage.hourly@2026-01-01|v}} for 2026 and {{az.minwage.hourly@2027-01-01|v}} for 2027, indexed "
    "{{az.minwage.indexation}}. Cities may set higher rates ({{az.local_minwage.allowed}}); Tucson and Flagstaff do. No State "
    "overtime statute: federal overtime applies.",
]
SECTION_TEXT[("AZ", "2")] = [
    "**Method.** {{az.wh.method}}. The employee elects one of {{az.wh.rate_options}} on Form A-4; without an election the "
    "default is {{az.wh.default_rate}} %. Supplemental pay: {{az.wh.supplemental.rate}}. Excluded from withholding: "
    "{{az.wh.exclusions}}.",
    "```\nperiod_tax = period_federal_FIT_wages x elected_percentage      # W-2 box 1 wages\n```",
]
SECTION_TEXT[("AZ", "2b")] = [
    "Non-residents are withheld after {{az.nonres.withholding_days_threshold}} days in Arizona in the year. Residents of "
    "{{az.nonres.wec_states}} may claim exemption on Form WEC (one-way: the credit is claimed at assessment).",
    "**Resident / non-resident matrix (Arizona income tax)**",
    "| Income type | Resident | Non-resident |\n"
    "|---|---|---|\n"
    "| Regular salary | Elected percentage of federal FIT wages | Elected percentage on Arizona wages after the {{az.nonres.withholding_days_threshold}}-day threshold; WEC exemption for residents of the listed States |\n"
    "| Annual bonus / supplemental pay | Same elected percentage | Same, on the Arizona portion |\n"
    "| Severance | Same elected percentage (federal wage definition) | Same, on the Arizona portion |\n"
    "| Equity | Same elected percentage; federal classification of equity income in Annex FED (FED.2b) | Same, on the Arizona portion |\n"
    "| Benefits in kind | Included where in federal FIT wages | Same, on the Arizona portion |\n"
    "| Contractor pay | Out of scope | Out of scope |",
]
SECTION_TEXT[("AZ", "3")] = [
    "Employer-only UI ({{az.sui.employee.rate}} % employee) on wages up to the base. From 2027 experience-rated employers pay "
    "{{az.ui_operating_fund.rate_of_ui_liability}} % of their UI liability into the UI Operating Fund, with UI liability reduced "
    "by the same amount. No SDI, TDI or PFML ({{az.sdi_pfml.exists}}).",
]
SECTION_TEXT[("AZ", "SP")] = [
    "- Domestic workers: no Arizona withholding (43-403(A)(2)); Tucson minimum wage excludes casual babysitting; UI threshold open (AZ.3).\n"
    "- Agricultural workers: no withholding for seasonal hand field labour except machine operators (who may elect).\n"
    "- Minors: hour limits for under-16s (table in AZ.1); under-18 newspaper carriers excluded from UI.\n"
    "- Tipped employees: tip credit up to {{az.minwage.tip_credit.max|v}} (State and Tucson); no tip credit in Flagstaff.\n"
    "- Clergy: churches and ministers excluded from UI; no withholding exception.\n"
    "- Students: own-school students, student nurses and interns, co-op students excluded from UI.\n"
    "- Non-resident aliens and statutory employees: no Arizona rule beyond the federal one; non-resident day threshold (AZ.2b).\n"
    "- Government: the sick-time law and the Tucson minimum wage exclude State and federal employers.\n"
    "- Native Americans working on their own reservation and military spouses: WEC exemption.\n"
    "- Non-resident common-carrier, motion-picture and disaster-recovery workers: excluded.",
    SP_GAP,
]
SECTION_TEXT[("AZ", "LG")] = ["The sick-time notice must be in English and Spanish (23-375(B)); minimum-wage and sick-time posters in both languages. The pay statement itself is in English."]

# =====================================================================================  CA
INTRO["CA"] = state_intro("California", "Classification: T3. Separate State withholding (PIT) and payroll taxes (UI, ETT, SDI) on one EDD return set; no local wage tax; local minimum wages exist.")
SECTION_TEXT[("CA", "1")] = [
    "State minimum wage {{ca.minwage.hourly@2026-01-01|v}} for 2026 and {{ca.minwage.hourly@2027-01-01|v}} for 2027. Overtime: "
    "{{ca.overtime.rule}}. No tip credit ({{ca.deductions.tip_credit.allowed}}). Cities and counties may set higher minimum "
    "wages and some industries have their own minimums: both are blocking gaps below, so a California work location cannot "
    "be paid at the State rate without first checking the locality and the industry.",
]
SECTION_TEXT[("CA", "2")] = [
    "**Method.** {{ca.wh.method}}. Certificate: {{ca.wh.certificate.form}}. Method B, per pay period:",
    "```\n"
    "annual_wages = period_wages x pay_periods\n"
    "if annual_wages <= low_income_exemption(status, allowances): tax = 0\n"
    "taxable      = annual_wages - estimated_deduction x additional_allowances - std_deduction(status, allowances)\n"
    "annual_tax   = brackets(status)(taxable) - allowance_credit x allowances\n"
    "period_tax   = max(0, annual_tax) / pay_periods\n"
    "```",
    "Bands by status: single, married and head of household each have their own table in this section (DE 44 (2026) "
    "Method B Tables 6 and 7, annual), with the rate, the ceiling and the tax at the bottom of each band (base). Married "
    "ceilings: {{ca.pit.brackets.married.ceilings}}; head of household "
    "ceilings: {{ca.pit.brackets.hoh.ceilings}}.",
    "**Supplemental pay** paid separately: bonuses and stock options {{ca.wh.supplemental.rate.bonus_stock_options}} %; other "
    "supplemental pay (overtime, commissions, severance, vacation pay) {{ca.wh.supplemental.rate.other}} %. Household employees: "
    "withholding only by agreement ({{ca.wh.household.by_agreement_only}}).",
    "California does not conform to the federal P.L. 119-21 deductions ({{ca.obbba.conforms}}) and taxes employer HSA "
    "contributions ({{ca.hsa.conforms}}); see CA.8.",
]
SECTION_TEXT[("CA", "2b")] = [
    "Sourcing: {{ca.nonres.sourcing}}.",
    "**Resident / non-resident matrix (California PIT)**",
    "| Income type | Resident | Non-resident |\n"
    "|---|---|---|\n"
    "| Regular salary | Method A or B on all wages; where another State withholds, withhold only the excess | Method A or B on California wages: all wages if working wholly in California; otherwise California working days / total working days (volume ratio for commissions) |\n"
    "| Annual bonus / supplemental pay | {{ca.wh.supplemental.rate.bonus_stock_options}} % (bonus) or aggregate | Same, on the California portion |\n"
    "| Severance | {{ca.wh.supplemental.rate.other}} % when paid separately, or aggregate | Same, on the California portion |\n"
    "| Equity (stock options) | {{ca.wh.supplemental.rate.bonus_stock_options}} % when paid separately, or aggregate | Same, on the California portion |\n"
    "| Benefits in kind | PIT wages per CA.8 (HSA taxable; group-term life above the excluded coverage reportable, not withheld) | Same, on the California portion |\n"
    "| Contractor pay | Out of scope | Out of scope |",
]
SECTION_TEXT[("CA", "3")] = [
    "Employer: UI on wages up to {{ca.sui.wage_base|v}} plus the Employment Training Tax ({{ca.ett.rate}} %). Employee: State "
    "Disability Insurance (SDI, which funds disability and paid family leave) at {{ca.sdi.employee.rate}} % on all wages, with no "
    "wage cap ({{ca.sdi.wage_cap.exists}}). A voluntary plan replaces SDI where approved (W-2 box 14 label {{ca.sdi.voluntary_plan.w2_box14_label}}).",
    "```\nca_sdi = period_SDI_wages x ca_sdi_employee_rate          # no annual cap\n```",
]
SECTION_TEXT[("CA", "OR")] = "EXAMPLE_CA"
SECTION_TEXT[("CA", "SP")] = [
    "- Domestic and household workers: UI and ETT above the quarterly cash-wage threshold; SDI above its own quarterly threshold; PIT only by agreement; the Lab. Code 226 statement does not apply.\n"
    "- Agricultural workers: UI, ETT and SDI apply; PIT withholding not required but PIT wages reportable (H-2A the same); overtime phase-in open (CA.1).\n"
    "- Minors: learner rate ({{ca.minwage.learner.percent}} % of minimum wage, any age); newspaper carriers under 18 excluded from UI, SDI and PIT.\n"
    "- Tipped employees: no tip credit.\n"
    "- Clergy: ministers and religious orders not subject to UI and SDI (elective) and PIT withholding not required; church employees not subject to UI and SDI, subject to PIT.\n"
    "- Students: own-school students, student nurses, young work-study students and organised-camp students not subject to UI and SDI, subject to PIT.\n"
    "- Non-resident aliens on F, J, M or Q visas: excluded from UI and SDI (CUIC 608); PIT subject unless a treaty covers State taxes.\n"
    "- Statutory employees: UI and SDI per DE 231TE/SE; commissioned authors no PIT withholding.\n"
    "- Government: UI subject; SDI only by election; PIT subject; elected officials, judiciary and National Guard not subject to UI and SDI.",
    SP_GAP,
]
SECTION_TEXT[("CA", "LG")] = ["The Lab. Code 2810.5 hire notice must be in the language the employer normally uses with the employee; the payslip is in English."]

# =====================================================================================  CO
INTRO["CO"] = state_intro("Colorado", "Classification: T4. Besides State withholding, occupational privilege taxes (OPT) are flat monthly amounts on separate city returns.")
SECTION_TEXT[("CO", "1")] = [
    "State minimum wage {{co.minwage.hourly|v}} for 2026; Denver {{co.local_minwage.denver.hourly|v}}. Overtime: {{co.overtime.rule}}. "
    "Other local minimum wages and the 2027 State rate are open (gaps below); the 2027 figures in the proposed order are not used.",
]
SECTION_TEXT[("CO", "2")] = [
    "**Method.** {{co.wh.method}}. Flat rate {{co.pit.rate.flat}} %. Wage base: {{co.wh.wages.conformity}}. The federal "
    "overtime deduction is not allowed for Colorado ({{co.wh.obbba_overtime_deduction.allowed}}).",
    "```\n"
    "annual_wages = period_wages x pay_periods\n"
    "taxable      = annual_wages - allowance        # DR 1098 allowance, or DR 0004 line 2 when filed\n"
    "period_tax   = max(0, taxable) x co_flat_rate / pay_periods + DR0004_line3\n"
    "```",
    "Allowance: single {{co.wh.std_allowance.dr1098.single|v}}; DR 0004 Table 1 (one job): single {{co.wh.dr0004.table1.single.1_job|v}}, "
    "head of household {{co.wh.dr0004.table1.hoh.1_job|v}}, married filing jointly {{co.wh.dr0004.table1.mfj.1_job|v}}.",
]
SECTION_TEXT[("CO", "2b")] = [
    "Rules: {{co.nonres.rules}}.",
    "**Resident / non-resident matrix (Colorado income tax)**",
    "| Income type | Resident | Non-resident |\n"
    "|---|---|---|\n"
    "| Regular salary | Flat-rate method (CO.2) on all wages except where another State requires withholding | Flat-rate method on Colorado-source wages, by days present |\n"
    "| Annual bonus / supplemental pay | No supplemental rate: aggregate with regular wages | Same, on the Colorado portion |\n"
    "| Severance | Aggregate with regular wages (wage base = federal withholding wages) | Same, on the Colorado portion |\n"
    "| Equity | Aggregate; federal classification of equity income in Annex FED (FED.2b) | Same, on the Colorado portion |\n"
    "| Benefits in kind | Federal exclusions flow through (wage-base conformity) | Same, on the Colorado portion |\n"
    "| Contractor pay | Out of scope | Out of scope |",
]
SECTION_TEXT[("CO", "2c")] = [
    "Occupational privilege taxes are flat monthly amounts, one employee and one employer amount per employee whose "
    "monthly earnings in the city reach the threshold, filed on the city's own return. Denver figures come from the 2025 tax "
    "guide (gap below).",
    "```\nif monthly_city_earnings >= city_threshold: employee_OPT = city_employee_amount; employer_OPT = city_employer_amount\n```",
]
SECTION_TEXT[("CO", "3")] = [
    "Employer-only UI on wages up to the base ({{co.sui.wage_base@2026-01-01|v}} for 2026; {{co.sui.wage_base@2027-01-01|v}} "
    "for 2027). FAMLI paid family and medical leave: {{co.famli.total.rate@2026-01-01}} % in 2026, split employee "
    "{{co.famli.employee.rate}} % and employer {{co.famli.employer.rate}} %; employers with up to "
    "{{co.famli.small_employer.max_employees}} employees owe only the employee share. 2027 total {{co.famli.total.rate@2027-01-01}} %; "
    "the 2027 split is a blocking gap. The FAMLI wage cap follows the federal OASDI base (Annex FED).",
]
SECTION_TEXT[("CO", "SP")] = [
    "- Domestic workers: UI follows the federal threshold.\n"
    "- Agricultural workers: longer overtime thresholds (CO.1 overtime rule); migratory-labourer disclosures in the worker's language (8-4-117).\n"
    "- Minors: {{co.minwage.minor_reduction.percent}} % below the State minimum for unemancipated minors ({{co.minwage.minor.hourly|v}} in 2026).\n"
    "- Tipped employees: tip credit {{co.minwage.tip_credit.max|v}}; State cash wage {{co.minwage.tipped.cash_wage|v}}; Denver {{co.local_minwage.denver.tipped_food_beverage|v}}; tips are the employee's property.\n"
    "- Clergy and statutory employees: no State rule beyond the federal one.\n"
    "- Students: UI excludes students at their own school (not student nurses).\n"
    "- Non-resident aliens: Colorado withholding applies without a valid TIN; FAMLI accepts ITINs.\n"
    "- Government: the Wage Act excludes the State, counties, municipalities and school districts; the Healthy Families and Workplaces Act includes them and excludes federal employers.\n"
    "- Military, military spouses and interstate transport workers: non-resident exemptions (CO.2b).\n"
    "- Multistate: the Healthy Families and Workplaces Act covers all employees working in Colorado; the UI other-State credit is open (CO.3).",
    SP_GAP,
]
SECTION_TEXT[("CO", "LG")] = ["The Healthy Families and Workplaces Act notice must be in English and in the first language of a qualifying share of the workforce; the COMPS order and poster also in Spanish; the payslip is in English."]

# =====================================================================================  CT
INTRO["CT"] = state_intro("Connecticut", "Classification: T3. Separate State withholding, UI and a separate Paid Leave contribution; no local wage tax.")
SECTION_TEXT[("CT", "1")] = [
    "State minimum wage {{ct.minwage.hourly@2026-01-01|v}} for 2026 and {{ct.minwage.hourly@2027-01-01|v}} for 2027, indexed "
    "{{ct.minwage.indexation}}.",
]
SECTION_TEXT[("CT", "2")] = [
    "**Method.** {{ct.wh.method}}. Certificate: {{ct.wh.certificate.form}}. Without a certificate: {{ct.wh.no_certificate.rate}} %. "
    "Supplemental pay: {{ct.wh.supplemental.method}}.",
    "```\n"
    "annual_wages = period_wages x pay_periods\n"
    "taxable      = annual_wages - TableA_exemption(code)\n"
    "annual_tax   = TableB(code)(taxable) + TableC_phaseout_addback + TableD_recapture\n"
    "annual_tax   = annual_tax x (1 - TableE_credit)\n"
    "period_tax   = annual_tax / pay_periods + CTW4_line2 - CTW4_line3\n"
    "```",
    "Table A exemption (maximum) by code: A {{ct.wh.table_a.exemption.a|v}}, B {{ct.wh.table_a.exemption.b|v}}, C "
    "{{ct.wh.table_a.exemption.c|v}}, F {{ct.wh.table_a.exemption.f|v}}. Table B rates {{ct.pit.rates}}; band breaks: codes "
    "A, D, F {{ct.pit.bracket_breaks.a_d_f}}; code B {{ct.pit.bracket_breaks.b}}; code C {{ct.pit.bracket_breaks.c}}. "
    "⚠️ RESEARCH-GAP (non-blocking): Tables C (phase-out add-back), D (recapture) and E (personal tax credit) of TPG-211 "
    "carry no facts key; the rules method cannot be computed until they are keyed (research request raised).",
    "**Method choice (configuration decision, 2026-11-02).** The Department of Revenue Services permits either the "
    "TPG-211 rules or its tables. The engine uses the DRS per-period withholding tables of IP 2026(1) (weekly, biweekly, "
    "semimonthly and monthly bands, one row per wage band and CT-W4 code, listed in CT.2 with their source), because the "
    "Department's worked examples are table-based and the tables reproduce them (CT.14). Wages above the table maximum of "
    "each period are computed with the TPG-211 rules, as the tables instruct. The TPG-211 rules above are shown as the "
    "reference method.",
    "Lump-sum pension withholding: {{ct.wh.pension_lump_sum.suspension}}.",
]
SECTION_TEXT[("CT", "2b")] = [
    "Rules: {{ct.nonres.rules}}.",
    "**Resident / non-resident matrix (Connecticut income tax)**",
    "| Income type | Resident | Non-resident |\n"
    "|---|---|---|\n"
    "| Regular salary | Rules or tables (CT.2) on all wages, prorated where another qualifying jurisdiction requires withholding | Rules or tables on Connecticut-service wages (CT-W4NA or records), otherwise all wages; day threshold and convenience rule in Annex MULTI |\n"
    "| Annual bonus / supplemental pay | Aggregate only (no flat rate) | Same, on the Connecticut portion |\n"
    "| Severance | Aggregate (federal wage definition) | Same, on the Connecticut portion |\n"
    "| Equity | Aggregate; federal classification of equity income in Annex FED (FED.2b) | Same, on the Connecticut portion |\n"
    "| Benefits in kind | Federal wage definition; Connecticut departures open (CT.8) | Same, on the Connecticut portion |\n"
    "| Contractor pay | Out of scope | Out of scope |",
]
SECTION_TEXT[("CT", "3")] = [
    "Employer UI on wages up to {{ct.sui.wage_base|v}} plus the fund-solvency rate ({{ct.sui.fund_solvency.rate}} %); no employee "
    "UI ({{ct.sui.employee.rate}} %). Connecticut Paid Leave: employee {{ct.pfml.employee.rate}} % on wages up to "
    "{{ct.pfml.wage_cap|v}}; coverage {{ct.pfml.multistate}}. No SDI or TDI.",
    "```\nct_pfml = min(period_CTPL_wages, max(0, ct_pfml_wage_cap - ytd_CTPL_wages)) x ct_pfml_employee_rate\n```",
]
SECTION_TEXT[("CT", "11")] = [
    "One index drives both the minimum wage and the UI wage base: the Employment Cost Index (wages and salaries, all "
    "civilian workers) for the twelve months to 30 June ({{ct.minwage.indexation}}). The minimum wage is rounded to the "
    "cent and the UI base to a round step stated in the source.",
]
SECTION_TEXT[("CT", "OR")] = [
    "Oracle values from the Department of Revenue Services informational publication IP 2026(1), examples 8 to 10 "
    "(table method), reproduced from the keyed per-period tables (CT.2).",
]
SECTION_TEXT[("CT", "SP")] = [
    "- Domestic workers: minimum wage and overtime exclude private-home domestic service except where FLSA covers it; UI above the quarterly cash-wage threshold; withholding voluntary (CT-941 HHE, CT-W3 HHE).\n"
    "- Agricultural workers: withhold where federal withholding applies; annual CT-941 option.\n"
    "- Minors: minor rate {{ct.minwage.minor.hourly|v}} in 2026; newspaper carriers under 18 excluded from UI.\n"
    "- Tipped employees: employer share {{ct.tipped.employer_share.hotel_restaurant|v}} (hotel and restaurant) and {{ct.tipped.employer_share.bartender|v}} (bartenders); no cannabis tip credit.\n"
    "- Clergy: UI excludes churches and ministers; withholding follows the federal definition.\n"
    "- Students: UI exclusions; resident assistants excluded from the minimum wage.\n"
    "- Non-resident aliens and statutory employees: no Connecticut rule beyond the federal one.\n"
    "- Government: State and municipal service UI-covered; Paid Leave excludes governments unless they opt in.\n"
    "- Military: non-resident military pay is not Connecticut wages; military spouses exempt on CT-W4.\n"
    "- Seasonal employees: excluded from sick leave.",
    SP_GAP,
]
SECTION_TEXT[("CT", "LG")] = ["The pay-code guide must be offered in English, Spanish and other common languages; the 31-57w(b) sick-leave notice in English and Spanish. The payslip is in English."]


# =====================================================================================  examples (C38)
def _d(x):
    return Decimal(str(x))


def _r2(x):
    return x.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def _fmt(x):
    return f"{x:,.2f}"


def _get(facts, key, frm=None):
    for f in facts:
        if f["key"] == key and (frm is None or f.get("effective_from") == frm):
            return f
    raise KeyError(key)


def example_al(facts, value_cell, tag):
    inp = _get(facts, "al.oracle.example.1.input")
    out = _get(facts, "al.oracle.example.1.withholding")
    m = re.search(r"weekly ([\d,]+\.\d+), federal withholding ([\d.]+)", inp["value"])
    wk, fit = _d(m.group(1).replace(",", "")), _d(m.group(2))
    n = Decimal(52)
    gross = wk * n
    sd = _d(_get(facts, "al.wh.std_deduction.married.min")["value"])
    pe = _d(_get(facts, "al.wh.personal_exemption.married")["value"])
    dep = _d(_get(facts, "al.wh.dependent.gi_to_50000")["value"])
    fit_a = fit * n
    taxable = gross - sd - fit_a - pe - 2 * dep
    c1 = _d(_get(facts, "al.pit.bracket.married.1.ceiling")["value"])
    c2 = _d(_get(facts, "al.pit.bracket.married.2.ceiling")["value"])
    r1, r2, r3 = (_d(_get(facts, f"al.pit.bracket.{i}.rate")["value"]) / 100 for i in (1, 2, 3))
    t1 = _r2(c1 * r1)
    t2 = _r2((c2 - c1) * r2)
    t3 = _r2((taxable - c2) * r3)
    annual = t1 + t2 + t3
    per = _r2(annual / n)
    assert per == _r2(_d(out["value"])), (per, out["value"])
    return [
        "Authority example (ADOR withholding booklet, rev. 01/2026), recomputed line by line from the keyed parameters. "
        "Rounding: half-up to the cent at each line.",
        f"Input: {tag(inp)}. Married status, two dependents, gross income in the lowest dependent band and above the "
        "standard-deduction phase-out range (so the minimum deduction applies).",
        "| Line | Base | Rate | Amount |\n|---|---|---|---|\n"
        f"| Annual wages | {_fmt(wk)} x 52 | — | {_fmt(gross)} |\n"
        f"| Standard deduction (married, minimum) | — | — | {value_cell(_get(facts, 'al.wh.std_deduction.married.min'))} |\n"
        f"| Annual federal income tax withheld | {_fmt(fit)} x 52 | — | {_fmt(fit_a)} |\n"
        f"| Personal exemption (married) | — | — | {value_cell(_get(facts, 'al.wh.personal_exemption.married'))} |\n"
        f"| Dependents | 2 x {value_cell(_get(facts, 'al.wh.dependent.gi_to_50000'))} | — | {_fmt(2 * dep)} |\n"
        f"| Taxable income | {_fmt(gross)} - {_fmt(sd)} - {_fmt(fit_a)} - {_fmt(pe)} - {_fmt(2 * dep)} | — | {_fmt(taxable)} |\n"
        f"| Band 1 | {value_cell(_get(facts, 'al.pit.bracket.married.1.ceiling'))} | {tag(_get(facts, 'al.pit.bracket.1.rate'))} % | {_fmt(t1)} |\n"
        f"| Band 2 | {_fmt(c2)} - {_fmt(c1)} = {_fmt(c2 - c1)} | {tag(_get(facts, 'al.pit.bracket.2.rate'))} % | {_fmt(t2)} |\n"
        f"| Band 3 | {_fmt(taxable)} - {_fmt(c2)} = {_fmt(taxable - c2)} | {tag(_get(facts, 'al.pit.bracket.3.rate'))} % | {_fmt(t3)} |\n"
        f"| Annual tax | {_fmt(t1)} + {_fmt(t2)} + {_fmt(t3)} | — | {_fmt(annual)} |\n"
        f"| Weekly withholding | {_fmt(annual)} / 52 | — | {value_cell(out)} |",
        "The computed weekly withholding equals the published value. If the employer rounds the period tax to the "
        "whole dollar, the weekly amount is the rounded figure.",
    ]


def example_ar(facts, value_cell, tag):
    inp = _get(facts, "ar.oracle.example.1.input")
    out = _get(facts, "ar.oracle.example.1.withholding")
    m = re.search(r"monthly ([\d,]+\.\d+), (\d+) exemptions", inp["value"])
    mo, ex = _d(m.group(1).replace(",", "")), int(m.group(2))
    gross = mo * 12
    sd = _d(_get(facts, "ar.wh.std_deduction")["value"])
    net = gross - sd
    mid = (net // 100) * 100 + 50
    b4 = _get(facts, "ar.pit.bracket.4.rate")
    s4 = _get(facts, "ar.pit.bracket.4.subtract")
    c3 = _d(_get(facts, "ar.pit.bracket.3.ceiling")["value"])
    c4 = _d(_get(facts, "ar.pit.bracket.4.ceiling")["value"])
    assert c3 < mid <= c4
    gross_tax = _r2(mid * _d(b4["value"]) / 100)
    tax = gross_tax - _d(s4["value"])
    tax_d = tax.quantize(Decimal("1"), rounding=ROUND_HALF_UP)
    cr = _d(_get(facts, "ar.wh.personal_credit.per_exemption")["value"])
    net_tax = tax_d - ex * cr
    per = _r2(net_tax / 12)
    assert per == _r2(_d(out["value"])), (per, out["value"])
    return [
        "Authority example (DFA Formula Method 2026), recomputed line by line from the keyed parameters. Rounding: annual "
        "tax half-up to the dollar (formula step), period amount half-up to the cent.",
        f"Input: {tag(inp)}.",
        "| Line | Calculation | Result |\n|---|---|---|\n"
        f"| Annual wages | {_fmt(mo)} x 12 | {_fmt(gross)} |\n"
        f"| Net taxable | {_fmt(gross)} - {value_cell(_get(facts, 'ar.wh.std_deduction'))} | {_fmt(net)} |\n"
        f"| Band midpoint | 100-dollar band of {_fmt(net)} | {_fmt(mid)} |\n"
        f"| Bracket 4 tax | {_fmt(mid)} x {tag(b4)} % - {value_cell(s4)} | {_fmt(gross_tax)} - {tag(s4)} = {_fmt(tax)} |\n"
        f"| Rounded to the dollar | — | {_fmt(tax_d)} |\n"
        f"| Less personal credits | {_fmt(tax_d)} - {ex} x {value_cell(_get(facts, 'ar.wh.personal_credit.per_exemption'))} | {_fmt(net_tax)} |\n"
        f"| Monthly withholding | {_fmt(net_tax)} / 12 | {value_cell(out)} |",
        "The computed monthly withholding equals the published value.",
    ]


def example_ca(facts, value_cell, tag):
    f_out = _get(facts, "ca.oracle.de44_f.monthly.withholding")
    e_out = _get(facts, "ca.oracle.de44.example_e.withholding_semimonthly")
    suite = _get(facts, "ca.oracle.suite")
    m = re.search(r"annual ([\d,]+) married (\d+) allowances", f_out.get("note", ""))
    annual, allow = _d(m.group(1).replace(",", "")), int(m.group(2))
    lie = _d(_get(facts, "ca.wh.low_income_exemption.married_2plus_hoh")["value"])
    sd = _d(_get(facts, "ca.wh.std_deduction.married_2plus_hoh")["value"])
    cred = _d(_get(facts, "ca.wh.allowance_credit.per_allowance")["value"])
    ceil = [_d(x.replace(",", "")) for x in re.findall(r"[\d,]{5,}", _get(facts, "ca.pit.brackets.married.ceilings")["value"])]
    r1 = _d(_get(facts, "ca.pit.bracket.single.1.rate")["value"]) / 100
    r2 = _d(_get(facts, "ca.pit.bracket.single.2.rate")["value"]) / 100
    assert annual > lie
    taxable = annual - sd
    assert ceil[0] < taxable <= ceil[1]
    base1 = _r2(ceil[0] * r1)
    excess = taxable - ceil[0]
    t2 = _r2(excess * r2)
    gross_tax = base1 + t2
    credits = allow * cred
    net = gross_tax - credits
    per = _r2(net / 12)
    assert per == _r2(_d(f_out["value"])), (per, f_out["value"])
    return [
        f"Oracle suite: {tag(suite)}. Example F is recomputed below from the keyed parameters (married, annual payroll "
        "expressed monthly). The married schedule is carried as one ceiling string; the first two married bands carry the "
        "single-schedule rates, as the published example shows. Rounding: half-up to the cent.",
        "| Line | Calculation | Result |\n|---|---|---|\n"
        f"| Annual wages | example input | {_fmt(annual)} |\n"
        f"| Low-income exemption test | {_fmt(annual)} > {value_cell(_get(facts, 'ca.wh.low_income_exemption.married_2plus_hoh'))} | taxable |\n"
        f"| Taxable income | {_fmt(annual)} - {value_cell(_get(facts, 'ca.wh.std_deduction.married_2plus_hoh'))} | {_fmt(taxable)} |\n"
        f"| Band 1 tax | {_fmt(ceil[0])} x {tag(_get(facts, 'ca.pit.bracket.single.1.rate'))} % | {_fmt(base1)} |\n"
        f"| Band 2 tax | ({_fmt(taxable)} - {_fmt(ceil[0])}) x {tag(_get(facts, 'ca.pit.bracket.single.2.rate'))} % = {_fmt(excess)} x rate | {_fmt(t2)} |\n"
        f"| Gross annual tax | {_fmt(base1)} + {_fmt(t2)} | {_fmt(gross_tax)} |\n"
        f"| Allowance credits | {allow} x {value_cell(_get(facts, 'ca.wh.allowance_credit.per_allowance'))} | {_fmt(credits)} |\n"
        f"| Annual tax | {_fmt(gross_tax)} - {_fmt(credits)} | {_fmt(net)} |\n"
        f"| Monthly withholding | {_fmt(net)} / 12 | {value_cell(f_out)} |",
        "The computed monthly withholding equals the published value. Example E (semi-monthly) published value: "
        f"{value_cell(e_out)}; its inputs are not keyed, so it is reproduced in Module 12 rather than here.",
    ]


EXAMPLES = {"EXAMPLE_AL": example_al, "EXAMPLE_AR": example_ar, "EXAMPLE_CA": example_ca}


# =====================================================================================  C38 table checks
def c38_checks(unit, facts):
    out = []
    if unit == "FED":
        for st in ("mfj", "single", "hoh"):
            rows = {}
            for f in facts:
                m = re.match(rf"^fed\.fit\.standard\.{st}\.bracket\.(\d+)\.(floor|rate|cumulative_tax)$", f["key"])
                if m:
                    rows.setdefault(int(m.group(1)), {})[m.group(2)] = _d(f["value"])
            ok = True
            for i in sorted(rows)[1:]:
                exp = rows[i - 1]["cumulative_tax"] + (rows[i]["floor"] - rows[i - 1]["floor"]) * rows[i - 1]["rate"] / 100
                if _r2(exp) != _r2(rows[i]["cumulative_tax"]):
                    ok = False
                    out.append(f"FED {st} bracket {i}: expected {exp} got {rows[i]['cumulative_tax']}")
            out.append(f"FED standard {st}: cumulative tax column {'OK' if ok else 'MISMATCH'} ({len(rows)} rows)")
    if unit == "AR":
        rows = {}
        for f in facts:
            m = re.match(r"^ar\.pit\.bracket\.(\d+)\.(ceiling|rate|subtract)$", f["key"])
            if m:
                rows.setdefault(int(m.group(1)), {})[m.group(2)] = _d(f["value"])
        rows[1]["rate"] = Decimal(0)
        rows[1]["subtract"] = Decimal(0)
        acc = Decimal(0)
        ok = True
        for i in sorted(rows)[1:]:
            acc = acc + rows[i - 1]["ceiling"] * (rows[i]["rate"] - rows[i - 1]["rate"]) / 100
            if _r2(acc) != rows[i]["subtract"]:
                ok = False
                out.append(f"AR bracket {i}: expected {_r2(acc)} got {rows[i]['subtract']}")
        out.append(f"AR subtraction column {'OK' if ok else 'MISMATCH'}")
    return out


# =====================================================================================  sections without facts
SECTION_TEXT[("AK", "11")] = [
    "The minimum wage is indexed to the Anchorage CPI-U from 2028 (no indexed value yet). The exempt-salary threshold and "
    "the school-bus driver rate follow the minimum wage by statutory multiple (AK.1). The UI wage base is set yearly from "
    "the State average annual wage (next-year base not yet published, AK.3). Garnishment exemptions follow the CPI "
    "(AS 09.38.115).",
]
SECTION_TEXT[("AL", "10")] = [
    "No State prevailing-wage law; federal Davis-Bacon only (Annex FED). Ala. Code 25-7-42 bars local labour-peace and "
    "project-labour-agreement mandates.",
]
SECTION_TEXT[("AL", "11")] = [
    "Nothing is indexed: the UI base is fixed in statute, withholding amounts are statutory and there is no State minimum "
    "wage. Only the yearly UC rate schedule and shared-cost rate change (25-4-54), notified per employer on UC-216.",
]
SECTION_TEXT[("AL", "12")] = [
    "Data Breach Notification Act of 2018 (ch. 8-38). No statute requiring SSN truncation on pay statements was found in the research.",
]
SECTION_TEXT[("AR", "6")] = [
    "No paid-sick-leave statute and no PFML in the research; vacation is a matter of written policy. Jury, voting and "
    "military leave are open (gap below).",
]
SECTION_TEXT[("AR", "8")] = [
    "Arkansas withholding wages exclude the federal exclusions for combat pay, cafeteria plans, IRAs "
    "and 401(k), 403(b), 408(k), 408(p) and 457 deferrals; non-cash wages are valued at fair market value; "
    "reported tips are wages. Employer HSA contributions outside a cafeteria plan, transit benefits and group-term life "
    "are open (gap below).",
]
SECTION_TEXT[("AR", "11")] = [
    "The minimum wage is not indexed; the UI base is fixed in statute; withholding amounts are republished by legislation "
    "without an index factor.",
]
SECTION_TEXT[("AZ", "13")] = [
    "From 2027: State minimum wage {{az.minwage.hourly@2027-01-01|v}}, Tucson {{az.local_minwage.tucson.hourly@2027-01-01|v}}, "
    "Flagstaff {{az.local_minwage.flagstaff.hourly@2027-01-01|v}}; UI Operating Fund {{az.ui_operating_fund.rate_of_ui_liability}} % "
    "of UI liability. Arizona conforms to the Internal Revenue Code as of {{az.irc_conformity_date}}. The 2026 agency "
    "bulletins are not swept (gap below).",
]
SECTION_TEXT[("CA", "11")] = [
    "The minimum wage is CPI-indexed (the Department of Finance certifies by 1 August, Lab. Code 1182.12(d)); the "
    "exempt-salary threshold follows the minimum wage by statutory multiple; the PIT tables are indexed yearly in DE 44; "
    "the UI base is fixed in statute ({{ca.sui.wage_base|v}}); the SDI rate is set yearly; meal and lodging values are set yearly.",
]
SECTION_TEXT[("CO", "11")] = [
    "The State minimum wage is CPI-indexed yearly (PAY CALC Order); Denver indexes on the local CPI-W; the exempt-salary "
    "thresholds are set yearly; the UI wage base follows statutory steps ({{co.sui.wage_base@2026-01-01|v}} for 2026, "
    "{{co.sui.wage_base@2027-01-01|v}} for 2027); the FAMLI rate is set yearly within a statutory cap; OPT amounts are fixed by ordinance.",
]
SECTION_TEXT[("CO", "12")] = [
    "The State data-protection statutes (C.R.S. 6-1-713, 6-1-713.5, 6-1-716) are open (gap below). No duty to truncate "
    "the SSN on the pay statement was found; the statement may show the SSN instead of the name (8-4-103(4)(e)).",
]
SECTION_TEXT[("CT", "8")] = [
    "Withholding follows the federal wage definition; no Connecticut departure was found for 401(k), cafeteria-plan, HSA, "
    "transit or group-term-life amounts (medium confidence; gap below). Paid Leave wages: {{ct.pfml.wages.fica_basis}}. "
    "New 2026 subtractions operate at assessment level, not in withholding.",
]
SECTION_TEXT[("CT", "13")] = [
    "In force in 2026: paid sick leave for employers with {{ct.leave.sick.coverage_threshold_employees@2026-01-01}} or more "
    "employees; the pay-code guide duty (CT.4); the minor-league baseball exclusion and the end of the cannabis tip credit; "
    "optional UI report fields. Enacted for 2027: paid sick leave from {{ct.leave.sick.coverage_threshold_employees@2027-01-01}} "
    "employee; minimum wage {{ct.minwage.hourly@2027-01-01|v}}; double damages; UI shared-work non-charging; prevailing-wage "
    "records. The lump-sum pension withholding suspension ends with 2026 (CT.2). Public Acts known only from legislative "
    "summaries are listed as a gap below.",
]
