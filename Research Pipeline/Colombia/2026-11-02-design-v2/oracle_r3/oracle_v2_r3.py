# COPIA AJUSTADA (2026-11-02, design v2.0 rodada 3) do oracle_v2.py, que fica intacto em 2026-10-29-validacao-research/oracle/.
# Ajustes (convencoes confirmadas pela lei na revisao independente):
#   R3-1 aporte arredondado uma vez por cotizante e fundo (Decreto 780 art. 3.2.1.5 num. 2; AT2 v30 campo 47): parte do
#        empregado = taxa legal ao peso; parte do empregador = total arredondado ao multiplo de 100 - parte do empregado;
#        fundo pago so pelo empregado (saude exonerada, FSP) = total arredondado.
#   R3-2 INCRNGO = aportes efetivamente descontados do empregado (ET arts. 55, 56 "que efectuen los trabajadores").
# ORACULO v2 (rodada 4, 2026-10-30) - copia de oracle.py com as decisoes da pesquisa oficial de 30/10
# (pesquisa-2026-10-30/TABELA-CONSOLIDADA.md; DECISOES-TEST4.md). oracle.py e oracle_v1_frozen.py ficam intactos.
# Mudancas (cada uma comentada no ponto do codigo):
#   T4-2  integral: IBC = 70% x salario integral + excesso Ley 1393 (excesso sem redutor) - Ley 100 art. 18; CE SU 25185/2021; CE 25907/2022
#   T4-4  excesso Ley 1393 so em saude, pensao e ARL; fora de CCF/SENA/ICBF - Ley 1393 art. 30; DL 1295/1994 art. 17; Ley 21/1982 art. 17
#   T4-5  limite de 40% so sobre o nao salarial desalarizado por pacto (campo "nonsalary_kind": pacted [default] | natural) - CE SU 25185/2021 regra 1; CE 25907/2022
#   T4-1  114-1: salario do mes < 10 SMMLV E IBC saude < 10 SMMLV (trava AT2 v30 campo 76) - DIAN Conceptos 8380/2024 e 7196/2025
#   A-08  72 UVT/dependente fora da retencao mensal (so declaracao anual); teto 40% / 1.340 UVT MANTIDO - DIAN Concepto 11383/2024 IV.2; DUR 1.2.4.1.6 par. 3
# Uso: python -I oracle_v2.py cases.json results-v2r4-<ts>.json
import json, sys, datetime
from decimal import Decimal as Dc, ROUND_HALF_UP, getcontext
getcontext().prec = 40

import os
HERE = os.path.dirname(os.path.abspath(__file__)) + os.sep
PAR = json.load(open(HERE + "params.json", encoding="utf-8"))


def V(k):
    return PAR[k]["value"]


def D(x):
    return x if isinstance(x, Dc) else Dc(str(x))


SMMLV = D(V("SMMLV_2026"))
UVT = D(V("UVT_2026"))
AUX = D(V("AUX_TRANSPORTE_2026"))


def peso(x):
    """AT2 v30: redondeo al peso, aproximacion aritmetica (>= .50 sube)."""
    return int(D(x).quantize(Dc("1"), rounding=ROUND_HALF_UP))


def ceil_peso(x):
    """Decreto 780/2016 art. 3.2.1.5 (Decreto 1990/2016 art. 1) num.1: IBC al peso superior."""
    import math
    return int(math.ceil(D(x)))


def ceil100(x):
    """idem num.2: aportes liquidados por cotizante al multiplo de 100 superior."""
    import math
    return int(math.ceil(D(x) / 100)) * 100


def series_at(key, date):
    val = None
    for s in V(key):
        if s["from"] <= date:
            val = s["value"]
    return D(val) if val is not None else None


def divisor_hora(date):
    # antes de 2025-07-15: 230 (Ley 2101: 47h->... ) no usado en 2026; se cubre 2026
    v = series_at("DIVISOR_HORA", date)
    return v if v is not None else D(230)


def rec_dom(date):
    v = series_at("REC_DOMINICAL", date)
    return v if v is not None else D("0.75")


