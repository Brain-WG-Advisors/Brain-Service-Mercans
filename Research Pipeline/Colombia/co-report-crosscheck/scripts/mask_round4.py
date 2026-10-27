"""Round-4 masking: the 871 electronic payroll files of September 2026 (one zip of caret-delimited .txt) in
02-client-reports-raw/round4-2026-10-22 -> 03-client-reports-masked/round4/NE_0001.txt ...
Runs LOCALLY; never prints a value. NEW key for this round (99-local-only/masking-key-round4.json): the round 1-3 key is not on this machine.
Format (probe_round4.py): one record per line, fields separated by '^', field 0 = 3-letter record type.
Rules (field index after the record type, 1-based as in the probe):
  REC (worker)   5 = document number -> ID ; 6, 7, 8, 9 = surnames / names -> NAME ; 13 = address -> ADDRESS ; 17 = employee code -> ID
  PAG (payment)  5 = bank account number -> ACCOUNT
  ENC (header)   8 = employee code (same shape as REC 17) -> ID ; 11 and 16 = free identifiers / text -> MASKED_TEXT
  every field     e-mail -> EMAIL token ; any run of 7+ digits inside a text field -> ID token
Everything else (record types, codes, dates, amounts, concept labels, company data in EMI) is kept, so the field rules can be checked.
Output file names are sequential; the zip entry name -> output name map goes to the key file only.
Writes 04-output/round4/pii-check.txt (statistics only). Usage: python scripts/mask_round4.py [--dry]"""
import os, re, sys, glob, json, zipfile, collections
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ZIPS = glob.glob(os.path.join(ROOT, '02-client-reports-raw', 'round4-2026-10-22', '*.zip'))
OUT = os.path.join(ROOT, '03-client-reports-masked', 'round4')
KEY = os.path.join(ROOT, '99-local-only', 'masking-key-round4.json')
CHK = os.path.join(ROOT, '04-output', 'round4', 'pii-check.txt')
DRY = '--dry' in sys.argv
RULES = {'REC': {5: 'ID', 6: 'NAME', 7: 'NAME', 8: 'NAME', 9: 'NAME', 13: 'ADDRESS', 17: 'ID'},
         'PAG': {5: 'ACCOUNT'},
         'ENC': {8: 'ID', 11: 'TEXT', 16: 'TEXT'}}
EMAIL = re.compile(r'[\w.+-]+@[\w-]+\.[\w.-]+')
LONGDIG = re.compile(r'(?<![\d.])\d{7,}(?![\d.])')
key = {'values': {}, 'files': {}}
if os.path.exists(KEY): key = json.load(open(KEY, encoding='utf-8'))
cnt = collections.Counter({k: 0 for k in ('ID', 'NAME', 'ADDRESS', 'ACCOUNT', 'EMAIL')})
for v in key['values'].values():
    m = re.fullmatch(r'([A-Z]+)_(\d{4})', v)
    if m: cnt[m.group(1)] = max(cnt[m.group(1)], int(m.group(2)))
def token(kind, val):
    k = kind + '|' + val
    if k not in key['values']:
        cnt[kind] += 1; key['values'][k] = f'{kind}_{cnt[kind]:04d}'
    return key['values'][k]
stats = collections.Counter(); files = 0
if not DRY: os.makedirs(OUT, exist_ok=True)
for z in ZIPS:
    zf = zipfile.ZipFile(z)
    for info in sorted((i for i in zf.infolist() if not i.is_dir()), key=lambda i: i.filename):
        files += 1
        name = key['files'].setdefault(info.filename, f'NE_{len(key["files"]) + 1:04d}.txt')
        out_lines = []
        for line in zf.read(info).decode('utf-8').splitlines():
            if not line.strip(): out_lines.append(line); continue
            f = line.split('^'); rule = RULES.get(f[0], {})
            for k in range(1, len(f)):
                v = f[k]; s = v.strip()
                if s == '': continue
                kind = rule.get(k)
                if kind == 'TEXT': f[k] = 'MASKED_TEXT'; stats[f'{f[0]}.{k} TEXT'] += 1
                elif kind: f[k] = token(kind, s); stats[f'{f[0]}.{k} {kind}'] += 1
                else:
                    v2 = EMAIL.sub(lambda m: token('EMAIL', m.group(0)), v)
                    if not re.fullmatch(r'-?\d+(\.\d+)?', s):            # amounts and codes stay; digit runs inside text are masked
                        v2 = LONGDIG.sub(lambda m: token('ID', m.group(0)), v2)
                    if v2 != v: stats[f'{f[0]}.{k} inline'] += 1
                    f[k] = v2
            out_lines.append('^'.join(f))
        if not DRY: open(os.path.join(OUT, name), 'w', encoding='utf-8', newline='\n').write('\n'.join(out_lines) + '\n')
lines = [f'Round 4 masking - {files} electronic payroll files (September 2026) -> 03-client-reports-masked/round4/ (new key)', '',
         'Masked fields (record.field kind: count):'] + [f'  {k}: {n}' for k, n in sorted(stats.items())] + \
        ['', 'Distinct tokens: ' + ', '.join(f'{k} {v}' for k, v in sorted(cnt.items()))]
if not DRY:
    os.makedirs(os.path.dirname(KEY), exist_ok=True); json.dump(key, open(KEY, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    os.makedirs(os.path.dirname(CHK), exist_ok=True); open(CHK, 'w', encoding='utf-8').write('\n'.join(lines) + '\n')
print('\n'.join(lines)); print('DRY RUN - nothing written' if DRY else 'written')
