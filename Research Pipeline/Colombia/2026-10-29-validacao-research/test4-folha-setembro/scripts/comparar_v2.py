# Test 4 - compara a folha REAL de setembro/2026 (provedor PMI, mascarada) com o ORACULO independente (so lei).
# v2 (rodada 4, 2026-10-30): usa oracle/oracle_v2.py (decisoes da pesquisa de 30/10: T4-1, T4-2, T4-4, T4-5, A-08).
# comparar.py e resultados.json originais ficam intactos. Uso:
#   python -I comparar_v2.py <entradas.json> <resultados-v2.json>
# Classes: BATE (|d|<=1) | TOLERANCIA (1<|d|<=100 COP) | SEM_DADO (entrada ausente / fora do modelo do oraculo) | DIVERGENCIA (|d|>100)
import sys, json, os, importlib.util, collections, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
ORA = os.path.normpath(os.path.join(HERE, "..", "..", "oracle", "oracle_v2.py"))
spec = importlib.util.spec_from_file_location("oracle_v2", ORA)
O = importlib.util.module_from_spec(spec)
spec.loader.exec_module(O)
D, V = O.D, O.V
SM, UVT = float(O.SMMLV), float(O.UVT)

ENT = json.load(open(sys.argv[1], encoding="utf-8"))
SEV = json.load(open(sys.argv[1].replace(".json", "-indemnizacao.json"), encoding="utf-8"))
EMP = ENT["employees"]
lines = []


def cls(d):
    a = abs(d)
    return "BATE" if a <= 1 else ("TOLERANCIA" if a <= 100 else "DIVERGENCIA")


def add(e, bloco, linha, prov, orac, mec=None, extra=None):
    if prov is None or orac is None:
        c, d = "SEM_DADO", None
    else:
        d = round(float(prov) - float(orac), 2)
        c = cls(d)
    if bloco == "D-INDEMNIZACAO" and linha == "dias" and d is not None:
        c = "BATE" if abs(d) < 0.01 else "DIVERGENCIA"  # dias: sem tolerancia em COP
    if c == "DIVERGENCIA" and mec and mec.startswith("SEM_EFEITO"):
        c = "SEM_EFEITO"
    if c == "DIVERGENCIA" and mec and mec.startswith("LACUNA_ORACULO"):
        c = "LACUNA_ORACULO"
    rec = {"emp": e, "bloco": bloco, "linha": linha, "provedor": prov, "oraculo": orac, "dif": d, "classe": c}
    if mec:
        rec["mecanismo"] = mec
    if extra:
        rec.update(extra)
    lines.append(rec)


def semdado(e, bloco, linha, motivo):
    lines.append({"emp": e, "bloco": bloco, "linha": linha, "provedor": None, "oraculo": None, "dif": None, "classe": "SEM_DADO", "motivo": motivo})


RISK = {"Class 1": "I", "1": "I", "Class 2": "II", "2": "II", "Class 3": "III", "Class 4": "IV", "Class 5": "V"}
LEAVE_WT = ("79401", "79403", "79405", "79406", "79407", "79408", "79411", "79414", "79418", "79419")

