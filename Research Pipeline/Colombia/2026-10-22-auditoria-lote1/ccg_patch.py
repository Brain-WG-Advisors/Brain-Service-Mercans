"""CCG v1.3 -> v1.4 by XML surgery (no python-docx save). Usage: python ccg_patch.py <src.docx> <dst.docx>"""
import zipfile, re, sys, html
sys.stdout.reconfigure(encoding='utf-8')
src, dst = sys.argv[1], sys.argv[2]
z = zipfile.ZipFile(src); data = {n: z.read(n) for n in z.namelist()}
def esc(s): return html.escape(s, quote=False)
d = data['word/document.xml'].decode('utf8')
VAC_OLD = 'Contributions continue; vacation pay is in the base'
VAC_NEW = ('Vacation: health and pension continue on the IBC of the month before the vacation (Decree 780 of 2016 art. 3.2.5.1); '
           'no occupational-risk contribution during the vacation (Decree 1072 of 2015 art. 2.2.4.2.1.6 num. 1.3); the vacation pay is in the '
           'CCF / SENA / ICBF base (Law 21 of 1982 art. 17; Law 89 of 1988 art. 1 par. 1). Paid leave: contributions continue on the base')
IGE_OLD = 'Contributions continue on the base'
IGE_NEW = open(__file__.replace('ccg_patch.py','ige.txt'), encoding='utf-8').read().strip()
assert d.count(VAC_OLD) == 1; d = d.replace(VAC_OLD, esc(VAC_NEW), 1)
# IGE: the first of the two 'Contributions continue on the base' cells is the IGE row (the second is LMA)
i_ige = d.find('>IGE<'); i_lma = d.find('>LMA<'); i_occ = d.find(IGE_OLD)
assert 0 < i_ige < i_occ < i_lma, (i_ige, i_occ, i_lma)
d = d[:i_occ] + esc(IGE_NEW) + d[i_occ + len(IGE_OLD):]
# version strings
for o, n in (('Version 1.3', 'Version 1.4'), ('CO-CCG-001 v1.3', 'CO-CCG-001 v1.4')):
    c = d.count(o); assert c >= 1, o; d = d.replace(o, n)
# version-control row 1.4 after the 1.3 row
trs = [m for m in re.finditer(r'<w:tr[ >].*?</w:tr>', d, re.S) if '>1.3<' in m.group(0)]
assert len(trs) == 1
tr = trs[0].group(0); texts = re.findall(r'(<w:t[^>]*>)([^<]*)(</w:t>)', tr)
new_vals = ['1.4', '22 October 2026', 'Wallisson Gomes',
            'PILA change events (Module 5 table): vacation - health and pension on the prior-month IBC, no occupational-risk contribution, '
            'vacation pay in the CCF / SENA / ICBF base; general-illness incapacity - the incapacity value as the IBC, no occupational-risk contribution.']
assert [t[1] for t in texts][:3] == ['1.3', '21 October 2026', 'Wallisson Gomes'], [t[1] for t in texts]
newtr = tr; k = 0
def rep(m):
    global k
    v = esc(new_vals[k]) if k < len(new_vals) else ''
    k += 1
    return m.group(1).replace('<w:t>', '<w:t xml:space="preserve">') + v + m.group(3)
newtr = re.sub(r'(<w:t[^>]*>)([^<]*)(</w:t>)', rep, newtr)
d = d.replace(tr, tr + newtr, 1)
data['word/document.xml'] = d.encode('utf8')
for n in list(data):
    if re.match(r'word/footer\d*\.xml|word/header\d*\.xml', n):
        t = data[n].decode('utf8'); data[n] = t.replace('CO-CCG-001 v1.3', 'CO-CCG-001 v1.4').encode('utf8')
with zipfile.ZipFile(dst, 'w', zipfile.ZIP_DEFLATED) as out:
    for info in z.infolist(): out.writestr(info, data[info.filename])
print('ok: VAC, IGE, version strings, VC row 1.4')
