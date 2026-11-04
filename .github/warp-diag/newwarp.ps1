# The newest Microsoft.Direct3D.WARP NuGet package: put its x64 d3d10warp.dll next to the game's exe.
param([Parameter(Mandatory)][string]$ExeDir)
$ErrorActionPreference = 'Stop'
$idx = Invoke-RestMethod 'https://api.nuget.org/v3-flatcontainer/microsoft.direct3d.warp/index.json'
"versions: $($idx.versions -join ' ')"
$ver = ($idx.versions | Where-Object { $_ -notmatch '-' } | Select-Object -Last 1)
if (-not $ver) { $ver = $idx.versions | Select-Object -Last 1 }
$zip = "$env:RUNNER_TEMP\warp.zip"
Invoke-WebRequest "https://api.nuget.org/v3-flatcontainer/microsoft.direct3d.warp/$ver/microsoft.direct3d.warp.$ver.nupkg" -OutFile $zip
Expand-Archive $zip "$env:RUNNER_TEMP\warp" -Force
Get-ChildItem "$env:RUNNER_TEMP\warp" -Recurse -File | ForEach-Object { "  $($_.FullName.Substring($env:RUNNER_TEMP.Length)) $($_.Length)" }
$dll = Get-ChildItem "$env:RUNNER_TEMP\warp" -Recurse -Filter d3d10warp.dll | Where-Object { $_.FullName -match 'x64|amd64' } | Select-Object -First 1
if (-not $dll) { throw 'no x64 d3d10warp.dll in the package' }
Copy-Item $dll.FullName "$ExeDir\d3d10warp.dll"
"package $ver, d3d10warp.dll $($dll.VersionInfo.FileVersion) -> $ExeDir"
"system's:  $((Get-Item "$env:WINDIR\System32\d3d10warp.dll").VersionInfo.FileVersion)"
