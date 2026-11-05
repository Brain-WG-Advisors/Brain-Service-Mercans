# Writes 07-qa-crosscheck/US-TEST0.json (schema mercans-test0/1.0).
# Every item was attempted with WebFetch on the authority URL of its register row on 2026-11-04 (compliance-qa-auditor, run close).
import json, os
HERE = os.path.dirname(os.path.abspath(__file__)); OUTF = os.path.join(HERE, "..", "US-TEST0.json")
D = "2026-11-04"
P15 = ("IRS", "Publication 15 (2026), Employer's Tax Guide", "https://www.irs.gov/publications/p15")
I940 = ("IRS", "Instructions for Form 940 (edition on irs.gov: TY2025)", "https://www.irs.gov/instructions/i940")
IW2 = ("IRS", "General Instructions for Forms W-2 and W-3 (2026)", "https://www.irs.gov/instructions/iw2w3")
EDD = ("California EDD", "Rates and Withholding (2026)", "https://edd.ca.gov/en/payroll_taxes/rates_and_withholding/")
DFS = ("NY Department of Financial Services", "PFL rate decision 2026", "https://www.dfs.ny.gov/apps-and-licensing/health-insurers/pfl-rate-decision-2026-page")
NYPFL = ("New York State Paid Family Leave", "2026 Paid Family Leave updates", "https://paidfamilyleave.ny.gov/2026")
WAPL = ("Washington ESD Paid Leave", "Employer roles and responsibilities", "https://paidleave.wa.gov/employer-roles-responsibilities/")
CAMW = ("California DIR / DLSE", "Minimum wage FAQ", "https://www.dir.ca.gov/dlse/faq_minimumwage.htm")
NY195 = ("New York State Senate", "Labor Law section 195", "https://www.nysenate.gov/legislation/laws/LAB/195")
PADOR = ("Pennsylvania Department of Revenue", "Employer withholding", "https://www.pa.gov/agencies/revenue/resources/tax-types-and-information/employer-withholding")
W4 = ("IRS", "Form W-4 (2026)", "https://www.irs.gov/pub/irs-pdf/fw4.pdf")
ORPR = ("Oregon Employment Department", "2026 tax rate press release (2025-11-18)", "https://www.oregon.gov/employ/NewsAndMedia/Documents/2025-11-18_Tax_Rate_2026_Press_Release.pdf")
TXLC = ("Texas Legislature", "Labor Code chapter 201 (201.082)", "https://tcss.legis.texas.gov/resources/LA/htm/LA.201.htm")
USC653 = ("US Code (govinfo)", "42 U.S.C. 653a", "https://www.govinfo.gov/content/pkg/USCODE-2024-title42/html/USCODE-2024-title42-chap7-subchapIV-partD-sec653a.htm")
RCW = ("Washington Legislature", "RCW 26.23.040", "https://app.leg.wa.gov/RCW/default.aspx?cite=26.23&full=true")
q = {
 "p15a": "The withholding rate on supplemental wages remains 22% (37% if supplemental wages paid to an employee during the calendar year exceed $1 million)",
 "p15b": "The rate of social security tax on taxable wages is 6.2% each for the employer and employee. The social security wage base limit is $184,500. The Medicare tax rate is 1.45% each for the employee and employer",
 "p15c": "monthly or semiweekly deposit schedule, determined by the lookback period",
 "p15d": "Form 941 due by the last day of the month following the end of the quarter (April 30, July 31, October 31, January 31)",
 "940a": "The FUTA tax is 6.0% (0.060) for 2025.",
 "940b": "You owe FUTA tax on the first $7,000 you pay to each employee during the calendar year.",
 "940c": "Most employers receive a maximum credit of up to 5.4% (0.054) against this FUTA tax.",
 "940d": "If your FUTA tax is more than $500 for the calendar year, you must deposit at least one quarterly payment.",
 "w2a": "Code TA: employer contributions under a section 128 Trump account contribution program",
 "w2b": "Code TP: the total amount of cash tips reported to the employer; Code TT: the total amount of qualified overtime compensation",
 "w2c": "Box 14b ... to report the Treasury Tipped Occupation Code(s)",
 "w2d": "Do not truncate the employees' SSN on Copy A ... An employer's EIN may not be truncated on any form.",
 "w2e": "use additional Forms W-2 when the boxes 15-20 capacity (two states/localities) is exceeded",
 "edd1": "The SDI withholding rate for 2026 is 1.3 percent. Effective January 1, 2024, Senate Bill 951 removes the taxable wage limit and maximum withholdings for each employee subject to SDI contributions.",
 "edd2": "The taxable wage limit is $7,000 per employee, per calendar year.",
 "edd3": "The ETT rate for 2026 is 0.1 percent.",
 "dfs": "0.432% of an employee's wages each pay period ... $411.91",
 "nypfl": "2026 NYSAWW $1,833.63; maximum weekly benefit $1,228.53; 67% of their average weekly wage, up to a cap of 67% of the current NYSAWW",
 "wa": "1.13% of each employee's gross wages, not including tips, up to the 2026 Social Security cap ($184,500) ... up to 71.43% can be paid by the employee",
 "camw1": "Effective January 1, 2026, the minimum wage is $16.90 per hour for all employers",
 "camw2": "not less than 85 percent of the minimum wage rounded to the nearest nickel during their first 160 hours of employment",
 "ny195a": "furnish each employee with a statement with every payment of wages, listing ... the dates of work covered ... name of employee; name of employer; address and phone number of employer; rate or rates of pay ... gross wages; deductions; allowances ... net wages",
 "ny195b": "establish, maintain and preserve for not less than six years contemporaneous, true, and accurate payroll records",
 "pa": "Entities are required to withhold PA personal income tax at a flat rate of 3.07 percent of compensation",
 "w4": "Form W-4 2026 ... Step 2: Multiple Jobs or Spouse Works ... Step 3: Claim Dependent and Other Credits ... (b) Deductions. Use the Deductions Worksheet on page 4",
 "or1": "The Paid Leave Oregon contribution rate for 2026 will remain at 1%.",
 "or2": "set by the annual Social Security taxable maximum wage amount, will rise 4.7 percent to $184,500 of wages per employee in 2026",
 "tx": "that part of the remuneration ... that exceeds remuneration to the individual ... by the employer, of $9,000",
 "653a": "not later than 20 days after the date the employer hires the employee ... the date services for remuneration were first performed by the employee",
 "rcw": "within twenty days of the hiring, rehiring, or return to work of the employee",
}
A = []


