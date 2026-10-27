"""Shared evidence collector (same checks.json shape as Netherlands/_tool):
checks: id, area, check, population, result (Pass/Finding/Not tested/Out of scope), detail
recon:  item, a_src, a, b_src, b, diff, result
not_tested: id, item, reason, unblock
recalc: list of dict rows (per employee)"""
import json
import os

TOL = 0.005


class Evidence:
    def __init__(self, client):
        self.d = {"client": client, "checks": [], "recon": [], "not_tested": [],
                  "recalc": [], "recalc_header": [], "notes": [], "exceptions": []}

    def check(self, cid, area, text, population, ok, detail="", result=None):
        r = result or ("Pass" if ok else "Finding")
        self.d["checks"].append({"id": cid, "area": area, "check": text,
                                 "population": population, "result": r,
                                 "detail": detail})
        return ok

    def exc(self, cid, key, msg):
        """Per-record exception that made a check fail (for review)."""
        self.d["exceptions"].append({"id": cid, "key": key, "msg": msg})

    def recon(self, item, a_src, a, b_src, b, tol=0.01, explained=None):
        diff = round((a or 0) - (b or 0), 2)
        res = "Pass" if abs(diff) <= tol else (explained or "Difference")
        self.d["recon"].append({"item": item, "a_src": a_src, "a": a, "b_src": b_src,
                                "b": b, "diff": diff, "result": res})
        return abs(diff) <= tol

    def nt(self, nid, item, reason, unblock):
        self.d["not_tested"].append({"id": nid, "item": item, "reason": reason,
                                     "unblock": unblock})

    def note(self, s):
        self.d["notes"].append(s)

    def save(self, val_dir):
        ev = os.path.join(val_dir, "_evidence")
        os.makedirs(ev, exist_ok=True)
        with open(os.path.join(ev, "checks.json"), "w", encoding="utf-8") as f:
            json.dump(self.d, f, ensure_ascii=False, indent=1, default=str)
        res = {}
        for c in self.d["checks"]:
            res[c["result"]] = res.get(c["result"], 0) + 1
        print("checks:", len(self.d["checks"]), res)
        for c in self.d["checks"]:
            if c["result"] != "Pass":
                print(f"  {c['id']} [{c['result']}] {c['check']} :: {c['detail'][:300]}")
        for r in self.d["recon"]:
            if r["result"] != "Pass":
                print(f"  RECON {r['item']}: {r['a']} vs {r['b']} diff {r['diff']}")


def eq(a, b, tol=TOL):
    try:
        return abs(float(a) - float(b)) <= tol
    except (TypeError, ValueError):
        return False


def num(s):
    """Parse '1,234.56' / '1.234,56' / '-' / '' to float or None."""
    if s is None:
        return None
    if isinstance(s, (int, float)):
        return float(s)
    s = str(s).strip().replace(" ", "").replace(" ", "")
    if s in ("", "-", "nan", "None"):
        return None
    neg = s.startswith("-") or (s.startswith("(") and s.endswith(")"))
    s = s.strip("-()")
    if "," in s and "." in s:
        if s.rfind(",") > s.rfind("."):
            s = s.replace(".", "").replace(",", ".")
        else:
            s = s.replace(",", "")
    elif "," in s:
        parts = s.split(",")
        s = s.replace(",", ".") if len(parts[-1]) in (1, 2) and len(parts) == 2 else s.replace(",", "")
    try:
        v = float(s)
    except ValueError:
        return None
    return -v if neg else v
