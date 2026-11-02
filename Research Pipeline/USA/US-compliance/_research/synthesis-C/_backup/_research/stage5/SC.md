# Stage 5 — South Carolina (SC): 13-domain findings

Worker: compliance-source-hunter, 2026-11-02. Brief: `_prompts/stage5-brief.md`. Mandate block: US-MQ-60 (answered at seal attempt 4; T3).
Budget declared: 60 fetches / 2 h. Used: about 33 fetches (curl + 3 web searches) and about 25 minutes, under the 75% mark.
Register shard: `00-official-sources/_register-shards/S5-SC.csv` (18 rows, US-SCS5-001..018). New sources are in `00-official-sources/ccg-sources/SC/` (23 files, 4.56 MB after this pass; the largest is the SUITS spec at 0.88 MB). A duplicate WH1603F_2026 download had the same md5 as `pdfs/SC/WH1603F_2026_webfetch-20261029.pdf` (1257ffc4…) and was deleted (F23).

Active rows reused without a re-fetch: US-SC-003 / US-SCR3-007 / US-SCP7-001 (DEW 2026 rate page, wayback 2026-06-07), US-SC-007 / US-SC-P5-1-002 (WH-1603F 2026), US-SC-P5-1-003 (WH-105), US-SCR3-002 (Reg. ch. 117), US-SCR3-003 (RR #22-3), US-SCR3-004 (12-6-3400 credit), US-SCR3-006 (Title 41 index), US-SCR3-008 (UCE-1010 POA), US-SCR3-009 (no prevailing wage law), US-SC-P5-2-001 (SC2848), US-SC-P5-2-003 (DOR tax index, no local income tax), US-SC-P5-2-004/-005/-006, US-SCL-001/-002, US-SCP9L-001/-002.

**Headline finding (live change).** 2026 Act No. 110 (H.4216) is **in force**. The Governor signed it on 2026-03-30, and it applies to tax years beginning after 2025. It sets the 2026 liability schedule at 1.99% below 30,000 USD of taxable income and 5.21% minus 966 USD from 30,000, and it replaces the federal standard deduction with the SC Income Adjusted Deduction (SCIAD). Section 6 orders SCDOR to adjust the withholding tables. As of **2026-11-02**, SCDOR still publishes the pre-Act tables and formula: WH-1603 Rev. 10/30/25 and WH-1603F Rev. 11/4/25 (0% / 3% / 6%), with the same md5 as the 2026-10-29 copy. Information Letter #26-20 (2026-08-31) says only that SCDOR "will consult" the Revenue and Fiscal Affairs Office (RFA), and gives no date [US-SCS5-001, US-SCS5-002, US-SCS5-005]. **Operating level:** the new rates apply when the annual return is assessed. Withholding in 2026 stays on WH-1603/1603F until SCDOR republishes the tables. Builders must not model 1.99/5.21 inside the 2026 withholding engine.

---

## 1. labour_code
- **Minimum wage:** SC has no state minimum-wage statute, so the federal FLSA rate of 7.25 USD/h applies. The research ruled out a state section from two things: the Title 41 chapter index [US-SCR3-006] and 6-1-130, which takes the FLSA section 6 rate as its reference. Local minimum wages are **preempted**: 6-1-130 bars any political subdivision from setting a minimum wage above the federal rate, except in its own contracts. No 2027 change is enacted [US-SCS5-012]. Confidence: 95%.
- **Overtime:** no state overtime statute in Title 41; FLSA only [US-SCR3-006]. Confidence: 85%. This is an absence proven only at the chapter-index level.
- **Pay frequency and timing:** no statutory frequency. The employer must pay at the time and place set in the hire notice under 41-10-30(A), and give 7 calendar days' written notice before changing it (wage increases excepted) [US-SC-P5-2-006; local file `ccg-sources/SC/SC-Code_41-10_wage-payment.html`, 41-10-40(D)].
- **Method of payment:** lawful US money, or a negotiable warrant or check dated the payday. Wages may go to an insured financial institution doing business in SC. With direct deposit, the employee gets a statement of earnings and withholdings and at least one free withdrawal per deposit (41-10-40(A)-(B)). The statute does not mention paycards [US-SC-004, US-SC-P5-2-006].
- **Deductions:** none without state or federal authority or the written notice under 41-10-30(A) (41-10-40(C)). Penalty for unpaid wages: treble damages, 3-year limitation (41-10-80(C)).
- **Lactation:** reasonable unpaid break time, or use of paid break or meal time (41-1-130) [US-SCS5-013].

## 2. income_tax
- **Withholding method 2026 (operative):** the WH-1603 tables (0-10 allowances) or the WH-1603F formula. Steps: annualize; subtract 5,000 USD per allowance; subtract a standard deduction of 10% of gross, capped at 7,500 USD, only with one or more allowances. Annual tax is 0% below 3,640 USD; 3% minus 109.20 USD from 3,640 to 18,230 USD; 6% minus 656.10 USD from 18,230 USD [US-SC-007, US-SC-P5-1-002, US-SCS5-004].
  - **G-DERIVE, done in Python:** 750 × 52 = 39,000; minus 3 × 5,000 and minus 3,900 gives 20,100; 20,100 × 0.06 − 656.10 = 549.90; ÷ 52 = **10.58**, matching the WH-1603F worked example.
  - Bracket continuity: 3,640 × 3% − 109.20 = 0. At 18,230, both 3% − 109.20 and 6% − 656.10 give 437.70, which matches the "max tax 1st bracket" constant.
- **Certificate:** SC W-4 (2026), Rev. 12/5/25.
  - Allowances, an additional amount, and exempt status (expires 2026-12-31); military-spouse domicile election (RR #24-5).
  - Regular wages may not be withheld as a flat amount or percentage.
  - An employee without an SC W-4 is withheld at zero allowances.
  - [US-SCS5-003, US-SC-P5-1-003]
- **Threshold and rounding:** withhold if wages are expected to reach 1,000 USD in the year. The employer may compute wages to the nearest dollar (12-8-520(A)-(B)) [US-SCS5-018, US-SCR3-001].
- **Supplemental rate:** none. No flat supplemental rate exists in the statute, in Reg. ch. 117, in the DOR withholding page or in the FAQ (re-read 2026-11-02, keyword search for bonus, supplemental and flat). Bonuses are wages run through the tables [US-SCR3-002, US-SCS5-002].
- **2026 liability (assessment level, Act 110):** the two-rate schedule above.
  - SC taxable income starts from federal AGI.
  - SCIAD is 15,000 / 22,500 / 30,000 USD (single or MFS / head of household / MFJ). It phases out over AGI 40,000–95,000, 60,000–142,500 and 80,000–190,000 USD respectively; the reduction is rounded down to 10 USD.
  - SC EITC is 125% of the federal credit, capped at 200 USD.
  - Continuity check: 30,000 × 1.99% = 597 = 30,000 × 5.21% − 966.
  - [US-SCS5-001, US-SCS5-005]
- **Resident / nonresident:**
  - Wages are taxed where earned. A nonresident is withheld on SC-earned wages.
  - A resident working in a state with no income tax is withheld for SC.
  - A resident's wages earned in another state are not SC-withheld if that state's withholding applies (12-8-520(C)(1)). The resident gets a credit for tax paid to other states (12-6-3400).
  - SC has no reciprocity agreement.
  - A nonresident's SCIAD is prorated by SC AGI / federal AGI.
  - [US-SCS5-002, US-SCS5-018, US-SCR3-003, US-SCR3-004, US-SCS5-001]
- **Local income taxes:** none. The SCDOR tax index lists only local sales taxes [US-SC-P5-2-003].
- **Conformity:** the IRC as of 2024-12-31 (12-6-40(A)(1)(a), last amended by 2025 Act No. 63). No 2026 conformity act appears in the section history [local `pdfs/SC/t12c006_scstatehouse-20261030.html`; cited via US-SCR3-004's file].
- Confidence: 95% on the 2026 withholding mechanics and the Act 110 text. The date of the post-Act-110 table revision is unknown.

## 3. social_security (SUI / SDI / PFML / levies)
- **SUI agency:** SC Department of Employment and Workforce (DEW). Contributions are employer-only and may not be deducted from wages (41-31-310) [US-SC-P5-2-005].
- **Taxable wage base:** **14,000 USD** per employee per calendar year, fixed by statute since 2015-01-01 and not indexed. Wages reported under other states' UI laws count toward it (41-27-380(B)) [US-SCS5-014]. This is A.1, confirming US-SC-003 (A.2).
- **2026 rates (DEW page, wayback copy of 2026-06-07):** class 1 total 0.060% up to class 20 total 5.460%; no solvency surcharge in 2026. A new employer pays the higher of the class 12 rate or 1%, plus DACA = **1.060%** [US-SC-003].
  - G-DERIVE: 14,000 × 0.0006 = 8.40; 14,000 × 0.0106 = 148.40; 14,000 × 0.0546 = 764.40. All three equal the page's "maximum cost per employee" figures.
- **DACA:** 0.06% of wages for all contributory employers, except reimbursing and governmental employers. The statute (41-27-410) [US-SCS5-014] and the DEW page [US-SCR3-007] are two independent authorities for the same number.
- **2026 Act No. 243 (S.688), in force 2026-07-01:**
  - Benefit-ratio look-back: 12 quarters through tax year 2026, **16 quarters for 2027**, 20 quarters from 2028 (employers in rate class 1 in 2026 keep 12 quarters while they stay in class 1).
  - Solvency surcharge (41-31-45) rewritten.
  - Unpaid tax execution issued on or after 2027-01-01: employer rate plus 2 percentage points.
  - Late-report penalty: 10%, minimum 25 USD; the 1,000 USD caps on penalties are removed.
  - [US-SCS5-015]
- **SDI / TDI / PFML / LTC:** none in SC (Title 41 chapter index) [US-SCR3-006].
- **Corporate officers:** covered unless the corporation files a written election out for at least 2 years and notifies the officers (41-27-265) [US-SCS5-014].
- Confidence: 90%. The 2026 rate-class table rests on the wayback copy, because dew.sc.gov returns 403 to a direct GET.

## 4. payslip_statute
- **Content:** an itemized statement of gross pay and deductions for each pay period (41-10-30(C)). With direct deposit, a statement of earnings and withholdings (41-10-40(B)). The statute requires no other field, such as hours, rates or employer address [US-SC-P5-2-006, US-SC-004].
- **Exemptions from 41-10-30:** employers of domestic labour in private homes, and employers with fewer than 5 employees at all times during the preceding 12 months (41-10-20).
- **Hire notice:** written notice of normal hours, wages, time and place of payment, and deductions, or conspicuous posting. Changes take effect only after 7 days' written notice [US-SC-P5-2-006].
- **Electronic delivery:** no SC statute addresses it. 41-10-30(C) says only "furnish".
- **Retention:** wage-payment records 3 years (41-10-30(B)); UI payroll records 5 years (Reg. 47-14) [US-SCS5-007].
- **SSN:** see domain 12.
- Confidence: 90%. Electronic consent rests only on the silence of the statute.

## 5. reporting_instruments
| Filing | Authority | Frequency / deadline | Format / channel | register_id |
|---|---|---|---|---|
| Withholding deposits | SCDOR | Resident agents: same dates as federal deposits. Nonresident agents (and agents not depositing federally): by the 15th of the next month if 500 USD or more, else quarterly. Payments allocated by paycheck date | MyDORWAY / EFT. Electronic required at 15,000 USD or more per quarter or 24+ payments a year; paper coupon WH-1601 | US-SCS5-002, US-SCS5-018 |
| WH-1605 (Q1–Q3) | SCDOR | Apr 30, Jul 31, Oct 31. Zero returns are required while the account is open | MyDORWAY, batch program (10+ returns), or paper | US-SCS5-002 |
| WH-1606 (Q4 + annual reconciliation) | SCDOR | Jan 31. Required if the account was open in any part of the year | same | US-SCS5-002 |
| W-2 to SCDOR | SCDOR | Jan 31 (employees, SSA and SCDOR) | `file_upload`: EFW2 .txt with the required SC **RS** state record (state code 45, full SSN), or Excel template (up to 30 employees), or manual entry. Electronic is mandatory at 10+ forms. Paper filers send WH-1612. Filing with SSA does **not** satisfy SC | US-SCS5-016, US-SCS5-017, US-SCS5-003 |
| Quarterly UI contribution and wage report | DEW | Last day of the month after the quarter (Reg. 47-15(C), 47-16) | `file_upload` / online in SUITS: ICESA, EFW2, XML or CSV (SUITS spec v1.6, 2023-10-25). Agents for 10+ employees must file electronically (41-31-160) | US-SCS5-006, US-SCS5-007, US-SC-P5-2-005 |
| New hire | DSS State Directory of New Hires | 20 calendar days after hire. Electronic transmitters: semi-monthly, 12–16 days apart. Rehire after 60+ days counts as a new hire | newhire.sc.gov, or a copy of the SC W-4 with boxes 8–10. Fields: employer name, address and FEIN; employee name, address and SSN | US-SCS5-011, US-SCS5-003 |
| Mass separation | DEW | UCB-113 per worker within 10 days (excluding Sundays and holidays); 10+ workers in one establishment | form | US-SCS5-007 |
| Registration | SCDOR (9-digit withholding file number, MyDORWAY) / DEW (SUITS) | at start | online | US-SCS5-002 |

- **Scope trap:** the TY2026 RS-1 edition is not yet published. The file at the same URL is the TY2025 edition (October 2025) [US-SCS5-017].
- Confidence: 90%.

## 6. leave
- **Paid sick leave:** no state statute. **Local mandates are preempted:** 41-1-25 (2017 Act No. 3) bars every political subdivision from requiring any employee benefit, including paid sick leave, paid vacation, paid holidays and retirement benefits [US-SCS5-013].
- **PFML:** none [US-SCR3-006].
- **Jury duty / subpoena:** protected against dismissal or demotion (41-1-70); no paid-leave mandate [US-SCS5-013].
- **Vacation and sick pay:** paid only under the employer's policy. Once due under the policy, they are "wages" for the wage-payment chapter (41-10-10(2)).
- Confidence: 90%.

## 7. termination
- **Final pay:** all wages due within 48 hours of separation, or by the next regular payday, which may not exceed 30 days. The rule applies to any separation, discharge or resignation alike (41-10-50). Remedy: treble damages (41-10-80(C)).
- **Accrued vacation:** payable only if due under the employer's policy or contract (41-10-10(2)). There is no statutory payout mandate.
- **Wages in dispute:** pay the conceded amount unconditionally (41-10-60).
- **Separation notice:** no employer-issued UI separation notice at termination. The employer answers DEW's claim notice (Reg. 47-19, 41-31-160). For mass separations, UCB-113 [US-SCS5-007].
- **Child support:** within 20 days after employment ends, notify the clerk of the termination date and the final paycheck (63-17-1460(G)) [US-SCS5-010].
- **State WARN law:** none found in the Title 41 index (absence at index level) [US-SCR3-006].
- Confidence: 90%.

## 8. benefits_in_kind
- **Conformity:** SC adopts the IRC as amended through 2024-12-31 (12-6-40). Act 110 decouples only the federal standard and itemized deductions (12-6-50(21)) [US-SCS5-001].
  - Federal exclusions (401(k), section 125, HSA, transit, group-term life) follow the 2024 IRC, and no SC departure was found.
  - Federal changes enacted after 2024-12-31 (OBBBA 2025) are not adopted for SC unless a later conformity act passes.
  - These are return-level effects; wages for withholding follow 12-8-520(D) and IRC 3401.
- **UI:** in-kind pay is valued at DEW rates (Reg. 47-1). In-kind pay to agricultural and domestic workers is excluded from UI wages, and so are employer plan payments for retirement, sickness, medical care and death (41-27-380(A)) [US-SCS5-007, US-SCS5-014].
- Confidence: 80%. No item-by-item SC addition/subtraction list (12-6-1130/1140) was read for each benefit.

## 9. deductions_garnishments
- **Consumer debt:** **no wage garnishment** for consumer credit sales, leases, loans or rental-purchase agreements (37-5-104). An employer may not discharge an employee over such a garnishment (37-5-106) [US-SCS5-008].
- **Child support:**
  - Start by the next regular pay period after service.
  - Cap: CCPA 15 USC 1673(b).
  - Employer fee: up to **3 USD per withholding**, deducted from the obligor.
  - Priority: current support first, and every order partly implemented.
  - Remit to the State Disbursement Unit within **7 working days**, stating the withholding date.
  - Out-of-state orders: the fee, cap and timing follow the law of the principal place of employment.
  - [US-SCS5-010]
- **Wage deductions:** require legal authority or written notice (41-10-40(C)).
- **State tax levy on wages:** not read (open question).
- Confidence: 85%.

## 10. collective_agreements / prevailing wage
- SC has **no state prevailing-wage law**: it is among the 24 states listed in the DOL footnote, and chapter 41-10 has no such section. Federal Davis-Bacon certified payroll applies on federal projects only [US-SCR3-009, US-SC-P5-1-004]. Confidence: 90%.

## 11. indexation
- **Income tax brackets:** cumulatively indexed each 15 December by chained CPI, capped at 4% a year, rounded to 10 USD, for the next tax year (12-6-520). The Act 110 30,000 USD bracket is indexed the same way.
- **Top rate (from TY2027):** cut if the Board of Economic Advisors (BEA) projects individual income tax revenue up by at least 5%. The reduction is the greater of 200 million USD or 25% of the surplus, until the rate reaches 1.99%. The forecast in effect on 15 February is final [US-SCS5-001, US-SCS5-005].
- **Withholding constants** (5,000 USD per allowance, 10% / 7,500 USD cap): set by DOR each year in WH-1603F; not statutory.
- **Not indexed:** the UI wage base (14,000 USD, statutory) and the minimum wage (federal).
- **Publication:** SCDOR's annual withholding tables in early November, via the news page and the Withholding Tax News email [US-SCS5-002]. The 2027 files (WH1603_2027, WH1603F_2027, SCW4_2027) returned **404 on 2026-11-02**, so they are not yet published.
- **DEW:** annual rate notice and tax-rate table (2027 not read).

## 12. data_protection
- **SSN (37-20-180):**
  - No public display of 6 or more digits.
  - No SSN, or a portion of 6 or more digits, on materials mailed to the individual unless law requires it, and never visible on a postcard or through the envelope.
  - Internet transmission only over a secure connection or encrypted.
  - No disclosure to third parties without consent, except for a legitimate business or government purpose.
- **Payroll consequences:**
  - Mailed pay statements show 5 digits at most.
  - The W-2 (federal requirement) and the DOR RS record (full SSN required) are exempt as legally required.
- [US-SCS5-009, US-SCS5-017]
- Confidence: 90%. The breach-notice statute 39-1-90 was not read.

## 13. live_legal_change (2026-01-01 → 2026-11-02)
| Change | Status | Level | register_id |
|---|---|---|---|
| 2026 Act No. 110 (H.4216): 1.99% / 5.21% schedule, SCIAD, EITC cap, decoupling from the federal standard deduction | **In force**: signed 2026-03-30, applies to TY2026 | Assessment (annual return). Withholding unchanged until SCDOR reissues WH-1603/1603F; no revised edition as of 2026-11-02 | US-SCS5-001, -002, -005 |
| Act 110 Section 6: DOR to adjust withholding tables | Ordered; **not yet implemented** (IL #26-20, 2026-08-31: "will consult RFA") | Withholding | US-SCS5-005 |
| 2026 Act No. 243 (S.688): UI benefit ratio 16 quarters (2027) / 20 quarters (2028); +2% rate on post-2027 executions; penalty caps removed | **In force** 2026-07-01 (benefit-ratio change effective for tax year 2027) | Employer UI rate | US-SCS5-015 |
| Other 2026 acts in the downloaded chapters: Act 146 (H.4189), Act 183 (H.3551, 12-6-1120(12)), Act 162 (S.32), Act 225 (S.556) | In force; they touch hospital definitions and return-level adjustments and credits, not payroll withholding (section titles only) | Assessment | — (sweep note) |
| Rate cut for TY2027 under 12-6-510(C)(2) | Contingent on the BEA forecast; not determined | Assessment, then tables | US-SCS5-001 |

Sweep method: a mechanical grep for "2026 Act No." in the history notes of every code chapter downloaded this pass and in t12c006. No 2026 amendments were found in chapters 41-10, 41-1, 12-8, 37-5, 37-20 or 63-17 (beyond Act 146 conforming edits in 63-17 and 43-5). This is limited to the chapters read; it is not a full SC session sweep.

## Special populations (state-level, US-OWN-005)
| Population | SC rule | register_id |
|---|---|---|
| Domestic / household workers | Exempt from the 41-10-30 notice and pay-statement duties. Employer-paid FICA and in-kind pay are excluded from UI wages. Coverage threshold (41-27-230) not read | US-SCS5-014; 41-10-20 in the US-SC-004 file |
| Agricultural | UI defines agricultural labour (41-27-120). Agricultural labour by students or qualifying part-timers is excluded (41-27-260(16)). In-kind pay excluded from UI wages. Minimum wage: federal | US-SCS5-014 |
| Minors | Child labour: 41-13-20 delegates the rules to LLR regulations (not read). Newspaper delivery by under-18s and a child under 18 employed by a parent are excluded from UI | US-SCS5-014 |
| Tipped employees | No state minimum wage, so the federal tipped rules apply. Reported tips are UI wages (41-27-380(A)) | US-SCS5-014, US-SCS5-012 |
| Clergy / religious | Churches and ministers excluded from UI (41-27-260(10)). Withholding: follows the federal wage definition | US-SCS5-014 |
| Students | A student employed by own school, and student nurses and interns, are excluded from UI (41-27-260(9), (12)) | US-SCS5-014 |
| Nonresident aliens | No SC rule beyond the general rule: SC wages withheld wherever the employee resides. 12-8-550: 2% on nonresidents performing temporary personal services (non-wage) | US-SCS5-018, US-SC-P5-2-004 |
| Statutory employees | No state rule beyond federal (chapter 12-8 read; wages follow IRC 3401) | US-SCS5-018 |
| Government employees | Elected and policymaking posts excluded from UI (41-27-260(5)). Governmental employers exempt from DACA (41-27-410). 12-8-10 includes governments as "person" | US-SCS5-014, US-SCS5-018 |
| Corporate officers | UI-covered unless the corporation elects out (2-year election plus notice) | US-SCS5-014 |
| Military spouses | Exemption election on the SC W-4 (RR #24-5) | US-SCS5-003 |
| Commission-only insurance and real-estate agents, direct sellers, owner-operator drivers | Excluded from UI | US-SCS5-014 |

## ACCESS gaps (exact URLs)
- `https://dew.sc.gov/employers/tax-rate-information`: HTTP 403 (direct curl, US exit IP). The wayback 2026-06-07 copy is already held (US-SC-003).
- `https://dew.sc.gov/employers/ui-tax-forms`: no response (curl code 000). The wayback 2026-10-09 copy is held.
- `https://dew.sc.gov/sites/dew/files/Documents/SUITS-%20Wage%20Report%20and%20Payment%20File%20Specification%20version%201.6%2010.25.2023.pdf`: HTTP 403. Retrieved via the wayback 2025-08-04 capture.
- `https://dew.sc.gov/employers/file-and-pay-taxes`: no wayback capture (404).
- `https://newhire.sc.gov/`: no response directly. The wayback 2026-10-16 copy is a JavaScript shell with no content.

## Open questions
1. **Post-Act-110 withholding tables.** When will SCDOR reissue WH-1603/WH-1603F/SC W-4, and will the revision be retroactive, mid-2026, or only the 2027 edition?
   - Attempted: the DOR withholding page and news page, IL #26-20, and the 2027 file URLs (404).
   - What would close it: the SCDOR 2027 (or revised 2026) WH-1603F, expected around November 2026 on dor.sc.gov/withholding, or a Withholding Tax News notice.
2. **DEW 2027 rate table and solvency surcharge** under the Act 243 look-back. Would close it: the DEW 2027 tax-rate information page or the employer rate notice. It needs a browser pass, since direct access returns 403.
3. **RS-1 for TY2026.** Would close it: the SCDOR October-2026 edition of RS-1.
4. **UI coverage thresholds for domestic and agricultural employers.** Would close it: 41-27-230 and 41-27-210 text, in the t41c027 file already held but not extracted.
5. **Child-labour regulations** (LLR, 41-13-20). Would close it: SC Code of Regulations chapter 71 child-labour article.
6. **SCDOR wage levy (garnishment for state tax).** Would close it: S.C. Code 12-54 (warrant of distraint and garnishment section).
7. **Item-by-item SC addition/subtraction treatment of fringe benefits after Act 110** (12-6-1130 / 12-6-1140). Would close it: those sections in the t12c006 file held.
