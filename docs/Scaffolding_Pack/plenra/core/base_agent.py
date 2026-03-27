from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class AgentResult:
    agent_name: str
    status: str
    summary: str
    payload: dict[str, Any] = field(default_factory=dict)


class BaseAgent:
    agent_name = "base_agent"
    mission = "Execute deterministic Plenra work."

    def run(self, context: dict[str, Any]) -> AgentResult:
        raise NotImplementedError("Agent must implement run().")
