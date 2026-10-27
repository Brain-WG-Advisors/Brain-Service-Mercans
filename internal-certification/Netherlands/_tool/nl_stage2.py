"""Stage 2: tie the return to the G2N, payslips, payments, GL and master data."""
import collections
import datetime as dt
import re

import g2n as G
from nl_check import (R26, fnum, payslip_pages, amounts_on, header_field,
                      bb_rate_for_jaarloon, parse_sepa)

YN = {"J": "Ja", "N": "Nee"}


def gval(df, codes):
    import pandas as pd
    tot = pd.Series(0.0, index=df.index)
    for c in codes:
        cc = G.col(df, c)
        if cc is not None:
            tot = tot + pd.to_numeric(df[cc], errors="coerce").fillna(0.0)
    return tot


def to_iso(d):
    d = str(d).strip()[:10]
    if re.match(r"\d\d-\d\d-\d{4}", d):
        return dt.datetime.strptime(d, "%d-%m-%Y").date().isoformat()
    return d


def _d(x):
    return to_iso(x) if x else None


def slip_header(pg, tpl):
    """Header fields of one payslip, normalised to the return's codes."""
    h = {}
    yn = {"ja": "J", "nee": "N", "yes": "J", "no": "N"}
    m = re.search(r"ZVW/WW/WIA\s+(\w)/(\w+)/(\w+)", pg)
    if m:
        h["ZVW/WW/WIA"] = f"{m.group(1)}/{yn.get(m.group(2).lower())}/{yn.get(m.group(3).lower())}"
    if tpl == "nl":
        m = re.search(r"LH/LHKorting\s+(\w+)/(\w+)", pg)
        if m:
            h["loonheffingskorting"] = yn.get(m.group(2).lower())
        m = re.search(r"Geboortedatum\s+(\d\d-\d\d-\d{4})", pg)
        if m:
            h["date of birth"] = _d(m.group(1))
        m = re.search(r"In dienst\s+(\d\d-\d\d-\d{4})", pg)
        if m:
            h["start date"] = _d(m.group(1))
        m = re.search(r"Contract\s+(onbepaalde|bepaalde)", pg)
        if m:
            h["contract (indefinite)"] = "J" if m.group(1) == "onbepaalde" else "N"
        m = re.search(r"Schriftelijk\s+(Ja|Nee)", pg)
        if m:
            h["written contract"] = yn[m.group(1).lower()]
        m = re.search(r"Oproep\s+(Ja|Nee)", pg)
        if m:
            h["on-call"] = yn[m.group(1).lower()]
        m = re.search(r"Verloonde uren\s+([\d.,]+)", pg)
        if m:
            h["verloonde uren"] = fnum(m.group(1))
        m = re.search(r"Tarief BT\s+([\d.,]+)\s*%", pg)
        if m:
            h["tarief_bt"] = fnum(m.group(1))
        m = re.search(r"Jaarloon BT\s+([\d.,]+)", pg)
        if m:
            h["jaarloon_bt"] = fnum(m.group(1))
    else:   # English template: layout text interleaves label and value columns
        from nl_check import eu
        m = re.search(r"Tax/Tax Disc\.\s+(\w+)/(\w+)", pg)
        if m:
            h["loonheffingskorting"] = yn.get(m.group(2).lower())
        m = re.search(r"Employee ID\s+(\d\d-\d\d-\d{4})", pg)   # DOB printed beside it
        if m:
            h["date of birth"] = _d(m.group(1))
        m = re.search(r"Start date\s+(\d\d-\d\d-\d{4})", pg)
        if m:
            h["start date"] = _d(m.group(1))
        m = re.search(r"Contract\s+(indefinite|fixed\S*|definite)", pg, re.I)
        if m:
            h["contract (indefinite)"] = "J" if m.group(1).lower() == "indefinite" else "N"
        lines = pg.splitlines()
        for i, ln in enumerate(lines):
            m = re.search(r"Annual salary\s+([\d,]+)%", ln)
            if m and i:
                prev = re.findall(r"\d{1,3}(?:\.\d{3})*,\d{2}", lines[i - 1])
                if prev:
                    h["jaarloon_bt"] = eu(prev[-1])
                h["tarief_bt"] = eu(m.group(1))
    return h


