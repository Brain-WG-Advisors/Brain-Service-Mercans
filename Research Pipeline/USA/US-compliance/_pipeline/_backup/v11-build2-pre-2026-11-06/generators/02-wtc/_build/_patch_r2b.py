import io
def sub(p, pairs):
    s = io.open(p, encoding="utf-8").read()
    for a, b in pairs:
        if s.count(a) != 1:
            print("COUNT", s.count(a), "in", p, ":", a[:80]); continue
        s = s.replace(a, b)
    io.open(p, "w", encoding="utf-8", newline="\n").write(s)
OT = "fed.obbba.overtime_deduction.level"
sub("wtc_fed2.py", [
 ("{val('rspec.fed.w2.box_map')} [{rid('rspec.fed.w2.box_map')}]", "{val('rspec.fed.w2.box_map')} [{', '.join(W.rids('rspec.fed.w2.box_map'))}]"),
 ("Nonresident alien employee: {val('fed.fit.nra.bik.treatment')} [{rid('fed.fit.nra.bik.treatment')}]. \"", "Nonresident alien employee: {W.gap('WTC-RQ-15')}. \""),
 ("Priority: {val('fed.iwo.priority')} [{rid('fed.iwo.priority')}]. \"", "Priority between orders: {W.gap('WTC-RQ-13')}. \""),
 ("Priority: {val('fed.iwo.priority')}. Taken after", "Priority: {W.gap('WTC-RQ-13')}. Taken after"),
 ("weekly earnings protected from garnishment \"\n       f\"{val('fed.ccpa.protected_weekly')} [{rid('fed.ccpa.max_rate')}].", "weekly earnings protected from garnishment: \"\n       f\"{W.gap('WTC-RQ-12')}."),
 ("(\"F\", \"RW Deferred Comp 408(k)(6)\"", "(\"F\", \"RW Deferred Comp 408(k)(6)\""),
 ("f\"Employee deferral reported in W-2 box 12 code {cd}. \" + W.gap(\"WTC-RQ-03\", \"treatment of this deferral and the code definition\") +",
  "f\"Employee deferral reported in W-2 box 12 code {cd}: {val('fed.w2.box12.code.' + cd.lower())} [{rid('fed.w2.box12.code.' + cd.lower())}]. \" + W.gap(\"WTC-RQ-03\", \"the tax treatment of this deferral\") +"),
 ("{val('fed.obbba.tips_deduction.level')} [{rid('fed.obbba.tips_deduction.level')}]. Deduction cap \"\n       f\"{val('fed.plaw119_21.qualified_overtime.deduction_cap')} at assessment.",
  "{val('%s')} [{rid('%s')}]. Deduction cap \"\n       f\"{val('fed.plaw119_21.qualified_overtime.deduction_cap')} at assessment." % (OT, OT)),
])
sub("wtc_global.py", [
 ("f\"overtime operates at assessment only and does not reduce withholding: {val('fed.obbba.tips_deduction.level')} \"\n                f\"[{rid('fed.obbba.tips_deduction.level')}].",
  "f\"overtime operates at assessment only and does not reduce withholding: {val('%s')} \"\n                f\"[{rid('%s')}]." % (OT, OT)),
 ("f\"employee, 2026: {val('fed.equity.withholding_treatment.resident')} [{rid('fed.equity.withholding_treatment.resident')}]. \"", "f\"employee, 2026: {W.gap('WTC-RQ-14')}. \""),
 ("W.gap(\"WTC-RQ-02\", \"tax treatment of the advance and of its recovery\")", "W.ug(\"fed.wages.advance_of_wages.classification\", WHY[\"fed.wages.advance_of_wages.classification\"])"),
])
sub("wtc_global_rows.py", [
 ("            expl = (f\"{name}. {kind} Same tax treatment and flags as anchor {anchor_code} ({anc}), which carries the parameters; the variant differs \"\n                    f\"only in how the payroll uses it (rate tier, reason or source). Flags marked Yes-No are conditional as stated on the anchor.\")\n        if role == \"Advance\":\n            expl += \" \" + W.gap(\"WTC-RQ-02\", \"tax treatment of the advance and of its recovery\")",
  "            if role == \"Advance\":\n                expl = f\"{name}. {kind} Anchor of the family: {anchor_code} ({anc}). \" + W.ug(\"fed.wages.advance_of_wages.classification\", G.WHY[\"fed.wages.advance_of_wages.classification\"]) + \". No tax flag is set until the treatment is stated.\"\n            else:\n                expl = (f\"{name}. {kind} Same tax treatment and flags as anchor {anchor_code} ({anc}), which carries the parameters; the variant differs \"\n                        f\"only in how the payroll uses it (rate tier, reason or source). Flags marked Yes-No are conditional as stated on the anchor.\")"),
])
