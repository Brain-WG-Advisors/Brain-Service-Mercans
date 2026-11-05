# LANG-5 - US-MQ-03 (language) and US-MQ-05 part c (transit / workforce levy) - TN TX UT VA VT WA WI WV WY

Pass date 2026-10-30. Shard: `00-official-sources/_register-shards/mandate-LANG-5.csv` (ids US-<UF>L-NNN). Method: statute text or agency page read (local saved copies by keyword scan with PyMuPDF `python -I`; live pages in Chrome own tab; no javascript_tool, no filter evasion, no CAPTCHA). Several state hosts (le.utah.gov, code.wvlegislature.gov, legislature.vermont.gov, lni.wa.gov) redirect to fbi.gov or are gated from this network; Wayback 2025/2026 copies used where readable.

Question A = does a state statute/rule require a wage notice, pay statement or employment notice in a language other than English (or the employee primary language)? Question B = transit tax or workforce/training levy on wages outside SUI.

| State | A (language) | B (transit / workforce levy outside SUI) | Register ids | Confidence |
|---|---|---|---|---|
| TN | no language clause in the Wage Regulations Act poster (50-2-101/103/202) or DLWD wages page read; no pay-statement duty; T.C.A. full text not readable | none: DOR full tax list and DLWD employer tax section list only UI | US-TNL-001, US-TNL-002 | A Medium (70%); B High (85%) |
| TX | rule: Labor Code 61.006 (TWC notices under ch. 61 in the two most common languages; agency duty) and 61.017(d)(1)(B)(i) (payroll card fee list in English or in the other language the employer offers); no pay-statement statute, so no payslip-language rule | none outside UI; Employment and Training Investment Assessment 0.10 pct sits inside the UI return and is offset in the replenishment rate (US-TXR3-003) | US-TXL-001, US-TXL-002 | A High (95%); B High (90%) |
| UT | UPDATED 2026-10-30 (P6): 34-28-3 (version effective 2014-05-13, the only Current version in the 2026-05-19 index) read: statement of each deduction every payday; construction-trades items; NO language clause [US-UTP6-001, A.1]. Residual: change after 2026-05-19 not verified. | no transit/training levy found on DWS rates page or Pub 14; state tax-type list bot-gated | US-UTP6-001 (replaces US-UTL-001 gated), US-UTL-002 | A 85%; B Medium-Low (60%) |
| VA | no language clause in 40.1-29 (subsection D read); PFML SB2 text not read; DOLI postings page not reached | none found; Virginia Tax tax-type list not reached (VEC and withholding pages only) | US-VAL-001, US-VAL-002 | A Medium (75%); B Medium-Low (65%) |
| VT | rule: 21 V.S.A. 342(f) payroll-card disclosures in the employee primary language or a language the employee understands (payroll-card disclosures only); 483(j) earned sick time notice has no language clause; no wage-statement statute | none transit/training; only the Child Care Contribution 0.44 pct employer payroll tax (other levy), HCFCA, USC | US-VTL-001, US-VTL-002, US-VTL-003 | A High (90%); B High (85%) |
| WA | no language clause in WAC 296-126-040 or RCW 49.46.210; PFML poster/insert offered in Spanish and other languages but page states no non-English mandate (RCW 50A and L&I postings not read) | none transit/training on wages: DOR list of 44 other taxes has only RTA (motor vehicle excise); EAF 0.02-0.03 pct inside UI; PFML, WA Cares, workers comp are insurance premiums; Seattle payroll expense tax is a local employer tax | US-WAL-001 to US-WAL-004 | A Medium (70%); B High (85%) |
| WI | rule: Wis. Stat. 103.915(8) migrant worker recruiting disclosure and work agreement in English and the worker language (not the pay statement); no language clause in 103.457 or DWD 272.10 | none: DOR Businesses programme list read in full; UI employer-only | US-WIL-001, US-WIL-002, US-WIL-003 | A High (88%); B High (88%) |
| WV | no language clause in 21-5-3 or 21-5-9 (saved official PDF copies, read); live host unreadable (302 to fbi.gov) | none state-level (Tax Division business menu); municipal Charleston city service fee USD 3.00/week is a user fee, not transit/training | US-WVL-001, US-WVL-002 | A Medium-High (80%); B High (85%) |
| WY | no language clause in W.S. Title 27 (270-page keyword scan; 27-4-101(b) read) | no separate levy; the UI adjustment factor (27-3-505(a)) is allocated 60 pct employment support fund and 20 pct workforce development training fund, collected inside the UI contribution; Revenue list not reached | US-WYL-001, US-WYL-002 | A High (88%); B Medium (70%) |

## Gaps for the owner
- UT: statute 34-28-3 text and the Utah Labor Commission postings page (gated); the Utah tax-type list (bot-gated).
- VA: SB2 (2026) PFML chapter text (script-rendered) and DOLI postings; Virginia Tax tax-type list.
- WA: RCW 50A notice provisions and L&I required-postings page (lni.wa.gov unreachable).
- TN: T.C.A. 50-2-103 full text (Lexis).
- Labor-agency required-postings pages were not located for WI, VA, UT, WV, WY, TN; answers rest on the wage-payment provisions plus the poster/agency pages named above.
- WA and VA statute checks used WebFetch page reads (fetch-model summary), hence Medium.

## Rule candidates for MQ-03 (CCG rows)
Employer-facing language rules found in these nine states: TX 61.017(d) (payroll card fee list), VT 342(f) (payroll card disclosures), WI 103.915(8) (migrant work agreement). None fixes the language of the pay statement itself.
