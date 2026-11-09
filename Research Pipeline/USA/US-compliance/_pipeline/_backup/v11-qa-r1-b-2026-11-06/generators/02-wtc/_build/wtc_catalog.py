# -*- coding: utf-8 -*-
"""Assembly of the catalogue: federal and State rows (registry, codes US-nnn), the 300 global rows, the tax code legend."""
import wtc_common as W
import wtc_gaps as G
import wtc_model as M
import wtc_fed as F
import wtc_fed2 as F2
import wtc_states as S
import wtc_states2 as S2
import wtc_global_rows as GR
import wtc_taxcodes as T


def assemble():
    G.define()
    reg = M.Registry()
    F.add_federal(reg)
    F2.add_federal2(reg)
    S.build_states(reg)
    S2.build_states2(reg)
    grows = GR.build_rows()
    T.define()
    symmap = dict(reg.sym)
    for r in grows:
        symmap[r.sym] = r.code
    allrows = grows + reg.rows
    for r in allrows:
        r.expl = M.resolve(r.expl, symmap)
        r.name = M.resolve(r.name, symmap)
    # keep only symbols that exist: every reference resolved above or the build stops
    return grows, reg.rows, allrows, symmap
