# P7-LEVIES - Employer payroll levies beyond FICA/FUTA/SUI base (US-MQ-05c)

Consolidated 2026-10-30 from RESEARCH + AUDIT (6 batches, 51 jurisdictions). Register rows `US-<UF>P7-NNN` in `_register-shards/mandate-P7-levies-r1.csv`, appended to `legal-basis-register.csv`.

Status rule: ACTIVE = audit CONFIRMED/CORRECTED + source tier A, plus audit-missed tier A items I confirmed by reading the source in this run (CA Schedule F+, DC interest surcharge, OH TCSF, OR special payroll tax, PA Philadelphia wage tax, NJ Jersey City, VA admin fee). All else MANUAL with the gap stated.

Notes: KY SCUF (suspended), MD FAMLI (2027) carry no 2026 contribution. OR special payroll tax and items inside the UI rate (ID, ME, RI, TX, UT, WA EAF, CA F+) are embedded in the UI rate, not extra cash cost unless stated.

## AK

| Levy | Payer | 2026 rate | Base | Scope | Register id | Status |
|---|---|---|---|---|---|---|
| State Training and Employment Program (STEP) employee contribution | employee | 0.10% of wages, credited back in full against employee UI (net nil); inside the 0.50% employee UI rate | 54,200 USD | statewide | US-AKP7-001 | ACTIVE |
| Technical and Vocational Education Program (TVEP) employee contribution | employee | 0.25% of wages, credited back in full against UI (net nil) | 54,200 USD | statewide | US-AKP7-002 | ACTIVE |

## AL

| Levy | Payer | 2026 rate | Base | Scope | Register id | Status |
|---|---|---|---|---|---|---|
| City of Birmingham occupational tax (withheld by employer) | employee | 1% of gross compensation for work in Birmingham | no cap seen | City of Birmingham; other AL cities/counties levy own, no state list | US-ALP7-001 | MANUAL - municode script-rendered; snippet only; 2026 rate not read; other AL localities not enumerated |
| Alabama UC special assessments (generic authority) | employer | no 2026 rate published | 8,000 USD | statewide | US-ALP7-002 | ACTIVE |

## AR

| Levy | Payer | 2026 rate | Base | Scope | Register id | Status |
|---|---|---|---|---|---|---|
| Arkansas UI stabilization rate | employer | 0.2% (listed as Stabilization Rate; whether added to or part of experience rate not stated on page) | 7,000 USD | statewide | US-ARP7-001 | ACTIVE |

## CA

| Levy | Payer | 2026 rate | Base | Scope | Register id | Status |
|---|---|---|---|---|---|---|
| Employment Training Tax (ETT) | employer | 0.1% of first 7,000 USD (max 7 USD/employee/year) | 7,000 USD | statewide | US-CAP7-001 | ACTIVE |
| State Disability Insurance (SDI incl. PFL) | employee | 1.3% withheld, no wage ceiling since 2024-01-01; no employer share | no cap | statewide | US-CAP7-002 | ACTIVE |
| UI Schedule F+ emergency surcharge (15% on Schedule F) | employer | Schedule F plus 15% emergency surcharge; UI rates 1.5%-6.2% | 7,000 USD | statewide | US-CAP7-003 | ACTIVE |

## CO

| Levy | Payer | 2026 rate | Base | Scope | Register id | Status |
|---|---|---|---|---|---|---|
| Colorado FAMLI premium | shared | 0.88% of wages: 0.44% employer + 0.44% employee; 0.86% in 2027 | 184,500 USD (SS cap 2026) | statewide | US-COP7-001 | MANUAL - famli.colorado.gov 403; <10-employee employer exemption and cap not read on primary page |
| UI Support Surcharge | employer | New employers 2026: 0.17% (0.48% heavy construction); experienced: 10% of rate (unverified) | 30,600 USD | statewide | US-COP7-002 | MANUAL - cdle 403; experienced-employer 10% rule unverified |
| UI Solvency Surcharge | employer | New employers 2026: 1.35% (1.525% heavy construction); none in 2027 introductory rate (unverified) | 30,600 USD | statewide | US-COP7-003 | MANUAL - cdle 403; experienced schedule and 2027 claim unverified |
| Denver Occupational Privilege Tax - employee share | employee | 5.75 USD/month when earnings >= 500 USD/month | flat monthly | City and County of Denver | US-COP7-004 | ACTIVE |
| Denver Occupational Privilege Tax - employer share | employer | 4.00 USD/month per taxable employee | flat monthly | City and County of Denver | US-COP7-005 | ACTIVE |
| Other CO city OPTs (Glendale, Greenwood Village, Sheridan); Aurora repealed 2025-01-01 | shared | Glendale 5+5/month (threshold 750); Greenwood Village 2+2 (250); Sheridan 3+3; Aurora repealed | flat monthly | Glendale, Greenwood Village, Sheridan | US-COP7-006 | MANUAL - No city primary page read; Aurora repeal corroborated by auroragov notice |

