# -*- coding: utf-8 -*-
"""US Statutory Integration Index (SIR) - common helpers: facts (SIR first), tags, F44 gate, gap registry,
binding log, text guards.

Every factual value written into the document comes from a facts file in _research/ through fv() / tag();
nothing is typed by hand. The generator (build_sir.py) is the only source of the document: a correction goes
into sir_defs.py / sir_rules.py / build_sir.py, never into the .docx.

Read-only inputs: _pipeline/build-manifest.json, scope_manifest.json, _research/*-facts.json, the register,
the approved Report Specs, DD and WTC. Facts priority for a key present in several files:
SIR, RSPEC, DD, WTC, CCG (period-aware, as the Report Spec helper).
"""
import csv
import glob
import json
import os
import sys as _sys_dw
_DW_DIR = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "01-ccg", "_build", "common"))
if _DW_DIR not in _sys_dw.path:
    _sys_dw.path.insert(0, _DW_DIR)
import deliverable_wording as DW  # noqa: E402  v1.1 QA r1: deliverable wording + effective-period status
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SIRDIR = os.path.dirname(HERE)
BASE = os.path.dirname(SIRDIR)
RESEARCH = os.path.join(BASE, "_research")
SPECS = os.path.join(BASE, "04-reports-spec")
CHECKS = os.path.join(HERE, "checks")
SCRATCH = os.path.join(HERE, "_scratch")
SHARED = os.path.expanduser("~/mercans-pipeline/shared")

sys.path.insert(0, os.path.join(SPECS, "_build"))
sys.path.insert(0, HERE)
import us_common as C  # noqa: E402  (read-only helper of the approved Report Specs)
import f44_lib  # noqa: E402

MANIFEST = C.MANIFEST
PKG = MANIFEST["package"]["version"]
ISSUE = MANIFEST["package"]["issue_date"]
AUTHOR = MANIFEST["package"]["issued_by"]
STATUS = "For QA" if "placeholder" in str(MANIFEST["package"].get("_note", "")).lower() else "Issued"
YEAR = MANIFEST["year"]
CODE = MANIFEST["code"]
COUNTRY = MANIFEST["country"]
STATE_NAMES = C.STATE_NAMES
SIR_ID = f"{CODE}-SIR-INDEX-001"
SIR_REF = f"{SIR_ID} v{PKG}"
FILENAME = f"{SIR_ID}-v{PKG}.docx"
DD_REF = f"{CODE}-DD-001 v{PKG}"
CCG_REF = f"{CODE}-CCG-001 v{PKG}"
WTC_REF = f"{CODE}-WTC-001 v{PKG}"
FOOTER = f"{SIR_ID} v{PKG} | Mercans Compliance Regulations Team | {YEAR}"

REG = {r["id"]: r for r in csv.DictReader(
    open(os.path.join(BASE, "00-official-sources", "legal-basis-register.csv"), encoding="utf-8"))}
SCOPE = C.SCOPE
SIRFACTS = json.load(open(os.path.join(RESEARCH, "SIR-facts.json"), encoding="utf-8"))
SIR_KEYS = [f["key"] for f in SIRFACTS["facts"]]
UNRESOLVED = SIRFACTS.get("unresolved", [])

PRIORITY = ["SIR-facts.json", "RSPEC-facts.json", "DD-8_sheets-facts.json", "WTC-country_specific-facts.json",
            "WTC-global_baseline-facts.json"]


def _prio(f):
    n = f["_file"]
    if n in PRIORITY:
        return PRIORITY.index(n)
    return 10 if n.startswith("CCG-") else 20


USED = {}            # (key, effective_from) -> set(locations)
_CUR = ["?"]
GAPS = {}            # id key -> record; filled by gap()
BLOCKED = {}         # key -> list of missing elements (F44)
_F44 = {}


def at(label):
    _CUR[0] = label


def fact(key, period=None):
    """Fact entry of `key` for the build year (or `period` = 'YYYY' / effective_from date); SIR file first."""
    es = C.FACTS.get(key)
    if not es:
        raise KeyError(f"no fact {key!r}")
    if period:
        p = str(period)
        cand = [f for f in es if str(f.get("effective_from") or "").startswith(p)
                or (len(p) == 4 and (f.get("effective_from") or "0000")[:4] <= p <= (f.get("effective_to") or "9999")[:4])]
    else:
        y0, y1 = f"{YEAR}-01-01", f"{YEAR}-12-31"
        cand = [f for f in es if (f.get("effective_from") or "0000") <= y1 and (f.get("effective_to") or "9999") >= y0]
        if not cand:
            cand = list(es)
    if not cand:
        raise KeyError(f"no fact {key!r} for period {period!r}")
    cand.sort(key=lambda f: (_prio(f), -(len(str(f.get("effective_from") or "")))))
    if not period and key in C41_KEYS and len(cand) > 1:
        cand.sort(key=lambda f: str(f.get("effective_from") or ""), reverse=True)   # the period in force now
    return cand[0]


