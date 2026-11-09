# -*- coding: utf-8 -*-
"""Assembly of the 300 global rows (see wtc_global.py for the family table, profiles and texts)."""
import wtc_common as W
import wtc_profiles as P
from wtc_model import Row, YES, NO, YN, NA
import wtc_fed as F
import wtc_global as G

TAXCODE_OF = {"basic": "US-TX-01", "ot": "US-TX-01", "saladd": "US-TX-01", "prem": "US-TX-01", "holiday": "US-TX-01", "oncall": "US-TX-01",
              "leave": "US-TX-01", "recog": "US-TX-01", "expat": "US-TX-01", "housing": "US-TX-01", "car": "US-TX-01",
              "travel": "US-TX-01", "birth": "US-TX-01", "covid": "US-TX-01", "personal": "US-TX-01", "social": "US-TX-01",
              "family": "US-TX-01", "school": "US-TX-01", "special": "US-TX-01", "reloc": "US-TX-01", "bonus": "US-TX-02",
              "profit": "US-TX-02", "disc": "US-TX-02", "supp13": "US-TX-02", "sev": "US-TX-09", "postterm": "US-TX-09",
              "grat": "US-TX-09", "stock": "US-TX-10", "transp": "US-TX-08", "edu": "US-TX-08", "medical": "US-TX-08",
              "perdiem": "US-TX-08", "d_basic": "US-TX-01", "d_ot": "US-TX-01", "d_saladd": "US-TX-01", "d_prem": "US-TX-01",
              "d_housing": "US-TX-01", "d_transp": "US-TX-08", "d_health": "US-TX-08", "d_pension": "US-TX-08",
              "d_parking": "US-TX-08", "d_oasdi": "US-TX-04"}
NO_TAX = {"rate", "ltd", "pensionpay", "benefit", "d_ltd", "d_benefit", "d_expense", "c_plan", "c_benefit", "c_accrual", "d_donation",
          "d_stock"}
ADDITIONAL = {"bonus", "profit", "disc", "supp13", "sev", "postterm", "grat", "stock", "reloc", "birth", "covid", "recog"}
FAMLABEL = {"basic": "basic salary", "ot": "overtime", "saladd": "salary addition", "prem": "premium pay", "holiday": "holiday allowance",
            "oncall": "on-call duty", "sev": "severance and seniority", "ltd": "long-term disability", "bonus": "annual and referral bonus",
            "profit": "profit-sharing bonus", "disc": "discretionary or one-time bonus", "leave": "annual leave pay", "expat": "expatriate allowance",
            "housing": "housing and rent allowance", "car": "car and car maintenance allowance", "transp": "transportation allowance",
            "reloc": "relocation allowance", "travel": "travel ticket allowance", "perdiem": "per diem allowance",
            "birth": "birth and marriage allowance", "covid": "special emergency allowance", "medical": "medical insurance or care",
            "personal": "personal allowance", "pensionpay": "pension and pension refund", "social": "social allowance",
            "benefit": "benefits plan", "edu": "education allowance", "school": "schooling allowance", "family": "family allowance",
            "recog": "recognition award", "special": "special allowance", "postterm": "post-termination payment",
            "stock": "stock options and grants", "grat": "gratuity and post-termination", "supp13": "supplemental base salary",
            "rate": "basic salary rate"}
EARN_OF = {"d_basic": "basic", "d_ot": "ot", "d_saladd": "saladd", "d_prem": "prem", "d_housing": "housing", "d_transp": "transp"}
STOCK_NAMES = {62890: "Stock options and grants - nonstatutory option spread and restricted stock",
               62990: "Stock options and grants - restricted stock unit settlement",
               62991: "Stock options and grants - restricted stock vesting",
               62993: "Stock options and grants - incentive stock option and employee stock purchase plan income",
               62994: "Stock options and grants - section 83(i) inclusion"}
STOCK_ROLE = {62890: "nonstatutory option spread (fair market value minus exercise price) and restricted stock when substantially vested",
              62990: "delivery of shares under a restricted stock unit", 62991: "restricted stock that has vested or been transferred",
              62993: "ordinary income on an incentive stock option disqualifying disposition or an employee stock purchase plan discount",
              62994: "income inclusion under a section 83(i) election"}
REP = {62100: "W-2 boxes 1, 3 and 5", 62110: "W-2 boxes 1, 3 and 5; box 12 code TT (qualified overtime premium)",
       21900: "W-2 box 4; Form 941 line 5a", 21640: "W-2 box 12 code D", 21641: "W-2 box 12 code E", 21642: "W-2 box 12 code G",
       21645: "W-2 box 12 code S", 62890: "W-2 box 12 code V"}


def _flags(code, fam, role):
    if code in G.PENSION_MAP:
        return None
    if fam == "stock":
        return G._stock_flags(code), G._stock_basis(code)
    f, b = G._prof(fam)
    return f, P.basis_for(f, b)


