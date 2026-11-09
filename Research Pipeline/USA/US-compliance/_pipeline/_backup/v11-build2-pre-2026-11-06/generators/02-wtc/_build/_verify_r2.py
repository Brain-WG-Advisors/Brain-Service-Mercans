import openpyxl,re,json
ws=openpyxl.load_workbook('02-wtc/US-WTC-001-v1.0.xlsx',read_only=True)['Wage Type Catalogue']
keys="ak.local_wage_tax.exists il.local_wage_tax.exists mo.local.st_louis.earnings.rate mo.local.st_louis.payroll_expense.rate ma.pfml.family.rate ma.pfml.medical.rate ma.sui.rate_schedule.table fed.ccpa.protected_weekly fed.iwo.priority fed.equity.withholding_treatment.resident fed.fit.nra.bik.treatment".split()
txt={r[0]:str(r[3]) for r in ws.iter_rows(min_row=2,values_only=True)}
allt=" ".join(txt.values())
print("tags of 11 keys:",[k for k in keys if "FACT:"+k+"=" in allt])
print("overtime key:", "FACT:fed.obbba.overtime_deduction.level" in allt, "FACT:rspec" , 'FACT:rspec.fed.w2.box_map' in allt)
for c in ('62103','62403','62901','US-051'): print(c, txt.get(c,txt.get(int(c)) if c.isdigit() else '')[:0] if False else '', ('Same tax treatment' in str(txt.get(int(c) if c.isdigit() else c,''))))
print("Same-as-anchor in advance rows:",[k for k,v in txt.items() if 'Advance' in v[:40] and 'Same tax treatment' in v])
print("rows ok")