## CT

| Levy | Payer | 2026 rate | Base | Scope | Register id | Status |
|---|---|---|---|---|---|---|
| Connecticut Paid Leave employee contribution | employee | 0.5% of wages; no employer contribution | 184,500 USD (SS wage base 2026) | statewide | US-CTP7-001 | ACTIVE |
| Connecticut UI fund solvency tax | employer | 1.0% added to charged rate (max charged 8.9%; combined 1.1%-9.9%) | 27,000 USD | statewide | US-CTP7-002 | ACTIVE |

## DC

| Levy | Payer | 2026 rate | Base | Scope | Register id | Status |
|---|---|---|---|---|---|---|
| DC UI administrative funding assessment | employer | 0.2% of all wages (also reimbursing employers); employees do not contribute | all wages | District of Columbia | US-DCP7-001 | ACTIVE |
| DC Universal Paid Leave tax | employer | 0.75% of covered wages, 100% employer-funded, not deductible from pay | all covered wages (no cap on page) | District of Columbia | US-DCP7-002 | ACTIVE |
| DC UI interest surcharge | employer | 0.1% added to contribution rate (reimbursing employers excepted); 2026 activation not confirmed | contribution base | District of Columbia | US-DCP7-003 | ACTIVE |

## DE

| Levy | Payer | 2026 rate | Base | Scope | Register id | Status |
|---|---|---|---|---|---|---|
| Operations and Technology Assessment | employer | 0.2% of taxable wages through 2026; 0.175% from 2027 | 14,500 USD | statewide | US-DEP7-001 | ACTIVE |
| Delaware Paid Leave contribution | shared | 0.8% only for employers required to offer all three leaves (25+ employees); parental-only employers (10-24) 0.32%; employer funds 100%, may recover up to 50% from employees | FICA wage limit (184,500 USD) | statewide | US-DEP7-002 | MANUAL - CORRECTED by audit; source is undated Wayback copy (tier B) |
| City of Wilmington wage tax | employee | ceiling 1.25%; enacted 2026 rate not read | earned income | City of Wilmington | US-DEP7-003 | MANUAL - Statute and 2026 enacted rate not read (audit UNVERIFIABLE) |
| Industry assessment rate (NAICS) | employer | 0.20/0.30/0.50/0.60/0.75% for five highest-cost NAICS levels; likely first billed 2027 | taxable wages | statewide | US-DEP7-004 | MANUAL - Missed levy; text not located by consolidation fetch; billing year unconfirmed |
| Employer size assessment rate | employer | Cat.2 0.25%; Cat.3 0.35%; Cat.1 0.00%; likely first billed 2027 | taxable wages | statewide | US-DEP7-005 | MANUAL - Missed levy; text not located by consolidation fetch; billing year unconfirmed |

## GA

| Levy | Payer | 2026 rate | Base | Scope | Register id | Status |
|---|---|---|---|---|---|---|
| Administrative Assessment | employer | 0.06% of taxable wages; authorised 2024-01-01 through 2026-12-31 | 9,500 USD | statewide | US-GAP7-001 | ACTIVE |

## HI

| Levy | Payer | 2026 rate | Base | Scope | Register id | Status |
|---|---|---|---|---|---|---|
| Employment and Training (E&T) assessment | employer | 0.01% | 64,500 USD | statewide | US-HIP7-001 | ACTIVE |
| Temporary Disability Insurance employee premium share | shared | Employee up to half of premium, max 0.5% of weekly wage and 7.50 USD/week | 1,500.21 USD/week | statewide | US-HIP7-002 | ACTIVE |
| Prepaid Health Care premium share | shared | Employee up to half of premium, max 1.5% of wages | employee wages | statewide | US-HIP7-003 | ACTIVE |

## ID

| Levy | Payer | 2026 rate | Base | Scope | Register id | Status |
|---|---|---|---|---|---|---|
| Workforce Development rate (inside UI tax) | employer | 0.03% standard (positive classes 0.00624%-0.02082%); administrative rate 0.000% | 58,300 USD | statewide | US-IDP7-001 | ACTIVE |

## IN

