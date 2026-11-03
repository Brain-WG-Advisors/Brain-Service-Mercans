import sys, json, subprocess, glob; sys.path.insert(0, '.')
from lib import *
fields, R = load_reg(); byid = {r['id']: r for r in R}
rev = json.load(open('_qa/CCG-review-r2.json', encoding='utf-8'))
keys = set(rev['numeric_verification']['_numeric_unverified_reasons'])
need = {}
for fn in facts_files():
    for f in json.load(open(fn, encoding='utf-8'))['facts']:
        if f['key'] in keys and not byid[f['register_id']]['local_file'].strip():
            need.setdefault(f['register_id'], []).append((f['key'], f['value']))
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36'
res = []
for rid, kv in need.items():
    r = byid[rid]; url = r['url']; st = rid.split('-')[1][:2] if not rid.startswith(('US-FED', 'US-MULTI')) else ('FED' if rid.startswith('US-FED') else 'MULTI')
    ext = 'pdf' if url.lower().split('?')[0].endswith('.pdf') else 'html'
    d = f'00-official-sources/ccg-sources/{st}'; os.makedirs(d, exist_ok=True)
    out = f'{d}/{st}_{rid}_r2-curl_2026-11-02.{ext}'
    p = subprocess.run(['curl', '-sS', '-L', '-A', UA, '-m', '40', '-o', out, '-w', '%{http_code}|%{size_download}', url], capture_output=True, text=True)
    code = p.stdout.strip(); ok = code.startswith('200') and os.path.exists(out) and os.path.getsize(out) > 3000
    found = []
    if ok:
        t = text_of(out); found = [(k, v) for k, v in kv if find(v, t)]
        if not found: ok = False
    if not ok and os.path.exists(out): os.remove(out)
    if ok:
        md5 = hashlib.md5(open(out, 'rb').read()).hexdigest()
        r['local_file'] = out
        r['verification_method'] += f' | QA r2 2026-11-02: local copy by curl (HTTP {code.split("|")[0]}), md5 {md5}; figures located: ' + ', '.join(f'{k}={v}' for k, v in found)
    res.append({'rid': rid, 'url': url, 'http': code or p.stderr.strip()[:80], 'saved': ok, 'found': found, 'keys': kv})
save_reg(fields, R)
json.dump(res, open('_research/qa-r2-fix/download-log.json', 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
for x in res: print(x['rid'], x['http'], x['saved'], [k for k, _ in x['found']], '|', [k for k, _ in x['keys']][:2])
