# -*- coding: utf-8 -*-
"""Self-checks of the US Report Specifications (run on a folder of *-Spec.xlsx).

  C29   residual markers in every cell (toolkit regex), tags stripped and unstripped
  WORD  pipeline wording outside tags
  C46p  period-aware C46: every [[FACT:key=value]] equals a dated value of the key; distinctive
        fact values written without a tag (shared rule + percent-aware), listed with context.
        DERIVED: an INTEGER number (no '%', no decimal part) of a row rendered from a layout,
        line-map or code-list fact (a position, a line number, a code) is not counted as unbound when the same sheet row cites the
        register id of a fact whose full value is tagged in the same workbook and contains that
        number; such hits are counted separately (rule documented in the RSPEC build log).
        Percentages and amounts with a decimal part are never DERIVED: they must be tagged.
  C12   core sheet: columns populated (of 21), blank column M on field rows, row width <= 21
  WIDTH every sheet: no value right of the header's last column
  C30   tagged numbers whose register rows are all weak (tier B/C or status MANUAL)
  COVER RSPEC facts never bound in any workbook
  GAPS  [[GAP:id]] ids: recorded limitation ids or research-request ids
  MSENT core sheet: every column-M Field Explanation has at least 2 substantive sentences (content, origin,
        rule, format, edge cases). Not counted: the trailing source attribution ('Source type: ... URL'),
        the standard 2026-draft notice, and a sentence with fewer than 3 words of its own outside fact
        tags, register ids, URLs and brackets (a tagged value alone is one rule, not an explanation).
        Exceptions are listed in MSENT_EXCEPTIONS with their reason and reported, never silently passed.
  FRAC  (QA r2 finding 3) a decimal fraction with 3 or more decimals written outside a tag ('x 0.124') that equals a percent rate fact / 100,
        or the sum of an employee and an employer rate fact / 100, is an unbound fact value.
  PCT   (QA r2 finding 3) any number followed by '%' outside a tag (URLs excluded) is unbound, unless it matches a
        declared exception of PCT_EXCEPTIONS (reason reported, never silently passed).
  UNIT  (QA r2 finding 4) every numeric tag in core-sheet columns G and M whose fact carries a unit (unit_of_measure
        or currency) is followed (or, for USD, preceded) by that unit: '%' right after a percent tag, 'USD' for a
        currency amount, 'per hour' for an hourly amount, the counted noun (employees, days, forms...) for a count.
usage: python spec_lint.py <dir> [--json out.json]
"""
import csv
import glob
import importlib.util
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import us_common as C  # noqa: E402

from openpyxl import load_workbook  # noqa: E402

_spec = importlib.util.spec_from_file_location(
    "ccs", os.path.expanduser("~/mercans-pipeline/shared/consistency-checks/consistency_checks.py"))
CCS = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(CCS)

TAG = CCS.TAG
GAPTAG = re.compile(r"\[\[GAP:\s*([A-Za-z0-9_.-]+)\s*\]\]")
ANYTAG = re.compile(r"\[\[(?:FACT|GAP):[^\]]*\]\]")
REG = {r["id"]: r for r in csv.DictReader(open(os.path.join(C.BASE, "00-official-sources", "legal-basis-register.csv"),
                                               encoding="utf-8"))}


def weak(rid):
    r = REG.get(rid)
    return r is None or r.get("tier") in ("B", "C") or r.get("status") == "MANUAL"


def same(a, b):
    x, y = CCS._num(a), CCS._num(b)
    if x is not None and y is not None:
        return abs(x - y) < 1e-9
    return str(a).strip() == str(b).strip()


forms = {}
for k, es in C.FACTS.items():
    for f in es:
        v = f.get("value")
        for n, p in CCS.distinctive_forms(k, v):
            forms.setdefault((round(n, 6), p), set()).add(k)
        if isinstance(v, (int, float)) and not isinstance(v, bool) and re.search(r"(^|\.)rate(\.|$)", k):
            n = float(v)
            if n and (CCS._sig(n) >= 3 or n != int(n)):
                forms.setdefault((round(n, 6), True), set()).add(k)

# ------------------------------------------------- FRAC / PCT / UNIT ---
def _is_rate(k, f):
    v = f.get("value")
    return (isinstance(v, (int, float)) and not isinstance(v, bool) and v
            and (str(f.get("unit_of_measure") or "").lower() in ("percent", "%")))


FRACS = {}
_rate_vals = {}
for k, es in C.FACTS.items():
    for f in es:
        if _is_rate(k, f):
            FRACS.setdefault(round(float(f["value"]) / 100, 10), set()).add(k)
            _rate_vals.setdefault(k, set()).add(float(f["value"]))