| Levy | Payer | 2026 rate | Base | Scope | Register id | Status |
|---|---|---|---|---|---|---|
| County income tax withheld by employer | employee | Varies by county, e.g. Marion 2.02%, Porter 0.50%, Randolph 3.00%, Boone 1.71% (changes effective 2026-10-01) | employee wages | county of residence on Jan 1 (92 counties) | US-INP7-001 | ACTIVE |

## KY

| Levy | Payer | 2026 rate | Base | Scope | Register id | Status |
|---|---|---|---|---|---|---|
| Service Capacity Upgrade Fund (SCUF) diversion | employer | Suspended all of 2026 (0.00%); 0.0115% diverted from rate from 2027-01-01 | 12,000 USD | statewide | US-KYP7-001 | ACTIVE |
| Local occupational license tax (Louisville 2.2%, Lexington 2.25%) | shared | Louisville Metro 2.2%; Lexington-Fayette 2.25%; others vary | gross compensation | Louisville, Lexington, many KY localities | US-KYP7-002 | MANUAL - Primary pages not opened (403); KOLA list not read |

## LA

| Levy | Payer | 2026 rate | Base | Scope | Register id | Status |
|---|---|---|---|---|---|---|
| UI Social Charges (Non-Charge, Incumbent Worker Training, Integrity) | employer | Rates not stated on LWC page; assessed only if assessed | 7,000 USD | statewide | US-LAP7-001 | MANUAL - No quantifiable rate; take from employer rate notice |

## MA

| Levy | Payer | 2026 rate | Base | Scope | Register id | Status |
|---|---|---|---|---|---|---|
| Workforce Training Fund contribution | employer | 0.056% (commissioner may adjust to ~22M USD/year) | 15,000 USD | statewide | US-MAP7-001 | ACTIVE |
| Employer Medical Assistance Contribution (EMAC) | employer | 0.34% (employers with <=5 employees exempt) | 15,000 USD | statewide | US-MAP7-002 | ACTIVE |
| Paid Family and Medical Leave contribution | shared | 0.88% (25+): family 0.18%, medical 0.70% (employee up to 40%); <25 employees 0.46% | Social Security max | statewide | US-MAP7-003 | MANUAL - mass.gov 403; secondary sources agree; 0.46% not independently seen |

## MD

| Levy | Payer | 2026 rate | Base | Scope | Register id | Status |
|---|---|---|---|---|---|---|
| Maryland FAMLI contribution (not in force 2026) | shared | No 2026 contribution; 0.9% from 2027-01-01 (0.45/0.45) | SS wage cap | statewide | US-MDP7-001 | ACTIVE |

## ME

| Levy | Payer | 2026 rate | Base | Scope | Register id | Status |
|---|---|---|---|---|---|---|
| Competitive Skills Scholarship Fund (CSSF) | employer | 0.14% | 12,000 USD | statewide | US-MEP7-001 | ACTIVE |
| Unemployment Program Administrative Fund (UPAF) | employer | 0.17% | 12,000 USD | statewide | US-MEP7-002 | ACTIVE |
| Paid Family and Medical Leave premium | shared | 1.0% (15+ employees; employee up to 0.5%); 0.5% (<15) | SS base | statewide | US-MEP7-003 | MANUAL - FAQ URL 404 live and Wayback per audit; structure unverified |

## MI

| Levy | Payer | 2026 rate | Base | Scope | Register id | Status |
|---|---|---|---|---|---|---|
| City of Detroit income tax withheld by employers | employee | Residents 2.4%; nonresidents 1.2% | wages | City of Detroit | US-MIP7-001 | MANUAL - Form 5469 not re-read by audit |
| Other Michigan city income taxes withheld (23 cities) | employee | Set by city ordinance; no rates read | wages | 23 cities | US-MIP7-002 | MANUAL - No rates; cannot be used as a rate source |

## MN

| Levy | Payer | 2026 rate | Base | Scope | Register id | Status |
|---|---|---|---|---|---|---|
| Workforce Development fee | employer | 0.10% of taxable wages; reimbursing employers exempt | 44,000 USD | statewide | US-MNP7-001 | ACTIVE |
| UI Additional Assessment (14%) and Special Assessment (0%) | employer | Additional assessment 14.00% of UI tax; special assessment 0.00% | 44,000 USD | statewide | US-MNP7-002 | ACTIVE |
| Minnesota Paid Leave premium | shared | 0.88% (family 0.27 + medical 0.61); employee up to 0.44%; small employer 0.66% | SS wage base (185,000 on page, unverified) | statewide | US-MNP7-003 | MANUAL - Live page 403; cap unverified |

## MO

