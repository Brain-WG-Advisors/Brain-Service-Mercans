# Mandate answers P5-W2B-r1 - WA, SC, MN, AZ, WI (Pass 4, wave 2B, 2026-10-29)

Register shard: `00-official-sources/_register-shards/mandate-P5-W2B-r1.csv` (ids US-<UF>-P5-1-NNN). Method: WebFetch (statutes; summarizer quotes marked), Chrome own tab (get_page_text), Wayback copy read in Chrome (AZ), official PDFs saved by the WebFetch tool and read locally with PyMuPDF (`python -I`). Blocks met: dwd.wisconsin.gov and revisor/legis hosts refused Node fetch in places; docs.legis.wisconsin.gov ECONNREFUSED (also no load in Chrome tab); app.leg.wa.gov Chrome permission denied (WebFetch worked); paidleave.mn.gov human-verification wall (gated, no Wayback copy); uimn.org not loadable and not archived; revenue.wi.gov page `.../FAQS/ise-withhold.aspx` 404; azdor.gov direct 403 (Wayback copy 2026-10-09 read). The summarizer-quoted rows are method `webfetch quote (summarizer)`; re-read in Chrome when the owner can.

Parts still missing before this pass (manifest): WA 2,6; SC 1,2,4,5,6; MN 1,2,3,4,6; AZ 1,2,3,4,6; WI 1-6.

## WA - US-MQ-67 (parts 2,6)
2. Local wage taxes: ANSWERED. No local tax is withheld from wages; the only local payroll-based levy located is Seattle's payroll expense tax, an employer business tax (SMC 5.38; 2026 thresholds 9,074,409 payroll in 2025 and one employee at 194,452+), quarterly, with a Taxpayer Authorization Form for payroll processors [US-WA-P5-1-001], H. State income tax on wages: none (US-WA-PIT-001). Absence for other WA cities is not proven by a statewide page.
6. ANSWERED. Pay statement WAC 296-126-040 (US-WA-LAB-001); prevailing wage RCW 39.12.020, L&I [US-WA-P5-1-002], M (summarizer); UI POA / TPA form per client (US-FIL-016, earlier pass); withholding POA: not applicable (no wage tax); calculator/oracle: none, no wage income tax. Confidence M-H.

## SC - US-MQ-60 (parts 1,2,4,5,6)
1. PARTIAL (80%). Certificate SC W-4 2026, formula WH-1603F re-read locally [US-SC-P5-1-002]; rounding: employer may compute wages to the nearest dollar, SC Code 12-8-520 [US-SC-P5-1-001, M]; threshold 1,000 expected annual wages. Supplemental/bonus rate: NOT LOCATED after reading WH-1603F, WH-105, the SCDOR withholding page summary and 12-8-520 (no such rule in them); SC Regulation not read.
2. Local: OPEN. No local wage tax is mentioned in WH-105 or the SCDOR page; absence not proven (no statewide statute/page stating it).
4. SDI/PFML/other: OPEN. SC has no programme in any page read; absence not proven.
5. PARTIAL. SC resident working in another state: other state's tax withheld; if no income tax there, SC tax withheld [US-SC-P5-1-003, WH-105 Rev. 2/13/23, H]; nonresident working in SC taxed by SC (US-SC-001). Reciprocity: none stated in WH-105 or the page. Credit statute 12-6-3030 not reached (title 12 ch.6 page too long; not read).
6. PARTIAL (75%). Pay statement SC Code 41-10-30 [US-SC-P5-1-004, M]; prevailing wage: none in chapter 41-10, state-wide absence not proven; POA: SCDOR POA form NOT LOCATED (URL guess 404); calculator: none, WH-1603 tables and WH-1603F worked example.

