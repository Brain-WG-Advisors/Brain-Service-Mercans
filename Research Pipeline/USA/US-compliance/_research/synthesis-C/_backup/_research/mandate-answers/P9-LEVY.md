# P9-LEVY: US-MQ-05 limb (c), absence proof in 22 states (2026-11-01)

Pass P9-LEVY by agent 2 (compliance-source-hunter). It answers the blocker row in 'Seal assessment (attempt 5)' of MANDATE.md for US-MQ-05 limb (c): employer levies on wages beyond SUI and withholding (transit, workforce/training, administrative add-ons).

Register rows are in `00-official-sources/_register-shards/mandate-P9-levy-r1.csv`: 44 rows, ids `US-<UF>P9V-NNN`. There are 36 active rows and 8 partial rows. By tier: A.2 36, A.3 7, A.1 1. None is tier B. None is MANUAL. The shard is not yet merged into `legal-basis-register.csv`, because the merge is not this pass's job.

Every source file is saved under `00-official-sources/pdfs/<UF>/`. Files fetched in this pass carry `_2026-11-01` in their name. Some local copies come from earlier passes, either Wayback `id_` copies of authority documents or files the user supplied. Each was re-read in this pass as text extracted from the file itself, not through a summariser. Their names are kept as they were.

Access on 2026-11-01:
- The VPN exit was Miami, US.
- The Wayback Machine was "Temporarily Offline" for the whole pass, so the archive fallback was unavailable.
- Claude in Chrome was not available to this agent.
- Several pages are blocked and are listed under Remaining gaps. Each blocked page is a finding, not a silence.

Method: for each state I read two kinds of source.
- **Revenue side.** The revenue department's tax-type list or menu, to establish that the only wage-based item is withholding.
- **UI side.** The workforce or UI agency's statement of what makes up the rate (admin fee, training surcharge, solvency or interest assessment).

"Absence proven" means both sides were read at tier A.

## 22-state table

