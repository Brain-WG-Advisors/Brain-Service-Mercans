# SIR research pack: United States (unit `third_party_provider_handoff`)

> **Synthesis C (2026-11-02).** Register ids were normalized to the facts-schema pattern (map: `_research/stage5/ID-RENAME-MAP.csv`, ids in this pack already rewritten). Every fact that was held for the register_id pattern defect (marked here as "legacy id, NOT a fact", "PENDING", "(P)", "parked" or "carried in unresolved") is now a validated fact in `facts[]`; promotion log `_research/synthesis-C/_work/step2-promotion-log.csv`. Counts of held facts quoted below are historical. The Open questions block below mirrors the current `unresolved[]`.

Synthesis B, 2026-11-02. Sources:
- `_research/stage5/{JUR}.md` section 5 (reporting_instruments), all 53 files;
- MANDATE US-MQ-09;
- `Research Pipeline/USA/00-filing-terceiros/PROCESSO-FILING-TERCEIROS.md`;
- the register.

No fetching this pass. Facts file: `_research/SIR-facts.json` (validated PASS). It holds 222 facts in the validated array and 69 parked under `_facts_blocked_by_register_id_pattern`: active rows whose multi-segment ids the 1.4.0 schema pattern rejects.

## 1. Scope (owner decisions; not legal findings)

- Statutory filings, federal and state, go through a **third-party filing provider**, with no ADP integration (owner, 2026-10-21).
- The provider choice is a business decision **outside this build** (US-MQ-09 owner limb, 2026-10-29).
- The SIR is the provider-agnostic hand-off. Mercans produces provider input and never submits to an authority. The employer keeps legal liability for every return and deposit [US-FED-008].
- Channel classification below describes what the **provider** submits to each authority: `online_form` / `file_upload` / `xml` / `api` / `paper`. The tax portal and the UI portal are separate institutions in every wage-tax state (C24).

## 2. Federal layer

**Agent authorisation**
- Form 8655 (Rev. 1-2024), one per EIN [US-FED-028, US-FED-009].
  - Line 15 lists the returns: 940, 941, 943, 944, 945, 1042, CT-1.
  - Line 16 covers deposits.
  - **Line 19 extends the authorisation to state and local returns related to lines 15/16.**
  - The agreement stays in force until revoked and does not revoke Form 2848/8821.
- Rev. Proc. 2012-32 sec. 5.05 [US-FED-008]:
  - the authorisation does **not** relieve the employer of responsibility or liability;
  - the agent gives a written statement at engagement and at least quarterly.
  - Level: employer reporting and deposit.
- Pub. 1474 (Rev. 4-2026) technical spec [US-FIL-001]:
  - a "service bureau" qualifies as reporting agent;
  - agent-list changes go electronically above 100 a week, via SLFT B2B only;
  - deposits go via EFTPS or FTA.
- Third-party payer arrangements (reporting agent vs sec. 3504 agent vs CPEO) follow Pub. 15 (2026) [US-FEDP51-002]. They are distinct appointments, and the provider contract must say which one applies.

**Deposits and returns**
- 2026 lookback: 2024-07-01 to 2025-06-30.
  - Liability of 50,000 or less = monthly depositor (15th).
  - More = semiweekly: Wed–Fri paydays deposit the next Wednesday; Sat–Tue paydays the next Friday.
  - 100,000 or more accumulated on any day = next business day.
  - Holidays follow DC legal holidays [US-FEDS5-004].
- 941 is quarterly, in cents; 944 only on IRS written notice.
- 940 is annual, due Jan 31 (Feb 10 if fully deposited). FUTA is deposited above 500 [US-FEDS5-031, partial; the 2026 i940 is unpublished].
- W-2/W-3 TY2026 are due to SSA and employees **2027-02-01** [US-FEDS5-007]. Format: EFW2 Pub. 42-007 via SSA BSO [US-FIL-002]. **The TY2026 EFW2 layout is not read** (ACCESS gap, US-FIL-003 / US-FEDS5-032 gated). This is the one blocking unresolved item for the W-2 hand-off spec.
- ACA 1094-C/1095-C for ALE members: e-file at 10+ returns; affordability 9.96% for 2026 [US-FEDS5-012, partial].
- New hire: 20 days, with the 42 U.S.C. 653a fields [US-FEDS5-024].
  - Electronic filers may send two monthly transmissions 12–16 days apart.
  - A multistate employer may designate one state after notifying HHS [US-MULTIS5-006].
