# -*- coding: utf-8 -*-
"""Build 01-ccg/modules/m06_tax.md from the CCG facts (US build)."""
import json
import os
from ccglib import *

U = "m06_tax"
set_unit(U)
o = []
A = o.append
ON = "2026-06-30"
EX = json.load(open(os.path.join(BASE, "01-ccg", "_examples", "m01_m07_examples.json"), encoding="utf-8"))

A("# Module 6: Income Tax Withholding System")
A("*Purpose: To define the entire income tax withholding system.*")

# ---------------------------------------------------------------- C31 matrix
A(H(2, "6.0 Resident vs non-resident matrix (federal income tax)"))
A("Resident = US citizen or resident alien; non-resident = nonresident alien (NRA). State residence is treated in §6.2. "
  f"Source rows: {COV('non_resident_employee')}; {COV('resident_employee')}.")
A("")
A("| Income type | Resident: rate, method, base | Non-resident alien: rate, method, base |")
A("|---|---|---|")
A(f"| Regular salary | Pub. 15-T Worksheet 1A, STANDARD or Step-2 schedule by filing status; base = income-tax wages annualised, less line 1g (USD {T('fed.fit.worksheet1a.line1g.other')} / USD {T('fed.fit.worksheet1a.line1g.mfj')} married filing jointly) when Step 2 is not checked {R('fed.fit.method')} | Same worksheet; Form W-4 per {Q('fed.fit.nra.w4.rule')} {R('fed.fit.nra.w4.rule')}; base = wages **plus** the NRA add-on (Table 2: USD {T('fed.fit.nra.addon.table2.annual', fmt='int')} a year; Table 1: USD {T('fed.fit.nra.addon.table1.annual', fmt='int')}), for the computation only: not on the W-2, no FICA/FUTA effect {R('fed.fit.nra.addon.table2.annual')} |")
A(f"| Annual / 13th-month bonus | Supplemental: flat {T('fed.fit.supplemental.flat_rate')}% (optional) or aggregate; {T('fed.fit.supplemental.mandatory_rate')}% mandatory above USD {T('fed.fit.supplemental.mandatory_threshold')} in the year {R('fed.fit.supplemental.flat_rate')} | Supplemental, same rates; the NRA add-on is **not** applied to the flat {T('fed.fit.supplemental.flat_rate')}% / {T('fed.fit.supplemental.mandatory_rate')}% methods {R('fed.fit.nra.addon.table2.weekly')} |")
A(f"| Severance | Wages for income tax, FICA and FUTA {K('fed.severance.is_wages')}; supplemental methods as for a bonus ({COV('termination_and_final_pay')}) | Wages; supplemental methods as for a bonus, NRA add-on not applied to the flat methods {R('fed.fit.nra.addon.table2.weekly')} |")
# round 2: RQ-505 / RQ-565 / RQ-566 closed by agent 2 (US-FEDQ1-001/-004/-006/-007/-008)
A(f"| Equity (stock options, RSUs) | {Q('fed.equity.withholding_treatment.resident')} {R('fed.equity.withholding_treatment.resident')}; "
  f"RSU FICA/FUTA timing: {Q('fed.equity.rsu.fica_timing')} {R('fed.equity.rsu.fica_timing')}; 83(i) deferred income withheld at "
  f"{T('fed.equity.83i.withholding_rate')}% {R('fed.equity.83i.withholding_rate')} | "
  f"{Q('fed.equity.withholding_treatment.nonresident')} {R('fed.equity.withholding_treatment.nonresident')} |")
