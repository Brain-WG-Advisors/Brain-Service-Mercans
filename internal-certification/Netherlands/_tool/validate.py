#!/usr/bin/env python3
"""Deterministic checks over a Netherlands payroll deliverable pack.

Runs the arithmetic and code-list tests that prose does badly at scale, and
emits a findings table. Judgement-level work stays with the reviewer.

Every finding carries the official control number where one exists. Where no
control exists (notably Whk), the finding says so explicitly.

Usage:
    python validate.py --xml loonaangifte.xml --year 2025 \
        [--g2n g2n.xlsx] [--sepa sepa.xml] [--master master.xlsx] \
        [--bt-upload tax_upload.xlsx] [--out findings.xlsx]
"""

import argparse
import datetime as dt
import os
import re
import sys
import xml.etree.ElementTree as ET
import collections
from collections import defaultdict

# --------------------------------------------------------------------------
# Statutory parameters. Sourced from Handboek Loonheffingen, tariefannex.
# Verify against references/<year>/rates-<year>.md before changing anything.
# --------------------------------------------------------------------------

RATES = {
    2025: {
        "AwfLg": 0.0274, "AwfHg": 0.0774, "AwfHz": 0.0774,
        "AofLg": 0.0628, "AofHg": 0.0764,
        "Wko": 0.0050, "Ufo": 0.0068,
        "WghZvw": 0.0651, "IngBijdrZvw": 0.0526,
        "max_premieloon_jaar": 75864.00,
        "max_premieloon_tijdvak": {
            "dag": 291.78, "week": 1458.92, "4weken": 5835.69,
            "maand": 6322.00, "kwartaal": 18966.00, "jaar": 75864.00,
        },
        "aow_leeftijd_jaren": 67,
        "anoniementarief": 0.52,
        "namespace_year": "2025",
    },
    # Handboek Loonheffingen 2026 (versie maart 2026), Bijlage 1, Tabel 9,
    # 11 and 12; AOW age 67 for 2024-2027 (§8.2.2). Read 2026-10-14.
    2026: {
        "AwfLg": 0.0274, "AwfHg": 0.0774, "AwfHz": 0.0774,
        "AofLg": 0.0627, "AofHg": 0.0763,
        "Wko": 0.0050, "Ufo": 0.0068,
        "WghZvw": 0.0610, "IngBijdrZvw": 0.0485,
        "max_premieloon_jaar": 79409.00,
        "max_premieloon_tijdvak": {
            "dag": 305.41, "week": 1527.09, "4weken": 6108.38,
            "maand": 6617.41, "kwartaal": 19852.25, "jaar": 79409.00,
        },
        "aow_leeftijd_jaren": 67,
        "anoniementarief": 0.52,
        "namespace_year": "2026",
    },
}

# Pay frequency of the run being validated ("4weken" or "maand"); set in main().
FREQ = "4weken"

# Monthly tijdvakken, from tijdvakcodes-2026.pdf (Maandaangiften 2026).
TIJDVAKKEN_MND = {
    2026: [
        ("6010", "2026-01-01", "2026-01-31", "2026-02-28"),
        ("6020", "2026-02-01", "2026-02-28", "2026-03-31"),
        ("6030", "2026-03-01", "2026-03-31", "2026-04-30"),
        ("6040", "2026-04-01", "2026-04-30", "2026-05-31"),
        ("6050", "2026-05-01", "2026-05-31", "2026-06-30"),
        ("6060", "2026-06-01", "2026-06-30", "2026-07-31"),
        ("6070", "2026-07-01", "2026-07-31", "2026-08-31"),
        ("6080", "2026-08-01", "2026-08-31", "2026-09-30"),
        ("6090", "2026-09-01", "2026-09-30", "2026-10-31"),
        ("6100", "2026-10-01", "2026-10-31", "2026-11-30"),
        ("6110", "2026-11-01", "2026-11-30", "2026-12-31"),
        ("6120", "2026-12-01", "2026-12-31", "2027-01-31"),
    ],
}


def tijdvakken(year):
    return (TIJDVAKKEN_MND if FREQ == "maand" else TIJDVAKKEN_4W).get(year, [])


# Four-weekly tijdvakken, from tijdvakcodes-<year>.pdf.
TIJDVAKKEN_4W = {
    2025: [
        ("5710", "2025-01-01", "2025-01-26", "2025-02-26"),
        ("5720", "2025-01-27", "2025-02-23", "2025-03-23"),
        ("5730", "2025-02-24", "2025-03-23", "2025-04-23"),
        ("5740", "2025-03-24", "2025-04-20", "2025-05-20"),
        ("5750", "2025-04-21", "2025-05-18", "2025-06-18"),
        ("5760", "2025-05-19", "2025-06-15", "2025-07-15"),
        ("5770", "2025-06-16", "2025-07-13", "2025-08-13"),
        ("5780", "2025-07-14", "2025-08-10", "2025-09-10"),
        ("5790", "2025-08-11", "2025-09-07", "2025-10-07"),
        ("5800", "2025-09-08", "2025-10-05", "2025-11-05"),
        ("5810", "2025-10-06", "2025-11-02", "2025-12-02"),
        ("5820", "2025-11-03", "2025-11-30", "2025-12-30"),
        ("5830", "2025-12-01", "2025-12-31", "2026-01-31"),
    ],
}

# Bijzondere beloningen, witte tabel Nederland Standaard.
# (jaarloon_from, under_aow_zonder, under_aow_met_std, under_aow_met_verr,
#  aow_zonder, aow_excl_std, aow_excl_verr, aow_incl_std, aow_incl_verr)
# The 1945-or-earlier and 1946-or-later blocks differ only at 38.442 and
# 40.503; BB_AOW_PRE46 carries the differences.
BB_2025 = [
    (0,       35.82, 0.00,  0.00,   17.92, 0.00,  0.00,  0.00,  0.00),
    (11050,   35.82, 35.82, -8.05,  17.92, 0.00,  0.00,  0.00,  0.00),
    (13144,   35.82, 35.82, -30.03, 17.92, 0.00,  0.00,  0.00,  0.00),
    (24342,   35.82, 35.82, -2.26,  17.92, 0.00,  0.00,  0.00,  0.00),
    (28407,   35.82, 35.82, 4.08,   17.92, 0.00,  0.00,  0.00,  0.00),
    (34001,   35.82, 35.82, 4.08,   17.92, 17.92, 2.04,  0.00,  0.00),
    (36661,   35.82, 35.82, 4.08,   17.92, 17.92, 2.04,  17.92, 2.04),
    (38442,   37.48, 37.48, 4.08,   37.48, 37.48, 2.04,  37.48, 2.04),
    (40503,   37.48, 37.48, 4.08,   37.48, 37.48, 2.04,  37.48, 2.04),
    (43072,   37.48, 37.48, 12.85,  37.48, 37.48, 6.43,  37.48, 6.43),
    (45309,   37.48, 37.48, 12.85,  37.48, 37.48, 21.43, 37.48, 21.43),
    (58876,   37.48, 37.48, 12.85,  37.48, 37.48, 6.43,  37.48, 6.43),
    (76818,   49.50, 49.50, 6.51,   49.50, 49.50, 3.26,  49.50, 3.26),
    (139405,  49.50, 49.50, 0.00,   49.50, 49.50, 0.00,  49.50, 0.00),
]

# Overrides for AOW-age employees born 1945 or earlier, where that block
# differs from the 1946-or-later block. Keyed by jaarloon threshold:
# (zonder, excl_std, excl_verr, incl_std, incl_verr)
BB_2025_AOW_PRE46 = {
    38442: (17.92, 17.92, 2.04, 17.92, 2.04),
    40503: (37.48, 37.48, 2.04, 37.48, 2.04),
}

# Per-employee, per-field rounding tolerance in euros. See controls-<year>.md.
TOLERANCE = 0.50

# SrtIv values that force AWf/Aof laag aanwas to zero (L2201, L2336, L2340).
BENEFIT_SRTIV = {"31", "32", "33", "38", "39", "40", "46"}
# SrtIv values where Loon SV must be zero (L2208).
LOONSV_ZERO_SRTIV = {
    "17", "22", "23", "24", "34", "36", "37", "42", "43", "44", "45",
    "50", "52", "55", "56", "57", "58", "59", "60", "61", "62", "63",
}
# Tabelcodes exempting the BSN requirement (L2287).
BSN_EXEMPT_TABELCODE = {"221", "224", "225", "940", "999"}


def ns_strip(tag):
    return tag.split("}", 1)[-1] if "}" in tag else tag


class Findings:
    def __init__(self):
        self.rows = []
        self.not_tested = []
        self.coverage = []
        self._n = 0

    def add(self, severity, area, finding, evidence="", impact="",
            basis="", control=""):
        self._n += 1
        self.rows.append({
            "ID": f"F{self._n:03d}", "Severity": severity, "Area": area,
            "Finding": finding, "Evidence": evidence,
            "Euro impact": impact, "Statutory basis": basis,
            "Control": control,
        })

    def skip(self, area, reason, control=""):
        self.not_tested.append({"Area": area, "Reason": reason,
                                "Control": control})

    def ok(self, control, area, check, population=""):
        """A check that ran clean. Coverage rows are part of the deliverable."""
        self.coverage.append({"Control": control, "Area": area,
                              "Check": check, "Population": population,
                              "Result": "Pass"})


