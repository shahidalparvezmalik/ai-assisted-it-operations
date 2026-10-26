# Human Review by Design: A Rules-Based Baseline for IT Operations Triage

**A priority suggestion is not a decision.** In IT Operations, useful decision support must show its evidence, make uncertainty visible, and leave accountability with people.

**By Shahid Al Parvez Malik**

> Editorial source copy for review. Updating this file does not publish or change a LinkedIn article.

Incident triage often starts with incomplete information. A ticket may describe a symptom without showing its scope. An alert may be noisy. A suggested priority can look precise even when key context is missing.

I built a small, runnable proof of concept to make one boundary concrete:

> **What can a tool suggest—and what must remain a human decision?**

## A small, transparent workflow

The demo uses seven fabricated incident cases. It validates required fields, applies an explicit impact-and-urgency matrix, preserves the supplied evidence, and flags missing context rather than filling gaps with assumptions.

For each case, it produces a priority suggestion and review flags. The CLI writes an assessment report, a summary, and a blank template for a human reviewer.

In the bundled sample run, the seven cases are distributed across the priority levels as **P1=1, P2=3, P3=1, and P4=2**. Every case is marked for human review. The program executes **zero actions**.

Those figures describe the sample run only. They do not measure accuracy, service improvement, or business impact.

## Why the rules are visible

The baseline uses the impact and urgency values supplied in the input. It does not infer them from the ticket summary, interpret free-text narratives, or call an AI model.

That is a deliberate first step. A reviewer can see the inputs behind a suggestion, inspect the evidence note, and challenge the result. Missing evidence stays visible. A priority suggestion is not approval, and a blank review template is not proof that a review took place.

The workflow is simple:

**Synthetic case → Validate fields → Apply transparent rules → Show evidence and suggestion → Human review**

## What this demonstration does—and does not—show

It demonstrates a deterministic CLI, a documented priority matrix, input validation, synthetic case assessments, reports, a human-review template, and unit tests.

It does **not** connect to an ITSM platform, read live infrastructure data, interpret ticket narratives, use an AI model, or remediate anything. The cases and evidence are fabricated. The matrix is an illustrative baseline, not an organizational severity policy. Tests verify code behavior, not the quality of real incident decisions.

That distinction matters: a working script demonstrates software behavior, not production readiness or the value of an AI system.

## Where a future evaluation should begin

Before considering a model or integration, an organization would need an analyst-reviewed evaluation set, clear data-handling boundaries, agreed measures, and an approval process. Measures might include evidence fidelity, missing-context detection, override patterns, and consistency across reviewed cases.

Any future model, external system, or real-data work would require a separate design and evaluation. It is not part of this proof of concept.

## Try the project

The repository includes the code, seven sample cases, tests, scoring notes, and run instructions:

[AI-Assisted IT Operations on GitHub](https://github.com/shahidalparvezmalik/ai-assisted-it-operations)

Requires Python 3.10 or later:

```bash
python -m unittest discover -v
python -m opsassist.cli --input data/cases.csv --output-dir reports
```

This is a review-only baseline: transparent rules, visible evidence, human review, and no action execution.

---

**About the author:** Shahid Al Parvez Malik is a Senior IT Infrastructure & Service Delivery Manager with 20+ years of professional IT experience across infrastructure, IT Operations, ITSM, service delivery, systems administration, networking, technical support, procurement, and vendor management.

[GitHub profile](https://github.com/shahidalparvezmalik) · [Professional portfolio](https://shahidalparvezmalik.com/)

#ITOperations #ITInfrastructure #ITSM #ServiceDelivery #ResponsibleAI #HumanOversight #Automation #IrishTech #IrishITTech #Ireland