def stage2(o, ret, rows, C, base, X):
    import pandas as pd
    P = ret["period"]
    ikvs = P["ikvs"]
    idmap = C.get("idmap", lambda x: x)
    xml_by = collections.defaultdict(list)
    for k in ikvs:
        xml_by[idmap(k.get("PersNr"))].append(k)
    rows_by = collections.defaultdict(list)
    for r in rows:
        rows_by[idmap(r["PersNr"])].append(r)
    ev = {"per_employee": collections.defaultdict(dict)}

    # ---------------- G2N ------------------------------------------------
    df, meta = G.load(X(C["g2n"]))
    df = df.set_index("_id", drop=False)
    gids, xids = set(df.index), set(xml_by)
    hc = (meta.get("Total headcount") or meta.get("Total Headcount")
          or meta.get("Report Headcount"))
    o.notes.append(f"G2N {C['g2n']}: {len(df)} employee rows "
                   f"({'two-row' if meta.get('_two_row_header') else 'one-row'} "
                   f"header); headcount printed in the header: {hc}.")
    num = lambda col: pd.to_numeric(df[col], errors="coerce").fillna(0.0)  # noqa
    tax = gval(df, C["tax"])
    er = {k: gval(df, v) for k, v in C["er"].items()}
    gross, ded, net = num(C["gross"]), num(C["deductions"]), num(C["net"])
    ev["g2n_net_total"] = float(net.sum())

    only_x, only_g = sorted(xids - gids), sorted(gids - xids)
    if only_x or only_g:
        o.find("High", "Population", f"Employees in the return and the G2N do "
               f"not match: {len(only_x)} only in the return, {len(only_g)} only in "
               f"the G2N.", f"only return: {only_x[:20]}; only G2N: {only_g[:20]}",
               "", "Cross-document reconciliation", "X-20",
               len(only_x) + len(only_g))
    else:
        o.check("X-20", "Population", "Every employee in the return has a G2N row "
                "and vice versa", f"{len(xids)} employees", "Pass")

    # G-S6 net identity; G-S9 employer total
    bijc = [str(c).split(" -")[0] for c in df.columns if str(c).startswith("658")]
    bij = gval(df, bijc)
    resid = gross - ded - net + gval(df, C.get("net_identity_add", [])) \
        - gval(df, C.get("net_identity_sub", []))
    bad = [(i, round(r, 2)) for i, r in resid.items()
           if abs(r) > 0.02 and abs(r - bij[i]) > 0.02]
    expl = [i for i, r in resid.items() if abs(r) > 0.02 and abs(r - bij[i]) <= 0.02]
    if bad:
        o.find("Medium", "Gross-to-net", f"{len(bad)} employees: {C['gross']} minus "
               f"{C['deductions']} does not equal {C['net']} (not explained by the "
               f"notional bijtelling).", "; ".join(f"{i} {r:,.2f}" for i, r in bad[:20]),
               f"{sum(r for _, r in bad):,.2f}", "Arithmetic", "G-S6", len(bad))
    else:
        o.check("G-S6", "Gross-to-net", f"{C['gross']} - {C['deductions']} = "
                f"{C['net']}" + (f"; {len(expl)} employees differ by exactly the "
                                 f"notional car bijtelling (taxed, not paid)"
                                 if expl else ""), f"{len(df)} employees", "Pass")
    if C.get("er_total"):
        built = gval(df, C["er_all"])
        d = num(C["er_total"]) - built
        badr = [(i, round(v, 2)) for i, v in d.items() if abs(v) > 0.02]
        if badr:
            o.find("Medium", "Gross-to-net", f"{len(badr)} employees: "
                   f"'{C['er_total']}' does not equal the sum of the employer "
                   f"columns.", "; ".join(f"{i} {v:,.2f}" for i, v in badr[:20]), "",
                   "Arithmetic", "G-S9", len(badr))
        else:
            o.check("G-S9", "Gross-to-net", f"'{C['er_total']}' foots to the "
                    f"employer columns", f"{len(df)} employees", "Pass")

    # X-02 return <-> G2N per employee
    for xk, label, gser, codes in (("IngLbPh", "loonheffing", tax, C["tax"]),
                                   *[(k, k, v, C["er"][k]) for k, v in er.items()]):
        hits = []
        for pid in sorted(xids & gids):
            xv = round(sum(fnum(k.get(f)) for k in xml_by[pid] for f in xk.split("+")), 2)
            gv = round(float(gser[pid]), 2)
            if abs(xv - gv) > 0.02:
                hits.append((pid, xv, gv))
        if hits:
            o.find("High", "Return to G2N", f"{len(hits)} employees: return "
                   f"{label} differs from the G2N ({'+'.join(codes)}).",
                   "; ".join(f"{h[0]} XML {h[1]:,.2f} G2N {h[2]:,.2f}" for h in hits[:20]),
                   f"{sum(h[1] - h[2] for h in hits):,.2f}",
                   "Cross-document reconciliation", "X-02", len(hits))
        else:
            o.check("X-02", "Return to G2N", f"Return {label} = G2N "
                    f"{'+'.join(codes)} per employee", f"{len(xids & gids)} employees",
                    "Pass")
        o.rec(label, f"Return {xk} (sum of IKVs)",
              sum(fnum(k.get(f)) for k in ikvs for f in xk.split("+")),
              f"G2N {'+'.join(codes)}",
              float(gser.sum()))
    o.rec("Net pay", "G2N total", float(net.sum()), "G2N employee rows",
          float(net.sum()))
    o.recon.pop()

    # E-08 Zvw against the capped premium wage (Zvw and SV maxima equal)
    zv = []
    for k in ikvs:
        b = fnum(k.get("PrlnWhkAnw"))
        z = fnum(k.get("WghZvw"))
        if (b > 0 or z > 0) and abs(round(b * R26["WghZvw"], 2) - z) > 0.02:
            zv.append((k.get("PersNr"), k.get("NumIV"), b, z, round(b * R26["WghZvw"], 2)))
    if zv:
        o.find("Observation", "Employer premiums", f"{len(zv)} IKVs: werkgeversheffing "
               "Zvw is not 6,10% of the capped premium wage declared for Whk. The Zvw "
               "bijdrageloon can differ from the SV wage and both are capped "
               "cumulatively (VCR), so each case needs the year-to-date to settle.",
               "; ".join(f"{h[0]}/{h[1]} base {h[2]:,.2f} Zvw {h[3]:,.2f} at 6,10% "
                         f"{h[4]:,.2f}" for h in zv[:20]),
               f"{sum(h[3] - h[4] for h in zv):,.2f}", "Handboek 2026 h.8; Tabel 11-12",
               "E-08", len(zv))
    else:
        o.check("E-08", "Employer premiums", "Werkgeversheffing Zvw = 6,10% of the "
                "capped premium wage on every IKV", f"{len(ikvs)} IKVs", "Pass")

    # ---------------- payslips -------------------------------------------
    tpl = C.get("slip_template", "nl")
    fmt = "eu" if tpl == "en" else "us"
    pages = {idmap(k): v for k, v in payslip_pages(
        X(C["payslips"]), C.get("slip_id_re", r"Pers\. nr\.\s+(\S+)")).items()}
    pids = set(pages)
    o.notes.append(f"Payslips {C['payslips']}: {sum(len(v) for v in pages.values())} "
                   f"pages for {len(pids)} employees (template '{tpl}').")
    miss = sorted(xids - pids)
    if miss:
        o.find("High", "Payslips", f"{len(miss)} employees in the return have no "
               "payslip in the pack.", "; ".join(miss[:25]), "", "Art. 7:626 BW",
               "J-06", len(miss))
    else:
        o.check("J-06", "Payslips", "Every employee in the return has a payslip",
                f"{len(xids)} employees", "Pass")
    if pids - xids:
        o.notes.append(f"Payslips for employees not in the return: "
                       f"{sorted(pids - xids)[:20]}")
    hdr_bad, amt_bad = collections.defaultdict(list), collections.defaultdict(list)
    parsed = collections.Counter()
    for pid in sorted(xids & pids):
        pg = "\n".join(pages[pid])
        vals = amounts_on(pg, fmt)
        ks = xml_by[pid]
        k0 = ([k for k in ks if k.get("IP_SrtIV") in ("15", "11", "13")] or ks)[0]
        rr = rows_by[pid]
        e = ev["per_employee"][pid]
        want = {"net pay": round(float(net.get(pid, 0)), 2)}
        for r in rr:
            if r["LbTab"][2:3] == "2" and r.get("tabelloon"):
                want["tabelloon " + r["NumIV"]] = r["tabelloon"]
                want["table tax " + r["NumIV"]] = round(r["IngLbPh"] - r.get("bt_tax", 0), 2)
            if abs(r["LnTabBB"]) > 0.005:
                want["bb wage " + r["NumIV"]] = round(r["LnTabBB"], 2)
                want["bb tax " + r["NumIV"]] = round(r.get("bt_tax", r["IngLbPh"]), 2)
        for lab, v in want.items():
            if abs(v) > 0.005 and v not in vals:
                amt_bad[lab.rsplit(" ", 1)[0] if lab[-1].isdigit() else lab].append(
                    f"{pid} {lab} {v:,.2f}")
        h = slip_header(pg, tpl)
        e["slip_header"] = h
        xv = {"loonheffingskorting": k0.get("IP_IndLhKort"),
              "ZVW/WW/WIA": "/".join(str(k0.get(t)) for t in ("IP_CdZvw", "IP_IndWW", "IP_IndWAO")),
              "date of birth": k0.get("NP_Gebdat"), "start date": k0.get("DatAanv"),
              "contract (indefinite)": k0.get("IP_IndArbovOnbepTd"),
              "written contract": k0.get("IP_IndSchriftArbov"),
              "on-call": k0.get("IP_IndOprov"),
              "verloonde uren": sum(fnum(k.get("IP_AantVerlU", k.get("AantVerlU"))) for k in ks)}
        for lab, x in xv.items():
            sv = h.get(lab)
            if sv is None:
                continue
            parsed[lab] += 1
            same = abs(sv - x) <= 0.5 if lab == "verloonde uren" else sv == x
            if not same:
                hdr_bad[lab].append(f"{pid} slip {sv} XML {x}")
        btr = [r.get("bt_rate") for r in rr if abs(r["LnTabBB"]) > 0.005 and r["LbTab"][2:3] == "2"]
        tb, jl = h.get("tarief_bt"), h.get("jaarloon_bt")
        if btr and tb is not None:
            parsed["Tarief BT printed vs rate applied"] += 1
            if abs(btr[0] - tb) > 0.02:
                hdr_bad["Tarief BT printed vs rate applied"].append(
                    f"{pid} slip {tb}% applied {btr[0]}%")
        if btr and jl is not None:
            parsed["BT rate vs Jaarloon BT bracket"] += 1
            aowk = any(r.get("AOW") for r in rr)
            pre = (k0.get("NP_Gebdat") or "9")[:4] <= "1945"
            exp = bb_rate_for_jaarloon("wit", k0.get("IP_IndLhKort") == "J", jl, aowk, pre)
            if aowk and abs(exp - btr[0]) > 0.02:
                exp = bb_rate_for_jaarloon("wit", True, jl, aowk, pre, aok=True) \
                    if k0.get("IP_IndLhKort") == "J" else exp
            e["bt_rate_from_jaarloon"] = exp
            if abs(exp - btr[0]) > 0.02:
                hdr_bad["BT rate vs Jaarloon BT bracket"].append(
                    f"{pid} Jaarloon BT {jl:,.2f} -> table {exp}%; applied {btr[0]}%")
    ev["slip_parsed"] = dict(parsed)
    for lab, lst in amt_bad.items():
        o.find("Medium", "Payslips", f"{len(lst)} employees: the {lab} of the "
               f"return/G2N is not printed on the payslip.", "; ".join(lst[:20]), "",
               "Art. 7:626 BW", "L-04", len(lst))
    for lab in ("net pay", "tabelloon", "table tax", "bb wage", "bb tax"):
        if lab not in amt_bad:
            o.check("L-04", "Payslips", f"Payslip prints the {lab} of the return/G2N",
                    f"{len(xids & pids)} employees", "Pass")
    sev = {"BT rate vs Jaarloon BT bracket": "High"}
    for lab, lst in hdr_bad.items():
        o.find(sev.get(lab, "Medium"), "Payslip vs return", f"{len(lst)} employees: "
               f"{lab} on the payslip differs from the return.", "; ".join(lst[:20]),
               "", "Gegevensspecificaties 2026; Handboek 2026 §9.3.6 (BT)",
               "G-02 / H-01 / D-11", len(lst))
    for lab, n in parsed.items():
        if lab not in hdr_bad:
            o.check("G-02", "Payslip vs return", f"Payslip {lab} agrees with the return",
                    f"{n} employees (field read from the slip)", "Pass")
    for lab in ("loonheffingskorting", "ZVW/WW/WIA", "verloonde uren", "date of birth",
                "start date", "contract (indefinite)", "written contract", "on-call",
                "Tarief BT printed vs rate applied", "BT rate vs Jaarloon BT bracket"):
        if lab not in parsed:
            o.not_tested.append(dict(id="G-02", item=f"Payslip {lab} vs return",
                                     reason="Field could not be read reliably from "
                                            "this payslip template's text layer.",
                                     unblock="Manual reading of the PDF, or a payslip "
                                             "export in a structured format."))
    ev["df"], ev["net"], ev["pages"] = df, net, pages
    return ev


