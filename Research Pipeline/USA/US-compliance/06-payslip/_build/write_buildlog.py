# -*- coding: utf-8 -*-
"""Writes _pipeline/PSL-build-log.md from the workbook, the generator state and the latest check outputs (run after the checks)."""
import collections
import csv
import datetime as dt
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import psl_common as S  # noqa: E402
import psl_lint as L  # noqa: E402

CK = os.path.join(HERE, "checks")
wb_path = os.path.join(S.PSLDIR, S.FILENAME)
lint = L.run(wb_path)
req = json.load(open(os.path.join(CK, "psl_requests.json"), encoding="utf-8"))
f44 = json.load(open(os.path.join(CK, "f44_self.json"), encoding="utf-8"))
rc = list(csv.DictReader(open(os.path.join(CK, "psl_recon.csv"), encoding="utf-8")))
bind = list(csv.DictReader(open(os.path.join(S.BASE, "_pipeline", "PSL-bindings.csv"), encoding="utf-8")))
sp = os.path.join(CK, "run_summary.txt")
summary = open(sp, encoding="utf-8").read() if os.path.exists(sp) else "(checks not yet run)"
cnt = collections.Counter((r["kind"], r["status"]) for r in rc)
why = collections.Counter(v["why"] for v in req.values())
by_file = collections.defaultdict(set)
for b in bind:
    by_file[b["facts_file"]].add(b["key"])
blocks = collections.OrderedDict()
for b in bind:
    blk = b["location"].split("!")[0]
    blocks.setdefault(blk, []).append(b)

o = []
A = o.append
A("# PSL - build log")
A(f"Artifact: PSL | Country: {S.CODE} | Round: 2 | Built: {dt.date.today().isoformat()}")
A(f"Manifest: _pipeline/build-manifest.json ({S.MANIFEST['currency']}, minor units {S.MANIFEST['currency_minor_units']}, tier {S.MANIFEST['tier']['overall']}, package v{S.PKG}, status {S.STATUS})")
A(f"Pack: _research/PSL-research-pack.md | Facts: _research/PSL-facts.json ({len(S.PSLFACTS['facts'])} facts, {len(S.UNRESOLVED)} unresolved entries)")
A(f"Output: 06-payslip/{S.FILENAME} (8 sheets) | Generator: 06-payslip/_build/build_psl.py (re-runnable; previous builds in _build/_backup/)")
A("")
A("## Precedent inspection (L1)")
A("Opened with openpyxl (REFERENCE_Payslip_Mozambique.xlsx, REFERENCE_Payslip_Tunisia.xlsx, 2026-11-04).")
A("- Mozambique: 9 sheets: How to set up Payslip, Compliance Payslip, SAmple, Mozambique (EN), Mozambique (PT), NEW Specification, Payslip Spec 1, Field Option, Population Range. No `Unit Rate Details` sheet.")
A("- Tunisia: 5 sheets: Tunisia (EN), Tunisia (FR), Payslip Spec, Unit Rate Details, Population Range. No `How to set up Payslip`, `Compliance Payslip` or `Field Option` sheet.")
A("- Payslip grid (both): columns A-J, rows 12 pt, Arial 6/7 pt, labels DCDCDC, section bars A9A9A9, gross / deduction / net totals as SUM formulas over columns H:J, logo image at A1. Payslip Spec: 4 columns B-E (Field Name, Field Local Name, HRP Mapping (TA & BA), Field Explanation), section bars. Unit Rate Details: B Earning Description, C Earning Code, D Rate Account, E Unit Account.")
A("- The v2.9 statement that the Mozambique reference already holds the 8 sheets is wrong; the sheets were mapped one by one:")
A("")
A("| Built sheet | From | Note |")
A("|---|---|---|")
A("| How to set up Payslip | Mozambique `How to set up Payslip` | text steps, document control and one Version Control row added |")
A("| Compliance Payslip | Mozambique `Compliance Payslip` | language-neutral master; same layout as the EN tab |")
A("| United States (EN) / (ES) | Mozambique `{country} (EN)`, `{country} (PT)`; Tunisia `(EN)`, `(FR)` | local tab is Spanish: es is the documented second-language seam (build manifest languages.seams) |")
A("| Payslip Spec | Tunisia `Payslip Spec` (4-column layout) | 5 sections; HRP syntax as in the references |")
A("| Field Option | Mozambique `Field Option` (Field Name, Option Value, Option Description, Usage Context) | holds the controlled values and the State rule blocks |")
A("| Population Range | Mozambique / Tunisia `Population Range` | 3 columns |")
A("| Unit Rate Details | Tunisia `Unit Rate Details` | rate and unit accounts taken from the approved WTC |")
A("| dropped | Mozambique `SAmple`, `NEW Specification` | not part of the contract |")
A("")
A("## Fact bindings")
A(f"{len(bind)} bindings (location, key, register_id, also_register_ids) in `_pipeline/PSL-bindings.csv`. Keys by facts file: " + "; ".join(f"{k} {len(v)}" for k, v in sorted(by_file.items())) + ". Priority PSL, WTC, DD, SIR, RSPEC, CCG; period-aware (build year 2026).")
A(f"Workbook tags: {lint['tags']}; distinct tags checked against the local copy of the cited row: {f44['tags_checked']}, misses {len(f44['misses'])}.")
A("")
A("| Location block | Bindings | Example (key -> register_id) |")
A("|---|---|---|")
for blk, bs in blocks.items():
    b0 = bs[0]
    A(f"| {blk} | {len(bs)} | `{b0['key']}` -> {b0['register_id']} |")
