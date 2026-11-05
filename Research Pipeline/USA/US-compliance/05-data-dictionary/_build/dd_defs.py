# -*- coding: utf-8 -*-
"""US Data Dictionary - element catalogue (definitions only).

Editorial text carries no figure, rate, date, code value or legal citation: every such value is
written by build_dd.py through a [[FACT:key=value]] tag of the keys named in `facts`.
Test applied to every candidate (shared INCLUDE/EXCLUDE tree):
  calculated monetary amount / authority-generated value / count or sum of other fields /
  file or system constant / wage amount  -> EXCLUDE (WTC, report generator, YTD mechanism)
  code that selects a calculation path, master data, user input, employee attribute -> INCLUDE
The decisions are listed in _pipeline/DD-build-log.md (scope decisions).
"""

# --------------------------------------------------------------------------- helpers ---
ELEMENTS = []


def el(eid, name, desc, dt="O", pre="", ftype="Text", fmt="", om="", facts=(), grp="", lvl="Employee ID",
       label=None, note="", sheet="CF", fmt_from=None, tcls=None, derived=(), consumers=()):
    """One DD element. `facts`: keys tagged in Additional Notes; `derived`: keys of derived values that are
    NOT stored (tagged in the note of the element that holds their inputs)."""
    if tcls is None:
        tcls = {"Date": "date", "Integer": "integer", "Decimal": "decimal", "Counter": "integer"}.get(ftype, "text")
        if om == "Boolean":
            tcls = "flag"
        elif om:
            tcls = "code"
    ELEMENTS.append(dict(id=eid, name=name, desc=desc, dt=dt, pre=pre, ftype=ftype, fmt=fmt, om=om,
                         facts=list(facts), grp=grp, lvl=lvl, label=label, note=note, sheet=sheet,
                         fmt_from=fmt_from, tcls=tcls, derived=list(derived), consumers=list(consumers)))


EE, ER = "Employee ID", "Employer ID"
B = "Boolean"

# =============================================================== ID INFORMATION: employee ===
el("ee.ssn", "Employee Social Security Number (SSN)",
   "Social Security number of the employee as shown on the Social Security card. Identifies the employee on the "
   "wage file, the State wage and new-hire reports and the annual wage statement.",
   dt="M", ftype="Text", fmt_from=("US-SSA-001", 81), sheet="ID", grp="Identification",
   facts=["dd.fl.ssn_not_itin", "rspec.fed.w2.ssn_truncation"], label="SSN",
   note="Stored in full; the truncation rule above is a statement rule, not a storage rule.")

# =========================================================== ID INFORMATION: legal entity ===
el("er.ein", "Employer Identification Number (EIN)",
   "Federal Employer Identification Number of the legal entity. Identifies the employer on every federal return, "
   "the wage file, the State returns and the new-hire reports.",
   dt="M", ftype="Text", fmt_from=("US-IRS-001", 3), sheet="ID", lvl=ER, grp="Identification",
   facts=["fed.ein.format"], label="Employer identification number",
   note="Held with the hyphen as on the returns; the wage file writes the EIN without the hyphen (US-SSA-001 RE rows), "
        "a file-layout rule of the generator.")
el("er.other_ein", "Other EIN",
   "Another EIN used by the legal entity for the same wage reporting year, written on the employer record of the "
   "wage file where one exists.",
   dt="CM", pre="The legal entity used an EIN other than its current EIN for the reporting year.",
   ftype="Text", fmt_from=("US-SSA-001", 56), sheet="ID", lvl=ER, grp="Identification", label="Other EIN")
el("er.agent_for_ein", "Agent for EIN",
   "EIN of the employer on whose behalf a reporting agent files, written on the employer record of the wage file.",
   dt="CM", pre="A reporting agent files for the legal entity (agent indicator code is set).",
   ftype="Text", fmt_from=("US-SSA-001", 53), sheet="ID", lvl=ER, grp="Identification", label="Agent for EIN")
el("er.establishment_number", "Establishment number",
   "Number that identifies one establishment of the legal entity on the employer record of the wage file.",
   dt="O", ftype="Text", sheet="ID", lvl=ER, grp="Identification", label="Establishment Number",
   note="Content rules of the field are not named in the cited sources; the field is held as free text.")
el("er.state_account_state", "State employer account State",
   "State of the agency that issued the account number to the legal entity. Repeat the three account fields once per "
   "State and programme.",
   dt="CM", pre="The legal entity is registered with a State agency for a programme.", ftype="Text",
   om="US State or District (USPS code)", sheet="ID", lvl=ER, grp="Identification", label="State of the account")
el("er.state_account_programme", "State employer account programme",
   "Programme of the State account number: withholding, unemployment insurance or paid leave.",
   dt="CM", pre="The legal entity is registered with a State agency for a programme.", ftype="Text",
   om="State employer account programme", sheet="ID", lvl=ER, grp="Identification", label="Programme of the account")
el("er.state_account_ids", "State employer account number",
   "Account number issued to the legal entity by a State agency for withholding, unemployment insurance or paid "
   "leave. Repeat the three account fields (State, programme, number) once per State and programme.",
   dt="CM", pre="The legal entity is registered with the State agency for the programme.",
   ftype="Text", fmt="Per State format", sheet="ID", lvl=ER, grp="Identification",
   facts=["dd.employer.state_account_ids", "dd.ct.pfml.employee_level_data"],
   label="State withholding, UI or paid-leave account number")
el("er.signature_pin", "Employer Signature PIN",
   "Personal identification number requested from the Social Security Administration by the employer to sign wage "
   "reports electronically; blank when the employer holds none.",
   dt="CM", pre="The employer holds a Signature PIN.", ftype="Text", fmt_from=("US-SSA-001", 77), sheet="ID",
   lvl=ER, grp="Identification", facts=["sir.fed.efw2.employer_signature_pin"], label="Employer Signature PIN")

el("er.supplemental_wage_method", "Supplemental wage withholding method election",
   "Method that the legal entity uses to withhold federal income tax on supplemental wages that are identified separately "
   "from regular wages: the optional flat rate or the aggregate method. The aggregate method is the only method when no "
   "income tax was withheld from regular wages in the current or preceding year. The mandatory rate above the annual "
   "supplemental wage threshold is not an election: it applies whatever method is held here.",
   dt="CM", pre="The legal entity pays supplemental wages that are identified separately from regular wages.",
   ftype="Text", om="Supplemental wage withholding method", sheet="ID", lvl=ER, grp="Employer federal returns",
   facts=["fed.fit.supplemental.aggregate_method", "fed.fit.supplemental.mandatory_rate", "fed.fit.supplemental.mandatory_threshold"],
   label="Supplemental wage method",
   consumers=["Regulation design (federal income tax on supplemental wages)"])
