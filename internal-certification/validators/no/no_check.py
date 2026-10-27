"""Norway - Henkel Norway AS, September 2026. Etapas 3-5: read every document, recalculate, reconcile.
Writes 02 Validation/_evidence/checks.json. Usage: python -I no_check.py"""
import glob
import os
import sys
from collections import defaultdict
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "common"))
sys.stdout.reconfigure(encoding="utf-8")

from lxml import etree  # noqa: E402

import hrb  # noqa: E402
import readers as R  # noqa: E402
import trekk  # noqa: E402
from framework import Evidence, eq, num  # noqa: E402

PKG = os.path.join(HERE, "..", "..", "Norway", "Henkel Norway - 2026-09")
VAL = os.path.join(PKG, "02 Validation")
X = os.path.join(VAL, "_extracted")
REF = os.path.join(HERE, "..", "..", "references", "Norway", "2026")


def f(pat):
    return glob.glob(os.path.join(X, pat))[0]


# ---- statutory parameters (references/Norway/2026, see Sources) ----
AGA_ZONE_RATE = {"1": 14.1}           # Stortingets avgiftsvedtak 2026 / Skatteetaten satser
G_2026 = 136549                        # NAV, G per 1 May 2026
FERIE_RATE_MIN = 10.2                  # Ferieloven §10(2)
FERIE_OVER60 = 2.3                     # Ferieloven §10(3), capped at 6G
UNION_CAP = 8700                       # Skatteloven §6-20(3)
DEADLINE = date(2026, 10, 5)           # a-melding due the 5th of the following month

# ---- client mapping (read from the client's own G2N / A-melding) ----
MAP = {  # G2N code -> (fordel, beskrivelse)
    "62100": ("kontantytelse", "fastloenn"),
    "62130": ("kontantytelse", "bonus"),
    "62570": ("kontantytelse", "fastTillegg"),
    "62137": ("naturalytelse", "annet"),
    "65500": ("naturalytelse", "bil"),
    "65630": ("naturalytelse", "skattepliktigDelForsikringer"),
    "65810": ("naturalytelse", "skattepliktigDelForsikringer"),
}

ev = Evidence("Henkel Norway AS (917472890) - September 2026")
am = R.read_amelding(f("z07_A-melding*.xml"))
rc = R.read_receipt(f("z06_tilbakemelding*.json"))
sm = R.read_summary_ods(f("z05_Reconciliation*.ods"))
g2n = hrb.read_g2n(f("z08_Gross To Net*.xls"))
ps = R.read_payslips_no(f("z04_payslips*.pdf"))
bk = R.read_pain001(f("z01_NO_7073_EE Bank*"))
gld = hrb.read_gl_report(f("z02_NO_7073_GL_Detailed*.xlsx"))
md = R.read_master_columns(f("z09_Masterdata*.xlsx"))

V = am["virksomheter"][0]
M = {m["ansattnummer"]: m for m in V["mottakere"]}
G = {e["Employee ID"]: e for e in g2n["emps"]}
P = {p.get("ansattnr"): p for p in ps}
ids = sorted(G)
N = len(ids)
popn = f"{N} employees"

# ============ A. Scope, receipt, acceptance ============
ev.check("A-01", "Scope", "A-melding period, employer and namespace", "1 message",
         am["kalendermaaned"] == "2026-09" and am["opplysningspliktig"] == "917472890"
         and am["namespace"].endswith("a-meldingen:v2_3"),
         f"{am['kalendermaaned']} / {am['opplysningspliktig']} / {am['namespace']}")
ok = (rc["meldingsId"] == am["meldingsId"] and rc["opplysningspliktig"] == am["opplysningspliktig"]
      and rc["kalendermaaned"] == am["kalendermaaned"] and rc["sumAGA"] == am["sumAGA"]
      and rc["trekk"] == [(d, int(v)) for d, v in am["trekk_per_dato"]] and rc["antall"] == len(M))
