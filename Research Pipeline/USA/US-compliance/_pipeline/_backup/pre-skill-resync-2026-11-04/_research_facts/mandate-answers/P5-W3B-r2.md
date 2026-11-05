# Mandate answers P5-W3B-r2 - IA UT OK AR MS (PASS 4, wave 3B, round 2, 2026-10-29)
Shard: `00-official-sources/_register-shards/mandate-P5-W3B-r2.csv` (33 rows, ids US-<UF>-P5-2-NNN). Round 2 used other pages than round 1: statute and rule texts, agency tax-type index pages (scope pages for absence), income-tax return instructions and credit forms, the AR bill record, agency forms indexes, federal DOL paid-leave listings. PDFs saved under `00-official-sources/pdfs/<UF>/` and read with PyMuPDF (`python -I`). Chrome: one own tab, closed at the end; tax.utah.gov and laborcommission.utah.gov are behind a Cloudflare bot check (not solved, recorded gated). Wayback: HTTP 429 on every request this round (shared IP), retried once after 60 s, recorded as gated. About 8-12 page reads per state.

Absence-of-levy parts (part 4) rest on two federal DOL listings (rows `-P5-2-` "US DOL ... paid leave"), tier B, read 2026-10-29: neither names IA, UT, OK, AR or MS. They cover paid family/medical leave and temporary disability. LTC (Washington only) and any new 2026 programme are not covered by those pages, so confidence is Medium, not High.

## Iowa (IA)
- Part 2 local wage taxes: ANSWERED. No city/county wage tax in the DOR tax-guidance index (US-IAP52-003). School district surtax and EMS surtax (six counties) are settled on the IA 1040 by residence (US-IAP51-005); the employer does not withhold them: Iowa Code 2026 sec. 422.16 has no surtax text (US-IAP52-002) and the 2026 IA W-4 (44-019a, 11/13/2025) tells the employee to reduce allowances or add line-8 withholding (US-IAP52-001). Confidence High for the surtax, Medium for "no municipal wage tax" (state index page only).
- Part 4 other levies: ABSENCE PROVEN (listing scope). No SDI/PFML/LTC on the DOL lists (US-IAP52-004/-005). HF 2631 (premiums split 55/45) was an introduced bill only. Confidence Medium.
- Parts 1, 3, 5, 6: unchanged (answered in prior passes).

## Utah (UT)
- Part 1 wage income tax: PARTIAL. Utah taxable wages follow federal withholding wages with no W-4 allowance subtraction; schedules use 4.45% with a 1.3% phase-out, or whole-dollar tables (Pub 14 Rev. 04/26, Wayback copy; US-UTP52-001). The copy has no supplemental-wage rate and no rounding sentence (searched locally). The rule R865-9I-14/15 that the Pub cites could not be read (adminrules.utah.gov 404). The effective date of 4.45% is not on the copy; incometax.utah.gov shows 4.5 percent on the return from tax year 2025 - to reconcile. Confidence Medium for the method, Low for supplemental/rounding.
- Part 2 local: PARTIAL. Pub 14 "Who Must Withhold" names only Utah income tax; tax.utah.gov tax index not reachable (bot gate). Confidence Low-Medium.
- Part 4 other levies: ABSENCE PROVEN (listing scope). DOL lists do not name Utah; DWS UI rates page copy has only employer UI items (US-UTP52-005/-006/-007). Confidence Medium.
- Part 6: PARTIAL. Pay-statement statute: Utah Code 34-28-3 (statement of total deductions on each regular payday) only from a search extract; primary GATED (US-UTP52-002). Withholding POA TC-737: GATED (-003). UI POA: DWS POA.pdf named, 403 (-004). Calculator: none; Pub 14 schedules/tables. Prevailing wage: answered in round 1 (US-UTP51-001).
- Owner-assist URLs: https://le.utah.gov/xcode/Title34/Chapter28/34-28-S3.html ; https://tax.utah.gov/forms/current/tc-737.pdf ; https://jobs.utah.gov/ui/employer/Public/Forms/POA.pdf ; https://adminrules.utah.gov/public/rule/R865-9I-14/Current%20Rules

