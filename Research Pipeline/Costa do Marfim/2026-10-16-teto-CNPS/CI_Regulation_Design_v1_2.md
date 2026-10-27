# CI — Côte d'Ivoire Federal Payroll — Clean-Room Regulation Design v1.2
**Country:** Côte d'Ivoire (CI) · ISO 3166-1 numeric 384 · Currency XOF (FCFA, whole francs, no decimal subunit)
**Tax year:** 2026 · **Regulation ID prefix:** `9384` (9 + ISO 384), ordinals from 11, spaced by 10
**Design basis:** `CI-CCG-001` (through v1.2), `CI-WTC-001-v1.0.xlsx`, `CI-DD-001-v1.0.xlsx`, `CI-SIR-001-v1.0`, the 7 Report Specs, `CI-QA-REPORT.md`, `CI-ALIGNMENT-PATCH.md`, primary-source verification, **plus Mohit Jain's email-thread resolutions (Jul–Aug 2026) and his design review notes (`CI_Review_Notes_for_Wallisson.md`, 07 Aug)**.
**Method:** Clean-room — built from the CCG + statutory research, not copied from the WTC (design-first principle).

**v1.2 changelog (2026-10-16):** CNPS PF / AM / AT-MP ceiling corrected 70 000 → 75 000 XOF/month from 1 Jan 2023 (CNPS communiqué of 11/01/2023; Loi 99-477 art. 23) — 9384141 band, 58211 label, verification figures (3 750 / 563 / 2 250; on-cost 70 063, AM rounded to the whole franc per CCG §1.5). No structural change.

