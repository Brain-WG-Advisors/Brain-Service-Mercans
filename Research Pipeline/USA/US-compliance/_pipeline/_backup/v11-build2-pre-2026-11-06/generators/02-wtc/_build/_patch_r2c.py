import io
def sub(p, pairs):
    s = io.open(p, encoding="utf-8").read()
    for a, b in pairs:
        if s.count(a) != 1:
            print("COUNT", s.count(a), "in", p, ":", a[:80]); continue
        s = s.replace(a, b)
    io.open(p, "w", encoding="utf-8", newline="\n").write(s)
sub("build_wtc.py", [
 ("(the \"\n              \"deductions that reverse an earning, codes 21100 to 21213 and the housing and transport deductions)", "(the \"\n              \"Deduction rows that reverse an earning of the salary, overtime, salary addition, premium, housing and transport families)"),
 ('{"code_table": "00-official-sources/code-tables/US-W2-box12.json"}', '{"code_table": CHECK_TABLE_REL}'),
 ("def write_sidecars(res):\n", '''CHECK_TABLE_REL = "02-wtc/_build/checks/US-W2-box12-codes.json"


def write_code_table():
    """Checkable form of the IRS code table (code -> validity) derived from the source-hunter file; the source file is not edited."""
    if not os.path.exists(W.TABLE_BOX12):
        return
    t = json.load(open(W.TABLE_BOX12, encoding="utf-8"))
    codes = {c["code"]: {"valid_from": c.get("valid_from"), "valid_to": c.get("valid_to")} for c in t["codes"]["w2_box12"]}
    out = dict(authority=t["authority"], register_id=t["register_id"], source_url=t["source_url"], valid_from=t["valid_from"],
               derived_from="00-official-sources/code-tables/US-W2-box12.json", codes={"w2_box12": codes})
    json.dump(out, open(os.path.join(W.BASE, CHECK_TABLE_REL), "w", encoding="utf-8"), indent=1)


def write_sidecars(res):
    write_code_table()
'''),
])
