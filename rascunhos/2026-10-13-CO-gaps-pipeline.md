# Colômbia: gaps do pipeline apontados no e-mail da Cinthya/Manju (2026-10-13)

Origem: e-mail "Review Completed: Colombia Social Security and Income Tax Automation" (Cinthya 13/10 + "Mercans Concepts - PMI.xlsx", 657 WTs do cliente PMI) × `~/mercans-pipeline/CO-compliance/02-wtc/CO-WTC-001-v1.1.xlsx`.

## Já coberto no WTC
Union leave / voto (CO-LIC-REMUNERADA, CST art. 57 num. 6 red. Ley 2466/2025); dependientes, intereses vivienda, medicina prepagada (aba Tax Credit, Classe B, ET arts. 119/387); embargos e cooperativas (CO-DED-EMBARGO, CO-DED-COOPERATIVA, CST 150/154/155/156).

## G1 — Folha de pensionados (aposentados pagos pela empresa)
Escopo não decidido (scope_manifest só tem "employed old-age pensioner in active service"). Decisão do Wallisson/Manju.

## G2 — Incapacidade > 180 dias (CONFIRMADO como gap)
| Aspecto | Regra | Fonte primária |
|---|---|---|
| Dias 1–2 | empregador | Decreto 1406/1999 art. 40 par. 1 (mod. Decreto 2943/2013 art. 1) |
| Dias 3–180 | EPS; 2/3 até dia 90, 1/2 dia 91–180 | CST art. 227; Ley 100/1993 art. 206 |
| Dias 181–540 | AFP, "subsidio equivalente a la incapacidad que venía disfrutando"; se a EPS não emitir conceito de reabilitação (dia 120 / envio dia 150), paga a EPS com recursos próprios | Ley 100/1993 art. 41 (red. Decreto-Ley 019/2012 art. 142) |
| Dia 541+ | EPS (ADRES) | Ley 1753/2015 art. 67 |
| Fluxo | Colpensiones paga ao afiliado ou terceiro autorizado por escrito | colpensiones.gov.co "Determinación del subsidio por incapacidad" (mod. 22/01/2024) |
| Contribuições | salud e pensión continuam; IBC = valor da incapacidade; autoliquidação pelo empregador (PILA) | Decreto 780/2016 art. 3.2.1.10 (= Decreto 1406/1999 art. 40); MinSalud 202211600074851 (18/01/2022) |
| Tributação | incapacidades NÃO são renda exenta; retenção aplica | DIAN Oficio 27408 de 01/11/2019 |
| Férias/cesantías | período conta (incapacidade não é suspensão; art. 53 só desconta suspensões do art. 51) | CST arts. 51 (red. Ley 50/1990 art. 4) e 53 |

### Os 3 pontos abertos (fechados em 2026-10-13, fonte primária lida)
| Ponto | Regra | Fonte primária |
|---|---|---|
| Salud do empregador nos dias 181–540 | Não há regra especial por quem paga o subsídio: art. 3.2.1.10 vale para "los períodos de incapacidad por riesgo común". Salud 12,5% (8,5% empregador / 4% empregado) sobre IBC = valor da incapacidade, nunca abaixo do mínimo legal. A exoneração do ET art. 114-1 (empregado com menos de 10 SMMLV) segue valendo normalmente. | Decreto 780/2016 art. 3.2.1.10 (texto Función Pública, lido); Ley 100/1993 art. 204 (red. Ley 1122/2007 art. 10); ET art. 114-1 (Ley 1819/2016 art. 65) |
| Prima de servicios | Os dias de incapacidade **contam** como tempo para prima (e cesantías/vacaciones): incapacidade não é suspensão (art. 51 taxativo); descontar seria equipará-la a suspensão. A jurisprudência não distingue pela duração da incapacidade. | CST art. 306 (red. Ley 1788/2016); CST arts. 51 e 53; CSJ SL588-2024, citada e transcrita na CSJ SL1659-2025 (26/03/2025, pp. 25–26), que reitera SL 30/01/2013 rad. 41867 e SL 15/04/1997 rad. 9119 |
| Base das prestações | Salário fixo: último salário mensal (art. 253). Salário variável: a média só considera os tempos efetivamente remunerados com salário, ou seja, **exclui o período de incapacidade** da média, mas os dias entram na contagem. ⚠️ Ressalva: na parte de casação (p. 26), a mesma SL1659-2025 fala em incluir "la retribución devengada en ese tiempo"; a regra acima está na sentença de instância (p. 28). | CST art. 253 (red. DL 2351/1965 art. 17); CSJ SL1659-2025 p. 28 |

