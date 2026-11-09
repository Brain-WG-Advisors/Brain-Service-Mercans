# -*- coding: utf-8 -*-
"""Append the annex DC..MA stanza to _pipeline/CCG-build-log.md (re-read before writing)."""
import json, os, re, sys, collections

BASE = sys.argv[1]
JURS = "DC DE FL GA HI IA ID IL IN KS KY LA MA".split()
SCR = os.path.dirname(os.path.abspath(__file__))
LOG = os.path.join(BASE, "_pipeline", "CCG-build-log.md")
added = json.load(open(os.path.join(SCR, "requests_added.json")))
ex = json.load(open(os.path.join(SCR, "examples_results.json")))
ovr = json.load(open(os.path.join(SCR, "overrides_applied.json"), encoding="utf-8"))
c46 = open(os.path.join(SCR, "c46_local.txt"), encoding="utf-8").read()

L = []
L.append("")
L.append("## Units annex_DC, annex_DE, annex_FL, annex_GA, annex_HI, annex_IA, annex_ID, annex_IL, annex_IN, annex_KS, annex_KY, annex_LA, annex_MA (builder 4 of 6), round 1")
L.append("")
L.append("Artifact: CCG | Country: US | Round: 1 | Built: 2026-11-02")
L.append("Manifest: _pipeline/build-manifest.json (USD, minor units 2, rounding 0.01/0.01, year 2026, overall tier T4; state_income_tax T4, local_income_tax T4; languages en, payslip English). Mandate: 00-official-sources/MANDATE.md sealed 2026-11-02 (contractors / 1099-NEC out of scope, US-OWN-008).")
L.append("Brief: _prompts/ccg-build-brief.md. Inputs per unit: _research/CCG-annex_{JUR}-research-pack.md and _research/CCG-annex_{JUR}-facts.json (validated by Synthesis C/D). No fetching; no edit of facts, register, MANDATE or manifest.")
L.append("")
L.append("### Precedent inspection (L1)")
L.append("- `shared/REFERENCE_CCG_Bulgaria.docx` opened with python-docx (toolkit `inspect_docx.py`): 1 section, portrait 8.5 x 11 in, 310 headings (H1 14 = Version Control + 13 modules, H2 84, H3 210, H4 2), 3 tables, 18,276 words, C29 scan clean. The precedent has no jurisdiction annexes; annex structure below is this build's own (H1 per annex, H2 per domain, parameter tables), to be placed after the 13 modules at assembly.")
L.append("- `shared/CCG_TEMPLATE_QUESTIONS.md` governs m01..m13 (H3 = template question). Annexes are not template modules, so no H3-per-question rule applies; the domain order follows the research-pack sections (1..13 + worked examples, special populations, language).")
L.append("")
L.append("### Outputs")
L.append("- `01-ccg/modules/annex_{DC,DE,FL,GA,HI,IA,ID,IL,IN,KS,KY,LA,MA}.md` (13 files, same folder as annex_AK..CT / FED / MULTI).")
L.append("- PATH NOTE for assembly: the MD..WY builders wrote to `01-ccg/annexes/`; annexes are therefore split across `01-ccg/modules/` (AK..MA, FED, MULTI) and `01-ccg/annexes/` (MD..WY). The DOCX assembly must read both or the orchestrator must pick one folder.")
L.append("- Build scripts (reproducible, scratch): `01-ccg/_scratch/annex-DC-MA/build_annexes.py` (annex generator), `overrides.py` (text overrides and internal-wording cleaning, all logged), `build_examples_annex_DC-MA.py` (worked examples, computed from facts and asserted against the oracle facts), `check_c46.py` (local C46 emulation), `append_requests.py`, `write_log.py`. Rebuild: `python build_examples_annex_DC-MA.py <BASE>` then `python build_annexes.py <BASE> DC,DE,FL,GA,HI,IA,ID,IL,IN,KS,KY,LA,MA`.")
L.append("")
L.append("### Construction rules applied")
L.append("- Every fact object of each annex facts file is written once as a parameter row (key, `[[FACT:key=value]]`, period in force, register_id + authority + tier + verification method + confidence, note). Multi-period keys get one row per period.")
L.append("- Notes are the fact record's own note (bound to that row's key and register_id). Notes that were truncated copies of register text (\"Derivation recorded in register row ...\", 61 notes) are replaced by a pointer to the register row instead of the truncated text.")
L.append("- Pack narrative (non-fact lines) is carried with its register citations; distinctive numbers equal to a USD / percent / ratio fact of the same annex are tagged automatically (same-section key preferred). Pipeline-internal wording (Python, Synthesis, MANDATE, Q-ids, OQ-ids, legacy, tier-B / MANUAL / gated, browser pass, builder, engine) is rewritten by the CLEAN rules in `overrides.py` (C47).")
L.append("- Each `unresolved[]` item of a facts file is a `⚠️ RESEARCH-GAP` line in place (section chosen by key), with blocking / non-blocking and what would close it, plus one research request (below). Blocking items are not filled.")
L.append("- Brief traps written as explicit configuration rules: KS withholding uses KW-100 table parameters, not the statutory brackets (KS.2); GA (KS... no) GA.2, IA.2, HI.2, DC.2 tips/overtime deductions at assessment only, withholding unchanged; DC 2026 withholding method unpublished = blocking gap `dc.wh.method` (DC.2); MA PFML 2026 per DFML table, swap from 2027-01-01 (MA.3).")
L.append("- Layer classification line per annex taken from the manifest tier census: FL T1; DE, KY T4; DC, GA, HI, IA, ID, IL, IN, KS, LA, MA T3.")
L.append("")
L.append("### Fact bindings (summary; full section -> key -> register_id table below)")
L.append("| Unit | facts | distinct keys | own keys tagged | tags in file | cross-unit keys cited | RESEARCH-GAP blocking / non-blocking |")
L.append("|---|---|---|---|---|---|---|")
tot = collections.Counter()
bind_rows = []
for j in JURS:
    r = json.load(open(os.path.join(SCR, f"report_{j}.json"), encoding="utf-8"))
    t = open(os.path.join(BASE, "01-ccg", "modules", f"annex_{j}.md"), encoding="utf-8").read()
    tags = re.findall(r"\[\[FACT:([a-z0-9_.]+)=", t)
    keys = set(r["keys"])
    cross = sorted(set(tags) - keys)
    b = sum(1 for g in r["gaps"] if g.get("blocking"))
    nb = len(r["gaps"]) - b + (1 if j == "IL" else 0)
    L.append(f"| annex_{j} | {r['facts']} | {len(keys)} | {len(keys & set(tags))} | {len(tags)} | {', '.join('`'+c+'`' for c in cross) or '-'} | {b} / {nb} |")
    tot.update(f=r["facts"], k=len(keys), kt=len(keys & set(tags)), t=len(tags), b=b, nb=nb)
    seen = set()
    for sec, key, rid, how in r["bindings"]:
        if how != "value" or (sec, key, rid) in seen:
            continue
        seen.add((sec, key, rid))
        bind_rows.append((j, sec, key, rid))