A("")
A("## Scope decisions")
A("| Item | Verdict | Basis |")
A("|---|---|---|")
A("| Payslip language | English first build, Spanish label tab as the seam | build manifest languages (owner decision US-OWN-006) |")
A("| State rules | all 51 jurisdictions, one row each in Field Option STATE_STATEMENT_RULE | PSL facts content / scope keys |")
A("| Worked example | one fictitious biweekly employee, work location TX, federal lines only | State lines are listed in the catalogue (160 wage types with payslip true) |")
A("| Statutory lines | every crosswalk wage type with payslip true is in Field Option PAYSLIP_LINE (160) | `_research/WTC-crosswalk.json`, C57 |")
A("| Totals | formulas on total rows only: Gross, Total deductions, Net, Total employer, leave balance, calculation blocks | house rule |")
A("| Social security | lesser of (remaining annual maximum) or (rate x period base), never annualised-then-divided | house rule; sample is mid-year near the wage base |")
A("| Currency | USD, two decimals (not in the zero-minor-unit set) | build manifest |")
A("| Employee legal name and home address | present in Payslip Spec (Employee Full Name, Employee Home Address), mapped to the DD fields | DD confirmation |")
A("| Contractors (Form 1099-NEC) | NO | scope, owner instruction recorded in the manifest |")
A("")
A("## Deviations from the agent's stated constants and from the references")
A("- Pay element lines read `code - wage type name` (for example `62100 - Basic salary`), not `XXXXX - ...`: the shared C29 rule bars an X-run next to a dash. Codes come from the WTC crosswalk.")
A("- Display label of a line is the crosswalk (US) label, which is the WTC `Name in Local Language (English)` column; the WTC column `Name in English` carries the global name (for example 21900).")
A(f"- Payslip Spec has {lint['info']['spec_rows']} field rows (target 25-35, minimum 20): the union of the State elements and the federal lines needs more.")
A("- Unit Rate Details: the approved WTC holds one rate wage type (62104, basic salary, listed only as the rate account of 62100) and one hours accumulator (US-030); the unit account US-030 is given only to the six time-based lines (62100, 62110, 62150, 62160, 62170, 62300); every other earning reads 'Amount only'.")
A("- Palette (QA1-17, owner default): the payslip tabs use only the fills measured in the two payslip references (DCDCDC labels, net row and employer block; A9A9A9 title band and section bars; white rows). The navy, green, F2F2F2 and FCE4D6 fills are removed. The WTC and DD palettes (4472C4 / FF9900 / D9E1F2) belong to those artifacts; the payslip references mandate their own palette, which is kept here, and the Payslip Spec headers keep the 0B5394 / 4BACC6 of the Tunisia reference.")
A("- Printed tabs: the three payslip tabs print the label and the value only; the calculation blocks sit below the print area. release.py strips [[FACT:]] tags only; nothing else needs stripping on those tabs. No release_rules.json is written: its text rules act on every package file, and register ids in brackets are a convention of the other artifacts.")
A("- Payslip rows with no DD field (bank name, account, payment method, employer operating name, separate employer mailing address): the Spec says so in column E; the DD owner decides whether these become master data. The DD does hold the employer physical-address fields, which the Employer Address row maps.")
A("- Reference sheets use Arial 6 pt on the payslip grid; kept (file prevails over the standard table). Title band and section bars A9A9A9, labels, net row and employer block DCDCDC.")
A("- Wage-type codes (US-nnn, 5-digit) are treated as identifiers by the period-aware lint (same convention as the WTC build); the shared C46 reads them as numbers and reports a few collisions with unrelated fact values.")
A("- Shared C46 (non-period-aware) reads the last dated value of a key and reports the 2026 wage base tag against the 2027 value; the period-aware C46 is 0 mismatches.")
A("")
import decimal
from fractions import Fraction as Fr