def hours_line(h):
    """valor de las horas: devuelve (valor, detalle)"""
    date = h["date"]
    hv = D(h["_salary"]) / divisor_hora(date)
    t = h["type"]
    n = D(h["hours"])
    rn, hed, hen = D(V("REC_NOCTURNO")), D(V("REC_EXTRA_DIURNA")), D(V("REC_EXTRA_NOCTURNA"))
    rd = rec_dom(date)
    # factores sobre el valor hora ordinario. Para mensualista el valor ordinario ya esta en el salario,
    # entonces solo se paga el recargo, salvo horas extras (que son tiempo adicional => 1 + recargo)
    f = {
        "RN": rn,                 # recargo nocturno ordinario
        "HED": 1 + hed,           # extra diurna
        "HEN": 1 + hen,           # extra nocturna
        "DOM": 1 + rd,            # horas trabajadas en dia de descanso: 100% + recargo (art.173 descanso ya en el salario mensual; art.179 recargo)
        "RN_DOM": 1 + rn + rd,    # nocturno ordinario en dia de descanso
        "HED_DOM": 1 + hed + rd,  # extra diurna en dia de descanso
        "HEN_DOM": 1 + hen + rd,  # extra nocturna en dia de descanso
    }[t]
    return n * hv * f, {"hv": float(hv), "factor": float(f), "divisor": float(divisor_hora(date)), "rec_dom": float(rd)}


def f2(x):
    return round(float(x), 2)


def retencion(income, incrngo, deduc_dep, deduc_prep, deduc_viv, afc, wp, dep72=0):
    """Procedimiento 1 (DUR 1625 art. 1.2.4.1.3). Todo en COP; devuelve dict de lineas."""
    out = {}
    base1 = income - incrngo
    out["ret_ingreso_laboral"] = f2(income)
    out["ret_incrngo_ss"] = f2(incrngo)
    out["ret_subtotal_tras_incrngo"] = f2(base1)
    dep = min(D(V("RET_DEP_PCT")) * income, D(V("RET_DEP_MAX_UVT")) * UVT) if deduc_dep else Dc(0)
    prep = min(D(deduc_prep), D(V("RET_PREPAGADA_MAX_UVT")) * UVT)
    viv = min(D(deduc_viv), D(V("RET_VIVIENDA_MAX_UVT")) * UVT)
    afc_cap = min(D(V("RET_AFC_PCT")) * income, D(V("RET_AFC_MAX_UVT_ANO")) * UVT / 12)
    afc_ex = min(D(afc), afc_cap)
    deds = dep + prep + viv
    # 25% (ET 206 num.10) se calcula tras detraer INCRNGO, deducciones y otras exentas
    e25_base = base1 - deds - afc_ex
    e25 = min(D(V("RET_EXENTA25_PCT")) * max(e25_base, Dc(0)), D(V("RET_EXENTA25_UVT_ANO")) * UVT / 12)
    cap = min(D(V("RET_CAP_PCT")) * base1, D(V("RET_CAP_UVT_ANO")) * UVT / 12)
    total_benef = deds + afc_ex + e25
    aplicado = min(total_benef, max(cap, Dc(0)))
    # ET 336 num.3 inc.2 (Ley 2277/2022): 72 UVT por dependiente (max 4), ADICIONAL al limite 40%/1340; prorrateo mensual /12
    # A-08 (v2): os 72 UVT/dependente (ET 336 num. 3) NAO entram na retencao mensal: o art. 388 remete ao 387, nao ao 336
    # (DIAN Concepto 11383/2024 cap. IV preg. 2). So na declaracao anual. O teto 40% / 1.340 UVT acima (cap) FICA:
    # DUR 1625 art. 1.2.4.1.6 par. 3 (Decreto 2231/2023) o manda aplicar na retencao (norma superior a doutrina).
    out["ret_dep72_so_declaracao_anual"] = f2(D(min(int(dep72), 4)) * 72 * UVT / 12)
    d72 = Dc(0)
    out["ret_deduc_dependiente_72uvt"] = f2(d72)
    base = max(base1 - aplicado - d72, Dc(0))
    out["ret_deduc_dependientes"] = f2(dep)
    out["ret_deduc_prepagada"] = f2(prep)
    out["ret_deduc_vivienda"] = f2(viv)
    out["ret_exenta_afc"] = f2(afc_ex)
    out["ret_exenta_25"] = f2(e25)
    out["ret_cap_40_1340"] = f2(cap)
    out["ret_beneficios_aplicados"] = f2(aplicado)
    out["ret_base_gravable"] = f2(base)
    buvt = base / UVT
    out["ret_base_uvt"] = f2(buvt)
    imp = Dc(0)
    for lo, hi, rate, fix in V("RET_TABLA_383"):
        lo, hi, rate, fix = D(lo), D(hi), D(rate), D(fix)
        if buvt > lo and buvt <= hi:
            imp = (buvt - lo) * rate + fix
            break
    out["ret_impuesto_uvt"] = f2(imp)
    out["ret_valor_retener_raw"] = f2(imp * UVT)
    out["ret_valor_retener"] = peso(imp * UVT)
    return out


