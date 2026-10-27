"""ISO 20022 pain.001 reader (shared)."""
from lxml import etree

from framework import num


def _ln(e):
    return etree.QName(e).localname


def _txt(e, path):
    cur = e
    for p in path.split("/"):
        nxt = None
        for c in cur:
            if isinstance(c.tag, str) and _ln(c) == p:
                nxt = c
                break
        if nxt is None:
            return None
        cur = nxt
    return (cur.text or "").strip()


def read_pain001(path):
    t = etree.parse(path)
    r = t.getroot()
    def f(e, name):
        return [x for x in e.iter() if isinstance(x.tag, str) and _ln(x) == name]
    gh = f(r, "GrpHdr")[0]
    res = {"MsgId": _txt(gh, "MsgId"), "NbOfTxs": int(_txt(gh, "NbOfTxs")),
           "CtrlSum": num(_txt(gh, "CtrlSum")), "pmtinf": [], "tx": []}
    for p in f(r, "PmtInf"):
        res["pmtinf"].append({"NbOfTxs": int(_txt(p, "NbOfTxs") or 0), "CtrlSum": num(_txt(p, "CtrlSum")),
                              "ReqdExctnDt": _txt(p, "ReqdExctnDt"), "DbtrIBAN": _txt(p, "DbtrAcct/Id/IBAN"),
                              "Ccy": _txt(p, "DbtrAcct/Ccy"), "Purp": _txt(p, "PmtTpInf/CtgyPurp/Cd")})
        for tx in f(p, "CdtTrfTxInf"):
            acct = _txt(tx, "CdtrAcct/Id/IBAN") or _txt(tx, "CdtrAcct/Id/Othr/Id")
            amt_el = [x for x in tx.iter() if isinstance(x.tag, str) and _ln(x) == "InstdAmt"][0]
            res["tx"].append({"e2e": _txt(tx, "PmtId/EndToEndId"), "amt": num(amt_el.text),
                              "ccy": amt_el.get("Ccy"), "name": _txt(tx, "Cdtr/Nm"), "acct": acct,
                              "ustrd": _txt(tx, "RmtInf/Ustrd")})
    return res


