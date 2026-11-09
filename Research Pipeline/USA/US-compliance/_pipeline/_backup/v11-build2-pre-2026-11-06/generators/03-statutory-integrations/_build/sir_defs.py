# -*- coding: utf-8 -*-
"""Content definitions of the US SIR index: which fact keys feed which register row, in which order.
Nothing here is a value; every value is read from the facts through sir_common."""
import sir_common as S

J = S.C.STATES
FED_AUTH = "sir.fed.agent_authorization.form"


def j_(code):
    return code.lower()


# ---- per-jurisdiction chains: (label, [candidate keys in order]); the first usable key of each label is written ----
def chains(spec, jur):
    j = j_(jur)
    if spec == "US-DOR-001":
        ks = [f"sir.{j}.withholding.returns", f"sir.{j}.withholding.return", f"sir.{j}.nys45", f"sir.{j}.oq",
              f"rspec.{j}.wh_return.form", f"rspec.{j}.nys45.form", f"rspec.{j}.oq.form", f"rspec.{j}.wh_deposit.form",
              f"rspec.{j}.wh_qtr_report.form", f"rspec.{j}.wh_return.applicable"]
        if jur == "CA":
            ks.insert(0, "sir.ca.ui_pit.returns")
        return [("Return and deposits", ks)]
    if spec == "US-DOR-002":
        main = [f"sir.{j}.w2.format", f"sir.{j}.w2.filing", f"sir.{j}.w2.spec_ty2026", f"rspec.{j}.annual_recon.form",
                f"rspec.{j}.w2_state.format", f"rspec.{j}.w2_state.channel", f"rspec.{j}.w2_state.form",
                f"sir.{j}.withholding.returns", f"sir.{j}.nys45", f"sir.{j}.oq"]
        if jur == "CA":
            main.insert(0, "sir.ca.ui_pit.returns")
        extra = [f"sir.{j}.w2.efile_threshold", f"sir.{j}.w2.due", f"rspec.{j}.w2_state.efile_threshold",
                 f"rspec.{j}.w2_state.due", f"rspec.{j}.annual_recon.due", f"{j}.report.w2.efile_threshold",
                 f"{j}.report.efile_threshold.employees", f"rspec.{j}.efile.mandate"]
        out = [("State W-2 copy and annual reconciliation", main), ("Threshold or due date", extra)]
        if jur == "CA":
            out.append(("Electronic file", ["sir.ca.de9c.efile_spec"]))
        if jur == "IN":
            out.append(("Schema", ["sir.in.w2.format"]))
        return out
    if spec == "US-UI-001":
        main = [f"sir.{j}.ui.wage_report", f"sir.{j}.nys45", f"sir.{j}.oq", f"rspec.{j}.ui_qtr.form",
                f"rspec.{j}.ui_qtr.due", f"rspec.{j}.ui_qtr.channel"]
        if jur == "LA":      # the channel is the LWC online services (US-LAS5-007); LAWATS is named only for the power of attorney
            main = ["rspec.la.ui_qtr.due"]
        if jur == "TX":
            main = ["sir.tx.ui.wage_report"] + main
        extra = [f"sir.{j}.ui.flat_file", f"sir.{j}.ui.xml", f"sir.{j}.ui.csv_layout", f"rspec.{j}.ui_qtr.file_formats",
                 f"rspec.{j}.ui_qtr.upload_formats", f"rspec.{j}.ui_qtr.formats", f"rspec.{j}.ui_qtr.layout",
                 f"rspec.{j}.ui_qtr.format", f"sir.{j}.ui.online_mandate", f"rspec.{j}.ui_qtr.online_mandate",
                 f"rspec.{j}.ui_qtr.efile_threshold"]
        out = [("Quarterly wage report", main), ("Format or mandate", extra)]
        if jur == "GA":      # v1.1 (US-GAV6B-001): DOL-4N electronic for all employers from 2026-08-09 (dated successor fact)
            out.append(("Electronic filing required for all employers", ["ga.report.sui.efile_all_employers"]))
        return out
    if spec == "US-SDNH-001":
        main = [f"sir.{j}.new_hire.days", f"{j}.newhire.report_days", f"{j}.newhire.report_business_days",
                f"sir.{j}.new_hire.recipient", f"rspec.{j}.new_hire.deadline"]
        return [("New-hire report", main), ("Recipient", [f"sir.{j}.new_hire.recipient", f"rspec.{j}.new_hire.recipient"])]
    if spec == "US-PFML-001":
        main = [f"sir.{j}.pfml.return", f"sir.{j}.paid_leave.return", f"rspec.{j}.pfml_qtr.form",
                f"rspec.{j}.pfml_ltc_qtr.form", f"rspec.{j}.tdi.state_return", f"sir.{j}.ui_pit.returns"]
        if jur == "CA":
            main = ["sir.ca.ui_pit.returns"] + main
        extra = [f"sir.{j}.paid_leave.bulk_format", f"rspec.{j}.pfml_qtr.channel", f"{j}.report.pfml_ltc.channels",
                 f"{j}.report.pfml.file_spec", f"rspec.{j}.pfml_qtr.return_elements"]
        return [("Programme report", main), ("Channel or file format", extra)]
    if spec in ("US-LOC-001", "US-LOC-002"):
        keys = [k for k in S.C.FACTS if k.startswith(f"sir.{j}.local.")]
        keys += [k for k in S.C.FACTS if k.startswith(f"rspec.{j}.local.") and "seattle" not in k
                 and not any(x in k for x in (".base_thresholds", ".comp_level", ".thresh", ".floor", ".due", ".rate"))]
        return [("Local return", sorted(keys, key=lambda k: (k.startswith("rspec."), k)))]
    if spec == "US-LOC-003":
        return [("City return", ["sir.wa.local.seattle_pet", "rspec.wa.local.seattle", "rspec.wa.local.seattle.sht.due"])]
    if spec == "US-DOR-003":
        return [("Return", ["sir.nv.mbt.return", "rspec.nv.mbt.form"])]
    if spec == "US-DOR-004":
        if jur == "NY":
            return [("Return", ["rspec.ny.mctmt.form", "rspec.ny.mctmt.quarterly_threshold"])]
        return [("Return", ["sir.or.oq", "rspec.or.oq.form"])]
    if spec == "US-WC-001":
        return [("Report", [f"rspec.{j}.wc_report.frequency", f"rspec.{j}.wh_qtr_report.form", f"sir.{j}.oq"])]
    return []


