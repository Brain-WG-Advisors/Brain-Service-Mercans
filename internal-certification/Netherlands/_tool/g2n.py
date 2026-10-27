#!/usr/bin/env python3
"""Gross-to-net: statutory recalculation, then reference for every other file.

The G2N is validated against STATUTE first — bases recomposed from the wage
types, tax recomputed from the tabellen, premiums recomputed from their own
bases, net proved, totals footed. Only once it stands on its own does it become
the reference that the payslip, the return, the ledger and the payment files
reconcile to at employee level.

That is different from using it as corroboration. A G2N that merely agrees with
the return proves nothing; a G2N whose own arithmetic is proven against the
Handboek is evidence.

Standalone:
    python g2n.py <g2n.xls[x]> --year 2025 [--period-table <witte-tabel.pdf>]
        [--catalogue <wage_type_catalogue.xlsx>] [--bt-upload <upload.xlsx>]
        [--dob <xml or master file>] [--out g2n_findings.csv]
"""

import argparse
import os
import re
import subprocess
import sys

TOL = 0.50                      # per employee per field, euros

# Account codes in the Mercans NL gross-to-net. Override with --map if a
# client uses different numbering.
ACC = {
    "tax_base":        "58552",   # income tax income base (regulation base)
    "bt_base":         "58572",   # white special rate tax income base
    "sv_base":         "58551",   # period taxable SSI base (EE)
    "sv_max":          "52990",   # maximum social security base
    "lhk_flag":        "58207",   # wage tax credit flag
    "arbeidskorting":  "58104",   # labour wage tax credit
    "alg_heffingskrt": "58103",   # general wage tax credit
    "starter":         "58200",
    "leaver":          "58299",
    "tax_regular":     "2552",    # payroll tax
    "tax_special":     "2572",    # wage tax special rate
    "tax_green":       "2582",    # green special rate
    "zvw_ee":          "2554",
    "wga_ee":          "2559",
    "wga_er":          "2560",
    "wko":             "2562",
    "aof_hoog":        "2563",
    "zvw_er":          "2564",
    "awf_laag":        "2568",
    "awf_hoog":        "2569",
}

RATES = {
    2025: {"aof_hoog": 0.0764, "aof_laag": 0.0628, "wko": 0.0050,
           "awf_laag": 0.0274, "awf_hoog": 0.0774, "zvw_er": 0.0651,
           "zvw_ee": 0.0526, "sv_max_4w": 5835.69, "aow_age": 67,
           "sv_max": {"4weken": 5835.69, "maand": 6322.00}},
    # Handboek Loonheffingen 2026 (versie maart 2026), Bijlage 1 Tabel 9/11/12.
    2026: {"aof_hoog": 0.0763, "aof_laag": 0.0627, "wko": 0.0050,
           "awf_laag": 0.0274, "awf_hoog": 0.0774, "zvw_er": 0.0610,
           "zvw_ee": 0.0485, "aow_age": 67,
           "sv_max": {"4weken": 6108.38, "maand": 6617.41}},
}

# Pay frequency; validate.py overrides it from --freq.
FREQ = "4weken"
PERIOD_END = None          # ISO date; validate.py sets it from the return
FREQ_LABEL = {"4weken": "four-weekly", "maand": "monthly"}


def norm_id(x):
    return re.sub(r"\.0$", "", str(x).strip())


