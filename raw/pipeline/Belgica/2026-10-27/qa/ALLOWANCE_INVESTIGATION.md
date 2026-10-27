# Belgian basic tax-free allowance, income year 2026 — investigation

**Status:** INVESTIGATION ONLY. No file in `01-ccg/` or `02-wtc/` was modified.
**Date of investigation:** 14 August 2026
**Question:** CCG and WTC state EUR 11,180 as the basic tax-free allowance for income year 2026. Is that correct after the personal income tax reform, and if not, what is?

---

## 1. Bottom line

The investigation resolved all three candidate figures. They are not competing estimates of one number — **they are three different numbers that each exist, for different purposes**:

| Figure | What it actually is | Status |
|---|---|---|
| **EUR 11,180** | The **counterfactual** indexed art. 131 WIB 92 amount for income year 2026 — what the allowance *would have been* had the reform not passed (old base EUR 4,785 × coefficient 2.3356 = 11,175.85 → 11,180) | **Superseded. Never became law.** |
| **EUR 11,170** | The **bedrijfsvoorheffing (Annex III) withholding** allowance actually in force for income year 2026, giving a reduction of EUR 2,987.98 | **In force today.** Pre-reform basis. |
| **EUR 11,550** | The **personal income tax (art. 131 WIB 92) assessment** allowance for income year 2026 / assessment year 2027, post-reform (new base EUR 4,945 × 2.3356 = 11,549.53 → 11,550) | **In force, confirmed by primary source.** |

**Answer to task 3 — the figure the CCG and WTC should use:**

Both artifacts describe the **bedrijfsvoorheffing withholding computation** (Annex III, scale I/II, step G at 26.75%). The correct figure for that computation, as the law stands on 14 August 2026, is **EUR 11,170.00**, giving a step-G reduction of **EUR 2,987.98**.

**EUR 11,180 is wrong in every reading.** It is neither the withholding figure (11,170) nor the assessment figure (11,550). It is a number that the reform prevented from ever taking effect.

Confidence: see §6.

---

## 2. Task 1 — the post-reform Annex III amendment

### 2.1 The reform law itself — FOUND, primary source

**Wet van 15 juli 2026 tot hervorming van de personenbelasting** / *Loi du 15 juillet 2026 portant réforme de l'impôt des personnes physiques*
Belgisch Staatsblad **29 July 2026**, p. 40196, **NUMAC 2026005724**.

Retrieved from the Staatsblad summary and article text via ejustice. Its **Article 2** amends art. 131 WIB 92, raising the non-indexed basic exempted amount in five steps:

| Non-indexed amount | Applicable from |
|---|---|
| 4.785 → **4.945 euro** | **aanslagjaar 2027** |
| 4.945 → 4.990 euro | aanslagjaar 2028 |
| 4.990 → 5.070 euro | aanslagjaar 2029 |
| 5.070 → 5.840 euro | aanslagjaar 2030 |
| 5.840 → 6.230 euro | aanslagjaar 2031 |

**Article 4** confirms: articles 2, 1° and 3, a) are *"van toepassing vanaf aanslagjaar 2027"*.

**Critical reading note.** *Aanslagjaar* 2027 = **income year 2026**. Several secondary sources (Securex, and Sodalis / Accountants Academy republishing Securex) state the allowance rises *"van € 10.910 (inkomstenjaar 2026) naar € 15.600 (inkomstenjaar 2030)"*. **That labelling is shifted by one year and is wrong.** EUR 10,910 is the indexed amount for *assessment year 2026 = income year **2025***. This off-by-one is the single largest source of confusion in the preliminary research, and it is what makes the three figures look contradictory.

Confirmed against two independent sources:
- Practicali, *De geïndexeerde bedragen aanslagjaar 2026*: aanslagjaar 2026 corresponds to income earned in calendar year **2025**; belastingvrije som = **10,910**.
- Attentia (FR, 27 Feb 2026): *"Pour l'année de revenus 2025, la quotité exemptée d'impôt de base était de 4 785 euros, non indexée, ou de 10 910 euros, indexée."*

### 2.2 The official indexation notice — FOUND, decisive primary source

**Bericht in verband met de automatische indexering inzake inkomstenbelastingen — Aanslagjaar 2027**
Belgisch Staatsblad **12 August 2026**, p. 43734, **NUMAC 2026006085**.

