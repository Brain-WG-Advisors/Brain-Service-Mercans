"""Denmark - eIndkomst September 2026. Usage: python -I dk_check.py sherwin|kgs
Reads eIndkomst upload, SKAT Afstemning, G2N, payslips, GL, (master, bank files for Sherwin)."""
import glob
import os
import sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "common"))
sys.stdout.reconfigure(encoding="utf-8")

import bank  # noqa: E402
import hrb  # noqa: E402
import readers as R  # noqa: E402
from framework import Evidence, eq, num  # noqa: E402

BASE = os.path.join(HERE, "..", "..", "Denmark")
CFG = {
    "sherwin": {"folder": "Sherwin Williams Denmark - 2026-09", "se": "24502511", "name": "Sherwin-Williams Denmark A/S",
                "upload": "Denmark E-Income Report*", "g2n": "Sherwin Gross to Net*", "slips": "Sept'26 Payslips*",
                "skat": "SKAT, eIndkomst*", "gl": "Employee Detail GL*", "master": "Master Data_17*",
                "ee": "Sherwin Williams-DNK_LE-EE*", "er": "Sherwin Williams-DNK_LE-ER*",
                "health": "65801", "car": ["65803"], "phone": "65807", "severance": "6213",
                "pension_ee": ["21640", "21641", "21646"], "pension_er": "23670",
                "non_a": ["62800", "62805"], "post_tax": ["21141"], "bededag": "62229", "salary": ["62100", "62102"]},
    "kgs": {"folder": "KGS Fire & Security Denmark - 2026-09", "se": "18458195", "name": "KGS Fire & Security Danmark ApS",
            "upload": "Denmark E-Income Report*", "g2n": "KGS Gross to Net*", "slips": "payslips KGS*",
            "skat": "SKAT, eIndkomst*", "gl": "Standard GL Report*", "master": None, "ee": None, "er": None,
            "health": "62610", "car": ["65804", "65803"], "phone": "65807", "severance": None,
            "pension_ee": ["21640"], "pension_er": "23670", "non_a": [], "post_tax": ["21114"], "bededag": "62229",
            "salary": ["62100", "62228"]},
}
ATP = [(117, 99, 198), (78, 66, 132), (39, 33, 66), (0, 0, 0)]   # S15-S17, monthly A-sats 2026
AM = 0.08
SEV_FREE = 8000                                                    # LL § 7 U

key = sys.argv[1]
C = CFG[key]
PKG = os.path.join(BASE, C["folder"])
VAL = os.path.join(PKG, "02 Validation")
X = os.path.join(VAL, "_extracted")


def f(p):
    r = glob.glob(os.path.join(X, p))
    return r[0] if r else None


ev = Evidence(f"{C['name']} ({C['se']}) - eIndkomst September 2026")
up = R.read_eindkomst_upload(f(C["upload"]))
sk = R.read_skat_afstemning(f(C["skat"]))
g2n = hrb.read_g2n(f(C["g2n"]))
G = {str(e["Employee ID"]).strip(): e for e in g2n["emps"]}
U = {r["6000-6"]: r for r in up["recs"]}
ps = R.read_payslips_dk(f(C["slips"]))
P = {p.get("ansattnr"): p for p in ps}
ids = list(G)
N = len(ids)
popn = f"{N} employees"


def c(e, code):
    return hrb.code(G[e], code)


def sumc(e, codes):
    return sum(c(e, x) for x in codes)


# ================= A. scope / receipt =================
ev.check("A-01", "Scope", "Upload file: indberetter and pligt SE-nr, production flag, one main ID, period 01-30.09.2026",
         f"{len(up['recs'])} records", all(r["1000-5"] == C["se"] and r["2001-4"] == C["se"] and r["1000-14"] == "P"
                                          and r["5000-6"] == "20260901" and r["5000-7"] == "20260930" for r in up["recs"]))
ev.check("A-02", "Authority receipt", "SKAT 'Afstemning af indberetninger' is for the same SE-nr and settlement period 09.2026",
         "1 print", sk["se"] == C["se"] and sk["period"] == ("09.2026", "09.2026"), f"{sk['se']} {sk['name']} {sk['period']} printed {sk['printed']}")
tot = defaultdict(float)
for r in up["recs"]:
    for code in r:
        if code and code[0] in "BA" and code[1:].isdigit():
            tot[code[1:]] += R.amt(r, code)
diffs = []
for fld, v in sk["fields"].items():
    if not eq(tot.get(fld, 0.0), v, 0.01):
        diffs.append(f"felt {fld}: upload {tot.get(fld, 0.0):,.2f} / SKAT {v:,.2f}")
