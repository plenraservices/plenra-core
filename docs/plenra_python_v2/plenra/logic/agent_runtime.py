from __future__ import annotations

from typing import Any

from plenra.agents import AGENT_REGISTRY


def run_agent(agent_key: str, context: dict[str, Any]) -> dict[str, Any]:
    agent_cls = AGENT_REGISTRY[agent_key]
    agent = agent_cls()
    result = agent.run(context)
    return {
        "agent_name": result.agent_name,
        "status": result.status,
        "summary": result.summary,
        "payload": result.payload,
    }
