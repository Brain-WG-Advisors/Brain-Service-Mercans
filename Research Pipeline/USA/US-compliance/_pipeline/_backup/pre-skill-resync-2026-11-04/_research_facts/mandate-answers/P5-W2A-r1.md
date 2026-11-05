# Mandate answers P5-W2A-r1 - NJ MA VA TN IN (PASS 4, wave 2A, 2026-10-29)

Hunter: compliance-source-hunter. Parts worked = blocking list in build-manifest.json minus earlier PASS sections. Register: `00-official-sources/_register-shards/mandate-P5-W2A-r1.csv` (29 rows). Method per row in `verification_method`. Wayback copies saved under `00-official-sources/pdfs/<UF>/`. Chrome: own tab, get_page_text/find only, no javascript_tool; closed at end. Wayback: 1 request per >=10 s, no 429.
Blocked in Chrome this wave: malegislature.gov (tab bounced back; used Wayback), mass.gov Circular M PDF (unreadable-pdf; used Wayback), lis.virginia.gov loaded (SB2 read). WebFetch 403: mass.gov, vec.virginia.gov, newarknj.gov; ECONNRESET: tn.gov via WebFetch (Chrome worked); ECONNREFUSED pub.njleg.gov.

## NJ - New Jersey (US-MQ-51) - missing 1,2,4,6 -> 1 answered, 4 answered, 2 and 6 partial
1. ANSWERED (US-NJP51-001/002). NJ-WT Sept 2025 (still the /current/ file): wage amounts may be rounded to the nearest dollar (p.24); supplemental wages with regular pay taxed on the combined payment, paid separately withheld without exemption allowances (p.11); NJ-W4; percentage tables for wages paid on/after 2020-10-01. No calculator located; oracle = percentage tables. Confidence M-H (2026 edition not found).
2. PARTIAL. NJ-WT lists no local wage tax. Only lead: Newark 1% employer payroll tax (employer-paid, not withheld) US-NJP51-005, search summary only, Newark 403 and njleg refused = gated, not usable as a figure.
4. ANSWERED (US-NJP51-003/004). Worker 2026 calendar year: UI 0.3825%, WF/SWF 0.0425% (UI/WF/SWF wage base 44,800), DI 0.19%, FLI 0.23% (base 171,100). Confirmed by arithmetic on Treasury notice M-6025 (8-2026): 190.40, 325.09, 393.53. Confidence H.
6. PARTIAL. Pay statement: N.J.S.A. 34:11-4.4 text still not read in full (existing US-NJ-003 excerpt). Prevailing wage: Act N.J.S.A. 34:11-56.25 ff, Commissioner of Labor, certified payroll 10 days (US-NJP51-007). POA: Form M-5008-R exists (listing only, US-NJP51-006); UI Employer Access TPA delegation (listing). Oracle: none; re-derive from percentage tables.

## MA - Massachusetts (US-MQ-39) - missing 1-6 -> 1,3,4,5,6 answered, 2 partial
1. ANSWERED (US-MAP51-001/002/003). 5.0% from 2026-01-01; surtax threshold 1,107,750 (9% above); W-4 plus M-4; Circular M tables or percentage method; supplemental wages: 5% (9% on the part above the threshold); rounding to nearest dollar at employer election (830 CMR 62B.2.1(8)). Confidence H.
2. PARTIAL. Guide and 830 CMR 62B.2.1 contain no local tax; no page states "no municipal income tax" explicitly. Treat as none (low-risk) pending an explicit source.
3. ANSWERED (US-MAP51-004/005). 2026 new employer 2.42%, construction 6.08%; wage base 15,000 (c.151A s.14(a)(4)). No employee share on pages. Confidence H.
4. ANSWERED (US-MAP51-006). PFML 2026 0.88% (25+ employees) / 0.46% (<25), employee up to 100% of family 0.18% + 40% of medical 0.28%; cap = Social Security maximum. 2027 split changes (Ch.101 Acts 2026). Confidence H.
5. ANSWERED (US-MAP51-002 (9)(b), -001). No reciprocity list found; resident with other-state tax withheld: MA withholding reduced by the other-state amount; nonresident taxed on MA services; non-MA employers withhold MA less home-state withholding. Day/dollar thresholds not stated. Confidence M.
6. ANSWERED (US-MAP51-007/008/009). Pay slip c.149 s.148; prevailing wage c.149 s.26 (commissioner); POA Form M-2848 plus MassTaxConnect third-party access; payroll service providers must e-file. Oracle: Circular M; PFML contribution calculator (DFML). UI POA form not located. Confidence M-H.

