# Agent 2 (source hunter): QA round 3 fixes (2026-11-02)

Inbound: `_qa/CCG-review-r3.json`, blockers 1-3, majors 5, 6 and 8, minors 9 and 13. Major 7 (50 rows with no local copy) was not in this pass's scope.
Every file rewritten has a backup in `_research/qa-r3-fix/_backup/`. Scripts are in `_research/qa-r3-fix/scripts/` (`apply_r3.py`, `gaps_r3.py`, `extra_r3.py`, `packs_r3.py`). Logs: `apply-r3-log.json`, `gaps-r3-log.json`, `gap-local-candidates.json`.
This pass wrote nothing under `01-ccg/` or `~/mercans-pipeline`, did not touch MANDATE or the manifest, and did not run `rebuild_all.py`.
Budget: about 85 tool calls and 3 web fetches. The fetches were a govinfo 3401 copy (HTTP 200) and two failed NH attempts (Wayback 429, gc.nh.gov 403).

All 19 facts files that changed validate against `facts.schema.json` 1.4.0 with 0 errors. Every `register_id` in every facts file resolves, and no file has a duplicate (key, effective_from) pair. The register now holds 2,616 rows, all 20 columns wide, with unique ids.

| Item | Action | Keys / rows |
|---|---|---|
| Blocker 1, RQ-559 (closed) | Pub. 15 (2026) sec. 15 p.51 rows 2/4/5/8 and p.47 (cafeteria); Pub. 15-B Table 2-1 p.6, pp.10, 17; IRC 3121(v)(1)(A), 3306(r)(1)(A), (5)(G) | `fed.retirement.pretax.tax_treatment`, `fed.base.{401k_deferral,403b_salary_reduction,457b_salary_reduction,simple_salary_reduction,section125_health,dependent_care,hsa_contribution}.{fit,fica,futa}`, `fed.base.section125.rule`; m03, mirrored in WTC/global_baseline; US-FEDS5-029, US-FEDS5-008, new US-FEDQ3-001/002/003 |
| Blocker 1, RQ-562 (closed) | 3121(a), 3306(b), Pub. 15 sec. 5 p.18, sec. 15 p.52 (tips), Table 2-1 | `fed.fica.wage_definition.exclusions`, `fed.futa.wage_definition.exclusions`, `fed.wages.general_definition`, `fed.base.{tips,group_term_life,educational_assistance,transportation}.*`; m04 + WTC; US-FEDQ3-002/003, US-FEDQ1-002 |
| Blocker 1, RQ-567 (closed) | 26 U.S.C. 3401(a), new local copy (md5 in register) | `fed.fit.wage_definition`, `fed.fit.wage_definition.exclusions`; m06 §6.1.1; US-FEDQ3-001 |
| Blocker 1, RQ-568 (closed) | Pub. 15 sec. 9 p.26: "treat the new employee as if they had checked the box for Single or Married filing separately in Step 1(c) and made no entries in Step 2, Step 3, or Step 4"; p.27; sec. 4 p.17 | `fed.w4.default_no_certificate` (+ `.pre2020_employee`), `fed.w4.exempt_not_renewed.default`, `fed.ssn.not_issued.w2_rule`; m06 + WTC; new US-FEDQ3-004 |
| Blocker 1, RQ-570 (closed) | Pub. 15-B pp.4, 6, 10-11, 17; Pub. 15-A (Trump account) | `fed.bik.{exclusion_conditions,hsa.conditions,health_fsa.conditions,dependent_care.conditions,educational_assistance.conditions,transportation.conditions,trump_account.conditions}`; m07. Unresolved: `fed.bik.trump_account.employment_tax_treatment` (RQ-591) |
| Blocker 1, RQ-572 (closed) | Pub. 15-B General Valuation Rule p.26, Commuting Rule p.27, sec. 4 pp.31-32 | `fed.bik.valuation.{general_rule,taxable_amount}`, `fed.bik.vehicle.{valuation_methods,commuting_rule.value_per_one_way (1.50),election_not_to_withhold_fit}`, `fed.bik.treated_as_paid`, `fed.bik.withholding.method`; m07 |
| Blocker 2, RQ-508 (closed) | DE 44 Rev. 52 p.48 (PDF p.56), Method B Tables 6 and 7, annual. G-DERIVE: each printed "Plus" base was reproduced from the previous band within 0.01 | `ca.pit.bracket.{married,hoh}.N.{rate,ceiling,base}` (N = 1..10) plus `ca.pit.bracket.married.rates`; annex_CA. Row US-CAS5-001, the Method B tables row, which shares a local file with US-CAS5-004. WTC has no CA bracket keys, so nothing was added there |
| Blocker 3, RQ-506 (closed) | Booklet rev. 01/2026 p.6 formula, checked against the p.7 schedule (MFJ 26,000-26,499 = 8,325; MS 13,000-13,249 = 4,162) | `al.wh.std_deduction.<single/married_separate/married/head_of_family>.phaseout.{start_gi,reduction_per_step,step_size,floor_from_gi}` and `al.wh.std_deduction.phaseout_steps`; annex_AL + WTC/country_specific; US-ALS5-001 |
| Major 6 (14 keys + 2 SC) | **Re-pointed:** `sc.pit.wh.band.2/3.rate` to US-SCP51-002 (WH-1603F p.1); `oh.wh.supplemental.rate` to US-OHS5-007 (ORC 5747.02(A)(3)(c) "2026 and thereafter ... 2.75%"; OAC 5703-7-10 points to it). **G-DERIVE** (fact set to `derived arithmetically`, line in the register): `co.famli.employee/employer.rate` 2027 = 0.86 x 50%; `ma.pfml.medical.rate` 2026 and `ma.pfml.family.rate` 2027 = 0.28 + 0.42; `ms.oracle.weekly_460_0ex.withholding` = (460x52-2,300-10,000) x 4% / 52 = 8.94; `wv.sui.employer.rate.max` = 7.5 + 1% surtax. **Quote recorded** (value is already in the row's own file): `de.local.wilmington.eit.rate` (the .bin file is a PDF, p.11 "one and one quarter percent (1.25%)"), `nc/pa.overtime.premium.multiplier` ("time and one half"), `nd/sd.data.breach.ag_threshold` ("two hundred fifty"), `wa.pit.high_income_tax.agi_threshold` ("$1 million"), `co.famli.*` 2026 0.44. **Recounted:** `oh.pit.municipal.count_in_force` 678 (1,083 rows, 685 codes), set to direct artifact inspection. **Moved to unresolved:** `ar.report.sui.efile_threshold_employees` (no local file holds 250; RQ-590) | annex_SC/OH/CO/MA/WV/AR, m12, WTC/country_specific |
| Major 8 | consumed_by for US-FEDR2-001..004 now lists CCG/m05, CCG/m06, CCG/annex_FED, WTC/global_baseline and DD/8_sheets. WTC got the 5 NRA/totalization facts and the US-FEDQ1 equity/NRA facts. DD got `dd.fed.nra.visa_class` (US-FEDR2-001) and `dd.fed.totalization.exemption` (US-FEDR2-003). US-FEDQ1-001/004/006/007/008 now list WTC/global_baseline; US-FEDQ1-002 lists the CCG units it now feeds. **Not done:** RSPEC (no W-2 box 3/5 fact was emitted, so no token was added). US-FEDQ1-003 and -005 are cited by no fact, so consumed_by stays empty | register; WTC-global_baseline; DD-8_sheets |
| Major 5 (partial) | Two more were closed from local Pub. 15: RQ-531 `fed.fit.supplemental.aggregate_method` (p.24) and RQ-524 `fed.vacation_payout.supplemental_status` (p.25). RQ-556 was narrowed with `fed.ein.format` (p.13). The 385 open entries never searched by URL were swept against the local files of their jurisdiction: `local_searched=true`, and searched[] gained a "local-files sweep" line. 181 have candidate files that contain the key's terms, listed in `gap-local-candidates.json`; none of these was judged answered. The unrelated ssa.gov lines on RQ-562 were removed, and closed entries list only the searches made for that key | gaps.json; CCG-research-request.json |
| Minor 9 | Gap entries RQ-581..591 were added for the agent-2 unresolved items that had none (FED totalization, GA, HI, IA, IN, KY x2, MA IP 25-18, NC student rate, AR, Trump account), with matching request entries so the builder can tag `[[GAP:RQ-…]]`. TN PC 617 already had one. No MA domestic meal/lodging unresolved key exists to tag | gaps.json; request file |
| Minor 13 | US-AKS5-009, US-FED-028, US-UTP6-002 and -003 got the "in force as at retrieved_on" note. US-LAP6-001 is noted as a repealed section and US-TXB5-301 as a proposed rule not adopted (no date invented). **US-NH-001 verified_on left empty:** revenue.nh.gov returned 403, Wayback 429 and gc.nh.gov 403, and these attempts are written in the row | register |

Gaps counts: closed 10, open 532, documented_limitation 32, check_existing_fact 1. Open entries not searched by URL: 383, all now locally swept.

## For the builder (agent 3)
Render the new keys in m03 Step 2, m04 §4.2 (the FUTA column), m06 §6.1.1 and §6.3, m07 §7.1 and §7.2, CA.2 and AL.2, and remove `[[GAP:RQ-506/508/524/531/559/562/567/568/570/572]]`. Remove the AR 250 figure and tag RQ-590. Tag the Trump account FICA/FUTA limitation RQ-591.

## For the auditor (agent 4)
The propagation ledger needs lines for:
- the new rows US-FEDQ3-001..004;
- the re-points of SC to US-SCP51-002 and OH to US-OHS5-007;
- the AR key moved to unresolved;
- the WTC/DD facts mirrored from m05/m06.

## Parallel shape of what remains
The 181 local candidates can be triaged per jurisdiction, one worker per state, in parallel. Major 7 (50 rows without a copy) and US-NH-001 need one browser or US-exit pass.

## Open questions (mirrors the new unresolved[])
- `fed.bik.trump_account.employment_tax_treatment`: the FICA/FUTA treatment of employer Trump account contributions is not stated in Pub. 15 or Pub. 15-A (2026). It closes with IRS guidance on irs.gov.
- `ar.report.sui.efile_threshold_employees`: the 250-employee e-file threshold is not in any local Arkansas file. It closes with Ark. Code Ann. 11-10-215 or the DWS reporting page.
