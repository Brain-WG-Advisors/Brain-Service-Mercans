"""Build '02 Validation/<file>.xlsx' from _evidence/checks.json + review/curated.py (REGISTER dict).
Same sheets and styling as Netherlands/_tool/build_workbook.py, generalised for any country.
Usage: python -I build_workbook.py "<package>/02 Validation"   (refuses to overwrite an existing file)"""
import importlib.util
import json
import os
import sys

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter

HEAD = PatternFill("solid", fgColor="1F3864")
SEVFILL = {"High": "F8CBAD", "Medium": "FFE699", "Low": "DDEBF7", "Observation": "E2EFDA"}
WRAP = Alignment(wrap_text=True, vertical="top")


def sheet(wb, title, header, rows, widths, freeze="A4", heading=None):
    ws = wb.create_sheet(title)
    ws["A1"] = heading or title
    ws["A1"].font = Font(bold=True, size=13)
    ws.append([])
    ws.append(header)
    for c in ws[3]:
        c.font = Font(bold=True, color="FFFFFF")
        c.fill = HEAD
        c.alignment = WRAP
    for r in rows:
        ws.append(list(r))
    for i, w in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = w
    for row in ws.iter_rows(min_row=4):
        for c in row:
            c.alignment = WRAP
    ws.freeze_panes = freeze
    return ws


def build(val):
    spec = importlib.util.spec_from_file_location("curated", os.path.join(val, "review", "curated.py"))
    CU = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(CU)
    K = CU.REGISTER
    out = os.path.join(val, K["file"])
    if os.path.exists(out):
        sys.exit(f"refusing to overwrite {out}; bump the version in REGISTER['file']")
    d = json.load(open(os.path.join(val, "_evidence", "checks.json"), encoding="utf-8"))
    wb = Workbook()
    ws = wb.active
    ws.title = "Cover"
    ws["A1"] = K["title"]
    ws["A1"].font = Font(bold=True, size=13)
    ws.append([])
    for k, v in K["cover"]:
        ws.append([k, v])
    ws.append(["Scope", "Validation only: format and content of the return, statutory recalculation, "
                        "cross-document reconciliation. Findings go to implementation/dev; nothing was "
                        "regenerated or resubmitted."])
    ws.column_dimensions["A"].width = 26
    ws.column_dimensions["B"].width = 110
    for row in ws.iter_rows(min_row=3):
        row[0].font = Font(bold=True)
        for c in row:
            c.alignment = WRAP

    ov = K.get("overrides", {})
    res = {}
    for c in d["checks"]:
        res[c["result"]] = res.get(c["result"], 0) + 1
    reviewed_pass = sum(1 for c in d["checks"] if c["result"] == "Finding" and ov.get(c["id"], ("", ""))[0] == "Pass")
    sev = {}
    for f in K["findings"]:
        sev[f[1]] = sev.get(f[1], 0) + 1
    nt_total = len(K["not_tested"]) + sum(1 for n in d["not_tested"] if n["id"] not in set(K.get("skip_auto_nt", [])))
    counts = (f"{len(d['checks'])} automated checks: Pass {res.get('Pass', 0)}, exception {res.get('Finding', 0)} "
              f"(of which {reviewed_pass} cleared on review), not tested {res.get('Not tested', 0)}, out of scope "
              f"{res.get('Out of scope', 0)}. Not Tested register: {nt_total} items. Findings register: "
              + (", ".join(f"{k} {sev[k]}" for k in ("High", "Medium", "Low", "Observation") if k in sev) or "none") + ".")
    sheet(wb, "Executive Summary", ["Item", "Text"], K["summary"] + [("Check counts", counts)], [26, 120],
          freeze=None, heading="Executive summary (qualified)")
    sheet(wb, "Assumptions", ["#", "Assumption / method note"], K["assumptions"], [6, 130],
          heading="Assumptions and method notes")
    ws = sheet(wb, "Findings Register", ["ID", "Severity", "Area", "Finding", "Evidence", "Impact",
                                         "Statutory basis", "Status", "Records affected"],
               K["findings"], [7, 11, 22, 70, 50, 30, 36, 9, 10])
    for row in ws.iter_rows(min_row=4):
        fill = SEVFILL.get(row[1].value)
        if fill:
            row[1].fill = PatternFill("solid", fgColor=fill)

    cov = []
    for c in d["checks"]:
        r, note = c["result"], c.get("detail", "")
        if c["id"] in ov:
            o = ov[c["id"]]
            if o[0] == "Pass":
                r = "Pass (reviewed)" if c["result"] in ("Finding", "Not tested") else r
            elif o[0] in ("Not tested", "Out of scope"):
                r = o[0]
            else:
                r = "Finding"
            note = o[1]
        cov.append((c["id"], c["area"], c["check"], c["population"], r, note))
    for row in K.get("extra_coverage", []):
        cov.append(row)
    sheet(wb, "Coverage", ["Control", "Area", "Check", "Population", "Result", "Review note"], cov,
          [10, 18, 70, 22, 15, 70], heading="Coverage - every check run, with its result")

    rec = [(r["item"], r["a_src"], r["a"], r["b_src"], r["b"], r["diff"],
            K.get("recon_notes", {}).get(r["item"], r["result"])) for r in d["recon"]]
    for item, a_src, a, b_src, b, *note in K.get("extra_recon", []):
        rec.append((item, a_src, a, b_src, b, round(a - b, 2),
                    note[0] if note else ("Pass" if abs(a - b) <= 0.01 else "Explained (see note)")))
    ws = sheet(wb, "Reconciliation", ["Item", "Source A", "Amount A", "Source B", "Amount B", "Difference",
                                      "Result"], rec, [30, 44, 14, 52, 14, 12, 30],
               heading=f"Reconciliation (totals, {K.get('currency', '')})")
    for row in ws.iter_rows(min_row=4):
        for c in (row[2], row[4], row[5]):
            c.number_format = "#,##0.00"

    rc = d.get("recalc", [])
    if rc:
        hdr = list(rc[0].keys())
        ws = sheet(wb, "Recalculation", hdr, [[r.get(h) for h in hdr] for r in rc], [14] + [13] * (len(hdr) - 1),
                   heading=K.get("recalc_heading", "Per-employee statutory recalculation"))
        for row in ws.iter_rows(min_row=4):
            for c in row:
                if isinstance(c.value, float):
                    c.number_format = "#,##0.00"

    nt = list(K["not_tested"])
    skip = set(K.get("skip_auto_nt", []))
    for n in d["not_tested"]:
        if n["id"] not in skip:
            nt.append((n["id"], n["item"], n["reason"], n["unblock"]))
    sheet(wb, "Not Tested", ["ID", "Item", "Reason", "What would unblock it"], nt, [8, 40, 70, 50],
          heading="Not tested - reason and what would unblock it")
    sheet(wb, "Sources", ["ID", "Publisher", "Document", "URL / location", "Version / date", "Used for"],
          K["sources"], [6, 16, 44, 60, 30, 50], heading="Sources (official, read 14-10-2026; sha256 in "
                                                        "references/<country>/2026/sources.md)")
    wb.save(out)
    print("written", out)


if __name__ == "__main__":
    build(sys.argv[1])
