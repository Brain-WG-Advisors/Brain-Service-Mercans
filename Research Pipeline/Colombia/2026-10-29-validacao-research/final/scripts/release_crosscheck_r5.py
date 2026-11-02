# -*- coding: utf-8 -*-
"""Release cross-check, Colombia finals (issue 2026-11-02: CCG v1.6, WTC v1.8, DD v1.5, five specs v1.2, Payslip v1.3,
SIR v1.3), adapted from release_crosscheck.py (issue 2026-10-30): each final = its DRAFT-R5 (revisao/rodada5/) with the
tracked changes accepted and the highlight removed, plus the declared edits of release_r5_edits.py. Added here: each
workbook opens (openpyxl read-only), zero formula errors, validate_workbook PASS, no highlight left on cells / rows /
columns; the docx opens (python-docx); the CCG footer edit is declared; the two unchanged specs keep the md5 of
2026-10-30. Original description (issue 2026-10-30): Modelled on the France tool
(fr-research-validation/workbook/release_crosscheck.py), extended to prove the release against the approved DRAFTs.

For every final it proves, independently of release.py:
  1. the ONLY content differences from the approved DRAFT are the edits declared in release_edits.py
     (xlsx: every cell value and formula of every sheet; docx: every paragraph of the DRAFT with all tracked changes
     accepted), and each declared edit produced exactly the declared text;
  2. formatting: every cell keeps the DRAFT's formatting except the review highlight fill FFDDEBF7, which no cell keeps;
     the sheet XML outside the cells (columns, merges, row heights, panes) and every other zip part are unchanged
     (only styles.xml, the sheets, docProps and, for the docx, document / settings / comments may differ);
  3. no residual marker: C29 lint (placeholder, TODO, TBD, FIXME, XXX, VERIFY No., to be confirmed / verified) and
     the internal markers of the validation (COVAL, DRAFT, confidence, Position -, Round n, finding IDs, agents,
     pipeline, other countries' projects); known legitimate occurrences are listed, not hidden;
  4. structure / metadata: no tracked changes, comments in the docx, rsids, track-changes switch, custom properties;
     created / modified = issue date, revision 1, author.
Writes final/RELEASE-CROSSCHECK-R5.md and final/MD5-FINAIS.txt (all current finals). Exit 1 if any check fails.
Usage: python -I final/scripts/release_crosscheck_r5.py
"""
import os, re, sys, zipfile, hashlib, difflib, html, collections, datetime
HERE = os.path.dirname(os.path.abspath(__file__)); VAL = os.path.normpath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, HERE)
import colib, release_r5_edits as E
import subprocess
VALIDATOR = r'C:\Users\instituto\.claude\skills\mercans-artifact-toolkit\scripts\validate_workbook.py'
ERR = re.compile(r'^#(REF!|VALUE!|DIV/0!|NAME\?|N/A|NUM!|NULL!)')
sys.stdout.reconfigure(encoding='utf-8')
os.chdir(VAL)
FINAL = 'final'
ISSUE = E.ISSUE

C29 = re.compile(r'\[placeholder\]|\bplaceholder\b|\bTODO\b|\bTBD\b|\bFIXME\b|\bXXX\b|VERIFY No\.|\bto be confirmed\b|\bto be verified\b', re.I)
INTERNAL = collections.OrderedDict([
    ('validation tag', re.compile(r'COVAL|\bDRAFT\b(?!ING)|\bRodada\b|\bRound \d\b|official research of')),
    ('confidence marker', re.compile(r'[Cc]onfidence \d|Position\s*[-–—]\s*confidence|\bprovisional position\b')),
    ('finding id', re.compile(r'\b(?:T4|SIM|NE|DD|PS|A|F|P|S|X)-\d{2}\b|\bD(?:[1-9]|1[0-6])\b(?=[ ,;:)])')),
    ('internal / tooling', re.compile(r'\bClaude\b|\bAnthropic\b|\boracle\b|\bpipeline\b|\bsubagent|\bLLM\b|VERIFY WITH|scope_manifest|04-reports-spec|v2\.\d+ template', re.I)),
    ('other country project', re.compile(r'\bFRVAL\b|\bFR-[A-Z]+-\d{3}|\bBE-[A-Z]+-\d{3}|\bLT-[A-Z]+-\d{3}|\bFrance\b|\bFrench\b|\bBelgi\w*|\bLithuan\w*|\bSpain\b|\bSpanish\b')),
    ('rework wording', re.compile(r'\b(re-?worked|rework|superseded (text|version)|previous version|earlier version|prior version|this version|new version|now reads|was:|\(was |value used earlier|default is unchanged|citation is added|our reading|is ours)\b', re.I)),
])
# legitimate occurrences, matched on (artifact, location regex, matched text regex)
LEGIT = [
    (r'.*', r"Country Codes - ISO 3166-1!B\d+", r'.*', 'ISO country list'),
    (r'.*', r'.*', r'^(Spanish|Spain|France)$', 'country / language named in the legal content (treaty lists, language rule, nationality example)'),
    (r'PAYSLIP', r'.*', r'^Spanish$', 'language rule'),
    (r'CCG', r'P\d+', r'^D[1-3]$', 'deduction labels (D1)-(D3) of the CCG worked example'),
    (r'WTC|CCG|DD', r'Version Control!.*|P(2[4-7]\d)', r'.*', 'Version Control history of earlier issued versions (unchanged)'),
]


def legit(art, loc, hit):
    for a, l, h, why in LEGIT:
        if why and re.fullmatch(a, art) and re.fullmatch(l, loc) and re.search(h, hit):
            return why
    return None


def md5(p):
    return hashlib.md5(open(p, 'rb').read()).hexdigest()


XF_RE = re.compile(r'<xf\b[^>]*?(?:/>|>.*?</xf>)', re.S)


