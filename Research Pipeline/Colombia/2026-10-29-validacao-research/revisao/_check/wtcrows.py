import sys, openpyxl, collections
sys.stdout.reconfigure(encoding='utf-8')
wb=openpyxl.load_workbook(sys.argv[1],read_only=True)
ws=wb['Wage Type Catalogue']
rows=list(ws.iter_rows(values_only=True))
hdr=None
for i,r in enumerate(rows[:8]):
    print(i+1,[str(x)[:70] if x else '' for x in r])
for n in [108,109,110,111,120,121,122,123,154,155,156,229,309,310,311,312,313,321,322,323,324,326,334,335,338]:
    r=rows[n-1]
    print(n,'B=',str(r[1])[:60],'| D=',str(r[3])[:50],'| F=',str(r[5])[:120],'| N..X=',r[13:24])
print(collections.Counter(r[21] for r in rows[8:]))