This is the FPS Finance indexation notice, published **after** the reform law and **two days before** this investigation. Its tables are embedded as images in the HTML view (*"Voor de raadpleging van de tabel, zie beeld"*), so the edition PDF was downloaded and the text layer extracted directly.

The notice explicitly cites the reform: *"Het bedrag bedoeld in artikel 41, § 2, eerste lid, 1°, van de wet van 15 juli 2026 tot hervorming van de personenbelasting..."*

**Indexation coefficient**, art. 178, §§ 1 and 2 WIB 92, aanslagjaar 2027: **2,3356** (avg. 2025 index 135.30 ÷ avg. 1988 index 57.93).

**Table I, verbatim:**

```
Art. 131, 1ste lid   Belastingvrije som :                          4.945    11.550
           3de lid   Verhoging voor gehandicapte belastingplichtige:  870     2.030
```

**This is the definitive figure: EUR 11,550.00 for assessment year 2027 = income year 2026.**

The same notice also confirms, from **Table III A** (coefficient 2,0592) and **Table II** (coefficient 2,2793), that several other CCG parameters *are* correct:

| Parameter | Base | Indexed AJ2027 | CCG value | Verdict |
|---|---|---|---|---|
| Art. 130 bracket 1 ceiling | 8.120 | **16.720** | 16,720 | ✅ correct |
| Art. 130 bracket 2 ceiling | 14.330 | **29.510** | 29,510 | ✅ correct |
| Art. 130 bracket 3 ceiling | 24.800 | **51.070** | 51,070 | ✅ correct |
| Art. 51 forfaitaire beroepskosten, employees, max | 2.950,00 | **6.070** | 6,070 | ✅ correct |

So the reform did **not** touch the brackets or the expense cap. The allowance is the isolated break.

### 2.3 The Annex III amendment — FOUND, but it does NOT change the allowance

This is the key negative finding, and it is confirmed from the full primary text, not inferred.

**Koninklijk besluit van 24 juli 2026 tot wijziging van de toepassingsregels voor de bedrijfsvoorheffing**
Belgisch Staatsblad **30 July 2026, Ed. 2**, p. 41276, **NUMAC 2026005690**.

This decree *does* amend Annex III, and its preamble *does* invoke the reform:

> *"Overwegende de wet van 15 juli 2026 tot hervorming van de personenbelasting, **artikelen 31, 47, 50 en 96**"*

It implements only articles 31, 47, 50 and 96 of the reform law — **not article 2**, which is the article that raises the basic exempted amount. Its stated rationale is deliberately partial:

> *"dat het van belang is dat de belastingplichtigen zo spoedig mogelijk het voordeel genieten van **bepaalde** maatregelen die een weerslag hebben op hun maandelijkse bezoldiging"*

Its operative articles, in full, concern:

| Art. | Change to Annex III | Effect from |
|---|---|---|
| 1 | Nr. 131: maintenance payments to non-residents, taxable share 80% → **70%** | date of publication |
| 2 | Nr. 45.2: overtime relief base **180 h/year** general; **360 h** hotel sector (PC 302 / temp agency where user is hotel); **280 h** road/rail works with electronic presence registration | **1 January 2026** |
| 3 | Nr. 45.3: art. 38, §1, 1st para. 30° → **29°/1 and 30°** | **1 April 2026** |
| 4 | **Nr. 46.2.2: fiscal work bonus very-low-wage component 52,54% → 63%** (for aanslagjaren 2027 and 2028) | **1 August 2026** |
| 5 | Nr. 78.3.2, new 5° and 6°: no withholding on leefloon / equivalent integration income | **1 January 2026** |
| 6 | Young athletes: minimum age 16 → 15; corrects a date error in Annex III | 1° from 1 Aug 2026; 2° from 1 Jan 2026 |

**No provision changes the tax-free allowance.** Entry-into-force article, verbatim:

> *"Artikel 1 treedt in werking op de dag van de bekendmaking van dit besluit in het Belgisch Staatsblad. De artikelen 2, 5 en 6, 2°, hebben uitwerking met ingang van 1 januari 2026. Artikel 3 heeft uitwerking met ingang van 1 april 2026. De artikelen 4, en 6, 1°, treden in werking op 1 augustus 2026."*

### 2.4 Proof that no other Annex III amendment exists

Two independent checks:

**(a) The 24 July 2026 decree's own preamble enumerates the Annex III chain**, and it is short:

> *"Gelet op het KB/WIB 92: — artikel 88, gewijzigd bij het koninklijk besluit van 19 december 2022; — nummer 131 van de bijlage III zoals vervangen door het koninklijk besluit van 12 december 2024; — **bijlage III, vervangen bij het koninklijk besluit van 11 december 2025**;"*

No intervening amendment is listed. Compare the equivalent line in the **KB of 11 December 2025** (BS 29 Dec 2025), which by contrast listed all three predecessors: *"bijlage III, vervangen bij het koninklijk besluit van 12 december 2024 en gewijzigd bij de koninklijke besluiten van 17 mei 2025 en 18 augustus 2025"*. The drafting convention is to enumerate exhaustively. **Therefore Annex III was untouched between 1 January 2026 and 24 July 2026**, and the 24 July decree is the only 2026 amendment.

**(b) Full sweep of the Belgisch Staatsblad from the reform law's publication to today.** Every edition was checked for FOD Financiën laws and royal decrees: **29, 30, 31 July and 3, 4, 5, 6, 7, 10, 11, 12, 13, 14 August 2026** (1–2 and 8–9 August were weekends; the Staatsblad publishes on working days only). Results:

- 29 Jul — the reform law (2026005724)
- 30 Jul Ed. 2 — the Annex III decree above (2026005690), no allowance change
- 5 Aug — KB of 22 July 2026, exemption from remitting withholding for overtime and seasonal fruit/vegetable workers (2026005926); art. 275/13 WIB 92, unrelated to the allowance
- 12 Aug — the AJ 2027 indexation notice (2026006085)
- all other editions — personnel notices, unclaimed estates, unrelated matters

**Conclusion for task 1: there is no post-reform Annex III amendment implementing the new allowance. It does not exist as at 14 August 2026.** The reform's increase has reached the *assessment* rules (art. 131 WIB 92, and the official indexation notice) but has **not** reached the *withholding* rules.

This was foreseen. Acerta, on the bill's submission: *"Voor de toepassing van de maatregelen bij de berekening van de bedrijfsvoorheffing zullen ze nog omgezet moeten worden in een wijziging van Bijlage III bij het KB/WIB 92."* And ZigZagHR, early August 2026: *"De tabellen voor de bedrijfsvoorheffing zullen daarom naar verwachting binnenkort via een koninklijk besluit worden aangepast. Zolang die niet zijn aangepast, zullen werknemers het verschil nog niet meteen op hun loonbrief zien."*

---

## 3. Task 2 — temporal scope and true-up

### 3.1 Does the reform apply to the whole of income year 2026?

**Yes, to the whole of it, for personal income tax purposes.** Article 4 of the law makes article 2, 1° *"van toepassing vanaf aanslagjaar 2027"*. Belgian assessment years attach to a whole income year: assessment year 2027 covers income earned 1 January – 31 December 2026 in its entirety. There is **no** partial-year, pro-rata or later-effective-date mechanism for the allowance. An employee's final 2026 tax liability is computed on EUR 11,550 for the full year regardless of when in 2026 the income arose.

Note the contrast with the *other* reform measures, several of which **do** carry specific dates — the fiscal work bonus component moves to 63% only **from 1 August 2026**, and the overtime threshold changes were given retroactive effect **to 1 January 2026**. The allowance is not date-split; the work bonus is.

### 3.2 Is there a retroactive true-up in payroll?

**No. There is no payroll true-up mechanism, and none is required.**

Reasoning, in order of strength:

1. **Nothing to true up against.** A true-up presupposes an amended withholding rule to recompute against. Annex III still carries the pre-reform allowance (§2.3–2.4). Payroll run on EUR 11,170 in 2026 is running *the rule that is in force*, not a stale rule.

2. **Withholding is an advance payment, settled at assessment.** Bedrijfsvoorheffing is credited against the final personal income tax liability, and any excess is refunded on assessment. The employee loses nothing permanently: the EUR 11,550 allowance is applied in full when the 2026 income is assessed in 2027, and the over-withholding comes back as a refund. The gap is a **cash-flow timing difference, not a compliance exposure.**

3. **When the legislator wants a payroll correction, it says so explicitly.** The 24 July 2026 decree is direct evidence. For over-withheld tax on capitalised maintenance payments it recites: *"dat de teveel ingehouden bedrijfsvoorheffing op onderhoudsuitkeringen uitgekeerd onder de vorm van een kapitaal ook zo snel mogelijk moet kunnen worden rechtgezet en doorgestort aan de verkrijgers van de onderhoudsgelden"*. No comparable recital exists for the allowance — because no allowance change was made.

