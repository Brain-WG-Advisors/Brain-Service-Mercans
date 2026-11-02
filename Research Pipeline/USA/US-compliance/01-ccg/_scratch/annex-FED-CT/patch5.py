p='build_annexes.py'; s=open(p,encoding='utf-8').read()
old='''                note = OV.note(unit, f["key"], note)'''
new='''                note = OV.note(unit, f["key"], note)
                if "{{" in note:
                    note = fill(note, facts)'''
assert old in s; s=s.replace(old,new)
open(p,'w',encoding='utf-8').write(s)
o='overrides.py'; t=open(o,encoding='utf-8').read()
t=t.replace('''def note(u, key, n):
    return NOTES.get((u, key), n)''','''def note(u, key, n):
    if (u, key) in NOTES:
        return NOTES[(u, key)]
    for (uu, pre), reps in NOTE_REPS.items():
        if uu == u and key.startswith(pre):
            for a, b in reps:
                n = n.replace(a, b)
    return n


NOTE_REPS = {
    ("FED", "fed.fit.nra.addon"): [("16,100 - 4,300", "{{fed.fit.std_deduction.single}} - {{fed.fit.allowance.pre2020_value}}"),
                                   ("Annual 11,800", "Annual {{fed.fit.nra.addon.table1.annual}}"),
                                   ("single standard deduction 16,100", "single standard deduction {{fed.fit.std_deduction.single}}")],
    ("CO", "co.famli"): [("0.44% employer + 0.44% employee", "{{co.famli.employer.rate}} % employer + {{co.famli.employee.rate}} % employee"),
                         ("SS wage base (184,500)", "SS wage base ({{fed.fica.oasdi.wage_base@2026-01-01}})"),
                         ("only the 0.44% employee share", "only the {{co.famli.employee.rate}} % employee share")],
    ("AR", "ar.pit.high_income"): [("4,701+ 3.7%", "4,701+ {{ar.pit.rate.top}} %")],
}''')
open(o,'w',encoding='utf-8').write(t)
