# -*- coding: utf-8 -*-
"""Build the US Wage Type Catalogue (stage 5) from the CZ template, the facts and the approved DD and Report Specs.

Re-runnable: python build_wtc.py [--out dir]  ->  02-wtc/US-WTC-001-v1.0.xlsx, _research/WTC-crosswalk.json,
checks/wtc_recon.csv, _pipeline/WTC-bindings.csv. The generator is the only source of the workbook (C71)."""
import copy
import csv
import datetime as dt
import json
import os
import re
import sys

from openpyxl import load_workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.worksheet.datavalidation import DataValidation

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import wtc_common as W  # noqa: E402
import wtc_catalog as CAT  # noqa: E402
import wtc_model as M  # noqa: E402
import wtc_recon as RC  # noqa: E402
import wtc_taxcodes as T  # noqa: E402

FONT = "Times New Roman"
REP_HDR = "Reporting Code (W-2 box and code, return line)"
SRC_HDR = "Tax Code Official Source (v2.4 C9)"
BASIS_HDR = "Legal Basis (register ids)"
BASE_HDRS = ["Mercans Code", "Wage Type Name in English", "Wage Type Name in Local Language (English: the payslip and filings are in English)",
             "Wage Type Explanation", "Category", "Formula", "Tax Code", "Calculation Type", "Prorating Method", "Occurrence", "Ignore If 0",
             "Enforce Setting", "In Period Reconciliation"]
HEADERS = BASE_HDRS + [h for _, h in M.FLAG_COLS if h not in ("Subject to State Income Tax", "Subject to Local Income Tax")] + \
    ["YTD Load (Yes/ No)", "YTD Remarks", "Subject to State Income Tax", "Subject to Local Income Tax", REP_HDR, BASIS_HDR, SRC_HDR]
# column letters
COL = {h: i + 1 for i, h in enumerate(HEADERS)}
ORDER_FLAGS = ["income_tax", "table_tax", "special_tax", "oasdi", "medicare", "futa", "sui", "state_programmes", "pension"]
FLAGCOL = {f: COL[M.FLAG_HDR[f]] for f in M.FLAG_NAMES}
ORANGE = {"Formula", "Calculation Type", "Prorating Method", "Ignore If 0", "Enforce Setting", "In Period Reconciliation", "YTD Load (Yes/ No)", "YTD Remarks"}


def col_letter(i):
    from openpyxl.utils import get_column_letter
    return get_column_letter(i)


def g(t):
    return W.clean(t)


def tmpl_style(ws, col):
    c = ws.cell(1, col)
    return dict(font=copy.copy(c.font), fill=copy.copy(c.fill), alignment=copy.copy(c.alignment), border=copy.copy(c.border))


def put_header(ws, styles, i, h):
    c = ws.cell(1, i)
    c.value = h
    src = {"Mercans Code": 1, "Wage Type Explanation": 4, "Calculation Type": 8, "Prorating Method": 9, "Ignore If 0": 11, "Enforce Setting": 12,
           "In Period Reconciliation": 13, "YTD Load (Yes/ No)": 19, "YTD Remarks": 20, "R": 18}.get(h)
    if src is None:
        src = 17 if h.startswith("Q") else (18 if h.startswith("R ") else (14 if i > 20 or h in ("Subject to Tax", "Table Tax", "Special Tax") else 2))
        if h in ("Wage Type Name in Local Language (English: the payslip and filings are in English)",):
            src = 3
        if h == "Category":
            src = 5
        if h == "Formula":
            src = 6
        if h == "Tax Code":
            src = 7
        if h == "Occurrence":
            src = 10
        if h == "Subject to Tax":
            src = 14
        if h == "Table Tax":
            src = 15
        if h == "Special Tax":
            src = 16
    st = styles[src]
    c.font, c.fill, c.alignment, c.border = copy.copy(st["font"]), copy.copy(st["fill"]), copy.copy(st["alignment"]), copy.copy(st["border"])
    c.alignment = Alignment(wrap_text=True, vertical="center", horizontal="center")


def clear_below(ws, first_row):
    for row in ws.iter_rows(min_row=first_row, max_row=ws.max_row):
        for c in row:
            c.value = None
            c.comment = None
    for r in list(ws.row_dimensions):
        if r >= first_row:
            ws.row_dimensions[r].height = None


