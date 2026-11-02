"""Motor do Dev (td_2026, Chade) executado a partir do td.json / CT-A-588.

Uso:  python -I sim_dev.py [caminho/td.json]     (sem argumento: roda um cenario de teste)
      from sim_dev import run_dev                 (usado por comparar.py)

SUPOSICOES SOBRE A SEMANTICA DO ENGINE (nao confirmadas no HRBlizz; o System Settings deu erro 526).
Cada uma e um interruptor ou regra no codigo, para testar a sensibilidade.

S1  Ordem: regulacoes executam pelo ordinal crescente; cada uma le o saldo das contas ate ali
    (entradas do holerite + contas 58xxx/25xx/26xx postadas por regulacoes anteriores).
S2  Matriz (taxability): conta exata (pattern nulo) vence padrao; entre padroes vence o mais
    especifico (mais caracteres nao-%). '%' = um digito qualquer, o padrao tem o mesmo tamanho do
    codigo. Conta sem regra = fora. Soma com sinal (conta negativa reduz); base final nunca < 0.
S3  Regulacao cuja base da matriz e 0 nao executa (SKIP_ZERO_BASE=True). Excecao S4.
S4  Piso (floorAmount) vale mesmo com matriz vazia (FLOOR_ON_EMPTY=True), conforme Suman 16/10
    (CONFERENCIA v4: "com a matriz vazia o piso ainda se aplica"). Afeta regs 9 e 161.
S5  Faixa flat: valor = base x taxa/100 (employeeRate ou employerRate); piso/teto sao ANUAIS e
    divididos por period_divisor, exceto em grupos '*_monthly' (valor ja mensal). period_divisor = 12.
S6  Formula roda depois de piso/teto; $band_amount_raw = valor apos piso/teto. A formula pode ignorar
    o raw (ex.: MULTIPLY($58105;0.20)): o valor e o da formula (forfait).
S7  Lancamento: credito 99999/99998 -> debito += valor (conta de base); debito 99999 -> credito -= valor
    (conta negativa); senao conta de credito += valor (passivo/imposto). Contas de despesa (6xxx, 2610)
    nao acumulam saldo aqui.
S8  Diferencial (reg 211, 'monthly'): faixas anuais sobre a base ja anualizada (reg 201 x period_divisor);
    imposto = soma de (min(renda; incomeTo) - incomeTo da faixa anterior) x taxa; a divisao pelo periodo
    fica na reg 221, sem arredondamento intermediario.
S9  Arredondamento: so as formulas do design arredondam (FLOOR(x+0,5) etc.). Valor sem formula lancado em
    conta de passivo (ex.: TFE reg 261) e arredondado ao XAF inteiro, meia-para-cima (XAF sem subunidade).
S10 Taxation type 'formula' (reg 32): o valor e o da formula, nao base x taxa (consequencia de S6).
S11 Flags (58218, 58205, 58206, 58212) entram como contas com o valor dado; 58206 no Dev e 0/1
    (tfe_holiday_flag). Gross-up ($$) nao e usado nestes cenarios.
S12 Pre-condicao falsa = regulacao nao executa. Variaveis desconhecidas valem 0.
"""
import json, math, re, sys

SKIP_ZERO_BASE = True      # S3
FLOOR_ON_EMPTY = True      # S4
PERIOD_DIVISOR = 12        # S5
TD_JSON = r'G:\Drives compartilhados\Compliance Team\Country Folders\Chad\07-design\td.json'


def load(path=TD_JSON):
    with open(path, encoding='utf8') as fh:
        d = json.load(fh)
    return sorted(d['regulations'], key=lambda r: r['ordinal'])


def pat_match(code, pat):
    return len(code) == len(pat) and all(p == '%' or p == c for p, c in zip(pat, code))


