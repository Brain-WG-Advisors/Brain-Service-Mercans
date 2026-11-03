# -*- coding: utf-8 -*-
"""Build 01-ccg/modules/m04_compensation.md from the CCG facts (US build)."""
import json
import os
from ccglib import *

U = "m04_compensation"
set_unit(U)
o = []
A = o.append
EX = json.load(open(os.path.join(BASE, "01-ccg", "_examples", "m01_m07_examples.json"), encoding="utf-8"))


def dated(key):
    """All dated values of a key as 'value (period)' strings, each tagged."""
    out = []
    seen = set()
    for f in sorted(FACTS[key], key=lambda x: x.get("effective_from") or ""):
        sig = (json.dumps(f["value"]), f.get("effective_from"), f.get("effective_to"))
        if sig in seen:
            continue
        seen.add(sig)
        on = f.get("effective_from")
        per = f"from {f['effective_from']}" + (f" to {f['effective_to']}" if f.get("effective_to") else "")
        out.append(f"USD {T(key, on=on if len(FACTS[key]) > 1 else None, fmt='money')} ({per})")
    return "; ".join(out)


A("# Module 4: Gross Compensation")
A("*Purpose: To define all components of gross pay and their calculation rules.*")

# ---------------------------------------------------------------- 4.1
A(H(2, "4.1 Minimum Wage"))
A(H(3, "Is there a minimum wage? Who is eligible?"))
A(f"Yes. The federal minimum wage is USD {T('fed.minwage.hourly')} an hour {R('fed.minwage.hourly')} and applies to "
  "employment covered by the Fair Labor Standards Act (FLSA). Special federal rules:")
A("")
A("| Group | Rule | Fact |")
A("|---|---|---|")
A(f"| Tipped employees (more than USD {T('fed.tipped.monthly_tips_threshold')} a month in tips) | Cash wage USD {T('fed.tipped.cash_wage.hourly')}; maximum tip credit USD {T('fed.tipped.tip_credit.max_hourly')} | {R('fed.tipped.cash_wage.hourly')} |")
A(f"| Executive, administrative and professional (EAP) exemption | Salary floor USD {T('fed.exempt.salary_floor.weekly')} a week (USD {T('fed.exempt.salary_floor.biweekly')} biweekly, USD {T('fed.exempt.salary_floor.semimonthly')} semimonthly, USD {T('fed.exempt.salary_floor.monthly')} monthly) | {R('fed.exempt.salary_floor.weekly')} |")
A(f"| Apprentices, trainees, learners | No federal apprentice payroll regime; the FLSA minimum applies (sub-minimum only under DOL certificates). States set learner rates, e.g. California {T('ca.minwage.learner.percent')}% for the first 160 hours, Washington 14-15 year olds USD {T('wa.labour.minwage.youth_14_15.hourly', on='2026-06-30')} in 2026 | {COV('apprentices_and_trainees')}; {R('ca.minwage.learner.percent')}; {R('wa.labour.minwage.youth_14_15.hourly', on='2026-06-30')} |")
A(f"| Part-time employees | No part-time regime: the minimum wage and the weekly overtime threshold apply per hour and per workweek regardless of schedule | {COV('part_time')} |")
A("")
A("Several State tipped-wage rules differ from the federal one (for example "
  f"{K('ak.minwage.tip_credit.allowed')}: no tip credit; {K('wa.minwage.tip_credit.allowed')}: no tip credit); see annexes.")
A(H(3, "Is the minimum wage applicable at a national level or does it vary by province/state?"))
A(f"Both. The federal rate is a floor and the most protective applicable rate wins: {Q('multi.wage_hour.overlay_rule')} "
  f"{R('multi.wage_hour.overlay_rule')}. The employer pays the highest of the federal, State and local minimum of the place "
  f"where the work is performed {R('fed.minwage.hourly')}. Several cities and counties set their own rates (examples below; "
  "California municipal rates are in Annex CA).")
