"""Transparent, deterministic assessment baseline for synthetic cases."""

from __future__ import annotations

from typing import Mapping

_LEVELS = {"low", "medium", "high"}


def assess_case(case: Mapping[str, str]) -> dict[str, object]:
    """Assess one case without invoking a model or executing any action."""
    case_id = str(case.get("case_id", "")).strip()
    service = str(case.get("service", "")).strip()
    summary = str(case.get("summary", "")).strip()
    impact = str(case.get("impact", "")).strip().lower()
    urgency = str(case.get("urgency", "")).strip().lower()
    evidence = str(case.get("evidence", "")).strip()

    if not case_id or not service or not summary:
        raise ValueError("case_id, service, and summary are required")
    if impact not in _LEVELS:
        raise ValueError(f"impact must be one of: {', '.join(sorted(_LEVELS))}")
    if urgency not in _LEVELS:
        raise ValueError(f"urgency must be one of: {', '.join(sorted(_LEVELS))}")

    if impact == "high" and urgency == "high":
        priority = "P1"
    elif impact == "high" or urgency == "high":
        priority = "P2"
    elif impact == "medium" and urgency == "medium":
        priority = "P3"
    else:
        priority = "P4"

    risk_level = {"P1": "high", "P2": "high", "P3": "medium", "P4": "low"}[priority]
    next_step = {
        "P1": "Escalate to the incident lead now; verify service impact and evidence.",
        "P2": "Ask the operations lead to review impact and confirm escalation.",
        "P3": "Analyst review; collect missing context before deciding next steps.",
        "P4": "Standard analyst triage; monitor for new evidence or impact.",
    }[priority]
    missing_context = [] if evidence else ["supporting evidence"]

    return {
        "case_id": case_id,
        "created_at": str(case.get("created_at", "")).strip(),
        "service": service,
        "summary": summary,
        "impact": impact,
        "urgency": urgency,
        "recommended_priority": priority,
        "risk_level": risk_level,
        "evidence_status": "provided" if evidence else "missing",
        "evidence_summary": evidence or "No supporting evidence supplied.",
        "missing_context": missing_context,
        "recommended_next_step": next_step,
        "human_review_required": True,
        "action_executed": False,
    }
