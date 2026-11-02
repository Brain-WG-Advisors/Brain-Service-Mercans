# Chade — design v4 (conferência)

> Hub: [[Chade]] · Contexto: [[PACOTE-CONTEXTO]] · Serviço: [[design]]
> Rascunho local, 2026-10-29. **Não vai ao Drive nem ao Dev sem ok do usuário.**

## Fonte
- Base: design v3 (Drive `Chad/07-design/chad-design/`, 2026-10-15; md5 = cópia de Downloads).
- O que mudar: respostas da reunião de 2026-10-16 (Suman, Mohit), na conversa "Mercans payroll knowledge base overview IV", msg [332] (projeto Design & Development KB, org Mercans).
- Contas que os relatórios leem: 7 Report Specs do Chade no Drive (`Chad/04-reports-spec`), aba "… Spec", coluna "System Mapping", lidas pelo Chrome em 2026-10-29 (export CSV de cada aba).
- Convenções de escrita: `07-design/td.json` (export do Dev de 2026-07-02): `simple_tax_$$_post_formula`, `LESS($58218;1)`, 58205/58206/58212.
- Regras: skill `mercans-regulation-design` (Downloads, `.skill`) e `KB_Design_Rulebook_v4.md`.

## Decisões
1. Os números de conta seguem o que as specs leem (58105, 58008, 58104, 58108, 58120–58128, 58130, 58131, 58552, 58106, 58205, 58212, 58218). Coincidem com o mapa do Dev.
2. Pares contábeis da CNPS mantidos como no v3 (EE 2610/2551; PFM 6020/2550), pela regra do par coerente de 16/10. As specs 005/006/007 mapeiam ao contrário → research gap R13.
3. `retro_` só onde há piso, teto ou tabela (regra literal de 16/10); o resto fica anotado como premissa A11.
4. Plano social passou para a flag 58210 (a 58206 é a da redução da TFE, como no Dev).

## Antes → depois
Ver `chad-design-blueprint-claude-v4/CHANGELOG.md` (10 itens).

## Conferência
- `python -I _build_v4.py`: gera o SKILL.md a partir dos mesmos dados que executa; os 10 cenários dão o mesmo EE CNPS, IRPP, TFE, TAFP e líquido do v3 (`ALL MATCH`).
- `preflight_check.py`: nenhuma violação.
- Não testado em motor: conta-teto (A10), `retro_` (A11), `_$$` (A12).

## Fora do pedido (vai ao hub, não entra no design)
- No `td.json` do Dev (reg 171), a banda com `employeeRate` 3,5 lança em 6020/2550 e a com `employerRate` 7,5 em 2610/2551: taxa e contas parecem trocadas. Isso é configuração do Dev; confirmar na versão de aceite.
- Spec DGI-001 chama 58552 de "Total Gross Salaries"; a DAS chama de "Net Taxable Base" → R14.

## Quem mexeu
| Data | Frente | O quê |
|---|---|---|
| 2026-10-29 | chade | v4 criada a partir do v3 + reunião 16/10 + 7 Report Specs; validação 10/10 igual ao v3 |
