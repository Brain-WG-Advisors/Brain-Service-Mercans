# Tchéquia

> Hub do país. Índice: [[00-INDEX]] · Skill: `payroll-compliance-czechia` · Fronteiras: [[fronteiras]]

## Situação
| Etapa | Status | Data | Observação |
|---|---|---|---|
| [[research-pipeline]] | ✅ | [data?] | skill compilada (data da pesquisa não aparece nos trechos lidos) |
| [[design]] | ⏳ | | |
| Produção (outro time) | — | | |
| [[suporte]] | ⏳ | | |

## Ficha do país (da skill)
> Resumo do que mais importa para o serviço. Fonte: skill `payroll-compliance-czechia`, lida em 2026-10-02. Valores exatos e tabelas: ler a skill. Se divergir, vale a skill.

- **Escopo:** ano-calendário 2026, setor privado (pracovní poměr, DPP, DPČ), CZK. Fora: servidores (Lei 234/2014), militares profissionais, forças de segurança (só a partir de 2027), OSVČ (autônomos), regime de `plat` do setor público. Não pesquisada a taxa de seguro de responsabilidade do empregador (vyhl. 125/1993 Sb.).
- **Órgãos:** ČSSZ, Finanční správa ČR, as sete zdravotní pojišťovny, MPSV, SÚIP.
- **Relatórios principais:** JMHZ (jednotné měsíční hlášení zaměstnavatele, Lei 323/2025, janela dias 1–20 do mês seguinte, via VREP/APEP no ČSSZ); registros de empregador/empregado com novo OIČ (via ISDS ou ePortál); PPZ (dia 20) e HOZ (8 dias; dia 20 para só DPP/DPČ) a cada uma das sete seguradoras de saúde, só eletrônico desde 1 jan 2026; Vyúčtování daně (roční zúčtování); calendário de conformidade em `04-reports-spec.md`.
- **Confiança da skill:** "PASS WITH NOTES", 0 defeitos críticos no build, 9 itens abertos abaixo do piso de 95% (nenhum muda taxa ou limite de 2026). `01-ccg.md` 96%, `02-wtc.md` 94%, `03-sir.md` 91%, `04-reports-spec.md` 90%, `05-data-dictionary.md` 92%, `06-payslip.md` 97%. DERIVED: layouts PPZ/HOZ (~70%) e boxes do Vyúčtování (~65%). Dois defeitos críticos em artefatos Mercans PRÉ-EXISTENTES (documentados, não propagados).

**Armadilhas confirmadas**
1. Um só flag de tributabilidade comanda as três sujeições (taxable ⇒ contributivo), com uma exceção relevante: odstupné = IR sim, SI não, HI não (engine) → `01-ccg.md`, `02-wtc.md`
2. Odstupné legal é TRIBUTÁVEL; o código 62910 do catálogo Mercans V2.0 tem `Subject to Tax = No`, o que está ERRADO e sub-retém ~meio mês de bruto por desligado; deve sair da base anual antes de comparar com o teto (engine) → `02-wtc.md`, QA §3.1
3. Teto de seguridade social é anual e cumulativo (48 × salário médio = 2 350 416 Kč); não dividir por 12; com um empregador, ultrapassar para empregado (7,1%) E empregador (24,8%); com vários, todos continuam e só o empregado recupera mediante pedido escrito; saúde (13,5%) não tem teto (engine) → `01-ccg.md` §3.4, §5.9
4. Trabalho de risco é 27,8% em 2026 (rampa 26,8→27,8→28,8→29,8); 29,8% é de paramédicos e bombeiros de empresa; § 5a(3) tira do bucket elevado o mês em que há contribuição de poupança de Lei 324/2025 (engine) → `01-ccg.md`
5. Arredondamentos conflitantes: base do adiantamento arredonda PARA CIMA a centenas; retenção na fonte e imposto PARA BAIXO em coroas; base anual PARA BAIXO a centenas; a soma dos adiantamentos não reproduz o imposto anual (engine) → `01-ccg.md` §12
6. Sem super-gross (abolido 1 jan 2021): base do adiantamento é a renda contabilizada do mês, sem deduzir contribuições do empregado nem somar as do empregador (engine) → `01-ccg.md`
7. Ordem de créditos: § 35ba pessoais primeiro, limitados ao adiantamento; só o benefício infantil § 35c vira bônus em dinheiro (≥50 Kč e renda mensal ≥11 200 Kč do empregador); crédito do cônjuge só anual; não residente só o crédito básico (engine) → `01-ccg.md`
8. Complemento da base mínima de saúde (salário mínimo 22 400 Kč) é do empregado, exceto se a falta vier de obstáculo do empregador (§ 207–209 ZP), aí o empregador paga; fácil codificar ao contrário (engine) → `01-ccg.md`
9. Limites de redução do salário-doença do empregador são POR HORA (× 0,175; 2026 = 285,78 / 428,58 / 856,98 Kč/h); diários 1 633 / 2 449 / 4 897 são da ČSSZ do dia 15 em diante; a aba de doença do catálogo Mercans usa diários de 2025 e paga a mais (engine) → `01-ccg.md`, `02-wtc.md`
10. JMHZ enviado antes do dia 1 é defeito técnico e INEFICAZ; multa 5 000 Kč × nº de empregados registrados, sem teto (Lei 323/2025 § 10, § 28(2)(d)) → `04-reports-spec.md`
11. Seguro de saúde fica TOTALMENTE fora do JMHZ: PPZ e HOZ vão a cada seguradora; atributos 10371 e 10482 do JMHZ não quitam nada com os seguros → `04-reports-spec.md`, `03-sir.md`
12. Três identificadores novos atribuídos pelo Estado, não deriváveis: OIČ (MPSV, um por pessoa), identificador de emprego/IDPPV (ČSSZ, um por vínculo), variabilní symbol (empregador e cada mzdová účtárna); o DD Mercans V2.0 não tem nenhum e também não tem código de estado de residência fiscal (engine/dados) → `05-data-dictionary.md`
13. Contribuição obrigatória de 4% de poupança para aposentadoria (trabalho de categoria 3) conta dentro do teto isento de 50 000 Kč (§ 6(9)(m) ZDP); exige opt-in e ≥3 turnos de risco no mês; definição de categoria 3 mais estreita (engine) → `01-ccg.md`
14. M2M no ČSSZ (VREP/APEP: POX submission + poll, WS, envelope GovTalk, assinatura qualificada), mas § 8(1)(c) Lei 323/2025 exclui os deveres do registro de empregador (§ 17), que vão por ISDS/ePortál; seguradoras e Finanční správa são portal → `03-sir.md`
15. Zaručená mzda não existe mais no privado (só salário mínimo); trabalho em feriado não gera 100% automático (§ 115: folga é padrão, adicional só se acordado); adicional de ambiente penoso é % do salário mínimo → `01-ccg.md`

