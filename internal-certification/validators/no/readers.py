"""Norway readers: A-melding XML, tilbakemelding JSON, a-ordningen summary (ods), G2N (xls, employees in
columns), payslips (pdfplumber word positions), pain.001 bank file, GL (detailed xlsx, finance xls, import csv),
master data (xlsx, employees in columns). Mapping per client lives in clients.py."""
import json
import re

import pandas as pd
import pdfplumber
from lxml import etree

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "common"))
from framework import num  # noqa: E402


def _ln(e):
    return etree.QName(e).localname


def _kids(e):
    return {_ln(c): c for c in e if isinstance(c.tag, str)}


def _txt(e, path):
    cur = e
    for p in path.split("/"):
        nxt = None
        for c in cur:
            if isinstance(c.tag, str) and _ln(c) == p:
                nxt = c
                break
        if nxt is None:
            return None
        cur = nxt
    return (cur.text or "").strip()


def _all(e, name):
    return [c for c in e if isinstance(c.tag, str) and _ln(c) == name]


def read_amelding(path):
    t = etree.parse(path)
    root = t.getroot()
    ns = etree.QName(root).namespace
    lev = _all(root, "Leveranse")[0]
    opp = _all(lev, "oppgave")[0]
    bet = _all(opp, "betalingsinformasjon")[0]
    out = {"namespace": ns, "meldingsId": _txt(lev, "meldingsId"),
           "kalendermaaned": _txt(lev, "kalendermaaned"),
           "leveringstidspunkt": _txt(lev, "leveringstidspunkt"),
           "kildesystem": _txt(lev, "kildesystem"),
           "opplysningspliktig": _txt(lev, "opplysningspliktig/norskIdentifikator"),
           "sumAGA": num(_txt(bet, "sumArbeidsgiveravgift")),
           "sumFinansskatt": num(_txt(bet, "sumFinansskattLoenn")),
           "sumUtleggstrekk": num(_txt(bet, "sumUtleggstrekk")),
           "trekk_per_dato": [(_txt(x, "loennsutbetalingsdato"), num(_txt(x, "beloep")))
                              for x in _all(bet, "sumForskuddstrekkPerLoennsutbetalingsdato")],
           "pensjonsinnretning": [_txt(p, "identifikator") for p in _all(opp, "pensjonsinnretning")],
           "virksomheter": []}
    for v in _all(opp, "virksomhet"):
        vd = {"orgnr": _txt(v, "norskIdentifikator"), "mottakere": [], "aga": []}
        for a in _all(v, "arbeidsgiveravgift"):
            for blk in a:
                if not isinstance(blk.tag, str):
                    continue
                vd["aga"].append({"type": _ln(blk),
                                  "kode": _txt(blk, "beregningskodeForArbeidsgiveravgift"),
                                  "sone": _txt(blk, "sone"),
                                  "grunnlag": num(_txt(blk, "avgiftsgrunnlagBeloep")),
                                  "sats": num(_txt(blk, "prosentsatsForAvgiftsberegning"))})
        for m in _all(v, "inntektsmottaker"):
            md = {"fnr": _txt(m, "norskIdentifikator"),
                  "navn": _txt(m, "identifiserendeInformasjon/navn"),
                  "foedselsdato": _txt(m, "identifiserendeInformasjon/foedselsdato"),
                  "ansattnummer": _txt(m, "identifiserendeInformasjon/ansattnummer"),
                  "arbeidsforhold": [], "trekk": [], "inntekt": []}
            for af in _all(m, "arbeidsforhold"):
                md["arbeidsforhold"].append({_ln(c): (c.text or "").strip() for c in af
                                             if isinstance(c.tag, str) and len(c) == 0})
            for fk in _all(m, "forskuddstrekk"):
                md["trekk"].append((_txt(fk, "beskrivelse"), num(_txt(fk, "beloep"))))
            for inn in _all(m, "inntekt"):
                d = {k: (_txt(inn, k)) for k in ("startdatoOpptjeningsperiode", "sluttdatoOpptjeningsperiode",
                                                  "fordel", "utloeserArbeidsgiveravgift",
                                                  "inngaarIGrunnlagForTrekk")}
                d["beloep"] = num(_txt(inn, "beloep"))
                typ = [c for c in inn if isinstance(c.tag, str) and _ln(c) in
                       ("loennsinntekt", "ytelseFraOffentlige", "pensjonEllerTrygd", "naeringsinntekt")]
                d["inntektstype"] = _ln(typ[0]) if typ else None
                d["beskrivelse"] = _txt(typ[0], "beskrivelse") if typ else None
                d["listeprisForBil"] = num(_txt(typ[0], "tilleggsinformasjon/bilOgBaat/listeprisForBil")) if typ else None
                d["bilregnr"] = _txt(typ[0], "tilleggsinformasjon/bilOgBaat/bilregistreringsnummer") if typ else None
                d["antall"] = num(_txt(typ[0], "antall")) if typ else None
                md["inntekt"].append(d)
            vd["mottakere"].append(md)
        out["virksomheter"].append(vd)
    return out


