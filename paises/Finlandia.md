---
tipo: pais
codigo: "FI"
etapa_research: "concluida"
etapa_research_data: 2026-08-28
etapa_design: "aguardando"
etapa_design_data: 
etapa_producao: 
etapa_suporte: "sem ticket no hub"
etapa_suporte_data: 
ccg: 
ccg_data: 
wtc: 
wtc_data: 
dd: 
dd_data: 
report_specs: 
report_specs_data: 
sir: 
sir_data: 
payslip: 
skill: "payroll-compliance-finland"
tickets_abertos: 
tickets_conferidos_em: 
atualizado_em: 2026-10-27
---
# Finlândia

> Hub do país. Índice: [[00-INDEX]] · Skill: `payroll-compliance-finland` · Fronteiras: [[fronteiras]]

## Situação
| Etapa | Status | Data | Observação |
|---|---|---|---|
| [[research-pipeline]] | ✅ | 2026-08-28 | skill compilada (build do zero; data da pesquisa no QA da skill) |
| [[design]] | ⏳ | | |
| Produção (outro time) | — | | |
| [[suporte]] | ⏳ | | |

## Ficha do país (da skill)
> Resumo do que mais importa para o serviço. Fonte: skill `payroll-compliance-finland`, lida em 2026-10-02. Valores exatos e tabelas: ler a skill. Se divergir, vale a skill.

- **Escopo:** ano fiscal 2026, setor privado, EUR. Åland em escopo com divergências sinalizadas (taxas municipais de Åland não obtidas). Fora: JuEL/Keva, Banco da Finlândia e esquemas da igreja, defesa, marítimos (Merimieseläkelaki), autônomos (YEL), agricultores (MYEL), light entrepreneurs. Acordos coletivos (203 setoriais) são camada não construída.
- **Órgãos:** Verohallinto, Tulorekisteriyksikkö, Työllisyysrahasto, seguradoras de pensão (TyEL), seguradoras de acidente privadas.
- **Relatórios principais:** FI-RPT-001 palkkatietoilmoitus (earnings payment report, Incomes Register, SOAP/SFTP, prazo de 5 dias após o pagamento); FI-RPT-002 työnantajan erillisilmoitus (relatório separado do empregador); FI-RPT-003 invalidação; FI-PAY-004 pagamento da retenção e do seguro-saúde do empregador; multa por atraso (myöhästymismaksu, 53/2018 § 23, €3 por dia); formulários em papel TULOR 6101e/6103e.
- **Confiança da skill:** a maioria 95–99%. Abaixo do piso/derivados: layout dos formulários em papel (~70%, U1); TyEL do empregador (~85%, é média nacional, U3); taxas de acidente e seguro de vida em grupo (~80%, U4); teto de 5 anos da bicicleta (~60%, U7); arredondamento da taxa adicional (~80%, U13); formulários de payslip na prática (~85%, U2). 13 itens abertos (U1–U13) e 4 resolvidos (R1–R4).

**Armadilhas confirmadas**
1. Retenção incide sobre o BRUTO; pensão 7,30%, desemprego 0,89% e diária 0,88% do empregado já estão dentro do % do cartão de imposto (VH/5046/00.01.00/2025 §§ 4.3.1–4.3.2) (engine) → `01-ccg.md`
2. Empregador não roda a escala progressiva: aplica perusprosentti até a tuloraja acumulada própria, depois lisäprosentti no excedente (engine) → `01-ccg.md` §5.2
3. Tuloraja é ANUAL e POR PAGADOR; não proratear por mês nem somar empregadores (engine) → `01-ccg.md`
4. TyEL do empregado é 7,30% para TODAS as idades em 2026; faixa 53–62 (8,65%) abolida (STM asetus 1020/2025 § 1) (engine) → `01-ccg.md` §4.1
5. Três janelas de idade e três pisos: saúde empregador 16→68; pensão 17→68/69/70; desemprego 18→65; pisos de €71,72/mês (pensão), €1.500/ano (desemprego), €1.200/ano (acidente) (engine) → `01-ccg.md`
6. Valores de Finlex são base e precisam de indexação: €41,89 × 1,712 = €71,72; €1.300 × (1,712/1,446) = 1.539,14 → €1.500 (arredondado a €100) (engine) → `01-ccg.md`, QA R1
7. Contribuição de saúde da diária (0,88%) é precipício: só se renda anual ≥ €17.255, e então sobre a renda inteira (VNa 1026/2025 § 2) (engine) → `01-ccg.md`
8. Payslip tem só três linhas de dedução legais (retenção, pensão, desemprego); 1,10% (assistência médica) e 0,88% (diária) não aparecem separados, exceto não residentes/destacados (tipo 412) (engine) → `06-payslip.md`
9. Data de pagamento anda PARA TRÁS (TSL 2:15: domingo/feriado/sábado = dia útil anterior), o que muda o relógio de 5 dias do Incomes Register e a multa (engine) → `06-payslip.md`
10. M2M nos dois sentidos: saída (SOAP `ws.tulorekisteri.fi:443`, SFTP `sftp.tulorekisteri.fi:22`, certificado X.509) e ENTRADA do cartão via API Vero `Ennakonpidätystiedot maksajalle` e `suorasiirto` por Ilmoitin (Tyvi descontinuado em 2026) → `03-sir.md`
11. Sem cartão e sem dados eletrônicos = 60% (1124/1996 § 3); cartão de 31 dez 2025 só vale para janeiro de 2026; janeiro consome a tuloraja do cartão 2026 (engine) → `01-ccg.md`
12. Sem salário mínimo e sem severance legais; piso = acordo coletivo universalmente vinculante (TSL 2:7) ou "usual e razoável" (TSL 2:10); rescisão dá aviso prévio (14 dias / 1 / 2 / 4 / 6 meses) e indenização por danos → `01-ccg.md`
13. Carregamento de carro privado no trabalho TRIBUTÁVEL desde 1 jan 2026 (€30/mês elétrico, €20 híbrido plug-in; 998/2025 § 25); bicicleta tem dois regimes pela data do compromisso: antes de 24 abr 2025 = €1.200/ano isento; depois = totalmente tributável (tipo 364) (engine) → `01-ccg.md` §§11–12
14. Tipo de rendimento 101 significa "Total wages" no relatório de pagamento, mas "No wages payable" no relatório separado; no separado o código 102 carrega o valor da contribuição de saúde do empregador, não a base (erro superestima ~52×) (engine) → `04-reports-spec.md`

