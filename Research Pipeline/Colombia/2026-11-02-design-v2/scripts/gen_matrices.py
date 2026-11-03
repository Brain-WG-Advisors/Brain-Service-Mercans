# Mechanically derives CO_Taxability_Perimeters_Extract_<PKG>.csv and CO_Taxability_Matrices_<PKG>.md from the WTC
# (version read from the file name, e.g. CO-WTC-001-v1.8.xlsx). 2026-11-02: package v1_1 (WTC v1.8); the WTC version is no
# longer hard-coded; the withholding paragraph no longer lists severance savings (N = No since WTC v1.8).
import sys, os, re, csv, collections, openpyxl, hashlib
WTC = sys.argv[1]; OUTD = sys.argv[2]
PKG = 'v2_0'  # 2026-11-02: design v2.0 (WTC v1.9)
WV = 'v' + re.search(r'v(\d+\.\d+)', os.path.basename(WTC)).group(1)
ws = openpyxl.load_workbook(WTC, read_only=True)["Wage Type Catalogue"]
rows = [(i, r) for i, r in enumerate(ws.iter_rows(min_row=1, values_only=True), start=1) if i > 1 and r[1]]
COLS = "NOPQRSTUVWX"
def v(r, c):
    x = r[13 + COLS.index(c)]
    return "" if x is None else str(x).strip()
PER = [("N", "N_SubjectToWithholding"), ("O", "O_Table383"), ("P", "P_NonResident408"), ("Q", "Q_Health"), ("R", "R_SolidarityFund"),
       ("S", "S_OccupationalRisk"), ("T", "T_PayrollLevies"), ("U", "U_Pension"), ("W", "W_BenefitsBase"), ("X", "X_VacationBase")]
