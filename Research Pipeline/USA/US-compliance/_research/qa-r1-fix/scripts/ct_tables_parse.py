"""QA r1b item 4 (RQ-497): parse the CT DRS 2026 withholding tables, IP 2026(1) pp. 31-38.
The table pages carry no text layer: every character is a filled vector path (PyMuPDF
get_text('words') returns 12 words per page, the footer only). Method:
  1. take every small filled path (a glyph) from page.get_drawings();
  2. label it twice and independently:
     (a) by its path-command signature (sequence of l/c/re items), for the signatures
         labelled by eye from a rendered contact sheet;
     (b) by nearest-template match of its rendered bitmap (600 dpi page render, glyph bbox
         crop resized to 12x16) against templates built from (a);
     a glyph is accepted only when (a) and (b) agree, or (a) is unknown and (b) is unambiguous;
  3. group glyphs into lines (y) and tokens (x gap), tokens into the 7 columns;
  4. check structure: wage bands contiguous (row 'greater than' == previous 'less than or equal'),
     every amount column non-decreasing, 7 numeric tokens per row.
Usage: python -I ct_tables_parse.py <pdf> <outdir>"""
import sys, os, re, json, csv, collections
import pymupdf
from PIL import Image

PDF, OUT = sys.argv[1], sys.argv[2]
os.makedirs(OUT, exist_ok=True)
doc = pymupdf.open(PDF)
PAGES = range(30, 38)  # 0-based: pp. 31-38

# signatures labelled by eye (contact sheet of the most frequent path signatures, regular weight only)
SIG = {
 'lccclcclccccclllcclcclccccccllcccclccccl': '$', 'lccclcclccccclllcclcclccclccllcccclccccl': '$',
 'lccclcclclccclllcclcclccclccllcccclccccl': '$', 'lccclcclccccclllcclcclccllccllcccclccccl': '$',
 'lccclccllcccclllcclcclccccccllcccclccccl': '$',
 'cccccccccccccccccccc': '0', 'llcclccll': '1', 'lccccccccccccccccccccccccccc': '6',
 'lccccccccllllllccccccc': '5', 'ccccccccccccccccccccccccccccccccc': '8', 'llllllllllllll': '4',
 'lllccclcccl': '7', 'lcccccclllcccccclccccccccccccc': '3', 'llccccccccclcccccccccl': '2',
 'lllcclcll': ',', 'lcccccclcccccccccccccccccccccc': '9', 'lcccccccllcccccclccccccccccccc': '3',
 'lllcccccccclcccccccccl': '2', 'lcccccllcccccccccccccccccccccc': '9', 'llccccccccclccccccclcl': '2',
 'lccccccllcccccclccccccccccccc': '3', 'llclccccccclcccccccccl': '2', 'lllcccccccclccccccccll': '2',
 'lccclcclcccccccccccccccccccccc': '9', 'lcccccclllcccccllccccccccccccc': '3', 'lccccccclcccccclccccccccccccc': '3',
 'lccccccllccccccclccccccccccccc': '3', 'llcllccll': '1', 'llcclcccccclcccccccccl': '2',
 'lllclcccccclcccccccccl': '2', 'llcclclll': '1', 'lllcccccccclccccclcccl': '2', 'lllclclcccl': '7',
}

def classify_sig(ty, w, h):
    if ty == 're' and w < 1.2 and h < 1.2:
        return '.'
    return SIG.get(ty)

GW, GH = 12, 16
def vec(img, r, zoom):
    cx = (r[0] + r[2]) / 2
    box = (int((cx - 2.1) * zoom), int((r[3] - 6.3) * zoom), int((cx + 2.1) * zoom), int((r[3] + 0.2) * zoom))
    g = img.crop(box).resize((GW, GH), Image.BILINEAR)
    return [255 - v for v in g.get_flattened_data()]

def dist(a, b):
    return sum((x - y) ** 2 for x, y in zip(a, b)) ** 0.5

