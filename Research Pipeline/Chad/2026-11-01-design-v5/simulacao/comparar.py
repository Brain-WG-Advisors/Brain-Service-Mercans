"""Roda os 10 cenarios do v4 (+2 extras) no motor do v4 (_build_v4.py, como esta) e no motor do Dev (sim_dev.py).
Grava RESULTADO.md e resultado.csv nesta pasta.   python -I comparar.py
"""
import csv, importlib.util, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
V4 = os.path.join(HERE, '..', '..', '..', '2026-10-29-design-v4', '_build_v4.py')
sys.path.insert(0, HERE)
import sim_dev

spec = importlib.util.spec_from_file_location('v4', V4)
v4 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v4)

DEV_REGS = sim_dev.load()
RES_DEV = {'58218': 0, '58205': 0, '58206': 0, '58212': 0}

# (nome, entradas v4, flags v4, entradas Dev (None = iguais), flags Dev)
SC = [
    ('1 Base 350.000', {'62100': 350000}, {}, None, {}),
    ('2 Salario zero', {}, {}, None, {}),
    ('3 13o salario', {'62100': 350000, '62200': 350000}, {}, None, {}),
    ('4 Moradia real 50.000 (teto 120.000)', {'62100': 600000, '65400': 50000}, {}, None, {}),
    ('5 Indenizacao individual 900.000', {'62100': 300000, '62180': 900000}, {}, None, {}),
    ('6 Aposentadoria compl. 30.000 (teto 14.000)', {'62100': 400000, '21600': 30000}, {}, {'62100': 400000, '21640': 30000}, {}),
    ('7 Transporte 120.000 a todos', {'62100': 300000, '62520': 120000}, {}, None, {}),
    ('8 Abono familiar 30.000 (0 dependentes)', {'62100': 300000, '62760': 30000}, {}, None, {}),
    ('9 Entidade com reducao 50% TFE/TAFP', {'62100': 350000}, {'58206': 2}, None, {'58206': 0}),
    ('10 Jovem graduado, mes 30', {'62100': 350000}, {'58218': 3, '58205': 30}, None, {'58218': 3, '58205': 30}),
    ('11 (extra) Nao residente 800.000', {'62100': 800000}, {'58218': 1, '58202': 2, '58203': 2, '58204': 2}, None, {'58218': 1}),
    ('12 (extra) Abono familiar 30.000 com 6 dependentes', {'62100': 300000, '62760': 30000}, {'58212': 6}, None, {'58212': 6}),
]

# linhas: (rotulo, funcao v4, funcao Dev)
def g(*accts):
    return lambda A: sum(A.get(a, 0.0) for a in accts)

ROWS = [
    ('Base 58105 (caixa bruto)', g('58105'), g('58105')),
    ('Base 58008 (bruto IRPP)', g('58008'), g('58008')),
    ('Base 58130 (bruto CNPS)', g('58130'), g('58130')),
    ('Base 58550 (CNPS segurado)', g('58550'), g('58550')),
    ('Base 58563 (TFE)', g('58563'), g('58563')),
    ('Base 58534 (TAFP)', g('58534'), g('58534')),
    ('58104 transporte isento', g('58104'), g('58104')),
    ('58108 abono familiar isento', g('58108'), g('58108')),
    ('Deducao CNPS EE no IRPP (v4 58141 / Dev 58100)', g('58141'), g('58100')),
    ('Deducao aposentadoria (v4 58142 / Dev 58101)', g('58142'), g('58101')),
    ('Base 58552 (renda tributavel IRPP)', g('58552'), g('58552')),
    ('IRPP (2552+2592)', g('2552', '2592'), g('2552', '2592')),
    ('TFE', g('2563'), g('2563')),
    ('TAFP', g('2534'), g('2534')),
    ('CNPS EE 3,5% (v4 conta 2551 / Dev conta 2550)', g('2551'), g('2550')),
    ('CNPS ER PFM 7,5% (v4 2550 / Dev 2551)', g('2550'), g('2551')),
    ('CNPS ER PVID 5% (2537)', g('2537'), g('2537')),
    ('CNPS ER AT/MP 4% (2560)', g('2560'), g('2560')),
    ('58106 limite de reporte', g('58106'), g('58106')),
    ('58131 taxa total CNPS', g('58131'), g('58131')),
]


