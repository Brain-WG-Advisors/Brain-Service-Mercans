# -*- coding: utf-8 -*-
"""Shared helpers for the CCG core-module builder (units m01..m07, US build).

Every factual value is rendered from the CCG facts files by key, never typed:
  T(key)  -> [[FACT:key=value]] tag (numbers and short strings)
  K(key)  -> `key` [register_id] citation for rule facts (value quoted elsewhere or paraphrased)
  Q(key)  -> the string value quoted inside a [[FACT:]] tag (verbatim rule text)
  D(key)  -> effective_from of the selected dated value (binding recorded)
Multi-dated keys must be selected with on='YYYY-MM-DD'.
Every call records a binding (location, key, register_id) for the build log.
GAP(...) writes an in-place RESEARCH-GAP marker and queues a research request.
"""
import glob
import json
import os
import re

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
RES = os.path.join(BASE, "_research")

FACTS = {}
UNRES = {}
for fp in sorted(glob.glob(os.path.join(RES, "CCG-*-facts.json"))):
    d = json.load(open(fp, encoding="utf-8"))
    for f in d.get("facts", []):
        f = dict(f)
        f["_file"] = os.path.basename(fp)
        FACTS.setdefault(f["key"], []).append(f)
    for u in d.get("unresolved", []):
        u = dict(u)
        u["_file"] = os.path.basename(fp)
        UNRES.setdefault(u["key"], []).append(u)

MANIFEST = json.load(open(os.path.join(BASE, "_pipeline", "build-manifest.json"), encoding="utf-8"))

STATE = {"unit": None, "loc": None}
BINDINGS = []      # (unit, loc, key, register_id, value_shown)
GAPS = []          # dicts
COVERAGE = []      # (unit, loc, row)
UNRES_USED = []    # (unit, loc, key, blocking)


def set_unit(unit):
    STATE["unit"] = unit
    STATE["loc"] = None


def _pick(key, on=None):
    if key not in FACTS:
        raise KeyError(f"fact key not found: {key}")
    fs = FACTS[key]
    # de-duplicate identical value+period copies held in two files (one key, one value)
    uniq = []
    for f in fs:
        sig = (json.dumps(f["value"], sort_keys=True), f.get("effective_from"), f.get("effective_to"))
        if sig not in [u[0] for u in uniq]:
            uniq.append((sig, f))
    fs = [u[1] for u in uniq]
    if on is None:
        if len(fs) > 1:
            raise ValueError(f"{key} has {len(fs)} dated values; pass on=")
        return fs[0]
    cands = [f for f in fs if (f.get("effective_from") or "0000") <= on <= (f.get("effective_to") or "9999")]
    if len(cands) != 1:
        raise ValueError(f"{key} on {on}: {len(cands)} candidates")
    return cands[0]


def _fmt(f, fmt=None):
    v = f["value"]
    if isinstance(v, bool):
        raise ValueError("boolean facts are cited with R()/K(), not tagged")
    if isinstance(v, str):
        return v
    if fmt == "money":
        return f"{v:,.2f}"
    if fmt == "int":
        return f"{v:,.0f}"
    if isinstance(v, int):
        return f"{v:,}"
    if float(v).is_integer():
        return f"{int(v):,}"
    if f.get("currency") == "USD":
        return f"{v:,.2f}"
    s = repr(v)
    return s


def _bind(key, f, shown):
    BINDINGS.append((STATE["unit"], STATE["loc"], key, f["register_id"], shown))


def T(key, on=None, fmt=None):
    f = _pick(key, on)
    s = _fmt(f, fmt)
    if "]" in s:
        raise ValueError(f"value of {key} contains ']' and cannot be tagged")
    _bind(key, f, s)
    return f"[[FACT:{key}={s}]]"


def Q(key, on=None):
    """Verbatim string value inside a tag (rule text)."""
    f = _pick(key, on)
    if not isinstance(f["value"], str):
        return T(key, on)
    return T(key, on)


def K(key, on=None):
    f = _pick(key, on)
    _bind(key, f, "(cited)")
    return f"`{key}` [{f['register_id']}]"


def R(key, on=None):
    """Register id only, binding recorded (for a claim paraphrased from the fact)."""
    f = _pick(key, on)
    _bind(key, f, "(paraphrased)")
    return f"[{f['register_id']}]"


def D(key, on=None, which="from"):
    f = _pick(key, on)
    _bind(key, f, f"(date {which})")
    return f.get("effective_from") if which == "from" else f.get("effective_to")


def V(key, on=None):
    f = _pick(key, on)
    _bind(key, f, "(value used in computation)")
    return f["value"]


def has(key):
    return key in FACTS


def H(level, text):
    STATE["loc"] = text.strip()
    return "\n" + "#" * level + " " + text.strip() + "\n"


def COV(row):
    """Reference a coverage-matrix row (CCG-coverage-facts.json) carried at this location."""
    cm = json.load(open(os.path.join(RES, "CCG-coverage-facts.json"), encoding="utf-8"))["coverage_matrix"]
    r = cm[row]
    COVERAGE.append((STATE["unit"], STATE["loc"], row))
    ids = ", ".join(s["register_id"] for s in r.get("sources", []))
    return f"coverage row `{row}` [{ids}]"


def UNR(key, text=None):
    """In-place marker for a key that the facts file carries in unresolved[] (no new request)."""
    us = UNRES.get(key)
    if not us:
        raise KeyError(f"not an unresolved key: {key}")
    u = us[0]
    blk = bool(u.get("blocking"))
    UNRES_USED.append((STATE["unit"], STATE["loc"], key, blk, u["_file"]))
    label = "blocking" if blk else "non-blocking"
    why = text or u["why"]
    return f"⚠️ RESEARCH-GAP ({label}): {why} (open item `{key}` in {u['_file']}; closes with: {u['what_would_close_it']})"


def GAP(key, text, question, why_blocking, domain, tier="A.2", blocking=False, attempted=None, shape=None,
        severity=None):
    """In-place marker plus a queued research request."""
    label = "blocking" if blocking else "non-blocking"
    g = dict(unit=STATE["unit"], loc=STATE["loc"], key=key, text=text, question=question,
             why_blocking=why_blocking, domain=domain, tier=tier, blocking=blocking,
             attempted=attempted or [], shape=shape,
             severity=severity or ("blocker" if blocking else "major"))
    # one request per key and unit; further locations are appended
    for x in GAPS:
        if x["key"] == key and x["unit"] == g["unit"]:
            x.setdefault("more_locs", []).append(STATE["loc"])
            break
    else:
        GAPS.append(g)
    return f"⚠️ RESEARCH-GAP ({label}): {text} (request key `{key}`)"


def MAN(*path):
    v = MANIFEST
    for p in path:
        v = v[p]
    return v


def dump_state(unit, outdir):
    os.makedirs(outdir, exist_ok=True)
    json.dump({"bindings": [b for b in BINDINGS if b[0] == unit],
               "gaps": [g for g in GAPS if g["unit"] == unit],
               "coverage": [c for c in COVERAGE if c[0] == unit],
               "unresolved_used": [u for u in UNRES_USED if u[0] == unit]},
              open(os.path.join(outdir, f"{unit}.state.json"), "w", encoding="utf-8"), indent=1,
              ensure_ascii=False)


def write_module(unit, text):
    path = os.path.join(BASE, "01-ccg", "modules", f"{unit}.md")
    text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"
    open(path, "w", encoding="utf-8", newline="\n").write(text)
    dump_state(unit, os.path.join(os.path.dirname(__file__), "state"))
    return path
