# -*- coding: utf-8 -*-
"""Federal-layer country additions of the US Wage Type Catalogue (codes US-nnn, allocated in definition order).

Every figure is written through W.val() / W.line() (tags); the treatment sentences carry the register id of the fact
that states them. Rows that serve a Report Spec payroll-result row say so in column D ("Serves: ...") and the
reconciliation (wtc_recon.py) proves it both ways.
"""
import wtc_common as W
import wtc_profiles as P
from wtc_why import WHY
from wtc_model import YES, NO, YN, NA, X

val, line, rid, dd = W.val, W.line, W.rid, W.dd

# DD elements (verified against the approved DD at import time: F25)
D_PAYFREQ = dd("Pay frequency")
D_W4_STATUS = dd("Form W-4 filing status (Step 1(c))")
D_W4_JOBS = dd("Form W-4 multiple jobs or spouse works (Step 2)")
D_W4_DEP = dd("Form W-4 dependents and other credits (Step 3)")
D_W4_OTHER = dd("Form W-4 other income (Step 4(a))")
D_W4_DED = dd("Form W-4 deductions (Step 4(b))")
D_W4_EXTRA = dd("Form W-4 extra withholding (Step 4(c))")
D_W4_EXEMPT = dd("Form W-4 exempt from withholding")
D_NRA = dd("Nonresident alien flag")
D_NRA_W4 = dd("Nonresident alien Form W-4 completed per Notice 1392")
D_8233 = dd("Form 8233 treaty exemption claimed")
D_VISA = dd("Nonresident alien visa class")
D_PURPOSE = dd("Work carries out the purpose of admission")
D_TOTAL_CTRY = dd("Totalization agreement country")
D_TOTAL_EX = dd("Totalization agreement FICA exemption")
D_SPECIAL = dd("Employee special population category")
D_HH_FIT = dd("Household employee: federal income tax withholding agreement")
D_TTOC1 = dd("Primary Treasury Tipped Occupation Code")
D_TTOC2 = dd("Secondary Treasury Tipped Occupation Code")
D_ACA_STATUS = dd("ACA monthly employee status")
D_ACA_OFFER = dd("ACA offer of coverage code (line 14), per month")
D_ACA_SAFE = dd("ACA safe harbor and relief code (line 16), per month")
D_HIRE = dd("Date services first performed (hire date)")
D_SEP = dd("Date of separation (termination date)")
D_RATE_BASIS = dd("Rate-of-pay basis")
D_FTPT = dd("Full-time or part-time status")
D_WORK_STATE = dd("Work State")
D_RES_STATE = dd("Residence State")
D_UI_STATE = dd("Unemployment insurance State")
D_TRANSPORT = dd("Interstate transport worker type")
D_MILSPOUSE = dd("Military spouse residence election")
D_VACFORF = dd("Vacation forfeiture policy acknowledged in writing")
D_FINALPAY = dd("Final wage payment date")
D_IWO = dd("Income withholding order address")
D_W2_3PSP = dd("W-2 third-party sick pay indicator")
D_W2_EMPCODE = dd("W-2 employment code")
D_NO_SSMED = dd("No social security or Medicare wages indicator")
D_FED_DEP = dd("Federal depositor status")
D_RETURN_TYPE = dd("Federal employment tax return type")
D_STATE_CERT = dd("State withholding certificate on file")
D_SEASONAL = dd("Seasonal employer indicator")
D_W2_KIND = dd("W-2 kind of employer")

SRC_FIT = "IRS Publication 15-T (2026), Federal Income Tax Withholding Methods"

IN_SCOPE = dict(fit="Employee taxes withheld: FIT, OASDI, Medicare, Additional Medicare, State and local income tax")


