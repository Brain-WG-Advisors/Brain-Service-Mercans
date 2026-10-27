"""Netherlands internal certification - per-client checks on a monthly 2026 pack.

Recalculates from the loonaangifte with the official 2026 tables and rates, then
ties the return, the gross-to-net, the payslips, the payment files and the GL
to each other per employee. Writes _evidence/checks.json; the workbook is built
from that file by build_workbook.py.

Usage:  python nl_check.py <client_key>      (see clients.py)
"""
import collections
import datetime as dt
import json
import os
import re
import subprocess
import sys
import warnings
import xml.etree.ElementTree as ET

warnings.filterwarnings("ignore")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import g2n as G                                   # noqa: E402  (loader, table parser)
from clients import CLIENTS, NL                   # noqa: E402

REF = os.path.join(NL, "_references", "2026")

# --- Official 2026 parameters (Handboek Loonheffingen 2026, versie maart 2026,
#     Bijlage 1 Tabel 9/11/12; tables "uitgave januari 2026") -------------------
R26 = {"AofLg": 0.0627, "AofHg": 0.0763, "Wko": 0.0050, "AwfLg": 0.0274,
       "AwfHg": 0.0774, "WghZvw": 0.0610, "BijdrZvw": 0.0485,
       "max_maand": 6617.41, "max_jaar": 79409.00, "aow": 67,
       "table_top": 11092.50, "top_rate": 0.4950}
PERIOD = ("2026-09-01", "2026-09-30")

# Bijzondere-beloning tables 2026, under-AOW columns (zonder LHK, met LHK
# standaard, verrekeningspercentage) and AOW born >=1946 columns (zonder,
# excl. AOK std, excl. verr., incl. AOK std, incl. verr.). Read with word
# positions from the official PDFs (layout text misaligns the verr. column).
# Columns: jaarloon_from, under-AOW (zonder, met std, met verr), AOW born <=1945
# (zonder, excl.AOK std, excl.AOK verr, incl.AOK std, incl.AOK verr), AOW born
# >=1946 (same five). Read with pdfplumber word positions from the official
# PDFs (uitgave januari 2026); the layout text misaligns the verr. column.
BB = {
    "wit": [
        (0, 35.75, 0.00, 0.00, 17.85, 0.00, 0.00, 0.00, 0.00, 17.85, 0.00, 0.00, 0.00, 0.00),
        (11358, 35.75, 35.75, -8.32, 17.85, 0.00, 0.00, 0.00, 0.00, 17.85, 0.00, 0.00, 0.00, 0.00),
        (12923, 35.75, 35.75, -31.01, 17.85, 0.00, 0.00, 0.00, 0.00, 17.85, 0.00, 0.00, 0.00, 0.00),
        (23931, 35.75, 35.75, -1.95, 17.85, 0.00, 0.00, 0.00, 0.00, 17.85, 0.00, 0.00, 0.00, 0.00),
        (29737, 35.75, 35.75, 4.45, 17.85, 0.00, 0.00, 0.00, 0.00, 17.85, 0.00, 0.00, 0.00, 0.00),
        (34719, 35.75, 35.75, 4.45, 17.85, 17.85, 2.22, 0.00, 0.00, 17.85, 17.85, 2.22, 0.00, 0.00),
        (37409, 35.75, 35.75, 4.45, 17.85, 17.85, 2.22, 17.85, 2.22, 17.85, 17.85, 2.22, 17.85, 2.22),
        (38884, 37.56, 37.56, 4.45, 17.85, 17.85, 2.22, 17.85, 2.22, 37.56, 37.56, 2.22, 37.56, 2.22),
        (41124, 37.56, 37.56, 4.45, 37.56, 37.56, 2.22, 37.56, 2.22, 37.56, 37.56, 2.22, 37.56, 2.22),
        (45593, 37.56, 37.56, 12.91, 37.56, 37.56, 6.45, 37.56, 6.45, 37.56, 37.56, 6.45, 37.56, 6.45),
        (46003, 37.56, 37.56, 12.91, 37.56, 37.56, 21.45, 37.56, 21.45, 37.56, 37.56, 21.45, 37.56, 21.45),
        (59783, 37.56, 37.56, 12.91, 37.56, 37.56, 6.45, 37.56, 6.45, 37.56, 37.56, 6.45, 37.56, 6.45),
        (78427, 49.50, 49.50, 6.51, 49.50, 49.50, 3.25, 49.50, 3.25, 49.50, 49.50, 3.25, 49.50, 3.25),
        (143555, 49.50, 49.50, 0.00, 49.50, 49.50, 0.00, 49.50, 0.00, 49.50, 49.50, 0.00, 49.50, 0.00)],
    "groen": [
        (0, 35.75, 0.00, 0.00, 17.85, 0.00, 0.00, 0.00, 0.00, 17.85, 0.00, 0.00, 0.00, 0.00),
        (8714, 35.75, 35.75, 0.00, 17.85, 0.00, 0.00, 0.00, 0.00, 17.85, 0.00, 0.00, 0.00, 0.00),
        (20297, 35.75, 35.75, 0.00, 17.85, 17.85, 0.00, 0.00, 0.00, 17.85, 17.85, 0.00, 0.00, 0.00),
        (23323, 35.75, 35.75, 0.00, 17.85, 17.85, 0.00, 17.85, 0.00, 17.85, 17.85, 0.00, 17.85, 0.00),
        (29737, 35.75, 35.75, 6.40, 17.85, 17.85, 3.20, 17.85, 3.20, 17.85, 17.85, 3.20, 17.85, 3.20),
        (38884, 37.56, 37.56, 6.40, 17.85, 17.85, 3.20, 17.85, 3.20, 37.56, 37.56, 3.20, 37.56, 3.20),
        (41124, 37.56, 37.56, 6.40, 37.56, 37.56, 3.20, 37.56, 3.20, 37.56, 37.56, 3.20, 37.56, 3.20),
        (46003, 37.56, 37.56, 6.40, 37.56, 37.56, 18.20, 37.56, 18.20, 37.56, 37.56, 18.20, 37.56, 18.20),
        (59783, 37.56, 37.56, 6.40, 37.56, 37.56, 3.20, 37.56, 3.20, 37.56, 37.56, 3.20, 37.56, 3.20),
        (78427, 49.50, 49.50, 0.00, 49.50, 49.50, 0.00, 49.50, 0.00, 49.50, 49.50, 0.00, 49.50, 0.00)],
}


