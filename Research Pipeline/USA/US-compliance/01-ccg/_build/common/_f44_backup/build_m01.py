# -*- coding: utf-8 -*-
"""Build 01-ccg/modules/m01_foundational.md from the CCG facts (US build)."""
import json
from ccglib import *

U = "m01_foundational"
set_unit(U)
o = []
A = o.append

A("# Module 1: Foundational Jurisdictional Parameters")
A("*Purpose: To establish the core environmental settings that govern all payroll operations.*")
A(H(2, "1.0 How the United States payroll system is organised"))
A("The United States is not one payroll jurisdiction but a stack of parallel layers. Every employee is "
  "routed to one federal core, one or more State layers and, in some places, a local layer; each layer "
  "computes its own amounts on its own base and is remitted to its own authority on its own return.")
A("")
A("| Layer | What the employer computes | Legal anchor (fact) |")
A("|---|---|---|")
A(f"| Federal income tax | Withholding under tables and procedures prescribed by the Secretary; covers federal tax only | {K('fed.fit.legal_basis.withholding_statute')} |")
A(f"| Federal social insurance (FICA) | Employee and employer OASDI and Medicare, reported on the quarterly return | {K('fed.fica.return_period')} |")
A(f"| Federal unemployment (FUTA) | Employer-only tax of {T('fed.futa.rate.gross')}% gross on wages paid in the calendar year, credited for State unemployment contributions | {K('fed.futa.legal_basis.rate_statute')}; {K('fed.futa.legal_basis.state_credit')}; {K('fed.futa.rate.gross')} |")
A("| State layer (50 States and the District of Columbia) | State income-tax withholding where the State taxes wages; State unemployment insurance (SUI); in some States disability, paid-leave or other payroll programmes | per-State annexes `annex_XX` |")
A(f"| Local layer | City, county, school-district or transit taxes in a minority of States | {COV('local_regimes')}; Module 6 §6.2 |")
A("")
A("**The FLSA is a floor, not a ceiling.** Where a State or municipality sets a more protective standard "
  f"the employer applies it: {Q('multi.wage_hour.overlay_rule')} {R('multi.wage_hour.overlay_rule')}.")
A("")
A("**States without a wage income tax.** The following States levy no income tax on wages in 2026; "
  "payroll in these States carries federal withholding, FICA, FUTA and the State programmes only.")
A("")
A("| State | No wage income tax | Effective | Source |")
A("|---|---|---|---|")
for st, name in [("ak", "Alaska"), ("nh", "New Hampshire"), ("nv", "Nevada"), ("sd", "South Dakota"),
                 ("tn", "Tennessee"), ("tx", "Texas"), ("wa", "Washington")]:
    k = f"{st}.no_wage_tax"
    f0 = FACTS[k][0]
    eff = f"from {f0['effective_from']}" + (f" to {f0['effective_to']}" if f0.get("effective_to") else "")
    A(f"| {name} | none levied | {eff} | {K(k)} |")
# round 2: the m01 open items fl/wy.no_wage_tax are answered by the annex facts fl.pit.exists / wy.pit.exists
for name, k in [("Florida", "fl.pit.exists"), ("Wyoming", "wy.pit.exists")]:
    f0 = FACTS[k][0]
    assert f0["value"] is False
    eff = f"from {f0['effective_from']}" + (f" to {f0['effective_to']}" if f0.get("effective_to") else "")
    A(f"| {name} | none levied | {eff} | {K(k)} |")
A("")
A(f"Washington: no wage income tax to {D('wa.no_wage_tax', which='to')} {R('wa.no_wage_tax')}. An enacted tax of "
  f"{T('wa.pit.high_income_tax.rate')}% on individuals with adjusted gross income above USD {T('wa.pit.high_income_tax.agi_threshold')} "
  f"applies from {D('wa.pit.high_income_tax.rate')}; it operates at assessment and is not modelled for payroll {R('wa.pit.high_income_tax.rate')}.")
A("")
A("**Live federal change.** Two Mobile Workforce bills are drafts and must not be modelled: "
  f"{Q('multi.mobile_workforce_bill.senate')} {R('multi.mobile_workforce_bill.senate')}; "
  f"{Q('multi.mobile_workforce_bill.house')} {R('multi.mobile_workforce_bill.house')}.")
A("")
A("**Calculation oracle.** "
  f"{Q('fed.oracle.source')} {R('fed.oracle.source')}. "
  f"{Q('fed.oracle.estimator_not_oracle')} {R('fed.oracle.estimator_not_oracle')}. State oracles are listed in Module 12.")
