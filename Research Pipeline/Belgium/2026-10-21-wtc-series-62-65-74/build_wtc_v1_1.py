"""BE-WTC-001 v1.1: acrescenta as séries 62 / 65 / 79 do Global WTC 1.1 que faltam.

Base: export do Drive de 16/10 (BE-WTC-001-v1.0). Edição por XML (sem openpyxl.save),
para preservar imagem, comentários e validações. Linhas novas entram a partir da 361
(depois de BE-059), em azul claro FFDDEBF7; nada das linhas 2-360 muda.
Uso: python -I build_wtc_v1_1.py <base.xlsx> <global_1_1.xlsx> <saida.xlsx>
"""
import sys, re, zipfile, csv, os, html
import openpyxl

BASE, GLOBAL, OUT = sys.argv[1:4]
HERE = os.path.dirname(os.path.abspath(__file__))

def norm(v):
    if isinstance(v, float) and v.is_integer():
        v = int(v)
    return '' if v is None else str(v).strip()

# ---------------------------------------------------------------- mapeamento
# código Global -> linha BE equivalente (cujo col F já traz a base legal)
M = {}
def put(codes, analog, note=''):
    for c in codes:
        M[str(c)] = (analog, note)
def rng(a, b):
    return range(a, b + 1)

NA_EOS = 'NA:Belgium has no statutory end-of-service gratuity (see 62900, which carries the pro rata end-of-year premium instead).'
NA_CONTR = 'NA:Payments to independent contractors are not remuneration under an employment contract and are outside the Belgian payroll.'
NA_OPEN = 'NA:No Belgian treatment was established for this slot in revision 1.1; it stays not applicable until a client case defines it.'
NA_UNPAID = 'NA:Unpaid leave carries no pay in Belgium; the unpaid days are handled through 62109 and the reduction 21109.'

# 4 dígitos
put([6201, 6210, 6216], '62100')
put([6202, 6203, 6277, 6278], '62222')
put([6211], '62110', 'The overtime supplement is carried separately in 62111 to 62113.')
put([6212], '62901')
put([6213], NA_EOS)
put([6214], '62203')
put([6215], '62129')
put([6217], '62170')
put([6218], '62143')
put([6220, 6228], '62200')
put([6221, 6224], '62210')
put([6222], '62220')
put([6223, 6225, 6226], '62202')
put([6227], '62883')
put([6230, 6231], '62300')
put([6232], '62960')
put([6233, 6234, 6235], '62305', 'Unused statutory leave is not paid out during employment; it is settled only on departure.')
put([6239], '62190', 'The statutory maternity benefit itself is paid by the health insurance fund, not through payroll; this slot carries an employer top-up.')
put([6240], '62430')
put([6241], '62400')
put([6250, 6253, 6254, 6271, 6280, 6283, 6284, 6285, 6287], 'BE-059')
put([6251], '62500')
put([6252], '62540')
put([6255], '62520')
put([6256, 6258], '62560')
put([6257], '62570')
put([6259], '62591', 'A gift within the exempt amount goes to 62590.')
put([6260, 6261, 6263], '62610')
put([6262], '62643')
put([6264], '62640')
put([6265], '62650')
put([6266, 6267, 6268, 6269], '62670')
put([6270, 6274], '62740')
put([6272], '62148')
put([6273, 6275], '62360', 'Treated as a cash allowance with no exemption of its own.')
put([6276], '62760')
put([6279], '62144')
put([6281, 6286], '62360', 'A cash meal or food allowance is ordinary remuneration; only meal vouchers meeting their conditions (62660) are exempt.')
put([6282], 'BE-056')
put([6289], '62100', 'Default treatment as ordinary remuneration until the element is defined for a client.')
# 5 dígitos, série 62
put(rng(62156, 62159), '62150')
put(rng(62230, 62249), '62220')
put([62301], '62101')
put([62442], '62402')
put([62452], '62412')
put([62461], '62101')
put([62462], '62102')
put([62617], '62610')
put([62644, 62649], '62642')
put([62651, 62652, 62653], '62650')
put([62671], '62670')
put(rng(62681, 62689), '62680')
put([62701, 62702], '62700')
put([62712], '62710')
put([62722], '62720')
put([62731, 62732], '62730')
put([62742], '62740')
put([62752], '62750')
put([62761], '62760')
put(rng(62771, 62779), '62222')
put([62780, 62781], '62760')
put([62782], '62762')
put(list(rng(62800, 62809)) + list(rng(62830, 62859)), 'BE-059')
put([62810, 62811, 62820, 62821], NA_OPEN)
put(rng(62860, 62865), '62360', 'A cash meal or food allowance is ordinary remuneration; only meal vouchers meeting their conditions (62660) are exempt.')
put([62866, 62867], '62591', 'Treated as a cash allowance with no exemption of its own.')
put([62868, 62869], '62224', 'Where the amount, occasion or frequency condition is breached, the whole value goes to 62229.')
put([62874], '62360', 'Treated as a cash allowance with no exemption of its own.')
put([62884], '62883')
put(list(rng(62891, 62899)) + [62992] + list(rng(62995, 62999)), '62890',
    'Depending on the plan, 62991 (earlier grant), 62993 (not accepted within 60 days) or 62994 (free shares / RSU) may apply instead.')