def parse_xml(path):
    """Return (root, meta, period_ikvs, correction_blocks)."""
    tree = ET.parse(path)
    root = tree.getroot()
    m = re.search(r"schemas/Loonaangifte/(\d{4})/", root.tag)
    meta = {
        "namespace_year": m.group(1) if m else None,
        "berichtversie": root.get("version"),
    }
    for el in root.iter():
        t = ns_strip(el.tag)
        if t in ("IdBer", "DatTdAanm", "GebrSwPakket", "RelNr", "LhNr", "NmIP"):
            meta.setdefault(t, el.text)

    period, corrections = None, []
    for ae in root.iter():
        t = ns_strip(ae.tag)
        if t == "TijdvakAangifte":
            period = ae
        elif t == "TijdvakCorrectie":
            corrections.append(ae)
    return root, meta, period, corrections


def collective(period_el):
    """Flat dict of the collective block's scalar children."""
    out, saldi = {}, []
    for el in period_el.iter():
        if ns_strip(el.tag) == "CollectieveAangifte":
            for c in el:
                tag = ns_strip(c.tag)
                if tag == "SaldoCorrectiesVoorgaandTijdvak":
                    s = {ns_strip(g.tag): g.text for g in c}
                    saldi.append(s)
                elif c.text is not None and not list(c):
                    out[tag] = c.text
    return out, saldi


def nominative(period_el):
    """One flat dict per inkomstenverhouding in the period block."""
    recs = []
    for el in period_el.iter():
        if ns_strip(el.tag) not in ("InkomstenverhoudingInitieel",
                                    "Inkomstenverhouding"):
            continue
        rec = defaultdict(list)
        for c in el.iter():
            tag = ns_strip(c.tag)
            if c.text and c.text.strip() and not list(c):
                rec[tag].append(c.text.strip())
        recs.append({k: (v[0] if len(v) == 1 else v) for k, v in rec.items()})
    return recs


def num(v, default=0.0):
    if v is None:
        return default
    if isinstance(v, list):
        v = v[0]
    try:
        return float(str(v).replace(",", "."))
    except (ValueError, TypeError):
        return default


def first(rec, *keys):
    for k in keys:
        if k in rec:
            v = rec[k]
            return v[0] if isinstance(v, list) else v
    return None


def reached_aow(birth, ref_date, aow_years):
    if not birth:
        return None
    try:
        b = dt.date.fromisoformat(str(birth)[:10])
        r = dt.date.fromisoformat(str(ref_date)[:10])
    except ValueError:
        return None
    try:
        aow = b.replace(year=b.year + aow_years)
    except ValueError:                      # 29 February
        aow = b.replace(year=b.year + aow_years, day=28)
    return r >= aow


def check_period(meta, coll, period_el, corrections, year, f):
    rates = RATES[year]
    if meta["namespace_year"] != rates["namespace_year"]:
        f.add("Critical", "Period",
              f"XML namespace year {meta['namespace_year']} does not match the "
              f"validation year {year}. A year mismatch produces silent false "
              f"passes; stop and use the matching reference set.",
              control="")
        return None

    dates = {ns_strip(c.tag): c.text for c in period_el
             if ns_strip(c.tag) in ("DatAanvTv", "DatEindTv")}
    start, end = dates.get("DatAanvTv"), dates.get("DatEindTv")
    match = [t for t in tijdvakken(year)
             if t[1] == start and t[2] == end]
    if match:
        code, _, _, deadline = match[0]
        f.add("Observation", "Period",
              f"Period identified as tijdvakcode {code} "
              f"({start} to {end}); filing and payment deadline {deadline}.",
              evidence=f"tijdvakcodes-{year}.pdf")
    else:
        f.add("Major", "Period",
              f"Declared tijdvak {start} to {end} is not a published "
              f"{FREQ} period for {year}. Confirm the pay cycle.",
              basis=f"Tijdvakcodes aangifte loonheffingen {year}")

    # Correction blocks must be genuine earlier periods of the same year,
    # and must not restate a period already inside the period block.
    valid = {(t[1], t[2]) for t in tijdvakken(year)}
    for cb in corrections:
        d = {ns_strip(c.tag): c.text for c in cb
             if ns_strip(c.tag) in ("DatAanvTv", "DatEindTv")}
        pair = (d.get("DatAanvTv"), d.get("DatEindTv"))
        if pair not in valid:
            f.add("Major", "Period",
                  f"TijdvakCorrectie block {pair[0]} to {pair[1]} is not a "
                  f"published {year} period boundary.",
                  basis=f"Tijdvakcodes aangifte loonheffingen {year}")
        if pair == (start, end):
            f.add("Critical", "Period",
                  "The same tijdvak appears as both the period block and a "
                  "TijdvakCorrectie block. The same wages are presented twice "
                  "in one return.",
                  basis="Gegevensspecificaties, hoofdstuk 2")
    return (start, end)


def period_gate(systematiek, corrections, f):
    """A-05: withhold the period tests until the systematiek is confirmed."""
    if systematiek in ("loon-in", "loon-over"):
        f.ok("A-05", "Systematiek",
             f"Confirmed as {systematiek} by the reviewer", "engagement-level")
        return True
    f.skip("Period integrity (A-05, A-06)",
           "Systematiek not confirmed. Under loon-in the period block should "
           "carry current-period wage plus retro paid in the run; under "
           "loon-over it should carry current-period wage only, with retro in "
           "the correction blocks. The two tests give opposite answers. The "
           "Handboek also states that a payment relating to a tijdvak of 2025 "
           "or earlier is always treated under the hoofdregel even where "
           "loon-over is otherwise applied, which is capable of reversing the "
           "determination and must be resolved with Dutch tax counsel. "
           "Re-run with --systematiek once confirmed.",
           "A-05")
    if corrections:
        f.add("Observation", "Systematiek",
              f"{len(corrections)} correction blocks are filed alongside this "
              f"return, which is one of the conditions for loon-over. This is "
              f"evidence, not a determination.",
              basis="Handboek Loonheffingen §9.2.1", control="A-05")
    return False


def check_collective_vs_nominative(coll, recs, saldi, f):
    """Poortcontrole: each collective total = rounded sum of its nominal field."""
    pairs = [
        ("TotLnLbPh", "LnLbPh"), ("IngLbPh", "IngLbPh"),
        ("TotLnSV", "LnSV"), ("TotWghZvw", "WghZvw"),
        ("IngBijdrZvw", "BijdrZvw"),
        ("TotPrlnAofAnwLg", "PrlnAofAnwLg"), ("TotPrlnAofAnwHg", "PrlnAofAnwHg"),
        ("TotPrlnAwfAnwLg", "PrlnAwfAnwLg"), ("TotPrlnAwfAnwHg", "PrlnAwfAnwHg"),
        ("TotPrlnAwfAnwHz", "PrlnAwfAnwHz"), ("TotPrlnWhkAnw", "PrlnWhkAnw"),
        ("TotPrAofLg", "PrAofLg"), ("TotPrAofHg", "PrAofHg"),
        ("TotOpslWko", "OpslWko"), ("TotPrGediffWhk", "PrGediffWhk"),
        ("TotPrAwfLg", "PrAwfLg"), ("TotPrAwfHg", "PrAwfHg"),
        ("TotPrAwfHz", "PrAwfHz"),
        ("PrLnUFO", "PrLnUfo"), ("PrUFO", "PrUFO"),
    ]
    tested = failed = 0
    for tot_tag, nom_tag in pairs:
        if tot_tag not in coll:
            continue
        tested += 1
        declared = num(coll[tot_tag])
        summed = sum(num(first(r, nom_tag)) for r in recs)
        if abs(declared - summed) > TOLERANCE:
            f.add("Critical", "Return consistency",
                  f"Collective {tot_tag} does not equal the sum of {nom_tag} "
                  f"across the nominative records.",
                  evidence=f"declared {declared:,.2f}; sum {summed:,.2f}",
                  impact=f"{declared - summed:,.2f}",
                  basis="Gegevensspecificaties, Poortcontrole overig",
                  control="B-01")
            failed += 1

    if tested and not failed:
        f.ok("B-01", "Return consistency",
             "Every collective total equals the sum of its nominative field",
             f"{tested} rubrieken")

    # TotGen = TotTeBet + sum of correction saldi
    if "TotGen" in coll and "TotTeBet" in coll:
        expected = num(coll["TotTeBet"]) + sum(num(s.get("Saldo")) for s in saldi)
        if abs(num(coll["TotGen"]) - expected) > TOLERANCE:
            f.add("Critical", "Return consistency",
                  "TotGen does not equal TotTeBet plus the correction saldi.",
                  evidence=f"TotGen {num(coll['TotGen']):,.2f}; "
                           f"expected {expected:,.2f}",
                  impact=f"{num(coll['TotGen']) - expected:,.2f}",
                  basis="Gegevensspecificaties, hoofdstuk 4",
                  control="B-02")
        else:
            f.ok("B-02", "Return consistency",
                 "TotGen equals TotTeBet plus the correction saldi",
                 "collective")

    for tag, val in coll.items():
        if num(val, None) is not None and num(val) < 0:
            f.add("Major", "Return consistency",
                  f"Negative amount in collective field {tag}.",
                  evidence=f"{num(val):,.2f}")