| State | Levies found (beyond SUI base rate and withholding) | Absence proven | Register ids | Pages read |
|---|---|---|---|---|
| AK | Employee UI 0.5-1.0% (27% of ABCR); employer rate = 73% of ABCR x factor + trust fund solvency adjustment. STEP 0.10% / TVEP 0.25% are carved from the employee rate (P7). No other add-on. | partial (UI yes; DOR list is rendered by script and was not read) | US-AKP9V-001, -002 | AK DOLWD UI Tax Calculation Cookbook (AS 23.20.290); tax.alaska.gov Tax Types |
| AR | **NEW/CORRECTED:** Administrative Assessment 0.1% from Q3 2024 (A.C.A. 11-10-706), which replaced the stabilization tax on 2023-07-01. Conditional: Advance Interest 0.2% (11-10-708, only while a Title XII advance accrues interest); Extended Benefit tax 0.1% (11-10-540, when triggered). Deficit assessments 2%/4%. The 2026 page shows new employer 2.0%, range 0.2-5.1% (base + 0.1). | yes | US-ARP9V-001..003 (supersedes US-ARP7-001, which labelled a "0.2% stabilization rate") | DWS Employer Handbook; dws.arkansas.gov 2026 Tax Rates; DFA Taxes menu |
| AZ | None. The 2026 DES rate chart has UI rates only (new employer 2.00%, base 8,000). The Job Training Tax is absent from the chart, and ARS 23-769 returns 404. | yes (residual: the ADOR Pub 10 edition is 2022) | US-AZP9V-001, -002 | DES UIT-0603A (12/25); ADOR Pub 10 |
| CT | Fund solvency tax 1.0% (combined 1.1-9.9%); CT Paid Leave 0.5% employee (P7). | partial (UI yes; the DRS list is paginated by script and only page 1 was read) | US-CTP9V-001, -002 | CTDOL 2026 rate page; DRS Tax Types p.1 |
| GA | Administrative Assessment. **CONFLICT:** GDOL handbook R-11/24 glossary says 0.08%; GDOL release of 2023-12-27 (US-GAP7-001) says 0.06% through 2026-12-31. | partial (the DOR page is a hub, not a list; the GDOL tax page returns 404) | US-GAP9V-001, -002 | GDOL Employer Handbook DOL-224; dor.georgia.gov/taxes |
| HI | E&T assessment 0.01% (confirmed for 2026); TDI and Prepaid Health Care employee shares (P7). | yes | US-HIP9V-001, -002 (supersedes US-HIP7-001) | DLIR UI rate schedule; DOTAX Hawaii Tax Information |
| IA | None. The 2026 rate is the Table D rate only. 260E New Jobs Training is a withholding diversion, not an extra levy. | partial (UI yes; the IDR menu is not a tax-type list) | US-IAP9V-001, -002 | IWD 70-5015 Rate Computations 2026; revenue.iowa.gov/taxes |
| KS | None. The 2026 schedule (Schedule C, 0-6.95%, base 15,100) has no surcharge or ESIAF line. | yes | US-KSP9V-001, -002 | KDOL Employer Tax Rates; KDOR Business Tax |
| KY | Interest surcharge only while the trust fund owes Title XII debt (not assessed when solvent). SCUF 0.0% in 2026 (allocation, not extra cost), 0.0115% from 2027. Local occupational license taxes are employee taxes withheld by the employer (local layer, US-KY-P5-2-002); not re-read, see gaps. | yes for the state; local not re-read | US-KYP9V-001, -002 | OUI Employer Guide 2026; DOR Business list (complete) |
| LA | Social charges inside the total rate: Non-Charge, Incumbent Worker Training, Integrity. **Quantified:** the non-FUTA-creditable share (IWTP + Integrity) is 1 - FUTA factor, about 10.5-13.2% of the total rate. | yes | US-LAP9V-001..003 (supersede US-LAP7-001) | LWC UI tax rates page (R.S. 23:1553); LWC 2026 rate table; LDR Business |
| MA | Not re-read: every mass.gov page returned 403. Known from P7 statutes: Workforce Training Fund 0.056%, EMAC 0.34%, PFML 0.88%/0.46%. | **no** | none | mass.gov (403) |
| MD | None. Table A 0.30-7.50%; FAMLI starts 2027 (P7). | yes | US-MDP9V-001, -002 | DUI Tax Rates page and 2026 table; Comptroller Business |
| MI | None on the revenue side (Treasury list read directly; Detroit and city income taxes are employee withholding). | partial (the UIA rate-composition page returns 404) | US-MIP9V-001 (supersedes US-MIL-003) | michigan.gov/taxes/business-taxes |
| MO | Maximum-rate surcharge 0.25% rising to 1.5% (max-rate employers only); Contribution Rate Adjustment of +10/20/30% or -7/-12% (2026 value not stated); Automation Fund is a diversion. St. Louis payroll expense tax 0.5% (P7). | yes for the state (residual: 2026 CRA value); KC not re-read | US-MOP9V-001 (supersedes US-MOP7-004, upgraded tier C to A.3), -002 (supersedes US-MOL-002) | DES M-INF-151; DES employers page; DOR Business |
| MT | Administrative Fund Tax 0.18% (0.13% for classes 1-2). | yes | US-MTP9V-001 | DOR Business & Income Tax; DLI Rate Explanation |
| NC | Conditional 20% surtax when the trust fund is below 1 billion USD (G.S. 96-9.7(b)), not shown as imposed in 2026 (base rate 1.9% = healthiest tier). | yes | US-NCP9V-001, -002 (both supersede US-NCL-002) | DES Tax Rate Information; NCDOR Taxes & Forms |
| ND | None (the 2026 schedules hold UI rate tables only, base 46,600). | yes (the JSND narrative page returns 403; the schedule PDF was read) | US-NDP9V-001 (supersedes US-NDL-002) | tax.nd.gov/business; JSND 2026 schedules |
| NH | **NEW:** emergency surcharges 0.5% or 1.0% when solvency is in jeopardy; negative surcharge for schedule II/III employers; fund balance reductions. Administrative Contribution 0.4% inside the rate (P7). | partial (the 2026 list on tax-rate-info.htm returns 403; DRA returns 403) | US-NHP9V-001 | NHES 0041 handbook |
| OK | None. | yes | US-OKP9V-001, -002 | OTC Other Taxes; OESC Important Numbers 2026 |
| RI | Job Development Assessment 0.21%; TDI/TCI 1.1% employee, base 100,000, max 1,100. | yes | US-RIP9V-001 (supersedes US-RIP7-002, MANUAL to active), -002 | DLT 2026 rates release; Division of Taxation sections |
| UT | Social cost inside the rate; 1% surcharge for unpaid prior contributions; delinquent payment surcharge 1.0%. | partial (UI yes; the USTC "List of All Tax Types" returns 404) | US-UTP9V-001 (supersedes US-UTP7-002, MANUAL to active), -002 | DWS Tax Rates; USTC Business |
| VA | Pool cost charge (all employers, % not read); fund building charge 0.2% when the fund is at 50% or less; administrative fee 0.05% (P7). | partial (2026 percentages not read; Virginia Tax business list returns 404) | US-VAP9V-001 (supersedes US-VAP7-001) | VEC UI tax FAQ |