el("er.state_sui_rate", "State-assigned unemployment insurance rate",
   "Unemployment insurance rate of the State account for a rating period, a percentage, entered per State account (the State "
   "and the account number are held in the State employer account fields). The entry is effective-dated: the rate applies from "
   "the start date of the entry.",
   dt="CM", pre="The legal entity holds a State unemployment insurance account with an assigned rate.", ftype="Decimal",
   fmt="Percentage", sheet="ID", lvl=ER, grp="Identification", label="State unemployment insurance rate",
   note="Not configured in this release [[GAP:DD-RQ-11]]: how each State notifies the assigned rate is not carried.",
   consumers=["Regulation design (State unemployment insurance employer contribution)"])

# ============================================================== COUNTRY FIELDS: employee name and address ===
el("ee.first_name", "Employee legal first name",
   "Given name of the employee exactly as on the Social Security card (legal name). Used on the wage file, "
   "the State wage reports, the new-hire reports and the annual wage statement.",
   dt="M", grp="Name and address", label="First Name",
   note="Employee legal name is carried in this and the next three fields; no other country-level field holds it.")
el("ee.middle_name", "Employee middle name or initial",
   "Middle name or middle initial of the employee, written when the employee has one.",
   dt="O", grp="Name and address", label="Middle Name or Initial")
el("ee.last_name", "Employee legal last name",
   "Family name of the employee exactly as on the Social Security card (legal name).",
   dt="M", grp="Name and address", label="Last Name")
el("ee.name_suffix", "Employee name suffix",
   "Generational or professional suffix of the employee name, written when the employee has one.",
   dt="O", grp="Name and address", label="Suffix")


def _addr(prefix, lvl, who, grp, rows):
    for key, nm, desc, dt, pre, ftype, om, label in rows:
        el(f"{prefix}.{key}", f"{who} {nm}", desc, dt=dt, pre=pre, ftype=ftype, om=om, lvl=lvl, grp=grp, label=label)


_ADDR_ROWS = [
    ("addr_location", "address location line",
     "Location line of the {w} address (suite, room or apartment) as carried in the Location Address position of the wage file.",
     "O", "", "Text", "", "Location Address"),
    ("addr_delivery", "address delivery line",
     "Delivery line of the {w} address (street or post box) as carried in the Delivery Address position of the wage file.",
     "M", "", "Text", "", "Delivery Address"),
    ("addr_city", "address city",
     "City of the {w} address.", "M", "", "Text", "", "City"),
    ("addr_state", "address State",
     "State or district of a United States {w} address, held as the USPS code.",
     "CM", "The address is in the United States.", "Text", "US State or District (USPS code)", "State Abbreviation"),
    ("addr_zip", "address ZIP code",
     "ZIP code of a United States {w} address.", "CM", "The address is in the United States.", "Text", "", "ZIP Code"),
    ("addr_zip_ext", "address ZIP code extension",
     "Extension of the ZIP code of a United States {w} address, written when known.",
     "O", "", "Text", "", "ZIP Code Extension"),
    ("addr_foreign_state", "address foreign State or province",
     "State or province of a {w} address outside the United States.",
     "CM", "The address is outside the United States.", "Text", "", "Foreign State/Province"),
    ("addr_foreign_postal", "address foreign postal code",
     "Postal code of a {w} address outside the United States.",
     "CM", "The address is outside the United States.", "Text", "", "Foreign Postal Code"),
    ("addr_country", "address country",
     "Country of the {w} address, held as the ISO 3166-1 alpha-2 code of the country list in this workbook.",
     "M", "", "Text", "", "Country Code"),
]
_addr("ee", EE, "Employee home", "Name and address",
      [(k, n, d.format(w="employee home"), dt, p, ft, om, lb) for k, n, d, dt, p, ft, om, lb in _ADDR_ROWS])
_addr("er", ER, "Employer", "Name and address",
      [(k, n, d.format(w="employer"), dt, p, ft, om, lb) for k, n, d, dt, p, ft, om, lb in _ADDR_ROWS])
el("er.legal_name", "Employer legal name",
   "Legal name of the employer entity as registered with the tax authority. Used on every return, the wage file and "
   "the new-hire reports.",
   dt="M", lvl=ER, grp="Name and address", label="Employer Name")
el("er.contact_name", "Employer contact name",
   "Name of the person the authority contacts about the employer's returns and wage files.",
   dt="O", lvl=ER, grp="Contact", label="Contact Name")
el("er.contact_phone", "Employer contact phone number",
   "Telephone number of the employer contact.", dt="O", lvl=ER, grp="Contact", label="Contact Phone Number")
el("er.contact_phone_ext", "Employer contact phone extension",
   "Telephone extension of the employer contact, written when one exists.", dt="O", lvl=ER, grp="Contact",
   label="Contact Phone Extension")
el("er.contact_fax", "Employer contact fax number",
   "Fax number of the employer contact, written when one exists.", dt="O", lvl=ER, grp="Contact",
   label="Contact Fax Number")
el("er.contact_email", "Employer contact e-mail",
   "E-mail address of the employer contact, written when one exists.", dt="O", lvl=ER, grp="Contact",
   label="Contact E-Mail/Internet")

# ============================================================== COUNTRY FIELDS: employment ===
el("ee.dob", "Employee date of birth",
   "Date of birth of the employee. Held for every employee and written only on the reports whose State asks for it.",
   dt="CM", pre="A State new-hire report, the Washington paid leave report or another return in this dictionary asks for the date of birth.",
   ftype="Date", fmt="YYYY-MM-DD", grp="Employment", facts=["dd.state.new_hire.dob", "dd.ms.new_hire.extra", "dd.ga.new_hire.extra"],
   label="Date of birth")
el("ee.gender", "Employee gender",
   "Gender of the employee as held in the HR record, written on the State reports that ask for it.",
   dt="CM", pre="A State report in this dictionary asks for the gender (new-hire or wage report).",
   grp="Employment", facts=["dd.vt.ui.gender_hourly"], label="Gender",
   note="Code values are not named in the cited sources; the HR record's gender list is used. The hourly wage that the "
        "Vermont report also asks for is a wage amount and is supplied from the base pay wage type, not from this dictionary.")
el("ee.hire_date", "Date services first performed (hire date)",
   "Date the employee first performed services for pay. This is the date of hire on the federal and State new-hire "
   "reports and the first-employed date on the State annual reconciliation.",
   dt="M", ftype="Date", fmt="YYYY-MM-DD", grp="Employment", facts=["dd.fed.new_hire.date_first_services", "dd.state.new_hire.rehire_gap_days"],
   label="Date first employed",
   derived=["dd.state.ui.month12_count", "dd.oh.ui.weeks_paid", "dd.nj.ui.base_weeks", "dd.pa.ui.credit_weeks"],
   note="The rehire gap is a comparison of this date with the previous termination date, computed by the report.")