def styles(z):
    sty = z.read('xl/styles.xml').decode('utf-8')
    xfs = XF_RE.findall(re.search(r'<cellXfs[^>]*>(.*?)</cellXfs>', sty, re.S).group(1))
    fills = re.findall(r'<fill>.*?</fill>|<fill/>', re.search(r'<fills[^>]*>(.*?)</fills>', sty, re.S).group(1), re.S)
    def norm(x, keep_fill):
        head = re.match(r'<xf\b[^>]*?/?>', x).group(0)
        a = dict(re.findall(r'(\w+)="([^"]*)"', head)); fid = a.pop('fillId', '0'); a.pop('applyFill', None)
        f = fills[int(fid)] if keep_fill else ''
        return (tuple(sorted(a.items())), x[len(head):], f)
    return xfs, fills, norm


def expected_value(cur, ops):
    if isinstance(ops, tuple) and ops[0] in ('set', 'num'):
        return ops[1]
    if isinstance(ops, tuple) and ops[0] == 'formula':
        return ops[2]
    v = cur
    for op, old, new in ops:
        if v.count(old) != 1: return None
        v = v.replace(old, new)
    return v


def sheet_skeleton(x):
    x = re.sub(r'<c r="[A-Z]+\d+"[^>]*?(?:/>|>.*?</c>)', '', x, flags=re.S)
    x = re.sub(r' s="\d+"| style="\d+"', '', x)
    return x


def check_xlsx(art, d, f):
    fails, info = [], collections.Counter()
    zd, zf = zipfile.ZipFile(d), zipfile.ZipFile(f)
    nd, nf = set(zd.namelist()) - {'docProps/custom.xml'}, set(zf.namelist())
    if nd != nf: fails.append(f'zip parts differ: {sorted(nd ^ nf)}')
    sheets = {p for _, p, _ in colib.sheetmap(zd)}
    for n in sorted(nd & nf):
        if n == 'xl/styles.xml' or n.startswith('docProps/') or n in sheets: continue
        if zd.read(n) != zf.read(n):
            if n in ('[Content_Types].xml', '_rels/.rels') and 'docProps/custom.xml' in zd.namelist():
                a = re.sub(rb'<Override PartName="/docProps/custom\.xml"[^>]*/>|<Relationship [^>]*Target="docProps/custom\.xml"[^>]*/>', b'', zd.read(n))
                if a == zf.read(n): info['custom properties removed'] = 1; continue
            fails.append(f'part changed: {n}')
    for n in sheets:
        if sheet_skeleton(zd.read(n).decode('utf-8')) != sheet_skeleton(zf.read(n).decode('utf-8')):
            fails.append(f'sheet structure outside cells changed: {n}')
    xd, fd, normd = styles(zd); xf_, ff, normf = styles(zf)
    blue_d = {i for i, x in enumerate(xd) if (m := re.search(r'fillId="(\d+)"', x)) and colib.BLUE in fd[int(m.group(1))]}
    blue_f = {i for i, x in enumerate(xf_) if (m := re.search(r'fillId="(\d+)"', x)) and colib.BLUE in ff[int(m.group(1))]}
    D = {(sh, r): (v, fo, s) for sh, r, v, fo, s in colib.xlsx_cells(d)}
    F = {(sh, r): (v, fo, s) for sh, r, v, fo, s in colib.xlsx_cells(f)}
    if set(D) != set(F): fails.append(f'cell set differs: {len(set(D) ^ set(F))}')
    edits = E.XLSX.get(art, {})
    seen = set()
    for k in sorted(set(D) & set(F)):
        (vd, fod, sd), (vf, fof, sf) = D[k], F[k]
        if sf in blue_f: fails.append(f'{k[0]}!{k[1]} still highlighted')
        if normd(xd[sd], False) != normf(xf_[sf], False): fails.append(f'{k[0]}!{k[1]} formatting changed beyond the fill')
        if sd not in blue_d and normd(xd[sd], True) != normf(xf_[sf], True): fails.append(f'{k[0]}!{k[1]} fill changed on a non-highlighted cell')
        if sd in blue_d: info['highlight removed'] += 1
        fe = edits.get(k)
        if isinstance(fe, tuple) and fe[0] == 'formula':
            if fof != fe[1] or not fod: fails.append(f'{k[0]}!{k[1]} declared formula edit mismatch')
            else: info['declared formula edits verified'] += 1
        elif fod != fof: fails.append(f'{k[0]}!{k[1]} formula changed')
        if (vd or '') != (vf or ''):
            if k not in edits: fails.append(f'{k[0]}!{k[1]} UNDECLARED change: {str(vd)[:80]!r} -> {str(vf)[:80]!r}')
            else:
                exp = expected_value(vd or '', edits[k])
                if exp is None or str(exp) != str(vf): fails.append(f'{k[0]}!{k[1]} declared edit mismatch')
                else: seen.add(k)
        elif k in edits and expected_value(vd or '', edits[k]) != (vd or ''):
            fails.append(f'{k[0]}!{k[1]} declared edit not applied')
        elif k in edits: seen.add(k)
    for k in edits:
        if k not in seen: fails.append(f'declared edit missing: {k}')
    info['declared edits verified'] = len(seen)
    # added for the 2026-11-02 issue: opens, no formula error, no highlight on rows / columns, validator
    import openpyxl
    wb = openpyxl.load_workbook(f, read_only=True); info['sheets'] = len(wb.sheetnames)
    for ws in wb.worksheets:
        for _ in ws.iter_rows(max_row=2): pass
    wb.close()
    nerr = sum(1 for (v_, fo_, s_) in F.values() if isinstance(v_, str) and ERR.match(v_))
    for n in sheets:
        x_ = zf.read(n).decode('utf-8')
        nerr += len(re.findall(r'<c [^>]*t="e"', x_))
        for m_ in re.finditer(r'<(?:row|col)\b[^>]*?(?: s| style)="(\d+)"', x_):
            if int(m_.group(1)) in blue_f: fails.append(f'row/column style still highlighted in {n}')
    info['formula errors'] = nerr
    if nerr: fails.append(f'{nerr} formula errors')
    if os.path.exists(VALIDATOR):
        r_ = subprocess.run([sys.executable, '-I', VALIDATOR, f], capture_output=True, text=True, encoding='utf-8', errors='replace')
        tail = (r_.stdout + r_.stderr).strip().splitlines()
        blk = [l for l in tail if re.search(r'blocker', l, re.I)]
        verdict = (blk[-1] if blk else (tail[-1] if tail else '')).strip()
        info['validate_workbook'] = verdict[:80] + f' (exit {r_.returncode})'
        if r_.returncode != 0 or 'PASS' not in verdict: fails.append('validate_workbook: ' + verdict[:120])
    else:
        fails.append('validate_workbook not found')
    return fails, info, F


