# -*- coding: utf-8 -*-
"""US Report Specifications - common helpers (facts, tags, text, channel classification).

Every number or factual value written into a workbook comes from a facts file in
_research/ through tag() / tagv(); nothing is typed by hand. The generator is the only
source of the workbooks (C71): a correction goes here or into the definitions, never
into the .xlsx.
"""
import csv
import datetime as dt
import glob
import json
import os
import re
import sys
from decimal import Decimal, ROUND_HALF_UP

HERE = os.path.dirname(os.path.abspath(__file__))
SPECS = os.path.dirname(HERE)
BASE = os.path.dirname(SPECS)
RESEARCH = os.path.join(BASE, "_research")

# shared library (read-only): mercans_spec
_LIB = os.environ.get("MERCANS_SPEC_LIB") or os.path.expanduser("~/mercans-pipeline/shared/spec-builder")
if _LIB not in sys.path:
    sys.path.insert(0, _LIB)

MANIFEST = json.load(open(os.path.join(BASE, "_pipeline", "build-manifest.json"), encoding="utf-8"))
PKG = MANIFEST["package"]["version"]
ISSUE = dt.datetime.strptime(MANIFEST["package"]["issue_date"], "%Y-%m-%d")
AUTHOR = MANIFEST["package"]["issued_by"]
YEAR = MANIFEST["year"]
CODE = MANIFEST["code"]
DD_REF = f"{CODE}-DD-001 v{PKG}"
CCG_REF = f"{CODE}-CCG-001 v{PKG}"
SCOPE = json.load(open(os.path.join(BASE, "scope_manifest.json"), encoding="utf-8"))

STATE_NAMES = {
    "AK": "Alaska", "AL": "Alabama", "AR": "Arkansas", "AZ": "Arizona", "CA": "California",
    "CO": "Colorado", "CT": "Connecticut", "DC": "District of Columbia", "DE": "Delaware",
    "FL": "Florida", "GA": "Georgia", "HI": "Hawaii", "IA": "Iowa", "ID": "Idaho", "IL": "Illinois",
    "IN": "Indiana", "KS": "Kansas", "KY": "Kentucky", "LA": "Louisiana", "MA": "Massachusetts",
    "MD": "Maryland", "ME": "Maine", "MI": "Michigan", "MN": "Minnesota", "MO": "Missouri",
    "MS": "Mississippi", "MT": "Montana", "NC": "North Carolina", "ND": "North Dakota",
    "NE": "Nebraska", "NH": "New Hampshire", "NJ": "New Jersey", "NM": "New Mexico", "NV": "Nevada",
    "NY": "New York", "OH": "Ohio", "OK": "Oklahoma", "OR": "Oregon", "PA": "Pennsylvania",
    "RI": "Rhode Island", "SC": "South Carolina", "SD": "South Dakota", "TN": "Tennessee",
    "TX": "Texas", "UT": "Utah", "VA": "Virginia", "VT": "Vermont", "WA": "Washington",
    "WI": "Wisconsin", "WV": "West Virginia", "WY": "Wyoming",
}
STATES = sorted(STATE_NAMES)

# ------------------------------------------------------------------ facts ---
FACTS = {}          # key -> [fact dict, ...] (all files, all periods)
RSPEC_KEYS = []     # keys of RSPEC-facts.json in file order
for _fp in sorted(glob.glob(os.path.join(RESEARCH, "*-facts.json"))):
    _src = os.path.basename(_fp)
    for _f in json.load(open(_fp, encoding="utf-8")).get("facts", []):
        _f = dict(_f)
        _f["_file"] = _src
        FACTS.setdefault(_f["key"], []).append(_f)
        if _src == "RSPEC-facts.json":
            RSPEC_KEYS.append(_f["key"])

_RS = json.load(open(os.path.join(RESEARCH, "RSPEC-facts.json"), encoding="utf-8"))
UNRESOLVED = {u["key"]: u for u in _RS.get("unresolved", [])}
_G = json.load(open(os.path.join(RESEARCH, "gaps.json"), encoding="utf-8"))
RSPEC_GAPS = {g["key"]: g for g in _G.get("RSPEC", {}).get("gaps", [])}

USED = {}           # key -> set(locations) (binding log)
_CUR = ["?"]        # current location label for the binding log


def at(label):
    _CUR[0] = label