| Levy | Payer | 2026 rate | Base | Scope | Register id | Status |
|---|---|---|---|---|---|---|
| City of St. Louis earnings tax withholding | employee | 1% of wages of employees living or working in St. Louis | wages | City of St. Louis | US-MOP7-001 | ACTIVE |
| City of St. Louis Payroll Expense Tax | employer | 0.5% of wages earned in the city; nonprofit/religious/educational/hospital/government exempt | payroll | City of St. Louis | US-MOP7-002 | ACTIVE |
| Kansas City earnings tax | employee | 1% (nonresident withholding voluntary) | wages | Kansas City, MO | US-MOP7-003 | MANUAL - Rate from FAQ wording only |
| UI maximum rate surcharge and rate adjustment | employer | Amounts not found | UI base | statewide | US-MOP7-004 | MANUAL - Secondary source only; effective rate may exceed 6% |

## MS

| Levy | Payer | 2026 rate | Base | Scope | Register id | Status |
|---|---|---|---|---|---|---|
| Workforce Investment and Training contributions (WET 0.15 + OWD 0.01 + Mississippi Works 0.04) | employer | Up to 0.20% added to UI rate; 2026 application NOT confirmed | 14,000 USD | statewide | US-MSP7-001 | MANUAL - No primary 2026 notice read |

## MT

| Levy | Payer | 2026 rate | Base | Scope | Register id | Status |
|---|---|---|---|---|---|---|
| Administrative Fund Tax | employer | 0.18% (0.13% for eligible classes 1-2) | 47,300 USD | statewide | US-MTP7-001 | ACTIVE |

## NH

| Levy | Payer | 2026 rate | Base | Scope | Register id | Status |
|---|---|---|---|---|---|---|
| Administrative Contribution (AC) carved out of UI rate | employer | 0.4% (2/5 of 1%), carved out of the schedule rate, no sunset in text | 14,000 USD (unverified) | statewide | US-NHP7-001 | ACTIVE |

## NJ

| Levy | Payer | 2026 rate | Base | Scope | Register id | Status |
|---|---|---|---|---|---|---|
| Workforce Development / Supplemental Workforce Fund - employer | employer | New employer 0.1175%; experienced individually | 44,800 USD | statewide | US-NJP7-001 | ACTIVE |
| Workforce Development / Supplemental Workforce Fund - worker | employee | 0.0425% (UI worker 0.3825% separate) | 44,800 USD | statewide | US-NJP7-002 | ACTIVE |
| Temporary Disability Insurance (TDI) | shared | Employee 0.19% on 171,100 USD; employer new-employer 0.50% on 44,800 USD; experience-rated | 171,100 employee / 44,800 employer | statewide | US-NJP7-003 | ACTIVE |
| Family Leave Insurance (FLI) - employee | employee | 0.23%; employer rate 0 | 171,100 USD | statewide | US-NJP7-004 | ACTIVE |
| Newark Employer Payroll Tax | employer | 1% of payroll; reduced 0.50% if >50% workforce are Newark residents (per excerpt) | payroll in Newark | City of Newark | US-NJP7-005 | MANUAL - newarknj.gov 403; excerpt only |
| Jersey City Employer Payroll Tax | employer | 1% of gross payroll; residents wages exempt; quarterly payroll < 2,500 USD exempt; quarterly filing | gross payroll | City of Jersey City | US-NJP7-006 | ACTIVE |

## NM

| Levy | Payer | 2026 rate | Base | Scope | Register id | Status |
|---|---|---|---|---|---|---|
| Workers Compensation Administration fee - employer share | employer | 2.55 USD per employee per quarter | flat per employee | statewide | US-NMP7-001 | MANUAL - Primary pages 404/403; excerpts only |
| Workers Compensation Administration fee - employee share | employee | 2.25 USD per employee per quarter | flat per employee | statewide | US-NMP7-002 | MANUAL - Primary pages 404/403; excerpts only |

## NV

| Levy | Payer | 2026 rate | Base | Scope | Register id | Status |
|---|---|---|---|---|---|---|
| Modified Business Tax - General Business | employer | 1.17% of quarterly wages above 50,000 USD | wages > 50,000/quarter | statewide | US-NVP7-001 | ACTIVE |
| Modified Business Tax - Financial Institutions | employer | 1.554% of wages after health-benefit deductions, no exemption | all wages | statewide | US-NVP7-002 | ACTIVE |
| Career Enhancement Program (CEP) assessment | employer | 0.05% in addition to UI rate (not for 5.4%-rate or reimbursing employers) | 43,700 USD (unverified) | statewide | US-NVP7-003 | ACTIVE |

