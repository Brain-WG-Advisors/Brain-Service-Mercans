# Belgium CCG - Content Review Log
Independent verification against primary/credible sources, module by module. Started 12 Aug 2026, in response to a request for genuine per-artifact review rather than reliance on the parallel session's self-reported "Gate 1" verification. Target: 97% accuracy floor, given Belgium's complexity (3 official languages with nullity sanctions in two regions, federal/regional/communal tax layering, an active unresolved EU law question).

Method: recompute every worked example by hand from its own stated inputs first (catches internal-consistency errors); then check the inputs themselves against external primary or credible secondary sources (catches wrong-fact errors, which internal consistency cannot catch on its own).

---

## Module 6 - Income Tax Withholding System

### Verified correct
| Item | Finding |
|---|---|
| Arithmetic of all 3 worked examples (resident EUR 4,000/mo; +2 dependants; non-resident scale III; EUR 6,000 bonus) | Recomputed by hand from stated inputs. Every step matches exactly, including the two-dependants variant (EUR 116.59/month saving) and the special SS contribution step-up in the bonus example. |
| Basic tax-free allowance EUR 11,180 (income year 2026 / assessment year 2027) | Confirmed - Liantis (Belgian payroll/HR services provider), specifically for assessment year 2027. Multiple other secondary sources gave inconsistent figures (10,570 / 10,910 / 11,170) because they conflated assessment-year 2026 (income year 2025) with assessment-year 2027 (income year 2026) - the CCG's own "income year 2026, assessment year 2027" framing is the correct one and matches the one source that addressed that specific year. |
| Lump-sum professional expense cap EUR 6,070 | Confirmed - source cites SPF Finances / Moniteur belge 29 Dec 2025 directly. |
| 7%-notional-surcharge mechanism (25/40/45/50% -> 26.75/42.80/48.15/53.50%) | Confirmed independently, same mechanism and same 4 numbers explained by an unrelated source. |
| 13.07% employee social security contribution | High confidence (stable rate, unchanged for years). |
| Top bracket threshold EUR 51,070 | Plausible via indexation cross-check: assessment-year-2026 top bracket was EUR 49,840; 49,840 x ~1.0247 = ~51,070, consistent with the ~2.4% indexation coefficient cited by an independent source. Not a direct confirmation of this exact figure, but strong circumstantial support. |
| Chefquet, Case C-119/24 (12 March 2026, Art. 45 TFEU, fixed 7% non-resident levy) | Confirmed via 8+ independent sources (Deloitte, KPMG, RSM, Bloomberg Tax, Vialto, Taxpatria, Vandelanotte, Arletti) in an earlier review pass. |

### RETRACTED - this was MY error, not a document defect
| Item | What I claimed | What actually happened |
|---|---|---|
| Inbound-taxpayer regime - percentage cap | I claimed "35%" was wrong and should be "30%", based on two Nov/Dec-2025 sources (Moore, Attentia) | WRONG. Two LATER and MORE AUTHORITATIVE sources (Claeys & Engels, April 2026; Andersen, May 2026), both citing the official Circulaire fiscale n 2026/C/51 (1 April 2026), confirm the law DID raise the percentage from 30% to 35%. The Nov/Dec 2025 sources were written before this clarifying circular existed. The CCG's original "35%" was correct across every module it appears in (2, 6, 7, 11). I edited Module 6's .md to "30%" based on the incomplete earlier finding; this has been reverted using the pre-edit backup. No other module or the .docx was touched, so the error never propagated beyond this one file, and it is now fully corrected. |

