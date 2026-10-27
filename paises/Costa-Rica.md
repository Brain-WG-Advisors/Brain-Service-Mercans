# Costa Rica

> Hub do país. Índice: [[00-INDEX]] · Skill: `payroll-compliance-costarica` · Fronteiras: [[fronteiras]]

## Situação
| Etapa | Status | Data | Observação |
|---|---|---|---|
| [[research-pipeline]] | ✅ | [data?] | skill compilada (pesquisa de agosto/2026 segundo o QA da skill; data exata de compilação não informada) |
| [[design]] | ⏳ | | |
| Produção (outro time) | — | | |
| [[suporte]] | ⏳ | | |

## Ficha do país (da skill)
> Resumo do que mais importa para o serviço. Fonte: skill `payroll-compliance-costarica`, lida em 2026-10-02. Valores exatos e tabelas: ler a skill. Se divergir, vale a skill.

- **Escopo:** ano fiscal 2026, setor privado, CRC. Fora: setor público (salario escolar, anualidades), independentes e asegurados voluntarios; não residentes (art. 59, remesas ao exterior) não construído.
- **Órgãos:** CCSS (cargas sociais, SICERE), DGT/Ministerio de Hacienda (TRIBU-CR), INS/SUGESE (riesgos del trabajo, RT-Virtual), MTSS (salários mínimos, feriados, jornada, rescisão).
- **Relatórios principais:** planilla CCSS/SICERE (mensal, pagar até dia 20); formulário 138 (RFT08, empregador pessoa jurídica) + informativo 208 (mensal, até dia 15; 137/207 pessoa física, 139/209 entes públicos); declaração anual do art. 43 Ley 7092 ao empregado; planilla RT-Virtual (10 dias úteis) e denúncia de acidente (8 dias úteis); relatório salarial semestral MTSS, registro de contratos e Libro de Salarios.
- **Confiança da skill:** PASS WITH NOTES, sem defeito crítico. Núcleo de cálculo primário ou re-derivado. 8 itens abaixo do piso de 95%: BMC 92% (U-1), fração da cesantía 85% (U-2), teto de 8 anos 80% (U-3), layout `.txt` do SICERE 40% (U-14), grades 138/208 45-55% (U-16/U-17), médias trabalhistas de benefícios 70% (U-11), SEM de microempresa 70% (U-21), retenção de registros 55% (U-20). Todo o domínio `ccss.sa.cr` ficou inacessível: valores administrativos da CCSS são DERIVED.

**Armadilhas confirmadas** (correções da skill)
1. Benefícios em espécie e dietas: 15% FIXO sobre o bruto, sem faixa isenta e sem créditos; duas correntes de imposto, nunca mesclar; continuam na base do SICERE (engine) → `01-ccg.md` Step 4
2. Base do IR é o salário BRUTO (cargas CCSS não deduzem); alívio pessoal é CRÉDITO (₡1.710/filho, ₡2.590/cônjuge por mês), não dedução (engine) → `01-ccg.md` Step 3
3. Retroativo é tributado no período em que foi ganho (Ley 10469/2024) e exige retificar as declarações mensais anteriores; precisa da lista de meses (engine) → `01-ccg.md` Step 3-bis
4. D-103 não existe mais (TRIBU-CR desde 2025-10-06); código `103` agora é ISU03, imposto de utilidades de pessoa pública → `03-sir.md` CR-SIR-02
5. Dois prazos mensais em ordem contraintuitiva: IR de salários até dia 15; CCSS/SICERE até dia 20 (engine) → `01-ccg.md` Part VI
6. "26,83% patronal" vale para um perfil só: INA 1,50% só com 5+ trabalhadores permanentes; FODESAF 5% não se aplica abaixo de 1 salario base (₡462.200); zonas francas (Ley 10234); microempresas (engine) → `01-ccg.md` Step 6
7. FCL é 1,50% e ROP 3,00% (trocados pela Ley 9906/2020); total 4,5% igual, o erro aparece na alocação (engine) → `01-ccg.md`
8. Duas Bases Mínimas Contributivas: SEM ₡346.789 e IVM ₡324.590 (2026); ₡333.328/₡311.990 circulam como "2026" mas são de 2024 (engine) → `07-qa-report.md` C-1, U-1
9. Divisor mensal é 30 (Decreto 45303-MTSS art. 7); hora = mensal ÷ 240 (engine) → `01-ccg.md` Part III
10. Aguinaldo: período 1-dez a 30-nov, sem cargas CCSS, isento de IR até 1/12 dos salários do ano; pagar nos primeiros 20 dias de dezembro (engine) → `01-ccg.md`
11. Feriados: em folha mensal já estão no salário; nenhum feriado é movido para segunda em 2026 (engine) → `01-ccg.md` Part III
12. Riesgos del trabalho não é constante: por apólice, teto 16%, até 50% de agravo; taxa vem da apólice (engine) → `01-ccg.md` Step 7
13. Cesantía acumula pela tabela do art. 29(3), base = média dos últimos 6 meses; preaviso e cesantía isentos de IR, compensação de férias tributável → `01-ccg.md` Part IV
14. Não existe payslip estatutário; só a declaração anual (Ley 7092 art. 43, 2 itens). SINALEVI mostra faixas 2025 nos arts. 33-34; valem as do Decreto 45333-H (C-3); faixas de 2026 caíram 0,38% → `06-payslip.md`, `07-qa-report.md` C-3