def monthly(c):
    """v2: redondeo PILA conforme Decreto 780 art. 3.2.1.5 (IBC al peso superior; aportes por cotizante al multiplo de 100 superior);
    se conservan valores *_raw sin redondeo (XML/payslip)."""
    o = {}
    sal = D(c["salary"])
    days = D(c.get("days", 30))
    integral = c.get("integral", False)
    base_pay = sal * days / 30
    extras = Dc(0)
    for h in c.get("extras", []):
        h = dict(h)
        h["_salary"] = sal
        val, det = hours_line(h)
        extras += val
        o["extra_%s_%s" % (h["type"], h["date"])] = f2(val)
    comm = D(c.get("commission", 0))
    salary_pay = base_pay + extras + comm
    o["basic"] = f2(base_pay)
    if extras:
        o["extras_total"] = f2(extras)
    aux = Dc(0)
    if (not integral) and sal <= D(V("AUX_TRANSPORTE_TETO_SMMLV")) * SMMLV:
        aux = AUX * days / 30
    o["auxilio_transporte"] = f2(aux)
    nonsal = D(c.get("nonsalary", 0))
    # T4-5 (v2): o limite de 40% (Ley 1393 art. 30) so alcanca o nao salarial DESALARIZADO POR PACTO. O nao salarial por
    # natureza (CST 128, 1a parte) fica fora do IBC, do numerador e do total (CE SU 25185/2021 regra 1; CE 25907/2022).
    # Campo novo do caso: "nonsalary_kind" = "pacted" (default, mantem os casos antigos) | "natural".
    # "nonsalary_natural" (opcional) = valor extra por natureza, so na renda tributavel.
    kind = c.get("nonsalary_kind", "pacted")
    ns_pact = nonsal if kind == "pacted" else Dc(0)
    ns_nat = (nonsal if kind == "natural" else Dc(0)) + D(c.get("nonsalary_natural", 0))
    # T4-2 (v2): no integral o "total da remuneracao" e o salario integral 100% + NS pactado (Ley 1393 art. 30)
    total_rem = salary_pay + ns_pact
    exceso = max(ns_pact - D(V("NOSALARIAL_MAX_PCT")) * total_rem, Dc(0))
    if nonsal or ns_nat:
        o["ley1393_exceso"] = f2(exceso)
        o["nonsalary_kind"] = kind
    # T4-2 (v2): integral = 70% x salario integral + excesso, sem redutor no excesso (Ley 100 art. 18 "70% de dicho salario";
    # CE SU 25185/2021 regra 3 "factores salariales + excesso"). v1 ignorava o excesso no integral.
    sal_base = salary_pay * D(V("INTEGRAL_IBC_PCT")) if integral else salary_pay
    ibc_raw = sal_base + exceso
    lo = D(V("IBC_MIN_SMMLV")) * SMMLV * days / 30
    hi = D(V("IBC_MAX_SMMLV")) * SMMLV * days / 30
    ibc_dec = min(max(ibc_raw, lo), hi)
    ibc = ceil_peso(ibc_dec)
    o["IBC"] = ibc
    mult = D(ibc) / (SMMLV * days / 30)
    o["IBC_en_SMMLV"] = round(float(mult), 6)
    pt, ps = D(V("PENSION_TOTAL")), D(V("PENSION_EMP_SHARE"))
    ib = D(ibc)
    raw = {}
    raw["salud_trab"] = ib * D(V("SALUD_TRAB"))
    raw["pension_trab"] = ib * pt * (1 - ps)
    fsp_s = fsp_b = Dc(0)
    if mult >= D(V("FSP_MIN_SMMLV")):
        fsp_s = ib * D(V("FSP_SOLIDARIDAD"))
        extra = Dc(0)
        for t in V("FSP_SUBSISTENCIA_TRAMOS"):
            ok = (mult >= D(t["gt"])) if t.get("incl_lower") else (mult > D(t["gt"]))
            if ok and mult <= D(t["le"]):
                extra = D(t["extra"])
        fsp_b = ib * (D(V("FSP_SUBSISTENCIA_BASE")) + extra)
    raw["fsp_solidaridad"] = fsp_s
    raw["fsp_subsistencia"] = fsp_b
    # T4-1 (v2): teste do ET 114-1 so sobre o pagamento salarial do mes (DIAN Conceptos 8380/2024 e 7196/2025; CE S4 25302/2022 e seg.)
    # E trava operacional da PILA: IBC saude >= 10 SMMLV obriga N (AT2 v30 campo 76). Salario < 10 com IBC >= 10 -> nao exonera, revisao manual.
    devenga = salary_pay
    lim = D(V("EXONERACION_LIMITE_SMMLV")) * SMMLV
    eleg = c.get("exonerated", True)
    sal_ok = devenga < lim
    ibc_ok = D(ibc) < lim
    exon = eleg and sal_ok and ibc_ok
    o["exonerado_114_1"] = bool(exon)
    if eleg and sal_ok and not ibc_ok:
        o["exon_travada_campo76"] = True
    raw["salud_emp"] = Dc(0) if exon else ib * D(V("SALUD_EMP"))
    raw["pension_emp"] = ib * pt * ps
    risk = c.get("risk", "I")
    raw["arl"] = ib * D(V("ARL")[risk])
    # T4-4 (v2): o excesso da Ley 1393 vale so para Ley 100 arts. 18 e 204 (pensao, saude) e chega a ARL por DL 1295/1994 art. 17
    # (ARL usa ib acima). CCF/SENA/ICBF: Ley 21/1982 art. 17 (salario + descansos remunerados), sem excesso. UGPP ABC 2025 (exemplo).
    para_base = max(sal_base, lo)
    raw["ccf"] = para_base * D(V("CCF"))
    raw["sena"] = Dc(0) if exon else para_base * D(V("SENA"))
    raw["icbf"] = Dc(0) if exon else para_base * D(V("ICBF"))
    for k, v in raw.items():
        o[k] = ceil100(v)          # PILA (valor de aporte por cotizante)
        o[k + "_raw"] = f2(v)        # sin redondeo (XML / payslip)
    # R3-1: saude e pensao = um aporte por fundo; parte do empregado ao peso, empregador = total - empregado
    if not exon:
        o["salud_trab"] = peso(raw["salud_trab"])
        o["salud_emp"] = ceil100(raw["salud_trab"] + raw["salud_emp"]) - o["salud_trab"]
    o["pension_trab"] = peso(raw["pension_trab"])
    o["pension_emp"] = ceil100(raw["pension_trab"] + raw["pension_emp"]) - o["pension_trab"]
    if c.get("retention", True):
        r = c.get("ret", {})
        income = salary_pay + nonsal + D(c.get("nonsalary_natural", 0)) + aux
        days_n = int(days)
        factor = Dc(1)
        if r.get("sub30") and days_n < 30:
            factor = Dc(30) / days  # DUR 1.2.4.1.3 proc.1 a): pagos / dias * 30 -> % -> aplicar a pagos reales
        inc_n = income * factor
        incrngo = (D(o["salud_trab"]) + D(o["pension_trab"]) + D(o["fsp_solidaridad"]) + D(o["fsp_subsistencia"])) * factor   # R3-2
        rt = retencion(inc_n, incrngo, r.get("dependientes", False), r.get("prepagada", 0), r.get("vivienda", 0), r.get("afc", 0), None,
                       dep72=r.get("dep72", 0))
        if factor != 1:
            pct = D(rt["ret_valor_retener_raw"]) / inc_n
            rt["ret_pct_aplicable"] = round(float(pct), 6)
            rt["ret_valor_retener_raw"] = f2(pct * income)
        o.update(rt)
    o["neto_aprox_raw"] = f2(salary_pay + nonsal + D(c.get("nonsalary_natural", 0)) + aux - raw["salud_trab"] - raw["pension_trab"] - fsp_s - fsp_b - D(o.get("ret_valor_retener_raw", 0)))
    return o