for fld, v in tot.items():
    if v and fld not in sk["fields"] and fld not in ("0200",):
        diffs.append(f"felt {fld}: upload {v:,.2f} / not in SKAT print")
ev.check("A-03", "Authority receipt", "Upload-file totals per feltnr = SKAT Afstemning totals (proof the file was received)",
         f"{len(sk['fields'])} fields", not diffs, "; ".join(diffs))
for fld, v in sk["fields"].items():
    ev.recon(f"Felt {fld}", "Upload file total", round(tot.get(fld, 0.0), 2), "SKAT Afstemning", v,
             explained="Difference (see review)")
ev.check("A-04", "Deadline", "Dispositionsdato within the period and SKAT data present by 30.09.2026 (large-employer deadline)",
         "1 report", all(r["5000-8"] <= "20260930" for r in up["recs"]) and sk["printed"] and sk["printed"][0] <= "9/30/26",
         f"dispositionsdato {sorted({r['5000-8'] for r in up['recs']})}; SKAT print {sk['printed']}")

# ================= B. format =================
bad = []
for r in up["recs"]:
    cpr = r["6000-4"] or ""
    if not (len(cpr) == 10 and cpr.isdigit()):
        bad.append(f"{r['6000-6']} CPR '{cpr}'")
ev.check("B-01", "Format", "CPR-nummer is 10 digits without separator", f"{len(up['recs'])} records", not bad, "; ".join(bad))
ev.check("B-02", "Format", "Indberetnings-ID unique per record; For-/bagudløn and indkomsttype set",
         f"{len(up['recs'])} records", len({r['5000-4'] for r in up['recs']}) == len(up["recs"])
         and all(r["5000-10"] in ("B", "F") for r in up["recs"]),
         f"indkomsttype (5000-12) blank on {sum(1 for r in up['recs'] if not r.get('5000-12'))} records (default 00)")
bad = []
for r in up["recs"]:
    hrs = R.amt(r, "A0200")
    atp = R.amt(r, "B0046")
    exp = next(e + er for lo, e, er in ATP if hrs >= lo)
    if not eq(atp, exp):
        bad.append(f"{r['6000-6']} hours {hrs} ATP {atp} expected {exp}")
ev.check("B-03", "Format", "ATP (felt 0046) = 2026 A-sats for the hours reported (felt 0200)", f"{len(up['recs'])} records",
         not bad, "; ".join(bad))

# ================= C. content upload vs G2N =================
bad, rec_rows = [], []
for e in ids:
    u = U.get(e)
    if not u:
        bad.append(f"{e} missing in upload")
        continue
    gross = num(G[e]["Gross Salary"])
    sev = c(e, C["severance"]) if C["severance"] else 0.0
    pens_ee = sumc(e, C["pension_ee"])
    atp_ee = c(e, "2517")
    nona = sumc(e, C["non_a"])
    exp13 = gross - sev - pens_ee - atp_ee - nona + (max(sev - SEV_FREE, 0) if sev else 0)
    if not (int(exp13) == R.amt(u, "B0013") or eq(exp13, R.amt(u, "B0013"), 1)):
        bad.append(f"{e} 0013 {R.amt(u, 'B0013'):,.2f} vs G2N-derived {exp13:,.2f}")
    for fld, val in (("B0015", c(e, "2552")), ("B0016", c(e, "2513")), ("B0147", pens_ee), ("B0148", c(e, C["pension_er"])),
                     ("B0026", c(e, C["health"])), ("B0019", sumc(e, C["car"])), ("B0020", c(e, C["phone"]))):
        if not eq(R.amt(u, fld), val, 0.01):
            bad.append(f"{e} {fld[1:]} upload {R.amt(u, fld):,.2f} vs G2N {val:,.2f}")
ev.check("C-01", "Content", "Per employee: 0013 = gross - own pension - own ATP - tax-free items (whole kr), and 0015/0016/0019/"
         "0020/0026/0147/0148 = G2N", popn, not bad, "; ".join(bad))
ev.check("C-02", "Content", "Same population in upload, G2N and payslips", popn,
         set(U) == set(ids) == set(P), f"upload {len(U)}, G2N {N}, payslips {len(P)}")