## Oklahoma (OK)
- Part 2 local: ABSENCE PROVEN (listing scope, Medium). OTC business tax-type list has no local wage tax (US-OKP52-003); OAC 710:90 (2026) has no "local" (US-OKP52-001).
- Part 4 other levies: ABSENCE PROVEN (listing scope, Medium). OESC 2026 numbers sheet: UI only, wage base $25,000.00, new employer 1.5%, range 0.2%-5.8% (US-OKP52-004); DOL lists do not name Oklahoma.
- Part 5 multistate: ANSWERED. Residents are employees whether services are inside or outside Oklahoma (OAC 710:90-1-3, US-OKP52-001); resident credit for tax paid to another state on Form 511-TX (2025), nonresidents do not qualify (US-OKP52-002); nonresident exclusion of $300 per quarter (68 O.S. 2385.1(4), US-OKP51-002); no reciprocity text in OAC 710:90 or OW-2. Confidence High for credit and scope, Medium-High for "no reciprocity".
- Parts 1, 3, 6: unchanged (answered).

## Arkansas (AR)
- Part 2 local: ABSENCE PROVEN (listing scope, Medium). DFA tax-type list: Withholding Wage Tax, no local income tax (US-ARP52-005).
- Part 4 other levies: ABSENCE PROVEN (listing scope, Medium). DOL lists do not name Arkansas; stabilization 0.2% sits inside the UI rate (US-ARP51-003).
- Part 5 multistate: ANSWERED. Resident credit: "Other State Tax Credit" on AR1000TC, line 36 of the 2025 AR1000F instructions (US-ARP52-001). Reciprocity: zero hits in those instructions and in the 2026 employer instructions; HB1116 (2025), which would have authorized reciprocity agreements and a 15-day / $2,500 nonresident threshold, died in House committee 2025-05-05, so none is in force (US-ARP52-002). Nonresident apportionment by working days and the Texarkana exemption stay per US-ARP51-002. Confidence High.
- Part 6: ANSWERED. Pay statement: no employee itemized-statement duty in 11 CAR Part 11 (07/21/2026 compilation, text searched) nor in the 2008 compilation (US-ARP52-006, US-ARP51-004); Medium. Withholding POA: DFA Power of Attorney (rev. Sept 2025), tax type entered on the form (US-ARP52-003). UI POA: none on the DWS/Reemployment forms list (US-ARP52-004), Medium. Prevailing wage: repealed 2017 (US-ARP51-001). Calculator: none; DFA formula/tables.

## Mississippi (MS)
- Part 2 local: ABSENCE PROVEN (listing scope, Medium-High). DOR "General Information" lists every tax administered (individual income, withholding, city utility taxes, ...) and no local income or wage tax (US-MSP52-001).
- Part 5 multistate: ANSWERED. Pub 89-700-25-1 (Rev. 07/25) Instructions section "Treatment of Residents and Nonresidents": nonresidents withheld on Mississippi-sourced wages (apportioned by earnings ratio); nonresident with Mississippi principal place of employment withheld on total wages unless the other state requires withholding; residents working elsewhere withheld on unless the other state requires it; zero reciprocity text (US-MSP52-002, supersedes US-MSP51-005). Resident credit for tax paid to another state, based on actual liability not withholding (DOR FAQ, US-MSP52-003). No day/dollar threshold stated. Confidence High for rules, Medium-High for "no reciprocity".
- Part 6: ANSWERED with caveats. Pay statement: Title 71 ch. 1 table of contents (Justia mirror, read in Chrome) has no itemized-statement section; secondary source, Medium (US-MSP52-004). Withholding POA: DOR Form 21-002 (US-MSP51-006, text not read). UI agent form: J-9 Reporting Agent Authorization on the MDES forms list, PDF has no extractable text -> unreadable-pdf (US-MSP52-005). Calculator: DOR withholding tables in Pub 89-700-25-1. Prevailing wage: none (US-MSP51-001).
- Parts 1, 3, 4: unchanged (answered in prior passes; 2026 Workforce Training rate caveat of round 1 stands).

## PASS 4 (wave 3B round 2) - status after this pass
| State | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| IA | answered | answered | answered | absence_proven | answered | answered |
| UT | partial | partial | answered | absence_proven | answered | partial (gated) |
| OK | answered | absence_proven | answered | absence_proven | answered | answered |
| AR | answered | absence_proven | answered | absence_proven | answered | answered |
| MS | answered | absence_proven | answered | answered (caveat) | answered | answered (caveats) |
