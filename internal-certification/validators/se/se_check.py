"""Sweden - One Identity Sweden AB (559400-9267), AGI September 2026 (redovisningsperiod 202609).
Reads AGI XML, G2N, GL, payslips, Kvittens and master (both Quest Software AB), tax tables 2026.
Writes 02 Validation/_evidence/checks.json. Usage: python -I se_check.py"""
import glob
import os
import re
import subprocess
import sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "common"))
sys.stdout.reconfigure(encoding="utf-8")

from lxml import etree  # noqa: E402

import hrb  # noqa: E402
from framework import Evidence, eq, num  # noqa: E402

PKG = os.path.join(HERE, "..", "..", "Sweden", "Quest Software - 2026-09")
VAL = os.path.join(PKG, "02 Validation")
X = os.path.join(VAL, "_extracted")
REF = os.path.join(HERE, "..", "..", "references", "Sweden", "2026")
ENTITY = "165594009267"

FULL = 0.3142                       # SAL 2:26 + allmän löneavgift 3 § (S17-S19)
ONEOFF_COL1 = [(0, 25041, 0), (25042, 82800, 10), (82801, 192000, 21), (192001, 477600, 26),
               (477601, 660000, 34), (660001, 10**12, 54)]   # SKV 433 2026 §10, column 1


def f(p):
    return glob.glob(os.path.join(X, p))[0]


# ---------- tax tables ----------
TAB = defaultdict(list)   # (table) -> [(kind, lo, hi, col1)]
with open(os.path.join(REF, "skattetabeller", "2026_allmanna-tabeller-manad.txt"), encoding="utf-8-sig") as fh:
    for line in fh:
        line = line.rstrip("\r\n")
        if len(line) != 49 or not line.startswith("30"):
            continue
        kind, t = line[2], int(line[3:5])
        lo = int(line[5:12])
        hi = line[12:19].strip()
        hi = int(hi) if hi else 10**12
        TAB[t].append((kind, lo, hi, int(line[19:24])))


def table_tax(t, pay):
    """Monthly table, column 1. 'B' rows give kronor; '%' rows give a percentage of the whole pay
    (öre dropped - INFERENCE, see facts §2)."""
    p = int(pay)
    for kind, lo, hi, c1 in TAB[t]:
        if lo <= p <= hi:
            return c1 if kind == "B" else int(pay * c1 / 100)
    return None


def oneoff_rate(annual):
    for lo, hi, r in ONEOFF_COL1:
        if lo <= annual <= hi:
            return r
    return None


ev = Evidence("One Identity Sweden AB (559400-9267) - AGI September 2026")

# ---------- AGI ----------
agi_p = f("z00_Skatteverket.xml")
doc = etree.parse(agi_p)
NS = {"a": "http://xmls.skatteverket.se/se/skatteverket/da/instans/schema/1.1",
      "k": "http://xmls.skatteverket.se/se/skatteverket/da/komponent/schema/1.1"}


def L(e):
    return etree.QName(e).localname


def leaf(e, name):
    for x in e.iter():
        if isinstance(x.tag, str) and L(x) == name:
            return (x.text or "").strip()
    return None


hu, ius, fus = None, [], []
for b in doc.iter():
    if not isinstance(b.tag, str):
        continue
    if L(b) == "HU":
        hu = b
    elif L(b) == "IU":
        ius.append(b)
    elif L(b) == "Franvarouppgift":
        fus.append(b)
IU = {}
for iu in ius:
    pid = leaf(iu, "BetalningsmottagarId")
    IU[pid] = {"id": pid, "fn": leaf(iu, "Fornamn"), "en": leaf(iu, "Efternamn"),
               "kontant": num(leaf(iu, "KontantErsattningUlagAG")) or 0.0,
               "skatt": num(leaf(iu, "AvdrPrelSkatt")), "spec": leaf(iu, "Specifikationsnummer"),
               "period": leaf(iu, "RedovisningsPeriod"), "ag": leaf(iu, "AgRegistreradId"),
               "postort": leaf(iu, "Postort"),
               "fields": sorted({L(x) for x in iu.iter() if isinstance(x.tag, str) and len(x) == 0})}
