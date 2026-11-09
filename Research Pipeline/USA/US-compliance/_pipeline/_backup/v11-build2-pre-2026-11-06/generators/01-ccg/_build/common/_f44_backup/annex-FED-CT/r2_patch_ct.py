# -*- coding: utf-8 -*-
"""Round 2 (orchestrator decision 2026-11-02 after agent 2 r1b): Connecticut engine method = DRS
tables (IP 2026(1), now keyed as ct.wh.table.<period>.row.<nnn>; they reproduce the IP examples
17.65 / 39.97 / 78.82); TPG-211 rules kept as reference. Recorded as a configuration decision, not a
gap. Idempotent. usage: python r2_patch_ct.py"""
import os

P = os.path.join(os.path.dirname(os.path.abspath(__file__)), "content.py")
raw = open(P, encoding="utf-8", newline="").read()
CR = chr(13) + chr(10)
crlf = CR in raw
t = raw.replace(CR, chr(10))
R = [
    ('"**Method choice (decision record).** The Department of Revenue Services permits either the TPG-211 rules or its "\n'
     '    "tables. Its worked examples are table-based, and the rules give results that differ from the tables by up to some "\n'
     '    "cents per period. The engine method is an owner decision; whichever is chosen, the per-period tables are not in the "\n'
     '    "research (blocking gap below), so the oracle examples cannot be reproduced yet.",',
     '"**Method choice (configuration decision, 2026-11-02).** The Department of Revenue Services permits either the "\n'
     '    "TPG-211 rules or its tables. The engine uses the DRS per-period withholding tables of IP 2026(1) (weekly, biweekly, "\n'
     '    "semimonthly and monthly bands, one row per wage band and CT-W4 code, listed in CT.2 with their source), because the "\n'
     '    "Department\'s worked examples are table-based and the tables reproduce them (CT.14). Wages above the table maximum of "\n'
     '    "each period are computed with the TPG-211 rules, as the tables instruct. The TPG-211 rules above are shown as the "\n'
     '    "reference method.",'),
    ('"(table method). They cannot be reproduced until the per-period tables are keyed (CT.2 gap).",',
     '"(table method), reproduced from the keyed per-period tables (CT.2).",'),
]
n = 0
for a, b in R:
    if a in t:
        t = t.replace(a, b)
        n += 1
    elif b not in t:
        raise SystemExit("not found: " + a[:90])
open(P, "w", encoding="utf-8", newline="").write(t.replace(chr(10), CR) if crlf else t)
print("applied", n)