### Confirmed correct (round 2, this same research pass)
| Item | Finding |
|---|---|
| Existing-contract retroactive-alignment deadline, 30 June 2026 (appears in Module 7 and Module 11) | CONFIRMED - both Claeys & Engels and Andersen, independently, citing the same 1 April 2026 circular, give this exact date (3 months from the circular's publication). |
| Minimum salary "nil for inbound researchers" (Module 2) | CONFIRMED independently by a separate source found in an earlier pass. |

### Downgraded to genuinely unresolved - DO NOT EDIT until resolved with a primary source
| Item | Why this is now unresolved rather than a confirmed omission |
|---|---|
| Inbound-taxpayer regime - fiscal vs. social-security (ONSS) alignment | Originally flagged as a confirmed omission (fiscal cap removed, ONSS cap NOT removed - based on Moore/Attentia/propay, all Nov-Dec 2025). A later source (Andersen, May 2026, citing the same 1 April 2026 circular) states the opposite: cost reimbursements under this regime "remain exempt from social contributions, even with the percentage increase and the cap removal." These may be reconcilable (the EUR 90,000 figure might have been an ONSS administrative tolerance for automatic acceptance, not a hard legal cap on the exemption itself - genuine reimbursement of an employer's own costs is not "remuneration" under general Belgian social security principles regardless of amount) - but this is my own speculation, not a confirmation. Given I have now gotten this specific topic wrong once already in this review, no edit will be made to any module (2, 5, 6, 7, 11) on this point until the actual circular text or ONSS's current published guidance is read directly. Flagging, not fixing.

### Flagged - not yet independently verified (checking now)
| Item | What the CCG states | Status |
|---|---|---|
| Special social security contribution formula bands (e.g. "82.05 + 3.38% x 789.00" for a EUR 12,000 quarterly wage; "118.83 + 1.10% x (18,000-12,300)" for EUR 18,000) | Used in Examples 1 and 3 | Checking now |
| Exceptional-payment withholding table bands (0.00% up to EUR 10,675.00; 51.48% for the EUR 45,860.01-59,900.00 band) | Used in Example 3 (bonus) | Checking now |
| Corrective-filing deadlines for income year 2025 (15 May 2026 exemption corrections; 10 July 2026 other corrections; Finprof channel closing 31 August 2026) | Stated in the refund-procedure table | Checking now |
| Chefquet legislative-status detail (Council of Ministers approval 18 July 2026, before the Council of State, not yet enacted) | Stated in the withholding tables note | Already flagged once as unconfirmed either way; not re-checked this pass |

---

## Module 5 - Social Security & Pension Systems

### Verified correct
| Item | Finding |
|---|---|
| Employee contribution breakdown (7.50+3.55+1.15+0.87 = 13.07%) | Recomputed by hand - exact match. |
| Wijninckx contribution, 3% -> 12.5% for contribution year 2026 | CONFIRMED - 6 independent sources including INASTI (official self-employed social security institute) and Claeys & Engels citing the law directly (Loi du 18 decembre 2025, articles 146 et seq., M.B. 30.12.2025). |
| Special social security contribution - full quarterly band table | CONFIRMED by internal cross-check: reproduces Module 6's two worked examples exactly (EUR 12,000/quarter -> 82.05 + 3.38% x 789.00; EUR 18,000/quarter -> 118.83 + 1.10% x 5,700.00), and the band boundaries match fragments independently found via web search earlier in this review. This was the item that had been open since the Module 6 review - resolved by reading Module 5's own content, no external fetch needed after all. |
| Special SS contribution annual maximum (EUR 182.82/quarter x 4 = EUR 731.28/year) | Arithmetic confirmed; EUR 731.28 also independently matches an external source found earlier (Trigone Conseil). |
| GMMI indexation step (EUR 2,189.81 -> EUR 2,233.61, exactly the 2% pivot-index step) | Recomputed - exact match. |
| CO2 contribution indexation coefficient (1.6291 = Sept-2025 health index 185.85 / Sept-2004 health index 114.08) | Recomputed - exact match. |

### Fixed - confirmed defect corrected in both .md and .docx
| Item | Before | After | Why |
|---|---|---|---|
| Special SS contribution phase-out sentence | "the rate applying to the lowest band was reduced from 9% in 2026" | Rewritten to state a phase-out reform is confirmed underway, WITHOUT asserting a specific "from X%" figure that could not be independently reconfirmed in this pass | No "9%" appears anywhere in the module's own band table (rates are 4.22% / 1.10% / 3.38% / 1.10%), and the sentence never said what it was reduced TO. Rather than guess a specific replacement figure from memory of an earlier search (risking a repeat of the 35%/30% error), the sentence was rewritten to state only what is confirmed (a reform exists) and to flag explicitly that the exact phase-in numbers need a primary-source check before the WTC build relies on them. |

### Inconclusive - explicitly not concluding either way (lesson applied from the 35%/30% error)
| Item | What was found |
|---|---|
| High-wage employer-contribution exemption threshold (CCG states EUR 86,700 from 1 Jan 2026, EUR 88,434 from 1 July 2026) | One source (blog.degandpartners.com, Nov 2025 - BEFORE the 18 Dec 2025 law) gives a different figure: EUR 85,000/quarter. A second, more targeted search for a later confirmation returned no relevant Belgian results. Given the demonstrated risk of trusting pre-law-passage sources (see the 35%/30% retraction above), this is left OPEN rather than corrected - the CCG's figure is not confirmed, but nor is it confirmed wrong. |

### Flagged - not yet independently verified (documented, not searched this pass)
| Item |
|---|
| Wage moderation contribution parameters (5.67% of wage + 5.67% of employer contributions, capped at 7.48%; reduced 4.27%, max 5.12%, for tax-shift categories) |
| Social work bonus limits (lower wage limit EUR 2,880.32 -> EUR 2,937.93; upper limit EUR 3,336.98 -> EUR 3,403.62; maximum monthly reduction EUR 127.54 / EUR 137.74) |

**Module 5 status: substantively closed.** 1 defect fixed, 6 items confirmed, 1 item genuinely inconclusive (documented as such, not resolved either way), 2 items queued for a future pass if needed.

## Module 7 - Deductions, Exemptions & Benefits

### Verified correct
| Item | Finding |
|---|---|
| Company car CO2 reference values 2026: 70 g/km petrol/LPG/NG, 58 g/km diesel | CONFIRMED - SPF Finances (fin.belgium.be) directly, corroborated by 5 more independent sources (Securex, UCM, myfid, Van Mossel, monbudget-auto). |
| Fiscal work bonus 2026 ceiling EUR 765 | CONFIRMED - 5 independent sources (Liantis, Acerta, Securex, aide-sociale.be, forumforthefuture), consistent 570 (2024) -> 710 (2025) -> 765 (2026) progression. |
| Garnishment worked example (EUR 2,100 net, 1 dependent child) | Recomputed by hand - every step matches exactly, including the band-shift-by-88 logic and the final EUR 304.20 attachable / EUR 1,795.80 paid. |
| Company car worked example (post-fix) | Now shows the corrected EUR 3,214.80 / EUR 267.90 - matches the fix applied in this session. |
| All previously-confirmed cross-module figures (30%/EUR 6,070 expenses; EUR 11,180 allowance; 13.07%; CBA90 ceilings; bicycle/homeworking allowances; flexi-job 28%; 1.6291 index; special SS contribution bands) | Reappear here in full context, no contradiction. |

### Directionally correct, specific detail NOT confirmed - flag, do not treat as settled
| Item | What was found |
|---|---|
| Fiscal work bonus phase-in 2027-2029 (rising to EUR 2,000/year; percentage 52.54% -> 63% -> 72%) | The 2026 figure (EUR 765) is solid, but a March-2026 source states explicitly the planned reinforcement "was not yet definitively adopted by the Chamber" as of that date, and describes the goal more loosely (reinforcement from 2028, gross=net target by 2029) than the CCG's precise schedule. Not confirmed as enacted law with these exact numbers. |

### Flagged - not yet independently verified (documented, lower priority given time)
| Item |
|---|
| CO2 solidarity contribution constants (F = 768 petrol / 600 diesel / 990 LPG) and the 2.75 multiplier for vehicles ordered from 1 July 2023 |
| Flexi-job wage tax exemption ceiling EUR 18,440 for income year 2026 |
| Inbound taxpayer eligibility specifics (60-month non-residency lookback; 150 km border-distance test) - plausible, matches known regime shape, not independently re-checked this pass |
| CO2 solidarity contribution minimum monthly floors (EUR 33.93 pre-July-2023 vehicles / EUR 42.34 from July 2023) |
| Garnishment dependent-child resource thresholds (EUR 4,015 cohabiting / EUR 5,799 single parent / EUR 7,352 disabled child) |

**Module 7 status: substantively reviewed.** 5 items/clusters confirmed (including 2 full worked-example recomputations), 1 item downgraded to "directional, not confirmed in detail," 5 items queued as flagged/unverified.

---

## Module 4 - Gross Compensation

### Verified correct - independent calendar-date recomputation (new verification technique this pass)
| Item | Finding |
|---|---|
| Proration Example 1: March 2026 has 22 working days; 16-31 March has 12 working days | INDEPENDENTLY CONFIRMED by direct day-of-week calculation from the conversation's anchor date (13 Aug 2026 = Thursday). 1 March 2026 = Sunday; no Belgian public holiday falls in March 2026. Both weekday counts verified by hand, matching exactly. |
| Proration Example 1 arithmetic (12/22=0.545455; 3,600 x factor=1,963.64; SS=256.65; taxable base=1,706.99) | Recomputed - exact match on every step. |
| Proration Example 2: 17 April 2026 is a Friday; April 2026 has 21 working days excluding Easter Monday (6 April); 13 working days from 1-17 April including Easter Monday | INDEPENDENTLY CONFIRMED - 1 April 2026 = Wednesday (verified via the same anchor-date calculation); Easter Monday 2026 = 6 April is consistent with Easter Sunday 2026 = 5 April. Weekday counts verified by hand (22 total weekdays in April minus 1 holiday = 21; 13 weekdays from 1-17 April). |
| Proration Example 2 arithmetic (13/21=0.619048; 3,600 x factor=2,228.57) | Recomputed - exact match. |
| Voluntary overtime scheme (360-hour quota from 1 April 2026, first 240 hours net/exempt, remaining 120 with supplement) | CONFIRMED internally consistent - 240+120=360, and this matches the scope_manifest.json's original scoping note from the very start of the Belgium build, now the THIRD independent internal confirmation point (scope_manifest + Module 4 + Module 7's exempt-income table). |
| Overtime tax relief percentages (66.81%/57.75% employee; 41.25%/32.19% employer) | Reappears identically from Module 7 - now cross-confirmed across 2 modules. |
| GMMI April->August indexation step (2,189.81 -> 2,233.61, exact 2% pivot step) | Already externally confirmed in the Module 5 review; reappears consistently here. |
| Exceptional-payment withholding table (11 bands, 0%-53.50%) and CBA90 ceilings (EUR 4,255/3,701, 33%/13.07%) | Reappear identically from Modules 6/7/9(fast-extraction); fully consistent, no new verification needed. |

### New internal-consistency finding (not previously noticed)
Module 4 states ordinary (non-departure) double holiday pay = 92% of monthly gross for a full service year. Module 8/9's DEPARTURE holiday pay formula states 7.67% of annual gross for the double-holiday-pay component. 7.67% x 12 = 92.04%, matching Module 4's 92% almost exactly. Two independently-stated figures, computed on different bases (annual-gross-percentage vs monthly-multiple), converge - strong internal corroboration even without an external source for either figure individually.

### Flagged - not yet independently verified (low priority - not "new 2026 change" claims or not feeding a shown calculation)
| Item |
|---|
| GMMI 1 January 2026 baseline, EUR 2,154.11 ("carried over from 2025" - not a new figure, lower risk) |
| Joint committee 200 sectoral indexation of 2.21% on 1 January 2026 (specific, single mention, does not feed any worked example shown) |

**Module 4 status: substantively reviewed.** Zero new errors found - the cleanest module reviewed so far. 8 items/clusters confirmed (including 2 full worked examples verified via independent calendar-date computation, a first for this review), 1 new cross-module consistency finding, 2 items flagged as low-priority/unverified.

---

## Module 9 - Termination & Irregular Payments

### Verified correct
| Item | Finding |
|---|---|
| Notice indemnity calculation, Steps 1-6 (39 weeks; EUR 67,778.40 annual base; EUR 50,833.80 indemnity; EUR 5,213.72 outplacement deduction; EUR 45,620.08 net indemnity; EUR 5,962.54 SS; EUR 21,216.78 withholding at 53.50%) | Recomputed by hand and via Python - every step matches exactly. |
| Notice period reform (52-week cap from 17 years' seniority from 1 June 2026; uniform 1-week notice in first 6 months from 1 August 2026) | CONFIRMED internally consistent - matches the scope_manifest.json's original scoping note, now the FOURTH independent internal confirmation point across this whole review. |
| Bonus worked example, Parts A-D in full (ordinary bonus EUR 5,000 vs CBA90 bonus EUR 3,500, including the EUR 0.65/EUR 0.37 net-per-employer-cost comparison) | Recomputed via Python - every single step matches exactly, no discrepancy anywhere in either part. |
| Outplacement floor/ceiling (EUR 1,800/EUR 5,500) and the 4-week deduction mechanism | Already externally confirmed in the Module 7 review; reused correctly here. |

### Fixed - confirmed defect corrected in both .md and .docx
| Item | Before | After | Why |
|---|---|---|---|
| Departure holiday pay withholding bracket (double-holiday-pay portion) | "7.67% single at 53.50%, 7.67% double at 47.44%" -> total withholding EUR 1,213.60 | "53.50% for both halves" -> total withholding EUR 1,284.17 (cascading to Step 8 summary: net EUR 1,116.14, and the Total row: withholding EUR 24,201.73 / net EUR 23,071.92) | The reference annual remuneration (EUR 62,640) exceeds EUR 59,900 in BOTH the exceptional-payment table AND the holiday-pay table - both tables' top band is 53.50%. The 47.44% figure is the SECOND-highest band (45,860.01-59,900.00), which does not apply once the reference exceeds 59,900. Confirmed by direct Python recomputation testing multiple hypotheses; this was a genuine bracket-selection error, not a rounding issue (the rounding-level gap, using the document's own wrong percentage, was only ~EUR 2). |

### Fixed - confirmed defect corrected in both .md and .docx (resolved via dedicated investigation)
| Item | Before | After | Why |
|---|---|---|---|
| April salary withholding | EUR 1,003.36 (net EUR 2,908.49; Total withholding EUR 24,201.73 / net EUR 23,071.92) | EUR 1,155.96 (net EUR 2,755.89; Total withholding EUR 24,354.33 / net EUR 22,919.32) | A dedicated investigation (Decimal-precision engine, validated against Module 6's own EUR 4,000 reference example before use) confirmed 1,003.36 was wrong under every tested method, including a systematic 648,000-combination grid search (the 6 "exact matches" found were shown to be statistically below the expected noise floor for that search space, not a real signal). Stale prior-year parameters were ruled out on DIRECTION - every historical year's parameters are LESS generous than 2026's, so an old-year error would move the figure UP, not down toward the target. The remaining judgement call - whether the EUR 250 monthly company car benefit belongs in this line's taxable base - was resolved by direct application of Module 6's own documented rule (benefits in kind enter the taxable base monthly, in the month enjoyed) plus the fact the employee's car was available through 30 April: EUR 1,155.96 is the value under this CCG's own rules, not the more conservative EUR 1,035.58 alternative. |

**Process note:** the first attempt to apply this fix in the .docx used an insufficiently specific match ("Ordinary scale" as a bare string) and wrote the explanatory note onto two UNRELATED rows elsewhere in Module 9 (a generic "salary for notice period worked" reference row, and a "company car returned late" reference row) before being caught and reverted. Both were confirmed and reverted to their original "Ordinary" text; only the genuine April-salary row was corrected. Lesson: a bare-string match against a common short label ("Ordinary scale") is unsafe even when scoped to a stage/table search zone - always verify a full-row context includes the specific facts identifying the intended row before writing, not just the target substring.

**Module 9 status: substantively reviewed, one item still genuinely open.** 4 items/clusters confirmed (including 2 full worked examples fully recomputed via Python with zero discrepancy), 1 confirmed defect fixed with a well-derived correction, 1 confirmed defect with the correct replacement value still undetermined.

---

## Module 1 - Foundational Jurisdictional Parameters

### Verified correct - independent calendar-date recomputation
| Item | Finding |
|---|---|
| All 10 statutory public holidays for 2026, with their stated weekdays | INDEPENDENTLY CONFIRMED, 10/10, via direct day-of-year/day-of-week calculation from the conversation's anchor date (13 Aug 2026 = Thursday, day 225 of the year). Two of the ten (Ascension Day = always Thursday, Whit Monday = always Monday, both fixed by their liturgical definition relative to Easter Sunday) carry an additional structural confirmation independent of the date arithmetic. |
| Identification of which 2026 holidays fall on a non-working day (Assumption, 15 Aug = Saturday; All Saints, 1 Nov = Sunday) needing a replacement day | CONFIRMED correct - matches exactly the two dates independently found to fall on a weekend among the ten. |
| Article 412 quarterly-filing threshold EUR 50,240 | Already externally confirmed (FPS Finance direct) earlier in this review; reappears consistently. |
| Language-of-documents framework (Decree 19 July 1973 Flanders; Decree 30 June 1982 Wallonia; coordinated laws 18 July 1966 Brussels) | CONFIRMED internally consistent - matches BE-COVERAGE.md's original scope charter verbatim, written before any CCG module existed. |
| DmfA quarterly deadlines (30 April / 31 July / 31 October / 31 January) | Verified internally consistent - each is genuinely the last calendar day of the month following its respective quarter. |

### Flagged - not yet independently verified (low priority)
| Item |
|---|
| Community-day dates (11 July Flemish; 27 September French; 15 November German-speaking/King's Feast) - explicitly stated as non-statutory for private-sector employees, so low risk even if unverified |
| Administrative deadline for fixing a replacement day (before 15 December 2025) - single mention, not independently checked |

**Module 1 status: substantively reviewed. Zero errors found** - the second module in a row (after Module 4) where an exhaustive independent recomputation (this time of every single statutory date in the calendar table, not just two worked examples) turned up no discrepancy at all.

---

## Module 2 - Master Data Configuration

### Fixed - confirmed defect corrected in both .md and .docx
| Item | Before | After | Why |
|---|---|---|---|
| INSZ sample value | 86.04.12-345.67 | 86.04.12-345.62 | The check-digit ALGORITHM stated two subsections earlier in this same module (check = 97 - (first nine digits mod 97), for a pre-2000 birth date) is correct and matches known Belgian national-register-number structure. Verified by direct Python computation: for the sample's own birth date (12 April 1986) and sequence number (345), the correct check digits are 62, not 67. The formula itself was right; the illustrative sample given alongside it was simply never validated against that formula. A developer testing a check-digit validator against this exact fixture would see their correct implementation "fail" against an invalid reference value. |

### Verified correct
| Item | Finding |
|---|---|
| INSZ/BIS check-digit formula and BIS month-shift logic (+20 unknown gender, +40 known gender) | The formula description matches known Belgian INSZ structure; the BIS month-shift was sanity-checked arithmetically (no overflow past a 2-digit field even for December + 40). |
| Reappearing figures (inbound-taxpayer 35%, double holiday pay 92%, meal voucher EUR 10.00/8.91/1.09) | Consistent with prior modules' already-confirmed findings; no new verification needed. |

### Flagged - not yet independently verified (low priority)
| Item |
|---|
| Enterprise number (KBO/BCE) and NSSO employer number check-digit formulas - structurally plausible (same mod-97 family as INSZ) but no sample value given to test against, and not independently sourced this pass |
| Document retention periods (5 years social documents; 7 years tax documents) - administrative, does not feed a calculation, not independently searched |

**Module 2 status: substantively reviewed.** 1 defect fixed (a self-inconsistent illustrative sample, not an algorithm error), 2 items/clusters confirmed, 2 items flagged low-priority/unverified.

---


## Module 3 - The Gross-to-Net Calculation Framework

### Verified correct - structural/logical consistency (this module introduces no new figures)
| Item | Finding |
|---|---|
| Overall G2N step ordering (SS before taxable base; taxable base before withholding; special SS contribution after withholding; post-tax deductions last) | CONFIRMED consistent with every worked example already verified in Modules 6, 7, 9, and 12 - SS is deducted before the taxable base is formed in every single instance checked across this whole review, with zero exceptions found. |
| The explicit statement that reversing steps 2 and 4 would change the result | Logically correct and independently verifiable - confirmed true in every worked example (SS is always subtracted before annualisation, never after). |
| G2N algebraic summary (A-G lines) | Structurally consistent with Module 6's own formula; not exhaustively re-verified against every prior worked example's exact G (net pay) figure, but no contradiction found. |
| All reused figures (13.07%, EUR 137.74/127.54, EUR 6,070, EUR 182.82, EUR 1.09, EUR 86,700/88,434, 8.86%/4.4%, ~92%/one-month provisions) | Already independently confirmed in prior modules; consistent here. |

### Worth noting - condensed summary omits a nuance stated fully elsewhere (not treated as a defect)
Step 6's deduction list ("wage assignments and garnishments, within the protected-earnings bands of Article 1409") does not separately call out maintenance/child-support debts, which Module 7 and Module 9's worked example both establish explicitly as the ONE category NOT subject to those protected bands (attachable in full, ranking ahead of all other creditors). Read in isolation, Module 3's summary could mislead a reader into assuming maintenance debts follow the same bands as ordinary garnishments - they do not, per the more detailed modules. This reads as an intentional simplification consistent with this CCG's established pattern of condensed overview modules deferring full detail to specialist modules, rather than a contradiction - flagged for awareness, not scored as a fix.

**Module 3 status: substantively reviewed. Zero numeric errors** - this module introduces no new figures requiring external verification; its value was in confirming the STRUCTURAL logic of the whole framework against everything already independently checked in Modules 4-9 and 12.

---

## Module 8 - Statutory Leave Management

### Verified correct - full worked-example recomputation
| Item | Finding |
|---|---|
| Double holiday pay worked example (EUR 3,600/month, gross 3,312.00 -> SS 432.88 -> taxable 2,879.12 -> reference 43,200.00, band 42.39% -> withholding 1,220.46 -> net 1,658.66) | Recomputed via Python - every single step matches exactly, zero discrepancy. |
| Departure holiday pay worked example (EUR 21,600 gross -> 3,313.44 total, split 1,656.72/1,656.72) | Recomputed - exact match on every figure. |

### Verified correct - external primary/credible sources
| Item | Finding |
|---|---|
| Sick-leave relapse period extended from 14 days to 8 weeks, effective 1 January 2026 | CONFIRMED - 9 independent sources (Group S, Acerta, Securex x2, Semafor, CESI, Neoviaq, Solidaris x2, Dynamik HR), unanimous on both the change and the effective date. |
| 20-week limit on neutralising guaranteed salary during progressive work resumption - removed from 1 January 2026 | CONFIRMED via the same search (Dynamik HR, CESI). |
| Blue-collar guaranteed-salary percentages for days 15-30 (25.88% / 85.88%) | CONFIRMED - exact match against an independent source (Semafor) citing the identical two figures. |

### Fixed - citation correction (not a factual error, a legal-basis attribution correction)
| Item | Before | After | Why |
|---|---|---|---|
| Legal basis for the 2026 relapse-period/progressive-resumption reform | Attributed only generically to "measures effective 1 January 2026," alongside a citation to "Law of 17 July 2023 on annual leave and sickness during leave" (a genuinely different, earlier reform) | Named citation added: "Law of 19 December 2025 implementing a reinforced return-to-work policy for incapacity for work" | The substantive facts (14 days -> 8 weeks; 20-week limit removed) were already correct - only the legal source was imprecisely attributed. Securex specifically names this law as the source of the 2026 relapse-period change, distinct from the 2023 law about sickness during annual leave (a separate, earlier reform, already correctly described elsewhere in this same module). Note: this fix's mechanism produced an unexplained result - both the .docx and .md fix scripts reported "0 replacements made," yet direct re-inspection of both files afterward confirmed the correct citation was present in both. The end state is verified correct in both files; the discrepancy between the script's own log and the actual result was not fully explained (similar to an earlier unexplained event in the Module 9 review) but does not change the confirmed-correct outcome. |

**Module 8 status: substantively reviewed.** 2 full worked examples verified with zero discrepancy, 3 external confirmations from strong multi-source research, 1 citation-precision fix applied and confirmed in both files.

---


## Module 10 - Reporting, Compliance & Finalisation

### Fixed - confirmed omission corrected in both .md and .docx
| Item | Before | After | Why |
|---|---|---|---|
| Year-end finalisation step 9, indexed-parameter effective dates | "1 January, with the further steps at 1 March, 1 April, 1 July and 1 September 2026" | "1 January, with further steps at 1 March, 1 April, 1 July, 1 August and 1 September 2026 (1 August is the GMMI's final 2026 indexation step, confirmed in Module 4)" | 1 August 2026 is the confirmed date of the GMMI's third and final 2026 indexation step (EUR 2,189.81 -> EUR 2,233.61, the exact 2% pivot-index crossing already externally and internally confirmed in Modules 4 and 5). A configuration checklist that omits this date would miss an entire real indexation event. |

### Verified correct - structural (this module is a summary; most detail is deliberately deferred to the Report Specs)
| Item | Finding |
|---|---|
| DmfA hierarchical structure (employer -> worker -> occupation line -> remuneration/service/contribution/deduction/special-contribution blocks) | Consistent with everything established about the DmfA across every prior module - no contradiction found. |
| Filing-mechanics table (DmfA/Dimona/Finprof/Belcotax all separate, none derived from another) | Consistent with the "no netting, no derivation" principle already seen in the 281.10/monthly-withholding-returns reconciliation language used elsewhere. |
| Correction cascade description (a corrective DmfA can ripple through the special SS contribution band, the social work bonus, net pay, and the 281.10) | Logically sound and consistent with the banded, quarterly-dependent mechanics already verified in Modules 5 and 9. |
| Corrective filing deadlines for income year 2025 (15 May / 10 July / 31 August 2026) | Already externally confirmed (Securex) earlier in this review; reappears consistently. |
| Payslip mandatory-content table and the unilingual-document rule | Consistent with Module 1's language framework, already confirmed against BE-COVERAGE.md. |

**Module 10 status: substantively reviewed.** 1 confirmed omission fixed (a missing indexation date), 5 items/clusters confirmed as internally consistent with everything established in prior modules - this module introduced very few new figures, being explicitly designed as a summary deferring detail to the Report Specs.

---

## Module 11 - Advanced Scenarios & Cross-Cutting Logic

### Fixed - genuine cross-module contradiction resolved (correction applied to Module 6, not Module 11)
| Item | Before (Module 6) | After | Why |
|---|---|---|---|
| Stock option valuation for exercise periods beyond 5 years | "doubled for options over 5 years" | "increased by 1 percentage point (0.5 percentage point under the reduced 9% rate) per year or part-year of the exercise period beyond 5 years from the offer -- not doubled" | Module 6 and Module 11 stated CONTRADICTORY mechanisms for the exact same rule (Module 11 already correctly said "increased by 1 percentage point per year beyond five years"). Resolved by 8 independent sources, including the Conseil Superieur des Finances (an official Belgian government advisory body) which gives the exact confirming worked example: a 7-year option is valued at 18%+2%=20%, not 36% (which "doubled" would imply). Securex and multiple accounting/law firms independently confirm the same mechanism and additionally confirm the reduced-rate increment is 0.5 percentage points/year, not 1 - a detail neither module had stated explicitly, now added to the corrected text. Module 6 was the one in error; Module 11 required no change. |

### Verified correct - structural/logical consistency
| Item | Finding |
|---|---|
| Proration/projection table (no future-earnings projection in Belgian withholding; special SS contribution implicitly projected then trued up in month 3) | Consistent with everything established in Modules 3, 5, 6, 9. |
| Multiple-employer, non-cumulative-withholding consequences (systematic under-withholding, corrected at assessment) | Logically sound and consistent with the CCG's own repeatedly-stated non-cumulative design principle. |
| Inbound taxpayer regime table (duration 5 years, extendable by 3; 150 km border test; 60-month lookback) | Consistent with figures already established in Modules 2, 6, 7; the 5-year/+3-year duration detail is new to this module but matches known regime shape (not independently re-sourced this pass, lower priority given the core financial parameters are already extensively confirmed). |
| Mid-year entity transfer and cross-border population tables (CBA 32bis, Limosa, Regulation 883/2004 substantial-activity test) | Structurally consistent with everything established; no new figures requiring verification. |

**Module 11 status: substantively reviewed.** 1 genuine cross-module contradiction found and resolved (the most consequential finding of this module - an outright factual conflict between two modules, not just an omission or citation issue), 4 items/clusters confirmed as internally consistent.

---

## Module 12 - Gross-to-Net Worked Examples

### Fixed - last straggler from an earlier fix, missed by a formatting-pattern mismatch
| Item | Before | After | Why |
|---|---|---|---|
| Example 5, Part D, "Net of the ordinary remuneration" formula | "(3,800.00 - 496.66 - 871.60)" showing result 2,431.76 | "(3,800.00 - 496.66 - 871.58)" | This is the SAME company-car example fixed earlier in this session (Module 7/12 cascade, 267.95->267.90). That fix's search patterns used an unspaced "-871.60" (as a value prefix) and never matched this occurrence, where the same old value appears with spaces around it as a subtraction operator inside a formula (" - 871.60 "), not as a standalone negative value. The .md file had already been corrected via a different replacement in the original pass; only the .docx had this one remaining. Confirmed both files now consistent. |

### Verified correct - full recomputation, all 6 worked examples
| Example | Finding |
|---|---|
| Example 1 (full-time resident, EUR 3,500 standard salary) | Recomputed via Python/by hand - every step matches, including the full employer-cost table (6 components summing exactly to EUR 5,195.03). One sub-cent rounding note (930.60 x 48.15% computes to 448.08, document shows 448.09) that does NOT propagate to any final displayed figure once divided by 12 and rounded - not treated as a defect. |
| Example 2 (part-time, low wage, social work bonus proration) | Recomputed - every step matches exactly, including the full-time-equivalent reference-wage proration logic for the social work bonus. |
| Example 3 (personal pension contribution) | Recomputed - every step matches exactly, including the 30%-of-contribution withholding relief mechanic. |
| Example 4 (garnishment with dependent child) | Recomputed - both the tax-withholding table AND the full garnishment-band table match exactly, cascading correctly to the final net-paid-to-employee figure. |
| Example 5 (company car + double holiday pay) | Now fully corrected (see Fixed section above) - all remaining figures confirmed matching the earlier Module 7/12 fix. |
| Example 6 (blue-collar, 108% contribution base) | Recomputed - every step matches exactly, including the 108% uplift applied consistently to both the SS base and the special SS contribution's quarterly-wage-at-108% figure. |

**Module 12 status: substantively reviewed - the last of the two content modules.** All 6 worked examples independently recomputed end-to-end; only one already-known example needed a final touch-up (a straggler from an earlier fix), and one sub-cent non-propagating rounding note was documented without action. This is the strongest verification result of any module in this review: 6 complete, independent worked-example recomputations with only trivial findings.

---

## Module 13 - Common Business Practices & Non-Statutory Rules

### Verified correct - structural/logical consistency (this module is entirely qualitative; no worked examples, no new statutory figures)
| Item | Finding |
|---|---|
| All reused figures (EUR 10.00 meal voucher, 8.86% group insurance, EUR 160.99 homeworking, EUR 4,255/3,701 CBA90) | Already extensively confirmed in prior modules; consistent here, no contradiction. |
| Extra-statutory leave framework (not covered by the 15.34% departure holiday pay; not protected by annual holidays legislation; excluded from the holiday certificate) | Logically consistent with the 15.34% departure holiday pay rate and the statutory-leave framework established across Modules 8 and 9. |
| Draw/commission recovery mechanics (Article 23's one-fifth cap applying to recoverable draws) | Consistent with the same cap already verified in Modules 3, 4, 7, 9, 12. |
| Off-cycle payment period-allocation rule (DmfA period vs withholding-tax payment-date, deliberately falling in different periods) | Consistent with the same "deliberately different periods, not a reconciliation error" principle already stated in Module 10. |

### Flagged - not independently verified (low priority - common practice, not a strict statutory figure)
| Item |
|---|
| "Variable pay averaged over the 12 months preceding the dismissal" for the notice-indemnity calculation - plausible, structurally sound, not contradicted by anything else established, but not independently cross-referenced against a worked example in this review |

**Module 13 status: substantively reviewed. Zero errors found** - the second entirely-qualitative module (after Module 3) to pass with no new figures requiring correction.

---

# REVIEW COMPLETE - ALL 13 MODULES

This closes the module-by-module content review of BE-CCG-001-v1.0.docx. Summary across all 13 modules:

- **Real defects found and fixed:** 7 (company car arithmetic error M7/M12; departure-holiday-pay bracket error M9; April salary withholding error M9, resolved via dedicated investigation; special SS contribution phase-out sentence M5; INSZ sample value M2; stock option valuation contradiction M6/M11; year-end indexation date omission M10)
- **Citation-precision corrections (facts already right, source misattributed):** 1 (sick-leave relapse reform legal basis M8)
- **Items confirmed correct via external primary/credible sources:** dozens, spanning CO2 reference values, Wijninckx, outplacement caps, Article 412 threshold, fiscal work bonus, sick-leave relapse reform, and more
- **Items confirmed correct via independent recomputation (arithmetic and calendar-date):** every worked example in Modules 4, 6, 7, 8, 9, and all 6 examples in Module 12 - dozens of individual calculation chains verified to the cent
- **Items still genuinely open/inconclusive:** 1 (the EUR 86,700/88,434 high-wage exemption threshold vs a single conflicting pre-law source - explicitly left undecided rather than guessed)
- **Items flagged as unverified but low-priority:** a modest number, mostly administrative/informational figures that do not feed a calculation

No module was found completely free of at least a flagged item, but 4 modules (1, 3, 4, 13) required zero corrections after full review.

---

## RESOLUTION - High-wage exemption threshold (previously left inconclusive in Module 5)

### Fixed - reopened and resolved across all 4 modules where it appeared (1, 3, 5, 11)
| Item | Before | After | Why |
|---|---|---|---|
| High-wage employer-contribution exemption second threshold | "EUR 88,434 from 1 July 2026" (appeared in Modules 1, 3, 5 x3, 11 - 6 occurrences total) | Replaced with a note that the EUR 86,700 threshold (confirmed correct, effective 1 January 2026) is confirmed unchanged through at least mid-2026, and that the actual 1 July 2026 event is a POPULATION-SCOPE exclusion (paid athletes and professional cyclists barred from combining this measure with their sport-specific reduction, per Programme Law of 30 May 2026, Articles 109-110) - not a threshold value increase | Resolved via Dutch-language search that surfaced 7+ independent sources including TWO official government sources: the RSZ's own administrative instructions (dated 16/01/2026, confirming EUR 86,700 from 1 January 2026 due to a December 2025 index-threshold crossing) and VLAIO (a Flemish government agency). Every source found, including ones dated as late as May 2026, describes the 1 July 2026 change as the athlete/cyclist exclusion - NONE mentions any further threshold increase to EUR 88,434. This also retroactively explains the EARLIER "conflicting" EUR 85,000 source found during the Module 5 review: that was not a stale pre-law draft as originally suspected, but the genuinely correct ORIGINAL threshold (Royal Decree of 6 October 2025, in force from 1 July 2025), later indexed to EUR 86,700 from 1 January 2026 - both figures were real and correctly sequenced, just not the way the CCG had assumed. |

**Resolution note:** this closes the one item that remained genuinely open across the entire 13-module review. The CCG's original error appears to have arisen from over-applying the "mid-year 2% indexation step" pattern seen elsewhere in this CCG (e.g. the GMMI's confirmed April-to-August 2026 step) to a threshold that did not actually receive a second 2026 indexation - a plausible but incorrect inference, now corrected with a specific, sourced replacement rather than a guess.

---


## SECOND-PASS INDEPENDENT REVIEW - full-document cross-check (post v1.0 upload)

Triggered by a fresh upload of BE-CCG-001-v1_0.docx for independent re-verification. Method: instead of module-by-module sequential review, extracted every EUR figure and every percentage from the ENTIRE document at once (155 distinct EUR values, 95 distinct percentages), cross-tabulated by module, and specifically hunted for near-miss numeric pairs (values close but not identical) as typo candidates - a check the original sequential module-by-module pass could not perform, since it only compared values when a fact happened to be noticed reappearing across 2-3 modules at a time.

### Fixed - genuine .md/.docx desync found and closed
| Item | Finding |
|---|---|
| Module 12 Example 5 profile sentence, company car benefit figure | The .md source was ALREADY correct ("EUR 267.90") from an earlier fix pass this session. The .docx had silently reverted to or never received the same correction, still showing "EUR 267.95" in the profile sentence specifically (the calculation table cell in the same .docx WAS correctly showing 267.90 - only the introductory profile sentence had the stale figure). This is a genuine .md-vs-.docx desync, invisible to any check that only inspects one file at a time. Fixed in the .docx; .md required no change. |

### Verified correct - newly checked, not covered by the original 13-module sequential pass
| Item | Finding |
|---|---|
| Special social security contribution, joint-assessment-with-working-spouse sub-rule (Module 5): minimum EUR 15.45/quarter from EUR 3,285.29; band EUR 43.32 + 1.10% above EUR 6,570.54; maximum EUR 154.92/quarter | CONFIRMED via the official Belgian social security administration's own site (socialsecurity.be, DmfA instructions) - exact match on all four constants. This entire sub-scenario had not been touched during the original 13-module review, which focused on the "individually assessed" case throughout. |
| Module 6 figures EUR 249.22 (= EUR 2,990.65 / 12, the monthly-equivalent tax-free allowance reduction) and EUR 181.53 (full multi-step special-SS-contribution recomputation: 118.83 + 1.10% x 5,700 = 181.53, vs 108.72 without a bonus, difference 72.81) | Both independently recomputed from scratch - exact match on every step. |
| All 7 of today's earlier fixes (car benefit, stock option valuation, April salary, INSZ sample, SS phase-out sentence, M10 indexation date, high-wage threshold) | Directly confirmed present and correct in the freshly uploaded file via targeted marker search across the whole document. |
| Comprehensive EUR and percentage near-miss sweep (all values within EUR 5 or 0.5 percentage points of each other, regardless of which module) | Every near-miss pair checked resolved to either a legitimate boundary convention (X.00/X.01 band edges) or a genuinely different, unrelated statutory concept that happens to be numerically close by coincidence. No additional errors found beyond the one fixed above. |

**Second-pass status: complete.** One genuine cross-file desync found and closed (a category of defect the sequential module-by-module method could not have caught), one previously-unreviewed sub-scenario confirmed correct via an official primary source, two more figures confirmed via recomputation, and a comprehensive whole-document numeric consistency sweep found nothing further. One item remains honestly unresolved: the H3 heading count (158) does not match the "136" figure recorded early in this session as the post-Gate-1-correction count - the discrepancy's cause was not determined and is flagged for awareness, not treated as a defect given no other evidence supports the document being an outdated version.

---

## SYSTEMATIC SWEEP - re-checking items previously left "flagged, text unchanged"

Triggered by discovering that the fiscal-work-bonus phase-in item (Module 7) had been logged as
uncertain but the CCG TEXT ITSELF was never edited to carry that caveat - meaning the WTC-building
agent, instructed to trust the CCG as authoritative, inherited the unflagged claim as if settled.
This sweep re-checked every other item left in the same "flagged, text unchanged" state.

### Fixed - the triggering item
| Item | Fix |
|---|---|
| Fiscal work bonus 2027-2029 phase-in (Module 7) | CCG (.md+.docx) AND WTC (Tax Credit sheet) both edited to state the reform is planned but not confirmed enacted, per the March-2026 source already found earlier - previously only logged, now in the actual text of both artifacts |

### Confirmed correct - all 5 originally-flagged items, no text change needed
| Item | Source |
|---|---|
| Wage moderation contribution (5.67%/7.48%/4.27%/5.12%) | ONSS official instructions (socialsecurity.be) + SPF Emploi, two independent official government sources, exact match on all four figures |
| CO2 solidarity contribution constants (F=768/600/990) | ONSS official instructions directly, plus 8 more independent sources (Securex, Acerta, Agoria, FLEET, Van Mossel, Dynamik, Cellule Mobilite) |
| CO2 solidarity minimum floors (EUR 33.93/42.34) | Same source cluster - consistent across all sources checked |
| Garnishment dependent-child resource thresholds (EUR 4,015/5,799/7,352) | Attentia, citing the exact same Royal Decree (3 Dec 2025) already cited in the CCG - exact match on all three figures |
| Variable pay averaged over 12 months preceding dismissal | Securex, directly on point for Belgian notice indemnity calculation |

### New defect found during this sweep (not one of the original 5 - surfaced incidentally)
| Item | Before | After | Why |
|---|---|---|---|
| CO2 solidarity contribution multiplier for vehicles ordered from 1 July 2023 | "2.75 for 2026" | "4 for 2026" | While confirming the F-constants, 4 independent sources (Agoria, Cellule Mobilite, Van Mossel, Dynamik HR) all state the 2026 multiplier is x4, not 2.75. This figure had been carried forward from the CCG's original fast-extraction content into the WTC-building prompt's "verified reference values" list WITHOUT ever being independently checked at the time - the same failure pattern as the high-wage threshold and stock-option errors found earlier in this review. Fixed in the CCG (.md+.docx) AND the WTC, since the WTC had independently inherited the same figure by reading the CCG directly as instructed. |

**Process lesson, stated explicitly for future reference:** a finding logged as "flagged/inconclusive" in a review log is NOT equivalent to the artifact's own text carrying that caveat. Anything that reads the artifact directly (a downstream build agent, a developer, a reviewer) will not see the review log unless separately pointed to it, and will treat unflagged text as settled fact. From this point forward, any item left genuinely unresolved must be written INTO the artifact's own text (as a stated caveat), not only logged externally.


---

## MAJOR TAX-ENGINE CORRECTION - triggered by request to verify against primary legislation

Triggered by Wallisson asking whether the whole review was grounded in actual statutes, not
secondary sources. Attempting genuine primary-source verification (Moniteur Belge / ejustice.just.fgov.be)
surfaced a real, previously undetected discrepancy in the single most load-bearing figure in the
entire CCG - the basic tax-free allowance - which cascaded into four dedicated investigations and
a comprehensive fix.

### Chain of discovery
1. Basic allowance: EUR 11,180 (used everywhere) is neither the withholding figure (11,170) nor the
   assessment figure (11,550) - it is a superseded pre-reform counterfactual that never became law.
2. Dependent-child supplements: the CCG's entire MECHANISM was wrong (treated as an addition to the
   allowance; Annex III actually applies a separate flat euro reduction after tax is computed), not
   just stale numbers - confirmed via direct reading of the machine-readable Annex III text.
3. Withholding bracket ceilings: the CCG used the ANNUAL ASSESSMENT brackets (16,720/29,510/51,070)
   inside the MONTHLY WITHHOLDING formula throughout - Annex III's own ceilings are 16,710/29,500/51,050,
   a systematic but separate rounding convention. Confirmed against the actual annex text, all four bands.
4. Reference-remuneration factor (12 vs 13.92): confirmed via Securex's own dedicated severance-pay
   article to be a genuinely DISPUTED area of Belgian tax practice, not a simple error - resolved by
   adopting 13.92 as Mercans' standardized convention (fewer examples to change, matches majority practice).
5. Module 9's notice-indemnity example used the WRONG TABLE ENTIRELY (nr. 53 general exceptional-payment
   table, 53.50%) instead of the correct severance-specific table (nr. 58, routed via nr. 62), a EUR
   5,766.20 over-withholding on one example - confirmed via multiple independent primary-annex-text
   fragments across several years' editions.
6. A pre-existing, unrelated .md/.docx desync on the inbound-taxpayer regime (the .docx correctly held
   35%/reform details from an earlier session; the .md still held a retracted 30% figure) was discovered
   as a side effect of the fix-application agent's diff-before-mirroring discipline, and merged (both
   files now carry the complete, correct content neither had alone).

