# E-mail ao time: skills v2.12 (versão final para envio — não enviado)

> Janela Pipeline, 2026-10-19. Substitui `2026-10-17-anuncio-pipeline-v2.12.md` (listava só 2 zips).
> Fonte de cada afirmação: `~/mercans-pipeline/dist/v2.12/CHANGELOG-v2.12.md` e `INSTALL.md`.
> Anexos: os 3 zips de `~/mercans-pipeline/dist/v2.12/chat/` (+ `INSTALL.md` e `CHANGELOG-v2.12.md`, opcional).
> Destinatários/canal: definir com o usuário.

---

**Subject:** Mercans compliance skills updated to v2.12

Hi team,

The Mercans compliance skills in Claude have been updated to v2.12. This version comes out of the France validation: the calculations were re-computed and compared with the official payroll engine, the DSN samples went through the official validator, and a risk-weighted sample of statements was re-checked against primary law. Every error that was ours was then checked against our own audit checks, and the gaps we found are now built into the skills.

**What you need to do**
In claude.ai or Claude Desktop, go to Customize → Skills and check that these three are there and switched on:
- **mercans-pipeline-methodology**: updated (replaces the version from 31 Aug)
- **mercans-compliance-workflow**: updated (replaces the version from 25 Aug)
- **mercans-artifact-toolkit**: new. It inspects and validates an uploaded WTC, DD, Report Spec, Payslip, CCG or SIR. It needs code execution switched on (Settings → Capabilities).

If you don't see them, upload the three attached zips via + Create skill → Upload a skill (do not unzip them). If you have an older copy of any of these, delete it so that only the new version is active.

**What changes in practice**
- **No silent skips.** A check that cannot run because a country lacks support (no machine-readable norm, no official validator, no code table) is now a FAIL, unless an exemption is recorded with a reason and an official source.
- **One source for every number.** Rates, ceilings and thresholds come from a single facts file and are tagged wherever they appear, so one correction reaches every artifact.
- **Special populations are asked every time.** Non-residents (including their social-security treatment), local regimes, employer type and size, special pay cycles, and changes during the year.
- **Codes and citations from the source.** Reporting codes must come from the authority's code table for the build year. Every article cited must be in the legal-basis register and in force.
- **Payslips.** Aligning a payslip to the Spain model never removes a statutory line, and the net must reconcile to the cent.

If you run the pipeline script: stop using `mercans_pipeline_v2_9.sh`; the current one is `mercans_pipeline_v2_12.sh`.

**Quick test:** open a new chat and ask *"What does Stage 9 do in pipeline v2.12, and when may a check be skipped?"* The answer should say that missing country support is a FAIL unless an exemption is recorded.

Any questions or anything that looks off, just reply to this email.

Thanks,
Wallisson
