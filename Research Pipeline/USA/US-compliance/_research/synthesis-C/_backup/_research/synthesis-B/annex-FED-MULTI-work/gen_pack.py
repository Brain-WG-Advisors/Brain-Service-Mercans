import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import BASE

ORDER = ['labour_code', 'income_tax', 'income_tax_nonresident', 'social_security', 'payslip_statute', 'reporting', 'leave', 'termination',
         'benefits_in_kind', 'deductions_garnishments', 'collective_agreements', 'indexation', 'data_protection', 'live_legal_change',
         'special_populations', 'oracle']
TITLE = {'labour_code': '1 — Employment / labour code', 'income_tax': '2 — Income tax', 'income_tax_nonresident': '2b — Non-resident regime',
         'social_security': '3 — Social security', 'payslip_statute': '4 — Payslip statute', 'reporting': '5 — Statutory reporting instruments',
         'leave': '6 — Leave', 'termination': '7 — Termination', 'benefits_in_kind': '8 — Benefits in kind', 'deductions_garnishments': '9 — Deductions and garnishments',
         'collective_agreements': '10 — Collective agreements', 'indexation': '11 — Indexation', 'data_protection': '12 — Payroll data protection',
         'live_legal_change': '13 — Live legal change', 'special_populations': 'Special populations (US-OWN-005)', 'oracle': 'Oracle (worked examples)'}


def line(x, pending=False):
    v = x['value']
    vs = f'**{v}**'
    unit = x.get('currency') or x.get('unit_of_measure') or ''
    rng = f"{x['effective_from']} → {x['effective_to'] or 'open'}"
    tag = ' — PENDING register_id pattern' if pending else ''
    s = f"- `{x['key']}` = {vs} {unit} ({rng}) [{x['tier']}, {x['register_id']}, {x['verification_method']}, conf {x['confidence']}]{tag}"
    if x.get('note'):
        s += f" — {x['note']}"
    return s


def build(unit, intro, prose, extra_sections, out):
    d = json.load(open(os.path.join(BASE, '_research', f'CCG-{unit}-facts.json'), encoding='utf-8'))
    facts = [(x, False) for x in d['facts']] + [(x, True) for x in d.get('_facts_pending_register_id_pattern', [])]
    L = [intro, '']
    for dom in ORDER:
        fx = [p for p in facts if p[0].get('_domain') == dom]
        if not fx and dom not in prose:
            continue
        L.append(f'## {TITLE[dom]}')
        if dom in prose:
            L.append(prose[dom])
            L.append('')
        for x, pen in fx:
            L.append(line(x, pen))
        L.append('')
    L += extra_sections
    L.append('## Open questions')
    L.append('Mirrors `unresolved[]` in the facts file: same keys, same wording.')
    L.append('')
    for e in d['unresolved']:
        L.append(f"- `{e['key']}` (blocking: {str(e.get('blocking', True)).lower()}) — {e['why']} **What would close it:** {e['what_would_close_it']}"
                 + (f" Attempted: {'; '.join(e['attempted'])}." if e.get('attempted') else '')
                 + (f" Related rows: {', '.join(e['_related_register_ids'])}." if e.get('_related_register_ids') else ''))
    L.append('')
    open(out, 'w', encoding='utf-8', newline='\n').write('\n'.join(L))


