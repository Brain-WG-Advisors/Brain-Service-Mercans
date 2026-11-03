# -*- coding: utf-8 -*-
"""Engine that executes a Colombia regulation set written in the development team's schema (co_design_v2.json).

Port of the Chad interpreter (Research Pipeline/Chad/2026-11-01-design-v5/simulacao/sim_dev.py, semantics S1-S12), adapted
to Colombia. Every assumption about the production engine is a named switch or rule below; none is confirmed in the
production system (no Colombia regulation set exists there yet: only the draft row 9170132 "CO Income Tax Flat").

S1  Order: regulations run by ascending ordinal; each reads the balance of every account posted so far (inputs, flags,
    WTC-row amounts, 58xxx results of earlier regulations).
S2  Matrix (taxabilityRules): exact account rules only (Colombia has no Mercans codes yet, so no wildcard pattern); isTaxable
    true = in, false or absent = out. Signed sum; the final base is never below 0.
S3  A regulation that has a matrix and whose matrix base is 0 does not execute (SKIP_ZERO_BASE). A regulation without a
    matrix always executes (its formula reads accounts).
S4  Bands: floorAmount / ceilingAmount are not used by this design (limits are written inside the formula, as the Dev does
    inside MIN()).
S5  Flat: $band_amount_raw = base x rate / 100, the rate from employeeRate / employeeRateAccount (employee share) or from
    employerRate / employerRateAccount (employer share), as the development team codes them (one field per band; an account
    holds a percentage computed by an earlier regulation). The engine records which share each band posted (self.share).
S6  Post formula: the posted value is the formula value; $band_amount_raw is available inside it. Taxation type formula:
    $band_amount_raw = base (rate 100) and the value is the formula's.
S7  Posting: debitAccount += value (several regulations may post to the same account, e.g. two illness segments to R327).
    creditAccount 99999 is the clearing account and holds nothing here.
S8  No differential construct: the art. 383 table is a flat lookup written as nested IF() (design Part 4).
S9  Rounding only where a formula rounds (ROUND = half-up to the peso; CEILING(x;n) = smallest multiple of n >= x).
S10 Unknown variables are an error (not 0): every read must be an input / flag, a constant, or posted by an earlier ordinal;
    a WTC wage type (R<row>) not paid in the period reads 0.
S11 Flags and HR fields enter as accounts (582xx, 64992) with the values given by the case.
S12 Assertion false = the regulation does not execute (nothing posted).
S13 Effective-dated constants (52504 hours divisor, 52505 rest-day surcharge) are read at the date carried by the pay line
    (per-line execution of a band that has a unitAccount: one evaluation per hours line of that wage type).
S14 `$<acct>_ytd` = sum of <acct> over the prior periods of the same calendar year (the run keeps the history).
S15 `$<acct>_raw` = sum of the $band_amount_raw of the regulations that posted <acct> (before the post formula).
S16 Decimal arithmetic, 40 significant digits.
S17 Bands of one regulation run in their order. This design never lets a band read the account of another band of its own
    regulation (the employer share is written from the base), so it does not depend on that order.
S18 Deduction wage types carry negative amounts (signed sum of S2), as the development team's negative accounts.
"""
import re, json
from decimal import Decimal as Dc, ROUND_HALF_UP, getcontext
getcontext().prec = 40

SKIP_ZERO_BASE = True   # S3


def D(x):
    return x if isinstance(x, Dc) else Dc(str(x))


# ------------------------------------------------------------------ expression language (Dev functions)
TOK = re.compile(r'\s*(?:(\$[A-Za-z0-9_]+)|([A-Z_]+)\(|(-?\d+(?:\.\d+)?)|(;)|(\)))')


