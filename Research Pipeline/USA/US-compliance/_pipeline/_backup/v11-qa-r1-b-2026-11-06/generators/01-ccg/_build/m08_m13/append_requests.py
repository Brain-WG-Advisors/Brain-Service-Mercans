# -*- coding: utf-8 -*-
"""Append the RESEARCH-GAP requests of units m08-m13 + coverage to the shared
_research/CCG-research-request.json (re-read immediately before writing; ids continue;
a key already requested is not repeated)."""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
REQ = os.path.join(BASE, "_research", "CCG-research-request.json")
MOD = os.path.join(BASE, "01-ccg", "modules")
sys.path.insert(0, HERE)
from factlib import clean  # noqa: E402

Q = {  # key: (unit, domain, tier, question, why, expected_shape)
    "fed.fmla.eligibility": ("m08_leave", "leave", "A.1", "What are the FMLA employer-coverage threshold and the employee-eligibility conditions (months of service, hours in the prior 12 months, worksite headcount radius) under 29 U.S.C. 2611 and 29 CFR 825.110?", "CCG m08 8.1 cannot state FMLA eligibility criteria; DD cannot flag FMLA-eligible employees.", "numbers with the statute section"),
    "fed.eo13706.sick_leave.accrual": ("m08_leave", "leave", "A.1", "What are the accrual rate (hours per hours worked) and the annual accrual cap of paid sick leave for federal contractors under Executive Order 13706 (29 CFR 13.5)?", "CCG m08 8.1 federal-contractor paid sick leave row cannot be written.", "two numbers with the 29 CFR 13.5 citation"),
    "multi.sick_leave.coverage_threshold": ("m08_leave", "leave", "A.1", "For each State with a paid-sick-leave law, which employees working partly in the State are covered (hours or days threshold in the State)?", "CCG m08 Table 8.1.1 cannot route multistate employees to a sick-leave regime.", "per State: threshold and statute"),
    "multi.paid_sick_leave.state_census": ("m08_leave", "leave", "A.1", "For the States absent from CCG m08 Table 8.1.1 (listed under the table), is a statewide paid-sick-leave statute in force in 2026, and if so what are its accrual ratio, caps and employer threshold?", "CCG m08 Table 8.1.1 lists these States with no key either way.", "per State: boolean exists + parameters + statute"),
    "fed.pfml.employer_top_up.treatment": ("m08_leave", "income_tax", "A.2", "How is an employer supplement paid alongside a State PFML/TDI benefit treated for FIT, FICA and FUTA, and on which form is it reported?", "CCG m08 8.1 partially-paid-leave answer cannot give the employer top-up treatment.", "treatment per tax with IRS source"),
    "fed.userra.leave_rules": ("m08_leave", "leave", "A.1", "What USERRA rules (38 U.S.C. 4301-4335) bind payroll: maximum cumulative service period, benefit and pension continuation during military leave, and the tax treatment of differential pay?", "CCG m08 8.1 military-service-leave answer is a gap.", "rules with statute sections"),
    "multi.final_pay.state_census": ("m09_termination", "termination", "A.1", "What are the final-pay deadlines on discharge and on resignation in the States listed under CCG m09 Table 9.1.1 (or the statement that no State statute sets one)?", "CCG m09 Table 9.1.1 lists these States with no key.", "per State: rule string + statute, or boolean absence"),
    "fed.vacation_payout.supplemental_status": ("m09_termination", "income_tax", "A.2", "Is accrued vacation pay paid out at separation, separately from regular wages, a supplemental wage eligible for the federal optional flat-rate method (Pub. 15 section 7, 26 CFR 31.3402(g)-1), and is it FICA/FUTA wages?", "CCG m09 9.1 withholding rule for unused leave paid at termination cannot be stated.", "classification + citation"),
    "fed.backpay.treatment": ("m09_termination", "income_tax", "A.2", "How are back pay and retroactive pay increases classified for federal withholding (supplemental or regular wages) and for FICA (year of payment), per Pub. 15 and Pub. 957?", "CCG m09 9.2 retroactive-adjustment method is a gap.", "classification + citation"),
    "fed.form940.instructions_current": ("m10_reporting", "statutory_reporting", "A.2", "Have the tax-year 2026 Instructions for Form 940 and Forms 1094-C/1095-C been issued, and do they change any due date, threshold or line used in the CCG?", "CCG m10 Table 10.1.1 rests on the 2025 editions.", "edition date + changed items"),
    "multi.newhire.registration_channel": ("m10_reporting", "statutory_reporting", "A.2", "Through which HHS/OCSS channel (form or portal) does a multistate employer notify its designated new-hire reporting State?", "CCG m10 10.1 multistate new-hire designation channel is a gap.", "form/portal name + URL"),
    "fed.iwo.revised_form.state_golive": ("m10_reporting", "deductions_garnishments", "A.2", "On which dates do the States go live with the revised IWO / e-IWO (gig-worker fields) approved under ICR 202607-0970-002?", "CCG m10 10.2 inbound IWO integration cannot date the format change.", "per State date or the OCSS action transmittal"),
    "multi.payroll_software.certification": ("m10_reporting", "statutory_reporting", "A.2", "Which States require payroll service providers or payroll software to register, test or be certified before filing (beyond Wisconsin)?", "CCG m10 10.4 software-certification answer covers one State only.", "per State: requirement + source"),
    "fed.indexation.publication_2027": ("m10_reporting", "indexation", "A.2", "What are the tax-year 2027 IRS inflation adjustments relevant to payroll (Pub. 15-T 2027 tables, 2027 retirement-plan limits)?", "CCG m10 10.5 year-end roll-forward cannot list 2027 values.", "dated facts effective 2027-01-01"),
    "fed.fit.supplemental.aggregate_method": ("m11_advanced", "income_tax", "A.2", "What is the Pub. 15 (2026) section 7 aggregate procedure for a supplemental payment made with, or after, the regular wages of the period (including subtraction of tax already withheld)?", "CCG m11 11.1 multiple-payments-in-a-period answer is a gap.", "procedure steps with citation"),
    "fed.fit.pay_frequency_change": ("m11_advanced", "income_tax", "A.2", "What rule applies to federal withholding when an employee's payroll period changes during the year, or for a short transitional period (Pub. 15-T miscellaneous pay period rules)?", "CCG m11 11.1 pay-cycle change answer is a gap.", "rule with Pub. 15-T citation"),
    "fed.common_paymaster.rule": ("m11_advanced", "social_security", "A.1", "What are the conditions of common-paymaster relief for related corporations under IRC 3121(s), and the successor-employer rule for the OASDI and FUTA wage bases?", "CCG m11 11.2 multiple-employer and entity-transfer answers, and coverage row multiple_employers, carry a gap.", "rules with IRC/CFR sections"),
    "fed.equity.compensation_treatment": ("m11_advanced", "income_tax", "A.2", "How are nonstatutory stock options, ISOs, ESPP and RSUs treated for federal withholding, FICA and FUTA (income timing, supplemental status, W-2 box 12 codes)?", "CCG m11 11.2 stock-option answer is a gap.", "per instrument: treatment + citation"),
    "fed.nra.residency_change": ("m11_advanced", "income_tax", "A.2", "How does withholding change when an employee becomes a US resident alien during the year (dual-status year): W-4 replacement, removal of the nonresident add-on, end of the FICA exemption for F/J/M/Q holders?", "CCG m11 11.2 residency-change answer is a gap.", "rules with Pub. 515/519 citation"),
    "fed.bik.business_mileage.rate": ("m11_advanced", "benefits_in_kind", "A.2", "What is the 2026 IRS business standard mileage rate (notice number)?", "CCG m11 fringe-benefit table row is a gap.", "cents per mile, effective 2026-01-01"),
    "practice.offcycle_payments": ("m13_practices", "labour_code", "A.2", "What employer conventions govern off-cycle payroll runs (when used, choice between the flat and aggregate supplemental methods, State limits on separate checks)?", "CCG m13 off-cycle practice answer is partly a gap.", "practice statements with sources"),
    "practice.commission_draw": ("m13_practices", "labour_code", "A.1", "How are recoverable and non-recoverable commission draws treated (wage status when advanced, recovery limits under federal and State minimum-wage and wage-deduction law)?", "CCG m13 commission-draw answer is a gap.", "rules with FLSA/State citations"),
    "practice.non_statutory_leave": ("m13_practices", "leave", "A.2", "Which non-statutory leave types are prevalent among US employers (bereavement, floating holidays, volunteer days) and how are they paid and reported?", "CCG m13 non-statutory leave answer is a gap.", "list with source (e.g. BLS National Compensation Survey)"),
    "ma.pfml.split.effective_date": ("m13_practices", "social_security", "A.1", "From which date does the Chapter 101 of 2026 family/medical PFML contribution split apply: taxable years from 2026-01-01 (s.45) or 2027-01-01 (DFML implementation)?", "CCG m13 open practice point; m05 and WTC Massachusetts PFML split depend on it.", "date + DFML notice or 458 CMR amendment"),
    "practice.dol_paid_leave_list": ("m13_practices", "leave", "A.2", "Saved copy of the current U.S. DOL Women's Bureau State paid-leave compilation, to restore the reverted rows (never to be used for Michigan).", "CCG m13 open practice point; State paid-leave census cross-check.", "local saved copy + edition date"),
    "ut.oracle.pub14.examples.withholding": ("m13_practices", "income_tax", "A.2", "What is the effective date of Utah Pub. 14 (Rev. 04/26) withholding tables and of its supplemental rate?", "CCG m12 cannot carry the six Utah examples as dated oracle facts; m13 open point.", "date with Tax Commission source"),
    "dc.oracle.method_2026": ("m13_practices", "income_tax", "A.2", "What is the District of Columbia 2026 withholding method after D.C. Act 26-416 (or the permanent FY2027 act): tables or formula, and the revised D-4?", "CCG m12 has no DC oracle; m13 open point; WTC DC withholding blocked.", "method + tables with OTR source"),
    "multi.workers_comp.employee_share": ("coverage", "social_security", "A.1", "Which States other than New Mexico and Washington allow or require an employee contribution or deduction for workers' compensation, and at what rate or amount?", "CCG coverage row work_accident_occupational_disease is partly a gap.", "per State: rule + amount + statute"),
    "fed.retirement.401k.wage_treatment": ("m12_worked_examples", "income_tax", "A.2", "How are 401(k) elective deferrals and section 125 cafeteria-plan salary reductions treated for federal income tax withholding, OASDI/Medicare and FUTA wages (Pub. 15, Pub. 15-B)?", "CCG m12 pre-tax gross-to-net example cannot be computed.", "per plan: FIT yes/no, FICA yes/no, FUTA yes/no with citation"),
    "fed.student_loan.payroll_obligation": ("m12_worked_examples", "deductions_garnishments", "A.1", "Is there a federal payroll obligation for student-loan repayment (administrative wage garnishment under 20 U.S.C. 1095a / 31 CFR 285.11): maximum percentage, notice, priority?", "CCG m12 student-loan example cannot be computed.", "limits with statute"),
    "ny.oracle.nys50t.example2.withholding": ("m12_worked_examples", "income_tax", "A.2", "Which rounding convention does NYS-50-T-NYS Method II apply (example 2 prints a figure one cent above half-up arithmetic)?", "CCG m12 NY oracle example 2 cannot be used as an expected result.", "rounding rule with DTF source or calculator result"),
    "ky.oracle.biweekly_1500.withholding": ("m12_worked_examples", "income_tax", "A.2", "What per-period rounding does the Kentucky 2026 withholding formula apply (the formula sheet shows a whole-dollar result without a stated rule)?", "CCG m12 KY oracle cannot be used as an expected result.", "rounding rule with DOR KY source"),
    "md.oracle.calculator": ("m12_worked_examples", "income_tax", "A.2", "What does the Maryland Comptroller withholding calculator return for a fixed case (e.g. single, 0 exemptions, biweekly 2,000.00, Baltimore City)?", "CCG m12 has no MD oracle.", "calculator inputs/outputs with run date"),
}
FILES = {"m08_leave": "m08_leave.md", "m09_termination": "m09_termination.md", "m10_reporting": "m10_reporting.md",
         "m11_advanced": "m11_advanced.md", "m12_worked_examples": "m12_worked_examples.md",
         "m13_practices": "m13_practices.md", "coverage": "coverage.md"}

