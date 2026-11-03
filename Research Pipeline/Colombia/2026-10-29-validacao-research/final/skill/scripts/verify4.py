# Completeness check of the references against the 2026-11-02 finals (copy of verify2.py; paths updated).
import sys, glob, os, re, openpyxl, docx
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from conv import clean, ptext
from docx.oxml.ns import qn
F=r'C:\Users\instituto\Documents\brain-service\Research Pipeline\Colombia\2026-10-29-validacao-research\final'
R=os.path.join(F,'skill','payroll-compliance-colombia','references')
def chk(src, md):
    txt=open(os.path.join(R,md),encoding='utf-8').read()
    tot=miss=0; ex=[]
    if src.endswith('.xlsx'):
        wb=openpyxl.load_workbook(src,read_only=True,data_only=True)
        for ws in wb.worksheets:
            for row in ws.iter_rows(values_only=True):
                for v in row:
                    c=re.sub(r'\bPMI\b','[client]',clean(v))
                    if c:
                        tot+=1
                        if c not in txt: miss+=1; ex.append(c[:90])
    else:
        d=docx.Document(src)
        for p in d.element.body.iter(qn('w:p')):
            c=clean(ptext(p)).replace(' <br> ',' ')
            if c:
                tot+=1
                if c.split(' <br> ')[0][:60] not in txt: miss+=1; ex.append(c[:90])
    print(os.path.basename(src), tot, miss); [print("   ",e) for e in ex[:8]]
chk(os.path.join(F,'CO-CCG-001-v1.7.docx'),'01-ccg.md')
chk(os.path.join(F,'CO-WTC-001-v1.9.xlsx'),'02-wtc.md')
chk(os.path.join(F,'CO-DD-001-v1.6.xlsx'),'05-data-dictionary.md')
chk(os.path.join(F,'CO_Compliance_Payslip_Generator.xlsx'),'06-payslip.md')
for f in sorted(glob.glob(os.path.join(F,'specs','*.xlsx'))): chk(f,'04-reports-spec.md')