def accepted_paras(path):
    return colib.docx_paras(path, accept=True)


def check_docx(art, d, f):
    fails, info = [], collections.Counter()
    zd, zf = zipfile.ZipFile(d), zipfile.ZipFile(f)
    if set(zd.namelist()) != set(zf.namelist()): fails.append('zip parts differ')
    for n in zd.namelist():
        if n in ('word/document.xml', 'word/settings.xml', 'word/comments.xml') or n.startswith('docProps/'): continue
        a, b = zd.read(n), zf.read(n)
        if n in E.FOOTER.get(art, {}):
            ta = a.decode('utf-8')
            for old_, new_ in E.FOOTER[art][n]:
                if ta.count(old_) != 1: fails.append(f'declared footer edit not found: {n}')
                ta = ta.replace(old_, new_)
            a = ta.encode('utf-8'); info['declared footer edits verified'] += len(E.FOOTER[art][n])
        if n.startswith('word/') and n.endswith('.xml'):
            a = re.sub(rb' w:rsid\w*="[0-9A-Fa-f]{8}"', b'', a); a = re.sub(rb'<w:rsids>.*?</w:rsids>', b'', a, flags=re.S)
        if a != b: fails.append(f'part changed: {n}')
    import docx as _docx
    _docx.Document(f); info['opens (python-docx)'] = 'yes'
    pd = accepted_paras(d); pf = colib.docx_paras(f, accept=False)
    edits = list(E.DOCX.get(art, []))
    used = collections.Counter()
    sm = difflib.SequenceMatcher(None, pd, pf, autojunk=False)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == 'equal': continue
        if tag == 'replace' and (i2 - i1) == (j2 - j1):
            for a, b in zip(pd[i1:i2], pf[j1:j2]):
                cur, hit = a, []
                for k, e in enumerate(edits):
                    old, new = e[0], e[1]; whole = len(e) > 2   # 'eq' / 'prev2' edits replace a whole paragraph
                    if (cur == old) if whole else (cur.count(old) == 1): cur = cur.replace(old, new); hit.append(k)
                ok = bool(hit) and cur == b
                if ok:
                    for k in hit: used[k] += 1
                if not ok: fails.append(f'UNDECLARED paragraph change: {a[:90]!r} -> {b[:90]!r}')
        else:
            fails.append(f'paragraphs {tag}: draft {i1}-{i2} final {j1}-{j2}: {pd[i1:i2][:2]} / {pf[j1:j2][:2]}')
    for k in range(len(edits)):
        if not used[k]: fails.append(f'declared edit not found: {edits[k][0][:70]!r}')
    info['paragraphs'] = len(pf); info['declared edits verified'] = sum(1 for k in range(len(edits)) if used[k])
    x = zf.read('word/document.xml').decode('utf-8')
    for pat, name in ((r'<w:(?:ins|del) ', 'tracked change'), (r'<w:delText', 'deleted text'), (r'<w:\w+Change\b', 'property change'),
                      (r'w:rsid', 'rsid'), (r'<w:comment(?:RangeStart|RangeEnd|Reference)', 'comment anchor')):
        if re.search(pat, x): fails.append(f'{name} left in document.xml')
    if 'word/comments.xml' in zf.namelist() and b'<w:comment ' in zf.read('word/comments.xml'): fails.append('comments left')
    if b'<w:trackRevisions' in zf.read('word/settings.xml'): fails.append('track changes switched on')
    return fails, info, pf


def metadata(f):
    out = []
    z = zipfile.ZipFile(f); n = z.namelist()
    if 'docProps/custom.xml' in n: out.append('custom properties')
    if 'docProps/core.xml' in n:
        c = z.read('docProps/core.xml').decode('utf-8')
        g = lambda t: (re.search(rf'<{t}[^>]*>([^<]*)<', c) or [None, ''])[1]
        if g('dcterms:created')[:10] not in ('', ISSUE): out.append('created ' + g('dcterms:created'))
        if g('dcterms:modified')[:10] not in ('', ISSUE): out.append('modified ' + g('dcterms:modified'))
        if g('cp:revision') not in ('', '1'): out.append('revision ' + g('cp:revision'))
        for t in ('dc:creator', 'cp:lastModifiedBy'):
            if g(t) and g(t) != E.AUTHOR: out.append(f'{t}={g(t)}')
        if g('dc:description'): out.append('description')
    if 'docProps/app.xml' in n:
        tt = re.search(rb'<TotalTime>(\d+)', z.read('docProps/app.xml'))
        if tt and tt.group(1) != b'0': out.append('TotalTime')
    return out


def lint(art, items):
    block, ok = [], collections.Counter()
    for loc, t in items:
        if not isinstance(t, str): continue
        for m in C29.finditer(t):
            block.append(f'C29 {loc}: …{t[max(0, m.start() - 60):m.end() + 40]}…')
        for k, rx in INTERNAL.items():
            for m in rx.finditer(t):
                why = legit(art, loc, m.group(0))
                if why: ok[why] += 1
                else: block.append(f'{k} {loc}: [{m.group(0)}] …{t[max(0, m.start() - 70):m.end() + 50]}…')
    return block, ok


