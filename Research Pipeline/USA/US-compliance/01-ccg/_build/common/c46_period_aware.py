# -*- coding: utf-8 -*-
"""Period-aware C46 for the US CCG (round 2; QA r1 fix 9).

The shared consistency_checks.c46 keeps ONE value per key (the last facts file loaded wins), so a
tag that carries the dated value of another period of the same key is reported as a mismatch, and
it reads a rate as a percentage only when the stored value is < 1 (US facts store percent). This
check uses the same deliverables / text units as the shared checker, and:
  - compares each [[FACT:key=value]] with EVERY dated value of the key (key + effective_from);
  - reports tags whose value is valid only outside the build year (needs a period label in text);
  - finds unbound values with the shared distinctiveness rule, plus percent-aware forms for facts
    stored in percent (unit_of_measure percent), after stripping [[FACT:]] AND [[GAP:]] tags.

usage: python c46_period_aware.py [--docx <file>] [--json out.json]
"""
import glob
import importlib.util
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
SHARED = os.path.expanduser("~/mercans-pipeline/shared/consistency-checks/consistency_checks.py")
spec = importlib.util.spec_from_file_location("cc_shared", SHARED)
CCS = importlib.util.module_from_spec(spec)
spec.loader.exec_module(CCS)

YEAR = json.load(open(os.path.join(BASE, "_pipeline", "build-manifest.json"), encoding="utf-8"))["year"]
Y0, Y1 = f"{YEAR}-01-01", f"{YEAR}-12-31"

facts = {}
units = {}
for fp in glob.glob(os.path.join(BASE, "_research", "*-facts.json")):
    for f in json.load(open(fp, encoding="utf-8")).get("facts", []):
        facts.setdefault(f["key"], []).append(f)
        if f.get("unit_of_measure"):
            units[f["key"]] = f["unit_of_measure"]


def same(a, b):
    x, y = CCS._num(a), CCS._num(b)
    if x is not None and y is not None:
        return abs(x - y) < 1e-9
    return str(a).strip() == str(b).strip()


def in_year(f):
    return (f.get("effective_from") or "0000") <= Y1 and (f.get("effective_to") or "9999") >= Y0


forms = {}
for k, es in facts.items():
    for f in es:
        v = f.get("value")
        for n, pct in CCS.distinctive_forms(k, v):
            forms.setdefault((round(n, 6), pct), set()).add(k)
        # percent-aware: rate stored in percent -> written "n %"
        if units.get(k) == "percent" and isinstance(v, (int, float)) and not isinstance(v, bool):
            n = float(v)
            if n and (CCS._sig(n) >= 3 or n != int(n)):
                forms.setdefault((round(n, 6), True), set()).add(k)

TAG = CCS.TAG
GAPTAG = re.compile(r"\[\[GAP:[^\]]*\]\]")


def run(paths):
    tags, missing, mismatch, offyear, unbound = 0, [], [], [], []
    for p in paths:
        tus = CCS.text_units(p)
        rows = {}
        for loc, t in tus:
            mm = re.match(r"(table \d+ r\d+)c\d+", loc)
            if mm:
                rows.setdefault(mm.group(1), []).append(t)
        for loc, t in tus:
            mm = re.match(r"(table \d+ r\d+)c\d+", loc)
            row_text = " | ".join(rows[mm.group(1)]) if mm else t
            for m in TAG.finditer(t):
                tags += 1
                k, v = m.group(1), m.group(2)
                if k not in facts:
                    missing.append({"where": loc, "key": k})
                    continue
                hit = [f for f in facts[k] if same(v, f.get("value"))]
                if not hit:
                    mismatch.append({"where": loc, "key": k, "written": v,
                                     "facts": sorted({str(f.get('value')) + ' @' + str(f.get('effective_from')) for f in facts[k]})[:4]})
                    continue
                if not any(in_year(f) for f in hit):
                    # the period label may sit in another cell of the row (Effective / Valid from
                    # columns) or elsewhere in the paragraph
                    ctx = TAG.sub(lambda x: x.group(2), row_text)
                    labelled = bool(re.search(r"\b(20(?:1\d|2[0-57-9]|[3-9]\d))\b|from \d{4}-|until|next year|prior|previous|history", ctx))
                    offyear.append({"where": loc, "key": k, "written": v,
                                    "periods": sorted({f"{f.get('effective_from')}..{f.get('effective_to')}" for f in hit}),
                                    "period_labelled_in_context": labelled})
            bare = GAPTAG.sub(" ", TAG.sub(" ", t))
            for m in CCS.NUM_IN_TEXT.finditer(bare):
                n = CCS._num(m.group(1))
                if n is None:
                    continue
                ks = forms.get((round(n, 6), bool(m.group(2))))
                if ks:
                    unbound.append({"where": loc, "text": m.group(0).strip(), "keys": sorted(ks)[:3],
                                    "context": bare[max(0, m.start() - 60): m.end() + 40]})
    return {"tags": tags, "keys_missing": len(missing), "mismatches_period_aware": len(mismatch),
            "tags_value_outside_build_year": len(offyear),
            "outside_year_unlabelled": len([o for o in offyear if not o["period_labelled_in_context"]]),
            "unbound_period_and_percent_aware": len(unbound),
            "binding": round(tags / (tags + len(unbound)), 4) if tags else 0,
            "detail": {"missing": missing, "mismatch": mismatch, "outside_year": offyear, "unbound": unbound}}


if __name__ == "__main__":
    if "--docx" in sys.argv:
        paths = [sys.argv[sys.argv.index("--docx") + 1]]
    else:
        paths = [p for p in CCS.deliverables(BASE) if "01-ccg" in p]
    r = run(paths)
    if "--json" in sys.argv:
        json.dump(r, open(sys.argv[sys.argv.index("--json") + 1], "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    sys.stdout.reconfigure(encoding="utf-8")
    print(json.dumps({k: v for k, v in r.items() if k != "detail"}, indent=1))
    for kind in ("missing", "mismatch"):
        for x in r["detail"][kind][:40]:
            print(kind.upper(), json.dumps(x, ensure_ascii=False)[:300])
    for x in r["detail"]["outside_year"]:
        if not x["period_labelled_in_context"]:
            print("OUTSIDE-YEAR-UNLABELLED", json.dumps(x, ensure_ascii=False)[:300])
    for x in r["detail"]["unbound"][:200]:
        print("UNBOUND", json.dumps(x, ensure_ascii=False)[:260])