# ---------------- FED ----------------
fed_intro = """# CCG annex_FED research pack — Federal layer

Synthesis B, 2026-11-02. Source: `_research/stage5/FED.md` and the active/partial rows of `00-official-sources/legal-basis-register.csv`; no fetching. Facts file: `_research/CCG-annex_FED-facts.json` (validator: PASS). Every value below is a fact object there; key in backticks, register id in brackets. Keys use the `fed.` prefix (state annexes use `{jur}.`, the routing layer `multi.`).

**Summary.** The federal layer is one calculation per employee on top of every State: FIT under Pub. 15-T 2026 (Worksheet 1A, annual percentage method), FICA (OASDI 6.2% + 6.2% to 184,500; Medicare 1.45% + 1.45%; Additional Medicare 0.9% employee-only over 200,000), FUTA (net 0.6% on 7,000 plus any credit reduction), deposits (lookback), Form 941/940/944, W-2/W-3 with the new P.L. 119-21 codes TP/TT/TA and box 14b, ACA 1094-C/1095-C, new-hire reporting, and the CCPA/levy/IWO garnishment floor. No federal pay-statement statute: payslip content is State law. Stage-5 confidence: high except the 2026 FUTA credit reductions (final after 2026-11-10) and EFW2 TY2026 (gated).

**Reuse rule carried from Stage 5.** Rows US-FED-001..030 stay active but have no local file; the US-FEDS5 rows carry the local copies and are cited first. Supersession applied at the merge: US-FEDS5-028 supersedes US-FEDP6-001 and closes the gated US-FEDR3-004 (IWO renewal approved 2026-08-25, expiry 2029-08-31) — this replaces the "renewal pending" modelling of US-OWN-007.

**Language (US-OWN-006).** Federal: English is the only official language and places no obligation on private employers [US-FED-020]; no federal instrument fixes pay-statement content or language [US-FED-010, US-FEDS5-021]; IRS/SSA filings in English. Spanish (rank 2) and other-language seams attach only to State notices/posters (State annexes)."""

fed_prose = {
    'labour_code': 'FLSA floor; the employer pays the highest of federal, State and local minimum (State annexes). Pay frequency, pay-day timing and method of payment have no federal rule.',
    'income_tax': 'G-DERIVE: column C of the three STANDARD schedules recomputed in Python from column A and the rates; top values equal the row (206,583.50 / 192,979.25 / 191,171.00). Zero brackets = 2026 standard deduction minus line 1g, standard deductions confirmed in a second document family (Rev. Proc. 2025-32). The Step-2-checked schedule thresholds are transcribed; their column C was not compared with the publication and is not emitted. Local income tax and reciprocity are not federal (annex_MULTI, State annexes).',
    'income_tax_nonresident': 'Non-resident aliens are treated at WITHHOLDING level: the Pub. 15-T add-on increases the wage used for the FIT computation only (no W-2, FICA or FUTA effect) and is not applied to 22%/37% supplemental wages. Notice 1392 W-4 rules; Form 8233 treaty wages go to 1042-S (IRIS e-file for TY2026). This satisfies C31 for the federal layer; State non-resident (other-State resident) treatment is annex_MULTI.',
    'social_security': 'The 2027 OASDI base 192,300 is an SSA-published value carried with medium confidence because re-verification on 2026-11-02 was blocked (ssa.gov 403). FUTA 2026 credit reductions (CA potential 5.3%, USVI 4.8%) are NOT facts until the 2026-11-10 determination; only the final 2025 reductions are emitted.',
    'payslip_statute': 'No federal pay-statement statute; FLSA prescribes records only. Pay-statement content, delivery and language: State annexes.',
    'reporting': 'EFW2 TY2026 is an ACCESS gap (US-FEDS5-032 gated). TY2026 i940 and i1094/1095-C not yet published: 2025 editions read (rows partial).',
    'leave': 'No federal paid sick or annual leave for private employers; State PFML/PSL in State annexes.',
    'termination': 'Final-pay timing and vacation payout are State law; WARN pay-in-lieu is the only federal payroll touchpoint.',
    'benefits_in_kind': 'Federal exclusions are the baseline the States conform to or depart from (State conformity per State annex). The 2026 business mileage rate is open.',
    'deductions_garnishments': 'CCPA floor; State limits may be stricter (State annexes). IRS levy is not subject to the CCPA cap (Pub. 1494 exempt amounts). Interstate IWO governing law: annex_MULTI.',
    'indexation': 'FLSA minimum wage, CCPA multiplier and the 684 salary floor are not indexed; the 2,000 information-return threshold is indexed after 2026. 2027 Rev. Proc. not yet published (no projections used).',
    'live_legal_change': 'P.L. 119-21 (enacted 2025-07-04, in force). Level carried in each fact: tips/overtime deductions operate at ASSESSMENT (withholding only via W-4 Step 4(b)); employer duty is REPORTING (W-2 TP/TT/14b). Do not build a payroll deduction for them. Proposed IRS regulations of October 2026 (IR-2026-117, -121) do not touch employer payroll.',
    'special_populations': 'US-OWN-005: all populations IN; federal rules in full here, State-level rules in the State annexes.',
    'oracle': 'Federal oracle per build-manifest.oracle: Pub. 15-T 2026 publishes only two worked examples (NRA weekly 526.90 -> 31; tribal monthly 6,000 -> 584.09); no full percentage-method example, so Stage 9b re-derives from Worksheet 1A + the Annual Percentage Method tables. The IRS Tax Withholding Estimator is not an oracle [US-FED-021]. State worked examples (CA DE 44, GA, MN, MI, OH, NY, IL, WI, VT, CT, ...) belong to the State annexes and to CCG m12_worked_examples.',
}
fed_extra = ["""## Special populations table (federal)
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
"""]
build('annex_FED', fed_intro, fed_prose, fed_extra, os.path.join(BASE, '_research', 'CCG-annex_FED-research-pack.md'))

