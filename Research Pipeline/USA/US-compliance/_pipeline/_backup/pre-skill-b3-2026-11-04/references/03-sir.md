United States of America

Statutory Integration Index — US-SIR-INDEX-001 v1.0

Provider-agnostic hand-off of federal, State and local statutory filings

| Field | Value |
|---|---|
| Document ID | US-SIR-INDEX-001 |
| Version | v1.0 |
| Country | United States of America (US) |
| Issue date | 2027-03-31 |
| Prepared by | Mercans Compliance Regulations Team |
| Companion documents | US-CCG-001 v1.0; US-WTC-001 v1.0; US-DD-001 v1.0; the Report Specifications US-*-Spec |


# Table of Contents

Right-click to update the Table of Contents.


# Document Control

| Field | Value |
|---|---|
| Document ID | US-SIR-INDEX-001 |
| Version | v1.0 |
| Country | United States of America (US) |
| Jurisdictions | Federal; 50 States and the District of Columbia; local taxing authorities named in section 7.7 |
| Discovery verdict | HAS_INTEGRATIONS. The single integrable party for Mercans is the third-party filing provider (owner decision): Mercans hands the provider the data set of section 8 and the provider transmits to each authority, including through the SFTP, web-service and bulk-file channels that some authorities publish. The provider runbook set is not issued until the provider is chosen: Not configured in this release (open gap SIR-RQ-27) |
| Language | English |
| Currency | USD |
| Package version | v1.0 |
| Issue date | 2027-03-31 |


## Version history

| Version | Date | Author | Status |
|---|---|---|---|
| v1.0 | 2027-03-31 | Wallisson Gomes | For QA |


# 0. Purpose, Scope & Audit Compliance

This index is the statutory-integration record for the United States of America. For every federal, State and local filing in scope it states who receives it, on which channel, under which agent authorisation and what a third-party filing provider must be given. Mercans produces the provider input and never submits to an authority; the provider transmits to each authority. The employer keeps legal liability for every return and deposit: retained by the employer = True [US-FED-008].

Discovery verdict: HAS_INTEGRATIONS. The single integrable party for Mercans is the third-party filing provider (owner decision): Mercans hands the provider the data set of section 8 and the provider transmits to each authority, including through the SFTP, web-service and bulk-file channels that some authorities publish. The provider runbook set is not issued until the provider is chosen: Not configured in this release (open gap SIR-RQ-27) Every inbound item is a document the employer acts on; no inbound file or message from an authority is parsed by the engine. Section 0.4 lists the integration status of each authority group.

The choice of filing provider is a business decision outside this document. Provider-specific input layouts replace the generic minimum data set of section 8 once a provider is chosen: Not configured in this release (open gap SIR-RQ-27)


## 0.1 Canonical integration inventory

| Integration ID | System | Direction | Product mapping required |
|---|---|---|---|
| US-OUT-001 | Statutory filing data hand-off to the third-party filing provider (all in-scope federal, State and local returns, deposits and new-hire reports) | OUTBOUND | Yes |
| US-OUT-002 | New-hire reporting (State Directory of New Hires; electronic two monthly transmissions) | OUTBOUND | Yes |
| US-INB-001 | Child-support income withholding orders (IWO / e-IWO) from State agencies | INBOUND | Yes |
| US-INB-002 | IRS notice of levy on wages (Form 668-W) with the employee's exemption statement | INBOUND | Yes |
| US-INB-003 | State UI contribution rate notices (annual employer rate per State, e.g. AZ UC-603, CA DE 2088, AK TR02) | INBOUND | Yes |


## 0.2 Direction & product-mapping rule

Direction is stated from the payroll engine outward: OUTBOUND is a submission or hand-off produced by the engine, INBOUND is a document or notice from an authority that the engine must act on. Product mapping is required wherever data held by the payroll product must be produced in, or read from, an authority or provider layout. Every Report Specification is outbound; the three inbound items of section 1 have no Report Specification because they are received, not filed.


## 0.3 Confidence and accuracy disclosure

Each hand-off row in section 7 carries the channel class, portal, confirmation status and accuracy statement of the matching Report Specification row (accuracy is stated on the Report Matrix scale of 0 to 100: lowest 50, highest 90). No filing was submitted and no real file was checked against an authority validator, so every channel stays marked as in the Report Specification; the closing evidence for each row is the provider's acceptance report or one accepted real filing.

Open questions recorded with the research (none blocks the document):

•  the choice of filing provider and its input layout: Not configured in this release (open gap SIR-RQ-27)

•  the New York withholding authorisation form: Not configured in this release (open gap SIR-RQ-22)

•  the Maine withholding and UI authorisation forms: Not configured in this release (open gap SIR-RQ-14)

•  the Mississippi withholding authorisation form: Not configured in this release (open gap SIR-RQ-18)

•  the Kentucky withholding and UI authorisation instruments: Not configured in this release (open gap SIR-RQ-10)

•  the Louisiana withholding authorisation form: Not configured in this release (open gap SIR-RQ-11)

•  the text of the Wyoming UI power of attorney form: Not configured in this release (open gap SIR-RQ-37)

•  the California electronic file layout of the quarterly wage detail: Not configured in this release (open gap SIR-RQ-04)

•  the Indiana W-2 XML schema: Not configured in this release (open gap SIR-RQ-08)

•  the tax-year State W-2 specification editions of eight jurisdictions: Not configured in this release (open gap SIR-RQ-36)

•  the UI wage-file layouts of eleven States: Not configured in this release (open gap SIR-RQ-35)

•  the Texas UI quarterly due date: Not configured in this release (open gap SIR-RQ-34)

•  the Michigan new-hire statute and penalty: Not configured in this release (open gap SIR-RQ-15)

•  the New Hampshire third-party administrator registration: Not configured in this release (open gap SIR-RQ-21)

•  the current Kansas Department of Revenue KW-100 withholding guide page: Not configured in this release (open gap SIR-RQ-09)

•  the 2026 Form 940 due date in the 2026 Instructions for Form 940: Not configured in this release (open gap SIR-RQ-03)

•  the 2026 electronic-filing threshold in the Instructions for Forms 1094-C and 1095-C: Not configured in this release (open gap SIR-RQ-02)

•  the Florida agent registration form RTS-9: Not configured in this release (open gap SIR-RQ-06)

•  the Massachusetts power of attorney form M-2848: Not configured in this release (open gap SIR-RQ-13)

•  the Mississippi reporting agent authorisation form J-9: Not configured in this release (open gap SIR-RQ-17)

•  the Nebraska reporting agent form 33: Not configured in this release (open gap SIR-RQ-20)

•  the Ohio Form JFS-20106: Not configured in this release (open gap SIR-RQ-26)

•  the Ohio municipal monthly-filing thresholds: Not configured in this release (open gap SIR-RQ-24)

Where the research does not support a statement, the cell reads "Not configured in this release" with a request number; the list is in Appendix B. A value is written only when every text element of it (numbers, form names, dates, channel names) was found in the saved copy of its cited source.


## 0.4 Integration landscape by authority group

One row per integrable party or authority group: whether a system-to-system channel exists, which channel, the direction from the payroll engine, the developer portal and the location of the configuration runbook. Authority channels that exist are operated by the filing provider, not by Mercans, so no authority runbook is issued.