Não confirmado em fonte oficial (só reprodução secundária, gydconsulting/accounter): Mintrabajo 08SE2023120300000055767 (rad. 05EE2022745400100002128), sobre incapacidade acima de 180 dias, diz que as prestações seguem e que se usa o "último salario percibido antes del inicio de su incapacidad". Mintrabajo não publica o texto. Fica fora como fonte, mas está alinhado com o que foi acima.
Fontes salvas: `raw/docs/oficiais/CO/2026-10-13-CSJ-SL1659-2025.pdf`, `raw/docs/oficiais/CO/2026-10-13-TSMedellin-05001310501120200000201.pdf`.
Conceitos da Função Pública sobre o tema NÃO servem (Decreto 1045/1978 = setor público).

### Correção candidata no WTC atual
CO-INCAP-EG-EPS diz "Exempt within the statutory minimum (ET art. 206 nums. 1-2 and par. 1)" — conflita com DIAN Oficio 27408/2019. Revisar também CO-INCAP-EG-EMPLEADOR e CO-INCAP-IRL. Nada aplicado.

## G3 — Jurado / eleitor (CONCLUÍDO — gap pequeno)
| Item | Regra | Fonte primária |
|---|---|---|
| Eleitor | meia jornada de descanso compensatório remunerado, no mês seguinte à votação, de comum acordo | Ley 403/1997 art. 3 (sem nota de modificação no artigo) |
| Jurado (e claveros/escrutadores, C-1005/2007) | 1 dia compensatório remunerado nos 45 dias seguintes | Decreto 2241/1986 (Código Electoral) art. 105 |
| Parafiscales | entra ("descansos remunerados de ley") | Ley 21/1982 art. 17 (via Consejo de Estado 2027/2010) |
| Retenção | tributável (não listado no ET art. 206) | leitura direta |
WTC hoje: CO-LIC-REMUNERADA cobre só o dia da votação (CST 57 num. 6). Proposta: acrescentar Ley 403 art. 3 e CE art. 105 à mesma linha. IBC/base prestacional herdados da linha atual (não reverificados).

## G4 — 8 relatórios manuais (CONCLUÍDO — papel nosso = dizer se é statutory)
| Relatório | Statutory? | Base |
|---|---|---|
| Contingent Withholding Report | SIM — NÃO coberto (gap) | DUR 1625/2016 arts. 1.2.1.22.42 e 1.2.4.1.12 (red. Decreto 2250/2017): empregador informa ao fundo beneficiário e valor da retención contingente (AFC/AVC: diferença retenção sem aporte × retenção efetiva) |
| CARGA MASIVA AFC | obrigação = mesma acima (depósito direto + informe); FORMATO do arquivo não é nosso (Implementation/Integration) | idem |
| Severance Massive Calculation | coberto | CO-CESANTIAS-006 |
| Detail IBC per Employee | coberto | CO-PILA-003 |
| Base of Withholding | coberto em conteúdo (F350/NE/F220); nenhuma norma exige relatório separado encontrada | CO-DIAN-001/002/004 |
| Leave Absence, Loans Balance, CONSOLIDADACCT | não statutory (controle do cliente) — não investigar | fronteiras.md |
Pipeline CO: zero ocorrências de "contingent", "AFC", "pensiones voluntarias" no scope_manifest.

## Ajuste de escopo (2026-10-13)
- M1 CANCELADO (usuário, 2026-10-13): qualquer cruzamento dos 657 códigos do cliente com o master WTC é mapeamento e não é nosso, nem na versão restrita (fronteiras.md: WTC do cliente = cliente/team lead; mapeamento = Config/Product). Agente interrompido. Nossos gaps saem só da leitura da lei e do que a Cinthya/Manju apontaram por escrito.
- Fluxo de pagamento em fundos privados (G2) sai: operação, não regra legal.

## Plano completo
- G4: classificar os 8 relatórios (obrigação legal × cliente).
- C1: corrigir tributação CO-INCAP-EG-EMPLEADOR / -EG-EPS / -IRL (DIAN 27408/2019).
- C2: nova linha incapacidade dia 181+ (após fechar abertos do G2).
- C3: Ley 403/CE 105 na CO-LIC-REMUNERADA.
- C4: retención contingente (AFC/FVP) — pesquisa → CCG, SIR e escopo (obrigação do empregador sem cobertura).
- D1: decisão escopo pensionados (G1).
- Externo: revisão CCG/SIR pela Cinthya.
Correções em CO-WTC-001-v1.2, só com aprovação.
