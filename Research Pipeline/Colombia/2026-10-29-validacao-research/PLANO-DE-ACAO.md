# Plano de ação: V&V da research da Colômbia (CO-VAL)

> **Versão 0.3 (2026-10-29), para aprovação do usuário.** Base: [[PROPOSTA]] (método, oráculos, suíte) · [[CONFERENCIA]] · Hub: [[Colombia]] · Pesquisa: [[PESQUISA-2026-10-29]]
> Histórico: v0.1 → 6/10; v0.2 → 8/10 (inventário, risco, garantia, uso pretendido, independência, 3 gates); **v0.3**: definições oficiais (SEVOCAB), níveis de integridade (IEEE 1012), linha de base completa (menos o SIR), distribuição de risco medida, vigência da base de teste conferida, cronograma recalibrado pela duração real da França, pseudo-oráculo aberto.
> Referências de método, conferidas em 29/10: definições verbatim do **IEEE SEVOCAB** (pascal.computer.org, que reproduz a ISO/IEC/IEEE 24765 e cita norma e cláusula); **IEEE 1012-2024** (versão vigente no SEVOCAB; a v0.2 citava a 2016); ISO/IEC/IEEE 15288:2023, 12207:2026, 29119-2/-3:2021, TR 29119-11:2020, 29148:2018, IEEE 828-2012. **PMBOK® Guide 8ª ed.** (PMI, novembro de 2025): 6 princípios e 7 domínios (governança, escopo, cronograma, finanças, partes interessadas, recursos, risco) pela página do PMI (lida pelo agente; reabertura deu 403); os nomes das 5 áreas de foco só em fonte secundária.

## 0. Termos (definições oficiais, verbatim)

| Termo | Definição oficial | Fonte | No projeto |
|---|---|---|---|
| **Verificação** | "confirmation, through the provision of objective evidence, that specified requirements have been fulfilled" | ISO/IEC/IEEE 15288:2023, 3.55; 12207:2026, 3.1.72 | Artefato × lei; spec × XSD/layout; marcação do WTC × lei |
| **Validação** | "confirmation, through the provision of objective evidence, that the requirements for a specific intended use or application have been fulfilled" | ISO/IEC/IEEE 12207:2026, 3.1.71 | Folha configurada pelos artefatos dá o resultado legal (§2) e quem configura aceita |
| (nota do SEVOCAB) | "A system can be verified to meet the stated requirements, yet be unsuitable for operation by the actual users." | SEVOCAB, nota a *verification* | Por isso há as duas, V e V |
| **IV&V** | "verification and validation performed by an organization that is technically, managerially, and financially independent of the development organization" | IEEE 1012-2024, 3.1 | Só com revisor externo (§6); sem ele: "V&V interna com independência técnica parcial" |
| **Base de teste** | "information used as the basis for designing and implementing test cases" | ISO/IEC/IEEE 29119-2:2021, 3.22 | Lei e fontes oficiais vigentes (§3b) |
| **Item de teste** | "work product to be tested" | ISO/IEC/IEEE 29119-2:2021 | Artefatos da linha de base (§3) |
| **Oráculo de teste** | "source of information for determining whether a test has passed or failed"; nota: pode ser especificação, outro sistema semelhante ou "asking a human expert" | ISO/IEC TR 29119-11:2020, 3.1.76 | A (lei), B (PMI), C (motor), D (especialista) |
| **Pseudo-oráculo** | "independently derived variant of the test item used to generate results, which are compared with the results of the original test item based on the same test inputs" (ex.: "a system developed by an independent team") | ISO/IEC TR 29119-11:2020, 3.1.59 | C (motor de mercado) e P (biblioteca aberta `col-nomina-co`, §6) |
| **Teste de aceitação** | "formal testing conducted to enable a user, customer, or other authorized entity to determine whether to accept a system or component" | IEEE 1012-2024, 3.1 | Walkthrough com o design (§2) |
| **Teste baseado em risco** | "testing in which the management, selection, prioritization, and use of testing activities and resources are consciously based on corresponding types and levels of analyzed risk" | ISO/IEC/IEEE 29119-2:2021, 3.16 | §4 |
| **Tarefas mínimas / nível de integridade** | "those verification and validation tasks required for the integrity level assigned to the system, software, or hardware to be verified and validated" | IEEE 1012-2024, 3.1 | Os níveis alto/médio/baixo do §4 são os nossos **níveis de integridade**; cada um tem tarefas mínimas |
| **Matriz de rastreabilidade de teste** | "document, spreadsheet, or other automated tool used to identify related items in documentation and software, such as requirements with associated tests" | ISO/IEC/IEEE 29119-3:2021, 3.26 | RTM: requisito ↔ fonte ↔ risco ↔ caso ↔ veredito |
| **Linha de base** | "formally approved version of a configuration item, regardless of media, formally designated and fixed at a specific time during the configuration item's life cycle" | ISO/IEC/IEEE 15288:2023, 3.8 | §3 (md5) |
| **Controle de mudança** | "process whereby modifications to documents, deliverables, or baselines associated with the project are identified, documented, approved, or rejected" | PMBOK 8ª ed. (via SEVOCAB) | §8 |
| **Defeito** | "imperfection or deficiency in a work product where that work product does not meet its requirements or specifications and needs to be either repaired or replaced" | ISO/IEC 23531:2020, 3.1 | Só defeito vira correção. "Lacuna" (a base não decide) e "decisão" (escolha legítima do cliente/BAU) são classes **nossas**, não da norma |
| **Critério de saída** | "states of being that have to be present before an effort can end successfully" | ISO/IEC/IEEE 24765:2017 | §1 e §8 |
| **Estimativa análoga** | "method of defining the cost or duration of a project by comparison to data from a similar project" | ISO/IEC/IEEE 24765 (via SEVOCAB) | §7. A faixa ROM −25%/+75% **não foi achada em fonte oficial**: removida |