4. **Precedent for retroactive Annex III effect exists but does not imply recomputation.** Articles 2, 5 and 6, 2° of the 24 July decree took effect *"met ingang van 1 januari 2026"*, i.e. retroactively over seven months of already-processed payroll. Belgian practice for such retroactive Annex III changes is prospective application in the next available run, not reissue of prior payslips. **Practical implication for the eventual allowance decree:** if FPS Finance follows this pattern and backdates the amended allowance to 1 January 2026, the CCG must state that the correction is absorbed going forward and reconciled at assessment — it must *not* promise a retroactive payslip rerun.

**What the CCG should say:** for income year 2026 the withholding applies EUR 11,170 while the final assessment applies EUR 11,550; the difference is refunded on assessment; a mid-year Royal Decree amending Annex III is expected and, if backdated, is to be absorbed prospectively.

---

## 4. Task 3 — the exact figure, and why not the other two

**Use EUR 11,170.00 in the CCG and WTC withholding computation, with a step-G reduction of EUR 2,987.98,** and document EUR 11,550.00 separately as the assessment-year figure.

### 4.1 Where 11,170 comes from, and why it is not a typo for 11,180

The two figures differ by a **rounding convention**, and the convention is verifiable on an independent year:

| Income year | art. 131 indexed (unrounded) | PIT / assessment — rounded to *nearest* 10 | Annex III / withholding — rounded *down* to lower 10 |
|---|---|---|---|
| 2025 | 4,785 × 2.2793 = **10,906.41** | **10,910** ✅ Practicali, Attentia | **10,900** ✅ Attentia, quoted in `APRIL_SALARY_INVESTIGATION.md` |
| 2026 (pre-reform) | 4,785 × 2.3356 = **11,175.85** | **11,180** ✅ Practicali AJ2027 | **11,170** ✅ Securex NL + FR |
| 2026 (post-reform) | 4,945 × 2.3356 = **11,549.53** | **11,550** ✅ BS 12 Aug 2026 | *see §4.3* |

The pattern holds in both years, in both directions, from independent sources. The EUR 10 gap is systematic, not an error. This also retrospectively explains the Attentia quote already recorded in `APRIL_SALARY_INVESTIGATION.md` (10,900 for 2025) which had looked anomalous against the 10,910 assessment figure.

Corroboration of the 11,170 withholding figure, two independent language versions of the same house, plus internal arithmetic:

- Securex NL, *Maandelijkse bezoldigingen*, last updated **20 February 2026**: *"belastingvrije som van 11.170 euro"*, basisbelasting reduced by *"2.987,98 euro"* (and *"5.975,96 euro"* = 2 × 2,987.98 for the two-earner case).
- Securex FR, *Rémunérations mensuelles*: reduction of *"2.987,98 euros (soit l'impôt sur le montant de base de la quotité exemptée de 11.170 euros)"*.
- Arithmetic check: 11,170 × 26.75% = 2,987.975 → **2,987.98** exactly. The CCG's own method (allowance × 26.75%) is therefore **correct**; only the amount fed into it is wrong.

### 4.2 Why not 11,550 in the CCG's step G

EUR 11,550 is the art. 131 WIB 92 amount used at **assessment**. Annex III is a separate instrument with its own amounts, and it has not been amended (§2.3). Putting 11,550 into the withholding formula today would describe a withholding computation that no payroll engine in Belgium is lawfully performing, and would under-withhold by roughly EUR 8 per employee per month.

### 4.3 The figure to expect when Annex III is eventually amended — PROJECTION, not a source

If the round-down convention in §4.1 holds, the amended Annex III allowance will be **EUR 11,540**, reduction **EUR 3,086.95**. If FPS Finance instead adopts the assessment figure directly it will be **EUR 11,550**, reduction **EUR 3,089.63**.

⚠️ **This is a derived projection from a two-datapoint pattern, not a sourced figure. Do not put it in the CCG.** It is recorded here only so that the fix in §5 can be scoped for either outcome.

---

## 5. Downstream impact inventory — scoping only, not applied

### 5.1 Statements of the parameter (text edits, no arithmetic)