A(f"| Labour-service pay | {CC.CONTRACTOR_SENTENCE} | Treaty-exempt personal-service wages: {Q('fed.fit.nra.treaty_exempt.reporting')} {R('fed.fit.nra.treaty_exempt.reporting')}; commercial-traveler exception: present at most {T('fed.fit.nra.commercial_traveler.max_days')} days and paid at most USD {T('fed.fit.nra.commercial_traveler.max_pay')} by a foreign employer {R('fed.fit.nra.commercial_traveler.max_days')} |")
# round 3 (QA r2 C31): social-security column of the matrix (FICA/FUTA), resident vs nonresident alien
_nra = nra_fica_text()
A(f"| Social security (FICA) and FUTA on wages | FICA (OASDI up to the annual wage base, Medicare) and FUTA on wages, as in Module 5 (5.1) "
  f"{R('fed.fica.oasdi.wage_base', on=ON)} {R('fed.futa.wage_base')} | "
  + ("As for residents, unless an exemption applies: " + _nra if _nra else
     "As for residents; the NRA withholding add-on has no FICA or FUTA effect. Nonresident-alien FICA/FUTA exemptions are not configured in this release")
  + " (Module 5, 5.1) |")
nb = f"{Q('fed.fit.nra.bik.treatment')} {R('fed.fit.nra.bik.treatment')}"
A(f"| Benefits in kind | Taxable fringe benefits are wages unless excluded (Module 7 §7.2); group-term life cost above USD {T('fed.bik.group_term_life.excluded_coverage')} is FICA wages and income-tax withholding is not required {R('fed.bik.group_term_life.excluded_coverage')} | {nb} |")

# ---------------------------------------------------------------- 6.1
A(H(2, "6.1 System Overview and Methodology"))
A(H(3, "Describe the country's income tax withholding system."))
A(f"Pay-as-you-earn withholding per pay period, in parallel layers. Federal: {Q('fed.fit.legal_basis.withholding_statute')} "
  f"{R('fed.fit.legal_basis.withholding_statute')}; method {Q('fed.fit.method')} {R('fed.fit.method')}. There is no employer "
  f"year-end income-tax regularisation: the employee settles at assessment ({COV('annual_regularisation')}). Each "
  "wage-taxing State runs its own withholding on its own base and return; some localities add a local layer. "
  "Routing (which State, which locality) is decided before any computation (§6.2).")
A(H(3, "What types of taxes are withheld by the employer?"))
A("| Tax withheld | Layer | Fact |")
A("|---|---|---|")
A(f"| Federal income tax | Federal | {R('fed.fit.legal_basis.withholding_statute')} |")
A(f"| Employee OASDI, Medicare, Additional Medicare | Federal (Module 5) | {R('fed.fica.oasdi.rate.employee')} |")
A("| State income tax | State, where the State taxes wages (Module 1 lists the States without one) | annexes |")
A(f"| Local income / wage / occupational taxes | Locality ({COV('local_regimes')}) | annexes |")
A("| Employee shares of State programmes (UI in AK/NJ/PA, SDI/TDI, PFML, WA Cares) | State (Module 5) | annexes |")
A("")
A(f"The facts also carry the federal backup-withholding rate, {T('fed.fit.backup_withholding.rate')}% {R('fed.fit.backup_withholding.rate')}.")
A(H(3, "At what level are tax rates published (central or state)?"))
A("Each layer publishes its own. Federal: IRS Pub. 15-T tables (§6.1.1). States publish their withholding formulas or "
  "tables; the withholding instrument does not always reproduce the statutory rates:")
A("")
A("| Pattern | State examples | Fact |")
A("|---|---|---|")
A(f"| Flat rate | Indiana {T('in.pit.rate', on=ON)}% in 2026 ({T('in.pit.rate', on='2027-06-30')}% from 2027) plus county tax; Utah {T('ut.pit.rate.flat')}%; Georgia {T('ga.pit.rate.flat')}% statutory for 2026 (withholding {T('ga.wh.rate', on='2026-03-01')}% to 2026-05-10, {T('ga.wh.rate', on='2026-06-30')}% from 2026-05-11 {R('ga.wh.rate', on='2026-03-01')}); Michigan {T('mi.pit.rate.flat')}% plus city taxes | {R('in.pit.rate', on=ON)}; {R('ut.pit.rate.flat')}; {R('ga.pit.rate.flat')}; {R('mi.pit.rate.flat')} |")
A(f"| Graduated | Maryland top rate {T('md.pit.top_rate')}% plus county tax (default county rate {T('md.local.county_rate.default_unknown')}%); California graduated tables (annex CA) | {R('md.pit.top_rate')}; {R('md.local.county_rate.default_unknown')} |")
A("| Statute differs from the withholding instrument | Ohio, Wisconsin, Nebraska, Kansas, South Carolina (trap table §6.2) | `practice.*` |")
A("| No wage income tax | Module 1 §1.0 | `*.no_wage_tax` |")