def load(path):
    """Read a gross-to-net past its metadata header. Returns (df, meta)."""
    import pandas as pd
    eng = "xlrd" if path.lower().endswith(".xls") else None
    raw = pd.read_excel(path, engine=eng, header=None, nrows=20)
    meta, hdr = {}, None
    for i in range(len(raw)):
        vals = [str(v) for v in raw.iloc[i].tolist() if str(v) != "nan"]
        if len(vals) >= 2 and len(vals) <= 3 and hdr is None:
            meta[vals[0]] = vals[1]
        if vals and str(vals[0]).strip() == "Employee ID":
            hdr = i
            break
    if hdr is None:
        raise RuntimeError(f"No 'Employee ID' header row found in {path}")
    full = pd.read_excel(path, engine=eng, header=None)
    top = [str(v).strip() if str(v) != "nan" else "" for v in full.iloc[hdr]]
    nxt = [str(v).strip() if str(v) != "nan" else "" for v in full.iloc[hdr + 1]]
    two_row = sum(bool(re.match(r"^\d+ - ", v)) for v in nxt) > 3
    if two_row:
        names = [b if b else a for a, b in zip(top, nxt)]
        body = full.iloc[hdr + 2:]
    else:
        names = top
        body = full.iloc[hdr + 1:]
    seen = {}
    uniq = []
    for n in names:                      # keep duplicates distinguishable
        k = n or "_blank"
        seen[k] = seen.get(k, 0) + 1
        uniq.append(k if seen[k] == 1 else f"{k}#{seen[k]}")
    df = pd.DataFrame(body.values, columns=uniq)
    df = df[df["Employee ID"].notna()].copy()
    df["_id"] = df["Employee ID"].map(norm_id)
    # drop footers such as GRAND TOTAL / Confidential
    df = df[df["_id"].str.match(r"^[A-Za-z]?\d+$", na=False)].copy()
    meta["_two_row_header"] = two_row
    return df, meta


def col(df, code):
    """Locate a column by its leading account number."""
    for c in df.columns:
        if str(c).split(" -")[0].strip() == str(code):
            return c
    return None


def val(df, code):
    import pandas as pd
    c = col(df, code)
    if c is None:
        return pd.Series(0.0, index=df.index)
    return pd.to_numeric(df[c], errors="coerce").fillna(0.0)


def parse_period_table(pdf_path):
    """Four-weekly witte tijdvaktabel -> sorted list of 12-value rows.

    Row layout: tabelloon, then under-AOW (zonder, met, verrek. arbk.),
    then AOW born <=1945 (zonder, excl AOK, incl AOK, verrek.), then
    AOW born >=1946 (same four).
    """
    cache = pdf_path + ".rows.json"
    if os.path.exists(cache) and os.path.getmtime(cache) > os.path.getmtime(pdf_path):
        import json
        return json.load(open(cache, encoding="utf-8"))
    try:
        # pdftotext leaves the AOW columns blank on some rows; reading the
        # words by position recovers every cell.
        import collections
        import pdfplumber
        lines = []
        with pdfplumber.open(pdf_path) as pdf:
            for p in pdf.pages:
                byrow = collections.defaultdict(list)
                for w in p.extract_words():
                    byrow[round(w["top"])].append((w["x0"], w["text"]))
                lines += [" ".join(t for _, t in sorted(v)) for _, v in sorted(byrow.items())]
    except ImportError:
        lines = subprocess.run(["pdftotext", "-layout", pdf_path, "-"],
                               capture_output=True, text=True,
                               check=True).stdout.splitlines()
    rows = []
    for line in lines:
        nums = re.findall(r"-?\d{1,3}(?:\.\d{3})*,\d{2}", line)
        # Some rows come out of the text layer with the AOW columns blank.
        # Dropping them (as v1.4 did) makes lookups fall to the row below.
        # Keep the under-AOW columns and mark the rest as missing.
        if len(nums) == 12:
            rows.append([float(n.replace(".", "").replace(",", ".")) for n in nums])
        elif 4 <= len(nums) < 12 and re.match(r"^\s*\d{1,3}(?:\.\d{3})*,\d{2}\s", line):
            v = [float(n.replace(".", "").replace(",", ".")) for n in nums[:4]]
            rows.append(v + [None] * 8)
    # keep only genuine tabelloon steps (multiples of 4,50), one row per step,
    # preferring the complete 12-value row
    best = {}
    for r in rows:
        if r[0] <= 0 or round(r[0] * 100) % 450 != 0:
            continue
        k = round(r[0], 2)
        if k not in best or (best[k][4] is None and r[4] is not None):
            best[k] = r
    rows = list(best.values())
    rows.sort(key=lambda r: r[0])
    try:
        import json
        json.dump(rows, open(cache, "w", encoding="utf-8"))
    except OSError:
        pass
    return rows


