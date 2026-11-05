# -*- coding: utf-8 -*-
# Exact text overrides applied after generation. Each one either binds a number to an
# existing facts key (cross-unit keys from the FED annex / WTC facts) or removes an
# unkeyed number that is not needed for the rule. Logged in CCG-build-log.md.
GLOBAL = [
    ("401(k), 125, HSA", "401(k), s.125, HSA"),
    ("401(k)/125/HSA", "401(k)/s.125/HSA"),
    ("exclude 125 premiums", "exclude s.125 premiums"),
    ("HSA/125/transit", "HSA/s.125/transit"),
    ("(125/deferred comp)", "(s.125/deferred comp)"),
    ("IRC 225 overtime", "IRC s.225 overtime"),
    ("(HSA, 125)", "(HSA, s.125)"),
    ("of 125, 401(k)", "of s.125, 401(k)"),
    ("401(k)/403(b), 125, HSA", "401(k)/403(b), s.125, HSA"),
]
PER = {
    "DE": [(" (Withholding unit 302-577-8779)", " (Withholding unit)")],
    "FL": [("still prints 6.15 (stale; overridden)", "still prints a stale pre-amendment amount (overridden)"),
           ("Capped at the 2003 FLSA tip credit: 5.15 - 2.13 = ",
            "Capped at the 2003 FLSA tip credit (2003 federal minimum wage less the federal tipped cash wage [[FACT:fed.tipped.cash_wage.hourly=2.13]]) = ")],
    "GA": [("the federal 7.25 applies", "the federal [[FACT:fed.minwage.hourly=7.25]] applies"),
           ("CCPA floor 30 x 7.25 = 217.50 binds [US-FED-011]: use 217.50",
            "CCPA floor 30 x [[FACT:fed.minwage.hourly=7.25]] = [[FACT:fed.ccpa.protected_weekly=217.50]] binds [US-FED-011]: use [[FACT:fed.ccpa.protected_weekly=217.50]]"),
           ("federal 2.13", "federal [[FACT:fed.tipped.cash_wage.hourly=2.13]]")],
    "HI": [("continues to 8.25/9/10/11% above", "continues to higher rates above")],
    "IA": [("(cash wage 4.35 derived on [[FACT:ia.minwage.hourly=7.25]])",
            "(cash wage derived as the minimum wage [[FACT:ia.minwage.hourly=7.25]] less the 40% credit)")],
    "IN": [("PIT statutory step 2.95 -> 2.90", "PIT statutory step [[FACT:in.pit.rate=2.95]]% -> [[FACT:in.pit.rate=2.9]]%")],
    "KY": [("sheet shows 47 for 47.98", "sheet shows 47 for [[FACT:ky.oracle.biweekly_1500.result=47.98]]"),
           ("/26 = 47.98, sheet shows 47", "/26 = [[FACT:ky.oracle.biweekly_1500.result=47.98]], sheet shows 47")],
    "LA": [("(FLSA 7.25)", "(FLSA [[FACT:fed.minwage.hourly=7.25]])"),
           ("FLSA 7.25 for covered", "FLSA [[FACT:fed.minwage.hourly=7.25]] for covered"),
           (" [[FACT:la.wh.std_deduction.single=12,875]]/12,500 = 1.03 (2025 base secondary source only).", "")],
    "MA": [("12.65, 14.37, 16.33", "12.65, [[FACT:ma.sui.employer.rate.max=14.37]], 16.33")],
}

