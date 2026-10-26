# AI-Assisted IT Operations operating model

This is a proposed operating model for a portfolio proof of concept, not an approved organizational policy. The runnable demo uses synthetic records and a deterministic rules baseline. It has no AI model/provider integration, live-system connection, or action execution.

## Purpose

Help an operations analyst review a synthetic incident case. Keep source evidence visible, make missing context explicit, and leave decisions with accountable people.

## Roles

| Role | Proposed responsibility |
|---|---|
| Service Desk analyst | Validate the request, confirm context, review suggestions, and record corrections or decisions. |
| Incident or operations lead | Confirm service impact, coordinate investigation, and decide when escalation is needed. |
| Service owner | Supply service criticality, dependencies, and business-impact context. |
| Policy owner / approver | Define allowed use, approval thresholds, and who may authorize consequential actions. |
| Reviewer | Periodically assess recommendation quality, overrides, escalation patterns, and audit records. |

Roles may be combined in a small team. The proof of concept does not define organizational authority or replace existing change, incident, security, or access-control procedures.

## Demonstration workflow

1. **Intake:** Load a fabricated case from `data/cases.csv`.
2. **Validate:** Check required fields and declared impact/urgency values; flag missing supporting evidence.
3. **Assess:** Apply the fixed matrix in [`SCORING_MODEL.md`](SCORING_MODEL.md). The demo does not interpret narrative text or call an AI model.
4. **Review:** Present the suggested priority and evidence separately. Human review is mandatory for every case.
5. **Record:** Generate `review_log_template.csv` for a person to fill in separately. The program does not claim a review or approval occurred.
6. **Act:** No action execution is implemented. Any real operational action remains outside this demonstration and must follow approved organizational policy.

## Minimum controls

- Use only synthetic examples in the repository; never commit confidential employer, customer, personal, credential, or production-system data.
- Keep source facts and generated/derived values distinguishable.
- Treat model confidence as unavailable; the current rules do not generate a confidence score.
- Escalate when evidence is incomplete, contradictory, security-sensitive, or high-impact.
- Do not execute, retry, or change production operations from this repository.
- Record human corrections and decisions separately; do not silently overwrite source cases.
- Set retention, access, and redaction rules before testing with anything beyond synthetic data.

## Evaluation measures to define before extending the demo

- Agreement of suggested triage with a reviewed, locally approved reference set
- Unsupported conclusions and missing evidence references
- Analyst correction / override rate
- Appropriate escalation of high-impact or uncertain cases
- Time to reach a reviewed decision
- Completeness of decision and audit records

No performance targets or achieved results are claimed. The included cases validate software behavior only; they do not establish operational accuracy or time savings.

## Current state and next design gate

The repository includes a runnable command-line baseline, seven fabricated cases, automated unit tests, and a proposed GitHub Actions workflow. The baseline is deterministic rules code, not AI. It demonstrates input validation, evidence visibility, priority suggestions, mandatory human review, and zero action execution.

Before adding a model, external provider, live data, or wider workflow, choose a narrow scenario distinct from the existing IT Service Desk automation and AgenticOps repositories. Define the approved data boundary, evaluation set, and human-review behavior before implementing that extension.
