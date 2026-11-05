# Shared appends proposed by the US run close (for the owner to apply)

Written by compliance-qa-auditor on 2026-11-04. Nothing here has been written to `~/mercans-pipeline/shared/`. Apply each block to the named file. Numbering follows the last entries found on 2026-11-04 (L11 in `CCG-Playbook-Learnings.md`, F74 in `country_failure_log.md`).

---

## 1. Append to `shared/CCG-Playbook-Learnings.md`

## L12
*2026-11-04, US run close, compliance-qa-auditor.* Never run a builder's reconciliation or lint script in place at run close. Several of them (US `sir_recon.py`, `dd_recon.py`, `wtc_recon.py`, `design_recon.py`) rewrite files in `<artifact>/_build/checks/`, and some of those files are listed in `md5_final.txt`. In the US run, `sir_recon.csv` was overwritten (the 2 DD fields added later showed as NO_CONSUMER) and had to be restored byte for byte. Copy the checks file first, or give the script an output path under `07-qa-crosscheck/`, then compare.

## L13
*2026-11-04, US run close, compliance-qa-auditor.* A rebuild of any upstream artifact after the SKILL has passed has to trigger a same-day F28 check of `references/`. In the US run, fact fixes made at the design stage rebuilt the CCG (13:29) and the DD (13:15) after the SKILL was built (12:30), so five practice notes and two DD elements went stale in the skill. Make the skill the last thing built, after DESIGN, or re-run its generator whenever an upstream md5 changes.

## L14
*2026-11-04, US run close, compliance-qa-auditor.* Every change to an artifact after its PASS needs its own targeted review file in `_qa/`. Evidence recorded only inside another artifact's review is not enough. In the US run, CCG b9de40ce and DD f65dc9bc changed after their last review. The DD diff was checked inside DESIGN-review-r2 and the WTC diff inside SIR-review-r3, so the run close had to rebuild the trail.

## L15
*2026-11-04, US run close, compliance-qa-auditor.* Register `effective_from` (and `verified_on`) when a row is created, not at run close. C41 looks at every non-superseded row. At US run close, 987 rows were not current: 948 had no effective_from, 19 were past their effective_to but still active, and 19 had no verified_on. No one had written `bulletin-sweep.json`. For a statute, use the in-force date; for a guide, use its publication or revision date; mark a past row `superseded` or `historical`. Write the bulletin sweep at Stage 3 and refresh it within 14 days of the run close.

## L16
*2026-11-04, US run close, compliance-qa-auditor.* Plan Test 0 (C39) for authority sites that block automated fetches. From this machine, 15 of the 56 sampled assertions could not be fetched (HTTP 403 from ssa.gov/oact, mass.gov, ncleg.gov, leginfo.ca.gov, twc.texas.gov, famli.colorado.gov and michigan.gov; refused connections from in.gov, le.utah.gov and oregonlegislature.gov; a script-only page at flsenate.gov). Keep those items as UNVERIFIED rather than dropping them, and verify them through a browser session from the start.

---

## 2. Append to `shared/country_failure_log.md`

## F75 — In-place check run overwrites a sealed check output
- **Source:** US run close, 2026-11-04 (`03-statutory-integrations/_build/checks/sir_recon.csv`).
- **Observed:** re-running `sir_recon.py` at Stage 8 rewrote a file listed in the SIR `md5_final.txt`. It added two NO_CONSUMER rows for DD elements created after the SIR build, which the SIR recon cannot credit to DESIGN.
- **Root cause:** builder check scripts write to fixed paths inside the artifact folder, and the run-close audit re-uses them.
- **Mitigation:** L12. Run-close checks write to `07-qa-crosscheck/`. The md5 of every sealed list is compared after each check.

## F76 — Register currency left to the run close
- **Source:** US run close, 2026-11-04 (C41).
- **Observed:** 987 of 2,456 non-superseded register rows were not current, and `bulletin-sweep.json` was missing. C41 failed at the last gate after every artifact had passed.
- **Root cause:** `effective_from` and `verified_on` are optional when a row is written, and no stage before Stage 10 runs C41.
- **Mitigation:** L15. Run C41 at every artifact close as a warning, and make it blocking at Stage 3.

## F77 — Test 0 starved by blocked authority sites
- **Source:** US run close, 2026-11-04 (C39 73.2 %).
- **Observed:** all 41 assertions that could be fetched passed, but 15 stayed UNVERIFIED because of 403s, refused connections and script-only pages. The registered local copies hold all 15 values.
- **Root cause:** geo and anti-bot blocks on US government sites, combined with a C39 rule that counts UNVERIFIED as a failure.
- **Mitigation:** L16. Do Test 0 in a browser session (Claude in Chrome) or from a US network. Keep the access route in `country_portal_registry.md`.

---

## 3. Append to `shared/country_portal_registry.md`

# United States (US)

*Added 2026-11-04 from `03-statutory-integrations/integration-landscape.json` (SIR v1.0, verdict HAS_INTEGRATIONS) and the 20 Report Specifications.*

| Institution | Portal / channel | Filings | Mercans route |
|---|---|---|---|
| Third-party filing provider (owner decision US-MQ-09) | File hand-off of the SIR section 8 data set; product mapping required | All in-scope federal, State and local returns, deposits and new-hire reports | The only integrable party. The provider runbook is not issued until a provider is chosen (SIR-RQ-27) |
| IRS | Provider-transmitted e-file / portal; no system-to-system channel recorded | Forms 941, 944, 943, 940, 941-X, Schedule H routing, 1042-S, 1094-C/1095-C (US-IRS-001..008) | Through the provider |
| SSA | Business Services Online (BSO), EFW2 Pub. 42-007 / EFW2C Pub. 42-014; AccuWage only inside an authenticated BSO session | W-2/W-3 (US-SSA-001) | Through the provider |
| State revenue departments (50 + DC) | State e-file portals and bulk files (examples: CA DE 8300 bulk XML/ICESA/MMREF-1/CSV; NY NYS-45 web upload; OH FSET) | State withholding returns, annual reconciliation / State W-2 (US-DOR-001..004) | Through the provider |
| State UI / workforce agencies | Portal entry, CSV/Excel upload, SFTP for large files and payroll service providers (for example NJ WR-30) | Quarterly UI wage reports (US-UI-001) | Through the provider |
| State programme agencies (PFML, disability, WC funds) | Batch XML (XSD) or CSV via SFTP (CT Paid Leave File Specification Toolkit) and portals | US-PFML-001, US-WC-001 | Through the provider |
| State Directories of New Hires | Electronic, two monthly transmissions 12–16 days apart, or within 20 days (42 U.S.C. 653a) | US-SDNH-001 | Through the provider |
| Local tax bodies (PA EIT/LST collectors, OH municipalities, Seattle, NYC, Philadelphia and others) | Local collector portals | US-LOC-001..003 | Through the provider |

**Access cautions (from this machine, 2026-10-29 to 2026-11-04):** geo blocks at dew.sc.gov and twc.texas.gov. HTTP 403 for automated fetches at ssa.gov/oact, mass.gov, ncleg.gov, leginfo.legislature.ca.gov, famli.colorado.gov and michigan.gov. Refused connections at in.gov, le.utah.gov and oregonlegislature.gov. flsenate.gov returns script-only pages. Use a browser session or a US network, and see `BLOQUEIOS-CHROME.md` in the US folder.

**Format rule carried:** no real US filing was available, so every Report Matrix row is marked "FORMAT TO CONFIRM vs a real filing".
