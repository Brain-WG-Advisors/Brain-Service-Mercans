# PSL research pack: United States (unit `8_sheets`)

> **Synthesis C (2026-11-02).** Register ids were normalized to the facts-schema pattern (map: `_research/stage5/ID-RENAME-MAP.csv`, ids in this pack already rewritten). Every fact that was held for the register_id pattern defect (marked here as "legacy id, NOT a fact", "PENDING", "(P)", "parked" or "carried in unresolved") is now a validated fact in `facts[]`; promotion log `_research/synthesis-C/_work/step2-promotion-log.csv`. Counts of held facts quoted below are historical. The Open questions block below mirrors the current `unresolved[]`.

Synthesis B, 2026-11-02. Source: `_research/stage5/{JUR}.md` sections 4 (payslip_statute) and 12 (data_protection), MANDATE US-MQ-03 / US-OWN-005 / US-OWN-006, and the register. No fetching this pass. Facts file: `_research/PSL-facts.json` (validated PASS). Every claim below carries its `register_id`; ids with multi-segment form (e.g. `US-MDP51-005`) are parked in the facts file under `_facts_blocked_by_register_id_pattern` because facts.schema 1.4.0 rejects that id shape (see report).

The PSL is one US template with per-jurisdiction rules. Sheet mapping is the builder's call. The sections below follow what the builder fills: the base payslip, the per-state mandatory element matrix, leave balances, SSN display, delivery, retention, annual statement (W-2) items and language.

## 1. Federal baseline

- No federal law requires a pay statement or fixes its content, delivery or language. 29 CFR 516.2(a) prescribes employer records only [US-FED-010]. Fact: `psl.fed.statement.required = false`.
- Payroll records are kept 3 years (29 CFR 516.5) [US-FEDS5-021]. Employment-tax records are kept 4 years [US-FEDS5-003].
- Build rule: one US payslip carrying the union of state elements, switched on by the work-location state (section 7).

## 2. Statement duty by jurisdiction

Scope codes used in the facts:
- `full`: a content list exists.
- `deductions_only`: only a deductions statement is required.
- `on_request`: a statement is due only when the employee asks.
- `non_flsa_only`: the duty covers only employees outside FLSA coverage.
- `none`: no state duty.