for e in EMP:
    idx = e["idx"]
    w = e["wt"]
    r = e["ibc_report"]
    has_leave = any(k in w for k in LEAVE_WT) or bool(w.get("64996"))
    intern = "62149" in w  # Internship Pay (INKOMPASS): apoio de sostenimiento, nao salarial
    pensioner = False  # campo Regime "AReg" do master data nao indica isencao de pensao (o provedor desconta pensao nesses casos)
    risk = RISK.get(e.get("arl_class") or "", None)
    # ---------------- A. IBC (Ley 100 art.18 / Ley 797 art.5; Ley 1393 art.30; integral 70%; teto 25 / piso 1 SMMLV; peso superior) -------------
    o = None
    if not r:
        semdado(idx, "A-IBC", "IBC", "empregado sem linha no Detail IBC report")
    elif intern:
        semdado(idx, "A-IBC", "IBC", "estagiario/aprendiz (62149 INKOMPASS): regra de aporte de aprendiz fora do oraculo (sem parametro)")
    elif has_leave:
        semdado(idx, "A-IBC", "IBC", "mes com ferias/incapacidade/licenca: IBC dos dias de ausencia (Dec. 780 art. 3.2.1.10 / vacaciones) nao modelado no oraculo")
    else:
        c = {"salary": r["salary_value"], "days": 30, "integral": e["integral"], "nonsalary": r["nonwage_value"],
             "risk": risk or "I", "retention": False}
        o = O.monthly(c)
        prov_ibc = r["ibc_total"]
        mec = None
        if abs(prov_ibc - o["IBC"]) > 100:
            # v2 (T4-2): o oraculo ja faz 70% x integral + excesso; a antiga LACUNA_ORACULO deixa de existir
            if e["integral"] and abs(prov_ibc - 0.7 * (r["salary_value"] + r["nonwage_value"])) <= 1:
                mec = "integral: 70% aplicado sobre salario + nao salariais (oraculo v2: 70% so do salario + excesso 1393)"
            elif e["integral"]:
                exc = max(0.0, r["nonwage_value"] - 0.4 * (r["salary_value"] + r["nonwage_value"]))
                alt = O.ceil_peso(min(max(0.7 * (r["salary_value"] + exc), SM), 25 * SM))
                mec = ("integral: 70% aplicado sobre (salario + excesso) - leitura (b) do CCG v1.4" if abs(prov_ibc - alt) <= 100
                       else "nao identificado")
            else:
                mec = "nao identificado"
        add(idx, "A-IBC", "IBC", prov_ibc, o["IBC"], mec, {"integral": e["integral"]})
        if r["nonwage_value"]:
            # excesso 1393 implicito no provedor: IBC_prov - base salarial
            base_sal = (0.7 if e["integral"] else 1) * r["salary_value"]
            prov_exc = max(0.0, min(prov_ibc, 25 * SM) - max(base_sal, SM)) if prov_ibc < 25 * SM else None
            add(idx, "A-IBC", "excesso_ley1393", None if prov_exc is None else round(prov_exc), o.get("ley1393_exceso", 0.0))
    # ---------------- B. Aportes (taxas da lei aplicadas ao IBC REPORTADO pelo provedor -> isola a regra de taxa/exoneracao/FSP/ARL) ----------
    if r and not intern and r["ibc_total"] > 0:
        ib = D(r["ibc_total"])
        base_g2n = -w.get("2556", 0.0) / 0.04 if w.get("2556") else None
        base_incons = base_g2n is not None and abs(base_g2n - float(ib)) > 2500
        ibf = float(ib)
        mult = ibf / SM
        exp = {}
        if not pensioner:
            exp["2554 salud trab 4%"] = ("2554", ibf * float(V("SALUD_TRAB")))
            exp["2556 pension trab 4%"] = ("2556", ibf * float(V("PENSION_TOTAL")) * (1 - float(V("PENSION_EMP_SHARE"))))
            exp["2567 pension emp 12%"] = ("2567", ibf * float(V("PENSION_TOTAL")) * float(V("PENSION_EMP_SHARE")))
            fsp = 0.0
            if mult >= float(V("FSP_MIN_SMMLV")):
                extra = 0.0
                for t in V("FSP_SUBSISTENCIA_TRAMOS"):
                    ok = (mult >= t["gt"]) if t.get("incl_lower") else (mult > t["gt"])
                    if ok and mult <= t["le"]:
                        extra = t["extra"]
                fsp = ibf * (float(V("FSP_SOLIDARIDAD")) + float(V("FSP_SUBSISTENCIA_BASE")) + extra)
            exp["2553 FSP"] = ("2553", fsp)
        # v2 (T4-1): exoneracao art. 114-1 ET = salario do mes < 10 SMMLV (so pagamentos salariais, sem ferias:
        # DIAN Conceptos 8380/2024 e 7196/2025) E IBC saude < 10 SMMLV (trava AT2 v30 campo 76)
        lim = float(V("EXONERACION_LIMITE_SMMLV")) * SM
        dev = r["salary_value"]
        trava76 = dev < lim and ibf >= lim
        exon = dev < lim and ibf < lim
        exp["2564 salud emp 8,5% (exon. 114-1)"] = ("2564", 0.0 if exon else ibf * float(V("SALUD_EMP")))
        if risk and not has_leave:
            exp["2560 ARL classe %s" % risk] = ("2560", ibf * float(V("ARL")[risk]))
        elif has_leave:
            semdado(idx, "B-APORTES", "2560 ARL", "mes com ausencia: ARL nao incide nos dias de ferias/incapacidade (base ARL != IBC total)")
        for k, (wt, val) in exp.items():
            prov = -w.get(wt, 0.0)
            mec = None
            if abs(prov - val) > 100:
                rate = {"2567": 0.12, "2560": float(V("ARL")[risk]) if risk else None, "2554": 0.04, "2556": 0.04}.get(wt)
                b64990 = w.get("64990", 0.0)
                if base_incons and wt != "2564":
                    mec = "inconsistencia interna do provedor: base usada no G2N != IBC do Detail IBC report"
                elif rate and b64990 and abs(prov / rate - b64990) <= 2500 and abs(b64990 - ibf) > 2500:
                    mec = "inconsistencia interna do provedor: aporte do empregador sobre a base 64990, menor que o IBC do trabalhador (Ley 100 art. 18/20: mesma base)"
                elif wt == "2564":
                    mec = "exoneracao 114-1: provedor %s, oraculo %s (salario %s 10 SMMLV%s)" % (
                        "cobra" if prov else "exonera", "exonera" if exon else "cobra", "<" if dev < lim else ">=",
                        "; IBC >= 10 SMMLV: trava campo 76" if trava76 else "")
                elif wt == "2553":
                    mec = "FSP: faixa/percentual diferente (IBC em SMMLV=%.2f)" % mult
                elif wt == "2560":
                    mec = "ARL: taxa implicita %.5f vs classe %s" % (prov / ibf if ibf else 0, risk)
                else:
                    mec = "taxa implicita %.5f" % (prov / ibf if ibf else 0)
            add(idx, "B-APORTES", k, round(prov, 2), round(val, 2), mec, {"exonerado_oraculo": exon, "trava_campo76": trava76} if wt == "2564" else None)
        # parafiscais (CCF 4%; SENA 2% e ICBF 3% com exoneracao): base implicita do provedor = 25110/4%
        ccf_p = -w.get("25110", 0.0)
        if ccf_p:
            pbase = ccf_p / 0.04
            add(idx, "B-APORTES", "25111 ICBF 3% (exon. 114-1)", -w.get("25111", 0.0), 0.0 if exon else pbase * float(V("ICBF")),
                "exoneracao 114-1 (ICBF)" if (bool(w.get("25111")) == exon) else None)
            add(idx, "B-APORTES", "25112 SENA 2% (exon. 114-1)", -w.get("25112", 0.0), 0.0 if exon else pbase * float(V("SENA")),
                "exoneracao 114-1 (SENA)" if (bool(w.get("25112")) == exon) else None)
            if o is not None:
                # base de parafiscais do oraculo (para_base = max(IBC_raw, piso)) x base implicita do provedor
                para_o = float(o["ccf_raw"]) / 0.04
                mec = None
                if abs(pbase - para_o) > 100 * 25:
                    sal_base = (0.7 if e["integral"] else 1.0) * r["salary_value"]
                    # v2 (T4-4): o oraculo ja tira o excesso Ley 1393 da base de parafiscais; a antiga LACUNA_ORACULO deixa de existir
                    if w.get("64990") and abs(pbase - w["64990"]) <= 2500:
                        mec = "inconsistencia interna do provedor: aporte do empregador sobre a base 64990, menor que o IBC do trabalhador (Ley 100 art. 18/20: mesma base)"
                    else:
                        mec = "base CCF: provedor %s oraculo" % (">" if pbase > para_o else "<")
                add(idx, "B-APORTES", "25110 CCF 4% (base do oraculo)", ccf_p, float(o["ccf_raw"]), mec)
        else:
            semdado(idx, "B-APORTES", "25110 CCF", "sem WT 25110 no G2N")
    # ---------------- C. Retencion en la fuente (DUR 1625 art. 1.2.4.1.3/1.2.4.1.6; ET 206 num.10; ET 336 num.3; ET 383) ---------------------
    b = e["bow"]
    if not b or b["income_total"] == 0:
        semdado(idx, "C-RETEFUENTE", "base", "sem linha/renda no Base of Withholding")
    else:
        inc = D(b["income_total"])
        if r and r["ibc_total"] > 0 and not intern:
            ib = float(r["ibc_total"])
            mult = ib / SM
            fsp = 0.0
            if mult >= 4 and not pensioner:
                extra = 0.0
                for t in V("FSP_SUBSISTENCIA_TRAMOS"):
                    ok = (mult >= t["gt"]) if t.get("incl_lower") else (mult > t["gt"])
                    if ok and mult <= t["le"]:
                        extra = t["extra"]
                fsp = ib * (0.01 + extra)
            incr_o = ib * 0.04 + (0 if pensioner else ib * 0.04 + fsp)
            add(idx, "C-RETEFUENTE", "INCRNGO (salud+pension+FSP)", b["incrngo"], round(incr_o, 2))
            incr = D(incr_o)
        else:
            incr = D(b["incrngo"])
            semdado(idx, "C-RETEFUENTE", "INCRNGO", "sem IBC do provedor para recalcular (usado o INCRNGO reportado)")
        rt = O.retencion(inc, incr, b["dep"] > 0, b["prepaid"], b["housing"], b["afc"] + b["apv"], None)
        add(idx, "C-RETEFUENTE", "dependientes 10%/32 UVT", b["dep"], rt["ret_deduc_dependientes"])
        add(idx, "C-RETEFUENTE", "prepagada <=16 UVT", b["prepaid"], rt["ret_deduc_prepagada"])
        add(idx, "C-RETEFUENTE", "vivienda <=100 UVT", b["housing"], rt["ret_deduc_vivienda"])
        afc_mec = None
        if (b["afc"] + b["apv"]) - rt["ret_exenta_afc"] > 100 and rt["ret_beneficios_aplicados"] >= 1340 * UVT / 12 - 1:
            afc_mec = "SEM_EFEITO: coluna AFC/APV acima do teto 30%/3.800 UVT, mas o limite 1.340 UVT ja corta o total"
        add(idx, "C-RETEFUENTE", "AFC+APV <=30%/3800 UVT", b["afc"] + b["apv"], rt["ret_exenta_afc"], afc_mec)
        add(idx, "C-RETEFUENTE", "renta exenta 25% (790 UVT/ano)", b["exempt25"], rt["ret_exenta_25"])
        # limite: provedor reporta o 40% sem o teto de 1340 UVT na coluna '40% limit'; o aplicado e min(total beneficios, limite)
        tot_prov = b["dep"] + b["prepaid"] + b["housing"] + b["afc"] + b["apv"] + b["exempt25"]
        applied_prov = (b["income_total"] - b["incrngo"]) - b["wht_basis"]
        mec = None
        if abs(applied_prov - rt["ret_beneficios_aplicados"]) > 100:
            cap1340 = 1340 * UVT / 12
            if abs(applied_prov) <= 1 and tot_prov > 0:
                mec = "base sem nenhum beneficio (25%, dependentes, AFC/APV) embora a propria planilha calcule o alivio (TOTAL TAX RELIEF)"
            elif tot_prov > cap1340 and applied_prov > cap1340 + 100:
                mec = "limite 1.340 UVT/ano (ET 336 num.3) nao aplicado: beneficios acima de 111,67 UVT/mes aceitos"
            elif abs(applied_prov - min(tot_prov, 0.4 * (b["income_total"] - b["incrngo"]))) <= 100:
                mec = "diferenca herdada (INCRNGO/25%) - limite 40% aplicado"
            else:
                mec = "nao identificado"
        add(idx, "C-RETEFUENTE", "beneficios aplicados (40% / 1.340 UVT)", round(applied_prov, 2), rt["ret_beneficios_aplicados"], mec,
            {"total_beneficios_prov": tot_prov})
        add(idx, "C-RETEFUENTE", "base gravable", b["wht_basis"], rt["ret_base_gravable"], mec)
        g2552 = -w.get("2552", 0.0) - w.get("21330", 0.0)  # expatriados: retencao registrada no WT 21330 (theoretical)
        if e.get("tax_procedure") == "3":
            semdado(idx, "C-RETEFUENTE", "retencion proc.'3'", "procedimento '3' do provedor (20% fixo + parcela constante): nao e procedimento 1 nem 2 do DUR; possivel retencao voluntaria maior - nao recalculado")
        elif b["pct_retention"] == 0:
            add(idx, "C-RETEFUENTE", "retencion proc.1 (tabla art. 383)", b["wht_with"], rt["ret_valor_retener"], mec, {"procedimento": 1})
        else:
            # proc. 2: % semestral nao recalculavel (12 meses anteriores) -> confere so a aritmetica base x %
            semdado(idx, "C-RETEFUENTE", "porcentaje fijo proc.2", "% semestral exige 12 meses anteriores (DUR 1.2.4.1.4); nao recalculado")
            add(idx, "C-RETEFUENTE", "retencion proc.2 = base x % (aritmetica)", b["wht_with"], round(b["wht_basis"] * b["pct_retention"]), None,
                {"procedimento": 2})
            add(idx, "C-RETEFUENTE", "retencion proc.2 com a base do oraculo x % do provedor", b["wht_with"], round(rt["ret_base_gravable"] * b["pct_retention"]), mec,
                {"procedimento": 2})
        add(idx, "C-RETEFUENTE", "G2N 2552 = Base of Withholding (consistencia interna)", g2552, b["wht_with"])
    # ---------------- E. Incapacidade (CST art. 227; Dec. 780 art. 3.2.1.10 / Dec. 2943/2013: 2 primeiros dias empregador) ----------------
    for lv in e["leaves"]:
        if lv["wt"] in ("79008", "79011") and e["salary_assigned"] > 0 and lv["days"] > 0:
            dia = e["salary_assigned"] / 30
            o_val = max(dia * 2 / 3, SM / 30) * lv["days"]
            mec = None
            if abs(lv["amount"] - o_val) > 100:
                ratio = lv["amount"] / (dia * lv["days"])
                mec = "pago a %.0f%% do salario diario (lei: 2/3, piso 1 SMLDV)" % (ratio * 100)
            add(idx, "E-LICENCAS", "incapacidad %s" % lv["wt"], lv["amount"], round(o_val), mec)
        elif lv["wt"] == "79006" and e["salary_assigned"] > 0:
            o_val = e["salary_assigned"] / 30 * lv["days"]
            add(idx, "E-LICENCAS", "maternidad (dias do mes)", lv["amount"], round(o_val))
        elif lv["wt"] in ("79001", "79003"):
            semdado(idx, "E-LICENCAS", "vacaciones %s" % lv["wt"], "base = salario ordinario/promedio 12 meses se variavel (CST 192) e dias habiles x calendario: nao recalculavel com 1 mes")