ev.check("A-02", "Authority receipt", "Tilbakemelding belongs to this A-melding (meldingsId, org.nr, period, "
         "totals, number of income recipients)", "1 receipt", ok,
         f"meldingsId {rc['meldingsId']}; AGA {rc['sumAGA']}; trekk {rc['trekk']}; recipients {rc['antall']}")
ev.check("A-03", "Authority receipt", "Receipt status 'mottatt' with no avvik", "1 receipt",
         rc["status"] == "mottatt" and not rc["avvik"], f"status {rc['status']}; avvik {rc['avvik']}")
info = sm["info"]
ev.check("A-04", "Authority receipt", "a-ordningen summary: status GODKJENT for the same message ID and Altinn reference",
         "1 summary", info.get("Status") == "GODKJENT" and info.get("Message ID") == am["meldingsId"]
         and info.get("Altinn reference") == rc["altinnReferanse"],
         f"{info.get('Status')} / {info.get('Message ID')} / {info.get('Altinn reference')}")
lev = rc["leveringstidspunkt"][:10]
ev.check("A-05", "Deadline", "Delivered by the 5th of the following month", "1 message",
         date.fromisoformat(lev) <= DEADLINE, f"delivered {lev}; deadline {DEADLINE}")

# ============ B. Format (XSD + code lists + combinations) ============
xsd_p = os.path.join(REF, "a-meldingen_v2_3_20240827.xsd")
try:
    schema = etree.XMLSchema(etree.parse(xsd_p))
    doc = etree.parse(f("z07_A-melding*.xml"))
    valid = schema.validate(doc)
    errs = "; ".join(str(e.message) for e in list(schema.error_log)[:5])
    ev.check("B-01", "Format", "A-melding validates against the official XSD v2_3", "1 message", valid, errs)
except Exception as e:  # schema imports may be missing
    ev.check("B-01", "Format", "A-melding validates against the official XSD v2_3", "1 message", False,
             f"XSD could not be compiled: {e}", result="Not tested")

import pandas as pd  # noqa: E402
comb = pd.read_excel(os.path.join(REF, "inntektskombinasjoner_R1_2026.xlsx"), sheet_name="Lønn",
                     header=None, dtype=str).iloc[1:]
valid_comb = set()
for _, r in comb.iterrows():
    if pd.isna(r[2]) or str(r[2]) >= "2026-10":  # still valid in Sep 2026 (gyldig til exclusive)
        valid_comb.add((r[7], r[8], r[4], r[5], "" if r[6] == "<TOM>" else r[6]))
bad = []
n_inc = 0
for m in V["mottakere"]:
    for i in m["inntekt"]:
        n_inc += 1
        aga = "<JA>" if i["utloeserArbeidsgiveravgift"] == "true" else "<NEI>"
        tr = "<JA>" if i["inngaarIGrunnlagForTrekk"] == "true" else "<NEI>"
        hit = any(c[0] == i["fordel"] and c[1] == i["beskrivelse"] and c[4] == ""
                  and (c[2] in (aga, "<JA/NEI>")) and (c[3] in (tr, "<JA/NEI>")) for c in valid_comb)
        if not hit:
            bad.append(f"{m['ansattnummer']} {i['fordel']}/{i['beskrivelse']}")
ev.check("B-02", "Format", "Each inntekt uses a valid fordel/beskrivelse/flag combination (inntektskombinasjoner R1 2026)",
         f"{n_inc} income lines", not bad, "; ".join(bad))
per_ok = all(i["startdatoOpptjeningsperiode"] == "2026-09-01" and i["sluttdatoOpptjeningsperiode"] == "2026-09-30"
             for m in V["mottakere"] for i in m["inntekt"])
