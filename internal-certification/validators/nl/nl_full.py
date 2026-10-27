"""Netherlands - full validation pass: tests the items left 'Not tested' on 14-10-2026 that can be tested with
the documents in the pack. Usage: python -I nl_full.py quest|excerpta|sherwin
Writes 02 Validation/_evidence/full_checks.json (same shape as checks.json)."""
import glob
import os
import re
import sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
TOOL = os.path.join(HERE, "..", "..", "Netherlands", "_tool")
sys.path.insert(0, os.path.join(HERE, "..", "common"))
sys.path.insert(0, TOOL)
sys.stdout.reconfigure(encoding="utf-8")

import pdfplumber  # noqa: E402

import nl_check as NC  # noqa: E402
from clients import CLIENTS, NL  # noqa: E402
from framework import Evidence, eq  # noqa: E402

key = sys.argv[1]
C = CLIENTS[key]
VAL = os.path.join(NL, C["folder"], "02 Validation")
X = os.path.join(VAL, "_extracted")


def fx(name):
    r = glob.glob(os.path.join(X, "**", name), recursive=True)
    return r[0]


AMT = re.compile(r"^-?[\d.,]+[.,]\d{2}$")


def to_num(s, eu):
    s = s.strip()
    neg = s.startswith("-")
    s = s.lstrip("-")
    s = s.replace(".", "").replace(",", ".") if eu else s.replace(",", "")
    try:
        v = float(s)
    except ValueError:
        return None
    return -v if neg else v


# ------------------------------------------------------------ payslip reader --
HDR = {  # label (Dutch / English) -> key
    "Schriftelijk": "written", "Written": "written",
    "Oproep": "oncall", "On-call": "oncall",
    "Contract": "contract",
    "LH/LHKorting": "lh", "Tax/Tax": "lh",
    "ZVW/WW/WIA": "zvw",
    "Verloonde": "uren", "Hours worked": "uren",
    "Kleur/Tabe": "tabel", "Color/Table": "tabel",
    "Jaarloon": "jaarloon_bt", "Annual": "jaarloon_bt",
    "Tarief": "tarief_bt", "Special rate": "tarief_bt",
    "Geboortedatum": "dob", "Date of birth": "dob",
}


def read_slips(path):
    """Mercans NL payslip (Dutch or English). Header: label column + value column 55-60 pt to the right;
    lines: Code | Payment | Deduction | Table | BT | SVW | Cumulative, boundaries from the column-title row."""
    out = defaultdict(list)
    with pdfplumber.open(path) as pdf:
        for pno, page in enumerate(pdf.pages, 1):
            words = page.extract_words()
            if not words:
                continue
            lines = defaultdict(list)
            for w in words:
                lines[round(w["top"])].append(w)
            tops = sorted(lines)
            txt = {t: " ".join(w["text"] for w in sorted(lines[t], key=lambda w: w["x0"])) for t in tops}
            eu = any("Employee ID" in s for s in txt.values())
            pid = None
            for t in tops:
                m = re.search(r"(?:Pers\. nr\.|Employee ID)\s+(\S+)", txt[t])
                if m:
                    pid = m.group(1)
            if not pid:
                continue
            rec = {"page": pno, "hdr": {}, "lines": [], "eu": eu}
            mper = next((re.match(r"^Periode?\s+(\d+)\s+20\d\d$", txt[t].strip()) for t in tops
                         if re.match(r"^Periode?\s+\d+\s+20\d\d$", txt[t].strip())), None)
            rec["periode"] = mper.group(1) if mper else None
            # header values: for every label word, value = words between label x+55 and next label x
            label_x = sorted({w["x0"] for t in tops for w in lines[t] if any(w["text"].startswith(k.split()[0])
                                                                           for k in HDR)})
            for t in tops:
                ws = sorted(lines[t], key=lambda w: w["x0"])
                s = txt[t]
                for lab, k in HDR.items():
                    first = lab.split()[0]
                    for i, w in enumerate(ws):
                        if w["text"] == first and (len(lab.split()) == 1 or " ".join(x["text"] for x in ws[i:i + len(lab.split())]) == lab):
                            vx0 = w["x0"] + (55 if eu else 60)
                            vals = [x["text"] for x in ws if vx0 - 3 <= x["x0"] < vx0 + 48]
                            if vals and k not in rec["hdr"]:
                                rec["hdr"][k] = " ".join(vals)
            # line items
            th = next((t for t in tops if txt[t].startswith("Code")), None)
            if th is None:
                continue
            cols = {w["text"]: w["x0"] for w in lines[th]}
            names = ["Betaling", "Inhouding", "Tabel", "BT", "SVW", "Cumulatief"] if not eu else \
                ["Payment", "Deduction", "Table", "BT", "SVW", "Cumulative"]
            xs = [cols[n] for n in names]
            for t in tops:
                if t <= th:
                    continue
                ws = sorted(lines[t], key=lambda w: w["x0"])
                if not ws or not re.match(r"^\d{4,5}$", ws[0]["text"]):
                    continue
                code = ws[0]["text"]
                desc = " ".join(w["text"] for w in ws[1:] if not AMT.match(w["text"]) and w["x0"] < xs[0] - 40)
                amts = [(w["x0"] + w["x1"]) / 2 for w in ws if AMT.match(w["text"])]
                vals = {n: None for n in names}
                for w in ws:
                    if not AMT.match(w["text"]):
                        continue
                    xr = w["x1"]
                    # right-aligned numbers: assign to the column whose title starts closest before the number end
                    best = None
                    for n, x in zip(names, xs):
                        if x - 25 <= xr <= x + 60:
                            if best is None or abs(xr - (x + 35)) < abs(xr - (xs[names.index(best)] + 35)):
                                best = n
                    if best:
                        vals[best] = to_num(w["text"], eu)
                rec["lines"].append({"code": code, "desc": desc, **{k: vals[n] for k, n in
                                                                    zip(["pay", "ded", "tab", "bt", "svw", "cum"], names)}})
            out[pid].append(rec)
    return out


