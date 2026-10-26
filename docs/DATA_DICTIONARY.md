# Input and output data dictionary

All examples in `data/cases.csv` are fabricated for demonstration. Do not replace them with employer, customer, personal, security-sensitive, or production data without approved safeguards.

## Input CSV

| Field | Required | Meaning / validation |
|---|---:|---|
| `case_id` | Yes | Unique synthetic case identifier. |
| `created_at` | No | Example timestamp, retained as text; no timezone or chronology analysis is performed. |
| `service` | Yes | Synthetic service label. |
| `summary` | Yes | Short case description; the baseline does not interpret natural language. |
| `impact` | Yes | `low`, `medium`, or `high`. |
| `urgency` | Yes | `low`, `medium`, or `high`. |
| `evidence` | Yes column; value may be blank | Synthetic evidence note. Blank values are flagged as missing context. |

The loader rejects a missing required column, an empty file, invalid impact/urgency values, required fields left blank, and duplicate case IDs.

## Generated artifacts

The command writes three files under `reports/` (or the directory passed to `--output-dir`):

- `case_assessments.csv` — one transparent priority suggestion per case; includes the evidence string, missing-context flag, next-step prompt, mandatory human review, and `action_executed=false`.
- `executive_summary.json` — case counts by suggested priority, method and limitations; `actions_executed` is always zero.
- `review_log_template.csv` — blank fields for a human reviewer to record a decision, notes, and review time. The program does not fill in or approve those fields.

Generated reports may contain source text supplied in the CSV. Use synthetic inputs only, and review outputs before sharing them.
