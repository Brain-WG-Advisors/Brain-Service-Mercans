# -*- coding: utf-8 -*-
"""Release of the Colombia finals (issue 2026-10-30), modelled on the France release (fr-research-validation,
workbook/finalize_release.py and the 2026-10-06/07 'FR finals' commits).

For each approved DRAFT (pairs.py) it writes the final under final/:
  xlsx - XML surgery only (openpyxl.save() is never used): every review highlight fill FFDDEBF7 removed (the cell
         gets back the style of the version in force when that cell existed there with the same formatting, otherwise
         the equivalent non-highlighted style most used in the same column); the declared text edits of
         release_edits.py applied (Version Control row of the issued version, internal markers rewritten in neutral
         product language). Every other zip part is copied byte for byte.
  docx - all tracked changes accepted (w:ins unwrapped, w:del removed, paragraph-mark and row markers, tblGridChange
         removed), then the declared paragraph edits.
  all  - issue metadata (created = modified = issue date, revision 1, author, no custom properties / rsids / TotalTime),
         zip entry times = issue date.
Usage: python -I final/scripts/release.py   (run from anywhere; paths are resolved from this file)
"""
import os, re, sys, zipfile, html, collections, calendar, time
HERE = os.path.dirname(os.path.abspath(__file__))
VAL = os.path.normpath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, HERE)
import colib, pairs, release_edits as RE_
sys.stdout.reconfigure(encoding='utf-8')
OUT = os.path.join(VAL, 'final')
DAY = RE_.ISSUE; STAMP = DAY + 'T09:00:00Z'; AUTHOR = RE_.AUTHOR
EPOCH = calendar.timegm(time.strptime(DAY + ' 09:00:00', '%Y-%m-%d %H:%M:%S'))
LOG = []


def esc(t):
    return t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


# ---------------------------------------------------------------- xlsx
XF_RE = re.compile(r'<xf\b[^>]*?(?:/>|>.*?</xf>)', re.S)


def xf_key(x):
    head = re.match(r'<xf\b[^>]*?/?>', x).group(0)
    attrs = dict(re.findall(r'(\w+)="([^"]*)"', head))
    attrs.pop('fillId', None); attrs.pop('applyFill', None)
    return (tuple(sorted(attrs.items())), x[len(head):])


def unfill(x):
    """same xf with no fill"""
    head = re.match(r'<xf\b[^>]*?/?>', x).group(0)
    nh = re.sub(r'\s*applyFill="[^"]*"', '', head)
    nh = re.sub(r'fillId="\d+"', 'fillId="0"', nh)
    return nh + x[len(head):]