# ---------------- D. Indemnizacao (CST art. 64, Ley 789/2002 art. 28) - Severance Massive Calculation ----------------
for s in SEV:
    i = s["idx"]
    if not s["ajustada"] or not s["salario_basico"]:
        semdado(i, "D-INDEMNIZACAO", "indemnizacao", "sem data/salario")
        continue
    if s["contrato"] and "Fixed" in s["contrato"]:
        semdado(i, "D-INDEMNIZACAO", "indemnizacao", "contrato a termo fixo: art. 64 = salarios do tempo faltante (data fim nao informada)")
        continue
    if s["ajustada"] <= "1992-12-27":
        semdado(i, "D-INDEMNIZACAO", "indemnizacao", "10+ anos em 27/12/2002: tabela transitoria Ley 789 art. 28 par. (nao parametrizada no oraculo)")
        continue
    # referencia da lei: salario = basico + variavel (CST art. 127: o variavel e salario; o proprio provedor monta BASE INDEMNIZACION assim)
    t = O.terminacion({"salary": s["base"] or s["salario_basico"], "start": s["ajustada"], "end": "2026-09-30"})
    servico = O.days360(s["ajustada"], "2026-09-30")
    if s["dias"] == 0 and servico <= 60:
        semdado(i, "D-INDEMNIZACAO", "indemnizacao", "ingresso ha <= 2 meses e provedor = 0: periodo de prueba (CST arts. 76-80) nao modelado no oraculo")
        continue
    gap = s["dias"] - t["indemnizacion_dias"]
    mec_d = None
    if gap >= 1:
        mec_d = "dias: tabela mais favoravel que o art. 64 (convencional/contratual; CST art. 13 permite)"
    elif -1 <= gap < -0.001:
        mec_d = "dias: fracao de ano truncada em dias inteiros (art. 64: 'proporcionalmente por fraccion')"
    elif gap < -1:
        mec_d = "dias: provedor abaixo do art. 64 em mais de 1 dia (nao identificado)"
    add(i, "D-INDEMNIZACAO", "dias", s["dias"], t["indemnizacion_dias"], mec_d)
    causas = []
    if mec_d:
        causas.append(mec_d)
    if s["variable"] and abs(s["valor"] - s["salario_basico"] / 30 * s["dias"]) <= 1:
        causas.append("valor: so o salario basico; a parte variavel (BASE INDEMNIZACION do proprio relatorio) fica fora")
    add(i, "D-INDEMNIZACAO", "valor", s["valor"], t["indemnizacion_valor"], " + ".join(causas) or None,
        {"variavel": bool(s["variable"]), "faixa_ge10": s["base"] >= 10 * SM})

