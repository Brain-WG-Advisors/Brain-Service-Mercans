# -*- coding: utf-8 -*-
"""US Data Dictionary - option mappers and the RSPEC x DD mapping rules."""
import re

from openpyxl import load_workbook

import dd_common as D

# =========================================================================== option mappers ===
# Each mapper: name, rows [(code, abbreviation, local name, english description)], keys (facts tagged on the
# first row), kind ('list' | 'external'), rid (register id when no tag is available).


def fo_rows(spec_prefix, field, skip_codes=()):
    """Rows of a Field Options list of an approved Report Spec: (code, description EN, authority wording, reference)."""
    import glob
    import os
    p = glob.glob(os.path.join(D.SPECS, f"{spec_prefix}-*.xlsx"))[0]
    ws = load_workbook(p)["Field Options"]
    out = []
    for r in range(2, ws.max_row + 1):
        if str(ws.cell(r, 1).value) == field:
            code = str(ws.cell(r, 2).value)
            if code in skip_codes:
                continue
            out.append((code, str(ws.cell(r, 3).value), str(ws.cell(r, 4).value), str(ws.cell(r, 5).value or "")))
    return out


MAPPERS = []


def mp(name, rows, keys=(), kind="list", note=""):
    MAPPERS.append(dict(name=name, rows=rows, keys=list(keys), kind=kind, note=note))


mp("Boolean", [("Y", "Yes", "Yes", "The condition applies."), ("N", "No", "No", "The condition does not apply.")])

mp("US State or District (USPS code)",
   [(c, n, n, f"{n}") for c, n in sorted(D.STATE_NAMES.items())])

mp("State employer account programme", [
    ("WH", "Withholding", "Withholding", "Income tax withholding account."),
    ("UI", "Unemployment insurance", "Unemployment insurance", "Unemployment insurance account."),
    ("PL", "Paid leave", "Paid leave", "Paid family and medical leave account.")])

mp("Supplemental wage withholding method", [
    ("1", "Flat rate", "Optional flat rate", "Optional flat rate method on supplemental wages identified separately; the rate is in the sources."),
    ("2", "Aggregate", "Aggregate method", "Aggregate method: the supplemental wages are added to the regular wages of the payroll period.")],
   keys=["fed.fit.supplemental.flat_rate"])

mp("Federal W-4 filing status", [
    ("S", "Single or Married filing separately", "Single or Married filing separately", "Step 1(c) option"),
    ("J", "Married filing jointly or Qualifying surviving spouse", "Married filing jointly or Qualifying surviving spouse", "Step 1(c) option"),
    ("H", "Head of household", "Head of household", "Step 1(c) option")], keys=["fed.w4.input_fields"])

mp("Employee special population category", [
    ("ORD", "Ordinary employee", "Ordinary employee", "Common-law employee outside the categories below."),
    ("NRA", "Nonresident alien", "Nonresident alien", "Nonresident alien employee."),
    ("STAT", "Statutory employee", "Statutory employee", "Statutory employee."),
    ("HH", "Household employee", "Household employee", "Household employee (Schedule H)."),
    ("AG", "Agricultural employee", "Agricultural employee", "Agricultural employee (Form 943)."),
    ("CLG", "Clergy", "Clergy", "Member of the clergy."),
    ("ABR", "Employee abroad", "Employee abroad", "Employee working outside the United States.")],
   note="Owner scope decision [US-OWN-005]; the categories are the scope categories, not a statutory list.")

mp("Nonresident alien visa class", [
    ("F-1", "F-1", "F-1 visa", "Visa class F-1."),
    ("J-1", "J-1", "J-1 visa", "Visa class J-1."),
    ("M-1", "M-1", "M-1 visa", "Visa class M-1."),
    ("Q-1", "Q-1", "Q-1 visa", "Visa class Q-1."),
    ("OTHER", "Other", "Other visa class", "Any other visa class.")],
   keys=["dd.fed.nra.visa_class"],
   note="Visa classes other than those listed are not named in the cited sources and use the Other code.")

mp("ACA monthly employee status", [
    ("FT", "Full-time employee", "Full-time employee", "Full-time employee for the month."),
    ("FTE", "Full-time equivalent employee", "Full-time equivalent employee", "Counted as a full-time equivalent for the month.")],
   keys=["dd.fed.aca.fte_tracking"])