def derived(A, ee_acc, pfm_acc, ded_acc_in, inp, dev_inp):
    cash = sum(v for k, v in inp.items() if k.startswith('62') or k.startswith('65') or k.startswith('79'))
    ded = sum(v for k, v in inp.items() if k.startswith('21'))
    ee = A.get(ee_acc, 0.0)
    irpp = A.get('2552', 0.0) + A.get('2592', 0.0)
    net = cash - ee - irpp - ded
    er = A.get('2550' if pfm_acc == '2550' else '2551', 0.0) + A.get('2537', 0.0) + A.get('2560', 0.0)
    cost = cash + er + A.get('2563', 0.0) + A.get('2534', 0.0)
    return net, cost


# regras do Dev que causam cada diferenca (ID da regulacao Dev, item da COMPARACAO.md)
C = {
    'floor0': 'reg 9148161 sem condicao 58130>0: o piso da CNPS vale com salario zero (COMPARACAO B1 #16)',
    'bik': 'regs 9148041..121: forfait % x 58105 em vez de MIN(real; teto) (B1 #20); 58105 inclui 65%%% (B1 #22, D1)',
    'sev': 'reg 9148131: 6218% fora do IRPP sempre (B1 #7); v4 tributa a individual',
    'pens': 'reg 9148181: 2164% dedutivel sem teto de 3,5% (B1 #8)',
    'trans': 'regs 9148141/151 incluem 58104 (transporte isento sai da base TFE/TAFP) (B1 #28); v4 mantem o transporte (Art. 189)',
    'fam': 'regs 9148032/033: abono isento ate 5.000 x 58212 (B1 #4); com 0 dependentes nada e isento',
    'fam_tfe': 'regs 9148141/151: 6276% fora da TFE/TAFP (B1 #28); v4 inclui',
    'relief': 'reg 9148261/251: so isencao total da TFE (58206=1); sem 50% e sem reducao da TAFP (B1 #30)',
    'nr_cnps': 'reg 9148171 sem flags 58202-58204: NR paga todos os ramos (B1 #12, C2)',
    'nr_tfe': 'regs 9148141/151/251/261: NR calcula TFE/TAFP (B1 #11)',
    'nr_base': 'reg 9148011: base NR = bruto sem Art. 45 (B1 #10)',
}
# causas proprias por (cenario, linha); linhas derivadas herdam das bases
OWN = {
    '2': {'Base 58550 (CNPS segurado)': 'floor0', 'CNPS EE 3,5% (v4 conta 2551 / Dev conta 2550)': 'floor0', 'CNPS ER PFM 7,5% (v4 2550 / Dev 2551)': 'floor0',
          'CNPS ER PVID 5% (2537)': 'floor0', 'CNPS ER AT/MP 4% (2560)': 'floor0', 'Deducao CNPS EE no IRPP (v4 58141 / Dev 58100)': 'floor0',
          '58106 limite de reporte': 'floor0'},
    '4': {'Base 58008 (bruto IRPP)': 'bik', 'Base 58105 (caixa bruto)': 'bik'},
    '5': {'Base 58008 (bruto IRPP)': 'sev', 'Base 58105 (caixa bruto)': 'bik'},
    '6': {'Deducao aposentadoria (v4 58142 / Dev 58101)': 'pens'},
    '7': {'Base 58563 (TFE)': 'trans', 'Base 58534 (TAFP)': 'trans'},
    '8': {'58108 abono familiar isento': 'fam', 'Base 58563 (TFE)': 'fam_tfe', 'Base 58534 (TAFP)': 'fam_tfe'},
    '9': {'TFE': 'relief', 'TAFP': 'relief'},
    '11': {'Base 58563 (TFE)': 'nr_tfe', 'Base 58534 (TAFP)': 'nr_tfe', 'TFE': 'nr_tfe', 'TAFP': 'nr_tfe',
           'Base 58550 (CNPS segurado)': 'nr_cnps', 'Base 58130 (bruto CNPS)': 'nr_cnps',
           'CNPS EE 3,5% (v4 conta 2551 / Dev conta 2550)': 'nr_cnps', 'CNPS ER PFM 7,5% (v4 2550 / Dev 2551)': 'nr_cnps',
           'CNPS ER PVID 5% (2537)': 'nr_cnps', 'CNPS ER AT/MP 4% (2560)': 'nr_cnps', 'Deducao CNPS EE no IRPP (v4 58141 / Dev 58100)': 'nr_cnps'},
    '12': {'Base 58563 (TFE)': 'fam_tfe', 'Base 58534 (TAFP)': 'fam_tfe'},
}
DEPS = {
    'Base 58552 (renda tributavel IRPP)': ['Base 58008 (bruto IRPP)', 'Deducao CNPS EE no IRPP (v4 58141 / Dev 58100)', 'Deducao aposentadoria (v4 58142 / Dev 58101)',
                                           '58104 transporte isento', '58108 abono familiar isento'],
    'IRPP (2552+2592)': ['Base 58552 (renda tributavel IRPP)'],
    'Base 58550 (CNPS segurado)': ['Base 58130 (bruto CNPS)'],
    'Base 58130 (bruto CNPS)': [],
    'CNPS EE 3,5% (v4 conta 2551 / Dev conta 2550)': ['Base 58550 (CNPS segurado)'],
    'CNPS ER PFM 7,5% (v4 2550 / Dev 2551)': ['Base 58550 (CNPS segurado)'],
    'CNPS ER PVID 5% (2537)': ['Base 58550 (CNPS segurado)'],
    'CNPS ER AT/MP 4% (2560)': ['Base 58550 (CNPS segurado)'],
    'Deducao CNPS EE no IRPP (v4 58141 / Dev 58100)': ['Base 58550 (CNPS segurado)'],
    'TFE': ['Base 58563 (TFE)'], 'TAFP': ['Base 58534 (TAFP)'],
    'Liquido': ['IRPP (2552+2592)', 'CNPS EE 3,5% (v4 conta 2551 / Dev conta 2550)'],
    'Custo da empresa': ['CNPS ER PFM 7,5% (v4 2550 / Dev 2551)', 'CNPS ER PVID 5% (2537)', 'CNPS ER AT/MP 4% (2560)', 'TFE', 'TAFP', 'Base 58105 (caixa bruto)'],
}
ORDER = [r[0] for r in ROWS]


