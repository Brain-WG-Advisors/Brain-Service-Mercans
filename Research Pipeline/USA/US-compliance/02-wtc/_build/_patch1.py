import re
def sub(p, pairs):
    s = open(p, encoding="utf-8").read()
    for a, b in pairs:
        if a not in s:
            print("MISSING in", p, ":", a[:70])
        s = s.replace(a, b)
    open(p, "w", encoding="utf-8").write(s)

sub("wtc_common.py", [('        gap_def(gid, what, u.get("what_would_close_it") or "the official source that states it", key,',
                       '        gap_def(gid, u.get("why") or what, u.get("what_would_close_it") or "the official source that states it", key,')])
sub("wtc_states.py", [('        why = WHY.get(key) or _neutral(u["why"])', '        why = WHY_TXT[key]'),
                      ('import wtc_fed as F\n', 'import wtc_fed as F\nfrom wtc_why import WHY as WHY_TXT\n')])
sub("wtc_fed.py", [('W.ug("fed.fit.2027.tables", "2027 withholding tables are not published; only the 2026 tables are configured")', 'W.ug("fed.fit.2027.tables", WHY["fed.fit.2027.tables"])'),
                   ('W.ug("fed.futa.credit_reduction.2026.final", "the 2026 credit reduction is potential until the Department of Labor determination, so it is not modelled as final")', 'W.ug("fed.futa.credit_reduction.2026.final", WHY["fed.futa.credit_reduction.2026.final"])'),
                   ('import wtc_profiles as P\n', 'import wtc_profiles as P\nfrom wtc_why import WHY\n')])
sub("wtc_global.py", [('W.ug("fed.bik.mileage.rate", "the 2026 business standard mileage rate is not carried")', 'W.ug("fed.bik.mileage.rate", WHY["fed.bik.mileage.rate"])'),
                      ('W.ug("fed.plan.402g.elective_deferral.limit_2027", "the 2027 limits are not published and are not configured")', 'W.ug("fed.plan.402g.elective_deferral.limit_2027", WHY["fed.plan.402g.elective_deferral.limit_2027"])'),
                      ('import wtc_fed as F\n', 'import wtc_fed as F\nfrom wtc_why import WHY\n')])
