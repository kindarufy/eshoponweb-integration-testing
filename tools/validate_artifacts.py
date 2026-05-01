from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "docs/environment.md",
    "docs/test-plan.md",
    "docs/test-strategy.md",
    "docs/test-cases.md",
    "docs/security-checklist.md",
    "checklists/e2e-checklist.md",
    "postman/eshoponweb.smoke.postman_collection.json",
    "postman/eshoponweb.local.postman_environment.json",
    "reports/findings.csv",
    "reports/findings.md",
    "reports/test-report.md",
    "reports/anomalies.md",
]

REQUIRED_FINDINGS_COLUMNS = [
    "ID",
    "Title",
    "Type",
    "Severity",
    "Area",
    "Steps",
    "Expected",
    "Actual",
    "Evidence",
    "Status",
    "Comment",
]


def validate_required_files() -> None:
    missing = [path for path in REQUIRED_FILES if not (ROOT / path).is_file()]
    if missing:
        raise SystemExit(f"Missing required files: {', '.join(missing)}")


def validate_json(path: Path) -> None:
    with path.open(encoding="utf-8") as file:
        json.load(file)


def validate_findings_csv() -> None:
    path = ROOT / "reports/findings.csv"
    with path.open(encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        if reader.fieldnames != REQUIRED_FINDINGS_COLUMNS:
            raise SystemExit(
                "Invalid findings.csv columns. "
                f"Expected {REQUIRED_FINDINGS_COLUMNS}, got {reader.fieldnames}"
            )
        rows = list(reader)
        if not rows:
            raise SystemExit("findings.csv must contain at least one finding")
        empty_ids = [index + 2 for index, row in enumerate(rows) if not row["ID"].strip()]
        if empty_ids:
            raise SystemExit(f"findings.csv contains empty IDs on lines: {empty_ids}")


def main() -> None:
    validate_required_files()
    validate_json(ROOT / "postman/eshoponweb.smoke.postman_collection.json")
    validate_json(ROOT / "postman/eshoponweb.local.postman_environment.json")
    validate_findings_csv()
    print("All testing artifacts are valid.")


if __name__ == "__main__":
    main()
