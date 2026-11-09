# -*- coding: utf-8 -*-
"""Federal tax profiles of the earning and deduction families: flag values, their register basis and the parameter text
that sits on the ANCHOR row of a family (followers point to the anchor and carry no figure, so no tagged figure is
repeated as boilerplate).

Flag semantics (stated once on the coverage sheet): for an earning row, Yes means the amount is wages for that tax
(enters its base), No means it is excluded from the base, Yes-No means conditional (column D says on what); for a
deduction row the flag describes the treatment of the amount deducted (No = removed from the base before the tax);
tax and contribution rows carry NA (their own amount is not a base).
"""
import wtc_common as W
from wtc_model import YES, NO, YN, NA

val, line, rid = W.val, W.line, W.rid


def B():
    """Register basis of each flag family (one register id each, from the facts that define the tax)."""
    return dict(
        income_tax=rid("fed.fit.method"), table_tax=rid("fed.fit.method"), special_tax=rid("fed.fit.supplemental.flat_rate"),
        oasdi=rid("fed.fica.oasdi.wage_base"), medicare=rid("fed.fica.medicare.rate.employee"),
        futa=rid("fed.futa.wage_base"), sui=rid("multi.sui.localization_test"), state_programmes=rid("multi.sui.localization_test"),
        pension=rid("fed.fica.oasdi.wage_base"), state_income_tax=rid("multi.no_wage_income_tax.states"),
        local_income_tax=rid("multi.no_wage_income_tax.states"))


# ------------------------------------------------------------------------------ flags ---
def flags_reg():
    return dict(income_tax=YES, table_tax=YES, special_tax=NO, oasdi=YES, medicare=YES, futa=YES, sui=YES,
                state_programmes=YES, pension=NA, state_income_tax=YES, local_income_tax=YES)


def flags_supp():
    f = flags_reg()
    f.update(table_tax=YN, special_tax=YN)
    return f


def flags_tips():
    f = flags_reg()
    f.update(income_tax=YN, oasdi=YN, medicare=YN, futa=YN, sui=YN, state_programmes=YN)
    return f


def flags_sev():
    f = flags_reg()
    f.update(table_tax=YN, special_tax=YN, sui=YN, state_programmes=YN)
    return f


def basis_for(flags, over=None):
    b = B()
    out = {k: b[k] for k, v in flags.items() if v != NA}
    out.update(over or {})
    return out


# ------------------------------------------------------------------- parameter text (anchors) ---
def txt_fit():
    return (f"Federal income tax (FIT) is withheld by {val('fed.fit.method')} [{rid('fed.fit.method')}]. "
            f"Rounding: {val('fed.fit.rounding')} [{rid('fed.fit.rounding')}].")


def txt_fica():
    return (f"Social security (OASDI): employee {val('fed.fica.oasdi.rate.employee')} and employer {val('fed.fica.oasdi.rate.employer')} "
            f"of wages up to the annual wage base {val('fed.fica.oasdi.wage_base')} per employee per employer [{rid('fed.fica.oasdi.wage_base')}]. "
            f"Medicare: employee {val('fed.fica.medicare.rate.employee')} and employer {val('fed.fica.medicare.rate.employer')} "
            f"of all wages [{rid('fed.fica.medicare.rate.employee')}]. Additional Medicare Tax: {val('fed.fica.addl_medicare.rate')} "
            f"withheld from the employee on wages above {val('fed.fica.addl_medicare.withholding_threshold')} in the calendar year "
            f"[{rid('fed.fica.addl_medicare.rate')}].")


def txt_futa():
    return (f"FUTA (employer only): net rate {val('fed.futa.rate.net')} on the first {val('fed.futa.wage_base')} of wages per employee "
            f"per year [{rid('fed.futa.wage_base')}].")


def txt_all_taxes():
    return " ".join([txt_fit(), txt_fica(), txt_futa()])


def txt_state_layer(sym_hint=""):
    return ("State income tax, State unemployment insurance, State programme contributions and local taxes follow the "
            "jurisdiction rows of this catalogue (see the State layer index on the Global WTC Coverage sheet); a State "
            "departure from the federal base is stated on the row that carries it.")
