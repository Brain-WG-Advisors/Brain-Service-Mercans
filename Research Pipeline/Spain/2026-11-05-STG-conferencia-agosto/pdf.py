import sys, pdfplumber
sys.stdout.reconfigure(encoding='utf-8')
P='C:/Users/instituto/Documents/brain-service/raw/tickets/api/anexos/HRBS-16884/20261105-1419 - Payslips - August 2026 - SCANDINAVIAN TOBACCO GROUP SPAIN SAU- PARALLEL (8).pdf'
with pdfplumber.open(P) as pdf:
    print(len(pdf.pages))
    out=[]
    for i,p in enumerate(pdf.pages):
        out.append('=====PAGE %d\n'%(i+1)+(p.extract_text() or ''))
open('payslips.txt','w',encoding='utf-8').write('\n'.join(out))
