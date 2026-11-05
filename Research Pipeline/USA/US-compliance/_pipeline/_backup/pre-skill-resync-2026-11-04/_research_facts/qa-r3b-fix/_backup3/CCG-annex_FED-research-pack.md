# CCG annex_FED research pack — Federal layer

> **Synthesis C (2026-11-02).** Register ids were normalized to the facts-schema pattern (map: `_research/stage5/ID-RENAME-MAP.csv`, ids in this pack already rewritten). Every fact that was held for the register_id pattern defect (marked here as "legacy id, NOT a fact", "PENDING", "(P)", "parked" or "carried in unresolved") is now a validated fact in `facts[]`; promotion log `_research/synthesis-C/_work/step2-promotion-log.csv`. Counts of held facts quoted below are historical. The Open questions block below mirrors the current `unresolved[]`.

Synthesis B, 2026-11-02. Source: `_research/stage5/FED.md` and the active/partial rows of `00-official-sources/legal-basis-register.csv`; no fetching. Facts file: `_research/CCG-annex_FED-facts.json` (validator: PASS). Every value below is a fact object there; key in backticks, register id in brackets. Keys use the `fed.` prefix (state annexes use `{jur}.`, the routing layer `multi.`).

**Summary.** The federal layer is one calculation per employee on top of every State: FIT under Pub. 15-T 2026 (Worksheet 1A, annual percentage method), FICA (OASDI 6.2% + 6.2% to 184,500; Medicare 1.45% + 1.45%; Additional Medicare 0.9% employee-only over 200,000), FUTA (net 0.6% on 7,000 plus any credit reduction), deposits (lookback), Form 941/940/944, W-2/W-3 with the new P.L. 119-21 codes TP/TT/TA and box 14b, ACA 1094-C/1095-C, new-hire reporting, and the CCPA/levy/IWO garnishment floor. No federal pay-statement statute: payslip content is State law. Stage-5 confidence: high except the 2026 FUTA credit reductions (final after 2026-11-10) and EFW2 TY2026 (gated).

**Reuse rule carried from Stage 5.** Rows US-FED-001..030 stay active but have no local file; the US-FEDS5 rows carry the local copies and are cited first. Supersession applied at the merge: US-FEDS5-028 supersedes US-FEDP6-001 and closes the gated US-FEDR3-004 (IWO renewal approved 2026-08-25, expiry 2029-08-31) — this replaces the "renewal pending" modelling of US-OWN-007.

**Language (US-OWN-006).** Federal: English is the only official language and places no obligation on private employers [US-FED-020]; no federal instrument fixes pay-statement content or language [US-FED-010, US-FEDS5-021]; IRS/SSA filings in English. Spanish (rank 2) and other-language seams attach only to State notices/posters (State annexes).

## 1 — Employment / labour code
FLSA floor; the employer pays the highest of federal, State and local minimum (State annexes). Pay frequency, pay-day timing and method of payment have no federal rule.

- `fed.minwage.hourly` = **7.25** USD (2009-07-24 → open) [A.1, US-FEDS5-017, quoted from authority page, conf high] — FLSA 206(a)(1)(C); not indexed; no 2026/2027 change enacted. Employer pays the highest of federal, state and local minimum (state annexes).
- `fed.overtime.weekly_threshold_hours` = **40** hours (1938-10-24 → open) [A.1, US-FEDS5-018, quoted from authority page, conf high] — No federal daily overtime; daily OT is state law (state annexes).
- `fed.overtime.premium.multiplier` = **1.5** ratio (1938-10-24 → open) [A.1, US-FEDS5-018, quoted from authority page, conf high] — 0.5 premium portion = qualified overtime compensation for P.L. 119-21 / W-2 code TT.
- `fed.tipped.cash_wage.hourly` = **2.13** USD (1996-08-20 → open) [A.1, US-FEDS5-019, quoted from authority page, conf high]
- `fed.tipped.tip_credit.max_hourly` = **5.12** USD (1996-08-20 → open) [A.1, US-FEDS5-019, derived arithmetically, conf high] — 7.25 - 2.13 = 5.12 (US-FEDS5-017 minimum wage minus cash wage).
- `fed.tipped.monthly_tips_threshold` = **30** USD (1996-08-20 → open) [A.1, US-FEDS5-019, quoted from authority page, conf high] — Tipped employee = customarily and regularly receives more than 30/month in tips (29 USC 203(t)).
- `fed.exempt.salary_floor.weekly` = **684** USD (2020-01-01 → open) [A.1, US-FEDS5-020, quoted from authority page, conf high] — EAP exemption, 29 CFR 541.600 current eCFR text (2024 increase not in the CFR).
- `fed.exempt.salary_floor.biweekly` = **1368** USD (2020-01-01 → open) [A.1, US-FEDS5-020, quoted from authority page, conf high] — EAP exemption, 29 CFR 541.600 current eCFR text (2024 increase not in the CFR).
- `fed.exempt.salary_floor.semimonthly` = **1482** USD (2020-01-01 → open) [A.1, US-FEDS5-020, quoted from authority page, conf high] — EAP exemption, 29 CFR 541.600 current eCFR text (2024 increase not in the CFR).
- `fed.exempt.salary_floor.monthly` = **2964** USD (2020-01-01 → open) [A.1, US-FEDS5-020, quoted from authority page, conf high] — EAP exemption, 29 CFR 541.600 current eCFR text (2024 increase not in the CFR).
- `fed.exempt.salary_floor.territories_weekly` = **455** USD (2020-01-01 → open) [A.1, US-FEDS5-020, quoted from authority page, conf high] — CNMI, Guam, PR, USVI.
- `fed.exempt.salary_floor.american_samoa_weekly` = **380** USD (2020-01-01 → open) [A.1, US-FEDS5-020, quoted from authority page, conf high]

## 2 — Income tax
G-DERIVE: column C of the three STANDARD schedules recomputed in Python from column A and the rates; top values equal the row (206,583.50 / 192,979.25 / 191,171.00). Zero brackets = 2026 standard deduction minus line 1g, standard deductions confirmed in a second document family (Rev. Proc. 2025-32). The Step-2-checked schedule thresholds are transcribed; their column C was not compared with the publication and is not emitted. Local income tax and reciprocity are not federal (annex_MULTI, State annexes).

