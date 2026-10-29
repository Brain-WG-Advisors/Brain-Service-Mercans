# Refresh the TOC and page fields of LT-SIR-001-v1.1.docx with Microsoft Word (COM), then save.
# Order: python build_sir_docx_lt.py -> this script -> python finalize_sir_docx.py
param([string]$Path = (Join-Path $PSScriptRoot "LT-SIR-001-v1.1.docx"))
$w = New-Object -ComObject Word.Application
$w.Visible = $false
$w.DisplayAlerts = 0
try {
  $d = $w.Documents.Open($Path, $false, $false, $false)
  if ($d.TablesOfContents.Count -ge 1) { $d.TablesOfContents.Item(1).Update() }
  $d.Fields.Update() | Out-Null
  "pages=" + $d.ComputeStatistics(2)
  $d.Save()
  $d.Close()
} finally { $w.Quit() }