def xlsx_release(art, draft, base, out, edits):
    zd = zipfile.ZipFile(draft); infos = zd.infolist(); data = {i.filename: zd.read(i.filename) for i in infos}; zd.close()
    sty = data['xl/styles.xml'].decode('utf-8')
    m = re.search(r'(<cellXfs count=")(\d+)(">)(.*?)(</cellXfs>)', sty, re.S)
    xfs = XF_RE.findall(m.group(4))
    assert len(xfs) == int(m.group(2)), 'cellXfs count'
    fills = re.findall(r'<fill>.*?</fill>|<fill/>', re.search(r'<fills[^>]*>(.*?)</fills>', sty, re.S).group(1), re.S)
    blue_f = {i for i, f in enumerate(fills) if colib.BLUE in f}
    def is_blue(i):
        mm = re.search(r'fillId="(\d+)"', xfs[i]); return bool(mm) and int(mm.group(1)) in blue_f
    blue = {i for i in range(len(xfs)) if is_blue(i)}
    keys = [xf_key(x) for x in xfs]
    # base styles by cell (same cellXfs prefix was checked in the DRAFT round; re-checked here)
    zb = zipfile.ZipFile(base); bsty = zb.read('xl/styles.xml').decode('utf-8'); zb.close()
    bxfs = XF_RE.findall(re.search(r'<cellXfs[^>]*>(.*?)</cellXfs>', bsty, re.S).group(1))
    prefix_ok = xfs[:len(bxfs)] == bxfs
    bstyle = {(sh, r): s for sh, r, v, f, s in colib.xlsx_cells(base)} if prefix_ok else {}
    smap = {nm: part for nm, part, st in colib.sheetmap(zipfile.ZipFile(draft))}
    # usage statistics of non-blue styles per (sheet, column) and per sheet
    colcount = collections.defaultdict(collections.Counter); shcount = collections.defaultdict(collections.Counter)
    for sh, r, v, f, s in colib.xlsx_cells(draft):
        if s not in blue:
            col = re.match(r'[A-Z]+', r).group(0); colcount[(sh, col)][s] += 1; shcount[sh][s] += 1
    added = {}
    stats = collections.Counter()

    def resolve(sh, ref, s):
        if s not in blue: return s
        bs = bstyle.get((sh, ref)) if ref else None
        if bs is not None and bs < len(xfs) and bs not in blue and keys[bs] == keys[s]:
            stats['base'] += 1; return bs
        cands = [i for i in range(len(xfs)) if i not in blue and keys[i] == keys[s]]
        if cands:
            col = re.match(r'[A-Z]+', ref).group(0) if ref else None
            def score(i):
                return (colcount[(sh, col)][i] if col else 0, shcount[sh][i], 1 if re.search(r'fillId="0"', xfs[i]) else 0, -i)
            stats['equivalent'] += 1
            return max(cands, key=score)
        nx = unfill(xfs[s])
        if nx not in added:
            xfs.append(nx); keys.append(xf_key(nx)); added[nx] = len(xfs) - 1
        stats['new-unfilled'] += 1
        return added[nx]

    # 1) every highlighted cell / row / column style
    for sh, part in smap.items():
        x = data[part].decode('utf-8')
        nc = len(re.findall(r'<c[\s>]', x)); nr = len(re.findall(r'<c r="', x))
        assert nc == nr, f'{art} {sh}: cell without leading r attribute'
        def cell_sub(mm):
            tag = mm.group(0); ref = re.search(r' r="([A-Z]+\d+)"', tag).group(1)
            sm = re.search(r' s="(\d+)"', tag)
            if not sm: return tag
            s = int(sm.group(1)); ns = resolve(sh, ref, s)
            return tag if ns == s else tag.replace(sm.group(0), f' s="{ns}"')
        x = re.sub(r'<c r="[A-Z]+\d+"[^>]*>', cell_sub, x)
        def row_sub(mm):
            tag = mm.group(0); sm = re.search(r' s="(\d+)"', tag)
            if not sm or int(sm.group(1)) not in blue: return tag
            stats['row'] += 1; return tag.replace(sm.group(0), f' s="{resolve(sh, None, int(sm.group(1)))}"')
        x = re.sub(r'<row\b[^>]*>', row_sub, x)
        def col_sub(mm):
            tag = mm.group(0); sm = re.search(r' style="(\d+)"', tag)
            if not sm or int(sm.group(1)) not in blue: return tag
            stats['col'] += 1; return tag.replace(sm.group(0), f' style="{resolve(sh, None, int(sm.group(1)))}"')
        x = re.sub(r'<col\b[^>]*>', col_sub, x)
        data[part] = x.encode('utf-8')
    if added:
        sty = sty[:m.start()] + m.group(1) + str(len(xfs)) + m.group(3) + ''.join(xfs) + m.group(5) + sty[m.end():]
        data['xl/styles.xml'] = sty.encode('utf-8')
    # 2) declared text edits
    ss = colib.shared_strings(zipfile.ZipFile(draft))
    for (sh, ref), ops in edits.items():
        part = smap[sh]; x = data[part].decode('utf-8')
        mm = re.search(r'<c r="%s"(?=[\s>/])([^>]*?)(/>|>(.*?)</c>)' % ref, x, re.S)
        assert mm, f'{art} {sh}!{ref} not found'
        attrs = mm.group(1); inner = mm.group(3) or ''
        t = re.search(r' t="(\w+)"', attrs); t = t.group(1) if t else 'n'
        v = re.search(r'<v>(.*?)</v>', inner, re.S)
        if t == 's': cur = ss[int(v.group(1))]
        elif t == 'inlineStr': cur = html.unescape(''.join(re.findall(r'<t(?: [^>]*)?>(.*?)</t>', inner, re.S)))
        elif t == 'str': cur = html.unescape(v.group(1)) if v else ''
        else: cur = v.group(1) if v else ''
        sattr = re.search(r' s="\d+"', attrs); sattr = sattr.group(0) if sattr else ''
        if isinstance(ops, tuple) and ops[0] == 'num':
            new = f'<c r="{ref}"{sattr}><v>{ops[1]}</v></c>'; newtext = ops[1]
        elif isinstance(ops, tuple) and ops[0] == 'formula':
            fo = re.search(r'<f[^>]*>(.*?)</f>', inner, re.S)
            assert fo and t == 'n', f'{art} {sh}!{ref}: formula edit on a non-formula cell'
            new = f'<c r="{ref}"{sattr}><f>{esc(ops[1])}</f><v>{ops[2]}</v></c>'
            cur = '=' + html.unescape(fo.group(1)); newtext = '=' + ops[1]
        else:
            if isinstance(ops, tuple) and ops[0] == 'set':
                newtext = ops[1]
            else:
                newtext = cur
                for op, old, nw in ops:
                    assert newtext.count(old) == 1, f'{art} {sh}!{ref}: "{old[:60]}" found {newtext.count(old)}x'
                    newtext = newtext.replace(old, nw)
            sp = ' xml:space="preserve"' if (newtext != newtext.strip() or '  ' in newtext or '\n' in newtext) else ''
            new = f'<c r="{ref}"{sattr} t="inlineStr"><is><t{sp}>{esc(newtext)}</t></is></c>'
        x = x[:mm.start()] + new + x[mm.end():]
        data[part] = x.encode('utf-8')
        LOG.append((art, f'{sh}!{ref}', cur, newtext))
    write_zip(out, infos, data)
    return dict(stats), prefix_ok, len(added)


