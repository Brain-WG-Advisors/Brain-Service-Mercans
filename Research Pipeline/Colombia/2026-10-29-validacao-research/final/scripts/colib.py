# -*- coding: utf-8 -*-
"""Leitura de xlsx/docx direto do XML (sem openpyxl.save), comum ao release e ao cross-check (CO, 2026-10-30)."""
import zipfile, re, html

BLUE = 'FFDDEBF7'


def unesc(t):
    return html.unescape(t)


def sheetmap(z):
    wb = z.read('xl/workbook.xml').decode('utf-8')
    rel = z.read('xl/_rels/workbook.xml.rels').decode('utf-8')
    rid = {}
    for m in re.finditer(r'<Relationship\b[^>]*>', rel):
        t = m.group(0)
        i = re.search(r'Id="([^"]+)"', t).group(1); g = re.search(r'Target="([^"]+)"', t).group(1)
        g = g.lstrip('/')
        if not g.startswith('xl/'): g = 'xl/' + g
        rid[i] = g
    out = []
    for m in re.finditer(r'<sheet\b[^>]*>', wb):
        t = m.group(0)
        nm = html.unescape(re.search(r'name="([^"]*)"', t).group(1))
        r = re.search(r'r:id="([^"]+)"', t).group(1)
        st = re.search(r'state="([^"]+)"', t)
        out.append((nm, rid[r], st.group(1) if st else 'visible'))
    return out


def shared_strings(z):
    if 'xl/sharedStrings.xml' not in z.namelist(): return []
    x = z.read('xl/sharedStrings.xml').decode('utf-8')
    res = []
    for si in re.findall(r'<si>(.*?)</si>', x, re.S):
        res.append(unesc(''.join(re.findall(r'<t(?: [^>]*)?>(.*?)</t>', si, re.S))))
    return res


def blue_xfs(z):
    sty = z.read('xl/styles.xml').decode('utf-8')
    fills = re.findall(r'<fill>.*?</fill>|<fill/>', re.search(r'<fills[^>]*>(.*?)</fills>', sty, re.S).group(1), re.S)
    bids = {i for i, f in enumerate(fills) if BLUE in f}
    xfs = re.findall(r'<xf\b[^>]*?(?:/>|>.*?</xf>)', re.search(r'<cellXfs[^>]*>(.*?)</cellXfs>', sty, re.S).group(1), re.S)
    out = set()
    for i, x in enumerate(xfs):
        m = re.search(r'fillId="(\d+)"', x)
        if m and int(m.group(1)) in bids: out.add(i)
    return out


CELL = re.compile(r'<c r="([A-Z]+\d+)"([^>]*?)(?:/>|>(.*?)</c>)', re.S)


def xlsx_cells(path):
    """yield (sheet, ref, value_text, formula, style_index) for every cell."""
    z = zipfile.ZipFile(path); ss = shared_strings(z)
    for nm, part, state in sheetmap(z):
        x = z.read(part).decode('utf-8')
        for m in CELL.finditer(x):
            ref, attrs, inner = m.group(1), m.group(2), m.group(3) or ''
            t = re.search(r' t="(\w+)"', attrs); t = t.group(1) if t else 'n'
            s = re.search(r' s="(\d+)"', attrs); s = int(s.group(1)) if s else 0
            f = re.search(r'<f[^>]*>(.*?)</f>', inner, re.S); f = unesc(f.group(1)) if f else None
            v = re.search(r'<v>(.*?)</v>', inner, re.S); v = unesc(v.group(1)) if v else None
            if t == 's' and v is not None: v = ss[int(v)]
            elif t == 'inlineStr': v = unesc(''.join(re.findall(r'<t(?: [^>]*)?>(.*?)</t>', inner, re.S)))
            yield nm, ref, v, f, s
    z.close()


def xlsx_comments(path):
    z = zipfile.ZipFile(path); out = []
    for n in z.namelist():
        if re.match(r'xl/comments\d*\.xml$', n) or 'threadedComment' in n:
            x = z.read(n).decode('utf-8')
            for m in re.finditer(r'<comment ref="([A-Z]+\d+)".*?</comment>', x, re.S):
                out.append((n, m.group(1), unesc(''.join(re.findall(r'<t(?: [^>]*)?>(.*?)</t>', m.group(0), re.S)))))
    return out


def docx_paras(path, part='word/document.xml', accept=True):
    """texto de cada parágrafo; accept=True: aceita ins e descarta del."""
    z = zipfile.ZipFile(path); x = z.read(part).decode('utf-8'); z.close()
    if accept:
        # a paragraph whose mark is deleted merges into the next one (here its content is always deleted too)
        x = re.sub(r'<w:p\b(?:(?!<w:p\b).)*?<w:pPr>(?:(?!</w:pPr>).)*?<w:rPr>(?:(?!</w:rPr>).)*?<w:del [^>]*/>(?:(?!<w:p\b).)*?</w:p>', '', x, flags=re.S)
        x = re.sub(r'<w:(?:ins|del) [^>]*/>', '', x)
        x = re.sub(r'<w:del\b[^>]*>.*?</w:del>', '', x, flags=re.S)
        x = re.sub(r'<w:moveFrom\b[^>]*>.*?</w:moveFrom>', '', x, flags=re.S)
    out = []
    for p in re.findall(r'<w:p\b(?:(?!<w:p\b).)*?</w:p>', x, re.S):
        t = ''.join(re.findall(r'<w:t(?: [^>]*)?>([^<]*)</w:t>', p))
        out.append(unesc(t))
    return out
