"""Atualiza o estado dos tickets citados nos hubs (rodar ao "abrir o dia").

Uso:  python scripts/atualizar_tickets.py            # consulta a API e grava
      python scripts/atualizar_tickets.py --sem-api  # só recalcula a partir da última cópia em raw/tickets/api/

1. Junta os IDs (HRBS-, SR-, CT-) da seção "## Suporte" de cada hub em paises/.
2. Baixa o estado atual pela API (scripts/youtrack_fetch.ps1 -> raw/tickets/api/<hoje>/).
3. Em cada hub com ticket, reescreve SÓ:
   - as properties etapa_suporte, etapa_suporte_data, tickets_abertos, tickets_conferidos_em;
   - a linha "| [[suporte]] |" da tabela Situação (o trecho "API dd/mm: ..." é trocado; o "Antes (...)" fica).
4. Alinha a coluna Suporte do painel do 00-INDEX (🔄 se há aberto, ✅ se todos fechados).
Hubs sem ticket citado não são tocados. Imprime o que mudou.
"""
import datetime
import glob
import io
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FECHADOS = {'Resolved', 'Done', 'Rejected'}
HOJE = datetime.date.today()
ROT = HOJE.strftime('%d/%m')


def ler(p):
    return io.open(p, encoding='utf-8').read()


def gravar(p, s):
    io.open(p, 'w', encoding='utf-8', newline='').write(s)


def ids_do_hub(t):
    m = re.search(r'\n## Suporte[^\n]*\n(.*?)(?=\n## |\Z)', t, re.S)
    return sorted(set(re.findall(r'\b(HRBS-\d+|SR-\d+|CT-\d+)\b', m.group(1) if m else '')))


def estado(tid):
    for d in sorted(glob.glob(os.path.join(RAIZ, 'raw', 'tickets', 'api', '20*')), reverse=True):
        f = os.path.join(d, tid + '.md')
        if os.path.exists(f):
            m = re.search(r'^- \*\*Estado:\*\*[ \t]*(.*)$', ler(f), re.M)
            v = m.group(1).strip() if m else ''
            return v or None
    return None


def baixar(ids):
    ps = os.path.join(RAIZ, 'scripts', 'youtrack_fetch.ps1')
    for i in range(0, len(ids), 40):
        lote = ids[i:i + 40]
        q = 'issue id: ' + ', '.join(lote)
        r = subprocess.run(['powershell', '-NoProfile', '-ExecutionPolicy', 'Bypass', '-File', ps, '-Query', q],
                           cwd=RAIZ, capture_output=True, text=True, encoding='utf-8', errors='replace')
        resumo = [l for l in r.stdout.splitlines() if l.startswith(('Issues encontradas', 'Baixados', 'Atualizados'))]
        print('  API lote %d: %s' % (i // 40 + 1, ' · '.join(resumo) or r.stderr.strip()[:300]))


def set_prop(t, k, v):
    v = '' if v == '' else (v if re.fullmatch(r'\d{4}-\d{2}-\d{2}|\d+', str(v)) else '"%s"' % v)
    return re.sub(r'^%s:.*$' % k, '%s: %s' % (k, v), t, count=1, flags=re.M)


def main():
    hubs = {}
    for p in sorted(glob.glob(os.path.join(RAIZ, 'paises', '*.md'))):
        n = os.path.basename(p)[:-3]
        if n == 'README':
            continue
        ids = ids_do_hub(ler(p))
        if ids:
            hubs[n] = ids
    todos = sorted({i for v in hubs.values() for i in v})
    print('%d tickets citados em %d hubs' % (len(todos), len(hubs)))
    if '--sem-api' not in sys.argv:
        baixar(todos)

    painel = {}
    mudou = []
    for n, ids in hubs.items():
        p = os.path.join(RAIZ, 'paises', n + '.md')
        t = ler(p)
        st = {i: estado(i) for i in ids}
        unk = [i for i, v in st.items() if not v]
        opn = ['%s %s' % (i, v) for i, v in st.items() if v and v not in FECHADOS]
        cls = [i for i, v in st.items() if v and v in FECHADOS]
        partes = []
        if opn:
            partes.append('abertos: ' + ', '.join(opn))
        if cls:
            partes.append('%d fechado(s): %s' % (len(cls), ', '.join(cls)))
        if unk:
            partes.append('estado não lido na API: ' + ', '.join(unk))
        n_abertos = len(opn)
        resumo = ('%d aberto(s): %s' % (n_abertos, ', '.join(i.split(' ')[0] for i in opn)) if opn else 'sem tickets abertos') + \
                 ('; estado não lido: ' + ', '.join(unk) if unk else '')
        novo = t
        if novo.startswith('---'):
            novo = set_prop(novo, 'etapa_suporte', resumo)
            novo = set_prop(novo, 'etapa_suporte_data', HOJE.isoformat())
            novo = set_prop(novo, 'tickets_abertos', str(n_abertos) if not (unk and not opn and not cls) else '')
            novo = set_prop(novo, 'tickets_conferidos_em', HOJE.isoformat())
        emoji = '🔄' if opn else ('✅' if cls else '⏳')
        linhas = novo.split('\n')
        for k, l in enumerate(linhas):
            if l.startswith('| [[suporte]] |'):
                c = [x.strip() for x in l.strip().strip('|').split('|')]
                obs = '|'.join(c[3:]).strip()
                m = re.match(r'^API \d\d/\d\d: .*?\.(?= Antes \(|$)', obs)
                if m:
                    resto = obs[m.end():].strip()
                else:
                    resto = ('Antes (%s): %s' % (c[2] or 'sem data', obs)) if obs else ''
                api = 'API %s: %s.' % (ROT, '; '.join(partes))
                linhas[k] = '| [[suporte]] | %s | %s | %s |' % (emoji, HOJE.isoformat(), (api + ' ' + resto).strip())
                break
        novo = '\n'.join(linhas)
        if novo != t:
            antes = re.search(r'^tickets_abertos: (.*)$', t, re.M)
            mudou.append('%s: abertos %s -> %s' % (n, antes.group(1) if antes else '?', n_abertos))
            gravar(p, novo)
        painel[n] = emoji

    ip = os.path.join(RAIZ, '00-INDEX.md')
    s = ler(ip)
    s2 = s
    for n, e in painel.items():
        s2 = re.sub(r'^(\| \[\[%s\]\] \| [^|]* \| [^|]* \| )[^|]*( \|)' % re.escape(n), r'\g<1>%s\2' % e, s2, count=1, flags=re.M)
    if s2 != s:
        gravar(ip, s2)
    print('Hubs alterados: %d' % len(mudou))
    for m in mudou:
        print('  ' + m)
    return 0


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.exit(main())
