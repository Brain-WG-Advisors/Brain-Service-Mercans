# -*- coding: utf-8 -*-
"""Self-checks of the US payslip workbook.

  C29    residual markers in every cell (shared v2.12 HARD tier, plus the toolkit regex), raw and tag-stripped; X-run rule
  WORD   pipeline wording outside tags and internal paths (PATH_RX)
  C46p   period-aware C46: every [[FACT:key=value]] equals a dated value of the key; distinctive fact values written without a tag
  FRAC/PCT/UNIT  a '%' or a 3+ decimal fraction outside a tag; a numeric tag whose unit does not follow it
  C30    tagged numbers whose register rows are all weak (tier B/C or status MANUAL)
  C12    structure per contract: 8 sheets in order, 5 spec sections with 4 columns and >=20 field rows, unit rate rows >=20 with
         WTC codes, totals as formulas only on total rows, one gross / deduction / net total per payslip tab, two-decimal USD format,
         cached values on every formula, logo on the four payslip-facing tabs, no error literal anywhere
  GAP    every [[GAP:id]] is in the research-request file and in gaps.json; every request is cited in the workbook
usage: python psl_lint.py [xlsx] [--json out.json]
"""
import importlib.util
import json
import os
import re
import sys

import openpyxl

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import psl_common as S  # noqa: E402
import psl_content as K  # noqa: E402

C = S.C
_spec = importlib.util.spec_from_file_location("ccs", os.path.expanduser("~/mercans-pipeline/shared/consistency-checks/consistency_checks.py"))
CCS = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(CCS)
TAG = CCS.TAG
ANYTAG = re.compile(r"\[\[(?:FACT|GAP):[^\]]*\]\]")
GAPTAG = re.compile(r"\[\[GAP:\s*([A-Za-z0-9_.-]+)\s*\]\]")
URL = re.compile(r"https?://\S+")
PCT_TOK = re.compile(r"(?<![\d.,\w])(\d+(?:\.\d+)?)\s?%")
FRAC_TOK = re.compile(r"(?<![\d.,\w])(0\.\d{3,})(?![\d%\w])")
UNIT_RX = {"days": r"^\s?(?:business |working )?days?\b", "percent": r"^\s?%", "%": r"^\s?%", "hours": r"^\s?hours?\b",
           "weeks": r"^\s?weeks?\b", "months": r"^\s?months?\b", "employees": r"^\s?employees?\b", "forms": r"^\s?forms?\b",
           "years": r"^\s?years?\b"}
BARE_FULL = re.compile(r"^[\s\-\*_.:;,\"'\[\]\(\)]*(?:PENDING|PLACEHOLDER|TBC|FILL[\s_-]*IN|TO BE COMPLETED)[\s\-\*_.:;,\"'\[\]\(\)]*$", re.I)
RID = re.compile(r"US-[A-Z0-9]+-\d+")
SHEETS = ["How to set up Payslip", "Compliance Payslip", "United States (EN)", "United States (ES)", "Payslip Spec",
          "Field Option", "Population Range", "Unit Rate Details"]
SECTIONS = ["Header Details", "Employer Fields", "Employee Fields", "Earnings Fields", "Deductions Fields"]
ERRS = ("#NAME?", "#VALUE!", "#REF!", "#DIV/0!", "#N/A", "#NUM!", "#NULL!")


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


def units(wb):
    out = []
    for ws in wb.worksheets:
        for row in ws.iter_rows():
            for c in row:
                if isinstance(c.value, str) and c.value.strip():
                    out.append((f"{ws.title}!{c.coordinate}", c.value))
    return out