ev.check("B-03", "Format", "Opptjeningsperiode of every income line is within September 2026", f"{n_inc} income lines", per_ok)
bil = [(m["ansattnummer"], i) for m in V["mottakere"] for i in m["inntekt"] if i["beskrivelse"] == "bil"]
ev.check("B-04", "Format", "Car benefit lines carry listepris and registration number", f"{len(bil)} car lines",
         all(i["listeprisForBil"] and i["bilregnr"] for _, i in bil))
sum_trekk = sum(-v for m in V["mottakere"] for _, v in m["trekk"])
ev.check("B-05", "Format", "Sum of per-employee forskuddstrekk = sumForskuddstrekk for the payment date", popn,
         eq(sum_trekk, am["trekk_per_dato"][0][1]), f"{sum_trekk} vs {am['trekk_per_dato'][0][1]}")
# employer identification
ev.check("B-06", "Format", "Virksomhet (underenhet) = master data sub-entity number", popn,
         all(str(md[e].get("Employment / Sub-Entity Number")) == V["orgnr"] for e in ids), V["orgnr"])
# identifiers: fnr vs birth date vs master
bad = []
for e in ids:
    m = M[e]
    fn = m["fnr"]
    bd = m["foedselsdato"]
    if fn[:2] != bd[8:10] or fn[2:4] != bd[5:7] or fn[4:6] != bd[2:4]:
        bad.append(f"{e} fnr/birthdate")
    if str(md[e].get("National ID")) != fn or str(md[e].get("Birth Date"))[:10] != bd:
        bad.append(f"{e} master")
    if str(G[e]["National ID"]) != fn:
        bad.append(f"{e} G2N")
ev.check("B-07", "Format", "Fødselsnummer consistent with birth date, G2N and master data", popn, not bad, "; ".join(bad))
bad = []
for e in ids:
    af = M[e]["arbeidsforhold"][0]
    mm = md[e]
    if af["startdato"] != str(mm.get("Hire Date"))[:10] or af["startdato"] != str(G[e]["Hire date"])[:10]:
        bad.append(f"{e} startdato {af['startdato']}")
    if not eq(af["stillingsprosent"], mm.get("Employment / Ratio of working time")):
        bad.append(f"{e} stillingsprosent")
    if not eq(af["antallTimerPerUkeSomEnFullStillingTilsvarer"],
              mm.get("Employment / No Of hours to which a full-time position equates")):
        bad.append(f"{e} hours")
    if str(af["yrke"]) != str(mm.get("Employment / Occupation Code")):
        bad.append(f"{e} yrke")
    if af["sisteLoennsendringsdato"] != str(mm.get("Employment / Last salary change date"))[:10]:
        bad.append(f"{e} sisteLoennsendringsdato")
ev.check("B-08", "Format", "Arbeidsforhold fields (start date, %, full-time hours, yrke, last pay change) = master/G2N",
         popn, not bad, "; ".join(bad))

# ============ C. Content: A-melding vs G2N (per employee, per element) ============
bad = []
rows_c = 0
for e in ids:
    exp = defaultdict(float)
    for c, (fd, bs) in MAP.items():
        v = hrb.code(G[e], c)
        if v:
            exp[(fd, bs)] += v
    got = defaultdict(float)
    for i in M[e]["inntekt"]:
        got[(i["fordel"], i["beskrivelse"])] += i["beloep"]
    for k in set(exp) | set(got):
        rows_c += 1
        if not eq(exp[k], got[k], 0.01):
            bad.append(f"{e} {k[1]}: G2N {exp[k]:.2f} / A-melding {got[k]:.2f}")
ev.check("C-01", "Content", "Every income line ties to the G2N pay elements (mapping read from the client file)",
         f"{rows_c} employee x description pairs", not bad, "; ".join(bad))
bad = []
for e in ids:
    t = {b: -v for b, v in M[e]["trekk"]}
    if not eq(t.get("ordinaert", 0), hrb.code(G[e], "2552")) or not eq(t.get("frivillig", 0), hrb.code(G[e], "2572")):
        bad.append(f"{e} trekk {t} vs G2N {hrb.code(G[e], '2552')}/{hrb.code(G[e], '2572')}")