| Jur | Duty | Key elements beyond gross/deductions/net | Source |
|---|---|---|---|
| AK | full | rate; period dates; FIT/FICA; AK ESA; board/lodging; advances; ST and OT hours; **sick leave used and balance** | US-AKS5-001 |
| AL | none | federal records only | US-ALP52-001 |
| AR | none | tip-credit amount per hour in writing when it changes | US-ARP52-006 |
| AZ | direct deposit / pay card only (no list) | **sick time available, used YTD, pay as sick time on every paycheck** | US-AZS5-001, US-AZS5-011 |
| CA | full, 9 items | hours (not salaried exempt); piece units; period; **last 4 SSN or employee ID**; employer legal name/address; every rate with hours; **paid sick leave available** | US-CAS5-005, US-CAS5-011 |
| CO | full | name or SSN; employer name/address; COMPS Rule 7: rate, tips, credits, time worked | US-COP51-005, US-COS5-001 |
| CT | full | hours; ST and OT gross separately; **pay-code guide URL on every pay record (100+ employees, from 2026-10-01)** | US-CTP51-005, US-CTS5-028 |
| DC | full | pay date; gratuities on a separate line; hours; tip declaration cash/card; **from 2026-01-01 list of compensation sources** | US-DCS5-010 |
| DE | full, employers with >3 employees | pay period; each deduction separately; hours (hourly) | US-DES5-002 |
| FL | none (labor pools only) | 448.24(2)(g),(h) | US-FLL-002 |
| GA | none | no statement duty in 34-7-2 | US-GAP9L-001 |
| HI | full, 14 items | employer address/phone; total, regular and OT hours; ST and OT pay; allowances toward MW; pay date; period; rates incl. piece | US-HIP52-001 |
| IA | full | hours, wages earned, deductions; itemised computation within 10 working days on request | US-IAP51-002 |
| ID | deductions_only | 45-609(2) | US-IDP51-002 |
| IL | full (pay stub) | itemised deductions; pay-card payees hours and rate; access and copy rules | US-ILS5-024 |
| IN | full but scope-limited | hours, wages, deductions; IC 22-2-2-3 reading excludes FLSA-covered employers (70%) | US-INP6-001, US-INS5-001 |
| KS | on_request | deductions | US-KSP52-001 |
| KY | deductions, employers 10+ | each deduction and purpose; electronic needs computer and printer access | US-KYP8-001 |
| LA | none | hire notice only | US-LAR3-002 |
| MA | full | employer name; date; hours; hourly rate; deductions or increases | US-MAP51-008 |
| MD | full | employer phone; pay date and period; hours; rates; other bases of pay; **ESSL balance**; **no SSN at all** | US-MDP51-005, US-MDS5-013, US-MDS5-008 |
| ME | full | pay-period date; hours; total earnings; itemised deductions (corrects earlier rows) | US-MES5-006 |
| MI | full | hours; pay-period ID; itemised deductions; **comp time**; SSN 4 digits max | US-MIS5-009, US-MIS5-013 |
| MN | full, 12 items | **ESST hours available and used** | US-MNP6-001, US-MNS5-011 |
| MO | deductions_only (monthly total) | 290.080 | US-MOP52-002 |
| MS | none | US-OWN-006 recorded limit | US-MSP9L-001 |
| MT | deductions_only | every deduction incl. taxes; "none" statement if nothing deducted | US-MTP51-006 |
| NC | deductions_only | 95-25.13 | US-NCW1B-003 |
| ND | full | hours; rate; required and authorised deductions (reverses earlier "no provision") | US-NDS5-007 |
| NE | full | employer identity; hours paid (not FLSA-exempt); deductions | US-NEP51-004 |
| NH | deductions_only | monthly accounting for 275:48 I(d) deductions | US-NHP51-001 |
| NJ | deductions; employers 10+ add gross, net, rate, hours | 34:11-4.6(c) | US-NJP8-001 |
| NM | full | employer identity; hours; total wages and benefits; **YTD sick leave accrued/used at least quarterly** | US-NMP8-001, US-NMS5-002 |
| NV | deductions; **paid-leave hours available every payday (50+ NV employees)** | 608.110(2), 608.0197(1)(h) | US-NVR3-001, US-NVS5-001 |
| NY | full | dates of work; employer address and phone; rates and basis; allowances; regular and OT rates and hours; piece rates | US-NYS5-006 |
| OH | full (from 2025-04-09) | employee address; additions and deductions with purpose; hourly hours and rate | US-OHP51-001 |
| OK | deductions_only | 165.2 | US-OKS5-003 |
| OR | full, items A-M | employer registry/ID number; allowances; regular and OT; piece rates; **new-hire payroll-code explanation from 2026** | US-ORS5-026, US-ORS5-022 |
| PA | full | hours; rates; allowances; deductions; net | US-PAP51-001 |
| RI | hours + deductions with explanation | commercial construction adds regular rate | US-RIP51-002 |
| SC | full (gross + deductions) | exempt: domestic and fewer than 5 employees | US-SCP52-006 |
| SD | none | Title 60 scan | US-SDS5-001 |
| TN | none | federal records | US-TNS5-001 |
| TX | non_flsa_only | 62.003 earnings statement signed by the employer or agent; best practice for others | US-TXS5-003 |
| UT | deductions_only (construction licensees full) | 34-28-3(4),(5) | US-UTP6-001, US-UTS5-012 |
| VA | full | employer address; hours; rate; deductions with purpose | US-VAS5-003 |
| VT | full (weekly pay) | hours; hourly rate; deductions incl. meals | US-VTP9-001 |
| WA | full, separate from paycheck | hours/days; rates; period; payment date; **sick leave accrued/used/available at least monthly** | US-WAS5-004, US-WAS5-005 |
| WI | hours, rate, deductions | coding allowed | US-WIP52-001 |
| WV | full | rate or salary; hours; OT rate; bonus/incentive; deductions (42 CSR 5 s.7.3 sunset 2029-07-01) | US-WVS5-008 |
| WY | deductions_only | agricultural exempt | US-WYP51-005 |