- W-2 boxes 15–20 hold two states and two localities per form [US-MULTIS5-011].

## 3. State mechanics common to all wage-tax states

1. **Two authorisations per state.** The 8655 line-19 tick does not replace them. One is for the revenue department (withholding POA). The other is for the workforce agency (UI agent/TPA), increasingly an online link rather than a paper POA:
   - PA UCMS handshake [US-PAP51-004];
   - TN "no POA needed since 2025-05-27" [US-TNR3-002];
   - MN Agent ID [US-MNP6-003];
   - CO MyUI Employer+ [US-COP52-003];
   - NV ESS external user [US-NVR3-003];
   - LA LAWATS online POA [US-LAP52-005];
   - VA ESS invitation with ID.me from 2026-08-01 [US-VAP6-001];
   - IL E-POA bulk file under a service-bureau MOU [US-ILP52-010].
2. **State W-2 copy.** Most states take **EFW2 with a state RS record**, often with a state RV total record. Exceptions:
   - **IA** uses a unique format and rejects the SSA file [US-IAS5-017].
   - **IN** requires XML for new filers [US-INS5-011].
   - **NC** uses its own fixed-field TY2026 spec v9-2026 [US-NCS5-028].
   - **NY** files **no W-2**: NYS-45 Part C carries the data [US-NYS5-010].
   - **CA** files **no W-2**: the DE 9C carries the data [US-CAS5-018].
   - **NJ** is due **Feb 15** [US-NJP51-001].
   - **MI** reconciles on 5081 by **2027-02-28** [US-MIS5-018].
   - **IA** is due **Feb 15** [US-IAS5-017].
3. **SSN not truncated** on state copies (AZ, DE, MT, SC); see the PSL pack section 4.
4. **Bulk-filer and provider programmes** need registration and tests:
   - NY Pub. 72.5: agent ID, prior approval and test file [US-FIL-007];
   - OH bulk filer with ETIN + OHID [US-FIL-012];
   - IA bulk-filer registration, up to 4 weeks [US-IAS5-017];
   - WI provider software registration and test [US-WIS5-016];
   - RI Payroll Letter of Intent [US-RIS5-018];
   - WV Letter of Intent [US-WVS5-010].
5. **Provider-specific duties:**
   - ME payroll processors need a Bureau of Consumer Credit Protection licence [US-MES5-011].
   - VT and WV e-filing is mandatory whenever a payroll service files [US-VTS5-017, US-WVS5-013].
   - ND: e-file if a third-party provider e-files federally [US-NDS5-002].
   - AK: online UI mandatory when a payroll agent files [US-AKS5-005].
   - GA: payroll providers serving more than 250 employers pay by EFT [US-GAP52-003].
   - WY: a PEO files a separate report per client and the client is jointly liable [US-WYS5-019].

## 4. Per-jurisdiction hand-off matrix

Columns: withholding return(s); state W-2 copy (format, e-file threshold); UI wage report (channel, e-file threshold); agent authorisations (withholding / UI); new-hire days. All ids are in SIR-facts.json under `sir.{jur}.*`.