**O que mais dá errado** (do QA)
- Catálogo Mercans `_CZ_Wage_Type_Catalogue_V2_0.xlsx`: 10 defeitos (`02-wtc.md` §6), incluindo o 62910 (sev. tributável) e a aba de doença com valores diários de 2025.
- DD Mercans `CZ_Data_Dictionary_V2_0.xlsx` (liberado em 2025-09-08, antes do go-live do JMHZ): 8 lacunas, 6 bloqueantes para 2026: sem OIČ; sem identificador de emprego; sem variabilní symbol; `hr.tax_residency` é status de 3 valores e não código de estado ISO (maior causa de falha no go-live de 1 abr 2026 segundo a Finanční správa, empregadores confundem com cidadania); mapper de seguradora omite 211 ZPMV; `legal_entity.er_tin` (DIČ) marcado obrigatório duro (empregadores sem outro registro perderam o DIČ em 1 abr 2026).
- Citar o 2025 em vez do 2026 (ano de mudança grande: JMHZ, registros no ČSSZ, poupança obrigatória, novo desconto de empregado, degrau do trabalho de risco, nova fórmula de valor impenhorável); ver `01-ccg.md` §15.

**Lacunas abertas / não confirmado** (candidatos a ticket ou nova pesquisa)
- §5.3 (~75%): estrutura de DADOS do JMHZ (XSD, tipos, tamanhos, enumerações) não obtida; só o conteúdo. Não é possível implementar só com a skill; precisa da datová věta e do Podávací a dotazovací protokol do ČSSZ. Maior lacuna conhecida.
- §3.2 (~60%): tratamento contributivo de odstupné ACIMA do mínimo legal é leitura não pacificada de § 5(2)(b) ZPSZ; sinalizar ao cliente, não escolher lado.
- §3.3 (~50%): taxa do seguro de responsabilidade do empregador (vyhl. 125/1993 Sb.).
- §4.1 (~70%): interfaces de dados das sete seguradoras (só VZP examinada); §5.1: PPZ/HOZ derivados.
- §4.2 (~85%): mecânica de envio à Finanční správa; §5.2 (~65%): boxes do Vyúčtování (obter PDFs de 2026).
- Futuro, não implementar: fim do Vyúčtování a partir de 2027; abolição da srážková daň (~40%, rumor); remoção do dever de reportar isentos no JMHZ (previsto para 1 jan 2027, tolerância administrativa em 2026).
- Valores de option mappers parcialmente reconstruídos (§5.4).
- Ações recomendadas pela skill (em ordem): obter documentação técnica do ČSSZ; corrigir as 6 lacunas bloqueantes do DD; corrigir o 62910 para Tax = Yes; obter decisão sobre odstupné; coletar specs PPZ/HOZ das 7 seguradoras; obter PDFs do Vyúčtování 2026.

**Valores-âncora**
| Item | Valor | A partir de | Fonte |
|---|---|---|---|
| Seguridade social (ČSSZ) | empregado 7,1% / empregador 24,8% (27,8% trabalho de risco; 29,8% paramédicos e bombeiros) | 2026-01-01 | ZPSZ § 7(1), § 5a(1)(b) |
| Teto anual de SS | 2 350 416 Kč (48 × 48 967 Kč) | 2026-01-01 | ZPSZ § 15a(1) |
| Seguro de saúde | 13,5% (4,5 empregado / 9,0 empregador), sem teto; base mínima = salário mínimo 22 400 Kč | 2026-01-01 | ZPVZP § 3(10) |
| Imposto de renda | 15% / 23% acima de 3× o salário médio mensal; sem super-gross | 2026-01-01 | ZDP |
| Janela do JMHZ | dias 1 a 20 do mês seguinte; multa 5 000 Kč × empregados | 2026-01-01 | Lei 323/2025 § 7(1), § 28(2)(d) |
| Limites horários do salário-doença do empregador | 285,78 / 428,58 / 856,98 Kč/h | 2026-01-01 | ZP § 192(2) |

## Artefatos entregues
| Artefato | Versão | Data | Arquivo/local | Observação |
|---|---|---|---|---|
| | | | | |

## Valores-chave (com vigência)
| Item | Valor | A partir de | Até | Fonte |
|---|---|---|---|---|
| | | | | |

## Decisões
- 

## Suporte (tickets)
| Data | Ticket | Assunto | Resolução | Mudou artefato? |
|---|---|---|---|---|
| | | | | |

## Pendências
- [ ]

## Correções ligadas
- _(links para entradas de [[correcoes]])_

## Fontes
- skill payroll-compliance-czechia (lida em 2026-10-02)
