# AI-assisted IT operations: a small rules-based demo

**LinkedIn article draft**  
**Author:** Shahid Al Parvez Malik

IT Operations teams make triage decisions with incomplete information. A ticket can describe a symptom without showing its scope. An alert may be noisy. A proposed fix can be harmless in a test environment and risky in production.

I wanted a small way to make one boundary concrete: what can a tool suggest, and what must stay with a person?

## What the demo does

I built a runnable command-line proof of concept using seven fabricated incident cases. It checks required fields, applies an explicit impact-and-urgency matrix, keeps the supplied evidence visible, and flags missing evidence. It writes a case assessment report, a summary, and a blank template for a human reviewer.

The sample run suggests priorities for all seven cases. Every case is marked for human review, and the program executes zero actions.

## What it does not do

Despite the project name, this first executable slice does not call an AI model. The priority suggestions come from fixed rules applied to the impact and urgency values in the input. It does not interpret ticket narratives, connect to a service-management platform, read live infrastructure data, or remediate anything.

That distinction matters. A working script with fabricated examples demonstrates software behavior, not production readiness, operational accuracy, or the value of an AI system.

## Why keep review in the workflow?

A priority suggestion is only useful when the analyst can inspect its inputs and challenge the result. Missing or conflicting evidence should remain visible rather than being filled in by assumption. Any real operational action would need its own policy, authorization, and verification controls; this demonstration has no action capability.

The example uses synthetic data only. Its matrix is a teaching baseline, not an organizational severity policy. The tests check the code paths and expected output, not the correctness of real incident decisions.

## Try the project

The repository includes the code, seven sample cases, unit tests, scoring notes, and run instructions:

https://github.com/shahidalparvezmalik/ai-assisted-it-operations

To run it, use Python 3.10 or later:

```bash
python -m unittest discover -v
python -m opsassist.cli --input data/cases.csv --output-dir reports
```

I am treating this as a small, review-only baseline. Any future work involving an AI model, external systems, or real data needs a separate design and evaluation before implementation.

## About the author

Shahid Al Parvez Malik is a Senior IT Infrastructure & Service Delivery Manager focused on IT infrastructure, IT Operations, ITSM, and service delivery.

GitHub: https://github.com/shahidalparvezmalik  
Professional portfolio: https://shahidalparvezmalik.com/

#ITOperations #ITInfrastructure #ITSM #ServiceDelivery #ResponsibleAI #HumanOversight #Automation #IrishTech #IrishITTech #Ireland