def check_premiums(coll, recs, year, f):
    rates = RATES[year]
    checks = [
        ("Aof hoog", "TotPrlnAofAnwHg", "TotPrAofHg", rates["AofHg"]),
        ("Aof laag", "TotPrlnAofAnwLg", "TotPrAofLg", rates["AofLg"]),
        ("Opslag Wko", "TotPrlnAofAnwHg", "TotOpslWko", rates["Wko"]),
        ("AWf laag", "TotPrlnAwfAnwLg", "TotPrAwfLg", rates["AwfLg"]),
        ("AWf hoog", "TotPrlnAwfAnwHg", "TotPrAwfHg", rates["AwfHg"]),
        ("AWf herzien", "TotPrlnAwfAnwHz", "TotPrAwfHz", rates["AwfHz"]),
    ]
    n = max(len(recs), 1)
    collective_tol = max(TOLERANCE, 0.10 * n)   # per-IKV rounding accumulates
    for label, base_tag, prem_tag, rate in checks:
        if base_tag not in coll or prem_tag not in coll:
            continue
        base, declared = num(coll[base_tag]), num(coll[prem_tag])
        expected = base * rate
        diff = declared - expected
        if abs(diff) > collective_tol and base > 0:
            ratio = declared / (base * rate)
            if 1.05 < ratio < 1.40:
                f.add("Critical", "Employer premiums",
                      f"{label} is {ratio:.3f} times the amount its own "
                      f"declared premium wage supports. A uniform overshoot "
                      f"across independent bases is the signature of a premium "
                      f"computed on one base and an aanwas declared on "
                      f"another — typically a run-level base against a "
                      f"period-level aanwas. Test against the run-level base "
                      f"before treating this as an independent exposure; if it "
                      f"reconciles there, it is a second consequence of the "
                      f"period-integrity finding and must not be reported as a "
                      f"separate euro impact.",
                      evidence=f"base {base:,.2f}; declared {declared:,.2f}; "
                               f"at {rate * 100:.2f}% {expected:,.2f}",
                      impact=f"{diff:,.2f} — provisional, see the finding text",
                      basis=f"Handboek Loonheffingen {year}, Tabel 9",
                      control="E-01")
                continue
        if abs(diff) > collective_tol:
            f.add("Critical", "Employer premiums",
                  f"{label} does not recalculate from its declared premium "
                  f"wage at {rate * 100:.2f}%.",
                  evidence=f"base {base:,.2f}; declared {declared:,.2f}; "
                           f"expected {expected:,.2f}",
                  impact=f"{diff:,.2f}",
                  basis=f"Handboek Loonheffingen {year}, Tabel 9 / 12")

    # Zvw employer levy has no declared premium-wage rubriek of its own, so it
    # cannot be recalculated from the collective block. LnSV is not the Zvw
    # base: the maximum bijdrageloon is applied separately and per employee,
    # and IKVs on a Zvw code other than K carry a different treatment.
    if "TotWghZvw" in coll:
        f.add("Observation", "Employer premiums",
              "Werkgeversheffing Zvw cannot be recalculated from the "
              "collective block: the return carries no Zvw premium-wage "
              "rubriek, and Loon SV is not the Zvw base. Recalculate per "
              "employee against the capped bijdrageloon and the Zvw code.",
              evidence=f"declared {num(coll['TotWghZvw']):,.2f}",
              basis=f"Handboek Loonheffingen {year}, Tabel 11 / 12")

    # Whk: no published rate, and no L-code for a zero premium.
    if "TotPrlnWhkAnw" in coll and "TotPrGediffWhk" in coll:
        base, declared = num(coll["TotPrlnWhkAnw"]), num(coll["TotPrGediffWhk"])
        if base > 0:
            implied = declared / base
            f.add("Observation", "Employer premiums",
                  f"Whk implied rate is {implied * 100:.3f}% "
                  f"(premium {declared:,.2f} over base {base:,.2f}). Whk is set "
                  f"per employer by beschikking, which was not supplied, so "
                  f"this rate is inferred and not verified. Note there is no "
                  f"L-code for a zero Whk premium against a non-zero base, so "
                  f"this passes the Belastingdienst gate regardless.",
                  basis="Art. 20 and art. 34(2) Wfsv; art. 3.18 Regeling Wfsv")

    # Zero premium against a non-zero base. L2341-L2343, L2401-L2405, L2268.
    zero_checks = [
        ("Aof laag", "PrlnAofAnwLg", "PrAofLg", "L2341"),
        ("Aof hoog", "PrlnAofAnwHg", "PrAofHg", "L2342"),
        ("AWf laag", "PrlnAwfAnwLg", "PrAwfLg", "L2401"),
        ("AWf hoog", "PrlnAwfAnwHg", "PrAwfHg", "L2402"),
        ("AWf herzien", "PrlnAwfAnwHz", "PrAwfHz", "L2403"),
        ("Whk", "PrlnWhkAnw", "PrGediffWhk", "none"),
    ]
    for label, base_tag, prem_tag, code in zero_checks:
        hits = [r for r in recs
                if num(first(r, base_tag)) >= 1 and num(first(r, prem_tag)) == 0]
        if hits:
            total_base = sum(num(first(r, base_tag)) for r in hits)
            note = ("" if code != "none" else
                    " No L-code covers this for Whk; it passes the gate "
                    "silently and is still owed by the employer.")
            f.add("Critical", "Employer premiums",
                  f"{len(hits)} income relations declare a {label} premium wage "
                  f"of €1 or more with a premium of zero.{note}",
                  evidence=f"total premium wage {total_base:,.2f}",
                  basis="Art. 20 Wfsv",
                  control=code if code != "none" else "no control exists")


def check_premium_on_aow(recs, period_dates, year, f):
    """E-10: premium charged where the employee was already at AOW age.

    L2322, L2328 and L2337 test the AANWAS, not the premium. No official
    control covers a premium charged with a nil aanwas.
    """
    start = period_dates[0] if period_dates else None
    if not start:
        return
    hits = []
    for r in recs:
        if not reached_aow(first(r, "Gebdat", "GebDat"), start,
                           RATES[year]["aow_leeftijd_jaren"]):
            continue
        prem = sum(num(first(r, t)) for t in
                   ("PrAofHg", "PrAofLg", "PrAwfLg", "PrAwfHg", "PrAwfHz",
                    "OpslWko", "PrGediffWhk"))
        if abs(prem) > 0.005:
            hits.append((first(r, "PersNr"), prem))
    if hits:
        f.add("Critical", "Employer premiums",
              f"{len(hits)} income relations are charged employee-insurance "
              f"premiums for an employee who had already reached AOW age at "
              f"the period start. L2322, L2328 and L2337 test the aanwas, not "
              f"the premium, so no official control catches this.",
              evidence="; ".join(f"{h[0]} {h[1]:,.2f}" for h in hits[:25]),
              impact=f"{sum(h[1] for h in hits):,.2f}",
              basis="Wet financiering sociale verzekeringen; Handboek Tabel 9",
              control="E-10 — no control exists")
    else:
        f.ok("E-10", "Employer premiums",
             "No premium charged on an employee at AOW age",
             f"{len(recs)} IKVs")


def check_indicators(recs, period_dates, year, f):
    rates = RATES[year]
    start = period_dates[0] if period_dates else None
    aow_ww, aow_wao, aow_aanwas = [], [], []
    no_reden, srtiv_loonsv, no_bsn, arbk_groen = [], [], [], []

    for r in recs:
        pid = first(r, "PersNr", "SofiNr") or "?"
        birth = first(r, "Gebdat", "GebDat")
        aow = reached_aow(birth, start, rates["aow_leeftijd_jaren"]) if start else None
        srtiv = str(first(r, "SrtIV", "CdSrtIV") or "")
        tabel = str(first(r, "LbTab", "CdLbTab") or "")

        if aow:
            if str(first(r, "IndWW") or "").upper() == "J":
                aow_ww.append(pid)
            if str(first(r, "IndWAO") or "").upper() == "J":
                aow_wao.append(pid)
            if any(num(first(r, t)) != 0 for t in
                   ("PrlnAwfAnwLg", "PrlnAwfAnwHg", "PrlnAwfAnwHz",
                    "PrlnAofAnwLg", "PrlnAofAnwHg", "PrlnWhkAnw")):
                aow_aanwas.append(pid)

        # L2501 applies only to SrtIV 11, 13 and 15; for other codes L2024
        # forbids the field (Gegevensspecificaties 2026, p. 64).
        if srtiv in ("11", "13", "15") and first(r, "DatEind", "DatEindIkv") \
                and not first(r, "CdRdnEindArbov", "CdRdnEindArbVerh"):
            no_reden.append(pid)

        if srtiv in LOONSV_ZERO_SRTIV and num(first(r, "LnSV")) != 0:
            srtiv_loonsv.append(pid)

        if tabel and tabel not in BSN_EXEMPT_TABELCODE and not first(r, "SofiNr"):
            no_bsn.append(pid)

        # L2505: arbeidskorting requires a white table (2nd digit 1).
        if num(first(r, "VerrArbKrt")) > 0:
            if len(tabel) == 3 and tabel[1] != "1" and tabel not in (
                    "210", "220", "221", "224", "225", "226", "227", "228",
                    "940", "950", "999"):
                arbk_groen.append(pid)

    def report(ids, sev, area, msg, basis, control):
        if ids:
            f.add(sev, area, msg.format(n=len(ids)),
                  evidence="; ".join(str(i) for i in ids[:25])
                          + (" ..." if len(ids) > 25 else ""),
                  basis=basis, control=control)

    passed = [("G-01", "Insured status", "No WW/WAO indicator J at AOW age",
               aow_ww + aow_wao + aow_aanwas),
              ("I-01", "Leavers", "Reden einde code supplied with every end date",
               no_reden),
              ("C-04", "Wage basis", "Loon SV zero where the SrtIv requires it",
               srtiv_loonsv),
              ("D-09", "Identity", "BSN present where the tabelcode requires it",
               no_bsn),
              ("D-08", "Tax table", "Arbeidskorting only on a white tabelcode",
               arbk_groen)]
    for ctrl, area, label, ids in passed:
        if not ids:
            f.ok(ctrl, area, label, f"{len(recs)} IKVs")

    report(aow_ww, "Critical", "Insured status",
           "{n} income relations declare IndWW = J for an employee who had "
           "reached AOW age at the period start.",
           "Wet financiering sociale verzekeringen", "L1315")
    report(aow_wao, "Critical", "Insured status",
           "{n} income relations declare IndWAO = J for an employee who had "
           "reached AOW age at the period start.",
           "Wet financiering sociale verzekeringen", "L1314")
    report(aow_aanwas, "Critical", "Insured status",
           "{n} income relations carry a non-zero premium wage for an employee "
           "already at AOW age at the period start.",
           "Wet financiering sociale verzekeringen", "L2322 / L2328 / L2337")
    report(no_reden, "Critical", "Leavers",
           "{n} income relations supply a datum einde inkomstenverhouding with "
           "no code reden einde arbeidsverhouding.",
           "Gegevensspecificaties, rubriek Code reden einde arbeidsverhouding",
           "L2501")
    report(srtiv_loonsv, "Major", "Wage basis",
           "{n} income relations report Loon SV other than zero against a code "
           "soort inkomstenverhouding that requires zero.",
           "Gegevensspecificaties, rubriek Loon SV", "L2208")
    report(no_bsn, "Critical", "Identity",
           "{n} income relations have no BSN while the code loonbelastingtabel "
           "does not exempt it. Absent a BSN the anoniementarief applies.",
           "Art. 26b Wet LB 1964", "L2287")
    report(arbk_groen, "Critical", "Tax table",
           "{n} income relations report verrekende arbeidskorting above zero "
           "while the code loonbelastingtabel is not a white table.",
           "Gegevensspecificaties, rubriek Verrekende arbeidskorting", "L2505")