for k in list(_rate_vals):
    m = re.match(r"^(.*)\.employee(\..*)?$", k)
    if not m:
        continue
    k2 = f"{m.group(1)}.employer{m.group(2) or ''}"
    for a in _rate_vals[k]:
        for b in _rate_vals.get(k2, ()):
            FRACS.setdefault(round((a + b) / 100, 10), set()).add(f"{k} + {k2}")
FRAC_TOK = re.compile(r"(?<![\d.,\w])(0\.\d{3,})(?![\d%\w])")   # 3+ decimals: a form rate (0.124), not a result (0.6)
PCT_TOK = re.compile(r"(?<![\d.,\w])(\d+(?:\.\d+)?)\s?%")
URL = re.compile(r"https?://\S+")
PCT_EXCEPTIONS = [
    (re.compile(r"Accuracy \d+%"), "Report Matrix accuracy assessment of the builder (Report Spec standard), not a fact"),
    (re.compile(r"\b98% Offer Method"), "name of certification D on Form 1094-C line 22 (a form label, not a rate applied)"),
]
UNIT_RX = {
    "percent": (r"^\s?%", None), "%": (r"^\s?%", None),
    "employees": (r"^[^.;|]{0,40}\bemployees?\b", None), "workers": (r"^[^.;|]{0,40}\bworkers?\b", None),
    "persons": (r"^[^.;|]{0,40}\b(persons?|people|employees?)\b", None),
    "days": (r"^[^.;|]{0,40}\bdays?\b", None), "working days": (r"^[^.;|]{0,40}\bdays?\b", None),
    "business days": (r"^[^.;|]{0,40}\bdays?\b", None), "weeks": (r"^[^.;|]{0,40}\bweeks?\b", None),
    "months": (r"^[^.;|]{0,40}\bmonths?\b", None), "years": (r"^[^.;|]{0,40}\byears?\b", None),
    "hours": (r"^[^.;|]{0,40}\bhours?\b", None), "minutes": (r"^[^.;|]{0,40}\bminutes?\b", None),
    "forms": (r"^[^.;|]{0,40}\b(forms?|returns?|statements?|W-2s?|information returns)\b", None),
    "statements": (r"^[^.;|]{0,40}\b(statements?|forms?|W-2s?)\b", None),
    "returns": (r"^[^.;|]{0,40}\b(returns?|forms?)\b", None),
    "usd per hour": (r"^[^.;|]{0,40}\bper hour", None),
    "USD": (r"^[^.;|]{0,25}\bUSD\b", r"(USD|\$)\s?$"),
}


def unit_ok(fct, before, after):
    v = fct.get("value")
    if isinstance(v, bool) or not isinstance(v, (int, float)):
        return None
    uom = str(fct.get("unit_of_measure") or "").strip()
    keyu = "usd per hour" if "per hour" in uom.lower() else (uom.lower() if uom else ("USD" if fct.get("currency") else ""))
    if keyu not in UNIT_RX:
        return None          # no checkable unit (ratio, count, bytes, characters, ... or no unit at all)
    a, b = UNIT_RX[keyu]
    return bool(re.search(a, after, re.I) or (b and re.search(b, before[-8:])))


# ------------------------------------------------------------ MSENT ---
MSENT_MIN = 2
MSENT_EXCEPTIONS = {}   # field id (column D) -> reason; empty in this build
_M_SRC = re.compile(r"Source type: (?:Official spec|Web research \(official authority page\))\.(?:\s+https?://\S+)?")
_M_DRAFT = re.compile(r"Per 2026 draft: read from the IRS early-release draft[^.]*\.")
_M_ABBR = re.compile(r"\b(?:e\.g|i\.e|U\.S\.C|U\.S|C\.F\.R|G\.S|No|Nos|Pub|Rev|Proc|Reg|Sec|Art|vs|etc|approx|Inc|Co|St|"
                     r"Dept|Stat|Ch|pp|para|cf|incl)\.", re.I)
_M_WORD = re.compile(r"[A-Za-z][A-Za-z'-]+")


def m_sentences(text):
    """Substantive sentences of a column-M cell (see MSENT in the module docstring)."""
    t = _M_SRC.sub(" ", str(text or ""))
    t = _M_DRAFT.sub(" ", t)
    t = ANYTAG.sub(" # ", t)
    t = re.sub(r"https?://\S+", " # ", t)
    prev = None
    while prev != t:
        prev = t
        t = re.sub(r"\[[^\[\]]*\]|\([^()]*\)", " # ", t)
    t = _M_ABBR.sub("#", t)
    t = re.sub(r"(\d)\.(\d)", r"\1\2", t)
    t = re.sub(r"\b([A-Z])\.(?=[A-Z]\.)", r"\1", t)
    return [x for x in re.split(r"(?<=[.!?])\s+", t.strip()) if len(_M_WORD.findall(x)) >= 3]


