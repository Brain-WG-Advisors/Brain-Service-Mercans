# Stage 5 — TX (Texas) — 13-domain findings

Worker: compliance-source-hunter, 2026-11-02. Budget declared: 60 fetches / 2 h; used about 41 fetches (including access probes), about 1 h.
Shard: `00-official-sources/_register-shards/S5-TX.csv` (US-TXS5-001..019). Sources: `00-official-sources/ccg-sources/TX/` (18 files, 1.2 MB).

**Access finding that changes the TX picture.** The official statutes site `statutes.capitol.texas.gov` is a JavaScript app, which is why earlier passes left ch. 61 / ch. 2258 / Const. 24-a as MANUAL chrome reads. Its own bundle points to a static file server run by the Texas Legislative Council: `https://tcss.legis.texas.gov/resources/{CODE}/htm/{CODE}.{chapter}.htm` (e.g. `.../LA/htm/LA.62.htm`). That server answers plain curl with the full chapter text (A.1). Every statute row in this shard comes from it, with a local file. **The same URL pattern unlocks the statute text for every other state worker that cites Texas law, and it should replace the MANUAL rows US-TXPIT-001, US-TXSUI-002 and US-TXSUI-003 at synthesis** (`supersedes` is set on US-TXS5-001/007/008).

`www.twc.texas.gov` still returns HTTP 202 with an empty body (bot or geo challenge), and Wayback `2026id_` copies return 403. The TWC host `efte.twc.texas.gov` (Texas Guidebook for Employers, rate estimator) can be read.

## 1 — labour_code
- **Minimum wage:** Texas pays the federal FLSA minimum wage (Labor Code 62.051). There is no separate state rate, so the figure is USD 7.25 through FLSA s.6 (federal row, FED unit). No 2027 change is enacted in ch. 62. The state minimum wage overrides local wage ordinances for private employment, except public contracts and agreements with local governments (62.0515). **No local minimum wages apply to private employers.** [US-TXS5-002, A.1, high]
- **Scope trap:** ch. 62 does not apply to anyone covered by the FLSA (62.151), so in practice it covers only employees outside FLSA coverage. The exemptions are in 62.152-62.160. [US-TXS5-002]
- **Overtime:** there is no state overtime rule beyond the FLSA. Ch. 62 has no overtime section, and ch. 61 refers to FLSA exemption only to set pay frequency. [US-TXS5-002, US-TXS5-004, high]
- **Pay frequency:** FLSA-exempt employees are paid at least monthly. Everyone else is paid at least twice a month, with pay periods as equal as possible. If no paydays are designated, they default to the 1st and 15th, and paydays must be posted (61.011-61.012). [US-TXS5-004, A.1, high]
- **Method of payment:** pay may be cash, a negotiable instrument, EFT to an account the employee designates, or a payroll card (61.016).
  - Direct deposit: the employer may elect it, with 60 days' written notice (61.017(c)).
  - Payroll card: 60 days' notice (or by the first day of work for new hires), a fee list in English or in the card's language, and an opt-out form. If the employee opts out, the alternate payment starts by the first payday after day 30 (61.017(d)-(e)).
  - Wages in kind need the employee's written agreement (61.016(b)).
  
  [US-TXS5-004, high]
- **Child labour:** the minimum age is 14. At 14-15, the limit is 8 h/day and 48 h/week, with night-hour bans (51.011, 51.013). [US-TXS5-006, high]

## 2 — income_tax
- **No state income tax.** The Constitution, Art. VIII s.24-a, bars a tax on individuals' net incomes (2019). New s.24-b (added 4 Nov 2025) also bars a capital gains tax. There is therefore no state withholding, no state W-4, no supplemental rate, no rounding rule, no state W-2 filing and no reciprocity. [US-TXS5-001, A.1, high. It supersedes the MANUAL US-TXPIT-001. The Comptroller tax index US-TXP52-001 corroborates it.]
- **Local income taxes:** none. The Comptroller index lists no payroll or wage tax at any level [US-TXP52-001, A.2]. Resident and nonresident rules do not apply.
- **Multistate note:** a TX resident working in another state is withheld by that state's rules, and a TX employer with out-of-state workers follows the work state. This sits with the MULTI unit.