def _bb_rates(row, lhk, aow=False, pre46=False):
    """All rates a row allows: AOW rows allow excl. and incl. AOK."""
    if not aow:
        return [round(row[2] + row[3], 2) if lhk else row[1]]
    b = 4 if pre46 else 9
    if not lhk:
        return [row[b]]
    return [round(row[b + 1] + row[b + 2], 2), round(row[b + 3] + row[b + 4], 2)]


def bb_valid_rates(colour, lhk, aow=False, pre46=False):
    """Every percentage a correct BT application can produce (column membership)."""
    out = {}
    for row in BB[colour]:
        for rate in _bb_rates(row, lhk, aow, pre46):
            out.setdefault(rate, []).append(row[0])
    return out


def bb_rate_for_jaarloon(colour, lhk, jaarloon, aow=False, pre46=False, aok=False):
    row = [r for r in BB[colour] if r[0] <= jaarloon][-1]
    rates = _bb_rates(row, lhk, aow, pre46)
    return rates[-1] if (aok and len(rates) > 1) else rates[0]


def s(tag):
    return tag.split("}")[-1]


def fnum(x):
    try:
        return float(str(x).replace(",", ""))
    except (TypeError, ValueError):
        return 0.0


# ----------------------------------------------------------------- XML ------
def parse_return(path):
    root = ET.parse(path).getroot()
    out = {"namespace": re.search(r"Loonaangifte/(\d{4})/(\d\d)", root.tag).groups(),
           "version": root.get("version"), "header": {}, "period": None,
           "corrections": []}
    for e in root.iter():
        if s(e.tag) in ("IdBer", "DatTdAanm", "ContPers", "TelNr", "RelNr",
                        "GebrSwPakket", "LhNr", "NmIP"):
            out["header"].setdefault(s(e.tag), (e.text or "").strip())
    for blk in root.iter():
        t = s(blk.tag)
        if t not in ("TijdvakAangifte", "TijdvakCorrectie"):
            continue
        b = {"start": None, "end": None, "coll": {}, "saldi": [], "ikvs": []}
        for c in blk:
            if s(c.tag) == "DatAanvTv":
                b["start"] = c.text
            elif s(c.tag) == "DatEindTv":
                b["end"] = c.text
        for e in blk.iter():
            if s(e.tag) == "CollectieveAangifte":
                for c in e:
                    if s(c.tag) == "SaldoCorrectiesVoorgaandTijdvak":
                        b["saldi"].append({s(g.tag): g.text for g in c})
                    elif not list(c):
                        b["coll"][s(c.tag)] = c.text
            if s(e.tag) in ("InkomstenverhoudingInitieel", "Inkomstenverhouding"):
                b["ikvs"].append(parse_ikv(e))
        if t == "TijdvakAangifte":
            out["period"] = b
        else:
            out["corrections"].append(b)
    return out


