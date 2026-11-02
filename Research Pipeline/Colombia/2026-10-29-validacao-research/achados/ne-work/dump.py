import openpyxl,sys
wb=openpyxl.load_workbook(sys.argv[1])
out=sys.argv[2]
for ws in wb:
    with open(out+'/'+ws.title.replace(' ','_')+'.txt','w',encoding='utf-8') as f:
        for row in ws.iter_rows():
            for c in row:
                if c.value is not None: f.write(f'{c.coordinate}\t{str(c.value)!r}\n')