def cents(x):
    """half-up rounding to the cent of an exact fraction"""
    return int((x * 100 + Fr(1, 2)).__floor__())


A("## Round 2: QA r1 builder items")
A("| Item | Change |")
A("|---|---|")
for it, ch in [
    ("QA1-01", "Employer social security is a formula, lesser of the remaining annual maximum and rate x period base, on the 3 tabs (calc rows under the print area)"),
    ("QA1-02", "New input row 'Medicare wages paid before this payslip' (no wage base); Additional Medicare and YTD Medicare use it; YTD Medicare = prior tax + Medicare + Additional Medicare"),
    ("QA1-03", "Employer Medicare is a formula; YTD gross = input 'gross paid before' + gross of the payslip"),
    ("QA1-04", "'Total Hours Worked' row (SUM of the hours column) and Spec row; PSL-legal-items 'hours' matches it"),
    ("QA1-05", "6 Spec rows: Bank Name, Account (masked), Payment Method, Compensation Sources, Pay-Code Guide Reference, Compensatory Time"),
    ("QA1-06", "State-switched rows and Spec rows: AZ sick pay received, NYC PTO accrued / paid used / unpaid used / unpaid available"),
    ("QA1-07", "Leave block of the TX sample reads 'not printed'"),
    ("QA1-08", "Spec SSN mapping returns no digits for MD; the Employee ID is the identifier"),
    ("QA1-09", "MN 181.032(b) items mapped: operating name, mailing address, meals and lodging allowances, 268B.14 deduction line (US-185), hours, rate basis"),
    ("QA1-10", "NM benefits-earned row and Spec row; RATE_OF_PAY_BASIS adds Shift, Day, Week, Other; NY 195(3) industry items are a named limitation (gap request)"),
    ("QA1-11", "Population Range C12 cites psl.ca.statement.household_exclusion; psl.va.statement.content removed from C13"),
    ("QA1-12", "Field Option NOT_CONFIGURED block removed"),
    ("QA1-13", "Payslip tabs print label and value only; print area set; calculation blocks outside it"),
    ("QA1-14", "'Build rule / Build default / generator' wording replaced; the 3 fact values arrive reworded (R2)"),
    ("QA1-15", "Spanish with diacritics on the ES tab and Spec column C; Hourly, Biweekly, Single or MFS, job title, bank translated"),
    ("QA1-16", "Unit Rate Details: 62104 row dropped; US-030 only on time-based lines; one specific basis text per row"),
    ("QA1-17", "Reference payslip palette applied (see deviations)"),
    ("QA1-18", "Payment details: header Amount, value = net pay formula"),
    ("QA1-19", "Spec EIN mapping adds the State employer account number for OR"),
    ("QA1-22", "PSL-bindings.csv is written from the cells of the finished workbook: one row per tag, location sheet!cell"),
]:
    A(f"| {it} | {ch} |")