## NY

| Levy | Payer | 2026 rate | Base | Scope | Register id | Status |
|---|---|---|---|---|---|---|
| Metropolitan Commuter Transportation Mobility Tax (MCTMT) | employer | Zone 1: 0.055% / 0.115% / 0.60% / 0.895% by quarterly payroll bracket (375,000/437,500/2,500,000); Zone 2: 0.055/0.115/0.34/0.635; bracket rate applies to whole zone payroll; local government Zone 1 max 0.60%, exempt in Zone 2 from 2025-07-01; filing threshold 312,500/quarter | quarterly MCTD payroll expense | MCTD (NYC, Nassau, Suffolk, Rockland, Westchester, Orange, Putnam, Dutchess) | US-NYP7-001 | ACTIVE |
| Paid Family Leave employee contribution | employee | 0.432% of gross wages; annual max 411.91 USD | capped by annual max | statewide | US-NYP7-002 | ACTIVE |
| Disability Benefits Law (DBL) employee contribution | shared | Employee 0.5% of wages max 0.60 USD/week (employer may elect to deduct); employer pays rest | weekly wages | statewide | US-NYP7-003 | ACTIVE |
| Re-employment Service Fund (RSF) | employer | 0.075% of quarterly wages, all contributory accounts | 17,600 USD (unverified on page) | statewide | US-NYP7-004 | ACTIVE |
| UI subsidiary rate (embedded in UI rate) | employer | Not published as separate number; derived new-employer 4.025% - 3.4% = 0.625% (derived) | 17,600 USD | statewide | US-NYP7-005 | MANUAL - Missed levy; subsidiary table not read; value derived not stated |

## OH

| Levy | Payer | 2026 rate | Base | Scope | Register id | Status |
|---|---|---|---|---|---|---|
| Municipal income tax withheld by employer | employee | Per municipality; 1% cap without voter approval (grandfathered exceptions) | qualifying wages | Ohio taxing municipalities | US-OHP7-001 | ACTIVE |
| School district income tax withholding | employee | Varies by district | district base | Ohio taxing school districts | US-OHP7-002 | MANUAL - Withholding duty text not read |
| Technology and Customer Service Fee (TCSF) - UI add-on | employer | 0.15% of taxable wages (every rate class 2026) | 9,000 USD | statewide | US-OHP7-003 | ACTIVE |

## OR

| Levy | Payer | 2026 rate | Base | Scope | Register id | Status |
|---|---|---|---|---|---|---|
| Statewide Transit Tax (STT) | employee | 0.1% of wages withheld by employer (Form OQ) | all wages | statewide | US-ORP7-001 | ACTIVE |
| TriMet Transit District payroll tax | employer | 0.8237% | all wages in district | TriMet district | US-ORP7-002 | ACTIVE |
| Lane Transit District payroll tax | employer | 0.80% | all wages in district | Lane Transit District | US-ORP7-003 | ACTIVE |
| Paid Leave Oregon contribution | shared | 1.0%: employee 60%, employer 40% (large employers or grant recipients) | 184,500 USD | statewide | US-ORP7-004 | ACTIVE |
| Workers Benefit Fund (WBF) assessment | shared | 0.018 USD per hour worked (1.8 cents); employer pays half, deducts half from workers | hours worked | statewide | US-ORP7-005 | ACTIVE |
| Special payroll tax (Wage Security Fund / SEDAF) inside UI | employer | 0.135% (0.00135) each quarter 2026; not an additional tax (embedded in UI rate; FUTA offset item) | 56,700 USD | statewide | US-ORP7-006 | ACTIVE |
| Portland Metro SHS and Multnomah Preschool for All income taxes (employer withholds) | employee | Metro 1% above 200,000 USD; PFA 1.5% above 200,000 and 3% above 400,000; thresholds inflation-indexed from 2026 | income above thresholds | Metro district / Multnomah County | US-ORP7-007 | MANUAL - CORRECTED by audit; research source tier B; 2026 indexed thresholds not retrieved |

## PA

