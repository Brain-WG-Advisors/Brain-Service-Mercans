# Uso de IA no serviço — regras da Mercans e como se aplicam a nós

> Fonte: Responsible AI Usage Awareness Training, Mercans QCRM, Q3 2026 (QCT_08, 31/08/2026), lido em 2026-10-20. Resumo do material em `raw/docs/2026-10-20-treinamento-responsible-AI-usage-Q3.md`. Ligado a [[correcoes]], [[fronteiras]] e [[analise-reports]].

## As regras (a partir de 2026-08-31, AI Usage Policy / AIMS)
1. **Só ferramentas de IA aprovadas** para trabalho; nada de "shadow AI".
2. **Não colar dado de cliente, de payroll ou confidencial** em ferramenta de IA; anonimizar/remover PII antes.
3. **Verificar toda saída de IA** antes de usar ou compartilhar, sobretudo fatos, números e conteúdo legal ou financeiro. Saída de IA em trabalho de cliente tem de ser exata, revisada e defensável.
4. **Humano no circuito** em decisões sobre pessoas.
5. **Pedido de pagamento ou de dados incomum** (urgência + segredo + dinheiro, mesmo vindo de "liderança", inclusive por vídeo/voz): verificar por um segundo canal conhecido e reportar.
6. Na dúvida, perguntar (QCRM). A Mercans está implantando o AIMS (ISO/IEC 42001), ainda não certificada.

## Como isso já bate com o nosso método
| Regra | Onde já está no cérebro |
|---|---|
| 3. Verificar a saída | Fonte primária para cada afirmação; "sem prova → sai da resposta" ([[CLAUDE]], comando de ticket, passo 5); memória "100% antes de apresentar". O caso Big Four do treinamento (citações inventadas, reembolso) é exatamente o risco que a regra evita. |
| 3. Defensável se contestado | `CONFERENCIA.md` por entrega (fonte, antes → depois, md5); [[correcoes]]. |
| 2. Sem PII | Regra 3 do cérebro: sem nomes, IDs ou salários de empregados nas notas; raws com IDs omitidos. |
| 4. Humano no circuito | Nada é enviado ou gravado em ticket/e-mail sem ok do usuário. |
| 5. Pagamentos | Validação de SEPA/banco na Certificação ([[analise-reports]]): o holerite é a âncora; não agimos sobre pedido de pagamento. |

## Pontos levantados na leitura — registro interno, sem ação (decisão do usuário, 2026-10-20)
- [x] **Claude é ferramenta aprovada?** Sim, segundo o usuário (20/10).
- [x] **Dado de cliente e de payroll no Claude:** relevado pelo usuário (20/10). Sem ação.
- [x] **Ferramentas de transcrição** (Tactiq, Otter, Gemini): aprovadas, segundo o usuário (20/10).
- [x] **AI Usage Policy lida** (20/10): resumo das duas políticas em `raw/docs/2026-10-20-politicas-IA-mercans.md`. Ver abaixo.

## Políticas (fonte primária)
| Documento | Versão | Situação |
|---|---|---|
| QCRM_066 — Mercans AI Usage Policy | V1.0, 2026-03-20 (Manju Shetija / Salman Saeed / Andre Voolaid) | **Vigente** ("Approved version"); revisão anual |
| IT_### — Acceptable Use Policy for AI Tools | V1.0, 2025-06-25 (Jasper Guevarra / Chris Jaagu / Andre Voolaid) | Anterior; cita ChatGPT Team e Google Gemini; acesso por caso de uso aprovado na ELT |

O que a QCRM_066 acrescenta ao treinamento, útil para o nosso trabalho:
- **Transparency (§3):** quando a IA contribuiu materialmente para documento ou saída para cliente, isso deve ser divulgado de forma apropriada; não apresentar como trabalho puramente humano em contexto regulado ou com cliente.
- **Revisão humana independente (§5)** antes de submeter análise, texto legal, cálculo financeiro ou declaração regulatória gerados com IA. Atenção especial a citações, referências e estatísticas. O nosso método já faz isso (fonte primária, `CONFERENCIA.md`, nada enviado sem ok do usuário).
- **A responsabilidade é pessoal (§5):** a IA não transfere nem dilui a responsabilidade de quem entrega.
- **Ferramenta aprovada ≠ aprovada para todo tipo de dado (§4).**
- Incidente: sat@mercans.com (§10).

## Status do treinamento
- Composição: documento (lido) + vídeo + quiz (≥ 80%) + formulário de feedback. Prazo final: 19/10/2026 (Final Reminder).
- **2026-10-20: concluído pelo usuário.** Quiz (10 perguntas, respostas tiradas do material) e feedback (nota 4, texto neutro) preenchidos com o Claude, revisados e enviados pelo usuário. Sem aviso ao QCRM (decisão do usuário: não é necessário). **Processo encerrado.**
