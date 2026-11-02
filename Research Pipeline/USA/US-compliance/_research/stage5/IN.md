# Stage 5 — Indiana (IN), 13-domain hunt

Worker run on 2026-11-02, 07:27 to 07:58 local time. Declared budget: 60 fetches / 2 h. I used about 39 fetches and web searches, then stopped because the VPN dropped and every remaining in.gov target needed the Wayback Machine.
New rows are in `00-official-sources/_register-shards/S5-IN.csv`, ids US-INS5-001..021 (21 rows). I reused the active rows of `legal-basis-register.csv` without fetching them again: US-IN-001/-002/-003, US-INP51-001, US-INR3-001..006/-008, US-INP6-001, US-INP7-001, US-INP9L-001 and US-FEDP52-007.
Source files are in `00-official-sources/ccg-sources/IN/` (14 files, 6.7 MB). The largest is the DWD Employer Handbook, 3.5 MB.
Rows US-INS5-001..006 and -020 cite the IC 2026 Title 22 Article 2 PDF that was already on disk (`pdfs/IN/IN_IC_Title22_Article2_2026_2026-10-30.pdf`). They carry sections that no row had registered before.

**Access note:** the Windscribe US exit was on when the run started (Miami) and dropped at about 07:36; from then on the exit was BR. From a BR exit:
- www.in.gov times out;
- forms.in.gov and kb.dol.in.gov return a Cloudflare 403;
- iga.in.gov serves only an SPA shell for every `ic/2026/...pdf?download=1` URL, even from the US exit;
- Wayback returned one HTTP 429 early in the run.

I fetched these directly: DN#1, the DOR withholding page and in-newhire.com. Everything else in.gov came from Wayback `id_` copies, and each local file name says so.

## 1 labour_code
- **Minimum wage:** Indiana sets no figure of its own. IC 22-2-2-4(c) sets the state minimum at the FLSA minimum wage, so it is **7.25 USD/h** for as long as 29 USC 206 is unchanged. That gives 7.25 for 2026 and 7.25 for 2027 unless federal law changes; no 2027 change is enacted [US-INS5-001].
- **Tipped employees:** the cash wage may not be below 2.13 USD/h, and tips make up the gap. The employer must support the tip credit with reported tips (22-2-2-4(d)) [US-INS5-001].
- **Scope of the state law:** it covers only employers with 2 or more employees that are **not** subject to the FLSA minimum wage (22-2-2-3). The exemptions are listed under special populations [US-INS5-001].
- **No local minimum wage:** IC 22-2-2-10.5 pre-empts it. IC 22-2-16-3 also stops local units from mandating any benefit, working condition or leave policy above state or federal law [US-INS5-002].
- **Overtime:** 1.5x the regular rate over 40 h per workweek. There is no daily overtime. Domestic service is covered by the 40 h rule. Hospitals may use a 14-day/80 h period with an 8 h daily trigger (22-2-2-4(f),(m),(n)), and the regular-rate exclusions mirror the FLSA [US-INS5-001].
- **Pay frequency and timing:** at least semimonthly, or biweekly if the employee asks. Pay must cover wages earned up to no more than **10 business days** before payday (IC 22-2-5-1). Salaried employees who are eligible for FLSA overtime are exempt from s.1 (22-2-5-1.1). Agriculture is exempt from the chapter (22-2-5-3) [US-INS5-003].
- **Method of payment:** US money, negotiable check, draft, money order, or electronic transfer to the financial institution the employee designates [US-INS5-003].
  - The statute does not name paycards.
  - "Designated by the employee" reads as employee choice: direct deposit cannot be forced. Confidence 75%.
- **Penalty:** if the employer did not act in good faith, liquidated damages are 2x the wages due, plus attorney fees (22-2-5-2) [US-INS5-003].
- **Confidence:** High for the minimum wage, overtime and pay frequency; Medium for paycards.

