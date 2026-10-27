# Aviso ao time: pipeline v2.12 (rascunho, não enviado)

> Janela geral, 2026-10-17. Base: `~/mercans-pipeline/dist/v2.12/INSTALL.md` e `CHANGELOG-v2.12.md`. Canal e destinatários: definir com o usuário. Anexos/link: os 2 zips de `dist/v2.12/chat/` (ou o link do repositório, depois do push).

**Subject:** Compliance research pipeline v2.12 — updated skills (please install)

Hi team,

The compliance research pipeline is now at **v2.12**. We validated the France dossier end to end: the calculations were re-computed independently and compared with the official payroll engine, the DSN samples went through the official validator, and the statements were checked against primary law. We then checked each of the 63 errors that were ours against the pipeline. Before this update, 5 were fully blocked. Now 18 are fully blocked and only 7 remain without a check.

Main changes:
- A check can no longer be skipped silently when a country lacks an official validator or code table. It fails unless an exemption is recorded with a reason and an official source.
- Statutory values are bound to a single facts file, so one correction reaches every artifact.
- New blocking checks for wage-type codes, tax flags and the employee/employer side across WTC, DD, specs and payslip, and for the payslip's legal items.

**What to do (chat / Claude Desktop):** upload the two attached skills via **Customize → Skills → Upload a skill**: `mercans-pipeline-methodology.zip` and `mercans-artifact-toolkit.zip`. Replace any older version of the same skill. Do not unzip them. If the organisation provisions them centrally, you will see them already switched on.

Please stop using any old copy of `mercans_pipeline_v2_9.sh`. The script is now `mercans_pipeline_v2_12.sh`.

The full changelog and install guide are attached. Claude Code users: see section 2 of INSTALL.md (plugin).

Thanks,
Wallisson
