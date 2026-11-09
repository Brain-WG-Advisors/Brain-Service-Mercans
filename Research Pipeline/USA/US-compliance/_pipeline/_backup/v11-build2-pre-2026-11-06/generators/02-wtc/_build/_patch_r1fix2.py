import io
def sub(p, pairs):
    s = io.open(p, encoding="utf-8").read()
    for a, b, *n in pairs:
        n = n[0] if n else 1
        if s.count(a) != n:
            print("COUNT", s.count(a), "in", p, ":", a[:70])
            continue
        s = s.replace(a, b)
    io.open(p, "w", encoding="utf-8", newline="\n").write(s)

sub("wtc_global.py", [("before the tax):  {val", "before the tax): {val"),
    ('Outside a section "\n                f"125 plan', 'Outside a section "\n                f"125 plan')])
sub("wtc_global.py", [('return (f"Employee contribution to health or life insurance. Through', 'return (f"Employee contribution to health or life insurance (flag class 2, salary reduction through a section 125 plan: No means removed from the base before the tax). Through')])
sub("wtc_common.py", [("def has(key):", '''TABLE_BOX12 = os.path.join(BASE, "00-official-sources", "code-tables", "US-W2-box12.json")


def rq08(text_when_open=None):
    """Reporting code table sentence: the IRS table is held (checked) or the limitation WTC-RQ-08."""
    if os.path.exists(TABLE_BOX12):
        return "the reporting codes are tested against the IRS Form W-2 box 12 code table (US-FEDS5-007)"
    return gap("WTC-RQ-08", "no code table of the annual wage statement is held for the build year")


def has(key):''')])
sub("wtc_fed2.py", [('''+ W.gap("WTC-RQ-08", "no code table of the annual wage statement is held for the build year") + ".",''', '''+ W.rq08() + ".",''', 2)])
sub("build_wtc.py", [
 ('"Wage Type Name in English": r.name,\n', '"Wage Type Name in English": (r.global_desc if r.glob else r.name),\n'),
 ('For a deduction row the flag describes the treatment of the amount deducted (No = removed from "\n              "the base before the tax).',
  'Deduction rows follow one of two classes, stated in column D of the row. Class 1, a reversal deduction (the "\n              "deductions that reverse an earning, codes 21100 to 21213 and the housing and transport deductions): the row carries the flags of the reversed "\n              "earning and Yes = the signed amount reduces that base. Class 2, a salary-reduction or pre-tax deduction (retirement plan deferral, health plan "\n              "contribution): No = removed from the base before the tax.'),
 ('reporting_codes=[], payslip', 'reporting_codes=_rep_codes(r), payslip'),
 ('cw = dict(schema="wtc-crosswalk", wtc_columns', 'cw = dict(schema="wtc-crosswalk", **({"code_table": "00-official-sources/code-tables/US-W2-box12.json"} if os.path.exists(W.TABLE_BOX12) else {}), wtc_columns'),
 ('reason = "" if c else "no wage type reads it: notice template or report-only attribute, consumed by the SIR or the notice, not by a wage type"',
  'reason = "" if c else "notice template input (NY LL 195.1, CO PSL notice) per DD; not a wage-type input"'),
 ('def write_sidecars(res):', '''BOX12 = re.compile(r"box 12 codes? ([A-Z]{1,2})\b")


def _rep_codes(r):
    """W-2 box 12 codes stated in the reporting cell, as 'w2_box12=<code>' (tested by C48 against the authority table)."""
    return [f"w2_box12={c}" for c in dict.fromkeys(BOX12.findall(r.rep or ""))] if os.path.exists(W.TABLE_BOX12) else []


def write_sidecars(res):'''),
])