rows, allfail = [], 0
md5lines = []
for art, d, b, f, v in E.PAIRS:
    fp = os.path.join(FINAL, f)
    if f.endswith('.xlsx'):
        fails, info, cells = check_xlsx(art, d, fp)
        items = [(f'{sh}!{r}', val) for (sh, r), (val, fo, s) in cells.items()]
        items += [(f'{n} {r}', t) for n, r, t in colib.xlsx_comments(fp)]
    else:
        fails, info, paras = check_docx(art, d, fp)
        items = [(f'P{i}', t) for i, t in enumerate(paras)]
        z = zipfile.ZipFile(fp)
        for n in z.namelist():
            if re.match(r'word/(header|footer)\d*\.xml', n):
                items.append((n, ''.join(re.findall(r'<w:t[^>]*>([^<]*)</w:t>', z.read(n).decode('utf-8')))))
    block, ok = lint(art, items)
    meta = metadata(fp)
    nf = len(fails) + len(block) + len(meta); allfail += nf
    md5lines.append(f'{md5(fp)}  {f}')
    rows.append((art, f, v, md5(fp), md5(d), info, fails, block, ok, meta))
    print(f'{art:8} {"PASS" if not nf else "FAIL"}  {f}  edits={info.get("declared edits verified", 0)}  ' + ', '.join(f'{k}={v_}' for k, v_ in info.items() if k != 'declared edits verified'))
    for x in (fails + block + meta)[:12]: print('     ', x[:220])

# SIR text (markdown, to paste in the Google Doc): DRAFT-R5 -> final, only the declared block lines change
import release_r5 as RR  # noqa: E402  (module import only declares the edits; the move step is idempotent and asserts md5)
sd, sb, sf, sv = E.SIR
sir = os.path.join(FINAL, sf)
def _blocks(path):
    out, inside = [], False
    for i, l in enumerate(open(path, encoding='utf-8').read().split('\n'), 1):
        if l.startswith('```'): inside = not inside; continue
        if inside: out.append((f'L{i}', l))
    return out
pb, db = _blocks(sir), _blocks(sd)
sfails = []
if len(pb) != len(db): sfails.append('number of block lines changed')
exp = {(o, n) for o, n in RR.SIR_SUBS if '\n' not in o} | {(l, RR.VH_NEW) for _, l in db if l.startswith(RR.VH_OLD_LINE_START)}
chg = [(a[1], b[1]) for a, b in zip(db, pb) if a[1] != b[1]]
for c in chg:
    if c not in exp: sfails.append(f'UNDECLARED block line change: {c[0][:80]!r}')
txt = open(sir, encoding='utf-8').read()
for bad in ('[R5]', 'DRAFT-R5', 'NÃO emitido'):
    if bad in txt: sfails.append(f'review marker left: {bad}')
block, ok = lint('SIR', pb)
allfail += len(block) + len(sfails)
md5lines.append(f'{md5(sir)}  {sf}')
rows.append(('SIR', sf, sv, md5(sir), md5(sd), {'blocks to paste': len(pb), 'block lines changed (declared)': len(chg)}, sfails, block, ok, []))
print(f'SIR      {"PASS" if not (block or sfails) else "FAIL"}  {sf}  lines={len(pb)} changed={len(chg)}')
for x in (sfails + block)[:12]: print('     ', x[:220])

# the two specs not changed in this issue: same file as issued on 2026-10-30
old_md5 = {}
for ln in open('final/_historico/2026-10-30/MD5-FINAIS.txt', encoding='utf-8'):
    if ln.startswith('#') or not ln.strip(): continue
    h_, f_ = ln.split(None, 1); old_md5[f_.strip()] = h_
for f_ in E.UNCHANGED:
    m_ = md5(os.path.join(FINAL, f_)); ok_ = m_ == old_md5[f_]
    if not ok_: allfail += 1
    md5lines.append(f'{m_}  {f_}')
    rows.append(('=' + os.path.basename(f_)[:14], f_, '1.1', m_, old_md5[f_], {'unchanged (md5 = issue 2026-10-30)': 'yes' if ok_ else 'NO'}, [] if ok_ else ['md5 differs from 2026-10-30'], [], {}, []))
    print(f'{f_}: unchanged {"PASS" if ok_ else "FAIL"}')
# only one version of each final in final/
import glob as _g
stale = [p for p in _g.glob('final/*.docx') + _g.glob('final/*.xlsx') + _g.glob('final/*-texto-final.md') + _g.glob('final/specs/*.xlsx')
         if os.path.relpath(p, 'final').replace('\\', '/') not in {x.split('  ', 1)[1] for x in md5lines}]
if stale: allfail += len(stale); print('STALE finals:', stale)

# ------------------------------------------------------------- cross-references (added 2026-11-02, after the release)
# (a) each final touched by release_xref.py differs from the final as released (copy in _historico/2026-11-02-antes-xref/)
#     only in the declared XREF cells: every other zip part byte for byte, every other cell value / formula / style equal.
# (b) no final cites another artifact at a version other than the one in force (Version Control rows excluded;
#     SIR: only the text that goes to the Doc, i.e. the code blocks, minus its version-history line).
CURRENT = {'CCG': '1.6', 'WTC': '1.8', 'DD': '1.5', 'SIR': '1.3', 'DIAN-001': '1.2', 'DIAN-004': '1.2', 'DIAN-005': '1.2',
           'CESANTIAS-006': '1.2', 'PILA-003': '1.2', 'DIAN-002': '1.1', 'PILA-007': '1.1', 'Payslip': '1.3'}
XRX = [re.compile(r'CO-(CCG|WTC|DD|SIR)-001[ -]v(\d\.\d+)'), re.compile(r'(?<![\w-])(CCG|WTC|DD|SIR) v(\d\.\d+)'),
       re.compile(r'CO-(DIAN-00\d|PILA-00\d|CESANTIAS-006)(?:-\w+)*\s+v(\d\.\d+)'), re.compile(r'(Payslip) Generator v(\d\.\d+)')]