Count: 13 closed (AR, AZ, HI, KS, KY, LA, MD, MO, MT, NC, ND, OK, RI); 8 partial (AK, CT, GA, IA, MI, NH, UT, VA); 1 not closed (MA). Across all 22, no transit payroll tax was found. Transit stays at OR and NY only (P7).

## Tier-B absence rows replaced

| Old row (tier B) | New row | Basis |
|---|---|---|
| US-MEL-003 | US-MEP9V-001 | MRS A-Z list read directly 2026-11-01 |
| US-MIL-003 | US-MIP9V-001 | Treasury Business Taxes read directly (UIA side still open) |
| US-MOL-002 | US-MOP9V-002 (+ US-MOP9V-001 for the DES side) | DOR Business + DES M-INF-151 |
| US-NCL-002 | US-NCP9V-001, US-NCP9V-002 | DES Tax Rate Information + NCDOR list |
| US-NDL-002 | US-NDP9V-001 | tax.nd.gov/business read directly |
| US-NEL-002 | US-NEP9V-001 | revenue.nebraska.gov/businesses read directly |

When this shard is merged, the old rows should get `status=superseded` and `effective_to=2026-11-01`. Their `consumed_by` is `US-MQ-05` only.

## MANUAL upgrades (P7)

| P7 row | Result | New row |
|---|---|---|
| US-DEP7-004 / -005 (DE industry and size assessments) | **Upgraded, A.1.** 19 Del. C. 3350E levels 0.20/0.30/0.50/0.60/0.75%; 3350F size 0.00/0.25/0.35%. Both are components of the earned rate only under 3350A "(2027 and after)", so **not payable in 2026**; first set by 2026-12-31. Also confirms 3350B OTA 0.2% through 2026, 0.175% from 2027. | US-DEP9V-001 |
| US-NYP7-005 (NY subsidiary rate) | **Upgraded, A.2, derived arithmetically.** Contribution rate = normal + subsidiary; 2026 new employer 4.025% - 3.4% = **0.625%**; RSF 0.075% separate (NYS-45 line 5). | US-NYP9V-001 |
| US-WAP7-006 (Seattle Social Housing Tax) | **Upgraded, A.2.** 5% of compensation above 1,000,000 USD paid in Seattle per employee; in force 2025-01-01; quarterly from 2026. | US-WAP9V-001 |
| US-WYP7-002 (WY fund-balance factors) | **Not upgraded.** Not re-fetched in this pass (budget). Stays MANUAL. | none |

Other P7 rows upgraded along the way: US-RIP7-002 (RI TDI), US-UTP7-002 (UT delinquency surcharge), US-LAP7-001 (LA social charges, now quantified), US-MOP7-004 (MO max-rate surcharge, tier C to A.3), US-ARP7-001 (AR, label corrected), US-VAP7-001 (VA pool cost: mechanism read, 2026 value still open).

## Local and city employer levies in the 22 states

- **MO.** St. Louis payroll expense tax 0.5% (employer) is already active (US-MOP7-002). The KC earnings tax is employee-borne; kcmo.gov returned 403, so US-MOP7-003 stays MANUAL.
- **KY.** Occupational license taxes on wages are employee taxes withheld by the employer. louisvilleky.gov returned 403, so US-KYP7-002 stays MANUAL. This could not be read here: Louisville's 2.2% may include a TARC (transit) component, which would be a transit-earmarked local wage tax. Not verified; do not model.
- **MI.** City income taxes are employee withholding (US-MIP7-001/002 MANUAL); no employer city payroll tax was found on the Treasury list.
- No other employer-paid local payroll tax was found in the 22 states.

## Remaining gaps (exact URLs; all tried 2026-11-01)

