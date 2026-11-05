# -*- coding: utf-8 -*-
"""Strict numeric self-check: (1) every keyed table row `key` | value | effective: value tokens are values of that key, dates are
effective dates of that key; (2) numbers in SKILL.md and 13-gotchas.md (outside ids and form names) exist in the facts. exit 1 on a miss."""
import glob, json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.abspath(os.path.join(HERE, ".."))
BASE = os.path.abspath(os.path.join(OUT, "..", "..", "US-compliance"))
NUM = re.compile(r"\d[\d,]*(?:\.\d+)?")
F = {}
for f in glob.glob(os.path.join(BASE, "_research", "*facts.json")):
    for x in json.load(open(f, encoding="utf8")).get("facts", []):
        F.setdefault(x["key"], []).append(x)


def nf(t):
    t = t.rstrip(",").replace(",", "")
    try:
        return repr(float(t))
    except ValueError:
        return t


def tk(s):
    return {nf(t) for t in NUM.findall(str(s))}


ROW = re.compile(r"^\|\s*`([a-z0-9_.]+)`\s*\|(.*)$")
EFF = re.compile(r"^(?:from )?(\d{4}-\d\d-\d\d)(?: to (\d{4}-\d\d-\d\d|open))?$")
files = [p for p in glob.glob(os.path.join(OUT, "**", "*.md"), recursive=True) if "_build" not in p]
bad = {"VAL": [], "PERIOD": [], "HAND": []}
n_rows = n_vals = n_per = 0
for p in sorted(files):
    rel = os.path.relpath(p, OUT)
    for i, line in enumerate(open(p, encoding="utf8").read().split("\n"), 1):
        m = ROW.match(line)
        if not m or m.group(1) not in F:
            continue
        cells = [c.strip() for c in re.split(r"(?<!\\)\|", m.group(2))]
        facts = F[m.group(1)]
        allv = set()
        for x in facts:
            allv |= tk(x.get("value"))
        effs = {x.get("effective_from") for x in facts} | {x.get("effective_to") for x in facts}
        n_rows += 1
        if cells:
            vt = tk(re.sub(r"open gap [A-Za-z-]*\d+", "", re.sub(r"\d{4}-\d\d-\d\d", "", cells[0])))
            if vt:
                n_vals += 1
                if not vt <= allv:
                    bad["VAL"].append((rel, i, m.group(1), sorted(vt - allv)[:3]))
        for c in cells[1:]:
            em = EFF.match(c)
            if em:
                for d in em.groups():
                    if d and d != "open":
                        n_per += 1
                        if d not in effs:
                            bad["PERIOD"].append((rel, i, m.group(1), d))
corp = set()
for k, v in F.items():
    for x in v:
        corp |= tk(" ".join(str(x.get(a) or "") for a in ("value", "effective_from", "effective_to", "register_id")))
IDS = re.compile(r"\b[A-Z]{1,6}-[A-Z0-9]+(?:-\d+)+\b|\bRQ-\d+\b|\bUS-[A-Z0-9]+-\d+\b")
FORMS = re.compile(r"Public Law 119-21|Pub\. 15-T|Forms? W-[24]|W-4|Forms? 94[01]|Form 1099-NEC|Act 110|Act 26-416|Chapter 101|"
                   r"HRS 487J|487J-2|Step 4\(b\)|US-OWN-0\d\d|001\.\.011|[Ss]ections? \d+|s\.45|W-166|WH-1603|TPG-211|KW-100|"
                   r"Pub\. 14|Rev\. [0-9/]+|\b20\d\d\b|\d{4}-\d\d-\d\d|^\s*\d+\. |\b\d\b|\b1[13]\b|\b5[01]\b|\b119\b|\b15-T\b")
n_hand = 0
for rel in ("SKILL.md", "references/13-gotchas.md"):
    t = open(os.path.join(OUT, rel), encoding="utf8").read().split("## Fact index")[0]
    t = FORMS.sub(" ", IDS.sub(" ", t))
    for n in NUM.findall(t):
        n = nf(n)
        n_hand += 1
        if n not in corp:
            bad["HAND"].append((rel, n))
print("keyed rows:", n_rows, "value checks:", n_vals, "period checks:", n_per, "handwritten numbers:", n_hand)
for k, v in bad.items():
    print("STRICT", k, len(v))
    for x in v[:15]:
        print("  ", x)
json.dump(bad, open(os.path.join(HERE, "selfcheck_strict_result.json"), "w"), indent=1)
sys.exit(1 if any(bad.values()) else 0)
