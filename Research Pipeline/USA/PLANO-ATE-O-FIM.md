# EUA — Plano até a última etapa (sem parar)

Criado em 2026-11-01 (frente EUA). Liga: [[frentes/eua/estado|estado da frente EUA]], [[paises/EUA|hub EUA]], `US-compliance/00-official-sources/MANDATE.md`, `PRIORIDADE-ESTADOS.md`.

Método: equipe de 4 agentes (skill `country-build`): escopo → fontes → montagem → revisão, com revisão antes de cada passo seguinte.

## Regras para não parar
1. **Eu decido e registro** o que for decisão técnica ou estatutária: pesquiso na fonte oficial e decido com a fonte. A decisão vai como linha `US-OWN-*` ou no `CONFERENCIA` da fase. Não volto ao usuário com pergunta estatutária.
2. **Site bloqueado:** tento pela VPN, depois Wayback, depois Chrome. Se nada funcionar, marco como lacuna e sigo. A lista sai uma vez por fase, sem travar.
3. **Revisão (QA):** no máximo 3 rodadas por artefato. Se na 3ª ainda falhar, registro o defeito como ressalva no relatório de QA e sigo.
4. **Ponto de controle no disco** ao fim de cada fase: `estado.md`, `log.md`, painel e `CHECKPOINT-<fase>.md`. Se a sessão cair, retomo do último ponto sem refazer nada.
5. **Paro só para:** (a) mandar algo ao Drive, monday, ticket ou e-mail (precisa do seu ok); (b) mudança de escopo (tirar estado ou pergunta).

## O que você precisa manter
- Notebook ligado, sem suspensão (a suspensão automática do Windows mata o processo).
- VPN Windscribe ligada nas fases 0 e 1 (pesquisa). Da fase 2 em diante não precisa.
- Esta janela aberta.

## Fases

| Fase | O quê | Etapas do script | Pronto quando |
|---|---|---|---|
| 0 | Fechar o escopo: US-MQ-03 (idioma), US-MQ-05c (taxas extras em 22 estados) e os defeitos de anotação do registro | antes da 1 | MANDATE selado (65/65), manifesto PASS |
| 1 | Pesquisa completa dos 13 temas: federal + multiestado, depois onda 1 (10 estados), onda 2 (15), onda 3 (26); grupos especiais por estado (US-OWN-005) no fim | pasta 00 | pacote de pesquisa + `facts.json` por artefato; registro sem linha citada que não seja ativa |
| 2 | CCG: módulos m01–m13 + anexos FED, MULTI e 51 estados, por onda | 1 | QA PASS do CCG |
| 3 | Trava do escopo | 2 | `scope_manifest.json` PASS |
| 4 | Report Specs → Data Dictionary → WTC → Integrações → Payslip | 3 a 7 | QA PASS de cada um |
| 5 | Alinhamento DD × Specs, auditoria pré-entrega, QA cross-check | 8 a 10 | relatório de QA sem bloqueio |
| 6 | Skill do país, design, pacote final (local) | 11 a 13 | pacote único dos EUA pronto em `US-compliance/` |
| — | **Para aqui:** seu ok para subir ao Drive | — | — |

## Ordem dos estados
Onda 1: CA, TX, NY, FL, IL, PA, OH, NC, MI, GA. Onda 2: NJ, MA, VA, TN, IN, WA, SC, MN, AZ, WI, MO, CO, KY, MD, AL. Onda 3: os outros 26 (CT … WY). Dentro da onda: estados mais simples primeiro, os com imposto local (T4) por último. Se chegar a lista de estados com cliente (BAU), reordeno.

## Andamento
- 2026-11-01: plano criado.
- 2026-11-02: ✅ Fase 0 — mandato selado (65/65, validador PASS). Decisões US-OWN-006 (idioma) e US-OWN-007 (taxas) registradas. Início da fase 1.
- 2026-11-02: Fase 1 — pesquisa dos 53 grupos concluída (~1.260 fontes). Em curso: juntar no registro; depois passada no navegador (precisa VPN) e pacotes de pesquisa por documento.
- 2026-11-02: ✅ Fase 1 concluída — registro 2.572 fontes; pacotes e facts de todos os documentos (≈5.300 valores, todos validados). Pendências que dependem de publicação (DC método 2026, UT vigência) ou de IP dos EUA ficam como lacuna marcada. Início da fase 2 (CCG).
- 2026-11-02: ✅ Fase 2 — CCG aprovado (QA r3e PASS; 3 rodadas + 2 correções dirigidas). Início da fase 3 (trava do escopo) e fase 4 (Report Specs, DD, WTC, Integrações, Payslip).