def days360(a, b):
    """dias comerciales 30/360 inclusivos entre dos fechas ISO."""
    y1, m1, d1 = map(int, a.split("-"))
    y2, m2, d2 = map(int, b.split("-"))
    d1 = min(d1, 30)
    d2 = min(d2, 30)
    return (y2 - y1) * 360 + (m2 - m1) * 30 + (d2 - d1) + 1


def prestaciones(c):
    o = {}
    sal = D(c["salary"])
    aux = AUX if sal <= 2 * SMMLV and not c.get("integral") else Dc(0)
    base = sal + aux
    days = D(c["days"])
    o["base_prima_cesantias"] = peso(base)
    kind = c["kind"]
    if kind in ("prima", "all"):
        o["prima"] = peso(base * days / 360)
    if kind in ("cesantias", "all"):
        ces = base * days / 360
        o["cesantias"] = peso(ces)
        o["intereses_cesantias"] = peso(ces * days * D(V("INTERES_CESANTIA")) / 360)
    return o


def vacaciones(c):
    o = {}
    sal = D(c["salary"])  # salario ordinario (sin extras, sin auxilio)
    if c["mode"] == "gozadas":
        o["vac_valor_dia"] = peso(sal / 30)
        o["vac_pago"] = peso(sal / 30 * D(c["dias_habiles"]))
    elif c["mode"] == "compensadas":
        maxd = D(V("VACACIONES_DIAS_HABILES")) * D(V("VACACIONES_COMPENSABLE_MAX"))
        d = D(c["dias_habiles"])
        o["max_compensable_dias"] = float(maxd)
        o["compensacion_excede_mitad"] = bool(d > maxd)
        o["vac_pago"] = peso(sal / 30 * d)
    elif c["mode"] == "mixta":
        o["vac_pago_gozadas"] = peso(sal / 30 * D(c["gozadas"]))
        o["vac_pago_compensadas"] = peso(sal / 30 * D(c["compensadas"]))
        o["vac_total"] = o["vac_pago_gozadas"] + o["vac_pago_compensadas"]
    elif c["mode"] == "causacion":
        o["vac_causada"] = peso(sal * D(c["days_worked"]) / 720)
    return o