# ================= D. statutory recalculation =================
rows, bad_am, bad_tax, bad_health, bad_sev, bad_bb, bad_ft = [], [], [], [], [], [], []
for e in ids:
    u, p, g = U[e], P[e], G[e]
    a13 = R.amt(u, "B0013")
    am_exp = round(a13 * AM)                    # nearest krone (engine); DJV example rounds up
    if not eq(am_exp, c(e, "2513"), 1):
        bad_am.append(f"{e} AM {c(e, '2513')} vs 8% x {a13:,.0f} = {a13 * AM:,.2f}")
    base = a13 - c(e, "2513")
    pct = next((l["sats"] for l in p["lines"] if l["code"] == "2552"), None)
    fr = p.get("fradrag_used")
    tax_exp = round((base - (fr or 0)) * pct / 100) if pct is not None else None
    ok_base = eq(p.get("askat_base"), base) and eq(p.get("skat_af"), base - (fr or 0))
    if tax_exp is None or not eq(tax_exp, c(e, "2552"), 1) or not ok_base:
        bad_tax.append(f"{e} base {p.get('askat_base')} vs {base}; skat af {p.get('skat_af')}; {pct}% -> {tax_exp} vs {c(e, '2552')}")
    h = c(e, C["health"])
    if h and not eq(R.amt(u, "B0026"), h, 0.01):
        bad_health.append(f"{e} health insurance {h:,.2f} not in 0026 and excluded from 0013 (AM {h * AM:,.2f}, A-skat ~{h * 0.92 * (pct or 0) / 100:,.2f} not withheld)")
    sev = c(e, C["severance"]) if C["severance"] else 0
    if sev:
        bad_sev.append(f"{e}: severance gross {sev:,.2f}; 0013 holds {a13:,.0f} (taxable part {sev - SEV_FREE:,.2f}); "
                       f"0069 reported {sk['fields'].get('0069', 0):,.2f}; upload file has no 0069 column")
    # store bededag 0.45%: engine base vs statutory base (fixed pay + employer pension; benefits kept excluded - INFERENCE)
    bb = c(e, C["bededag"])
    if bb:
        sal = sumc(e, C["salary"])
        ben = c(e, C["health"]) + sumc(e, C["car"]) + c(e, C["phone"])
        eng = round((sal + ben) * 0.0045, 2)
        stat = round((sal + c(e, C["pension_er"])) * 0.0045, 2)
        if not eq(bb, stat, 0.05):
            bad_bb.append(f"{e} paid {bb:,.2f}; (salary+pension) x 0.45% = {stat:,.2f}; engine base incl. benefits = {eng:,.2f}")
    fe = p["ferie"].get("ferieberettiget_periode")
    if fe:
        ben = c(e, C["health"]) + sumc(e, C["car"]) + c(e, C["phone"])
        if ben and eq(fe, num(g["Gross Salary"]) - sumc(e, C["non_a"]), 0.05):
            bad_ft.append(f"{e} ferieberettiget {fe:,.2f} includes benefits {ben:,.2f}")
    rows.append({"Employee": e, "A-indkomst 0013": a13, "AM 8% (nearest kr)": am_exp, "AM withheld": c(e, "2513"),
                 "A-skat base (0013-AM)": base, "Fradrag used (payslip)": fr, "Trækprocent (payslip)": pct,
                 "A-skat expected": tax_exp, "A-skat withheld": c(e, "2552"), "Hours 0200": R.amt(u, "A0200"),
                 "ATP 0046": R.amt(u, "B0046"), "Health ins. (G2N)": h or None, "0026 reported": R.amt(u, "B0026") or None,
                 "Store bededag paid": bb or None})
ev.d["recalc"] = rows
ev.check("D-01", "AM-bidrag", "AM-bidrag = 8% of felt 0013 (rounded to whole kr)", popn, not bad_am, "; ".join(bad_am))
ev.check("D-02", "A-skat", "A-skat = (0013 - AM - monthly fradrag) x trækprocent, with fradrag and % as printed on the payslip "
         "(skattekort not in the pack)", popn, not bad_tax, "; ".join(bad_tax))
ev.check("D-03", "A-skat", "Employer-paid health insurance taxed: in felt 0026 and in 0013 (LL § 16(3); eIndkomst guide §8.4.1)",
         f"{sum(1 for e in ids if c(e, C['health']))} employees", not bad_health, "; ".join(bad_health))
ev.check("D-04", "Severance", "Fratrædelsesgodtgørelse: 0069 = gross, not in 0013; A-skat/AM only above 8,000 (LL § 7 U; "
         "guide §8.4.3)", f"{sum(1 for e in ids if C['severance'] and c(e, C['severance']))} employees", not bad_sev,
         "; ".join(bad_sev))
ev.check("D-05", "Store bededag", "0.45% supplement on fixed pay incl. employer pension, excl. benefits kept during holiday "
         "(LOV 214/2023 § 3; bill remarks)", f"{sum(1 for e in ids if c(e, C['bededag']))} employees", not bad_bb,
         "; ".join(bad_bb[:6]) + (f" ... ({len(bad_bb)} total)" if len(bad_bb) > 6 else ""))