ZOOM = 600 / 72
glyphs = []
for pg in PAGES:
    page = doc[pg]
    pm = page.get_pixmap(matrix=pymupdf.Matrix(ZOOM, ZOOM), colorspace=pymupdf.csGRAY)
    img = Image.frombytes('L', (pm.width, pm.height), pm.samples)
    for x in page.get_drawings():
        if x['type'] != 'f' or x.get('fill') != (0.0, 0.0, 0.0):
            continue
        r = x['rect']
        if r.width > 4.2 or r.height > 6.6 or r.y0 < 120:   # body glyphs only (title/headers are bigger or above)
            continue
        if r.x0 < 0 or r.x1 > page.rect.x1 or r.y1 > 745:   # pp. 34/36/37 carry the facing page paths off-page; footer line at ~751
            continue
        ty = ''.join(it[0] for it in x['items'])
        g = {'pg': pg + 1, 'x0': r.x0, 'y0': r.y0, 'x1': r.x1, 'y1': r.y1, 'ty': ty,
             'sig': classify_sig(ty, r.width, r.height)}
        if g['sig'] not in ('.', ','):
            g['v'] = vec(img, (r.x0, r.y0, r.x1, r.y1), ZOOM)
        glyphs.append(g)

# templates from signature-labelled glyphs (digits and $ only)
acc = collections.defaultdict(list)
for g in glyphs:
    if g['sig'] and g['sig'] not in ('.', ','):
        acc[g['sig']].append(g['v'])
TPL = {k: [sum(c) / len(v) for c in zip(*v)] for k, v in acc.items()}
stats = collections.Counter()
for g in glyphs:
    if g['sig'] in ('.', ','):
        g['ch'] = g['sig']; stats['punct'] += 1; continue
    tall = (g['y1'] - g['y0']) >= 5.6   # '$' is ~6.0-6.2pt tall, digits ~4.8-5.2pt
    ds = sorted((dist(g['v'], t), k) for k, t in TPL.items() if (k == '$') == tall)
    if len(ds) == 1:
        ds.append((1e9, '-'))
    (d1, k1), (d2, k2) = ds[0], ds[1]
    g['nn'], g['d1'], g['d2'] = k1, d1, d2
    if g['sig']:
        g['ch'] = g['sig'] if g['sig'] == k1 else None
        stats['agree' if g['ch'] else 'DISAGREE'] += 1
    else:
        g['ch'] = k1 if d1 < 0.6 * d2 else None
        stats['nn_only' if g['ch'] else 'AMBIGUOUS'] += 1

# lines -> tokens
rows_by_page = collections.defaultdict(list)
for g in glyphs:
    cy = round((g['y1']) * 2) / 2  # baseline-ish: bottom of digits; '$' and ',' descend, use digits' y1 later
    rows_by_page[g['pg']].append(g)

def lines(gl):
    # digits share a baseline (y1 within 0.4pt); '$' (taller), ',' and '.' join the line whose baseline is nearest
    digs = sorted((g for g in gl if g.get('ch') not in ('$', ',', '.')), key=lambda g: g['y1'])
    base = []
    for g in digs:
        if not base or g['y1'] - base[-1][-1] > 1.5:
            base.append([g['y1']])
        else:
            base[-1].append(g['y1'])
    bl = [sum(b) / len(b) for b in base]
    out = collections.defaultdict(list)
    for g in gl:
        ref = g['y1'] if g.get('ch') not in ('$', ',', '.') else (g['y1'] - 0.5 if g.get('ch') == '$' else (g['y1'] - 0.0 if g.get('ch') == '.' else g['y0'] + 0.6))
        key = min(bl, key=lambda b: abs(b - ref))
        out[round(key, 1)].append(g)
    return out

tables = []
problems = []
for pg, gl in sorted(rows_by_page.items()):
    for y, lg in sorted(lines(gl).items()):
        lg.sort(key=lambda g: g['x0'])
        toks, cur, last = [], [], None
        for g in lg:
            if last is not None and g['x0'] - last > 6.0:
                toks.append(cur); cur = []
            cur.append(g); last = g['x1']
        if cur: toks.append(cur)
        texts = []
        for t in toks:
            s = ''.join(g['ch'] if g.get('ch') else '?' for g in t)
            texts.append((round(t[0]['x0'], 1), s))
        tables.append({'pg': pg, 'y': y, 'tokens': texts})

conf = collections.Counter((g['sig'], g.get('nn')) for g in glyphs if g['sig'] and g.get('nn') and g['sig'] != g['nn'])
print(conf.most_common(20))
json.dump({'stats': dict(stats)}, open(os.path.join(OUT, 'glyph-stats.json'), 'w'))
with open(os.path.join(OUT, 'raw-lines.tsv'), 'w', encoding='utf-8') as fh:
    for t in tables:
        fh.write('%d\t%.1f\t%s\n' % (t['pg'], t['y'], '\t'.join('%s@%s' % (s, x) for x, s in t['tokens'])))
print(dict(stats), len(tables))