# ---------------------------------------------------------------- 6.1.1
A(H(2, "6.1.1 Taxable Income Definition"))
A(H(3, "Provide the statutory definition of 'Taxable Income'."))
# round 3b (QA r3 blocker 1, RQ-567 closed by agent 2 R3)
A("| Element | Rule | Source |")
A("|---|---|---|")
A(f"| Definition (26 U.S.C. 3401(a)) | {T('fed.fit.wage_definition')} | {R('fed.fit.wage_definition')} |")
A(f"| Exclusions | {T('fed.fit.wage_definition.exclusions')} | {R('fed.fit.wage_definition.exclusions')} |")
A("")
A("Operationally, the withholding base is the employee's income-tax wages for the period after the pre-tax "
  "deductions that reduce income-tax wages (Module 3, Step 2).")
A(H(3, "Explain how this base is derived from total gross earnings."))
A("```")
A("1a  wages_period      = gross - federally excluded pre-tax deductions   (+ NRA add-on for a nonresident alien)")
A("1c  annual_wages      = wages_period x pay_periods_per_year")
A("1e  = 1c + W-4 Step 4(a)")
A(f"1g  = {T('fed.fit.worksheet1a.line1g.mfj')} (MFJ) or {T('fed.fit.worksheet1a.line1g.other')} (other) if W-4 Step 2 NOT checked, else 0")
A("1h  = W-4 Step 4(b) + 1g")
A("1i  adjusted_annual   = max(0, 1e - 1h)")
A(f"    (pre-2020 W-4: adjusted_annual = annual_wages - allowances x {T('fed.fit.allowance.pre2020_value')})")
A("```")
A("")
A(f"Facts: {K('fed.fit.worksheet1a.line1g.mfj')}; {K('fed.fit.worksheet1a.line1g.other')}; {K('fed.fit.allowance.pre2020_value')}; "
  f"pay periods {Q('fed.fit.pay_periods_per_year')}.")
A(H(3, "Deliverable: Provide a step-by-step decision guide to determine the correct tax schedule for an employee."))
A("| Step | Question | Outcome | Fact |")
A("|---|---|---|---|")
A(f"| 1 | Which States and localities apply? | Work State, residence State and locality from the routing keys, then reciprocity, thresholds, convenience and federal transport limits (§6.2) | {R('multi.sit.work_location.rule')} |")
A(f"| 2 | Exempt checkbox on a 2026 W-4? | No federal income tax withheld for 2026 only | {R('fed.w4.exempt.validity')} |")
A(f"| 3 | Nonresident alien? | Single schedule regardless of marital status, no exempt, add NRA add-on (Table 2 if 2020+ W-4 or first paid 2020+, else Table 1) | {R('fed.fit.nra.w4.rule')}; {R('fed.fit.nra.addon.table1.annual')} |")
A(f"| 4 | Form W-4 from 2019 or earlier? | Allowances method, each worth USD {T('fed.fit.allowance.pre2020_value')} | {R('fed.fit.allowance.pre2020_value')} |")
A("| 5 | W-4 Step 2 checked? | Yes: Step-2 schedule, no line 1g. No: STANDARD schedule, line 1g subtracted | `fed.fit.step2.*`; `fed.fit.standard.*` |")
A("| 6 | Filing status? | Married filing jointly / Single or married filing separately / Head of household column | `fed.w4.input_fields` |")
A(f"| 7 | Supplemental payment? | Flat {T('fed.fit.supplemental.flat_rate')}% or aggregate; {T('fed.fit.supplemental.mandatory_rate')}% above USD {T('fed.fit.supplemental.mandatory_threshold')} | {R('fed.fit.supplemental.mandatory_threshold')} |")
A("| 8 | State schedule | The State's own certificate and method (annex); defaults for a missing certificate (Module 2) | annexes |")
A(H(3, "Deliverable: Explain the official tax calculation method with formulas and examples."))
A("```")
A("find row r of the schedule with floor_r <= adjusted_annual < floor_(r+1)")
A("2e excess    = adjusted_annual - floor_r")
A("2f           = excess x rate_r")
A("2g tentative = cumulative_tax_r + 2f")
A("2h period    = 2g / pay_periods_per_year")
A("3  credits   = W-4 Step 3 / pay_periods_per_year ;  4  extra = W-4 Step 4(c)")
A("FIT_period   = max(0, 2h - credits) + extra")
A("```")
A("")
A("**2026 Annual Percentage Method, STANDARD schedule (W-4 Step 2 not checked).** Floor and cumulative tax in USD; rate in %.")
A("")
A("| Row | MFJ floor | MFJ rate | MFJ cumulative | Single/MFS floor | Single rate | Single cumulative | HoH floor | HoH rate | HoH cumulative |")
A("|---|---|---|---|---|---|---|---|---|---|")
for i in range(1, 9):
    cells = []
    for s in ("mfj", "single", "hoh"):
        b = f"fed.fit.standard.{s}.bracket.{i}"
        cells += [T(b + ".floor"), T(b + ".rate"), T(b + ".cumulative_tax", fmt="money")]
    A(f"| {i} | " + " | ".join(cells) + " |")