def table_lookup(rows, tabelloon, aow, lhk, born_pre46=False, aok=False):
    """Withholding for a tabelloon. Takes the last row not above it."""
    if not rows or tabelloon is None:
        return None
    lo, hi = 0, len(rows) - 1
    if tabelloon < rows[0][0]:
        return 0.0
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if rows[mid][0] <= tabelloon:
            lo = mid
        else:
            hi = mid - 1
    r = rows[lo]
    if not aow:
        return r[2] if lhk else r[1]
    base = 4 if born_pre46 else 8
    if not lhk:
        return r[base]
    return r[base + 2] if aok else r[base + 1]


class Result:
    def __init__(self):
        self.rows = []

    def add(self, ref, area, finding, n, evidence="", impact="", basis=""):
        self.rows.append({"Ref": ref, "Area": area, "Finding": finding,
                          "Records": n, "Evidence": evidence,
                          "Euro impact": impact, "Basis": basis})

    def ok(self, ref, area, check, n):
        self.rows.append({"Ref": ref, "Area": area, "Finding": f"PASS — {check}",
                          "Records": n, "Evidence": "", "Euro impact": "",
                          "Basis": ""})


def _report(res, ref, area, hits, msg, basis, impact_idx=None):
    if not hits:
        return False
    ev = "; ".join(str(h[0]) for h in hits[:25]) + (" ..." if len(hits) > 25 else "")
    imp = ""
    if impact_idx is not None:
        imp = f"{sum(h[impact_idx] for h in hits):,.2f}"
    res.add(ref, area, msg.format(n=len(hits)), len(hits), ev, imp, basis)
    return True


