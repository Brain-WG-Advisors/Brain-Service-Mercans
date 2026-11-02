import sys,openpyxl,re
sys.stdout.reconfigure(encoding='utf-8')
pat=re.compile(sys.argv[1],re.I)
for f in sys.argv[2:]:
    wb=openpyxl.load_workbook(f,read_only=True)
    for ws in wb.worksheets:
        for r in ws.iter_rows():
            for c in r:
                if isinstance(c.value,str) and pat.search(c.value):
                    print(f"{f[-45:-30]}|{ws.title}!{c.coordinate}: {c.value[:int(__import__('os').environ.get('W','300'))]}")