mp("Interstate transport worker type", [
    ("MOTOR", "Motor carrier", "Motor carrier", "Interstate motor carrier worker."),
    ("RAIL", "Rail", "Rail", "Interstate rail worker."),
    ("AIR", "Air carrier", "Air carrier", "Air carrier worker."),
    ("SEAMAN", "Seaman", "Seaman", "Seaman.")], keys=["dd.multi.transport_worker_type"])

mp("Ohio municipal tax collector", [
    ("CCA", "Central collection agency", "Central collection agency", "Collector of the municipal tax."),
    ("RITA", "Regional income tax agency", "Regional income tax agency", "Collector of the municipal tax."),
    ("MUNI", "Municipal tax administrator", "Municipal tax administrator", "Collector of the municipal tax.")],
   keys=["dd.oh.municipality_work"])

mp("New York City or Yonkers residence status", [
    ("NYC", "New York City resident", "New York City resident", "Resident of New York City for the period."),
    ("YONK", "Yonkers resident", "Yonkers resident", "Resident of Yonkers for the period.")],
   keys=["dd.ny.nyc_yonkers_residence"])

mp("Kentucky locality of work", [
    ("LOU", "Louisville Metro", "Louisville Metro", "Locality of work."),
    ("LEX", "Lexington-Fayette", "Lexington-Fayette", "Locality of work.")], keys=["dd.ky.locality", "dd.ky.locality.lexington_name"])

mp("Oregon transit district", [
    ("TRIMET", "TriMet", "TriMet", "Transit district of work."),
    ("LANE", "Lane", "Lane", "Transit district of work.")], keys=["dd.or.transit_district"])

mp("Federal employment tax return type", [
    ("941", "Form 941 (quarterly)", "Form 941", "Quarterly federal employment tax return."),
    ("944", "Form 944 (annual)", "Form 944", "Annual return filed only on IRS notice.")],
   keys=["rspec.fed.form944.rule"])


def _fo_mapper(name, spec, field, keys=(), skip=()):
    rows = [(c, d, a, ref) for (c, d, a, ref) in fo_rows(spec, field, skip)]
    mp(name, rows, keys=keys)


_fo_mapper("Federal depositor status", "US-IRS-001", "Depositor status")
MAPPERS[-1]["keys"] = ["dd.fed.depositor_status.codes"]
_fo_mapper("W-2 agent indicator code", "US-SSA-001", "Agent Indicator Code", ["rspec.fed.efw2.re.agent_indicator.codes"])
_fo_mapper("W-2 kind of employer", "US-SSA-001", "Kind of Employer", ["rspec.fed.efw2.re.kind_of_employer.codes"])
for _m in MAPPERS[-2:]:      # the EFW2 blank value is stored as 'blank', not as the pseudo-code '(other)' (QA r1 finding 11)
    _m["rows"] = [("blank" if r[0] == "(other)" else r[0],) + tuple(r[1:]) for r in _m["rows"]]
_fo_mapper("W-2 employment code", "US-SSA-001", "Employment Code", ["rspec.fed.efw2.re.employment_code.codes"])
_fo_mapper("W-2 tax jurisdiction code", "US-SSA-001", "Tax Jurisdiction Code", ["rspec.fed.efw2.re.tax_jurisdiction.codes"])
_fo_mapper("W-2 third-party sick pay indicator", "US-SSA-001", "Third-Party Sick Pay Indicator",
           ["rspec.fed.efw2.re.third_party_sick_pay.codes"])
_fo_mapper("ACA offer of coverage code (line 14)", "US-IRS-007", "Line 14", ["rspec.fed.aca.form1095c.line14_codes"],
           skip=("1I, 1V, 1W, 1X, 1Y, 1Z",))
_fo_mapper("ACA safe harbor and relief code (line 16)", "US-IRS-007", "Line 16", ["rspec.fed.aca.form1095c.line16_codes"],
           skip=("2I",))
_fo_mapper("Treasury Tipped Occupation Code", "US-SSA-001", "Tipped occupation code", ["rspec.fed.w2.box14b.ttoc_codes"])
_fo_mapper("State filing frequency", "US-DOR-001", "Frequency")

# Connecticut CT-W4 codes A-F (named in the State certificate fact)
mp("Connecticut withholding code (CT-W4)",
   [(c, f"Code {c}", f"CT-W4 code {c}", "Withholding code of form CT-W4.") for c in "ABCDEF"], keys=["dd.state.w4.ct"])