A("")
A("**Scope of this guide.** Private-sector employers and their common-law employees. " + CC.CONTRACTOR_SENTENCE +
  " All special employee populations are in scope at the federal layer (owner decision US-OWN-005); their treatment "
  "is in Module 11.")

A(H(3, "Tier verdict (build manifest)"))
A("Repeated verbatim from the build manifest (tier classification).")
A("")
A(f"**Overall:** {MAN('tier', 'overall')}")
A("")
A("| Domain | Tier |")
A("|---|---|")
for dom, tv in MAN("tier", "by_domain").items():
    A(f"| {dom} | {tv} |")
A("")
A("> **Rationale (verbatim):** " + MAN("tier", "rationale"))

# ---------------------------------------------------------------- 1.1
A(H(2, "1.1 Fiscal, Currency, and Language"))
A(H(3, "What is the statutory tax year?"))
A(f"The calendar year. Wage statements are prepared on a calendar-year basis: {Q('fed.tax_year.basis')} {R('fed.tax_year.basis')}. "
  f"FUTA is levied on {Q('fed.futa.legal_basis.rate_statute')} {R('fed.futa.legal_basis.rate_statute')}, and the "
  f"FICA and withholding return period is {Q('fed.fica.return_period')} {R('fed.fica.return_period')}.")
A("")
A("| Element | Period | Fact |")
A("|---|---|---|")
A(f"| Federal withholding, FICA, W-2 | Calendar year (1 January to 31 December) | {K('fed.tax_year.basis')} |")
A(f"| FUTA annual wage base | Calendar year, per employer | {K('fed.futa.wage_base')} |")
A(f"| Quarterly returns | Calendar quarter | {K('fed.fica.return_period')} |")
A("| State income-tax and SUI years | Per State annex | `annex_XX` |")
A(H(3, "Can employers adopt an alternate tax year? If yes, under what circumstances and what are the implications?"))
A("No for payroll purposes. Every payroll-tax period carried in the facts is fixed to the calendar year or the "
  f"calendar quarter ({K('fed.tax_year.basis')}; {K('fed.fica.return_period')}; {K('fed.futa.legal_basis.rate_statute')}), "
  "and no fact provides an employer election of a different payroll tax year. This is the mandate answer US-MQ-01 "
  "(build manifest `_year_note`: calendar year, no fiscal-year option). A corporate fiscal year chosen for income-tax "
  "accounting does not move any payroll period. Implication for configuration: the payroll year, every annual wage base "
  "and every year-to-date accumulator reset on 1 January.")
A(H(3, "What is the official currency for payroll processing and reporting? Provide the ISO code."))
A(f"United States dollar, ISO 4217 code **{MAN('currency')}**, {MAN('currency_minor_units')} minor units "
  "(build manifest `currency`, `currency_minor_units`). Payroll and all federal and State filings are in the same "
  "currency; no reporting currency differs from the payroll currency.")
A(H(3, "What is the official language for statutory reports and employee payslips?"))
A(f"English. {Q('fed.language.official')} {R('fed.language.official')}.")
A("")
A("| Document | Language rule | Basis |")
A("|---|---|---|")
A("| Employee pay statement | English | Owner decision US-OWN-006 (payslip language rule) |")
A("| Authority-facing filings (IRS, SSA, State agencies) | English | Owner decision US-OWN-006 (authority-facing language rule) |")
A("| Notices and posters in certain States | English plus Spanish or the employee's primary language where a State statute requires it | Owner decision US-OWN-006 (State notice seams); not a payroll-calculation item |")
A("")
A("No source read in the mandate census requires the pay statement itself in a language other than English; "
  "bilingual documents are permitted (`languages._bilingual_documents_permitted`).")

# ---------------------------------------------------------------- 1.2
A(H(2, "1.2 Pay Cycles and Dates"))
A(H(3, "What are the permissible payroll payment frequencies in the country?"))
A("Federal law sets no minimum pay frequency in the facts; the federal withholding tables support the following "
  f"pay periods per year: {Q('fed.fit.pay_periods_per_year')} {R('fed.fit.pay_periods_per_year')}. "
  "The binding minimum frequency and the maximum lag between period end and payday are State law. The work-location "
  "State's rule applies.")
A("")
A("| State | Statutory pay-frequency rule | Fact |")
A("|---|---|---|")
PF = []
for k in sorted(FACTS):
    if "pay_frequency" in k and len(k.split(".")[0]) == 2 and k.split(".")[0] not in ("mt",):
        PF.append(k)