xref_rows, xref_fail = [], []
for art, (f_, m_) in getattr(E, 'XREF_BEFORE', {}).items():
    pre, fin = os.path.join(FINAL, '_historico', '2026-11-02-antes-xref', f_), os.path.join(FINAL, f_)
    if md5(pre) != m_: xref_fail.append(f'{art}: copy of the released final has md5 {md5(pre)}, expected {m_}')
    za, zb = zipfile.ZipFile(pre), zipfile.ZipFile(fin)
    if za.namelist() != zb.namelist(): xref_fail.append(f'{art}: zip parts differ')
    RES_ = getattr(E, 'RESID', {}).get(art, {})   # residual edits applied after the xref update (section below)
    sh_edit = {p_ for nm_, p_, _ in colib.sheetmap(za) if any(k[0] == nm_ for k in list(E.XREF[art]) + list(RES_))}
    for n in za.namelist():
        if n not in sh_edit and za.read(n) != zb.read(n): xref_fail.append(f'{art}: part changed outside the edited sheet: {n}')
    A = {(sh, r): (v, fo, s) for sh, r, v, fo, s in colib.xlsx_cells(pre)}
    B = {(sh, r): (v, fo, s) for sh, r, v, fo, s in colib.xlsx_cells(fin)}
    if set(A) != set(B): xref_fail.append(f'{art}: cell set differs')
    for k in sorted(set(A) & set(B)):
        if k in E.XREF[art]:
            exp_ = expected_value(A[k][0] or '', E.XREF[art][k])
            if B[k][0] != exp_ or B[k][1] != A[k][1] or B[k][2] != A[k][2]: xref_fail.append(f'{art} {k[0]}!{k[1]}: declared edit mismatch')
            else: xref_rows.append((art, f'{k[0]}!{k[1]}', A[k][0], B[k][0]))
        elif k in RES_:
            if B[k][0] != expected_value(A[k][0] or '', RES_[k]) or B[k][1] != A[k][1] or B[k][2] != A[k][2]: xref_fail.append(f'{art} {k[0]}!{k[1]}: residual edit mismatch')
        elif A[k] != B[k]: xref_fail.append(f'{art} {k[0]}!{k[1]}: UNDECLARED change')
    for k in E.XREF[art]:
        if k not in {(a_.split('!')[0], a_.split('!')[1]) for _, a_, _, _ in xref_rows if _ == art}: pass
    if len([r_ for r_ in xref_rows if r_[0] == art]) != len(E.XREF[art]): xref_fail.append(f'{art}: not every declared edit verified')
stale_refs, nrefs = [], collections.Counter()
def _scan(art, loc, t):
    for rx in XRX:
        for m in rx.finditer(t or ''):
            key, ver = m.group(1), m.group(2); nrefs[art] += 1
            if CURRENT.get(key) and CURRENT[key] != ver: stale_refs.append(f'{art} {loc}: "{m.group(0)}" (in force: {key} v{CURRENT[key]})')
for art, d, b, f, v in E.PAIRS + [('=' + os.path.basename(u)[:14], None, None, u, '1.1') for u in E.UNCHANGED]:
    fp = os.path.join(FINAL, f)
    if f.endswith('.xlsx'):
        for sh, r, val, fo, s in colib.xlsx_cells(fp):
            if sh == 'Version Control' or (sh == 'Payslip Spec' and re.fullmatch(r'[A-E](8[0-9]|9[0-9])', r) and art == 'PAYSLIP'): continue
            if isinstance(val, str): _scan(art, f'{sh}!{r}', val)
        for n, r, t in colib.xlsx_comments(fp): _scan(art, f'{n} {r}', t)
    else:
        z = zipfile.ZipFile(fp)
        for n in z.namelist():
            if re.match(r'word/(document|header\d*|footer\d*|footnotes|endnotes)\.xml$', n):
                for i, t in enumerate(colib.docx_paras(fp, part=n, accept=False)): _scan(art, f'{n} P{i}', t)
for loc, t in _blocks(sir):
    if not re.match(r'v\d\.\d+ \| \d{4}-', t): _scan('SIR', loc, t)
xref_fail += [f'stale cross-reference: {x}' for x in stale_refs]
allfail += len(xref_fail)
print('XREF', 'PASS' if not xref_fail else 'FAIL', f'edits verified={len(xref_rows)}', 'version citations scanned=' + ', '.join(f'{k} {v_}' for k, v_ in nrefs.items()))
for x in xref_fail[:20]: print('     ', x[:220])

