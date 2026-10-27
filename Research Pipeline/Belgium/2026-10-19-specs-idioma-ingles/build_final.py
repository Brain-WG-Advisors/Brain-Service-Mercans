"""BE Report Specs v1.1 final, rebuilt from the 1.0 exports by XML surgery.
Scope: G, M, J, O, T (5 NSSO/FEDRIS specs), Field Options C "CP ..." names, and
BE-DD-001-v1.4 -> BE-DD-001-v1.0 in every cell of the 9 specs. Changed cells in FFDDEBF7.
"""
import zipfile, re, json, sys, os, html, glob
from xml.sax.saxutils import escape
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tdict import L, TAIL, NEWPFX
from jdict import J, CP
from yfix import fix
from tparse import parse, PFX

SRC = 'all10'; OUT = sys.argv[1]; os.makedirs(OUT, exist_ok=True)
BLUE = 'FFDDEBF7'
# G/M translations (step 1)
targets = json.load(open('targets.json', encoding='utf-8'))
TR = {}
for i in range(1, 5):
    s = json.load(open(f'batch{i}.json', encoding='utf-8')); e = json.load(open(f'batch{i}_en.json', encoding='utf-8'))
    for k in s: TR[s[k]] = e[k]
GM = {(t['file'].replace('.xlsx', ''), t['cell']): t['prefix'] + fix(t['body'], TR[t['body']]) for t in targets}
# O translations
OTR = {}
for i in range(1, 4):
    p = f'obatch{i}_en.json'
    if os.path.exists(p):
        s = json.load(open(f'obatch{i}.json', encoding='utf-8')); e = json.load(open(p, encoding='utf-8'))
        for k in s: OTR[s[k]] = e[k]

def t_rebuild(v):
    items, rest = parse(v)
    out = NEWPFX + ' ' + '; '.join(f'{L[l]} {c} {s}' for l, c, s in items)
    if rest: out += ('; ' if items else ' ') + TAIL[rest]
    if not items and not rest: out = NEWPFX + ' Anomaly label | Anomaly code | Severity'
    return out

CURAT_O = "0=période pendant laquelle elle n'est pas sous la curatelle 1=période pendant laquelle elle est sous curatelle"
LANG = {'BE-NSSO-001-Dimona-Spec', 'BE-NSSO-002-DmfA-Spec', 'BE-NSSO-003-DmfAModification-Spec',
        'BE-NSSO-004-DRS-Spec', 'BE-FEDRIS-001-WorkAccident-Spec'}

def shared(z):
    x = z.read('xl/sharedStrings.xml').decode('utf-8'); out = []
    for si in re.findall(r'<si>(.*?)</si>', x, re.S):
        out.append(html.unescape(''.join(re.findall(r'<t[^>]*>(.*?)</t>', si, re.S))))
    return out

def cell_text(cxml, sst):
    t = re.search(r'\bt="(\w+)"', cxml.split('>')[0]); t = t.group(1) if t else None
    if t == 's': return sst[int(re.search(r'<v>(\d+)</v>', cxml).group(1))]
    if t == 'inlineStr': return html.unescape(''.join(re.findall(r'<t[^>]*>(.*?)</t>', cxml, re.S)))
    if t == 'str': return html.unescape(re.search(r'<v>(.*?)</v>', cxml, re.S).group(1))
    return None

def new_value(base, sheet, core, ref, v):
    col = re.match(r'[A-Z]+', ref).group(0); n = v
    if base in LANG and sheet == core:
        if col in 'GM' and (base, ref) in GM: n = GM[(base, ref)]
        elif col == 'J' and v in J: n = J[v]
        elif col == 'O' and v in OTR:
            n = fix(v, OTR[v])
            if v == CURAT_O: n = 'Period not under bankruptcy administration'.join(['0=', ' 1=Period under bankruptcy administration (sous curatelle)'])
            n = n.replace('(= working time (prestation))', '(= service performed (prestation))')
        elif col == 'T' and v.startswith(PFX): n = t_rebuild(v)
    if base in LANG and sheet == 'Field Options' and col == 'C':
        if v in CP: n = CP[v]
        elif v == 'Travailleurs statutaires — Statutory workers.': n = 'Statutory workers (Travailleurs statutaires).'
        elif v.startswith('[valeur permise, description non trouvee]'): n = v.replace('[valeur permise, description non trouvee]', '[permitted value, description not found]', 1)
    if 'BE-DD-001-v1.4' in n: n = n.replace('BE-DD-001-v1.4', 'BE-DD-001-v1.0')
    return n

def vc_text(base, cols):
    if base not in LANG:
        return 'DD citation corrected to BE-DD-001-v1.0, the current Data Dictionary version (it cited a version that does not exist).'
    parts = []
    names = {'G': 'Conditional Reason (G)', 'M': 'Field Explanation (M)', 'J': 'Format (J; masks kept literal)',
             'O': 'Option Values (O; codes and XML values kept literal)', 'T': 'Query to RA (T; ACRF anomaly labels translated, codes and severity unchanged)'}
    for c in 'MGJOT':
        if c in cols: parts.append(names[c])
    s = 'Translated to English, per Suman Rai\'s request: ' + ', '.join(parts)
    if 'CP' in cols: s += ', Field Options joint committee names (official FR name in brackets)'
    s += '. DD citation corrected to BE-DD-001-v1.0, the current Data Dictionary version.'
    return s

