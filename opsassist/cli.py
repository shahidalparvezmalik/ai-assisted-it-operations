"""Command-line interface for the review-only incident briefing demo."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Sequence

from .io import load_cases, write_reports


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Create review-only assessments from synthetic incident cases."
    )
    parser.add_argument(
        "--input", default="data/cases.csv", help="Input cases CSV (default: data/cases.csv)."
    )
    parser.add_argument(
        "--output-dir", default="reports", help="Directory for generated reports (default: reports)."
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        cases = load_cases(args.input)
        outputs = write_reports(cases, args.output_dir)
    except (OSError, ValueError) as exc:
        parser.error(str(exc))

    print(f"Cases assessed: {len(cases)}")
    print("Assessment method: transparent rules baseline (not an AI model)")
    print("Human review required: yes; no actions are executed")
    for label, path in outputs.items():
        print(f"{label}: {Path(path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
