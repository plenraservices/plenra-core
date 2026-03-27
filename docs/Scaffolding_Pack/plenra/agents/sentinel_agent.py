from __future__ import annotations

from plenra.core.base_agent import AgentResult, BaseAgent


class SentinelAgent(BaseAgent):
    agent_name = "sentinel_agent"
    mission = "Detect loopholes, undefined variables, and silent-loss risk."

    def run(self, context: dict) -> AgentResult:
        return AgentResult(
            agent_name=self.agent_name,
            status="ok",
            summary="Sentinel scaffold executed.",
            payload={
                "mission": self.mission,
                "received_keys": sorted(context.keys()),
            },
        )