Build consequences:
- The US payslip must carry hours, every rate with its hours, OT split, allowances toward minimum wage, piece counts, employer address/phone and pay period on the base template. That is the union of CA/HI/NY/OR.
- Optional blocks switch on per state: tips/gratuities (DC, CO), compensation sources (DC), pay-code guide URL (CT), comp time (MI).
- **Texas (correction).** The sealed US-MQ-63 part 6 line "no pay-statement requirement" is wrong as a statement about Texas. The payslip and CCG say: "statutory earnings statement for non-FLSA employees (62.003); best practice for everyone else" [US-TXS5-003].
- **Maine and North Dakota.** Both have content rules; the old absence rows are superseded [US-MES5-006, US-NDS5-007].
- **Indiana.** The duty is scope-limited (IN-OQ): emit the elements anyway [US-INS5-001].

## 3. Leave balances on the statement (hard PSL fields)

| Jur | Item | Frequency | Source |
|---|---|---|---|
| AK | sick leave used in accrual year + balance (PTO used/balance satisfies) | each statement | US-AKS5-001, US-AKS5-010 |
| AZ | earned paid sick time available, used YTD, pay received as sick time | each regular paycheck | US-AZS5-011 |
| CA | paid sick leave available | each payday (statement or separate writing) | US-CAS5-011 |
| MD | ESSL balance (online system satisfies) | each pay | US-MDS5-013 |
| MN | ESST hours available and used | each pay period | US-MNS5-011 |
| NM | YTD earned sick leave accrued and used | at least quarterly | US-NMS5-002 |
| NV | available paid-leave hours (50+ NV employees) | every payday | US-NVS5-001 |
| WA | paid sick leave accrued, used, available | at least monthly | US-WAS5-005 |
| NYC | accrued/used/balance | lead only | US-NYS5-023 is MANUAL B, so unresolved |

## 4. SSN on pay documents

The build default is last 4 digits at most, and none at all in MD. The rule per state:

- **MD**: no SSN on the wage check, any attachment, the direct-deposit notice or a card-credit notice. Treat a truncated SSN as barred too [US-MDS5-008].
- **CA**: last 4 digits or an employee ID [US-CAS5-005].
- **MI**: no more than 4 sequential digits, and an SSN privacy policy is required [US-MIS5-013].
- **NE**: last 4 digits at most where coworkers can see it [US-NES5-013].
- **SC**: 5 digits at most on mailed material [US-SCS5-009].
- **RI**: no part of the SSN on mailed material [US-RIS5-020].
- **No full SSN on mailed material:**
  - AK [US-AKS5-016]; HI [US-HIS5-028]; NC [US-NCS5-016]; OK [US-OKS5-008];
  - PA [US-PAS5-020]; TX [US-TXS5-013]; VT [US-VTS5-015].
- **CO**: the SSN may replace the name (8-4-103(4)(e)). The build uses the name [US-COP51-005].
- **MO**: neither the SSN nor its last 4 digits may serve as the employee number [US-MOS5-016].
- **NY**: Labor Law 203-d bars public display [US-NYS5-009].
- **W-2**: truncation is allowed on employee copies only, never on Copy A [US-FEDS5-022]. Several states reject a truncated SSN on state copies:
  - AZ [US-AZS5-025];
  - DE [US-DES5-008];
  - MT [US-MTS5-005];
  - SC RS record [US-SCS5-017].

  OK allows the last 4 digits on the employee statement [US-OKS5-014].
