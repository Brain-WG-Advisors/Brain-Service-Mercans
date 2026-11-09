# -*- coding: utf-8 -*-
"""Row model, flag vocabulary, tax code legend and the registry of the US Wage Type Catalogue.

Columns of the 'Wage Type Catalogue' sheet (CZ V2.0 template columns A-P and S-T kept in meaning; the Q column is expanded
into one column per fund, as the template instructions require for a country with several distinct funds):

 A Mercans Code | B Name EN | C Name local (English: the payslip and filings are in English) | D Explanation |
 E Category | F Formula (engine expression, left empty) | G Tax Code (legend) | H Calculation Type (dev, empty) |
 I Prorating (dev, empty) | J Occurrence | K Ignore If 0 (dev) | L Enforce Setting (dev) | M In Period Reconciliation (dev) |
 N Subject to Tax | O Table Tax | P Special Tax | Q1..Q5 Subject to Social Insurance per fund | R Subject to Pension |
 S YTD Load (dev) | T YTD Remarks (dev) | U..Y US additions (State income tax, Local income tax, Reporting code, Legal basis, Tax code source)
"""
import re

YES, NO, YN, NA = "Yes", "No", "Yes-No", "NA"

# flag name -> header (wtc_columns.flags of the crosswalk)
FLAG_COLS = [
    ("income_tax", "Subject to Tax"),
    ("table_tax", "Table Tax"),
    ("special_tax", "Special Tax"),
    ("oasdi", "Q1 Subject to Social Insurance - OASDI (Social Security tax)"),
    ("medicare", "Q2 Subject to Social Insurance - Medicare and Additional Medicare tax"),
    ("futa", "Q3 Subject to Social Insurance - FUTA (federal unemployment tax)"),
    ("sui", "Q4 Subject to Social Insurance - State unemployment insurance (SUI)"),
    ("state_programmes", "Q5 Subject to Social Insurance - State disability, paid family and medical leave, long-term care programmes"),
    ("pension", "R Subject to Pension (no statutory pension contribution at payroll; OASDI is Q1)"),
    ("state_income_tax", "Subject to State Income Tax"),
    ("local_income_tax", "Subject to Local Income Tax"),
]
FLAG_NAMES = [f for f, _ in FLAG_COLS]
FLAG_HDR = dict(FLAG_COLS)

CATS = ("Earning", "Deduction", "Employer Contribution", "Tax", "Intermediary", "Base", "Flag", "Notional", "Percentage")

# ------------------------------------------------------------------ tax code legend (G) ---
# code -> (meaning, register-id key facts used for its official source, list built in wtc_taxcodes)
TAXCODES = {}


def taxcode(code, meaning, source_keys, note=""):
    TAXCODES[code] = dict(meaning=meaning, source_keys=list(source_keys), note=note)


class Row:
    def __init__(self, code, name, cat, expl, tax_code="US-NA", occ="Recurring", flags=None, basis=None, side="NONE",
                 rep="", payslip=False, in_kind=False, inputs=(), fam="", legal=(), glob=False, sign=None):
        assert cat in CATS, cat
        self.code = code
        self.name = name
        self.cat = cat
        self.expl = expl
        self.tax_code = tax_code
        self.occ = occ
        self.flags = {k: NA for k in FLAG_NAMES}
        for k, v in (flags or {}).items():
            assert k in FLAG_NAMES, k
            assert v in (YES, NO, YN, NA), (code, k, v)
            self.flags[k] = v
        self.basis = dict(basis or {})
        self.side = side
        self.rep = rep
        self.payslip = payslip
        self.in_kind = in_kind
        self.inputs = list(inputs)
        self.fam = fam
        self.legal = list(legal)
        self.glob = glob
        self.sign = sign
        self.spec_rows = []     # filled by the reconciliation

    def __repr__(self):
        return f"<Row {self.code} {self.name}>"


class Registry:
    def __init__(self):
        self.rows = []          # country additions, in definition order
        self.sym = {}           # symbol -> code
        self.n = 0

    def add(self, sym, name, cat, expl, **kw):
        assert sym not in self.sym, sym
        self.n += 1
        code = f"US-{self.n:03d}"
        self.sym[sym] = code
        r = Row(code, name, cat, expl, **kw)
        r.sym = sym
        self.rows.append(r)
        return r


MARK = re.compile(r"\{\{ref:([A-Za-z0-9_]+)\}\}")


def X(sym):
    """Cross reference to a country wage type by symbol; resolved to its code when the catalogue is finalised."""
    return "{{ref:%s}}" % sym


def resolve(text, symmap):
    def sub(m):
        s = m.group(1)
        if s not in symmap:
            raise KeyError(f"unresolved wage type reference {s!r}")
        return symmap[s]
    return MARK.sub(sub, text)