# ------------------------------------------------------------- residuals (added 2026-11-02, before the Drive upload)
# Each final touched by release_residuos.py differs from its copy taken just before (final/_historico/2026-11-02-antes-residuos/)
# only in the declared edits (RESID / RESID_DOCX): xlsx - every other zip part byte for byte, every other cell value / formula /
# style equal, edited cells keep formula and style; docx - only word/document.xml changes, and in it only the declared
# paragraphs, each declared edit used exactly once.
RPRE = os.path.join(FINAL, '_historico', '2026-11-02-antes-residuos')
RPRE2 = os.path.join(FINAL, '_historico', '2026-11-02-antes-residuos2')
# chain (second batch added 2026-11-02): antes-residuos -> antes-residuos2 (RESID / RESID_DOCX) -> final (RESID2 / RESID2_DOCX);
# a final not touched by the second batch is compared with final/ directly in the first step.
def resid_check(PREDIR, BEFORE, RX, RXD, target):
    res_rows, res_fail = [], []
    for art, (f_, m_) in BEFORE.items():
        pre, fin = os.path.join(PREDIR, f_), target(f_)
        if md5(pre) != m_: res_fail.append(f'{art}: copy has md5 {md5(pre)}, expected {m_}')
        za, zb = zipfile.ZipFile(pre), zipfile.ZipFile(fin)
        if za.namelist() != zb.namelist(): res_fail.append(f'{art}: zip parts differ')
        if f_.endswith('.docx'):
            for n in za.namelist():
                if n != 'word/document.xml' and za.read(n) != zb.read(n): res_fail.append(f'{art}: part changed: {n}')
            pa, pb_ = colib.docx_paras(pre, accept=False), colib.docx_paras(fin, accept=False)
            if len(pa) != len(pb_): res_fail.append(f'{art}: paragraph count differs')
            used_ = collections.Counter()
            for i, (a, b) in enumerate(zip(pa, pb_)):
                if a == b: continue
                hit = None
                for k, e in enumerate(RXD[art]):
                    if len(e) > 2:
                        ok_ = a == e[0] and i >= 2 and pa[i - 2] == e[2]['prev2'] and b == e[1]
                    else:
                        ok_ = a.count(e[0]) == 1 and a.replace(e[0], e[1]) == b
                    if ok_: hit = k; break
                if hit is None: res_fail.append(f'{art} P{i}: UNDECLARED change {a[:80]!r} -> {b[:80]!r}')
                else: used_[hit] += 1; res_rows.append((art, f'P{i}', a, b))
            for k, e in enumerate(RXD[art]):
                if used_[k] != 1: res_fail.append(f'{art}: declared edit used {used_[k]}x: {e[0][:60]!r}')
        else:
            RES_ = RX[art]
            shp = {p_ for nm_, p_, _ in colib.sheetmap(za) if any(k[0] == nm_ for k in RES_)}
            for n in za.namelist():
                if n not in shp and za.read(n) != zb.read(n): res_fail.append(f'{art}: part changed outside the edited sheets: {n}')
            for n in shp:
                if sheet_skeleton(za.read(n).decode('utf-8')) != sheet_skeleton(zb.read(n).decode('utf-8')): res_fail.append(f'{art}: sheet structure outside cells changed: {n}')
            A = {(sh, r): (v, fo, s) for sh, r, v, fo, s in colib.xlsx_cells(pre)}
            B = {(sh, r): (v, fo, s) for sh, r, v, fo, s in colib.xlsx_cells(fin)}
            if set(A) != set(B): res_fail.append(f'{art}: cell set differs')
            for k in sorted(set(A) & set(B)):
                if k in RES_:
                    exp_ = expected_value(A[k][0] or '', RES_[k])
                    if exp_ is None or exp_ == A[k][0] or B[k][0] != exp_ or B[k][1] != A[k][1] or B[k][2] != A[k][2]: res_fail.append(f'{art} {k[0]}!{k[1]}: declared edit mismatch')
                    else: res_rows.append((art, f'{k[0]}!{k[1]}', A[k][0], B[k][0]))
                elif A[k] != B[k]: res_fail.append(f'{art} {k[0]}!{k[1]}: UNDECLARED change')
            if len([r_ for r_ in res_rows if r_[0] == art]) != len(RES_): res_fail.append(f'{art}: not every declared edit verified')
    return res_rows, res_fail
B2 = getattr(E, 'RESID2_BEFORE', {})
_b2files = {f_ for f_, m_ in B2.values()}
res_rows, res_fail = resid_check(RPRE, getattr(E, 'RESID_BEFORE', {}), E.RESID, E.RESID_DOCX,
                                 lambda f_: os.path.join(RPRE2 if f_ in _b2files else FINAL, f_))
res2_rows, res2_fail = resid_check(RPRE2, B2, getattr(E, 'RESID2', {}), getattr(E, 'RESID2_DOCX', {}), lambda f_: os.path.join(FINAL, f_))
allfail += len(res2_fail)
print('RESID2', 'PASS' if not res2_fail else 'FAIL', f'edits verified={len(res2_rows)}')
for x in res2_fail[:20]: print('     ', x[:220])
allfail += len(res_fail)
print('RESID', 'PASS' if not res_fail else 'FAIL', f'edits verified={len(res_rows)}')
for x in res_fail[:20]: print('     ', x[:220])

open(os.path.join(FINAL, 'MD5-FINAIS.txt'), 'w', encoding='utf-8').write(
    f'# MD5 dos finais (emissão {ISSUE}, com as referências cruzadas e os dois lotes de resíduos corrigidos antes da subida ao Drive; CO-DIAN-002 e CO-PILA-007 sem mudança desde 2026-10-30); gerado por final/scripts/release_crosscheck_r5.py em {datetime.datetime.now():%Y-%m-%d %H:%M}\n' + '\n'.join(md5lines) + '\n')

L = [f'# Release cross-check R5, finais da Colômbia (emissão {ISSUE})', '',
     'Ligado a [[CONFERENCIA]], [[CONFERENCIA-R5]] e [[RELEASE-CROSSCHECK]] (emissão anterior). Gerado por `final/scripts/release_crosscheck_r5.py` em '
     f'{datetime.datetime.now():%Y-%m-%d %H:%M}. Compara cada final com o seu DRAFT-R5 (`revisao/rodada5/`, md5 em `revisao/rodada5/MD5-DRAFTS-R5.txt`). '
     'Finais substituídos (30/10) em `final/_historico/2026-10-30/`.', '',
     '## O que a ferramenta prova', '',
     '1. **Conteúdo:** a única diferença de texto entre DRAFT-R5 e final são as edições declaradas em `final/scripts/release_r5_edits.py` (Version Control da versão emitida, com "Released 2026-11-02 — approved by Wallisson Gomes"; versão no cabeçalho e no rodapé do CCG; referências cruzadas de `XREF` e resíduos de `RESID` / `RESID_DOCX`, ver as seções próprias) (xlsx: valor e fórmula de todas as células de todas as abas; docx: todos os parágrafos do DRAFT com as alterações controladas aceitas). Cada edição declarada produziu exatamente o texto declarado.',
     '2. **Formatação:** toda célula mantém a formatação do DRAFT, exceto o fundo de destaque `FFDDEBF7`, que nenhuma célula mantém. A estrutura das abas fora das células (colunas, mesclagens, alturas, painéis) e todas as outras partes do zip são idênticas byte a byte.',
     '3. **Marcadores:** lint C29 (placeholder, TODO, TBD, FIXME, XXX, VERIFY No., to be confirmed / verified) e marcadores internos (COVAL, DRAFT, confiança, "Position -", rodada, IDs de achado, ferramentas internas, pipeline, outros países, frases de retrabalho). Ocorrências legítimas aparecem contadas, não escondidas.',
     '4. **Metadados e estrutura:** sem alterações controladas, comentários no docx, rsids, controle de alterações ligado, propriedades personalizadas; criação = modificação = data de emissão, revisão 1, autor.',
     '5. **Abre e calcula:** cada xlsx abre (openpyxl só leitura) e o docx abre (python-docx); zero erros de fórmula; nenhum estilo de linha/coluna com o azul; `validate_workbook.py` PASS em cada xlsx.',
     '6. **Uma versão de cada final:** `final/` só tem os finais desta emissão e as duas specs inalteradas (md5 igual ao de 30/10).', '',
     '## Resultado', '', '| Artefato | Final | Versão | Edições declaradas conferidas | Outras medidas | Falhas | md5 final | md5 DRAFT |', '|---|---|---|---|---|---|---|---|']