| Location | Current text | Note |
|---|---|---|
| `m06_tax.md:99` | decision tree — "basic tax-free allowance EUR 11,180 (income year 2026)" | |
| `m06_tax.md:133` | formula step 7 — "26.75% x (11,180 + dependant supplements)" | |
| `m06_tax.md:179` | rates section — "Basic tax-free allowance: **EUR 11,180**" | |
| `m06_tax.md:243` | "annual net taxable income ... at or below EUR 11,180 has a computed withholding of zero" | threshold → 11,170 |
| `m07_deductions.md:29` | "basic allowance **EUR 11,180**" | |
| `m12_examples.md:5` | examples preamble — "basic tax-free allowance EUR 11,180" | |
| `02-wtc/be_wtc_data_part7.py:60` | "less 26.75% x (EUR 11,180 basic tax-free allowance + …)" | rebuild WTC after edit |
| `02-wtc/build_be_wtc.py:550` | "Basic allowance EUR 11,180. Supplements: …" | rebuild WTC after edit |

The WTC carries the allowance **only as descriptive text** — no computed withholding amounts were found in `02-wtc/`. The WTC fix is two string edits plus a rebuild and selfcheck; there is no arithmetic to redo.

### 5.2 Chained arithmetic in the CCG worked examples

Every example below chains: **step G → annual withholding → monthly withholding → net pay** (and, in one case, → garnishment). Recomputed at 11,170 (reduction 2,987.98), and also shown at 11,540 for the eventual post-reform decree.

| Example | Line | Tax before reductions (F) | G now | Annual now | Monthly now | **Monthly @ 11,170** | Monthly @ 11,540 |
|---|---|---|---|---|---|---|---|
| m06 §6.1 single, 4,000 | 156–158 | 12,906.21 | 2,990.65 | 9,915.56 | 826.30 | **826.52** | 818.27 |
| m06 §6.1 two children | 162 | 12,906.21 | 4,389.68 | 8,516.53 | 709.71 | **709.93** ⚠️ | — |
| m06 Example 2, scale III | 349 | — | — | — | comparison sentence: "EUR 249.22 per month, or EUR 2,990.65 per year" | **249.00 / 2,987.98** | 257.25 / 3,086.95 |
| m12 E1, 3,500 | 24–26 | 10,394.81 | 2,990.65 | 7,404.16 | 617.01 | **617.24** | 608.99 |
| m12 E2, 1,300 | 60–62 | 2,711.25 | 2,990.65 | 0.00 (floored) | 0.00 | **0.00 — unchanged** | 0.00 |
| m12 E3, 4,200 + pension | 87–90 | 13,910.77 | 2,990.65 | 10,488.12 | 874.01 | **874.23** | 865.99 |
| m12 E4, 2,800 + 1 child | 117–120 | 7,874.76 | 3,533.68 | 3,576.08 | 298.01 | **298.23** ⚠️ | — |
| m12 E5, 3,800 + car | 161–163 | 13,449.57 | 2,990.65 | 10,458.92 | 871.58 | **871.80** | 863.55 |
| m12 E6, blue-collar | 217–220 | 7,159.26 | 2,990.65 | 3,403.61 | 283.63 | **283.86** | 275.61 |

⚠️ = also depends on the dependent-child supplements, which are separately suspect — see §5.4.

**Net-pay and second-order lines that must follow:**

| Example | Line | Current | @ 11,170 |
|---|---|---|---|
| m12 E1 net pay | 29, 43 | 2,377.91 | **2,377.68** (and the employer-cost ratio sentence at line 43) |
| m12 E3 net pay | 94 | 2,593.45 | **2,593.23** |
| m12 E4 net for art. 1409 | 122 | 2,246.53 | **2,246.31** |
| m12 E4 garnishment, 4th band (100%) | 132 | 319.53 | **319.31** |
| m12 E4 total attachable | 133 | 450.73 | **450.51** |
| m12 E4 net before attachment | 137 | 2,246.53 | **2,246.31** |
| m12 E4 net paid to employee | 140 | 1,772.91 | **1,772.91 — unchanged** ✅ |
| m12 E4 maintenance-debt sentence | 142 | "the full EUR 2,246.53 would have been attachable" | **2,246.31** |
| m12 E5 net of ordinary remuneration | 189 | 2,431.76 | **2,431.54** |
| m12 E5 net paid in quarter-end month | 192 | 4,035.18 | **4,034.96** |
| m12 E6 net pay | 222 | 2,120.80 | **2,120.57** |

Two useful properties of this fix:

- **m12 E2 is fully insulated.** Its withholding is floored at zero under every candidate figure, so no line changes. Only the general threshold sentence at `m06_tax.md:243` needs the new number.
- **m12 E4's final net is self-cancelling.** The EUR 0.22 fall in net lands entirely in the 100%-attachable band, so the attachment absorbs it and *"Net paid to the employee"* stays at EUR 1,772.91. Worth stating explicitly in the fix ticket so a reviewer does not "correct" it.

**Not affected:** the special social security contribution bands (driven by quarterly *wage*, not by withholding), employer social security, the CO2 solidarity contribution, meal-voucher shares, the 108% blue-collar uplift, double-holiday-pay withholding (its own percentage table, keyed on annual gross), and the bonus/exceptional-payment tables. The bracket ceilings 16,720 / 29,510 / 51,070 and the EUR 6,070 expense cap are confirmed correct (§2.2) and must **not** be touched.

### 5.3 Legal-basis citations to refresh

`m06_tax.md:164` and `m12_examples.md:226` both cite *"Annex III … as replaced by the Royal Decree of 11 December 2025"*. That citation is still accurate as the replacing instrument, but it is now **incomplete**: Annex III has since been amended by the **Royal Decree of 24 July 2026** (BS 30 July 2026, Ed. 2). Both citations should be extended, and the reform law itself (**Law of 15 July 2026**, BS 29 July 2026) added wherever art. 131 WIB 92 is cited.

### 5.4 Adjacent defects surfaced by this investigation — flagged, NOT resolved

These fall outside the allowance question but were exposed by the same primary sources, and they touch the same worked examples. **Each needs its own verification pass before anything is changed.**

**(a) The dependent-child supplements look wrong.** The CCG states (m06:100–101, m06:179, m07:29, WTC ×2): EUR **2,030** for one child, **5,230** for two, **11,720** for three. The official AJ 2027 figures in Table II of the 12 August 2026 indexation notice (coefficient 2,2793) are:

| Art. 132, 1st para. | Base | Indexed AJ2027 |
|---|---|---|
| 1° one child | 935 | **2.130** |
| 2° two children | 2.250 | **5.130** |
| 3° three children | 5.020 | **11.440** |
| 4° four children | 8.120 | **18.510** |
| 5° per child above the fourth | 3.100 | **7.070** |
| 6° additional, each child under 3 with no childcare deduction | 325 | **740** |
| 7° dependant aged 66+ requiring care | 2.610 | **5.950** |
| 8° any other dependant | 870 | **1.980** |

None of the CCG's three figures matches. Worse, **EUR 2,030 is exactly the AJ 2027 art. 131, 3rd para. supplement for a *disabled taxpayer*** (base 870), per Table I — which suggests a category mix-up rather than a stale-year problem. The reform law's article 3 amends art. 132 alongside art. 131, so the pre-reform AJ2027 values were probably different again. **Do not assume Annex III uses the art. 132 amounts** — the withholding annex may express family reductions differently. Verify against the Annex III text before touching m06:100–101, m06:162, m12 E4, or the WTC strings.

**(b) The fiscal work bonus is out of date from 1 August 2026.** Article 4 of the KB of 24 July 2026 raises the very-low-wage component in Annex III nr. 46.2.2 from **52,54% to 63%** for assessment years 2027 and 2028, in force **1 August 2026** — i.e. two weeks ago. The CCG uses a flat *"Fiscal work bonus | Annual maximum of 765.00"* in m12 E4 (line 118) and E6 (line 218). The 52,54% figure is corroborated as the old value by SSGPI service note SSGPI-RIO-2026/9 of 8 January 2026 (*"52,54 % du montant du volet B du bonus à l'emploi réellement accordé"*). This is a live, dated change affecting two worked examples.

**(c) The overtime relief threshold.** Article 2 of the same decree sets the Annex III base at **180 hours** generally, **360** for the hotel sector, **280** for qualifying road/rail works — with retroactive effect to **1 January 2026**. `m06_tax.md:105` says *"overtime relief on up to 180 hours per year"*, which is right for the general case but silent on the two raised ceilings.

**(d) The "1 July 2026" work bonus note.** `m12_examples.md:5` refers to *"social work bonus parameters in force from 1 July 2026"*. That is the **social** work bonus (NSSO), distinct from the **fiscal** reduction in (b), which changed on **1 August 2026**. The examples should not conflate the two dates.

---

## 6. Confidence

