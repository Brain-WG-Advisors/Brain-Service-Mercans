"""Run every stage for one client and write 02 Validation/_evidence/checks.json."""
import json, os, sys
import nl_check as N
import nl_stage2 as S

key = sys.argv[1]
o, ret, rows, C, base, X = N.run(key)
ev = S.stage2(o, ret, rows, C, base, X)
S.stage3(o, ret, C, X, ev)
S.stage_payrep(o, ret, C, X, ev)
S.stage_gl(o, ret, C, X, ev)
S.stage_master(o, ret, C, X, ev)
import skill_xml
skill_xml.run(o, ret, rows, C, base, X, ev)
os.makedirs(os.path.join(base, "_evidence"), exist_ok=True)
out = dict(client=C["name"], header=ret["header"], namespace=ret["namespace"],
           checks=o.checks, findings=o.findings, recon=o.recon,
           not_tested=o.not_tested, notes=o.notes, ikv_rows=rows,
           per_employee=ev["per_employee"])
json.dump(out, open(os.path.join(base, "_evidence", "checks.json"), "w",
                    encoding="utf-8"), indent=1, default=str, ensure_ascii=False)
for c in o.checks:
    print(c["id"], c["result"], c["check"][:110])
print()
for f in o.findings:
    print(f["severity"], f["control"], f["finding"][:160], "|", str(f["evidence"])[:260])
for r in o.recon:
    print("REC", r["item"], "|", r["a_src"], r["a"], "|", r["b_src"], r["b"], "|", r["diff"], r["result"])
for n in o.notes:
    print("NOTE", n)
