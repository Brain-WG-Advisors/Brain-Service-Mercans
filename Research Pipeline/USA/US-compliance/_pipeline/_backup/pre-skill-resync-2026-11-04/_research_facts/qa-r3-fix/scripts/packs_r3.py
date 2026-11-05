# QA r3: research-pack sections (rewritten whole file each time; inserted before "## Open questions").
import sys, os, shutil
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
BASE = r'C:/Users/instituto/Documents/brain-service/Research Pipeline/USA/US-compliance'
os.chdir(BASE)
BK = '_research/qa-r3-fix/_backup'
def put(path, section, open_lines=()):
    dst = os.path.join(BK, path.replace('/', '__'))
    if not os.path.exists(dst): shutil.copy2(path, dst)
    t = open(path, encoding='utf-8').read()
    marker = '## QA round 3 research additions (2026-11-02, agent 2)'
    if marker in t: t = t[:t.index(marker)] + t[t.index('## Open questions'):] if '## Open questions' in t[t.index(marker):] else t[:t.index(marker)]
    if '## Open questions' in t:
        i = t.index('## Open questions'); t = t[:i] + section.rstrip() + '\n\n' + t[i:]
    else:
        t = t.rstrip() + '\n\n' + section.rstrip() + '\n\n## Open questions\n'
    for ln in open_lines:
        if ln not in t: t = t.rstrip() + '\n' + ln + '\n'
    open(path, 'w', encoding='utf-8').write(t)

core = '''## QA round 3 research additions (2026-11-02, agent 2)

Inbound: `_qa/CCG-review-r3.json` blocker 1. All from local registered copies; one new local copy (26 U.S.C. 3401, govinfo, HTTP 200).

**m03 — federal bases reduced by pre-tax deductions (RQ-559, closed).** Pub. 15 (2026) sec. 15 table p.51 [US-FEDS5-029]: 401(k) elective deferrals "Generally exempt, but see section 402(g)" for income tax, "Taxable" for social security/Medicare and FUTA (`fed.base.401k_deferral.fit/.fica/.futa`); the statute agrees, IRC 3121(v)(1)(A) and 3306(r)(1)(A) [US-FEDQ3-002, US-FEDQ3-003]. 403(b) salary reduction (row 4), 457(b) salary reduction (row 8) and SIMPLE (row 5): excluded from income tax only (`fed.base.403b_salary_reduction.*`, `fed.base.457b_salary_reduction.*`, `fed.base.simple_salary_reduction.*`). Section 125 (p.47): a qualified benefit chosen takes its outside-the-plan treatment, cash chosen is fully taxable (`fed.base.section125.rule`; IRC 3121(a)(5)(G), 3306(b)(5)(G)). Pub. 15-B (2026) Table 2-1 p.6 [US-FEDS5-008]: accident and health benefits exempt from all three (`fed.base.section125_health.*`), dependent care up to 7,500 / 3,750 MFS (`fed.base.dependent_care.*`), HSA up to the contribution limit for a qualified individual (`fed.base.hsa_contribution.*`, p.17). Summary key `fed.retirement.pretax.tax_treatment`. Mirrored in `WTC-global_baseline-facts.json` for the Subject-to flags.

**m04 — FICA/FUTA wage definition and inclusion list (RQ-562, closed).** `fed.fica.wage_definition.exclusions` [US-FEDQ3-002, 3121(a)], `fed.futa.wage_definition.exclusions` [US-FEDQ3-003, 3306(b)], `fed.wages.general_definition` [US-FEDQ1-002, Pub. 15 sec. 5 p.18]. Per-payment flags: tips (`fed.base.tips.*`, Pub. 15 p.52: 20 a month test), group-term life (`fed.base.group_term_life.*`, Table 2-1 footnote 6: cost over 50,000 is FICA wages, income-tax withholding optional, FUTA exempt), educational assistance 5,250 (`fed.base.educational_assistance.*`), transportation 340 / 340 (`fed.base.transportation.*`). PFML employee contributions keep the existing key `fed.pfml.employee_contribution.w2`.

**m06 §6.1.1 — taxable income definition (RQ-567, closed).** IRC 3401(a) [US-FEDQ3-001]: `fed.fit.wage_definition` and `fed.fit.wage_definition.exclusions` ((a)(12) qualified plans incl. 401(k), (a)(14) group-term life, (a)(16) tips, (a)(18) 127/129, (a)(19) 132 fringes, (a)(22) HSA; 409A amounts are wages).

**m06 §6.3 — no Form W-4 / no SSN (RQ-568, closed).** Pub. 15 (2026) sec. 9 p.26 [US-FEDQ3-004]: "treat the new employee as if they had checked the box for Single or Married filing separately in Step 1(c) and made no entries in Step 2, Step 3, or Step 4" (`fed.w4.default_no_certificate`); pre-2020 employees single / zero allowances (`...pre2020_employee`); exempt W-4 not renewed by 15 February: same default (p.27, `fed.w4.exempt_not_renewed.default`). SSN applied for: "Applied For" / zeros and a later W-2c (p.17, `fed.ssn.not_issued.w2_rule`). Sections 4 and 9 state no higher wage-withholding rate for a missing SSN (inspected directly, pp.17, 26-27); the engine default is the W-4 default above.

**m07 §7.1 — exclusion conditions (RQ-570, closed).** Pub. 15-B (2026) [US-FEDS5-008]: `fed.bik.hsa.conditions` (p.17, HDHP 1,700 / 3,400 deductible, 8,500 / 17,000 out-of-pocket), `fed.bik.health_fsa.conditions` (p.4, 3,400 cap), `fed.bik.dependent_care.conditions` (pp.10-11), `fed.bik.educational_assistance.conditions` (p.11), `fed.bik.transportation.conditions` (pp.4, 6). Trump account: `fed.bik.trump_account.conditions` from 2026-07-04 [US-FEDR3-005, Pub. 15-A]; its FICA/FUTA treatment is not published, see Open questions.

**m07 §7.2 — valuation (RQ-572, closed).** `fed.bik.valuation.general_rule` (FMV, p.26), `fed.bik.valuation.taxable_amount` (p.4), `fed.bik.vehicle.valuation_methods` and `fed.bik.vehicle.commuting_rule.value_per_one_way` = 1.50 (p.27), `fed.bik.treated_as_paid` and `fed.bik.withholding.method` (pp.31-32), `fed.bik.vehicle.election_not_to_withhold_fit` = true (p.32; notice by 31 January or within 30 days; social security and Medicare still due).

**Also closed from the local Pub. 15 (major 5):** RQ-531 `fed.fit.supplemental.aggregate_method` (m11, p.24), RQ-524 `fed.vacation_payout.supplemental_status` (m09, p.25); RQ-556 narrowed with `fed.ein.format` = 00-0000000 (m02, p.13), State account formats still open. All on US-FEDQ1-002.

**Major 8 — NRA and totalization downstream.** WTC global_baseline now carries `fed.fica.nra.fjmq_exempt`, `fed.fica.nra.fjmq_exempt.scope`, `fed.futa.nra.fjmq_exempt`, `fed.fica.nra.other_visas.liable`, `fed.fica.totalization.exemption_rule` and the US-FEDQ1 equity / NRA keys; DD carries `dd.fed.nra.visa_class` [US-FEDR2-001] and `dd.fed.totalization.exemption` [US-FEDR2-003]. RSPEC (W-2 boxes 3/5) was not given a fact this round.
'''
put('_research/CCG-research-pack.md', core, ['- `fed.bik.trump_account.employment_tax_treatment` — FICA/FUTA treatment of employer Trump account contributions is not stated in Pub. 15 or Pub. 15-A (2026); closes with IRS guidance on irs.gov (gaps RQ-591).'])

