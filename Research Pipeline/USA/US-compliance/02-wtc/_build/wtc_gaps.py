# -*- coding: utf-8 -*-
"""Gap definitions of the US Wage Type Catalogue (WTC-RQ-01 .. WTC-RQ-19: gaps of the builder; WTC-RQ-20 upward: open items
of the facts, allocated on first use by W.ug). A gap is written in the cell as 'Not configured in this release [[GAP:id]]: ...',
never as a value: the request goes to _research/WTC-research-request.json and a matching limitation entry to _research/gaps.json."""
import wtc_common as W


def define():
    g = W.gap_def
    g("WTC-RQ-01", "allowance-specific exclusions from wages (accountable plan reimbursement, per diem, housing furnished for the "
      "convenience of the employer, car and travel allowances, expatriate allowances) are not stated by any fact; the rows carry the "
      "cash-wage treatment of the regular wage rows",
      "IRS Publication 15-B and Publication 463 (or the regulations they cite) read for accountable plan reimbursement, per diem and "
      "lodging furnished for the convenience of the employer, entered as facts with register rows",
      "wtc.fed.allowance_exclusions", domain="income_tax", severity="major")
    g("WTC-RQ-02", "tax treatment of the recovery of a salary advance, of the generic benefit plan deduction and contribution, and of the "
      "recovery of an expense reimbursement is not stated by any fact; the rows carry no tax flag",
      "the official rule for each item (wage payment rules and Publication 15-B) as facts with register rows",
      "wtc.fed.advance_and_benefit_plan_treatment", domain="income_tax")
    g("WTC-RQ-03", "the tax treatment of the designated Roth deferral (401(k) and 403(b)) and of the 408(k)(6) and 501(c)(18)(D) deferrals is not stated by a fact; "
      "these rows carry no tax flag (their W-2 box 12 codes are defined by the IRS code table)",
      "the Internal Revenue Code and Publication 15 text on the wage treatment of designated Roth and other deferrals, as facts with register rows",
      "wtc.fed.roth_deferral_treatment", domain="income_tax", severity="major")
    g("WTC-RQ-04", "treatment of employer contributions to a qualified retirement plan (matching and non-elective) is not stated by a fact; "
      "the row carries no tax flag",
      "the Internal Revenue Code and Publication 15-B text on employer plan contributions, as facts with register rows",
      "wtc.fed.employer_plan_contribution", domain="income_tax")
    g("WTC-RQ-05", "treatment of long-term disability and third-party sick pay (employee-paid and employer-paid premium and benefit) is not "
      "stated by a fact; the rows carry no tax flag",
      "Publication 15-A on sick pay and the FICA six-month rule, as facts with register rows",
      "wtc.fed.sick_pay_ltd", domain="income_tax")
    g("WTC-RQ-06", "treatment of pension and pension-refund payments is not stated by a fact (a pension distribution is not wages from the "
      "employer); the rows carry no tax flag",
      "the official source for the payment types that the global rows 62640 to 62648 describe, as facts with register rows",
      "wtc.fed.pension_payments", domain="income_tax")
    g("WTC-RQ-07", "the State unemployment insurance and State programme (disability, paid leave) wage definition for the allowance, "
      "severance and fringe families is carried only where a State row lists a departure; the rows carry Yes-No on those two flags",
      "per State: the unemployment insurance wage definition and the programme wage definition as facts with register rows",
      "wtc.state.wage_definition_by_family", domain="social_security", severity="major")
    g("WTC-RQ-08", "no authority code table of the reporting codes (W-2 box 12 codes) is held for the build year, so the reporting code check "
      "cannot test the codes of column W",
      "an authority code table for the annual wage statement box 12 codes, valid for the build year",
      "wtc.reporting.code_table", domain="statutory_reporting", severity="major")
    g("WTC-RQ-09", "no rate, base or deduction rule of the Wyoming State workers' compensation fund is carried; the row carries no tax flag and no figure",
      "the Wyoming Workers' Safety and Compensation Division premium rate and payroll reporting rule, as facts with register rows",
      "wtc.wy.workers_comp_fund", domain="statutory_reporting")

    g("WTC-RQ-10", "the Massachusetts paid family and medical leave rates are derived from a split that the source does not print; no rate is written",
      "the Department of Family and Medical Leave rate page or regulation stating the family and medical rates as figures, with a register row",
      "ma.pfml.family.rate", domain="social_security")
    g("WTC-RQ-11", "one cell of the Massachusetts unemployment insurance rate schedule is not located in the stored copy; the schedule is not written",
      "a complete copy of the Massachusetts rate schedule with every cell located, as a register row",
      "ma.sui.rate_schedule.table", domain="social_security")
    g("WTC-RQ-12", "the weekly protected earnings amount of the consumer credit protection limit is derived (30 times the federal minimum hourly wage) and is not printed in the stored copy; no figure is written",
      "the Department of Labor fact sheet or 15 USC 1673 text with the amount stated, as a register row",
      "fed.ccpa.protected_weekly", domain="statutory_reporting")
    g("WTC-RQ-13", "the priority between several income withholding orders is not stated by the registered source (Publication 1494 carries no such rule)",
      "the official text on the priority of support orders over other garnishments and between orders, as a register row",
      "fed.iwo.priority", domain="statutory_reporting")
    g("WTC-RQ-14", "the 2026 federal withholding treatment of equity compensation of a resident employee combines several sources and is not proven clause by clause",
      "a clause-by-clause check of Publications 15-B, 15-T and 515 and the regulation on stock-based wages, entered as separate facts",
      "fed.equity.withholding_treatment.resident", domain="income_tax", severity="major")
    g("WTC-RQ-15", "the withholding treatment of benefits in kind of a nonresident alien combines several sources and is not proven clause by clause",
      "a clause-by-clause check of Publications 15-B, 15-T and 515 as separate facts",
      "fed.fit.nra.bik.treatment", domain="income_tax")


GENERIC_RQ = ["WTC-RQ-01", "WTC-RQ-02", "WTC-RQ-03", "WTC-RQ-04", "WTC-RQ-05", "WTC-RQ-06", "WTC-RQ-07", "WTC-RQ-08", "WTC-RQ-09", "WTC-RQ-10", "WTC-RQ-11", "WTC-RQ-12", "WTC-RQ-13", "WTC-RQ-14", "WTC-RQ-15"]
