# -*- coding: utf-8 -*-
"""Round 2 (QA r1 finding 41, C32): Georgia withholding-level text bound to ga.wh.rate (dated) and
assessment-level text to ga.pit.rate.flat. Idempotent. usage: python r2_ga_level_split.py <BASE>"""
import json
import os
import sys

BASE = sys.argv[1]


def patch(rel, a, b):
    p = os.path.join(BASE, rel)
    raw = open(p, encoding="utf-8", newline="").read()
    crlf = raw.count("\r\n") > raw.count("\n") / 2
    t = raw.replace("\r\n", "\n")
    if b in t:
        print(rel, "already applied")
        return
    if a not in t:
        raise SystemExit(f"{rel}: not found {a[:80]!r}")
    t = t.replace(a, b)
    open(p, "w", encoding="utf-8", newline="").write(t.replace("\n", "\r\n") if crlf else t)
    print(rel, "patched")


# m06 flat-rate table: assessment rate plus the dated withholding rate
patch("01-ccg/_build-m01-m07/build_m06.py",
      "Georgia {T('ga.pit.rate.flat')}% statutory for 2026;",
      "Georgia {T('ga.pit.rate.flat')}% statutory for 2026 (withholding {T('ga.wh.rate', on='2026-03-01')}% "
      "to 2026-05-10, {T('ga.wh.rate', on='2026-06-30')}% from 2026-05-11 {R('ga.wh.rate', on='2026-03-01')});")
# GA worked example (dated from 2026-05-11): the withholding rate, not the assessment rate
patch("01-ccg/_scratch/annex-DC-MA/build_examples_annex_DC-MA.py",
      'r_t, r = f.t("ga.pit.rate.flat", "2026-06-30")',
      'r_t, r = f.t("ga.wh.rate", "2026-06-30")  # round 2: withholding level (QA r1 C32)')
patch("01-ccg/_scratch/annex-DC-MA/build_examples_annex_DC-MA.py",
      "The rate applies from 2026-01-01; employers that kept the prior rate until 2026-05-11 follow the transition described in GA.2.",
      "The withholding rate used applies to payments from 2026-05-11; payments to 2026-05-10 were withheld at the earlier withholding rate (GA.2).")
# annex GA pack summary / fact note: the auto-tagger bound the withholding mentions to the assessment key
p = os.path.join(BASE, "01-ccg", "_build", "common", "percent_tags.json")
d = json.load(open(p, encoding="utf-8"))
rules = d.setdefault("annex_GA.md", [])
for r in [
    {"find": "withholding at [[FACT:ga.pit.rate.flat=4.99]]% from 2026-05-11",
     "replace": "withholding at [[FACT:ga.wh.rate=4.99]]% from 2026-05-11",
     "_why": "QA r1 finding 41: withholding level bound to ga.wh.rate"},
    {"find": "Withholding at [[FACT:ga.pit.rate.flat=4.99]]% from 2026-05-11",
     "replace": "Withholding at [[FACT:ga.wh.rate=4.99]]% from 2026-05-11",
     "_why": "QA r1 finding 41: withholding level bound to ga.wh.rate"},
]:
    if not any(x["find"] == r["find"] for x in rules):
        rules.append(r)
json.dump(d, open(p, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
print("percent_tags.json GA rules:", len(rules))
