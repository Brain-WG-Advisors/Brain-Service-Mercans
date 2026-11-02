# -*- coding: utf-8 -*-
"""Rodada 5 (2026-11-02): cirurgia no XML para os DRAFT-R5 da Colombia.
xlsx: celula alterada (ou criada) recebe o estilo original clonado com fundo FFDDEBF7; texto em inlineStr; as demais
      partes do zip sao copiadas byte a byte (openpyxl.save nunca e usado).
docx: alteracao controlada (w:del / w:ins, autor e data fixos) no document.xml; paragrafo inteiro apagado com a marca de
      paragrafo apagada; linha nova de tabela com w:trPr/w:ins. python-docx so le (localiza celulas)."""
import re, html, zipfile, os, hashlib

BLUE = 'FFDDEBF7'
AUTHOR = 'Wallisson Gomes'
DATE = '2026-11-02T00:00:00Z'


def esc(t):
    return t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def md5(p):
    return hashlib.md5(open(p, 'rb').read()).hexdigest()


def read_zip(path):
    z = zipfile.ZipFile(path)
    infos = z.infolist(); data = {i.filename: z.read(i.filename) for i in infos}; z.close()
    return infos, data


def write_zip(path, infos, data):
    tmp = path + '.tmp'
    with zipfile.ZipFile(tmp, 'w') as o:
        for i in infos:
            zi = zipfile.ZipInfo(i.filename, i.date_time); zi.compress_type = i.compress_type; zi.external_attr = i.external_attr
            o.writestr(zi, data[i.filename])
    os.replace(tmp, path)


# ------------------------------------------------------------------ xlsx
def sheetmap(data):
    wb = data['xl/workbook.xml'].decode('utf-8'); rel = data['xl/_rels/workbook.xml.rels'].decode('utf-8')
    rid = {}
    for m in re.finditer(r'<Relationship\b[^>]*>', rel):
        t = m.group(0)
        i = re.search(r'Id="([^"]+)"', t).group(1); g = re.search(r'Target="([^"]+)"', t).group(1).lstrip('/')
        rid[i] = g if g.startswith('xl/') else 'xl/' + g
    out = {}
    for m in re.finditer(r'<sheet\b[^>]*>', wb):
        t = m.group(0)
        out[html.unescape(re.search(r'name="([^"]*)"', t).group(1))] = rid[re.search(r'r:id="([^"]+)"', t).group(1)]
    return out


def shared_strings(data):
    if 'xl/sharedStrings.xml' not in data: return []
    x = data['xl/sharedStrings.xml'].decode('utf-8')
    return [html.unescape(''.join(re.findall(r'<t(?: [^>]*)?>(.*?)</t>', si, re.S))) for si in re.findall(r'<si>(.*?)</si>', x, re.S)]


XF_RE = re.compile(r'<xf\b[^>]*?(?:/>|>.*?</xf>)', re.S)


class Styles:
    def __init__(self, data):
        self.data = data
        self.sty = data['xl/styles.xml'].decode('utf-8')
        fm = re.search(r'(<fills count=")(\d+)(">)(.*?)(</fills>)', self.sty, re.S)
        fills = re.findall(r'<fill>.*?</fill>|<fill/>', fm.group(4), re.S)
        b = [i for i, f in enumerate(fills) if BLUE in f and 'patternFill' in f]
        if b:
            self.bid = b[0]
        else:
            nf = '<fill><patternFill patternType="solid"><fgColor rgb="%s"/><bgColor indexed="64"/></patternFill></fill>' % BLUE
            fills.append(nf); self.bid = len(fills) - 1
            self.sty = self.sty[:fm.start()] + fm.group(1) + str(len(fills)) + fm.group(3) + ''.join(fills) + fm.group(5) + self.sty[fm.end():]
        m = re.search(r'<cellXfs count="(\d+)">(.*?)</cellXfs>', self.sty, re.S)
        self.xfs = XF_RE.findall(m.group(2))
        assert len(self.xfs) == int(m.group(1))
        self.n0 = len(self.xfs)

    def blue(self, s):
        x = self.xfs[s]
        if re.search(r'fillId="%d"' % self.bid, x): return s
        head = re.match(r'<xf\b[^>]*?/?>', x).group(0)
        nh = re.sub(r'fillId="\d+"', 'fillId="%d"' % self.bid, head) if 'fillId=' in head else head.replace('<xf ', '<xf fillId="%d" ' % self.bid, 1)
        nh = re.sub(r'applyFill="\d"', 'applyFill="1"', nh) if 'applyFill' in nh else nh.replace('<xf ', '<xf applyFill="1" ', 1)
        nx = nh + x[len(head):]
        if nx in self.xfs: return self.xfs.index(nx)
        self.xfs.append(nx); return len(self.xfs) - 1

    def save(self):
        m = re.search(r'<cellXfs count="(\d+)">(.*?)</cellXfs>', self.sty, re.S)
        self.sty = self.sty[:m.start()] + '<cellXfs count="%d">%s</cellXfs>' % (len(self.xfs), ''.join(self.xfs)) + self.sty[m.end():]
        self.data['xl/styles.xml'] = self.sty.encode('utf-8')