def add(art, loc, assertion, risk, src, quote_key=None, result="PASS", note=None):
    s = {"authority": src[0], "title": src[1], "url": src[2], "consulted_on": D}
    if quote_key:
        s["quote"] = q[quote_key]
    a = {"id": f"T{len(A) + 1:02d}", "artifact": art, "location": loc, "assertion": assertion, "risk": risk, "source": s, "result": result}
    if note:
        a["note"] = note
    A.append(a)


PDFNOTE = "PDF retrieved by WebFetch from the authority URL; text extracted locally with pypdf"
add("CCG", "annex_FED FED.3 fed.fica.oasdi.wage_base [US-FED-022]", "OASDI wage base 2026 = 184,500", "high", P15, "p15b")
add("WTC", "Wage Type Catalogue / 21900 / Explanation (fed.fica.oasdi.rate.employee) [US-FEDS5-005]", "OASDI rate 6.2% employee and employer", "high", P15, "p15b")
add("PSL", "Compliance Payslip!A92 (fed.fica.medicare.rate.employee) [US-FEDS5-005]", "Medicare rate 1.45% employee", "high", P15, "p15b")
add("CCG", "annex_FED FED.2 fed.fit.supplemental.flat_rate [US-FEDS5-003]", "Supplemental flat rate 22%", "high", P15, "p15a")
add("DD", "ID Information / Supplemental wage withholding method election / Additional Notes (fed.fit.supplemental.mandatory_rate)", "Mandatory 37% on supplemental wages over 1,000,000", "high", P15, "p15a")
add("DD", "Country Option Mappers / Federal depositor status (dd.fed.depositor_status.codes) [US-FEDS5-004]", "Two deposit schedules: monthly and semiweekly", "medium", P15, "p15c", note="summary of the deposit-schedule section")
add("RSPEC", "US-IRS-001 Form 941 example (rspec.fed.form941.frequency) [US-FEDS5-004]", "Form 941 quarterly, due last day of the month after the quarter", "high", P15, "p15d")
add("CCG", "annex_FED FED.3 fed.futa.rate.gross [US-FED-007]", "FUTA gross rate 6.0%", "high", I940, "940a", note="irs.gov edition is TY2025; the rate is statutory (26 USC 3301, US-FED-013); facts carry it from 2025-01-01")
add("WTC", "Wage Type Catalogue FUTA row (fed.futa.wage_base) [US-FED-007]", "FUTA wage base 7,000", "high", I940, "940b")
add("RSPEC", "US-IRS-004 Form 940 example (fed.futa.credit.max) [US-FED-007]", "Maximum FUTA credit 5.4%", "high", I940, "940c")
add("CCG", "annex_FED FED.3 fed.futa.rate.net [US-FED-007]", "Net FUTA rate 0.6% (6.0 less 5.4)", "high", I940, "940c")
add("RSPEC", "US-IRS-004 Form 940 example (fed.futa.deposit_threshold) [US-FEDS5-031]", "FUTA deposit required when liability exceeds 500", "medium", I940, "940d")
add("RSPEC", "US-SSA-001 W2 example (rspec.fed.w2.box12.new_codes) [US-FEDS5-007]", "W-2 box 12 code TA = Trump account employer contributions", "medium", IW2, "w2a")
add("RSPEC", "US-SSA-001 W2 example (rspec.fed.w2.box12.new_codes) [US-FEDS5-007]", "W-2 box 12 codes TP cash tips and TT qualified overtime", "medium", IW2, "w2b")
add("DD", "Country Fields / Primary Treasury Tipped Occupation Code (dd.fed.w2.tipped_occupation_code) [US-FEDS5-007]", "W-2 box 14b carries the Treasury Tipped Occupation Code (TY2026)", "medium", IW2, "w2c")
add("DD", "ID Information / Employee SSN / Additional Notes (rspec.fed.w2.ssn_truncation) [US-FEDS5-007]", "SSN truncation only on employee copies, never Copy A; EIN never truncated", "medium", IW2, "w2d")
add("RSPEC", "US-SSA-001 RS-024 (rspec.fed.w2.multistate_boxes) [US-MULTIS5-011]", "Boxes 15-20 hold two states/localities; more needs additional W-2", "low", IW2, "w2e")
add("WTC", "Wage Type Catalogue / PROG CA sdi / Explanation (ca.sdi.employee.rate) [US-CAP7-002]", "CA SDI employee rate 2026 = 1.3%", "high", EDD, "edd1")
add("CCG", "annex_CA CA.3 SDI wage cap exists (ca.sdi.wage_cap.exists=False) [US-CAP7-002]", "CA SDI has no taxable wage limit (from 2024)", "high", EDD, "edd1")
add("WTC", "Wage Type Catalogue / SUI CA / Explanation (ca.sui.wage_base) [US-CAS5-016]", "CA UI taxable wage limit 7,000", "high", EDD, "edd2")
add("WTC", "Wage Type Catalogue / SUI CA / Explanation (ca.ett.rate) [US-CAP7-001]", "CA ETT rate 2026 = 0.1%", "medium", EDD, "edd3")
add("WTC", "Wage Type Catalogue / PROG NY pfl / Explanation (ny.pfl.employee.rate)", "NY PFL employee rate 2026 = 0.432%", "high", DFS, "dfs")
add("WTC", "Wage Type Catalogue / PROG NY pfl / Explanation (ny.pfl.employee.max_annual)", "NY PFL annual maximum 2026 = 411.91", "high", DFS, "dfs")
add("CCG", "annex_NY (ny.pfl.nysaww) [US-NYB5-002]", "NYSAWW 2026 = 1,833.63", "medium", NYPFL, "nypfl")
add("CCG", "annex_NY (ny.pfl.benefit.max_weekly) [US-NYB5-002]", "PFL maximum weekly benefit 2026 = 1,228.53", "low", NYPFL, "nypfl")
add("CCG", "annex_NY (ny.pfl.benefit.rate_of_aww) [US-NYB5-002]", "PFL benefit = 67% of AWW", "low", NYPFL, "nypfl")
add("WTC", "Wage Type Catalogue / PROG WA pfml / Explanation (wa.pfml.total.rate) [US-WAS5-015]", "WA PFML total premium 2026 = 1.13%", "high", WAPL, "wa")
add("WTC", "Wage Type Catalogue / PROG WA pfml / Explanation (wa.pfml.employee.share) [US-WAB5-002]", "WA PFML employee share up to 71.43%", "high", WAPL, "wa")
add("CCG", "annex_WA (wa.pfml.wage_cap.annual)", "WA PFML wage cap 2026 = 184,500", "high", WAPL, "wa")
add("CCG", "annex_CA CA.1 Minimum wage hourly (ca.minwage.hourly) [US-CAS5-006]", "CA minimum wage 2026 = 16.90 per hour", "high", CAMW, "camw1")
add("CCG", "annex_CA CA.1 learner percent (ca.minwage.learner.percent) [US-CAS5-006]", "Learners: 85% of minimum wage for the first 160 hours", "low", CAMW, "camw2")
add("PSL", "Field Option!C58 (psl.ny.statement.content) [US-NYS5-006]", "NY wage statement content under Labor Law 195(3)", "medium", NY195, "ny195a")
add("PSL", "Field Option!C150 (psl.ny.retention.payroll_records.years) [US-NYS5-006]", "NY payroll records kept 6 years", "low", NY195, "ny195b")
add("WTC", "Wage Type Catalogue / SIT PA / Explanation (pa.pit.rate.flat) [US-PAS5-009]", "PA withholding flat 3.07%", "high", PADOR, "pa")
add("DD", "Country Fields / Form W-4 deductions (Step 4(b)) / Additional Notes (dd.fed.w4_2026.fields) [US-FEDS5-006]", "2026 Form W-4 steps: 2 multiple jobs, 3 credits, 4(b) deductions", "medium", W4, "w4", note=PDFNOTE)
add("CCG", "annex_OR (or.pfml.rate.total) [US-ORS5-003]", "Paid Leave Oregon 2026 rate = 1%", "high", ORPR, "or1", note=PDFNOTE)
add("CCG", "annex_OR (or.pfml.wage_cap.annual) [US-ORS5-003]", "Paid Leave Oregon 2026 wage cap = 184,500", "high", ORPR, "or2", note=PDFNOTE)
add("WTC", "Wage Type Catalogue / SUI TX / Explanation (tx.sui.wage_base) [US-TXS5-007]", "TX UI taxable wage base = 9,000", "high", TXLC, "tx")
add("SIR", "6.1 New hire, federal (sir.fed.new_hire.days) [US-FEDS5-024]", "New-hire report due within 20 days of hire (federal floor)", "medium", USC653, "653a")
add("DD", "Country Fields / Date services first performed / Additional Notes (dd.fed.new_hire.date_first_services) [US-FEDS5-024]", "New-hire report carries the date services were first performed", "medium", USC653, "653a")
add("SIR", "7.5 US-SDNH-001-WA (sir.wa.new_hire.days) [US-WAS5-018]", "WA new-hire report within 20 days", "low", RCW, "rcw")