### Fix applied and independently verified
An independent Decimal-based recomputation engine was built by the fix-application agent, first
validated by reproducing every PRE-fix CCG figure exactly from the old parameters (proving the engine
itself was correct), then used to verify every POST-fix figure against the investigations' own
pre-computed values - full agreement, no discrepancy. 59 figures changed across 5 CCG modules, the
.docx, and 3 WTC-generation scripts (so a future WTC rebuild will not silently regenerate the old
wrong figures).

### Explicitly NOT fixed - flagged for a future, separate pass
- A newly-found EUR 0.19 arithmetic error in m09 Step 7 (1,303.95 x 53.50%) - outside the authorized
  scope of this fix, documented but not touched.
- Whether the same nr. 53-vs-58 mechanism error extends to arrears/back-pay references elsewhere in
  Modules 4, 9, and 11 - flagged as "probable, needs its own verification pass," deliberately not
  pursued to avoid further scope expansion in an already very large fix.
- Legal-basis citation refresh (adding the Royal Decree of 24 July 2026 and Law of 15 July 2026
  alongside the original 11 December 2025 citation) - new content, not one of the numeric fixes.

**This is likely the most consequential finding of the entire review**: a figure used in nearly
every tax calculation in both the CCG and WTC was wrong, and the error was only surfaced by insisting
on primary-source verification rather than accepting internally-consistent, previously-recomputed
figures as sufficient.


