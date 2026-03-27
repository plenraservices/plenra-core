from __future__ import annotations


TRANSITIONS = {
    ("new", "contact_made"): "contacted",
    ("contacted", "qualified"): "qualified",
    ("qualified", "proposal_sent"): "proposal_sent",
    ("proposal_sent", "deal_won"): "won",
    ("proposal_sent", "deal_lost"): "lost",
    ("contacted", "no_response"): "cooldown",
}


def next_lead_state(current_state: str, signal: str) -> str:
    return TRANSITIONS.get((current_state, signal), current_state)
