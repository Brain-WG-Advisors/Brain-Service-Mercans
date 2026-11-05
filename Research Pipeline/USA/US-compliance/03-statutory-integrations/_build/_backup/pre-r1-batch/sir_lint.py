# -*- coding: utf-8 -*-
"""Self-checks of the US SIR index (docx).

  C29    residual markers in every paragraph and cell (shared v2.12 HARD tier, plus the toolkit regex), raw and tag-stripped
  WORD   pipeline wording outside tags and internal paths (PATH_RX)
  C46p   period-aware C46: every [[FACT:key=value]] equals a dated value of the key; distinctive fact values written without a tag
  FRAC/PCT/UNIT  a '%' or a 3+ decimal fraction outside a tag; a numeric tag whose unit does not follow it
  C30    tagged numbers whose register rows are all weak (tier B/C or status MANUAL)
  C12    structure per contract: Document ID = file id, TOC field, section headings in order, tables with the contracted
         columns, every Report Spec in the outbound register with direction OUTBOUND, one hand-off row per Report Matrix row
  GAP    every [[GAP:id]] is in the research-request file and in gaps.json; every request is cited in the document
usage: python sir_lint.py [docx] [--json out.json]
"""
import importlib.util
import json
import os
import re
import sys

import docx

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import sir_common as S  # noqa: E402
import sir_specs as P  # noqa: E402

C = S.C
_spec = importlib.util.spec_from_file_location(
    "ccs", os.path.expanduser("~/mercans-pipeline/shared/consistency-checks/consistency_checks.py"))
CCS = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(CCS)
TAG = CCS.TAG
ANYTAG = re.compile(r"\[\[(?:FACT|GAP):[^\]]*\]\]")
GAPTAG = re.compile(r"\[\[GAP:\s*([A-Za-z0-9_.-]+)\s*\]\]")
URL = re.compile(r"https?://\S+")
PCT_TOK = re.compile(r"(?<![\d.,\w])(\d+(?:\.\d+)?)\s?%")
FRAC_TOK = re.compile(r"(?<![\d.,\w])(0\.\d{3,})(?![\d%\w])")
UNIT_RX = {"days": r"^\s?(?:business |working )?days?\b", "percent": r"^\s?%", "%": r"^\s?%", "hours": r"^\s?hours?\b",
           "weeks": r"^\s?weeks?\b", "months": r"^\s?months?\b", "employees": r"^\s?employees?\b", "forms": r"^\s?forms?\b"}
BARE_FULL = re.compile(r"^[\s\-\*_.:;,\"'\[\]\(\)]*(?:PENDING|PLACEHOLDER|TBC|FILL[\s_-]*IN|TO BE COMPLETED)[\s\-\*_.:;,\"'\[\]\(\)]*$", re.I)
RID = re.compile(r"US-[A-Z0-9]+-\d+")
SECTIONS = ["Table of Contents", "Document Control", "0. Purpose, Scope & Audit Compliance",
            "1. Inbound Integrations (documents from authorities)", "2. Outbound Integrations (submissions through the provider)",
            "3. Authorisation Requirements", "4. Technical Specifications",
            "5. Error Handling: routing, rejection and correction rules", "6. SLA and Deadlines", "7. Per-report hand-off register",
            "8. Provider input data set", "Appendix A. Sources", "Appendix B. Not configured in this release"]


def same(a, b):
    x, y = CCS._num(a), CCS._num(b)
    if x is not None and y is not None:
        return abs(x - y) < 1e-9
    return str(a).strip() == str(b).strip()


def weak(rid):
    r = S.REG.get(rid)
    return r is None or r.get("tier") in ("B", "C") or r.get("status") == "MANUAL"


FORMS = {}
for _k, _es in C.FACTS.items():
    for _f in _es:
        for _n, _p in CCS.distinctive_forms(_k, _f.get("value")):
            FORMS.setdefault((round(_n, 6), _p), set()).add(_k)


def units(d):
    """[(location, text)] of the document: paragraphs, table cells (merged cells once), footers."""
    out = []
    for i, p in enumerate(d.paragraphs):
        if p.text.strip():
            out.append((f"para {i + 1}", p.text))
    for ti, t in enumerate(d.tables):
        for ri, r in enumerate(t.rows):
            seen = set()
            for ci, c in enumerate(r.cells):
                if id(c._tc) in seen:
                    continue
                seen.add(id(c._tc))
                if c.text.strip():
                    out.append((f"table {ti + 1} r{ri + 1}c{ci + 1}", c.text))
    for si, s in enumerate(d.sections):
        for p in s.footer.paragraphs:
            if p.text.strip():
                out.append((f"footer s{si + 1}", p.text))
    return out


