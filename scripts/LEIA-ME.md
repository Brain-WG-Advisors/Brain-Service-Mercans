# scripts/

## youtrack_fetch.ps1

Baixa tickets do YouTrack (`https://youtrack.hrblizz.dev`) e salva cada um como Markdown.

### 1. Criar o token
No YouTrack: **Profile → Account Security → New token**, escopo **YouTrack**. Copie o valor (ele só aparece uma vez).

### 2. Colocar no `.env`
Na raiz do cérebro (`brain-service\.env`), uma linha:

```
YOUTRACK_TOKEN=perm:xxxxxxxx
```

O `.env` nunca deve ser lido, exibido nem copiado fora do script. Se usar outro nome de variável, passe `-TokenVar NOME`.

### 3. Uso
```powershell
cd C:\Users\instituto\Documents\brain-service

# Primeiro: só lista IDs e títulos, não grava nada
.\scripts\youtrack_fetch.ps1 -DryRun

# Depois: baixa de verdade (padrão: tickets atribuídos, abertos ou comentados por mim, atualizados desde 2026-01-01)
.\scripts\youtrack_fetch.ps1

# Atualização semanal: use a data da última execução
.\scripts\youtrack_fetch.ps1 -Since 2026-10-05

# Consulta própria
.\scripts\youtrack_fetch.ps1 -Query "project: HRBS State: Resolved updated: 2026-09-01 .. Today"
```
Se der erro de política de execução: `powershell -ExecutionPolicy Bypass -File .\scripts\youtrack_fetch.ps1 -DryRun`.

### 4. Onde ficam os arquivos
- `raw\tickets\api\AAAA-MM-DD\<ID>.md`: um por ticket (metadados, descrição, comentários, nomes dos anexos). Cada execução cria a pasta do dia; nada em `raw/` é sobrescrito.
- `scripts\youtrack_indice.md`: tabela ID | Título | Estado | Atualizado. Entradas de execuções anteriores são mantidas.
- O resumo no console mostra quantos foram baixados, novos e atualizados desde a execução anterior.

Depois de baixar, use "ingere raw/tickets/api/..." para levar o conteúdo ao cérebro (os arquivos podem conter dados pessoais; ao ingerir, seguir a regra 3 do `CLAUDE.md`).


> Cada execução grava em `raw/tickets/api/AAAA-MM-DD/` (pasta nova por dia; `raw/` é imutável). O índice acumulado fica em `scripts/youtrack_indice.md`.