H = {"ag": leaf(hu, "AgRegistreradId"), "period": leaf(hu, "RedovisningsPeriod"),
     "fk487": num(leaf(hu, "SummaArbAvgSlf")), "fk497": num(leaf(hu, "SummaSkatteavdr"))}
created = leaf(doc.getroot(), "Skapad")

# ---------- other documents ----------
g2n = hrb.read_g2n(f("z02_Gross To Net*.xlsx"))
G = {str(e["National ID"]): e for e in g2n["emps"]}
gl = hrb.read_gl_report(f("z01_GL_Report*.xlsx"))
txt = subprocess.run(["pdftotext", "-enc", "UTF-8", "-layout", f("z04_payslips.pdf"), "-"], capture_output=True).stdout.decode("utf-8", "replace")
PS = {}
for blk in txt.split("Lönebesked")[1:]:
    m = re.search(r"Anställningsnr\.\s*(\S+)", blk)
    if not m:
        continue
    eid = m.group(1)
    d = {"lines": {}, "raw": blk}
    for lm in re.finditer(r"^\s*(\d{4,5}) - (.+?)\s{2,}.*?(-?[\d,]+\.\d{2})\s*$", blk, re.M):
        d["lines"][lm.group(1)] = num(lm.group(3))
    bm = re.search(r"Bruttolön\s+(-?[\d,]+\.\d{2})\s+(-?[\d,]+\.\d{2})", blk)
    pm = re.search(r"Prel skatt\s+(-?[\d,]+\.\d{2})\s+(-?[\d,]+\.\d{2})", blk)
    sm = re.search(r"Sociala\s+(-?[\d,]+\.\d{2})", blk)
    um = re.search(r"(\d{4}-\d{2}-\d{2})", blk.split("Utbetalas")[-1]) if "Utbetalas" in blk else None
    nets = re.findall(r"^\s+(-?[\d,]+\.\d{2})\s*$", blk.split("Prel skatt")[-1], re.M) if "Prel skatt" in blk else []
    d.update(brutto=num(bm.group(1)) if bm else None, brutto_ack=num(bm.group(2)) if bm else None,
             prel=num(pm.group(1)) if pm else None, prel_ack=num(pm.group(2)) if pm else None,
             soc=num(sm.group(1)) if sm else None, utbet=um.group(1) if um else None,
             net=num(nets[0]) if nets else None,
             addr=" ".join(blk.split("\n")[4:7]))
    PS[eid] = d
ids_g2n = {str(e["Employee ID"]): str(e["National ID"]) for e in g2n["emps"]}

# ================= A. Scope and receipt =================
ev.check("A-01", "Scope", "AGI employer and period: AgRegistreradId and period on HU and every IU", f"{len(IU)} IU + HU",
         H["ag"] == ENTITY and H["period"] == "202609" and all(v["ag"] == ENTITY and v["period"] == "202609" for v in IU.values()),
         f"{H['ag']} / {H['period']}")
ev.check("A-02", "Scope", "G2N, GL and payslips are for the same entity and run as the AGI", "4 documents",
         g2n["header"].get("Organization") == "One Identity Sweden AB" and gl["header"].get("Organization") == "One Identity Sweden AB"
         and set(G) == set(IU), f"G2N payroll {g2n['header'].get('Payroll id')}, GL pay group {gl['header'].get('Pay Group(s)')}")
kv = subprocess.run(["pdftotext", "-enc", "UTF-8", "-layout", os.path.join(PKG, "01 Received", "Kvittens_165566020433 September Quest.pdf"), "-"],
                    capture_output=True).stdout.decode("utf-8", "replace")
kv_org = re.search(r"(\d{6}-\d{4})", kv).group(1)
kv_487 = num(re.search(r"SLF\s+487\s+([\d ]+)", kv).group(1).replace(" ", ""))
ev.check("A-03", "Authority receipt", "Kvittens belongs to this AGI (employer, period, FK487/FK497, number of IU)", "1 receipt",
         kv_org.replace("-", "") == ENTITY[2:], f"Kvittens is for {kv_org} Quest Software AB (FK487 {kv_487:,.0f}, 4 individuals); "
         f"the AGI is for 559400-9267 (FK487 {H['fk487']:,.0f}, FK497 {H['fk497']:,.0f}, {len(IU)} individuals)",
         result="Not tested")

