# -*- coding: utf-8 -*-
"""Fact loader and tag writer for the CCG units m08-m13 + coverage (US build, stage 1).

Every number written by the module renderers and by 01-ccg/_examples/build_examples.py
comes from _research/*-facts.json through this module, so no figure is typed by hand.
T(key) returns the [[FACT:key=value]] tag and records the binding (location, key,
register_id) for the build log. Dated keys (two entries for one key) are selected with
on="YYYY-MM-DD" (entry in force on that date) or ef="YYYY-MM-DD" (effective_from).
"""
import glob
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(HERE, "..", "common"))
import ccg_common as CC  # noqa: E402  round 2: aliases, [[GAP:]] tags, internal paths, percent tags
RESEARCH = os.path.join(BASE, "_research")

FACTS = {}          # key -> [entry, ...] (entry carries _file)
UNRESOLVED = {}     # key -> unresolved item (with _file)
for fp in sorted(glob.glob(os.path.join(RESEARCH, "*-facts.json"))):
    d = json.load(open(fp, encoding="utf-8"))
    for f in d.get("facts", []):
        e = dict(f)
        e["_file"] = os.path.basename(fp)
        FACTS.setdefault(f["key"], []).append(e)
    for u in d.get("unresolved", []):
        x = dict(u)
        x["_file"] = os.path.basename(fp)
        UNRESOLVED.setdefault(u["key"], x)

BINDINGS = []       # (location, key, value-as-written, register_id, file)
LOC = ["(unset)"]
GAPS = []           # (location, marker text, request key)


def set_loc(loc):
    LOC[0] = loc


def has(key):
    return key in FACTS


def entries(key):
    if key not in FACTS:
        key = CC.alias(key)
    if key not in FACTS:
        raise KeyError(f"fact key not in facts files: {key}")
    return FACTS[key]


def entry(key, on=None, ef=None, value=None):
    es = entries(key)
    if value is not None:
        es = [e for e in es if e["value"] == value]
    if ef is not None:
        es = [e for e in es if e.get("effective_from") == ef]
    if on is not None:
        es = [e for e in es if (e.get("effective_from") or "0000") <= on
              and (e.get("effective_to") is None or on <= e["effective_to"])]
    vals = {json.dumps(e["value"]) for e in es}
    if not es:
        raise KeyError(f"no entry of {key} for on={on} ef={ef} value={value}")
    if len(vals) > 1:
        raise ValueError(f"ambiguous key {key}: {sorted(vals)} - pass on= or ef=")
    return es[0]


def V(key, **kw):
    """Raw value (for arithmetic)."""
    return entry(key, **kw)["value"]


def R(key, **kw):
    return entry(key, **kw)["register_id"]


def fmt(e):
    v = e["value"]
    if isinstance(v, bool):
        return "True" if v else "False"
    if isinstance(v, (int, float)):
        if float(v).is_integer():
            return f"{int(v):,}"
        if e.get("currency"):
            return f"{v:,.2f}"
        s = repr(float(v))
        ip, dp = s.split(".")
        return f"{int(ip):,}.{dp}"
    return str(v)


def T(key, **kw):
    e = entry(key, **kw)
    v = e["value"]
    if isinstance(v, str) and "]" in v:
        raise ValueError(f"{key}: value contains ']' and cannot be tagged")
    w = fmt(e)
    BINDINGS.append((LOC[0], key, w, e["register_id"], e["_file"]))
    flag = " (partial source)" if "PARTIAL ROW" in (e.get("note") or "") else ""
    return f"[[FACT:{key}={w}]]{flag}"


def TV(key):
    """All dated values of a key, each tagged with its dates (for keys with several entries)."""
    es = entries(key)
    if len({json.dumps(e["value"]) for e in es}) == 1:
        return T(key, value=es[0]["value"]) + dated(key, value=es[0]["value"])
    parts, seen = [], set()
    for e in sorted(es, key=lambda x: x.get("effective_from") or ""):
        sig = (json.dumps(e["value"]), e.get("effective_from"))
        if sig in seen:
            continue
        seen.add(sig)
        parts.append(T(key, ef=e.get("effective_from"), value=e["value"]) + _span(e))
    return "; ".join(parts)


def _span(e):
    f, t = e.get("effective_from"), e.get("effective_to")
    if t:
        return f" ({f} to {t})"
    return f" (from {f})"


def B(key, yes, no, **kw):
    """Boolean fact written as words (no tag: C46 compares booleans as strings);
    the binding is still recorded for the build log."""
    e = entry(key, **kw)
    BINDINGS.append((LOC[0], key, str(e["value"]), e["register_id"], e["_file"]))
    return yes if e["value"] else no


def REG(key, **kw):
    """Register id in brackets, recorded as a binding of the claim."""
    if not kw and len({x["register_id"] for x in entries(key)}) == 1:
        e = entries(key)[0]
    elif not kw:
        # round 2: a key that gained a dated period (facts re-run) cites the row in force mid build year
        e = entry(key, on="2026-06-30")
    else:
        e = entry(key, **kw)
    return f"[{e['register_id']}]"


def bind(key, **kw):
    """Record a prose binding (claim paraphrased, no number written)."""
    e = entries(key)[0] if not kw else entry(key, **kw)
    BINDINGS.append((LOC[0], key, "(prose)", e["register_id"], e["_file"]))
    return e["register_id"]


def dated(key, **kw):
    """' (from 2026-07-01)' or ' (until 2026-07-31)' when the value changes inside the build year."""
    e = entry(key, **kw)
    f, t = e.get("effective_from"), e.get("effective_to")
    parts = []
    if f and "2026-01-02" <= f <= "2027-12-31":
        parts.append(f"from {f}")
    if t and t < "2026-12-31":
        parts.append(f"until {t}")
    return f" ({', '.join(parts)})" if parts else ""