def check_awf_contract(recs, f):
    """L2201 / L2225 / L2302 — AWf laag needs the J-J-N indicator set."""
    laag_wrong, hoog_wrong, hz_wrong, missing = [], [], [], []
    for r in recs:
        pid = first(r, "PersNr", "SofiNr") or "?"
        onbep = str(first(r, "IndArbovOnbepTd", "IndArbovkOnbepTijd") or "").upper()
        schrift = str(first(r, "IndSchriftArbov", "IndSchriftArbovk") or "").upper()
        oproep = str(first(r, "IndOprov", "IndOprovk") or "").upper()
        srtiv = str(first(r, "SrtIV", "CdSrtIV") or "")
        aard = str(first(r, "CdAard", "CdAardArbVerh") or "")
        jjn = (onbep == "J" and schrift == "J" and oproep == "N")

        if not (onbep and schrift and oproep):
            if num(first(r, "PrlnAwfAnwLg")) > 0:
                missing.append(pid)
            continue
        if num(first(r, "PrlnAwfAnwLg")) != 0:
            if not jjn or aard == "83" or srtiv in BENEFIT_SRTIV:
                laag_wrong.append(pid)
        if num(first(r, "PrlnAwfAnwHg")) != 0 and jjn:
            hoog_wrong.append(pid)
        if num(first(r, "PrlnAwfAnwHz")) != 0 and not jjn:
            hz_wrong.append(pid)

    if not (laag_wrong or hoog_wrong or hz_wrong or missing):
        f.ok("F-01", "AWf classification",
             "AWf laag/hoog/herzien consistent with the contract indicators",
             f"{len(recs)} IKVs")
    if laag_wrong:
        f.add("Critical", "AWf classification",
              f"{len(laag_wrong)} income relations carry AWf laag premium wage "
              f"while the contract indicators, aard or SrtIv imply it must be "
              f"zero.",
              evidence="; ".join(laag_wrong[:25]),
              basis="Wfsv, premiedifferentiatie AWf", control="L2201")
    if hoog_wrong:
        f.add("Major", "AWf classification",
              f"{len(hoog_wrong)} income relations carry AWf hoog premium wage "
              f"while the contract indicators are J-J-N, i.e. they qualify for "
              f"the low premium.",
              evidence="; ".join(hoog_wrong[:25]),
              basis="Wfsv, premiedifferentiatie AWf", control="L2225")
    if hz_wrong:
        f.add("Major", "AWf classification",
              f"{len(hz_wrong)} income relations carry AWf herzien while the "
              f"contract indicators are not J-J-N.",
              evidence="; ".join(hz_wrong[:25]),
              basis="Wfsv, herzieningssituaties AWf", control="L2302")
    if missing:
        f.add("Major", "AWf classification",
              f"{len(missing)} income relations carry AWf laag premium wage "
              f"with one or more contract indicators absent. The low premium "
              f"cannot be substantiated for these records.",
              evidence="; ".join(missing[:25]),
              basis="Wfsv, premiedifferentiatie AWf", control="L2201")


def check_zvw(recs, f):
    bijdr, l1911, l2509 = [], [], []
    for r in recs:
        pid = first(r, "PersNr", "SofiNr") or "?"
        code = str(first(r, "CdZvw", "CdVerzSitZvw") or "").upper()
        if num(first(r, "BijdrZvw", "IngBijdrZvw")) != 0 and code != "M":
            bijdr.append(pid)
        if code == "L" and num(first(r, "WghZvw")) != 0:
            l1911.append(pid)
        if str(first(r, "SrtIV", "CdSrtIV") or "") == "17" and \
                num(first(r, "WghZvw")) != 0:
            l2509.append(pid)
    if not (bijdr or l1911 or l2509):
        f.ok("G-06", "Zvw",
             "Zvw code consistent with bijdrage, levy and SrtIv",
             f"{len(recs)} IKVs")
    for ids, msg, code in (
        (bijdr, "report an ingehouden bijdrage Zvw while the code "
                "verzekeringssituatie Zvw is not M", "L1310"),
        (l1911, "carry Zvw code L (0%-tarief) with a non-zero "
                "werkgeversheffing Zvw", "L1911"),
        (l2509, "carry SrtIv 17 (DGA not insured) with a non-zero "
                "werkgeversheffing Zvw", "L2509"),
    ):
        if ids:
            f.add("Major", "Zvw", f"{len(ids)} income relations {msg}.",
                  evidence="; ".join(ids[:25]),
                  basis="Zorgverzekeringswet", control=code)


def check_bt_upload(path, f):
    """Test uploaded bijzonder-tarief overrides against the table's valid cells."""
    try:
        import pandas as pd
    except ImportError:
        f.skip("Bijzondere beloningen", "pandas unavailable; upload not tested")
        return
    valid = set()
    for row in BB_2025:
        valid.add(round(row[1], 2))
        valid.add(round(row[2] + row[3], 2))
        valid.add(round(row[4], 2))
        valid.add(round(row[5] + row[6], 2))
        valid.add(round(row[7] + row[8], 2))
    for _, v in BB_2025_AOW_PRE46.items():
        valid.add(round(v[0], 2))
        valid.add(round(v[1] + v[2], 2))
        valid.add(round(v[3] + v[4], 2))

    df = pd.read_excel(path)
    col = next((c for c in df.columns if "amount" in str(c).lower()), None)
    if col is None:
        f.skip("Bijzondere beloningen", f"no amount column found in {path}")
        return
    vals = sorted({round(float(v), 2) for v in df[col].dropna()})
    bad = [v for v in vals if v not in valid]
    f.add("Observation", "Bijzondere beloningen",
          f"Bijzonder-tarief percentages are supplied to the engine as an "
          f"upload ({len(df)} rows, {len(vals)} distinct values). Because the "
          f"rate is an override, the engine never derives it and a wrong value "
          f"will not self-correct in any period. Test each against the "
          f"employee's date of birth, loonheffingskorting and "
          f"alleenstaandeouderenkorting status.",
          evidence=f"distinct values: {', '.join(f'{v:.2f}' for v in vals)}")
    if bad:
        f.add("Critical", "Bijzondere beloningen",
              f"{len(bad)} uploaded percentages are not cells of the witte "
              f"tabel bijzondere beloningen.",
              evidence=", ".join(f"{v:.2f}" for v in bad),
              basis="Belastingdienst, witte tabel bijzondere beloning, "
                    "uitgave januari 2025")
    else:
        f.add("Observation", "Bijzondere beloningen",
              "Every uploaded percentage is a valid cell of the table. That "
              "does not mean each is the correct cell for its employee — a "
              "valid percentage from the wrong age or korting column is the "
              "commonest defect here, and it is invisible at this level.")


def check_sepa(path, f):
    try:
        root = ET.parse(path).getroot()
    except ET.ParseError as e:
        f.skip("Payments", f"SEPA file could not be parsed: {e}")
        return
    nb = ctrl = None
    txs = []
    for el in root.iter():
        t = ns_strip(el.tag)
        if t == "NbOfTxs" and nb is None:
            nb = el.text
        elif t == "CtrlSum" and ctrl is None:
            ctrl = el.text
        elif t == "InstdAmt":
            txs.append(num(el.text))
    if nb is not None and int(num(nb)) != len(txs):
        f.add("Critical", "Payments",
              "SEPA group header NbOfTxs does not equal the transaction count.",
              evidence=f"header {nb}; counted {len(txs)}",
              basis="ISO 20022 pain.001")
    if (nb is not None and int(num(nb)) == len(txs) and ctrl is not None
            and abs(num(ctrl) - sum(txs)) <= 0.01):
        f.ok("K-01 / K-02", "Payments",
             "SEPA header transaction count and control sum both tie",
             f"{len(txs)} transactions")
    if ctrl is not None and abs(num(ctrl) - sum(txs)) > 0.01:
        f.add("Critical", "Payments",
              "SEPA group header CtrlSum does not equal the sum of the "
              "instructed amounts.",
              evidence=f"header {num(ctrl):,.2f}; summed {sum(txs):,.2f}",
              impact=f"{num(ctrl) - sum(txs):,.2f}",
              basis="ISO 20022 pain.001")