for art, f, v, mf, mdr, info, fails, block, ok, meta in rows:
    other = '; '.join(f'{k} {v_}' for k, v_ in info.items() if k != 'declared edits verified')
    L.append(f'| {art} | `{f}` | {v} | {info.get("declared edits verified", "-")} | {other} | {len(fails) + len(block) + len(meta)} | `{mf[:12]}` | `{mdr[:12]}` |')
L += ['', '## Referências cruzadas', '',
      'Citações de versão de outro artefato que ficaram velhas depois da emissão (CO-PILA-003 e CO-CESANTIAS-006 passaram a v1.2), corrigidas no final emitido por `final/scripts/release_xref.py` (edições declaradas em `XREF` de `release_r5_edits.py`; edição limpa, sem azul nem alteração controlada; linhas de Version Control não tocadas). A ferramenta prova: (a) o final difere da cópia do final emitido às 09:44 (`final/_historico/2026-11-02-antes-xref/`) só nas células declaradas (demais partes do zip byte a byte; demais células com valor, fórmula e estilo iguais); (b) nenhuma citação de versão de outro artefato diverge da vigente em nenhum final (fora Version Control; no SIR, só o texto dos blocos que vai para o Doc, sem a linha do Version history).', '',
      'Vigentes: ' + ', '.join(f'{k} v{v_}' for k, v_ in CURRENT.items()) + '.', '',
      '| Artefato | Célula | Antes | Depois |', '|---|---|---|---|']
for a_, w_, b_, c_ in xref_rows:
    seg = [mm.group(0) for rx in XRX for mm in rx.finditer(b_)]
    segn = [mm.group(0) for rx in XRX for mm in rx.finditer(c_)]
    L.append(f'| {a_} | {w_} | {"; ".join(x for x in seg if x not in segn)} | {"; ".join(x for x in segn if x not in seg)} |')
L += ['', 'Citações de versão conferidas por final: ' + ', '.join(f'{k} {v_}' for k, v_ in nrefs.items()) + f'; divergentes da vigente: {len(stale_refs)}.',
      f'Resultado: {"PASS" if not xref_fail else "FAIL"} ({len(xref_fail)} falhas).']
for x in xref_fail: L.append(f'- {x[:300]}')
L += ['', '## Resíduos corrigidos antes da subida ao Drive (2026-11-02)', '',
      'Resíduos achados depois da emissão, corrigidos no final emitido por `final/scripts/release_residuos.py` (edições declaradas em `RESID` e `RESID_DOCX` de `release_r5_edits.py`; log `final/scripts/release_residuos_log.json`; edição limpa por cirurgia no XML, sem azul nem alteração controlada). Cópia de cada final antes da correção em `final/_historico/2026-11-02-antes-residuos/` (md5 = `MD5-FINAIS.txt` das 10:12).', '',
      '1. **CCG, Módulo 12, Exemplo 4, linha (E):** "within the monthly cap" → teto anual de 790 UVT pelo acumulado (decisão A-1; CE S4 rad. 24047/2021). Varredura do CCG inteiro por "monthly cap/limit", "per month" e "÷ 12" ligados aos tetos de 790/1.340/3.800/2.500 UVT: nenhum outro. Os tetos mensais que ficam são mensais na norma: juros de moradia 100 UVT (DUR 1625 art. 1.2.4.1.27: "sin que exceda de cien Unidades de Valor (100) UVT mensuales"), medicina prepagada 16 UVT e dependentes 32 UVT (ET art. 387; DUR 1625 art. 1.2.4.1.6 nums. 4.2 e 4.3: "dieciséis (16) Unidades de Valor (UVT) mensuales", "treinta y dos (32) Unidades de Valor (UVT) mensuales"). A nota do CCG (Módulo 7) que chamava de "market practice" o rateio mensal dos juros de moradia foi corrigida no segundo lote (abaixo). Capa: 30 → 2 November 2026.',
      '2. **Meios de pagamento:** DD `ID Information`!H7 e CO-DIAN-001 (NIE066 e Population Rules) citam só códigos do mapper Payment Method do DD (linhas 95–104). Em conta: 42, 45, 47, 98. Saíram 46, 30/31, 23/25/26 e ZZZ (fora do mapper); 48/49 só com cartão ligado a conta (Anexo Técnico NE v1.0, NIE064–NIE068 e tabelas 5.3.3.1/5.3.3.2). A linha v1.2 do Version Control da NE passou a citar a regra. H8/H9 não citam códigos (remetem ao H7): sem mudança.',
      '3. **Teto de 2.500 UVT (ET art. 55):** a lei limita "el veinticinco por ciento (25%) del ingreso laboral o tributario anual, limitado a 2.500 UVT" (texto da Ley 2010 de 2019 art. 31), ou seja, um teto anual. Nenhum final divide 2.500 UVT por 12 (WTC: "2,500 UVT per year"); só o design mudou (`58151`).', '',
      'A ferramenta prova: (a) só as partes do zip esperadas mudaram (docx: `word/document.xml`; xlsx: as abas editadas, e nelas nada fora das células); (b) só as células e parágrafos declarados mudaram, com o texto declarado, mantendo fórmula e estilo; (c) cada edição declarada foi usada uma vez. As provas das seções de cima (DRAFT-R5 → final, abre, zero erro de fórmula, `validate_workbook` PASS, marcadores, metadados, versões citadas) foram rodadas de novo sobre os finais corrigidos, com os resíduos declarados.', '',
      '| Artefato | Onde | Antes | Depois |', '|---|---|---|---|']
