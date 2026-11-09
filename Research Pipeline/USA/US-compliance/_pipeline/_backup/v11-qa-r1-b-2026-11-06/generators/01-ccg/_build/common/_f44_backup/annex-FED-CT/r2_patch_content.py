# -*- coding: utf-8 -*-
"""Round-2 (QA r1) one-off edit of content.py: equity / NRA BIK matrix cells (RQ-505/565/566 closed),
contractor sentence citing US-OWN-008 (finding 57). Idempotent: does nothing when already applied."""
import os
P = os.path.join(os.path.dirname(os.path.abspath(__file__)), "content.py")
t = open(P, encoding="utf-8", newline="").read()
R = [
    ('status, so it is a cross-layer dependency. Independent contractors (Form 1099-NEC) are out of scope.",',
     'status, so it is a cross-layer dependency. Independent contractors and Form 1099-NEC reporting are out of scope "\n'
     '    "(owner instruction of 2026-10-29) [US-OWN-008].",'),
    ('| Equity (option exercise, share vesting) | ⚠️ RESEARCH-GAP (blocking): the federal classification and withholding treatment of equity income are not in the research | ⚠️ RESEARCH-GAP (blocking): same request |',
     '| Equity (option exercise, share vesting) | {{fed.equity.withholding_treatment.resident}}; RSU FICA/FUTA timing: {{fed.equity.rsu.fica_timing}} | {{fed.equity.withholding_treatment.nonresident}} |'),
    ('| Benefits in kind | Taxable fringe benefits are wages; exclusions in FED.8 | Same; treaty exemption only where claimed on Form 8233 |',
     '| Benefits in kind | Taxable fringe benefits are wages; exclusions in FED.8 | {{fed.fit.nra.bik.treatment}} |'),
    ('| Contractor / labour-service pay | Out of scope (Form 1099-NEC, owner decision) | Out of scope |',
     '| Contractor / labour-service pay | Independent contractors and Form 1099-NEC reporting are out of scope (owner instruction of 2026-10-29) [US-OWN-008] | Same |'),
    ('"- Minors: ⚠️ RESEARCH-GAP (non-blocking): child-labour hour limits not in the research (AR.6).",',
     '"- Minors: ⚠️ RESEARCH-GAP [[GAPKEY:ar.leave.mandated_leave]] (non-blocking): child-labour hour limits not in the research (AR.6).",'),
    ("classification of equity income open at federal level (Annex FED, FED.2b)",
     "federal classification of equity income in Annex FED (FED.2b)"),
]
n = 0
for a, b in R:
    if a in t:
        t = t.replace(a, b)
        n += 1
    elif b not in t:
        raise SystemExit(f"neither old nor new text found: {a[:80]!r}")
open(P, "w", encoding="utf-8", newline="").write(t)
print("replacements applied:", n)