A(H(3, "Provide all applicable minimum wage rates."))
A("All dates are effective dates; a rate change applies to hours worked from the date shown.")
A("")
A("| Jurisdiction | Hourly minimum wage | Fact |")
A("|---|---|---|")
A(f"| Federal (FLSA) | {dated('fed.minwage.hourly')} | {R('fed.minwage.hourly')} |")
MW = {}
for k in sorted(FACTS):
    p = k.split(".")
    if len(p[0]) == 2 and p[0] not in ("fl",) and k in (f"{p[0]}.minwage.hourly",):
        MW[p[0]] = k
MW["fl"] = "fl.minwage.hourly"
special = {"ny": ["ny.minwage.nyc_li_westchester.hourly", "ny.minwage.rest.hourly"],
           "or": ["or.labour.minwage.standard.hourly"], "tx": ["tx.minwage.hourly"]}
states = sorted(set(MW) | set(special))
for st in states:
    if st in special:
        parts = []
        for k in special[st]:
            lab = {"ny.minwage.nyc_li_westchester.hourly": "New York City, Long Island, Westchester",
                   "ny.minwage.rest.hourly": "rest of State",
                   "or.labour.minwage.standard.hourly": "standard (Portland metro and nonurban rates in annex OR)",
                   "tx.minwage.hourly": "State rate"}[k]
            parts.append(f"{lab}: {dated(k)}")
        k0 = special[st][0]
        first0 = sorted(FACTS[k0], key=lambda x: x.get('effective_from') or '')[0]
        A(f"| {st.upper()} | {'; '.join(parts)} | {R(k0, on=first0['effective_from'] if len({x.get('effective_from') for x in FACTS[k0]}) > 1 else None)} |")
    else:
        k = MW[st]
        first = sorted(FACTS[k], key=lambda x: x.get('effective_from') or '')[0]
        A(f"| {st.upper()} | {dated(k)} | {R(k, on=first['effective_from'] if len(FACTS[k]) > 1 else None)} |")
ALL = [j.lower() for j in MAN("tier", "_jurisdictions") if len(j) == 2]
missing = sorted(j.upper() for j in ALL if j not in states)
A("| " + ", ".join(missing) + " | No State minimum-wage fact in the pack; the federal floor applies to FLSA-covered employment | see request below |")
A("")
A("Local minimum wages (examples; full lists in the annexes):")
A("")
A("| Locality | Rate | Fact |")
A("|---|---|---|")
for k, lab in [("wa.labour.minwage.local.seattle.hourly", "Seattle, WA"),
               ("wa.labour.minwage.local.tukwila.hourly", "Tukwila, WA"),
               ("wa.labour.minwage.local.seatac.hourly", "SeaTac, WA (hospitality and transportation)"),
               ("md.local_minwage.montgomery.51_plus", "Montgomery County, MD (51+ employees)"),
               ("md.local_minwage.howard", "Howard County, MD"),
               ("md.local_minwage.prince_georges", "Prince George's County, MD")]:
    f0 = FACTS[k][0]
    per = f"from {f0['effective_from']}" + (f" to {f0['effective_to']}" if f0.get("effective_to") else "")
    A(f"| {lab} | USD {T(k)} ({per}) | {R(k)} |")
A("")
A(GAP("multi.minwage.remaining_states",
      "no State minimum-wage fact for " + ", ".join(missing) + "; whether each has a State rate (relevant to employment outside FLSA coverage) is not established",
      "For " + ", ".join(missing) + ", what State minimum wage (if any) applies in 2026 and 2027 to private employment not covered by the FLSA, per the State statute or labour department?",
      "CCG m04 §4.1 minimum-wage table incomplete for " + str(len(missing)) + " States",
      "labour_code", tier="A.2"))
