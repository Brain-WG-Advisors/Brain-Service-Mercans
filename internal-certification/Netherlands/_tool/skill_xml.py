"""Run the XML-only controls of the nl-payroll-validator skill (v1.4, adapted to
2026 monthly) and fold them into the client's results. Checks that nl_check.py
already performs from the official 2026 tables are not repeated here."""
import validate as V

SEV = {"Critical": "High", "Major": "Medium", "Observation": "Observation"}


def run(o, ret, rows, C, base, X, ev):
    import os
    V.FREQ = "maand"
    f = V.Findings()
    root, meta, period_el, corrections = V.parse_xml(X(C["xml"]))
    recs = V.nominative(period_el)
    dates = ("2026-09-01", "2026-09-30")
    V.period_gate("loon-over", corrections, f)
    V.check_verloonde_uren(recs, f)
    V.check_leavers_and_contract_fields(recs, f)
    V.check_premium_on_aow(recs, dates, 2026, f)
    V.check_indicators(recs, dates, 2026, f)
    V.check_awf_contract(recs, f)
    V.check_zvw(recs, f)
    V.check_aok_materiality(recs, dates, 2026, f)
    saldi = sum(float(x.get("Saldo") or 0) for x in ret["period"]["saldi"])
    V.check_zeroed_corrections(corrections, {"_saldi_total": str(saldi)}, f)
    for r in f.rows:
        o.find(SEV.get(r["Severity"], "Observation"), r["Area"], r["Finding"],
               r["Evidence"], r["Euro impact"], r["Statutory basis"],
               r["Control"] or "skill", "")
    for c in f.coverage:
        o.check(c["Control"], c["Area"], c["Check"], c["Population"], "Pass")
    for n in f.not_tested:
        o.not_tested.append(dict(id=n.get("Control", ""), item=n["Area"],
                                 reason=n["Reason"], unblock=""))
