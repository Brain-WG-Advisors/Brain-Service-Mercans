# Mandate answers: FED + MULTI (US-MQ-01..10, 12)

Date: 2026-10-29. Worker: compliance-source-hunter (scope: mandate only). Register shard: `00-official-sources/_register-shards/mandate-FED-MULTI.csv` (ids US-FED-001..021, US-MULTI-001..003). `consumed_by` is empty on every row (no facts file emitted in this pass); the scaffolder or the next pass must fill it.
Fetch accounting: about 47 tool calls (incl. 2 searches); ~12 returned 403/404/redirect/connection errors. Slightly above the 45 declared, because failed calls were counted late. Acquisition stopped at that point.
Blocked (recorded, not worked around): ssa.gov (cbb.html, press release, COLA factsheet) 403; federalregister.gov redirected to a bot "unblock" page; taxadmin.org (FTA) 403; michigan.gov RAB 403; DOL state-paid-leave pages 404; uscode.house.gov 404; codes.ohio.gov connection refused. Substitutes: GovInfo US Code and Federal Register PDF, eCFR API.

---
# PASS 2 (Chrome re-hunt, 2026-10-29) — supersedes pass 1 where stated below
Budget declared 45 page reads; used 36 (reads counted per URL, failed loads counted when a host answered). Register rows added: US-FED-022..030, US-MULTI-004..023; in place: US-FED-003, US-FED-008, US-MULTI-002 (marked superseded for the pairs below), US-MULTI-003. Verification method on each row says `chrome-read` (real Chrome page text) or `http-read` (curl of the official URL, text extracted locally; used where Chrome shows PDFs without text or returned a cross-domain security stop). No javascript_tool, no filter bypass.

## P2 / US-MQ-02 Currency, rounding — unchanged
No new source needed beyond pass 1; Pub 15-T 2026 re-read: rounding text confirmed (optional, drop under 50 cents, 50-99 up, "if rounding is used, it must be used consistently"), US-FED-001/027. Form 941 cents rule stands (US-FED-005). Confidence 90%. Still NOT LOCATED: express USD sentence for W-2 (inferred).

## P2 / US-MQ-03 Language — unchanged for federal
Nothing new read. NOT LOCATED stays: per-state primary-language notices (belongs to the state workers).

## P2 / US-MQ-05 Devolved payroll-adjacent domains — federal tax-advantaged limits now answered
- 402(g) elective deferral 2026 = 24,500 (2025: 23,500); age-50 catch-up 8,000; ages 60-63 11,250; IRA 7,500 (US-FED-023, IR-2025-111 read in Chrome; Notice 2025-67 itself not read). Confidence 95%.
- HSA 2026: self-only 4,400, family 8,750 (Rev. Proc. 2025-19 sec. 3.01, US-FED-024; PDF unreadable in Chrome, read through a downloaded copy). Confidence 95%. HDHP deductible/OOP minimums for HSA not extracted (the MSA analogue is in US-FED-025).
- Health FSA 3,400 (carryover 680); 132(f) transit and parking 340 each per month; 911 exclusion 132,900 (US-FED-025).
- Still NOT LOCATED: list of states with SDI/TDI/PFML/WA Cares (state workers), IWO form.

## P2 / US-MQ-06 Indexation — closed except 2027 Rev. Proc.
(a) Rev. Proc. 2025-32 sec. 1 says items are "generally determined by reference to section 1(f)" but does not name the series; 26 USC 1(f)(3) (read on LII, US-FED-026) fixes the series as C-CPI-U (chained), base CPI 2016. Confidence 90% (LII republication, not uscode.house.gov).
(b) SSA page read in Chrome (US-FED-022): 2026 base 184,500 confirmed; the page already publishes 2027 = 192,300 (employee/employer maximum OASDI 11,922.60 each in 2027). The 2027 Rev. Proc. and the 2027 FUTA/FICA items other than the base were not searched. Confidence 98% for both bases. Mark `next_year` refresh partially closed (SSA only).
(c) Other indexed limits now located: see MQ-05 list.