POS = re.compile(r"^\d{1,3}(-\d{1,3})?$")
RID = re.compile(r"US-[A-Z0-9]+-\d+")


def tagged_tokens(wb):
    """register id -> numbers appearing in the full values tagged in this workbook."""
    out = {}
    for ws in wb.worksheets:
        for row in ws.iter_rows():
            for c in row:
                if not isinstance(c.value, str):
                    continue
                for t in TAG.finditer(c.value):
                    k, val = t.group(1), t.group(2)
                    for f in C.FACTS.get(k, []):
                        if not same(val, f.get("value")):
                            continue
                        toks = out.setdefault(f["register_id"], set())
                        for mm in CCS.NUM_IN_TEXT.finditer(str(val)):
                            n = CCS._num(mm.group(1))
                            if n is not None:
                                toks.add(round(n, 6))
                        for x in re.findall(r"\d+(?:\.\d+)?", str(val)):
                            toks.add(round(float(x), 6))
    return out


def run(d):
    rep = {"files": 0, "C29": [], "WORD": [], "tags": 0, "mismatch": [], "missing_key": [], "unbound": [],
           "C12": {}, "blankM": [], "width": [], "C30": [], "gaps": set(), "bound_keys": set(), "derived": 0,
           "MSENT": [], "MSENT_exceptions": [], "MSENT_fields": 0,
           "FRAC": [], "PCT": [], "PCT_exceptions": [], "UNIT": [], "UNIT_checked": 0}
    known_gap = {g["id"] for g in C.RSPEC_GAPS.values()}
    for p in sorted(glob.glob(os.path.join(d, "*-Spec.xlsx"))):
        rep["files"] += 1
        name = os.path.basename(p)
        wb = load_workbook(p)
        toks = tagged_tokens(wb)
        for ws in wb.worksheets:
            hdr_row = 1 if ws.title.endswith("Spec") or ws.title in ("Field Options", "Population Rules") else None
            last = None
            if hdr_row:
                last = max(c.column for c in ws[hdr_row] if c.value is not None)
            for row in ws.iter_rows():
                row_rids = set(RID.findall(" ".join(str(x.value) for x in row if isinstance(x.value, str))))
                for c in row:
                    v = c.value
                    if not isinstance(v, str):
                        continue
                    loc = f"{name}!{ws.title}!{c.coordinate}"
                    if C.C29.search(v):
                        rep["C29"].append((loc, C.C29.search(v).group(0)))
                    bare = ANYTAG.sub(" ", v)
                    m = C.PIPELINE_WORDS.search(bare)
                    if m:
                        rep["WORD"].append((loc, m.group(0)))
                    for t in TAG.finditer(v):
                        rep["tags"] += 1
                        k, val = t.group(1), t.group(2)
                        rep["bound_keys"].add(k)
                        if k not in C.FACTS:
                            rep["missing_key"].append((loc, k))
                            continue
                        hit = [f for f in C.FACTS[k] if same(val, f.get("value"))]
                        if not hit:
                            rep["mismatch"].append((loc, k, val[:60]))
                        elif re.search(r"\d", val) and all(weak(f["register_id"]) for f in hit):
                            rep["C30"].append((loc, k))
                    for g in GAPTAG.findall(v):
                        rep["gaps"].add(g)
                    # FRAC / PCT: rates outside tags (URLs and tags stripped)
                    plain = URL.sub(" ", ANYTAG.sub(" ", v))
                    for mm in FRAC_TOK.finditer(plain):
                        ks = FRACS.get(round(float(mm.group(1)), 10))
                        if ks and float(mm.group(1)) != 0:
                            rep["FRAC"].append((loc, mm.group(1), sorted(ks)[:2], plain[max(0, mm.start() - 40): mm.end() + 20]))
                    for mm in PCT_TOK.finditer(plain):
                        ctx = plain[max(0, mm.start() - 40): mm.end() + 30]
                        ex = [why for rx, why in PCT_EXCEPTIONS if rx.search(plain[max(0, mm.start() - 12): mm.end() + 20])]
                        (rep["PCT_exceptions"] if ex else rep["PCT"]).append((loc, mm.group(0), ex[0] if ex else ctx))
                    # UNIT: numeric tags of core-sheet columns G / M carry their unit
                    if ws.title.endswith("Spec") and c.column in (7, 13):
                        for t in TAG.finditer(v):
                            k, val = t.group(1), t.group(2)
                            hit = [f for f in C.FACTS.get(k, []) if same(val, f.get("value"))]
                            if not hit:
                                continue
                            ok = unit_ok(hit[0], v[:t.start()], v[t.end():])
                            if ok is None:
                                continue
                            rep["UNIT_checked"] += 1
                            if not ok:
                                rep["UNIT"].append((loc, k, val, (hit[0].get("unit_of_measure") or hit[0].get("currency")),
                                                    v[max(0, t.start() - 30): t.end() + 40]))
                    if POS.match(v.strip()) and ws.title.endswith("Spec") and c.column in (8, 9):
                        continue   # file positions / lengths, not fact values
                    for mm in CCS.NUM_IN_TEXT.finditer(GAPTAG.sub(" ", TAG.sub(" ", v))):
                        n = CCS._num(mm.group(1))
                        if n is None:
                            continue
                        ks = forms.get((round(n, 6), bool(mm.group(2))))
                        tok = mm.group(1)
                        integer_tok = (not mm.group(2)) and "." not in tok and n == int(n)
                        if ks and integer_tok and any(round(n, 6) in toks.get(r, ()) for r in row_rids):
                            rep["derived"] += 1
                            continue
                        if ks:
                            ctx = bare[max(0, mm.start() - 50): mm.end() + 30]
                            rep["unbound"].append((loc, mm.group(0).strip(), sorted(ks)[:2], ctx))
                    if last and c.column > last:
                        rep["width"].append(loc)
            if ws.title.endswith("Spec"):
                pop = {i: 0 for i in range(1, 22)}
                for r in range(2, ws.max_row + 1):
                    a = ws.cell(r, 1).value
                    if a is None or str(a).startswith("═══"):
                        continue
                    for i in range(1, 22):
                        if ws.cell(r, i).value not in (None, ""):
                            pop[i] += 1
                    if not ws.cell(r, 13).value:
                        rep["blankM"].append(f"{name}!{ws.title}!M{r}")
                    if str(a).startswith("(continued)"):
                        continue   # continuation row of an over-long column G rule
                    rep["MSENT_fields"] += 1
                    ns = len(m_sentences(ws.cell(r, 13).value))
                    if ns < MSENT_MIN:
                        fid = str(ws.cell(r, 4).value or "")
                        hit = (f"{name}!{ws.title}!M{r}", fid, ns)
                        if fid in MSENT_EXCEPTIONS:
                            rep["MSENT_exceptions"].append(hit + (MSENT_EXCEPTIONS[fid],))
                        else:
                            rep["MSENT"].append(hit)
                rep["C12"][name] = sum(1 for i in pop if pop[i] > 0)
    unused = sorted(set(C.RSPEC_KEYS) - rep["bound_keys"])
    # a value with square brackets cannot be tagged; it is quoted with parentheses and its register id
    quoted = []
    if unused:
        alltext = []
        for p in sorted(glob.glob(os.path.join(d, "*-Spec.xlsx"))):
            for ws in load_workbook(p).worksheets:
                for row in ws.iter_rows():
                    alltext += [c.value for c in row if isinstance(c.value, str)]
        blob = chr(10).join(alltext)
        for k in unused:
            f = C.fact(k)
            if "]" in str(f["value"]) and (str(f["value"]).replace("[", "(").replace("]", ")") + f" [{f['register_id']}]") in blob:
                quoted.append(k)
    unused = [k for k in unused if k not in quoted]
    rep["quoted_untaggable"] = quoted
    rep["unbound_rspec_facts"] = unused
    rep["gap_ids_unknown"] = sorted(g for g in rep["gaps"] if g not in known_gap and not g.startswith("RSPEC-RQ-"))
    rep["gaps"] = sorted(rep["gaps"])
    rep["bound_keys"] = len(rep["bound_keys"])
    return rep


if __name__ == "__main__":
    r = run(sys.argv[1])
    summ = {k: (len(v) if isinstance(v, list) else v) for k, v in r.items() if k not in ("C12",)}
    summ["C12_min_columns"] = min(r["C12"].values()) if r["C12"] else None
    sys.stdout.reconfigure(encoding="utf-8")
    print(json.dumps(summ, indent=1))
    for x in r["MSENT_exceptions"]:
        print("MSENT EXCEPTION", x)
    for k in ("FRAC", "PCT", "UNIT"):
        for x in r[k][:40]:
            print(k, x)
    for k in ("C29", "WORD", "mismatch", "missing_key", "blankM", "width", "C30", "gap_ids_unknown", "MSENT"):
        for x in r[k][:15]:
            print(k, x)
    for x in r["unbound"][:60]:
        print("UNBOUND", x)
    print("UNUSED RSPEC FACTS", r["unbound_rspec_facts"])
    if "--json" in sys.argv:
        json.dump(r, open(sys.argv[sys.argv.index("--json") + 1], "w", encoding="utf-8"), indent=1, ensure_ascii=False, default=list)