| Claim | Confidence | Basis |
|---|---|---|
| Reform law is the Law of 15 July 2026, BS 29 July 2026, NUMAC 2026005724 | **Certain** | Staatsblad summary + article text |
| Art. 131 non-indexed base 4,785 → 4,945 from aanslagjaar 2027 | **Certain** | Art. 2 and 4 of the law, primary text |
| Aanslagjaar 2027 = income year 2026, whole year, no partial-date rule | **Certain** | Art. 4 of the law; Belgian assessment-year structure; corroborated by Attentia's AJ table |
| **Indexed art. 131 amount for income year 2026 = EUR 11,550** | **Certain** | BS 12 Aug 2026 Table I, verbatim: `4.945  11.550`; arithmetic 4,945 × 2.3356 = 11,549.53 |
| Brackets 16,720 / 29,510 / 51,070 and cap 6,070 unchanged | **Certain** | BS 12 Aug 2026 Tables III A |
| No post-reform Annex III amendment to the allowance exists as at 14 Aug 2026 | **High** | KB 24 July 2026 full text (implements only arts. 31/47/50/96); its preamble's exhaustive Annex III chain; complete Staatsblad sweep 29 Jul – 14 Aug 2026 |
| **Annex III withholding allowance in force = EUR 11,170, reduction EUR 2,987.98** | **High, not certain** | Securex NL (20 Feb 2026) + Securex FR, independently; exact arithmetic 11,170 × 26.75% = 2,987.98; round-down convention independently confirmed on income year 2025 (10,900 vs 10,910). ⚠️ **Not verified against the Annex III text itself** — the annex in the BS of 29 Dec 2025 is embedded with a non-standard font encoding and is not machine-readable. |
| EUR 11,180 is wrong for income year 2026 | **Certain** | It is neither 11,170 nor 11,550; Attentia states explicitly it was the no-reform counterfactual |
| Post-amendment Annex III figure will be EUR 11,540 | **Projection only** | Two-datapoint rounding pattern. Do not rely on it. |
| Child supplements 2,030 / 5,230 / 11,720 are wrong | **Probable, needs own pass** | Mismatch against BS 12 Aug 2026 Table II; 2,030 collides exactly with the disabled-taxpayer supplement |

**The one residual gap.** The EUR 11,170 figure rests on high-quality secondary sources plus a confirmed arithmetic pattern, not on the Annex III text. To close it, obtain a readable copy of Annex III as replaced by the KB of 11 December 2025 — via Fisconetplus, the FPS Finance "Regels 1 januari 2026" publication for social secretariats, or the `Bijlage-III-KB-WIB-2026` PDF linked from the Securex Annex III overview page. The FPS Finance calculation page currently lists only up to the 2025 rules. **This should be done before the fix is applied**, because it is the single number the whole fix turns on.

---

## 7. Recommendation

1. **Do not adopt EUR 11,550 in the withholding computation.** It is the correct assessment figure and the wrong withholding figure.
2. **Correct the withholding computation to EUR 11,170 / reduction EUR 2,987.98**, after closing the residual gap in §6.
3. **Add an explicit two-figure explanation** to Module 6: withholding runs on the Annex III amount, the final assessment runs on EUR 11,550 under the Law of 15 July 2026, and the difference is refunded on assessment. This is a genuine feature of income year 2026 and a client will ask about it.
4. **Add a watch item** for the Royal Decree amending Annex III for the allowance. It is expected imminently and, on the evidence of the 24 July decree, may be backdated to 1 January 2026. When it lands, the §5.2 table gives the recomputation at 11,540; re-verify the figure against the decree rather than using the projection.
5. **Open three separate tickets** for §5.4 (a) child supplements, (b) fiscal work bonus 63% from 1 August 2026, (c) overtime ceilings 360/280. Item (b) is already in force and affects two worked examples.
6. **Refresh the legal-basis citations** per §5.3.

---

## 8. Sources

**Primary — Belgisch Staatsblad / Moniteur belge (via ejustice.just.fgov.be)**

- Wet van 15 juli 2026 tot hervorming van de personenbelasting — BS 29.07.2026, p. 40196, NUMAC 2026005724
- Koninklijk besluit van 24 juli 2026 tot wijziging van de toepassingsregels voor de bedrijfsvoorheffing — BS 30.07.2026 Ed. 2, p. 41276, NUMAC 2026005690
- Bericht in verband met de automatische indexering inzake inkomstenbelastingen — Aanslagjaar 2027 — BS 12.08.2026, p. 43734, NUMAC 2026006085
- Koninklijk besluit van 11 december 2025 tot wijziging van het KB/WIB 92, op het stuk van de bedrijfsvoorheffing — BS 29.12.2025, p. 97613 (Annex III replaced; annex text not machine-readable)
- KB van 22 juli 2026, vrijstelling doorstorting bedrijfsvoorheffing, overuren en gelegenheidsarbeiders fruit/groenteteelt — BS 05.08.2026, NUMAC 2026005926
- Staatsblad summaries, all editions 29.07.2026 – 14.08.2026

