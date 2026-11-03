p='build_annexes.py'; s=open(p,encoding='utf-8').read()
old='(?![\w/-]|\.\d|\]\])", rep, text)'
assert old in s, 'lookahead'
s=s.replace(old,'(?![\w-]|\.\d|\]\])", rep, text)')
old='for _fp in sorted(glob.glob(os.path.join(RES, "CCG-annex_*-facts.json"))):'
assert old in s
s=s.replace(old,'for _fp in sorted(glob.glob(os.path.join(RES, "CCG-annex_*-facts.json"))) + sorted(glob.glob(os.path.join(RES, "*-facts.json"))):')
s=s.replace('''        W(f"| {SRC[rid]} | {clip(r.get('instrument_name', ''))} | {clip(r.get('article_or_section', ''))} | {clip(r.get('authority', ''), 80)} |")''','''        W(f"| {SRC[rid]} | {autotag(clip(r.get('instrument_name', '')), vidx)} | {clip(r.get('article_or_section', ''))} | {clip(r.get('authority', ''), 80)} |")''')
open(p,'w',encoding='utf-8').write(s)
o='overrides.py'; t=open(o,encoding='utf-8').read()
t=t.replace('''NOTES = {}''','''_AL_PHASE = "Phase-out steps by gross income are in the source booklet and carry no facts key (gap in AL.2)."
NOTES = {
    ("AL", "al.wh.std_deduction.single.max"): _AL_PHASE,
    ("AL", "al.wh.std_deduction.married.max"): _AL_PHASE,
    ("AL", "al.wh.std_deduction.married_separate.max"): _AL_PHASE,
    ("AL", "al.wh.std_deduction.head_of_family.max"): _AL_PHASE,
    ("AL", "al.wh.personal_exemption.single"): "Status 0: no exemption; single and married filing separately: this amount; married and head of family: {{al.wh.personal_exemption.married}}.",
    ("AL", "al.wh.dependent.gi_to_50000"): "Per dependent, by the employee's gross-income band (amounts in the next two rows).",
    ("FED", "fed.bik.dependent_care.exclusion"): "Half for married filing separately; raised by P.L. 119-21.",
    ("CT", "ct.tipped.employer_share.hotel_restaurant"): "Fixed employer cash wage; maximum tip credit 2026 {{ct.tipped.max_tip_credit.hotel_restaurant}} (minimum wage {{ct.minwage.hourly@2026-01-01}} less the employer share). Bartenders: employer share {{ct.tipped.employer_share.bartender}}. Other industries and meal credits: in the source. No cannabis tip credit from 2026-10-01 (PA 26-12 s.6).",
    ("CO", "co.sui.new_employer.rate.total"): "Sum of the base rate, the support surcharge and the solvency surcharge for non-construction employers; heavy-construction and 2027 rates are in the source and carry no facts key.",
    ("CA", "ca.sui.employer.rate.min"): None,
}''')
t=t.replace('''def note(u, key, n):
    if (u, key) in NOTES:
        return NOTES[(u, key)]''','''def note(u, key, n):
    if (u, key) in NOTES and NOTES[(u, key)] is not None:
        return NOTES[(u, key)]''')
t=t.replace('''    ("AR", "ar.pit.high_income"): [''','''    ("FED", "fed.levy"): [("16,100", "{{fed.fit.std_deduction.single}}")],
    ("CA", "ca.sui"): [("max 434/employee", "max {{ca.sui.max_per_employee}}/employee")],
    ("AR", "ar.pit.high_income"): [''')
open(o,'w',encoding='utf-8').write(t)
c='content.py'; u=open(c,encoding='utf-8').read()
u=u.replace('**Overtime:** the Act 2026-604 deduction "\n    "(up to','**Overtime:** the 2026 overtime-premium deduction "\n    "(up to')
u=u.replace('Withholding wages; section 125 exclusion ({{ar.sui.wages.section125_excluded}} for UI)','Withholding wages; cafeteria-plan exclusion ({{ar.sui.wages.section125_excluded}} for UI)')
u=u.replace('"Arkansas withholding wages exclude the federal exclusions for combat pay (IRC 112), cafeteria plans (IRC 125), IRAs "\n    "(IRC 219) and 401(k)','"Arkansas withholding wages exclude the federal exclusions for combat pay, cafeteria plans, IRAs "\n    "and 401(k)')
u=u.replace('in the first language of a qualifying share of the workforce (8-13.3-408(2));','in the first language of a qualifying share of the workforce;')
open(c,'w',encoding='utf-8').write(u)
print('Act 2026-604' in u, 'IRC 125' in u, '8-13.3-408' in u)
