#!/usr/bin/env python3
"""Parse Dutch payslip PDFs: header, cumulative footer, reservering block.

Used by validate.py for the cumulative roll-forward test (J-02 to J-04), the
zero-value footer test (J-07) and the reservering test (J-08). Standalone use:

    python payslips.py <payslips.pdf> [--out payslips.csv]

Requires pdftotext (poppler-utils), which is present in this environment.

The parser targets the layout used by HR Blizz Netherlands payslips. Fields are
located by label, not by column position, so a change in column widths does not
break it; a change in the Dutch labels will. If a field returns None for most
of the population, check the labels below against a sample slip before treating
the result as a finding.
"""

import argparse
import re
import subprocess
import sys

NUM = r"(-?[\d.,]+)"


def _num(s):
    """'50,219.45' or '50.219,45' -> float. Returns None on failure."""
    if s is None:
        return None
    s = s.strip()
    if not s or s in {"-", "--"}:
        return None
    # Decide the decimal separator by whichever appears last.
    if "," in s and "." in s:
        dec = "," if s.rfind(",") > s.rfind(".") else "."
        thou = "." if dec == "," else ","
        s = s.replace(thou, "").replace(dec, ".")
    elif "," in s:
        # Ambiguous: a lone comma is decimal if it is followed by 1-2 digits.
        s = re.sub(r",(\d{1,2})$", r".\1", s).replace(",", "")
    try:
        return float(s)
    except ValueError:
        return None


def _find(page, label, after=None):
    """Value following a label on the same line."""
    pat = re.escape(label) + r"[^\S\n]{2,}" + NUM
    for line in page.splitlines():
        if after and after not in line:
            pass
        m = re.search(pat, line)
        if m:
            return _num(m.group(1))
    return None


def _find_text(page, label):
    pat = re.escape(label) + r"[^\S\n]{2,}(\S+)"
    m = re.search(pat, page)
    return m.group(1) if m else None


def parse_page(page):
    """One payslip page -> dict, or None if it is not a payslip."""
    pid = _find_text(page, "Pers. nr.")
    if not pid:
        return None
    rec = {
        "employee_id": pid,
        "period": None,
        "run_nummer": _find(page, "Run nummer"),
        # cumulative footer
        "cum_fiscaal_loon": _find(page, "Fiscaal loon"),
        "cum_loonheffing": _find(page, "Loonheffing "),
        "cum_svw_loon": _find(page, "SVW loon"),
        "cum_arbeidskorting": _find(page, "Arbeidskorting cum."),
        "cum_dagen_gewerkt": _find(page, "Dagen gewerkt"),
        "cum_verloonde_uren": _find(page, "Verloonde uren"),
        # header fields worth cross-checking
        "tarief_bt": None,
        "jaarloon_bt": _find(page, "Jaarloon BT"),
        "kleur_tabel": _find_text(page, "Kleur/Tabe"),
        "lh_lhkorting": _find_text(page, "LH/LHKorting"),
        "zvw_ww_wia": _find_text(page, "ZVW/WW/WIA"),
        "schriftelijk": _find_text(page, "Schriftelijk"),
        "oproep": _find_text(page, "Oproep"),
        "geboortedatum": _find_text(page, "Geboortedatum"),
        "uit_dienst": _find_text(page, "Uit dienst"),
        "totaal_netto": None,
        # reservering
        "res_vakantiegeld_res": None,
        "res_vakantiegeld_saldo": None,
    }
    m = re.search(r"Salaris Periode\s+(\d+)", page) or \
        re.search(r"Periode\s+(\d{1,2})\b", page)
    if m:
        rec["period"] = int(m.group(1))
    m = re.search(r"Tarief BT\s+" + NUM + r"\s*%", page)
    if m:
        rec["tarief_bt"] = _num(m.group(1))
    m = re.search(r"Totaal netto[^\S\n]{2,}" + NUM, page)
    if m:
        rec["totaal_netto"] = _num(m.group(1))
    m = re.search(r"Vakantiegeld[^\S\n]{2,}" + NUM + r"[^\S\n]{2,}" + NUM, page)
    if m:
        rec["res_vakantiegeld_res"] = _num(m.group(1))
        rec["res_vakantiegeld_saldo"] = _num(m.group(2))
    return rec


def parse_pdf(path):
    """Every payslip page in the file -> list of dicts."""
    try:
        txt = subprocess.run(["pdftotext", "-layout", path, "-"],
                             capture_output=True, text=True,
                             check=True).stdout
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        raise RuntimeError(f"pdftotext failed on {path}: {e}")
    out = []
    for page in txt.split("\f"):
        if not page.strip():
            continue
        rec = parse_page(page)
        if rec:
            out.append(rec)
    return out


def main():
    p = argparse.ArgumentParser()
    p.add_argument("pdf")
    p.add_argument("--out")
    a = p.parse_args()
    recs = parse_pdf(a.pdf)
    if not recs:
        sys.exit("No payslip pages recognised. Check the labels in this file "
                 "against parse_page().")
    periods = {}
    for r in recs:
        periods[r["period"]] = periods.get(r["period"], 0) + 1
    print(f"{len(recs)} payslips parsed; "
          f"{len({r['employee_id'] for r in recs})} distinct employees")
    print("by period:", dict(sorted(periods.items(),
                                    key=lambda x: (x[0] is None, x[0]))))
    miss = [k for k in ("cum_fiscaal_loon", "cum_svw_loon", "cum_loonheffing")
            if sum(1 for r in recs if r[k] is None) > len(recs) * 0.5]
    if miss:
        print("WARNING: mostly unparsed ->", miss,
              "\n  Check the labels against a sample slip before using this.")
    if a.out:
        import csv
        with open(a.out, "w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=list(recs[0]))
            w.writeheader()
            w.writerows(recs)
        print("written to", a.out)


if __name__ == "__main__":
    main()