def col2n(c):
    n = 0
    for ch in c: n = n * 26 + ord(ch) - 64
    return n


def cell_value(m, ss):
    attrs, inner = m.group(1), m.group(3) or ''
    t = re.search(r' t="(\w+)"', attrs); t = t.group(1) if t else 'n'
    v = re.search(r'<v>(.*?)</v>', inner, re.S)
    if t == 's': return ss[int(v.group(1))]
    if t == 'inlineStr': return html.unescape(''.join(re.findall(r'<t(?: [^>]*)?>(.*?)</t>', inner, re.S)))
    return html.unescape(v.group(1)) if v else ''


def xlsx_apply(src, dst, edits, log, art):
    """edits: list of (sheet, ref, op, src_id, style_from). op: ('set', text) | ('num', v) | ('sub', [(old, new), ...]) |
    ('cache', v) (formula cell: only the cached value changes; formula kept)."""
    infos, data = read_zip(src)
    sm = sheetmap(data); ss = shared_strings(data); st = Styles(data)
    for sh, ref, op, sid, sfrom in edits:
        part = sm[sh]; x = data[part].decode('utf-8')
        pat = re.compile(r'<c r="%s"(?=[\s>/])([^>]*?)(/>|>(.*?)</c>)' % ref, re.S)
        m = pat.search(x)
        if m:
            cur = cell_value(m, ss); attrs = m.group(1)
            sm_ = re.search(r' s="(\d+)"', attrs); s = int(sm_.group(1)) if sm_ else 0
        else:
            cur = ''; s = None
        if sfrom:
            mf = re.search(r'<c r="%s"(?=[\s>/])([^>]*?)(?:/>|>)' % sfrom, x)
            sf = re.search(r' s="(\d+)"', mf.group(1)) if mf else None
            if s is None or s == 0 or not cur: s = int(sf.group(1)) if sf else 0
        if s is None: s = 0
        ns = st.blue(s)
        kind = op[0]
        if kind == 'set': newtext = op[1]
        elif kind == 'num': newtext = str(op[1])
        elif kind == 'sub':
            newtext = cur
            for old, new in op[1]:
                assert newtext.count(old) == 1, f'{art} {sh}!{ref}: "{old[:70]}" found {newtext.count(old)}x'
                newtext = newtext.replace(old, new)
        elif kind == 'cache':
            assert m and '<f' in (m.group(3) or ''), f'{art} {sh}!{ref}: cache on a non-formula cell'
            newtext = str(op[1])
        if kind == 'num':
            new = f'<c r="{ref}" s="{ns}"><v>{op[1]}</v></c>'
        elif kind == 'cache':
            inner = m.group(3); a2 = re.sub(r' s="\d+"', f' s="{ns}"', m.group(1))
            inner2 = re.sub(r'<v>.*?</v>', '<v>%s</v>' % esc(str(op[1])), inner, flags=re.S)
            new = f'<c r="{ref}"{a2}>{inner2}</c>'
        else:
            sp = ' xml:space="preserve"' if (newtext != newtext.strip() or '  ' in newtext or '\n' in newtext) else ''
            new = f'<c r="{ref}" s="{ns}" t="inlineStr"><is><t{sp}>{esc(newtext)}</t></is></c>'
        if m:
            x = x[:m.start()] + new + x[m.end():]
        else:
            x = insert_cell(x, ref, new)
        data[part] = x.encode('utf-8')
        log.append(dict(art=art, where=f'{sh}!{ref}', before=cur, after=newtext, src=sid))
    st.save()
    write_zip(dst, infos, data)


