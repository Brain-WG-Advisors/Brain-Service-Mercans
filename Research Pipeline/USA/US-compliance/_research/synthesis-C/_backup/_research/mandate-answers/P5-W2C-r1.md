# Mandate answers P5-W2C-r1 - MO CO KY MD AL (PASS 4, wave 2C, 2026-10-29)

Hunter: compliance-source-hunter. Parts worked = blocking list in build-manifest.json minus earlier PASS sections. Register: `00-official-sources/_register-shards/mandate-P5-W2C-r1.csv` (18 rows). Chrome: own tab, get_page_text only, no javascript_tool, tab closed. WebFetch PDFs saved to `00-official-sources/pdfs/<UF>/` and read locally with PyMuPDF (`python -I`).
Gated this wave: denvergov.org (WAF "Support ID"), kcmo.gov (Access Denied), stlouis-mo.gov and revisor.mo.gov and apps.legislature.ky.gov (tab bounced to another domain), cdle.colorado.gov Paydays page (Access denied), labor.mo.gov (403; Chrome no text), dor.mo.gov forms (403), famli.maryland.gov (error page). Wayback: HTTP 429 twice on labor.mo.gov MODES-4595 (snapshot 20250607085028 exists; retried once after 60 s, still gated). Search-summary figures were NOT used as figures.

## MO - Missouri (US-MQ-44) - missing 2,3,4,6
2. PARTIAL. Guide 4282 (US-MO-P5-1-001) has no local-tax section. Kansas City / St. Louis earnings-tax pages gated (kcmo.gov Access Denied; stlouis-mo.gov bounced). Not located from a primary page.
3. PARTIAL (gated). DES tax-rates page and MODES-4595 unreadable (labor.mo.gov 403 / no text; Wayback 429). A search summary reported wage base 9,000 and new employer rate 2.376% for 2026: NOT accepted as a figure. Next step: Wayback MODES-4595 when 429 clears.
4. PARTIAL. No SDI/PFML programme in 4282; no primary absence statement.
6. PARTIAL. Answered: POA = Form 2827 (US-MO-P5-1-001, read in the guide text); oracle = DOR online Withholding Calculator (mytax.mo.gov/rptp/portal/home/withholding-calculator). Not located: pay-statement statute and prevailing-wage statute (RSMo ch. 290; revisor.mo.gov gated); UI third-party-agent form.
Also confirmed from the guide (part 5 closed): no reciprocity agreement with any state; rounding to nearest whole dollar. Confidence H for these.

## CO - Colorado (US-MQ-25) - missing 1,2,3,5,6
1. ANSWERED (US-CO-P5-1-001/-002). 2026: 4.40% flat; annualised wages minus 5,500 (11,000 MFJ/QSS) or DR 0004 line 2; certificate W-4 or DR 0004. Worksheet has no separate supplemental rate and no rounding step. Effective 2026-01-01. Confidence H.
2. PARTIAL. Guide (Revised January 2026) has no local-tax section. Denver OPT page gated (WAF); not located from a primary page.
3. ANSWERED (US-CO-P5-1-003/-004). Chargeable wage limit 2026 = 30,600. New employer 2026: non-construction 3.05% combined (1.53% + 0.17% support + 1.35% solvency surcharge); heavy construction 6.285%. Employer-paid; no employee share on the pages. Confidence H.
4. ANSWERED (existing US-CO-FAMLI-001, quote-level, chrome-read earlier): FAMLI 0.88% (0.44/0.44) to SS cap. CDLE famli.colorado.gov/employers returned 403 to WebFetch this wave, not re-read. Confidence M-H.
5. ANSWERED (US-CO-P5-1-002). Resident: no CO withholding on wages for services in another state that requires withholding; nonresident: CO wages apportioned by days (day counts if majority of working time in CO). No reciprocity list in the guide. Confidence H.
6. PARTIAL. Pay statement: C.R.S. 8-4-103(4),(4.5) (US-CO-P5-1-005, read from Wayback 20250726 copy). POA: DR 0145 (listing only, US-CO-P5-1-006). Oracle: DR 1098 Withholding Calculator. NOT located: state prevailing-wage statute/agency; UI third-party-agent authorization form.

