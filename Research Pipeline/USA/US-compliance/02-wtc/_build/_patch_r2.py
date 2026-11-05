import io
def sub(p, pairs):
    s = io.open(p, encoding="utf-8").read()
    for a, b in pairs:
        if s.count(a) != 1:
            print("COUNT", s.count(a), "in", p, ":", a[:80]); continue
        s = s.replace(a, b)
    io.open(p, "w", encoding="utf-8", newline="\n").write(s)

sub("wtc_why.py", [('WHY = {\n', '''WHY = {
    "fed.wages.advance_of_wages.classification": "whether an advance of wages is wages for federal income tax, social security, Medicare and FUTA when paid, and how its recovery is treated, is not stated by the registered sources",
    "ut.sit.schedule.before_2026_04_01": "the withholding schedule in force before the current Utah publication is not captured, so no earlier period is configured",
    "ak.local_wage_tax.exists": "whether Alaska has a local wage tax is not confirmed against a stored copy of the authority page",
    "il.local_wage_tax.exists": "whether Illinois has a local wage tax is not confirmed against a stored copy of the authority page",
    "mo.local.st_louis.earnings.rate": "the St. Louis earnings tax rate is not confirmed against a stored copy of the authority page",
    "mo.local.st_louis.payroll_expense.rate": "the St. Louis payroll expense tax rate is not confirmed against a stored copy of the authority page",
    "ca.local.minimum_wage": "no register of local minimum wages is kept by the State authority",
    "de.levy.blue_collar_training": "the Delaware blue collar training tax is filed manually and is not configured",
''')])
sub("wtc_states.py", [
 ('"sit": ("sit", "wh", "pit", "base"), "sui": ("sui", "ui", "base"),', '"sit": ("sit", "wh", "pit", "base", "local_wage_tax"), "sui": ("sui", "ui", "base"),'),
 ('def open_items(st, kinds):', 'def open_items(st, kinds, prefixes=None):'),
 ('        if len(p) > 1 and p[1] in okp:\n', '        if len(p) > 1 and p[1] == "local_wage_tax" and "sui" in kinds and st.upper() not in NO_WAGE_TAX:\n            continue\n        if prefixes and not any(".".join(p[1:]).startswith(x) for x in prefixes):\n            continue\n        if len(p) > 1 and p[1] in okp:\n'),
 ('def gaps_for(st, kinds):\n    parts = []\n    for key in open_items(st, kinds):', 'def gaps_for(st, kinds, prefixes=None):\n    parts = []\n    for key in open_items(st, kinds, prefixes):'),
 ('    for k in keys:\n        if k in skip:\n            continue\n        CONSUMED.add(k)\n        out.append(line(k))',
  '    for k in keys:\n        if k in skip:\n            continue\n        CONSUMED.add(k)\n        if k in W.RESIDUAL:\n            out.append(W.gap(*W.RESIDUAL[k]))\n            continue\n        out.append(line(k))'),
])
sub("wtc_states2.py", [('gaps = S.gaps_for(st, ["local"])', 'gaps = S.gaps_for(st, ["local"], prefixes if st == "MO" else None)')])
sub("wtc_common.py", [('GAPS = {}       # id', '''# Residual keys of the R2 facts: proven only in part (derived, multi-source or unlocated). Printed as the neutral gap, no figure.
RESIDUAL = {
    "ma.pfml.family.rate": ("WTC-RQ-10", "the Massachusetts paid family and medical leave rates are derived from a split that the source does not print"),
    "ma.pfml.medical.rate": ("WTC-RQ-10", "the Massachusetts paid family and medical leave rates are derived from a split that the source does not print"),
    "ma.sui.rate_schedule.table": ("WTC-RQ-11", "one cell of the Massachusetts unemployment insurance rate schedule is not located in the stored copy"),
}
GAPS = {}       # id''')])
sub("wtc_gaps.py", [('\n\nGENERIC_RQ', '''
    g("WTC-RQ-10", "the Massachusetts paid family and medical leave rates are derived from a split that the source does not print; no rate is written",
      "the Department of Family and Medical Leave rate page or regulation stating the family and medical rates as figures, with a register row",
      "ma.pfml.family.rate", domain="social_security")
    g("WTC-RQ-11", "one cell of the Massachusetts unemployment insurance rate schedule is not located in the stored copy; the schedule is not written",
      "a complete copy of the Massachusetts rate schedule with every cell located, as a register row",
      "ma.sui.rate_schedule.table", domain="social_security")
    g("WTC-RQ-12", "the weekly protected earnings amount of the consumer credit protection limit is derived (30 times the federal minimum hourly wage) and is not printed in the stored copy; no figure is written",
      "the Department of Labor fact sheet or 15 USC 1673 text with the amount stated, as a register row",
      "fed.ccpa.protected_weekly", domain="statutory_reporting")
    g("WTC-RQ-13", "the priority between several income withholding orders is not stated by the registered source (Publication 1494 carries no such rule)",
      "the official text on the priority of support orders over other garnishments and between orders, as a register row",
      "fed.iwo.priority", domain="statutory_reporting")
    g("WTC-RQ-14", "the 2026 federal withholding treatment of equity compensation of a resident employee combines several sources and is not proven clause by clause",
      "a clause-by-clause check of Publications 15-B, 15-T and 515 and the regulation on stock-based wages, entered as separate facts",
      "fed.equity.withholding_treatment.resident", domain="income_tax", severity="major")
    g("WTC-RQ-15", "the withholding treatment of benefits in kind of a nonresident alien combines several sources and is not proven clause by clause",
      "a clause-by-clause check of Publications 15-B, 15-T and 515 as separate facts",
      "fed.fit.nra.bik.treatment", domain="income_tax")


GENERIC_RQ'''), ('"WTC-RQ-08", "WTC-RQ-09"]', '"WTC-RQ-08", "WTC-RQ-09", "WTC-RQ-10", "WTC-RQ-11", "WTC-RQ-12", "WTC-RQ-13", "WTC-RQ-14", "WTC-RQ-15"]')])
