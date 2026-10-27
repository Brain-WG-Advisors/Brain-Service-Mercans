---
name: payroll-compliance-cotedivoire
description: >
  Côte d'Ivoire (CI) payroll & statutory compliance reference for Mercans analysts —
  2026 tax year. Single ITS regime (post-2024 reform), CNPS social security, FDFP,
  employer wage taxes, Labour Code leave/overtime/termination, statutory filing
  calendar, and payslip rules. Use when answering any CI payroll, tax, social-security,
  leave, termination, or statutory-filing question, or when validating a CI calculation.
license: Mercans internal
---

# Côte d'Ivoire — Payroll & Statutory Compliance Skill (2026)

> **How to use this skill.** This is the authoritative quick-reference for Mercans
> compliance analysts working Côte d'Ivoire payroll for tax year **2026**. Every rate
> carries its legal source. Items marked **`[VERIFY WITH RA]`** are unresolved or
> source-contested — do **not** hard-code them into a client engine without Regulation
> Analyst sign-off. Companion files: `statutory_rates.json` (machine-readable),
> `filing_calendar.md` (month-by-month), `quick_reference.md` (cheat sheet).

---

## ⚠️ 0. CRITICAL — Read this first (the 2024 ITS reform)

**Côte d'Ivoire merged its three former salary taxes into ONE single progressive ITS,
effective 1 January 2024 — and it is unchanged for 2026.**

- Governing law: **Ordonnance n°2023-719 du 13 septembre 2023** (in force 1 Jan 2024),
  amending the CGI; DGI doctrine note **N°00026/MFB/DGI/DLCD du 03 janvier 2024**.
- The **Annexe Fiscale 2026 (Loi de Finances 2026) makes NO change** to the ITS bracket
  table, RICF, or rates — the post-2024 regime stands for 2026.

| ABOLISHED / merged 1 Jan 2024 — **DO NOT USE** | Replaced by |
|---|---|
| **IS** — Impôt sur les Salaires (incl. employer-borne ~1.2%/1.5%) | Single **ITS** |
| **CN** — Contribution Nationale *on the employee's salary* | Single **ITS** |
| **IGR** — Impôt Général sur le Revenu *on salaries* | Single **ITS** |
| **20% professional-expense abatement** (old CGI art. 119) | **Suppressed** |
| **Quotient familial divisor** (divide income by parts) | **RICF** tax credit (§3) |

