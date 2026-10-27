"""Denmark readers: eIndkomst upload file (xlsx, field-coded columns), SKAT 'Afstemning af indberetninger'
(PDF print), payslips (Mercans DK template, pdfplumber word positions), Employee Detail GL (Sherwin)."""
import os
import re
import sys

import pandas as pd
import pdfplumber

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "common"))
from framework import num  # noqa: E402


def read_eindkomst_upload(path):
    """Row 0 = Danish labels, row 1 = field codes (e.g. 6000-4, B0013), rows 2.. = one record per employee."""
    df = pd.read_excel(path, header=None, dtype=str)
    labels = [str(x).strip() for x in df.iloc[0].tolist()]
    codes = [str(x).strip() for x in df.iloc[1].tolist()]
    recs = []
    for i in range(2, df.shape[0]):
        row = df.iloc[i].tolist()
        if all(pd.isna(x) for x in row):
            continue
        d = {}
        for c, v in zip(codes, row):
            d[c] = None if pd.isna(v) else str(v).strip()
        recs.append(d)
    return {"labels": dict(zip(codes, labels)), "codes": codes, "recs": recs}


def amt(rec, code):
    v = rec.get(code)
    return num(v) if v not in (None, "") else 0.0


def read_skat_afstemning(path):
    """Sum per feltnr from the SKAT eIndkomst reconciliation print."""
    with pdfplumber.open(path) as pdf:
        text = "\n".join(p.extract_text() or "" for p in pdf.pages)
    se = re.search(r"SE-nr\.\s*(\d{8})", text)
    per = re.search(r"afregningsperiode\s+(\d{2}\.\d{4})\s*-\s*(\d{2}\.\d{4})", text)
    printed = re.search(r"(\d{1,2}/\d{1,2}/\d{2}),\s*([\d:]+\s*[AP]M)", text)
    lines = text.splitlines()
    fields, values = [], []
    for i, l in enumerate(lines):
        if "Feltnr" in l:
            fields = re.findall(r"Feltnr\s+(\d{4})", l)
            for l2 in lines[i + 1:i + 4]:
                vs = re.findall(r"-?[\d.]+,\d{2}", l2)
                if len(vs) == len(fields):
                    values = [num(v) for v in vs]
                    break
            break
    name = None
    for i, l in enumerate(lines):
        if l.strip().startswith("SE-nr."):
            name = lines[i + 1].strip() if i + 1 < len(lines) else None
    return {"se": se.group(1) if se else None, "period": per.groups() if per else None,
            "printed": printed.groups() if printed else None, "name": name,
            "fields": dict(zip(fields, values))}


AMT = re.compile(r"^-?[\d,]+\.\d{2}$")