ev.check("D-06", "Ferietillæg", "Ferieberettiget løn (ferietillæg 1% base) excludes benefits kept during holiday (FL § 19)",
         popn, not bad_ft, "; ".join(bad_ft[:6]) + (f" ... ({len(bad_ft)} total)" if len(bad_ft) > 6 else ""))
bad = [f"{e} {P[e]['ferie'].get('ferietillaeg_periode')} vs 1% x {P[e]['ferie'].get('ferieberettiget_periode')}"
       for e in ids if P[e]["ferie"].get("ferieberettiget_periode") and not eq(
           P[e]["ferie"]["ferietillaeg_periode"], round(P[e]["ferie"]["ferieberettiget_periode"] * 0.01, 2), 0.01)]
ev.check("D-07", "Ferietillæg", "Ferietillæg accrued = 1% of ferieberettiget løn (FL § 16(1))", popn, not bad, "; ".join(bad))

# ================= E. payslips =================
bad = []
for e in ids:
    p, g = P[e], G[e]
    if not eq(p.get("netto"), num(g["Net Pay"]), 0.01) or not eq(p.get("indtjening"), num(g["Gross Salary"]), 0.01):
        bad.append(f"{e} net/gross {p.get('netto')}/{p.get('indtjening')}")
    if (p.get("cpr") or "").replace("-", "") != (U[e]["6000-4"] or "").replace("-", "") or p.get("se") != C["se"]:
        bad.append(f"{e} cpr/se")
    for l in p["lines"]:
        if l["code"] in ("2552", "2513", "2517") + tuple(C["pension_ee"]):
            if not eq(abs(l["amount"] or 0), c(e, l["code"]), 0.01):
                bad.append(f"{e} {l['code']} {l['amount']} vs {c(e, l['code'])}")
ev.check("E-01", "Payslip", "Payslip gross, net, CPR, SE-nr, A-skat, AM, ATP and pension = G2N/report", popn, not bad, "; ".join(bad))
dates = sorted({p.get("betalingsdato") for p in ps})
ev.check("E-02", "Payslip", "Payment date on payslip = dispositionsdato", popn,
         all(d and d[6:] + d[3:5] + d[:2] == up["recs"][0]["5000-8"] for d in dates), f"payslip {dates}; dispositionsdato {up['recs'][0]['5000-8']}")

# ================= F. bank =================
if C["ee"]:
    ee = bank.read_pain001(f(C["ee"]))
    er = bank.read_pain001(f(C["er"]))
    ms = R.__dict__.get("x")
    import importlib.util
    spec = importlib.util.spec_from_file_location("noread", os.path.join(HERE, "..", "no", "readers.py"))
    NOR = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(NOR)
    md = NOR.read_master_columns(f(C["master"]))
    ev.check("F-01", "Bank", "EE file: NbOfTxs/CtrlSum consistent; one transfer per employee = G2N net", popn,
             ee["NbOfTxs"] == len(ee["tx"]) == N and eq(ee["CtrlSum"], sum(t["amt"] for t in ee["tx"]))
             and eq(ee["CtrlSum"], num(g2n["totals"]["Net Pay"]), 0.01), f"{ee['NbOfTxs']} / {ee['CtrlSum']}")
    bad = []
    for e in ids:
        tx = [t for t in ee["tx"] if eq(t["amt"], num(G[e]["Net Pay"]), 0.005)]
        m = md.get(e)
        if not tx:
            bad.append(f"{e} no transfer")
        elif m and m.get("IBAN") and tx[0]["acct"] != m.get("IBAN"):
            bad.append(f"{e} IBAN {tx[0]['acct']} vs master {m.get('IBAN')}")
        if not m:
            bad.append(f"{e} not in master data")
        if P[e].get("konto") and tx and P[e]["konto"].split("-")[-1] != tx[0]["acct"]:
            bad.append(f"{e} payslip account {P[e]['konto']} vs bank {tx[0]['acct']}")
    ev.check("F-02", "Bank", "Beneficiary account = payslip account = master-data IBAN", popn, not bad, "; ".join(bad))
    skat_tx = sum(t["amt"] for t in er["tx"] if "Skatteforvaltningen" in (t["name"] or ""))
    atp_tx = sum(t["amt"] for t in er["tx"] if "ATP" in (t["name"] or ""))
    pen_tx = sum(t["amt"] for t in er["tx"] if "Danica" in (t["name"] or ""))
    other = [t for t in er["tx"] if not any(k in (t["name"] or "") for k in ("Skatteforvaltningen", "ATP", "Danica"))]
    ev.recon("A-skat + AM paid", "ER file to Skatteforvaltningen", skat_tx, "SKAT 0015 + 0016",
             sk["fields"]["0015"] + sk["fields"]["0016"])
    ev.recon("ATP paid", "ER file to ATP", atp_tx, "SKAT 0046", sk["fields"]["0046"])
    ev.recon("Pension paid", "ER file to Danica + other pension transfers", pen_tx + sum(t["amt"] for t in other),
             "SKAT 0147 + 0148", sk["fields"]["0147"] + sk["fields"]["0148"])
    ev.check("F-03", "Bank", "Tax/AM payment execution date not later than the deadline (30.09.2026)", "1 file",
             all(pi["ReqdExctnDt"] <= "2026-09-30" for pi in er["pmtinf"]), str([pi["ReqdExctnDt"] for pi in er["pmtinf"]]))
    ev.recon("Net pay", "G2N Net Pay", num(g2n["totals"]["Net Pay"]), "EE bank file CtrlSum", ee["CtrlSum"])
    ev.check("F-04", "Master data", "Master data covers the run (terminated employees excepted)", popn,
             all(e in md or G[e].get("Termination date") for e in ids), f"master {len(md)}, G2N {N}")