def stage3(o, ret, C, X, ev):
    """Payments, GL and master data."""
    import pandas as pd
    lh = ret["header"].get("LhNr")
    if C.get("receipt"):
        txt = open(X(C["receipt"]), encoding="utf-8", errors="replace").read()
        nums = sorted(set(re.findall(r"<nummer>([^<]+)</nummer>", txt)))
        codes = re.findall(r"<statuscode>(\d+)</statuscode>", txt)
        ts = sorted(re.findall(r"<tijdstempelStatus>([^<]+)</tijdstempelStatus>", txt))
        if nums and lh not in nums:
            o.find("High", "Authority receipt", f"The Digipoort status response in the "
                   f"pack belongs to loonheffingennummer {', '.join(nums)}, not to this "
                   f"return ({lh}). There is no evidence in the pack that this return "
                   f"was delivered or accepted, and the pack holds another payroll tax "
                   f"number's submission data.", f"{C['receipt']}: status codes "
                   f"{', '.join(sorted(set(codes)))}; timestamps {ts[0]} to {ts[-1]}",
                   "No acceptance evidence for this return", "Digipoort koppelvlak "
                   "(getStatussenProces); Gegevensspecificaties 2026", "A-10", 1)
        elif nums:
            o.check("A-10", "Authority receipt", f"Digipoort status response is for "
                    f"{lh}; final status codes {', '.join(sorted(set(codes)))}",
                    "1 response", "Pass")
    else:
        o.not_tested.append(dict(id="A-10", item="Authority acceptance of the return",
            reason="No Digipoort/Belastingdienst response in the pack. The 'Wage Tax "
                   "Overview' PDF is generated by HRBLIZZ, not by the authority.",
            unblock="Digipoort status response (getStatussenProces) or the "
                    "ontvangstbevestiging / foutenrapport for this return."))
    net = ev["net"]
    pos = float(net[net > 0].sum())
    # ---------------- SEPA ------------------------------------------------
    for i, f in enumerate(C["sepa"]):
        hdr, tx = parse_sepa(X(f))
        amts = [a.get("InstdAmt", "") for a in tx]
        badfmt = [a for a in amts if not re.fullmatch(r"\d+(\.\d{1,2})?", a)]
        e2e = collections.Counter(a.get("EndToEndId") for a in tx)
        dup = [k for k, v in e2e.items() if v > 1]
        total = round(sum(fnum(a) for a in amts), 2)
        okcnt = str(len(tx)) == hdr.get("NbOfTxs")
        okctl = abs(fnum(hdr.get("CtrlSum")) - total) <= 0.005
        ctl_fmt = re.fullmatch(r"\d+(\.\d{1,2})?", hdr.get("CtrlSum", "")) is not None
        role = C.get("sepa_roles", {}).get(f, "net pay")
        label = f"SEPA '{f}'"
        if badfmt or not ctl_fmt:
            o.find("High", "Payments", f"{label}: amounts are not valid ISO 20022 "
                   f"decimals ({len(badfmt)} InstdAmt{'' if ctl_fmt else ' and CtrlSum'} "
                   f"with a thousands separator, e.g. '{(badfmt or [hdr.get('CtrlSum')])[0]}').",
                   f"MsgId {hdr.get('MsgId')}", "File would be rejected by the bank",
                   "ISO 20022 pain.001.001.03 (ActiveOrHistoricCurrencyAndAmount: "
                   "decimal, '.' separator)", "K-01", len(badfmt) + (0 if ctl_fmt else 1))
        if dup:
            o.find("Medium", "Payments", f"{label}: EndToEndId repeated across "
                   f"{sum(e2e[d] for d in dup)} transactions.", f"{dup[:5]}", "",
                   "ISO 20022 / EPC SCT rulebook: EndToEndId identifies the transaction",
                   "K-01", sum(e2e[d] for d in dup))
        if okcnt and okctl:
            o.check("K-01 / K-02", "Payments", f"{label}: NbOfTxs and CtrlSum tie to "
                    f"the transactions", f"{len(tx)} transactions", "Pass")
        else:
            o.find("High", "Payments", f"{label}: header does not tie (NbOfTxs "
                   f"{hdr.get('NbOfTxs')} vs {len(tx)}; CtrlSum {hdr.get('CtrlSum')} vs "
                   f"{total:,.2f}).", "", "", "ISO 20022", "K-01 / K-02", 1)
        if role == "net pay":
            o.rec("Net pay", "G2N positive net pay", pos, label + " sum", total)
        elif role == "tax":
            coll = ret["period"]["coll"]
            o.rec("Loonheffingen payment", "Return TotGen", fnum(coll.get("TotGen")),
                  label + " sum", total)
        ev.setdefault("sepa", {})[f] = dict(hdr=hdr, tx=tx, total=total, role=role)
    return ev


