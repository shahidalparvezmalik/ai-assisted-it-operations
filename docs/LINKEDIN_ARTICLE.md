# AI-Assisted IT Operations: Keeping Human Judgment in the Loop

**LinkedIn article draft**  
**Author:** Shahid Al Parvez Malik

IT Operations teams work with a steady stream of tickets, alerts, service requests and infrastructure signals. Each item carries useful context, but analysts still have to decide what matters, what to investigate and what action is safe.

AI can help with that work. It can summarize an incident, group related reports, surface relevant knowledge or suggest what to check next. The suggestion is only useful if an operator can see why it was made and decide whether to act on it.

## Assistance is not authority

An AI system can produce a clear answer from incomplete information. A ticket may describe a symptom but omit its scope. An alert may be noisy. A suggested fix may be appropriate for a test environment and risky in production.

That is why an AI recommendation should not silently become an operational decision. The workflow needs to show the evidence, uncertainty and possible impact, then put the decision in the hands of an accountable person when the risk calls for it.

## A practical operations workflow

A controlled AI-assisted workflow can follow a simple sequence:

1. Gather the permitted incident or service-desk context.
2. Summarize what is known and identify missing information.
3. Present relevant evidence and a recommendation.
4. Let an analyst review, correct or reject the recommendation.
5. Record the decision and, where applicable, check the outcome.

This does not require every step to be automated. In many cases, a useful first step is a better summary or a clearer handoff, not an automated change.

## Set the boundary before adding action

The boundary should depend on risk. A low-impact suggestion can be offered for review. A security-sensitive, privileged or service-impacting action needs stronger controls, and may need explicit human approval. If confidence is low or evidence conflicts, the system should make that visible and escalate rather than fill the gap with a guess.

Any future execution capability should be separated from the model's recommendation. Policy can determine whether an action is allowed; authorization can determine who may approve it; verification can check whether the intended result occurred. The system should keep an audit record of what it suggested, what the operator decided and what happened next.

## What I am exploring

I have started an **AI-Assisted IT Operations** proof of concept to explore incident analysis, Service Desk workflows and operational decision support with human oversight. The project is in progress. I am treating it as a design and learning exercise, not as a production deployment or a claim of measured operational results.

The repository is here: https://github.com/shahidalparvezmalik/ai-assisted-it-operations

My aim is to keep the project grounded in operational practice: make the recommendation understandable, keep the human accountable and record enough context to review the decision later. The next step is to build and test small examples using synthetic or sanitized data, then document what works and where the approach needs limits.

AI can help an operations team process information. It should not obscure who made the decision, what evidence supported it or who is responsible for the action.

## About the author

Shahid Al Parvez Malik is a Senior IT Infrastructure & Service Delivery Manager focused on IT infrastructure, IT Operations, ITSM and service delivery. This proof of concept explores practical AI assistance with appropriate governance and human oversight.

GitHub: https://github.com/shahidalparvezmalik  
Professional portfolio: https://shahidalparvezmalik.com/

#ITOperations #ITInfrastructure #ITSM #ServiceDelivery #ResponsibleAI #Automation #HumanOversight #IrishTech #Ireland