def validate(df, year, res, period_rows=None, dob=None, lhk=None,
             bt_supplied=None, catalogue=None, is_period=True):
    """Statutory recalculation of the gross-to-net."""
    R = RATES[year]
    ids = df["_id"].tolist()
    sv = val(df, ACC["sv_base"])
    taxbase = val(df, ACC["tax_base"])
    n = len(df)

    # G-S1: SV base against the period maximum
    if is_period:
        cap = R["sv_max"][FREQ]
        over = [(i, b) for i, b in zip(ids, sv) if b > cap + 0.01]
        at = [(i, b) for i, b in zip(ids, sv) if abs(b - cap) < 0.005]
        if at:
            res.add("G-S1", "SV base",
                    f"{len(at)} employees carry an SV base exactly at the "
                    f"{FREQ_LABEL[FREQ]} maximum of {cap:,.2f}. Confirm the cap was "
                    f"applied cumulatively under VCR and not as a flat period "
                    f"ceiling.", len(at),
                    "; ".join(i for i, _ in at[:25]), "",
                    "Handboek Loonheffingen, hoofdstuk 5 (VCR)")
        if not over and not at:
            res.ok("G-S1", "SV base", "SV base within the period maximum", n)

    # G-S2: employer premiums from the SV base
    for ref, code, key, label in (
            ("G-S2a", ACC["aof_hoog"], "aof_hoog", "Aof hoog"),
            ("G-S2b", ACC["wko"], "wko", "Opslag Wko"),
            ("G-S2c", ACC["awf_laag"], "awf_laag", "AWf laag"),
            ("G-S2d", ACC["awf_hoog"], "awf_hoog", "AWf hoog"),
            ("G-S2e", ACC["zvw_er"], "zvw_er", "Werkgeversheffing Zvw")):
        if col(df, code) is None:
            continue
        dec = val(df, code)
        hits, nil = [], []
        for i, b, d in zip(ids, sv, dec):
            if b == 0:
                continue
            if d == 0:
                # Mutually exclusive premiums (AWf laag vs hoog) and
                # classification questions are tested elsewhere; a nil premium
                # is not a recalculation failure.
                nil.append((i, b))
                continue
            exp = round(b * R[key], 2)
            if abs(d - exp) > TOL:
                hits.append((i, b, d, exp, d - exp))
        if not _report(res, ref, "Employer premiums", hits,
                       f"{{n}} employees: {label} does not recalculate from "
                       f"the SV base at {R[key] * 100:.2f}%.",
                       f"Handboek Loonheffingen {year}, Tabel 9 / 12", 4):
            res.ok(ref, "Employer premiums",
                   f"{label} recalculates at {R[key] * 100:.2f}% of the SV base",
                   n - len(nil))

    # G-S2f: employee Zvw where it applies
    if col(df, ACC["zvw_ee"]) is not None:
        dec = val(df, ACC["zvw_ee"])
        hits = []
        for i, b, d in zip(ids, sv, dec):
            if d == 0 or b == 0:
                continue
            exp = round(b * R["zvw_ee"], 2)
            if abs(d - exp) > TOL:
                hits.append((i, b, d, exp, d - exp))
        if not _report(res, "G-S2f", "Employee contributions", hits,
                       f"{{n}} employees: the ingehouden bijdrage Zvw does not "
                       f"recalculate at {R['zvw_ee'] * 100:.2f}% of the SV "
                       f"base.", f"Handboek Loonheffingen {year}, Tabel 12", 4):
            res.ok("G-S2f", "Employee contributions",
                   "Employee Zvw recalculates where charged", n)

    # G-S3: special-rate tax against the client-supplied percentage
    if bt_supplied and col(df, ACC["bt_base"]) is not None:
        bb, bt = val(df, ACC["bt_base"]), val(df, ACC["tax_special"])
        mism, nosup = [], []
        for i, b, t in zip(ids, bb, bt):
            if b <= 0.02:
                continue
            p = bt_supplied.get(i)
            if p is None:
                nosup.append((i, b, t))
                continue
            exp = round(b * p / 100, 2)
            if abs(t - exp) > TOL:
                mism.append((i, b, p, t, exp, t - exp))
        if not _report(res, "G-S3", "Special-rate tax", mism,
                       "{n} employees: special-rate tax does not equal the "
                       "client-supplied percentage applied to the special-rate "
                       "base.", "Client input, pay element 52572", 5):
            res.ok("G-S3", "Special-rate tax",
                   "Special-rate tax equals the supplied percentage applied to "
                   "its base", n)
        _report(res, "G-S3b", "Special-rate tax", nosup,
                "{n} employees have a special-rate base with no percentage "
                "supplied.", "Client input, pay element 52572")

    # G-S4: regular withholding against the period table
    if period_rows and dob and is_period:
        tax = val(df, ACC["tax_regular"])
        flag = val(df, ACC["lhk_flag"])
        hits, skipped = [], 0
        for i, tb, t in zip(ids, taxbase, tax):
            d = dob.get(i)
            if d is None or tb <= 0:
                skipped += 1
                continue
            import datetime as dt
            b = dt.date.fromisoformat(str(d)[:10])
            # Handboek 2026 §9.3.3: the AOW column applies from the 1st day of
            # the calendar month in which the AOW age is reached.
            try:
                bday = b.replace(year=b.year + R["aow_age"])
            except ValueError:
                bday = b.replace(year=b.year + R["aow_age"], day=28)
            pend = dt.date.fromisoformat(PERIOD_END) if PERIOD_END else dt.date(year, 12, 31)
            aow = (bday.year, bday.month) <= (pend.year, pend.month)
            l = (lhk.get(i) if lhk else None)
            if l is None:
                l = bool(flag[df.index[ids.index(i)]]) if len(flag) else True
            exp = table_lookup(period_rows, tb, aow, bool(l),
                               born_pre46=(b.year <= 1945))
            if exp is None:
                skipped += 1
                continue
            if abs(t - exp) > TOL:
                hits.append((i, tb, t, exp, t - exp))
        if not _report(res, "G-S4", "Regular withholding", hits,
                       "{n} employees: regular loonheffing does not equal the "
                       f"amount in the {FREQ_LABEL[FREQ]} witte tijdvaktabel for their "
                       "tabelloon, age and loonheffingskorting status.",
                       f"Witte tabel {FREQ} {year} (Nederland, Standaard)", 4):
            res.ok("G-S4", "Regular withholding",
                   "Regular loonheffing matches the period table",
                   n - skipped)
        if skipped:
            res.add("G-S4b", "Regular withholding",
                    f"{skipped} employees not recalculated: no date of birth, "
                    f"or a nil tax base.", skipped, "", "", "")
    elif is_period:
        res.add("G-S4", "Regular withholding",
                "NOT TESTED — supply --period-table and a date-of-birth source "
                "(the loonaangifte XML or the master extract) to recalculate "
                "regular withholding.", 0, "", "", "")

    # G-S5: base composition against the wage type catalogue
    if catalogue:
        for ref, base_code, flagname, label in (
                ("G-S5a", ACC["tax_base"], "tax", "income tax base"),
                ("G-S5b", ACC["sv_base"], "sv", "SV base")):
            codes = catalogue.get(flagname, set())
            present = [c for c in df.columns
                       if str(c).split(" -")[0].strip() in codes]
            if not present:
                continue
            import pandas as pd
            built = sum(pd.to_numeric(df[c], errors="coerce").fillna(0.0)
                        for c in present)
            declared = val(df, base_code)
            hits = [(i, bu, de, bu - de) for i, bu, de
                    in zip(ids, built, declared) if abs(bu - de) > TOL]
            if not _report(res, ref, "Base composition", hits,
                           f"{{n}} employees: the {label} does not equal the "
                           f"sum of the wage types the catalogue flags as "
                           f"subject to it ({len(present)} elements).",
                           "NL Wage Type Catalogue", 3):
                res.ok(ref, "Base composition",
                       f"The {label} equals the sum of its flagged wage types", n)
    else:
        res.add("G-S5", "Base composition",
                "NOT TESTED — supply --catalogue to recompose the tax and SV "
                "bases from the wage types flagged as subject to them. This is "
                "the deepest statutory test on the gross-to-net; without it "
                "the bases are taken as given.", 0, "", "", "")

    # G-S6: net pay proves out
    import pandas as pd
    if {"Gross Salary", "Total Deductions", "Net Pay"} <= set(df.columns):
        g = pd.to_numeric(df["Gross Salary"], errors="coerce").fillna(0.0)
        d = pd.to_numeric(df["Total Deductions"], errors="coerce").fillna(0.0)
        nt = pd.to_numeric(df["Net Pay"], errors="coerce").fillna(0.0)
        # A residual equal to the bijtelling columns is presentation, not a
        # calculation error: notional wage is taxed but never paid.
        bij = sum(pd.to_numeric(df[c], errors="coerce").fillna(0.0)
                  for c in df.columns
                  if str(c).split(" -")[0].strip().startswith("658")) \
            if any(str(c).split(" -")[0].strip().startswith("658")
                   for c in df.columns) else pd.Series(0.0, index=df.index)
        hits, explained = [], []
        for i, a, b, c, bj in zip(ids, g, d, nt, bij):
            resid = a - b - c
            if abs(resid) <= TOL:
                continue
            (explained if abs(resid - bj) <= TOL else hits).append(
                (i, a, b, c, resid))
        if explained:
            res.add("G-S6b", "Net pay",
                    f"{len(explained)} employees: gross minus deductions "
                    f"exceeds net by exactly the bijtelling columns. Notional "
                    f"wage is taxed but not paid, so this is a presentation "
                    f"point rather than a calculation error — but the client "
                    f"will query it.", len(explained),
                    "; ".join(e[0] for e in explained[:25]), "", "")
        caveat = ("" if is_period else
                  " NOTE: this is a year-to-date report. Retro reversals can "
                  "aggregate differently across the gross, deduction and net "
                  "columns, so the identity is only conclusive on a "
                  "single-period gross-to-net. Re-run on the period report "
                  "before treating this as a finding.")
        if not _report(res, "G-S6", "Net pay", hits,
                       "{n} employees: gross minus total deductions does not "
                       "equal net pay, and the difference is not the "
                       "bijtelling." + caveat, "Arithmetic", 4):
            res.ok("G-S6", "Net pay", "Gross minus deductions equals net", n)
        neg = [(i, c) for i, c in zip(ids, nt) if c < 0]
        zer = [(i, c) for i, c in zip(ids, nt) if c == 0]
        if neg:
            res.add("G-S7", "Net pay",
                    f"{len(neg)} employees have negative net pay. Correctly "
                    f"excluded from an outgoing payment batch; confirm each is "
                    f"recovered.", len(neg),
                    "; ".join(i for i, _ in neg[:25]),
                    f"{sum(c for _, c in neg):,.2f}", "")
        if zer:
            res.add("G-S8", "Net pay",
                    f"{len(zer)} employees have nil net pay.", len(zer),
                    "; ".join(i for i, _ in zer[:25]), "", "")

    # G-S9: employer contribution total foots
    if "Total Employer Contributions" in df.columns:
        er_codes = [ACC[k] for k in ("wga_er", "wko", "aof_hoog", "zvw_er",
                                     "awf_laag", "awf_hoog")]
        built = sum(val(df, c) for c in er_codes)
        extra = [c for c in df.columns if str(c).split(" -")[0].strip()
                 .startswith("236")]
        for c in extra:
            built = built + pd.to_numeric(df[c], errors="coerce").fillna(0.0)
        dec = pd.to_numeric(df["Total Employer Contributions"],
                            errors="coerce").fillna(0.0)
        hits = [(i, b, d, b - d) for i, b, d in zip(ids, built, dec)
                if abs(b - d) > TOL]
        if not _report(res, "G-S9", "Totals", hits,
                       "{n} employees: total employer contributions does not "
                       "equal the sum of the employer elements.", "Arithmetic", 3):
            res.ok("G-S9", "Totals",
                   "Total employer contributions foots to its elements", n)
    return res