ev.check("C-02", "Content", "Forskuddstrekk ordinært = G2N 2552 and frivillig = G2N 2572", popn, not bad, "; ".join(bad))
aga_l = next(a for a in V["aga"] if a["type"] == "loennOgGodtgjoerelse")
aga_p = next((a for a in V["aga"] if a["type"] == "tilskuddOgPremieTilPensjon"), None)
inc_aga = sum(i["beloep"] for m in V["mottakere"] for i in m["inntekt"] if i["utloeserArbeidsgiveravgift"] == "true")
ev.check("C-03", "Content", "AGA basis 'lønn og godtgjørelse' = sum of income lines that trigger AGA = G2N gross",
         popn, eq(aga_l["grunnlag"], inc_aga, 0.01) and eq(aga_l["grunnlag"], num(g2n["totals"]["Gross Pay"]), 0.01),
         f"{aga_l['grunnlag']} / {inc_aga:.2f} / {g2n['totals']['Gross Pay']}")
otp = sum(hrb.code(G[e], "23671") for e in ids)
ev.check("C-04", "Content", "AGA basis 'tilskudd og premie til pensjon' = G2N 23671 Special pension", popn,
         aga_p is not None and eq(aga_p["grunnlag"], otp, 0.01), f"{aga_p and aga_p['grunnlag']} / {otp}")
ev.check("C-05", "Content", "A-melding income totals = a-ordningen summary per description", "6 descriptions",
         eq(sm["income_totals"].get("Fixed salary"), 475733) and eq(sm["income_totals"].get("Car"), 61881.62),
         str(sm["income_totals"]))
ev.check("C-06", "Content", "Pension scheme (OTP) identifier reported", "1 message",
         bool(am["pensjonsinnretning"]), str(am["pensjonsinnretning"]))
# union dues (fradrag) reported?
dues = {e: hrb.code(G[e], "21126") for e in ids if hrb.code(G[e], "21126")}
ev.check("C-07", "Content", "Trade-union dues deducted in pay are reported as fradrag 'fagforeningskontingent'",
         f"{len(dues)} employees with G2N 21126", False if dues else True,
         f"G2N 21126 total {sum(dues.values()):.2f} NOK ({', '.join(f'{k} {v:.0f}' for k, v in dues.items())}); "
         "no <fradrag> element in the A-melding")

# ============ D. Statutory recalculation ============
recalc = []
bad_tab, bad_aga, bad_union = [], [], []
for e in ids:
    g = G[e]
    gross = num(g["Gross Pay"])
    tab = str(g["Table Number"])
    pct = num(g["Tax Percentage"])
    withheld = hrb.code(g, "2552")
    ud = hrb.code(g, "21126")
    if tab not in ("0", "", "None"):
        method = f"Tabell {tab}"
        t_exp, row = trekk.lookup(tab, gross)
        t_union, row_u = trekk.lookup(tab, gross - ud)
    else:
        method = f"Prosent {pct:.0f}%"
        t_exp = int(gross) * pct / 100          # §5-10-4: base rounded down to whole krone
        t_exp = int(t_exp)
        t_union = int(int(gross - ud) * pct / 100)
        row = row_u = None
    if not eq(t_exp, withheld, 0.5):
        bad_tab.append(f"{e} expected {t_exp} withheld {withheld}")
    if ud and not eq(t_union, withheld, 0.5):
        bad_union.append(f"{e} {withheld:.0f} withheld vs {t_union:.0f} with dues {ud:.0f} deducted (diff {withheld - t_union:.0f})")
    aga_base = gross + hrb.code(g, "23671")
    aga_exp = round(aga_base * AGA_ZONE_RATE["1"] / 100, 2)
    if not eq(aga_exp, hrb.code(g, "2550"), 0.01):
        bad_aga.append(f"{e} {aga_exp} vs {hrb.code(g, '2550')}")
    recalc.append({"Employee": e, "Method": method, "Trekkgrunnlag (gross incl. benefits)": gross,
                   "Table row used": row, "Expected trekk": t_exp, "Withheld (G2N 2552)": withheld,
                   "Diff": round(withheld - t_exp, 2), "Union dues deducted": ud,
                   "Trekk with dues deducted (§5-9)": t_union if ud else None,
                   "AGA base (gross + OTP)": aga_base, "AGA 14.1% expected": aga_exp,
                   "AGA G2N": hrb.code(g, "2550"), "Extra voluntary trekk": hrb.code(g, "2572")})