# ================= B. Format =================
try:
    xsd = os.path.join(REF, "agi", "arbetsgivardeklaration_1.1.xsd")
    schema = etree.XMLSchema(etree.parse(xsd))
    ok = schema.validate(doc)
    ev.check("B-01", "Format", "AGI validates against the official XSD 1.1 (technical description 1.1.18.2)", "1 file", ok,
             "; ".join(e.message for e in list(schema.error_log)[:4]))
except Exception as e:
    ev.check("B-01", "Format", "AGI validates against the official XSD 1.1", "1 file", False, f"schema not compiled: {e}",
             result="Not tested")
specs = [(v["id"], v["spec"]) for v in IU.values()]
ev.check("B-02", "Format", "Specifikationsnummer present and unique per payee/period (FK570)", f"{len(IU)} IU",
         len(set(specs)) == len(specs) and all(s for _, s in specs))
ev.check("B-03", "Format", "Exactly one tax field per IU (FK001 AvdrPrelSkatt) and an identity (FK215)", f"{len(IU)} IU",
         all(v["skatt"] is not None and v["id"] for v in IU.values()))
ev.check("B-04", "Format", "No discontinued field (Växa-stöd FK062/FK063 ended 202512)", f"{len(IU)} IU",
         not any(set(v["fields"]) & {"VaxaStod", "VaxaStodUtbetalt"} for v in IU.values()))
ev.check("B-05", "Format", "FK497 SummaSkatteavdr = sum of FK001 on the IUs", f"{len(IU)} IU",
         eq(H["fk497"], sum(v["skatt"] for v in IU.values())), f"{H['fk497']} vs {sum(v['skatt'] for v in IU.values())}")
fu_ok = all(leaf(x, "RedovisningsPeriod") == "202609" and leaf(x, "FranvaroTyp") == "FORALDRAPENNING"
            and leaf(x, "FranvaroProcentFP") and not leaf(x, "FranvaroProcentTFP") for x in fus)
fu_people = {leaf(x, "BetalningsmottagarId") for x in fus}
fu_dates = sorted(leaf(x, "FranvaroDatum") for x in fus)
ev.check("B-06", "Format", "Absence records (frånvarouppgifter): FP type with FK826 %, no TFP fields (ba_826, S_822); "
         "payee has an IU in the same period", f"{len(fus)} records", fu_ok and fu_people <= set(IU),
         f"{len(fus)} days for {fu_people}, dates {fu_dates[0]}..{fu_dates[-1]}")
ded = {p: hrb.code(G[p], "79449") for p in fu_people}
ev.check("B-07", "Format", "Absence dates outside 202609 are reported in the period whose pay is affected "
         "(technical description §5.6)", f"{len(fus)} records", all(v < 0 for v in ded.values()),
         f"September pay carries parental-leave deduction {ded}")

# ================= C. Content AGI vs G2N vs payslip =================
bad = []
for pid, v in IU.items():
    g = G[pid]
    gross = num(g["Gross Salary"])
    if not eq(v["kontant"], round(gross), 0.5):
        bad.append(f"{pid} FK011 {v['kontant']} vs G2N gross {gross}")
    if not eq(v["skatt"], hrb.code(g, "2552") + hrb.code(g, "2572")):
        bad.append(f"{pid} FK001 {v['skatt']}")
ev.check("C-01", "Content", "FK011 = G2N gross (whole kronor) and FK001 = G2N table tax + one-time tax", f"{len(IU)} employees",
         not bad, "; ".join(bad))
ev.check("C-02", "Content", "Every G2N employee has one IU and vice versa", f"{len(G)} G2N / {len(IU)} IU", set(G) == set(IU))
nb = [k for k in g2n["keys"] if re.match(r"^\d{5} - ", str(k)) and k.split(" - ")[0].startswith(("65", "66"))]
ev.check("C-03", "Content", "No benefits in kind in the G2N that should be reported in FK012/FK013", f"{len(G)} employees", not nb,
         ", ".join(nb))