put([62905], '62901')
put([62909], NA_EOS)
put(list(rng(62921, 62925)) + list(rng(62931, 62935)), '62930')
put(rng(62940, 62949), NA_CONTR)
put([62970] + list(rng(62973, 62979)) + list(rng(62983, 62989)), '62100', 'A salary addition is ordinary remuneration.')
put([62971, 62981], '62141')
put([62972, 62982], '62142')
# série 65
put([65220, 65221, 65222], '62670')
put([65400], '62400'); put([65401], '62401'); put([65402], '62402')
put([65410], '62410')
put([65500], '62500'); put([65501], '62501'); put([65502], '62502')
put([65510, 65511, 65512], '62503')
put(rng(65520, 65523), '62505')
put(list(rng(65570, 65572)) + list(rng(65580, 65582)), '62570')
put([65600, 65601, 65602, 65608, 65620], 'BE-057')
put([65610, 65611, 65612], 'BE-059')
put([65630], '62610')
put([65650, 65651, 65652], 'BE-056')
put([65660, 65661, 65662], '62360', 'A cash meal allowance is ordinary remuneration; only meal vouchers meeting their conditions (62660) are exempt.')
put([65670], '62660'); put([65671], '62661'); put([65672], '62662')
put(list(rng(65700, 65702)) + list(rng(65710, 65712)), '62190',
    'The statutory maternity benefit itself is paid by the health insurance fund, not through payroll; this slot carries an employer top-up.')
put([65720], '62740')
put(rng(65770, 65779), '62770')
put(list(rng(65800, 65869)) + list(rng(65880, 65899)), '62670')
# série 79
put([79401, 79450, 79452], '62305', 'Unused statutory leave is not paid out during employment; it is settled only on departure.')
put([79402, 79405], '62966')
put([79403, 79409], '62720')
put([79404], '62966', 'Belgium has no statutory leave of this kind; where granted by contract, the pay follows the paid short-leave treatment.')
put([79406], '62190', 'The statutory maternity benefit itself is paid by the health insurance fund, not through payroll; this slot carries an employer top-up.')
put([79407], '62967')
put([79408, 79468, 79478], '62960')
put([79410], NA_UNPAID)
put(list(rng(79411, 79449)) + list(rng(79480, 79499)), '62966')

