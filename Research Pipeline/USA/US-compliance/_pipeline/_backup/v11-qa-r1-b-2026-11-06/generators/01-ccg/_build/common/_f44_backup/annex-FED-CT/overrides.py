"""Glue between build_annexes.py and the hand-written content (content.py)."""
import content as C

INTRO = C.INTRO
SECTION_TEXT = C.SECTION_TEXT
AFTER = C.AFTER
TAIL = C.TAIL
PLACE = C.PLACE
TITLES = C.TITLES
PIVOTS = C.PIVOTS
GAP_TOPIC = C.GAP_TOPIC
GAP_CLOSE = {
    ("CT", "ct.wh.tables.per_period"): "the DRS withholding tables in IP 2026(1) transcribed as keyed per-period tables, together with the owner's choice of engine method (rules or tables)",
    ("CT", "ct.payslip.consolidated_text_lag"): "a consolidated text of 31-13a that includes PA 26-12 s.38; until then PA 26-12 governs",
    ("MULTI", "multi.sui.other_state_wage_credit.ar"): "the Arkansas UI handbook page that states the transfer-credit clause, registered as a source",
    ("MULTI", "multi.nonresident.sc.threshold"): "SC Code 12-8-520(A) reconciled with the SC DOR withholding guide (WH-1603F / WH105)",
    ("AR", "ar.wh.formula.switch_date"): "the DFA withholding release or notice of May 2026 announcing the start date of the reissued formula (the Act itself does not state it)",
    ("AR", "ar.live.bulletin_sweep"): "the arkleg Acts index for the 2025 Regular and 2026 Fiscal Sessions",
    ("AZ", "az.live.bulletin_sweep"): "the ADOR news archive and DES employer bulletins for 2026",
    ("AZ", "az.report.w2.pub701_edition"): "the ADOR Pub 701 2026 edition",
    ("AR", "ar.garn.iwo.employer_fee"): "the OCSE employer guide or Ark. Code 9-14-218 / 9-14-226",
    ("CO", "co.famli.split.next_year"): "7 CCR 2702-3 and C.R.S. 8-13.3-507 on famli.colorado.gov or in the Colorado Register",
    ("CO", "co.leave.sick.amendments_and_payslip_econsent"): "the current Healthy Families and Workplaces Act text and CDLE INFO #6 / #13",
    ("FED", "fed.fica.oasdi.wage_base.next_year_reverification"): "the SSA 2027 COLA fact sheet or contribution-and-benefit-base page, or the 2027 Federal Register notice",
    ("FED", "fed.leave.eo13706.accrual"): "29 CFR 13.5 on eCFR",
    ("MULTI", "multi.newhire.multistate_registration_channel"): "the ACF multistate employer registration page",
    ("MULTI", "multi.sui.other_state_wage_credit.la"): "R.S. 23:1536",
    ("AK", "ak.garn.iwo.employer_fee"): "AS 25.27.062 on the Alaska Legislature site, or the CSED ACSESS Business Portal employer guide",
    ("AK", "ak.live.bulletin_sweep"): "the Alaska Administrative Register issues for 2026 and the BASIS passed-legislation list of the 34th Legislature",
    ("CT", "ct.live.public_act_texts"): "the Public Act PDFs on cga.ct.gov",
    ("CT", "ct.garn.employer_fee"): "a full read of 52-362 and 52-361a(j)-(k)",
    ("CO", "co.local_minwage.other_cities"): "the coloradolaborlaw.gov local minimum wage list or each city or county notice (Edgewater, Boulder, Boulder County) and the Denver 2027 rate notice",
    ("CA", "ca.local_minwage.hourly"): "each city labour-standards office bulletin for the 2026-07-01 and 2027-01-01 rates",
    ("AL", "al.local.occupational_tax.census"): "the Alabama League of Municipalities occupational-tax list, then each city ordinance or tax page (Birmingham, Auburn, Bessemer, Gadsden, Opelika, Fairfield, Macon County)",
    ("AL", "al.garn.iwo.employer_fee"): "Ala. Code 30-3-60 to 30-3-71 in full, or the DHR Child Support employer page",
    ("AL", "al.live.overtime_withholding_exemption.end_date"): "the ADOR page on the overtime pay exemption as amended by Act 2024-437",
}
_AL_PHASE = "Phase-out steps by gross income are in the source booklet and carry no facts key (gap in AL.2)."
NOTES = {
    ("AL", "al.wh.std_deduction.single.max"): _AL_PHASE,
    ("AL", "al.wh.std_deduction.married.max"): _AL_PHASE,
    ("AL", "al.wh.std_deduction.married_separate.max"): _AL_PHASE,
    ("AL", "al.wh.std_deduction.head_of_family.max"): _AL_PHASE,
    ("AL", "al.wh.personal_exemption.single"): "Status 0: no exemption; single and married filing separately: this amount; married and head of family: {{al.wh.personal_exemption.married}}.",
    ("AL", "al.wh.dependent.gi_to_50000"): "Per dependent, by the employee's gross-income band (amounts in the next two rows).",
    ("FED", "fed.bik.dependent_care.exclusion"): "Half for married filing separately; raised by P.L. 119-21.",
    ("CT", "ct.tipped.employer_share.hotel_restaurant"): "Fixed employer cash wage; maximum tip credit 2026 {{ct.tipped.max_tip_credit.hotel_restaurant}} (minimum wage {{ct.minwage.hourly@2026-01-01}} less the employer share). Bartenders: employer share {{ct.tipped.employer_share.bartender}}. Other industries and meal credits: in the source. No cannabis tip credit from 2026-10-01 (PA 26-12 s.6).",
    ("CO", "co.sui.new_employer.rate.total"): "Sum of the base rate, the support surcharge and the solvency surcharge for non-construction employers; heavy-construction and 2027 rates are in the source and carry no facts key.",
    ("CA", "ca.sui.employer.rate.min"): None,
}
KEEP_PACK = set()
EXTRA_SRC = {}