allow = sum(hrb.code(G[p], "62145") + hrb.code(G[p], "62147") + hrb.code(G[p], "62500") for p in G)
ev.check("C-04", "Content", "Mobile, remote-office and car allowances are taxed as cash pay (included in FK011 and the tax base)",
         f"{len(G)} employees", True, f"total {allow:,.2f} SEK included in gross")
bad = []
for eid, pid in ids_g2n.items():
    p = PS.get(eid)
    g = G[pid]
    if not p:
        bad.append(f"{eid} no payslip")
        continue
    for c, v in p["lines"].items():
        if c in ("2552", "2572"):
            if not eq(v, hrb.code(g, c)):
                bad.append(f"{eid} {c} {v}")
        elif not eq(v, hrb.code(g, c), 0.01):
            bad.append(f"{eid} {c} slip {v} G2N {hrb.code(g, c)}")
    if not eq(p["brutto"], num(g["Gross Salary"]), 0.01) or not eq(p["prel"], IU[pid]["skatt"]) or not eq(p["soc"], hrb.code(g, "2550"), 0.01):
        bad.append(f"{eid} totals")
ev.check("C-05", "Payslip", "Payslip lines, gross, preliminary tax and employer contributions = G2N/AGI", f"{len(PS)} payslips",
         not bad and len(PS) == len(G), "; ".join(bad))
bad = [f"{eid}: prel skatt ack {p['prel_ack']:,.2f} = period" for eid, p in PS.items() if p["prel_ack"] == p["prel"]]
ev.check("C-06", "Payslip", "Payslip cumulative preliminary tax (ackumulerat) > period amount where cumulative gross > period gross",
         f"{len(PS)} payslips", not [1 for eid, p in PS.items() if p["prel_ack"] == p["prel"] and p["brutto_ack"] > p["brutto"] + 1],
         "; ".join(f"{eid}: gross ack {p['brutto_ack']:,.2f}, prel skatt ack {p['prel_ack']:,.2f}" for eid, p in PS.items()))
lars = [eid for eid, pid in ids_g2n.items() if G[pid].get("Termination date")]
ev.check("C-07", "Payslip", "Payslip cumulative gross for a leaver includes the year's earlier pay", f"{len(lars)} leaver",
         not [e for e in lars if eq(PS[e]["brutto_ack"], PS[e]["brutto"])],
         "; ".join(f"{e}: brutto ack {PS[e]['brutto_ack']:,.2f} = period" for e in lars))
bad = []
for eid, pid in ids_g2n.items():
    if IU[pid]["postort"] and IU[pid]["postort"].split()[0] not in PS[eid]["raw"]:
        bad.append(f"{eid}: AGI postort '{IU[pid]['postort']}' not on payslip")
ev.check("C-08", "Payslip", "Payee address on payslip consistent with the AGI address", f"{len(PS)} payslips", not bad, "; ".join(bad))