A("")
A(f"Coverage of mid-year changes ({COV('mid_year_rate_change')}): the District of Columbia, Oregon and Alaska change on "
  f"{D('dc.minwage.hourly', on='2026-07-01')}, Florida on {D('fl.minwage.hourly', on='2026-09-30')}, and the Nevada daily "
  f"overtime rule on {D('nv.overtime.daily_threshold_wage')}; each rate is applied by the date the hours were worked.")
A(H(3, "Does the minimum wage impact any tax or social security calculations?"))
A("Not the tax or contribution rates. It feeds three payroll calculations:")
A("")
A("| Calculation | How the minimum wage enters | Fact |")
A("|---|---|---|")
A(f"| Federal garnishment protection | Protected amount USD {T('fed.ccpa.protected_weekly')} a week = 30 x the federal minimum wage | {R('fed.ccpa.protected_weekly')} |")
A(f"| State garnishment protection | Multiples of the higher State or federal minimum, e.g. California {T('ca.garn.creditor.minwage_multiple.weekly')} x (weekly), Arizona {T('az.garn.creditor.minwage_multiple')} x, Colorado weekly floor USD {T('co.garn.creditor.weekly_floor')}, Connecticut weekly protected USD {T('ct.garn.creditor.weekly_protected')} | {R('ca.garn.creditor.minwage_multiple.weekly')}; {R('az.garn.creditor.minwage_multiple')}; {R('co.garn.creditor.weekly_floor')}; {R('ct.garn.creditor.weekly_protected')} |")
A(f"| Tip credit | Cash wage plus tip credit must reach the minimum: USD {T('fed.tipped.cash_wage.hourly')} + USD {T('fed.tipped.tip_credit.max_hourly')} = USD {T('fed.minwage.hourly')} | {R('fed.tipped.tip_credit.max_hourly')} |")
A(H(3, "How are deductions handled if they cannot be made due to minimum wage constraints?"))
A(GAP("fed.flsa.deductions_below_minimum_wage",
      "the FLSA rule on deductions that would reduce pay below the minimum wage (and the State variants) is not in the facts",
      "Under 29 CFR 531.35 and related FLSA rules, which deductions (uniforms, tools, cash shortages, loans, board and lodging) may not reduce an employee's wage below the federal minimum wage or cut into overtime, and how should a deduction that cannot be taken be handled (carried forward or dropped)?",
      "CCG m04 §4.1 cannot state the minimum-wage limit on deductions; deduction-capping logic in the engine has no rule",
      "labour_code", tier="A.1"))
A("Statutory deductions (taxes, garnishments within their limits) are not limited by the minimum wage; the garnishment "
  "protected amounts in Module 7 apply instead.")

# ---------------------------------------------------------------- 4.2
A(H(2, "4.2 Salary Components"))
A(H(3, "What are the mandatory and common salary components?"))
A("Federal law mandates no salary component other than the minimum wage and the overtime premium. The components "
  "that the law classifies, and that the WTC must carry, are:")
A("")
A("| Component | Classification that matters | Fact |")
A("|---|---|---|")
A("| Regular wages (salary or hourly) | Regular wages: Worksheet 1A method | `fed.fit.method` |")
A(f"| Overtime premium | Regular wages for withholding; qualified overtime reported on the W-2 | {K('fed.plaw119_21.qualified_overtime.level')} |")
A(f"| Tips | Subject to withholding and FICA when USD {T('fed.tips.reporting_threshold_monthly')} or more in a month | {R('fed.tips.reporting_threshold_monthly')} |")
A(f"| Bonuses, commissions, severance | Supplemental wages: flat {T('fed.fit.supplemental.flat_rate')}% optional or aggregate | {R('fed.fit.supplemental.flat_rate')} |")
A(f"| Non-cash fringe benefits | Taxable unless an exclusion applies (Module 7) | {K('fed.bik.parking.monthly_exclusion')} and related keys |")
A(H(3, "What is the general definition and pay cycle for each component?"))
A("Regular wages are paid on the employer's regular payday under the work State's pay-frequency rule (Module 1 §1.2). "
  "Overtime is due with the wages of the period, or by the next regular payday where a State says so (for example "
  f"{K('ca.pay_frequency.rule')}). Supplemental wages may be paid with or separately from regular wages; the "
  "withholding method depends on that choice (Module 6 §6.2).")