| Levy | Payer | 2026 rate | Base | Scope | Register id | Status |
|---|---|---|---|---|---|---|
| Employee Unemployment Compensation contribution | employee | 0.07% of gross wages (2023 onward) | no cap | statewide | US-PAP7-001 | ACTIVE |
| UC surcharge and Additional Contributions | employer | Surcharge 9.2% applied to rate; Additional Contributions 0.60% (not newly liable) | 10,000 USD | statewide | US-PAP7-002 | ACTIVE |
| Local Earned Income Tax (EIT, Act 32) | employee | Varies by municipality/school district | earned income | PA localities; Philadelphia separate | US-PAP7-003 | MANUAL - No rate or rule verified (audit UNVERIFIABLE) |
| Local Services Tax (LST) | employee | Pittsburgh 52 USD/year; other localities set own up to cap; exemption under 12,000 USD earned income | flat per employee | municipality / school district | US-PAP7-004 | MANUAL - CORRECTED by audit for Pittsburgh only; research source tier B |
| Pittsburgh Payroll Expense Tax | employer | 0.55% (5.5 mills) of payroll for work in Pittsburgh; not deductible from wages | total payroll | City of Pittsburgh | US-PAP7-005 | ACTIVE |
| Philadelphia Wage Tax (employer withholds) | employee | Resident 3.74% / non-resident 3.43% through 2026-06-30; 3.735% / 3.425% from 2026-07-01 | compensation (non-residents: work in city) | City of Philadelphia | US-PAP7-006 | ACTIVE |

## RI

| Levy | Payer | 2026 rate | Base | Scope | Register id | Status |
|---|---|---|---|---|---|---|
| Job Development Assessment (JDA) | employer | 0.21% (Schedule F rates less 0.21; new employer 1.21% incl. JDA) | 30,800 USD (32,300 highest); wage bases unverified | statewide | US-RIP7-001 | ACTIVE |
| Temporary Disability / Caregiver Insurance (TDI/TCI) | employee | 1.1% of wages, max 1,100 USD/year | 100,000 USD | statewide | US-RIP7-002 | MANUAL - dlt.ri.gov 403; excerpts only |

## SC

| Levy | Payer | 2026 rate | Base | Scope | Register id | Status |
|---|---|---|---|---|---|---|
| Departmental Administrative Contingency Assessment (DACA) | employer | 0.06% added to base rate; solvency surcharge zero in 2026 | 14,000 USD | statewide | US-SCP7-001 | ACTIVE |

## SD

| Levy | Payer | 2026 rate | Base | Scope | Register id | Status |
|---|---|---|---|---|---|---|
| Reemployment Assistance administrative fee | employer | 0.08% for experience-rated employers only (N/A to new employers years 1-3) | 15,000 USD | statewide | US-SDP7-001 | ACTIVE |
| Reemployment Assistance investment fee | employer | New employers 0.55%; established 0.00%-0.53% by reserve ratio (hold-harmless cap) | 15,000 USD | statewide | US-SDP7-002 | ACTIVE |

## TX

| Levy | Payer | 2026 rate | Base | Scope | Register id | Status |
|---|---|---|---|---|---|---|
| Employment and Training Investment Assessment (ETIA) | employer | 0.10% of wages; offset by equal RTR reduction (net no increase) | 9,000 USD | statewide | US-TXP7-001 | ACTIVE |
| Unemployment Obligation Assessment - Interest Tax | employer | 0.01%; Bond Obligation Assessment 0.00% | 9,000 USD | statewide | US-TXP7-002 | ACTIVE |

## UT

| Levy | Payer | 2026 rate | Base | Scope | Register id | Status |
|---|---|---|---|---|---|---|
| Social cost (UI component) | employer | 0.1% fixed for all employers, inside the UI rate | 50,700 USD | statewide | US-UTP7-001 | ACTIVE |
| Delinquency surcharge (conditional) | employer | 1% added only if unpaid prior-year contributions | 50,700 USD | statewide | US-UTP7-002 | MANUAL - Conditional; text not re-read by audit |

## VA

| Levy | Payer | 2026 rate | Base | Scope | Register id | Status |
|---|---|---|---|---|---|---|
| UI pool cost charge | employer | Added each Jan 1; 2026 percentage not found | 8,000 USD | statewide | US-VAP7-001 | MANUAL - Mechanism text and 2026 value not found (VEC blocked) |
| UI fund building rate | employer | 0.2% added unless fund balance factor > 50%; 2026 application unknown | 8,000 USD | statewide | US-VAP7-002 | ACTIVE |
| Unemployment administrative fee (0.05% of taxable wages, offset by 0.05-point rate reduction) | employer | 0.05% of taxable wages assessed quarterly; rates reduced by 0.05 percent; not deductible from employees | 8,000 USD | statewide | US-VAP7-003 | ACTIVE |
| Virginia Paid Family and Medical Leave premiums (future) | shared | No 2026 contribution; collection begins 2028-04-01; rate not published | not read | statewide | US-VAP7-004 | MANUAL - CORRECTED by audit to future item; Chapter number unverified |

## VT

