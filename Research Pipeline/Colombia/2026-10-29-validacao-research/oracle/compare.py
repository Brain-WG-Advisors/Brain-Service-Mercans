# Comparacao linha a linha: valores dos exemplos da research (lidos DEPOIS do congelamento) x oraculo (results-research-*.json).
# Tolerancia COP 1 (PILA: IBC peso superior; aportes multiplo de 100 superior, ja no oraculo v2).
import json, sys, glob
sys.stdout.reconfigure(encoding="utf-8")
HERE = __file__.rsplit("compare.py", 1)[0] or "./"
RES = sorted(glob.glob(HERE + "results-research-*.json"))[-1]
R = {x["id"]: x for x in json.load(open(RES, encoding="utf-8"))["results"]}
SMMLV, UVT, AUX = 1750905, 52374, 249095


def o(case, key):
    return R[case]["lines"][key]


CCG = "CCG-001 v1.4"
items = []  # (ref, artefato, local, descricao, valor_research, valor_oraculo, tol)


def it(ref, art, loc, desc, rv, ov, tol=1.0, note=""):
    items.append(dict(ref=ref, artefato=art, local=loc, desc=desc, research=rv, oraculo=ov, tol=tol, note=note))


# --- CCG 4.3 contratacao no meio do mes (RC01)
L = CCG + " §4.3 'Worked example mid-month hire, August 2026'"
it("CCG-01", CCG, L, "salario basico 20 dias", 1600000.00, o("RC01", "basic"), 0.01)
it("CCG-02", CCG, L, "auxilio de transporte 20 dias", 166063.33, o("RC01", "auxilio_transporte"), 0.01)
it("CCG-03", CCG, L, "IBC", 1600000, o("RC01", "IBC"))
it("CCG-04", CCG, L, "salud trabajador 4% (up to 100)", 64000, o("RC01", "salud_trab"))
it("CCG-05", CCG, L, "pension trabajador 4%", 64000, o("RC01", "pension_trab"))
it("CCG-06", CCG, L, "FSP", 0, o("RC01", "fsp_solidaridad") + o("RC01", "fsp_subsistencia"))
it("CCG-07", CCG, L, "pension empleador 12%", 192000, o("RC01", "pension_emp"))
it("CCG-08", CCG, L, "salud empleador (exonerada)", 0, o("RC01", "salud_emp"))
it("CCG-09", CCG, L, "ARL 0,522% (8.352 -> 8.400)", 8400, o("RC01", "arl"))
it("CCG-10", CCG, L, "CCF 4%", 64000, o("RC01", "ccf"))
it("CCG-11", CCG, L, "SENA+ICBF (exonerados)", 0, o("RC01", "sena") + o("RC01", "icbf"))
it("CCG-12", CCG, L, "base gravavel retencion (proc.1, <30 dias: 30/dias)", 1842821.25, o("RC01", "ret_base_gravable"), 0.01)
it("CCG-13", CCG, L, "retencion", 0, o("RC01", "ret_valor_retener_raw"), 0.01)
# --- CCG 6.1.1 exemplo 1 (RC02)
L = CCG + " §6.1.1 'Worked example resident, Procedure 1, August 2026' / §6.3 Ex.1"
it("CCG-14", CCG, L, "INCRNGO (pension 4% + FSP 1% + salud 4%)", 720000, o("RC02", "ret_incrngo_ss"))
it("CCG-15", CCG, L, "renta exenta 25%", 1820000, o("RC02", "ret_exenta_25"))
it("CCG-16", CCG, L, "base gravavel", 5460000, o("RC02", "ret_base_gravable"))
it("CCG-17", CCG, L, "retencion (tabla 383, banda 19%)", 92049.30, o("RC02", "ret_valor_retener_raw"), 0.01)
# --- CCG 6.3 exemplo 2 (RC03)
L = CCG + " §6.3 'Example 2 - resident employee with declared deductions'"
it("CCG-18", CCG, L, "deducao dependientes art.387 (10% x 8.000.000)", 800000, o("RC03", "ret_deduc_dependientes"))
it("CCG-19", CCG, L, "renta exenta 25% sobre (7.280.000-2.700.000)", 1145000, o("RC03", "ret_exenta_25"))
it("CCG-20", CCG, L, "deducoes+exenta limitadas a 40%", 2912000, o("RC03", "ret_beneficios_aplicados"))
it("CCG-21", CCG, L, "72 UVT x 2 dependientes /12 (fora do cap)", 628488, o("RC03", "ret_deduc_dependiente_72uvt"))
it("CCG-22", CCG, L, "base gravavel", 3739512, o("RC03", "ret_base_gravable"))
it("CCG-23", CCG, L, "retencion", 0, o("RC03", "ret_valor_retener_raw"), 0.01)
# --- CCG 6.3 exemplo 3 alternativa residente (RC04)
L = CCG + " §6.3 'Example 3' (alternativa: se fosse residente)"
it("CCG-24", CCG, L, "base gravavel", 10237500, o("RC04", "ret_base_gravable"))
it("CCG-25", CCG, L, "retencion se residente (banda 28%)", 1190532, o("RC04", "ret_valor_retener_raw"), 1)
it("CCG-26", CCG, L, "FSP 1% total (150.000)", 150000, o("RC04", "fsp_solidaridad") + o("RC04", "fsp_subsistencia"))
# --- CCG 6.3 exemplo 4 (RC05)
L = CCG + " §6.3 'Example 4 - irregular payment: retention bonus'"
it("CCG-27", CCG, L, "excesso 40% devolvido a base (20M - 11,2M)", 8800000, o("RC05", "ley1393_exceso"))
it("CCG-28", CCG, L, "IBC", 16800000, o("RC05", "IBC"))
it("CCG-29", CCG, L, "salud+pension+FSP trabajador (9%)", 1512000, o("RC05", "salud_trab") + o("RC05", "pension_trab") + o("RC05", "fsp_solidaridad") + o("RC05", "fsp_subsistencia"))
it("CCG-30", CCG, L, "renta exenta 25% limitada a 790/12 UVT", 3447955, o("RC05", "ret_exenta_25"))
it("CCG-31", CCG, L, "base gravavel", 23040045, o("RC05", "ret_base_gravable"))
it("CCG-32", CCG, L, "retencion", 4994989.65, o("RC05", "ret_valor_retener_raw"), 0.01)
# --- CCG 4.5 prima / vacaciones / 1.5 / 1.3 / integral
it("CCG-33", CCG, CCG + " §4.5 'Formula and worked example' prima 1o sem", "prima (2.400.000+249.095)x180/360", 1324547.50, o("RC08", "prima"), 1)
it("CCG-34", CCG, CCG + " §8.x 'Vacation payout formula and worked example'", "vacaciones na rescisao 510 dias /720", 1700000, o("RC09", "vac_causada"))
it("CCG-35", CCG, CCG + " §1.5 tabela arredondamento", "ARL 41.760 -> 41.800", 41800, o("RC16", "arl"))
it("CCG-36", CCG, CCG + " §1.3 'Worked illustration' semanal 4 pagos", "salud 4% sobre 2.000.000", 80000, o("RC14", "salud_trab"))
it("CCG-37", CCG, CCG + " §1.3 'Worked illustration' semanal 5 pagos", "salud 4% sobre 2.500.000", 100000, o("RC15", "salud_trab"))
it("CCG-38", CCG, CCG + " §4.6 salario integral piso 13 SMMLV", "IBC 70% x 22.761.765 = 15.933.235,50 arredondado para cima", 15933236, 15933236, 1, "ver C22 do results-v2")
# --- CCG 8.1 mes misto (calculo manual com leis; ver SIMULACAO.md)
L = CCG + " §8.1 'Worked example - a mixed month. September 2026'"
it("CCG-39", CCG, L, "salario 21 dias a 2.400.000", 1680000.00, 2400000 * 21 / 30, 0.01)
it("CCG-40", CCG, L, "vacaciones 5 dias a 2.400.000/30", 400000.00, 2400000 * 5 / 30, 0.01)
it("CCG-41", CCG, L, "IBC = 1.680.000 + 2.200.000x5/30 (IBC previo) + max(incap, SMMLVx4/30)", 2280121, int(-(-(1680000 + 2200000 * 5 / 30 + max(2400000 / 30 * 2 / 3 * 4, SMMLV * 4 / 30)) // 1)))
it("CCG-42", CCG, L, "salud trab 4% (ceil 100) sobre 2.280.121", 91300, int(-(-(2280121 * 0.04) // 100)) * 100)
it("CCG-43", CCG, L, "auxilio de transporte: dias efetivamente trabalhados (21) vs 26 (21+5 ferias)", 215882.33, AUX * 21 / 30, 0.01, "oraculo: aux por dia trabalhado; fonte local ausente => confianca baixa")
# incapacidade: sem piso (CST 227 local) vs com piso (CCG)
it("CCG-44", CCG, L, "incapacidad 4 dias (2/3, sem piso SMLDV)", 233454.00, round(2400000 / 30 * 2 / 3 * 4, 2), 0.01, "PENDENTE: piso 1 SMLDV nao esta no texto local (X02)")
# --- Spec 001 Nomina Electronica (RC06)
S1 = "CO-DIAN-001 Example Analysis"
it("SPEC-01", S1, S1 + "!C35 (B35 Salud)", "salud trab", 480000, o("RC06", "salud_trab_raw"), 0.01)
it("SPEC-02", S1, S1 + "!C36", "pension trab", 480000, o("RC06", "pension_trab_raw"), 0.01)
it("SPEC-03", S1, S1 + "!C37/C38", "FSP solidaridad+subsistencia", 120000, o("RC06", "fsp_solidaridad") + o("RC06", "fsp_subsistencia"))
it("SPEC-04", S1, S1 + "!C39", "base retencion (8.190.000)", 8190000, o("RC06", "ret_base_gravable"))
it("SPEC-05", S1, S1 + "!A39/C39 (NIE177)", "retencion en la fuente empleado", 617000, o("RC06", "ret_valor_retener_raw"), 1, "Spec redondea a 1.000 (ET 868); oraculo: sem arredondamento individual (DUR 1.6.1.11.11 so formularios)")
it("SPEC-06", S1, S1 + "!C40 (NIE188)", "DeduccionesTotal 480.000+480.000+120.000+retencion", 1697000, 480000 * 2 + 120000 + o("RC06", "ret_valor_retener_raw"), 1)
it("SPEC-07", S1, S1 + "!C43 (NIE189)", "ComprobanteTotal 12.000.000 - deducciones", 10303000, 12000000 - (480000 * 2 + 120000 + o("RC06", "ret_valor_retener_raw")), 1)
S2 = "CO-DIAN-002 Example Analysis"
it("SPEC-08", S2, S2 + "!B14 casilla 77", "base retencion", 8190000, o("RC06", "ret_base_gravable"))
it("SPEC-09", S2, S2 + "!B15 casilla 93 (e 130/136/138/980)", "retencion consolidada (arred. a 1.000 no formulario, DUR 1.6.1.11.11)", 617000, round(o("RC06", "ret_valor_retener_raw") / 1000) * 1000, 1, "no formulario 350 o arredondamento a 1.000 e correto (agregado); o erro e propagar para NIE177")
S4 = "CO-DIAN-004 Example Analysis"
it("SPEC-10", S4, S4 + "!C23 casilla 53", "salud 12 meses", 5760000, 12 * 480000)
it("SPEC-11", S4, S4 + "!C24 casilla 54", "pension+FSP 12 meses (600.000/mes)", 7200000, 12 * (480000 + o("RC06", "fsp_solidaridad") + o("RC06", "fsp_subsistencia")))
it("SPEC-12", S4, S4 + "!C27 casilla 60", "retencion anual = 12 x retencion mensual", 7404000, 12 * o("RC06", "ret_valor_retener_raw"), 1)
it("SPEC-13", S4, S4 + "!C20 casilla 49", "cesantias consignadas (saldo 2025 sobre 12M)", 12000000, o("RC13", "cesantias"))
it("SPEC-14", S4, S4 + "!C18 casilla 47", "intereses 12% sobre 12M", 1440000, o("RC13", "intereses_cesantias"))
it("SPEC-15", S4, S4 + "!C26 casilla 59 / 2276 N33", "promedio 6 meses (jul-dic: 6x12M + prima dic 6M)/6", 13120000, (6 * 12000000 + 6000000) / 6, 1, "oraculo nao reproduz 13.120.000")
it("SPEC-16", S4, S4 + "!C26", "umbral 350 UVT", 18330900, 350 * UVT)
it("SPEC-17", S4, S4 + "!C21 casilla 52", "ingreso bruto total 144M+12M+1,44M+12M", 157440000, 144000000 + 12000000 + o("RC13", "intereses_cesantias") + o("RC13", "cesantias"))
S3 = "CO-PILA-003 Example Analysis"
it("SPEC-18", S3, S3 + "!C21 T2R2-042..045", "IBC", 12000000, o("RC06", "IBC"))
it("SPEC-19", S3, S3 + "!C25 T2R2-047", "pension total 16%", 1920000, o("RC06", "pension_emp") + o("RC06", "pension_trab"))
it("SPEC-20", S3, S3 + "!C26-27 T2R2-051/052", "FSP 60.000 + 60.000", 120000, o("RC06", "fsp_solidaridad") + o("RC06", "fsp_subsistencia"))
it("SPEC-21", S3, S3 + "!C31 T2R2-055", "salud 4% (exonerada)", 480000, o("RC06", "salud_trab"))
it("SPEC-22", S3, S3 + "!C34 T2R2-063", "ARL 0,522% = 62.640 -> 62.700", 62700, o("RC06", "arl"))
it("SPEC-23", S3, S3 + "!C35 T2R2-065", "CCF 4%", 480000, o("RC06", "ccf"))
it("SPEC-24", S3, S3 + "!D43", "custo empleador 1.440.000+0+62.700+480.000", 1982700, o("RC06", "pension_emp") + o("RC06", "salud_emp") + o("RC06", "arl") + o("RC06", "ccf") + o("RC06", "sena") + o("RC06", "icbf"))
it("SPEC-25", S3, S3 + "!D37", "valor da exoneracao 114-1 (salud 8,5% + SENA 2% + ICBF 3% de 12M)", 1620000, 12000000 * (0.085 + 0.02 + 0.03))
it("SPEC-26", S3, S3 + "!D21", "teto 25 SMMLV", 43772625, 25 * SMMLV)
S6 = "CO-CESANTIAS-006 Example Analysis"
it("SPEC-27", S6, S6 + "!C5/C21 T14", "base cesantias (1.750.905+249.095)x360/360", 2000000, o("RC12", "cesantias"))
it("SPEC-28", S6, S6 + "!C31", "intereses 12% (IN02)", 240000, o("RC12", "intereses_cesantias"))
it("SPEC-29", S6, S6 + "!D34", "diferenca se omitir aux", 249095, o("RC12", "cesantias") - SMMLV)
# --- Payslip v1.1-DRAFT 'Colombia (EN)'
P = "CO_Compliance_Payslip_Generator-v1.1-DRAFT.xlsx"
PS = "Colombia (EN)"
it("PAY-01", P, PS + "!H34", "salud trabajador 4% x 19.200.000", 768000, o("RC07", "salud_trab_raw"), 0.01)
it("PAY-02", P, PS + "!H35", "pension trabajador 4%", 768000, o("RC07", "pension_trab_raw"), 0.01)
it("PAY-03", P, PS + "!H36 (vazia)", "FSP 1% (IBC 10,97 SMMLV >= 4)", 0, o("RC07", "fsp_solidaridad") + o("RC07", "fsp_subsistencia"), 1, "celula sem valor")
it("PAY-04", P, PS + "!H37 (vazia)", "retencion en la fuente (proc.1)", 0, o("RC07", "ret_valor_retener_raw"), 1, "celula sem valor")
it("PAY-05", P, PS + "!H44", "salud empleador 8,5% (>=10 SMMLV, nao exonerado)", 1632000, o("RC07", "salud_emp_raw"), 0.01)
it("PAY-06", P, PS + "!H45", "pension empleador 12%", 2304000, o("RC07", "pension_emp_raw"), 0.01)
it("PAY-07", P, PS + "!H46 (vazia)", "ARL clase I 0,522%", 0, o("RC07", "arl"), 1, "celula sem valor")
it("PAY-08", P, PS + "!H47 (vazia)", "CCF 4%", 0, o("RC07", "ccf"), 1, "celula sem valor")
it("PAY-09", P, PS + "!H48", "SENA 2%", 384000, o("RC07", "sena_raw"), 0.01)
it("PAY-10", P, PS + "!H49", "ICBF 3%", 576000, o("RC07", "icbf_raw"), 0.01)
it("PAY-11", P, PS + "!H56", "provisao prima 8,33% x 19.200.000", 1599360, o("RC10", "prima"), 1, "taxa truncada 8,33% vs 1/12")
it("PAY-12", P, PS + "!H57", "provisao vacaciones 4,17% x 18.950.000", 790215, o("RC11", "vac_causada"), 1, "taxa 4,17% vs 15/360")
it("PAY-13", P, PS + "!H54/H55 (vazias)", "provisao cesantias (1/12) x 19.200.000", 0, 1600000, 1, "celula sem valor")
it("PAY-14", P, PS + "!H55 (vazia)", "intereses cesantias (12% x 30/360 s/ cesantias)", 0, 19200, 1, "celula sem valor")
it("PAY-15", P, PS + "!I8/H40", "neto a pagar", 17664000, 19200000 - o("RC07", "salud_trab_raw") - o("RC07", "pension_trab_raw") - o("RC07", "fsp_solidaridad_raw") - o("RC07", "fsp_subsistencia_raw") - o("RC07", "ret_valor_retener_raw"), 1)
it("PAY-16", P, PS + "!H50/H67", "total aportes empleador", 4896000, o("RC07", "salud_emp_raw") + o("RC07", "pension_emp_raw") + o("RC07", "arl") + o("RC07", "ccf_raw") + o("RC07", "sena_raw") + o("RC07", "icbf_raw"), 1)

out = []
npass = nfail = 0
for x in items:
    d = abs(float(x["research"]) - float(x["oraculo"]))
    x["delta"] = round(float(x["oraculo"]) - float(x["research"]), 2)
    x["status"] = "PASS" if d <= x["tol"] else "FAIL"
    if x["status"] == "PASS":
        npass += 1
    else:
        nfail += 1
    out.append(x)
json.dump(out, open(HERE + "compare-results.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("itens", len(out), "PASS", npass, "FAIL", nfail)
for x in out:
    if x["status"] == "FAIL":
        print(x["ref"], x["local"][-48:], "|", x["desc"][:50], "| research", x["research"], "| oraculo", round(float(x["oraculo"]), 2), "| d", x["delta"])
