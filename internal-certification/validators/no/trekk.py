"""Skatteetaten trekktabeller 2026 (text format: table 4 | period 1 | type 1 | grunnlag 6 | trekk 6).
Lookup rule used: the row with the highest trekkgrunnlag <= the amount (table rows are interval starts)."""
import bisect
import zipfile

ZIP = r"C:\Users\instituto\Documents\internal-certification\references\Norway\2026\trekktabeller_2026_alle.zip"
_cache = {}


def load(tables, period="1"):
    want = {str(t) for t in tables} - set(_cache)
    if want:
        with zipfile.ZipFile(ZIP) as z:
            name = z.namelist()[0]
            with z.open(name) as f:
                for raw in f:
                    s = raw.decode("ascii").strip()
                    if len(s) != 18 or s[:4] not in want or s[4] != period or s[5] != "0":
                        continue
                    _cache.setdefault(s[:4], []).append((int(s[6:12]), int(s[12:18])))
        for t in want:
            _cache.setdefault(t, []).sort()
    return {str(t): _cache.get(str(t), []) for t in tables}


def lookup(table, amount):
    rows = load([table])[str(table)]
    if not rows:
        return None, None
    keys = [r[0] for r in rows]
    i = bisect.bisect_right(keys, int(amount)) - 1
    if i < 0:
        return 0, None
    return rows[i][1], rows[i][0]


def max_row(table):
    rows = load([table])[str(table)]
    return rows[-1] if rows else None