el("ee.termination_date", "Date of separation (termination date)",
   "Last day of employment of the employee. Written on the State annual reconciliation and the State wage reports "
   "that ask for separation dates.",
   dt="CM", pre="The employee has separated from the employer.", ftype="Date", fmt="YYYY-MM-DD", grp="Employment",
   facts=["dd.mo.ui.separation_probation"], label="Date of separation",
   note="Only the separation date is held; the probationary flag that the Missouri report derives from the dates is "
        "computed by the report.")
el("ee.state_of_hire", "State of hire",
   "State in which the employee is hired, used where a new-hire report asks for the State of hire.",
   dt="CM", pre="The State new-hire report asks for the State of hire.", ftype="Text", om="US State or District (USPS code)",
   grp="Employment", facts=["dd.ga.new_hire.extra"], label="State of hire")
el("ee.rate_of_pay_basis", "Rate-of-pay basis",
   "Basis on which the employee is paid (hourly or salaried), written on the new-hire reports that ask for the rate-of-pay basis.",
   dt="CM", pre="The State new-hire report asks for the rate-of-pay basis.", grp="Employment",
   facts=["dd.in.new_hire.job_comp"], label="Rate of pay basis",
   note="The starting compensation named in the research is a wage amount and is supplied from the base pay wage type "
        "(Wage Type Catalogue), not stored here.")
el("ee.pay_frequency", "Pay frequency",
   "Frequency at which the employee is paid, written on the new-hire reports that ask for it.",
   dt="CM", pre="The State new-hire report asks for the pay frequency.", grp="Employment",
   facts=["dd.ms.new_hire.extra"], label="Pay frequency",
   note="Held from the payroll calendar assigned to the employee; the salary named in the research is a wage amount "
        "and is not stored here.")
el("ee.full_part_time", "Full-time or part-time status",
   "Whether the employee works full time or part time, written on the wage reports that ask for it.",
   dt="CM", pre="The State wage report asks for the full-time or part-time status.", grp="Employment",
   facts=["dd.tx.ui.enhanced"], label="Full/part-time")
el("ee.remote_work_status", "Remote-work status",
   "Whether the employee works remotely, written on the wage reports that ask for it.",
   dt="CM", pre="The State wage report asks for the remote-work status.", grp="Employment", om=B,
   facts=["dd.tx.ui.enhanced"], label="Remote-work status",
   note="The start quarter from which the Texas filing carries this item is not named in the cited sources.")
el("ee.industry", "Industry of employment",
   "Industry of the employee's place of employment, written on the wage reports that ask for it.",
   dt="CM", pre="The State wage report asks for the industry.", grp="Employment", facts=["dd.tx.ui.enhanced"],
   label="Industry", note="The code list and layout for this item are not named in the cited sources.")
el("ee.job_title", "Job title",
   "Job title of the employee as held in the HR record, written on the reports that ask for the job title.",
   dt="CM", pre="The State report asks for the job title.", grp="Employment",
   facts=["dd.in.new_hire.job_comp", "dd.ne.ui.hours_job_title", "dd.wv.ui.soc_county"], label="Job title")
el("ee.occupation", "Occupation",
   "Occupation of the employee in words, written on the reports that ask for the occupation.",
   dt="CM", pre="The State report asks for the occupation.", grp="Employment",
   facts=["dd.la.new_hire.occupation", "dd.ct.ui.occupation_hours_zip", "dd.tx.ui.enhanced"], label="Occupation")
el("ee.soc_code", "Standard Occupational Classification (SOC) code",
   "Six-digit Standard Occupational Classification code of the employee's occupation.",
   dt="CM", pre="The State report asks for the SOC code.", ftype="Text", om="SOC occupation code (federal list)",
   grp="Employment", facts=["dd.wa.ui.soc_code", "dd.in.ui.soc_start_date", "dd.wv.ui.soc_county"], label="SOC code")
el("ee.ak_occupation_code", "Alaska occupational code",
   "Occupational code of the employee written on the Alaska quarterly contribution report.",
   dt="CM", pre="The employee works in Alaska.", om="Alaska occupational code (authority list)", grp="Employment",
   facts=["dd.ak.ui.occupation_code"], label="Occupational code")
el("ee.ak_geographic_code", "Alaska geographic code",
   "Geographic code of the employee's place of work written on the Alaska quarterly contribution report.",
   dt="CM", pre="The employee works in Alaska.", om="Alaska geographic code (authority list)", grp="Employment",
   facts=["dd.ak.ui.geographic_code"], label="Geographic code")
el("ee.worksite_zip", "Worksite ZIP code",
   "ZIP code of the employee's primary worksite. Written on the Connecticut wage report where the employer chooses to "
   "include it and used as the work-site ZIP code on Form 1095-C where the offer code asks for it.",
   dt="CM", pre="The Connecticut wage report or the Form 1095-C offer code asks for the worksite ZIP code.",
   grp="Employment", facts=["dd.ct.ui.occupation_hours_zip"], label="ZIP code",
   note="The positions of the optional Connecticut fields in the file layout are not named in the cited sources.")
el("ee.county_primary_employment", "County of primary employment",
   "County of the employee's primary place of employment, written on the reports that ask for the county.",
   dt="CM", pre="The State report asks for the county of employment.", grp="Employment",
   facts=["dd.tx.ui.enhanced", "dd.wv.ui.soc_county"], label="County")
el("ee.work_location", "Work location",
   "Work location of the employee as defined by the employer, written on the State wage report that asks for the work location.",
   dt="CM", pre="The State wage report asks for the work location.", grp="Employment",
   facts=["dd.ma.ui.hours_work_location"], label="Work location")
el("ee.ui_adjustment_reason", "Unemployment insurance adjustment reason code",
   "Code stating why a wage record is adjusted, written on the State wage reports that carry an adjustment reason.",
   dt="CM", pre="The State wage report carries an adjustment reason code.", om="UI adjustment reason code (State list)",
   grp="Employment", facts=["dd.ma.ui.hours_work_location"], label="Adjustment reason code")
el("ee.wa_exempt_officer", "Corporate officer without voluntary unemployment insurance coverage",
   "Flag that the employee is a corporate officer of the employer who has not elected voluntary unemployment insurance coverage.",
   dt="CM", pre="The employee works in Washington and is a corporate officer.", om=B, grp="Employment",
   facts=["dd.wa.exempt_officer"], label="Exempt corporate officer")