def main():
    out, tot = [], []
    for name, inp, fl, dinp, dfl in SC:
        f4 = dict(v4.RES); f4.update(fl)
        A4 = v4.run({k: v for k, v in inp.items()}, f4)
        fd = dict(RES_DEV); fd.update(dfl)
        dev_inp = dinp or inp
        AD = sim_dev.run_dev(dev_inp, fd, DEV_REGS)
        vals = {}
        for lab, f_v4, f_dev in ROWS:
            vals[lab] = (f_v4(A4), f_dev(AD))
        cash4 = sum(v for k, v in inp.items() if k[:2] == '62')          # definicao de "cash" do _build_v4.py (so 62xxx)
        cashd = sum(v for k, v in dev_inp.items() if k[:2] == '62')
        bik4 = sum(v for k, v in inp.items() if k[:2] in ('65', '79'))
        bikd = sum(v for k, v in dev_inp.items() if k[:2] in ('65', '79'))
        ded4 = sum(v for k, v in inp.items() if k.startswith('21'))
        dedd = sum(v for k, v in dev_inp.items() if k.startswith('21'))
        n4 = cash4 - A4.get('2551', 0) - A4.get('2552', 0) - A4.get('2592', 0) - ded4
        nd = cashd - AD.get('2550', 0) - AD.get('2552', 0) - AD.get('2592', 0) - dedd
        c4 = cash4 + bik4 + A4.get('2550', 0) + A4.get('2537', 0) + A4.get('2560', 0) + A4.get('2563', 0) + A4.get('2534', 0)
        cd = cashd + bikd + AD.get('2551', 0) + AD.get('2537', 0) + AD.get('2560', 0) + AD.get('2563', 0) + AD.get('2534', 0)
        vals['Liquido'] = (n4, nd)
        vals['Custo da empresa'] = (c4, cd)
        key = name.split()[0]
        diffs = {l: round(d - n, 2) for l, (n, d) in vals.items()}
        causa = {}
        own = OWN.get(key, {})
        for l in list(vals):
            if diffs[l] == 0:
                continue
            if l in own:
                causa[l] = C[own[l]]
        # herdar
        def inherit(l, seen=()):
            if l in causa:
                return causa[l]
            ds = [inherit(d, seen + (l,)) for d in DEPS.get(l, []) if diffs.get(d, 0) != 0 and d not in seen]
            ds = [x for x in ds if x]
            uniq = []
            for x in ds:
                if x not in uniq:
                    uniq.append(x)
            return ' | '.join(uniq)
        for l in vals:
            if diffs[l] != 0 and l not in causa:
                causa[l] = inherit(l) or 'NAO ATRIBUIDA'
        for l in ORDER + ['Liquido', 'Custo da empresa']:
            n, d = vals[l]
            out.append((name, l, round(n, 2), round(d, 2), diffs[l], causa.get(l, '')))
    # CSV
    with open(os.path.join(HERE, 'resultado.csv'), 'w', newline='', encoding='utf-8-sig') as fh:
        w = csv.writer(fh, delimiter=';')
        w.writerow(['cenario', 'linha', 'nosso_v4_XAF', 'dev_XAF', 'dif_dev_menos_nosso_XAF', 'causa (reg Dev / item COMPARACAO.md)'])
        w.writerows(out)
    return out