# Regex cleaning of pipeline-internal wording (C47), applied to narrative, notes and gap
# text (never inside a [[FACT:]] tag).
CLEAN = [
    (r"\s*\((re-derived|reproduced) in Python[^)]*\)", ""),
    (r"\s*\bre-derived in Python\b( to the cent)?", r" re-derived\1"),
    (r"\s*Reproduced in Python\.", ""),
    (r",\s*Python\)", ")"),
    (r"\s*\(Python\)", ""),
    (r"\s*\((?:\d+ values )?re-derived in Python\)", ""),
    (r"\s*\((Q\d+|[A-Z]{2}-OQ-\d+)\)", ""),
    (r"\s*\(rounding unexplained, Q\d+\)", " (rounding unexplained)"),
    (r",\s*Q\d+\)", ")"),
    (r"\s*\b[A-Z]{2}-OQ-\d+\b", ""),
    (r"\blegacy row ", "row "),
    (r"\[legacy (US-[A-Z0-9-]+)\]", r"[\1]"),
    (r",\s*legacy (US-[A-Z0-9-]+)\)", r", \1)"),
    (r"(US-[A-Z0-9-]+) legacy\b", r"\1"),
    (r"(US-[A-Z0-9-]+) legacy;", r"\1;"),
    (r";\s*mandate US-MQ-\d+\]", "]"),
    (r"\s*per MANDATE\]", "]"),
    (r"\s*\(builder reads the chart\)", " (the full county chart is the configuration source)"),
    (r"\s*\(browser pass(, US exit)?\)", ""),
    (r"\s*via (the orchestrator )?browser pass", ""),
    (r"Owner/builder decision", "Owner decision"),
    (r"DECISION \(brief trap\):", "Decision:"),
    (r"(?<!the )\bengine must\b", "the payroll calculation must"), (r"\bthe engine must\b", "the payroll calculation must"),
    (r"\s*\((\d{2})%; ([^)]*)\)", r" (\2)"),
    (r"\s*\((\d{2})%\)", ""),
    (r"Not researched \(\d+%\)\.", "Not researched."),
    (r"\(UI \+ COVID = effective in every band\)", "(UI + COVID = effective in every band)"),
]
PER.setdefault("IA", [])
PER["IA"] += [
    ("(correction: not whole dollar as US-IA-001 and the MANDATE currency block say)", "(not whole dollar)"),
    (" Supersedes the rounding clause of US-IA-001 and the MANDATE currency block listing IA as whole-dollar", " Supersedes the whole-dollar rounding clause of US-IA-001"),
]
PER["IA"] += [
    (" (S5A-MERGE note on US-IA-001)", ""),
    ("RESEARCH-GAP: US-IA-001 and the MANDATE currency block say whole-dollar; 2026 formula/tables say nearest cent.",
     "RESEARCH-GAP: an older register row (US-IA-001) states whole-dollar rounding; the 2026 formula and tables say nearest cent."),
    ("would close it: Synthesis supersedes the rounding clause of US-IA-001 by US-IAS5-005/-015 (done in S5A note); optionally IDR 2025 formula PDF. Scaffolder to amend the MANDATE currency block (US-MQ-01).)",
     "would close it: the Iowa Department of Revenue 2025 withholding formula, needed only for periods before 2026.)"),
]
CLEAN += [
    (r"Statute row is legacy (US-[A-Z0-9-]+)", r"Statute row \1"),
    (r"\(legacy (US-[A-Z0-9-]+)\)", r"(\1)"),
]

CLEAN += [
    (r"\(tier-B lead\)", "(secondary source)"),
    (r"\btier-B lead\b", "a secondary source"),
    (r"\btier-B MANUAL row\b", "secondary-source row"),
    (r"\(tier-B detail only, (US-[A-Z0-9-]+) MANUAL\)", r"(secondary-source detail only, \1)"),
    (r"\brests on tier-B \((US-[A-Z0-9-]+) MANUAL\)", r"rests on a secondary source (\1)"),
    (r"\(tier-B error\)", "(secondary-source error)"),
    (r"\(tier B\)", "(secondary source)"),
    (r"\btier-B only\b", "secondary source only"),
    (r"\(tier-B (\d)", r"(secondary source: \1"),
    (r"effective date tier-B ", "effective date per a secondary source "),
    (r"\bnot on an A-tier source\b", "not on a primary source"),
    (r"\bremains an open MANUAL item from P7\b", "remains an open item"),
    (r"(US-[A-Z0-9-]+) MANUAL\b", r"\1"),
    (r"\s*\(gated\)", " (behind the employer login)"),
    (r"\bgated \(403\)", "not accessible (HTTP 403)"),
    (r"\(2003, A\.3\)", "(2003, secondary source)"),
]