def load_table(path, must=("Debit Amount",)):
    """Read a report past its metadata block: header = first row holding `must`."""
    import pandas as pd
    eng = "xlrd" if path.lower().endswith(".xls") else None
    raw = pd.read_excel(path, engine=eng, header=None)
    h = next(i for i in range(min(len(raw), 40))
             if all(any(str(v).strip() == m for v in raw.iloc[i]) for m in must))
    cols = [str(v).strip() for v in raw.iloc[h]]
    df = pd.DataFrame(raw.iloc[h + 1:].values, columns=cols)
    return df


def stage_gl(o, ret, C, X, ev):
    import pandas as pd
    g = C["gl_cols"]
    gl = load_table(X(C["gl"]), must=(g["debit"], g["credit"]))
    gl = gl[gl[g["emp"]].notna()].copy()
    gl[g["emp"]] = gl[g["emp"]].map(lambda v: re.sub(r"\.0$", "", str(v).strip()))
    gl = gl[gl[g["emp"]].str.match(r"^[A-Za-z]?\d+$")]
    dr = pd.to_numeric(gl[g["debit"]], errors="coerce").fillna(0.0)
    cr = pd.to_numeric(gl[g["credit"]], errors="coerce").fillna(0.0)
    o.notes.append(f"GL {C['gl']}: {len(gl)} lines, {gl[g['emp']].nunique()} employees.")
    ok = o.rec("GL balance", "GL debits", float(dr.sum()), "GL credits", float(cr.sum()))
    o.check("K-06", "Ledger", "GL debits equal credits", f"{len(gl)} lines",
            "Pass" if ok else "Finding")
    if not ok:
        o.find("Medium", "Ledger", "The GL does not balance.",
               f"debits {dr.sum():,.2f} credits {cr.sum():,.2f}",
               f"{dr.sum() - cr.sum():,.2f}", "Double entry", "K-06", 1)
    # net pay per employee
    el = gl[g["element"]].astype(str)
    is_net = el.str.contains(C["gl_net"], regex=True)
    netgl = (cr - dr)[is_net].groupby(gl[g["emp"]][is_net]).sum()
    net = ev["net"]
    diffs = [(i, round(float(net.get(i, 0)), 2), round(float(netgl.get(i, 0)), 2))
             for i in sorted(set(net.index) | set(netgl.index))
             if abs(float(net.get(i, 0)) - float(netgl.get(i, 0))) > 0.02]
    o.rec("Net pay", "G2N total", float(net.sum()), f"GL '{C['gl_net']}' lines",
          float(netgl.sum()))
    if diffs:
        o.find("Medium", "Ledger", f"{len(diffs)} employees: GL net pay differs from "
               "the G2N.", "; ".join(f"{d[0]} G2N {d[1]:,.2f} GL {d[2]:,.2f}" for d in diffs[:20]),
               f"{sum(d[1] - d[2] for d in diffs):,.2f}", "Cross-document", "K-07", len(diffs))
    else:
        o.check("K-07", "Ledger", "GL net pay equals the G2N per employee",
                f"{len(net)} employees", "Pass")
    # statutory liability lines (tax + employer premiums) vs the return
    if C.get("gl_statutory"):
        is_st = el.str.contains(C["gl_statutory"], regex=True)
        if C.get("gl_statutory_account"):
            ac, av = C["gl_statutory_account"]
            is_st = is_st & (gl[ac].astype(str).str.replace(r"\.0$", "", regex=True) == av)
        st = float((cr - dr)[is_st].sum())
        P = ret["period"]
        due = sum(fnum(k.get(f)) for k in P["ikvs"] for f in (
            "IngLbPh", "PrAofLg", "PrAofHg", "PrAofUit", "OpslWko", "PrGediffWhk",
            "PrAwfLg", "PrAwfHg", "PrAwfHz", "PrAwfUit", "PrUFO", "BijdrZvw", "WghZvw"))
        o.rec("Loonheffingen payable (period block)", "Return: tax + premiums, "
              "sum of IKVs", due, "GL tax/premium credit lines", st)
    # foreign-country element labels
    if C.get("gl_label_check"):
        lab = gl[C["gl_label_check"]].astype(str)
        alien = sorted({v for v in lab.unique()
                        if re.search(r"EOBI|EIS \(|Social Fund|SOCSO|EPF|PAYE|NSSF", v)})
        if alien:
            o.find("Low", "Ledger", f"{len(alien)} GL pay-element labels name schemes "
                   f"of other countries for Dutch premiums.", "; ".join(alien), "",
                   "Presentation", "K-07", len(alien))
    ev["gl"] = gl
    return ev