def sheet_text(ws, rows, widths=None, title_rows=1):
    """Plain sheet writer for the narrative sheets: rows = list of lists."""
    clear_below(ws, 1)
    for row in ws.iter_rows(min_row=1, max_row=ws.max_row):
        for c in row:
            c.fill = PatternFill(fill_type=None)
    for r, vals in enumerate(rows, start=1):
        for ci, v in enumerate(vals, start=1):
            if v is None:
                continue
            c = ws.cell(r, ci)
            c.value = g(v) if isinstance(v, str) else v
            c.font = Font(name=FONT, size=11, bold=(r <= title_rows or r in HEADROWS.get(ws.title, ())))
            c.alignment = Alignment(wrap_text=True, vertical="top")
    if widths:
        for k, v in widths.items():
            ws.column_dimensions[k].width = v


HEADROWS = {}


def build(out_dir=None, sidecars=True):
    W.USED.clear()
    W.GAP_USED.clear()
    W.GAPS.clear()
    W.UG.clear()
    grows, usrows, allrows, symmap = CAT.assemble()
    wb = load_workbook(W.TEMPLATE)
    ws = wb["Wage Type Catalogue"]
    styles = {i: tmpl_style(ws, i) for i in range(1, 21)}
    data_font = copy.copy(ws["B2"].font)
    for dv in list(ws.data_validations.dataValidation):
        ws.data_validations.dataValidation.remove(dv)
    clear_below(ws, 2)
    for row in ws.iter_rows(min_row=1, max_row=ws.max_row, max_col=40):
        for c in row:
            if c.row > 1:
                c.fill = PatternFill(fill_type=None)
    for c in ws[1]:
        if c.column > 0:
            c.value = None
    for i, h in enumerate(HEADERS, start=1):
        put_header(ws, styles, i, h)
    ws.row_dimensions[1].height = 75
    rows = sorted(grows, key=lambda r: int(r.code)) + usrows
    for ri, r in enumerate(rows, start=2):
        vals = {"Mercans Code": (int(r.code) if r.code.isdigit() else r.code), "Wage Type Name in English": (r.global_desc if r.glob else r.name),
                "Wage Type Name in Local Language (English: the payslip and filings are in English)": r.name,
                "Wage Type Explanation": r.expl, "Category": r.cat, "Tax Code": r.tax_code, "Occurrence": r.occ,
                REP_HDR: r.rep or None, BASIS_HDR: ", ".join(sorted(set(r.legal))) or None,
                SRC_HDR: T.source_text(r.tax_code) if r.tax_code != "US-NA" else "Not a tax code: no official source applies."}
        for f, hdr in M.FLAG_COLS:
            vals[hdr] = r.flags[f]
        for h, v in vals.items():
            c = ws.cell(ri, COL[h])
            c.value = g(v) if isinstance(v, str) else v
            c.font = Font(name=FONT, size=11)
            c.alignment = Alignment(wrap_text=True, vertical="top")
    last = len(rows) + 1
    ws.auto_filter.ref = f"A1:{col_letter(len(HEADERS))}{last}"
    ws.freeze_panes = "C1"
    for k, v in {"A": 13, "B": 44, "C": 30, "D": 100, "E": 18, "F": 14, "G": 12, "J": 13, "N": 12, "O": 11, "P": 12, "Q": 16, "R": 16, "S": 16, "T": 16,
                 "U": 16, "V": 16, "W": 16, "X": 16, "Y": 16, "Z": 14, "AA": 30, "AB": 28, "AC": 70, "AD": 40}.items():
        ws.column_dimensions[k].width = v
    ws.column_dimensions[col_letter(COL[REP_HDR])].width = 34
    ws.column_dimensions[col_letter(COL[BASIS_HDR])].width = 28
    ws.column_dimensions[col_letter(COL[SRC_HDR])].width = 70
    for cat_dv in (("Earning,Deduction,Base,Employer Contribution,Flag,Intermediary,Notional,Tax,Percentage", [COL["Category"]]),
                   ("Recurring,Additional,NA", [COL["Occurrence"]]),
                   ("Yes,No,Yes-No,NA", [COL[M.FLAG_HDR[f]] for f in M.FLAG_NAMES])):
        dv = DataValidation(type="list", formula1=f'"{cat_dv[0]}"', allow_blank=True)
        for ci in cat_dv[1]:
            dv.add(f"{col_letter(ci)}2:{col_letter(ci)}{last}")
        ws.add_data_validation(dv)

    # ---- Version Control: one row ----------------------------------------------------------------------
    vc = wb["Version Control"]
    vc["B8"].value = "Wage Type Catalogue"
    vc["B9"].value = f"{W.COUNTRY} | {W.WTC_ID} v{W.PKG}"
    for dv in vc.data_validations.dataValidation:
        if "Released" in str(dv.formula1):
            dv.formula1 = '"In Progress,Under Review,Approved,Released,Issued,For QA"'
    vc["B13"].value, vc["C13"].value = float(W.PKG), W.ISSUE
    vc["D13"].value, vc["E13"].value, vc["F13"].value = "Wage Type Catalogue of the United States payroll package", W.STATUS, W.AUTHOR
    for col in "BCDEF":
        vc[f"{col}14"].value = None

    # ---- Sick leave ----------------------------------------------------------------------------------------
    W.at("Sick Leave Paid By Employer")
    sk = wb["Sick Leave Paid By Employer"]
    sheet_text(sk, [
        ["Employer-paid sick leave - United States"],
        [f"No federal law requires private employers to pay for leave: {W.val('fed.paid_leave.private_employers.exists')} [{W.rid('fed.paid_leave.private_employers.exists')}]. "
         f"Unpaid job-protected family and medical leave under the federal family leave statute lasts up to {W.val('fed.fmla.weeks')} weeks "
         f"[{W.rid('fed.fmla.weeks')}] ({W.val('fed.fmla.military_caregiver.weeks')} weeks for military caregiver leave); it creates no wage type."],
        ["Paid sick leave required by a State or city law is paid through the wage rows: the hours taken are paid on the basic salary row 62100 (or the "
         "hourly equivalent) and are wages for every tax with the flags of that row. The accrual rates, caps, carry-over and payout rules of each State "
         f"are in {W.CCG_REF} Module 8 and the State annexes; the catalogue holds no separate statutory sick pay calculation, because there is no "
         "employer-paid sickness benefit that follows a reduced assessment base as in the template of another country."],
        ["Third-party sick pay (an insurer pays) is a flag, not a wage type: see the third-party sick pay flag row of this catalogue."]],
        {"A": 140}, 1)

    # ---- Tax credit ----------------------------------------------------------------------------------------
    W.at("Tax Credit")
    tc = wb["Tax Credit"]
    cred = [("ca.wh.allowance_credit.per_allowance", "California withholding allowance credit"),
            ("ar.sit.personal_credit", "Arkansas personal credit"), ("de.wh.personal_credit.per_exemption", "Delaware personal credit per exemption"),
            ("or.pit.allowance.credit", "Oregon allowance credit")]
    rows_tc = [["Tax credits at payroll - United States"],
               ["Federal level: the credits of the employee (for example dependents) reach withholding only through Step 3 of the withholding certificate "
                f"({F_STEP3()}); the catalogue holds no credit wage type. The certificate fields are inputs of the federal income tax withholding row."],
               ["State credits applied inside the State withholding computation (no separate wage type):"]]
    for k, lab in cred:
        rows_tc.append([W.line(k, lab)])
    sheet_text(tc, rows_tc, {"A": 140}, 1)

    # ---- coverage and guide ---------------------------------------------------------------------------------
    recs, un = RC.compute(symmap)
    assert not un, un
    cov = wb.create_sheet("Global WTC Coverage")
    g_rows = coverage_rows(grows, usrows, symmap, last)
    sheet_text(cov, g_rows, {"A": 12, "B": 46, "C": 18, "D": 60, "E": 60, "F": 30}, 1)
    HEADROWS["Global WTC Coverage"] = HEAD_COV
    for r_ in HEAD_COV:
        for c in cov[r_]:
            if c.value is not None:
                c.font = Font(name=FONT, size=11, bold=True)
    frg = wb.create_sheet("Form Reference Guide")
    guide_rows = form_guide(recs, symmap)
    sheet_text(frg, guide_rows, {"A": 44, "B": 52, "C": 34, "D": 12, "E": 70}, 2)
    for c in frg[2]:
        if c.value is not None:
            c.font = Font(name=FONT, size=11, bold=True)

    out = os.path.join(out_dir or W.WTCDIR, W.FILENAME)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    wb.save(out)
    res = dict(out=out, rows=rows, grows=grows, usrows=usrows, symmap=symmap, recs=recs, last=last)
    if sidecars:
        write_sidecars(res)
    return res