# ---------------------------------------------------------------- docx
def accept_all(x):
    n0 = len(re.findall(r'<w:(?:ins|del) ', x))
    # paragraphs whose mark is deleted: their whole content must be deleted too -> drop the paragraph
    def para(mm):
        p = mm.group(0)
        if re.search(r'<w:pPr>(?:(?!</w:pPr>).)*<w:rPr>(?:(?!</w:rPr>).)*<w:del [^>]*/>', p, re.S):
            rest = re.sub(r'<w:del\b[^>]*[^/]>.*?</w:del>', '', re.sub(r'<w:pPr>.*?</w:pPr>', '', p, flags=re.S), flags=re.S)
            assert not re.findall(r'<w:t(?: [^>]*)?>[^<]+</w:t>', rest), 'deleted paragraph mark with surviving text'
            return ''
        return p
    x = re.sub(r'<w:p\b(?:(?!<w:p\b).)*?</w:p>', para, x, flags=re.S)
    assert not re.search(r'<w:trPr>(?:(?!</w:trPr>).)*<w:del ', x, re.S), 'deleted table row'
    x = re.sub(r'<w:(?:ins|del) [^>]*/>', '', x)                       # paragraph-mark / row markers
    x = re.sub(r'<w:del\b[^>]*>.*?</w:del>', '', x, flags=re.S)         # deleted runs
    x = re.sub(r'<w:moveFrom\b[^>]*>.*?</w:moveFrom>', '', x, flags=re.S)
    x = re.sub(r'</?w:(?:ins|moveTo)\b[^>]*>', '', x)                   # inserted runs kept
    x = re.sub(r'<w:(rPrChange|pPrChange|sectPrChange|tblPrChange|trPrChange|tcPrChange|tblGridChange|numberingChange)\b[^>]*>.*?</w:\1>', '', x, flags=re.S)
    x = re.sub(r'<w:(rPrChange|pPrChange|tblGridChange)\b[^>]*/>', '', x)
    for bad in ('<w:ins ', '<w:del ', '<w:delText', '<w:moveFrom', '<w:moveTo'):
        assert bad not in x, 'residual ' + bad
    assert not re.search(r'<w:\w+Change\b', x), 'residual property change'
    return x, n0


def colib_paras(x):
    return [''.join(html.unescape(t) for t in re.findall(r'<w:t(?: [^>]*)?>([^<]*)</w:t>', p))
            for p in re.findall(r'<w:p\b(?:(?!<w:p\b).)*?</w:p>', x, re.S)]