A(H(3, "Which components are taxable vs non-taxable and sociable vs non-sociable?"))
A("| Component | Federal income tax | FICA (social security and Medicare) | FUTA | Fact |")
A("|---|---|---|---|---|")
A(f"| Regular wages, overtime, bonuses, commissions | Taxable | Subject | Subject (wages) | {R('fed.plaw119_21.qualified_overtime.level')}; {R('fed.futa.legal_basis.rate_statute')}; {COV('overtime')} |")
A(f"| Severance and pay in lieu of notice | Taxable | Subject | Subject | {K('fed.severance.is_wages')} |")
# round 3b (QA r3 blocker 1, RQ-562 closed by agent 2 R3): FIT / FICA / FUTA cells rendered from fed.base.* facts
A(f"| Tips | {T('fed.base.tips.fit')} | {T('fed.base.tips.fica')} | {T('fed.base.tips.futa')} | {R('fed.base.tips.fica')}; {R('fed.tips.reporting_threshold_monthly')} |")
A(f"| Group-term life insurance | {T('fed.base.group_term_life.fit')} | {T('fed.base.group_term_life.fica')} | {T('fed.base.group_term_life.futa')} | {R('fed.base.group_term_life.fica')} |")
A(f"| PFML employee contribution | W-2 wages | W-2 wages | No FUTA exclusion is configured for the contribution: it is withheld from wages, which stay wages under the general definition | {R('fed.pfml.employee_contribution.is_w2_wages')}; {R('fed.wages.general_definition')} |")
A(f"| Transit passes, commuter vehicle and qualified parking | {T('fed.base.transportation.fit')} | {T('fed.base.transportation.fica')} | {T('fed.base.transportation.futa')} | {R('fed.base.transportation.fica')} |")
A(f"| Educational assistance | {T('fed.base.educational_assistance.fit')} | {T('fed.base.educational_assistance.fica')} | {T('fed.base.educational_assistance.futa')} | {R('fed.base.educational_assistance.fica')} |")
A(f"| Dependent-care assistance | {T('fed.base.dependent_care.fit')} | {T('fed.base.dependent_care.fica')} | {T('fed.base.dependent_care.futa')} | {R('fed.base.dependent_care.fica')} |")
A(f"| Retirement deferrals and Section 125 reductions | See Module 3, Step 2 | See Module 3, Step 2 | See Module 3, Step 2 | {R('fed.retirement.pretax.tax_treatment')} |")
A(f"| Moving expenses, bicycle commuting | No exclusion (eliminated, except moving for Armed Forces / intelligence community) | No exclusion | No exclusion | {K('fed.bik.moving_and_bicycle.excluded')} |")
A(f"| Ministers' pay | No withholding (self-employment tax); parsonage allowance excluded from W-2 box 1 | Not withheld | Not established from an official source [[GAP:RQ-593]] | {K('fed.minister.withholding')} |")
A("")
A("")
A("Statutory wage definitions behind the table:")
A("")
A("| Base | Definition and exclusions | Source |")
A("|---|---|---|")
A(f"| All federal employment taxes (general) | {T('fed.wages.general_definition')} | {R('fed.wages.general_definition')} |")
A(f"| FICA wages | {T('fed.fica.wage_definition.exclusions')} | {R('fed.fica.wage_definition.exclusions')} |")
A(f"| FUTA wages | {T('fed.futa.wage_definition.exclusions')} | {R('fed.futa.wage_definition.exclusions')} |")
A("| Income-tax withholding wages | Module 6 §6.1.1 (26 U.S.C. 3401(a)) | Module 6 |")
A(H(3, "Are components uniform across the country or do they differ by state/province?"))
A("Federal classification is uniform. State classification differs, because each State decides its own conformity "
  f"(examples: {K('ca.obbba.conforms')} no State tips or overtime deduction; {K('pa.bik.pa.401k_403b_457.taxable')}; "
  f"{K('nj.sui.wages.401k_included')}; {K('ms.bik.section125.excluded')}). Each State annex carries its own inclusion "
  "and exclusion rules.")