# ---------------------------------------------------------------- holandês
NL = {
 'Annual leave pay': 'Enkel vakantiegeld', 'Assignment salary': 'Loon tijdens detachering',
 'Awards plan 1': 'Beloningsplan 1', 'Awards plan 1 N>B': 'Beloningsplan 1 (netto naar bruto)',
 'Awards plan 2': 'Beloningsplan 2', 'Awards plan 2 N>B': 'Beloningsplan 2 (netto naar bruto)',
 'Basic salary': 'Basisloon', 'Basic salary (special)': 'Basisloon (bijzonder)',
 'Benefit earning': 'Voordeel van alle aard', 'Benefit earning (notional tax base)': 'Voordeel van alle aard (fictieve belastbare basis)',
 'Benefits in-kind': 'Voordelen in natura', 'Benefits plan 1': 'Voordelenplan 1', 'Benefits plan 1 (non-cash)': 'Voordelenplan 1 (niet in geld)',
 'Benefits plan 2': 'Voordelenplan 2', 'Benefits plan 2 - Grossup Value': 'Voordelenplan 2 - brutowaarde (gross-up)', 'Benefits plan 3': 'Voordelenplan 3',
 'Birth allowance': 'Geboortevergoeding', 'Birth and Marriage Allowance': 'Geboorte- en huwelijksvergoeding',
 'Bonus (annual, referral, etc)': 'Bonus (jaarlijks, aanbreng, enz.)', 'Bonus - profit sharing': 'Bonus - winstdeelname',
 'Bonuses - discretionary or one-time': 'Bonussen - discretionair of eenmalig', 'Bonuses - post-termination': 'Bonussen - na uitdiensttreding',
 'Bonuses, Incentives and Premiums': 'Bonussen, incentives en premies', 'Car Fuel Benefit': 'Voordeel brandstof bedrijfswagen',
 'Car allowance - employee is using personal car for business purposes': 'Autovergoeding - eigen wagen voor dienstverplaatsingen',
 'Car benefit': 'Voordeel van alle aard bedrijfswagen', 'Car cash benefit': 'Autovergoeding in geld', 'Commission': 'Commissieloon',
 'Contractor payments': 'Betalingen aan zelfstandige contractanten', 'Custom pay element': 'Specifiek looncomponent',
 'Death allowance': 'Overlijdensvergoeding', 'Donation recovery': 'Terugvordering schenking',
 'Education & Schooling allowance 2': 'Opleidings- en schoolvergoeding 2', 'Education & Schooling allowance 3': 'Opleidings- en schoolvergoeding 3',
 'Education & Schooling allowance 4': 'Opleidings- en schoolvergoeding 4', 'Education & Schooling allowance 5': 'Opleidings- en schoolvergoeding 5',
 'Education Benefit': 'Voordeel opleiding', 'Education allowance': 'Opleidingsvergoeding', 'Emergency leave payout': 'Uitbetaling noodverlof',
 'End of service gratuity': 'Vergoeding einde dienst (end of service)', 'Entertainment allowance': 'Vergoeding voor ontvangstkosten',
 'Examination leave payout': 'Uitbetaling examenverlof', 'Expense advances': 'Voorschotten op kosten', 'Expense recovery': 'Terugvordering kosten',
 'Expense reimbursement': 'Onkostenvergoeding', 'Family allowance': 'Gezinsvergoeding', 'Family allowance (MLA, Children)': 'Gezinsvergoeding (kinderen)',
 'Food allowance': 'Voedingsvergoeding', 'Gift allowance/voucher': 'Geschenkvergoeding / geschenkcheque',
 'Gratuity, EOS, Post-termination, etc.': 'Vergoeding bij uitdiensttreding e.a.', 'Hajj leave payout': 'Uitbetaling hadj-verlof',
 'Hardship allowance': 'Vergoeding voor moeilijke omstandigheden', 'Health Insurance Benefit': 'Voordeel ziektekostenverzekering',
 'Health care': 'Gezondheidszorg', 'Housing & Rent allowance 2': 'Huisvestings- en huurvergoeding 2',
 'Housing & Rent allowance 3': 'Huisvestings- en huurvergoeding 3', 'Housing & Rent allowance 4': 'Huisvestings- en huurvergoeding 4',
 'Housing Utility benefit': 'Voordeel nutsvoorzieningen woning', 'Housing allowance': 'Huisvestingsvergoeding', 'Housing benefit': 'Voordeel huisvesting',
 'In-kind company car usage': 'Voordeel van alle aard - gebruik bedrijfswagen', 'In-kind company housing': 'Voordeel van alle aard - woning van de onderneming',
 'In-kind medical insurance': 'Voordeel van alle aard - medische verzekering', 'Incentives and performance bonuses': 'Incentives en prestatiebonussen',
 'Incentives plan 1': 'Incentiveplan 1', 'Incentives plan 2': 'Incentiveplan 2',
 'Leave balance payout (leavers and non-leavers)': 'Uitbetaling verlofsaldo (vertrekkers en niet-vertrekkers)',
 'Life insurance Installments / Contributions': 'Levensverzekering - premies / bijdragen', 'Marriage leave payout': 'Uitbetaling huwelijksverlof',
 'Maternity Allowance (cash benefit)': 'Moederschapsuitkering (in geld)', 'Maternity allowance (benefit) 1': 'Moederschapsvergoeding (voordeel) 1',
 'Maternity allowance (benefit) 2': 'Moederschapsvergoeding (voordeel) 2', 'Maternity leave payout': 'Uitbetaling moederschapsverlof',
 'Meal allowance': 'Maaltijdvergoeding', 'Meal benefit': 'Voordeel maaltijden', 'Meal cash benefit': 'Maaltijdvergoeding in geld',
 'Meal vouchers': 'Maaltijdcheques', 'Meal/food allowance': 'Maaltijd- / voedingsvergoeding', 'Medical insurance / Medical Care': 'Medische verzekering / medische zorg',
 'On-call duty': 'Wachtdienst', 'On-site provided meal': 'Maaltijd ter plaatse verstrekt', 'Other leave payout': 'Uitbetaling ander verlof',
 'Overtime': 'Overuren', 'Paid leave (PTO)': 'Betaald verlof', 'Parking allowance': 'Parkeervergoeding', 'Paternity leave payout': 'Uitbetaling vaderschapsverlof',
 'Pensions & Pension Contributions': 'Pensioenen en pensioenbijdragen', 'Pensions & Pension Refunds': 'Pensioenen en terugbetaling pensioenbijdragen',
 'Per diem allowance': 'Dagvergoeding', 'Per diem benefit': 'Voordeel dagvergoeding', 'Personal allowance': 'Persoonlijke vergoeding',
 'Phone benefit': 'Voordeel telefoon', 'Phone benefit (GL)': 'Voordeel telefoon (GL)', 'Phone benefit 2': 'Voordeel telefoon 2',
 'Phone cash benefit': 'Telefoonvergoeding in geld', 'Points benefit': 'Voordeel puntensysteem', 'Post-termination payment': 'Betaling na uitdiensttreding',
 'Premium pay (i.e. Shift premium)': 'Premie (bv. ploegenpremie)', 'Profit distribution': 'Winstuitkering', 'Recognition Award': 'Erkenningsbeloning',
 'Recognition Award benefit': 'Voordeel erkenningsbeloning', 'Relocation allowance': 'Verhuisvergoeding', 'Representative allowance': 'Representatievergoeding',
 'Resettlement allowance': 'Herinstallatievergoeding', 'Salary addition': 'Looncomplement', 'Schooling allowance': 'Schoolvergoeding',
 'Seniority gratuity': 'Anciënniteitspremie', 'Sick leave payout': 'Uitbetaling ziekteverlof', 'Sick leave payout 2': 'Uitbetaling ziekteverlof 2',
 'Sick leave payout 3': 'Uitbetaling ziekteverlof 3', 'Sick pay': 'Loon bij ziekte', 'Social raise': 'Sociale verhoging',
 'Social raise (pre-tax deduction)': 'Sociale verhoging (aftrek vóór belasting)',
 'Social raise / Social allowance (Adjustment)': 'Sociale verhoging / sociale vergoeding (correctie)',
 'Social raise / Social allowance (Advance)': 'Sociale verhoging / sociale vergoeding (voorschot)', 'Special allowance': 'Bijzondere vergoeding',
 'Statutory Gratuity, EOS': 'Wettelijke vergoeding einde dienst (EOS)', 'Stock options and grants': 'Aandelenopties en toekenningen',
 'Supplemental basic': 'Aanvullend basisloon', 'Supplemental basic (i.e. 13th or 14th months salary)': 'Aanvullend basisloon (bv. 13de of 14de maand)',
 'Telephone allowance': 'Telefoonvergoeding', 'Tools and work-clothes': 'Gereedschap en werkkledij', 'Training leave payout': 'Uitbetaling opleidingsverlof',
 'Transportation / car expense': 'Vervoers- / autokosten', 'Transportation allowance': 'Vervoersvergoeding', 'Travel expenses': 'Reiskosten',
 'Travel ticket allowance': 'Vergoeding vervoerbewijs', 'Unpaid leave payout': 'Uitbetaling onbetaald verlof',
 'Vacation cashout leave payout': 'Uitbetaling vakantiesaldo', 'Vacation cashout leave payout adjustment': 'Correctie uitbetaling vakantiesaldo',
 'Vacation leave payout': 'Uitbetaling vakantieverlof', 'Year-end bonus provision payment': 'Betaling eindejaarspremie (provisie)',
}
PFX = {'Arrears': 'Achterstallen', 'Adjustment': 'Correctie', 'Advance': 'Voorschot', 'Addition': 'Aanvulling'}

