# Prompt: coleta com Claude in Chrome (F3 chats, F4 reuniões, F5 Drive)

> Usar no Claude Code com o Chrome conectado (`/chrome`). Plano: [[PLANO]] §3 (bloqueios), §4, §5, §6 Fase 3.
> Pré-requisitos: decisões 0.2 e 0.5 (F3); 0.1, 0.2 e 0.5 (F4, F5). Escopo: **2026-01-01 até a data da coleta**.

## Regras para o Claude (valem para F3, F4 e F5)
- **Só leitura.** Não editar, mover, renomear, comentar, compartilhar nem apagar nada (Drive, Docs, Meet, claude.ai). Não enviar mensagem em conversa existente do claude.ai.
- **Inventário antes de baixar.** Listar tudo do período em `inventarios/<fonte>.md` ([modelos/inventario.md](../modelos/inventario.md)) e **esperar o ok**.
- **Só o que está no catálogo** ([[PLANO]] §6 Fase 3). Na dúvida se um item entra, ele vai para o inventário como "pendente: perguntar".
- **Sem dados pessoais** de funcionários de clientes. Arquivo nominal (holerite, ficha, "Nome | País | ID") → pular e anotar "descartado: dado pessoal".
- **Não baixar artefatos completos** (CCG, WTC, DD, Specs inteiros). O conteúdo estatutário já está nas skills.
- **Texto fiel:** copiar o conteúdo como está (sem resumir) para `raw/`. A extração acontece depois, em cartões.
- Cabeçalho de todo arquivo em `raw/`: título, data do original, link, "coletado em AAAA-MM-DD via Chrome".
- Se uma página pedir login, permissão ou confirmação, **parar e avisar** (não clicar em "pedir acesso" nem em "aceitar").

## F3: Conversas do claude.ai (projetos Mercans)
1. **Inventário:** em claude.ai → Projects, para cada projeto Mercans (Compliance, Compliance Research, Design & Development, tickets e outros que aparecerem), listar as conversas com última atividade ≥ 2026-01-01: `projeto | título | data | link`. Incluir as conversas fora de projeto com tema Mercans (busca por país, HRBS-, CT-, SR-, CCG, WTC, DD). Gravar em `inventarios/chats.md`. **Esperar o ok.**
2. **Coleta fiel:** abrir cada conversa aprovada e copiar o texto completo (perguntas e respostas, na ordem) para `raw/chats/conversas/AAAA-MM-DD-<projeto>-<titulo-curto>.md`. Não colar prompt na conversa, porque isso alteraria o histórico.
   - Conversa muito longa: copiar em partes (`...-parte1.md`, `-parte2.md`).
   - Alternativa, se estiver liberada: Settings → Privacy → Export data (todas as conversas num arquivo). Nesse caso, salvar o export em `raw/chats/export-AAAA-MM-DD/` e filtrar pelo inventário.
3. **Extração:** aqui no Claude Code, cada conversa vira cartões ([modelos/extracao.md](../modelos/extracao.md)), usando as seções de [extracao-conversa.md](extracao-conversa.md) como roteiro (decisões, correções, versões, pendências). Nível C, salvo quando a conversa cita fonte A ou um artefato versionado (B). Subagentes Sonnet por lote de conversas.
4. Validação → ingestão → Conjunto B → métricas → log/commit ([[PLANO]] §6 Fase 3).

## F4: Reuniões
1. **Inventário:** no Drive, buscar `Transcript`, `Transcrição`, `Notes by Gemini`, `Anotações do Gemini`, `Meeting notes`, e a pasta `Meet Recordings`, de 2026-01-01 até hoje. Listar: `data | título | participantes (só papéis/times) | link | tipo (transcrição/notas)`.
   - **Entram:** reuniões do time de compliance, research, design, handover, liderança (ex.: a de 2026-06-30) e as com Dev/BA sobre artefatos nossos.
   - **Ficam fora:** outros times sem pauta nossa, 1:1 pessoais, RH.
   - Gravar em `inventarios/reunioes.md`. **Esperar o ok.**
2. **Coleta:** `raw/reunioes/AAAA-MM-DD-<titulo-curto>.txt`, com o texto integral e o cabeçalho padrão. Quando houver notas e transcrição, baixar as duas (as notas resumem, a transcrição prova).
3. **Extração:** cartões com o **trecho/minuto** exato como localização. Decisão em reunião = nível C, sempre com quem e quando. Se a reunião cita documento ou lei, o cartão aponta para eles (alvo F5 ou fonte A).
4. Validação → ingestão → Conjunto B → métricas → log/commit. `raw/reunioes/` **não vai para o git**.

## F5: Drive "Compliance Team"
1. **Alvos:** partir de `inventarios/drive-alvos.md` (links do board Compliance Artifacts e dos RCA, gerados na F1). Completar navegando a pasta "Compliance Team" de cada país do escopo (decisão 0.9): `05 - Payroll Regulation Guide` (CCG), `03 - WTC`, `02 - DD`, `12 - Country Report Codes` e as pastas de QA/pendências.
2. **Inventário por país:** `arquivo | versão (do nome e do Version Control) | data de modificação | link | o que coletar`. Regra 8: a versão vigente é a de maior número. Listar as outras como histórico, sem baixar. Gravar em `inventarios/drive.md`. **Esperar o ok.**
3. **Coleta:** de cada artefato vigente, **só** a aba/seção **Version Control / Changelog** (todas as linhas) → `raw/drive/<Pais>/<arquivo>-version-control.md`. QA reports e listas de pendências → inteiros. RCA docs (links do monday) → inteiros.
4. **Extração:** cartões tipo "versão final" (artefato, versão, data, o que mudou, ticket citado) e "erro+causa" (linhas de VC que corrigem erro). Nível B. Cruzar com a tabela "Artefatos entregues" do hub e com `inventarios/monday.md`.
5. Validação → ingestão (hub: versão vigente + histórico) → métricas → log/commit. `raw/drive/` **não vai para o git**.
