# Mandate answers P5-W3B-r1 - IA UT OK AR MS (PASS 4, wave 3B, round 1, 2026-10-29)
Shard: `00-official-sources/_register-shards/mandate-P5-W3B-r1.csv` (26 rows, ids US-<UF>-P5-1-NNN). Only parts listed as missing in `build-manifest.json` (IA 2,4,6; UT 1,2,4,5,6; OK 2,4,5,6; AR 2-6; MS 2-6) were worked. Method: WebFetch/WebSearch on official hosts, PDFs saved under `00-official-sources/pdfs/<UF>/` and read locally with PyMuPDF (`python -I`), one Chrome tab (le.utah.gov, refused; tab closed). Wayback: 1 request, HTTP 429, retried once after 45 s, 429 again -> recorded as gated (shared IP). About 8-10 page reads per state. No CAPTCHA seen.

Prevailing wage (part 6, all five states): US DOL WHD "State Prevailing Wage Laws" page (dated 2023-01-01) lists IA, MS as without law, UT repealed 1981, OK invalidated by 1995 court decision, AR repealed 2017. Register ids US-IA/UT/OK/AR/MS-P5-1-001. Tier B government summary; confidence Medium (page dated 2023; later changes not checked).

## Iowa (IA) - missing 2, 4, 6
- Part 2 local wage taxes: PARTIAL. No city/county wage tax located. School district surtax and EMS surtax (six counties: Appanoose, Cass, Pocahontas, Sac, Shelby, Winnebago) are computed on the individual return by residence on last day of tax year (IA 1040 line 19, 2025 return); the page does not mention employer withholding. US-IA-P5-1-005. Confidence Medium. Gap: no Iowa primary text read that says employers do not withhold the surtax.
- Part 4 other levies: PARTIAL / OPEN. No enacted SDI/PFML/LTC programme located; search returned only introduced bills (HF 2631, family/medical leave premiums 55/45 split) which are NOT law. Absence not proven from a primary read. Confidence Low.
- Part 6: ANSWERED. Pay statement: Iowa Code 91A.6(4) statement of hours, wages, deductions on each regular payday; 91A.6(3) itemized statement within 10 working days of request (US-IA-P5-1-002, High). Prevailing wage: none for private employers (-001). POA withholding: IA 2848 form 14-101a (06/18/2026) (-003). POA UI: IWD form 68-0092 (12-2025) / myIowaUI (-004). Calculator/oracle: none located; re-derive from the Iowa withholding formula (US-IA-001).

## Utah (UT) - missing 1, 2, 4, 5, 6
- Part 1 wage income tax: PARTIAL. Pub 14 Rev. 04/26 (Wayback copy 2026-07-13) schedules use 4.45% with a 1.3% allowance phase-out, federal W-4 basis, no W-4 allowance subtraction (US-UT-P5-1-001, High for method). Not found in the copy read: supplemental-wage rate and rounding rule. Effective date of 4.45% still rests on a search summary (US-UT-PIT-004).
- Part 2 local wage taxes: OPEN. Pub 14 and DWS page name none; absence not proven by a primary statement. Confidence Low.
- Part 3 SUI (already answered): addendum US-UT-P5-1-003 adds 2026 social cost .001, reserve factor 1.10, 1.0% delinquency surcharge.
- Part 4 other levies: PARTIAL. DWS page shows only the UI surcharge/social cost; no SDI/PFML mentioned. Utah Code 34-28 statute not read. Confidence Low-Medium.
- Part 5 multistate: ANSWERED. 20-day nonresident exclusion (Utah Code 59-10-402, 59-10-117.5), resident credit via reduction by other-state withholding, employer 60-day exemption; no reciprocal agreements listed in Pub 14. US-UT-P5-1-002, Medium-High.
- Part 6: PARTIAL. Prevailing wage ANSWERED (-001). Pay-statement statute: GATED (le.utah.gov ECONNREFUSED in WebFetch and Chrome; Wayback 429; justia and laborcommission.utah.gov 403); search summary only, section number unverified (US-UT-P5-1-004). Withholding POA: TC-737 named by search result, URL 403/404, unreadable (-005). UI POA form: not located. Calculator: none; use Pub 14 schedules.
- Owner-assist URLs: https://le.utah.gov/xcode/Title34/Chapter28/34-28-S3.html ; https://tax.utah.gov/forms/current/tc-737.pdf