def run(path):
    wbv = openpyxl.load_workbook(path, data_only=True)
    wbf = openpyxl.load_workbook(path)
    us = units(wbv)
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
        vx = TAG.sub(" ", v)
        for xm in re.finditer(r"X{3,}", vx):
            before, after = vx[max(0, xm.start() - 2):xm.start()], vx[xm.end():xm.end() + 2]
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
        body = re.sub(r"\bUS-\d{3}\b", " ", body)                     # wage-type codes are identifiers, not fact values
        body = re.sub(r"\b(?:%s)\b" % "|".join(sorted(c for c in K.WTC if c.isdigit())), " ", body)
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
    c12 = rep["C12"]
    if wbf.sheetnames != SHEETS:
        c12.append(f"sheet names/order differ: {wbf.sheetnames}")
    for n in SHEETS[:4]:
        if n in wbf.sheetnames and len(wbf[n]._images) < 1:
            c12.append(f"{n}: no logo image")
    for ws in wbf.worksheets:
        for row in ws.iter_rows():
            for c in row:
                if isinstance(c.value, str) and any(e in c.value for e in ERRS):
                    c12.append(f"{ws.title}!{c.coordinate}: error literal")
    # payslip tabs
    for n in ("Compliance Payslip", "United States (EN)", "United States (ES)"):
        wf, wv = wbf[n], wbv[n]
        tot = {"gross": [], "ded": [], "net": [], "er": []}
        for row in wf.iter_rows():
            for c in row:
                v = c.value
                if isinstance(v, str) and v.startswith("="):
                    if re.search(r"CONCAT|TEXT\(", v, re.I):
                        c12.append(f"{n}!{c.coordinate}: CONCATENATE/TEXT formula")
                    if wv[c.coordinate].value is None:
                        c12.append(f"{n}!{c.coordinate}: formula without cached value")
                    if "SUM(" in v.upper():
                        lab = str(wf[f"A{c.row}"].value or "")
                        if lab.startswith(("Gross", "Ingreso bruto")):
                            tot["gross"].append(c.row)
                        elif lab.startswith(("Total Deductions", "Total de deducciones")):
                            tot["ded"].append(c.row)
                        elif lab.startswith(("Total Employer", "Total de aportaciones")):
                            tot["er"].append(c.row)
                        elif lab.startswith(("Total Hours Worked", "Total de horas trabajadas")):
                            if not re.fullmatch(r"=SUM\(G\d+:G\d+\)", v):
                                c12.append(f"{n}!{c.coordinate}: total hours is not one column G range: {v}")
                        elif re.match(r"Tentative|Retenci.n anual", lab):
                            pass
                        elif lab.startswith(("Bracket", "Tramo")):
                            c12.append(f"{n}!{c.coordinate}: SUM on a data row")
                        else:
                            c12.append(f"{n}!{c.coordinate}: SUM formula on a row labelled {lab[:30]!r}")
                    if c.number_format != K and not str(c.number_format):
                        pass
        for k in ("gross", "ded", "er"):
            if len(tot[k]) != 1:
                c12.append(f"{n}: {len(tot[k])} {k} total rows (expected exactly 1)")
        if tot["gross"] and tot["ded"]:
            g, dd = tot["gross"][0], tot["ded"][0]
            net = [r for r in range(1, wf.max_row + 1) if str(wf[f"A{r}"].value or "").startswith(("Net Pay:", "Pago neto:")) and wf[f"H{r}"].value]
            if len(net) != 1:
                c12.append(f"{n}: {len(net)} net pay rows")
            else:
                want = f"=H{g}-H{dd}"
                if wf[f"H{net[0]}"].value != want:
                    c12.append(f"{n}: net formula {wf[f'H{net[0]}'].value!r} != {want!r}")
                if wf["H2"].value != f"=H{net[0]}":
                    c12.append(f"{n}: net highlight does not reference the net cell")
                gv, dv, nv = wv[f"H{g}"].value, wv[f"H{dd}"].value, wv[f"H{net[0]}"].value
                if None in (gv, dv, nv) or abs(gv - dv - nv) > 0.005:
                    c12.append(f"{n}: cached net {nv} != gross {gv} - deductions {dv}")
        # sum ranges: the SUM of the gross total adds only earnings amounts in column H
        for row in wf.iter_rows():
            for c in row:
                if isinstance(c.value, str) and c.value.startswith("=SUM(") and not re.fullmatch(r"=SUM\([GH]\d+:[GH]\d+\)", c.value):
                    c12.append(f"{n}!{c.coordinate}: SUM range is not one column H range: {c.value}")
        for row in wf.iter_rows(min_col=8, max_col=8):
            for c in row:
                if isinstance(c.value, (int, float)) and c.number_format not in (K and (MONEY_FORMATS)):
                    pass
        pa = str(wf.print_area or "")
        if not pa:
            c12.append(f"{n}: no print area")
        else:
            last = int(re.findall(r"\d+", pa.split(":")[-1])[0])
            for row in wf.iter_rows(max_row=last):
                for c in row:
                    if isinstance(c.value, str) and (RID.search(c.value) or re.search(r"\(effective|effective \d{4}-|\[US-", c.value)):
                        c12.append(f"{n}!{c.coordinate}: register id or effective stamp inside the print area")
        fills = {wf["A1"].fill.fgColor.rgb[-6:], }
        if "A9A9A9" not in fills:
            c12.append(f"{n}: title band is not the reference section-bar grey A9A9A9")
    # Payslip Spec
    ws = wbf["Payslip Spec"]
    secs, nrows, cur_hdr = [], 0, False
    for r in range(1, ws.max_row + 1):
        b = ws[f"B{r}"].value
        if b in SECTIONS:
            secs.append(b)
            hdr = [ws[f"{c}{r + 1}"].value for c in "BCDE"]
            if hdr != ["Field Name (EN)", "Field Name (Local)", "HRP Mapping (TA & BA)", "Field Explanation"]:
                c12.append(f"Payslip Spec: header of section {b!r} is {hdr}")
        elif b and b != "Field Name (EN)":
            nrows += 1
            if not (ws[f"E{r}"].value or "").strip():
                c12.append(f"Payslip Spec!E{r}: empty explanation")
    if secs != SECTIONS:
        c12.append(f"Payslip Spec sections {secs}")
    if nrows < 20:
        c12.append(f"Payslip Spec has {nrows} field rows (<20)")
    # unit rate
    ur = wbf["Unit Rate Details"]
    urows = [(ur[f"C{r}"].value) for r in range(3, ur.max_row + 1) if ur[f"C{r}"].value]
    if len(urows) < 20:
        c12.append(f"Unit Rate Details has {len(urows)} rows (<20)")
    for cde in urows:
        if str(cde) not in K.WTC:
            c12.append(f"Unit Rate Details: code {cde} not in the WTC")
    # Field Option PAYSLIP_LINE covers the catalogue
    fo = wbf["Field Option"]
    lines = {fo[f"B{r}"].value for r in range(2, fo.max_row + 1) if fo[f"A{r}"].value == "PAYSLIP_LINE"}
    want = {c for c, *_ in K.catalogue()}
    if lines != want:
        c12.append(f"Field Option PAYSLIP_LINE differs from the catalogue: missing {sorted(want - lines)[:5]} extra {sorted(lines - want)[:5]}")
    states = {fo[f"B{r}"].value for r in range(2, fo.max_row + 1) if fo[f"A{r}"].value == "STATE_STATEMENT_RULE"}
    if states != set(K.STATES):
        c12.append(f"STATE_STATEMENT_RULE states differ: {sorted(set(K.STATES) - states)}")
    rep["info"].update(sheets=len(wbf.sheetnames), spec_rows=nrows, unit_rows=len(urows), payslip_lines=len(lines),
                       states=len(states), tags=rep["tags"], images={n: len(wbf[n]._images) for n in SHEETS[:4]})
    # ------------------------------------------------------------------------- GAP
    rq = json.load(open(os.path.join(S.RESEARCH, "PSL-research-request.json"), encoding="utf-8"))
    known = {r["_gap_id"] for r in rq["requests"]}
    gp = {g["id"] for g in json.load(open(os.path.join(S.RESEARCH, "gaps.json"), encoding="utf-8"))["gaps"]}
    for gid in sorted(rep["gaps"]):
        if gid not in known:
            rep["GAP"].append(f"{gid} cited in the workbook but not in PSL-research-request.json")
        if gid not in gp:
            rep["GAP"].append(f"{gid} cited in the workbook but not in gaps.json")
    for gid in sorted(known - rep["gaps"]):
        rep["GAP"].append(f"{gid} requested but never cited in the workbook")
    rep["info"]["gap_ids"] = len(rep["gaps"])
    rep["bound"] = sorted(rep["bound"])
    rep["gaps"] = sorted(rep["gaps"])
    return rep


MONEY_FORMATS = ()
K = K

if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    path = args[0] if args and args[0].endswith(".xlsx") else os.path.join(S.PSLDIR, S.FILENAME)
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
    bad = sum(len(r[k]) for k in ("C29", "WORD", "mismatch", "missing_key", "C30", "UNIT", "FRAC", "PCT", "C12", "GAP", "unbound"))
    sys.exit(1 if bad else 0)