A(f"\nSource {R('fed.fit.standard.single.bracket.1.floor')}; the standard deduction behind the zero bracket is USD "
  f"{T('fed.fit.std_deduction.single')} single, USD {T('fed.fit.std_deduction.mfj')} married filing jointly, USD "
  f"{T('fed.fit.std_deduction.hoh')} head of household {R('fed.fit.std_deduction.single')}.")
A("")
A("**Step-2-checked schedule (floors and rates; cumulative tax per the formula above).**")
A("")
A("| Row | MFJ floor | MFJ rate | Single/MFS floor | Single rate | HoH floor | HoH rate |")
A("|---|---|---|---|---|---|---|")
for i in range(1, 9):
    cells = []
    for s in ("mfj", "single", "hoh"):
        b = f"fed.fit.step2.{s}.bracket.{i}"
        cells += [T(b + ".floor"), T(b + ".rate")]
    A(f"| {i} | " + " | ".join(cells) + " |")
A(f"\nSource {R('fed.fit.step2.single.bracket.1.floor')}. Worked examples: §6.3. Oracle: {K('fed.oracle.source')}.")

# ---------------------------------------------------------------- 6.2
A(H(2, "6.2 Tax Rates and Logic"))
A(H(3, "What are the latest tax rates by tax type, residential status, and payment frequency?"))
A("Federal rates are the annual schedules of §6.1.1, identical for every frequency (applied after annualising). The NRA "
  "add-on is published per frequency:")
A("")
A("| Pay frequency | Table 2 add-on (USD) | Table 1 add-on (USD) |")
A("|---|---|---|")
for p in ["weekly", "biweekly", "semimonthly", "monthly", "quarterly", "semiannual", "annual", "daily"]:
    A(f"| {p} | {T('fed.fit.nra.addon.table2.' + p, fmt='money')} | {T('fed.fit.nra.addon.table1.' + p, fmt='money')} |")
A(f"\nSource {R('fed.fit.nra.addon.table2.weekly')}. Supplemental rates: §6.0. State rates: §6.1 and annexes.")
A("")
A(f"Special pay cycles and supplemental pay ({COV('special_pay_cycles')}): Pub. 15-T supports daily to annual periods "
  f"(annualise, then divide); supplemental pay is withheld at the flat {T('fed.fit.supplemental.flat_rate')}% or by the "
  f"aggregate method, {T('fed.fit.supplemental.mandatory_rate')}% mandatory above USD {T('fed.fit.supplemental.mandatory_threshold')}; "
  f"State supplemental rates are annex detail (examples in Module 4 §4.5: California {T('ca.wh.supplemental.rate.bonus_stock_options')}% bonus / {T('ca.wh.supplemental.rate.other')}% other).")
