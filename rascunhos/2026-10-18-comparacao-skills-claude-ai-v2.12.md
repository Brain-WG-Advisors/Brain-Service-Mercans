# Comparação: skills Mercans no claude.ai × pacote v2.12 (18/10/2026)

**Origem:** `frentes/pipeline/mercans-pipeline-methodology.skill`, baixado pelo usuário em 18/10 do claude.ai. O conteúdo é idêntico, byte a byte, à cópia sincronizada em `~/.claude/skills/synced/` (data interna 31/08/2026). Lista das skills da conta: `manifest.json` sincronizado.

| Skill | No claude.ai | No pacote (`~/mercans-pipeline/dist/v2.12/chat/`) | Ação |
|---|---|---|---|
| `mercans-pipeline-methodology` | 31/08/2026: pipeline v2.9, checks até C33, 11 stages, script `v2_9` | v2.12: §8 com as tabelas da v2.11 e da v2.12, regra de SKIP = FAIL, valores substituídos (C41), lições da França; referências de operação, QA e lições atualizadas; nomes de colegas neutralizados | substituir |
| `mercans-compliance-workflow` | 25/08/2026 | + regra "ajuste de layout nunca remove linha estatutária" e as verificações 4 (linhas antes × depois) e 5 (líquido ao centavo) no padrão do Payslip, pela lição F-25..F-28 da França | substituir |
| `mercans-artifact-toolkit` | não existe | nova para o chat (scripts de inspeção e validação; nota de uso no chat) | adicionar |
| `mercans-pipeline-contracts`, `country-build` | não existem | só no plugin do Code (governam os handoffs entre subagentes) | não vão para o chat |

**Diferença na methodology (claude.ai → pacote, antes da rodada de 18/10):**
- `SKILL.md`: +51 linhas e −8 linhas.
- `pipeline-operations`: +14 e −5.
- `qa-checks`: +13.
- `battle-tested-lessons`: +15.
- `xlsx-xml-surgery`: igual.

Na rodada de 18/10 entraram ainda a tabela da v2.11 e o texto neutro.

**Zips (todos com a pasta da skill na raiz, CRC OK e frontmatter válido):**
- `mercans-pipeline-methodology.zip`: 37 KB.
- `mercans-compliance-workflow.zip`: 11 KB.
- `mercans-artifact-toolkit.zip`: 27 KB.

Texto para o time: `dist/v2.12/ANNOUNCEMENT.md`.