# State withholding certificate: one entry per State (the per-State facts)
_W4 = sorted(k for k in D.DD_KEYS if k.startswith("dd.state.w4."))
mp("State withholding certificate",
   [(k.rsplit(".", 1)[1].upper(), D.STATE_NAMES[k.rsplit(".", 1)[1].upper()], k, "") for k in _W4], kind="w4")

# External code lists: pointers to the authority list (the list itself is not reproduced)
mp("SOC occupation code (federal list)", [("(authority list)", "SOC code", "Standard Occupational Classification",
   "Six-digit Standard Occupational Classification code. Not configured in this release [[GAP:DD-RQ-02]]: the code list is not carried.")], keys=["dd.wa.ui.soc_code", "dd.in.ui.soc_start_date"], kind="external")
mp("NAICS industry code", [("(authority list)", "NAICS code", "North American Industry Classification System",
   "Industry code written in the Maryland RV record. Not configured in this release [[GAP:DD-RQ-02]]: the code list is not carried.")],
   keys=["dd.md.naics"], kind="external")
mp("Alaska occupational code (authority list)", [("(authority list)", "Alaska occupational code", "Alaska occupational code",
   "Occupational code of the Alaska quarterly report. Not configured in this release [[GAP:DD-RQ-02]]: the code list is not carried.")],
   keys=["dd.ak.ui.occupation_code"], kind="external")
mp("Alaska geographic code (authority list)", [("(authority list)", "Alaska geographic code", "Alaska geographic code",
   "Geographic code of the Alaska quarterly report. Not configured in this release [[GAP:DD-RQ-02]]: the code list is not carried.")],
   keys=["dd.ak.ui.geographic_code"], kind="external")
mp("Ohio school district code", [("(authority list)", "Ohio school district code", "School district code",
   "Code of the employee's residence school district. Not configured in this release [[GAP:DD-RQ-02]]: the code list is not carried.")],
   keys=["dd.oh.school_district_code"], kind="external")
mp("Ohio municipal code", [("(authority list)", "Ohio municipal code", "Municipal code",
   "Code of the municipality used to look up the rate in the Ohio municipal rate table; the code list is described by the source below.")],
   keys=["dd.oh.municipal_rate_table", "dd.oh.municipal.code_list"], kind="external")
mp("Pennsylvania PSD code", [("(authority list)", "Pennsylvania PSD code", "Political subdivision code",
   "Code looked up with the Pennsylvania address search application; the layout of the code is not named in the cited sources. Not configured in this release [[GAP:DD-RQ-02]]: the code list is not carried.")],
   keys=["dd.pa.psd_code"], kind="external")
mp("Indiana county", [("(authority list)", "Indiana county", "Indiana county",
   "County of the Indiana withholding form; the county code list is described by the source below.")],
   keys=["dd.in.county_residence_jan1", "dd.in.county_code.list"], kind="external")
mp("Maryland county", [("(authority list)", "Maryland county", "Maryland county",
   "County of the Maryland withholding form (local rate tables); the county code lists are described by the source below.")],
   keys=["dd.md.county_residence", "dd.md.county_code.list"], kind="external")
mp("UI adjustment reason code (State list)", [("(authority list)", "Adjustment reason code", "Adjustment reason code",
   "Reason code of the State wage report; the Maryland list is described by the source below. Not configured in this release [[GAP:DD-RQ-03]]: the code values of the Massachusetts list are not carried.")],
   keys=["dd.ma.ui.hours_work_location", "dd.md.ui.adjustment_reason.codes"], kind="external")


# ====================================================================== spec row -> DD element ===
ADDR = {"Location Address": "addr_location", "Delivery Address": "addr_delivery", "City": "addr_city",
        "State Abbreviation": "addr_state", "ZIP Code": "addr_zip", "ZIP Code Extension": "addr_zip_ext",
        "Foreign State/Province": "addr_foreign_state", "Foreign Postal Code": "addr_foreign_postal",
        "Country Code": "addr_country"}
EE_ADDR_ALL = [f"ee.{v}" for v in ADDR.values()]
ER_ADDR_ALL = [f"er.{v}" for v in ADDR.values()]

# (spec regex, name regex, mapping-text regex, [elements], exception reason)
R = []