def insert_cell(x, ref, new):
    col, row = re.match(r'([A-Z]+)(\d+)', ref).groups(); r = int(row)
    rm = re.search(r'<row r="%d"(?=[\s>/])([^>]*?)(/>|>(.*?)</row>)' % r, x, re.S)
    if rm:
        inner = rm.group(3) or ''
        cells = list(re.finditer(r'<c r="([A-Z]+)\d+"[^>]*?(?:/>|>.*?</c>)', inner, re.S))
        pos = len(inner)
        for c in cells:
            if col2n(c.group(1)) > col2n(col): pos = c.start(); break
        inner2 = inner[:pos] + new + inner[pos:]
        attrs = rm.group(1)
        sp = re.search(r' spans="(\d+):(\d+)"', attrs)
        if sp:
            a, b = int(sp.group(1)), int(sp.group(2)); n = col2n(col)
            attrs = attrs.replace(sp.group(0), f' spans="{min(a, n)}:{max(b, n)}"')
        return x[:rm.start()] + f'<row r="{r}"{attrs}>{inner2}</row>' + x[rm.end():]
    rows = list(re.finditer(r'<row r="(\d+)"', x))
    pos = None
    for rr in rows:
        if int(rr.group(1)) > r: pos = rr.start(); break
    if pos is None: pos = x.index('</sheetData>')
    return x[:pos] + f'<row r="{r}">{new}</row>' + x[pos:]


