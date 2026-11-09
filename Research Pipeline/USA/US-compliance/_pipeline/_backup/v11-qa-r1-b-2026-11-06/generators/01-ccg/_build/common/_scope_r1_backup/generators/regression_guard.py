# -*- coding: utf-8 -*-
"""Post-build regression guard (artifact-builder, QA r3d).

Diffs every generated unit (01-ccg/modules/*.md, 01-ccg/annexes/*.md) against the copy of the previous build
and FAILS if a changed line is not explained by
  (a) the facts diff: a fact key (or register row) that changed between the facts snapshot taken before the
      round and the current facts / register, or that agent 2 names in _research/qa-r3d-fix/AGENT2-R3d.md;
  (b) a routed builder fix of r3d:
        F4  vocabulary stripper (TN.3 note restored),
        F1  binding guard / status and key-family binding (every re-bound key is in the generators' r3d logs),
        F8  AL.2 status minimums and ID.3 rate components,
        F7  'local copy' wording removed from Sources cells (old line == new line after the new vocabulary rules),
      or a Sources-label renumbering only (S<n> labels shift when the cited register rows change).
It also fails when a changed line has unbalanced parentheses or double quotes that the previous line did not have
(QA r3d finding 4 lint), and when the TN.3 evidence note is not rendered in full.

usage: python regression_guard.py [--prev DIR] [--facts-before DIR] [--agent2 FILE] [--json FILE]
Exit 1 on any unexplained change.
"""
import argparse
import csv
import difflib
import glob
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, HERE)
sys.stdout.reconfigure(encoding="utf-8")
import ccg_common as CC  # noqa: E402

ap = argparse.ArgumentParser()
ap.add_argument("--prev", default=os.path.join(HERE, "_r3d_backup", "prev_build"))
ap.add_argument("--facts-before", default=os.path.join(HERE, "_r3d_backup", "facts_before"))
ap.add_argument("--agent2", default=os.path.join(BASE, "_research", "qa-r3d-fix", "AGENT2-R3d.md"))
ap.add_argument("--json", default=os.path.join(HERE, "out", "regression_guard.json"))
a = ap.parse_args()

TAG = re.compile(r"\[\[(FACT|GAP):([^=\]]+)(?:=([^\]]*))?\]\]")
RID = re.compile(r"\bUS-[A-Z0-9]+-\d+\b")
KEYRX = re.compile(r"\b[a-z]{2,5}(?:\.[a-z0-9_]+){1,9}\b")


# ------------------------------------------------------------------ facts diff
def facts_by_key(folder):
    out = {}
    for fp in glob.glob(os.path.join(folder, "*-facts.json")):
        for f in json.load(open(fp, encoding="utf-8")).get("facts", []):
            out.setdefault(f["key"], []).append(json.dumps(f, sort_keys=True, ensure_ascii=False))
        for u in json.load(open(fp, encoding="utf-8")).get("unresolved", []):
            out.setdefault(u["key"], []).append("U" + json.dumps(u, sort_keys=True, ensure_ascii=False))
    return {k: sorted(v) for k, v in out.items()}


def register(path):
    with open(path, encoding="utf-8", newline="") as fh:
        return {r["id"]: json.dumps(r, sort_keys=True, ensure_ascii=False) for r in csv.DictReader(fh)}


fb, fa = facts_by_key(a.facts_before), facts_by_key(os.path.join(BASE, "_research"))
changed_keys = {k for k in set(fb) | set(fa) if fb.get(k) != fa.get(k)}
rb = register(os.path.join(a.facts_before, "legal-basis-register.csv"))
ra = register(os.path.join(BASE, "00-official-sources", "legal-basis-register.csv"))
changed_rids = {i for i in set(rb) | set(ra) if rb.get(i) != ra.get(i)}
# a register row cited by a changed fact (before or after) is part of the facts diff too
for k in changed_keys:
    for rec in fb.get(k, []) + fa.get(k, []):
        changed_rids |= set(RID.findall(rec))
agent2_keys, agent2_rids = set(), set()
if os.path.exists(a.agent2):
    t = open(a.agent2, encoding="utf-8").read()
    agent2_keys = {k for k in KEYRX.findall(t) if k in fa or k in fb}
    agent2_rids = set(RID.findall(t))