# ---------------- MULTI ----------------
multi_intro = """# CCG annex_MULTI research pack — Multistate routing layer

Synthesis B, 2026-11-02. Sources: `_research/stage5/MULTI.md`, the MULTI hand-off sections of the 51 State findings files (`_research/stage5/{JUR}.md`) and the active/partial rows of `00-official-sources/legal-basis-register.csv`; no fetching. Facts file: `_research/CCG-annex_MULTI-facts.json` (validator: PASS). Keys use the `multi.` prefix with the State code after the concept.

**What this annex routes.** Three keys from the build manifest drive every multistate decision: `work_location_jurisdiction` (income-tax withholding State and wage-hour law), `residence_jurisdiction` (resident withholding, reciprocity, transport-worker and military-spouse rules) and `sui_state` (UI, and by default PFML/SDI). Income tax is sourced to the place of physical performance except where a convenience/necessity rule applies (NY, PA, DE, NE; NJ and CT retaliatory). UI covers the entire service in ONE State by the localization test.

**Register-id pattern defect (contract).** 37 facts rest on active A.1/A.2 rows whose ids have a multi-segment form (US-XX-P5-1-003, US-AZ-WH-003, US-FED-P5-1-009 ...) that the facts.schema `register_id` pattern rejects. They are held unchanged in `_facts_pending_register_id_pattern` and are listed below with the tag "PENDING register_id pattern". Where a pattern-compliant row stated the same rule (MO, OK, IL partners, MS and AR credit level) it was cited instead. This is a contract decision for the scaffolder/owner, not a research gap.

**Corrections to MULTI.md applied here.** (1) MS has a resident withholding rule (withhold MS except to the extent another State withholds; full MS on commuters to no-tax States) — moved out of "credit only" [US-MSS5-004, US-MSS5-019]. (2) LA: the LAC 61:I.1923 rule is ADOPTED (LR 52:358, 2026-03-20) [US-LAS5-002], superseding the NOI row US-MULTIS5-022. (3) AR convenience question closed on the primary Act 1019 of 2021 [US-ARS5-006]. (4) ND 20-day, MN 15,300, WI 1,500 and MS standard-deduction nonresident rules added from the State units.

**Language (US-OWN-006).** No multistate language rule; the payslip is in English and the pay-statement statute follows the work-location State (CA reach by *Ward*)."""