## 1. Termo de abertura
- **Objetivo:** provar, com evidência rastreável, que a research da Colômbia está correta frente à lei e serve para configurar a folha, **antes de ela se tornar ativa** (design do Dev previsto para ~20/11, sem confirmação).
- **Critério de sucesso ("100%")**, como critério de saída:
  1. 100% dos requisitos de risco alto e médio com teste executado; os de risco baixo com verificação automática + amostra (§4);
  2. 100% das checagens com veredito;
  3. zero defeito aberto (todos corrigidos em `-DRAFT-` aprovado);
  4. toda lacuna/decisão fechada com fonte ou retirada do escopo por decisão registrada;
  5. cada artefato no nível de garantia aceito no GA (§5).
- **Fora do escopo:** Drive/artefato vivo sem ok; configuração do HRBlizz; envio real a DIAN/PILA; criar conta externa sem ok.
- **Premissas (confirmar no GA):** P1: research CO **não ativa** no nosso sistema → correção = nova versão, sem ticket ao Development (se ativa, regra 9). P2: linha de base = §3.

## 2. Uso pretendido e aceite (validação)
- **Uso pretendido:** o time de design/Development configura a folha CO no HRBlizz a partir de: WTC (wage types e tratamento), CCG (regras de cálculo), DD (dados do empregado e da empresa), 7 specs (arquivos estatutários), SIR (fluxo de integração) e Payslip; o BAU opera.
- **Requisitos de uso (validação):** U1, todo cálculo do CCG pode ser configurado sem interpretação; U2, todo WT do WTC tem tratamento completo; U3, todo dado que cálculo e arquivos exigem existe no DD; U4, toda spec gera um arquivo aceito pelo destinatário; U5, o SIR cobre todos os arquivos com prazo e canal.
- **Aceite:** walkthrough com o time de design (quem configura) sobre U1–U5 numa amostra. Depende do usuário/Manju (§6).

## 3. Linha de base (medida em 29/10, `achar_versao.py`)

| Item | Versão | Arquivo local | md5 | Observação |
|---|---|---|---|---|
| CCG | v1.4 | `2026-10-22-auditoria-lote1/CO-CCG-001-v1.4.docx` | 8b087e4d00… | Drive: Google Doc v1.4 (conferir export × local) |
| WTC | v1.6 | `2026-10-22-auditoria-lote1/CO-WTC-001-v1.6.xlsx` | 05b839bbf8… | Drive: Google Sheet v1.6 |
| DD | v1.3 | `2026-10-22-auditoria-lote1/CO-DD-001-v1.3.xlsx` | f5a14676f2… | Drive: Google Sheet v1.3 |
| 7 specs | v1.0 | `co-report-crosscheck/05-final/*.xlsx` | CESANTIAS-006 93b38907…; DIAN-001 b9f0d815…; DIAN-002 ff91e90d…; DIAN-004 a9ebaf29…; DIAN-005 f48c5a76…; PILA-003 12225906…; PILA-007 4bfea698… | Drive: Google Sheets (26/10, Replace) |
| SIR | v1.1 (Issued, 2026-10-21) | `linha-de-base/CO-SIR-001-v1.1-captura-2026-10-29.md` (captura de texto pelo Chrome, 19.875 caracteres) | — (Google Doc) | Lido em 29/10 pelo Claude in Chrome |
| Payslip | v1.1 (nome DRAFT, sem Version Control) | `CO-compliance/06-payslip/CO_Compliance_Payslip_Generator-v1.1-DRAFT.xlsx` | 32ded04fef… = **idêntico** ao `18 - Payslip/CO_Compliance_Payslip_Generator.xlsx` do Drive (24/09) | Resolvido em 29/10 pelo md5. O `.gsheet` da mesma pasta é de 14/07 (anterior) |