def run(path):
    d = docx.Document(path)
    us = units(d)
    rep = dict(C29=[], WORD=[], mismatch=[], missing_key=[], unbound=[], C30=[], FRAC=[], PCT=[], UNIT=[], tags=0,
               bound=set(), gaps=set(), C12=[], GAP=[], info={})
    tagged_tokens = {}
    for loc, v in us:
        for t in TAG.finditer(v):
            k, val = t.group(1), t.group(2)
            for f in C.FACTS.get(k, []):
                if same(val, f.get("value")):
                    toks = tagged_tokens.setdefault(f["register_id"], set())
                    for x in re.findall(r"\d+(?:\.\d+)?", str(val)):
                        toks.add(round(float(x), 6))
    for loc, v in us:
        row_rids = set(RID.findall(v))
        bare = ANYTAG.sub(" ", v)
        hh = S.hard_hits(v) or S.hard_hits(bare)
        if hh:
            rep["C29"].append((loc, hh[0]))
        m = C.C29.search(bare)
        if m:
            rep["C29"].append((loc, m.group(0)))
        if BARE_FULL.match(v):
            rep["C29"].append((loc, "bare placeholder value"))
        for xm in re.finditer(r"X{3,}", v):          # shared C29 X-run rule: sanctioned only next to a digit, dot or colon
            before, after = v[max(0, xm.start() - 2):xm.start()], v[xm.end():xm.end() + 2]
            if not (re.search(r"[.\d]$", before) or re.match(r"\s*[.:\d]", after)):
                rep["C29"].append((loc, "X-run " + xm.group(0)))
        m = C.PIPELINE_WORDS.search(bare)
        if m:
            rep["WORD"].append((loc, m.group(0)))
        pm = C.PATH_RX.search(v)
        if pm:
            rep["WORD"].append((loc, "internal path: " + pm.group(0)))
        for t in TAG.finditer(v):
            rep["tags"] += 1
            k, val = t.group(1), t.group(2)
            rep["bound"].add(k)
            if k not in C.FACTS:
                rep["missing_key"].append((loc, k))
                continue
            hit = [f for f in C.FACTS[k] if same(val, f.get("value"))]
            if not hit:
                rep["mismatch"].append((loc, k, val[:60]))
            elif re.search(r"\d", val) and all(weak(f["register_id"]) for f in hit):
                rep["C30"].append((loc, k))
            f0 = hit[0] if hit else None
            if f0 is not None and isinstance(f0.get("value"), (int, float)) and f0.get("unit_of_measure"):
                u = str(f0["unit_of_measure"]).lower()
                rx = UNIT_RX.get(u)
                if rx and not re.search(rx, v[t.end():t.end() + 20], re.I):
                    rep["UNIT"].append((loc, k, u))
        for g_ in GAPTAG.findall(v):
            rep["gaps"].add(g_)
        plain = URL.sub(" ", ANYTAG.sub(" ", v))
        for mm in PCT_TOK.finditer(plain):
            rep["PCT"].append((loc, mm.group(0), plain[max(0, mm.start() - 40): mm.end() + 20]))
        for mm in FRAC_TOK.finditer(plain):
            rep["FRAC"].append((loc, mm.group(0)))
        body = re.sub(r"\[US-[A-Z0-9]+-\d+\]|\bUS-[A-Z0-9]+-\d{3}(?:-[A-Z]{2})?\b( v\d+\.\d+)?", " ", plain)
        body = re.sub(r"\b(?:effective|read)[^()]*\d{4}-\d{2}-\d{2}", " ", body)
        body = re.sub(r"\b\d{4}-\d{2}-\d{2}\b", " ", body)
        for mm in CCS.NUM_IN_TEXT.finditer(body):
            n = CCS._num(mm.group(1))
            if n is None:
                continue
            ks = FORMS.get((round(n, 6), bool(mm.group(2))))
            integer_tok = (not mm.group(2)) and "." not in mm.group(1) and n == int(n)
            if ks and integer_tok and any(round(n, 6) in tagged_tokens.get(r_, ()) for r_ in row_rids):
                continue
            if ks:
                rep["unbound"].append((loc, mm.group(0).strip(), sorted(ks)[:2], body[max(0, mm.start() - 40): mm.end() + 25]))
    # ------------------------------------------------------------------- C12 structure
    heads = [(p.style.name, p.text) for p in d.paragraphs if p.style.name.startswith("Heading")]
    h1 = [t for s_, t in heads if s_ == "Heading 1"]
    if h1 != SECTIONS:
        rep["C12"].append(f"Heading 1 list differs: {h1}")
    h2 = [t for s_, t in heads if s_ == "Heading 2"]
    for need in ("0.1 Canonical integration inventory", "0.2 Direction & product-mapping rule", "1.2 Inbound register",
                 "2.1 Outbound register: one row per Report Specification", "3.3 Authorisation instrument per jurisdiction"):
        if need not in h2:
            rep["C12"].append(f"missing heading {need!r}")
    x = d.element.xml
    if "TOC \\o" not in x:
        rep["C12"].append("no TOC field")
    fid = re.sub(r"-v\d+[._]\d+.*$", "", os.path.basename(path))
    docid = None
    for t in d.tables:
        for r in t.rows:
            c = [c.text.strip() for c in r.cells]
            if len(c) >= 2 and c[0].lower() == "document id":
                docid = c[1]
                if c[1] != fid:
                    rep["C12"].append(f"Document ID {c[1]!r} != file id {fid!r}")
    if docid is None:
        rep["C12"].append("no Document ID row")
    ft = d.sections[0].footer.paragraphs[0].text
    if ft != S.FOOTER:
        rep["C12"].append(f"footer {ft!r} != {S.FOOTER!r}")
    # version history: exactly one row, package version
    vh = [t for t in d.tables if [c.text for c in t.rows[0].cells] == ["Version", "Date", "Author", "Status"]]
    if len(vh) != 1 or len(vh[0].rows) != 2 or vh[0].rows[1].cells[0].text != f"v{S.PKG}":
        rep["C12"].append("version history is not one row with the package version")
    # outbound register
    spec_ids = {s["id"]: s for s in P.specs()}
    reg_tbl = None
    for t in d.tables:
        hdr = [c.text.strip() for c in t.rows[0].cells]
        if hdr and hdr[0] == "Report Spec":
            reg_tbl = t
    if reg_tbl is None:
        rep["C12"].append("no outbound register table")
    else:
        got = {r.cells[0].text.strip(): r.cells[1].text.strip() for r in reg_tbl.rows[1:]}
        if set(got) != set(spec_ids):
            rep["C12"].append(f"outbound register specs differ: missing {sorted(set(spec_ids) - set(got))} extra {sorted(set(got) - set(spec_ids))}")
        for sid, dr in got.items():
            if dr != "OUTBOUND":
                rep["C12"].append(f"{sid}: direction {dr!r}")
    # one hand-off row per Report Matrix row
    rows_in_doc = []
    for t in d.tables:
        hdr = [c.text.strip() for c in t.rows[0].cells]
        if hdr and hdr[0] == "Report row":
            rows_in_doc += [r.cells[0].text.strip() for r in t.rows[1:]]
    exp = [r["row_id"] for s in P.specs() for r in s["rows"]]
    if sorted(rows_in_doc) != sorted(exp):
        rep["C12"].append(f"hand-off rows differ from the Report Matrix rows: doc {len(rows_in_doc)} spec {len(exp)}")
    if len(rows_in_doc) != len(set(rows_in_doc)):
        rep["C12"].append("duplicate hand-off rows")
    rep["info"].update(tables=len(d.tables), paragraphs=len(d.paragraphs), handoff_rows=len(rows_in_doc), spec_rows=len(exp),
                       sections=len(d.sections), tags=rep["tags"])
    # ------------------------------------------------------------------------- GAP
    rq = json.load(open(os.path.join(S.RESEARCH, "SIR-research-request.json"), encoding="utf-8"))
    known = {r["_gap_id"] for r in rq["requests"]}
    gp = {g["id"] for g in json.load(open(os.path.join(S.RESEARCH, "gaps.json"), encoding="utf-8"))["gaps"]}
    for gid in sorted(rep["gaps"]):
        if gid not in known:
            rep["GAP"].append(f"{gid} cited in the document but not in SIR-research-request.json")
        if gid not in gp:
            rep["GAP"].append(f"{gid} cited in the document but not in gaps.json")
    for gid in sorted(known - rep["gaps"]):
        rep["GAP"].append(f"{gid} requested but never cited in the document")
    rep["info"]["gap_ids"] = len(rep["gaps"])
    rep["bound"] = sorted(rep["bound"])
    rep["gaps"] = sorted(rep["gaps"])
    return rep


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    path = args[0] if args and args[0].endswith(".docx") else os.path.join(S.SIRDIR, S.FILENAME)
    r = run(path)
    sys.stdout.reconfigure(encoding="utf-8")
    summ = {k: (len(v) if isinstance(v, list) else v) for k, v in r.items() if k not in ("info", "bound", "gaps")}
    summ["info"] = r["info"]
    print(json.dumps(summ, indent=1, default=list))
    for k in ("C29", "WORD", "mismatch", "missing_key", "C30", "UNIT", "FRAC", "PCT", "C12", "GAP"):
        for x in r[k][:30]:
            print(k, x)
    for x in r["unbound"][:60]:
        print("UNBOUND", x)
    if "--json" in sys.argv:
        json.dump(r, open(sys.argv[sys.argv.index("--json") + 1], "w", encoding="utf-8"), indent=1, ensure_ascii=False, default=list)