# ------------------------------------------------------------ return ---------
ret = NC.parse_return(fx(C["xml"]))
ikvs = ret["period"]["ikvs"] if "ikvs" in ret["period"] else None
ev = Evidence(f"{C['name']} - Netherlands full validation pass (September 2026)")


def jn(v):
    v = (v or "").strip().lower()
    return {"ja": "J", "yes": "J", "nee": "N", "no": "N", "j": "J", "n": "N"}.get(v, v.upper())


IK = {}
for ik in ikvs:
    IK.setdefault(str(ik.get("PersNr")).lstrip("0"), []).append(ik)
slips_all = read_slips(fx(C["payslips"]))
slips = {k: [r for r in v if r.get("periode") in (None, "09")] or v for k, v in slips_all.items()}
S = {k.lstrip("0").lstrip("M"): v for k, v in slips.items()}
if key == "excerpta":
    S = {k.lstrip("0"): v for k, v in slips.items()}
    IK = {}
    for ik in ikvs:
        IK.setdefault(str(ik.get("PersNr")), []).append(ik)

# ================= H. payslip header fields vs return =================
pairs = [("written", "IP_IndSchriftArbov"), ("oncall", "IP_IndOprov"), ("lh", "IP_IndLhKort")]
res = defaultdict(list)
tested = 0
for pid, recs in S.items():
    iks = IK.get(pid) or IK.get(pid.lstrip("M")) or []
    if not iks:
        res["no IKV"].append(pid)
        continue
    h = recs[0]["hdr"]
    emp = [i for i in iks if str(i.get("IP_SrtIV")) not in ("62", "18", "31")]   # employment IKV, not after-payments
    ik = emp[-1] if emp else iks[-1]
    tested += 1
    for hk, rk in pairs:
        v = h.get(hk)
        if hk == "lh" and v:
            v = v.split("/")[-1]
        if v is None:
            res[f"{hk} unreadable"].append(pid)
        elif jn(v) != (ik.get(rk) or ""):
            res[f"{hk}: slip {v} / return {ik.get(rk)}"].append(pid)
    z = h.get("zvw")
    if z:
        parts = [p.strip() for p in z.split("/")]
        exp = [ik.get("IP_CdZvw"), ik.get("IP_IndWW"), ik.get("IP_IndWAO")]
        got = [parts[0].upper()] + [jn(p) for p in parts[1:3]]
        if got != exp:
            res[f"ZVW/WW/WIA slip {z} / return {'/'.join(map(str, exp))}"].append(pid)
    else:
        res["zvw unreadable"].append(pid)
    c = h.get("contract", "")
    onb = "J" if ("onbepaald" in c.lower() or "indefinite" in c.lower()) else ("N" if c else None)
    if onb and onb != ik.get("IP_IndArbovOnbepTd"):
        res[f"contract slip {c} / return {ik.get('IP_IndArbovOnbepTd')}"].append(pid)
summ = "; ".join(f"{k}: {len(v)} ({', '.join(v[:6])}{'...' if len(v) > 6 else ''})" for k, v in res.items())
ev.check("H-11", "Payslip header", "Written contract, on-call, indefinite contract, loonheffingskorting and ZVW/WW/WIA "
         "on the payslip = the return indicators (IndSchriftArbov, IndOprov, IndArbovOnbepTd, IndLhKort, CdZvw/IndWW/IndWAO)",
         f"{tested} employees with payslip + IKV", not res, summ)
ev.d["exceptions"] += [{"id": "H-11", "key": k, "msg": ", ".join(v)} for k, v in res.items()]