def read_receipt(path):
    j = json.load(open(path, encoding="utf-8"))
    m = j["mottak"][0]
    lev = m["mottattLeveranse"][0]
    tot = lev["mottattAvgiftOgTrekkTotalt"]
    return {"kalendermaaned": m["kalendermaaned"], "meldingsId": lev["meldingsId"],
            "ettermottak": m.get("tilbakemeldingEtterMottakAvMeldingsId"),
            "opplysningspliktig": m["opplysningspliktig"]["norskIdentifikator"],
            "altinnReferanse": lev["altinnReferanse"], "status": lev["mottakstatus"],
            "leveringstidspunkt": lev["leveringstidspunkt"], "antall": lev["antallInntektsmottakere"],
            "sumAGA": tot["sumArbeidsgiveravgift"], "sumFinansskatt": tot["sumFinansskattLoenn"],
            "trekk": [(x["loennsutbetalingsdato"], x["beloep"]) for x in tot["sumForskuddstrekkPerLoennsutbetalingsdato"]],
            "avvik": lev.get("avvik", []) + m["mottattPeriode"].get("avvik", []),
            "kid": m.get("innbetalingsinformasjon", {})}


def read_summary_ods(path):
    sh = pd.read_excel(path, sheet_name=None, header=None, dtype=object, engine="odf")
    sub = sh["Submission information"].dropna(how="all")
    hdr = [str(x).strip() for x in sub.iloc[0].tolist()]
    val = [("" if pd.isna(x) else str(x).strip()) for x in sub.iloc[1].tolist()]
    info = dict(zip(hdr, val))
    dn = sh["Declarant - numbers"]
    flat = [[("" if pd.isna(x) else str(x).strip()) for x in r] for r in dn.values.tolist()]
    inc = {}
    for r in flat:
        if len(r) > 3 and r[1] in ("Cash benefit", "Benefit in kind") and r[0]:
            inc.setdefault(r[0], num(r[3]))
    pay = sh["Payment deduction and deduction"].dropna(how="all")
    trekk = []
    for r in pay.values.tolist()[1:]:
        r = [("" if pd.isna(x) else str(x).strip()) for x in r]
        trekk.append((r[1], num(r[3]), r[5]))
    income = sh["Income information"].dropna(how="all")
    rows = []
    for r in income.values.tolist()[1:]:
        r = [("" if pd.isna(x) else str(x).strip()) for x in r]
        rows.append((r[1], num(r[4]), r[6], r[7]))
    return {"info": info, "income_totals": inc, "trekk": trekk, "income_rows": rows}


def read_g2n_columns(path, engine=None):
    """G2N with labels in columns 8-9 and one employee per column from 10; last column = total."""
    df = pd.read_excel(path, header=None, dtype=object, engine=engine)
    df = df.dropna(how="all").dropna(axis=1, how="all")
    vals = df.values.tolist()
    hdr = {str(vals[0][i]).strip(): vals[1][i] for i in range(8) if not pd.isna(vals[0][i])}
    # locate label columns: the column containing 'Employee ID'
    lab = next(i for i, x in enumerate(vals[0]) if str(x).strip() == "Employee ID")
    ids = []
    for j in range(lab + 2, len(vals[0])):
        x = vals[0][j]
        if pd.isna(x):
            break
        ids.append((j, str(x).strip()))
    total_col = ids[-1][0] + 1
    emps = {e: {} for _, e in ids}
    totals = {}
    section = None
    for r in vals:
        a = "" if pd.isna(r[lab]) else str(r[lab]).strip()
        b = "" if pd.isna(r[lab + 1]) else str(r[lab + 1]).strip()
        if a:
            section = a
        key = b if b else a
        if b:
            key = f"{section}::{b}"
        for j, e in ids:
            emps[e][key] = r[j]
        totals[key] = r[total_col] if total_col < len(r) else None
    return {"header": hdr, "ids": [e for _, e in ids], "emp": emps, "total": totals}


def g2n_code(emp, code):
    """Value of a pay element by its code ('62100') whatever section it sits in."""
    for k, v in emp.items():
        if "::" in k and k.split("::", 1)[1].startswith(f"{code} -"):
            return num(v) or 0.0
    return 0.0


AMT = re.compile(r"^-?[\d,]+\.\d{2}$")