def reference(df):
    """Per-employee reference frame for reconciling every other deliverable."""
    import pandas as pd
    out = pd.DataFrame({"employee_id": df["_id"]})
    for k, code in ACC.items():
        if col(df, code) is not None:
            out[k] = val(df, code).values
    for c in ("Gross Salary", "Total Deductions", "Net Pay",
              "Total Employer Contributions"):
        if c in df.columns:
            out[c.lower().replace(" ", "_")] = pd.to_numeric(
                df[c], errors="coerce").fillna(0.0).values
    out["tax_total"] = out.get("tax_regular", 0) + out.get("tax_special", 0) \
        + out.get("tax_green", 0)
    return out


def main():
    p = argparse.ArgumentParser()
    p.add_argument("g2n")
    p.add_argument("--year", type=int, default=2025)
    p.add_argument("--period-table")
    p.add_argument("--catalogue")
    p.add_argument("--bt-upload")
    p.add_argument("--cumulative", action="store_true",
                   help="the file is a year-to-date report, not one period")
    p.add_argument("--out")
    a = p.parse_args()
    import pandas as pd
    df, meta = load(a.g2n)
    print(f"{len(df)} employees; period {meta.get('Period', 'unknown')}")
    rows = parse_period_table(a.period_table) if a.period_table else None
    if rows:
        print(f"period table: {len(rows)} tabelloon rows")
    bt = None
    if a.bt_upload:
        u = pd.read_excel(a.bt_upload)
        ic = next(c for c in u.columns if "id" in str(c).lower())
        ac = next(c for c in u.columns if "amount" in str(c).lower())
        bt = {norm_id(i): float(v) for i, v in zip(u[ic], u[ac])
              if pd.notna(v)}
    res = Result()
    validate(df, a.year, res, period_rows=rows, bt_supplied=bt,
             is_period=not a.cumulative)
    out = pd.DataFrame(res.rows)
    print(out[["Ref", "Area", "Records", "Finding"]].to_string(index=False))
    if a.out:
        out.to_csv(a.out, index=False)
        print("written to", a.out)


if __name__ == "__main__":
    main()
