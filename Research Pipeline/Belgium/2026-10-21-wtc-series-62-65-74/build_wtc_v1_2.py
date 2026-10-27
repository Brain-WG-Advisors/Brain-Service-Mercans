"""BE-WTC-001 v1.2: corrige a taxa patronal básica na linha 23671 (Wage Type Catalogue!F58).

Fonte: Instruções administrativas ONSS, "Les cotisations" › "Le pourcentage de cotisation globalisé" e
"La cotisation de modération salariale" (edição 2025/4, lida em 21/10/2026 via cópia arquivada de 07/12/2025;
a mesma página foi lida no site em 13/10/2026). Edição por XML a partir da v1.1 (sem openpyxl.save).
Uso: python -I build_wtc_v1_2.py BE-WTC-001-v1.1.xlsx BE-WTC-001-v1.2.xlsx
"""
import sys, re, zipfile, html

SRC, OUT = sys.argv[1:3]
NEW_F58 = ("White-collar (categories 1 and 3 of the structural reduction): basic employer contribution 19.88% from "
           "Q1 2018 (tax shift - Law of 26 December 2015 and Law of 16 May 2016; 24.92% was the basic rate from Q1 2015), "
           "of which pensions 8.86%, medical care 3.80%, sickness and disability 2.35%, unemployment 1.46%, occupational "
           "diseases 1.00%, work accidents 0.30% and the remaining branches, plus the wage moderation contribution of at "
           "most 5.12% [(19.88 x 0.0427) + 4.27], giving approximately 25.00% (NSSO administrative instructions, "
           "'Les cotisations' - 'Le pourcentage de cotisation globalise' and 'La cotisation de moderation salariale'). "
           "Blue-collar: the whole base is the gross at 108%, giving approximately 30.57%. Employer contributions are NOT "
           "due on the double holiday pay. The basic and wage moderation contributions are not due on the part of the "
           "quarterly wage above EUR 86,700 from 1 January 2026 (see BE-033).")
OLD_START = "White-collar: basic employer contribution 24.92%"
DESC = ("Employer global social security contribution (23671, row 58, Formula): basic employer rate corrected from 24.92% "
        "to 19.88% from Q1 2018 plus wage moderation of at most 5.12% (about 25.00%), per the NSSO administrative "
        "instructions. Same correction as the CCG of 13 October 2026. Highlighted in light blue.")

zin = zipfile.ZipFile(SRC)
parts = {n: zin.read(n) for n in zin.namelist()}
ss = re.findall(r'<si>.*?</si>', parts['xl/sharedStrings.xml'].decode('utf-8'), re.S)

sh = parts['xl/worksheets/sheet2.xml'].decode('utf-8')
m = re.search(r'<c r="F58" s="(\d+)" t="s"><v>(\d+)</v></c>', sh)
assert m, 'F58 não encontrado como shared string'
old_text = html.unescape(re.sub(r'<[^>]+>', '', ss[int(m.group(2))]))
assert old_text.startswith(OLD_START), old_text[:80]

# estilo azul: o clone de s=22 com fill FFDDEBF7 criado na v1.1 (id 96)
sty = parts['xl/styles.xml'].decode('utf-8')
xfs = re.findall(r'<xf\b[^>]*?(?:/>|>.*?</xf>)', re.search(r'<cellXfs[^>]*>(.*?)</cellXfs>', sty, re.S).group(1), re.S)
fills = re.findall(r'<fill>.*?</fill>', re.search(r'<fills[^>]*>(.*?)</fills>', sty, re.S).group(1), re.S)
blue_fill = [i for i, f in enumerate(fills) if 'FFDDEBF7' in f][0]
cand = [i for i, x in enumerate(xfs) if f'fillId="{blue_fill}"' in x and
        re.sub(r'fillId="\d+"|applyFill="\d" ', '', x) == re.sub(r'fillId="\d+"|applyFill="\d" ', '', xfs[int(m.group(1))])]
assert cand, 'clone azul do estilo de F58 não encontrado'
newcell = f'<c r="F58" s="{cand[0]}" t="inlineStr"><is><t xml:space="preserve">{html.escape(NEW_F58, quote=False)}</t></is></c>'
sh = sh[:m.start()] + newcell + sh[m.end():]
parts['xl/worksheets/sheet2.xml'] = sh.encode('utf-8')

vc = parts['xl/worksheets/sheet1.xml'].decode('utf-8')
vals = {'B15': ('1.2', 'n'), 'C15': ('46316', 'n'), 'D15': (DESC, 's'), 'E15': ('Under Review', 's'), 'F15': ('Wallisson Gomes', 's')}
def vcell(mm):
    ref, s = mm.group(1), mm.group(2)
    v, t = vals[ref]
    if t == 'n':
        return f'<c r="{ref}" s="{s}"><v>{v}</v></c>'
    return f'<c r="{ref}" s="{s}" t="inlineStr"><is><t xml:space="preserve">{html.escape(v, quote=False)}</t></is></c>'
vc, n = re.subn(r'<c r="([B-F]15)" s="(\d+)"/>', vcell, vc)
assert n == 5, n
parts['xl/worksheets/sheet1.xml'] = vc.encode('utf-8')

with zipfile.ZipFile(OUT, 'w') as zout:
    for info in zin.infolist():
        zout.writestr(info, parts[info.filename], compress_type=info.compress_type)
print('ok', OUT, 'F58 estilo', cand[0])