def check_loon_sv_basis(recs, year, f):
    """C-01 / C-02: LnSV is the SV wage BEFORE the maximum premieloon."""
    cap = RATES[year]["max_premieloon_tijdvak"][FREQ]
    hits = []
    for r in recs:
        lnsv = num(first(r, "LnSV"))
        lnlb = num(first(r, "LnLbPh"))
        if abs(lnsv - cap) < 0.005 and lnlb > cap + 0.01:
            hits.append((first(r, "PersNr"), lnlb, lnsv, lnlb - cap))
    if hits:
        f.add("Critical", "Wage basis",
              f"{len(hits)} income relations declare Loon SV at exactly the "
              f"{FREQ} maximum premieloon of {cap:,.2f} while Loon LB/PH "
              f"exceeds it. Loon SV is kolom 8 of the loonstaat, the SV wage "
              f"before the maximum is applied; the cap belongs in the aanwas "
              f"fields, not in Loon SV. Capping it understates the UWV dagloon "
              f"base.",
              evidence="; ".join(f"{h[0]} LnLbPh {h[1]:,.2f}" for h in hits[:20]),
              impact=f"{sum(h[3] for h in hits):,.2f}",
              basis="Gegevensspecificaties, rubriek Loon SV; Handboek "
                    "Loonheffingen, hoofdstuk 5 (VCR)",
              control="C-01 / C-02")
    else:
        f.ok("C-01", "Wage basis",
             "Loon SV not capped at the period maximum", f"{len(recs)} IKVs")


def check_verloonde_uren(recs, f):
    """H-01 to H-03."""
    vals = collections.Counter(first(r, "AantVerlU") for r in recs)
    zero = [first(r, "PersNr") for r in recs if num(first(r, "AantVerlU")) == 0]
    top, topn = (vals.most_common(1) or [(None, 0)])[0]
    share = topn / max(len(recs), 1)
    if share > 0.5:
        f.add("Major", "Verloonde uren",
              f"{topn} of {len(recs)} income relations ({share:.0%}) declare "
              f"the same verloonde uren value of {top}, across only "
              f"{len(vals)} distinct values in the whole population. The "
              f"rubriek requires the hours actually verloond in the tijdvak, "
              f"not contract hours.",
              evidence=f"distinct values: {sorted(v for v in vals if v)[:12]}",
              basis="Gegevensspecificaties, rubriek Aantal verloonde uren",
              control="H-01 / H-02")
    else:
        f.ok("H-01", "Verloonde uren", "Hours vary across the population",
             f"{len(recs)} IKVs")
    if zero:
        f.add("Observation", "Verloonde uren",
              f"{len(zero)} income relations declare zero verloonde uren.",
              evidence="; ".join(str(z) for z in zero[:25]), control="H-03")


def check_wko_and_whk_rate(recs, year, f):
    """E-04 / E-05."""
    wko = RATES[year]["Wko"]
    bad = []
    for r in recs:
        base = num(first(r, "PrlnAofAnwHg")) + num(first(r, "PrlnAofAnwLg"))
        if base <= 0:
            continue
        exp = round(base * wko, 2)
        dec = num(first(r, "OpslWko"))
        if abs(dec - exp) > TOLERANCE:
            bad.append((first(r, "PersNr"), base, dec, exp, dec - exp))
    if bad:
        f.add("Major", "Employer premiums",
              f"Opslag Wko does not equal {wko * 100:.2f}% of the Aof premium "
              f"wage in the same record, on {len(bad)} income relations.",
              evidence="; ".join(f"{b[0]} declared {b[2]:,.2f} expected "
                                 f"{b[3]:,.2f}" for b in bad[:20]),
              impact=f"{sum(b[4] for b in bad):,.2f}",
              basis="Handboek Loonheffingen, Tabel 9", control="E-05 / L2268")
    else:
        f.ok("E-05", "Employer premiums", "Opslag Wko ties to the Aof base",
             f"{len(recs)} IKVs")

    rates = []
    for r in recs:
        b, prem = num(first(r, "PrlnWhkAnw")), num(first(r, "PrGediffWhk"))
        if b > 0 and prem > 0:
            rates.append((first(r, "PersNr"), b, prem, prem / b))
    if len(rates) > 5:
        modal = collections.Counter(round(x[3], 6) for x in rates).most_common(1)[0][0]
        off = [x for x in rates if abs(x[3] - modal) > 0.00005]
        if off:
            f.add("Major", "Employer premiums",
                  f"Whk premium is inconsistent with the rate applied to the "
                  f"other {len(rates) - len(off)} records "
                  f"({modal * 100:.4f}%), on {len(off)} income relations.",
                  evidence="; ".join(f"{o[0]} {o[3] * 100:.4f}%" for o in off[:20]),
                  impact=f"{sum(o[2] - o[1] * modal for o in off):,.2f}",
                  basis="Art. 20 Wfsv; rate inferred, beschikking not supplied",
                  control="E-04")
        else:
            f.ok("E-04", "Employer premiums",
                 f"Whk rate consistent at {modal * 100:.4f}% (inferred)",
                 f"{len(rates)} IKVs carrying a premium")


def check_leavers_and_contract_fields(recs, f):
    """I-02, H-04, H-05."""
    code99 = [first(r, "PersNr") for r in recs
              if str(first(r, "CdRdnEindArbov", "CdRdnEindArbVerh") or "") == "99"]
    if code99:
        f.add("Major", "Leavers",
              f"{len(code99)} leavers carry reden einde code 99 (een andere, "
              f"hiervoor niet genoemde reden). Code 99 is a residual, not an "
              f"answer; each needs the specific legal ground from the "
              f"termination register.",
              evidence="; ".join(str(c) for c in code99[:25]),
              basis="Codes voor de aangifte loonheffingen, Code reden einde "
                    "arbeidsverhouding", control="I-02")
    if not code99:
        f.ok("I-02", "Leavers", "No reden einde code 99 used as a fallback",
             f"{len(recs)} IKVs")
    req = {"11", "13", "15", "17"}
    noc = [first(r, "PersNr") for r in recs
           if str(first(r, "SrtIV", "CdSrtIV") or "") in req
           and not first(r, "Ctrctln")]
    noh = [first(r, "PersNr") for r in recs
           if str(first(r, "SrtIV", "CdSrtIV") or "") in req
           and not first(r, "AantCtrcturenPWk")]
    if not (noc or noh):
        f.ok("H-04 / H-05", "Contract data",
             "Contractloon and contracturen supplied where mandatory",
             f"{len(recs)} IKVs")
    for ids, label, ctrl in ((noc, "Contractloon", "H-04 / 1615"),
                             (noh, "Aantal contracturen per week", "H-05 / 1614")):
        if ids:
            f.add("Major", "Contract data",
                  f"{label} is not supplied on {len(ids)} income relations "
                  f"where the code soort inkomstenverhouding makes it "
                  f"mandatory.",
                  evidence="; ".join(str(i) for i in ids[:25]),
                  basis="Gegevensspecificaties, Poortcontrole overig",
                  control=ctrl)


def check_retro(path, coll, year, f):
    """A-07: tie the period block and correction saldi to the retro export."""
    try:
        import pandas as pd
    except ImportError:
        f.skip("Retro reconciliation", "pandas unavailable", "A-07")
        return
    df = pd.read_excel(path)
    df.columns = [str(c).strip() for c in df.columns]
    if "Processing Period Name" not in df.columns or "Account" not in df.columns:
        f.skip("Retro reconciliation",
               "Export lacks a Processing Period Name or Account column",
               "A-07")
        return
    per = df["Processing Period Name"].astype(str)
    cur_name = per.value_counts().idxmax()
    cur = df[per == cur_name]
    prior = df[per.str.match(r"Period \d+", na=False) & (per < cur_name)]

    def tot(d, accts):
        return d[d["Account"].isin(accts)]["Amount"].sum()

    lh_retro = tot(prior, [2552, 2572])
    lh_cur = tot(cur, [2552, 2572])
    sv_retro, sv_cur = tot(prior, [58551]), tot(cur, [58551])

    declared_lh = num(coll.get("IngLbPh"))
    declared_sv = num(coll.get("TotLnSV"))
    if abs((lh_retro + lh_cur) - declared_lh) < max(1000.0, declared_lh * 0.002):
        f.add("Critical", "Period integrity",
              f"The period block contains the retro. Loon SV of "
              f"{declared_sv:,.2f} splits into {sv_cur:,.2f} for {cur_name} "
              f"and {sv_retro:,.2f} of retro from prior periods; loonheffing "
              f"of {declared_lh:,.2f} splits into {lh_cur:,.2f} and "
              f"{lh_retro:,.2f}. Whether this is correct depends on the "
              f"systematiek — see systematiek-determination.md.",
              evidence=f"retro export {os.path.basename(path)}",
              impact=f"{lh_retro:,.2f}",
              basis="Handboek Loonheffingen §9.2 / §9.2.1", control="A-07")

    saldi = num(coll.get("_saldi_total"))
    if saldi:
        rate = (RATES[year]["AofHg"] + RATES[year]["Wko"] +
                RATES[year]["AwfLg"] + RATES[year]["WghZvw"] + 0.0033)
        expected = lh_retro + sv_retro * rate
        resid = saldi - expected
        pct = abs(resid) / saldi if saldi else 0
        verdict = ("reconciles" if pct < 0.01 else
                   "does NOT reconcile — something else is inside the "
                   "correction blocks")
        f.add("Critical" if pct >= 0.01 else "Observation", "Period integrity",
              f"Correction saldi {verdict}. Saldi {saldi:,.2f} against retro "
              f"loonheffing {lh_retro:,.2f} plus employer premiums of "
              f"{sv_retro * rate:,.2f} on a retro SV base of {sv_retro:,.2f} "
              f"at {rate * 100:.2f}%. Residual {resid:,.2f} ({pct:.2%}).",
              evidence=f"retro export {os.path.basename(path)}",
              impact=f"{saldi:,.2f}", control="A-07")

    fut = df[per.isin(["Period 10", "Period 11", "Period 12", "Period 13"])]
    if len(fut):
        f.add("Observation", "Retro export",
              f"{len(fut)} rows are tagged to periods later than the period "
              f"under review.",
              evidence=", ".join(sorted(fut["Processing Period Name"].unique())),
              control="A-07")