for k in PF:
    st = k.split(".")[0].upper()
    if isinstance(FACTS[k][0]["value"], (int, float)):
        A(f"| {st} | maximum interval between paydays: {T(k)} days | {R(k)} |")
    else:
        A(f"| {st} | {Q(k)} | {R(k)} |")
A(f"| MT | Prevailing-wage work only: {Q('mt.prevailing_wage.pay_frequency')} | {R('mt.prevailing_wage.pay_frequency')} |")
A("")
ALL = [j.lower() for j in MAN("tier", "_jurisdictions") if len(j) == 2]
have = {k.split(".")[0] for k in PF}
missing = sorted(j.upper() for j in ALL if j not in have)
A(GAP("multi.pay_frequency.remaining_states",
      "the facts carry no general pay-frequency rule for " + ", ".join(missing) + " (Montana only for prevailing-wage work), and no federal statement that federal law sets none",
      "For " + ", ".join(missing) + " (Montana: general rule), what is the statutory minimum pay frequency and the maximum lag between period end and payday for private employers in 2026, and is it true that federal law (FLSA) prescribes no pay frequency?",
      "CCG m01 §1.2 pay-frequency table incomplete for " + str(len(missing)) + " States; DD pay-frequency validation per work State cannot be completed",
      "labour_code", tier="A.1",
      attempted=["_research/CCG-annex_*-facts.json keys *.pay_frequency.*", "_research/CCG-research-pack.md m01"],
      shape="one rule string per State with its statute section and effective date"))
A(H(3, "For each frequency, detail the corresponding statutory reporting and payment deadlines for both income tax withholding and social security contributions."))
A("At the federal layer the deposit deadline does **not** depend on the pay frequency. Federal income tax withheld and "
  "both shares of FICA are deposited together on one schedule fixed by the employer's lookback-period liability; the "
  "pay frequency only determines the paydays that start each deposit clock.")
A("")
A("| Obligation | Rule | Fact |")
A("|---|---|---|")
A(f"| Lookback period for 2026 | {Q('fed.deposit.lookback_period')} | {R('fed.deposit.lookback_period')} |")
A(f"| Monthly depositor | Lookback liability of USD {T('fed.deposit.monthly_max_lookback_liability')} or less: deposit by the 15th of the following month. Above it: semiweekly (Wednesday, Thursday or Friday paydays deposit by the following Wednesday; Saturday to Tuesday paydays by the following Friday) | {R('fed.deposit.monthly_max_lookback_liability')} |")
A(f"| Next-day rule | USD {T('fed.deposit.next_day_threshold')} or more accumulated on any day: deposit by the next business day; deposit holidays are District of Columbia legal holidays | {R('fed.deposit.next_day_threshold')} |")
A(f"| Quarterly return (FIT + FICA) | {Q('fed.form941.frequency')} (register row partial) | {R('fed.form941.frequency')} |")
A(f"| Annual Form 944 | Only on written IRS notice; liability ceiling USD {T('fed.form944.max_liability')} (register row partial) | {R('fed.form944.max_liability')} |")
A(f"| FUTA deposit | Deposit for a quarter when accumulated liability exceeds USD {T('fed.futa.deposit_threshold')} (register row partial) | {R('fed.futa.deposit_threshold')} |")
A(f"| FUTA annual return | {Q('fed.form940.due')} (register row partial) | {R('fed.form940.due')} |")
A(f"| W-2 to SSA and employees, tax year 2026 | {T('fed.w2.due_date')} | {R('fed.w2.due_date')} |")
A(f"| State unemployment | {Q('multi.ui_wage_report.routing')} | {R('multi.ui_wage_report.routing')} |")
A("| State income-tax withholding deposits and returns | Per State annex and Module 10 | `annex_XX` |")
A(H(3, "Describe the statutory rule for handling pay dates that fall on a weekend or public holiday."))
A("There is no federal rule in the facts. Where a State statute addresses it, the work-location State's rule applies:")
A("")
A("| State | Rule (extract of the State pay-frequency fact) | Fact |")
A("|---|---|---|")
for k, txt in [("de.pay_frequency.rule", "nonwork-day payday moves earlier"),
               ("id.pay_frequency.rule", "nonworkday payday moves earlier"),
               ("md.pay_frequency.rule", "nonworkday payday moves to preceding workday"),
               ("me.pay_frequency.rule", "closed-day payday moves to next business day")]:
    A(f"| {k.split('.')[0].upper()} | {txt} | {K(k)} |")