## Oklahoma (OK) - missing 2, 4, 5, 6
- Part 2 local wage taxes: PARTIAL. Neither OW-2 (Rev. 11-2025) nor OAC 710:90 (2026, read in full text) mentions local taxes; absence not proven by an affirmative statement. US-OK-P5-1-002/-003. Confidence Medium-Low.
- Part 4 other levies: OPEN. Only search results about state-employee HealthChoice disability (not a payroll levy); no primary statement that Oklahoma has no SDI/PFML. Confidence Low.
- Part 5 multistate: PARTIAL. 68 O.S. 2385.1(4): nonresident with services in the state and income not more than $300 per calendar quarter is excluded (US-OK-P5-1-002, High, effective 2026-01-01). No reciprocity and no resident-credit language located in OW-2/OAC 710:90.
- Part 6: ANSWERED. Pay statement: 40 O.S. 165.2 (US-OK-003, existing). Prevailing wage: none (-001). POA withholding: BT-129 (Rev. 7-2026) (-004). POA UI: OES-190T (Rev. 11-25) / OES-190B benefits (-005). Calculator: OTC OW-2 tables/percentage method (US-OK-001); no separate oracle located.

## Arkansas (AR) - missing 2, 3, 4, 5, 6
- Part 2 local wage taxes: PARTIAL. DFA Employer's Instructions (Eff. 01/01/2026, Rev. 4/27/26) name only the state tax (3.7%; supplemental 3.7%); no local tax mentioned; Texarkana border-city exemption (Ark. Code 26-52-604). US-AR-P5-1-002. Confidence Medium.
- Part 3 SUI: ANSWERED. 2026 wage base $7,000; new employer 2.0%; range 0.2%-5.1% (deficit 6.1/8.1/10.1%); stabilization 0.2%; no employee contribution on the page. US-AR-P5-1-003 (WebFetch of reemployment.arkansas.gov, redirect from dws). High-Medium.
- Part 4 other levies: PARTIAL. Stabilization rate 0.2% is inside the UI rate; no SDI/PFML located. Confidence Low-Medium.
- Part 5 multistate: PARTIAL. Nonresident wages for Arkansas-performed services withheld, apportioned by working days; Texarkana TX/AR residents exemption; no reciprocal agreement named. US-AR-P5-1-002. Resident-credit text for AR residents working elsewhere not read.
- Part 6: PARTIAL. Prevailing wage ANSWERED (-001, repealed 2017). Pay statement: AR DOL statutes compilation (rev. 2008) shows only records-keeping (11-4-217), no employee pay-statement duty (US-AR-P5-1-004, Medium; 2008 revision). POA forms (DFA withholding, DWS) NOT located (DFA withholding page and instructions silent). Calculator: none; DFA formula/tables.

## Mississippi (MS) - missing 2, 3, 4, 5, 6
- Part 2 local wage taxes: PARTIAL. DOR withholding page and Pub 89-700-25-1 (Rev. 07/25) mention no local income tax; absence not stated affirmatively. US-MS-P5-1-005. Confidence Medium-Low.
- Part 3 SUI: ANSWERED. Wage base $14,000 (Code 71-5-353(4); UI-2/3 header); new employers 1.0%/1.1%/1.2% (MDES page; statute); experience range 0.0%-5.4%; paid by employer. US-MS-P5-1-002/-003. High (statute copy dated 2024-02-15; rates page read 2026-10-29).
- Part 4 other levies: ANSWERED with caveat. Workforce Investment and Training contributions 0.20% of taxable wages (0.15% WET + 0.01% OWD + 0.04% Mississippi Works, the last only when general experience rate < 0.2%), employer-paid, added to the UI rate; MDES page says it "might be applicable for the rate year" so the 2026 rate is not confirmed. US-MS-P5-1-004. Medium. No SDI/PFML located.
- Part 5 multistate: PARTIAL. Withholding applies to residents, nonresidents and nonresident aliens on Mississippi-taxable wages (Pub 89-700-25-1); no reciprocal agreement named. US-MS-P5-1-005. Medium-Low.
- Part 6: PARTIAL. Prevailing wage ANSWERED (-001). Pay-statement statute: NOT LOCATED after search of MDES law and DOL pages (no itemized-statement duty found; Title 71 ch. 1 text not read). Withholding POA: DOR Form 21-002 listed on DOR page (-006, form text not read). UI agent form NOT located. Calculator: DOR withholding tables in Pub 89-700-25-1 (US-MS-PIT-001).

## PASS 4 (wave 3B) - status after this pass
| State | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| IA | answered (prior) | partial | answered (prior) | partial | answered (prior) | answered |
| UT | partial | open | answered | partial | answered | partial |
| OK | answered (prior) | partial | answered (prior) | open | partial | answered |
| AR | answered (prior) | partial | answered | partial | partial | partial |
| MS | answered (prior) | partial | answered | answered (caveat) | partial | partial |
