# -*- coding: utf-8 -*-
"""Round 2 (QA r1 finding 55): IL-700-T example 1 labelled as the table method; the automated-method
result is compared with the new fact il.oracle.il700t.example1.automated_method_result (agent 2,
2026-11-02). Idempotent. usage: python r2_patch_il.py"""
import os

P = os.path.join(os.path.dirname(os.path.abspath(__file__)), "build_examples_annex_DC-MA.py")
t = open(P, encoding="utf-8", newline="").read()
old_head = 'L += ["**Example IL-1: weekly wages 300.00, IL-W-4 Line 1 = 2, Line 2 = 1 (IL-700-T example).**", ""]'
new_head = ('L += ["**Example IL-1: weekly wages 300.00, IL-W-4 Line 1 = 2, Line 2 = 1 (IL-700-T example 1, '
            'automated payroll method; the booklet prints the table-method result).**", ""]')
old_tail = t[t.index("if res1 != o1:"):t.index('write("IL", L)')]
new_tail = (
    'o1a = D(str(f.get("il.oracle.il700t.example1.automated_method_result")))\n'
    'RESULTS.append(("IL", "IL-1 automated", str(res1), str(o1a), res1 == o1a))\n'
    'assert res1 == o1a, (res1, o1a)\n'
    'L += ["", f"Result {m(res1)} = published automated-method result '
    '[[FACT:il.oracle.il700t.example1.automated_method_result={m(o1a)}]] (match). The IL-700-T prints '
    '[[FACT:il.oracle.il700t.example1.withholding=8.38]] for the same employee because its example uses the '
    'wage-bracket table, whose values are computed at the bracket midpoint; both are correct for their method. '
    'A payroll engine using the formula reproduces the automated-method result.", ""]\n'
)
if old_head in t:
    t = t.replace(old_head, new_head)
if "automated_method_result" not in t:
    t = t.replace(old_tail, new_tail)
open(P, "w", encoding="utf-8", newline="").write(t)
print("ok")