A("")
A("Federal deposit deadlines that fall on a deposit holiday move as stated in "
  f"{K('fed.deposit.next_day_threshold')} (deposit holidays are District of Columbia legal holidays).")
A("")
A(GAP("multi.payday.nonworkday_rule",
      "the payday-on-a-non-working-day rule is keyed for DE, ID, MD and ME only; the other States and the federal position are not in the facts",
      "For each State other than DE, ID, MD and ME, does a statute or regulation say whether a regular payday falling on a Saturday, Sunday or legal holiday moves earlier or later, and does any federal rule (FLSA) address it?",
      "CCG m01 §1.2 cannot state the payday-shift rule for 46 jurisdictions; the pay-calendar configuration has no rule to apply",
      "labour_code", tier="A.1", attempted=["_research/CCG-annex_*-facts.json *.pay_frequency.rule"],
      shape="per State: earlier / later / no rule, with section"))
A(H(3, "What are the common payroll pay dates and cut-off dates for payroll processing?"))
A("Statutory windows drive the calendar: several States fix the payday window by statute (for example "
  f"{K('ca.pay_frequency.rule')}, {K('oh.pay_frequency.rule')}, {K('mi.pay_frequency.rule')}, "
  f"{K('nm.pay_frequency.rule')}, {K('tx.pay_frequency.rule')}). The cut-off date is the last day of the pay period "
  "allowed by the work-location State's maximum lag (table above).")
A("")
A(GAP("practice.payroll_calendar.common_dates",
      "common (non-statutory) US pay dates and processing cut-offs by frequency are not in the facts",
      "What pay dates and payroll processing cut-off conventions are most common for US private employers by frequency (weekly Friday, biweekly, semimonthly 15th/last day, monthly), per a payroll-industry or government statistical source?",
      "CCG m01 §1.2 common pay dates question unanswered; payroll calendar defaults cannot be proposed",
      "labour_code", tier="A.2"))

# ---------------------------------------------------------------- 1.3
A(H(2, "1.3 Extra Pay Period Handling"))
A(H(3, "Describe the statutory handling and calculation adjustments required for fiscal years containing extra pay periods (e.g., 53 weekly pays)."))
# round 2: RQ-553 closed by agent 2 (fed.fit.extra_pay_period.rule, US-FEDQ1-007)
A("The federal method annualises each payment with the number of pay periods of its frequency "
  f"({Q('fed.fit.pay_periods_per_year')}; {R('fed.fit.pay_periods_per_year')}). A calendar year with 53 weekly "
  "paydays (or 27 biweekly paydays) does not change that divisor:")
A("")
A(f"- Rule: {Q('fed.fit.extra_pay_period.rule')} {R('fed.fit.extra_pay_period.rule')}.")
A("- Configuration: keep the pay-period count of the frequency (no 53 / 27 divisor); the extra payday is one more "
  "ordinary payroll period for income-tax withholding.")
A(H(3, "Detail the impact on annualized tax calculations and social security contributions."))
A("Social insurance is unaffected in method: the OASDI, FUTA and SUI bases are annual amounts applied to wages "
  f"**paid** in the calendar year ({COV('accrual_vs_payment')}). An extra payday falls in the year in which it is paid "
  f"and counts toward that year's bases (OASDI USD {T('fed.fica.oasdi.wage_base', on='2026-06-30')} for 2026; "
  f"FUTA USD {T('fed.futa.wage_base')} per employer). Income tax: each payday, including the extra one, is withheld "
  f"as a regular payroll period with the normal annualisation {R('fed.fit.extra_pay_period.rule')}; the year-end "
  "assessment on the employee's return settles any difference.")
A(H(3, "If optional adjustment methods are permitted, provide a step-by-step guide."))
A("No optional federal adjustment method exists: the IRS publications provide none for an extra payday "
  f"{R('fed.fit.extra_pay_period.rule')}. Steps: (1) keep the frequency's pay-period count in Worksheet 1A; "
  "(2) withhold the extra payday as an ordinary period; (3) apply FICA and FUTA to the wages paid, against the annual "
  "bases of the year of payment. State methods follow the State annex.")

