# Triagem da fila de tickets — 2026-10-16

> Janela Suporte, a pedido da janela geral. **Só triagem** (nada gravado em ticket, nenhum draftComment).
> Fonte: API YouTrack, puxada em 16/10 ~09:56–12:55 UTC → `raw/tickets/api/2026-10-16/` (54 arquivos). Consultas: `for: me #Unresolved` (4), `commenter: me`, `reporter: me` e `mentioned: me` com `updated: 2026-10-15 .. Today` (18 / 15 / 32; com sobreposição). Lido antes: [[correcoes]], `frentes/suporte/estado.md`, fim do [[log]].
> Corte: comentários depois dos nossos envios de 15/10 (~15:00–18:00 UTC).

## Painel

### 🔴 Urgente hoje (pedem algo a nós)

| Ticket | País | O que pedem a nós | Padrão já resolvido? | Muda artefato? | Próximo passo |
|---|---|---|---|---|---|
| SR-414 | [[Ucrania]] | Lily (16/10 11:09): alinhar a aba **UA-1PV-001 Spec** com a aba **Sample** (campos da Sample faltam na Spec) e destacar as mudanças em outra cor | Sim: mesmo pedido que gerou as seções F/H de D1/4DF (16 elementos do DECLARHEAD que estavam só na amostra), SR-160/161 em 15/10 | Sim: 1-PV Spec → v5.3 | Partir da export ativa (planilha no Drive, base v5.2 md5 92c5cbb8), listar elemento a elemento Sample × Spec × XSD S0301016, acrescentar linhas, destacar `FFDDEBF7`; rascunho de comentário curto |
| SR-415 | [[Ucrania]] | Lily (16/10 11:07): o mesmo para **UA-1PV-002 Spec** × **Sample** (trimestral) | Sim (idem SR-414) | Sim: 1-PV-002 Spec → nova versão (base v1.4 de 13/10; conferir se há maior no Drive) | Idem, contra o XSD S0301121; aproveitar e decidir os achados pendentes do hub (r.3070, r.7010/7030/7040, r.3080) |
| HRBS-15216 | [[Ucrania]] | Vaishnavi (16/10 11:53, @wgomes): Configuração não mexe em campos de regulação (nível de país); pede que **nós** levemos adiante o pedido da Nataliia (alterar obrigatoriedade, remover 1C Personnel Number, labels UK etc. no DD) | Parcial: respondemos em 25/09 e 28/09 (o que mudou no DD) | Talvez: confirmar se as mudanças de 25/09 estão no DD vigente (V4.1 de 13/10) | Usuário decide: quem aplica o DD no nível de país (Lily/Design & Dev, por [[fronteiras]]) e se respondemos apontando a versão do DD + para quem vai |

### ⏳ Espera o usuário

| Ticket | País | O que pedem a nós | Próximo passo |
|---|---|---|---|
| HRBS-14528 | [[Espanha]] | Shyam (16/10 10:56, @wgomes): Config diz que a integração do `.msj` já existe; pede **marcar uma call** para entender o que apontamos em 28/09 (aviso de notificação da Sede, prazo de 10 dias, assunto NMTT1HAF10) | Usuário: aceitar/marcar a call (ou responder por escrito que nossa parte está entregue e o resto é de Config) |

### 🔄 Espera outros (nada pedido a nós)

| Ticket | País | Situação | Próximo passo |
|---|---|---|---|
| SR-160 | [[Ucrania]] | In Review. Lily → mjohn (16/10): ajustes no XML gerado; mjohn corrigiu e anexou template/amostra | Nenhum nosso (ver Observação 1) |
| SR-161 | [[Ucrania]] | In Review. Lily → mjohn (16/10); mjohn: "updated C_DOC_SUB to 101", removeu R02G0xI | Nenhum nosso (ver Observação 1: C_DOC_SUB do 4DF é 104) |
| SR-162 | [[Ucrania]] | **Done.** Lily 16/10 12:49: "Testing ok in acceptance" | Nenhum; registrar no hub como entregue |
| SR-163 | [[Ucrania]] | In Review. Lily → mjohn; mjohn 12:53 "Done. updated." | Nenhum nosso |
| SR-432 | [[Espanha]] | Lily → Drew (16/10): mapeamento atualizado; Drew colocou em acceptance (rows 29–30 `work_center_ccc`, 36–37 `social_security_principal_ccc`) | Nenhum nosso |
| HRBS-14394 | [[Holanda]] | Archit (16/10 11:49) encaminhou ao time de Configuração citando nossa resposta (6.617,41; 52990 → 52999) | Nenhum nosso |

### ✅ Nada a fazer

| Ticket | País | Por quê |
|---|---|---|
| HRBS-12110 | [[Congo]] | Na fila (In Progress), último comentário 07/10 (dbalogun), sem pergunta a nós |
| HRBS-15253 | [[Lituania]] | Último comentário 13/10 (kgunawan); nada novo |
| SR-313 (TD), SR-357 (NA) | Chade, Namíbia | Done; comentários do mjohn de 15/10 sem menção a nós |
| CT-* (4081, 4130, 4137, 4254, 4338, 4346, 4356, 4395, 4396, 4453, 4577, 161, 3940, 501, 502, 541) | vários | Sem comentário novo |
| 26 HRBS da busca `mentioned: me` (Noruega 14066/13690/14231, Paquistão 16065, Algéria 11592, Tunísia 11694, Holanda 15179, Vietnã, Tailândia, Índia, Quênia, Egito, Angola etc.) | vários | Atualizados desde 15/10, mas nenhum comentário novo nos menciona (a menção é antiga) |

**Fila `for: me #Unresolved` em 16/10: 4** (HRBS-15216, SR-414, SR-415, HRBS-12110). Saíram desde 15/10: SR-160/161/162/163, SR-432, HRBS-14394 (atribuídos a outros após o envio). Voltou: SR-415 (pedido novo). Entrou: HRBS-15216 (atribuído a nós).

## Observações (fora do pedido → hub, não ticket)
1. **Templates do Dev (UA), a conferir nos anexos:** no SR-161 o mjohn diz ter mudado `C_DOC_SUB` para **101** no 4DF; nossa spec 4DF v3.3 fixa "104" (J0510411). Na tabela da Lily, o root gerado do D1 (SR-160) e do D6 (SR-163) aparece com `xsi:noNamespaceSchemaLocation="J0510411.xsd"` (schema do 4DF; D1 = J0510111, D6 = J0510611). Não verificado no XML anexo. Registrado nas Pendências de [[Ucrania]].
2. Hub [[Ucrania]]: a pendência "Responder HRBS-15216" estava desatualizada (respondido em 25/09 e 28/09); linha atualizada.