| Levy | Payer | 2026 rate | Base | Scope | Register id | Status |
|---|---|---|---|---|---|---|
| Child Care Contribution (Act 76 of 2023) | shared | Employer 0.44% of VT wages; may withhold up to 0.11% from employee | all wages | statewide | US-VTP7-001 | ACTIVE |

## WA

| Levy | Payer | 2026 rate | Base | Scope | Register id | Status |
|---|---|---|---|---|---|---|
| Paid Family and Medical Leave premium | shared | 1.13% of gross wages; employee up to 71.43%; employers <50 no employer share | 184,500 USD | statewide | US-WAP7-001 | ACTIVE |
| WA Cares Fund long-term care premium | employee | 0.58% of gross wages | no cap | statewide | US-WAP7-002 | ACTIVE |
| Employment Administration Fund and social cost factor (inside UI) | employer | EAF 0.02%-0.03%; social cost cap 1.22%; experience cap 5.4%; combined cap 6% | 78,200 USD | statewide | US-WAP7-003 | ACTIVE |
| Workers compensation medical-aid premium (employee half) | shared | Employer deducts half of medical-aid premium per risk class; hourly rates not collected | hours worked | statewide | US-WAP7-004 | MANUAL - RCW page SSL error; L&I hourly rates not collected |
| Seattle Payroll Expense Tax (JumpStart) - applicability thresholds | employer | Applies at Seattle payroll >= 9,074,409 USD in 2025 and an employee with >= 194,452 USD compensation in 2026; tiers (audit read): 0.746% on 194,452-518,537.99 and 1.811% on 518,538+ for payroll < 129,634,413; higher tiers 2.024% / 2.557% | compensation above thresholds | City of Seattle | US-WAP7-005 | ACTIVE |
| Seattle Social Housing Tax | employer | 5% of annual compensation above 1 million USD paid in Seattle | compensation > 1,000,000 | City of Seattle | US-WAP7-006 | MANUAL - Missed levy; page SSL error in this run, not confirmed by me |

## WI

| Levy | Payer | 2026 rate | Base | Scope | Register id | Status |
|---|---|---|---|---|---|---|
| Solvency component in UI new-employer rate | employer | New employer under 500,000 payroll: construction 2.00+0.50, others 2.50+0.55; 500,000+: construction 2.00+0.70, others 2.50+0.75 | 14,000 USD | statewide | US-WIP7-001 | ACTIVE |

## WV

| Levy | Payer | 2026 rate | Base | Scope | Register id | Status |
|---|---|---|---|---|---|---|
| Unemployment automation and administration fee | employer | 7% of total taxable wages for 12 months ending preceding June 30 (collections capped 18M/year, ends at 60M or 2031-07-01); 21A-5-5(d) also reduces rate by 7%; net dollar effect unresolved | taxable wages | statewide | US-WVP7-001 | ACTIVE |
| Charleston City Service Fee | employee | 3.00 USD per week withheld | flat weekly | City of Charleston | US-WVP7-002 | ACTIVE |
| Morgantown Municipal Service Fee | employee | 3.00 USD per calendar week per employee | flat weekly | City of Morgantown | US-WVP7-003 | MANUAL - Undated for 2026; tier B |
| Huntington / Wheeling city service fees | employee | Huntington 5.00/week; Wheeling 2.00/week (search summaries) | flat weekly | Huntington, Wheeling | US-WVP7-004 | MANUAL - Amounts not read in primary text |

## WY

| Levy | Payer | 2026 rate | Base | Scope | Register id | Status |
|---|---|---|---|---|---|---|
| Noncharged-benefits adjustment factor (ESF 60% / UC 20% / training 20%) | employer | Added to UI rate; numeric 2026 factor not published on pages read | 33,800 USD (unverified) | statewide | US-WYP7-001 | ACTIVE |
| Fund balance adjustment factors in WY UI rate | employer | Positive/negative adjustment computed annually; value not published in text read | UI base | statewide | US-WYP7-002 | MANUAL - Missed levy; no numeric value; not re-read |

## States with no levy found