**O que mais dá errado** (do QA)
- Ordem de risco: (1) tributar benefício em espécie na escala progressiva em vez de 15% fixo; (2) declarar em "D-103" ou no dia 20 em vez do formulário 138 até dia 15; (3) aplicar 26,83% a empregador com menos de 5 permanentes.
- Fontes secundárias: BMC defasada (C-1), fator do ano 6 da cesantía errado (C-4), totais patronais/empregado válidos só para um perfil (C-5), FCL/ROP invertidos (C-6).

**Lacunas abertas / não confirmado** (candidatos a ticket ou nova pesquisa)
- U-2 e U-3 (cesantía): taxa de fração acima de 6 meses (DAJ-AE-083-09 usa o último ano completo) e leitura do teto de 8 anos (167,74 dias); ambiguidade estatutária.
- U-10: conflito entre Ley 7092 art. 35(c) e RLISR art. 48(a) sobre o subsídio de incapacidade da CCSS ser tributável.
- U-14, U-16, U-17, U-19: layouts do `.txt` SICERE, grades 138/208 e Libro de Salarios não obtidos; não apresentar lista de campos como se fosse o formulário.
- U-11 e U-12: benefícios em espécie nas médias de aguinaldo/cesantía/férias; sem tabela de valoração por benefício (a DGT valora).
- U-20 e U-15: sem prazo de guarda de registros; canal atual dos 3 arquivos MTSS incerto.
- Feeds vivos (nunca fixar): tasa básica pasiva do BCCR, as duas BMCs, decreto de salários mínimos (muda no meio do ano), decreto de faixas, salario base, tarifa de RT, circular de feriados.
- Não é lei: jornadas excepcionais 4x3 (Expediente 24.290) não é lei.

**Valores-âncora** (2026; fonte: SKILL.md)
| Item | Valor | A partir de | Fonte |
|---|---|---|---|
| Cargas sociais CCSS/SICERE | empregado 10,83%; patronal 26,83% (perfil padrão) | 2026 | Ley 17; Reglamento del Seguro de Salud art. 62; ver gates acima |
| BMC (SEM / IVM) | ₡346.789 / ₡324.590 | 2026 | derivado de Decreto 45303-MTSS (TONC ₡373.092,30); ⚠️ CCSS inacessível |
| Salario base (Ley 7337) | ₡462.200 | 2026 | citado na skill (Ley 5662 art. 15(b)); ⚠️ norma exata do valor não citada no SKILL.md |
| Faixas e créditos IR salário | ver tabela da skill; crédito filho ₡1.710, cônjuge ₡2.590 por mês | 2026 | Decreto 45333-H (La Gaceta 229, 2025-12-05) |
| IR sobre benefícios em espécie/dietas | 15% fixo sobre o bruto | 2026 | Ley 7092 art. 33(ch); RLISR art. 49 |
| Prazos mensais | IR dia 15; CCSS dia 20 | 2026 | Ley 7092 arts. 31 quinquies, 42; Ley 17 art. 31 |

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
- skill payroll-compliance-costarica (lida em 2026-10-02)