def stage_master(o, ret, C, X, ev):
    import pandas as pd
    if not C.get("master"):
        return
    m = load_table(X(C["master"]), must=(C["master_cols"]["id"],))
    mc = C["master_cols"]
    m = m[m[mc["id"]].notna()].copy()
    m["_id"] = m[mc["id"]].map(lambda v: re.sub(r"\.0$", "", str(v).strip()))
    m = m[m["_id"].str.match(r"^[A-Za-z]?\d+$")].drop_duplicates("_id").set_index("_id")
    idmap = C.get("idmap", lambda x: x)
    xml = {}
    for k in ret["period"]["ikvs"]:
        xml.setdefault(idmap(k.get("PersNr")), k)
    o.notes.append(f"Master data {C['master']}: {len(m)} employees.")
    miss = sorted(set(xml) - set(m.index))
    if miss:
        o.find("Observation", "Master data", f"{len(miss)} employees in the return are "
               f"not in the master-data extract supplied.", "; ".join(miss[:25]), "",
               "Extract completeness (not by itself a defect)", "M-04", len(miss))
    else:
        o.check("M-04", "Master data", "Every employee in the return is in the master "
                "extract", f"{len(xml)} employees", "Pass")
    for lab, col, tag in (("date of birth", mc.get("dob"), "NP_Gebdat"),
                          ("start date", mc.get("hire"), "DatAanv")):
        if not col or col not in m.columns:
            continue
        bad = []
        for pid in sorted(set(xml) & set(m.index)):
            v = m.at[pid, col]
            if str(v) in ("nan", "NaT", ""):
                continue
            mv = to_iso(pd.to_datetime(v, dayfirst=True).date().isoformat()) \
                if not re.match(r"\d{4}-\d\d-\d\d", str(v)) else str(v)[:10]
            if mv != xml[pid].get(tag):
                bad.append(f"{pid} master {mv} XML {xml[pid].get(tag)}")
        if bad:
            o.find("Medium", "Master data", f"{len(bad)} employees: {lab} in the master "
                   f"data differs from the return.", "; ".join(bad[:20]), "",
                   "Gegevensspecificaties 2026", "M-01", len(bad))
        else:
            o.check("M-01", "Master data", f"Master {lab} agrees with the return",
                    f"{len(set(xml) & set(m.index))} employees", "Pass")


