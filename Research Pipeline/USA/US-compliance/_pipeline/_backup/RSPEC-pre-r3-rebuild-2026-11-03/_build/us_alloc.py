# -*- coding: utf-8 -*-
"""Allocation of the RSPEC facts to the 20 Report Specifications (one per in-scope filing of
scope_manifest.json). Pure key-pattern rules, so a new fact lands in the right workbook without
a hand edit; unallocated RSPEC keys are reported by the build."""
import re

from us_common import RSPEC_KEYS, STATES

# doc id -> key regexes (matched against the full key)
RULES = [
    ("NOTICE", [r"^rspec\.(co\.notice|nj\.separation)\.", r"^rspec\.ca\.contractor_report\.",
                r"^rspec\.(ct\.household|or\.annual)\.forms$"]),
    ("US-IRS-001", [r"^rspec\.fed\.(form941|deposit|reporting_agent)\."]),
    ("US-IRS-002", [r"^rspec\.fed\.form944\."]),
    ("US-IRS-003", [r"^rspec\.fed\.form943\."]),
    ("US-IRS-004", [r"^rspec\.fed\.(form940|futa)\."]),
    ("US-IRS-005", [r"^rspec\.fed\.(schedule_h|household)\."]),
    ("US-IRS-006", [r"^rspec\.fed\.form1042s\."]),
    ("US-IRS-007", [r"^fed\.aca\.", r"^rspec\.fed\.aca\."]),
    ("US-IRS-008", [r"^rspec\.fed\.form941x\."]),
    ("US-SSA-001", [r"^rspec\.fed\.(w2|efw2)\.", r"^fed\.(w2|efw2|efw2c|fica)\."]),
    ("US-SDNH-001", [r"^rspec\.fed\.new_hire\.", r"^fed\.newhire\.", r"(^|\.)new_?hire\.", r"\.newhire\."]),
    ("US-PFML-001", [r"^rspec\.multi\.pfml\.", r"^rspec\.[a-z]{2}\.(pfml_qtr|pfml_ltc_qtr|pfml_ltc|pfml|tdi)\.",
                     r"^wa\.(report\.pfml_ltc|pfml)\.", r"^ct\.report\.pfml\.", r"^ca\.sdi\."]),
    ("US-UI-001", [r"^rspec\.multi\.ui_qtr\.", r"^rspec\.[a-z]{2}\.(ui_qtr|ui_monthly|mass_separation)\.",
                   r"^[a-z]{2}\.report\.(sui|ui)\.", r"^dd\.in\.ui\."]),
    ("US-LOC-002", [r"^rspec\.(nj\.local\.newark_jersey_city|mo\.local\.st_louis)$", r"^rspec\.pa\.local\.pittsburgh_"]),
    ("US-LOC-003", [r"^rspec\.wa\.local\.seattle(\.|$)"]),
    ("US-LOC-001", [r"^rspec\.[a-z]{2}\.local\.", r"^rspec\.oh\.(municipal|school_district)\."]),
    ("US-DOR-003", [r"^rspec\.nv\.mbt\."]),
    ("US-DOR-004", [r"^rspec\.ny\.mctmt\."]),
    ("US-WC-001", [r"^rspec\.wy\.wc_report\."]),
    ("US-DOR-002", [r"^rspec\.[a-z]{2}\.(annual_recon|w2_state|w2_employee)\.", r"^sir\.[a-z]{2}\.w2\.",
                    r"^[a-z]{2}\.report\.(w2|annual_reconciliation|efile_threshold)\."]),
    ("US-DOR-001", [r"^rspec\.[a-z]{2}\.(wh_return|wh_deposit|wh_payment|wh_remit|wh_status|wh_qtr_report|efile|"
                    r"nys45|nys1|oq|registration|poa|permit)\.", r"^[a-z]{2}\.report\.(wh|mo941)\."]),
]


def doc_of(key):
    for doc, pats in RULES:
        if any(re.search(p, key) for p in pats):
            return doc
    return None


def jur_of(key):
    p = key.split(".")
    for seg in p[:3]:
        if seg.upper() in STATES:
            return seg.upper()
    if "fed" in p[:2]:
        return "FED"
    if "multi" in p[:2]:
        return "MULTI"
    return None


def allocation():
    out, orphan = {}, []
    seen = set()
    for k in RSPEC_KEYS:
        if k in seen:
            continue
        seen.add(k)
        d = doc_of(k)
        if d is None:
            orphan.append(k)
            continue
        out.setdefault(d, {}).setdefault(jur_of(k) or "?", []).append(k)
    return out, orphan


if __name__ == "__main__":
    a, o = allocation()
    for d in sorted(a):
        print(d, {j: len(v) for j, v in sorted(a[d].items())})
    print("ORPHAN", o)
