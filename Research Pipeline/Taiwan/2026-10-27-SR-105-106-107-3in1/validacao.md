# Validação XML / pacote — 2026-10-27

Comandos: `python -I scripts/validate.py <base> <v1.1>` e `validate_workbook.py <v1.1> --quiet` (mercans-artifact-toolkit).

## SR-105 — TW - SI electronic filing Salary Adjustment specification v1.1.xlsx
```
5af6c892e8fe8955a39b75e6347ba775 *TW - SI electronic filing Salary Adjustment specification v1.1.xlsx
a8414b1c322c47f7d1945713cd644cb0 *C:/Users/instituto/Documents/brain-service/raw/docs/drive-exports/2026-10-27/TW - SI electronic filing Salary Adjustment specification.xlsx
  media     base=1 nova=1
  drawings  base=4 nova=4
  comments  base=1 nova=1
  vml       base=1 nova=1
  threaded  base=0 nova=0
  abas: ['Version Control', 'Report Matrix', 'Specification', 'Options']
  imagens em Version Control 1
  Version Control 14: 1.1 2026-10-27 00:00:00 | Draft | Wallisson Gomes | date? True
  B6='Period' em lista: True
  B7='XLSX' em lista: True
  B11='Electronic: Upload online ' em lista: True
RESULTADO: OK
--- toolkit (só C29 esperado: marcadores TO BE CONFIRMED pedidos):
  [BLOCKER] C29/residual-marker  Specification!L5
  [BLOCKER] C29/residual-marker  Specification!L18
  [BLOCKER] C29/residual-marker  Specification!L23
  [BLOCKER] C29/residual-marker  Specification!L36
  [BLOCKER] C29/residual-marker  Specification!L38
  [BLOCKER] C29/residual-marker  Specification!A45
VERDICT   FAIL  (blocker=6 major=0 minor=0)
```

## SR-106 — TW - SI Termination specification v1.1.xlsx
```
1f943ccee7c9104cd334a643c721fd47 *TW - SI Termination specification v1.1.xlsx
10d1865cee8c97136496c0de2cd5dcce *C:/Users/instituto/Documents/brain-service/raw/docs/drive-exports/2026-10-27/TW - SI Termination specification.xlsx
  media     base=1 nova=1
  drawings  base=4 nova=4
  comments  base=2 nova=2
  vml       base=2 nova=2
  threaded  base=0 nova=0
  abas: ['Version Control', 'Report Matrix', 'Spec', 'Options']
  imagens em Version Control 1
  Version Control 14: 1.1 2026-10-27 | Draft | Wallisson Gomes | date? False
  B6='Period' em lista: True
  B7='XLSX' em lista: True
  B11='Electronic: Upload online ' em lista: True
RESULTADO: OK
--- toolkit (só C29 esperado: marcadores TO BE CONFIRMED pedidos):
  [BLOCKER] C29/residual-marker  Spec!F5
  [BLOCKER] C29/residual-marker  Spec!F24
  [BLOCKER] C29/residual-marker  Spec!F29
  [BLOCKER] C29/residual-marker  Spec!F44
  [BLOCKER] C29/residual-marker  Spec!F47
VERDICT   FAIL  (blocker=5 major=0 minor=0)
```

## SR-107 — TW - SI electronic filing Joiner Specification v1.1.xlsx
```
cf497ce651e1b42236f5b75730090817 *TW - SI electronic filing Joiner Specification v1.1.xlsx
575c1a2e40caf2cc383c9d8b861c431e *C:/Users/instituto/Documents/brain-service/raw/docs/drive-exports/2026-10-27/TW - SI electronic filing Joiner Specification.xlsx
  media     base=1 nova=1
  drawings  base=5 nova=4
  comments  base=2 nova=2
  vml       base=2 nova=2
  threaded  base=1 nova=1
  abas: ['Version Control', 'Report Matrix', 'Spec', 'Options']
  imagens em Version Control 1
  Version Control 14: 1.1 2026-10-27 00:00:00 | Draft | Wallisson Gomes | date? True
  B6='Period' em lista: True
  B7='XLSX' em lista: True
  B11='Electronic: Upload online ' em lista: True
RESULTADO: OK
--- toolkit (só C29 esperado: marcadores TO BE CONFIRMED pedidos):
  [BLOCKER] C29/residual-marker  Report Matrix!B14
  [BLOCKER] C29/residual-marker  Spec!F4
  [BLOCKER] C29/residual-marker  Spec!F7
  [BLOCKER] C29/residual-marker  Spec!F10
  [BLOCKER] C29/residual-marker  Spec!F12
  [BLOCKER] C29/residual-marker  Spec!F14
  [BLOCKER] C29/residual-marker  Spec!F19
  [BLOCKER] C29/residual-marker  Spec!F22
  [BLOCKER] C29/residual-marker  Spec!F24
  [BLOCKER] C29/residual-marker  Spec!F25
  [BLOCKER] C29/residual-marker  Spec!F28
  [BLOCKER] C29/residual-marker  Spec!F29
  [BLOCKER] C29/residual-marker  Spec!F30
  [BLOCKER] C29/residual-marker  Spec!F31
VERDICT   FAIL  (blocker=14 major=0 minor=0)
```
