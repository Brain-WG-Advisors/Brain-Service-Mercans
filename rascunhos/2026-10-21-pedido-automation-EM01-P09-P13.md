# Pedido ao AUTOMATION — aplicar EM-01 em P09–P13 (2026-10-21)

Decisão do usuário (21/10): aplicar a regra do Marko no EM-01 (hierarquia: Marko diretor, Manju gerente). Manju: "But EM 01 finding would have impact in all deliverables". Divergência com Gegevensspecificaties 2025 p. 121/102 e Handboek §11.2.9 fica registrada só no cérebro (log 21/10), não na nota.

## Texto para colar (não enviado)
PEDIDO — aplicar o EM-01 do Marko em P09–P13 (decisão da gestão)

Decisão: o EM-01 passa a ser aplicado como o Marko pede: LnInGld = LnLbPh − WrdLn em todas as inkomstenverhoudingen de P09 a P13, inclusive nos blocos de correção (é a opção B: 173 registros — P09 62, P10 13, P11 12, P12 48, P13 38). Na nota, não argumentar contra a regra.

Base: P09 V14, P10 V9, P11 V7 e P12/P13 V3 (20261021).

1. Alterar só o LnInGld nos XML; nada de G2N, holerite, GL, SEPA ou payment report. TotTeBet, TotGen, saldos e prêmios iguais (mostrar antes × depois por período).
2. Versões novas: P09 V15, P10 V10, P11 V8, P12 V4, P13 V4 (nome do zip com 20261021), cada uma com o Corrections Log atualizado.
3. Revalidar com o catálogo completo (98 testes): EM-01 = 0 em todos os períodos e nenhum teste piorando em relação à V3/versão anterior. Mostrar Pass/Fail/Obs/Não testável por período.
4. Nota v1.3: EM-01 corrigido conforme o relatório v3.0 (LnInGld = LnLbPh − WrdLn), sem argumentação contrária; o resto como na v1.2.
5. Entregar os SHA-256 dos zips, da nota e de cada XML. Não mexer no Drive. Sem "client confirmation".

## Resposta do AUTOMATION (21/10)
- EM-01 aplicado: 175 registros (não 173; +2 blocos P02/P03 do 727 que entraram no P13 V3 pelo EM-02): P09 62, P10 13, P11 12, P12 48, P13 40. Só o <LnInGld> mudou; coletivos iguais campo a campo; os outros 5 arquivos de cada set idênticos byte a byte.
- TotTeBet/TotGen iguais: P09 15.286/18.582; P10 14.997/15.268; P11 23.100/21.677; P12 16.070/23.513; P13 18.614/20.296.
- Catálogo 98 (anterior → novo, Pass/Fail/Obs/NT): P09 78/1/3/16 → 79/0/3/16; P10 83/2/3/10 → 84/1/3/10; P11 82/4/3/9 → 83/3/3/9; P12 81/4/3/10 → 82/3/3/10; P13 83/3/3/9 → 84/2/3/9. Única mudança: F-13 (= EM-01) Fail → Pass. Ele corrigiu o relato anterior: no P12 V3 o F-13 já falhava pela definição do catálogo.
- Fails restantes (já na nota): C-07 (P11/P12), E-06, G-14 (P11–P13); Obs F-07b, G-03, H-05.
- Nota v1.3 (10 p.): EM-01 como corrigido, sem argumento contrário (sem Handboek §11.2.x/"kolom").
- SHA-256: zips P09 V15 61d18847…, P10 V10 483fc186…, P11 V8 cab520bf…, P12 V4 abe37482…, P13 V4 ccbf34c7…; nota v1.3 51e50e46…; XML P09 56868583…, P10 f9e0b2a1…, P11 1d0fd36a…, P12 d319f013…, P13 e59b7426….
- No Drive: só trocar o XML de cada período.