def para_edit(x, old, new, opt=None):
    """opt: {} = 'old' in exactly one paragraph; {'eq': True, 'n': N} = paragraphs whose whole text is 'old' (N of them,
    edited one per call); {'prev2': T} = the paragraph whose text is 'old' and whose second-previous paragraph is T."""
    opt = opt or {}
    paras = list(re.finditer(r'<w:p\b(?:(?!<w:p\b).)*?</w:p>', x, re.S))
    texts = [''.join(html.unescape(t) for t in re.findall(r'<w:t(?: [^>]*)?>([^<]*)</w:t>', pm.group(0))) for pm in paras]
    hits = []
    for i, pm in enumerate(paras):
        txt = texts[i]
        if opt.get('eq') or 'prev2' in opt:
            if txt != old: continue
            if 'prev2' in opt and (i < 2 or texts[i - 2] != opt['prev2']): continue
        if old in txt:
            hits.append((pm, list(re.finditer(r'(<w:t(?: [^>]*)?>)([^<]*)(</w:t>)', pm.group(0))), txt))
    assert hits and (len(hits) == 1 or opt.get('eq')) and hits[0][2].count(old) == 1, f'docx edit "{old[:60]}": {len(hits)} paragraphs'
    pm, segs, txt = hits[0]
    a = txt.index(old); b = a + len(old)
    pos = 0; newsegs = []
    for s in segs:
        t = html.unescape(s.group(2)); s0, s1 = pos, pos + len(t); pos = s1
        if s1 <= a or s0 >= b or s0 == s1:
            newsegs.append(t); continue
        keep_l = t[:a - s0] if a > s0 else ''
        keep_r = t[b - s0:] if b < s1 else ''
        ins = new if s0 <= a < s1 else ''
        newsegs.append(keep_l + ins + keep_r)
    p = pm.group(0); out = []; last = 0
    for s, nt in zip(segs, newsegs):
        if nt == html.unescape(s.group(2)): continue
        open_ = s.group(1)
        if 'xml:space' not in open_: open_ = open_[:-1] + ' xml:space="preserve">'
        out.append(p[last:s.start()]); out.append(open_ + esc(nt) + s.group(3)); last = s.end()
    out.append(p[last:]); np_ = ''.join(out)
    chk = ''.join(html.unescape(t) for t in re.findall(r'<w:t(?: [^>]*)?>([^<]*)</w:t>', np_))
    assert chk == txt.replace(old, new), 'docx edit mismatch'
    return x[:pm.start()] + np_ + x[pm.end():], txt, chk


def docx_release(art, draft, out, edits):
    zd = zipfile.ZipFile(draft); infos = zd.infolist(); data = {i.filename: zd.read(i.filename) for i in infos}; zd.close()
    x, n0 = accept_all(data['word/document.xml'].decode('utf-8'))
    for e in edits:
        old, new = e[0], e[1]; opt = e[2] if len(e) > 2 else {}
        if opt.get('eq'):
            neq = sum(1 for t in colib_paras(x) if t == old)
            assert neq == opt['n'], f'eq edit "{old}": {neq} paragraphs, expected {opt["n"]}'
        for _ in range(opt.get('n', 1)):
            x, before, after = para_edit(x, old, new, opt)
            LOG.append((art, 'paragraph', before, after))
    data['word/document.xml'] = x.encode('utf-8')
    if 'word/settings.xml' in data:
        data['word/settings.xml'] = re.sub(rb'<w:trackRevisions[^>]*/>', b'', data['word/settings.xml'])
    if 'word/comments.xml' in data:
        # review comments inherited from v1.4 (author 'Claude', a 2026-10-05 redline note) are removed with their anchors
        c = data['word/comments.xml'].decode('utf-8')
        ncom = len(re.findall(r'<w:comment ', c))
        c = re.sub(r'<w:comment [^>]*>.*?</w:comment>', '', c, flags=re.S)
        data['word/comments.xml'] = c.encode('utf-8')
        d = data['word/document.xml'].decode('utf-8')
        d = re.sub(r'<w:commentRange(?:Start|End) [^>]*/>', '', d)
        d = re.sub(r'<w:r [^>]*>(?:(?!</w:r>).)*?<w:commentReference [^>]*/>(?:(?!</w:r>).)*?</w:r>|<w:r><w:commentReference [^>]*/></w:r>', '', d, flags=re.S)
        assert not re.search(r'<w:comment', d), 'comment anchor left'
        data['word/document.xml'] = d.encode('utf-8')
        LOG.append((art, 'comments', f'{ncom} comment(s)', 'removed'))
    write_zip(out, infos, data)
    return n0