# verloonde uren slip vs return (Excerpta was Not tested)
bad = []
for pid, recs in S.items():
    iks = IK.get(pid) or []
    u = recs[0]["hdr"].get("uren")
    if not iks or not u:
        continue
    uv = to_num(u.split()[0], recs[0]["eu"])
    ru = sum(float(i.get("IP_AantVerlU") or i.get("AantVerlU") or 0) for i in iks)
    if uv is not None and abs(uv - ru) > 1:
        bad.append(f"{pid} slip {uv} / return {ru}")
ev.check("H-12", "Payslip header", "Hours on the payslip (verloonde uren / hours worked) = AantVerlU in the return (tolerance 1 h)",
         f"{len(S)} payslips", not bad, f"{len(bad)} differ: " + "; ".join(bad[:15]))

# ================= G-S5. wage-type base composition from payslip columns =================
mat = defaultdict(lambda: defaultdict(int))
desc = {}
recon_bad = []
SA = {k.lstrip("0").lstrip("M") if key != "excerpta" else k.lstrip("0"): v for k, v in slips_all.items()}
for pid, recs in SA.items():
    for r in recs:
        for l in r["lines"]:
            amt = l["pay"] if l["pay"] is not None else (-l["ded"] if l["ded"] is not None else None)
            if amt is None:   # notional line (e.g. car addition): only fiscal columns filled
                amt = next((v for v in (l["tab"], l["bt"], l["svw"]) if v is not None), None)
            if amt is None or abs(amt) < 0.005:
                continue

            def sgn(v):
                if v is None:
                    return 0
                return 1 if eq(v, amt, 0.011) else (-1 if eq(v, -amt, 0.011) else 9)
            k = (sgn(l["tab"]), sgn(l["bt"]), sgn(l["svw"]))
            mat[l["code"]][k] += 1
            desc.setdefault(l["code"], l["desc"])
rows = []
for code in sorted(mat):
    combos = dict(mat[code])
    dominant = max(combos, key=combos.get)
    rows.append({"Code": code, "Description": desc[code], "Table (LB tabelloon)": dominant[0], "BT (bijzonder tarief)": dominant[1],
                 "SVW (SV-loon)": dominant[2], "Occurrences": sum(combos.values()),
                 "Consistent": "Yes" if len(combos) == 1 else f"No {combos}"})
ev.d["wage_types"] = rows
incons = [r for r in rows if r["Consistent"] != "Yes"]
ev.check("G-S5a", "Base composition", "Each pay element has one fiscal treatment (Table/BT/SVW) across all employees",
         f"{len(rows)} pay elements", not incons, "; ".join(f"{r['Code']} {r['Description']}: {r['Consistent']}" for r in incons))

# per-employee: slip column totals = return LnLbPh / LnTabBB / LnSV
bad = []
for pid, recs in S.items():
    iks = IK.get(pid) or []
    if not iks:
        continue
    tab = sum(l["tab"] or 0 for r in recs for l in r["lines"])
    bt = sum(l["bt"] or 0 for r in recs for l in r["lines"])
    svw = sum(l["svw"] or 0 for r in recs for l in r["lines"])
    lb = sum(float(i.get("LnLbPh") or 0) for i in iks)
    bb = sum(float(i.get("LnTabBB") or 0) for i in iks)
    sv = sum(float(i.get("LnSV") or 0) for i in iks)
    if not (eq(tab + bt, lb, 0.05) and eq(bt, bb, 0.05) and eq(svw, sv, 0.05)):
        bad.append(f"{pid} slip T+BT {tab + bt:.2f}/BT {bt:.2f}/SVW {svw:.2f} vs return LnLbPh {lb:.2f}/LnTabBB {bb:.2f}/LnSV {sv:.2f}")
ev.check("G-S5b", "Base composition", "Per employee: sum of payslip Table+BT = LnLbPh, BT = LnTabBB, SVW = LnSV",
         f"{len(S)} employees", not bad, f"{len(bad)}: " + "; ".join(bad[:12]))

# ================= D-12. Alleenstaandeouderenkorting =================
aow_rows = [r for r in ev.d.get("ikv_rows", [])] if False else []
ev.save_name = "full_checks.json"
import json  # noqa: E402
ev.d["slip_headers"] = {pid: recs[0]["hdr"] for pid, recs in S.items()}
os.makedirs(os.path.join(VAL, "_evidence"), exist_ok=True)
with open(os.path.join(VAL, "_evidence", "full_checks.json"), "w", encoding="utf-8") as f:
    json.dump(ev.d, f, ensure_ascii=False, indent=1, default=str)
for c in ev.d["checks"]:
    print(c["id"], c["result"], "|", c["check"][:90], "|", c["detail"][:700])
print("wage types:", len(rows))
for r in rows:
    print("  ", r)