for a_, w_, b_, c_ in res_rows:
    L.append(f'| {a_} | {w_} | {(b_ or "").replace("|", "/")} | {(c_ or "").replace("|", "/")} |')
L += ['', f'Resultado: {"PASS" if not res_fail else "FAIL"} ({len(res_fail)} falhas; {len(res_rows)} edições conferidas).']
for x in res_fail: L.append(f'- {x[:300]}')
L += ['', '## Resíduos de coerência, segundo lote (2026-11-02)', '',
      'Ajustes de coerência achados depois do primeiro lote de resíduos, corrigidos no final por `final/scripts/release_residuos2.py` (edições declaradas em `RESID2` e `RESID2_DOCX` de `release_r5_edits.py`; log `final/scripts/release_residuos2_log.json`; mesmo método: cirurgia no XML, edição limpa, sem azul nem alteração controlada). Cópia de cada final antes deste lote em `final/_historico/2026-11-02-antes-residuos2/` (md5 = `MD5-FINAIS.txt` das 10:24). A prova do primeiro lote passou a comparar `antes-residuos` com essa cópia (cadeia antes-residuos → antes-residuos2 → final).', '',
      '1. **CCG, Módulo 7, B1 (juros de moradia), linha Limit:** o teto mensal de 100 UVT deixa de ser chamado de "market practice" e passa a regra legal: DUR 1625 de 2016 art. 1.2.4.1.27 ("sin que exceda de cien (100) Unidades de Valor (UVT) mensuales", trecho conferido em `raw/docs/oficiais/CO/2026-10-13-DUR-1625-2016-DIAN.htm`); limite anual de 1.200 UVT do ET art. 119 mantido. Sai a remissão ao relatório de QA.',
      '2. **CCG, linha Payment method:** a lista 42/45/47/10/20/48/49 passa a incluir 98 (CATS: Nequi, Daviplata), como o mapper Payment Method do DD (10, 20, 42, 45, 47, 48, 49, 71, 72, 98); o sentido da frase (meios de pagamento usuais) foi mantido.',
      '3. **CO-DIAN-001, Field Options, bloco Medio de pago (linhas 79–87):** não há linha livre (linha 88 = lista completa; linha 89 = cabeçalho do bloco seguinte, mesclado A89:D89). Inserir linha deslocaria mesclagens, linhas seguintes e as referências por célula das provas; por isso o 98 entrou de forma explícita na célula D88 (código, sigla, nome e regra dos atributos bancários NIE066–NIE068, como nas linhas 79–87), e o cabeçalho A78 deixou de limitar o subconjunto aos códigos 1–97. M72 (valores realistas 42, 45, 10, 20) mantido.', '',
      'A ferramenta prova, como no primeiro lote: só as partes do zip esperadas mudaram; só as células e parágrafos declarados mudaram, com o texto declarado, mantendo fórmula e estilo; cada edição declarada usada uma vez. As provas DRAFT-R5 → final, abre, zero erro de fórmula, `validate_workbook` PASS, marcadores, metadados e versões citadas foram rodadas de novo com este lote declarado.', '',
      '| Artefato | Onde | Antes | Depois |', '|---|---|---|---|']
for a_, w_, b_, c_ in res2_rows:
    L.append(f'| {a_} | {w_} | {(b_ or "").replace("|", "/")} | {(c_ or "").replace("|", "/")} |')
L += ['', f'Resultado: {"PASS" if not res2_fail else "FAIL"} ({len(res2_fail)} falhas; {len(res2_rows)} edições conferidas).']
for x in res2_fail: L.append(f'- {x[:300]}')
L += ['', f'**Veredito: {"PASS" if not allfail else "FAIL"}** ({allfail} falhas).', '', '## Ocorrências legítimas (não são marcador)', '']
for art, f, v, mf, mdr, info, fails, block, ok, meta in rows:
    for why, n in ok.items(): L.append(f'- {art}: {n} × {why}')
L += ['', '## Falhas', '']
for art, f, v, mf, mdr, info, fails, block, ok, meta in rows:
    for x in fails + block + meta: L.append(f'- {art}: {x[:300]}')
if not allfail: L.append('Nenhuma.')
L += ['', '## Fora do escopo desta ferramenta', '',
      '- Comentários do time herdados das versões vigentes no WTC e no DD: são do Google Sheets, idênticos aos dos finais de 30/10, e foram mantidos.',
      '- Os estilos azuis acrescentados nos DRAFT-R5 continuam definidos em `styles.xml`, mas nenhuma célula, linha ou coluna os usa (como no release de 30/10).',
      '- O texto jurídico: é conferido pelo Test 0 (revisor independente), não por esta ferramenta.']
open(os.path.join(FINAL, 'RELEASE-CROSSCHECK-R5.md'), 'w', encoding='utf-8').write('\n'.join(L) + '\n')
print('VERDICT', 'PASS' if not allfail else 'FAIL', allfail)
sys.exit(1 if allfail else 0)