def has(key):
    return key in C.FACTS


def fmt(v):
    return C.fmt_value(v)


def f44_miss(f):
    """Missing text elements of the fact in the local copy of its register row(s). Cached per (key, from, rid)."""
    ck = (f["key"], f.get("effective_from"), f["register_id"], str(f["value"]))
    if ck not in _F44:
        miss, has_copy = f44_lib.check_fact(f)
        _F44[ck] = (miss, has_copy)
    return _F44[ck]


def rids(f):
    return [f["register_id"]] + [r for r in (f.get("_also_register_ids") or []) if r != f["register_id"]]


def cite_f(f):
    return " ".join(f"[{r}]" for r in rids(f))


def eff_f(f):
    a, b = f.get("effective_from"), f.get("effective_to")
    if DW.period_status(f) or (f.get("_effective_from_basis") and b):      # v1.1 QA r1: proposed / historical / own end date
        return DW.period_wording(f, "")
    if f.get("_effective_from_basis"):
        return f"in force for {YEAR}; the source carries no effective date"
    if a and b:
        return f"effective {a} to {b}"
    if a:
        return f"effective from {a}"
    return ""


def _note_use(f):
    USED.setdefault((f["key"], f.get("effective_from")), set()).add(_CUR[0])


GAP_IDS = {}
OPEN_KEYS = set()      # keys whose fact is an open question (documented in the facts' unresolved[]); set by sir_defs


def gap(key, why=None, jur=None):
    """Neutral gap text for a key: 'Not configured in this release [[GAP:SIR-RQ-nn]]'. The id is assigned after
    pass 1, in sorted key order (stable between rebuilds). `jur` records the jurisdiction of a grouped request."""
    g = GAPS.setdefault(key, {"key": key, "why": why, "locations": [], "jurs": set()})
    if _CUR[0] not in g["locations"]:
        g["locations"].append(_CUR[0])
    if why and not g.get("why"):
        g["why"] = why
    if jur:
        g["jurs"].add(jur)
    return f"Not configured in this release [[GAP:{GAP_IDS.get(key, 'SIR-RQ-00')}]]"


def tag(key, period=None):
    f = fact(key, period)
    if "]" in str(f["value"]):
        raise ValueError(f"{key}: value contains ']' and cannot be written as a [[FACT:]] tag")
    _note_use(f)
    return f"[[FACT:{key}={fmt(f['value'])}]]"


def usable(key, period=None):
    """(True, None) when the fact exists, is not an open question, passes F44 and (if it carries a figure) rests on a
    tier-A register row; else (False, reason)."""
    if key not in C.FACTS:
        return False, "no_fact"
    if key in OPEN_KEYS:
        return False, "open"
    f = fact(key, period)
    if "]" in str(f["value"]):
        return False, "bracket"
    miss, has_copy = f44_miss(f)
    if not has_copy and not miss:
        miss = [("nocopy", "no saved copy of the cited source")]
    if miss:
        return False, ("f44", miss)
    if re.search(r"\d", str(f["value"])) and not reg_ok(f["register_id"]):
        return False, "tier"
    return True, None


C41_KEYS = {"sir.ga.ui.wage_report", "rspec.me.wh_return.form", "sir.nj.withholding.agent_authorization", "sir.dc.withholding.agent_authorization",
            "sir.tx.ui.agent_authorization", "rspec.fed.form940.due", "rspec.fed.futa.credit_reduction.states",
            "ga.report.sui.efile_all_employers"}   # v1.1: GA all-employer e-filing from 2026-08-09
TY2025_GAP = {"rspec.fed.form940.due": "rspec.fed.form940.due.ty2026", "fed.aca.efile_threshold": "fed.aca.efile_threshold.ty2026"}


