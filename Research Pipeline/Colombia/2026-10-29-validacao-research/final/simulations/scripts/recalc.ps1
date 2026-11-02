param([string]$Path)
$x = New-Object -ComObject Excel.Application
$x.Visible = $false
$x.DisplayAlerts = $false
try {
  $wb = $x.Workbooks.Open($Path)
  $x.CalculateFull()
  $wb.Save()
  $wb.Close($true)
  "recalculated: $Path"
} finally {
  $x.Quit()
  [System.Runtime.Interopservices.Marshal]::ReleaseComObject($x) | Out-Null
}
