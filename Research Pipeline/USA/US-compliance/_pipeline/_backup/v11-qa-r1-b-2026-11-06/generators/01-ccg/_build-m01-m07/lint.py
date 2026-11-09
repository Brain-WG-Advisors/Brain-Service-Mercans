# -*- coding: utf-8 -*-
"""Lint the m01..m07 module files: tag/fact agreement (C46 simulation over ALL dated values and the
last-loaded value the checker uses), untagged distinctive fact values, C29 residual markers, C70
gap phrases, H3 coverage against CCG_TEMPLATE_QUESTIONS.md."""
import glob
import json
import os
import re
import sys

sys.path.insert(0, os.path.expanduser("~/mercans-pipeline/shared/consistency-checks"))
import consistency_checks as cc  # noqa: E402

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
facts_all, facts_last = {}, {}
for fp in glob.glob(os.path.join(BASE, "_research", "*-facts.json")):
    for f in json.load(open(fp, encoding="utf-8")).get("facts", []):
        facts_all.setdefault(f["key"], []).append(f.get("value"))
        facts_last[f["key"]] = f.get("value")
forms = {}
for k, vs in facts_all.items():
    for v in vs:
        for n, pct in cc.distinctive_forms(k, v):
            forms.setdefault((round(n, 6), pct), set()).add(k)
MARK = re.compile(r"(TODO|TBD|FIXME|XXX|\[CHECK\]|\[\?\]|VERIFY No\.|to be confirmed|to be verified|\[placeholder\])", re.I)
GAPTXT = cc_gap = re.compile(r"\b(not obtained|could not be obtained|not retrievable|could not be retrieved|was not available)\b", re.I)


def same(v, x):
    a, b = cc._num(v), cc._num(x)
    if a is not None and b is not None and not isinstance(x, bool):
        return abs(a - b) < 1e-9
    return str(v).strip() == str(x).strip()


units = [a for a in sys.argv[1:] if not a.startswith("--")] or ["m01_foundational", "m02_master_data", "m03_gross_to_net", "m04_compensation",
                         "m05_social_security", "m06_tax", "m07_deductions"]
tot = {"mismatch": 0, "unbound": 0, "marker": 0, "gaptext": 0, "lastval": 0}
for u in units:
    p = os.path.join(BASE, "01-ccg", "modules", f"{u}.md")
    t = open(p, encoding="utf-8").read()
    for i, line in enumerate(t.splitlines(), 1):
        for m in cc.TAG.finditer(line):
            k, v = m.group(1), m.group(2)
            if not any(same(v, x) for x in facts_all.get(k, [])):
                print(u, i, "TAG-MISMATCH", k, v[:60]); tot["mismatch"] += 1
            elif not same(v, facts_last.get(k)):
                tot["lastval"] += 1
                if "--v" in sys.argv:
                    print(u, i, "C46-LASTVALUE", k, v[:40], "checker compares with", str(facts_last.get(k))[:40])
        bare = cc.TAG.sub(" ", line)
        for m in cc.NUM_IN_TEXT.finditer(bare):
            n = cc._num(m.group(1))
            if n is None:
                continue
            ks = forms.get((round(n, 6), bool(m.group(2))))
            if ks:
                print(u, i, "UNBOUND", m.group(0), sorted(ks)[:3], "::", bare[max(0, m.start() - 40):m.end() + 20]); tot["unbound"] += 1
        if MARK.search(bare):
            print(u, i, "C29-MARKER", MARK.search(bare).group(0)); tot["marker"] += 1
        if GAPTXT.search(line):
            print(u, i, "C70-GAPTEXT", GAPTXT.search(line).group(0)); tot["gaptext"] += 1
    h3 = len(re.findall(r"^### ", t, re.M))
    gaps = len(re.findall(r"RESEARCH-GAP \(blocking\)", t)), len(re.findall(r"RESEARCH-GAP \(non-blocking\)", t))
    tags = len(cc.TAG.findall(t))
    print(f"{u}: H3={h3} tags={tags} gaps blocking/non-blocking={gaps} words={len(cc.TAG.sub('x', t).split())}")
print("TOTAL", tot)