A(H(3, "What is the calculation logic for each salary component?"))
A("| Component | Logic |")
A("|---|---|")
A("| Salaried | Periodic salary for the pay period; proration only where the employer's policy applies it (§4.3) |")
A("| Hourly | Hours worked x hourly rate, at least the applicable minimum wage (§4.1) |")
A(f"| Overtime | Overtime hours x regular rate x {T('fed.overtime.premium.multiplier')} (§4.4) |")
A(f"| Tipped | Cash wage + tips; employer tops up to the minimum when the tip credit does not reach it ({R('fed.tipped.tip_credit.max_hourly')}) |")
A("| Supplemental | Amount as granted; withholding method per Module 6 |")
A(H(3, "Which components require employee-declared values and submissions?"))
A("| Declaration | Content | Fact |")
A("|---|---|---|")
A(f"| Form W-4 | {Q('fed.w4.input_fields')} | {R('fed.w4.input_fields')} |")
A("| State withholding certificate | Per State (Module 2) | annexes |")
A(f"| Tip report | Tips of USD {T('fed.tips.reporting_threshold_monthly')} or more in a month reported to the employer | {R('fed.tips.reporting_threshold_monthly')} |")
A(f"| Treaty exemption (nonresident alien) | Form 8233; treaty-exempt wages reported on Form 1042-S | {K('fed.fit.nra.treaty_exempt.reporting')} |")
A(f"| Reciprocity / nonresidence certificate | Per work State (Module 2) | `multi.reciprocity.*` |")
A(H(3, "Deliverable: Define the primary earnings base for social security contributions. Produce a comprehensive Inclusion/Exclusion analysis."))
A("The primary base is FICA wages: all remuneration for employment unless excluded. It feeds three different caps:")
A("")
A("| Base | Cap 2026 | Fact |")
A("|---|---|---|")
A(f"| OASDI | USD {T('fed.fica.oasdi.wage_base', on='2026-06-30')} per employer | {R('fed.fica.oasdi.wage_base', on='2026-06-30')} |")
A(f"| Medicare | No cap; Additional Medicare above USD {T('fed.fica.addl_medicare.withholding_threshold')} | {R('fed.fica.addl_medicare.withholding_threshold')} |")
A(f"| FUTA | USD {T('fed.futa.wage_base')} per employer | {R('fed.futa.wage_base')} |")
A("")
A("Inclusion/exclusion analysis: the rows supported by the facts are in the table of the previous question; the complete "
  "statutory list is research gap `fed.fica.wage_definition.exclusions`. State unemployment bases follow their own "
  "definitions (Module 5 §5.1.1).")

# ---------------------------------------------------------------- 4.3
A(H(2, "4.3 Proration"))
A(H(3, "Are fixed wages prorated for the number of working days?"))
A(f"No statutory rule. Federal law sets no proration method ({COV('mid_month_joiner_and_leaver')}); withholding is "
  "computed on the wages actually paid in the period. Whether a fixed salary is prorated, and on which day count, is "
  "the employer's policy, subject to the minimum wage for the hours worked and, for EAP-exempt staff, the salary-basis "
  f"floor (USD {T('fed.exempt.salary_floor.weekly')} a week, {R('fed.exempt.salary_floor.weekly')}).")