explained_keys = changed_keys | agent2_keys
explained_rids = changed_rids | agent2_rids
# Sources rows of the FED-CT annexes print the register row's instrument / article, not its id: a row is part of
# the facts diff when it carries the instrument or article text of a changed register row (old or new version)
_SRCTXT = set()
for i in explained_rids:
    for rec in (rb.get(i), ra.get(i)):
        if rec:
            r = json.loads(rec)
            for fld in ("instrument_name", "article_or_section"):
                v = (r.get(fld) or "").replace("|", "/").strip()
                if len(v) >= 12:
                    _SRCTXT.add(v[:60])

# ------------------------------------------------------------------ routed builder fixes (r3d)
ROUTED_KEYS = {"tn.sui.employee.rate", "al.local.leeds.rate", "id.sui.new_employer.rate",
               "id.sui.new_employer.ui_component.rate", "id.sui.new_employer.admin_component.rate"}
ROUTED_KEY_RX = re.compile(r"^al\.wh\.std_deduction\.")
rebind_keys = set()
for fp in glob.glob(os.path.join(BASE, "01-ccg", "_scratch", "annex-DC-MA", "report_*.json")):
    d = json.load(open(fp, encoding="utf-8"))
    for r in d.get("r3d_rebind", []):
        rebind_keys |= {x for x in r[1:3] if x}
    for r in d.get("r3d_components", []):
        rebind_keys.add(r[1])
fr = os.path.join(BASE, "01-ccg", "_scratch", "annex-FED-CT", "report.json")
if os.path.exists(fr):
    for u, d in json.load(open(fr, encoding="utf-8")).items():
        for r in d.get("r3d_rebind", []):
            rebind_keys |= {x for x in r[1:3] if x}
for fp in glob.glob(os.path.join(BASE, "_research", "synthesis-B", "_scratch-ccg-build-MD-NV", "*.json")):
    try:
        d = json.load(open(fp, encoding="utf-8"))
    except Exception:
        continue
    for st in (d.values() if isinstance(d, dict) else d if isinstance(d, list) else []):
        if isinstance(st, dict):
            for r in st.get("r3d_guard_refused", []):
                rebind_keys.add(r[2])


def visible(s):
    return TAG.sub(lambda m: m.group(3) or "", s)


def tag_keys(s):
    return [m.group(2) for m in TAG.finditer(s) if m.group(1) == "FACT"]


def keys_in(s):
    return set(tag_keys(s)) | set(re.findall(r"`([a-z]{2,5}(?:\.[a-z0-9_]+)+)`", s))


def balanced(s):
    v = s
    depth = 0
    for ch in v:
        depth += (ch == "(") - (ch == ")")
        if depth < 0:
            return False
    return depth == 0 and v.count('"') % 2 == 0


def explain(unit, old, new):
    """Return the reason a changed line is explained, or None."""
    ks = keys_in(old or "") | keys_in(new or "")
    rs = set(RID.findall(old or "")) | set(RID.findall(new or ""))
    if ks & explained_keys:
        return "facts diff (key: " + ", ".join(sorted(ks & explained_keys))[:120] + ")"
    if rs & explained_rids:
        return "facts diff (register: " + ", ".join(sorted(rs & explained_rids))[:120] + ")"
    if re.match(r"\|\s*S\d+\s*\|", (new or old or "")) and any(t in (old or "") or t in (new or "") for t in _SRCTXT):
        return "facts diff (register row text)"
    if ks & ROUTED_KEYS or any(ROUTED_KEY_RX.match(k) for k in ks):
        return "routed fix F4/F8/F1 (" + ", ".join(sorted(k for k in ks if k in ROUTED_KEYS or ROUTED_KEY_RX.match(k)))[:120] + ")"
    if old is not None and new is not None:
        if CC.strip_internal(old) == new or CC.strip_internal(old) == CC.strip_internal(new):
            return "routed fix F7 (vocabulary rules)"
        sl = lambda s: re.sub(r"\bS\d+\b", "S#", s)  # noqa: E731
        if sl(old) == sl(new):
            return "Sources label renumbering"
        if visible(old) == visible(new):
            diffk = set(tag_keys(old)) ^ set(tag_keys(new))
            if diffk and diffk <= rebind_keys:
                return "routed fix F1/F8 re-binding (" + ", ".join(sorted(diffk))[:120] + ")"
        # a tag removed by the guard: the number is printed untagged, nothing else changed
        if TAG.sub(lambda m: m.group(3) or "", old) == new and set(tag_keys(old)) - set(tag_keys(new)) <= rebind_keys:
            return "routed fix F1 guard (binding refused)"
    return None