# ------------------------------------------------------------------ docx
class Docx:
    def __init__(self, src):
        import docx as _docx
        self.infos, self.data = read_zip(src)
        self.x = self.data['word/document.xml'].decode('utf-8')
        self.doc = _docx.Document(src)                          # read only: element positions
        body = self.doc.element.body
        W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
        self.allp = list(body.iter(W + 'p'))
        self.pidx = {id(p): i for i, p in enumerate(self.allp)}
        n = len(re.findall(r'<w:p\b(?:(?!<w:p\b).)*?</w:p>', self.x, re.S))
        assert n == len(self.allp), f'paragraph count regex {n} != lxml {len(self.allp)}'
        self.nid = 900000
        assert not re.search(r'w:id="9\d{5}"', self.x)
        self.ops = []                                             # (global paragraph index, kind, payload)

    def _id(self):
        self.nid += 1; return self.nid

    def para_of(self, loc, old=None):
        """loc: 'P661' (python-docx body paragraph) | 'T105R13C2' (cell; the paragraph of that cell containing old)."""
        m = re.fullmatch(r'P(\d+)', loc)
        if m:
            return self.pidx[id(self.doc.paragraphs[int(m.group(1))]._p)]
        t, r, c = map(int, re.fullmatch(r'T(\d+)R(\d+)C(\d+)', loc).groups())
        cell = self.doc.tables[t].rows[r].cells[c]
        ps = [p for p in cell.paragraphs if (old is None or old in p.text)]
        assert len(ps) == 1, f'{loc}: {len(ps)} paragraphs with {old!r}'
        return self.pidx[id(ps[0]._p)]

    def text(self, gi):
        return ''.join(html.unescape(t) for t in re.findall(r'<w:t(?: [^>]*)?>([^<]*)</w:t>', self._paras()[gi].group(0)))

    def _paras(self):
        return list(re.finditer(r'<w:p\b(?:(?!<w:p\b).)*?</w:p>', self.x, re.S))

    # tracked replacement of 'old' by 'new' inside paragraph gi
    def replace(self, gi, old, new):
        pm = self._paras()[gi]; p = pm.group(0)
        runs = list(re.finditer(r'<w:r(?=[\s>])([^>]*)>(.*?)</w:r>', p, re.S))
        atoms = []   # (run_match, rPr, child_xml, text)
        for rm in runs:
            body = rm.group(2)
            rpr = re.match(r'\s*(<w:rPr>.*?</w:rPr>|<w:rPr/>)?', body, re.S).group(1) or ''
            rest = body[body.index(rpr) + len(rpr):] if rpr else body
            kx = re.findall(r'(<w:t(?: [^>]*)?>[^<]*</w:t>|<w:[A-Za-z]+\b[^>]*/>|<w:([A-Za-z]+)\b[^>]*>.*?</w:\2>)', rest, re.S)
            kx = [k[0] for k in kx]
            assert ''.join(kx) == rest.strip() or ''.join(kx) == rest, f'run content not parsed: {rest[:120]}'
            for k in kx:
                tm = re.match(r'<w:t(?: [^>]*)?>([^<]*)</w:t>', k)
                atoms.append((rm, rpr, k, html.unescape(tm.group(1)) if tm else None))
        full = ''.join(a[3] or '' for a in atoms)
        assert full.count(old) == 1, f'P{gi}: "{old[:70]}" found {full.count(old)}x in "{full[:120]}"'
        a = full.index(old); b = a + len(old)
        result = full.replace(old, new)
        # redline only the differing middle (common prefix / suffix kept as plain text)
        pre = 0
        while pre < min(len(old), len(new)) and old[pre] == new[pre]: pre += 1
        suf = 0
        while suf < min(len(old), len(new)) - pre and old[len(old) - 1 - suf] == new[len(new) - 1 - suf]: suf += 1
        a += pre; b -= suf; new = new[pre:len(new) - suf]
        out_by_run = {}
        pos = 0; inserted = False
        for rm, rpr, k, t in atoms:
            pieces = out_by_run.setdefault(rm.start(), [rm, []])[1]
            if t is None:
                inside = a < pos < b
                pieces.append(('del' if inside else 'keep', rpr, k, None))
                continue
            s0, s1 = pos, pos + len(t); pos = s1
            touches = (s0 < b and s1 > a) or (a == b and not inserted and s0 <= a <= s1 and len(t) > 0)
            if not touches:
                pieces.append(('keept', rpr, None, t)); continue
            left = t[:max(a - s0, 0)]; mid = t[max(a - s0, 0):min(b - s0, len(t))] if b > s0 else ''; right = t[max(min(b - s0, len(t)), max(a - s0, 0)):]
            if left: pieces.append(('keept', rpr, None, left))
            if mid: pieces.append(('delt', rpr, None, mid))
            if not inserted and new:
                pieces.append(('ins', rpr, None, new)); inserted = True
            elif not inserted and not new:
                inserted = True
            if right: pieces.append(('keept', rpr, None, right))
        assert inserted or not new, f'P{gi}: insertion point not found'
        np_ = p; shift = 0
        for start in sorted(out_by_run):
            rm, pieces = out_by_run[start]
            if all(k_[0] in ('keep', 'keept') for k_ in pieces): continue   # untouched run: original XML kept
            tag = '<w:r%s>' % rm.group(1)
            xml = ''
            for kind, rpr, k, t in pieces:
                if kind == 'keep': xml += f'{tag}{rpr}{k}</w:r>'
                elif kind == 'keept': xml += f'{tag}{rpr}<w:t xml:space="preserve">{esc(t)}</w:t></w:r>'
                elif kind == 'del': xml += f'<w:del w:id="{self._id()}" w:author="{AUTHOR}" w:date="{DATE}">{tag}{rpr}{k}</w:r></w:del>'
                elif kind == 'delt': xml += f'<w:del w:id="{self._id()}" w:author="{AUTHOR}" w:date="{DATE}">{tag}{rpr}<w:delText xml:space="preserve">{esc(t)}</w:delText></w:r></w:del>'
                elif kind == 'ins': xml += f'<w:ins w:id="{self._id()}" w:author="{AUTHOR}" w:date="{DATE}">{tag}{rpr}<w:t xml:space="preserve">{esc(t)}</w:t></w:r></w:ins>'
            s, e = rm.start() + shift, rm.end() + shift
            np_ = np_[:s] + xml + np_[e:]; shift += len(xml) - (rm.end() - rm.start())
        self.x = self.x[:pm.start()] + np_ + self.x[pm.end():]
        return full, result

    def delete_para(self, gi):
        pm = self._paras()[gi]; p = pm.group(0); full = self.text(gi)
        def wrap(rm):
            r = rm.group(0)
            r = re.sub(r'<w:t((?: [^>]*)?)>', r'<w:delText\1>', r).replace('</w:t>', '</w:delText>')
            return f'<w:del w:id="{self._id()}" w:author="{AUTHOR}" w:date="{DATE}">{r}</w:del>'
        np_ = re.sub(r'<w:r(?=[\s>])[^>]*>.*?</w:r>', wrap, p, flags=re.S)
        mark = f'<w:del w:id="{self._id()}" w:author="{AUTHOR}" w:date="{DATE}"/>'
        if re.search(r'<w:pPr>.*?<w:rPr/>.*?</w:pPr>', np_, re.S):
            np_ = re.sub(r'(<w:pPr>.*?)<w:rPr/>', lambda m: m.group(1) + '<w:rPr>' + mark + '</w:rPr>', np_, count=1, flags=re.S)
        elif re.search(r'<w:pPr>.*?<w:rPr>.*?</w:pPr>', np_, re.S):
            np_ = re.sub(r'(<w:pPr>.*?<w:rPr>)', lambda m: m.group(1) + mark, np_, count=1, flags=re.S)
        elif '<w:pPr>' in np_:
            np_ = np_.replace('</w:pPr>', '<w:rPr>' + mark + '</w:rPr></w:pPr>', 1)
        else:
            np_ = re.sub(r'(<w:p\b[^>]*>)', lambda m: m.group(1) + '<w:pPr><w:rPr>' + mark + '</w:rPr></w:pPr>', np_, count=1)
        self.x = self.x[:pm.start()] + np_ + self.x[pm.end():]
        return full

    def insert_row_after(self, table_idx, row_idx, texts):
        """copia a linha (table_idx, row_idx) e insere depois dela uma linha nova com 'texts' (uma por celula), controlada."""
        tr = self.doc.tables[table_idx].rows[row_idx]._tr
        ps = [self.pidx[id(p)] for p in tr.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p')]
        paras = self._paras()
        a = paras[ps[0]].start(); b = paras[ps[-1]].end()
        s = [m.start() for m in re.finditer(r'<w:tr[ >]', self.x[:a])][-1]
        e = self.x.index('</w:tr>', b) + len('</w:tr>')
        row = self.x[s:e]
        cells = list(re.finditer(r'<w:tc>.*?</w:tc>|<w:tc .*?</w:tc>', row, re.S))
        assert len(cells) == len(texts), (len(cells), len(texts))
        newcells = []
        for cm, t in zip(cells, texts):
            c = cm.group(0)
            pms = list(re.finditer(r'<w:p\b(?:(?!<w:p\b).)*?</w:p>', c, re.S))
            p = pms[0].group(0)
            r1 = re.search(r'<w:r(?=[\s>])[^>]*>(\s*<w:rPr>.*?</w:rPr>)?', p, re.S)
            rpr = r1.group(1) or '' if r1 else ''
            ppr = re.search(r'<w:pPr>.*?</w:pPr>', p, re.S); ppr = ppr.group(0) if ppr else '<w:pPr></w:pPr>'
            mark = f'<w:ins w:id="{self._id()}" w:author="{AUTHOR}" w:date="{DATE}"/>'
            if '<w:rPr/>' in ppr: ppr = ppr.replace('<w:rPr/>', '<w:rPr>' + mark + '</w:rPr>', 1)
            elif '<w:rPr>' in ppr: ppr = ppr.replace('<w:rPr>', '<w:rPr>' + mark, 1)
            else: ppr = ppr.replace('</w:pPr>', '<w:rPr>' + mark + '</w:rPr></w:pPr>', 1)
            popen = re.match(r'<w:p\b[^>]*>', p).group(0)
            np_ = f'{popen}{ppr}<w:ins w:id="{self._id()}" w:author="{AUTHOR}" w:date="{DATE}"><w:r>{rpr.strip()}<w:t xml:space="preserve">{esc(t)}</w:t></w:r></w:ins></w:p>'
            np_ = re.sub(r' w14:paraId="[^"]*"| w14:textId="[^"]*"', '', np_)
            c2 = c[:pms[0].start()] + np_ + c[pms[-1].end():]
            newcells.append(c2)
        head = row[:cells[0].start()]; tail = row[cells[-1].end():]
        mark = f'<w:ins w:id="{self._id()}" w:author="{AUTHOR}" w:date="{DATE}"/>'
        head = re.sub(r' w14:paraId="[^"]*"| w14:textId="[^"]*"', '', head)
        if '<w:trPr>' in head: head = head.replace('<w:trPr>', '<w:trPr>' + mark, 1)
        elif '<w:trPr/>' in head: head = head.replace('<w:trPr/>', '<w:trPr>' + mark + '</w:trPr>', 1)
        else:
            mo = re.match(r'<w:tr\b[^>]*>(\s*<w:tblPrEx>.*?</w:tblPrEx>)?', head, re.S)
            head = head[:mo.end()] + '<w:trPr>' + mark + '</w:trPr>' + head[mo.end():]
        newrow = head + ''.join(newcells) + tail
        self.x = self.x[:e] + newrow + self.x[e:]
        return texts

    def save(self, dst, track=True):
        self.data['word/document.xml'] = self.x.encode('utf-8')
        if track and 'word/settings.xml' in self.data and b'trackRevisions' not in self.data['word/settings.xml']:
            s = self.data['word/settings.xml'].decode('utf-8')
            s = re.sub(r'(<w:settings\b[^>]*>)', r'\1<w:trackRevisions/>', s, count=1)
            self.data['word/settings.xml'] = s.encode('utf-8')
        write_zip(dst, self.infos, self.data)