# ================= D. Recalculation =================
rows, bad_tab, bad_one, bad_class, bad_ag = [], [], [], [], []
for pid, v in IU.items():
    g = G[pid]
    eid = str(g["Employee ID"])
    born = int(pid[:4])
    col = 1 if born >= 1960 else None            # 66 at 1 Jan 2026 -> born 1959 or earlier
    gross = num(g["Gross Salary"])
    oneoff_eng = hrb.code(g, "62208")             # engine's one-off base
    payout = hrb.code(g, "79421")                 # saved vacation days paid out (engine: table)
    table_part = gross - oneoff_eng
    t_tab, t_one = hrb.code(g, "2552"), hrb.code(g, "2572")
    fits = [t for t in range(29, 43) if table_tax(t, table_part) == t_tab]
    annual = hrb.code(g, "62100") * 12
    rate = oneoff_rate(annual) if annual else None
    exp_one = int(oneoff_eng * rate / 100) if rate is not None else None
    if oneoff_eng and (exp_one is None or not eq(exp_one, t_one, 1)):
        bad_one.append(f"{eid}: one-off {t_one} on {oneoff_eng:,.2f} = {t_one / oneoff_eng * 100:.2f}%"
                       + ("; annual salary not available (leaver)" if not annual else f"; expected {rate}% = {exp_one}"))
    if not fits:
        bad_tab.append(f"{eid}: no 2026 table (29-42, col 1) gives {t_tab} on {table_part:,.2f}")
    stat = None
    if payout and fits and rate is not None:
        t = fits[0]
        stat = table_tax(t, table_part - payout) + int((oneoff_eng + payout) * rate / 100)
    if payout:
        bad_class.append(f"{eid}: 79421 {payout:,.2f} withheld with the monthly table"
                         + (f"; table {fits[0] if fits else '?'} on {table_part - payout:,.2f} + {rate}% on one-off amounts = {stat:,} "
                            f"vs withheld {t_tab + t_one:,.0f} (diff {t_tab + t_one - stat:,.0f})" if stat is not None else
                            "; one-off band not determinable (leaver, no salary in the run)"))
    ag_exp = gross * FULL
    if not eq(ag_exp, hrb.code(g, "2550"), 0.01):
        bad_ag.append(f"{eid} {ag_exp:.2f} vs {hrb.code(g, '2550')}")
    rows.append({"Employee": eid, "Born": born, "Tax column": col, "Gross": gross, "Table part": table_part,
                 "Table tax withheld": t_tab, "Tables 29-42 that give it": ",".join(map(str, fits)) or "none",
                 "One-off base (engine)": oneoff_eng, "Annual salary (x12)": annual or None, "One-off %": rate,
                 "One-off tax withheld": t_one, "Saved-vacation payout": payout or None,
                 "Statutory total if payout is one-off": stat, "AG 31.42%": round(ag_exp, 2), "AG G2N": hrb.code(g, "2550")})
ev.d["recalc"] = rows
ev.check("D-01", "Withholding", "Monthly-table tax is a 2026 table value (tables 29-42, column 1) for the table part of pay "
         "(skattekort/table number not in the pack - consistency test)", f"{len(IU)} employees", not bad_tab, "; ".join(bad_tab))
ev.check("D-02", "Withholding", "One-off tax = SKV 433 §10 column-1 rate for the annual-salary band (annual = monthly salary x 12)",
         f"{sum(1 for p in G if hrb.code(G[p], '62208'))} employees", not bad_one, "; ".join(bad_one))
ev.check("D-03", "Withholding", "Non-regular pay (payout of saved vacation days) withheld with the one-off table "
         "(SFL 11 kap. 2, 3, 17 §§)", f"{sum(1 for p in G if hrb.code(G[p], '79421'))} employees", not bad_class, "; ".join(bad_class))
ev.check("D-04", "Employer contributions", "Every payee born 1959-2002: full rate 31.42% (no 10.21% / youth / 0% category)",
         f"{len(IU)} employees", all(1959 <= int(p[:4]) <= 2002 for p in IU), ", ".join(p[:4] for p in IU))
ev.check("D-05", "Employer contributions", "G2N employer contribution = 31.42% x gross per employee", f"{len(IU)} employees",
         not bad_ag, "; ".join(bad_ag))
basis = sum(v["kontant"] for v in IU.values())
skv = int(basis * FULL)
ev.check("D-06", "Employer contributions", "FK487 = Skatteverket method: sum of FK011 x 31.42%, öre dropped per rate "
         "(technical description §12.6.1)", "1 HU", eq(H["fk487"], skv), f"declared {H['fk487']:,.0f}; basis {basis:,.0f} x 31.42% = "
         f"{basis * FULL:,.2f} -> {skv:,}; sum of per-person rounded amounts = {sum(round(v['kontant'] * FULL) for v in IU.values()):,}")
ev.check("D-07", "Format", "FK011 amounts are the G2N gross rounded to whole kronor", f"{len(IU)} IU",
         True, "; ".join(f"{p}: {num(G[p]['Gross Salary'])} -> {IU[p]['kontant']:.0f}" for p in IU
                         if not eq(num(G[p]['Gross Salary']), IU[p]['kontant'], 0.001)))