def parse_ikv(el):
    """IKV-level fields kept apart from the Inkomstenperiode fields."""
    ikv = {"_periods": []}
    for c in el:
        tag = s(c.tag)
        if tag == "NatuurlijkPersoon":
            for g in c.iter():
                if g.text and g.text.strip() and not list(g):
                    ikv["NP_" + s(g.tag)] = g.text.strip()
        elif tag == "Inkomstenperiode":
            ikv["_periods"].append({s(g.tag): g.text.strip() for g in c.iter()
                                    if g.text and g.text.strip() and not list(g)})
        elif not list(c):
            ikv[tag] = (c.text or "").strip()
        else:
            for g in c.iter():
                if g.text and g.text.strip() and not list(g):
                    ikv.setdefault(s(g.tag), g.text.strip())
    ip = ikv["_periods"][-1] if ikv["_periods"] else {}
    for k, v in ip.items():
        ikv.setdefault("IP_" + k, v)
    return ikv


# -------------------------------------------------------------- tables -----
_TABLE = {}


def period_table(colour):
    if colour not in _TABLE:
        fn = {"wit": "wit_mnd_nl_std_20260101.pdf",
              "groen": "groen_mnd_nl_std_20260101.pdf"}[colour]
        _TABLE[colour] = G.parse_period_table(os.path.join(REF, fn))
    return _TABLE[colour]


def aow_reached(dob, period_end=PERIOD[1]):
    """Handboek 2026 §9.3.3: AOW column from the 1st day of the month in
    which the AOW age is reached."""
    b = dt.date.fromisoformat(dob[:10])
    try:
        d = b.replace(year=b.year + R26["aow"])
    except ValueError:
        d = b.replace(year=b.year + R26["aow"], day=28)
    e = dt.date.fromisoformat(period_end)
    return (d.year, d.month) <= (e.year, e.month)


def table_tax(colour, tabelloon, aow, lhk, born_pre46=False):
    """(withholding, verrekende arbeidskorting) from the monthly table."""
    rows = period_table(colour)
    if tabelloon < rows[0][0]:
        return 0.0, 0.0
    top = rows[-1]
    r = [x for x in rows if x[0] <= tabelloon][-1]
    if not aow:
        tax, ak = (r[2] if lhk else r[1]), (r[3] if lhk else 0.0)
    else:
        base = 4 if born_pre46 else 8
        if r[base] is None:
            raise LookupError(f"AOW columns blank in the text layer at {r[0]}")
        tax, ak = (r[base + 1] if lhk else r[base]), (r[base + 3] if lhk else 0.0)
    if tabelloon > R26["table_top"]:
        # "neem 49,50% van het verschil ... Rond het resultaat af op centen in
        # het voordeel van de werknemer" (table footer)
        import math
        extra = math.floor((tabelloon - top[0]) * R26["top_rate"] * 100) / 100
        tax = tax + extra
    return round(tax, 2), round(ak, 2)


