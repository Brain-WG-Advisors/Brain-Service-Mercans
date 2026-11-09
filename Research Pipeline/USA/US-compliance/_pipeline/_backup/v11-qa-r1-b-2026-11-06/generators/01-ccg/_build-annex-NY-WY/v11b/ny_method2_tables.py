# -*- coding: utf-8 -*-
"""v1.1 build 2 (2026-11-06): write the NYS and NYC Method II per-period tables into src/NY.md (section @income_tax).

Replaces the NYS Method II bullet + annual tables and the NYC Method II bullet + annual table with: the method
fact, an allowance table per payroll period (weekly, biweekly, semimonthly, monthly, daily, annual), one rate table
per payroll period (Tables II-A..II-E, letter read from each fact's note) and the annual schedule for annual payrolls.
Every figure is a {{key}} placeholder (bound to CCG-annex_NY-facts.json by build.py). Idempotent: the block is found
between its bullet heading and the next bullet that is not part of it.
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "src", "NY.md")
BASE = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
F = {f["key"]: f for f in json.load(open(os.path.join(BASE, "_research", "CCG-annex_NY-facts.json"), encoding="utf-8"))["facts"]}
FREQS = ["weekly", "biweekly", "semimonthly", "monthly", "daily"]


def nlines(pre, st, fr):
    return max(int(k.split(".")[-2]) for k in F if k.startswith(f"{pre}.{st}.{fr}.bracket.") and k.endswith(".floor"))


def letter(pre, fr):
    m = re.search(r"Table II - ([A-E])", F[f"{pre}.single.{fr}.bracket.1.rate"]["note"])
    if not m:
        raise SystemExit(f"no table letter in note of {pre}.single.{fr}.bracket.1.rate")
    return m.group(1)


def cells(pre, st, fr, i):
    k = f"{pre}.{st}.{fr}.bracket.{i}" if fr else f"{pre}.{st}.bracket.{i}"
    if f"{k}.floor" not in F:
        return ["-", "-", "-"]
    return [f"USD {{{{{k}.floor}}}}", f"{{{{{k}.rate}}}} %", f"USD {{{{{k}.base}}}}"]


def allowances(pre, label):
    L = [f"**{label} Method II allowances by payroll period**", "",
         "| Payroll period | Deduction allowance, single | Deduction allowance, married | Value of one exemption, single | Value of one exemption, married |",
         "|---|---|---|---|---|"]
    for fr in FREQS:
        L.append(f"| {fr.capitalize()} | USD {{{{{pre}.single.{fr}.deduction_allowance}}}} | USD {{{{{pre}.married.{fr}.deduction_allowance}}}} "
                 f"| USD {{{{{pre}.single.{fr}.exemption_allowance}}}} | USD {{{{{pre}.married.{fr}.exemption_allowance}}}} |")
    L.append(f"| Annual | USD {{{{{pre}.single.deduction_allowance}}}} | USD {{{{{pre}.married.deduction_allowance}}}} "
             f"| USD {{{{{pre}.exemption_allowance}}}} | USD {{{{{pre}.exemption_allowance}}}} |")
    return L + [""]


def rate_table(pre, label, fr):
    title = (f"**{label} Method II, {fr} payroll (Table II-{letter(pre, fr)})**" if fr
             else f"**{label} Method II annual schedule (annual payrolls)**")
    n = max(nlines(pre, st, fr) if fr else max(int(k.split(".")[-2]) for k in F
            if k.startswith(f"{pre}.{st}.bracket.") and k.endswith(".floor")) for st in ("single", "married"))
    L = [title, "", "| Line | Single: net wages at least | Single: rate | Single: add | Married: net wages at least | Married: rate | Married: add |",
         "|---|---|---|---|---|---|---|"]
    for i in range(1, n + 1):
        L.append("| " + " | ".join([str(i)] + cells(pre, "single", fr, i) + cells(pre, "married", fr, i)) + " |")
    return L + [""]


def block(pre, label, head):
    L = [head, ""] + allowances(pre, label)
    for fr in FREQS:
        L += rate_table(pre, label, fr)
    L += rate_table(pre, label, None)
    return L


NYS_HEAD = ("- **Method II exact calculation, New York State [US-NYV7-001].** {{ny.wh.method2.annualisation}} The payroll applies the "
            "allowance amounts and the rate table of the employee's own payroll period, as printed in the publication (allowance "
            "tables and rate Tables II-A to II-E); the annual amounts and the annual schedule apply only to annual payrolls. "
            "Allowance for the period = deduction allowance of the status plus the value of one exemption for each exemption "
            "claimed; amount to withhold = (net wages - column 3) x column 4 + column 5 on the line where the net "
            "wages fall. Quarterly and semiannual payrolls have no Method II table in the publication and are not derived "
            "(documented limitation, open point below).")
NYC_HEAD = ("- **New York City resident withholding, Method II [US-NYV7-002].** {{ny.local.nyc.method2.annualisation}} The NYC "
            "allowance amounts and rate table of the employee's own payroll period apply (NYS-50-T-NYC allowance tables and rate "
            "Tables II-A to II-E); the annual amounts and the annual schedule apply only to annual payrolls. Same formula as New York State.")

src = open(SRC, encoding="utf-8").read()
lines = src.split("\n")


def replace(lines, start_pat, stop_pat, new):
    s = next(i for i, l in enumerate(lines) if l.startswith(start_pat))
    e = next(i for i in range(s + 1, len(lines)) if lines[i].startswith(stop_pat))
    return lines[:s] + new + lines[e:]


lines = replace(lines, "- **Method II exact calculation, New York State", "- **Method III, top income", block("ny.wh.method2", "NYS", NYS_HEAD))
lines = replace(lines, "- **New York City resident withholding, Method II", "- **Yonkers resident surcharge", block("ny.local.nyc.method2", "NYC", NYC_HEAD))
out = "\n".join(lines)
used = set(re.findall(r"\{\{([a-z0-9_.]+)\}\}", out))
missing = sorted(k for k in used if k not in F)
if missing:
    raise SystemExit(f"placeholders without a fact: {missing}")
m2 = {k for k in F if ".method2." in k and k.startswith(("ny.wh.method2", "ny.local.nyc.method2"))}
print(f"method2 keys in facts: {len(m2)}; placeholders bound in NY.md: {len(m2 & used)}; not in narrative: {sorted(m2 - used)}")
open(SRC, "w", encoding="utf-8", newline="\n").write(out)