FED_ROWS = {
    "US-IRS-001": [("Return and deposits", ["sir.fed.941.due", "rspec.fed.form941.frequency"]),
                   ("Deposit rule", ["fed.deposit.monthly_max_lookback_liability"]),
                   ("Next-business-day deposit", ["fed.deposit.next_day_threshold"]),
                   ("Look-back period", ["sir.fed.deposit.lookback_period"])],
    "US-IRS-002": [("Return", ["rspec.fed.form944.due"]), ("Rule", ["rspec.fed.form944.rule"])],
    "US-IRS-003": [("Return", ["rspec.fed.form943.due"])],
    "US-IRS-004": [("Return", ["rspec.fed.form940.due"])],
    "US-IRS-005": [("Return", ["rspec.fed.schedule_h.due"])],
    "US-IRS-006": [("Channel", ["fed.form1042s.channel"])],
    "US-IRS-007": [("Due date", ["rspec.fed.aca.ty2026_due"]), ("E-file threshold", ["fed.aca.efile_threshold"])],
    "US-IRS-008": [("Deadlines", ["rspec.fed.form941x.deadlines"]), ("Process", ["rspec.fed.form941x.process_rule"])],
    "US-SSA-001": [("Format and channel", ["sir.fed.w2.format"]), ("Due date", ["sir.fed.w2.due_ty2026"]),
                   ("Record layout", ["sir.fed.efw2.layout_ty2026"])],
}

