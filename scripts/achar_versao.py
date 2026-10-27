"""Acha a maior versão de um artefato antes de editar (regra 8; base = linhagem do Drive).

Uso:  python scripts/achar_versao.py <País|código> <ccg|wtc|dd|sir|payslip|spec> [termo extra]
      ex.: python scripts/achar_versao.py CO wtc   |   python scripts/achar_versao.py espanha spec CRA

Varre (só leitura): Downloads, Drive (Country Folders/<país>, sem Archived) e Research Pipeline/<país>.
Lista cada arquivo com versão, data de modificação e md5 (até 50 MB) e aponta a maior versão.
Aceita "v1.6", "V1_6" e "v1-6" no nome. Arquivo -DRAFT- é marcado (não conta como vigente pela metodologia).
"""
import glob
import hashlib
import io
import os
import re
import sys
import time
import unicodedata

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DRIVE = r'G:\Drives compartilhados\Compliance Team\Country Folders'
DOWN = os.path.join(os.path.expanduser('~'), 'Downloads')
TIPOS = {
    'ccg': r'ccg|regulation guide|configuration guide',
    'wtc': r'wtc|wage ?type',
    'dd': r'(^|[^a-z])dd([^a-z]|$)|data ?dictionary',
    'sir': r'(^|[^a-z])sir([^a-z]|$)|statutory integration|staturory integration',
    'payslip': r'payslip',
    'spec': r'spec|statutory report',
}
VER = re.compile(r'[vV]\s?(\d+)[._-](\d+)')
EN = {'ZA': 'South Africa', 'DE': 'Germany', 'DZ': 'Algeria', 'AU': 'Australia', 'BH': 'Bahrain', 'BY': 'Belarus',
      'BE': 'Belgium', 'BW': 'Botswana', 'BG': 'Bulgaria', 'CA': 'Canada', 'KZ': 'Kazakhstan', 'TD': 'Chad', 'CL': 'Chile',
      'CN': 'China', 'CY': 'Cyprus', 'CO': 'Colombia', 'CG': 'Republic of Congo', 'CI': "Côte d'Ivoire", 'CR': 'Costa Rica',
      'DK': 'Denmark', 'EG': 'Egypt', 'ES': 'Spain', 'EE': 'Estonia', 'PH': 'Philippines', 'FI': 'Finland', 'FR': 'France',
      'GA': 'Gabon', 'GQ': 'Eq. Guinea', 'NL': 'Netherlands', 'HU': 'Hungary', 'IN': 'India', 'ID': 'Indonesia',
      'IE': 'Ireland', 'KW': 'Kuwait', 'LB': 'Lebanon', 'LT': 'Lithuania', 'MY': 'Malaysia', 'MA': 'Morocco',
      'MZ': 'Mozambique', 'NA': 'Namibia', 'NO': 'Norway', 'PT': 'Portugal', 'CD': 'Democratic Republic of Congo',
      'GB': 'GB', 'RO': 'Romania', 'SG': 'Singapore', 'SE': 'Sweden', 'TH': 'Thailand', 'TW': 'Taiwan', 'CZ': 'Czechia',
      'UA': 'Ukraine', 'VN': 'Vietnam'}


def norm(t):
    t = unicodedata.normalize('NFKD', t).encode('ascii', 'ignore').decode()
    return re.sub(r'[^a-z0-9]', '', t.lower())


def hub(arg):
    alvo = norm(arg)
    for p in glob.glob(os.path.join(RAIZ, 'paises', '*.md')):
        n = os.path.basename(p)[:-3]
        t = io.open(p, encoding='utf-8').read()
        m = re.search(r'^codigo: "?([A-Z]{2})', t, re.M)
        cc = m.group(1) if m else ''
        if norm(n) == alvo or norm(cc) == alvo:
            return n, cc
    return None, None


def md5(p):
    try:
        if os.path.getsize(p) > 50 * 1024 * 1024 or p.endswith(('.gsheet', '.gdoc')):
            return '-'
        return hashlib.md5(open(p, 'rb').read()).hexdigest()[:10]
    except OSError:
        return '?'


def main():
    if len(sys.argv) < 3 or sys.argv[2].lower() not in TIPOS:
        print(__doc__)
        return 1
    nome, cc = hub(sys.argv[1])
    if not nome:
        print('País não encontrado em paises/.')
        return 1
    tipo = sys.argv[2].lower()
    extra = ' '.join(sys.argv[3:]).lower()
    en = EN.get(cc, '')
    locais = [('Downloads', DOWN, 1), ('Drive', os.path.join(DRIVE, en), 4)]
    rp = [d for d in glob.glob(os.path.join(RAIZ, 'Research Pipeline', '*')) if norm(os.path.basename(d)) in (norm(nome), norm(en))]
    locais += [('Research Pipeline', d, 4) for d in rp]
    achados = []
    for rot, raiz, prof in locais:
        if not os.path.isdir(raiz):
            continue
        for dp, dn, fn in os.walk(raiz):
            dn[:] = [x for x in dn if 'archiv' not in x.lower()]
            if dp[len(raiz):].count(os.sep) >= prof:
                dn[:] = []
            for f in fn:
                low = (os.path.basename(dp) + ' / ' + f).lower()
                if not re.search(TIPOS[tipo], low) or (extra and extra not in low):
                    continue
                if rot == 'Downloads' and not (cc.lower() in f.lower() or norm(en) in norm(f) or norm(nome) in norm(f)):
                    continue
                v = VER.search(f)
                if not v:
                    continue
                p = os.path.join(dp, f)
                achados.append(((int(v.group(1)), int(v.group(2))), rot, p, time.strftime('%Y-%m-%d %H:%M', time.localtime(os.path.getmtime(p))), md5(p), 'draft' in f.lower()))
    sys.stdout.reconfigure(encoding='utf-8')
    if not achados:
        print('Nenhum arquivo com versão no nome para %s %s.' % (nome, tipo.upper()))
        return 0
    achados.sort(key=lambda a: (a[0], a[3]), reverse=True)
    print('# %s %s%s: %d arquivo(s)' % (nome, tipo.upper(), (' "%s"' % extra) if extra else '', len(achados)))
    for ver, rot, p, dt, h, dr in achados[:15]:
        print('- v%d.%d%s · %s · %s · md5 %s · %s' % (ver[0], ver[1], ' (DRAFT)' if dr else '', rot, dt, h, p))
    final = [a for a in achados if not a[5]]
    if final:
        top = final[0]
        print('\n**Maior versão (não DRAFT): v%d.%d** · %s · %s' % (top[0][0], top[0][1], top[1], top[2]))
        mesmos = [a for a in final if a[0] == top[0] and a[4] not in ('-', '?')]
        if len({a[4] for a in mesmos}) > 1:
            print('⚠️ Há cópias da mesma versão com md5 diferente: comparar antes de editar.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
