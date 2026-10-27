---
name: payslip-5-sheet-vs-8-sheet-contract
description: "O briefing do Payslip pede 5 abas; o contrato PSL exige 8 - no BE a divergência foi resolvida adotando as 8, e o validador hoje passa"
metadata: 
  node_type: memory
  type: project
  originSessionId: 760d3460-704b-4cb9-8a55-3d2d2c94456f
  modified: 2026-08-17T04:32:07.190Z
---

O briefing do Belgium Payslip Generator (14/08/2026) fixa **5 abas obrigatórias**:
`<País> (EN)`, `<País> (NL)`, `Payslip Spec`, `Unit Rate Details`,
`Population Range`. O contrato do
[[verify-every-artifact-against-shared-templates]] — codificado em
`~/.claude/skills/mercans-artifact-toolkit/scripts/validate_workbook.py
--artifact PSL` — exige **8 abas**, sendo as três extras `How to set up Payslip`,
`Compliance Payslip` (mestre neutro de idioma) e `Field Option`. O skill documenta
a ausência dessas três como causa-raiz de payslips incompletos em builds
anteriores.

**RESOLVIDO no BE (verificado em 17/08/2026):** as 3 abas foram adicionadas (via
`BE-compliance/06-payslip/_add_missing_sheets.py`) e o artefato hoje tem as 8. O
validador retorna `VERDICT PASS (blocker=0 major=0 minor=0)`. A anotação anterior
desta memória — de que o BE ficava em `FAIL` com 3 blockers esperados — está
**superada**; se aparecer FAIL agora, é defeito real, não divergência de padrão.

**Why:** os dois padrões coexistiam no repo e ninguém tinha decidido qual valia,
então o FAIL era ruído. A decisão de fato tomada no BE foi adotar o contrato de 8
abas, que é o mais rigoroso e o único que o validador conhece.

**How to apply:** em país novo, construir direto com as 8 abas — é o que o
validador cobra e o que o BE já entrega. Não tratar mais FAIL de PSL como
esperado.
