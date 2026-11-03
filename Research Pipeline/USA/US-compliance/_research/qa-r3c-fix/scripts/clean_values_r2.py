import json,sys
fix={
 ('CCG-annex_LA-facts.json','la.live.lac_61_i_1923'):(
  "LAC 61:I.1923 as amended, adopted LR 52:358, effective 2026-03-20: nonresident compensation for duties performed in Louisiana on 30 or fewer days in the calendar year is exempt from Louisiana withholding (A.2.a); the home-state condition (A.2.d) is repealed; the exemption does not apply where the nonresident has other Louisiana-source income (C.1.a); the employee notifies the employer within 10 days from the 31st day (C.1.b.i); the employer withholds and reports on Form L-1 from the period in which the 31st day falls (C.2). Level: withholding and employer reporting.",
  "Final Rule 2603#037 (LR 52:358) replaces the earlier Notice of Intent for the same section and implements Act 382 of 2025 (R.S. 47:112.2, 47:248). C.1.a says 'less than 30 days' while A.2.a and the statute say '30 or fewer'; the statute governs."),
 ('CCG-annex_IA-facts.json','ia.wh.method'):(
  "T1 = G - D; T2 = T1 x 3.80%; T3 = T2 - W/P; T4 = T3 + A (2026 formula, released Nov 2025); wage-bracket tables published as an alternative",None),
}
for f in ('CCG-annex_MA-facts.json','WTC-country_specific-facts.json'):
  fix[(f,'ma.sui.rate_schedule.table')]=("45 account-reserve rows x 7 schedules (positive reserve 17.0+ : A 0.56 / B 0.64 / C 0.73 / D 0.83 / E 0.94 / F 1.07 / G 1.21 ... negative reserve 23+ : 8.62 / 9.79 / 11.13 / 12.65 / 14.37 / 16.33 / 18.55)","The full 45 x 7 rate schedule is in the source document at the cited URL.")
for f in ('CCG-annex_OH-facts.json','WTC-country_specific-facts.json'):
  fix[(f,'oh.pit.municipal.rate_table')]=("The Finder OHMuniRateTable.csv (Ohio Department of Taxation): fields begin date, end date, municipal FIPS, name, rate; 1,083 rows, 678 municipalities with a row in force on 2026-11-01, 14 rate rows beginning 2026-01-01; rates only (no resident credit, no collector)","Ohio Department of Taxation Finder download OHMuniRateTable.csv, retrieved 2026-11-02.")
files=sorted({k[0] for k in fix})
for f in files:
  d=json.load(open(f,encoding='utf-8')); n=0
  for x in d['facts']:
    k=(f,x['key'])
    if k in fix:
      v,note=fix[k]; x['value']=v; n+=1
      if note:
        old=x.get('note')
        x['note']=note if not old else (old if note in old else old.rstrip()+' '+note)
  json.dump(d,open(f,'w',encoding='utf-8',newline='\n'),ensure_ascii=False,indent=2); print(f,n)
