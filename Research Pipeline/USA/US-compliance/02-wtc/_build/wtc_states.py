# -*- coding: utf-8 -*-
"""State and local layer of the US Wage Type Catalogue (one row per jurisdiction and programme, generated from the
country-specific facts: every figure is a tagged fact with its own dates; nothing is typed).

Layers per jurisdiction: State income tax withholding (SIT), State unemployment insurance (SUI, employer), SUI employee
contribution (AK, NJ, PA), State programmes (disability, paid family and medical leave, long-term care, workers'
compensation fees), employer levies on separate returns and local taxes.
"""
import json
import os

import wtc_common as W
import wtc_profiles as P
from wtc_model import YES, NO, YN, NA, X
import wtc_fed as F
from wtc_why import WHY as WHY_TXT

val, line, rid = W.val, W.line, W.rid

NO_WAGE_TAX = ("AK", "FL", "NV", "NH", "SD", "TN", "TX", "WA", "WY")   # multi.no_wage_income_tax.states

_WTC_KEYS = None


def wtc_keys():
    """Keys of the country-specific facts file in file order (one entry per key)."""
    global _WTC_KEYS
    if _WTC_KEYS is None:
        d = json.load(open(os.path.join(W.RESEARCH, "WTC-country_specific-facts.json"), encoding="utf-8"))
        seen, out = set(), []
        for f in d["facts"]:
            if f["key"] not in seen:
                seen.add(f["key"])
                out.append(f["key"])
        _WTC_KEYS = out
    return _WTC_KEYS


PROG_P1 = {"sdi", "tdi", "tdi_fli", "fli", "pfl", "famli", "pfml", "paid_leave", "cares", "dbl", "wf_swf", "phc", "wbf", "wc", "secure_choice"}
SUI_P1 = {"sui", "ui", "ui_operating_fund", "ett", "emac", "wtf", "abcr"}


def cls(key):
    p = key.split(".")
    p1 = p[1] if len(p) > 1 else ""
    p2 = p[2] if len(p) > 2 else ""
    last = p[-1]
    if p1 == "oracle" or (p1 == "pit" and p2 == "oracle"):
        return "oracle"
    if p1 == "pit" and p2 == "exists":
        return "exists"
    if p1 in ("local", "local_wage_tax") or (p1 == "pit" and p2 in ("local", "municipal", "school_district")):
        return "local"
    if p1 in ("sit", "pit", "wh", "nonres", "conformity", "obbba", "meals", "lodging", "bik"):
        return "sit"
    if p1 == "base":
        return "sui" if last.startswith("ui") else "sit"
    if p1 in ("sui", "ui") and p2 == "employee":
        return "suiee"
    if p1 in SUI_P1:
        return "sui"
    if p1 in PROG_P1:
        return "prog"
    if p1 == "levy":
        return "levy"
    return "other"


def skeys(st, kind):
    s = st.lower()
    return [k for k in wtc_keys() if k.split(".")[0] == s and cls(k) == kind]


CONSUMED = set()


def lines(keys, skip=()):
    out = []
    for k in keys:
        if k in skip:
            continue
        CONSUMED.add(k)
        if k in W.RESIDUAL:
            out.append(W.gap(*W.RESIDUAL[k]))
            continue
        out.append(line(k))
    return "; ".join(out)


def open_items(st, kinds, prefixes=None):
    """Gap sentences for the open items (unresolved facts) of a State whose key belongs to one of the layers."""
    out = []
    for key, u in W.unresolved().items():
        p = key.split(".")
        if p[0] != st.lower():
            continue
        k = {"sit": ("sit", "wh", "pit", "base", "local_wage_tax"), "sui": ("sui", "ui", "base"), "prog": ("pfml", "famli", "pfl", "sdi", "tdi", "cares"),
             "local": ("local",), "levy": ("levy",)}
        okp = set()
        for kd in kinds:
            okp |= set(k[kd])
        if len(p) > 1 and p[1] == "local_wage_tax" and "sui" in kinds and st.upper() not in NO_WAGE_TAX:
            continue
        if prefixes and not any(".".join(p[1:]).startswith(x) for x in prefixes):
            continue
        if len(p) > 1 and p[1] in okp:
            if p[1] == "pit" and len(p) > 2 and p[2] in ("local", "municipal", "school_district") and "local" not in kinds:
                continue
            if p[1] == "base" and "sui" in kinds and "sit" not in kinds and not any(x in key for x in ("ui", "pfml", "cares")):
                continue
            if p[1] == "base" and "sit" in kinds and "sui" not in kinds and any(x in key for x in ("ui", "pfml", "cares")):
                continue
            out.append(key)
    return out


UI_LINKED = {"MS": ["ms.levy.workforce_investment_training.rate"], "OH": ["oh.levy.tcsf.rate"], "NY": ["ny.levy.rsf"]}
WHY = {}   # unresolved key -> wording of the cell (neutral, English, no pipeline vocabulary)