rows, unexplained, lint = [], [], []
for sub in ("modules", "annexes"):
    for fp in sorted(glob.glob(os.path.join(a.prev, sub, "*.md"))):
        name = os.path.basename(fp)
        np_ = os.path.join(BASE, "01-ccg", sub, name)
        if not os.path.exists(np_):
            unexplained.append((f"{sub}/{name}", "unit missing in the new build", "", ""))
            continue
        o = open(fp, encoding="utf-8").read().split("\n")
        n = open(np_, encoding="utf-8").read().split("\n")
        sm = difflib.SequenceMatcher(None, o, n, autojunk=False)
        for op, i1, i2, j1, j2 in sm.get_opcodes():
            if op == "equal":
                continue
            olds, news = o[i1:i2], n[j1:j2]
            pairs = []
            for k in range(max(len(olds), len(news))):
                pairs.append((olds[k] if k < len(olds) else None, news[k] if k < len(news) else None))
            for ol, nl in pairs:
                if (ol or "").strip() == "" and (nl or "").strip() == "":
                    continue
                why = explain(name, ol, nl)
                rec = (f"{sub}/{name}", why or "UNEXPLAINED", (ol or "")[:300], (nl or "")[:300])
                rows.append(rec)
                if not why:
                    unexplained.append(rec)
                if nl is not None and not balanced(visible(nl)) and (ol is None or balanced(visible(ol))):
                    lint.append((f"{sub}/{name}", nl[:300]))
    new_units = {os.path.basename(p) for p in glob.glob(os.path.join(BASE, "01-ccg", sub, "*.md"))}
    old_units = {os.path.basename(p) for p in glob.glob(os.path.join(a.prev, sub, "*.md"))}
    for x in sorted(new_units - old_units):
        unexplained.append((f"{sub}/{x}", "new unit not in the previous build", "", ""))

# TN.3 evidence note rendered in full (QA r3d finding 4)
tn = open(os.path.join(BASE, "01-ccg", "annexes", "annex_TN.md"), encoding="utf-8").read()
tn_row = next((ln for ln in tn.split("\n") if ln.startswith("| `tn.sui.employee.rate`")), "")
tn_ok = ("50-7-402 and 50-7-403" in tn_row and "financed solely by employer premiums" in tn_row
         and balanced(visible(tn_row.split("|")[-2])))

res = {"status": "PASS" if not unexplained and not lint and tn_ok else "FAIL",
       "changed_lines": len(rows), "unexplained": len(unexplained), "paren_quote_lint": len(lint), "tn3_full": tn_ok,
       "facts_changed_keys": len(changed_keys), "register_changed_rows": len(changed_rids - set().union(
           *[set(RID.findall(r)) for k in changed_keys for r in fb.get(k, []) + fa.get(k, [])] or [set()])),
       "agent2_keys": len(agent2_keys), "rebind_keys": len(rebind_keys),
       "by_reason": {}, "unexplained_list": unexplained, "lint_list": lint, "rows": rows}
for r in rows:
    key = re.sub(r" \(.*", "", r[1])
    res["by_reason"][key] = res["by_reason"].get(key, 0) + 1
os.makedirs(os.path.dirname(a.json), exist_ok=True)
json.dump(res, open(a.json, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
print(f"[regression guard] {res['status']}: {len(rows)} changed lines, {len(unexplained)} unexplained, "
      f"{len(lint)} paren/quote lint, TN.3 full note {tn_ok}; by reason {res['by_reason']}")
for u in unexplained:
    print("  UNEXPLAINED", u[0], "\n    OLD:", u[2][:220], "\n    NEW:", u[3][:220])
for l_ in lint:
    print("  LINT", l_[0], l_[1][:220])
sys.exit(0 if res["status"] == "PASS" else 1)