def fact(key, period=None):
    """The fact entry of `key` for the build year (or for `period` = 'YYYY' or an
    effective_from date). RSPEC-facts.json wins over other files for the same key/period."""
    es = FACTS.get(key)
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
            cand = es
    if not cand:
        raise KeyError(f"no fact {key!r} for period {period!r}")
    cand.sort(key=lambda f: (f["_file"] != "RSPEC-facts.json"))
    return cand[0]


def fmt_value(v):
    if isinstance(v, bool):
        return str(v)
    if isinstance(v, int):
        return f"{v:,}"
    if isinstance(v, float):
        if v.is_integer() and abs(v) >= 1000:
            return f"{int(v):,}"
        s = repr(v)
        return s
    return str(v)


def num(key, period=None):
    v = fact(key, period)["value"]
    if isinstance(v, bool) or not isinstance(v, (int, float)):
        raise TypeError(f"{key} is not numeric: {v!r}")
    return Decimal(str(v))


def tag(key, period=None):
    f = fact(key, period)
    if "]" in str(f["value"]):
        raise ValueError(f"{key}: value contains ']' and cannot be written as a [[FACT:]] tag")
    USED.setdefault(key if not period else f"{key}@{f.get('effective_from')}", set()).add(_CUR[0])
    return f"[[FACT:{key}={fmt_value(f['value'])}]]"


def note_use(key, period=None):
    """Record a location whose content is derived field by field from the value of `key`
    (a line map or record layout rendered row by row). The full tagged value is written
    once in the same workbook; the binding log keeps every derived location."""
    f = fact(key, period)
    USED.setdefault(key if not period else f"{key}@{f.get('effective_from')}", set()).add(_CUR[0])
    return f


def is_draft(key, period=None):
    """True when the fact rests on an IRS early-release draft (note of the fact)."""
    return "DRAFT" in str(fact(key, period).get("note") or "")


def per_draft(key, period=None):
    """Neutral marker for a value read from an IRS 2026 early-release draft."""
    return (" Per 2026 draft: read from the IRS early-release draft of the 2026 form or instructions; "
            "re-verify against the final 2026 revision before go-live.") if is_draft(key, period) else ""


_NUMTOK = r"(?<![\d,.\w]){}(?!\d|,\d|\.\d)"


def retag(text, keys, period=None):
    """Replace each plain occurrence of the formatted value of `keys` in `text` by its tag,
    so that a figure quoted inside a rendered line label is still a bound fact."""
    out = str(text)
    for k in keys:
        f = fact(k, period)
        v = fmt_value(f["value"])
        pieces = re.split(r"(\[\[(?:FACT|GAP):[^\]]*\]\])", out)
        rx = re.compile(_NUMTOK.format(re.escape(v)))
        for i in range(0, len(pieces), 2):
            if rx.search(pieces[i]):
                pieces[i] = rx.sub(lambda m: tag(k, period), pieces[i])
        out = "".join(pieces)
    return out


def quote(key, period=None):
    """Value of a fact that cannot be tagged (it contains square brackets), quoted with
    parentheses instead and cited by register id; the location is logged as derived."""
    f = note_use(key, period)
    v = str(f["value"]).replace("[", "(").replace("]", ")")
    return f"{v} [{f['register_id']}]"


def rid(key, period=None):
    return fact(key, period)["register_id"]


def url(key, period=None):
    return fact(key, period).get("url") or ""


def src(key, period=None):
    """'[US-XXX-NNN]' + source type + URL, for column M."""
    f = fact(key, period)
    kind = ("Official spec" if "artifact inspection" in str(f.get("verification_method", ""))
            else "Web research (official authority page)")
    u = f.get("url") or ""
    return f"[{f['register_id']}] Source type: {kind}. {u}".strip()


def tagr(key, period=None):
    """tag + register id citation."""
    return f"{tag(key, period)} [{rid(key, period)}]"


def gap(key_or_id):
    """[[GAP:id]] for a known RSPEC limitation key, a partial request key, or a builder request id."""
    from us_gaps import PARTIAL
    if key_or_id in PARTIAL:
        return f"[[GAP:{PARTIAL[key_or_id]}]]"
    if key_or_id in RSPEC_GAPS:
        return f"[[GAP:{RSPEC_GAPS[key_or_id]['id']}]]"
    return f"[[GAP:{key_or_id}]]"