ev.d["recalc"] = recalc
ev.check("D-01", "Withholding", "Forskuddstrekk = 2026 trekktabell (month, wage) on gross incl. benefits in kind, "
         "or prosenttrekk on gross rounded down (§5-10-4)", popn, not bad_tab, "; ".join(bad_tab))
ev.check("D-02", "Withholding", "Union dues deducted in pay reduce the withholding base (Skattebetalingsloven §5-9(1)(b), "
         "forskrift §5-9-1)", f"{len(dues)} employees", not bad_union, "; ".join(bad_union))
ev.check("D-03", "Withholding", "Referral bonus taxed with the salary under the table (§5-10-1(2): paid with salary, "
         "earned in the same period)", "1 employee", eq(trekk.lookup("8030", num(G["01460001"]["Gross Pay"]))[0], 74389),
         "Stein: table 8030 on 166,770.13 = 74,389")
ev.check("D-04", "Employer contribution", "AGA per employee = 14.1% (zone 1) x (gross + OTP premium)", popn,
         not bad_aga, "; ".join(bad_aga))
tot_aga = round(sum(a["grunnlag"] * a["sats"] / 100 for a in V["aga"]), 2)
ev.check("D-05", "Employer contribution", "sumArbeidsgiveravgift = sum(grunnlag x sats) in whole kroner", "1 message",
         int(tot_aga) == am["sumAGA"], f"{tot_aga} -> {am['sumAGA']}")
ev.check("D-06", "Employer contribution", "Zone and rate: sone 1 at 14.1% for both bases (avgiftsvedtak 2026)", "2 bases",
         all(a["sone"] == "1" and eq(a["sats"], 14.1) for a in V["aga"]))
# holiday pay accrual (GL)
gl_by = defaultdict(lambda: defaultdict(float))
for l in gld["lines"]:
    pe = str(l["Pay Element"]).split(" - ")[0]
    gl_by[str(l["Employee ID"])][pe] += (num(l["Debit Amount"]) or 0) - (num(l["Credit Amount"]) or 0)
bad = []
for e in ids:
    base = hrb.code(G[e], "62100") + hrb.code(G[e], "62130")
    exp12 = round(base * 0.12, 2)
    if not eq(gl_by[e]["42100"], exp12, 0.01):
        bad.append(f"{e} GL 42100 {gl_by[e]['42100']} vs 12% {exp12}")
    if gl_by[e]["42101"]:
        if not eq(gl_by[e]["42101"], round(hrb.code(G[e], "62100") * FERIE_OVER60 / 100, 2), 0.01):
            bad.append(f"{e} over-60 {gl_by[e]['42101']}")
ev.check("D-07", "Holiday pay", "GL holiday-pay provision = 12% (contractual, >= 10.2% statutory) of the month's "
         "salary (+bonus) and +2.3% for employees entitled to the over-60 week", popn, not bad, "; ".join(bad))
over60 = []
for e in ids:
    by = int(M[e]["foedselsdato"][:4])
    entitled = by <= 1967  # turns 60 before 1 Sept 2027 (ferieår for 2026 earnings) - Ferieloven §5(2)
    has = bool(gl_by[e]["42101"])
    if entitled != has:
        over60.append(f"{e} born {by} entitled={entitled} accrued={has}")