def incapacidad(c):
    o = {}
    sal = D(c["salary"])
    dia = sal / 30
    smldv = SMMLV / 30
    tot = Dc(0)
    for seg in V("INC_COMUN"):
        a, b = seg["d_from"], seg["d_to"]
        n = max(0, min(c["days"], b) - a + 1)
        if n:
            val = dia * D(seg["pct"]) * n if False else dia * (Dc(2) / 3 if seg["pct"] > 0.6 else Dc("0.5")) * n
            o["inc_dias_%d_%d_%s" % (a, b, seg["payer"])] = peso(val)
            tot += val
    o["inc_total"] = peso(tot)
    o["inc_valor_dia_sin_piso"] = peso(dia * Dc(2) / 3)
    o["piso_smldv_dia"] = peso(smldv)
    o["piso_aplica"] = bool(dia * Dc(2) / 3 < smldv)
    o["IBC_incapacidad"] = peso(max(tot, SMMLV * D(c["days"]) / 30))
    return o


def maternidad(c):
    o = {}
    sal = D(c["salary"])
    dias = D(V("MATERNIDAD_SEMANAS")) * 7
    o["lic_dias"] = int(dias)
    o["lic_valor"] = peso(sal / 30 * dias)
    o["lic_IBC"] = peso(max(sal / 30 * dias, SMMLV / 30 * dias))
    return o