A(H(3, "Describe the statutory or standard business practice for prorating fixed salary components for mid-period hires and terminations."))
A("Configuration choice (non-statutory): the engine offers a working-day or a calendar-day factor per pay group. The "
  "chosen factor is applied to every fixed component of the period; variable components are paid as earned.")
A(H(3, "Provide the proration formula and a worked example."))
A("```")
A("prorated_salary = round( period_salary x days_in_service / days_in_period , 2 )   # half-up to the cent")
A("```")
A("")
A("Worked example (configuration choice, working-day factor; computed by `01-ccg/_examples/build_examples_m01_m07.py`):")
A("")
A("| Calculation | Result |")
A("|---|---|")
for row in EX["proration"]:
    A(f"| {row[0]} | {row[1]} |")

# ---------------------------------------------------------------- 4.4
A(H(2, "4.4 Overtime"))
A(H(3, "Detail the statutory rules for overtime, including eligibility criteria and mandatory rates."))
A(f"Federal ({COV('overtime')}): {T('fed.overtime.premium.multiplier')} x the regular rate for hours over "
  f"{T('fed.overtime.weekly_threshold_hours')} in a workweek {R('fed.overtime.weekly_threshold_hours')}; there is no federal "
  "daily overtime. EAP-exempt employees paid at least the salary floor are excluded. States add daily or seventh-day overtime:")
A("")
A("| Jurisdiction | Rule | Fact |")
A("|---|---|---|")
A(f"| CA | {Q('ca.overtime.rule')} | {R('ca.overtime.rule')} |")
A(f"| AK | {T('ak.overtime.premium.multiplier')} x over {T('ak.overtime.daily_threshold_hours')} hours a day and over {T('ak.overtime.weekly_threshold_hours')} a week; employers with fewer than 4 employees exempt | {R('ak.overtime.daily_threshold_hours')} |")
A(f"| NV | From {D('nv.overtime.daily_threshold_wage')}: employees earning under USD {T('nv.overtime.daily_threshold_wage')} an hour get 1.5 x over 8 hours in 24 hours | {R('nv.overtime.daily_threshold_wage')} |")
A(f"| WA | {T('wa.overtime.premium.multiplier')} x over {T('wa.overtime.weekly_threshold_hours')} hours a week; no daily overtime | {R('wa.overtime.weekly_threshold_hours')} |")
A(f"| DC | Over {T('dc.overtime.weekly_threshold_hours')} hours a week; no daily overtime | {R('dc.overtime.weekly_threshold_hours')} |")
A("")
A("Worked example (computed by the examples script from the federal facts):")
A("")
A("| Calculation | Result |")
A("|---|---|")
for row in EX["overtime"]:
    A(f"| {row[0]} | {row[1]} |")
A(H(3, "Explain how overtime is treated for income tax and social security calculations."))
A(f"Overtime is regular wages for withholding and fully subject to FICA, FUTA and SUI. The federal qualified-overtime "
  f"deduction operates only at assessment: {Q('fed.plaw119_21.qualified_overtime.level')} {R('fed.plaw119_21.qualified_overtime.level')}; "
  f"the employee's annual deduction is capped at USD {T('fed.plaw119_21.qualified_overtime.deduction_cap')} "
  f"(USD {T('fed.plaw119_21.qualified_overtime.deduction_cap_mfj')} married filing jointly) {R('fed.plaw119_21.qualified_overtime.deduction_cap')}. "
  f"Build rule: {Q('practice.fed.pl119_21_withholding')} {R('practice.fed.pl119_21_withholding')}.")