def stage_payrep(o, ret, C, X, ev):
    """Payment report: per employee against the G2N; total against SEPA."""
    import pandas as pd
    if not C.get("payment_report"):
        return
    pc = C["payrep_cols"]
    pr = load_table(X(C["payment_report"]), must=(pc["emp"], pc["value"]))
    pr = pr[pr[pc["emp"]].notna()].copy()
    pr["_id"] = pr[pc["emp"]].map(lambda v: re.sub(r"\.0$", "", str(v).strip()))
    pr = pr[pr["_id"].str.match(r"^[A-Za-z]?\d+$")]
    val = pd.to_numeric(pr[pc["value"]], errors="coerce").fillna(0.0)
    per = val.groupby(pr["_id"]).sum()
    net = ev["net"]
    o.notes.append(f"Payment report {C['payment_report']}: {len(pr)} lines, "
                   f"{len(per)} employees, total {val.sum():,.2f}.")
    pos = net[net > 0]
    diffs = [(i, round(float(pos.get(i, 0)), 2), round(float(per.get(i, 0)), 2))
             for i in sorted(set(pos.index) | set(per.index))
             if abs(float(pos.get(i, 0)) - float(per.get(i, 0))) > 0.02]
    o.rec("Net pay", "G2N positive net pay", float(pos.sum()), "Payment report total",
          float(val.sum()))
    if diffs:
        o.find("Medium", "Payments", f"{len(diffs)} employees: payment report amount "
               "differs from G2N net pay.", "; ".join(f"{d[0]} G2N {d[1]:,.2f} report "
                                                      f"{d[2]:,.2f}" for d in diffs[:25]),
               f"{sum(d[1] - d[2] for d in diffs):,.2f}", "Cross-document", "K-05", len(diffs))
    else:
        o.check("K-05", "Payments", "Payment report equals G2N net pay per employee",
                f"{len(per)} employees", "Pass")
    # SEPA by IBAN against the payment report
    if pc.get("iban"):
        ib = dict(zip(pr[pc["iban"]].astype(str).str.replace(" ", ""), pr["_id"]))
        for f, sp in ev.get("sepa", {}).items():
            if sp["role"] != "net pay":
                continue
            unmatched, wrong = [], []
            for t in sp["tx"]:
                pid = ib.get((t.get("iban") or "").replace(" ", ""))
                if pid is None:
                    unmatched.append(f"{t.get('name')} {t.get('InstdAmt')}")
                elif abs(fnum(t.get("InstdAmt")) - float(per.get(pid, 0))) > 0.02:
                    wrong.append(f"{pid} SEPA {t.get('InstdAmt')} report {per.get(pid, 0):,.2f}")
            sepa_ib = {(t.get("iban") or "").replace(" ", "") for t in sp["tx"]}
            notpaid = sorted(pid for k, pid in ib.items()
                             if k not in sepa_ib and abs(float(per.get(pid, 0))) > 0.005)
            if unmatched or wrong or notpaid:
                o.find("Medium", "Payments", f"SEPA '{f}' vs payment report: "
                       f"{len(unmatched)} transfers to an IBAN not in the report, "
                       f"{len(wrong)} amount differences, {len(notpaid)} report lines "
                       f"with no transfer.", "; ".join((unmatched + wrong + notpaid)[:20]),
                       "", "Cross-document", "K-05", len(unmatched) + len(wrong) + len(notpaid))
            else:
                o.check("K-05", "Payments", f"Every SEPA transfer in '{f}' matches the "
                        f"payment report by IBAN and amount", f"{len(sp['tx'])} transfers",
                        "Pass")