else:
    ev.check("F-01", "Bank", "Bank files", "-", True, "Money movement outside Mercans for this client (decision 14-10-2026)",
             result="Out of scope")

# ================= G. GL =================
if key == "sherwin":
    gl = R.read_gl_employee_detail(f(C["gl"]))
    dcol, ccol, acol = "Debit Amount", "Credit Amount", "Account"
else:
    glr = hrb.read_gl_report(f(C["gl"]))
    gl, dcol, ccol, acol = glr["lines"], "Debit Amount", "Credit Amount", "GL Code"
deb = sum(num(l[dcol]) or 0 for l in gl)
cre = sum(num(l[ccol]) or 0 for l in gl)
ev.check("G-01", "GL", "GL debit = credit", f"{len(gl)} lines", eq(deb, cre, 0.01), f"{deb:,.2f} / {cre:,.2f}")
by_pe = defaultdict(float)
for l in gl:
    pe = str(l.get("Pay Element") or l.get("CategoryType/ Pay Element") or "")
    by_pe[pe] += (num(l[ccol]) or 0) - (num(l[dcol]) or 0)
tax_gl = sum(v for k, v in by_pe.items() if "A-Tax" in k)
am_gl = sum(v for k, v in by_pe.items() if "AM-Contribution" in k or "Am contribution" in k)
net_gl = sum(v for k, v in by_pe.items() if k.strip() in ("NET Pay", "2610 - Net Pay"))
ev.recon("A-skat", "GL credit A-Tax", round(tax_gl, 2), "SKAT 0015", sk["fields"]["0015"])
ev.recon("AM-bidrag", "GL credit AM", round(am_gl, 2), "SKAT 0016", sk["fields"]["0016"])
ev.recon("Net pay", "GL credit net pay", round(net_gl, 2), "G2N Net Pay", num(g2n["totals"]["Net Pay"]))
if key == "kgs":
    lab = defaultdict(set)
    for l in gl:
        lab[(str(l["GL Code"]), str(l["GL Description"]))].add(str(l["Pay Element"]).split(" - ", 1)[-1])
    odd = [f"{a} '{d}' carries {sorted(v)[:4]}" for (a, d), v in lab.items()
           if (d in ("Pension skyldig", "ATP skyldig", "Vaerdi af fri bil") and len(v) > 1)]
    ev.check("G-02", "GL", "GL account descriptions consistent with the pay elements posted", f"{len(lab)} accounts", not odd,
             "; ".join(odd))
    missing_id = [e for e in ids if not G[e].get("National ID")]
    short = [e for e in ids if G[e].get("National ID") and len(str(G[e]["National ID"])) != 10]
    ev.check("G-03", "G2N", "G2N National ID present and 10 digits", popn, not missing_id and not short,
             f"blank: {missing_id}; wrong length: {short}")

ev.nt("NT-01", "Skattekort (trækprocent and monthly fradrag)", "Not in the pack; D-02 uses the % and fradrag printed on the "
      "payslip (decision 14-10-2026).", "eSkattekort extract per employee for September 2026.")
ev.nt("NT-02", "Pension scheme rates (employee/employer %)", "Contractual, not statutory.", "Pension agreement, if wanted.")
ev.save(VAL)
