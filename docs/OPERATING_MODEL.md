# AI-Assisted IT Operations operating model

This document describes a proposed operating model for the proof of concept. It is guidance for design and discussion, not an approved organizational policy. The repository currently has no live integrations or action execution.

## Purpose

Use AI assistance to help an operations analyst review an incident or service-desk case. Keep the source evidence visible, make uncertainty explicit, and leave operational decisions with accountable people.

## Roles

| Role | Proposed responsibility |
|---|---|
| Service Desk analyst | Validate the request, confirm context, review suggestions, and record corrections or decisions. |
| Incident or operations lead | Confirm service impact, coordinate investigation, and decide when escalation is needed. |
| Service owner | Supply service criticality, dependencies, and business-impact context. |
| Policy owner / approver | Define allowed use, approval thresholds, and who may authorize consequential actions. |
| Reviewer | Periodically assess recommendation quality, overrides, escalation patterns, and audit records. |

Roles may be combined in a small team. The proof of concept does not define organizational authority or replace existing change, incident, security, or access-control procedures.

## Proposed case workflow

1. **Intake:** Record a synthetic or sanitized incident/request and its source.
2. **Context:** Gather only permitted information; distinguish observed facts from user-entered statements and missing data.
3. **Analysis:** Present an AI-generated summary or recommendation separately from the source evidence.
4. **Review:** An analyst checks the evidence, uncertainty, impact, and recommendation. The analyst can amend, reject, or escalate it.
5. **Authorization:** Any consequential or privileged action stays outside this proof of concept and follows the organization's approved authorization path.
6. **Record:** Preserve the recommendation, evidence references, human decision, approver when relevant, and outcome for later review.

## Minimum controls

- Do not submit confidential employer, customer, personal, credential, or production-system data to an unapproved model.
- Keep source facts and generated text distinguishable.
- Do not treat model confidence as a calibrated probability or proof of correctness.
- Escalate when evidence is incomplete, contradictory, low-confidence, security-sensitive, or high-impact.
- Do not execute, retry, or change production operations from this repository.
- Record human corrections and decisions; do not silently overwrite the original case.
- Set retention, access, and redaction rules before testing with anything beyond synthetic data.

## Evaluation measures to define before testing

- Factual agreement of summaries with the supplied evidence
- Unsupported claims and missing evidence references
- Analyst correction / override rate
- Appropriate escalation of high-impact or uncertain cases
- Time to reach a reviewed decision
- Completeness of decision and audit records

No performance targets or achieved results are claimed. Define a labeled test set and review method before reporting accuracy or time savings.

## Current state and next design gate

This repository is currently a documentation-led proof of concept. It does not contain a runnable AI model, synthetic case dataset, provider integration, unit tests, or CI workflow yet. Before adding these, choose a narrow scenario that stays distinct from the existing IT Service Desk automation and AgenticOps repositories; then specify its input schema, evaluation cases, and human-review behavior.