def rule(spec=None, name=None, L=None, els=(), exc=None):
    R.append((spec, name, L, list(els), exc))


# explicit per-row rules first
for lab, key in ADDR.items():
    rule("US-SSA-001", rf"^RW {re.escape(lab)}$", None, [f"ee.{key}"])
    rule("US-SSA-001", rf"^RE {re.escape(lab)}$", None, [f"er.{key}"])
rule("US-SSA-001", r"^RE Employer Contact Name$", None, ["er.contact_name"])
rule("US-SSA-001", r"^RE Employer Contact Phone Number$", None, ["er.contact_phone"])
rule("US-SSA-001", r"^RE Employer Contact Phone Extension$", None, ["er.contact_phone_ext"])
rule("US-SSA-001", r"^RE Employer Contact Fax Number$", None, ["er.contact_fax"])
rule("US-SSA-001", r"^RE Employer Contact E-Mail/Internet$", None, ["er.contact_email"])
rule("US-SSA-001", r"^RE Employer Signature PIN", None, ["er.signature_pin"])
rule("US-SSA-001", r"^RE Employer/Agent EIN$", None, ["er.ein"])
rule("US-SSA-001", r"^RE Agent for EIN$", None, ["er.agent_for_ein"])
rule("US-SSA-001", r"^RE Other EIN$", None, ["er.other_ein"])
rule("US-SSA-001", r"^RE Employer Name$", None, ["er.legal_name"])
rule("US-SSA-001", r"^RE Establishment Number$", None, ["er.establishment_number"])
rule("US-SSA-001", r"^RE Agent Indicator Code$", None, ["er.w2_agent_indicator"])
rule("US-SSA-001", r"^RE Kind of Employer$", None, ["er.w2_kind_of_employer"])
rule("US-SSA-001", r"^RE Employment Code$", None, ["er.w2_employment_code"])
rule("US-SSA-001", r"^RE Tax Jurisdiction Code$", None, ["er.w2_tax_jurisdiction"])
rule("US-SSA-001", r"^RE Third-Party Sick Pay Indicator$", None, ["er.w2_third_party_sick_pay"])
rule("US-SSA-001", r"^RE Terminating Business Indicator$", None, ["er.w2_terminating_business"])
rule("US-SSA-001", r"^RA Resub Indicator$", None, ["er.w2_resub_indicator"])
rule("US-SSA-001", r"^RW SSN$", None, ["ee.ssn"])
rule("US-SSA-001", r"^RW Employee First Name$", None, ["ee.first_name"])
rule("US-SSA-001", r"^RW Middle Name or Initial$", None, ["ee.middle_name"])
rule("US-SSA-001", r"^RW Last Name$", None, ["ee.last_name"])
rule("US-SSA-001", r"^RW Suffix$", None, ["ee.name_suffix"])
rule("US-SSA-001", r"^RW Primary Treasury Tipped", None, ["ee.ttoc_primary"])
rule("US-SSA-001", r"^RW Secondary Treasury Tipped", None, ["ee.ttoc_secondary"])

# Form 941 / 944 / 940 / 941-X / 1094-C return configuration rows
rule("US-IRS-00[12]", r"line (4|3): no SS/Medicare wages checkbox", None, ["er.no_ss_medicare_wages"])
rule("US-IRS-00[12]", r"line (17|14): business closed", None, ["er.business_closed", "er.final_wage_date"])
rule("US-IRS-001", r"line 18: seasonal employer", None, ["er.seasonal_employer"])
rule("US-IRS-004", r"line 1a: single state abbreviation", None, ["er.form940_single_state"])
rule("US-IRS-007", r"line 3: street", None, ["er.addr_delivery"])
rule("US-IRS-007", r"line 4: city", None, ["er.addr_city"])
rule("US-IRS-007", r"line 5: state", None, ["er.addr_state"])
rule("US-IRS-007", r"line 6: country and ZIP", None, ["er.addr_country", "er.addr_zip"])
rule("US-IRS-007", r"line 7: contact name", None, ["er.contact_name"])
rule("US-IRS-007", r"line 8: contact phone", None, ["er.contact_phone"])
rule("US-IRS-007", r"line 9-16", None, ["er.aca_dge"])
rule("US-IRS-007", r"line 19: authoritative", None, ["er.aca_authoritative_transmittal"])
rule("US-IRS-007", r"line 21: member of Aggregated", None, ["er.aca_aggregated_group"])
rule("US-IRS-007", r"line 22: certifications", None, ["er.aca_certifications"])
rule("US-IRS-007", r"line 36-65", None, ["er.aca_other_members"])
rule("US-IRS-008", r"line 3: W-2/W-2c certification", None, ["er.correction_w2_certification"])
rule("US-IRS-008", r"line 41:", None, ["er.correction_one_line"])
rule("US-IRS-008", r"line 42:", None, ["er.correction_reclassified"])
rule("US-IRS-008", r"line 43:", None, ["er.correction_explanation"])
rule("US-IRS-007", r"Monthly full-time and FTE status", None, ["ee.aca_monthly_status"])
rule("US-IRS-007", r"Line 14: offer of coverage code", None, ["ee.aca_offer_code"])
rule("US-IRS-007", r"Line 16: section 4980H", None, ["ee.aca_safe_harbor_code", "ee.aca_monthly_status"])
rule("US-IRS-007", r"Line 17: ZIP code", None, ["ee.worksite_zip", "ee.addr_zip"])