| Jur | Withholding | State W-2 | UI wage report | Authorisation W/H · UI | New hire |
|---|---|---|---|---|---|
| AK | none | none | TQ01C, CSV upload; online at 50+ or agent | - · UI POA 7/24 [US-AKP51-006] | 20 |
| AL | A-6/A-1/A-3 | EFW2 RS only; 10+ | eGov upload/form | ? · UC POA 02/2025 | **7** |
| AR | AR941M/A, AR3MAR (Feb 28) | EFW2 (RV not allowed); 125+ employees | Tax21; 250+ | DFA POA 9/2025 · not located | 20 |
| AZ | A1-QRT, A1-R | EFW2 RS (04), all electronic | DES UC-018 (403) | 821-PSC · UIT-1146A | 20 |
| CA | DE 9/DE 9C (PIT+SDI+UI), DE 88 | **not filed** | DE 9C (XML/ICESA/MMREF/CSV/FSET) | DE 48 (one form) | 20 |
| CO | DR 1094 freq by amount | .txt or XLSX; 10+ | MyUI (403) | DR 0145 · MyUI TPA | 20 (fed) |
| CT | CT-941, CT-W3 | EFW2 or CSV | ReEmployCT 276-char | LGL-001/003 · COR | 20 |
| DC | FR-900Q/A | EFW2 RS; 25+ | UC-30 ESSP; 250+ machine | D-2848 · OUCTAX-1 | 20 |
| DE | quarterly/monthly/8th-monthly; WTH-REC | EFW2 RS; >10 | UC-8/8A | IRS 2848 · DUI POA | 20 |
| FL | none | none | RT-6 flat file v7 or XML (XSD validated); 10+ | DR-835 (RT agent) | 20 (+ contractors) |
| GA | G-7; G-1003 | EFW2+GA RS or template | DOL-4N; 25+ | RD-1061/1063 · GDOL POA | **10** |
| HI | HW-14; VP-1 | EFW2 on HTO; 10+ from 2026 | UC-B6 | N-848 · online profile | 20 |
| IA | quarterly; no reconciliation | **IA-unique** 512; Feb 15 | 65-5300 + detail | IA 2848 · 68-0092 | **15** |
| ID | 910; 967 | EFW2 + ID records | TX20 portal | ID-POA · Portal Auth. | 20 |
| IL | IL-941; no reconciliation | MyTax/ETIN EFW2 | UI-3/40 + monthly 25+ | IL-2848 [US-IL-004] · E-POA MOU | 20 |
| IN | WH-1; WH-3 | **XML** (new filers); 25+ | ESS upload >50 | POA-1/ePOA · ESS agent | 20 |
| KS | KW-5; KW-3 | EFW2 KS RS or CSV; 51+ | MMREF/NASWA; 25+ | DO-10 · K-CNS-032 | 20 (business days) |
| KY | K-1/K-3 | EFW2 DOR RS; 26+ | KUIP | not located | 20 (to AG) |
| LA | L-1; L-3 | LaWage; 50+ | LAWATS | R-7006 superseded · LAWATS POA | 20 |
| MA | M-941 | EFW2; 50+ | DUA CSV/EFW2/ICESA | M-2848 + MTC access | **14** |
| MD | MW506; MW508 | MD-modified EFW2; 25+ | BEACON (CSV/XML/ICESA/EFW2) | 548P [US-MDP51-001] · DOL UI POA (no active row read) | 20 |
| ME | 941ME | portal bulk spec (not read) | UC-1 to MRS | 2848-ME (superseded row) · UC-28 MANUAL | **7** |
| MI | 5080; 5081 (Feb 28) | MTO EFW2; 10+ | MiUI CSV/ICESA/EFW2/XML | Form 151 · UIA 1488 | 20 (fed) |
| MN | quarterly e-Services | DOR method; >10 | 268.044 incl. hours | REV184b · Agent ID | 20 |
| MO | MO-941 | EFW2 + RV; 250+ | MODES-4 UInteract | - · DES POA | 20 |
| MS | 89-105 | EFW2 RS 28; 10+ | UI-2/UI-3 ICESA/EFW2 | 21-002 (MANUAL) · J-9 | **15** |
| MT | MW-1; MW-3 | EFW2 via TAP | eServices, e-file mandatory | MT POA/2848 + TAP access | 20 |
| NC | NC-5/5P/5Q; NC-3 | eNC3 fixed-field v9-2026 | NCUI 101; 10+ | GEN-58 (superseded) · DES POA | 20 |
| ND | 306; 307 | EFW2 TAP | UI EASY / SFTP | Form 500 | 20 |
| NE | 941N | EFW2 NE RS+RV; >50 | NEworks / FTP | Form 33 · NDOL POA | 20 |
| NH | none | none | WebTax/NHUIS | - · written request / NHUIS | 20 (+ contractors) |
| NJ | NJ-927/500; NJ-W-3 | electronic; **Feb 15** | WR-30 (30th, no extension) | M-5008-R · DOL POA | 20 (+ contractors) |
| NM | TRD-41414 + TRD-41431 | TAP TXT or CF/SF | electronic (Delimited/ICESA/XML/EFW2) | ACD-31102 · ES-905 | 20 |
| NV | none (MBT TAX-F003) | none | ESS EFW2/CSV | - · ESS external user | 20 |
| NY | NYS-45 (combined) | **not filed** | NYS-45 Pub. 72.5 | POA-1 (gated) · agent ID | 20 |
| OH | IT 501; IT 941; SD 101/141 | upload with SD code | ODJFS (spec not read) | WT 8655 / TBOR 1 · JFS-20106 | 20 |
| OK | quarterly (20th) | EFW2 OkTAP | OES-3 ICESA 275 | BT-129 · OES-190T | 20 |
| OR | Form OQ combined | OR-WR iWire EFW2 | in OQ (Form 132) | OR-AUTH-REP/INFO | 20 (+ contractors) |
| PA | W-3; REV-1667 | myPATH EFW2/CSV; 10+ | UC-2/2A UC-2010 | REV-677 · UCMS handshake | 20 |
| RI | RI-941; RI W-3 | EFW2 RS; 25+ RI employees | DLT TX-17; 25+ | RI-2848 · not located | **14** |
| SC | WH-1605/1606 | EFW2 SC RS; 10+ | SUITS ICESA/EFW2/XML/CSV | SC2848 · UCE-1010 | 20 |
| SD | none | none | Form 21 | - · RA POA 01/2026 | 20 |
| TN | none | none | e-Services ICESA | - · no POA since 2025-05-27 | 20 |
| TX | none | none | QuickFile ICESA/MMREF/delimited | - · C-42 | 20 |
| UT | TC-941E | EFW2 RS; 250+ fixed | online only | TC-737 · DWS POA | 20 |
| VA | VA-5/15/16; VA-6 | EFW2 code 51 | ESS / Web Upload | PAR 101 · ESS TPA | 20 |
| VT | WHT-436; WHT-434 | direct to VT; 10+ / always for services | e-Services incl. gender and hourly wage | PA-1 · C-50 | **10** |
| WA | none | none | ESD (hours, SOC); PFML + WA Cares portal | - · UI POA per client | 20 |
| WI | WT-6; WT-7 | EFW2 RS 55; 10+ | 25+ | A-222 · UCT-8291-E | 20 |
| WV | IT-101Q; IT-103 | EFW2 RS+WV RV; 10+ or service | UC Employer System | WV-2848 · WorkForce WV POA | **14** |
| WY | none | none | WYUI | - · MODES-4444 | 20 |

