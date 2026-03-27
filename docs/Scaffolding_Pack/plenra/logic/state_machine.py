from __future__ import annotations


VALID_LEAD_STATES = [
    "new",
    "contacted",
    "qualified",
    "proposal_sent",
    "won",
    "lost",
    "cooldown",
]


def next_lead_state(current_state: str, signal: str) -> str:
    transitions = {
        ("new", "contact_made"): "contacted",
        ("contacted", "qualified"): "qualified",
        ("qualified", "proposal_sent"): "proposal_sent",
        ("proposal_sent", "deal_won"): "won",
        ("proposal_sent", "deal_lost"): "lost",
        ("contacted", "no_response"): "cooldown",
    }
    return transitions.get((current_state, signal), current_state)
