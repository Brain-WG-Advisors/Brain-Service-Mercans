"""Painel "onde estamos?": ESTADO.md + estado.md de cada frente + tickets abertos dos hubs.

Uso:  python scripts/onde_estamos.py

Só lê. Mostra, por frente, as linhas que marcam espera (⏳, 🔄, "Esperando", "- [ ]") e os itens prontos (✅) da última
atualização, e a lista de países com ticket aberto (properties dos hubs). A resposta ao usuário usa o formato
✅ pronto | ⏳ espera você | 🔄 espera outros/frente, só com o que mudou desde o último painel.
"""
import glob
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MARCA = re.compile(r'⏳|🔄|✅|[Ee]sperando|^\s*- \[ \]')


def resumo(p, limite=12):
    if not os.path.exists(p):
        return ['(sem estado)']
    t = io.open(p, encoding='utf-8').read()
    m = re.search(r'[Aa]tualizado em (\d{4}-\d{2}-\d{2})', t)
    linhas = [l.strip() for l in t.splitlines() if MARCA.search(l) and not l.startswith('|---')]
    linhas = [l[:220] + (' …' if len(l) > 220 else '') for l in linhas]
    cab = ['(atualizado em %s)' % m.group(1)] if m else []
    return cab + linhas[:limite] + (['… +%d linhas em %s' % (len(linhas) - limite, os.path.relpath(p, RAIZ))] if len(linhas) > limite else [])


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    print('# Onde estamos\n\n## Geral (ESTADO.md)')
    print('\n'.join('- ' + l for l in resumo(os.path.join(RAIZ, 'ESTADO.md'), 15)))
    for d in sorted(glob.glob(os.path.join(RAIZ, 'frentes', '*', 'estado.md'))):
        print('\n## Frente %s' % os.path.basename(os.path.dirname(d)))
        print('\n'.join('- ' + l for l in resumo(d)))
    abertos = []
    for p in sorted(glob.glob(os.path.join(RAIZ, 'paises', '*.md'))):
        t = io.open(p, encoding='utf-8').read()
        m = re.search(r'^tickets_abertos: (\d+)', t, re.M)
        if m and int(m.group(1)) > 0:
            s = re.search(r'^etapa_suporte: "?([^"\n]*)', t, re.M)
            abertos.append('%s: %s' % (os.path.basename(p)[:-3], s.group(1) if s else m.group(1)))
    print('\n## Tickets abertos nos hubs (%d países; atualizar com atualizar_tickets.py)' % len(abertos))
    print('\n'.join('- ' + a for a in abertos) or '- nenhum')
    return 0


if __name__ == '__main__':
    sys.exit(main())