el("ee.wa_cares_exemption", "Washington Cares exemption status",
   "Whether the employee holds an approved exemption from the Washington Cares programme, written on the combined "
   "paid leave and Washington Cares report.",
   dt="CM", pre="The employee works in Washington.", om=B, grp="Employment",
   facts=["dd.wa.pfml_ltc.employee_fields"], label="WA Cares exemption status")
el("ee.wy_forfeiture_policy_ack", "Vacation forfeiture policy acknowledged in writing",
   "Flag that the employee has acknowledged in writing the employer's policy on forfeiture of accrued vacation. "
   "Selects whether accrued vacation is paid at termination.",
   dt="CM", pre="The employee works in Wyoming and the employer has a written forfeiture policy.", om=B, grp="Employment",
   facts=["dd.wy.vacation_forfeiture_policy_acknowledged"], label="Forfeiture policy acknowledged")
el("er.everify_certified", "E-Verify certification",
   "Flag that the employer certifies use of E-Verify, made on the first Florida return of the calendar year.",
   dt="CM", pre="The employer is a private employer subject to the Florida E-Verify rule.", om=B, lvl=ER, grp="Employer registration",
   facts=["dd.fl.everify_certified"], label="E-Verify certification")
el("er.health_coverage_offered", "Employer health insurance offered",
   "Whether the employer offers health insurance, written on the new-hire reports that ask for it.",
   dt="CM", pre="The State new-hire report asks whether health insurance is offered.", om=B, lvl=ER, grp="Employer registration",
   facts=["dd.md.new_hire.wage_health"], label="Health insurance offered",
   note="The starting wage named in the research is a wage amount and is not stored here.")
el("ee.health_coverage_available", "Medical or dependent health coverage available to the employee",
   "Whether medical insurance (or dependent health coverage) is available to the employee, written on the new-hire "
   "reports that ask for it.",
   dt="CM", pre="The State new-hire report asks for medical-insurance availability or eligibility.", om=B, grp="Employment",
   facts=["dd.ms.new_hire.extra", "dd.ga.new_hire.extra", "dd.ia.new_hire.health"], label="Medical insurance eligibility")
el("ee.dependent_coverage_date", "Dependent health coverage qualifying date",
   "Date from which the employee qualifies for dependent health coverage, written on the Iowa new-hire report.",
   dt="CM", pre="Dependent health coverage is available to the employee.", ftype="Date", fmt="YYYY-MM-DD", grp="Employment",
   facts=["dd.ia.new_hire.health"], label="Qualifying date")
el("er.iwo_address", "Income withholding order address",
   "Address to which income withholding orders or the notices of orders and garnishments are sent, written on the Iowa new-hire report.",
   dt="CM", pre="The Iowa new-hire report asks for the address.", lvl=ER, grp="Employer registration",
   facts=["dd.ia.new_hire.health"], label="Income withholding order address")

# ============================================================== COUNTRY FIELDS: federal tax certificate ===
_W4 = "dd.fed.w4_2026.fields"
el("ee.w4_filing_status", "Form W-4 filing status (Step 1(c))",
   "Filing status the employee selected in Step 1(c) of the federal Form W-4. Selects the Publication 15-T withholding table.",
   dt="M", om="Federal W-4 filing status", grp="Federal tax certificate", facts=[_W4, "fed.w4.input_fields"],
   label="Step 1(c) filing status")
el("ee.w4_multiple_jobs", "Form W-4 multiple jobs or spouse works (Step 2)",
   "Flag that the employee ticked the multiple-jobs box in Step 2 of the federal Form W-4. Read by the federal income tax withholding calculation.",
   dt="O", om=B, grp="Federal tax certificate", facts=[_W4], label="Step 2 multiple jobs")
el("ee.w4_dependents_credit", "Form W-4 dependents and other credits (Step 3)",
   "Amount of credits the employee claimed in Step 3 of the federal Form W-4, as entered by the employee.",
   dt="O", ftype="Decimal", grp="Federal tax certificate", facts=[_W4], label="Step 3 credits")
el("ee.w4_other_income", "Form W-4 other income (Step 4(a))",
   "Other income the employee entered in Step 4(a) of the federal Form W-4, as entered by the employee.",
   dt="O", ftype="Decimal", grp="Federal tax certificate", facts=[_W4], label="Step 4(a) other income")
el("ee.w4_deductions", "Form W-4 deductions (Step 4(b))",
   "Deductions the employee entered in Step 4(b) of the federal Form W-4, as entered by the employee.",
   dt="O", ftype="Decimal", grp="Federal tax certificate", facts=[_W4], label="Step 4(b) deductions")
el("ee.w4_extra_withholding", "Form W-4 extra withholding (Step 4(c))",
   "Additional amount to withhold each pay period that the employee entered in Step 4(c) of the federal Form W-4.",
   dt="O", ftype="Decimal", grp="Federal tax certificate", facts=[_W4], label="Step 4(c) extra withholding")
el("ee.w4_exempt", "Form W-4 exempt from withholding",
   "Flag that the employee claimed exemption from federal income tax withholding on the Form W-4.",
   dt="O", om=B, grp="Federal tax certificate", facts=[_W4, "fed.w4.exempt.validity"], label="Exempt")
el("ee.special_population", "Employee special population category",
   "Category of the employee for federal employment taxes. Selects the return, the wage-file employment code and the "
   "tax treatment: ordinary employee, nonresident alien, statutory employee, household, agricultural, clergy or employee abroad.",
   dt="M", om="Employee special population category", grp="Federal tax certificate", label="Employee category",
   note="Owner scope decision [US-OWN-005]: all populations are in scope at the federal layer. Contractors and "
        "Form 1099-NEC payees are out of scope and carry no master data here.")
el("ee.household_withholding_agreement", "Household employee: federal income tax withholding agreement",
   "Flag that the household employer and the household employee agreed that federal income tax is withheld from the wages.",
   dt="CM", pre="The employee category is household.", om=B, grp="Federal tax certificate",
   facts=["fed.household.fit.withholding"], label="Withholding by agreement")
el("ee.nra_flag", "Nonresident alien flag",
   "Flag that the employee is a nonresident alien for federal tax. Selects the nonresident alien withholding add-on, "
   "the Form 8233 treaty claim and the Form 1042-S reporting.",
   dt="M", om=B, grp="Federal tax certificate", facts=["dd.fed.nra.flag"], label="Nonresident alien")
el("ee.nra_notice1392", "Nonresident alien Form W-4 completed per Notice 1392",
   "Flag that the nonresident alien employee completed the Form W-4 according to Notice 1392.",
   dt="CM", pre="The employee is a nonresident alien.", om=B, grp="Federal tax certificate", facts=["dd.fed.nra.flag"],
   label="Notice 1392 Form W-4")
