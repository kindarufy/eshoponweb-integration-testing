#!/usr/bin/env bash
set -euo pipefail

ESHOP_ROOT="${1:-../eShopOnWeb}"

if [ ! -f "$ESHOP_ROOT/eShopOnWeb.sln" ]; then
  echo "eShopOnWeb solution was not found: $ESHOP_ROOT/eShopOnWeb.sln"
  echo "Usage: ./scripts/run-eshoponweb.sh /path/to/eShopOnWeb"
  exit 1
fi

cd "$ESHOP_ROOT"

echo "Building eShopOnWeb..."
dotnet restore eShopOnWeb.sln
dotnet build eShopOnWeb.sln

echo "Starting Web project..."
echo "For Admin UI checks, start PublicApi in a separate terminal if needed:"
echo "  cd $ESHOP_ROOT/src/PublicApi && dotnet run"
cd src/Web
dotnet run --launch-profile Web