# ---- authorisation instruments per jurisdiction ----
WH_AUTH = lambda j: [f"sir.{j}.withholding.agent_authorization", f"sir.{j}.agent_authorization", f"sir.{j}.representative",
                     f"rspec.{j}.poa.form"]
UI_AUTH = lambda j: [f"sir.{j}.ui.agent_authorization", f"sir.{j}.agent_authorization"] + (["sir.ny.bulk_spec"] if j == "ny" else [])
NO_WAGE_TAX = {"AK", "FL", "NH", "NV", "SD", "TN", "TX", "WA", "WY"}
# an open question recorded in the facts for a jurisdiction and topic (documented limitation, not a new request)
OPEN_BY_JUR = {("NY", "wh"): "sir.ny.withholding.agent_authorization", ("ME", "wh"): "sir.me.withholding.agent_authorization",
               ("MS", "wh"): "sir.ms.withholding.agent_authorization", ("KY", "wh"): "sir.ky.agent_authorization",
               ("KY", "ui"): "sir.ky.agent_authorization", ("LA", "wh"): "sir.la.withholding.agent_authorization",
               ("WY", "ui"): "sir.wy.ui.agent_authorization_form_text"}

# keys of the facts that the file records as open questions (unresolved[]): each is a documented limitation
OPEN_KEYS = [u["key"] for u in S.UNRESOLVED if u["key"] != "precheck.next.text_elements_unmatched"]
S.OPEN_KEYS.update(k for k in OPEN_KEYS if k in S.C.FACTS)

# ---- provider programmes and duties (section 3.4) ----
PROVIDER_ROWS = [
    ("Federal reporting agent", "sir.fed.reporting_agent.tech_spec"),
    ("Federal third-party payer arrangements", "sir.fed.third_party_payer.rules"),
    ("Federal agent authorisation, returns covered", "sir.fed.agent_authorization.returns"),
    ("New York bulk web upload", "sir.ny.bulk_spec"),
    ("Ohio bulk filing", "sir.oh.bulk_filing"),
    ("Wisconsin provider registration", "sir.wi.provider_registration"),
    ("Maine payroll processor licence", "sir.me.payroll_processor_licence"),
    ("Wyoming service supplier", "sir.wy.service_supplier"),
    ("Alaska online filing by a payroll agent", "sir.ak.ui.online_mandate"),
    ("North Dakota withholding return", "sir.nd.withholding.returns"),
    ("Vermont withholding return", "sir.vt.withholding.returns"),
    ("Minnesota withholding return", "sir.mn.withholding.returns"),
]

# ---- technical specifications (section 4) ----
TECH_ROWS = [
    ("EFW2 TY2026 record layout (SSA)", "sir.fed.efw2.layout_ty2026"),
    ("EFW2 state records (RS, RV) the provider builds", "sir.fed.efw2.state_records"),
    ("W-2 and W-2c format and channel", "sir.fed.w2.format"),
    ("W-2 boxes 15 to 20", "sir.multi.w2.state_boxes"),
    ("California DE 9C electronic file", "sir.ca.de9c.efile_spec"),
    ("Connecticut Paid Leave batch file", "sir.ct.paid_leave.bulk_format"),
    ("Florida RT-6 flat file", "sir.fl.ui.flat_file"),
    ("Florida RT-6 XML", "sir.fl.ui.xml"),
    ("Alaska CSV layout", "sir.ak.ui.csv_layout"),
    ("Indiana W-2 file", "sir.in.w2.format"),
    ("North Carolina TY2026 specification", "sir.nc.w2.spec_ty2026"),
    ("Iowa W-2 file", "sir.ia.w2.format"),
    ("Maryland W-2 file", "sir.md.w2.format"),
    ("Massachusetts W-2 file", "sir.ma.w2.format"),
    ("Pennsylvania UC-2 layout", "sir.pa.ui.wage_report"),
    ("Michigan UI wage report formats", "sir.mi.ui.wage_report"),
]