# --- Bijzondere beloningen: inverted table -------------------------------
# Combined percentage -> the column it can legitimately appear in.
# Columns: U+ under AOW with LHK, U- under AOW without, A+ AOW with LHK
# (excl. AOK), A- AOW without. 2025 Nederland Standaard.
BB_COLUMNS_2025 = {
    "U+": {0.00, 27.77, 5.79, 33.56, 39.90, 41.56, 50.33, 56.01, 49.50},
    "U-": {35.82, 37.48, 49.50},
    "A+": {0.00, 19.96, 39.52, 43.91, 58.91, 52.76, 49.50},
    "A-": {17.92, 37.48, 49.50},
}
# Jaarloon band implied by each combined percentage, for the plausibility test.
BB_BANDS_2025 = {
    "U+": [(0, 0, 11049), (27.77, 11050, 13143), (5.79, 13144, 24341),
           (33.56, 24342, 28406), (39.90, 28407, 38441),
           (41.56, 38442, 43071), (50.33, 43072, 76817),
           (56.01, 76818, 139404), (49.50, 139405, None)],
    "U-": [(35.82, 0, 38441), (37.48, 38442, 76817), (49.50, 76818, None)],
}


def _norm_id(x):
    return re.sub(r"\.0$", "", str(x).strip())


def _bb_column(rec, period_start, year):
    aow = reached_aow(first(rec, "Gebdat", "GebDat"), period_start,
                      RATES[year]["aow_leeftijd_jaren"])
    lhk = str(first(rec, "IndLhKort") or "").upper() == "J"
    if aow is None:
        return None
    return ("A+" if lhk else "A-") if aow else ("U+" if lhk else "U-")


def check_bt(bt_path, retro_path, recs, period_dates, year, f):
    """Bijzondere beloningen: conformity, column membership, upload structure.

    The percentage is a CLIENT-SUPPLIED INPUT via the upload. Derivation of the
    bracket from jaarloon is therefore out of scope. What is in scope is whether
    payroll applied the rate that was supplied.
    """
    try:
        import pandas as pd
    except ImportError:
        f.skip("Bijzondere beloningen", "pandas unavailable", "D-06")
        return
    up = pd.read_excel(bt_path)
    col = next((c for c in up.columns if "amount" in str(c).lower()), None)
    idc = next((c for c in up.columns if "id" in str(c).lower()), None)
    if col is None or idc is None:
        f.skip("Bijzondere beloningen",
               f"Upload {os.path.basename(bt_path)} lacks an id or amount "
               f"column", "D-06")
        return
    supplied = {_norm_id(a): round(float(b), 2)
                for a, b in zip(up[idc], up[col]) if pd.notna(b)}

    # --- D-03: column membership (client-input defect) ---
    start = period_dates[0] if period_dates else None
    wrong, unknown = [], 0
    for r in recs:
        pid = _norm_id(first(r, "PersNr") or "")
        pct = supplied.get(pid)
        if pct is None:
            continue
        c = _bb_column(r, start, year) if start else None
        if c is None:
            unknown += 1
            continue
        if pct not in BB_COLUMNS_2025[c]:
            wrong.append((pid, pct, c))
    if wrong:
        f.add("Critical", "Bijzondere beloningen",
              f"{len(wrong)} supplied bijzonder-tarief percentages do not "
              f"exist anywhere in the table column that applies to the "
              f"employee's age and loonheffingskorting status. A percentage "
              f"can be a valid cell of the table and still be the wrong cell. "
              f"This is a defect in the client-supplied input, not in the "
              f"calculation.",
              evidence="; ".join(f"{w[0]} {w[1]:.2f}% against column {w[2]}"
                                 for w in wrong[:25]),
              basis="Belastingdienst, witte tabel bijzondere beloning "
                    "Nederland Standaard, uitgave januari 2025",
              control="D-03")
    else:
        f.ok("D-03", "Bijzondere beloningen",
             "Every supplied percentage sits in the applicable column",
             f"{len(supplied)} uploaded rows")
    if unknown:
        f.skip("Bijzondere beloningen column test",
               f"{unknown} income relations have no date of birth in the "
               f"return, so the applicable column cannot be determined.",
               "D-03")

    # --- D-07: conformity of applied rate to supplied rate ---
    if not retro_path:
        f.skip("Bijzondere beloningen conformity (D-07)",
               "Transaction-level pay-element export not supplied. The rate "
               "actually applied cannot be derived, so conformity of the "
               "applied rate to the client-supplied rate is untested.", "D-07")
    else:
        rt = pd.read_excel(retro_path)
        rt.columns = [str(c).strip() for c in rt.columns]
        if "Account" not in rt.columns:
            f.skip("Bijzondere beloningen conformity (D-07)",
                   "Retro export lacks an Account column.", "D-07")
        else:
            per = rt["Processing Period Name"].astype(str)
            cur = per.value_counts().idxmax()
            sel = rt[(per == cur) & (rt["Account"] == 2572)].copy()
            sel["_id"] = sel[[c for c in sel.columns
                              if "employee" in str(c).lower()][0]].map(_norm_id)
            applied = sel.groupby("_id")["Amount"].sum().to_dict()

            mism, notax, nosup, matched = [], [], [], 0
            for r in recs:
                pid = _norm_id(first(r, "PersNr") or "")
                base = num(first(r, "LnTabBB"))
                if base <= 0.02:
                    continue
                tax, sup = applied.get(pid), supplied.get(pid)
                if tax is None:
                    notax.append((pid, base, sup))
                elif sup is None:
                    nosup.append((pid, base, round(tax / base * 100, 2)))
                else:
                    eff = round(tax / base * 100, 2)
                    if abs(eff - sup) > 0.05:
                        mism.append((pid, base, sup, eff, base * (sup - eff) / 100))
                    else:
                        matched += 1
            if notax:
                f.add("Critical", "Bijzondere beloningen",
                      f"{len(notax)} income relations declare a bijzondere "
                      f"beloningen wage with no special-rate tax element "
                      f"produced in the period. The client-supplied "
                      f"percentage was therefore not demonstrably applied, "
                      f"and the declared LnTabBB is uncorroborated. Confirm "
                      f"against the payslip before concluding: the tax may be "
                      f"folded into the regular element, or the export may be "
                      f"incomplete.",
                      evidence="; ".join(f"{n[0]} base {n[1]:,.2f} "
                                         f"supplied {n[2]}" for n in notax[:25]),
                      basis="Handboek Loonheffingen §9.3.6", control="D-07")
            if mism:
                f.add("Critical", "Bijzondere beloningen",
                      f"{len(mism)} income relations were taxed at a rate "
                      f"other than the percentage the client supplied.",
                      evidence="; ".join(f"{m[0]} supplied {m[2]:.2f}% "
                                         f"applied {m[3]:.2f}% on {m[1]:,.2f}"
                                         for m in mism[:25]),
                      impact=f"{sum(m[4] for m in mism):,.2f}",
                      basis="Client-supplied input, pay element 52572",
                      control="D-07")
            if nosup:
                f.add("Major", "Bijzondere beloningen",
                      f"{len(nosup)} income relations were taxed at a "
                      f"special rate with no percentage supplied for them.",
                      evidence="; ".join(f"{n[0]} applied {n[2]:.2f}%"
                                         for n in nosup[:25]),
                      control="D-07")
            if matched and not (mism or nosup):
                f.ok("D-07", "Bijzondere beloningen",
                     "Applied rate equals the client-supplied rate",
                     f"{matched} IKVs with a bb base")

    # --- D-10: upload structure ---
    if "Start date" in up.columns and "End date" not in up.columns:
        f.add("Major", "Bijzondere beloningen",
              f"The bijzonder-tarief upload carries a start date but no end "
              f"date on any of its {len(up)} rows. A rate set once cannot be "
              f"ended, so it follows an employee across an AOW transition or "
              f"a change of loonheffingskorting status and will not "
              f"self-correct in any later period.",
              basis="Client configuration", control="D-10")
    nosupply = [_norm_id(first(r, "PersNr") or "") for r in recs
                if _norm_id(first(r, "PersNr") or "") not in supplied
                and num(first(r, "LnTabBB")) > 0.02]
    if nosupply:
        f.add("Observation", "Bijzondere beloningen",
              f"{len(nosupply)} income relations have a bijzondere beloningen "
              f"wage but no row in the upload. The derivation used for them "
              f"needs documenting.",
              evidence="; ".join(nosupply[:25]), control="D-10")

    f.skip("Bijzonder-tarief bracket derivation",
           "OUT OF SCOPE. The percentage is supplied by the client through pay "
           "element 52572 and is treated as an input, not as a calculation. "
           "Whether the supplied percentage is the correct jaarloon bracket "
           "cannot be verified while Jaarloon BT is not produced, and is not "
           "part of this assurance. Conformity of the applied rate to the "
           "supplied rate, and membership of the applicable column, are "
           "tested and reported separately.", "D-11")