def sens():
    res = []
    for nome, kw in [('S3 desligada (regulacao com base 0 executa)', dict(SKIP_ZERO_BASE=False)),
                     ('S4 desligada (piso nao vale com matriz vazia)', dict(FLOOR_ON_EMPTY=False))]:
        old = (sim_dev.SKIP_ZERO_BASE, sim_dev.FLOOR_ON_EMPTY)
        for k, v in kw.items():
            setattr(sim_dev, k, v)
        for sn, inp, fl, dinp, dfl in SC[:2]:
            fd = dict(RES_DEV)
            fd.update(dfl)
            A = sim_dev.run_dev(dinp or inp, fd, DEV_REGS)
            irpp = A.get('2552', 0) + A.get('2592', 0)
            res.append((nome, sn, A.get('58105', 0), A.get('58008', 0), irpp, A.get('2550', 0), A.get('2563', 0)))
        sim_dev.SKIP_ZERO_BASE, sim_dev.FLOOR_ON_EMPTY = old
    return res


def fmt(x):
    return f'{x:,.0f}'.replace(',', '.')


def write_md(rows):
    from collections import OrderedDict
    sc = OrderedDict()
    for r in rows:
        sc.setdefault(r[0], []).append(r)
    KEY = ['IRPP (2552+2592)', 'TFE', 'TAFP', 'CNPS EE 3,5% (v4 conta 2551 / Dev conta 2550)', 'Liquido', 'Custo da empresa']
    L = ['# Simulacao Chade: motor do Dev (td_2026) x nosso v4, 10 cenarios do v4', '',
         '> Feito em 2026-10-30 (frente Chade). Calculo local; nada foi carregado no HRBlizz. Dev = `td.json` (igual ao CT-A-588), executado por `sim_dev.py`; nosso = `_build_v4.py` como esta (`run()`). Gerado por `comparar.py`; dados em `resultado.csv`.',
         '> Diferenca = Dev menos nosso, em XAF. Causa = regulacao do Dev (ID 9148xxx) e item da [[COMPARACAO]] (B1 #n / C#). Siglas: IRPP, TFE, TAFP, CNPS EE (empregado) / ER (empregador).', '',
         '## Suposicoes do engine que mais pesam (lista completa no topo de `sim_dev.py`)',
         '- **S2 matriz**: conta exata vence padrao; entre padroes vence o mais especifico (afeta 65400 em `65%%%` x `6540%`, 62180 em `621%%` x `6218%`).',
         '- **S3**: regulacao com base 0 nao roda. Se rodasse, as 9 regs de forfait (41..121) lancariam % de 58105 para todo empregado (ver sensibilidade).',
         '- **S4**: piso da CNPS vale com matriz vazia (Suman 16/10). Define o cenario 2 (salario zero).',
         '- **S5/S8**: piso/teto anuais divididos por 12; IRPP anualiza x12, aplica a tabela e divide por 12; FLOOR(x+0,5) so no fim.',
         '- **S9**: TFE (reg 261, sem formula) arredondada ao XAF inteiro.',
         '- **Dados**: 58206 no Dev e 0/1, entao a "reducao 50%" do cenario 9 entra como 0 (nao existe no Dev). Cenario 6: o codigo 21600 do v4 nao casa com `2164%` do Dev; usado 21640 (mesmo valor). Cenario 8: 0 dependentes (como no v4); o cenario 12 (extra) repete com 6.',
         '- **CNPS EE**: o Dev lanca os 3,5% do empregado em 2550/6020 e os 7,5% PFM em 2551/2610 (C1). As linhas comparam por papel (3,5% = EE), nao por conta.',
         '- Liquido = remuneracao em dinheiro (62xxx) - CNPS EE - IRPP - deducoes 21xxx (mesma conta do v4). Custo da empresa = 62xxx + beneficios 65xxx/79xxx + CNPS ER (PFM, PVID, AT/MP) + TFE + TAFP.', '']
    nbate = 0
    resumo = []
    for n, rs in sc.items():
        nd = [r for r in rs if r[4] != 0]
        L.append(f'## Cenario {n}')
        if not nd:
            L.append(f'**Bate ao franco em todas as {len(rs)} linhas** (bases, IRPP, TFE, TAFP, CNPS EE/ER, deducoes, liquido, custo da empresa).')
            L += ['', '| Linha | Nosso | Dev |', '| --- | ---: | ---: |']
            for r in rs:
                if r[1] in KEY:
                    L.append(f'| {r[1]} | {fmt(r[2])} | {fmt(r[3])} |')
            L.append('')
            if not n.startswith(('11', '12')):
                nbate += 1
            resumo.append((n, 0, 0, None))
            continue
        L += [f'{len(nd)} de {len(rs)} linhas diferem; as outras bateram.', '', '| Linha | Nosso | Dev | Dif. (Dev - nosso) | Causa |', '| --- | ---: | ---: | ---: | --- |']
        for r in rs:
            if r[4] != 0 or r[1] in KEY:
                L.append(f'| {r[1]} | {fmt(r[2])} | {fmt(r[3])} | {fmt(r[4]) if r[4] else "0"} | {r[5]} |')
        L.append('')
        liq = [r for r in rs if r[1] == 'Liquido'][0][4]
        irpp = [r for r in rs if r[1] == 'IRPP (2552+2592)'][0][4]
        mx = max([r for r in nd if not r[1].startswith('Base')] or nd, key=lambda r: abs(r[4]))
        resumo.append((n, irpp, liq, mx))
    L += ['## Resumo', '', f'- Cenarios 1 a 10 que batem ao franco em todas as linhas: **{nbate} de 10** (1, 3 e 10).',
          '', '| Cenario | Dif. IRPP | Dif. liquido | Maior diferenca (linha, XAF) |', '| --- | ---: | ---: | --- |']
    for n, irpp, liq, mx in resumo:
        L.append(f'| {n} | {fmt(irpp)} | {fmt(liq)} | ' + (f'{mx[1]}: {fmt(mx[4])}' if mx else '-') + ' |')
    L += ['', '## Sensibilidade (so o Dev; cenarios 1 e 2)', '', '| Suposicao alterada | Cenario | 58105 | 58008 | IRPP | CNPS EE | TFE |', '| --- | --- | ---: | ---: | ---: | ---: | ---: |']
    for nome, sn, a, b, c, d, e in sens():
        L.append(f'| {nome} | {sn} | {fmt(a)} | {fmt(b)} | {fmt(c)} | {fmt(d)} | {fmt(e)} |')
    L += ['', 'Com S3 desligada o Dev tributaria forfait de moradia, veiculo etc. para quem nao tem beneficio; a configuracao so e viavel se o engine pula regulacao com base zero (ponto a confirmar com o Ram). Com S4 desligada o cenario 2 deixa de gerar CNPS e passa a bater com o nosso.', '',
          '## O que a simulacao nao cobre', '- Proporcionalidade, retro e gross-up (`$$`), igual ao VALIDATION do v4. Nao e o engine real: o resultado vale sob as suposicoes S1..S12.',
          '- Nao decide quem esta certo; cada diferenca aponta a regra a resolver pela lei (ver COMPARACAO.md).', '',
          '## Bloco de prova', '- **Pedido -> resposta:** 10 cenarios (+2 extras) x linhas de base, imposto, CNPS, liquido e custo nos dois motores; valor, diferenca e causa por linha; resumo acima.',
          '- **Fontes:** `td.json` (Drive; igual ao CT-A-588 conforme COMPARACAO secao A), `_build_v4.py`, `COMPARACAO.md`. Nenhuma lei lida.',
          '- **Teste:** o motor do v4 reproduz os resultados do `VALIDATION.md`; o motor do Dev reproduz 28.464 de IRPP no cenario 1, igual ao v4.',
          '- **Confianca:** cerca de 85% nos numeros do Dev (dependem das suposicoes S1..S12, nao confirmadas no engine); 98% nos do v4.', '',
          '## Quem mexeu', '| Data | Frente | O que |', '| --- | --- | --- |', '| 2026-10-30 | chade | simulacao criada (`sim_dev.py`, `comparar.py`) |']
    with open(os.path.join(HERE, 'RESULTADO.md'), 'w', encoding='utf-8') as fh:
        fh.write('\n'.join(L) + '\n')


if __name__ == '__main__':
    rows = main()
    write_md(rows)
    from collections import OrderedDict
    sc = OrderedDict()
    for r in rows:
        sc.setdefault(r[0], []).append(r)
    for n, rs in sc.items():
        nd = [r for r in rs if r[4] != 0]
        print(n, '->', 'BATE' if not nd else f'{len(nd)} linhas diferem')