# ---- routing, rejection and correction rules (section 5) ----
RULE_ROWS = [
    ("California files no State W-2", "sir.ca.ui_pit.returns"),
    ("New York files no State W-2", "sir.ny.nys45"),
    ("Iowa rejects the SSA file", "sir.ia.w2.format"),
    ("Indiana new filers", "sir.in.w2.format"),
    ("Vermont W-2 routing", "sir.vt.withholding.returns"),
    ("Kansas W-2 routing", "sir.ks.w2.format"),
    ("Michigan W-2 routing", "sir.mi.w2.filing"),
    ("Nevada MBT wages and UI wages", "sir.nv.mbt.return"),
    ("Federal return correction (941-X)", "rspec.fed.form941x.deadlines"),
    ("Federal correction process", "rspec.fed.form941x.process_rule"),
    ("Full SSN on State copies, Arizona", "rspec.az.w2_state.ssn_truncation"),
    ("Multistate new-hire election", "sir.multi.new_hire.single_state_election"),
]

# ---- deadlines (section 6) ----
DEADLINE_ROWS = [
    ("Form 941 and 944", "sir.fed.941.due"),
    ("Form 940", "rspec.fed.form940.due"),
    ("W-2 and W-3, TY2026", "sir.fed.w2.due_ty2026"),
    ("W-2 due date conflict, Massachusetts", "sir.ma.w2.due"),
    ("New hire, federal", "sir.fed.new_hire.days"),
    ("Federal deposit look-back", "sir.fed.deposit.lookback_period"),
    ("Monthly depositor ceiling", "fed.deposit.monthly_max_lookback_liability"),
    ("Next-business-day deposit", "fed.deposit.next_day_threshold"),
    ("ACA forms TY2026", "rspec.fed.aca.ty2026_due"),
    ("Form 941-X", "rspec.fed.form941x.deadlines"),
    ("New Jersey UI wage report", "sir.nj.ui.wage_report"),
    ("Michigan withholding reconciliation", "sir.mi.withholding.returns"),
]

# ---- inbound ----
INBOUND_FACTS = {
    "iwo": [("Governing law of an interstate order", "multi.iwo.governing_law"),
            ("Remittance period", "multi.iwo.remittance_business_days"),
            ("Priority among garnishments", "fed.iwo.priority"),
            ("Order form approval expiry", "fed.iwo.omb_expiry")],
    "levy": [("Exempt amount, single filer, no dependents, monthly", "fed.levy.exempt.single_0dep.monthly")],
}

