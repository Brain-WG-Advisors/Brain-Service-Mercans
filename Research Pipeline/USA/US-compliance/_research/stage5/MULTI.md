# Stage 5 — MULTI (multistate routing layer), 13-domain hunt

Unit: MULTI. Worker: compliance-source-hunter, 2026-11-02. Brief: `_prompts/stage5-brief.md`.
Register shard: `00-official-sources/_register-shards/S5-MULTI.csv` (26 rows, `US-MULTIS5-001..026`).
Sources: `00-official-sources/ccg-sources/MULTI/` (24 files, 3,664,676 bytes).
Budget: 90 fetches / 3 h declared. Used about 45 fetches (incl. 3 web searches) in about 20 min wall clock.

Reuse rule applied. Active A.1/A.2 rows already in `legal-basis-register.csv` are cited, not re-fetched: the 23 `US-MULTI-0xx` rows, the per-state part-5 rows, and `US-FEDP52-005/006`. New rows were added only where the build held no official copy (the LII republications of 49 USC 14503/11502), where a rule was missing (the IL 30-day rule, the LA 30-day rule, Ward/Oman, W-2 boxes 15-20, IWO, new-hire) or where the row had no local file (the NY convenience test).

Routing keys this unit feeds (build-manifest `_sub_national_key`): `work_location_jurisdiction`, `residence_jurisdiction`, `sui_state`.

---

## 1. labour_code — which State's wage-hour law applies to a multistate worker
- **Federal floor plus overlay.** The FLSA does not excuse a higher State or municipal minimum wage, a lower maximum workweek or a stricter child-labour standard (29 U.S.C. 218(a)) [US-MULTIS5-008, A.1]. The applicable overlay is the law of the place where the work is performed. No federal choice-of-law rule exists beyond this.
- **California, by ruling (G-RULING).**
  - *Oman v. Delta Air Lines*, Cal. S. Ct. **S248726**, 2020-06-29. It turns on Lab. Code 204 (pay-day timing) and 226. Status: in force. Level: employer pay timing / pay statement. Lab. Code 204 and 226 do not reach pay periods in which the employee works in CA only episodically and for less than a day at a time, unless the employee works primarily in CA in that period, or works primarily in no State and has the CA base of operations. CA wage-hour reach is decided statute by statute (*Sullivan v. Oracle* (2011) 51 Cal.4th 1191, as cited). The minimum-wage reach was left undecided [US-MULTIS5-019, A.1].
- Per-state minimum wage, overtime, pay frequency and method of payment are carried by the 51 state units, not here.
- Confidence: 85% (rule structure). The CA minimum-wage reach for nonresidents is an open question.

## 2. income_tax — work-State vs residence, reciprocity, thresholds, convenience, transport workers
**2.1 General sourcing (MANDATE US-MQ-10(a)).** There is no general federal rule.
- Each State taxes its residents on all wages and gives a credit for tax paid to the work State.
- Each State taxes nonresidents on wages for services performed in the State.
- Federal limits exist only for transport workers (2.6) and military spouses (2.7) [US-FEDP52-005; US-MULTIS5-001..005].
- Nine jurisdictions levy no wage income tax: AK, FL, NV, NH, SD, TN, TX, WA, WY (per-state answers US-MQ-20, 29, 53, 50, 61, 62, 63, 67, 70).

**2.2 Resident withholding when the employee works in another State: "difference" withholding.** This is how a residence State treats its own residents when the work State also requires withholding. Each pattern below is read from the State's own source.

| Residence State | Rule for its resident working in another State | register_id |
|---|---|---|
| CT | All wages subject. Where the employer must withhold for the other jurisdiction, CT tax is prorated and only the excess is remitted | US-CTP10-001 |
| KS | KS tax less the other State's required withholding. Example: 250 - 130 = 120. Zero if the other State's withholding is higher | US-KSP51-003 |
| VT | Compute on the full payment, then reduce by tax withheld for the work State | US-VTP51-003 |
| NC, CO, GA | No home-State withholding on wages for services in a State that requires its own withholding | US-NCP51-002, US-COP51-002, US-GAP52-003 |
| SC | Withhold for the other State. If that State has no income tax, withhold SC | US-SCP51-003, US-SCR3-003 |
| OK, OH, NY, LA | Residents are withheld on wages wherever earned (LA: if those wages are not subject to withholding where earned) | US-OKP52-001, US-OHP52-006, US-NY-013, US-LAP51-001 |
| Credit at assessment only (no withholding rule) | DC, ME, RI, SC, OH, AR, OK, MS | US-DCP51-007, US-MEP52-004, US-RIP52-002, US-SCR3-004, US-OHP52-004, US-ARP52-001, US-OKP52-002, US-MSP52-003 |

