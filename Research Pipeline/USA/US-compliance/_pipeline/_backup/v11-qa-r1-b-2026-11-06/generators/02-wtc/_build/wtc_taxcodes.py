# -*- coding: utf-8 -*-
"""Tax code legend of the US Wage Type Catalogue (column G). The legend is this country's own list: no code of another country
appears in the catalogue, and every code used is defined here with the official source it rests on (v2.4 C9)."""
import wtc_common as W
from wtc_model import TAXCODES, taxcode

LEGEND = [
    ("US-TX-01", "Regular and other cash wages: wages for federal income tax withholding, social security, Medicare and FUTA",
     ["fed.fit.method", "fed.fica.oasdi.wage_base", "fed.futa.wage_base"]),
    ("US-TX-02", "Supplemental wages (bonus, commission and similar payments): optional flat rate, mandatory rate above the annual threshold or aggregate method",
     ["fed.fit.supplemental.flat_rate", "fed.fit.supplemental.mandatory_rate"]),
    ("US-TX-03", "Tips: cash tips reported to the employer", ["fed.base.tips.fit", "fed.base.tips.fica"]),
    ("US-TX-04", "Employee taxes withheld: federal income tax, social security, Medicare and Additional Medicare Tax",
     ["fed.fit.method", "fed.fica.oasdi.rate.employee", "fed.fica.addl_medicare.rate"]),
    ("US-TX-05", "Employer taxes: social security, Medicare and FUTA (and the FUTA credit reduction)",
     ["fed.fica.oasdi.rate.employer", "fed.futa.wage_base"]),
    ("US-TX-06", "State and local income tax withheld from the employee (one row per jurisdiction)",
     ["multi.no_wage_income_tax.states", "multi.resident_credit.level"]),
    ("US-TX-07", "State unemployment insurance, State disability and paid leave programme contributions and State levies (employee and employer; one row per jurisdiction and programme)",
     ["multi.sui.localization_test", "multi.sui.employee_contribution.states"]),
    ("US-TX-08", "Excluded, conditional or imputed fringe benefit and salary reduction items (section 125, qualified plans, transportation, dependent care, group-term life, HSA)",
     ["fed.base.section125.rule", "fed.base.group_term_life.fit", "fed.base.dependent_care.fit"]),
    ("US-TX-09", "Severance, gratuity and post-termination payments", ["fed.severance.treatment"]),
    ("US-TX-10", "Equity compensation (options, restricted stock, restricted stock units, section 83(i))",
     ["fed.equity.withholding_treatment.resident", "fed.equity.rsu.fica_timing"]),
    ("US-TX-11", "Local employer payroll taxes on a separate return (city payroll expense and social housing taxes)",
     ["wa.local.seattle.payroll_expense_tax", "nj.local.newark.payroll_tax.rate"]),
    ("US-NA", "No tax code: item with no tax effect (after-tax deduction, reporting-only amount, flag, accumulator)", []),
]


def define():
    TAXCODES.clear()
    for code, meaning, keys in LEGEND:
        taxcode(code, meaning, keys)


def source_text(code):
    """Official source string of a legend code, from the register rows of the facts that define it."""
    t = TAXCODES[code]
    if not t["source_keys"]:
        return "Not a tax code: the item has no tax effect, so no official source applies."
    seen, parts = set(), []
    for k in t["source_keys"]:
        for r_ in W.rids(k):
            if r_ in seen:
                continue
            seen.add(r_)
            row = W.REG[r_]
            parts.append(f"{row['instrument_name']} ({row['authority']}) [{r_}]")
    return "; ".join(parts)