el("ee.treaty_exemption_8233", "Form 8233 treaty exemption claimed",
   "Flag that the nonresident alien employee claimed a tax treaty exemption on Form 8233. The exempt wages go to Form 1042-S.",
   dt="CM", pre="The employee is a nonresident alien.", om=B, grp="Federal tax certificate", facts=["dd.fed.nra.flag"],
   label="Form 8233 treaty claim")
el("ee.nra_visa_class", "Nonresident alien visa class",
   "Immigration visa class of the nonresident alien employee. Drives the exemption flags for employee and employer social "
   "security, Medicare and unemployment tax.",
   dt="CM", pre="The employee is a nonresident alien.", om="Nonresident alien visa class", grp="Federal tax certificate",
   facts=["dd.fed.nra.visa_class"], label="Visa class")
el("ee.nra_purpose_of_admission", "Work carries out the purpose of admission",
   "Flag that the employee's services carry out the purpose of the visa admission, including authorised practical training.",
   dt="CM", pre="The employee is a nonresident alien holding a visa class that the exemption names.", om=B,
   grp="Federal tax certificate", facts=["dd.fed.nra.visa_class"], label="Purpose of admission")
el("ee.nra_country_of_residence", "Nonresident alien country of residence",
   "Country of residence of the nonresident alien employee, held as the ISO 3166-1 alpha-2 code. Written on Form 1042-S "
   "for the recipient country and treaty claim.",
   dt="CM", pre="The employee is a nonresident alien with services reported on Form 1042-S.", grp="Federal tax certificate",
   facts=["dd.fed.nra.flag"], label="Recipient country code")
el("ee.totalization_country", "Totalization agreement country",
   "Country of the social security totalization agreement under which the employee is covered by a foreign system.",
   dt="CM", pre="The employee holds a certificate of coverage under a totalization agreement.", grp="Federal tax certificate",
   facts=["dd.fed.totalization.exemption"], label="Totalization agreement country")
el("ee.totalization_exempt", "Totalization agreement FICA exemption",
   "Flag that the employee is covered exclusively by a foreign social security system under an agreement, so that "
   "employee and employer FICA do not apply.",
   dt="CM", pre="The employee holds a certificate of coverage under a totalization agreement.", om=B, grp="Federal tax certificate",
   facts=["dd.fed.totalization.exemption", "fed.fica.totalization.exemption_rule"], label="Totalization exemption")
el("ee.ttoc_primary", "Primary Treasury Tipped Occupation Code",
   "Treasury Tipped Occupation Code of the employee's main tipped occupation, written in box 14b of the wage statement.",
   dt="CM", pre="The employee has cash tips reported in box 12.", om="Treasury Tipped Occupation Code", grp="Federal tax certificate",
   facts=["dd.fed.w2.tipped_occupation_code"], label="Primary Treasury Tipped Occupation Code")
el("ee.ttoc_secondary", "Secondary Treasury Tipped Occupation Code",
   "Treasury Tipped Occupation Code of a second tipped occupation, written in box 14b of the wage statement.",
   dt="CM", pre="The employee has cash tips reported in box 12 in more than one tipped occupation.",
   om="Treasury Tipped Occupation Code", grp="Federal tax certificate", facts=["dd.fed.w2.tipped_occupation_code"],
   label="Secondary Treasury Tipped Occupation Code")

# ============================================================== COUNTRY FIELDS: ACA ===
el("ee.aca_monthly_status", "ACA monthly employee status",
   "Status of the employee for each calendar month (full-time or full-time equivalent) as determined by the employer's "
   "measurement method. Feeds the applicable large employer test and the monthly lines of Form 1095-C. One value per month.",
   dt="CM", pre="The employer is subject to Forms 1094-C and 1095-C.", om="ACA monthly employee status", grp="ACA",
   facts=["dd.fed.aca.fte_tracking"], label="Monthly status",
   note="The determination is entered or imported as a status; the supporting hours come from time data, not from this dictionary.")
el("ee.aca_offer_code", "ACA offer of coverage code (line 14), per month",
   "Form 1095-C line 14 code that states the offer of coverage made to the employee in the month. One value per month.",
   dt="CM", pre="The employer is subject to Forms 1094-C and 1095-C.", om="ACA offer of coverage code (line 14)", grp="ACA",
   facts=["rspec.fed.aca.form1095c.line14_codes"], label="Line 14 offer of coverage")
el("ee.aca_safe_harbor_code", "ACA safe harbor and relief code (line 16), per month",
   "Form 1095-C line 16 code that states the safe harbor or relief applying to the employee in the month. One value per month.",
   dt="CM", pre="A safe harbor or relief applies to the month.", om="ACA safe harbor and relief code (line 16)", grp="ACA",
   facts=["rspec.fed.aca.form1095c.line16_codes"], label="Line 16 safe harbor")

# ============================================================== COUNTRY FIELDS: state tax certificate ===
el("ee.state_cert_form", "State withholding certificate on file",
   "Withholding certificate the employee gave the employer for the State. Selects the State withholding method. "
   "The form identifier and revision are listed in the option mapper, one entry per State.",
   dt="CM", pre="The work State levies income tax withholding.", om="State withholding certificate", grp="State tax certificate",
   label="State withholding certificate",
   note="\u26a0\ufe0f Not configured in this release [[GAP:DD-RQ-01]]: the line structure of each State certificate (allowances, additional amount, exemption "
        "claim) is not carried; the dictionary holds the form identifier only. Per-State form entries: see "
        "Country Option Mappers.")
el("ee.ct_withholding_code", "Connecticut withholding code (CT-W4)",
   "Withholding code the employee selected on the Connecticut form CT-W4.",
   dt="CM", pre="The work State is Connecticut.", om="Connecticut withholding code (CT-W4)", grp="State tax certificate",
   facts=["dd.state.w4.ct"], label="CT-W4 code")
el("ee.state_allowances", "State withholding allowances or exemptions claimed",
   "Number of allowances or exemptions the employee claimed on the State certificate, as entered by the employee.",
   dt="CM", pre="The State form on file uses allowances or exemptions.", ftype="Integer", grp="State tax certificate",
   facts=["dd.state.w4.ri", "dd.state.w4.ne", "dd.state.w4.mn", "dd.state.w4.oh"], label="Allowances or exemptions",
   note="\u26a0\ufe0f Not configured in this release [[GAP:DD-RQ-01]]: which State forms use allowances or exemptions, and their limits, is not carried beyond "
        "the form facts above.")