report = {}; changes_all = []
for f in sorted(glob.glob(SRC + '/*.xlsx')):
    name = os.path.basename(f); base = re.sub(r' \(\d+\)', '', name).replace('.xlsx', '')
    z = zipfile.ZipFile(f); sst = shared(z)
    wbx = z.read('xl/workbook.xml').decode(); rels = z.read('xl/_rels/workbook.xml.rels').decode()
    rid = {m[0]: m[1] for m in re.findall(r'<sheet [^>]*name="([^"]+)"[^>]*r:id="(rId\d+)"', wbx)}
    tgt = {}
    for rel in re.findall(r'<Relationship [^>]*/>', rels):
        tgt[re.search(r'Id="(rId\d+)"', rel).group(1)] = re.search(r'Target="([^"]+)"', rel).group(1)
    core = [n for n in rid if n.endswith('Spec')][0]
    sty = z.read('xl/styles.xml').decode()
    fm = re.search(r'<fills count="(\d+)">(.*?)</fills>', sty, re.S); nf = int(fm.group(1))
    sty = sty.replace(fm.group(0), f'<fills count="{nf+1}">{fm.group(2)}<fill><patternFill patternType="solid"><fgColor rgb="{BLUE}"/><bgColor rgb="{BLUE}"/></patternFill></fill></fills>')
    xm = re.search(r'<cellXfs count="(\d+)">(.*?)</cellXfs>', sty, re.S)
    xfs = re.findall(r'<xf\b[^>]*?(?:/>|>.*?</xf>)', xm.group(2), re.S); assert len(xfs) == int(xm.group(1))
    clones = {}; newx = []
    def blue(s):
        s = int(s)
        if s not in clones:
            x = xfs[s]
            x = re.sub(r'fillId="\d+"', f'fillId="{nf}"', x) if 'fillId=' in x else x.replace('<xf ', f'<xf fillId="{nf}" ', 1)
            x = x.replace('applyFill="0"', 'applyFill="1"') if 'applyFill=' in x else x.replace('<xf ', '<xf applyFill="1" ', 1)
            clones[s] = len(xfs) + len(newx); newx.append(x)
        return clones[s]
    def tcell(ref, s, text):
        return f'<c r="{ref}" s="{s}" t="inlineStr"><is><t xml:space="preserve">{escape(text)}</t></is></c>'
    new_parts = {}; cols = set(); CNT = {'n': 0}
    for sn, r in rid.items():
        path = 'xl/' + tgt[r]; x = z.read(path).decode('utf-8'); FLAG = {'c': False}
        def sub(m):
            cx = m.group(0); ref = m.group(1)
            v = cell_text(cx, sst)
            if not isinstance(v, str): return cx
            n = new_value(base, sn, core, ref, v)
            if n == v: return cx
            s = re.search(r'\bs="(\d+)"', cx.split('>')[0]); s = s.group(1) if s else '0'
            FLAG['c'] = True; CNT['n'] += 1
            col = re.match(r'[A-Z]+', ref).group(0)
            if sn == core and col in 'GMJOT' and base in LANG and n.replace('BE-DD-001-v1.0', '') != v.replace('BE-DD-001-v1.4', ''): cols.add(col)
            if sn == 'Field Options' and col == 'C' and v in CP: cols.add('CP')
            changes_all.append(dict(spec=base, sheet=sn, cell=ref, before=v, after=n))
            return tcell(ref, blue(s), n)
        x = re.sub(r'<c r="([A-Z]+\d+)"(?:\s[^>]*?)?(?:/>|>(?:(?!<c ).)*?</c>)', sub, x, flags=re.S)
        if sn == 'Version Control':
            rows = re.findall(r'<row r="(\d+)"[^>]*>(.*?)</row>', x, re.S)
            last = max(int(rr) for rr, cc in rows if re.search(rf'<c r="B{rr}"', cc) and int(rr) > 12)
            lastrow = dict(rows)[str(last)]; st = dict(re.findall(r'<c r="([B-F])\d+" s="(\d+)"', lastrow)); nr = last + 1
            pending_vc = (path, x, nr, st, last, lastrow)
            new_parts[path] = x
        elif FLAG['c']:
            new_parts[path] = x
    path, x, nr, st, last, lastrow = pending_vc
    text = vc_text(base, cols)
    if f'<c r="C{last}" s="{st["C"]}" t="s">' in lastrow:
        datec = tcell(f'C{nr}', blue(st['C']), '2026-10-19')
    else:
        datec = f'<c r="C{nr}" s="{blue(st["C"])}"><v>46314</v></c>'
    cells = tcell(f'B{nr}', blue(st['B']), '1.1') + datec + tcell(f'D{nr}', blue(st['D']), text) + tcell(f'E{nr}', blue(st['E']), 'Draft') + tcell(f'F{nr}', blue(st['F']), 'Wallisson Gomes')
    em = re.search(rf'<row r="{nr}"([^>]*?)(/>|>(.*?)</row>)', x, re.S); assert em and not (em.group(3) or '').strip()
    new_parts[path] = x.replace(em.group(0), f'<row r="{nr}"{em.group(1)}>{cells}</row>', 1)
    sty = sty.replace(xm.group(0), f'<cellXfs count="{len(xfs)+len(newx)}">{xm.group(2)}{"".join(newx)}</cellXfs>')
    new_parts['xl/styles.xml'] = sty
    outname = base + '_v1.1.xlsx'; zo = zipfile.ZipFile(os.path.join(OUT, outname), 'w')
    for it in z.infolist():
        data = new_parts[it.filename].encode('utf-8') if it.filename in new_parts else z.read(it.filename)
        zo.writestr(it, data, compress_type=it.compress_type)
    zo.close(); report[outname] = dict(changed=CNT['n'], cols=sorted(cols), vc=text)
json.dump(changes_all, open('changes_final.json', 'w', encoding='utf-8'), ensure_ascii=False)
print(json.dumps(report, indent=1, ensure_ascii=False))