# ---------------------------------------------------------------- 1.4
A(H(2, "1.4 Holiday Calendar"))
A(H(3, "What are the official public holidays?"))
# round 2: RQ-554 closed by agent 2 (fed.holiday.<name>.observed_date 2026 / 2027, fed.holidays.legal_public)
A(f"Federal legal public holidays: {Q('fed.holidays.legal_public')} {R('fed.holidays.legal_public')}. Federal "
  f"filing, furnishing and deposit dates roll forward under this rule: {Q('fed.deposit.due_date.non_business_day_rule')} "
  f"{R('fed.deposit.due_date.non_business_day_rule')}.")
A("")
A("| Holiday | 2026 observed date | 2027 observed date | Federal deposit / filing holiday |")
A("|---|---|---|---|")
for hk, lab in [("new_years_day", "New Year's Day"), ("mlk_birthday", "Birthday of Martin Luther King, Jr."),
                ("washingtons_birthday", "Washington's Birthday"), ("memorial_day", "Memorial Day"),
                ("juneteenth", "Juneteenth National Independence Day"), ("independence_day", "Independence Day"),
                ("labor_day", "Labor Day"), ("columbus_day", "Columbus Day"), ("veterans_day", "Veterans Day"),
                ("thanksgiving_day", "Thanksgiving Day"), ("christmas_day", "Christmas Day")]:
    k = f"fed.holiday.{hk}.observed_date"
    A(f"| {lab} | {T(k, on='2026-06-30')} {R(k, on='2026-06-30')} | {T(k, on='2027-06-30')} {R(k, on='2027-06-30')} | "
      "2026: yes (Pub. 15 2026 list); 2027: IRS list not yet published |")
k = "fed.holiday.dc_emancipation_day.observed_date"
A(f"| District of Columbia Emancipation Day (not a 5 U.S.C. 6103 holiday) | {T(k)} {R(k)} | not in the research | "
  "2026: yes (District of Columbia legal holiday) |")
A(H(3, "Are there any regional, state-specific, or company-specific holidays?"))
A(GAP("multi.holidays.state_2026",
      "State legal holidays (which affect State deposit due dates and some State payday rules) are not in the facts",
      "For each State, what are the 2026 State legal holidays that move State withholding or unemployment deposit and filing due dates?",
      "CCG m01 §1.4 State holiday table empty; State due-date roll-forward cannot be configured",
      "labour_code", tier="A.2"))
A("Company holidays are employer policy; no federal statute requires paid holidays for private employers in the facts "
  f"({K('fed.paid_leave.private_employers.exists')}).")

# ---------------------------------------------------------------- 1.5
A(H(2, "1.5 Rounding and Precision Rules"))
A(H(3, "What are the statutory or common business practice rules for rounding final net pay and individual calculation components?"))
A(f"Federal: {Q('fed.fit.rounding')} {R('fed.fit.rounding')}. No fact requires rounding of net pay; amounts are paid in "
  f"cents ({MAN('currency_minor_units')} minor units). State withholding rounding is set State by State:")
A("")
A("| Jurisdiction | Rounding rule | Fact |")
A("|---|---|---|")
for k in ["ia.wh.rounding", "id.wh.rounding", "ks.wh.rounding", "ky.wh.rounding", "ma.wh.rounding", "mn.pit.rounding",
          "mo.pit.rounding", "nc.pit.rounding", "nd.pit.rounding", "ny.pit.rounding", "ok.pit.rounding",
          "or.pit.rounding", "pa.pit.rounding", "ut.pit.rounding", "wi.pit.rounding", "fl.sui.rounding"]:
    A(f"| {k.split('.')[0].upper()} ({'unemployment' if '.sui.' in k else 'withholding'}) | {Q(k)} | {R(k)} |")
A("")
A("Build rule: compute every intermediate at full precision and round each statutory amount once, half-up to the cent, "
  "unless the jurisdiction's rule above rounds to the dollar; apply the optional federal whole-dollar rounding only if the "
  "employer elects it and then consistently.")
A("")
A(UNR("ky.wh.rounding.tax", "Kentucky: the 2026 formula sheet shows a bi-weekly result rounded down to whole dollars, while KRS 141.310(4) rounds only wages; the per-period rounding of the tax is not established"))
A(H(3, "What level of decimal precision is required for statutory reporting?"))
A(f"Cents on the quarterly federal return: {Q('fed.form941.amounts_in_cents')} {R('fed.form941.amounts_in_cents')}. "
  f"The annual wage statement file is a fixed-length record format ({T('fed.efw2.record_length')}-byte records, {R('fed.efw2.record_length')}); "
  "money-field layout is in the Report Specs. State filings follow each State's specification (Report Specs, annexes).")

write_module(U, "\n".join(o))
print("written", U)