el("ee.in_county_residence", "Indiana county of residence on January 1",
   "Indiana county in which the employee lived on January 1 (Form WH-4).",
   dt="CM", pre="The employee works in Indiana.", om="Indiana county", grp="State tax certificate",
   facts=["dd.in.county_residence_jan1", "dd.state.w4.in"], label="County of residence")
el("ee.in_county_employment", "Indiana county of principal employment on January 1",
   "Indiana county of the employee's principal place of employment on January 1 (Form WH-4).",
   dt="CM", pre="The employee works in Indiana.", om="Indiana county", grp="State tax certificate",
   facts=["dd.in.county_residence_jan1"], label="County of principal employment")
el("ee.md_county_residence", "Maryland county of residence",
   "Maryland county of residence of the employee (Form MW507), selecting the local rate table.",
   dt="CM", pre="The employee works in Maryland.", om="Maryland county", grp="State tax certificate",
   facts=["dd.md.county_residence", "dd.state.w4.md"], label="County of residence")

# ============================================================== COUNTRY FIELDS: jurisdiction ===
el("ee.work_state", "Work State",
   "State where the employee's service is localized. Drives State withholding and the unemployment insurance State. "
   "Held as the USPS code and read at every payment.",
   dt="M", om="US State or District (USPS code)", grp="Work and residence jurisdiction", facts=["dd.multi.work_state"],
   label="State of withholding")
el("ee.sui_state", "Unemployment insurance State",
   "Single State to which the employee's unemployment insurance wages are reported for the period under the localization "
   "test; also keys the Washington family and medical leave premium.",
   dt="M", om="US State or District (USPS code)", grp="Work and residence jurisdiction", facts=["dd.multi.sui_state"],
   label="Recipient State", derived=["dd.state.ui.out_of_state_wages"],
   note="Wages reported to other States in the year are a wage amount: they enter through the year-to-date load of the "
        "Wage Type Catalogue, not through this dictionary.")
el("ee.residence_state", "Residence State",
   "State where the employee lives. Drives resident withholding, reciprocity, the resident credit and the transport-worker federal rules.",
   dt="M", om="US State or District (USPS code)", grp="Work and residence jurisdiction", facts=["dd.multi.residence_state"],
   label="State of residence", derived=["dd.la.workday_counter"],
   note="Day counts used by the nonresident rules (days worked in the taxing State, total days worked, the Louisiana "
        "workday count) are time data accumulated by the payroll calculation and the year-to-date load; they are not held "
        "in this dictionary.")
el("ee.transport_worker_type", "Interstate transport worker type",
   "Type of interstate transport worker (motor carrier, rail, air carrier or seaman), selecting the federal rule that "
   "allocates income tax to one State.",
   dt="CM", pre="The employee is an interstate transport worker.", om="Interstate transport worker type",
   grp="Work and residence jurisdiction", facts=["dd.multi.transport_worker_type"], label="Transport worker type")
el("ee.military_spouse_election", "Military spouse residence election",
   "Flag that the employee is the spouse of a servicemember and elected to keep a residence State under the Servicemembers Civil Relief Act.",
   dt="CM", pre="The employee is the spouse of a servicemember.", om=B, grp="Work and residence jurisdiction",
   facts=["dd.multi.military_spouse"], label="Military spouse election")
# ============================================================== COUNTRY FIELDS: local taxes ===
el("ee.oh_school_district", "Ohio school district of residence",
   "Ohio school district code of the employee's residence. Written on the wage statement and the school district return.",
   dt="CM", pre="The employee works in Ohio.", om="Ohio school district code", grp="Local taxes",
   facts=["dd.oh.school_district_code"], label="School district code",
   note="The full-year nonresident value in the fact above rests on the 2025 school district list [US-OHS5-019] (effective to 2025-12-31); no 2026 restatement of that value is named in the cited sources.")
el("ee.oh_municipality_work", "Ohio municipality of work",
   "Ohio municipality of the employee's place of work; the rate is resolved by the municipal code and the pay date.",
   dt="CM", pre="The employee works in Ohio.", om="Ohio municipal code", grp="Local taxes",
   facts=["dd.oh.municipality_work", "dd.oh.municipal_rate_table"], label="Municipality of work")
el("ee.oh_municipality_residence", "Ohio municipality of residence",
   "Ohio municipality of the employee's residence.",
   dt="CM", pre="The employee works in Ohio.", om="Ohio municipal code", grp="Local taxes", facts=["dd.oh.municipality_work"],
   label="Municipality of residence")
el("er.oh_tax_collector", "Ohio municipal tax collector",
   "Collector of the municipal income tax for the Ohio municipality.",
   dt="CM", pre="The employer withholds Ohio municipal income tax.", om="Ohio municipal tax collector", lvl=ER, grp="Local taxes",
   facts=["dd.oh.municipality_work"], label="Collector")
el("ee.pa_psd_work", "Pennsylvania PSD code of the work location",
   "Political subdivision code of the employee's work location, looked up with the Pennsylvania address search application.",
   dt="CM", pre="The employee works in Pennsylvania.", om="Pennsylvania PSD code", grp="Local taxes", facts=["dd.pa.psd_code"],
   label="PSD code of work")
el("ee.pa_psd_residence", "Pennsylvania PSD code of the residence",
   "Political subdivision code of the employee's residence, looked up with the Pennsylvania address search application.",
   dt="CM", pre="The employee works in Pennsylvania.", om="Pennsylvania PSD code", grp="Local taxes", facts=["dd.pa.psd_code"],
   label="PSD code of residence",
)
el("ee.nyc_yonkers_residence", "New York City or Yonkers residence status",
   "Whether the employee is a resident of New York City or Yonkers for the period; blank when neither.",
   dt="CM", pre="The employee works in New York.", om="New York City or Yonkers residence status", grp="Local taxes",
   facts=["dd.ny.nyc_yonkers_residence"], label="NYC or Yonkers resident")
el("ee.nyc_yonkers_resident_from", "New York City or Yonkers residence start date",
   "First day of the resident period of the employee in New York City or Yonkers.",
   dt="CM", pre="The employee is a New York City or Yonkers resident.", ftype="Date", fmt="YYYY-MM-DD", grp="Local taxes",
   facts=["dd.ny.nyc_yonkers_residence"], label="Resident from")
el("ee.nyc_yonkers_resident_to", "New York City or Yonkers residence end date",
   "Last day of the resident period of the employee in New York City or Yonkers.",
   dt="CM", pre="The employee stopped being a New York City or Yonkers resident.", ftype="Date", fmt="YYYY-MM-DD",
   grp="Local taxes", facts=["dd.ny.nyc_yonkers_residence"], label="Resident to")