def add_federal(reg):
    A = reg.add
    B = P.B()

    # ------------------------------------------------------------------ income tax withholding ---
    A("fit_reg", "Federal income tax withholding (FIT) - regular wages", "Tax",
      ("Federal income tax withheld from the employee on regular wages. "
       + P.txt_fit() +
       f" Computation: annualise the period wages with the number of pay periods of the {D_PAYFREQ}, apply the standard or the "
       f"Step-2-checked schedule of the percentage method, and divide the annual tax by the same number of periods. "
       f"{line('fed.fit.worksheet1a.line1g.mfj', 'Worksheet 1A line 1g, married filing jointly')}; "
       f"{line('fed.fit.worksheet1a.line1g.other', 'Worksheet 1A line 1g, all other filing statuses')}. "
       f"{line('fed.fit.standard.single.thresholds', 'Standard schedule bracket thresholds, single')}; "
       f"{line('fed.fit.rates', 'bracket rates (percent)')}. "
       f"Pre-2020 Form W-4 allowance value: {val('fed.fit.allowance.pre2020_value')} [{rid('fed.fit.allowance.pre2020_value')}]. "
       f"No usable certificate: {val('fed.w4.default_no_certificate')} [{rid('fed.w4.default_no_certificate')}]. "
       f"Extra payday: {val('fed.fit.extra_pay_period.rule')} [{rid('fed.fit.extra_pay_period.rule')}]. "
       f"Oracle (Pub. 15-T 2026 worked examples): {line('fed.oracle.pub15t.nra_example.withholding', 'nonresident alien example result')}; "
       f"{line('fed.oracle.pub15t.tribal_example.withholding', 'tribal example result')}. "
       f"Inputs: {D_W4_STATUS}, {D_W4_JOBS}, {D_W4_DEP}, {D_W4_OTHER}, {D_W4_DED}, {D_W4_EXTRA}, {D_W4_EXEMPT}, {D_PAYFREQ}. "
       + W.ug("fed.fit.2027.tables", WHY["fed.fit.2027.tables"]) +
       ". Declared: W-2 box 2 and Form 941 line 3 (Report Specifications US-SSA-001 and US-IRS-001). "
       "Two-level rule: the federal deduction for qualified tips and overtime operates at assessment and does not change this withholding "
       f"[{rid('fed.obbba.tips_deduction.level')}]."),
      tax_code="US-TX-04", side="EE", rep="W-2 box 2; Form 941 line 3; Form 944 line 2", payslip=True,
      inputs=[D_W4_STATUS, D_W4_JOBS, D_W4_DEP, D_W4_OTHER, D_W4_DED, D_W4_EXTRA, D_W4_EXEMPT, D_PAYFREQ],
      legal=["US-FEDS5-001", "US-FED-001", "US-FEDQ3-004", "US-FEDQ1-007", "US-FED-027"], fam="fed_tax")

    A("fit_supp22", "FIT on supplemental wages - optional flat rate", "Tax",
      (f"Optional flat-rate withholding on separately identified supplemental wages (bonus, commission, and other payments listed on the "
       f"supplemental wage rows): {val('fed.fit.supplemental.flat_rate')} [{rid('fed.fit.supplemental.flat_rate')}]. "
       f"The aggregate method (add the supplemental wages to the regular wages of the period and withhold on the total with the "
       f"{X('fit_reg')} method) is the alternative; one method is used consistently per payment. Nonresident alien add-on applies to flat-rate "
       f"supplemental wages: {val('fed.fit.nra_addon.applies_to_supplemental_flat')} [{rid('fed.fit.nra_addon.applies_to_supplemental_flat')}]. "
       f"Inputs: {D_W4_STATUS}, {D_NRA}."),
      tax_code="US-TX-04", side="EE", rep="W-2 box 2; Form 941 line 3", payslip=True,
      inputs=[D_W4_STATUS, D_NRA], legal=["US-FEDS5-003"], fam="fed_tax")

    A("fit_supp37", "FIT on supplemental wages - mandatory rate above the annual threshold", "Tax",
      (f"Mandatory flat-rate withholding on the part of supplemental wages paid in the calendar year to the employee that is above "
       f"{val('fed.fit.supplemental.mandatory_threshold')}: {val('fed.fit.supplemental.mandatory_rate')} "
       f"[{rid('fed.fit.supplemental.mandatory_rate')}]. Accumulator: year-to-date supplemental wages per employee (the Subject to Tax "
       f"and Special Tax flags of the supplemental wage rows plus the year-to-date mechanism). An 83(i) inclusion is withheld at "
       f"{val('fed.equity.83i.withholding_rate')} [{rid('fed.equity.83i.withholding_rate')}]."),
      tax_code="US-TX-04", side="EE", rep="W-2 box 2; Form 941 line 3", payslip=True,
      inputs=[D_W4_STATUS], legal=["US-FEDS5-003", "US-FEDQ1-001"], fam="fed_tax")

    A("fit_nra_addon", "FIT nonresident alien add-on to wages for the withholding computation", "Intermediary",
      (f"Amount added to the period wages of a nonresident alien before the percentage method is applied (Pub. 15-T). Table 2 (employee "
       f"who has submitted Form W-4): weekly {val('fed.fit.nra.addon.table2.weekly')}, biweekly {val('fed.fit.nra.addon.table2.biweekly')}, "
       f"semimonthly {val('fed.fit.nra.addon.table2.semimonthly')}, monthly {val('fed.fit.nra.addon.table2.monthly')}, annual "
       f"{val('fed.fit.nra_addon.table2.annual')} [{rid('fed.fit.nra.addon.table2.weekly')}]. Table 1 (no Form W-4): weekly "
       f"{val('fed.fit.nra.addon.table1.weekly')}, annual {val('fed.fit.nra_addon.table1.annual')} [{rid('fed.fit.nra.addon.table1.weekly')}]. "
       f"Form W-4 rule: {val('fed.fit.nra.w4_rule')} [{rid('fed.fit.nra.w4_rule')}]. The add-on is used for the computation only; it is not "
       f"wages and it is not applied to flat-rate supplemental wages. Oracle: the Pub. 15-T 2026 nonresident alien example "
       f"{val('fed.oracle.pub15t.nra_example.withholding')} [{rid('fed.oracle.pub15t.nra_example.withholding')}]. "
       f"Inputs: {D_NRA}, {D_NRA_W4}, {D_PAYFREQ}."),
      tax_code="US-TX-04", side="NONE", inputs=[D_NRA, D_NRA_W4, D_PAYFREQ], legal=["US-FEDS5-002", "US-FEDS5-015", "US-FEDS5-016"],
      fam="fed_tax")

    # ------------------------------------------------------------------ social security / Medicare ---
    A("oasdi_er", "Social security tax (OASDI) - employer", "Employer Contribution",
      (f"Employer share of the social security tax: {val('fed.fica.oasdi.rate.employer')} of social security wages up to the annual wage base "
       f"{val('fed.fica.oasdi.wage_base')} per employee per employer [{rid('fed.fica.oasdi.rate.employer')}]. Accumulator: year-to-date "
       f"social security wages of the employee with this employer (Subject to Social Insurance Q1 plus the year-to-date mechanism). "
       f"Computation: the lesser of (remaining annual maximum) and (rate x period wages), never an annualise-then-divide shortcut. "
       f"Exempt: {val('fed.fica.nra.fjmq_exempt.scope')} [{rid('fed.fica.nra.fjmq_exempt.scope')}]; {val('fed.fica.totalization.exemption_rule')} "
       f"[{rid('fed.fica.totalization.exemption_rule')}, US-FEDR2-004]. Inputs: {D_VISA}, {D_PURPOSE}, {D_TOTAL_CTRY}, {D_TOTAL_EX}."),
      tax_code="US-TX-05", side="ER", rep="Form 941 line 5a; Form 944 line 4a", inputs=[D_VISA, D_PURPOSE, D_TOTAL_CTRY, D_TOTAL_EX, D_NRA],
      legal=["US-FEDS5-005", "US-FEDS5-016", "US-FEDR2-003", "US-FEDR2-004"], fam="fed_tax")

    A("medicare_ee", "Medicare tax - employee", "Tax",
      (f"Employee Medicare tax: {val('fed.fica.medicare.rate.employee')} of all Medicare wages; wage base capped: "
       f"{val('fed.fica.medicare.wage_base.capped')} [{rid('fed.fica.medicare.rate.employee')}]. "
       f"Declared: W-2 box 6 with the Additional Medicare Tax; Form 941 line 5c."),
      tax_code="US-TX-04", side="EE", rep="W-2 box 6; Form 941 line 5c", payslip=True,
      inputs=[D_NO_SSMED], legal=["US-FEDS5-005"], fam="fed_tax")

    A("medicare_er", "Medicare tax - employer", "Employer Contribution",
      (f"Employer Medicare tax: {val('fed.fica.medicare.rate.employer')} of all Medicare wages, no wage base [{rid('fed.fica.medicare.rate.employer')}]. "
       f"Declared: Form 941 line 5c; Form 944 line 4c."),
      tax_code="US-TX-05", side="ER", rep="Form 941 line 5c", inputs=[D_NO_SSMED], legal=["US-FEDS5-005"], fam="fed_tax")

    A("addl_medicare_ee", "Additional Medicare Tax - employee", "Tax",
      (f"Additional Medicare Tax withheld from the employee only: {val('fed.fica.addl_medicare.rate')} of Medicare wages above "
       f"{val('fed.fica.addl_medicare.withholding_threshold')} paid in the calendar year "
       f"[{rid('fed.fica.addl_medicare.rate')}]. Accumulator: year-to-date Medicare wages. Declared: W-2 box 6; "
       f"Form 941 line 5d."),
      tax_code="US-TX-04", side="EE", rep="W-2 box 6; Form 941 line 5d", payslip=True, inputs=[D_NO_SSMED],
      legal=["US-FEDS5-005"], fam="fed_tax")

    # ------------------------------------------------------------------------------- FUTA ---
    A("futa_er", "Federal unemployment tax (FUTA) - employer", "Employer Contribution",
      (f"Employer-only federal unemployment tax: gross rate {val('fed.futa.rate.gross')} less the credit for State contributions, "
       f"net {val('fed.futa.rate.net')}, on the first {val('fed.futa.wage_base')} of wages per employee per year [{rid('fed.futa.wage_base')}]. "
       f"Accumulator: year-to-date FUTA wages per employee. Exempt from FUTA (nonresident alien in F-1, J-1, M-1 or Q status): "
       f"{val('fed.futa.nra.fjmq_exempt')} [{rid('fed.futa.nra.fjmq_exempt')}]. Declared: Form 940 and its Schedule A (Report Specification US-IRS-004)."),
      tax_code="US-TX-05", side="ER", rep="Form 940 lines 3 to 7", inputs=[D_VISA, D_PURPOSE],
      legal=["US-FED-007", "US-FEDS5-016"], fam="fed_tax")

    A("futa_credit_reduction", "FUTA credit reduction - employer", "Employer Contribution",
      (f"Additional FUTA owed by the employer in a credit reduction State on FUTA wages paid there: potential 2026 reduction California "
       f"{val('fed.futa.credit_reduction.ca.potential.rate')} and U.S. Virgin Islands {val('fed.futa.credit_reduction.vi.potential.rate')} "
       f"[{rid('fed.futa.credit_reduction.ca.potential.rate')}]. It is final only after the Department of Labor determination: "
       + W.ug("fed.futa.credit_reduction.2026.final", WHY["fed.futa.credit_reduction.2026.final"]) +
       ". Declared: Form 940 Schedule A, one row per State of coverage."),
      tax_code="US-TX-05", side="ER", rep="Form 940 Schedule A; line 9 and line 11", legal=["US-FEDS5-009"], fam="fed_tax")

    # ------------------------------------------------------------------ bases and accumulators ---
    mk = lambda sym, name, expl, rep="", legal=("US-FEDS5-007",), inputs=(), cat="Base": A(sym, name, cat, expl, tax_code="US-NA", side="NONE", rep=rep, inputs=inputs, legal=list(legal), fam="fed_base")  # noqa: E731

    mk("base_fit", "Federal taxable wages (FIT wage accumulator)",
       ("Accumulator of the wages that enter the federal income tax base: every earning row whose Subject to Tax flag is Yes, less the "
        "pre-tax deductions whose flag is No. Per pay period, quarter and year. Serves: the federal quarterly and annual returns and the "
        "annual wage statement, line wages, tips and other compensation (W-2 box 1)."),
       rep="W-2 box 1; Form 941 line 2; Form 944 line 1")
    mk("base_oasdi", "Social security wages (capped accumulator)",
       (f"Accumulator of the wages whose Subject to Social Insurance Q1 flag is Yes, capped per employee per year at the wage base "
        f"{val('fed.fica.oasdi.wage_base')} [{rid('fed.fica.oasdi.wage_base')}]; W-2 box 3 excludes social security tips (box 7). Year-to-date per "
        f"employee and employer."),
       rep="W-2 box 3; Form 941 line 5a column 1")
    mk("base_oasdi_tips", "Social security tips (accumulator)",
       ("Accumulator of the cash tips that are social security wages (box 7 of the annual wage statement; Form 941 line 5b), capped together "
        "with the social security wages at the same wage base."), rep="W-2 box 7; Form 941 line 5b")
    mk("base_medicare", "Medicare wages and tips (uncapped accumulator)",
       "Accumulator of the wages and tips whose Subject to Social Insurance Q2 flag is Yes; no cap.", rep="W-2 box 5; Form 941 line 5c column 1")
    mk("base_addl_medicare", "Wages subject to Additional Medicare Tax withholding (accumulator)",
       (f"Accumulator of the Medicare wages paid in the calendar year above {val('fed.fica.addl_medicare.withholding_threshold')} "
        f"[{rid('fed.fica.addl_medicare.withholding_threshold')}] on which the Additional Medicare Tax was withheld."),
       rep="Form 941 line 5d; Form 944 line 4d; Form 943 line 6")
    mk("base_futa_gross", "FUTA total payments to employees (accumulator)",
       "Accumulator of all payments to employees in the year, whether or not subject to FUTA. Form 940 line 3.", rep="Form 940 line 3",
       legal=("US-FED-007",))
    mk("base_futa_exempt", "FUTA payments exempt from tax (accumulator)",
       "Accumulator of the payments in the year whose Subject to Social Insurance Q3 flag is No (Form 940 line 4).", rep="Form 940 line 4",
       legal=("US-FED-007",))
    mk("base_futa_excess", "FUTA payments above the wage base per employee (accumulator)",
       (f"Accumulator of the payments to each employee in the year in excess of {val('fed.futa.wage_base')} [{rid('fed.futa.wage_base')}] "
        f"(Form 940 line 5)."), rep="Form 940 line 5", legal=("US-FED-007",))
    mk("base_futa", "FUTA taxable wages (accumulator)",
       (f"Accumulator of the wages up to {val('fed.futa.wage_base')} per employee per year on which FUTA is due; also kept per State of unemployment "
        f"insurance coverage ({D_UI_STATE}) for Schedule A."), rep="Form 940 line 7; Schedule A", legal=("US-FED-007",), inputs=[D_UI_STATE])
    mk("liab_fed", "Federal employment tax liability per payment date",
       ("Intermediary: federal income tax withheld plus employee and employer social security and Medicare tax, accumulated per payment date, "
        "per month and per quarter. It drives the deposit schedule and the Schedule B daily liability lines; it is a payroll result, not a payment."),
       rep="Form 941 line 16 and Schedule B; Form 944 line 13; Form 943 line 17", cat="Intermediary",
       inputs=[D_FED_DEP, D_RETURN_TYPE])
    mk("liab_futa", "FUTA liability per quarter",
       "Intermediary: FUTA computed on the quarter wages, accumulated per quarter for the Form 940 part 5 lines.", rep="Form 940 part 5",
       legal=("US-FED-007",), cat="Intermediary")
    mk("dep_fed", "Federal tax deposits made (payment register)",
       ("Intermediary: the register of federal tax deposits made per period and their confirmation numbers; it is a payment record that the "
        "return reads next to the liability. The authorisation for the filing provider and the deposit schedule are outside the catalogue."),
       rep="Form 941 line 13; Form 944 line 10; Form 940 line 13", cat="Intermediary", inputs=[D_FED_DEP])
    mk("adj_fed_period", "Employment tax adjustments of the period (fractions of cents, sick pay, tips and group-term life)",
       ("Intermediary: the current-period adjustments carried on the quarterly, annual and agricultural returns (fractions of cents, third-party "
        "sick pay, tips and group-term life tax adjustments, prior-period corrections). Kept per period so that the return line equals the sum "
        "of the postings."),
       rep="Form 941 lines 7 to 9; Form 944 line 6; Form 943 line 10; Form 941-X line 15", cat="Intermediary")
    mk("cr_qsbpt", "Qualified small business payroll tax credit (research credit against payroll tax)",
       "Intermediary: the credit elected on Form 6765 and taken against the employer share of social security tax. Per quarter and year.",
       rep="Form 941 line 11; Form 944 line 8; Form 943 line 12; Form 941-X line 16", cat="Intermediary")
    mk("tax_3121q", "Section 3121(q) notice and demand tax on unreported tips",
       "Intermediary: the tax assessed on unreported tips after an IRS notice and demand; reported on its own line.",
       rep="Form 941 line 5f; Form 941-X line 14", cat="Intermediary")
    mk("add_wages_941x", "Special additions to wages for federal income tax, social security and Medicare (correction returns)",
       ("Intermediary: special additions to wages on a correction return (Form 941-X lines 19 to 22) and the sick and family leave wages of the "
        "periods that the form still lists. Read from the correction register, not from the current payroll."),
       rep="Form 941-X lines 9, 10 and 19 to 22", cat="Intermediary")
    mk("futa_late", "FUTA - State unemployment tax paid late or excluded payments",
       "Intermediary: the Form 940 lines for excluded payments and State unemployment tax paid after the due date (line 10), per year.",
       rep="Form 940 line 10", cat="Intermediary", legal=("US-FED-007",))
    mk("hh_cash", "Household cash wages (annual and quarterly accumulators)",
       (f"Accumulator for a household employee: cash wages per employee per year for the social security and Medicare test "
        f"({val('fed.household.fica_cash_threshold')}) and cash wages per quarter for the FUTA test ({val('fed.household.futa_quarter_threshold')}) "
        f"[{rid('fed.household.fica_cash_threshold')}]. Federal income tax is withheld only by agreement: {val('fed.household.fit.withholding')} "
        f"[{rid('fed.household.fit.withholding')}]. State withholding: {val('special_population.household.state_withholding')} "
        f"[{rid('special_population.household.state_withholding')}]. Inputs: {D_SPECIAL}, {D_HH_FIT}."),
       rep="Schedule H; W-2 box 1", legal=("US-FEDS5-029",), inputs=[D_SPECIAL, D_HH_FIT])
    mk("treaty_exempt", "Treaty-exempt wages of a nonresident alien (accumulator)",
       (f"Accumulator of the wages exempt under a tax treaty claimed on Form 8233; reported on Form 1042-S, not in W-2 box 1: "
        f"{val('fed.fit.treaty_exempt_wages.reporting')} [{rid('fed.fit.treaty_exempt_wages.reporting')}]. Inputs: {D_8233}, {D_NRA}."),
       rep="Form 1042-S", legal=("US-FEDS5-016",), inputs=[D_8233, D_NRA])
    mk("hours_worked", "Hours worked (unit of measure of the earning wage types)",
       ("Intermediary: hours accumulated from the time data of every earning wage type that carries hours as its unit of measure, per employee "
        "per period; read by the State unemployment and programme returns that ask for hours. It is a quantity, not an amount."),
       rep="State UI and programme returns (hours)", cat="Intermediary", inputs=[D_RATE_BASIS, D_FTPT])

    # ------------------------------------------------------------------ flags driving the treatment ---
    fl = lambda sym, name, expl, inputs=(), legal=(), rep="": A(sym, name, "Flag", expl, tax_code="US-NA", side="NONE", rep=rep,  # noqa: E731
                                                                  inputs=list(inputs), legal=list(legal), fam="flag")
    fl("flag_paid12", "Employee paid in the pay period that includes the 12th (count flag)",
       ("Flag per employee and month: 1 when the employee received pay for the pay period that includes the 12th day of the month. The "
        "quarterly return counts the flags of the last month of the quarter; the agricultural annual return counts the period including 12 March."),
       rep="Form 941 line 1; Form 943 line 1", legal=["US-FEDS5-007"], inputs=[D_HIRE, D_SEP, D_PAYFREQ])
    fl("flag_aca", "ACA monthly status flag (full-time status, offer of coverage and employee required contribution)",
       (f"Flag per employee and month feeding the health coverage statements: full-time status, offer of coverage and safe harbour codes "
        f"({D_ACA_STATUS}, {D_ACA_OFFER}, {D_ACA_SAFE}). The employee required contribution of the lowest-cost self-only coverage is tested "
        f"against the affordability rate {val('fed.aca.affordability.rate')} [{rid('fed.aca.affordability.rate')}] of the employee income measure "
        f"chosen by the safe harbour code; the monthly employee share comes from the health premium deduction 21610."),
       rep="Form 1095-C lines 14 to 16; Form 1094-C", legal=["US-FEDS5-007"], inputs=[D_ACA_STATUS, D_ACA_OFFER, D_ACA_SAFE])
    fl("flag_nra", "Nonresident alien flag (withholding treatment)",
       (f"Flag that switches the nonresident alien rules: the add-on to wages ({X('fit_nra_addon')}), the FICA exemption for F-1, J-1, M-1 and Q "
        f"statuses ({X('oasdi_er')}), the treaty exemption ({X('treaty_exempt')}). Other visa categories: {val('fed.fica.nra.other_visas.liable')} "
        f"means the pay is liable for FICA [{rid('fed.fica.nra.other_visas.liable')}]. Resident equity and fringe benefit rules differ for this flag; see the "
        f"equity rows. Inputs: {D_NRA}, {D_VISA}."),
       inputs=[D_NRA, D_VISA, D_NRA_W4], legal=["US-FEDS5-016", "US-FEDS5-002"])
    fl("flag_minister", "Minister of religion flag (common-law employee)",
       f"{val('fed.minister.withholding')} [{rid('fed.minister.withholding')}]. State withholding: {val('special_population.minister.ms_or')} "
       f"[{rid('special_population.minister.ms_or')}]. Inputs: {D_SPECIAL}.",
       inputs=[D_SPECIAL], legal=["US-FED-030"])
    fl("flag_statutory_emp", "Statutory employee flag",
       f"{val('fed.statutory_employee.treatment')} [{rid('fed.statutory_employee.treatment')}]. Inputs: {D_SPECIAL}.",
       rep="W-2 box 13", inputs=[D_SPECIAL], legal=["US-FEDR3-005"])
    fl("flag_agri", "Agricultural employee flag (Form 943)",
       (f"Agricultural labour is reported on Form 943: social security and Medicare apply when the employee is paid "
        f"{val('fed.agricultural.per_worker_threshold')} or more in the year or the employer pays {val('fed.agricultural.total_threshold')} "
        f"in total [{rid('fed.agricultural.per_worker_threshold')}]. Alabama: {val('special_population.agricultural.al')} "
       f"[{rid('special_population.agricultural.al')}]. Inputs: {D_SPECIAL}, {D_W2_EMPCODE}, {D_SEASONAL}."),
       rep="Form 943", inputs=[D_SPECIAL, D_W2_EMPCODE, D_SEASONAL], legal=["US-FEDR3-006"])
    fl("flag_3psp", "Third-party sick pay flag",
       f"Flag per employee for sick pay paid by a third party; reported in W-2 box 13. Input: {D_W2_3PSP}.",
       rep="W-2 box 13", inputs=[D_W2_3PSP], legal=["US-FEDS5-007"])
    fl("flag_student", "Student employee flag",
       f"{val('fed.students.treatment')} [{rid('fed.students.treatment')}]. Inputs: {D_SPECIAL}.",
       inputs=[D_SPECIAL], legal=["US-FEDS5-029"])
    fl("flag_prevwage", "Prevailing wage project flag (informational)",
       ("Informational flag only: it marks pay for public-works work covered by a prevailing wage law. The payroll build does not produce "
        "certified payroll reports and the flag changes no tax or contribution."), legal=["US-OWN-009"])
    fl("flag_sit_state", "State of income tax withholding (sourcing flag)",
       (f"Flag that selects the State layer for the employee: the State of work unless reciprocity, the nonresident threshold, the convenience "
        f"rule, the transport rule or the military spouse rule changes it. Resident credit: {val('multi.resident_credit.level')} "
        f"[{rid('multi.resident_credit.level')}]. Transport: motor carrier {val('multi.transport.motor_carrier.rule')}; rail "
        f"{val('multi.transport.rail.rule')}; air {val('multi.transport.air.rule')}. Convenience rule: {val('multi.convenience_rule.states')} "
        f"[{rid('multi.convenience_rule.states')}]. Mobile workforce bill: {val('multi.mobile_workforce_bill.status')}. Military spouse: "
        f"{val('multi.military_spouse.rule')} [{rid('multi.military_spouse.rule')}]. Inputs: {D_WORK_STATE}, {D_RES_STATE}, {D_TRANSPORT}, "
        f"{D_MILSPOUSE}, {D_STATE_CERT}."),
       inputs=[D_WORK_STATE, D_RES_STATE, D_TRANSPORT, D_MILSPOUSE, D_STATE_CERT],
       legal=["US-MULTIS5-017", "US-FEDP52-005", "US-AZWH-003"])
    fl("flag_ui_state", "State of unemployment insurance coverage (localization flag)",
       (f"Flag that selects the single State that covers all the service of the employee with one employer: {val('multi.sui.localization_test')} "
        f"[{rid('multi.sui.localization_test')}]. The State disability and paid leave programmes follow this State unless the State row says "
        f"otherwise. Employee contribution States: {val('multi.sui.employee_contribution.states')} [{rid('multi.sui.employee_contribution.states')}]. "
        f"Inputs: {D_UI_STATE}, {D_WORK_STATE}, {D_RES_STATE}."),
       inputs=[D_UI_STATE, D_WORK_STATE, D_RES_STATE], legal=["US-MULTIS5-017"])
    return reg