multi_prose = {
    'labour_code': 'Wage-hour law follows the place of performance (federal floor plus the more protective State/municipal overlay). Per-State minimum wage, overtime, pay frequency and method of payment are in the State annexes. California reach is decided statute by statute (G-RULING pinned below).',
    'income_tax': """Nine jurisdictions levy no wage income tax: AK, FL, NV, NH, SD, TN, TX, WA, WY (State annexes carry the row each).

**Resident working in another State.** Withholding-level rules per State (difference withholding, home-State stop, or home-State always) are the `multi.resident_out_of_state.*` facts. The resident credit for tax paid to another State operates at ASSESSMENT (`multi.resident_credit.*.level`) and must not be built as a payroll deduction.

**Reciprocity.** 30 bilateral pairs confirmed on both sides from each State's own source; partner lists are symmetric. AZ is unilateral (one-way); DC exempts every nonresident. States without reciprocity with an explicit source are emitted as `partners = none`; the remaining negatives (AL, CA, CO, ID, KS, LA, MA, NM, UT, HI, MS, NE, NY, OK, OR, RI, SC) are carried in the State annexes — none is named as a partner by any reciprocal State, so no pair is missed. Local taxes sit outside State reciprocity (MI cities, IN county, PA EIT, OH municipal/school district, MD county nonresident rate).

**Nonresident thresholds.** Day/dollar thresholds before work-State withholding starts are `multi.nonresident.*`; States with no threshold use a day/earnings ratio from day 1 (`allocation_rule`). LA is pinned: Act 382 (2025) in force from 2026-01-01, rule adopted 2026-03-20; how days 1-30 are caught up after day 31 is open. VT's 30 days is written "thirty days" in the row (number check passed by reading).

**Convenience of the employer.** NY and PA (necessity tests), DE (statutory, assessment via PIT-SCW), NE (from 2025); NJ (from 2023) and CT (from 2019) retaliatory; AR expressly not (Act 1019 of 2021). Everywhere else: physical performance.

**Federal limits.** Transport workers (motor carrier, rail, air carrier >50%, seamen) and military spouses. The Mobile Workforce bills (S. 1443, H.R. 10271) are drafts, not enacted — do not model.""",
    'social_security': """**Localization (sui_state).** Uniform four-step test (localized / base of operations / direction or control / residence), with the reciprocal coverage election as fallback. State statutory instances confirmed in the units: FL 443.1216, MD LE 8-202, ME 1043, IA 871 IAC 23.24, NV 612.080, ND, SD (DLR 90-day rule of thumb, guidance not statute, US-SDS5-020), VT, OR 657.035, AR (four-step), MS 71-5-11.

**Other-State wage-base credit (per State, from each State unit).** YES in 25 States (AK, AL, CA, CT, DE, FL, HI, KS, KY, ME, MI, MS, NC, ND, NE, NH, NV, OK, OR, RI, SC, SD, VT, WV, WY); ID conditional (only if tax was paid to the other State); NO in IA and MT. AR: the AR unit reports a credit on permanent transfer with the same employer (handbook example MO 6,000 in Q1 -> 1,000 AR-taxable in Q2), but the cited row US-ARP9V-001 does not carry that clause, so it is not emitted as a fact and sits in Open questions. Open after the State unit searched: CO, DC, LA, MD (implied only by the BEACON file field), MO, NM, UT. Not answered in the State unit: AZ, GA, IL, IN, MA, MN, NJ, NY, OH, PA, TN, TX, VA, WA, WI.

**PFML/SDI/TDI coverage.** Follows UI localization in WA, CT, ME, OR, MD, RI; DC uses its own 50%-of-work-time test and DE the primary DE worksite. Default: key the premium State to `sui_state` unless the State annex proves otherwise. Open: CA, NJ, NY, MA, CO, MN, VT, HI.""",
    'payslip_statute': 'G-RULING: *Ward v. United Airlines* (S248702) pinned with status and level. Default for every other State: the work-location State\'s statute (State units found no territorial clause in AK, CT, IA, ID, KY, ME, MO, MT, ND, NE, NM, NV, OK, OR, RI, UT, VT, WY).',
    'reporting': 'State W-2 copies and formats (EFW2 RS record or State spec) are per State annex. Registration/nexus trigger: the first wage subject to that State\'s withholding (thresholds above) or the first localized employee (UI).',
    'deductions_garnishments': 'CCPA limits are federal (annex_FED); State limits per State annex.',
    'live_legal_change': 'Sweep 2026-01-01 to 2026-11-02 (multistate scope): LA Act 382 + LAC 61:I.1923 adopted; AL 30-day safe harbor in force for 2026 [US-ALS5-003]; NE 7-day threshold + convenience from 2025; federal Mobile Workforce bills not enacted; DOL localization reminder (Spirit Airlines memo) restates UIPL 20-04. Per-State bulletin sweeps belong to the State units.',
}
multi_extra = ["""## Special populations (multistate round, US-OWN-005)
| Population | Multistate rule | register_id |
|---|---|---|
| Motor carrier drivers (2+ States) | residence State only (tax and information returns) | US-MULTIS5-001 |
| Rail employees (2+ States) | residence State only | US-MULTIS5-002 |
| Air carrier crew (2+ States) | residence State + State of more than 50% scheduled flight time | US-MULTIS5-003 |
| Seamen / vessel crew, pilots | no State withholding on seamen's wages; multi-State crew/pilots residence only | US-MULTIS5-004 |
| Military spouses | duty State does not source the spouse's wages; residence election | US-MULTIS5-005 |
| Interstate transportation workers (CA wage law) | Lab. Code 226/204 where CA is the base of operations when no majority State | US-MULTIS5-018, -019 |
| Telecommuters | income tax: physical place of work except convenience/necessity States; UI: localization (UIPL 20-04) | US-MULTIS5-013, -014, -016 |
| Athletes / entertainers | excluded from the day safe harbors (AL, WV, MT, UT, ND) | US-ALS5-003, US-MULTI-015, US-MT-P5-1-003, US-UT-P5-1-002, US-NDS5-004 |
| Agricultural workers | no multistate rule beyond federal (ID: agricultural under 1,000 not withheld) | US-ID-P5-2-002 |
| Nonresident aliens | federal (annex_FED); States apply resident/nonresident rules (ME, GA, HI: no special State rule beyond nonresident thresholds) | State annexes |
| Domestic, minors, tipped, clergy, students, statutory and government employees | no multistate-specific rule found; State annexes carry the State rule | (negative not proven) |

## Routing algorithm for the builder (from the facts above)
1. Wage-hour law: `work_location_jurisdiction` (plus CA reach rulings).
2. Work-State income-tax withholding: apply the transport/military-spouse federal limits first; then reciprocity (`residence_jurisdiction` partner of the work State with certificate on file -> no work-State withholding); then the nonresident threshold or allocation rule; then the convenience rule of the work State (NY/PA/NE/DE; NJ/CT retaliatory).
3. Resident-State withholding: `multi.resident_out_of_state.{residence}` (difference, stop, or always); resident credit is assessment-level only.
4. UI: `sui_state` by the localization test; FUTA 7,000 per employer across States; other-State wage credit per `multi.sui.other_state_wage_credit.{state}`.
5. PFML/SDI: `sui_state` unless the State coverage test differs (DC, DE).
6. Reporting: State withholding returns to every withholding State; UI wage report to `sui_state` only; W-2 boxes 15-20 two States per form; new hire to the work State or the designated State.
7. Garnishment: interstate IWO governed by the law of the principal place of employment.
"""]
build('annex_MULTI', multi_intro, multi_prose, multi_extra, os.path.join(BASE, '_research', 'CCG-annex_MULTI-research-pack.md'))
print('ok')