def check_aok_materiality(recs, period_dates, year, f):
    """D-12: close the alleenstaandeouderenkorting question where it cannot bite.

    The incl.-AOK and excl.-AOK columns diverge only at jaarloon rows 34.001
    and 38.442. Outside those bands the distinction is immaterial.
    """
    start = period_dates[0] if period_dates else None
    if not start:
        return
    aow_emps = [r for r in recs
                if reached_aow(first(r, "Gebdat", "GebDat"), start,
                               RATES[year]["aow_leeftijd_jaren"])]
    if not aow_emps:
        f.ok("D-12", "Bijzondere beloningen",
             "No AOW-age employees, so the alleenstaandeouderenkorting "
             "columns cannot apply", f"{len(recs)} IKVs")
    else:
        f.skip("Alleenstaandeouderenkorting",
               f"{len(aow_emps)} AOW-age income relations. The incl.-AOK and "
               f"excl.-AOK columns diverge only at jaarloon 34.001 and 38.442; "
               f"outside those bands the distinction is immaterial. Confirm "
               f"whether any of these employees can fall in those bands, or "
               f"obtain the AOK flag, to close this.", "D-12")


def check_zeroed_corrections(corrections, coll, f):
    """A-09: correction blocks present but all saldi zero."""
    if not corrections:
        return
    saldi_total = num(coll.get("_saldi_total"))
    if abs(saldi_total) < 0.01:
        f.add("Critical", "Period integrity",
              f"{len(corrections)} correction blocks are present and every "
              f"saldo reads zero. If the retro was also removed from the "
              f"period block, it is now declared in neither place and has "
              f"disappeared from the filing. Under loon-over the retro belongs "
              f"in the correction blocks; zeroing them while restating the "
              f"period block understates the return.",
              basis="Handboek Loonheffingen §9.2.1; hoofdstuk 14",
              control="A-09")
    else:
        f.ok("A-09", "Period integrity",
             "Correction blocks carry non-zero saldi",
             f"{len(corrections)} blocks")



def check_g2n(path, recs, year, f, period_table=None, catalogue=None,
              bt_upload=None, cumulative=False):
    """The gross-to-net is validated against statute FIRST, then becomes the
    per-employee reference every other deliverable reconciles to."""
    try:
        from g2n import load, validate, reference, parse_period_table, Result, norm_id
    except ImportError:
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        from g2n import load, validate, reference, parse_period_table, Result, norm_id
    try:
        df, meta = load(path)
    except Exception as e:
        f.skip("Gross-to-net", f"Could not read {os.path.basename(path)}: {e}",
               "L-01")
        return None
    dob = {_norm_id(first(r, "PersNr") or ""): first(r, "Gebdat", "GebDat")
           for r in recs}
    lhk = {_norm_id(first(r, "PersNr") or ""):
           str(first(r, "IndLhKort") or "").upper() == "J" for r in recs}
    bt = None
    if bt_upload:
        import pandas as pd
        u = pd.read_excel(bt_upload)
        ic = next(c for c in u.columns if "id" in str(c).lower())
        ac = next(c for c in u.columns if "amount" in str(c).lower())
        bt = {norm_id(i): float(x) for i, x in zip(u[ic], u[ac])
              if pd.notna(x)}
    rows = parse_period_table(period_table) if period_table else None
    res = Result()
    validate(df, year, res, period_rows=rows, dob=dob, lhk=lhk,
             bt_supplied=bt, catalogue=catalogue, is_period=not cumulative)
    for r in res.rows:
        if str(r["Finding"]).startswith("PASS —"):
            f.ok(r["Ref"], "Gross-to-net",
                 str(r["Finding"])[7:], f"{r['Records']} employees")
        elif str(r["Finding"]).startswith("NOT TESTED"):
            f.skip(f"Gross-to-net — {r['Area']}", str(r["Finding"])[12:].strip(" —"),
                   r["Ref"])
        else:
            sev = ("Critical" if r["Area"] in ("Employer premiums", "SV base",
                                               "Base composition",
                                               "Special-rate tax",
                                               "Regular withholding")
                   else "Major")
            f.add(sev, "Gross-to-net", r["Finding"], r["Evidence"],
                  r["Euro impact"], r["Basis"], r["Ref"])
    ref = reference(df)
    f.ok("L-00", "Gross-to-net",
         f"Statutory recalculation complete; the gross-to-net is now the "
         f"per-employee reference for the other deliverables",
         f"{len(ref)} employees")
    return ref


def reconcile_to_g2n(ref, recs, f):
    """Every other deliverable reconciles to the validated gross-to-net."""
    if ref is None:
        return
    g = {r.employee_id: r for r in ref.itertuples()}
    pairs = [("LnSV", "sv_base", "Loon SV"),
             ("LnLbPh", "tax_base", "fiscal wage"),
             ("LnTabBB", "bt_base", "bijzondere beloningen wage")]
    for tag, gcol, label in pairs:
        if gcol not in ref.columns:
            continue
        hits = []
        for r in recs:
            pid = _norm_id(first(r, "PersNr") or "")
            row = g.get(pid)
            if row is None:
                continue
            x, y = num(first(r, tag)), getattr(row, gcol, 0.0)
            if abs(x - y) > TOLERANCE:
                hits.append((pid, x, y, x - y))
        if hits:
            f.add("Critical", "XML to gross-to-net",
                  f"{len(hits)} income relations: the return's {label} does "
                  f"not equal the gross-to-net for the same employee.",
                  evidence="; ".join(f"{h[0]} XML {h[1]:,.2f} G2N {h[2]:,.2f}"
                                     for h in hits[:25]),
                  impact=f"{sum(h[3] for h in hits):,.2f}",
                  basis="Cross-deliverable reconciliation", control="X-02")
        else:
            f.ok("X-02", "XML to gross-to-net",
                 f"Return {label} equals the gross-to-net per employee",
                 f"{len(recs)} IKVs")
    missing = sorted({_norm_id(first(r, "PersNr") or "") for r in recs} - set(g))
    if missing:
        f.add("Critical", "XML to gross-to-net",
              f"{len(missing)} income relations in the return have no "
              f"gross-to-net row.", evidence="; ".join(missing[:25]),
              control="X-20")


def check_payslips(pdf_path, recs, year, f, prior_cum_path=None):
    """J-02 to J-08: cumulative footer, roll-forward, zero values, reservering."""
    try:
        from payslips import parse_pdf
    except ImportError:
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        from payslips import parse_pdf
    try:
        slips = parse_pdf(pdf_path)
    except RuntimeError as e:
        f.skip("Payslips", str(e), "J-01")
        return None
    if not slips:
        f.skip("Payslips", "No payslip pages recognised in the PDF. The layout "
                           "labels may differ from this client's template.",
               "J-01")
        return None

    by_period = collections.Counter(s_["period"] for s_ in slips)
    cur = max((p for p in by_period if p is not None), default=None)
    current = [s_ for s_ in slips if s_["period"] == cur]
    prior = [s_ for s_ in slips if s_["period"] == (cur - 1 if cur else None)]
    f.ok("J-01", "Payslips",
         f"Payslip pack parsed: {len(slips)} slips across periods "
         f"{sorted(k for k in by_period if k)}, {len(current)} for the current "
         f"period", f"{len({s_['employee_id'] for s_ in slips})} employees")

    # --- J-06: a payslip for every income relation in the return ---
    xml_ids = {_norm_id(first(r, "PersNr") or "") for r in recs}
    slip_ids = {_norm_id(s_["employee_id"]) for s_ in current}
    missing = sorted(xml_ids - slip_ids)
    if missing:
        f.add("Critical", "Payslips",
              f"{len(missing)} income relations in the return have no payslip "
              f"for the period.",
              evidence="; ".join(missing[:25]), basis="Art. 7:626 BW",
              control="J-06")
    else:
        f.ok("J-06", "Payslips", "Every income relation has a payslip",
             f"{len(xml_ids)} IKVs")

    # --- J-02: the cumulative block must roll forward ---
    pc = {_norm_id(s_["employee_id"]): s_ for s_ in prior}
    cc = {_norm_id(s_["employee_id"]): s_ for s_ in current}
    both = sorted(set(pc) & set(cc))
    if both:
        stuck = [e for e in both
                 if pc[e]["cum_fiscaal_loon"] is not None
                 and cc[e]["cum_fiscaal_loon"] is not None
                 and abs(cc[e]["cum_fiscaal_loon"]
                         - pc[e]["cum_fiscaal_loon"]) < 0.005]
        if len(stuck) > len(both) * 0.2:
            f.add("Critical", "Payslips",
                  f"The cumulative block does not roll forward. For "
                  f"{len(stuck)} of {len(both)} employees holding both a "
                  f"prior-period and a current-period payslip, the cumulative "
                  f"fiscaal loon is identical on both. A cumulative that does "
                  f"not move cannot be reconciled by the employee and carries "
                  f"no year-to-date meaning.",
                  evidence="; ".join(f"{e} {cc[e]['cum_fiscaal_loon']:,.2f} "
                                     f"on both" for e in stuck[:15]),
                  basis="Handboek Loonheffingen; art. 7:626 BW",
                  control="J-02")
        elif stuck:
            f.add("Major", "Payslips",
                  f"{len(stuck)} of {len(both)} employees show an unchanged "
                  f"cumulative fiscaal loon across two consecutive payslips.",
                  evidence="; ".join(stuck[:25]), control="J-02")
        else:
            f.ok("J-02", "Payslips", "Cumulative block rolls forward",
                 f"{len(both)} employees with consecutive slips")
    else:
        f.skip("Payslip cumulative roll-forward (J-02)",
               "The pack contains payslips for only one period, so the "
               "roll-forward cannot be tested. Supply the prior period's "
               "payslips, or a cumulative gross-to-net to the prior period "
               "end.", "J-02")

    # --- J-03 / J-04: no negative cumulative ---
    neg = [(s_["employee_id"], k, s_[k]) for s_ in current
           for k in ("cum_fiscaal_loon", "cum_loonheffing", "cum_svw_loon")
           if s_[k] is not None and s_[k] < 0]
    if neg:
        f.add("Critical", "Payslips",
              f"{len(neg)} negative cumulative values on current-period "
              f"payslips.",
              evidence="; ".join(f"{n[0]} {n[1]} {n[2]:,.2f}" for n in neg[:25]),
              basis="Handboek Loonheffingen", control="J-03 / J-04")
    else:
        f.ok("J-03 / J-04", "Payslips", "No negative cumulative values",
             f"{len(current)} slips")

    # --- J-07: footer fields that print nil across the population ---
    for key, label in (("cum_svw_loon", "SVW loon"),
                       ("jaarloon_bt", "Jaarloon BT"),
                       ("cum_arbeidskorting", "Arbeidskorting cumulatief")):
        vals = [s_[key] for s_ in slips if s_[key] is not None]
        if vals and all(abs(v) < 0.005 for v in vals):
            f.add("Major", "Payslips",
                  f"{label} prints 0,00 on all {len(vals)} payslips in the "
                  f"pack. The field is produced but never populated, so no "
                  f"reader can verify anything that depends on it.",
                  basis="Art. 7:626 BW; Handboek §9.3.6", control="J-07")

    # --- J-08: reservering block ---
    res = [s_ for s_ in current if s_["res_vakantiegeld_saldo"] is not None]
    if res:
        nil = [s_ for s_ in res if abs(s_["res_vakantiegeld_saldo"]) < 0.005]
        if len(nil) == len(res):
            f.add("Major", "Payslips",
                  f"The vakantiegeld reservation and balance print 0,00 on all "
                  f"{len(res)} current-period payslips while holiday pay "
                  f"accrues as a live element.",
                  control="J-08")
        elif nil:
            f.add("Observation", "Payslips",
                  f"{len(nil)} of {len(res)} current-period payslips show a "
                  f"nil vakantiegeld balance.",
                  evidence="; ".join(s_["employee_id"] for s_ in nil[:25]),
                  control="J-08")
        else:
            f.ok("J-08", "Payslips", "Vakantiegeld reservation populated",
                 f"{len(res)} slips")
    return slips