# ------------------------------------------------------------ payslips -----
def payslip_pages(pdf, id_re=r"Pers\. nr\.\s+(\S+)"):
    txt = subprocess.run(["pdftotext", "-layout", pdf, "-"], capture_output=True,
                         text=True, encoding="utf-8", errors="replace",
                         check=True).stdout
    pages = {}
    for pg in txt.split("\f"):
        m = re.search(id_re, pg)
        if m:
            pages.setdefault(m.group(1), []).append(pg)
    return pages


def eu(x):
    """'3.966,01' -> 3966.01"""
    return float(x.replace(".", "").replace(",", "."))


def amounts_on(page, fmt="us"):
    vals = set()
    if fmt == "eu":
        for m in re.finditer(r"-?\d{1,3}(?:\.\d{3})*,\d{2}\b", page):
            vals.add(round(eu(m.group(0)), 2))
    else:
        for m in re.finditer(r"-?\d{1,3}(?:,\d{3})*\.\d{2}|-?\d+\.\d{2}", page):
            vals.add(round(fnum(m.group(0)), 2))
    return vals


def header_field(page, label):
    m = re.search(re.escape(label) + r"[^\S\n]{2,}(\S+(?: \S+)?)", page)
    return m.group(1).strip() if m else None


# --------------------------------------------------------------- SEPA ------
def parse_sepa(path):
    r = ET.parse(path).getroot()
    hdr = {s(e.tag): (e.text or "").strip() for e in r.iter()
           if s(e.tag) in ("MsgId", "CreDtTm", "NbOfTxs", "CtrlSum", "ReqdExctnDt")}
    tx = []
    for t in r.iter():
        if s(t.tag) != "CdtTrfTxInf":
            continue
        d = {}
        for e in t.iter():
            if s(e.tag) == "Cdtr":
                d["name"] = next((g.text for g in e.iter() if s(g.tag) == "Nm"), None)
            elif s(e.tag) == "CdtrAcct":
                d["iban"] = next((g.text for g in e.iter() if s(g.tag) == "IBAN"), None)
            elif s(e.tag) in ("InstdAmt", "EndToEndId", "Ustrd", "InstrId"):
                d[s(e.tag)] = (e.text or "").strip()
        tx.append(d)
    return hdr, tx


# --------------------------------------------------------------- main ------
class Out:
    def __init__(self):
        self.checks = []          # every check: id, area, check, population, result, detail
        self.findings = []
        self.recon = []
        self.not_tested = []
        self.notes = []

    def check(self, cid, area, check, population, result, detail=""):
        self.checks.append(dict(id=cid, area=area, check=check,
                                population=population, result=result,
                                detail=detail))

    def find(self, sev, area, finding, evidence, impact, basis, cid, n):
        self.findings.append(dict(severity=sev, area=area, finding=finding,
                                  evidence=evidence, impact=impact, basis=basis,
                                  control=cid, records=n))
        self.check(cid, area, finding[:140], n, "Finding")

    def rec(self, item, a_src, a, b_src, b, tol=0.01):
        diff = round((a or 0) - (b or 0), 2)
        self.recon.append(dict(item=item, a_src=a_src, a=round(a or 0, 2),
                               b_src=b_src, b=round(b or 0, 2), diff=diff,
                               result="Pass" if abs(diff) <= tol else "Difference"))
        return abs(diff) <= tol


