# ORACULO independente da folha colombiana (Python puro). Escrito SO a partir da lei (params.json); nao le CCG/WTC/skill/hub.
# Uso: python -I oracle.py cases.json results-<ts>.json
import json, sys, datetime
from decimal import Decimal as Dc, ROUND_HALF_UP, getcontext
getcontext().prec = 40

HERE = __file__.rsplit("oracle.py", 1)[0] or "./"
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
        "DOM": rd,                # trabajo ordinario en dia de descanso: solo recargo (art.179)
        "RN_DOM": rn + rd,        # nocturno ordinario en dia de descanso
        "HED_DOM": 1 + hed + rd,  # extra diurna en dia de descanso
        "HEN_DOM": 1 + hen + rd,  # extra nocturna en dia de descanso
    }[t]
    return n * hv * f, {"hv": float(hv), "factor": float(f), "divisor": float(divisor_hora(date)), "rec_dom": float(rd)}


def f2(x):
    return round(float(x), 2)


def retencion(income, incrngo, deduc_dep, deduc_prep, deduc_viv, afc, wp):
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
    base = max(base1 - aplicado, Dc(0))
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
    out["ret_valor_retener"] = peso(imp * UVT)
    return out


def monthly(c):
    o = {}
    sal = D(c["salary"])
    days = D(c.get("days", 30))
    period = c["period"]
    integral = c.get("integral", False)
    base_pay = sal * days / 30
    extras = Dc(0)
    for h in c.get("extras", []):
        h = dict(h)
        h["_salary"] = sal
        val, det = hours_line(h)
        extras += val
        o["extra_%s_%s" % (h["type"], h["date"])] = peso(val)
    comm = D(c.get("commission", 0))
    salary_pay = base_pay + extras + comm
    o["basic"] = peso(base_pay)
    if extras:
        o["extras_total"] = peso(extras)
    aux = Dc(0)
    if (not integral) and sal <= D(V("AUX_TRANSPORTE_TETO_SMMLV")) * SMMLV:
        aux = AUX * days / 30
    o["auxilio_transporte"] = peso(aux)
    nonsal = D(c.get("nonsalary", 0))
    total_rem = salary_pay + nonsal
    exceso = max(nonsal - D(V("NOSALARIAL_MAX_PCT")) * total_rem, Dc(0))
    if nonsal:
        o["ley1393_exceso"] = peso(exceso)
    if integral:
        ibc_raw = salary_pay * D(V("INTEGRAL_IBC_PCT"))
    else:
        ibc_raw = salary_pay + exceso
    lo = D(V("IBC_MIN_SMMLV")) * SMMLV * days / 30
    hi = D(V("IBC_MAX_SMMLV")) * SMMLV * days / 30
    ibc = peso(min(max(ibc_raw, lo), hi))
    o["IBC"] = ibc
    mult = D(ibc) / (SMMLV * days / 30)
    o["IBC_en_SMMLV"] = round(float(mult), 6)
    # empleado
    o["salud_trab"] = peso(D(ibc) * D(V("SALUD_TRAB")))
    o["pension_trab"] = peso(D(ibc) * D(V("PENSION_TOTAL")) * (1 - D(V("PENSION_EMP_SHARE"))))
    fsp_s = fsp_b = 0
    fsp_factor = Dc(0)
    if mult >= D(V("FSP_MIN_SMMLV")):
        fsp_s = peso(D(ibc) * D(V("FSP_SOLIDARIDAD")))
        extra = Dc(0)
        for t in V("FSP_SUBSISTENCIA_TRAMOS"):
            if mult >= D(t["gt"]) if t.get("incl_lower") else mult > D(t["gt"]):
                if mult <= D(t["le"]):
                    extra = D(t["extra"])
        fsp_factor = D(V("FSP_SUBSISTENCIA_BASE")) + extra
        fsp_b = peso(D(ibc) * fsp_factor)
    o["fsp_solidaridad"] = fsp_s
    o["fsp_subsistencia"] = fsp_b
    # empleador
    devenga = salary_pay if not integral else salary_pay
    exon = c.get("exonerated", True) and (devenga < D(V("EXONERACION_LIMITE_SMMLV")) * SMMLV * (days / 30 if c.get("prorate_exon", False) else 1))
    o["exonerado_114_1"] = bool(exon)
    o["salud_emp"] = 0 if exon else peso(D(ibc) * D(V("SALUD_EMP")))
    o["pension_emp"] = peso(D(ibc) * D(V("PENSION_TOTAL")) * D(V("PENSION_EMP_SHARE")))
    risk = c.get("risk", "I")
    o["arl"] = peso(D(ibc) * D(V("ARL")[risk]))
    para_base = ibc_raw if not c.get("para_base_ibc") else D(ibc)
    para_base = max(para_base, lo)
    o["ccf"] = peso(para_base * D(V("CCF")))
    o["sena"] = 0 if exon else peso(para_base * D(V("SENA")))
    o["icbf"] = 0 if exon else peso(para_base * D(V("ICBF")))
    # retencion (procedimiento 1)
    if c.get("retention", True):
        r = c.get("ret", {})
        income = salary_pay + nonsal + aux
        incrngo = D(o["salud_trab"]) + D(o["pension_trab"]) + D(fsp_s) + D(fsp_b)
        o.update(retencion(income, incrngo, r.get("dependientes", False), r.get("prepagada", 0), r.get("vivienda", 0), r.get("afc", 0), None))
    o["neto_aprox"] = peso(salary_pay + nonsal + aux - D(o["salud_trab"]) - D(o["pension_trab"]) - D(fsp_s) - D(fsp_b) - D(o.get("ret_valor_retener", 0)))
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
    o["pension_emp"] = peso(ibc * D(V("PENSION_TOTAL")) * D(V("PENSION_EMP_SHARE")))
    o["pension_trab"] = peso(ibc * D(V("PENSION_TOTAL")) * (1 - D(V("PENSION_EMP_SHARE"))))
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
    json.dump({"generated": datetime.datetime.now().isoformat(timespec="seconds"), "oracle": "oracle.py", "params": "params.json", "results": res},
              open(sys.argv[2], "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    n = sum(len(r.get("lines", {})) for r in res)
    print("cases", len(res), "lines", n, "pending", sum(1 for r in res if r["status"] == "PENDENTE"))
