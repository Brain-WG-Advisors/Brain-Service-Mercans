import sys,openpyxl,re
sys.stdout.reconfigure(encoding='utf-8')
pat=re.compile(sys.argv[1],re.I)
for f in sys.argv[2:]:
    wb=openpyxl.load_workbook(f,read_only=True)
    for ws in wb.worksheets:
        for row in ws.iter_rows():
            for c in row:
                v=c.value
                if isinstance(v,str) and pat.search(v):
                    m=pat.search(v); s=max(0,m.start()-160)
                    print(f.split('/')[-1][:22],ws.title,c.coordinate,'|',v[s:m.end()+200].replace('\n',' '))
