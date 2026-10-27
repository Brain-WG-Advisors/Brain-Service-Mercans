---
tipo: pais
codigo: "TD"
etapa_research: "concluida"
etapa_research_data: 2026-06-30
etapa_design: "em andamento"
etapa_design_data: 2026-08-25
etapa_producao: 
etapa_suporte: "sem ticket no hub"
etapa_suporte_data: 
ccg: "v1.2"
ccg_data: 
wtc: "v1.1"
wtc_data: 
dd: "v1.1"
dd_data: 
report_specs: "7 report specs (versao nao citada)"
report_specs_data: 
sir: 
sir_data: 
payslip: 
skill: "payroll-compliance-chad"
tickets_abertos: 
tickets_conferidos_em: 
atualizado_em: 2026-10-27
---
# Chade (Chad, TD)

> Hub do país. Índice: [[00-INDEX]] · Skill: `payroll-compliance-chad` · Fronteiras: [[fronteiras]]

## Situação
| Etapa | Status | Data | Observação |
|---|---|---|---|
| [[research-pipeline]] | ✅ | 2026-06-30 | Pesquisa concluída (Wallisson); skill file entregue e atualizado com esclarecimentos do Mohit. CCG v1.2 / WTC v1.1 / DD v1.1 + 7 report specs (chat: compliance-research; design-dev-kb; mercans-compliance) |
| [[design]] | 🔄 | 2026-08-25 | Regulation Design clean-room v1.0 (2026-07-07) e comparação com CT-A-580 (lógica ~89%, geral ~83%); design novo do zero pedido a Wallisson em 2026-08-25, "a fazer" |
| Produção (outro time) | — | | |
| [[suporte]] | ⏳ | — | Sem tickets nas fontes. Arquivos OLE2 criptografados da Baker Hughes aguardam senha (Govind Thakur) |

## Ficha do país (da skill)
> Resumo do que mais importa para o serviço. Fonte: skill `payroll-compliance-chad`, lida em 2026-10-02. Valores exatos e tabelas: ler a skill. Se divergir, vale a skill.

- **Escopo:** FY2026, setor privado, moeda XAF. O SKILL.md é só roteador + esclarecimentos; alíquotas, faixas e tetos ficam em `references/01-ccg.md`.
- **Órgãos:** DGI (IRPP-TS, TFE, TAFP; e-Tax), CNPS (PFM, AT/MP, PVID), ONAPE (citado no QA).
- **Relatórios principais:** DGI: IRPP-TS, TFE e TAFP (mensais), DAS (anual). CNPS: Appel Mensuel (mensal), DNTS (trimestral), Récapitulatif (anual). O SKILL.md lista 7; o QA de maio/2026 fala em 11 specs.
- **Confiança da skill:** QA de 2026-05-29, nota 93,1/100, NEEDS PATCHES leve (0 crítico, 1 MAJOR, 2 MINOR), depois READY_FOR_HANDOVER. CCG↔WTC, CCG↔Report Specs e cobertura do Global WTC (491/491) em 100%. Não há itens TIER-B nem tokens `[VERIFY WITH RA]` no QA; os residuais são avisos de nomenclatura.

**Armadilhas confirmadas** (esclarecimentos de julho/2026 com Compliance; prevalecem sobre o resto da skill)
1. CNPS/TFE/TAFP seguem a relação de emprego exercida no Chade, não a residência fiscal: não residente com contrato local está sujeito aos três; a exclusão é empregado × prestador de serviço (e diplomatas) → SKILL.md, esclarecimento 1
2. Não residente: 18% flat sobre o bruto de fonte chadiana, sem isenções do Art. 45 e sem teto de BIK do Art. 46; BIK entra a valor cheio (engine) → esclarecimento 2
3. Base do BIK do Art. 46 = bruto em dinheiro, excluindo todos os BIK; nenhum BIK entra na base de outro (usar valor agregado "dinheiro + BIK" é circular) (engine) → esclarecimento 3
4. TFE e TAFP seguem a base do IRPP: item isento de IRPP (Art. 45) é isento de TFE/TAFP e vice-versa; bolsa escolar isenta de CNPS/TFE/TAFP; seguro-saúde de grupo isento, individual tributável; Relocation 1 (dinheiro) tributável, Relocation 2 (reembolso com recibo) fora de tudo → esclarecimento 4
5. Diplomatas (Art. 3-2°): fora de IRPP e de CNPS; "CNPS ainda se aplica" vale só para isenções de deficiência/jovem graduado/pagamento militar → esclarecimento 5
6. Prime de panier / indemnité de repas (6566%): isenta dentro do limite legal por ser condição de trabalho; acima do limite ou como complemento geral em dinheiro, vira CNPS-tributável (com teto) → esclarecimento 6

**O que mais dá errado** (do QA)
- Nomes de campo das specs divergem do DD (C4 em 57,5%, 91 campos sem par): `Family Name` → `Surname`, `Function` → `Job Title`, etc.; só nomenclatura, não falta conteúdo
- `Pay Frequency` ausente do DD; CCG diz `Employee Category` e o DD `Occupational Category`
- Spec 007 (Récapitulatif) sem linha "NO" por desenho; incluir linha cinza N/A

