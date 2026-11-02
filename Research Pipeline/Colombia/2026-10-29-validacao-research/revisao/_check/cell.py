import sys,openpyxl
sys.stdout.reconfigure(encoding='utf-8')
wb=openpyxl.load_workbook(sys.argv[1])
for a in sys.argv[2:]:
    s,c=a.split('!'); print(f"== {a}\n{wb[s][c].value}\n")
