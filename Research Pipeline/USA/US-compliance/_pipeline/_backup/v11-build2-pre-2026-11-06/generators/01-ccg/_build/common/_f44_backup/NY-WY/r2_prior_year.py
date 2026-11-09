# -*- coding: utf-8 -*-
"""Round 2 (QA r1 finding 49 / C41): prior-year values (moved to _history by agent 2) out of the
NY-WY narrative sources. Idempotent. usage: python r2_prior_year.py"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
EDITS = {
    "RI.md": [("| 2025-01-01 | {{ri.minwage.hourly@2025-01-01}} USD |\n", "")],
    "WY.md": [("| 2025 | {{wy.sui.wage_base@2025-01-01}} USD |\n", "")],
    "OR.md": [(" USD (2025: {{or.sui.wage_base@2025-01-01}} USD);", " USD;")],
    "VT.md": [(" USD for 2026 ({{vt.sui.wage_base@2025-01-01}} USD in 2025), indexed", " USD for 2026, indexed"),
              ("The step from the 2025 base of {{vt.sui.wage_base@2025-01-01}} USD to the 2026 base of "
               "{{vt.sui.wage_base@2026-01-01}} USD cannot be re-derived",
               "The 2026 base of {{vt.sui.wage_base@2026-01-01}} USD cannot be re-derived from the prior-year base")],
}
for f, pairs in EDITS.items():
    p = os.path.join(HERE, "src", f)
    t = open(p, encoding="utf-8", newline="").read()
    crlf = "\r\n" in t
    t = t.replace("\r\n", "\n")
    for a, b in pairs:
        if a in t:
            t = t.replace(a, b)
            print(f, "edited")
        elif b and b in t:
            print(f, "already applied")
        elif not b:
            print(f, "already applied (row removed)")
        else:
            raise SystemExit(f"{f}: text not found: {a[:70]!r}")
    if crlf:
        t = t.replace("\n", "\r\n")
    open(p, "w", encoding="utf-8", newline="").write(t)