def F_STEP3():
    return W.dd("Form W-4 dependents and other credits (Step 3)")


HEAD_COV = []


def coverage_rows(grows, usrows, symmap, last):
    HEAD_COV.clear()
    r = []
    r.append(["Global WTC coverage - United States"])
    r.append([f"All {len(grows)} pay element codes of the global baseline are present with their codes preserved; country research decides the treatment; "
              f"{len(usrows)} country-specific wage types are added (codes US-nnn). Total rows of the catalogue: {len(grows) + len(usrows)}."])
    r.append(["Flag meaning. For an earning row Yes = the amount is wages for that tax (enters its base), No = excluded from the base, Yes-No = conditional "
              "(column D states on what), NA = not applicable. Deduction rows follow one of two classes, stated in column D of the row. Class 1, a reversal deduction (the "
              "Deduction rows that reverse an earning of the salary, overtime, salary addition, premium, housing and transport families): the row carries the flags of the reversed "
              "earning and Yes = the signed amount reduces that base. Class 2, a salary-reduction or pre-tax deduction (retirement plan deferral, health plan "
              "contribution): No = removed from the base before the tax. Tax, contribution, flag, reporting and accumulator rows carry NA unless stated. Columns Q1 to Q5 hold one fund each: "
              "social security (OASDI), Medicare, FUTA, State unemployment insurance, State disability and paid leave programmes. Column R is NA on every row: "
              "the United States has no statutory pension contribution at payroll other than OASDI (Q1). Orange dev-team columns (formula, calculation type, "
              "prorating, ignore if 0, enforce, in period reconciliation, year-to-date) are left empty."])
    r.append(["Out of scope: non-employee compensation and backup withholding on it (Form 1099-NEC) [US-OWN-008]; no wage type is built for it."])
    r.append([None])
    r.append(["Tax code legend (column G)"])
    HEAD_COV.append(len(r))
    r.append(["Code", "Meaning", "Rows", "Official source (v2.4 C9)"])
    HEAD_COV.append(len(r))
    cnt = {}
    for x in grows + usrows:
        cnt[x.tax_code] = cnt.get(x.tax_code, 0) + 1
    for code, t in M.TAXCODES.items():
        r.append([code, t["meaning"], cnt.get(code, 0), T.source_text(code)])
    r.append(["Architecture note (sub-national layers). Rows coded US-TX-06, US-TX-07 and US-TX-11 are jurisdiction-specific and mutually exclusive per employee "
              "and period: the State income tax row applies for the State chosen by the sourcing flag, reciprocity and the nonresident thresholds replace it, "
              "and the resident credit operates at assessment, not as a payroll deduction. The State of unemployment insurance coverage is chosen once per "
              "employee by the localization order and the State programmes follow it. Local rows add to, never replace, the State row."])
    r.append([None])
    r.append(["State layer index"])
    HEAD_COV.append(len(r))
    r.append(["State", "Name", "Income tax withholding", "Unemployment insurance (employer)", "Programmes, levies and local rows"])
    HEAD_COV.append(len(r))
    by = {}
    for x in usrows:
        s = getattr(x, "sym", "")
        m = re.match(r"(sit|sui|suiee|prog|levy|loc)_([A-Z]{2})", s)
        if m:
            by.setdefault(m.group(2), {}).setdefault(m.group(1), []).append(x.code)
    for st in W.STATES:
        d = by.get(st, {})
        sit = " ".join(d.get("sit", [])) or "no State income tax withholding"
        rest = " ".join(d.get("suiee", []) + d.get("prog", []) + d.get("levy", []) + d.get("loc", [])) or "none"
        r.append([st, W.STATE_NAMES[st], sit, " ".join(d.get("sui", [])) or "none", rest])
    r.append([None])
    r.append(["Global codes by family and country additions"])
    HEAD_COV.append(len(r))
    r.append(["Code", "Name", "Type", "Treatment summary", "Family / anchor"])
    HEAD_COV.append(len(r))
    for x in grows:
        fl = ",".join(f"{k}={v}" for k, v in x.flags.items() if v != "NA") or "no tax flag"
        r.append([int(x.code), x.name, x.global_type, fl, x.fam])
    for x in usrows:
        r.append([x.code, x.name, "country addition", ",".join(f"{k}={v}" for k, v in x.flags.items() if v != "NA") or "no tax flag", x.fam])
    return r