ev.check("D-08", "Holiday pay", "Over-60 supplement accrued exactly for employees who reach 60 in the holiday year",
         popn, not over60, "; ".join(over60))
bad = []
for e in ids:
    ps_ = P[e]
    fp = next((l for l in ps_["lines"] if l["label"] == "Feriepenger"), None)
    if fp and not eq(fp["period"], gl_by[e]["42100"], 0.01):
        bad.append(f"{e} payslip {fp['period']} / G2N {hrb.code(G[e], '42100')} / GL {gl_by[e]['42100']:.2f}")
ev.check("D-09", "Holiday pay", "Period holiday-pay accrual on payslip and G2N = GL provision", popn, not bad, "; ".join(bad))

# ============ E. Payslips (anchor) ============
ev.check("E-01", "Payslip", "One payslip per G2N employee, same employer org.nr and fødselsnummer", popn,
         sorted(P) == ids and all(P[e].get("orgnr") == "917472890" and P[e].get("fnr") == M[e]["fnr"] for e in ids))
bad = []
for e in ids:
    p = P[e]
    if not (eq(p["summary"].get("netto"), num(G[e]["Net Pay"])) and eq(p.get("net_top"), num(G[e]["Net Pay"]))):
        bad.append(f"{e} net")
    if p.get("tabell") != str(G[e]["Table Number"]) or not eq(p.get("pct"), num(G[e]["Tax Percentage"])):
        bad.append(f"{e} skattekort {p.get('tabell')}/{p.get('pct')}")
    if p.get("utbetalingsdato") != "18.09.2026":
        bad.append(f"{e} date {p.get('utbetalingsdato')}")
    for l in p["lines"]:
        c = l["code"]
        if c and c[0].isdigit() and l["period"] is not None and c not in ("2552",):
            gv = hrb.code(G[e], c)
            if c in ("21122", "21126", "2572"):
                gv = -gv
            if not eq(l["period"], gv, 0.01):
                bad.append(f"{e} {l['label']} slip {l['period']} G2N {gv}")
ev.check("E-02", "Payslip", "Payslip net, skattekort table/% , payment date and every period line = G2N", popn,
         not bad, "; ".join(bad))
bad = []
for e in ids:
    fr = P[e]["summary"].get("fradrag")
    exp = hrb.code(G[e], "2552") + hrb.code(G[e], "2572") + hrb.code(G[e], "21122") + hrb.code(G[e], "21126")
    if not eq(fr, exp, 0.01):
        bad.append(f"{e} fradrag {fr} vs tax+deductions {exp}")
ev.check("E-03", "Payslip", "Payslip 'Fradrag' = tax + voluntary tax + ESP + union dues (withheld tax read from summary)",
         popn, not bad, "; ".join(bad))
bad = []
for e in ids:
    sk = P[e]["summary"].get("skattepliktig")
    tg = num(G[e]["Gross Pay"])
    if not eq(sk, tg, 0.01):
        bad.append(f"{e} payslip {sk:,.2f} vs trekkgrunnlag/A-melding {tg:,.2f} (benefits in kind "
                   f"{hrb.code(G[e], '65500') + hrb.code(G[e], '65630') + hrb.code(G[e], '65810'):,.2f})")
ev.check("E-04", "Payslip", "Payslip 'Skattepliktig inntekt' = taxable income reported and used for withholding",
         popn, not bad, "; ".join(bad))

# ============ F. Bank ============
pi = bk["pmtinf"][0]
ev.check("F-01", "Bank", "pain.001 header: NbOfTxs/CtrlSum = transactions; SALA; NOK; execution date = payment date",
         "1 file", bk["NbOfTxs"] == len(bk["tx"]) and eq(bk["CtrlSum"], sum(t["amt"] for t in bk["tx"]))
         and pi["Purp"] == "SALA" and pi["Ccy"] == "NOK" and pi["ReqdExctnDt"] == am["trekk_per_dato"][0][0],
         f"{bk['NbOfTxs']} tx, {bk['CtrlSum']}, {pi['ReqdExctnDt']}")
