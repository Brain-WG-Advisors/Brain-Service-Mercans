# -*- coding: utf-8 -*-
"""US Wage Type Catalogue - common helpers (facts, tags, text guards, gaps, DD / spec inventory).

Every factual value written into the workbook comes from a facts file in _research/ through the
tag helpers; nothing is typed by hand. The generator (build_wtc.py) is the only source of the
workbook (C71): a correction goes into wtc_*.py, never into the .xlsx.

Read-only inputs: _pipeline/build-manifest.json, scope_manifest.json, _research/*-facts.json,
00-official-sources/legal-basis-register.csv, the approved DD and the 20 approved Report Specs,
the CZ catalogue template and the Global WTC in ~/mercans-pipeline/shared/.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
WTCDIR = os.path.dirname(HERE)
BASE = os.path.dirname(WTCDIR)
RESEARCH = os.path.join(BASE, "_research")
SPECS = os.path.join(BASE, "04-reports-spec")
DDDIR = os.path.join(BASE, "05-data-dictionary")
CHECKS = os.path.join(HERE, "checks")
BACKUP = os.path.join(HERE, "_backup")
SHARED = os.path.expanduser("~/mercans-pipeline/shared")
TEMPLATE = os.path.join(SHARED, "_CZ_Wage_Type_Catalogue_V2_0.xlsx")
GLOBAL_WTC = os.path.join(SHARED, "Global_WTC_V1_0.xlsx")

sys.path.insert(0, os.path.join(DDDIR, "_build"))
import dd_common as D  # noqa: E402  (loads us_common as D.C)

C = D.C
MANIFEST = C.MANIFEST
PKG = MANIFEST["package"]["version"]
ISSUE = C.ISSUE
AUTHOR = MANIFEST["package"]["issued_by"]
STATUS = "For QA" if "placeholder" in str(MANIFEST["package"].get("_note", "")).lower() else "Issued"   # QA SIR r1 item 18: release sets "Issued"
YEAR = MANIFEST["year"]
CODE = MANIFEST["code"]
COUNTRY = MANIFEST["country"]
WTC_ID = f"{CODE}-WTC-001"
FILENAME = f"{WTC_ID}-v{PKG}.xlsx"
DD_REF = D.DD_REF
CCG_REF = C.CCG_REF
STATE_NAMES = C.STATE_NAMES
STATES = C.STATES
REG = D.REG
USED = C.USED


def at(label):
    C.at(label)


# ----------------------------------------------------------------------------- facts ---
def periods(key):
    """All dated values of a key (all facts files), newest first, duplicates (same date and value) removed."""
    es = C.FACTS.get(key)
    if not es:
        raise KeyError(f"no fact {key!r}")
    es = sorted(es, key=lambda f: 0 if str(f.get("_file", "")).startswith("WTC-") else 1)   # WTC facts files carry the current register ids
    seen = {}
    for f in es:
        seen.setdefault((f.get("effective_from"), json.dumps(f["value"])), f)
    y0, y1 = f"{YEAR}-01-01", f"{YEAR}-12-31"

    def order(f):
        a_, b_ = f.get("effective_from") or "0000", f.get("effective_to") or "9999"
        inyear = a_ <= y1 and b_ >= y0
        return (0 if inyear else (1 if a_ > y1 else 2), a_)
    return sorted(seen.values(), key=order)


TABLE_BOX12 = os.path.join(BASE, "00-official-sources", "code-tables", "US-W2-box12.json")


def rq08(text_when_open=None):
    """Reporting code table sentence: the IRS table is held (checked) or the limitation WTC-RQ-08."""
    if os.path.exists(TABLE_BOX12):
        return "the reporting codes are tested against the IRS Form W-2 box 12 code table (US-FEDS5-007)"
    return gap("WTC-RQ-08", "no code table of the annual wage statement is held for the build year")


def has(key):
    return key in C.FACTS


def tagf(f):
    """[[FACT:key=value]] of one dated fact (period-aware: never collapses the periods of a key)."""
    key = f["key"]
    v = f["value"]
    if "]" in str(v) or "\n" in str(v):
        raise ValueError(f"{key}: value cannot be written as a tag")
    C.USED.setdefault(f"{key}@{f.get('effective_from')}", set()).add(C._CUR[0])
    return f"[[FACT:{key}={C.fmt_value(v)}]]"


def unit_suffix(f):
    v = f["value"]
    if isinstance(v, bool) or not isinstance(v, (int, float)):
        return ""
    u = f.get("unit_of_measure")
    if u == "percent":
        return "%"
    if u == "ratio":
        return " (ratio)"
    if u:
        return " " + u
    if f.get("currency"):
        return " " + f["currency"]
    return ""


def vtxt(f):
    return tagf(f) + unit_suffix(f)


def eff_txt(f):
    a, b = f.get("effective_from"), f.get("effective_to")
    if f.get("_effective_from_basis"):
        return "in force for the build year; the source carries no effective date"
    if a and b:
        return f"effective {a} to {b}"
    if a:
        return f"effective from {a}"
    return ""


def cur(key):
    """The fact of `key` in force in the build year (else the newest period)."""
    ps = periods(key)
    y1 = f"{YEAR}-12-31"
    inyear = [f for f in ps if (f.get("effective_from") or "0000") <= y1 and (f.get("effective_to") or "9999") >= f"{YEAR}-01-01"]
    return (inyear or ps)[0]


def rid(key):
    return cur(key)["register_id"]


def rids(key):
    out = []
    for f in periods(key):
        for r in [f["register_id"]] + list(f.get("_also_register_ids") or []):
            if r not in out:
                out.append(r)
    return out


def val(key):
    """Tagged value (with unit); a key with several periods renders every period with its dates."""
    ps = periods(key)
    if len(ps) == 1:
        return vtxt(ps[0])
    return "; ".join(f"{vtxt(f)} ({eff_txt(f)})" for f in ps)


def line(key, label=None, rid_=True, dates=True):
    """'label: value [register id] (effective ...)' for every period of the key, tagged."""
    ps = periods(key)
    lab = label or humanize(key)
    parts = []
    for f in ps:
        t = f"{vtxt(f)}"
        if rid_:
            t += f" [{f['register_id']}]"
        if dates and eff_txt(f):
            t += f" ({eff_txt(f)})"
        parts.append(t)
    return f"{lab}: " + "; ".join(parts)


TOKENS = {"wh": "withholding", "sit": "state income tax", "pit": "personal income tax", "sui": "unemployment insurance",
          "ui": "unemployment insurance", "std": "standard", "pfml": "paid family and medical leave",
          "tdi": "temporary disability insurance", "sdi": "state disability insurance", "fli": "family leave insurance",
          "famli": "family and medical leave insurance", "pfl": "paid family leave", "dbl": "disability benefits law",
          "nra": "nonresident alien", "bik": "benefit in kind", "obbba": "2025 tips and overtime act", "gtl": "group-term life",
          "hoh": "head of household", "mfj": "married filing jointly", "wc": "workers compensation",
          "lst": "local services tax", "eit": "earned income tax", "opt": "occupational privilege tax",
          "mbt": "modified business tax", "mctmt": "metropolitan commuter transportation mobility tax",
          "rsf": "reemployment services fund", "tcsf": "unemployment compensation fund levy",
          "etia": "employment training and innovation assessment", "ett": "employment training tax",
          "wbf": "workers benefit fund", "shs": "supplemental housing services", "pfa": "preschool for all",
          "esa": "employment security administration", "emac": "employment and marketing assessment",
          "wtf": "workforce training fund", "upaf": "unemployment programme administration fund",
          "daca": "dislocated worker adjustment assessment", "jda": "job development assessment",
          "cep": "career enhancement programme", "abcr": "base contribution rate", "nonres": "nonresident",
          "gi": "gross income", "ee": "employee", "er": "employer", "w4": "withholding certificate",
          "iwo": "income withholding order", "ccpa": "consumer credit protection act", "fica": "FICA", "futa": "FUTA",
          "oasdi": "social security (OASDI)", "fit": "federal income tax", "125": "cafeteria plan"}


def humanize(key):
    parts = key.split(".")[1:]
    out = []
    for p in parts:
        for w in p.split("_"):
            out.append(TOKENS.get(w, w))
    s = " ".join(out)
    return s[:1].upper() + s[1:] if s else key


def clean(text):
    """Guard on every string written: no residual markers (shared C29 HARD list), no pipeline wording, no internal paths."""
    s = str(text)
    h = D.hard_hits(s)
    if h:
        raise ValueError(f"residual marker {h} in: {s[:140]}")
    C.clean(s)
    m = C.PATH_RX.search(s)
    if m:
        raise ValueError(f"internal path {m.group(0)!r} in: {s[:140]}")
    return s


# ----------------------------------------------------------------------------- gaps ---
# Residual keys of the R2 facts: proven only in part (derived, multi-source or unlocated). Printed as the neutral gap, no figure.
RESIDUAL = {
    "ma.pfml.family.rate": ("WTC-RQ-10", "the Massachusetts paid family and medical leave rates are derived from a split that the source does not print"),
    "ma.pfml.medical.rate": ("WTC-RQ-10", "the Massachusetts paid family and medical leave rates are derived from a split that the source does not print"),
    "ma.sui.rate_schedule.table": ("WTC-RQ-11", "one cell of the Massachusetts unemployment insurance rate schedule is not located in the stored copy"),
}
GAPS = {}       # id -> dict(subject, close, key, domain, severity, blocking)
GAP_USED = {}   # id -> locations


def gap_def(gid, subject, close, key, domain="social_security", severity="minor", blocking=False, unresolved=None):
    GAPS[gid] = dict(subject=subject, close=close, key=key, domain=domain, severity=severity, blocking=blocking,
                     unresolved=unresolved or [])


def gap(gid, what=None):
    """Neutral limitation cell text: 'Not configured in this release [[GAP:WTC-RQ-nn]]: <what>'."""
    if gid not in GAPS:
        raise KeyError(f"gap {gid} not defined")
    GAP_USED.setdefault(gid, set()).add(C._CUR[0])
    t = f"Not configured in this release [[GAP:{gid}]]"
    if what:
        t += f": {what}"
    return t


_UNRES = None


def unresolved():
    """unresolved[] entries of the two WTC facts files, by key."""
    global _UNRES
    if _UNRES is None:
        _UNRES = {}
        for fn in ("WTC-global_baseline-facts.json", "WTC-country_specific-facts.json"):
            for u in json.load(open(os.path.join(RESEARCH, fn), encoding="utf-8")).get("unresolved", []):
                _UNRES[u["key"]] = u
    return _UNRES


UG = {}         # unresolved key -> gap id (ids are allocated in order of first use)
UG_TEXT = {}    # unresolved key -> wording written in the cell (author override of the sanitised reason)


def ug(key, what):
    """Gap for an open item of the facts (unresolved[]): id allocated on first use, request carries the open item."""
    u = unresolved()[key]
    if key not in UG:
        gid = f"WTC-RQ-{len(UG) + 20:02d}"
        UG[key] = gid
        gap_def(gid, u.get("why") or what, u.get("what_would_close_it") or "the official source that states it", key,
                domain=("income_tax" if ".sit." in key or ".pit." in key else "social_security"),
                severity="major" if u.get("blocking") else "minor", blocking=False, unresolved=[key])
        GAPS[gid]["facts_blocking"] = bool(u.get("blocking"))
    return gap(UG[key], what)


def gaptag(gid):
    if gid not in GAPS:
        raise KeyError(f"gap {gid} not defined")
    GAP_USED.setdefault(gid, set()).add(C._CUR[0])
    return f"[[GAP:{gid}]]"


# ------------------------------------------------------------------------ DD inventory ---
_DD_NAMES = None


def dd_names():
    """Field Names of the approved DD (ID Information col C, Country Fields col D), read-only."""
    global _DD_NAMES
    if _DD_NAMES is None:
        from openpyxl import load_workbook
        wb = load_workbook(os.path.join(DDDIR, f"{CODE}-DD-001-v{PKG}.xlsx"), read_only=True)
        names = []
        for sh, col in (("ID Information", 3), ("Country Fields", 4)):
            for row in wb[sh].iter_rows(min_row=5, values_only=True):
                if len(row) < col or not row[col - 1]:
                    continue
                v = str(row[col - 1])
                if v == "Field Name":
                    continue
                names.append(v)
        _DD_NAMES = names
    return _DD_NAMES


def dd(name):
    """A DD element name, verified against the approved DD (F25: never cite a field that does not exist)."""
    if name not in dd_names():
        raise KeyError(f"DD element {name!r} not in {DD_REF}")
    return name