A("")
A("State overtime deductions also operate at assessment only (never reduce State withholding):")
A("")
A("| State | Rule | Fact |")
A("|---|---|---|")
A(f"| AL | Overtime premium deduction up to USD {T('al.pit.overtime_premium_deduction.max')}, assessment only | {R('al.pit.overtime_premium_deduction.max')} |")
A(f"| GA | Overtime subtraction up to USD {T('ga.pit.overtime_subtraction.max')}, assessment only | {R('ga.pit.overtime_subtraction.max')} |")
A(f"| MI | {Q('mi.pit.tips_overtime_deduction')} | {R('mi.pit.tips_overtime_deduction')} |")
A(f"| IA | {Q('ia.pit.obbba')} | {R('ia.pit.obbba')} |")
A(f"| DC | {Q('dc.pit.obbba_deductions')} | {R('dc.pit.obbba_deductions')} |")
A(f"| CO | Colorado's worksheet removes the federal qualified-overtime deduction from W-4 Step 4(b) for State withholding | {K('co.wh.obbba_overtime_deduction.allowed')} |")
A(f"| CA | {K('ca.obbba.conforms')}: no State tips or overtime deduction | {R('ca.obbba.conforms')} |")
A(f"| HI | {GAP('hi.pit.tips_overtime_deduction.level', 'the Hawaii treatment of tips and overtime deductions (assessment-only per the build journal) has no fact', 'Does Hawaii allow a State income-tax deduction or exclusion for qualified tips or overtime for tax year 2026, and does it operate only at assessment (no change to withholding)?', 'CCG m04 §4.4 and m06 trap table cannot state the Hawaii level; WTC cannot set the HI flag', 'income_tax', tier='A.1')} | |")
A("")
A(f"W-2 reporting of overtime and tips: {Q('fed.w2.box12.new_codes')} {R('fed.w2.box12.new_codes')}.")

# ---------------------------------------------------------------- 4.5
A(H(2, "4.5 Bonuses"))
A(H(3, "Is there a statutory requirement to pay bonuses? If so, how are they calculated?"))
A(GAP("fed.bonus.statutory_obligation",
      "no fact states whether any federal or State statute requires a private employer to pay a bonus (13th-month or similar)",
      "Does any federal statute or any State statute require private employers to pay a bonus, 13th-month salary or similar periodic payment, and if a promised bonus is paid, which State wage-payment rules govern its timing?",
      "CCG m04 §4.5 statutory bonus question unanswered",
      "labour_code", tier="A.1"))
A(H(3, "Is there a specific tax treatment for bonuses?"))
A(f"Yes. Bonuses are supplemental wages. Federal: flat {T('fed.fit.supplemental.flat_rate')}% (optional) or the "
  f"aggregate method; {T('fed.fit.supplemental.mandatory_rate')}% mandatory on supplemental wages above USD "
  f"{T('fed.fit.supplemental.mandatory_threshold')} paid to one employee in the calendar year {R('fed.fit.supplemental.mandatory_rate')}. "
  f"FICA applies as to regular wages ({COV('special_pay_cycles')}). States set their own supplemental methods:")
A("")
A("| State | Supplemental method | Fact |")
A("|---|---|---|")
A(f"| CA | Bonuses and stock options {T('ca.wh.supplemental.rate.bonus_stock_options')}%; other supplemental {T('ca.wh.supplemental.rate.other')}% (when paid separately) | {R('ca.wh.supplemental.rate.bonus_stock_options')} |")
A(f"| ID | Flat {T('id.wh.supplemental.rate')}% on a separately issued payment, or aggregate | {R('id.wh.supplemental.rate')} |")
A(f"| ND | Flat {T('nd.wh.supplemental.rate')}% or aggregate | {R('nd.wh.supplemental.rate')} |")
A(f"| KY | {Q('ky.wh.supplemental.method')} | {R('ky.wh.supplemental.method')} |")
A(f"| SC | No flat supplemental rate: bonuses through the tables | {K('sc.pit.supplemental.flat_rate.exists')} |")
A("")
A("A worked bonus example is in Module 6 §6.3.")

# ---------------------------------------------------------------- 4.6
A(H(2, "4.6 Wage Classification (Country-Specific)"))
A(H(3, "Are there country-specific classifications for wages critical for social security or tax calculations?"))
A("Yes. US payroll classifies each payment along four independent axes; one payment can fall in different "
  "classes for different bases.")