## 3 — social_security (SUI; no SDI/PFML)
- **Agency:** Texas Workforce Commission. **Wage base: USD 9,000 per employee per calendar year.** It is fixed in the statute (201.082(1)) and not indexed. [US-TXS5-007, A.1. The authority page US-TXSUI-001 / US-TXR3-003 agrees: second independent document family.]
- **2026 rates:** minimum 0.32%, maximum 6.32% [US-TXSUI-001, US-TXR3-003, A.2, already registered]. Components: deficit 0.00% and obligation assessment 0.01% [US-TXS5-019; the estimator labels its components differently from the rates page, as US-TXP52-002 already notes].
- **New employer rate:** the statute sets the greater of the major-group rate less 0.1 pt, or 2.6% (204.006) [US-TXS5-008, A.1]. TWC publishes "generally 2.70%" for the first six calendar quarters [US-TXS5-019, A.2]. **G-DERIVE:** the 2.70% cannot be re-derived, because the 2026 major-group rates are not published on any readable page. 2.70% is consistent with the statute, since it is at or above the 2.6% floor.
- **Employee contribution:** none. The employer may not deduct UI contributions from wages (204.003). [US-TXS5-008, high]
- **ETIA:** 0.1% of taxable wages, paid by the employer and collected with contributions (204.121). It is offset by a 0.1-pt cut in the replenishment rate (204.0625), so there is no net increase. [US-TXS5-008, plus the existing US-TXP7-001]
- **Coverage:**
  - Employer threshold: USD 1,500 in wages in a quarter, or one worker in 20 weeks (201.021).
  - Domestic employers: USD 1,000 in cash wages in a quarter, with an annual-reporting option due Jan 31 (201.027).
  - Farm and ranch labour: 201.028 / 201.047.
  
  [US-TXS5-007]
- **UI wages:** these include non-cash pay and FUTA-taxable tips (201.081). They exclude employer plan payments for retirement, sickness or medical costs, 401(a) and 403(a) payments, and FICA paid by the employer (201.082). [US-TXS5-007]
- **SDI / TDI / PFML / LTC: none.** No statute exists. Texas is absent from the DOL lists [US-TXR3-003, existing].

## 4 — payslip_statute — CORRECTION
- **Labor Code 62.003 (Earnings statement) exists.** At the end of each pay period the employer must give a written statement, signed by the employer or its agent, showing:
  - employee name;
  - rate of pay;
  - gross pay for the period;
  - each deduction and its purpose;
  - net pay;
  - hours worked (hourly pay) or units produced (piece rate).
  
  The statement may take any form, including the check voucher. If meals or lodging count toward the wage, they must be stated separately (62.053). [US-TXS5-003, A.1, high on the text]
- **Scope:** ch. 62 does not apply to FLSA-covered persons (62.151), so the duty applies **only to employees outside FLSA coverage**. For FLSA-covered employees, Texas has no statutory pay-statement content rule (FLSA records rules only).
- **This corrects** the mandate answer line "Labor Code ch. 61 read in full: no pay-statement requirement" (US-MQ-63 part 6; US-TXR3-001, US-TXLAB-001). That line is right about ch. 61 but wrong as a statement about Texas. The PSL and CCG should say: "statutory earnings statement for employees not covered by the FLSA (62.003); best practice for everyone else". Confidence on applying the scope: medium (no TWC commentary read).
- **Electronic delivery and retention:** no Texas rule found in ch. 61 or ch. 62. Retention follows FLSA and UI record rules (TWC rule 815.106, not read; see ACCESS gaps).

## 5 — reporting_instruments
- **Withholding return / state W-2:** not applicable, because there is no income tax [US-TXS5-001].
- **Quarterly UI wage report and payment:**
  - Filing is electronic only: Unemployment Tax Services, or QuickFile using ICESA, MMREF-1 or delimited formats (TWC rules 815.107/815.109) [US-TXSUI-006, existing, A.2].
  - The due date is not read from a primary source. TWC rule 815.107 text is ACCESS-blocked. It is commonly the last day of the month after the quarter, but that comes from tier-B leads only and is not registered.