## 3b. Base de teste: vigência conferida em 29/10
| Fonte | Situação | Ação |
|---|---|---|
| NE: Res. DIAN 000227/2025 (compila a 13/2021; arts. 1.5.3.x), Anexo T5.4 "Versión 1.0" | Vigente; nenhum anexo/XSD mais novo achado. Micrositio DIAN ainda lista a Caja V1.0 | XSD local `NominaIndividualElectronicaXSDV1.0.6.xsd` e de ajuste = **vigentes**. Citar a 227/2025, não a 13/2021 |
| NE: set de pruebas da habilitação | Exige RUT, habilitação como facturador, certificado digital e software; **sem serviço de validação sem NIT** (fonte secundária) | Fica no I5 (decisão Mercans); sem ele, só XSD |
| PILA: Res. 2388/2016, alterada pela Res. 1529 de 24/07/2026 (anexos 2 e 3) | **Obtidos em 29/10**: Res. 1529/2026 (texto assinado) e AT2 v30 de 24-07-2026 (MinSalud), a mesma versão que a CO-PILA-003 cita. e AT3 v15 (pensionados), ambos baixados | Base de teste da PILA de ativos = AT2 v30. Defeitos D1/D2 confirmados nela |
| SMMLV 2026 | Valor COP 1.750.905; Decreto 1469/2025 com força desde a revogação da suspensão (jul/2026); processos acumulados em 2/10, sentença pendente (secundária) | Já registrado no hub (C21); caso de teste com o valor; o instrumento é lacuna até ler o auto |
| MinTrabajo "Mi calculadora" | A página existe (JavaScript); cobre prestaciones; login não confirmado | Conferência pontual pelo navegador do usuário |

## 4. Inventário medido e níveis de risco

| Artefato | Tamanho medido (29/10) | Risco alto (erro de pagamento ou multa) | Médio (arquivo rejeitado / configuração errada) | Baixo (texto, exemplo) |
|---|---|---|---|---|
| CCG v1.4 | 1.114 parágrafos (624 com número), 248 tabelas / 2.106 linhas, 212 títulos | Parâmetros e fórmulas (alíquotas, tetos, faixas, divisores, prazos de pagamento) | Regras de processo (quando, quem, ordem) | Contexto, histórico |
| WTC v1.6 | 405 WTs, 298 com marcação; 12 colunas estatutárias; **3.600 marcações não-NA**; + Employer Sick Pay (52), Tax Credit (90), Form Reference (66) | Marcações de retención, saúde, pensão, FSP, ARL, parafiscales, salarial/não salarial, base de prestaciones, base de férias | Elemento da NE, fórmula, ocorrência | Nomes e explicações |
| DD v1.3 | 102 campos do país + 21 de ID + 200 linhas de mapeadores | Campos que mudam cálculo (tipo de contrato, integral, risco ARL, dependentes, AFC, datas) | Demais campos exigidos pelas specs; listas de valores | Instruções |
| 7 specs v1.0 | 762 linhas de campo; 194 regras de preenchimento; 594 opções de campo; 266 linhas de exemplo; 994 linhas de arquivo de amostra | Campos de valor (bases, aportes, retención, totais) | Estrutura, posição/tamanho, opções, regras | Exemplos, matriz |
| SIR v1.1 | a medir (Doc) | Prazos e obrigações | Canal, formato, sequência | Descrição |
| Payslip | a medir | Valores e os 13 itens da Res. 227/2025 | Layout | Visual |

**Distribuição medida (classificação automática preliminar, 29/10):**
- CCG: 3.220 unidades (parágrafos + linhas de tabela) → **965 alto** (com alíquota, valor, UVT/SMMLV, teto, prazo), 528 médio (citação legal sem valor), 1.727 baixo.
- WTC: **3.195 marcações estatutárias não-NA (alto)**, 810 médio (elemento NE + fórmula), ~1.215 baixo (nomes/explicação). As marcações se repetem por tipo de verba: a verificação é por **classe de equivalência** (uma regra legal por tipo de verba, ~30–40 regras, aplicada aos 298 WTs), não célula a célula.
- Specs: 762 linhas de campo; a heurística marcou 678 como "valor", o que **não é confiável** (o texto de descrição contamina). Classificar pelo tipo de dado do campo na F1.
- Alto risco real estimado: ~1.000 (CCG) + ~35 regras × 298 WTs (WTC) + ~300–450 campos de valor (specs) + ~30 campos do DD.

