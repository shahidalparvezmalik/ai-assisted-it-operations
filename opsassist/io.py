"""CSV input validation and review-only report generation."""

from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Iterable, Mapping

from .assessment import assess_case

_REQUIRED_COLUMNS = {"case_id", "service", "summary", "impact", "urgency", "evidence"}
_OUTPUT_COLUMNS = [
    "case_id", "created_at", "service", "summary", "impact", "urgency",
    "recommended_priority", "risk_level", "evidence_status", "evidence_summary",
    "missing_context", "recommended_next_step", "human_review_required", "action_executed",
]


def load_cases(path: str | Path) -> list[dict[str, str]]:
    """Load and validate cases from a UTF-8 CSV file."""
    with Path(path).open("r", encoding="utf-8-sig", newline="") as source:
        reader = csv.DictReader(source)
        if reader.fieldnames is None:
            raise ValueError("input CSV must include a header row")
        missing_columns = sorted(_REQUIRED_COLUMNS.difference(reader.fieldnames))
        if missing_columns:
            raise ValueError(f"input CSV is missing required columns: {', '.join(missing_columns)}")
        cases = [dict(row) for row in reader]

    if not cases:
        raise ValueError("input CSV contains no cases")

    seen_ids: set[str] = set()
    for line_number, case in enumerate(cases, start=2):
        try:
            assessment = assess_case(case)
        except ValueError as exc:
            raise ValueError(f"invalid case on CSV line {line_number}: {exc}") from exc
        case_id = str(assessment["case_id"])
        if case_id in seen_ids:
            raise ValueError(f"duplicate case_id on CSV line {line_number}: {case_id}")
        seen_ids.add(case_id)
    return cases


def write_reports(cases: Iterable[Mapping[str, str]], output_dir: str | Path) -> dict[str, Path]:
    """Write assessments, a summary, and a blank human-review template."""
    records = [assess_case(case) for case in cases]
    if not records:
        raise ValueError("at least one case is required to create reports")

    destination = Path(output_dir)
    destination.mkdir(parents=True, exist_ok=True)
    assessments_path = destination / "case_assessments.csv"
    summary_path = destination / "executive_summary.json"
    review_path = destination / "review_log_template.csv"

    with assessments_path.open("w", encoding="utf-8", newline="") as target:
        writer = csv.DictWriter(target, fieldnames=_OUTPUT_COLUMNS)
        writer.writeheader()
        for record in records:
            row = dict(record)
            row["missing_context"] = "; ".join(record["missing_context"])
            row["human_review_required"] = str(record["human_review_required"]).lower()
            row["action_executed"] = str(record["action_executed"]).lower()
            writer.writerow(row)

    by_priority = {priority: 0 for priority in ("P1", "P2", "P3", "P4")}
    for record in records:
        by_priority[str(record["recommended_priority"])] += 1
    summary = {
        "assessment_method": "transparent_rules_baseline",
        "synthetic_demo": True,
        "cases_assessed": len(records),
        "by_recommended_priority": by_priority,
        "human_review_required": len(records),
        "actions_executed": 0,
        "limitations": [
            "This is a deterministic demonstration, not an AI model or operational policy.",
            "Priority suggestions require human review and must not trigger actions.",
            "Synthetic examples do not establish real-world accuracy or impact.",
        ],
    }
    summary_path.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")

    with review_path.open("w", encoding="utf-8", newline="") as target:
        writer = csv.DictWriter(
            target,
            fieldnames=["case_id", "reviewer", "decision", "notes", "reviewed_at"],
        )
        writer.writeheader()
        for record in records:
            writer.writerow({
                "case_id": record["case_id"],
                "reviewer": "",
                "decision": "",
                "notes": "",
                "reviewed_at": "",
            })

    return {
        "assessments": assessments_path,
        "summary": summary_path,
        "review_template": review_path,
    }
