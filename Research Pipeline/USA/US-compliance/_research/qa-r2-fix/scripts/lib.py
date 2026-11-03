import csv, json, glob, os, re, hashlib, html
BASE = r"C:/Users/instituto/Documents/brain-service/Research Pipeline/USA/US-compliance"
os.chdir(BASE)
REG = '00-official-sources/legal-basis-register.csv'
CACHE = r"C:/Users/INSTIT~1/AppData/Local/Temp/claude/C--Users-instituto-Documents-brain-service-frentes-eua/272453a3-1ad8-4a54-b824-fda2544cbf81/scratchpad/txtcache"
os.makedirs(CACHE, exist_ok=True)
def load_reg():
    with open(REG, encoding='utf-8', newline='') as f:
        rd = csv.DictReader(f); rows = list(rd); return rd.fieldnames, rows
def save_reg(fields, rows):
    with open(REG, 'w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields, quoting=csv.QUOTE_MINIMAL); w.writeheader(); w.writerows(rows)
def facts_files():
    return sorted(glob.glob('_research/*-facts.json'))
def files_of(row):
    return [x.strip() for x in (row.get('local_file') or '').split(';') if x.strip()]
def text_of(path):
    if not os.path.exists(path): return ''
    h = hashlib.md5(path.encode()).hexdigest()
    cp = os.path.join(CACHE, h + '.txt')
    if os.path.exists(cp): return open(cp, encoding='utf-8').read()
    t = ''
    ext = path.lower().rsplit('.', 1)[-1]
    try:
        if ext == 'pdf':
            import pymupdf
            d = pymupdf.open(path); t = '\n'.join(f'[[PAGE {i+1}]]\n' + p.get_text() for i, p in enumerate(d))
        elif ext in ('html', 'htm'):
            t = open(path, encoding='utf-8', errors='ignore').read()
            t = re.sub(r'(?is)<(script|style).*?</\1>', ' ', t); t = html.unescape(re.sub(r'<[^>]+>', ' ', t))
        elif ext == 'xlsx':
            import openpyxl
            wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
            t = '\n'.join(' | '.join(str(c) for c in r if c is not None) for ws in wb for r in ws.iter_rows(values_only=True))
        elif ext == 'docx':
            import docx
            t = '\n'.join(p.text for p in docx.Document(path).paragraphs)
        else:
            t = open(path, encoding='utf-8', errors='ignore').read()
    except Exception as e:
        t = ''
    t = re.sub(r'[ \t\u00a0]+', ' ', t)
    open(cp, 'w', encoding='utf-8').write(t)
    return t
def variants(v):
    out = set()
    if isinstance(v, bool) or not isinstance(v, (int, float)): return out
    for x in (v, v * 100, v / 100):
        x = round(x, 6)
        if x == int(x):
            i = int(x); out |= {f'{i:,}', str(i), f'{i:,}.00', f'{i}.00'}
        else:
            for d in (1, 2, 3, 4, 5):
                s = f'{x:.{d}f}'
                if float(s) == x: out |= {s, f'{x:,.{d}f}', s.lstrip('0') if s.startswith('0.') else s}
    return {o for o in out if o}
def find(v, text):
    hits = []
    for s in variants(v):
        for m in re.finditer(r'(?<![\d.,])' + re.escape(s) + r'(?![\d]|[.,]\d)', text):
            hits.append((m.start(), s))
    return sorted(hits)
def page_at(text, pos):
    p = text.rfind('[[PAGE ', 0, pos)
    return text[p+7:text.find(']]', p)] if p >= 0 else None
def snippet(text, pos, w=90):
    return re.sub(r'\s+', ' ', text[max(0, pos - w): pos + w]).strip()
