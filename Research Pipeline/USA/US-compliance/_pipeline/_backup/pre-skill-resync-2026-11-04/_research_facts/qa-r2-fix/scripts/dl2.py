import sys, json, subprocess; sys.path.insert(0, '.')
from lib import *
fields, R = load_reg(); byid = {r['id']: r for r in R}
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36'
for rid in ['US-CTP7-001', 'US-PA-009', 'US-SCP52-005', 'US-TNR3-003', 'US-TXR3-002', 'US-VAR3-002', 'US-KY-002']:
    r = byid[rid]; url = r['url']; st = rid.split('-')[1][:2]
    ext = 'pdf' if url.lower().split('?')[0].endswith('.pdf') else 'html'
    out = f'00-official-sources/ccg-sources/{st}/{st}_{rid}_r2-curl_2026-11-02.{ext}'
    p = subprocess.run(['curl', '-sS', '-L', '-A', UA, '-m', '40', '-o', out, '-w', '%{http_code}', url], capture_output=True, text=True)
    if p.stdout.strip() == '200' and os.path.getsize(out) > 3000:
        md5 = hashlib.md5(open(out, 'rb').read()).hexdigest(); r['local_file'] = out
        r['verification_method'] += f' | QA r2 2026-11-02: local copy by curl (HTTP 200), md5 {md5}; the keyed figure was NOT located by text search in this copy (zero rate stated as a rule, figure in a script-rendered table, or computed example) - see AGENT2-R2.md'
        print(rid, 'saved', os.path.getsize(out))
    else:
        print(rid, 'failed', p.stdout); os.path.exists(out) and os.remove(out)
save_reg(fields, R)
