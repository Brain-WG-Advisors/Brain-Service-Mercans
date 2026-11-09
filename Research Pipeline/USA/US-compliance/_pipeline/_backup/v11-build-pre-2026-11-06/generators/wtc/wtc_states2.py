# -*- coding: utf-8 -*-
"""State programmes, employer levies on separate returns and local taxes of the US Wage Type Catalogue."""
import wtc_common as W
import wtc_profiles as P
from wtc_model import YES, NO, YN, NA, X
import wtc_fed as F
import wtc_states as S

val, line, rid = W.val, W.line, W.rid
sn = W.STATE_NAMES

# (state, stem, name, key prefixes after the state code, sides, extra keys, report)
PROGRAMS = [
    ("CA", "sdi", "State disability insurance (SDI)", ["sdi."], "EE", [], "US-PFML-001"),
    ("CO", "famli", "Paid family and medical leave insurance (FAMLI)", ["famli."], "BOTH", [], "US-PFML-001"),
    ("CT", "pfml", "Paid family and medical leave (PFML)", ["pfml."], "EE", [], "US-PFML-001"),
    ("DC", "pfl", "Paid family leave (PFL)", ["pfl."], "ER", [], "US-PFML-001"),
    ("DE", "pfml", "Paid leave (PFML)", ["pfml."], "BOTH", [], "US-PFML-001"),
    ("HI", "tdi", "Temporary disability insurance (TDI)", ["tdi."], "EE", [], "US-PFML-001"),
    ("HI", "phc", "Prepaid health care (PHC)", ["phc."], "EE", [], "US-PFML-001"),
    ("MA", "pfml", "Paid family and medical leave (PFML)", ["pfml."], "BOTH", [], "US-PFML-001"),
    ("MD", "pfml", "Paid family and medical leave insurance (FAMLI)", ["pfml.", "famli."], "BOTH", [], "US-PFML-001"),
    ("ME", "pfml", "Paid family and medical leave (PFML)", ["pfml."], "BOTH", ["me.pfml.w2_box14_label"], "US-PFML-001"),
    ("MN", "pfml", "Paid leave (PFML)", ["paid_leave.", "pfml."], "BOTH", [], "US-PFML-001"),
    ("NJ", "tdifli", "Temporary disability insurance (TDI) and family leave insurance (FLI)", ["tdi.", "tdi_fli.", "fli.", "wf_swf."], "BOTH", [], "US-PFML-001"),
    ("NY", "pfl", "Paid family leave (PFL)", ["pfl."], "EE", [], "US-PFML-001"),
    ("NY", "dbl", "Disability benefits law (DBL)", ["dbl."], "EE", [], "US-PFML-001"),
    ("OR", "pfml", "Paid leave Oregon (PFML)", ["pfml."], "BOTH", [], "US-PFML-001"),
    ("OR", "wbf", "Workers' Benefit Fund assessment", ["wbf."], "BOTH", [], "US-WC-001"),
    ("RI", "tdi", "Temporary disability insurance (TDI)", ["tdi."], "EE", [], "US-PFML-001"),
    ("VT", "ccc", "Child Care Contribution", ["levy.child_care."], "BOTH", [], "US-PFML-001"),
    ("WA", "pfml", "Paid family and medical leave (PFML)", ["pfml."], "BOTH", [], "US-PFML-001"),
    ("WA", "cares", "WA Cares Fund long-term care premium", ["cares."], "EE", ["special_population.wa_cares.niv_exempt"], "US-PFML-001"),
    ("WA", "wc", "Workers' compensation State fund premium - employee share", ["wc."], "EE", [], "US-WC-001"),
    ("NM", "wcfee", "Workers' compensation fee", ["levy.wc_fee."], "BOTH", [], "US-WC-001"),
    ("IL", "secure", "Illinois Secure Choice payroll deduction", ["secure_choice."], "EE", [], "US-LOC-001"),
]
# employer levies on separate returns / transit levies: (state, stem, name, side, key prefixes, report)
LEVIES = [
    ("NV", "mbt", "Modified Business Tax (MBT)", "ER", ["levy.mbt."], "US-DOR-003"),
    ("NY", "mctmt", "Metropolitan Commuter Transportation Mobility Tax (MCTMT)", "ER", ["levy.mctmt"], "US-DOR-004"),
    ("OR", "stt", "Statewide transit tax - employee", "EE", ["levy.statewide_transit."], "US-DOR-004"),
    ("OR", "trimet", "TriMet transit payroll tax - employer", "ER", ["levy.trimet."], "US-DOR-004"),
    ("OR", "lane", "Lane Transit District payroll tax - employer", "ER", ["levy.lane_transit."], "US-DOR-004"),
]
# local taxes: (state, stem, name, side, cat, key prefixes, report)
LOCALS = [
    ("AL", "leeds", "Alabama municipal occupational tax - Leeds", "EE", ["local.leeds."]),
    ("CO", "opt_ee", "Colorado occupational privilege tax - employee share", "EE", ["local.opt.denver.employee", "local.opt.greenwood_village.employee", "local.opt.glendale.employee"]),
    ("CO", "opt_er", "Colorado occupational privilege tax - employer share", "ER", ["local.opt.denver.employer", "local.opt.greenwood_village.employer", "local.opt.glendale.employer"]),
    ("DE", "wilm", "Wilmington earned income tax", "EE", ["local.wilmington."]),
    ("IN", "county", "Indiana county income tax", "EE", ["local."]),
    ("KY", "occ", "Kentucky occupational license tax - Louisville and Lexington", "EE", ["local."]),
    ("MD", "county", "Maryland county income tax", "EE", ["local."]),
    ("MI", "detroit", "Michigan city income tax - Detroit", "EE", ["local.detroit."]),
    ("MI", "cities", "Michigan city income tax - self-administered cities", "EE", ["local.uniform."]),
    ("MO", "stl", "St. Louis and Kansas City earnings tax", "EE", ["local.st_louis.earnings", "local.kansas_city."]),
    ("MO", "stl_pe", "St. Louis payroll expense tax - employer", "ER", ["local.st_louis.payroll_expense"]),
    ("NJ", "city", "Newark and Jersey City payroll tax - employer", "ER", ["local."]),
    ("NY", "nyc", "New York City and Yonkers income tax withholding", "EE", ["local."]),
    ("OH", "muni", "Ohio municipal income tax", "EE", ["local.municipal.", "pit.municipal."]),
    ("OH", "school", "Ohio school district income tax", "EE", ["local.school_district.", "pit.school_district."]),
    ("OR", "metro", "Oregon Metro supportive housing services personal income tax", "EE", ["local.metro_shs."]),
    ("OR", "mult", "Multnomah County preschool for all personal income tax", "EE", ["local.multnomah_pfa."]),
    ("PA", "eit", "Pennsylvania local earned income tax (EIT)", "EE", ["local.eit."]),
    ("PA", "lst", "Pennsylvania local services tax (LST)", "EE", ["local.lst."]),
    ("PA", "phl", "Philadelphia wage tax", "EE", ["local.philadelphia."]),
    ("PA", "pgh", "Pittsburgh payroll expense tax - employer", "ER", ["pit.local.pittsburgh."]),
    ("WA", "seattle", "Seattle payroll expense tax and social housing tax - employer", "ER", ["local."]),
    ("WV", "svc", "Charleston municipal service fee", "EE", ["local."]),
]
FLAG_ONLY = {"AK": "local_wage_tax.exists", "AZ": "local_wage_tax.exists", "IL": "local_wage_tax.exists", "NC": "local.income_tax.applies"}


