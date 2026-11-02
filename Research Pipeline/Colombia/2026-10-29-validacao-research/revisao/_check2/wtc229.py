import sys,openpyxl
sys.stdout.reconfigure(encoding='utf-8')
for f in sys.argv[1:3]:
    ws=openpyxl.load_workbook(f,read_only=True)['Wage Type Catalogue']
    rows=list(ws.iter_rows(min_row=1,max_row=230,values_only=True))
    print('==',f[-50:]); 
    for i in (0,1,2,3,227,228,229):
        if i<len(rows): print(i+1,[str(x)[:120] for x in rows[i][:8]])
g=openpyxl.load_workbook(sys.argv[3],read_only=True)
ws=g.worksheets[0]
for i,r in enumerate(ws.iter_rows(values_only=True),1):
    if i in (1,2,228,229,230) or (r and str(r[0])=='62591'): print('G',i,r[:6])