**Local layers the provider must cover** (T4 elements, keyed by work/residence location):
- AL occupational, per city agent [US-ALS5-017];
- CO Denver OPT [US-COP52-001];
- DE Wilmington [US-DEP52-001];
- KY occupational [US-KYP52-002];
- MO St. Louis / Kansas City;
- NJ Newark and Jersey City [US-NJP6-001];
- OH municipal and school district [US-OHP52-003, US-FIL-012];
- OR Portland / Metro / Multnomah XML [US-ORS5-024];
- PA EIT/LST and Philadelphia [US-PAS5-017];
- WA Seattle PET [US-WAP51-001];
- MI cities; NY NYC/Yonkers inside NYS-45; MD county inside MW506.

## 5. What a provider must receive (minimum data set, provider-agnostic)

Derived from the read layouts: CA DE 8300, NY Pub. 72.5, OH bulk guide, Pub. 1474, and the state UI fields above.

- **Per employer entity:**
  - FEIN, legal name and address, matching IRS records [US-FIL-001];
  - every state withholding and UI account number;
  - local account IDs (e.g. Metro SHW-, Multnomah MCW-);
  - the signed 8655 and the state authorisations;
  - deposit frequency per jurisdiction.
- **Per employee, per period:**
  - SSN (never truncated on filings), name split as each state requires;
  - work state and locality, residence state and locality, school-district code (OH), county (IN, MD);
  - `sui_state`.