- `fed.fit.method` = **IRS Pub. 15-T (2026) Worksheet 1A with the Annual Percentage Method tables (STANDARD schedule; Step-2-checked schedule when W-4 Step 2 box checked)**  (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high] — LEVEL: withholding.
- `fed.fit.worksheet1a.line1g.mfj` = **12900** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high] — Applied when the W-4 Step 2 box is NOT checked.
- `fed.fit.worksheet1a.line1g.other` = **8600** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.allowance.pre2020_value` = **4300** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high] — Per allowance on a pre-2020 Form W-4 (line 1k).
- `fed.fit.standard.mfj.bracket.1.floor` = **0** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.standard.mfj.bracket.1.rate` = **0** percent (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.standard.mfj.bracket.1.cumulative_tax` = **0.0** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, derived arithmetically, conf high] — Column C re-derived in Python from column A thresholds and the 0/10/12/22/24/32/35/37 rates; top values 206,583.50 (MFJ) / 192,979.25 (Single) / 191,171.00 (HoH) equal the figures in US-FEDS5-001.
- `fed.fit.standard.mfj.bracket.2.floor` = **19300** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.standard.mfj.bracket.2.rate` = **10** percent (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.standard.mfj.bracket.2.cumulative_tax` = **0.0** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, derived arithmetically, conf high] — Column C re-derived in Python from column A thresholds and the 0/10/12/22/24/32/35/37 rates; top values 206,583.50 (MFJ) / 192,979.25 (Single) / 191,171.00 (HoH) equal the figures in US-FEDS5-001.
- `fed.fit.standard.mfj.bracket.3.floor` = **44100** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.standard.mfj.bracket.3.rate` = **12** percent (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.standard.mfj.bracket.3.cumulative_tax` = **2480.0** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, derived arithmetically, conf high] — Column C re-derived in Python from column A thresholds and the 0/10/12/22/24/32/35/37 rates; top values 206,583.50 (MFJ) / 192,979.25 (Single) / 191,171.00 (HoH) equal the figures in US-FEDS5-001.
- `fed.fit.standard.mfj.bracket.4.floor` = **120100** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.standard.mfj.bracket.4.rate` = **22** percent (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.standard.mfj.bracket.4.cumulative_tax` = **11600.0** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, derived arithmetically, conf high] — Column C re-derived in Python from column A thresholds and the 0/10/12/22/24/32/35/37 rates; top values 206,583.50 (MFJ) / 192,979.25 (Single) / 191,171.00 (HoH) equal the figures in US-FEDS5-001.
- `fed.fit.standard.mfj.bracket.5.floor` = **230700** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.standard.mfj.bracket.5.rate` = **24** percent (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.standard.mfj.bracket.5.cumulative_tax` = **35932.0** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, derived arithmetically, conf high] — Column C re-derived in Python from column A thresholds and the 0/10/12/22/24/32/35/37 rates; top values 206,583.50 (MFJ) / 192,979.25 (Single) / 191,171.00 (HoH) equal the figures in US-FEDS5-001.
- `fed.fit.standard.mfj.bracket.6.floor` = **422850** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.standard.mfj.bracket.6.rate` = **32** percent (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.standard.mfj.bracket.6.cumulative_tax` = **82048.0** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, derived arithmetically, conf high] — Column C re-derived in Python from column A thresholds and the 0/10/12/22/24/32/35/37 rates; top values 206,583.50 (MFJ) / 192,979.25 (Single) / 191,171.00 (HoH) equal the figures in US-FEDS5-001.
- `fed.fit.standard.mfj.bracket.7.floor` = **531750** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.standard.mfj.bracket.7.rate` = **35** percent (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.standard.mfj.bracket.7.cumulative_tax` = **116896.0** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, derived arithmetically, conf high] — Column C re-derived in Python from column A thresholds and the 0/10/12/22/24/32/35/37 rates; top values 206,583.50 (MFJ) / 192,979.25 (Single) / 191,171.00 (HoH) equal the figures in US-FEDS5-001.
- `fed.fit.standard.mfj.bracket.8.floor` = **788000** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.standard.mfj.bracket.8.rate` = **37** percent (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.standard.mfj.bracket.8.cumulative_tax` = **206583.5** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, derived arithmetically, conf high] — Column C re-derived in Python from column A thresholds and the 0/10/12/22/24/32/35/37 rates; top values 206,583.50 (MFJ) / 192,979.25 (Single) / 191,171.00 (HoH) equal the figures in US-FEDS5-001.
- `fed.fit.standard.single.bracket.1.floor` = **0** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high] — Single schedule also used for MFS.
- `fed.fit.standard.single.bracket.1.rate` = **0** percent (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.standard.single.bracket.1.cumulative_tax` = **0.0** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, derived arithmetically, conf high] — Column C re-derived in Python from column A thresholds and the 0/10/12/22/24/32/35/37 rates; top values 206,583.50 (MFJ) / 192,979.25 (Single) / 191,171.00 (HoH) equal the figures in US-FEDS5-001.
- `fed.fit.standard.single.bracket.2.floor` = **7500** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.standard.single.bracket.2.rate` = **10** percent (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.standard.single.bracket.2.cumulative_tax` = **0.0** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, derived arithmetically, conf high] — Column C re-derived in Python from column A thresholds and the 0/10/12/22/24/32/35/37 rates; top values 206,583.50 (MFJ) / 192,979.25 (Single) / 191,171.00 (HoH) equal the figures in US-FEDS5-001.
- `fed.fit.standard.single.bracket.3.floor` = **19900** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.standard.single.bracket.3.rate` = **12** percent (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.standard.single.bracket.3.cumulative_tax` = **1240.0** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, derived arithmetically, conf high] — Column C re-derived in Python from column A thresholds and the 0/10/12/22/24/32/35/37 rates; top values 206,583.50 (MFJ) / 192,979.25 (Single) / 191,171.00 (HoH) equal the figures in US-FEDS5-001.
- `fed.fit.standard.single.bracket.4.floor` = **57900** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.standard.single.bracket.4.rate` = **22** percent (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.standard.single.bracket.4.cumulative_tax` = **5800.0** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, derived arithmetically, conf high] — Column C re-derived in Python from column A thresholds and the 0/10/12/22/24/32/35/37 rates; top values 206,583.50 (MFJ) / 192,979.25 (Single) / 191,171.00 (HoH) equal the figures in US-FEDS5-001.
- `fed.fit.standard.single.bracket.5.floor` = **113200** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.standard.single.bracket.5.rate` = **24** percent (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.standard.single.bracket.5.cumulative_tax` = **17966.0** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, derived arithmetically, conf high] — Column C re-derived in Python from column A thresholds and the 0/10/12/22/24/32/35/37 rates; top values 206,583.50 (MFJ) / 192,979.25 (Single) / 191,171.00 (HoH) equal the figures in US-FEDS5-001.
- `fed.fit.standard.single.bracket.6.floor` = **209275** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.standard.single.bracket.6.rate` = **32** percent (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.standard.single.bracket.6.cumulative_tax` = **41024.0** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, derived arithmetically, conf high] — Column C re-derived in Python from column A thresholds and the 0/10/12/22/24/32/35/37 rates; top values 206,583.50 (MFJ) / 192,979.25 (Single) / 191,171.00 (HoH) equal the figures in US-FEDS5-001.
- `fed.fit.standard.single.bracket.7.floor` = **263725** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.standard.single.bracket.7.rate` = **35** percent (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.standard.single.bracket.7.cumulative_tax` = **58448.0** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, derived arithmetically, conf high] — Column C re-derived in Python from column A thresholds and the 0/10/12/22/24/32/35/37 rates; top values 206,583.50 (MFJ) / 192,979.25 (Single) / 191,171.00 (HoH) equal the figures in US-FEDS5-001.
- `fed.fit.standard.single.bracket.8.floor` = **648100** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.standard.single.bracket.8.rate` = **37** percent (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.standard.single.bracket.8.cumulative_tax` = **192979.25** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, derived arithmetically, conf high] — Column C re-derived in Python from column A thresholds and the 0/10/12/22/24/32/35/37 rates; top values 206,583.50 (MFJ) / 192,979.25 (Single) / 191,171.00 (HoH) equal the figures in US-FEDS5-001.
- `fed.fit.standard.hoh.bracket.1.floor` = **0** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.standard.hoh.bracket.1.rate` = **0** percent (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.standard.hoh.bracket.1.cumulative_tax` = **0.0** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, derived arithmetically, conf high] — Column C re-derived in Python from column A thresholds and the 0/10/12/22/24/32/35/37 rates; top values 206,583.50 (MFJ) / 192,979.25 (Single) / 191,171.00 (HoH) equal the figures in US-FEDS5-001.
- `fed.fit.standard.hoh.bracket.2.floor` = **15550** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.standard.hoh.bracket.2.rate` = **10** percent (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.standard.hoh.bracket.2.cumulative_tax` = **0.0** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, derived arithmetically, conf high] — Column C re-derived in Python from column A thresholds and the 0/10/12/22/24/32/35/37 rates; top values 206,583.50 (MFJ) / 192,979.25 (Single) / 191,171.00 (HoH) equal the figures in US-FEDS5-001.
- `fed.fit.standard.hoh.bracket.3.floor` = **33250** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.standard.hoh.bracket.3.rate` = **12** percent (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.standard.hoh.bracket.3.cumulative_tax` = **1770.0** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, derived arithmetically, conf high] — Column C re-derived in Python from column A thresholds and the 0/10/12/22/24/32/35/37 rates; top values 206,583.50 (MFJ) / 192,979.25 (Single) / 191,171.00 (HoH) equal the figures in US-FEDS5-001.
- `fed.fit.standard.hoh.bracket.4.floor` = **83000** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.standard.hoh.bracket.4.rate` = **22** percent (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.standard.hoh.bracket.4.cumulative_tax` = **7740.0** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, derived arithmetically, conf high] — Column C re-derived in Python from column A thresholds and the 0/10/12/22/24/32/35/37 rates; top values 206,583.50 (MFJ) / 192,979.25 (Single) / 191,171.00 (HoH) equal the figures in US-FEDS5-001.
- `fed.fit.standard.hoh.bracket.5.floor` = **121250** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.standard.hoh.bracket.5.rate` = **24** percent (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.standard.hoh.bracket.5.cumulative_tax` = **16155.0** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, derived arithmetically, conf high] — Column C re-derived in Python from column A thresholds and the 0/10/12/22/24/32/35/37 rates; top values 206,583.50 (MFJ) / 192,979.25 (Single) / 191,171.00 (HoH) equal the figures in US-FEDS5-001.
- `fed.fit.standard.hoh.bracket.6.floor` = **217300** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.standard.hoh.bracket.6.rate` = **32** percent (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.standard.hoh.bracket.6.cumulative_tax` = **39207.0** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, derived arithmetically, conf high] — Column C re-derived in Python from column A thresholds and the 0/10/12/22/24/32/35/37 rates; top values 206,583.50 (MFJ) / 192,979.25 (Single) / 191,171.00 (HoH) equal the figures in US-FEDS5-001.
- `fed.fit.standard.hoh.bracket.7.floor` = **271750** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.standard.hoh.bracket.7.rate` = **35** percent (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.standard.hoh.bracket.7.cumulative_tax` = **56631.0** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, derived arithmetically, conf high] — Column C re-derived in Python from column A thresholds and the 0/10/12/22/24/32/35/37 rates; top values 206,583.50 (MFJ) / 192,979.25 (Single) / 191,171.00 (HoH) equal the figures in US-FEDS5-001.
- `fed.fit.standard.hoh.bracket.8.floor` = **656150** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.standard.hoh.bracket.8.rate` = **37** percent (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.standard.hoh.bracket.8.cumulative_tax` = **191171.0** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, derived arithmetically, conf high] — Column C re-derived in Python from column A thresholds and the 0/10/12/22/24/32/35/37 rates; top values 206,583.50 (MFJ) / 192,979.25 (Single) / 191,171.00 (HoH) equal the figures in US-FEDS5-001.
- `fed.fit.step2.mfj.bracket.1.floor` = **0** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.step2.mfj.bracket.1.rate` = **0** percent (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.step2.mfj.bracket.2.floor` = **16100** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.step2.mfj.bracket.2.rate` = **10** percent (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.step2.mfj.bracket.3.floor` = **28500** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.step2.mfj.bracket.3.rate` = **12** percent (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.step2.mfj.bracket.4.floor` = **66500** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.step2.mfj.bracket.4.rate` = **22** percent (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.step2.mfj.bracket.5.floor` = **121800** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.step2.mfj.bracket.5.rate` = **24** percent (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.step2.mfj.bracket.6.floor` = **217875** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.step2.mfj.bracket.6.rate` = **32** percent (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.step2.mfj.bracket.7.floor` = **272325** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.step2.mfj.bracket.7.rate` = **35** percent (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.step2.mfj.bracket.8.floor` = **400450** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.step2.mfj.bracket.8.rate` = **37** percent (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.step2.single.bracket.1.floor` = **0** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high] — Single schedule also used for MFS.
- `fed.fit.step2.single.bracket.1.rate` = **0** percent (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.step2.single.bracket.2.floor` = **8050** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.step2.single.bracket.2.rate` = **10** percent (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.step2.single.bracket.3.floor` = **14250** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.step2.single.bracket.3.rate` = **12** percent (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.step2.single.bracket.4.floor` = **33250** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.step2.single.bracket.4.rate` = **22** percent (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.step2.single.bracket.5.floor` = **60900** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.step2.single.bracket.5.rate` = **24** percent (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.step2.single.bracket.6.floor` = **108938** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.step2.single.bracket.6.rate` = **32** percent (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.step2.single.bracket.7.floor` = **136163** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.step2.single.bracket.7.rate` = **35** percent (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.step2.single.bracket.8.floor` = **328350** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.step2.single.bracket.8.rate` = **37** percent (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.step2.hoh.bracket.1.floor` = **0** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.step2.hoh.bracket.1.rate` = **0** percent (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.step2.hoh.bracket.2.floor` = **12075** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.step2.hoh.bracket.2.rate` = **10** percent (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.step2.hoh.bracket.3.floor` = **20925** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.step2.hoh.bracket.3.rate` = **12** percent (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.step2.hoh.bracket.4.floor` = **45800** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.step2.hoh.bracket.4.rate` = **22** percent (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.step2.hoh.bracket.5.floor` = **64925** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.step2.hoh.bracket.5.rate` = **24** percent (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.step2.hoh.bracket.6.floor` = **112950** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.step2.hoh.bracket.6.rate` = **32** percent (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.step2.hoh.bracket.7.floor` = **140175** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.step2.hoh.bracket.7.rate` = **35** percent (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.step2.hoh.bracket.8.floor` = **332375** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.step2.hoh.bracket.8.rate` = **37** percent (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.std_deduction.mfj` = **32200** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-010, second independent authority, conf high] — Rev. Proc. 2025-32; G-DERIVE: standard deduction minus line 1g = zero bracket 19300 of Pub. 15-T (US-FEDS5-001).
- `fed.fit.std_deduction.single` = **16100** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-010, second independent authority, conf high] — Rev. Proc. 2025-32; G-DERIVE: standard deduction minus line 1g = zero bracket 7500 of Pub. 15-T (US-FEDS5-001).
- `fed.fit.std_deduction.hoh` = **24150** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-010, second independent authority, conf high] — Rev. Proc. 2025-32; G-DERIVE: standard deduction minus line 1g = zero bracket 15550 of Pub. 15-T (US-FEDS5-001).
- `fed.fit.pay_periods_per_year` = **2 / 4 / 12 / 24 / 26 / 52 / 260 (semiannual, quarterly, monthly, semimonthly, biweekly, weekly, daily)**  (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-001, quoted from authority page, conf high]
- `fed.fit.rounding` = **Optional: wages may be rounded to the nearest dollar and the period tax rounded to the nearest dollar (drop under 50 cents, 50-99 cents up)**  (2026-01-01 → open) [A.2, US-FED-001, quoted from authority page, conf high]
- `fed.fit.supplemental.flat_rate` = **22** percent (2026-01-01 → open) [A.2, US-FEDS5-003, quoted from authority page, conf high] — Optional flat method; made permanent by P.L. 119-21. LEVEL: withholding.
- `fed.fit.supplemental.mandatory_rate` = **37** percent (2026-01-01 → open) [A.2, US-FEDS5-003, quoted from authority page, conf high] — LEVEL: withholding.
- `fed.fit.supplemental.mandatory_threshold` = **1000000** USD (2026-01-01 → open) [A.2, US-FEDS5-003, quoted from authority page, conf high] — Supplemental wages above 1,000,000 paid to one employee in the calendar year.
- `fed.fit.backup_withholding.rate` = **24** percent (2026-01-01 → open) [A.2, US-FEDS5-003, quoted from authority page, conf high]
- `fed.w4.input_fields` = **filing status (Single/MFS, MFJ/QSS, HoH); Step 2 flag; Step 3 amount; Step 4(a); Step 4(b); Step 4(c); exempt checkbox**  (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-006, quoted from authority page, conf high]
- `fed.w4.exempt.validity` = **2026 only: the exemption checkbox certification lapses; a new W-4 is required for 2027**  (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-006, quoted from authority page, conf high]

## 2b — Non-resident regime
Non-resident aliens are treated at WITHHOLDING level: the Pub. 15-T add-on increases the wage used for the FIT computation only (no W-2, FICA or FUTA effect) and is not applied to 22%/37% supplemental wages. Notice 1392 W-4 rules; Form 8233 treaty wages go to 1042-S (IRIS e-file for TY2026). This satisfies C31 for the federal layer; State non-resident (other-State resident) treatment is annex_MULTI.

- `fed.fit.nra.addon.table2.weekly` = **309.6** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-002, quoted from authority page, conf high] — Table 2: 2020+ W-4 or first paid 2020+. Added to wages for the FIT computation only (not on W-2, no FICA/FUTA effect); not applied to 22%/37% supplemental. Annual = single standard deduction 16,100. LEVEL: withholding.
- `fed.fit.nra.addon.table2.biweekly` = **619.2** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-002, quoted from authority page, conf high] — Table 2: 2020+ W-4 or first paid 2020+. Added to wages for the FIT computation only (not on W-2, no FICA/FUTA effect); not applied to 22%/37% supplemental. Annual = single standard deduction 16,100. LEVEL: withholding.
- `fed.fit.nra.addon.table2.semimonthly` = **670.8** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-002, quoted from authority page, conf high] — Table 2: 2020+ W-4 or first paid 2020+. Added to wages for the FIT computation only (not on W-2, no FICA/FUTA effect); not applied to 22%/37% supplemental. Annual = single standard deduction 16,100. LEVEL: withholding.
- `fed.fit.nra.addon.table2.monthly` = **1341.7** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-002, quoted from authority page, conf high] — Table 2: 2020+ W-4 or first paid 2020+. Added to wages for the FIT computation only (not on W-2, no FICA/FUTA effect); not applied to 22%/37% supplemental. Annual = single standard deduction 16,100. LEVEL: withholding.
- `fed.fit.nra.addon.table2.quarterly` = **4025.0** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-002, quoted from authority page, conf high] — Table 2: 2020+ W-4 or first paid 2020+. Added to wages for the FIT computation only (not on W-2, no FICA/FUTA effect); not applied to 22%/37% supplemental. Annual = single standard deduction 16,100. LEVEL: withholding.
- `fed.fit.nra.addon.table2.semiannual` = **8050.0** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-002, quoted from authority page, conf high] — Table 2: 2020+ W-4 or first paid 2020+. Added to wages for the FIT computation only (not on W-2, no FICA/FUTA effect); not applied to 22%/37% supplemental. Annual = single standard deduction 16,100. LEVEL: withholding.
- `fed.fit.nra.addon.table2.annual` = **16100.0** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-002, quoted from authority page, conf high] — Table 2: 2020+ W-4 or first paid 2020+. Added to wages for the FIT computation only (not on W-2, no FICA/FUTA effect); not applied to 22%/37% supplemental. Annual = single standard deduction 16,100. LEVEL: withholding.
- `fed.fit.nra.addon.table2.daily` = **61.9** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-002, quoted from authority page, conf high] — Table 2: 2020+ W-4 or first paid 2020+. Added to wages for the FIT computation only (not on W-2, no FICA/FUTA effect); not applied to 22%/37% supplemental. Annual = single standard deduction 16,100. LEVEL: withholding.
- `fed.fit.nra.addon.table1.weekly` = **226.9** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-002, quoted from authority page, conf high] — Table 1: first paid before 2020 with no 2020+ W-4. Annual 11,800 = 16,100 - 4,300. LEVEL: withholding.
- `fed.fit.nra.addon.table1.biweekly` = **453.8** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-002, quoted from authority page, conf high] — Table 1: first paid before 2020 with no 2020+ W-4. Annual 11,800 = 16,100 - 4,300. LEVEL: withholding.
- `fed.fit.nra.addon.table1.semimonthly` = **491.7** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-002, quoted from authority page, conf high] — Table 1: first paid before 2020 with no 2020+ W-4. Annual 11,800 = 16,100 - 4,300. LEVEL: withholding.
- `fed.fit.nra.addon.table1.monthly` = **983.3** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-002, quoted from authority page, conf high] — Table 1: first paid before 2020 with no 2020+ W-4. Annual 11,800 = 16,100 - 4,300. LEVEL: withholding.
- `fed.fit.nra.addon.table1.quarterly` = **2950.0** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-002, quoted from authority page, conf high] — Table 1: first paid before 2020 with no 2020+ W-4. Annual 11,800 = 16,100 - 4,300. LEVEL: withholding.
- `fed.fit.nra.addon.table1.semiannual` = **5900.0** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-002, quoted from authority page, conf high] — Table 1: first paid before 2020 with no 2020+ W-4. Annual 11,800 = 16,100 - 4,300. LEVEL: withholding.
- `fed.fit.nra.addon.table1.annual` = **11800.0** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-002, quoted from authority page, conf high] — Table 1: first paid before 2020 with no 2020+ W-4. Annual 11,800 = 16,100 - 4,300. LEVEL: withholding.
- `fed.fit.nra.addon.table1.daily` = **45.4** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-002, quoted from authority page, conf high] — Table 1: first paid before 2020 with no 2020+ W-4. Annual 11,800 = 16,100 - 4,300. LEVEL: withholding.
- `fed.fit.nra.w4.rule` = **Check Single or MFS regardless of marital status; write NRA below Step 4(c); exempt not allowed; Step 3 only for residents of Canada, Mexico, South Korea or India (students/apprentices)**  (2020-01-01 → open) [A.3, US-FEDS5-015, quoted from authority page, conf high] — Notice 1392 (Rev. 1-2020) still the posted edition. LEVEL: withholding.
- `fed.fit.nra.treaty_exempt.reporting` = **Treaty-exempt wages claimed on Form 8233 are reported on Form 1042-S (not W-2 box 1); 2026 Forms 1042-S due 2027-03-15 and must be e-filed via IRIS**  (2026-01-01 → open) [A.2, US-FEDS5-016, quoted from authority page, conf high] — LEVEL: employer reporting.
- `fed.fit.nra.commercial_traveler.max_days` = **90** days (2026-01-01 → open) [A.2, US-FEDS5-016, quoted from authority page, conf high] — Exception from withholding: NRA present <= 90 days, total pay <= 3,000, foreign employer not engaged in US trade/business.
- `fed.fit.nra.commercial_traveler.max_pay` = **3000** USD (2026-01-01 → open) [A.2, US-FEDS5-016, quoted from authority page, conf high]

## 3 — Social security
The 2027 OASDI base 192,300 is an SSA-published value, verified 2026-11-02 on the browser-pass copy of SSA cbb.html [US-FEDB5-401]: "For earnings in 2027, this base is $192,300." FUTA 2026 credit reductions (CA potential 5.3%, USVI 4.8%) are NOT facts until the 2026-11-10 determination; only the final 2025 reductions are emitted.

- `fed.fica.oasdi.rate.employee` = **6.2** percent (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-005, quoted from authority page, conf high]
- `fed.fica.oasdi.rate.employer` = **6.2** percent (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-005, quoted from authority page, conf high]
- `fed.fica.oasdi.wage_base` = **184500** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-005, derived arithmetically, conf high] — G-DERIVE (US-FED-003, Federal Register 2025-19763): 60,600 x AWI(2024) 69,846.57 / AWI(1992) 22,935.42 = 184,548.71, rounded to a multiple of 300 = 184,500.
- `fed.fica.oasdi.wage_base` = **192300** USD (2027-01-01 → 2027-12-31) [A.2, US-FEDB5-401, quoted from authority page, conf high] — SSA published 2027 figure (cbb.html table 1937-2027). Re-verification on 2026-11-02 blocked (ssa.gov 403); not derived (AWI 2025 not held).
- `fed.fica.medicare.rate.employee` = **1.45** percent (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-005, quoted from authority page, conf high] — No wage base.
- `fed.fica.medicare.rate.employer` = **1.45** percent (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-005, quoted from authority page, conf high]
- `fed.fica.addl_medicare.rate` = **0.9** percent (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-005, quoted from authority page, conf high] — Employee only, no employer match.
- `fed.fica.addl_medicare.withholding_threshold` = **200000** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-005, quoted from authority page, conf high] — Wages paid in excess of 200,000 in the calendar year, regardless of filing status. LEVEL: withholding.
- `fed.futa.rate.gross` = **6.0** percent (2025-01-01 → open) [A.2, US-FED-007, quoted from authority page, conf high]
- `fed.futa.credit.max` = **5.4** percent (2025-01-01 → open) [A.2, US-FED-007, quoted from authority page, conf high]
- `fed.futa.rate.net` = **0.6** percent (2025-01-01 → open) [A.2, US-FED-007, quoted from authority page, conf high] — Plus any credit reduction for the state of the wages (Schedule A).
- `fed.futa.wage_base` = **7000** USD (2025-01-01 → open) [A.2, US-FED-007, quoted from authority page, conf high] — Per employee per employer per calendar year across all States (US-MULTIS5-009).
- `fed.futa.credit_reduction.ca` = **1.2** percent (2025-01-01 → 2025-12-31) [A.2, US-FEDS5-009, quoted from authority page, conf high] — FINAL for 2025 (Form 940 for 2025, Schedule A). [PARTIAL ROW: register status=partial; carry the partial flag]
- `fed.futa.credit_reduction.vi` = **4.5** percent (2025-01-01 → 2025-12-31) [A.2, US-FEDS5-009, quoted from authority page, conf high] — FINAL for 2025, U.S. Virgin Islands. [PARTIAL ROW: register status=partial; carry the partial flag]
- `fed.futa.deposit_threshold` = **500** USD (2026-01-01 → open) [A.2, US-FEDS5-031, quoted from authority page, conf high] — Deposit FUTA for a quarter when accumulated liability exceeds 500. [PARTIAL ROW: register status=partial; carry the partial flag]

## 4 — Payslip statute
No federal pay-statement statute; FLSA prescribes records only. Pay-statement content, delivery and language: State annexes.

- `fed.payslip.statute.exists` = **False**  (2026-11-02 → open) [A.1, US-FEDS5-021, quoted from authority page, conf high] — No federal pay-statement content/delivery rule; FLSA prescribes records only (29 CFR 516.2, US-FED-010). Pay statements = state law.
- `fed.records.flsa.retention_years` = **3** years (2026-11-02 → open) [A.1, US-FEDS5-021, quoted from authority page, conf high] — 29 CFR 516.5; supplementary records 2 years (516.6).
- `fed.records.irs.retention_years` = **4** years (2026-01-01 → open) [A.2, US-FEDS5-003, quoted from authority page, conf high]

## 5 — Statutory reporting instruments
EFW2 TY2026 is an ACCESS gap (US-FEDS5-032 gated). TY2026 i940 and i1094/1095-C not yet published: 2025 editions read (rows partial).

- `fed.deposit.lookback_period` = **2024-07-01 to 2025-06-30 (Form 941 filers); CY2024 for 943/944/945 filers**  (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-004, quoted from authority page, conf high]
- `fed.deposit.monthly_max_lookback_liability` = **50000** USD (2026-01-01 → open) [A.2, US-FEDS5-004, quoted from authority page, conf high] — <= 50,000 monthly depositor (by the 15th of the following month); > 50,000 semiweekly (Wed/Thu/Fri paydays -> following Wednesday; Sat-Tue -> following Friday).
- `fed.deposit.next_day_threshold` = **100000** USD (2026-01-01 → open) [A.2, US-FEDS5-004, quoted from authority page, conf high] — 100,000 or more accumulated on any day -> deposit next business day; deposit holidays = DC legal holidays.
- `fed.form941.frequency` = **quarterly; due last day of the month after the quarter; amounts in cents**  (2026-01-01 → open) [A.2, US-FEDS5-031, quoted from authority page, conf high] — [PARTIAL ROW: register status=partial; carry the partial flag]
- `fed.form944.max_liability` = **1000** USD (2026-01-01 → open) [A.2, US-FEDS5-031, quoted from authority page, conf high] — Annual Form 944 only on written IRS notice. [PARTIAL ROW: register status=partial; carry the partial flag]
- `fed.form940.due` = **January 31 (10 more days if all FUTA deposited on time)**  (2026-01-01 → open) [A.2, US-FEDS5-031, quoted from authority page, conf high] — [PARTIAL ROW: register status=partial; carry the partial flag]
- `fed.w2.due_date` = **2027-02-01**  (2026-01-01 → open) [A.2, US-FEDS5-007, quoted from authority page, conf high] — TY2026 Copy A to SSA and employee copies.
- `fed.w2.no_withholding_threshold` = **2000** USD (2026-01-01 → open) [A.2, US-FEDS5-007, quoted from authority page, conf high] — W-2 required at 2,000+ wages even with no withholding (was 600); indexed after 2026 (US-FEDS5-003).
- `fed.w2.box12.new_codes` = **TP (cash tips reported to employer); TT (qualified overtime compensation); TA (employer Trump-account contributions)**  (2026-01-01 → open) [A.2, US-FEDS5-007, quoted from authority page, conf high] — LEVEL: employer reporting.
- `fed.w2.box14b` = **Box 14 split into 14a Other and 14b Treasury Tipped Occupation Code(s)**  (2026-01-01 → open) [A.2, US-FEDS5-007, quoted from authority page, conf high] — LEVEL: employer reporting.
- `fed.aca.ale.fte_threshold` = **50** employees (2025-01-01 → open) [A.2, US-FEDS5-012, quoted from authority page, conf high] — TY2025 instructions (TY2026 edition not yet published). [PARTIAL ROW: register status=partial; carry the partial flag]
- `fed.aca.efile_threshold` = **10** returns (2025-01-01 → open) [A.2, US-FEDS5-012, quoted from authority page, conf high] — [PARTIAL ROW: register status=partial; carry the partial flag]
- `fed.aca.affordability.rate` = **9.96** percent (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-011, quoted from authority page, conf high] — Required contribution percentage, plan years beginning in 2026.
- `fed.newhire.deadline_days` = **20** days (1997-10-01 → open) [A.1, US-FEDS5-024, quoted from authority page, conf high] — Or, electronic filers, two monthly transmissions 12-16 days apart; state deadlines shorter per state annex.
- `fed.newhire.fields` = **employee name, address, SSN, date services first performed; employer name, address, FEIN**  (1997-10-01 → open) [A.1, US-FEDS5-024, quoted from authority page, conf high]
- `fed.reporting_agent.authorization` = **Form 8655 (Rev. Jan 2024); agent may sign/file 940/941 and deposit; taxpayer stays liable**  (2012-11-19 → open) [A.2, US-FED-008, quoted from authority page, conf high]

## 6 — Leave
No federal paid sick or annual leave for private employers; State PFML/PSL in State annexes.

- `fed.fmla.weeks` = **12** weeks (1993-08-05 → open) [A.1, US-FEDS5-026, quoted from authority page, conf high] — In a 12-month period; may be unpaid; employer may require substitution of accrued paid leave.
- `fed.fmla.military_caregiver.weeks` = **26** weeks (1993-08-05 → open) [A.1, US-FEDS5-026, quoted from authority page, conf high]
- `fed.paid_leave.private_employers.exists` = **False**  (1993-08-05 → open) [A.1, US-FEDS5-026, quoted from authority page, conf high] — No federal paid sick or annual leave for private employers; contractors under EO 13706 (accrual not transcribed).
- `fed.pfml.employee_contribution.is_w2_wages` = **True**  (2026-01-01 → open) [A.2, US-FEDS5-007, quoted from authority page, conf high] — State PFML employee contribution and employer voluntary payment are W-2 wages (Rev. Rul. 2025-4, Notice 2026-6).

## 7 — Termination
Final-pay timing and vacation payout are State law; WARN pay-in-lieu is the only federal payroll touchpoint.

- `fed.final_pay.rule` = **No federal immediate final-pay rule; wages due by the regular payday; timing and vacation payout are state law**  (1989-02-04 → open) [A.1, US-FEDS5-025, quoted from authority page, conf high]
- `fed.warn.notice_days` = **60** days (1989-02-04 → open) [A.1, US-FEDS5-025, quoted from authority page, conf high] — Pay in lieu = back-pay liability (29 USC 2104).
- `fed.severance.is_wages` = **True**  (2026-01-01 → open) [A.2, US-FEDS5-029, quoted from authority page, conf high] — Severance is wages for FIT, FICA and FUTA.

## 8 — Benefits in kind
Federal exclusions are the baseline the States conform to or depart from (State conformity per State annex). The 2026 business mileage rate is open.

- `fed.bik.parking.monthly_exclusion` = **340** USD (2026-01-01 → open) [A.2, US-FEDS5-008, quoted from authority page, conf high]
- `fed.bik.transit.monthly_exclusion` = **340** USD (2026-01-01 → open) [A.2, US-FEDS5-008, quoted from authority page, conf high]
- `fed.bik.health_fsa.salary_reduction_cap` = **3400** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-010, quoted from authority page, conf high]
- `fed.bik.health_fsa.carryover_max` = **680** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-010, quoted from authority page, conf high]
- `fed.bik.dependent_care.exclusion` = **7500** USD (2026-01-01 → open) [A.2, US-FEDS5-008, quoted from authority page, conf high] — 3,750 MFS; raised from 5,000 by P.L. 119-21.
- `fed.bik.educational_assistance.exclusion` = **5250** USD (2026-01-01 → open) [A.2, US-FEDS5-008, quoted from authority page, conf high] — Exclusion made permanent.
- `fed.bik.group_term_life.excluded_coverage` = **50000** USD (2026-01-01 → open) [A.2, US-FEDS5-008, quoted from authority page, conf high] — Imputed cost of coverage above 50,000 is FICA wages; FIT withholding not required.
- `fed.bik.group_term_life.monthly_cost_per_1000.under_25` = **0.05** USD (2026-01-01 → open) [A.2, US-FEDS5-008, quoted from authority page, conf high] — Pub. 15-B Table 2-2.
- `fed.bik.group_term_life.monthly_cost_per_1000.25_29` = **0.06** USD (2026-01-01 → open) [A.2, US-FEDS5-008, quoted from authority page, conf high] — Pub. 15-B Table 2-2.
- `fed.bik.group_term_life.monthly_cost_per_1000.30_34` = **0.08** USD (2026-01-01 → open) [A.2, US-FEDS5-008, quoted from authority page, conf high] — Pub. 15-B Table 2-2.
- `fed.bik.group_term_life.monthly_cost_per_1000.35_39` = **0.09** USD (2026-01-01 → open) [A.2, US-FEDS5-008, quoted from authority page, conf high] — Pub. 15-B Table 2-2.
- `fed.bik.group_term_life.monthly_cost_per_1000.40_44` = **0.1** USD (2026-01-01 → open) [A.2, US-FEDS5-008, quoted from authority page, conf high] — Pub. 15-B Table 2-2.
- `fed.bik.group_term_life.monthly_cost_per_1000.45_49` = **0.15** USD (2026-01-01 → open) [A.2, US-FEDS5-008, quoted from authority page, conf high] — Pub. 15-B Table 2-2.
- `fed.bik.group_term_life.monthly_cost_per_1000.50_54` = **0.23** USD (2026-01-01 → open) [A.2, US-FEDS5-008, quoted from authority page, conf high] — Pub. 15-B Table 2-2.
- `fed.bik.group_term_life.monthly_cost_per_1000.55_59` = **0.43** USD (2026-01-01 → open) [A.2, US-FEDS5-008, quoted from authority page, conf high] — Pub. 15-B Table 2-2.
- `fed.bik.group_term_life.monthly_cost_per_1000.60_64` = **0.66** USD (2026-01-01 → open) [A.2, US-FEDS5-008, quoted from authority page, conf high] — Pub. 15-B Table 2-2.
- `fed.bik.group_term_life.monthly_cost_per_1000.65_69` = **1.27** USD (2026-01-01 → open) [A.2, US-FEDS5-008, quoted from authority page, conf high] — Pub. 15-B Table 2-2.
- `fed.bik.group_term_life.monthly_cost_per_1000.70_plus` = **2.06** USD (2026-01-01 → open) [A.2, US-FEDS5-008, quoted from authority page, conf high] — Pub. 15-B Table 2-2.
- `fed.bik.trump_account.employer_contribution_max` = **2500** USD (2026-07-04 → open) [A.2, US-FEDS5-030, quoted from authority page, conf high] — Sec. 128 program; W-2 code TA; indexed after 2027.
- `fed.bik.moving_and_bicycle.excluded` = **False**  (2026-01-01 → open) [A.2, US-FEDS5-008, quoted from authority page, conf high] — Moving-expense and bicycle-commuting exclusions eliminated (moving: except Armed Forces / intelligence community).
- `fed.retirement.401k.elective_deferral_limit` = **24500** USD (2026-01-01 → 2026-12-31) [A.2, US-FED-023, quoted from authority page, conf high]
- `fed.retirement.401k.catch_up_50` = **8000** USD (2026-01-01 → 2026-12-31) [A.2, US-FED-023, quoted from authority page, conf high]
- `fed.retirement.401k.catch_up_60_63` = **11250** USD (2026-01-01 → 2026-12-31) [A.2, US-FED-023, quoted from authority page, conf high]
- `fed.retirement.simple.deferral_limit` = **17000** USD (2026-01-01 → 2026-12-31) [A.2, US-FED-023, quoted from authority page, conf high] — 18,100 for SIMPLE plans with the higher limit.
- `fed.hsa.limit.self_only` = **4400** USD (2026-01-01 → 2026-12-31) [A.2, US-FED-024, quoted from authority page, conf high]
- `fed.hsa.limit.family` = **8750** USD (2026-01-01 → 2026-12-31) [A.2, US-FED-024, quoted from authority page, conf high]
- `fed.feie.amount` = **132900** USD (2026-01-01 → 2026-12-31) [A.2, US-FED-025, quoted from authority page, conf high] — Rev. Proc. 2025-32 sec. 911 item, also stated in US-FEDP52-002 (same document, item .38). Foreign earned income exclusion; employer may stop FIT withholding on the employee statement (US-FEDR3-007).

## 9 — Deductions and garnishments
CCPA floor; State limits may be stricter (State annexes). IRS levy is not subject to the CCPA cap (Pub. 1494 exempt amounts). Interstate IWO governing law: annex_MULTI.

- `fed.ccpa.max_rate` = **25** percent (1970-07-01 → open) [A.1, US-FEDS5-023, quoted from authority page, conf high] — Lesser of 25% of weekly disposable earnings or the amount above 30 x 7.25.
- `fed.ccpa.protected_weekly` = **217.5** USD (1970-07-01 → open) [A.1, US-FEDS5-023, quoted from authority page, conf high] — 30 x 7.25.
- `fed.ccpa.support.max_rate.with_dependents` = **50** percent (1970-07-01 → open) [A.1, US-FEDS5-023, quoted from authority page, conf high] — 55% with arrears older than 12 weeks.
- `fed.ccpa.support.max_rate.without_dependents` = **60** percent (1970-07-01 → open) [A.1, US-FEDS5-023, quoted from authority page, conf high] — 65% with arrears older than 12 weeks.
- `fed.ccpa.support.arrears_addon` = **5** percent (1970-07-01 → open) [A.1, US-FEDS5-023, quoted from authority page, conf high] — +5 points (55/65) where arrears older than 12 weeks.
- `fed.levy.exempt.single_0dep.daily` = **61.92** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-014, quoted from authority page, conf high] — Pub. 1494 (2026); MFS = Single. Weekly = 16,100/52; monthly = 16,100/12.
- `fed.levy.exempt.single_0dep.weekly` = **309.62** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-014, quoted from authority page, conf high] — Pub. 1494 (2026); MFS = Single. Weekly = 16,100/52; monthly = 16,100/12.
- `fed.levy.exempt.single_0dep.biweekly` = **619.23** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-014, quoted from authority page, conf high] — Pub. 1494 (2026); MFS = Single. Weekly = 16,100/52; monthly = 16,100/12.
- `fed.levy.exempt.single_0dep.semimonthly` = **670.83** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-014, quoted from authority page, conf high] — Pub. 1494 (2026); MFS = Single. Weekly = 16,100/52; monthly = 16,100/12.
- `fed.levy.exempt.single_0dep.monthly` = **1341.67** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-014, quoted from authority page, conf high] — Pub. 1494 (2026); MFS = Single. Weekly = 16,100/52; monthly = 16,100/12.
- `fed.levy.exempt.per_dependent.daily` = **20.38** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-014, quoted from authority page, conf high] — 5,300/52 weekly; 5,300/12 monthly.
- `fed.levy.exempt.per_dependent.weekly` = **101.92** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-014, quoted from authority page, conf high] — 5,300/52 weekly; 5,300/12 monthly.
- `fed.levy.exempt.per_dependent.biweekly` = **203.85** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-014, quoted from authority page, conf high] — 5,300/52 weekly; 5,300/12 monthly.
- `fed.levy.exempt.per_dependent.semimonthly` = **220.83** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-014, quoted from authority page, conf high] — 5,300/52 weekly; 5,300/12 monthly.
- `fed.levy.exempt.per_dependent.monthly` = **441.67** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-014, quoted from authority page, conf high] — 5,300/52 weekly; 5,300/12 monthly.
- `fed.levy.exempt.mfj_0dep.weekly` = **619.23** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-014, quoted from authority page, conf high]
- `fed.levy.exempt.mfj_0dep.monthly` = **2683.33** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-014, quoted from authority page, conf high]
- `fed.levy.exempt.hoh_0dep.weekly` = **464.42** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-014, quoted from authority page, conf high]
- `fed.iwo.priority` = **IWO for support ranks before other garnishments, except an IRS levy served before the underlying support order**  (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-014, quoted from authority page, conf high] — Stated in US-FEDS5-014 (Pub. 1494 row) citing the OCSS employer page US-FEDP51-006.
- `fed.iwo.omb_expiry` = **2029-08-31**  (2026-08-25 → 2029-08-31) [A.2, US-FEDS5-028, quoted from authority page, conf high] — OMB 0970-0154 approved without change 2026-08-25; current form extended one year while states reprogram the revised (gig-worker fields) IWO/e-IWO. Supersedes US-FEDP6-001. LEVEL: employer withholding.

## 10 — Collective agreements
- `fed.cba.scope` = **A CBA binds the certified bargaining unit only; no sector-wide extension mechanism**  (2026-01-01 → open) [A.1, US-FED-018, quoted from authority page, conf high]
- `fed.davis_bacon.contract_threshold` = **2000** USD (2026-01-01 → open) [A.1, US-FED-019, quoted from authority page, conf high] — Federal construction contracts over 2,000.
- `fed.davis_bacon.certified_payroll.frequency` = **weekly, to the contracting agency; prime responsible for subcontractors; optional form WH-347; records 3 years**  (2023-10-23 → open) [A.1, US-FEDS5-027, quoted from authority page, conf high]

## 11 — Indexation
FLSA minimum wage, CCPA multiplier and the 684 salary floor are not indexed; the 2,000 information-return threshold is indexed after 2026. 2027 Rev. Proc. not yet published (no projections used).

- `fed.indexation.caliber` = **C-CPI-U (chained CPI-U) under 26 U.S.C. 1(f)(3)**  (2026-01-01 → open) [A.3, US-FEDQ1-012 (supersedes US-FED-026, LII copy), quoted from authority page, conf high] — Rev. Proc. 2025-32 applies it for 2026 (US-FEDS5-010). OASDI base indexed on AWI (US-FED-003). FLSA minimum wage, CCPA multiplier and the 684 salary floor are NOT indexed.
- `fed.indexation.oasdi_caliber` = **National Average Wage Index (AWI), base rounded to a multiple of 300**  (2026-01-01 → open) [A.1, US-FED-003, quoted from authority page, conf high]

## 12 — Payroll data protection
- `fed.ssn.truncation.format` = **TTIN: first five digits of the SSN masked (asterisks or X characters), last four digits shown, e.g. ***-**-1234; allowed on employee W-2 copies only; never on Copy A; EIN never truncated** (2019-07-03 -> open) [A.1, US-FEDS5-022, quoted from authority page, conf high]

## 13 — Live legal change
P.L. 119-21 (enacted 2025-07-04, in force). Level carried in each fact: tips/overtime deductions operate at ASSESSMENT (withholding only via W-4 Step 4(b)); employer duty is REPORTING (W-2 TP/TT/14b). Do not build a payroll deduction for them. Proposed IRS regulations of October 2026 (IR-2026-117, -121) do not touch employer payroll.

- `fed.plaw119_21.qualified_tips.deduction_cap` = **25000** USD (2025-01-01 → 2028-12-31) [A.2, US-FEDS5-030, quoted from authority page, conf high] — IN FORCE (enacted 2025-07-04). Reaches withholding only via W-4 Step 4(b); employer reporting via W-2 TP/14b; tips stay fully FICA-subject. Do NOT model as a payroll deduction. LEVEL: assessment.
- `fed.plaw119_21.qualified_overtime.deduction_cap` = **12500** USD (2025-01-01 → 2028-12-31) [A.2, US-FEDS5-030, quoted from authority page, conf high] — 25,000 MFJ. Employer reporting via W-2 TT; overtime stays fully FICA-subject. LEVEL: assessment.
- `fed.plaw119_21.qualified_overtime.deduction_cap_mfj` = **25000** USD (2025-01-01 → 2028-12-31) [A.2, US-FEDS5-030, quoted from authority page, conf high] — LEVEL: assessment.
- `fed.plaw119_21.reporting_penalty_relief` = **TY2025 only (Notice 2025-62); separate reporting of tips/TTOC/overtime mandatory from TY2026**  (2025-01-01 → 2025-12-31) [A.2, US-FEDS5-013, quoted from authority page, conf high] — LEVEL: employer reporting.

## Special populations (US-OWN-005)
US-OWN-005: all populations IN; federal rules in full here, State-level rules in the State annexes.

- `fed.household.fica_cash_threshold` = **3000** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-029, quoted from authority page, conf high] — FICA if cash wages 3,000+ in 2026 (exempt under 18 unless principal occupation); FIT only by agreement; Schedule H.
- `fed.household.futa_quarter_threshold` = **1000** USD (2026-01-01 → open) [A.2, US-FEDS5-029, quoted from authority page, conf high] — FUTA if 1,000+ cash wages in any quarter of current or prior year.
- `fed.agricultural.per_worker_threshold` = **150** USD (2026-01-01 → open) [A.2, US-FEDR3-006, quoted from authority page, conf high] — Cash wages 150+ to a farmworker in a year, or 2,500+ total farm pay, make cash wages subject to FICA and FIT; Form 943.
- `fed.agricultural.total_threshold` = **2500** USD (2026-01-01 → open) [A.2, US-FEDR3-006, quoted from authority page, conf high]
- `fed.agricultural.futa_quarter_threshold` = **20000** USD (2026-01-01 → open) [A.2, US-FEDR3-006, quoted from authority page, conf high] — Or 10+ farmworkers on some part of a day in 20+ weeks.
- `fed.election_worker.fica_threshold` = **2500** USD (2026-01-01 → 2026-12-31) [A.2, US-FEDS5-003, quoted from authority page, conf high]
- `fed.tips.reporting_threshold_monthly` = **20** USD (2026-01-01 → open) [A.2, US-FEDS5-003, quoted from authority page, conf high] — Tips of 20+ in a month are subject to FIT/FICA.
- `fed.minister.withholding` = **No FIT, social security or Medicare withholding (SE tax; voluntary FIT withholding agreement allowed); parsonage allowance excluded from W-2 box 1**  (2026-01-01 → open) [A.2, US-FED-030, quoted from authority page, conf high]
- `fed.statutory_employee.treatment` = **FICA withheld, no FIT withholding; W-2 box 13 checked; FUTA for drivers and traveling salespersons only**  (2026-01-01 → open) [A.2, US-FEDR3-005, quoted from authority page, conf high]
- `fed.family_employment.treatment` = **Child under 18 of a sole proprietor/parents-only partnership: FICA exempt, FUTA exempt under 21; spouse: FUTA exempt; parent employed by child: FUTA exempt**  (2026-01-01 → open) [A.2, US-FEDS5-029, quoted from authority page, conf high]
- `fed.students.treatment` = **Private school/college students: FIT withheld, FICA and FUTA exempt; public school: FICA exempt unless sec. 218 agreement; work-experience full-time student: FICA taxable**  (2026-01-01 → open) [A.2, US-FEDS5-029, quoted from authority page, conf high]
- `fed.government_employee.treatment` = **FIT withheld; no FUTA; FICA with sec. 218 / Medicare-only exceptions**  (2026-01-01 → open) [A.2, US-FEDS5-029, quoted from authority page, conf high]

## Oracle (worked examples)
Federal oracle per build-manifest.oracle: Pub. 15-T 2026 publishes only two worked examples (NRA weekly 526.90 -> 31; tribal monthly 6,000 -> 584.09); no full percentage-method example, so Stage 9b re-derives from Worksheet 1A + the Annual Percentage Method tables. The IRS Tax Withholding Estimator is not an oracle [US-FED-021]. State worked examples (CA DE 44, GA, MN, MI, OH, NY, IL, WI, VT, CT, ...) belong to the State annexes and to CCG m12_worked_examples.

- `fed.oracle.pub15t.nra_example.wages` = **526.9** USD (2026-01-01 → open) [A.2, US-FED-027, quoted from authority page, conf high] — Weekly wages 300 + Table 1 add-on 226.90 = 526.90 (Pub. 15-T 2026 example).
- `fed.oracle.pub15t.nra_example.withholding` = **31** USD (2026-01-01 → open) [A.2, US-FED-027, quoted from authority page, conf high] — Wage-bracket result for 526.90 weekly; residual none recorded. Stage 9b re-derives the percentage method from Worksheet 1A (no full percentage-method example is published).
- `fed.oracle.pub15t.tribal_example.payment` = **6000** USD (2026-01-01 → open) [A.2, US-FED-027, quoted from authority page, conf high] — Tribal monthly gaming payment example.
- `fed.oracle.pub15t.tribal_example.withholding` = **584.09** USD (2026-01-01 → open) [A.2, US-FED-027, quoted from authority page, conf high]

## Special populations table (federal)
| Population | Federal rule | register_id |
|---|---|---|
| Domestic/household | FIT only by agreement; FICA at 3,000+ cash (2026); FUTA at 1,000+ in a quarter; Schedule H | US-FEDS5-029 |
| Agricultural | FICA/FIT at 150 per worker or 2,500 total; Form 943; FUTA 20,000/quarter or 10 workers in 20 weeks | US-FEDR3-006 |
| Minors / family | Child under 18 of a sole proprietor: FICA exempt, FUTA exempt under 21; spouse FUTA exempt | US-FEDS5-029 |
| Tipped | Cash wage 2.13, tip credit 5.12; tips 20+/month subject to FIT/FICA; W-2 TP and 14b | US-FEDS5-019, US-FEDS5-003, US-FEDS5-007 |
| Clergy | No FIT/FICA withholding (SE tax; voluntary FIT) | US-FED-030 |
| Students | Private school: FICA/FUTA exempt; public: FICA exempt unless sec. 218 | US-FEDS5-029 |
| Nonresident aliens | 15-T add-on, Notice 1392 W-4, 8233/1042-S, commercial-traveler exception | US-FEDS5-002, -015, -016 |
| Statutory employees | FICA yes, FIT no | US-FEDR3-005 |
| Government employees | FIT yes, FUTA no, FICA with sec. 218 exceptions | US-FEDS5-029 |
| Election workers | FICA at 2,500+ (2026) | US-FEDS5-003 |
| Employees abroad (US citizens) | FIT withholding may stop on the FEIE statement; FEIE 132,900 | US-FEDR3-007, US-FED-025 |

## Synthesis D additions (2026-11-02)

Source: browser-pass rows S5B-P1 / S5B-P2 merged into `legal-basis-register.csv` and SSA EFW2 TY2026 (US-FEDS5-032) read locally. Every claim below carries its register_id; the facts file is authoritative. Full log: `_research/synthesis-D/SYNTHESIS-D.md`.

Facts added:
- `fed.newhire.electronic_interval` = **Electronic/magnetic filers: two monthly transmissions, not less than 12 nor more than 16 days apart** (1997-10-01 → open) [A.2, US-FEDB5-001, quoted from authority page, conf high] — OCSS employer page restating 42 USC 653a(b)(2).
- `fed.newhire.state_penalty.max_per_hire` = **25** USD (1997-10-01 → open) [A.2, US-FEDB5-001, quoted from authority page, conf high] — State civil penalty cap per newly hired employee; 500 USD if failure results from a conspiracy (42 USC 653a(d)).
- `fed.newhire.state_penalty.conspiracy.max_per_hire` = **500** USD (1997-10-01 → open) [A.2, US-FEDB5-001, quoted from authority page, conf high]
- `fed.newhire.form` = **W-4 copy or an equivalent form; seven federal data elements (employee name, address, SSN, date of hire = first day of services for pay; employer name, address, FEIN)** (1997-10-01 → open) [A.2, US-FEDB5-001, quoted from authority page, conf high]
- `fed.efw2.edition` = **SSA Publication No. 42-007, EFW2 Tax Year 2026 (page header dated 2026-09-14; no version change entries yet)** (2026-01-01 → open) [A.2, US-FEDS5-032, direct artifact inspection, conf high]
- `fed.efw2.record_length` = **512** bytes (2026-01-01 → open) [A.2, US-FEDS5-032, direct artifact inspection, conf high]
- `fed.efw2.records` = **512-byte records in order RA, RE, RW, (RO), (RS), RT, (RU), (RV), RF; RA/RE/RW/RT/RF required; RO/RS/RU/RV optional; RS and RV are not read or processed by SSA or IRS (state-defined)** (2026-01-01 -> open) [A.2, US-FEDS5-032, direct artifact inspection, conf high]
- `fed.efw2.ty2026_changes` = **TY2026 changes: RE adds Employer Signature PIN (319-328); RW adds Box 14b Primary/Secondary Treasury Tipped Occupation Code (490-492 / 493-495); RO/RU split Codes A and B into separate money fields (combined A+B field valid through TY2025 only), add money fields for existing Codes J, K, L, P and new Codes TA, TP, TT; SS wage base 184,500; FIRE replaced by IRIS** (2026-01-01 → open) [A.2, US-FEDS5-032, direct artifact inspection, conf high] — LEVEL: employer reporting.

Open questions closed: `fed.efw2.layout`.

## QA round 1 additions (2026-11-02)

Answers to RQ-505, RQ-534, RQ-565 (equity), RQ-566 (NRA fringe benefits), RQ-553 (extra pay period) and RQ-554 (2026/2027 holidays), all from IRS, OPM, GPO and eCFR text held locally under `00-official-sources/ccg-sources/FED/`. Facts file is authoritative.

**2 - Income tax / 2b - Non-resident regime: equity compensation.** Pub. 15-B (2026) "Employee Stock Options" [A.2, US-FEDQ1-001]; Pub. 15 (2026) sec. 5 and sec. 7 [A.2, US-FEDQ1-002]; Pub. 525 (TY2025) [A.3, US-FEDQ1-003, mechanics only]; 26 CFR 31.3121(v)(2)-1 [A.1, US-FEDQ1-004] and 31.3306(r)(2)-1 [A.1, US-FEDQ1-005]; Pub. 515 (2026) [A.2, US-FEDQ1-006]; Pub. 15-T (2026) Introduction [A.2, US-FEDQ1-007]. LEVEL: withholding (FIT), withholding (FICA/FUTA), employer reporting (W-2 codes V, GG, HH).

**8 - Benefits in kind: NRA employees.** Pub. 15-B sec. 4 and Group-Term Life [A.2, US-FEDQ1-008] with Pub. 15-T and Pub. 515 rows above. LEVEL: withholding.

Facts added (annex FED and m06_tax carry the same keys and values):
- `fed.equity.withholding_treatment.resident` = **Resident employee, 2026: (1) Nonstatutory option (NSO): the spread at exercise (FMV - price) is wages - a taxable fringe benefit subject to the supplemental-wage rules (22% optional flat or aggregate; 37% on supplemental wages above 1,000,000), FICA and FUTA wages, timed at the actual exercise (transfer) date; W-2 boxes 1, 3 (to the SS base), 5 and box 12 code V. (2) ISO and ESPP options: no FICA or FUTA at grant, exercise or disposition; no FIT withholding required on a disqualifying disposition or on the ESPP discount at a qualifying disposition, but the ordinary income is W-2 box 1 wages. (3) Restricted stock (actual shares subject to forfeiture): FMV minus amount paid is wages when substantially vested (or at transfer with an 83(b) election). (4) RSU (legally binding right to receive shares in a future year): FICA and FUTA wages at the later of service performance and vesting (special timing rule, 26 CFR 31.3121(v)(2)-1 / 31.3306(r)(2)-1); FIT withholding when the shares are delivered (settlement) as supplemental wages. (5) 83(i) election (private company): FIT deferred up to 5 years and withheld at 37% when included; FICA/FUTA not deferred; W-2 codes GG/HH.** (2026-01-01 -> open) [A.2, US-FEDQ1-001, second independent authority, conf medium] - Rows: Pub. 15-B options and 83(i) (US-FEDQ1-001), Pub. 15 sec. 7 (US-FEDQ1-002), Pub. 525 (US-FEDQ1-003), 26 CFR 31.3121(v)(2)-1 (US-FEDQ1-004), 31.3306(r)(2)-1 (US-FEDQ1-005). Confidence medium only for the RSU limb: no IRS publication names RSUs in the FIT timing rule; it follows from settlement in shares (Pub. 15-B 83(i) paragraph) and the NQDC definition in 31.3121(v)(2)-1(b)(4)(iii). LEVEL: withholding.
- `fed.equity.withholding_treatment.nonresident` = **Nonresident alien employee, 2026: equity income is wages subject to graduated withholding as for residents, with the Pub. 15-T NRA add-on, except that no add-on applies when the payment is withheld at the 22% optional or 37% mandatory flat supplemental rate. Only the U.S.-source part is wages for U.S. withholding: compensation attributable to several years is sourced on a time basis (U.S. workdays / total workdays over the period to which it is attributable, facts and circumstances). FICA/FUTA follow the resident rules (NSO spread and RSU at vesting are FICA wages) unless the employee is exempt as an F-1/J-1/M-1/Q nonimmigrant. Reporting on Form W-2; Form 1042-S only for wages exempt under a treaty claimed on Form 8233.** (2026-01-01 -> open) [A.2, US-FEDQ1-006, second independent authority, conf medium] - Rows: Pub. 515 (US-FEDQ1-006), Pub. 15-T NRA/supplemental (US-FEDQ1-007), Pub. 15-B (US-FEDQ1-001). The grant-to-vest sourcing period for options/RSUs (Treas. Reg. 1.861-4(b)(2)(ii)(F)) was not read: see unresolved fed.equity.nra.sourcing_period. LEVEL: withholding.
- `fed.equity.nso.w2_code` = **V** (2026-01-01 -> open) [A.2, US-FEDQ1-001, second independent authority, conf high] - Also Pub. 525 (US-FEDQ1-003). LEVEL: employer reporting.
- `fed.equity.iso_espp.fica_futa_applies` = **False** (2026-01-01 -> open) [A.2, US-FEDQ1-001, quoted from authority page, conf high] - LEVEL: withholding.
- `fed.equity.iso_espp.fit_withholding_required` = **False** (2026-01-01 -> open) [A.2, US-FEDQ1-001, quoted from authority page, conf high] - Ordinary income at a disqualifying disposition (or ESPP discount at a qualifying disposition) is still W-2 box 1 wages. LEVEL: withholding.
- `fed.equity.83i.withholding_rate` = **37** percent (2026-01-01 -> open) [A.2, US-FEDQ1-001, quoted from authority page, conf high] - W-2 box 12 codes GG (amount included) and HH (aggregate deferrals). LEVEL: withholding.
- `fed.equity.rsu.fica_timing` = **Later of the performance of the services and the date the right is no longer subject to a substantial risk of forfeiture (vesting); FUTA follows the same rule** (2026-01-01 -> open) [A.1, US-FEDQ1-004, quoted from authority page, conf high] - 26 CFR 31.3121(v)(2)-1(a)(2)(ii), (b)(4)(iii); 31.3306(r)(2)-1(a) (US-FEDQ1-005). LEVEL: withholding.
- `fed.fit.nra.bik.treatment` = **Nonresident alien employee, 2026: taxable fringe benefits are wages subject to graduated FIT withholding. Added to regular wages for the payroll period, they are withheld with the Pub. 15-T NRA add-on; withheld separately at the 22% optional flat supplemental rate (37% above 1,000,000), no add-on applies. Noncash fringes may be treated as paid per pay period, quarter, half-year or year (at least annually). FICA and FUTA apply as for residents unless the employee is an F-1/J-1/M-1/Q nonimmigrant. Group-term life cost over 50,000: FICA wages, no FIT withholding and no FUTA required, W-2 boxes 1, 3, 5 and box 12 code C. Only U.S.-source fringes are wages for withholding: housing, education, local transportation (main job location), tax reimbursement (taxing jurisdiction), hazardous duty and moving (new main job location) are sourced geographically, other fringes on a time basis. Reported on Form W-2 (Form 1042-S only for treaty-exempt wages on Form 8233).** (2026-01-01 -> open) [A.2, US-FEDQ1-008, second independent authority, conf high] - Rows: Pub. 15-B sec. 4 and GTL (US-FEDQ1-008), Pub. 15-T NRA/supplemental (US-FEDQ1-007), Pub. 515 (US-FEDQ1-006), Pub. 15 sec. 7 (US-FEDQ1-002). LEVEL: withholding.
- `fed.fit.nra.addon.flat_rate_supplemental.applies` = **False** (2026-01-01 -> open) [A.2, US-FEDQ1-007, quoted from authority page, conf high] - Pub. 15-T Introduction: the NRA procedure does not apply when the 22% optional or 37% mandatory flat rate is used. LEVEL: withholding.

**1 - Labour code / reporting calendar (m01 1.3 and 1.4).** 5 U.S.C. 6103 [A.1, US-FEDQ1-009]; OPM 2026/2027 schedules [A.2, US-FEDQ1-010]; Pub. 15 (2026) Calendar and sec. 11 legal-holiday list [A.2, US-FEDQ1-011]. Facts in `CCG-m01_foundational-facts.json`:
- `fed.holiday.new_years_day.observed_date` = **2026-01-01** (2026-01-01 -> 2026-12-31) [A.2, US-FEDQ1-011, second independent authority, conf high] - Pub. 15 2026 legal-holiday list = OPM 2026 schedule (US-FEDQ1-010); date re-derived from the 5 U.S.C. 6103 rule (US-FEDQ1-009). LEVEL: employer reporting.
- `fed.holiday.mlk_birthday.observed_date` = **2026-01-19** (2026-01-01 -> 2026-12-31) [A.2, US-FEDQ1-011, second independent authority, conf high] - Pub. 15 2026 legal-holiday list = OPM 2026 schedule (US-FEDQ1-010); date re-derived from the 5 U.S.C. 6103 rule (US-FEDQ1-009). LEVEL: employer reporting.
- `fed.holiday.washingtons_birthday.observed_date` = **2026-02-16** (2026-01-01 -> 2026-12-31) [A.2, US-FEDQ1-011, second independent authority, conf high] - Pub. 15 2026 legal-holiday list = OPM 2026 schedule (US-FEDQ1-010); date re-derived from the 5 U.S.C. 6103 rule (US-FEDQ1-009). LEVEL: employer reporting.
- `fed.holiday.memorial_day.observed_date` = **2026-05-25** (2026-01-01 -> 2026-12-31) [A.2, US-FEDQ1-011, second independent authority, conf high] - Pub. 15 2026 legal-holiday list = OPM 2026 schedule (US-FEDQ1-010); date re-derived from the 5 U.S.C. 6103 rule (US-FEDQ1-009). LEVEL: employer reporting.
- `fed.holiday.juneteenth.observed_date` = **2026-06-19** (2026-01-01 -> 2026-12-31) [A.2, US-FEDQ1-011, second independent authority, conf high] - Pub. 15 2026 legal-holiday list = OPM 2026 schedule (US-FEDQ1-010); date re-derived from the 5 U.S.C. 6103 rule (US-FEDQ1-009). LEVEL: employer reporting.
- `fed.holiday.independence_day.observed_date` = **2026-07-03** (2026-01-01 -> 2026-12-31) [A.2, US-FEDQ1-011, second independent authority, conf high] - July 4, 2026 is a Saturday; observed Friday July 3 (5 U.S.C. 6103(b)(1)); also the IRS legal holiday. Pub. 15 2026 legal-holiday list = OPM 2026 schedule (US-FEDQ1-010); date re-derived from the 5 U.S.C. 6103 rule (US-FEDQ1-009). LEVEL: employer reporting.
- `fed.holiday.labor_day.observed_date` = **2026-09-07** (2026-01-01 -> 2026-12-31) [A.2, US-FEDQ1-011, second independent authority, conf high] - Pub. 15 2026 legal-holiday list = OPM 2026 schedule (US-FEDQ1-010); date re-derived from the 5 U.S.C. 6103 rule (US-FEDQ1-009). LEVEL: employer reporting.
- `fed.holiday.columbus_day.observed_date` = **2026-10-12** (2026-01-01 -> 2026-12-31) [A.2, US-FEDQ1-011, second independent authority, conf high] - Pub. 15 2026 legal-holiday list = OPM 2026 schedule (US-FEDQ1-010); date re-derived from the 5 U.S.C. 6103 rule (US-FEDQ1-009). LEVEL: employer reporting.
- `fed.holiday.veterans_day.observed_date` = **2026-11-11** (2026-01-01 -> 2026-12-31) [A.2, US-FEDQ1-011, second independent authority, conf high] - Pub. 15 2026 legal-holiday list = OPM 2026 schedule (US-FEDQ1-010); date re-derived from the 5 U.S.C. 6103 rule (US-FEDQ1-009). LEVEL: employer reporting.
- `fed.holiday.thanksgiving_day.observed_date` = **2026-11-26** (2026-01-01 -> 2026-12-31) [A.2, US-FEDQ1-011, second independent authority, conf high] - Pub. 15 2026 legal-holiday list = OPM 2026 schedule (US-FEDQ1-010); date re-derived from the 5 U.S.C. 6103 rule (US-FEDQ1-009). LEVEL: employer reporting.
- `fed.holiday.christmas_day.observed_date` = **2026-12-25** (2026-01-01 -> 2026-12-31) [A.2, US-FEDQ1-011, second independent authority, conf high] - Pub. 15 2026 legal-holiday list = OPM 2026 schedule (US-FEDQ1-010); date re-derived from the 5 U.S.C. 6103 rule (US-FEDQ1-009). LEVEL: employer reporting.
- `fed.holiday.new_years_day.observed_date` = **2027-01-01** (2027-01-01 -> 2027-12-31) [A.2, US-FEDQ1-010, derived arithmetically, conf medium] - OPM 2027 schedule, re-derived from 5 U.S.C. 6103 and EO 11582; the IRS 2027 list (Pub. 15 for 2027) is not yet published. LEVEL: employer reporting.
- `fed.holiday.mlk_birthday.observed_date` = **2027-01-18** (2027-01-01 -> 2027-12-31) [A.2, US-FEDQ1-010, derived arithmetically, conf medium] - OPM 2027 schedule, re-derived from 5 U.S.C. 6103 and EO 11582; the IRS 2027 list (Pub. 15 for 2027) is not yet published. LEVEL: employer reporting.
- `fed.holiday.washingtons_birthday.observed_date` = **2027-02-15** (2027-01-01 -> 2027-12-31) [A.2, US-FEDQ1-010, derived arithmetically, conf medium] - OPM 2027 schedule, re-derived from 5 U.S.C. 6103 and EO 11582; the IRS 2027 list (Pub. 15 for 2027) is not yet published. LEVEL: employer reporting.
- `fed.holiday.memorial_day.observed_date` = **2027-05-31** (2027-01-01 -> 2027-12-31) [A.2, US-FEDQ1-010, derived arithmetically, conf medium] - OPM 2027 schedule, re-derived from 5 U.S.C. 6103 and EO 11582; the IRS 2027 list (Pub. 15 for 2027) is not yet published. LEVEL: employer reporting.
- `fed.holiday.juneteenth.observed_date` = **2027-06-18** (2027-01-01 -> 2027-12-31) [A.2, US-FEDQ1-010, derived arithmetically, conf medium] - OPM 2027 schedule, re-derived from 5 U.S.C. 6103 and EO 11582; the IRS 2027 list (Pub. 15 for 2027) is not yet published. LEVEL: employer reporting.
- `fed.holiday.independence_day.observed_date` = **2027-07-05** (2027-01-01 -> 2027-12-31) [A.2, US-FEDQ1-010, derived arithmetically, conf medium] - OPM 2027 schedule, re-derived from 5 U.S.C. 6103 and EO 11582; the IRS 2027 list (Pub. 15 for 2027) is not yet published. LEVEL: employer reporting.
- `fed.holiday.labor_day.observed_date` = **2027-09-06** (2027-01-01 -> 2027-12-31) [A.2, US-FEDQ1-010, derived arithmetically, conf medium] - OPM 2027 schedule, re-derived from 5 U.S.C. 6103 and EO 11582; the IRS 2027 list (Pub. 15 for 2027) is not yet published. LEVEL: employer reporting.
- `fed.holiday.columbus_day.observed_date` = **2027-10-11** (2027-01-01 -> 2027-12-31) [A.2, US-FEDQ1-010, derived arithmetically, conf medium] - OPM 2027 schedule, re-derived from 5 U.S.C. 6103 and EO 11582; the IRS 2027 list (Pub. 15 for 2027) is not yet published. LEVEL: employer reporting.
- `fed.holiday.veterans_day.observed_date` = **2027-11-11** (2027-01-01 -> 2027-12-31) [A.2, US-FEDQ1-010, derived arithmetically, conf medium] - OPM 2027 schedule, re-derived from 5 U.S.C. 6103 and EO 11582; the IRS 2027 list (Pub. 15 for 2027) is not yet published. LEVEL: employer reporting.
- `fed.holiday.thanksgiving_day.observed_date` = **2027-11-25** (2027-01-01 -> 2027-12-31) [A.2, US-FEDQ1-010, derived arithmetically, conf medium] - OPM 2027 schedule, re-derived from 5 U.S.C. 6103 and EO 11582; the IRS 2027 list (Pub. 15 for 2027) is not yet published. LEVEL: employer reporting.
- `fed.holiday.christmas_day.observed_date` = **2027-12-24** (2027-01-01 -> 2027-12-31) [A.2, US-FEDQ1-010, derived arithmetically, conf medium] - OPM 2027 schedule, re-derived from 5 U.S.C. 6103 and EO 11582; the IRS 2027 list (Pub. 15 for 2027) is not yet published. LEVEL: employer reporting.
- `fed.holiday.dc_emancipation_day.observed_date` = **2026-04-16** (2026-01-01 -> 2026-12-31) [A.2, US-FEDQ1-011, quoted from authority page, conf high] - District of Columbia legal holiday: an IRS legal holiday for federal deposit and filing dates, not a 5 U.S.C. 6103 federal holiday. LEVEL: employer reporting.
- `fed.holidays.legal_public` = **New Year's Day; Birthday of Martin Luther King, Jr.; Washington's Birthday; Memorial Day; Juneteenth National Independence Day; Independence Day; Labor Day; Columbus Day; Veterans Day; Thanksgiving Day; Christmas Day (11 legal public holidays)** (2021-06-17 -> open) [A.1, US-FEDQ1-009, quoted from authority page, conf high] - 5 U.S.C. 6103(a). For IRS due dates the DC holidays apply (adds DC Emancipation Day, April 16). 
- `fed.deposit.due_date.non_business_day_rule` = **A filing, furnishing or deposit due date that falls on a Saturday, Sunday or legal holiday moves to the next business day; legal holiday = District of Columbia legal holiday; a statewide holiday never delays a federal deposit; semiweekly depositors get one extra day for each legal holiday in the 3 weekdays after the semiweekly period** (2026-01-01 -> open) [A.2, US-FEDQ1-011, quoted from authority page, conf high] - LEVEL: employer reporting.
- `fed.fit.extra_pay_period.rule` = **No IRS rule adjusts withholding for a 27th biweekly or 53rd weekly payday: Pub. 15-T Worksheet 1A annualises each payment with the Table 3 count for the payroll period (weekly 52, biweekly 26), and Pub. 15 sec. 8 requires withholding for the regular payroll period, so the extra payday is withheld as one more ordinary period. FICA and FUTA: wages are counted when paid, against the 2026 annual bases for wages paid in 2026.** (2026-01-01 -> 2026-12-31) [A.2, US-FEDQ1-007, direct artifact inspection, conf high] - Negative finding: full text of Pub. 15-T (2026) and Pub. 15 (2026) searched for 53/27-period provisions; none. FICA/FUTA paid-basis: Pub. 15 sec. 7/9 and 31.3121(v)(2)-1(a)(1) (US-FEDQ1-004). LEVEL: withholding.

**Derivation (G-SPOT, G-DERIVE).** Each 2026 and 2027 holiday date was re-derived in Python from the 5 U.S.C. 6103(a) rule (nth weekday / fixed date) with the 6103(b)(1) Saturday-to-Friday and EO 11582 Sunday-to-Monday shifts: all 22 dates equal the OPM schedules; the 11 federal 2026 dates also equal the Pub. 15 (2026) list, which adds DC Emancipation Day (Thursday 2026-04-16).

**Negative finding (G-SPOT, direct artifact inspection).** Pub. 15-T (2026) and Pub. 15 (2026) were searched in full for any 53-weekly / 27-biweekly provision: none. Worksheet 1A line 1b takes the Table 3 count (weekly 52, biweekly 26) and Pub. 15 sec. 8 withholds per regular payroll period, so the extra payday is one more ordinary period. Fact `fed.fit.extra_pay_period.rule`.

**Confidence note.** `fed.equity.withholding_treatment.resident` is conf medium only for the RSU income-tax timing limb: no IRS publication read names RSUs in a FIT timing sentence; it rests on settlement in shares (Pub. 15-B 83(i) paragraph) and on 31.3121(v)(2)-1(b)(4)(iii). FICA/FUTA timing for RSUs is A.1 (`fed.equity.rsu.fica_timing`, conf high).

**Not obtained.** The IRS Equity (Stock)-Based Compensation Audit Techniques Guide URL returned 404; the eCFR API returned only paragraph (a) of 26 CFR 1.861-4, so the grant-to-vest sourcing period for options/RSUs of NRA employees stays open (`fed.equity.nra.sourcing_period`).

**C30 fix.** `fed.indexation.caliber` now rests on the govinfo text of 26 U.S.C. 1(f)(3) [A.1, US-FEDQ1-012]; the LII row US-FED-026 is superseded.


## QA r3b additions (agent 2, 2026-11-02)
- `fed.ein.format` [US-FEDS5-029, Pub. 15 (2026) sec. 1, PDF p.13]: nine digits, 00-0000000. RQ-556 stays open for State account-number formats. RQ-545 is closed: 401(k) / section 125 treatment is carried by the `fed.base.*` keys in CCG-m03_gross_to_net-facts.json [US-FEDS5-029, US-FEDS5-008]; m12 must use them.

## Open questions
Mirrors `unresolved[]` in the facts file: same keys, same wording.

- `fed.futa.credit_reduction.ca` (blocking: false) — The 2026 California credit reduction (potential 5.3% = 1.5% advance + 3.8% BCR add-on) becomes final only if the Title XII advance is outstanding on 2026-11-10; on 2026-11-02 only the potential figure is published (US-FEDS5-009, partial). **What would close it:** The DOL OUI "FUTA Credit Reductions" page/xlsx after 2026-11-10, or the 2026 Schedule A (Form 940) instructions. Attempted: https://oui.doleta.gov/unemploy/futa_credit.asp (2026-11-02, page updated 2026-09-11). Related rows: US-FEDS5-009.
- `fed.futa.credit_reduction.vi` (blocking: false) — U.S. Virgin Islands 2026 potential 4.8%; same 2026-11-10 determination. **What would close it:** Same DOL OUI update after 2026-11-10. Attempted: https://oui.doleta.gov/unemploy/futa_credit.asp. Related rows: US-FEDS5-009.
- ~~`fed.fica.oasdi.wage_base.next_year_reverification`~~ CLOSED 2026-11-02 (agent 2 F44): F44 2026-11-02: verified on the P4 browser copy of SSA cbb.html (US-FEDB5-401, FED/FED_SSA_cbb_browser_2026-11-02.txt l.4): "For earnings in 2027, this base is $192,300."; table row "2027 192,300".
- `fed.indexation.next_year` (blocking: false) — 2027 federal inflation adjustments (Rev. Proc. for TY2027, 401(k)/IRA notice, 2027 Pub. 15-T) not published as of 2026-11-02 (IR-2026-117..129 checked). **What would close it:** IRS releases expected Nov-Dec 2026: the TY2027 Rev. Proc., the 2027 retirement-plan limits notice and the 2027 Pub. 15-T (draft or final). Attempted: IRS news releases October 2026. Related rows: US-FEDS5-010.
- `fed.form940.instructions_edition` (blocking: false) — TY2026 Instructions for Form 940 not yet issued; the 2025 edition was read (US-FEDS5-031 partial). **What would close it:** IRS i940 (2026), usually December-January. Related rows: US-FEDS5-031.
- `fed.aca.instructions_edition` (blocking: false) — TY2026 Instructions for Forms 1094-C/1095-C not yet issued; TY2025 edition read (US-FEDS5-012 partial). **What would close it:** IRS i109495c (2026). Related rows: US-FEDS5-012.
- `fed.leave.eo13706.accrual` (blocking: false) — EO 13706 federal-contractor paid-sick-leave accrual figures not transcribed. **What would close it:** 29 CFR 13.5 from eCFR (one fetch). Related rows: US-FEDS5-026.
- `fed.bik.mileage_rate` (blocking: false) — 2026 business standard mileage rate (cents-per-mile valuation) not printed in Pub. 15-B and not fetched. **What would close it:** The IRS 2026 standard mileage rate notice. Related rows: US-FEDS5-008.
- `fed.iwo.revised_form_go_live` (blocking: false) — The revised IWO/e-IWO (gig-worker fields) must be used after the one-year extension, but the state go-live date is not published. **What would close it:** An OCSE Action Transmittal implementing ICR 202607-0970-002. Attempted: https://www.reginfo.gov/public/do/PRAViewICR?ref_nbr=202607-0970-002. Related rows: US-FEDS5-028.
- `fed.equity.nra.sourcing_period` (blocking: false) - Pub. 515 says multiyear compensation is sourced on a time basis over the period to which it is attributable (facts and circumstances); the specific grant-to-vest period rule for stock options and RSUs in Treas. Reg. 1.861-4(b)(2)(ii)(F) was not read (the eCFR API returned only paragraph (a) of 1.861-4 on 2026-11-02). **What would close it:** Full text of 26 CFR 1.861-4(b)(2)(ii)(F) on ecfr.gov (browser) or govinfo CFR annual edition, title 26 vol. 9. Related rows: US-FEDQ1-006.