def run(key):
    C = CLIENTS[key]
    base = os.path.join(NL, C["folder"], "02 Validation")
    X = lambda p: os.path.join(base, "_extracted", p)   # noqa: E731
    o = Out()
    ret = parse_return(X(C["xml"]))
    P = ret["period"]
    ikvs = P["ikvs"]
    o.notes.append(f"Return {C['xml']}: namespace {ret['namespace']}, version "
                   f"{ret['version']}, {len(ikvs)} IKVs in the period block, "
                   f"{len(ret['corrections'])} correction blocks.")
    # ---------------- A: scope -------------------------------------------
    o.check("A-01", "Scope", "Namespace year 2026 matches the period year",
            "1 return", "Pass" if ret["namespace"][0] == "2026" else "Finding")
    o.check("A-02", "Scope", "Tijdvak 2026-09-01..2026-09-30 is tijdvakcode 6090 "
            "(deadline 31-10-2026); submitted " + ret["header"].get("DatTdAanm", ""),
            "1 return", "Pass" if (P["start"], P["end"]) == PERIOD else "Finding")
    months = {(f"2026-{m:02d}-01") for m in range(1, 9)}
    bad = [c for c in ret["corrections"] if c["start"] not in months]
    o.check("A-03", "Scope", "Correction blocks are earlier 2026 monthly tijdvakken",
            f"{len(ret['corrections'])} blocks", "Pass" if not bad else "Finding")

    # ---------------- B: internal consistency ----------------------------
    coll = P["coll"]
    sums = collections.Counter()
    for k in ikvs:
        for f_ in ("LnLbPh", "LnSV", "IngLbPh", "PrAofLg", "PrAofHg", "PrAofUit",
                   "OpslWko", "PrGediffWhk", "PrAwfLg", "PrAwfHg", "PrAwfHz",
                   "BijdrZvw", "WghZvw", "VerrArbKrt", "PrUFO",
                   "PrlnAofAnwLg", "PrlnAofAnwHg", "PrlnAofAnwUit", "PrlnWhkAnw",
                   "PrlnAwfAnwLg", "PrlnAwfAnwHg", "PrlnAwfAnwHz", "PrlnAwfAnwUit"):
            sums[f_] += fnum(k.get(f_, k.get("IP_" + f_, 0)))
    pairs = {"TotLnLbPh": "LnLbPh", "TotLnSV": "LnSV", "IngLbPh": "IngLbPh",
             "TotPrAofLg": "PrAofLg", "TotPrAofHg": "PrAofHg",
             "TotOpslWko": "OpslWko", "TotPrGediffWhk": "PrGediffWhk",
             "TotPrAwfLg": "PrAwfLg", "TotPrAwfHg": "PrAwfHg",
             "IngBijdrZvw": "BijdrZvw", "TotWghZvw": "WghZvw",
             "TotPrlnAofAnwLg": "PrlnAofAnwLg", "TotPrlnAofAnwHg": "PrlnAofAnwHg",
             "TotPrlnWhkAnw": "PrlnWhkAnw", "TotPrlnAwfAnwLg": "PrlnAwfAnwLg",
             "TotPrlnAwfAnwHg": "PrlnAwfAnwHg"}
    bad = []
    for ck, nk in pairs.items():
        if ck in coll:
            # collective amounts are whole euros, rounded or truncated, EUR 1 margin (Gegevensspec. 2026 §4.1)
            if abs(fnum(coll[ck]) - int(sums[nk])) > 1:
                bad.append(f"{ck} {coll[ck]} vs sum {sums[nk]:.2f}")
    if bad:
        o.find("Medium", "Return consistency", "Collective totals do not equal the "
               "sum of the nominative amounts (whole-euro rounding allowed).",
               "; ".join(bad), "", "Gegevensspecificaties 2026, collectieve aangifte",
               "B-01", len(bad))
    else:
        o.check("B-01", "Return consistency", "Each collective total equals the "
                "sum of its nominative field (whole euros, rounded; EUR 1 margin)",
                f"{len(pairs)} rubrieken x {len(ikvs)} IKVs", "Pass")
    tot = sum(fnum(coll.get(k, 0)) for k in (
        "IngLbPh", "TotPrAofLg", "TotPrAofHg", "TotPrAofUit", "TotOpslWko",
        "TotPrGediffWhk", "TotPrAwfLg", "TotPrAwfHg", "TotPrAwfHz", "TotPrAwfUit",
        "PrUFO", "TotPrUFO",
        "IngBijdrZvw", "TotWghZvw", "TotEHPubUitk", "TotEHGebrAuto", "TotEHVUT",
        "EHPubUitk", "EHGebrAuto", "EHVUT", "EhOvsFrfWrkkstrg", "AVZeev", "VrlAVSO"))
    saldi = sum(fnum(x.get("Saldo")) for x in P["saldi"])
    o.rec("Tax due for the period", "Return TotTeBet", fnum(coll.get("TotTeBet")),
          "Sum of collective tax and premium rubrieken", tot, tol=1)
    o.rec("Total to pay incl. corrections", "Return TotGen",
          fnum(coll.get("TotGen")), "TotTeBet + correction saldi",
          fnum(coll.get("TotTeBet")) + saldi, tol=0.5)
    o.check("B-02", "Return consistency", "TotGen = TotTeBet + correction saldi",
            "collective", o.recon[-1]["result"] == "Pass" and "Pass" or "Finding")

    # ---------------- per-IKV statutory recalculation ---------------------
    reg_hits, ak_hits, bt_bad, prem_hits, cap_hits, rows = [], [], [], [], [], []
    aok_rows = []
    for k in ikvs:
        pid, lb = k.get("PersNr"), k.get("IP_LbTab", "")
        lhk = k.get("IP_IndLhKort") == "J"
        dob = k.get("NP_Gebdat")
        aow = aow_reached(dob) if dob else False
        lnlb, bbw = fnum(k.get("LnLbPh")), fnum(k.get("LnTabBB"))
        ing, ak = fnum(k.get("IngLbPh")), fnum(k.get("VerrArbKrt"))
        row = dict(PersNr=pid, NumIV=k.get("NumIV"), LbTab=lb, LHK=lhk, AOW=aow,
                   SrtIV=k.get("IP_SrtIV"), LnLbPh=lnlb, LnTabBB=bbw,
                   IngLbPh=ing, VerrArbKrt=ak)
        colour = {"1": "wit", "2": "groen"}.get(lb[1:2])
        if lb[:1] == "0" and colour and lb[2:3] == "2":       # monthly table
            tl = round(lnlb - bbw, 2)
            if colour != "wit":
                raise LookupError("groene maandtabel not parsed; LbTab " + lb)
            exp, exp_ak = table_tax(colour, tl, aow, lhk, dob and dob[:4] <= "1945")
            bt = round(ing - exp, 2)
            row.update(tabelloon=tl, exp_regular=exp, exp_ak=exp_ak, bt_tax=bt)
            if abs(bbw) > 0.005:
                rate = round(bt / bbw * 100, 2)
                row["bt_rate"] = rate
                valid = bb_valid_rates(colour, lhk, aow, bool(dob and dob[:4] <= "1945"))
                if not any(abs(rate - v) <= 0.02 or abs(round(bbw * v / 100, 2) - bt) <= 0.02
                           for v in valid):
                    bt_bad.append(row)
            elif abs(ing - exp) > 0.02:
                if aow and lhk:
                    r = [x for x in period_table(colour) if x[0] <= tl][-1]
                    b = 4 if (dob and dob[:4] <= "1945") else 8
                    if abs(ing - r[b + 2]) <= 0.02:
                        row["aok_applied"] = True
                        aok_rows.append(row)
                        rows.append(row)
                        continue
                reg_hits.append(row)
            if lhk and colour == "wit" and abs(ak - exp_ak) > 0.02:
                ak_hits.append(row)
        elif lb[:1] == "0" and colour and lb[2:3] == "0":     # bb table only
            rate = round(ing / bbw * 100, 2) if bbw else None
            row.update(bt_rate=rate, tabelloon=round(lnlb - bbw, 2))
            if bbw and not any(abs(rate - v) <= 0.02 or abs(round(bbw * v / 100, 2) - ing) <= 0.02
                               for v in bb_valid_rates(colour, lhk, aow,
                                                       bool(dob and dob[:4] <= "1945"))):
                bt_bad.append(row)
        # employer premiums from their own declared base (E-01)
        for prem, basek, r in (("PrAofLg", "PrlnAofAnwLg", R26["AofLg"]),
                               ("PrAofHg", "PrlnAofAnwHg", R26["AofHg"]),
                               ("PrAofUit", "PrlnAofAnwUit", R26["AofHg"]),
                               ("PrAwfUit", "PrlnAwfAnwUit", R26["AwfLg"]),
                               ("PrAwfLg", "PrlnAwfAnwLg", R26["AwfLg"]),
                               ("PrAwfHg", "PrlnAwfAnwHg", R26["AwfHg"])):
            b, p = fnum(k.get(basek)), fnum(k.get(prem))
            if abs(round(b * r, 2) - p) > 0.02:
                prem_hits.append((pid, k.get("NumIV"), prem, b, p, round(b * r, 2)))
        aofb = fnum(k.get("PrlnAofAnwLg")) + fnum(k.get("PrlnAofAnwHg")) + fnum(k.get("PrlnAofAnwUit"))
        if abs(round(aofb * R26["Wko"], 2) - fnum(k.get("OpslWko"))) > 0.02:
            prem_hits.append((pid, k.get("NumIV"), "OpslWko", aofb,
                              fnum(k.get("OpslWko")), round(aofb * R26["Wko"], 2)))
        lnsv = fnum(k.get("LnSV"))
        if abs(lnsv - R26["max_maand"]) < 0.005 and lnlb > R26["max_maand"] + 0.01:
            cap_hits.append(pid)
        rows.append(row)
    n = len(ikvs)
    if reg_hits:
        o.find("High", "Wage tax", f"{len(reg_hits)} IKVs: loonheffing does "
               "not equal the monthly witte/groene tabel 2026 amount for the "
               "tabelloon, age column and loonheffingskorting status.",
               "; ".join(f"{r['PersNr']}/{r['NumIV']} tabelloon {r['tabelloon']:,.2f} "
                         f"declared {r['IngLbPh']:,.2f} table {r['exp_regular']:,.2f}"
                         for r in reg_hits[:20]),
               f"{sum(r['IngLbPh'] - r['exp_regular'] for r in reg_hits):,.2f}",
               "Witte/Groene Maandloon-tabel 2026 (uitgave januari 2026)", "D-02",
               len(reg_hits))
    else:
        o.check("D-02", "Wage tax", "Regular loonheffing equals the monthly table "
                "(IKVs without bb wage: IngLbPh; with bb wage: tested via D-03)",
                f"{n} IKVs", "Pass")
    if aok_rows:
        o.find("Observation", "Wage tax", f"{len(aok_rows)} AOW-age IKVs are taxed "
               "with the alleenstaandeouderenkorting column (incl. AOK). That column "
               "applies only to an employee entitled to the AOK (AOW for a single "
               "person); the pack does not evidence entitlement.",
               "; ".join(f"{r['PersNr']}/{r['NumIV']} tabelloon {r['tabelloon']:,.2f} "
                         f"declared {r['IngLbPh']:,.2f}" for r in aok_rows),
               "", "Witte Maandloon-tabel 2026, AOW columns; Handboek 2026 h.24",
               "D-12", len(aok_rows))
    if ak_hits:
        o.find("Medium", "Wage tax", f"{len(ak_hits)} IKVs: verrekende "
               "arbeidskorting differs from the monthly table column.",
               "; ".join(f"{r['PersNr']} declared {r['VerrArbKrt']} table {r['exp_ak']}"
                         for r in ak_hits[:20]), "",
               "Witte Maandloon-tabel 2026, column verrekende arbeidskorting",
               "D-08", len(ak_hits))
    else:
        o.check("D-08", "Wage tax", "Verrekende arbeidskorting equals the table "
                "column on every white-table IKV with loonheffingskorting",
                f"{n} IKVs", "Pass")
    if bt_bad:
        o.find("High", "Bijzondere beloningen", f"{len(bt_bad)} IKVs: the "
               "special-rate tax (IngLbPh minus the table amount on the tabelloon) "
               "is not any rate of the applicable bijzondere-beloning column.",
               "; ".join(f"{r['PersNr']}/{r['NumIV']} bb wage {r['LnTabBB']:,.2f} "
                         f"BT tax {r.get('bt_tax', r['IngLbPh']):,.2f} = "
                         f"{r.get('bt_rate')}%" for r in bt_bad[:20]), "",
               "Witte/Groene tabel bijzondere beloning 2026", "D-03", len(bt_bad))
    else:
        o.check("D-03", "Bijzondere beloningen", "Effective special rate of every "
                "IKV with a bb wage is a rate of the applicable table column "
                "(column membership; bracket derivation is D-11)",
                f"{sum(1 for r in rows if abs(r['LnTabBB']) > 0.005)} IKVs with bb wage",
                "Pass")
    if prem_hits:
        o.find("High", "Employer premiums", f"{len(prem_hits)} premium amounts "
               "do not recalculate from their own declared premium wage at the "
               "2026 rate.", "; ".join(f"{h[0]}/{h[1]} {h[2]} base {h[3]:,.2f} "
                                        f"declared {h[4]:,.2f} expected {h[5]:,.2f}"
                                        for h in prem_hits[:20]),
               f"{sum(h[4] - h[5] for h in prem_hits):,.2f}",
               "Handboek Loonheffingen 2026, Tabel 9", "E-01", len(prem_hits))
    else:
        o.check("E-01", "Employer premiums", "Aof laag/hoog, AWf laag/hoog and "
                "Opslag Wko recalculate from their declared premium wage at the "
                "2026 rates (6,27/7,63/2,74/7,74/0,50%)", f"{n} IKVs", "Pass")
    if cap_hits:
        o.find("High", "Wage basis", f"{len(cap_hits)} IKVs declare Loon SV at "
               "exactly the monthly maximum while Loon LB/PH exceeds it.",
               "; ".join(cap_hits[:25]), "", "Gegevensspecificaties 2026, Loon SV",
               "C-01", len(cap_hits))
    else:
        o.check("C-01", "Wage basis", "Loon SV is not capped at the monthly maximum "
                "premieloon (cap applied in the aanwas fields)", f"{n} IKVs", "Pass")
    whk = [(k.get("PersNr"), fnum(k.get("PrGediffWhk")) / fnum(k.get("PrlnWhkAnw")))
           for k in ikvs if fnum(k.get("PrlnWhkAnw")) > 0]
    zero_whk = [k.get("PersNr") for k in ikvs
                if fnum(k.get("PrlnWhkAnw")) > 0 and fnum(k.get("PrGediffWhk")) == 0]
    if whk:
        modal = collections.Counter(round(x[1], 4) for x in whk).most_common(1)[0][0]
        off = [x for x in whk if abs(round(x[1], 4) - modal) > 0.0001]
        o.notes.append(f"Whk implied rate {modal * 100:.2f}% on {len(whk)} IKVs "
                       f"(beschikking not in the pack; rate inferred).")
        if off or zero_whk:
            o.find("Medium", "Employer premiums", f"Whk premium inconsistent with the "
                   f"rate on the other IKVs ({modal * 100:.2f}%) or nil against a "
                   f"non-zero base on {len(off) + len(zero_whk)} IKVs.",
                   "; ".join(f"{p} {r * 100:.3f}%" for p, r in off[:20]) +
                   ("; nil: " + "; ".join(zero_whk) if zero_whk else ""), "",
                   "Art. 20 Wfsv; no L-code exists for Whk", "E-03 / E-04",
                   len(off) + len(zero_whk))
        else:
            o.check("E-03 / E-04", "Employer premiums", f"Whk premium present and "
                    f"at one consistent rate ({modal * 100:.2f}%, inferred - "
                    f"beschikking not supplied) on every IKV with a Whk base",
                    f"{len(whk)} IKVs", "Pass")
    return o, ret, rows, C, base, X


if __name__ == "__main__":
    o, *_ = run(sys.argv[1])
    for c in o.checks:
        print(c["id"], c["result"], c["check"][:110])
    for r in o.recon:
        print("REC", r)
    for nte in o.notes:
        print("NOTE", nte)