def _keys(st, kind_keys, prefixes, extra=()):
    out = []
    s = st.lower() + "."
    for k in kind_keys:
        rest = k[len(s):] if k.startswith(s) else None
        if rest is None:
            continue
        if any(rest.startswith(p) for p in prefixes):
            out.append(k)
    return out + [e for e in extra if e in W.C.FACTS]


def build_states2(reg):
    A = reg.add
    for st, stem, name, prefixes, sides, extra, report in PROGRAMS:
        allk = [k for k in S.wtc_keys() if k.split(".")[0] == st.lower()]
        ks = _keys(st, allk, prefixes, extra)
        sym_ee = f"prog_{st}_{stem}_ee"
        W.at(f"Wage Type Catalogue / PROG {st} {stem} / Explanation")
        er_keys = [k for k in ks if "employer" in k.split(".", 1)[1]]
        ee_keys = [k for k in ks if k not in er_keys] if sides == "BOTH" else ks
        gaps = S.gaps_for(st, ["prog"] if stem != "ccc" else ["levy"])
        if sides in ("EE", "BOTH"):
            body = S.lines(ee_keys)
            A(sym_ee, f"{name} - employee - {sn[st]}", "Tax",
              (f"{sn[st]} {name}: contribution deducted from the employee. " + (body + ". " if body else "") + gaps.strip() +
               (f" The employer share is {X(f'prog_{st}_{stem}_er')}." if sides == 'BOTH' else "") +
               f" The programme State follows {X('flag_ui_state')} unless this row states otherwise. State employee contributions to the programme are W-2 wages: "
               f"{val('fed.pfml.employee_contribution.w2')} [{rid('fed.pfml.employee_contribution.w2')}]. Declared: the programme quarterly report "
               f"(Report Specification {report}) and, where the State requires, W-2 box 14."),
              tax_code="US-TX-07", side="EE", rep=f"State programme report ({st}); W-2 box 14", payslip=True, inputs=[F.D_UI_STATE, F.D_WORK_STATE],
              legal=sorted({W.rid(k) for k in ks} | {"US-FEDS5-007"}), fam="prog")
        if sides in ("ER", "BOTH"):
            body = S.lines(er_keys) if sides == "BOTH" or er_keys else ""
            if sides == "ER":
                body = S.lines(ks)
            ref = f"The total and employee figures are on {X(sym_ee)}. " if sides == "BOTH" else ""
            A(f"prog_{st}_{stem}_er", f"{name} - employer - {sn[st]}", "Employer Contribution",
              (f"{sn[st]} {name}: contribution paid by the employer. " + ref + (body + ". " if body else "") + (gaps.strip() if sides == "ER" else "") +
               f" Declared: the programme quarterly report (Report Specification {report})."),
              tax_code="US-TX-07", side="ER", rep=f"State programme report ({st})", inputs=[F.D_UI_STATE], legal=sorted({W.rid(k) for k in ks}),
              fam="prog")
    # --------------------------------------------------------------------- Wyoming state fund (no facts) ---
    W.at("Wage Type Catalogue / PROG WY wc / Explanation")
    A("prog_WY_wc", "Workers' compensation State fund premium - Wyoming", "Employer Contribution",
      ("Premium of the Wyoming State workers' compensation fund paid by the employer. " + W.gap("WTC-RQ-09", "no rate, base or deduction rule of the Wyoming fund is carried")),
      tax_code="US-NA", side="ER", rep="US-WC-001 (Wyoming)", legal=[], fam="prog")
    # ----------------------------------------------------------------------------- levies ---
    for st, stem, name, side, prefixes, report in LEVIES:
        allk = [k for k in S.wtc_keys() if k.split(".")[0] == st.lower()]
        ks = _keys(st, allk, prefixes)
        W.at(f"Wage Type Catalogue / LEVY {st} {stem} / Explanation")
        gaps = S.gaps_for(st, ["levy"]) if stem in ("stt", "trimet", "lane") else ""
        A(f"levy_{st}_{stem}", f"{name} - {sn[st]}", "Employer Contribution" if side == "ER" else "Tax",
          (f"{sn[st]} {name}, {'paid by the employer' if side == 'ER' else 'deducted from the employee'}. " + S.lines(ks) + "." + gaps +
           f" Declared on a separate return (Report Specification {report})."),
          tax_code="US-TX-07", side=side, rep=f"{report} ({st})", payslip=(side == "EE"), legal=sorted({W.rid(k) for k in ks}), fam="levy")
    # ------------------------------------------------------------------------------ local ---
    for st, stem, name, side, prefixes in LOCALS:
        allk = [k for k in S.wtc_keys() if k.split(".")[0] == st.lower()]
        ks = _keys(st, allk, prefixes)
        ks = [k for k in ks if S.cls(k) == "local"]
        W.at(f"Wage Type Catalogue / LOCAL {st} {stem} / Explanation")
        gaps = S.gaps_for(st, ["local"], prefixes if st == "MO" else None)
        ins = [W.dd("Work State")]
        extra_in = {"IN": ["Indiana county of residence on January 1", "Indiana county of principal employment on January 1"],
                    "MD": ["Maryland county of residence"], "OH": ["Ohio municipality of work", "Ohio municipality of residence",
                           "Ohio school district of residence", "Ohio municipal tax collector"] if stem == "muni" or stem == "school" else [],
                    "PA": ["Pennsylvania PSD code of the work location", "Pennsylvania PSD code of the residence"],
                    "NY": ["New York City or Yonkers residence status", "New York City or Yonkers residence start date",
                           "New York City or Yonkers residence end date"], "KY": ["Kentucky locality of work", "Kentucky locality of residence (school board component)"],
                    "MI": ["Michigan city of residence or predominant place of employment"],
                    "CO": ["Denver occupational privilege tax work location"], "OR": ["Oregon Metro SHS or Multnomah PFA work location",
                           "Oregon Metro SHS or Multnomah PFA opt-in or opt-out"]}.get(st, [])
        if stem in ("lst", "eit", "phl", "pgh"):
            extra_in = extra_in
        ins += [W.dd(x) for x in extra_in]
        ins = list(dict.fromkeys(ins))
        rep_spec = "US-LOC-002" if side == "ER" else "US-LOC-001"
        A(f"loc_{st}_{stem}", name, "Employer Contribution" if side == "ER" else "Tax",
          (f"{name}. " + S.lines(ks) + "." + gaps + f" Inputs: {', '.join(ins)}. Declared: Report Specification {rep_spec}"
           + (" (separate employer return)." if side == "ER" else " and the State or local withholding return.")),
          tax_code="US-TX-11" if side == "ER" else "US-TX-06", side=side, rep=f"{rep_spec} ({st})", payslip=(side == "EE"), inputs=ins,
          legal=sorted({W.rid(k) for k in ks}), fam="local")
    # flags 'no local wage tax' of four States are carried on their income tax / unemployment rows
    return reg
