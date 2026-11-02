# Gera params.json: cada parametro = value + effective + source (arquivo local + artigo). Fonte: SO a lei em raw/docs/oficiais/CO.
import json
D = "raw/docs/oficiais/CO/"


def p(v, eff, src, gap=None, note=None):
    d = {"value": v, "effective": eff, "source": src}
    if gap:
        d["source_gap"] = gap
    if note:
        d["note"] = note
    return d


P = {
    "SMMLV_2026": p(1750905, "2026-01-01", "ancora fornecida pelo usuario (decreto anual do salario minimo; nao ha copia local do decreto)", gap="decreto do SMMLV 2026 nao esta em raw/docs/oficiais/CO; valor dado como ancora"),
    "UVT_2026": p(52374, "2026-01-01", "ancora fornecida pelo usuario (Res. DIAN UVT 2026; nao local)", gap="resolucao DIAN da UVT 2026 nao local; valor dado como ancora"),
    "AUX_TRANSPORTE_2026": p(249095, "2026-01-01", "ancora fornecida pelo usuario (decreto anual; nao local)", gap="decreto auxilio 2026 nao local"),
    "AUX_TRANSPORTE_TETO_SMMLV": p(2, "2026-01-01", D + "2026-10-22-CSJ-Sentencia-2994-1989-auxilio-transporte-FuncionPublica.pdf (natureza); regra 'hasta 2 SMMLV' = Ley 15/1959 e decretos anuais", gap="limite de 2 SMMLV nao verificado em texto local; criterio de borda: <= 2 SMMLV recebe"),
    "DIAS_MES_NOMINA": p(30, "all", "pratica 30/360 (CST art. 134 pagos por periodos; base de 30 dias)", gap="base 30 dias convencional"),
    "DIVISOR_HORA": p([{"from": "2025-07-15", "value": 220}, {"from": "2026-07-15", "value": 210}], "2025-07-15; 2026-07-15", D + "2026-10-22-CST-pr005-SecretariaSenado.html art. 161 (Ley 2466/2025 art. 11): 'sin perjuicio de lo establecido en el articulo 3o de la Ley 2101 de 2021 sobre la aplicacion gradual, y una jornada maxima de cuarenta y dos (42) horas a la semana'", gap="Ley 2101/2021 art. 3 (44h desde 2025-07-15, 42h desde 2026-07-15) nao esta local; divisor = h_sem/6*30 (44->220; 42->210) derivado aritmeticamente; datas conforme instrucao do usuario"),
    "REC_DOMINICAL": p([{"from": "2025-07-01", "value": 0.80}, {"from": "2026-07-01", "value": 0.90}, {"from": "2027-07-01", "value": 1.00}], "2025-07-01; 2026-07-01; 2027-07-01", D + "2026-10-21-CST-pr006-SecretariaSenado.html art. 179 (Ley 2466/2025 art. 14) PARAGRAFO TRANSITORIO: 'A partir del primero de julio de 2025 ... 80%. A partir del primero de julio de 2026 ... 90%. A partir del primero de julio de 2027 ... plena aplicacion'"),
    "REC_NOCTURNO": p(0.35, "1990-12-28", D + "2026-10-22-CST-pr005 art. 168 num.1 (Ley 50/1990 art. 24): recargo nocturno 35%"),
    "REC_EXTRA_DIURNA": p(0.25, "1990-12-28", D + "2026-10-22-CST-pr005 art. 168 num.2: extra diurno 25%"),
    "REC_EXTRA_NOCTURNA": p(0.75, "1990-12-28", D + "2026-10-22-CST-pr005 art. 168 num.3: extra nocturno 75%"),
    "NOCTURNO_INICIO_HORA": p(19, "2026-06-15 (6 meses apos sancion Ley 2466)", D + "2026-10-22-CST-pr005 art. 160 (Ley 2466 art.10): nocturno entre 19:00 y 06:00; par.2 vigencia 6 meses despues de sancion", note="so classificacao; casos informam horas ja classificadas"),
    "IBC_MIN_SMMLV": p(1, "all", D + "2026-10-21-Ley-797-2003 art. 5 (art. 18 Ley 100): 'En ningun caso el ingreso base de cotizacion podra ser inferior a un salario minimo'"),
    "IBC_MAX_SMMLV": p(25, "all", D + "2026-10-21-Ley-797-2003 art. 5 (art. 18 Ley 100): 'limite de la base de cotizacion sera de veinticinco (25) salarios minimos'"),
    "INTEGRAL_IBC_PCT": p(0.70, "all", D + "2026-10-21-Ley-797-2003 art. 5: 'salario integral, se calculara sobre el 70%'; Decreto 780/2016 art. 2.2.1.1.2.1 idem"),
    "INTEGRAL_MIN_SMMLV": p(13, "all", D + "2026-10-22-Ley-50-1990 art. 18 (CST art. 132 num.2): salario ordinario superior a 10 SMMLV + factor prestacional 30% => 13 SMMLV", note="10 + 30% factor prestacional"),
    "NOSALARIAL_MAX_PCT": p(0.40, "2010-12-23", D + "2026-10-21-Ley-1393-2010 art. 30: 'pagos laborales no constitutivos de salario ... no podran ser superiores al 40% del total de la remuneracion'"),
    "SALUD_TOTAL": p(0.125, "2007-01-01", D + "2026-10-13-Decreto-780-2016 art. 2.2.1.1.2.1 ('12,5% de un salario minimo'); reparto 4%/8,5% = Ley 1122/2007 art. 10", gap="texto da Ley 1122/2007 art.10 nao local; 4% trabajador / 8,5% empleador tomado da ley, confirmar"),
    "SALUD_TRAB": p(0.04, "2007-01-01", "idem", gap="Ley 1122 art.10 nao local"),
    "SALUD_EMP": p(0.085, "2007-01-01", "idem", gap="Ley 1122 art.10 nao local"),
    "PENSION_TOTAL": p(0.16, "2008-01-01", D + "2026-10-21-Ley-797-2003 art. 7 (art. 20 Ley 100): 13,5% + 1% (2004) + 0,5% + 0,5% (2005/2006) + 1% adicional (2008) = 16%; empleador 75% / trabajador 25%", note="texto local da 15,5% + 'podra' 1% (Decreto 4982/2007 nao local)", gap="Decreto 4982/2007 nao local"),
    "PENSION_EMP_SHARE": p(0.75, "all", D + "2026-10-21-Ley-797-2003 art. 7: 'Los empleadores pagaran el 75% de la cotizacion total y los trabajadores el 25% restante'"),
    "FSP_SOLIDARIDAD": p(0.005, "2003-01-29", D + "2026-10-21-Ley-797-2003 art. 7 y art. 8 (art. 27 Ley 100): 1% a partir de 4 SMMLV, 50% subcuenta solidaridad; AT2 v30 campo 51: 'multiplicar ... por 0.5%'"),
    "FSP_SUBSISTENCIA_BASE": p(0.005, "2003-01-29", D + "2026-10-21-Ley-797-2003 art. 8 num.2 b): 'El cincuenta (50%) de la cotizacion adicional del 1%'; AT2 v30 campo 52"),
    "FSP_SUBSISTENCIA_TRAMOS": p([{"gt": 16, "le": 17, "extra": 0.002, "incl_lower": True}, {"gt": 17, "le": 18, "extra": 0.004}, {"gt": 18, "le": 19, "extra": 0.006}, {"gt": 19, "le": 20, "extra": 0.008}, {"gt": 20, "le": 999, "extra": 0.010}], "2003-01-29", D + "2026-10-29-MinSalud-AT2-v30 campo 52: 'Igual a 16 hasta 17 0.2% / Mayor a 17 hasta 18 0.4% / Mayor a 18 hasta 19 0.6% / Mayor a 19 hasta 20 0.8% / Mayor a 20 1.0%' (Ley 797 art. 8)", note="limite inferior 16 inclusivo; (17,18] etc. Adicional al 0,5% base"),
    "FSP_N_REGIME_AT2": p("PENDENTE", "2025-07-01", D + "2026-10-29-MinSalud-AT2-v30 campo 52 (cotizante 'N' em campo 5): 4-7: 1.0%; 7-11: 1.3%; 11-19: 2.0%; 19-20: 2.3%; >=20: 2.5% (Ley 2381/2024 art. 20)", note="regime alternativo; vigencia/eficacia da Ley 2381 nao resolvida => casos PENDENTE"),
    "FSP_MIN_SMMLV": p(4, "2003-01-29", D + "2026-10-21-Ley-797-2003 art. 7: 'ingreso mensual igual o superior a cuatro (4) salarios minimos' (inclusivo)"),
    "EXONERACION_LIMITE_SMMLV": p(10, "2017-01-01", D + "2026-10-22-ET-pr004-SecretariaSenado.html art. 114-1 (Ley 1819/2016 art. 65): exoneradas SENA, ICBF y salud empleador 'trabajadores que devenguen ... menos de diez (10) salarios minimos' (estrictamente menor)"),
    "CCF": p(0.04, "1982", D + "2026-10-13-Ley-21-1982-SENA.htm art. 7 (4% subsidio familiar)"),
    "SENA": p(0.02, "1982", D + "2026-10-13-Ley-21-1982-SENA.htm art. 7 (2% SENA)"),
    "ICBF": p(0.03, "1988", D + "2026-10-22-Ley-89-1988-ICBF.pdf art. 1 (3% ICBF)"),
    "ARL": p({"I": 0.00522, "II": 0.01044, "III": 0.02436, "IV": 0.04350, "V": 0.06960}, "1994-06-22", D + "2026-10-13-Decreto-1072-2015 art. 2.2.4.3.2 (tabla de cotizaciones, valor inicial): I 0.522%, II 1.044%, III 2.436%, IV 4.350%, V 6.960%"),
    "PILA_REDONDEO": p("peso, half-up (2 decimales)", "2026-07-24", D + "2026-10-29-MinSalud-AT2-v30 campo 47: 'redondearse al peso ... si el valor es igual o superior a .50, se debe aproximar al peso superior'"),
    "PILA51_BANDAS": p([{"d_min": 1, "d_max": 7, "cuartos": 1}, {"d_min": 8, "d_max": 14, "cuartos": 2}, {"d_min": 15, "d_max": 21, "cuartos": 3}, {"d_min": 22, "d_max": 30, "cuartos": 4}], "2026-07-24", D + "2026-10-29-MinSalud-AT2-v30 tipo cotizante 51 ('Entre 1 y 7 dias Un cuarto de un SMMLV ... Entre 22 y 30 dias Un SMMLV'); ARL: 30 dias, IBC = 1 SMMLV; CCF mismas bandas"),
    "IBC_INCAPACIDAD": p("valor de la incapacidad (min 1 SMMLV)", "all", D + "2026-10-13-Decreto-780-2016 art. 3.2.1.10: 'se tomara como Ingreso Base de Cotizacion el valor de la incapacidad o licencia de maternidad'; 'en ningun caso ... inferior a las bases minimas'"),
    "INC_COMUN": p([{"d_from": 1, "d_to": 2, "pct": 0.6667, "payer": "empleador"}, {"d_from": 3, "d_to": 90, "pct": 0.6667, "payer": "EPS"}, {"d_from": 91, "d_to": 180, "pct": 0.50, "payer": "EPS"}], "all", D + "2026-10-22-CST-pr007 art. 227 (2/3 primeros 90 dias; 1/2 el tiempo restante hasta 180) + Decreto 780/2016 art. 3.2.1.10 par.1 (2 primeros dias empleador; desde el tercero EPS)", note="piso SMLDV => PENDENTE; 2/3 usado como 66,67% exato (2/3)"),
    "MATERNIDAD_SEMANAS": p(18, "2021-06-30", D + "2026-10-22-CST-pr007 art. 236 num.1: 'licencia de dieciocho (18) semanas ... remunerada con el salario que devengue'"),
    "VACACIONES_DIAS_HABILES": p(15, "all", D + "2026-10-21-CST-pr006 art. 186 num.1: quince (15) dias habiles por ano"),
    "VACACIONES_COMPENSABLE_MAX": p(0.5, "2010-12-29", D + "2026-10-21-CST-pr006 art. 189 num.1: 'hasta la mitad de las vacaciones'"),
    "VACACIONES_BASE": p("salario ordinario, sin extras ni trabajo en descanso, sin auxilio", "all", D + "2026-10-21-CST-pr006 art. 192 num.1 ('solo se excluiran ... el valor del trabajo en dias de descanso obligatorio y el valor del trabajo suplementario')"),
    "PRIMA_DIAS_POR_ANO": p(30, "all", "CST art. 306: 30 dias de salario por ano, pagaderos 15 dias por semestre (30 jun / 20 dic); base salario + auxilio de transporte", gap="CST arts. 249-253 y 306 no estan en la carpeta local; regla cargada del texto legal conocido"),
    "CESANTIA_DIAS_POR_ANO": p(30, "all", "CST art. 249 (un mes por ano, base 360 dias) + Ley 50/1990 art. 99 num.1 (liquidacion 31-dic)", gap="art. 249 no local; art. 99 local (liquidacion anual)"),
    "INTERES_CESANTIA": p(0.12, "all", D + "2026-10-22-Ley-50-1990-FuncionPublica.pdf art. 99 num.2: 'intereses legales del 12% anual o proporcionales por fraccion'; Ley 52/1975 (no local)", gap="Ley 52/1975 no local; art. 99 local conferido"),
    "INDEMNIZACION_ART64": p({"lt10": {"first_year_days": 30, "add_per_year": 20}, "ge10": {"first_year_days": 20, "add_per_year": 15}}, "2002-12-27", D + "2026-10-22-CST-pr001-SecretariaSenado.html art. 64 (Ley 789/2002 art. 28): <10 SMMLV: 30 dias + 20 por ano subsiguiente; >=10 SMMLV: 20 dias + 15 por ano"),
    "RET_TABLA_383": p([[0, 95, 0.0, 0], [95, 150, 0.19, 0], [150, 360, 0.28, 10], [360, 640, 0.33, 69], [640, 945, 0.35, 162], [945, 2300, 0.37, 268], [2300, 10 ** 9, 0.39, 770]], "2020-01-01", D + "2026-10-13-DUR-1625-2016-DIAN.htm art. 1.2.4.1.17 (tabla ET 383, Decreto 359/2020): '>0 95 0,0% / >95 150 19% / >150 360 28% mas 10 UVT / >360 640 33% mas 69 / >640 945 35% mas 162 / >945 2300 37% mas 268 / >2300 39% mas 770'", note="intervalos abiertos a la izquierda: base == 95 UVT => 0; formato [desde, hasta, marginal, UVT fijas]"),
    "RET_PROC1": p("tabla aplicada al total de pagos gravables del mes", "all", D + "2026-10-13-DUR-1625-2016 art. 1.2.4.1.3 Procedimiento 1; par.2 art. 1.2.4.1.6 'totalidad de los pagos ... en el respectivo mes'"),
    "RET_DEP_PCT": p(0.10, "2017-12-29", D + "DUR 1625 art. 1.2.4.1.6 num.4.3: deduccion dependientes hasta 10% del total de la renta, maximo 32 UVT mensuales"),
    "RET_DEP_MAX_UVT": p(32, "2017-12-29", "idem"),
    "RET_PREPAGADA_MAX_UVT": p(16, "2017-12-29", D + "DUR 1625 art. 1.2.4.1.6 num.4.2: pagos por salud ... no supere 16 UVT mensuales"),
    "RET_VIVIENDA_MAX_UVT": p(100, "2020-01-01", D + "DUR 1625 art. 1.2.4.1.23: 'sin que exceda de cien (100) UVT mensuales'"),
    "RET_AFC_PCT": p(0.30, "2012-01-01", D + "DUR 1625 art. 1.2.1.22.41 / 1.2.1.22.43: AVP+AFC hasta 30% del ingreso laboral y 3.800 UVT/ano"),
    "RET_AFC_MAX_UVT_ANO": p(3800, "2012-01-01", "idem"),
    "RET_CAP_PCT": p(0.40, "2023-01-01", D + "2026-10-22-ET-pr014 art. 336 num.3 (Ley 2277/2022 art. 7): 'no excedan el cuarenta (40%) del resultado del numeral anterior, que en todo caso no puede exceder de mil trescientas cuarenta (1.340) UVT anuales'; DUR 1.2.4.1.6 par.3"),
    "RET_CAP_UVT_ANO": p(1340, "2023-01-01", "idem", note="mensual = 1340/12 (prorrateo mensual: criterio del oraculo)"),
    "RET_EXENTA25_PCT": p(0.25, "2023-01-01", D + "2026-10-22-ET-pr008 art. 206 num.10 (Ley 2277/2022 art. 2): 'El veinticinco por ciento (25%) del valor total de los pagos laborales limitada anualmente a setecientos noventa (790) UVT. El calculo ... una vez se detraiga ... los ingresos no constitutivos de renta, las deducciones y las demas rentas exentas'"),
    "RET_EXENTA25_UVT_ANO": p(790, "2023-01-01", "idem", note="mensual = 790/12 = 65,83 UVT (criterio del oraculo)"),
    "RET_DEP_72UVT": p("PENDENTE", "2023-01-01", D + "ET 336 num.3 inc.2 (72 UVT por dependiente, max 4, adicional al limite 40%/1340) - ver declaracion anual; efecto na retencion mensual no resuelto en copia local"),
}
json.dump(P, open("params.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(P), "params")
