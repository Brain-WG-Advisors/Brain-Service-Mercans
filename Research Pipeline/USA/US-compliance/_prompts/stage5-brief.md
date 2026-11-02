# Stage 5 brief — 13-domain hunt, one worker per jurisdiction unit (US build)

Written by the orchestrator, 2026-11-02. Every Stage-5 worker reads this file first. The mandate is SEALED (seal attempt 6, 65/65); do not edit MANDATE.md, SKELETON-MANIFEST.md or build-manifest.json.

BASE = C:\Users\instituto\Documents\brain-service\Research Pipeline\USA\US-compliance (never write under ~/mercans-pipeline).

## Your unit
You are given one JUR (FED, MULTI or a USPS code). Read only what concerns your JUR:
- `_pipeline/build-manifest.json`: `tier.by_domain`, `tier._by_jurisdiction[JUR]`, `tier._sub_national_key`, `languages`, `source_partitioning`.
- `00-official-sources/MANDATE.md`: your jurisdiction question block (US-MQ-20..70) or, for FED/MULTI, US-MQ-01..14; plus the US-OWN-001..007 decisions.
- `00-official-sources/legal-basis-register.csv`: the `active` rows for your JUR. **Reuse them; do not re-fetch what an active A.1/A.2 row already holds with a local file.** Re-fetch only when the row lacks a local file or the edition is not the 2026 one.