**Lacunas abertas / não confirmado** (candidatos a ticket ou nova pesquisa)
- Verificar se o rename C4/C2/C7 foi aplicado em todas as specs (005/006/007/008/009/004/010/011)
- `Insurable Salary` e `Months Worked This Year`: reclassificar como CALC ou adicionar ao DD; `Event Date`/`Accident Date`/`Accident Time` ainda a incluir no DD
- Harmonização semântica entre specs (`DGI Centre` etc.) adiada para v1.2; `Exemption Flag` usa o mapper Boolean (confirmar que é intencional)
- F22 (câmbio entre períodos) tratado só na reconciliação anual do CNPS
- Skim de conteúdo (F7 semântica de tax code da WTC, F8 inbound/outbound da SIR, F12 chave composta) ainda recomendado

**Valores-âncora** (o SKILL.md não traz tabelas; só estes pontos)
| Item | Valor | A partir de | Fonte |
|---|---|---|---|
| Retenção não residente | 18% flat sobre bruto de fonte chadiana, sem Art. 45/46 | FY2026 | CGI Art. 116 (esclarecimento 2) |
| BIK Art. 46 | % sobre bruto em dinheiro: logement 20%, véhicule 10%, nourriture MIN(15%; 75.000) | FY2026 | CGI Art. 46 (esclarecimento 3) |
| Dedução de despesas profissionais | 30% (sequência: bruto imponível Art. 34 − 30% − CNPS = líquido tributável) | FY2026 | esclarecimento 3 |
| Base legal CNPS | Law 7/66; Decrets 1634/1635/1636 de 2009 | — | citados no SKILL.md |
| Alíquotas CNPS, faixas IRPP-TS, SMIG, tetos | não constam no SKILL.md; ler `references/01-ccg.md` | FY2026 | — |

## Artefatos entregues
| Artefato | Versão | Data | Arquivo/local | Observação |
|---|---|---|---|---|
| CCG / WTC / DD / 7 report specs | v1.2 / v1.1 / v1.1 | — | — | Base do design (chat: design-dev-kb) |
| Crítica pré-submissão + lista de problemas (14 itens) | — | 2026-06-25 | TD_DevTeam_Critique_PreSubmission.md; TD_Lista_Problemas_Pesquisa.md | Concluída |
| Regulation Design clean-room do Claude (24 artigos: 23 ativos + 1 retirado) | v1.0 | 2026-07-07 | TD_Regulation_Design_v1_0.md | Concluído |
| Statutory Research CCG Positions (Q1–Q7) | — | 2026-07-07 | TD_Statutory_Research_CCG_Positions.md | Posições para a reunião |
| Comparação Claude × Dev (CT-A-580, 31 regs) | — | 2026-07-07 | TD_Design_Comparison_Claude_vs_DevTeam.md | Lógica ~89%, geral ~83% (Mohit fez em ~2 dias com IA) |
| Skill `payroll-compliance-chad` | [INCERTO] | — | skill | Entregue e atualizada |

## Valores-chave (com vigência)
Valores discutidos nos chats; vigência não registrada. Skill traz o conteúdo estatutário completo.
| Item | Valor | A partir de | Até | Fonte |
|---|---|---|---|---|
| Teto de dedução familiar | 5.000 por dependente: afirmado pelo Mohit, sem base legal (é o valor CNPS de CI); Art. 45-4° não tem teto | ⚠️ vigência? | 2026-07-07 (retirado do design) | ⚠️ sem fonte para o 5.000; Art. 45-4° CGI (chat: design-dev-kb) |
| Meal cash (628x) | WTC dizia tributável, CCG não; exceção: 628x tributável | 2026-07-07 | — | resposta ao e-mail Mohit → Wallisson [INCERTO] (chat: design-dev-kb) |
| Transporte | Isento até 30% da base; o excesso é tributável e sujeito a CNPS (WTC v1.1 tratava como isenção total) | ⚠️ vigência? | — | TD_DevTeam_Critique_PreSubmission (chat: design-dev-kb) |
| Piso CNPS | Fixo, sem proração; AT/MP só metadado, taxa fixa de 4% | 2026-06-25 | — | RA default; correção M2 (chat: design-dev-kb) |
| Exemplo validado | Base 350.000: PVID EE 12.250; IRPP 28.464; ER ≈ 88.200 | ⚠️ vigência? | — | CCG M12 (chat: design-dev-kb) |
| Confirmação da LFI 2026 | Loi 008 de 2025-12-26 | — | — | Pendente de confirmar (chat: design-dev-kb) |

