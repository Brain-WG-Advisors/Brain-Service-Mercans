import io
def sub(p, pairs):
    s = io.open(p, encoding="utf-8").read()
    for a, b in pairs:
        if s.count(a) != 1:
            print("COUNT", s.count(a), "in", p, ":", a[:70])
            continue
        s = s.replace(a, b)
    io.open(p, "w", encoding="utf-8", newline="\n").write(s)

# item 6/11 flags
sub("wtc_global.py", [('"leave", "recog", "supp13", "d_basic"', '"leave", "recog", "d_basic"'),
                      ('    if fam in ("bonus", "profit", "disc"):\n        return P.flags_supp(), {}',
                       '    if fam in ("bonus", "profit", "disc", "supp13"):\n        return P.flags_supp(), {}'),
                      ('"federal tax; the supplemental wage rules of the bonus family apply. "',
                       '"federal tax; the supplemental wage rules of the bonus family (anchor 62200) apply: optional flat rate or aggregate method, as on that anchor. "')])
sub("wtc_profiles.py", [("    f.update(income_tax=YN, oasdi=YN, medicare=YN, futa=YN)\n    return f",
                         "    f.update(income_tax=YN, oasdi=YN, medicare=YN, futa=YN, sui=YN, state_programmes=YN)\n    return f")])
sub("wtc_fed2.py", [("Accumulator: \"\n       f\"year-to-date tips for the social security wage base (box 7 {X('base_oasdi_tips')}).",
                     "Washington paid family and medical leave: {val('wa.pfml.base.tips')} [{rid('wa.pfml.base.tips')}]. Accumulator: \"\n       f\"year-to-date tips for the social security wage base (box 7 {X('base_oasdi_tips')}).")])
# item 10
sub("wtc_fed.py", [("{val('fed.fica.totalization.exemption_rule')} \"\n       f\"[{rid('fed.fica.totalization.exemption_rule')}]. Inputs: {D_VISA}, {D_PURPOSE}, {D_TOTAL_CTRY}, {D_TOTAL_EX}.\"),",
                    "{val('fed.fica.totalization.exemption_rule')} \"\n       f\"[{rid('fed.fica.totalization.exemption_rule')}, US-FEDR2-004]. Inputs: {D_VISA}, {D_PURPOSE}, {D_TOTAL_CTRY}, {D_TOTAL_EX}.\"),"),
                   ('legal=["US-FEDS5-005", "US-FEDS5-016", "US-FEDR2-003"], fam="fed_tax")\n\n    A("medicare_ee"',
                    'legal=["US-FEDS5-005", "US-FEDS5-016", "US-FEDR2-003", "US-FEDR2-004"], fam="fed_tax")\n\n    A("medicare_ee"')])
# item 4 class statements
sub("wtc_global_rows.py", [('expl = (f"{name}. Deduction that reverses part of {target}: it reduces the same bases as the earning, so the flags are those of the "',
                            'expl = (f"{name}. Flag class 1 (reversal deduction): Yes means the signed amount reduces that base. Deduction that reverses part of {target}: it reduces the same bases as the earning, so the flags are those of the "')])
sub("wtc_global.py", [('text = (f"Employee pre-tax {label}:', 'text = (f"Employee pre-tax {label} (flag class 2, salary reduction: No means removed from the base before the tax): ')])
