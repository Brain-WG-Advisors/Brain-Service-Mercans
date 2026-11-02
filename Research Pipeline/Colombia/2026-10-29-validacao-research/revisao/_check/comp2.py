import sys, openpyxl
sys.stdout.reconfigure(encoding='utf-8')
wb=openpyxl.load_workbook(sys.argv[1],read_only=True)
ws=wb['Comparativo']
for i,row in enumerate(ws.iter_rows(values_only=True)):
    if row[1] in ('DD-08','NE-05','A-07','A-12'):
        print(row)
