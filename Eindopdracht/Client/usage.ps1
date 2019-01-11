$proc = Get-Counter -Counter "\Processor(_Total)\% Processor Time" -SampleInterval 4
$cpu=($proc.readings -split ":")[-1]

$system = Get-WmiObject win32_OperatingSystem
$TotaalAantalMemory = $system.TotalVisibleMemorySize
$VrijAantalGeheugen = $system.FreePhysicalMemory
$GebruiktAantalGeheugen = $TotaalAantalMemory - $VrijAantalGeheugen
$GebruiktAantalGeheugenProcenten = [math]::Round(($GebruiktAantalGeheugen / $TotaalAantalMemory) * 100,1)

Write-Host "CPU:" $cpu
Write-Host "Memory:" $GebruiktAantalGeheugenProcenten