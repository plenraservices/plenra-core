from __future__ import annotations

from plenra.core.base_agent import AgentResult, BaseAgent


class VPAnalyticsAgent(BaseAgent):
    agent_name = "vp_analytics_agent"
    prompt_key = "vp_analytics_agent"
    mission = "Measure signals, KPIs, kill rules, and scale rules."

    def run(self, context: dict) -> AgentResult:
        return AgentResult(
            agent_name=self.agent_name,
            status="ok",
            summary="Analytics scaffold executed.",
            payload={
                "mission": self.mission,
                "prompt": self.get_prompt(),
                "received_keys": sorted(context.keys()),
            },
        )
