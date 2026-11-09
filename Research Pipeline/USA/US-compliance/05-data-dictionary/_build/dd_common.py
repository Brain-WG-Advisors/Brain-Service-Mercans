# -*- coding: utf-8 -*-
"""US Data Dictionary - common helpers (facts, tags, text guards, spec inventory).

Every factual value written into the workbook comes from a facts file in _research/ through
tag(); nothing is typed by hand. The generator (build_dd.py) is the only source of the workbook:
a correction goes into dd_defs.py / dd_rules.py / build_dd.py, never into the .xlsx.

Read-only inputs: _pipeline/build-manifest.json, _research/*-facts.json, the 20 approved Report
Specs in 04-reports-spec/, the CZ template in ~/mercans-pipeline/shared/.
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
from decimal import Decimal

HERE = os.path.dirname(os.path.abspath(__file__))
DDDIR = os.path.dirname(HERE)
BASE = os.path.dirname(DDDIR)
RESEARCH = os.path.join(BASE, "_research")
SPECS = os.path.join(BASE, "04-reports-spec")
OUT = os.path.join(DDDIR)
CHECKS = os.path.join(HERE, "checks")
SCRATCH = os.path.join(HERE, "_scratch")
SHARED = os.path.expanduser("~/mercans-pipeline/shared")
TEMPLATE = os.path.join(SHARED, "CZ_Data_Dictionary_V2_0.xlsx")

# the Report Spec generator helpers (read-only): fact() / tag() semantics are shared
sys.path.insert(0, os.path.join(SPECS, "_build"))
import us_common as C  # noqa: E402

MANIFEST = C.MANIFEST
PKG = MANIFEST["package"]["version"]
ISSUE = C.ISSUE
AUTHOR = MANIFEST["package"]["issued_by"]
STATUS = "For QA" if "placeholder" in str(MANIFEST["package"].get("_note", "")).lower() else "Issued"   # QA SIR r1 item 18: release sets "Issued"
YEAR = MANIFEST["year"]
CODE = MANIFEST["code"]
COUNTRY = MANIFEST["country"]
DD_ID = f"{CODE}-DD-001"
DD_REF = f"{DD_ID} v{PKG}"
FILENAME = f"{DD_ID}-v{PKG}.xlsx"
STATE_NAMES = C.STATE_NAMES

REG = {r["id"]: r for r in csv.DictReader(
    open(os.path.join(BASE, "00-official-sources", "legal-basis-register.csv"), encoding="utf-8"))}

DDFACTS = json.load(open(os.path.join(RESEARCH, "DD-8_sheets-facts.json"), encoding="utf-8"))
DD_KEYS = [f["key"] for f in DDFACTS["facts"]]
OWNER_SCOPE = {o["key"]: o for o in DDFACTS.get("_owner_scope", [])}

USED = C.USED          # key -> locations (binding log)


def at(label):
    C.at(label)


def fact(key, period=None):
    return C.fact(key, period)


def tag(key, period=None):
    return C.tag(key, period)


def rid(key, period=None):
    f = fact(key, period)
    return f["register_id"]


def eff(key, period=None):
    """Effective-period wording of a fact (period-aware: never collapsed)."""
    f = fact(key, period)
    a, b = f.get("effective_from"), f.get("effective_to")
    basis = f.get("_effective_from_basis")
    if DW.period_status(f) or (basis and b):      # v1.1 QA r1: proposed / historical / own end date
        return DW.period_wording(f, "")
    if basis:
        return f"in force for {YEAR}; the source carries no effective date"
    if a and b:
        return f"effective {a} to {b}"
    if a:
        return f"effective from {a}"
    return ""


def src(key, period=None):
    """Tagged fact + register id + effective period, ready for an Additional Notes cell."""
    f = fact(key, period)
    unit = ""
    v = f.get("value")
    if isinstance(v, (int, float)) and not isinstance(v, bool) and f.get("unit_of_measure"):
        unit = "%" if f["unit_of_measure"] == "percent" else f" {f['unit_of_measure']}"          # unit written from the fact, right after the tag
    cites = " ".join(f"[{r}]" for r in [f["register_id"]] + [x for x in (f.get("_also_register_ids") or []) if x != f["register_id"]])
    return f"{tag(key, period)}{unit} {cites} ({eff(key, period)})"


HARD_CS = [r"\bTODO\b", r"\bTBD\b", r"\bFIXME\b", r"\bVERIFY\s+No\b", r"RESEARCH-GAP", r"\?\?\?"]   # shared v2.12 C29, tier 1
HARD_CI = [r"\[\s*placeholder\s*\]", r"\[\s*CHECK\s*\]", r"\[\s*\?\s*\]", r"to be confirmed", r"to be verified", r"lorem ipsum"]


def hard_hits(text):
    """Shared pipeline v2.12 C29 HARD tier (case-sensitive word markers, case-insensitive phrase markers)."""
    out = [p for p in HARD_CS if re.search(p, text)]
    return out + [p for p in HARD_CI if re.search(p, text, re.I)]


def clean(text):
    """Guard on every string written: no residual markers (shared C29 HARD list), no pipeline wording.
    A documented limitation reads 'Not configured in this release [[GAP:DD-RQ-nn]]'."""
    s = str(text)
    h = hard_hits(s)
    if h:
        raise ValueError(f"residual marker {h} in: {s[:120]}")
    C.clean(s)
    return s


# ------------------------------------------------------------------ spec inventory ---
def spec_id(path):
    return re.match(r"(US-[A-Z0-9]+-\d{3})", os.path.basename(path)).group(1)


_SPEC_ROWS = None


def spec_rows():
    """Every field row of the 20 approved Report Specs (read-only):
    dict(spec, file, sheet, row, name, label, rtype, fid, payroll, mand, cond, length, fmt, example,
         mapping, expl, optvals, valtype)."""
    global _SPEC_ROWS
    if _SPEC_ROWS is not None:
        return _SPEC_ROWS
    from openpyxl import load_workbook
    rows = []
    for p in sorted(glob.glob(os.path.join(SPECS, "*-Spec.xlsx"))):
        wb = load_workbook(p, read_only=False)
        core = [s for s in wb.sheetnames if s.endswith(" Spec")][0]
        ws = wb[core]
        sid = spec_id(p)
        for r in range(2, ws.max_row + 1):
            a = ws.cell(r, 1).value
            if not a or str(a).startswith("═") or str(a).startswith("(continued)"):
                continue
            g = lambda c: ws.cell(r, c).value  # noqa: E731
            rows.append(dict(spec=sid, file=os.path.basename(p), sheet=core, row=r, name=str(a),
                             label=g(2), rtype=g(3), fid=g(4), payroll=g(5), mand=g(6), cond=g(7),
                             length=g(9), fmt=g(10), example=g(11), mapping=str(g(12) or ""),
                             expl=str(g(13) or ""), optvals=g(15), valtype=g(18)))
    _SPEC_ROWS = rows
    return rows


def spec_row(spec, row):
    for r in spec_rows():
        if r["spec"] == spec and r["row"] == row:
            return r
    raise KeyError((spec, row))
