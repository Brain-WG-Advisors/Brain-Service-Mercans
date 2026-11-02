import sys,openpyxl,re
sys.stdout.reconfigure(encoding='utf-8')
pat=re.compile(sys.argv[1])
for f in sys.argv[2:]:
    wb=openpyxl.load_workbook(f,read_only=True)
    for ws in wb.worksheets:
        for row in ws.iter_rows():
            for c in row:
                if isinstance(c.value,str) and pat.search(c.value):
                    m=pat.search(c.value); s=max(0,m.start()-100)
                    print(f.split('/')[-1][:22],ws.title,c.coordinate,'|',c.value[s:m.end()+100].replace('\n',' '))
