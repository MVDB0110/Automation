$Cpu = Get-Counter -Counter "\Processor(_Total)\% Processor Time" -SampleInterval 4
$CpuPercentage=($Cpu.readings -split ":")[-1]

$system = Get-WmiObject win32_OperatingSystem
$TotaalAantalMemory = $system.TotalVisibleMemorySize
$VrijAantalGeheugen = $system.FreePhysicalMemory
$GebruiktAantalGeheugen = $TotaalAantalMemory - $VrijAantalGeheugen
$GeheugenPercentage = [math]::Round(($GebruiktAantalGeheugen / $TotaalAantalMemory) * 100,1)

$CpuPercentage
$GeheugenPercentage