ca = '''## QA round 3 research additions (2026-11-02, agent 2)

**RQ-508 closed — married and head-of-household Method B annual rates.** DE 44 Rev. 52 (4-26) p.48 (PDF p.56), Method B Table 6 Married Persons and Table 7 Unmarried/Head of Household, Annual Payroll Period [US-CAS5-001; the same local file backs US-CAS5-004]. Keys `ca.pit.bracket.married.N.rate / .ceiling / .base` and `ca.pit.bracket.hoh.N.rate / .ceiling / .base` (N = 1..10; band 10 has no ceiling), plus `ca.pit.bracket.married.rates`. Rates are the same ten as the single schedule: 1.1 / 2.2 / 4.4 / 6.6 / 8.8 / 10.23 / 11.33 / 12.43 / 13.53 / 14.63. Married ceilings 22,158 / 52,528 / 82,904 / 115,084 / 145,448 / 742,958 / 891,542 / 1,000,000 / 1,485,906 (base over 1,485,906: 164,228.58); HoH ceilings 22,173 / 52,530 / 67,716 / 83,805 / 98,990 / 505,208 / 606,251 / 1,000,000 / 1,010,417 (base over 1,010,417: 107,334.77). The 13.53% band runs from 1,000,000 to 1,485,906 (married) and to 1,010,417 (HoH), as printed.
Derivation line (G-DERIVE): every printed "Plus" base reproduced from the previous band, base(n) = base(n-1) + rate(n-1) x band width, within 0.01, for both tables (Python, 2026-11-02).
'''
put('_research/CCG-annex_CA-research-pack.md', ca)

al = '''## QA round 3 research additions (2026-11-02, agent 2)

**RQ-506 closed — standard-deduction phase-out.** ADOR withholding booklet rev. 01/2026, p.6 Formula step 2A, checked against the p.7 Schedule of Standard Deduction Amounts [US-ALS5-001]. Keys per status (`single`, `married_separate`, `married`, `head_of_family`): `al.wh.std_deduction.<status>.phaseout.start_gi`, `.reduction_per_step`, `.step_size`, `.floor_from_gi`, and the summary `al.wh.std_deduction.phaseout_steps` (also in WTC country_specific).
- 0/S: 3,000 up to GI 25,999; less 25 for each 500 or part above 25,999; 2,500 from 35,500.
- MS: 4,250 up to 12,999; less 88 for each 250 or part above 12,999; 2,500 from 17,750.
- M: 8,500 up to 25,999; less 175 for each 500 or part above 25,999; 5,000 from 35,500.
- H: 5,200 up to 25,999; less 135 for each 500 or part above 25,999; 2,500 from 35,500.
Derivation lines: 3,000 - 25 x 19 = 2,525; 4,250 - 88 x 19 = 2,578; 8,500 - 175 x 19 = 5,175; 5,200 - 135 x 19 = 2,635 (last stepped values, each above its floor); schedule spot checks MFJ 26,000-26,499 = 8,325 and MS 13,000-13,249 = 4,162 match.
'''
put('_research/CCG-annex_AL-research-pack.md', al)

ar = '''## QA round 3 research additions (2026-11-02, agent 2)

`ar.report.sui.efile_threshold_employees` (250) was removed from the facts: neither the local DWS Employer Handbook (US-ARP9V-001) nor any other local Arkansas file carries the figure. It is now unresolved (gaps RQ-590).
'''
put('_research/CCG-annex_AR-research-pack.md', ar, ['- `ar.report.sui.efile_threshold_employees` — the 250-employee electronic-filing threshold is not in any local Arkansas file; closes with Ark. Code Ann. 11-10-215 or the DWS employer reporting page (gaps RQ-590).'])
print('packs written')