---

## REGRESSION AUDIT FINDINGS AND FIX (16 August)

3 blockers, 5 majors, 6 minors found. All 6 requested fixes applied and independently
reverified (spot-checked the car-coefficient chain directly against the docx table -
confirmed 88% with visible arithmetic, EUR 3,009.60 annual benefit, matches exactly).

### Confirmed correct, not a new finding
The 11,170 vs 11,180 concern carried forward from 3 prior sweeps is resolved: the CCG
correctly carries BOTH scales, properly separated (Table 53 = assessment, Table 54 =
Annex III withholding). The auditor concluded the shared CCG-Playbook-Learnings.md L4
is what's misleading, not our CCG - worth a note there if that file is ever revisited.

### Fixed
- Fix 1 (blocker): company car age coefficient 94%->88%, 13 downstream figures
  recomputed through Module 12 Example 5.
- Fix 2 (blocker): Module 9 redundancy withholding 697.42->697.61, totals recomputed.
- Fix 3 (blocker): social work bonus - discovered it's genuinely TWO components
  (P = R_B + R_A) since April 2024; the worked examples were right, the stated rule
  was wrong (fixed the rule, not the examples). Full 2026 parameter tables added for
  all 5 dated steps. Fiscal work bonus percentages added (33.14%/52.54%).
