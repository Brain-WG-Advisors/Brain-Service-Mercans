# PASS 4 (wave 3C, round 2) - NE, NH, ME, HI, DE

Date 2026-10-29/30. Hunter: compliance-source-hunter. Shard: `00-official-sources/_register-shards/mandate-P5-W3C-r2.csv` (20 rows, ids US-<UF>-P5-2-NNN). Local copies under `00-official-sources/pdfs/<UF>/` (files ending `_wb`).
Different approach from round 1: Wayback copies of other official pages (agency FAQ, forms index, tax list, booklet under its current file name), statute sites (legislature.maine.gov, nebraskalegislature.gov, capitol.hawaii.gov, gc.nh.gov) and agency forms indexes. No Chrome tab was needed, none opened. No CAPTCHA. Wayback requests spaced 10 s, no 429.

## ME - Maine
1. ANSWERED (US-ME-P5-2-001, -002; supersedes detail of US-ME-P5-1-003). The 2026 booklet exists under `26_wh_tab_instr.pdf` (revised Dec 2025; round 1 searched the wrong file name). Percentage method, single schedule 5.80% below 27,400 / 1,589 + 6.75% to 64,850 / 4,117 + 7.15% above; 2026 personal exemption 5,300; standard deduction as adjusted in the booklet; W-4ME status box decides married vs single table; federal W-4 Step 4(b) not used; round to nearest dollar; supplemental paid separately flat 5%, with regular wages aggregated. Effective 2026-01-01. Confidence H. Open: married schedule and the exact adjusted deduction amounts not transcribed; a search-result item (EY, 26 Aug 2026) says MRS added a surcharge on income above 1 million to the formula: not read in the booklet text extracted (grep "million" found nothing), so the surcharge is unverified here.
2. PARTIAL (US-ME-P5-2-010). The MRS list of all taxes and the withholding booklet/FAQ mention no municipal income tax. Not proven by a statute that municipalities cannot levy one. Confidence M.
3. (unchanged, round 1: US-ME-P5-1-001.)
4. (unchanged, round 1; PFML 2026 applied rate still open.)
5. ANSWERED (US-ME-P5-2-003, -004, -005). Nonresident: more than 12 days present AND more than 3,000 gross Maine-source in the year (36 MRSA 5142(8-B); booklet instruction 3, effective 2026). Resident credit: 36 MRSA 5217-A. Reciprocity: 5250(3) allows agreements conditioned on reciprocity; no agreement is listed in the booklet or MRS pages: none identified. Convenience rule: none found. Confidence M-H (subsection texts via fetch summary).
6. ANSWERED with one absence (US-ME-P5-2-006..009, -001). Pay statement: ABSENCE PROVEN in the section index of 26 MRSA ch.7 sub-ch.2 (621-A to 640) plus full text of 621-A/622/664 (round 1): records duty only. Prevailing wage: 26 MRSA 1304/1306, Director of the Bureau of Labor Standards. POA: withholding Form 2848-ME (round 1) and booklet processor-POA guidance; UI Form ME UC-28 (2018). Processor licensing: Bureau of Consumer Credit Protection (booklet; FAQ Q17). Oracle: none listed; booklet tables. Confidence H except 1306 not read.

## NE - Nebraska
4. ABSENCE PROVEN (US-NE-P5-2-001). DOR business-tax menu and the full withholding resource list show no SDI/TDI/PFML/other employee levy; NDOL employer guide is UI only, employer-paid. Confidence M-H (agency lists, no explicit negative statute).
6. ANSWERED (US-NE-P5-2-002, -003 + round 1 US-NE-P5-1-004). Pay statement 48-1230(2) and Form 33 / NDOL UI POA (round 1). Prevailing wage: chapter 73 full text read, no state prevailing-wage rate statute; 73-102 fair labor standards statement only (chapter 48 not searched). Oracle: none on the DOR page; Circular EN tables. NDOL UI POA still snippet-level from round 1 (Wayback copy of the page exists locally, form text not re-read this round).

## NH - New Hampshire
6. PARTIAL (US-NH-P5-2-001, -002). Pay statement confirmed on the DOL FAQ (RSA 275:49 IV, Lab 803.03(f)). Prevailing wage: RSA ch.279 read, nothing; state statute not located and the DOL FAQ has no entry (not proven absent in the rest of Title XXIII). Withholding POA/oracle: not applicable, no wage income tax. UI agent authorisation: NHES form NHES-0041 and rule Emp 303.10 appeared only as search results; the PDF is not in the Wayback archive and the live host returns 403 to WebFetch. Gated URL for the owner: https://mm.nh.gov/files/uploads/nhes/documents/nhes0041.pdf. Confidence M.

## HI - Hawaii
6. ANSWERED (US-HI-P5-2-001, -002, -003). Pay statement: HRS 387-6(c) read in full from the statute page (per-pay-period statement with 14 elements; electronic allowed with written employee consent) in addition to 388-7(4). Prevailing wage: HRS 104-2 (contracts over 2,000, director sets rates). POA: withholding Form N-848 (round 1); UI: online employer profile can authorise CPA/service company, UC-25 SIDES agent, POA no longer required for SIDES TPAs (agency pages via fetch tool, not saved). Oracle: none; Booklet A tables. Confidence H for statutes, M-H for UI pages.

## DE - Delaware
2. ANSWERED (US-DE-P5-2-001; supersedes the open rate in US-DE-P5-1-004). Wilmington earned income tax 1.25% on residents (wherever earned) and on nonresidents for work in the City, since 1978-07-01 (Regulations rev. 5/25/2023, sec. 201). Collected by the City Department of Finance, separate from the state return; employers withhold, quarterly returns and annual reconciliation/W-2. No other Delaware local wage tax found (statutes 22 Del. C. 901-902 round 1). Confidence H.
6. ANSWERED (US-DE-P5-2-002 + round 1). Pay statement 19 Del. C. 1108(4) and prevailing wage 29 Del. C. 6960 (round 1). UI POA: DUI Power of Attorney form read. Withholding POA: the Division of Revenue forms index lists only IRS 2848 and ATH-RTF (release of information), so no Delaware withholding POA exists on the index. Oracle: none; Employer Guide tables (undated guide, round-1 caveat stands). Confidence M-H.

## Status after round 2
DE 1:answered 2:answered 3:answered 4:answered 5:answered 6:answered
HI 1-5:answered 6:answered
ME 1:answered 2:partial 3:answered 4:answered 5:answered 6:answered
NE 1-3:answered 4:absence_proven 5:answered 6:answered
NH 1-5:answered 6:partial
Gated/unread: nhes0041.pdf (NH, 403 and not archived); maine.gov 1 million surcharge (EY item, not in booklet text); MRS Rule 803/806 not opened (statute and booklet used instead).
Note for the team: the shared scratchpad is used by parallel agents; this round created `wb.sh` and `txt.py` there (txt.py may have been overwritten by another worker) and did not touch other workers' files knowingly.