def matrix_sum(rules, A):
    tot = 0.0
    for code, v in A.items():
        if not v or not code.isdigit():
            continue
        best = None
        for m in rules:
            if m['pattern']:
                if not pat_match(code, m['pattern']):
                    continue
                spec = sum(1 for ch in m['pattern'] if ch != '%')
            else:
                if m['account'] != code:
                    continue
                spec = 99
            if best is None or spec > best[0]:
                best = (spec, m['isTaxable'])
        if best and best[1]:
            tot += v
    return max(tot, 0.0)


def ev(expr, A, raw=None):
    e = expr.replace('$band_amount_raw', repr(raw if raw is not None else 0.0))
    e = e.replace('$period_divisor', repr(float(PERIOD_DIVISOR)))
    e = re.sub(r'\$(\d{4,5})', lambda m: repr(float(A.get(m.group(1), 0.0))), e)
    e = e.replace(';', ',')
    env = dict(FLOOR=math.floor, ADD=lambda a, b: a + b, MULTIPLY=lambda a, b: a * b, DIVIDE=lambda a, b: a / b,
               MIN=min, MAX=max, EQUALS=lambda a, b: a == b, LESS=lambda a, b: a < b, GREATER=lambda a, b: a > b,
               NOT=lambda a: not a, AND=lambda *a: all(a), OR=lambda *a: any(a), IF=lambda c, a, b: a if c else b)
    return eval(e, {'__builtins__': {}}, env)


def half_up(x):
    return math.floor(x + 0.5)


def run_dev(inputs, flags, regs=None, log=None):
    """inputs: {conta: valor}; flags: {'58218':..,'58205':..,'58206':..,'58212':..}. Devolve saldo por conta."""
    regs = regs or load()
    A = {k: float(v) for k, v in inputs.items()}
    A.update({k: float(v) for k, v in flags.items()})
    for r in regs:
        pre = r.get('assertion') or ''
        if pre and not ev(pre, A):
            continue
        base = matrix_sum(r['taxabilityRules'], A)
        has_floor = any(b['floorAmount'] is not None for b in r['bands'])
        if base == 0 and SKIP_ZERO_BASE and not (has_floor and FLOOR_ON_EMPTY):
            continue
        div = 1.0 if '_monthly' in r['taxRuleGroup'] else float(PERIOD_DIVISOR)
        if r['taxationType'] == 'differential':
            tot, prev = 0.0, 0.0
            for b in sorted(r['bands'], key=lambda b: b['incomeFrom']):
                hi = b['incomeTo']
                if base > prev:
                    tot += (min(base, hi) - prev) * (b['employeeRate'] or 0) / 100
                prev = hi
            d = r['bands'][0]['debitAccount']
            A[d] = A.get(d, 0.0) + tot
            continue
        for b in r['bands']:
            if b.get('assertion') and not ev(b['assertion'], A):
                continue
            rate = b['employeeRate'] if b['employeeRate'] is not None else (b['employerRate'] or 0)
            amt = base * rate / 100
            if b['floorAmount'] is not None:
                amt = max(amt, b['floorAmount'] / div)
            if b['ceilingAmount'] is not None:
                amt = min(amt, b['ceilingAmount'] / div)
            if b['formula']:
                amt = ev(b['formula'], A, amt)
            deb, cred = b['debitAccount'], b['creditAccount']
            if cred in ('99999', '99998'):
                A[deb] = A.get(deb, 0.0) + amt
            elif deb == '99999':
                A[cred] = A.get(cred, 0.0) - amt
            else:
                if not b['formula']:
                    amt = half_up(amt)           # S9
                A[cred] = A.get(cred, 0.0) + amt
            if log is not None:
                log.append((r['ordinal'], r['name'], rate, round(base, 2), round(amt, 2), deb, cred))
    return A


if __name__ == '__main__':
    path = sys.argv[1] if len(sys.argv) > 1 else TD_JSON
    regs = load(path)
    lg = []
    A = run_dev({'62100': 350000}, {'58218': 0, '58205': 0, '58206': 0, '58212': 0}, regs, lg)
    for l in lg:
        print(l)
    print({k: round(v, 2) for k, v in A.items() if k.startswith(('58', '25', '26'))})