def form_guide(recs, symmap):
    r = [["Form Reference Guide - wage type category to Report Specification row"],
         ["Wage Type Category", "Spec File", "Sheet Name", "Row Number", "Notes"]]
    code2name = {}
    seen = set()
    for rec, hit, codes in recs:
        key = (hit[0], rec["spec"], rec["row"])
        if key in seen:
            continue
        seen.add(key)
        r.append([f"{' '.join(codes)} ({hit[0]})", rec["file"], rec["sheet"], rec["row"], rec["name"]])
    return r


BOX12 = re.compile(r"box 12 codes? ([A-Z]{1,2})(?![A-Za-z])")


def _rep_codes(r):
    """W-2 box 12 codes stated in the reporting cell, as 'w2_box12=<code>' (tested by C48 against the authority table)."""
    return [f"w2_box12={c}" for c in dict.fromkeys(BOX12.findall(r.rep or ""))] if os.path.exists(W.TABLE_BOX12) else []


CHECK_TABLE_REL = "02-wtc/_build/checks/US-W2-box12-codes.json"


def write_code_table():
    """Checkable form of the IRS code table (code -> validity) derived from the source-hunter file; the source file is not edited."""
    if not os.path.exists(W.TABLE_BOX12):
        return
    t = json.load(open(W.TABLE_BOX12, encoding="utf-8"))
    codes = {c["code"]: {"valid_from": c.get("valid_from"), "valid_to": c.get("valid_to")} for c in t["codes"]["w2_box12"]}
    out = dict(authority=t["authority"], register_id=t["register_id"], source_url=t["source_url"], valid_from=t["valid_from"],
               derived_from="00-official-sources/code-tables/US-W2-box12.json", codes={"w2_box12": codes})
    json.dump(out, open(os.path.join(W.BASE, CHECK_TABLE_REL), "w", encoding="utf-8"), indent=1)


