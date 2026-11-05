$x = New-Object -ComObject Excel.Application
$x.Visible = $false; $x.DisplayAlerts = $false
$w = $x.Workbooks.Open("C:\Users\instituto\Documents\brain-service\Research Pipeline\USA\US-compliance\06-payslip\US_Compliance_Payslip_Generator.xlsx", 0, $true)
$s = $w.Worksheets.Item("United States (EN)")
$s.PageSetup.Zoom = $false; $s.PageSetup.FitToPagesWide = 1; $s.PageSetup.FitToPagesTall = 2
$s.ExportAsFixedFormat(0, "C:\Users\instituto\Documents\brain-service\Research Pipeline\USA\US-compliance\06-payslip\_build\_scratch\en.pdf")
Write-Output ("net value: " + $s.Range("H2").Value2 + " | H22 " + $s.Range("H22").Value2)
$w.Close($false); $x.Quit()