GAP_TEXT = {
    "fed.eo13706.sick_leave.accrual": "the accrual rate and annual cap of paid sick leave for federal contractors under Executive Order 13706 are not keyed.",
    "multi.sick_leave.coverage_threshold": "paid-sick-leave coverage of employees who work only partly in a State is set per State and is not keyed at multistate level.",
    "fed.form940.instructions_current": "the tax-year 2026 instructions for Forms 940 and 1094-C/1095-C are not yet issued; the 2025 editions were read.",
    "multi.newhire.registration_channel": "the HHS channel through which a multistate employer registers its designated new-hire State was not read (the statute, 42 U.S.C. 653a(b)(1)(B), carries the rule).",
    "fed.iwo.revised_form.state_golive": "the dates on which States go live with the revised IWO / e-IWO (gig-worker fields) within the one-year extension are not known.",
    "fed.indexation.publication_2027": "the tax-year 2027 IRS inflation adjustments, 2027 retirement-plan limits and 2027 Pub. 15-T are not yet published.",
    "fed.common_paymaster.rule": "common-paymaster relief for related employers (IRC 3121(s)) is not keyed.",
    "multi.workers_comp.employee_share": "only the New Mexico fee and the Washington employee deduction are keyed; other States that allow an employee workers' compensation deduction have not been swept.",
    "fed.bik.business_mileage.rate": "the 2026 IRS business standard mileage rate is not keyed (it is not printed in Pub. 15-B).",
    "ma.pfml.split.effective_date": "Chapter 101 of 2026 (s.45) applies the family/medical split change to taxable years from 2026-01-01, while the Department of Family and Medical Leave applies it from 2027-01-01. The build follows the Department (2026 split unchanged) until a notice or regulation settles the transition.",
    "practice.dol_paid_leave_list": "the U.S. DOL compilation of State paid-leave laws could not be read, and the DOL prevailing-wage compilation is out of date for Michigan.",
    "ut.oracle.pub14.examples.withholding": "the effective date of Utah Pub. 14 (Rev. 04/26) is not established, so its six reproduced examples are not dated facts.",
    "dc.oracle.method_2026": "the District of Columbia has published no 2026 withholding method: an emergency act effective 2026-08-13 revoked personal exemptions and the D-4 is under review.",
}


def gap(text, key):
    GAPS.append((LOC[0], text, key))
    return f"⚠️ RESEARCH-GAP [[GAPKEY:{key}]]: {text}"


STATE_NAMES = {}
_m = json.load(open(os.path.join(BASE, "_pipeline", "build-manifest.json"), encoding="utf-8"))
for u in _m["tier"]["_fanout"]["units"]:
    if u.get("name"):
        STATE_NAMES[u["jurisdiction"]] = u["name"]
STATES = [j for j in _m["tier"]["_jurisdictions"] if j not in ("FED", "MULTI")]


def keys_matching(rx):
    r = re.compile(rx)
    return sorted(k for k in FACTS if r.search(k))


def humanize(suffix):
    return suffix.replace("_", " ").replace(".", " / ")


_TAGRX = re.compile(r"(\[\[FACT:[^\]]*\]\])")
_CLEAN = [
    ("Every figure below is computed by `01-ccg/_examples/build_examples.py` from the facts files; no number is typed by hand.",
     "Every figure below is computed from the verified rates, bases and constants; no number is typed by hand."),
    ("derived by the Stage 5 worker", "re-derived from the published method"),
    ("Worker re-derivation; ", "Re-derivation from the published method; "),
    ("worker derivation", "re-derivation"),
    (" keyed in the facts", " established from official sources"),
    ("from keyed facts", "from verified figures"), ("from the keyed rates", "from the verified rates"),
    ("are all keyed", "are all verified"), ("not all keyed", "not all verified"),
    ("Keyed rule", "Verified rule"), ("(keyed States)", "(States with a verified rule)"),
    ("The facts carry", "The verified sources give"), ("the facts carry", "the verified sources give"),
    ("in the facts files", "in the verified sources"), ("facts files", "verified sources"),
    ("is not carried as a fact", "is not established from an official source"),
    ("held as a fact", "established from an official source"),
    ("as dated facts", "as dated results"), ("not dated facts", "not dated results"),
    ("The facts do not key how", "No official source in this build establishes how"),
    ("main pre-tax plans are facts:", "main pre-tax plans are:"), ("Open practice points (not facts):", "Open practice points:"), ("(not facts, not expected results)", "(not expected results)"),
    ("Oracle fact ", "Published result "),
    (", as the key says", ", as the rule says"), ("give a payout key", "give a payout rule"),
    ("with no paid-sick-leave key in the verified sources", "with no verified paid-sick-leave rule"),
    ("have no payout key in the verified sources", "have no verified payout rule"),
    ("with no final-pay key in the verified sources", "with no verified final-pay rule"),
    ("carry no key stating how", "do not establish how"), ("lists every example established from an official source", "lists every verified example"),
    ("(owner decision recorded in MANDATE.md)", "(owner decision)"),
    ("is not keyed", "is not established from an official source"), ("are not keyed", "are not established from an official source"),
    ("Not keyed", "Not established"), ("not keyed", "not established from an official source"),
    ("rule is keyed", "rule is established"), ("are keyed", "are established from official sources"),
    ("is keyed", "is established from an official source"),
]


def clean(text):
    parts = _TAGRX.split(text)
    out = []
    for i, p in enumerate(parts):
        if i % 2 == 0:
            for a, b in _CLEAN:
                p = p.replace(a, b)
        out.append(p)
    return "".join(out)