A("")
A("**Local layer (examples)**")
A("")
A("| Locality | Rate | Fact |")
A("|---|---|---|")
A(f"| Philadelphia, PA | Resident {T('pa.local.philadelphia.resident.rate', on=ON)}% / nonresident {T('pa.local.philadelphia.nonresident.rate', on=ON)}% to {D('pa.local.philadelphia.resident.rate', on=ON, which='to')}; resident {T('pa.local.philadelphia.resident.rate', on='2026-07-01')}% / nonresident {T('pa.local.philadelphia.nonresident.rate', on='2026-07-01')}% from {D('pa.local.philadelphia.resident.rate', on='2026-07-01')} | {R('pa.local.philadelphia.resident.rate', on='2026-07-01')} |")
A(f"| Detroit, MI | Resident {T('mi.local.detroit.rate.resident')}% / nonresident {T('mi.local.detroit.rate.nonresident')}%; annual exemption USD {T('mi.local.detroit.exemption.annual')} | {R('mi.local.detroit.rate.resident')} |")
A(f"| Louisville Metro, KY | {T('ky.local.louisville.rate.all_wages')}% on all wages earned in Louisville Metro; residents {T('ky.local.louisville.rate.resident_total')}% in total | {R('ky.local.louisville.rate.all_wages')} |")
A(f"| Maryland counties | Collected with the State return; default county rate {T('md.local.county_rate.default_unknown')}% | {R('md.local.county_rate.default_unknown')} |")
A(f"| Indiana counties | {Q('in.county.change_dates')} | {R('in.county.change_dates')} |")
A(f"| Ohio municipalities | Base: {Q('oh.local.municipal_base')} | {R('oh.local.municipal_base')} |")
A("")
A("Local taxes are outside State reciprocity (annex MULTI notes); W-2 boxes carry up to "
  f"{T('multi.w2.states_per_form')} States and localities per form {R('multi.w2.states_per_form')}.")
A(H(3, "How are rates applied for different frequencies?"))
A(f"Annualise, apply the annual schedule, divide back: line 1c multiplies by the pay periods of the frequency "
  f"({Q('fed.fit.pay_periods_per_year')}), line 2h divides by the same number {R('fed.fit.pay_periods_per_year')}. The NRA "
  "add-on is added per period from the table above. Several States round the per-period result (Module 1 §1.5).")
A(H(3, "How does tax applicability and calculation logic differ by residential status?"))
A("Federal: §6.0. State: a resident is taxed on all wages; a nonresident on wages for services performed in the State "
  f"({Q('multi.pit.sourcing.general')} {R('multi.pit.sourcing.general')}). Each State decides how it withholds for a "
  "resident working elsewhere:")
A("")
A("| State | Resident working in another State | Fact |")
A("|---|---|---|")
for st in ["ct", "ks", "vt", "ma", "ga", "nc", "co", "il", "ny", "ok", "oh", "la", "wi", "ms", "sc"]:
    k = f"multi.resident_out_of_state.{st}.withholding_rule"
    A(f"| {st.upper()} | {Q(k)} | {R(k)} |")
A("")
A("The credit for tax paid to another State is never a payroll deduction where it operates at assessment: "
  + ", ".join(f"{st.upper()} {R('multi.resident_credit.' + st + '.level')}" for st in ["sc", "ar", "ms", "dc", "me", "ri", "oh", "ok", "az"])
  + ".")