| Key | Why | Attempted | What would close it |
|---|---|---|---|
| MA all | mass.gov 403 (bot block); Wayback offline | https://www.mass.gov/info-details/learn-about-your-unemployment-insurance-tax-rate (403) | The DUA 2026 contribution-rate page and the DOR tax-type list, opened in a normal browser and saved to pdfs/MA/, or Wayback when it is back online |
| CT revenue list | Script pagination | https://portal.ct.gov/drs/taxes (page 1 of 6 only) | All 6 pages of the DRS Tax Types list (browser) |
| GA admin assessment 2026 rate | 0.08% (handbook R-11/24) vs 0.06% (GDOL 2023-12-27, through 2026) | https://dol.georgia.gov/employers/unemployment-insurance-tax (404); https://dor.georgia.gov/taxes (hub) | A GDOL 2026 tax-rate notice or O.C.G.A. 34-8-185 text; the DOR tax-type list |
| NH 2026 surcharges | 403 | https://www.nhes.nh.gov/services/employers/tax-rate-info.htm ; https://www.revenue.nh.gov/taxes | NHES tax-rate-info page (the current surcharge and reduction list) |
| MI UIA composition | 404 | https://www.michigan.gov/leo/bureaus-agencies/uia/employers/tax-rates ; .../employer-tax-info | The UIA employer tax-rate page or Form UIA 1771 (rate notice) explanation |
| VA 2026 pool cost / fund building | VEC 2026 values not on FAQ; Virginia Tax list 404 | https://www.tax.virginia.gov/business-taxes (404) | VEC 2026 rate notice components page; Virginia Tax business tax list |
| UT revenue list | 404 | https://tax.utah.gov/business/tax-types | The USTC "List of All Tax Types" (correct URL from the menu, in a browser) |
| IA revenue list | Menu only | https://revenue.iowa.gov/taxes | IDR tax-type index |
| AK revenue list | Rendered by script | https://tax.alaska.gov/programs/programs/index.aspx | Tax Division Tax Types page in a browser |
| KY local (TARC component) | 403 | https://louisvilleky.gov/government/revenue-commission/occupational-license-tax | Louisville Metro Revenue Commission rate page |
| MO KC earnings tax | 403 | https://www.kcmo.gov/city-hall/departments/finance/tax-home/earnings-tax | KC Revenue Division earnings tax page |
| WY fund-balance factors | Not attempted (budget) | none | WY DWS 2026 rate notice explanation; W.S. 27-3-503 |
| AZ JTT repeal (statute) | azleg 404 | https://www.azleg.gov/ars/23/00769.htm | Session law repealing ARS 23-769 (absence on the 2026 DES chart already read) |

Shape of the remaining work: 10 independent, parallel browser reads (MA, CT, GA, NH, MI, VA, UT, IA, AK, KY/MO local). All of them are ACCESS gaps, not research gaps; one agent per state, or one owner session of about 30 minutes in a normal browser.

## Proposed scope statement for US-MQ-05 (c)

Transit payroll taxes: OR and NY only (P7), with none found in the 22 states re-read here.

Workforce and administrative add-ons are the P7 list, with these changes:
- AR corrected to Administrative Assessment 0.1%, plus conditional interest and EB taxes.
- MO max-rate surcharge and CRA added at A.3.
- NH emergency surcharges added.
- LA social charges quantified.
- DE industry and size assessments moved to 2027.

Absence is proven at tier A in 13 of the 22 states; 8 are partial and 1 (MA) is open on ACCESS. Sealing still needs either the owner decision `US-OWN-006` accepting this statement, or the 10 browser reads above.

## Open questions (mirror of unresolved[])

- `levy.ga.admin_assessment.rate`: 0.08% vs 0.06% for 2026. Closes with the GDOL 2026 rate notice or the statute text.
- `levy.mo.cra.rate`: the 2026 CRA percentage. Closes with the DES 2026 rate notice explanation.
- `levy.va.pool_cost.rate`: the 2026 percentage. Closes with the VEC 2026 rate components page.
- `levy.nh.emergency_surcharge.status`: whether it is in effect in 2026. Closes with NHES tax-rate-info.htm.
- `levy.ky.louisville.tarc_component`: whether one exists. Closes with the Louisville Metro Revenue Commission page.
- MA entire state: ACCESS.

## Round 2 (browser reads, 2026-11-01)

Pass P9-LEVY round 2, run by a sub-agent of the EUA window in Claude in Chrome (own tab, closed at the end) with a US VPN exit. Pages were read with get_page_text. Where a page held no text, the needed lines were transcribed from screenshots (GA DOR). Statute PDFs were fetched with curl and a browser user agent, then text-extracted. No CAPTCHA or bot check came up. Each page text is saved under `00-official-sources/pdfs/<UF>/`, with the URL and read date at the top.

