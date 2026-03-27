from __future__ import annotations


SUPPORTED_SCENARIOS = {
    "baseline",
    "winner_takes_all",
    "fake_winner_collapse",
}


def run_simulation_scenario(name: str, context: dict) -> dict:
    if name not in SUPPORTED_SCENARIOS:
        raise ValueError("Unsupported simulation scenario")

    if name == "baseline":
        return {**context, "scenario": name}

    if name == "winner_takes_all":
        value = context.get("value", 0)
        return {**context, "scenario": name, "value": value * 1.2}

    value = context.get("value", 0)
    return {**context, "scenario": name, "value": value * 0.7, "collapse_detected": True}