def gaps_for(st, kinds, prefixes=None):
    parts = []
    for key in open_items(st, kinds, prefixes):
        u = W.unresolved()[key]
        why = WHY_TXT[key]
        parts.append(W.ug(key, why))
    return (" " + " ".join(p + "." for p in parts)) if parts else ""


def _neutral(s):
    s = s.split(" (")[0] if len(s) > 220 else s
    s = s.replace("journal trap: ", "").replace("tier B", "unofficial").replace("tier-B", "unofficial").replace("tier C", "unofficial")
    return s.rstrip(".")[:240]


def build_states(reg):
    A = reg.add
    B = P.B()
    sn = W.STATE_NAMES
    inputs_sit = [F.D_STATE_CERT, F.D_WORK_STATE, F.D_RES_STATE]
    # ------------------------------------------------------------------ SIT, one row per wage-taxing jurisdiction ---
    for st in W.STATES:
        if st in NO_WAGE_TAX:
            continue
        ks = skeys(st, "sit")
        if st in ("AZ", "IL", "NC"):
            ks += skeys(st, "local")                    # 'no local wage tax' flag of the State
        extra_in = list(inputs_sit)
        if st in ("MN", "NE", "OH", "RI"):
            extra_in.append(W.dd("State withholding allowances or exemptions claimed"))
        if st == "CT":
            extra_in.append(W.dd("Connecticut withholding code (CT-W4)"))
        if st == "MD":
            extra_in.append(W.dd("Maryland county of residence"))
        if st == "IN":
            extra_in += [W.dd("Indiana county of residence on January 1"), W.dd("Indiana county of principal employment on January 1")]
        W.at(f"Wage Type Catalogue / SIT {st} / Explanation")
        body = lines(ks)
        gaps = gaps_for(st, ["sit"])
        expl = (f"{sn[st]} income tax withheld from the employee on wages. " + (body + ". " if body else "")
                + f"State withholding follows the federal wage base unless a departure is listed above. Inputs: {', '.join(extra_in)}."
                + gaps + f" Declared: W-2 boxes 15 to 17 and the State withholding return (Report Specifications US-DOR-001 and US-DOR-002).")
        A(f"sit_{st}", f"State income tax withholding - {sn[st]}", "Tax", expl, tax_code="US-TX-06", side="EE",
          rep=f"W-2 boxes 15 to 17 ({st})", payslip=True, inputs=extra_in, legal=sorted({W.rid(k) for k in ks}), fam="sit")
    # ------------------------------------------------------------------ SUI employer ---
    for st in W.STATES:
        ks = skeys(st, "sui")
        if st not in ("AK", "NJ", "PA"):
            ks += skeys(st, "suiee")                    # 'employee contribution applies' flag of the other States
        if st in NO_WAGE_TAX:
            ks += skeys(st, "exists") + skeys(st, "sit") + skeys(st, "local")
        if st in ("VA", "NH", "AK"):
            ks += skeys(st, "prog") + [k for k in wtc_keys() if k == "ak.sdi_pfml.applies"] * (st == "AK" and not skeys(st, "prog"))
        ks += UI_LINKED.get(st, [])
        ks = list(dict.fromkeys(ks))
        if not ks:
            continue
        W.at(f"Wage Type Catalogue / SUI {st} / Explanation")
        body = lines(ks)
        gaps = gaps_for(st, ["sui"])
        extra = ""
        sl = [k for k in wtc_keys() if k.startswith("multi.sui.other_state_wage_credit." + st.lower())]
        if sl:
            extra = " " + lines(sl) + "."
        A(f"sui_{st}", f"State unemployment insurance - employer - {sn[st]}", "Employer Contribution",
          (f"{sn[st]} unemployment insurance contribution paid by the employer, with the unemployment-insurance-linked assessments of the State. "
           + body + "." + extra + gaps + f" The State of coverage is set by {X('flag_ui_state')}. Declared: the State quarterly wage and contribution "
           f"report (Report Specification US-UI-001)."),
          tax_code="US-TX-07", side="ER", rep=f"State UI report ({st})", inputs=[F.D_UI_STATE, W.dd("State employer account State"),
          W.dd("State employer account number")], legal=sorted({W.rid(k) for k in ks}), fam="sui")
    # ------------------------------------------------------------------ SUI employee ---
    for st in ("AK", "NJ", "PA"):
        ks = skeys(st, "suiee")
        W.at(f"Wage Type Catalogue / SUI EE {st} / Explanation")
        A(f"suiee_{st}", f"State unemployment insurance - employee - {sn[st]}", "Tax",
          (f"{sn[st]} unemployment insurance contribution deducted from the employee. " + lines(ks) + ". Employee contribution States: "
           f"{val('multi.sui.employee_contribution.states')} [{rid('multi.sui.employee_contribution.states')}]. Declared on the State quarterly wage "
           f"report (US-UI-001) and in W-2 box 14 where the State requires."),
          tax_code="US-TX-07", side="EE", rep=f"State UI report ({st})", payslip=True, inputs=[F.D_UI_STATE],
          legal=sorted({W.rid(k) for k in ks}), fam="suiee")
    return reg
