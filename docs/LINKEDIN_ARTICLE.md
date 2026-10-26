# AI-Assisted IT Operations: A Small Rules-Based Demo

**Human review by design: making incident-priority suggestions transparent without automating decisions.**

**By Shahid Al Parvez Malik**

> Editorial source copy for review. Updating this repository file does not publish or change a LinkedIn article.

An incident priority can look precise even when the case is missing important context. A ticket may describe a symptom without showing its impact. Evidence may be incomplete. A suggested fix may be safe in a test environment but risky in production.

For an analyst, the useful question is not simply *“What priority did the tool assign?”* It is:

> **What evidence supports the suggestion—and what must remain a human decision?**

## A small, transparent workflow

I built a runnable command-line proof of concept using seven fabricated incident cases. It validates required fields, applies an explicit impact-and-urgency matrix, preserves the evidence supplied with each case, and flags missing context rather than filling gaps with assumptions.

For each case, the CLI produces a suggested priority and review flags. It writes an assessment report, a summary, and a blank template where a human reviewer can record a later decision.

In the bundled sample run, the priority counts are **P1=1, P2=3, P3=1, and P4=2**. Every case requires human review. The program executes **zero actions**.

Those counts show what the sample code did; they do not demonstrate accuracy, better service outcomes, or production readiness.

## Why make the rules visible?

The baseline uses the impact and urgency values supplied in the input. It does not infer them from ticket narratives, interpret free text, or call an AI model.

That boundary is deliberate. An analyst can inspect the inputs behind a suggestion, review the evidence note, and challenge the result. If evidence is missing, the tool flags it rather than inventing an answer.

The workflow is simple:

**Synthetic case → Validate fields → Apply transparent rules → Show evidence and suggestion → Human review**

A priority suggestion is not approval. The blank review template is not proof that a review occurred. Any operational action would need its own authorization and verification process; this demo has no action capability.

## What the demo does—and does not—show

It demonstrates input validation, a fixed priority matrix, seven synthetic case assessments, review flags, CSV/JSON reports, a human-review template, and unit tests.

It does **not** connect to an ITSM platform, read live infrastructure data, interpret ticket narratives, use an AI model, or remediate anything. The cases and evidence are fabricated. The matrix is an illustrative baseline, not an organizational severity policy. The tests check software behavior, not the quality of real incident decisions.

A working script is useful evidence of implementation. It is not evidence of AI capability or production suitability.

## What a responsible next step would require

Before considering a model, external system, or real data, an organization would need an analyst-reviewed evaluation set, clear data-handling rules, agreed measures, and an approval process. Measures could include evidence fidelity, missing-context detection, consistency, and how often analysts override suggestions.

That evaluation is future work—not a capability of this proof of concept.

## Try the project

The repository contains the code, seven sample cases, tests, scoring notes, and run instructions: [AI-Assisted IT Operations on GitHub](https://github.com/shahidalparvezmalik/ai-assisted-it-operations).

Requires Python 3.10 or later:

```bash
python -m unittest discover -v
python -m opsassist.cli --input data/cases.csv --output-dir reports
```

The aim is modest: make the suggestion visible, preserve the evidence, and keep the decision with a person.

---

**About the author:** Shahid Al Parvez Malik is a Senior IT Infrastructure & Service Delivery Manager with 20+ years of professional IT experience across infrastructure, IT Operations, ITSM, service delivery, systems administration, networking, technical support, procurement, and vendor management.

[GitHub profile](https://github.com/shahidalparvezmalik) · [Professional portfolio](https://shahidalparvezmalik.com/)

#ITOperations #ITInfrastructure #ITSM #ServiceDelivery #ResponsibleAI #HumanOversight #Automation #IrishTech #IrishITTech #Ireland