- **Per employee, per period, wages:**
  - federal wages, SS/Medicare wages;
  - state and local taxable wages and tax;
  - UI subject and taxable wages;
  - PFML/SDI/CCC/levy amounts.
- **Per employee, state extras:**
  - hours: MN, WA, MA, VT hourly, CT optional;
  - SOC/occupation: AK, IN, WA, WV, TX enhanced;
  - geographic code (AK); gender (VT hourly); weeks (OH, NJ base weeks); probationary flag (MO).
- **Per payroll:**
  - pay date, which drives deposit dates;
  - deposit amounts per jurisdiction, in cents.
- **New-hire feed:**
  - 653a fields, plus the state extras: DOB, start wage, health-insurance availability (MD, MS, NY, OR, NJ);
  - contractors in FL, NH, NJ, OR, MA, ME, IA, IL, VA, OH. Note: 1099 contractors are out of payroll scope, but the new-hire duty exists.
- **Annual:** W-2 data including TY2026 Box 12 TP/TT/TA and 14b, Box 14 state items; the EFW2 layout is pending.

## 6. Scope traps

- **CA and NY do not take a W-2.** Writing a state-W-2 spec for them is a filing that does not exist [US-CAS5-018, US-NYS5-010].
- **IA rejects the SSA EFW2 file** [US-IAS5-017].
- **IN new filers must use XML** [US-INS5-011].
- **VT left CF/SF** [US-VTS5-017]. **KS and MI W-2s are not shared through CF/SF** [US-KSS5-026, US-MIPIT-001].
- **NV MBT wages must equal ESD wages from 2026** [US-NVS5-009].
- **Deadline conflicts:**
  - MA W-2: Jan 31 vs end of March. Use Jan 31 [US-MAS5-015].
  - NM: Jan 31 (FYI-330) vs the Feb page [US-NMP52-005].
  - IN W-2: Jan 31 vs Feb 28 FAQ. Use Jan 31 [US-INS5-010].
  - NJ WR-30 due on the 30th with no weekend extension [US-NJS5-017].
- **TY2026 state W-2 editions** are not yet posted for GA, MD, SC, WV, IA, KS, MS and DC. Re-check in January 2027.

## 7. Special populations (US-OWN-005)

Federal populations are all IN. Filing consequences read:
- household employers: Schedule H, not 941 [US-FED-004]; and state annual options:
  - CT-W3 HHE [US-CTS5-014];
  - NJ-927-H;
  - DC annual UI;
  - FL RT-7;
  - SD 21D/E;
  - UT annual;
- agricultural: Form 943 and state annual returns (OR WA/STT-A, CT annual) [US-FEDR3-006, US-ORS5-010];
- WA exempt corporate officers reported as a count plus wages [US-WAS5-027].

State special-population rules beyond these are deferred (owner).

## 8. Parallelism note

The remaining closures are independent per-state lookups and can be fanned out:
- UI file layouts in 11 states;
- TY2026 W-2 editions in 8 states;
- 6 missing authorisation instruments: NY POA-1, ME 2848-ME/UC-28, MS 21-002, KY, LA R-7006, AR UI.

The EFW2 TY2026 PDF is a single user browser download.

## Synthesis D additions (2026-11-02)

Source: browser-pass rows S5B-P1 / S5B-P2 merged into `legal-basis-register.csv` and SSA EFW2 TY2026 (US-FEDS5-032) read locally. Every claim below carries its register_id; the facts file is authoritative. Full log: `_research/synthesis-D/SYNTHESIS-D.md`.

