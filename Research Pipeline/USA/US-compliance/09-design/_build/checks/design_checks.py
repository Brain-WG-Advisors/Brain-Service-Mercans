# -*- coding: utf-8 -*-
"""Self-checks of the US Regulation Design: C29 (hard markers, X-run), WORD/PATH, NOTES, FRAC/PCT/UNIT, C46 period-aware
(tags equal to a dated fact, value of another period labelled, no unbound value), gap markers against gaps.json and the
request file, C30. usage: python design_checks.py [--json out]   exit 1 on any hit."""
import glob
import importlib.util
import json
import os
import re
import sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(HERE, ".."))
import design_common as C  # noqa: E402

ccg_common = os.path.join(BASE, "01-ccg", "_build", "common", "c46_period_aware.py")
spec = importlib.util.spec_from_file_location("c46pa", ccg_common)
PA = importlib.util.module_from_spec(spec)
spec.loader.exec_module(PA)

path = glob.glob(os.path.join(BASE, "09-design", "US_Regulation_Design_v*.md"))[0]
text = open(path, encoding="utf-8").read()
lines = text.splitlines()
ANY = C.ANYTAG
TAG = re.compile(r"\[\[FACT:([A-Za-z0-9_.]+)=([^\]]*)\]\]")
URL = re.compile(r"https?://\S+")
PCT_TOK = re.compile(r"(?<![\d.,\w])(\d+(?:\.\d+)?)\s?%")
FRAC_TOK = re.compile(r"(?<![\d.,\w])(0\.\d{3,})(?![\d%\w])")
UNIT_RX = {"days": r"^\s?days?\b", "percent": r"^\s?%", "%": r"^\s?%", "hours": r"^\s?hours?\b", "weeks": r"^\s?weeks?\b",
           "months": r"^\s?months?\b", "employees": r"^\s?employees?\b"}
NOTES = re.compile(r"\bR\d 20\d\d|effective_from|local copy|script shell|journal|orchestrator|agent 2|triage|precheck|"
                   r"(?:returned|HTTP)[^.]{0,40}\bbytes\b", re.I)
XRUN = re.compile(r"X{3,}")
rep = dict(C29=[], WORD=[], PATH=[], NOTES=[], FRAC=[], PCT=[], UNIT=[], C30=[], GAP=[], file=os.path.basename(path), lines=len(lines))


def same(a, b):
    return PA.same(a, b)


for i, ln in enumerate(lines, 1):
    bare = ANY.sub(" ", ln)
    hh = C.hard_hits(bare)
    if hh:
        rep["C29"].append((i, hh[0]))
    if XRUN.search(bare):
        rep["C29"].append((i, "X-run"))
    m = C.PIPELINE_WORDS.search(bare)
    if m:
        rep["WORD"].append((i, m.group(0)))
    pm = C.PATH_RX.search(bare)
    if pm:
        rep["PATH"].append((i, pm.group(0)))
    nm = NOTES.search(bare)
    if nm:
        rep["NOTES"].append((i, nm.group(0)))
    plain = URL.sub(" ", bare)
    for mm in PCT_TOK.finditer(plain):
        rep["PCT"].append((i, mm.group(0)))
    for mm in FRAC_TOK.finditer(plain):
        rep["FRAC"].append((i, mm.group(0)))
    for t in TAG.finditer(ln):
        k, v = t.group(1), t.group(2)
        hit = [f for f in C.FACTS.get(k, []) if same(v, f.get("value"))]
        if not hit:
            continue
        if all(C.REG.get(f["register_id"], {}).get("tier") in ("B", "C") or C.REG.get(f["register_id"], {}).get("status") == "MANUAL"
               for f in hit) and re.search(r"\d", v):
            rep["C30"].append((i, k))
        f0 = hit[0]
        if isinstance(f0.get("value"), (int, float)) and not isinstance(f0.get("value"), bool) and f0.get("unit_of_measure"):
            rx = UNIT_RX.get(str(f0["unit_of_measure"]).lower())
            if rx and not re.search(rx, ln[t.end():t.end() + 20], re.I):
                rep["UNIT"].append((i, k))

# gaps: every marker in gaps.json with sources and date; every DESIGN id in the request file
gj = {x["id"]: x for x in json.load(open(os.path.join(C.RESEARCH, "gaps.json"), encoding="utf-8"))["gaps"]}
req = {"DESIGN-" + r["id"] for r in json.load(open(os.path.join(C.RESEARCH, "DESIGN-research-request.json"), encoding="utf-8"))["requests"]}
used = set(re.findall(r"\[\[GAP:\s*([A-Za-z0-9_.-]+)\s*\]\]", text))
for g in sorted(used):
    if g not in gj:
        rep["GAP"].append((g, "not in gaps.json"))
    elif not gj[g].get("searched") or not gj[g].get("searched_on"):
        rep["GAP"].append((g, "no sources or date"))
    if g.startswith("DESIGN-RQ-") and g not in req:
        rep["GAP"].append((g, "not in the request file"))
for g in req:
    if g not in used:
        rep["GAP"].append((g, "in the request file but not used"))
rep["gap_ids_used"] = sorted(used)

# wage-type codes are identifiers, not values: stripped (line numbers preserved) before the unbound-value scan
CODE_RX = re.compile(r"\bUS-\d{3}\b|`\d{5}`")
tmp = os.path.join(HERE, "_design_stripped.md")
with open(tmp, "w", encoding="utf-8", newline="\n") as _fh:
    _fh.write("\n".join(CODE_RX.sub("CODE", ln) for ln in lines) + "\n")
pa = PA.run([tmp])
os.remove(tmp)
rep["C46_period_aware"] = {k: v for k, v in pa.items() if k != "detail"}
rep["C46_detail"] = {k: v[:20] for k, v in pa["detail"].items() if k != "outside_year"}
rep["C46_outside_unlabelled"] = [o for o in pa["detail"]["outside_year"] if not o["period_labelled_in_context"]][:20]
json.dump(rep, open(os.path.join(HERE, "design_checks.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False, default=list)
sys.stdout.reconfigure(encoding="utf-8")
cnt = {k: len(rep[k]) for k in ("C29", "WORD", "PATH", "NOTES", "FRAC", "PCT", "UNIT", "C30", "GAP")}
print(cnt)
print({k: v for k, v in pa.items() if k != "detail"})
for k in ("C29", "WORD", "PATH", "NOTES", "FRAC", "PCT", "UNIT", "C30", "GAP"):
    for x in rep[k][:10]:
        print(k, x)
for k in ("missing", "mismatch", "unbound"):
    for x in pa["detail"][k][:15]:
        print("C46", k, json.dumps(x, ensure_ascii=False)[:260])
for x in rep["C46_outside_unlabelled"][:10]:
    print("OUTSIDE-YEAR-UNLABELLED", json.dumps(x, ensure_ascii=False)[:260])
bad = (any(cnt.values()) or pa["keys_missing"] or pa["mismatches_period_aware"] or pa["outside_year_unlabelled"]
       or pa["unbound_period_and_percent_aware"] or not pa["tags"])
sys.exit(1 if bad else 0)
