# -*- coding: utf-8 -*-
"""US Regulation Design - common helpers.

Every value written into the design comes from a facts file in _research/ through T() (a [[FACT:key=value]]
tag); nothing numeric is typed by hand. WTC codes and DD field names are verified against the approved
workbooks when they are written (W() and D()). The generator (build_design.py) is the only source of the
document: a correction goes into the generator, never into the .md.
Read-only inputs: build-manifest.json, *-facts.json, the WTC and DD workbooks, gaps.json.
"""
import csv
import glob
import json
import os
import re
import sys
from decimal import Decimal

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
DESDIR = os.path.dirname(HERE)
BASE = os.path.dirname(DESDIR)
RESEARCH = os.path.join(BASE, "_research")
CHECKS = os.path.join(HERE, "checks")

MANIFEST = json.load(open(os.path.join(BASE, "_pipeline", "build-manifest.json"), encoding="utf-8"))
PKG = MANIFEST["package"]["version"]
ISSUE = MANIFEST["package"]["issue_date"]
AUTHOR = MANIFEST["package"]["issued_by"]
YEAR = MANIFEST["year"]
CODE = MANIFEST["code"]
STATUS = "For QA"
FILENAME = f"{CODE}_Regulation_Design_v{PKG}.md"

STATE_NAMES = {
    "AL": "Alabama", "AK": "Alaska", "AZ": "Arizona", "AR": "Arkansas", "CA": "California", "CO": "Colorado",
    "CT": "Connecticut", "DE": "Delaware", "DC": "District of Columbia", "FL": "Florida", "GA": "Georgia",
    "HI": "Hawaii", "ID": "Idaho", "IL": "Illinois", "IN": "Indiana", "IA": "Iowa", "KS": "Kansas",
    "KY": "Kentucky", "LA": "Louisiana", "ME": "Maine", "MD": "Maryland", "MA": "Massachusetts",
    "MI": "Michigan", "MN": "Minnesota", "MS": "Mississippi", "MO": "Missouri", "MT": "Montana",
    "NE": "Nebraska", "NV": "Nevada", "NH": "New Hampshire", "NJ": "New Jersey", "NM": "New Mexico",
    "NY": "New York", "NC": "North Carolina", "ND": "North Dakota", "OH": "Ohio", "OK": "Oklahoma",
    "OR": "Oregon", "PA": "Pennsylvania", "RI": "Rhode Island", "SC": "South Carolina", "SD": "South Dakota",
    "TN": "Tennessee", "TX": "Texas", "UT": "Utah", "VT": "Vermont", "VA": "Virginia", "WA": "Washington",
    "WV": "West Virginia", "WI": "Wisconsin", "WY": "Wyoming"}
STATES = sorted(STATE_NAMES)


# ------------------------------------------------------------------ facts
def _rank(path):
    n = os.path.basename(path)
    return (1 if n.startswith("CCG-") else 0, n)


FACTS = {}
for _fp in sorted(glob.glob(os.path.join(RESEARCH, "*-facts.json")), key=_rank):
    for _f in json.load(open(_fp, encoding="utf-8")).get("facts", []):
        _f = dict(_f)
        _f["_file"] = os.path.basename(_fp)
        FACTS.setdefault(_f["key"], []).append(_f)

REG = {r["id"]: r for r in csv.DictReader(
    open(os.path.join(BASE, "00-official-sources", "legal-basis-register.csv"), encoding="utf-8"))}
GAPS = {g["id"]: g for g in json.load(open(os.path.join(RESEARCH, "gaps.json"), encoding="utf-8"))["gaps"]}

USED = []      # (location, key, register_id)
USED_GAPS = set()
_CUR = ["?"]


def at(label):
    _CUR[0] = label


def entries(key):
    """Distinct dated entries of a key, in date order."""
    seen, out = set(), []
    for f in FACTS.get(key, []):
        sig = (str(f.get("value")), f.get("effective_from"), f.get("effective_to"))
        if sig in seen:
            continue
        seen.add(sig)
        out.append(f)
    out.sort(key=lambda f: (f.get("effective_from") or "0000"))
    return out


def has(key):
    return key in FACTS


def fact(key, period=None):
    """Entry of `key` for the build year, or for `period` ('YYYY' or an effective_from date)."""
    es = entries(key)
    if not es:
        raise KeyError(f"no fact {key!r}")
    if period:
        p = str(period)
        cand = [f for f in es if str(f.get("effective_from") or "").startswith(p)]
        if not cand and len(p) == 4:
            cand = [f for f in es if (f.get("effective_from") or "0000")[:4] <= p <= (f.get("effective_to") or "9999")[:4]]
        if not cand:
            raise KeyError(f"no fact {key!r} for period {period!r}")
        return cand[0]
    y0, y1 = f"{YEAR}-01-01", f"{YEAR}-12-31"
    cand = [f for f in es if (f.get("effective_from") or "0000") <= y1 and (f.get("effective_to") or "9999") >= y0]
    if not cand:
        cand = es
    return cand[-1]


def fmt_value(f):
    v = f["value"]
    if isinstance(v, bool):
        return str(v)
    if isinstance(v, str):
        return v
    if isinstance(v, int):
        return f"{v:,}"
    d = Decimal(repr(v)).normalize()
    if f.get("currency") and not f.get("unit_of_measure") and -d.as_tuple().exponent <= 2:
        return f"{v:,.0f}" if float(v).is_integer() else f"{v:,.2f}"
    s = format(d, "f")
    if "." in s:
        a, b = s.split(".")
        return f"{int(a):,}.{b}"
    return f"{int(s):,}"


