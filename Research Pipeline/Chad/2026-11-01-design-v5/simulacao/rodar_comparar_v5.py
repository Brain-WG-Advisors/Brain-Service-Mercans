"""Roda comparar.py (copia identica, md5 0e3709fe...) contra o _build_v5.py em vez do _build_v4.py.

comparar.py carrega o motor "nosso" por um caminho fixo (V4 = ../../../2026-10-29-design-v4/_build_v4.py).
Para nao alterar o arquivo, este runner le o texto e troca em memoria (1) essa linha e (2), desde a rodada 3,
as contas do nosso lado nas linhas de deducao (v5 usa as da WTC V3.0: 58100 no lugar de 58141, 58101 no lugar de 58142).
Saida (nesta pasta): resultado.csv e RESULTADO.md, com os rotulos "v4" trocados por "v5".
    python -I rodar_comparar_v5.py
"""
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, 'comparar.py')
OLD = "V4 = os.path.join(HERE, '..', '..', '..', '2026-10-29-design-v4', '_build_v4.py')"
NEW = "V4 = os.path.join(HERE, '..', '_build_v5.py')"

with open(SRC, encoding='utf-8') as fh:
    code = fh.read()
assert code.count(OLD) == 1, 'linha do caminho do v4 nao encontrada: comparar.py mudou'
code = code.replace(OLD, NEW)
for a, b in (("g('58141'), g('58100')", "g('58100'), g('58100')"), ("g('58142'), g('58101')", "g('58101'), g('58101')")):
    assert code.count(a) == 1, a
    code = code.replace(a, b)
sys.path.insert(0, HERE)
g = {'__name__': '__main__', '__file__': SRC}
exec(compile(code, SRC, 'exec'), g)

# rotulos: o motor "nosso" agora e o v5 (as contas comparadas sao as mesmas do v4)
for fn in ('RESULTADO.md', 'resultado.csv'):
    p = os.path.join(HERE, fn)
    enc = 'utf-8-sig' if fn.endswith('.csv') else 'utf-8'
    with open(p, encoding=enc) as fh:
        t = fh.read()
    t = t.replace('nosso v4', 'nosso v5').replace('nosso_v4', 'nosso_v5').replace('(v4 ', '(v5 ').replace('v4 conta', 'v5 conta') \
         .replace('_build_v4.py', '_build_v5.py').replace('10 cenarios do v4', '10 cenarios do v4 rodados no v5')
    # causas novas do v5 que o OWN do comparar.py nao conhece: trocadas por cenario (linha de tabela no .md, linha no .csv)
    CAUSA = {'7': 'v5 9148051: transporte inteiro fora da CNPS (guia CNPS p. 8; a confirmar com o usuario); o Dev tira so a parte isenta (58104)',
             '2': 'v5 9148053 banda 6: taxa 20 em 58131 so com salario segurado (58550 > 0)',
             '8': 'faixas do IRPP do Dev com limite x.99: 1 XAF a menos quando o IRPP cai em meio franco; v5 grava 800.000 (art. 1-IV)',
             '12': 'faixas do IRPP do Dev com limite x.99: 1 XAF a menos quando o IRPP cai em meio franco; v5 grava 800.000 (art. 1-IV)',
             '10': 'v5 9148081/082: parte da folha do jovem diplomado < 35 fora da TF/TA (art. 188-10, 174-3; flag 58219); o Dev nao tem'}
    IRPP11 = ' | e: v5 tributa o nao residente pela tabela progressiva (CGI art. 44-II-2, 847); o Dev usa 18% (art. 116). Aqui o comparar.py roda o nosso com os ramos da CNPS desligados (flags do v4); no v5 o padrao e todos os ramos (VALIDATION cenario 11)'
    out, cur = [], None
    for line in t.split('\n'):
        if line.startswith('## Cenario '):
            cur = line.split()[2]
        key = line.split(' ')[0] if fn.endswith('.csv') else cur
        if 'NAO ATRIBUIDA' in line:
            line = line.replace('NAO ATRIBUIDA', CAUSA.get(key, 'v5: ver CHANGELOG'))
        if key == '11' and line.startswith(('| IRPP (2552+2592)', '| Liquido', '11 (extra) Nao residente 800.000;IRPP', '11 (extra) Nao residente 800.000;Liquido')):
            line = line.rstrip(' |') + IRPP11 + (' |' if line.startswith('|') else '')
        out.append(line)
    t = '\n'.join(out)
    if fn == 'RESULTADO.md':
        n_bate = t.count('**Bate ao franco')
        t = t.replace('Feito em 2026-10-30 (frente Chade).', 'Gerado em 2026-11-01 (frente Chade, v5 rodada 3; texto-base de 2026-10-30).')
        t = t.replace('# Simulacao Chade: motor do Dev (td_2026) x nosso v5, 10 cenarios do v4 rodados no v5', '# Simulacao Chade: motor do Dev (td_2026) x nosso v5 (10 cenarios do v4 + 2 extras)')
        import re as _re
        t = _re.sub(r'\*\*\d+ de 10\*\* \(1, 3 e 10\)', '**%d de 10**' % sum(1 for s in t.split('## Cenario ')[1:11] if '**Bate ao franco' in s), t)
        t = t.replace('- Liquido = remuneracao em dinheiro', '- **v5:** o Liquido desta tabela NAO desconta o PSA de 400 (comparar.py inalterado); o liquido do v5 com PSA esta em `../chad-design-blueprint-claude-v5/VALIDATION.md`. O PSA nao existe no Dev.\n- Liquido = remuneracao em dinheiro')
        t = t.rstrip('\n') + '\n| 2026-11-01 | chade | rodado contra o v5 (`rodar_comparar_v5.py`; comparar.py e sim_dev.py copias identicas) |\n'
    with open(p, 'w', encoding=enc, newline='') as fh:
        fh.write(t)
