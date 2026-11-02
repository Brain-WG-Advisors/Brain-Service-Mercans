# -*- coding: utf-8 -*-
"""Release cross-check, Colombia finals (issue 2026-10-30). Modelled on the France tool
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
Writes final/RELEASE-CROSSCHECK.md and final/MD5-FINAIS.txt. Exit 1 if any check fails.
Usage: python -I final/scripts/release_crosscheck.py
"""
import os, re, sys, zipfile, hashlib, difflib, html, collections, datetime
HERE = os.path.dirname(os.path.abspath(__file__)); VAL = os.path.normpath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, HERE)
import colib, pairs, release_edits as E
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
    (r'WTC|CCG|DD', r'Version Control!.*|P(2[45]\d|26\d)', r'.*', 'Version Control history of earlier issued versions (unchanged)'),
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
        if n.startswith('word/') and n.endswith('.xml'):
            a = re.sub(rb' w:rsid\w*="[0-9A-Fa-f]{8}"', b'', a); a = re.sub(rb'<w:rsids>.*?</w:rsids>', b'', a, flags=re.S)
        if a != b: fails.append(f'part changed: {n}')
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
    if b'<w:comment ' in zf.read('word/comments.xml'): fails.append('comments left')
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
for art, d, b, f, v in pairs.PAIRS:
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

# SIR text (markdown, to paste in the Google Doc)
sir = os.path.join(FINAL, 'CO-SIR-001-v1.2-texto-final.md')
if os.path.exists(sir):
    lines = open(sir, encoding='utf-8').read().split('\n')
    # only the text to paste (lines between ``` fences) is product text
    paste, inside = [], False
    for i, l in enumerate(lines, 1):
        if l.startswith('```'): inside = not inside; continue
        if inside: paste.append((f'L{i}', l))
    block, ok = lint('SIR', paste)
    allfail += len(block)
    md5lines.append(f'{md5(sir)}  CO-SIR-001-v1.2-texto-final.md')
    rows.append(('SIR', 'CO-SIR-001-v1.2-texto-final.md', '1.2', md5(sir), md5('revisao/SIR/CO-SIR-001-v1.2-DRAFT-COVAL-2026-10-29-REDLINE.md'), {'blocks to paste': len(paste)}, [], block, ok, []))
    print(f'SIR      {"PASS" if not block else "FAIL"}  CO-SIR-001-v1.2-texto-final.md  lines={len(paste)}')
    for x in block[:12]: print('     ', x[:220])

open(os.path.join(FINAL, 'MD5-FINAIS.txt'), 'w', encoding='utf-8').write(
    f'# MD5 dos finais (emissão {ISSUE}); gerado por final/scripts/release_crosscheck.py em {datetime.datetime.now():%Y-%m-%d %H:%M}\n' + '\n'.join(md5lines) + '\n')

L = [f'# Release cross-check, finais da Colômbia (emissão {ISSUE})', '',
     'Ligado a [[CONFERENCIA]] e [[BASELINE]]. Gerado por `final/scripts/release_crosscheck.py` em '
     f'{datetime.datetime.now():%Y-%m-%d %H:%M}. Compara cada final com o DRAFT aprovado (`revisao/`, md5 em `revisao/MD5-DRAFTS.txt`).', '',
     '## O que a ferramenta prova', '',
     '1. **Conteúdo:** a única diferença de texto entre DRAFT e final são as edições declaradas em `final/scripts/release_edits.py` (xlsx: valor e fórmula de todas as células de todas as abas; docx: todos os parágrafos do DRAFT com as alterações controladas aceitas). Cada edição declarada produziu exatamente o texto declarado.',
     '2. **Formatação:** toda célula mantém a formatação do DRAFT, exceto o fundo de destaque `FFDDEBF7`, que nenhuma célula mantém. A estrutura das abas fora das células (colunas, mesclagens, alturas, painéis) e todas as outras partes do zip são idênticas byte a byte.',
     '3. **Marcadores:** lint C29 (placeholder, TODO, TBD, FIXME, XXX, VERIFY No., to be confirmed / verified) e marcadores internos (COVAL, DRAFT, confiança, "Position -", rodada, IDs de achado, ferramentas internas, pipeline, outros países, frases de retrabalho). Ocorrências legítimas aparecem contadas, não escondidas.',
     '4. **Metadados e estrutura:** sem alterações controladas, comentários no docx, rsids, controle de alterações ligado, propriedades personalizadas; criação = modificação = data de emissão, revisão 1, autor.', '',
     '## Resultado', '', '| Artefato | Final | Versão | Edições declaradas conferidas | Outras medidas | Falhas | md5 final | md5 DRAFT |', '|---|---|---|---|---|---|---|---|']
for art, f, v, mf, mdr, info, fails, block, ok, meta in rows:
    other = '; '.join(f'{k} {v_}' for k, v_ in info.items() if k != 'declared edits verified')
    L.append(f'| {art} | `{f}` | {v} | {info.get("declared edits verified", "-")} | {other} | {len(fails) + len(block) + len(meta)} | `{mf[:12]}` | `{mdr[:12]}` |')
L += ['', f'**Veredito: {"PASS" if not allfail else "FAIL"}** ({allfail} falhas).', '', '## Ocorrências legítimas (não são marcador)', '']
for art, f, v, mf, mdr, info, fails, block, ok, meta in rows:
    for why, n in ok.items(): L.append(f'- {art}: {n} × {why}')
L += ['', '## Falhas', '']
for art, f, v, mf, mdr, info, fails, block, ok, meta in rows:
    for x in fails + block + meta: L.append(f'- {art}: {x[:300]}')
if not allfail: L.append('Nenhuma.')
L += ['', '## Fora do escopo desta ferramenta', '',
      '- Comentários do time herdados das versões vigentes no WTC (2 partes) e no DD (3 partes): são do Google Sheets, idênticos aos da v1.6 / v1.3, e foram mantidos (não são marcas da validação).',
      '- O texto jurídico: é conferido pelo Test 0 (revisor independente), não por esta ferramenta.']
open(os.path.join(FINAL, 'RELEASE-CROSSCHECK.md'), 'w', encoding='utf-8').write('\n'.join(L) + '\n')
print('VERDICT', 'PASS' if not allfail else 'FAIL', allfail)
sys.exit(1 if allfail else 0)
