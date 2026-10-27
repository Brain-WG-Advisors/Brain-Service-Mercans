"""Probe the round-4 electronic payroll files (zip of .txt in 02-client-reports-raw/round4-2026-10-22) WITHOUT printing any value.
Prints only structure: encodings, first non-blank character, XML root, element paths and attribute NAMES with counts,
and for non-XML files the line count and the text before the first ':' / '=' / ';' of each line when it is a short label.
Usage: python scripts/probe_round4.py"""
import os, re, sys, glob, zipfile, collections
import xml.etree.ElementTree as ET
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ZIPS = glob.glob(os.path.join(ROOT, '02-client-reports-raw', 'round4-2026-10-22', '*.zip'))
enc = collections.Counter(); first = collections.Counter(); roots = collections.Counter()
paths = collections.Counter(); attrs = collections.Counter(); xml_err = 0; nonxml = 0
labels = collections.Counter(); sizes = []
def local(t): return t.split('}', 1)[-1]
def walk(e, p):
    p = p + '/' + local(e.tag); paths[p] += 1
    for a in e.attrib: attrs[p + '@' + local(a)] += 1
    for c in e: walk(c, p)
for z in ZIPS:
    zf = zipfile.ZipFile(z)
    for i in zf.infolist():
        if i.is_dir(): continue
        raw = zf.read(i); sizes.append(len(raw))
        if raw.startswith(b'\xef\xbb\xbf'): raw = raw[3:]; e = 'utf-8-sig'
        else:
            try: raw.decode('utf-8'); e = 'utf-8'
            except UnicodeDecodeError: e = 'latin-1'
        enc[e] += 1
        txt = raw.decode('utf-8' if e.startswith('utf') else 'latin-1')
        s = txt.lstrip(); first[s[:1] if s else '(empty)'] += 1
        if s.startswith('<'):
            try:
                root = ET.fromstring(s.encode('utf-8')); roots[local(root.tag)] += 1; walk(root, '')
            except ET.ParseError: xml_err += 1
        else:
            nonxml += 1
            for l in txt.splitlines():
                m = re.match(r'\s*([A-Za-z_ ]{2,40})\s*[:=;]', l)
                if m: labels[m.group(1).strip()] += 1
print('files:', len(sizes), '| bytes min/max:', min(sizes), max(sizes))
print('encodings:', dict(enc)); print('first char:', dict(first)); print('xml roots:', dict(roots), '| xml parse errors:', xml_err, '| non-xml:', nonxml)
print('\nELEMENT PATHS (count of files x occurrences):')
for p, n in sorted(paths.items()): print(f'  {n:6d}  {p}')
print('\nATTRIBUTE NAMES:')
for p, n in sorted(attrs.items()): print(f'  {n:6d}  {p}')
if labels:
    print('\nNON-XML LINE LABELS (top 80):')
    for k, n in labels.most_common(80): print(f'  {n:6d}  {k}')

# ---- flat-file structure (added): lines, delimiters, fields per line, record-type prefix, field shape classes ----
nlines = collections.Counter(); delim = collections.Counter(); pref = collections.Counter(); nf = collections.Counter()
shape = collections.defaultdict(collections.Counter)
def cls(v):
    v = v.strip()
    if v == '': return 'empty'
    if re.fullmatch(r'-?\d+', v): return f'int{len(v)}'
    if re.fullmatch(r'-?\d+[.,]\d+', v): return 'decimal'
    if re.fullmatch(r'\d{4}-\d{2}-\d{2}', v): return 'date-iso'
    if re.fullmatch(r'\d{2}[/-]\d{2}[/-]\d{4}', v): return 'date-dmy'
    if re.fullmatch(r'[A-Z]{1,4}', v): return f'code{len(v)}'
    if re.fullmatch(r'[A-Za-zÁÉÍÓÚÑáéíóúñ .\'-]+', v): return 'text-alpha'
    if '@' in v: return 'email-like'
    return 'mixed'
for z in ZIPS:
    zf = zipfile.ZipFile(z)
    for i in zf.infolist():
        if i.is_dir(): continue
        txt = zf.read(i).decode('utf-8'); ls = [l for l in txt.splitlines() if l.strip()]
        nlines[len(ls)] += 1
        for l in ls:
            for d, nm in (('|', 'pipe'), (';', 'semicolon'), ('\t', 'tab'), (',', 'comma')):
                if d in l: delim[nm] += 1
            pref[l[:1]] += 1
            if '|' in l:
                parts = l.split('|'); nf[(l[:1], len(parts))] += 1
                for k, p in enumerate(parts): shape[(l[:1], k)][cls(p)] += 1
print('\nlines per file:', dict(sorted(nlines.items())))
print('lines containing delimiter:', dict(delim)); print('first char per line:', dict(pref))
print('(record first char, fields) counts:', dict(sorted(nf.items())))
print('\nFIELD SHAPES per (record first char, position):')
for k in sorted(shape): print(' ', k, dict(shape[k].most_common(4)))

# ---- fixed-width structure (added): per record type, line lengths and dominant character class per position (D digit, A letter, _ space, . other) ----
lens = collections.defaultdict(collections.Counter); pos = collections.defaultdict(lambda: collections.defaultdict(collections.Counter))
def ch(c): return 'D' if c.isdigit() else ('A' if c.isalpha() else ('_' if c == ' ' else '.'))
for z in ZIPS:
    zf = zipfile.ZipFile(z)
    for i in zf.infolist():
        if i.is_dir(): continue
        for l in zf.read(i).decode('utf-8').splitlines():
            if not l.strip(): continue
            t = l[:1]; lens[t][len(l)] += 1
            for k, c in enumerate(l): pos[t][k][ch(c)] += 1
print('\nFIXED-WIDTH: line lengths per record type')
for t in sorted(lens): print(' ', t, dict(sorted(lens[t].items())))
print('\nDOMINANT CLASS PER POSITION (runs: class x length, starting position):')
for t in sorted(pos):
    seq = [max(pos[t][k].items(), key=lambda x: x[1])[0] for k in range(max(pos[t]) + 1)]
    runs = []; s = 0
    for k in range(1, len(seq) + 1):
        if k == len(seq) or seq[k] != seq[s]: runs.append(f'{s}:{seq[s]}x{k - s}'); s = k
    print(' ', t, ' '.join(runs))