## 2 income_tax
- **State rate:** 2.95% of Indiana AGI for 2026. DOR's rates page says "will adjust in 2027 to 2.90%" [US-INS5-009, US-INS5-007]. IC 6-3-2-1 itself was not read on an official host because iga.in.gov is an SPA.
- **Method (DN#1 R47/10-26, effective 2026-10-01, supersedes R46/01-26 = US-IN-001):** taxable wages = gross pay per period minus deduction constants [US-INS5-007]. The constants come from these annual amounts:

  | WH-4 line | What it claims | Annual amount |
  |---|---|---|
  | Line 5 | Personal exemptions | 1,000 each |
  | Lines 6 and 7 | Dependent and first-time dependent | 1,500 each |
  | Line 8 | Adopted child | 3,000 |

  - Each annual amount is divided by the pay periods: weekly 52, biweekly 26, semimonthly 24, monthly 12, daily 365.
  - Taxable wages x 2.95% gives the state tax; taxable wages x the county rate gives the county tax.
  - The notice gives no rounding instruction beyond 2-decimal constants and results.
- **G-DERIVE:** I re-derived DOR's worked example in Python [US-INS5-007].
  - Inputs: weekly pay of 800, Table A 5 = 96.15, B 3 = 86.54, B 1 = 28.85, C 2 = 115.38.
  - Constants total 326.92, so taxable wages are 473.08.
  - State: 473.08 x 0.0295 = **13.96**. County: 473.08 x 0.01 = **4.73**. Both match the notice.
  - Every constant also matches annual amount / periods (for example 1,000/26 = 38.46 and 1,500/24 = 62.50).
- **Supplemental pay:** bonuses and other one-time payments are withheld at the flat 2.95% plus county rate, with no exemptions. Indiana does not follow the IRC 3402(n) no-withholding allowance [US-INS5-007].
- **Withholding certificate:** Form WH-4, State Form 48845, edition **R10/8-23** [US-INS5-021].
  - It records the counties of residence and of principal employment as of Jan 1.
  - Additional state and county amounts go on lines 9-10.
  - The line 7 first-time dependent exemption lasts one year only, so a new WH-4 is needed each year.
  - A new WH-4 is due within 10 days when exemptions decrease.
- **Local income tax (county LIT):** all 92 counties levy it, on the county of residence on Jan 1, or for an out-of-state resident the county of principal work on Jan 1. The county is fixed for the whole year [US-INS5-008, US-INS5-007].
  - The rate chart has been in force since 2026-10-01. The Jan-1 edition differs only for Boone, which went from 0.017 to **0.0171** on 2026-10-01. Range 0.005 (Porter) to 0.03 (Randolph); Marion 0.0202 [US-INS5-007].
  - Rate-change calendar: an ordinance passed Jan 1–Aug 31 takes effect Oct 1 of the same year; Sep 1–Oct 31 takes effect Jan 1 of the next year; Nov 1–Dec 31 takes effect Oct 1 of the next year [US-INS5-008].
  - Statutory caps: expenditure rate up to 2.5% (2.75% in Marion), plus 1.25% for property-tax relief, plus special-purpose rates [US-INS5-008].
  - LIT is withheld and reported with the state tax on WH-1, WH-3 and the W-2 RS record (T3 piggyback) [US-INS5-010, US-INS5-011].
  - There is no separate nonresident LIT rate [US-INS5-008].
- **Nonresidents:**
  - **30-day safe harbor (IC 6-3-2-27.5, from 2024-01-01):** no state or county withholding when the employee is expected to work 30 days or fewer in Indiana. The employer needs a time-and-attendance system or Form WH-4AFF, and must catch up once the 30 days are exceeded. The safe harbor does not apply to athletes, entertainers, public figures or part-year residents [US-INS5-007, US-INS5-008].
  - **Reciprocity:** KY, MI, OH, PA and WI residents give the employer Form WH-47, and no state tax is withheld. County tax is still withheld if the principal work county on Jan 1 is in Indiana [US-IN-002, US-INS5-012, US-INS5-008].
  - **Nonresident aliens:** only one exemption on the WH-4 [US-INS5-021].
- **Withholding duty follows the federal duty:** "If you are required to withhold federal taxes, then you must also withhold Indiana state and county taxes." Casual laborers, some domestic employees, ministers and pension recipients may choose no withholding [US-INS5-012].
- **Oracle:** DOR offers no calculator. The DN#1 worked example, re-derived above, is the oracle (as in US-INR3-008).
- **Confidence:** High for the 2026 method and rates; Medium-high for the 2027 rate of 2.90% (authority page, statute not read).

## 3 social_security (UI; no SDI, TDI, PFML or LTC)
- **SUI (DWD):** premiums apply to the first **9,500 USD** of wages per employee per calendar year [US-INS5-014, US-INR3-001].
  - The handbook's "2011 to 2025" label and the undated rate-computation page support 9,500 for 2026. That value comes from carry-forward of the unchanged statute (IC 22-4-4-2 not read) and no 2026-labelled DWD page. Confidence 80%.
  - The base is **not indexed**.
- **Rates:** minimum 0.50% (47.50 per employee), typical new employer 2.50% (237.50), maximum in good standing 7.40% (703.00), maximum delinquent 9.40% (902.50). Each dollar figure checks as 9,500 x rate (derived) [US-INS5-014].
  - New employers pay 2.5% for their first 4 calendar years. Construction (NAICS 23) pays the lesser of 4.0% or the construction average (2.50% for 2025). Government pays 1.6% [US-INS5-014, US-IN-003].
  - The penalty rate is the computed rate plus 2% [US-INS5-015].
  - The **2025** solvency surcharge was 0%. The 2026 surcharge and schedule were not obtained (US-INS5-015 is `partial`).
- **No employee contribution:** premiums are employer-only [US-INS5-014, US-FEDP52-006 (employee UI only AK, NJ, PA)].
- **No SDI, TDI, PFML, LTC, transit or workforce levy** [US-INR3-002, US-KYR3-003, US-OWN-007]. County LIT is withheld from the employee [US-INP7-001].
- **Coverage thresholds:** domestic employers from 1,000 USD in cash wages in a quarter. Agricultural employers from 20,000 USD in a quarter, or 10 workers in 20 weeks. Clergy are excluded [US-INS5-014].
- **Confidence:** High for the structure; Medium for the 2026 rate-year parameters.

## 4 payslip_statute
- **IC 22-2-2-8(a):** the employer furnishes each employee, each pay period, a statement showing at least hours worked, wages paid and the deductions made. A sworn statement must be given to the commissioner on demand, and the poster is required [US-INP6-001].
- **Scope finding (new):** the duty binds "every employer subject to the provisions of this chapter". IC 22-2-2-3 defines that employer as one with 2 or more employees that is **not subject to the FLSA minimum wage** [US-INS5-001].
  - Read literally, the Indiana pay-statement duty therefore does not reach FLSA-covered employers, which is most employers.
  - The build should still emit hours, wages and deductions, because that costs nothing and is safe.
  - Confidence in the scope reading: 70%. See Open questions.
- **Delivery and retention:** no electronic-delivery or retention clause in IC 22-2-2-8. The fallback is the federal 3-year rule in 29 CFR 516 (FED shard). There is no language clause [US-INP6-001, US-INP9L-001].

## 5 reporting_instruments
| Filing | Authority / channel | Frequency and deadline | Format | Register |
|---|---|---|---|---|
| Registration | DOR via INBiz (EIN needed); DWD via E S S/UPLINK | before the first payroll | online_form | US-INS5-010, US-INS5-014 |
| WH-1 withholding return | DOR INTIME (online or upload under 10 MB) or SFTP (over 10 MB) | Annual (monthly average 83.33 USD or less, due 30 days after the period); monthly (1,000 USD or less, due 30 days after month end); early filer (over 1,000 USD, due 20 days after month end). EFT required if the average is over 5,000 USD/month. Zero returns are mandatory | xml (IDORWTH2016V1.0) or online_form | US-INS5-010, US-INS5-012 |
| WH-3 annual reconciliation + state W-2 | DOR INTIME/SFTP | Jan 31 (next business day if it falls on a weekend or holiday). Electronic filing is mandatory above 25 statements (IC 6-3-4-16.5) | xml; IRIS XML; EFW2 (existing filers only, RS record pos. 306-343: county code, local wages, local tax, 10-digit TID + 3-digit location); 1220 (W-2G/1099, retiring Sep 2027) | US-INS5-010, US-INS5-011, US-INS5-013 |
| Quarterly UI wage and employment report | DWD E S S/UPLINK | Apr 30, Jul 31, Oct 31, Jan 31. Electronic filing mandatory since 2019 (646 IAC 5-2-2); electronic payment required (646 IAC 5-2-17) | online_form (up to 50 workers) or file_upload (CSV or Indiana-modified ICESA; required above 50). SOC code (6 digits) and start date per worker | US-INS5-014 |
| New hire | Indiana New Hire Reporting Center (in-newhire.com) | within 20 days of hire, or of rehire after a break of 60+ days; file submitters send twice a month, 12-16 days apart | online_form or file_upload/SFTP; electronic only since 2024-07-01 (SB 148). Extra fields: job title, SOC, starting compensation, rate-of-pay basis | US-INS5-016, US-INS5-014 |

- **Penalties:**
  - WH-1: up to 20% (minimum 5 USD).
  - WH-3: 10 USD per statement.
  - UI report: 25 USD per missing or inadequate report.
  - New hire: 25 USD per employee, or 500 USD where there is collusion.
- **Conflict:** DOR's FAQ says the W-2 copy goes to DOR "by February 28". The withholding page and the EFW2 guide say January 31. **Use January 31** [US-INS5-012 vs US-INS5-010/011].
- **Scope trap:** the EFW2 guide is labelled "2025 and prior tax years" and says new filers must use XML. The XML schema IDORWTH2016V1.0 has **not been downloaded** (ACCESS gap).
- **Confidence:** High for deadlines and channels; Medium for formats (schema not on disk).

## 6 leave
- **Paid sick leave:** no state statute requires it of private employers, and local mandates are pre-empted (IC 22-2-16-3) [US-INS5-002, US-INS5-006].
- **PFML:** none [US-INR3-002].
- **Military family leave (IC 22-2-13):** up to 10 working days per year, unpaid, for a family member of a person ordered to active duty. The employee needs 12 months of service and 1,500 hours. Paid vacation or personal leave may be substituted, but not sick leave [US-INS5-006].
- **Not researched:** other mandated leave (jury duty, voting, volunteer firefighter) is outside IC 22-2 and was not searched. See Open questions.

## 7 termination
- **Final pay:**
  - Discharge (employer separates the employee): wages are due at the regular payday for the pay period in which the separation happened (IC 22-2-9-2) [US-INS5-005].
  - Resignation: due at the next usual payday. If the employer does not know where the employee is, penalties do not start until 10 business days after a demand or until the employee gives an address (IC 22-2-5-1(b)) [US-INS5-003].
  - Disputed amounts: the employer pays the part it concedes (22-2-9-3) [US-INS5-005].
- **Accrued vacation:** Indiana has no payout statute. Case law treats vacation pay promised by policy as wages (tier-B lead only, not registered). Open.
- **UI separation notice:** no mandatory notice at separation was located. Employers answer DWD requests (Base Period Separation Notice SF52984) [US-INS5-014].

## 8 benefits_in_kind
- **Conformity:** Indiana starts from federal AGI, and the withholding duty follows the federal duty [US-INS5-012]. The IRC conformity date (IC 6-3-1-11) and any departures (HSA, 125, transit) were **not read**. No departure was located; see Open questions. Confidence 60%.

## 9 deductions_garnishments
- **Wage assignments:** valid only if all of these hold [US-INS5-004]:
  - in writing, signed by the employee and revocable;
  - agreed in writing by the employer;
  - a copy delivered to the employer within 10 days;
  - made for one of the purposes listed in IC 22-2-6-2(b).
- **Limits on assignments:**
  - Uniforms and tools: at direct cost, and no more than the lesser of 2,500 USD/year or 5% of weekly disposable earnings.
  - No charge for OSHA personal protective equipment.
  - Interest on employer loans: prime + 4% at most.
- **Overpayment recovery (IC 22-2-6-4):** 2 weeks' notice, capped at the lesser of 25% of weekly disposable earnings or the amount above 30x the federal minimum wage. A 10x decimal-point error may be recovered at once [US-INS5-004].
- **Child support (IC 31-16-15, DCS) [US-INS5-017]:**
  - Withholding starts by the first pay period falling within 14 days after service; remit to INSCCU each payday.
  - Employers with 50+ employees and more than one order must remit electronically.
  - CCPA limits: 50%, 55%, 60% or 65%.
  - Priority: child support comes before every other claim except current taxes.
  - The employer may keep a fee of 2.00 USD per payment, inside the CCPA limit.
  - Lump sums (severance, vacation, bonus) are subject to arrears withholding.
- **Creditor garnishment:** limited to 25% of disposable earnings under the Indiana/CCPA business-garnishment limit [US-INS5-017].
  - The garnishment statute moved from IC 24-4.5-5-105 to **IC 37-2-6-4** (consumer-credit recodification, P.L.115-2026). The A.1 cross-reference is in the 2026 IC 22-2-6-2 [US-INS5-020]. The effective date, reported as 2026-07-01, comes from tier B only.
  - Any Indiana employer garnishment fee was not read.
- **State tax levies:** not researched.

## 10 collective_agreements / prevailing wage
- Indiana has had no state prevailing-wage law since 2015-07-01, when HEA 1019-2015 repealed the Common Construction Wage Act. Federal Davis-Bacon still applies to federal projects [US-INR3-005, US-INR3-006]. No state certified-payroll duty applies.

## 11 indexation
| Item | Indexed? | Where the new value appears | Register |
|---|---|---|---|
| Minimum wage | No; tracks the FLSA | federal | US-INS5-001 |
| SUI wage base 9,500 | No; fixed since 2011 | DWD handbook | US-INS5-014 |
| State PIT rate | Statutory step-down: 2.95% (2026), 2.90% (2027) | DOR rates page | US-INS5-009 |
| County LIT rates | By county ordinance, on Jan 1 / Oct 1 | DN#1, reissued January and October | US-INS5-007, US-INS5-008 |
| WH-4 exemption amounts | Not indexed: 1,000 / 1,500 / 3,000 | DN#1 | US-INS5-007 |

- **G-DERIVE:** done for the DN#1 example and for the UI rate-cost table. No caliber index is used.

## 12 data_protection
- **SSN on pay statements:** no Indiana truncation rule was located. IC 22-2-2-8 lists content only, so this is not proof that none exists.
- **Breach notification:** the breach-disclosure law (IC 24-4.9) is enforced by the AG, who can seek up to 150,000 USD for non-disclosure [US-INS5-018, partial].
- **SSN on filings:** the WH-4 takes an SSN or ITIN. The UI report treats an invalid SSN or ITIN as an inadequate report [US-INS5-021, US-INS5-014].
- **Confidence:** Medium-low.

## 13 live_legal_change (2026-01-01 to today)
| Change | Effective | Level | Status | Register |
|---|---|---|---|---|
| DN#1 R47/10-26: Boone LIT 0.017 → 0.0171 | 2026-10-01 | withholding | in force | US-INS5-007 |
| State PIT 2.95% → 2.90% | 2027-01-01 | withholding + assessment | enacted (per DOR page) | US-INS5-009 |
| P.L.104-2026: IC 22-2-6-2(b)(19) political-subdivision deferred-retirement assignment (opt-out) | 2026 (date not shown) | payroll deduction | enacted | US-INS5-004 |
| P.L.115-2026: UCCC recodified into IC 37 (garnishment cite → IC 37-2-6-4) | 2026-07-01 (tier B) | garnishment | enacted; date unconfirmed | US-INS5-020 |
| SEA 1-2025: municipal LIT (up to 1.2%) and new county caps | 2028-01-01 | withholding (sub-county) | enacted; tier-B detail only | US-INS5-019 (MANUAL) |
| 1220 flat file retired by DOR | 2027-09 | employer reporting | announced | US-INS5-010 |
| SB 148-2024: new-hire electronic filing and 4 extra fields | 2024-07-01 | reporting | in force | US-INS5-016 |

- **Not covered:** the full 2026 bulletin sweep (Indiana Register, DOR "what's new") was not run; see the gaps below.

## Special populations (state level, US-OWN-005)
| Population | Indiana rule | Register |
|---|---|---|
| Domestic / household | Exempt from the state minimum-wage law only through FLSA coverage. 40 h overtime rule applies (22-2-2-4(n)). Companionship workers employed by agencies are excluded. UI coverage from 1,000 USD in cash wages per quarter. May opt out of state withholding ("some domestic employees") | US-INS5-001, US-INS5-014, US-INS5-012 |
| Agricultural | Excluded from the state minimum-wage law (22-2-2-3(m)) and from the pay-frequency chapter (22-2-5-3). UI coverage from 20,000 USD per quarter or 10 workers in 20 weeks | US-INS5-001, US-INS5-003, US-INS5-014 |
| Minors | The state minimum-wage law excludes those under 16. IC 22-2-18.1 sets hours limits only (14-15: 7am-7pm, 9pm Jun 1–Labor Day) with no payroll effect. No state youth wage | US-INS5-001 |
| Tipped | Cash wage 2.13 USD plus tip credit; tip pooling IC 22-2-2-14.1 (not extracted) | US-INS5-001 |
| Clergy / religious | Excluded from the state minimum-wage law (22-2-2-3(f)). Ministers may choose no state withholding. Excluded from UI | US-INS5-001, US-INS5-012, US-INS5-014 |
| Students | Students working for their own school and student nurses are excluded from the minimum-wage law (22-2-2-3(g),(i)). WH-4 dependent student test: under 24 and full-time for 5 months | US-INS5-001, US-INS5-021 |
| Nonresident aliens | WH-4: one exemption only | US-INS5-021 |
| Nonresidents (any) | 30-day safe harbor; reciprocity with 5 states, but county tax still withheld | US-INS5-007, US-IN-002 |
| Statutory employees / commission-only | Commission-only employees and outside salespeople are excluded from the minimum-wage law (22-2-2-3(d),(k)). No other state rule beyond federal was located | US-INS5-001 |
| Government employees | Covered by the wage-assignment chapter (22-2-6-1(b)). New government employer UI rate 1.6%, or reimbursable status. The local-mandate pre-emption does not apply to a unit's own employees | US-INS5-004, US-INS5-014, US-INS5-002 |
| Casual laborers / pensioners | May choose no state withholding | US-INS5-012 |

## ACCESS gaps (exact URLs)
- `https://iga.in.gov/ic/2026/Title_6/Article_3.pdf?download=1` and `https://iga.in.gov/ic/2026/Title_22/Article_4.pdf?download=1`: HTTP 200 SPA shell of 691 bytes. Wayback `id_` returned 404. These would close IC 6-3-2-1 (2027 rate), 6-3-4-8.1 (frequency), 22-4-4-2 (wage base) and 22-4-11 (rate schedule).
- `https://iga.in.gov/ic/2026/Title_24/Article_4.5.pdf?download=1` and `https://iga.in.gov/ic/2026/Title_6/Article_3.6.pdf?download=1`: same SPA shell. These would close the garnishment fee and LIT detail.
- `https://www.in.gov/dor/files/IDORWTH2016V1.0`: not fetched, because the connection timed out after the VPN dropped (BR exit). This is the WH-1/WH-3 XML schema. The business rules `https://www.in.gov/dor/files/business-rules-wh1-xml.pdf` and `business-rules-wh3-xml.pdf` were not fetched either.
- `https://www.in.gov/dlgf/files/2026-memos/Legislation-Affecting-Local-Income-Taxes.pdf`: Wayback 404, and the direct fetch timed out.
- `https://kb.dol.in.gov/`: Cloudflare 403. This is the IDOL knowledge base for vacation payout and pay-statement scope.
- `https://forms.in.gov/download.aspx?id=2702`: Cloudflare 403 directly. A Wayback copy was used instead.
- The 2026 rate-year page `https://www.in.gov/dwd/indiana-unemployment/employers/employer-guide/rate-computation/state-premium-rate-computation/`: the 2026-01-13 snapshot still shows 2025.

## Open questions
1. **Scope of IC 22-2-2-8:** the duty binds only employers "subject to this chapter", which IC 22-2-2-3 limits to non-FLSA employers. Should the build model an Indiana pay-statement duty for FLSA-covered employers? Recommendation: emit hours, wages and deductions for every employer, and document it as best practice, not as a statutory duty. **What would close it:** IDOL guidance from kb.dol.in.gov, or the IDOL Wage & Hour FAQ, read from a US exit.
2. **SUI 2026 rate year:** the solvency surcharge and the applied-rate schedule, plus a 2026-labelled wage base. **What would close it:** the DWD state-premium-rate page as currently published, or IC 22-4-4-2 / 22-4-11-3.3 from the 2026 IC PDF, read through the browser pass.
3. **2027 PIT rate 2.90%:** resting on the DOR page alone. **What would close it:** IC 6-3-2-1 from the 2026 IC Title 6 Article 3 PDF (browser pass).
4. **WH-1/WH-3 XML:** the schema IDORWTH2016V1.0 and the business rules are needed for the RSPEC/SIR field spec. **What would close it:** the files at the URLs above, fetched from a US exit. Also the TY2026 edition of the EFW2 guide.
5. **Accrued vacation payout on termination:** **What would close it:** an IDOL knowledge-base article, or the Indiana Supreme Court decision on vacation pay as wages read on an official host (courts.in.gov).
6. **Benefits-in-kind conformity:** the IRC conformity date for 2026 and any HSA, 125 or transit departures. **What would close it:** IC 6-3-1-11 (2026), or the DOR IT-40 2025 instructions, "Add-backs" section.
7. **Creditor-garnishment employer fee and the IC 37-2-6-4 text and effective date.** **What would close it:** IC Title 37 Article 2 (2026) through the browser pass.
8. **Other mandated leave** (jury duty IC 34-28-4, voting, volunteer firefighter / emergency responder) and any pay-continuation duty: not researched.
9. **Superseded rows:** the synthesis should mark these so the merge carries `supersedes`:
   - US-IN-001 and US-INP51-001 (DN#1 R46/01-26, county chart) get `effective_to` 2026-09-30 for the county chart, superseded by US-INS5-007.
   - US-INP51-002 (handbook rev. 2023) is already superseded, now by US-INS5-014.
   - US-INP7-001 claims "Boone 1.71% (changes effective 2026-10-01)" while its local file is R46, where Boone is 0.017. The figure is right, but its source is R47 = US-INS5-007.
10. **Parallelisable:** none of the remaining items needs a separate agent. Items 1-4 and 7 are browser-pass items on in.gov and iga.in.gov from a US exit.

**Overall confidence for IN:** 80%.
- High (90%): withholding method and rates, LIT, deadlines, final pay, deductions, child support.
- Medium (70%): UI 2026 parameters, payslip scope, formats (schema not on disk).
- Low (55%): benefits in kind, data protection, vacation payout.