- **Enhanced wage-report content (live, 2025):** Labor Code 204.0025 directs TWC to require, inside routine wage filings, wage, industry, occupation, full- or part-time status, county of primary employment and remote-work status. It was amended by S.B. 1786, H.B. 120 and H.B. 2 (2025, effective May/June 2025). [US-TXS5-008, A.1] The implementing TWC layout or rule was not read, so it is unknown which fields are mandatory from which quarter. This is a DD/RSPEC open question.
- **New hire:** report to the OAG Child Support Division's state directory within **20 calendar days** of the first day of work. Electronic reporters may instead report twice a month, 12-16 days apart [US-TXS5-012 statute; US-TXS5-016 OAG form A.2; US-TXS5-017 TWC A.3, second independent authority].
  - Required fields: FEIN, employer name, employer address for IWOs, employee SSN, date of hire, full name and address.
  - Optional fields: TWC account number, DOB, salary and frequency, state of hire.
  - Penalties: USD 25 per employee, USD 500 for conspiracy.
- **Registration:** a TWC UI account is required once the 201.021 / 201.027 / 201.028 thresholds are met. The UI agent authorisation is Form C-42 [US-TXSUI-005, US-TXP52-008, existing].

## 6 — leave
- **Paid sick leave:** no state statute. Labor Code 1.005 (H.B. 2127, effective 2023-09-01) preempts city and county ordinances on employment leave, benefits and scheduling for private employers, so the Austin, Dallas and San Antonio ordinances cannot apply. [US-TXS5-005, A.1, high]
- **PFML:** none (see domain 3).
- **Leave pay counts as wages only if promised in writing:** vacation, holiday, sick, parental and severance pay become "wages" only when owed under a written agreement or policy (61.001(7)(B)) [US-TXS5-004].
- **Voting time:** paid. The employer may not penalise time off to vote, and "penalty" includes lost wages. This does not apply if the polls are open two consecutive hours outside working hours (Election Code 276.004). [US-TXS5-014, high]
- **Jury service and military leave:** not fetched (Civ. Prac. & Rem. Code 122.001; Gov. Code 437.204 / 431.005). See Open questions.

## 7 — termination
- **Final pay:** a discharged employee must be paid by the 6th calendar day after discharge. An employee who leaves for any other reason is paid by the next regularly scheduled payday (61.014). Commissions and bonuses follow the agreement (61.015). [US-TXS5-004, A.1, high]
- **Accrued vacation payout:** owed only if a written policy or agreement promises it, and on its terms [US-TXS5-004; TWC guidebook US-TXS5-018, A.3].
- **Child-support interaction:** an employer holding a IV-D administrative writ must notify the OAG before any lump-sum payment of USD 500 or more (bonus, or pay in lieu of leave). It then holds the payment for 10 days or until the OAG authorises it (FC 158.215). Severance is withheld as if it were usual earnings, within the 50% cap (158.214). [US-TXS5-011, high]
- **State separation notice:** no statutory employee separation notice was found in ch. 61 or chs. 201/204. Not confirmed against TWC rules.
- **WARN:** no state mini-WARN found (not searched in depth; low payroll relevance).

## 8 — benefits_in_kind
- With no income tax, conformity matters only for the **UI wage definition** (201.081-201.082). Non-cash remuneration is UI wages. Employer payments to a plan for retirement, sickness, medical or death benefits, and 401(a)/403(a) trust payments, are excluded. [US-TXS5-007]
- Not read: how TWC treats employee elective 401(k) deferrals and section 125 salary reductions (FUTA treats deferrals as wages; 201.082 does not expressly exclude them). Open question.

