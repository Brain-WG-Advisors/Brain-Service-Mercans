# -*- coding: utf-8 -*-
"""Reconciliation WTC x DD x Report Specifications (both directions) -> checks/wtc_recon.csv."""
import csv
import os
import re

import wtc_common as W

# (spec regex, name regex, [symbols]) first match wins. Symbols: country row symbols or 'g<code>' global codes.
RULES = [
    (r".", r"(?i)treaty-exempt", ["treaty_exempt"]),
    (r"US-IRS-00[1-3]|US-IRS-008", r"count of employees|employees in pay period|number of agricultural employees", ["flag_paid12"]),
    (r"US-IRS-007", r"employee required contribution", ["flag_aca", "g21610"]),
    (r"US-IRS-007", r"Form 1094-C|Form 1095-C|Line 1[0-9]|All 12 Months", ["flag_aca"]),
    (r"US-IRS-004", r"Schedule A", ["base_futa", "futa_credit_reduction"]),
    (r"US-IRS-004", r"liability by quarter", ["liab_futa"]),
    (r"US-IRS-004", r"line 4|exempt from FUTA", ["base_futa_exempt"]),
    (r"US-IRS-004", r"line 5|excess of|in excess", ["base_futa_excess"]),
    (r"US-IRS-004", r"line 10|paid late", ["futa_late"]),
    (r"US-IRS-004", r"line 13|deposited", ["dep_fed"]),
    (r"US-IRS-004", r"Total payments|FUTA gross", ["base_futa_gross"]),
    (r"US-IRS-004", r"FUTA taxable", ["base_futa"]),
    (r"US-IRS-005", r"Household cash wages|Cash wages subject to FUTA|State unemployment", ["hh_cash", "base_futa"]),
    (r"US-IRS-005", r"Medicare tax|Additional Medicare", ["base_medicare", "base_addl_medicare", "hh_cash"]),
    (r"US-IRS-005", r"social security", ["base_oasdi", "hh_cash"]),
    (r"US-IRS-005", r"Federal income tax", ["fit_reg", "hh_cash"]),
    (r"US-IRS-00[1238]", r"5b|SS tips|SS tips", ["base_oasdi_tips"]),
    (r"US-IRS-00[1238]", r"3121\(q\)", ["tax_3121q"]),
    (r"US-IRS-00[1238]", r"qualified small business", ["cr_qsbpt"]),
    (r"US-IRS-00[1238]", r"special additions|sick/family leave wages", ["add_wages_941x"]),
    (r"US-IRS-00[1238]", r"fractions of cents|sick pay adj|group-term life adj|adjustments|tax adjustments", ["adj_fed_period"]),
    (r"US-IRS-00[1238]", r"Additional Medicare", ["base_addl_medicare", "addl_medicare_ee"]),
    (r"US-IRS-00[1238]", r"Deposits|deposit", ["dep_fed"]),
    (r"US-IRS-00[1238]", r"liability", ["liab_fed"]),
    (r"US-IRS-00[1238]", r"Quarter and year corrected|Adjustment or claim|direction", ["adj_fed_period"]),
    (r"US-IRS-00[1238]", r"Taxable Medicare", ["base_medicare", "medicare_ee", "medicare_er"]),
    (r"US-IRS-00[1238]", r"social security", ["base_oasdi", "g21900", "oasdi_er"]),
    (r"US-IRS-00[1238]", r"Federal income tax", ["fit_reg", "fit_supp22", "fit_supp37"]),
    (r"US-IRS-008", r"line 4a|line 5a|overreported|claim", ["adj_fed_period"]),
    (r"US-IRS-00[1238]", r"Wages, tips", ["base_fit"]),
    (r"US-DOR-003", r"health benefits", ["hlth_dummy"]),
    (r"US-DOR-003", r".", ["sui_NV", "levy_NV_mbt"]),
    (r"US-DOR-004", r".", ["levy_NY_mctmt", "levy_OR_trimet", "levy_OR_lane", "levy_OR_stt"]),
    (r"US-LOC-001", r".", ["loc_PA_eit", "loc_OH_muni", "loc_IN_county", "loc_MD_county", "loc_MI_detroit", "loc_NY_nyc", "loc_KY_occ", "loc_PA_phl"]),
    (r"US-LOC-002", r".", ["loc_NJ_city", "loc_MO_stl", "loc_MO_stl_pe", "loc_PA_pgh", "loc_CO_opt_er"]),
    (r"US-LOC-003", r".", ["loc_WA_seattle"]),
    (r"US-PFML-001", r"Hours|hours", ["hours_worked"]),
    (r"US-PFML-001", r".", ["prog_WA_pfml_ee", "prog_WA_pfml_er", "prog_MA_pfml_ee", "prog_CT_pfml_ee", "prog_OR_pfml_ee"]),
    (r"US-UI-001", r"Hours", ["hours_worked"]),
    (r"US-UI-001", r".", ["sui_CA", "base_futa", "sui_NY"]),
    (r"US-WC-001", r"Hours", ["hours_worked"]),
    (r"US-WC-001", r".", ["prog_WA_wc_ee", "prog_NM_wcfee_ee", "prog_OR_wbf_ee"]),
    (r"US-DOR-00[12]", r"local|Local", ["loc_PA_eit", "loc_OH_muni", "loc_NY_nyc"]),
    (r"US-DOR-00[12]", r"UI|unemployment", ["sui_CA"]),
    (r"US-DOR-00[12]", r"payment|deposit", ["dep_fed"]),
    (r"US-DOR-00[12]", r".", ["sit_CA", "sit_NY", "sit_PA"]),
    (r"US-SSA-001", r"Wages, Tips", ["base_fit"]),
    (r"US-SSA-001", r"Federal Income Tax", ["fit_reg"]),
    (r"US-SSA-001", r"Social Security Wages", ["base_oasdi"]),
    (r"US-SSA-001", r"Social Security Tax", ["g21900"]),
    (r"US-SSA-001", r"Medicare Wages", ["base_medicare"]),
    (r"US-SSA-001", r"Medicare Tax", ["medicare_ee", "addl_medicare_ee"]),
    (r"US-SSA-001", r"Social Security Tips", ["base_oasdi_tips", "tips_cash"]),
    (r"US-SSA-001", r"Dependent Care", ["dep_care"]),
    (r"US-SSA-001", r"401\(k\)", ["g21640"]),
    (r"US-SSA-001", r"403\(b\)\s*$|Deferred Comp 403", ["g21641"]),
    (r"US-SSA-001", r"408\(k\)", ["ded_408k6"]),
    (r"US-SSA-001", r"457\(b\)", ["g21642"]),
    (r"US-SSA-001", r"501\(c\)", ["ded_501c18"]),
    (r"US-SSA-001", r"Section 457 Dist", ["w2_nq457"]),
    (r"US-SSA-001", r"Not Section 457", ["w2_nqnot457"]),
    (r"US-SSA-001", r"HSA", ["hsa_er"]),
    (r"US-SSA-001", r"Combat", ["w2_q"]),
    (r"US-SSA-001", r"Group Term", ["gtl_imputed"]),
    (r"US-SSA-001", r"Nonstatutory", ["g62890"]),
    (r"US-SSA-001", r"409A", ["w2_409a"]),
    (r"US-SSA-001", r"Roth 401", ["ded_roth401"]),
    (r"US-SSA-001", r"Roth 403", ["ded_roth403"]),
    (r"US-SSA-001", r"Employer-Sponsored Health", ["w2_dd"]),
    (r"US-SSA-001", r"QSEHRA", ["w2_ff"]),
    (r"US-SSA-001", r"Statutory Employee", ["flag_statutory_emp"]),
    (r"US-SSA-001", r"Retirement Plan", ["flag_retplan"]),
    (r"US-SSA-001", r"Third-Party Sick", ["flag_3psp"]),
    (r"US-SSA-001", r"Allocated Tips", ["tips_alloc"]),
    (r"US-SSA-001", r"Code A$", ["w2_a"]), (r"US-SSA-001", r"Code B$", ["w2_b"]), (r"US-SSA-001", r"Code J$", ["w2_j"]),
    (r"US-SSA-001", r"Code K$", ["w2_k"]), (r"US-SSA-001", r"Code L$", ["w2_l"]), (r"US-SSA-001", r"Code P$", ["w2_p"]),
    (r"US-SSA-001", r"Code TA$", ["trump_er"]), (r"US-SSA-001", r"Code TP$", ["tips_cash"]), (r"US-SSA-001", r"Code TT$", ["ot_premium"]),
]
RULES = [r for r in RULES if "hlth_dummy" not in r[2]] + []


