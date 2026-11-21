# Build a shippable release of aion2-menu
param([string]$Version = "0.6.3")

$ErrorActionPreference = "Stop"
Write-Host "Building aion2-menu $Version"

python -m pip install --upgrade build
python -m build --wheel --outdir dist
Copy-Item "config/default.yaml" -Destination "dist/default.yaml" -Force
Copy-Item "offsets/global_offsets.json" -Destination "dist/global_offsets.json" -Force

Write-Host "Artifacts:"
Get-ChildItem dist | Select-Object Name, Length