Level: the credit operates at **assessment**, not withholding (e.g. AZ, US-AZWH-003). The WTC/DD must not model a credit as a payroll deduction.

**2.3 Reciprocity matrix (all States, from each State's own source).** Reciprocity is a bilateral exemption from work-State withholding when the employee gives the employer a nonresidence certificate.
- 30 reciprocal pairs, each confirmed on BOTH sides from that State's own source. The partner lists below are symmetric.

| State | Partners | Employee certificate | register_id |
|---|---|---|---|
| DC | MD, VA (and see note) | D-4A | US-MULTI-016, US-DCP51-006 |
| IA | IL | IA 44-016 | US-MULTI-018 |
| IL | IA, KY, MI, WI | IL-W-5-NR | US-ILP51-001, US-MULTIS5-023 |
| IN | KY, MI, OH, PA, WI | WH-47 | US-IN-002 |
| KY | IL, IN, MI, OH (unless 20% S-corp owner), VA (daily commuters only), WV, WI | 42A809 | US-MULTI-009, US-KY-001 |
| MD | DC, PA, VA, WV (not for abode >6 months and 183+ days, except WV) | MW507 (US-MDP51-001) | US-MULTI-008 |
| MI | IL, IN, KY, MN, OH, WI | per MI Guide 446 (not named in the row) | US-MULTI-010, US-MIP51-001 |
| MN | MI, ND (must return home at least monthly; yearly MWR) | MWR | US-MULTI-013 |
| MT | ND | MW-4 | US-MTP51-004 |
| ND | MN, MT (yearly NDW-R) | NDW-R | US-MULTI-014, US-NDP51-001 |
| NJ | PA (compensation only) | NJ-165 | US-MULTI-011 |
| OH | IN, KY, MI, PA, WV | IT 4 (combined certificate; superseded row US-OHP51-002, confirm in OH unit) | US-MULTI-005, US-OHP52-006 |
| PA | IN, MD, NJ, OH, VA, WV | REV-419 | US-MULTI-007, US-PA-001 |
| VA | DC, KY (daily commuters), MD, PA, WV | VA certificate (not named in the row; VA unit) | US-MULTI-004, US-VAPIT-004 |
| WI | IL, IN, KY, MI | W-220 | US-MULTI-006, US-WIP51-001 |
| WV | KY, MD, OH, PA, VA | WV/IT-104 | US-MULTI-015 |

- **Unilateral, not reciprocal: AZ.** AZ exempts residents of CA, IN, OR and VA (Form WEC) because those States give a credit. The reverse does not hold: an AZ resident working in CA is withheld by CA [US-MULTI-017, US-AZP51-002]. Model it as one-way.
- **DC note.** D.C. Code 1-206.02(a)(5) bars DC from taxing any nonresident's personal income [US-DCP51-006]. DC withholding therefore stops for ANY nonresident (D-4A: domicile outside DC and under 183 days), not only for MD/VA residents. The "MD, VA" pairing matters only from the partner side.
- **No reciprocity (explicit State source):** AR, CT, DE, GA, HI, ME (agreements authorised, none in force), MO, MS, NC, NE, NY, OK, OR, RI, SC, VT. Sources: US-MQ part-5 answers; US-MULTI-019 (DE), US-MOP51-001, US-MEP52-005, US-CTP10-001, US-ORP10-001.
- **Without an explicit negative row:** AL, CA, CO, ID, KS, LA, MA, NM, UT. None is listed as a partner by any reciprocal State above, so no pair is missed. The negative is carried in their part-5 answers.
- **Local taxes are outside state reciprocity:**
  - MI city taxes (US-MQ-42);
  - IN county tax still withheld (US-MQ-35, US-IN-002);
  - PA local EIT: higher of the resident EIT or the work-municipality nonresident rate (US-PA-004);
  - OH municipal / school-district taxes (OH unit);
  - MD county tax: nonresident special rate (US-MDP51-001).

**2.4 Nonresident day/dollar thresholds (withholding starts after).**

| State | Threshold | register_id |
|---|---|---|
| AL | 30 days (duties in more than one State; resident State has a similar exclusion or no PIT); from day 31 all AL wages for the year | US-MULTI-021 |
| AZ | 60 days | US-MULTI-017 |
| CT | 15 days; above that, all CT days including the first 15 | US-CTP10-001 |
| DC | Nonresidents not taxed at all; residence test 183 days | US-DCP51-006, US-MULTI-016 |
| HI | 60 days, paid from an office outside HI (HW-6) | US-HIP51-002 |
| ID | under 1,000 USD | US-IDP52-002 |
| IL | more than 30 working days, for non-localized service (localization rules first) | **US-MULTIS5-023** |
| LA | **30 days from 2026-01-01** (was 25); from day 31, withhold for every day incl. the first 30; home-State condition repealed | **US-MULTIS5-021**, US-MULTIS5-022 |
| ME | more than 12 days AND more than 3,000 | US-MEP52-003 |
| MT | under 30 days and work in more than one State | US-MTP51-003 |
| NE | more than 7 days (from 2025) | US-NEP51-002 |
| NM | 15 days or fewer | US-NMP52-002 |
| OK | 300 USD per quarter | US-OKP51-002 |
| OR | Oregon wages under the standard deduction | US-ORP10-001 |
| UT | 20 days, resident of a no-tax or similar-exclusion State | US-UTP51-002 |
| VT | out-of-state employers: from 30 days of work at a VT location | US-VTP52-003 |
| WV | 30 days, work in more than one State | US-MULTI-015 |
| GA | more than 5% or 5,000 USD attributable to GA | US-MQ-30 (US-GAP52-003) |
| SC | IRC 151(d) amount (except SC-situs construction) | US-MQ-60 (US-SCR3-001/003) |
| No threshold, ratio from day 1 | CA (working-day ratio), CO (days present), NY (day ratio with convenience test), MS (earnings ratio), AR | US-MULTIS5-010, US-COP51-002, US-MULTIS5-013, US-MSP52-002, US-ARP51-002 |

**2.5 Convenience-of-the-employer / remote-work sourcing.**
- **NY:** 20 NYCRR 132.18(a). Days outside NY count only if worked of necessity. Home-office days are NY days unless the home is a bona fide employer office [US-MULTIS5-013 (TSB-M-06(5)I), US-MULTIS5-012 (DTF FAQ), US-MULTI-003].
- **PA:** 61 Pa. Code 109.8 necessity test, same structure as NY's [US-MULTIS5-014, A.1]. The PA reciprocal agreements prevail.
- **DE:** working from home does not qualify for the PIT-SCW exclusion (assessment level) [US-MULTIS5-015].
- **NE:** from 2025, services for the nonresident's convenience are NE-sourced (77-2733(8)(c)) [US-NEP51-002].
- **Retaliatory / reciprocal convenience rules:**
  - NJ, from 2023, applies the rule against residents of States that apply one: DE, NE, NY, with CT by reciprocal law; PA is excluded [US-MULTI-012, US-NJP52-002];
  - CT, from 2019 [US-MULTI-020].
- **AR:** not a convenience State. The DFA guide sources nonresident wages to services performed in AR [US-ARP51-002]. The 2021 repeal (SB 484) is a tier-B lead only, primary not fetched.
- Everywhere else, wages follow the place of physical performance (2.1).

**2.6 Federal transport-worker limits (A.1, official text).**
- 49 U.S.C. 14503: motor carrier employees with duties in 2 or more States are taxed by the residence State only [US-MULTIS5-001, supersedes the LII row US-FEDP51-007].
- 49 U.S.C. 11502: rail, residence State only [US-MULTIS5-002, supersedes US-FEDP51-008].
- 49 U.S.C. 40116(f): air carrier, residence State plus the State where more than 50% of pay is earned (scheduled flight time) [US-MULTIS5-003].
- 46 U.S.C. 11108: seamen's wages may not be withheld for State tax; multi-State pilots and crew are taxable only by the residence State [US-MULTIS5-004].
- 4 U.S.C. 114: retirement income only, not wages [US-FEDP51-009].

**2.7 Military spouses.** Under 50 U.S.C. 4001(a)(2)-(3), (c), the spouse's service income is not sourced to the duty State, and the couple may elect the servicemember's residence, the spouse's residence or the permanent duty station [US-MULTIS5-005]. Payroll effect: stop work-State withholding on the State certificate.

**2.8 Live federal proposals (not enacted, do not model).** S. 1443 (2025-04-10, Senate Finance) and H.R. 10271 (2026-09-03, House Judiciary), the Mobile Workforce State Income Tax Simplification Act. They would allow taxation only by the residence State plus a State of more than 30 days of presence, effective 1 January of the second year after enactment [US-MULTIS5-020, US-MULTIS5-025].

Confidence: 90% on the reciprocity matrix and the convenience list; 85% on thresholds (LA's regulation is not yet final).

## 3. social_security — SUI localization, reciprocal coverage, wage-base credit, PFML coverage
- **Localization test (sui_state).** One State covers the employee's entire service with one employer. The test is applied in order:
  1. localized: performed entirely in the State, or out-of-state service only incidental (temporary, transitory, isolated);
  2. else some service in the base-of-operations State;
  3. else some service in the State of direction or control;
  4. else some service in the State of residence.
- Sources: US-FEDP52-005 (DOL Comparison 2023, still the latest edition [US-MULTIS5-026]); UIPL 20-04 (2004, continuing, adds telecommuting examples) [US-MULTIS5-016]; the DOL OUI restatement in the Spirit Airlines memo [US-MULTIS5-017, second independent document]; statutory instances Fla. Stat. 443.1216 [US-MULTI-001] and RCW 50A.05.010(8) [US-MULTIS5-024].
- **Reciprocal coverage election.** When no test resolves the case, the employer, the employee and the States may agree to cover all service in one State: a State where services are performed, the State of residence, or a State where the employer has a place of business. A few States do not participate [US-FEDP52-005; CA CUIC 602/603, US-MULTIS5-010].
- **Wage base when an employee moves between States.**
  - FUTA: 7,000 per employer per calendar year across all States; successor carry-over [US-MULTIS5-009].
  - SUI: each State decides whether wages already reported to another State count toward its own base. Verified for CA only: CUIC 930.1, credit in the same year on transfer to CA [US-MULTIS5-010]. Other States are open (see Open questions).
- **PFML/SDI coverage.** WA PFML uses the UI localization definition [US-MULTIS5-024]. The DD should key the premium State to `sui_state` unless a state unit proves otherwise.
- **Employee UI contributions** exist only in AK, NJ and PA [US-FEDP52-006].
- Confidence: 90% on the test; 60% on SUI wage-base credit across States (only CA proven).

## 4. payslip_statute — multistate reach
- *Ward v. United Airlines*, Cal. S. Ct. **S248702**, 2020-06-29. It turns on Lab. Code 226 (with Wage Order 9 sec. 1(E)). Status: in force. Level: pay-statement content (payroll output).
- The rule: Lab. Code 226 applies if the employee's PRINCIPAL place of work is in CA, meaning a majority of working time there. For workers with no majority State, it applies where CA is the base of work operations and some work is done in CA. Employer location, residence, place of pay receipt, taxes paid and a CBA are irrelevant [US-MULTIS5-018].
- No other State's reach rule was researched. Default: the pay-statement statute of the work-location State; the payslip is in English (MANDATE language rule).
- Confidence: 75%.

## 5. reporting_instruments — multistate W-2, new hire, UI reporting
- **W-2 boxes 15-20** carry up to TWO States and TWO localities. For more, issue a second W-2 repeating boxes a-f, never duplicating federal data on Copy A. On the W-3, box 15 = "X" when more than one State; boxes 16-19 are summed [US-MULTIS5-011].
- State copies and formats (EFW2 RS record or state spec) are per State, in the state units.
- **New hire.** A multistate employer that reports electronically may send all new-hire reports to ONE designated State after notifying HHS in writing. Deadline: 20 days, or two monthly transmissions 12-16 days apart [US-MULTIS5-006; CA restatement US-MULTIS5-010]. The HHS/OCSS registration page itself was not reachable (ACCESS gap).
- **UI quarterly wage report** goes to the `sui_state` only (localization, section 3). State income-tax withholding returns go to every State where withholding applies under section 2.
- **Registration / nexus triggers.** No federal rule. The trigger is the first wage subject to that State's withholding (section 2.4 thresholds) or the first localized employee (UI). Examples:
  - VT: out-of-state employers from 30 days [US-VTP52-003];
  - OR: an out-of-state employer withholds for OR residents working in OR, with relief at 300 or less [US-ORP10-001];
  - MI: out-of-state employers with employees working in MI [US-MIP51-001].
- Confidence: 85%.

## 6. leave
- No federal multistate rule beyond section 3 (PFML coverage follows localization, WA proven).
- Paid-sick-leave coverage of a multistate worker (e.g. hours-in-State thresholds) is per State and NOT researched here. Open question routed to the state units.
- Confidence: 50%.

## 7. termination
- Not applicable at MULTI level. Final-pay timing and payout follow the work-State statute (state units). For CA, *Oman* limits Lab. Code 204 for episodic CA work [US-MULTIS5-019]; final-pay sections 201-203 were not ruled on there.

## 8. benefits_in_kind
- Not applicable at MULTI level. State conformity to federal exclusions (PA and NJ 401(k), CA/NJ HSA) is a per-State question; the routing layer only selects which State's rule applies (section 2).

## 9. deductions_garnishments
- **Interstate child-support IWO.** The employer applies the income-withholding law of the State of the obligor's PRINCIPAL PLACE OF EMPLOYMENT for the fee, the maximum withheld, the timing, the priority among obligees and terms not in the order. Remittance goes to the SDU within 7 business days. Compliance with a notice regular on its face shields from civil liability; every State must have UIFSA in effect [US-MULTIS5-007, A.1].
- The CCPA limits are a FED matter.
- Confidence: 90%.

## 10. collective_agreements
- Not applicable at MULTI level. Prevailing-wage regimes attach to the project location (state units, P5/P6 rows).

## 11. indexation
- Not applicable at MULTI level. The day/dollar thresholds in section 2.4 are fixed in statute, not indexed. Exceptions carried by the state units: OR (the standard deduction amount) and SC (the IRC 151(d) amount).

## 12. data_protection
- Not applicable at MULTI level. SSN truncation and payroll-record privacy are per State.
- Cross-State data transfer has no federal payroll-specific rule located (not researched; low payroll impact).

## 13. live_legal_change (sweep 2026-01-01 to 2026-11-02, multistate scope)

| Change | Status | Level | register_id |
|---|---|---|---|
| LA mobile workforce: 25 to 30 days; home-State condition repealed | Act 382 (2025) in force, applies to tax periods from 2026-01-01; LAC 61:I.1923 amendment proposed (NOI, comments to 2026-01-26), final adoption not verified | withholding + nonresident tax | US-MULTIS5-021, -022 |
| AL 30-day safe harbor | Act 2025-334, in force for 2026 | withholding | US-MULTI-021 |
| NE 7-day threshold + convenience | in force from tax year 2025 | withholding / sourcing | US-NEP51-002 |
| Federal Mobile Workforce Act (S. 1443, H.R. 10271) | introduced, in committee, not enacted | withholding + tax | US-MULTIS5-020, -025 |
| DOL localization reminder (Spirit Airlines) | guidance, restates UIPL 20-04 | UI reporting | US-MULTIS5-017 |

What the sweep covered: govinfo for federal bills; LA legislature and LDR; State pages already registered. It did NOT cover each State's bulletin feed one by one; the 51 state units own that sweep.

---

## Special populations (multistate round, US-OWN-005)

| Population | Multistate rule | register_id |
|---|---|---|
| Motor carrier drivers (2+ States) | residence State only (tax and information returns) | US-MULTIS5-001 |
| Rail employees (2+ States) | residence State only | US-MULTIS5-002 |
| Air carrier crew (2+ States) | residence State + State of more than 50% scheduled flight time | US-MULTIS5-003 |
| Seamen / vessel crew, pilots | no State withholding on seamen's wages; multi-State crew/pilots taxed by residence only | US-MULTIS5-004 |
| Military spouses | duty State does not source the spouse's wages; residence election (servicemember, spouse or duty station) | US-MULTIS5-005; state certificates US-MULTI-015/016, US-ILP51-001 |
| Interstate transportation workers (CA wage law) | CA Lab. Code 226/204 apply where CA is the base of operations when no majority State | US-MULTIS5-018, -019 |
| Telecommuters | income tax: physical place of work, except the convenience/necessity States (NY, PA, DE, NE; NJ/CT retaliatory); UI: localization (UIPL 20-04) | section 2.5; US-MULTIS5-016 |
| Athletes / entertainers | excluded from the 30-day safe harbors (WV, MT, UT); duty-day rules per State | US-MULTI-015, US-MTP51-003, US-UTP51-002 |
| Domestic / household workers | no multistate rule beyond federal; state units | federal: FED unit |
| Agricultural workers | no multistate rule beyond federal (ID: agricultural under 1,000 not withheld) | US-IDP52-002 |
| Minors, tipped, clergy, students, statutory employees, government employees | no multistate-specific rule found; state units carry the state rule; federal treatment in the FED unit | (pages read: none specific; negative not proven) |
| Nonresident aliens | federal (FED unit); States follow their resident/nonresident rules (e.g. MS withholds on nonresident aliens) | US-MSP51-005 (superseded) to state unit |

---

## ACCESS gaps (exact URLs)
1. `https://www.acf.hhs.gov/css/form/multistate-employer-registration-form` returned HTTP 202 with an empty body (redirect to acf.gov). The Wayback `https://web.archive.org/web/2026id_/https://www.acf.hhs.gov/css/form/multistate-employer-registration-form` returned 404. The statute (US-MULTIS5-006) carries the rule; the HHS registration channel is unread.
2. `https://www.acf.hhs.gov/css/employers/employer-responsibilities/new-hire-reporting` returned HTTP 202, empty.
3. `https://www.congress.gov/bill/119th-congress/senate-bill/1443/all-actions` returned 403. The bill status rests on govinfo (introduced version only).
4. `https://wdr.doleta.gov/directives/attach/UIPL20-04.pdf`: connection failed (curl 000). The Wayback `2026id_` copy returned 404. Used the dol.gov HTML (`/sites/dolgov/files/ETA/advisories/UIPL/2004/UIPL20-04.html`); Attachment I (examples) is not held.
5. `https://app.leg.wa.gov/RCW/default.aspx?cite=50A.05.010`: connection failed (curl 000). Read from the Wayback 2026-04-23 copy.
6. `https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title{T}-section{N}` returned 404 for every section (URL format, not a block). Used govinfo USCODE-2024 instead.

## Open questions
- **MULTI-OQ-1 (route to the LA unit, conflict).** LA R.S. 47:248 30-day mobile workforce exemption from 2026-01-01 [US-MULTIS5-021]. US-LAP51-001 is silent and the superseded US-LAP51-004 said "no de minimis rule". The LA part-5 answer (US-MQ-38) needs the threshold added. What would close it: the LA unit adds the rule; the Louisiana Register issue adopting the LAC 61:I.1923 amendment (LDR Tax Policy and Planning Division) confirms the final regulation.
- **MULTI-OQ-2.** SUI wage-base credit for wages reported to another State, per State (only CA CUIC 930.1 proven). What would close it: each state UI law's taxable-wage definition (state units), or the DOL "Significant Provisions of State UI Laws, July 2026" [lead in US-MULTIS5-026].
- **MULTI-OQ-3.** PFML/SDI coverage of multistate workers in CA, NJ, NY, RI, MA, CT, OR, CO, DE, MD, ME, MN, VT (only WA proven to follow localization). What would close it: each programme's coverage definition (state units).
- **MULTI-OQ-4.** Paid-sick-leave coverage thresholds for employees working partly in a State. Per-State statutes (state units).
- **MULTI-OQ-5.** Arkansas repeal of the convenience rule (SB 484 of 2021): only tier-B leads. What would close it: the Arkansas Act text on arkleg.gov. Low impact: the DFA guide already sources by place of performance.
- **MULTI-OQ-6.** The HHS/OCSS multistate new-hire employer registration channel (form/portal). What would close it: a browser read of the ACF page (orchestrator's Chrome pass).
- **MULTI-OQ-7.** The NY convenience-of-employer rule's live litigation status was not swept. What would close it: the NY DTF/Tax Appeals Tribunal decisions list for 2026.
- **MULTI-OQ-8.** Pay-statement reach rules outside CA (e.g. NY, IL) for remote employees. Per-State; default is the work-location State.