## VA - Virginia (US-MQ-65) - missing 1,2,3,4,6 -> 1,4 answered; 2,3,6 partial
1. ANSWERED (US-VAP51-001). Guide 2614086 Rev. 10/26 read as full text (Wayback 2026-10-09): standard deduction 8,750, brackets to 5.75%, supplemental flat 5.75%, tables rounded to whole dollars. Replaces the MANUAL row US-VAPIT-005. Confidence H.
2. PARTIAL. Guide has no local-tax section; no explicit absence statement found.
3. PARTIAL. Wage base 8,000; new employer 2.5% plus add-ons; fund building charge 0.2% when trust fund <= 50%; 2026 pool cost percentage NOT located (US-VAP51-002/003). Employee share: none mentioned.
4. ANSWERED (US-VAP51-004). PFML enacted: SB2 Chapter 981, approved 2026-04-22, effective 2026-07-01; VEC; premiums and benefits begin 2028-04-01. Rate not located (chaptered text not read). No other levy found.
6. PARTIAL. Pay statement Va. Code 40.1-29(D) (US-VAP51-005); prevailing wage 2.2-4321.3, Commissioner of Labor and Industry (-006); POA Form PAR 101 (-007; read); VEC third-party agent route from search listing only (VEC 403). Oracle: none; formula p.21 of guide.

## TN - Tennessee (US-MQ-62) - missing 1,2,4,6 -> 1 answered; 2,4,6 partial
1. ANSWERED (US-TNP51-001). DOR GEN-34: no state income tax on earned income, no withholding requirement; Hall tax repealed 2021-01-01. Confidence H.
2. PARTIAL. GEN-34 silent on local wage taxes; none located.
4. PARTIAL. No SDI/PFML programme located (search only: no state-mandated private-sector PFL); no primary page states absence.
6. PARTIAL. DLWD Wage Regulations Act summary and Wages & Breaks page: pay frequency and deductions, no itemized pay-statement requirement (US-TNP51-003); full T.C.A. 50-2 text not read. Prevailing wage: Title 12-4-401, highways only, 2026 rates (-002). POA: DOR general form listing only (-004); no wage withholding. Oracle: none needed.

## IN - Indiana (US-MQ-35) - missing 2,3,4,6 -> 2 answered; 3,4,6 partial
2. ANSWERED (US-INP51-001). Only local wage tax = county tax withheld with state tax, by Jan-1 county of residence and principal work county (0.5%-3.0%); no city or school-district tax in DN#1.
3. PARTIAL. Wage base 9,500 (DWD Agent Handbook rev. 7/2023, US-INP51-002); new employer 2.5% (existing US-IN-003); employee contribution not mentioned. 2026 wage base not re-dated on a 2026 page (Employer-Guide.pdf Wayback copy unreadable, 0 pages).
4. PARTIAL. No SDI/PFML programme located; no primary absence statement.
6. PARTIAL. Pay statement, prevailing wage, state POA form: NOT LOCATED (in.gov DoR/DWD/IGA not read this wave beyond the Wayback files above). Oracle: DN#1 and WH-4 tables.

## PASS 4 (wave 2A) - status after this pass
NJ 1:answered 2:partial 3:answered 4:answered 5:answered 6:partial
MA 1:answered 2:partial 3:answered 4:answered 5:answered 6:answered
VA 1:answered 2:partial 3:partial 4:answered 5:answered 6:partial
TN 1:answered 2:partial 3:answered 4:partial 5:n/a 6:partial
IN 1:answered 2:answered 3:partial 4:partial 5:answered 6:partial