## MN - US-MQ-43 (parts 1,2,3,4,6)
1. ANSWERED. Supplemental payment off-cycle 6.25 percent; rounding to nearest dollar at employer election above the highest bracket, Minn. Stat. 290.92 subd. 2a [US-MN-P5-1-001, M]; W-4MN and reciprocity in US-MN-PIT-001.
2. Local: OPEN (no read).
3. PARTIAL (60%). Taxable wages = 60 percent of state average annual wage rounded to 1,000 (2026 figure not read); employer-only payment; new employer rate not less than 1 percent [US-MN-P5-1-003, M]. uimn.org not loadable.
4. PARTIAL (40%) with CONFLICT. Minnesota Paid Leave: statute summarizer reading 0.7 percent, 50 percent minimum employer share, SS wage cap [US-MN-P5-1-002]; earlier lead 0.88 percent; official page gated. NOT answered; do not model.
6. PARTIAL (65%). Pay statement Minn. Stat. 181.032 (US-MN-PAY-001); prevailing wage Minn. Stat. 177.42-177.44, DLI [US-MN-P5-1-004, M]; POA/third-party form: NOT LOCATED; calculator: DOR withholding calculator exists in e-Services (WebFetch of revenue.state.mn.us/withholding-tax, summary only).

## AZ - US-MQ-23 (parts 1,2,3,4,6)
1. ANSWERED. Percentage election (0.5-3.5 percent of gross taxable wages), A-4 within 5 days else 2.0 percent default, zero election renewed annually, bonuses fall under the same percentage because the base is gross taxable wages [US-AZ-P5-1-001/-002, H]; A.R.S. 43-401 tables, bonus named in the statute [US-AZ-P5-1-003, M]. Rounding: NOT LOCATED in the pages read.
2. Local: OPEN. ADOR page lists no local wage tax; absence not proven by an explicit statement.
3. PARTIAL. Wage base 8,000 and new employer rate 2.0 percent (US-AZ-UI-001); A.R.S. 23-727 shows employer-paid contributions [US-AZ-P5-1-005, M]; employee contribution absence is an inference.
4. OPEN. No SDI/PFML found in any AZ page read; absence not proven.
5. (not in manifest list) Reciprocal exemption by Form WEC: CA, IN, OR, VA residents; 60-day nonresident rule [US-AZ-P5-1-002].
6. PARTIAL (60%). Pay statement: A.R.S. 23-351 (statement of earnings and withholdings for direct deposit/payroll card) and 23-364(D) [US-AZ-P5-1-004, M]; prevailing wage: NOT LOCATED; POA / payroll service company authorization: gated (Cloudflare, earlier pass), not solved; calculator: none, percentage election.

## WI - US-MQ-68 (parts 1-6)
1. ANSWERED (85%). W-166 (1/26) read locally [US-WI-P5-1-001, H]: WT-4, supplemental wages with regular wages or flat percentages 3.54/4.65/5.30/7.65 by estimated annual gross, alternate method formula, calculator (US-WI-PIT-002). Caveat: guide tables are headed "withholding periods on or after 2022-01-01" and rates "continue for 2025"; no rounding rule located in the 63 pages.
2. Local: OPEN. W-166 contains no local wage tax text; absence not proven.
3. PARTIAL (65%). Wage base 14,000 and quarterly reporting, UI handbook UCB-201-P R. 03/16/2026 [US-WI-P5-1-003, H]; new-employer rates US-WI-SUI-001; employee contribution absence not proven.
4. OPEN. No WI SDI/PFML text located; absence not proven.
5. ANSWERED. Reciprocity IL, IN, KY, MI via Form W-220; special MN arrangement for WI residents working in MN; disaster-responder exemption; nonresidents of non-reciprocal states under 1,500 expected WI earnings not withheld [US-WI-P5-1-001, H]. Convenience rule: none in the guide.
6. PARTIAL (50%). UI POA form UCT-8291-E [US-WI-P5-1-002]; wage statements: Pub 117 referenced (US-WI-PIT-002), statute not read (docs.legis.wisconsin.gov unreachable); withholding POA form, prevailing wage (Wis. Stat. 103.49) not read; calculator US-WI-PIT-002.

## Summary
Answered: WA 2/2 missing parts; AZ 1/5; MN 1/5; WI 2/6; SC 0/5 fully (1,5,6 partial). Browser tab closed at end. Nothing written to MANDATE.md or build-manifest.json.