## P2 / US-MQ-08 Oracle — answered
Pub. 15-T (2026) read in full text (71 pages, extract of 249k chars): the only worked examples are the nonresident-alien weekly example (300 + 226.90 = 526.90 -> 31 withheld) and the tribal-gaming monthly example (6,000 -> 584.09) (US-FED-027). There is NO published full percentage-method worked example; Worksheet 1A is the normative procedure (line 1g 12,900 MFJ / 8,600 other; allowance 4,300 for pre-2020 W-4). Oracle for tests = hand re-derivation from Worksheet 1A and the Annual Percentage Method tables, plus the two examples above. IRS Tax Withholding Estimator remains an employee tool (not an oracle). Confidence 90%. Not done: derived worked case from the annual tables (tables were not parsed in this pass).

## P2 / US-MQ-09 Third-party filing — federal answered
Form 8655 (Rev. 1-2024) read (US-FED-028): lines 15/16 list the returns and deposits; line 19 lets the agent sign and file state or local returns tied to lines 15/16; agreement text keeps the employer liable. Rev. Proc. 2012-32 re-read (US-FED-008): effective 2012-11-19, supersedes Rev. Proc. 2007-38; sec. 5.05 (as revised) requires the reporting agent to notify the taxpayer in writing at least quarterly that the authorization does not remove the employer's liability. Pub. 15 (2026) third-party payer section (US-FED-029) states employer remains liable for PSP and reporting agent. Pub. 1474 downloaded but not analysed (no claim made). Confidence 92%. State POA forms and owner questions: unchanged (state workers/owner).