def read_payslips_no(path):
    """One page per employee (Henkel template). Labels at x<250; period amount x 400-470; YTD x>=480.
    Header values read from fixed labels; summary row under 'Sammendrag'."""
    out = []
    with pdfplumber.open(path) as pdf:
        for pno, page in enumerate(pdf.pages, 1):
            words = page.extract_words()
            lines = {}
            for w in words:
                lines.setdefault(round(w["top"]), []).append(w)
            tops = sorted(lines)
            rec = {"page": pno, "lines": [], "ytd": {}}
            def row_text(t, lo=0, hi=9999):
                return " ".join(w["text"] for w in sorted(lines[t], key=lambda w: w["x0"]) if lo <= w["x0"] < hi)
            for t in tops:
                lt = row_text(t, 0, 180)
                rt = row_text(t, 180, 300)
                if lt.startswith("Lønnsmottaker"):
                    rec["navn"] = rt
                if lt.startswith("Arbeidstaker"):
                    rec["ansattnr"] = rt
                if lt.startswith("Utbetalingsdato"):
                    rec["utbetalingsdato"] = rt
                s = row_text(t)
                m = re.search(r"Fødselsnummer\s+(\d{11})", s)
                if m:
                    rec["fnr"] = m.group(1)
                m = re.search(r"Organisasjonsnr\.\s+(\d{9})", s)
                if m:
                    rec["orgnr"] = m.group(1)
                m = re.search(r"Skattekort / skatt %\s+(\d+)\s*/\s*(\d+)%", s)
                if m:
                    rec["tabell"], rec["pct"] = m.group(1), int(m.group(2))
                m = re.match(r"^NOK\s+([\d,]+\.\d{2})$", s.strip())
                if m and "net_top" not in rec:
                    rec["net_top"] = num(m.group(1))
            # item lines: label at x<250 starting with code or Feriepenger*
            labels = []
            for t in tops:
                lab = row_text(t, 55, 270)
                if re.match(r"^(\d{4,5} - |Feriepenge)", lab):
                    labels.append((t, lab))
            amts = [w for w in words if AMT.match(w["text"]) and w["x0"] > 400]
            for t, lab in labels:
                near = [w for w in amts if abs(w["top"] - t) <= 9]
                per = [w for w in near if w["x0"] < 470]
                ytd = [w for w in near if w["x0"] >= 470]
                rec["lines"].append({"label": lab,
                                     "code": lab.split(" - ")[0] if " - " in lab else lab,
                                     "period": num(per[0]["text"]) if per else None,
                                     "ytd": num(ytd[0]["text"]) if ytd else None})
            # summary
            st = next((t for t in tops if row_text(t).startswith("Betalingsvaluta")), None)
            if st is not None:
                nxt = [t for t in tops if t > st][0]
                ws = sorted(lines[nxt], key=lambda w: w["x0"])
                vals = {}
                for w in ws:
                    if w["text"] == "NOK":
                        continue
                    x = w["x0"]
                    k = ("skattepliktig" if x < 260 else "fradrag" if x < 360 else
                         "ytelser" if x < 460 else "netto")
                    vals[k] = num(w["text"])
                rec["summary"] = vals
            out.append(rec)
    return out


def read_pain001(path):
    t = etree.parse(path)
    r = t.getroot()
    def f(e, name):
        return [x for x in e.iter() if isinstance(x.tag, str) and _ln(x) == name]
    gh = f(r, "GrpHdr")[0]
    res = {"MsgId": _txt(gh, "MsgId"), "NbOfTxs": int(_txt(gh, "NbOfTxs")),
           "CtrlSum": num(_txt(gh, "CtrlSum")), "pmtinf": [], "tx": []}
    for p in f(r, "PmtInf"):
        res["pmtinf"].append({"NbOfTxs": int(_txt(p, "NbOfTxs") or 0), "CtrlSum": num(_txt(p, "CtrlSum")),
                              "ReqdExctnDt": _txt(p, "ReqdExctnDt"), "DbtrIBAN": _txt(p, "DbtrAcct/Id/IBAN"),
                              "Ccy": _txt(p, "DbtrAcct/Ccy"), "Purp": _txt(p, "PmtTpInf/CtgyPurp/Cd")})
        for tx in f(p, "CdtTrfTxInf"):
            acct = _txt(tx, "CdtrAcct/Id/IBAN") or _txt(tx, "CdtrAcct/Id/Othr/Id")
            amt_el = [x for x in tx.iter() if isinstance(x.tag, str) and _ln(x) == "InstdAmt"][0]
            res["tx"].append({"e2e": _txt(tx, "PmtId/EndToEndId"), "amt": num(amt_el.text),
                              "ccy": amt_el.get("Ccy"), "name": _txt(tx, "Cdtr/Nm"), "acct": acct,
                              "ustrd": _txt(tx, "RmtInf/Ustrd")})
    return res


def read_master_columns(path):
    """HRBLIZZ master data: header row containing 'Employee ID' (possibly preceded by a group row), one row
    per employee below it. Returns {employee id: {column label: value}}; for grouped columns the label is
    'Group / Field' when the row above carries a group name."""
    df = pd.read_excel(path, header=None, dtype=str)
    vals = [[None if (isinstance(x, float) and pd.isna(x)) else x for x in r] for r in df.values.tolist()]
    hi = next(i for i, r in enumerate(vals) if any(str(x).strip() == "Employee ID" for x in r if x is not None))
    hdr = vals[hi]
    grp = vals[hi - 1] if hi > 0 else [None] * len(hdr)
    labels, cur = [], None
    for j, h in enumerate(hdr):
        g = grp[j] if j < len(grp) else None
        if g is not None and str(g).strip() and j >= 8:
            cur = str(g).strip()
        lab = None if h is None else str(h).strip()
        labels.append(lab)
    col = labels.index("Employee ID")
    out = {}
    for r in vals[hi + 1:]:
        if r[col] is None:
            continue
        out[str(r[col]).strip()] = {labels[j]: r[j] for j in range(len(labels)) if labels[j]}
    return out