**v1.1 changelog — incorporates the dev-team feedback loop (this is the whole point of the project):**
1. **[NEW] Special employee categories** — intern, apprentice, first-employment exemption, senior officer/dirigeant-assimilé (Mohit review notes #1, #2, #5). This was the largest gap class in v1.0.
2. **[FIX] CMU** — corrected to the universal per-person contribution that does **not** fall to zero in an unpaid month (Mohit email #2).
3. **[FIX] Complementary pension cap** — corrected to the two-legged "10% of taxable pay OR 320,000 XOF, whichever is **lower**" (Mohit email #3, confirmed against DGI published reference; this is the same mechanism as the dev's CT-A-620 "private pension capping 320,000").
4. **[FIX] RICF** — single/divorced parent with a disabled child now **combines** (1.5 + 1.0 = 2.5 parts, Mohit email #4); and the design now mandates full-combination-matrix validation, not spot-test (Mohit review notes #3).
5. **[FIX] Unpaid leave** — per-branch behaviour (CNPS zero base / CMU still owed), replacing the earlier blanket rule (Mohit email #1, review notes #6).
6. **[STILL BLOCKED]** Severance/retirement ITS mechanism — unchanged, still awaiting Mohit's confirmation (see Part 6 #4b). This is the one item the design cannot close without him.

**Status:** Updated with all resolvable feedback. One item (ITS-on-termination mechanism) remains blocked on Mohit. A dev production design now exists (CT-A-620) — see the separate comparison document.

---

## Part 0 — Design Shape Decisions

**D1 — Two independent bases, no cascade.** ITS and CNPS are computed from the *same* gross figure in parallel, not in sequence. CNPS employee contributions are **never** subtracted from the ITS base (the reform-defined base is "total des rémunérations"). This is the single most important shape decision — get it backwards and every downstream figure is wrong (the CCG's own "F18 trap" warning).

**D2 — ITS is a pure monthly Differential, not annualised.** No year-to-date, no projection, no cumulative method. Each month is one independent `Differential` regulation on that month's gross. This is architecturally simpler than Chad or Canada — there is no factor-A annualisation step at all.

**D3 — RICF is a post-tax credit, not a base-reducing quotient.** Modelled as `_post_formula` against `$band_amount_raw` from the Differential regulation, floored at 0. Never touches the base.

**D4 — The four SMIG-multiple-capped premiums (panier, salissure, tenue, outillage) use the credit-side negative-intermediate pattern.** Each excluded amount is posted to the credit side of a debit-type intermediate, goes negative, and is included directly in both the ITS and CNPS taxability matrices — it subtracts automatically. This is more idiomatic than a `MAX(0, excess)` formula and matches the convention established elsewhere in the KB. Critically, the CCG's own Module 4.2 table shows these four premiums get the **same** cap applied to **both** ITS and CNPS — one credit intermediate serves both matrices.

**D5 — Overtime is five distinct earning-series wage types, not one.** Per "work on series, not individual pay elements": each statutory band (see Part 6, Resolution Log #1) is its own pay element, priced by the payroll engine from hours already bucketed by band. Bucketing weekly hours into the five bands is a time-and-attendance function upstream of payroll — the engine receives monthly totals per band and prices each (see Open Items).

**D6 — CE (employer expat tax) is a flag-driven binary rate on one regulation, not two.** `$hr.personnel_type` gates 0%/9.2% on the same base; no need for separate LOC/EXP regulations.

**D7 — Statutory severance/retirement indemnities are walled off from the earnings series entirely**, not included-then-exempted. They never enter `58201` (Total Gross). This is cleaner than a matrix exclusion because they are a genuinely different payment type (indemnité, not salaire) under Décret 2017-210 — matching how the WTC already treats them (CI-TX-03 with a flat "No" on every CNPS column, including for any excess). Only the *excess over the statutory formula* is ordinary ITS-taxable salary. *(Originally this note also said the excess is never CNPS-sociable, following the WTC's coding — that's since been revised. Part 6 #4 has the current position: excess defaulted to CNPS-sociable, pending an actual ruling. Treat Part 6 as current wherever it and this note disagree.)*

**D8 — BIK is valued once, feeds both bases equally.** No floor/ceiling distinction between ITS and CNPS treatment of a benefit in kind — same administrative-scale value goes into both (CCG 7.2, 4.6).

**D10 — Special employee categories are modelled as base-modifying regulations, gated on `$hr.employee_category`** *(v1.1, closes Mohit review notes #1/#2/#5 — the largest gap class in v1.0).* Four distinct treatments, each touching a *different* base, so none can be folded into a single generic rule:
- **Intern (stagiaire):** distinct **CNPS base** treatment — the CCG documents intern relief affecting the contribution base (per the dev's CT-A-620, a DGI capping with floor/ceiling 450,000/1,800,000 and a YTM capping). Modelled as reg `9384161`.
- **Apprentice (apprenti):** distinct **employer-wage-tax base** treatment (separate from intern's CNPS-base relief — Mohit is explicit these hit different bases). Reg `9384171`.
- **First-employment exemption:** a **separate** relief tied to the employee's first period of employment, distinct from intern relief (Mohit review notes #2 — this was a genuinely new item, not previously in the design). Anchored to `$hr.first_employment_start_date`, not birth date. Reg `9384181`.
- **Senior officer / dirigeant-assimilé:** distinct **CNPS treatment** for certain senior company officers (Mohit review notes #5). Reg `9384191`.

**D11 — Unpaid leave behaves per-CNPS-branch, not by a blanket rule** *(v1.1, Mohit email #1 + review notes #6).* On a fully-unpaid month (`$hr.unpaid_leave_full_month`):
- **CNPS pension + PF/AM/AT-MP:** zero salary → zero base → zero contribution; **no separate nil declaration**. The employee stays on the annual DISA at zero (omission applies only to actual *termination* — a suspended contract is not a closed one).
- **CMU:** **still owed.** It is a universal per-person contribution (~1,000 XOF/month total), not salary-linked, so it does **not** drop to zero with the other branches. This is why CMU (reg `9384151`/`9384341`) must not inherit the SMIG-floor/zero-base behaviour of the pension branch.

**D12 — Ordinal blocks:** 11–90 gross assembly & CNPS-exemption credits · 101–190 CNPS · **161–191 special employee categories** · 201–290 ITS · 301–390 employer contributions · 401–460 overtime · 501–560 termination · 601–650 BIK · 901+ net pay/post-tax.

---

## Part 1 — Flags (HRB-layer inputs)

| Flag | Type | Source | Drives |
|---|---|---|---|
| `$hr.personnel_type` | LOC / EXP | DD (Personnel Type) | CE rate (0%/9.2%) — reg `9384351` |
| `$hr.marital_status` | Célibataire/Marié/Divorcé/Veuf | DD | RICF parts — reg `9384231` |
| `$hr.dependent_children_count` | integer | DD | RICF parts (+0.5/child) |
| `$hr.disabled_dependent_children_count` | integer | DD | RICF parts (+1.0/child) |
| `$hr.atmp_risk_rate` | 2.0–5.0% | DD, employer-level (sector-notified at CNPS affiliation) | reg `9384331` |
| `$hr.cmu_insured_count` | integer, default 1 | DD | CMU flat charges — regs `9384151`/`9384341` |
| `$hr.employee_category` | ORDINARY / INTERN / APPRENTICE / SENIOR_OFFICER | DD | special-category regs `9384161`–`9384191` |
| `$hr.first_employment_flag` | boolean | DD (declared) | first-employment exemption — reg `9384201`(new) |
| `$hr.first_employment_start_date` | date | DD | anchors the first-employment exemption window |
| `$hr.unpaid_leave_full_month` | boolean | derived (zero gross for the period) | per-branch unpaid-leave behaviour (Part 0 D12) |
| `$hr.benefit_in_kind_type` | LOG/VEH/DOM/EAU/ELEC/TEL (multi) | DD (Benefit in Kind Type(s)) | BIK regs `9384601`–`9384641` |
| `$hr.complementary_pension_enrolled` | boolean | HR-system (enrolment doc) | gates reg `9384212` |
| `$hr.complementary_pension_period_amount` | amount/period | HR-system | input to reg `9384212` |
| `$hr.transport_allowance_period_amount` | amount/period | HR-system | input to reg `9384031` |
| `$hr.transport_zone` | ABIDJAN / BOUAKE / INTERIEUR | HR-system (employee's work locality) | selects the transport exemption ceiling — reg `9384031` |

HRB inputs stay strictly separate from the payroll-engine calculation layer below — these flags and master-data fields are never referenced inside a band formula except as lookup keys.

---

## Part 2 — Intermediate Accounts Register

| Account | Name | Type |
|---|---|---|
| 58201 | Total Gross Remuneration (Σ Earning-category series) | Debit |
| 58202 | Hourly SMIG Rate (= 75 000 ÷ 173.33) | Debit (reference) |
| 58203 | Transport CNPS/ITS-Exempt Credit | Debit, credit-side posting → negative |
| 58204 | Prime de Panier CNPS/ITS-Exempt Credit | Debit, credit-side posting → negative |
| 58205 | Prime de Salissure CNPS/ITS-Exempt Credit | Debit, credit-side posting → negative |
| 58206 | Indemnité de Tenue CNPS/ITS-Exempt Credit | Debit, credit-side posting → negative |
| 58207 | Prime d'Outillage CNPS/ITS-Exempt Credit | Debit, credit-side posting → negative |
| 58208 | CNPS Contributory Base, pre-floor (58201 − Σ58203:58207) | Debit |
| 58209 | CNPS Contributory Base, SMIG-floored ("Assiette CNPS") | Debit |
| 58210 | CNPS Pension Base (58209, ceiling 3 375 000) | Debit |
| 58211 | CNPS PF/AM/AT-MP Shared Base (58209, ceiling 75 000) | Debit |
| 58212 | Complementary-Pension Pre-Tax Credit (ITS-only, cap 10% of 58201) | Debit, credit-side posting → negative |
| 58213 | ITS Taxable Base (58201 − Σ58203:58207 − 58212) | Debit |
| 58214 | RICF Parts | Debit (reference) |
| 58215 | Gross ITS / Impôt Brut (Differential output) | Debit |
| 58216 | RICF Credit Amount | Debit |
| 58217 | Net ITS | Debit |
| 58218 | Overtime Hourly Base Rate (monthly base salary ÷ 173.33) | Debit (reference) |
| 58219 | Severance — Statutory Amount (30/35/40% banded) | Debit |
| 58220 | Retirement Indemnity — Statutory Amount (banded, capped 25×SMIG) | Debit |
| 58221 | BIK — Logement + Mobilier | Debit |
| 58222 | BIK — Eau | Debit |
| 58223 | BIK — Électricité | Debit |
| 58224 | BIK — Domesticité | Debit |
| 58225 | BIK — Véhicule | Debit |
| 58226 | Net Pay | Debit |
| 58227 | CNPS Pension — Employee Deduction Amount (58210 × 6.30%, distinct from the base) | Debit |
| 58228 | CMU — Employee Deduction Amount (flat 500 × `$hr.cmu_insured_count`) | Debit |
| 58229 | Post-Tax Garnishment Amount | Debit |

*(Added 58227–58229 during the second review pass — a systematic sweep found the Net Pay formula and reg 9384131 both referencing deduction amounts by placeholder text or an unregistered number instead of a real account. Split the BIK range into five explicit rows for the same reason: the original 58221–58225 range relied on matching list order against Part 4's regulation order, which is implicit and breaks silently if either list is ever reordered.)*

---

## Part 3 — Regulation Sequence

| Ord. | ID | Name | Tax Group | Tax Rule Group | Taxation Type |
|---|---|---|---|---|---|
| 11 | 9384011 | Total Gross Remuneration (series sum) | — | `_simple_tax` | Flat |
| 21 | 9384021 | Hourly SMIG Rate | — | `_post_formula` | Formula |
| 31 | 9384031 | Transport Allowance — CNPS/ITS-Exempt Credit | Social Security | `_post_formula` | Formula |
| 41 | 9384041 | Prime de Panier — CNPS/ITS-Exempt Credit (≤3× hourly SMIG) | Social Security | `_post_formula` | Formula |
| 51 | 9384051 | Prime de Salissure — CNPS/ITS-Exempt Credit (≤13×) | Social Security | `_post_formula` | Formula |
| 61 | 9384061 | Indemnité de Tenue — CNPS/ITS-Exempt Credit (≤7×) | Social Security | `_post_formula` | Formula |
| 71 | 9384071 | Prime d'Outillage — CNPS/ITS-Exempt Credit (≤10×) | Social Security | `_post_formula` | Formula |
| 101 | 9384101 | CNPS Contributory Base (pre-floor) | Social Security | `_post_formula` | Formula |
| 111 | 9384111 | CNPS Contributory Base (SMIG floor 75 000) | Social Security | `_post_formula` | Formula |
| 121 | 9384121 | CNPS Pension Base (ceiling 3 375 000) | Social Security | `_table` | Flat |
| 131 | 9384131 | CNPS Pension — Employee (6.30%) | Social Security | `_simple_tax` | Flat |
| 141 | 9384141 | CNPS PF/AM/AT-MP Shared Base (ceiling 75 000) | Social Security | `_table` | Flat |
| 151 | 9384151 | CMU — Employee (universal per-person; unpaid-month-persistent) | Social Security | `_simple_tax` | Flat |
| 161 | 9384161 | Intern (stagiaire) — CNPS base capping (floor/ceiling + YTM) | Social Security | `_post_formula` | Formula |
| 171 | 9384171 | Apprentice (apprenti) — employer-wage-tax base treatment | Income Tax | `_post_formula` | Formula |
| 181 | 9384181 | First-Employment Exemption (window from hire date) | Income Tax | `_post_formula` | Formula |
| 191 | 9384191 | Senior Officer / Dirigeant-Assimilé — CNPS treatment | Social Security | `_post_formula` | Formula |
| 201 | 9384201 | Sector AT/MP Rate (client-config passthrough) | Social Security | `_fixed` | Flat |
| 212 | 9384212 | Complementary Pension — Pre-Tax Credit (cap: LOWER of 10% taxable or 320,000) | Income Tax | `_post_formula` | Formula |
| 213 | 9384213 | ITS Taxable Base | Income Tax | `_post_formula` | Formula |
| 221 | 9384221 | Gross ITS (Impôt Brut) — 6-bracket monthly Differential | Income Tax | `_simple_tax` | **Differential** |
| 231 | 9384231 | RICF Parts (from marital status + children) | Income Tax | `_post_formula` | Formula |
| 241 | 9384241 | RICF Credit Amount (lookup by parts) | Income Tax | `_table` | Flat |
| 251 | 9384251 | Net ITS (Impôt Brut − RICF, floor 0) | Income Tax | `_post_formula` | Formula |
| 301 | 9384301 | CNPS Pension — Employer (7.70%) | Social Security | `_simple_tax` | Flat |
| 311 | 9384311 | CNPS Prestations Familiales — Employer (5.00%) | Social Security | `_simple_tax` | Flat |
| 321 | 9384321 | CNPS Assurance Maternité — Employer (0.75%) | Social Security | `_simple_tax` | Flat |
| 331 | 9384331 | CNPS AT/MP — Employer (2–5% sector rate) | Social Security | `_simple_tax` | Flat |
| 341 | 9384341 | CMU — Employer (flat 500/insured person) | Social Security | `_simple_tax` | Flat |
| 351 | 9384351 | Contribution à la charge des employeurs (CE) — 0%/9.2% by personnel type | Income Tax | `_simple_tax` | Flat |
| 361 | 9384361 | Contribution Nationale — Employeur (CN, 1.20%) | Income Tax | `_simple_tax` | Flat |
| 371 | 9384371 | Taxe d'Apprentissage — FDFP (0.40%) | Income Tax | `_simple_tax` | Flat |
| 381 | 9384381 | Taxe FPC — FDFP (1.20%) | Income Tax | `_simple_tax` | Flat |
| 401 | 9384401 | Overtime Hourly Base Rate | — | `_post_formula` | Formula |
| 411 | 9384411 | Overtime — 41st–46th hour (+15%) | — | `_simple_tax` | Flat |
| 421 | 9384421 | Overtime — beyond 46th hour (+50%) | — | `_simple_tax` | Flat |
| 431 | 9384431 | Overtime — night, weekday (+75%) | — | `_simple_tax` | Flat |
| 441 | 9384441 | Overtime — Sunday/holiday, **daytime** (+75%) *(new — closes MAJOR-1)* | — | `_simple_tax` | Flat |
| 451 | 9384451 | Overtime — Sunday/holiday, **night** (+100%) | — | `_simple_tax` | Flat |
| 501 | 9384501 | Indemnité de Licenciement — statutory (30/35/40% banded) | — | `_post_formula` | Formula |
| 511 | 9384511 | Indemnité de Licenciement — excess over statutory (taxable) | — | `_simple_tax` | Flat |
| 521 | 9384521 | Indemnité de Départ à la Retraite — statutory (banded, cap 25×SMIG) | — | `_post_formula` | Formula |
| 531 | 9384531 | Indemnité de Départ à la Retraite — excess over cap (taxable) | — | `_simple_tax` | Flat |
| 541 | 9384541 | Indemnité Compensatrice de Préavis | — | `_simple_tax` | Flat |
| 551 | 9384551 | Indemnité Compensatrice de Congé | — | `_post_formula` | Formula |
| 601 | 9384601 | BIK — Logement + Mobilier (room-graded, arrêté 1028) | — | `_post_formula` | Formula |
| 611 | 9384611 | BIK — Eau (room-graded 10k–60k + 30k if pool; reconcile vs. invoice-based alternative) | — | `_post_formula` | Formula |
| 621 | 9384621 | BIK — Électricité (room-graded 10k–70k + 20k/AC unit) | — | `_post_formula` | Formula |
| 631 | 9384631 | BIK — Domesticité (gardien 50k / gens de maison 60k / cuisinier 90k) | — | `_fixed` | Flat |
| 641 | 9384641 | BIK — Véhicule (personal-use only; genuine service vehicle excluded) | — | `_fixed` | Flat |
| 901 | 9384901 | Post-Tax Garnishment (priority-ordered: maintenance > public claims > general creditors) | — | `_post_formula` | Formula |
| 911 | 9384911 | Net Pay | — | `_post_formula` | Formula |

**52 regulations** (v1.1: 48 from v1.0 + 4 new special-employee-category regs 9384161/171/181/191 incorporating Mohit's review notes #1/#2/#5). For comparison: Chad's clean-room design had 24; the dev's CI production design (CT-A-620) is a leaner 18-reg core (see the separate comparison — the dev omits overtime, termination, and detailed BIK that this design models, while this v1.1 now also covers the interns/first-employment/senior-officer categories the dev design includes). None of the 52 is padding — each is a genuinely distinct statutory rule.

---

## Part 4 — Regulation Articles (detailed)

Straightforward flat-rate pass-throughs (`9384131/301/311/321/331/341/351/361/371/381/151/411/421/431/441/451`) share one shape — a single band, rate on one side, no formula — so they're given as compact band rows. The differential tax, RICF, the four exemption credits, and termination get full treatment since that's where the design decisions live.

### 9384011 — Total Gross Remuneration
**Form data:** Tax Group — · Tax Rule Group `_simple_tax` · Taxation Type `Flat`
**Matrix:** Sum of every wage type flagged `Earning` in the WTC (base salary, sursalaire, seniority bonus, overtime series 9384411–9384451, gratification/13th-month, commissions, discretionary bonuses, préavis/congé indemnities, BIK series 9384601–9384641). **Excludes** the two severance/retirement regs (9384501–9384531 statutory legs) per D7, and excludes family allowances and genuine expense reimbursements (never enter the series at all).
**Band:** unitAccount → 58201, employeeRate 100, debitAccount 58201.

### 9384021 — Hourly SMIG Rate
**Formula:** `DIVIDE(75000; 173.33)` = **432.69 XOF/hour**. Reference value consumed by regs 9384041–9384071 and 9384401–9384451.
Verified independently: 75 000 ÷ (40h × 52 ÷ 12) = 75 000 ÷ 173.33 = 432.69.

### 9384031 — Transport Allowance CNPS/ITS-Exempt Credit
**Formula:** `MULTIPLY(-1; MIN($hr.transport_allowance_period_amount; TRANSPORT_EXEMPT_CAP[$hr.transport_zone]))`, posted credit-side to 58203.
**Resolved (was open item):** the DGI-recognised ceiling is zone-based, not a single national figure — confirmed via the implementing arrêté (Ministre de l'Emploi et de la Protection sociale, 30 Jan 2020) plus a current (2026) practitioner source giving the identical figures:

| Zone | Monthly exempt ceiling (XOF) |
|---|---|
| District d'Abidjan | 30 000 |
| Bouaké | 24 000–25 000 *(two sources disagree by 1 000; Abidjan and Intérieur are consistent everywhere I found)* |
| Intérieur (all other towns) | 20 000 |

Both CNPS and ITS use the same ceiling (CPS art. 23 caps it at "une fois le montant exonéré par l'administration fiscale" — i.e., the CNPS limit is defined as exactly the DGI figure, not a separately-set number). Recommend confirming the Bouaké figure with RA before go-live; Abidjan and Intérieur are solid.

### 9384041 — Prime de Panier CNPS/ITS-Exempt Credit
**Formula:** `MULTIPLY(-1; MIN($panier_paid_this_period; MULTIPLY(3; 58202)))`, posted credit-side to 58204.
**Revised (was a design assumption, now corrected):** the Part 6 draft originally applied this cap per day paid. On further research this is wrong — a university-level Ivorian-law course document quoting CPS art. 23 directly gives "Prime mensuelle de salissure," "Indemnité mensuelle de tenue," "Prime mensuelle d'outillage," and "Indemnité mensuelle de transport" — the word **mensuelle** is in the name of every sibling cap. "Prime de panier" is the one line in that same list without it, which is a real, if narrow, textual difference — but a separate Labour Code decree (96-204, night work) ties the identical "3× hourly SMIG" figure to a *per-qualifying-night* entitlement (six consecutive hours worked). Weighing both: panier is very commonly paid as an ordinary monthly allowance (Module 13.5), not exclusively as the night-work entitlement, so I now read the CNPS exemption test itself as **monthly**, matching its siblings — the night-work decree is a separate, narrower rule (the statutory *amount owed* to night workers specifically) that happens to reuse the same multiplier, not the general exemption mechanism. Flagging this reasoning explicitly rather than asserting it quietly — it's a real judgment call, not a sourced certainty. Corrects WTC's current CI-TX-01 either way (see Resolution Log #2).

### 9384051 / 9384061 / 9384071 — Salissure / Tenue / Outillage Credits
Identical mechanism to 9384041, multipliers 13× / 7× / 10× respectively, all confirmed **monthly** by the same source (each is explicitly named "mensuelle"), posting credit-side to 58205/58206/58207. All three already match the WTC (CI-TX-03) — no correction needed, included here only for completeness of the series.

### 9384101 — CNPS Contributory Base (pre-floor)
**Formula:** `SUBTRACT(58201; ADD(58203; 58204; 58205; 58206; 58207))` → 58208. (Credits are already negative, so this is effectively 58201 plus four negative credits — same operation, engine-idiomatic form.)

### 9384111 — CNPS Contributory Base (SMIG-floored)
**Formula:** `IF(LESS(58208; 75000); 75000; 58208)` → 58209. Applies only to an effectively-employed worker for the period; a wholly-unpaid period produces no base at all (Module 8).

### 9384121 — CNPS Pension Base
**Band:** floorAmount — , ceilingAmount 3 375 000, unitAccount 58209 → debitAccount 58210. Taxation Type `Flat`, Tax Rule Group `_table` (band selects/caps, no differential).

### 9384131 — CNPS Pension, Employee
**Band:** incomeFrom 0, incomeTo — , employeeRate 6.30, unitAccount 58210, debitAccount 58227.
Verified: 600 000 × 6.30% = 37 800 (CCG Example 1, Module 3, Module 5, Module 12.1 — all four independently reproduce this figure).

### 9384141 — CNPS PF/AM/AT-MP Shared Base
**Band:** ceilingAmount 75 000, unitAccount 58209 → debitAccount 58211. One base intermediate feeds three separate employer-only regs (9384311/321/331) — no need to recompute the 75 000 cap three times.

### 9384151 — CMU, Employee
**Band:** Flat 500 XOF × `$hr.cmu_insured_count` (default 1), no base, no cap.
**v1.1 clarification (Mohit email #2):** CMU is a **universal per-person contribution**, not a salary-linked one. It is charged **regardless of gross pay** — including a fully-unpaid month (`$hr.unpaid_leave_full_month`), where the pension and PF/AM/AT-MP branches all fall to zero but CMU does **not**. The engine must therefore compute this reg independently of the CNPS base chain (58208/58209) — it never reads the SMIG-floored base and never zeroes with it. Employer side (9384341) is the matching 500; combined the CMU is ~1,000 XOF/person/month total, which reconciles to Mohit's "1,000 per person" figure (500 EE + 500 ER). *(Reconciliation note for RA: confirm whether the 1,000 is split 500/500 EE/ER as modelled here, or is a single 1,000 charge — the split is the design's current position.)*

### 9384161 — Intern (Stagiaire) CNPS Base Capping *(v1.1 — new, Mohit review notes #1)*
**Formula:** applies the DGI/CNPS intern capping to the contribution base — floor/ceiling bracketing plus a year-to-month capping, gated on `$hr.employee_category = INTERN`. Per the dev's CT-A-620 the capping uses floor/ceiling **450,000 / 1,800,000** with a YTM component (accounts 58101-analogue). The intern relief affects the **CNPS contribution base specifically** (distinct from the apprentice treatment, which hits a different base — Mohit is explicit on this). **[NEEDS-RA-CONFIRM]** the exact floor/ceiling and whether the capping is monthly or YTM — adopted from the dev design pending CCG-section confirmation.

### 9384171 — Apprentice (Apprenti) Employer-Wage-Tax Base *(v1.1 — new, Mohit review notes #1)*
**Formula:** adjusts the **employer-wage-tax base** (the CE/CN/TA/TFPC base, not the CNPS base) for apprentices, gated on `$hr.employee_category = APPRENTICE`. Mohit's note is explicit that intern relief and apprentice relief touch *different* bases — so this is a separate regulation from 9384161, not a shared category rule. **[NEEDS-RA-CONFIRM]** exact mechanism from the CCG apprentice section.

### 9384181 — First-Employment Exemption *(v1.1 — new, Mohit review notes #2)*
**Formula:** applies the first-period-of-employment exemption over a window anchored to `$hr.first_employment_start_date` (not birth date — per the anchoring lesson: countdown runs from the exemption start, not a demographic date), gated on `$hr.first_employment_flag`. This is a **distinct relief from the intern treatment** (Mohit flagged it as a separate CCG citation — it was genuinely absent from v1.0, not a duplicate of intern relief). **[NEEDS-RA-CONFIRM]** the exemption amount/duration and which base(s) it reduces, from the CCG legal-citations section.

### 9384191 — Senior Officer / Dirigeant-Assimilé CNPS Treatment *(v1.1 — new, Mohit review notes #5)*
**Formula:** applies the distinct CNPS treatment the CCG documents for certain senior company officers/assimilés, gated on `$hr.employee_category = SENIOR_OFFICER`. **[NEEDS-RA-CONFIRM]** the exact distinction (base, rate, or ceiling difference) from the CCG's senior-officer section.

### 9384201 — Sector AT/MP Rate
Client-config passthrough of `$hr.atmp_risk_rate` (2.0%–5.0%, notified by CNPS at affiliation). Feeds 9384331. Not itself a calculation — a rate lookup.

### 9384212 — Complementary Pension Pre-Tax Credit
**Formula (v1.1 — corrected, Mohit email #3):** `MULTIPLY(-1; MIN($hr.complementary_pension_period_amount; MIN(MULTIPLY(0.10; 58213_taxable); 320000)))`, posted credit-side to 58212, gated on `$hr.complementary_pension_enrolled`.
**The cap is two-legged:** the exempt amount is the **LOWER of** (a) 10% of monthly *taxable* remuneration **or** (b) 320,000 XOF flat. This is **not** two separate 10% limits (the "double cap" wording was ambiguous; Mohit resolved it against DGI's published reference). Note two things this fixes from v1.0: (1) the cap base is *taxable* remuneration, and since the 320,000 flat leg binds first for any salary above ~3.2M/month, the flat leg is the operative cap for high earners; (2) **this is the same mechanism as the dev's CT-A-620 "private pension capping 320,000"** — v1.0 modelled only the 10% leg and treated 320,000 as out of scope; they are one two-legged rule. **[RESOLVED — no longer commentary-sourced; DGI published reference per Mohit.]**

### 9384213 — ITS Taxable Base
**Formula:** `ADD(58201; 58203; 58204; 58205; 58206; 58207; 58212)` — gross plus the four SMIG-cap exemption credits plus the complementary-pension credit; all five are already posted as negative values (credit-side), so adding them is what subtracts them. *(Tightened during this review — an earlier draft subtracted a double-negation of 58212 instead of adding it like the other four; both are arithmetically equivalent, but the mixed pattern invited exactly the kind of error a straight ADD across all five avoids.)* **Deliberately excludes CNPS employee contributions** — this is the D1 shape decision made concrete. No professional-expense abatement, no 20% abatement (both abolished 2024).

### 9384221 — Gross ITS (Impôt Brut)
**Form data:** Tax Group `Income Tax` · Tax Rule Group `_simple_tax` (baseline — the progressive computation itself comes from Taxation Type) · Taxation Type **`Differential`**.
**Bands** (unitAccount 58213 throughout, all six rows in one regulation per the KB's Differential convention — no atomic Threshold/Base/Amount decomposition):

| incomeFrom | incomeTo | employeeRate |
|---|---|---|
| 0 | 75 000 | 0% |
| 75 001 | 240 000 | 16% |
| 240 001 | 800 000 | 21% |
| 800 001 | 2 400 000 | 24% |
| 2 400 001 | 8 000 000 | 28% |
| 8 000 001 | — | 32% |

Output → 58215. Verified against CCG Examples across Modules 3/6/9/12/13 (every one reproduces these six bands exactly on five different income levels).

### 9384231 — RICF Parts
**Formula:** table lookup on `$hr.marital_status` for the base parts, then `ADD(base_parts; MULTIPLY(0.5; $hr.dependent_children_count); MULTIPLY(1.0; $hr.disabled_dependent_children_count))`, capped at 5 via `MIN(...;5)`. Employer derogation (1 part default for a minor child not head-of-household) is a client-config override, not a formula branch. Output → 58214.

**v1.1 — combination rule made explicit (Mohit email #4):** a single/divorced parent with a disabled child **combines** the two additions — base 1.5 (single/divorced-parent status with ≥1 child) **+** 1.0 (disabled child) **= 2.5 parts**. The 0.5 single-parent bonus is **not** replaced by the 1.0 disabled-child part; they add. The `ADD(...)` structure above already produces this correctly as long as the base-parts lookup grants 1.5 for a single/divorced parent with children — the fix is ensuring the base-parts table encodes that 1.5, not that the parent status and disabled-child status are treated as mutually exclusive.

**⚠️ v1.1 — validation-method correction (Mohit review notes #3):** v1.0 validated RICF by **spot-testing common cases**, which Mohit flagged as insufficient — "a few combinations may not currently reconcile." **This regulation must be validated against the CCG's full "situation matrimoniale" combination matrix**, every marital-status × child-count × disability combination, not by sampling. The specific combinations to verify systematically: widowed (with/without children), single/divorced parent (with/without children), married (with/without children), each crossed with disabled-child counts. **[NEEDS-SYSTEMATIC-VALIDATION]** — the formula is believed correct but has not yet been run against the complete matrix; this is a build-blocking check before go-live, not a spot-test.

### 9384241 — RICF Credit Amount
**Band:** `_table` lookup on 58214 (parts) → monthly credit:

| Parts | Monthly credit (XOF) |
|---|---|
| 1 | 0 |
| 1.5 | 5 500 |
| 2 | 11 000 |
| 2.5 | 16 500 |
| 3 | 22 000 |
| 3.5 | 27 500 |
| 4 | 33 000 |
| 4.5 | 38 500 |
| 5 | 44 000 |

Output → 58216.

### 9384251 — Net ITS
**Formula:** `IF(LESS(SUBTRACT(58215;58216);0); 0; SUBTRACT(58215;58216))` → 58217. Uses `$band_amount_raw` from 9384221 (Tax Rule Group `_post_formula` reading the Differential's output), not `$employee_taxable_amount` — per the KB's authoritative distinction, this regulation is a formula step consuming the prior band's raw output, not summing a taxability matrix.

*(70+ pensioner 75% reduction and the 320 000 pension abatement are pension-only — out of scope for the active-employee core design; flagged in Part 6 as a scope note, not a gap, since this build targets active salaried employees.)*

### 9384301/311/321/331/341 — Employer CNPS contributions
| Reg | Rate | Base |
|---|---|---|
| 9384301 Pension (ER) | 7.70% | 58210 |
| 9384311 Prestations Familiales | 5.00% | 58211 |
| 9384321 Assurance Maternité | 0.75% | 58211 |
| 9384331 AT/MP | `$hr.atmp_risk_rate` (2–5%) | 58211 |
| 9384341 CMU (ER) | flat 500/head | — |

All verified against CCG Examples (600 000 case: 46 200 / 3 750 / 563 / 2 250 (@3%) / 500 — reproduced identically in Modules 3, 5, and 12.1).

### 9384351 — Contribution à la charge des employeurs (CE)
**Formula:** `IF(EQUALS($hr.personnel_type;'EXP'); MULTIPLY(0.092; 58201); 0)`. Verified: expat on 2 250 000 → 207 000 (Module 12, Example 5); local → 0 throughout.

### 9384361/371/381 — CN / Taxe d'Apprentissage / TFPC
Flat 1.20% (9384361, CN) / 0.40% (9384371, Taxe d'Apprentissage) / 1.20% (9384381, TFPC) on 58201, unconditional (both local and expatriate). Together with CE these total the "contribution employeurs": 2.8% of gross for local, 12.0% for expatriate — verified in every employer-on-cost table across the CCG.

### 9384401 — Overtime Hourly Base Rate
**Formula:** `DIVIDE($base_salary_period; 173.33)` → 58218. Premium base is *salaire réel excluding the indemnité d'expatriation* (CCI art. 51) — the expatriation allowance wage type is explicitly excluded from this formula's input even though it's included in the ITS/CNPS series elsewhere.

### 9384411–9384451 — Overtime, five bands
All `_simple_tax` / Flat, rate on the unit account fed by 58218 × hours-in-band (hours arrive pre-bucketed from time & attendance — see Open Items):

| Reg | Band | Rate |
|---|---|---|
| 9384411 | 41st–46th weekly hour, day | 115% |
| 9384421 | Beyond 46th weekly hour, day | 150% |
| 9384431 | Night (21h–5h), weekday | 175% |
| 9384441 | Sunday/public holiday, **daytime** | 175% |
| 9384451 | Sunday/public holiday, **night** | 200% |

This five-band structure — not the WTC's current four-band structure — is the design's position. Full basis in Part 6, Resolution Log #1.

### 9384501 — Indemnité de Licenciement, statutory
**Formula:** for each service-year band, `years_in_band × band_rate × average_monthly_global_salary_12mo`, summed:

| Years band | Rate |
|---|---|
| 1st–5th year | 30% |
| 6th–10th year | 35% |
| Beyond 10th year | 40% |

Output → 58219. **Never enters 58201** (D7) — walled off from both ITS and CNPS bases entirely, matching the WTC's existing CI-TX-03/"No"-on-all-CNPS-columns coding. Verified: 13-year case → 450 000 + 525 000 + 360 000 = 1 335 000 (Module 9, Module 12 redundancy example — both reproduce this exactly).

### 9384511 — Indemnité de Licenciement, excess over statutory
**Formula:** `MAX(0; contractual_severance_paid − 58219)`.
**Design default revised following research — still not a sourced rule, but no longer an unweighted guess either.** No CNPS circular, doctrine, or case law resolves whether the excess is CNPS-sociable; the Code de Prévoyance Sociale art. 23 text only carves out expense-reimbursement indemnities, and the CNPS's own gloss states everything else ("toutes les autres primes, gratifications ou indemnités") is contributory — which cuts against a blanket exclusion of an above-formula excess. Two Ivorian secondary sources conflict directly (one implies only the legally-capped amount is excluded; a named Abidjan accounting firm's material implies the whole indemnité is excluded regardless of amount), and French/Senegalese analogues (non-authoritative for CI, but structurally similar regimes) treat the excess as sociable. **Revised default: the excess is CNPS-sociable**, reversing the original per-WTC inference — implemented behind a configurable flag (`$config.severance_excess_cnps_treatment`) rather than hard-coded, given the genuine uncertainty. Do not present this as settled in front of Mohit; present it as the conservative default pending a CNPS ruling or a Big-Four Abidjan opinion.

**Separate, newly-surfaced conflict — the ITS side of this same regulation may also be wrong, not just the CNPS side.** The design's ITS treatment — exempt up to the full statutory formula (58219), with the excess taxed as ordinary salary through the standard progressive brackets — matches the CCG's own Module 9 narrative, and mechanically runs the excess in as a second, ITS-only gross variable (taxable=Yes/sociable=per the flag above) feeding into 9384213 alongside 58201, rather than through 58201 itself. But the research turned up a citation (a payroll vendor's Côte d'Ivoire tax summary, citing DGI Note n°2410/SEPMBPE/DGI-DLCD of 20 June 2018 and an administrative note of 12 April 2022) describing a **completely different mechanism**: a small fixed ITS-exempt amount (60 000 XOF, not the full statutory formula) with everything above that taxed at a **flat 50% rate**, not the progressive brackets. These cannot both be right. I have not verified which is correct — this wasn't the question I sent to research, it surfaced as a side effect, and I'm flagging it rather than picking one. **This is now the single highest-priority open item in the whole design** — if the 60 000/flat-50% mechanism is the real one, this regulation's ITS formula (and the CCG's Module 9 narrative it's built on) needs to change, not just get a footnote.

### 9384521/531 — Indemnité de Départ à la Retraite
Identical 30/35/40% banded formula to 9384501, additionally capped at **25 × SMIG = 1 875 000 XOF** (2026 terms) per CCI art. 40. Same walled-off treatment and same excess/taxable split as severance — and the same two open questions apply here too: the CNPS-excess default revision (below) and the newly-surfaced ITS-mechanism conflict (#4b in Part 6) both cover this regulation as well as 9384511, since both indemnités are governed by the same Décret 2017-210 architecture and neither piece of research distinguished between them.

### 9384541 — Indemnité Compensatrice de Préavis
**Formula:** notice-period length (Décret 96-200, by category/seniority) × average remuneration. Fully taxable and fully sociable — enters 58201 directly (ordinary salary treatment, unlike severance).

### 9384551 — Indemnité Compensatrice de Congé
**Formula:** `MULTIPLY(accrued_leave_days; DIVIDE(monthly_remuneration; 26))`. Fully taxable and sociable. Verified: 7 months × 2.2 days/mo = 15.4 days × (200 000/26) = 118 461 (Module 8 and Module 9, both reproduce this exactly, including the 1/12-method cross-check for temporary hires).

### 9384601 — BIK Logement + Mobilier
**Resolved (was open item).** Arrêté n°1028 grades both house and furniture by room count (professional-source-verified via a payroll vendor's Côte d'Ivoire tax summary citing the arrêté directly; not primary-text-verified):

| Rooms | House (XOF) | Furniture (XOF) |
|---|---|---|
| 1 | 60 000 | 10 000 |
| 2 | 80 000 | 20 000 |
| 3 | 160 000 | 40 000 |
| 4 | 300 000 | 60 000 |
| 5 | 480 000 | 80 000 |
| 6 | 600 000 | 100 000 |
| 7+ | 800 000 | 150 000 |

**Formula:** `ADD(HOUSE_SCALE[room_count]; FURNITURE_SCALE[room_count])`. Matches the CCG's own framing that the forfait applies only where no actual invoice exists — a temporary hotel stay still uses real cost, per CCG 7.2.

### 9384611 — BIK Eau
**Partially resolved — two presentations found, not yet reconciled.** The same source that gave the housing grid also grades water by room count (10 000–60 000 XOF across the 1–7+ room bands) plus the already-confirmed +30 000 XOF if the dwelling has a pool. This conflicts with the earlier finding of "invoice cost + flat 30 000 XOF forfait (+30 000 if pool)." Both could be real — e.g. the room-graded figure as the default forfait and the invoice-based version as the alternative when the employer pays a metered bill directly (mirroring the housing hotel-cost exception) — but that's my inference, not a sourced reconciliation. **Design uses the room-graded table as primary** (it's part of the same integrated arrêté 1028 grid as housing/furniture/electricity, which is more internally consistent) with the invoice-based version flagged as a fallback pending confirmation.

### 9384621 — BIK Électricité
**Resolved, refines the earlier finding.** Same grid, room-graded 10 000–70 000 XOF, **plus** the already-confirmed +20 000 XOF per air-conditioning unit or air-conditioned room. **Formula:** `ADD(ELEC_SCALE[room_count]; MULTIPLY(20000; ac_unit_count))`.

### 9384631 — BIK Domesticité
**Resolved (was open item).** Not one flat forfait — three category amounts:

| Category | Monthly XOF |
|---|---|
| Gardien / jardinier (security man / gardener) | 50 000 |
| Gens de maison / caretaker (household staff) | 60 000 |
| Cuisinier (cook) | 90 000 |

**Formula:** `SUMPRODUCT(DOMESTIC_STAFF_SCALE[category]; headcount_per_category)`.

**Téléphone and third-party gardiennage — removed from this regulation, they were never a forfait.** The research resolved this by explaining the absence: home telephone costs and an invoiced third-party security-company service are both valued at **real cost under CGI art. 118**, same as any BIK not enumerated in arrêté 1028's list — there's no missing number to find because none exists by design. An individual security guard employed directly as domestic staff is the 50 000 XOF gardien line above; a security company's invoice is not. Neither needs a dedicated valuation regulation — they flow through the general real-value BIK mechanism (D8) directly.

### 9384641 — BIK Véhicule
Unchanged: flat, personal-use only; `IF(genuine_service_vehicle;0;taxable_value)`.

Verified mechanism (not the exact figures, at the time) via CCG Module 7.2 and Module 12 Example 5 (200 000 housing benefit correctly raising both the ITS base and the CNPS base by the same 200 000) — the actual grid above is new since that check; worth re-running Example 5 once room count is known for that scenario, though the CCG's example intentionally used a round number rather than a real room-graded value, so no contradiction to resolve there.

### 9384901 — Post-Tax Garnishment
**Resolved (was open item):** found the actual implementing text, **Décret n°2014-370 du 18 juin 2014**. Output → 58229. Two distinct regimes, not one:

| Instrument | Basis (art. 2: monthly gross incl. accessories, minus source-withheld taxes, expense-representative indemnities, family-charge benefits, and indemnities declared unseizable) | Cap |
|---|---|---|
| Court-ordered seizure (saisie-arrêt — the general creditor/maintenance case) | Same base | Flat **33%** (art. 3) |
| Voluntary wage assignment / bank-loan repayment (cession de rémunération) | Same base | Graduated: 35% (≤200k) / 38% / 42% / 45% / 48% / 52% / 55% / 57% (>2M) (art. 4) |

**Formula:** `MULTIPLY(0.33; garnishment_base)` for court-ordered seizure; `MULTIPLY(assignment_band_rate; garnishment_base)` for voluntary assignment/loan, band-selected from the table above.
**Still open:** the CCG's claim that *pension alimentaire* (maintenance) can exceed the normal 33% ceiling wasn't corroborated by this décret's text — art. 3 states 33% as *the* maximum for court-ordered seizure without carving out maintenance specifically. Either maintenance's priority comes from a different legal basis entirely (Family Code enforcement mechanisms, plausible under Francophone civil-law tradition) or the CCG's general statement doesn't hold precisely for this décret. Recommend confirming with RA before treating maintenance as able to exceed 33% in the engine.

### 9384911 — Net Pay
**Formula:** `SUBTRACT(58201; 58227; 58228; $hr.complementary_pension_period_amount; 58217; 58229)`, i.e. `Gross − CNPS employee pension deduction − CMU employee deduction − complementary-pension contribution (full amount, not the capped 58212 credit) − Net ITS − post-tax garnishment`.
**Fixed during this review — genuine gap, not cosmetic.** The formula previously omitted the complementary-pension term entirely. It correctly reduced the *ITS base* via 58212/58213, but never actually took the contribution out of net pay — for any employee using that benefit, net pay would have come out overstated by the full contribution amount. Caught by actually re-deriving CCG Module 12 Example 3 by hand (below) rather than trusting the earlier validation set, which happened to only cover scenarios where this term is zero. Note the term is the **full** contribution amount, not the 10%-capped 58212 credit — if a contribution exceeds the cap, the excess still leaves net pay even though it gets no ITS relief.

---

## Part 5 — Worked Validation

Ran the full regulation sequence against the CCG's own verified worked examples. The original pass (Validations 1–2) only exercised the core gross→CNPS→ITS→net-pay spine and the expatriate CE branch — roughly a third of the 48 regulations. This review adds three more (3–5) specifically to cover blocks the first pass never touched: the complementary-pension credit, the entire termination block, overtime, and the garnishment mechanism. Validation 3 is what caught the Net Pay formula gap above.

### Validation 1 — CCG Module 12, Example 1 (local, 600 000 XOF, 3 parts)
| Step | Reg(s) | Design output | CCG figure | Match |
|---|---|---|---|---|
| Gross (58201) | 9384011 | 600 000 | 600 000 | ✅ |
| CNPS base (58209/58210) | 9384101/111/121 | 600 000 (below both floor concern and ceiling) | 600 000 | ✅ |
| CNPS pension EE | 9384131 | 37 800 | 37 800 | ✅ |
| CMU EE | 9384151 | 500 | 500 | ✅ |
| ITS base (58213) | 9384213 | 600 000 (no exemptions/comp. pension in this case) | 600 000 | ✅ |
| Gross ITS (58215) | 9384221 | 102 000 | 102 000 | ✅ |
| RICF (58216) | 9384231/241 | 22 000 (3 parts) | 22 000 | ✅ |
| Net ITS (58217) | 9384251 | 80 000 | 80 000 | ✅ |
| Net pay (58226) | 9384911 | 600 000 − 38 300 − 80 000 = **481 700** | 481 700 | ✅ |
| Employer on-cost | 9384301/311/321/331/341/361/371/381/351 | 46 200+3 750+563+2 250+500+7 200+2 400+7 200+0 = **70 063** | 70 063 | ✅ |

### Validation 2 — CCG Module 12, Example 5 (expatriate, 2 000 000 cash + 250 000 housing BIK, 3 parts)
| Step | Design output | CCG figure | Match |
|---|---|---|---|
| Gross incl. BIK (58201) | 2 250 000 | 2 250 000 | ✅ |
| CNPS pension EE (9384131) | 141 750 | 141 750 | ✅ |
| Gross ITS (9384221) | 492 000 | 492 000 | ✅ |
| RICF (3 parts) | 22 000 | 22 000 | ✅ |
| Net ITS (9384251) | 470 000 | 470 000 | ✅ |
| CE @ 9.2% (9384351, EXP branch) | 207 000 | 207 000 | ✅ |
| Net cash pay (9384911) | 2 000 000 − 142 250 − 470 000 = **1 387 750** | 1 387 750 | ✅ |
| Employer total on-cost | 449 875 | 449 875 | ✅ |

### Validation 3 — CCG Module 12, Example 3 (900 000 gross, complementary pension 45 000, 2.5 parts) — new this review
This is the scenario that exposed the Net Pay gap above; shown with the fix applied.
| Step | Reg(s) | Design output | CCG figure | Match |
|---|---|---|---|---|
| Comp. pension credit (58212) | 9384212 | MIN(45 000; 90 000) = **−45 000** | (45 000 excluded, within 10% cap) | ✅ |
| ITS base (58213) | 9384213 | 900 000 − 45 000 = **855 000** | 855 000 | ✅ |
| Gross ITS (58215) | 9384221 | **157 200** | 157 200 | ✅ |
| RICF (2.5 parts) | 9384241 | 16 500 | 16 500 | ✅ |
| Net ITS (58217) | 9384251 | **140 700** | 140 700 | ✅ |
| CNPS pension EE | 9384131 | 900 000 × 6.30% = **56 700** | 56 700 | ✅ |
| Net pay (58226) | 9384911, **with the fix** | 900 000 − 56 700 − 500 − 45 000 − 140 700 = **657 100** | 657 100 | ✅ (would have been 702 100 — wrong by exactly 45 000 — under the pre-fix formula) |

### Validation 4 — CCG Module 9 / Module 12.10 redundancy example (13-year severance, local employee)
Tests the whole termination block in one pass — the block carrying both open items #4 and #4b.
| Step | Reg(s) | Design output | CCG figure | Match |
|---|---|---|---|---|
| Severance, statutory (58219) | 9384501 | 450 000+525 000+360 000 = **1 335 000** | 1 335 000 | ✅ |
| Préavis (3 months × 300 000) | 9384541 | **900 000** | 900 000 | ✅ |
| Congé (15.4 days × 300 000/26) | 9384551 | **177 692** | 177 692 | ✅ |
| Taxable terminal base | 9384213 (préavis+congé only, severance walled off per D7) | 900 000+177 692 = **1 077 692** | 1 077 692 | ✅ |
| Net ITS on terminal base | 9384221/241/251 | **183 146** | 183 146 | ✅ |
| CNPS on terminal base | 9384131 | 1 077 692 × 6.30% = **67 895** | 67 895 | ✅ |
| Net terminal payment | 9384911 | 2 412 692 − 183 146 − 67 895 − 500 = **2 161 151** | 2 161 151 | ✅ |

Confirms the D7 wall-off (severance never entering 58201/58213) reproduces the CCG's own split exactly — but note this validates the *statutory* leg's mechanics only, not the excess-over-statutory questions in #4/#4b, since this example has no excess to test.

### Validation 5 — CCG Module 4.4 overtime example (200 000 base, 6h@+15%/3h@+50%/2h@night+75%)
| Step | Reg(s) | Design output | CCG figure | Match |
|---|---|---|---|---|
| Hourly base rate (58218) | 9384401 | 200 000 ÷ 173.33 = **1 153.85** | 1 153.85 | ✅ |
| 41st–46th band | 9384411 | 6 × 1 153.85 × 1.15 = **7 961.5** | ≈7 961.5 | ✅ |
| Beyond 46th band | 9384421 | 3 × 1 153.85 × 1.50 = **5 192.3** | ≈5 192.3 | ✅ |
| Night band | 9384431 | 2 × 1 153.85 × 1.75 = **4 038.5** | ≈4 038.5 | ✅ |
| Total overtime | sum | **≈17 192** | ≈17 192 | ✅ |

Doesn't exercise 9384441 (Sunday/holiday daytime, the new fifth band) since the CCG's own example predates that correction — no CCG example exists yet for that band specifically, since it doesn't appear in the CCG at all. Worth a synthetic test once the WTC/CCG are patched per Resolution Log #1.

### Validation 6 — CCG Module 12, Example 4 (garnishment mechanism, not the rate)
Confirms ordering/mechanism only — this example's 50 000 XOF garnishment is a given court-ordered amount, not derived from the 33% rule, so it doesn't test 9384901's rate logic.
| Step | Design output | CCG figure | Match |
|---|---|---|---|
| Net before garnishment (400 000 gross, 1 part) | 400 000 − 25 700 (CNPS) − 60 000 (ITS) = **314 300** | 314 300 | ✅ |
| Net after garnishment | 314 300 − 50 000 = **264 300** | 264 300 | ✅ |

Confirms garnishment comes off net, after ITS/CNPS, and doesn't feed back into either base — the mechanism `9384901`/`9384911` are built on. Still doesn't validate the 33%/35–57% rate table itself (see 9384901's own open item on the maintenance-priority question).

All six validations tie out exactly once the Net Pay fix is applied. Validations 4–6 cover the termination, overtime, and garnishment blocks that the original two-validation pass never touched — none of those regulations had been checked against a real number before this review.

---

## Part 6 — Open Items

### v1.1 status — what the Mohit feedback loop resolved (the project's whole point)

The dev-team feedback (email thread + `CI_Review_Notes_for_Wallisson.md`) closed or corrected the following. These are no longer open:

| Item | v1.0 state | v1.1 resolution | Source |
|---|---|---|---|
| Complementary-pension cap | 10% only, commentary-sourced (was the lowest-priority open gap) | **Two-legged: LOWER of 10% taxable or 320,000 XOF** — DGI published reference; = the dev's CT-A-620 capping | Mohit email #3 |
| CMU in unpaid month | blanket "flat 500, unaffected by absence" — but not explicit it survives a zero-pay month | **Universal per-person, explicitly persists when pension/other branches zero out** | Mohit email #2 |
| RICF single/divorced parent + disabled child | not explicitly addressed | **Combines: 1.5 + 1.0 = 2.5 parts** | Mohit email #4 |
| Unpaid leave, all branches | one blanket rule | **Per-branch: CNPS zero base / CMU still owed** | Mohit email #1 |
| Interns / apprentices | not modelled | **New regs 9384161/171 (distinct bases)** | Mohit review #1 |
| First-employment exemption | not modelled (not even known) | **New reg 9384181** | Mohit review #2 |
| Senior officers / assimilés | not modelled | **New reg 9384191** | Mohit review #5 |
| RICF validation method | spot-test | **Now mandates full-matrix validation** (flagged NEEDS-SYSTEMATIC-VALIDATION on 9384231) | Mohit review #3 |

The four new special-category regs and the RICF full-matrix check carry **[NEEDS-RA-CONFIRM]** / **[NEEDS-SYSTEMATIC-VALIDATION]** tags — the *structure* is in place per the dev design and Mohit's notes, but the exact floor/ceiling/amount/duration figures need pulling from the specific CCG sections, and the RICF matrix must be run in full before go-live.

### Resolution Log (design decisions made via statutory research, not left open)

**#1 — Overtime bands (was CI-QA-REPORT MAJOR-1).** Independently verified against seven convergent sources, including the FAO-hosted consolidated legal text (droit-afrique.com, sourced to Décret n°96-203 art. 24 and the implementing *arrêté du Ministre chargé du Travail* under Code du Travail art. 31.4, which itself defers the exact rate to *arrêté* absent a CCI provision): **41st–46th hour +15%, beyond 46th +50%, night +75%, Sunday/holiday daytime +75%, Sunday/holiday night +100%.** The CCG's own Module 4.4 narrative and worked example use "48th hour" — this is the error, not the WTC. The WTC's CI-HS-15/50 codes already correctly use 46 (someone patched this since the QA report), but CI-HS-FERIE still collapses the Sunday/holiday day and night bands into one +100% rate — that gap is real and this design closes it with the new 9384441. **Recommend:** correct the CCG's Module 4.4 text from 48→46, and add the missing band to the WTC.

**#2 — Prime de panier (was CI-QA-REPORT MAJOR-2).** Confirmed still live in the actual WTC file (CI-PRIME-PANIER = CI-TX-01, "no statutory CI exemption") — not yet patched. This design adopts the CCG's position (CI-TX-03 equivalent, excluded ≤ 3× hourly SMIG per art. 23 CPS), matching the sibling premiums (salissure/tenue/outillage), which the WTC already codes correctly. **Recommend:** recode CI-PRIME-PANIER to CI-TX-03 in the WTC.

### New items surfaced while building this design — status after Advanced Research pass

**#3 — Per-day vs per-month basis for the four SMIG-multiple caps — RESOLVED, revised.** Unchanged from the prior pass: designed as monthly for all four (panier included), on the strength of a CPS art. 23 secondary source naming three of the four caps "mensuelle" explicitly. See reg 9384041.

**#4 — Excess-over-statutory severance/retirement: CNPS treatment — still not sourced, but no longer an unweighted guess.** Advanced Research went looking for a CNPS circular, doctrine note, or case law and found none exist anywhere publicly accessible. What it did produce: two conflicting Ivorian secondary sources, a comparative-law reasoning from France/Senegal, and a recommended conservative default. **Design default flipped**: excess is now treated as CNPS-sociable (previously: never sociable), configurable rather than hard-coded. See reg 9384511. This is a business-risk decision dressed as a technical default, not a resolved fact — say so plainly if this comes up in review.

**#4b — NEW, higher priority than #4: possible conflict in the ITS mechanism for severance/retirement excess.** Not something I went looking for — it surfaced while researching #4. One source (Côte d'Ivoire tax summary citing two dated DGI administrative notes) describes the severance ITS exemption as a small fixed amount (60 000 XOF) with the excess taxed at a flat 50%, which is structurally nothing like the CCG's own "exempt to the full statutory formula, then ordinary progressive brackets on the excess" account that the whole of Part 4's severance treatment is built on. I have not adjudicated between these — I don't have enough confidence in the new source to overwrite the CCG's own primary research, but I also can't wave it away. **Resolve this before anything else in this design** — if the fixed-amount/flat-50% mechanism is real, it changes reg 9384511's formula, not just its CNPS side-note, and probably changes the CCG itself.

**#5 — Auto-imported disclosed gaps from the CCG — mostly resolved now:**
- ~~Transport allowance exemption ceiling~~ — resolved (prior pass): zone-based, Abidjan 30 000 / Bouaké ~24–25 000 / Intérieur 20 000.
- ~~Code du Travail art. 33.1 quotité saisissable bands~~ — resolved (prior pass): Décret 2014-370, 33% flat / 35–57% graduated.
- ~~Arrêté n°1028 BIK forfaits~~ — **resolved this pass**: full housing/furniture/electricity grid by room count, three domestic-staff categories, and confirmation that telephone/third-party gardiennage were never forfaits at all (real value by design — see 9384601–9384631). One residual nuance: the water figure has two inconsistent presentations that Advanced Research flagged but didn't reconcile (see 9384611).
- ~~Complementary-pension 10% cap~~ — **RESOLVED in v1.1** (Mohit email #3): two-legged cap, LOWER of 10% taxable or 320,000 XOF, DGI published reference. See reg 9384212 and the v1.1 status table above.
- Payslip exact mandatory field list — unchanged, still not in source folder, not pursued this round.

**Net effect of this pass:** Q2 (BIK figures) resolved substantially — real, usable numbers with one flagged sub-nuance. Q1 (CNPS excess) did not resolve, but produced a defensible interim default plus something more important than what was asked for: a live, unreconciled conflict over how severance ITS actually works, which needs to be settled before this design goes further, not filed alongside the smaller gaps.

### Scope notes (not gaps)
- Pension/life-annuity ITS treatment (320 000 abatement, 70+ age reduction) is out of scope for this active-employee core design, consistent with how the CCG frames it as a pensioner-only regime.
- Board of directors' attendance fees, stock-option gains, and the multi-employer RICF double-counting safeguard are documented in the CCG (Modules 5/11) but have no dedicated regulation here since they're either out of the wage-type series (director fees) or client-config/process controls (RICF single-claim, stock-option realisation timing) rather than calculation steps.

---

## Part 7 — Readiness

A dev production design now exists (CT-A-620) — see the separate comparison document (`CI_Design_Comparison_Claude_vs_DevTeam.md`). v1.1 has folded in both the email-thread resolutions and Mohit's review notes.

**The one item that remains genuinely blocked — and the only thing standing between this design and closure — is #4b: the severance/retirement ITS mechanism.** It is exempt-to-formula-then-brackets (CCG) vs. fixed-60,000-then-flat-50% (a DGI-note-sourced alternative), and Mohit has not yet confirmed which. This changes an actual formula (reg 9384511/531), not just documentation, so it cannot be resolved by the design side alone. Everything else Mohit raised is now incorporated.

**Remaining non-blocking follow-ups:** pull the exact figures for the four new special-category regs (9384161/171/181/191) from the CCG sections; run the RICF full-combination-matrix validation (9384231); reconcile the CMU 500+500-vs-1,000 split; and the water-grid duplication (9384611). The 5-band overtime (#1) and the CNPS-excess default (#4) carry forward from prior passes.

**For the RA team (per the cross-training question):** the biggest lesson from this feedback loop is that special employee categories (intern/apprentice/first-employment/senior-officer) were the largest gap class — future CCGs should surface these as their own section, and RICF-type combination tables must be documented as a full matrix, not by common-case examples.

---

## Part 8 — Review Log (this pass)

Requested after finding a duplicate header and a stale cross-reference in Part 6 last round, with the instruction to check everything else once more, excluding the open items themselves. Found eight more issues — one of them a real calculation gap, the rest documentation/consistency defects of the same kind as the two that prompted this review:

1. **Net Pay formula (9384911) never subtracted the complementary-pension contribution** — only its effect on the ITS base. Any employee using that benefit would have had net pay overstated by the full contribution amount. This is the one genuine calculation gap in the list, not a wording issue. Found by hand-deriving CCG Example 3 rather than trusting the existing validation set — it happened to only cover scenarios where the missing term is zero. **Fixed**: formula now includes the term; Validation 3 added to Part 5 specifically to prove it.
2. **Part 1 flag cross-reference wrong**: the transport-allowance flag pointed at regulation `9384203`, which doesn't exist, instead of `9384031`. **Fixed.**
3. **A bogus placeholder regulation, `9384211`**, sat in Part 3's table with no content anywhere in Part 4 and blank Tax Group/Rule/Type fields — never a real regulation, leftover from drafting. **Removed.**
4. **Total regulation count was wrong** as a direct consequence of #3: stated as 42, actual count is 48. **Fixed**, with the discrepancy explained rather than just silently changed.
5. **Duplicate section header** for `9384521/531`, with different content split across the two copies — same failure mode as the Part 6 duplicate found last round, same root cause (an edit that added new content without merging into the section already there). **Merged into one.**
6. **A mechanism explanation went missing during an earlier edit**: 9384511's note on *how* the ITS-taxable excess actually flows into the ITS calculation (as a second, ITS-only gross variable feeding 9384213) was deleted when that section got rewritten for the CNPS-excess finding, and never replaced — leaving a formula-relevant detail simply absent. **Restored**, and the vague "§Part 4 above" self-reference that replaced it is now a concrete pointer to 58219 and the actual mechanism instead.
7. **Part 2's BIK account label was stale**: still described account 58224 as covering téléphone/gardiennage after Part 4 had already been corrected to say neither is a forfait. **Fixed**, and the Logement label updated to reflect the merged furniture calculation.
8. **9384213's formula mixed patterns**: four credits handled by straight addition, a fifth handled by double-negation that arrives at the same number through a more error-prone route. Not wrong, but exactly the kind of inconsistency that invites a real bug the next time someone edits it. **Simplified** to one consistent pattern.

Broader point behind #1: the original Part 5 only exercised roughly a third of the 48 regulations — termination, overtime, the complementary-pension credit, and garnishment had never been checked against a real number. Added four more validations (3–6) against CCG examples covering those blocks specifically, rather than assuming the untested two-thirds were fine because the tested third was.

None of this touches Part 6's open items, per the instruction — #4, #4b, and the water-grid duplication in 9384611 are unchanged, still open, exactly as unresolved as before this pass.

## Part 9 — JSON Conversion Test (Prompt 3), Actually Run

Not a read-through this time — built real JSON against the exact 13-key/16-key/3-key schema for a sample of regulations (script + output available on request), to see what breaks on contact rather than guessing.

**What converted cleanly:** `9384131` (simple flat rate), `9384221` (the 6-band Differential) — both produced valid JSON with no ambiguity once a `taxabilityRules` value was assumed (see below). Two smaller friction points surfaced even here: `9384351` (CE) has no `employeeRate` and no `employeeRateAccount`, which by Prompt 4's default rule should set `employeeRate` to 100 — except Prompt 4 also carves out an explicit exception for employer-only regulations, which this is, so leaving it blank is correct, but only because I knew to apply the exception rather than the default. And `9384501` (severance) doesn't fit the schema cleanly at all: its `taxGroup` is genuinely neither "Income Tax" nor "Social Security" (D7 walls it off from both), which the documented 2-value schema doesn't have a slot for; and its 30/35/40%-by-years-of-service structure doesn't map onto `incomeFrom`/`incomeTo` the way a tax bracket does, since those fields are named for income, not tenure — I used a free-text formula instead, which produces valid JSON but is a workaround, not a clean fit.

**What did not convert — and this is the real finding:** every regulation needs a `taxabilityRules` array, and this design never built one for any of them. For most of the 48, that's a small gap — a regulation reading from an already-computed intermediate (like `9384131` reading from `58210`) plausibly just needs a one-line rule pointing at that account. But `9384011` (Total Gross Remuneration) is different: per its own description, it sums *directly* from raw WTC wage-type codes, which means its `taxabilityRules` has to be a real, wildcard-condensed matrix per Prompt 2's rules — and that's a substantially bigger job than anything else in this design.

Pulled the actual numbers from the WTC to see how big: 266 `Earning`-category codes split across five tax-code groups (196 CI-TX-01, 20 each of CI-TX-02/03/05, 10 CI-TX-04). Two things this surfaced concretely:
- **Confirmed a design decision was correct but never formalized**: the WTC categorises `CI-IND-LICENCIEMENT`/`CI-IND-RETRAITE` as `Earning`, same as ordinary salary — meaning a naive "include everything tagged Earning" rule would wrongly pull severance/retirement into gross, contradicting D7. The design's own prose already excludes them ("excludes the two severance/retirement regs"), so this isn't a new error, but it means the actual exclusion has to be an explicit `isTaxable: false` override in the matrix, not just a sentence in Part 4 — the same is true for the 20 CI-TX-02 codes (family allowances/reimbursements), which the design's prose also already excludes correctly, same gap between "stated" and "formally encoded."
- **The condensation itself doesn't fall out for free**: of the 196 CI-TX-01 codes, only 8 of the 43 ten-blocks are fully populated and cleanly wildcard-able under Prompt 2's rules; the other 35 are irregular and would need cross-checking against every other tax-code group's ranges before it's safe to sweep the gaps into a wildcard (Prompt 2 allows this only when a gap isn't secretly claimed by a different status elsewhere).

**Bottom line:** the regulation layer (bands, rates, formulas — everything Parts 3–4 actually contain) converts to the schema without drama once you know the two small traps above. The taxability-matrix layer (Prompt 2's condensed Yes/No list, Section 2 of the 3-section structure Prompt 5 describes) was never built for this design at all — not wrong, just absent, concentrated almost entirely in `9384011` since everything else reads from intermediates rather than raw wage types. That's a real, scoped, doable follow-on task now that it's been pulled into the open, not a hypothetical risk anymore.
