# -*- coding: utf-8 -*-
"""US Payslip (PSL) - common helpers: facts (PSL first), tags, F44 gate, gap registry, binding log, text guards.

Every factual value written into the workbook comes from a facts file in _research/ through fv() / tag() / pick();
nothing is typed by hand. build_psl.py is the only source of the workbook: a correction goes into psl_content.py /
build_psl.py, never into the .xlsx.
Facts priority for a key present in several files: PSL, WTC, DD, SIR, RSPEC, CCG last (period-aware).
"""
import csv
import json
import os
import re
import sys
from decimal import Decimal

HERE = os.path.dirname(os.path.abspath(__file__))
PSLDIR = os.path.dirname(HERE)
BASE = os.path.dirname(PSLDIR)
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
STATUS = "For QA"                       # owner default until release
YEAR = MANIFEST["year"]
CODE = MANIFEST["code"]
COUNTRY = MANIFEST["country"]
STATE_NAMES = C.STATE_NAMES
PSL_ID = f"{CODE}-PSL-001"
FILENAME = f"{CODE}_Compliance_Payslip_Generator.xlsx"
DD_REF = f"{CODE}-DD-001 v{PKG}"
CCG_REF = f"{CODE}-CCG-001 v{PKG}"
WTC_REF = f"{CODE}-WTC-001 v{PKG}"
REGISTER = os.path.join(BASE, "00-official-sources", "legal-basis-register.csv")
REG = {r["id"]: r for r in csv.DictReader(open(REGISTER, encoding="utf-8"))}
PSLFACTS = json.load(open(os.path.join(RESEARCH, "PSL-facts.json"), encoding="utf-8"))
UNRESOLVED = {u["key"]: u for u in PSLFACTS.get("unresolved", [])}
OPEN_KEYS = set(UNRESOLVED)

PRIORITY = ["PSL-facts.json", "WTC-country_specific-facts.json", "WTC-global_baseline-facts.json",
            "DD-8_sheets-facts.json", "SIR-facts.json", "RSPEC-facts.json"]


def _prio(f):
    n = f["_file"]
    if n in PRIORITY:
        return PRIORITY.index(n)
    return 10 if n.startswith("CCG-") else 20


USED = {}            # (key, effective_from) -> set(locations)
_CUR = ["?"]
GAPS = {}            # key -> record
BLOCKED = {}         # key -> missing elements (F44)
_F44 = {}
GAP_IDS = {}


def at(label):
    _CUR[0] = label


def fact(key, period=None):
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
    return cand[0]


def has(key):
    return key in C.FACTS


def fmt(v):
    return C.fmt_value(v)


def num(key, period=None):
    return Decimal(str(fact(key, period)["value"]))


def f44_miss(f):
    ck = (f["key"], f.get("effective_from"), f["register_id"], str(f["value"]))
    if ck not in _F44:
        _F44[ck] = f44_lib.check_fact(f)
    return _F44[ck]


def rids(f):
    return [f["register_id"]] + [r for r in (f.get("_also_register_ids") or []) if r != f["register_id"]]


def cite_f(f):
    return " ".join(f"[{r}]" for r in rids(f))


def eff_f(f):
    a, b = f.get("effective_from"), f.get("effective_to")
    if f.get("_effective_from_basis"):
        return f"in force for {YEAR}; the source carries no effective date"
    if a and b:
        return f"effective {a} to {b}"
    if a:
        return f"effective from {a}"
    return ""


def note_use(key, period=None):
    f = fact(key, period)
    USED.setdefault((f["key"], f.get("effective_from")), set()).add(_CUR[0])
    return f


def gap(key, why=None, jur=None):
    g = GAPS.setdefault(key, {"key": key, "why": why, "locations": [], "jurs": set()})
    if _CUR[0] not in g["locations"]:
        g["locations"].append(_CUR[0])
    if why and not g.get("why"):
        g["why"] = why
    if jur:
        g["jurs"].add(jur)
    return f"Not configured in this release [[GAP:{GAP_IDS.get(key, 'PSL-RQ-00')}]]"


def tag(key, period=None):
    f = fact(key, period)
    if "]" in str(f["value"]):
        raise ValueError(f"{key}: value contains ']' and cannot be written as a [[FACT:]] tag")
    note_use(key, period)
    return f"[[FACT:{key}={fmt(f['value'])}]]"


def reg_ok(rid):
    r = REG.get(rid)
    return bool(r) and r.get("tier") not in ("B", "C") and r.get("status") != "MANUAL"


def usable(key, period=None):
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


def render(key, period=None, with_cite=True, with_eff=False, plain=False):
    f = fact(key, period)
    if plain:                                   # printed payslip: label value only, no register id, no effective stamp
        with_cite, with_eff = False, False
    t = tag(key, period)
    u = f.get("unit_of_measure")
    v = f["value"]
    if u and isinstance(v, (int, float)) and not isinstance(v, bool):
        t += "%" if u in ("percent", "%") else f" {u}"
    elif f.get("currency") and isinstance(v, (int, float)) and not isinstance(v, bool):
        t += f" {f['currency']}"
    if with_cite:
        t += f" {cite_f(f)}"
    if not plain and (with_eff or f.get("effective_to")):
        t += f" ({eff_f(f)})"
    if not plain and "DRAFT" in str(f.get("note") or ""):
        t += (" Per 2026 draft: read from the IRS early-release draft of the 2026 form or instructions; "
              "re-verify against the final 2026 revision before go-live.")
    return t


def fv(key, period=None, with_cite=True, with_eff=False, jur=None, plain=False):
    """Tagged fact + unit + register ids. Never unproven text: an open question, or a value whose text elements are not
    found in the local copy of its register row(s), returns the neutral gap text."""
    ok, why = usable(key, period)
    if ok:
        return render(key, period, with_cite, with_eff, plain)
    if isinstance(why, tuple):
        BLOCKED[key] = why[1]
    return gap(key, "f44" if isinstance(why, tuple) else str(why), jur)


def pick(keys, jur=None, gap_key=None, with_cite=True):
    first_blocked = None
    for k in keys:
        ok, why = usable(k)
        if ok:
            return render(k, None, with_cite), k
        if why != "no_fact" and first_blocked is None:
            first_blocked = (k, why)
    if first_blocked:
        k, why = first_blocked
        if isinstance(why, tuple):
            BLOCKED[k] = why[1]
        return gap(k, "f44" if isinstance(why, tuple) else str(why), jur), None
    return gap(gap_key or "psl.unspecified.missing", "missing", jur), None


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


def state_name(code):
    return STATE_NAMES[code.upper()]
