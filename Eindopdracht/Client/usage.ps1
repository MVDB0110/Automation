Get-WmiObject win32_processor | select LoadPercentage  | fl


$system = Get-WmiObject win32_OperatingSystem
$TotaalAantalMemory = $system.TotalVisibleMemorySize
$VrijAantalGeheugen = $system.FreePhysicalMemory
$GebruiktAantalGeheugen = $TotaalAantalMemory - $VrijAantalGeheugen
$GebruiktAantalGeheugenProcenten = [math]::Round(($GebruiktAantalGeheugen / $TotaalAantalMemory) * 100,1)

Write-host "Geheugen in gebruik: "  $GebruiktAantalGeheugenProcenten %