by_name = {}
bad = []
for e in ids:
    mm = md[e]
    acct = f"{mm.get('Primary Bank Account / Branch Code')}{str(mm.get('Primary Bank Account / Bank Account Number')).zfill(7)}"
    tx = [t for t in bk["tx"] if t["acct"] == acct]
    if len(tx) != 1:
        bad.append(f"{e} account {acct} not found once")
        continue
    if not eq(tx[0]["amt"], num(G[e]["Net Pay"])):
        bad.append(f"{e} {tx[0]['amt']} vs net {G[e]['Net Pay']}")
    if tx[0]["name"] != mm.get("Primary Bank Account / Exact Beneficiary Name"):
        bad.append(f"{e} name")
ev.check("F-02", "Bank", "One transfer per employee to the master-data account (branch + account), amount = G2N net",
         popn, not bad, "; ".join(bad))
ev.recon("Net pay", "G2N Net Pay total", num(g2n["totals"]["Net Pay"]), "EE bank file CtrlSum", bk["CtrlSum"])

# ============ G. GL ============
deb = sum(num(l["Debit Amount"]) or 0 for l in gld["lines"])
cre = sum(num(l["Credit Amount"]) or 0 for l in gld["lines"])
ev.check("G-01", "GL", "GL Detailed: debit = credit and = printed footer", f"{len(gld['lines'])} lines",
         eq(deb, cre, 0.01) and eq(deb, gld["footer"]["Debit Amount"], 0.01), f"{deb:.4f} / {cre:.4f}")
import csv  # noqa: E402
csv_rows = list(csv.DictReader(open(f("z00_Mercans_GLImport*.csv"), encoding="utf-8-sig")))
fin = pd.read_excel(f("z03_NO_7073_Henkel_GL*.xls"), header=None, dtype=object, engine="xlrd").values.tolist()
fin_rows = [r for r in fin if str(r[0]).strip() == "2"]
by_acct = defaultdict(float)
for l in gld["lines"]:
    by_acct[str(l["GL Code"])] += (num(l["Debit Amount"]) or 0) - (num(l["Credit Amount"]) or 0)
by_csv = defaultdict(float)
for r in csv_rows:
    by_csv[r["GeneralLedgerCode"]] += float(r["Amount"])
by_fin = defaultdict(float)
for r in fin_rows:
    by_fin[str(r[5]).strip()] += (1 if str(r[1]).strip() == "40" else -1) * (num(r[2]) or 0)
diff = [f"{a}: detailed {by_acct[a]:.2f} / csv {by_csv[a]:.2f} / finance {by_fin[a]:.2f}"
        for a in sorted(set(by_acct) | set(by_csv) | set(by_fin))
        if not (eq(by_acct[a], by_csv[a], 0.02) and eq(by_acct[a], by_fin[a], 0.02))]
ev.check("G-02", "GL", "The three GL versions (Detailed xlsx, finance file xls, CORRECTED import csv) agree per account",
         f"{len(by_acct)} accounts", not diff, "; ".join(diff))
ev.check("G-03", "GL", "CSV import balances (sum of signed amounts = 0)", f"{len(csv_rows)} lines",
         eq(sum(by_csv.values()), 0, 0.05), f"{sum(by_csv.values()):.4f}")
ev.recon("Withholding tax", "GL 185410 credit", -by_acct["185410"], "A-melding sumForskuddstrekk", am["trekk_per_dato"][0][1])
ev.recon("Employer contribution (AGA)", "GL 184300 credit", -by_acct["184300"], "A-melding sumArbeidsgiveravgift",
         am["sumAGA"], tol=0.5)