# ---- provider minimum data set (section 8): (element, needed for, key) ----
DATA_SET = {
    "Per employer entity": [
        ("State withholding, UI and paid-leave account identifiers per State", "Every State return", "dd.employer.state_account_ids"),
        ("Federal depositor status", "Federal deposits", "dd.fed.depositor_status.codes"),
        ("New York MCTMT payroll zone", "MCTMT return", "dd.employer.ny_mctmt_zone"),
        ("Corporate officer without voluntary UI coverage flag, Washington", "Washington UI report", "dd.wa.exempt_officer"),
        ("E-Verify certification, Florida", "Florida RT-6", "dd.fl.everify_certified"),
        ("Employer Signature PIN (EFW2 RE record, optional)", "Form W-2 file to SSA", "sir.fed.efw2.employer_signature_pin"),
    ],
    "Per employee, identity and routing": [
        ("Work State", "State and UI routing", "dd.multi.work_state"),
        ("Residence State", "Resident withholding", "dd.multi.residence_state"),
        ("State of unemployment insurance coverage", "UI wage reports", "dd.multi.sui_state"),
        ("Wages reported to other States in the year", "UI taxable wage computation", "dd.state.ui.out_of_state_wages"),
        ("Date services first performed", "New-hire reports", "dd.fed.new_hire.date_first_services"),
        ("Date of birth for State new-hire reports", "New-hire reports", "dd.state.new_hire.dob"),
        ("SSN, not an ITIN, Florida", "Florida RT-6", "dd.fl.ssn_not_itin"),
    ],
    "Per employee, State extras": [
        ("Occupational code, Alaska", "Alaska UI wage report", "dd.ak.ui.occupation_code"),
        ("Geographic code, Alaska", "Alaska UI wage report", "dd.ak.ui.geographic_code"),
        ("SOC code, Washington", "Washington UI wage report", "dd.wa.ui.soc_code"),
        ("SOC code and start date, Indiana", "Indiana UI wage report", "dd.in.ui.soc_start_date"),
        ("Job, compensation and rate-of-pay basis, Indiana new hire", "Indiana new-hire report", "dd.in.new_hire.job_comp"),
        ("SOC or job title and county, West Virginia", "West Virginia UI wage report", "dd.wv.ui.soc_county"),
        ("Occupation, hours and worksite ZIP, Connecticut", "Connecticut UI wage report", "dd.ct.ui.occupation_hours_zip"),
        ("Gender and hourly wage, Vermont", "Vermont UI wage report", "dd.vt.ui.gender_hourly"),
        ("Enhanced content, Texas", "Texas UI wage report: proposed only, not mandatory until the TWC amendment to 40 TAC ch. 815 "
         "is adopted (US-TXV6-005)", "dd.tx.ui.enhanced"),
        ("Separation dates and probationary flag, Missouri", "Missouri UI wage report", "dd.mo.ui.separation_probation"),
        ("Hours and job title, Nebraska", "Nebraska UI wage report", "dd.ne.ui.hours_job_title"),
        ("Hours, work location and adjustment reason, Massachusetts", "Massachusetts UI wage report", "dd.ma.ui.hours_work_location"),
        ("Weeks paid, Ohio", "Ohio UI wage report", "dd.oh.ui.weeks_paid"),
        ("Base weeks, New Jersey", "New Jersey WR-30", "dd.nj.ui.base_weeks"),
        ("Credit weeks, Pennsylvania", "Pennsylvania UC-2", "dd.pa.ui.credit_weeks"),
        ("Month-of-12th employment counts", "Florida and other monthly counts", "dd.state.ui.month12_count"),
        ("NAICS code, Maryland W-2 file", "Maryland MW508 record", "dd.md.naics"),
        ("Treasury Tipped Occupation Code", "W-2 box 14b", "dd.fed.w2.tipped_occupation_code"),
    ],
    "Per employee, local and school-district routing": [
        ("Ohio municipality and collector", "Ohio municipal returns", "dd.oh.municipality_work"),
        ("Ohio school district code", "Ohio W-2 upload and school-district returns", "dd.oh.school_district_code"),
        ("Pennsylvania PSD code", "Pennsylvania EIT returns", "dd.pa.psd_code"),
        ("Indiana county on January 1", "Indiana WH-1 and W-2", "dd.in.county_residence_jan1"),
        ("Maryland county of residence", "Maryland MW506", "dd.md.county_residence"),
        ("Kentucky locality", "Kentucky occupational returns", "dd.ky.locality"),
        ("Oregon Metro and Multnomah work location", "Portland returns", "dd.or.metro_multnomah"),
        ("Oregon transit district", "Form OQ", "dd.or.transit_district"),
        ("Michigan city", "Michigan city returns", "dd.mi.city_residence_work"),
        ("Denver occupational privilege tax location", "Denver return", "dd.co.denver_opt"),
        ("New York City and Yonkers residence", "NYS-45 and withholding", "dd.ny.nyc_yonkers_residence"),
    ],
    "New-hire extras": [
        ("Health insurance offered and starting wage, Maryland", "Maryland new-hire report", "dd.md.new_hire.wage_health"),
        ("Employee fields, Mississippi", "Mississippi new-hire report", "dd.ms.new_hire.extra"),
        ("Employee fields, Georgia", "Georgia new-hire report", "dd.ga.new_hire.extra"),
        ("Occupation, Louisiana", "Louisiana new-hire report", "dd.la.new_hire.occupation"),
        ("Dependent health coverage, Iowa", "Iowa new-hire report", "dd.ia.new_hire.health"),
        ("Re-hire gap", "New-hire reports", "dd.state.new_hire.rehire_gap_days"),
    ],
    "Programme reports": [
        ("Connecticut Paid Leave employee-level data", "Connecticut Paid Leave return", "dd.ct.pfml.employee_level_data"),
        ("Washington Paid Leave and WA Cares employee fields", "Washington programme report", "dd.wa.pfml_ltc.employee_fields"),
        ("Delaware Paid Leave hours and wages", "Delaware Paid Leave report", "dd.de.paid_leave.hours"),
        ("Oregon Form 132 wage and hour detail", "Form OQ", "dd.or.form132.hours"),
        ("Minnesota paid hours", "Minnesota UI and Paid Leave", "dd.mn.ui.paid_hours"),
    ],
}