def parse(expr):
    pos = 0; toks = []
    while pos < len(expr):
        m = TOK.match(expr, pos)
        if not m:
            raise SyntaxError(f'cannot parse at {pos}: {expr[pos:pos+40]!r}')
        pos = m.end()
        v, f, n, sc, cp = m.groups()
        if v: toks.append(('var', v[1:]))
        elif f: toks.append(('fn', f))
        elif n: toks.append(('num', n))
        elif sc: toks.append((';', None))
        elif cp: toks.append((')', None))
    i = 0

    def node():
        nonlocal i
        t, v = toks[i]; i += 1
        if t == 'num': return ('num', D(v))
        if t == 'var': return ('var', v)
        if t == 'fn':
            args = []
            if toks[i][0] == ')':
                i += 1; return ('fn', v, args)
            while True:
                args.append(node())
                t2 = toks[i][0]; i += 1
                if t2 == ')': break
                assert t2 == ';', expr
            return ('fn', v, args)
        raise SyntaxError(expr)
    tree = node()
    assert i == len(toks), f'trailing tokens in {expr!r}'
    return tree


def variables(expr):
    return set(re.findall(r'\$([A-Za-z0-9_]+)', expr or ''))


def ceiling(x, n):
    n = D(n)
    q = (x / n).to_integral_value(rounding='ROUND_CEILING')
    return q * n


def ev(tree, get):
    k = tree[0]
    if k == 'num': return tree[1]
    if k == 'var': return get(tree[1])
    f, a = tree[1], tree[2]
    E = lambda j: ev(a[j], get)
    if f == 'IF': return E(1) if E(0) else E(2)
    if f == 'AND': return Dc(1) if all(ev(x, get) for x in a) else Dc(0)
    if f == 'OR': return Dc(1) if any(ev(x, get) for x in a) else Dc(0)
    if f == 'NOT': return Dc(0) if E(0) else Dc(1)
    vals = [ev(x, get) for x in a]
    if f == 'ADD': return sum(vals, Dc(0))
    if f == 'SUBTRACT': return vals[0] - vals[1]
    if f == 'MULTIPLY':
        r = Dc(1)
        for x in vals: r *= x
        return r
    if f == 'DIVIDE': return Dc(0) if vals[1] == 0 else vals[0] / vals[1]
    if f == 'MIN': return min(vals)
    if f == 'MAX': return max(vals)
    if f == 'EQUALS': return Dc(1) if vals[0] == vals[1] else Dc(0)
    if f == 'LESS': return Dc(1) if vals[0] < vals[1] else Dc(0)
    if f == 'GREATER': return Dc(1) if vals[0] > vals[1] else Dc(0)
    if f == 'LTE': return Dc(1) if vals[0] <= vals[1] else Dc(0)
    if f == 'GTE': return Dc(1) if vals[0] >= vals[1] else Dc(0)
    if f == 'ROUND': return vals[0].quantize(Dc('1'), rounding=ROUND_HALF_UP)
    if f == 'CEILING': return ceiling(vals[0], vals[1] if len(vals) > 1 else 1)
    if f == 'FLOOR': return vals[0].to_integral_value(rounding='ROUND_FLOOR')
    raise NameError(f)


_CACHE = {}


def evaluate(expr, get):
    if expr not in _CACHE: _CACHE[expr] = parse(expr)
    return ev(_CACHE[expr], get)


