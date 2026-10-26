import csv
import io
import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from opsassist.assessment import assess_case
from opsassist.cli import main
from opsassist.io import load_cases, write_reports


class AssessmentTests(unittest.TestCase):
    def test_high_impact_urgent_case_requires_review_and_never_executes_action(self):
        case = {
            "case_id": "CASE-001",
            "created_at": "2026-10-26T09:00:00Z",
            "service": "Identity",
            "summary": "Users cannot sign in",
            "impact": "high",
            "urgency": "high",
            "evidence": "Synthetic evidence: authentication errors increased.",
        }
        result = assess_case(case)
        self.assertEqual(result["recommended_priority"], "P1")
        self.assertEqual(result["risk_level"], "high")
        self.assertTrue(result["human_review_required"])
        self.assertFalse(result["action_executed"])
        self.assertEqual(result["evidence_summary"], case["evidence"])

    def test_priority_matrix_is_transparent(self):
        cases = [
            ("high", "high", "P1"),
            ("high", "medium", "P2"),
            ("high", "low", "P2"),
            ("medium", "high", "P2"),
            ("medium", "medium", "P3"),
            ("medium", "low", "P4"),
            ("low", "high", "P2"),
            ("low", "medium", "P4"),
            ("low", "low", "P4"),
        ]
        for impact, urgency, expected in cases:
            with self.subTest(impact=impact, urgency=urgency):
                record = {
                    "case_id": "CASE-X", "service": "Email", "summary": "Synthetic case",
                    "impact": impact, "urgency": urgency, "evidence": "Synthetic evidence",
                }
                self.assertEqual(assess_case(record)["recommended_priority"], expected)

    def test_missing_evidence_is_flagged(self):
        record = {
            "case_id": "CASE-X", "service": "Email", "summary": "Synthetic case",
            "impact": "medium", "urgency": "low", "evidence": "",
        }
        result = assess_case(record)
        self.assertEqual(result["evidence_status"], "missing")
        self.assertIn("supporting evidence", result["missing_context"])

    def test_invalid_impact_is_rejected(self):
        record = {
            "case_id": "CASE-X", "service": "Email", "summary": "Synthetic case",
            "impact": "urgent", "urgency": "low", "evidence": "Synthetic evidence",
        }
        with self.assertRaisesRegex(ValueError, "impact must be one of"):
            assess_case(record)


class ReportTests(unittest.TestCase):
    def test_load_cases_reads_and_validates_csv_rows(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "cases.csv"
            path.write_text(
                "case_id,created_at,service,summary,impact,urgency,evidence\n"
                "CASE-TEST,2026-10-26T09:00:00Z,Email,Mail delay,medium,low,Synthetic signal\n",
                encoding="utf-8",
            )
            cases = load_cases(path)
        self.assertEqual(len(cases), 1)
        self.assertEqual(cases[0]["case_id"], "CASE-TEST")

    def test_reports_include_review_gate_and_zero_actions(self):
        record = {
            "case_id": "CASE-REPORT", "service": "Email", "summary": "Synthetic case",
            "impact": "high", "urgency": "high", "evidence": "Synthetic evidence",
        }
        with tempfile.TemporaryDirectory() as directory:
            outputs = write_reports([record], Path(directory) / "reports")
            with outputs["summary"].open(encoding="utf-8") as source:
                summary = json.load(source)
            with outputs["assessments"].open(encoding="utf-8", newline="") as source:
                assessment = next(csv.DictReader(source))
            with outputs["review_template"].open(encoding="utf-8", newline="") as source:
                review = next(csv.DictReader(source))
        self.assertEqual(summary["cases_assessed"], 1)
        self.assertEqual(summary["human_review_required"], 1)
        self.assertEqual(summary["actions_executed"], 0)
        self.assertEqual(assessment["human_review_required"], "true")
        self.assertEqual(assessment["action_executed"], "false")
        self.assertEqual(review["case_id"], "CASE-REPORT")
        self.assertEqual(review["decision"], "")

    def test_repository_dataset_produces_review_only_outputs(self):
        repository = Path(__file__).resolve().parents[1]
        cases = load_cases(repository / "data" / "cases.csv")
        self.assertEqual(len(cases), 7)
        with tempfile.TemporaryDirectory() as directory:
            outputs = write_reports(cases, directory)
            with outputs["summary"].open(encoding="utf-8") as source:
                summary = json.load(source)
            with outputs["assessments"].open(encoding="utf-8", newline="") as source:
                rows = list(csv.DictReader(source))
        self.assertEqual(summary["actions_executed"], 0)
        self.assertEqual(summary["by_recommended_priority"], {"P1": 1, "P2": 3, "P3": 1, "P4": 2})
        self.assertEqual(summary["human_review_required"], 7)
        self.assertEqual(len(rows), 7)
        self.assertTrue(all(row["human_review_required"] == "true" for row in rows))
        self.assertTrue(all(row["action_executed"] == "false" for row in rows))


class CliTests(unittest.TestCase):
    def test_cli_runs_assessment_and_reports_output_paths(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "cases.csv"
            source.write_text(
                "case_id,created_at,service,summary,impact,urgency,evidence\n"
                "CASE-CLI,2026-10-26T09:00:00Z,Email,Mail delay,medium,low,Synthetic signal\n",
                encoding="utf-8",
            )
            output_dir = Path(directory) / "reports"
            with mock.patch("sys.stdout", new_callable=io.StringIO) as stdout:
                result = main(["--input", str(source), "--output-dir", str(output_dir)])
            self.assertEqual(result, 0)
            self.assertIn("Cases assessed: 1", stdout.getvalue())
            self.assertTrue((output_dir / "case_assessments.csv").is_file())


if __name__ == "__main__":
    unittest.main()
