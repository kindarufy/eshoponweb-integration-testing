param(
    [string]$EshopRoot = "..\eShopOnWeb"
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$solution = Join-Path $EshopRoot "eShopOnWeb.sln"

if (-not (Test-Path $solution)) {
    Write-Error "eShopOnWeb solution was not found: $solution"
    Write-Host "Usage: .\scripts\run-eshoponweb.ps1 -EshopRoot C:\path\to\eShopOnWeb"
    exit 1
}

Push-Location $EshopRoot

Write-Host "Building eShopOnWeb..."
dotnet restore eShopOnWeb.sln
dotnet build eShopOnWeb.sln

Write-Host "Starting Web project..."
Write-Host "For Admin UI checks, start PublicApi in a separate terminal if needed:"
Write-Host "  cd $EshopRoot\src\PublicApi; dotnet run"

Set-Location "src\Web"
dotnet run --launch-profile Web

Pop-Location