def write_report(f, meta, period_dates, recs, out_path):
    try:
        from openpyxl import Workbook
        from openpyxl.styles import Font
    except ImportError:
        for r in f.rows:
            print(r)
        return None
    wb = Workbook()
    ws = wb.active
    ws.title = "Cover"
    cover = [
        ("Netherlands payroll pack — deterministic validation", ""),
        ("Entity", meta.get("NmIP", "")),
        ("Loonheffingennummer", meta.get("LhNr", "")),
        ("Period", f"{period_dates[0]} to {period_dates[1]}"
                   if period_dates else ""),
        ("Belastingjaar", meta.get("namespace_year", "")),
        ("Berichtversie", meta.get("berichtversie", "")),
        ("Software package", meta.get("GebrSwPakket", "")),
        ("Income relations in period block", len(recs)),
        ("Systematiek", meta.get("systematiek") or "NOT CONFIRMED"),
        ("Report version", "v1.4"),
        ("Generated", dt.date.today().isoformat()),
        ("", ""),
        ("Scope", "Deterministic checks only. Rate lookups against the "
                  "payslip pack, cumulatives and GL mapping require the "
                  "reviewer."),
    ]
    for row in cover:
        ws.append(list(row))
    ws["A1"].font = Font(bold=True, size=13)
    for c in "AB":
        ws.column_dimensions[c].width = 46

    ws2 = wb.create_sheet("Findings Register")
    cols = ["ID", "Severity", "Area", "Finding", "Evidence", "Euro impact",
            "Statutory basis", "Control"]
    ws2.append(cols)
    for c in ws2[1]:
        c.font = Font(bold=True)
    for r in f.rows:
        ws2.append([r[c] for c in cols])
    for c, w in zip("ABCDEFGH", (8, 12, 22, 70, 46, 14, 40, 16)):
        ws2.column_dimensions[c].width = w

    wsc = wb.create_sheet("Coverage")
    wsc.append(["Control", "Area", "Check", "Population", "Result"])
    for c in wsc[1]:
        c.font = Font(bold=True)
    for r in f.coverage:
        wsc.append([r["Control"], r["Area"], r["Check"], r["Population"],
                    r["Result"]])
    for c, w in zip("ABCDE", (10, 22, 56, 22, 10)):
        wsc.column_dimensions[c].width = w

    ws3 = wb.create_sheet("Not Tested")
    ws3.append(["Control", "Area", "Reason"])
    for c in ws3[1]:
        c.font = Font(bold=True)
    for r in f.not_tested:
        ws3.append([r.get("Control", ""), r["Area"], r["Reason"]])
    for c, w in zip("ABC", (10, 30, 96)):
        ws3.column_dimensions[c].width = w

    wb.save(out_path)
    return out_path


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--xml", required=True)
    p.add_argument("--year", type=int, default=2025)
    p.add_argument("--g2n")
    p.add_argument("--sepa")
    p.add_argument("--master")
    p.add_argument("--bt-upload")
    p.add_argument("--retro")
    p.add_argument("--payslips")
    p.add_argument("--period-table")
    p.add_argument("--catalogue")
    p.add_argument("--g2n-cumulative", action="store_true")
    p.add_argument("--systematiek",
                   choices=["loon-in", "loon-over"], default=None)
    p.add_argument("--freq", choices=["4weken", "maand"], default="4weken")
    p.add_argument("--g2n-map", help="JSON file overriding g2n.ACC codes")
    p.add_argument("--out", default="findings.xlsx")
    a = p.parse_args()
    global FREQ
    FREQ = a.freq
    import g2n as _g
    _g.FREQ = a.freq
    if a.g2n_map:
        import json
        _g.ACC.update(json.load(open(a.g2n_map, encoding="utf-8")))

    if a.year not in RATES:
        sys.exit(f"No reference data bundled for {a.year}. "
                 f"Available: {sorted(RATES)}")

    f = Findings()
    root, meta, period_el, corrections = parse_xml(a.xml)
    if period_el is None:
        sys.exit("No TijdvakAangifte block found; nothing to validate.")

    coll, saldi = collective(period_el)
    coll["_saldi_total"] = str(sum(num(x.get("Saldo")) for x in saldi))
    recs = nominative(period_el)
    period_dates = check_period(meta, coll, period_el, corrections, a.year, f)

    period_gate(a.systematiek, corrections, f)
    check_collective_vs_nominative(coll, recs, saldi, f)
    check_loon_sv_basis(recs, a.year, f)
    check_verloonde_uren(recs, f)
    check_wko_and_whk_rate(recs, a.year, f)
    check_leavers_and_contract_fields(recs, f)
    check_premium_on_aow(recs, period_dates, a.year, f)
    check_premiums(coll, recs, a.year, f)
    check_indicators(recs, period_dates, a.year, f)
    check_awf_contract(recs, f)
    check_zvw(recs, f)

    if a.retro:
        check_retro(a.retro, coll, a.year, f)
    else:
        f.skip("Retro reconciliation",
               "Transaction-level pay-element export not supplied. Period "
               "integrity cannot be settled arithmetically without it.",
               "A-07")
    f.skip("Zvw per-employee recalculation",
           "Requires VCR across the year. A single-period recalculation "
           "produces false positives on catch-up Zvw and false negatives "
           "elsewhere; per-employee Zvw differences are not reported from one "
           "period.", "E-08")
    if a.sepa:
        check_sepa(a.sepa, f)
    else:
        f.skip("Payments", "SEPA file not supplied; payment tests not run.")
    check_aok_materiality(recs, period_dates, a.year, f)
    check_zeroed_corrections(corrections, coll, f)
    if a.bt_upload:
        check_bt_upload(a.bt_upload, f)
        check_bt(a.bt_upload, a.retro, recs, period_dates, a.year, f)
    else:
        f.skip("Bijzondere beloningen",
               "Bijzonder-tarief upload not supplied. Neither conformity of "
               "the applied rate to the supplied rate, nor column membership, "
               "can be tested.", "D-03 / D-07")
    if not a.master:
        f.skip("Master data",
               "Master data not supplied; XML values not cross-checked "
               "against the employee record.")
    g2n_ref = None
    if period_dates:
        _g.PERIOD_END = period_dates[1]
    if a.g2n:
        g2n_ref = check_g2n(a.g2n, recs, a.year, f,
                            period_table=a.period_table,
                            bt_upload=a.bt_upload,
                            cumulative=a.g2n_cumulative)
        reconcile_to_g2n(g2n_ref, recs, f)
    else:
        f.skip("Gross-to-net",
               "Not supplied. The statutory recalculation of tax and premium "
               "bases, the tax and premium calculations, net pay and the "
               "totals are all untested, and no employee-level reference "
               "exists for the other deliverables to reconcile to.",
               "L-00 to L-04")
    if a.payslips:
        check_payslips(a.payslips, recs, a.year, f)
    else:
        f.skip("Payslips",
               "Payslip pack not supplied. Cumulative roll-forward, negative "
               "cumulatives, nil footer fields, the reservering block and "
               "payslip completeness are untested.", "J-01 to J-08")
    f.skip("GL mapping",
           "GL account mapping is not read by this script. Reconcile wage "
           "types to accounts using the client's pay-elements file.")

    meta["systematiek"] = a.systematiek
    out = write_report(f, meta, period_dates, recs, a.out)
    crit = sum(1 for r in f.rows if r["Severity"] == "Critical")
    print(f"{len(f.rows)} findings ({crit} critical), "
          f"{len(f.coverage)} checks passed, "
          f"{len(f.not_tested)} areas not tested.")
    if out:
        print(f"Written to {os.path.abspath(out)}")


if __name__ == "__main__":
    main()