def render(key, period=None, with_cite=True, with_eff=False):
    f = fact(key, period)
    t = tag(key, period)
    dated = False
    if key in C41_KEYS:      # C41: a value that changes during the build year is printed with its date
        ef, et = str(f.get("effective_from") or ""), str(f.get("effective_to") or "")
        if ef.startswith(str(YEAR)) and ef[5:] != "01-01":
            t += f" (from {ef})"
        elif et.startswith(str(YEAR)):
            # v1.1 QA r1: an item with its own end date prints its own dates once, with no generic C41 wording
            t += f" ({ef} to {et})" if ef else f" (until {et})"
            dated = True
    u = f.get("unit_of_measure")
    if u and isinstance(f["value"], (int, float)) and not isinstance(f["value"], bool):
        if u == "days" and "business" in key:
            u = "business days"
        t += f" {u}"
    if with_cite:
        t += f" {cite_f(f)}"
    if (with_eff or f.get("effective_to")) and not dated:
        t += f" ({eff_f(f)})"
    if f44_lib.LIMITATION_KEYS.get(key):       # F27: the limitation sentence the DD prints for the same fact
        t += " " + f44_lib.LIMITATION_KEYS[key]
    if key in TY2025_GAP:      # SIR-QA2-05: a TY2025 rule printed as a dated limitation, with its request number
        if key == "fed.aca.efile_threshold":
            t += " (TY2025 rule, re-verify on the 2026 instructions)"
        t += " " + gap(TY2025_GAP[key], "open")
    if "DRAFT" in str(f.get("note") or ""):
        t += (" Per 2026 draft: read from the IRS early-release draft of the 2026 form or instructions; "
              "re-verify against the final 2026 revision before go-live.")
    return t


def try_fv(key, period=None, with_cite=True, with_eff=False):
    ok, _why = usable(key, period)
    return render(key, period, with_cite, with_eff) if ok else None


def fv(key, period=None, with_cite=True, with_eff=False, jur=None):
    """Tagged fact value + unit + register ids (+ effective period). Never unproven text: an open question or a value
    whose text elements are not found in the local copy of its register row(s) returns the neutral gap text."""
    ok, why = usable(key, period)
    if ok:
        return render(key, period, with_cite, with_eff)
    if isinstance(why, tuple):
        BLOCKED[key] = why[1]
    return gap(key, "f44" if isinstance(why, tuple) else str(why), jur)


def pick(keys, jur=None, gap_key=None, with_cite=True, with_eff=False):
    """First usable fact of `keys` (in order). When none is usable: the neutral gap text on the first blocked
    candidate (F44 / open), else on `gap_key` (a grouped request for a missing source)."""
    first_blocked = None
    for k in keys:
        k, _, per = k.partition("@")       # v1.1 build 2: 'key@effective_from' selects one dated period
        per = per or None
        ok, why = usable(k, per)
        if ok:
            return render(k, per, with_cite, with_eff), k
        if why != "no_fact" and first_blocked is None:
            first_blocked = (k, why)
    if first_blocked:
        k, why = first_blocked
        if isinstance(why, tuple):
            BLOCKED[k] = why[1]
        return gap(k, "f44" if isinstance(why, tuple) else str(why), jur), None
    return gap(gap_key or "sir.unspecified.missing", "missing", jur), None


# ------------------------------------------------------------------ text guards ---
HARD_CS = [r"\bTODO\b", r"\bTBD\b", r"\bFIXME\b", r"\bVERIFY\s+No\b", r"RESEARCH-GAP", r"\?\?\?"]
HARD_CI = [r"\[\s*placeholder\s*\]", r"\[\s*CHECK\s*\]", r"\[\s*\?\s*\]", r"to be confirmed", r"to be verified", r"lorem ipsum"]
ANYTAG = re.compile(r"\[\[(?:FACT|GAP):[^\]]*\]\]")


def hard_hits(text):
    out = [p for p in HARD_CS if re.search(p, text)]
    return out + [p for p in HARD_CI if re.search(p, text, re.I)]


def clean(text):
    s = str(text)
    h = hard_hits(s)
    if h:
        raise ValueError(f"residual marker {h} in: {s[:120]}")
    bare = ANYTAG.sub(" ", s)
    m = C.C29.search(bare) or C.PIPELINE_WORDS.search(bare)
    if m:
        raise ValueError(f"forbidden wording {m.group(0)!r} in: {s[:160]}")
    pm = C.PATH_RX.search(s)
    if pm:
        raise ValueError(f"internal path {pm.group(0)!r} in: {s[:160]}")
    return s


def reg_name(rid):
    r = REG.get(rid)
    return r["instrument_name"] if r else rid


def reg_ok(rid):
    r = REG.get(rid)
    return bool(r) and r.get("tier") not in ("B", "C") and r.get("status") != "MANUAL"


def state_name(code):
    return STATE_NAMES[code.upper()]