## 9 — deductions_garnishments
- **Wage deductions:** only by court order, by state or federal law, or with written employee authorisation for a lawful purpose (61.018) [US-TXS5-004].
- **Garnishment:** current wages are exempt, except for court-ordered child support and spousal maintenance (Const. Art. XVI s.28; CPRC 63.004). Federal tax levies and federal administrative garnishments apply by federal law. **Creditor wage garnishment is not available under Texas law.** [US-TXS5-009, US-TXS5-010, A.1, high]
- **Child-support IWO:** [US-TXS5-011, high]
  - Cap: 50% of disposable earnings (158.009).
  - Start: by the first pay period after delivery (158.202).
  - Remittance: to the State Disbursement Unit on each pay date. Employers with 50 or more employees must pay by EFT/EDI within 2 business days, and face up to USD 25 per paper remittance (158.203).
  - **Employer fee: up to USD 10 per month** (158.204).
  - Several orders: split equally across current support, then arrears (158.207).
  - Termination: notify within 7 days (158.211).
- **State tax levies:** not applicable for income tax. TWC can levy for unpaid UI contributions (not examined).

## 10 — collective_agreements (prevailing wage)
- Government Code ch. 2258 applies to public works. The public body sets the prevailing per diem rate (by survey or Davis-Bacon), and there is no state agency rate table. The penalty is USD 60 per worker per day, and contractors must keep records of name, occupation and per diem wage. There is no state certified-payroll form in the statute. [US-TXR3-002 (existing A.1); US-TXS5-015 adds the local file.]

## 11 — indexation
- Nothing is indexed by state law:
  - minimum wage: follows the FLSA;
  - UI wage base: USD 9,000, set by statute;
  - UI rates: recomputed by TWC each year (benefit ratio, replenishment ratio, deficit and obligation assessment; ch. 204 subch. C/D) and mailed in December. **2027 rates are not yet published as of 2026-11-02.**
- G-DERIVE does not apply: no index-linked amount exists.

## 12 — data_protection
- Business and Commerce Code 501.001: a private person may not make an SSN public, print it on access cards, send it over a non-secure Internet connection, or mail it on material unless law requires it. Uses required by law and internal administrative uses are exempt. **There is no SSN truncation rule specific to pay statements.** Mailing a paper payslip that shows the full SSN risks breaching 501.001(a)(5), because no law requires the SSN on a payslip. Recommend masking it. [US-TXS5-013, A.1; the application to payslips is our reading, medium]

## 13 — live_legal_change (2026-01-01 to 2026-11-02)
- **Const. Art. VIII s.24-b:** capital gains tax ban, approved 4 Nov 2025. No payroll effect; it confirms the no-income-tax position. [US-TXS5-001]
- **Labor Code 204.0025:** enhanced wage-filing data (2025 amendments). Payroll and DD impact depends on the TWC implementation, which was not read. [US-TXS5-008]
- **TWC 2026 rates:** registered (US-TXSUI-001). 2027 rate notices are due in December 2026, so re-check them at the bulletin sweep.
- **Federal minimum wage:** no change enacted.
- **Not done:** a sweep of TWC news, the Texas Register and the 89th Legislature special sessions (www.twc.texas.gov is blocked). It is left for the orchestrator's browser pass.

## Special populations (state level)
| Population | Rule | register_id |
|---|---|---|
| Domestic / household | UI covered once cash wages reach USD 1,000 in a quarter, with an annual-reporting option due Jan 31 (201.027). Exempt from the state minimum wage (62.154); the FLSA still applies where it covers them | US-TXS5-007, US-TXS5-002 |
| Agricultural | UI covers farm and ranch labour per 201.028/201.047. H-2A workers are excluded from UI unless FUTA covers them (201.078). Ch. 62 exemptions for dairy and livestock (62.160) | US-TXS5-007, US-TXS5-002 |
| Minors | Minimum age 14; hour limits for ages 14-15 (51.013). Under-18 non-graduates are exempt from the state minimum wage (62.155); the FLSA governs where it applies | US-TXS5-006, US-TXS5-002 |
| Tipped | Cash wage per FLSA 3(m); "tipped" means more than USD 20 a month in tips (62.052). UI wages include FUTA-taxable tips (201.081) | US-TXS5-002, US-TXS5-007 |
| Clergy / religious | Excluded from UI employment: churches, church organisations, ministers, religious orders (201.066). Exempt from ch. 62 (62.152) | US-TXS5-007, US-TXS5-002 |
| Students | Excluded from UI when working for their own school or in a credit co-op programme; some camp students also excluded (201.069). Under-20 students are exempt from the state minimum wage (62.155) | US-TXS5-007, US-TXS5-002 |
| Nonresident aliens | No state income tax, so there is no state rule. Only the UI H-2A exclusion (201.078) | US-TXS5-001, US-TXS5-007 |
| Statutory employees | UI "employment" includes certain drivers and salespersons (201.042); full text not reviewed. No state income tax effect | US-TXS5-007 (section listed, not quoted) |
| Government employees | The state and political subdivisions are UI employers (201.026), with reimbursement or contribution options in ch. 205 (not read). Elected officials are exempt from ch. 62 (62.153) | US-TXS5-007, US-TXS5-002 |