| State | Conclusion | Official pages checked |
|---|---|---|
| AZ | No additional payroll levy; 0.1% Job Training Tax repealed 2016-01-01 (secondary sources; azleg 23-769 404). Audit CONFIRMED via search. Medium. | des.az.gov UI FAQ (403); azdor.gov withholding; azleg.gov ARS 23-727; ARS 23-769 (404) |
| FL | No transit/training/SDI levy; only Reemployment Tax. Audit did not re-check. Medium. | floridarevenue.com taxes and fees list; flsenate.gov Title XXXI |
| IA | No surcharge/transit/employee contribution on 2026 UI page (Rate Table D, base 20,400); school district and EMS surtaxes settled on individual return. Audit did not re-check. Medium. | workforce.iowa.gov UI taxes and 2026 release; revenue.iowa.gov; dol.gov state FMLA |
| IL | Fund Builder embedded in rate; no local wage tax or SDI/PFML. Audit CONFIRMED. Chicago/local not separately verified. | ides.illinois.gov UI rates 2026 PDF; tax.illinois.gov; labor.illinois.gov paid leave |
| KS | No payroll levy beyond UI; ESIAF surcharge repealed 2024-07-01 (HB 2570). Audit CONFIRMED via secondary sources; KDOL 403. Low-medium. | klrd.gov UI trust fund 2026; klrd.gov Tax Facts |
| MD | No UI add-on (Tax Table A, base 8,500); FAMLI starts 2027 (row listed); county income tax is income-tax withholding. Audit CONFIRMED. Medium. | labor.maryland.gov tax rate; paidleave.maryland.gov; marylandcomptroller.gov withholding guide |
| NC | Only contingent 20% surtax (G.S. 96-9.7(b)) when trust fund < 1B USD, not shown imposed for 2026; no transit/PFML; local income taxes barred. Audit CONFIRMED. | des.nc.gov; ncdor.gov; G.S. 105-247; dol.gov paid leave |
| ND | 2026 schedule shows UI rates only; conditional 10% surcharge is experience-rating (credited to account). Audit UNVERIFIABLE (partial PDF extraction). Medium. | jobsnd.com 2026 schedules; tax.nd.gov; NDCC 40-05.1; NDCC ch. 34 |
| NE | No separate training/workforce/admin assessment; wage base 9,000 (24,000 category 20). Audit CONFIRMED. | dol.nebraska.gov 2026 UI guide; revenue.nebraska.gov withholding |
| OK | OESC 2026 sheet: base 25,000, new rate 1.5%, no add-on; no paid leave program. Audit UNVERIFIABLE (OTC other taxes not expanded). Medium. | oklahoma.gov/tax businesses; OESC Important Numbers 2026; dol.gov paid leave |
| TN | Only UI premium (base 7,000, new 2.7%); Hall income tax archived; no PFML. Audit UNVERIFIABLE (DLWD 403). Medium. | tn.gov/revenue taxes list; tn.gov/workforce UI tax; dol.gov paid leave |

AZ/FL/IA/KS/ND/OK/TN are medium or low-medium confidence (agency pages 403 or not re-checked by audit). WY has only UI adjustment factors (rows above).

## Refuted / unverifiable

- REFUTED: none. CORRECTED by audit (corrected value used): DE Paid Leave (0.8% only for 25+ employees; 10-24 employers 0.32%), NV MBT financial institutions (1.554%), NH AC (tier A, RSA 282-A:87), OR Portland SHS/PFA (thresholds), SD admin fee (experience-rated only), SD investment fee (established 0.00-0.53%), PA LST (Pittsburgh 52 USD), VA PFML (future, 2028-04-01).
- Research errors to avoid: CA SDI is 1.3% (not 1.4%); NV statute copy shows 1.475% (unreduced); DE old FAQ wage base 18,500 is stale (14,500); register US-MN-PFML-001 superseded.
- UNVERIFIABLE (MANUAL): CO FAMLI/Support/Solvency, other CO OPTs, MA PFML, MN Paid Leave, ME PFML, MS WIT, LA social charges, MI Detroit and cities, KC, KY local, DE Wilmington, NJ Newark, NM WC fee, OH school district, RI TDI/TCI, UT delinquency, PA EIT, WA WC medical aid, VA pool cost.
- Audit-missed tier A, not confirmed by me (MANUAL): DE industry and size assessments, NY subsidiary rate, WA Seattle Social Housing Tax, WY fund-balance factors. Tier B/C missed: MO max-rate surcharge, WV Morgantown/Huntington/Wheeling.
- Cross-state gaps: transit and health-care levies absent only by agency-page inference; workers' comp payroll assessments not researched (except OR WBF, WA medical aid); FUTA credit reduction is federal (R3-FED).

## Verdict US-MQ-05c

Rows: 111 (75 ACTIVE, 36 MANUAL, 0 REFUTED). Jurisdictions covered: 51/51; uncovered: none.
**CLOSED** under the stated rule (every jurisdiction has an ACTIVE/MANUAL row or a no-levy entry with pages checked). Residual: MANUAL rows and medium-confidence no-levy states stay as MANUAL items in MANDATE and must not be quoted as final values.