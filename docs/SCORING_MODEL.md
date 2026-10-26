# Priority rules and limits

The demo applies this fixed, deterministic matrix to the declared `impact` and `urgency` fields. It does not infer either field from the case summary.

| Impact / urgency | high | medium | low |
|---|---|---|---|
| high | P1 (high risk) | P2 (high risk) | P2 (high risk) |
| medium | P2 (high risk) | P3 (medium risk) | P4 (low risk) |
| low | P2 (high risk) | P4 (low risk) | P4 (low risk) |

This rule is a teaching baseline only; it is not an organizational severity policy, ITIL standard, or calibrated risk model.

## Output behavior

- Every case requires human review, regardless of suggested priority.
- P1/P2 prompts ask for an incident or operations lead to review; P3/P4 prompts suggest analyst triage.
- Missing evidence is called out rather than inferred.
- The report preserves the input evidence note and lists the rule-based suggestion separately.
- The tool has no remediation or integration code. `action_executed` is always false.

Do not use these outputs to make live service decisions. Define and validate local policies, evaluation cases, and approval procedures before any real operational use.