el("ee.ky_work_locality", "Kentucky locality of work",
   "Kentucky locality in which the employee works.",
   dt="CM", pre="The employee works in Kentucky.", om="Kentucky locality of work", grp="Local taxes",
   facts=["dd.ky.locality"], label="Locality of work")
el("ee.ky_residence_locality", "Kentucky locality of residence (school board component)",
   "Kentucky locality of the employee's residence, used for the school board component.",
   dt="CM", pre="The employee works in Kentucky.", grp="Local taxes", facts=["dd.ky.locality"], label="Locality of residence")
el("ee.or_metro_multnomah_location", "Oregon Metro SHS or Multnomah PFA work location",
   "Whether the employee's work location is in the Metro SHS area or the Multnomah PFA area.",
   dt="CM", pre="The employee works in Oregon.", om=B, grp="Local taxes", facts=["dd.or.metro_multnomah"],
   label="Metro / Multnomah work location")
el("ee.or_metro_multnomah_optout", "Oregon Metro SHS or Multnomah PFA opt-in or opt-out",
   "Flag that the employee opted in to or out of the Metro SHS or Multnomah PFA tax, as the form allows.",
   dt="CM", pre="The work location is in the Metro or Multnomah area.", om=B, grp="Local taxes",
   facts=["dd.or.metro_multnomah"], label="Opt-in / opt-out")
el("ee.or_transit_district", "Oregon transit district of work",
   "Transit district in which the employee works (TriMet or Lane), written on the Oregon quarterly report.",
   dt="CM", pre="The employee works in Oregon.", om="Oregon transit district", grp="Local taxes",
   facts=["dd.or.transit_district"], label="Transit district")
el("ee.mi_city_residence", "Michigan city of residence or predominant place of employment",
   "Whether the employee is a resident or nonresident of a Michigan income-tax city (for example Detroit) and the city of "
   "predominant place of employment (Form DW-4).",
   dt="CM", pre="The employee works in a Michigan income-tax city.", grp="Local taxes", facts=["dd.mi.city_residence_work"],
   label="City of residence / employment")
el("ee.denver_opt_worksite", "Denver occupational privilege tax work location",
   "Flag that the employee's work location is in Denver, which selects the Denver OPT test.",
   dt="CM", pre="The employee works in Colorado.", om=B, grp="Local taxes", facts=["dd.co.denver_opt"],
   label="Denver OPT work location",
   note="The monthly earnings test is a comparison of the pay result with the threshold, computed by the payroll "
        "calculation; only the work location is held here.")
el("ee.ia_school_district_residence", "Iowa school district of residence",
   "Iowa school district of the employee's residence, recorded from the Iowa W-4.",
   dt="CM", pre="The employee works in Iowa.", grp="Local taxes", facts=["dd.ia.school_district_residence", "dd.state.w4.ia"],
   label="School district")

# ============================================================== COUNTRY FIELDS: notices ===
el("ee.primary_language", "Employee primary language",
   "First or primary language of the employee. Selects the language of the pay-rate and payday notice (New York) and "
   "feeds the Colorado paid sick leave notice language.",
   dt="CM", pre="The employee works in New York or Colorado.", grp="Notices", facts=["dd.ny.employee_primary_language", "dd.co.workforce_first_language_5pct"],
   label="Primary language",
   note="Notice seam only: the payslip stays in English; the share of the workforce speaking a language is computed by the notice template.")

# ============================================================== COUNTRY FIELDS: employer configuration ===
el("er.ny_mctmt_zone", "New York MCTMT zone",
   "MCTMT zone of the employer's payroll, selecting the zone rate table of the return.",
   dt="CM", pre="The employer has payroll subject to the MCTMT.", lvl=ER,
   grp="Employer registration", facts=["dd.employer.ny_mctmt_zone"], label="MCTMT zone")
el("er.naics", "NAICS industry code (Maryland wage file)",
   "North American Industry Classification System code of the employer, written in the RV record of the Maryland wage file.",
   dt="CM", pre="The employer files the Maryland MW508 wage file.", om="NAICS industry code", lvl=ER, grp="Employer registration",
   facts=["dd.md.naics"], label="NAICS")
el("er.state_filing_frequency", "State filing frequency",
   "Filing and deposit frequency the State assigned to the employer for its withholding or unemployment insurance account. "
   "One value per State.",
   dt="CM", pre="The legal entity is registered with the State agency.", om="State filing frequency", lvl=ER,
   grp="Employer registration", label="Filing frequency",
   note="The frequency is named by the State; the codes are internal configuration codes.")
el("er.state_efile_threshold", "State electronic filing or payment requirement applies",
   "Flag that the employer reaches the State threshold that requires electronic filing or payment. One value per State.",
   dt="CM", pre="The State sets an electronic filing or payment threshold.", om=B, lvl=ER, grp="Employer registration",
   label="Electronic filing required",
   note="The thresholds are stated in the Report Specification rows named under Used by; the flag is set by the employer "
        "configuration.")
el("er.federal_depositor_status", "Federal depositor status",
   "Federal tax deposit schedule of the employer (monthly or semiweekly), written on Form 941.",
   dt="M", om="Federal depositor status", lvl=ER, grp="Employer federal returns", label="Depositor status")
el("er.federal_return_type", "Federal employment tax return type",
   "Annual return that the employer files instead of the quarterly return (Form 941 or Form 944), as the IRS notice requires.",
   dt="M", om="Federal employment tax return type", lvl=ER, grp="Employer federal returns",
   facts=["rspec.fed.form944.rule"], label="Return type")
el("er.no_ss_medicare_wages", "No social security or Medicare wages indicator",
   "Flag that the employer does not expect to pay social security or Medicare wages (Form 941 line 4, Form 944 line 3).",
   dt="CM", pre="The employer pays no wages subject to social security or Medicare tax in the period.", om=B, lvl=ER,
   grp="Employer federal returns", label="No SS/Medicare wages checkbox")
el("er.business_closed", "Business closed indicator",
   "Flag that the employer closed its business or stopped paying wages (Form 941 line 17, Form 944 line 14).",
   dt="CM", pre="The business has closed or stopped paying wages.", om=B, lvl=ER, grp="Employer federal returns",
   label="Business closed")
el("er.final_wage_date", "Final wage payment date",
   "Date the employer paid final wages, written with the business closed indicator.",
   dt="CM", pre="The business has closed.", ftype="Date", fmt="YYYY-MM-DD", lvl=ER, grp="Employer federal returns",
   label="Final wage date")
el("er.seasonal_employer", "Seasonal employer indicator",
   "Flag that the employer is a seasonal employer and does not have to file a return for every quarter (Form 941 line 18).",
   dt="CM", pre="The employer is a seasonal employer.", om=B, lvl=ER, grp="Employer federal returns", label="Seasonal employer")