def dutch(name):
    m = re.match(r'^(Arrears|Adjustment|Advance|Addition) - (.*)$', name)
    if m:
        return PFX[m.group(1)] + ' - ' + NL[m.group(2)]
    return NL[name]

# ---------------------------------------------------------------- dados
gwb = openpyxl.load_workbook(GLOBAL, data_only=True)
gws = gwb.worksheets[1]
GL = [(norm(r[1]), norm(r[0]), norm(r[2])) for r in gws.iter_rows(min_row=2, max_col=3, values_only=True) if norm(r[1])]
bwb = openpyxl.load_workbook(BASE, data_only=True)
bws = bwb['Wage Type Catalogue']
BE, ROW = {}, {}
for i, r in enumerate(bws.iter_rows(min_row=2, max_col=20, values_only=True), 2):
    k = norm(r[0])
    if k:
        BE[k] = [norm(c) for c in r]
        ROW[k] = i
new = [(c, n, t) for c, n, t in GL if c[:2] in ('62', '65', '79') and c not in BE]
assert len(new) == 468, len(new)
missing = [c for c, _, _ in new if c not in M]
assert not missing, missing

rows, audit = [], []
for c, gname, gtype in new:
    analog, note = M[c]
    kind = (re.match(r'^(Arrears|Adjustment|Advance|Addition) - ', gname) or [None, ''])[1] if re.match(r'^(Arrears|Adjustment|Advance|Addition) - ', gname) else ''
    if analog.startswith('NA:'):
        E, G, J, flags = 'Earning', 'NA', 'Additional', ['NA'] * 5
        F = f"Global WTC 1.1 code {c} ('{gname}'). Not applicable in Belgium: {analog[3:]}"
        ref = 'NA'
    else:
        a = BE[analog]
        E, G, J, flags = a[4], a[6], a[9], a[13:18]
        F = (f"Global WTC 1.1 code {c} ('{gname}'). Belgian treatment follows {analog} '{a[1]}' "
             f"(this sheet, row {ROW[analog]}), whose explanation carries the legal basis.")
        aname = a[1]
        analog_is_arrears = aname.startswith('Arrears')
        if kind == 'Arrears' and not analog_is_arrears and flags[0] == 'Yes' and G == '250' and flags[1] == 'Yes':
            G, flags = '252', ['Yes', 'No', 'Yes', flags[3], flags[4]]
            F += (" Arrears relating to a previous calendar year: withholding at the exceptional-remuneration rate, "
                  f"as for 62101 (row {ROW['62101']}).")
        elif kind in ('Adjustment', 'Advance', 'Addition') and not aname.startswith(('Adjustment', 'Advance')):
            F += f" {kind} within the current calendar year, following the same treatment."
        if kind:
            J = 'Additional'
        if note:
            F += ' ' + note
        ref = analog
    rows.append([c, gname, dutch(gname), '', E, F, G, '', '', J, '', '', '', *flags, '', ''])
    audit.append([c, gname, gtype, ref, E, G, J, *flags])

