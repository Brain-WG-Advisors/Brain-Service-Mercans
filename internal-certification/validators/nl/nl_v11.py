"""Netherlands full validation - builds <workbook>_v1.1.xlsx from v1.0 (v1.0 untouched).
Adds the full-pass controls (Coverage), the new findings (Findings Register) and replaces the Not Tested sheet
with the items that still need a document. Usage: python -I nl_v11.py"""
import os
import sys

from openpyxl import load_workbook
from openpyxl.styles import Alignment, PatternFill

sys.stdout.reconfigure(encoding="utf-8")
NL = r"C:\Users\instituto\Documents\internal-certification\Netherlands"
SEV = {"High": "F8CBAD", "Medium": "FFE699", "Low": "DDEBF7", "Observation": "E2EFDA"}
WRAP = Alignment(wrap_text=True, vertical="top")
TODAY = "14-10-2026"

DATA = {
    "Quest Software - 2026-09": {
        "file": "NL_Quest_2026-09_Validation.xlsx",
        "findings": [
            ("F-08", "High", "Authority acceptance",
             "There is no Digipoort status response or Belastingdienst acknowledgement for return 809615253L01P20260901. The "
             "'Wage Tax Overview' in the pack is produced by HRBLIZZ, not by the authority.",
             "Pack contents (8 files); no getStatussenProces / ontvangstbevestiging.", "Acceptance of the September return unproven.",
             "Digipoort koppelvlak; Gegevensspecificaties aangifte loonheffingen 2026.", "Open - requested", 1),
            ("F-09", "Observation", "Premium - gedifferentieerde Whk",
             "The return applies a Whk rate of 1.45% (TotPrGediffWhk 384 / TotPrlnWhkAnw 26,470). Quest is in sector 42 "
             "(Groothandel II). On its premium wage (about EUR 0.32 m a year, annualised from September) it is a small "
             "employer, for which the 2026 rate is the sector rate of 1.45% (WGA 0.91% + ZW-flex 0.54%, Tabel 10) - equal to "
             "the declared rate. INFERENCE: the size class is set on the 2024 premium wage, which is not in the pack.",
             "Return CollectieveAangifte; Sect 042; Handboek 2026 §7.6.1 and Bijlage 1 Tabel 10.",
             "None if small employer; a medium or large employer would have an individual rate.",
             "Handboek Loonheffingen 2026 §7.6, Tabel 10.", "Open - mededeling requested", 1),
            ("F-10", "Medium", "Payslip - SV wage",
             "The leaver 96083's payslip adds the severance payment (35,625.93) to the SVW (SV wage) column. The severance is "
             "'loon uit vroegere dienstbetrekking' on its own income relation (SrtIV 62), which is not SV wage; the return is "
             "correct (LnSV 13,580.14 on IKV 0001, nil on IKV 0002).",
             "Payslip 96083 SVW total 49,206.07 vs return LnSV 13,580.14.", "Employee document overstates the SV wage; no premium effect.",
             "Handboek 2026 §4.7.1, §17.2.6.", "Open", 1),
            ("F-11", "Observation", "Allowances - home allowance",
             "'Home allowance' (62810) of EUR 100 a month is paid untaxed (not in Table, BT or SVW) to 3 employees. The targeted "
             "exemption for home working is EUR 2.45 per home-working day (2026) - at most EUR 53.90 in September (22 days) "
             "or EUR 43.69 a month as a fixed allowance. The excess (EUR 46.10-56.31 per employee) is untaxed only if it is "
             "designated under the WKR (vrije ruimte / eindheffing).",
             "Payslips 70030, 76628, 89826: 62810 100.00, columns Table/BT/SVW blank.",
             "Up to EUR 168.93 a month of wage if not designated.", "Handboek 2026 §22.1.12, §23.1.2, Bijlage (thuiswerken EUR 2,45).",
             "Open - confirmation requested", 3),
        ],
        "coverage": [
            ("H-11", "Payslip header", "Written contract, on-call, indefinite contract, loonheffingskorting and ZVW/WW/WIA on the "
             "payslip = return indicators", "4 employees", "Pass", "All 4 match the employment IKV (leaver 96083 compared with IKV 0001)."),
            ("H-12", "Payslip header", "Payslip hours = AantVerlU", "4 employees", "Finding", "See F-01/F-02 (173.33 vs 176; leaver 0)."),
            ("G-S5a", "Base composition", "Each pay element has one fiscal treatment (Table/BT/SVW) across all employees",
             "12 pay elements", "Pass", "Read from the Table/BT/SVW columns of every payslip line."),
            ("G-S5c", "Base composition", "Fiscal treatment matches the statutory nature of each element", "12 pay elements",
             "Pass (reviewed)", "Pension premium deductible for all loonheffingen; commission, holiday hours and severance at "
             "the special rate; car addition in Table and SVW; WKR items outside wage. Exceptions: F-10 (payslip SVW), F-11."),
            ("G-S5b", "Base composition", "Per employee: payslip Table+BT = LnLbPh, BT = LnTabBB, SVW = LnSV", "4 employees",
             "Finding", "See F-10."),
            ("W-01", "Premium", "Whk rate against the 2026 official framework (sector table / min-max)", "1 return", "Finding",
             "See F-09."),
            ("D-12", "Wage tax", "Alleenstaandeouderenkorting", "0 AOW-age IKVs", "Pass", "No AOW-age employee in the run."),
        ],
        "not_tested": [
            ("NT-01", "Acceptance of the return", "No Digipoort response in the pack (F-08).",
             "Digipoort status response for 809615253L01P20260901 - requested (followups.md, draft)."),
            ("NT-02", "Exact Whk rate", "Mededeling/beschikking 2026 not in the pack (F-09).", "Whk mededeling 2026 - requested."),
            ("NT-03", "Payslip cumulative roll-forward", "Only September payslips.", "August 2026 payslips or YTD G2N - requested."),
            ("NT-05", "Jaarloon BT derivation", "Needs the prior-year wage.", "Jaarloon BT build-up per employee - requested."),
            ("NT-06", "WKR designation of the home allowance", "Designation is an employer choice not visible in the pack (F-11).",
             "WKR designation / eindheffing calculation - requested."),
        ],
    },
    "Excerpta Medica - 2026-09": {
        "file": "NL_Excerpta_2026-09_Validation.xlsx",
        "findings": [
            ("F-06", "High", "Authority acceptance",
             "There is no Digipoort status response or Belastingdienst acknowledgement for return 822945526L01P20260901; the "
             "'Wage Tax Overview' is an HRBLIZZ document.", "Pack contents (8 files).", "Acceptance of the September return unproven.",
             "Digipoort koppelvlak; Gegevensspecificaties 2026.", "Open - requested", 1),
            ("F-07", "Medium", "Payslip - SV wage",
             "M1022936's payslip adds the statutory transition payment (62900, 1,098.37) to the SVW column. The transition "
             "payment is 'loon uit vroegere dienstbetrekking' (green table), not SV wage; the return is correct (LnSV 7,608.97).",
             "Payslip M1022936 SVW 8,707.34 vs return LnSV 7,608.97.", "Employee document overstates the SV wage; no premium effect.",
             "Handboek 2026 §4.7.1, §17.2.6.", "Open", 1),
            ("F-08", "Observation", "Allowances - phone allowance",
             "'Phone Allowance' (62805, EUR 21.00-33.50) is paid untaxed to 10 employees. A fixed phone allowance has no "
             "targeted exemption; it is untaxed only if designated under the WKR (vrije ruimte / eindheffing). Home Office "
             "(62834, EUR 45.00, 3 employees) fits the EUR 2.45/day targeted exemption; travel allowance (62804, 45.81) fits "
             "EUR 0.23/km.", "Payslips: 62805 columns Table/BT/SVW blank.", "EUR 260.00 a month of wage (10 employees) if not designated.",
             "Handboek 2026 h.10 (WKR), §22.1.12.", "Open - confirmation requested", 10),
        ],
        "coverage": [
            ("H-11", "Payslip header", "Written contract, on-call, indefinite contract, loonheffingskorting and ZVW/WW/WIA on the "
             "payslip = return indicators", "84 employees", "Pass", "All 84 match (English template read by word position)."),
            ("H-12", "Payslip header", "Payslip hours worked = AantVerlU", "84 employees", "Pass (reviewed)",
             "3 differences are unpaid/parental-unpaid leave (79490/79491): the return reduces paid hours (e.g. M1022934 "
             "156 x 86.2% = 134); the payslip shows contractual hours as the Handboek requires."),
            ("G-S5a", "Base composition", "Each pay element has one fiscal treatment across all employees", "29 pay elements",
             "Pass", "Read from the Table/BT/SVW columns of every payslip line."),
            ("G-S5c", "Base composition", "Fiscal treatment matches the statutory nature of each element", "29 pay elements",
             "Pass (reviewed)", "Pension, cycle-to-work and 30%-ruling deductions reduce all bases; bonuses/holiday allowance "
             "for leavers at the special rate; WKR/targeted exemptions outside wage. Exceptions: F-07, F-08."),
            ("G-S5d", "Base composition", "30%-ruling allowance <= 30% of wage incl. allowance; wage excl. allowance above the "
             "2026 salary norm (EUR 48,013)", "30%-ruling employees", "Pass", "M1023003: 1,311.66 = 23.7% of 5,529.02; "
             "wage excl. allowance about EUR 50.6k a year."),
            ("G-S5b", "Base composition", "Per employee: payslip Table+BT = LnLbPh, BT = LnTabBB, SVW = LnSV", "84 employees",
             "Finding", "See F-07."),
            ("W-01", "Premium", "Whk rate against the 2026 official framework", "1 return", "Pass (reviewed)",
             "1.71%: medium employer (premium wage about EUR 4.1 m a year), weighted between sector 44 (2.10%) and an "
             "individual rate within the 2026 bounds 0.38%-6.08% (§7.6.2-7.6.3). Exact rate needs the beschikking (NT-02)."),
            ("D-12", "Wage tax", "Alleenstaandeouderenkorting", "1 AOW-age IKV", "Pass (reviewed)",
             "M1023246: withheld 452.16 matches neither column (485.08 excl. / 440.08 incl. AOK) - already F-01."),
        ],
        "not_tested": [
            ("NT-01", "Acceptance of the return", "No Digipoort response in the pack (F-06).",
             "Digipoort status response for 822945526L01P20260901 - requested (followups.md, draft)."),
            ("NT-02", "Exact Whk rate", "Beschikking 2026 not in the pack; plausibility passed (W-01).", "Whk beschikking 2026 - requested."),
            ("NT-03", "What the August correction changed", "Original August message not supplied.",
             "August 2026 loonaangifte as first submitted - requested."),
            ("NT-05", "Payslip cumulative roll-forward", "Only September payslips.", "August 2026 payslips or YTD G2N - requested."),
            ("NT-07", "WKR designation of phone allowance", "Employer choice not visible in the pack (F-08).",
             "WKR designation / eindheffing calculation - requested."),
        ],
    },
    "Sherwin Williams - 2026-09": {
        "file": "NL_SherwinWilliams_2026-09_Validation.xlsx",
        "findings": [
            ("F-10", "Medium", "Payslip - insurance indicators",
             "Payslip ZVW/WW/WIA indicators contradict the return for 6 employees: the 3 AOW-age employees (0420831, 0421178, "
             "0426237) show WW/WIA 'Ja' although they are no longer insured (return N/N, correct); 1202221 (25, regular "
             "employee) shows 'Nee/Nee' while insured (return J/J, correct); the new hires 1346647 and 1351879 show no ZVW code.",
             "Payslip header 'ZVW/WW/WIA' vs return CdZvw/IndWW/IndWAO.", "Employee documents wrong; return correct.",
             "Handboek 2026 §27 (loonstrook); Wet WW/WIA insured status.", "Open", 6),
            ("F-11", "Medium", "Payslip - table wage",
             "For 8 employees the payslip's 'Tabel' column omits pay element 62730 'Maandelijkse vergoeding' (EUR 167-174): "
             "e.g. 1257701 shows a table wage of 3,004.86 while the tax (455.50) is correctly computed on 3,171.94, the table "
             "wage declared in the return (LnLbPh). The element is in the SVW column and in the return.",
             "Payslip Tabel totals vs return LnLbPh for 1257701, 1242108, 1170228, 1191478, 1166406, 1196982, 1146506, 1187109.",
             "Employee cannot reconcile the withholding; no tax effect.", "Handboek 2026 §27 (loonstrook).", "Open", 8),
        ],
        "coverage": [
            ("H-11", "Payslip header", "Written contract, on-call, indefinite contract, loonheffingskorting and ZVW/WW/WIA on the "
             "payslip = return indicators", "222 employees", "Finding", "216 match; 6 see F-10."),
            ("H-12", "Payslip header", "Payslip verloonde uren = AantVerlU", "222 employees", "Finding", "See F-03 (173.33 vs 176)."),
            ("G-S5a", "Base composition", "Each pay element has one fiscal treatment across all employees", "58 pay elements",
             "Pass", "Read from the Tabel/BT/SVW columns of all 317 payslip pages (September and retro slips)."),
            ("G-S5c", "Base composition", "Fiscal treatment matches the statutory nature of each element", "58 pay elements",
             "Pass (reviewed)", "PAWW and pension premiums deductible for all loonheffingen (Handboek 2026 §2 grondslag); "
             "overtime, vakantiegeld, eindejaarsuitkering at the special rate; 30% bruto/netto, onbelaste reis-/km-vergoeding, "
             "VOG, jubileum outside wage. Exception: 62730 on the payslip only (F-11)."),
            ("G-S5b", "Base composition", "Per employee (September slip): Tabel+BT = LnLbPh, BT = LnTabBB, SVW = LnSV", "222 employees",
             "Finding", "214 match; 8 see F-11."),
            ("W-01", "Premium", "Whk rate against the 2026 official framework", "1 return", "Pass (reviewed)",
             "1.83%: large employer (premium wage about EUR 11.8 m a year) - individual rate within the 2026 bounds "
             "0.38%-6.08% (§7.6.2). Exact rate needs the beschikking (NT-02)."),
            ("D-12", "Wage tax", "Alleenstaandeouderenkorting", "3 AOW-age IKVs", "Finding",
             "0426237: Pass - columns equal at its tabelloon. 0420831, 0421178: withheld on the AOK column - see F-05."),
        ],
        "not_tested": [
            ("NT-01", "Acceptance of this return", "The response in the pack is for another loonheffingennummer (F-01).",
             "Digipoort status response for 002879487L01P20260901 - requested (followups.md, draft)."),
            ("NT-02", "Exact Whk rate", "Beschikking not in the pack; plausibility passed (W-01).", "Whk beschikking 2026 - requested."),
            ("NT-03", "Per-employee retro allocation", "Original January-August messages not supplied.",
             "Original 2026 messages or pay-element retro export - requested."),
            ("NT-05", "Payslip cumulative roll-forward", "Prior-run payslips not supplied.", "August 2026 payslips - requested."),
            ("NT-07", "AOK entitlement (0420831, 0421178)", "Entitlement depends on the employee's AOW status (F-05).",
             "Client confirmation - requested."),
        ],
    },
}