def read_payslips_dk(path):
    out = []
    with pdfplumber.open(path) as pdf:
        for pno, page in enumerate(pdf.pages, 1):
            words = page.extract_words()
            lines = {}
            for w in words:
                lines.setdefault(round(w["top"]), []).append(w)
            tops = sorted(lines)

            def txt(t, lo=0, hi=9999):
                return " ".join(w["text"] for w in sorted(lines[t], key=lambda w: w["x0"]) if lo <= w["x0"] < hi)

            rec = {"page": pno, "lines": [], "saldi": {}, "ferie": {}}
            tb = next((t for t in tops if txt(t).startswith("Beskrivelse")), 9999)
            for t in tops:
                s = txt(t)
                for lab, key in (("Ansattes navn", "navn"), ("Medarbejder ID", "ansattnr"), ("CPR-nummer", "cpr"),
                                 ("Betalingsdato", "betalingsdato"), ("CVR/SE-nummer", "se"),
                                 ("Ansættelsesdato", "ansat")):
                    m = re.search(re.escape(lab) + r"\s+(\S+(?:\s\S+)*?)(?=\s{0}(?:Medarbejder ID|Ansættelsesdato|CPR-nummer|$))", s)
                if s.startswith("Ansattes navn"):
                    rec["navn"] = txt(t, 170, 300)
                    rec["ansattnr"] = txt(t, 400, 600)
                if s.startswith("Medarbejderens adresse"):
                    rec["ansat"] = txt(t, 400, 600)
                if s.startswith("Betalingsdato"):
                    rec["betalingsdato"] = txt(t, 170, 300)
                m2 = re.search(r"CPR-nummer\s+(\S+)", s)
                if m2:
                    rec["cpr"] = m2.group(1)
                if s.startswith("CVR/SE-nummer"):
                    rec["se"] = txt(t, 170, 300)
                if s.startswith("Lønseddel for perioden"):
                    rec["periode"] = txt(t, 170, 400)
                if s.startswith("DKK"):
                    vs = [w for w in sorted(lines[t], key=lambda w: w["x0"]) if AMT.match(w["text"])]
                    if len(vs) == 3:
                        rec["indtjening"], rec["fradrag"], rec["netto"] = [num(w["text"]) for w in vs]
                m = re.search(r"A-SKAT:\s*([\d,]+\.\d{2})\s+Anvendt skattefradrag:\s*([\d,]+\.\d{2})\s+Skat af:\s*([\d,]+\.\d{2})", s)
                if m:
                    rec["askat_base"], rec["fradrag_used"], rec["skat_af"] = [num(x) for x in m.groups()]
                m = re.search(r"på konto:\s*(\S+)", s)
                if m:
                    rec["konto"] = m.group(1)
                m = re.match(r"^(\d{4,5})\s*(.*)$", txt(t, 55, 370))
                if m and t < tb:
                    ws = sorted(lines[t], key=lambda w: w["x0"])
                    # amounts may sit on the A-SKAT label line just below (2552)
                    near = [w for tt in tops if abs(tt - t) <= 2 for w in lines[tt]]
                    units = [w for w in near if 370 <= w["x0"] < 425 and AMT.match(w["text"])]
                    sats = [w for w in near if 425 <= w["x0"] < 470 and AMT.match(w["text"])]
                    belob = [w for w in near if w["x0"] >= 470 and AMT.match(w["text"])]
                    base = re.search(r"Base:\s*([\d,]+\.\d{2})", " ".join(w["text"] for w in near))
                    rec["lines"].append({"code": m.group(1), "label": m.group(2).replace("Base:", "").strip(),
                                         "units": num(units[0]["text"]) if units else None,
                                         "sats": num(sats[0]["text"]) if sats else None,
                                         "amount": num(belob[0]["text"]) if belob else None,
                                         "base": num(base.group(1)) if base else None})
                if t >= tb:
                    left = txt(t, 55, 255)
                    lv = [w for w in lines[t] if 255 <= w["x0"] < 300 and AMT.match(w["text"])]
                    if left and lv and left not in ("Beskrivelse",):
                        rec["saldi"][left] = num(lv[0]["text"])
                    if "Ferieberettiget" in s:
                        v = [w for w in lines[t] if w["x0"] >= 420 and AMT.match(w["text"])]
                        if v:
                            rec["ferie"]["ferieberettiget_periode"] = num(v[0]["text"])
                    if "Ferietillæg" in s:
                        v = sorted([w for w in lines[t] if w["x0"] >= 420 and AMT.match(w["text"])], key=lambda w: w["x0"])
                        if v:
                            rec["ferie"]["ferietillaeg_periode"] = num(v[0]["text"])
                            rec["ferie"]["ferietillaeg_ultimo"] = num(v[-1]["text"])
            out.append(rec)
    return out


def read_gl_employee_detail(path):
    """Sherwin 'Employee Detail GL File': header block, row starting 'Emp No'."""
    df = pd.read_excel(path, header=None, dtype=object)
    vals = [[None if (isinstance(x, float) and pd.isna(x)) else x for x in r] for r in df.values.tolist()]
    hi = next(i for i, r in enumerate(vals) if r and str(r[0]).strip() == "Emp No")
    hdr = [str(x).strip() if x is not None else None for x in vals[hi]]
    lines = []
    for r in vals[hi + 1:]:
        if r[0] is None or str(r[0]).strip().lower() in ("confidential", "total", ""):
            continue
        lines.append(dict(zip(hdr, r)))
    return lines