## P2 / US-MQ-10 Multistate — reciprocity answered from state sources for 17 jurisdictions
Reciprocity pairs, each from the state's own page or form (row ids in brackets):
- AZ: CA, IN, OR, VA [US-MULTI-017]
- DC: no state list; nonresident (D-4A) is simply not subject to DC withholding if not 183+ days in DC [016]
- IA: IL only [018]
- IL: IA, KY, MI, WI (not read on tax.illinois.gov: host did not load; confirmed from IA [018], KY [009], MI [010], WI [006] pages)
- IN: KY, MI, OH, PA, WI (not read on in.gov: connection refused; confirmed from KY [009], MI [010], OH [005], PA [007], WI [006], AZ [017])
- KY: IL, IN, MI, OH, VA (daily commuters), WV, WI [009]
- MD: DC, PA, VA, WV [008, dated 2011]
- MI: IL, IN, KY, MN, OH, WI [010]
- MN: MI, ND [013]
- MT: ND (not read: revenue.mt.gov did not load; confirmed from ND page [014])
- ND: MN, MT [014]
- NJ: PA [011]
- OH: IN, KY, MI, PA, WV [005]
- PA: IN, MD, NJ, OH, VA, WV [007]
- VA: DC, KY, MD, PA, WV [004]
- WI: IL, IN, KY, MI [006]
- WV: KY, MD, OH, PA, VA [015]
- DE: none [019]. Exemption certificates: WI W-220, PA REV-419, NJ NJ-165, KY 42A809, MN MWR (annual), ND NDW-R (annual), WV IT-104, AZ WEC, DC D-4A, IA 44-016, IL IL-W-5-NR.
Confidence 90% for the 15 jurisdictions read on their own pages; 80% for IL, IN, MT (confirmed only from the partner states' pages).
Convenience-of-employer: NY (telecommuting days stay NY days unless a bona fide employer office is set up at the telecommuting location; page read, US-MULTI-003); NJ (applies the resident state's rule, names DE, NE, NY; CT by reciprocal law; PA excluded) [012]; CT applies the nonresident's state test to work for a CT employer from 2019-01-01 [020]. NE and DE: named by NJ only (NE page revenue.nebraska.gov did not load; DE guide read shows no reciprocity, but no convenience-rule text was located there). PA and AR: NOT LOCATED.
Nonresident thresholds located: AZ 60 days present (withholding) [017]; AL 30 days safe harbour [021]; WV 30 days or less and work in more than one state [015]; MD reciprocity does not apply at 183+ days with abode over 6 months (except WV) [008]; DC 183 days [016]; WI filing threshold 2,000 [006]; GA filing threshold lesser of 5% or 5,000 (filing rule, not withholding) [022]; CO no minimum, day-apportioned [023]; NE seven-day rule and ID 1,000 appear only in search summaries (not read; leads only). Still NOT LOCATED on a read page: other states' employer withholding thresholds (state workers).
Resident credit / difference withholding: WI says no credit for tax paid on reciprocity income and credit allowed for tax paid to a reciprocal state on non-exempt income (Pub 121); MD AR 3: nonresidents claim the credit on the home-state return. No uniform rule.
Statute for mobile workers (49 USC 14503 etc.) and federal-level sourcing: not attempted in pass 2.

## P2 / US-MQ-12 Special populations (federal layer)
- Students: enrolled and regularly attending at a private school/college/university: FICA and FUTA exempt, FIT withheld; public or auxiliary nonprofit: FICA exempt unless a section 218 agreement covers the service (Pub 15 2026, US-FED-029).
- Employees abroad: US citizen working abroad for a foreign affiliate: FIT exempt if the 911 exclusion is reasonably expected or foreign law requires withholding; FICA applies only if an American employer covers the citizen by agreement or if the employer is an American employer; resident alien abroad: FIT withheld (US-FED-029). Section 3121(z) treats a controlled foreign person as an American employer (Pub 15 text read). Confidence 85% (table read, footnotes simplified).
- Clergy: Pub 15-A (2026) sec. 4: minister's earnings are not subject to FIT, social security or Medicare withholding even if common-law employee; subject to SE tax; voluntary FIT agreement; no SS/Medicare wages on W-2/941/944; parsonage allowance excluded (US-FED-030). Members of a recognized religious sect opposed to insurance: exemption only if both employee and employer are members (Pub 15). Confidence 92%.
- Agricultural and household: Pub 15 table points farmwork to Pub 51 (Circular A); Pub 51 URL irs.gov/pub/irs-pdf/p51.pdf returned 404, so Pub 51 itself NOT READ; household threshold 3,000 (FICA) from Pub 15 What's New. Pub 54 not read.
- Statutory employees, nonresident aliens: unchanged from pass 1.
Proposal for owner unchanged.

## Hosts and files that did not read (pass 2)
Do not load at all: tax.illinois.gov (Chrome and curl), www.in.gov (connection refused), revenue.mt.gov, revenue.nebraska.gov (Chrome stop + curl 000), tax.idaho.gov (curl 000). 403 to curl, not retried in Chrome: azdor.gov PDF form (page read instead). Unreadable PDF in Chrome (no text): irs-drop rp-25-19.pdf, in.gov ib33.pdf. No "Permission denied" from get_page_text was received. Chrome cross-domain security stops on navigate+get_page_text: ssa.gov was fine; irs.gov/newsroom, portal.ct.gov, revenue.mt.gov, tax.illinois.gov (stops), the same pages read later in a separate call where possible. 404: portal.ct.gov nonresident page, irs.gov Pub 51, pa.gov/md pages tried first.

---
# PASS 1 text (kept for history; where it conflicts with PASS 2 above, PASS 2 wins)
## US-MQ-01 Tax year
**Status: PARTIAL (federal answered, state check NOT LOCATED).**
Answer: Federal employment-tax periods are the calendar year / calendar quarter. No fiscal-year option found. FUTA tax is imposed "for each calendar year" on wages "paid ... during the calendar year" (26 USC 3301, US-FED-013). FICA returns are per calendar quarter, farm labor per calendar year, Form 944 annual option (26 CFR 31.6011(a)-1, US-FED-015; Form 941 instr. Rev. March 2026, US-FED-005). W-2 is furnished "in respect of the remuneration paid ... during the calendar year", due Jan 31 following; 2026 forms due 2027-02-01 (26 CFR 31.6051-1, US-FED-016; W-2/W-3 instr., US-FED-006). Form 940 is a calendar-year return (US-FED-007, 2025 edition; 2026 edition not published as of today). Pub. 15 mentions "calendar or fiscal year" only in the due-date context (US-FED-004), it does not give employers a fiscal reporting period; this is a reading of that fragment, not a statement that fiscal year is barred in so many words.
Answer to the question "may a fiscal-year employer report on its fiscal year": No, on the instruments read. Confidence 90%.
NOT LOCATED: one state DoR annual-reconciliation instruction confirming calendar year (no state page fetched). Closing: any state withholding annual reconciliation instruction (jurisdiction workers US-MQ-20..70).
register_id: US-FED-004/005/006/007/013/015/016.

## US-MQ-02 Currency, minor units, rounding
**Status: PARTIAL.**
(a) Computation (Pub. 15-T 2026, US-FED-001): "you may reduce the last digit of the wages to zero, or figure the wages to the nearest dollar. You may also round the tax for the pay period to the nearest dollar"; rounding rule: drop under 50 cents, 50-99 cents up. Rounding is OPTIONAL, so the exact-cent calculation is permitted. Confidence 90% (quote read from page; page text read to 100k of 162k chars, the rest read for examples only).
(b) Returns: Form 941 "Don't round entries to whole dollars. Always show an amount for cents, even if it is zero" (US-FED-005). Form 940: employer "may choose to round" to nearest dollar (US-FED-007, 2025 edition). W-2: the instruction lists "Omit the decimal point and cents from entries" as a common error, i.e. cents are expected; no explicit USD sentence found (US-FED-006). Confidence 80% for W-2 (inferred from an error list).
Payment unit coarser than USD 0.01: none located. NOT LOCATED: a statute/instruction expressly requiring USD on returns (31 USC 5103 legal tender not fetched). Closing: General Instructions for Forms W-2/W-3 "Electronic filing" amounts section, offset > 100000 chars, not read.
Do not set payment rounding coarser than 0.01; keep rounding.rule pending (optional whole-dollar for withholding computation and Form 940).

## US-MQ-03 Language (G-LANG)
**Status: PARTIAL.**
Federal: English designated official language by presidential action of 2025-03-01 (sec. 3(a)); page states no obligation on private employers (US-FED-020). EO number not printed on the fetched page (it is, to my knowledge, EO 14224; unconfirmed here). FLSA 29 CFR 516.2(a): lists records the employer keeps; it does NOT require a pay statement furnished to the employee and has no language provision (US-FED-010). So no federal instrument fixes payslip language or requires a federal pay statement; the governing constraints are state wage-statement laws (jurisdiction workers). Authority-facing filings: forms/instructions are in English; no language statute located. Confidence 85% federal.
NOT LOCATED: states with primary-language notice requirements (none fetched; unverified lead: New York wage-theft notice rule). Closing: per-state wage notice provision in US-MQ-20..70.
Non-statutory constraint proposal for languages.payslip_rule: "no federal rule; state pay-statement statute governs; en default, es seam optional" (proposal, not a finding).

## US-MQ-04 T4 discriminator
**Status: PARTIAL (federal side proven; state side partially).**
(a) Federal: 26 USC 3402(a)(1): every employer paying wages "shall deduct and withhold ... a tax determined in accordance with tables or computational procedures prescribed by the Secretary"; section covers federal tax only, state tax not mentioned (US-FED-012). FUTA 6% of wages for the calendar year (US-FED-013). FICA/FUTA returns are federal quarterly/annual returns to IRS (US-FED-015, US-FED-005, US-FED-007). 944 is a federal annual alternative.
(b) State: state UI is a separate state law and agency: FL Stat. 443.1216 (state UI statute, US-MULTI-001) shows a self-standing state tax-base definition with its own localization rules. NOT LOCATED: a representative state income-tax withholding statute (Ohio RC 5747.06 fetch failed: connection refused) and the state UI return statute. Confidence for (b): 70%, from absence of any state tax in IRC 3402 plus the state UI statute read; the "separate return to the state DoR" limb is common knowledge but not source-read here.
FUTA credit dependency: YES. 26 USC 3302(a)(1) credits state UI contributions; (c)(1) caps total credits at 90% of the tax; (c)(2) reduces the credit for states with outstanding Title XII advances (credit-reduction states); (g) relief mechanism (US-FED-014). So the federal FUTA result depends on state contributions paid and on the state's loan status. Closing for credit-reduction list: DOL annual determination (2026 credit reduction states published November; Form 940 Schedule A).
Keep T3 for futa as in the mandate.

## US-MQ-05 Devolved payroll-adjacent domains
**Status: PARTIAL.**
Federal anchors found: child-support/creditor garnishment limits, 15 USC 1673 (25% / 30x federal minimum wage; support 50/55 and 60/65%) (US-FED-011); new-hire reporting within 20 days to the State Directory of New Hires, and the state-issued income withholding notice, 42 USC 653a (US-FED-017).
NOT LOCATED (primary): the list of states with SDI/TDI/PFML, long-term-care (WA Cares), transit/workforce levies, state-fund workers' comp payroll deductions (DOL state paid leave pages 404; no state statute fetched); the federal Income Withholding for Support (IWO) form (OMB form) not fetched. Do not copy a state list from tier-3. Closing: state agency pages under US-MQ-20..70 (the answer for each jurisdiction question part 4), DOL Wage and Hour "state paid family and medical leave" page at its current URL, OCSE IWO form page.

## US-MQ-06 Indexation (federal)
**Status: PARTIAL.**
(a) Rev. Proc. 2025-32 (post-OBBBA modification of Rev. Proc. 2024-40) sets 2026 items "generally determined by reference to section 1(f)"; standard deduction MFJ 32,200 / HoH 24,150 / single and MFS 16,100; qualified transportation fringe 340/month (transit) and 340/month (parking); health FSA cap 3,400, carryover 680 (US-FED-002; text extracted and read locally). The CPI variant is NOT stated in the procedure text I read; the statute (IRC 1(f)(3), chained CPI-U) was not fetched, so the caliber is unproved here. Confidence 70% on caliber, 95% on the amounts quoted. OBBBA = Pub. L. 119-21 (4 July 2025) made the TCJA rate tables permanent (sec. 70101 as cited in the procedure).
(b) SSA: OASDI base 184,500 for remuneration paid in 2026 (FR notice 90 FR 49047, 2025-11-03, US-FED-003). Formula, SSA Act sec. 230(b): larger of (1994 base 60,600 x AWI(2024)/AWI(1992)) or current base (176,100), rounded to a multiple of 300. G-DERIVE reproduced: 60,600 x 69,846.57 / 22,935.42 = 184,548.71 -> 184,500 (Python check; matches the notice). AWI(2024) = 69,846.57. Pub. 15 2026 independently states "The social security wage base limit is $184,500" (US-FED-004, second document family). 6.2% x 184,500 = 11,439.00 maximum employee OASDI. Confidence 98%. The ssa.gov pages themselves returned 403.
(c) Other indexed limits: only fringe items above located. NOT LOCATED: 402(g) deferral limit, HSA 223 limits, Section 129/other: the IRS notices (not fetched). Closing: IRS "COLA increases for dollar limitations" notice for 2026 and Rev. Proc. 2025-19 (HSA).
2027: not checked (SSA 2027 notice and the 2027 Rev. Proc. were not searched in this scope). Mark `next_year` refresh open.

## US-MQ-07 Collective agreements
**Status: ANSWERED (federal).**
29 USC 159(a): a representative chosen by the majority in an appropriate unit "shall be the exclusive representatives of all the employees in such unit" (US-FED-018): a CBA binds the unit, not a sector; no extension mechanism to non-signatory employers appears in the statute. Davis-Bacon, 40 USC 3142: federal construction contracts over 2,000 USD require Labor Secretary prevailing wage determinations, paid at least weekly (US-FED-019). For a private-sector payroll build, prevailing wage is a contract-level overlay, not a sector rule; recommendation: out of scope except as an optional flag for covered public-works contracts (owner confirm). State prevailing-wage statutes: NOT LOCATED here (US-MQ-20..70). Confidence 90%. Supports collective_agreements = T1 (provisional label stands).

## US-MQ-08 Oracle
**Status: PARTIAL.**
IRS Tax Withholding Estimator is an employee tool producing a W-4/W-4P, not an employer payroll engine; it does NOT qualify (US-FED-021; page last reviewed 2026-06-27). Pub. 15-T 2026 (US-FED-001) contains the normative wage-bracket tables and Worksheets 1A/1B/3/5; the pages read contain only one worked example (nonresident alien adjustment) and no complete percentage-method or wage-bracket worked example with a resulting amount. So the official oracle = Pub. 15-T 2026 tables and worksheets (hand re-derivation), not a published set of worked examples. Confidence 75%. NOT LOCATED: any IRS payroll-withholding calculator. Pub. 15-T text (162,596 chars) read in two passes (0-100k, 100k-end), examples search negative. Closing: Pub. 15-T 2026 Part 1 introduction on percentage-method worksheet if a worked "Example" exists in the PDF edition; IRS "Publication 15-T" PDF extraction. Per-state oracle: jurisdiction workers.

## US-MQ-09 Third-party filing authorisation
**Status: PARTIAL (federal answered; state and owner parts open).**
Rev. Proc. 2012-32 (effective 2012-11-19; supersedes Rev. Proc. 2007-38) governs Form 8655 Reporting Agent Authorization: it lets the agent sign and electronically file Forms 940 and 941 and make federal tax deposits/payments on the employer's behalf (sec. 1.01). Liability: "An Authorization does not relieve the taxpayer of the responsibility (or from liability for failing) to ensure that all tax returns are filed timely and that all FTDs and FTPs are made timely" (sec. 5.05); the agent must give the employer a written statement advising of this, recommend EFTPS enrollment to verify deposits, and mention that state-level verification programs may exist (US-FED-008). Form 8655 current revision January 2024; Pub. 1474 (technical specifications for reporting agents, April 2026 revision) and Rev. Proc. 2012-33 are the related documents (US-FED-009). The 941/940 instructions also reference section 3504 agents and CPEOs filing aggregate returns (Schedule R) and the W-2 instruction mentions Form 2678 agents (US-FED-005/006): these are different appointments, where the employer-liability position differs; not analyzed here. Confidence 90% federal.
NOT LOCATED: state POA/agent forms (jurisdiction workers). Owner questions (provider name, input format): unanswerable by research; owner. SIR scope fact stands: Mercans produces provider input, employer retains liability.

## US-MQ-10 Multistate
**Status: PARTIAL.**
(a) Work-state sourcing vs residence: NOT LOCATED as a uniform rule (state-by-state). (b) Reciprocity pairs: only snippet leads, registered MANUAL tier-B (US-MULTI-002): PA-IN, MD, NJ; IL-IA, KY, MI, WI; MI-IL, IN; WI-IL, IN, KY, MI; IN-KY, MI, OH, PA, WI; DC-MD, VA. This list is incomplete and unverified: do not use as a source. Closing: FTA reciprocal-agreement list (403), plus the state statutes/DoR pages in US-MQ-20..70. (c) Resident credit and difference withholding: NOT LOCATED. (d) Convenience-of-employer: NY located by search only (US-MULTI-003, not fetched, MANUAL); other states (known leads NE, PA, DE, CT, AR) NOT LOCATED. (e) Day/dollar thresholds: NOT LOCATED. (f) SUI localization: Florida Stat. 443.1216(7)/(9)/(12) read (US-MULTI-001): employment includes the entire service if localized in the state, or if not localized in any state but some is performed there; localized if performed entirely inside, or outside service is incidental; reciprocal arrangement under s. 443.221. The base-of-operations / direction-and-control / residence tail of the test was not read (the fetch summary omitted it): confidence 75%. Federal limiting statute for mobile employees: NOT LOCATED (the 49 USC 14503 fetch returned page-not-found; no claim is made). Closing for (a)-(e): the 51 jurisdiction packs; for the federal statute, retry GovInfo/uscode for 49 USC 14503 and 40116, 46 USC 11108, 4 USC 114 (unverified leads from memory, treat as unproven).

## US-MQ-12 Special populations (federal layer)
**Status: PARTIAL.**
Read: nonresident aliens: Pub. 15 states employers "must withhold federal income taxes on the wages of nonresident alien employees"; NRA Form W-4 requires withholding as single and no exemption from withholding; Pub. 15-T gives wage add-on procedures by payroll frequency (US-FED-004, US-FED-001). Agricultural: employers of farm employees file Form 943, not 941; household employees: Schedule H, not 941 (US-FED-005, US-FED-007, US-FED-004 section headings include statutory employees, farmworkers, crew leaders). Statutory employees: appear in Pub. 15 headings; rule text not read.
NOT LOCATED: clergy, student FICA exemption, employees abroad (Pub. 15 read to 200,000 of 357,505 chars; Pub. 15-A and Pub. 51 not fetched). Closing: Pub. 15 sections 5-15 (offset 200000+), Pub. 15-A, Pub. 51, Pub. 54.
Proposal for owner (not a finding): IN scope = NRA, statutory employees, ordinary common-law employees; OUT or FLAG = household (Schedule H), agricultural (Form 943), clergy, employees abroad, pending owner confirmation per population.

---
## Notes for the scaffolder
- Nothing here requires editing MANDATE.md before the owner decides; recommended statuses: MQ-07 answered; MQ-01, 02, 03, 04, 05, 06, 08, 09, 10, 12 partial with the NOT LOCATED items listed above. Not touched: MQ-11, 13, 14, 20..70.
- Tier verdict impact: federal T2 (3402 federal-only, Pub 15-T) and FUTA T3 (3302 dependency) hold; T4 for state layer is supported by structure but its representative state statute citation is missing (MQ-04 b).
- Parallel shape for remaining work: state reciprocity, convenience rules, thresholds, SDI/PFML, primary-language notices and state POA forms are per-jurisdiction lookups (fan-out by state); federal gap closers (402(g)/HSA, 2027 SSA base and Rev. Proc., Pub 15 later sections, 49 USC 14503) are a short single-worker task. SSA and FTA pages were bot-blocked (403): use the human browser or the SSA FR notice.
- Key facts ready for a facts file (not emitted this pass): ss.ceiling.annual 184500 (US-FED-003, derived arithmetically, eff. 2026-01-01); stdded values (US-FED-002); fica rates 6.2%/1.45%/0.9% (US-FED-004; the 0.9% threshold amount not read); futa 6.0% less 5.4% credit, 7,000 base (US-FED-007, 2025 edition; 2026 Form 940 instruction unpublished).


## PASS 3 (Wayback copies, 2026-10-29)

Source: Wayback Machine archived copies of the official files (timestamp in each register row), read locally; figures below come only from the file text. Register shard rows updated to status active (wayback-copy verification).

### MI RAB 2017-13 (US-MULTI-002)
- Part 5 multistate: reciprocal agreements Michigan with WI (1967-10-01), IN and KY (1968-01-01), IL (1971-01-01), OH (1972-01-01), MN (1984-01-01); not applicable to local taxes or contractors; no state certificate (employer's own form). Approved 2017-06-01, copy 2026-05-17; see G3 for details.
