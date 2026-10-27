"""Contexto do país em um passo, para abrir qualquer task.

Uso:  python scripts/contexto_pais.py <País ou código>  [--completo]
      ex.: python scripts/contexto_pais.py CO  |  python scripts/contexto_pais.py espanha

Junta, a partir do cérebro (só leitura):
  - properties do hub (etapas, versões vigentes, tickets abertos);
  - tickets abertos com estado, título e data da última consulta à API (raw/tickets/api/);
  - correções do país (correcoes.md);
  - pendências abertas e valores sem fonte/vigência do hub.
Sem --completo, linhas longas são cortadas; a fonte é sempre o arquivo indicado.
"""
import glob
import io
import os
import re
import sys
import unicodedata

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CORTE = 260


def norm(t):
    t = unicodedata.normalize('NFKD', t).encode('ascii', 'ignore').decode()
    return re.sub(r'[^a-z0-9]', '', t.lower())


def ler(p):
    return io.open(p, encoding='utf-8').read()


def props(texto):
    if not texto.startswith('---'):
        return {}
    bloco = texto.split('---', 2)[1]
    out = {}
    for linha in bloco.splitlines():
        if ':' in linha:
            k, v = linha.split(':', 1)
            out[k.strip()] = v.strip().strip('"')
    return out


def achar_hub(arg):
    alvo = norm(arg)
    for p in sorted(glob.glob(os.path.join(RAIZ, 'paises', '*.md'))):
        nome = os.path.basename(p)[:-3]
        if nome == 'README':
            continue
        t = ler(p)
        if norm(nome) == alvo or norm(props(t).get('codigo', '')) == alvo:
            return nome, t
        titulo = t.split('\n# ', 1)[-1].split('\n', 1)[0] if '\n# ' in t else ''
        if norm(titulo) == alvo:
            return nome, t
    return None, None


def secao(texto, titulo):
    m = re.search(r'\n## ' + re.escape(titulo) + r'[^\n]*\n(.*?)(?=\n## |\Z)', texto, re.S)
    return m.group(1) if m else ''


def corta(s, completo):
    s = s.strip()
    return s if completo or len(s) <= CORTE else s[:CORTE] + ' …'


def estado_api(tid):
    pastas = sorted(glob.glob(os.path.join(RAIZ, 'raw', 'tickets', 'api', '20*')), reverse=True)
    for d in pastas:
        f = os.path.join(d, tid + '.md')
        if os.path.exists(f):
            t = ler(f)
            est = re.search(r'^- \*\*Estado:\*\*\s*(.*)$', t, re.M)
            tit = t.split('\n', 1)[0].lstrip('# ').strip()
            upd = re.search(r'^- \*\*Atualizado:\*\*\s*(.*)$', t, re.M)
            return (est.group(1).strip() if est else '?'), tit, os.path.basename(d), (upd.group(1).strip() if upd else '')
    return 'sem cópia da API', '', '', ''


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    completo = '--completo' in sys.argv
    if not args:
        print(__doc__)
        return 1
    nome, t = achar_hub(' '.join(args))
    if not nome:
        print('Hub não encontrado para "%s". Use o nome do arquivo em paises/ ou o código ISO.' % ' '.join(args))
        return 1
    p = props(t)
    out = ['# Contexto: %s (%s)' % (nome, p.get('codigo', '?')),
           'Hub: paises/%s.md · atualizado em %s · skill: %s' % (nome, p.get('atualizado_em', '?'), p.get('skill') or 'não há')]

    out.append('\n## Etapas')
    for k in ('research', 'design', 'producao', 'suporte'):
        v = p.get('etapa_' + k, '')
        d = p.get('etapa_%s_data' % k, '')
        out.append('- %s: %s%s' % (k.capitalize(), v or '—', (' (%s)' % d) if d else ''))

    out.append('\n## Versões vigentes (regra 8: maior número)')
    for k, rot in (('ccg', 'CCG'), ('wtc', 'WTC'), ('dd', 'DD'), ('report_specs', 'Report Specs'), ('sir', 'SIR'), ('payslip', 'Payslip')):
        v = p.get(k, '')
        d = p.get(k + '_data', '')
        out.append('- %s: %s%s' % (rot, v or 'não registrado no hub', (' (%s)' % d) if d else ''))
    if p.get('versoes_fonte'):
        out.append('- Fonte das versões: ' + p['versoes_fonte'])
    if p.get('obs_versoes'):
        out.append('- ⚠️ ' + p['obs_versoes'])

    sup = secao(t, 'Suporte')
    ids = sorted(set(re.findall(r'\b(HRBS-\d+|SR-\d+|CT-\d+)\b', sup)))
    abertos = []
    for tid in ids:
        est, tit, quando, upd = estado_api(tid)
        if est not in ('Resolved', 'Done', 'Rejected'):
            abertos.append('- %s · %s · %s (API %s%s)' % (tid, est, tit, quando, ', atualizado ' + upd if upd else ''))
    out.append('\n## Tickets abertos (%d de %d citados no hub)' % (len(abertos), len(ids)))
    out += abertos or ['- nenhum']

    corr = [l for l in ler(os.path.join(RAIZ, 'correcoes.md')).splitlines()
            if l.startswith('|') and ('[[%s]]' % nome in l or '[[%s|' % nome in l)]
    out.append('\n## Correções do país (%d, correcoes.md; ler antes de responder)' % len(corr))
    out += ['- ' + corta(l.strip('| '), completo) for l in corr]

    pend = [l for l in secao(t, 'Pendências').splitlines() if l.startswith('- [ ]')]
    out.append('\n## Pendências abertas (%d)' % len(pend))
    out += [corta(l, completo) for l in pend] or ['- nenhuma']

    sem = [l for l in secao(t, 'Valores-chave').splitlines() if l.startswith('|') and '⚠️' in l]
    out.append('\n## Valores sem fonte ou sem vigência (%d) — não afirmar sem conferir' % len(sem))
    out += ['- ' + corta(l.strip('| '), completo) for l in sem] or ['- nenhum']

    sys.stdout.reconfigure(encoding='utf-8')
    print('\n'.join(out))
    return 0


if __name__ == '__main__':
    sys.exit(main())