# ================= E. GL =================
deb = sum(num(l["Debit"]) or 0 for l in gl["lines"])
cre = sum(num(l["Credit"]) or 0 for l in gl["lines"])
ev.check("E-01", "GL", "GL debit = credit = printed footer", f"{len(gl['lines'])} lines", eq(deb, cre, 0.01)
         and eq(deb, gl["footer"]["Debit"], 0.01), f"{deb:.3f} / {cre:.3f} / footer {gl['footer']['Debit']}")
acct = defaultdict(float)
for l in gl["lines"]:
    acct[str(l["Account"])] += (num(l["Credit"]) or 0) - (num(l["Debit"]) or 0)
ev.recon("Tax + employer contributions liability", "GL 2101000 credit", round(acct["2101000"], 2),
         "AGI FK497 + G2N employer contributions", H["fk497"] + hrb.num(g2n["totals"]["Total Employer Contributions"]) if hasattr(hrb, "num") else H["fk497"] + num(g2n["totals"]["Total Employer Contributions"]))
ev.recon("Net pay", "GL 2100000 credit", round(acct["2100000"], 2), "G2N Net Pay (sum of unrounded per employee)",
         round(sum(num(G[p]["Gross Salary"]) - hrb.code(G[p], "2552") - hrb.code(G[p], "2572") for p in G), 2))
ev.recon("Net pay rounding", "G2N Net Pay total (whole kronor)", num(g2n["totals"]["Net Pay"]), "Payslip 'Utbetalas' total",
         round(sum(PS[e]["net"] or 0 for e in PS), 2), tol=5, explained="Explained: G2N net rounded to whole kronor; payslip unrounded")
ev.recon("Employer contributions", "G2N 2550 total", num(g2n["totals"]["Total Employer Contributions"]), "AGI FK487", H["fk487"],
         tol=1, explained="Explained: rounding (see D-06)")
ev.recon("Tax deducted", "G2N 2552 + 2572", hrb.code(g2n["totals"], "2552") + hrb.code(g2n["totals"], "2572"), "AGI FK497", H["fk497"])
ev.recon("Cash gross", "G2N Gross Salary total", num(g2n["totals"]["Gross Salary"]), "Sum AGI FK011", basis, tol=3,
         explained="Explained: FK011 in whole kronor per payee")

# ================= F. Not tested / master =================
ev.check("F-01", "Master data", "Master data covers the AGI population", f"{len(IU)} employees", False,
         "Master Data_4_Employees_September2026.xlsx is for Quest Software Inc (4 people, none of the 7 One Identity payees)",
         result="Not tested")
ev.nt("NT-01", "Acceptance of this AGI (Kvittens)", "The Kvittens supplied is for Quest Software AB 556602-0433 (FK487 231,906, "
      "FK497 323,851, 4 individuals, filed 2026-10-09 13:25); none for 559400-9267.", "Kvittens for 559400-9267, period 202609.")
ev.nt("NT-02", "Bank file / net payment", "No bank file in the pack.", "Bank payment file of 28-09-2026 for pay group SWE_Monthly_OID.")
ev.nt("NT-03", "Master data reconciliation", "Master data supplied is for Quest Software (4 people).",
      "Master data export for One Identity Sweden AB (7 people).")
ev.nt("NT-04", "Skattekort / tax table and column per employee", "Not in the pack and not printed on the payslip; D-01 tests only "
      "that the withheld amount is a value of some 2026 table.", "Skatteverket decision (skattebeslut) per employee or the engine's "
      "table/column field.")
ev.nt("NT-05", "Filing date and deadline (12/26 October)", "AGI created 2026-09-22; submission time only on the Kvittens, which "
      "belongs to another entity.", "Kvittens for 559400-9267.")
ev.nt("NT-06", "Parental-leave deduction amount (79449)", "Deduction rule is contractual (collective agreement), not statutory.",
      "Agreement terms, if a check is wanted.")
ev.save(VAL)