def mapped_rows():
    out = []
    for r in W.D.spec_rows():
        m = r["mapping"]
        if m.startswith("Payroll result") or m.startswith("Correction register"):
            out.append(r)
    return out


def compute(symmap):
    """-> (records, unmapped)"""
    recs, un = [], []
    for r in mapped_rows():
        hit = None
        if r["spec"] == "US-DOR-003" and "health" in r["name"].lower():
            hit = ["levy_NV_mbt"]
        else:
            for sp, nm, syms in RULES:
                if re.search(sp, r["spec"]) and re.search(nm, r["name"]):
                    hit = syms
                    break
        codes = [symmap[s] for s in (hit or []) if s in symmap]
        if not codes:
            un.append(r)
            continue
        recs.append((r, hit, codes))
    return recs, un


def write_csv(recs, un, rows, dd_missing, dd_consumers, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["direction", "item", "detail", "mapped_to", "status", "reason"])
        for r, hit, codes in recs:
            w.writerow(["RSPEC->WTC", f"{r['spec']} row {r['row']}", r["name"], " ".join(codes), "MAPPED", ""])
        for r in un:
            w.writerow(["RSPEC->WTC", f"{r['spec']} row {r['row']}", r["name"], "", "UNMAPPED", ""])
        for rw in rows:
            for i in rw.inputs:
                ok = i in W.dd_names()
                w.writerow(["WTC->DD", rw.code, i, i if ok else "", "MAPPED" if ok else "UNMAPPED", ""])
        for name, consumers, reason in dd_consumers:
            w.writerow(["DD->WTC", name, "", " ".join(consumers), "MAPPED" if consumers else "EXCEPTION", reason])