A("")
A("**Nonresident thresholds (work State withholds only above them)**")
A("")
A("| State | Threshold | Fact |")
A("|---|---|---|")
for k, lab in [("al.nonres.safe_harbor.days", "days"), ("multi.nonresident.az.threshold_days", "days"),
               ("multi.nonresident.ct.threshold_days", "days"), ("hi.nonres.exempt_days", "days"),
               ("multi.nonresident.il.threshold_days", "days"), ("multi.nonresident.la.threshold_days", "days"),
               ("multi.nonresident.me.threshold_days", "days"), ("mt.pit.nonresident.days_exemption", "days"),
               ("ne.pit.nonresident.duty_days", "days"), ("nm.pit.nonresident.days_threshold", "days"),
               ("multi.nonresident.ut.threshold_days", "days"), ("multi.nonresident.vt.threshold_days", "days"),
               ("multi.nonresident.wv.threshold_days", "days"), ("ga.nonres.threshold_amount", "USD"),
               ("multi.nonresident.id.threshold_amount", "USD"), ("multi.nonresident.mn.threshold_amount", "USD"),
               ("ok.pit.nonresident.quarterly_threshold", "USD per quarter"), ("wi.pit.nonresident.de_minimis", "USD")]:
    st = k.split(".")[2].upper()
    v = T(k)
    A(f"| {st} | {('USD ' + v + lab[3:]) if lab.startswith('USD') else (v + ' ' + lab)} | {R(k)} |")
for k in ["multi.nonresident.ca.allocation_rule", "multi.nonresident.ny.allocation_rule", "multi.nonresident.co.allocation_rule",
          "multi.nonresident.ar.allocation_rule", "multi.nonresident.ms.threshold_rule", "multi.nonresident.nd.threshold_rule",
          "multi.nonresident.la.employer_start_rule"]:
    A(f"| {k.split('.')[2].upper()} | {Q(k)} | {R(k)} |")
A("")
A(UNR("multi.nonresident.la.catch_up_rule"))
A("")
A("**Reciprocity** (work-State withholding stops on a certificate): partner table in Module 2 §2.2. "
  f"{Q('multi.reciprocity.az.unilateral')} {R('multi.reciprocity.az.unilateral')}. {Q('multi.reciprocity.dc.nonresident_exempt')} {R('multi.reciprocity.dc.nonresident_exempt')}.")
A("")
A("**Convenience-of-the-employer rules**")
A("")
A("| State | Rule | Fact |")
A("|---|---|---|")
for st in ["ny", "pa", "de", "ne", "nj", "ct", "ar"]:
    k = f"multi.convenience.{st}.rule"
    A(f"| {st.upper()} | {Q(k)} | {R(k)} |")
A(f"| All other States | {Q('multi.convenience.default')} | {R('multi.convenience.default')} |")
A("")
A("**Federal limits on State taxation**")
A("")
A("| Worker | Rule | Fact |")
A("|---|---|---|")
A(f"| Motor carrier | {Q('multi.transport.motor_carrier')} | {R('multi.transport.motor_carrier')} |")
A(f"| Rail | {Q('multi.transport.rail')} | {R('multi.transport.rail')} |")
A(f"| Air carrier | {Q('multi.transport.air_carrier')} | {R('multi.transport.air_carrier')} |")
A(f"| Seamen | {Q('multi.transport.seamen')} | {R('multi.transport.seamen')} |")
A(f"| Military spouse | {Q('multi.military_spouse.rule', on=ON)} | {R('multi.military_spouse.rule', on=ON)} |")
A(H(3, "Provide the tax calculation logic covering eligibility, joining month, termination month, mid-month joining, mid-month terminations, and mid-month salary revisions."))
A(f"Per pay period on the wages paid, with the period's frequency; no proration and no catch-up "
  f"({COV('mid_month_joiner_and_leaver')}). A salary revision changes the wages of the period in which it is paid. A "
  "terminated employee's final pay is withheld with the regular or supplemental method by its nature (Module 9).")