**O que mais dá errado** (do QA)
- Resolvidos mas críticos: piso de desemprego (R1: estatuto diz €1.300, Fundo diz €1.500, ambos certos), bicicleta/carregamento (R2), TyEL sem faixa etária (R3), aritmética do exemplo (R4).
- Engine ainda com 7,15% / 8,65% de TyEL sobre-deduz 1,35pp de uma coorte inteira.
- Apresentar TyEL 17,10%, acidente (~0,70%) e seguro de vida em grupo (~0,06%) como taxas do cliente: são médias.
- Taxas municipais e da igreja não podem ser cacheadas (43 municípios mudaram em 2026).

**Lacunas abertas / não confirmado** (candidatos a ticket ou nova pesquisa)
- U1: layouts em papel TULOR 6101e/6103e (~70%).
- U2: `tyosuojelu.fi` retornou 403; U10: `stm.fi` e `valtioneuvosto.fi` 403 (sem lacuna residual).
- U3: TyEL do empregador depende da seguradora e faixa de folha.
- U4: taxas de acidente/vida em grupo não são legais.
- U5: faixa da taxa da igreja (~85%); U9: taxas municipais de Åland não obtidas; U11: taxas municipais devem ser consulta ao vivo.
- U6: vencimento do TyEL é contratual (~90%).
- U7: teto transitório de 5 anos da bicicleta (~60%).
- U12: reforma da saúde de 2028 já está na lei.
- U13: direção de arredondamento da taxa adicional ambígua (~80%).
- U8: pisos setoriais não enumeráveis (estrutural).

**Valores-âncora**
| Item | Valor | A partir de | Fonte |
|---|---|---|---|
| TyEL empregado | 7,30% (todas as idades) | 2026-01-01 | STM asetus 1020/2025 § 1 |
| Desemprego | empregado 0,89%; empregador 0,31% / 1,23% (faixas) | 2026-01-01 | L 1111/2025 (altera 555/1998 § 18) |
| Seguro-saúde | empregador 1,91%; empregado dentro do % de retenção | 2026-01-01 | VNa 1026/2025; 771/2016 |
| Retenção sem cartão | 60% | 2026-02-01 (janeiro: cartão de 2025) | Ennakkoperintäasetus 1124/1996 § 3 |
| Piso de pensão | €71,72 por empregado/mês (€41,89 × 1,712) | 2026-01-01 | TyEL 395/2006 § 4 |
| Contribuição diária (saúde) | 0,88% se renda anual ≥ €17.255 | 2026-01-01 | VNa 1026/2025 § 2 |

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

## Internal Certification (Análise de Reports)
> Frente 5: `frentes/certificacao/estado.md` · Método: [[analise-reports]] · Pasta: `internal-certification/Finland`

- Sem pacote: Marju Martinson não respondeu aos pedidos de 07/10 e 09/10 (C-11). Report principal a confirmar: Tulorekisteri.

## Pendências
- [ ]

## Correções ligadas
- _(links para entradas de [[correcoes]])_

## Fontes
- skill payroll-compliance-finland (lida em 2026-10-02)