**Ordem de grandeza:** ~9.000 unidades verificáveis. Tratamento:
- **Alto:** simulação (oráculos A + B, e C/D se aprovados) + verificação total contra a fonte.
- **Médio:** verificação automática total (XSD, layout, coerência DD↔spec↔WTC) + verificação contra a fonte do que falhar.
- **Baixo:** verificação automática (lint de valores, links, vigências) + amostra estatística por artefato, com o tamanho da amostra fixado no GA.

A classificação de cada item é gravada na RTM (requisito ↔ fonte ↔ risco ↔ caso ↔ veredito).

## 5. Nível de garantia por artefato (aceitar no GA)

| Artefato | Nível alcançável sem ajuda externa | Com C/D aprovados | Limite |
|---|---|---|---|
| CCG (cálculo) | Médio: lei + oráculo A + folha B | Alto | A tem o mesmo autor da research |
| WTC | Médio | Alto | idem |
| DD | Médio: coerência total + lei | Médio | — |
| CO-DIAN-001 NE | **Alto no formato** (XSD oficial; vigência a confirmar) + médio nos valores | Alto (set de pruebas DIAN, se houver NIT de teste) | — |
| CO-DIAN-002/004 (350, 220) | Médio: casillas × oráculo | Alto | Sem validador oficial offline |
| CO-DIAN-005 (2276) | **Limitado**: valores sim; layout DERIVED, sem XSD oficial | Limitado | Q-11 aberto |
| CO-PILA-003/007 | Médio nos valores; **limitado no formato** | Alto (simulador de operador) | Sem validador público |
| CO-CESANTIAS-006 | Médio | Médio | Formato por guia de operador |
| SIR | Médio (documental) | Médio | — |
| Payslip | Médio | Alto | Versão indefinida |

## 6. Independência (plano principal, não contingência)
| ID | Ação | Dá | Depende de |
|---|---|---|---|
| I1 | Oráculo A escrito a partir da base de teste e revisado por agente com prompt adversarial | Independência técnica parcial | nós |
| I2 | Folha B (PMI, setembro, mascarada) | Terceiro real, mas parcialmente circular (specs ajustadas a ela em 16–26/10) | nós |
| I2b | Pseudo-oráculo P: biblioteca aberta `col-nomina-co` (Python, licença MIT, roda local sem cadastro; cobre prestaciones, PILA, retención, integral, horas extras, incapacidades, liquidação) | Segunda implementação, de outro autor, sem custo | Nós. **Ressalvas**: projeto de 1 pessoa, 9 commits, sem testes, constantes de 2024 (UVT 47.065) → atualizar parâmetros e tratar como não verificado; vale como contraprova, não como juiz |
| I3 | Motor C: trial Aleluya ou Alegra (15 dias; carga em lote alegada nas páginas de venda, sem manual público) | Segundo motor de mercado | **ok do usuário** (cadastro). Os termos da Aleluya não autorizam nem proíbem empresa fictícia e tratam os dados como "bajo juramento" → **perguntar ao fornecedor por escrito antes** |
| I4 | Revisor D: especialista colombiano de folha ou time de implementação da Mercans revisa a amostra de risco alto | Independência gerencial (e financeira, se externo) = IV&V | **Manju/Marko** (mensagem rascunhada: `MENSAGEM-MANJU-DRAFT.md`) |
| I5 | Ambientes oficiais: set de pruebas DIAN (NIT de teste); simulador de operador PILA | Nível alto no formato | Mercans |

## 7. EAP e cronograma (estimativa por analogia)

Estimativa análoga (24765). Base corrigida em 29/10: a França não levou "~2 dias". O histórico do `fr-research-validation` mostra trabalho de **05/10 a 09/10 (5 dias corridos)**, com motor oficial pronto e parte feita antes no claude.ai (início não datado). A Colômbia não tem motor nem geradores e tem 7 specs (a França tinha 15). Fator 2 a 3 sobre 5 dias → **10 a 15 dias de trabalho**. Faixa sem percentual fixo (a regra −25%/+75% não foi achada em fonte oficial). Revisar no GA com a RTM real. Unidade abaixo: sessão (~meio dia).