## ACCESS gaps
- `https://www.twc.texas.gov/programs/unemployment-tax/your-tax-rates`: HTTP 202, empty body. Wayback `https://web.archive.org/web/2026id_/https://www.twc.texas.gov/programs/unemployment-tax/your-tax-rates` returns 302, then a blocked capture. The 2026 figures are already registered from an earlier Wayback copy (US-TXSUI-001).
- `https://web.archive.org/web/2026id_/https://www.twc.texas.gov/programs/unemployment-tax/employers-quarterly-wage-report-filing-options`: HTTP 403. Needed for the quarterly due date.
- `https://texreg.sos.state.tx.us/public/readtac$ext.TacPage?...ti=40&pt=20&ch=815&rl=107` (40 TAC 815.107, wage report due date) and the analogous rule 815.106 (records): "Site Has Moved" page. The new SOS TAC host was not resolved.
- `https://www.texasattorneygeneral.gov/sites/default/files/files/child-support/Publications/new-hire.pdf` and `.../Publications/csquickrefemp.pdf`: HTTP 404 (the form PDF was read instead).
- `https://employer.oag.texas.gov/`: Salesforce app shell with no readable content (lump-sum notification and independent-contractor reporting pages not read).

## Open questions
1. **US-MQ-63 part 6 correction:** Labor Code 62.003 earnings statement (scope: employees outside FLSA coverage, 62.151). The orchestrator and scaffolder should record this against the sealed answer. The PSL and CCG must not say "Texas has no pay-statement law".
2. **Quarterly UI wage report due date** (40 TAC 815.107) and records retention (815.106). Would close it: the rule text from the SOS Texas Administrative Code, or TWC's employer page, read in the browser pass.
3. **Labor Code 204.0025 implementation:** which new wage-report fields (occupation, FT/PT, county, remote status) are mandatory, and from which quarter. Would close it: the TWC wage-report file specification (ICESA/TXUS layout) or the TWC rule adopted under 204.0025.
4. **New employer rate 2.70% vs the statutory 2.6% floor:** consistent, but cannot be derived without the 2026 major-group rates. Would close it: a TWC rate notice or the TWC "how your 2026 tax rate was calculated" page.
5. **UI treatment of elective 401(k) deferrals and section 125 reductions** (201.082 is silent). Would close it: the TWC rule defining wages (40 TAC ch. 815) or TWC tax guidance.
6. **Independent-contractor reporting to the OAG** (tier-B lead hklaw 2017; not verified). Would close it: 1 TAC 55.303 text or the OAG employer portal page.
7. **Jury service and military leave pay rules** (CPRC 122.001; Gov. Code 431.005 / 437.204): not fetched. They can be read through the same tcss.legis.texas.gov pattern (e.g. `.../CP/htm/CP.122.htm`).
8. **2027 TWC rates and the live-change sweep:** due December 2026.

**Confidence by domain:**
- High: 1, 2, 3, 7, 9, 10, 11.
- Medium-high: 4 (text high; scope application medium), 5 (due date open), 6.
- Medium: 8, 12, 13.
