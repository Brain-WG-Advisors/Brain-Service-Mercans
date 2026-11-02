"""Leitura pontual de células dos DRAFTs (conferência pessoal). Uso: python -I scripts/spotcheck.py <pasta revisao>"""
import sys, glob, os, openpyxl
sys.stdout.reconfigure(encoding='utf-8')
R = sys.argv[1]


def v(pat, sheet, cells):
    f = glob.glob(os.path.join(R, pat))[0]
    wb = openpyxl.load_workbook(f, read_only=True, data_only=True)
    ws = wb[sheet] if sheet in wb.sheetnames else wb.worksheets[int(sheet)]
    for c in cells:
        print(os.path.basename(f)[:34], ws.title, c, '|', str(ws[c].value)[:170])


v('FORMS/CO-DIAN-004*DRAFT*.xlsx', '3', ['K52', 'K63'])
v('FORMS/CO-DIAN-002*DRAFT*.xlsx', 'Population Rules', ['C5'])
v('PILA/CO-PILA-003*DRAFT*.xlsx', '3', ['G155', 'G156'])
v('PAYSLIP/*DRAFT*.xlsx', 'Colombia (EN)', ['H55'])
v('WTC/*DRAFT*.xlsx', 'Wage Type Catalogue', ['B229'])