# ---------------------------------------------------------------- metadata (France finalize_release.py)
def core(x):
    x = re.sub(r'(<dcterms:created[^>]*>)[^<]*(</dcterms:created>)', rf'\g<1>{STAMP}\2', x)
    x = re.sub(r'(<dcterms:modified[^>]*>)[^<]*(</dcterms:modified>)', rf'\g<1>{STAMP}\2', x)
    x = re.sub(r'<cp:revision>[^<]*</cp:revision>', '<cp:revision>1</cp:revision>', x)
    x = re.sub(r'(<dc:creator(?: [^>]*)?>)[^<]*(</dc:creator>)', rf'\g<1>{AUTHOR}\2', x)
    x = re.sub(r'<dc:creator/>', f'<dc:creator>{AUTHOR}</dc:creator>', x)
    if '<cp:lastModifiedBy' in x:
        x = re.sub(r'<cp:lastModifiedBy>[^<]*</cp:lastModifiedBy>|<cp:lastModifiedBy/>', f'<cp:lastModifiedBy>{AUTHOR}</cp:lastModifiedBy>', x)
    x = re.sub(r'<dc:description>[^<]*</dc:description>|<dc:description/>', '', x)
    x = re.sub(r'<cp:lastPrinted>[^<]*</cp:lastPrinted>', '', x)
    return x


def write_zip(path, infos, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    drop = {'docProps/custom.xml'}
    tmp = path + '.tmp'
    with zipfile.ZipFile(tmp, 'w') as o:
        for i in infos:
            n = i.filename
            if n in drop: continue
            d = data[n]
            if n == 'docProps/core.xml': d = core(d.decode('utf-8')).encode('utf-8')
            elif n == 'docProps/app.xml': d = re.sub(rb'<TotalTime>\d+</TotalTime>', b'<TotalTime>0</TotalTime>', d)
            elif n == '[Content_Types].xml': d = re.sub(rb'<Override PartName="/docProps/custom\.xml"[^>]*/>', b'', d)
            elif n == '_rels/.rels': d = re.sub(rb'<Relationship [^>]*Target="docProps/custom\.xml"[^>]*/>', b'', d)
            elif n.startswith('word/') and n.endswith('.xml'):
                d = re.sub(rb' w:rsid\w*="[0-9A-Fa-f]{8}"', b'', d)
                d = re.sub(rb'<w:rsids>.*?</w:rsids>', b'', d, flags=re.S)
            zi = zipfile.ZipInfo(n, date_time=time.gmtime(EPOCH)[:6]); zi.compress_type = i.compress_type; zi.external_attr = i.external_attr
            o.writestr(zi, d)
    os.replace(tmp, path)
    os.utime(path, (EPOCH, EPOCH))


if __name__ == '__main__':
    os.chdir(VAL)
    for art, d, b, f, v in pairs.PAIRS:
        out = os.path.join(OUT, f)
        if d.endswith('.docx'):
            n0 = docx_release(art, d, out, RE_.DOCX.get(art, []))
            print(f'{art:8} {f}: {n0} tracked changes accepted, {len(RE_.DOCX.get(art, []))} paragraph edits')
        else:
            st, pok, nadd = xlsx_release(art, d, b, out, RE_.XLSX.get(art, {}))
            print(f'{art:8} {f}: highlight removed {st} (base styles usable: {pok}; new xf {nadd}); {len(RE_.XLSX.get(art, {}))} cell edits')
    import json
    json.dump([dict(artifact=a, where=w, before=bf, after=af) for a, w, bf, af in LOG],
              open(os.path.join(OUT, 'scripts', 'release_log.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('edits logged', len(LOG))