# Configuration rules stated explicitly for the traps named in the CCG build brief.
# Text only; every concept points at its facts key.
EXTRA = {
    ("KS", "2"): ["Configuration rule: withholding is computed with the KW-100 table parameters (`ks.wh.allowance.*`, `ks.wh.table.*`), whose bands already contain the standard deduction as a zero band. The statutory brackets, exemptions and standard deductions (`ks.pit.*`) are assessment parameters and must not be applied directly to wages in the withholding calculation."],
    ("GA", "2"): ["Configuration rule: the HB 463 overtime and tip subtractions (`ga.pit.overtime_subtraction.max`, `ga.pit.tip_subtraction.max`) operate at assessment only. They do not reduce withholding; payroll reports them on the W-2 only."],
    ("IA", "2"): ["Configuration rule: the federal tips and overtime deductions are conformed at assessment only (`ia.pit.obbba`). There is no withholding allowance for them; the withholding formula is unchanged."],
    ("HI", "2"): ["Configuration rule: Hawaii conforms to the federal tips deduction at assessment only and does not conform to the overtime deduction (`hi.pit.ot_deduction.conformed`). Neither changes withholding."],
    ("DC", "2"): ["Configuration rule: the federal tips and overtime deductions are allowed as DC deductions from tax year 2026 at assessment only (`dc.pit.obbba_deductions`). Withholding is not changed for them."],
    ("MA", "3"): ["Configuration rule: 2026 payroll applies the DFML 2026 contribution table; the Chapter 101 family/medical swap applies from 2027-01-01 (`ma.pfml.split.decision`). The employee and employer totals are the same before and after the swap."],
}
CLEAN += [
    (r"\btier-B MANUAL (US-[A-Z0-9-]+): not facts", r"a secondary source (\1)"),
    (r"\btier-B MANUAL (US-[A-Z0-9-]+)", r"a secondary source (\1)"),
    (r", tier-B\)", ", per a secondary source)"),
    (r"\(tier-B: ", "(secondary source: "),
    (r"\bper tier-B\b", "per a secondary source"),
    (r"\btier-B says\b", "a secondary source says"),
    (r"\bfrom tier B\b", "from a secondary source"),
    (r"\btier-B\b", "a secondary source"),
    (r"\btier B\b", "a secondary source"),
]
PER["HI"] += [
    ("would close it: Final merge: alias row for HRS 387-6(c) with S5-pattern id.)",
     "would close it: a legal-basis register row that cites HRS 387-6(c) directly at high confidence.)"),
]
PER["GA"] += [
    ("; derived projection 4.865% / 30,750 / 15,375 / 5,125 is not a fact.", "; no 2027 value is modelled until it is published."),
    (" 2026 rate range not on a primary source (secondary source: 0.04-8.10%): not a fact.", " The 2026 rate range is not on a primary source and is not modelled."),
    ("; enacted version and sunset unconfirmed - not a fact.", "; enacted version and sunset unconfirmed, not modelled."),
    ("HB 463 conditional step schedule: rate -0.125/yr from 2027 to 3.99%; std deduction +750/+375 to 36,000/18,000; dependent +125 to 6,000. If no trigger holds, 2027 = 4.865%, 30,750/15,375, 5,125 (derived projection - NOT facts until OPB 2026-12-01 and the 2027 DOR guide).",
     "HB 463 sets a conditional step schedule for the rate, standard deduction and dependent allowance from 2027; no 2027 value is modelled until the OPB determination of 2026-12-01 and the 2027 DOR guide are published."),
]
PER.setdefault("KS", [])
PER["KS"] += [(" 2027 projection ~15,700 NOT a fact.", " No 2027 value is modelled.")]
PER["DE"] += [(" Separate DD/RSPEC payable line.", " Separate payable line.")]
PER["FL"] += [(" (DD/RSPEC scope item)", ""), (" (Stage 3 / RSPEC)", "")]
CLEAN += [
    (r"\s*read with US VPN", ""),
    (r";\s*parallel fan-out", ""),
    (r"\s*\(US exit\)", ""),
]