**F18 trap — the #1 CI error.** Web calculators (talent.com, macalculatriceenligne, etc.)
still apply pre-reform mechanics: "CN 1.5%", "IGR", a "15%/20% frais professionnels
abatement", and a "CNPS 6.3% deduction before tax". **All wrong for 2024–2026.** Apply the
single ITS bracket table **directly to total gross remuneration** — no abatement, and
**CNPS is NOT deducted from the ITS base** (the reform text defines the base as "total des
rémunérations"; DGI worked examples apply brackets to gross). There is **no separate CN, no
IGR, and no employer-borne salary-tax portion** of ITS — ITS is borne by the employee and
withheld by the employer.

> Note: a **separate employer-side levy still called "Contribution Nationale (CN) employeur"
> at 1.2%** survives as part of the *contribution employeurs* (§2.2). It is a **different
> levy** from the abolished employee CN. Don't conflate them.

---

## 1. Country overview

| Item | Value |
|---|---|
| Official name | République de Côte d'Ivoire |
| Currency | West African CFA franc — **XOF** (FCFA / F CFA); pegged to EUR (655.957) |
| Amounts | **Whole XOF, no decimal subunit** — round contributions & ITS to nearest franc |
| Official language | French |
| Fiscal / tax year | **Calendar year** (1 Jan – 31 Dec); ITS withheld **monthly** (PAYE) |
| Income tax on salary | **ITS** — Impôt sur les Traitements, Salaires, Pensions et Rentes Viagères |
| Social security | **CNPS** (Caisse Nationale de Prévoyance Sociale) + **CMU** via CNAM |
| Tax authority | **DGI** (Direction Générale des Impôts) — portal **e-impots.gouv.ci** |
| Labour law | **Loi n°2015-532 du 20 juillet 2015** (Code du Travail) + CCI (Convention Collective Interprofessionnelle) |
| Employer tax ID | **NCC** (Numéro de Compte Contribuable), transitioning to **IDU** (Identifiant Unique) |

---

## 2. Statutory rates — Social security & payroll taxes

### 2.1 CNPS — mandatory social-security branches (2026)

Legal basis: Code de Prévoyance Sociale (Loi 99-477 du 02/08/1999); CNPS *Guide de
l'Employeur*; CNPS communiqué of 11/01/2023 (floor and ceilings); CLEISS (rates only). Base (assiette) = **total gross salary incl. benefits in kind**,
excluding genuine reimbursed business expenses (art. 23 CPS).

| Branch | Employer | Employee | Monthly ceiling (plafond) | Monthly floor |
|---|---|---|---|---|
| **Retraite / Vieillesse** (pension) | **7.70%** | **6.30%** | **3 375 000 XOF/mo** (40 500 000/yr) | SMIG 75 000 |
| **Prestations Familiales** (PF) | **5.00%** | — | **75 000 XOF/mo** | SMIG 75 000 |
| **Assurance Maternité** (AM) | **0.75%** | — | **75 000 XOF/mo** | SMIG 75 000 |
| **Accidents du Travail / MP** (AT/MP) | **2% – 5%** by risk class of sector | — | **75 000 XOF/mo** | SMIG 75 000 |
| **CMU** (Couverture Maladie Universelle) | **500 XOF** | **500 XOF** | flat per insured person | n/a |

- **Pension is 14% total**, split employer 55% / employee 45% → 7.70% / 6.30% (CLEISS-confirmed).
- **AT/MP rate is sector-specific** (2–5%), notified to the employer by CNPS at affiliation.
  `[VERIFY WITH RA]` the exact class rate per client sector.
- **Dual-ceiling effect:** pension uses the high **3 375 000** ceiling; PF/AM/AT-MP all cap at
  **75 000** (= SMIG = floor), so for any salary ≥ 75 000 those three are fixed (PF 3 750; AM 562.50;
  AT/MP 1 500–3 750). Ceilings in force since **1 Jan 2023**: CNPS communiqué "Nouveau plafond des
  cotisations sociales" (11 Jan 2023, under Décret 2022-986); legal basis Loi 99-477 art. 23. The
  **70 000** (840 000/yr) on the cnps.ci "Employeur" page, in the 2021 CNPS Guide and on the CLEISS contribution sheet is pre-2023 —
  SUPERSEDED, do not use. CMU is a flat **1 000/person/month** (500 EE + 500 ER).
- **Assiette floor = SMIG 75 000/mo.** *(The CNPS Guide PDF still prints the obsolete
  36 607 SMIG and an old 1 647 315 pension ceiling — both SUPERSEDED, do not use.)*
- **Excluded within SMIG-multiple limits:** prime de panier ≤ 3× hourly SMIG; salissure
  ≤ 13×; indemnité de tenue ≤ 7×; outillage ≤ 10×; transport up to the tax-exempt amount;
  family allowances excluded (art. 23 CPS). Excess over the cap is reintegrated into the base.

### 2.2 Employer wage taxes — "contribution employeurs" (DGI / CGI art. 134–146)

Base for all four = the employee's total gross taxable remuneration (the ITS base).
**Local (Ivorian) vs expatriate** distinction is critical.

| Tax | LOCAL personnel | EXPATRIATE personnel | Authority |
|---|---|---|---|
| **CE** — Contribution à la charge des employeurs | **0% (exonéré)** | **9.2%** | CGI art. 134 ff., 146 |
| **CN employeur** — Contribution Nationale (employer part) | **1.2%** | **1.2%** | CGI art. 146 |
| **TA** — Taxe d'Apprentissage (collected by FDFP) | **0.4%** | **0.4%** | CGI art. 143; Loi 66-615 |
| **TFPC** — Taxe additionnelle Formation Prof. Continue (FDFP) | **1.2%** | **1.2%** | CGI art. 146; Loi 77-924 |

- **Total employer wage-tax load: LOCAL = 2.8%** (0 + 1.2 + 0.4 + 1.2); **EXPAT = 12.0%**
  (9.2 + 1.2 + 0.4 + 1.2). **FDFP** = TA 0.4% + TFPC 1.2% = **1.6%**.
- Exemptions (CGI art. 136/136 bis): CN/CE exonerated on first-employment pay for 2 years and
  on intern allowances ≤ 150 000 XOF/mo per intern (≤12 months); CNPS maternity indemnities
  exonerated (art. 134-4°).

---

## 3. Income tax — ITS (Impôt sur les Traitements et Salaires)

### 3.1 Progressive monthly bracket table (CGI art. 119 bis; Ord. 2023-719)

Applied **marginally** (slice by slice) to **monthly taxable remuneration** = total gross
incl. benefits in kind, **no abatement, CNPS not deducted**.

| Monthly taxable income (XOF) | Marginal rate |
|---|---|
| 0 – 75 000 | **0%** |
| 75 001 – 240 000 | **16%** |
| 240 001 – 800 000 | **21%** |
| 800 001 – 2 400 000 | **24%** |
| 2 400 001 – 8 000 000 | **28%** |
| Above 8 000 000 | **32%** |

- First **75 000/mo at 0%** (= SMIG, so a minimum-wage worker with no benefits pays **0 ITS**).
- **F18 trap:** ignore alternative "0/10/15/20/25/35%" or "150k/300k/600k" tables from
  calculator sites — those are draft/superseded/simulator figures. The enacted table is above.

### 3.2 RICF — Réduction d'Impôt pour Charges de Famille (CGI art. 120)

A **non-refundable tax credit subtracted from gross ITS** (replaces the old quotient familial).
**Net ITS = Gross ITS − RICF, floored at 0.**

| Parts | Monthly reduction (XOF) | Annual (XOF) |
|---|---|---|
| 1 | 0 | 0 |
| 1,5 | 5 500 | 66 000 |
| 2 | 11 000 | 132 000 |
| 2,5 | 16 500 | 198 000 `[VERIFY WITH RA — OCR showed 195/196 000; 16 500×12=198 000 is consistent]` |
| 3 | 22 000 | 264 000 |
| 3,5 | 27 500 | 330 000 |
| 4 | 33 000 | 396 000 |
| 4,5 | 38 500 | 462 000 |
| 5 | 44 000 | 528 000 |

**Parts by family situation (CGI art. 120-2°):**

| Situation | Parts |
|---|---|
| Single / divorced / widowed, no dependent child | 1 |
| Married, no child **or** single/divorced + 1 child | 2 |
| Married/widowed + 1 child **or** single/divorced + 2 children | 2,5 |
| Married/widowed + 2 children **or** single/divorced + 3 children | 3 |
| Married/widowed + 3 children **or** single/divorced + 4 children | 3,5 |

- **+0,5 part per dependent child; +1 part per disabled child. Max 5 parts.**
- **Employer practical cap:** for a minor child not head-of-household the employer applies
  **1 part** by derogation unless documentation justifies more. `[VERIFY WITH RA]` operational use.
- Dependent child = minor, **or under 27 if studying**, with no separately-taxed income.
- Situation assessed at 1 Jan (or 31 Dec if charges increase mid-year).

### 3.3 Special ITS rules

- **Pensions / life annuities:** fixed **abatement of 320 000 XOF** before the brackets
  (raised from 300 000 by Ord. 2023-719). For pensioners only — NOT active employees.
- **Retirees aged 70+:** further **75% reduction of net ITS** (after RICF).
- **Bonuses, primes, 13th-month, gratifications:** part of "total des rémunérations" →
  **fully subject to ITS in the month paid**, run through the monthly brackets (no averaging).
- **Benefits in kind:** valued on the administrative scale **Arrêté n°1028/MEF-DGI du 7 Nov 1996**
  (housing by number of rooms; water flat +30 000, +30 000 if pool; electricity +20 000 per AC
  unit; domesticité/téléphone/gardiennage forfaits). Genuine company/service vehicles are NOT a
  taxable benefit. `[VERIFY WITH RA]` exact per-room XOF forfaits (not in source folder).
- **Non-residents:** taxable if >183 days in CI **or** paid by a CI-established employer;
  ITS withheld under the same brackets. `[VERIFY WITH RA]` any flat non-resident rate / DTT interaction.

### 3.4 ITS calculation method (active employee)

1. **Gross taxable monthly** = base + allowances + overtime + bonuses (in month paid) + benefits
   in kind − legally exempt items. (No abatement; do **not** deduct CNPS.)
2. **Apply brackets marginally** → **gross ITS (impôt brut)**.
3. **Determine parts** (§3.2), cap 5.
4. **Subtract RICF** for those parts → **net ITS**, floor at 0.
5. *(Pensioners 70+ only)* apply 75% reduction.
6. Result = **monthly ITS to withhold**, remit by the §6 deadline.

---

## 4. Worked example — local employee, 600 000 XOF/mo (reconciles across CCG/WTC/payslip)

**Profile:** Ivorian (local); gross **600 000 XOF/mo**; married + 2 children → **3 parts**;
1 CMU person; AT/MP risk 3% (mid-range example).

**Employee deductions**

| Item | Base | Rate | Amount |
|---|---|---|---|
| CNPS pension (EE) | 600 000 (< ceiling) | 6.30% | **37 800** |
| CMU (EE) | flat | 500 | **500** |
| ITS — gross: 0(≤75k) + 26 400(165k@16%) + 75 600(360k@21%) = 102 000; − RICF 3 parts 22 000 | | | **80 000** |
| **Net pay** | | | **= 600 000 − 37 800 − 500 − 80 000 = 481 700** |

**Employer cost on the same 600 000**

| Contribution | Base | Rate | Amount |
|---|---|---|---|
| CNPS pension (ER) | 600 000 | 7.70% | 46 200 |
| Prestations Familiales | 75 000 (cap) | 5.00% | 3 750 |
| Maternité | 75 000 (cap) | 0.75% | 562.50 |
| AT/MP (3% ex.) | 75 000 (cap) | 3.00% | 2 250 |
| CMU (ER) | flat | 500 | 500 |
| CN employeur | 600 000 | 1.20% | 7 200 |
| Taxe apprentissage (FDFP) | 600 000 | 0.40% | 2 400 |
| TFPC (FDFP) | 600 000 | 1.20% | 7 200 |
| CE (local → exonéré) | — | 0% | 0 |
| **Total employer on-cost** | | | **70 062.50** |

**Total employer outlay = 670 062.50 XOF/mo.** *(If expatriate: add CE 9.2% × 600 000 = 55 200;
on-cost ≈ 125 262.50, outlay ≈ 725 262.50.)*

---

## 5. Labour Code — leave, hours, overtime, termination

### 5.1 Minimum wage (2026)

| Item | Monthly (XOF) | Basis |
|---|---|---|
| **SMIG** (general) | **75 000** | Décret 2022-986 (since 1 Jan 2023, unchanged 2026) |
| **SMAG** (agricultural) | **39 960** | Same décret |

- Salary may never fall below the applicable **category minimum** (salaire minimum catégoriel),
  usually higher than SMIG. `[VERIFY WITH RA]` no 2026 tripartite revision before go-live.
- Annual SMIG base for retirement-cap = **2 080 hours** (CCI art. 40).

### 5.2 Working hours & overtime

- **Normal:** 40 h/week (general); 2 400 h/year (agricultural). Weekly rest ≥ 24 h (Sunday).
- **Night work:** 21h00–05h00. Standard monthly-hours divisor: **173,33 h/mo** (market practice;
  `[VERIFY WITH RA]` the engine divisor).

**Overtime premiums (CCI art. 51) on the *salaire réel* excluding expatriation indemnity:**

> ⚠️ **`[VERIFY WITH RA]` — UNRESOLVED SOURCE CONFLICT (QA MAJOR-1).** Two band schemes exist
> and must be reconciled with the RA against the current CCI/arrêté before any client build:

| Band | Mercans WTC / published-CCI scheme **(engine-implemented)** | Labour-Code research reading |
|---|---|---|
| +15% | 41st–**46th** hour (weekday day) | 41st–**48th** hour |
| +50% | beyond **46th** hour | beyond **48th** hour |
| +75% | night 21h–5h | night weekday **and** Sunday/holiday **daytime** |
| +100% | all Sunday / public-holiday hours | Sunday/holiday **night** only |

The WTC implements **41–46 / >46 / night +75 / Sunday-holiday +100**. The research brief (from
the Code/CCI PDF) reads **41–48 / >48** plus a distinct **Sunday/holiday daytime +75%** band.
Confirm the exact thresholds and whether a Sunday-daytime +75% band applies. *Forfaitaire
(lump-sum) overtime clauses are null for workers, employees and agents de maîtrise.*

### 5.3 Annual leave (Code du Travail arts. 25.1–25.9)

- **Accrual: 2,2 working days (jours ouvrables) per month** = **26,4 ≈ 27 days/year.**
- Right to take opens after **12 months** service.
- **Seniority bonus days:** +1 (5 yr), +2 (10 yr), +3 (15 yr), +5 (20 yr), +7 (25 yr), +8 (30 yr).
- **Mother bonus:** +2 days/dependent child if worker <21 at period end (or from the 4th child if >21).
- Pay ≥ salary + all remuneration elements, paid at departure on leave. Unused leave on termination
  → *indemnité compensatrice de congé* (taxable salary). `[VERIFY WITH RA]` daily divisor (26 vs 30).

### 5.4 Public holidays 2026

14 days. Fixed: 1 Jan, 1 May (chômé/payé), 7 Aug (Fête Nationale, chômé/payé), 15 Aug, 1 Nov,
15 Nov, 25 Dec, plus Easter Monday (6 Apr), Ascension (14 May), Pentecost Monday (25 May).
**Islamic dates are lunar-estimated** (Laylat al-Qadr ~16 Mar, Aïd el-Fitr ~19–20 Mar,
Tabaski ~27 May, Maouloud ~24–25 Aug) and may shift ±1–2 days by moon sighting —
`[VERIFY WITH RA]` against the official 2026 arrêté. (See `filing_calendar.md`.)

### 5.5 Maternity / paternity / sick

- **Maternity: 14 weeks** (6 before + 8 after); +2 wks multiple birth, +3 wks if illness.
  **Cash benefit borne by CNPS**, not the employer. Nursing breaks 1 h/day for 15 months.
- **Paternity:** no standalone statutory leave — covered by CCI exceptional family-event leave
  (a few days). `[VERIFY WITH RA]` exact CCI permissions-exceptionnelles day-count.
- **Sick:** certified illness suspends the contract; counts toward leave accrual up to 6 months.
  Sick-pay quantum set by CBA/policy. `[VERIFY WITH RA]` CCI sick-pay schedule.

### 5.6 Other statutory pay elements

- **Prime de fin d'année (13th month), CCI art. 53:** ≥ **75% of the monthly category minimum**;
  pro-rated for partial-year service. Fully subject to ITS + CNPS.
- **Prime d'ancienneté, CCI art. 55:** **2% of category minimum after 2 yr, +1%/yr → 25% cap** at 25 yr.

### 5.7 Termination

**Notice (préavis) — Décret 96-200** (subject to more favourable CBA):

| Category | Seniority | Notice |
|---|---|---|
| Monthly-paid, cat. 1–5 | ≤ 6 yr / 6–11 / 11–16 / >16 | 1 / 2 / 3 / 4 months |
| Hourly/daily, cat. 1–5 | ≤6mo / 6mo–1yr / 1–6 / 6–11 / 11–16 / >16 | 8d / 15d / 1mo / 2 / 3 / 4 months |
| Cat. 6+ (cadres) | ≤ 16 yr / > 16 yr | 3 / 4 months |

During notice: 2 free paid days/week for job search. No notice for *faute lourde*.

**Severance — Indemnité de licenciement (Décret 2017-210 art. 4 = CCI art. 39):**
Eligibility ≥ **1 year** service and no gross misconduct. Per **year of presence**, a % of the
**average monthly global salary of the last 12 months** (fractions rounded down to inferior month):

| Years band | Rate per year |
|---|---|
| Up to 5th year | **30%** |
| 6th–10th year | **35%** |
| Beyond 10th year | **40%** |

*Example — 13 yr, avg 300 000/mo:* (5×30% + 5×35% + 3×40%) × 300 000 = 450 000 + 525 000 +
360 000 = **1 335 000 XOF**.

**Retirement indemnity (Décret 2017-210 art. 5; CCI art. 40):** same 30/35/40% formula,
**capped at 25 × SMIG** (annual 2 080-h base). Retirement age **55** (deferrable 1 yr per
dependent child). `[VERIFY WITH RA]` current CNPS pension age (historically 55–60).

**Tax of termination pay:** statutory/legal portion of *licenciement* / *départ retraite*
indemnities is generally **ITS-exempt**; amounts above the legal entitlement, plus *préavis*
and *indemnité compensatrice de congé*, are **taxable salary**. `[VERIFY WITH RA]` the exact
exemption boundary against Annexe Fiscale 2026 / DGI — do not hard-code a %.

---

## 6. Filing calendar (statutory payroll filings)

Full month-by-month detail in `filing_calendar.md`. Summary:

| Filing | Authority | Frequency | Deadline | Portal |
|---|---|---|---|---|
| **ITS withholding declaration** | DGI | Monthly | **15th** of following month (centres); DGE/DME 10th industrial/petrol/mining, 15th commercial, 20th services; TEE 10th | e-impots.gouv.ci |
| **Contribution employeurs** (CE/CN/TA/TFPC) | DGI → FDFP | Monthly | **15th** of following month | e-impots.gouv.ci |
| **État de régularisation ITS** (annual reconciliation) | DGI | Annual | **15 Feb** (others); DGE/DME 10/15/20 Feb | e-impots.gouv.ci |
| **État 301** (annual recap of salaries paid) | DGI | Annual | **30 June** (audited accounts) / **30 May** (others) | e-impots.gouv.ci |
| **CNPS social contributions** | CNPS | Monthly (≥20 emp.) / Quarterly (<20) | within **15 days** of period end | e-CNPS (online only) |
| **DISA** (annual individual salaries) + DASC | CNPS | Annual | **31 March** following year | e-DISA Excel / e-CNPS; DASC on paper |
| **CMU nominative declaration** | CNPS (for CNAM) | Monthly/Quarterly | within **15 days** of period end | e-CNPS |

- **ITS small-amount simplification:** if monthly withholding ≤ **10 000 XOF**, defer to
  semi-annual (15 Jul / 15 Jan), unless a month exceeds 5 000 (then pay within 15 days).
- **e-impôts mandatory for ALL enterprises (incl. micro) from 1 Jan 2026** (LF2026).
  `[VERIFY WITH RA]` exact LF2026 article.
- **DISA penalty:** 10% of total monthly contributions for late/non-filing (art. 30, Loi 99-477).
  **CNPS late-payment surcharge:** 0,050% per the delay.

**HR-scope (do NOT build as payroll filings):** embauches/licenciements declaration to Agence
Emploi Jeunes (Code art. 11.1); periodic main-d'œuvre returns to Inspection du Travail (art. 92.1);
opening-of-business declaration; AT/MP accident declaration within 48 h (art. 92.4 — event-based).

---

## 7. Payslip requirements (Bulletin de Paie — Code du Travail art. 32.5)

- Employer must deliver an **individual payslip at the moment of payment**; the **detailed
  structure is set by decree** (the Code itself does not enumerate fields). `[VERIFY WITH RA]`
  the implementing arrêté for the exact mandatory field list.
- **Mercans payslip = 5-sheet generator**, sheet 2 in **local language (French)**.
- **Expected itemised components:** employer identity (name, address, **NCC**, **CNPS matricule**,
  activity code); employee identity (name, **CNPS insured number**, category/échelon); period;
  gross (base + primes + indemnités + benefits in kind); each CNPS employee deduction (**retraite
  6,3%**, **CMU 500**); **ITS withheld (after RICF)**; other deductions; **net payable**;
  paid-leave balance; payment date/method.
- Acceptance "without reserve" / "pour solde de tout compte" does **not** waive worker rights
  (art. 32.6). Records retained as accounting pieces.

---

## 8. Top 5 compliance risks for Mercans analysts

1. **Pre-reform ITS mechanics (F18).** Never apply IS/CN/IGR, the 20% abatement, a quotient
   divisor, or CNPS-deducted-from-ITS-base. Single ITS on **total gross**, RICF as a credit. (§0, §3)
2. **Overtime band conflict (QA MAJOR-1, UNRESOLVED).** CCG says 41–48; WTC/CCI says 41–46.
   Confirm bands with RA before any build — wrong bands = wrong gross. (§5.2) `[VERIFY WITH RA]`
3. **Prime de panier classification (QA MAJOR-2, UNRESOLVED).** CCG + art. 23 CPS: excluded from
   CNPS ≤ **3× hourly SMIG** (excess reintegrated), like salissure/tenue/outillage. The WTC
   currently codes panier **fully sociable (CI-TX-01)** — these contradict. Treat panier as
   **conditionally exempt (CI-TX-03)** and flag the WTC. (§2.1) `[VERIFY WITH RA]`
4. **Local vs expatriate split.** CE is **0% local / 9.2% expat**; total employer wage tax jumps
   **2.8% → 12%**. Mis-flagging personnel type mis-states employer cost materially. (§2.2)
5. **Wrong CNPS ceilings/SMIG from stale PDFs.** Use pension ceiling **3 375 000** (not 1 647 315
   / 2 700 000) and SMIG **75 000** (not 36 607 / 60 000). PF/AM/AT-MP cap **75 000** since 1 Jan 2023 (not 70 000 — pre-2023 value still on the cnps.ci "Employeur" page). (§2.1)
   `[VERIFY WITH RA]` the current CNPS appel-de-cotisations ceiling at go-live.

---

## 9. Wage type reference (key WTC codes — CI-WTC-001)

**Tax-code legend** (sourced to CGI / Ordonnance 2023-719):

| Code | Meaning |
|---|---|
| **CI-TX-01** | Standard taxable salary — single ITS + all 4 CNPS branches |
| **CI-TX-02** | Fully exempt — excluded from BOTH ITS and CNPS base |
| **CI-TX-03** | Conditional exemption — exempt up to a statutory cap; excess reintegrated |
| **CI-TX-04** | Benefit in kind — valued on Arrêté n°1028 scale; ITS + CNPS |
| **CI-TX-05** | Expatriate remuneration — ITS + CNPS + employer CE 9.2% |
| **CI-NA** | Not a taxable/sociable wage type (employee deduction / employer contribution / rate / base) |

**Selected CI wage types:**

| Code | Wage type | Treatment |
|---|---|---|
| CI-TX-01 | Salaire de base, prime d'ancienneté, prime de fin d'année, gratifications, bonuses, indemnité compensatrice de congé, indemnité de préavis | Full ITS + CNPS |
| CI-HS-15 / -50 / -NUIT / -FERIE | Overtime +15% / +50% / night +75% / Sunday-holiday +100% | Taxable & sociable `[VERIFY bands — §5.2]` |
| CI-TX-04 | Avantages en nature (LOG/VEH/DOM/EAU/ELEC/TEL) | Arrêté 1028 scale |
| CI-TX-05 / CI-CE-EXPAT | Indemnité d'expatriation; employer CE on expats (9.2%) | ITS+CNPS+CE |
| CI-PRIME-TRANSPORT / -SALISSURE / -TENUE / -OUTILLAGE | Transport / dirt / uniform / tooling | **CI-TX-03** conditional (SMIG-multiple cap) |
| CI-PRIME-PANIER | Meal / basket allowance | **Should be CI-TX-03** (≤3× hourly SMIG); WTC currently CI-TX-01 `[VERIFY — risk #3]` |
| CI-TX-02 | Family allowances, business-expense reimbursement | No ITS / no CNPS |
| CI-TX-03 | Indemnité de licenciement, indemnité de départ à la retraite | ITS exempt to cap / no CNPS |
| CI-CMU-EE / CI-CMU-ER | CMU employee / employer | Flat 500 each (not a subjection column) |

---

## 10. Data field reference (key DD fields — CI-DD-001)

| Field | Local (FR) | Option mapper | Notes |
|---|---|---|---|
| National ID / Residence Card Number | Numéro CNI / Carte de Résident / Séjour | ID Document Type (CNI/RES/SEJOUR/PASS) | On DISA + État 301 |
| CNPS Insured Number | Numéro Assuré CNPS | — | Unique & permanent across employers |
| CMU Number | Numéro CMU | — | Numeric (CNAM-assigned) |
| Personnel Type | Type de personnel | **LOC / EXP** | Drives CE 0% vs 9.2% |
| Marital Status | Situation matrimoniale | **C / M / D / V** | Drives RICF parts |
| Number of Dependent Children / Disabled Children | Enfants à charge / handicapés | — | Drives RICF parts |
| Benefit in Kind Type(s) | Type(s) d'avantage en nature | **LOG/VEH/DOM/EAU/ELEC/TEL** | Arrêté 1028 valuation |
| Contract Type | Type de contrat | **CDI / CDD / APP / STG** | Scope: civil servants (IPS-CGRAE) & non-salariés out |
| Job Category / Échelon | Catégorie / Échelon | **OUV / EMP / AM / CADRE** | Drives notice/severance |
| Employer NCC / IDU, CNPS Matricule | — | Employer ID Type (NCC/IDU) | Employer registration |

> **Scope discipline (QA-verified):** the DD holds **master data only** — no calculated
> amounts, no base-salary value (those live as WTC parameters). RICF parts, AT/MP rate, the
> arrêté-1028 scale and contribution amounts are **WTC parameters, not DD fields.**

---

## 11. Key authorities & sources

| Authority | Role | Channel |
|---|---|---|
| **DGI** — Direction Générale des Impôts | ITS, employer wage taxes, État 301 | e-impots.gouv.ci |
| **CNPS** — Caisse Nationale de Prévoyance Sociale | Social security, DISA, CMU collection | e-CNPS portal |
| **CNAM / IPS-CNAM** | CMU scheme | via CNPS collection |
| **FDFP** | Apprenticeship + continuing-training taxes | via DGI filing |
| **Inspection du Travail** | Labour oversight, declarations | Ministère de l'Emploi |
| **ARTCI** | Data-protection (Loi 2013-450); DPO register due 31 Jan 2026 | artci.ci |

**Primary legal sources:** Ordonnance n°2023-719 du 13/09/2023 (ITS reform); DGI note
N°00026/MFB/DGI/DLCD du 03/01/2024; CGI art. 115–120, 134–146; Loi 99-477 du 02/08/1999 (CPS);
Décret 2022-986 (SMIG); Loi n°2015-532 du 20/07/2015 (Code du Travail); Décret 96-200 (préavis);
Décret 2017-210 (severance/retirement); CCI (overtime, primes, leave bonuses); Arrêté n°1028 du
07/11/1996 (benefits-in-kind scale); Annexe Fiscale 2026; DGI Calendrier des Obligations Fiscales;
CNPS communiqué « Nouveau plafond des cotisations sociales » of 11/01/2023 (CNPS floor and ceilings);
CLEISS (CNPS rates only; its PF/AM/AT-MP ceiling of 70 000 is pre-2023).

> **Source authority order (Mercans):** official government form/XSD > CCG > web research.
> No official e-impots/e-CNPS form PDF or XSD exists in source — field codes/positions are
> **DERIVED**; confirm masks (NCC digit count, CNPS/CMU number length) with RA.
