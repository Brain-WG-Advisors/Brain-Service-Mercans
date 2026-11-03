# -*- coding: utf-8 -*-
"""Exact-substring patch helper used during the round-2 rebuild (line endings preserved)."""


def patch(path, pairs, count_check=True):
    raw = open(path, encoding="utf-8", newline="").read()
    crlf = raw.count("\r\n") > raw.count("\n") / 2
    t = raw.replace("\r\n", "\n")
    for a, b in pairs:
        if a not in t:
            raise AssertionError(f"{path}: not found: {a[:120]!r}")
        if count_check and t.count(a) != 1:
            raise AssertionError(f"{path}: {t.count(a)} occurrences of {a[:80]!r}")
        t = t.replace(a, b)
    if crlf:
        t = t.replace("\n", "\r\n")
    open(path, "w", encoding="utf-8", newline="").write(t)
