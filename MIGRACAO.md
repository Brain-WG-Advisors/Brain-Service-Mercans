# Migração do Brain Service para outra máquina

> Escrito em 2026-10-22. Objetivo: levar o brain para a máquina onde está o trabalho consolidado (pipeline v2.9, saídas dos países, failure log F1–F37), para trabalhar de lá.
> O brain está no GitHub (`ViniCerqueira/brain-service`, privado), então **a migração é um clone** e não uma cópia de pasta.

## O que vai por qual caminho
| Item | Caminho | Observação |
|---|---|---|
| Todo o brain (notas, hubs, correções, plano, prompts, modelos, raw em texto, scripts) | **GitHub** (`git clone`) | É a cópia oficial |
| 101 PDFs originais dos tickets + `raw/youtrack_tickets.zip` | Pacote `brain-service-fora-do-git-2026-10-22.zip` (Área de Trabalho da máquina antiga, 65 MB) | Fora do git por tamanho; o texto já está em `raw/tickets/txt-utf8/` |
| `.claude/settings.local.json` (permissões do Claude Code nesta pasta) | Mesmo pacote | Opcional |
| Memória do Claude Code (6 arquivos: quem é o usuário, preferências, contexto) | Mesmo pacote, pasta `memoria-claude-code/` | Restaurada na primeira sessão |
| **`.env` (token do YouTrack)** | **Não vai.** Recriar à mão na máquina nova | Nunca copiar, enviar ou colar o token em chat |
| `raw/reunioes/`, `raw/drive/` | Ainda vazios | Na máquina nova, continuam fora do git |

Para levar o pacote: pen drive, OneDrive ou outro meio da empresa. **Não** subir para o GitHub.

## Passo a passo na máquina nova (Windows)
1. **Pré-requisitos:** Git, GitHub CLI (`gh`) e Claude Code instalados.
2. **Login no GitHub com a conta ViniCerqueira:**
   ```powershell
   gh auth login
   ```
3. **Clonar** (sugestão: a mesma pasta da máquina antiga):
   ```powershell
   cd $HOME\Documents
   gh repo clone ViniCerqueira/brain-service
   cd brain-service
   git config user.name "ViniCerqueira"
   git config user.email "$(gh api user --jq .id)+ViniCerqueira@users.noreply.github.com"
   ```
4. **Pacote fora do git:** descompactar `brain-service-fora-do-git-2026-10-22.zip` numa pasta qualquer e copiar:
   - o conteúdo de `brain-service\` (pastas `raw\` e `.claude\`) para dentro de `Documents\brain-service\`, mesclando;
   - a pasta `memoria-claude-code\` pode ficar onde foi descompactada (passo 6).
5. **Recriar o `.env`** na raiz do brain, com uma linha: `YOUTRACK_TOKEN=<seu token>`. O token sai do YouTrack: Profile → Account Security → New token, escopo YouTrack. Pode ser um token novo, e o antigo pode ser revogado.
6. **Primeira sessão do Claude Code** nesta pasta. Colar:
   ```
   Sessão de migração do Brain Service (vim de outra máquina; ver MIGRACAO.md).
   1. Restaure a minha memória: copie os arquivos de <caminho>\memoria-claude-code\ para o seu diretório de memória
      deste projeto (sem duplicar nada que já exista) e confirme o índice MEMORY.md.
   2. Confira a integridade: git status limpo, git log igual ao remoto, 101 PDFs em raw/tickets/youtrack_tickets/,
      .env existe (NÃO leia o conteúdo), .gitignore protegendo .env, raw/reunioes, raw/drive e publicar/.
   3. Faça um DryRun do YouTrack para testar o token: .\scripts\youtrack_fetch.ps1 -DryRun (só a contagem).
   4. Esta máquina tem o pipeline atual. Localize (só listar, sem abrir arquivos de segredo): a pasta do pipeline
      (mercans_pipeline_v2_9.sh), as pastas <CC>-compliance/ com as saídas reais, shared/ e o country_failure_log.
      Atualize a decisão 0.7 e o prompt da F6 no PLANO: o cenário 3 agora é local.
   5. Registre a migração no log.md, commit + push.
   ```
7. **Na máquina antiga:** se ela não for mais usada para o brain, não editar mais a pasta de lá. Se for, rodar `git pull` antes e `git push` depois de cada sessão, para as duas não divergirem.

## Mac ou Linux
Os mesmos passos. Clonar em `~/Documents/brain-service` e criar o `.env` com `nano .env`. O script do YouTrack é PowerShell: instalar o `pwsh` (PowerShell 7) ou pedir ao Claude uma versão em bash.

## Por que vale a pena
- A **F6 (pipeline)** deixa de depender de cópia: as saídas reais e a v2.9 estão na própria máquina.
- O **country_failure_log (F1–F37)** e o `shared/` viram fontes diretas (erros e causas do pipeline → `correcoes.md`).
- O risco "máquina × Drive divergentes" (PLANO §13) pode ser conferido no mesmo lugar.
