"""Confere um arquivo depois de "importei/copiei para o Drive" (resultado em 1 linha).

Uso:  python scripts/conferir_import.py <arquivo local> <arquivo ou pasta no Drive>
      ex.: python scripts/conferir_import.py "Research Pipeline/Colombia/x/CO-WTC-001_v1.6.xlsx" "G:/.../Colombia/03 - WTC"

- Arquivo binário no Drive (xlsx/docx): compara md5 local × Drive.
- Se o destino for pasta: procura o mesmo nome (ou o mesmo nome em .gsheet/.gdoc).
- .gsheet/.gdoc (Google nativo) não tem md5 no disco: confirma só que existe e a data; o conteúdo se confere
  pelo export (memória "Sheets: gviz pula linhas vazias": usar export?format=csv&gid).
"""
import hashlib
import os
import sys
import time


def md5(p):
    return hashlib.md5(open(p, 'rb').read()).hexdigest()


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        return 1
    loc, dst = sys.argv[1], sys.argv[2]
    sys.stdout.reconfigure(encoding='utf-8')
    if not os.path.isfile(loc):
        print('❌ local não encontrado: %s' % loc)
        return 1
    nome = os.path.basename(loc)
    if os.path.isdir(dst):
        base = os.path.splitext(nome)[0]
        cands = [os.path.join(dst, nome)] + [os.path.join(dst, base + e) for e in ('.gsheet', '.gdoc')]
        dst = next((c for c in cands if os.path.exists(c)), cands[0])
    if not os.path.exists(dst):
        print('❌ não está no Drive: %s' % dst)
        return 1
    quando = time.strftime('%Y-%m-%d %H:%M', time.localtime(os.path.getmtime(dst)))
    if dst.endswith(('.gsheet', '.gdoc')):
        print('⚠️ existe como Google nativo (%s, %s): md5 indisponível; conferir conteúdo pelo export csv/txt' % (os.path.basename(dst), quando))
        return 0
    a, b = md5(loc), md5(dst)
    print(('✅ idêntico' if a == b else '❌ DIFERENTE') + ' · local %s · Drive %s (%s) · %s' % (a[:10], b[:10], quando, dst))
    return 0 if a == b else 2


if __name__ == '__main__':
    sys.exit(main())