with open(os.path.join(OUTD, "CO_Taxability_Perimeters_Extract_%s.csv" % PKG), "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(["WTC_Row", "Name", "Category", "Tax_Code", "Salary_Class"] + [p[1] for p in PER])
    for i, r in rows:
        w.writerow([i, r[1], r[4], r[6], v(r, "V")] + [v(r, c) for c, _ in PER])

md5 = hashlib.md5(open(WTC, "rb").read()).hexdigest()
na_all = [(i, r) for i, r in rows if all(v(r, c) == "NA" for c, _ in PER)]
active = [(i, r) for i, r in rows if not all(v(r, c) == "NA" for c, _ in PER)]
L = []
A = L.append
A("# CO — Taxability Matrices (companion to `CO_Regulation_Design_%s.md`)" % PKG)
A("")
A(("Mechanically derived from **CO-WTC-001 " + WV + "**, sheet *Wage Type Catalogue*, columns N–X (%d wage-type rows; raw extraction: `CO_Taxability_Perimeters_Extract_" + PKG + ".csv`). Nothing here is hand-transcribed. "
  "Convention, as for the dev team's matrices: **specific overrides first** (`No` and `Yes-No` rows), then the default; rows that are `NA` in a perimeter are not in that matrix.") % len(rows))
A("")
A("**Row identifiers.** WTC " + WV + " carries no Mercans codes in column A (codes are assigned at configuration). Every row is therefore identified here by its **WTC row number** (`R123`) and English name; the CSV carries the same key. When codes are assigned, the matrices are re-keyed one to one; no wildcard (`621%%`-style) condensation is possible until then.")
A("")
A("**Perimeters (WTC column → matrix → consuming regulation):**")
A("")
A("| WTC column | Matrix | Feeds | Consumed by |")
A("|---|---|---|---|")
feeds = {"N": ("A — Subject to withholding", "`58150` taxable labour payments (monthly read)", "`9170072` (R320, R339, R340, R343, R344, R345 false), `9170073` (service bonus, Procedure 2)"),
         "O": ("B — Art. 383 table", "routing: `Yes` = read on the table (monthly, service bonus or termination percentage)", "`9170085`, `9170088`–`9170093`"),
         "P": ("C — Non-resident flat 20%", "`58163`", "`9170132`"),
         "Q": ("D — Health", "`58106` IBC (health)", "`9170045`, `9170056`"),
         "R": ("E — Solidarity pension fund", "`58113` IBC (FSP)", "`9170050`, `9170058`, `9170059`"),
         "S": ("F — Occupational risk", "`58114` IBC (ARL)", "`9170051`, `9170060`"),
         "T": ("G — Payroll levies (CCF / SENA / ICBF)", "`58108` levy base", "`9170047`, `9170061`–`9170063`"),
         "U": ("H — Pension", "`58112` IBC (pension)", "`9170049`, `9170057`"),
         "W": ("I — Statutory-benefit base (prima / cesantías / interest)", "`58171`", "`9170020`–`9170023`"),
         "X": ("J — Vacation base", "`58175`", "`9170014`–`9170019`")}
for c, _ in PER:
    A("| %s | %s | %s | %s |" % (c, feeds[c][0], feeds[c][1], feeds[c][2]))
A("| V | K — Salary class (CST arts. 127 / 128) | `58101` (Salary), `58102` (Non-Salary – pacted) | `9170041`, `9170042` |")
A("")
A("---")
A("")
A("## 🔴 Structural finding — the engine matrix cannot express `Yes-No`")
A("")
cnt = {c: sum(1 for i, r in rows if v(r, c) == "Yes/No") for c, _ in PER}
A("The WTC marks rows **`Yes/No`** (subject only in part or only under a condition). A taxability matrix holds `Yes` or `No` per row; there is no third state. Count per perimeter: " +
  ", ".join("%s %d" % (c, cnt[c]) for c, _ in PER) + ".")
A("")
yn_soc = [(i, r) for i, r in rows if any(v(r, c) == "Yes/No" for c in "QRSU")]
pact = [(i, r) for i, r in yn_soc if v(r, "V") == "Non-Salary - pacted"]
other = [(i, r) for i, r in yn_soc if v(r, "V") != "Non-Salary - pacted"]
A("**Social-security perimeters (Q, R, S, U): two families, two different treatments.**")
A("")
A("1. **Pacted non-salary (%d rows, column V = `Non-Salary - pacted`).** The payment is outside the contribution base only up to 40%% of total remuneration (Law 1393 of 2010 art. 30; Consejo de Estado SU exp. 25185 of 9 December 2021, rule 3). "
  "Built: these rows are **`No`** in matrices D, E, F and H and **`Yes`** in matrix K-pacted (`58102`); regulation `9170044` computes the excess over 40%% (`58104`), which is added to every IBC (health, pension, FSP, occupational risk) and **never** to the levy base (Law 21 of 1982 art. 17; Decree-Law 1295 of 1994 art. 17 for occupational risk)." % len(pact))
A("2. **Conditional rows (%d rows, other classes: %s).** The condition is a statutory test on the payment itself, stated in the WTC explanation (e.g. the per diem allowance, the apprentice support by phase, the payroll advance). "
  "These must be **split into two wage types at configuration** — the exempt portion (`No`) and the subject portion (`Yes`) — with the split decided upstream of the regulation. They are set to `No` in the matrices below and listed as split." % (len(other), ", ".join("R%d %s" % (i, r[1]) for i, r in other)))
A("")
A("**Withholding perimeter (N): %d rows `Yes/No`.** Pensions, gratuities and end-of-service payments, third-party meals (≤ 41 UVT when salary ≤ 310 UVT, art. 387-1), employer voluntary pension contributions (Tax Code art. 55: up to 25%% of income and 2,500 UVT a year), occasional per diem (Decree 1625 of 2016 art. 1.2.4.7) and the payroll advance. "
  "Same split rule: `No` in matrix A and listed split; the subject portion is configured as its own wage type. "
  "Severance savings and their interest are `No` (no withholding at source for any employee, resident or non-resident: Law 100 of 1993 art. 135 par. 3; Decree 1625 of 2016 art. 1.2.4.1.11)." % cnt["N"])
A("")
A("---")
A("")
A("## Rows excluded from all ten matrices (`NA` in every perimeter)")
A("")
A("%d rows are `NA` in every column N–X: deductions and recoveries, employer-contribution and accrual lines, bases, flags, percentages and the withholding lines themselves. They are produced by regulations, not summed by matrices:" % len(na_all))
A("")
A("```")
ids = ["R%d" % i for i, r in na_all]
for k in range(0, len(ids), 12):
    A(", ".join(ids[k:k + 12]))
A("```")
A("")
names = {"N": "A", "O": "B", "P": "C", "Q": "D", "R": "E", "S": "F", "T": "G", "U": "H", "W": "I", "X": "J"}
for c, colname in PER:
    vals = collections.Counter(v(r, c) for i, r in rows)
    A("## Matrix %s — %s (WTC column %s)" % (names[c], feeds[c][0].split(" — ", 1)[1], c))
    A("")
    A("**Consumed by:** %s · **Feeds:** %s" % (feeds[c][2], feeds[c][1]))
    A("")
    A("Counts: `Yes` %d · `No` %d · `Yes/No` %d (→ `No`: pacted rows via the Law 1393 excess, others split) · `NA` %d (not in the matrix)." % (vals.get("Yes", 0), vals.get("No", 0), vals.get("Yes/No", 0), vals.get("NA", 0)))
    A("")
    exc = [(i, r) for i, r in rows if v(r, c) in ("No", "Yes/No")]
    A("**Section 1 — overrides (%d rows):**" % len(exc))
    A("")
    A("| WTC row | Value | Wage type | Salary class |")
    A("|---|---|---|---|")
    for i, r in exc:
        val = v(r, c)
        if val == "Yes/No":
            lab = "No (via Law 1393 excess `58104`)" if (c in "QRSU" and v(r, "V") == "Non-Salary - pacted") else "No split"
        else:
            lab = "No"
        A("| R%d | %s | %s | %s |" % (i, lab, r[1].replace("|", "/"), v(r, "V")))
    A("")
    yes = [i for i, r in rows if v(r, c) == "Yes"]
    A("**Section 2 — default `Yes` (%d rows):** every row not `NA` and not listed in Section 1. Row list (for configuration check):" % len(yes))
    A("")
    A("```")
    ids = ["R%d" % i for i in yes]
    for k in range(0, len(ids), 15):
        A(", ".join(ids[k:k + 15]))
    A("```")
    A("")
# Salary class matrix K
A("## Matrix K — Salary class (WTC column V; CST arts. 127 / 128)")
A("")
vc = collections.Counter(v(r, "V") for i, r in rows)
A("Counts: " + " · ".join("`%s` %d" % (k, n) for k, n in vc.most_common()) + ".")
A("")
A("- **`Salary`** → `58101` salary payments of the month (the art. 114-1 test and the IBC start here).")
A("- **`Non-Salary - pacted`** → `58102`, the numerator of the Law 1393 40% test.")
A("- **`Non-Salary - non-remunerative`** → outside the IBC, the 40% numerator and the total (CE SU 25185/2021, rule 1).")
A("- **`Paid Rest`** (vacation paid in cash) → outside the IBC (CE S4 exp. 26941 of 2024) but inside the levy base (Law 21 of 1982 art. 17).")
A("- **`Conditional`** → configuration decides per client (split).")
A("")
A("| WTC row | Class | Wage type |")
A("|---|---|---|")
for i, r in rows:
    if v(r, "V") in ("Paid Rest", "Conditional"):
        A("| R%d | %s | %s |" % (i, v(r, "V"), r[1]))
A("")
A("---")
A("")
A("## Consolidated register (all %d active rows, all perimeters)" % len(active))
A("")
A("| WTC row | Wage type | Cat. | V class | N | O | P | Q | R | S | T | U | W | X |")
A("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
ab = {"Yes": "Y", "No": "N", "Yes/No": "Y/N", "NA": "NA", "": ""}
cl = {"Salary": "S", "Non-Salary - pacted": "NS-p", "Non-Salary - non-remunerative": "NS-n", "Paid Rest": "PR", "Conditional": "C", "NA": "NA"}
for i, r in active:
    A("| R%d | %s | %s | %s | %s |" % (i, r[1].replace("|", "/"), (r[4] or "")[:4], cl.get(v(r, "V"), v(r, "V")), " | ".join(ab.get(v(r, c), v(r, c)) for c, _ in PER)))
A("")
A("Legend: Y = Yes, N = No, Y/N = Yes/No (→ `No` split in the matrix), NA = not applicable. V class: S Salary, NS-p Non-Salary pacted, NS-n Non-Salary non-remunerative, PR Paid Rest, C Conditional.")
A("")
A("**Source file:** CO-WTC-001 " + WV + ", md5 `%s`." % md5)
open(os.path.join(OUTD, "CO_Taxability_Matrices_%s.md" % PKG), "w", encoding="utf-8").write("\n".join(L) + "\n")
print("rows", len(rows), "active", len(active), "na_all", len(na_all), "yn", cnt, "pact", len(pact), "other", len(other))