A(H(3, "Provide a detailed definition for each classification."))
A("| Classification | Definition | Fact |")
A("|---|---|---|")
A(f"| Regular vs supplemental wages | Supplemental = bonuses, commissions, severance and similar; may be withheld at a flat rate | {R('fed.fit.supplemental.flat_rate')} |")
A(f"| Withholding wages vs FICA wages | A payment can be FICA wages without income-tax withholding being required (group-term life cost above USD {T('fed.bik.group_term_life.excluded_coverage')} of coverage); a statutory employee's pay is FICA-withheld with no income-tax withholding | {R('fed.bik.group_term_life.excluded_coverage')}; {K('fed.statutory_employee.treatment')} |")
A(f"| Taxable wage base vs total wages | OASDI, FUTA and each SUI/PFML base stop at a cap; Medicare does not | {R('fed.futa.wage_base')} |")
# round 2 (QA r1 C41): fed.plaw119_21.reporting_penalty_relief is a TY2025-only value (moved to _history);
# the 2026 reporting rule is carried by the in-force W-2 code fact.
A(f"| Qualified tips and qualified overtime | Reported separately on the W-2 from tax year 2026, Box 12 codes: {Q('fed.w2.box12.new_codes')} | {R('fed.w2.box12.new_codes')} |")
A(f"| State and local wages | Wages allocated to each State and locality; the W-2 carries up to {T('multi.w2.states_per_form')} States and localities per form | {R('multi.w2.states_per_form')} |")
A(H(3, "Create a reference table classifying common pay components."))
A("| Pay component | Regular / supplemental | Federal income tax | FICA | W-2 reporting |")
A("|---|---|---|---|---|")
A("| Salary, hourly wages | Regular | Worksheet 1A | Yes | W-2 wages |")
A(f"| Overtime premium | Regular | Worksheet 1A | Yes | Box 12 code TT for qualified overtime ({R('fed.w2.box12.new_codes')}) |")
A(f"| Cash tips reported | Regular | Worksheet 1A | Yes | Box 12 code TP; box 14b occupation code ({R('fed.w2.box14b')}) |")
A(f"| Bonus, commission | Supplemental | Flat or aggregate | Yes | W-2 wages ({R('fed.fit.supplemental.flat_rate')}) |")
A(f"| Severance | Supplemental | Flat or aggregate | Yes | W-2 wages ({R('fed.severance.is_wages')}) |")
A(f"| Group-term life cost above the excluded coverage | Imputed | Not required | Yes | ({R('fed.bik.group_term_life.excluded_coverage')}) |")
A(f"| Employer Trump-account contribution | Employer contribution | Excluded up to USD {T('fed.bik.trump_account.employer_contribution_max')} from {D('fed.bik.trump_account.employer_contribution_max')} | ⚠️ RESEARCH-GAP [[GAPKEY:fed.bik.trump_account.employment_tax_treatment]]: FICA and FUTA treatment of the employer contribution is not established from an official source | Box 12 code TA ({R('fed.bik.trump_account.employer_contribution_max')}) |")
A("")
A(CC.PREVAILING_WAGE_SENTENCE)  # SCOPE r1 finding 2 (US-OWN-009)
A("")
A("Prevailing-wage overlay: federal construction contracts over USD "
  f"{T('fed.davis_bacon.contract_threshold')} carry Davis-Bacon wage rates and weekly certified payroll "
  f"({Q('fed.davis_bacon.certified_payroll.frequency')}; {R('fed.davis_bacon.certified_payroll.frequency')}). State "
  "prevailing-wage laws are in the annexes; never use the federal DOL State list for Michigan.")
A("")
A(UNR("practice.dol_paid_leave_list"))

write_module(U, "\n".join(o))
print("written", U)