el("er.form940_single_state", "Form 940 single State abbreviation",
   "State in which the employer paid all unemployment contributions, written on Form 940 line 1a.",
   dt="CM", pre="The employer paid unemployment contributions to one State only.", om="US State or District (USPS code)", lvl=ER,
   grp="Employer federal returns", label="Single state abbreviation")
el("er.correction_w2_certification", "Form 941-X Form W-2 certification",
   "Employer's certification on Form 941-X line 3 that wage statements were or will be furnished or corrected.",
   dt="CM", pre="The employer files a Form 941-X correction.", om=B, lvl=ER, grp="Employer federal returns",
   label="W-2/W-2c certification")
el("er.correction_one_line", "Form 941-X under- and over-reported on one line",
   "Flag for Form 941-X line 41 that the correction reports under- and over-reported amounts on one line.",
   dt="CM", pre="The employer files a Form 941-X correction.", om=B, lvl=ER, grp="Employer federal returns",
   label="Under- and over-reported on one line")
el("er.correction_reclassified", "Form 941-X reclassified workers indicator",
   "Flag for Form 941-X line 42 that the correction reclassifies workers.",
   dt="CM", pre="The employer files a Form 941-X correction.", om=B, lvl=ER, grp="Employer federal returns",
   label="Reclassified workers")
el("er.correction_explanation", "Form 941-X explanation",
   "Free-text explanation of the correction for Form 941-X line 43.",
   dt="CM", pre="The employer files a Form 941-X correction.", lvl=ER, grp="Employer federal returns", label="Explanation")
el("er.aca_dge", "ACA designated government entity",
   "Name, address and contact of the designated government entity on Form 1094-C lines 9 to 16.",
   dt="CM", pre="A designated government entity files for the employer.", lvl=ER, grp="ACA", label="Designated Government Entity")
el("er.aca_authoritative_transmittal", "ACA authoritative transmittal indicator",
   "Flag for Form 1094-C line 19 that this is the authoritative transmittal for the employer.",
   dt="CM", pre="The employer files Forms 1094-C and 1095-C.", om=B, lvl=ER, grp="ACA", label="Authoritative transmittal")
el("er.aca_aggregated_group", "ACA aggregated applicable large employer group member",
   "Flag for Form 1094-C line 21 that the employer is a member of an aggregated applicable large employer group.",
   dt="CM", pre="The employer files Forms 1094-C and 1095-C.", om=B, lvl=ER, grp="ACA", label="Member of Aggregated ALE Group")
el("er.aca_certifications", "ACA certifications of eligibility",
   "Certifications of eligibility selected on Form 1094-C line 22 (qualifying offer method and the offer method certifications).",
   dt="CM", pre="The employer files Forms 1094-C and 1095-C.", lvl=ER, grp="ACA", label="Certifications of Eligibility")
el("er.aca_other_members", "ACA other applicable large employer members of the group",
   "Names and EINs of the other members of the aggregated group listed on Form 1094-C.",
   dt="CM", pre="The employer is a member of an aggregated applicable large employer group.", lvl=ER, grp="ACA",
   label="Other ALE Members")
el("er.w2_agent_indicator", "W-2 agent indicator code",
   "Code stating whether a reporting agent or common paymaster files the wage file for the employer.",
   dt="CM", pre="A reporting agent or common paymaster files for the employer.", om="W-2 agent indicator code", lvl=ER,
   grp="Employer W-2 batch configuration", facts=["rspec.fed.efw2.re.agent_indicator.codes"], label="Agent Indicator Code")
el("er.w2_kind_of_employer", "W-2 kind of employer",
   "Code for the kind of employer written on the employer record of the wage file.",
   dt="M", om="W-2 kind of employer", lvl=ER, grp="Employer W-2 batch configuration",
   facts=["rspec.fed.efw2.re.kind_of_employer.codes"], label="Kind of Employer")
el("er.w2_employment_code", "W-2 employment code",
   "Code for the type of employment (regular, household, agricultural, military and others) of the wage file.",
   dt="M", om="W-2 employment code", lvl=ER, grp="Employer W-2 batch configuration",
   facts=["rspec.fed.efw2.re.employment_code.codes"], label="Employment Code")
el("er.w2_tax_jurisdiction", "W-2 tax jurisdiction code",
   "Code for the tax jurisdiction of the wage file (domestic or a territory).",
   dt="M", om="W-2 tax jurisdiction code", lvl=ER, grp="Employer W-2 batch configuration",
   facts=["rspec.fed.efw2.re.tax_jurisdiction.codes"], label="Tax Jurisdiction Code")
el("er.w2_third_party_sick_pay", "W-2 third-party sick pay indicator",
   "Indicator that the employer record covers third-party sick pay.",
   dt="M", om="W-2 third-party sick pay indicator", lvl=ER, grp="Employer W-2 batch configuration",
   facts=["rspec.fed.efw2.re.third_party_sick_pay.codes"], label="Third-Party Sick Pay Indicator")
el("er.w2_terminating_business", "W-2 terminating business indicator",
   "Indicator on the employer record that the business ended and the wage file is the last.",
   dt="CM", pre="The business ended during the reporting year.", om=B, lvl=ER, grp="Employer W-2 batch configuration",
   label="Terminating Business Indicator")
el("er.w2_resub_indicator", "W-2 resubmission indicator",
   "Indicator on the submitter record that the wage file is a resubmission.",
   dt="CM", pre="The wage file is a resubmission.", om=B, lvl=ER, grp="Employer W-2 batch configuration",
   label="Resub Indicator",
   note="The code values of this indicator are not named in the cited sources.")

el("er.newhire_designated_state", "Designated new-hire State",
   "State chosen by a multistate employer to receive all of its new-hire reports, set after the employer notifies HHS.",
   dt="CM", pre="The employer reports electronically in more than one State and designates one State.",
   om="US State or District (USPS code)", lvl=ER, grp="Employer registration",
   facts=["rspec.fed.new_hire.multistate_designation"], label="Designated State")


# return-level indicators: master-data sheet, but set per return (QA r1 finding 12)
RETURN_LEVEL = ("er.no_ss_medicare_wages", "er.business_closed", "er.final_wage_date", "er.correction_w2_certification",
                "er.correction_one_line", "er.correction_reclassified", "er.correction_explanation",
                "er.w2_terminating_business", "er.w2_resub_indicator")
for _e in ELEMENTS:
    if _e["id"] in RETURN_LEVEL:
        _e["desc"] = _e["desc"].rstrip() + " Entered for the return period it applies to (effective-dated per return); not a standing master value."
