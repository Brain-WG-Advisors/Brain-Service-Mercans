import openpyxl, sys, copy, datetime
from openpyxl.styles import PatternFill
sys.stdout.reconfigure(encoding='utf-8')
BLUE = PatternFill('solid', fgColor='FFDDEBF7')
SRC_MANUAL = 'TGSS CRA manual (updated 1 Jul 2026), "CRA 0051 a 0054"'

def setc(ws, ref, val):
    ws[ref].value = val
    ws[ref].fill = BLUE

def copy_style(ws, src_row, dst_row, cols):
    for col in cols:
        s = ws[f'{col}{src_row}']; d = ws[f'{col}{dst_row}']
        d.font = copy.copy(s.font); d.border = copy.copy(s.border)
        d.alignment = copy.copy(s.alignment); d.number_format = s.number_format

# ---------- CRA v2.5 ----------
wb = openpyxl.load_workbook('base/ES-CRA-001_ConceptosRetributivos_Spec-export-2026-11-02.xlsx')
ws = wb['Pay Elements with CRA Code']
assert ws['A10'].value in (58188, 58188.0) and ws['F10'].value == 'E'
PRO = ('the amount is reported prorated over the 12 months before the month of termination, '
       'not in the termination month (one CRA record per settlement period; a CRA file may carry several periods). '
       f'Source: {SRC_MANUAL}; Art. 23.2.B RD 2064/1995.')
setc(ws, 'F10', 'I')
setc(ws, 'H10', '02-Nov-26 CORRECTION: indicator I, not E. Under Art. 147.2.c LGSS only the exempt amount of that article (see '
     'CCG v1.8, 9.1) stays outside the contribution base; the excess is part of it, and the CRA manual says the part '
     'included in the base is declared as "I" under 0054. Also, ' + PRO +
     ' Columns C/D mirror the WTC flags for the termination month (the excess enters the base through the prorated L03 '
     'settlements, ES-BASES-001 v3.4). The answer below is superseded.\n\n' + ws['H10'].value)
for r in (8, 9):
    assert ws[f'A{r}'].value in (58184, 58186, 58184.0, 58186.0)
    setc(ws, f'H{r}', '02-Nov-26 CORRECTION: E is right for the exempt amount, but ' + PRO + '\n\n' + ws[f'H{r}'].value)
pr = wb['Population Rules']
assert pr['C13'].value == 'Use CRA 0054 - split into I (above limit) and E (below limit)'
setc(pr, 'C13', 'Use CRA 0054 - split into I (above the exempt amount of Art. 147.2.c LGSS) and E (up to it); both parts '
     'prorated over the 12 months before the month of termination (CRA manual 1 Jul 2026, "CRA 0051 a 0054")')
vc = wb['Version Control']
assert vc['B19'].value in (None, '') and str(vc['B18'].value) == '2,4'
copy_style(vc, 18, 19, 'BCDEF')
for col, v in zip('BCDEF', ['2.5', datetime.datetime(2026, 11, 2),
        'Severance (0054), aligned with CCG v1.8 9.1: 58188 indicator E -> I (excess above the exempt amount of Art. 147.2.c LGSS is part of the contribution base); 58184/58186/58188 reported prorated over the 12 months before the termination month (TGSS CRA manual 1 Jul 2026; Art. 23.2.B RD 2064/1995); Population Rules row 13 updated.',
        'In Progress', 'Wallisson Gomes']):
    setc(vc, f'{col}19', v)
vc['C19'].number_format = vc['C17'].number_format
wb.save('ES-CRA-001_ConceptosRetributivos_Spec_v2.5.xlsx')

# ---------- WTC V4.9 ----------
wb = openpyxl.load_workbook('base/Spain_Wage_Type_Catalogue_V4.8-export-2026-11-02.xlsx')
ws = wb['Wage Type Catalogue']
assert ws['A132'].value in (58188, 58188.0) and ws['P132'].value == 'No' and ws['Q132'].value == 'No'
setc(ws, 'D132', 'Severance excess above the statutory exempt amount. SS: BCCC/BCCP = No, so the excess does not enter '
     'the termination-month base. Under Art. 23.2.B RD 2064/1995 it is prorated over the 12 months before the termination month; '
     'the specs report it through L03 settlements on base codes 500/601 (ES-BASES-001 v3.4) and in the CRA as 0054/I '
     '(ES-CRA-001 v2.5). Tax: subject to IRPF; Irregular Income = Yes (30% reduction of Art. 18.2 LIRPF when its conditions are met). '
     'This one wage type carries both the IRPF taxable excess and the SS excess; they can differ (the EUR 180,000 cap exists '
     'only for IRPF, Art. 7.e LIRPF; the conciliation rules differ, Art. 7.e LIRPF and Art. 147.2.c LGSS), see CCG v1.8, 9.1.')
vc = wb['Version Control']
assert vc['B31'].value in (None, '') and str(vc['B30'].value) == '4.8'
copy_style(vc, 30, 31, 'BCDEF')
for col, v in zip('BCDEF', ['4.9', datetime.datetime(2026, 11, 2),
        '58188: Wage Type Explanation rewritten (flags unchanged). BCCC/BCCP = No kept: the SS excess is prorated over the 12 months before the termination month through L03 (ES-BASES-001 v3.4) and reported in the CRA as 0054/I (ES-CRA-001 v2.5), in line with CCG v1.8 9.1. Removed the outdated "BCCC/BCCP=Yes" and "Subject to Tax=No" remarks.',
        'Under Review', 'Wallisson Gomes']):
    setc(vc, f'{col}31', v)
vc['C31'].number_format = vc['C30'].number_format
wb.save('Spain_Wage_Type_Catalogue_V4.9.xlsx')
print('ok')