L.append(f"| **total** | {tot['f']} | {tot['k']} | {tot['kt']} | {tot['t']} | | {tot['b']} / {tot['nb']} |")
L.append("")
L.append("Untaggable value (carried verbatim in the row with its key, no tag): `ia.wh.method` (its value contains square brackets, `[US-IAS5-015]`, which would break the `[[FACT:]]` tag syntax). Cross-unit keys are cited with the exact value of the FED annex / WTC facts files.")
L.append("")
L.append("### Worked examples (C38): computed from facts, asserted against the published oracle facts")
L.append("| Example | Computed | Oracle | Result |")
L.append("|---|---|---|---|")
for j, name, comp, orc, ok in ex:
    L.append(f"| {name} | {comp} | {orc} | {'match' if ok else 'NO MATCH -> RESEARCH-GAP il.oracle.il700t.example1.inputs'} |")
L.append("No state oracle example in the facts for DC, FL, KS, MA (section 14 says so). ID-2 (published 20) not reproduced: its zero bracket matches neither ID table (open item `id.wh.example_threshold_discrepancy`). KY-2 per-period rounding (sheet prints 47) open (`ky.wh.rounding.tax`).")
L.append("")
L.append("### Text overrides applied (each binds a number to an existing key or removes an unkeyed number)")
for j, a, b_, n in ovr:
    L.append(f"- {j}: `{a[:110]}` -> `{b_[:110]}` (x{n})")