def build_rows():
    g = G.load_global()
    desc_count = {}
    for _, d, _t in g:
        base = G.ROLE.match(d).group(2) if G.ROLE.match(d) else d
        desc_count.setdefault(base, []).append(d)
    variant_idx = {}
    meta = {}
    for code, desc, typ in g:
        fam = G.fam_of(code)
        m = G.ROLE.match(desc)
        role = m.group(1) if m else None
        base_desc = m.group(2) if m else desc
        key = (base_desc, fam)
        if role is None:
            variant_idx[key] = variant_idx.get(key, 0) + 1
        v = variant_idx.get(key, 1)
        multi = sum(1 for d in desc_count[base_desc] if not G.ROLE.match(d)) > 1
        nm = base_desc + (f" - type {v}" if multi else "")
        if code == 62104:
            nm = "Basic salary rate (rate of pay)"
        if code in STOCK_NAMES:
            nm = STOCK_NAMES[code]
        if code == 21900:
            nm = "Social security tax (OASDI) - employee"
        if code in G.PENSION_MAP:
            nm = f"Pre-tax {G.PENSION_MAP[code][0]} - employee deduction"
        name = f"{role} - {nm}" if role else nm
        cat = {"earning": "Earning", "deduction": "Deduction", "contribution": "Employer Contribution", "rate": "Percentage"}[typ]
        if code == 21900:
            cat = "Tax"
        meta[code] = dict(name=name, cat=cat, fam=fam, role=role, typ=typ)
    first_of = {}
    for code, _d, _t in g:
        first_of.setdefault(meta[code]["fam"], code)
    out = []
    for code, desc, typ in g:
        mt = meta[code]
        fam, role, name, cat = mt["fam"], mt["role"], mt["name"], mt["cat"]
        W.at(f"Wage Type Catalogue / {code} / Explanation")
        anchor_code = G.ANCHOR.get(fam)
        is_anchor = (anchor_code == code) if anchor_code else (first_of[fam] == code)
        # ------------------------------------------------------------------ flags
        ptext = None
        if code in G.PENSION_MAP:
            flags, basis, ptext = G.pension_row(code, name)
        else:
            flags, basis = _flags(code, fam, role)
        if fam in NO_TAX or role == "Advance" or fam == "d_oasdi":
            flags, basis = {k: NA for k in P.FLAG_NAMES_LIST}, {}
        basis = {k: v for k, v in basis.items() if flags.get(k, NA) != NA}
        # ------------------------------------------------------------------ explanation
        if code in G.PENSION_MAP:
            expl = f"{name}. {ptext}"
        elif fam in EARN_OF:
            ea = EARN_OF[fam]
            ec = code + 41000
            target = f"earning {ec} ({meta[ec]['name']})" if ec in meta else f"earning family {FAMLABEL[ea]} (anchor {G.ANCHOR[ea]})"
            expl = (f"{name}. Flag class 1 (reversal deduction): Yes means the signed amount reduces that base. Deduction that reverses part of {target}: it reduces the same bases as the earning, so the flags are those of the "
                    f"earning family; the parameters sit on anchor {G.ANCHOR[ea]}. A recovery of an advance already paid is not a reduction of "
                    f"wages. Flags marked Yes-No are conditional as stated on the anchor.")
        elif fam.startswith(("d_", "c_")):
            expl = f"{name}. {G.deduction_text(fam, code, name)}"
        elif fam == "stock":
            if is_anchor:
                expl = f"{name}. {G.anchor_text(fam, name)}"
            else:
                expl = (f"{name}. Covers {STOCK_ROLE[code]}. The treatment and the figures are on anchor 62890; the resident and nonresident alien "
                        f"rules differ as stated there. Flags marked Yes-No are conditional as stated on the anchor.")
        elif is_anchor and not role:
            expl = f"{name}. {G.anchor_text(fam, name)}"
        else:
            anc = meta[anchor_code]["name"]
            kind = {"Arrears": "Arrears: amounts owed for earlier periods and paid now.",
                    "Adjustment": "Adjustment: corrects a posted amount of the family.",
                    "Advance": "Advance: advance payment of an amount of the family."}.get(role, f"Variant of the {FAMLABEL.get(fam, fam)} family.")
            if role == "Advance":
                expl = f"{name}. {kind} Anchor of the family: {anchor_code} ({anc}). " + W.ug("fed.wages.advance_of_wages.classification", G.WHY["fed.wages.advance_of_wages.classification"]) + ". No tax flag is set until the treatment is stated."
            else:
                expl = (f"{name}. {kind} Same tax treatment and flags as anchor {anchor_code} ({anc}), which carries the parameters; the variant differs "
                        f"only in how the payroll uses it (rate tier, reason or source). Flags marked Yes-No are conditional as stated on the anchor.")
        # ------------------------------------------------------------------ attributes
        tcode = "US-NA" if (role == "Advance" or fam in NO_TAX) else TAXCODE_OF.get(fam, "US-NA")
        occ = "Additional" if (role or fam in ADDITIONAL) else "Recurring"
        side = "EE" if typ == "deduction" else ("ER" if typ == "contribution" else "NONE")
        if fam == "c_accrual":
            cat = "Notional"
        inputs = []
        if code == 62100:
            inputs = [F.D_RATE_BASIS, F.D_PAYFREQ, F.D_FTPT]
        elif fam == "leave" and code in (62300, 62305):
            inputs = [F.D_VACFORF, F.D_FINALPAY, F.D_SEP]
        elif fam in ("sev", "postterm") and is_anchor:
            inputs = [F.D_HIRE, F.D_SEP, F.D_FINALPAY]
        elif code == 21900:
            inputs = [F.D_VISA, F.D_PURPOSE, F.D_TOTAL_CTRY, F.D_TOTAL_EX, F.D_NO_SSMED]
        elif code == 62104:
            inputs = [F.D_RATE_BASIS]
        r = Row(str(code), name, cat, expl, tax_code=tcode, occ=occ, flags=flags, basis=basis, side=side, rep=REP.get(code, ""),
                payslip=bool(is_anchor or code in (21900, 21640, 21641, 21642, 21645, 21610, 21611, 21810, 21820)),
                inputs=inputs, fam=fam, legal=sorted(set(basis.values())), glob=True)
        r.sym = f"g{code}"
        r.global_type = typ
        r.global_desc = desc
        out.append(r)
    return out