## Decisões
- 2026-06-25: piso CNPS fixo, sem proração; classe de risco AT/MP só metadado, taxa fixa de 4% — RA default; correção M2 (chat: design-dev-kb)
- 2026-06-30: usar Chad e Ireland como baseline das sessões de gap-filling de acurácia — Manju (chat: compliance-research)
- 2026-07-02: IRPP numa regulação Differential anual (÷12 automático); teto de dedução numa ceiling account calculada; reconciliação de flags MTD no ordinal 1 e de passivos no 301 — Mohit, cross-training (chat: design-dev-kb)
- 2026-07-07: retirar 9148041/58126 (teto de 5.000 por filho): o Art. 45-4° não tem teto; base TFE/TAFP literal do Art. 189; base NR 18% = 58008; pré-tax de aposentadoria só "caractère obligatoire" (Art. 47-II); severance indenizatória fora da TFE; forfait BIK do Art. 46 sobre a base em dinheiro — pesquisa primária (CGI 2025, LFI, CdT 1996) (chat: design-dev-kb)
- 2026-07-07: CT-A-580: produção usa estimativa ×12, 9 forfaits sobre 58105, FLOOR(x+0,5), piso fixo, constantes em 9148009 — Dev (chat: design-dev-kb)
- 2026-08-25: automação de design começa por países pequenos (CI, Chad, Gabon, Iraq, Yemen); novo design do Chade do zero com Wallisson — Manju/Mohit (chat: design-dev-kb)

## Suporte (tickets)
| Data | Ticket | Assunto | Resolução | Mudou artefato? |
|---|---|---|---|---|
| — | CT-A-580 | Design/regulações do dev (31 regs), comparado com o design do Claude | Comparação feita (2026-07-07); não é ticket de cliente | Não |
| — | (arquivos criptografados) | 11 arquivos OLE2 da Baker Hughes | Aguardando senha com Govind Thakur | — |

## Pendências
- [ ] Divergência hub × skill: o hub (decisão de 2026-07-07) usa a "base TFE/TAFP literal do Art. 189"; a skill (esclarecimento 4) diz que TFE/TAFP seguem a base do IRPP, sem regra própria — verificar (skill lida em 2026-10-02)
- [ ] Divergência hub × skill: o hub registra meal cash 628x como exceção tributável [INCERTO]; a skill (esclarecimento 6) diz que prime de panier genuína é isenta dentro do limite legal e só vira CNPS-tributável acima dele — verificar (skill lida em 2026-10-02)
- [ ] Divergência hub × skill: o hub fala em 7 report specs; o QA da skill (2026-05-29) lista 11 specs/filings no escopo (o SKILL.md cita 7 relatórios) — verificar qual é o conjunto final (skill lida em 2026-10-02)
- [ ] Fonte do teto de 5.000 por dependente; se não houver, remover das regs 9148032/033 — Mohit (chat: design-dev-kb; KT 2026-07-07)
- [ ] Confirmar a resposta sobre meal cash 628x (tributável) — Compliance [INCERTO] (chat: design-dev-kb)
- [ ] Teto do Art. 47 na 9148181; severance contra o WTC; frais 15%; regularização anual CNPS (Art. 12); defeito dos "60 anos"; contas a pagar ER — Dev (chat: design-dev-kb)
- [ ] Posições sobre NR e TFE/TAFP no CCG + pedido de ruling da DGI — Compliance/DGI (chat: design-dev-kb)
- [ ] Localizar o décret de garnishment (Art. 277); quotité de penhora (Tribunal du travail) — RA/Pesquisa (chat: design-dev-kb)
- [ ] OI-3 PE plan-social 62182 — Mohit/Andre; OI-11 perímetro dos "appointements"; população diária/horista; status final dos itens C1–L2 [INCERTO] — Compliance (chat: design-dev-kb)
- [ ] Confirmar a LFI 2026 (Loi 008 de 2025-12-26) — Compliance (chat: design-dev-kb)
- [ ] BIK base 58105 inclui `65%%%`? comparação diz que sim, pesquisa diz bruto em dinheiro — Compliance [INCERTO] (chat: design-dev-kb)
- [ ] Novo design do zero — Wallisson (chat: design-dev-kb)
- [ ] Senha dos arquivos criptografados da Baker Hughes — Govind Thakur (chat: mercans-compliance)
- [ ] Atualizar Chad no Monday; alinhar o design na call de quinta — Wallisson (chat: compliance-research)

## Correções ligadas
- [[correcoes]]: teto de 5.000/filho no CCG e nas regs do dev (9148032/033), corrigido: Art. 45-4° não tem teto (2026-07-07).
- [[correcoes]]: WTC v1.1 com transporte como isenção total, corrigido: isento até 30%, excesso tributável e sujeito a CNPS.
- [[correcoes]]: design do dev (frais 15% ausente, "60 anos" no lugar de 60 meses e <35 anos, aposentadoria sem teto, base NR bruta etc.) e design do Claude (delta única 58128, dupla contagem 58125/58127) corrigidos em 2026-07-07; DD com "Czechia Report" a remover.

## Fontes
- raw/chats/2026-10-01-mercans-design-dev-kb.md
- raw/chats/2026-10-01-compliance-research.md
- raw/chats/2026-10-01-mercans-compliance.md
- skill payroll-compliance-chad (lida em 2026-10-02)