# federal identification and category rows
rule(None, None, r"employer FEIN$|employer FEIN \(forward", ["er.ein"])
rule(None, None, r"employer legal name and address", ["er.legal_name"] + ER_ADDR_ALL)
rule(None, None, r"employer legal name$", ["er.legal_name"])
rule(None, None, r"employee legal name$", ["ee.first_name", "ee.last_name"])
rule(None, None, r"employee SSN$", ["ee.ssn"])
rule(None, None, r"employee home address$", EE_ADDR_ALL)
rule(None, None, r"employee master data \(forward|employee master data$", ["ee.middle_name", "ee.name_suffix"])
rule(None, None, r"hire date$", ["ee.hire_date"])
rule(None, None, r"termination date$", ["ee.termination_date"])
rule(None, None, r"employer federal depositor status", ["er.federal_depositor_status"])
rule(None, None, r"employer federal return type", ["er.federal_return_type"])
rule(None, None, r"employee category flags \(household", ["ee.special_population"])
rule(None, None, r"employee category = household", ["ee.special_population"])
rule(None, None, r"household withholding agreement", ["ee.household_withholding_agreement"])
rule(None, None, r"agricultural employee flag", ["ee.special_population"])
rule(None, None, r"nonresident alien flag and visa class; employee category", ["ee.nra_flag", "ee.nra_visa_class", "ee.special_population"])
rule(None, None, r"nonresident alien flag and visa class", ["ee.nra_flag", "ee.nra_visa_class", "ee.nra_purpose_of_admission"])
rule(None, None, r"nonresident alien flag, Form 8233", ["ee.nra_flag", "ee.treaty_exemption_8233"])
rule(None, None, r"visa class \(forward", ["ee.nra_visa_class"])
rule(None, None, r"recipient country and treaty claim", ["ee.nra_country_of_residence", "ee.treaty_exemption_8233"])
rule(None, None, r"totalization country", ["ee.totalization_country", "ee.totalization_exempt"])
rule(None, None, r"Treasury Tipped Occupation Code per employee", ["ee.ttoc_primary", "ee.ttoc_secondary"])
rule(None, None, r"monthly offer of coverage", ["ee.aca_offer_code"])
rule(None, None, r"monthly status and safe harbor", ["ee.aca_safe_harbor_code", "ee.aca_monthly_status"])
rule(None, None, r"monthly full-time / FTE status", ["ee.aca_monthly_status"])
rule(None, None, r"employee residence or work-site ZIP", ["ee.addr_zip", "ee.worksite_zip"])
rule(None, None, r"employer W-2 batch configuration", ["er.w2_agent_indicator"])   # refined by the name rules above
rule(None, None, r"employer Signature PIN", ["er.signature_pin"])
rule(None, None, r"MCTMT zone", ["er.ny_mctmt_zone"])
rule(None, None, r"locality codes", ["ee.oh_municipality_work", "ee.pa_psd_work", "ee.in_county_residence", "ee.ky_work_locality",
                                      "ee.or_metro_multnomah_location", "ee.mi_city_residence", "ee.nyc_yonkers_residence"])