Facts added:
- `sir.az.ui.wage_report` = **UC-018 quarterly via DES Tax and Wage System (online) or bulk file; due last day of month after quarter; zero report required** (2026-01-01 → open) [A.2, US-AZB5-005, quoted from authority page, conf high]
- `sir.ct.paid_leave.bulk_format` = **Batch XML (XSD) or CSV via SFTP per File Specification Toolkit v2.1.9; employer-level return totals only; acknowledgement file E/W** (2026-10-05 → open) [A.3, US-CTB5-001, direct artifact inspection, conf high]
- `sir.mi.new_hire.days` = **20** days (2026-01-01 → open) [A.2, US-MIB5-001, quoted from authority page, conf high]
- `sir.fed.efw2.layout_ty2026` = **SSA Publication No. 42-007, EFW2 Tax Year 2026 (page header dated 2026-09-14; no version change entries yet). 512-byte records in order RA, RE, RW, [RO], [RS], RT, [RU], [RV], RF; RA/RE/RW/RT/RF required; RO/RS/RU/RV optional; RS and RV are not read or processed by SSA or IRS (state-defined). TY2026 changes: RE adds Employer Signature PIN (319-328); RW adds Box 14b Primary/Secondary Treasury Tipped Occupation Code (490-492 / 493-495); RO/RU split Codes A and B into separate money fields (combined A+B field valid through TY2025 only), add money fields for existing Codes J, K, L, P and new Codes TA, TP, TT; SS wage base 184,500; FIRE replaced by IRIS** (2026-01-01 → open) [A.2, US-FEDS5-032, direct artifact inspection, conf high]
- `sir.fed.efw2.state_records` = **Provider must build RS per state spec on the TY2026 base layout: state employer account 248-267, state code 274-275, state wages/tax 276-297, other state data 298-307, tax type code 308 with local wages/tax 309-330, supplemental 338-487; RV 3-512 state-defined; SSA ignores RS/RV** (2026-01-01 → open) [A.2, US-FEDS5-032, direct artifact inspection, conf high]
- `sir.fed.efw2.employer_signature_pin` = **Optional RE 319-328 Employer Signature PIN (S-XXXXXX-Y, Luhn) requested by the employer from SSA to sign wage reports electronically; blanks if none** (2026-01-01 → open) [A.2, US-FEDS5-032, direct artifact inspection, conf high]

Facts changed:
- `sir.fed.w2.format` (2026-01-01): note 'TY2026 record layout itself NOT read (26efw2.pdf gated, US-FIL-003 / US-FEDS5-032).' → 'TY2026 record layout read 2026-11-02: see sir.fed.efw2.layout_ty2026 (US-FEDS5-032).'

Open questions closed: `sir.fed.efw2.layout_ty2026`, `sir.ct.paid_leave.file_spec`.

Still open, new attempts recorded in `unresolved[].attempted`: `sir.mi.new_hire.statute`, `sir.w2.state_specs_ty2026`.

## Open questions (mirrors `unresolved[]` in SIR-facts.json)

- `sir.provider.selection`: owner decision outside the build. Closes with an owner/BAU RFP (6 questions).
- `sir.ny.withholding.agent_authorization`: POA-1 not read (US-FIL-021 gated).
- `sir.me.withholding.agent_authorization`: 2848-ME row superseded; UC-28 row MANUAL.
- `sir.ms.withholding.agent_authorization`: Form 21-002 not read (MANUAL B).
- `sir.ky.agent_authorization`: no KY instrument located.
- `sir.la.withholding.agent_authorization`: R-7006 row superseded, no successor.
- `sir.wy.ui.agent_authorization_form_text`: Drive PDF unreadable (gated).
- `sir.ca.de9c.file_spec`: DE 9C FSET/e-file field spec not fetched.
- `sir.in.w2.xml_schema`: IDORWTH2016V1.0 not downloaded.
- `sir.w2.state_specs_ty2026`: TY2026 editions not yet posted (GA, MD, SC, WV, IA, KS, MS, DC).
- `sir.ui.file_specs_missing`: UI layouts not read in 11 states.
- `sir.tx.ui.due_date`: TWC rule 815.107 blocked.
- `sir.mi.new_hire.statute`: MI statute and penalty not located.
