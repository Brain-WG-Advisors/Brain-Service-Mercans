# Prompt: coleta com Claude in Chrome (reuniões e Drive)

> Usar no Claude Code com o Chrome conectado (`/chrome`). Fontes F4 e F5 do [[PLANO]].
> Pré-requisitos: [[PLANO]] itens 0.1 (ok do chefe) e 0.5 (extensão logada).

## Regras para o Claude
- **Só leitura.** Não editar, mover, comentar, compartilhar nem apagar nada no Drive, no Meet ou no Docs.
- **Coletar só o que está no catálogo** ([[PLANO]] 4.2). Na dúvida se um arquivo entra, listar e perguntar.
- **Sem dados pessoais** de funcionários de clientes. Se um arquivo for nominal (holerite, ficha de funcionário), pular e anotar o motivo.
- **Não baixar artefatos completos** (CCG, WTC, DD, Specs inteiros): só Version Control/changelog, QA report e listas de pendências.
- **Primeiro listar, depois baixar.** Mostrar a lista (nome, data, pasta, link) e esperar o ok.
- Salvar como texto (`.txt`/`.md`). Se o Drive só permitir download do arquivo (`.docx`/`.xlsx`), salvar o original e anotar.

## F4: Reuniões
1. No Drive, buscar: `Transcript`, `Notes by Gemini`, `Meeting notes`, `Anotações do Gemini`, de 2026-01-01 até hoje.
2. Filtrar: reuniões do time de compliance, research, design ou com a liderança. Descartar as de outros times e as 1:1 pessoais.
3. Listar no formato: `data | título | participantes (só papéis) | link`. Esperar ok.
4. Salvar cada uma em `raw/reunioes/AAAA-MM-DD-<titulo-curto>.txt`, com cabeçalho: título, data, link e "coletado em AAAA-MM-DD via Chrome".
5. Registrar em [[log]]: quantas foram listadas, baixadas e descartadas.

## F5: Drive "Compliance Team"
1. Abrir a pasta "Compliance Team". Para cada país do [[00-INDEX]]:
   - `05 - Payroll Regulation Guide` (CCG), `03 - WTC`, `02 - DD`, `12 - Country Report Codes`: abrir a **versão de maior número** (regra 8) e copiar só a aba/seção **Version Control** ou **Changelog**.
   - QA reports e listas de pendências, se existirem.
2. Listar por país: `arquivo | versão | data de modificação | link`. Esperar ok.
3. Salvar em `raw/drive/<Pais>/<arquivo>-version-control.md`, com cabeçalho: arquivo, versão, link, data de modificação e "coletado em AAAA-MM-DD via Chrome".
4. Registrar em [[log]].

## Depois da coleta
Seguir o ciclo do [[PLANO]] 4.2: extrair cartões ([modelos/extracao.md](../modelos/extracao.md)) → ingerir → perguntas no teste → log → commit (sem `raw/reunioes/` e `raw/drive/`).