- **Not read** (absence not proven): CO, DC, IL, IA, ID, KY, LA, MA, ME, NJ (ACCESS), NM (403), TN, UT, WV. Recorded as one unresolved entry.

## 5. Electronic delivery

| Rule | Jurisdictions | Sources |
|---|---|---|
| Express consent | CT (explicit consent plus a secure way to access and print); OR (express agreement plus print/store on receipt) | US-CTS5-027, US-ORS5-026 |
| Written authorization | HI | US-HIS5-007 |
| Allowed with conditions | ME (print at no cost); MN (employer computer access, kept 3 years); KY (computer and printer access); WA (receive and copy on payday); DE (employee can retain it; paper on request); NJ (unless paper requested); WV (direct access) | US-MES5-006, US-MNP6-001, US-KYP8-001, US-WAS5-004, US-DES5-002, US-NJP8-001, US-WVS5-008 |
| Allowed, no consent | IA, NC, VA ("online accounting"), MD ("written or online"), AK | US-IAP51-002, US-NCS5-024, US-VAS5-003, US-MDP51-005, US-AKS5-001 |
| Open (statute silent, guidance not read) | CA, CO, MA, NY, NV | unresolved entries |

Build default: electronic with an opt-in consent record and free print or download access. That satisfies the strictest rules read (CT, OR, HI).

## 6. Retention (pay records)

The longest rule read is 6 years:
- NJ wage-hour 6 [US-NJS5-022];
- NY 6 [US-NYS5-006];
- AR withholding 6 [US-ARP51-002, figure read in the local file].

Then:
- WV 5 [US-WVS5-008]; MT payroll-tax 5 [US-MTS5-005];
- AZ 4 [US-AZS5-006]; WA ESD 4 [US-WAS5-030]; OK tax 4 [US-OKS5-014];
- federal 3 / IRS 4 [US-FEDS5-021, US-FEDS5-003];
- NV 2 [US-NVS5-001]; OR 2 [US-ORS5-019]; WY 2 [US-WYS5-001];
- KY 1 [US-KYP8-002].

GA GDOL records are kept 7 years (with full SSN) [US-GAS5-005]. NC 10 years is unresolved: the row does not carry it.

Build default: 7 years for payslip archives. That covers every period read.

## 7. Multistate reach

CA Lab. Code 226 applies when CA is the principal place of work. It is *Ward v. United Airlines*, Cal. S. Ct. **S248702**, 2020-06-29, on Lab. Code 226; in force; level = pay-statement content [US-MULTIS5-018].

Elsewhere the default is the work-location state's statute:
- IA "employed in this state" [US-IAS5-027];
- WV, OK, WY, DE: work in the state (stage-5 findings).

The payslip rule set is therefore keyed by `work_location_jurisdiction`, not residence.

## 8. Annual statement (W-2) items the payslip/YTD must feed

- **TY2026 changes** [US-FEDS5-007]:
  - Box 12 TP (cash tips), TT (qualified overtime), TA (Trump-account employer contribution);
  - Box 14 split into 14a and 14b (Treasury Tipped Occupation Code).
  - Mandatory from TY2026; the penalty relief was TY2025 only [US-FEDS5-013].
  - Level: employer reporting. The employee deduction operates at assessment [US-FEDS5-030].
- **Box 14 state items:**
  - VT Child Care Contribution employee share. Max 0.11% of the 0.44% total; the employer may withhold less or none [US-VTS5-030].
  - ME PFML label **MEPFML**. The employee share is withheld after taxes [US-MES5-025, A.3].
  - CA SDI as **CASDI** (or VPDI); CA PIT wages in box 16 and CA PIT withheld in box 17 [US-CAS5-018].
- **Multistate:** up to two states and two localities per W-2; a second W-2 for more [US-MULTIS5-011].
- **MA PFML:** no active row on W-2 box 14 labelling was located in this pass. It is not asserted.