The register rows are in `00-official-sources/_register-shards/mandate-P9-levy-r2.csv`: 26 rows, ids `US-<UF>P9W-NNN`. By tier: A.1 2, A.2 24. By status: active 23, partial 3. None is tier B. This shard is not merged into `legal-basis-register.csv` either.

Several round-1 URLs had moved: NHES tax-rate-info.htm, revenue.nh.gov/taxes, the Louisville occupational-license-tax page, the KCMO earnings-tax page and the UIA tax-rates page. In each case the current page was found through the site's own menu or search.

| Gap | Result | Register ids | Still open (exact URL) |
|---|---|---|---|
| CT revenue list | **Closed.** The DRS "Information for Businesses" A-Z list has 29 taxes, and the only wage-based one is Withholding Tax. All 6 pages of `/drs/taxes` were also read; none has a wage levy. | US-CTP9W-001 (supersedes US-CTP9V-002), -002 | none |
| GA admin assessment | **Closed: 0.06% for 2026.** The source is SB 160 (2023), Act 86, which enacted O.C.G.A. 34-8-180 to -185. The rate is 0.06% from 2024-01-01 to 2026-12-31. It excludes reimbursing employers and employers at the minimum positive reserve rate or the maximum deficit reserve rate. New employers pay 2.64% + 0.06%, which matches the GDOL FAQ "total tax rate of 2.70 percent". The article is repealed on 2027-01-01 (34-8-185). The handbook figure of 0.08% is superseded. Note that HB 518, named in the GDOL release, stalled in the Senate; SB 160 is the act that passed. The DOR list shows Withholding as the only wage-based item. | US-GAP9W-001 (A.1; supersedes US-GAP9V-001 and US-GAP7-001), -002, -003 (supersedes US-GAP9V-002) | Watch for 2027: the assessment lapses unless it is re-enacted |
| NH surcharges 2026 | **Closed.** For all four quarters of 2026: fund balance reduction 1.00% (Schedule I), Emergency Power Surcharge **0.00%** (last charged in 2020-Q3/Q4), inverse rate surcharge 0.50% for negative-rated employers (Schedules II/III). The Administrative Contribution (0.1-0.4%) is carved out of the net rate. The DRA list has no wage tax. The **Business Enterprise Tax** is 0.55% of a base that includes compensation, but it is an entity-level annual business tax and is not run through payroll. Proposed: out of scope, owner to confirm. | US-NHP9W-001 (supersedes US-NHP9V-001), -002, -003 | none (BET scope: owner decision) |
| MI UIA composition | **Closed.** The 2026 rate is CBC + ABC + NBC, plus a non-reporting penalty. 2026 summary: new employer 2.7%, construction 5.0%, range 0.06-12.2%, 15.2% with penalty. No obligation assessment, solvency or training surcharge is shown. | US-MIP9W-001, -002 | none |
| VA 2026 pool cost / fund building | **Partial.** The revenue side is closed: Virginia Tax lists Employer Withholding as the only wage-based item. On the UI side, the VEC FAQ (exact URL) describes the mechanism: Pool Cost Charge for all employers, and a 0.2% Fund Building Charge when the fund is at 50% or less. The 2026 percentages are on no VEC page. A site search for 2026 returned nothing. | US-VAP9W-001 (supersedes US-VAP9V-001, partial), -002 | The 2026 pool cost % and fund-building status. Nothing at https://www.vec.virginia.gov/ (search "2026 tax rates"). Next sources to try: the employer's 2026 rate notice, or Va. Code 60.2-528/533 with the 2026 fund balance factor |
| UT revenue list | **Closed.** The USTC "List of All Tax Types" (https://tax.utah.gov/business/utah-taxes/) has 44 items, and the only wage-based one is Employer Withholding Tax. | US-UTP9W-001 (supersedes US-UTP9V-002) | none |
| IA revenue list | **Closed.** The IDR Tax Guidance index lists categories, and the only wage-based one is Withholding Tax. Its submenu covers OBBBA, Jobs Credits (260E/F diversion) and sports wagering. | US-IAP9W-001 (supersedes US-IAP9V-002) | none |
| AK revenue list | **Closed.** https://tax.alaska.gov/programs/index.aspx (without the doubled `/programs/`) lists 25 tax types. The Withholding entry says there is no individual income tax and so no withholding. Employment Security Tax is the DOLWD UI. | US-AKP9W-001 (supersedes US-AKP9V-002) | none |
| KY Louisville TARC | **Closed: a TARC component exists, and employees pay it.** Louisville OLT on wages, per the W-1 instructions: Metro 1.25% + Transit Authority **0.20%**, 1.45% on all wages earned in Louisville Metro. School Boards adds 0.75% for residents only, so residents pay 2.2%. All of it is withheld from employee compensation; no employer-paid part is stated. This is a transit-earmarked **local employee** wage tax, so it does not change the employer-levy list. | US-KYP9W-001 (supersedes US-KYP7-002), -002 | none |
| MO KC earnings tax + CRA 2026 | **Closed.** KC earnings tax: 1%, employee-borne. Employers in KC withhold it (nonresident businesses may opt in). There is no employer-paid part on wages; the business-side 1% applies to net profits. CRA 2026: **12% reduction**, derived from the DES table (new employer rate 2.376% "include[s] applicable contribution rate adjustments", and 2.376 / 2.7 = 0.88). DES also says no Federal Interest Assessment is expected for 2026, and the Automation Fund is a redirect of at most 0.020% with no extra tax. | US-MOP9W-001 (supersedes US-MOP7-003), -002 (supersedes US-MOP9V-001, A.3 to A.2) | none |
| WY rate factors | **Partial (structure closed, 2026 values open).** W.S. 27-3-505 sets three adjustment factors on top of the base rate. (a) A noncharged-benefits factor: 20% to the UI fund, **60% to the Employment Support Fund, 20% to the Workforce Development Training Fund**. This is a workforce-training levy built into the UI rate. (b) A positive fund-balance factor when the fund is below 3.5% of payrolls. (c) A negative factor when the fund is above 4%. (a) + (b) is capped at 1.5%. Delinquent employers pay +2%. The DWS page says "four additional rate factors" but neither names them nor gives 2026 values. | US-WYP9W-001 (A.1; supersedes US-WYP7-002), -002 | 2026 factor values: https://dws.wyo.gov/dws-division/unemployment-insurance/employers/unemployment-tax-rates/ has none. A 2026 rate notice or a DWS rate-factor table is needed |
| MA (main session) | **Closed** with the main-session reads (`pdfs/MA/MA_DUA_pages_2026-11-01.txt` and screenshots). DOR lists only Withholding and PFML as wage items. DUA 2026: new employer 2.42%, construction 6.08%. **New levy:** COVID-19 Recovery Assessment for experience-rated employers, 0.178-2.716% in 2026 (schedule E). EMAC and the Workforce Training Fund (c.151A s.14L) are confirmed in force; their rates are carried from P7. | US-MAP9W-001..005 | 2026 WTF/EMAC rates as published by DUA (P7 statute values carried) |

### Updated 22-state count

- **Closed (21):** AK, AR, AZ, CT, GA, HI, IA, KS, KY, LA, MA, MD, MI, MO, MT, NC, ND, NH, OK, RI, UT.
- **Partial (1):** VA. Absence is proven on both sides; only the 2026 Pool Cost Charge % and fund-building status are open.
- **Open (0).**

Outside the 22: WY is now partial (structure at A.1, 2026 values open). The residual for MO (2026 CRA) and for KY local (TARC) is closed.

### Changes to the proposed scope statement for US-MQ-05 (c)

- **Add MA COVID-19 Recovery Assessment.** Experience-rated employers only; 2026 rates 0.178-2.716%.
- **GA Administrative Assessment is 0.06%.** In force until 2026-12-31 and repealed on 2027-01-01.
- **NH Emergency Power Surcharge is 0.00% in 2026.** It stays as a conditional mechanism only.
- **MO CRA 2026 is a 12% reduction.**
- **WY noncharged-benefits factor** carries an Employment Support Fund / Workforce Development Training Fund share. It is part of the UI rate, not a separate line.
- **Transit:** still OR and NY only on the employer side. The Louisville TARC 0.20% is a local transit wage tax paid by the employee and withheld by the employer, so it belongs with the local withholding layer, not with employer levies.

### Open questions after round 2

- `levy.va.pool_cost.rate`: still open, see the table above.
- `levy.wy.adjustment_factors.2026`: new; needs the 2026 values.
- `levy.nh.bet.scope`: owner decision on whether the Business Enterprise Tax stays out of payroll scope (recommendation: out).
- Closed: `levy.ga.admin_assessment.rate` (0.06%), `levy.mo.cra.rate` (-12%), `levy.nh.emergency_surcharge.status` (0.00% in 2026), `levy.ky.louisville.tarc_component` (yes, 0.20%, employee-borne), MA ACCESS.