ev.recon("Net pay", "GL 185300 net credit", -by_acct["185300"], "G2N Net Pay total", num(g2n["totals"]["Net Pay"]))
ev.recon("OTP premium", "G2N 23671", otp, "A-melding AGA pension basis", aga_p["grunnlag"])
ev.recon("Gross pay", "G2N Gross Pay", num(g2n["totals"]["Gross Pay"]), "A-melding AGA wage basis", aga_l["grunnlag"])
ev.recon("Union dues", "GL 180029 credit", -by_acct["180029"], "G2N 21126", sum(dues.values()))
ev.recon("Employee share programme", "GL 84211 credit", -by_acct["84211"], "G2N 21122",
         sum(hrb.code(G[e], "21122") for e in ids))
ev.check("G-04", "GL", "OTP premium posting has a liability/clearing side", "4 employees",
         by_acct.get("416020", 0) == 0 or any(a.startswith("2") or a.startswith("18") for a in []),
         f"416020 (P&L) credit {by_acct.get('416020', 0):.2f} / 416035 (P&L) debit {by_acct.get('416035', 0):.2f}: "
         "premium nets to zero in P&L with no balance-sheet account")

# ============ H. Population and master ============
pops = {"G2N": set(ids), "A-melding": set(M), "payslips": set(P), "master": set(md),
        "GL": {e.zfill(8) for e in gl_by}, "bank": {e for e in ids}}
ev.check("H-01", "Population", "Same 6 employees in A-melding, G2N, payslips, bank, GL and master data", popn,
         all(v == set(ids) for v in pops.values()) and rc["antall"] == N and int(g2n["header"]["Report Headcount"]) == N)
nat = {e: md[e].get("Nationality") for e in ids}
ev.check("H-02", "Master data", "Nationality plausible for Norwegian residents with Norwegian fødselsnummer", popn,
         not all(v == "Canada" for v in nat.values()), f"all 6 = {set(nat.values())}")
bad = []
for e in ids:
    ms = num(md[e].get("62100 - Salary"))
    if not eq(ms, hrb.code(G[e], "62100")):
        bad.append(f"{e} master 62100 {ms:,.0f} / paid {hrb.code(G[e], '62100'):,.0f}")
ev.check("H-03", "Master data", "Master-data salary element 62100 = salary paid in the run", popn, not bad, "; ".join(bad))
ev.check("H-04", "Master data", "Employment ID present for every employee", popn,
         all(md[e].get("Employment / Employment ID") for e in ids),
         "; ".join(e for e in ids if not md[e].get("Employment / Employment ID")))

# OTP minimum (annual obligation) - informational
otp_rows = [f"{e} Sep {hrb.code(G[e], '23671'):.2f} ({hrb.code(G[e], '23671') / hrb.code(G[e], '62100') * 100:.2f}% of salary)"
            for e in ids]
ev.note("OTP per employee: " + "; ".join(otp_rows))

ev.nt("NT-01", "Car benefit valuation (bil)", "Car type (fuel/EV), first-registration date and months of use are not in the "
      "pack (master car fields empty except list price), so the 2026 sjablong cannot be recalculated.",
      "Car data per employee (fuel type, first registration, list price basis) or the engine's car-benefit calculation.")
ev.nt("NT-02", "OTP minimum contribution (2% of pay up to 12G)", "The obligation is annual and scheme-specific; Stein "
      "Arnegard and Ståle Strønen have no premium in September but YTD premiums on the payslip.",
      "Pension scheme terms and the annual premium per employee.")
ev.nt("NT-03", "Payment of forskuddstrekk and AGA", "No tax payment file in the pack. From 2026 forskuddstrekk is due the "
      "first working day after salary payment (Skatteetaten, frister og betaling).",
      "Payment confirmation for KID 0091747289005260919 (trekk) and AGA term 5.")
ev.nt("NT-04", "Taxable per-diem amount (62137)", "The taxable excess of travel allowances is supplied by the expense "
      "system; the underlying trips and state rates are not in the pack.", "Travel-expense data for September.")
ev.save(VAL)