GAPSEC = {
    ("MULTI", "multi.nonresident.la.catch_up_rule"): "2",
    ("MULTI", "multi.nonresident.sc.threshold"): "2",
    ("MULTI", "multi.convenience.ny.litigation_status"): "2",
    ("MULTI", "multi.ca.minimum_wage.nonresident_reach"): "1",
    ("MULTI", "multi.paid_sick_leave.multistate_scope"): "1",
    ("AZ", "az.ui.separation_notice_and_domestic_threshold"): "3",
    ("AZ", "az.minwage.statute_23_362_current"): "1",
    ("AZ", "az.pit.departures_from_federal"): "8",
    ("AR", "ar.pit.wages.hsa_transit_gtl"): "8",
    ("AL", "al.pit.wages.transit_group_term_life"): "8",
    ("CT", "ct.pit.departures_from_federal"): "8",
    ("CA", "ca.hsa.conformity_2026"): "8",
    ("CA", "ca.local_minwage.hourly"): "1",
    ("CA", "ca.industry_minwage.fast_food_health_care"): "1",
    ("CA", "ca.warn.employer_threshold"): "7",
    ("CA", "ca.overtime.agricultural_phase_in"): "1",
    ("CO", "co.local_minwage.other_cities"): "1",
    ("CO", "co.famli.split.next_year"): "3",
    ("CO", "co.data_protection.statutes"): "12",
    ("CO", "co.local.opt.denver.current_edition"): "2c",
    ("AK", "ak.sui.wage_base.derivation"): "3",
    ("AK", "ak.sui.wage_base.next_year"): "3",
    ("FED", "fed.leave.eo13706.accrual"): "6",
    ("FED", "fed.indexation.next_year"): "11",
    ("FED", "fed.form940.instructions_edition"): "5",
    ("FED", "fed.aca.instructions_edition"): "5",
    ("FED", "fed.bik.mileage_rate"): "8",
    ("FED", "fed.iwo.revised_form_go_live"): "9",
    ("FED", "fed.futa.credit_reduction.ca"): "3",
    ("FED", "fed.futa.credit_reduction.vi"): "3",
    ("FED", "fed.fica.oasdi.wage_base.next_year_reverification"): "3",
}