rule(None, None, r"Ohio school district of residence", ["ee.oh_school_district"])
rule(None, None, r"work State and residence State", ["ee.work_state", "ee.residence_state"])
rule(None, None, r"UI State per employee|work State / UI State", ["ee.sui_state", "ee.work_state"])
rule(None, None, r"hours per employee per quarter", [], "payroll result: hours accumulated from time data (WTC unit of measure), not a DD field (F26)")
rule(None, None, r"SOC code / job title", ["ee.soc_code", "ee.job_title"])
rule(None, None, r"designated new-hire State", ["er.newhire_designated_state"])
rule(None, None, r"date of birth and State-specific new-hire", ["ee.dob", "ee.gender", "ee.rate_of_pay_basis", "ee.pay_frequency",
                                                                  "ee.job_title", "ee.occupation", "ee.state_of_hire",
                                                                  "ee.health_coverage_available", "ee.dependent_coverage_date"])
rule(None, None, r"employee name, home address, SSN, date services first performed",
     ["ee.first_name", "ee.last_name", "ee.ssn", "ee.hire_date", "er.legal_name", "er.ein"] + EE_ADDR_ALL[:0])
# derived values: the spec cites the DD, the tree keeps them out (F26)
rule("US-UI-001", r"^Monthly employment counts", None, [],
     "derived: count of employees on the payroll in the pay period including the 12th of each month; computed by the "
     "report from hire date, termination date and the payroll calendar (INCLUDE/EXCLUDE tree: count of other fields)")
rule("US-UI-001", r"^Weeks counted per employee", None, [],
     "derived: weeks paid, base weeks and credit weeks are computed per quarter from wages and pay dates by the report "
     "(INCLUDE/EXCLUDE tree: count/sum of other fields; transactional per-payrun value)")
rule("US-UI-001", r"^Other State-specific employee data", None,
     ["ee.ak_geographic_code", "ee.gender", "ee.termination_date", "ee.work_location",
      "ee.ui_adjustment_reason", "er.everify_certified", "ee.wa_exempt_officer"])

# state-specific element sets of the 'Data elements reported' rows
rule("US-UI-001", r"^CT Data elements", None, ["ee.occupation", "ee.worksite_zip"])
rule("US-UI-001", r"^MA Data elements", None, ["ee.ssn", "ee.first_name", "ee.last_name", "ee.work_location",
                                                "ee.ui_adjustment_reason", "er.state_account_ids"])
rule("US-UI-001", r"^MN Data elements", None, ["ee.ssn", "ee.first_name", "ee.last_name"])
rule("US-UI-001", r"^OH Data elements", None, ["ee.ssn", "ee.first_name", "ee.last_name"])
rule("US-UI-001", r"^TX Data elements", None, ["ee.industry", "ee.occupation", "ee.full_part_time",
                                                "ee.county_primary_employment", "ee.remote_work_status"])
rule("US-UI-001", r"^VT Data elements", None, ["ee.ssn", "ee.first_name", "ee.last_name", "ee.gender"])
rule("US-UI-001", r"^WA Data elements", None, ["ee.ssn", "ee.first_name", "ee.last_name", "ee.soc_code"])
rule("US-UI-001", r"^WV Data elements", None, ["ee.ssn", "ee.first_name", "ee.last_name", "ee.soc_code", "ee.job_title",
                                                "ee.county_primary_employment"])
rule("US-PFML-001", r"^CT Data elements reported", None, ["er.ein", "er.state_account_ids"])
rule("US-PFML-001", r"^WA Data elements reported", None, ["ee.ssn", "ee.first_name", "ee.last_name", "ee.middle_name", "ee.dob",
                                                           "ee.wa_cares_exemption"])
rule("US-SDNH-001", r"^MI Data elements reported", None,
     ["ee.ssn", "ee.first_name", "ee.last_name", "ee.dob", "ee.hire_date", "er.ein", "er.legal_name", "er.contact_email",
      "er.contact_phone", "er.contact_fax"] + EE_ADDR_ALL[:0])
rule("US-DOR-002", r"^UT Data elements reported", None, ["er.ein", "er.state_account_ids", "ee.ssn"])
rule("US-DOR-002", r"Identifier and labelling rule", None, ["er.ein", "er.state_account_ids", "ee.ssn"])
rule(None, r"Identifier and labelling rule", None, ["er.ein", "er.state_account_ids", "ee.ssn"])