# ---------------- resumo ----------------
res = collections.Counter(l["classe"] for l in lines)
porbloco = collections.defaultdict(collections.Counter)
mecs = collections.defaultdict(lambda: {"n": 0, "emps": set(), "soma_abs_dif": 0.0, "bloco": None, "linhas": set()})
for l in lines:
    porbloco[l["bloco"]][l["classe"]] += 1
    if l["classe"] == "DIVERGENCIA":
        k = l.get("mecanismo") or "nao identificado"
        k = k.split(" (IBC em")[0] if k.startswith("FSP") else k
        k = "ARL: taxa implicita diferente da classe" if k.startswith("ARL") else k
        k = "taxa implicita diferente" if k.startswith("taxa implicita") else k
        m = mecs[(l["bloco"], k)]
        m["n"] += 1
        m["emps"].add(l["emp"])
        m["soma_abs_dif"] += abs(l["dif"])
        m["linhas"].add(l["linha"])
out = {"generated": datetime.datetime.now().isoformat(timespec="seconds"), "oracle": "oracle/oracle_v2.py + params.json (rodada 4)",
       "fonte": "03-client-reports-masked (folha setembro/2026, copias mascaradas)",
       "empregados": len(EMP), "indemnizacao_linhas_fonte": len(SEV), "linhas": len(lines), "classes": dict(res),
       "por_bloco": {k: dict(v) for k, v in porbloco.items()},
       "divergencias_por_mecanismo": [{"bloco": k[0], "mecanismo": k[1], "linhas": v["n"], "empregados": len(v["emps"]),
                                      "soma_abs_dif": round(v["soma_abs_dif"]), "itens": sorted(v["linhas"])}
                                     for k, v in sorted(mecs.items(), key=lambda x: -x[1]["n"])],
       "nota_privacidade": "valores absolutos (provedor/oraculo) nao sao gravados: so diferenca e classe por linha; rodar os scripts para ver os valores",
       "detalhe": [{k: v for k, v in l.items() if k not in ("provedor", "oraculo", "total_beneficios_prov")} for l in lines]}
json.dump(out, open(sys.argv[2], "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(json.dumps({k: out[k] for k in ("empregados", "linhas", "classes", "por_bloco")}, ensure_ascii=False, indent=1))
for m in out["divergencias_por_mecanismo"]:
    print(m["bloco"], "|", m["mecanismo"], "|", m["linhas"], "linhas", m["empregados"], "emp", m["soma_abs_dif"], m["itens"][:4])