def intro(u):
    return INTRO.get(u, [])


def section_text(u, sid):
    v = SECTION_TEXT.get((u, sid))
    if isinstance(v, str) and v in C.EXAMPLES:
        return C.EXAMPLES[v]
    return v


def keep_pack_prose(u, sid):
    return (u, sid) in KEEP_PACK


def after_section(u, sid):
    return AFTER.get((u, sid), [])


def tail(u):
    return TAIL.get(u, [])


def place(u, key):
    return PLACE.get((u, key))


def default_section(u, f):
    k = f["key"]
    if ".report" in k or ".efw2" in k or ".newhire" in k:
        return "5"
    # round 3b: facts added by agent 2 R3 without a _domain (CA married/HoH bands, AL phase-out) go to the
    # section of their key prefix instead of 13 (Live legal change)
    return gap_section(u, k)


def gap_section(u, key):
    if (u, key) in GAPSEC:
        return GAPSEC[(u, key)]
    k = key.split(".", 1)[1] if "." in key else key
    for pre, s in [("minwage", "1"), ("overtime", "1"), ("pay", "1"), ("paycard", "1"), ("wh.", "2"), ("pit", "2"),
                   ("fit", "2"), ("nonres", "2b"), ("reciprocity", "2b"), ("local", "2c"), ("sui", "3"), ("sdi", "3"),
                   ("pfml", "3"), ("famli", "3"), ("fica", "3"), ("futa", "3"), ("ui.", "3"), ("payslip", "4"),
                   ("report", "5"), ("newhire", "5"), ("efw2", "5"), ("aca", "5"), ("leave", "6"), ("final_pay", "7"),
                   ("warn", "7"), ("bik", "8"), ("hsa", "8"), ("garn", "9"), ("ccpa", "9"), ("iwo", "9"),
                   ("prevailing", "10"), ("index", "11"), ("data", "12"), ("records", "12"), ("live", "13")]:
        if k.startswith(pre):
            return s
    return "13"


def rewrite(u, line):
    return line


def keep_pipe_line(u, line):
    return False


def note(u, key, n):
    if (u, key) in NOTES and NOTES[(u, key)] is not None:
        return NOTES[(u, key)]
    for (uu, pre), reps in NOTE_REPS.items():
        if uu == u and key.startswith(pre):
            for a, b in reps:
                n = n.replace(a, b)
    return n


NOTE_REPS = {
    ("FED", "fed.fit.nra.addon"): [("16,100 - 4,300", "{{fed.fit.std_deduction.single}} - {{fed.fit.allowance.pre2020_value}}"),
                                   ("Annual 11,800", "Annual {{fed.fit.nra.addon.table1.annual}}"),
                                   ("single standard deduction 16,100", "single standard deduction {{fed.fit.std_deduction.single}}")],
    ("CO", "co.famli"): [("0.44% employer + 0.44% employee", "{{co.famli.employer.rate}} % employer + {{co.famli.employee.rate}} % employee"),
                         ("SS wage base (184,500)", "SS wage base ({{fed.fica.oasdi.wage_base@2026-01-01}})"),
                         ("only the 0.44% employee share", "only the {{co.famli.employee.rate}} % employee share")],
    ("FED", "fed.levy"): [("16,100", "{{fed.fit.std_deduction.single}}")],
    ("CA", "ca.sui"): [("max 434/employee", "max {{ca.sui.max_per_employee}}/employee")],
    ("AR", "ar.pit.high_income"): [("4,701+ 3.7%", "4,701+ {{ar.pit.rate.top}} %")],
}


def section_title(u, sid):
    return TITLES.get((u, sid))


def after_bracket(u, fam, W):
    for p in AFTER.get((u, "bracket:" + fam), []):
        W(p)
        W("")


def extra_sources(u):
    return set(EXTRA_SRC.get(u, []))


def gap_topic(u, key):
    return GAP_TOPIC.get((u, key))


def gap_close(u, key):
    return GAP_CLOSE.get((u, key))


def pivots(u, sid):
    return PIVOTS.get((u, sid), [])


def c38(u, facts):
    return C.c38_checks(u, facts)
