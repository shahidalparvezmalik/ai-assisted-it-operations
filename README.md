# AI-Assisted IT Operations

![AI-Assisted IT Operations banner](docs/images/ai-assisted-it-operations-banner.png)

> A portfolio proof of concept exploring how AI can assist IT Operations teams with incident analysis, Service Desk workflows and operational decisions, while keeping people accountable for decisions and actions.

**Author:** Shahid Al Parvez Malik  
**Focus:** IT Operations | ITSM | Service Delivery | Responsible AI

> **Status:** Project in progress. This repository is a proof-of-concept workspace, not a production deployment. Do not use it with live services or sensitive operational data.

## Why this project

Operations teams see incidents, alerts, service requests and infrastructure signals in different places. AI may help summarize that information and suggest what an analyst should check next. It can also make a confident recommendation from incomplete or misleading data.

This project explores a controlled workflow: use AI for assistance, keep recommendations reviewable, and require human authorization for consequential actions.

## Scope

The proof of concept is intended to explore:

- Incident summarization and analysis support
- Service Desk workflow assistance
- Contextual recommendations for operational decisions
- Confidence and evidence visibility
- Human review and approval boundaries
- Auditable records of recommendations and decisions

Specific implemented capabilities will be documented here as they are built. No model, integration, performance result or production use is claimed at this stage.

## Proposed workflow

```text
Operational signal / ticket
          ↓
Gather permitted context
          ↓
Summarize and analyze
          ↓
Show evidence, uncertainty and recommendation
          ↓
Human reviews and decides
          ↓
Record decision and outcome
```

Any future action execution should be separately gated by policy, risk and authorization. The initial scope is decision support, not unrestricted autonomous remediation.

## Guardrails

- Use synthetic or sanitized examples; never commit confidential employer, customer or personal data.
- Keep the source signal and supporting evidence visible alongside AI-generated suggestions.
- Treat model output as untrusted advice, not as an instruction or an authoritative record.
- Escalate low-confidence, high-impact or security-sensitive cases to a person.
- Do not perform changes to production systems from this proof of concept.
- Measure usefulness through reviewable operational outcomes, not the number of generated recommendations.

## Repository contents

- `README.md` — project scope, principles and current status
- `docs/LINKEDIN_ARTICLE.md` — companion article draft
- `docs/LINKEDIN_SHORT_POST.md` — short LinkedIn promotion draft
- `docs/LINKEDIN_GROUPS_POST.md` — LinkedIn group post draft
- `docs/LINKEDIN_NETWORK_BLURB.md` — text for “Tell your network what your article is about”
- `docs/images/ai-assisted-it-operations-banner.png` — project banner

## LinkedIn article

[AI-Assisted IT Operations: Keeping Human Judgment in the Loop](docs/LINKEDIN_ARTICLE.md)

The article is a draft saved in this repository. It has not yet been published on LinkedIn. Add the article's LinkedIn URL to the short and group post drafts after publishing.

## About the author

Shahid Al Parvez Malik is a Senior IT Infrastructure & Service Delivery Manager with experience across IT infrastructure, operations, ITSM and service delivery. This project is a portfolio exploration of practical AI assistance with governance and human oversight.

- GitHub profile: https://github.com/shahidalparvezmalik
- Professional portfolio: https://shahidalparvezmalik.com/

## Suggested GitHub topics

`ai-assisted-it-operations` `it-operations` `itsm` `service-desk` `incident-management` `responsible-ai` `human-in-the-loop` `automation`

## Hashtags

Use where suitable in LinkedIn copy: #IrishTech #IrishITTech #Ireland