- Fix 4 (major): special SS contribution - confirmed 3 tables exist, all now stated
  and labelled with WTC's "INDIVIDUALLY ASSESSED EMPLOYEE" terminology. The EUR 12.33
  gap explained (4.22% vs 5.90% entry rates). A previously-wrong caption corrected.
- Fix 5 (major): pre-2014 notice rules researched and added (Law of 26 Dec 2013).
  Notable process note: the agent nearly drafted from a legal commentary that was
  itself wrong (published during a narrow window when a repeal-then-restoration made
  the law's status genuinely ambiguous) - caught this before finalizing by
  cross-checking FPS Employment directly, and added a warning against that specific
  commentary for future reference.
- Fix 6 (major): FEDRIS authority added to Module 10; confirmed the CCG's original
  8-day deadline was correct (not the Report Spec's "silent correction"); consolidated
  a redundant ASR row to point at the dedicated FEDRIS entry instead.

### New finding surfaced during Fix 3 — NOW CLOSED (work bonus fix pass)
Examples 2, 4, 6 granted only the work bonus's component A and called it "the maximum" -
with the corrected two-component formula they understated the bonus (Example 6:
should be 218.73, not 137.74). Recorded as an explicit OPEN ITEM in Module 5.1.1
rather than silently fixed (would ripple through 3 examples' full tax chains, a
materially larger change than requested) or silently left wrong. DECISION: fix this
next, as a separate, explicit action.

**Closed.** All three examples recomputed on the 1 July 2026 parameter rows, both
components, plus the full downstream chain. Social work bonus: E2 299.53 FTE ->
179.72 prorated -> **capped at 169.91**; E4 37.21 + 127.54 = **164.75**; E6
80.99 + 137.74 = **218.73**. The fix propagated further than the bonus line, because
the **fiscal** work bonus is a percentage of the social work bonus granted (33.14% on
component A, 52.54% on component B, Module 7 item 4) - both examples that claimed a
flat "annual maximum of 765.00" were wrong twice over. E4's derived fiscal bonus is
741.84, **below** the cap, so the 765.00 it previously claimed was an overstatement;
E6's is 1,058.40, so the cap genuinely binds there and 765.00 survives by coincidence.
Net effects: E2 net pay 1,192.44 -> **1,285.83**; E4 net for art. 1409 2,252.92 ->
**2,272.28** with net paid to the employee **unchanged at 1,772.91** (the whole
increase lands in the 100%-attachable band - the creditor takes it, not the employee);
E6 net pay 2,120.44 -> **2,166.77**. Two mislabellings also corrected: "the maximum"
removed from E4/E6, and E1's cited zero point moved from 3,403.62 (the 1 September
row) to 3,336.98 (the 1 July row actually in force for these examples) - E1's amount
stays 0.00 either way. The OPEN ITEM block in Module 5.1.1 is replaced by a CLOSED
block carrying the resulting figures. 44 independent recomputation checks, all pass,
with the parameters read back out of the .docx rather than restated. Mirroring
re-verified on tree.getpath: 0 of 4,551 module text units missing from the docx; the
only 9 docx-only units are title-page/TOC lines. Backups: *.bak-before-workbonus-fix
for the docx and 6 modules, none deleted.

### New finding surfaced during the work bonus fix, NOT actioned (outside its scope)
The same single-component understatement is live in two other artifacts, which carry
parameters and formulas rather than worked examples, so they were out of this pass's
stated scope (Examples 2, 4, 6):
- **06-payslip/BE_Compliance_Payslip_Generator.xlsx, cell J40** on both the Belgium (EN)
  and Belgium (NL) sheets: `=IF(J35<=3403.62,-127.54,0)`. This is wrong three ways -
  it grants component A only; it grants the **full maximum anywhere below the upper
  limit**, which is exactly the error Module 5.1.1's "Correction of record" warns
  against; and 3403.62 is the 1 September row's zero point. An employee on 3,000.00
  would be paid a 127.54 bonus that is actually 0.00 + a degressive component A.
- **02-wtc/BE-WTC-001-v1.0.xlsx**, cells `Version Control!C25`, `Wage Type Catalogue!F55`,
  `Wage Type Catalogue!F303` and `Tax Credit!B6`: all describe "maximum monthly
  reduction EUR 127.54 white-collar / EUR 137.74 blue-collar" as if it were the whole
  bonus. Those are the component A maxima; component B (171.99 / 185.75) is absent.
DECISION: raise as the next explicit action, as was done for this one. The payslip
formula is the more urgent of the two - it is executable, not descriptive.

### Two new honest gap markers introduced (kept as-is, not reworded to pass lint)
- NOT FOUND: work-bonus annual cap after the 1 July indexation
- NOT RESOLVED: whether the EUR 765 fiscal work bonus maximum is a basisbedrag
  subject to indexation - sources contradict by roughly a factor of two

### Verification
47 independent recomputation checks, all pass. .md<->.docx mirroring re-verified
with a corrected extraction method (keyed on tree.getpath, not id() - directly
inheriting a lesson from the audit pass's own self-caught extraction bug): 0 of
3,624 module text units missing from the docx; the only docx-only units are
legitimate title-page/TOC lines. Backups exist (39 total in 01-ccg/), none deleted.

**Status: all 6 requested fixes applied and independently confirmed. One new,
explicitly-scoped follow-up item (the 3 understated examples) queued as next action.**

---

## WORK BONUS FIX PROPAGATED TO THE PAYSLIP AND THE WTC — CLOSED (17 August)

Closes the two items raised as "the next explicit action" at the end of the work
bonus fix pass. Authoritative source: Module 5.1.1's dated 2026 parameter tables,
read back **out of the .docx** for verification rather than restated from the fix.

### Fix 1 — Payslip (the executable defect)
`Belgium (EN)!J40` and `Belgium (NL)!J40` were `=IF(J35<=3403.62,-127.54,0)`.
Wrong three ways: component A only; the **full maximum granted anywhere below the
upper limit** (the exact error Module 5.1.1's "Correction of record" warns
against); and 3,403.62 is the **1 September** zero point, whereas this specimen's
pay period is 01/07/2026–31/07/2026, so the **1 July** row governs.

Replaced with `=-M82`, driven by a labelled helper annex in columns **L:N, rows
64–84** of both language sheets — outside the `A1:J120` print area, so the printed
payslip is unchanged. The annex carries the 1 July 2026 white-collar parameters as
auditable cells (B: 2,300.62 / 171.99 / 0.2699 / 2,937.93; A: 2,937.93 / 127.54 /
0.3196 / 3,336.98), the performance fraction, the FTE reference wage, R_B, R_A,
P = R_B + R_A, the proration and the cap at the contribution due. A single-cell
one-liner was rejected in favour of helper cells so the parameters stay auditable.
Also corrected: the row-40 and step-3 labels, the statutory note A110 on both
sheets, and `Payslip Spec!E105`, which stated the same wrong rule in prose.

### Fix 2 — WTC
`Version Control!C25`, `Wage Type Catalogue!F55`, `Wage Type Catalogue!F303` and
`Tax Credit!B6` all presented 127.54 / 137.74 as the whole bonus with component B
absent. All four rewritten with the two-component structure, the **full five-row
dated 2026 ladder** for both components, the blue-collar x 1.08 relationship, the
dovetail, the annual cap and its NOT FOUND marker after 1 July. `Tax Credit!B6`
additionally records why this matters downstream: the fiscal work bonus is a
percentage of the social work bonus actually granted, at different rates per
component (33.14% on A, 52.54% on B, Module 7), so understating one understates
the other.

### Generators patched, so a rebuild cannot revert the fix
Applying the lesson from the tax-engine pass. The four WTC source strings live in
`be_wtc_data_part1.py`, `be_wtc_data_part7.py` and `build_be_wtc.py`; each was
spliced by tokenising the source, locating the run of adjacent STRING tokens whose
concatenation equals the old cell text, and substituting a literal built **from the
corrected workbook cell**, so the replacement was never retyped. All four now
reconstruct to the corrected text byte-for-byte and all three files compile.
`_build_payslip.py` had its `WB_LIMIT = 3403.62` constant replaced by the
two-component parameter set and a `wb_formula()` helper emitting a correct
self-contained degressive formula, verified to reproduce the artifact's annex at
every point in the band including the cap.

**Note on the payslip generator:** it was found to be **already stale** relative to
the delivered artifact before this fix (its language note differs from the shipped
A109), and a post-build patch script `_fix_regression_psl.py` already exists — so
build-then-patch is the established payslip workflow and the generator is not a
reliable rebuild path regardless. Patched here so it is at least not *wrong*;
resyncing it fully is a separate item, not attempted.

### Verification
- Parameters read back out of the .docx; the **dovetail** (component B's zero point
  equals component A's full-amount limit) and the **blue-collar x 1.08** relation
  hold in **all 5 dated rows** for both maxima and coefficients.
- The recomputation engine reproduces Module 5.1.1's own closed examples exactly:
  E4 37.21 + 127.54 = **164.75** (S=2,800.00 white-collar); E6 80.99 + 137.74 =
  **218.73** (S=2,660.00 blue-collar); E2 299.53 FTE x 0.60 = **179.72**.
- The workbook's **stored formula strings** were parsed back out and evaluated
  end-to-end (not reimplemented), confirming correct cell references.
- **Net pay unchanged at EUR 2,377.51.** Both the old and the new formula return
  0.00 at S = 3,500.00, so this specimen's figure never moved; the old formula was
  right here by luck and wrong everywhere in the band. Confirmed by evaluating the
  pre-fix backup as well as the fixed file.
- Both validators **PASS (blocker=0 major=0 minor=0)**, unchanged from baseline.

Backups: `*.bak-before-workbonus-fix` for both workbooks and all four generator
sources; none deleted.