| Fase | Pacotes | Sessões | Saída |
|---|---|---|---|
| F1 Linha de base + inventário | md5; RTM com risco de cada item (extração automática de CCG/WTC/DD/specs); fontes vigentes (XSD NE, anexo PILA, SMMLV C21); SIR e Payslip localizados | 2–3 | **GA** |
| F2 Construção | oráculo A + `params.json`; suíte da RTM (~60 casos de risco alto + limites); leitor B; geradores (NE, PILA, casillas, cesantías, payslip); revisão adversarial do A | 4–5 | — |
| F3 Execução | verificação automática total (médio/baixo); simulação (alto); amostra (baixo); C e D, se aprovados | 3–4 | — |
| F4 Análise e correção | classificação de cada divergência com a lei; `-DRAFT-` + changelog; reteste; zero regressão | 3–4 | **GB** |
| F5 Encerramento | relatório de V&V (inglês); walkthrough de aceite com o design; lições | 1–2 | **GC** |
| **Total** | | **13–18 sessões** (≈ 10–15 dias, conforme a sua disponibilidade) | Começando em 30/10: GC entre ~13/11 e ~20/11. **No limite do prazo do design (~20/11)** → R9: entregar CCG/WTC/DD primeiro |

Caminho crítico: F1 → oráculo A → geradores → F3 → F4. Os pontos sem fonte (Q-5, Q-6/7, Q-8, mesada de junho, C21, 2276) correm em paralelo desde a F1.

## 8. Gates (3) e regra de decisão
- **GA, escopo e garantia (fim da F1):** RTM e tamanho real; níveis de risco e de garantia; amostra do risco baixo; tolerâncias por regime de arredondamento (CCG §11); premissas P1/P2; cronograma revisado; I3/I4/I5 aprovados ou recusados.
- **GB, defeitos (F4):** cada defeito com o texto legal + os DRAFTs juntos.
- **GC, aceite:** relatório + nível de garantia atingido × aceito.
- **Entre os gates** (proposta, como na França em 06/10): aplico a opção recomendada e registro em `CONFERENCIA.md`. Continua pedindo ok: Drive, ticket, e-mail, conta externa, apagar.

## 9. RACI (A = aprova, R = executa, C = consultado, I = informado)
| Entrega | Frente (agente) | Revisor adversarial (agente) | Wallisson | Manju/Marko | Design/Dev | Revisor externo (I4) |
|---|---|---|---|---|---|---|
| RTM, oráculo, suíte, geradores | R | R (G2 interno) | A no GA | I | — | — |
| Defeitos e DRAFTs | R | R (contraprova) | A no GB | I | — | C (amostra) |
| Recursos I3–I5 | — | — | R (pede) | A | — | — |
| Aceite de uso (U1–U5) | R (prepara) | — | A | I | C (walkthrough) | — |
| Drive, ticket, e-mail | — | — | A + R | I | I | — |
Nomes de Manju, Marko e design: **a confirmar pelo usuário**.

## 10. Riscos
| ID | Risco | P | I | Resposta |
|---|---|---|---|---|
| R1 | Oráculo A repete erro da research | A | A | I1 + I3/I4; sem I3/I4 → declarar garantia "média" |
| R2 | B circular | A | M | B não decide sozinho |
| R3 | Base de teste desatualizada | **A (confirmado na PILA: Res. 1529/2026)** | A | NE conferida (vigente). PILA: obter a 1529 na F1 e reavaliar CO-PILA-003/007 antes de testar |
| R4 | Pontos sem fonte impedem 100% | A | A | Pesquisa desde a F1; o que não fechar → decisão no GA/GB |
| R5 | Geradores maiores que o estimado | M | M | Prioridade NE → PILA → casillas; revisar no GA |
| R6 | PII nas saídas mascaradas | B | A | `pii_audit_masked.py` antes; parar se achar |
| R7 | Item muda durante o teste | M | M | md5 da linha de base; mudança = registro + reteste |
| R8 | I3/I4/I5 não aprovados | M | A | Plano segue com garantia "média" declarada |
| R9 | Design começa antes do GC (~20/11) | **A** | A | Entregar por artefato: CCG/WTC/DD primeiro (são o que o design usa primeiro) |

## 11. Qualidade, medição, comunicação, encerramento
- **Métricas:** cobertura por risco (testados ÷ inventariados); aprovação por checagem e por regra; defeitos por artefato e gravidade (S1 bloqueia a entrega; S2 resultado errado; S3 forma/documento; S4 cosmético); lacunas abertas; nível de garantia atingido.
- **Evidência:** todo veredito aponta arquivo e linha/célula da fonte.
- **Comunicação:** o painel das frentes lê cada fim de rodada; gates nesta janela.
- **Encerramento:** relatório de V&V em inglês com resultado, cobertura, nível de garantia e limites de independência; lições → `correcoes.md` e backlog da skill.