**Official / semi-official**

- SSGPI service note SSGPI-RIO-2026/9, 8 January 2026, *Calcul du précompte professionnel (applicable à partir du 01-01-2026)*

**Secondary — Annex III figures and reform commentary**

- [Securex — Maandelijkse bezoldigingen (bijlage III), last updated 20 Feb 2026](https://www.securex.be/nl/lex4you/werkgever/themas/verlonen/fiscale-loonlasten-bedrijfsvoorheffing/maandelijkse-bezoldigingen-\(en-ermee-gelijkgestelde-inkomsten,-met-uitzondering-van-vervangingsinkom) — 11.170 / 2.987,98
- [Securex — Rémunérations mensuelles (annexe III)](https://www.securex.be/fr/lex4you/employeur/themes/remunerer/charges-salariales-le-precompte-professionel/remunerations-mensuelles-\(et-revenus-y-assimiles,-a-l-exception-des-revenus-de-remplacement\)) — 2.987,98 = tax on 11.170
- [Attentia — Réforme de l'IPP : impact sur la rémunération en 2026, 27 Feb 2026](https://www.attentia.be/fr/actualites/reforme-de-limpot-des-personnes-physiques-impact-sur-la-remuneration-en-2026/) — 4,785/10,910 for income year 2025; 11,180 as counterfactual; 4,945/11,550 for income year 2026
- [Practicali — De geïndexeerde bedragen aanslagjaar 2027, 6 Jan 2026](https://www.practicali.be/blog/geindexeerde-bedragen-aj-2027) — 11,180 indexed, 11,550 flagged as proposed
- [Practicali — De geïndexeerde bedragen aanslagjaar 2026](https://www.practicali.be/blog/geindexeerde-bedragen-aj-2026) — AJ2026 = income year 2025, 10,910
- [Acerta — Wetsontwerp hervorming personenbelasting: impact op de loonverwerking](https://www.acerta.be/nl/inspiratie/wetsontwerp-tot-hervorming-van-de-personenbelasting-ingediend-de-kamer-impact-op-de-loonverwerking) — Annex III amendment still required
- [ZigZagHR — Fiscale hervorming: dit verandert voor nettoloon, overuren en werkbonus](https://zigzaghr.be/fiscale-hervorming-dit-verandert-voor-nettoloon-overuren-en-werkbonus/) — withholding tables not yet adapted, early Aug 2026
- [SYNOVA — Wet tot hervorming personenbelasting, 13 Jul 2026](https://www.synova.be/nl/nieuws-info/wet-tot-hervorming-personenbelasting-wat-verandert) — 11,550 for aanslagjaar 2027; benefit ≈ EUR 92.50/year = (11,550 − 11,180) × 25%
- [Securex — Nieuwe regels bedrijfsvoorheffing voor 2026, 29 Dec 2025](https://www.securex.be/nl/lex4you/werkgever/nieuws/nieuwe-regels-bedrijfsvoorheffing-voor-2026-40ec0964b78d053e5fc7e243df8d4f0a) — cites KB 11 Dec 2025
- [Securex — Wet over de personenbelasting wijzigt fiscaal landschap, 13 Jul 2026](https://www.securex.be/nl/lex4you/werkgever/nieuws/wet-tot-hervorming-van-de-personenbelasting-wijzigt-fiscaal-landschap)
- [Liantis — Belastingvrije som stijgt stapsgewijs vanaf 2026](https://www.liantis.be/nl/nieuws/hervorming-personenbelasting-belastingvrije-som-stijgt-stapsgewijs-vanaf-2026)

**Sources found to be unreliable on this point** — these state the allowance rises *"van € 10.910 (inkomstenjaar 2026)"*, mislabelling the assessment year as the income year: [Sodalis](https://sodalis.be/nl/wet-tot-hervorming-van-de-personenbelasting-goedgekeurd/), [Accountants Academy, 4 Aug 2026](https://nieuws.accountantsacademy.be/hervorming-personenbelasting-2026-dit-verandert-fiscaal) (both citing Securex).