## 9. Language (payslip vs notices)

- Payslip in English. Authority-facing filings in English. es is rank 2: a seam for the payslip, and mandatory-later for notice templates. This is owner-delegated decision US-OWN-006, carried under `_owner_decisions`, not as a fact, because the owner row has no A tier.
- The federal official language is English, with no obligation on private employers [US-FED-020].
- Notice/poster seams (facts `psl.notice_language.*`):
  - CA 2810.5 [US-CAP6-001];
  - NY 195(1)(a) [US-NYP51-003];
  - MN [US-MNP6-001];
  - DC [US-DCS5-010];
  - NJ gender-equity, 50+ employees, deliverable as a pay-check insert [US-NJP9M-001];
  - NJ ESL [US-FEDR3-010];
  - CO COMPS 7.4.3 [US-COP9L-001];
  - CO 5% [US-COL-001];
  - TX HB 915 [US-TXP9M-001];
  - AZ [US-AZL-001];
  - CT [US-CTL-001];
  - DE [US-DEL-001];
  - FL [US-FLL-001];
  - MA [US-MAL-002];
  - MI 10% [US-MIL-001];
  - OR BOLI template [US-ORL-001];
  - VT pay-card [US-VTL-001].
- **OR SB 906 (from 2026-01-01):** the new-hire explanation of all payroll codes is itself a PSL companion document [US-ORS5-022].

## 10. Special populations (US-OWN-005)

- Federal populations are all IN: NRA, statutory, household, agricultural, clergy, employees abroad. State-level special-population rules are deferred to a later round [US-OWN-005].
- PSL-relevant carve-outs read:
  - CA household employees excluded from 226 [US-CAS5-005].
  - SC domestic employers and those with fewer than 5 employees exempt [US-SCP52-006].
  - WY agricultural exempt [US-WYP51-005].
  - VA agricultural employers: statement on request only [US-VAS5-003].
  - DE state and federal employees excluded [US-DES5-002].
  - TX: non-FLSA employees only [US-TXS5-003].
  - IN: non-FLSA employers only [US-INS5-001].

## Open questions (mirrors `unresolved[]` in PSL-facts.json)

- `psl.ca.statement.electronic_consent`: CA Lab. Code 226 says "in writing"; no electronic-consent rule fetched. Closes with the Labor Commissioner FAQ on electronic wage statements.
- `psl.co.statement.electronic_consent`: no Colorado electronic-consent rule read. Closes with the CDLE COMPS / Wage Act rule.
- `psl.ma.statement.electronic_consent`: the AG rule on electronic pay stubs was not located. Closes with the MA AG Fair Labor Division advisory.
- `psl.ny.statement.electronic_consent`: NYDOL guidance not read. Closes with the NYDOL WTPA FAQ.
- `psl.nyc.pto.on_statement`: only a tier-B lead (US-NYS5-023). Closes with NYC Admin. Code 20-919 / DCWP rule text.
- `psl.ri.retention_and_hire_notice_2026`: the new 28-14-12 was not reachable (US-RIS5-008 partial). Closes with the official R.I.G.L. 28-14-12 text.
- `psl.il.statement.content_rule_300_600`: 56 Ill. Adm. Code 300.600 not read. Closes with JCAR text.
- `psl.nv.statement.electronic_consent`: no Nevada rule located. Closes with NRS/NAC 608 or Labor Commissioner guidance.
- `psl.ssn_rule.unread_states`: SSN statutes not read in 14 jurisdictions. Closes with one targeted read per statute.
- `psl.nc.retention.withholding_records.years`: the 10-year figure is cited in NC.md but not carried by US-NC-001. Closes by re-registering NC-30 s.26.
- `psl.in.statement.scope_confirmation`: IC 22-2-2-3 reading at 70%. Closes with Indiana DOL guidance.
- `psl.tx.statement.scope_confirmation`: 62.151 applied without TWC commentary. Closes with the TWC Labor Law page.