A("")
A(f"Mid-year changes are applied by **payment date** ({COV('mid_year_rate_change')}):")
A("")
A("| Change | Effective | Fact |")
A("|---|---|---|")
A(f"| Ohio withholding tables | {T('oh.wh.tables.effective_from')} | {R('oh.wh.tables.effective_from')} |")
A(f"| Philadelphia wage tax rates | {D('pa.local.philadelphia.resident.rate', on='2026-07-01')} | {R('pa.local.philadelphia.resident.rate', on='2026-07-01')} |")
A(f"| Indiana county rates | {Q('in.county.change_dates')} | {R('in.county.change_dates')} |")
A(f"| Idaho withholding tables (zero bracket single USD {T('id.wh.zero_bracket.single.annual', on='2026-08-01')} from {D('id.wh.zero_bracket.single.annual', on='2026-08-01')}; USD {T('id.wh.zero_bracket.single.annual', on='2026-03-01')} before) | {D('id.wh.zero_bracket.single.annual', on='2026-08-01')} | {R('id.wh.zero_bracket.single.annual', on='2026-08-01')} |")
A(f"| Georgia | {Q('practice.ga.rate_change_2026')} | {R('practice.ga.rate_change_2026')} |")
A(H(3, "Do tax rates vary by gender or age?"))
A("No. The federal schedules carried in the facts are keyed only by filing status and the W-4 Step 2 box "
  "(`fed.fit.standard.*`, `fed.fit.step2.*`); no gender or age dimension exists. States may add age-linked allowances: "
  f"{Q('ia.pit.obbba')} {R('ia.pit.obbba')}.")
A(H(3, "What is the minimum tax rate applicable?"))
A(f"{T('fed.fit.standard.single.bracket.1.rate')}% on the first row of every schedule: no federal income tax is withheld "
  f"until the adjusted annual wage reaches USD {T('fed.fit.standard.single.bracket.2.floor')} (single), USD "
  f"{T('fed.fit.standard.mfj.bracket.2.floor')} (married filing jointly) or USD {T('fed.fit.standard.hoh.bracket.2.floor')} "
  f"(head of household); the first positive rate is {T('fed.fit.standard.single.bracket.2.rate')}% {R('fed.fit.standard.single.bracket.2.rate')}.")
A("")
A("**Build traps (statute vs withholding instrument, assessment-only items)**")
A("")
A("| Jurisdiction | Rule for the engine | Fact |")
A("|---|---|---|")
for k in ["practice.sc.withholding_rates_2026", "practice.wi.use_w166_tables", "practice.ne.use_circular_en_tables",
          "practice.ks.kw100_header_stale", "practice.oh.flat_rate_vs_tables", "practice.mi.tips_ot_deduction_level",
          "practice.va.std_deduction_2027_not_modelled", "practice.ct.tables_vs_rules", "practice.hi.2027_tables_pending",
          "practice.al.fit_before_sit", "practice.or.federal_cap", "practice.fed.pl119_21_withholding",
          "practice.fed.estimator_not_oracle", "practice.dc.2026_method_unpublished"]:
    A(f"| {k.split('.')[1].upper()} | {Q(k)} | {R(k)} |")
A(f"| OH (statute) | {Q('oh.sit.statutory')} | {R('oh.sit.statutory')} |")
A(f"| AL, GA, IA, DC (tips / overtime) | Assessment only, no withholding change: Module 4 §4.4 | {R('al.pit.overtime_premium_deduction.max')}; {R('ga.pit.tip_subtraction.max')}; {R('ia.pit.obbba')}; {R('dc.pit.obbba_deductions')} |")
A("| HI (tips / overtime) | ⚠️ RESEARCH-GAP (non-blocking): level not in the facts (request `hi.pit.tips_overtime_deduction.level`, raised in Module 4) | |")
A(f"| ND | Method: {Q('nd.wh.method')}; the booklet's worked example is a recorded defect, use the method/table ({K('nd.oracle.section2_booklet.withholding')}) | {R('nd.wh.method')} |")
A("")
A(UNR("dc.oracle.method_2026"))
A("")
A(UNR("ut.oracle.pub14.examples.withholding", "Utah: the effective date of Pub 14 (Rev. 04/26) is not established, so its examples are not dated facts"))

# ---------------------------------------------------------------- 6.3
A(H(2, "6.3 Adjustments and Special Cases"))
A(H(3, "For annualized tax systems, which salary components must be projected?"))
A("None beyond the current period. Worksheet 1A annualises the current period's wages by multiplying by the pay "
  "periods; it does not project other components or year-to-date earnings. Supplemental pay withheld at the flat rate "
  f"is not annualised {R('fed.fit.supplemental.flat_rate')}.")
