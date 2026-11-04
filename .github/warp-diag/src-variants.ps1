# Variants of a game exe built on this runner, 8 starts each. Usage: src-variants.ps1 -Exe path -List "name|A=1;B=2" ...
param([Parameter(Mandatory)][string]$Exe, [Parameter(Mandatory)][string[]]$List, [int]$Count = 8)
foreach ($item in $List) {
  $name, $vars = $item -split '\|', 2
  # each variant in a fresh process so that environment variables do not leak into the next one
  pwsh -NoProfile -File "$PSScriptRoot\variant.ps1" -Exe $Exe -Name $name -Vars $vars -Count $Count -TimeoutSecs 150
}