L.append("")
L.append("### Local C46 emulation on the annex markdown (the real check runs on the assembled DOCX)")
L.append("- Tags whose key is not in any facts file: 0. Tags disagreeing with every period of their key: 0.")
L.append("- 53 tags carry the value of a NON-LAST period of a multi-period key (e.g. `dc.minwage.hourly` 17.95 to 2026-06-30 and 18.40 from 2026-07-01). `consistency_checks.c46` keeps only the last value per key (`facts[f['key']] = f.get('value')`), so it will report these as mismatches although each tag equals the fact of its own period. Checker limitation, not a content defect: needs either a period-aware C46 or period-qualified keys in the facts (owner of shared/ decides).")
L.append("- 17 residual untagged numbers that coincide with a fact value of ANOTHER unit (legal citations or example arithmetic, no key of their own):")
for ln in c46.splitlines():
    if ln.startswith("== "):
        cur = ln.split(":")[0][3:]
    if "unbound" in ln:
        L.append(f"  - annex_{cur}{ln.strip()[7:]}")
L.append("  Reasons: DC 214 = D.C. Act 26-214 citation; DE 1,750.00 = bracket-5 slice of example DE-1; GA 347 = HB 347 citation, 276 = withholding-table band in the guide example; HI 1.21 = TDI statutory multiplier (no key); IA 871 = 871 IAC citation; ID 20.38 = unrounded published example; KS 269 = SB 269 citation, 512 = KS period threshold in a note; KY 367 = KRS 367 citation; MA 4.58 = M-4 semimonthly per-person amount, 1.21 / 12.65 = schedule-table cells, 2.25 = meal deduction cap. None is a claim about the other unit's fact.")
L.append("")
L.append("### Research requests appended to `_research/CCG-research-request.json`")
L.append(f"- {len(added)} items, {added[0]}..{added[-1]} (one per RESEARCH-GAP marker: 124 facts-file `unresolved[]` items + 1 new: `il.oracle.il700t.example1.inputs`). File re-read immediately before writing; existing items untouched; validated with `shared/schemas/validate_contract.py research-request` -> PASS.")
L.append("- Blocking (15): " + ", ".join(sorted(f"`{g['key']}`" for j in JURS for g in json.load(open(os.path.join(SCR, f'report_{j}.json'), encoding='utf-8'))['gaps'] if g.get('blocking'))) + ".")
L.append("")
L.append("### Deviations from the agent's stated constants")
L.append("- Annex layout (H1 annex, H2 domain, parameter tables) is not in the Bulgaria precedent, which has no annexes; it is a build decision, reversible at assembly.")
L.append("- Output folder `01-ccg/modules/` (brief: 'one output file per unit under 01-ccg/'); see PATH NOTE.")
L.append("- `[[FACT:]]` tags on bool and string facts are written with the exact facts value (string comparison in C46).")
L.append("")
L.append("### Open items")
L.append(f"- {tot['b']} blocking RESEARCH-GAP markers: the annexes DC, DE, FL, GA, HI, ID, IL, KY, LA, MA cannot close until they are answered (IA, IN, KS have no blocking gap).")
L.append(f"- {tot['nb']} non-blocking markers ship as named limitations (each with what would close it, in place and in the research request).")
L.append("- C29: no residual marker other than the RESEARCH-GAP lines (lint run on the 13 files: 0 hits for placeholder/TODO/TBD/FIXME/XXX/[CHECK]/[?]/VERIFY No./to be confirmed/to be verified).")
L.append("")
L.append("### Accuracy")
L.append("About 85%. Every value is an A.1/A.2 register-backed fact (some at medium confidence) and the 13 computable oracle examples reproduce the published results except IL-700-T example 1. The gap is the 15 blocking items (DC 2026 withholding method and the permanent FY2027 act; DE W-4 2020+ mapping; FL 401(k) deferrals in the UI base; GA TY2026 W-2 RS layout and 2027 rate trigger; HI 2027 withholding tables; ID W-4 2026 edition; IL Chicago and Cook County paid leave; KY local occupational-tax census; LA mobile-workforce catch-up and IRC conformity; MA W-2 due date and IRC conformity) and 110 non-blocking items, mostly file layouts behind employer logins and statute texts not read. They are closed by the authorities' own publications listed per request, not by more secondary research.")
L.append("")
L.append("### Full binding table (section -> key -> register_id)")
L.append("| Location | key | register_id |")
L.append("|---|---|---|")
for j, sec, key, rid in bind_rows:
    L.append(f"| 01-ccg/modules/annex_{j}.md {sec} | `{key}` | {rid} |")
L.append("")

text = "\n".join(L)
text = text.replace("GA (KS... no) GA.2", "GA.2")
cur = open(LOG, encoding="utf-8").read() if os.path.exists(LOG) else "# CCG build log\n"
if "## Units annex_DC, annex_DE" in cur:
    print("stanza already present; not appended")
else:
    open(LOG, "w", encoding="utf-8").write(cur.rstrip("\n") + "\n" + text)
    print("appended", len(L), "lines")
