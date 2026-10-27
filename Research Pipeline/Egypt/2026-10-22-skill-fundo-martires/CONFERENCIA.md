# Skill payroll-compliance-egypt — Fundo dos Mártires no setor privado (2026-10-22)

## Pedido
Janela Gmail (pedido do usuário), a partir da resposta à planilha Ericsson ME (#6): corrigir na skill a afirmação de que o Fundo dos Mártires (0,05%) não se aplica ao setor privado. Erro registrado em `correcoes.md` (2026-10-22) e nas Pendências de [[Egito]].

## Base
- `_base/payroll-compliance-egypt/`: cópia de `~/.claude/skills/.trash/1791418175888-24024-B4Plfx/payroll-compliance-egypt/` (06/10/2026), a única cópia local da skill.
- Conferida contra a v1 do claude.ai (`skill_012xb8yUhTvPATGGHefDvyfu`) em 22/10: o SHA-256 dos 8 arquivos (texto bruto, linhas em branco normalizadas) é igual ao da base.

## Fontes (lidas pessoalmente, pelas imagens das páginas; o texto do PDF sai ilegível)
- Lei 4/2021 art. 1 (novo art. 8 da Lei 16/2018), Gazette nº 8 bis (هـ) de 03/03/2021, pp. 5–6; em vigor no dia seguinte à publicação: [[raw/docs/oficiais/EG/2026-10-22-lei-4-2021-fundo-martires-gazette.pdf|2026-10-22-lei-4-2021-fundo-martires-gazette.pdf]]. O art. 8(1) desconta 5/10.000 do salário dos empregados dos entes públicos **e dos empregados de pessoas jurídicas privadas regidas pela Lei do Trabalho**, exceto trabalho irregular ou por dia; a entidade paga o salário já com o desconto e o MoF arrecada.
- Circular Geral MoF 14/2021 (10/05/2021): o item 3 repete o artigo e define o salário como "إجمالي الراتب الشهري" (salário mensal total). A parte "ثانيا" 2 trata dos demais entes: a ETA emite as instruções e repassa mensalmente até o dia 10 do mês seguinte. Inclui ainda o كتاب دوري 119/2021 (contas do Fundo). Cópia de host secundário (aliateck.com): [[raw/docs/oficiais/EG/2026-10-22-mof-circular-14-2021-e-kitab-dawri-119-2021-fundo-martires.pdf|2026-10-22-mof-circular-14-2021-e-kitab-dawri-119-2021-fundo-martires.pdf]].
- ETA Payroll FAQ v4, Q110 (já citada na skill): calcula sobre as remunerações básicas, para todos os trabalhadores exceto o diarista egípcio.

## Alterações (só Fundo dos Mártires; script `aplicar_correcao.py`; diff em `diff.txt`)
| Arquivo | Antes | Depois |
|---|---|---|
| `SKILL.md` escopo | O fundo era listado como regra pública que "does not apply" | Regra pública só para o selo; o fundo se aplica ao setor privado (§8.2) |
| `SKILL.md` | "Eight sections are below the 95% floor", incluindo a exclusão do fundo | "Seven"; o item do fundo foi retirado |
| `01-ccg.md` linha 54 | "no payroll stamp duty and no martyrs'-fund deduction" | Só o selo fica de fora; o fundo se aplica (§8.2) |
| `01-ccg.md` §8.2 | "NOT a private-sector payroll item"; escopo público | Escopo inclui o setor privado, com citação literal da Gazette; base e repasse pela Circular 14/2021; FAQ Q110 mantida; nota de divergência (diarista: todos × só egípcios; base total × básica) |
| `07-qa-report.md` | 8 seções abaixo do piso; linha "private sector not subject 80%"; §3.4 aberta; ação nº 5 | 7 seções; linha "private sector subject 98%"; §3.4 FECHADA; ação nº 5 feita |
| `04-reports-spec.md` RPT-06 | Escopo só público; 75% | Escopo com o setor privado, exceto trabalho irregular ou por dia; base legal na Gazette; 90% |
| `05-data-dictionary.md` | `martyrs_fund_subject`: "Public / public-business-sector only"; forma jurídica determinava o escopo do fundo | Y para todos, N só para trabalho irregular ou por dia; a forma jurídica não determina o escopo do fundo |

Sem mudança: `03-sir.md` (já trata o fundo como claim no Core, sem restrição), `02-wtc.md` e `06-payslip.md` (não citam o fundo), e a linha 69 do DD (diarista egípcio excluído, conforme a FAQ; a divergência com a lei ficou registrada no §8.2).

## Conferência
- `diff -rq`: mudaram só SKILL.md, 01, 04, 05 e 07.
- O script exige exatamente uma ocorrência de cada trecho (assert).
- `grep martyr`: não sobrou afirmação de exclusão do setor privado.

## Frentes
- 2026-10-22 · Pipeline · cópia corrigida e diff preparados.
- 2026-10-22 · Pipeline · com o ok do usuário: Substituir com `payroll-compliance-egypt.zip` (md5 `016165835f20d15902f32f47dffe67ed`) → v2; hash dos 5 arquivos alterados conferido no claude.ai; **publicada para a organização** com nota de versão. Pendência do hub marcada, `correcoes.md` e `log.md` atualizados.

## Arquivos da entrega
- Mapa dos arquivos desta pasta: [[Research Pipeline/Egypt/2026-10-22-skill-fundo-martires/MAPA|mapa]]