## KY - Kentucky (US-MQ-37) - missing 1,2,3,4,6
1. PARTIAL. 3.5% flat, 2026 standard deduction 3,360 (US-KY-001/002); bonuses subject to withholding, no separate flat supplemental rate stated (US-KY-P5-1-001). Rounding rule NOT stated (examples show cents and whole dollars). Confidence M-H.
2. PARTIAL. Guide has no local-tax section; local occupational license taxes (counties, cities, school districts) not read from a primary statute or page (apps.legislature.ky.gov gated).
3. ANSWERED (US-KY-P5-1-002). Employer Guide approved 2026-07-31: 2026 wage base 12,000; new employer 2.70%; SCUF suspended 2026. No employee contribution described. Confidence H.
4. PARTIAL. No SDI/PFML programme found; no primary absence statement. SCUF is an employer UI add-on only (0.0115% from 2027).
6. PARTIAL. Representative POA = Form 20A100 (US-KY-P5-1-001); KUIP portal serves employers and TPAs (US-KY-P5-1-002). Not located: pay-statement statute (KRS 337.070 not read), prevailing wage (KRS 337.505 ff. not read), UI TPA form, calculator (none; formula sheet 42A003 TCF).

## MD - Maryland (US-MQ-40) - missing 1,3,4,6
1. ANSWERED (US-MD-P5-1-001). Guide effective Jan 2026 (rev. Dec 2025): MW507; percentage tables by county of residence; lump-sum annual bonus at 6.50% state plus highest local rate; nonresident 2.25% special rate; online withholding calculator. No rounding rule in the guide. Confidence H.
3. ANSWERED (US-MD-P5-1-002). 2026 Table A, rates 0.30%-7.50%, wage base 8,500, new employers 1.0%-2.6% (range, exact new-employer rate not stated on the page). No employee share stated. Confidence H for base, M for the new-employer point value.
4. ANSWERED (US-MD-P5-1-003/-004). FAMLI: contributions 0.9% (0.45/0.45) from 2027-01-01 to the SS cap, first payment 2027-04-30; benefits from 2028-01-01. Nothing payable in 2026. No SDI. Confidence H.
5. Previously closed (not re-worked).
6. ANSWERED. Pay statement LE 3-504 (US-MD-P5-1-005); prevailing wage SFP 17-201 ff., Commissioner of Labor and Industry (US-MD-P5-1-006); POA Form 548P (US-MD-P5-1-001); oracle: Comptroller online withholding calculator. UI TPA form not located (BEACON "New Third-Party Agents: Get Started" link on the DOL page, not opened).

## AL - Alabama (US-MQ-21) - missing 2,3,4,5,6
2. ANSWERED (US-AL-P5-1-001). Occupational taxes are administered by each city or county, not ADOR (booklet p.2); locality list not published by the state. Confidence H.
3. ANSWERED (US-AL-P5-1-002). Wage base 8,000; new employer 2.70% (FAQ page dated 2023-11-16, still the published new-account rate); experience rates 0.59%-6.19% (17 steps, ADOR UC page); Alabama Department of Workforce administers (booklet still names Dept of Labor). 2026 shared-cost schedule not on the page. Confidence M-H.
4. PARTIAL. No SDI/PFML programme found; no primary absence statement.
5. ANSWERED (US-AL-P5-1-001). Act 2025-334 30-day safe harbor; resident employer / nonresident employee rules; carrier exemptions. No reciprocity agreement list in the booklet. Confidence H.
6. PARTIAL. POA Form 2848A (listing, US-AL-P5-1-003); rounding and 5% supplemental rate from booklet; oracle: tables and formula (no calculator located). NOT located: pay-statement statute, prevailing-wage statute, UI POA form.

## PASS 4 (wave 2C) - status after this pass
MO 1:answered 2:partial 3:partial 4:partial 5:answered 6:partial
CO 1:answered 2:partial 3:answered 4:answered 5:answered 6:partial
KY 1:partial 2:partial 3:answered 4:partial 5:answered 6:partial
MD 1:answered 2:answered 3:answered 4:answered 5:answered 6:answered
AL 1:answered 2:answered 3:answered 4:partial 5:answered 6:partial