def gap_close(key):
    from us_gaps import TEXT
    return TEXT[key][1]


def gap_subject(key):
    from us_gaps import TEXT
    return TEXT[key][0]


def limitation(key, lead="Layout not configured in this release"):
    return f"{lead} {gap(key)}: {gap_subject(key)}. Closes with: {gap_close(key)}."


# ---------------------------------------------------------------- numbers ---
CENT = Decimal("0.01")


def money(x):
    return Decimal(x).quantize(CENT, rounding=ROUND_HALF_UP)


def m2(x):
    return f"{money(x):,.2f}"


def pct(key, period=None):
    """rate stored in percent -> Decimal fraction."""
    return num(key, period) / Decimal(100)


# ----------------------------------------------------------- channel class ---
PORTALS = [
    "eGov", "Tax21", "ATAP", "AZTaxes", "AZFSET", "DES Tax and Wage System", "e-Services for Business",
    "Revenue Online", "myconneCT", "ReEmployCT", "MyTax.DC.gov", "DOES ESSP", "ESSP", "Delaware Taxpayer Portal",
    "Delaware LaborFirst", "GTC", "HTO", "GovConnectIowa", "myIowaUI", "TAP", "MyTax", "INTIME", "UPLINK",
    "KUIP", "MyTaxes", "LaTAP", "LaWage", "LAWATS", "MassTaxConnect", "BEACON", "ReEmployME", "MTO", "MiUI",
    "UInteract", "NCSUITS", "eNC3", "UI EASY", "NebFile", "NEworks", "WebTax", "My Nevada Tax", "ESS",
    "OkTAP", "EZ Tax Express", "Frances Online", "iWire", "Portland Revenue Online", "myPATH", "Tax Portal",
    "SUITS", "Employer e-Services", "Unemployment Tax Services", "QuickFile", "myVTax", "EAMS", "SAW",
    "FileLocal", "paidleave.wa.gov", "UI eServices", "ES Tax portal", "myAlaska", "e-Services", "PFML portal",
    "DWD E S S", "OH|TAX", "TWS", "MTA", "Avenu", "Business Services Online", "IRIS",
]


def portals_in(text):
    t = str(text)
    found = []
    for p in sorted(PORTALS, key=len, reverse=True):
        if re.search(rf"(?<![A-Za-z]){re.escape(p)}(?![A-Za-z])", t) and not any(p in q for q in found):
            found.append(p)
    return found


def channel_types(text, xsd=False):
    """Channel classes (online_form / file_upload / xml / api / paper) named by a fact value.
    xml is recorded only where the value cites a published schema or file specification (C23)."""
    t = str(text).lower()
    out = []
    if re.search(r"online|portal|manual|key|data entry|e-services|web|single entry|entry", t):
        out.append("online_form")
    if re.search(r"upload|csv|efw2|icesa|mmref|txt|file|sftp|ftp|bulk|delimited|fixed|excel|xlsx|template|import", t):
        out.append("file_upload")
    if xsd and re.search(r"\bxml\b", t):
        out.append("xml")
    if re.search(r"web service|\bapi\b|fset", t):
        out.append("api")
    if re.search(r"paper|mail|fax|cd/dvd|cd\b|coupon|voucher", t):
        out.append("paper")
    return out


# ------------------------------------------------------------ text checks ---
C29 = re.compile(r"\[placeholder\]|\bplaceholder\b|\bTODO\b|\bTBD\b|\bFIXME\b|\bXXX\b|VERIFY No\.|"
                 r"\bto be confirmed\b|\bto be verified\b|<insert\b", re.I)
PIPELINE_WORDS = re.compile(r"\b(Stage \d|Synthesis|facts file|research pack|register row|tier-?B|MANUAL row|"
                            r"PENDING|browser pass|VPN|fan-out|RESEARCH-GAP|agent 2|builder|_research|_pipeline|"
                            r"build-manifest|scope_manifest|\.json\b|US exit)", re.I)


def clean(text):
    """Guard on every string written: no residual markers, no pipeline wording."""
    s = str(text)
    bare = re.sub(r"\[\[(?:FACT|GAP):[^\]]*\]\]", " ", s)
    m = C29.search(bare) or PIPELINE_WORDS.search(bare)
    if m:
        raise ValueError(f"forbidden wording {m.group(0)!r} in: {s[:160]}")
    return s
