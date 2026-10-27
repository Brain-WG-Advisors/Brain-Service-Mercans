"""DD UA V4.2 -> V4.3 (SR-415): 3 campos novos em Country Fields (apos a linha 85)
+ linha 4.3 no Version Control. Cirurgia de XML; demais entradas copiadas byte a byte."""
import re, sys, zipfile
from xml.sax.saxutils import escape

SRC, DST = sys.argv[1], sys.argv[2]

def shift(xml, start, k):
    def row(m):
        r = int(m.group(1))
        return m.group(0) if r < start else m.group(0).replace(f'r="{r}"', f'r="{r+k}"', 1)
    def cell(m):
        col, r = m.group(1), int(m.group(2))
        return m.group(0) if r < start else f'<c r="{col}{r+k}"'
    xml = re.sub(r'<row r="(\d+)"', row, xml)
    return re.sub(r'<c r="([A-Z]+)(\d+)"', cell, xml)

def s(ref, style, text):
    return f'<c r="{ref}" s="{style}" t="inlineStr"><is><t xml:space="preserve">{escape(text)}</t></is></c>'
def n(ref, style, val):
    return f'<c r="{ref}" s="{style}"><v>{val}</v></c>'
def e(ref, style):
    return f'<c r="{ref}" s="{style}"/>'

SRC_FMT = ("Derzhstat, Формат (стандарт) електронного документа звітності респондентів, "
           "version 3.1, Table 1 (C_REG, C_RAJ); Derzhstat directory of statistics bodies SPR_SSCU.XML")
FIELDS = [
    dict(ord='10.0', name='Derzhstat Region Code (C_REG)', code='derzhstat_region_code',
         local='Код області органу державної статистики (C_REG)',
         desc=("Code of the region where the State Statistics Service (Держстат) body to which the employer's "
               "statistical reports are submitted is located (Derzhstat directory SPR_SSCU, REGION/CODE). "
               "Header element C_REG of Derzhstat e-reports (e.g. 1-PV monthly S0301016 and quarterly S0301121). "
               "Not the ДПС code held in DPS Region Code: e.g. м. Київ = 80 in SPR_SSCU and 26 in SPR_STI."),
         fmt='Code as in SPR_SSCU REGION/CODE (e.g. 05, 80)', val='Derzhstat directory SPR_SSCU.',
         note=f'Added SR-415 (Lily Li, 19-Oct-2026). Source: {SRC_FMT}.'),
    dict(ord='11.0', name='Derzhstat District Code (C_RAJ)', code='derzhstat_district_code',
         local='Код району органу державної статистики (C_RAJ)',
         desc=("Code of the district where that Держстат body is located (Derzhstat directory SPR_SSCU, "
               "REGION/LOCAL/CODE). Header element C_RAJ of Derzhstat e-reports (e.g. 1-PV). "
               "Not the ДПС code held in DPS District Code."),
         fmt='Code as in SPR_SSCU REGION/LOCAL/CODE', val='Derzhstat directory SPR_SSCU.',
         note=f'Added SR-415 (Lily Li, 19-Oct-2026). Source: {SRC_FMT}.'),
    dict(ord='12.0', name='Statistical District Code (RAY)', code='statistical_district_code',
         local='Код району (RAY)',
         desc=("District code per КАТОТТГ of the address where the activity reported on is carried out, as held "
               "in the employer's Derzhstat enterprise card. Element RAY of Form 1-PV (S0301016, S0301121). "
               "It has 3 digits, while the district level of the КАТОТТГ Administrative Territory Code has 2."),
         fmt='3 digits', val="Exactly 3 digits; '000' not allowed (Derzhstat common_types, type STATRAY).",
         note=("Added SR-415 (Lily Li, 19-Oct-2026). Source: Derzhstat technical-field lists of S0301016 and "
               "S0301121 (RAY: 3 characters, mandatory, filled automatically from the enterprise card); "
               "Derzhstat common_types.xsd (STATRAY).")),
]

def field_row(r, f):
    c = [e(f'A{r}', 20), s(f'B{r}', 83, 'Ukraine'), s(f'C{r}', 83, 'Employer'), n(f'D{r}', 83, f['ord']),
         s(f'E{r}', 83, f['name']), s(f'F{r}', 83, 'Legal Entity HR'), s(f'G{r}', 83, f['code']),
         s(f'H{r}', 84, f['local']), s(f'I{r}', 82, f['desc']), s(f'J{r}', 83, 'CM'),
         s(f'K{r}', 82, 'When the employer submits Derzhstat e-reports (e.g. 1-PV)'),
         s(f'L{r}', 83, 'Text'), s(f'M{r}', 82, f['fmt']), e(f'N{r}', 82), s(f'O{r}', 82, f['val']),
         s(f'P{r}', 83, 'Employer Information'), n(f'Q{r}', 83, '1.0'), s(f'R{r}', 83, 'employer_information'),
         s(f'S{r}', 83, 'Reporting Details'), n(f'T{r}', 83, '2.0'), s(f'U{r}', 83, 'reporting_details'),
         e(f'V{r}', 82), s(f'W{r}', 83, 'Write'), s(f'X{r}', 83, 'Read'), s(f'Y{r}', 82, f['note'])]
    c += [e(f'{col}{r}', 20) for col in ['Z'] + [f'A{x}' for x in 'ABCDEFGHIJKLMNOPQ']]
    return f'<row r="{r}" ht="15.75" customHeight="1">' + ''.join(c) + '</row>'

VC_TEXT = ("SR-415 (Lily Li, 19/10): added Employer fields Derzhstat Region Code (C_REG), Derzhstat District "
           "Code (C_RAJ) and Statistical District Code (RAY) under Reporting Details (ordinals 10–12), for "
           "Form 1-PV. Source: Derzhstat Format 3.1, Table 1; Derzhstat directory SPR_SSCU; technical-field "
           "lists of S0301016/S0301121.")
vc_row = ('<row r="29" ht="15.75" customHeight="1">' + e('A29', 20) + s('B29', 47, '4.3') +
          n('C29', 53, '46315.0') + s('D29', 49, VC_TEXT) + s('E29', 45, 'Under Review') +
          s('F29', 45, 'Wallisson Gomes') + '</row>')

zin = zipfile.ZipFile(SRC)
zout = zipfile.ZipFile(DST, 'w', zipfile.ZIP_DEFLATED)
for info in zin.infolist():
    data = zin.read(info.filename)
    if info.filename == 'xl/worksheets/sheet5.xml':
        x = data.decode('utf-8')
        x = shift(x, 86, 3)
        i = x.index('<row r="89"')
        x = x[:i] + ''.join(field_row(85 + j, f) for j, f in enumerate(FIELDS, 1)) + x[i:]
        data = x.encode('utf-8')
    elif info.filename == 'xl/worksheets/sheet1.xml':
        x = data.decode('utf-8')
        x = shift(x, 29, 1)
        i = x.index('<row r="30"')
        x = x[:i] + vc_row + x[i:]
        data = x.encode('utf-8')
    zout.writestr(info, data)
zout.close()
print('ok', DST)