def write_sidecars(res):
    write_code_table()
    rows, symmap = res["rows"], res["symmap"]
    # crosswalk (builder output used by C48 / C50)
    wt = {}
    for r in rows:
        wt[r.code] = dict(label=r.name, side=r.side, flags={k: {"value": v, "basis": r.basis.get(k) or (r.legal[0] if r.legal else "US-FEDS5-001")}
                                                            for k, v in r.flags.items() if v != "NA"},
                          reporting_codes=_rep_codes(r), payslip=bool(r.payslip), in_kind=bool(r.in_kind))
    cw = dict(schema="wtc-crosswalk", **({"code_table": CHECK_TABLE_REL} if os.path.exists(W.TABLE_BOX12) else {}), wtc_columns=dict(code="Mercans Code", explanation="Wage Type Explanation", category="Category",
                                                       reporting=REP_HDR, flags={f: M.FLAG_HDR[f] for f in M.FLAG_NAMES}), wage_types=wt)
    json.dump(cw, open(os.path.join(W.RESEARCH, "WTC-crosswalk.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    # reconciliation
    usage = list(csv.DictReader(open(os.path.join(W.DDDIR, "_build", "checks", "dd_element_usage.csv"), encoding="utf-8")))
    cons = []
    for u in usage:
        if u["spec_ids_citing"]:
            continue
        name = u["dd_element"]
        c = [r.code for r in rows if name in r.inputs]
        reason = "" if c else "notice template input (NY LL 195.1, CO PSL notice) per DD; not a wage-type input"
        cons.append((name, c, reason))
    RC.write_csv(res["recs"], [], rows, [], cons, os.path.join(W.CHECKS, "wtc_recon.csv"))
    # bindings
    with open(os.path.join(W.BASE, "_pipeline", "WTC-bindings.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["location", "key", "register_id", "effective_from", "facts_file"])
        for key, locs in sorted(W.USED.items()):
            k, _, eff = key.partition("@")
            for f in W.periods(k):
                if (f.get("effective_from") or "") == eff or not eff:
                    for loc in sorted(locs):
                        w.writerow([loc, k, f["register_id"], f.get("effective_from"), f["_file"]])
                    break
    import wtc_requests
    wtc_requests.main()


if __name__ == "__main__":
    od = sys.argv[sys.argv.index("--out") + 1] if "--out" in sys.argv else None
    res = build(od, sidecars=od is None)
    print("written", res["out"], "rows", len(res["rows"]), "recon", len(res["recs"]))