with open(os.path.join(HERE, 'mapeamento-v1.1.csv'), 'w', newline='', encoding='utf-8-sig') as f:
    w = csv.writer(f)
    w.writerow(['Codigo', 'Nome Global 1.1', 'Tipo Global', 'Linha BE equivalente', 'Category', 'Tax Code', 'Occurrence',
                'Subject to Tax', 'Table Tax', 'Special Tax', 'Subject to SI', 'Subject to Pension'])
    w.writerows(audit)

# ---------------------------------------------------------------- XML
zin = zipfile.ZipFile(BASE)
parts = {n: zin.read(n) for n in zin.namelist()}

sty = parts['xl/styles.xml'].decode('utf-8')
nf = int(re.search(r'<fills count="(\d+)"', sty).group(1))
sty = re.sub(r'<fills count="\d+">(.*?)</fills>',
             lambda m: f'<fills count="{nf+1}">' + m.group(1) +
             '<fill><patternFill patternType="solid"><fgColor rgb="FFDDEBF7"/><bgColor rgb="FFDDEBF7"/></patternFill></fill></fills>',
             sty, flags=re.S)
xm = re.search(r'<cellXfs count="(\d+)">(.*?)</cellXfs>', sty, re.S)
xfs = re.findall(r'<xf\b[^>]*?(?:/>|>.*?</xf>)', xm.group(2), re.S)
assert len(xfs) == int(xm.group(1))
newid = {}
for s in (61, 22, 25, 32, 69):
    x = xfs[s]
    x = re.sub(r'fillId="\d+"', f'fillId="{nf}"', x)
    x = x.replace('<xf ', '<xf applyFill="1" ', 1) if 'applyFill' not in x else re.sub(r'applyFill="\d"', 'applyFill="1"', x)
    newid[s] = len(xfs)
    xfs.append(x)
