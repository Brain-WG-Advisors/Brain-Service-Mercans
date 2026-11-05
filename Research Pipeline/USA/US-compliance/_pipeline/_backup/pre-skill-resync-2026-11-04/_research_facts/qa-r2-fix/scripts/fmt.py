import json, glob, os, re, sys
os.chdir(r"C:/Users/instituto/Documents/brain-service/Research Pipeline/USA/US-compliance/_research")
def style(path):
    b = open(path, 'rb').read(); nl = '\r\n' if b'\r\n' in b else '\n'
    m = re.search(rb'\n( +)"', b); ind = len(m.group(1)) if m else 1
    asc = not re.search(rb'[\x80-\xff]', b) and b'\u' in b
    return nl, ind, asc
def dump(obj, path, ref=None):
    nl, ind, asc = style(ref or path)
    s = json.dumps(obj, ensure_ascii=asc, indent=ind)
    open(path, 'w', encoding='utf-8', newline='').write(s.replace('\n', nl) + ('' if not open(ref or path,'rb').read().endswith(b'\n') else nl))
if __name__ == '__main__':
    for f in glob.glob('*-facts.json'):
        bk = 'qa-r2-fix/_backup/' + f
        if os.path.exists(bk): dump(json.load(open(f, encoding='utf-8')), f, bk)
