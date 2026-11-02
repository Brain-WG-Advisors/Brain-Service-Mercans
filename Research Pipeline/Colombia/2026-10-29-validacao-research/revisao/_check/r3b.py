import sys,glob,openpyxl
sys.path.insert(0,'_check'); sys.stdout.reconfigure(encoding='utf-8')
from xsurg import edit
NE=glob.glob('NE/*.xlsx')[0]
w=openpyxl.load_workbook(NE,read_only=True); v=w['Version Control']['D14'].value; w.close()
v=v.replace("SIM-03, SIM-04, NE-05, SIM-03 (C21), adjustment-note XSD names (B119, B121).","SIM-04, NE-05, SIM-03 (incl. C21), adjustment-note XSD names (B119, B121).")
edit(NE,{('Version Control','D14'):v}); print(v)