def blocked(art, loc, assertion, risk, auth, title, url, why):
    add(art, loc, assertion, risk, (auth, title, url), None, "UNVERIFIED",
        note=f"access blocked from this machine on {D}: {why}. The registered local copy (verified 2026-10-29..2026-11-03) contains the value (07-qa-crosscheck/_runclose/blocked_local.py), which does not count for C39. Re-verify on the authority site from a browser and set PASS/FAIL with a quote.")


blocked("CCG", "annex_FED (fed.fica.oasdi.wage_base, 2027 period) [US-FEDB5-401]", "OASDI wage base 2027 = 192,300", "high", "SSA", "Contribution and benefit base", "https://www.ssa.gov/oact/cola/cbb.html", "HTTP 403")
blocked("WTC", "Wage Type Catalogue / PROG CO famli (co.famli.employee.rate) [US-COB5-003]", "CO FAMLI 2026 = 0.88% split 0.44/0.44", "high", "Colorado FAMLI", "Employers", "https://famli.colorado.gov/employers", "HTTP 403")
blocked("PSL", "Field Option!C87 (psl.ca.ssn.rule) [US-CAS5-005]", "CA wage statement shows only the last 4 SSN digits or an employee ID", "medium", "California Legislature", "Labor Code 226", "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=LAB&sectionNum=226", "HTTP 403")
blocked("PSL", "Field Option!C144 (psl.ca.retention.wage_statements.years) [US-CAS5-005]", "CA wage statement copies kept 3 years", "low", "California Legislature", "Labor Code 226", "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=LAB&sectionNum=226", "HTTP 403")
blocked("WTC", "Wage Type Catalogue / SIT IN / Explanation (in.pit.rate) [US-INS5-009]", "IN income tax 2026 = 2.95%", "high", "Indiana DOR", "Rates, fees and penalties", "https://www.in.gov/dor/resources/tax-rates-and-reports/rates-fees-and-penalties/", "connection refused (two attempts)")
blocked("WTC", "Wage Type Catalogue / PROG MA pfml / Explanation (ma.pfml.rate.total.under_25) [US-MAS5-012]", "MA PFML under-25 employers total 0.46%", "high", "Mass.gov DFML", "PFML contribution rates and calculator", "https://www.mass.gov/info-details/paid-family-and-medical-leave-employer-contribution-rates-and-calculator", "HTTP 403")
blocked("CCG", "annex_FL (fl.sui.wage_base) [US-FLS5-003]", "FL reemployment tax wage base 7,000", "high", "Florida Senate", "Florida Statutes 443.1217", "https://www.flsenate.gov/Laws/Statutes/2026/443.1217", "page renders by script (only 'Loading Florida Statutes' returned)")
blocked("CCG", "annex_NC (nc.pit.rate.flat) [US-NCS5-011]", "NC income tax 2026 = 3.99%", "high", "NC General Assembly", "G.S. 105-153.7", "https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-153.7.html", "HTTP 403")
blocked("CCG", "annex_KY (ky.pit.rate.flat) [US-KYS5-009]", "KY income tax 2026 = 3.5%", "high", "Kentucky Legislature", "KRS 141.020", "https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=56339", "fetch failed (two attempts)")
blocked("CCG", "annex_UT (ut.pit.rate.flat) [US-UTS5-001]", "UT income tax 2026 = 4.45%", "high", "Utah Legislature", "Utah Code 59-10-104", "https://le.utah.gov/xcode/Title59/Chapter10/C59-10-S104_2026050620260506.html", "connection refused")
blocked("CCG", "annex_MI (mi.pit.rate.flat) [US-MIPIT-001]", "MI withholding 2026 = 4.25%", "high", "Michigan Treasury", "Withholding Guide 446 (2026)", "https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/SUW/TY2026/446_Withholding-Guide_2026.pdf", "HTTP 403")
blocked("CCG", "annex_CO (co.pit.rate.flat) [US-COS5-012]", "CO income tax 2026 = 4.4%", "high", "Colorado DOR", "DR 0004 (2026)", "https://tax.colorado.gov/sites/default/files/documents/DR_0004_2026.pdf", "PDF retrieved but the rate is not in its extractable text")
blocked("SIR", "sir.fed.w2.format [US-FIL-002]", "W-2 filed as EFW2 (Pub. 42-007), W-2c as EFW2C (42-014), via SSA BSO", "medium", "SSA", "EFW2 and EFW2C", "https://www.ssa.gov/employer/EFW2&EFW2C.htm", "HTTP 403")
blocked("SIR", "sir.tx.ui.agent_authorization [US-TXP52-008]", "TX agent authorization = Form C-42", "medium", "Texas Workforce Commission", "Form C-42", "https://www.twc.texas.gov/programs/unemployment-tax/forms/c-42", "HTTP 403")
blocked("CCG", "annex_OR (or.sui.wage_base.other_state_credit) [US-ORS5-015]", "OR UI wage base credits wages taxed by another State", "medium", "Oregon Legislature", "ORS chapter 657", "https://www.oregonlegislature.gov/bills_laws/ors/ors657.html", "connection refused")

doc = {"schema": "mercans-test0/1.0", "country": "US", "run_date": D,
       "sampling": ("risk-weighted: rates, wage bases and caps of the federal core and the largest State programmes first (high), "
                    "then filing rules and payslip content; one assertion per artifact cell bound to a registered fact; every item "
                    "attempted with WebFetch on the URL of its register row. Items whose page was blocked from this machine are kept "
                    "as UNVERIFIED, not dropped."),
       "assertions": A}
json.dump(doc, open(OUTF, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
print(len(A), sum(a["result"] == "PASS" for a in A), sum(a["risk"] == "high" for a in A))