A(H(3, "Are year-end tax adjustments required?"))
A(f"No employer year-end income-tax adjustment: the employee reconciles at assessment ({COV('annual_regularisation')}). "
  f"The exempt status is renewed yearly ({Q('fed.w4.exempt.validity')}). 2027 parameters: "
  + UNR("fed.indexation.publication_2027"))
A(H(3, "Are there minimum or higher tax requirements if employees fail to submit a tax ID or social security number?"))
# round 3b (QA r3 blocker 1, RQ-568 closed by agent 2 R3)
A("| Situation | Federal rule | Source |")
A("|---|---|---|")
A(f"| New employee gives no Form W-4 in 2026 | Withhold as if the employee had entered: {T('fed.w4.default_no_certificate')} | {R('fed.w4.default_no_certificate')} |")
A(f"| Employee paid before 2020 with no Form W-4 on file | {T('fed.w4.default_no_certificate.pre2020_employee')} | {R('fed.w4.default_no_certificate.pre2020_employee')} |")
A(f"| Exempt status not renewed | {T('fed.w4.exempt_not_renewed.default')} | {R('fed.w4.exempt_not_renewed.default')} |")
A(f"| No SSN yet | {T('fed.ssn.not_issued.w2_rule')} | {R('fed.ssn.not_issued.w2_rule')} |")
A("")
A("State defaults for a missing State certificate are in Module 2 (for example "
  f"{K('ct.cert.default_no_certificate')}: flat withholding; {K('ca.cert.default_no_certificate')}).")
A(H(3, "What is the income tax and social security refund procedure?"))
A(f"Employee side: income tax and excess OASDI from several employers are refunded at assessment ({COV('multiple_employers')}). "
  "Employer side: corrections run through the federal correction returns.")
A("")
A(GAP("fed.employment_tax.adjustment_procedure",
      "the employer procedure to repay or reimburse over-withheld income tax or over-collected FICA in the same year and after year-end (26 CFR 31.6413, Forms 941-X / W-2c) is not in the facts",
      "Under 26 CFR 31.6413(a) and the Instructions for Form 941-X (2026), how does an employer repay or reimburse over-withheld federal income tax and over-collected employee FICA within the calendar year and after year-end, and what employee statements are required?",
      "CCG m06 §6.3 refund procedure unanswered; correction workflow of the engine has no rule",
      "statutory_reporting", tier="A.2"))
A(H(3, "Deliverable: Provide detailed worked examples for a standard resident employee, a non-resident employee, and an irregular payment."))
A("Computed by `01-ccg/_examples/build_examples_m01_m07.py` from the facts; each amount rounded half-up to the cent "
  "(Module 1 §1.5); full precision carried between lines.")
for exk, title in [("ex1", "Example 1: standard resident employee"), ("ex2", "Example 2: nonresident alien employee"),
                   ("ex3", "Example 3: irregular payment (bonus)")]:
    e = EX[exk]
    A(f"\n**{title}.** {e['scenario']}\n")
    if exk == "ex3":
        A("| Line | Base | Rate | Amount |")
        A("|---|---|---|---|")
        for r in e["fit"] + e["fica"]:
            A("| " + " | ".join(r) + " |")
    else:
        A("| Line | Calculation | Result |")
        A("|---|---|---|")
        for r in e["fit"]:
            A("| " + " | ".join(r) + " |")
        A("")
        A("| Line | Base | Rate | Amount |")
        A("|---|---|---|---|")
        for r in e["fica"]:
            A("| " + " | ".join(r) + " |")
    A("")
    A("| Line | Calculation | Result |")
    A("|---|---|---|")
    for r in e["net"]:
        A("| " + " | ".join(r) + " |")
A("")
A("State and local withholding for these employees depends on the work and residence State (annex worked examples, "
  "Module 12).")

write_module(U, "\n".join(o))
print("written", U)