# ------------------------------------------------------------------ run
class Run:
    def __init__(self, design, consts, inputs, lines=(), history=None, period='2026-03'):
        self.design = sorted(design['regulations'], key=lambda r: r['ordinal'])
        self.consts = consts           # {acct: value or [(from, value), ...]}
        self.A = {k: D(v) for k, v in inputs.items()}
        self.raw = {}
        self.lines = list(lines)       # [{'unit': 'H306', 'hours': 10, 'date': '2026-07-14'}]
        self.hist = history or {}      # {acct: sum of prior periods}
        self.period = period
        self.trace = {}                # regulation name -> (raw, value) when executed
        self.posted_by = {}
        self.share = {}                # debit account -> 'EE' | 'ER' (flat bands)
        # accounts a regulation of the set can post: read as 0 while not posted (regulation skipped by S3 / S12)
        self.outputs = {b['debitAccount'] for r in self.design for b in r['bands']}

    def const_at(self, acct, date):
        v = self.consts[acct]
        if isinstance(v, list):
            val = None
            for frm, x in v:
                if frm <= date: val = x
            return D(val)
        return D(v)

    def getter(self, extra=None, date=None):
        def get(name):
            if extra and name in extra: return extra[name]
            if name.endswith('_ytd'): return D(self.hist.get(name[:-4], 0))
            if name.endswith('_raw'):
                base = name[:-4]
                if base in self.raw: return self.raw[base]
                if base in self.outputs: return Dc(0)
                raise NameError(f'{name}: {base} is not posted by any regulation')
            if name in self.consts: return self.const_at(name, date or (self.period + '-15'))
            if name in self.A: return self.A[name]
            if name in self.outputs: return Dc(0)
            if re.fullmatch(r'R\d+', name): return Dc(0)          # S10: a WTC wage type not paid this period
            raise NameError(f'unknown variable ${name}')
        return get

    def matrix_base(self, rules):
        tot = Dc(0)
        for r in rules:
            if r['isTaxable'] and r['account'] in self.A:
                tot += self.A[r['account']]
        return max(tot, Dc(0))

    def post(self, acct, value, raw, rid):
        self.A[acct] = self.A.get(acct, Dc(0)) + value
        self.raw[acct] = self.raw.get(acct, Dc(0)) + raw
        self.posted_by.setdefault(acct, []).append(rid)

    def go(self):
        for r in self.design:
            g = self.getter()
            if r.get('assertion') and not evaluate(r['assertion'], g):
                continue
            rules = r.get('taxabilityRules') or []
            base = self.matrix_base(rules) if rules else Dc(0)
            if rules and SKIP_ZERO_BASE and base == 0:
                continue
            for b in r['bands']:
                if b.get('assertion') and not evaluate(b['assertion'], self.getter()):
                    continue
                if b.get('unitAccount'):            # S13 per-line execution
                    tot = Dc(0)
                    for ln in self.lines:
                        if ln['unit'] != b['unitAccount']: continue
                        gl = self.getter({'hours': D(ln['hours'])}, ln['date'])
                        tot += evaluate(b['formula'], gl)
                    if tot: self.post(b['debitAccount'], tot, tot, r.get('regulationId', r.get('id')))
                    continue
                if r['taxationType'] == 'flat':
                    g = self.getter()
                    if b.get('employeeRate') is not None: rate, sh = D(b['employeeRate']), 'EE'
                    elif b.get('employeeRateAccount'): rate, sh = g(b['employeeRateAccount']), 'EE'
                    elif b.get('employerRate') is not None: rate, sh = D(b['employerRate']), 'ER'
                    elif b.get('employerRateAccount'): rate, sh = g(b['employerRateAccount']), 'ER'
                    else: raise ValueError(f"{r['name']}: flat band without a rate")
                    raw = base * rate / 100
                    self.share[b['debitAccount']] = sh
                else:
                    raw = base
                g = self.getter()
                val = evaluate(b['formula'], self.getter({'band_amount_raw': raw})) if b.get('formula') else raw
                self.post(b['debitAccount'], val, raw, r.get('regulationId', r.get('id')))
                self.trace[r['name']] = (raw, val)
        return self


def run_year(design, consts, months, upto):
    """months: {m: (inputs, lines)} for m = 1..upto; returns the Run of month `upto` with the year-to-date history (S14)."""
    hist = {}
    for m in range(1, upto + 1):
        inp, lines = months[m]
        r = Run(design, consts, inp, lines, history=dict(hist), period=f'2026-{m:02d}').go()
        for k, v in r.A.items():
            if k[:1] == '5' and k not in inp:
                hist[k] = hist.get(k, Dc(0)) + v
    return r