# ---- DD elements without a Report Spec consumer: disposition in this index (checked in sir_recon) ----
DD_DISPOSITION = {
    "Alaska occupational code": ("consumed", "Alaska UI wage report", "dd.ak.ui.occupation_code"),
    "Employer health insurance offered": ("consumed", "Maryland new-hire report", "dd.md.new_hire.wage_health"),
    "Oregon transit district of work": ("consumed", "Form OQ", "dd.or.transit_district"),
    "NAICS industry code (Maryland wage file)": ("consumed", "Maryland MW508 record", "dd.md.naics"),
    "Iowa school district of residence": ("not_consumed", "Individual assessment (school district surtax at filing), not an employer filing carried by a provider", "dd.ia.school_district_residence"),
    "Supplemental wage withholding method election": ("not_consumed", "Input of the federal income tax calculation on supplemental wages (regulation design); no authority filing or integration carries it", "fed.fit.supplemental.aggregate_method"),
    "State-assigned unemployment insurance rate": ("inbound", "Loaded as configuration data from the annual State UI rate notice (US-INB-003, section 1.2)", None),
    "Employee primary language": ("not_consumed", "Employee notice template input; no authority filing or integration carries it", "dd.ny.employee_primary_language"),
}


# ---- discovery verdict (SIR-QA1-01): one integrable party, the filing provider; the same sentence everywhere ----
VERDICT = "HAS_INTEGRATIONS"
PROVIDER_GAP_KEY = "sir.provider.selection"
# authority group -> fact keys that record a machine channel (SFTP, web service, XML or bulk file upload); the group is
# integration=true when at least one of them is usable. The channel is operated by the filing provider, not by Mercans.
MACHINE_FACTS = {
    "STATE-REV": ["sir.ca.de9c.efile_spec", "sir.oh.bulk_filing", "sir.ny.bulk_spec"],
    "STATE-UI": ["sir.nj.ui.wage_report", "sir.ga.ui.wage_report", "sir.nv.ui.wage_report", "sir.nd.ui.wage_report"],
    "STATE-PROG": ["sir.ct.paid_leave.bulk_format"],
}


def verdict_sentence():
    """Same sentence in the landscape rationale, Document Control and section 0 (written with the provider gap id)."""
    return ("The single integrable party for Mercans is the third-party filing provider (owner decision): Mercans hands the provider "
            "the data set of section 8 and the provider transmits to each authority, including through the SFTP, web-service and "
            "bulk-file channels that some authorities publish. The provider runbook set is not issued until the provider is chosen: "
            + S.gap(PROVIDER_GAP_KEY, "no_fact"))