def terminacion(c):
    o = {}
    sal = D(c["salary"])
    n = days360(c["start"], c["end"])
    o["dias_servicio_360"] = n
    p = V("INDEMNIZACION_ART64")["ge10" if sal >= 10 * SMMLV else "lt10"]
    extra_days = max(D(n) - 360, Dc(0))
    ind_days = D(p["first_year_days"]) + D(p["add_per_year"]) * extra_days / 360
    if n <= 360:
        ind_days = D(p["first_year_days"])
    o["indemnizacion_dias"] = float(ind_days)
    o["indemnizacion_valor"] = peso(sal / 30 * ind_days)
    return o


def pila51(c):
    o = {}
    d = c["days"]
    q = None
    for b in V("PILA51_BANDAS"):
        if b["d_min"] <= d <= b["d_max"]:
            q = b["cuartos"]
    ibc = SMMLV * q / 4
    o["IBC_pension"] = peso(ibc)
    tot = peso(ibc * D(V("PENSION_TOTAL")))
    o["pension_total"] = tot
    o["pension_trab"] = peso(ibc * D(V("PENSION_TOTAL")) * (1 - D(V("PENSION_EMP_SHARE"))))
    o["pension_emp"] = tot - o["pension_trab"]   # R3-1 (AT2 v30 campo 47: total = IBC x 16%)
    o["IBC_arl"] = peso(SMMLV)
    o["arl"] = peso(SMMLV * D(V("ARL")[c.get("risk", "I")]))
    o["IBC_ccf"] = peso(ibc)
    o["ccf"] = peso(ibc * D(V("CCF")))
    return o


def ret_table(c):
    base = D(c["base_cop"])
    buvt = base / UVT
    imp = Dc(0)
    for lo, hi, rate, fix in V("RET_TABLA_383"):
        lo, hi, rate, fix = D(lo), D(hi), D(rate), D(fix)
        if buvt > lo and buvt <= hi:
            imp = (buvt - lo) * rate + fix
            break
    return {"base_uvt": float(buvt), "impuesto_uvt": float(imp), "valor_retener": peso(imp * UVT)}


MOD = {"ret_table": ret_table, "monthly": monthly, "prestaciones": prestaciones, "vacaciones": vacaciones, "incapacidad": incapacidad,
       "maternidad": maternidad, "terminacion": terminacion, "pila51": pila51}


def run(cases):
    res = []
    for c in cases:
        if c.get("pending"):
            res.append({"id": c["id"], "status": "PENDENTE", "reason": c["pending"], "name": c["name"]})
            continue
        out = MOD[c["module"]](c)
        res.append({"id": c["id"], "name": c["name"], "status": "RAN", "lines": out})
    return res


if __name__ == "__main__":
    cases = json.load(open(sys.argv[1], encoding="utf-8"))
    res = run(cases["cases"] if isinstance(cases, dict) else cases)
    json.dump({"generated": datetime.datetime.now().isoformat(timespec="seconds"), "oracle": "oracle_v2.py", "params": "params.json", "results": res},
              open(sys.argv[2], "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    n = sum(len(r.get("lines", {})) for r in res)
    print("cases", len(res), "lines", n, "pending", sum(1 for r in res if r["status"] == "PENDENTE"))
