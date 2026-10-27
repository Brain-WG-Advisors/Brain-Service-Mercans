# Rascunho — feedback à Manju: Mammoet Montage P09 (set V12) — 2026-10-20

> ⚠️ SUPERADO em 20/10: FND-01, FND-02, FND-05 e FND-06 foram retirados (ver correcoes.md 2026-10-20). Não usar este rascunho; a resposta foi enviada pelo usuário no chat.

## Base conferida (lida pessoalmente)
- `G:\Meu Drive\file\Mammoet_Montage_P09_2025_Forensic_Validation_Report_Mercans_v1.1_2026-10-20.docx` (+ Validation Register, Six-Way Tie, Confirmation Gates, pack zip; 10:28). Set validado: Mammoet_Montage_P09_2025_V12_20261020 + corrections log v1.1. Nederland fora do escopo.
- 96 testes: 85 Pass / 4 Obs / 2 Fail / 5 N/T. Gates G01–G10, G13, G14 PASS; G11a/b e G12a/b SKIPPED (sem templates de referência).
- Fail: FND-01 (OpgRchtVakBsl declarado zero; X-11/X-12, 54 de 74). Obs: FND-02 (P01–P06 bijtelling sem dedução da contribuição), FND-03 (data de criação da mensagem antes do fim do tijdvak), FND-04 (2559 sem Whk beschikking; €114,86, 7 empregados), FND-05 (reserva de vakantiegeld ≠ 8%), FND-06 (holerite de 10000726 com catálogo 0,00).
- F-16 (LnInGld = fiscal wage, 681/681, 135 carros): está no relatório **Mammoet Nederland** P09 v2.0 (Downloads, "Mammoet Nederland B.V. … 686 income relations"), não na Montage. Na Montage o teste equivalente F-13 (LnLbPh = LnInGld + WrdLn − aftrekposten) passa em 6/6; F-13b 56/56.

## Rascunho (EN, para colar — não enviado)
Hi Manju, feedback on Montage P09 (set V12 + corrections log v1.1). Validation pack is in the folder I shared.

- Everything ties: net pay, bank details, wage types and GL across all six reports; SEPA, GL and premium arithmetic pass. 96 tests: 85 pass, 4 observations, 2 fails, 5 not testable (missing reference files).
- One defect to fix before filing: FND-01, the holiday-allowance accrual (OpgRchtVakBsl) is declared as zero.
- Also to fix: FND-03, the message creation date is before the end of the tijdvak.
- Observations needing a decision or evidence: P01–P06 car benefit not reduced by the employee contribution (FND-02), employee WGA 2559 withheld without the Whk beschikking (€114.86, 7 employees, FND-04), holiday reservation not 8% (FND-05), payslip car header of 10000726 shows catalogue value 0.00 (FND-06).
- F-16: it doesn't occur in Montage. The kolom 3 check (LnInGld + WrdLn − deductions = LnLbPh) passes on all Montage relations. The F-16 text with 681 relations and 135 car users is from the Nederland P09 v2.0 report.

## Acréscimo (20/10, após ler o chat claude.ai NL AUTOMATION, msg de 13:06)
O FND-01 é regressão do V12: a nossa V5.1 declarava o OpgRchtVakBsl; o V12 do time perdeu. Mesmo run e pagamentos iguais (SEPA byte-idêntico à V5.1). Linha opcional para o rascunho:
> FND-01 is new in V12: our V5.1 of the same run declared the holiday-allowance accrual, so it can be taken from there.
