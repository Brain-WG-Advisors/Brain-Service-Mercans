"""Build 02 Validation/<file>.xlsx from _evidence/checks.json + curated.py."""
import json
import os
import sys

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter

from clients import CLIENTS, NL
import curated as CU

HEAD = PatternFill("solid", fgColor="1F3864")
SEVFILL = {"High": "F8CBAD", "Medium": "FFE699", "Low": "DDEBF7",
           "Observation": "E2EFDA"}
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


def build(key):
    C, K = CLIENTS[key], CU.CLIENTS[key]
    base = os.path.join(NL, C["folder"], "02 Validation")
    d = json.load(open(os.path.join(base, "_evidence", "checks.json"), encoding="utf-8"))
    wb = Workbook()
    ws = wb.active
    ws.title = "Cover"
    ws["A1"] = "Netherlands statutory payroll reports - internal certification validation"
    ws["A1"].font = Font(bold=True, size=13)
    ws.append([])
    for k, v in K["cover"]:
        ws.append([k, v])
    ws.append(["Systematiek", "Loon-over (see Assumptions A2)"])
    ws.append(["Scope", "Validation only: format and content of the return, statutory "
                        "recalculation, cross-document reconciliation. Findings go to "
                        "implementation/dev; nothing was regenerated or resubmitted."])
    ws.column_dimensions["A"].width = 26
    ws.column_dimensions["B"].width = 110
    for row in ws.iter_rows(min_row=3):
        row[0].font = Font(bold=True)
        for c in row:
            c.alignment = WRAP

    # executive summary with control counts
    res = {}
    for c in d["checks"]:
        res[c["result"]] = res.get(c["result"], 0) + 1
    ov = K.get("overrides", {})
    reviewed_pass = sum(1 for c in d["checks"] if c["result"] == "Finding"
                        and ov.get(c["id"], ("", ""))[0] == "Pass")
    sev = {}
    for f in K["findings"]:
        sev[f[1]] = sev.get(f[1], 0) + 1
    counts = (f"{len(d['checks'])} automated checks: Pass {res.get('Pass', 0)}, "
              f"exception {res.get('Finding', 0)} (of which {reviewed_pass} cleared on "
              f"review). Not tested: {len(K['not_tested'])}. Findings register: "
              + ", ".join(f"{k} {sev[k]}" for k in ("High", "Medium", "Low", "Observation")
                          if k in sev) + ".")
    sheet(wb, "Executive Summary", ["Item", "Text"],
          K["summary"] + [("Check counts", counts)], [26, 120], freeze=None,
          heading="Executive summary (qualified)")

    sheet(wb, "Assumptions", ["#", "Assumption / method note"],
          CU.COMMON_ASSUMPTIONS, [6, 130], heading="Assumptions and method notes")

    ws = sheet(wb, "Findings Register",
               ["ID", "Severity", "Area", "Finding", "Evidence", "Impact",
                "Statutory basis", "Status", "Records affected"],
               K["findings"], [7, 11, 22, 70, 50, 30, 36, 9, 10])
    for row in ws.iter_rows(min_row=4):
        fill = SEVFILL.get(row[1].value)
        if fill:
            row[1].fill = PatternFill("solid", fgColor=fill)

    cov = []
    for c in d["checks"]:
        r, note = c["result"], c.get("detail", "")
        if r == "Finding" and c["id"] in ov:
            r, note = ov[c["id"]][0] if ov[c["id"]][0] == "Pass" else "Finding", ov[c["id"]][1]
            if r == "Pass":
                r = "Pass (reviewed)"
        cov.append((c["id"], c["area"], c["check"], c["population"], r, note))
    sheet(wb, "Coverage", ["Control", "Area", "Check", "Population", "Result",
                           "Review note"], cov, [14, 20, 70, 26, 14, 60],
          heading="Coverage - every check run, with its result")

    rec = [(r["item"], r["a_src"], r["a"], r["b_src"], r["b"], r["diff"],
            r["result"]) for r in d["recon"]]
    for item, a_src, a, b_src, b in K.get("extra_recon", []):
        rec.append((item, a_src, a, b_src, b, round(a - b, 2),
                    "Pass" if abs(a - b) <= 0.01 else "Explained (see note)"))
    ws = sheet(wb, "Reconciliation", ["Item", "Source A", "Amount A", "Source B",
                                      "Amount B", "Difference", "Result"],
               rec, [30, 44, 14, 52, 14, 12, 18], heading="Reconciliation (totals, EUR)")
    for row in ws.iter_rows(min_row=4):
        for c in (row[2], row[4], row[5]):
            c.number_format = "#,##0.00"
    if key == "sherwin":
        ws.append([])
        ws.append(["Note", "Under loon-over the period block holds September wage only; "
                   "the G2N and GL also carry the retro paid in September, which is "
                   "declared in the 8 correction blocks. The per-rubriek differences "
                   "above add up to EUR 3.008,17 against correction saldi of EUR 3.010 "
                   "(saldi are whole euros per period)."])

    rows = []
    for r in d["ikv_rows"]:
        rows.append((r["PersNr"], r["NumIV"], r["SrtIV"], r["LbTab"],
                     "J" if r["LHK"] else "N", "Yes" if r["AOW"] else "No",
                     r["LnLbPh"], r["LnTabBB"], r.get("tabelloon"),
                     r.get("exp_regular"), r.get("bt_tax"), r.get("bt_rate"),
                     r["IngLbPh"], r["VerrArbKrt"], r.get("exp_ak")))
    ws = sheet(wb, "Recalculation", ["PersNr", "NumIV", "SrtIV", "LbTab", "LHK",
                                     "AOW col.", "Loon LB/PH", "Loon BB", "Tabelloon",
                                     "Table tax (2026)", "Implied BT tax",
                                     "Implied BT %", "IngLbPh declared",
                                     "VerrArbKrt declared", "Table arbeidskorting"],
               rows, [11, 7, 6, 6, 5, 8, 12, 12, 12, 12, 12, 9, 12, 12, 12],
               heading="Per-IKV recalculation against the 2026 monthly table")
    for row in ws.iter_rows(min_row=4):
        for c in row[6:]:
            c.number_format = "#,##0.00"

    nt = list(K["not_tested"])
    for n in d["not_tested"]:
        if n.get("id") in ("A-07", "E-08") or "Payslip" in n.get("item", ""):
            continue
        nt.append((n.get("id", ""), n.get("item", ""), n.get("reason", ""),
                   n.get("unblock", "")))
    sheet(wb, "Not Tested", ["ID", "Item", "Reason", "What would unblock it"], nt,
          [8, 40, 70, 50], heading="Not tested - reason and what would unblock it")

    sheet(wb, "Sources", ["Publisher", "Document", "URL / location", "Version / date",
                          "Used for"], CU.SOURCES, [16, 44, 60, 30, 50],
          heading="Sources (official)")
    out = os.path.join(base, K["file"])
    wb.save(out)
    print("written", out)


if __name__ == "__main__":
    for k in sys.argv[1:]:
        build(k)