sty = sty[:xm.start()] + f'<cellXfs count="{len(xfs)}">' + ''.join(xfs) + '</cellXfs>' + sty[xm.end():]
parts['xl/styles.xml'] = sty.encode('utf-8')

COLS = [chr(65 + i) for i in range(20)]
STY = {'A': 61, 'B': 22, 'C': 22, 'D': 25, 'F': 22, 'T': 69}

def cell(ref, val, s):
    if val == '':
        return f'<c r="{ref}" s="{s}"/>'
    if ref[0] == 'A' and val.isdigit():
        return f'<c r="{ref}" s="{s}"><v>{val}</v></c>'
    return f'<c r="{ref}" s="{s}" t="inlineStr"><is><t xml:space="preserve">{html.escape(val, quote=False)}</t></is></c>'

sh = parts['xl/worksheets/sheet2.xml'].decode('utf-8')
for i, r in enumerate(rows):
    rn = 361 + i
    cells = ''.join(cell(f'{col}{rn}', r[j], newid[STY.get(col, 32)]) for j, col in enumerate(COLS))
    cells += ''.join(f'<c r="{c}{rn}" s="16"/>' for c in ['U', 'V', 'W', 'X', 'Y', 'Z', 'AA', 'AB', 'AC', 'AD', 'AE', 'AF', 'AG', 'AH', 'AI'])
    newrow = f'<row r="{rn}" ht="15.75" customHeight="1">{cells}</row>'
    sh, n = re.subn(rf'<row r="{rn}"[^>]*>.*?</row>', lambda m: newrow, sh, count=1, flags=re.S)
    assert n == 1, rn
parts['xl/worksheets/sheet2.xml'] = sh.encode('utf-8')

# Version Control: linha 14
vc = parts['xl/worksheets/sheet1.xml'].decode('utf-8')
desc = ('Added the Global WTC 1.1 codes missing from the 62, 65 and 79 series (468 rows, catalogue rows 361 to 828, '
        'highlighted in light blue): 62 series 247 (178 five-digit, 69 four-digit), 65 series 148, 79 series 73. '
        'Each row follows the Belgian treatment of the equivalent existing wage type named in its Formula column. '
        'Rows 2 to 360 unchanged.')
def vcell(m):
    ref, s = m.group(1), m.group(2)
    v = {'B14': ('1.1', 'n'), 'C14': ('46316', 'n'), 'D14': (desc, 's'), 'E14': ('Under Review', 's'), 'F14': ('Wallisson Gomes', 's')}[ref]
    if v[1] == 'n':
        return f'<c r="{ref}" s="{s}"><v>{v[0]}</v></c>'
    return f'<c r="{ref}" s="{s}" t="inlineStr"><is><t xml:space="preserve">{html.escape(v[0], quote=False)}</t></is></c>'
vc, n = re.subn(r'<c r="([B-F]14)" s="(\d+)"/>', vcell, vc)
assert n == 5, n
parts['xl/worksheets/sheet1.xml'] = vc.encode('utf-8')

with zipfile.ZipFile(OUT, 'w') as zout:
    for info in zin.infolist():
        zout.writestr(info, parts[info.filename], compress_type=info.compress_type)
print('ok', OUT, len(rows), 'linhas; estilos novos', newid)