MARKERS = {}
for loc, text, key in json.load(open(os.path.join(HERE, "out", "gaps_modules.json"), encoding="utf-8")):
    MARKERS.setdefault(key, (loc, text))
for loc, text, key in json.load(open(os.path.join(BASE, "01-ccg", "_examples", "out", "gaps_examples.json"), encoding="utf-8")):
    MARKERS.setdefault(key, (loc, text))


def locate(key):
    loc, text = MARKERS[key]
    text = clean(text)
    fname = loc.split(" ")[0]
    lines = open(os.path.join(MOD, fname), encoding="utf-8").read().split("\n")
    sec = "header"
    for i, line in enumerate(lines, 1):
        if line.startswith("#"):
            sec = line.lstrip("# ").strip()[:80].replace("!", "")
        if "RESEARCH-GAP" in line and text[:50] in line:
            return f"01-ccg/modules/{fname}!{sec}!L{i}"
    raise SystemExit(f"marker for {key} not found in {fname}")


def main():
    missing = set(MARKERS) - set(Q)
    if missing:
        raise SystemExit(f"gap keys without a request definition: {sorted(missing)}")
    d = json.load(open(REQ, encoding="utf-8"))      # re-read immediately before writing
    have = {r["key"] for r in d["requests"]}
    n = max(int(r["id"][3:]) for r in d["requests"])
    added = []
    for key, (unit, dom, tier, q, why, shape) in Q.items():
        if key in have:
            continue
        n += 1
        if n > 999:
            raise SystemExit("request id space exhausted (RQ-999)")
        where = locate(key)
        d["requests"].append({
            "id": f"RQ-{n:03d}", "key": key, "location": where, "question": q, "why_blocking": why,
            "domain": dom, "acceptable_tier": tier,
            "attempted_by_requester": [f"_research/CCG-{unit}-facts.json facts[] and unresolved[]",
                                       "_research/CCG-research-pack.md",
                                       "all _research/*-facts.json keys searched (FED, MULTI and State annexes, WTC, PSL, SIR, RSPEC, DD)"],
            "severity": "minor", "expected_shape": shape,
            "_unit": unit, "_blocking": False, "_placeholder_written": "RESEARCH-GAP marker at " + where})
        added.append(f"RQ-{n:03d} {key}")
    json.dump(d, open(REQ, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(len(added), "appended")
    for a in added:
        print(" ", a)


if __name__ == "__main__":
    main()
