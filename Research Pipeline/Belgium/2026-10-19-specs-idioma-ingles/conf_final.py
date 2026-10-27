"""Conference: 1.0 x 1.1 final, 9 BE specs."""
import sys, os, glob, re, json, zipfile, hashlib, collections
sys.stdout.reconfigure(encoding='utf-8', errors='replace'); sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from openpyxl import load_workbook
from langdefs import FR, NL, EN
from tparse import parse, PFX
OUT = sys.argv[1]
LANG = {'BE-NSSO-001-Dimona-Spec', 'BE-NSSO-002-DmfA-Spec', 'BE-NSSO-003-DmfAModification-Spec', 'BE-NSSO-004-DRS-Spec', 'BE-FEDRIS-001-WorkAccident-Spec'}
HOM = {'moment', 'minutes', 'date', 'zone', 'si', 'ce', 'au', 'entre', 'ne', 'commission', 'type', 'code', 'de', 'service', 'occupation', 'pension', 'article', 'base', 'note', 'position', 'a', 'on', 'maximum', 'positions', 'pour', 'sur', 'que', 'est', 'date', 'nombre', 'valeur', 'annexe', 'cette', 'il', 'elle'}
FRX = (FR | set("à été être où après avant chaque lorsqu autre autres cas même ainsi peut doivent concerné cadre ayant auprès fixant correspondant relative mesure période travailleurs données numéro invalide présent domaine définition longueur incorrecte erreur séquence cardinalité admis numérique chiffres maximum composé sont dans par avec des les une".split())) - HOM | {'annexe'} - {'annexe'}
NLX = {'het', 'een', 'voor', 'wordt', 'worden', 'niet', 'deze', 'bij', 'door', 'naar', 'ook', 'werkgever', 'werknemer', 'bijdrage', 'jaar', 'maand', 'werknemers', 'bijdragen', 'werkgevers'}

def sig(c):
    g = lambda o, a: getattr(o, a, None); b = c.border
    return (c.value, c.number_format, g(c.font, 'name'), g(c.font, 'sz'), g(c.font, 'b'), g(c.font, 'i'), str(g(c.font.color, 'rgb') if c.font.color else None),
            c.fill.fill_type, str(c.fill.fgColor.rgb), c.alignment.horizontal, c.alignment.vertical, c.alignment.wrap_text,
            tuple(g(getattr(b, s), 'style') for s in ('left', 'right', 'top', 'bottom')))
def local_hdr(h):
    h = (h or '').lower(); return ('(fr' in h or '(nl' in h or 'local' in h) and '(en' not in h
def strip(v):
    v = re.sub(r"\([^()]*\)", "", v); v = re.sub(r"\([^()]*\)", "", v)
    return re.sub(r"[«“\"‘][^»”\"’]*[»”\"’]", "", v)
def frwords(v):
    w = re.findall(r"[a-zàâçéèêëîïôûùüÿœ]+", strip(v).lower())
    return [x for x in w if x in FRX] + [x for x in w if x in NLX]
def quoted(v): return re.findall(r"«[^»]*»|\"[^\"]*\"", v)

