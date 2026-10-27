#!/bin/bash
# Copies the client's reports from ~/Downloads into 02-client-reports-raw/ (never read by Claude).
cd "$(dirname "$0")/.."
SRC="${1:-$HOME/Downloads}"
FILES=(
"Vertical G2N Dynamic 2026-09-01 - 2026-09-30.xlsx"
"Variance Per Employee Net.xlsx"
"Variance Per Employee Gross.xlsx"
"Variance on Total Statutory.xlsx"
"Severance Massive Calculation Structure September 2026.xlsx"
"Pac Reports.xlsx"
"OP BANCARIZADOS NÓMINA MENSUAL 2026-09-01 - 2026-09-30.pdf"
"Loans Balance New Report September 2026.xlsx"
"Leave Reimbursement Report September 2026.xlsx"
"ESS Report.xlsx"
"CCT Detailed Third Party Consolidada.xlsx"
"CARGA_MASIVA_AFC_202609.xlsx"
"Accumulated Report.xlsx"
"1764_PMI_Zero_Negative_Net_Pay_Report_202609.xlsx"
"1764_PMI_Leave_Absence_Report_.xlsx"
"1764_PMI_Duplicate_Bank_Accounts_Report_202609.pdf"
"1764_PMI_Detail_IBC_per_Employees_S.S._Report_202609.xlsx"
"1764_PMI_Base of Withholding 2026-09-01 - 2026-09-30.xlsx"
"1764_PMI_Bank_Payments_Report_202609.xlsx"
"1764_PMI_Bank_Payments_Report_202609.pdf"
"1764_Master_Data_Report_202609.xlsx"
)
ok=0; miss=0
for f in "${FILES[@]}"; do
  if [ -f "$SRC/$f" ]; then cp "$SRC/$f" "02-client-reports-raw/"; ok=$((ok+1)); else echo "NOT FOUND: $f"; miss=$((miss+1)); fi
done
echo "Copied $ok files to 02-client-reports-raw/ ($miss not found)."
echo "Next: python3 scripts/mask_reports.py"
