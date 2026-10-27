# -*- coding: utf-8 -*-
"""Shared helpers for the CO v1.1 DD<->spec alignment patch."""
import ast
import re
import textwrap

RUN = re.compile(r'"(?:[^"\\]|\\.)*"(?:\s*\n\s*"(?:[^"\\]|\\.)*")*')

BS = chr(92)
QT = chr(34)


def emit(value, indent, width=98):
    """Re-emit a python str as an indented run of adjacent string literals."""
    pad = " " * indent
    body = width - indent
    if body < 30:
        body = 30
    lines = textwrap.wrap(value, width=body, break_long_words=False,
                          break_on_hyphens=False)
    if not lines:
        return QT + QT
    out = []
    for i, ln in enumerate(lines):
        if i < len(lines) - 1:
            ln = ln + " "
        ln = ln.replace(BS, BS + BS).replace(QT, BS + QT)
        out.append(QT + ln + QT)
    return ("\n" + pad).join(out)


def replace_literal(src, predicate, transform):
    """For every adjacent-string-literal run whose value satisfies predicate,
    rewrite it with transform(value). Returns (newsrc, n_changed)."""
    n = 0
    out = []
    pos = 0
    for m in RUN.finditer(src):
        if m.start() < pos:
            continue
        try:
            val = ast.literal_eval("(" + m.group(0) + ")")
        except Exception:
            continue
        if not isinstance(val, str) or not predicate(val):
            continue
        new = transform(val)
        if new == val:
            continue
        line_start = src.rfind("\n", 0, m.start()) + 1
        indent = m.start() - line_start
        out.append(src[pos:m.start()])
        out.append(emit(new, indent))
        pos = m.end()
        n += 1
    out.append(src[pos:])
    return "".join(out), n