summary = {}
for f in sorted(glob.glob(OUT + '/*_v1.1.xlsx')):
    base = os.path.basename(f).replace('_v1.1.xlsx', '')
    src = glob.glob(f'all10/{base}*.xlsx')[0]
    a = load_workbook(src); b = load_workbook(f)
    assert a.sheetnames == b.sheetnames
    core = [s for s in a.sheetnames if s.endswith('Spec')][0]
    bycol = collections.Counter(); other = []; badstyle = []; outscope = []; litbad = []
    for sn in a.sheetnames:
        wa, wb_ = a[sn], b[sn]
        for r in range(1, max(wa.max_row, wb_.max_row) + 1):
            for c in range(1, max(wa.max_column, wb_.max_column) + 1):
                ca, cb = wa.cell(r, c), wb_.cell(r, c); sa, sb = sig(ca), sig(cb)
                if sa == sb: continue
                if sn == 'Version Control' and ca.value is None and r >= 13: bycol['VC'] += 1; continue
                if sa[0] == sb[0]: other.append((sn, cb.coordinate, 'style only')); continue
                if sa[1:7] != sb[1:7] or sa[9:] != sb[9:] or sb[8] != 'FFDDEBF7': badstyle.append((sn, cb.coordinate))
                col = cb.column_letter; before, after = str(sa[0]), str(sb[0])
                if base in LANG and sn == core and col in 'GMJOT': key = col
                elif base in LANG and sn == 'Field Options' and col == 'C' and before.startswith(('CP ', 'Travailleurs statutaires', '[valeur permise')): key = 'CP' if before.startswith('CP ') else 'FO-C'
                elif before.replace('BE-DD-001-v1.4', 'BE-DD-001-v1.0') == after: key = 'v1.4 only'
                else: outscope.append((sn, cb.coordinate)); key = 'OUT'
                bycol[key] += 1
                if 'BE-DD-001-v1.4' in before and key != 'v1.4 only': bycol['(+v1.4 in same cell)'] += 1
                # literal checks
                bn = before.replace('BE-DD-001-v1.4', 'BE-DD-001-v1.0')
                if key == 'T' and before.startswith(PFX):
                    it1, _ = parse(before); codes1 = [(x[1], x[2]) for x in it1]
                    codes2 = re.findall(r'(\d{5}-\d{3}) (B|NP|P)\b', after)
                    if codes1 != codes2: litbad.append((cb.coordinate, 'T codes'))
                aft = after.replace('ACRF anomaly codes, Annexe 30 (FR labels translated):', '')
                if sorted(re.findall(r'\d+', bn)) != sorted(re.findall(r'\d+', aft)): litbad.append((cb.coordinate, 'digits'))
                if key in 'GMO':
                    for q in quoted(bn):
                        inner = q.strip('«»"').strip()
                        if inner and inner not in after: litbad.append((cb.coordinate, 'quote ' + q[:40]))
                if key == 'J':
                    for m in re.findall(r'\b(?:A?N\(\d+\)|AAAA|MM|JJ|CCC|NNN+C*|HH|SSS?|AAAAT)\b', before):
                        if m not in after: litbad.append((cb.coordinate, 'mask ' + m))
    # language sweep, all sheets/cols of 1.1
    resid = []
    for sn in b.sheetnames:
        if sn == 'Sample File': continue
        ws = b[sn]; rows = list(ws.iter_rows(values_only=True)); hr = 0
        for i, rr in enumerate(rows[:6]):
            if sum(1 for v in rr if v) >= 3: hr = i; break
        hdr = {j: str(v) for j, v in enumerate(rows[hr]) if v} if rows else {}
        for i, rr in enumerate(rows, start=1):
            for j, v in enumerate(rr):
                if not isinstance(v, str) or local_hdr(hdr.get(j)): continue
                w = frwords(v)
                if len(w) >= 2 or (len(w) == 1 and len(v) < 25): resid.append((sn, f'{chr(65+j) if j < 26 else "?"}{i}', w[:4], v[:110]))
    v14 = sum(1 for sn in b.sheetnames for rr in b[sn].iter_rows(values_only=True) for v in rr if isinstance(v, str) and 'v1.4' in v)
    z = zipfile.ZipFile(f)
    summary[base] = dict(md5=hashlib.md5(open(f, 'rb').read()).hexdigest(), changed=dict(bycol), other_diffs=other, bad_style=badstyle,
                         out_of_scope=outscope, literal_mismatch=litbad, lang_residual=len(resid), v14=v14, zip=z.testzip())
    print('##', base, summary[base]['md5']); print('  changed', dict(bycol)); print('  other', other[:5], 'badstyle', badstyle[:5], 'outscope', outscope[:5])
    print('  literal mismatches', len(litbad), litbad[:8]); print('  v1.4 left', v14, 'zip', z.testzip())
    print('  language residual', len(resid))
    for x in resid[:40]: print('    ', x)
json.dump(summary, open('conf_final.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1, default=str)