def tag(key, period=None, f=None):
    f = f or fact(key, period)
    v = fmt_value(f)
    if isinstance(f["value"], str) and (("]" in v) or ("|" in v) or ("\n" in v)):
        raise ValueError(f"{key}: value cannot be written as a tag")
    USED.append((_CUR[0], key + (f"@{f.get('effective_from')}" if period else ""), f.get("register_id")))
    return f"[[FACT:{key}={v}]]"


UNIT_SUFFIX = {"percent": "%", "days": " days", "hours": " hours", "weeks": " weeks", "months": " months",
               "employees": " employees", "years": " years"}


def T(key, period=None, f=None):
    """Tagged value with its unit: percent -> tag%, days/hours/... -> tag unit, USD amount -> USD tag."""
    f = f or fact(key, period)
    t = tag(key, period, f)
    u = f.get("unit_of_measure")
    v = f["value"]
    if isinstance(v, (int, float)) and not isinstance(v, bool):
        if u in UNIT_SUFFIX:
            return t + UNIT_SUFFIX[u]
        if u:
            return f"{t} {u}"
        if f.get("currency"):
            return f"{f['currency']} {t}"
    return t


def period_label(f):
    a, b = f.get("effective_from"), f.get("effective_to")
    if a and b:
        return f"{a} to {b}"
    return f"from {a}" if a else "no start date"


def regid(key, period=None):
    return fact(key, period)["register_id"]


def G(gid):
    if gid not in GAPS and not gid.startswith("DESIGN-RQ-"):
        raise KeyError(f"gap {gid} not in gaps.json")
    USED_GAPS.add(gid)
    return f"[[GAP:{gid}]]"


def NC(gid):
    return f"Not configured in this release {G(gid)}"


# ----------------------------------------------------------------- WTC / DD
from openpyxl import load_workbook  # noqa: E402

WTC_PATH = glob.glob(os.path.join(BASE, "02-wtc", "*.xlsx"))[0]
DD_PATH = glob.glob(os.path.join(BASE, "05-data-dictionary", "*.xlsx"))[0]
WTC = {}
_ws = load_workbook(WTC_PATH, read_only=True)["Wage Type Catalogue"]
for _r in _ws.iter_rows(min_row=2, values_only=True):
    if _r[0] and _r[0] != "Mercans Code":
        WTC[str(_r[0])] = {"name": _r[1], "category": _r[4], "tax_code": _r[6]}
DDF = {}
_wd = load_workbook(DD_PATH, read_only=True)
for _sn, _off in (("ID Information", 0), ("Country Fields", 1)):
    for _r in _wd[_sn].iter_rows(min_row=5, values_only=True):
        nm = _r[_off + 2] if len(_r) > _off + 2 else None
        if nm and nm != "Field Name":
            DDF[nm] = _sn
WTCREF = {}
DDREF = {}
REGREF = {}


def W(code):
    """WTC reference written `US-001` (verified against the workbook)."""
    code = str(code)
    if code not in WTC:
        raise KeyError(f"WTC code {code} not in the workbook")
    WTCREF.setdefault(code, set()).add(_CUR[0])
    return f"`{code}`"


def Wg(code):
    """Global WTC code, written WTC `21900`."""
    code = str(code)
    if code not in WTC:
        raise KeyError(f"WTC code {code} not in the workbook")
    WTCREF.setdefault(code, set()).add(_CUR[0])
    return f"WTC `{code}`"


def D(name):
    """DD field reference written DD:`Field name` (verified)."""
    if name not in DDF:
        raise KeyError(f"DD field {name!r} not in the dictionary")
    DDREF.setdefault(name, set()).add(_CUR[0])
    return f"DD:`{name}`"


def R(rid):
    if rid not in REG:
        raise KeyError(f"register id {rid} not in the register")
    REGREF.setdefault(rid, set()).add(_CUR[0])
    return f"[{rid}]"


# ----------------------------------------------------------------- guards
HARD_CS = [r"\bTODO\b", r"\bTBD\b", r"\bFIXME\b", r"\bVERIFY\s+No\b", r"RESEARCH-GAP", r"\?\?\?", r"\bXXX\b"]
HARD_CI = [r"\[\s*placeholder\s*\]", r"\[\s*CHECK\s*\]", r"\[\s*\?\s*\]", r"to be confirmed", r"to be verified",
           r"lorem ipsum"]
PIPELINE_WORDS = re.compile(r"\b(Stage \d|Synthesis|facts file|research pack|register row|tier-?B|MANUAL row|PENDING|"
                            r"browser pass|VPN|fan-out|agent 2|builder|_research|_pipeline|build-manifest|"
                            r"scope_manifest|US exit|QA r\d|round \d|corrected on|changelog|C\d\d\b)", re.I)
PATH_RX = re.compile(r"00-official-sources|_research/|_pipeline/|\.json\b|\.py\b|[A-Za-z]:\\")
ANYTAG = re.compile(r"\[\[(?:FACT|GAP):[^\]]*\]\]")


def hard_hits(text):
    out = [p for p in HARD_CS if re.search(p, text)]
    return out + [p for p in HARD_CI if re.search(p, text, re.I)]


def clean(text):
    s = str(text)
    bare = ANYTAG.sub(" ", s)
    h = hard_hits(bare)
    if h:
        raise ValueError(f"residual marker {h} in: {s[:140]}")
    m = PIPELINE_WORDS.search(bare)
    if m:
        raise ValueError(f"pipeline wording {m.group(0)!r} in: {s[:140]}")
    if PATH_RX.search(bare):
        raise ValueError(f"internal path in: {s[:140]}")
    return s


def cell(s):
    """Table cell text: no pipe, no newline."""
    return str(s).replace("|", "/").replace("\n", " ").strip()