## What to cover (all 13 domains of the method, mapped to the US)
For a state/DC unit, per domain record: the rule, every number with vigência (effective_from/to), the instrument, and a register_id. "Not applicable" needs a cited reason.
1. labour_code: minimum wage (2026 and any 2027 already enacted; local minimum wages in the state), overtime rules beyond FLSA, pay frequency, pay-day timing, method of payment (direct deposit/paycard consent).
2. income_tax: state withholding method 2026 (formula/tables, allowances or W-4 equivalent form name and edition), supplemental rate, rounding, reciprocity, local income taxes (who withholds, rates, residence vs work location), resident/nonresident rules.
3. social_security: SUI (2026 taxable wage base, new-employer rate, rate range, employee contribution if any), SDI/TDI/PFML (rates, wage caps, employee/employer split, start dates), employer levies (use the P7/P9 list; do not redo).
4. payslip_statute: required pay-statement content, delivery (electronic consent), retention.
5. reporting_instruments: withholding return(s) and deposit frequency, annual reconciliation, state W-2 filing (format: EFW2 or state spec, deadline), quarterly UI wage report (format, deadline), new-hire reporting (deadline, fields), registration.
6. leave: paid sick leave statute (accrual, cap, payout rules), PFML benefit-side payroll interaction, other mandated leave with pay impact.
7. termination: final pay timing (discharge vs resignation), accrued vacation payout rule, separation notices (e.g. UI separation notice), WARN-style state laws only if payroll-relevant.
8. benefits_in_kind: state conformity to federal exclusions (401(k), 125, HSA, transit, group-term life) — where the state departs from federal (e.g. PA, NJ, CA HSA).
9. deductions_garnishments: wage-deduction authorization rules, state garnishment limits that differ from CCPA, child-support IWO state specifics (fees, priority), state tax levies.
10. collective_agreements: prevailing wage (public works) — payroll-relevant obligations (certified payroll), threshold. (Use the P5/P6 rows already registered.)
11. indexation: what is indexed annually (min wage, wage base, PFML cap, brackets) and the publication that carries the new value.
12. data_protection: SSN truncation on pay statements, payroll-record privacy rules.
13. live_legal_change: changes effective in 2026 or already enacted for 2027 (search the agency's news/bulletins from 2026-01-01 to today).
Plus **special populations** (US-OWN-005, state-level round): domestic/household workers, agricultural, minors, tipped employees, clergy/religious, students, nonresident aliens, statutory employees, government employees — state rules that change payroll treatment (withholding, UI coverage, minimum wage). One line each: rule + register_id, or "no state rule beyond federal" with the page read.

FED unit: federal layer for the same domains (FIT Pub. 15-T 2026 incl. 2027 indications, FICA/Additional Medicare, FUTA incl. 2026 credit-reduction states, W-4, 941/944/940, W-2/W-3 + EFW2 2026, deposit rules, Pub. 15/15-A/15-B, FLSA, CCPA, IWO, federal new-hire, ACA reporting 1094/1095-C, nonresident alien withholding, supplemental rates, backup withholding relevance). MULTI unit: work-location vs residence rules, reciprocity matrix (all states), convenience-of-employer rules, UI localization test, remote-work sourcing, multistate W-2 reporting, nexus/registration triggers.

## Access rules
- VPN Windscribe (US exit) is usually on; check `curl -s ipinfo.io`. Fetch with curl, save the file, read it locally. Never take a number from a search summary or WebFetch summary (G-NUMBER).
- Blocked: try `https://web.archive.org/web/2026id_/<url>` once. If still blocked: record the exact URL as an ACCESS gap and move on. **Do not use Claude in Chrome** (the orchestrator runs a single browser pass afterwards). Never add browser-style headers to dodge a bot check.
- Tier B (Justia, FindLaw, Cornell LII, vendors, law firms) = leads only, never support for a number.

## Known access routes (from earlier workers)
- Texas statutes: `https://tcss.legis.texas.gov/resources/{CODE}/htm/{CODE}.{ch}.htm` (plain curl).
- Illinois statutes: `https://ftp.ilga.gov/ILCS/Ch%20{CCCC}/Act%20{AAAA}/{CCCC}{AAAA}0K{sec}.html`; Admin. Code under `/JCAR/`.
- Ohio statutes: codes.ohio.gov works with curl.
- Alabama Code: POST to `https://alison.legislature.state.al.us/graphql` (see _research/stage5/AL.md).
- Utah admin rules: adminrules.utah.gov JSON API (see _research/stage5/UT.md).
- Montana statutes: mca.legmt.gov (see _research/stage5/MT.md).
- Wayback copies may arrive gzip-compressed: use `curl --compressed`.

## MULTI hand-offs (each state unit checks its own)
Read `_research/stage5/MULTI.md` open questions and answer for your state: SUI wage-base credit for wages reported to another state; PFML/SDI coverage of multistate workers; paid-sick-leave coverage of employees working partly in the state; pay-statement reach to out-of-state work. LA: Act 382 of 2025 30-day nonresident rule and whether LAC 61:I.1923 amendment was adopted. AR: 2021 repeal of convenience rule (official source).

## Outputs (write incrementally — one register row as each source is acquired; a crash must not lose work)
- Source files: `00-official-sources/ccg-sources/{JUR}/` with the date in the name (2026-11-02 or the day you fetch).
- Register shard: `00-official-sources/_register-shards/S5-{JUR}.csv` — the same 20 columns as legal-basis-register.csv; ids `US-{JUR}S5-NNN`; tier only A.1/A.2/A.3/B/C; status active/MANUAL/gated/partial; `supersedes` = a real id or empty; `consumed_by` = the artifact(s) that will use it (CCG, DD, WTC, RSPEC, SIR, PSL).
- Findings: `_research/stage5/{JUR}.md` — one section per domain (rule, numbers with vigência, register_ids, confidence), the special-populations table, then "ACCESS gaps" (exact URLs) and "Open questions".
- Do NOT write `legal-basis-register.csv` (the synthesis merges the shards), any research pack/facts file, or anything under 01-…09-.

## Scratch
The session scratchpad is shared by parallel workers: put every helper script and temp file in your own subfolder `<scratchpad>/{JUR}/` (create it).

## Budget
Declare it in your first message: about 60 fetches and 2 h wall clock for a state; 90 fetches / 3 h for FED and MULTI. At 75% of either, stop fetching and finish the files. Return a 5-line summary: domains covered, rows written, ACCESS gaps, open questions, confidence.