| Party or authority group | Integration | Channel | Direction | Developer portal | Runbook location |
|---|---|---|---|---|---|
| Third-party filing provider (owner decision US-MQ-09) | Yes | File hand-off of the provider input data set of section 8; product mapping required | OUTBOUND | Not applicable | Not configured in this release (open gap SIR-RQ-27) |
| Internal Revenue Service | No | Provider-transmitted portal, file upload or electronic return; no system-to-system channel recorded | OUTBOUND | None recorded | None (no integration) |
| Social Security Administration | No | Provider-transmitted portal, file upload or electronic return; no system-to-system channel recorded | OUTBOUND | None recorded | None (no integration) |
| State departments of revenue / taxation (50 States and the District of Columbia) | Yes, operated by the filing provider | DE 8300 e-file guide: Upload Bulk Return File (zip <=10 MB) XML, ICESA or MMREF-1, CSV, or FSET XML web service [US-FIL-006]; Bulk Filing Guide Part A: IT 501, IT 941, SD 101, SD 141, FSET v4.4; ETIN [US-FIL-012]; Pub. 72.5 (2/25) NYS-45 Web Upload: prior approval, test file, agent identification number [US-FIL-007] | OUTBOUND | None recorded | None; no Mercans runbook (provider operates the channel) |
| State workforce / unemployment insurance agencies | Yes, operated by the filing provider | WR-30 quarterly, electronic (online or SFTP), due the 30th with no weekend extension [US-NJS5-017]; DOL-4N quarterly; electronic required at 25+ employees; portal entry, CSV/Excel (100-15,000), SFTP (>15,000 and payroll service providers) [US-GAS5-005]; RPT3795 + NEW0098 quarterly in ESS (entry, SFTP EFW2, CSV/tab) [US-NVS5-008] | OUTBOUND | None recorded | None; no Mercans runbook (provider operates the channel) |
| State programme agencies (paid leave, disability, workers' compensation) | Yes, operated by the filing provider | Batch XML (XSD) or CSV via SFTP per File Specification Toolkit v2.1.9; employer-level return totals only; acknowledgement file E/W [US-CTB5-001] | OUTBOUND | None recorded | None; no Mercans runbook (provider operates the channel) |
| State Directories of New Hires | No | Provider-transmitted portal, file upload or electronic return; no system-to-system channel recorded | OUTBOUND | None recorded | None (no integration) |
| Local taxing authorities (cities, counties, school districts, collectors) | No | Provider-transmitted portal, file upload or electronic return; no system-to-system channel recorded | OUTBOUND | None recorded | None (no integration) |
| Child-support agencies, IRS levy, State UI rate notices | No | Document received by the employer; not parsed by the engine | INBOUND | None recorded | None (no integration) |


# 1. Inbound Integrations (documents from authorities)


## 1.1 Finding: three inbound documents drive payroll configuration

No inbound file or message from an authority is parsed by the engine. Three kinds of document arrive and change what the payroll does, so the product must be able to take their data in: income withholding orders, the federal notice of levy on wages, and the State UI contribution rate notice.


## 1.2 Inbound register

| ID | Authority / document | Direction | What the engine must do | Product mapping; Report Spec |
|---|---|---|---|---|
| US-INB-001 | State child-support agencies (income withholding order, electronic or paper) | INBOUND | Set up the deduction, apply the governing law, remit within the State period. Governing law of an interstate order: When an employer receives an income withholding order issued by another State, the employer shall apply the income withholding law of the State of the obligor's principal place of employment in determining the employer's fee for processing an income withholding order; the maximum amount permitted to be withheld from the obligor's income; the time periods within which the employer must implement the income withholding order and forward the child support payment; the priorities for withholding and allocating income withheld for multiple child support obligees; and any withholding terms or conditions not specified in the order [US-MULTIS5-007] Remittance period: 7 business days [US-MULTIS5-007] Priority among garnishments: Withholding for support has priority over any other legal process under state law against the same income (section 466(b)(7) of the Social Security Act); if a federal tax levy is in effect, notify the sender [US-FEDP6-002] [US-FEDR3-003] (effective 2026-01-01 to 2026-12-31) Order form approval expiry: 2029-08-31 [US-FEDS5-028] (effective 2026-08-25 to 2029-08-31) | Yes; none (received, not filed) |
| US-INB-002 | Internal Revenue Service (notice of levy on wages, with the employee's exemption statement) | INBOUND | Exempt amount by filing status and dependents; the rest goes to the IRS. Exempt amount, single filer, no dependents, monthly: 1341.67 [US-FEDS5-014] (effective 2026-01-01 to 2026-12-31) | Yes; none (received, not filed) |
| US-INB-003 | State workforce agencies (annual UI contribution rate notice) | INBOUND | Employer rate per State and year, loaded as configuration data before the first payroll of the year. | Yes; none (received, not filed) |


# 2. Outbound Integrations (submissions through the provider)


## 2.1 Outbound register: one row per Report Specification

Channel classes are those of the Report Matrix of each specification (online_form, file_upload, xml, api, paper); xml is recorded only where the specification cites a published schema. Section 7 lists every report row.

| Report Spec | Direction | Report | Authority | Channel classes | Accuracy (0 to 100) | Hand-off register |
|---|---|---|---|---|---|---|
| US-DOR-001 | OUTBOUND | State Income-Tax Withholding Returns and Deposits | State departments of revenue / taxation (one per State; see Report Matrix) | online_form, file_upload, paper | 75 to 90 | Section 7.2 |
| US-DOR-002 | OUTBOUND | State Annual Withholding Reconciliation and State Copies of Form W-2 | State departments of revenue / taxation (one per State; see Report Matrix) | online_form, file_upload, api, paper | 75 to 90 | Section 7.3 |
| US-DOR-003 | OUTBOUND | Nevada Modified Business Tax Return (Form TAX-F003, general business) | Nevada Department of Taxation | online_form | 75 | Section 7.8 |
| US-DOR-004 | OUTBOUND | Employer Payroll Transit Levies (Oregon, New York) | Oregon Department of Revenue; New York State Department of Taxation and Finance | online_form | 75 to 85 | Section 7.8 |
| US-IRS-001 | OUTBOUND | Form 941 Employer's Quarterly Federal Tax Return | Internal Revenue Service (IRS), U.S. Department of the Treasury | file_upload | 85 | Section 7.1 |
| US-IRS-002 | OUTBOUND | Form 944 Employer's Annual Federal Tax Return | Internal Revenue Service (IRS), U.S. Department of the Treasury | file_upload | 80 | Section 7.1 |
| US-IRS-003 | OUTBOUND | Form 943 Employer's Annual Federal Tax Return for Agricultural Employees | Internal Revenue Service (IRS), U.S. Department of the Treasury | file_upload | 80 | Section 7.1 |
| US-IRS-004 | OUTBOUND | Form 940 Employer's Annual Federal Unemployment (FUTA) Tax Return | Internal Revenue Service (IRS), U.S. Department of the Treasury | file_upload | 80 | Section 7.1 |
| US-IRS-005 | OUTBOUND | Schedule H Routing (Household Employees) | Internal Revenue Service (IRS), U.S. Department of the Treasury | none (routing flag) | 90 | Section 7.1 |
| US-IRS-006 | OUTBOUND | Form 1042-S Treaty-Exempt Wages of Nonresident Aliens | Internal Revenue Service (IRS), U.S. Department of the Treasury | file_upload | 80 | Section 7.1 |
| US-IRS-007 | OUTBOUND | Forms 1094-C and 1095-C (ACA Employer Reporting) | Internal Revenue Service (IRS), U.S. Department of the Treasury | file_upload | 75 | Section 7.1 |
| US-IRS-008 | OUTBOUND | Form 941-X Adjusted Employer's Quarterly Federal Tax Return | Internal Revenue Service (IRS), U.S. Department of the Treasury | file_upload | 85 | Section 7.1 |
| US-LOC-001 | OUTBOUND | Local Income / Wage Tax Returns | Local taxing authorities (cities, counties, school districts, collectors; see Report Matrix) | online_form, file_upload, api, paper | 70 to 75 | Section 7.7 |
| US-LOC-002 | OUTBOUND | City Employer Payroll Taxes (Jersey City, Newark, St. Louis, Pittsburgh) | City tax offices (see Report Matrix) | online_form, paper | 75 | Section 7.7 |
| US-LOC-003 | OUTBOUND | Seattle Payroll Expense Tax and Social Housing Tax Returns | City of Seattle, Department of Finance and Administrative Services | online_form, paper | 85 | Section 7.7 |
| US-PFML-001 | OUTBOUND | State PFML / SDI / LTC Programme Reports | State programme agencies (one per programme; see Report Matrix) | online_form, file_upload, xml | 50 to 90 | Section 7.6 |
| US-SDNH-001 | OUTBOUND | New-Hire Report (State Directories of New Hires) | State Directories of New Hires (one per State; HHS designation for multistate employers) | online_form, file_upload, paper | 50 to 80 | Section 7.5 |
| US-SSA-001 | OUTBOUND | Forms W-2 and W-3 (EFW2) Wage and Tax Statements | Social Security Administration (SSA), with the IRS | file_upload | 90 | Section 7.1 |
| US-UI-001 | OUTBOUND | State Unemployment Insurance Quarterly Contribution and Wage Reports | State workforce / unemployment insurance agencies (one per State; see Report Matrix) | online_form, file_upload, xml, api, paper | 50 to 90 | Section 7.4 |
| US-WC-001 | OUTBOUND | State-Fund Workers' Compensation Premiums and Fees Collected through Payroll (WA, NM, OR, WY) | WA Department of Labor & Industries; NM Taxation and Revenue Department; OR Department of Revenue; WY Department of W... | online_form | 75 | Section 7.8 |


## 2.2 What each channel carries

| Category | Reported to | Specification |
|---|---|---|
| Federal employment tax returns, deposits and corrections | IRS | US-IRS-001 to US-IRS-008 |
| Wage and tax statements and transmittals | SSA; State revenue departments | US-SSA-001; US-DOR-002 |
| State withholding returns and deposits | State revenue departments | US-DOR-001; US-DOR-003; US-DOR-004 |
| State UI wage reports | State workforce agencies | US-UI-001 |
| Paid-leave, disability and workers' compensation reports | State programme agencies | US-PFML-001; US-WC-001 |
| Local returns | Cities, counties, school districts, collectors | US-LOC-001; US-LOC-002; US-LOC-003 |
| New-hire reports | State Directories of New Hires | US-SDNH-001 |


# 3. Authorisation Requirements


## 3.1 Federal appointment

| Item | Requirement | Source |
|---|---|---|
| Reporting agent authorisation | Form 8655 Reporting Agent Authorization (Rev. 1-2024), one per EIN | [US-FED-028] |
| Returns and deposits covered; State and local extension | Line 15: 940, 941, 943, 944, 945, 1042, CT-1; line 16 deposits; line 19 extends the authorisation to state/local returns related to lines 15/16 | [US-FED-028] |
| Technical specification for reporting agents | Pub. 1474 (Rev. 4-2026): reporting agent = accounting service, franchiser, bank, service bureau or other payroll-services entity; agent list additions/deletions electronic above 100 submissions a week via SLFT B2B; deposits via EFTPS or FTA | [US-FIL-001] |
| Third-party payer arrangements | Pub. 15 (2026) third-party payer arrangements (reporting agents, sec. 3504 agents, CPEOs) - liability allocation per arrangement | [US-FEDP51-002] |


## 3.2 Two authorisations per State

The federal agreement does not replace the State instruments. Each wage-tax State needs an authorisation from the employer to the revenue department (withholding) and another to the workforce agency (UI); the revenue department and the workforce agency are separate institutions with separate portals. Several States now use an online link or handshake instead of a paper form; the instrument of each jurisdiction is listed in section 3.3.


## 3.3 Authorisation instrument per jurisdiction

| Jurisdiction | Withholding authorisation (revenue department) | UI authorisation (workforce agency) |
|---|---|---|
| Alaska (AK) | No State wage tax, so no withholding authorisation: none: no state wage tax [US-AKWT-001] | UI Tax Power of Attorney (Rev. 7/24), eight checkable areas [US-AKP51-006] |
| Alabama (AL) | Not configured in this release (open gap SIR-RQ-33) | Department of Workforce UC Power of Attorney (rev. 02/2025): TAX, BENEFITS, TAX AND BENEFITS, TAX REPORTS ONLY [US-ALP52-002] |
| Arkansas (AR) | DFA Power of Attorney (rev. September 2025) [US-ARP52-003] | Not configured in this release (open gap SIR-RQ-28) |
| Arizona (AZ) | Form 821-PSC Withholding Tax Payroll Service Company Authorization [US-AZP52-001] | DES UIT-1146A Limited Power of Attorney [US-AZP52-002] |
| California (CA) | DE 48 Power of Attorney Declaration (e-Services or mail) [US-CAEDD-006] | DE 48 Power of Attorney Declaration (e-Services or mail) [US-CAEDD-006] |
| Colorado (CO) | DR 0145 Tax Information Designation and Power of Attorney [US-COP51-006] | Employers can assign a TPA online in MyUI Employer+ (Account Maintenance dropdown > Third Party Administrator (TPA) authorization link); only employers can assign a TPA to an employer account [US-COP52-003] |
| Connecticut (CT) | DRS LGL-001 / LGL-003 [US-CTP51-007] | TPA Certificate of Representation (COR) and client link in ReEmployCT [US-CTP52-002] |
| District of Columbia (DC) | OTR D-2848 [US-DCP51-014] | Power of Attorney, Form No. OUCTAX-1, District of Columbia Department of Employment Services [US-DCP52-003] |
| Delaware (DE) | Not configured in this release (open gap SIR-RQ-33) | DUI Power of Attorney (UI); withholding representation by IRS 2848 only [US-DEP52-002] |
| Florida (FL) | No State wage tax, so no withholding authorisation: none: no income tax on natural persons [US-FL-001] | Not configured in this release (open gap SIR-RQ-05) |
| Georgia (GA) | Power of Attorney and Declaration of Representative (Form RD-1061); Disclosure Authorization Form (Form RD-1062); Reporting Agent Authorization (Form RD-1063) [US-GAW1B-003] | GDOL power of attorney [US-GAW1B-001] |
| Hawaii (HI) | Form N-848 Power of Attorney [US-HIP51-004] | Employers authorize a Third-Party Administrator (TPA) online through the employer portal (UC-25 Notification of Changes, Add SIDES Agent); a Letter of Authorization or Power of Attorney is no longer required [US-HIP52-003] [US-HIS5-012] |
| Iowa (IA) | IA 2848 (14-101a, 06/18/2026) [US-IAP51-003] | IWD 68-0092 Power of Attorney or Authorized Representative [US-IAP51-004] |
| Idaho (ID) | Form ID-POA (withholding) [US-IDR3-001] | Idaho Department of Labor Employer Portal Authorization Form [US-IDR3-002] |
| Illinois (IL) | Form IL-2848 POA incl. withholding income tax accounts [US-IL-004] | IDES service bureau MOU with POA option; E-POA bulk file (caret-delimited, max 1000 rows/day) [US-ILP52-010] |
| Indiana (IN) | POA-1 or INTIME ePOA [US-INR3-003] | Agent authorised in ESS at one of three levels (UI Agent Handbook) [US-INR3-004] |
| Kansas (KS) | DO-10 Power of Attorney [US-KSP51-005] | K-CNS-032 TPA link form [US-KSP52-003] |
| Kentucky (KY) | Not configured in this release (open gap SIR-RQ-10) | Not configured in this release (open gap SIR-RQ-10) |
| Louisiana (LA) | Not configured in this release (open gap SIR-RQ-11) | Online Power of Attorney in LAWATS [US-LAP52-005] |
| Massachusetts (MA) | Not configured in this release (open gap SIR-RQ-12) | Not configured in this release (open gap SIR-RQ-12) |
| Maryland (MD) | Form 548P Limited Power of Attorney and Maryland Reporting Agents Authorization (Comptroller of Maryland), used in place of the federal Form 8655 [US-MDP51-001] | Not configured in this release (open gap SIR-RQ-28) |
| Maine (ME) | Not configured in this release (open gap SIR-RQ-14) | Not configured in this release (open gap SIR-RQ-28) |
| Michigan (MI) | Treasury Form 151 Authorized Representative Declaration [US-MIP52-011] | UIA 1488 Power of Attorney [US-MIP52-005] |
| Minnesota (MN) | REV184b Business Power of Attorney [US-MNP52-005] | UI Agent Self-Service ID (8-digit Agent ID) [US-MNP6-003] |
| Missouri (MO) | Not configured in this release (open gap SIR-RQ-33) | Division of Employment Security (DES) Power of Attorney: a signed, written agreement must be submitted to the DES (the DES provides a Power of Attorney form) [US-MOP52-008] |
| Mississippi (MS) | Not configured in this release (open gap SIR-RQ-18) | Not configured in this release (open gap SIR-RQ-16) |
| Montana (MT) | Montana Form POA or federal 2848; third-party access in TAP [US-MTS5-005] | Not configured in this release (open gap SIR-RQ-28) |
| North Carolina (NC) | Not configured in this release (open gap SIR-RQ-33) | DES Power of Attorney and Declaration of Representative (one per agent per employer) [US-NCP51-003] |
| North Dakota (ND) | Form 500 Authorization to Disclose / Designation of Representative; payroll provider designated on registration [US-NDP51-002] | Not configured in this release (open gap SIR-RQ-28) |
| Nebraska (NE) | Not configured in this release (open gap SIR-RQ-19) | Not configured in this release (open gap SIR-RQ-19) |
| New Hampshire (NH) | No State wage tax, so no withholding authorisation: none: no state wage tax [US-NH-006] | Written request to NHES to designate an authorized agent; the request must be made by the employer and signed by a duly authorized employee whose position or title is stated in the request [US-NHP6-001] |
| New Jersey (NJ) | M-5008-R Appointment of Taxpayer Representative (6/26) [US-NJR3-004] | New Jersey Department of Labor Division of Employer Accounts Power of Attorney form [US-NJR3-005] |
| New Mexico (NM) | ACD-31102 Tax Information Authorization [US-NMP51-004] | ES-905 Power of Attorney / Authorization of Agent or TPA login [US-NMP6-001] |
| Nevada (NV) | No State wage tax, so no withholding authorisation: none: no state wage tax [US-NVP51-001] | Agent added as external ESS user [US-NVR3-003] |
| New York (NY) | Not configured in this release (open gap SIR-RQ-22) | Pub. 72.5 (2/25) NYS-45 Web Upload: prior approval, test file, agent identification number [US-FIL-007] |
| Ohio (OH) | WT 8655 Payroll Service Company Authorization [US-FIL-011] | Not configured in this release (open gap SIR-RQ-25) |
| Oklahoma (OK) | BT-129 Power of Attorney (Rev. 7-2026) [US-OKP51-004] | OES-190T Appointment of Account Representative [US-OKP51-005] |
| Oregon (OR) | Form OR-AUTH-REP (authorized representative) / Form OR-AUTH-INFO (designee), Oregon Department of Revenue [US-ORP51-005] | Form OR-AUTH-REP (authorized representative) / Form OR-AUTH-INFO (designee), Oregon Department of Revenue [US-ORP51-005] |
| Pennsylvania (PA) | REV-677 Power of Attorney (07-25) [US-FIL-010] | Employers using a TPA must electronically register the Power of Attorney relationship in UCMS by assigning the TPA to their account; the TPA must then accept the association (the handshake) [US-PAP51-004] |
| Rhode Island (RI) | RI-2848 [US-RIP51-004] | Not configured in this release (open gap SIR-RQ-28) |
| South Carolina (SC) | SC2848 [US-SCP52-001] | UCE-1010 Written Authorization [US-SCR3-008] |
| South Dakota (SD) | No State wage tax, so no withholding authorisation: none: no state wage tax [US-SDS5-001] | RA POA Rev. 01/2026 (Tax, Benefits or Limited) [US-SDP51-001] |
| Tennessee (TN) | No State wage tax, so no withholding authorisation: False [US-TNP51-001] | POAs are no longer needed; third-party filers use the Manage Clients link (Register Client UI Tax Account link for employers not yet registered) in Employer e-Services; wage reports are filed in Employer e-Services from May 27, 2025 [US-TNR3-002] |
| Texas (TX) | No State wage tax, so no withholding authorisation: none: no state income tax [US-TXS5-001] | Form C-42 Written Authorization to Represent Employing Unit [US-TXP52-008] |
| Utah (UT) | TC-737 Power of Attorney (Rev. 9/26) [US-UTP6-002] | DWS UI Power of Attorney (Rev. 08/24) [US-UTP6-003] |
| Virginia (VA) | PAR 101 (person, not business) [US-VAP51-007] | ESS TPA invitation; ID.me login from 2026-08-01 [US-VAP6-001] |
| Vermont (VT) | Form PA-1 Special Power of Attorney [US-VTP51-012] | Form C-50 Limited Power of Attorney [US-VTP51-013] |
| Washington (WA) | No State wage tax, so no withholding authorisation: none: no income tax [US-WAS5-013] | Complete and sign a power of attorney form for each client company; add the third-party administrator's information in the representative sections of the power of attorney form [US-FEDP51-016] |
| Wisconsin (WI) | Form A-222 Power of Attorney [US-WIP52-003] | UCT-8291-E Employer Power of Attorney Assignment [US-WIP51-002] |
| West Virginia (WV) | WV-2848 [US-WVP51-006] | WorkForce WV Power of Attorney (Rev. 3.23) [US-WVP52-006] |
| Wyoming (WY) | No State wage tax, so no withholding authorisation: none: no income tax [US-WYP51-001] | Not configured in this release (open gap SIR-RQ-37) |


## 3.4 Provider programmes and duties

| Programme or duty | Requirement | Source |
|---|---|---|
| Federal reporting agent | Pub. 1474 (Rev. 4-2026): reporting agent = accounting service, franchiser, bank, service bureau or other payroll-services entity; agent list additions/deletions electronic above 100 submissions a week via SLFT B2B; deposits via EFTPS or FTA | [US-FIL-001] |
| Federal third-party payer arrangements | Pub. 15 (2026) third-party payer arrangements (reporting agents, sec. 3504 agents, CPEOs) - liability allocation per arrangement | [US-FEDP51-002] |
| Federal agent authorisation, returns covered | Line 15: 940, 941, 943, 944, 945, 1042, CT-1; line 16 deposits; line 19 extends the authorisation to state/local returns related to lines 15/16 | [US-FED-028] |
| New York bulk web upload | Pub. 72.5 (2/25) NYS-45 Web Upload: prior approval, test file, agent identification number | [US-FIL-007] |
| Ohio bulk filing | Bulk Filing Guide Part A: IT 501, IT 941, SD 101, SD 141, FSET v4.4; ETIN | [US-FIL-012] |
| Wisconsin provider registration | Payroll service providers must register and test their software with DOR | [US-WIS5-016] |
| Maine payroll processor licence | Payroll processors must hold a Bureau of Consumer Credit Protection licence (effective 2026-01-01 to 2026-12-31) | [US-MES5-011] |
| Wyoming service supplier | The service supplier shall keep separate records, submit a list of all clients to the department on a quarterly basis and submit separate quarterly reports for each client; if the service supplier fails to pay contributions or submit required reports, the client is jointly and severally liable (W.S. 27-3-502) | [US-WYS5-019] |
| Alaska online filing by a payroll agent | Contribution reports must be filed via Internet when a wage schedule lists 50 or more employees in a quarter; $1 million or more in taxable wages in the current or preceding calendar year; or a payroll agent reports on behalf of an employer | [US-AKS5-005] |
| North Dakota withholding return | Form 306 quarterly; e-file if prior-year withholding 1,000+ or a provider e-files federally; Form 307 + W-2 EFW2 by 31 Jan | [US-NDS5-002] |
| Vermont withholding return | WHT-436 quarterly (carries CCC); WHT-434 annual by 31 Jan, e-file at 10+ and always for payroll services; no CF/SF (effective 2026-01-01 to 2026-12-31) | [US-VTS5-017] [US-VTP52-003] |
| Minnesota withholding return | Quarterly via e-Services; W-2 information due to the Minnesota Department of Revenue by January 31; with a total of more than 10 forms (W-2s plus 1099s) you must electronically submit the information using e-Services; a third-party bulk filer and each of its clients must have a valid Minnesota Tax ID Number (effective 2026-01-01 to 2026-12-31) | [US-MNS5-010] |


# 4. Technical Specifications

File layouts are those published by the authority and read for this release. Where a layout is not configured the cell says so; the provider's own import layout is recorded in the provider contract, not here.

| Layout or specification | What it fixes | Source |
|---|---|---|
| EFW2 TY2026 record layout (SSA) | SSA Publication No. 42-007, EFW2 Tax Year 2026 (page header dated 2026-09-14; no version change entries yet). 512-byte records in order RA, RE, RW, (RO), (RS), RT, (RU), (RV), RF; RA/RE/RW/RT/RF required; RO/RS/RU/RV optional; RS and RV are not read or processed by SSA or IRS (state-defined). TY2026 changes: RE adds Employer Signature PIN (319-328); RW adds Box 14b Primary/Secondary Treasury Tipped Occupation Code (490-492 / 493-495); RO/RU split Codes A and B into separate money fields (combined A+B field valid through TY2025 only), add money fields for existing Codes J, K, L, P and new Codes TA, TP, TT; SS wage base 184,500; FIRE replaced by IRIS | [US-FEDS5-032] |
| EFW2 state records (RS, RV) the provider builds | Provider must build RS per state spec on the TY2026 base layout: state employer account 248-267, state code 274-275, state wages/tax 276-297, other state data 298-307, tax type code 308 with local wages/tax 309-330, supplemental 338-487; RV 3-512 state-defined; SSA ignores RS/RV | [US-FEDS5-032] |
| W-2 and W-2c format and channel | EFW2 Publication 42-007 (W-2) / 42-014 (W-2c) via SSA Business Services Online | [US-FIL-002] |
| W-2 boxes 15 to 20 | W-2 boxes 15-20: up to two states and two localities per form; additional W-2 for more | [US-MULTIS5-011] |
| California DE 9C electronic file | DE 8300 e-file guide: Upload Bulk Return File (zip <=10 MB) XML, ICESA or MMREF-1, CSV, or FSET XML web service | [US-FIL-006] |
| Connecticut Paid Leave batch file | Batch XML (XSD) or CSV via SFTP per File Specification Toolkit v2.1.9; employer-level return totals only; acknowledgement file E/W | [US-CTB5-001] |
| Florida RT-6 flat file | Flat File Web Import v7 (Dec 2023): records 00/01/02/03/99, 2 implied decimals | [US-FLS5-022] |
| Florida RT-6 XML | Not configured in this release (open gap SIR-RQ-07) | [US-FLS5-023] [US-FLS5-022] |
| Alaska CSV layout | Header record 11 columns + wage detail record 12 columns (rev. 2016-05-17) | [US-AKS5-014] |
| Indiana W-2 file | XML IDORWTH2016V1.0 for new filers; EFW2 for existing filers (RS 306-343 county code, local wages/tax); schema not downloaded | [US-INS5-011] [US-INR3-002] |
| North Carolina TY2026 specification | TY2026 specs version 9-2026 (use beginning January 2027) | [US-NCS5-028] |
| Iowa W-2 file | IDR-unique EFW2-based ASCII 512 bytes (SSA file rejected): RS state code 19, permit 248-267, Iowa RV total; e-file by 15 Feb, W-2s with Iowa withholding only | [US-IAS5-017] [US-IAS5-018] |
| Maryland W-2 file | MW508 + W-2s by 31 Jan; modified Maryland EFW2 bulk upload; RS FEIN 328-336, CRN 338-345; RV=MW508 with NAICS | [US-MDS5-016] |
| Massachusetts W-2 file | EFW2 RA/RE/RS/RT; RT must equal sum of RS; PDF/CSV refused; 50+ W-2s electronic | [US-MAS5-019] |
| Pennsylvania UC-2 layout | Form UC-2 + UC-2A filed online via the Pennsylvania UC Management System (paper Forms UC-2 and UC-2A only under a temporary waiver); layout UC-2010 | [US-FIL-008] [US-PAS5-013] |
| Michigan UI wage report formats | MiUI quarterly (25th after quarter): CSV v3, ICESA v2, EFW2 v2, XML v1 | [US-MIS5-022] |

State W-2 editions for TY2026: Not configured in this release (open gap SIR-RQ-36)

State UI wage-file layouts: Not configured in this release (open gap SIR-RQ-35)


# 5. Error Handling: routing, rejection and correction rules

Authority error-code catalogue (reject and business-rule lists per channel class): Not configured in this release (open gap SIR-RQ-38) The rules below are the routing and rejection rules the research found, each stated by the authority that applies it.

| Rule | Statement | Source |
|---|---|---|
| California files no State W-2 | DE 9 + DE 9C quarterly, electronic only (per employee subject wages, PIT wages, PIT withheld); DE 88 deposits on the federal schedule; no annual reconciliation; W-2 NOT filed with EDD/FTB (effective 2026-01-01 to 2026-12-31) | [US-CAS5-018] |
| New York files no State W-2 | NYS-45 quarterly combined withholding + wage reporting + UI; e-file and ACH mandatory; no W-2 filed with NY | [US-NYS5-010] |
| Iowa rejects the SSA file | IDR-unique EFW2-based ASCII 512 bytes (SSA file rejected): RS state code 19, permit 248-267, Iowa RV total; e-file by 15 Feb, W-2s with Iowa withholding only | [US-IAS5-017] [US-IAS5-018] |
| Indiana new filers | XML IDORWTH2016V1.0 for new filers; EFW2 for existing filers (RS 306-343 county code, local wages/tax); schema not downloaded | [US-INS5-011] [US-INR3-002] |
| Vermont W-2 routing | WHT-436 quarterly (carries CCC); WHT-434 annual by 31 Jan, e-file at 10+ and always for payroll services; no CF/SF (effective 2026-01-01 to 2026-12-31) | [US-VTS5-017] [US-VTP52-003] |
| Kansas W-2 routing | EFW2 with Kansas RS record (K-2MT Rev. 10-25) or CSV formatted as in the KW-2CSV W-2 Specifications for Electronic Filing; Kansas does not accept withholding information submitted on magnetic media | [US-KSS5-026] [US-KSS5-001] |
| Michigan W-2 routing | Due 31 Jan; 10+ forms via MTO in EFW2 / Pub 1220; W-2s not via CF/SF | [US-MIPIT-001] |
| Nevada MBT wages and UI wages | MBT TAX-F003 quarterly on My Nevada Tax; from 2026-01-01 MBT wages compared with ESD wages | [US-NVS5-009] [US-NVS5-010] |
| Federal return correction (941-X) | Underreported: file by the due date of the return for the period in which the error was discovered and pay by filing (interest-free). Period of limitations: overreported - 3 years from the date Form 941 was filed or 2 years from payment, whichever later; underreported - 3 years from filing; Forms 941 for a year are deemed filed on April 15 of the following year. | [US-FEDS6-007] |
| Federal correction process | Adjustment process (line 1): underreported tax (pay with the 941-X), or overreported tax applied as a credit to the Form 941 for the period in which the 941-X is filed; required when correcting both under- and over-reported amounts. Claim process (line 2): overreported tax only, refund or abatement. Overreported corrections in the last 90 days of the period of limitations must use the claim process (and a separate 941-X for any underreported amounts). One 941-X per quarter corrected. | [US-FEDS6-007] |
| Full SSN on State copies, Arizona | SSNs and EINs must not be truncated | [US-AZS5-025] |
| Multistate new-hire election | Electronic multistate employers may report all new hires to one designated state after notifying HHS in writing | [US-MULTIS5-006] |


# 6. SLA and Deadlines


## 6.1 Federal and cross-cutting deadlines

| Item | Deadline or threshold | Source |
|---|---|---|
| Form 941 and 944 | Quarterly, last day of the month after the quarter; amounts in cents; 944 only on IRS written notice (liability 1,000 or less) | [US-FEDS5-004] |
| Form 940 | TY2025 rule: Form 940 for 2025 due February 2, 2026 (February 10, 2026 if all FUTA tax was deposited when due) (TY2025 rule, re-verify on the 2026 instructions) (effective 2026-01-01 to 2026-02-10) Not configured in this release (open gap SIR-RQ-03) | [US-FEDS5-031] |
| W-2 and W-3, TY2026 | 2027-02-01 to SSA and employees | [US-FEDS5-007] |
| W-2 due date conflict, Massachusetts | 31 January (W-2 page and handbook); the Withholding Tax Guide says end of March for 50+ (conflict; Jan 31 recommended) | [US-MAS5-015] |
| New hire, federal | 20 days | [US-FEDS5-024] |
| Federal deposit look-back | 2024-07-01 to 2025-06-30 for calendar 2026 | [US-FEDS5-004] |
| Monthly depositor ceiling | 50,000 | [US-FEDS5-004] |
| Next-business-day deposit | 100,000 | [US-FEDS5-004] |
| ACA forms TY2026 | TY2026: file 1094-C/1095-C with IRS by March 1, 2027 (paper) or 2027-03-31 (electronic); furnish 1095-C to employees by 2027-03-02 (automatic extension from 2027-01-31; alternative website notice possible) Per 2026 draft: read from the IRS early-release draft of the 2026 form or instructions; re-verify against the final 2026 revision before go-live. | [US-FEDS6-006] |
| Form 941-X | Underreported: file by the due date of the return for the period in which the error was discovered and pay by filing (interest-free). Period of limitations: overreported - 3 years from the date Form 941 was filed or 2 years from payment, whichever later; underreported - 3 years from filing; Forms 941 for a year are deemed filed on April 15 of the following year. | [US-FEDS6-007] |
| New Jersey UI wage report | WR-30 quarterly, electronic (online or SFTP), due the 30th with no weekend extension | [US-NJS5-017] |
| Michigan withholding reconciliation | SUW 5080 monthly/quarterly (20th); 5081 annual reconciliation 2027-02-28; accelerated EFT at 480,000+ (effective 2026-01-01 to 2026-12-31) | [US-MIS5-018] [US-MIS5-021] |


## 6.2 State deadlines

State due dates are written on the report row of section 7 that they govern. State acknowledgement and response-time rules were not read for this release: Not configured in this release (open gap SIR-RQ-39)


# 7. Per-report hand-off register

One row per report row of the Report Specifications. The hand-off requirement is the rule the research found for that authority; the status and accuracy statement is the one of the Report Matrix.


## 7.1 Federal returns, wage statements and corrections

| Report row | Authority | Channel class; portal | Hand-off requirement | Status; accuracy |
|---|---|---|---|---|
| US-IRS-001 | Internal Revenue Service (IRS) | file_upload; portal: IRS e-file through the authorised reporting agent (Form 8655) | Return and deposits: Quarterly, last day of the month after the quarter; amounts in cents; 944 only on IRS written notice (liability 1,000 or less) [US-FEDS5-004]; Deposit rule: 50,000 [US-FEDS5-004]; Next-business-day deposit: 100,000 [US-FEDS5-004]; Look-back period: 2024-07-01 to 2025-06-30 for calendar 2026 [US-FEDS5-004] | TO CONFIRM; accuracy 85. Closes with: the provider import layout and one accepted real filing. |
| US-IRS-002 | Internal Revenue Service (IRS) | file_upload; portal: IRS e-file through the authorised reporting agent (Form 8655) | Return: For 2026: file Form 944 by 2027-02-01; by February 10, 2027 if all deposits were made on time in full [US-FEDS6-003] Per 2026 draft: read from the IRS early-release draft of the 2026 form or instructions; re-verify against the final 2026 revision before go-live.; Rule: annual, only on written IRS notice, liability of 1,000 or less [US-FEDS5-004] | TO CONFIRM; accuracy 80. Closes with: the final 2026 Form 944 and its instructions, and one accepted real filing. |
| US-IRS-003 | Internal Revenue Service (IRS) | file_upload; portal: IRS e-file through the authorised reporting agent (Form 8655) | Return: For 2026: file Form 943 by 2027-02-01; by February 10, 2027 if deposits were made on time in full payment of the year's taxes [US-FEDS6-004] Per 2026 draft: read from the IRS early-release draft of the 2026 form or instructions; re-verify against the final 2026 revision before go-live. | TO CONFIRM; accuracy 80. Closes with: the final 2026 Form 943 and its instructions, and one accepted real filing. |
| US-IRS-004 | Internal Revenue Service (IRS) | file_upload; portal: IRS e-file through the authorised reporting agent (Form 8655) | Return: TY2025 rule: Form 940 for 2025 due February 2, 2026 (February 10, 2026 if all FUTA tax was deposited when due) (TY2025 rule, re-verify on the 2026 instructions) [US-FEDS5-031] (effective 2026-01-01 to 2026-02-10) Not configured in this release (open gap SIR-RQ-03) | TO CONFIRM; accuracy 80. Closes with: the final 2026 Form 940 and instructions (RSPEC-GAP-001) and the final 2026 credit-reduction list (RSPEC-RQ-08). |
| US-IRS-005 | Internal Revenue Service (IRS) | none (routing flag); portal: Not applicable | Return: 2027-04-15 (with the 2026 Form 1040/1040-SR/1040-SS/1040-NR/1041; extension of the return extends Schedule H; stand-alone if no return) [US-FEDS6-010] | CONFIRMED; accuracy 90. Closes with: one household employer's filed Schedule H checked against the statement. |
| US-IRS-006 | Internal Revenue Service (IRS) | file_upload; portal: IRS IRIS | Channel: IRIS (FIRE retired for TY2026); due 2027-03-15 [US-FEDS5-016] | CONFIRMED (channel and box codes), TO CONFIRM (code pairing for wages); accuracy 80. Closes with: one accepted real filing for a treaty-exempt employee. |
| US-IRS-007 | Internal Revenue Service (IRS) | file_upload; portal: IRS electronic filing through the reporting agent | Due date: TY2026: file 1094-C/1095-C with IRS by March 1, 2027 (paper) or 2027-03-31 (electronic); furnish 1095-C to employees by 2027-03-02 (automatic extension from 2027-01-31; alternative website notice possible) [US-FEDS6-006] Per 2026 draft: read from the IRS early-release draft of the 2026 form or instructions; re-verify against the final 2026 revision before go-live.; E-file threshold: 10 returns [US-FEDS5-012] (TY2025 rule, re-verify on the 2026 instructions) Not configured in this release (open gap SIR-RQ-02) | TO CONFIRM; accuracy 75. Closes with: the final 2026 Instructions for Forms 1094-C and 1095-C (RSPEC-GAP-002). |
| US-IRS-008 | Internal Revenue Service (IRS) | file_upload; portal: IRS e-file through the authorised reporting agent (Form 8655) | Deadlines: Underreported: file by the due date of the return for the period in which the error was discovered and pay by filing (interest-free). Period of limitations: overreported - 3 years from the date Form 941 was filed or 2 years from payment, whichever later; underreported - 3 years from filing; Forms 941 for a year are deemed filed on April 15 of the following year. [US-FEDS6-007]; Process: Adjustment process (line 1): underreported tax (pay with the 941-X), or overreported tax applied as a credit to the Form 941 for the period in which the 941-X is filed; required when correcting both under- and over-reported amounts. Claim process (line 2): overreported tax only, refund or abatement. Overreported corrections in the last 90 days of the period of limitations must use the claim process (and a separate 941-X for any underreported amounts). One 941-X per quarter corrected. [US-FEDS6-007] | TO CONFIRM; accuracy 85. Closes with: the provider import layout and one accepted real filing. |
| US-SSA-001 | Social Security Administration (SSA) | file_upload; portal: SSA Business Services Online | Format and channel: EFW2 Publication 42-007 (W-2) / 42-014 (W-2c) via SSA Business Services Online [US-FIL-002]; Due date: 2027-02-01 to SSA and employees [US-FEDS5-007]; Record layout: SSA Publication No. 42-007, EFW2 Tax Year 2026 (page header dated 2026-09-14; no version change entries yet). 512-byte records in order RA, RE, RW, (RO), (RS), RT, (RU), (RV), RF; RA/RE/RW/RT/RF required; RO/RS/RU/RV optional; RS and RV are not read or processed by SSA or IRS (state-defined). TY2026 changes: RE adds Employer Signature PIN (319-328); RW adds Box 14b Primary/Secondary Treasury Tipped Occupation Code (490-492 / 493-495); RO/RU split Codes A and B into separate money fields (combined A+B field valid through TY2025 only), add money fields for existing Codes J, K, L, P and new Codes TA, TP, TT; SS wage base 184,500; FIRE replaced by IRIS [US-FEDS5-032] | CONFIRMED (channel and RA, RE, RW, RT, RF positions), TO CONFIRM (other RO / RU positions); accuracy 90. Closes with: the RO and RU record tables (RSPEC-RQ-15) and one accepted real submission. |


## 7.2 State withholding returns and deposits

| Report row | Authority | Channel class; portal | Hand-off requirement | Status; accuracy |
|---|---|---|---|---|
| US-DOR-001-AK | Alaska Dept of Revenue Tax Division | none (no return for this jurisdiction); portal: Not applicable | Return and deposits: none: no state wage tax [US-AKWT-001] | CONFIRMED |
| US-DOR-001-AL | Alabama Department of Revenue, Withholding Tax Section | online_form; portal: not named in the cited channel sources | Return and deposits: A-6 monthly (if >1,000 withheld in month 1 or 2 of quarter, due 15th); A-1 quarterly; A-3 annual reconciliation + W-2s by 31 January; My Alabama Taxes [US-ALS5-001] | TO CONFIRM; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-DOR-001-AR | Arkansas Department of Finance and Administration | online_form; portal: not named in the cited channel sources | Return and deposits: AR941M monthly by 15th (new registrations); AR941A annual by 31 Jan if under 1,000; AR3MAR annual reconciliation 28 Feb; EFT mandatory at 20,000/month average [US-ARP51-002] | TO CONFIRM; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-DOR-001-AZ | Arizona Department of Revenue | online_form; portal: not named in the cited channel sources | Return and deposits: A1-QRT quarterly (even zero); A1-R annual reconciliation with W-2s by 31 Jan; A1-APR annual payment filers under 200; EFT at 500+ [US-AZP52-005] | CONFIRMED; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-DOR-001-CA | California EDD | online_form; portal: not named in the cited channel sources | Return and deposits: DE 9 + DE 9C quarterly, electronic only (per employee subject wages, PIT wages, PIT withheld); DE 88 deposits on the federal schedule; no annual reconciliation; W-2 NOT filed with EDD/FTB [US-CAS5-018] (effective 2026-01-01 to 2026-12-31) | CONFIRMED; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-DOR-001-CO | Colorado Department of Revenue | online_form; portal: not named in the cited channel sources | Return and deposits: Quarterly (<7,000/yr), monthly (7,000-50,000), weekly (>=50,000, EFT); zero returns required; DR 1094 paper [US-COS5-006] | TO CONFIRM; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-DOR-001-CT | Connecticut Department of Revenue Services | online_form; portal: myconneCT (named in [US-CTS5-013]) | Return and deposits: CT-941 quarterly via myconneCT even with zero; remitter class weekly/monthly/quarterly by 12-month lookback; CT-W3 + all W-2s by 31 Jan (key-and-send, EFW2 upload or DRS CSV) [US-CTS5-013] | CONFIRMED; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-DOR-001-DC | DC Office of Tax and Revenue | online_form; portal: MyTax.DC.gov | Return and deposits: FR-900Q quarterly on MyTax.DC.gov (e-file mandatory since TY2023); due Apr 30/Jul 31/Oct 31/Jan 31; zero return required [US-DCS5-014] | CONFIRMED; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-DOR-001-DE | Delaware Division of Revenue | online_form; portal: not named in the cited channel sources | Return and deposits: Quarterly / monthly / eighth-monthly by lookback period (statutory thresholds 4,500 / 25,000, subject to annual adjustment); WTH-REC Annual Reconciliation/Transmittal filed on or before the last day of January with a duplicate of each W-2 [US-DES5-005] [US-DES5-009] | TO CONFIRM; accuracy 75. Closes with: the Delaware Division of Revenue 2026 withholding filing-frequency notice (RSPEC-GAP-006). |
| US-DOR-001-FL | Florida Senate | none (no return for this jurisdiction); portal: Not applicable | Return and deposits: none: no income tax on natural persons [US-FL-001] | CONFIRMED |
| US-DOR-001-GA | Georgia Department of Revenue | online_form; portal: not named in the cited channel sources | Return and deposits: G-7 (semi-weekly / monthly / quarterly / annual by lookback); EFT and e-file mandatory once a G-7 exceeds 500 [US-GAS5-002] | CONFIRMED; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-DOR-001-HI | Hawaii Department of Taxation | online_form; portal: not named in the cited channel sources | Return and deposits: HW-14 quarterly (15th after quarter) with VP-1 deposits quarterly/monthly/semi-weekly; W-2/HW-2 to DOTAX by 31 Jan [US-HIS5-005] [US-HIP51-001] | CONFIRMED; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-DOR-001-IA | Iowa Department of Revenue | online_form; portal: GovConnectIowa (named in [US-IAS5-016]) | Return and deposits: Quarterly return via GovConnectIowa; deposits quarterly/monthly/semimonthly; no annual reconciliation (VSPs no longer filed) [US-IAS5-016] | CONFIRMED; accuracy 80. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-DOR-001-ID | Idaho State Tax Commission | online_form; portal: TAP | Return and deposits: Form 910 in TAP (semimonthly / monthly / quarterly / annual); Form 967 + W-2s last day of January [US-IDS5-009] [US-IDS5-010] | TO CONFIRM; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-DOR-001-IL | Illinois Department of Revenue | online_form; portal: MyTax | Return and deposits: IL-941 quarterly, electronic; no annual reconciliation; deposits monthly or semi-weekly (>12,000 lookback) [US-ILS5-011] | CONFIRMED; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-DOR-001-IN | Indiana Department of Revenue | online_form, file_upload; portal: INTIME | Return and deposits: WH-1 via INTIME (annual / monthly / early filer); WH-3 + W-2 by 31 Jan, electronic above 25 statements [US-INS5-010] | TO CONFIRM; accuracy 80. Closes with: the Indiana DOR XML schema package IDORWTH2016V1.0 (RSPEC-GAP-014). |
| US-DOR-001-KS | Kansas Department of Revenue | online_form; portal: not named in the cited channel sources | Return and deposits: KW-5 each period (quad-monthly, semi-monthly, monthly, quarterly or annually); the annual return KW-3, W-2s and 1099s are due by January 31 of the following year; Form KW-3 must be filed electronically [US-KSS5-007] [US-KSS5-001] | CONFIRMED; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-DOR-001-KY | Kentucky Department of Revenue | online_form; portal: MyTaxes (named in [US-KYS5-013]) | Return and deposits: MyTaxes: K-3 annual / K-1 quarterly / monthly / twice-monthly; zero returns required [US-KYS5-013] | TO CONFIRM; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-DOR-001-LA | Louisiana Department of Revenue | online_form; portal: LaTAP | Return and deposits: L-1 quarterly electronic; L-3 + W-2s by first business day after 31 Jan via LaWage [US-LAS5-003] [US-LAP51-002] | CONFIRMED; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-DOR-001-MA | Massachusetts Department of Revenue | online_form; portal: MassTaxConnect (named in [US-MAS5-013]) | Return and deposits: M-941 via MassTaxConnect: annual / quarterly / monthly / quarterly with 3-business-day accelerated payments by annual amount [US-MAS5-013] | CONFIRMED; accuracy 80. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-DOR-001-MD | Comptroller of Maryland | online_form; portal: not named in the cited channel sources | Return and deposits: MW506 on Maryland Tax Connect (accelerated / monthly / quarterly / seasonal / annual) [US-MDS5-021] | CONFIRMED; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-DOR-001-ME | Maine Revenue Services | online_form; portal: not named in the cited channel sources | Return and deposits: 941ME quarterly electronic (Rule 104); semiweekly deposits at 18,000+ lookback; no W-3ME after TY2023 [US-MEP52-002] [US-MEP52-009] | CONFIRMED; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-DOR-001-MI | Michigan Department of Treasury | online_form; portal: MTO (named in [US-MIS5-018]) | Return and deposits: SUW 5080 monthly/quarterly (20th); 5081 annual reconciliation 2027-02-28; accelerated EFT at 480,000+ [US-MIS5-018] [US-MIS5-021] (effective 2026-01-01 to 2026-12-31) | CONFIRMED; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-DOR-001-MN | Minnesota Department of Revenue | online_form; portal: e-Services (named in [US-MNS5-010]) | Return and deposits: Quarterly via e-Services; W-2 information due to the Minnesota Department of Revenue by January 31; with a total of more than 10 forms (W-2s plus 1099s) you must electronically submit the information using e-Services; a third-party bulk filer and each of its clients must have a valid Minnesota Tax ID Number [US-MNS5-010] (effective 2026-01-01 to 2026-12-31) | TO CONFIRM; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-DOR-001-MO | Missouri Department of Revenue | online_form; portal: not named in the cited channel sources | Return and deposits: MO-941 monthly / quarterly / annual; quarter-monthly payments at 9,000+ [US-MOS5-001] (effective 2026-01-01 to 2026-12-31) | CONFIRMED; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-DOR-001-MS | Mississippi Department of Revenue | paper; portal: TAP | Return and deposits: 89-105 via TAP, 15th after the period; no depository; e-file at 20,000+ liability [US-MSS5-019] | TO CONFIRM; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-DOR-001-MT | Montana Department of Revenue | online_form; portal: TAP (named in [US-MTS5-005]) | Return and deposits: Accelerated / monthly / annual deposits; MW-3 + all W-2s by 31 Jan via TAP (EFW2); truncated SSNs not accepted [US-MTS5-005] | TO CONFIRM; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-DOR-001-NC | NC Department of Revenue | online_form; portal: eNC3 (named in [US-NC-001]) | Return and deposits: NC-5: quarterly <250/month; monthly 250-<2,000 (15th); semiweekly >=2,000 (NC-5P) + NC-5Q quarterly [US-NC-001] | CONFIRMED; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-DOR-001-ND | ND Office of State Tax Commissioner | file_upload; portal: not named in the cited channel sources | Return and deposits: Form 306 quarterly; e-file if prior-year withholding 1,000+ or a provider e-files federally; Form 307 + W-2 EFW2 by 31 Jan [US-NDS5-002] | CONFIRMED; accuracy 80. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-DOR-001-NE | Nebraska Department of Revenue | online_form; portal: not named in the cited channel sources | Return and deposits: 941N quarterly; 501N/EFT monthly deposits when >500 in month 1 or 2 [US-NES5-010] (effective 2026-01-01 to 2026-12-31) | CONFIRMED; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-DOR-001-NH | NH Department of Revenue Administration | none (no return for this jurisdiction); portal: Not applicable | Return and deposits: none: no state wage tax [US-NH-006] | CONFIRMED |
| US-DOR-001-NJ | NJ Division of Taxation | online_form; portal: not named in the cited channel sources | Return and deposits: NJ-927 quarterly electronic; NJ-500 monthly; NJ-W-3 + W-2s by 15 Feb, electronic since TY2020 [US-NJP51-001] | CONFIRMED; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-DOR-001-NM | New Mexico Taxation and Revenue Department | online_form; portal: not named in the cited channel sources | Return and deposits: TRD-41414 (25th after period) and new TRD-41431 quarterly from 2026-01-01; e-file mandate from 2026 [US-NMS5-012] | TO CONFIRM; accuracy 90. Closes with: the TRD TAP bulk filing schema for TRD-41431 and the DWS UI wage file specifications (RSPEC-GAP-027). |
| US-DOR-001-NV | Nevada Legislature (Legislative Counsel Bureau) | none (no return for this jurisdiction); portal: Not applicable | Return and deposits: none: no state wage tax [US-NVP51-001] | CONFIRMED |
| US-DOR-001-NY | NY Department of Taxation and Finance / NY Department of Labor | file_upload, paper; portal: not named in the cited channel sources | Return and deposits: NYS-45 quarterly combined withholding + wage reporting + UI; e-file and ACH mandatory; no W-2 filed with NY [US-NYS5-010] | CONFIRMED; accuracy 80. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-DOR-001-OH | Ohio Department of Taxation | online_form; portal: not named in the cited channel sources | Return and deposits: IT 501 (quarterly / monthly / partial-weekly) and IT 941 by 31 Jan; W-2 upload by 31 Jan with school district code [US-OHB5-401] | CONFIRMED; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-DOR-001-OK | Oklahoma Tax Commission | online_form; portal: not named in the cited channel sources | Return and deposits: Quarterly return 20th after quarter via OkTAP; W-2 via EFW2 or entry by 31 Jan [US-OKS5-010] [US-OK-001] | TO CONFIRM; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-DOR-001-OR | Oregon Department of Revenue with OED and DCBS | online_form; portal: Frances Online | Return and deposits: Form OQ quarterly via Frances Online: withholding, UI, Paid Leave, WBF, TriMet, Lane, STT; Schedule B; Form 132 [US-ORS5-010] (effective 2026-01-01 to 2026-12-31) | CONFIRMED; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-DOR-001-PA | Pennsylvania Department of Revenue | online_form; portal: myPATH (named in [US-PAS5-010]) | Return and deposits: myPATH deposits; quarterly W-3; REV-1667 + W-2s by 31 Jan, electronic at 10+ [US-PAS5-010] [US-PAS5-009] | TO CONFIRM; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-DOR-001-RI | RI Division of Taxation | online_form; portal: Tax Portal (named in [US-RIS5-018]) | Return and deposits: Weekly/monthly/quarterly deposits; RI-941 quarterly; RI W-3 by 31 Jan; W-2 EFW2 with RS via Tax Portal [US-RIS5-018] | CONFIRMED; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-DOR-001-SC | South Carolina Department of Revenue | online_form; portal: not named in the cited channel sources | Return and deposits: WH-1605 Q1-Q3 and WH-1606 Q4 + annual reconciliation via MyDORWAY [US-SCS5-002] [US-SCR3-002] | CONFIRMED; accuracy 80. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-DOR-001-SD | South Dakota Department of Revenue | none (no return for this jurisdiction); portal: Not applicable | Return and deposits: none: no state wage tax [US-SDS5-001] | CONFIRMED |
| US-DOR-001-TN | Tennessee Department of Revenue | none (no return for this jurisdiction); portal: Not applicable | Return and deposits: False [US-TNP51-001] | CONFIRMED |
| US-DOR-001-TX | Texas Legislative Council (tcss.legis.texas.gov official statutes file server) | none (no return for this jurisdiction); portal: Not applicable | Return and deposits: none: no state income tax [US-TXS5-001] | CONFIRMED |
| US-DOR-001-UT | Utah State Tax Commission | online_form; portal: not named in the cited channel sources | Return and deposits: TC-941E e-file only, quarterly (monthly payments at 1,000+); annual reconciliation with W-2s by 31 Jan [US-UTS5-013] [US-UTS5-014] | CONFIRMED; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-DOR-001-VA | Virginia Department of Taxation (Virginia Tax) | online_form; portal: not named in the cited channel sources | Return and deposits: VA-5 quarterly/monthly, VA-15/VA-16 semi-weekly; VA-6 by 31 Jan; all electronic [US-VAS5-013] | CONFIRMED; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-DOR-001-VT | Vermont Department of Taxes | online_form; portal: not named in the cited channel sources | Return and deposits: WHT-436 quarterly (carries CCC); WHT-434 annual by 31 Jan, e-file at 10+ and always for payroll services; no CF/SF [US-VTS5-017] [US-VTP52-003] (effective 2026-01-01 to 2026-12-31) | CONFIRMED; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-DOR-001-WA | Washington Department of Revenue | none (no return for this jurisdiction); portal: Not applicable | Return and deposits: none: no income tax [US-WAS5-013] | CONFIRMED |
| US-DOR-001-WI | Wisconsin Department of Revenue | online_form; portal: not named in the cited channel sources | Return and deposits: WT-6 (DOR-assigned frequency), WT-7 by 31 Jan (TY2026 2027-02-01); electronic only [US-WIS5-011] [US-WIS5-016] | CONFIRMED; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-DOR-001-WV | West Virginia Tax Division | online_form; portal: MyTaxes (named in [US-WVS5-010]) | Return and deposits: IT-101Q quarterly, last day of month after quarter, even nil; remit by 15th; annual IT-101A <600/yr [US-WVS5-014] [US-WVS5-010] | CONFIRMED; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-DOR-001-WY | Wyoming Legislature | none (no return for this jurisdiction); portal: Not applicable | Return and deposits: none: no income tax [US-WYP51-001] | CONFIRMED |


## 7.3 State annual reconciliation and W-2 copies

| Report row | Authority | Channel class; portal | Hand-off requirement | Status; accuracy |
|---|---|---|---|---|
| US-DOR-002-AL | Alabama Department of Revenue, Withholding Tax Section | file_upload; portal: not named in the cited channel sources | State W-2 copy and annual reconciliation: EFW2 RS record only, 512 bytes; RS includes federal income tax withheld cols 298-307 [US-ALS5-006]; Threshold or due date: 10 forms [US-ALS5-006] | CONFIRMED; accuracy 90. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-DOR-002-AR | Arkansas Department of Finance and Administration | file_upload, paper; portal: ATAP | State W-2 copy and annual reconciliation: EFW2 (RA, RE, RW, RS, RT, RF, RCS required; RV not allowed) via ATAP bulk upload, due 31 Jan with ARW-3 [US-ARP51-002]; Threshold or due date: 125 employees [US-ARP51-002] | CONFIRMED; accuracy 80. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-DOR-002-AZ | Arizona Department of Revenue | file_upload, api; portal: AZTaxes; AZFSET | State W-2 copy and annual reconciliation: Electronic mandatory: EFW2 .txt via AZTaxes/AZFSET or transmitter; RS required, RV optional, state code 04; SSN/EIN not truncated [US-AZS5-025] | CONFIRMED; accuracy 90. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-DOR-002-CA | California EDD | online_form; portal: not named in the cited channel sources | State W-2 copy and annual reconciliation: DE 9 + DE 9C quarterly, electronic only (per employee subject wages, PIT wages, PIT withheld); DE 88 deposits on the federal schedule; no annual reconciliation; W-2 NOT filed with EDD/FTB [US-CAS5-018] (effective 2026-01-01 to 2026-12-31); Electronic file: DE 8300 e-file guide: Upload Bulk Return File (zip <=10 MB) XML, ICESA or MMREF-1, CSV, or FSET XML web service [US-FIL-006] | CONFIRMED; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-DOR-002-CO | Colorado Department of Revenue (CDOR), Taxation Division | online_form, file_upload; portal: Revenue Online (named in [US-COS5-006]) | State W-2 copy and annual reconciliation: electronic: Submit a Manual Withholding File, or upload an electronic file in .txt format (Submit a Withholding File Attachment); CDOR Year-End W-2 info return template held [US-COS5-006] [US-COS5-013]; Threshold or due date: Jan 31 to employees and the Colorado Department of Revenue [US-COS5-006] | CONFIRMED; accuracy 80. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-DOR-002-CT | Connecticut Department of Revenue Services | online_form, file_upload; portal: myconneCT | State W-2 copy and annual reconciliation: CT-W3 + all W-2s by Jan 31 via myconneCT: key-and-send, EFW2 upload or DRS CSV [US-CTS5-013] | CONFIRMED; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-DOR-002-DC | DC Office of Tax and Revenue | file_upload; portal: MyTax.DC.gov | State W-2 copy and annual reconciliation: EFW2/EFW2C with required RS record via MyTax.DC.gov, due 31 Jan; TY2025 edition read [US-DCS5-015]; Threshold or due date: 25 forms [US-DCS5-015] | CONFIRMED; accuracy 90. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-DOR-002-DE | Delaware Division of Revenue | online_form, file_upload, paper; portal: Delaware Taxpayer Portal | State W-2 copy and annual reconciliation: EFW2 with Delaware RS records via the Delaware Taxpayer Portal; SSN not truncated; paper only for 10 or fewer [US-DES5-008] | TO CONFIRM; accuracy 80. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-DOR-002-GA | Georgia Department of Revenue | online_form, file_upload; portal: GTC | State W-2 copy and annual reconciliation: G-1003 + W-2s by 31 Jan (TY2026: 2027-02-01) via GTC, Excel/CSV template or EFW2 + GA RS; 1099s via IRIS XML only [US-GAS5-003] | CONFIRMED; accuracy 90. Closes with: the GA DOR Federal Format specification for tax year 2026 and the G-1003 template (RSPEC-GAP-008). |
| US-DOR-002-HI | Hawaii Department of Taxation | online_form, file_upload; portal: HTO | State W-2 copy and annual reconciliation: HTO Simple File Import (maximum 1,000 employee records per submission), manual entry on HTO, SSA file upload method, or Hawaii Bulk Filing System [US-HIS5-005]; Threshold or due date: 10 forms [US-HIS5-006] | TO CONFIRM; accuracy 80. Closes with: DOTAX Publication EF-10 and the DLIR UC-B6 electronic filing specification (RSPEC-GAP-010). |
| US-DOR-002-IA | Iowa Department of Revenue | file_upload; portal: GovConnectIowa (named in [US-IAS5-017]) | State W-2 copy and annual reconciliation: IDR-unique EFW2-based ASCII 512 bytes (SSA file rejected): RS state code 19, permit 248-267, Iowa RV total; e-file by 15 Feb, W-2s with Iowa withholding only [US-IAS5-017] [US-IAS5-018]; Threshold or due date: Feb 15, only W-2s/1099s carrying Iowa withholding; must be filed electronically (GovConnectIowa) [US-IAS5-017] | CONFIRMED; accuracy 90. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-DOR-002-ID | Idaho State Tax Commission | file_upload; portal: TAP | State W-2 copy and annual reconciliation: EFW2 plus Idaho state records uploaded in TAP (spec on STC developers page, not read) [US-IDS5-010] | TO CONFIRM; accuracy 90. Closes with: the Idaho STC W-2 electronic filing specification (RSPEC-GAP-012). |
| US-DOR-002-IL | Illinois Department of Revenue | online_form, file_upload; portal: MyTax | State W-2 copy and annual reconciliation: Electronic only: MyTax (entry, CSV, EFW2 under IDR-996) or bulk EFW2 with ETIN (IDR-986); 2026 W-2s by 2027-02-01; 1099 bulk via IRIS from 2026-09-18 [US-ILS5-013] | CONFIRMED; accuracy 80. Closes with: IDOR IDR-986 (Illinois W-2 electronic filing specification) (RSPEC-GAP-013). |
| US-DOR-002-IN | Indiana Department of Revenue | file_upload; portal: INTIME (named in [US-INS5-010]) | State W-2 copy and annual reconciliation: XML IDORWTH2016V1.0 for new filers; EFW2 for existing filers (RS 306-343 county code, local wages/tax); schema not downloaded [US-INS5-011] [US-INR3-002]; Threshold or due date: 25 statements [US-INS5-011] | TO CONFIRM; accuracy 80. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-DOR-002-KS | Kansas Department of Revenue | file_upload; portal: not named in the cited channel sources | State W-2 copy and annual reconciliation: EFW2 with Kansas RS record (K-2MT Rev. 10-25) or CSV formatted as in the KW-2CSV W-2 Specifications for Electronic Filing; Kansas does not accept withholding information submitted on magnetic media [US-KSS5-026] [US-KSS5-001]; Threshold or due date: 51 forms [US-KSS5-026] | TO CONFIRM; accuracy 80. Closes with: KDOR K-2MT for tax year 2026 (RSPEC-GAP-015). |
| US-DOR-002-KY | Kentucky Department of Revenue | file_upload, paper; portal: MyTaxes | State W-2 copy and annual reconciliation: SSA EFW2 with DOR-defined RS or K-5; electronic at 26+ statements; paper W-2s not processed [US-KYS5-013]; Threshold or due date: 26 statements [US-KYS5-013] | TO CONFIRM; accuracy 90. Closes with: the KY DOR W-2 electronic filing specification and the KUIP ICESA / CSV wage file specification (RSPEC-GAP-016). |
| US-DOR-002-LA | Louisiana Department of Revenue | online_form; portal: LaWage (named in [US-LAS5-003]) | State W-2 copy and annual reconciliation: L-3 + W-2s on or before first business day after Jan 31; within 30 days on closure [US-LAS5-003] [US-LAS5-008]; Threshold or due date: 50 forms [US-LAS5-009] | CONFIRMED; accuracy 75. Closes with: the LDR LaWage file specification and the LWC online-services wage file specification (RSPEC-GAP-017). |
| US-DOR-002-MA | Massachusetts Department of Revenue | file_upload; portal: MassTaxConnect (named in [US-MAS5-015]) | State W-2 copy and annual reconciliation: EFW2 RA/RE/RS/RT; RT must equal sum of RS; PDF/CSV refused; 50+ W-2s electronic [US-MAS5-019]; Threshold or due date: 31 January (W-2 page and handbook); the Withholding Tax Guide says end of March for 50+ (conflict; Jan 31 recommended) [US-MAS5-015] | CONFIRMED; accuracy 90. Closes with: the current MA DOR W-2 electronic filing handbook and the DOR guidance on the deadline (RSPEC-GAP-018). |
| US-DOR-002-MD | Comptroller of Maryland | file_upload; portal: not named in the cited channel sources | State W-2 copy and annual reconciliation: MW508 + W-2s by 31 Jan; modified Maryland EFW2 bulk upload; RS FEIN 328-336, CRN 338-345; RV=MW508 with NAICS [US-MDS5-016]; Threshold or due date: 25 forms [US-MDS5-016] | TO CONFIRM; accuracy 90. Closes with: the Comptroller of Maryland tax-year 2026 W-2 / 1099 electronic filing specification (RSPEC-GAP-020). |
| US-DOR-002-ME | Maine Revenue Services | online_form; portal: Tax Portal (named in [US-MES5-011]) | State W-2 copy and annual reconciliation: Electronic to MRS by 31 Jan, paper not accepted; Maine Tax Portal bulk spec not read [US-MES5-011] (effective 2026-01-01 to 2026-12-31); Threshold or due date: electronically with MRS by Jan 31; paper not accepted [US-MES5-011] (effective 2026-01-01 to 2026-12-31) | CONFIRMED; accuracy 75. Closes with: the MRS Maine Tax Portal Bulk File Upload Specifications (RSPEC-GAP-021). |
| US-DOR-002-MI | Michigan Department of Treasury | file_upload; portal: MTO | State W-2 copy and annual reconciliation: Due 31 Jan; 10+ forms via MTO in EFW2 / Pub 1220; W-2s not via CF/SF [US-MIPIT-001] | CONFIRMED; accuracy 80. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-DOR-002-MN | Minnesota Department of Revenue | online_form; portal: e-Services (named in [US-MNS5-010]) | State W-2 copy and annual reconciliation: Quarterly via e-Services; W-2 information due to the Minnesota Department of Revenue by January 31; with a total of more than 10 forms (W-2s plus 1099s) you must electronically submit the information using e-Services; a third-party bulk filer and each of its clients must have a valid Minnesota Tax ID Number [US-MNS5-010] (effective 2026-01-01 to 2026-12-31); Threshold or due date: W-2 information to the Minnesota Department of Revenue by Jan 31; e-Services mandatory above 10 W-2 + 1099 [US-MNS5-010] (effective 2026-01-01 to 2026-12-31) | TO CONFIRM; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-DOR-002-MO | Missouri Department of Revenue | online_form; portal: not named in the cited channel sources | State W-2 copy and annual reconciliation: MO-941 monthly / quarterly / annual; quarter-monthly payments at 9,000+ [US-MOS5-001] (effective 2026-01-01 to 2026-12-31); Threshold or due date: 250 forms [US-MOS5-001] (effective 2026-01-01 to 2026-12-31) | TO CONFIRM; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-DOR-002-MS | Mississippi Department of Revenue | file_upload; portal: TAP | State W-2 copy and annual reconciliation: EFW2 RS (state code 28) via TAP; electronic at 10+ W-2s or when one payroll provider all year; Pub 89-145 Rev 10/25 [US-MSS5-005]; Threshold or due date: 10 [US-MSS5-005] | CONFIRMED; accuracy 90. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-DOR-002-MT | Montana Department of Revenue | online_form, file_upload; portal: TAP | State W-2 copy and annual reconciliation: MW-3 + all W-2s due Jan 31; federal W-3 not accepted; no truncated SSNs [US-MTS5-005] | CONFIRMED; accuracy 90. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-DOR-002-NC | NC Department of Revenue | file_upload; portal: eNC3 | State W-2 copy and annual reconciliation: TY2026 specs version 9-2026 (use beginning January 2027) [US-NCS5-028] | CONFIRMED; accuracy 90. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-DOR-002-ND | ND Office of State Tax Commissioner | file_upload; portal: not named in the cited channel sources | State W-2 copy and annual reconciliation: Form 307 + W-2 due Jan 31; e-file of 307 required even with zero W-2s [US-NDS5-002] | CONFIRMED; accuracy 80. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-DOR-002-NE | Nebraska Department of Revenue | file_upload; portal: NebFile | State W-2 copy and annual reconciliation: W-3N + W-2 by 31 Jan; >50 forms via NebFile; EFW2 with NE RS (state code 31) and RV [US-NES5-017]; Threshold or due date: 50 [US-NES5-017] | CONFIRMED; accuracy 90. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-DOR-002-NJ | NJ Division of Taxation | online_form, file_upload; portal: not named in the cited channel sources | State W-2 copy and annual reconciliation: NJ-W-3 by Feb 15 (or 30 days after wages stop); W-2 electronic since TY2020 (online, upload, Axway 100+) [US-NJP51-001] | CONFIRMED; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-DOR-002-NM | New Mexico Taxation and Revenue Department | online_form; portal: TAP (named in [US-NMP52-005]) | State W-2 copy and annual reconciliation: TRD-41414 (25th after period) and new TRD-41431 quarterly from 2026-01-01; e-file mandate from 2026 [US-NMS5-012]; Threshold or due date: TRD-41414, TRD-41431, TRD-41409 e-file and e-pay from 2026 [US-NMS5-012] | TO CONFIRM; accuracy 75. Closes with: the TRD TAP bulk filing schema for TRD-41431 and the DWS UI wage file specifications (RSPEC-GAP-027). |
| US-DOR-002-NY | NY Department of Taxation and Finance / NY Department of Labor | online_form; portal: not named in the cited channel sources | State W-2 copy and annual reconciliation: NYS-45 quarterly combined withholding + wage reporting + UI; e-file and ACH mandatory; no W-2 filed with NY [US-NYS5-010] | CONFIRMED; accuracy 75. Closes with: the current NYS-45-I instructions (RSPEC-GAP-029). |
| US-DOR-002-OH | Ohio Department of Taxation | file_upload, paper; portal: OH\|TAX | State W-2 copy and annual reconciliation: IT 941 by Jan 31; W-2/1099 upload (OH\|TAX Upload Income Statement) by Jan 31; CD eliminated [US-OHB5-401] | CONFIRMED; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-DOR-002-OK | Oklahoma Tax Commission | online_form, file_upload, paper; portal: OkTAP | State W-2 copy and annual reconciliation: EFW2 upload (SSA 42-007) or manual entry via OkTAP by Jan 31; no magnetic media/paper [US-OK-001] | CONFIRMED; accuracy 90. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-DOR-002-OR | Oregon Department of Revenue with OED and DCBS | file_upload; portal: iWire | State W-2 copy and annual reconciliation: OR-WR + W-2s via iWire (EFW2 or template) by 31 Jan [US-ORS5-010] (effective 2026-01-01 to 2026-12-31) | CONFIRMED; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-DOR-002-PA | Pennsylvania Department of Revenue | online_form, paper; portal: myPATH | State W-2 copy and annual reconciliation: REV-1667 Annual Withholding Reconciliation with W-2s; electronic through myPATH when filing 10 or more income statements; paper or myPATH below 10 [US-PAS5-009] | CONFIRMED; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-DOR-002-RI | RI Division of Taxation | online_form, file_upload; portal: Tax Portal | State W-2 copy and annual reconciliation: RI W-3 due Jan 31 [US-RIS5-018]; Threshold or due date: 25 employees [US-RIS5-018] (effective 2026-01-01 to 2026-12-31) | CONFIRMED; accuracy 80. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-DOR-002-SC | South Carolina Department of Revenue | online_form, file_upload; portal: not named in the cited channel sources | State W-2 copy and annual reconciliation: EFW2 .txt (SSA Publication 42-007) with the SCDOR state record per RS-1 (full SSN), or Excel template (up to 30 employees), or manual entry [US-SCS5-016]; Threshold or due date: 10 forms [US-SCS5-016] | TO CONFIRM; accuracy 80. Closes with: SCDOR RS-1 for tax year 2026 (RSPEC-GAP-035). |
| US-DOR-002-UT | Utah State Tax Commission | file_upload; portal: not named in the cited channel sources | State W-2 copy and annual reconciliation: EFW2 with RS required, RV optional; lowercase .txt; fixed-length mandatory at 250+ [US-UTS5-014]; Threshold or due date: with Q4/annual return Jan 31, electronic with all W-2s and 1099s, even with zero activity [US-UTR3-001] | CONFIRMED; accuracy 80. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-DOR-002-VA | Virginia Department of Taxation (Virginia Tax) | online_form, file_upload; portal: not named in the cited channel sources | State W-2 copy and annual reconciliation: Web Upload EFW2 / Pub 1220 (state code 51) by 31 Jan; upload does not create VA-6 [US-VAS5-009] [US-VAP51-001] | CONFIRMED; accuracy 90. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-DOR-002-VT | Vermont Department of Taxes | online_form, file_upload; portal: myVTax | State W-2 copy and annual reconciliation: WHT-434 by Jan 31, transmittal for W-2/1099; e-file at 10+ forms and always for payroll services; no CF/SF [US-VTS5-017] (effective 2026-01-01 to 2026-12-31) | TO CONFIRM; accuracy 90. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-DOR-002-WI | Wisconsin Department of Revenue | file_upload; portal: My Tax Account | State W-2 copy and annual reconciliation: EFW2 with RS (state code 55); 10+ electronic; no transmittal [US-WIS5-012]; Threshold or due date: 10 [US-WIS5-012] | CONFIRMED; accuracy 90. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-DOR-002-WV | West Virginia Tax Division | file_upload; portal: MyTaxes | State W-2 copy and annual reconciliation: IT-103 + state W-2 by Jan 31 via MyTaxes (Letter of Intent) [US-WVS5-010]; Threshold or due date: 10 employees [US-WVS5-010] | CONFIRMED; accuracy 90. Closes with: the WV Tax Division IT-105 (2026) and the current 11-21-74 text (RSPEC-GAP-039). |


## 7.4 State UI quarterly wage reports

| Report row | Authority | Channel class; portal | Hand-off requirement | Status; accuracy |
|---|---|---|---|---|
| US-UI-001-AK | Alaska DOLWD Employment Security Tax | file_upload; portal: not named in the cited channel sources | Quarterly wage report: TQ01C (2/26) with wage schedule [US-AKS5-013]; Format or mandate: Header record 11 columns + wage detail record 12 columns (rev. 2016-05-17) [US-AKS5-014] | CONFIRMED; accuracy 90. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-UI-001-AL | Alabama Department of Workforce, Unemployment Compensation | online_form, file_upload, paper; portal: eGov | Quarterly wage report: Quarterly Contribution and Wage Report via eGov (online_form or file_upload); computer-generated paper not accepted; corrections UC-10C [US-ALS5-007] | CONFIRMED; accuracy 80. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-UI-001-AR | Arkansas Division of Workforce Services / Division of Reemployment | paper; portal: Tax21 | Quarterly wage report: DWS-ARK-209B / 209BR / 209BS via Tax21 or paper [US-ARP9V-001] | TO CONFIRM; accuracy 75. Closes with: the Arkansas DWS Tax21 e-file rule or the employer handbook page stating the threshold (RSPEC-GAP-041). |
| US-UI-001-AZ | Arizona Department of Economic Security | online_form, file_upload; portal: DES Tax and Wage System | Quarterly wage report: UC-018 quarterly via DES Tax and Wage System (online) or bulk file; due last day of month after quarter; zero report required [US-AZB5-005] | CONFIRMED; accuracy 75. Closes with: A.A.C. R6-3-1705 or the DES employer handbook on electronic filing (RSPEC-GAP-043). |
| US-UI-001-CA | California EDD | online_form, file_upload, api; portal: e-Services for Business | Quarterly wage report: DE 9 + DE 9C (per employee subject wages, PIT wages, PIT withheld); corrections DE 9ADJ [US-CAS5-002] (effective 2026-01-01 to 2026-12-31); Format or mandate: DE 9C electronic options (DE 8300 Rev. 12 (7-24)): e-Services for Business direct entry or CSV import; Upload Bulk Return File (zip, max 10 MB) in XML, ICESA or MMREF-1; FSET bulk transmission (XML web service). CSV fields: SSN, first name, MI, last name, total subject wages, PIT wages, PIT withheld, wage plan code (A, J, L, P, R, S, U). Third-party representative needs its own e-Services login; no test environment for bulk formats; penalty 20 USD per wage item not filed electronically [US-FIL-006] | CONFIRMED; accuracy 90. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-UI-001-CO | State authority (not named in the cited sources) | not configured; portal: not configured | Quarterly wage report: Not configured in this release (open gap SIR-RQ-31) | TO CONFIRM; accuracy 50. Closes with: the CDLE MyUI Employer+ wage report file specification and due-date page (RSPEC-GAP-003). |
| US-UI-001-CT | Connecticut Department of Labor | online_form, file_upload, api; portal: ReEmployCT | Quarterly wage report: Quarterly via ReEmployCT (entry, upload, TPA, FSET); 276-character fixed-length S/T records; optional occupation, hours, worksite ZIP from Q3 2026 [US-CTS5-032] [US-CTP10-001]; Format or mandate: 276-character fixed-length .txt; S record per employee (start/length: SSN 2/9, last name 11/20, first name 31/12, middle initial 43/1, state code 44/2 = 09, quarter and year 46/6, total wages 64/14, taxing entity code 143/4 = WAGE, employer account number 147/10); T record per employer [US-CTS5-032] | CONFIRMED; accuracy 90. Closes with: the CT DOL ReEmployCT file format edition that carries the Q3 2026 fields (RSPEC-GAP-005). |
| US-UI-001-DC | DC Department of Employment Services (DOES) | online_form; portal: not named in the cited channel sources | Quarterly wage report: UC-30 quarterly via DOES ESSP; machine-readable mandatory at 250+ employees; PFL same channel [US-DCS5-018] [US-DCS5-026] [US-DCS5-016] | CONFIRMED; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-UI-001-DE | Delaware Department of Labor | online_form; portal: not named in the cited channel sources | Quarterly wage report: UC-8 tax report + UC-8A wage report, quarterly, Online Employer Services Portal [US-DES5-011] | TO CONFIRM; accuracy 75. Closes with: the Delaware DUI employer portal wage file specification (RSPEC-GAP-007). |
| US-UI-001-FL | Florida Department of Revenue | online_form, file_upload; portal: not named in the cited channel sources | Quarterly wage report: RT-6 quarterly; e-file and e-pay mandatory at 10+ employees in any quarter of the prior state fiscal year [US-FLS5-006] [US-FL-005]; Format or mandate: Flat File Web Import v7 (Dec 2023): records 00/01/02/03/99, 2 implied decimals [US-FLS5-022] | CONFIRMED; accuracy 90. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-UI-001-GA | Georgia Department of Labor | online_form; portal: not named in the cited channel sources | Quarterly wage report: DOL-4N quarterly; electronic required at 25+ employees; portal entry, CSV/Excel (100-15,000), SFTP (>15,000 and payroll service providers) [US-GAS5-005] | TO CONFIRM; accuracy 75. Closes with: the adopted GDOL rule 300-2-2-.02(6) with its effective date (RSPEC-GAP-009). |
| US-UI-001-HI | Hawaii DLIR Unemployment Insurance Division | online_form; portal: not named in the cited channel sources | Quarterly wage report: UC-B6 quarterly, last day of month after quarter; bulk spec not located [US-HIS5-012] | TO CONFIRM; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-UI-001-IA | Iowa Workforce Development | online_form; portal: not named in the cited channel sources | Quarterly wage report: Contribution and Payroll Report 65-5300 + wage detail by SSN, electronic [US-IAS5-024] | CONFIRMED; accuracy 75. Closes with: the IWD myIowaUI wage file specification and the IDR W-2 file specification for tax year 2026 (RSPEC-GAP-011). |
| US-UI-001-ID | Idaho Department of Labor | online_form; portal: not named in the cited channel sources | Quarterly wage report: TX20 + TX26 quarterly, Employer Portal mandatory [US-IDS5-021] | TO CONFIRM; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-UI-001-IL | Illinois Department of Employment Security | file_upload; portal: MyTax | Quarterly wage report: UI-3/40 quarterly + monthly wage report for 25+ employees (months 1-2, MyTax CSV) [US-ILS5-017] [US-ILP52-010] | CONFIRMED; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-UI-001-IN | Indiana Department of Workforce Development | online_form, file_upload; portal: DWD E S S; UPLINK | Quarterly wage report: Quarterly via E S S/UPLINK; file upload (CSV or Indiana ICESA) required above 50; SOC code and start date per worker [US-INS5-014] | CONFIRMED; accuracy 80. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-UI-001-KS | Kansas Department of Labor | online_form, file_upload, paper; portal: not named in the cited channel sources | Quarterly wage report: Quarterly wage report and contribution return; MMREF/NASWA upload; e-file at 25+ employees (stricter reading of a self-contradicting page) [US-KSS5-022]; Format or mandate: MMREF / NASWA upload; K-CNS-100 by mail for 25 or fewer employees (26 or more must file online) [US-KSS5-022] | CONFIRMED; accuracy 80. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-UI-001-KY | Kentucky Office of Unemployment Insurance | online_form, file_upload; portal: KUIP | Quarterly wage report: Quarterly in KUIP (replaced KEWES 2026) [US-KYS5-019]; Format or mandate: KUIP quarterly wage report methods: zero payroll report, file upload in ICESA or CSV format, manual entry, copy-and-modify a prior quarter; KUIP computes the tax [US-KYS6-001] | TO CONFIRM; accuracy 90. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-UI-001-LA | Louisiana Workforce Commission | online_form; portal: not named in the cited channel sources | Quarterly wage report: last day of month after quarter; domestic annual Jan 31; mandatory electronic (LWC online services) [US-LAS5-007] | TO CONFIRM; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-UI-001-MA | Massachusetts Department of Unemployment Assistance (EOLWD) | file_upload; portal: not named in the cited channel sources | Quarterly wage report: DUA quarterly wage detail by 3 p.m. on due date; CSV, EFW2 or ICESA; includes hours and state income tax withheld [US-MAS5-018]; Format or mandate: CSV, EFW2 or ICESA upload (DUA) [US-MAS5-018] | CONFIRMED; accuracy 80. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-UI-001-MD | Maryland Department of Labor, Division of Unemployment Insurance | online_form, file_upload, xml; portal: BEACON | Quarterly wage report: BEACON quarterly: online, CSV, XML, ICESA or EFW2 (spec 2026-04-20) [US-MDS5-017] | CONFIRMED; accuracy 90. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-UI-001-ME | Maine Department of Labor, Bureau of Unemployment Compensation | online_form; portal: ReEmployME | Quarterly wage report: ME UC-1 quarterly via ReEmployME; monthly employment for the 12th, gross/excess/taxable wages, UC rate, CSSF, UPAF; filed with the Maine Department of Labor [US-MES5-021] (effective 2026-01-01 to 2026-12-31) | CONFIRMED; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-UI-001-MI | Michigan LEO - Unemployment Insurance Agency | file_upload, xml; portal: MiUI | Quarterly wage report: MiUI quarterly (25th after quarter): CSV v3, ICESA v2, EFW2 v2, XML v1 [US-MIS5-022]; Format or mandate: MiUI four formats: Delimited CSV (2026 spec v3, 2026-04-08), ICESA (v2), EFW2 (v2 2026-04-03, RE/RS 512-byte UIA profile), XML (v1 2026-02-23); MiWAM legacy refused [US-MIS5-022] | CONFIRMED; accuracy 90. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-UI-001-MN | Minnesota Department of Employment and Economic Development | online_form; portal: not named in the cited channel sources | Quarterly wage report: Quarterly wage detail electronic incl. paid hours (268.044) [US-MNS5-015] | TO CONFIRM; accuracy 75. Closes with: the UIMN data submission methods and file formats page and MN DOR Fact Sheets 2 and 2a (RSPEC-GAP-023). |
| US-UI-001-MO | Missouri Department of Labor and Industrial Relations, Division of Employment Security | file_upload; portal: UInteract | Quarterly wage report: MODES-4 quarterly on UInteract (NASWA/ICESA); electronic at 50+ employees who e-file W-2 with SSA; spec M-INF-368 [US-MOS5-013] | TO CONFIRM; accuracy 90. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-UI-001-MS | Mississippi Department of Employment Security | file_upload; portal: not named in the cited channel sources | Quarterly wage report: UI-2 + UI-3 quarterly; ICESA S record (275) [US-MSS5-013] [US-MSS5-014]; Format or mandate: ICESA S record 275 chars (UIWAGE.TXT) or MMREF-1 "RS" record (now SSA EFW2) with required positions 1-2, 3-4, 10-18, 19-68, 197-202, 203-213, 248-267 [US-MSS5-013] [US-FEDS5-032] | CONFIRMED; accuracy 90. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-UI-001-MT | Montana Department of Labor and Industry, Unemployment Insurance Division | online_form; portal: UI eServices (named in [US-MTS5-025]) | Quarterly wage report: Quarterly via UI eServices; electronic mandatory from 2025-07-01 (ARM 24.40.1609) [US-MTS5-025] | TO CONFIRM; accuracy 75. Closes with: the Montana UI Contributions E-Filing Handbook (RSPEC-GAP-024). |
| US-UI-001-NC | NC Division of Employment Security (NC Department of Commerce) | online_form; portal: NCSUITS | Quarterly wage report: Quarterly Tax and Wage Report filed online in NCSUITS, Apr 30 / Jul 31 / Oct 31 / Jan 31; online filing required at ten or more employee wage items; Zero report when no wages and business continues [US-NCS5-025] | CONFIRMED; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-UI-001-ND | Job Service North Dakota | file_upload; portal: UI EASY | Quarterly wage report: Quarterly via UI EASY or Secure FTP [US-NDS5-011] | CONFIRMED; accuracy 80. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-UI-001-NE | Nebraska Department of Labor | file_upload; portal: NEworks | Quarterly wage report: Combined Tax Report + Wage Report quarterly via NEworks online or FTP [US-NES5-011] | TO CONFIRM; accuracy 75. Closes with: the NDOL UI wage report file specification (RSPEC-GAP-025). |
| US-UI-001-NH | New Hampshire Employment Security (NHES) | online_form; portal: WebTax | Quarterly wage report: Quarterly Employer Tax and Wage Report via WebTax/NHUIS (2016 handbook figures) [US-NHS5-013] | TO CONFIRM; accuracy 75. Closes with: the current New Hampshire Code of Administrative Rules Emp 300 (RSPEC-GAP-026). |
| US-UI-001-NJ | NJ Department of Labor and Workforce Development, Division of Employer Accounts | online_form; portal: not named in the cited channel sources | Quarterly wage report: WR-30 quarterly, electronic (online or SFTP), due the 30th with no weekend extension [US-NJS5-017] | TO CONFIRM; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-UI-001-NM | New Mexico Department of Workforce Solutions, UI Tax | file_upload; portal: not named in the cited channel sources | Quarterly wage report: Quarterly electronic only; Delimited, ICESA, XML, EFW2 published [US-NMS5-016] [US-NMP51-001]; Format or mandate: Delimited, ICESA, XML, EFW2; electronic only; last day of month after quarter [US-NMS5-008] [US-NMS5-016] | TO CONFIRM; accuracy 90. Closes with: the TRD TAP bulk filing schema for TRD-41431 and the DWS UI wage file specifications (RSPEC-GAP-027). |
| US-UI-001-NV | Nevada DETR Employment Security Division | online_form, file_upload; portal: ESS | Quarterly wage report: RPT3795 + NEW0098 quarterly in ESS (entry, SFTP EFW2, CSV/tab) [US-NVS5-008] | TO CONFIRM; accuracy 90. Closes with: the current DETR ESD employer handbook naming the form (RSPEC-GAP-028). |
| US-UI-001-NY | NY Department of Taxation and Finance / NY Department of Labor | file_upload, paper; portal: not named in the cited channel sources | Quarterly wage report: NYS-45 quarterly combined withholding + wage reporting + UI; e-file and ACH mandatory; no W-2 filed with NY [US-NYS5-010] | CONFIRMED; accuracy 80. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-UI-001-OH | Ohio Department of Job and Family Services (ODJFS) | online_form; portal: not named in the cited channel sources | Quarterly wage report: Not configured in this release (open gap SIR-RQ-31) | TO CONFIRM; accuracy 75. Closes with: the ODJFS Employer Resource Information Center wage file specification (RSPEC-GAP-030). |
| US-UI-001-OK | Oklahoma Employment Security Commission | online_form, file_upload; portal: EZ Tax Express | Quarterly wage report: OES-3 via EZ Tax Express; ICESA 275 E/S/T [US-OKS5-020] [US-OKS5-030]; Format or mandate: ICESA fixed 275-character ASCII CR/LF; E, S, T required, P optional (only when more than one OK UI account is used, typically by third-party administrators); S: name as on SS card in upper case, SSN, total and taxable wages [US-OKS5-020] | CONFIRMED; accuracy 90. Closes with: OAC 240:10-5 (OESC Employer Contributions rules) or the OESC employer handbook (RSPEC-GAP-031). |
| US-UI-001-OR | Oregon Department of Revenue with OED and DCBS | online_form; portal: Frances Online | Quarterly wage report: Form OQ quarterly via Frances Online: withholding, UI, Paid Leave, WBF, TriMet, Lane, STT; Schedule B; Form 132 [US-ORS5-010] (effective 2026-01-01 to 2026-12-31) | CONFIRMED; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-UI-001-PA | Pennsylvania Department of Labor and Industry, Office of UC Tax Services | online_form, file_upload; portal: not named in the cited channel sources | Quarterly wage report: Form UC-2 + UC-2A filed online via the Pennsylvania UC Management System (paper Forms UC-2 and UC-2A only under a temporary waiver); layout UC-2010 [US-FIL-008] [US-PAS5-013]; Format or mandate: UC-2010 ICESA/CSV [US-FIL-008] | CONFIRMED; accuracy 90. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-UI-001-RI | RI Department of Labor and Training, Employer Tax Unit | online_form; portal: not named in the cited channel sources | Quarterly wage report: TX-17 Quarterly Tax and Wage Report (Employment Security, TDI, Job Development fund), one report and payment; Jan 31 / Apr 30 / Jul 31 / Oct 31; zero report required [US-RIS5-017]; Format or mandate: 25 employees [US-RIS5-017] | CONFIRMED; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-UI-001-SC | South Carolina Department of Employment and Workforce | online_form, file_upload, xml; portal: SUITS | Quarterly wage report: Quarterly via SUITS: ICESA, EFW2, XML or CSV (spec v1.6) [US-SCS5-006] | CONFIRMED; accuracy 90. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-UI-001-SD | South Dakota Department of Labor and Regulation | paper; portal: not named in the cited channel sources | Quarterly wage report: Form 21 quarterly RA wage report, received by Apr 30 / Jul 31 / Oct 31 / Jan 31; zero reports required; corrections 21C [US-SDS5-013]; Format or mandate: CD/DVD 85-byte E and S records; S: social security no., names, total and taxable wages (2 implied decimals), state code 46, DLR account [US-SDS5-014] | CONFIRMED; accuracy 90. Closes with: the SD DLR Reemployment Assistance wage upload specification (RSPEC-GAP-036). |
| US-UI-001-TN | Tennessee Department of Labor and Workforce Development | online_form, file_upload; portal: Employer e-Services | Quarterly wage report: LB-0851 + LB-0456 quarterly in Employer e-Services (ICESA variants, 58-char text) [US-TNS5-005] [US-TNS5-007] | TO CONFIRM; accuracy 80. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-UI-001-TX | Texas Workforce Commission | file_upload; portal: Unemployment Tax Services; QuickFile | Quarterly wage report: Electronic only: Unemployment Tax Services or QuickFile (ICESA, MMREF-1, delimited) [US-TXSUI-006] | CONFIRMED; accuracy 80. Closes with: the adopted 40 TAC 815.107 amendment and the TWC layout implementing Labor Code 204.0025 (RSPEC-GAP-037). |
| US-UI-001-UT | Utah Department of Workforce Services | online_form; portal: not named in the cited channel sources | Quarterly wage report: Quarterly Wage List and Contribution Report online only [US-UTS5-004] | TO CONFIRM; accuracy 75. Closes with: the Utah DWS wage file upload specification (RSPEC-GAP-038). |
| US-UI-001-VA | Virginia Employment Commission (VEC) | online_form, file_upload; portal: ESS | Quarterly wage report: VEC quarterly via ESS, eForm or Web Upload (Excel, MMREF/EFW2, ICESA, delimited) [US-VAS5-014] | TO CONFIRM; accuracy 90. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-UI-001-VT | Vermont Department of Labor | online_form; portal: Employer e-Services (named in [US-VTS5-009]) | Quarterly wage report: Quarterly via Employer e-Services; hourly workers also gender and hourly wage [US-VTS5-007] | TO CONFIRM; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-UI-001-WA | Washington Employment Security Department | online_form; portal: EAMS (named in [US-WAS5-013]); SAW (named in [US-WAS5-013]) | Quarterly wage report: ESD quarterly via EAMS/SAW: name, SSN, gross, hours, SOC code [US-WAS5-013] | TO CONFIRM; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-UI-001-WI | Wisconsin DWD Unemployment Insurance Division | online_form; portal: not named in the cited channel sources | Quarterly wage report: Quarterly; electronic at 25+ employees (108.205(2)) [US-WIS5-013]; Format or mandate: 25 employees [US-WIS5-014] | TO CONFIRM; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-UI-001-WV | WorkForce West Virginia | online_form; portal: not named in the cited channel sources | Quarterly wage report: Quarterly via UC Employer System; SOC/job title, county [US-WVUI-001] | TO CONFIRM; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-UI-001-WY | Wyoming Department of Workforce Services | online_form; portal: not named in the cited channel sources | Quarterly wage report: WYUI quarterly (Apr 30 / Jul 31 / Oct 31 / Jan 31); file spec not read [US-WYS5-009] | TO CONFIRM; accuracy 75. Closes with: the WY DWS WYUI wage file specification (RSPEC-GAP-040). |


## 7.5 State new-hire reports

| Report row | Authority | Channel class; portal | Hand-off requirement | Status; accuracy |
|---|---|---|---|---|
| US-SDNH-001-AK | Alaska Department of Revenue, Child Support Enforcement Division (formerly CSSD) | online_form; portal: not named in the cited channel sources | New-hire report: 20 days [US-AKS5-007] | TO CONFIRM; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-SDNH-001-AL | Alabama Department of Workforce, New-Hire Unit | online_form; portal: not named in the cited channel sources | New-hire report: 7 days [US-ALS5-008] | TO CONFIRM; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-SDNH-001-AR | Arkansas Division of Workforce Services / Division of Reemployment | online_form; portal: not named in the cited channel sources | New-hire report: 20 days [US-ARP9V-001] | TO CONFIRM; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-SDNH-001-AZ | State authority (not named in the cited sources; legal basis published by Arizona State... | online_form; portal: not named in the cited channel sources | New-hire report: 20 days [US-AZS5-012] | TO CONFIRM; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-SDNH-001-CA | California EDD | online_form; portal: not named in the cited channel sources | New-hire report: 20 days [US-CAS5-002] (effective 2026-01-01 to 2026-12-31) | CONFIRMED; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-SDNH-001-CO | State authority (not named in the cited sources) | not configured; portal: not configured | New-hire report: Not configured in this release (open gap SIR-RQ-30) | TO CONFIRM; accuracy 50. Closes with: the Colorado State Directory of New Hires employer page or C.R.S. 26-13-125.5 (RSPEC-GAP-004). |
| US-SDNH-001-CT | State authority (not named in the cited sources; legal basis published by Connecticut G... | online_form; portal: not named in the cited channel sources | New-hire report: 20 days [US-CTS5-019] | TO CONFIRM; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-SDNH-001-DC | State authority (not named in the cited sources; legal basis published by Council of th... | online_form; portal: not named in the cited channel sources | New-hire report: 20 days [US-DCS5-022] | TO CONFIRM; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-SDNH-001-DE | State authority (not named in the cited sources; legal basis published by Delaware Gene... | online_form; portal: not named in the cited channel sources | New-hire report: 20 days [US-DES5-005] | TO CONFIRM; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-SDNH-001-FL | State authority (not named in the cited sources; legal basis published by Florida Senat... | online_form; portal: not named in the cited channel sources | New-hire report: 20 days [US-FLS5-008] | TO CONFIRM; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-SDNH-001-GA | Georgia Department of Human Services, Georgia State Directory of New Hires | online_form; portal: not named in the cited channel sources | New-hire report: 10 days [US-GAS5-012] | TO CONFIRM; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-SDNH-001-HI | Hawaii Department of the Attorney General, Child Support Enforcement Agency | online_form; portal: not named in the cited channel sources | New-hire report: 20 days [US-HIS5-021] | TO CONFIRM; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-SDNH-001-IA | State authority (not named in the cited sources; legal basis published by Iowa Legislat... | online_form; portal: not named in the cited channel sources | New-hire report: 15 days [US-IAS5-012] | TO CONFIRM; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-SDNH-001-ID | State authority (not named in the cited sources; legal basis published by Idaho Legisla... | online_form; portal: not named in the cited channel sources | New-hire report: 20 days [US-IDS5-015] | TO CONFIRM; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-SDNH-001-IL | Illinois Department of Employment Security | online_form; portal: not named in the cited channel sources | New-hire report: 20 days [US-ILS5-018] | TO CONFIRM; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-SDNH-001-IN | Indiana New Hire Reporting Center (State of Indiana; operated by contractor Stellarware) | online_form; portal: not named in the cited channel sources | New-hire report: 20 days [US-INS5-016] | TO CONFIRM; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-SDNH-001-KS | State authority (not named in the cited sources; legal basis published by Kansas Office... | online_form; portal: not named in the cited channel sources | New-hire report: 20 business days [US-KSS5-019] | TO CONFIRM; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-SDNH-001-KY | State authority (not named in the cited sources; legal basis published by Kentucky Legi... | online_form; portal: not named in the cited channel sources | New-hire report: 20 days [US-KYS5-020]; Recipient: Office of the Attorney General since 2025-07-01, within 20 days [US-KYS5-020] | TO CONFIRM; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-SDNH-001-LA | State authority (not named in the cited sources; legal basis published by Louisiana Sta... | online_form; portal: not named in the cited channel sources | New-hire report: 20 days [US-LAS5-010] | TO CONFIRM; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-SDNH-001-MA | Massachusetts Department of Revenue (Child Support Services) | online_form; portal: not named in the cited channel sources | New-hire report: 14 days [US-MAS5-016] | TO CONFIRM; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-SDNH-001-MD | State authority (not named in the cited sources; legal basis published by Maryland Gene... | online_form; portal: not named in the cited channel sources | New-hire report: 20 days [US-MDS5-018] | TO CONFIRM; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-SDNH-001-ME | State authority (not named in the cited sources; legal basis published by Maine Legisla... | online_form; portal: not named in the cited channel sources | New-hire report: 7 days [US-MES5-016] | TO CONFIRM; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-SDNH-001-MI | Michigan Department of Health and Human Services, Child Support Division (New Hires Ope... | online_form, file_upload, paper; portal: not named in the cited channel sources | New-hire report: 20 days [US-MIB5-001] | CONFIRMED; accuracy 80. Closes with: the Michigan New Hire Act citation in the MCL (RSPEC-GAP-022). |
| US-SDNH-001-MN | State authority (not named in the cited sources; legal basis published by Minnesota Off... | online_form; portal: not named in the cited channel sources | New-hire report: 20 days [US-MNS5-016] | TO CONFIRM; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-SDNH-001-MO | Missouri Department of Revenue | online_form; portal: not named in the cited channel sources | New-hire report: 20 days [US-MOS5-001] | TO CONFIRM; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-SDNH-001-MS | Mississippi Department of Human Services (State Directory of New Hires) | online_form; portal: not named in the cited channel sources | New-hire report: 15 days [US-MSS5-006] | TO CONFIRM; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-SDNH-001-MT | State authority (not named in the cited sources; legal basis published by Montana Legis... | online_form; portal: not named in the cited channel sources | New-hire report: 20 days [US-MTS5-012] | TO CONFIRM; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-SDNH-001-NC | State authority (not named in the cited sources; legal basis published by NC General As... | online_form; portal: not named in the cited channel sources | New-hire report: 20 days [US-NCS5-020] | TO CONFIRM; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-SDNH-001-ND | ND Department of Health and Human Services (Child Support) | online_form; portal: not named in the cited channel sources | New-hire report: 20 days [US-NDS5-013] | TO CONFIRM; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-SDNH-001-NE | State authority (not named in the cited sources; legal basis published by Nebraska Legi... | online_form; portal: not named in the cited channel sources | New-hire report: 20 days [US-NES5-014] | TO CONFIRM; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-SDNH-001-NH | NH General Court | online_form; portal: not named in the cited channel sources | New-hire report: 20 days [US-NHS5-006] | TO CONFIRM; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-SDNH-001-NJ | NJ Department of Human Services, Division of Family Development (New Jersey Child Suppo... | online_form; portal: not named in the cited channel sources | New-hire report: 20 days [US-NJS5-018] | TO CONFIRM; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-SDNH-001-NM | New Mexico New Hire Directory (state directory operated for NM; HCA Child Support Servi... | online_form; portal: not named in the cited channel sources | New-hire report: 20 days [US-NMS5-010] | TO CONFIRM; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-SDNH-001-NV | Nevada DETR Employment Security Division | online_form; portal: not named in the cited channel sources | New-hire report: 20 days [US-NVS5-007] | TO CONFIRM; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-SDNH-001-NY | NY Department of Taxation and Finance / NY Department of Labor | online_form; portal: not named in the cited channel sources | New-hire report: 20 days [US-NYS5-010] | TO CONFIRM; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-SDNH-001-OH | State authority (not named in the cited sources; legal basis published by Ohio General... | online_form; portal: not named in the cited channel sources | New-hire report: 20 days [US-OHS5-014] | TO CONFIRM; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-SDNH-001-OK | State authority (not named in the cited sources; legal basis published by Oklahoma Legi... | online_form; portal: not named in the cited channel sources | New-hire report: 20 days [US-OKS5-007] | TO CONFIRM; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-SDNH-001-OR | Oregon Department of Justice, Division of Child Support | online_form; portal: not named in the cited channel sources | New-hire report: 20 days [US-ORS5-016] | TO CONFIRM; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-SDNH-001-PA | State authority (not named in the cited sources; legal basis published by Pennsylvania... | online_form; portal: not named in the cited channel sources | New-hire report: 20 days [US-PAS5-008] | TO CONFIRM; accuracy 75. Closes with: the PA New Hire Reporting Program employer page (RSPEC-GAP-033). |
| US-SDNH-001-RI | State authority (not named in the cited sources; legal basis published by Rhode Island... | online_form; portal: not named in the cited channel sources | New-hire report: 14 days [US-RIS5-010] | TO CONFIRM; accuracy 75. Closes with: R.I. Gen. Laws 15-24-5 (RSPEC-GAP-034). |
| US-SDNH-001-SC | State authority (not named in the cited sources; legal basis published by South Carolin... | online_form; portal: not named in the cited channel sources | New-hire report: 20 days [US-SCS5-011] | TO CONFIRM; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-SDNH-001-SD | State authority (not named in the cited sources; legal basis published by South Dakota... | online_form; portal: not named in the cited channel sources | New-hire report: 20 days [US-SDS5-007] | TO CONFIRM; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-SDNH-001-TN | Tennessee Department of Labor and Workforce Development | online_form; portal: not named in the cited channel sources | New-hire report: 20 days [US-TNS5-008] | TO CONFIRM; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-SDNH-001-TX | Texas Workforce Commission | online_form; portal: not named in the cited channel sources | New-hire report: 20 days [US-TXS5-016] | TO CONFIRM; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-SDNH-001-UT | Utah Department of Workforce Services (Unemployment Insurance and New Hire Reporting) | online_form; portal: not named in the cited channel sources | New-hire report: 20 days [US-UTS5-003] | TO CONFIRM; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-SDNH-001-VA | Virginia New Hire Reporting Center (DSS Division of Child Support Enforcement) | online_form; portal: not named in the cited channel sources | New-hire report: 20 days [US-VAS5-006] | TO CONFIRM; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-SDNH-001-VT | State authority (not named in the cited sources; legal basis published by Vermont Gener... | online_form; portal: not named in the cited channel sources | New-hire report: 10 days [US-VTS5-014] | TO CONFIRM; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-SDNH-001-WA | State authority (not named in the cited sources; legal basis published by Washington St... | online_form; portal: not named in the cited channel sources | New-hire report: 20 days [US-WAS5-018] | TO CONFIRM; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-SDNH-001-WI | Wisconsin DWD Unemployment Insurance Division | online_form; portal: not named in the cited channel sources | New-hire report: 20 days [US-WIS5-013] | TO CONFIRM; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-SDNH-001-WV | WorkForce West Virginia | online_form; portal: not named in the cited channel sources | New-hire report: 14 days [US-WVS5-016] | TO CONFIRM; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-SDNH-001-WY | State authority (not named in the cited sources; legal basis published by Wyoming Legis... | online_form; portal: not named in the cited channel sources | New-hire report: 20 days [US-WYS5-006] | TO CONFIRM; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |


## 7.6 State paid-leave, disability and long-term-care programme reports

| Report row | Authority | Channel class; portal | Hand-off requirement | Status; accuracy |
|---|---|---|---|---|
| US-PFML-001-CA | California EDD | online_form; portal: not named in the cited channel sources | Programme report: DE 9 + DE 9C quarterly, electronic only (per employee subject wages, PIT wages, PIT withheld); DE 88 deposits on the federal schedule; no annual reconciliation; W-2 NOT filed with EDD/FTB [US-CAS5-018] (effective 2026-01-01 to 2026-12-31) | TO CONFIRM; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-PFML-001-CO | Colorado Department of Labor and Employment, Family & Medical Leave Insurance Division | online_form; portal: not named in the cited channel sources | Programme report: FAMLI wage report and premium payment per quarter (2026 Q3 deadline October 31) [US-COS5-008] | CONFIRMED; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-PFML-001-CT | Connecticut Paid Leave Authority | online_form, file_upload, xml; portal: not named in the cited channel sources | Programme report: CT Paid Leave quarterly return via portal or batch return files in two file formats: XML or CSV [US-CTS5-022] [US-CTS5-036]; Channel or file format: Batch XML (XSD) or CSV via SFTP per File Specification Toolkit v2.1.9; employer-level return totals only; acknowledgement file E/W [US-CTB5-001] | CONFIRMED; accuracy 90. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-PFML-001-DC | DC DOES Office of Paid Family Leave | online_form; portal: ESSP | Programme report: Not configured in this release (open gap SIR-RQ-29); Channel or file format: PFL quarterly wage filing and tax payment via the Employer Self-Service Portal (ESSP); due April 30 (Q1), July 31 (Q2), October 31 (Q3), January 31 (Q4) [US-DCS5-019] | CONFIRMED; accuracy 80. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-PFML-001-DE | Delaware Department of Labor | online_form; portal: Delaware LaborFirst | Programme report: Quarterly Hours & Wage Report and contributions in Delaware LaborFirst [US-DES5-013] | CONFIRMED; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-PFML-001-HI | Hawaii Department of Labor and Industrial Relations (DCD) | online_form; portal: not named in the cited channel sources | Programme report: False [US-HIS7-001] | CONFIRMED; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-PFML-001-MA | State authority (not named in the cited sources) | not configured; portal: not configured | Programme report: Not configured in this release (open gap SIR-RQ-29) | TO CONFIRM; accuracy 50. Closes with: the DFML employer contribution and wage reporting guide (RSPEC-GAP-019). |
| US-PFML-001-MD | Maryland Department of Labor (FAMLI Division) | online_form; portal: not named in the cited channel sources | Programme report: Not configured in this release (open gap SIR-RQ-29) | TO CONFIRM; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-PFML-001-ME | Maine Department of Labor, Paid Family and Medical Leave | online_form; portal: PFML portal | Programme report: PFML quarterly wage report and premium in the PFML portal; third-party payroll designation in the portal [US-MES5-024] | CONFIRMED; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-PFML-001-MN | Minnesota DEED (Paid Leave) | online_form; portal: not named in the cited channel sources | Programme report: Paid Leave quarterly wage detail and premium to the commissioner (Minnesota Department of Employment and Economic Development), electronic [US-MNS5-018] | CONFIRMED; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-PFML-001-WA | Washington ESD Paid Family and Medical Leave | online_form, file_upload; portal: paidleave.wa.gov | Programme report: combined Paid Leave + WA Cares quarterly report (wages and hours) on paidleave.wa.gov [US-WAPFML-001]; Channel or file format: Manual entry (up to 50 employees), single CSV file (ESD template), ICESA bulk file for employer agents [US-WAB5-003] | CONFIRMED; accuracy 90. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |


## 7.7 Local income, wage and city payroll tax returns

| Report row | Authority | Channel class; portal | Hand-off requirement | Status; accuracy |
|---|---|---|---|---|
| US-LOC-001-AL | City of Leeds, Alabama (revenue examiner; remittance via Avenu) | online_form; portal: Avenu (named in [US-ALS5-017]) | Local return: Municipal occupational taxes filed with each city/county or its agent (e.g. Leeds via Avenu, Birmingham via HdL) [US-ALS5-017] | TO CONFIRM; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-LOC-001-CO | City and County of Denver Department of Finance | online_form; portal: not named in the cited channel sources | Local return: Denver Occupational Privilege Tax withheld by employer, returned to Denver Treasury [US-COP52-001] | TO CONFIRM; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-LOC-001-DE | City of Wilmington Department of Finance | online_form; portal: not named in the cited channel sources | Local return: Wilmington earned income tax 1.25% collected by the City [US-DEP52-001] | TO CONFIRM; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-LOC-001-KY | Louisville Metro Revenue Commission | online_form; portal: not named in the cited channel sources | Local return: Local occupational taxes administered by cities/counties/school districts (Louisville W-1/W-3; Lexington) [US-KYP52-002] [US-KYP9W-001] | TO CONFIRM; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-LOC-001-MI | Michigan Department of Treasury - City Tax Administration | online_form; portal: not named in the cited channel sources | Local return: Detroit monthly return Form 5323 (15th) and annual reconciliation Form 5321 TY2026 due 2027-02-28; DW-4 certificate [US-MIP51-002] | TO CONFIRM; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-LOC-001-MO | City of Kansas City, Missouri Finance Department | online_form; portal: not named in the cited channel sources | Local return: Kansas City 1% earnings tax; RD-100 registration [US-MOP52-007] | TO CONFIRM; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-LOC-001-OH | Ohio Department of Taxation | file_upload, api; portal: not named in the cited channel sources | Local return: Not configured in this release (open gap SIR-RQ-23) | CONFIRMED; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-LOC-001-OR | City of Portland Revenue Division | online_form; portal: Portland Revenue Online (named in [US-ORS5-024]) | Local return: Quarterly returns and annual reconciliation on Portland Revenue Online; XML ReturnBatch 1.0; W-2 EFW2 by 31 Jan [US-ORS5-024] [US-OR-002] | TO CONFIRM; accuracy 75. Closes with: the City of Portland Revenue Division bulk upload guide (RSPEC-GAP-032). |
| US-LOC-001-PA | Local EIT/LST tax collector designated for the worksite PSD (DCED Address Search) [US-P... | not named in the cited channel sources; portal: not named in the cited channel sources | Local return: EIT/LST quarterly returns and W2-R to the collector; Philadelphia quarterly returns [US-PAS5-017] [US-PAS5-018] | TO CONFIRM; accuracy 70. Closes with: the local collector's filing instructions or a real filing. |
| US-LOC-001-WV | City of Charleston, Office of the City Collector | paper; portal: City finance offices (Charleston, Morgantown) | Local return: Charleston City Service Fee: 3.00 per calendar week (Sun-Sat, no proration) withheld by employer; Form CSF-2 City Service Fee Return with each remittance; calendar-quarter reporting periods (ending March 31, June 30, September 30, December 31); fees remitted to the City Collector before the expiration of one month from the end of the reporting period; the regulations state no filing channel (City Collector, 915 Quarrier Street, Charleston); CSF-1 prior payment, CSF-3 refund (3 years) [US-WVS6-001] | TO CONFIRM; accuracy 75. Closes with: the ordinances and return forms of the other municipalities (for example Huntington, Wheeling, Parkersburg, Fairmont, Weirton) (RSPEC-RQ-11). |
| US-LOC-002-MO | City of St. Louis Collector of Revenue | online_form; portal: not named in the cited channel sources | Local return: Kansas City 1% earnings tax; RD-100 registration [US-MOP52-007] | TO CONFIRM; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-LOC-002-NJ | City of Newark, Division of Tax Abatement and Special Taxes | online_form; portal: not named in the cited channel sources | Local return: Newark and Jersey City quarterly employer payroll tax returns [US-NJP6-001] | TO CONFIRM; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-LOC-002-PA | City of Pittsburgh, Department of Finance | paper; portal: City of Pittsburgh Department of Finance | Local return: EIT/LST quarterly returns and W2-R to the collector; Philadelphia quarterly returns [US-PAS5-017] [US-PAS5-018] | TO CONFIRM; accuracy 75. Closes with: the 2026 Form ET-1 from the City of Pittsburgh Department of Finance (RSPEC-RQ-12). |
| US-LOC-003-WA | City of Seattle Office of City Finance | online_form, paper; portal: FileLocal https://www.seattle.gov/city-finance/business-taxes-and-licenses/seattle-taxe... | City return: Seattle payroll expense tax: Taxpayer Authorization Form per client [US-WAP51-001] | TO CONFIRM; accuracy 85. Closes with: a real filing or the provider's acceptance report for Seattle. |


## 7.8 Nevada MBT, payroll transit levies and State-fund workers' compensation

| Report row | Authority | Channel class; portal | Hand-off requirement | Status; accuracy |
|---|---|---|---|---|
| US-DOR-003-NV | Nevada Department of Taxation | online_form; portal: My Nevada Tax (named in [US-NVS5-009]) | Return: MBT TAX-F003 quarterly on My Nevada Tax; from 2026-01-01 MBT wages compared with ESD wages [US-NVS5-009] [US-NVS5-010] | TO CONFIRM; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-DOR-004-NY | NY Department of Taxation and Finance | online_form; portal: NY DTF Web File https://www.tax.ny.gov/forms/current-forms/mta/mta305i.htm | Return: MTA-305 quarterly [US-NY-003] | TO CONFIRM; accuracy 85. Closes with: the MTA-305 form itself and a real filing or the provider's acceptance report. |
| US-DOR-004-OR | Oregon Department of Revenue with OED and DCBS | online_form; portal: Frances Online | Return: Form OQ quarterly via Frances Online: withholding, UI, Paid Leave, WBF, TriMet, Lane, STT; Schedule B; Form 132 [US-ORS5-010] (effective 2026-01-01 to 2026-12-31) | CONFIRMED; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-WC-001-NM | New Mexico Taxation and Revenue Department | online_form; portal: not named in the cited channel sources | Report: TRD-41431 (new 2026-01-01): WC fee return + employee quarterly wage and withholding report, 25th after quarter [US-NMS5-012] | CONFIRMED; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-WC-001-OR | Oregon Department of Revenue with OED and DCBS | online_form; portal: Frances Online | Report: Form OQ quarterly via Frances Online: withholding, UI, Paid Leave, WBF, TriMet, Lane, STT; Schedule B; Form 132 [US-ORS5-010] (effective 2026-01-01 to 2026-12-31) | CONFIRMED; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-WC-001-WA | Washington State Department of Labor & Industries | online_form; portal: not named in the cited channel sources | Report: Not configured in this release (open gap SIR-RQ-32) | CONFIRMED; accuracy 75. Closes with: the L&I Employer Quarterly Report instructions or the WAC 296-17 reporting sections (RSPEC-GAP-042). |
| US-WC-001-WY | Wyoming Department of Workforce Services | online_form; portal: not named in the cited channel sources | Report: workers compensation payroll report monthly (quarterly by permission), joint UI/WC reporting [US-WYS5-007] | TO CONFIRM; accuracy 75. Closes with: a real filing or the provider's acceptance report for this jurisdiction. |


# 8. Provider input data set

The minimum data a provider must receive, derived from the layouts read. Field names and types are owned by US-DD-001 v1.0; the authority's own box and block identifiers are used here. Elements that accumulate payroll results (hours, weeks, wage totals) are produced by the payroll calculation and are listed because the provider needs them, not because the data dictionary holds them.


## 8.1 Per employer entity

| Data element | Needed for | Statement | Source |
|---|---|---|---|
| State withholding, UI and paid-leave account identifiers per State | Every State return | per-state withholding account / UI account / paid-leave account ids (e.g. UT 14-digit number ending in WTH; KS 036#######F##; MD Central Registration Number in RS positions 338-345; IA 9-digit permit number) | [US-UTR3-001] [US-KSS5-026] [US-MDS5-016] [US-IAS5-017] |
| Federal depositor status | Federal deposits | Form 941 deposit schedule names: monthly schedule depositor; semiweekly schedule depositor (from the lookback period: $50,000 or less = monthly; more than $50,000 = semiweekly) | [US-FEDS5-004] |
| New York MCTMT payroll zone | MCTMT return | MCTMT zone payroll | [US-NY-003] |
| Corporate officer without voluntary UI coverage flag, Washington | Washington UI report | corporate officer without voluntary UI coverage flag | [US-WAS5-027] |
| E-Verify certification, Florida | Florida RT-6 | E-Verify certification (private employers 25+), certified on first RT-6 of the year | [US-FLS5-010] [US-FLS5-021] |
| Employer Signature PIN (EFW2 RE record, optional) | Form W-2 file to SSA | Optional RE 319-328 Employer Signature PIN (S-XXXXXX-Y, Luhn) requested by the employer from SSA to sign wage reports electronically; blanks if none | [US-FEDS5-032] |


## 8.2 Per employee, identity and routing

| Data element | Needed for | Statement | Source |
|---|---|---|---|
| Work State | State and UI routing | work state where the service is localized (UI localization of work, UIPL 20-04) | [US-MULTIS5-017] |
| Residence State | Resident withholding | residence state (drives resident withholding; interstate transport workers are subject to withholding only by their State of residence under 49 U.S.C. 14503) | [US-MULTIS5-001] |
| State of unemployment insurance coverage | UI wage reports | single UI state per employee per period under the localization test; also applies to WA family and medical leave (RCW Title 50A) (in force for 2026; the source carries no effective date) | [US-MULTIS5-024] [US-MULTIS5-017] |
| Wages reported to other States in the year | UI taxable wage computation | wages reported to other states in the year (excess wage computation) | [US-MULTIS5-010] |
| Date services first performed | New-hire reports | date services first performed (new-hire report federal minimum) | [US-FEDS5-024] |
| Date of birth for State new-hire reports | New-hire reports | date of birth required by GA, IA, ME, MS, NJ, OH, OR, WA, WI, WV new-hire reports | [US-NJS5-018] [US-GAS5-012] [US-IAS5-012] [US-MES5-016] [US-MSS5-007] [US-OHS5-014] [US-ORS5-016] [US-WAS5-018] [US-WIS5-013] [US-WVS5-016] |
| SSN, not an ITIN, Florida | Florida RT-6 | SSN required on RT-6; ITIN not accepted | [US-FLS5-024] |


## 8.3 Per employee, State extras

| Data element | Needed for | Statement | Source |
|---|---|---|---|
| Occupational code, Alaska | Alaska UI wage report | 6- or 8-digit occupational code per employee | [US-AKS5-014] |
| Geographic code, Alaska | Alaska UI wage report | 2-digit Alaska geographic code per employee | [US-AKS5-014] |
| SOC code, Washington | Washington UI wage report | SOC code per employee | [US-WAS5-013] |
| SOC code and start date, Indiana | Indiana UI wage report | SOC code (6 digits) and start date per worker | [US-INS5-014] |
| Job, compensation and rate-of-pay basis, Indiana new hire | Indiana new-hire report | job title, SOC, starting compensation, rate-of-pay basis | [US-INS5-016] |
| SOC or job title and county, West Virginia | West Virginia UI wage report | SOC or job title and county per employee | [US-WVUI-001] |
| Occupation, hours and worksite ZIP, Connecticut | Connecticut UI wage report | Not configured in this release (open gap SIR-RQ-01) | [US-CTS5-018] [US-CTS5-016] |
| Gender and hourly wage, Vermont | Vermont UI wage report | gender and hourly wage for hourly workers | [US-VTS5-007] |
| Enhanced content, Texas | Texas UI wage report | industry, occupation, full/part-time, county of primary employment, remote-work status | [US-TXS5-008] |
| Separation dates and probationary flag, Missouri | Missouri UI wage report | separation dates and probationary flag P with dates (28 days or less) | [US-MOS5-013] |
| Hours and job title, Nebraska | Nebraska UI wage report | hours and job title (optional) | [US-NES5-011] |
| Hours, work location and adjustment reason, Massachusetts | Massachusetts UI wage report | hours worked, work location, 12th-of-month employment, adjustment reason code | [US-MAS5-018] |
| Weeks paid, Ohio | Ohio UI wage report | number of weeks paid per employee | [US-OHS5-020] |
| Base weeks, New Jersey | New Jersey WR-30 | base weeks per employee (week >= 20 x prior-year minimum wage) | [US-NJS5-017] |
| Credit weeks, Pennsylvania | Pennsylvania UC-2 | credit weeks per employee (week with remuneration >= 116) | [US-PAS5-013] |
| Month-of-12th employment counts | Florida and other monthly counts | covered on payroll in the pay period including the 12th of each month (employer monthly counts) | [US-FLS5-021] |
| NAICS code, Maryland W-2 file | Maryland MW508 record | NAICS code (employer) in MW508 RV record | [US-MDS5-016] |
| Treasury Tipped Occupation Code | W-2 box 14b | Treasury Tipped Occupation Code per employee (W-2 box 14b, TY2026) | [US-FEDS5-007] |


## 8.4 Per employee, local and school-district routing

| Data element | Needed for | Statement | Source |
|---|---|---|---|
| Ohio municipality and collector | Ohio municipal returns | Ohio municipality of work (718.03) and residence; collector: the central collection agency, the regional income tax agency or the municipal tax administrator | [US-OHP52-003] |
| Ohio school district code | Ohio W-2 upload and school-district returns | four-digit Ohio school district code of residence (9999 full-year nonresident); W-2 and SD 101/141 | [US-OHB5-401] [US-OHB5-001] [US-OHS5-018] [US-OHS5-019] |
| Pennsylvania PSD code | Pennsylvania EIT returns | PA PSD code of work location and of residence (looked up with the DCED Address Search Application) | [US-PAS5-017] [US-PAS5-018] |
| Indiana county on January 1 | Indiana WH-1 and W-2 | Indiana county of residence and county of principal employment on Jan 1 (WH-4) | [US-INS5-021] |
| Maryland county of residence | Maryland MW506 | Maryland county of residence (local rate tables) via MW507 | [US-MDP51-001] |
| Kentucky locality | Kentucky occupational returns | Kentucky locality of work (Louisville Metro) and residence (school board component) | [US-KYP9W-001] |
| Oregon Metro and Multnomah work location | Portland returns | Metro SHS / Multnomah PFA work location and opt-in/opt-out | [US-ORS5-004] |
| Oregon transit district | Form OQ | TriMet / Lane transit district of work (effective 2026-01-01 to 2026-12-31) | [US-ORS5-010] |
| Michigan city | Michigan city returns | Michigan city (e.g. Detroit) resident / nonresident predominant place of employment; DW-4 | [US-MIP51-002] |
| Denver occupational privilege tax location | Denver return | Denver OPT work location and monthly earnings >=500 test | [US-COP52-001] |
| New York City and Yonkers residence | NYS-45 and withholding | NYC / Yonkers resident status and resident period | [US-NYS5-010] |


## 8.5 New-hire extras

| Data element | Needed for | Statement | Source |
|---|---|---|---|
| Health insurance offered and starting wage, Maryland | Maryland new-hire report | starting wage, employer health insurance offered, MD UI account number | [US-MDS5-018] |
| Employee fields, Mississippi | Mississippi new-hire report | Date of birth, gender, salary, payment frequency and medical insurance eligibility (required employee fields of the Mississippi new hire report beyond name, address, SSN and date of hire) | [US-MSS5-007] [US-MSS5-006] |
| Employee fields, Georgia | Georgia new-hire report | Employee's Date of Birth, Employee's Medical Insurance availability, Employee's State of Hire | [US-GAS5-012] |
| Occupation, Louisiana | Louisiana new-hire report | occupation | [US-LAS5-010] |
| Dependent health coverage, Iowa | Iowa new-hire report | whether the employer has employee dependent health care coverage available and the appropriate date on which the employee may qualify for the coverage; the address to which income withholding orders or the notices of orders and garnishments should be sent | [US-IAS5-012] |
| Re-hire gap | New-hire reports | 60 days | [US-CTS5-019] |


## 8.6 Programme reports

| Data element | Needed for | Statement | Source |
|---|---|---|---|
| Connecticut Paid Leave employee-level data | Connecticut Paid Leave return | none: the CT Paid Leave return carries employer-level totals only (CT wages, CT employee counts, contributions); employee records are rejected, so no per-employee CTPL field is needed beyond the CTPL-wage computation | [US-CTB5-001] |
| Washington Paid Leave and WA Cares employee fields | Washington programme report | Per employee for the Paid Leave/WA Cares report: date of birth, WA Cares exemption status (approved exemption letter), quarterly hours associated with wages (rounded up) | [US-WAB5-003] |
| Delaware Paid Leave hours and wages | Delaware Paid Leave report | hours and wages per employee for Delaware Paid Leave quarterly report | [US-DES5-013] |
| Oregon Form 132 wage and hour detail | Form OQ | employee wage and hour detail (Form 132) (effective 2026-01-01 to 2026-12-31) | [US-ORS5-010] |
| Minnesota paid hours | Minnesota UI and Paid Leave | total paid hours worked per quarter (exempt FT = 40 h/week) | [US-MNS5-015] |


## 8.7 Inputs not carried by any filing

Two data elements of the data dictionary reach no authority filing and no provider hand-off: the employee primary language is an input of the employee notice template, and the Iowa school district of residence is an input of the individual assessment. They are therefore not part of the provider data set.

| Data element | Why it is not a provider input | Statement | Source |
|---|---|---|---|
| Iowa school district of residence | Individual assessment (school district surtax at filing), not an employer filing carried by a provider | Iowa school district of residence (surtax at assessment; IA W-4 note) | [US-IAP52-001] |
| Employee primary language | Employee notice template input; no authority filing or integration carries it | employee primary language for the Labor Law 195.1 pay-rate/payday notice (English + primary language) | [US-NYP9L-001] |


# Appendix A. Sources

Sources cited in this document, by register id.

| Register id | Authority | Instrument type | Published on (host) |
|---|---|---|---|
| US-AKP51-006 | Alaska DOLWD Employment Security Tax | form | www.labor.alaska.gov |
| US-AKS5-005 | Alaska DOLWD Employment Security Tax | agency guide | labor.alaska.gov |
| US-AKS5-007 | Alaska Department of Revenue, Child Support Enforcement Division (form | agency guide | childsupport.alaska.gov |
| US-AKS5-013 | Alaska DOLWD Employment Security Tax | form | labor.alaska.gov |
| US-AKS5-014 | Alaska DOLWD Employment Security Tax | technical specification | labor.alaska.gov |
| US-AKWT-001 | Alaska Dept of Revenue Tax Division | portal page | tax.alaska.gov |
| US-ALP52-002 | Alabama Department of Workforce, UC Division | form | web.archive.org |
| US-ALS5-001 | Alabama Department of Revenue, Withholding Tax Section | guide | www.revenue.alabama.gov |
| US-ALS5-006 | Alabama Department of Revenue | technical spec | www.revenue.alabama.gov |
| US-ALS5-007 | Alabama Department of Workforce, Unemployment Compensation | authority page | workforce.alabama.gov |
| US-ALS5-008 | Alabama Department of Workforce, New-Hire Unit | authority page | workforce.alabama.gov |
| US-ALS5-017 | City of Leeds, Alabama (revenue examiner; remittance via Avenu) | guide | leedsalabama.gov |
| US-ARP51-002 | Arkansas Department of Finance and Administration | withholding guide | www.dfa.arkansas.gov |
| US-ARP52-003 | Arkansas Department of Finance and Administration | form | www.dfa.arkansas.gov |
| US-ARP9V-001 | Arkansas Division of Workforce Services / Division of Reemployment | agency guide | reemployment.arkansas.gov |
| US-AZB5-005 | Arizona Department of Economic Security | agency page | des.az.gov |
| US-AZP52-001 | Arizona Department of Revenue | authority form | azdor.gov |
| US-AZP52-002 | Arizona Department of Economic Security | authority form | des.az.gov |
| US-AZP52-005 | Arizona Department of Revenue | authority page | azdor.gov |
| US-AZS5-012 | Arizona State Legislature (azleg.gov, A.R.S.) | statute | www.azleg.gov |
| US-AZS5-025 | Arizona Department of Revenue | publication | azdor.gov |
| US-CAEDD-006 | California EDD | form | edd.ca.gov |
| US-CAS5-002 | California EDD | guide | edd.ca.gov |
| US-CAS5-018 | California EDD | guide | edd.ca.gov |
| US-COP51-006 | Colorado Department of Revenue | portal page | tax.colorado.gov |
| US-COP52-001 | City and County of Denver Department of Finance | tax guide | web.archive.org |
| US-COP52-003 | Colorado Department of Labor and Employment | agency page | cdle.colorado.gov |
| US-COS5-006 | Colorado Department of Revenue (CDOR), Taxation Division | agency guide | tax.colorado.gov |
| US-COS5-008 | Colorado Department of Labor and Employment, Family & Medical Leave In | agency notice | content.govdelivery.com |
| US-COS5-013 | Colorado Department of Revenue | technical specification | tax.colorado.gov |
| US-CTB5-001 | Connecticut Paid Leave Authority | technical guide | www.ctpaidleave.org |
| US-CTP10-001 | Connecticut Department of Revenue Services | guide | portal.ct.gov |
| US-CTP51-007 | Connecticut DRS | form index | portal.ct.gov |
| US-CTP52-002 | Connecticut Department of Labor | authority page | portal.ct.gov |
| US-CTS5-013 | Connecticut Department of Revenue Services | guide | portal.ct.gov |
| US-CTS5-019 | Connecticut General Assembly | statute | www.cga.ct.gov |
| US-CTS5-022 | Connecticut Paid Leave Authority | agency page | www.ctpaidleave.org |
| US-CTS5-032 | Connecticut Department of Labor | technical specification | portal.ct.gov |
| US-CTS5-036 | Connecticut Paid Leave Authority | agency page | www.ctpaidleave.org |
| US-DCP51-014 | DC Office of Tax and Revenue | authority page | otr.cfo.dc.gov |
| US-DCP52-003 | DC Department of Employment Services, Office of Unemployment Compensat | form | essp.does.dc.gov |
| US-DCS5-014 | DC Office of Tax and Revenue | authority publication | otr.cfo.dc.gov |
| US-DCS5-015 | DC Office of Tax and Revenue | technical specification | otr.cfo.dc.gov |
| US-DCS5-016 | DC Department of Employment Services | portal page | essp.does.dc.gov |
| US-DCS5-018 | Council of the District of Columbia | statute | code.dccouncil.gov |
| US-DCS5-019 | DC DOES Office of Paid Family Leave | authority page | dcpaidfamilyleave.dc.gov |
| US-DCS5-022 | Council of the District of Columbia | statute | code.dccouncil.gov |
| US-DCS5-026 | DC Department of Employment Services (DOES) | authority page | does.dc.gov |
| US-DEP52-001 | City of Wilmington Department of Finance | regulation | www.wilmingtonde.gov |
| US-DEP52-002 | Delaware Department of Labor; Delaware Division of Revenue | form | laborfiles.delaware.gov |
| US-DES5-005 | Delaware General Assembly (Delaware Code Online) | statute | delcode.delaware.gov |
| US-DES5-008 | Delaware Division of Revenue | faq | revenue.delaware.gov |
| US-DES5-009 | Delaware Division of Revenue | form instructions | revenuefiles.delaware.gov |
| US-DES5-011 | Delaware Department of Labor | faq | labor.delaware.gov |
| US-DES5-013 | Delaware Department of Labor | agency page | labor.delaware.gov |
| US-FED-008 | IRS | revenue procedure | www.irs.gov |
| US-FED-028 | IRS | official form | www.irs.gov |
| US-FEDP51-002 | IRS | technical guide | www.irs.gov |
| US-FEDP51-016 | Washington Employment Security Department | authority page | esd.wa.gov |
| US-FEDP6-002 | HHS Administration for Children and Families (OCSE) | official form | acf.gov |
| US-FEDR3-003 | HHS / ACF / OCSE | official form | acf.gov |
| US-FEDS5-004 | IRS | technical guide | www.irs.gov |
| US-FEDS5-007 | IRS | form instructions | www.irs.gov |
| US-FEDS5-012 | IRS | form instructions | www.irs.gov |
| US-FEDS5-014 | IRS | rate table | www.irs.gov |
| US-FEDS5-016 | IRS | technical guide | www.irs.gov |
| US-FEDS5-024 | U.S. Congress (OLRC/GPO) | statute | www.govinfo.gov |
| US-FEDS5-028 | OMB Office of Information and Regulatory Affairs / HHS ACF OCSE | official notice | www.reginfo.gov |
| US-FEDS5-031 | IRS | technical guide | www.irs.gov |
| US-FEDS5-032 | Social Security Administration | technical specification | www.ssa.gov |
| US-FEDS6-003 | Internal Revenue Service | official form draft | www.irs.gov |
| US-FEDS6-004 | Internal Revenue Service | official form draft | www.irs.gov |
| US-FEDS6-006 | Internal Revenue Service | form instructions draft | www.irs.gov |
| US-FEDS6-007 | Internal Revenue Service | form instructions | www.irs.gov |
| US-FEDS6-010 | Internal Revenue Service | technical guide | www.irs.gov |
| US-FIL-001 | IRS | technical guide | www.irs.gov |
| US-FIL-002 | Social Security Administration | technical guide | www.ssa.gov |
| US-FIL-006 | California EDD | technical guide | edd.ca.gov |
| US-FIL-007 | NYS Dept of Taxation and Finance | technical guide | www.tax.ny.gov |
| US-FIL-008 | PA Dept of Labor and Industry | technical guide | www.pa.gov |
| US-FIL-010 | PA Department of Revenue | form | www.pa.gov |
| US-FIL-011 | Ohio Department of Taxation | form | dam.assets.ohio.gov |
| US-FIL-012 | Ohio Department of Taxation | technical guide | dam.assets.ohio.gov |
| US-FL-001 | Florida Senate | constitution | www.flsenate.gov |
| US-FL-005 | Florida Department of Revenue | form | floridarevenue.com |
| US-FLS5-006 | Florida Senate (2026 Florida Statutes) | statute | www.flsenate.gov |
| US-FLS5-008 | Florida Senate (2026 Florida Statutes) | statute | www.flsenate.gov |
| US-FLS5-010 | Florida Senate (2026 Florida Statutes) | statute | www.flsenate.gov |
| US-FLS5-021 | Florida Department of Revenue | form | floridarevenue.com |
| US-FLS5-022 | Florida Department of Revenue | technical specification | floridarevenue.com |
| US-FLS5-024 | Florida Department of Revenue | authority page | floridarevenue.com |
| US-GAS5-002 | Georgia Department of Revenue | official guide | dor.georgia.gov |
| US-GAS5-003 | Georgia Department of Revenue | official guide | dor.georgia.gov |
| US-GAS5-005 | Georgia Department of Labor | official guide | dol.georgia.gov |
| US-GAS5-012 | Georgia Department of Human Services, Georgia State Directory of New H | agency page | newhire-reporting.com |
| US-GAW1B-001 | Georgia Department of Labor | guide | dol.georgia.gov |
| US-GAW1B-003 | Georgia Department of Revenue | authority page | dor.georgia.gov |
| US-HIP51-001 | Hawaii Department of Taxation | withholding guide | files.hawaii.gov |
| US-HIP51-004 | Hawaii Department of Taxation | form | files.hawaii.gov |
| US-HIP52-003 | Hawaii Department of Labor and Industrial Relations | guide | labor.hawaii.gov |
| US-HIS5-005 | Hawaii Department of Taxation | authority page | tax.hawaii.gov |
| US-HIS5-006 | Hawaii Department of Taxation | circular | files.hawaii.gov |
| US-HIS5-012 | Hawaii DLIR Unemployment Insurance Division | official guide | labor.hawaii.gov |
| US-HIS5-021 | Hawaii Department of the Attorney General, Child Support Enforcement A | official guide | ag.hawaii.gov |
| US-HIS7-001 | Hawaii Department of Labor and Industrial Relations (DCD) | authority page | labor.hawaii.gov |
| US-IAP51-003 | Iowa Department of Revenue | form | revenue.iowa.gov |
| US-IAP51-004 | Iowa Workforce Development - UI Tax Bureau | form | workforce.iowa.gov |
| US-IAP52-001 | Iowa Department of Revenue | form | revenue.iowa.gov |
| US-IAS5-012 | Iowa Legislature | statute | www.legis.iowa.gov |
| US-IAS5-016 | Iowa Department of Revenue | authority page | revenue.iowa.gov |
| US-IAS5-017 | Iowa Department of Revenue | authority page | revenue.iowa.gov |
| US-IAS5-018 | Iowa Department of Revenue | technical spec | revenue.iowa.gov |
| US-IAS5-024 | Iowa Workforce Development (published by Iowa Legislature) | regulation | www.legis.iowa.gov |
| US-IDR3-001 | Idaho State Tax Commission | form | tax.idaho.gov |
| US-IDR3-002 | Idaho Department of Labor, Unemployment Insurance Compliance Bureau | form | www.labor.idaho.gov |
| US-IDS5-009 | Idaho State Tax Commission (Wayback id_ 20260618173701 and 20260412130 | authority page | tax.idaho.gov |
| US-IDS5-010 | Idaho State Tax Commission (Wayback id_ 20260214041722 and 20260514224 | authority page | tax.idaho.gov |
| US-IDS5-015 | Idaho Legislature (Wayback id_ 20260222181234) | statute | legislature.idaho.gov |
| US-IDS5-021 | Idaho Department of Labor (Wayback id_ 20260113182918) | official guide | www.labor.idaho.gov |
| US-IL-004 | Illinois Department of Revenue | guide | tax.illinois.gov |
| US-ILP52-010 | Illinois Department of Employment Security | technical spec | ides.illinois.gov |
| US-ILS5-011 | Illinois Department of Revenue | official instructions | tax.illinois.gov |
| US-ILS5-013 | Illinois Department of Revenue | official guide | tax.illinois.gov |
| US-ILS5-017 | Illinois Department of Employment Security | authority page | ides.illinois.gov |
| US-ILS5-018 | Illinois Department of Employment Security | authority page | ides.illinois.gov |
| US-INR3-002 | Indiana Department of Revenue; Indiana DWD | authority page | www.in.gov |
| US-INR3-003 | Indiana Department of Revenue | authority page | www.in.gov |
| US-INR3-004 | Indiana Department of Workforce Development | authority publication | www.in.gov |
| US-INS5-010 | Indiana Department of Revenue | authority page | www.in.gov |
| US-INS5-011 | Indiana Department of Revenue | technical spec | www.in.gov |
| US-INS5-014 | Indiana Department of Workforce Development | official guide | www.in.gov |
| US-INS5-016 | Indiana New Hire Reporting Center (State of Indiana; operated by contr | portal doc | in-newhire.com |
| US-INS5-021 | Indiana Department of Revenue | official form | forms.in.gov |
| US-KSP51-005 | Kansas Department of Revenue | form | www.ksrevenue.gov |
| US-KSP52-003 | Kansas Department of Labor | authority page | www.dol.ks.gov |
| US-KSS5-001 | Kansas Department of Revenue | guide | www.ksrevenue.gov |
| US-KSS5-007 | Kansas Office of the Revisor of Statutes | statute | www.ksrevisor.gov |
| US-KSS5-019 | Kansas Office of the Revisor of Statutes | statute | www.ksrevisor.gov |
| US-KSS5-022 | Kansas Department of Labor | agency page | www.dol.ks.gov |
| US-KSS5-026 | Kansas Department of Revenue | technical spec | www.ksrevenue.gov |
| US-KYP52-002 | Kentucky Department of Revenue | agency page | web.archive.org |
| US-KYP9W-001 | Louisville Metro Revenue Commission | agency page | louisvilleky.gov |
| US-KYS5-013 | Kentucky Department of Revenue | guide | revenue.ky.gov |
| US-KYS5-019 | Kentucky Office of Unemployment Insurance | guide | ui.ky.gov |
| US-KYS5-020 | Kentucky Legislative Research Commission | statute | apps.legislature.ky.gov |
| US-KYS6-001 | Kentucky Education and Labor Cabinet, Office of Unemployment Insurance | official guide | ui.ky.gov |
| US-LAP51-002 | Louisiana Department of Revenue | faq | revenue.louisiana.gov |
| US-LAP52-005 | Louisiana Workforce Commission | authority page | www.laworks.net |
| US-LAS5-003 | Louisiana Department of Revenue | authority page | revenue.louisiana.gov |
| US-LAS5-007 | Louisiana Workforce Commission | faq | www.laworks.net |
| US-LAS5-008 | Louisiana Department of Revenue (Louisiana Administrative Code) | regulation | dam.ldr.la.gov |
| US-LAS5-009 | Louisiana Department of Revenue | faq | www.revenue.la.gov |
| US-LAS5-010 | Louisiana State Legislature | statute | www.legis.la.gov |
| US-MAS5-013 | Massachusetts Department of Revenue | guide | www.mass.gov |
| US-MAS5-015 | Massachusetts Department of Revenue | guide | www.mass.gov |
| US-MAS5-016 | Massachusetts Department of Revenue (Child Support Services) | guide | www.mass.gov |
| US-MAS5-018 | Massachusetts Department of Unemployment Assistance (EOLWD) | guide | www.mass.gov |
| US-MAS5-019 | Massachusetts Department of Revenue | technical spec | www.mass.gov |
| US-MDP51-001 | Comptroller of Maryland | guide | www.marylandcomptroller.gov |
| US-MDS5-016 | Comptroller of Maryland | technical specification | www.marylandcomptroller.gov |
| US-MDS5-017 | Maryland Department of Labor, Division of Unemployment Insurance | technical specification | labor.maryland.gov |
| US-MDS5-018 | Maryland General Assembly | statute | mgaleg.maryland.gov |
| US-MDS5-021 | Comptroller of Maryland | guide | www.marylandcomptroller.gov |
| US-MEP52-002 | Maine Revenue Services | withholding guide | www.maine.gov |
| US-MEP52-009 | Maine Revenue Services | withholding guide | www.maine.gov |
| US-MES5-011 | Maine Revenue Services | withholding guide | www.maine.gov |
| US-MES5-016 | Maine Legislature, Office of the Revisor of Statutes | statute | legislature.maine.gov |
| US-MES5-021 | Maine Department of Labor, Bureau of Unemployment Compensation | form instructions | www.maine.gov |
| US-MES5-024 | Maine Legislature, Office of the Revisor of Statutes | statute | legislature.maine.gov |
| US-MIB5-001 | Michigan Department of Health and Human Services, Child Support Divisi | authority page | www.mi-newhire.com |
| US-MIP51-002 | Michigan Department of Treasury - City Tax Administration | publication | www.michigan.gov |
| US-MIP52-005 | Michigan Unemployment Insurance Agency (LEO) | form | www.michigan.gov |
| US-MIP52-011 | Michigan Department of Treasury | form | www.michigan.gov |
| US-MIPIT-001 | Michigan Department of Treasury | guide | www.michigan.gov |
| US-MIS5-018 | Michigan Department of Treasury | form | www.michigan.gov |
| US-MIS5-021 | Michigan Department of Treasury | authority page | www.michigan.gov |
| US-MIS5-022 | Michigan LEO - Unemployment Insurance Agency | technical specification | www.michigan.gov |
| US-MNP52-005 | Minnesota Department of Revenue | authority form | www.revenue.state.mn.us |
| US-MNP6-003 | Minnesota Department of Employment and Economic Development, UI Minnes | authority page | mn.gov |
| US-MNS5-010 | Minnesota Department of Revenue | guide | www.revenue.state.mn.us |
| US-MNS5-015 | Minnesota Office of the Revisor of Statutes | statute | www.revisor.mn.gov |
| US-MNS5-016 | Minnesota Office of the Revisor of Statutes | statute | www.revisor.mn.gov |
| US-MNS5-018 | Minnesota Office of the Revisor of Statutes | statute | www.revisor.mn.gov |
| US-MOP52-007 | City of Kansas City, Missouri Finance Department | agency page | web.archive.org |
| US-MOP52-008 | Missouri DOLIR, Division of Employment Security | agency page | web.archive.org |
| US-MOS5-001 | Missouri Department of Revenue | guide | dor.mo.gov |
| US-MOS5-013 | Missouri Department of Labor and Industrial Relations, Division of Emp | agency guide | labor.mo.gov |
| US-MSS5-005 | Mississippi Department of Revenue | technical specification | www.dor.ms.gov |
| US-MSS5-006 | Mississippi Department of Human Services (State Directory of New Hires | authority page | www.ms-newhire.com |
| US-MSS5-007 | Mississippi Department of Human Services (State Directory of New Hires | authority page | ms-newhire.com |
| US-MSS5-013 | Mississippi Department of Employment Security | technical specification | mdes.ms.gov |
| US-MSS5-014 | Mississippi Department of Employment Security | authority page | mdes.ms.gov |
| US-MSS5-019 | Mississippi Department of Revenue | authority faq | www.dor.ms.gov |
| US-MTS5-005 | Montana Department of Revenue | withholding guide | revenuefiles.mt.gov |
| US-MTS5-012 | Montana Legislature (MCA 2025) | statute | mca.legmt.gov |
| US-MTS5-025 | Montana Department of Labor and Industry, Unemployment Insurance Divis | employer guide | uid.dli.mt.gov |
| US-MULTIS5-001 | US Congress / GPO | federal statute | www.govinfo.gov |
| US-MULTIS5-006 | US Congress / GPO | federal statute | www.govinfo.gov |
| US-MULTIS5-007 | US Congress / GPO | federal statute | www.govinfo.gov |
| US-MULTIS5-010 | California EDD | authority publication | edd.ca.gov |
| US-MULTIS5-011 | IRS | form instructions | www.irs.gov |
| US-MULTIS5-017 | US DOL ETA Office of Unemployment Insurance | federal guidance | www.dol.gov |
| US-MULTIS5-024 | Washington State Legislature | state statute | app.leg.wa.gov |
| US-NC-001 | NC Department of Revenue | withholding guide | www.ncdor.gov |
| US-NCP51-003 | NC Division of Employment Security | form | www.des.nc.gov |
| US-NCS5-020 | NC General Assembly (General Statutes, official host ncleg.gov) | statute | www.ncleg.gov |
| US-NCS5-025 | NC Division of Employment Security (NC Department of Commerce) | official guide | des.nc.gov |
| US-NCS5-028 | NC Department of Revenue | official guide | www.ncdor.gov |
| US-NDP51-002 | ND Office of State Tax Commissioner | form | www.tax.nd.gov |
| US-NDS5-002 | ND Office of State Tax Commissioner | guideline | www.tax.nd.gov |
| US-NDS5-011 | Job Service North Dakota | authority page | jobsnd.com |
| US-NDS5-013 | ND Department of Health and Human Services (Child Support) | authority page | www.hhs.nd.gov |
| US-NES5-010 | Nebraska Department of Revenue | withholding guide | revenue.nebraska.gov |
| US-NES5-011 | Nebraska Department of Labor | authority guide | dol.nebraska.gov |
| US-NES5-014 | Nebraska Legislature | statute | nebraskalegislature.gov |
| US-NES5-017 | Nebraska Department of Revenue | technical specification | revenue.nebraska.gov |
| US-NH-006 | NH Department of Revenue Administration | authority page | www.revenue.nh.gov |
| US-NHP6-001 | New Hampshire Employment Security | employer guide | mm.nh.gov |
| US-NHS5-006 | NH General Court | statute | gc.nh.gov |
| US-NHS5-013 | New Hampshire Employment Security (NHES) | agency guide | www.nhes.nh.gov |
| US-NJP51-001 | NJ Division of Taxation | withholding guide | www.nj.gov |
| US-NJP6-001 | City of Jersey City (Tax Collector) | municipal page | jerseycity.hosted.civiclive.com |
| US-NJR3-004 | NJ Division of Taxation | form | www.nj.gov |
| US-NJR3-005 | NJ Dept of Labor and Workforce Development | form | www.nj.gov |
| US-NJS5-017 | NJ Department of Labor and Workforce Development, Division of Employer | agency guidance | www.nj.gov |
| US-NJS5-018 | NJ Department of Human Services, Division of Family Development (New J | agency page | www.njcsesp.com |
| US-NMP51-001 | NM Department of Workforce Solutions | authority page | www.dws.nm.gov |
| US-NMP51-004 | NM Taxation and Revenue Department | form | www.tax.newmexico.gov |
| US-NMP6-001 | New Mexico Department of Workforce Solutions (Unemployment Compensatio | official form | www.dws.nm.gov |
| US-NMS5-008 | New Mexico Department of Workforce Solutions, UI Tax | authority page | www.dws.nm.gov |
| US-NMS5-010 | New Mexico New Hire Directory (state directory operated for NM; HCA Ch | portal documentation | nm-newhire.com |
| US-NMS5-012 | New Mexico Taxation and Revenue Department | authority notice | www.tax.newmexico.gov |
| US-NMS5-016 | New Mexico Department of Workforce Solutions | employer guide | www.dws.nm.gov |
| US-NVP51-001 | NV Dept of Employment, Training and Rehabilitation | authority page | detr.nv.gov |
| US-NVR3-003 | NV DETR Employment Security Division | guide | detr.nv.gov |
| US-NVS5-007 | Nevada Legislature; Nevada DETR Employment Security Division | statute | detr.nv.gov |
| US-NVS5-008 | Nevada DETR Employment Security Division | guide | detr.nv.gov |
| US-NVS5-009 | Nevada Department of Taxation | authority page | tax.nv.gov |
| US-NVS5-010 | Nevada Department of Taxation | official form | tax.nv.gov |
| US-NY-003 | NY Department of Taxation and Finance | authority page | www.tax.ny.gov |
| US-NYP9L-001 | New York State Department of Labor | agency page | dol.ny.gov |
| US-NYS5-010 | NY Department of Taxation and Finance / NY Department of Labor | withholding guide | www.tax.ny.gov |
| US-OHB5-001 | Ohio Department of Taxation | publication | dam.assets.ohio.gov |
| US-OHB5-401 | Ohio Department of Taxation | authority page | tax.ohio.gov |
| US-OHP52-003 | Ohio General Assembly (codes.ohio.gov) | statute | codes.ohio.gov |
| US-OHS5-014 | Ohio General Assembly / LSC (codes.ohio.gov) | statute | codes.ohio.gov |
| US-OHS5-018 | Ohio Department of Taxation | rate table | dam.assets.ohio.gov |
| US-OHS5-019 | Ohio Department of Taxation | rate table | dam.assets.ohio.gov |
| US-OHS5-020 | Ohio General Assembly / LSC (codes.ohio.gov) | statute | codes.ohio.gov |
| US-OK-001 | Oklahoma Tax Commission | withholding guide | oklahoma.gov |
| US-OKP51-004 | Oklahoma Tax Commission | form | oklahoma.gov |
| US-OKP51-005 | Oklahoma Employment Security Commission | form | oklahoma.gov |
| US-OKS5-007 | Oklahoma Legislature (Oklahoma Statutes, Title 40) | statute | www.oklegislature.gov |
| US-OKS5-010 | Oklahoma Legislature (Oklahoma Statutes, Title 68) | statute | www.oklegislature.gov |
| US-OKS5-020 | Oklahoma Employment Security Commission | technical specification | oklahoma.gov |
| US-OKS5-030 | Oklahoma Employment Security Commission | portal documentation | eztaxexpress.oesc.ok.gov |
| US-OR-002 | Oregon DOR / OED / DCBS | withholding guide | www.oregon.gov |
| US-ORP51-005 | Oregon Department of Revenue | form index | www.oregon.gov |
| US-ORS5-004 | City of Portland Revenue Division (for Metro and Multnomah County) | circular | www.portland.gov |
| US-ORS5-010 | Oregon Department of Revenue with OED and DCBS | technical spec | www.oregon.gov |
| US-ORS5-016 | Oregon Department of Justice, Division of Child Support | circular | www.doj.state.or.us |
| US-ORS5-024 | City of Portland Revenue Division | technical spec | www.portland.gov |
| US-PAP51-004 | PA Department of Labor & Industry - Office of UC Tax Services | authority page | www.pa.gov |
| US-PAS5-008 | Pennsylvania General Assembly (palegis.us consolidated statutes) | statute | www.palegis.us |
| US-PAS5-009 | Pennsylvania Department of Revenue | authority page | www.pa.gov |
| US-PAS5-010 | Pennsylvania Department of Revenue | technical guide | www.pa.gov |
| US-PAS5-013 | Pennsylvania Department of Labor and Industry, Office of UC Tax Servic | official guide | pa.gov |
| US-PAS5-017 | Pennsylvania General Assembly | statute | www.legis.state.pa.us |
| US-PAS5-018 | Pennsylvania Department of Community & Economic Development | authority page | dced.pa.gov |
| US-RIP51-004 | RI Division of Taxation | form | tax.ri.gov |
| US-RIS5-010 | Rhode Island General Assembly | statute | webserver.rilegislature.gov |
| US-RIS5-017 | RI Department of Labor and Training, Employer Tax Unit | authority page | dlt.ri.gov |
| US-RIS5-018 | RI Division of Taxation | technical spec | tax.ri.gov |
| US-SCP52-001 | South Carolina Department of Revenue | authority form | dor.sc.gov |
| US-SCR3-002 | SC Legislative Services Agency (Code of Regulations) | regulation | www.scstatehouse.gov |
| US-SCR3-008 | South Carolina Department of Employment and Workforce | form | dew.sc.gov |
| US-SCS5-002 | South Carolina Department of Revenue | authority page | dor.sc.gov |
| US-SCS5-006 | South Carolina Department of Employment and Workforce | technical specification | www.dew.sc.gov |
| US-SCS5-011 | South Carolina Legislature | statute | www.scstatehouse.gov |
| US-SCS5-016 | South Carolina Department of Revenue | authority page | dor.sc.gov |
| US-SDP51-001 | South Dakota Department of Labor and Regulation | form | dlr.sd.gov |
| US-SDS5-001 | South Dakota Legislature (Legislative Research Council) | statute | sdlegislature.gov |
| US-SDS5-007 | South Dakota Legislature (Legislative Research Council) | statute | sdlegislature.gov |
| US-SDS5-013 | South Dakota Department of Labor and Regulation | authority page | dlr.sd.gov |
| US-SDS5-014 | South Dakota Department of Labor and Regulation | technical spec | dlr.sd.gov |
| US-TNP51-001 | Tennessee Department of Revenue | authority page | revenue.support.tn.gov |
| US-TNR3-002 | Tennessee Dept of Labor and Workforce Development | authority page | lwdsupport.tn.gov |
| US-TNS5-005 | Tennessee Department of Labor and Workforce Development | authority page | lwdsupport.tn.gov |
| US-TNS5-007 | Tennessee Department of Labor and Workforce Development | form | www.tn.gov |
| US-TNS5-008 | Tennessee Department of Labor and Workforce Development | authority page | www.tn.gov |
| US-TXP52-008 | Texas Workforce Commission | agency page | www.twc.texas.gov |
| US-TXS5-001 | Texas Legislative Council (tcss.legis.texas.gov official statutes file | constitution | tcss.legis.texas.gov |
| US-TXS5-008 | Texas Legislative Council (tcss.legis.texas.gov) | statute | tcss.legis.texas.gov |
| US-TXS5-016 | Office of the Attorney General of Texas - Child Support Division | form | www.texasattorneygeneral.gov |
| US-TXSUI-006 | Texas Workforce Commission | authority page | www.twc.texas.gov |
| US-UTP6-002 | Utah State Tax Commission | official form | tax.utah.gov |
| US-UTP6-003 | Utah Department of Workforce Services, Unemployment Insurance | official form | jobs.utah.gov |
| US-UTR3-001 | Utah State Tax Commission | withholding guide | tax.utah.gov |
| US-UTS5-003 | Utah Department of Workforce Services (Unemployment Insurance and New | authority page | jobs.utah.gov |
| US-UTS5-004 | Utah Department of Workforce Services | authority page | jobs.utah.gov |
| US-UTS5-013 | Utah State Tax Commission via adminrules.utah.gov | admin rule | adminrules.utah.gov |
| US-UTS5-014 | Utah State Tax Commission | technical specification | tax.utah.gov |
| US-VAP51-001 | Virginia Department of Taxation | authority publication | www.tax.virginia.gov |
| US-VAP51-007 | Virginia Department of Taxation | form | www.tax.virginia.gov |
| US-VAP6-001 | Virginia Employment Commission | authority page | www.vec.virginia.gov |
| US-VAS5-006 | Virginia General Assembly (Code of Virginia); Virginia New Hire Report | statute | law.lis.virginia.gov |
| US-VAS5-009 | Virginia General Assembly (Code of Virginia) | statute | law.lis.virginia.gov |
| US-VAS5-013 | Virginia Department of Taxation (Virginia Tax) | official guide | www.tax.virginia.gov |
| US-VAS5-014 | Virginia Employment Commission (VEC) | agency faq | www.vec.virginia.gov |
| US-VTP51-012 | Vermont Department of Taxes | form | tax.vermont.gov |
| US-VTP51-013 | Vermont Department of Labor | form | labor.vermont.gov |
| US-VTP52-003 | Vermont Department of Taxes | authority page | tax.vermont.gov |
| US-VTS5-007 | Vermont General Assembly (Wayback copy 2025-04-22) | statute | legislature.vermont.gov |
| US-VTS5-014 | Vermont General Assembly (Wayback copy 2026-03-09) | statute | legislature.vermont.gov |
| US-VTS5-017 | Vermont Department of Taxes | authority publication | tax.vermont.gov |
| US-WAB5-003 | Washington Employment Security Department - Paid Family and Medical Le | technical guide | paidleave.wa.gov |
| US-WAP51-001 | City of Seattle Office of City Finance | authority page | www.seattle.gov |
| US-WAPFML-001 | Washington ESD Paid Family and Medical Leave | authority page | paidleave.wa.gov |
| US-WAS5-013 | Washington Employment Security Department | authority page | esd.wa.gov |
| US-WAS5-018 | Washington State Legislature (Code Reviser), via Wayback snapshot 2025 | statute | app.leg.wa.gov |
| US-WAS5-027 | Washington Employment Security Department | authority page | esd.wa.gov |
| US-WIP51-002 | Wisconsin Department of Workforce Development | authority form | dwd.wisconsin.gov |
| US-WIP52-003 | Wisconsin Department of Revenue | authority publication | www.revenue.wi.gov |
| US-WIS5-011 | Wisconsin Department of Revenue | authority publication | www.revenue.wi.gov |
| US-WIS5-012 | Wisconsin Department of Revenue | authority publication | www.revenue.wi.gov |
| US-WIS5-013 | Wisconsin DWD Unemployment Insurance Division | authority publication | dwd.wisconsin.gov |
| US-WIS5-014 | Wisconsin Legislature (LRB) | statute | docs.legis.wisconsin.gov |
| US-WIS5-016 | Wisconsin Department of Revenue | authority bulletin | www.revenue.wi.gov |
| US-WVP51-006 | West Virginia State Tax Department | form | tax.wv.gov |
| US-WVP52-006 | WorkForce West Virginia Unemployment Compensation Division | form | workforcewv.org |
| US-WVS5-010 | West Virginia Tax Division | authority publication | tax.wv.gov |
| US-WVS5-014 | West Virginia Tax Division | form | tax.wv.gov |
| US-WVS5-016 | WorkForce West Virginia | publication | workforcewv.org |
| US-WVS6-001 | City of Charleston, Office of the City Collector | municipal regulation | www.charlestonwv.gov |
| US-WVUI-001 | WorkForce West Virginia | authority page | workforcewv.org |
| US-WYP51-001 | Wyoming Legislature | statute | wyoleg.gov |
| US-WYS5-006 | Wyoming Legislature | statute | wyoleg.gov |
| US-WYS5-007 | Wyoming Legislature | statute | wyoleg.gov |
| US-WYS5-009 | Wyoming Department of Workforce Services | authority page | dws.wyo.gov |
| US-WYS5-019 | Wyoming Legislature | statute | wyoleg.gov |


# Appendix B. Not configured in this release

Each request number below appears in the cell it concerns; none blocks the document.

| Request | What is missing | What would close it |
|---|---|---|
| SIR-RQ-01 | Statement for Connecticut (ui.occupation hours zip) whose wording is not proven in the saved copy of its source | The authority page or form that carries the wording, saved and read |
| SIR-RQ-02 | Not read: the 2026 electronic-filing threshold in the Instructions for Forms 1094-C and 1095-C | IRS publication of the final 2026 Instructions for Forms 1094-C and 1095-C |
| SIR-RQ-03 | Not read: the 2026 Form 940 due date in the 2026 Instructions for Form 940 | IRS publication of the final 2026 Instructions for Form 940 (expected December 2026) |
| SIR-RQ-04 | Not read: the California electronic file layout of the quarterly wage detail | EDD DE 8300 annexes / FSET schema download |
| SIR-RQ-38 | Authority error-code catalogue per channel class (reject and business-rule lists) | The authority reject / business-rule lists per channel class, or an owner decision that error handling belongs to the provider contract (US-MQ-09) |
| SIR-RQ-05 | Statement for Florida (agent authorization) whose wording is not proven in the saved copy of its source | The authority page or form that carries the wording, saved and read |
| SIR-RQ-06 | Not read: the Florida agent registration form RTS-9 | the Florida Department of Revenue page or form that names the reemployment-tax agent registration (RTS-9) - floridarevenue.com Forms library |
| SIR-RQ-07 | Statement for Florida (ui.xml) whose wording is not proven in the saved copy of its source | The authority page or form that carries the wording, saved and read |
| SIR-RQ-08 | Not read: the Indiana W-2 XML schema | Indiana DOR XML schema archive, extracted and inspected |
| SIR-RQ-09 | Not read: the current Kansas Department of Revenue KW-100 withholding guide page | a live copy of kw100.html and KW-2CSV from a network that reaches ksrevenue.gov |
| SIR-RQ-10 | Not read: the Kentucky withholding and UI authorisation instruments | Kentucky DOR Form 20A100 and the KUIP TPA/agent authorization page |
| SIR-RQ-11 | Not read: the Louisiana withholding authorisation form | Louisiana LDR Form R-7006 current edition read on revenue.louisiana.gov |
| SIR-RQ-12 | Statement for Massachusetts (agent authorization) whose wording is not proven in the saved copy of its source | The authority page or form that carries the wording, saved and read |
| SIR-RQ-13 | Not read: the Massachusetts power of attorney form M-2848 | a saved copy of the mass.gov POA / third-party authorization page (browser save by an owner with access) or Form M-2848 PDF |
| SIR-RQ-14 | Not read: the Maine withholding and UI authorisation forms | Current Maine Revenue Services Form 2848-ME and Maine DOL UC-28 read on maine.gov |
| SIR-RQ-15 | Not read: the Michigan new-hire statute and penalty | MCL 400.231 et seq. text on legislature.mi.gov |
| SIR-RQ-16 | Statement for Mississippi (ui.agent authorization) whose wording is not proven in the saved copy of its source | The authority page or form that carries the wording, saved and read |
| SIR-RQ-17 | Not read: the Mississippi reporting agent authorisation form J-9 | an OCR text of the J-9 PDF or the MDES downloadable-forms page text naming Form J-9 (mdes.ms.gov downloadable forms) |
| SIR-RQ-18 | Not read: the Mississippi withholding authorisation form | Mississippi DOR Form 21-002 PDF read on dor.ms.gov |
| SIR-RQ-19 | Statement for Nebraska (agent authorization) whose wording is not proven in the saved copy of its source | The authority page or form that carries the wording, saved and read |
| SIR-RQ-20 | Not read: the Nebraska reporting agent form 33 | the Nebraska Department of Revenue Form 33 (power of attorney) PDF and the NDOL UI representative form page |
| SIR-RQ-21 | Not read: the New Hampshire third-party administrator registration | the current NHES page or form naming how a third-party administrator registers for NHUIS (nhes.nh.gov employer pages) |
| SIR-RQ-22 | Not read: the New York withholding authorisation form | Form POA-1 from tax.ny.gov/poa read on the official host |
| SIR-RQ-23 | Statement for Ohio (local.municipal) whose wording is not proven in the saved copy of its source | The authority page or form that carries the wording, saved and read |
| SIR-RQ-24 | Not read: the Ohio municipal monthly-filing thresholds | the Ohio Revised Code 718.04 / Ohio Department of Taxation municipal withholding page stating the thresholds |
| SIR-RQ-25 | Statement for Ohio (ui.agent authorization) whose wording is not proven in the saved copy of its source | The authority page or form that carries the wording, saved and read |
| SIR-RQ-26 | Not read: the Ohio Form JFS-20106 | the JFS-20106 PDF itself or a browser-rendered copy of the ODJFS tax forms page |
| SIR-RQ-27 | Not read: the choice of filing provider and its input layout | Owner/BAU RFP to candidate providers (6 questions: external file/API, IRS reporting agent, state POAs 50+DC, deposit account, local returns, SLA/penalty liability); provider-specific input spec the... |
| SIR-RQ-39 | State acknowledgement and response-time rules for electronic filings | The State authority pages that state acknowledgement and response times, saved and read |
| SIR-RQ-28 | No source recorded for agent authorization in: AR, MD, ME, MT, ND, RI | The authority's own page or form for each jurisdiction named, read on the official host |
| SIR-RQ-29 | No source recorded for programme in: DC, MA, MD | The authority's own page or form for each jurisdiction named, read on the official host |
| SIR-RQ-30 | No source recorded for new hire in: CO | The authority's own page or form for each jurisdiction named, read on the official host |
| SIR-RQ-31 | No source recorded for quarterly in: CO, OH | The authority's own page or form for each jurisdiction named, read on the official host |
| SIR-RQ-32 | No source recorded for report in: WA | The authority's own page or form for each jurisdiction named, read on the official host |
| SIR-RQ-33 | No source recorded for agent authorization in: AL, DE, MO, NC | The authority's own page or form for each jurisdiction named, read on the official host |
| SIR-RQ-34 | Not read: the Texas UI quarterly due date | TWC rule 815.107 text (40 TAC 815) read on the official host |
| SIR-RQ-35 | Not read: the UI wage-file layouts of eleven States | One official spec per state, downloaded and inspected; parallel lookups |
| SIR-RQ-36 | Not read: the tax-year State W-2 specification editions of eight jurisdictions | Re-check each state W-2 spec page in January 2027 before the first TY2026 file |
| SIR-RQ-37 | Not read: the text of the Wyoming UI power of attorney form | WY DWS POA PDF downloaded by the user |



## Fact index

Every value above with its key, effective period and register id.

| Key | Value | Effective | Register id |
|---|---|---|---|
| `dd.ak.ui.geographic_code` | 2-digit Alaska geographic code per employee | from 2016-05-17 | US-AKS5-014 |
| `dd.ak.ui.occupation_code` | 6- or 8-digit occupational code per employee | from 2016-05-17 | US-AKS5-014 |
| `dd.co.denver_opt` | Denver OPT work location and monthly earnings >=500 test | from 2025-07-31 | US-COP52-001 |
| `dd.ct.pfml.employee_level_data` | none: the CT Paid Leave return carries employer-level totals only (CT wages, CT employee counts, contributions); employee records are rejected, so no per-employee CTPL field is needed beyond the CTPL-wage computation | from 2026-10-05 | US-CTB5-001 |
| `dd.de.paid_leave.hours` | hours and wages per employee for Delaware Paid Leave quarterly report | from 2025-01-01 | US-DES5-013 |
| `dd.employer.ny_mctmt_zone` | MCTMT zone payroll | from 2025-07-01 | US-NY-003 |
| `dd.employer.state_account_ids` | per-state withholding account / UI account / paid-leave account ids (e.g. UT 14-digit number ending in WTH; KS 036#######F##; MD Central Registration Number in RS positions 338-345; IA 9-digit permit number) | from 2026-01-01 | US-UTR3-001 |
| `dd.fed.depositor_status.codes` | Form 941 deposit schedule names: monthly schedule depositor; semiweekly schedule depositor (from the lookback period: $50,000 or less = monthly; more than $50,000 = semiweekly) | from 2026-01-01 | US-FEDS5-004 |
| `dd.fed.new_hire.date_first_services` | date services first performed (new-hire report federal minimum) | from 1997-10-01 | US-FEDS5-024 |
| `dd.fed.w2.tipped_occupation_code` | Treasury Tipped Occupation Code per employee (W-2 box 14b, TY2026) | from 2026-01-01 | US-FEDS5-007 |
| `dd.fl.everify_certified` | E-Verify certification (private employers 25+), certified on first RT-6 of the year | from 2023-07-01 | US-FLS5-010 |
| `dd.fl.ssn_not_itin` | SSN required on RT-6; ITIN not accepted | from 2026-01-01 | US-FLS5-024 |
| `dd.ga.new_hire.extra` | Employee's Date of Birth, Employee's Medical Insurance availability, Employee's State of Hire | from 1998-10-01 | US-GAS5-012 |
| `dd.ia.new_hire.health` | whether the employer has employee dependent health care coverage available and the appropriate date on which the employee may qualify for the coverage; the address to which income withholding orders or the notices of orders and garnishments should be sent | from 1998-07-01 | US-IAS5-012 |
| `dd.ia.school_district_residence` | Iowa school district of residence (surtax at assessment; IA W-4 note) | from 2026-01-01 | US-IAP52-001 |
| `dd.in.county_residence_jan1` | Indiana county of residence and county of principal employment on Jan 1 (WH-4) | from 2026-01-01 | US-INS5-021 |
| `dd.in.new_hire.job_comp` | job title, SOC, starting compensation, rate-of-pay basis | from 2024-07-01 | US-INS5-016 |
| `dd.in.ui.soc_start_date` | SOC code (6 digits) and start date per worker | from 2025-07-01 | US-INS5-014 |
| `dd.ky.locality` | Kentucky locality of work (Louisville Metro) and residence (school board component) | from 2026-01-01 | US-KYP9W-001 |
| `dd.la.new_hire.occupation` | occupation | from 2026-01-01 | US-LAS5-010 |
| `dd.ma.ui.hours_work_location` | hours worked, work location, 12th-of-month employment, adjustment reason code | from 2026-01-01 | US-MAS5-018 |
| `dd.md.county_residence` | Maryland county of residence (local rate tables) via MW507 | from 2026-01-01 | US-MDP51-001 |
| `dd.md.naics` | NAICS code (employer) in MW508 RV record | from 2026-01-01 | US-MDS5-016 |
| `dd.md.new_hire.wage_health` | starting wage, employer health insurance offered, MD UI account number | from 2026-01-01 | US-MDS5-018 |
| `dd.mi.city_residence_work` | Michigan city (e.g. Detroit) resident / nonresident predominant place of employment; DW-4 | from 2026-01-01 | US-MIP51-002 |
| `dd.mn.ui.paid_hours` | total paid hours worked per quarter (exempt FT = 40 h/week) | from 2026-01-01 | US-MNS5-015 |
| `dd.mo.ui.separation_probation` | separation dates and probationary flag P with dates (28 days or less) | from 2026-01-01 | US-MOS5-013 |
| `dd.ms.new_hire.extra` | Date of birth, gender, salary, payment frequency and medical insurance eligibility (required employee fields of the Mississippi new hire report beyond name, address, SSN and date of hire) | from 1998-10-01 | US-MSS5-007 |
| `dd.multi.residence_state` | residence state (drives resident withholding; interstate transport workers are subject to withholding only by their State of residence under 49 U.S.C. 14503) | from 1996-01-01 | US-MULTIS5-001 |
| `dd.multi.sui_state` | single UI state per employee per period under the localization test; also applies to WA family and medical leave (RCW Title 50A) | from 2026-01-01 to 2027-06-30 | US-MULTIS5-024 |
| `dd.multi.work_state` | work state where the service is localized (UI localization of work, UIPL 20-04) | from 2026-01-01 | US-MULTIS5-017 |
| `dd.ne.ui.hours_job_title` | hours and job title (optional) | from 2025-09-11 | US-NES5-011 |
| `dd.nj.ui.base_weeks` | base weeks per employee (week >= 20 x prior-year minimum wage) | from 2026-01-01 | US-NJS5-017 |
| `dd.ny.employee_primary_language` | employee primary language for the Labor Law 195.1 pay-rate/payday notice (English + primary language) | from 2026-01-01 | US-NYP9L-001 |
| `dd.ny.nyc_yonkers_residence` | NYC / Yonkers resident status and resident period | from 2026-01-01 | US-NYS5-010 |
| `dd.oh.municipality_work` | Ohio municipality of work (718.03) and residence; collector: the central collection agency, the regional income tax agency or the municipal tax administrator | from 2016-09-14 | US-OHP52-003 |
| `dd.oh.school_district_code` | four-digit Ohio school district code of residence (9999 full-year nonresident); W-2 and SD 101/141 | from 2026-01-01 | US-OHB5-401 |
| `dd.oh.ui.weeks_paid` | number of weeks paid per employee | from 2014-09-15 | US-OHS5-020 |
| `dd.or.form132.hours` | employee wage and hour detail (Form 132) | from 2026-01-01 to 2026-12-31 | US-ORS5-010 |
| `dd.or.metro_multnomah` | Metro SHS / Multnomah PFA work location and opt-in/opt-out | from 2022-01-01 | US-ORS5-004 |
| `dd.or.transit_district` | TriMet / Lane transit district of work | from 2026-01-01 to 2026-12-31 | US-ORS5-010 |
| `dd.pa.psd_code` | PA PSD code of work location and of residence (looked up with the DCED Address Search Application) | from 2018-05-04 | US-PAS5-017 |
| `dd.pa.ui.credit_weeks` | credit weeks per employee (week with remuneration >= 116) | from 2023-09-01 | US-PAS5-013 |
| `dd.state.new_hire.dob` | date of birth required by GA, IA, ME, MS, NJ, OH, OR, WA, WI, WV new-hire reports | from 2026-01-01 | US-NJS5-018 |
| `dd.state.new_hire.rehire_gap_days` | 60 | from 2026-01-01 | US-CTS5-019 |
| `dd.state.ui.month12_count` | covered on payroll in the pay period including the 12th of each month (employer monthly counts) | from 2026-01-01 | US-FLS5-021 |
| `dd.state.ui.out_of_state_wages` | wages reported to other states in the year (excess wage computation) | from 2026-01-01 | US-MULTIS5-010 |
| `dd.tx.ui.enhanced` | industry, occupation, full/part-time, county of primary employment, remote-work status | from 2026-01-01 | US-TXS5-008 |
| `dd.vt.ui.gender_hourly` | gender and hourly wage for hourly workers | from 2026-01-01 | US-VTS5-007 |
| `dd.wa.exempt_officer` | corporate officer without voluntary UI coverage flag | from 2026-01-01 | US-WAS5-027 |
| `dd.wa.pfml_ltc.employee_fields` | Per employee for the Paid Leave/WA Cares report: date of birth, WA Cares exemption status (approved exemption letter), quarterly hours associated with wages (rounded up) | from 2026-06-26 | US-WAB5-003 |
| `dd.wa.ui.soc_code` | SOC code per employee | from 2026-01-01 | US-WAS5-013 |
| `dd.wv.ui.soc_county` | SOC or job title and county per employee | from 2026-01-01 | US-WVUI-001 |
| `fed.aca.efile_threshold` | 10 | from 2025-01-01 | US-FEDS5-012 |
| `fed.deposit.monthly_max_lookback_liability` | 50,000 | from 2026-01-01 | US-FEDS5-004 |
| `fed.deposit.next_day_threshold` | 100,000 | from 2026-01-01 | US-FEDS5-004 |
| `fed.form1042s.channel` | IRIS (FIRE retired for TY2026); due 2027-03-15 | from 2026-01-01 | US-FEDS5-016 |
| `fed.iwo.omb_expiry` | 2029-08-31 | from 2026-08-25 to 2029-08-31 | US-FEDS5-028 |
| `fed.iwo.priority` | Withholding for support has priority over any other legal process under state law against the same income (section 466(b)(7) of the Social Security Act); if a federal tax levy is in effect, notify the sender | from 2026-01-01 to 2026-12-31 | US-FEDP6-002 |
| `fed.levy.exempt.single_0dep.monthly` | 1341.67 | from 2026-01-01 to 2026-12-31 | US-FEDS5-014 |
| `in.report.w2.efile_threshold` | 25 | from 2026-01-01 | US-INS5-011 |
| `ks.newhire.report_business_days` | 20 | from 2026-01-01 | US-KSS5-019 |
| `ky.newhire.report_days` | 20 | from 2025-07-01 | US-KYS5-020 |
| `ms.report.w2.efile_threshold` | 10 | from 2026-01-01 | US-MSS5-005 |
| `multi.iwo.governing_law` | When an employer receives an income withholding order issued by another State, the employer shall apply the income withholding law of the State of the obligor's principal place of employment in determining the employer's fee for processing an income withholding order; the maximum amount permitted to be withheld from the obligor's income; the time periods within which the employer must implement the income withholding order and forward the child support payment; the priorities for withholding and allocating income withheld for multiple child support obligees; and any withholding terms or conditions not specified in the order | from 2026-01-01 | US-MULTIS5-007 |
| `multi.iwo.remittance_business_days` | 7 | from 2026-01-01 | US-MULTIS5-007 |
| `ne.report.w2.efile_threshold` | 50 | from 2025-11-01 | US-NES5-017 |
| `oh.newhire.report_days` | 20 | from 2013-09-29 | US-OHS5-014 |
| `ri.report.w2.efile_threshold` | 25 | from 2026-01-01 to 2026-12-31 | US-RIS5-018 |
| `rspec.ak.ui_qtr.form` | TQ01C (2/26) with wage schedule | from 2026-01-01 | US-AKS5-013 |
| `rspec.ar.ui_qtr.form` | DWS-ARK-209B / 209BR / 209BS via Tax21 or paper | from 2024-07-01 | US-ARP9V-001 |
| `rspec.az.w2_state.ssn_truncation` | SSNs and EINs must not be truncated | from 2026-01-01 | US-AZS5-025 |
| `rspec.ca.ui_qtr.file_formats` | DE 9C electronic options (DE 8300 Rev. 12 (7-24)): e-Services for Business direct entry or CSV import; Upload Bulk Return File (zip, max 10 MB) in XML, ICESA or MMREF-1; FSET bulk transmission (XML web service). CSV fields: SSN, first name, MI, last name, total subject wages, PIT wages, PIT withheld, wage plan code (A, J, L, P, R, S, U). Third-party representative needs its own e-Services login; no test environment for bulk formats; penalty 20 USD per wage item not filed electronically | from 2024-07-01 | US-FIL-006 |
| `rspec.ca.ui_qtr.form` | DE 9 + DE 9C (per employee subject wages, PIT wages, PIT withheld); corrections DE 9ADJ | from 2026-01-01 to 2026-12-31 | US-CAS5-002 |
| `rspec.co.pfml_qtr.form` | FAMLI wage report and premium payment per quarter (2026 Q3 deadline October 31) | from 2026-01-01 | US-COS5-008 |
| `rspec.co.w2_state.due` | Jan 31 to employees and the Colorado Department of Revenue | from 2026-01-01 | US-COS5-006 |
| `rspec.co.w2_state.format` | electronic: Submit a Manual Withholding File, or upload an electronic file in .txt format (Submit a Withholding File Attachment); CDOR Year-End W-2 info return template held | from 2026-01-01 | US-COS5-006 |
| `rspec.ct.ui_qtr.layout` | 276-character fixed-length .txt; S record per employee (start/length: SSN 2/9, last name 11/20, first name 31/12, middle initial 43/1, state code 44/2 = 09, quarter and year 46/6, total wages 64/14, taxing entity code 143/4 = WAGE, employer account number 147/10); T record per employer | from 2022-07-01 | US-CTS5-032 |
| `rspec.ct.w2_state.form` | CT-W3 + all W-2s by Jan 31 via myconneCT: key-and-send, EFW2 upload or DRS CSV | from 2026-01-01 | US-CTS5-013 |
| `rspec.dc.pfml_qtr.channel` | PFL quarterly wage filing and tax payment via the Employer Self-Service Portal (ESSP); due April 30 (Q1), July 31 (Q2), October 31 (Q3), January 31 (Q4) | from 2026-01-01 | US-DCS5-019 |
| `rspec.dc.wh_return.form` | FR-900Q quarterly on MyTax.DC.gov (e-file mandatory since TY2023); due Apr 30/Jul 31/Oct 31/Jan 31; zero return required | from 2026-01-01 | US-DCS5-014 |
| `rspec.fed.aca.ty2026_due` | TY2026: file 1094-C/1095-C with IRS by March 1, 2027 (paper) or 2027-03-31 (electronic); furnish 1095-C to employees by 2027-03-02 (automatic extension from 2027-01-31; alternative website notice possible) | from 2026-01-01 | US-FEDS6-006 |
| `rspec.fed.form940.due` | TY2025 rule: Form 940 for 2025 due February 2, 2026 (February 10, 2026 if all FUTA tax was deposited when due) (TY2025 rule, re-verify on the 2026 instructions) | from 2026-01-01 to 2026-02-10 | US-FEDS5-031 |
| `rspec.fed.form941x.deadlines` | Underreported: file by the due date of the return for the period in which the error was discovered and pay by filing (interest-free). Period of limitations: overreported - 3 years from the date Form 941 was filed or 2 years from payment, whichever later; underreported - 3 years from filing; Forms 941 for a year are deemed filed on April 15 of the following year. | from 2026-01-01 | US-FEDS6-007 |
| `rspec.fed.form941x.process_rule` | Adjustment process (line 1): underreported tax (pay with the 941-X), or overreported tax applied as a credit to the Form 941 for the period in which the 941-X is filed; required when correcting both under- and over-reported amounts. Claim process (line 2): overreported tax only, refund or abatement. Overreported corrections in the last 90 days of the period of limitations must use the claim process (and a separate 941-X for any underreported amounts). One 941-X per quarter corrected. | from 2026-01-01 | US-FEDS6-007 |
| `rspec.fed.form943.due` | For 2026: file Form 943 by 2027-02-01; by February 10, 2027 if deposits were made on time in full payment of the year's taxes | from 2026-01-01 | US-FEDS6-004 |
| `rspec.fed.form944.due` | For 2026: file Form 944 by 2027-02-01; by February 10, 2027 if all deposits were made on time in full | from 2026-01-01 | US-FEDS6-003 |
| `rspec.fed.form944.rule` | annual, only on written IRS notice, liability of 1,000 or less | from 2026-01-01 | US-FEDS5-004 |
| `rspec.fed.schedule_h.due` | 2027-04-15 (with the 2026 Form 1040/1040-SR/1040-SS/1040-NR/1041; extension of the return extends Schedule H; stand-alone if no return) | from 2026-01-01 | US-FEDS6-010 |
| `rspec.hi.tdi.state_return` | False | from 2026-01-01 | US-HIS7-001 |
| `rspec.hi.w2_state.format` | HTO Simple File Import (maximum 1,000 employee records per submission), manual entry on HTO, SSA file upload method, or Hawaii Bulk Filing System | from 2026-01-01 | US-HIS5-005 |
| `rspec.ia.w2_state.due` | Feb 15, only W-2s/1099s carrying Iowa withholding; must be filed electronically (GovConnectIowa) | from 2026-01-01 | US-IAS5-017 |
| `rspec.ks.ui_qtr.format` | MMREF / NASWA upload; K-CNS-100 by mail for 25 or fewer employees (26 or more must file online) | from 2026-01-01 | US-KSS5-022 |
| `rspec.ky.ui_qtr.upload_formats` | KUIP quarterly wage report methods: zero payroll report, file upload in ICESA or CSV format, manual entry, copy-and-modify a prior quarter; KUIP computes the tax | from 2026-01-01 | US-KYS6-001 |
| `rspec.ky.w2_state.efile_threshold` | 26 | from 2026-03-01 | US-KYS5-013 |
| `rspec.la.annual_recon.form` | L-3 + W-2s on or before first business day after Jan 31; within 30 days on closure | from 2026-06-30 | US-LAS5-003 |
| `rspec.la.ui_qtr.due` | last day of month after quarter; domestic annual Jan 31; mandatory electronic (LWC online services) | from 2026-01-01 | US-LAS5-007 |
| `rspec.ma.ui_qtr.format` | CSV, EFW2 or ICESA upload (DUA) | from 2026-01-01 | US-MAS5-018 |
| `rspec.me.ui_qtr.form` | ME UC-1 quarterly via ReEmployME; monthly employment for the 12th, gross/excess/taxable wages, UC rate, CSSF, UPAF; filed with the Maine Department of Labor | from 2026-01-01 to 2026-12-31 | US-MES5-021 |
| `rspec.me.w2_state.due` | electronically with MRS by Jan 31; paper not accepted | from 2026-01-01 to 2026-12-31 | US-MES5-011 |
| `rspec.mi.local.detroit` | Detroit monthly return Form 5323 (15th) and annual reconciliation Form 5321 TY2026 due 2027-02-28; DW-4 certificate | from 2026-01-01 | US-MIP51-002 |
| `rspec.mi.ui_qtr.formats` | MiUI four formats: Delimited CSV (2026 spec v3, 2026-04-08), ICESA (v2), EFW2 (v2 2026-04-03, RE/RS 512-byte UIA profile), XML (v1 2026-02-23); MiWAM legacy refused | from 2026-02-23 | US-MIS5-022 |
| `rspec.mn.pfml_qtr.form` | Paid Leave quarterly wage detail and premium to the commissioner (Minnesota Department of Employment and Economic Development), electronic | from 2026-01-01 | US-MNS5-018 |
| `rspec.mn.w2_state.due` | W-2 information to the Minnesota Department of Revenue by Jan 31; e-Services mandatory above 10 W-2 + 1099 | from 2026-01-01 to 2026-12-31 | US-MNS5-010 |
| `rspec.mo.local.kansas_city` | Kansas City 1% earnings tax; RD-100 registration | from 2026-01-01 | US-MOP52-007 |
| `rspec.ms.ui_qtr.format` | ICESA S record 275 chars (UIWAGE.TXT) or MMREF-1 "RS" record (now SSA EFW2) with required positions 1-2, 3-4, 10-18, 19-68, 197-202, 203-213, 248-267 | from 2012-02-01 | US-MSS5-013 |
| `rspec.mt.annual_recon.form` | MW-3 + all W-2s due Jan 31; federal W-3 not accepted; no truncated SSNs | from 2026-01-01 | US-MTS5-005 |
| `rspec.nc.ui_qtr.form` | Quarterly Tax and Wage Report filed online in NCSUITS, Apr 30 / Jul 31 / Oct 31 / Jan 31; online filing required at ten or more employee wage items; Zero report when no wages and business continues | from 2026-01-01 | US-NCS5-025 |
| `rspec.nc.wh_return.form` | NC-5: quarterly <250/month; monthly 250-<2,000 (15th); semiweekly >=2,000 (NC-5P) + NC-5Q quarterly | from 2026-01-01 | US-NC-001 |
| `rspec.nd.annual_recon.form` | Form 307 + W-2 due Jan 31; e-file of 307 required even with zero W-2s | from 2026-01-01 | US-NDS5-002 |
| `rspec.nj.annual_recon.form` | NJ-W-3 by Feb 15 (or 30 days after wages stop); W-2 electronic since TY2020 (online, upload, Axway 100+) | from 2026-01-01 | US-NJP51-001 |
| `rspec.nm.efile.mandate` | TRD-41414, TRD-41431, TRD-41409 e-file and e-pay from 2026 | from 2026-01-01 | US-NMS5-012 |
| `rspec.nm.ui_qtr.formats` | Delimited, ICESA, XML, EFW2; electronic only; last day of month after quarter | from 2026-01-01 | US-NMS5-008 |
| `rspec.nm.wh_qtr_report.form` | TRD-41431 (new 2026-01-01): WC fee return + employee quarterly wage and withholding report, 25th after quarter | from 2026-01-01 | US-NMS5-012 |
| `rspec.ny.mctmt.form` | MTA-305 quarterly | from 2025-07-01 | US-NY-003 |
| `rspec.oh.annual_recon.form` | IT 941 by Jan 31; W-2/1099 upload (OH\\|TAX Upload Income Statement) by Jan 31; CD eliminated | from 2026-01-01 | US-OHB5-401 |
| `rspec.ok.ui_qtr.format` | ICESA fixed 275-character ASCII CR/LF; E, S, T required, P optional (only when more than one OK UI account is used, typically by third-party administrators); S: name as on SS card in upper case, SSN, total and taxable wages | from 2024-10-01 | US-OKS5-020 |
| `rspec.ok.w2_state.format` | EFW2 upload (SSA 42-007) or manual entry via OkTAP by Jan 31; no magnetic media/paper | from 2026-01-01 | US-OK-001 |
| `rspec.pa.annual_recon.form` | REV-1667 Annual Withholding Reconciliation with W-2s; electronic through myPATH when filing 10 or more income statements; paper or myPATH below 10 | from 2026-01-01 | US-PAS5-009 |
| `rspec.pa.ui_qtr.layout` | UC-2010 ICESA/CSV | from 2025-11-01 | US-FIL-008 |
| `rspec.ri.annual_recon.form` | RI W-3 due Jan 31 | from 2026-01-01 | US-RIS5-018 |
| `rspec.ri.ui_qtr.efile_threshold` | 25 | from 2022-04-11 | US-RIS5-017 |
| `rspec.ri.ui_qtr.form` | TX-17 Quarterly Tax and Wage Report (Employment Security, TDI, Job Development fund), one report and payment; Jan 31 / Apr 30 / Jul 31 / Oct 31; zero report required | from 2022-04-11 | US-RIS5-017 |
| `rspec.sc.w2_state.efile_threshold` | 10 | from 2026-01-01 | US-SCS5-016 |
| `rspec.sc.w2_state.format` | EFW2 .txt (SSA Publication 42-007) with the SCDOR state record per RS-1 (full SSN), or Excel template (up to 30 employees), or manual entry | from 2026-01-01 | US-SCS5-016 |
| `rspec.sd.ui_qtr.form` | Form 21 quarterly RA wage report, received by Apr 30 / Jul 31 / Oct 31 / Jan 31; zero reports required; corrections 21C | from 2026-01-01 | US-SDS5-013 |
| `rspec.sd.ui_qtr.layout` | CD/DVD 85-byte E and S records; S: social security no., names, total and taxable wages (2 implied decimals), state code 46, DLR account | from 2026-01-01 | US-SDS5-014 |
| `rspec.tn.wh_return.applicable` | False | from 2025-05-27 | US-TNP51-001 |
| `rspec.ut.annual_recon.due` | with Q4/annual return Jan 31, electronic with all W-2s and 1099s, even with zero activity | from 2026-06-01 | US-UTR3-001 |
| `rspec.vt.annual_recon.form` | WHT-434 by Jan 31, transmittal for W-2/1099; e-file at 10+ forms and always for payroll services; no CF/SF | from 2026-01-01 to 2026-12-31 | US-VTS5-017 |
| `rspec.wa.pfml_ltc_qtr.form` | combined Paid Leave + WA Cares quarterly report (wages and hours) on paidleave.wa.gov | from 2026-01-01 | US-WAPFML-001 |
| `rspec.wi.ui_qtr.efile_threshold` | 25 | from 2013-01-01 | US-WIS5-014 |
| `rspec.wv.annual_recon.form` | IT-103 + state W-2 by Jan 31 via MyTaxes (Letter of Intent) | from 2025-01-01 | US-WVS5-010 |
| `rspec.wv.local.charleston.service_fee_return` | Charleston City Service Fee: 3.00 per calendar week (Sun-Sat, no proration) withheld by employer; Form CSF-2 City Service Fee Return with each remittance; calendar-quarter reporting periods (ending March 31, June 30, September 30, December 31); fees remitted to the City Collector before the expiration of one month from the end of the reporting period; the regulations state no filing channel (City Collector, 915 Quarrier Street, Charleston); CSF-1 prior payment, CSF-3 refund (3 years) | from 2018-01-15 | US-WVS6-001 |
| `rspec.wv.wh_return.form` | IT-101Q quarterly, last day of month after quarter, even nil; remit by 15th; annual IT-101A <600/yr | from 2026-01-01 | US-WVS5-014 |
| `rspec.wy.wc_report.frequency` | workers compensation payroll report monthly (quarterly by permission), joint UI/WC reporting | from 2026-05-08 | US-WYS5-007 |
| `sir.ak.new_hire.days` | 20 | from 2022-06-02 | US-AKS5-007 |
| `sir.ak.ui.agent_authorization` | UI Tax Power of Attorney (Rev. 7/24), eight checkable areas | from 2024-07-01 | US-AKP51-006 |
| `sir.ak.ui.csv_layout` | Header record 11 columns + wage detail record 12 columns (rev. 2016-05-17) | from 2016-05-17 | US-AKS5-014 |
| `sir.ak.ui.online_mandate` | Contribution reports must be filed via Internet when a wage schedule lists 50 or more employees in a quarter; $1 million or more in taxable wages in the current or preceding calendar year; or a payroll agent reports on behalf of an employer | from 2025-05-05 | US-AKS5-005 |
| `sir.ak.withholding.return` | none: no state wage tax | from 2026-01-01 | US-AKWT-001 |
| `sir.al.local.occupational_tax` | Municipal occupational taxes filed with each city/county or its agent (e.g. Leeds via Avenu, Birmingham via HdL) | from 2026-01-01 | US-ALS5-017 |
| `sir.al.new_hire.days` | 7 | from 2026-01-01 | US-ALS5-008 |
| `sir.al.ui.agent_authorization` | Department of Workforce UC Power of Attorney (rev. 02/2025): TAX, BENEFITS, TAX AND BENEFITS, TAX REPORTS ONLY | from 2025-02-01 | US-ALP52-002 |
| `sir.al.ui.wage_report` | Quarterly Contribution and Wage Report via eGov (online_form or file_upload); computer-generated paper not accepted; corrections UC-10C | from 2026-01-01 | US-ALS5-007 |
| `sir.al.w2.efile_threshold` | 10 | from 2024-08-01 | US-ALS5-006 |
| `sir.al.w2.format` | EFW2 RS record only, 512 bytes; RS includes federal income tax withheld cols 298-307 | from 2024-08-01 | US-ALS5-006 |
| `sir.al.withholding.returns` | A-6 monthly (if >1,000 withheld in month 1 or 2 of quarter, due 15th); A-1 quarterly; A-3 annual reconciliation + W-2s by 31 January; My Alabama Taxes | from 2026-01-01 | US-ALS5-001 |
| `sir.ar.new_hire.days` | 20 | from 2024-07-01 | US-ARP9V-001 |
| `sir.ar.w2.efile_threshold` | 125 | from 2026-01-01 | US-ARP51-002 |
| `sir.ar.w2.format` | EFW2 (RA, RE, RW, RS, RT, RF, RCS required; RV not allowed) via ATAP bulk upload, due 31 Jan with ARW-3 | from 2026-01-01 | US-ARP51-002 |
| `sir.ar.withholding.agent_authorization` | DFA Power of Attorney (rev. September 2025) | from 2025-09-01 | US-ARP52-003 |
| `sir.ar.withholding.returns` | AR941M monthly by 15th (new registrations); AR941A annual by 31 Jan if under 1,000; AR3MAR annual reconciliation 28 Feb; EFT mandatory at 20,000/month average | from 2026-01-01 | US-ARP51-002 |
| `sir.az.new_hire.days` | 20 | from 2026-01-01 | US-AZS5-012 |
| `sir.az.ui.agent_authorization` | DES UIT-1146A Limited Power of Attorney | from 2026-01-01 | US-AZP52-002 |
| `sir.az.ui.wage_report` | UC-018 quarterly via DES Tax and Wage System (online) or bulk file; due last day of month after quarter; zero report required | from 2026-01-01 | US-AZB5-005 |
| `sir.az.w2.format` | Electronic mandatory: EFW2 .txt via AZTaxes/AZFSET or transmitter; RS required, RV optional, state code 04; SSN/EIN not truncated | from 2026-01-01 | US-AZS5-025 |
| `sir.az.withholding.agent_authorization` | Form 821-PSC Withholding Tax Payroll Service Company Authorization | from 2026-01-01 | US-AZP52-001 |
| `sir.az.withholding.returns` | A1-QRT quarterly (even zero); A1-R annual reconciliation with W-2s by 31 Jan; A1-APR annual payment filers under 200; EFT at 500+ | from 2026-01-01 | US-AZP52-005 |
| `sir.ca.agent_authorization` | DE 48 Power of Attorney Declaration (e-Services or mail) | from 2024-04-01 | US-CAEDD-006 |
| `sir.ca.de9c.efile_spec` | DE 8300 e-file guide: Upload Bulk Return File (zip <=10 MB) XML, ICESA or MMREF-1, CSV, or FSET XML web service | from 2024-07-01 | US-FIL-006 |
| `sir.ca.new_hire.days` | 20 | from 2026-01-01 to 2026-12-31 | US-CAS5-002 |
| `sir.ca.ui_pit.returns` | DE 9 + DE 9C quarterly, electronic only (per employee subject wages, PIT wages, PIT withheld); DE 88 deposits on the federal schedule; no annual reconciliation; W-2 NOT filed with EDD/FTB | from 2026-01-01 to 2026-12-31 | US-CAS5-018 |
| `sir.co.local.denver_opt` | Denver Occupational Privilege Tax withheld by employer, returned to Denver Treasury | from 2025-07-31 | US-COP52-001 |
| `sir.co.ui.agent_authorization` | Employers can assign a TPA online in MyUI Employer+ (Account Maintenance dropdown > Third Party Administrator (TPA) authorization link); only employers can assign a TPA to an employer account | from 2026-01-01 | US-COP52-003 |
| `sir.co.withholding.agent_authorization` | DR 0145 Tax Information Designation and Power of Attorney | from 2026-01-01 | US-COP51-006 |
| `sir.co.withholding.returns` | Quarterly (<7,000/yr), monthly (7,000-50,000), weekly (>=50,000, EFT); zero returns required; DR 1094 paper | from 2026-01-01 | US-COS5-006 |
| `sir.ct.new_hire.days` | 20 | from 2026-01-01 | US-CTS5-019 |
| `sir.ct.paid_leave.bulk_format` | Batch XML (XSD) or CSV via SFTP per File Specification Toolkit v2.1.9; employer-level return totals only; acknowledgement file E/W | from 2026-10-05 | US-CTB5-001 |
| `sir.ct.paid_leave.return` | CT Paid Leave quarterly return via portal or batch return files in two file formats: XML or CSV | from 2026-01-01 | US-CTS5-022 |
| `sir.ct.ui.agent_authorization` | TPA Certificate of Representation (COR) and client link in ReEmployCT | from 2026-01-01 | US-CTP52-002 |
| `sir.ct.ui.wage_report` | Quarterly via ReEmployCT (entry, upload, TPA, FSET); 276-character fixed-length S/T records; optional occupation, hours, worksite ZIP from Q3 2026 | from 2022-07-01 | US-CTS5-032 |
| `sir.ct.withholding.agent_authorization` | DRS LGL-001 / LGL-003 | from 2026-01-01 | US-CTP51-007 |
| `sir.ct.withholding.returns` | CT-941 quarterly via myconneCT even with zero; remitter class weekly/monthly/quarterly by 12-month lookback; CT-W3 + all W-2s by 31 Jan (key-and-send, EFW2 upload or DRS CSV) | from 2026-01-01 | US-CTS5-013 |
| `sir.dc.new_hire.days` | 20 | from 2026-01-01 | US-DCS5-022 |
| `sir.dc.ui.agent_authorization` | Power of Attorney, Form No. OUCTAX-1, District of Columbia Department of Employment Services | from 2026-01-01 | US-DCP52-003 |
| `sir.dc.ui.wage_report` | UC-30 quarterly via DOES ESSP; machine-readable mandatory at 250+ employees; PFL same channel | from 2026-01-01 | US-DCS5-018 |
| `sir.dc.w2.efile_threshold` | 25 | from 2025-01-01 | US-DCS5-015 |
| `sir.dc.w2.format` | EFW2/EFW2C with required RS record via MyTax.DC.gov, due 31 Jan; TY2025 edition read | from 2025-01-01 | US-DCS5-015 |
| `sir.dc.withholding.agent_authorization` | OTR D-2848 | from 2026-09-16 | US-DCP51-014 |
| `sir.de.local.wilmington` | Wilmington earned income tax 1.25% collected by the City | from 1978-07-01 | US-DEP52-001 |
| `sir.de.new_hire.days` | 20 | from 2026-01-01 | US-DES5-005 |
| `sir.de.paid_leave.return` | Quarterly Hours & Wage Report and contributions in Delaware LaborFirst | from 2025-01-01 | US-DES5-013 |
| `sir.de.ui.agent_authorization` | DUI Power of Attorney (UI); withholding representation by IRS 2848 only | from 2026-01-01 | US-DEP52-002 |
| `sir.de.ui.wage_report` | UC-8 tax report + UC-8A wage report, quarterly, Online Employer Services Portal | from 2026-01-01 | US-DES5-011 |
| `sir.de.w2.format` | EFW2 with Delaware RS records via the Delaware Taxpayer Portal; SSN not truncated; paper only for 10 or fewer | from 2026-01-01 | US-DES5-008 |
| `sir.de.withholding.returns` | Quarterly / monthly / eighth-monthly by lookback period (statutory thresholds 4,500 / 25,000, subject to annual adjustment); WTH-REC Annual Reconciliation/Transmittal filed on or before the last day of January with a duplicate of each W-2 | from 2026-01-01 | US-DES5-005 |
| `sir.fed.941.due` | Quarterly, last day of the month after the quarter; amounts in cents; 944 only on IRS written notice (liability 1,000 or less) | from 2026-01-01 | US-FEDS5-004 |
| `sir.fed.agent_authorization.employer_liability_retained` | True | from 2012-11-19 | US-FED-008 |
| `sir.fed.agent_authorization.form` | Form 8655 Reporting Agent Authorization (Rev. 1-2024), one per EIN | from 2024-01-01 | US-FED-028 |
| `sir.fed.agent_authorization.returns` | Line 15: 940, 941, 943, 944, 945, 1042, CT-1; line 16 deposits; line 19 extends the authorisation to state/local returns related to lines 15/16 | from 2024-01-01 | US-FED-028 |
| `sir.fed.deposit.lookback_period` | 2024-07-01 to 2025-06-30 for calendar 2026 | from 2026-01-01 | US-FEDS5-004 |
| `sir.fed.efw2.employer_signature_pin` | Optional RE 319-328 Employer Signature PIN (S-XXXXXX-Y, Luhn) requested by the employer from SSA to sign wage reports electronically; blanks if none | from 2026-01-01 | US-FEDS5-032 |
| `sir.fed.efw2.layout_ty2026` | SSA Publication No. 42-007, EFW2 Tax Year 2026 (page header dated 2026-09-14; no version change entries yet). 512-byte records in order RA, RE, RW, (RO), (RS), RT, (RU), (RV), RF; RA/RE/RW/RT/RF required; RO/RS/RU/RV optional; RS and RV are not read or processed by SSA or IRS (state-defined). TY2026 changes: RE adds Employer Signature PIN (319-328); RW adds Box 14b Primary/Secondary Treasury Tipped Occupation Code (490-492 / 493-495); RO/RU split Codes A and B into separate money fields (combined A+B field valid through TY2025 only), add money fields for existing Codes J, K, L, P and new Codes TA, TP, TT; SS wage base 184,500; FIRE replaced by IRIS | from 2026-01-01 | US-FEDS5-032 |
| `sir.fed.efw2.state_records` | Provider must build RS per state spec on the TY2026 base layout: state employer account 248-267, state code 274-275, state wages/tax 276-297, other state data 298-307, tax type code 308 with local wages/tax 309-330, supplemental 338-487; RV 3-512 state-defined; SSA ignores RS/RV | from 2026-01-01 | US-FEDS5-032 |
| `sir.fed.new_hire.days` | 20 | from 1997-10-01 | US-FEDS5-024 |
| `sir.fed.reporting_agent.tech_spec` | Pub. 1474 (Rev. 4-2026): reporting agent = accounting service, franchiser, bank, service bureau or other payroll-services entity; agent list additions/deletions electronic above 100 submissions a week via SLFT B2B; deposits via EFTPS or FTA | from 2026-04-01 | US-FIL-001 |
| `sir.fed.third_party_payer.rules` | Pub. 15 (2026) third-party payer arrangements (reporting agents, sec. 3504 agents, CPEOs) - liability allocation per arrangement | from 2026-01-01 | US-FEDP51-002 |
| `sir.fed.w2.due_ty2026` | 2027-02-01 to SSA and employees | from 2026-01-01 | US-FEDS5-007 |
| `sir.fed.w2.format` | EFW2 Publication 42-007 (W-2) / 42-014 (W-2c) via SSA Business Services Online | from 2026-01-01 | US-FIL-002 |
| `sir.fl.new_hire.days` | 20 | from 2026-01-01 | US-FLS5-008 |
| `sir.fl.ui.flat_file` | Flat File Web Import v7 (Dec 2023): records 00/01/02/03/99, 2 implied decimals | from 2026-01-01 | US-FLS5-022 |
| `sir.fl.ui.wage_report` | RT-6 quarterly; e-file and e-pay mandatory at 10+ employees in any quarter of the prior state fiscal year | from 2026-01-01 | US-FLS5-006 |
| `sir.fl.withholding.return` | none: no income tax on natural persons | from 1971-01-01 | US-FL-001 |
| `sir.ga.new_hire.days` | 10 | from 1998-10-01 | US-GAS5-012 |
| `sir.ga.ui.agent_authorization` | GDOL power of attorney | from 2013-01-01 | US-GAW1B-001 |
| `sir.ga.ui.wage_report` | DOL-4N quarterly; electronic required at 25+ employees; portal entry, CSV/Excel (100-15,000), SFTP (>15,000 and payroll service providers) | from 2026-01-01 | US-GAS5-005 |
| `sir.ga.w2.filing` | G-1003 + W-2s by 31 Jan (TY2026: 2027-02-01) via GTC, Excel/CSV template or EFW2 + GA RS; 1099s via IRIS XML only | from 2026-01-01 | US-GAS5-003 |
| `sir.ga.withholding.agent_authorization` | Power of Attorney and Declaration of Representative (Form RD-1061); Disclosure Authorization Form (Form RD-1062); Reporting Agent Authorization (Form RD-1063) | from 2026-01-01 | US-GAW1B-003 |
| `sir.ga.withholding.returns` | G-7 (semi-weekly / monthly / quarterly / annual by lookback); EFT and e-file mandatory once a G-7 exceeds 500 | from 2026-01-01 | US-GAS5-002 |
| `sir.hi.new_hire.days` | 20 | from 2026-01-01 | US-HIS5-021 |
| `sir.hi.ui.agent_authorization` | Employers authorize a Third-Party Administrator (TPA) online through the employer portal (UC-25 Notification of Changes, Add SIDES Agent); a Letter of Authorization or Power of Attorney is no longer required | from 2026-01-01 | US-HIP52-003 |
| `sir.hi.ui.wage_report` | UC-B6 quarterly, last day of month after quarter; bulk spec not located | from 2026-01-01 | US-HIS5-012 |
| `sir.hi.w2.efile_threshold` | 10 | from 2026-01-01 | US-HIS5-006 |
| `sir.hi.withholding.agent_authorization` | Form N-848 Power of Attorney | from 2026-01-01 | US-HIP51-004 |
| `sir.hi.withholding.returns` | HW-14 quarterly (15th after quarter) with VP-1 deposits quarterly/monthly/semi-weekly; W-2/HW-2 to DOTAX by 31 Jan | from 2026-01-01 | US-HIS5-005 |
| `sir.ia.new_hire.days` | 15 | from 1998-07-01 | US-IAS5-012 |
| `sir.ia.ui.agent_authorization` | IWD 68-0092 Power of Attorney or Authorized Representative | from 2025-12-01 | US-IAP51-004 |
| `sir.ia.ui.wage_report` | Contribution and Payroll Report 65-5300 + wage detail by SSN, electronic | from 2025-02-26 | US-IAS5-024 |
| `sir.ia.w2.format` | IDR-unique EFW2-based ASCII 512 bytes (SSA file rejected): RS state code 19, permit 248-267, Iowa RV total; e-file by 15 Feb, W-2s with Iowa withholding only | from 2026-01-01 | US-IAS5-017 |
| `sir.ia.withholding.agent_authorization` | IA 2848 (14-101a, 06/18/2026) | from 2026-06-18 | US-IAP51-003 |
| `sir.ia.withholding.returns` | Quarterly return via GovConnectIowa; deposits quarterly/monthly/semimonthly; no annual reconciliation (VSPs no longer filed) | from 2026-01-01 | US-IAS5-016 |
| `sir.id.new_hire.days` | 20 | from 1997-10-01 | US-IDS5-015 |
| `sir.id.ui.agent_authorization` | Idaho Department of Labor Employer Portal Authorization Form | from 2026-01-01 | US-IDR3-002 |
| `sir.id.ui.wage_report` | TX20 + TX26 quarterly, Employer Portal mandatory | from 2025-11-05 | US-IDS5-021 |
| `sir.id.w2.format` | EFW2 plus Idaho state records uploaded in TAP (spec on STC developers page, not read) | from 2026-01-01 | US-IDS5-010 |
| `sir.id.withholding.agent_authorization` | Form ID-POA (withholding) | from 2019-12-17 | US-IDR3-001 |
| `sir.id.withholding.returns` | Form 910 in TAP (semimonthly / monthly / quarterly / annual); Form 967 + W-2s last day of January | from 2026-01-01 | US-IDS5-009 |
| `sir.il.new_hire.days` | 20 | from 2026-01-01 | US-ILS5-018 |
| `sir.il.ui.agent_authorization` | IDES service bureau MOU with POA option; E-POA bulk file (caret-delimited, max 1000 rows/day) | from 2017-09-05 | US-ILP52-010 |
| `sir.il.ui.wage_report` | UI-3/40 quarterly + monthly wage report for 25+ employees (months 1-2, MyTax CSV) | from 2026-01-01 | US-ILS5-017 |
| `sir.il.w2.filing` | Electronic only: MyTax (entry, CSV, EFW2 under IDR-996) or bulk EFW2 with ETIN (IDR-986); 2026 W-2s by 2027-02-01; 1099 bulk via IRIS from 2026-09-18 | from 2026-10-01 | US-ILS5-013 |
| `sir.il.withholding.agent_authorization` | Form IL-2848 POA incl. withholding income tax accounts | from 2026-01-01 | US-IL-004 |
| `sir.il.withholding.returns` | IL-941 quarterly, electronic; no annual reconciliation; deposits monthly or semi-weekly (>12,000 lookback) | from 2026-01-01 | US-ILS5-011 |
| `sir.in.new_hire.days` | 20 | from 2024-07-01 | US-INS5-016 |
| `sir.in.ui.agent_authorization` | Agent authorised in ESS at one of three levels (UI Agent Handbook) | from 2023-07-21 | US-INR3-004 |
| `sir.in.ui.wage_report` | Quarterly via E S S/UPLINK; file upload (CSV or Indiana ICESA) required above 50; SOC code and start date per worker | from 2025-07-01 | US-INS5-014 |
| `sir.in.w2.format` | XML IDORWTH2016V1.0 for new filers; EFW2 for existing filers (RS 306-343 county code, local wages/tax); schema not downloaded | from 2026-01-01 | US-INS5-011 |
| `sir.in.withholding.agent_authorization` | POA-1 or INTIME ePOA | from 2026-10-09 | US-INR3-003 |
| `sir.in.withholding.returns` | WH-1 via INTIME (annual / monthly / early filer); WH-3 + W-2 by 31 Jan, electronic above 25 statements | from 2026-01-01 | US-INS5-010 |
| `sir.ks.ui.agent_authorization` | K-CNS-032 TPA link form | from 2026-01-01 | US-KSP52-003 |
| `sir.ks.ui.wage_report` | Quarterly wage report and contribution return; MMREF/NASWA upload; e-file at 25+ employees (stricter reading of a self-contradicting page) | from 2026-01-01 | US-KSS5-022 |
| `sir.ks.w2.efile_threshold` | 51 | from 2026-01-01 | US-KSS5-026 |
| `sir.ks.w2.format` | EFW2 with Kansas RS record (K-2MT Rev. 10-25) or CSV formatted as in the KW-2CSV W-2 Specifications for Electronic Filing; Kansas does not accept withholding information submitted on magnetic media | from 2026-01-01 | US-KSS5-026 |
| `sir.ks.withholding.agent_authorization` | DO-10 Power of Attorney | from 2026-01-01 | US-KSP51-005 |
| `sir.ks.withholding.returns` | KW-5 each period (quad-monthly, semi-monthly, monthly, quarterly or annually); the annual return KW-3, W-2s and 1099s are due by January 31 of the following year; Form KW-3 must be filed electronically | from 2026-01-01 | US-KSS5-007 |
| `sir.ky.local.occupational` | Local occupational taxes administered by cities/counties/school districts (Louisville W-1/W-3; Lexington) | from 2026-10-12 | US-KYP52-002 |
| `sir.ky.new_hire.recipient` | Office of the Attorney General since 2025-07-01, within 20 days | from 2025-07-01 | US-KYS5-020 |
| `sir.ky.ui.wage_report` | Quarterly in KUIP (replaced KEWES 2026) | from 2026-01-01 | US-KYS5-019 |
| `sir.ky.w2.format` | SSA EFW2 with DOR-defined RS or K-5; electronic at 26+ statements; paper W-2s not processed | from 2026-03-01 | US-KYS5-013 |
| `sir.ky.withholding.returns` | MyTaxes: K-3 annual / K-1 quarterly / monthly / twice-monthly; zero returns required | from 2026-03-01 | US-KYS5-013 |
| `sir.la.new_hire.days` | 20 | from 2026-01-01 | US-LAS5-010 |
| `sir.la.ui.agent_authorization` | Online Power of Attorney in LAWATS | from 2026-01-01 | US-LAP52-005 |
| `sir.la.w2.efile_threshold` | 50 | from 2026-01-01 | US-LAS5-009 |
| `sir.la.withholding.returns` | L-1 quarterly electronic; L-3 + W-2s by first business day after 31 Jan via LaWage | from 2026-06-30 | US-LAS5-003 |
| `sir.ma.new_hire.days` | 14 | from 2026-01-01 | US-MAS5-016 |
| `sir.ma.ui.wage_report` | DUA quarterly wage detail by 3 p.m. on due date; CSV, EFW2 or ICESA; includes hours and state income tax withheld | from 2026-01-01 | US-MAS5-018 |
| `sir.ma.w2.due` | 31 January (W-2 page and handbook); the Withholding Tax Guide says end of March for 50+ (conflict; Jan 31 recommended) | from 2026-01-30 | US-MAS5-015 |
| `sir.ma.w2.format` | EFW2 RA/RE/RS/RT; RT must equal sum of RS; PDF/CSV refused; 50+ W-2s electronic | from 2019-12-19 | US-MAS5-019 |
| `sir.ma.withholding.returns` | M-941 via MassTaxConnect: annual / quarterly / monthly / quarterly with 3-business-day accelerated payments by annual amount | from 2026-01-01 | US-MAS5-013 |
| `sir.md.new_hire.days` | 20 | from 2026-01-01 | US-MDS5-018 |
| `sir.md.ui.wage_report` | BEACON quarterly: online, CSV, XML, ICESA or EFW2 (spec 2026-04-20) | from 2026-04-20 | US-MDS5-017 |
| `sir.md.w2.efile_threshold` | 25 | from 2026-01-01 | US-MDS5-016 |
| `sir.md.w2.format` | MW508 + W-2s by 31 Jan; modified Maryland EFW2 bulk upload; RS FEIN 328-336, CRN 338-345; RV=MW508 with NAICS | from 2026-01-01 | US-MDS5-016 |
| `sir.md.withholding.agent_authorization` | Form 548P Limited Power of Attorney and Maryland Reporting Agents Authorization (Comptroller of Maryland), used in place of the federal Form 8655 | from 2026-01-01 | US-MDP51-001 |
| `sir.md.withholding.returns` | MW506 on Maryland Tax Connect (accelerated / monthly / quarterly / seasonal / annual) | from 2026-01-01 | US-MDS5-021 |
| `sir.me.new_hire.days` | 7 | from 2026-01-01 | US-MES5-016 |
| `sir.me.payroll_processor_licence` | Payroll processors must hold a Bureau of Consumer Credit Protection licence | from 2026-01-01 to 2026-12-31 | US-MES5-011 |
| `sir.me.pfml.return` | PFML quarterly wage report and premium in the PFML portal; third-party payroll designation in the portal | from 2025-01-01 | US-MES5-024 |
| `sir.me.w2.filing` | Electronic to MRS by 31 Jan, paper not accepted; Maine Tax Portal bulk spec not read | from 2026-01-01 to 2026-12-31 | US-MES5-011 |
| `sir.me.withholding.returns` | 941ME quarterly electronic (Rule 104); semiweekly deposits at 18,000+ lookback; no W-3ME after TY2023 | from 2026-04-14 | US-MEP52-002 |
| `sir.mi.new_hire.days` | 20 | from 2026-01-01 | US-MIB5-001 |
| `sir.mi.ui.agent_authorization` | UIA 1488 Power of Attorney | from 2020-02-01 | US-MIP52-005 |
| `sir.mi.ui.wage_report` | MiUI quarterly (25th after quarter): CSV v3, ICESA v2, EFW2 v2, XML v1 | from 2026-02-23 | US-MIS5-022 |
| `sir.mi.w2.filing` | Due 31 Jan; 10+ forms via MTO in EFW2 / Pub 1220; W-2s not via CF/SF | from 2026-01-01 | US-MIPIT-001 |
| `sir.mi.withholding.agent_authorization` | Treasury Form 151 Authorized Representative Declaration | from 2021-11-01 | US-MIP52-011 |
| `sir.mi.withholding.returns` | SUW 5080 monthly/quarterly (20th); 5081 annual reconciliation 2027-02-28; accelerated EFT at 480,000+ | from 2026-01-01 to 2026-12-31 | US-MIS5-018 |
| `sir.mn.new_hire.days` | 20 | from 2026-01-01 | US-MNS5-016 |
| `sir.mn.ui.agent_authorization` | UI Agent Self-Service ID (8-digit Agent ID) | from 2026-01-01 | US-MNP6-003 |
| `sir.mn.ui.wage_report` | Quarterly wage detail electronic incl. paid hours (268.044) | from 2026-01-01 | US-MNS5-015 |
| `sir.mn.withholding.agent_authorization` | REV184b Business Power of Attorney | from 2026-01-01 | US-MNP52-005 |
| `sir.mn.withholding.returns` | Quarterly via e-Services; W-2 information due to the Minnesota Department of Revenue by January 31; with a total of more than 10 forms (W-2s plus 1099s) you must electronically submit the information using e-Services; a third-party bulk filer and each of its clients must have a valid Minnesota Tax ID Number | from 2026-01-01 to 2026-12-31 | US-MNS5-010 |
| `sir.mo.new_hire.days` | 20 | from 2012-08-28 | US-MOS5-001 |
| `sir.mo.ui.agent_authorization` | Division of Employment Security (DES) Power of Attorney: a signed, written agreement must be submitted to the DES (the DES provides a Power of Attorney form) | from 2026-01-01 | US-MOP52-008 |
| `sir.mo.ui.wage_report` | MODES-4 quarterly on UInteract (NASWA/ICESA); electronic at 50+ employees who e-file W-2 with SSA; spec M-INF-368 | from 2026-01-01 | US-MOS5-013 |
| `sir.mo.w2.efile_threshold` | 250 | from 2026-01-01 to 2026-12-31 | US-MOS5-001 |
| `sir.mo.withholding.returns` | MO-941 monthly / quarterly / annual; quarter-monthly payments at 9,000+ | from 2026-01-01 to 2026-12-31 | US-MOS5-001 |
| `sir.ms.new_hire.days` | 15 | from 1998-10-01 | US-MSS5-006 |
| `sir.ms.ui.wage_report` | UI-2 + UI-3 quarterly; ICESA S record (275) | from 2012-02-01 | US-MSS5-013 |
| `sir.ms.w2.format` | EFW2 RS (state code 28) via TAP; electronic at 10+ W-2s or when one payroll provider all year; Pub 89-145 Rev 10/25 | from 2026-01-01 | US-MSS5-005 |
| `sir.ms.withholding.returns` | 89-105 via TAP, 15th after the period; no depository; e-file at 20,000+ liability | from 2026-01-01 | US-MSS5-019 |
| `sir.mt.new_hire.days` | 20 | from 2026-01-01 | US-MTS5-012 |
| `sir.mt.ui.wage_report` | Quarterly via UI eServices; electronic mandatory from 2025-07-01 (ARM 24.40.1609) | from 2025-07-01 | US-MTS5-025 |
| `sir.mt.withholding.agent_authorization` | Montana Form POA or federal 2848; third-party access in TAP | from 2026-01-01 | US-MTS5-005 |
| `sir.mt.withholding.returns` | Accelerated / monthly / annual deposits; MW-3 + all W-2s by 31 Jan via TAP (EFW2); truncated SSNs not accepted | from 2026-01-01 | US-MTS5-005 |
| `sir.multi.new_hire.single_state_election` | Electronic multistate employers may report all new hires to one designated state after notifying HHS in writing | from 2026-01-01 | US-MULTIS5-006 |
| `sir.multi.w2.state_boxes` | W-2 boxes 15-20: up to two states and two localities per form; additional W-2 for more | from 2026-01-01 | US-MULTIS5-011 |
| `sir.nc.new_hire.days` | 20 | from 2026-01-01 | US-NCS5-020 |
| `sir.nc.ui.agent_authorization` | DES Power of Attorney and Declaration of Representative (one per agent per employer) | from 2025-07-01 | US-NCP51-003 |
| `sir.nc.w2.spec_ty2026` | TY2026 specs version 9-2026 (use beginning January 2027) | from 2027-01-01 | US-NCS5-028 |
| `sir.nd.new_hire.days` | 20 | from 2026-01-01 | US-NDS5-013 |
| `sir.nd.ui.wage_report` | Quarterly via UI EASY or Secure FTP | from 2026-01-01 | US-NDS5-011 |
| `sir.nd.withholding.agent_authorization` | Form 500 Authorization to Disclose / Designation of Representative; payroll provider designated on registration | from 2026-01-01 | US-NDP51-002 |
| `sir.nd.withholding.returns` | Form 306 quarterly; e-file if prior-year withholding 1,000+ or a provider e-files federally; Form 307 + W-2 EFW2 by 31 Jan | from 2026-01-01 | US-NDS5-002 |
| `sir.ne.new_hire.days` | 20 | from 2004-01-01 | US-NES5-014 |
| `sir.ne.ui.wage_report` | Combined Tax Report + Wage Report quarterly via NEworks online or FTP | from 2025-09-11 | US-NES5-011 |
| `sir.ne.w2.format` | W-3N + W-2 by 31 Jan; >50 forms via NebFile; EFW2 with NE RS (state code 31) and RV | from 2025-11-01 | US-NES5-017 |
| `sir.ne.withholding.returns` | 941N quarterly; 501N/EFT monthly deposits when >500 in month 1 or 2 | from 2026-01-01 to 2026-12-31 | US-NES5-010 |
| `sir.nh.new_hire.days` | 20 | from 2026-01-01 | US-NHS5-006 |
| `sir.nh.ui.agent_authorization` | Written request to NHES to designate an authorized agent; the request must be made by the employer and signed by a duly authorized employee whose position or title is stated in the request | from 2026-01-01 | US-NHP6-001 |
| `sir.nh.ui.wage_report` | Quarterly Employer Tax and Wage Report via WebTax/NHUIS (2016 handbook figures) | from 2026-01-01 | US-NHS5-013 |
| `sir.nh.withholding.return` | none: no state wage tax | from 2026-01-01 | US-NH-006 |
| `sir.nj.local.payroll_tax` | Newark and Jersey City quarterly employer payroll tax returns | from 2018-11-20 | US-NJP6-001 |
| `sir.nj.new_hire.days` | 20 | from 2026-01-01 | US-NJS5-018 |
| `sir.nj.ui.agent_authorization` | New Jersey Department of Labor Division of Employer Accounts Power of Attorney form | from 2026-01-01 | US-NJR3-005 |
| `sir.nj.ui.wage_report` | WR-30 quarterly, electronic (online or SFTP), due the 30th with no weekend extension | from 2026-01-01 | US-NJS5-017 |
| `sir.nj.withholding.agent_authorization` | M-5008-R Appointment of Taxpayer Representative (6/26) | from 2026-06-09 | US-NJR3-004 |
| `sir.nj.withholding.returns` | NJ-927 quarterly electronic; NJ-500 monthly; NJ-W-3 + W-2s by 15 Feb, electronic since TY2020 | from 2026-01-01 | US-NJP51-001 |
| `sir.nm.new_hire.days` | 20 | from 1997-10-01 | US-NMS5-010 |
| `sir.nm.ui.agent_authorization` | ES-905 Power of Attorney / Authorization of Agent or TPA login | from 2026-01-01 | US-NMP6-001 |
| `sir.nm.ui.wage_report` | Quarterly electronic only; Delimited, ICESA, XML, EFW2 published | from 2026-01-01 | US-NMS5-016 |
| `sir.nm.withholding.agent_authorization` | ACD-31102 Tax Information Authorization | from 2023-03-27 | US-NMP51-004 |
| `sir.nm.withholding.returns` | TRD-41414 (25th after period) and new TRD-41431 quarterly from 2026-01-01; e-file mandate from 2026 | from 2026-01-01 | US-NMS5-012 |
| `sir.nv.mbt.return` | MBT TAX-F003 quarterly on My Nevada Tax; from 2026-01-01 MBT wages compared with ESD wages | from 2023-07-01 | US-NVS5-009 |
| `sir.nv.new_hire.days` | 20 | from 2026-01-01 | US-NVS5-007 |
| `sir.nv.ui.agent_authorization` | Agent added as external ESS user | from 2026-01-01 | US-NVR3-003 |
| `sir.nv.ui.wage_report` | RPT3795 + NEW0098 quarterly in ESS (entry, SFTP EFW2, CSV/tab) | from 2026-01-01 | US-NVS5-008 |
| `sir.nv.withholding.return` | none: no state wage tax | from 2026-01-01 | US-NVP51-001 |
| `sir.ny.bulk_spec` | Pub. 72.5 (2/25) NYS-45 Web Upload: prior approval, test file, agent identification number | from 2025-03-21 | US-FIL-007 |
| `sir.ny.new_hire.days` | 20 | from 2026-01-01 | US-NYS5-010 |
| `sir.ny.nys45` | NYS-45 quarterly combined withholding + wage reporting + UI; e-file and ACH mandatory; no W-2 filed with NY | from 2026-01-01 | US-NYS5-010 |
| `sir.oh.bulk_filing` | Bulk Filing Guide Part A: IT 501, IT 941, SD 101, SD 141, FSET v4.4; ETIN | from 2025-01-01 | US-FIL-012 |
| `sir.oh.withholding.agent_authorization` | WT 8655 Payroll Service Company Authorization | from 2012-07-01 | US-FIL-011 |
| `sir.oh.withholding.returns` | IT 501 (quarterly / monthly / partial-weekly) and IT 941 by 31 Jan; W-2 upload by 31 Jan with school district code | from 2026-01-01 | US-OHB5-401 |
| `sir.ok.new_hire.days` | 20 | from 2015-11-01 | US-OKS5-007 |
| `sir.ok.ui.agent_authorization` | OES-190T Appointment of Account Representative | from 2025-11-01 | US-OKP51-005 |
| `sir.ok.ui.wage_report` | OES-3 via EZ Tax Express; ICESA 275 E/S/T | from 2024-10-01 | US-OKS5-020 |
| `sir.ok.withholding.agent_authorization` | BT-129 Power of Attorney (Rev. 7-2026) | from 2026-07-01 | US-OKP51-004 |
| `sir.ok.withholding.returns` | Quarterly return 20th after quarter via OkTAP; W-2 via EFW2 or entry by 31 Jan | from 2023-07-01 | US-OKS5-010 |
| `sir.or.agent_authorization` | Form OR-AUTH-REP (authorized representative) / Form OR-AUTH-INFO (designee), Oregon Department of Revenue | from 2026-01-01 | US-ORP51-005 |
| `sir.or.local.portland_metro_multnomah` | Quarterly returns and annual reconciliation on Portland Revenue Online; XML ReturnBatch 1.0; W-2 EFW2 by 31 Jan | from 2023-11-27 | US-ORS5-024 |
| `sir.or.new_hire.days` | 20 | from 2024-01-01 | US-ORS5-016 |
| `sir.or.oq` | Form OQ quarterly via Frances Online: withholding, UI, Paid Leave, WBF, TriMet, Lane, STT; Schedule B; Form 132 | from 2026-01-01 to 2026-12-31 | US-ORS5-010 |
| `sir.or.w2.filing` | OR-WR + W-2s via iWire (EFW2 or template) by 31 Jan | from 2026-01-01 to 2026-12-31 | US-ORS5-010 |
| `sir.pa.local.eit_lst` | EIT/LST quarterly returns and W2-R to the collector; Philadelphia quarterly returns | from 2018-05-04 | US-PAS5-017 |
| `sir.pa.new_hire.days` | 20 | from 2026-01-01 | US-PAS5-008 |
| `sir.pa.ui.agent_authorization` | Employers using a TPA must electronically register the Power of Attorney relationship in UCMS by assigning the TPA to their account; the TPA must then accept the association (the handshake) | from 2026-01-01 | US-PAP51-004 |
| `sir.pa.ui.wage_report` | Form UC-2 + UC-2A filed online via the Pennsylvania UC Management System (paper Forms UC-2 and UC-2A only under a temporary waiver); layout UC-2010 | from 2025-11-01 | US-FIL-008 |
| `sir.pa.withholding.agent_authorization` | REV-677 Power of Attorney (07-25) | from 2025-07-01 | US-FIL-010 |
| `sir.pa.withholding.returns` | myPATH deposits; quarterly W-3; REV-1667 + W-2s by 31 Jan, electronic at 10+ | from 2026-01-01 | US-PAS5-010 |
| `sir.ri.new_hire.days` | 14 | from 1997-10-01 | US-RIS5-010 |
| `sir.ri.withholding.agent_authorization` | RI-2848 | from 2026-01-01 | US-RIP51-004 |
| `sir.ri.withholding.returns` | Weekly/monthly/quarterly deposits; RI-941 quarterly; RI W-3 by 31 Jan; W-2 EFW2 with RS via Tax Portal | from 2026-01-01 | US-RIS5-018 |
| `sir.sc.new_hire.days` | 20 | from 1998-10-01 | US-SCS5-011 |
| `sir.sc.ui.agent_authorization` | UCE-1010 Written Authorization | from 2026-01-01 | US-SCR3-008 |
| `sir.sc.ui.wage_report` | Quarterly via SUITS: ICESA, EFW2, XML or CSV (spec v1.6) | from 2023-10-25 | US-SCS5-006 |
| `sir.sc.withholding.agent_authorization` | SC2848 | from 2023-02-17 | US-SCP52-001 |
| `sir.sc.withholding.returns` | WH-1605 Q1-Q3 and WH-1606 Q4 + annual reconciliation via MyDORWAY | from 2026-01-01 | US-SCS5-002 |
| `sir.sd.new_hire.days` | 20 | from 2026-01-01 | US-SDS5-007 |
| `sir.sd.ui.agent_authorization` | RA POA Rev. 01/2026 (Tax, Benefits or Limited) | from 2026-01-01 | US-SDP51-001 |
| `sir.sd.withholding.return` | none: no state wage tax | from 2026-01-01 | US-SDS5-001 |
| `sir.tn.new_hire.days` | 20 | from 2026-01-01 | US-TNS5-008 |
| `sir.tn.ui.agent_authorization` | POAs are no longer needed; third-party filers use the Manage Clients link (Register Client UI Tax Account link for employers not yet registered) in Employer e-Services; wage reports are filed in Employer e-Services from May 27, 2025 | from 2025-05-27 | US-TNR3-002 |
| `sir.tn.ui.wage_report` | LB-0851 + LB-0456 quarterly in Employer e-Services (ICESA variants, 58-char text) | from 2025-05-27 | US-TNS5-005 |
| `sir.tx.new_hire.days` | 20 | from 2023-05-01 | US-TXS5-016 |
| `sir.tx.ui.agent_authorization` | Form C-42 Written Authorization to Represent Employing Unit | from 2026-03-13 | US-TXP52-008 |
| `sir.tx.ui.wage_report` | Electronic only: Unemployment Tax Services or QuickFile (ICESA, MMREF-1, delimited) | from 2026-01-01 | US-TXSUI-006 |
| `sir.tx.withholding.return` | none: no state income tax | from 2019-11-05 | US-TXS5-001 |
| `sir.ut.new_hire.days` | 20 | from 2026-01-01 | US-UTS5-003 |
| `sir.ut.ui.agent_authorization` | DWS UI Power of Attorney (Rev. 08/24) | from 2026-01-01 | US-UTP6-003 |
| `sir.ut.ui.wage_report` | Quarterly Wage List and Contribution Report online only | from 2026-01-01 | US-UTS5-004 |
| `sir.ut.w2.format` | EFW2 with RS required, RV optional; lowercase .txt; fixed-length mandatory at 250+ | from 2024-12-01 | US-UTS5-014 |
| `sir.ut.withholding.agent_authorization` | TC-737 Power of Attorney (Rev. 9/26) | from 2026-01-01 | US-UTP6-002 |
| `sir.ut.withholding.returns` | TC-941E e-file only, quarterly (monthly payments at 1,000+); annual reconciliation with W-2s by 31 Jan | from 2026-01-01 | US-UTS5-013 |
| `sir.va.new_hire.days` | 20 | from 2020-07-01 | US-VAS5-006 |
| `sir.va.ui.agent_authorization` | ESS TPA invitation; ID.me login from 2026-08-01 | from 2026-08-01 | US-VAP6-001 |
| `sir.va.ui.wage_report` | VEC quarterly via ESS, eForm or Web Upload (Excel, MMREF/EFW2, ICESA, delimited) | from 2026-01-01 | US-VAS5-014 |
| `sir.va.w2.format` | Web Upload EFW2 / Pub 1220 (state code 51) by 31 Jan; upload does not create VA-6 | from 2026-01-01 | US-VAS5-009 |
| `sir.va.withholding.agent_authorization` | PAR 101 (person, not business) | from 2026-01-01 | US-VAP51-007 |
| `sir.va.withholding.returns` | VA-5 quarterly/monthly, VA-15/VA-16 semi-weekly; VA-6 by 31 Jan; all electronic | from 2025-07-01 | US-VAS5-013 |
| `sir.vt.new_hire.days` | 10 | from 2025-09-01 | US-VTS5-014 |
| `sir.vt.ui.agent_authorization` | Form C-50 Limited Power of Attorney | from 2016-04-01 | US-VTP51-013 |
| `sir.vt.ui.wage_report` | Quarterly via Employer e-Services; hourly workers also gender and hourly wage | from 2026-01-01 | US-VTS5-007 |
| `sir.vt.withholding.agent_authorization` | Form PA-1 Special Power of Attorney | from 2025-06-01 | US-VTP51-012 |
| `sir.vt.withholding.returns` | WHT-436 quarterly (carries CCC); WHT-434 annual by 31 Jan, e-file at 10+ and always for payroll services; no CF/SF | from 2026-01-01 to 2026-12-31 | US-VTS5-017 |
| `sir.wa.local.seattle_pet` | Seattle payroll expense tax: Taxpayer Authorization Form per client | from 2026-01-01 | US-WAP51-001 |
| `sir.wa.new_hire.days` | 20 | from 2026-01-01 | US-WAS5-018 |
| `sir.wa.ui.agent_authorization` | Complete and sign a power of attorney form for each client company; add the third-party administrator's information in the representative sections of the power of attorney form | from 2026-01-01 | US-FEDP51-016 |
| `sir.wa.ui.wage_report` | ESD quarterly via EAMS/SAW: name, SSN, gross, hours, SOC code | from 2026-01-01 | US-WAS5-013 |
| `sir.wa.withholding.return` | none: no income tax | from 2026-01-01 | US-WAS5-013 |
| `sir.wi.new_hire.days` | 20 | from 2026-03-16 | US-WIS5-013 |
| `sir.wi.provider_registration` | Payroll service providers must register and test their software with DOR | from 2026-01-01 | US-WIS5-016 |
| `sir.wi.ui.agent_authorization` | UCT-8291-E Employer Power of Attorney Assignment | from 2026-01-01 | US-WIP51-002 |
| `sir.wi.ui.wage_report` | Quarterly; electronic at 25+ employees (108.205(2)) | from 2026-03-16 | US-WIS5-013 |
| `sir.wi.w2.format` | EFW2 with RS (state code 55); 10+ electronic; no transmittal | from 2026-01-01 | US-WIS5-012 |
| `sir.wi.withholding.agent_authorization` | Form A-222 Power of Attorney | from 2026-01-01 | US-WIP52-003 |
| `sir.wi.withholding.returns` | WT-6 (DOR-assigned frequency), WT-7 by 31 Jan (TY2026 2027-02-01); electronic only | from 2026-01-01 | US-WIS5-011 |
| `sir.wv.new_hire.days` | 14 | from 2024-06-01 | US-WVS5-016 |
| `sir.wv.ui.agent_authorization` | WorkForce WV Power of Attorney (Rev. 3.23) | from 2026-01-01 | US-WVP52-006 |
| `sir.wv.ui.wage_report` | Quarterly via UC Employer System; SOC/job title, county | from 2026-01-01 | US-WVUI-001 |
| `sir.wv.withholding.agent_authorization` | WV-2848 | from 2015-12-01 | US-WVP51-006 |
| `sir.wy.new_hire.days` | 20 | from 2026-05-08 | US-WYS5-006 |
| `sir.wy.service_supplier` | The service supplier shall keep separate records, submit a list of all clients to the department on a quarterly basis and submit separate quarterly reports for each client; if the service supplier fails to pay contributions or submit required reports, the client is jointly and severally liable (W.S. 27-3-502) | from 2026-05-08 | US-WYS5-019 |
| `sir.wy.ui.wage_report` | WYUI quarterly (Apr 30 / Jul 31 / Oct 31 / Jan 31); file spec not read | from 2026-01-01 | US-WYS5-009 |
| `sir.wy.withholding.return` | none: no income tax | from 2026-01-01 | US-WYP51-001 |
| `wa.report.pfml_ltc.channels` | Manual entry (up to 50 employees), single CSV file (ESD template), ICESA bulk file for employer agents | from 2026-06-26 | US-WAB5-003 |
| `wi.report.w2.efile_threshold` | 10 | from 2026-01-01 | US-WIS5-012 |
| `wv.report.efile_threshold.employees` | 10 | from 2025-01-01 | US-WVS5-010 |