# employer State account / frequency / threshold rows
rule(None, None, r"per-State employer account identifiers", ["er.state_account_ids"])
rule(None, None, r"employer State account and filing frequency|employer State filing frequency", ["er.state_account_ids", "er.state_filing_frequency"])
rule(None, None, r"employer jurisdiction configuration \(threshold flag\)", ["er.state_efile_threshold"])
rule(None, None, r"employer and employee identifiers", ["er.ein", "er.state_account_ids", "ee.ssn"])
# remaining 'employer master data or return configuration' / 'employer master data' rows are caught above by name rules
rule(None, None, r"employer master data", ["er.legal_name"])
rule(None, None, r"employee master data and payroll period results", ["ee.ssn"])

# ------------------------------------------------------------------ non-DD dispositions ---
DISP = [
    (r"^Payroll result", "payroll result (WTC accumulator or pay-run total): not a DD field (INCLUDE/EXCLUDE tree)"),
    (r"^Calculated", "calculated by the generator from other rows: not a DD field (tree: calculated / count or sum)"),
    (r"^Field-model row", "alias of another field-model row of the same specification: not a separate DD field"),
    (r"^Jurisdiction configuration|^Jurisdiction rate table|^System constant|^Return generator|^File generator|^Statement generator|^Filing calendar|^Provider hand-off",
     "generator / provider configuration or constant owned by the return and file generators: not employee or employer master data"),
    (r"^Correction register", "correction record of the payroll results: not a DD field"),
    (r"^Payroll calendar", "payroll calendar of the payroll system: not a country DD field"),
    (r"^Not mapped", "the specification states no source mapping for the row"),
    (r"^Payroll results of the items", "payroll results: not a DD field"),
    (r"^Derived:", "derived count computed by the report from other fields: not a DD field (INCLUDE/EXCLUDE tree, F26)"),
]


NAMES = {}          # element name -> id, set by dd_recon.compute

HOURS_NOTE = "payroll result: hours accumulated from time data (WTC unit of measure)"
# Column L of the Report Spec rows whose mapping is not the plain list of DD names (QA r1 findings 1, 4, 5)
HOURS_ONLY = {("US-UI-001", "UI-C-009"), ("US-PFML-001", "PFML-C-003")}
HOURS_MIXED = {("US-IRS-007", "ACA-004"), ("US-PFML-001", "PFML-WA-002"), ("US-UI-001", "UI-C-012"),
               ("US-UI-001", "UI-CT-004"), ("US-UI-001", "UI-MA-003"), ("US-UI-001", "UI-MN-001"), ("US-UI-001", "UI-WA-001")}
L_OVERRIDE = {
    ("US-UI-001", "UI-C-008"): (f"Derived: count of employees on the payroll in the pay period including the 12th, computed by the "
                                f"report from {D.DD_REF} Date services first performed (hire date) | Date of separation (termination "
                                f"date) and the payroll calendar"),
    ("US-UI-001", "UI-C-011"): ("Derived: weeks paid / base weeks / credit weeks computed per quarter by the report from wages (WTC) "
                                "and pay dates"),
}
for _k in HOURS_ONLY:
    L_OVERRIDE[_k] = "Payroll result: hours accumulated from time data (WTC unit of measure)"


def exact_names(mapping):
    """Elements named exactly in a 'US-DD-001 vX: A | B; ...' mapping, or None."""
    m = re.match(re.escape(D.DD_ID) + r" v[\d.]+: ([^;]*)", mapping)
    if not m or not NAMES:
        return None
    parts = [x.strip() for x in m.group(1).split(" | ")]
    if parts and all(x in NAMES for x in parts):
        return [NAMES[x] for x in parts]
    return None


def match_rule(r):
    """(elements, exception reason or None) for a DD-citing spec row, or None when no rule matches."""
    ex = exact_names(r["mapping"])
    if ex:
        return ex, None
    for sp, nm, L, els, exc in R:
        if sp and not re.match(sp, r["spec"]):
            continue
        if nm and not re.search(nm, r["name"]):
            continue
        if L and not re.search(L, r["mapping"]):
            continue
        if not (sp or nm or L):
            continue
        return els, exc
    return None


def disposition(r):
    m = r["mapping"]
    for rx, why in DISP:
        if re.search(rx, m):
            return why
    return "mapping does not cite the Data Dictionary"