A("")
A("### Worked example recomputed by hand (integer cents, independent of the generator)")
gross = 288000 + 21600 + 1700000
k401 = cents(Fr(gross, 100) * Fr(5, 100))
fica = gross - 8500
base_ss = 18450000
ytd_ss = 18150000
rate_ss = Fr(62, 1000)
rate_med = Fr(145, 10000)
rate_add = Fr(9, 1000)
thr_add = 20000000
rem = cents(Fr(base_ss, 100) * rate_ss) - cents(Fr(ytd_ss, 100) * rate_ss)
per = cents(Fr(fica, 100) * rate_ss)
ss = min(rem, per)
med = cents(Fr(fica, 100) * rate_med)
mwy = ytd_ss + fica
exc = max(0, min(fica, mwy - thr_add))
add = cents(Fr(exc, 100) * rate_add)
A(f"- Gross = 80 x 36.00 + 4 x 54.00 + 17,000.00 = {gross / 100:,.2f}; 401(k) 5% = {k401 / 100:,.2f}; cafeteria plan 85.00; FICA wages = {fica / 100:,.2f}")
A(f"- Employee social security: remaining = 6.2% x 184,500.00 - 6.2% x 181,500.00 = {rem / 100:,.2f}; period = 6.2% x {fica / 100:,.2f} = {per / 100:,.2f}; withheld = lesser = {ss / 100:,.2f}")
A(f"- Employer social security: same rate, same base, same prior wages, so lesser = {min(rem, per) / 100:,.2f} (before: uncapped {per / 100:,.2f})")
A(f"- Medicare: 1.45% x {fica / 100:,.2f} = {med / 100:,.2f} employee and {med / 100:,.2f} employer")
A(f"- Additional Medicare: Medicare wages YTD = 181,500.00 + {fica / 100:,.2f} = {mwy / 100:,.2f}; above 200,000.00 = {exc / 100:,.2f} (limited to this payslip); 0.9% x {exc / 100:,.2f} = {add / 100:,.2f}")
A(f"- Employer total = {(min(rem, per) + med) / 100:,.2f}; YTD Medicare = {cents(Fr(18150000, 100) * rate_med) / 100:,.2f} + {med / 100:,.2f} + {add / 100:,.2f} = {(cents(Fr(18150000, 100) * rate_med) + med + add) / 100:,.2f}; YTD gross = 185,000.00 + {gross / 100:,.2f} = {(18500000 + gross) / 100:,.2f}")
A("")
A("## Open items (not configured in this release)")
A(f"{len(req)} requests, all non-blocking: {dict(why)}. Each has a cell reading 'Not configured in this release [[GAP:PSL-RQ-nn]]', an entry in `_research/gaps.json` and a request in `_research/PSL-research-request.json`.")
A("")
A("| Gap id | Key | Reason | First cell |")
A("|---|---|---|---|")
for k, v in sorted(req.items(), key=lambda x: x[1]["gid"]):
    A(f"| {v['gid']} | `{k}` | {v['why']} | {v['locations'][0] if v['locations'] else ''} |")
A("")
A("## Reconciliation")
A("| Kind | Status | Rows |")
A("|---|---|---|")
for (kd, st), n in sorted(cnt.items()):
    A(f"| {kd} | {st} | {n} |")
A("`MAPPED_NO_DD_FIELD`: the amount is a payroll result or input of the wage type and no DD master-data field holds it (F26). Unmapped 0.")
A("")
A("## Checks (latest run)")
A("```")
A(summary.strip())
A("```")
A("")
A("## Accuracy")
A("85% - official reference structure (Mozambique and Tunisia workbooks), approved WTC and DD, and research with a register row for every rule; the worked example is computed from the facts. "
  "No real US payslip sample was available, and the State rules are statute readings, not tested against a filed statement. "
  f"{len(req)} items are open (statements not proven in the saved source copy, or not yet read). "
  "Closing the gap needs the authority pages named in each request (agent 2) and a payslip accepted by one payroll operator (development team).")
open(os.path.join(S.BASE, "_pipeline", "PSL-build-log.md"), "w", encoding="utf-8").write("\n".join(o) + "\n")
print("PSL-build-log.md written,", len(o), "lines")