def run():
    for folder, D in DATA.items():
        base = os.path.join(NL, folder, "02 Validation")
        src = os.path.join(base, D["file"])
        out = src.replace(".xlsx", "_v1.1.xlsx")
        if os.path.exists(out):
            sys.exit(f"refusing to overwrite {out}")
        wb = load_workbook(src)
        # cover: version line
        ws = wb["Cover"]
        ws.append(["Version", f"v1.1 - full validation pass {TODAY}: every 'Not tested' item testable with the pack was "
                              "tested (payslip header fields, base composition per pay element, Whk rate framework, AOK); "
                              "the remaining items need a document from the client (Not Tested sheet)."])
        for c in ws[ws.max_row]:
            c.alignment = WRAP
        # findings
        ws = wb["Findings Register"]
        for f in D["findings"]:
            ws.append(list(f))
            row = ws[ws.max_row]
            for c in row:
                c.alignment = WRAP
            row[1].fill = PatternFill("solid", fgColor=SEV[f[1]])
        # coverage
        ws = wb["Coverage"]
        for r in D["coverage"]:
            ws.append(list(r))
            for c in ws[ws.max_row]:
                c.alignment = WRAP
        # not tested: replace data rows
        ws = wb["Not Tested"]
        ws.delete_rows(4, ws.max_row)
        for r in D["not_tested"]:
            ws.append(list(r))
            for c in ws[ws.max_row]:
                c.alignment = WRAP
        # executive summary note
        ws = wb["Executive Summary"]
        sev = {}
        for f in D["findings"]:
            sev[f[1]] = sev.get(f[1], 0) + 1
        ws.append(["Full validation (v1.1)", f"{len(D['coverage'])} controls added from the full pass; "
                   f"{len(D['findings'])} new findings (" + ", ".join(f"{k} {v}" for k, v in sev.items()) +
                   f"). {len(D['not_tested'])} items remain Not tested because they need a client document; each is "
                   "requested in followups.md (draft, not sent)."])
        for c in ws[ws.max_row]:
            c.alignment = WRAP
        wb.save(out)
        print("written", out)


if __name__ == "__main__":
    run()
